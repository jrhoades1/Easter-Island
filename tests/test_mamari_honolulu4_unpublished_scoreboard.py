"""Honolulu 4 (W) unpublished / photos-only lock.

Cycle 100 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A–V. HEAD-check before filename assume (cycle
54 Gr vs Ga; cycle 79 Da vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs
Fa; cycle 86 Jb vs Ja; cycle 87 Lb vs La; cycle 88 Mb vs Ma; cycle
89 Nr vs Na; cycle 92 Ob vs Oa; cycle 93 Rr vs Ra; cycle 94 Sr vs
Sa; cycle 96 Tb vs Ta; cycle 97 Ub vs Ua; cycle 98 Vb vs Va):
Wb.html / Wr.html / Wv.html / W/tablets.html are unpublished 404s.
Wa.html and W.html are 200 photos-only (no Barthel). W/index.html
names Wa.html as Barthel/Bishop Museum. Catalog name is Honolulu 4
[#445] — not Honolulu 1 / Honolulu 2 / Honolulu 3 / Washington /
Vienna / London / Reimiro / Boomerang / Atua-Mata-Riri. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. No second new letter (X).

Locks the negative: W is named in tablets.html; Kohaumotu publishes
no Barthel codes. Stem counts, island hits, and W's longest n stay
None. Do not invent a tablet. Cycle 99 A–V inventory stays. Claim
that can lose: w_unpublished.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    TestMamariHonolulu3VendorScoreboard,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    extract_published_tokens,
    side_line_stems,
    tablet_row,
)
from tests.test_mamari_santiago_ib_scoreboard import (
    published_all_lines_hrefs,
)
from tests.test_mamari_second_passage_scoreboard import (
    load_corpus_survey,
    published_stems,
)
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html

W_HTML_DIR = Path(__file__).parent / "fixtures" / "honolulu_w_html"
WA_HTML_PATH = W_HTML_DIR / "Wa.html"
W_ITEM_HTML_PATH = W_HTML_DIR / "W.html"
W_INDEX_HTML_PATH = W_HTML_DIR / "W_index.html"
WA_JSON_PATH = W_HTML_DIR / "Wa_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_W_INDEX_URL = "http://kohaumotu.org/Rongorongo/W/index.html"
CITED_WA_URL = "http://kohaumotu.org/Rongorongo/W/Wa.html"
CITED_W_ITEM_URL = "http://kohaumotu.org/Rongorongo/W/W.html"

SIDE_WA = "Wa"
WA_LINE_NAMES = tuple(f"Wa{n}" for n in range(1, 5))

STANDING_WA_BYTES = 1379
STANDING_W_ITEM_BYTES = 1313
STANDING_W_INDEX_BYTES = 3097
STANDING_W_ALL_LINES = ("Wa.html",)
STANDING_TABLET_W = ("W", "W/index.html", "Honolulu 4 [#445]")
STANDING_HEAD = {
    "W/index.html": 200,
    "Wa.html": 200,
    "Wb.html": 404,
    "Wr.html": 404,
    "Wv.html": 404,
    "W.html": 200,
    "W/tablets.html": 404,
}
STANDING_WA_HTML = False
STANDING_WA_HTML_HEAD = 200
STANDING_WA_HTML_KIND = "photos_only"
STANDING_WB_HTML = False
STANDING_WR_HTML = False
STANDING_WV_HTML = False
STANDING_W_HTML = False
STANDING_W_HTML_HEAD = 200
STANDING_W_HTML_KIND = "photos_only"
STANDING_WA_PUBLISHED_CELLS = ("(10-30)!", "_", "_", "_*")
STANDING_CLAIM = "w_unpublished"
STANDING_RESULT = "w_honolulu_unpublished"
STANDING_NEW_TABLET = False
STANDING_NEXT_CATALOG = "X"
STANDING_CATALOG_X = ("X", "X/index.html", "Tangata Manu")
UNPUBLISHED_W_PAGES = ("Wb.html", "Wr.html", "Wv.html")


@dataclass(frozen=True)
class WUnpublishedLock:
    """W search result. Counts stay None when Barthel is unpublished."""

    w_barthel: bool
    wa_html: bool
    w_html: bool
    result: str
    stem_count: int | None
    longest_n: int | None
    gk_hits: tuple[int, ...] | None
    hpq_hits: tuple[int, ...] | None
    e_n9_hits: int | None
    er7_4_hits: int | None
    m_n4_hits: int | None
    n_n6_hits: int | None
    s_n7_hits: int | None
    v_n4_hits: int | None


def load_vendored_wa_html() -> str:
    """Return the vendored Kohaumotu Wa.html snapshot (photos-only)."""
    return WA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_w_item_html() -> str:
    """Return the vendored Kohaumotu W.html snapshot (photos-only)."""
    return W_ITEM_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_w_index_html() -> str:
    """Return the vendored Kohaumotu W/index.html snapshot."""
    return W_INDEX_HTML_PATH.read_text(encoding="utf-8")


def has_real_barthel_codes(html: str, prefix: str = SIDE_WA) -> bool:
    """True iff the shared parser yields a 3-digit Barthel stem."""
    published = extract_published_tokens(html, prefix)
    return any(published_stems(tokens) for tokens in published.values())


def unpublished_w_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished W Barthel filenames under fixtures, if any."""
    return tuple(
        name for name in UNPUBLISHED_W_PAGES if any(fixtures.glob(f"**/{name}"))
    )


def score_w_unpublished(has_barthel: bool) -> WUnpublishedLock:
    """Lock absence and stop. Do not invent W stems or island hits."""
    if has_barthel:
        raise AssertionError("W has no published Barthel; do not invent stems")
    return WUnpublishedLock(
        w_barthel=False,
        wa_html=False,
        w_html=False,
        result=STANDING_RESULT,
        stem_count=None,
        longest_n=None,
        gk_hits=None,
        hpq_hits=None,
        e_n9_hits=None,
        er7_4_hits=None,
        m_n4_hits=None,
        n_n6_hits=None,
        s_n7_hits=None,
        v_n4_hits=None,
    )


class TestHonolulu4UnpublishedHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_photos_only_cells_are_not_barthel(self):
        """(10-30)! / _ / _* yield no stems; a planted 051-200 does."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td>no image</td></tr>"
            "<tr><td>(10-30)!</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>_</td></tr></table>"
            '<h3><a name="Line_3">Line 3</a></h3>'
            "<table><tr><td>_</td></tr></table>"
            '<h3><a name="Line_4">Line 4</a></h3>'
            "<table><tr><td>_*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_WA)
        self.assertEqual(list(published), ["Wa1", "Wa2", "Wa3", "Wa4"])
        self.assertEqual(published["Wa1"], ["(10", "30)!"])
        self.assertEqual(published["Wa2"], [])
        self.assertEqual(published["Wa3"], [])
        self.assertEqual(published["Wa4"], [])
        stems = side_line_stems(published, WA_LINE_NAMES)
        self.assertEqual(stems, [[], [], [], []])
        self.assertFalse(has_real_barthel_codes(html))
        planted = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td>051-200.200.011</td></tr></table>"
        )
        self.assertTrue(has_real_barthel_codes(planted))
        self.assertEqual(unpublished_w_html_names(Path("/no/such/fixtures")), ())
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_absence_lock_stops_without_inventing_counts(self):
        """Missing Barthel yields None counts. A present page is refused."""
        provider = MockProvider()
        lock = score_w_unpublished(False)
        self.assertFalse(lock.w_barthel)
        self.assertEqual(lock.result, STANDING_RESULT)
        self.assertIsNone(lock.stem_count)
        self.assertIsNone(lock.longest_n)
        self.assertIsNone(lock.gk_hits)
        self.assertIsNone(lock.v_n4_hits)
        with self.assertRaises(AssertionError):
            score_w_unpublished(True)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHonolulu4UnpublishedScoreboard(unittest.TestCase):
    """Cited tablets.html → W → photos-only lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.w_index = load_vendored_w_index_html()
        self.wa = load_vendored_wa_html()
        self.w_item = load_vendored_w_item_html()
        self.lock = score_w_unpublished(has_real_barthel_codes(self.wa))

    def test_parent_catalog_names_w_without_barthel(self):
        """Catalog → tablets → W index → Wa/W.html photos-only. Not Wb/Wr/Wv."""
        self.assertTrue(W_INDEX_HTML_PATH.is_file())
        self.assertTrue(WA_HTML_PATH.is_file())
        self.assertTrue(W_ITEM_HTML_PATH.is_file())
        self.assertTrue((W_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertFalse(WA_JSON_PATH.exists())
        self.assertFalse((W_HTML_DIR / "Wb.html").exists())
        self.assertFalse((W_HTML_DIR / "Wr.html").exists())
        self.assertFalse((W_HTML_DIR / "Wv.html").exists())
        self.assertEqual(STANDING_WA_HTML, False)
        self.assertEqual(STANDING_WB_HTML, False)
        self.assertEqual(STANDING_WR_HTML, False)
        self.assertEqual(STANDING_WV_HTML, False)
        self.assertEqual(STANDING_W_HTML, False)
        self.assertEqual(STANDING_WA_HTML_HEAD, 200)
        self.assertEqual(STANDING_W_HTML_HEAD, 200)
        self.assertEqual(STANDING_WA_HTML_KIND, "photos_only")
        self.assertEqual(STANDING_W_HTML_KIND, "photos_only")
        self.assertEqual(STANDING_HEAD["W/index.html"], 200)
        self.assertEqual(STANDING_HEAD["Wa.html"], 200)
        self.assertEqual(STANDING_HEAD["W.html"], 200)
        self.assertEqual(STANDING_HEAD["Wb.html"], 404)
        self.assertEqual(STANDING_HEAD["Wr.html"], 404)
        self.assertEqual(STANDING_HEAD["Wv.html"], 404)
        self.assertEqual(STANDING_HEAD["W/tablets.html"], 404)
        self.assertEqual(WA_HTML_PATH.stat().st_size, STANDING_WA_BYTES)
        self.assertEqual(W_ITEM_HTML_PATH.stat().st_size, STANDING_W_ITEM_BYTES)
        self.assertEqual(W_INDEX_HTML_PATH.stat().st_size, STANDING_W_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "W"), STANDING_TABLET_W)
        self.assertEqual(published_all_lines_hrefs(self.w_index), STANDING_W_ALL_LINES)
        self.assertIn("Item W:Honolulu 4 [#445]", self.w_index)
        self.assertIn("Barthel” tracings are in fact drawings", self.w_index)
        self.assertIn('href="Wa.html"', self.w_index)
        self.assertIn('href="W.html"', self.w_index)
        self.assertNotIn('href="Wb.html"', self.w_index)
        self.assertNotIn('href="Wr.html"', self.w_index)
        self.assertNotIn('href="Wv.html"', self.w_index)
        self.assertIn("Item W:Honolulu 4 [#445]", self.wa)
        self.assertIn("Rongorongo W", self.wa)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', self.wa)
        self.assertIn('<h3><a name="Line_4">Line 4</a></h3>', self.wa)
        self.assertIn("(10-30)!", self.wa)
        self.assertIn("one side only", self.wa)
        self.assertIn("no numbering", self.w_item)
        self.assertIn("provides only the image", self.w_item)
        self.assertFalse(has_real_barthel_codes(self.wa))
        self.assertFalse(has_real_barthel_codes(self.w_item, prefix="W"))
        published = extract_published_tokens(self.wa, SIDE_WA)
        self.assertEqual(tuple(published), WA_LINE_NAMES)
        self.assertEqual(published["Wa1"], ["(10", "30)!"])
        self.assertEqual(
            [published[name] for name in WA_LINE_NAMES[1:]],
            [[], [], []],
        )
        self.assertEqual(side_line_stems(published, WA_LINE_NAMES), [[], [], [], []])
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_w_html_names(fixtures), ())
        text = (W_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        for url in (
            CITED_CATALOG_URL,
            CITED_TABLETS_URL,
            CITED_W_INDEX_URL,
            CITED_WA_URL,
            CITED_W_ITEM_URL,
        ):
            self.assertIn(url, text)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
        self.assertIn("tablet X", text)
        self.assertEqual(tablet_row(self.tablets, "X"), STANDING_CATALOG_X)
        self.assertEqual(STANDING_NEXT_CATALOG, "X")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.lock, score_w_unpublished(False))
        self.assertFalse(self.lock.w_barthel)
        self.assertIsNone(self.lock.stem_count)
        self.assertIsNone(self.lock.longest_n)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_v_and_inventory_scoreboards_still_compute(self):
        """Cycle 98 V vendor lock and cycle 99 A–V inventory stay."""
        prior_v = TestMamariHonolulu3VendorScoreboard()
        prior_v.setUp()
        prior_v.test_longest_repeating_ngram_is_4()
        prior_v.test_survey_matches_computed_lock()
        from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
            TestMamariCorpusLongestNInventoryScoreboard,
        )

        prior_inv = TestMamariCorpusLongestNInventoryScoreboard()
        prior_inv.setUp()
        prior_inv.test_inventory_holds_and_priors_match()
        prior_inv.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-100 W unpublished lock."""
        lock = self.survey["tablet_w_honolulu_unpublished"]
        self.assertEqual(lock["cycle"], 100)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_w"], "W")
        self.assertEqual(lock["name_w"], "Honolulu 4 [#445]")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["w_index"], CITED_W_INDEX_URL)
        self.assertEqual(lock["wa_page"], CITED_WA_URL)
        self.assertEqual(lock["w_item_page"], CITED_W_ITEM_URL)
        self.assertEqual(tuple(lock["w_pages"]), STANDING_W_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Wa"], STANDING_WA_BYTES)
        self.assertEqual(lock["html_bytes"]["W"], STANDING_W_ITEM_BYTES)
        self.assertEqual(lock["index_bytes"]["W"], STANDING_W_INDEX_BYTES)
        self.assertEqual(lock["head_check"], STANDING_HEAD)
        self.assertEqual(lock["wa_html_kind"], STANDING_WA_HTML_KIND)
        self.assertEqual(lock["w_html_kind"], STANDING_W_HTML_KIND)
        self.assertEqual(tuple(lock["wa_published_cells"]), STANDING_WA_PUBLISHED_CELLS)
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["wa_html"])
        self.assertFalse(lock["wb_html"])
        self.assertFalse(lock["wr_html"])
        self.assertFalse(lock["wv_html"])
        self.assertFalse(lock["w_html"])
        self.assertIsNone(lock["stem_count"])
        self.assertIsNone(lock["longest_n"])
        self.assertIsNone(lock["gk_hits"])
        self.assertIsNone(lock["hpq_hits"])
        self.assertIsNone(lock["e_n9_hits"])
        self.assertIsNone(lock["er7_4_hits"])
        self.assertIsNone(lock["m_n4_hits"])
        self.assertIsNone(lock["n_n6_hits"])
        self.assertIsNone(lock["s_n7_hits"])
        self.assertIsNone(lock["v_n4_hits"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["next_catalog"], STANDING_NEXT_CATALOG)
        self.assertEqual(tuple(lock["catalog_x"]), STANDING_CATALOG_X)
        self.assertTrue(lock["standing_v_honolulu_vendor_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_v_honolulu_vendor"]["cycle"], 98)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertFalse(self.survey["corpus_longest_n_inventory"]["w_html"])
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHonolulu4UnpublishedImageSnapshot(unittest.TestCase):
    """Cycle 100 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
