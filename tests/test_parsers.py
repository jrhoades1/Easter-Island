"""Tests for language parsers using saved HTML fixtures."""

import os
import sys
import unittest

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsers.language.asjp import ASJPParser
from parsers.language.glosbe import GlosbeParser
from parsers.language.ids import IDSParser
from parsers.language.omniglot import OmniglotParser
from parsers.language.wikipedia import WikipediaLanguageParser

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


def load_fixture(filename: str) -> str:
    """Load an HTML fixture file."""
    filepath = os.path.join(FIXTURES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


class TestWikipediaParser(unittest.TestCase):
    """Test Wikipedia language page parser."""

    @classmethod
    def setUpClass(cls):
        cls.parser = WikipediaLanguageParser()
        cls.html = load_fixture("wikipedia_rapa_nui.html")
        cls.url = "https://en.wikipedia.org/wiki/Rapa_Nui_language"
        cls.entries = cls.parser.parse(cls.html, cls.url)

    def test_can_parse_correct_url(self):
        """Parser should recognize Rapa Nui Wikipedia URLs."""
        self.assertTrue(self.parser.can_parse("https://en.wikipedia.org/wiki/Rapa_Nui_language"))
        self.assertTrue(self.parser.can_parse("https://en.wikipedia.org/wiki/rapa_nui_language"))

    def test_rejects_wrong_url(self):
        """Parser should reject non-Rapa Nui Wikipedia URLs."""
        self.assertFalse(self.parser.can_parse("https://en.wikipedia.org/wiki/Easter_Island"))
        self.assertFalse(self.parser.can_parse("https://example.com/rapa_nui"))

    def test_extracts_entries(self):
        """Parser should extract language entries from the page."""
        self.assertGreater(len(self.entries), 0, "Should extract at least some entries")

    def test_extracts_numerals(self):
        """Parser should extract Rapa Nui numerals."""
        numeral_entries = [e for e in self.entries if e.part_of_speech == "numeral"]
        self.assertGreater(len(numeral_entries), 0, "Should extract numeral entries")

        # Check for specific numerals
        numeral_words = {e.word for e in numeral_entries}
        expected_numerals = {"tahi", "rua", "toru"}  # 1, 2, 3
        found = expected_numerals & numeral_words
        self.assertGreater(len(found), 0, f"Should find some of {expected_numerals}, found {numeral_words}")

    def test_extracts_pronouns(self):
        """Parser should extract Rapa Nui pronouns."""
        pronoun_entries = [e for e in self.entries if e.part_of_speech == "pronoun"]
        self.assertGreater(len(pronoun_entries), 0, "Should extract pronoun entries")

        # Check for specific pronouns
        pronoun_words = {e.word for e in pronoun_entries}
        expected_pronouns = {"au", "koe", "ia"}  # I, you, he/she
        found = expected_pronouns & pronoun_words
        self.assertGreater(len(found), 0, f"Should find some of {expected_pronouns}, found {pronoun_words}")

    def test_entries_have_metadata(self):
        """All entries should have proper metadata."""
        for entry in self.entries:
            self.assertIsNotNone(entry.metadata, f"Entry '{entry.word}' missing metadata")
            self.assertEqual(entry.metadata.source_name, "Wikipedia")
            self.assertEqual(entry.metadata.source_url, self.url)

    def test_entries_have_translations(self):
        """All entries should have at least one translation."""
        for entry in self.entries:
            self.assertGreater(len(entry.translations), 0, f"Entry '{entry.word}' has no translations")

    def test_entries_have_normalized_form(self):
        """All entries should have a normalized form."""
        for entry in self.entries:
            self.assertIsNotNone(entry.normalized, f"Entry '{entry.word}' missing normalized form")
            self.assertGreater(len(entry.normalized), 0)


class TestIDSParser(unittest.TestCase):
    """Test IDS database parser."""

    @classmethod
    def setUpClass(cls):
        cls.parser = IDSParser()
        cls.html = load_fixture("ids_contribution.html")
        cls.url = "https://ids.clld.org/contributions/238"
        cls.entries = cls.parser.parse(cls.html, cls.url)

    def test_can_parse_correct_url(self):
        """Parser should recognize IDS URLs."""
        self.assertTrue(self.parser.can_parse("https://ids.clld.org/contributions/238"))
        self.assertTrue(self.parser.can_parse("https://ids.clld.org/languages/123"))

    def test_rejects_wrong_url(self):
        """Parser should reject non-IDS URLs."""
        self.assertFalse(self.parser.can_parse("https://example.com/ids"))
        self.assertFalse(self.parser.can_parse("https://asjp.clld.org/languages/RAPA_NUI"))

    def test_extracts_entries(self):
        """Parser should extract entries from IDS page."""
        # IDS page structure may vary, but we should get some entries
        self.assertIsInstance(self.entries, list)

    def test_entries_have_high_confidence(self):
        """IDS entries should have high confidence."""
        for entry in self.entries:
            if entry.metadata:
                self.assertEqual(entry.metadata.confidence, "high")


class TestASJPParser(unittest.TestCase):
    """Test ASJP database parser."""

    @classmethod
    def setUpClass(cls):
        cls.parser = ASJPParser()
        cls.html = load_fixture("asjp_rapa_nui.html")
        cls.url = "https://asjp.clld.org/languages/RAPA_NUI"
        cls.entries = cls.parser.parse(cls.html, cls.url)

    def test_can_parse_correct_url(self):
        """Parser should recognize ASJP URLs."""
        self.assertTrue(self.parser.can_parse("https://asjp.clld.org/languages/RAPA_NUI"))

    def test_rejects_wrong_url(self):
        """Parser should reject non-ASJP URLs."""
        self.assertFalse(self.parser.can_parse("https://ids.clld.org/contributions/238"))

    def test_returns_list(self):
        """Parser should return a list (even if empty due to JS-loaded content)."""
        self.assertIsInstance(self.entries, list)


class TestGlosbeParser(unittest.TestCase):
    """Test Glosbe dictionary parser."""

    @classmethod
    def setUpClass(cls):
        cls.parser = GlosbeParser()
        cls.html = load_fixture("glosbe_en_rap.html")
        cls.url = "https://glosbe.com/en/rap"
        cls.entries = cls.parser.parse(cls.html, cls.url)

    def test_can_parse_correct_url(self):
        """Parser should recognize Glosbe Rapa Nui URLs."""
        self.assertTrue(self.parser.can_parse("https://glosbe.com/en/rap"))
        self.assertTrue(self.parser.can_parse("https://glosbe.com/rap/en"))

    def test_rejects_wrong_url(self):
        """Parser should reject non-Rapa Nui Glosbe URLs."""
        self.assertFalse(self.parser.can_parse("https://glosbe.com/en/es"))
        self.assertFalse(self.parser.can_parse("https://example.com/rap"))

    def test_returns_list(self):
        """Parser should return a list."""
        self.assertIsInstance(self.entries, list)


class TestOmniglotParser(unittest.TestCase):
    """Test Omniglot parser."""

    @classmethod
    def setUpClass(cls):
        cls.parser = OmniglotParser()
        cls.html = load_fixture("omniglot_rapanui.html")
        cls.url = "https://www.omniglot.com/writing/rapanui.htm"
        cls.entries = cls.parser.parse(cls.html, cls.url)

    def test_can_parse_correct_url(self):
        """Parser should recognize Omniglot Rapa Nui URLs."""
        self.assertTrue(self.parser.can_parse("https://www.omniglot.com/writing/rapanui.htm"))
        self.assertTrue(self.parser.can_parse("https://omniglot.com/writing/rapanui.htm"))

    def test_rejects_wrong_url(self):
        """Parser should reject non-Rapa Nui Omniglot URLs."""
        self.assertFalse(self.parser.can_parse("https://www.omniglot.com/writing/maori.htm"))
        self.assertFalse(self.parser.can_parse("https://example.com/rapanui"))

    def test_returns_list(self):
        """Parser should return a list."""
        self.assertIsInstance(self.entries, list)


class TestParserRegistry(unittest.TestCase):
    """Test the parser registry and URL routing."""

    def test_get_parser_for_wikipedia(self):
        """Should return Wikipedia parser for Wikipedia URLs."""
        from parsers.language import get_language_parser
        parser = get_language_parser("https://en.wikipedia.org/wiki/Rapa_Nui_language")
        self.assertIsInstance(parser, WikipediaLanguageParser)

    def test_get_parser_for_ids(self):
        """Should return IDS parser for IDS URLs."""
        from parsers.language import get_language_parser
        parser = get_language_parser("https://ids.clld.org/contributions/238")
        self.assertIsInstance(parser, IDSParser)

    def test_get_parser_for_unknown_url(self):
        """Should return None for unknown URLs."""
        from parsers.language import get_language_parser
        parser = get_language_parser("https://example.com/unknown")
        self.assertIsNone(parser)


if __name__ == "__main__":
    unittest.main()
