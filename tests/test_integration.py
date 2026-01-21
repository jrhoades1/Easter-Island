"""Integration tests for the full language scraper."""

import os
import sys
import json
import unittest
from unittest.mock import patch, MagicMock

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from language_scraper import (
    deduplicate_entries,
    compute_statistics,
    collect_source_attribution,
    scrape_language_data,
)
from models.language import LanguageEntry, Translation, Metadata


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


def load_fixture(filename: str) -> str:
    """Load an HTML fixture file."""
    filepath = os.path.join(FIXTURES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


class TestDeduplication(unittest.TestCase):
    """Test entry deduplication logic."""

    def test_deduplicate_identical_entries(self):
        """Should merge entries with same normalized form."""
        entries = [
            LanguageEntry(
                word="Tahi",
                translations=[Translation(language="en", text="one")]
            ),
            LanguageEntry(
                word="tahi",
                translations=[Translation(language="en", text="first")]
            ),
        ]

        result = deduplicate_entries(entries)

        self.assertEqual(len(result), 1)
        # Should have both translations
        texts = {t.text for t in result[0].translations}
        self.assertIn("one", texts)
        self.assertIn("first", texts)

    def test_deduplicate_different_entries(self):
        """Should keep entries with different normalized forms."""
        entries = [
            LanguageEntry(word="tahi", translations=[Translation(language="en", text="one")]),
            LanguageEntry(word="rua", translations=[Translation(language="en", text="two")]),
        ]

        result = deduplicate_entries(entries)

        self.assertEqual(len(result), 2)

    def test_deduplicate_empty_list(self):
        """Should handle empty list."""
        result = deduplicate_entries([])
        self.assertEqual(result, [])

    def test_deduplicate_preserves_metadata(self):
        """Should preserve metadata from first entry."""
        entries = [
            LanguageEntry(
                word="tahi",
                translations=[Translation(language="en", text="one")],
                metadata=Metadata(source_url="http://first.com", source_name="First")
            ),
            LanguageEntry(
                word="tahi",
                translations=[Translation(language="en", text="1")],
                metadata=Metadata(source_url="http://second.com", source_name="Second")
            ),
        ]

        result = deduplicate_entries(entries)

        self.assertEqual(result[0].metadata.source_name, "First")


class TestStatistics(unittest.TestCase):
    """Test statistics computation."""

    def test_compute_statistics_basic(self):
        """Should compute basic statistics."""
        entries = [
            LanguageEntry(word="tahi", part_of_speech="numeral"),
            LanguageEntry(word="rua", part_of_speech="numeral"),
            LanguageEntry(word="mata", part_of_speech="noun", semantic_category="body"),
        ]

        stats = compute_statistics(entries)

        self.assertEqual(stats["total_entries"], 3)
        self.assertEqual(stats["entries_by_pos"]["numeral"], 2)
        self.assertEqual(stats["entries_by_pos"]["noun"], 1)
        self.assertEqual(stats["entries_by_category"]["body"], 1)

    def test_compute_statistics_empty(self):
        """Should handle empty entries."""
        stats = compute_statistics([])

        self.assertEqual(stats["total_entries"], 0)
        self.assertEqual(stats["entries_by_pos"], {})
        self.assertEqual(stats["entries_by_category"], {})


class TestSourceAttribution(unittest.TestCase):
    """Test source attribution collection."""

    def test_collect_sources(self):
        """Should collect unique sources with counts."""
        entries = [
            LanguageEntry(
                word="tahi",
                metadata=Metadata(source_url="http://a.com", source_name="Source A")
            ),
            LanguageEntry(
                word="rua",
                metadata=Metadata(source_url="http://a.com", source_name="Source A")
            ),
            LanguageEntry(
                word="mata",
                metadata=Metadata(source_url="http://b.com", source_name="Source B")
            ),
        ]

        sources = collect_source_attribution(entries)

        self.assertEqual(len(sources), 2)

        source_a = next(s for s in sources if s["name"] == "Source A")
        self.assertEqual(source_a["entries_contributed"], 2)

        source_b = next(s for s in sources if s["name"] == "Source B")
        self.assertEqual(source_b["entries_contributed"], 1)

    def test_collect_sources_handles_no_metadata(self):
        """Should handle entries without metadata."""
        entries = [
            LanguageEntry(word="tahi"),  # No metadata
        ]

        sources = collect_source_attribution(entries)

        self.assertEqual(sources, [])


class TestIntegrationWithFixtures(unittest.TestCase):
    """Integration tests using saved fixtures."""

    def test_full_pipeline_with_mocked_requests(self):
        """Test full scraping pipeline with mocked HTTP requests."""
        # Load fixtures
        fixtures = {
            "https://asjp.clld.org/languages/RAPA_NUI": load_fixture("asjp_rapa_nui.html"),
            "https://ids.clld.org/contributions/238": load_fixture("ids_contribution.html"),
            "https://glosbe.com/en/rap": load_fixture("glosbe_en_rap.html"),
            "https://www.omniglot.com/writing/rapanui.htm": load_fixture("omniglot_rapanui.html"),
            "https://en.wikipedia.org/wiki/Rapa_Nui_language": load_fixture("wikipedia_rapa_nui.html"),
        }

        def mock_fetch(url):
            return fixtures.get(url)

        with patch("language_scraper.fetch_page", side_effect=mock_fetch):
            data = scrape_language_data()

        # Verify output structure
        self.assertIn("scraped_at", data)
        self.assertIn("version", data)
        self.assertIn("language", data)
        self.assertIn("statistics", data)
        self.assertIn("entries", data)
        self.assertIn("sources", data)

        # Verify language metadata
        self.assertEqual(data["language"]["name"], "Rapa Nui")
        self.assertEqual(data["language"]["iso_639_3"], "rap")

        # Verify we got some entries
        self.assertGreater(len(data["entries"]), 0)

        # Verify entries are sorted alphabetically
        words = [e["word"] for e in data["entries"]]
        self.assertEqual(words, sorted(words, key=lambda w: data["entries"][words.index(w)]["normalized"]))

    def test_output_is_json_serializable(self):
        """Test that output can be serialized to JSON."""
        fixtures = {
            "https://asjp.clld.org/languages/RAPA_NUI": load_fixture("asjp_rapa_nui.html"),
            "https://ids.clld.org/contributions/238": load_fixture("ids_contribution.html"),
            "https://glosbe.com/en/rap": load_fixture("glosbe_en_rap.html"),
            "https://www.omniglot.com/writing/rapanui.htm": load_fixture("omniglot_rapanui.html"),
            "https://en.wikipedia.org/wiki/Rapa_Nui_language": load_fixture("wikipedia_rapa_nui.html"),
        }

        def mock_fetch(url):
            return fixtures.get(url)

        with patch("language_scraper.fetch_page", side_effect=mock_fetch):
            data = scrape_language_data()

        # Should not raise
        json_str = json.dumps(data, ensure_ascii=False)
        self.assertIsInstance(json_str, str)

        # Should round-trip
        parsed = json.loads(json_str)
        self.assertEqual(parsed["language"]["name"], "Rapa Nui")


class TestOutputStructure(unittest.TestCase):
    """Test the structure of scraped output."""

    def test_entry_structure(self):
        """Test that entries have expected structure."""
        entry = LanguageEntry(
            word="tahi",
            ipa="[tahi]",
            translations=[Translation(language="en", text="one")],
            part_of_speech="numeral",
            metadata=Metadata(source_url="http://test.com", source_name="Test")
        )

        data = entry.to_dict()

        # Required fields
        self.assertIn("word", data)
        self.assertIn("normalized", data)
        self.assertIn("translations", data)

        # Translation structure
        self.assertEqual(len(data["translations"]), 1)
        self.assertIn("language", data["translations"][0])
        self.assertIn("text", data["translations"][0])

        # Metadata structure
        self.assertIn("metadata", data)
        self.assertIn("source_url", data["metadata"])
        self.assertIn("source_name", data["metadata"])
        self.assertIn("scraped_at", data["metadata"])
        self.assertIn("confidence", data["metadata"])


if __name__ == "__main__":
    unittest.main()
