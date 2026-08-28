"""Échancrée (D) vendor lock.

Cycle 79 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / G / H / I / K / P / Q. HEAD-check
before filename assume (cycle 54 Gr vs Ga): Dr.html / Dv.html /
D.html are unpublished 404s. D/index.html names Da.html / Db.html
(a/b, like A/C). Digits are copied from the snapshots. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. No second new letter.

Locks per vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; D's own longest repeating n-gram (n and whether
n≥8 exists). Claim that can lose: known tradition islands are
exact-0 on D (closed-tradition hold-out). Stronger than "no 8-gram"
because both measured true and the hold-out is the one that can leak.

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
    FOURTH_TABLET_PAGES,
    fourth_tablet_html_names,
    published_all_lines_hrefs,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_grkv_maximal_scoreboard import (
    TestMamariSmallSantiagoLondonGrkvMaximalScoreboard,
)
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html

DA_HTML_DIR = Path(__file__).parent / "fixtures" / "echancree_da_html"
DB_HTML_DIR = Path(__file__).parent / "fixtures" / "echancree_db_html"
DA_HTML_PATH = DA_HTML_DIR / "Da.html"
DB_HTML_PATH = DB_HTML_DIR / "Db.html"
D_INDEX_HTML_PATH = DA_HTML_DIR / "D_index.html"
DA_JSON_PATH = DA_HTML_DIR / "Da_barthel.json"
DB_JSON_PATH = DB_HTML_DIR / "Db_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_D_INDEX_URL = "http://kohaumotu.org/Rongorongo/D/index.html"
CITED_DA_URL = "http://kohaumotu.org/Rongorongo/D/Da.html"
CITED_DB_URL = "http://kohaumotu.org/Rongorongo/D/Db.html"

SIDE_DA = "Da"
SIDE_DB = "Db"
D_SIDES = (SIDE_DA, SIDE_DB)

DA_LINE_NAMES = tuple(f"Da{n}" for n in range(1, 9))
DB_LINE_NAMES = tuple(f"Db{n}" for n in range(1, 7))
D_LINE_NAMES = {
    SIDE_DA: DA_LINE_NAMES,
    SIDE_DB: DB_LINE_NAMES,
}

STANDING_DA_BYTES = 3469
STANDING_DB_BYTES = 2760
STANDING_D_INDEX_BYTES = 3770
STANDING_DA_STEM_COUNTS = (17, 22, 22, 23, 24, 22, 20, 0)
STANDING_DB_STEM_COUNTS = (16, 23, 23, 19, 20, 15)
STANDING_STEM_TOTALS = {
    SIDE_DA: 150,
    SIDE_DB: 116,
}
STANDING_STEM_COUNTS = {
    SIDE_DA: STANDING_DA_STEM_COUNTS,
    SIDE_DB: STANDING_DB_STEM_COUNTS,
}
STANDING_D_ALL_LINES = ("Da.html", "Db.html")
STANDING_TABLET_D = ("D", "D/index.html", "Échancrée")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in D_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in D_SIDES
}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_TRADITION_ISLAND = False
STANDING_LONGEST_N = 4
STANDING_EIGHTGRAM_EXISTS = False
STANDING_CLAIM = "tradition_islands_absent"
STANDING_RESULT = "d_echancree_vendored"
STANDING_NEW_TABLET = True
STANDING_DR_HTML = False
STANDING_DV_HTML = False
STANDING_D_HTML = False
UNPUBLISHED_D_PAGES = FOURTH_TABLET_PAGES


def load_vendored_da_html() -> str:
    """Return the vendored Kohaumotu Da.html snapshot."""
    return DA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_db_html() -> str:
    """Return the vendored Kohaumotu Db.html snapshot."""
    return DB_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_d_index_html() -> str:
    """Return the vendored Kohaumotu D/index.html snapshot."""
    return D_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_da_barthel_json() -> dict:
    """Return the vendored parsed Da Barthel JSON."""
    return json.loads(DA_JSON_PATH.read_text(encoding="utf-8"))


def load_db_barthel_json() -> dict:
    """Return the vendored parsed Db Barthel JSON."""
    return json.loads(DB_JSON_PATH.read_text(encoding="utf-8"))


def load_d_sides() -> dict[str, list[list[str]]]:
    """Da / Db stems from the vendored parsers. No E scrape."""
    return {
        SIDE_DA: side_line_stems(
            extract_published_tokens(load_vendored_da_html(), SIDE_DA),
            DA_LINE_NAMES,
        ),
        SIDE_DB: side_line_stems(
            extract_published_tokens(load_vendored_db_html(), SIDE_DB),
            DB_LINE_NAMES,
        ),
    }


def island_hits_by_d_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each D side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in D_SIDES
    }


def unpublished_d_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished D Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_D_PAGES if any(fixtures.glob(f"**/{name}")))


def score_d_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on combined Da+Db. Search only."""
    lines = by_side[SIDE_DA] + by_side[SIDE_DB]
    names = DA_LINE_NAMES + DB_LINE_NAMES
    return score_remainder_repeating_ngrams(lines, analyzer, line_names=names)


class TestEchancreeVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; DaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>000!-006-381-</td></tr></table>"
            '<h3><a name="Line_8">Line 8</a></h3>'
            "<table><tr><td>(10-20)!</td></tr>"
            "<tr><td>*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_DA)
        self.assertEqual(list(published), ["Da1", "Da8"])
        self.assertEqual(published["Da1"], ["000!", "006", "381"])
        self.assertEqual(published["Da8"], ["(10", "20)!"])
        stems = side_line_stems(published, ("Da1", "Da8"))
        self.assertEqual(stems[0], ["000", "006", "381"])
        self.assertEqual(stems[1], [])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {side: [[]] for side in D_SIDES}
        by_side[SIDE_DA] = [list(gram)]
        hits = island_hits_by_d_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_DA][0], 1)
        self.assertEqual(hits[SIDE_DB], (0,) * len(GK_LOCKED_GRAMS))
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_d_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariEchancreeVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → D → Da/Db lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.d_index = load_vendored_d_index_html()
        self.by_side = load_d_sides()
        self.gk_hits = island_hits_by_d_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_d_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.profile = score_d_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_d(self):
        """Catalog → tablets → D index → Da/Db. Not Dr, Dv, or D.html."""
        self.assertTrue(DA_HTML_PATH.is_file())
        self.assertTrue(DB_HTML_PATH.is_file())
        self.assertTrue(DA_JSON_PATH.is_file())
        self.assertTrue(DB_JSON_PATH.is_file())
        self.assertTrue((DA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((DB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(D_INDEX_HTML_PATH.is_file())
        self.assertFalse((DA_HTML_DIR / "Dr.html").exists())
        self.assertFalse((DA_HTML_DIR / "Dv.html").exists())
        self.assertFalse((DA_HTML_DIR / "D.html").exists())
        self.assertFalse((DB_HTML_DIR / "Dr.html").exists())
        self.assertEqual(STANDING_DR_HTML, False)
        self.assertEqual(STANDING_DV_HTML, False)
        self.assertEqual(STANDING_D_HTML, False)
        self.assertEqual(DA_HTML_PATH.stat().st_size, STANDING_DA_BYTES)
        self.assertEqual(DB_HTML_PATH.stat().st_size, STANDING_DB_BYTES)
        self.assertEqual(D_INDEX_HTML_PATH.stat().st_size, STANDING_D_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "D"), STANDING_TABLET_D)
        self.assertEqual(published_all_lines_hrefs(self.d_index), STANDING_D_ALL_LINES)
        self.assertIn("Item D:Échancrée", self.d_index)
        self.assertIn('href="Da.html"', self.d_index)
        self.assertIn('href="Db.html"', self.d_index)
        self.assertNotIn('href="Dr.html"', self.d_index)
        self.assertNotIn('href="Dv.html"', self.d_index)
        da = load_vendored_da_html()
        db = load_vendored_db_html()
        self.assertIn("Item D:Échancrée", da)
        self.assertIn("Item D:Échancrée", db)
        self.assertIn("Rongorongo Da", da)
        self.assertIn("Rongorongo Db", db)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_d_html_names(fixtures), ())
        self.assertEqual(fourth_tablet_html_names(fixtures), ())
        self.assertEqual(FOURTH_TABLET_PAGES[0], "D.html")
        for directory, urls in (
            (DA_HTML_DIR, (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_D_INDEX_URL, CITED_DA_URL)),
            (DB_HTML_DIR, (CITED_DB_URL, CITED_D_INDEX_URL)),
        ):
            text = (directory / "ATTRIBUTION").read_text(encoding="utf-8")
            for url in urls:
                self.assertIn(url, text)
            self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
            self.assertIn("tablet E", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        da_json = load_da_barthel_json()
        db_json = load_db_barthel_json()
        da_pub = extract_published_tokens(load_vendored_da_html(), SIDE_DA)
        db_pub = extract_published_tokens(load_vendored_db_html(), SIDE_DB)
        self.assertEqual(da_json["tablet"], "D")
        self.assertEqual(db_json["tablet"], "D")
        self.assertEqual(da_json["side"], SIDE_DA)
        self.assertEqual(db_json["side"], SIDE_DB)
        self.assertEqual(da_json["source"]["url"], CITED_DA_URL)
        self.assertEqual(db_json["source"]["url"], CITED_DB_URL)
        for name in DA_LINE_NAMES:
            self.assertEqual(da_json["lines"][name], da_pub[name])
            self.assertEqual(da_json["stems"][name], self.by_side[SIDE_DA][int(name[2:]) - 1])
        for name in DB_LINE_NAMES:
            self.assertEqual(db_json["lines"][name], db_pub[name])
            self.assertEqual(db_json["stems"][name], self.by_side[SIDE_DB][int(name[2:]) - 1])
        self.assertEqual(da_json["lines"]["Da8"], ["(10", "20)!"])
        self.assertEqual(da_json["stems"]["Da8"], [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_tradition_islands_absent(self):
        """Per-side stem totals; G–K + n=25 and H∩P∩Q islands are 0 on D."""
        for side in D_SIDES:
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

    def test_longest_repeating_ngram_has_no_8gram(self):
        """D's own repeating profile: longest n=4; no n≥8. Not the claim."""
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest_n, 4)
        self.assertFalse(any(row.n >= 8 for row in self.profile.rows))
        self.assertFalse(STANDING_EIGHTGRAM_EXISTS)
        self.assertEqual(self.profile.eightgrams, ())
        self.assertIsNone(self.profile.top_8gram)
        self.assertNotEqual(STANDING_CLAIM, "no_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_grkv_maximal_scoreboard_still_computes(self):
        """Cycle 78 Gr–Kv maximal lock stays."""
        prior = TestMamariSmallSantiagoLondonGrkvMaximalScoreboard()
        prior.setUp()
        prior.test_n15_is_suffix_of_n25_not_a_maximal()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-79 D vendor lock."""
        lock = self.survey["tablet_d_echancree_vendor"]
        self.assertEqual(lock["cycle"], 79)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_d"], "D")
        self.assertEqual(lock["name_d"], "Échancrée")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["d_index"], CITED_D_INDEX_URL)
        self.assertEqual(tuple(lock["d_pages"]), STANDING_D_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Da"], STANDING_DA_BYTES)
        self.assertEqual(lock["html_bytes"]["Db"], STANDING_DB_BYTES)
        self.assertEqual(lock["stem_totals"]["Da"], STANDING_STEM_TOTALS[SIDE_DA])
        self.assertEqual(lock["stem_totals"]["Db"], STANDING_STEM_TOTALS[SIDE_DB])
        self.assertEqual(tuple(lock["stem_counts"]["Da"]), STANDING_DA_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Db"]), STANDING_DB_STEM_COUNTS)
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
        self.assertFalse(lock["eightgram_exists"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["new_tablet"])
        self.assertFalse(lock["dr_html"])
        self.assertFalse(lock["dv_html"])
        self.assertFalse(lock["d_html"])
        self.assertTrue(lock["standing_q_vendor_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_maximals_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_grkv_maximals"]["cycle"], 78)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariEchancreeVendorImageSnapshot(unittest.TestCase):
    """Cycle 79 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
