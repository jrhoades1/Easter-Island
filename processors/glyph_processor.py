"""Computer vision processor for Rongorongo glyph detection and analysis."""

import os
from dataclasses import dataclass
from typing import Optional

import cv2
import numpy as np
from sklearn.cluster import DBSCAN

from models.glyphs import (
    BoundingBox,
    GlyphCluster,
    GlyphInstance,
    GlyphPosition,
    PositionStats,
)


@dataclass
class ProcessorConfig:
    """Configuration for the glyph processor."""

    # Preprocessing
    blur_kernel_size: int = 5
    adaptive_block_size: int = 11
    adaptive_c: int = 2

    # Contour filtering
    min_contour_area: int = 100
    max_contour_area: int = 50000
    min_aspect_ratio: float = 0.2
    max_aspect_ratio: float = 5.0

    # Bounding box
    bbox_padding: int = 5

    # Line detection
    line_merge_threshold: int = 20  # Vertical distance to merge into same line

    # Feature extraction
    target_glyph_size: tuple[int, int] = (64, 64)
    # "unsigned": abs of signed log-Hu so Hu5–Hu7 sign-flips do not split types.
    # "signed": cycle-1 path (−sign(h)·log10(|h|)). Detection is unchanged either way.
    hu_sign_mode: str = "unsigned"

    # Clustering
    dbscan_eps: float = 0.5
    dbscan_min_samples: int = 2


class GlyphProcessor:
    """Processes images to detect, extract, and cluster Rongorongo glyphs."""

    def __init__(self, config: Optional[ProcessorConfig] = None):
        """Initialize the processor with optional configuration."""
        self.config = config or ProcessorConfig()

    # =========================================================================
    # Image Loading and Preprocessing
    # =========================================================================

    def load_image(self, image_path: str) -> Optional[np.ndarray]:
        """Load an image from file path.

        Args:
            image_path: Path to the image file.

        Returns:
            Image as numpy array, or None if loading fails.
        """
        if not os.path.exists(image_path):
            return None
        img = cv2.imread(image_path)
        if img is None:
            return None
        return img

    def convert_grayscale(self, image: np.ndarray) -> np.ndarray:
        """Convert image to grayscale.

        Args:
            image: Input image (color or grayscale).

        Returns:
            Grayscale image.
        """
        if len(image.shape) == 2:
            return image
        if len(image.shape) == 3 and image.shape[2] == 1:
            return image.squeeze()
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def apply_threshold(self, image: np.ndarray) -> np.ndarray:
        """Apply adaptive thresholding to binarize the image.

        Args:
            image: Grayscale input image.

        Returns:
            Binary image.
        """
        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            self.config.adaptive_block_size,
            self.config.adaptive_c,
        )

    def denoise(self, image: np.ndarray) -> np.ndarray:
        """Apply denoising to the image.

        Args:
            image: Input image.

        Returns:
            Denoised image.
        """
        return cv2.GaussianBlur(
            image,
            (self.config.blur_kernel_size, self.config.blur_kernel_size),
            0,
        )

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """Full preprocessing pipeline.

        Args:
            image: Input image.

        Returns:
            Preprocessed binary image ready for contour detection.
        """
        gray = self.convert_grayscale(image)
        denoised = self.denoise(gray)
        binary = self.apply_threshold(denoised)
        return binary

    # =========================================================================
    # Glyph Detection
    # =========================================================================

    def find_contours(self, binary_image: np.ndarray) -> list[np.ndarray]:
        """Find contours in binary image.

        Args:
            binary_image: Preprocessed binary image.

        Returns:
            List of contours.
        """
        contours, _ = cv2.findContours(
            binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        return list(contours)

    def filter_contours(self, contours: list[np.ndarray]) -> list[np.ndarray]:
        """Filter contours by area and aspect ratio.

        Args:
            contours: List of contours to filter.

        Returns:
            Filtered list of contours.
        """
        filtered = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < self.config.min_contour_area:
                continue
            if area > self.config.max_contour_area:
                continue

            x, y, w, h = cv2.boundingRect(contour)
            if h == 0:
                continue
            aspect_ratio = w / h
            if aspect_ratio < self.config.min_aspect_ratio:
                continue
            if aspect_ratio > self.config.max_aspect_ratio:
                continue

            filtered.append(contour)
        return filtered

    def contour_to_bounding_box(
        self, contour: np.ndarray, image_shape: tuple[int, ...]
    ) -> BoundingBox:
        """Convert a contour to a bounding box with padding.

        Args:
            contour: OpenCV contour.
            image_shape: Shape of the source image for boundary clamping.

        Returns:
            BoundingBox with padding applied.
        """
        x, y, w, h = cv2.boundingRect(contour)
        padding = self.config.bbox_padding

        # Apply padding with boundary clamping
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = min(image_shape[1] - x, w + 2 * padding)
        h = min(image_shape[0] - y, h + 2 * padding)

        return BoundingBox(x=x, y=y, width=w, height=h)

    def detect_glyphs(
        self, image: np.ndarray, source_image: str
    ) -> list[GlyphInstance]:
        """Detect glyphs in an image.

        Args:
            image: Input image.
            source_image: Filename of the source image.

        Returns:
            List of detected GlyphInstance objects.
        """
        binary = self.preprocess(image)
        contours = self.find_contours(binary)
        filtered = self.filter_contours(contours)

        instances = []
        for i, contour in enumerate(filtered):
            bbox = self.contour_to_bounding_box(contour, image.shape)
            instance_id = GlyphInstance.generate_id(source_image, i)
            instances.append(
                GlyphInstance(
                    instance_id=instance_id,
                    source_image=source_image,
                    bounding_box=bbox,
                )
            )

        return instances

    # =========================================================================
    # Line Detection and Position Assignment
    # =========================================================================

    def detect_lines(self, instances: list[GlyphInstance]) -> list[list[GlyphInstance]]:
        """Group glyph instances into lines based on vertical position.

        Args:
            instances: List of detected glyph instances.

        Returns:
            List of lines, where each line is a list of instances.
        """
        if not instances:
            return []

        # Sort by vertical center position
        sorted_instances = sorted(
            instances, key=lambda g: g.bounding_box.center[1]
        )

        lines: list[list[GlyphInstance]] = []
        current_line: list[GlyphInstance] = []
        current_y = -1000  # Start with impossible value

        for instance in sorted_instances:
            center_y = instance.bounding_box.center[1]
            if abs(center_y - current_y) > self.config.line_merge_threshold:
                # Start a new line
                if current_line:
                    lines.append(current_line)
                current_line = [instance]
                current_y = center_y
            else:
                current_line.append(instance)
                # Update current_y to average of line
                current_y = sum(g.bounding_box.center[1] for g in current_line) / len(
                    current_line
                )

        if current_line:
            lines.append(current_line)

        # Sort each line left to right
        for line in lines:
            line.sort(key=lambda g: g.bounding_box.center[0])

        return lines

    def assign_positions(self, instances: list[GlyphInstance]) -> list[GlyphInstance]:
        """Assign line numbers and positions to glyph instances.

        Args:
            instances: List of detected glyph instances.

        Returns:
            Same instances with position information added.
        """
        lines = self.detect_lines(instances)

        for line_num, line in enumerate(lines):
            total = len(line)
            for pos, instance in enumerate(line):
                instance.position = GlyphPosition(
                    line_number=line_num,
                    position_in_line=pos,
                    total_in_line=total,
                )

        # Flatten back to list
        return [inst for line in lines for inst in line]

    # =========================================================================
    # Feature Extraction
    # =========================================================================

    def extract_glyph_image(
        self, image: np.ndarray, bbox: BoundingBox
    ) -> np.ndarray:
        """Extract and normalize a glyph image from the source.

        Args:
            image: Source image.
            bbox: Bounding box of the glyph.

        Returns:
            Normalized glyph image.
        """
        # Extract region
        roi = image[bbox.y : bbox.y + bbox.height, bbox.x : bbox.x + bbox.width]

        # Convert to grayscale if needed
        if len(roi.shape) == 3:
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Resize to target size
        resized = cv2.resize(roi, self.config.target_glyph_size)

        return resized

    def compute_hu_moments(self, glyph_image: np.ndarray) -> list[float]:
        """Compute Hu moments for a glyph image.

        Args:
            glyph_image: Normalized glyph image.

        Returns:
            List of 7 log-Hu values. Default is unsigned (abs of the
            signed log-Hu). Pass hu_sign_mode="signed" for the cycle-1
            −sign(h)·log10(|h|) path.
        """
        # Ensure binary
        _, binary = cv2.threshold(glyph_image, 127, 255, cv2.THRESH_BINARY)

        moments = cv2.moments(binary)
        hu_moments = cv2.HuMoments(moments).flatten()

        # Signed log transform (cycle-1). Unsigned takes abs so Hu5–Hu7
        # sign-flips do not inflate Euclidean distance.
        signed_log_hu = []
        for h in hu_moments:
            if h != 0:
                signed_log_hu.append(float(-np.sign(h) * np.log10(abs(h))))
            else:
                signed_log_hu.append(0.0)

        mode = self.config.hu_sign_mode
        if mode == "unsigned":
            return [abs(v) for v in signed_log_hu]
        if mode == "signed":
            return signed_log_hu
        raise ValueError(
            f"hu_sign_mode must be 'unsigned' or 'signed', got {mode!r}"
        )

    def extract_features(
        self, image: np.ndarray, instance: GlyphInstance
    ) -> list[float]:
        """Extract feature vector for a glyph instance.

        Args:
            image: Source image.
            instance: Glyph instance to extract features for.

        Returns:
            Feature vector.
        """
        glyph_img = self.extract_glyph_image(image, instance.bounding_box)
        hu_moments = self.compute_hu_moments(glyph_img)
        return hu_moments

    def extract_features_batch(
        self, image: np.ndarray, instances: list[GlyphInstance]
    ) -> list[GlyphInstance]:
        """Extract features for multiple glyph instances.

        Args:
            image: Source image.
            instances: List of glyph instances.

        Returns:
            Same instances with features added.
        """
        for instance in instances:
            instance.features = self.extract_features(image, instance)
        return instances

    # =========================================================================
    # Clustering
    # =========================================================================

    def cluster_glyphs(
        self, instances: list[GlyphInstance]
    ) -> tuple[list[GlyphCluster], list[GlyphInstance]]:
        """Cluster glyph instances by visual similarity.

        Args:
            instances: List of glyph instances with features.

        Returns:
            Tuple of (clusters, instances with cluster_id assigned).
        """
        if not instances:
            return [], []

        # Build feature matrix
        features = np.array([inst.features for inst in instances])

        # Handle single instance case
        if len(instances) == 1:
            cluster_id = GlyphCluster.generate_id(1)
            instances[0].cluster_id = cluster_id
            cluster = GlyphCluster(
                cluster_id=cluster_id,
                instances=[instances[0].instance_id],
                mean_features=instances[0].features,
            )
            return [cluster], instances

        # Run DBSCAN
        clustering = DBSCAN(
            eps=self.config.dbscan_eps,
            min_samples=self.config.dbscan_min_samples,
            metric="euclidean",
        )
        labels = clustering.fit_predict(features)

        # Group instances by cluster
        cluster_map: dict[int, list[GlyphInstance]] = {}
        noise_instances: list[GlyphInstance] = []

        for instance, label in zip(instances, labels):
            if label == -1:
                noise_instances.append(instance)
            else:
                if label not in cluster_map:
                    cluster_map[label] = []
                cluster_map[label].append(instance)

        # Create GlyphCluster objects, sorted by frequency (most common first)
        sorted_labels = sorted(cluster_map.keys(), key=lambda label: -len(cluster_map[label]))
        clusters = []

        for i, label in enumerate(sorted_labels):
            cluster_instances = cluster_map[label]
            cluster_id = GlyphCluster.generate_id(i + 1)

            # Assign cluster_id to instances
            for inst in cluster_instances:
                inst.cluster_id = cluster_id

            # Calculate mean features
            mean_features = np.mean(
                [inst.features for inst in cluster_instances], axis=0
            ).tolist()

            cluster = GlyphCluster(
                cluster_id=cluster_id,
                instances=[inst.instance_id for inst in cluster_instances],
                mean_features=mean_features,
            )
            clusters.append(cluster)

        # Handle noise points - each becomes its own cluster
        for i, inst in enumerate(noise_instances):
            cluster_id = GlyphCluster.generate_id(len(clusters) + i + 1)
            inst.cluster_id = cluster_id
            cluster = GlyphCluster(
                cluster_id=cluster_id,
                instances=[inst.instance_id],
                mean_features=inst.features,
            )
            clusters.append(cluster)

        return clusters, instances

    # =========================================================================
    # Position Statistics
    # =========================================================================

    def compute_position_stats(
        self,
        cluster: GlyphCluster,
        all_instances: list[GlyphInstance],
    ) -> PositionStats:
        """Compute position statistics for a cluster.

        Args:
            cluster: The cluster to compute stats for.
            all_instances: All instances (for neighbor analysis).

        Returns:
            PositionStats for the cluster.
        """
        # Get instances for this cluster
        cluster_instances = [
            inst for inst in all_instances if inst.cluster_id == cluster.cluster_id
        ]

        stats = PositionStats()

        # Line distribution
        for inst in cluster_instances:
            if inst.position:
                line = inst.position.line_number
                stats.line_distribution[line] = stats.line_distribution.get(line, 0) + 1

        # Average position in line
        positions = []
        for inst in cluster_instances:
            if inst.position and inst.position.total_in_line > 0:
                relative_pos = inst.position.position_in_line / inst.position.total_in_line
                positions.append(relative_pos)
        if positions:
            stats.avg_position_in_line = sum(positions) / len(positions)

        # Common neighbors (simplified - just count adjacent cluster IDs)
        neighbor_counts: dict[str, int] = {}
        for inst in cluster_instances:
            if inst.position:
                # Find neighbors in same line
                for other in all_instances:
                    if other.instance_id == inst.instance_id:
                        continue
                    if other.position and other.position.line_number == inst.position.line_number:
                        if abs(other.position.position_in_line - inst.position.position_in_line) == 1:
                            if other.cluster_id:
                                neighbor_counts[other.cluster_id] = (
                                    neighbor_counts.get(other.cluster_id, 0) + 1
                                )

        # Top 5 neighbors
        sorted_neighbors = sorted(neighbor_counts.items(), key=lambda x: -x[1])
        stats.common_neighbors = [n[0] for n in sorted_neighbors[:5]]

        return stats

    # =========================================================================
    # Glyph Image Saving
    # =========================================================================

    def save_glyph_image(
        self,
        image: np.ndarray,
        instance: GlyphInstance,
        output_dir: str,
    ) -> str:
        """Save an extracted glyph image to disk.

        Args:
            image: Source image.
            instance: Glyph instance to save.
            output_dir: Directory to save to.

        Returns:
            Path to saved image.
        """
        os.makedirs(output_dir, exist_ok=True)

        glyph_img = self.extract_glyph_image(image, instance.bounding_box)
        filename = f"{instance.instance_id}.png"
        filepath = os.path.join(output_dir, filename)

        cv2.imwrite(filepath, glyph_img)
        instance.image_path = filepath
        return filepath

    def save_representative_image(
        self,
        cluster: GlyphCluster,
        all_instances: list[GlyphInstance],
        images: dict[str, np.ndarray],
        output_dir: str,
    ) -> str:
        """Save a representative image for a cluster.

        Args:
            cluster: The cluster.
            all_instances: All glyph instances.
            images: Dict mapping source filenames to loaded images.
            output_dir: Directory to save to.

        Returns:
            Path to saved representative image.
        """
        os.makedirs(output_dir, exist_ok=True)

        # Find the first instance in this cluster
        for inst in all_instances:
            if inst.instance_id in cluster.instances:
                if inst.source_image in images:
                    image = images[inst.source_image]
                    glyph_img = self.extract_glyph_image(image, inst.bounding_box)
                    filename = f"{cluster.cluster_id}_representative.png"
                    filepath = os.path.join(output_dir, filename)
                    cv2.imwrite(filepath, glyph_img)
                    cluster.representative_image = filepath
                    return filepath

        return ""


def instances_to_line_sequences(instances: list[GlyphInstance]) -> list[list[str]]:
    """Map clustered cataloger instances to cluster-id sequences in reading order.

    Groups by (source_image, line_number) and sorts each group by
    position_in_line. Emits G00n IDs as assigned by cluster_glyphs.
    Does not remap those IDs to Barthel stems.

    PatternMiningAgent._extract_sequences is not the cataloger hook: it
    reads a lexicon dict with clusters[].positions.instances, which
    RongorongoLexicon.to_dict() does not emit. The real fields are on
    GlyphInstance.position and GlyphInstance.cluster_id.
    """
    buckets: dict[tuple[str, int], list[tuple[int, str]]] = {}
    for inst in instances:
        if inst.position is None or not inst.cluster_id:
            continue
        key = (inst.source_image, inst.position.line_number)
        buckets.setdefault(key, []).append(
            (inst.position.position_in_line, inst.cluster_id)
        )

    sequences: list[list[str]] = []
    for key in sorted(buckets):
        ordered = sorted(buckets[key], key=lambda item: item[0])
        sequences.append([cluster_id for _, cluster_id in ordered])
    return sequences
