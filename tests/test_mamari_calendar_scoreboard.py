"""Scoreboard: n-gram / structural analyzers on Mamari Ca6–Ca9.

Non-LLM check that the existing pattern-mining analyzers recover the one
widely accepted readable structure in Rongorongo — the stereotyped repeating
delimiter on Tablet C (Mamari) Ca6–Ca9 — when fed a published Barthel-coded
transcription.

Fail condition: the delimiter motif is missing from the top-N n-grams of
matching length, or a same-length n-gram outranks it.

Sources and extraction limits are recorded on the fixture
(tests/fixtures/mamari_ca6_ca9_barthel.json). Glyph meanings are not assigned.
"""

import json
import re
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.lexical_validation.historical_validator import (
    HistoricalContext,
    HistoricalValidator,
)
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from agents.pattern_mining.structural_patterns import StructuralPatternAnalyzer

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "mamari_ca6_ca9_barthel.json"

# Guy 1990: eight-glyph separator "390.41 378y 41 V631B 8.78.711", after
# mechanical Barthel-stem tokenization (ligature split + allograph letters
# stripped). Kohaumotu writes 670 where Guy writes V631B.
DELIMITER_MOTIF = ("390", "041", "378", "041", "670", "008", "078", "711")

# Rank window for same-length n-grams. Fail if the motif is outside this
# window, or if any same-length n-gram has a strictly higher frequency.
TOP_N = 3

# Strip Barthel orientation / allograph marks (40A, 378y, 041h, V670, 002V?).
_ALLOGRAPH_MARKS = re.compile(r"[A-Za-z?*!]+")


def load_mamari_fixture() -> dict:
    """Load the published Ca6–Ca9 Barthel fixture."""
    with FIXTURE_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def barthel_stems(tokens: list[str]) -> list[str]:
    """Mechanical Barthel-number stems. Does not invent or remap types.

    Hyphen-separated published tokens are already split by the fixture.
    Ligatures (390.041, 008.078.711) are split on '.'; letter suffixes and
    a leading V (Guy/Barthel orientation) are stripped so 378y and 041h
    collapse to their published type numbers. 315y and 375 are left distinct
    from 378 — those first-delimiter variants are not remapped.
    """
    stems: list[str] = []
    for token in tokens:
        piece = token.strip().rstrip("*")
        if not piece:
            continue
        for part in piece.split("."):
            part = part.strip()
            if not part:
                continue
            if part.startswith("V") and len(part) > 1 and part[1].isdigit():
                part = part[1:]
            part = _ALLOGRAPH_MARKS.sub("", part)
            if part.isdigit():
                stems.append(part.zfill(3))
    return stems


def fixture_line_stems(data: dict) -> list[list[str]]:
    """Return Ca6–Ca9 lines as Barthel-stem sequences."""
    lines = data["lines"]
    return [barthel_stems(lines[name]) for name in ("Ca6", "Ca7", "Ca8", "Ca9")]


class TestMamariCalendarScoreboard(unittest.TestCase):
    """Recover the Mamari delimiter / repetition from published Barthel numbers."""

    def setUp(self):
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.structural_analyzer = StructuralPatternAnalyzer(llm_provider=self.provider)
        self.fixture = load_mamari_fixture()
        self.lines = fixture_line_stems(self.fixture)

    def test_fixture_is_cited_published_barthel(self):
        """Fixture must cite a real published encoding, not invented numbers."""
        source = self.fixture["source"]
        self.assertIn("kohaumotu.org", source["primary"]["url"])
        self.assertTrue(self.fixture["lines"]["Ca7"])
        self.assertTrue(self.fixture["lines"]["Ca8"])
        dois = {item.get("doi") for item in source["scholarship"]}
        self.assertIn("10.3406/jso.1990.2882", dois)

    def test_delimiter_motif_ranks_in_top_n_ngrams(self):
        """Guy's 8-glyph delimiter must top same-length n-grams."""
        n = len(DELIMITER_MOTIF)
        ngrams = self.ngram_analyzer.extract_ngrams(self.lines, n=n, min_frequency=2)

        self.assertTrue(ngrams, "no repeating 8-grams recovered from Ca6–Ca9")

        ranks = [i for i, (gram, _freq) in enumerate(ngrams) if gram == DELIMITER_MOTIF]
        self.assertTrue(
            ranks,
            "delimiter motif missing from 8-grams "
            f"(top were {ngrams[:TOP_N]})",
        )
        rank = ranks[0]
        self.assertLess(
            rank,
            TOP_N,
            f"delimiter motif ranked {rank + 1}, outside top-{TOP_N}: {ngrams[:TOP_N]}",
        )
        motif_freq = ngrams[rank][1]
        best_freq = ngrams[0][1]
        self.assertGreaterEqual(
            motif_freq,
            best_freq,
            f"same-length noise outranks delimiter ({ngrams[0]} vs motif freq {motif_freq})",
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_structural_analyzer_emits_repetition(self):
        """Consecutive night-sign runs (glyph 040) must yield a repetition pattern."""
        patterns = self.structural_analyzer.find_repetition_patterns(
            self.lines, min_frequency=2
        )
        repetitions = [p for p in patterns if p.pattern_type == "repetition"]
        self.assertTrue(repetitions, "no repetition pattern emitted")
        self.assertTrue(
            any("040" in p.glyph_ids for p in repetitions),
            f"repetition patterns did not include night-sign 040: {repetitions}",
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_historical_validator_still_flags_calendar(self):
        """Existing HistoricalContext hook still classifies a time-domain item as calendar."""
        self.assertIn("calendar", HistoricalContext.KNOWN_TEXT_TYPES)
        expected = HistoricalContext.KNOWN_TEXT_TYPES["calendar"]["expected_patterns"]
        self.assertIn("repetitive sequences", expected)

        validator = HistoricalValidator(llm_provider=self.provider)
        result = validator.validate(
            {
                "reference_id": "mamari-ca6-ca9",
                "language_entry_word": "mahina",
                "semantic_domain": "time",
            }
        )
        self.assertEqual(result.text_type_match, "calendar")
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
