"""Small St Petersburg (Q) vendor lock.

Cycle 70 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / G / H / I / K / P. Q/index.html
names Qr/Qv (Gr vs Ga lesson: Qa.html is an unpublished 404).
Digits are copied from the snapshots. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents.

Locks per vendored side: stem count; exact hits of the six cycle-67
G–K islands (expect 0). Does not scrape D.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    TestMamariLargeSantiagoStPetersburgVendorScoreboard,
    extract_published_tokens,
    side_line_stems,
    tablet_row,
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
from tests.test_mamari_small_santiago_london_island_off_gk_scoreboard import (
    LOCKED_ISLANDS,
)
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html

QR_HTML_DIR = Path(__file__).parent / "fixtures" / "small_st_petersburg_qr_html"
QV_HTML_DIR = Path(__file__).parent / "fixtures" / "small_st_petersburg_qv_html"
QR_HTML_PATH = QR_HTML_DIR / "Qr.html"
QV_HTML_PATH = QV_HTML_DIR / "Qv.html"
Q_INDEX_HTML_PATH = QR_HTML_DIR / "Q_index.html"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_Q_INDEX_URL = "http://kohaumotu.org/Rongorongo/Q/index.html"
CITED_QR_URL = "http://kohaumotu.org/Rongorongo/Q/Qr.html"
CITED_QV_URL = "http://kohaumotu.org/Rongorongo/Q/Qv.html"

SIDE_QR = "Qr"
SIDE_QV = "Qv"
Q_SIDES = (SIDE_QR, SIDE_QV)

QR_LINE_NAMES = tuple(f"Qr{n}" for n in range(1, 10))
QV_LINE_NAMES = tuple(f"Qv{n}" for n in range(1, 10))
Q_LINE_NAMES = {
    SIDE_QR: QR_LINE_NAMES,
    SIDE_QV: QV_LINE_NAMES,
}

STANDING_QR_BYTES = 7119
STANDING_QV_BYTES = 6663
STANDING_Q_INDEX_BYTES = 4232
STANDING_QR_STEM_COUNTS = (18, 59, 66, 60, 69, 50, 59, 63, 59)
STANDING_QV_STEM_COUNTS = (57, 62, 57, 52, 52, 45, 46, 41, 11)
STANDING_STEM_TOTALS = {
    SIDE_QR: 503,
    SIDE_QV: 423,
}
STANDING_STEM_COUNTS = {
    SIDE_QR: STANDING_QR_STEM_COUNTS,
    SIDE_QV: STANDING_QV_STEM_COUNTS,
}
STANDING_Q_ALL_LINES = ("Qr.html", "Qv.html")
STANDING_TABLET_Q = ("Q", "Q/index.html", "Small St.Petersburg")
STANDING_ISLAND_HITS = {
    side: (0,) * len(LOCKED_ISLANDS) for side in Q_SIDES
}
STANDING_ANY_GK_ISLAND = False
STANDING_RESULT = "q_small_st_petersburg_vendored"
STANDING_NEW_TABLET = True
STANDING_TABLET_D_SCRAPED = False
STANDING_QA_HTML = False
ABSENT_Q_AND_D_PAGES = (
    "Q.html",
    "Qa.html",
    "Qb.html",
) + FOURTH_TABLET_PAGES


def load_vendored_qr_html() -> str:
    """Return the vendored Kohaumotu Qr.html snapshot."""
    return QR_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_qv_html() -> str:
    """Return the vendored Kohaumotu Qv.html snapshot."""
    return QV_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_q_index_html() -> str:
    """Return the vendored Kohaumotu Q/index.html snapshot."""
    return Q_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_q_sides() -> dict[str, list[list[str]]]:
    """Qr / Qv stems from the vendored parsers. No D scrape."""
    return {
        SIDE_QR: side_line_stems(
            extract_published_tokens(load_vendored_qr_html(), SIDE_QR),
            QR_LINE_NAMES,
        ),
        SIDE_QV: side_line_stems(
            extract_published_tokens(load_vendored_qv_html(), SIDE_QV),
            QV_LINE_NAMES,
        ),
    }


def island_hits_by_q_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] = LOCKED_ISLANDS,
) -> dict[str, tuple[int, ...]]:
    """Exact G–K island hits on each Q side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in Q_SIDES
    }


def forbidden_d_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished Q / D Barthel filenames under fixtures, if any."""
    return tuple(name for name in ABSENT_Q_AND_D_PAGES if any(fixtures.glob(f"**/{name}")))


class TestSmallStPetersburgVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; QrN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>304.003-000.003</td></tr></table>"
            '<h3><a name="Line_9">Line 9</a></h3>'
            "<table><tr><td>001-004-064-</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_QR)
        self.assertEqual(list(published), ["Qr1", "Qr9"])
        self.assertEqual(published["Qr1"], ["304.003", "000.003"])
        self.assertEqual(published["Qr9"], ["001", "004", "064"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = LOCKED_ISLANDS[0]
        by_side = {side: [[]] for side in Q_SIDES}
        by_side[SIDE_QR] = [list(gram)]
        hits = island_hits_by_q_side(by_side)
        self.assertEqual(hits[SIDE_QR][0], 1)
        self.assertEqual(hits[SIDE_QV], (0,) * len(LOCKED_ISLANDS))
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(forbidden_d_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallStPetersburgVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → Q → Qr/Qv lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.q_index = load_vendored_q_index_html()
        self.by_side = load_q_sides()
        self.island_hits = island_hits_by_q_side(self.by_side)

    def test_parent_catalog_selects_and_vendors_q(self):
        """Catalog → tablets → Q index → Qr/Qv. Not Qa or D."""
        self.assertTrue(QR_HTML_PATH.is_file())
        self.assertTrue(QV_HTML_PATH.is_file())
        self.assertTrue((QR_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((QV_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(Q_INDEX_HTML_PATH.is_file())
        self.assertFalse((QR_HTML_DIR / "Qa.html").exists())
        self.assertFalse((QR_HTML_DIR / "Qb.html").exists())
        self.assertFalse((QR_HTML_DIR / "Q.html").exists())
        self.assertEqual(STANDING_QA_HTML, False)
        self.assertEqual(QR_HTML_PATH.stat().st_size, STANDING_QR_BYTES)
        self.assertEqual(QV_HTML_PATH.stat().st_size, STANDING_QV_BYTES)
        self.assertEqual(Q_INDEX_HTML_PATH.stat().st_size, STANDING_Q_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "Q"), STANDING_TABLET_Q)
        self.assertEqual(published_all_lines_hrefs(self.q_index), STANDING_Q_ALL_LINES)
        self.assertIn("Item Q:The Small St. Petersburg tablet", self.q_index)
        self.assertIn('href="Qr.html"', self.q_index)
        self.assertIn('href="Qv.html"', self.q_index)
        self.assertNotIn('href="Qa.html"', self.q_index)
        qr = load_vendored_qr_html()
        qv = load_vendored_qv_html()
        self.assertIn("Item Q:The Small St. Petersburg Tablet", qr)
        self.assertIn("The Small St. Petersburg Tablet", qv)
        self.assertIn("Rongorongo Qr", qr)
        self.assertIn("Rongorongo Qv", qv)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(forbidden_d_html_names(fixtures), ())
        self.assertEqual(fourth_tablet_html_names(fixtures), ())
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        for directory, urls in (
            (QR_HTML_DIR, (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_Q_INDEX_URL, CITED_QR_URL)),
            (QV_HTML_DIR, (CITED_QV_URL, CITED_Q_INDEX_URL)),
        ):
            text = (directory / "ATTRIBUTION").read_text(encoding="utf-8")
            for url in urls:
                self.assertIn(url, text)
            self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
            self.assertIn("tablet D", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_gk_islands_absent(self):
        """Per-side stem totals; six G–K islands are 0 on every Q side."""
        for side in Q_SIDES:
            counts = [len(line) for line in self.by_side[side]]
            self.assertEqual(counts, list(STANDING_STEM_COUNTS[side]))
            self.assertEqual(sum(counts), STANDING_STEM_TOTALS[side])
            self.assertEqual(self.island_hits[side], STANDING_ISLAND_HITS[side])
            for gram, count in zip(LOCKED_ISLANDS, self.island_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
        self.assertFalse(any(any(hits) for hits in self.island_hits.values()))
        self.assertEqual(STANDING_ANY_GK_ISLAND, False)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_hp_vendor_scoreboard_still_computes(self):
        """Cycle 69 H/P vendor and G–K island-absent lock stays."""
        prior = TestMamariLargeSantiagoStPetersburgVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_gk_islands_absent()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-70 Q vendor lock."""
        lock = self.survey["tablet_q_small_st_petersburg_vendor"]
        self.assertEqual(lock["cycle"], 70)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_q"], "Q")
        self.assertEqual(lock["name_q"], "Small St. Petersburg")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["q_index"], CITED_Q_INDEX_URL)
        self.assertEqual(tuple(lock["q_pages"]), STANDING_Q_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Qr"], STANDING_QR_BYTES)
        self.assertEqual(lock["html_bytes"]["Qv"], STANDING_QV_BYTES)
        self.assertEqual(lock["stem_totals"]["Qr"], STANDING_STEM_TOTALS[SIDE_QR])
        self.assertEqual(lock["stem_totals"]["Qv"], STANDING_STEM_TOTALS[SIDE_QV])
        self.assertEqual(tuple(lock["stem_counts"]["Qr"]), STANDING_QR_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Qv"]), STANDING_QV_STEM_COUNTS)
        locked_hits = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        self.assertEqual(locked_hits, STANDING_ISLAND_HITS)
        self.assertFalse(lock["any_gk_island"])
        self.assertTrue(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertFalse(lock["qa_html"])
        self.assertTrue(lock["standing_hp_vendor_unchanged"])
        self.assertTrue(lock["standing_hp_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_h_p_grand_tradition_vendor"]["cycle"], 69)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallStPetersburgVendorImageSnapshot(unittest.TestCase):
    """Cycle 70 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
