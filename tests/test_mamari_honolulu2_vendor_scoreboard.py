"""Honolulu 2 (U) vendor lock.

Cycle 97 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / L /
M / N / O / P / Q / R / S / T. HEAD-check before filename assume (cycle
54 Gr vs Ga; cycle 79 Da vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs
Fa; cycle 86 Jb vs Ja; cycle 87 Lb vs La; cycle 88 Mb vs Ma; cycle
89 Nr vs Na; cycle 92 Ob vs Oa; cycle 93 Rr vs Ra; cycle 94 Sr vs
Sa; cycle 96 Tb vs Ta): Ub.html / Ur.html / Uv.html / U.html are
unpublished 404s. U/index.html names Ua.html (Barthel) only. Catalog
name is Honolulu 2 [#3623] — not Honolulu 1 / Washington / Vienna /
London / Reimiro / Boomerang / Atua-Mata-Riri. Digits are copied
from the snapshots. No invented Barthel. No G00n→Barthel map. No
type merge. No detector retune. No CV. No new agents. No second
new letter.

Locks the vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; exact hits of M's n=4
006 022 006 022; exact hits of N's n=6 004 064 034 006 004 064;
exact hits of S's n=7 004 660 081 004 660 081 004; U's own
longest repeating n-gram (n and whether n≥8 exists). T's locked
facts stay. Claim that can lose: known tradition islands,
E islands, M's n=4, N's n=6, and S's n=7 are exact-0 on U
(closed-tradition hold-out). U has no repeating n≥4, so the
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
from tests.test_mamari_honolulu_vendor_scoreboard import (
    TestMamariHonoluluVendorScoreboard,
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

UA_HTML_DIR = Path(__file__).parent / "fixtures" / "honolulu_ua_html"
UA_HTML_PATH = UA_HTML_DIR / "Ua.html"
U_INDEX_HTML_PATH = UA_HTML_DIR / "U_index.html"
UA_JSON_PATH = UA_HTML_DIR / "Ua_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_U_INDEX_URL = "http://kohaumotu.org/Rongorongo/U/index.html"
CITED_UA_URL = "http://kohaumotu.org/Rongorongo/U/Ua.html"

SIDE_UA = "Ua"
U_SIDES = (SIDE_UA,)

UA_LINE_NAMES = tuple(f"Ua{n}" for n in range(1, 5))
U_LINE_NAMES = {SIDE_UA: UA_LINE_NAMES}

STANDING_UA_BYTES = 1677
STANDING_U_INDEX_BYTES = 2919
STANDING_UA_STEM_COUNTS = (0, 12, 19, 0)
STANDING_STEM_TOTALS = {SIDE_UA: 31}
STANDING_STEM_COUNTS = {SIDE_UA: STANDING_UA_STEM_COUNTS}
STANDING_U_ALL_LINES = ("Ua.html",)
STANDING_TABLET_U = ("U", "U/index.html", "Honolulu 2 [#3623]")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in U_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in U_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in U_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in U_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in U_SIDES}
STANDING_M_N4_HITS = {side: 0 for side in U_SIDES}
STANDING_N_N6_HITS = {side: 0 for side in U_SIDES}
STANDING_S_N7_HITS = {side: 0 for side in U_SIDES}
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
STANDING_RESULT = "u_honolulu_vendored"
STANDING_NEW_TABLET = True
STANDING_UA_HTML = True
STANDING_UB_HTML = False
STANDING_UR_HTML = False
STANDING_UV_HTML = False
STANDING_U_HTML = False
UNPUBLISHED_U_PAGES = ("Ub.html", "Ur.html", "Uv.html", "U.html")


def load_vendored_ua_html() -> str:
    """Return the vendored Kohaumotu Ua.html snapshot."""
    return UA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_u_index_html() -> str:
    """Return the vendored Kohaumotu U/index.html snapshot."""
    return U_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_ua_barthel_json() -> dict:
    """Return the vendored parsed Ua Barthel JSON."""
    return json.loads(UA_JSON_PATH.read_text(encoding="utf-8"))


def load_u_sides() -> dict[str, list[list[str]]]:
    """Ua stems from the vendored parser. No V scrape."""
    return {
        SIDE_UA: side_line_stems(
            extract_published_tokens(load_vendored_ua_html(), SIDE_UA),
            UA_LINE_NAMES,
        ),
    }


def island_hits_by_u_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each U side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in U_SIDES
    }


def unpublished_u_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished U Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_U_PAGES if any(fixtures.glob(f"**/{name}")))


def score_u_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on Ua. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_UA],
        analyzer,
        line_names=UA_LINE_NAMES,
    )


class TestHonolulu2VendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; UaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>(8-16)!*</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>000!-030b-073.006-000!*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_UA)
        self.assertEqual(list(published), ["Ua1", "Ua2"])
        self.assertEqual(published["Ua1"], ["(8", "16)!*"])
        self.assertEqual(published["Ua2"], ["000!", "030b", "073.006", "000!*"])
        stems = side_line_stems(published, ("Ua1", "Ua2"))
        self.assertEqual(stems[0], [])
        self.assertEqual(stems[1], ["000", "030", "073", "006", "000"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {SIDE_UA: [list(gram)]}
        hits = island_hits_by_u_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_UA][0], 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_u_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHonolulu2VendorScoreboard(unittest.TestCase):
    """Cited tablets.html → U → Ua lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.u_index = load_vendored_u_index_html()
        self.by_side = load_u_sides()
        self.gk_hits = island_hits_by_u_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_u_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in U_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in U_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in U_SIDES
        }
        self.m_n4_hits = {
            side: ngram_hit_count(self.by_side[side], M_N4_GRAM) for side in U_SIDES
        }
        self.n_n6_hits = {
            side: ngram_hit_count(self.by_side[side], N_N6_GRAM) for side in U_SIDES
        }
        self.s_n7_hits = {
            side: ngram_hit_count(self.by_side[side], S_N7_GRAM) for side in U_SIDES
        }
        self.profile = score_u_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_u(self):
        """Catalog → tablets → U index → Ua. Not Ub, Ur, Uv, or U.html."""
        self.assertTrue(UA_HTML_PATH.is_file())
        self.assertTrue(UA_JSON_PATH.is_file())
        self.assertTrue((UA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(U_INDEX_HTML_PATH.is_file())
        self.assertFalse((UA_HTML_DIR / "Ub.html").exists())
        self.assertFalse((UA_HTML_DIR / "Ur.html").exists())
        self.assertFalse((UA_HTML_DIR / "Uv.html").exists())
        self.assertFalse((UA_HTML_DIR / "U.html").exists())
        self.assertEqual(STANDING_UA_HTML, True)
        self.assertEqual(STANDING_UB_HTML, False)
        self.assertEqual(STANDING_UR_HTML, False)
        self.assertEqual(STANDING_UV_HTML, False)
        self.assertEqual(STANDING_U_HTML, False)
        self.assertEqual(UA_HTML_PATH.stat().st_size, STANDING_UA_BYTES)
        self.assertEqual(U_INDEX_HTML_PATH.stat().st_size, STANDING_U_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "U"), STANDING_TABLET_U)
        self.assertEqual(published_all_lines_hrefs(self.u_index), STANDING_U_ALL_LINES)
        self.assertIn("Item U:Honolulu 2 [#3623]", self.u_index)
        self.assertIn('href="Ua.html"', self.u_index)
        self.assertNotIn('href="Ub.html"', self.u_index)
        self.assertNotIn('href="Ur.html"', self.u_index)
        self.assertNotIn('href="Uv.html"', self.u_index)
        self.assertNotIn('href="U.html"', self.u_index)
        ua = load_vendored_ua_html()
        self.assertIn("Item U:Honolulu 2 [#3623]", ua)
        self.assertIn("Rongorongo: Tablet U", ua)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', ua)
        self.assertIn('<h3><a name="Line_4">Line 4</a></h3>', ua)
        self.assertIn("one side only", ua)
        self.assertIn("(8-16)!", ua)
        self.assertIn("(10-20)!", ua)
        self.assertIn("000!-030b-073.006-044?-040-000!-000!-", ua)
        self.assertIn("000!-065.006.003?-000!.003-002-007-047-004-002-595-", ua)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_u_html_names(fixtures), ())
        text = (UA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        for url in (
            CITED_CATALOG_URL,
            CITED_TABLETS_URL,
            CITED_U_INDEX_URL,
            CITED_UA_URL,
        ):
            self.assertIn(url, text)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
        self.assertIn("tablet V", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        ua_json = load_ua_barthel_json()
        ua_pub = extract_published_tokens(load_vendored_ua_html(), SIDE_UA)
        self.assertEqual(ua_json["tablet"], "U")
        self.assertEqual(ua_json["side"], SIDE_UA)
        self.assertEqual(ua_json["name"], "Honolulu 2 [#3623]")
        self.assertEqual(ua_json["source"]["url"], CITED_UA_URL)
        self.assertEqual(tuple(ua_json["lines"]), UA_LINE_NAMES)
        self.assertEqual(tuple(ua_json["stems"]), UA_LINE_NAMES)
        for index, name in enumerate(UA_LINE_NAMES):
            self.assertEqual(ua_json["lines"][name], ua_pub[name])
            self.assertEqual(ua_json["stems"][name], self.by_side[SIDE_UA][index])
        self.assertEqual(ua_json["lines"]["Ua1"], ["(8", "16)!*"])
        self.assertEqual(ua_json["stems"]["Ua1"], [])
        self.assertEqual(ua_json["lines"]["Ua4"], ["(10", "20)!*"])
        self.assertEqual(ua_json["stems"]["Ua4"], [])
        self.assertEqual(ua_json["lines"]["Ua2"][0], "000!")
        self.assertEqual(ua_json["stems"]["Ua2"][0], "000")
        self.assertEqual(ua_json["lines"]["Ua2"][2], "073.006")
        self.assertEqual(ua_json["stems"]["Ua2"][2:4], ["073", "006"])
        self.assertEqual(len(ua_json["lines"]["Ua2"]), 11)
        self.assertEqual(len(ua_json["stems"]["Ua2"]), 12)
        self.assertEqual(ua_json["lines"]["Ua2"][7], "600V")
        self.assertEqual(ua_json["stems"]["Ua2"][8], "600")
        self.assertEqual(ua_json["lines"]["Ua3"][1], "065.006.003?")
        self.assertEqual(ua_json["stems"]["Ua3"][1:4], ["065", "006", "003"])
        self.assertEqual(ua_json["lines"]["Ua3"][11], "042?:008")
        self.assertEqual(ua_json["stems"]["Ua3"][15:17], ["042", "008"])
        self.assertEqual(len(ua_json["lines"]["Ua3"]), 14)
        self.assertEqual(len(ua_json["stems"]["Ua3"]), 19)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E, Er7, M, N, S are 0."""
        for side in U_SIDES:
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
        """U's own repeating profile: longest n=0; no n≥4 freq≥2. Not the claim."""
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

    def test_existing_t_honolulu_scoreboard_still_computes(self):
        """Cycle 96 T vendor lock stays."""
        prior = TestMamariHonoluluVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_4gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-97 U vendor lock."""
        lock = self.survey["tablet_u_honolulu_vendor"]
        self.assertEqual(lock["cycle"], 97)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_u"], "U")
        self.assertEqual(lock["name_u"], "Honolulu 2 [#3623]")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["u_index"], CITED_U_INDEX_URL)
        self.assertEqual(lock["ua_page"], CITED_UA_URL)
        self.assertEqual(tuple(lock["u_pages"]), STANDING_U_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Ua"], STANDING_UA_BYTES)
        self.assertEqual(lock["stem_totals"]["Ua"], STANDING_STEM_TOTALS[SIDE_UA])
        self.assertEqual(tuple(lock["stem_counts"]["Ua"]), STANDING_UA_STEM_COUNTS)
        self.assertEqual(tuple(lock["lines"]["Ua"]), UA_LINE_NAMES)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Ua"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Ua"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Ua"], 0)
        self.assertEqual(lock["m_n4_hits"]["Ua"], 0)
        self.assertEqual(lock["n_n6_hits"]["Ua"], 0)
        self.assertEqual(lock["s_n7_hits"]["Ua"], 0)
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
        self.assertTrue(lock["ua_html"])
        self.assertFalse(lock["ub_html"])
        self.assertFalse(lock["ur_html"])
        self.assertFalse(lock["uv_html"])
        self.assertFalse(lock["u_html"])
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
        self.assertEqual(self.survey["tablet_t_honolulu_vendor"]["cycle"], 96)
        self.assertEqual(self.survey["tablet_s_washington_sb2_s_only"]["cycle"], 95)
        self.assertEqual(self.survey["tablet_s_washington_vendor"]["cycle"], 94)
        self.assertEqual(
            tuple(self.survey["tablet_s_washington_vendor"]["longest_tokens"]),
            S_N7_GRAM,
        )
        self.assertTrue(self.survey["tablet_s_washington_sb2_s_only"]["s_only"])
        self.assertEqual(self.survey["tablet_r_atua_vendor"]["cycle"], 93)
        self.assertEqual(self.survey["tablet_o_boomerang_vendor"]["cycle"], 92)
        self.assertEqual(self.survey["tablet_t_honolulu_vendor"]["result"], "t_honolulu_vendored")
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHonolulu2VendorImageSnapshot(unittest.TestCase):
    """Cycle 97 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
