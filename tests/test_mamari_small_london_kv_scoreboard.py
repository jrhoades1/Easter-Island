"""Small London verso Kv: Kohaumotu Kv.html search lock.

Cycle 60 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / I / G / Kr. Cycle 59 vendored
Kr.html and documented Kv.html as the verso. This cycle vendors
that Kv.html. Digits are copied from the snapshot. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents.

Locks on Kv.html only: stem count; presence/absence of the locked
A/B/C motifs and the Ia top 5-gram; 076 rate (hits/stems, whether
rate ≥ 0.10); 090 076 / 076 071 / 430 076 / 076 200 hit counts.
If Kv.html is absent, lock that absence and stop. Do not scrape
tablet D.

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
    verso_all_lines_href,
)
from tests.test_mamari_small_london_kr_scoreboard import (
    KR_HTML_DIR,
    KR_HTML_PATH,
    K_INDEX_HTML_PATH,
    STANDING_DOCUMENTED_RECTO,
    STANDING_K_ALL_LINES,
    STANDING_K_INDEX_BYTES,
    STANDING_TABLET_K,
    TestMamariSmallLondonKrScoreboard,
    load_vendored_k_index_html,
    tablet_k_row,
)
from tests.test_mamari_small_santiago_ga_scoreboard import (
    recto_all_lines_href,
)
from tests.test_mamari_small_santiago_gv_430_076_200_ngram_scoreboard import (
    GRAM_076_200,
    GRAM_430_076,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import MOTIF_10GRAM
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import MOTIF_AB_9GRAM

KV_HTML_DIR = Path(__file__).parent / "fixtures" / "small_london_kv_html"
KV_HTML_PATH = KV_HTML_DIR / "Kv.html"
KR_IN_KV_DIR = KV_HTML_DIR / "Kr.html"
KA_HTML_PATH = KV_HTML_DIR / "Ka.html"
CITED_KV_URL = "http://kohaumotu.org/Rongorongo/K/Kv.html"
CITED_KR_URL = "http://kohaumotu.org/Rongorongo/K/Kr.html"
CITED_K_INDEX_URL = "http://kohaumotu.org/Rongorongo/K/index.html"
CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"

KV_LINE_NAMES = tuple(f"Kv{n}" for n in range(1, 6))
STANDING_HTML_BYTES = 2396
STANDING_STEM_COUNTS = (11, 25, 29, 29, 1)
STANDING_STEM_TOTAL = 95
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
STANDING_KV_HTML = True
STANDING_RESULT = "kv_html_vendored"
STANDING_ABSENT_RESULT = "kv_html_absent"
STANDING_DOCUMENTED_VERSO = "Kv.html"
STANDING_NEW_TABLET = False
STANDING_TABLET_D_SCRAPED = False


@dataclass(frozen=True)
class KvVersoLock:
    """Kv.html search lock. Counts stay None when the page is absent."""

    kv_html: bool
    result: str
    documented_verso: str | None
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


def load_vendored_kv_html() -> str:
    """Return the vendored Kohaumotu Kv.html snapshot."""
    return KV_HTML_PATH.read_text(encoding="utf-8")


def extract_kv_published_tokens(html: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Kv.html <td> text.

    Same mechanical copy as Aa.html / Gr.html / Gv.html / Ia.html /
    Kr.html. Does not invent numbers. Image cells are skipped.
    """
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"Kv{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def kv_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Kv1–Kv5 as stem sequences. Search only."""
    return [published_stems(published[name]) for name in KV_LINE_NAMES]


def score_kv_verso(
    kv_exists: bool,
    lines: list[list[str]] | None = None,
    documented_verso: str | None = None,
) -> KvVersoLock:
    """Lock Kv.html counts, or absence. Do not invent stems. Do not scrape D."""
    if not kv_exists:
        return KvVersoLock(
            kv_html=False,
            result=STANDING_ABSENT_RESULT,
            documented_verso=documented_verso,
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
        raise AssertionError("Kv.html exists; pass extracted stems")
    rate = score_076_rate(lines, "tablet_k_small_london_verso")
    motif_a = bool(find_ngram_hits(lines, MOTIF_10GRAM)) or bool(
        find_ngram_hits(lines, MOTIF_AB_9GRAM)
    )
    return KvVersoLock(
        kv_html=True,
        result=STANDING_RESULT,
        documented_verso=documented_verso,
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


def substitute_d(fixtures: Path) -> tuple[str, ...]:
    """D-side Barthel filenames under fixtures, if any were vendored."""
    return fourth_tablet_html_names(fixtures)


class TestSmallLondonKvHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; KvN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>000!-019-019-</td></tr></table>"
            '<h3><a name="Line_5">Line 5</a></h3>'
            "<table><tr><td>???</td></tr>"
            "<tr><td>070-(5-6)!*</td></tr></table>"
        )
        published = extract_kv_published_tokens(html)
        self.assertEqual(list(published), ["Kv1", "Kv5"])
        self.assertEqual(published["Kv1"], ["000!", "019", "019"])
        self.assertEqual(published["Kv5"], ["070", "(5", "6)!*"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_absence_lock_keeps_documented_verso_without_inventing_counts(self):
        """Missing Kv.html yields None counts and names the index verso."""
        provider = MockProvider()
        lock = score_kv_verso(False, documented_verso="Kv.html")
        self.assertFalse(lock.kv_html)
        self.assertEqual(lock.result, STANDING_ABSENT_RESULT)
        self.assertEqual(lock.documented_verso, STANDING_DOCUMENTED_VERSO)
        self.assertIsNone(lock.stem_count)
        self.assertIsNone(lock.stem_076_hits)
        self.assertIsNone(lock.stem_076_rate)
        self.assertIsNone(lock.hits_430_076)
        self.assertIsNone(lock.ia_5gram_top)
        with self.assertRaises(AssertionError):
            score_kv_verso(True)
        self.assertEqual(substitute_d(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])

    def test_vendor_lock_counts_stems_motifs_and_076(self):
        """Present Kv.html locks stem/076/n-gram/motif fields from stems."""
        provider = MockProvider()
        lines = [
            ["999", "071", "076", "010", "079", "090", "076", "071", "430", "076", "200"],
            ["002"] * 9,
        ]
        lock = score_kv_verso(True, lines, STANDING_DOCUMENTED_VERSO)
        self.assertTrue(lock.kv_html)
        self.assertEqual(lock.result, STANDING_RESULT)
        self.assertEqual(lock.stem_count, 20)
        self.assertEqual(lock.stem_076_hits, 3)
        self.assertEqual(lock.stem_076_rate, 3 / 20)
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


class TestMamariSmallLondonKvScoreboard(unittest.TestCase):
    """Cited tablets.html → K → Kv.html lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.k_index = load_vendored_k_index_html()
        self.html = load_vendored_kv_html()
        self.published = extract_kv_published_tokens(self.html)
        self.lines = kv_line_stems(self.published)
        self.k_sides = published_all_lines_hrefs(self.k_index)
        self.lock = score_kv_verso(
            KV_HTML_PATH.exists(),
            self.lines,
            verso_all_lines_href(self.k_sides, STANDING_DOCUMENTED_RECTO),
        )

    def test_parent_catalog_selects_and_vendors_kv(self):
        """Catalog → tablets → K → Kv.html. Not Ka or D."""
        self.assertTrue(KV_HTML_PATH.is_file())
        self.assertTrue((KV_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(K_INDEX_HTML_PATH.is_file())
        self.assertTrue(KR_HTML_PATH.is_file())
        self.assertFalse(KR_IN_KV_DIR.exists())
        self.assertFalse((KR_HTML_DIR / "Kv.html").exists())
        self.assertFalse(KA_HTML_PATH.exists())
        self.assertEqual(KV_HTML_PATH.stat().st_size, STANDING_HTML_BYTES)
        self.assertEqual(K_INDEX_HTML_PATH.stat().st_size, STANDING_K_INDEX_BYTES)
        self.assertEqual(tablet_k_row(self.tablets), STANDING_TABLET_K)
        self.assertEqual(self.k_sides, STANDING_K_ALL_LINES)
        self.assertEqual(recto_all_lines_href(self.k_sides), STANDING_DOCUMENTED_RECTO)
        self.assertEqual(
            verso_all_lines_href(self.k_sides, STANDING_DOCUMENTED_RECTO),
            STANDING_DOCUMENTED_VERSO,
        )
        self.assertEqual(STANDING_DOCUMENTED_VERSO, "Kv.html")
        self.assertIn("Item K:Small London tablet", self.k_index)
        self.assertIn('href="Kv.html"', self.k_index)
        self.assertIn("Verso (all lines)", self.k_index)
        self.assertIn('href="Kr.html"', self.html)
        self.assertIn("Item K:the Small London Tablet", self.html)
        self.assertIn("Verso", self.html)
        self.assertIn("Rongorongo Kv", self.html)
        self.assertNotIn("Item A:Tahua", self.html)
        self.assertNotIn("Item C:Mamari", self.html)
        self.assertNotIn("Item G:The Small Santiago", self.html)
        self.assertEqual(list(self.published), list(KV_LINE_NAMES))
        attribution = (KV_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_CATALOG_URL, attribution)
        self.assertIn(CITED_TABLETS_URL, attribution)
        self.assertIn(CITED_K_INDEX_URL, attribution)
        self.assertIn(CITED_KR_URL, attribution)
        self.assertIn(CITED_KV_URL, attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        self.assertIn("Ka.html", attribution)
        self.assertIn("tablet D", attribution)
        self.assertIn("Gr vs Ga", attribution)
        self.assertEqual(substitute_d(KV_HTML_DIR), ())
        self.assertEqual(fourth_tablet_html_names(KR_HTML_DIR), ())
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(fourth_tablet_html_names(fixtures), ())
        self.assertEqual(FOURTH_TABLET_PAGES[0], "D.html")
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertTrue(STANDING_KV_HTML)
        self.assertEqual(self.lock.result, STANDING_RESULT)
        self.assertEqual(self.lock.documented_verso, STANDING_DOCUMENTED_VERSO)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_count_motifs_076_rate_and_locked_ngrams(self):
        """95 stems; A/B/C motifs and Ia 5-gram absent; 076 is 0/95."""
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
        rate = score_076_rate(self.lines, "tablet_k_small_london_verso")
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
            score_kv_verso(True, self.lines, STANDING_DOCUMENTED_VERSO),
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

    def test_existing_kr_scoreboard_still_computes(self):
        """Cycle 59 Kr vendor and Cycle 58 3×10 table stay."""
        prior = TestMamariSmallLondonKrScoreboard()
        prior.setUp()
        prior.test_parent_catalog_selects_and_vendors_kr()
        prior.test_stem_count_motifs_076_rate_and_locked_ngrams()
        prior.test_existing_430_076_200_scoreboard_still_computes()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-60 Kv.html vendor lock."""
        lock = self.survey["tablet_k_small_london_verso_kv"]
        self.assertEqual(lock["cycle"], 60)
        self.assertEqual(lock["tablet"], "K")
        self.assertEqual(lock["name"], "Small London")
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["kv_html"])
        self.assertEqual(lock["documented_verso_page"], STANDING_DOCUMENTED_VERSO)
        self.assertEqual(lock["documented_all_lines"], list(STANDING_K_ALL_LINES))
        self.assertEqual(lock["source_page"], CITED_KV_URL)
        self.assertEqual(lock["verso_of"], CITED_KR_URL)
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["tablet_index"], CITED_K_INDEX_URL)
        self.assertEqual(lock["html_bytes"], STANDING_HTML_BYTES)
        self.assertEqual(lock["lines"], list(KV_LINE_NAMES))
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
        self.assertTrue(lock["standing_kr_locks_unchanged"])
        self.assertTrue(lock["standing_430_076_200_ngram_unchanged"])
        self.assertEqual(self.survey["tablet_k_small_london_recto"]["cycle"], 59)
        self.assertEqual(
            self.survey["tablet_k_small_london_recto"]["result"],
            "kr_html_vendored",
        )
        self.assertFalse(self.survey["tablet_k_small_london_recto"]["kv_html_vendored"])
        self.assertEqual(self.survey["stem_430_076_200_ngram_per_fixture"]["cycle"], 58)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallLondonKvImageSnapshot(unittest.TestCase):
    """Cycle 60 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
