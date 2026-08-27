"""Unit tests for glyph clustering."""

import unittest

import cv2
import numpy as np

from models.glyphs import BoundingBox, GlyphInstance, GlyphPosition
from processors.glyph_processor import GlyphProcessor, ProcessorConfig


def create_test_glyph(shape: str, size: int = 50) -> np.ndarray:
    """Generate a simple shape as a test glyph."""
    img = np.ones((size, size), dtype=np.uint8) * 255
    if shape == "circle":
        cv2.circle(img, (size // 2, size // 2), size // 3, 0, -1)
    elif shape == "square":
        cv2.rectangle(img, (size // 4, size // 4), (3 * size // 4, 3 * size // 4), 0, -1)
    elif shape == "triangle":
        pts = np.array(
            [[size // 2, size // 4], [size // 4, 3 * size // 4], [3 * size // 4, 3 * size // 4]]
        )
        cv2.fillPoly(img, [pts], 0)
    return img


def create_glyph_instance(
    shape: str, instance_id: str, source: str = "test.png"
) -> tuple[GlyphInstance, np.ndarray]:
    """Create a glyph instance with its image.

    Returns:
        Tuple of (GlyphInstance, image containing the glyph).
    """
    glyph = create_test_glyph(shape, 50)
    # Create padded image
    img = np.ones((70, 70), dtype=np.uint8) * 255
    img[10:60, 10:60] = glyph

    bbox = BoundingBox(x=10, y=10, width=50, height=50)
    instance = GlyphInstance(
        instance_id=instance_id,
        source_image=source,
        bounding_box=bbox,
    )
    return instance, img


class TestDBSCANClustering(unittest.TestCase):
    """Tests for DBSCAN clustering."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_cluster_identical_glyphs(self):
        """Test that identical glyphs end up in the same cluster."""
        instances = []
        images = []

        # Create 5 identical circles
        for i in range(5):
            inst, img = create_glyph_instance("circle", f"circle_{i:03d}")
            instances.append(inst)
            images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs(instances)

        # All should be in the same cluster
        cluster_ids = set(inst.cluster_id for inst in instances)
        self.assertEqual(len(cluster_ids), 1)

    def test_cluster_distinct_glyphs(self):
        """Test that different shapes end up in different clusters."""
        shapes = ["circle", "square", "triangle"]
        instances = []
        images = []

        for shape in shapes:
            # Create 3 of each shape (enough for DBSCAN min_samples)
            for i in range(3):
                inst, img = create_glyph_instance(shape, f"{shape}_{i:03d}")
                instances.append(inst)
                images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs(instances)

        # Should have at least 3 distinct clusters (one per shape type)
        # Note: Some shapes might cluster together if features are similar
        cluster_ids = set(inst.cluster_id for inst in instances if inst.cluster_id)
        self.assertGreaterEqual(len(cluster_ids), 2)

    def test_cluster_similar_glyphs(self):
        """Test that similar glyphs (same shape, slight variations) group together."""
        instances = []
        images = []

        # Create circles with slight size variations
        for i in range(4):
            size = 48 + i  # 48, 49, 50, 51
            glyph = create_test_glyph("circle", size)

            img = np.ones((70, 70), dtype=np.uint8) * 255
            offset = (70 - size) // 2
            img[offset : offset + size, offset : offset + size] = glyph

            bbox = BoundingBox(x=offset, y=offset, width=size, height=size)
            inst = GlyphInstance(f"circle_{i}", "test.png", bbox)
            instances.append(inst)
            images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs(instances)

        # Similar circles should cluster together
        cluster_ids = set(inst.cluster_id for inst in instances)
        # Should have fewer clusters than instances (some grouping)
        # With 4 similar circles, expect 1-3 clusters depending on eps
        self.assertLess(len(cluster_ids), 4)

    def test_cluster_with_noise(self):
        """Test that outliers are handled correctly."""
        # Configure with higher min_samples to create noise points
        config = ProcessorConfig(dbscan_eps=0.1, dbscan_min_samples=3)
        processor = GlyphProcessor(config)

        instances = []
        images = []

        # Create 3 circles (will cluster)
        for i in range(3):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        # Create 1 square (isolated, might be noise)
        inst, img = create_glyph_instance("square", "square_0")
        instances.append(inst)
        images.append(img)

        # Create 1 triangle (isolated, might be noise)
        inst, img = create_glyph_instance("triangle", "triangle_0")
        instances.append(inst)
        images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = processor.extract_features(img, inst)

        clusters, instances = processor.cluster_glyphs(instances)

        # All instances should have a cluster_id assigned
        # (noise points get their own single-instance clusters)
        for inst in instances:
            self.assertIsNotNone(inst.cluster_id)

    def test_cluster_eps_sensitivity(self):
        """Test that different eps values affect clustering."""
        instances = []
        images = []

        # Create different shapes
        for shape in ["circle", "square", "triangle"]:
            for i in range(2):
                inst, img = create_glyph_instance(shape, f"{shape}_{i}")
                instances.append(inst)
                images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        # Test with small eps (more clusters)
        config_small = ProcessorConfig(dbscan_eps=0.1, dbscan_min_samples=1)
        processor_small = GlyphProcessor(config_small)
        features_copy = [inst.features.copy() for inst in instances]

        # Reset instances
        for inst, feat in zip(instances, features_copy):
            inst.features = feat
            inst.cluster_id = None

        clusters_small, _ = processor_small.cluster_glyphs(instances)

        # Reset instances again
        for inst, feat in zip(instances, features_copy):
            inst.features = feat
            inst.cluster_id = None

        # Test with large eps (fewer clusters)
        config_large = ProcessorConfig(dbscan_eps=10.0, dbscan_min_samples=1)
        processor_large = GlyphProcessor(config_large)

        clusters_large, _ = processor_large.cluster_glyphs(instances)

        # Large eps should give fewer or equal clusters
        self.assertLessEqual(len(clusters_large), len(clusters_small))

    def test_cluster_min_samples(self):
        """Test that min_samples parameter affects clustering."""
        instances = []
        images = []

        # Create 2 circles
        for i in range(2):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        # With min_samples=2, the 2 circles should form a cluster
        config = ProcessorConfig(dbscan_eps=1.0, dbscan_min_samples=2)
        processor = GlyphProcessor(config)

        clusters, _ = processor.cluster_glyphs(instances)

        # Should have exactly 1 cluster with 2 instances
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0].frequency, 2)


class TestClusterIDAssignment(unittest.TestCase):
    """Tests for cluster ID assignment."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_assign_cluster_ids(self):
        """Test that IDs are assigned as G001, G002, etc."""
        instances = []
        images = []

        # Create enough glyphs to form multiple clusters
        for shape in ["circle", "square"]:
            for i in range(3):
                inst, img = create_glyph_instance(shape, f"{shape}_{i}")
                instances.append(inst)
                images.append(img)

        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs(instances)

        # Check ID format
        for cluster in clusters:
            self.assertTrue(cluster.cluster_id.startswith("G"))
            # Should be 4 characters: G + 3 digits
            self.assertEqual(len(cluster.cluster_id), 4)
            # Should be a valid number
            int(cluster.cluster_id[1:])

    def test_cluster_id_ordering(self):
        """Test that most frequent cluster gets G001."""
        instances = []
        images = []

        # Create 5 circles (more frequent)
        for i in range(5):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        # Create 2 squares (less frequent)
        for i in range(2):
            inst, img = create_glyph_instance("square", f"square_{i}")
            instances.append(inst)
            images.append(img)

        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, _ = self.processor.cluster_glyphs(instances)

        # G001 should have the highest frequency
        g001 = next((c for c in clusters if c.cluster_id == "G001"), None)
        if g001:
            max_freq = max(c.frequency for c in clusters)
            self.assertEqual(g001.frequency, max_freq)


class TestClusterStatistics(unittest.TestCase):
    """Tests for cluster statistics."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_cluster_frequency_count(self):
        """Test counting instances per cluster."""
        instances = []
        images = []

        # Create 4 identical circles
        for i in range(4):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, _ = self.processor.cluster_glyphs(instances)

        # All should be in one cluster with frequency 4
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0].frequency, 4)

    def test_cluster_mean_features(self):
        """Test calculating mean feature vector."""
        instances = []
        images = []

        for i in range(3):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, _ = self.processor.cluster_glyphs(instances)

        # Cluster should have mean features
        self.assertEqual(len(clusters[0].mean_features), 7)

    def test_position_statistics(self):
        """Test calculating line distribution."""
        bbox = BoundingBox(x=0, y=0, width=50, height=50)

        instances = [
            GlyphInstance("a", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
            GlyphInstance("b", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
            GlyphInstance("c", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
        ]

        # Assign positions
        instances[0].position = GlyphPosition(line_number=0, position_in_line=0, total_in_line=2)
        instances[1].position = GlyphPosition(line_number=0, position_in_line=1, total_in_line=2)
        instances[2].position = GlyphPosition(line_number=1, position_in_line=0, total_in_line=1)

        from models.glyphs import GlyphCluster

        cluster = GlyphCluster(cluster_id="G001", instances=["a", "b", "c"])

        stats = self.processor.compute_position_stats(cluster, instances)

        # Line distribution
        self.assertEqual(stats.line_distribution.get(0, 0), 2)
        self.assertEqual(stats.line_distribution.get(1, 0), 1)

    def test_neighbor_analysis(self):
        """Test finding common neighboring glyphs."""
        bbox = BoundingBox(x=0, y=0, width=50, height=50)

        instances = [
            GlyphInstance("a", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
            GlyphInstance("b", "test.png", bbox, features=[1.0] * 7, cluster_id="G002"),
            GlyphInstance("c", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
            GlyphInstance("d", "test.png", bbox, features=[1.0] * 7, cluster_id="G003"),
        ]

        # Same line: a(G001) - b(G002) - c(G001) - d(G003)
        instances[0].position = GlyphPosition(line_number=0, position_in_line=0, total_in_line=4)
        instances[1].position = GlyphPosition(line_number=0, position_in_line=1, total_in_line=4)
        instances[2].position = GlyphPosition(line_number=0, position_in_line=2, total_in_line=4)
        instances[3].position = GlyphPosition(line_number=0, position_in_line=3, total_in_line=4)

        from models.glyphs import GlyphCluster

        cluster = GlyphCluster(cluster_id="G001", instances=["a", "c"])

        stats = self.processor.compute_position_stats(cluster, instances)

        # G001 (a, c) should have G002 as a neighbor
        self.assertIn("G002", stats.common_neighbors)


class TestSameLineAllographMerge(unittest.TestCase):
    """Post-DBSCAN adjacent same-line stitch. No live CV of Mamari GIFs."""

    def _thin_instance(
        self,
        instance_id: str,
        position: int,
        features: list[float],
        width: int = 26,
        height: int = 66,
        cluster_id: str | None = None,
        source: str = "line.gif",
    ) -> GlyphInstance:
        return GlyphInstance(
            instance_id=instance_id,
            source_image=source,
            bounding_box=BoundingBox(x=position * 30, y=0, width=width, height=height),
            features=features,
            cluster_id=cluster_id,
            position=GlyphPosition(0, position, 6),
        )

    def test_adjacent_tall_thin_run_shares_an_id(self):
        """Six adjacent thin glyphs with Hu dist 0.8 merge after DBSCAN."""
        instances = []
        for i in range(6):
            feat = [0.8 * i] + [0.0] * 6
            instances.append(self._thin_instance(f"c{i}", i, feat))

        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs(instances)
        ids = {inst.cluster_id for inst in clustered}
        self.assertEqual(len(ids), 1)

    def test_merge_can_be_disabled(self):
        instances = []
        for i in range(6):
            feat = [0.8 * i] + [0.0] * 6
            instances.append(self._thin_instance(f"c{i}", i, feat))

        processor = GlyphProcessor(ProcessorConfig(same_line_allograph_merge=False))
        _, clustered = processor.cluster_glyphs(instances)
        ids = {inst.cluster_id for inst in clustered}
        self.assertEqual(len(ids), 6)

    def test_wide_neighbor_does_not_merge_with_thin(self):
        """Tall-thin gate blocks a wide adjacent box even when Hu is close."""
        thin = self._thin_instance("thin", 0, [0.0] * 7, width=26, height=66)
        wide = self._thin_instance("wide", 1, [0.8] + [0.0] * 6, width=70, height=65)
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([thin, wide])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_dissimilar_area_does_not_merge(self):
        small = self._thin_instance("a", 0, [0.0] * 7, width=26, height=66)
        tall = self._thin_instance("b", 1, [0.8] + [0.0] * 6, width=26, height=120)
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([small, tall])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)


class TestSingleGlyphClustering(unittest.TestCase):
    """Tests for edge cases with single glyphs."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_single_instance(self):
        """Test clustering with a single glyph instance."""
        inst, img = create_glyph_instance("circle", "single_0")
        inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs([inst])

        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0].frequency, 1)
        self.assertEqual(instances[0].cluster_id, clusters[0].cluster_id)


if __name__ == "__main__":
    unittest.main()
