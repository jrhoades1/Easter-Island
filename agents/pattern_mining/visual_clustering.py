"""Visual clustering analysis for glyph similarity."""

from dataclasses import dataclass
from typing import Optional

import numpy as np

from ..base import LLMMessage, LLMProvider, LLMResponse


@dataclass
class VisualCluster:
    """A cluster of visually similar glyphs."""

    cluster_id: str
    glyph_ids: list[str]
    centroid_glyph: str  # Most representative glyph
    avg_similarity: float
    shared_features: list[str]
    llm_analysis: Optional[str] = None


@dataclass
class GlyphFeatures:
    """Visual features for a glyph."""

    glyph_id: str
    hu_moments: list[float]  # 7 Hu moments
    aspect_ratio: float
    fill_ratio: float  # Foreground/bounding box ratio
    contour_count: int
    stroke_orientation: float  # Dominant angle


class VisualClusterAnalyzer:
    """
    Analyzes visual similarity between glyphs.

    Uses Hu moments and other features to cluster similar glyphs,
    which may represent:
    - Variant forms of the same glyph
    - Phonetic variants
    - Contextual allographs
    """

    SYSTEM_PROMPT = """You are an expert in paleographic analysis and visual pattern recognition
for ancient scripts.

When analyzing clusters of visually similar Rongorongo glyphs, consider:
1. Are these variants of the same base glyph (like handwriting variations)?
2. Could they represent related but distinct meanings (like singular/plural)?
3. Might they be positional variants (different forms at start/end of words)?
4. Could visual similarity indicate phonetic similarity?

Known glyph categories in Rongorongo include:
- Bird forms (various species and orientations)
- Human figures (standing, seated, actions)
- Fish and marine life
- Plants and objects
- Geometric shapes

Provide analysis while acknowledging the script is undeciphered."""

    def __init__(self, llm_provider: Optional[LLMProvider] = None):
        """
        Initialize the visual cluster analyzer.

        Args:
            llm_provider: Optional LLM for cluster interpretation
        """
        self.llm = llm_provider

    def compute_similarity(
        self,
        features1: GlyphFeatures,
        features2: GlyphFeatures,
    ) -> float:
        """
        Compute similarity between two glyphs based on features.

        Args:
            features1: First glyph's features
            features2: Second glyph's features

        Returns:
            Similarity score 0.0 to 1.0
        """
        # Hu moment similarity (most important)
        hu1 = np.array(features1.hu_moments)
        hu2 = np.array(features2.hu_moments)

        # Use log scale for Hu moments (they vary widely)
        hu1_log = np.sign(hu1) * np.log10(np.abs(hu1) + 1e-10)
        hu2_log = np.sign(hu2) * np.log10(np.abs(hu2) + 1e-10)

        hu_distance = np.linalg.norm(hu1_log - hu2_log)
        hu_similarity = 1.0 / (1.0 + hu_distance)

        # Aspect ratio similarity
        ar_diff = abs(features1.aspect_ratio - features2.aspect_ratio)
        ar_similarity = 1.0 / (1.0 + ar_diff)

        # Fill ratio similarity
        fill_diff = abs(features1.fill_ratio - features2.fill_ratio)
        fill_similarity = 1.0 / (1.0 + fill_diff * 5)

        # Weighted combination
        similarity = (
            0.6 * hu_similarity + 0.2 * ar_similarity + 0.2 * fill_similarity
        )

        return similarity

    def build_similarity_matrix(
        self,
        all_features: list[GlyphFeatures],
    ) -> np.ndarray:
        """
        Build pairwise similarity matrix.

        Args:
            all_features: Features for all glyphs

        Returns:
            N x N similarity matrix
        """
        n = len(all_features)
        matrix = np.zeros((n, n))

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    matrix[i, j] = 1.0
                else:
                    sim = self.compute_similarity(all_features[i], all_features[j])
                    matrix[i, j] = sim
                    matrix[j, i] = sim

        return matrix

    def cluster_glyphs(
        self,
        all_features: list[GlyphFeatures],
        similarity_threshold: float = 0.7,
        min_cluster_size: int = 2,
    ) -> list[VisualCluster]:
        """
        Cluster glyphs by visual similarity.

        Uses hierarchical clustering based on similarity matrix.

        Args:
            all_features: Features for all glyphs
            similarity_threshold: Minimum similarity to cluster together
            min_cluster_size: Minimum glyphs per cluster

        Returns:
            List of visual clusters
        """
        if not all_features:
            return []

        n = len(all_features)
        similarity_matrix = self.build_similarity_matrix(all_features)

        # Simple agglomerative clustering
        clusters: list[set[int]] = [{i} for i in range(n)]
        glyph_to_cluster = list(range(n))

        # Merge similar glyphs
        for i in range(n):
            for j in range(i + 1, n):
                if similarity_matrix[i, j] >= similarity_threshold:
                    # Merge clusters
                    ci, cj = glyph_to_cluster[i], glyph_to_cluster[j]
                    if ci != cj:
                        clusters[ci].update(clusters[cj])
                        for k in clusters[cj]:
                            glyph_to_cluster[k] = ci
                        clusters[cj] = set()

        # Build cluster objects
        result = []
        cluster_id = 0

        for cluster_indices in clusters:
            if len(cluster_indices) >= min_cluster_size:
                cluster_id += 1
                indices = list(cluster_indices)

                # Find centroid (highest average similarity to others)
                best_centroid = indices[0]
                best_avg_sim = 0

                for i in indices:
                    avg_sim = np.mean(
                        [similarity_matrix[i, j] for j in indices if j != i]
                    )
                    if avg_sim > best_avg_sim:
                        best_avg_sim = avg_sim
                        best_centroid = i

                # Calculate cluster average similarity
                sims = []
                for i in indices:
                    for j in indices:
                        if i < j:
                            sims.append(similarity_matrix[i, j])
                avg_similarity = np.mean(sims) if sims else 1.0

                result.append(
                    VisualCluster(
                        cluster_id=f"vis_{cluster_id:03d}",
                        glyph_ids=[all_features[i].glyph_id for i in indices],
                        centroid_glyph=all_features[best_centroid].glyph_id,
                        avg_similarity=float(avg_similarity),
                        shared_features=self._identify_shared_features(
                            [all_features[i] for i in indices]
                        ),
                    )
                )

        return result

    def _identify_shared_features(
        self,
        features: list[GlyphFeatures],
    ) -> list[str]:
        """Identify features shared by cluster members."""
        shared = []

        # Aspect ratio
        aspects = [f.aspect_ratio for f in features]
        if max(aspects) - min(aspects) < 0.3:
            avg = sum(aspects) / len(aspects)
            if avg > 1.5:
                shared.append("wide_shape")
            elif avg < 0.7:
                shared.append("tall_shape")
            else:
                shared.append("square_shape")

        # Fill ratio
        fills = [f.fill_ratio for f in features]
        avg_fill = sum(fills) / len(fills)
        if avg_fill > 0.5:
            shared.append("dense_fill")
        else:
            shared.append("sparse_fill")

        # Contour count
        contours = [f.contour_count for f in features]
        avg_contours = sum(contours) / len(contours)
        if avg_contours > 3:
            shared.append("complex_shape")
        else:
            shared.append("simple_shape")

        return shared

    def analyze_clusters(
        self,
        clusters: list[VisualCluster],
        glyph_images: Optional[dict[str, bytes]] = None,
    ) -> list[VisualCluster]:
        """
        Use LLM to analyze visual clusters.

        Args:
            clusters: Clusters to analyze
            glyph_images: Optional map of glyph_id to image bytes

        Returns:
            Clusters with LLM analysis added
        """
        if not self.llm or not clusters:
            return clusters

        cluster_desc = "\n".join(
            f"- {c.cluster_id}: {len(c.glyph_ids)} glyphs ({', '.join(c.glyph_ids[:5])}), "
            f"features: {c.shared_features}, similarity: {c.avg_similarity:.2f}"
            for c in clusters[:10]
        )

        user_prompt = f"""Analyze these visual clusters of Rongorongo glyphs:

{cluster_desc}

For each cluster, suggest what the visual similarity might indicate
about the relationship between these glyphs.

Respond with JSON:
{{
    "analyses": [
        {{
            "cluster_id": "vis_001",
            "analysis": "your interpretation of what this cluster represents",
            "relationship_type": "variants|related_meanings|positional|coincidental"
        }}
    ]
}}"""

        messages = [
            LLMMessage(role="system", content=self.SYSTEM_PROMPT),
            LLMMessage(role="user", content=user_prompt),
        ]

        # Add images if available
        if glyph_images:
            images = []
            for cluster in clusters[:3]:  # Top 3 clusters
                centroid_id = cluster.centroid_glyph
                if centroid_id in glyph_images:
                    images.append(glyph_images[centroid_id])

            if images:
                messages[1].images = images

        response = self.llm.complete(messages, max_tokens=1000, temperature=0.2)

        self._apply_analyses(clusters, response)
        return clusters

    def _apply_analyses(
        self, clusters: list[VisualCluster], response: LLMResponse
    ) -> None:
        """Apply LLM analyses to clusters."""
        import json

        try:
            content = response.content.strip()
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])

            data = json.loads(content)

            analysis_map = {
                a["cluster_id"]: a["analysis"] for a in data.get("analyses", [])
            }

            for cluster in clusters:
                if cluster.cluster_id in analysis_map:
                    cluster.llm_analysis = analysis_map[cluster.cluster_id]

        except (json.JSONDecodeError, KeyError):
            pass
