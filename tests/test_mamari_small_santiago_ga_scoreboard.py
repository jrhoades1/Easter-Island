"""Small Santiago recto Ga: Kohaumotu Ga.html absence lock.

Cycle 54 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / I. Preferred tablet this cycle is G.
Ga.html is not a published page. G/index.html is the documented
recto check (A lists Aa.html; B lists Br.html; G lists Gr.html).
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents.

If Ga.html is absent, lock that absence and stop. Do not scrape
Gr.html as a substitute. Do not scrape tablet K or tablet D. Do
not invent stem counts, 076 rates, or 090 076 / 076 071 /
090 076 071 hits. Motifs and the Ia 5-gram top are not searched
on a missing page.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_br_scoreboard import (
    B_INDEX_HTML_PATH,
    load_vendored_b_index_html,
)
from tests.test_mamari_santiago_ib_scoreboard import (
    FOURTH_TABLET_PAGES,
    STANDING_A_ALL_LINES,
    STANDING_B_ALL_LINES,
    STANDING_I_ALL_LINES,
    TestMamariSantiagoIbScoreboard,
    fourth_tablet_html_names,
    published_all_lines_hrefs,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_tahua_aa_scoreboard import (
    A_INDEX_HTML_PATH,
    _TABLET_ROW,
    load_vendored_a_index_html,
    load_vendored_tablets_html,
)

GA_HTML_DIR = Path(__file__).parent / "fixtures" / "small_santiago_ga_html"
GA_HTML_PATH = GA_HTML_DIR / "Ga.html"
G_INDEX_HTML_PATH = GA_HTML_DIR / "G_index.html"
CITED_GA_URL = "http://kohaumotu.org/Rongorongo/G/Ga.html"
CITED_G_INDEX_URL = "http://kohaumotu.org/Rongorongo/G/index.html"

G_BARTHEL_PAGES = ("Ga.html", "Gb.html", "Gr.html", "Gv.html")
K_BARTHEL_PAGES = ("K.html", "Ka.html", "Kb.html", "Kr.html", "Kv.html")

STANDING_G_ALL_LINES = ("Gr.html", "Gv.html")
STANDING_GA_HTML = False
STANDING_DOCUMENTED_RECTO = "Gr.html"
STANDING_GR_HTML_VENDORED = False
STANDING_RESULT = "ga_html_absent"
STANDING_NEW_TABLET = False
STANDING_TABLET_D_SCRAPED = False
STANDING_TABLET_K_SCRAPED = False
STANDING_TABLET_G = ("G", "G/index.html", "Small Santiago")
STANDING_G_INDEX_BYTES = 4041


@dataclass(frozen=True)
class GaAbsenceLock:
    """Ga.html search result. Counts stay None when the page is absent."""

    ga_html: bool
    documented_recto: str | None
    documented_all_lines: tuple[str, ...]
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


def load_vendored_g_index_html() -> str:
    """Return the vendored Kohaumotu G/index.html snapshot."""
    return G_INDEX_HTML_PATH.read_text(encoding="utf-8")


def tablet_g_row(tablets_html: str) -> tuple[str, str, str] | None:
    """G if that row has an href. Does not invent a URL."""
    for letter, href, linked_name, plain_name in _TABLET_ROW.findall(tablets_html):
        _ = plain_name
        if letter == "G" and href:
            return (letter, href, linked_name)
    return None


def recto_all_lines_href(sides: tuple[str, ...]) -> str | None:
    """First published all-lines page, or None if the index lists none."""
    return sides[0] if sides else None


def score_ga_absence(
    ga_exists: bool,
    documented_recto: str | None = None,
    documented_all_lines: tuple[str, ...] = (),
) -> GaAbsenceLock:
    """Lock absence and stop. Do not invent Ga stems."""
    if ga_exists:
        raise AssertionError("Ga.html is unpublished; do not invent stems")
    return GaAbsenceLock(
        ga_html=False,
        documented_recto=documented_recto,
        documented_all_lines=documented_all_lines,
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


def substitute_barthel_pages(fixtures: Path) -> tuple[str, ...]:
    """G-side or K-side Barthel filenames under fixtures, if any were vendored."""
    names = G_BARTHEL_PAGES + K_BARTHEL_PAGES
    return tuple(name for name in names if any(fixtures.glob(f"**/{name}")))


class TestSmallSantiagoGaHelpers(unittest.TestCase):
    """Helpers on synthetic indexes. No CV, no LLM."""

    def test_all_lines_hrefs_and_ga_or_none(self):
        """A/B expose an a/r page; G lists Gr.html, not Ga.html."""
        provider = MockProvider()
        a = published_all_lines_hrefs(
            '<li><a href="Aa.html">a</a></li>'
            '<li><a href="ba_Aa.html">skip</a></li>'
            '<li><a href="Ab.html">b</a></li>'
        )
        b = published_all_lines_hrefs(
            '<li><a href="Br.html">r</a></li><li><a href="Bv.html">v</a></li>'
        )
        g = published_all_lines_hrefs(
            '<li><a href="Gr.html">recto</a></li>'
            '<li><a href="fi_Gr.html">skip</a></li>'
            '<li><a href="Gv.html">verso</a></li>'
            '<li><a href="Gr.html">dup</a></li>'
        )
        self.assertEqual(a, STANDING_A_ALL_LINES)
        self.assertEqual(b, STANDING_B_ALL_LINES)
        self.assertEqual(g, STANDING_G_ALL_LINES)
        self.assertNotIn("Ga.html", g)
        self.assertEqual(recto_all_lines_href(a), "Aa.html")
        self.assertEqual(recto_all_lines_href(b), "Br.html")
        self.assertEqual(recto_all_lines_href(g), STANDING_DOCUMENTED_RECTO)
        self.assertNotEqual(recto_all_lines_href(g), "Ga.html")
        self.assertEqual(provider.get_call_history(), [])

    def test_absence_lock_stops_without_inventing_counts(self):
        """Missing Ga.html yields None counts. A present page is refused."""
        provider = MockProvider()
        lock = score_ga_absence(False, STANDING_DOCUMENTED_RECTO, STANDING_G_ALL_LINES)
        self.assertFalse(lock.ga_html)
        self.assertEqual(lock.result, STANDING_RESULT)
        self.assertEqual(lock.documented_recto, STANDING_DOCUMENTED_RECTO)
        self.assertEqual(lock.documented_all_lines, STANDING_G_ALL_LINES)
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
            score_ga_absence(True)
        self.assertEqual(substitute_barthel_pages(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])

    def test_tablets_row_selects_small_santiago(self):
        """G wins when linked; a missing G row is None."""
        html = (
            "<table>"
            '<tr><td>C</td><td><a href="C/index.html">Mamari</a></td></tr>'
            '<tr><td>G</td><td><a href="G/index.html">Small Santiago</a></td></tr>'
            "</table>"
        )
        self.assertEqual(tablet_g_row(html), STANDING_TABLET_G)
        self.assertIsNone(tablet_g_row(html.replace("G/index.html", "")))
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoGaScoreboard(unittest.TestCase):
    """Cited tablets.html → G → Ga.html absence lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.g_index = load_vendored_g_index_html()
        self.a_index = load_vendored_a_index_html()
        self.b_index = load_vendored_b_index_html()
        self.g_sides = published_all_lines_hrefs(self.g_index)
        self.lock = score_ga_absence(
            GA_HTML_PATH.exists(),
            recto_all_lines_href(self.g_sides),
            self.g_sides,
        )

    def test_ga_html_is_absent_on_the_documented_g_source(self):
        """G/index lists Gr.html + Gv.html. No Ga.html. Cycle 54 dir has no Gr."""
        self.assertTrue(G_INDEX_HTML_PATH.is_file())
        self.assertTrue((GA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertFalse(GA_HTML_PATH.exists())
        self.assertEqual(G_INDEX_HTML_PATH.stat().st_size, STANDING_G_INDEX_BYTES)
        self.assertEqual(tablet_g_row(self.tablets), STANDING_TABLET_G)
        self.assertIn("Item G:The Small Santiago tablet", self.g_index)
        self.assertIn('href="Gr.html"', self.g_index)
        self.assertIn('href="Gv.html"', self.g_index)
        self.assertNotIn("Ga.html", self.g_index)
        self.assertEqual(self.g_sides, STANDING_G_ALL_LINES)
        self.assertEqual(
            published_all_lines_hrefs(self.a_index),
            STANDING_A_ALL_LINES,
        )
        self.assertEqual(
            published_all_lines_hrefs(self.b_index),
            STANDING_B_ALL_LINES,
        )
        self.assertEqual(STANDING_I_ALL_LINES, ("Ia.html",))
        self.assertEqual(recto_all_lines_href(self.g_sides), STANDING_DOCUMENTED_RECTO)
        self.assertEqual(STANDING_DOCUMENTED_RECTO, "Gr.html")
        self.assertEqual(STANDING_GA_HTML, False)
        self.assertFalse(STANDING_GR_HTML_VENDORED)
        attribution = (GA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_G_INDEX_URL, attribution)
        self.assertIn(CITED_GA_URL, attribution)
        self.assertIn("not a published page", attribution)
        self.assertIn("do not scrape Gr.html", attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        self.assertIn("tablet K", attribution)
        self.assertIn("tablet D", attribution)
        self.assertEqual(substitute_barthel_pages(GA_HTML_DIR), ())
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(fourth_tablet_html_names(fixtures), ())
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertFalse(STANDING_TABLET_K_SCRAPED)
        self.assertEqual(self.lock, score_ga_absence(False, "Gr.html", STANDING_G_ALL_LINES))
        self.assertFalse(self.lock.ga_html)
        self.assertEqual(self.lock.result, STANDING_RESULT)
        self.assertIsNone(self.lock.stem_count)
        self.assertIsNone(self.lock.stem_076_rate)
        self.assertIsNone(self.lock.hits_090_076_071)
        self.assertIsNone(self.lock.ia_5gram_top)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_ib_and_090_076_071_scoreboards_still_compute(self):
        """Cycle 53 Ib absence and Cycle 52 3×8 n-gram table stay."""
        prior = TestMamariSantiagoIbScoreboard()
        prior.setUp()
        prior.test_ib_html_is_absent_on_the_documented_i_source()
        prior.test_existing_090_076_071_and_scoreboards_still_compute()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-54 Ga.html absence."""
        lock = self.survey["tablet_g_small_santiago_recto"]
        self.assertEqual(lock["cycle"], 54)
        self.assertEqual(lock["tablet"], "G")
        self.assertEqual(lock["name"], "Small Santiago")
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertFalse(lock["ga_html"])
        self.assertEqual(lock["documented_recto_page"], STANDING_DOCUMENTED_RECTO)
        self.assertEqual(lock["documented_all_lines"], list(STANDING_G_ALL_LINES))
        self.assertFalse(lock["gr_html_vendored"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertFalse(lock["tablet_k_scraped"])
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
        self.assertTrue(lock["standing_ib_locks_unchanged"])
        self.assertEqual(self.survey["santiago_staff_verso_ib"]["cycle"], 53)
        self.assertEqual(self.survey["stem_090_076_071_ngram_per_fixture"]["cycle"], 52)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(FOURTH_TABLET_PAGES[0], "D.html")
        self.assertFalse(A_INDEX_HTML_PATH.name.startswith("D"))
        self.assertFalse(B_INDEX_HTML_PATH.name.startswith("K"))
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoGaImageSnapshot(unittest.TestCase):
    """Cycle 54 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
