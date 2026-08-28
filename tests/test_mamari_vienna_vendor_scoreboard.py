"""Great Vienna (M) vendor lock.

Cycle 88 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / L /
P / Q. HEAD-check before filename assume (cycle 54 Gr vs Ga; cycle 79
Da vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs Fa; cycle 86 Jb vs Ja;
cycle 87 Lb vs La): Mb.html / Mr.html / Mv.html / M.html are
unpublished 404s. M/index.html names Ma.html (Lines) only. Catalog
name is Great Vienna — not London / Reimiro. Digits are copied from
the snapshots. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. No second new
letter.

Locks the vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; M's own longest repeating n-gram
(n and whether n≥8 exists). L's locked facts stay. Claim that
can lose: known tradition islands and E islands are exact-0 on M
(closed-tradition hold-out). M has a repeating 4-gram (no n≥8),
so the hold-out is the lock that can leak.

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
from tests.test_mamari_reimiro2_vendor_scoreboard import (
    TestMamariReimiro2VendorScoreboard,
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
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html

MA_HTML_DIR = Path(__file__).parent / "fixtures" / "vienna_ma_html"
MA_HTML_PATH = MA_HTML_DIR / "Ma.html"
M_INDEX_HTML_PATH = MA_HTML_DIR / "M_index.html"
MA_JSON_PATH = MA_HTML_DIR / "Ma_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_M_INDEX_URL = "http://kohaumotu.org/Rongorongo/M/index.html"
CITED_MA_URL = "http://kohaumotu.org/Rongorongo/M/Ma.html"

SIDE_MA = "Ma"
M_SIDES = (SIDE_MA,)

MA_LINE_NAMES = tuple(f"Ma{n}" for n in range(1, 10))
M_LINE_NAMES = {SIDE_MA: MA_LINE_NAMES}

STANDING_MA_BYTES = 3495
STANDING_M_INDEX_BYTES = 3353
STANDING_MA_STEM_COUNTS = (0, 23, 15, 13, 6, 4, 0, 0, 4)
STANDING_STEM_TOTALS = {SIDE_MA: 65}
STANDING_STEM_COUNTS = {SIDE_MA: STANDING_MA_STEM_COUNTS}
STANDING_M_ALL_LINES = ("Ma.html",)
STANDING_TABLET_M = ("M", "M/index.html", "Great Vienna")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in M_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in M_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in M_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in M_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in M_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 4
STANDING_LONGEST_NGRAM = ("006", "022", "006", "022")
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "m_vienna_vendored"
STANDING_NEW_TABLET = True
STANDING_MA_HTML = True
STANDING_MB_HTML = False
STANDING_MR_HTML = False
STANDING_MV_HTML = False
STANDING_M_HTML = False
UNPUBLISHED_M_PAGES = ("Mb.html", "Mr.html", "Mv.html", "M.html")


def load_vendored_ma_html() -> str:
    """Return the vendored Kohaumotu Ma.html snapshot."""
    return MA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_m_index_html() -> str:
    """Return the vendored Kohaumotu M/index.html snapshot."""
    return M_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_ma_barthel_json() -> dict:
    """Return the vendored parsed Ma Barthel JSON."""
    return json.loads(MA_JSON_PATH.read_text(encoding="utf-8"))


def load_m_sides() -> dict[str, list[list[str]]]:
    """Ma stems from the vendored parser. No N scrape."""
    return {
        SIDE_MA: side_line_stems(
            extract_published_tokens(load_vendored_ma_html(), SIDE_MA),
            MA_LINE_NAMES,
        ),
    }


def island_hits_by_m_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each M side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in M_SIDES
    }


def unpublished_m_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished M Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_M_PAGES if any(fixtures.glob(f"**/{name}")))


def score_m_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on Ma. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_MA],
        analyzer,
        line_names=MA_LINE_NAMES,
    )


class TestViennaVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; MaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>(10-20)!</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>000!-006-022?</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_MA)
        self.assertEqual(list(published), ["Ma1", "Ma2"])
        self.assertEqual(published["Ma1"], ["(10", "20)!"])
        self.assertEqual(published["Ma2"], ["000!", "006", "022?"])
        stems = side_line_stems(published, ("Ma1", "Ma2"))
        self.assertEqual(stems[0], [])
        self.assertEqual(stems[1], ["000", "006", "022"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {SIDE_MA: [list(gram)]}
        hits = island_hits_by_m_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_MA][0], 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_m_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariViennaVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → M → Ma lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.m_index = load_vendored_m_index_html()
        self.by_side = load_m_sides()
        self.gk_hits = island_hits_by_m_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_m_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in M_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in M_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in M_SIDES
        }
        self.profile = score_m_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_m(self):
        """Catalog → tablets → M index → Ma. Not Mb, Mr, Mv, or M.html."""
        self.assertTrue(MA_HTML_PATH.is_file())
        self.assertTrue(MA_JSON_PATH.is_file())
        self.assertTrue((MA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(M_INDEX_HTML_PATH.is_file())
        self.assertFalse((MA_HTML_DIR / "Mb.html").exists())
        self.assertFalse((MA_HTML_DIR / "Mr.html").exists())
        self.assertFalse((MA_HTML_DIR / "Mv.html").exists())
        self.assertFalse((MA_HTML_DIR / "M.html").exists())
        self.assertEqual(STANDING_MA_HTML, True)
        self.assertEqual(STANDING_MB_HTML, False)
        self.assertEqual(STANDING_MR_HTML, False)
        self.assertEqual(STANDING_MV_HTML, False)
        self.assertEqual(STANDING_M_HTML, False)
        self.assertEqual(MA_HTML_PATH.stat().st_size, STANDING_MA_BYTES)
        self.assertEqual(M_INDEX_HTML_PATH.stat().st_size, STANDING_M_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "M"), STANDING_TABLET_M)
        self.assertEqual(published_all_lines_hrefs(self.m_index), STANDING_M_ALL_LINES)
        self.assertIn("Item M:Great Vienna", self.m_index)
        self.assertIn("Only one side legible.", self.m_index)
        self.assertIn('href="Ma.html"', self.m_index)
        self.assertNotIn('href="Mb.html"', self.m_index)
        self.assertNotIn('href="Mr.html"', self.m_index)
        self.assertNotIn('href="Mv.html"', self.m_index)
        self.assertNotIn('href="M.html"', self.m_index)
        ma = load_vendored_ma_html()
        self.assertIn("The Great Vienna Tablet", ma)
        self.assertIn("Rongorongo Ma", ma)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', ma)
        self.assertIn('<h3><a name="Line_9">Line 9</a></h3>', ma)
        self.assertIn("(10-20)!", ma)
        self.assertIn("(3-8)!", ma)
        self.assertIn("000!-670?-026?-006-691", ma)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_m_html_names(fixtures), ())
        text = (MA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        for url in (
            CITED_CATALOG_URL,
            CITED_TABLETS_URL,
            CITED_M_INDEX_URL,
            CITED_MA_URL,
        ):
            self.assertIn(url, text)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
        self.assertIn("tablet N", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        ma_json = load_ma_barthel_json()
        ma_pub = extract_published_tokens(load_vendored_ma_html(), SIDE_MA)
        self.assertEqual(ma_json["tablet"], "M")
        self.assertEqual(ma_json["side"], SIDE_MA)
        self.assertEqual(ma_json["name"], "Great Vienna")
        self.assertEqual(ma_json["source"]["url"], CITED_MA_URL)
        for name in MA_LINE_NAMES:
            self.assertEqual(ma_json["lines"][name], ma_pub[name])
            self.assertEqual(
                ma_json["stems"][name],
                self.by_side[SIDE_MA][int(name[2:]) - 1],
            )
        self.assertEqual(ma_json["lines"]["Ma1"], ["(10", "20)!"])
        self.assertEqual(ma_json["stems"]["Ma1"], [])
        self.assertEqual(ma_json["lines"]["Ma7"], ["(3", "8)!"])
        self.assertEqual(ma_json["stems"]["Ma7"], [])
        self.assertEqual(ma_json["lines"]["Ma8"], ["(3", "8)!"])
        self.assertEqual(ma_json["stems"]["Ma8"], [])
        self.assertEqual(len(ma_json["lines"]["Ma2"]), 21)
        self.assertEqual(len(ma_json["stems"]["Ma2"]), 23)
        self.assertEqual(ma_json["lines"]["Ma2"][0], "000!")
        self.assertEqual(ma_json["stems"]["Ma2"][0], "000")
        self.assertEqual(ma_json["lines"]["Ma2"][-1], "000!*")
        self.assertEqual(ma_json["stems"]["Ma2"][-1], "000")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E n=9, Er7 4-gram are 0 on M."""
        for side in M_SIDES:
            counts = [len(line) for line in self.by_side[side]]
            self.assertEqual(counts, list(STANDING_STEM_COUNTS[side]))
            self.assertEqual(sum(counts), STANDING_STEM_TOTALS[side])
            self.assertEqual(self.gk_hits[side], STANDING_GK_ISLAND_HITS[side])
            self.assertEqual(self.hpq_hits[side], STANDING_HPQ_ISLAND_HITS[side])
            self.assertEqual(self.e_n9_hits[side], STANDING_E_N9_HITS[side])
            self.assertEqual(self.er7_4_hits[side], STANDING_ER7_4_HITS[side])
            self.assertEqual(self.er7_8_hits[side], STANDING_ER7_8_HITS[side])
            for gram, count in zip(GK_LOCKED_GRAMS, self.gk_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            for gram, count in zip(HPQ_LOCKED_ISLANDS, self.hpq_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], E_GRAM_N9), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], ER7_GRAM4), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], ER7_GRAM8), 0)
        self.assertFalse(any(any(hits) for hits in self.gk_hits.values()))
        self.assertFalse(any(any(hits) for hits in self.hpq_hits.values()))
        self.assertFalse(any(self.e_n9_hits.values()))
        self.assertFalse(any(self.er7_4_hits.values()))
        self.assertFalse(any(self.er7_8_hits.values()))
        self.assertEqual(STANDING_ANY_GK_ISLAND, False)
        self.assertEqual(STANDING_ANY_HPQ_ISLAND, False)
        self.assertEqual(STANDING_ANY_E_N9, False)
        self.assertEqual(STANDING_ANY_ER7_DOUBLE, False)
        self.assertEqual(STANDING_ANY_KNOWN_ISLAND, False)
        self.assertEqual(STANDING_CLAIM, "known_islands_absent")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_repeating_ngram_has_no_8gram(self):
        """M's own repeating profile: longest n=4; no n≥8. Not the claim."""
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest_n, 4)
        self.assertEqual(len(self.profile.longest), 1)
        self.assertEqual(self.profile.longest[0].tokens, STANDING_LONGEST_NGRAM)
        self.assertEqual(self.profile.longest[0].freq, 2)
        self.assertEqual(self.profile.longest[0].spans, (("Ma2", 5, 9), ("Ma2", 7, 11)))
        self.assertFalse(any(row.n >= 8 for row in self.profile.rows))
        self.assertFalse(STANDING_EIGHTGRAM_EXISTS)
        self.assertEqual(len(self.profile.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.profile.eightgrams, ())
        self.assertIsNone(self.profile.top_8gram)
        self.assertNotEqual(STANDING_CLAIM, "no_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_l_reimiro_scoreboard_still_computes(self):
        """Cycle 87 L vendor lock stays."""
        prior = TestMamariReimiro2VendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_4gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-88 M vendor lock."""
        lock = self.survey["tablet_m_vienna_vendor"]
        self.assertEqual(lock["cycle"], 88)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_m"], "M")
        self.assertEqual(lock["name_m"], "Great Vienna")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["m_index"], CITED_M_INDEX_URL)
        self.assertEqual(lock["ma_page"], CITED_MA_URL)
        self.assertEqual(tuple(lock["m_pages"]), STANDING_M_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Ma"], STANDING_MA_BYTES)
        self.assertEqual(lock["stem_totals"]["Ma"], STANDING_STEM_TOTALS[SIDE_MA])
        self.assertEqual(tuple(lock["stem_counts"]["Ma"]), STANDING_MA_STEM_COUNTS)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Ma"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Ma"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Ma"], 0)
        self.assertFalse(lock["any_gk_island"])
        self.assertFalse(lock["any_hpq_island"])
        self.assertFalse(lock["any_e_n9"])
        self.assertFalse(lock["any_er7_double"])
        self.assertFalse(lock["any_known_island"])
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertFalse(lock["eightgram_exists"])
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["new_tablet"])
        self.assertTrue(lock["ma_html"])
        self.assertFalse(lock["mb_html"])
        self.assertFalse(lock["mr_html"])
        self.assertFalse(lock["mv_html"])
        self.assertFalse(lock["m_html"])
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
        self.assertEqual(self.survey["tablet_l_reimiro_vendor"]["cycle"], 87)
        self.assertEqual(self.survey["tablet_j_reimiro_vendor"]["cycle"], 86)
        self.assertEqual(self.survey["tablet_f_chauvet_vendor"]["cycle"], 85)
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["cycle"], 80)
        self.assertEqual(self.survey["tablet_e_keiti_er7_double"]["cycle"], 84)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariViennaVendorImageSnapshot(unittest.TestCase):
    """Cycle 88 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
