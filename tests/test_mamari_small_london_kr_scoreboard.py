"""Small London recto Kr: Kohaumotu Kr.html search lock.

Cycle 59 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / I / G. Preferred tablet this
cycle is K / Small London. Kr.html is the published recto on
K/index.html (same Gr vs Ga lesson: Ka.html is unpublished; the
index lists Kr.html). Digits are copied from the snapshot. No
invented Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents.

Locks on Kr.html only: stem count; presence/absence of the locked
A/B/C motifs and the Ia top 5-gram; 076 rate (hits/stems, whether
rate ≥ 0.10); 090 076 / 076 071 / 430 076 / 076 200 hit counts.
If Kr.html is absent, lock the published K-side filename from
K/index.html. Do not scrape Kv or another tablet letter.

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
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_scoreboard import STANDING_LONGEST_NGRAM as IA_5GRAM
from tests.test_mamari_second_passage_scoreboard import (
    _LINE_HEADER,
    find_ngram_hits,
    load_corpus_survey,
    published_stems,
)
from tests.test_mamari_santiago_ib_scoreboard import (
    FOURTH_TABLET_PAGES,
    fourth_tablet_html_names,
    published_all_lines_hrefs,
)
from tests.test_mamari_small_santiago_ga_scoreboard import (
    recto_all_lines_href,
)
from tests.test_mamari_small_santiago_gv_430_076_200_ngram_scoreboard import (
    GRAM_076_200,
    GRAM_430_076,
    TestMamariSmallSantiagoGv430076200NgramScoreboard,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import MOTIF_10GRAM
from tests.test_mamari_tahua_aa_scoreboard import (
    _TABLET_ROW,
    load_vendored_tablets_html,
)
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import MOTIF_AB_9GRAM

KR_HTML_DIR = Path(__file__).parent / "fixtures" / "small_london_kr_html"
KR_HTML_PATH = KR_HTML_DIR / "Kr.html"
KV_HTML_PATH = KR_HTML_DIR / "Kv.html"
KA_HTML_PATH = KR_HTML_DIR / "Ka.html"
K_INDEX_HTML_PATH = KR_HTML_DIR / "K_index.html"
CITED_KR_URL = "http://kohaumotu.org/Rongorongo/K/Kr.html"
CITED_K_INDEX_URL = "http://kohaumotu.org/Rongorongo/K/index.html"
CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"

KR_LINE_NAMES = tuple(f"Kr{n}" for n in range(1, 6))
STANDING_HTML_BYTES = 2548
STANDING_K_INDEX_BYTES = 3826
STANDING_STEM_COUNTS = (26, 29, 29, 24, 23)
STANDING_STEM_TOTAL = 131
STANDING_MOTIF_9GRAM_PRESENT = False
STANDING_MOTIF_10GRAM_PRESENT = False
STANDING_MOTIF_AB_9GRAM_PRESENT = False
STANDING_MOTIF_BV_8GRAM_PRESENT = False
STANDING_IA_5GRAM_PRESENT = False
STANDING_076_HITS = 0
STANDING_076_RATE = STANDING_076_HITS / STANDING_STEM_TOTAL
STANDING_076_RATE_GE_THRESHOLD = False
STANDING_090_076_HITS = 0
STANDING_076_071_HITS = 0
STANDING_430_076_HITS = 0
STANDING_076_200_HITS = 0
STANDING_KR_HTML = True
STANDING_RESULT = "kr_html_vendored"
STANDING_ABSENT_RESULT = "kr_html_absent"
STANDING_DOCUMENTED_RECTO = "Kr.html"
STANDING_K_ALL_LINES = ("Kr.html", "Kv.html")
STANDING_TABLET_K = ("K", "K/index.html", "Small London")
STANDING_KV_HTML_VENDORED = False
STANDING_NEW_TABLET = False
STANDING_TABLET_D_SCRAPED = False
D_AND_KV_PAGES = FOURTH_TABLET_PAGES + ("Kv.html", "Ka.html")


@dataclass(frozen=True)
class KrRectoLock:
    """Kr.html search lock. Counts stay None when the page is absent."""

    kr_html: bool
    result: str
    documented_recto: str | None
    stem_count: int | None
    stem_076_hits: int | None
    stem_076_rate: float | None
    stem_076_rate_ge_0_10: bool | None
    hits_090_076: int | None
    hits_076_071: int | None
    hits_430_076: int | None
    hits_076_200: int | None
    motif_a: bool | None
    motif_b: bool | None
    motif_c: bool | None
    ia_5gram_top: bool | None


def load_vendored_kr_html() -> str:
    """Return the vendored Kohaumotu Kr.html snapshot."""
    return KR_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_k_index_html() -> str:
    """Return the vendored Kohaumotu K/index.html snapshot."""
    return K_INDEX_HTML_PATH.read_text(encoding="utf-8")


def extract_kr_published_tokens(html: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Kr.html <td> text.

    Same mechanical copy as Aa.html / Gr.html / Gv.html / Ia.html.
    Does not invent numbers. Image cells are skipped.
    """
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"Kr{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def kr_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Kr1–Kr5 as stem sequences. Search only."""
    return [published_stems(published[name]) for name in KR_LINE_NAMES]


def tablet_k_row(tablets_html: str) -> tuple[str, str, str] | None:
    """K if that row has an href. Does not invent a URL."""
    for letter, href, linked_name, plain_name in _TABLET_ROW.findall(tablets_html):
        _ = plain_name
        if letter == "K" and href:
            return (letter, href, linked_name)
    return None


def score_kr_recto(
    kr_exists: bool,
    lines: list[list[str]] | None = None,
    documented_recto: str | None = None,
) -> KrRectoLock:
    """Lock Kr.html counts, or absence. Do not invent stems. Do not scrape Kv."""
    if not kr_exists:
        return KrRectoLock(
            kr_html=False,
            result=STANDING_ABSENT_RESULT,
            documented_recto=documented_recto,
            stem_count=None,
            stem_076_hits=None,
            stem_076_rate=None,
            stem_076_rate_ge_0_10=None,
            hits_090_076=None,
            hits_076_071=None,
            hits_430_076=None,
            hits_076_200=None,
            motif_a=None,
            motif_b=None,
            motif_c=None,
            ia_5gram_top=None,
        )
    if lines is None:
        raise AssertionError("Kr.html exists; pass extracted stems")
    rate = score_076_rate(lines, "tablet_k_small_london_recto")
    motif_a = bool(find_ngram_hits(lines, MOTIF_10GRAM)) or bool(
        find_ngram_hits(lines, MOTIF_AB_9GRAM)
    )
    return KrRectoLock(
        kr_html=True,
        result=STANDING_RESULT,
        documented_recto=documented_recto,
        stem_count=rate.stems,
        stem_076_hits=rate.hits,
        stem_076_rate=rate.rate,
        stem_076_rate_ge_0_10=rate.ge_threshold,
        hits_090_076=ngram_hit_count(lines, GRAM_090_076),
        hits_076_071=ngram_hit_count(lines, GRAM_076_071),
        hits_430_076=ngram_hit_count(lines, GRAM_430_076),
        hits_076_200=ngram_hit_count(lines, GRAM_076_200),
        motif_a=motif_a,
        motif_b=bool(find_ngram_hits(lines, BV_8GRAM)),
        motif_c=bool(find_ngram_hits(lines, MOTIF_9GRAM)),
        ia_5gram_top=bool(find_ngram_hits(lines, IA_5GRAM)),
    )


def substitute_kv_or_d(fixtures: Path) -> tuple[str, ...]:
    """Kv / Ka or D-side Barthel filenames under fixtures, if any were vendored."""
    return tuple(name for name in D_AND_KV_PAGES if any(fixtures.glob(f"**/{name}")))


class TestSmallLondonKrHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; KrN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>000!-522-045.061.009-</td></tr></table>"
            '<h3><a name="Line_5">Line 5</a></h3>'
            "<table><tr><td>090-076-071-</td></tr></table>"
        )
        published = extract_kr_published_tokens(html)
        self.assertEqual(list(published), ["Kr1", "Kr5"])
        self.assertEqual(published["Kr1"], ["000!", "522", "045.061.009"])
        self.assertEqual(published["Kr5"], ["090", "076", "071"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_absence_lock_keeps_documented_recto_without_inventing_counts(self):
        """Missing Kr.html yields None counts and names the index recto."""
        provider = MockProvider()
        lock = score_kr_recto(False, documented_recto="Kr.html")
        self.assertFalse(lock.kr_html)
        self.assertEqual(lock.result, STANDING_ABSENT_RESULT)
        self.assertEqual(lock.documented_recto, STANDING_DOCUMENTED_RECTO)
        self.assertIsNone(lock.stem_count)
        self.assertIsNone(lock.stem_076_hits)
        self.assertIsNone(lock.stem_076_rate)
        self.assertIsNone(lock.hits_430_076)
        self.assertIsNone(lock.ia_5gram_top)
        with self.assertRaises(AssertionError):
            score_kr_recto(True)
        self.assertEqual(substitute_kv_or_d(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])

    def test_vendor_lock_counts_stems_motifs_and_076(self):
        """Present Kr.html locks stem/076/n-gram/motif fields from stems."""
        provider = MockProvider()
        lines = [
            ["999", "071", "076", "010", "079", "090", "076", "430", "076", "200"],
            ["002"] * 9,
        ]
        lock = score_kr_recto(True, lines, STANDING_DOCUMENTED_RECTO)
        self.assertTrue(lock.kr_html)
        self.assertEqual(lock.result, STANDING_RESULT)
        self.assertEqual(lock.stem_count, 19)
        self.assertEqual(lock.stem_076_hits, 3)
        self.assertEqual(lock.stem_076_rate, 3 / 19)
        self.assertTrue(lock.stem_076_rate_ge_0_10)
        self.assertEqual(lock.hits_090_076, 1)
        self.assertEqual(lock.hits_076_071, 1)
        self.assertEqual(lock.hits_430_076, 1)
        self.assertEqual(lock.hits_076_200, 1)
        self.assertTrue(lock.ia_5gram_top)
        self.assertFalse(lock.motif_a)
        self.assertFalse(lock.motif_b)
        self.assertFalse(lock.motif_c)
        self.assertEqual(RATE_THRESHOLD, 0.10)
        self.assertEqual(provider.get_call_history(), [])

    def test_tablets_row_selects_small_london(self):
        """K wins when linked; a missing K row is None."""
        html = (
            "<table>"
            '<tr><td>G</td><td><a href="G/index.html">Small Santiago</a></td></tr>'
            '<tr><td>K</td><td><a href="K/index.html">Small London</a></td></tr>'
            "</table>"
        )
        self.assertEqual(tablet_k_row(html), STANDING_TABLET_K)
        self.assertIsNone(tablet_k_row(html.replace("K/index.html", "")))
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallLondonKrScoreboard(unittest.TestCase):
    """Cited tablets.html → K → Kr.html lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.k_index = load_vendored_k_index_html()
        self.html = load_vendored_kr_html()
        self.published = extract_kr_published_tokens(self.html)
        self.lines = kr_line_stems(self.published)
        self.k_sides = published_all_lines_hrefs(self.k_index)
        self.lock = score_kr_recto(
            KR_HTML_PATH.exists(),
            self.lines,
            recto_all_lines_href(self.k_sides),
        )

    def test_parent_catalog_selects_and_vendors_kr(self):
        """Catalog → tablets → K → Kr.html. Not Ka, Kv, or D."""
        self.assertTrue(KR_HTML_PATH.is_file())
        self.assertTrue((KR_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(K_INDEX_HTML_PATH.is_file())
        self.assertFalse(KV_HTML_PATH.exists())
        self.assertFalse(KA_HTML_PATH.exists())
        self.assertEqual(KR_HTML_PATH.stat().st_size, STANDING_HTML_BYTES)
        self.assertEqual(K_INDEX_HTML_PATH.stat().st_size, STANDING_K_INDEX_BYTES)
        self.assertEqual(tablet_k_row(self.tablets), STANDING_TABLET_K)
        self.assertEqual(self.k_sides, STANDING_K_ALL_LINES)
        self.assertEqual(recto_all_lines_href(self.k_sides), STANDING_DOCUMENTED_RECTO)
        self.assertEqual(STANDING_DOCUMENTED_RECTO, "Kr.html")
        self.assertNotEqual(STANDING_DOCUMENTED_RECTO, "Ka.html")
        self.assertIn("Item K:Small London tablet", self.k_index)
        self.assertIn('href="Kr.html"', self.k_index)
        self.assertIn('href="Kv.html"', self.k_index)
        self.assertNotIn("Ka.html", self.k_index)
        self.assertIn("Item K:the Small London Tablet", self.html)
        self.assertIn("Recto", self.html)
        self.assertIn("Rongorongo Kr", self.html)
        self.assertNotIn("Item A:Tahua", self.html)
        self.assertNotIn("Item C:Mamari", self.html)
        self.assertNotIn("Item G:The Small Santiago", self.html)
        self.assertEqual(list(self.published), list(KR_LINE_NAMES))
        attribution = (KR_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_CATALOG_URL, attribution)
        self.assertIn(CITED_TABLETS_URL, attribution)
        self.assertIn(CITED_K_INDEX_URL, attribution)
        self.assertIn(CITED_KR_URL, attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        self.assertIn("Ka.html", attribution)
        self.assertIn("Kv.html", attribution)
        self.assertIn("tablet D", attribution)
        self.assertIn("Gr vs Ga", attribution)
        self.assertEqual(substitute_kv_or_d(KR_HTML_DIR), ())
        self.assertEqual(fourth_tablet_html_names(KR_HTML_DIR), ())
        self.assertEqual(FOURTH_TABLET_PAGES[0], "D.html")
        self.assertFalse(STANDING_KV_HTML_VENDORED)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertTrue(STANDING_KR_HTML)
        self.assertEqual(self.lock.result, STANDING_RESULT)
        self.assertEqual(self.lock.documented_recto, STANDING_DOCUMENTED_RECTO)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_count_motifs_076_rate_and_locked_ngrams(self):
        """131 stems; A/B/C motifs and Ia 5-gram absent; 076 is 0/131."""
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
        rate = score_076_rate(self.lines, "tablet_k_small_london_recto")
        self.assertEqual(rate.hits, STANDING_076_HITS)
        self.assertEqual(rate.stems, STANDING_STEM_TOTAL)
        self.assertEqual(rate.rate, STANDING_076_RATE)
        self.assertEqual(rate.rate, STANDING_076_HITS / STANDING_STEM_TOTAL)
        self.assertEqual(rate.ge_threshold, STANDING_076_RATE_GE_THRESHOLD)
        self.assertEqual(rate.ge_threshold, rate.rate >= RATE_THRESHOLD)
        self.assertLess(rate.rate, RATE_THRESHOLD)
        self.assertEqual(ngram_hit_count(self.lines, GRAM_090_076), STANDING_090_076_HITS)
        self.assertEqual(ngram_hit_count(self.lines, GRAM_076_071), STANDING_076_071_HITS)
        self.assertEqual(ngram_hit_count(self.lines, GRAM_430_076), STANDING_430_076_HITS)
        self.assertEqual(ngram_hit_count(self.lines, GRAM_076_200), STANDING_076_200_HITS)
        self.assertEqual(
            self.lock,
            score_kr_recto(True, self.lines, STANDING_DOCUMENTED_RECTO),
        )
        self.assertEqual(self.lock.stem_count, STANDING_STEM_TOTAL)
        self.assertEqual(self.lock.stem_076_hits, STANDING_076_HITS)
        self.assertEqual(self.lock.stem_076_rate, STANDING_076_RATE)
        self.assertFalse(self.lock.stem_076_rate_ge_0_10)
        self.assertEqual(self.lock.hits_090_076, STANDING_090_076_HITS)
        self.assertEqual(self.lock.hits_076_071, STANDING_076_071_HITS)
        self.assertEqual(self.lock.hits_430_076, STANDING_430_076_HITS)
        self.assertEqual(self.lock.hits_076_200, STANDING_076_200_HITS)
        self.assertFalse(self.lock.motif_a)
        self.assertFalse(self.lock.motif_b)
        self.assertFalse(self.lock.motif_c)
        self.assertFalse(self.lock.ia_5gram_top)
        self.assertEqual(STEM_076, "076")
        self.assertEqual(IA_5GRAM, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM_430_076, ("430", "076"))
        self.assertEqual(GRAM_076_200, ("076", "200"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_430_076_200_scoreboard_still_computes(self):
        """Cycle 58 3×10 table and prior G/Ia scoreboards stay."""
        prior = TestMamariSmallSantiagoGv430076200NgramScoreboard()
        prior.setUp()
        prior.test_three_by_ten_hit_table()
        prior.test_existing_gv_076_and_ia_ngram_scoreboards_still_compute()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-59 Kr.html vendor lock."""
        lock = self.survey["tablet_k_small_london_recto"]
        self.assertEqual(lock["cycle"], 59)
        self.assertEqual(lock["tablet"], "K")
        self.assertEqual(lock["name"], "Small London")
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["kr_html"])
        self.assertEqual(lock["documented_recto_page"], STANDING_DOCUMENTED_RECTO)
        self.assertEqual(lock["documented_all_lines"], list(STANDING_K_ALL_LINES))
        self.assertEqual(lock["source_page"], CITED_KR_URL)
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["tablet_index"], CITED_K_INDEX_URL)
        self.assertEqual(lock["html_bytes"], STANDING_HTML_BYTES)
        self.assertEqual(lock["lines"], list(KR_LINE_NAMES))
        self.assertEqual(lock["stem_count"], STANDING_STEM_TOTAL)
        self.assertEqual(lock["stem_counts_by_line"], list(STANDING_STEM_COUNTS))
        self.assertEqual(lock["stem_076_hits"], STANDING_076_HITS)
        self.assertEqual(lock["stem_076_rate"], STANDING_076_RATE)
        self.assertFalse(lock["stem_076_rate_ge_0_10"])
        self.assertEqual(lock["hits_090_076"], STANDING_090_076_HITS)
        self.assertEqual(lock["hits_076_071"], STANDING_076_071_HITS)
        self.assertEqual(lock["hits_430_076"], STANDING_430_076_HITS)
        self.assertEqual(lock["hits_076_200"], STANDING_076_200_HITS)
        self.assertEqual(lock["motif_9gram"], STANDING_MOTIF_9GRAM_PRESENT)
        self.assertEqual(lock["motif_10gram"], STANDING_MOTIF_10GRAM_PRESENT)
        self.assertEqual(lock["motif_ab_9gram"], STANDING_MOTIF_AB_9GRAM_PRESENT)
        self.assertEqual(lock["motif_bv_8gram"], STANDING_MOTIF_BV_8GRAM_PRESENT)
        self.assertEqual(lock["ia_5gram_top"], STANDING_IA_5GRAM_PRESENT)
        self.assertFalse(lock["kv_html_vendored"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_gr_locks_unchanged"])
        self.assertTrue(lock["standing_gv_locks_unchanged"])
        self.assertTrue(lock["standing_gv_076_inventory_unchanged"])
        self.assertTrue(lock["standing_430_076_200_ngram_unchanged"])
        self.assertEqual(self.survey["stem_430_076_200_ngram_per_fixture"]["cycle"], 58)
        self.assertEqual(self.survey["tablet_g_small_santiago_verso_gv"]["cycle"], 56)
        self.assertEqual(self.survey["tablet_g_small_santiago_recto_gr"]["cycle"], 55)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallLondonKrImageSnapshot(unittest.TestCase):
    """Cycle 59 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
