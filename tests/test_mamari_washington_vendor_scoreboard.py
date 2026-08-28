"""Great Washington (S) vendor lock.

Cycle 94 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / F / G / H / I / J / K / L /
M / N / O / P / Q / R. HEAD-check before filename assume (cycle 54
Gr vs Ga; cycle 79 Da vs Dr; cycle 80 Er vs Ea; cycle 85 Fr vs Fa;
cycle 86 Jb vs Ja; cycle 87 Lb vs La; cycle 88 Mb vs Ma; cycle 89
Nr vs Na; cycle 92 Ob vs Oa; cycle 93 Rr vs Ra): Sr.html / Sv.html
are unpublished 404s. S.html is 200 photos-only (no Barthel).
S/index.html names Sa.html / Sb.html (a/b, like A/C/D/F/N/R).
Catalog name is Great Washington — not Vienna / London / Reimiro /
Boomerang / Atua-Mata-Riri. Digits are copied from the snapshots.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. No second new letter.

Locks the vendored sides: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; exact hits of M's n=4
006 022 006 022; exact hits of N's n=6 004 064 034 006 004 064;
S's own longest repeating n-gram (n and whether n≥8 exists). R's
locked facts stay. Claim that can lose: known tradition islands,
E islands, M's n=4, and N's n=6 are exact-0 on S (closed-tradition
hold-out). Longest repeating n=7 is measured, not the claim.

Search lock, not a merge and not a translation. MockProvider only.
"""

import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_atua_vendor_scoreboard import (
    TestMamariAtuaVendorScoreboard,
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

SA_HTML_DIR = Path(__file__).parent / "fixtures" / "washington_sa_html"
SB_HTML_DIR = Path(__file__).parent / "fixtures" / "washington_sb_html"
SA_HTML_PATH = SA_HTML_DIR / "Sa.html"
SB_HTML_PATH = SB_HTML_DIR / "Sb.html"
S_INDEX_HTML_PATH = SA_HTML_DIR / "S_index.html"
SA_JSON_PATH = SA_HTML_DIR / "Sa_barthel.json"
SB_JSON_PATH = SB_HTML_DIR / "Sb_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_S_INDEX_URL = "http://kohaumotu.org/Rongorongo/S/index.html"
CITED_SA_URL = "http://kohaumotu.org/Rongorongo/S/Sa.html"
CITED_SB_URL = "http://kohaumotu.org/Rongorongo/S/Sb.html"
CITED_S_URL = "http://kohaumotu.org/Rongorongo/S/S.html"

SIDE_SA = "Sa"
SIDE_SB = "Sb"
S_SIDES = (SIDE_SA, SIDE_SB)

SA_LINE_NAMES = tuple(f"Sa{n}" for n in range(1, 9))
SB_LINE_NAMES = tuple(f"Sb{n}" for n in range(1, 10))
S_LINE_NAMES = {
    SIDE_SA: SA_LINE_NAMES,
    SIDE_SB: SB_LINE_NAMES,
}

STANDING_SA_BYTES = 6989
STANDING_SB_BYTES = 6731
STANDING_S_INDEX_BYTES = 4187
STANDING_SA_STEM_COUNTS = (42, 44, 46, 52, 55, 67, 52, 22)
STANDING_SB_STEM_COUNTS = (16, 40, 57, 74, 64, 60, 57, 39, 0)
STANDING_STEM_TOTALS = {
    SIDE_SA: 380,
    SIDE_SB: 407,
}
STANDING_STEM_COUNTS = {
    SIDE_SA: STANDING_SA_STEM_COUNTS,
    SIDE_SB: STANDING_SB_STEM_COUNTS,
}
STANDING_S_ALL_LINES = ("Sa.html", "Sb.html")
STANDING_TABLET_S = ("S", "S/index.html", "Great Washington")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in S_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in S_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in S_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in S_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in S_SIDES}
STANDING_M_N4_HITS = {side: 0 for side in S_SIDES}
STANDING_N_N6_HITS = {side: 0 for side in S_SIDES}
STANDING_ANY_GK_ISLAND = False
STANDING_ANY_HPQ_ISLAND = False
STANDING_ANY_E_N9 = False
STANDING_ANY_ER7_DOUBLE = False
STANDING_ANY_M_N4 = False
STANDING_ANY_N_N6 = False
STANDING_ANY_KNOWN_ISLAND = False
STANDING_LONGEST_N = 7
STANDING_LONGEST_NGRAM = ("004", "660", "081", "004", "660", "081", "004")
STANDING_EIGHTGRAM_EXISTS = False
STANDING_EIGHTGRAM_COUNT = 0
STANDING_CLAIM = "known_islands_absent"
STANDING_RESULT = "s_washington_vendored"
STANDING_NEW_TABLET = True
STANDING_SA_HTML = True
STANDING_SB_HTML = True
STANDING_SR_HTML = False
STANDING_SV_HTML = False
STANDING_S_HTML = False
STANDING_S_HTML_HEAD = 200
STANDING_S_HTML_KIND = "photos_only"
UNPUBLISHED_S_PAGES = ("Sr.html", "Sv.html")
NON_BARTHEL_S_PAGES = ("S.html",)


def load_vendored_sa_html() -> str:
    """Return the vendored Kohaumotu Sa.html snapshot."""
    return SA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_sb_html() -> str:
    """Return the vendored Kohaumotu Sb.html snapshot."""
    return SB_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_s_index_html() -> str:
    """Return the vendored Kohaumotu S/index.html snapshot."""
    return S_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_sa_barthel_json() -> dict:
    """Return the vendored parsed Sa Barthel JSON."""
    return json.loads(SA_JSON_PATH.read_text(encoding="utf-8"))


def load_sb_barthel_json() -> dict:
    """Return the vendored parsed Sb Barthel JSON."""
    return json.loads(SB_JSON_PATH.read_text(encoding="utf-8"))


def load_s_sides() -> dict[str, list[list[str]]]:
    """Sa / Sb stems from the vendored parser. No T scrape."""
    return {
        SIDE_SA: side_line_stems(
            extract_published_tokens(load_vendored_sa_html(), SIDE_SA),
            SA_LINE_NAMES,
        ),
        SIDE_SB: side_line_stems(
            extract_published_tokens(load_vendored_sb_html(), SIDE_SB),
            SB_LINE_NAMES,
        ),
    }


def island_hits_by_s_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each S side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in S_SIDES
    }


def unpublished_s_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished or non-Barthel S filenames under fixtures, if any."""
    names = UNPUBLISHED_S_PAGES + NON_BARTHEL_S_PAGES
    return tuple(name for name in names if any(fixtures.glob(f"**/{name}")))


def score_s_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on combined Sa+Sb. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_SA] + by_side[SIDE_SB],
        analyzer,
        line_names=SA_LINE_NAMES + SB_LINE_NAMES,
    )


class TestWashingtonVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; SaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>000!-002-306.003-060-</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>006:700-000!*</td></tr></table>"
        )
        published = extract_published_tokens(html, SIDE_SA)
        self.assertEqual(list(published), ["Sa1", "Sa2"])
        self.assertEqual(published["Sa1"], ["000!", "002", "306.003", "060"])
        self.assertEqual(published["Sa2"], ["006:700", "000!*"])
        stems = side_line_stems(published, ("Sa1", "Sa2"))
        self.assertEqual(stems[0], ["000", "002", "306", "003", "060"])
        self.assertEqual(stems[1], ["006", "700", "000"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {side: [[]] for side in S_SIDES}
        by_side[SIDE_SA] = [list(gram)]
        hits = island_hits_by_s_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_SA][0], 1)
        self.assertEqual(hits[SIDE_SB], (0,) * len(GK_LOCKED_GRAMS))
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_s_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariWashingtonVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → S → Sa/Sb lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.s_index = load_vendored_s_index_html()
        self.by_side = load_s_sides()
        self.gk_hits = island_hits_by_s_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_s_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in S_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in S_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in S_SIDES
        }
        self.m_n4_hits = {
            side: ngram_hit_count(self.by_side[side], M_N4_GRAM) for side in S_SIDES
        }
        self.n_n6_hits = {
            side: ngram_hit_count(self.by_side[side], N_N6_GRAM) for side in S_SIDES
        }
        self.profile = score_s_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_s(self):
        """Catalog → tablets → S index → Sa/Sb. Not Sr, Sv, or S.html Barthel."""
        self.assertTrue(SA_HTML_PATH.is_file())
        self.assertTrue(SB_HTML_PATH.is_file())
        self.assertTrue(SA_JSON_PATH.is_file())
        self.assertTrue(SB_JSON_PATH.is_file())
        self.assertTrue((SA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((SB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(S_INDEX_HTML_PATH.is_file())
        self.assertFalse((SA_HTML_DIR / "Sr.html").exists())
        self.assertFalse((SA_HTML_DIR / "Sv.html").exists())
        self.assertFalse((SA_HTML_DIR / "S.html").exists())
        self.assertFalse((SB_HTML_DIR / "Sr.html").exists())
        self.assertFalse((SB_HTML_DIR / "S.html").exists())
        self.assertEqual(STANDING_SA_HTML, True)
        self.assertEqual(STANDING_SB_HTML, True)
        self.assertEqual(STANDING_SR_HTML, False)
        self.assertEqual(STANDING_SV_HTML, False)
        self.assertEqual(STANDING_S_HTML, False)
        self.assertEqual(STANDING_S_HTML_HEAD, 200)
        self.assertEqual(STANDING_S_HTML_KIND, "photos_only")
        self.assertEqual(SA_HTML_PATH.stat().st_size, STANDING_SA_BYTES)
        self.assertEqual(SB_HTML_PATH.stat().st_size, STANDING_SB_BYTES)
        self.assertEqual(S_INDEX_HTML_PATH.stat().st_size, STANDING_S_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "S"), STANDING_TABLET_S)
        self.assertEqual(published_all_lines_hrefs(self.s_index), STANDING_S_ALL_LINES)
        self.assertIn("Item S:The Great Washington tablet", self.s_index)
        self.assertIn('href="Sa.html"', self.s_index)
        self.assertIn('href="Sb.html"', self.s_index)
        self.assertIn('href="S.html"', self.s_index)
        self.assertIn("Photos of complete item", self.s_index)
        self.assertNotIn('href="Sr.html"', self.s_index)
        self.assertNotIn('href="Sv.html"', self.s_index)
        sa = load_vendored_sa_html()
        sb = load_vendored_sb_html()
        self.assertIn("Item S:The Great Washington Tablet", sa)
        self.assertIn("Item S:The Great Washington Tablet", sb)
        self.assertIn("Rongorongo Sa", sa)
        self.assertIn("Rongorongo Sb", sb)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', sa)
        self.assertIn('<h3><a name="Line_8">Line 8</a></h3>', sa)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', sb)
        self.assertIn('<h3><a name="Line_9">Line 9</a></h3>', sb)
        self.assertIn("000!-739.022f-062.001-053-015.063.003-046-110-002-060-001V-280-", sa)
        self.assertIn("000!-000!-004.064-011-006.000!-005-001-005-000!.006-070-200-", sb)
        self.assertEqual(extract_published_tokens("<h1>photos</h1>", SIDE_SA), {})
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_s_html_names(fixtures), ())
        for directory, urls in (
            (
                SA_HTML_DIR,
                (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_S_INDEX_URL, CITED_SA_URL),
            ),
            (SB_HTML_DIR, (CITED_SB_URL, CITED_S_INDEX_URL)),
        ):
            text = (directory / "ATTRIBUTION").read_text(encoding="utf-8")
            for url in urls:
                self.assertIn(url, text)
            self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
            self.assertIn("tablet T", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        sa_json = load_sa_barthel_json()
        sb_json = load_sb_barthel_json()
        sa_pub = extract_published_tokens(load_vendored_sa_html(), SIDE_SA)
        sb_pub = extract_published_tokens(load_vendored_sb_html(), SIDE_SB)
        self.assertEqual(sa_json["tablet"], "S")
        self.assertEqual(sb_json["tablet"], "S")
        self.assertEqual(sa_json["side"], SIDE_SA)
        self.assertEqual(sb_json["side"], SIDE_SB)
        self.assertEqual(sa_json["name"], "Great Washington")
        self.assertEqual(sb_json["name"], "Great Washington")
        self.assertEqual(sa_json["source"]["url"], CITED_SA_URL)
        self.assertEqual(sb_json["source"]["url"], CITED_SB_URL)
        for name in SA_LINE_NAMES:
            self.assertEqual(sa_json["lines"][name], sa_pub[name])
            self.assertEqual(
                sa_json["stems"][name],
                self.by_side[SIDE_SA][int(name[2:]) - 1],
            )
        for name in SB_LINE_NAMES:
            self.assertEqual(sb_json["lines"][name], sb_pub[name])
            self.assertEqual(
                sb_json["stems"][name],
                self.by_side[SIDE_SB][int(name[2:]) - 1],
            )
        self.assertEqual(sa_json["lines"]["Sa1"][0], "…000!")
        self.assertEqual(sa_json["stems"]["Sa1"][0], "739")
        self.assertEqual(sa_json["lines"]["Sa1"][1], "739.022f")
        self.assertEqual(sa_json["stems"]["Sa1"][0:2], ["739", "022"])
        self.assertEqual(len(sa_json["lines"]["Sa1"]), 35)
        self.assertEqual(len(sa_json["stems"]["Sa1"]), 42)
        self.assertEqual(sa_json["lines"]["Sa1"][12], "004.064")
        self.assertEqual(sa_json["stems"]["Sa1"][16:20], ["004", "064", "745", "001"])
        self.assertEqual(sa_json["lines"]["Sa6"][0], "…000!.044")
        self.assertEqual(sa_json["stems"]["Sa6"][0], "044")
        self.assertEqual(sb_json["lines"]["Sb1"][2], "004.064")
        self.assertEqual(sb_json["stems"]["Sb1"][1:3], ["004", "064"])
        self.assertEqual(sb_json["stems"]["Sb2"][15:22], list(STANDING_LONGEST_NGRAM))
        self.assertEqual(sb_json["lines"]["Sb9"], ["(30", "50)!"])
        self.assertEqual(sb_json["stems"]["Sb9"], [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E, Er7, M n=4, N n=6 are 0."""
        for side in S_SIDES:
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

    def test_longest_repeating_ngram_is_7(self):
        """S's own repeating profile: longest n=7; no n≥8. Not the claim."""
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest_n, 7)
        self.assertEqual(len(self.profile.longest), 1)
        self.assertEqual(self.profile.longest[0].tokens, STANDING_LONGEST_NGRAM)
        self.assertEqual(self.profile.longest[0].freq, 2)
        self.assertFalse(any(row.n >= 8 for row in self.profile.rows))
        self.assertFalse(STANDING_EIGHTGRAM_EXISTS)
        self.assertEqual(len(self.profile.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.profile.eightgrams, ())
        self.assertIsNone(self.profile.top_8gram)
        self.assertEqual(STANDING_LONGEST_NGRAM, ("004", "660", "081", "004", "660", "081", "004"))
        self.assertNotEqual(STANDING_CLAIM, "no_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_r_atua_scoreboard_still_computes(self):
        """Cycle 93 R vendor lock stays."""
        prior = TestMamariAtuaVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_known_islands_absent()
        prior.test_longest_repeating_ngram_has_no_4gram()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-94 S vendor lock."""
        lock = self.survey["tablet_s_washington_vendor"]
        self.assertEqual(lock["cycle"], 94)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_s"], "S")
        self.assertEqual(lock["name_s"], "Great Washington")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["s_index"], CITED_S_INDEX_URL)
        self.assertEqual(lock["sa_page"], CITED_SA_URL)
        self.assertEqual(lock["sb_page"], CITED_SB_URL)
        self.assertNotIn(CITED_S_URL, (lock["sa_page"], lock["sb_page"], lock["s_index"]))
        self.assertEqual(tuple(lock["s_pages"]), STANDING_S_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Sa"], STANDING_SA_BYTES)
        self.assertEqual(lock["html_bytes"]["Sb"], STANDING_SB_BYTES)
        self.assertEqual(lock["stem_totals"]["Sa"], STANDING_STEM_TOTALS[SIDE_SA])
        self.assertEqual(lock["stem_totals"]["Sb"], STANDING_STEM_TOTALS[SIDE_SB])
        self.assertEqual(tuple(lock["stem_counts"]["Sa"]), STANDING_SA_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Sb"]), STANDING_SB_STEM_COUNTS)
        self.assertEqual(tuple(lock["lines"]["Sa"]), SA_LINE_NAMES)
        self.assertEqual(tuple(lock["lines"]["Sb"]), SB_LINE_NAMES)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Sa"], 0)
        self.assertEqual(lock["e_n9_hits"]["Sb"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Sa"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Sb"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Sa"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Sb"], 0)
        self.assertEqual(lock["m_n4_hits"]["Sa"], 0)
        self.assertEqual(lock["m_n4_hits"]["Sb"], 0)
        self.assertEqual(lock["n_n6_hits"]["Sa"], 0)
        self.assertEqual(lock["n_n6_hits"]["Sb"], 0)
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
        self.assertTrue(lock["sa_html"])
        self.assertTrue(lock["sb_html"])
        self.assertFalse(lock["sr_html"])
        self.assertFalse(lock["sv_html"])
        self.assertFalse(lock["s_html"])
        self.assertEqual(lock["s_html_head"], STANDING_S_HTML_HEAD)
        self.assertEqual(lock["s_html_kind"], STANDING_S_HTML_KIND)
        self.assertTrue(lock["standing_r_atua_vendor_unchanged"])
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
        self.assertEqual(self.survey["tablet_r_atua_vendor"]["cycle"], 93)
        self.assertEqual(self.survey["tablet_o_boomerang_vendor"]["cycle"], 92)
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["cycle"], 89)
        self.assertEqual(tuple(self.survey["tablet_n_vienna_vendor"]["longest_tokens"]), N_N6_GRAM)
        self.assertEqual(self.survey["tablet_m_vienna_vendor"]["cycle"], 88)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariWashingtonVendorImageSnapshot(unittest.TestCase):
    """Cycle 94 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
