"""Pattern Mining Agent - Discover patterns in glyph sequences."""

import json
from pathlib import Path
from typing import Optional

from ..base import BaseAgent, LLMCache, LLMProvider
from .ngram_analyzer import NgramAnalyzer, NgramPattern
from .structural_patterns import StructuralPatternAnalyzer, StructuralPattern
from .visual_clustering import GlyphFeatures, VisualClusterAnalyzer, VisualCluster


class PatternMiningAgent(BaseAgent):
    """
    Pattern mining agent for Rongorongo analysis.

    Discovers patterns through:
    - N-gram sequence analysis
    - Structural position patterns
    - Visual similarity clustering
    """

    AGENT_NAME = "pattern_mining"
    VERSION = "1.0.0"

    def __init__(
        self,
        llm_provider: LLMProvider,
        cache: Optional[LLMCache] = None,
    ):
        """
        Initialize the pattern mining agent.

        Args:
            llm_provider: LLM provider for pattern interpretation
            cache: Optional response cache
        """
        super().__init__(llm_provider, cache)
        self.ngram_analyzer = NgramAnalyzer(llm_provider)
        self.structural_analyzer = StructuralPatternAnalyzer(llm_provider)
        self.visual_analyzer = VisualClusterAnalyzer(llm_provider)

    def get_input_schema(self) -> dict:
        """Get input schema for pattern mining agent."""
        return {
            "type": "object",
            "required": ["glyph_lexicon"],
            "properties": {
                "glyph_lexicon": {
                    "type": "object",
                    "description": "Rongorongo lexicon from glyph_cataloger",
                    "properties": {
                        "clusters": {"type": "array"},
                        "sequences": {"type": "array"},
                    },
                },
                "glyph_features": {
                    "type": "object",
                    "description": "Map of glyph_id to visual features",
                },
                "glyph_images": {
                    "type": "object",
                    "description": "Map of glyph_id to base64 image data",
                },
                "max_ngram": {
                    "type": "integer",
                    "default": 5,
                    "description": "Maximum n-gram size to analyze",
                },
                "min_pattern_frequency": {
                    "type": "integer",
                    "default": 2,
                    "description": "Minimum frequency for pattern inclusion",
                },
                "similarity_threshold": {
                    "type": "number",
                    "default": 0.7,
                    "description": "Threshold for visual clustering",
                },
            },
        }

    def get_output_schema(self) -> dict:
        """Get output schema for pattern mining agent."""
        return {
            "type": "object",
            "properties": {
                "run_metadata": {"type": "object"},
                "ngram_patterns": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "pattern_id": {"type": "string"},
                            "sequence": {"type": "array"},
                            "frequency": {"type": "integer"},
                            "llm_hypothesis": {"type": "string"},
                        },
                    },
                },
                "structural_patterns": {"type": "array"},
                "visual_clusters": {"type": "array"},
                "statistics": {"type": "object"},
            },
        }

    def run(self, input_data: dict) -> dict:
        """
        Execute pattern mining analysis.

        Args:
            input_data: Contains glyph_lexicon and optional features/images

        Returns:
            Discovered patterns with LLM interpretations
        """
        lexicon = input_data["glyph_lexicon"]
        glyph_features = input_data.get("glyph_features", {})
        glyph_images = input_data.get("glyph_images", {})
        max_ngram = input_data.get("max_ngram", 5)
        min_freq = input_data.get("min_pattern_frequency", 2)
        sim_threshold = input_data.get("similarity_threshold", 0.7)

        # Extract sequences from lexicon
        sequences = self._extract_sequences(lexicon)

        # N-gram analysis
        ngram_patterns = self._analyze_ngrams(
            sequences, max_ngram, min_freq
        )

        # Structural pattern analysis
        structural_patterns = self._analyze_structure(sequences, min_freq)

        # Visual clustering
        visual_clusters = self._analyze_visual_similarity(
            lexicon, glyph_features, glyph_images, sim_threshold
        )

        # Compile statistics
        statistics = self._compile_statistics(
            sequences, ngram_patterns, structural_patterns, visual_clusters
        )

        return {
            "ngram_patterns": [self._pattern_to_dict(p) for p in ngram_patterns],
            "structural_patterns": [
                self._structural_to_dict(p) for p in structural_patterns
            ],
            "visual_clusters": [self._cluster_to_dict(c) for c in visual_clusters],
            "statistics": statistics,
        }

    def _extract_sequences(self, lexicon: dict) -> list[dict]:
        """Extract glyph sequences from lexicon."""
        sequences = []

        # Check for explicit sequences
        if "sequences" in lexicon:
            for seq in lexicon["sequences"]:
                sequences.append({
                    "sequence": seq.get("glyph_ids", []),
                    "source": seq.get("source", "unknown"),
                })

        # Or reconstruct from clusters with position data
        elif "clusters" in lexicon:
            # Group by line/tablet
            lines_by_source: dict[str, list[tuple[float, str]]] = {}

            for cluster in lexicon["clusters"]:
                cluster_id = cluster.get("cluster_id", "")
                positions = cluster.get("positions", {})

                for pos in positions.get("instances", []):
                    source = pos.get("tablet", "unknown")
                    line = pos.get("line", 0)
                    position = pos.get("position_in_line", 0)

                    key = f"{source}_line{line}"
                    if key not in lines_by_source:
                        lines_by_source[key] = []
                    lines_by_source[key].append((position, cluster_id))

            # Sort each line by position
            for key, glyphs in lines_by_source.items():
                glyphs.sort(key=lambda x: x[0])
                sequences.append({
                    "sequence": [g[1] for g in glyphs],
                    "source": key.split("_")[0],
                })

        return sequences

    def _analyze_ngrams(
        self,
        sequences: list[dict],
        max_n: int,
        min_freq: int,
    ) -> list[NgramPattern]:
        """Run n-gram analysis."""
        if not sequences:
            return []

        patterns = self.ngram_analyzer.find_patterns(
            sequences, max_n=max_n, min_frequency=min_freq
        )

        # Get LLM interpretations for top patterns
        if patterns:
            patterns = self.ngram_analyzer.interpret_patterns(patterns, top_k=10)

        return patterns

    def _analyze_structure(
        self,
        sequences: list[dict],
        min_freq: int,
    ) -> list[StructuralPattern]:
        """Run structural pattern analysis."""
        if not sequences:
            return []

        lines = [s["sequence"] for s in sequences]
        patterns = self.structural_analyzer.find_all_patterns(lines, min_freq)

        # Get LLM interpretations
        if patterns:
            patterns = self.structural_analyzer.interpret_patterns(patterns)

        return patterns

    def _analyze_visual_similarity(
        self,
        lexicon: dict,
        features_data: dict,
        images: dict,
        threshold: float,
    ) -> list[VisualCluster]:
        """Run visual similarity clustering."""
        # Build feature objects
        features = []

        for cluster in lexicon.get("clusters", []):
            cluster_id = cluster.get("cluster_id", "")

            if cluster_id in features_data:
                feat = features_data[cluster_id]
                features.append(
                    GlyphFeatures(
                        glyph_id=cluster_id,
                        hu_moments=feat.get("hu_moments", [0] * 7),
                        aspect_ratio=feat.get("aspect_ratio", 1.0),
                        fill_ratio=feat.get("fill_ratio", 0.5),
                        contour_count=feat.get("contour_count", 1),
                        stroke_orientation=feat.get("stroke_orientation", 0.0),
                    )
                )
            elif "features" in cluster:
                # Use features from lexicon
                feat = cluster["features"]
                features.append(
                    GlyphFeatures(
                        glyph_id=cluster_id,
                        hu_moments=feat.get("hu_moments", [0] * 7),
                        aspect_ratio=feat.get("aspect_ratio", 1.0),
                        fill_ratio=feat.get("fill_ratio", 0.5),
                        contour_count=feat.get("contour_count", 1),
                        stroke_orientation=feat.get("stroke_orientation", 0.0),
                    )
                )

        if not features:
            return []

        # Cluster glyphs
        clusters = self.visual_analyzer.cluster_glyphs(
            features, similarity_threshold=threshold
        )

        # Decode images for LLM analysis
        decoded_images = {}
        for glyph_id, img_data in images.items():
            decoded_images[glyph_id] = self._decode_image(img_data)

        # Get LLM analysis
        if clusters:
            clusters = self.visual_analyzer.analyze_clusters(
                clusters, decoded_images
            )

        return clusters

    def _decode_image(self, image_data: str) -> bytes:
        """Decode base64 image data."""
        import base64

        if image_data.startswith("data:"):
            image_data = image_data.split(",", 1)[1]
        return base64.b64decode(image_data)

    def _compile_statistics(
        self,
        sequences: list[dict],
        ngrams: list[NgramPattern],
        structural: list[StructuralPattern],
        visual: list[VisualCluster],
    ) -> dict:
        """Compile pattern statistics."""
        total_glyphs = sum(len(s["sequence"]) for s in sequences)
        unique_glyphs = len(set(
            g for s in sequences for g in s["sequence"]
        ))

        return {
            "input": {
                "total_sequences": len(sequences),
                "total_glyphs": total_glyphs,
                "unique_glyphs": unique_glyphs,
            },
            "ngram_patterns": {
                "total": len(ngrams),
                "with_hypothesis": sum(1 for p in ngrams if p.llm_hypothesis),
                "by_length": self._count_by_n(ngrams),
            },
            "structural_patterns": {
                "total": len(structural),
                "line_markers": sum(
                    1 for p in structural if p.pattern_type == "line_marker"
                ),
                "repetitions": sum(
                    1 for p in structural if p.pattern_type == "repetition"
                ),
            },
            "visual_clusters": {
                "total": len(visual),
                "avg_cluster_size": (
                    sum(len(c.glyph_ids) for c in visual) / len(visual)
                    if visual
                    else 0
                ),
                "with_analysis": sum(1 for c in visual if c.llm_analysis),
            },
        }

    def _count_by_n(self, patterns: list[NgramPattern]) -> dict[int, int]:
        """Count patterns by n-gram length."""
        counts: dict[int, int] = {}
        for p in patterns:
            counts[p.n] = counts.get(p.n, 0) + 1
        return counts

    def _pattern_to_dict(self, pattern: NgramPattern) -> dict:
        """Convert NgramPattern to dictionary."""
        return {
            "pattern_id": pattern.pattern_id,
            "sequence": pattern.sequence,
            "n": pattern.n,
            "frequency": pattern.frequency,
            "probability": pattern.probability,
            "positions": pattern.positions,
            "tablets": pattern.tablets,
            "llm_hypothesis": pattern.llm_hypothesis,
        }

    def _structural_to_dict(self, pattern: StructuralPattern) -> dict:
        """Convert StructuralPattern to dictionary."""
        return {
            "pattern_id": pattern.pattern_id,
            "pattern_type": pattern.pattern_type,
            "glyph_ids": pattern.glyph_ids,
            "frequency": pattern.frequency,
            "position_preference": pattern.position_preference,
            "context": pattern.context,
            "llm_interpretation": pattern.llm_interpretation,
        }

    def _cluster_to_dict(self, cluster: VisualCluster) -> dict:
        """Convert VisualCluster to dictionary."""
        return {
            "cluster_id": cluster.cluster_id,
            "glyph_ids": cluster.glyph_ids,
            "centroid_glyph": cluster.centroid_glyph,
            "avg_similarity": cluster.avg_similarity,
            "shared_features": cluster.shared_features,
            "llm_analysis": cluster.llm_analysis,
        }


def save_results(results: dict, output_path: str) -> None:
    """Save pattern mining results to JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
