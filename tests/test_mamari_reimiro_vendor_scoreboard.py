"""Reimiro 1 (J) vendor lock.

Cycle 86 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / K / P / Q.
HEAD-check before filename assume (cycle 54 Gr vs Ga; cycle 79 Da
vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs Fa): Jb.html / Jr.html /
Jv.html are unpublished 404s. J/index.html names Ja.html (Lines)
and J.html (Item and Lines). Catalog name is Reimiro 1 — not
London / Vienna. Digits are copied from the snapshots. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. No second new letter.

Locks the vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; J's own longest repeating n-gram
(n and whether n≥8 exists). F's locked facts stay. Claim that
can lose: known tradition islands and E islands are exact-0 on J
(closed-tradition hold-out). J is short (longest n=0; no n≥4
freq≥2), so the hold-out is the lock that can leak.

Search lock, not a merge and not a translation. MockProvider only.
"""

import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_chauvet_vendor_scoreboard import (
    TestMamariChauvetVendorScoreboard,
)
from tests.test_mamari_gk_islands_off_hpq_scoreboard import (
    LOCKED_GRAMS as GK_LOCKED_GRAMS,
)
from tests.test_mamari_hpq_island_off_hpq_scoreboard import (
    LOCKED_ISLANDS as HPQ_LOCKED_ISLANDS,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
    GRAM4 as ER7_GRAM4,
    GRAM8 as ER7_GRAM8,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    GRAM_N9 as E_GRAM_N9,
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

JA_HTML_DIR = Path(__file__).parent / "fixtures" / "reimiro_ja_html"
JA_HTML_PATH = JA_HTML_DIR / "Ja.html"
J_HTML_PATH = JA_HTML_DIR / "J.html"
J_INDEX_HTML_PATH = JA_HTML_DIR / "J_index.html"
JA_JSON_PATH = JA_HTML_DIR / "Ja_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_J_INDEX_URL = "http://kohaumotu.org/Rongorongo/J/index.html"
CITED_JA_URL = "http://kohaumotu.org/Rongorongo/J/Ja.html"
CITED_J_URL = "http://kohaumotu.org/Rongorongo/J/J.html"

SIDE_JA = "Ja"
J_SIDES = (SIDE_JA,)

JA_LINE_NAMES = ("Ja1",)
J_LINE_NAMES = {SIDE_JA: JA_LINE_NAMES}

STANDING_JA_BYTES = 782
STANDING_J_HTML_BYTES = 1191
STANDING_J_INDEX_BYTES = 2632
STANDING_JA_STEM_COUNTS = (2,)
STANDING_STEM_TOTALS = {SIDE_JA: 2}
STANDING_STEM_COUNTS = {SIDE_JA: STANDING_JA_STEM_COUNTS}
STANDING_J_ALL_LINES = ("Ja.html",)
STANDING_TABLET_J = ("J", "J/index.html", "Reimiro 1")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in J_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in J_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in J_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in J_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in J_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 0
STANDING_LONGEST_NGRAM = ()
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "j_reimiro_vendored"
STANDING_NEW_TABLET = True
STANDING_JA_HTML = True
STANDING_JB_HTML = False
STANDING_JR_HTML = False
STANDING_JV_HTML = False
STANDING_J_HTML = True
UNPUBLISHED_J_PAGES = ("Jb.html", "Jr.html", "Jv.html")


def load_vendored_ja_html() -> str:
    """Return the vendored Kohaumotu Ja.html snapshot."""
    return JA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_j_html() -> str:
    """Return the vendored Kohaumotu J.html item+lines snapshot."""
    return J_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_j_index_html() -> str:
    """Return the vendored Kohaumotu J/index.html snapshot."""
    return J_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_ja_barthel_json() -> dict:
    """Return the vendored parsed Ja Barthel JSON."""
    return json.loads(JA_JSON_PATH.read_text(encoding="utf-8"))


def load_j_sides() -> dict[str, list[list[str]]]:
    """Ja stems from the vendored parser. No L scrape."""
    return {
        SIDE_JA: side_line_stems(
            extract_published_tokens(load_vendored_ja_html(), SIDE_JA),
            JA_LINE_NAMES,
        ),
    }


def island_hits_by_j_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each J side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in J_SIDES
    }


def unpublished_j_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished J Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_J_PAGES if any(fixtures.glob(f"**/{name}")))


def score_j_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on Ja. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_JA],
        analyzer,
        line_names=JA_LINE_NAMES,
    )


class TestReimiroVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; JaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>522-088*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_JA)
        self.assertEqual(list(published), ["Ja1"])
        self.assertEqual(published["Ja1"], ["522", "088*"])
        stems = side_line_stems(published, ("Ja1",))
        self.assertEqual(stems[0], ["522", "088"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {SIDE_JA: [list(gram)]}
        hits = island_hits_by_j_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_JA][0], 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_j_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariReimiroVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → J → Ja lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.j_index = load_vendored_j_index_html()
        self.by_side = load_j_sides()
        self.gk_hits = island_hits_by_j_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_j_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in J_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in J_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in J_SIDES
        }
        self.profile = score_j_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_j(self):
        """Catalog → tablets → J index → Ja. Not Jb, Jr, or Jv. J.html is item+lines."""
        self.assertTrue(JA_HTML_PATH.is_file())
        self.assertTrue(J_HTML_PATH.is_file())
        self.assertTrue(JA_JSON_PATH.is_file())
        self.assertTrue((JA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(J_INDEX_HTML_PATH.is_file())
        self.assertFalse((JA_HTML_DIR / "Jb.html").exists())
        self.assertFalse((JA_HTML_DIR / "Jr.html").exists())
        self.assertFalse((JA_HTML_DIR / "Jv.html").exists())
        self.assertEqual(STANDING_JA_HTML, True)
        self.assertEqual(STANDING_JB_HTML, False)
        self.assertEqual(STANDING_JR_HTML, False)
        self.assertEqual(STANDING_JV_HTML, False)
        self.assertEqual(STANDING_J_HTML, True)
        self.assertEqual(JA_HTML_PATH.stat().st_size, STANDING_JA_BYTES)
        self.assertEqual(J_HTML_PATH.stat().st_size, STANDING_J_HTML_BYTES)
        self.assertEqual(J_INDEX_HTML_PATH.stat().st_size, STANDING_J_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "J"), STANDING_TABLET_J)
        self.assertEqual(published_all_lines_hrefs(self.j_index), STANDING_J_ALL_LINES)
        self.assertIn("Item J:Reimiro 1", self.j_index)
        self.assertIn('href="Ja.html"', self.j_index)
        self.assertIn('href="J.html"', self.j_index)
        self.assertNotIn('href="Jb.html"', self.j_index)
        self.assertNotIn('href="Jr.html"', self.j_index)
        self.assertNotIn('href="Jv.html"', self.j_index)
        ja = load_vendored_ja_html()
        item = load_vendored_j_html()
        self.assertIn("Item J:Rei Miro 1", ja)
        self.assertIn("Item J:Rei Miro 1", item)
        self.assertIn("Rongorongo Ja1", ja)
        self.assertIn("Rongorongo J", item)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', ja)
        self.assertIn("522-088*", ja)
        self.assertNotIn('<h3><a name="Line_1">', item)
        self.assertEqual(extract_published_tokens(item, SIDE_JA), {})
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_j_html_names(fixtures), ())
        text = (JA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        for url in (
            CITED_CATALOG_URL,
            CITED_TABLETS_URL,
            CITED_J_INDEX_URL,
            CITED_JA_URL,
            CITED_J_URL,
        ):
            self.assertIn(url, text)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
        self.assertIn("tablet L", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        ja_json = load_ja_barthel_json()
        ja_pub = extract_published_tokens(load_vendored_ja_html(), SIDE_JA)
        self.assertEqual(ja_json["tablet"], "J")
        self.assertEqual(ja_json["side"], SIDE_JA)
        self.assertEqual(ja_json["name"], "Reimiro 1")
        self.assertEqual(ja_json["source"]["url"], CITED_JA_URL)
        self.assertEqual(ja_json["lines"]["Ja1"], ja_pub["Ja1"])
        self.assertEqual(ja_json["stems"]["Ja1"], self.by_side[SIDE_JA][0])
        self.assertEqual(ja_json["lines"]["Ja1"], ["522", "088*"])
        self.assertEqual(ja_json["stems"]["Ja1"], ["522", "088"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E n=9, Er7 4-gram are 0 on J."""
        for side in J_SIDES:
            counts = [len(line) for line in self.by_side[side]]
            self.assertEqual(counts, list(STANDING_STEM_COUNTS[side]))
            self.assertEqual(sum(counts), STANDING_STEM_TOTALS[side])
            self.assertEqual(self.gk_hits[side], STANDING_GK_ISLAND_HITS[side])
            self.assertEqual(self.hpq_hits[side], STANDING_HPQ_ISLAND_HITS[side])
            self.assertEqual(self.e_n9_hits[side], STANDING_E_N9_HITS[side])
            self.assertEqual(self.er7_4_hits[side], STANDING_ER7_4_HITS[side])
            self.assertEqual(self.er7_8_hits[side], STANDING_ER7_8_HITS[side])
            for gram, count in zip(GK_LOCKED_GRAMS, self.gk_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            for gram, count in zip(HPQ_LOCKED_ISLANDS, self.hpq_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], E_GRAM_N9), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], ER7_GRAM4), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], ER7_GRAM8), 0)
        self.assertFalse(any(any(hits) for hits in self.gk_hits.values()))
        self.assertFalse(any(any(hits) for hits in self.hpq_hits.values()))
        self.assertFalse(any(self.e_n9_hits.values()))
        self.assertFalse(any(self.er7_4_hits.values()))
        self.assertFalse(any(self.er7_8_hits.values()))
        self.assertEqual(STANDING_ANY_GK_ISLAND, False)
        self.assertEqual(STANDING_ANY_HPQ_ISLAND, False)
        self.assertEqual(STANDING_ANY_E_N9, False)
        self.assertEqual(STANDING_ANY_ER7_DOUBLE, False)
        self.assertEqual(STANDING_ANY_KNOWN_ISLAND, False)
        self.assertEqual(STANDING_CLAIM, "known_islands_absent")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_repeating_ngram_has_no_4gram(self):
        """J's own repeating profile: longest n=0; no n≥4 freq≥2. Not the claim."""
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest_n, 0)
        self.assertEqual(self.profile.rows, ())
        self.assertEqual(self.profile.longest, ())
        self.assertFalse(any(row.n >= 8 for row in self.profile.rows))
        self.assertFalse(STANDING_EIGHTGRAM_EXISTS)
        self.assertEqual(len(self.profile.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.profile.eightgrams, ())
        self.assertIsNone(self.profile.top_8gram)
        self.assertEqual(STANDING_LONGEST_NGRAM, ())
        self.assertNotEqual(STANDING_CLAIM, "no_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_f_chauvet_scoreboard_still_computes(self):
        """Cycle 85 F vendor lock stays."""
        prior = TestMamariChauvetVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_4gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-86 J vendor lock."""
        lock = self.survey["tablet_j_reimiro_vendor"]
        self.assertEqual(lock["cycle"], 86)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_j"], "J")
        self.assertEqual(lock["name_j"], "Reimiro 1")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["j_index"], CITED_J_INDEX_URL)
        self.assertEqual(lock["ja_page"], CITED_JA_URL)
        self.assertEqual(lock["j_page"], CITED_J_URL)
        self.assertEqual(tuple(lock["j_pages"]), STANDING_J_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Ja"], STANDING_JA_BYTES)
        self.assertEqual(lock["html_bytes"]["J"], STANDING_J_HTML_BYTES)
        self.assertEqual(lock["stem_totals"]["Ja"], STANDING_STEM_TOTALS[SIDE_JA])
        self.assertEqual(tuple(lock["stem_counts"]["Ja"]), STANDING_JA_STEM_COUNTS)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Ja"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Ja"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Ja"], 0)
        self.assertFalse(lock["any_gk_island"])
        self.assertFalse(lock["any_hpq_island"])
        self.assertFalse(lock["any_e_n9"])
        self.assertFalse(lock["any_er7_double"])
        self.assertFalse(lock["any_known_island"])
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertFalse(lock["eightgram_exists"])
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["new_tablet"])
        self.assertTrue(lock["ja_html"])
        self.assertFalse(lock["jb_html"])
        self.assertFalse(lock["jr_html"])
        self.assertFalse(lock["jv_html"])
        self.assertTrue(lock["j_html"])
        self.assertTrue(lock["standing_f_chauvet_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertTrue(lock["standing_d_echancree_vendor_unchanged"])
        self.assertTrue(lock["standing_q_vendor_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_maximals_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_f_chauvet_vendor"]["cycle"], 85)
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["cycle"], 80)
        self.assertEqual(self.survey["tablet_e_keiti_er7_double"]["cycle"], 84)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariReimiroVendorImageSnapshot(unittest.TestCase):
    """Cycle 86 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
