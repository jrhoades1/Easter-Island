"""Tablet I (Santiago Staff): Kohaumotu Ia.html search lock.

Cycle 46 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C. Preferred tablet this cycle is I.
Digits are copied from vendored Ia.html (Ir.html is not a published
page). No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. Image track stays parked.

Locks on Ia.html only: Guy's 8-stem delimiter (freq / spans or
absent), the Ca remainder 9-gram, the Aa 10-gram, the Ab 9-gram,
the Bv 8-gram (present/absent), the 004 600 004 sandwich (freq or
absent), longest n with freq≥2, top 8-gram or none, stem count.
Existing A / B / C scoreboards stay the lock.

Search lock, not a merge and not a translation. MockProvider only.
"""

import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_600_sandwich_scoreboard import SANDWICH
from tests.test_mamari_aruku_br_scoreboard import (
    BR_LINE_NAMES,
    STANDING_LONGEST_N as BR_LONGEST_N,
    STANDING_LONGEST_NGRAM as BR_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as BR_STEM_TOTAL,
    br_line_stems,
    extract_br_published_tokens,
    first_non_a_c_tablet,
    load_vendored_br_html,
    score_br_repeating_ngrams,
)
from tests.test_mamari_aruku_bv_scoreboard import (
    BV_LINE_NAMES,
    STANDING_LONGEST_N as BV_LONGEST_N,
    STANDING_LONGEST_NGRAM as BV_8GRAM,
    STANDING_STEM_TOTAL as BV_STEM_TOTAL,
    bv_line_stems,
    extract_bv_published_tokens,
    load_vendored_bv_html,
    score_bv_repeating_ngrams,
)
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
    CITED_TABLETS_URL,
    STANDING_LONGEST_N as AA_LONGEST_N,
    STANDING_LONGEST_NGRAM as AA_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as AA_STEM_TOTAL,
    STANDING_TOP_8GRAM as AA_TOP_8GRAM,
    _TABLET_ROW,
    aa_line_stems,
    extract_aa_published_tokens,
    first_non_c_tablet,
    load_vendored_aa_html,
    load_vendored_catalog_html,
    load_vendored_tablets_html,
    score_aa_repeating_ngrams,
)
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import (
    MOTIF_AB_9GRAM,
    STANDING_AB_MOTIF_FREQ,
    STANDING_AB_MOTIF_SPANS,
)
from tests.test_mamari_tahua_ab_scoreboard import (
    AB_LINE_NAMES,
    STANDING_LONGEST_N as AB_LONGEST_N,
    STANDING_LONGEST_NGRAM as AB_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as AB_STEM_TOTAL,
    ab_line_stems,
    extract_ab_published_tokens,
    load_vendored_ab_html,
    score_ab_repeating_ngrams,
)

IA_HTML_DIR = Path(__file__).parent / "fixtures" / "santiago_ia_html"
IA_HTML_PATH = IA_HTML_DIR / "Ia.html"
I_INDEX_HTML_PATH = IA_HTML_DIR / "I_index.html"
CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_I_INDEX_URL = "http://kohaumotu.org/Rongorongo/I/index.html"
CITED_IA_URL = "http://kohaumotu.org/Rongorongo/I/Ia.html"

IA_LINE_NAMES = tuple(f"Ia{n}" for n in range(1, 15))
STANDING_PAGE_LINE_ORDER = (
    "Ia11",
    "Ia10",
    "Ia9",
    "Ia8",
    "Ia7",
    "Ia6",
    "Ia5",
    "Ia4",
    "Ia3",
    "Ia2",
    "Ia1",
    "Ia14",
    "Ia13",
    "Ia12",
)
STANDING_HTML_BYTES = 25288
STANDING_I_INDEX_BYTES = 5422
STANDING_STEM_COUNTS = (
    179,
    177,
    156,
    168,
    170,
    168,
    179,
    178,
    190,
    192,
    180,
    157,
    194,
    181,
)
STANDING_STEM_TOTAL = 2469
STANDING_GUY_DELIMITER_PRESENT = False
STANDING_GUY_DELIMITER_FREQ = 0
STANDING_GUY_DELIMITER_SPANS = ()
STANDING_MOTIF_9GRAM_PRESENT = False
STANDING_MOTIF_10GRAM_PRESENT = False
STANDING_MOTIF_AB_9GRAM_PRESENT = False
STANDING_MOTIF_BV_8GRAM_PRESENT = False
STANDING_SANDWICH_PRESENT = False
STANDING_SANDWICH_FREQ = 0
STANDING_SANDWICH_SPANS = ()
STANDING_LONGEST_N = 5
STANDING_LONGEST_NGRAM = ("999", "071", "076", "010", "079")
STANDING_LONGEST_FREQ = 3
STANDING_LONGEST_SPANS = (("Ia4", 6, 11), ("Ia4", 25, 30), ("Ia5", 108, 113))
STANDING_TOP_8GRAM = None
STANDING_TOP_8GRAM_FREQ = 0
STANDING_EIGHTGRAM_COUNT = 0
STANDING_TABLET_I = ("I", "I/index.html", "Santiago Staff")
STANDING_FALLBACK_NON_ABC = ("D", "D/index.html", "Échancrée")
STANDING_BARTHEL_PAGE_HREF = "Ia.html"
STANDING_IR_HTML = False


def load_vendored_ia_html() -> str:
    """Return the vendored Kohaumotu Ia.html snapshot."""
    return IA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_i_index_html() -> str:
    """Return the vendored I/index.html snapshot."""
    return I_INDEX_HTML_PATH.read_text(encoding="utf-8")


def extract_ia_published_tokens(html: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Ia.html <td> text.

    Same mechanical copy as Aa.html / Ab.html / Br.html / Bv.html /
    Ca.html / Cb.html. Does not invent numbers. Image cells are skipped.
    """
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"Ia{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def ia_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Ia1–Ia14 as stem sequences in Barthel line order. Search only."""
    return [published_stems(published[name]) for name in IA_LINE_NAMES]


def tablet_i_or_next_non_abc(tablets_html: str) -> tuple[str, str, str] | None:
    """I if that row has an href; else first tablet that is not A, B, or C."""
    i_row = None
    fallback = None
    for letter, href, linked_name, plain_name in _TABLET_ROW.findall(tablets_html):
        _ = plain_name
        if not href:
            continue
        if letter == "I" and i_row is None:
            i_row = (letter, href, linked_name)
        if letter not in ("A", "B", "C") and fallback is None:
            fallback = (letter, href, linked_name)
    return i_row or fallback


def score_ia_repeating_ngrams(lines, analyzer):
    """n≥4 freq≥2 profile on the vendored Ia fixture. Search only."""
    return score_remainder_repeating_ngrams(
        lines, analyzer, line_names=IA_LINE_NAMES
    )


class TestSantiagoIaHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; Horley order keeps IaN names."""
        html = (
            '<h3><a name="Line_11">Line 11</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>430.076-021t-</td></tr></table>"
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td>600-517*</td></tr></table>"
        )
        published = extract_ia_published_tokens(html)
        self.assertEqual(list(published), ["Ia11", "Ia1"])
        self.assertEqual(published["Ia11"], ["430.076", "021t"])
        self.assertEqual(published["Ia1"], ["600", "517"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_prefers_tablet_i_and_falls_back_to_next_non_abc(self):
        """I wins when linked; D is the next non-A/B/C if I is missing."""
        html = (
            "<table>"
            '<tr><td>A</td><td><a href="A/index.html">Tahua</a></td></tr>'
            '<tr><td>B</td><td><a href="B/index.html">Aruku-Kurenga</a></td></tr>'
            '<tr><td>C</td><td><a href="C/index.html">Mamari</a></td></tr>'
            '<tr><td>D</td><td><a href="D/index.html">Échancrée</a></td></tr>'
            '<tr><td>I</td><td><a href="I/index.html">Santiago Staff</a></td></tr>'
            "</table>"
        )
        self.assertEqual(tablet_i_or_next_non_abc(html), STANDING_TABLET_I)
        no_i = html.replace(
            '<tr><td>I</td><td><a href="I/index.html">Santiago Staff</a></td></tr>',
            "",
        )
        self.assertEqual(tablet_i_or_next_non_abc(no_i), STANDING_FALLBACK_NON_ABC)
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIaScoreboard(unittest.TestCase):
    """Cited tablets.html → I → Ia.html lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.catalog = load_vendored_catalog_html()
        self.tablets = load_vendored_tablets_html()
        self.i_index = load_vendored_i_index_html()
        self.html = load_vendored_ia_html()
        self.published = extract_ia_published_tokens(self.html)
        self.lines = ia_line_stems(self.published)
        self.profile = score_ia_repeating_ngrams(self.lines, self.analyzer)

    def test_parent_catalog_selects_santiago_ia(self):
        """Catalog → tablets → I/Santiago Staff → Ia.html. Not an invented URL."""
        self.assertTrue(I_INDEX_HTML_PATH.is_file())
        self.assertTrue(IA_HTML_PATH.is_file())
        self.assertTrue((IA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertEqual(I_INDEX_HTML_PATH.stat().st_size, STANDING_I_INDEX_BYTES)
        self.assertEqual(IA_HTML_PATH.stat().st_size, STANDING_HTML_BYTES)
        self.assertIn('href="tablets.html"', self.catalog)
        self.assertEqual(tablet_i_or_next_non_abc(self.tablets), STANDING_TABLET_I)
        self.assertNotEqual(first_non_c_tablet(self.tablets)[0], "I")
        self.assertNotEqual(first_non_a_c_tablet(self.tablets)[0], "I")
        self.assertIn("Item I:The Santiago Staff", self.i_index)
        self.assertIn(f'href="{STANDING_BARTHEL_PAGE_HREF}"', self.i_index)
        self.assertIn("All lines", self.i_index)
        self.assertNotIn("Ir.html", self.i_index)
        self.assertEqual(STANDING_IR_HTML, False)
        self.assertIn("Item I:Santiago Staff", self.html)
        self.assertIn("Horley", self.html)
        self.assertIn("Rongorongo I", self.html)
        self.assertNotIn("Item A:Tahua", self.html)
        self.assertNotIn("Item C:Mamari", self.html)
        self.assertNotIn("Ir.html", self.html)
        self.assertEqual(list(self.published), list(STANDING_PAGE_LINE_ORDER))
        self.assertEqual(set(self.published), set(IA_LINE_NAMES))
        attribution = (IA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_CATALOG_URL, attribution)
        self.assertIn(CITED_TABLETS_URL, attribution)
        self.assertIn(CITED_I_INDEX_URL, attribution)
        self.assertIn(CITED_IA_URL, attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        lock = self.survey["tablet_i_santiago_staff"]
        self.assertEqual(lock["source_page"], CITED_IA_URL)
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["result"], "ia_html_vendored")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_guys_8stem_delimiter_is_absent(self):
        """Guy 390 041 378 041 670 008 078 711 does not occur on Ia."""
        hits = find_ngram_hits(self.lines, DELIMITER_MOTIF)
        spans = tuple(
            (IA_LINE_NAMES[line_index], start, start + len(DELIMITER_MOTIF))
            for line_index, start in hits
        )
        self.assertEqual(len(hits), STANDING_GUY_DELIMITER_FREQ)
        self.assertEqual(spans, STANDING_GUY_DELIMITER_SPANS)
        self.assertEqual(bool(hits), STANDING_GUY_DELIMITER_PRESENT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ca_aa_ab_bv_motifs_and_sandwich_are_absent(self):
        """Ca 9-gram, Aa 10-gram, Ab 9-gram, Bv 8-gram, and 004 600 004 are absent."""
        self.assertEqual(find_ngram_hits(self.lines, MOTIF_9GRAM), [])
        self.assertEqual(find_ngram_hits(self.lines, MOTIF_10GRAM), [])
        self.assertEqual(find_ngram_hits(self.lines, MOTIF_AB_9GRAM), [])
        self.assertEqual(find_ngram_hits(self.lines, BV_8GRAM), [])
        sandwich = find_ngram_hits(self.lines, SANDWICH)
        spans = tuple(
            (IA_LINE_NAMES[line_index], start, start + len(SANDWICH))
            for line_index, start in sandwich
        )
        self.assertEqual(len(sandwich), STANDING_SANDWICH_FREQ)
        self.assertEqual(spans, STANDING_SANDWICH_SPANS)
        self.assertEqual(bool(sandwich), STANDING_SANDWICH_PRESENT)
        self.assertEqual(bool(find_ngram_hits(self.lines, MOTIF_9GRAM)), STANDING_MOTIF_9GRAM_PRESENT)
        self.assertEqual(bool(find_ngram_hits(self.lines, MOTIF_10GRAM)), STANDING_MOTIF_10GRAM_PRESENT)
        self.assertEqual(
            bool(find_ngram_hits(self.lines, MOTIF_AB_9GRAM)),
            STANDING_MOTIF_AB_9GRAM_PRESENT,
        )
        self.assertEqual(
            bool(find_ngram_hits(self.lines, BV_8GRAM)),
            STANDING_MOTIF_BV_8GRAM_PRESENT,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_n_top_8gram_and_stem_count(self):
        """Longest n with freq≥2 is 5; no repeating 8-gram; 2469 stems."""
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
        self.assertIsNone(p.top_8gram)
        self.assertEqual(STANDING_TOP_8GRAM, None)
        self.assertEqual(STANDING_TOP_8GRAM_FREQ, 0)
        self.assertEqual(len(p.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(STANDING_EIGHTGRAM_COUNT, 0)
        self.assertNotEqual(STANDING_LONGEST_NGRAM, DELIMITER_MOTIF)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_a_b_and_c_scoreboards_still_compute(self):
        """Aa / Ab / Br / Bv / Guy / Ca 9-gram / sandwich / Cb 5-grams stay."""
        aa = aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html()))
        ab = ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html()))
        br = br_line_stems(extract_br_published_tokens(load_vendored_br_html()))
        bv = bv_line_stems(extract_bv_published_tokens(load_vendored_bv_html()))
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

        ab_profile = score_ab_repeating_ngrams(ab, self.analyzer)
        self.assertEqual(sum(len(line) for line in ab), AB_STEM_TOTAL)
        self.assertEqual(ab_profile.longest_n, AB_LONGEST_N)
        self.assertEqual(ab_profile.longest[0].tokens, AB_LONGEST_NGRAM)
        ab_motif = find_ngram_hits(ab, MOTIF_AB_9GRAM)
        self.assertEqual(len(ab_motif), STANDING_AB_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AB_LINE_NAMES[line_index], start, start + len(MOTIF_AB_9GRAM))
                for line_index, start in ab_motif
            ),
            STANDING_AB_MOTIF_SPANS,
        )

        br_profile = score_br_repeating_ngrams(br, self.analyzer)
        self.assertEqual(sum(len(line) for line in br), BR_STEM_TOTAL)
        self.assertEqual(br_profile.longest_n, BR_LONGEST_N)
        self.assertEqual(br_profile.longest[0].tokens, BR_LONGEST_NGRAM)
        self.assertIsNone(br_profile.top_8gram)

        bv_profile = score_bv_repeating_ngrams(bv, self.analyzer)
        self.assertEqual(sum(len(line) for line in bv), BV_STEM_TOTAL)
        self.assertEqual(bv_profile.longest_n, BV_LONGEST_N)
        self.assertEqual(bv_profile.longest[0].tokens, BV_8GRAM)
        self.assertEqual(len(find_ngram_hits(bv, BV_8GRAM)), 2)

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

        self.assertEqual(find_ngram_hits(calendar, SANDWICH), [])
        self.assertEqual(find_ngram_hits(remainder, SANDWICH), [])
        self.assertEqual(find_ngram_hits(cb_lines, SANDWICH), [])
        self.assertEqual(find_ngram_hits(aa, SANDWICH), [])
        self.assertEqual(len(find_ngram_hits(ab, SANDWICH)), 3)
        self.assertEqual(find_ngram_hits(br, SANDWICH), [])
        self.assertEqual(find_ngram_hits(bv, SANDWICH), [])

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
        self.assertEqual(tuple(AA_LINE_NAMES), tuple(f"Aa{n}" for n in range(1, 9)))
        self.assertEqual(tuple(AB_LINE_NAMES), tuple(f"Ab{n}" for n in range(1, 9)))
        self.assertEqual(tuple(BR_LINE_NAMES), tuple(f"Br{n}" for n in range(1, 11)))
        self.assertEqual(tuple(BV_LINE_NAMES), tuple(f"Bv{n}" for n in range(1, 13)))
        self.assertEqual(tuple(IA_LINE_NAMES), tuple(f"Ia{n}" for n in range(1, 15)))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-46 Santiago Staff Ia lock."""
        lock = self.survey["tablet_i_santiago_staff"]
        self.assertEqual(lock["cycle"], 46)
        self.assertEqual(lock["result"], "ia_html_vendored")
        self.assertEqual(lock["tablet"], "I")
        self.assertEqual(lock["name"], "Santiago Staff")
        self.assertEqual(lock["source_page"], CITED_IA_URL)
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["tablet_index"], CITED_I_INDEX_URL)
        self.assertEqual(lock["html_bytes"], STANDING_HTML_BYTES)
        self.assertEqual(lock["index_bytes"], STANDING_I_INDEX_BYTES)
        self.assertFalse(lock["ir_html"])
        self.assertEqual(lock["page_line_order"], list(STANDING_PAGE_LINE_ORDER))
        self.assertEqual(lock["lines"], list(IA_LINE_NAMES))
        self.assertEqual(lock["stem_count"], STANDING_STEM_TOTAL)
        self.assertEqual(lock["stem_counts_by_line"], list(STANDING_STEM_COUNTS))
        self.assertEqual(lock["guy_8stem_delimiter"], STANDING_GUY_DELIMITER_PRESENT)
        self.assertEqual(lock["guy_8stem_delimiter_freq"], STANDING_GUY_DELIMITER_FREQ)
        self.assertEqual(lock["guy_8stem_delimiter_spans"], [])
        self.assertEqual(lock["motif_9gram"], STANDING_MOTIF_9GRAM_PRESENT)
        self.assertEqual(lock["motif_10gram"], STANDING_MOTIF_10GRAM_PRESENT)
        self.assertEqual(lock["motif_ab_9gram"], STANDING_MOTIF_AB_9GRAM_PRESENT)
        self.assertEqual(lock["motif_bv_8gram"], STANDING_MOTIF_BV_8GRAM_PRESENT)
        self.assertEqual(lock["sandwich_004_600_004"], STANDING_SANDWICH_PRESENT)
        self.assertEqual(lock["sandwich_004_600_004_freq"], STANDING_SANDWICH_FREQ)
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertEqual(lock["longest_freq"], STANDING_LONGEST_FREQ)
        self.assertEqual(
            [tuple(span) for span in lock["longest_spans"]],
            list(STANDING_LONGEST_SPANS),
        )
        self.assertIsNone(lock["top_8gram"])
        self.assertEqual(lock["top_8gram_freq"], STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertFalse(lock["top_8gram_is_guy_delimiter"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["aruku_bv_8gram_motif"]["cycle"], 45)
        self.assertEqual(self.survey["tablet_b_aruku_kurenga_verso"]["cycle"], 44)
        self.assertEqual(self.survey["tablet_a_tahua_side_a"]["cycle"], 36)
        self.assertEqual(self.survey["cycle"], 28)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIaImageSnapshot(unittest.TestCase):
    """Cycle 46 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
