"""Tablet A (Tahua) side a: parent-catalog Kohaumotu Aa.html search lock.

Cycle 36 text-search lock. The parent catalog
http://kohaumotu.org/Rongorongo/ is the folder above the already-used
C pages (same publisher, not an invented URL). First non-C tablet with
an extractable Barthel-number HTML page is A / Tahua (preferred).
Digits are copied from vendored Aa.html. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No new
agents. Image track stays parked.

Locks on Aa.html only: Guy's 8-stem delimiter (freq / spans or
absent), the Ca remainder 9-gram (present/absent), each of the three
Cb 5-grams (present/absent), longest n with freq≥2, top 8-gram or
none, stem count. Cycle 37 locks that 10-gram as a motif (hits,
flanks, 8-prefix, C-absent). Cycle 38 vendors the Aa.html verso
Ab.html and locks that side only. Cycle 39 locks that Ab
9-gram as a motif (hits, flanks, 8-prefix, 600-slot,
cross-absent). Existing C scoreboards stay the lock.

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

AA_HTML_DIR = Path(__file__).parent / "fixtures" / "tahua_aa_html"
AA_HTML_PATH = AA_HTML_DIR / "Aa.html"
CATALOG_HTML_PATH = AA_HTML_DIR / "catalog.html"
TABLETS_HTML_PATH = AA_HTML_DIR / "tablets.html"
A_INDEX_HTML_PATH = AA_HTML_DIR / "A_index.html"
CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_A_INDEX_URL = "http://kohaumotu.org/Rongorongo/A/index.html"
CITED_AA_URL = "http://kohaumotu.org/Rongorongo/A/Aa.html"
CITED_CA_URL = "http://kohaumotu.org/Rongorongo/C/Ca.html"
CITED_CB_URL = "http://kohaumotu.org/Rongorongo/C/Cb.html"

AA_LINE_NAMES = tuple(f"Aa{n}" for n in range(1, 9))
STANDING_HTML_BYTES = 11287
STANDING_CATALOG_BYTES = 4697
STANDING_TABLETS_BYTES = 9087
STANDING_A_INDEX_BYTES = 5556
STANDING_STEM_COUNTS = (116, 108, 98, 114, 104, 111, 134, 121)
STANDING_STEM_TOTAL = 906
STANDING_GUY_DELIMITER_PRESENT = False
STANDING_GUY_DELIMITER_FREQ = 0
STANDING_GUY_DELIMITER_SPANS = ()
STANDING_MOTIF_PRESENT = False
STANDING_CB_5GRAM_PRESENT = (False, False, False)
STANDING_LONGEST_N = 10
STANDING_LONGEST_NGRAM = (
    "080",
    "004",
    "280",
    "182",
    "048",
    "022",
    "025",
    "025",
    "009",
    "005",
)
STANDING_TOP_8GRAM = (
    "080",
    "004",
    "280",
    "182",
    "048",
    "022",
    "025",
    "025",
)
STANDING_TOP_8GRAM_FREQ = 2
STANDING_EIGHTGRAM_COUNT = 3
STANDING_FIRST_NON_C = ("A", "A/index.html", "Tahua")
STANDING_BARTHEL_PAGE_HREF = "Aa.html"

_TABLET_ROW = re.compile(
    r"<td>([A-Z])</td>\s*<td>(?:<a href=\"([^\"]+)\">([^<]+)</a>|([^<]+))</td>",
    re.DOTALL,
)


def load_vendored_aa_html() -> str:
    """Return the vendored Kohaumotu Aa.html snapshot."""
    return AA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_catalog_html() -> str:
    """Return the vendored parent catalog snapshot."""
    return CATALOG_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_tablets_html() -> str:
    """Return the vendored tablets.html snapshot."""
    return TABLETS_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_a_index_html() -> str:
    """Return the vendored A/index.html snapshot."""
    return A_INDEX_HTML_PATH.read_text(encoding="utf-8")


def extract_aa_published_tokens(html: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Aa.html <td> text.

    Same mechanical copy as Ca.html / Cb.html. Does not invent
    numbers. Image cells are skipped.
    """
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"Aa{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def aa_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Aa1–Aa8 as stem sequences. Search only."""
    return [published_stems(published[name]) for name in AA_LINE_NAMES]


def first_non_c_tablet(tablets_html: str) -> tuple[str, str, str] | None:
    """First non-C tablet row that has an href. Does not invent a URL."""
    for letter, href, linked_name, plain_name in _TABLET_ROW.findall(tablets_html):
        if letter == "C":
            continue
        if href:
            return (letter, href, linked_name)
        _ = plain_name
    return None


def score_aa_repeating_ngrams(lines, analyzer):
    """n≥4 freq≥2 profile on the vendored Aa fixture. Search only."""
    return score_remainder_repeating_ngrams(
        lines, analyzer, line_names=AA_LINE_NAMES
    )


class TestTahuaAaHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; lines are named AaN."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>430!.040-320.009-</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>080.004-280*</td></tr></table>"
        )
        published = extract_aa_published_tokens(html)
        self.assertEqual(published["Aa1"], ["430!.040", "320.009"])
        self.assertEqual(published["Aa2"], ["080.004", "280*"])

    def test_first_non_c_skips_mamari(self):
        """C is skipped; first linked other tablet wins."""
        html = (
            "<table>"
            '<tr><td>C</td><td><a href="C/index.html">Mamari</a></td></tr>'
            '<tr><td>A</td><td><a href="A/index.html">Tahua</a></td></tr>'
            "</table>"
        )
        self.assertEqual(first_non_c_tablet(html), ("A", "A/index.html", "Tahua"))
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])


class TestMamariTahuaAaScoreboard(unittest.TestCase):
    """Cited parent-catalog Aa.html lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.catalog = load_vendored_catalog_html()
        self.tablets = load_vendored_tablets_html()
        self.a_index = load_vendored_a_index_html()
        self.html = load_vendored_aa_html()
        self.published = extract_aa_published_tokens(self.html)
        self.lines = aa_line_stems(self.published)
        self.profile = score_aa_repeating_ngrams(self.lines, self.analyzer)

    def test_parent_catalog_selects_tahua_aa(self):
        """Catalog → tablets → A/Tahua → Aa.html. Not an invented URL."""
        self.assertTrue(CATALOG_HTML_PATH.is_file())
        self.assertTrue(TABLETS_HTML_PATH.is_file())
        self.assertTrue(A_INDEX_HTML_PATH.is_file())
        self.assertTrue(AA_HTML_PATH.is_file())
        self.assertTrue((AA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertEqual(CATALOG_HTML_PATH.stat().st_size, STANDING_CATALOG_BYTES)
        self.assertEqual(TABLETS_HTML_PATH.stat().st_size, STANDING_TABLETS_BYTES)
        self.assertEqual(A_INDEX_HTML_PATH.stat().st_size, STANDING_A_INDEX_BYTES)
        self.assertEqual(AA_HTML_PATH.stat().st_size, STANDING_HTML_BYTES)
        self.assertIn('href="tablets.html"', self.catalog)
        self.assertNotIn('name="Line_1"', self.catalog)
        self.assertEqual(first_non_c_tablet(self.tablets), STANDING_FIRST_NON_C)
        self.assertIn("Item A:Tahua", self.a_index)
        self.assertIn(f'href="{STANDING_BARTHEL_PAGE_HREF}"', self.a_index)
        self.assertIn("Side a (all lines)", self.a_index)
        self.assertIn("Item A:Tahua", self.html)
        self.assertIn("Side a", self.html)
        self.assertIn("Rongorongo Aa", self.html)
        self.assertNotIn("Item C:Mamari", self.html)
        self.assertEqual(list(self.published), list(AA_LINE_NAMES))
        attribution = (AA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_CATALOG_URL, attribution)
        self.assertIn(CITED_TABLETS_URL, attribution)
        self.assertIn(CITED_A_INDEX_URL, attribution)
        self.assertIn(CITED_AA_URL, attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        lock = self.survey["tablet_a_tahua_side_a"]
        self.assertEqual(lock["source_page"], CITED_AA_URL)
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["result"], "aa_html_vendored")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_guys_8stem_delimiter_is_absent(self):
        """Guy 390 041 378 041 670 008 078 711 does not occur on Aa."""
        hits = find_ngram_hits(self.lines, DELIMITER_MOTIF)
        spans = tuple(
            (AA_LINE_NAMES[line_index], start, start + len(DELIMITER_MOTIF))
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
        self.assertEqual(bool(hits), STANDING_MOTIF_PRESENT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_three_cb_5grams_are_absent(self):
        """Each cycle-33 Cb longest 5-gram is absent on Aa."""
        present = tuple(
            bool(find_ngram_hits(self.lines, gram)) for gram in CB_5GRAMS
        )
        self.assertEqual(present, STANDING_CB_5GRAM_PRESENT)
        self.assertEqual(len(CB_5GRAMS), 3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_n_top_8gram_and_stem_count(self):
        """Longest n with freq≥2 is 10; top 8-gram is not Guy; 906 stems."""
        p = self.profile
        self.assertEqual(
            [len(line) for line in self.lines],
            list(STANDING_STEM_COUNTS),
        )
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_STEM_TOTAL)
        self.assertEqual(p.longest_n, STANDING_LONGEST_N)
        self.assertEqual(p.longest[0].tokens, STANDING_LONGEST_NGRAM)
        self.assertEqual(p.top_8gram.tokens, STANDING_TOP_8GRAM)
        self.assertEqual(p.top_8gram.freq, STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(len(p.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertNotEqual(p.top_8gram.tokens, DELIMITER_MOTIF)
        self.assertGreaterEqual(STANDING_EIGHTGRAM_COUNT, 1)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_c_scoreboards_still_compute(self):
        """Guy / Ca 9-gram / three Cb 5-grams / longest-n locks on C only."""
        calendar = fixture_line_stems(load_mamari_fixture())
        remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        cb_lines = cb_line_stems(extract_cb_published_tokens(load_vendored_cb_html()))
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
        """CORPUS_SURVEY.json records the cycle-36 Tahua Aa lock."""
        lock = self.survey["tablet_a_tahua_side_a"]
        self.assertEqual(lock["cycle"], 36)
        self.assertEqual(lock["result"], "aa_html_vendored")
        self.assertEqual(lock["tablet"], "A")
        self.assertEqual(lock["name"], "Tahua")
        self.assertEqual(lock["source_page"], CITED_AA_URL)
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["tablet_index"], CITED_A_INDEX_URL)
        self.assertEqual(lock["html_bytes"], STANDING_HTML_BYTES)
        self.assertEqual(lock["lines"], list(AA_LINE_NAMES))
        self.assertEqual(lock["stem_count"], STANDING_STEM_TOTAL)
        self.assertEqual(lock["stem_counts_by_line"], list(STANDING_STEM_COUNTS))
        self.assertEqual(lock["guy_8stem_delimiter"], STANDING_GUY_DELIMITER_PRESENT)
        self.assertEqual(lock["guy_8stem_delimiter_freq"], STANDING_GUY_DELIMITER_FREQ)
        self.assertEqual(lock["guy_8stem_delimiter_spans"], [])
        self.assertEqual(lock["motif_9gram"], STANDING_MOTIF_PRESENT)
        self.assertEqual(
            [row[1] for row in lock["cb_5grams"]],
            list(STANDING_CB_5GRAM_PRESENT),
        )
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertEqual(tuple(lock["top_8gram"]), STANDING_TOP_8GRAM)
        self.assertEqual(lock["top_8gram_freq"], STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertFalse(lock["top_8gram_is_guy_delimiter"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["off_tablet_c_ceiling"]["cycle"], 35)
        self.assertEqual(self.survey["cycle"], 28)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariTahuaAaImageSnapshot(unittest.TestCase):
    """Cycle 36 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
