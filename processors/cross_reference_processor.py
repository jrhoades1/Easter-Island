"""Processor for creating symbolic cross-references between glyphs and linguistic roots."""

import os
from dataclasses import dataclass
from typing import Optional

import yaml

from config import (
    CONFIDENCE_LEVELS,
    EVIDENCE_WEIGHTS,
    SHAPE_SEMANTIC_MAPPING,
)
from models.cross_reference import (
    CrossReference,
    CrossReferenceLexicon,
    EvidenceItem,
    EvidenceType,
    GlyphSemanticProfile,
    ShapeCategory,
    ShapeTag,
)
from models.glyphs import GlyphCluster, RongorongoLexicon
from models.language import LanguageEntry


@dataclass
class ProcessorConfig:
    """Configuration for the cross-reference processor."""

    # Minimum confidence to create a cross-reference
    min_confidence_threshold: float = 0.1

    # Maximum candidates per glyph
    max_candidates_per_glyph: int = 5

    # Whether to include shape-only matches (no specific word match)
    include_domain_only_matches: bool = True

    # Frequency matching settings
    frequency_match_tolerance: int = 3  # Rank difference tolerance


class ShapeTagger:
    """Assigns shape category tags to glyph clusters."""

    def __init__(self, annotations: Optional[dict] = None):
        """Initialize with optional manual annotations.

        Args:
            annotations: Dictionary mapping cluster_id to annotation dict
        """
        self.annotations = annotations or {}

    @classmethod
    def load_annotations(cls, yaml_path: str) -> "ShapeTagger":
        """Load shape annotations from a YAML file.

        Args:
            yaml_path: Path to the YAML annotations file

        Returns:
            ShapeTagger with loaded annotations
        """
        if not os.path.exists(yaml_path):
            return cls()

        with open(yaml_path, "r", encoding="utf-8") as f:
            annotations = yaml.safe_load(f) or {}

        return cls(annotations)

    def tag_cluster(self, cluster: GlyphCluster) -> list[ShapeTag]:
        """Assign shape tags to a glyph cluster.

        Args:
            cluster: The glyph cluster to tag

        Returns:
            List of ShapeTag assignments
        """
        tags = []

        # Check for manual annotation
        if cluster.cluster_id in self.annotations:
            ann = self.annotations[cluster.cluster_id]
            category = ShapeCategory(ann.get("category", "undetermined"))
            tags.append(
                ShapeTag(
                    category=category,
                    confidence=ann.get("confidence", 0.9),
                    subcategory=ann.get("subcategory"),
                    visual_features=ann.get("visual_features", []),
                    tagged_by="manual",
                )
            )
        else:
            # Default: undetermined with low confidence
            tags.append(
                ShapeTag(
                    category=ShapeCategory.UNDETERMINED,
                    confidence=0.3,
                    tagged_by="rule_based",
                )
            )

        return tags


class SemanticMatcher:
    """Matches glyph shape categories to linguistic entries."""

    def __init__(self, config: Optional[ProcessorConfig] = None):
        """Initialize the semantic matcher.

        Args:
            config: Processor configuration
        """
        self.config = config or ProcessorConfig()

    def find_candidates(
        self,
        profile: GlyphSemanticProfile,
        entries: list[LanguageEntry],
        glyph_rank: int,
    ) -> list[tuple[LanguageEntry, float]]:
        """Find candidate language entries for a glyph profile.

        Args:
            profile: The glyph's semantic profile
            entries: Available language entries
            glyph_rank: The glyph's frequency rank (1 = most frequent)

        Returns:
            List of (entry, base_score) tuples sorted by score
        """
        if not profile.primary_category:
            return []

        category_name = profile.primary_category.value
        mapping = SHAPE_SEMANTIC_MAPPING.get(category_name, {})

        if not mapping:
            return []

        target_categories = mapping.get("semantic_categories", [])
        target_words = mapping.get("rapa_nui_words", [])

        # If no target categories or words defined, return no candidates
        if not target_categories and not target_words:
            return []

        candidates = []

        for entry in entries:
            score = 0.0

            # Check direct word match
            if entry.normalized in [w.lower() for w in target_words]:
                score += 0.5

            # Check semantic category match
            if entry.semantic_category and entry.semantic_category.lower() in [
                c.lower() for c in target_categories
            ]:
                score += 0.3

            # Check etymology for proto-Polynesian connection (only if already matched)
            if score > 0 and entry.etymology and entry.etymology.origin:
                if "proto" in entry.etymology.origin.lower():
                    score += 0.2

            if score > 0:
                candidates.append((entry, score))

        # Sort by score descending
        candidates.sort(key=lambda x: x[1], reverse=True)

        # Return top candidates
        return candidates[: self.config.max_candidates_per_glyph]


class EvidenceCollector:
    """Collects and evaluates evidence for cross-references."""

    def __init__(self, config: Optional[ProcessorConfig] = None):
        """Initialize the evidence collector.

        Args:
            config: Processor configuration
        """
        self.config = config or ProcessorConfig()

    def collect_evidence(
        self,
        cluster: GlyphCluster,
        profile: GlyphSemanticProfile,
        entry: LanguageEntry,
        glyph_rank: int,
        word_rank: int,
    ) -> list[EvidenceItem]:
        """Collect all evidence items for a glyph-word association.

        Args:
            cluster: The glyph cluster
            profile: The glyph's semantic profile
            entry: The language entry candidate
            glyph_rank: Frequency rank of the glyph
            word_rank: Frequency rank of the word (if applicable)

        Returns:
            List of evidence items
        """
        evidence = []

        # 1. Shape-semantic evidence
        shape_evidence = self._evaluate_shape_semantic(profile, entry)
        if shape_evidence:
            evidence.append(shape_evidence)

        # 2. Frequency correlation evidence
        freq_evidence = self._evaluate_frequency(glyph_rank, word_rank)
        if freq_evidence:
            evidence.append(freq_evidence)

        # 3. Positional pattern evidence
        pos_evidence = self._evaluate_positional(cluster, entry)
        if pos_evidence:
            evidence.append(pos_evidence)

        # 4. Neighbor context evidence
        neighbor_evidence = self._evaluate_neighbors(cluster, profile)
        if neighbor_evidence:
            evidence.append(neighbor_evidence)

        return evidence

    def _evaluate_shape_semantic(
        self, profile: GlyphSemanticProfile, entry: LanguageEntry
    ) -> Optional[EvidenceItem]:
        """Evaluate shape-semantic evidence."""
        if not profile.primary_category:
            return None

        category_name = profile.primary_category.value
        mapping = SHAPE_SEMANTIC_MAPPING.get(category_name, {})

        if not mapping:
            return None

        target_words = [w.lower() for w in mapping.get("rapa_nui_words", [])]
        target_categories = [c.lower() for c in mapping.get("semantic_categories", [])]

        strength = 0.0
        description_parts = []

        # Direct word match
        if entry.normalized in target_words:
            strength += 0.6
            description_parts.append(f"'{entry.word}' in {category_name} word list")

        # Semantic category match
        if entry.semantic_category:
            entry_cat = entry.semantic_category.lower()
            if entry_cat in target_categories:
                strength += 0.4
                description_parts.append(
                    f"semantic category '{entry.semantic_category}' matches {category_name} domain"
                )

        if strength > 0:
            return EvidenceItem(
                evidence_type=EvidenceType.SHAPE_SEMANTIC,
                description=" and ".join(description_parts),
                strength=min(strength, 1.0),
                source="shape_semantic_mapping",
                data={
                    "category": category_name,
                    "word": entry.word,
                    "semantic_category": entry.semantic_category,
                },
            )

        return None

    def _evaluate_frequency(
        self, glyph_rank: int, word_rank: int
    ) -> Optional[EvidenceItem]:
        """Evaluate frequency correlation evidence."""
        if glyph_rank <= 0 or word_rank <= 0:
            return None

        rank_diff = abs(glyph_rank - word_rank)
        tolerance = self.config.frequency_match_tolerance

        if rank_diff <= tolerance:
            # Closer ranks = higher strength
            strength = max(0.2, 1.0 - (rank_diff / (tolerance + 1)) * 0.8)

            return EvidenceItem(
                evidence_type=EvidenceType.FREQUENCY_CORRELATION,
                description=f"Glyph rank {glyph_rank} correlates with word rank {word_rank}",
                strength=strength,
                source="frequency_analysis",
                data={"glyph_rank": glyph_rank, "word_rank": word_rank, "rank_diff": rank_diff},
            )

        return None

    def _evaluate_positional(
        self, cluster: GlyphCluster, entry: LanguageEntry
    ) -> Optional[EvidenceItem]:
        """Evaluate positional pattern evidence."""
        # Check if glyph tends toward certain positions
        avg_pos = cluster.positions.avg_position_in_line

        # Simplistic positional analysis
        tendency = "neutral"
        if avg_pos < 0.33:
            tendency = "initial"
        elif avg_pos > 0.66:
            tendency = "final"

        if tendency != "neutral":
            # This is speculative - would need actual positional data
            return EvidenceItem(
                evidence_type=EvidenceType.POSITIONAL_PATTERN,
                description=f"Glyph tends toward {tendency} position (avg: {avg_pos:.2f})",
                strength=0.3,
                source="positional_analysis",
                data={"avg_position": avg_pos, "tendency": tendency},
            )

        return None

    def _evaluate_neighbors(
        self, cluster: GlyphCluster, profile: GlyphSemanticProfile
    ) -> Optional[EvidenceItem]:
        """Evaluate neighbor context evidence."""
        neighbors = cluster.positions.common_neighbors

        if len(neighbors) >= 2:
            return EvidenceItem(
                evidence_type=EvidenceType.NEIGHBOR_CONTEXT,
                description=f"Commonly co-occurs with {', '.join(neighbors[:3])}",
                strength=0.2,
                source="neighbor_analysis",
                data={"neighbors": neighbors},
            )

        return None


class ConfidenceCalculator:
    """Calculates overall confidence scores and levels."""

    @staticmethod
    def compute_confidence(evidence: list[EvidenceItem]) -> tuple[float, str]:
        """Compute overall confidence from evidence items.

        Args:
            evidence: List of evidence items

        Returns:
            Tuple of (confidence_score, confidence_level)
        """
        if not evidence:
            return 0.0, "speculative"

        # Weighted sum of evidence
        total_score = 0.0
        total_weight = 0.0

        for item in evidence:
            weight = EVIDENCE_WEIGHTS.get(item.evidence_type.value, 0.1)
            total_score += item.strength * weight
            total_weight += weight

        if total_weight > 0:
            confidence = total_score / total_weight
        else:
            confidence = 0.0

        # Determine level
        level = "speculative"
        for level_name, (min_val, max_val) in CONFIDENCE_LEVELS.items():
            if min_val <= confidence < max_val:
                level = level_name
                break

        return round(confidence, 3), level


class CrossReferenceProcessor:
    """Main processor for creating cross-references between glyphs and language."""

    def __init__(self, config: Optional[ProcessorConfig] = None):
        """Initialize the processor.

        Args:
            config: Processor configuration
        """
        self.config = config or ProcessorConfig()
        self.tagger = ShapeTagger()
        self.matcher = SemanticMatcher(config)
        self.evidence_collector = EvidenceCollector(config)

    def load_annotations(self, yaml_path: str) -> None:
        """Load shape annotations from YAML file.

        Args:
            yaml_path: Path to annotations file
        """
        self.tagger = ShapeTagger.load_annotations(yaml_path)

    def process(
        self,
        glyph_lexicon: RongorongoLexicon,
        language_entries: list[LanguageEntry],
    ) -> CrossReferenceLexicon:
        """Process glyph and language data to create cross-references.

        Args:
            glyph_lexicon: The Rongorongo glyph lexicon
            language_entries: List of language entries

        Returns:
            Cross-reference lexicon with profiles and references
        """
        result = CrossReferenceLexicon()

        # Sort clusters by frequency for ranking
        sorted_clusters = sorted(
            glyph_lexicon.clusters, key=lambda c: c.frequency, reverse=True
        )

        # Create rank lookup
        cluster_ranks = {c.cluster_id: i + 1 for i, c in enumerate(sorted_clusters)}

        # Create word frequency ranking (by number of translations/examples)
        word_ranks = self._rank_words(language_entries)

        # Process each cluster
        xref_index = 1
        for cluster in glyph_lexicon.clusters:
            glyph_rank = cluster_ranks[cluster.cluster_id]

            # Create semantic profile
            profile = self._create_profile(cluster, glyph_rank)
            result.add_profile(profile)

            # Find and create cross-references
            candidates = self.matcher.find_candidates(
                profile, language_entries, glyph_rank
            )

            for entry, base_score in candidates:
                word_rank = word_ranks.get(entry.normalized, 0)

                # Collect evidence
                evidence = self.evidence_collector.collect_evidence(
                    cluster, profile, entry, glyph_rank, word_rank
                )

                if not evidence:
                    continue

                # Calculate confidence
                confidence, level = ConfidenceCalculator.compute_confidence(evidence)

                if confidence < self.config.min_confidence_threshold:
                    continue

                # Determine semantic domain
                domain = entry.semantic_category or "unknown"

                # Get proto-Polynesian root if available
                proto_root = None
                if entry.etymology and entry.etymology.origin:
                    if "proto" in entry.etymology.origin.lower():
                        proto_root = entry.etymology.origin

                # Create cross-reference
                xref = CrossReference(
                    reference_id=CrossReference.generate_id(xref_index),
                    glyph_cluster_id=cluster.cluster_id,
                    language_entry_word=entry.word,
                    language_entry_normalized=entry.normalized,
                    overall_confidence=confidence,
                    confidence_level=level,
                    evidence=evidence,
                    semantic_domain=domain,
                    proto_polynesian_root=proto_root,
                )

                result.add_cross_reference(xref)
                profile.cross_reference_ids.append(xref.reference_id)
                xref_index += 1

        # Compute statistics
        result.compute_statistics()

        return result

    def _create_profile(
        self, cluster: GlyphCluster, glyph_rank: int
    ) -> GlyphSemanticProfile:
        """Create a semantic profile for a glyph cluster.

        Args:
            cluster: The glyph cluster
            glyph_rank: Frequency rank of the cluster

        Returns:
            GlyphSemanticProfile for the cluster
        """
        tags = self.tagger.tag_cluster(cluster)

        profile = GlyphSemanticProfile(
            cluster_id=cluster.cluster_id,
            shape_tags=tags,
            frequency_rank=glyph_rank,
            frequency_count=cluster.frequency,
        )

        # Set primary category from highest confidence tag
        if tags:
            best_tag = max(tags, key=lambda t: t.confidence)
            profile.primary_category = best_tag.category

        # Determine positional tendency
        avg_pos = cluster.positions.avg_position_in_line
        if avg_pos < 0.33:
            profile.positional_tendency = "initial"
        elif avg_pos > 0.66:
            profile.positional_tendency = "final"
        else:
            profile.positional_tendency = "medial"

        return profile

    def _rank_words(self, entries: list[LanguageEntry]) -> dict[str, int]:
        """Rank words by their "importance" (translations, examples).

        Args:
            entries: List of language entries

        Returns:
            Dictionary mapping normalized word to rank
        """
        # Score by number of translations and examples
        scored = []
        for entry in entries:
            score = len(entry.translations) + len(entry.examples) * 2
            scored.append((entry.normalized, score))

        # Sort by score descending
        scored.sort(key=lambda x: x[1], reverse=True)

        # Create rank lookup
        return {word: i + 1 for i, (word, _) in enumerate(scored)}
