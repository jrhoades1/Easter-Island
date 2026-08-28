"""Honolulu 1 (T) vendor lock.

Cycle 96 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / L /
M / N / O / P / Q / R / S. HEAD-check before filename assume (cycle
54 Gr vs Ga; cycle 79 Da vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs
Fa; cycle 86 Jb vs Ja; cycle 87 Lb vs La; cycle 88 Mb vs Ma; cycle
89 Nr vs Na; cycle 92 Ob vs Oa; cycle 93 Rr vs Ra; cycle 94 Sr vs
Sa): Tb.html / Tr.html / Tv.html / T.html are unpublished 404s.
T/index.html names Ta.html (Barthel) only. Catalog name is
Honolulu 1 [#3629] — not Washington / Vienna / London / Reimiro /
Boomerang / Atua-Mata-Riri. Digits are copied from the snapshots.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. No second new letter.

Locks the vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; exact hits of M's n=4
006 022 006 022; exact hits of N's n=6 004 064 034 006 004 064;
exact hits of S's n=7 004 660 081 004 660 081 004; T's own
longest repeating n-gram (n and whether n≥8 exists). S's locked
facts stay. Claim that can lose: known tradition islands,
E islands, M's n=4, N's n=6, and S's n=7 are exact-0 on T
(closed-tradition hold-out). T has no repeating n≥4, so the
hold-out is the lock that can leak.

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
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html
from tests.test_mamari_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
)
from tests.test_mamari_washington_sb2_s_only_scoreboard import (
    TestMamariWashingtonSb2SOnlyScoreboard,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as S_N7_GRAM,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    TestMamariWashingtonVendorScoreboard,
)

TA_HTML_DIR = Path(__file__).parent / "fixtures" / "honolulu_ta_html"
TA_HTML_PATH = TA_HTML_DIR / "Ta.html"
T_INDEX_HTML_PATH = TA_HTML_DIR / "T_index.html"
TA_JSON_PATH = TA_HTML_DIR / "Ta_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_T_INDEX_URL = "http://kohaumotu.org/Rongorongo/T/index.html"
CITED_TA_URL = "http://kohaumotu.org/Rongorongo/T/Ta.html"

SIDE_TA = "Ta"
T_SIDES = (SIDE_TA,)

TA_LINE_NAMES = tuple(f"Ta{n}" for n in range(1, 12))
T_LINE_NAMES = {SIDE_TA: TA_LINE_NAMES}

STANDING_TA_BYTES = 4370
STANDING_T_INDEX_BYTES = 3471
STANDING_TA_STEM_COUNTS = (0, 24, 24, 30, 21, 22, 9, 17, 14, 11, 0)
STANDING_STEM_TOTALS = {SIDE_TA: 172}
STANDING_STEM_COUNTS = {SIDE_TA: STANDING_TA_STEM_COUNTS}
STANDING_T_ALL_LINES = ("Ta.html",)
STANDING_TABLET_T = ("T", "T/index.html", "Honolulu 1 [#3629]")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in T_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in T_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in T_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in T_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in T_SIDES}
STANDING_M_N4_HITS = {side: 0 for side in T_SIDES}
STANDING_N_N6_HITS = {side: 0 for side in T_SIDES}
STANDING_S_N7_HITS = {side: 0 for side in T_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_M_N4 = False
STANDING_ANY_N_N6 = False
STANDING_ANY_S_N7 = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 0
STANDING_LONGEST_NGRAM = ()
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "t_honolulu_vendored"
STANDING_NEW_TABLET = True
STANDING_TA_HTML = True
STANDING_TB_HTML = False
STANDING_TR_HTML = False
STANDING_TV_HTML = False
STANDING_T_HTML = False
UNPUBLISHED_T_PAGES = ("Tb.html", "Tr.html", "Tv.html", "T.html")


def load_vendored_ta_html() -> str:
    """Return the vendored Kohaumotu Ta.html snapshot."""
    return TA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_t_index_html() -> str:
    """Return the vendored Kohaumotu T/index.html snapshot."""
    return T_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_ta_barthel_json() -> dict:
    """Return the vendored parsed Ta Barthel JSON."""
    return json.loads(TA_JSON_PATH.read_text(encoding="utf-8"))


def load_t_sides() -> dict[str, list[list[str]]]:
    """Ta stems from the vendored parser. No U scrape."""
    return {
        SIDE_TA: side_line_stems(
            extract_published_tokens(load_vendored_ta_html(), SIDE_TA),
            TA_LINE_NAMES,
        ),
    }


def island_hits_by_t_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each T side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in T_SIDES
    }


def unpublished_t_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished T Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_T_PAGES if any(fixtures.glob(f"**/{name}")))


def score_t_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on Ta. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_TA],
        analyzer,
        line_names=TA_LINE_NAMES,
    )


class TestHonoluluVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; TaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>(10-20)!</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>000!-004.076-000!*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_TA)
        self.assertEqual(list(published), ["Ta1", "Ta2"])
        self.assertEqual(published["Ta1"], ["(10", "20)!"])
        self.assertEqual(published["Ta2"], ["000!", "004.076", "000!*"])
        stems = side_line_stems(published, ("Ta1", "Ta2"))
        self.assertEqual(stems[0], [])
        self.assertEqual(stems[1], ["000", "004", "076", "000"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {SIDE_TA: [list(gram)]}
        hits = island_hits_by_t_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_TA][0], 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_t_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHonoluluVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → T → Ta lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.t_index = load_vendored_t_index_html()
        self.by_side = load_t_sides()
        self.gk_hits = island_hits_by_t_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_t_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in T_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in T_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in T_SIDES
        }
        self.m_n4_hits = {
            side: ngram_hit_count(self.by_side[side], M_N4_GRAM) for side in T_SIDES
        }
        self.n_n6_hits = {
            side: ngram_hit_count(self.by_side[side], N_N6_GRAM) for side in T_SIDES
        }
        self.s_n7_hits = {
            side: ngram_hit_count(self.by_side[side], S_N7_GRAM) for side in T_SIDES
        }
        self.profile = score_t_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_t(self):
        """Catalog → tablets → T index → Ta. Not Tb, Tr, Tv, or T.html."""
        self.assertTrue(TA_HTML_PATH.is_file())
        self.assertTrue(TA_JSON_PATH.is_file())
        self.assertTrue((TA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(T_INDEX_HTML_PATH.is_file())
        self.assertFalse((TA_HTML_DIR / "Tb.html").exists())
        self.assertFalse((TA_HTML_DIR / "Tr.html").exists())
        self.assertFalse((TA_HTML_DIR / "Tv.html").exists())
        self.assertFalse((TA_HTML_DIR / "T.html").exists())
        self.assertEqual(STANDING_TA_HTML, True)
        self.assertEqual(STANDING_TB_HTML, False)
        self.assertEqual(STANDING_TR_HTML, False)
        self.assertEqual(STANDING_TV_HTML, False)
        self.assertEqual(STANDING_T_HTML, False)
        self.assertEqual(TA_HTML_PATH.stat().st_size, STANDING_TA_BYTES)
        self.assertEqual(T_INDEX_HTML_PATH.stat().st_size, STANDING_T_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "T"), STANDING_TABLET_T)
        self.assertEqual(published_all_lines_hrefs(self.t_index), STANDING_T_ALL_LINES)
        self.assertIn("Item T:Honolulu 1 [#3629]", self.t_index)
        self.assertIn('href="Ta.html"', self.t_index)
        self.assertNotIn('href="Tb.html"', self.t_index)
        self.assertNotIn('href="Tr.html"', self.t_index)
        self.assertNotIn('href="Tv.html"', self.t_index)
        self.assertNotIn('href="T.html"', self.t_index)
        ta = load_vendored_ta_html()
        self.assertIn("Item T:Honolulu 1 [#3629]", ta)
        self.assertIn("Rongorongo Ta", ta)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', ta)
        self.assertIn('<h3><a name="Line_11">Line 11</a></h3>', ta)
        self.assertIn("one side only", ta)
        self.assertIn("(10-20)!", ta)
        self.assertIn("(8-16)!", ta)
        self.assertIn("000!-000!-382?-480-004.076-073f?-006.074-048.076-070-053-322.076-000!-011-", ta)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_t_html_names(fixtures), ())
        text = (TA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        for url in (
            CITED_CATALOG_URL,
            CITED_TABLETS_URL,
            CITED_T_INDEX_URL,
            CITED_TA_URL,
        ):
            self.assertIn(url, text)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
        self.assertIn("tablet U", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        ta_json = load_ta_barthel_json()
        ta_pub = extract_published_tokens(load_vendored_ta_html(), SIDE_TA)
        self.assertEqual(ta_json["tablet"], "T")
        self.assertEqual(ta_json["side"], SIDE_TA)
        self.assertEqual(ta_json["name"], "Honolulu 1 [#3629]")
        self.assertEqual(ta_json["source"]["url"], CITED_TA_URL)
        self.assertEqual(tuple(ta_json["lines"]), TA_LINE_NAMES)
        self.assertEqual(tuple(ta_json["stems"]), TA_LINE_NAMES)
        for index, name in enumerate(TA_LINE_NAMES):
            self.assertEqual(ta_json["lines"][name], ta_pub[name])
            self.assertEqual(ta_json["stems"][name], self.by_side[SIDE_TA][index])
        self.assertEqual(ta_json["lines"]["Ta1"], ["(10", "20)!"])
        self.assertEqual(ta_json["stems"]["Ta1"], [])
        self.assertEqual(ta_json["lines"]["Ta11"], ["(8", "16)!"])
        self.assertEqual(ta_json["stems"]["Ta11"], [])
        self.assertEqual(ta_json["lines"]["Ta2"][0], "000!")
        self.assertEqual(ta_json["stems"]["Ta2"][0], "000")
        self.assertEqual(ta_json["lines"]["Ta2"][4], "004.076")
        self.assertEqual(ta_json["stems"]["Ta2"][4:6], ["004", "076"])
        self.assertEqual(len(ta_json["lines"]["Ta2"]), 18)
        self.assertEqual(len(ta_json["stems"]["Ta2"]), 24)
        self.assertEqual(ta_json["lines"]["Ta6"][1], "600V.076")
        self.assertEqual(ta_json["stems"]["Ta6"][1:3], ["600", "076"])
        self.assertEqual(ta_json["lines"]["Ta10"][3:6], ["006", "600", "011.076"])
        self.assertEqual(ta_json["stems"]["Ta10"][3:7], ["006", "600", "011", "076"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E, Er7, M, N, S are 0."""
        for side in T_SIDES:
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

    def test_longest_repeating_ngram_has_no_4gram(self):
        """T's own repeating profile: longest n=0; no n≥4 freq≥2. Not the claim."""
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

    def test_existing_s_washington_scoreboard_still_computes(self):
        """Cycle 94 S vendor lock and cycle 95 Sb2 S-only lock stay."""
        prior = TestMamariWashingtonVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_is_7()
        prior.test_survey_matches_computed_lock()
        prior_s_only = TestMamariWashingtonSb2SOnlyScoreboard()
        prior_s_only.setUp()
        prior_s_only.test_7gram_is_zero_off_s_and_s_only()
        prior_s_only.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-96 T vendor lock."""
        lock = self.survey["tablet_t_honolulu_vendor"]
        self.assertEqual(lock["cycle"], 96)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_t"], "T")
        self.assertEqual(lock["name_t"], "Honolulu 1 [#3629]")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["t_index"], CITED_T_INDEX_URL)
        self.assertEqual(lock["ta_page"], CITED_TA_URL)
        self.assertEqual(tuple(lock["t_pages"]), STANDING_T_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Ta"], STANDING_TA_BYTES)
        self.assertEqual(lock["stem_totals"]["Ta"], STANDING_STEM_TOTALS[SIDE_TA])
        self.assertEqual(tuple(lock["stem_counts"]["Ta"]), STANDING_TA_STEM_COUNTS)
        self.assertEqual(tuple(lock["lines"]["Ta"]), TA_LINE_NAMES)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Ta"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Ta"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Ta"], 0)
        self.assertEqual(lock["m_n4_hits"]["Ta"], 0)
        self.assertEqual(lock["n_n6_hits"]["Ta"], 0)
        self.assertEqual(lock["s_n7_hits"]["Ta"], 0)
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
        self.assertTrue(lock["ta_html"])
        self.assertFalse(lock["tb_html"])
        self.assertFalse(lock["tr_html"])
        self.assertFalse(lock["tv_html"])
        self.assertFalse(lock["t_html"])
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
        self.assertEqual(self.survey["tablet_s_washington_sb2_s_only"]["cycle"], 95)
        self.assertEqual(self.survey["tablet_s_washington_vendor"]["cycle"], 94)
        self.assertEqual(
            tuple(self.survey["tablet_s_washington_vendor"]["longest_tokens"]),
            S_N7_GRAM,
        )
        self.assertTrue(self.survey["tablet_s_washington_sb2_s_only"]["s_only"])
        self.assertEqual(self.survey["tablet_r_atua_vendor"]["cycle"], 93)
        self.assertEqual(self.survey["tablet_o_boomerang_vendor"]["cycle"], 92)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHonoluluVendorImageSnapshot(unittest.TestCase):
    """Cycle 96 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
