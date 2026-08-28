"""Santiago Staff verso Ib: Kohaumotu Ib.html absence lock.

Cycle 53 text-search lock. Same already-vendored Kohaumotu I/
source used for Ia. Ib.html is not a published page. I/index.html
is the documented verso check (A lists Ab.html; B lists Bv.html;
I lists Ia.html only). No invented Barthel. No G00n→Barthel map.
No type merge. No detector retune. No CV. No new agents.

If Ib.html is absent, lock that absence and stop. Do not scrape
tablet D. Do not invent stem counts, 076 rates, or 090 076 /
076 071 / 090 076 071 hits. Motifs and the Ia 5-gram top are
not searched on a missing page.

Search lock, not a merge and not a translation. MockProvider only.
"""

import re
import unittest
from dataclasses import dataclass
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_br_scoreboard import (
    B_INDEX_HTML_PATH,
    load_vendored_b_index_html,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    TestMamariSantiagoIa090076071NgramScoreboard,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    IA_HTML_DIR,
    IA_HTML_PATH,
    I_INDEX_HTML_PATH,
    STANDING_FALLBACK_NON_ABC,
    STANDING_I_INDEX_BYTES,
    STANDING_IR_HTML,
    load_vendored_i_index_html,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_tahua_aa_scoreboard import (
    A_INDEX_HTML_PATH,
    load_vendored_a_index_html,
)

IB_HTML_DIR = Path(__file__).parent / "fixtures" / "santiago_ib_html"
IB_HTML_PATH = IB_HTML_DIR / "Ib.html"
IB_INDEX_HTML_PATH = IB_HTML_DIR / "I_index.html"
CITED_IB_URL = "http://kohaumotu.org/Rongorongo/I/Ib.html"
CITED_I_INDEX_URL = "http://kohaumotu.org/Rongorongo/I/index.html"

ALL_LINES_HREF = re.compile(r'href="([A-Z][abrv]\.html)"')
# Unpublished D pages (cycle 54 Gr vs Ga lesson). HEAD-check 2026-08-28:
# Dr.html / Dv.html / D.html 404. Da.html / Db.html are the published
# sides and are vendored in cycle 79.
FOURTH_TABLET_PAGES = ("D.html", "Dr.html", "Dv.html")

STANDING_A_ALL_LINES = ("Aa.html", "Ab.html")
STANDING_B_ALL_LINES = ("Br.html", "Bv.html")
STANDING_I_ALL_LINES = ("Ia.html",)
STANDING_IB_HTML = False
STANDING_DOCUMENTED_VERSO = None
STANDING_RESULT = "ib_html_absent"
STANDING_NEW_TABLET = False
STANDING_TABLET_D_SCRAPED = False


@dataclass(frozen=True)
class IbAbsenceLock:
    """Ib.html search result. Counts stay None when the page is absent."""

    ib_html: bool
    documented_verso: str | None
    result: str
    stem_count: int | None
    stem_076_hits: int | None
    stem_076_rate: float | None
    hits_090_076: int | None
    hits_076_071: int | None
    hits_090_076_071: int | None
    motif_a: bool | None
    motif_b: bool | None
    motif_c: bool | None
    ia_5gram_top: bool | None


def published_all_lines_hrefs(html: str) -> tuple[str, ...]:
    """Unique Xa/Xb/Xr/Xv.html hrefs in document order. Search only."""
    seen: list[str] = []
    for href in ALL_LINES_HREF.findall(html):
        if href not in seen:
            seen.append(href)
    return tuple(seen)


def verso_all_lines_href(sides: tuple[str, ...], recto: str) -> str | None:
    """Second all-lines page after recto, or None if unpublished."""
    others = tuple(href for href in sides if href != recto)
    if recto not in sides or not others:
        return None
    return others[0]


def score_ib_absence(
    ib_exists: bool,
    documented_verso: str | None = None,
) -> IbAbsenceLock:
    """Lock absence and stop. Do not invent Ib stems."""
    if ib_exists:
        raise AssertionError("Ib.html is unpublished; do not invent stems")
    return IbAbsenceLock(
        ib_html=False,
        documented_verso=documented_verso,
        result=STANDING_RESULT,
        stem_count=None,
        stem_076_hits=None,
        stem_076_rate=None,
        hits_090_076=None,
        hits_076_071=None,
        hits_090_076_071=None,
        motif_a=None,
        motif_b=None,
        motif_c=None,
        ia_5gram_top=None,
    )


def fourth_tablet_html_names(fixtures: Path) -> tuple[str, ...]:
    """D-side Barthel filenames under fixtures, if any were vendored."""
    return tuple(
        name
        for name in FOURTH_TABLET_PAGES
        if any(fixtures.glob(f"**/{name}"))
    )


class TestSantiagoIbHelpers(unittest.TestCase):
    """Helpers on synthetic indexes. No CV, no LLM."""

    def test_all_lines_hrefs_and_verso_or_none(self):
        """A/B expose a second side; I with only Ia.html has no verso."""
        provider = MockProvider()
        a = published_all_lines_hrefs(
            '<li><a href="Aa.html">a</a></li>'
            '<li><a href="ba_Aa.html">skip</a></li>'
            '<li><a href="Ab.html">b</a></li>'
            '<li><a href="Aa.html">dup</a></li>'
        )
        b = published_all_lines_hrefs(
            '<li><a href="Br.html">r</a></li><li><a href="Bv.html">v</a></li>'
        )
        i = published_all_lines_hrefs(
            '<li><a href="Ia.html">all</a></li>'
            '<li><a href="ba_Ia.html">order</a></li>'
            '<li><a href="comp_Ia.html">cmp</a></li>'
        )
        self.assertEqual(a, STANDING_A_ALL_LINES)
        self.assertEqual(b, STANDING_B_ALL_LINES)
        self.assertEqual(i, STANDING_I_ALL_LINES)
        self.assertEqual(verso_all_lines_href(a, "Aa.html"), "Ab.html")
        self.assertEqual(verso_all_lines_href(b, "Br.html"), "Bv.html")
        self.assertIsNone(verso_all_lines_href(i, "Ia.html"))
        self.assertEqual(verso_all_lines_href(i, "Ia.html"), STANDING_DOCUMENTED_VERSO)
        self.assertEqual(provider.get_call_history(), [])

    def test_absence_lock_stops_without_inventing_counts(self):
        """Missing Ib.html yields None counts. A present page is refused."""
        provider = MockProvider()
        lock = score_ib_absence(False)
        self.assertFalse(lock.ib_html)
        self.assertEqual(lock.result, STANDING_RESULT)
        self.assertIsNone(lock.stem_count)
        self.assertIsNone(lock.stem_076_hits)
        self.assertIsNone(lock.stem_076_rate)
        self.assertIsNone(lock.hits_090_076)
        self.assertIsNone(lock.hits_076_071)
        self.assertIsNone(lock.hits_090_076_071)
        self.assertIsNone(lock.motif_a)
        self.assertIsNone(lock.motif_b)
        self.assertIsNone(lock.motif_c)
        self.assertIsNone(lock.ia_5gram_top)
        with self.assertRaises(AssertionError):
            score_ib_absence(True)
        self.assertEqual(fourth_tablet_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIbScoreboard(unittest.TestCase):
    """Cited I/index.html Ib.html absence lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_index = load_vendored_i_index_html()
        self.ib_index = IB_INDEX_HTML_PATH.read_text(encoding="utf-8")
        self.a_index = load_vendored_a_index_html()
        self.b_index = load_vendored_b_index_html()
        self.i_sides = published_all_lines_hrefs(self.i_index)
        self.lock = score_ib_absence(
            IB_HTML_PATH.exists(),
            verso_all_lines_href(self.i_sides, "Ia.html"),
        )

    def test_ib_html_is_absent_on_the_documented_i_source(self):
        """I/index lists Ia.html only. No Ib.html file. No tablet D."""
        self.assertTrue(IB_INDEX_HTML_PATH.is_file())
        self.assertTrue((IB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertFalse(IB_HTML_PATH.exists())
        self.assertFalse((IA_HTML_DIR / "Ib.html").exists())
        self.assertTrue(I_INDEX_HTML_PATH.is_file())
        self.assertTrue(IA_HTML_PATH.is_file())
        self.assertEqual(IB_INDEX_HTML_PATH.stat().st_size, STANDING_I_INDEX_BYTES)
        self.assertEqual(self.ib_index, self.i_index)
        self.assertEqual(self.i_sides, STANDING_I_ALL_LINES)
        self.assertEqual(
            published_all_lines_hrefs(self.a_index),
            STANDING_A_ALL_LINES,
        )
        self.assertEqual(
            published_all_lines_hrefs(self.b_index),
            STANDING_B_ALL_LINES,
        )
        self.assertEqual(verso_all_lines_href(self.i_sides, "Ia.html"), STANDING_DOCUMENTED_VERSO)
        self.assertIsNone(STANDING_DOCUMENTED_VERSO)
        self.assertEqual(STANDING_IB_HTML, False)
        self.assertEqual(STANDING_IR_HTML, False)
        self.assertIn("cylindrical", self.i_index)
        self.assertNotIn("Ib.html", self.i_index)
        self.assertNotIn("Ib.html", self.ib_index)
        attribution = (IB_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_I_INDEX_URL, attribution)
        self.assertIn(CITED_IB_URL, attribution)
        self.assertIn("not a published page", attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        self.assertIn("tablet D", attribution)
        self.assertEqual(STANDING_FALLBACK_NON_ABC[0], "D")
        self.assertEqual(
            fourth_tablet_html_names(Path(__file__).parent / "fixtures"),
            (),
        )
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertFalse(A_INDEX_HTML_PATH.name.startswith("D"))
        self.assertFalse(B_INDEX_HTML_PATH.name.startswith("D"))
        self.assertEqual(self.lock, score_ib_absence(False))
        self.assertFalse(self.lock.ib_html)
        self.assertEqual(self.lock.result, STANDING_RESULT)
        self.assertIsNone(self.lock.stem_count)
        self.assertIsNone(self.lock.stem_076_rate)
        self.assertIsNone(self.lock.hits_090_076_071)
        self.assertIsNone(self.lock.ia_5gram_top)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_090_076_071_and_scoreboards_still_compute(self):
        """Cycle 52 3×8 n-gram table and A/B/C/Ia scoreboards stay."""
        prior = TestMamariSantiagoIa090076071NgramScoreboard()
        prior.setUp()
        prior.test_three_by_eight_hit_table()
        prior.test_existing_090_071_rate_and_scoreboards_still_compute()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-53 Ib.html absence."""
        lock = self.survey["santiago_staff_verso_ib"]
        self.assertEqual(lock["cycle"], 53)
        self.assertEqual(lock["passage"], "tablet_i_santiago_staff")
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertFalse(lock["ib_html"])
        self.assertIsNone(lock["documented_verso_page"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertIsNone(lock["stem_count"])
        self.assertIsNone(lock["stem_076_hits"])
        self.assertIsNone(lock["stem_076_rate"])
        self.assertIsNone(lock["stem_076_rate_ge_0_10"])
        self.assertIsNone(lock["hits_090_076"])
        self.assertIsNone(lock["hits_076_071"])
        self.assertIsNone(lock["hits_090_076_071"])
        self.assertIsNone(lock["motif_9gram"])
        self.assertIsNone(lock["motif_10gram"])
        self.assertIsNone(lock["motif_ab_9gram"])
        self.assertIsNone(lock["motif_bv_8gram"])
        self.assertIsNone(lock["ia_5gram_top"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_ia_999_locks_unchanged"])
        self.assertTrue(lock["standing_ia_076_locks_unchanged"])
        self.assertTrue(lock["standing_ia_076_cells_unchanged"])
        self.assertTrue(lock["standing_ia_076_rate_unchanged"])
        self.assertTrue(lock["standing_ia_090_071_rate_unchanged"])
        self.assertTrue(lock["standing_ia_090_076_071_ngram_unchanged"])
        self.assertEqual(self.survey["stem_090_076_071_ngram_per_fixture"]["cycle"], 52)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIbImageSnapshot(unittest.TestCase):
    """Cycle 53 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
