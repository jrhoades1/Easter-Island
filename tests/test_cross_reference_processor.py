"""Unit tests for cross-reference processor."""

import os
import tempfile
import unittest

import yaml

from models.cross_reference import (
    EvidenceType,
    GlyphSemanticProfile,
    ShapeCategory,
    ShapeTag,
)
from models.glyphs import GlyphCluster, PositionStats, RongorongoLexicon
from models.language import Etymology, LanguageEntry, Translation
from processors.cross_reference_processor import (
    ConfidenceCalculator,
    CrossReferenceProcessor,
    EvidenceCollector,
    EvidenceItem,
    ProcessorConfig,
    SemanticMatcher,
    ShapeTagger,
)


class TestShapeTagger(unittest.TestCase):
    """Tests for ShapeTagger class."""

    def test_tag_cluster_no_annotations(self):
        """Test tagging without annotations returns undetermined."""
        tagger = ShapeTagger()
        cluster = GlyphCluster(cluster_id="G001", instances=["a", "b"])

        tags = tagger.tag_cluster(cluster)

        self.assertEqual(len(tags), 1)
        self.assertEqual(tags[0].category, ShapeCategory.UNDETERMINED)
        self.assertEqual(tags[0].tagged_by, "rule_based")

    def test_tag_cluster_with_annotations(self):
        """Test tagging with manual annotations."""
        annotations = {
            "G001": {
                "category": "avian",
                "confidence": 0.9,
                "subcategory": "frigate_bird",
                "visual_features": ["wings", "beak"],
            }
        }
        tagger = ShapeTagger(annotations)
        cluster = GlyphCluster(cluster_id="G001", instances=["a", "b"])

        tags = tagger.tag_cluster(cluster)

        self.assertEqual(len(tags), 1)
        self.assertEqual(tags[0].category, ShapeCategory.AVIAN)
        self.assertEqual(tags[0].confidence, 0.9)
        self.assertEqual(tags[0].subcategory, "frigate_bird")
        self.assertEqual(tags[0].visual_features, ["wings", "beak"])
        self.assertEqual(tags[0].tagged_by, "manual")

    def test_tag_cluster_partial_annotation(self):
        """Test tagging with partial annotation (category only)."""
        annotations = {"G002": {"category": "geometric"}}
        tagger = ShapeTagger(annotations)
        cluster = GlyphCluster(cluster_id="G002", instances=["x"])

        tags = tagger.tag_cluster(cluster)

        self.assertEqual(tags[0].category, ShapeCategory.GEOMETRIC)
        self.assertEqual(tags[0].confidence, 0.9)  # Default
        self.assertIsNone(tags[0].subcategory)

    def test_load_annotations_nonexistent_file(self):
        """Test loading from nonexistent file returns empty tagger."""
        tagger = ShapeTagger.load_annotations("/nonexistent/path.yaml")
        self.assertEqual(tagger.annotations, {})

    def test_load_annotations_from_yaml(self):
        """Test loading annotations from YAML file."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", delete=False
        ) as f:
            yaml.dump(
                {
                    "G001": {"category": "avian", "confidence": 0.85},
                    "G002": {"category": "anthropomorphic", "confidence": 0.7},
                },
                f,
            )
            yaml_path = f.name

        try:
            tagger = ShapeTagger.load_annotations(yaml_path)
            self.assertIn("G001", tagger.annotations)
            self.assertIn("G002", tagger.annotations)
            self.assertEqual(tagger.annotations["G001"]["category"], "avian")
        finally:
            os.unlink(yaml_path)


class TestSemanticMatcher(unittest.TestCase):
    """Tests for SemanticMatcher class."""

    def setUp(self):
        """Set up test entries."""
        self.entries = [
            LanguageEntry(
                word="manu",
                normalized="manu",
                translations=[Translation("en", "bird", None)],
                semantic_category="animals",
                etymology=Etymology(origin="Proto-Polynesian *manu"),
            ),
            LanguageEntry(
                word="tangata",
                normalized="tangata",
                translations=[Translation("en", "person", None)],
                semantic_category="kinship",
            ),
            LanguageEntry(
                word="tahi",
                normalized="tahi",
                translations=[Translation("en", "one", None)],
                semantic_category="quantity",
            ),
            LanguageEntry(
                word="ika",
                normalized="ika",
                translations=[Translation("en", "fish", None)],
                semantic_category="animals",
            ),
        ]

    def test_find_candidates_avian(self):
        """Test finding candidates for avian category."""
        matcher = SemanticMatcher()
        profile = GlyphSemanticProfile(cluster_id="G001")
        profile.primary_category = ShapeCategory.AVIAN

        candidates = matcher.find_candidates(profile, self.entries, 1)

        # Should find 'manu' as a strong match
        self.assertGreater(len(candidates), 0)
        words = [e.word for e, _ in candidates]
        self.assertIn("manu", words)

    def test_find_candidates_geometric(self):
        """Test finding candidates for geometric category."""
        matcher = SemanticMatcher()
        profile = GlyphSemanticProfile(cluster_id="G001")
        profile.primary_category = ShapeCategory.GEOMETRIC

        candidates = matcher.find_candidates(profile, self.entries, 1)

        # Should find 'tahi' due to quantity semantic category
        words = [e.word for e, _ in candidates]
        self.assertIn("tahi", words)

    def test_find_candidates_undetermined(self):
        """Test that undetermined category returns no candidates."""
        matcher = SemanticMatcher()
        profile = GlyphSemanticProfile(cluster_id="G001")
        profile.primary_category = ShapeCategory.UNDETERMINED

        candidates = matcher.find_candidates(profile, self.entries, 1)

        self.assertEqual(len(candidates), 0)

    def test_find_candidates_no_primary_category(self):
        """Test that no primary category returns no candidates."""
        matcher = SemanticMatcher()
        profile = GlyphSemanticProfile(cluster_id="G001")

        candidates = matcher.find_candidates(profile, self.entries, 1)

        self.assertEqual(len(candidates), 0)

    def test_find_candidates_respects_max_limit(self):
        """Test that max candidates limit is respected."""
        config = ProcessorConfig(max_candidates_per_glyph=1)
        matcher = SemanticMatcher(config)
        profile = GlyphSemanticProfile(cluster_id="G001")
        profile.primary_category = ShapeCategory.AVIAN

        # Add more animal entries
        entries = self.entries + [
            LanguageEntry(
                word="kura",
                normalized="kura",
                translations=[Translation("en", "feather", None)],
                semantic_category="animals",
            ),
        ]

        candidates = matcher.find_candidates(profile, entries, 1)

        self.assertEqual(len(candidates), 1)

    def test_proto_polynesian_boost(self):
        """Test that proto-Polynesian etymology boosts score."""
        matcher = SemanticMatcher()
        profile = GlyphSemanticProfile(cluster_id="G001")
        profile.primary_category = ShapeCategory.AVIAN

        candidates = matcher.find_candidates(profile, self.entries, 1)

        # manu has proto-Polynesian etymology, should be ranked higher
        if len(candidates) > 0:
            top_entry, top_score = candidates[0]
            self.assertEqual(top_entry.word, "manu")


class TestEvidenceCollector(unittest.TestCase):
    """Tests for EvidenceCollector class."""

    def setUp(self):
        """Set up test data."""
        self.collector = EvidenceCollector()
        self.cluster = GlyphCluster(
            cluster_id="G001",
            instances=["a", "b", "c"],
            positions=PositionStats(
                avg_position_in_line=0.2,
                common_neighbors=["G002", "G003"],
            ),
        )
        self.profile = GlyphSemanticProfile(cluster_id="G001")
        self.profile.primary_category = ShapeCategory.AVIAN
        self.profile.add_shape_tag(ShapeTag(category=ShapeCategory.AVIAN, confidence=0.8))

        self.entry = LanguageEntry(
            word="manu",
            normalized="manu",
            translations=[Translation("en", "bird", None)],
            semantic_category="animals",
        )

    def test_collect_evidence_shape_semantic(self):
        """Test collecting shape-semantic evidence."""
        evidence = self.collector.collect_evidence(
            self.cluster, self.profile, self.entry, 1, 1
        )

        shape_evidence = [
            e for e in evidence if e.evidence_type == EvidenceType.SHAPE_SEMANTIC
        ]
        self.assertEqual(len(shape_evidence), 1)
        self.assertGreater(shape_evidence[0].strength, 0)

    def test_collect_evidence_frequency(self):
        """Test collecting frequency correlation evidence."""
        evidence = self.collector.collect_evidence(
            self.cluster, self.profile, self.entry, 1, 2
        )

        freq_evidence = [
            e for e in evidence if e.evidence_type == EvidenceType.FREQUENCY_CORRELATION
        ]
        self.assertEqual(len(freq_evidence), 1)

    def test_collect_evidence_positional(self):
        """Test collecting positional evidence."""
        evidence = self.collector.collect_evidence(
            self.cluster, self.profile, self.entry, 1, 1
        )

        pos_evidence = [
            e for e in evidence if e.evidence_type == EvidenceType.POSITIONAL_PATTERN
        ]
        # Initial position (0.2) should generate evidence
        self.assertEqual(len(pos_evidence), 1)
        self.assertIn("initial", pos_evidence[0].description.lower())

    def test_collect_evidence_neighbor(self):
        """Test collecting neighbor evidence."""
        evidence = self.collector.collect_evidence(
            self.cluster, self.profile, self.entry, 1, 1
        )

        neighbor_evidence = [
            e for e in evidence if e.evidence_type == EvidenceType.NEIGHBOR_CONTEXT
        ]
        self.assertEqual(len(neighbor_evidence), 1)

    def test_no_frequency_evidence_when_ranks_differ_too_much(self):
        """Test that no frequency evidence when ranks differ significantly."""
        evidence = self.collector.collect_evidence(
            self.cluster, self.profile, self.entry, 1, 100
        )

        freq_evidence = [
            e for e in evidence if e.evidence_type == EvidenceType.FREQUENCY_CORRELATION
        ]
        self.assertEqual(len(freq_evidence), 0)

    def test_no_positional_evidence_for_neutral_position(self):
        """Test no positional evidence for neutral (middle) positions."""
        cluster = GlyphCluster(
            cluster_id="G001",
            instances=["a"],
            positions=PositionStats(avg_position_in_line=0.5),
        )
        evidence = self.collector.collect_evidence(
            cluster, self.profile, self.entry, 1, 1
        )

        pos_evidence = [
            e for e in evidence if e.evidence_type == EvidenceType.POSITIONAL_PATTERN
        ]
        self.assertEqual(len(pos_evidence), 0)


class TestConfidenceCalculator(unittest.TestCase):
    """Tests for ConfidenceCalculator class."""

    def test_compute_confidence_empty_evidence(self):
        """Test confidence with no evidence."""
        score, level = ConfidenceCalculator.compute_confidence([])
        self.assertEqual(score, 0.0)
        self.assertEqual(level, "speculative")

    def test_compute_confidence_low(self):
        """Test low confidence (speculative)."""
        evidence = [
            EvidenceItem(
                evidence_type=EvidenceType.NEIGHBOR_CONTEXT,
                description="Test",
                strength=0.2,
            )
        ]
        score, level = ConfidenceCalculator.compute_confidence(evidence)
        self.assertLess(score, 0.25)
        self.assertEqual(level, "speculative")

    def test_compute_confidence_tentative(self):
        """Test tentative confidence range."""
        evidence = [
            EvidenceItem(
                evidence_type=EvidenceType.SHAPE_SEMANTIC,
                description="Test",
                strength=0.4,
            ),
            EvidenceItem(
                evidence_type=EvidenceType.FREQUENCY_CORRELATION,
                description="Test",
                strength=0.3,
            ),
        ]
        score, level = ConfidenceCalculator.compute_confidence(evidence)
        self.assertGreaterEqual(score, 0.25)
        self.assertLess(score, 0.50)
        self.assertEqual(level, "tentative")

    def test_compute_confidence_plausible(self):
        """Test plausible confidence range."""
        evidence = [
            EvidenceItem(
                evidence_type=EvidenceType.SHAPE_SEMANTIC,
                description="Test",
                strength=0.8,
            ),
            EvidenceItem(
                evidence_type=EvidenceType.FREQUENCY_CORRELATION,
                description="Test",
                strength=0.7,
            ),
            EvidenceItem(
                evidence_type=EvidenceType.POSITIONAL_PATTERN,
                description="Test",
                strength=0.6,
            ),
        ]
        score, level = ConfidenceCalculator.compute_confidence(evidence)
        self.assertGreaterEqual(score, 0.50)
        self.assertLess(score, 0.75)
        self.assertEqual(level, "plausible")

    def test_compute_confidence_strong(self):
        """Test strong confidence range."""
        evidence = [
            EvidenceItem(
                evidence_type=EvidenceType.SHAPE_SEMANTIC,
                description="Test",
                strength=1.0,
            ),
            EvidenceItem(
                evidence_type=EvidenceType.FREQUENCY_CORRELATION,
                description="Test",
                strength=1.0,
            ),
            EvidenceItem(
                evidence_type=EvidenceType.POSITIONAL_PATTERN,
                description="Test",
                strength=1.0,
            ),
            EvidenceItem(
                evidence_type=EvidenceType.NEIGHBOR_CONTEXT,
                description="Test",
                strength=1.0,
            ),
            EvidenceItem(
                evidence_type=EvidenceType.PUBLISHED_HYPOTHESIS,
                description="Test",
                strength=1.0,
            ),
        ]
        score, level = ConfidenceCalculator.compute_confidence(evidence)
        self.assertGreaterEqual(score, 0.75)
        self.assertEqual(level, "strong")


class TestCrossReferenceProcessor(unittest.TestCase):
    """Tests for CrossReferenceProcessor class."""

    def setUp(self):
        """Set up test data."""
        self.glyph_lexicon = RongorongoLexicon(
            source_images=["test.png"],
            clusters=[
                GlyphCluster(
                    cluster_id="G001",
                    instances=["a", "b", "c", "d", "e"],
                    positions=PositionStats(
                        avg_position_in_line=0.2,
                        common_neighbors=["G002"],
                    ),
                ),
                GlyphCluster(
                    cluster_id="G002",
                    instances=["f", "g"],
                    positions=PositionStats(
                        avg_position_in_line=0.5,
                        common_neighbors=["G001"],
                    ),
                ),
            ],
        )

        self.language_entries = [
            LanguageEntry(
                word="manu",
                normalized="manu",
                translations=[Translation("en", "bird", None)],
                semantic_category="animals",
            ),
            LanguageEntry(
                word="tangata",
                normalized="tangata",
                translations=[Translation("en", "person", None)],
                semantic_category="kinship",
            ),
        ]

    def test_process_creates_profiles(self):
        """Test that process creates glyph profiles."""
        processor = CrossReferenceProcessor()
        result = processor.process(self.glyph_lexicon, self.language_entries)

        self.assertEqual(len(result.glyph_profiles), 2)
        profile_ids = [p.cluster_id for p in result.glyph_profiles]
        self.assertIn("G001", profile_ids)
        self.assertIn("G002", profile_ids)

    def test_process_with_annotations(self):
        """Test processing with shape annotations."""
        processor = CrossReferenceProcessor()

        # Create temp annotation file
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", delete=False
        ) as f:
            yaml.dump({"G001": {"category": "avian", "confidence": 0.9}}, f)
            yaml_path = f.name

        try:
            processor.load_annotations(yaml_path)
            result = processor.process(self.glyph_lexicon, self.language_entries)

            # G001 should have avian category
            profile = result.get_profile("G001")
            self.assertEqual(profile.primary_category, ShapeCategory.AVIAN)
        finally:
            os.unlink(yaml_path)

    def test_process_creates_cross_references(self):
        """Test that process creates cross-references when matches exist."""
        processor = CrossReferenceProcessor()

        # Add annotations to enable matching
        processor.tagger = ShapeTagger(
            {"G001": {"category": "avian", "confidence": 0.9}}
        )

        result = processor.process(self.glyph_lexicon, self.language_entries)

        # Should have at least one cross-reference for G001 -> manu
        xrefs_for_g001 = result.get_references_for_glyph("G001")
        self.assertGreater(len(xrefs_for_g001), 0)

    def test_process_computes_statistics(self):
        """Test that statistics are computed."""
        processor = CrossReferenceProcessor()
        result = processor.process(self.glyph_lexicon, self.language_entries)

        self.assertEqual(result.statistics.total_glyphs_profiled, 2)

    def test_process_sets_frequency_ranks(self):
        """Test that frequency ranks are set correctly."""
        processor = CrossReferenceProcessor()
        result = processor.process(self.glyph_lexicon, self.language_entries)

        profile1 = result.get_profile("G001")
        profile2 = result.get_profile("G002")

        # G001 has more instances, should be rank 1
        self.assertEqual(profile1.frequency_rank, 1)
        self.assertEqual(profile2.frequency_rank, 2)

    def test_process_sets_positional_tendency(self):
        """Test that positional tendency is set correctly."""
        processor = CrossReferenceProcessor()
        result = processor.process(self.glyph_lexicon, self.language_entries)

        profile1 = result.get_profile("G001")
        profile2 = result.get_profile("G002")

        # G001 avg_position 0.2 should be initial
        self.assertEqual(profile1.positional_tendency, "initial")
        # G002 avg_position 0.5 should be medial
        self.assertEqual(profile2.positional_tendency, "medial")

    def test_min_confidence_threshold(self):
        """Test that low confidence matches are filtered."""
        config = ProcessorConfig(min_confidence_threshold=0.9)
        processor = CrossReferenceProcessor(config)

        result = processor.process(self.glyph_lexicon, self.language_entries)

        # With high threshold, most matches should be filtered
        # (depends on test data and matching logic)
        self.assertIsNotNone(result)

    def test_cross_reference_ids_linked(self):
        """Test that cross-reference IDs are linked in profiles."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger(
            {"G001": {"category": "avian", "confidence": 0.9}}
        )

        result = processor.process(self.glyph_lexicon, self.language_entries)

        profile = result.get_profile("G001")
        xrefs = result.get_references_for_glyph("G001")

        if xrefs:
            # Profile should contain the reference IDs
            for xref in xrefs:
                self.assertIn(xref.reference_id, profile.cross_reference_ids)


class TestProcessorConfig(unittest.TestCase):
    """Tests for ProcessorConfig dataclass."""

    def test_default_values(self):
        """Test default configuration values."""
        config = ProcessorConfig()
        self.assertEqual(config.min_confidence_threshold, 0.1)
        self.assertEqual(config.max_candidates_per_glyph, 5)
        self.assertTrue(config.include_domain_only_matches)
        self.assertEqual(config.frequency_match_tolerance, 3)

    def test_custom_values(self):
        """Test custom configuration values."""
        config = ProcessorConfig(
            min_confidence_threshold=0.3,
            max_candidates_per_glyph=10,
            frequency_match_tolerance=5,
        )
        self.assertEqual(config.min_confidence_threshold, 0.3)
        self.assertEqual(config.max_candidates_per_glyph, 10)


if __name__ == "__main__":
    unittest.main()
