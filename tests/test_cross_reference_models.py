"""Unit tests for cross-reference data models."""

import json
import unittest
from datetime import datetime

from models.cross_reference import (
    CrossReference,
    CrossReferenceLexicon,
    CrossReferenceStatistics,
    EvidenceItem,
    EvidenceType,
    GlyphSemanticProfile,
    ShapeCategory,
    ShapeTag,
)


class TestShapeCategory(unittest.TestCase):
    """Tests for ShapeCategory enum."""

    def test_all_categories_exist(self):
        """Test that all expected shape categories are defined."""
        expected = [
            "avian",
            "anthropomorphic",
            "phytomorphic",
            "ichthyomorphic",
            "geometric",
            "composite",
            "undetermined",
        ]
        actual = [c.value for c in ShapeCategory]
        self.assertEqual(sorted(expected), sorted(actual))

    def test_category_values(self):
        """Test that category enum values match their names."""
        self.assertEqual(ShapeCategory.AVIAN.value, "avian")
        self.assertEqual(ShapeCategory.ANTHROPOMORPHIC.value, "anthropomorphic")
        self.assertEqual(ShapeCategory.GEOMETRIC.value, "geometric")

    def test_category_from_string(self):
        """Test creating category from string value."""
        cat = ShapeCategory("avian")
        self.assertEqual(cat, ShapeCategory.AVIAN)

    def test_invalid_category_raises(self):
        """Test that invalid category string raises ValueError."""
        with self.assertRaises(ValueError):
            ShapeCategory("invalid_category")


class TestEvidenceType(unittest.TestCase):
    """Tests for EvidenceType enum."""

    def test_all_types_exist(self):
        """Test that all expected evidence types are defined."""
        expected = [
            "shape_semantic",
            "frequency",
            "positional",
            "neighbor",
            "published",
            "manual",
        ]
        actual = [t.value for t in EvidenceType]
        self.assertEqual(sorted(expected), sorted(actual))

    def test_type_from_string(self):
        """Test creating evidence type from string value."""
        ev_type = EvidenceType("shape_semantic")
        self.assertEqual(ev_type, EvidenceType.SHAPE_SEMANTIC)


class TestShapeTag(unittest.TestCase):
    """Tests for ShapeTag dataclass."""

    def test_creation_minimal(self):
        """Test creating a shape tag with minimal fields."""
        tag = ShapeTag(category=ShapeCategory.AVIAN, confidence=0.8)
        self.assertEqual(tag.category, ShapeCategory.AVIAN)
        self.assertEqual(tag.confidence, 0.8)
        self.assertIsNone(tag.subcategory)
        self.assertEqual(tag.visual_features, [])
        self.assertEqual(tag.tagged_by, "manual")

    def test_creation_full(self):
        """Test creating a shape tag with all fields."""
        tag = ShapeTag(
            category=ShapeCategory.AVIAN,
            confidence=0.9,
            subcategory="frigate_bird",
            visual_features=["wings", "forked_tail"],
            tagged_by="expert",
            tagged_at="2026-01-20T10:00:00",
        )
        self.assertEqual(tag.subcategory, "frigate_bird")
        self.assertEqual(tag.visual_features, ["wings", "forked_tail"])
        self.assertEqual(tag.tagged_by, "expert")
        self.assertEqual(tag.tagged_at, "2026-01-20T10:00:00")

    def test_auto_timestamp(self):
        """Test that tagged_at is auto-filled if not provided."""
        tag = ShapeTag(category=ShapeCategory.GEOMETRIC, confidence=0.5)
        self.assertIsNotNone(tag.tagged_at)
        # Should be a valid ISO timestamp
        datetime.fromisoformat(tag.tagged_at)

    def test_to_dict(self):
        """Test serialization to dictionary."""
        tag = ShapeTag(
            category=ShapeCategory.AVIAN,
            confidence=0.85,
            subcategory="frigate_bird",
            visual_features=["wings"],
            tagged_by="manual",
            tagged_at="2026-01-20T10:00:00",
        )
        d = tag.to_dict()
        self.assertEqual(d["category"], "avian")
        self.assertEqual(d["confidence"], 0.85)
        self.assertEqual(d["subcategory"], "frigate_bird")
        self.assertEqual(d["visual_features"], ["wings"])
        self.assertEqual(d["tagged_by"], "manual")

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {
            "category": "anthropomorphic",
            "confidence": 0.7,
            "subcategory": "standing_figure",
            "visual_features": ["arms", "legs"],
            "tagged_by": "rule_based",
            "tagged_at": "2026-01-20T10:00:00",
        }
        tag = ShapeTag.from_dict(d)
        self.assertEqual(tag.category, ShapeCategory.ANTHROPOMORPHIC)
        self.assertEqual(tag.confidence, 0.7)
        self.assertEqual(tag.subcategory, "standing_figure")

    def test_confidence_rounding(self):
        """Test that confidence is rounded in to_dict."""
        tag = ShapeTag(category=ShapeCategory.AVIAN, confidence=0.123456789)
        d = tag.to_dict()
        self.assertEqual(d["confidence"], 0.123)


class TestEvidenceItem(unittest.TestCase):
    """Tests for EvidenceItem dataclass."""

    def test_creation_minimal(self):
        """Test creating evidence with minimal fields."""
        evidence = EvidenceItem(
            evidence_type=EvidenceType.SHAPE_SEMANTIC,
            description="Bird glyph matches bird domain",
            strength=0.6,
        )
        self.assertEqual(evidence.evidence_type, EvidenceType.SHAPE_SEMANTIC)
        self.assertEqual(evidence.description, "Bird glyph matches bird domain")
        self.assertEqual(evidence.strength, 0.6)
        self.assertIsNone(evidence.source)
        self.assertEqual(evidence.data, {})

    def test_creation_full(self):
        """Test creating evidence with all fields."""
        evidence = EvidenceItem(
            evidence_type=EvidenceType.FREQUENCY_CORRELATION,
            description="High frequency correlation",
            strength=0.8,
            source="frequency_analysis",
            data={"glyph_rank": 1, "word_rank": 2},
        )
        self.assertEqual(evidence.source, "frequency_analysis")
        self.assertEqual(evidence.data["glyph_rank"], 1)

    def test_to_dict(self):
        """Test serialization to dictionary."""
        evidence = EvidenceItem(
            evidence_type=EvidenceType.POSITIONAL_PATTERN,
            description="Initial position tendency",
            strength=0.4,
            source="positional_analysis",
            data={"avg_position": 0.2},
        )
        d = evidence.to_dict()
        self.assertEqual(d["type"], "positional")
        self.assertEqual(d["description"], "Initial position tendency")
        self.assertEqual(d["strength"], 0.4)
        self.assertEqual(d["source"], "positional_analysis")
        self.assertIn("avg_position", d["data"])

    def test_to_dict_minimal(self):
        """Test that minimal evidence excludes empty optional fields."""
        evidence = EvidenceItem(
            evidence_type=EvidenceType.MANUAL_ANNOTATION,
            description="Expert annotation",
            strength=0.9,
        )
        d = evidence.to_dict()
        self.assertNotIn("source", d)
        self.assertNotIn("data", d)

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {
            "type": "neighbor",
            "description": "Co-occurrence pattern",
            "strength": 0.3,
            "source": "neighbor_analysis",
            "data": {"neighbors": ["G002", "G003"]},
        }
        evidence = EvidenceItem.from_dict(d)
        self.assertEqual(evidence.evidence_type, EvidenceType.NEIGHBOR_CONTEXT)
        self.assertEqual(evidence.strength, 0.3)
        self.assertEqual(evidence.data["neighbors"], ["G002", "G003"])


class TestCrossReference(unittest.TestCase):
    """Tests for CrossReference dataclass."""

    def test_creation(self):
        """Test creating a cross-reference."""
        xref = CrossReference(
            reference_id="XR001",
            glyph_cluster_id="G001",
            language_entry_word="manu",
            language_entry_normalized="manu",
            overall_confidence=0.45,
            confidence_level="tentative",
            semantic_domain="animals",
        )
        self.assertEqual(xref.reference_id, "XR001")
        self.assertEqual(xref.glyph_cluster_id, "G001")
        self.assertEqual(xref.language_entry_word, "manu")
        self.assertEqual(xref.overall_confidence, 0.45)
        self.assertEqual(xref.confidence_level, "tentative")

    def test_default_values(self):
        """Test default values for optional fields."""
        xref = CrossReference(
            reference_id="XR001",
            glyph_cluster_id="G001",
            language_entry_word="manu",
            language_entry_normalized="manu",
            overall_confidence=0.5,
            confidence_level="tentative",
            semantic_domain="animals",
        )
        self.assertEqual(xref.evidence, [])
        self.assertIsNone(xref.proto_polynesian_root)
        self.assertEqual(xref.created_by, "system")
        self.assertIsNone(xref.notes)
        self.assertFalse(xref.is_published_hypothesis)
        self.assertTrue(xref.requires_review)

    def test_with_evidence(self):
        """Test cross-reference with evidence items."""
        evidence = [
            EvidenceItem(
                evidence_type=EvidenceType.SHAPE_SEMANTIC,
                description="Avian glyph matches bird domain",
                strength=0.6,
            ),
            EvidenceItem(
                evidence_type=EvidenceType.FREQUENCY_CORRELATION,
                description="Rank correlation",
                strength=0.4,
            ),
        ]
        xref = CrossReference(
            reference_id="XR001",
            glyph_cluster_id="G001",
            language_entry_word="manu",
            language_entry_normalized="manu",
            overall_confidence=0.5,
            confidence_level="tentative",
            semantic_domain="animals",
            evidence=evidence,
        )
        self.assertEqual(len(xref.evidence), 2)

    def test_to_dict(self):
        """Test serialization to dictionary."""
        xref = CrossReference(
            reference_id="XR001",
            glyph_cluster_id="G001",
            language_entry_word="manu",
            language_entry_normalized="manu",
            overall_confidence=0.5,
            confidence_level="tentative",
            semantic_domain="animals",
            proto_polynesian_root="*manu (bird)",
            notes="Test note",
        )
        d = xref.to_dict()
        self.assertEqual(d["reference_id"], "XR001")
        self.assertEqual(d["glyph_cluster_id"], "G001")
        self.assertEqual(d["proto_polynesian_root"], "*manu (bird)")
        self.assertEqual(d["notes"], "Test note")

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {
            "reference_id": "XR005",
            "glyph_cluster_id": "G003",
            "language_entry_word": "tangata",
            "language_entry_normalized": "tangata",
            "overall_confidence": 0.6,
            "confidence_level": "plausible",
            "semantic_domain": "kinship",
            "evidence": [],
            "created_at": "2026-01-20T10:00:00",
            "created_by": "test",
        }
        xref = CrossReference.from_dict(d)
        self.assertEqual(xref.reference_id, "XR005")
        self.assertEqual(xref.language_entry_word, "tangata")
        self.assertEqual(xref.confidence_level, "plausible")

    def test_generate_id(self):
        """Test ID generation."""
        self.assertEqual(CrossReference.generate_id(1), "XR001")
        self.assertEqual(CrossReference.generate_id(42), "XR042")
        self.assertEqual(CrossReference.generate_id(999), "XR999")


class TestGlyphSemanticProfile(unittest.TestCase):
    """Tests for GlyphSemanticProfile dataclass."""

    def test_creation(self):
        """Test creating a semantic profile."""
        profile = GlyphSemanticProfile(
            cluster_id="G001",
            frequency_rank=1,
            frequency_count=10,
        )
        self.assertEqual(profile.cluster_id, "G001")
        self.assertEqual(profile.shape_tags, [])
        self.assertIsNone(profile.primary_category)
        self.assertEqual(profile.cross_reference_ids, [])
        self.assertEqual(profile.frequency_rank, 1)
        self.assertEqual(profile.positional_tendency, "neutral")

    def test_add_shape_tag(self):
        """Test adding a shape tag updates primary category."""
        profile = GlyphSemanticProfile(cluster_id="G001")
        tag = ShapeTag(category=ShapeCategory.AVIAN, confidence=0.8)
        profile.add_shape_tag(tag)

        self.assertEqual(len(profile.shape_tags), 1)
        self.assertEqual(profile.primary_category, ShapeCategory.AVIAN)

    def test_add_multiple_tags(self):
        """Test that highest confidence tag becomes primary."""
        profile = GlyphSemanticProfile(cluster_id="G001")
        profile.add_shape_tag(ShapeTag(category=ShapeCategory.AVIAN, confidence=0.5))
        profile.add_shape_tag(ShapeTag(category=ShapeCategory.GEOMETRIC, confidence=0.9))

        self.assertEqual(profile.primary_category, ShapeCategory.GEOMETRIC)

    def test_to_dict(self):
        """Test serialization to dictionary."""
        profile = GlyphSemanticProfile(
            cluster_id="G001",
            frequency_rank=2,
            frequency_count=5,
            positional_tendency="initial",
            barthel_number="600",
        )
        profile.add_shape_tag(ShapeTag(category=ShapeCategory.AVIAN, confidence=0.8))
        profile.cross_reference_ids.append("XR001")

        d = profile.to_dict()
        self.assertEqual(d["cluster_id"], "G001")
        self.assertEqual(d["frequency_rank"], 2)
        self.assertEqual(d["primary_category"], "avian")
        self.assertEqual(d["barthel_number"], "600")
        self.assertEqual(len(d["shape_tags"]), 1)
        self.assertEqual(d["cross_reference_ids"], ["XR001"])

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {
            "cluster_id": "G005",
            "shape_tags": [{"category": "geometric", "confidence": 0.7, "tagged_by": "manual"}],
            "primary_category": "geometric",
            "cross_reference_ids": ["XR002", "XR003"],
            "frequency_rank": 3,
            "frequency_count": 4,
            "positional_tendency": "final",
        }
        profile = GlyphSemanticProfile.from_dict(d)
        self.assertEqual(profile.cluster_id, "G005")
        self.assertEqual(profile.primary_category, ShapeCategory.GEOMETRIC)
        self.assertEqual(len(profile.shape_tags), 1)
        self.assertEqual(profile.positional_tendency, "final")


class TestCrossReferenceStatistics(unittest.TestCase):
    """Tests for CrossReferenceStatistics dataclass."""

    def test_creation_defaults(self):
        """Test default values."""
        stats = CrossReferenceStatistics()
        self.assertEqual(stats.total_glyphs_profiled, 0)
        self.assertEqual(stats.total_cross_references, 0)
        self.assertEqual(stats.by_confidence_level, {})
        self.assertEqual(stats.by_shape_category, {})
        self.assertEqual(stats.by_semantic_domain, {})

    def test_to_dict(self):
        """Test serialization."""
        stats = CrossReferenceStatistics(
            total_glyphs_profiled=10,
            total_cross_references=25,
            by_confidence_level={"speculative": 15, "tentative": 10},
            by_shape_category={"avian": 5, "geometric": 3},
            by_semantic_domain={"animals": 8, "kinship": 4},
        )
        d = stats.to_dict()
        self.assertEqual(d["total_glyphs_profiled"], 10)
        self.assertEqual(d["total_cross_references"], 25)
        self.assertEqual(d["by_confidence_level"]["speculative"], 15)

    def test_from_dict(self):
        """Test deserialization."""
        d = {
            "total_glyphs_profiled": 5,
            "total_cross_references": 12,
            "by_confidence_level": {"tentative": 8},
            "by_shape_category": {"anthropomorphic": 3},
            "by_semantic_domain": {"body": 5},
        }
        stats = CrossReferenceStatistics.from_dict(d)
        self.assertEqual(stats.total_glyphs_profiled, 5)
        self.assertEqual(stats.by_confidence_level["tentative"], 8)


class TestCrossReferenceLexicon(unittest.TestCase):
    """Tests for CrossReferenceLexicon dataclass."""

    def test_creation_defaults(self):
        """Test default values."""
        lexicon = CrossReferenceLexicon()
        self.assertEqual(lexicon.version, "1.0.0")
        self.assertIn("warning", lexicon.methodology)
        self.assertEqual(lexicon.glyph_profiles, [])
        self.assertEqual(lexicon.cross_references, [])

    def test_add_profile(self):
        """Test adding a glyph profile."""
        lexicon = CrossReferenceLexicon()
        profile = GlyphSemanticProfile(cluster_id="G001")
        lexicon.add_profile(profile)
        self.assertEqual(len(lexicon.glyph_profiles), 1)

    def test_add_cross_reference(self):
        """Test adding a cross-reference."""
        lexicon = CrossReferenceLexicon()
        xref = CrossReference(
            reference_id="XR001",
            glyph_cluster_id="G001",
            language_entry_word="manu",
            language_entry_normalized="manu",
            overall_confidence=0.5,
            confidence_level="tentative",
            semantic_domain="animals",
        )
        lexicon.add_cross_reference(xref)
        self.assertEqual(len(lexicon.cross_references), 1)

    def test_get_profile(self):
        """Test getting a profile by ID."""
        lexicon = CrossReferenceLexicon()
        profile = GlyphSemanticProfile(cluster_id="G005")
        lexicon.add_profile(profile)

        result = lexicon.get_profile("G005")
        self.assertIsNotNone(result)
        self.assertEqual(result.cluster_id, "G005")

        result = lexicon.get_profile("G999")
        self.assertIsNone(result)

    def test_get_references_for_glyph(self):
        """Test getting cross-references for a glyph."""
        lexicon = CrossReferenceLexicon()
        lexicon.add_cross_reference(
            CrossReference(
                reference_id="XR001",
                glyph_cluster_id="G001",
                language_entry_word="manu",
                language_entry_normalized="manu",
                overall_confidence=0.5,
                confidence_level="tentative",
                semantic_domain="animals",
            )
        )
        lexicon.add_cross_reference(
            CrossReference(
                reference_id="XR002",
                glyph_cluster_id="G001",
                language_entry_word="kura",
                language_entry_normalized="kura",
                overall_confidence=0.3,
                confidence_level="speculative",
                semantic_domain="animals",
            )
        )
        lexicon.add_cross_reference(
            CrossReference(
                reference_id="XR003",
                glyph_cluster_id="G002",
                language_entry_word="tangata",
                language_entry_normalized="tangata",
                overall_confidence=0.4,
                confidence_level="tentative",
                semantic_domain="kinship",
            )
        )

        refs = lexicon.get_references_for_glyph("G001")
        self.assertEqual(len(refs), 2)
        ref_ids = [r.reference_id for r in refs]
        self.assertIn("XR001", ref_ids)
        self.assertIn("XR002", ref_ids)

    def test_get_references_for_word(self):
        """Test getting cross-references for a word."""
        lexicon = CrossReferenceLexicon()
        lexicon.add_cross_reference(
            CrossReference(
                reference_id="XR001",
                glyph_cluster_id="G001",
                language_entry_word="manu",
                language_entry_normalized="manu",
                overall_confidence=0.5,
                confidence_level="tentative",
                semantic_domain="animals",
            )
        )
        lexicon.add_cross_reference(
            CrossReference(
                reference_id="XR002",
                glyph_cluster_id="G002",
                language_entry_word="Manu",  # Different case
                language_entry_normalized="manu",
                overall_confidence=0.4,
                confidence_level="tentative",
                semantic_domain="animals",
            )
        )

        refs = lexicon.get_references_for_word("manu")
        self.assertEqual(len(refs), 2)

        refs = lexicon.get_references_for_word("MANU")
        self.assertEqual(len(refs), 2)

    def test_compute_statistics(self):
        """Test computing statistics."""
        lexicon = CrossReferenceLexicon()

        # Add profiles
        profile1 = GlyphSemanticProfile(cluster_id="G001")
        profile1.add_shape_tag(ShapeTag(category=ShapeCategory.AVIAN, confidence=0.8))
        lexicon.add_profile(profile1)

        profile2 = GlyphSemanticProfile(cluster_id="G002")
        profile2.add_shape_tag(ShapeTag(category=ShapeCategory.AVIAN, confidence=0.7))
        lexicon.add_profile(profile2)

        # Add cross-references
        lexicon.add_cross_reference(
            CrossReference(
                reference_id="XR001",
                glyph_cluster_id="G001",
                language_entry_word="manu",
                language_entry_normalized="manu",
                overall_confidence=0.5,
                confidence_level="tentative",
                semantic_domain="animals",
            )
        )
        lexicon.add_cross_reference(
            CrossReference(
                reference_id="XR002",
                glyph_cluster_id="G002",
                language_entry_word="tangata",
                language_entry_normalized="tangata",
                overall_confidence=0.2,
                confidence_level="speculative",
                semantic_domain="kinship",
            )
        )

        lexicon.compute_statistics()

        self.assertEqual(lexicon.statistics.total_glyphs_profiled, 2)
        self.assertEqual(lexicon.statistics.total_cross_references, 2)
        self.assertEqual(lexicon.statistics.by_confidence_level["tentative"], 1)
        self.assertEqual(lexicon.statistics.by_confidence_level["speculative"], 1)
        self.assertEqual(lexicon.statistics.by_shape_category["avian"], 2)
        self.assertEqual(lexicon.statistics.by_semantic_domain["animals"], 1)
        self.assertEqual(lexicon.statistics.by_semantic_domain["kinship"], 1)

    def test_to_dict(self):
        """Test serialization to dictionary."""
        lexicon = CrossReferenceLexicon()
        lexicon.glyph_lexicon_file = "glyphs.json"
        lexicon.language_lexicon_file = "language.json"

        d = lexicon.to_dict()
        self.assertIn("version", d)
        self.assertIn("methodology", d)
        self.assertIn("source_data", d)
        self.assertEqual(d["source_data"]["glyph_lexicon"], "glyphs.json")

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {
            "version": "2.0.0",
            "created_at": "2026-01-20T10:00:00",
            "methodology": {"warning": "Test warning"},
            "source_data": {"glyph_lexicon": "g.json", "language_lexicon": "l.json"},
            "glyph_profiles": [],
            "cross_references": [],
            "statistics": {},
        }
        lexicon = CrossReferenceLexicon.from_dict(d)
        self.assertEqual(lexicon.version, "2.0.0")
        self.assertEqual(lexicon.glyph_lexicon_file, "g.json")

    def test_roundtrip_serialization(self):
        """Test that serialization and deserialization preserve data."""
        lexicon = CrossReferenceLexicon()

        profile = GlyphSemanticProfile(cluster_id="G001", frequency_rank=1)
        profile.add_shape_tag(ShapeTag(category=ShapeCategory.AVIAN, confidence=0.8))
        lexicon.add_profile(profile)

        lexicon.add_cross_reference(
            CrossReference(
                reference_id="XR001",
                glyph_cluster_id="G001",
                language_entry_word="manu",
                language_entry_normalized="manu",
                overall_confidence=0.5,
                confidence_level="tentative",
                semantic_domain="animals",
                evidence=[
                    EvidenceItem(
                        evidence_type=EvidenceType.SHAPE_SEMANTIC,
                        description="Test evidence",
                        strength=0.6,
                    )
                ],
            )
        )

        lexicon.compute_statistics()

        # Serialize and deserialize
        d = lexicon.to_dict()
        json_str = json.dumps(d)
        restored_d = json.loads(json_str)
        restored = CrossReferenceLexicon.from_dict(restored_d)

        # Verify
        self.assertEqual(len(restored.glyph_profiles), 1)
        self.assertEqual(len(restored.cross_references), 1)
        self.assertEqual(restored.cross_references[0].reference_id, "XR001")
        self.assertEqual(len(restored.cross_references[0].evidence), 1)


if __name__ == "__main__":
    unittest.main()
