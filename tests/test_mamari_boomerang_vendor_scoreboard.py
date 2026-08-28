"""Boomerang / Berlin (O) vendor lock.

Cycle 92 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / L /
M / N / P / Q. HEAD-check before filename assume (cycle 54 Gr vs Ga;
cycle 79 Da vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs Fa; cycle 86
Jb vs Ja; cycle 87 Lb vs La; cycle 88 Mb vs Ma; cycle 89 Nr vs Na):
Ob.html / Or.html / Ov.html / O.html are unpublished 404s.
O/index.html lists ba_Oa.html, not Oa.html. Oa.html is still a
200 Barthel page with name="Line_N" anchors (Fischer-renumbered
Oa3–Oa9). Catalog name is Boomerang — not Vienna / London /
Reimiro. Digits are copied from the snapshots. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. No second new letter.

Locks the vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; exact hits of M's n=4
006 022 006 022; exact hits of N's n=6 004 064 034 006 004 064;
O's own longest repeating n-gram (n and whether n≥8 exists). N's
locked facts stay. Claim that can lose: known tradition islands,
E islands, M's n=4, and N's n=6 are exact-0 on O (closed-tradition
hold-out). O has no repeating n≥4, so the hold-out is the lock
that can leak.

Search lock, not a merge and not a translation. MockProvider only.
"""

import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_gk_islands_off_hpq_scoreboard import (
    LOCKED_GRAMS as GK_LOCKED_GRAMS,
)
from tests.test_mamari_hpq_island_off_hpq_scoreboard import (
    LOCKED_ISLANDS as HPQ_LOCKED_ISLANDS,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
    GRAM4 as ER7_GRAM4,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
    GRAM8 as ER7_GRAM8,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    GRAM_N9 as E_GRAM_N9,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    extract_published_tokens,
    side_line_stems,
    tablet_row,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ib_scoreboard import (
    published_all_lines_hrefs,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_vienna_na1_n_only_scoreboard import (
    TestMamariSmallViennaNa1NOnlyScoreboard,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    TestMamariSmallViennaVendorScoreboard,
)
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html
from tests.test_mamari_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
)

OA_HTML_DIR = Path(__file__).parent / "fixtures" / "boomerang_oa_html"
OA_HTML_PATH = OA_HTML_DIR / "Oa.html"
O_INDEX_HTML_PATH = OA_HTML_DIR / "O_index.html"
OA_JSON_PATH = OA_HTML_DIR / "Oa_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_O_INDEX_URL = "http://kohaumotu.org/Rongorongo/O/index.html"
CITED_OA_URL = "http://kohaumotu.org/Rongorongo/O/Oa.html"

SIDE_OA = "Oa"
O_SIDES = (SIDE_OA,)

OA_LINE_NAMES = tuple(f"Oa{n}" for n in range(3, 10))
O_LINE_NAMES = {SIDE_OA: OA_LINE_NAMES}

STANDING_OA_BYTES = 3658
STANDING_O_INDEX_BYTES = 3734
STANDING_OA_STEM_COUNTS = (12, 24, 19, 24, 12, 17, 9)
STANDING_STEM_TOTALS = {SIDE_OA: 117}
STANDING_STEM_COUNTS = {SIDE_OA: STANDING_OA_STEM_COUNTS}
STANDING_O_ALL_LINES = ()
STANDING_INDEX_BARTHEL_HREF = "ba_Oa.html"
STANDING_TABLET_O = ("O", "O/index.html", "Boomerang")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in O_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in O_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in O_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in O_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in O_SIDES}
STANDING_M_N4_HITS = {side: 0 for side in O_SIDES}
STANDING_N_N6_HITS = {side: 0 for side in O_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_M_N4 = False
STANDING_ANY_N_N6 = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 0
STANDING_LONGEST_NGRAM = ()
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "o_boomerang_vendored"
STANDING_NEW_TABLET = True
STANDING_OA_HTML = True
STANDING_OB_HTML = False
STANDING_OR_HTML = False
STANDING_OV_HTML = False
STANDING_O_HTML = False
STANDING_BA_OA_HTML = False
UNPUBLISHED_O_PAGES = ("Ob.html", "Or.html", "Ov.html", "O.html")


def load_vendored_oa_html() -> str:
    """Return the vendored Kohaumotu Oa.html snapshot."""
    return OA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_o_index_html() -> str:
    """Return the vendored Kohaumotu O/index.html snapshot."""
    return O_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_oa_barthel_json() -> dict:
    """Return the vendored parsed Oa Barthel JSON."""
    return json.loads(OA_JSON_PATH.read_text(encoding="utf-8"))


def load_o_sides() -> dict[str, list[list[str]]]:
    """Oa stems from the vendored parser. No R scrape."""
    return {
        SIDE_OA: side_line_stems(
            extract_published_tokens(load_vendored_oa_html(), SIDE_OA),
            OA_LINE_NAMES,
        ),
    }


def island_hits_by_o_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each O side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in O_SIDES
    }


def unpublished_o_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished O Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_O_PAGES if any(fixtures.glob(f"**/{name}")))


def score_o_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on Oa. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_OA],
        analyzer,
        line_names=OA_LINE_NAMES,
    )


class TestBoomerangVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_fischer_line_names_and_skips_image_cells(self):
        """name=Line_N is Fischer's number; Oa3 not Oa1. Digit <td> only."""
        html = (
            '<h3><a name="Line_3">Line 1 (Fischer\'s Line 3)</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>000!-007?-005.037?-000!-</td></tr></table>"
            '<h3><a name="Line_4">Line 2 (Fischer\'s Line 4)</a></h3>'
            "<table><tr><td>??</td></tr></table>"
            "<table><tr><td>006:700-000!*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_OA)
        self.assertEqual(list(published), ["Oa3", "Oa4"])
        self.assertEqual(published["Oa3"], ["000!", "007?", "005.037?", "000!"])
        self.assertEqual(published["Oa4"], ["006:700", "000!*"])
        stems = side_line_stems(published, ("Oa3", "Oa4"))
        self.assertEqual(stems[0], ["000", "007", "005", "037", "000"])
        self.assertEqual(stems[1], ["006", "700", "000"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {SIDE_OA: [list(gram)]}
        hits = island_hits_by_o_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_OA][0], 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_o_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariBoomerangVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → O → Oa lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.o_index = load_vendored_o_index_html()
        self.by_side = load_o_sides()
        self.gk_hits = island_hits_by_o_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_o_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in O_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in O_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in O_SIDES
        }
        self.m_n4_hits = {
            side: ngram_hit_count(self.by_side[side], M_N4_GRAM) for side in O_SIDES
        }
        self.n_n6_hits = {
            side: ngram_hit_count(self.by_side[side], N_N6_GRAM) for side in O_SIDES
        }
        self.profile = score_o_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_o(self):
        """Catalog → tablets → O index. Oa.html is 200; index lists ba_Oa.html."""
        self.assertTrue(OA_HTML_PATH.is_file())
        self.assertTrue(OA_JSON_PATH.is_file())
        self.assertTrue((OA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(O_INDEX_HTML_PATH.is_file())
        self.assertFalse((OA_HTML_DIR / "Ob.html").exists())
        self.assertFalse((OA_HTML_DIR / "Or.html").exists())
        self.assertFalse((OA_HTML_DIR / "Ov.html").exists())
        self.assertFalse((OA_HTML_DIR / "O.html").exists())
        self.assertFalse((OA_HTML_DIR / "ba_Oa.html").exists())
        self.assertEqual(STANDING_OA_HTML, True)
        self.assertEqual(STANDING_OB_HTML, False)
        self.assertEqual(STANDING_OR_HTML, False)
        self.assertEqual(STANDING_OV_HTML, False)
        self.assertEqual(STANDING_O_HTML, False)
        self.assertEqual(STANDING_BA_OA_HTML, False)
        self.assertEqual(OA_HTML_PATH.stat().st_size, STANDING_OA_BYTES)
        self.assertEqual(O_INDEX_HTML_PATH.stat().st_size, STANDING_O_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "O"), STANDING_TABLET_O)
        self.assertEqual(published_all_lines_hrefs(self.o_index), STANDING_O_ALL_LINES)
        self.assertEqual(published_all_lines_hrefs(self.o_index), ())
        self.assertIn("Item O:Berlin Tablet (Boomerang)", self.o_index)
        self.assertIn("Only one side legible", self.o_index)
        self.assertIn(f'href="{STANDING_INDEX_BARTHEL_HREF}"', self.o_index)
        self.assertNotIn('href="Oa.html"', self.o_index)
        self.assertNotIn('href="Ob.html"', self.o_index)
        self.assertNotIn('href="Or.html"', self.o_index)
        self.assertNotIn('href="Ov.html"', self.o_index)
        self.assertNotIn('href="O.html"', self.o_index)
        oa = load_vendored_oa_html()
        self.assertIn("The Berlin Tablet (the \"Boomerang\")", oa)
        self.assertIn("Rongorongo Oa", oa)
        self.assertIn('<h3><a name="Line_3">Line 1 (Fischer\'s Line 3)</a></h3>', oa)
        self.assertIn('<h3><a name="Line_9">Line 7 (Fischer\'s Line 9)</a></h3>', oa)
        self.assertNotIn('<h3><a name="Line_1">', oa)
        self.assertNotIn('<h3><a name="Line_2">', oa)
        self.assertIn("000!-007?-013?-755-005.037?-000!-", oa)
        self.assertIn("600-400-004.064-006:700-204?.108a-004.064-736-000!*", oa)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_o_html_names(fixtures), ())
        text = (OA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        for url in (
            CITED_CATALOG_URL,
            CITED_TABLETS_URL,
            CITED_O_INDEX_URL,
            CITED_OA_URL,
        ):
            self.assertIn(url, text)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
        self.assertIn("tablet R", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        oa_json = load_oa_barthel_json()
        oa_pub = extract_published_tokens(load_vendored_oa_html(), SIDE_OA)
        self.assertEqual(oa_json["tablet"], "O")
        self.assertEqual(oa_json["side"], SIDE_OA)
        self.assertEqual(oa_json["name"], "Boomerang")
        self.assertEqual(oa_json["source"]["url"], CITED_OA_URL)
        self.assertEqual(tuple(oa_json["lines"]), OA_LINE_NAMES)
        self.assertEqual(tuple(oa_json["stems"]), OA_LINE_NAMES)
        for index, name in enumerate(OA_LINE_NAMES):
            self.assertEqual(oa_json["lines"][name], oa_pub[name])
            self.assertEqual(oa_json["stems"][name], self.by_side[SIDE_OA][index])
        self.assertEqual(oa_json["lines"]["Oa3"][0], "000!")
        self.assertEqual(oa_json["stems"]["Oa3"][0], "000")
        self.assertEqual(oa_json["lines"]["Oa3"][4], "005.037?")
        self.assertEqual(oa_json["stems"]["Oa3"][4:6], ["005", "037"])
        self.assertEqual(len(oa_json["lines"]["Oa3"]), 10)
        self.assertEqual(len(oa_json["stems"]["Oa3"]), 12)
        self.assertEqual(oa_json["lines"]["Oa6"][14], "004.064")
        self.assertEqual(oa_json["stems"]["Oa6"][14:16], ["004", "064"])
        self.assertEqual(oa_json["lines"]["Oa6"][15], "006:700")
        self.assertEqual(oa_json["stems"]["Oa6"][16:18], ["006", "700"])
        self.assertNotIn("Oa1", oa_json["lines"])
        self.assertNotIn("Oa2", oa_json["lines"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E, Er7, M n=4, N n=6 are 0."""
        for side in O_SIDES:
            counts = [len(line) for line in self.by_side[side]]
            self.assertEqual(counts, list(STANDING_STEM_COUNTS[side]))
            self.assertEqual(sum(counts), STANDING_STEM_TOTALS[side])
            self.assertEqual(self.gk_hits[side], STANDING_GK_ISLAND_HITS[side])
            self.assertEqual(self.hpq_hits[side], STANDING_HPQ_ISLAND_HITS[side])
            self.assertEqual(self.e_n9_hits[side], STANDING_E_N9_HITS[side])
            self.assertEqual(self.er7_4_hits[side], STANDING_ER7_4_HITS[side])
            self.assertEqual(self.er7_8_hits[side], STANDING_ER7_8_HITS[side])
            self.assertEqual(self.m_n4_hits[side], STANDING_M_N4_HITS[side])
            self.assertEqual(self.n_n6_hits[side], STANDING_N_N6_HITS[side])
            for gram, count in zip(GK_LOCKED_GRAMS, self.gk_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            for gram, count in zip(HPQ_LOCKED_ISLANDS, self.hpq_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], E_GRAM_N9), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], ER7_GRAM4), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], ER7_GRAM8), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], M_N4_GRAM), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], N_N6_GRAM), 0)
        self.assertFalse(any(any(hits) for hits in self.gk_hits.values()))
        self.assertFalse(any(any(hits) for hits in self.hpq_hits.values()))
        self.assertFalse(any(self.e_n9_hits.values()))
        self.assertFalse(any(self.er7_4_hits.values()))
        self.assertFalse(any(self.er7_8_hits.values()))
        self.assertFalse(any(self.m_n4_hits.values()))
        self.assertFalse(any(self.n_n6_hits.values()))
        self.assertEqual(STANDING_ANY_GK_ISLAND, False)
        self.assertEqual(STANDING_ANY_HPQ_ISLAND, False)
        self.assertEqual(STANDING_ANY_E_N9, False)
        self.assertEqual(STANDING_ANY_ER7_DOUBLE, False)
        self.assertEqual(STANDING_ANY_M_N4, False)
        self.assertEqual(STANDING_ANY_N_N6, False)
        self.assertEqual(STANDING_ANY_KNOWN_ISLAND, False)
        self.assertEqual(STANDING_CLAIM, "known_islands_absent")
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(N_N6_GRAM, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_repeating_ngram_has_no_4gram(self):
        """O's own repeating profile: longest n=0; no n≥4 freq≥2. Not the claim."""
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest_n, 0)
        self.assertEqual(self.profile.rows, ())
        self.assertEqual(self.profile.longest, ())
        self.assertFalse(any(row.n >= 8 for row in self.profile.rows))
        self.assertFalse(STANDING_EIGHTGRAM_EXISTS)
        self.assertEqual(len(self.profile.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.profile.eightgrams, ())
        self.assertIsNone(self.profile.top_8gram)
        self.assertEqual(STANDING_LONGEST_NGRAM, ())
        self.assertNotEqual(STANDING_CLAIM, "no_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_n_vienna_scoreboard_still_computes(self):
        """Cycle 89 N vendor lock and cycle 91 Na1 N-only lock stay."""
        prior = TestMamariSmallViennaVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_8gram()
        prior.test_survey_matches_computed_lock()
        prior_n_only = TestMamariSmallViennaNa1NOnlyScoreboard()
        prior_n_only.setUp()
        prior_n_only.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-92 O vendor lock."""
        lock = self.survey["tablet_o_boomerang_vendor"]
        self.assertEqual(lock["cycle"], 92)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_o"], "O")
        self.assertEqual(lock["name_o"], "Boomerang")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["o_index"], CITED_O_INDEX_URL)
        self.assertEqual(lock["oa_page"], CITED_OA_URL)
        self.assertEqual(tuple(lock["o_pages"]), STANDING_O_ALL_LINES)
        self.assertEqual(lock["index_barthel_href"], STANDING_INDEX_BARTHEL_HREF)
        self.assertEqual(lock["html_bytes"]["Oa"], STANDING_OA_BYTES)
        self.assertEqual(lock["stem_totals"]["Oa"], STANDING_STEM_TOTALS[SIDE_OA])
        self.assertEqual(tuple(lock["stem_counts"]["Oa"]), STANDING_OA_STEM_COUNTS)
        self.assertEqual(tuple(lock["lines"]["Oa"]), OA_LINE_NAMES)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Oa"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Oa"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Oa"], 0)
        self.assertEqual(lock["m_n4_hits"]["Oa"], 0)
        self.assertEqual(lock["n_n6_hits"]["Oa"], 0)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertEqual(tuple(lock["n_n6_tokens"]), N_N6_GRAM)
        self.assertFalse(lock["any_gk_island"])
        self.assertFalse(lock["any_hpq_island"])
        self.assertFalse(lock["any_e_n9"])
        self.assertFalse(lock["any_er7_double"])
        self.assertFalse(lock["any_m_n4"])
        self.assertFalse(lock["any_n_n6"])
        self.assertFalse(lock["any_known_island"])
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertFalse(lock["eightgram_exists"])
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["new_tablet"])
        self.assertTrue(lock["oa_html"])
        self.assertFalse(lock["ob_html"])
        self.assertFalse(lock["or_html"])
        self.assertFalse(lock["ov_html"])
        self.assertFalse(lock["o_html"])
        self.assertFalse(lock["ba_oa_html"])
        self.assertTrue(lock["standing_n_vienna_na1_n_only_unchanged"])
        self.assertTrue(lock["standing_n_vienna_vendor_unchanged"])
        self.assertTrue(lock["standing_m_vienna_ma2_m_only_unchanged"])
        self.assertTrue(lock["standing_m_vienna_vendor_unchanged"])
        self.assertTrue(lock["standing_l_reimiro_vendor_unchanged"])
        self.assertTrue(lock["standing_j_reimiro_vendor_unchanged"])
        self.assertTrue(lock["standing_f_chauvet_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertTrue(lock["standing_d_echancree_vendor_unchanged"])
        self.assertTrue(lock["standing_q_vendor_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_maximals_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_n_vienna_na1_n_only"]["cycle"], 91)
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["cycle"], 89)
        self.assertEqual(tuple(self.survey["tablet_n_vienna_vendor"]["longest_tokens"]), N_N6_GRAM)
        self.assertEqual(self.survey["tablet_m_vienna_vendor"]["cycle"], 88)
        self.assertEqual(self.survey["tablet_m_vienna_ma2_m_only"]["cycle"], 90)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariBoomerangVendorImageSnapshot(unittest.TestCase):
    """Cycle 92 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
