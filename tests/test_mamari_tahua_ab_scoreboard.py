"""Tablet A (Tahua) side b: Kohaumotu Ab.html search lock.

Cycle 38 text-search lock. Same Kohaumotu tablet-A source already
used for Aa (verso of the cited Aa.html). Digits are copied from
vendored Ab.html. No invented Barthel. No G00n→Barthel map. No
type merge. No detector retune. No CV. No new agents. Image
track stays parked.

Locks on Ab.html only: the cycle-37 Aa 10-gram motif (freq / spans
or absent), Guy's 8-stem delimiter (freq / spans or absent), the
Ca remainder 9-gram (present/absent), longest n with freq≥2, top
8-gram or none, stem count. Existing Aa / C scoreboards stay the
lock.

Search lock, not a merge and not a translation. MockProvider only.
"""

import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_cb_5gram_ca_cross_scoreboard import (
    CB_5GRAMS,
    STANDING_CA_CROSS_TABLE,
    score_cb_5gram_ca_cross,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CB_EIGHTGRAM_COUNT,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CB_LONGEST_N,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_NGRAMS,
    score_cb_repeating_ngrams,
)
from tests.test_mamari_cb_side_b_scoreboard import (
    CB_LINE_NAMES,
    cb_line_stems,
    extract_cb_published_tokens,
    load_vendored_cb_html,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import MOTIF_9GRAM
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CA_REMAINDER_EIGHTGRAM_COUNT,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CA_REMAINDER_LONGEST_N,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    REMAINDER_LINE_NAMES,
    _LINE_HEADER,
    extract_ca_published_tokens,
    find_ngram_hits,
    load_corpus_survey,
    load_vendored_ca_html,
    published_stems,
    remainder_line_stems,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import (
    MOTIF_10GRAM,
    STANDING_AA_MOTIF_FREQ,
    STANDING_AA_MOTIF_SPANS,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    AA_LINE_NAMES,
    CITED_AA_URL,
    STANDING_LONGEST_N as AA_LONGEST_N,
    STANDING_LONGEST_NGRAM as AA_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as AA_STEM_TOTAL,
    STANDING_TOP_8GRAM as AA_TOP_8GRAM,
    aa_line_stems,
    extract_aa_published_tokens,
    load_vendored_a_index_html,
    load_vendored_aa_html,
    score_aa_repeating_ngrams,
)

AB_HTML_DIR = Path(__file__).parent / "fixtures" / "tahua_ab_html"
AB_HTML_PATH = AB_HTML_DIR / "Ab.html"
CITED_AB_URL = "http://kohaumotu.org/Rongorongo/A/Ab.html"
CITED_A_INDEX_URL = "http://kohaumotu.org/Rongorongo/A/index.html"
CITED_CA_URL = "http://kohaumotu.org/Rongorongo/C/Ca.html"
CITED_CB_URL = "http://kohaumotu.org/Rongorongo/C/Cb.html"

AB_LINE_NAMES = tuple(f"Ab{n}" for n in range(1, 9))
STANDING_HTML_BYTES = 11257
STANDING_STEM_COUNTS = (108, 121, 123, 116, 112, 128, 109, 109)
STANDING_STEM_TOTAL = 926
STANDING_GUY_DELIMITER_PRESENT = False
STANDING_GUY_DELIMITER_FREQ = 0
STANDING_GUY_DELIMITER_SPANS = ()
STANDING_MOTIF_9GRAM_PRESENT = False
STANDING_MOTIF_10GRAM_PRESENT = False
STANDING_MOTIF_10GRAM_FREQ = 0
STANDING_MOTIF_10GRAM_SPANS = ()
STANDING_LONGEST_N = 9
STANDING_LONGEST_NGRAM = (
    "605",
    "003",
    "004",
    "600",
    "004",
    "003",
    "040",
    "003",
    "050",
)
STANDING_LONGEST_FREQ = 2
STANDING_LONGEST_SPANS = (("Ab3", 2, 11), ("Ab5", 13, 22))
STANDING_TOP_8GRAM = (
    "605",
    "003",
    "004",
    "600",
    "004",
    "003",
    "040",
    "003",
)
STANDING_TOP_8GRAM_FREQ = 2
STANDING_EIGHTGRAM_COUNT = 3


def load_vendored_ab_html() -> str:
    """Return the vendored Kohaumotu Ab.html snapshot."""
    return AB_HTML_PATH.read_text(encoding="utf-8")


def extract_ab_published_tokens(html: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Ab.html <td> text.

    Same mechanical copy as Aa.html / Ca.html / Cb.html. Does not
    invent numbers. Image cells are skipped.
    """
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"Ab{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def ab_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Ab1–Ab8 as stem sequences. Search only."""
    return [published_stems(published[name]) for name in AB_LINE_NAMES]


def score_ab_repeating_ngrams(lines, analyzer):
    """n≥4 freq≥2 profile on the vendored Ab fixture. Search only."""
    return score_remainder_repeating_ngrams(
        lines, analyzer, line_names=AB_LINE_NAMES
    )


class TestTahuaAbHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; lines are named AbN."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>079-005:042-005j-</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>605.003a-004*</td></tr></table>"
        )
        published = extract_ab_published_tokens(html)
        self.assertEqual(published["Ab1"], ["079", "005:042", "005j"])
        self.assertEqual(published["Ab2"], ["605.003a", "004*"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])


class TestMamariTahuaAbScoreboard(unittest.TestCase):
    """Cited Aa.html verso Ab.html lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.aa_html = load_vendored_aa_html()
        self.a_index = load_vendored_a_index_html()
        self.html = load_vendored_ab_html()
        self.published = extract_ab_published_tokens(self.html)
        self.lines = ab_line_stems(self.published)
        self.profile = score_ab_repeating_ngrams(self.lines, self.analyzer)

    def test_verso_of_cited_aa_is_vendored(self):
        """Aa.html navbar / A index already link Ab.html. Not an invented URL."""
        self.assertTrue(AB_HTML_PATH.is_file())
        self.assertTrue((AB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertEqual(AB_HTML_PATH.stat().st_size, STANDING_HTML_BYTES)
        self.assertIn('href="Ab.html"', self.aa_html)
        self.assertIn("side b", self.aa_html)
        self.assertIn('href="Ab.html"', self.a_index)
        self.assertIn("Side b (all lines)", self.a_index)
        self.assertIn("Item A:Tahua", self.html)
        self.assertIn("Side b", self.html)
        self.assertIn("Rongorongo Ab", self.html)
        self.assertNotIn("Item C:Mamari", self.html)
        self.assertNotIn("Side a", self.html)
        self.assertEqual(list(self.published), list(AB_LINE_NAMES))
        attribution = (AB_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_AB_URL, attribution)
        self.assertIn(CITED_AA_URL, attribution)
        self.assertIn(CITED_A_INDEX_URL, attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        lock = self.survey["tablet_a_tahua_side_b"]
        self.assertEqual(lock["source_page"], CITED_AB_URL)
        self.assertEqual(lock["verso_of"], CITED_AA_URL)
        self.assertEqual(lock["result"], "ab_html_vendored")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_aa_10gram_motif_is_absent(self):
        """080 004 280 182 048 022 025 025 009 005 does not occur on Ab."""
        hits = find_ngram_hits(self.lines, MOTIF_10GRAM)
        spans = tuple(
            (AB_LINE_NAMES[line_index], start, start + len(MOTIF_10GRAM))
            for line_index, start in hits
        )
        self.assertEqual(len(hits), STANDING_MOTIF_10GRAM_FREQ)
        self.assertEqual(spans, STANDING_MOTIF_10GRAM_SPANS)
        self.assertEqual(bool(hits), STANDING_MOTIF_10GRAM_PRESENT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_guys_8stem_delimiter_is_absent(self):
        """Guy 390 041 378 041 670 008 078 711 does not occur on Ab."""
        hits = find_ngram_hits(self.lines, DELIMITER_MOTIF)
        spans = tuple(
            (AB_LINE_NAMES[line_index], start, start + len(DELIMITER_MOTIF))
            for line_index, start in hits
        )
        self.assertEqual(len(hits), STANDING_GUY_DELIMITER_FREQ)
        self.assertEqual(spans, STANDING_GUY_DELIMITER_SPANS)
        self.assertEqual(bool(hits), STANDING_GUY_DELIMITER_PRESENT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ca_9gram_is_absent(self):
        """Remainder motif 002 010 070 760 040 006 430 047 002 is absent."""
        hits = find_ngram_hits(self.lines, MOTIF_9GRAM)
        self.assertEqual(hits, [])
        self.assertEqual(bool(hits), STANDING_MOTIF_9GRAM_PRESENT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_n_top_8gram_and_stem_count(self):
        """Longest n with freq≥2 is 9; top 8-gram is not Guy; 926 stems."""
        p = self.profile
        self.assertEqual(
            [len(line) for line in self.lines],
            list(STANDING_STEM_COUNTS),
        )
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_STEM_TOTAL)
        self.assertEqual(p.longest_n, STANDING_LONGEST_N)
        self.assertEqual(p.longest[0].tokens, STANDING_LONGEST_NGRAM)
        self.assertEqual(p.longest[0].freq, STANDING_LONGEST_FREQ)
        self.assertEqual(p.longest[0].spans, STANDING_LONGEST_SPANS)
        self.assertEqual(p.top_8gram.tokens, STANDING_TOP_8GRAM)
        self.assertEqual(p.top_8gram.freq, STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(len(p.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertNotEqual(p.top_8gram.tokens, DELIMITER_MOTIF)
        self.assertEqual(STANDING_TOP_8GRAM, STANDING_LONGEST_NGRAM[:8])
        self.assertGreaterEqual(STANDING_EIGHTGRAM_COUNT, 1)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_aa_and_c_scoreboards_still_compute(self):
        """Aa 10-gram / Guy / Ca 9-gram / Cb 5-grams / longest-n stay."""
        aa = aa_line_stems(extract_aa_published_tokens(self.aa_html))
        calendar = fixture_line_stems(load_mamari_fixture())
        remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        cb_lines = cb_line_stems(extract_cb_published_tokens(load_vendored_cb_html()))

        aa_profile = score_aa_repeating_ngrams(aa, self.analyzer)
        self.assertEqual(sum(len(line) for line in aa), AA_STEM_TOTAL)
        self.assertEqual(aa_profile.longest_n, AA_LONGEST_N)
        self.assertEqual(aa_profile.longest[0].tokens, AA_LONGEST_NGRAM)
        self.assertEqual(aa_profile.top_8gram.tokens, AA_TOP_8GRAM)
        aa_motif = find_ngram_hits(aa, MOTIF_10GRAM)
        self.assertEqual(len(aa_motif), STANDING_AA_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AA_LINE_NAMES[line_index], start, start + len(MOTIF_10GRAM))
                for line_index, start in aa_motif
            ),
            STANDING_AA_MOTIF_SPANS,
        )

        guy_cal = find_ngram_hits(calendar, DELIMITER_MOTIF)
        guy_rem = find_ngram_hits(remainder, DELIMITER_MOTIF)
        guy_cb = find_ngram_hits(cb_lines, DELIMITER_MOTIF)
        self.assertTrue(guy_cal)
        self.assertEqual(guy_rem, [])
        self.assertEqual(guy_cb, [])

        motif_cal = find_ngram_hits(calendar, MOTIF_9GRAM)
        motif_rem = find_ngram_hits(remainder, MOTIF_9GRAM)
        motif_cb = find_ngram_hits(cb_lines, MOTIF_9GRAM)
        self.assertEqual(motif_cal, [])
        self.assertEqual(len(motif_rem), 2)
        self.assertEqual(motif_cb, [])

        cross = score_cb_5gram_ca_cross(
            CB_5GRAMS,
            calendar,
            CALENDAR_LINE_NAMES,
            remainder,
            REMAINDER_LINE_NAMES,
        )
        locked = tuple((row.tokens, row.calendar_hits, row.remainder_hits) for row in cross)
        self.assertEqual(locked, STANDING_CA_CROSS_TABLE)
        for gram in CB_5GRAMS:
            self.assertTrue(find_ngram_hits(cb_lines, gram))

        rem_profile = score_remainder_repeating_ngrams(remainder, self.analyzer)
        cb_profile = score_cb_repeating_ngrams(cb_lines, self.analyzer)
        self.assertEqual(rem_profile.longest_n, CA_REMAINDER_LONGEST_N)
        self.assertEqual(len(rem_profile.eightgrams), CA_REMAINDER_EIGHTGRAM_COUNT)
        self.assertGreaterEqual(CA_REMAINDER_EIGHTGRAM_COUNT, 1)
        self.assertEqual(cb_profile.longest_n, CB_LONGEST_N)
        self.assertEqual(len(cb_profile.eightgrams), CB_EIGHTGRAM_COUNT)
        self.assertEqual(CB_EIGHTGRAM_COUNT, 0)
        self.assertEqual(
            tuple(row.tokens for row in cb_profile.longest),
            tuple(tokens for tokens, _n, _freq, _spans in STANDING_LONGEST_NGRAMS),
        )
        self.assertEqual(tuple(CB_LINE_NAMES), tuple(f"Cb{n}" for n in range(1, 15)))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-38 Tahua Ab lock."""
        lock = self.survey["tablet_a_tahua_side_b"]
        self.assertEqual(lock["cycle"], 38)
        self.assertEqual(lock["result"], "ab_html_vendored")
        self.assertEqual(lock["tablet"], "A")
        self.assertEqual(lock["name"], "Tahua")
        self.assertEqual(lock["source_page"], CITED_AB_URL)
        self.assertEqual(lock["verso_of"], CITED_AA_URL)
        self.assertEqual(lock["tablet_index"], CITED_A_INDEX_URL)
        self.assertEqual(lock["html_bytes"], STANDING_HTML_BYTES)
        self.assertEqual(lock["lines"], list(AB_LINE_NAMES))
        self.assertEqual(lock["stem_count"], STANDING_STEM_TOTAL)
        self.assertEqual(lock["stem_counts_by_line"], list(STANDING_STEM_COUNTS))
        self.assertEqual(lock["motif_10gram"], STANDING_MOTIF_10GRAM_PRESENT)
        self.assertEqual(lock["motif_10gram_freq"], STANDING_MOTIF_10GRAM_FREQ)
        self.assertEqual(lock["motif_10gram_spans"], [])
        self.assertEqual(tuple(lock["motif_10gram_tokens"]), MOTIF_10GRAM)
        self.assertEqual(lock["guy_8stem_delimiter"], STANDING_GUY_DELIMITER_PRESENT)
        self.assertEqual(lock["guy_8stem_delimiter_freq"], STANDING_GUY_DELIMITER_FREQ)
        self.assertEqual(lock["guy_8stem_delimiter_spans"], [])
        self.assertEqual(lock["motif_9gram"], STANDING_MOTIF_9GRAM_PRESENT)
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertEqual(lock["longest_freq"], STANDING_LONGEST_FREQ)
        self.assertEqual(
            [tuple(span) for span in lock["longest_spans"]],
            list(STANDING_LONGEST_SPANS),
        )
        self.assertEqual(tuple(lock["top_8gram"]), STANDING_TOP_8GRAM)
        self.assertEqual(lock["top_8gram_freq"], STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertFalse(lock["top_8gram_is_guy_delimiter"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["cycle"], 37)
        self.assertEqual(self.survey["tablet_a_tahua_side_a"]["cycle"], 36)
        self.assertEqual(self.survey["cycle"], 28)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariTahuaAbImageSnapshot(unittest.TestCase):
    """Cycle 38 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
