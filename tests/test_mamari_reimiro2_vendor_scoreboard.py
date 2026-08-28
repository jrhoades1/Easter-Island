"""Reimiro 2 (L) vendor lock.

Cycle 87 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / P / Q.
HEAD-check before filename assume (cycle 54 Gr vs Ga; cycle 79 Da
vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs Fa; cycle 86 Jb vs Ja):
Lb.html / Lr.html / Lv.html are unpublished 404s. L/index.html
names La.html (Lines) and L.html (Item). Catalog name is Reimiro 2
— not London / Vienna. Digits are copied from the snapshots. No
invented Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. No second new letter.

Locks the vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; L's own longest repeating n-gram
(n and whether n≥8 exists). J's locked facts stay. Claim that
can lose: known tradition islands and E islands are exact-0 on L
(closed-tradition hold-out). L is short (longest n=0; no n≥4
freq≥2), so the hold-out is the lock that can leak.

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
from tests.test_mamari_reimiro_vendor_scoreboard import (
    TestMamariReimiroVendorScoreboard,
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

LA_HTML_DIR = Path(__file__).parent / "fixtures" / "reimiro_la_html"
LA_HTML_PATH = LA_HTML_DIR / "La.html"
L_HTML_PATH = LA_HTML_DIR / "L.html"
L_INDEX_HTML_PATH = LA_HTML_DIR / "L_index.html"
LA_JSON_PATH = LA_HTML_DIR / "La_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_L_INDEX_URL = "http://kohaumotu.org/Rongorongo/L/index.html"
CITED_LA_URL = "http://kohaumotu.org/Rongorongo/L/La.html"
CITED_L_URL = "http://kohaumotu.org/Rongorongo/L/L.html"

SIDE_LA = "La"
L_SIDES = (SIDE_LA,)

LA_LINE_NAMES = ("La1",)
L_LINE_NAMES = {SIDE_LA: LA_LINE_NAMES}

STANDING_LA_BYTES = 1301
STANDING_L_HTML_BYTES = 1070
STANDING_L_INDEX_BYTES = 2829
STANDING_LA_STEM_COUNTS = (51,)
STANDING_STEM_TOTALS = {SIDE_LA: 51}
STANDING_STEM_COUNTS = {SIDE_LA: STANDING_LA_STEM_COUNTS}
STANDING_L_ALL_LINES = ("La.html",)
STANDING_TABLET_L = ("L", "L/index.html", "Reimiro 2")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in L_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in L_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in L_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in L_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in L_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 0
STANDING_LONGEST_NGRAM = ()
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "l_reimiro_vendored"
STANDING_NEW_TABLET = True
STANDING_LA_HTML = True
STANDING_LB_HTML = False
STANDING_LR_HTML = False
STANDING_LV_HTML = False
STANDING_L_HTML = True
UNPUBLISHED_L_PAGES = ("Lb.html", "Lr.html", "Lv.html")


def load_vendored_la_html() -> str:
    """Return the vendored Kohaumotu La.html snapshot."""
    return LA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_l_html() -> str:
    """Return the vendored Kohaumotu L.html item snapshot."""
    return L_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_l_index_html() -> str:
    """Return the vendored Kohaumotu L/index.html snapshot."""
    return L_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_la_barthel_json() -> dict:
    """Return the vendored parsed La Barthel JSON."""
    return json.loads(LA_JSON_PATH.read_text(encoding="utf-8"))


def load_l_sides() -> dict[str, list[list[str]]]:
    """La stems from the vendored parser. No M scrape."""
    return {
        SIDE_LA: side_line_stems(
            extract_published_tokens(load_vendored_la_html(), SIDE_LA),
            LA_LINE_NAMES,
        ),
    }


def island_hits_by_l_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each L side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in L_SIDES
    }


def unpublished_l_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished L Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_L_PAGES if any(fixtures.glob(f"**/{name}")))


def score_l_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on La. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_LA],
        analyzer,
        line_names=LA_LINE_NAMES,
    )


class TestReimiro2VendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; LaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>607x-066-071*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_LA)
        self.assertEqual(list(published), ["La1"])
        self.assertEqual(published["La1"], ["607x", "066", "071*"])
        stems = side_line_stems(published, ("La1",))
        self.assertEqual(stems[0], ["607", "066", "071"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {SIDE_LA: [list(gram)]}
        hits = island_hits_by_l_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_LA][0], 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_l_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariReimiro2VendorScoreboard(unittest.TestCase):
    """Cited tablets.html → L → La lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.l_index = load_vendored_l_index_html()
        self.by_side = load_l_sides()
        self.gk_hits = island_hits_by_l_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_l_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in L_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in L_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in L_SIDES
        }
        self.profile = score_l_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_l(self):
        """Catalog → tablets → L index → La. Not Lb, Lr, or Lv. L.html is item only."""
        self.assertTrue(LA_HTML_PATH.is_file())
        self.assertTrue(L_HTML_PATH.is_file())
        self.assertTrue(LA_JSON_PATH.is_file())
        self.assertTrue((LA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(L_INDEX_HTML_PATH.is_file())
        self.assertFalse((LA_HTML_DIR / "Lb.html").exists())
        self.assertFalse((LA_HTML_DIR / "Lr.html").exists())
        self.assertFalse((LA_HTML_DIR / "Lv.html").exists())
        self.assertEqual(STANDING_LA_HTML, True)
        self.assertEqual(STANDING_LB_HTML, False)
        self.assertEqual(STANDING_LR_HTML, False)
        self.assertEqual(STANDING_LV_HTML, False)
        self.assertEqual(STANDING_L_HTML, True)
        self.assertEqual(LA_HTML_PATH.stat().st_size, STANDING_LA_BYTES)
        self.assertEqual(L_HTML_PATH.stat().st_size, STANDING_L_HTML_BYTES)
        self.assertEqual(L_INDEX_HTML_PATH.stat().st_size, STANDING_L_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "L"), STANDING_TABLET_L)
        self.assertEqual(published_all_lines_hrefs(self.l_index), STANDING_L_ALL_LINES)
        self.assertIn("Item L:Reimiro 2", self.l_index)
        self.assertIn('href="La.html"', self.l_index)
        self.assertIn('href="L.html"', self.l_index)
        self.assertNotIn('href="Lb.html"', self.l_index)
        self.assertNotIn('href="Lr.html"', self.l_index)
        self.assertNotIn('href="Lv.html"', self.l_index)
        la = load_vendored_la_html()
        item = load_vendored_l_html()
        self.assertIn("Item L:Rei Miro 2", la)
        self.assertIn("Item L:Rei Miro 2", item)
        self.assertIn("Rongorongo La1", la)
        self.assertIn("Rongorongo L", item)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', la)
        self.assertIn("607x-607x-066-071-002", la)
        self.assertNotIn('<h3><a name="Line_1">', item)
        self.assertEqual(extract_published_tokens(item, SIDE_LA), {})
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_l_html_names(fixtures), ())
        text = (LA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        for url in (
            CITED_CATALOG_URL,
            CITED_TABLETS_URL,
            CITED_L_INDEX_URL,
            CITED_LA_URL,
            CITED_L_URL,
        ):
            self.assertIn(url, text)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
        self.assertIn("tablet M", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        la_json = load_la_barthel_json()
        la_pub = extract_published_tokens(load_vendored_la_html(), SIDE_LA)
        self.assertEqual(la_json["tablet"], "L")
        self.assertEqual(la_json["side"], SIDE_LA)
        self.assertEqual(la_json["name"], "Reimiro 2")
        self.assertEqual(la_json["source"]["url"], CITED_LA_URL)
        self.assertEqual(la_json["lines"]["La1"], la_pub["La1"])
        self.assertEqual(la_json["stems"]["La1"], self.by_side[SIDE_LA][0])
        self.assertEqual(len(la_json["lines"]["La1"]), 44)
        self.assertEqual(len(la_json["stems"]["La1"]), 51)
        self.assertEqual(la_json["lines"]["La1"][0], "607x")
        self.assertEqual(la_json["stems"]["La1"][0], "607")
        self.assertEqual(la_json["lines"]["La1"][-1], "051*")
        self.assertEqual(la_json["stems"]["La1"][-1], "051")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E n=9, Er7 4-gram are 0 on L."""
        for side in L_SIDES:
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

    def test_longest_repeating_ngram_has_no_4gram(self):
        """L's own repeating profile: longest n=0; no n≥4 freq≥2. Not the claim."""
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

    def test_existing_j_reimiro_scoreboard_still_computes(self):
        """Cycle 86 J vendor lock stays."""
        prior = TestMamariReimiroVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_4gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-87 L vendor lock."""
        lock = self.survey["tablet_l_reimiro_vendor"]
        self.assertEqual(lock["cycle"], 87)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_l"], "L")
        self.assertEqual(lock["name_l"], "Reimiro 2")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["l_index"], CITED_L_INDEX_URL)
        self.assertEqual(lock["la_page"], CITED_LA_URL)
        self.assertEqual(lock["l_page"], CITED_L_URL)
        self.assertEqual(tuple(lock["l_pages"]), STANDING_L_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["La"], STANDING_LA_BYTES)
        self.assertEqual(lock["html_bytes"]["L"], STANDING_L_HTML_BYTES)
        self.assertEqual(lock["stem_totals"]["La"], STANDING_STEM_TOTALS[SIDE_LA])
        self.assertEqual(tuple(lock["stem_counts"]["La"]), STANDING_LA_STEM_COUNTS)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["La"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["La"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["La"], 0)
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
        self.assertTrue(lock["la_html"])
        self.assertFalse(lock["lb_html"])
        self.assertFalse(lock["lr_html"])
        self.assertFalse(lock["lv_html"])
        self.assertTrue(lock["l_html"])
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
        self.assertEqual(self.survey["tablet_j_reimiro_vendor"]["cycle"], 86)
        self.assertEqual(self.survey["tablet_f_chauvet_vendor"]["cycle"], 85)
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["cycle"], 80)
        self.assertEqual(self.survey["tablet_e_keiti_er7_double"]["cycle"], 84)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariReimiro2VendorImageSnapshot(unittest.TestCase):
    """Cycle 87 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
