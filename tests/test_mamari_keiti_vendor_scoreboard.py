"""Keiti (E) vendor lock.

Cycle 80 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / G / H / I / K / P / Q. HEAD-check
before filename assume (cycle 54 Gr vs Ga; cycle 79 Da vs Dr):
Ea.html / Eb.html / E.html are unpublished 404s. E/index.html names
Er.html / Ev.html (r/v, like G/H/K/P/Q). Digits are copied from the
snapshots. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. No second new letter.

Locks per vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; E's own longest repeating n-gram (n and whether
n≥8 exists). D's locked facts stay. Claim that can lose: known
tradition islands are exact-0 on E (closed-tradition hold-out).
E is not short (longest n=9; n≥8 exists), so the hold-out is the
lock that can leak.

Search lock, not a merge and not a translation. MockProvider only.
"""

import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_echancree_vendor_scoreboard import (
    TestMamariEchancreeVendorScoreboard,
)
from tests.test_mamari_gk_islands_off_hpq_scoreboard import (
    LOCKED_GRAMS as GK_LOCKED_GRAMS,
)
from tests.test_mamari_hpq_island_off_hpq_scoreboard import (
    LOCKED_ISLANDS as HPQ_LOCKED_ISLANDS,
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

ER_HTML_DIR = Path(__file__).parent / "fixtures" / "keiti_er_html"
EV_HTML_DIR = Path(__file__).parent / "fixtures" / "keiti_ev_html"
ER_HTML_PATH = ER_HTML_DIR / "Er.html"
EV_HTML_PATH = EV_HTML_DIR / "Ev.html"
E_INDEX_HTML_PATH = ER_HTML_DIR / "E_index.html"
ER_JSON_PATH = ER_HTML_DIR / "Er_barthel.json"
EV_JSON_PATH = EV_HTML_DIR / "Ev_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_E_INDEX_URL = "http://kohaumotu.org/Rongorongo/E/index.html"
CITED_ER_URL = "http://kohaumotu.org/Rongorongo/E/Er.html"
CITED_EV_URL = "http://kohaumotu.org/Rongorongo/E/Ev.html"

SIDE_ER = "Er"
SIDE_EV = "Ev"
E_SIDES = (SIDE_ER, SIDE_EV)

ER_LINE_NAMES = tuple(f"Er{n}" for n in range(1, 10))
EV_LINE_NAMES = tuple(f"Ev{n}" for n in range(1, 9))
E_LINE_NAMES = {
    SIDE_ER: ER_LINE_NAMES,
    SIDE_EV: EV_LINE_NAMES,
}

STANDING_ER_BYTES = 6438
STANDING_EV_BYTES = 5481
STANDING_E_INDEX_BYTES = 3961
STANDING_ER_STEM_COUNTS = (56, 54, 48, 55, 53, 53, 49, 50, 44)
STANDING_EV_STEM_COUNTS = (52, 45, 59, 55, 51, 56, 53, 53)
STANDING_STEM_TOTALS = {
    SIDE_ER: 462,
    SIDE_EV: 424,
}
STANDING_STEM_COUNTS = {
    SIDE_ER: STANDING_ER_STEM_COUNTS,
    SIDE_EV: STANDING_EV_STEM_COUNTS,
}
STANDING_E_ALL_LINES = ("Er.html", "Ev.html")
STANDING_TABLET_E = ("E", "E/index.html", "Keiti")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in E_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in E_SIDES
}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_TRADITION_ISLAND = False
STANDING_LONGEST_N = 9
STANDING_LONGEST_NGRAM = (
    "300",
    "040",
    "300",
    "028",
    "004",
    "430",
    "022",
    "380",
    "203",
)
STANDING_EIGHTGRAM_EXISTS = True
STANDING_EIGHTGRAM_COUNT = 4
STANDING_CLAIM = "tradition_islands_absent"
STANDING_RESULT = "e_keiti_vendored"
STANDING_NEW_TABLET = True
STANDING_EA_HTML = False
STANDING_EB_HTML = False
STANDING_E_HTML = False
UNPUBLISHED_E_PAGES = ("E.html", "Ea.html", "Eb.html")


def load_vendored_er_html() -> str:
    """Return the vendored Kohaumotu Er.html snapshot."""
    return ER_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_ev_html() -> str:
    """Return the vendored Kohaumotu Ev.html snapshot."""
    return EV_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_e_index_html() -> str:
    """Return the vendored Kohaumotu E/index.html snapshot."""
    return E_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_er_barthel_json() -> dict:
    """Return the vendored parsed Er Barthel JSON."""
    return json.loads(ER_JSON_PATH.read_text(encoding="utf-8"))


def load_ev_barthel_json() -> dict:
    """Return the vendored parsed Ev Barthel JSON."""
    return json.loads(EV_JSON_PATH.read_text(encoding="utf-8"))


def load_e_sides() -> dict[str, list[list[str]]]:
    """Er / Ev stems from the vendored parsers. No F scrape."""
    return {
        SIDE_ER: side_line_stems(
            extract_published_tokens(load_vendored_er_html(), SIDE_ER),
            ER_LINE_NAMES,
        ),
        SIDE_EV: side_line_stems(
            extract_published_tokens(load_vendored_ev_html(), SIDE_EV),
            EV_LINE_NAMES,
        ),
    }


def island_hits_by_e_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each E side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in E_SIDES
    }


def unpublished_e_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished E Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_E_PAGES if any(fixtures.glob(f"**/{name}")))


def score_e_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on combined Er+Ev. Search only."""
    lines = by_side[SIDE_ER] + by_side[SIDE_EV]
    names = ER_LINE_NAMES + EV_LINE_NAMES
    return score_remainder_repeating_ngrams(lines, analyzer, line_names=names)


class TestKeitiVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; ErN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>040?-630?-004-</td></tr></table>"
            '<h3><a name="Line_9">Line 9</a></h3>'
            "<table><tr><td>300.040</td></tr>"
            "<tr><td>*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_ER)
        self.assertEqual(list(published), ["Er1", "Er9"])
        self.assertEqual(published["Er1"], ["040?", "630?", "004"])
        self.assertEqual(published["Er9"], ["300.040"])
        stems = side_line_stems(published, ("Er1", "Er9"))
        self.assertEqual(stems[0], ["040", "630", "004"])
        self.assertEqual(stems[1], ["300", "040"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {side: [[]] for side in E_SIDES}
        by_side[SIDE_ER] = [list(gram)]
        hits = island_hits_by_e_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_ER][0], 1)
        self.assertEqual(hits[SIDE_EV], (0,) * len(GK_LOCKED_GRAMS))
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_e_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariKeitiVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → E → Er/Ev lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.e_index = load_vendored_e_index_html()
        self.by_side = load_e_sides()
        self.gk_hits = island_hits_by_e_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_e_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.profile = score_e_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_e(self):
        """Catalog → tablets → E index → Er/Ev. Not Ea, Eb, or E.html."""
        self.assertTrue(ER_HTML_PATH.is_file())
        self.assertTrue(EV_HTML_PATH.is_file())
        self.assertTrue(ER_JSON_PATH.is_file())
        self.assertTrue(EV_JSON_PATH.is_file())
        self.assertTrue((ER_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((EV_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(E_INDEX_HTML_PATH.is_file())
        self.assertFalse((ER_HTML_DIR / "Ea.html").exists())
        self.assertFalse((ER_HTML_DIR / "Eb.html").exists())
        self.assertFalse((ER_HTML_DIR / "E.html").exists())
        self.assertFalse((EV_HTML_DIR / "Ea.html").exists())
        self.assertEqual(STANDING_EA_HTML, False)
        self.assertEqual(STANDING_EB_HTML, False)
        self.assertEqual(STANDING_E_HTML, False)
        self.assertEqual(ER_HTML_PATH.stat().st_size, STANDING_ER_BYTES)
        self.assertEqual(EV_HTML_PATH.stat().st_size, STANDING_EV_BYTES)
        self.assertEqual(E_INDEX_HTML_PATH.stat().st_size, STANDING_E_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "E"), STANDING_TABLET_E)
        self.assertEqual(published_all_lines_hrefs(self.e_index), STANDING_E_ALL_LINES)
        self.assertIn("Item E:Keiti", self.e_index)
        self.assertIn('href="Er.html"', self.e_index)
        self.assertIn('href="Ev.html"', self.e_index)
        self.assertNotIn('href="Ea.html"', self.e_index)
        self.assertNotIn('href="Eb.html"', self.e_index)
        er = load_vendored_er_html()
        ev = load_vendored_ev_html()
        self.assertIn("Item E:Keiti", er)
        self.assertIn("Item E:Keiti", ev)
        self.assertIn("Rongorongo Er", er)
        self.assertIn("Rongorongo Ev", ev)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_e_html_names(fixtures), ())
        for directory, urls in (
            (ER_HTML_DIR, (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_E_INDEX_URL, CITED_ER_URL)),
            (EV_HTML_DIR, (CITED_EV_URL, CITED_E_INDEX_URL)),
        ):
            text = (directory / "ATTRIBUTION").read_text(encoding="utf-8")
            for url in urls:
                self.assertIn(url, text)
            self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
            self.assertIn("tablet F", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        er_json = load_er_barthel_json()
        ev_json = load_ev_barthel_json()
        er_pub = extract_published_tokens(load_vendored_er_html(), SIDE_ER)
        ev_pub = extract_published_tokens(load_vendored_ev_html(), SIDE_EV)
        self.assertEqual(er_json["tablet"], "E")
        self.assertEqual(ev_json["tablet"], "E")
        self.assertEqual(er_json["side"], SIDE_ER)
        self.assertEqual(ev_json["side"], SIDE_EV)
        self.assertEqual(er_json["source"]["url"], CITED_ER_URL)
        self.assertEqual(ev_json["source"]["url"], CITED_EV_URL)
        for name in ER_LINE_NAMES:
            self.assertEqual(er_json["lines"][name], er_pub[name])
            self.assertEqual(er_json["stems"][name], self.by_side[SIDE_ER][int(name[2:]) - 1])
        for name in EV_LINE_NAMES:
            self.assertEqual(ev_json["lines"][name], ev_pub[name])
            self.assertEqual(ev_json["stems"][name], self.by_side[SIDE_EV][int(name[2:]) - 1])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_tradition_islands_absent(self):
        """Per-side stem totals; G–K + n=25 and H∩P∩Q islands are 0 on E."""
        for side in E_SIDES:
            counts = [len(line) for line in self.by_side[side]]
            self.assertEqual(counts, list(STANDING_STEM_COUNTS[side]))
            self.assertEqual(sum(counts), STANDING_STEM_TOTALS[side])
            self.assertEqual(self.gk_hits[side], STANDING_GK_ISLAND_HITS[side])
            self.assertEqual(self.hpq_hits[side], STANDING_HPQ_ISLAND_HITS[side])
            for gram, count in zip(GK_LOCKED_GRAMS, self.gk_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            for gram, count in zip(HPQ_LOCKED_ISLANDS, self.hpq_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
        self.assertFalse(any(any(hits) for hits in self.gk_hits.values()))
        self.assertFalse(any(any(hits) for hits in self.hpq_hits.values()))
        self.assertEqual(STANDING_ANY_GK_ISLAND, False)
        self.assertEqual(STANDING_ANY_HPQ_ISLAND, False)
        self.assertEqual(STANDING_ANY_TRADITION_ISLAND, False)
        self.assertEqual(STANDING_CLAIM, "tradition_islands_absent")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_repeating_ngram_is_9_and_eightgrams_exist(self):
        """E's own repeating profile: longest n=9; n≥8 exists. Not the claim."""
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest_n, 9)
        self.assertTrue(any(row.n >= 8 for row in self.profile.rows))
        self.assertTrue(STANDING_EIGHTGRAM_EXISTS)
        self.assertEqual(len(self.profile.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertIsNotNone(self.profile.top_8gram)
        self.assertEqual(self.profile.longest[0].tokens, STANDING_LONGEST_NGRAM)
        self.assertNotEqual(STANDING_CLAIM, "no_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_d_echancree_scoreboard_still_computes(self):
        """Cycle 79 D vendor lock stays."""
        prior = TestMamariEchancreeVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_tradition_islands_absent()
        prior.test_longest_repeating_ngram_has_no_8gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-80 E vendor lock."""
        lock = self.survey["tablet_e_keiti_vendor"]
        self.assertEqual(lock["cycle"], 80)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_e"], "E")
        self.assertEqual(lock["name_e"], "Keiti")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["e_index"], CITED_E_INDEX_URL)
        self.assertEqual(lock["er_page"], CITED_ER_URL)
        self.assertEqual(lock["ev_page"], CITED_EV_URL)
        self.assertEqual(tuple(lock["e_pages"]), STANDING_E_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Er"], STANDING_ER_BYTES)
        self.assertEqual(lock["html_bytes"]["Ev"], STANDING_EV_BYTES)
        self.assertEqual(lock["stem_totals"]["Er"], STANDING_STEM_TOTALS[SIDE_ER])
        self.assertEqual(lock["stem_totals"]["Ev"], STANDING_STEM_TOTALS[SIDE_EV])
        self.assertEqual(tuple(lock["stem_counts"]["Er"]), STANDING_ER_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Ev"]), STANDING_EV_STEM_COUNTS)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertFalse(lock["any_gk_island"])
        self.assertFalse(lock["any_hpq_island"])
        self.assertFalse(lock["any_tradition_island"])
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertTrue(lock["eightgram_exists"])
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["new_tablet"])
        self.assertFalse(lock["ea_html"])
        self.assertFalse(lock["eb_html"])
        self.assertFalse(lock["e_html"])
        self.assertTrue(lock["standing_d_echancree_vendor_unchanged"])
        self.assertTrue(lock["standing_q_vendor_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_maximals_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_d_echancree_vendor"]["cycle"], 79)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariKeitiVendorImageSnapshot(unittest.TestCase):
    """Cycle 80 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
