"""Tests for historical validator."""

import unittest

from agents.lexical_validation.historical_validator import (
    HistoricalValidator,
    HistoricalValidationResult,
    HistoricalContext,
    Inconsistency,
    InconsistencyType,
)
from agents.base.providers import MockProvider


class TestHistoricalContext(unittest.TestCase):
    """Tests for HistoricalContext data."""

    def test_known_text_types(self):
        """Test that known text types are defined."""
        self.assertIn("calendar", HistoricalContext.KNOWN_TEXT_TYPES)
        self.assertIn("genealogical", HistoricalContext.KNOWN_TEXT_TYPES)
        self.assertIn("chant", HistoricalContext.KNOWN_TEXT_TYPES)
        self.assertIn("inventory", HistoricalContext.KNOWN_TEXT_TYPES)

    def test_text_type_structure(self):
        """Test text type has required fields."""
        calendar = HistoricalContext.KNOWN_TEXT_TYPES["calendar"]
        self.assertIn("description", calendar)
        self.assertIn("expected_domains", calendar)
        self.assertIn("expected_patterns", calendar)
        self.assertIn("sources", calendar)

    def test_cultural_facts(self):
        """Test cultural facts are defined."""
        self.assertIn("manu", HistoricalContext.CULTURAL_FACTS)
        self.assertIn("moai", HistoricalContext.CULTURAL_FACTS)
        self.assertIn("rongorongo", HistoricalContext.CULTURAL_FACTS)

    def test_sound_changes(self):
        """Test sound change mappings are defined."""
        self.assertIn("*t", HistoricalContext.EXPECTED_SOUND_CHANGES)
        self.assertIn("*k", HistoricalContext.EXPECTED_SOUND_CHANGES)
        self.assertEqual(HistoricalContext.EXPECTED_SOUND_CHANGES["*k"], "ʔ")


class TestHistoricalValidator(unittest.TestCase):
    """Tests for HistoricalValidator."""

    def setUp(self):
        """Set up test fixtures."""
        self.validator = HistoricalValidator()

    def test_create_validator_without_llm(self):
        """Test creating validator without LLM."""
        validator = HistoricalValidator()
        self.assertIsNone(validator.llm)

    def test_create_validator_with_llm(self):
        """Test creating validator with LLM."""
        provider = MockProvider()
        validator = HistoricalValidator(llm_provider=provider)
        self.assertEqual(validator.llm.name, "mock")

    def test_validate_consistent_reference(self):
        """Test validating a consistent reference."""
        reference = {
            "reference_id": "XR001",
            "language_entry_word": "manu",
            "semantic_domain": "animals",
            "proto_polynesian_root": "*manu (bird)",
        }

        result = self.validator.validate(reference)

        self.assertIsInstance(result, HistoricalValidationResult)
        self.assertTrue(result.is_consistent)
        self.assertGreater(result.consistency_score, 0.5)
        self.assertGreater(len(result.supporting_evidence), 0)

    def test_validate_anachronistic_reference(self):
        """Test validating a reference with anachronistic terms."""
        reference = {
            "reference_id": "XR002",
            "language_entry_word": "horse",
            "semantic_domain": "animals",
        }

        result = self.validator.validate(reference)

        self.assertFalse(result.is_consistent)
        self.assertLess(result.consistency_score, 0.5)

        # Should have a cultural inconsistency
        cultural = [
            i for i in result.inconsistencies
            if i.inconsistency_type == InconsistencyType.CULTURAL
        ]
        self.assertGreater(len(cultural), 0)
        self.assertEqual(cultural[0].severity, "major")

    def test_validate_linguistic_consistency(self):
        """Test linguistic consistency checking."""
        # Good: no unexpected sound correspondences (no *k in proto form)
        reference = {
            "reference_id": "XR003",
            "language_entry_word": "manu",
            "semantic_domain": "animals",
            "proto_polynesian_root": "*manu (bird)",
        }

        result = self.validator.validate(reference)
        # Should not flag linguistic issues (regular sound correspondences)
        ling_issues = [
            i for i in result.inconsistencies
            if i.inconsistency_type == InconsistencyType.LINGUISTIC
        ]
        self.assertEqual(len(ling_issues), 0)

    def test_validate_text_type_match(self):
        """Test text type matching."""
        reference = {
            "reference_id": "XR004",
            "language_entry_word": "hanga",
            "semantic_domain": "time",
        }

        result = self.validator.validate(reference)

        # Should match calendar text type
        self.assertEqual(result.text_type_match, "calendar")

    def test_validate_with_glyph_profile(self):
        """Test validation with glyph profile data."""
        reference = {
            "reference_id": "XR005",
            "language_entry_word": "ariki",
            "semantic_domain": "kinship",
        }
        glyph_profile = {
            "cluster_id": "G001",
            "positions": {
                "avg_position_in_line": 0.2,
                "line_distribution": {"1": 5, "2": 3, "3": 4, "4": 2},
            },
        }

        result = self.validator.validate(reference, glyph_profile)

        # Should be consistent (kinship term in multiple lines)
        self.assertTrue(result.is_consistent)

    def test_validate_batch(self):
        """Test batch validation."""
        references = [
            {"reference_id": "XR001", "language_entry_word": "manu", "semantic_domain": "animals"},
            {"reference_id": "XR002", "language_entry_word": "tangata", "semantic_domain": "kinship"},
            {"reference_id": "XR003", "language_entry_word": "horse", "semantic_domain": "animals"},
        ]

        results = self.validator.validate_batch(references)

        self.assertEqual(len(results), 3)
        self.assertTrue(results[0].is_consistent)  # manu
        self.assertTrue(results[1].is_consistent)  # tangata
        self.assertFalse(results[2].is_consistent)  # horse (anachronistic)

    def test_result_to_dict(self):
        """Test converting result to dictionary."""
        result = HistoricalValidationResult(
            reference_id="XR001",
            is_consistent=True,
            consistency_score=0.85,
            supporting_evidence=["Test evidence"],
            text_type_match="calendar",
        )

        d = result.to_dict()

        self.assertEqual(d["reference_id"], "XR001")
        self.assertTrue(d["is_consistent"])
        self.assertEqual(d["consistency_score"], 0.85)
        self.assertEqual(len(d["supporting_evidence"]), 1)

    def test_generate_report(self):
        """Test report generation."""
        references = [
            {"reference_id": "XR001", "language_entry_word": "manu", "semantic_domain": "animals"},
            {"reference_id": "XR002", "language_entry_word": "horse", "semantic_domain": "animals"},
        ]

        results = self.validator.validate_batch(references)
        report = self.validator.generate_report(results)

        self.assertIn("Historical Validation Report", report)
        self.assertIn("Summary", report)
        self.assertIn("Total references: 2", report)


class TestInconsistencyType(unittest.TestCase):
    """Tests for InconsistencyType enum."""

    def test_all_types_defined(self):
        """Test all inconsistency types are defined."""
        self.assertEqual(InconsistencyType.TEMPORAL.value, "temporal")
        self.assertEqual(InconsistencyType.CULTURAL.value, "cultural")
        self.assertEqual(InconsistencyType.LINGUISTIC.value, "linguistic")
        self.assertEqual(InconsistencyType.SEMANTIC.value, "semantic")
        self.assertEqual(InconsistencyType.ARCHAEOLOGICAL.value, "archaeological")


class TestValidatorWithLLM(unittest.TestCase):
    """Tests for validator with LLM analysis."""

    def test_analyze_with_llm(self):
        """Test LLM analysis is triggered for inconsistencies."""
        provider = MockProvider(default_response="Analysis: This appears plausible. Confidence: medium.")
        validator = HistoricalValidator(llm_provider=provider)

        # Reference with anachronism will trigger LLM analysis
        reference = {
            "reference_id": "XR001",
            "language_entry_word": "metal",
            "semantic_domain": "culture",
        }

        result = validator.validate(reference)

        # LLM analysis should be present
        self.assertIsNotNone(result.llm_analysis)
        self.assertIn("Analysis", result.llm_analysis)


if __name__ == "__main__":
    unittest.main()
