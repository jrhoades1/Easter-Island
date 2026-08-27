"""Small Santiago recto Gr: Kohaumotu Gr.html search lock.

Cycle 55 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / I. Cycle 54 locked Ga.html as
unpublished and documented Gr.html as the recto. This cycle vendors
that Gr.html. Digits are copied from the snapshot. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents.

Locks on Gr.html only: stem count; presence/absence of the locked
A/B/C motifs and the Ia top 5-gram; 076 rate (hits/stems, whether
rate ≥ 0.10); 090 076 / 076 071 / 090 076 071 hit counts. If
Gr.html is absent, lock that absence and stop. Do not scrape Gv
or another tablet.

Search lock, not a merge and not a translation. MockProvider only.
"""

import re
import unittest
from dataclasses import dataclass
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_bv_scoreboard import STANDING_LONGEST_NGRAM as BV_8GRAM
from tests.test_mamari_remainder_9gram_motif_scoreboard import MOTIF_9GRAM
from tests.test_mamari_santiago_ia_076_inventory_scoreboard import STEM_076
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    RATE_THRESHOLD,
    score_076_rate,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    GRAM_076_071,
    GRAM_090_076,
    GRAM_090_076_071,
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_scoreboard import STANDING_LONGEST_NGRAM as IA_5GRAM
from tests.test_mamari_second_passage_scoreboard import (
    _LINE_HEADER,
    find_ngram_hits,
    load_corpus_survey,
    published_stems,
)
from tests.test_mamari_small_santiago_ga_scoreboard import (
    GA_HTML_DIR,
    G_INDEX_HTML_PATH,
    STANDING_DOCUMENTED_RECTO,
    STANDING_G_ALL_LINES,
    STANDING_G_INDEX_BYTES,
    STANDING_TABLET_G,
    TestMamariSmallSantiagoGaScoreboard,
    load_vendored_g_index_html,
    tablet_g_row,
)
from tests.test_mamari_santiago_ib_scoreboard import (
    FOURTH_TABLET_PAGES,
    fourth_tablet_html_names,
    published_all_lines_hrefs,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import MOTIF_10GRAM
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import MOTIF_AB_9GRAM

GR_HTML_DIR = Path(__file__).parent / "fixtures" / "small_santiago_gr_html"
GR_HTML_PATH = GR_HTML_DIR / "Gr.html"
GV_HTML_PATH = GR_HTML_DIR / "Gv.html"
CITED_GR_URL = "http://kohaumotu.org/Rongorongo/G/Gr.html"
CITED_G_INDEX_URL = "http://kohaumotu.org/Rongorongo/G/index.html"
CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"

GR_LINE_NAMES = tuple(f"Gr{n}" for n in range(1, 9))
STANDING_HTML_BYTES = 4270
STANDING_STEM_COUNTS = (40, 40, 40, 45, 44, 54, 48, 44)
STANDING_STEM_TOTAL = 355
STANDING_MOTIF_9GRAM_PRESENT = False
STANDING_MOTIF_10GRAM_PRESENT = False
STANDING_MOTIF_AB_9GRAM_PRESENT = False
STANDING_MOTIF_BV_8GRAM_PRESENT = False
STANDING_IA_5GRAM_PRESENT = False
STANDING_076_HITS = 2
STANDING_076_RATE = STANDING_076_HITS / STANDING_STEM_TOTAL
STANDING_076_RATE_GE_THRESHOLD = False
STANDING_090_076_HITS = 0
STANDING_076_071_HITS = 0
STANDING_090_076_071_HITS = 0
STANDING_GR_HTML = True
STANDING_RESULT = "gr_html_vendored"
STANDING_ABSENT_RESULT = "gr_html_absent"
STANDING_GV_HTML_VENDORED = False
STANDING_NEW_TABLET = False
STANDING_TABLET_D_SCRAPED = False
STANDING_TABLET_K_SCRAPED = False
K_BARTHEL_PAGES = ("K.html", "Ka.html", "Kb.html", "Kr.html", "Kv.html")


@dataclass(frozen=True)
class GrRectoLock:
    """Gr.html search lock. Counts stay None when the page is absent."""

    gr_html: bool
    result: str
    stem_count: int | None
    stem_076_hits: int | None
    stem_076_rate: float | None
    stem_076_rate_ge_0_10: bool | None
    hits_090_076: int | None
    hits_076_071: int | None
    hits_090_076_071: int | None
    motif_a: bool | None
    motif_b: bool | None
    motif_c: bool | None
    ia_5gram_top: bool | None


def load_vendored_gr_html() -> str:
    """Return the vendored Kohaumotu Gr.html snapshot."""
    return GR_HTML_PATH.read_text(encoding="utf-8")


def extract_gr_published_tokens(html: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Gr.html <td> text.

    Same mechanical copy as Aa.html / Br.html / Ca.html / Ia.html.
    Does not invent numbers. Image cells are skipped.
    """
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"Gr{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def gr_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Gr1–Gr8 as stem sequences. Search only."""
    return [published_stems(published[name]) for name in GR_LINE_NAMES]


def score_gr_recto(gr_exists: bool, lines: list[list[str]] | None = None) -> GrRectoLock:
    """Lock Gr.html counts, or absence. Do not invent stems. Do not scrape Gv."""
    if not gr_exists:
        return GrRectoLock(
            gr_html=False,
            result=STANDING_ABSENT_RESULT,
            stem_count=None,
            stem_076_hits=None,
            stem_076_rate=None,
            stem_076_rate_ge_0_10=None,
            hits_090_076=None,
            hits_076_071=None,
            hits_090_076_071=None,
            motif_a=None,
            motif_b=None,
            motif_c=None,
            ia_5gram_top=None,
        )
    if lines is None:
        raise AssertionError("Gr.html exists; pass extracted stems")
    rate = score_076_rate(lines, "tablet_g_small_santiago_recto")
    motif_a = bool(find_ngram_hits(lines, MOTIF_10GRAM)) or bool(
        find_ngram_hits(lines, MOTIF_AB_9GRAM)
    )
    return GrRectoLock(
        gr_html=True,
        result=STANDING_RESULT,
        stem_count=rate.stems,
        stem_076_hits=rate.hits,
        stem_076_rate=rate.rate,
        stem_076_rate_ge_0_10=rate.ge_threshold,
        hits_090_076=ngram_hit_count(lines, GRAM_090_076),
        hits_076_071=ngram_hit_count(lines, GRAM_076_071),
        hits_090_076_071=ngram_hit_count(lines, GRAM_090_076_071),
        motif_a=motif_a,
        motif_b=bool(find_ngram_hits(lines, BV_8GRAM)),
        motif_c=bool(find_ngram_hits(lines, MOTIF_9GRAM)),
        ia_5gram_top=bool(find_ngram_hits(lines, IA_5GRAM)),
    )


def substitute_k_or_gv(fixtures: Path) -> tuple[str, ...]:
    """Gv or K-side Barthel filenames under fixtures, if any were vendored."""
    names = ("Gv.html",) + K_BARTHEL_PAGES
    return tuple(name for name in names if any(fixtures.glob(f"**/{name}")))


class TestSmallSantiagoGrHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; GrN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>002.076-007*</td></tr></table>"
            '<h3><a name="Line_8">Line 8</a></h3>'
            "<table><tr><td>090-076-071-</td></tr></table>"
        )
        published = extract_gr_published_tokens(html)
        self.assertEqual(list(published), ["Gr1", "Gr8"])
        self.assertEqual(published["Gr1"], ["002.076", "007*"])
        self.assertEqual(published["Gr8"], ["090", "076", "071"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_absence_lock_stops_without_inventing_counts(self):
        """Missing Gr.html yields None counts and does not read Gv."""
        provider = MockProvider()
        lock = score_gr_recto(False)
        self.assertFalse(lock.gr_html)
        self.assertEqual(lock.result, STANDING_ABSENT_RESULT)
        self.assertIsNone(lock.stem_count)
        self.assertIsNone(lock.stem_076_hits)
        self.assertIsNone(lock.stem_076_rate)
        self.assertIsNone(lock.hits_090_076_071)
        self.assertIsNone(lock.ia_5gram_top)
        with self.assertRaises(AssertionError):
            score_gr_recto(True)
        self.assertEqual(substitute_k_or_gv(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])

    def test_vendor_lock_counts_stems_motifs_and_076(self):
        """Present Gr.html locks stem/076/n-gram/motif fields from stems."""
        provider = MockProvider()
        lines = [
            ["999", "071", "076", "010", "079", "090", "076", "071"],
            ["002"] * 9,
        ]
        lock = score_gr_recto(True, lines)
        self.assertTrue(lock.gr_html)
        self.assertEqual(lock.result, STANDING_RESULT)
        self.assertEqual(lock.stem_count, 17)
        self.assertEqual(lock.stem_076_hits, 2)
        self.assertEqual(lock.stem_076_rate, 2 / 17)
        self.assertTrue(lock.stem_076_rate_ge_0_10)
        self.assertEqual(lock.hits_090_076, 1)
        self.assertEqual(lock.hits_076_071, 1)
        self.assertEqual(lock.hits_090_076_071, 1)
        self.assertTrue(lock.ia_5gram_top)
        self.assertFalse(lock.motif_a)
        self.assertFalse(lock.motif_b)
        self.assertFalse(lock.motif_c)
        self.assertEqual(RATE_THRESHOLD, 0.10)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoGrScoreboard(unittest.TestCase):
    """Cited tablets.html → G → Gr.html lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.g_index = load_vendored_g_index_html()
        self.html = load_vendored_gr_html()
        self.published = extract_gr_published_tokens(self.html)
        self.lines = gr_line_stems(self.published)
        self.lock = score_gr_recto(GR_HTML_PATH.exists(), self.lines)

    def test_parent_catalog_selects_and_vendors_gr(self):
        """Catalog → tablets → G → Gr.html. Not Ga, Gv, K, or D."""
        self.assertTrue(GR_HTML_PATH.is_file())
        self.assertTrue((GR_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(G_INDEX_HTML_PATH.is_file())
        self.assertFalse(GV_HTML_PATH.exists())
        self.assertFalse((GA_HTML_DIR / "Gr.html").exists())
        self.assertFalse((GA_HTML_DIR / "Ga.html").exists())
        self.assertEqual(GR_HTML_PATH.stat().st_size, STANDING_HTML_BYTES)
        self.assertEqual(G_INDEX_HTML_PATH.stat().st_size, STANDING_G_INDEX_BYTES)
        self.assertEqual(tablet_g_row(self.tablets), STANDING_TABLET_G)
        self.assertEqual(published_all_lines_hrefs(self.g_index), STANDING_G_ALL_LINES)
        self.assertEqual(STANDING_DOCUMENTED_RECTO, "Gr.html")
        self.assertIn("Item G:The Small Santiago tablet", self.g_index)
        self.assertIn('href="Gr.html"', self.g_index)
        self.assertIn("Item G:The Small Santiago Tablet", self.html)
        self.assertIn("Recto", self.html)
        self.assertIn("Rongorongo Gr", self.html)
        self.assertNotIn("Item A:Tahua", self.html)
        self.assertNotIn("Item C:Mamari", self.html)
        self.assertEqual(list(self.published), list(GR_LINE_NAMES))
        attribution = (GR_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_CATALOG_URL, attribution)
        self.assertIn(CITED_TABLETS_URL, attribution)
        self.assertIn(CITED_G_INDEX_URL, attribution)
        self.assertIn(CITED_GR_URL, attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        self.assertIn("No Gv scrape", attribution)
        self.assertIn("Gv.html", attribution)
        self.assertIn("tablet K", attribution)
        self.assertIn("tablet D", attribution)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(substitute_k_or_gv(fixtures), ())
        self.assertEqual(fourth_tablet_html_names(fixtures), ())
        self.assertEqual(FOURTH_TABLET_PAGES[0], "D.html")
        self.assertFalse(STANDING_GV_HTML_VENDORED)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertFalse(STANDING_TABLET_K_SCRAPED)
        self.assertTrue(STANDING_GR_HTML)
        self.assertEqual(self.lock.result, STANDING_RESULT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_count_motifs_076_rate_and_090_076_071(self):
        """355 stems; A/B/C motifs and Ia 5-gram absent; 076 is 2/355."""
        self.assertEqual(
            [len(line) for line in self.lines],
            list(STANDING_STEM_COUNTS),
        )
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_STEM_TOTAL)
        self.assertEqual(
            bool(find_ngram_hits(self.lines, MOTIF_9GRAM)),
            STANDING_MOTIF_9GRAM_PRESENT,
        )
        self.assertEqual(
            bool(find_ngram_hits(self.lines, MOTIF_10GRAM)),
            STANDING_MOTIF_10GRAM_PRESENT,
        )
        self.assertEqual(
            bool(find_ngram_hits(self.lines, MOTIF_AB_9GRAM)),
            STANDING_MOTIF_AB_9GRAM_PRESENT,
        )
        self.assertEqual(
            bool(find_ngram_hits(self.lines, BV_8GRAM)),
            STANDING_MOTIF_BV_8GRAM_PRESENT,
        )
        self.assertEqual(
            bool(find_ngram_hits(self.lines, IA_5GRAM)),
            STANDING_IA_5GRAM_PRESENT,
        )
        rate = score_076_rate(self.lines, "tablet_g_small_santiago_recto")
        self.assertEqual(rate.hits, STANDING_076_HITS)
        self.assertEqual(rate.stems, STANDING_STEM_TOTAL)
        self.assertEqual(rate.rate, STANDING_076_RATE)
        self.assertEqual(rate.rate, STANDING_076_HITS / STANDING_STEM_TOTAL)
        self.assertEqual(rate.ge_threshold, STANDING_076_RATE_GE_THRESHOLD)
        self.assertEqual(rate.ge_threshold, rate.rate >= RATE_THRESHOLD)
        self.assertLess(rate.rate, RATE_THRESHOLD)
        self.assertEqual(ngram_hit_count(self.lines, GRAM_090_076), STANDING_090_076_HITS)
        self.assertEqual(ngram_hit_count(self.lines, GRAM_076_071), STANDING_076_071_HITS)
        self.assertEqual(
            ngram_hit_count(self.lines, GRAM_090_076_071),
            STANDING_090_076_071_HITS,
        )
        self.assertEqual(self.lock, score_gr_recto(True, self.lines))
        self.assertEqual(self.lock.stem_count, STANDING_STEM_TOTAL)
        self.assertEqual(self.lock.stem_076_hits, STANDING_076_HITS)
        self.assertEqual(self.lock.stem_076_rate, STANDING_076_RATE)
        self.assertFalse(self.lock.stem_076_rate_ge_0_10)
        self.assertEqual(self.lock.hits_090_076, STANDING_090_076_HITS)
        self.assertEqual(self.lock.hits_076_071, STANDING_076_071_HITS)
        self.assertEqual(self.lock.hits_090_076_071, STANDING_090_076_071_HITS)
        self.assertFalse(self.lock.motif_a)
        self.assertFalse(self.lock.motif_b)
        self.assertFalse(self.lock.motif_c)
        self.assertFalse(self.lock.ia_5gram_top)
        self.assertEqual(STEM_076, "076")
        self.assertEqual(IA_5GRAM, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_ga_and_scoreboards_still_compute(self):
        """Cycle 54 Ga absence and prior A/B/C/Ia scoreboards stay."""
        prior = TestMamariSmallSantiagoGaScoreboard()
        prior.setUp()
        prior.test_ga_html_is_absent_on_the_documented_g_source()
        prior.test_existing_ib_and_090_076_071_scoreboards_still_compute()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-55 Gr.html vendor lock."""
        lock = self.survey["tablet_g_small_santiago_recto_gr"]
        self.assertEqual(lock["cycle"], 55)
        self.assertEqual(lock["tablet"], "G")
        self.assertEqual(lock["name"], "Small Santiago")
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["gr_html"])
        self.assertEqual(lock["source_page"], CITED_GR_URL)
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["tablet_index"], CITED_G_INDEX_URL)
        self.assertEqual(lock["html_bytes"], STANDING_HTML_BYTES)
        self.assertEqual(lock["lines"], list(GR_LINE_NAMES))
        self.assertEqual(lock["stem_count"], STANDING_STEM_TOTAL)
        self.assertEqual(lock["stem_counts_by_line"], list(STANDING_STEM_COUNTS))
        self.assertEqual(lock["stem_076_hits"], STANDING_076_HITS)
        self.assertEqual(lock["stem_076_rate"], STANDING_076_RATE)
        self.assertFalse(lock["stem_076_rate_ge_0_10"])
        self.assertEqual(lock["hits_090_076"], STANDING_090_076_HITS)
        self.assertEqual(lock["hits_076_071"], STANDING_076_071_HITS)
        self.assertEqual(lock["hits_090_076_071"], STANDING_090_076_071_HITS)
        self.assertEqual(lock["motif_9gram"], STANDING_MOTIF_9GRAM_PRESENT)
        self.assertEqual(lock["motif_10gram"], STANDING_MOTIF_10GRAM_PRESENT)
        self.assertEqual(lock["motif_ab_9gram"], STANDING_MOTIF_AB_9GRAM_PRESENT)
        self.assertEqual(lock["motif_bv_8gram"], STANDING_MOTIF_BV_8GRAM_PRESENT)
        self.assertEqual(lock["ia_5gram_top"], STANDING_IA_5GRAM_PRESENT)
        self.assertFalse(lock["gv_html_vendored"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertFalse(lock["tablet_k_scraped"])
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
        self.assertTrue(lock["standing_ga_locks_unchanged"])
        self.assertEqual(self.survey["tablet_g_small_santiago_recto"]["cycle"], 54)
        self.assertEqual(self.survey["tablet_g_small_santiago_recto"]["result"], "ga_html_absent")
        self.assertFalse(self.survey["tablet_g_small_santiago_recto"]["gr_html_vendored"])
        self.assertEqual(self.survey["santiago_staff_verso_ib"]["cycle"], 53)
        self.assertEqual(self.survey["stem_090_076_071_ngram_per_fixture"]["cycle"], 52)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoGrImageSnapshot(unittest.TestCase):
    """Cycle 55 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
