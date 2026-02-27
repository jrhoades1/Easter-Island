"""Tests for language data models."""

import os
import sys
import unittest

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.language import Etymology, Example, LanguageEntry, Metadata, Translation


class TestLanguageEntryNormalization(unittest.TestCase):
    """Test word normalization functionality."""

    def test_normalize_lowercase(self):
        """Normalization should lowercase words."""
        entry = LanguageEntry(word="Tahi")
        self.assertEqual(entry.normalized, "tahi")

    def test_normalize_removes_diacritics(self):
        """Normalization should remove diacritical marks."""
        entry = LanguageEntry(word="hā")
        self.assertEqual(entry.normalized, "ha")

        entry = LanguageEntry(word="ꞌaŋahuru")
        # The glottal stop ꞌ and ŋ should be preserved as they're not combining marks
        self.assertIn("a", entry.normalized)

    def test_normalize_static_method(self):
        """Static normalize_word method should work independently."""
        self.assertEqual(LanguageEntry.normalize_word("Tahi"), "tahi")
        self.assertEqual(LanguageEntry.normalize_word("HĀ"), "ha")

    def test_auto_normalization_on_init(self):
        """Normalization should happen automatically on initialization."""
        entry = LanguageEntry(word="Mata")
        self.assertEqual(entry.normalized, "mata")

    def test_explicit_normalized_not_overwritten(self):
        """If normalized is explicitly set, it should be used."""
        entry = LanguageEntry(word="Mata", normalized="custom")
        self.assertEqual(entry.normalized, "custom")


class TestLanguageEntryMerging(unittest.TestCase):
    """Test merging of language entries from multiple sources."""

    def test_merge_translations(self):
        """Merging should combine translations from both entries."""
        entry1 = LanguageEntry(
            word="mata",
            translations=[Translation(language="en", text="eye")]
        )
        entry2 = LanguageEntry(
            word="mata",
            translations=[Translation(language="en", text="face")]
        )

        merged = entry1.merge_with(entry2)

        self.assertEqual(len(merged.translations), 2)
        texts = {t.text for t in merged.translations}
        self.assertIn("eye", texts)
        self.assertIn("face", texts)

    def test_merge_avoids_duplicate_translations(self):
        """Merging should not duplicate identical translations."""
        entry1 = LanguageEntry(
            word="mata",
            translations=[Translation(language="en", text="eye")]
        )
        entry2 = LanguageEntry(
            word="mata",
            translations=[Translation(language="en", text="eye")]  # Same
        )

        merged = entry1.merge_with(entry2)

        self.assertEqual(len(merged.translations), 1)

    def test_merge_examples(self):
        """Merging should combine examples from both entries."""
        entry1 = LanguageEntry(
            word="mata",
            examples=[Example(rapa_nui="He mata", translation="An eye")]
        )
        entry2 = LanguageEntry(
            word="mata",
            examples=[Example(rapa_nui="Mata rahi", translation="Big eye")]
        )

        merged = entry1.merge_with(entry2)

        self.assertEqual(len(merged.examples), 2)

    def test_merge_takes_ipa_if_missing(self):
        """Merging should take IPA from other entry if self doesn't have it."""
        entry1 = LanguageEntry(word="mata", ipa=None)
        entry2 = LanguageEntry(word="mata", ipa="[ˈmata]")

        merged = entry1.merge_with(entry2)

        self.assertEqual(merged.ipa, "[ˈmata]")

    def test_merge_keeps_own_ipa(self):
        """Merging should keep own IPA if present."""
        entry1 = LanguageEntry(word="mata", ipa="[mata]")
        entry2 = LanguageEntry(word="mata", ipa="[ˈmata]")

        merged = entry1.merge_with(entry2)

        self.assertEqual(merged.ipa, "[mata]")

    def test_merge_takes_pos_if_missing(self):
        """Merging should take part of speech from other if missing."""
        entry1 = LanguageEntry(word="mata")
        entry2 = LanguageEntry(word="mata", part_of_speech="noun")

        merged = entry1.merge_with(entry2)

        self.assertEqual(merged.part_of_speech, "noun")

    def test_merge_takes_category_if_missing(self):
        """Merging should take semantic category from other if missing."""
        entry1 = LanguageEntry(word="mata")
        entry2 = LanguageEntry(word="mata", semantic_category="body")

        merged = entry1.merge_with(entry2)

        self.assertEqual(merged.semantic_category, "body")

    def test_merge_etymology(self):
        """Merging should combine etymology information."""
        entry1 = LanguageEntry(
            word="mata",
            etymology=Etymology(origin=None, cognates=["Maori mata"])
        )
        entry2 = LanguageEntry(
            word="mata",
            etymology=Etymology(origin="Proto-Polynesian", cognates=["Hawaiian maka"])
        )

        merged = entry1.merge_with(entry2)

        self.assertEqual(merged.etymology.origin, "Proto-Polynesian")
        self.assertIn("Maori mata", merged.etymology.cognates)
        self.assertIn("Hawaiian maka", merged.etymology.cognates)


class TestLanguageEntrySerialization(unittest.TestCase):
    """Test JSON serialization of language entries."""

    def test_to_dict_basic(self):
        """to_dict should produce serializable dictionary."""
        entry = LanguageEntry(
            word="tahi",
            translations=[Translation(language="en", text="one")]
        )

        data = entry.to_dict()

        self.assertEqual(data["word"], "tahi")
        self.assertEqual(data["normalized"], "tahi")
        self.assertEqual(len(data["translations"]), 1)
        self.assertEqual(data["translations"][0]["text"], "one")

    def test_to_dict_with_all_fields(self):
        """to_dict should include all populated fields."""
        entry = LanguageEntry(
            word="mata",
            ipa="[ˈmata]",
            translations=[Translation(language="en", text="eye", gloss="EYE")],
            part_of_speech="noun",
            semantic_category="body",
            examples=[Example(rapa_nui="He mata", translation="An eye", source="Test")],
            etymology=Etymology(origin="Proto-Polynesian", cognates=["Maori mata"], loan=False),
            metadata=Metadata(source_url="http://test.com", source_name="Test", confidence="high")
        )

        data = entry.to_dict()

        self.assertEqual(data["ipa"], "[ˈmata]")
        self.assertEqual(data["part_of_speech"], "noun")
        self.assertEqual(data["semantic_category"], "body")
        self.assertEqual(data["etymology"]["origin"], "Proto-Polynesian")
        self.assertEqual(data["metadata"]["source_name"], "Test")

    def test_to_dict_omits_none_fields(self):
        """to_dict should not include None fields."""
        entry = LanguageEntry(word="tahi")

        data = entry.to_dict()

        self.assertNotIn("ipa", data)
        self.assertNotIn("part_of_speech", data)
        self.assertNotIn("semantic_category", data)


class TestTranslation(unittest.TestCase):
    """Test Translation dataclass."""

    def test_translation_creation(self):
        """Should create translation with required fields."""
        t = Translation(language="en", text="eye")
        self.assertEqual(t.language, "en")
        self.assertEqual(t.text, "eye")
        self.assertIsNone(t.gloss)

    def test_translation_with_gloss(self):
        """Should support optional gloss field."""
        t = Translation(language="en", text="eye", gloss="EYE")
        self.assertEqual(t.gloss, "EYE")


class TestExample(unittest.TestCase):
    """Test Example dataclass."""

    def test_example_creation(self):
        """Should create example with required fields."""
        e = Example(rapa_nui="He mata", translation="An eye")
        self.assertEqual(e.rapa_nui, "He mata")
        self.assertEqual(e.translation, "An eye")
        self.assertIsNone(e.source)

    def test_example_with_source(self):
        """Should support optional source field."""
        e = Example(rapa_nui="He mata", translation="An eye", source="Wikipedia")
        self.assertEqual(e.source, "Wikipedia")


class TestMetadata(unittest.TestCase):
    """Test Metadata dataclass."""

    def test_metadata_creation(self):
        """Should create metadata with required fields."""
        m = Metadata(source_url="http://test.com", source_name="Test")
        self.assertEqual(m.source_url, "http://test.com")
        self.assertEqual(m.source_name, "Test")
        self.assertEqual(m.confidence, "medium")  # default

    def test_metadata_has_timestamp(self):
        """Should auto-generate timestamp."""
        m = Metadata(source_url="http://test.com", source_name="Test")
        self.assertIsNotNone(m.scraped_at)
        self.assertGreater(len(m.scraped_at), 0)


class TestEtymology(unittest.TestCase):
    """Test Etymology dataclass."""

    def test_etymology_defaults(self):
        """Should have sensible defaults."""
        e = Etymology()
        self.assertIsNone(e.origin)
        self.assertEqual(e.cognates, [])
        self.assertFalse(e.loan)

    def test_etymology_with_values(self):
        """Should accept all values."""
        e = Etymology(origin="Proto-Polynesian", cognates=["Maori mata"], loan=True)
        self.assertEqual(e.origin, "Proto-Polynesian")
        self.assertEqual(e.cognates, ["Maori mata"])
        self.assertTrue(e.loan)


if __name__ == "__main__":
    unittest.main()
