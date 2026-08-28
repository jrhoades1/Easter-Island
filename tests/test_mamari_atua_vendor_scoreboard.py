"""Atua-Mata-Riri (R) vendor lock.

Cycle 93 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / L /
M / N / O / P / Q. HEAD-check before filename assume (cycle 54 Gr vs
Ga; cycle 79 Da vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs Fa; cycle 86
Jb vs Ja; cycle 87 Lb vs La; cycle 88 Mb vs Ma; cycle 89 Nr vs Na;
cycle 92 Ob vs Oa): Rr.html / Rv.html / R.html are unpublished 404s.
R/index.html names Ra.html / Rb.html (a/b, like A/C/D/F/N). Catalog
name is Atua-Mata-Riri — not Vienna / London / Reimiro / Boomerang.
Digits are copied from the snapshots. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No new
agents. No second new letter.

Locks the vendored sides: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; exact hits of M's n=4
006 022 006 022; exact hits of N's n=6 004 064 034 006 004 064;
R's own longest repeating n-gram (n and whether n≥8 exists). O's
locked facts stay. Claim that can lose: known tradition islands,
E islands, M's n=4, and N's n=6 are exact-0 on R (closed-tradition
hold-out). R has no repeating n≥4, so the hold-out is the lock
that can leak.

Search lock, not a merge and not a translation. MockProvider only.
"""

import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_boomerang_vendor_scoreboard import (
    TestMamariBoomerangVendorScoreboard,
)
from tests.test_mamari_gk_islands_off_hpq_scoreboard import (
    LOCKED_GRAMS as GK_LOCKED_GRAMS,
)
from tests.test_mamari_hpq_island_off_hpq_scoreboard import (
    LOCKED_ISLANDS as HPQ_LOCKED_ISLANDS,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
    GRAM4 as ER7_GRAM4,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
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
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_tahua_aa_scoreboard import load_vendored_tablets_html
from tests.test_mamari_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
)

RA_HTML_DIR = Path(__file__).parent / "fixtures" / "atua_ra_html"
RB_HTML_DIR = Path(__file__).parent / "fixtures" / "atua_rb_html"
RA_HTML_PATH = RA_HTML_DIR / "Ra.html"
RB_HTML_PATH = RB_HTML_DIR / "Rb.html"
R_INDEX_HTML_PATH = RA_HTML_DIR / "R_index.html"
RA_JSON_PATH = RA_HTML_DIR / "Ra_barthel.json"
RB_JSON_PATH = RB_HTML_DIR / "Rb_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_R_INDEX_URL = "http://kohaumotu.org/Rongorongo/R/index.html"
CITED_RA_URL = "http://kohaumotu.org/Rongorongo/R/Ra.html"
CITED_RB_URL = "http://kohaumotu.org/Rongorongo/R/Rb.html"

SIDE_RA = "Ra"
SIDE_RB = "Rb"
R_SIDES = (SIDE_RA, SIDE_RB)

RA_LINE_NAMES = tuple(f"Ra{n}" for n in range(1, 9))
RB_LINE_NAMES = tuple(f"Rb{n}" for n in range(1, 10))
R_LINE_NAMES = {
    SIDE_RA: RA_LINE_NAMES,
    SIDE_RB: RB_LINE_NAMES,
}

STANDING_RA_BYTES = 3948
STANDING_RB_BYTES = 4057
STANDING_R_INDEX_BYTES = 4111
STANDING_RA_STEM_COUNTS = (28, 35, 38, 41, 35, 41, 31, 17)
STANDING_RB_STEM_COUNTS = (15, 27, 20, 27, 34, 43, 35, 23, 0)
STANDING_STEM_TOTALS = {
    SIDE_RA: 266,
    SIDE_RB: 224,
}
STANDING_STEM_COUNTS = {
    SIDE_RA: STANDING_RA_STEM_COUNTS,
    SIDE_RB: STANDING_RB_STEM_COUNTS,
}
STANDING_R_ALL_LINES = ("Ra.html", "Rb.html")
STANDING_TABLET_R = ("R", "R/index.html", "Atua-Mata-Riri")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in R_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in R_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in R_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in R_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in R_SIDES}
STANDING_M_N4_HITS = {side: 0 for side in R_SIDES}
STANDING_N_N6_HITS = {side: 0 for side in R_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_M_N4 = False
STANDING_ANY_N_N6 = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 0
STANDING_LONGEST_NGRAM = ()
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "r_atua_vendored"
STANDING_NEW_TABLET = True
STANDING_RA_HTML = True
STANDING_RB_HTML = True
STANDING_RR_HTML = False
STANDING_RV_HTML = False
STANDING_R_HTML = False
UNPUBLISHED_R_PAGES = ("Rr.html", "Rv.html", "R.html")


def load_vendored_ra_html() -> str:
    """Return the vendored Kohaumotu Ra.html snapshot."""
    return RA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_rb_html() -> str:
    """Return the vendored Kohaumotu Rb.html snapshot."""
    return RB_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_r_index_html() -> str:
    """Return the vendored Kohaumotu R/index.html snapshot."""
    return R_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_ra_barthel_json() -> dict:
    """Return the vendored parsed Ra Barthel JSON."""
    return json.loads(RA_JSON_PATH.read_text(encoding="utf-8"))


def load_rb_barthel_json() -> dict:
    """Return the vendored parsed Rb Barthel JSON."""
    return json.loads(RB_JSON_PATH.read_text(encoding="utf-8"))


def load_r_sides() -> dict[str, list[list[str]]]:
    """Ra / Rb stems from the vendored parser. No S scrape."""
    return {
        SIDE_RA: side_line_stems(
            extract_published_tokens(load_vendored_ra_html(), SIDE_RA),
            RA_LINE_NAMES,
        ),
        SIDE_RB: side_line_stems(
            extract_published_tokens(load_vendored_rb_html(), SIDE_RB),
            RB_LINE_NAMES,
        ),
    }


def island_hits_by_r_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each R side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in R_SIDES
    }


def unpublished_r_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished R Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_R_PAGES if any(fixtures.glob(f"**/{name}")))


def score_r_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on combined Ra+Rb. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_RA] + by_side[SIDE_RB],
        analyzer,
        line_names=RA_LINE_NAMES + RB_LINE_NAMES,
    )


class TestAtuaVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; RaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>000!-002-306.003-060-</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>006:700-000!*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_RA)
        self.assertEqual(list(published), ["Ra1", "Ra2"])
        self.assertEqual(published["Ra1"], ["000!", "002", "306.003", "060"])
        self.assertEqual(published["Ra2"], ["006:700", "000!*"])
        stems = side_line_stems(published, ("Ra1", "Ra2"))
        self.assertEqual(stems[0], ["000", "002", "306", "003", "060"])
        self.assertEqual(stems[1], ["006", "700", "000"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {side: [[]] for side in R_SIDES}
        by_side[SIDE_RA] = [list(gram)]
        hits = island_hits_by_r_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_RA][0], 1)
        self.assertEqual(hits[SIDE_RB], (0,) * len(GK_LOCKED_GRAMS))
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_r_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariAtuaVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → R → Ra/Rb lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.r_index = load_vendored_r_index_html()
        self.by_side = load_r_sides()
        self.gk_hits = island_hits_by_r_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_r_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in R_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in R_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in R_SIDES
        }
        self.m_n4_hits = {
            side: ngram_hit_count(self.by_side[side], M_N4_GRAM) for side in R_SIDES
        }
        self.n_n6_hits = {
            side: ngram_hit_count(self.by_side[side], N_N6_GRAM) for side in R_SIDES
        }
        self.profile = score_r_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_r(self):
        """Catalog → tablets → R index → Ra/Rb. Not Rr, Rv, or R.html."""
        self.assertTrue(RA_HTML_PATH.is_file())
        self.assertTrue(RB_HTML_PATH.is_file())
        self.assertTrue(RA_JSON_PATH.is_file())
        self.assertTrue(RB_JSON_PATH.is_file())
        self.assertTrue((RA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((RB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(R_INDEX_HTML_PATH.is_file())
        self.assertFalse((RA_HTML_DIR / "Rr.html").exists())
        self.assertFalse((RA_HTML_DIR / "Rv.html").exists())
        self.assertFalse((RA_HTML_DIR / "R.html").exists())
        self.assertFalse((RB_HTML_DIR / "Rr.html").exists())
        self.assertEqual(STANDING_RA_HTML, True)
        self.assertEqual(STANDING_RB_HTML, True)
        self.assertEqual(STANDING_RR_HTML, False)
        self.assertEqual(STANDING_RV_HTML, False)
        self.assertEqual(STANDING_R_HTML, False)
        self.assertEqual(RA_HTML_PATH.stat().st_size, STANDING_RA_BYTES)
        self.assertEqual(RB_HTML_PATH.stat().st_size, STANDING_RB_BYTES)
        self.assertEqual(R_INDEX_HTML_PATH.stat().st_size, STANDING_R_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "R"), STANDING_TABLET_R)
        self.assertEqual(published_all_lines_hrefs(self.r_index), STANDING_R_ALL_LINES)
        self.assertIn("Item R:Atua-Mata-Riri", self.r_index)
        self.assertIn('href="Ra.html"', self.r_index)
        self.assertIn('href="Rb.html"', self.r_index)
        self.assertNotIn('href="Rr.html"', self.r_index)
        self.assertNotIn('href="Rv.html"', self.r_index)
        self.assertNotIn('href="R.html"', self.r_index)
        ra = load_vendored_ra_html()
        rb = load_vendored_rb_html()
        self.assertIn("Item R:Tablet Atua-Mata-Riri", ra)
        self.assertIn("Item R:Tablet Atua-Mata-Riri", rb)
        self.assertIn("Rongorongo Ra", ra)
        self.assertIn("Rongorongo Rb", rb)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', ra)
        self.assertIn('<h3><a name="Line_8">Line 8</a></h3>', ra)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', rb)
        self.assertIn('<h3><a name="Line_9">Line 9</a></h3>', rb)
        self.assertIn("000!-002-306.003-060-280-301-020-020V-048-049f-200.200.200-", ra)
        self.assertIn("000!-206?-007-306.003-", rb)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_r_html_names(fixtures), ())
        for directory, urls in (
            (
                RA_HTML_DIR,
                (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_R_INDEX_URL, CITED_RA_URL),
            ),
            (RB_HTML_DIR, (CITED_RB_URL, CITED_R_INDEX_URL)),
        ):
            text = (directory / "ATTRIBUTION").read_text(encoding="utf-8")
            for url in urls:
                self.assertIn(url, text)
            self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
            self.assertIn("tablet S", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        ra_json = load_ra_barthel_json()
        rb_json = load_rb_barthel_json()
        ra_pub = extract_published_tokens(load_vendored_ra_html(), SIDE_RA)
        rb_pub = extract_published_tokens(load_vendored_rb_html(), SIDE_RB)
        self.assertEqual(ra_json["tablet"], "R")
        self.assertEqual(rb_json["tablet"], "R")
        self.assertEqual(ra_json["side"], SIDE_RA)
        self.assertEqual(rb_json["side"], SIDE_RB)
        self.assertEqual(ra_json["name"], "Atua-Mata-Riri")
        self.assertEqual(rb_json["name"], "Atua-Mata-Riri")
        self.assertEqual(ra_json["source"]["url"], CITED_RA_URL)
        self.assertEqual(rb_json["source"]["url"], CITED_RB_URL)
        for name in RA_LINE_NAMES:
            self.assertEqual(ra_json["lines"][name], ra_pub[name])
            self.assertEqual(
                ra_json["stems"][name],
                self.by_side[SIDE_RA][int(name[2:]) - 1],
            )
        for name in RB_LINE_NAMES:
            self.assertEqual(rb_json["lines"][name], rb_pub[name])
            self.assertEqual(
                rb_json["stems"][name],
                self.by_side[SIDE_RB][int(name[2:]) - 1],
            )
        self.assertEqual(ra_json["lines"]["Ra1"][0], "000!")
        self.assertEqual(ra_json["stems"]["Ra1"][0], "000")
        self.assertEqual(ra_json["lines"]["Ra1"][2], "306.003")
        self.assertEqual(ra_json["stems"]["Ra1"][2:4], ["306", "003"])
        self.assertEqual(len(ra_json["lines"]["Ra1"]), 25)
        self.assertEqual(len(ra_json["stems"]["Ra1"]), 28)
        self.assertEqual(ra_json["lines"]["Ra4"][21], "004.064.254.004.064")
        self.assertEqual(ra_json["stems"]["Ra4"][31:36], ["004", "064", "254", "004", "064"])
        self.assertEqual(ra_json["lines"]["Ra5"][16], "006:700")
        self.assertEqual(ra_json["stems"]["Ra5"][17:19], ["006", "700"])
        self.assertEqual(rb_json["lines"]["Rb1"][6], "043:001?")
        self.assertEqual(rb_json["stems"]["Rb1"][8:10], ["043", "001"])
        self.assertEqual(rb_json["lines"]["Rb9"], ["(10", "25)!"])
        self.assertEqual(rb_json["stems"]["Rb9"], [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E, Er7, M n=4, N n=6 are 0."""
        for side in R_SIDES:
            counts = [len(line) for line in self.by_side[side]]
            self.assertEqual(counts, list(STANDING_STEM_COUNTS[side]))
            self.assertEqual(sum(counts), STANDING_STEM_TOTALS[side])
            self.assertEqual(self.gk_hits[side], STANDING_GK_ISLAND_HITS[side])
            self.assertEqual(self.hpq_hits[side], STANDING_HPQ_ISLAND_HITS[side])
            self.assertEqual(self.e_n9_hits[side], STANDING_E_N9_HITS[side])
            self.assertEqual(self.er7_4_hits[side], STANDING_ER7_4_HITS[side])
            self.assertEqual(self.er7_8_hits[side], STANDING_ER7_8_HITS[side])
            self.assertEqual(self.m_n4_hits[side], STANDING_M_N4_HITS[side])
            self.assertEqual(self.n_n6_hits[side], STANDING_N_N6_HITS[side])
            for gram, count in zip(GK_LOCKED_GRAMS, self.gk_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            for gram, count in zip(HPQ_LOCKED_ISLANDS, self.hpq_hits[side]):
                self.assertEqual(count, ngram_hit_count(self.by_side[side], gram))
                self.assertEqual(count, 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], E_GRAM_N9), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], ER7_GRAM4), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], ER7_GRAM8), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], M_N4_GRAM), 0)
            self.assertEqual(ngram_hit_count(self.by_side[side], N_N6_GRAM), 0)
        self.assertFalse(any(any(hits) for hits in self.gk_hits.values()))
        self.assertFalse(any(any(hits) for hits in self.hpq_hits.values()))
        self.assertFalse(any(self.e_n9_hits.values()))
        self.assertFalse(any(self.er7_4_hits.values()))
        self.assertFalse(any(self.er7_8_hits.values()))
        self.assertFalse(any(self.m_n4_hits.values()))
        self.assertFalse(any(self.n_n6_hits.values()))
        self.assertEqual(STANDING_ANY_GK_ISLAND, False)
        self.assertEqual(STANDING_ANY_HPQ_ISLAND, False)
        self.assertEqual(STANDING_ANY_E_N9, False)
        self.assertEqual(STANDING_ANY_ER7_DOUBLE, False)
        self.assertEqual(STANDING_ANY_M_N4, False)
        self.assertEqual(STANDING_ANY_N_N6, False)
        self.assertEqual(STANDING_ANY_KNOWN_ISLAND, False)
        self.assertEqual(STANDING_CLAIM, "known_islands_absent")
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(N_N6_GRAM, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_repeating_ngram_has_no_4gram(self):
        """R's own repeating profile: longest n=0; no n≥4 freq≥2. Not the claim."""
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

    def test_existing_o_boomerang_scoreboard_still_computes(self):
        """Cycle 92 O vendor lock stays."""
        prior = TestMamariBoomerangVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_4gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-93 R vendor lock."""
        lock = self.survey["tablet_r_atua_vendor"]
        self.assertEqual(lock["cycle"], 93)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_r"], "R")
        self.assertEqual(lock["name_r"], "Atua-Mata-Riri")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["r_index"], CITED_R_INDEX_URL)
        self.assertEqual(lock["ra_page"], CITED_RA_URL)
        self.assertEqual(lock["rb_page"], CITED_RB_URL)
        self.assertEqual(tuple(lock["r_pages"]), STANDING_R_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Ra"], STANDING_RA_BYTES)
        self.assertEqual(lock["html_bytes"]["Rb"], STANDING_RB_BYTES)
        self.assertEqual(lock["stem_totals"]["Ra"], STANDING_STEM_TOTALS[SIDE_RA])
        self.assertEqual(lock["stem_totals"]["Rb"], STANDING_STEM_TOTALS[SIDE_RB])
        self.assertEqual(tuple(lock["stem_counts"]["Ra"]), STANDING_RA_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Rb"]), STANDING_RB_STEM_COUNTS)
        self.assertEqual(tuple(lock["lines"]["Ra"]), RA_LINE_NAMES)
        self.assertEqual(tuple(lock["lines"]["Rb"]), RB_LINE_NAMES)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Ra"], 0)
        self.assertEqual(lock["e_n9_hits"]["Rb"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Ra"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Rb"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Ra"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Rb"], 0)
        self.assertEqual(lock["m_n4_hits"]["Ra"], 0)
        self.assertEqual(lock["m_n4_hits"]["Rb"], 0)
        self.assertEqual(lock["n_n6_hits"]["Ra"], 0)
        self.assertEqual(lock["n_n6_hits"]["Rb"], 0)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertEqual(tuple(lock["n_n6_tokens"]), N_N6_GRAM)
        self.assertFalse(lock["any_gk_island"])
        self.assertFalse(lock["any_hpq_island"])
        self.assertFalse(lock["any_e_n9"])
        self.assertFalse(lock["any_er7_double"])
        self.assertFalse(lock["any_m_n4"])
        self.assertFalse(lock["any_n_n6"])
        self.assertFalse(lock["any_known_island"])
        self.assertEqual(lock["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(tuple(lock["longest_tokens"]), STANDING_LONGEST_NGRAM)
        self.assertFalse(lock["eightgram_exists"])
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["new_tablet"])
        self.assertTrue(lock["ra_html"])
        self.assertTrue(lock["rb_html"])
        self.assertFalse(lock["rr_html"])
        self.assertFalse(lock["rv_html"])
        self.assertFalse(lock["r_html"])
        self.assertTrue(lock["standing_o_boomerang_vendor_unchanged"])
        self.assertTrue(lock["standing_n_vienna_na1_n_only_unchanged"])
        self.assertTrue(lock["standing_n_vienna_vendor_unchanged"])
        self.assertTrue(lock["standing_m_vienna_ma2_m_only_unchanged"])
        self.assertTrue(lock["standing_m_vienna_vendor_unchanged"])
        self.assertTrue(lock["standing_l_reimiro_vendor_unchanged"])
        self.assertTrue(lock["standing_j_reimiro_vendor_unchanged"])
        self.assertTrue(lock["standing_f_chauvet_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertTrue(lock["standing_d_echancree_vendor_unchanged"])
        self.assertTrue(lock["standing_q_vendor_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_maximals_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_o_boomerang_vendor"]["cycle"], 92)
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["cycle"], 89)
        self.assertEqual(tuple(self.survey["tablet_n_vienna_vendor"]["longest_tokens"]), N_N6_GRAM)
        self.assertEqual(self.survey["tablet_m_vienna_vendor"]["cycle"], 88)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariAtuaVendorImageSnapshot(unittest.TestCase):
    """Cycle 93 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
