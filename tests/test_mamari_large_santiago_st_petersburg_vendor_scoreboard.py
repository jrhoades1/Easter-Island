"""Large Santiago (H) and Large St Petersburg (P) vendor lock.

Cycle 69 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / G / I / K. H/index.html and
P/index.html name Hr/Hv and Pr/Pv (Gr vs Ga lesson: Ha.html and
Pa.html are unpublished 404s). Digits are copied from the
snapshots. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents.

Locks per vendored side: stem count; exact hits of the six cycle-67
G–K islands (expect 0). Does not scrape Q or D.

Search lock, not a merge and not a translation. MockProvider only.
"""

import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ib_scoreboard import (
    FOURTH_TABLET_PAGES,
    fourth_tablet_html_names,
    published_all_lines_hrefs,
)
from tests.test_mamari_second_passage_scoreboard import (
    _LINE_HEADER,
    load_corpus_survey,
    published_stems,
)
from tests.test_mamari_small_santiago_london_island_off_gk_scoreboard import (
    LOCKED_ISLANDS,
    TestMamariSmallSantiagoLondonIslandOffGkScoreboard,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    _TABLET_ROW,
    load_vendored_tablets_html,
)

HR_HTML_DIR = Path(__file__).parent / "fixtures" / "large_santiago_hr_html"
HV_HTML_DIR = Path(__file__).parent / "fixtures" / "large_santiago_hv_html"
PR_HTML_DIR = Path(__file__).parent / "fixtures" / "large_st_petersburg_pr_html"
PV_HTML_DIR = Path(__file__).parent / "fixtures" / "large_st_petersburg_pv_html"
HR_HTML_PATH = HR_HTML_DIR / "Hr.html"
HV_HTML_PATH = HV_HTML_DIR / "Hv.html"
PR_HTML_PATH = PR_HTML_DIR / "Pr.html"
PV_HTML_PATH = PV_HTML_DIR / "Pv.html"
H_INDEX_HTML_PATH = HR_HTML_DIR / "H_index.html"
P_INDEX_HTML_PATH = PR_HTML_DIR / "P_index.html"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_H_INDEX_URL = "http://kohaumotu.org/Rongorongo/H/index.html"
CITED_P_INDEX_URL = "http://kohaumotu.org/Rongorongo/P/index.html"
CITED_HR_URL = "http://kohaumotu.org/Rongorongo/H/Hr.html"
CITED_HV_URL = "http://kohaumotu.org/Rongorongo/H/Hv.html"
CITED_PR_URL = "http://kohaumotu.org/Rongorongo/P/Pr.html"
CITED_PV_URL = "http://kohaumotu.org/Rongorongo/P/Pv.html"

SIDE_HR = "Hr"
SIDE_HV = "Hv"
SIDE_PR = "Pr"
SIDE_PV = "Pv"
H_SIDES = (SIDE_HR, SIDE_HV)
P_SIDES = (SIDE_PR, SIDE_PV)
HP_SIDES = H_SIDES + P_SIDES
HP_SIDE_PAIRS = (
    (SIDE_HR, SIDE_PR),
    (SIDE_HR, SIDE_PV),
    (SIDE_HV, SIDE_PR),
    (SIDE_HV, SIDE_PV),
)

HR_LINE_NAMES = tuple(f"Hr{n}" for n in range(1, 13))
HV_LINE_NAMES = tuple(f"Hv{n}" for n in range(1, 13))
PR_LINE_NAMES = tuple(f"Pr{n}" for n in range(1, 12))
PV_LINE_NAMES = tuple(f"Pv{n}" for n in range(1, 12))
LINE_NAMES = {
    SIDE_HR: HR_LINE_NAMES,
    SIDE_HV: HV_LINE_NAMES,
    SIDE_PR: PR_LINE_NAMES,
    SIDE_PV: PV_LINE_NAMES,
}

STANDING_HR_BYTES = 10736
STANDING_HV_BYTES = 11374
STANDING_PR_BYTES = 10591
STANDING_PV_BYTES = 10219
STANDING_H_INDEX_BYTES = 4407
STANDING_P_INDEX_BYTES = 4323
STANDING_HR_STEM_COUNTS = (67, 76, 84, 82, 85, 72, 65, 63, 53, 58, 45, 21)
STANDING_HV_STEM_COUNTS = (35, 65, 63, 67, 81, 79, 75, 72, 79, 79, 69, 67)
STANDING_PR_STEM_COUNTS = (66, 78, 105, 95, 105, 82, 87, 78, 46, 45, 38)
STANDING_PV_STEM_COUNTS = (32, 41, 47, 72, 74, 76, 94, 87, 72, 79, 65)
STANDING_STEM_TOTALS = {
    SIDE_HR: 771,
    SIDE_HV: 831,
    SIDE_PR: 825,
    SIDE_PV: 739,
}
STANDING_STEM_COUNTS = {
    SIDE_HR: STANDING_HR_STEM_COUNTS,
    SIDE_HV: STANDING_HV_STEM_COUNTS,
    SIDE_PR: STANDING_PR_STEM_COUNTS,
    SIDE_PV: STANDING_PV_STEM_COUNTS,
}
STANDING_H_ALL_LINES = ("Hr.html", "Hv.html")
STANDING_P_ALL_LINES = ("Pr.html", "Pv.html")
STANDING_TABLET_H = ("H", "H/index.html", "Great Santiago")
STANDING_TABLET_P = ("P", "P/index.html", "Great St.Petersburg")
STANDING_ISLAND_HITS = {
    side: (0,) * len(LOCKED_ISLANDS) for side in HP_SIDES
}
STANDING_ANY_GK_ISLAND = False
STANDING_RESULT = "hp_grand_tradition_vendored"
STANDING_NEW_TABLET = True
STANDING_TABLET_Q_SCRAPED = False
STANDING_TABLET_D_SCRAPED = False
Q_AND_ABSENT_PAGES = (
    "Q.html",
    "Qa.html",
    "Qb.html",
    "Qr.html",
    "Qv.html",
    "Ha.html",
    "Pa.html",
) + FOURTH_TABLET_PAGES


def load_vendored_hr_html() -> str:
    """Return the vendored Kohaumotu Hr.html snapshot."""
    return HR_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_hv_html() -> str:
    """Return the vendored Kohaumotu Hv.html snapshot."""
    return HV_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_pr_html() -> str:
    """Return the vendored Kohaumotu Pr.html snapshot."""
    return PR_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_pv_html() -> str:
    """Return the vendored Kohaumotu Pv.html snapshot."""
    return PV_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_h_index_html() -> str:
    """Return the vendored Kohaumotu H/index.html snapshot."""
    return H_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_p_index_html() -> str:
    """Return the vendored Kohaumotu P/index.html snapshot."""
    return P_INDEX_HTML_PATH.read_text(encoding="utf-8")


def extract_published_tokens(html: str, prefix: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens. Does not invent numbers."""
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"{prefix}{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def side_line_stems(published: dict[str, list[str]], names: tuple[str, ...]) -> list[list[str]]:
    """One side as stem sequences. Search only."""
    return [published_stems(published[name]) for name in names]


def tablet_row(tablets_html: str, letter: str) -> tuple[str, str, str] | None:
    """Named tablet if that row has an href. Does not invent a URL."""
    for found, href, linked_name, plain_name in _TABLET_ROW.findall(tablets_html):
        _ = plain_name
        if found == letter and href:
            return (found, href, linked_name)
    return None


def load_h_p_sides() -> dict[str, list[list[str]]]:
    """Hr / Hv / Pr / Pv stems from the vendored parsers. No Q scrape."""
    return {
        SIDE_HR: side_line_stems(
            extract_published_tokens(load_vendored_hr_html(), SIDE_HR),
            HR_LINE_NAMES,
        ),
        SIDE_HV: side_line_stems(
            extract_published_tokens(load_vendored_hv_html(), SIDE_HV),
            HV_LINE_NAMES,
        ),
        SIDE_PR: side_line_stems(
            extract_published_tokens(load_vendored_pr_html(), SIDE_PR),
            PR_LINE_NAMES,
        ),
        SIDE_PV: side_line_stems(
            extract_published_tokens(load_vendored_pv_html(), SIDE_PV),
            PV_LINE_NAMES,
        ),
    }


def island_hits_by_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] = LOCKED_ISLANDS,
) -> dict[str, tuple[int, ...]]:
    """Exact G–K island hits on each H/P side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in HP_SIDES
    }


def forbidden_html_names(fixtures: Path) -> tuple[str, ...]:
    """Q / D / Ha / Pa Barthel filenames under fixtures, if any."""
    return tuple(name for name in Q_AND_ABSENT_PAGES if any(fixtures.glob(f"**/{name}")))


class TestLargeSantiagoStPetersburgVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; HrN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>060.069-162*</td></tr></table>"
            '<h3><a name="Line_12">Line 12</a></h3>'
            "<table><tr><td>001-004-064-</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_HR)
        self.assertEqual(list(published), ["Hr1", "Hr12"])
        self.assertEqual(published["Hr1"], ["060.069", "162*"])
        self.assertEqual(published["Hr12"], ["001", "004", "064"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = LOCKED_ISLANDS[0]
        by_side = {side: [[]] for side in HP_SIDES}
        by_side[SIDE_HR] = [list(gram)]
        hits = island_hits_by_side(by_side)
        self.assertEqual(hits[SIDE_HR][0], 1)
        self.assertEqual(hits[SIDE_HV], (0,) * len(LOCKED_ISLANDS))
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(forbidden_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariLargeSantiagoStPetersburgVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → H/P → Hr/Hv/Pr/Pv lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.h_index = load_vendored_h_index_html()
        self.p_index = load_vendored_p_index_html()
        self.by_side = load_h_p_sides()
        self.island_hits = island_hits_by_side(self.by_side)

    def test_parent_catalog_selects_and_vendors_h_and_p(self):
        """Catalog → tablets → H/P indexes → Hr/Hv and Pr/Pv. Not Ha, Q, or D."""
        self.assertTrue(HR_HTML_PATH.is_file())
        self.assertTrue(HV_HTML_PATH.is_file())
        self.assertTrue(PR_HTML_PATH.is_file())
        self.assertTrue(PV_HTML_PATH.is_file())
        self.assertTrue((HR_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((HV_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((PR_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((PV_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(H_INDEX_HTML_PATH.is_file())
        self.assertTrue(P_INDEX_HTML_PATH.is_file())
        self.assertFalse((HR_HTML_DIR / "Ha.html").exists())
        self.assertFalse((PR_HTML_DIR / "Pa.html").exists())
        self.assertEqual(HR_HTML_PATH.stat().st_size, STANDING_HR_BYTES)
        self.assertEqual(HV_HTML_PATH.stat().st_size, STANDING_HV_BYTES)
        self.assertEqual(PR_HTML_PATH.stat().st_size, STANDING_PR_BYTES)
        self.assertEqual(PV_HTML_PATH.stat().st_size, STANDING_PV_BYTES)
        self.assertEqual(H_INDEX_HTML_PATH.stat().st_size, STANDING_H_INDEX_BYTES)
        self.assertEqual(P_INDEX_HTML_PATH.stat().st_size, STANDING_P_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "H"), STANDING_TABLET_H)
        self.assertEqual(tablet_row(self.tablets, "P"), STANDING_TABLET_P)
        self.assertEqual(published_all_lines_hrefs(self.h_index), STANDING_H_ALL_LINES)
        self.assertEqual(published_all_lines_hrefs(self.p_index), STANDING_P_ALL_LINES)
        self.assertIn("Item H:The Great Santiago tablet", self.h_index)
        self.assertIn("Item P:The Great St. Petersburg tablet", self.p_index)
        self.assertIn('href="Hr.html"', self.h_index)
        self.assertIn('href="Hv.html"', self.h_index)
        self.assertIn('href="Pr.html"', self.p_index)
        self.assertIn('href="Pv.html"', self.p_index)
        self.assertNotIn('href="Ha.html"', self.h_index)
        self.assertNotIn('href="Pa.html"', self.p_index)
        hr = load_vendored_hr_html()
        hv = load_vendored_hv_html()
        pr = load_vendored_pr_html()
        pv = load_vendored_pv_html()
        self.assertIn("Item H:The Great Santiago Tablet", hr)
        self.assertIn("Item H:The Great Santiago Tablet", hv)
        self.assertIn("Item P:The Great St. Petersburg Tablet", pr)
        self.assertIn("Item P:The Great St. Petersburg Tablet", pv)
        self.assertIn("Rongorongo Hr", hr)
        self.assertIn("Rongorongo Hv", hv)
        self.assertIn("Rongorongo Pr", pr)
        self.assertIn("Rongorongo Pv", pv)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(forbidden_html_names(fixtures), ())
        self.assertEqual(fourth_tablet_html_names(fixtures), ())
        self.assertFalse(STANDING_TABLET_Q_SCRAPED)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        for directory, urls in (
            (HR_HTML_DIR, (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_H_INDEX_URL, CITED_HR_URL)),
            (HV_HTML_DIR, (CITED_HV_URL, CITED_H_INDEX_URL)),
            (PR_HTML_DIR, (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_P_INDEX_URL, CITED_PR_URL)),
            (PV_HTML_DIR, (CITED_PV_URL, CITED_P_INDEX_URL)),
        ):
            text = (directory / "ATTRIBUTION").read_text(encoding="utf-8")
            for url in urls:
                self.assertIn(url, text)
            self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
            self.assertIn("tablet Q", text)
            self.assertIn("tablet D", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_gk_islands_absent(self):
        """Per-side stem totals; six G–K islands are 0 on every H/P side."""
        for side in HP_SIDES:
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

    def test_existing_gk_island_off_scoreboard_still_computes(self):
        """Cycle 68 six-island off-G/K table stays."""
        prior = TestMamariSmallSantiagoLondonIslandOffGkScoreboard()
        prior.setUp()
        prior.test_six_by_eight_hit_table()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-69 H/P vendor lock."""
        lock = self.survey["tablet_h_p_grand_tradition_vendor"]
        self.assertEqual(lock["cycle"], 69)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_h"], "H")
        self.assertEqual(lock["tablet_p"], "P")
        self.assertEqual(lock["name_h"], "Great Santiago")
        self.assertEqual(lock["name_p"], "Great St. Petersburg")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["h_index"], CITED_H_INDEX_URL)
        self.assertEqual(lock["p_index"], CITED_P_INDEX_URL)
        self.assertEqual(tuple(lock["h_pages"]), STANDING_H_ALL_LINES)
        self.assertEqual(tuple(lock["p_pages"]), STANDING_P_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Hr"], STANDING_HR_BYTES)
        self.assertEqual(lock["html_bytes"]["Hv"], STANDING_HV_BYTES)
        self.assertEqual(lock["html_bytes"]["Pr"], STANDING_PR_BYTES)
        self.assertEqual(lock["html_bytes"]["Pv"], STANDING_PV_BYTES)
        self.assertEqual(lock["stem_totals"]["Hr"], STANDING_STEM_TOTALS[SIDE_HR])
        self.assertEqual(lock["stem_totals"]["Hv"], STANDING_STEM_TOTALS[SIDE_HV])
        self.assertEqual(lock["stem_totals"]["Pr"], STANDING_STEM_TOTALS[SIDE_PR])
        self.assertEqual(lock["stem_totals"]["Pv"], STANDING_STEM_TOTALS[SIDE_PV])
        self.assertEqual(tuple(lock["stem_counts"]["Hr"]), STANDING_HR_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Hv"]), STANDING_HV_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Pr"]), STANDING_PR_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Pv"]), STANDING_PV_STEM_COUNTS)
        locked_hits = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        self.assertEqual(locked_hits, STANDING_ISLAND_HITS)
        self.assertFalse(lock["any_gk_island"])
        self.assertTrue(lock["new_tablet"])
        self.assertFalse(lock["tablet_q_scraped"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_island_off_gk_hits"]["cycle"], 68)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariLargeSantiagoStPetersburgVendorImageSnapshot(unittest.TestCase):
    """Cycle 69 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
