"""Integration tests for the cross-reference system."""

import json
import os
import shutil
import tempfile
import unittest

import yaml

from models.cross_reference import CrossReferenceLexicon, ShapeCategory
from models.glyphs import GlyphCluster, PositionStats, RongorongoLexicon
from models.language import Etymology, LanguageEntry, Translation
from processors.cross_reference_processor import CrossReferenceProcessor, ShapeTagger


class TestEndToEndPipeline(unittest.TestCase):
    """End-to-end pipeline tests."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = os.path.join(self.temp_dir, "output")
        os.makedirs(self.output_dir)

    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.temp_dir)

    def _create_glyph_lexicon(self) -> RongorongoLexicon:
        """Create a test glyph lexicon."""
        return RongorongoLexicon(
            source_images=["tablet_a.png"],
            clusters=[
                GlyphCluster(
                    cluster_id="G001",
                    instances=["a1", "a2", "a3", "a4", "a5"],
                    positions=PositionStats(
                        avg_position_in_line=0.15,
                        common_neighbors=["G002", "G003"],
                    ),
                ),
                GlyphCluster(
                    cluster_id="G002",
                    instances=["b1", "b2", "b3"],
                    positions=PositionStats(
                        avg_position_in_line=0.5,
                        common_neighbors=["G001"],
                    ),
                ),
                GlyphCluster(
                    cluster_id="G003",
                    instances=["c1", "c2"],
                    positions=PositionStats(
                        avg_position_in_line=0.8,
                        common_neighbors=["G001", "G002"],
                    ),
                ),
            ],
        )

    def _create_language_entries(self) -> list[LanguageEntry]:
        """Create test language entries."""
        return [
            LanguageEntry(
                word="manu",
                normalized="manu",
                translations=[
                    Translation("en", "bird", None),
                    Translation("en", "flying creature", None),
                ],
                semantic_category="animals",
                etymology=Etymology(origin="Proto-Polynesian *manu"),
            ),
            LanguageEntry(
                word="manutara",
                normalized="manutara",
                translations=[Translation("en", "sooty tern", None)],
                semantic_category="animals",
            ),
            LanguageEntry(
                word="tangata",
                normalized="tangata",
                translations=[Translation("en", "person", None)],
                semantic_category="kinship",
                etymology=Etymology(origin="Proto-Polynesian *tangata"),
            ),
            LanguageEntry(
                word="tahi",
                normalized="tahi",
                translations=[Translation("en", "one", None)],
                semantic_category="quantity",
            ),
            LanguageEntry(
                word="rua",
                normalized="rua",
                translations=[Translation("en", "two", None)],
                semantic_category="quantity",
            ),
            LanguageEntry(
                word="ika",
                normalized="ika",
                translations=[Translation("en", "fish", None)],
                semantic_category="animals",
            ),
        ]

    def _create_annotations(self) -> dict:
        """Create test shape annotations."""
        return {
            "G001": {
                "category": "avian",
                "confidence": 0.9,
                "subcategory": "frigate_bird",
                "visual_features": ["wings", "forked_tail"],
            },
            "G002": {
                "category": "anthropomorphic",
                "confidence": 0.8,
                "visual_features": ["standing_figure"],
            },
            "G003": {
                "category": "geometric",
                "confidence": 0.7,
            },
        }

    def test_full_pipeline_without_annotations(self):
        """Test complete pipeline without manual annotations."""
        processor = CrossReferenceProcessor()
        glyph_lexicon = self._create_glyph_lexicon()
        language_entries = self._create_language_entries()

        result = processor.process(glyph_lexicon, language_entries)

        # Should create profiles for all glyphs
        self.assertEqual(len(result.glyph_profiles), 3)

        # All profiles should be undetermined without annotations
        for profile in result.glyph_profiles:
            self.assertEqual(profile.primary_category, ShapeCategory.UNDETERMINED)

    def test_full_pipeline_with_annotations(self):
        """Test complete pipeline with manual annotations."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger(self._create_annotations())

        glyph_lexicon = self._create_glyph_lexicon()
        language_entries = self._create_language_entries()

        result = processor.process(glyph_lexicon, language_entries)

        # Check profiles have correct categories
        profile_g001 = result.get_profile("G001")
        self.assertEqual(profile_g001.primary_category, ShapeCategory.AVIAN)

        profile_g002 = result.get_profile("G002")
        self.assertEqual(profile_g002.primary_category, ShapeCategory.ANTHROPOMORPHIC)

        profile_g003 = result.get_profile("G003")
        self.assertEqual(profile_g003.primary_category, ShapeCategory.GEOMETRIC)

        # Should have cross-references
        self.assertGreater(result.statistics.total_cross_references, 0)

    def test_pipeline_creates_valid_cross_references(self):
        """Test that cross-references have valid structure."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger(self._create_annotations())

        glyph_lexicon = self._create_glyph_lexicon()
        language_entries = self._create_language_entries()

        result = processor.process(glyph_lexicon, language_entries)

        for xref in result.cross_references:
            # Check required fields
            self.assertTrue(xref.reference_id.startswith("XR"))
            self.assertTrue(xref.glyph_cluster_id.startswith("G"))
            self.assertIsInstance(xref.language_entry_word, str)
            self.assertGreater(len(xref.language_entry_word), 0)
            self.assertGreaterEqual(xref.overall_confidence, 0.0)
            self.assertLessEqual(xref.overall_confidence, 1.0)
            self.assertIn(
                xref.confidence_level,
                ["speculative", "tentative", "plausible", "strong"],
            )

    def test_pipeline_semantic_matching(self):
        """Test that semantic matching works correctly."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger(self._create_annotations())

        glyph_lexicon = self._create_glyph_lexicon()
        language_entries = self._create_language_entries()

        result = processor.process(glyph_lexicon, language_entries)

        # G001 (avian) should match with manu/manutara
        xrefs_g001 = result.get_references_for_glyph("G001")
        words_matched = [x.language_entry_word for x in xrefs_g001]

        # Should include bird-related words
        self.assertTrue(
            any(w in words_matched for w in ["manu", "manutara"]),
            f"Expected bird words in {words_matched}",
        )

    def test_output_json_serialization(self):
        """Test that output can be serialized to JSON."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger(self._create_annotations())

        glyph_lexicon = self._create_glyph_lexicon()
        language_entries = self._create_language_entries()

        result = processor.process(glyph_lexicon, language_entries)

        # Serialize to JSON
        output_path = os.path.join(self.output_dir, "cross_reference.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result.to_dict(), f, indent=2)

        # Verify file exists and is valid JSON
        self.assertTrue(os.path.exists(output_path))

        with open(output_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("version", data)
        self.assertIn("methodology", data)
        self.assertIn("glyph_profiles", data)
        self.assertIn("cross_references", data)

    def test_output_json_roundtrip(self):
        """Test JSON roundtrip (serialize then deserialize)."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger(self._create_annotations())

        glyph_lexicon = self._create_glyph_lexicon()
        language_entries = self._create_language_entries()

        result = processor.process(glyph_lexicon, language_entries)

        # Serialize
        json_str = json.dumps(result.to_dict())

        # Deserialize
        data = json.loads(json_str)
        restored = CrossReferenceLexicon.from_dict(data)

        # Verify key fields match
        self.assertEqual(
            len(restored.glyph_profiles), len(result.glyph_profiles)
        )
        self.assertEqual(
            len(restored.cross_references), len(result.cross_references)
        )

    def test_statistics_accuracy(self):
        """Test that computed statistics are accurate."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger(self._create_annotations())

        glyph_lexicon = self._create_glyph_lexicon()
        language_entries = self._create_language_entries()

        result = processor.process(glyph_lexicon, language_entries)

        # Verify statistics
        self.assertEqual(
            result.statistics.total_glyphs_profiled,
            len(result.glyph_profiles),
        )
        self.assertEqual(
            result.statistics.total_cross_references,
            len(result.cross_references),
        )

        # Verify confidence level counts
        level_counts = {}
        for xref in result.cross_references:
            level = xref.confidence_level
            level_counts[level] = level_counts.get(level, 0) + 1

        for level, count in level_counts.items():
            self.assertEqual(
                result.statistics.by_confidence_level.get(level, 0),
                count,
            )


class TestYAMLAnnotationsIntegration(unittest.TestCase):
    """Tests for YAML annotations integration."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.temp_dir)

    def test_load_yaml_annotations(self):
        """Test loading annotations from YAML file."""
        yaml_content = {
            "G001": {
                "category": "avian",
                "confidence": 0.9,
                "subcategory": "frigate_bird",
                "visual_features": ["wings", "beak"],
            },
            "G002": {
                "category": "anthropomorphic",
                "confidence": 0.8,
            },
        }

        yaml_path = os.path.join(self.temp_dir, "annotations.yaml")
        with open(yaml_path, "w") as f:
            yaml.dump(yaml_content, f)

        processor = CrossReferenceProcessor()
        processor.load_annotations(yaml_path)

        # Create test glyph
        from models.glyphs import GlyphCluster

        cluster = GlyphCluster(cluster_id="G001", instances=["a"])
        tags = processor.tagger.tag_cluster(cluster)

        self.assertEqual(len(tags), 1)
        self.assertEqual(tags[0].category, ShapeCategory.AVIAN)
        self.assertEqual(tags[0].subcategory, "frigate_bird")

    def test_yaml_missing_fields(self):
        """Test handling of YAML with missing optional fields."""
        yaml_content = {"G001": {"category": "geometric"}}

        yaml_path = os.path.join(self.temp_dir, "annotations.yaml")
        with open(yaml_path, "w") as f:
            yaml.dump(yaml_content, f)

        processor = CrossReferenceProcessor()
        processor.load_annotations(yaml_path)

        from models.glyphs import GlyphCluster

        cluster = GlyphCluster(cluster_id="G001", instances=["a"])
        tags = processor.tagger.tag_cluster(cluster)

        self.assertEqual(tags[0].category, ShapeCategory.GEOMETRIC)
        self.assertEqual(tags[0].confidence, 0.9)  # Default
        self.assertIsNone(tags[0].subcategory)


class TestEdgeCases(unittest.TestCase):
    """Tests for edge cases."""

    def test_empty_glyph_lexicon(self):
        """Test handling of empty glyph lexicon."""
        processor = CrossReferenceProcessor()
        glyph_lexicon = RongorongoLexicon(source_images=[], clusters=[])
        language_entries = [
            LanguageEntry(
                word="manu",
                normalized="manu",
                translations=[Translation("en", "bird", None)],
            )
        ]

        result = processor.process(glyph_lexicon, language_entries)

        self.assertEqual(len(result.glyph_profiles), 0)
        self.assertEqual(len(result.cross_references), 0)

    def test_empty_language_entries(self):
        """Test handling of empty language entries."""
        processor = CrossReferenceProcessor()
        glyph_lexicon = RongorongoLexicon(
            source_images=["test.png"],
            clusters=[GlyphCluster(cluster_id="G001", instances=["a"])],
        )
        language_entries = []

        result = processor.process(glyph_lexicon, language_entries)

        # Should create profiles but no cross-references
        self.assertEqual(len(result.glyph_profiles), 1)
        self.assertEqual(len(result.cross_references), 0)

    def test_single_glyph_single_word(self):
        """Test with minimal data (one glyph, one word)."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger({"G001": {"category": "avian", "confidence": 0.9}})

        glyph_lexicon = RongorongoLexicon(
            source_images=["test.png"],
            clusters=[
                GlyphCluster(
                    cluster_id="G001",
                    instances=["a"],
                    positions=PositionStats(avg_position_in_line=0.5),
                )
            ],
        )
        language_entries = [
            LanguageEntry(
                word="manu",
                normalized="manu",
                translations=[Translation("en", "bird", None)],
                semantic_category="animals",
            )
        ]

        result = processor.process(glyph_lexicon, language_entries)

        self.assertEqual(len(result.glyph_profiles), 1)
        # May or may not have cross-references depending on confidence threshold

    def test_no_semantic_matches(self):
        """Test when shape categories don't match any semantic domains."""
        processor = CrossReferenceProcessor()
        # All glyphs are composite (no matching in SHAPE_SEMANTIC_MAPPING)
        processor.tagger = ShapeTagger(
            {"G001": {"category": "composite", "confidence": 0.9}}
        )

        glyph_lexicon = RongorongoLexicon(
            source_images=["test.png"],
            clusters=[GlyphCluster(cluster_id="G001", instances=["a"])],
        )
        language_entries = [
            LanguageEntry(
                word="manu",
                normalized="manu",
                translations=[Translation("en", "bird", None)],
                semantic_category="animals",
            )
        ]

        result = processor.process(glyph_lexicon, language_entries)

        # Should have profile but no cross-references
        self.assertEqual(len(result.glyph_profiles), 1)
        self.assertEqual(len(result.cross_references), 0)

    def test_unicode_handling(self):
        """Test handling of Unicode characters in words."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger({"G001": {"category": "avian", "confidence": 0.9}})

        glyph_lexicon = RongorongoLexicon(
            source_images=["test.png"],
            clusters=[
                GlyphCluster(
                    cluster_id="G001",
                    instances=["a"],
                    positions=PositionStats(avg_position_in_line=0.2),
                )
            ],
        )
        language_entries = [
            LanguageEntry(
                word="mānu",  # With macron
                normalized="manu",
                translations=[Translation("en", "bird", None)],
                semantic_category="animals",
            )
        ]

        result = processor.process(glyph_lexicon, language_entries)

        # Should handle Unicode without errors
        self.assertEqual(len(result.glyph_profiles), 1)


class TestConfidenceLevelDistribution(unittest.TestCase):
    """Tests for confidence level distribution."""

    def test_confidence_levels_are_valid(self):
        """Test that all confidence levels are valid."""
        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger(
            {
                "G001": {"category": "avian", "confidence": 0.9},
                "G002": {"category": "anthropomorphic", "confidence": 0.7},
            }
        )

        glyph_lexicon = RongorongoLexicon(
            source_images=["test.png"],
            clusters=[
                GlyphCluster(
                    cluster_id="G001",
                    instances=["a", "b", "c"],
                    positions=PositionStats(avg_position_in_line=0.2),
                ),
                GlyphCluster(
                    cluster_id="G002",
                    instances=["d", "e"],
                    positions=PositionStats(avg_position_in_line=0.5),
                ),
            ],
        )

        language_entries = [
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

        result = processor.process(glyph_lexicon, language_entries)

        valid_levels = {"speculative", "tentative", "plausible", "strong"}
        for xref in result.cross_references:
            self.assertIn(xref.confidence_level, valid_levels)

    def test_confidence_score_matches_level(self):
        """Test that confidence scores match their assigned levels."""
        from config import CONFIDENCE_LEVELS

        processor = CrossReferenceProcessor()
        processor.tagger = ShapeTagger({"G001": {"category": "avian", "confidence": 0.9}})

        glyph_lexicon = RongorongoLexicon(
            source_images=["test.png"],
            clusters=[
                GlyphCluster(
                    cluster_id="G001",
                    instances=["a", "b", "c", "d", "e"],
                    positions=PositionStats(
                        avg_position_in_line=0.1,
                        common_neighbors=["G002", "G003"],
                    ),
                )
            ],
        )

        language_entries = [
            LanguageEntry(
                word="manu",
                normalized="manu",
                translations=[Translation("en", "bird", None)],
                semantic_category="animals",
            )
        ]

        result = processor.process(glyph_lexicon, language_entries)

        for xref in result.cross_references:
            level = xref.confidence_level
            min_val, max_val = CONFIDENCE_LEVELS[level]
            self.assertGreaterEqual(
                xref.overall_confidence,
                min_val,
                f"Score {xref.overall_confidence} below min for {level}",
            )
            self.assertLess(
                xref.overall_confidence,
                max_val,
                f"Score {xref.overall_confidence} at or above max for {level}",
            )


if __name__ == "__main__":
    unittest.main()
