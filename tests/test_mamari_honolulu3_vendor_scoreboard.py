"""Honolulu 3 (V) vendor lock.

Cycle 98 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / L /
M / N / O / P / Q / R / S / T / U. HEAD-check before filename assume
(cycle 54 Gr vs Ga; cycle 79 Da vs Dr; cycle 80 Er vs Ea; cycle 85
Fr vs Fa; cycle 86 Jb vs Ja; cycle 87 Lb vs La; cycle 88 Mb vs Ma;
cycle 89 Nr vs Na; cycle 92 Ob vs Oa; cycle 93 Rr vs Ra; cycle 94
Sr vs Sa; cycle 96 Tb vs Ta; cycle 97 Ub vs Ua): Vb.html / Vr.html /
Vv.html / V.html are unpublished 404s. V/index.html names Va.html
(Barthel) only. Catalog name is Honolulu 3 [#3622] — not Honolulu 1
/ Honolulu 2 / Washington / Vienna / London / Reimiro / Boomerang /
Atua-Mata-Riri. Digits are copied from the snapshots. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune. No
CV. No new agents. No second new letter.

Locks the vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; exact hits of M's n=4
006 022 006 022; exact hits of N's n=6 004 064 034 006 004 064;
exact hits of S's n=7 004 660 081 004 660 081 004; V's own
longest repeating n-gram (n and whether n≥8 exists). U's locked
facts stay. Claim that can lose: known tradition islands,
E islands, M's n=4, N's n=6, and S's n=7 are exact-0 on V
(closed-tradition hold-out). V's longest repeating n-gram is
n=4 048 010 048 010 (not the claim).

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
from tests.test_mamari_honolulu2_vendor_scoreboard import (
    TestMamariHonolulu2VendorScoreboard,
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
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html
from tests.test_mamari_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as S_N7_GRAM,
)

VA_HTML_DIR = Path(__file__).parent / "fixtures" / "honolulu_va_html"
VA_HTML_PATH = VA_HTML_DIR / "Va.html"
V_INDEX_HTML_PATH = VA_HTML_DIR / "V_index.html"
VA_JSON_PATH = VA_HTML_DIR / "Va_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_V_INDEX_URL = "http://kohaumotu.org/Rongorongo/V/index.html"
CITED_VA_URL = "http://kohaumotu.org/Rongorongo/V/Va.html"

SIDE_VA = "Va"
V_SIDES = (SIDE_VA,)

VA_LINE_NAMES = tuple(f"Va{n}" for n in range(1, 3))
V_LINE_NAMES = {SIDE_VA: VA_LINE_NAMES}

STANDING_VA_BYTES = 1273
STANDING_V_INDEX_BYTES = 3047
STANDING_VA_STEM_COUNTS = (26, 0)
STANDING_STEM_TOTALS = {SIDE_VA: 26}
STANDING_STEM_COUNTS = {SIDE_VA: STANDING_VA_STEM_COUNTS}
STANDING_V_ALL_LINES = ("Va.html",)
STANDING_TABLET_V = ("V", "V/index.html", "Honolulu 3 [#3622]")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in V_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in V_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in V_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in V_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in V_SIDES}
STANDING_M_N4_HITS = {side: 0 for side in V_SIDES}
STANDING_N_N6_HITS = {side: 0 for side in V_SIDES}
STANDING_S_N7_HITS = {side: 0 for side in V_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_M_N4 = False
STANDING_ANY_N_N6 = False
STANDING_ANY_S_N7 = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 4
STANDING_LONGEST_NGRAM = ("048", "010", "048", "010")
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "v_honolulu_vendored"
STANDING_NEW_TABLET = True
STANDING_VA_HTML = True
STANDING_VB_HTML = False
STANDING_VR_HTML = False
STANDING_VV_HTML = False
STANDING_V_HTML = False
UNPUBLISHED_V_PAGES = ("Vb.html", "Vr.html", "Vv.html", "V.html")


def load_vendored_va_html() -> str:
    """Return the vendored Kohaumotu Va.html snapshot."""
    return VA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_v_index_html() -> str:
    """Return the vendored Kohaumotu V/index.html snapshot."""
    return V_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_va_barthel_json() -> dict:
    """Return the vendored parsed Va Barthel JSON."""
    return json.loads(VA_JSON_PATH.read_text(encoding="utf-8"))


def load_v_sides() -> dict[str, list[list[str]]]:
    """Va stems from the vendored parser. No W scrape."""
    return {
        SIDE_VA: side_line_stems(
            extract_published_tokens(load_vendored_va_html(), SIDE_VA),
            VA_LINE_NAMES,
        ),
    }


def island_hits_by_v_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each V side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in V_SIDES
    }


def unpublished_v_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished V Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_V_PAGES if any(fixtures.glob(f"**/{name}")))


def score_v_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on Va. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_VA],
        analyzer,
        line_names=VA_LINE_NAMES,
    )


class TestHonolulu3VendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; VaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>051-200.200.011-048.010*</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_VA)
        self.assertEqual(list(published), ["Va1", "Va2"])
        self.assertEqual(published["Va1"], ["051", "200.200.011", "048.010*"])
        self.assertEqual(published["Va2"], [])
        stems = side_line_stems(published, ("Va1", "Va2"))
        self.assertEqual(stems[0], ["051", "200", "200", "011", "048", "010"])
        self.assertEqual(stems[1], [])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {SIDE_VA: [list(gram)]}
        hits = island_hits_by_v_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_VA][0], 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_v_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHonolulu3VendorScoreboard(unittest.TestCase):
    """Cited tablets.html → V → Va lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.v_index = load_vendored_v_index_html()
        self.by_side = load_v_sides()
        self.gk_hits = island_hits_by_v_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_v_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in V_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in V_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in V_SIDES
        }
        self.m_n4_hits = {
            side: ngram_hit_count(self.by_side[side], M_N4_GRAM) for side in V_SIDES
        }
        self.n_n6_hits = {
            side: ngram_hit_count(self.by_side[side], N_N6_GRAM) for side in V_SIDES
        }
        self.s_n7_hits = {
            side: ngram_hit_count(self.by_side[side], S_N7_GRAM) for side in V_SIDES
        }
        self.profile = score_v_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_v(self):
        """Catalog → tablets → V index → Va. Not Vb, Vr, Vv, or V.html."""
        self.assertTrue(VA_HTML_PATH.is_file())
        self.assertTrue(VA_JSON_PATH.is_file())
        self.assertTrue((VA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(V_INDEX_HTML_PATH.is_file())
        self.assertFalse((VA_HTML_DIR / "Vb.html").exists())
        self.assertFalse((VA_HTML_DIR / "Vr.html").exists())
        self.assertFalse((VA_HTML_DIR / "Vv.html").exists())
        self.assertFalse((VA_HTML_DIR / "V.html").exists())
        self.assertEqual(STANDING_VA_HTML, True)
        self.assertEqual(STANDING_VB_HTML, False)
        self.assertEqual(STANDING_VR_HTML, False)
        self.assertEqual(STANDING_VV_HTML, False)
        self.assertEqual(STANDING_V_HTML, False)
        self.assertEqual(VA_HTML_PATH.stat().st_size, STANDING_VA_BYTES)
        self.assertEqual(V_INDEX_HTML_PATH.stat().st_size, STANDING_V_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "V"), STANDING_TABLET_V)
        self.assertEqual(published_all_lines_hrefs(self.v_index), STANDING_V_ALL_LINES)
        self.assertIn("Item V:Honolulu 3 [#3622]", self.v_index)
        self.assertIn('href="Va.html"', self.v_index)
        self.assertNotIn('href="Vb.html"', self.v_index)
        self.assertNotIn('href="Vr.html"', self.v_index)
        self.assertNotIn('href="Vv.html"', self.v_index)
        self.assertNotIn('href="V.html"', self.v_index)
        va = load_vendored_va_html()
        self.assertIn("Item V:Honolulu 3 [#3622]", va)
        self.assertIn("Rongorongo: Tablet V", va)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', va)
        self.assertIn('<h3><a name="Line_2">Line 2</a></h3>', va)
        self.assertIn("one side only", va)
        self.assertIn("051-200.200.011-002-048.010-048.010-048.010-102-700-700-", va)
        self.assertIn("145-591?-591?-200?-748?-057-057-", va)
        self.assertIn("057?-070-061.061-450?*", va)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_v_html_names(fixtures), ())
        text = (VA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        for url in (
            CITED_CATALOG_URL,
            CITED_TABLETS_URL,
            CITED_V_INDEX_URL,
            CITED_VA_URL,
        ):
            self.assertIn(url, text)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
        self.assertIn("tablet W", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        va_json = load_va_barthel_json()
        va_pub = extract_published_tokens(load_vendored_va_html(), SIDE_VA)
        self.assertEqual(va_json["tablet"], "V")
        self.assertEqual(va_json["side"], SIDE_VA)
        self.assertEqual(va_json["name"], "Honolulu 3 [#3622]")
        self.assertEqual(va_json["source"]["url"], CITED_VA_URL)
        self.assertEqual(tuple(va_json["lines"]), VA_LINE_NAMES)
        self.assertEqual(tuple(va_json["stems"]), VA_LINE_NAMES)
        for index, name in enumerate(VA_LINE_NAMES):
            self.assertEqual(va_json["lines"][name], va_pub[name])
            self.assertEqual(va_json["stems"][name], self.by_side[SIDE_VA][index])
        self.assertEqual(va_json["lines"]["Va1"][0], "051")
        self.assertEqual(va_json["stems"]["Va1"][0], "051")
        self.assertEqual(va_json["lines"]["Va1"][1], "200.200.011")
        self.assertEqual(va_json["stems"]["Va1"][1:4], ["200", "200", "011"])
        self.assertEqual(va_json["lines"]["Va1"][3:6], ["048.010", "048.010", "048.010"])
        self.assertEqual(va_json["stems"]["Va1"][5:11], ["048", "010", "048", "010", "048", "010"])
        self.assertEqual(va_json["lines"]["Va1"][-1], "450?*")
        self.assertEqual(va_json["stems"]["Va1"][-1], "450")
        self.assertEqual(len(va_json["lines"]["Va1"]), 20)
        self.assertEqual(len(va_json["stems"]["Va1"]), 26)
        self.assertEqual(va_json["lines"]["Va2"], [])
        self.assertEqual(va_json["stems"]["Va2"], [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E, Er7, M, N, S are 0."""
        for side in V_SIDES:
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
            self.assertEqual(self.s_n7_hits[side], STANDING_S_N7_HITS[side])
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
            self.assertEqual(ngram_hit_count(self.by_side[side], S_N7_GRAM), 0)
        self.assertFalse(any(any(hits) for hits in self.gk_hits.values()))
        self.assertFalse(any(any(hits) for hits in self.hpq_hits.values()))
        self.assertFalse(any(self.e_n9_hits.values()))
        self.assertFalse(any(self.er7_4_hits.values()))
        self.assertFalse(any(self.er7_8_hits.values()))
        self.assertFalse(any(self.m_n4_hits.values()))
        self.assertFalse(any(self.n_n6_hits.values()))
        self.assertFalse(any(self.s_n7_hits.values()))
        self.assertEqual(STANDING_ANY_GK_ISLAND, False)
        self.assertEqual(STANDING_ANY_HPQ_ISLAND, False)
        self.assertEqual(STANDING_ANY_E_N9, False)
        self.assertEqual(STANDING_ANY_ER7_DOUBLE, False)
        self.assertEqual(STANDING_ANY_M_N4, False)
        self.assertEqual(STANDING_ANY_N_N6, False)
        self.assertEqual(STANDING_ANY_S_N7, False)
        self.assertEqual(STANDING_ANY_KNOWN_ISLAND, False)
        self.assertEqual(STANDING_CLAIM, "known_islands_absent")
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(N_N6_GRAM, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(S_N7_GRAM, ("004", "660", "081", "004", "660", "081", "004"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_repeating_ngram_is_4(self):
        """V's own repeating profile: longest n=4; no n≥8. Not the claim."""
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest_n, 4)
        self.assertEqual(len(self.profile.longest), 1)
        self.assertEqual(self.profile.longest[0].tokens, STANDING_LONGEST_NGRAM)
        self.assertEqual(self.profile.longest[0].freq, 2)
        self.assertFalse(any(row.n >= 8 for row in self.profile.rows))
        self.assertFalse(STANDING_EIGHTGRAM_EXISTS)
        self.assertEqual(len(self.profile.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.profile.eightgrams, ())
        self.assertIsNone(self.profile.top_8gram)
        self.assertEqual(STANDING_LONGEST_NGRAM, ("048", "010", "048", "010"))
        self.assertNotEqual(STANDING_CLAIM, "no_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_u_honolulu_scoreboard_still_computes(self):
        """Cycle 97 U vendor lock stays."""
        prior = TestMamariHonolulu2VendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_4gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-98 V vendor lock."""
        lock = self.survey["tablet_v_honolulu_vendor"]
        self.assertEqual(lock["cycle"], 98)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_v"], "V")
        self.assertEqual(lock["name_v"], "Honolulu 3 [#3622]")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["v_index"], CITED_V_INDEX_URL)
        self.assertEqual(lock["va_page"], CITED_VA_URL)
        self.assertEqual(tuple(lock["v_pages"]), STANDING_V_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Va"], STANDING_VA_BYTES)
        self.assertEqual(lock["stem_totals"]["Va"], STANDING_STEM_TOTALS[SIDE_VA])
        self.assertEqual(tuple(lock["stem_counts"]["Va"]), STANDING_VA_STEM_COUNTS)
        self.assertEqual(tuple(lock["lines"]["Va"]), VA_LINE_NAMES)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Va"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Va"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Va"], 0)
        self.assertEqual(lock["m_n4_hits"]["Va"], 0)
        self.assertEqual(lock["n_n6_hits"]["Va"], 0)
        self.assertEqual(lock["s_n7_hits"]["Va"], 0)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertEqual(tuple(lock["n_n6_tokens"]), N_N6_GRAM)
        self.assertEqual(tuple(lock["s_n7_tokens"]), S_N7_GRAM)
        self.assertFalse(lock["any_gk_island"])
        self.assertFalse(lock["any_hpq_island"])
        self.assertFalse(lock["any_e_n9"])
        self.assertFalse(lock["any_er7_double"])
        self.assertFalse(lock["any_m_n4"])
        self.assertFalse(lock["any_n_n6"])
        self.assertFalse(lock["any_s_n7"])
        self.assertFalse(lock["any_known_island"])
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertFalse(lock["eightgram_exists"])
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["new_tablet"])
        self.assertTrue(lock["va_html"])
        self.assertFalse(lock["vb_html"])
        self.assertFalse(lock["vr_html"])
        self.assertFalse(lock["vv_html"])
        self.assertFalse(lock["v_html"])
        self.assertTrue(lock["standing_u_honolulu_vendor_unchanged"])
        self.assertTrue(lock["standing_t_honolulu_vendor_unchanged"])
        self.assertTrue(lock["standing_s_washington_sb2_s_only_unchanged"])
        self.assertTrue(lock["standing_s_washington_vendor_unchanged"])
        self.assertTrue(lock["standing_r_atua_vendor_unchanged"])
        self.assertTrue(lock["standing_o_boomerang_vendor_unchanged"])
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
        self.assertEqual(self.survey["tablet_u_honolulu_vendor"]["cycle"], 97)
        self.assertEqual(self.survey["tablet_t_honolulu_vendor"]["cycle"], 96)
        self.assertEqual(self.survey["tablet_s_washington_sb2_s_only"]["cycle"], 95)
        self.assertEqual(self.survey["tablet_s_washington_vendor"]["cycle"], 94)
        self.assertEqual(
            tuple(self.survey["tablet_s_washington_vendor"]["longest_tokens"]),
            S_N7_GRAM,
        )
        self.assertTrue(self.survey["tablet_s_washington_sb2_s_only"]["s_only"])
        self.assertEqual(self.survey["tablet_u_honolulu_vendor"]["result"], "u_honolulu_vendored")
        self.assertEqual(self.survey["tablet_t_honolulu_vendor"]["result"], "t_honolulu_vendored")
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHonolulu3VendorImageSnapshot(unittest.TestCase):
    """Cycle 98 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
