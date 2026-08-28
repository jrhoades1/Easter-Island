"""Small Vienna (N) vendor lock.

Cycle 89 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / L /
M / P / Q. HEAD-check before filename assume (cycle 54 Gr vs Ga;
cycle 79 Da vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs Fa; cycle 86
Jb vs Ja; cycle 87 Lb vs La; cycle 88 Mb vs Ma): Nr.html / Nv.html /
N.html are unpublished 404s. N/index.html names Na.html / Nb.html
(a/b, like A/C/D/F). Catalog name is Small Vienna — not Great
Vienna / London / Reimiro. Digits are copied from the snapshots.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. No second new letter.

Locks the vendored sides: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; exact hits of M's n=4
006 022 006 022; N's own longest repeating n-gram (n and whether
n≥8 exists). M's locked facts stay. Claim that can lose: known
tradition islands, E islands, and M's n=4 are exact-0 on N
(closed-tradition hold-out). N has a repeating 6-gram (no n≥8),
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
from tests.test_mamari_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
    TestMamariViennaVendorScoreboard,
)

NA_HTML_DIR = Path(__file__).parent / "fixtures" / "vienna_na_html"
NB_HTML_DIR = Path(__file__).parent / "fixtures" / "vienna_nb_html"
NA_HTML_PATH = NA_HTML_DIR / "Na.html"
NB_HTML_PATH = NB_HTML_DIR / "Nb.html"
N_INDEX_HTML_PATH = NA_HTML_DIR / "N_index.html"
NA_JSON_PATH = NA_HTML_DIR / "Na_barthel.json"
NB_JSON_PATH = NB_HTML_DIR / "Nb_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_N_INDEX_URL = "http://kohaumotu.org/Rongorongo/N/index.html"
CITED_NA_URL = "http://kohaumotu.org/Rongorongo/N/Na.html"
CITED_NB_URL = "http://kohaumotu.org/Rongorongo/N/Nb.html"

SIDE_NA = "Na"
SIDE_NB = "Nb"
N_SIDES = (SIDE_NA, SIDE_NB)

NA_LINE_NAMES = tuple(f"Na{n}" for n in range(1, 6))
NB_LINE_NAMES = tuple(f"Nb{n}" for n in range(1, 6))
N_LINE_NAMES = {
    SIDE_NA: NA_LINE_NAMES,
    SIDE_NB: NB_LINE_NAMES,
}

STANDING_NA_BYTES = 2649
STANDING_NB_BYTES = 2474
STANDING_N_INDEX_BYTES = 3818
STANDING_NA_STEM_COUNTS = (32, 29, 30, 38, 22)
STANDING_NB_STEM_COUNTS = (23, 20, 27, 18, 18)
STANDING_STEM_TOTALS = {
    SIDE_NA: 151,
    SIDE_NB: 106,
}
STANDING_STEM_COUNTS = {
    SIDE_NA: STANDING_NA_STEM_COUNTS,
    SIDE_NB: STANDING_NB_STEM_COUNTS,
}
STANDING_N_ALL_LINES = ("Na.html", "Nb.html")
STANDING_TABLET_N = ("N", "N/index.html", "Small Vienna")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in N_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in N_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in N_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in N_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in N_SIDES}
STANDING_M_N4_HITS = {side: 0 for side in N_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_M_N4 = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 6
STANDING_LONGEST_NGRAM = ("004", "064", "034", "006", "004", "064")
STANDING_LONGEST_SPANS = (("Na1", 3, 9), ("Na1", 11, 17))
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "n_vienna_vendored"
STANDING_NEW_TABLET = True
STANDING_NA_HTML = True
STANDING_NB_HTML = True
STANDING_NR_HTML = False
STANDING_NV_HTML = False
STANDING_N_HTML = False
UNPUBLISHED_N_PAGES = ("Nr.html", "Nv.html", "N.html")


def load_vendored_na_html() -> str:
    """Return the vendored Kohaumotu Na.html snapshot."""
    return NA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_nb_html() -> str:
    """Return the vendored Kohaumotu Nb.html snapshot."""
    return NB_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_n_index_html() -> str:
    """Return the vendored Kohaumotu N/index.html snapshot."""
    return N_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_na_barthel_json() -> dict:
    """Return the vendored parsed Na Barthel JSON."""
    return json.loads(NA_JSON_PATH.read_text(encoding="utf-8"))


def load_nb_barthel_json() -> dict:
    """Return the vendored parsed Nb Barthel JSON."""
    return json.loads(NB_JSON_PATH.read_text(encoding="utf-8"))


def load_n_sides() -> dict[str, list[list[str]]]:
    """Na / Nb stems from the vendored parser. No O scrape."""
    return {
        SIDE_NA: side_line_stems(
            extract_published_tokens(load_vendored_na_html(), SIDE_NA),
            NA_LINE_NAMES,
        ),
        SIDE_NB: side_line_stems(
            extract_published_tokens(load_vendored_nb_html(), SIDE_NB),
            NB_LINE_NAMES,
        ),
    }


def island_hits_by_n_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each N side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in N_SIDES
    }


def unpublished_n_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished N Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_N_PAGES if any(fixtures.glob(f"**/{name}")))


def score_n_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on combined Na+Nb. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_NA] + by_side[SIDE_NB],
        analyzer,
        line_names=NA_LINE_NAMES + NB_LINE_NAMES,
    )


class TestSmallViennaVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; NaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>000!-034-004.064-034.006-</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>006:700-003-000!*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_NA)
        self.assertEqual(list(published), ["Na1", "Na2"])
        self.assertEqual(published["Na1"], ["000!", "034", "004.064", "034.006"])
        self.assertEqual(published["Na2"], ["006:700", "003", "000!*"])
        stems = side_line_stems(published, ("Na1", "Na2"))
        self.assertEqual(stems[0], ["000", "034", "004", "064", "034", "006"])
        self.assertEqual(stems[1], ["006", "700", "003", "000"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {side: [[]] for side in N_SIDES}
        by_side[SIDE_NA] = [list(gram)]
        hits = island_hits_by_n_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_NA][0], 1)
        self.assertEqual(hits[SIDE_NB], (0,) * len(GK_LOCKED_GRAMS))
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_n_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallViennaVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → N → Na/Nb lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.n_index = load_vendored_n_index_html()
        self.by_side = load_n_sides()
        self.gk_hits = island_hits_by_n_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_n_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in N_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in N_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in N_SIDES
        }
        self.m_n4_hits = {
            side: ngram_hit_count(self.by_side[side], M_N4_GRAM) for side in N_SIDES
        }
        self.profile = score_n_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_n(self):
        """Catalog → tablets → N index → Na/Nb. Not Nr, Nv, or N.html."""
        self.assertTrue(NA_HTML_PATH.is_file())
        self.assertTrue(NB_HTML_PATH.is_file())
        self.assertTrue(NA_JSON_PATH.is_file())
        self.assertTrue(NB_JSON_PATH.is_file())
        self.assertTrue((NA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((NB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(N_INDEX_HTML_PATH.is_file())
        self.assertFalse((NA_HTML_DIR / "Nr.html").exists())
        self.assertFalse((NA_HTML_DIR / "Nv.html").exists())
        self.assertFalse((NA_HTML_DIR / "N.html").exists())
        self.assertFalse((NB_HTML_DIR / "Nr.html").exists())
        self.assertEqual(STANDING_NA_HTML, True)
        self.assertEqual(STANDING_NB_HTML, True)
        self.assertEqual(STANDING_NR_HTML, False)
        self.assertEqual(STANDING_NV_HTML, False)
        self.assertEqual(STANDING_N_HTML, False)
        self.assertEqual(NA_HTML_PATH.stat().st_size, STANDING_NA_BYTES)
        self.assertEqual(NB_HTML_PATH.stat().st_size, STANDING_NB_BYTES)
        self.assertEqual(N_INDEX_HTML_PATH.stat().st_size, STANDING_N_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "N"), STANDING_TABLET_N)
        self.assertEqual(published_all_lines_hrefs(self.n_index), STANDING_N_ALL_LINES)
        self.assertIn("Item N:The Small Vienna tablet", self.n_index)
        self.assertIn('href="Na.html"', self.n_index)
        self.assertIn('href="Nb.html"', self.n_index)
        self.assertNotIn('href="Nr.html"', self.n_index)
        self.assertNotIn('href="Nv.html"', self.n_index)
        self.assertNotIn('href="N.html"', self.n_index)
        na = load_vendored_na_html()
        nb = load_vendored_nb_html()
        self.assertIn("The Small Vienna Tablet", na)
        self.assertIn("The Small Vienna Tablet", nb)
        self.assertIn("Rongorongo Na", na)
        self.assertIn("Rongorongo Nb", nb)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', na)
        self.assertIn('<h3><a name="Line_5">Line 5</a></h3>', na)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', nb)
        self.assertIn('<h3><a name="Line_5">Line 5</a></h3>', nb)
        self.assertIn("000!-034-200-004.064-034.006", na)
        self.assertIn("000!-125-600-125-600-125", nb)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_n_html_names(fixtures), ())
        for directory, urls in (
            (
                NA_HTML_DIR,
                (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_N_INDEX_URL, CITED_NA_URL),
            ),
            (NB_HTML_DIR, (CITED_NB_URL, CITED_N_INDEX_URL)),
        ):
            text = (directory / "ATTRIBUTION").read_text(encoding="utf-8")
            for url in urls:
                self.assertIn(url, text)
            self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
            self.assertIn("tablet O", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        na_json = load_na_barthel_json()
        nb_json = load_nb_barthel_json()
        na_pub = extract_published_tokens(load_vendored_na_html(), SIDE_NA)
        nb_pub = extract_published_tokens(load_vendored_nb_html(), SIDE_NB)
        self.assertEqual(na_json["tablet"], "N")
        self.assertEqual(nb_json["tablet"], "N")
        self.assertEqual(na_json["side"], SIDE_NA)
        self.assertEqual(nb_json["side"], SIDE_NB)
        self.assertEqual(na_json["name"], "Small Vienna")
        self.assertEqual(nb_json["name"], "Small Vienna")
        self.assertEqual(na_json["source"]["url"], CITED_NA_URL)
        self.assertEqual(nb_json["source"]["url"], CITED_NB_URL)
        for name in NA_LINE_NAMES:
            self.assertEqual(na_json["lines"][name], na_pub[name])
            self.assertEqual(
                na_json["stems"][name],
                self.by_side[SIDE_NA][int(name[2:]) - 1],
            )
        for name in NB_LINE_NAMES:
            self.assertEqual(nb_json["lines"][name], nb_pub[name])
            self.assertEqual(
                nb_json["stems"][name],
                self.by_side[SIDE_NB][int(name[2:]) - 1],
            )
        self.assertEqual(na_json["lines"]["Na1"][0], "000!")
        self.assertEqual(na_json["stems"]["Na1"][0], "000")
        self.assertEqual(na_json["lines"]["Na1"][3], "004.064")
        self.assertEqual(na_json["stems"]["Na1"][3:5], ["004", "064"])
        self.assertEqual(len(na_json["lines"]["Na1"]), 21)
        self.assertEqual(len(na_json["stems"]["Na1"]), 32)
        self.assertEqual(nb_json["lines"]["Nb3"][3], "006:700")
        self.assertEqual(nb_json["stems"]["Nb3"][4:6], ["006", "700"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E, Er7, M n=4 are 0 on N."""
        for side in N_SIDES:
            counts = [len(line) for line in self.by_side[side]]
            self.assertEqual(counts, list(STANDING_STEM_COUNTS[side]))
            self.assertEqual(sum(counts), STANDING_STEM_TOTALS[side])
            self.assertEqual(self.gk_hits[side], STANDING_GK_ISLAND_HITS[side])
            self.assertEqual(self.hpq_hits[side], STANDING_HPQ_ISLAND_HITS[side])
            self.assertEqual(self.e_n9_hits[side], STANDING_E_N9_HITS[side])
            self.assertEqual(self.er7_4_hits[side], STANDING_ER7_4_HITS[side])
            self.assertEqual(self.er7_8_hits[side], STANDING_ER7_8_HITS[side])
            self.assertEqual(self.m_n4_hits[side], STANDING_M_N4_HITS[side])
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
        self.assertFalse(any(any(hits) for hits in self.gk_hits.values()))
        self.assertFalse(any(any(hits) for hits in self.hpq_hits.values()))
        self.assertFalse(any(self.e_n9_hits.values()))
        self.assertFalse(any(self.er7_4_hits.values()))
        self.assertFalse(any(self.er7_8_hits.values()))
        self.assertFalse(any(self.m_n4_hits.values()))
        self.assertEqual(STANDING_ANY_GK_ISLAND, False)
        self.assertEqual(STANDING_ANY_HPQ_ISLAND, False)
        self.assertEqual(STANDING_ANY_E_N9, False)
        self.assertEqual(STANDING_ANY_ER7_DOUBLE, False)
        self.assertEqual(STANDING_ANY_M_N4, False)
        self.assertEqual(STANDING_ANY_KNOWN_ISLAND, False)
        self.assertEqual(STANDING_CLAIM, "known_islands_absent")
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_repeating_ngram_has_no_8gram(self):
        """N's own repeating profile: longest n=6; no n≥8. Not the claim."""
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest_n, 6)
        self.assertEqual(len(self.profile.longest), 1)
        self.assertEqual(self.profile.longest[0].tokens, STANDING_LONGEST_NGRAM)
        self.assertEqual(self.profile.longest[0].freq, 2)
        self.assertEqual(self.profile.longest[0].spans, STANDING_LONGEST_SPANS)
        self.assertFalse(any(row.n >= 8 for row in self.profile.rows))
        self.assertFalse(STANDING_EIGHTGRAM_EXISTS)
        self.assertEqual(len(self.profile.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.profile.eightgrams, ())
        self.assertIsNone(self.profile.top_8gram)
        self.assertNotEqual(STANDING_CLAIM, "no_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_m_vienna_scoreboard_still_computes(self):
        """Cycle 88 M vendor lock stays."""
        prior = TestMamariViennaVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_8gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-89 N vendor lock."""
        lock = self.survey["tablet_n_vienna_vendor"]
        self.assertEqual(lock["cycle"], 89)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_n"], "N")
        self.assertEqual(lock["name_n"], "Small Vienna")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["n_index"], CITED_N_INDEX_URL)
        self.assertEqual(lock["na_page"], CITED_NA_URL)
        self.assertEqual(lock["nb_page"], CITED_NB_URL)
        self.assertEqual(tuple(lock["n_pages"]), STANDING_N_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Na"], STANDING_NA_BYTES)
        self.assertEqual(lock["html_bytes"]["Nb"], STANDING_NB_BYTES)
        self.assertEqual(lock["stem_totals"]["Na"], STANDING_STEM_TOTALS[SIDE_NA])
        self.assertEqual(lock["stem_totals"]["Nb"], STANDING_STEM_TOTALS[SIDE_NB])
        self.assertEqual(tuple(lock["stem_counts"]["Na"]), STANDING_NA_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Nb"]), STANDING_NB_STEM_COUNTS)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Na"], 0)
        self.assertEqual(lock["e_n9_hits"]["Nb"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Na"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Nb"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Na"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Nb"], 0)
        self.assertEqual(lock["m_n4_hits"]["Na"], 0)
        self.assertEqual(lock["m_n4_hits"]["Nb"], 0)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertFalse(lock["any_gk_island"])
        self.assertFalse(lock["any_hpq_island"])
        self.assertFalse(lock["any_e_n9"])
        self.assertFalse(lock["any_er7_double"])
        self.assertFalse(lock["any_m_n4"])
        self.assertFalse(lock["any_known_island"])
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertFalse(lock["eightgram_exists"])
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["new_tablet"])
        self.assertTrue(lock["na_html"])
        self.assertTrue(lock["nb_html"])
        self.assertFalse(lock["nr_html"])
        self.assertFalse(lock["nv_html"])
        self.assertFalse(lock["n_html"])
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
        self.assertEqual(self.survey["tablet_m_vienna_vendor"]["cycle"], 88)
        self.assertEqual(self.survey["tablet_l_reimiro_vendor"]["cycle"], 87)
        self.assertEqual(self.survey["tablet_j_reimiro_vendor"]["cycle"], 86)
        self.assertEqual(self.survey["tablet_f_chauvet_vendor"]["cycle"], 85)
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["cycle"], 80)
        self.assertEqual(self.survey["tablet_e_keiti_er7_double"]["cycle"], 84)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallViennaVendorImageSnapshot(unittest.TestCase):
    """Cycle 89 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
