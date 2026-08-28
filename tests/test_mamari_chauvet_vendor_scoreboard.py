"""Chauvet fragment (F) vendor lock.

Cycle 85 text-search lock. Same already-vendored Kohaumotu catalog /
tablets.html used for A / B / C / D / E / G / H / I / K / P / Q.
HEAD-check before filename assume (cycle 54 Gr vs Ga; cycle 79 Da
vs Dr; cycle 80 Er vs Ea): Fr.html / Fv.html / F.html are
unpublished 404s. F/index.html names Fa.html / Fb.html (a/b, like
A/C/D). Digits are copied from the snapshots. Fb.html uses
published Side b, line N headers, not Line_N anchors. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. No second new letter.

Locks per vendored side: stem count; exact hits of the six cycle-67
G–K islands plus the cycle-76 n=25; exact hits of the five cycle-71
H∩P∩Q n≥8 islands; exact hits of the cycle-81 E n=9 and the
cycle-84 Er7 doubled 4-gram; F's own longest repeating n-gram
(n and whether n≥8 exists). E's locked facts stay. Claim that
can lose: known tradition islands and E islands are exact-0 on F
(closed-tradition hold-out). F is short (longest n=0; no n≥4
freq≥2), so the hold-out is the lock that can leak.

Search lock, not a merge and not a translation. MockProvider only.
"""

import json
import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_gk_islands_off_hpq_scoreboard import (
    LOCKED_GRAMS as GK_LOCKED_GRAMS,
)
from tests.test_mamari_hpq_island_off_hpq_scoreboard import (
    LOCKED_ISLANDS as HPQ_LOCKED_ISLANDS,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
    GRAM4 as ER7_GRAM4,
    GRAM8 as ER7_GRAM8,
    TestMamariKeitiEr7DoubleScoreboard,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    GRAM_N9 as E_GRAM_N9,
)
from tests.test_mamari_keiti_vendor_scoreboard import (
    TestMamariKeitiVendorScoreboard,
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

FA_HTML_DIR = Path(__file__).parent / "fixtures" / "chauvet_fa_html"
FB_HTML_DIR = Path(__file__).parent / "fixtures" / "chauvet_fb_html"
FA_HTML_PATH = FA_HTML_DIR / "Fa.html"
FB_HTML_PATH = FB_HTML_DIR / "Fb.html"
F_INDEX_HTML_PATH = FA_HTML_DIR / "F_index.html"
FA_JSON_PATH = FA_HTML_DIR / "Fa_barthel.json"
FB_JSON_PATH = FB_HTML_DIR / "Fb_barthel.json"

CITED_CATALOG_URL = "http://kohaumotu.org/Rongorongo/"
CITED_TABLETS_URL = "http://kohaumotu.org/Rongorongo/tablets.html"
CITED_F_INDEX_URL = "http://kohaumotu.org/Rongorongo/F/index.html"
CITED_FA_URL = "http://kohaumotu.org/Rongorongo/F/Fa.html"
CITED_FB_URL = "http://kohaumotu.org/Rongorongo/F/Fb.html"

SIDE_FA = "Fa"
SIDE_FB = "Fb"
F_SIDES = (SIDE_FA, SIDE_FB)

FA_LINE_NAMES = tuple(f"Fa{n}" for n in range(1, 7))
FB_LINE_NAMES = tuple(f"Fb{n}" for n in range(1, 5))
F_LINE_NAMES = {
    SIDE_FA: FA_LINE_NAMES,
    SIDE_FB: FB_LINE_NAMES,
}

STANDING_FA_BYTES = 1963
STANDING_FB_BYTES = 1438
STANDING_F_INDEX_BYTES = 3597
STANDING_FA_STEM_COUNTS = (4, 10, 12, 10, 8, 0)
STANDING_FB_STEM_COUNTS = (0, 1, 9, 2)
STANDING_STEM_TOTALS = {
    SIDE_FA: 44,
    SIDE_FB: 12,
}
STANDING_STEM_COUNTS = {
    SIDE_FA: STANDING_FA_STEM_COUNTS,
    SIDE_FB: STANDING_FB_STEM_COUNTS,
}
STANDING_F_ALL_LINES = ("Fa.html", "Fb.html")
STANDING_TABLET_F = ("F", "F/index.html", "Stephen-Chauvet Fragment")
STANDING_GK_ISLAND_HITS = {
    side: (0,) * len(GK_LOCKED_GRAMS) for side in F_SIDES
}
STANDING_HPQ_ISLAND_HITS = {
    side: (0,) * len(HPQ_LOCKED_ISLANDS) for side in F_SIDES
}
STANDING_E_N9_HITS = {side: 0 for side in F_SIDES}
STANDING_ER7_4_HITS = {side: 0 for side in F_SIDES}
STANDING_ER7_8_HITS = {side: 0 for side in F_SIDES}
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
STANDING_RESULT = "f_chauvet_vendored"
STANDING_NEW_TABLET = True
STANDING_FR_HTML = False
STANDING_FV_HTML = False
STANDING_F_HTML = False
UNPUBLISHED_F_PAGES = ("F.html", "Fr.html", "Fv.html")

_FB_LINE_HEADER = re.compile(r"<h3>Side [ab], line (\d+)</h3>")


def load_vendored_fa_html() -> str:
    """Return the vendored Kohaumotu Fa.html snapshot."""
    return FA_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_fb_html() -> str:
    """Return the vendored Kohaumotu Fb.html snapshot."""
    return FB_HTML_PATH.read_text(encoding="utf-8")


def load_vendored_f_index_html() -> str:
    """Return the vendored Kohaumotu F/index.html snapshot."""
    return F_INDEX_HTML_PATH.read_text(encoding="utf-8")


def load_fa_barthel_json() -> dict:
    """Return the vendored parsed Fa Barthel JSON."""
    return json.loads(FA_JSON_PATH.read_text(encoding="utf-8"))


def load_fb_barthel_json() -> dict:
    """Return the vendored parsed Fb Barthel JSON."""
    return json.loads(FB_JSON_PATH.read_text(encoding="utf-8"))


def extract_fb_published_tokens(html: str, prefix: str = SIDE_FB) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Fb Side b, line N markup.

    Fb.html has no Line_N anchors. Digits still sit in <td> text.
    Does not invent numbers.
    """
    chunks = _FB_LINE_HEADER.split(html)
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


def extract_f_published_tokens(html: str, prefix: str) -> dict[str, list[str]]:
    """Fa uses Line_N; Fb uses Side b, line N. Shared parser first."""
    published = extract_published_tokens(html, prefix)
    if published:
        return published
    return extract_fb_published_tokens(html, prefix)


def load_f_sides() -> dict[str, list[list[str]]]:
    """Fa / Fb stems from the vendored parsers. No J scrape."""
    return {
        SIDE_FA: side_line_stems(
            extract_f_published_tokens(load_vendored_fa_html(), SIDE_FA),
            FA_LINE_NAMES,
        ),
        SIDE_FB: side_line_stems(
            extract_f_published_tokens(load_vendored_fb_html(), SIDE_FB),
            FB_LINE_NAMES,
        ),
    }


def island_hits_by_f_side(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...],
) -> dict[str, tuple[int, ...]]:
    """Exact island hits on each F side. Search only."""
    return {
        side: tuple(ngram_hit_count(by_side[side], gram) for gram in grams)
        for side in F_SIDES
    }


def unpublished_f_html_names(fixtures: Path) -> tuple[str, ...]:
    """Unpublished F Barthel filenames under fixtures, if any."""
    return tuple(name for name in UNPUBLISHED_F_PAGES if any(fixtures.glob(f"**/{name}")))


def score_f_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on combined Fa+Fb. Search only."""
    lines = by_side[SIDE_FA] + by_side[SIDE_FB]
    names = FA_LINE_NAMES + FB_LINE_NAMES
    return score_remainder_repeating_ngrams(lines, analyzer, line_names=names)


class TestChauvetVendorHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; FaN names stay."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>300!-685!-073f!-005!-(3-5)!*</td></tr></table>"
            '<h3><a name="Line_6">Line 6</a></h3>'
            "<table><tr><td>(2-3)!*</td></tr>"
            "<tr><td>*</td></tr></table>"
        )
        published = extract_f_published_tokens(html, SIDE_FA)
        self.assertEqual(list(published), ["Fa1", "Fa6"])
        self.assertEqual(published["Fa1"], ["300!", "685!", "073f!", "005!", "(3", "5)!*"])
        self.assertEqual(published["Fa6"], ["(2", "3)!*"])
        stems = side_line_stems(published, ("Fa1", "Fa6"))
        self.assertEqual(stems[0], ["300", "685", "073", "005"])
        self.assertEqual(stems[1], [])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_fb_side_b_line_headers_are_published_not_line_n(self):
        """Fb.html has no Line_N anchors; Side b, line N still copies digits."""
        html = (
            "<h3>Side b, line 1</h3>"
            "<table><tr><td>(6-8)!*</td></tr></table>"
            "<h3>Side b, line 3</h3>"
            "<table><tr><td>000!-200!-096!*</td></tr></table>"
        )
        self.assertEqual(extract_published_tokens(html, SIDE_FB), {})
        published = extract_f_published_tokens(html, SIDE_FB)
        self.assertEqual(list(published), ["Fb1", "Fb3"])
        self.assertEqual(published["Fb1"], ["(6", "8)!*"])
        self.assertEqual(published["Fb3"], ["000!", "200!", "096!*"])
        stems = side_line_stems(published, ("Fb1", "Fb3"))
        self.assertEqual(stems[0], [])
        self.assertEqual(stems[1], ["000", "200", "096"])
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_island_hits_require_consecutive_tokens(self):
        """A planted island counts; a gap does not."""
        provider = MockProvider()
        gram = GK_LOCKED_GRAMS[0]
        by_side = {side: [[]] for side in F_SIDES}
        by_side[SIDE_FA] = [list(gram)]
        hits = island_hits_by_f_side(by_side, GK_LOCKED_GRAMS)
        self.assertEqual(hits[SIDE_FA][0], 1)
        self.assertEqual(hits[SIDE_FB], (0,) * len(GK_LOCKED_GRAMS))
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(unpublished_f_html_names(Path("/no/such/fixtures")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariChauvetVendorScoreboard(unittest.TestCase):
    """Cited tablets.html → F → Fa/Fb lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.tablets = load_vendored_tablets_html()
        self.f_index = load_vendored_f_index_html()
        self.by_side = load_f_sides()
        self.gk_hits = island_hits_by_f_side(self.by_side, GK_LOCKED_GRAMS)
        self.hpq_hits = island_hits_by_f_side(self.by_side, HPQ_LOCKED_ISLANDS)
        self.e_n9_hits = {
            side: ngram_hit_count(self.by_side[side], E_GRAM_N9) for side in F_SIDES
        }
        self.er7_4_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM4) for side in F_SIDES
        }
        self.er7_8_hits = {
            side: ngram_hit_count(self.by_side[side], ER7_GRAM8) for side in F_SIDES
        }
        self.profile = score_f_longest_repeating(self.by_side, self.analyzer)

    def test_parent_catalog_selects_and_vendors_f(self):
        """Catalog → tablets → F index → Fa/Fb. Not Fr, Fv, or F.html."""
        self.assertTrue(FA_HTML_PATH.is_file())
        self.assertTrue(FB_HTML_PATH.is_file())
        self.assertTrue(FA_JSON_PATH.is_file())
        self.assertTrue(FB_JSON_PATH.is_file())
        self.assertTrue((FA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((FB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue(F_INDEX_HTML_PATH.is_file())
        self.assertFalse((FA_HTML_DIR / "Fr.html").exists())
        self.assertFalse((FA_HTML_DIR / "Fv.html").exists())
        self.assertFalse((FA_HTML_DIR / "F.html").exists())
        self.assertFalse((FB_HTML_DIR / "Fr.html").exists())
        self.assertEqual(STANDING_FR_HTML, False)
        self.assertEqual(STANDING_FV_HTML, False)
        self.assertEqual(STANDING_F_HTML, False)
        self.assertEqual(FA_HTML_PATH.stat().st_size, STANDING_FA_BYTES)
        self.assertEqual(FB_HTML_PATH.stat().st_size, STANDING_FB_BYTES)
        self.assertEqual(F_INDEX_HTML_PATH.stat().st_size, STANDING_F_INDEX_BYTES)
        self.assertEqual(tablet_row(self.tablets, "F"), STANDING_TABLET_F)
        self.assertEqual(published_all_lines_hrefs(self.f_index), STANDING_F_ALL_LINES)
        self.assertIn("Item F:Stephen-Chauvet Fragment", self.f_index)
        self.assertIn('href="Fa.html"', self.f_index)
        self.assertIn('href="Fb.html"', self.f_index)
        self.assertNotIn('href="Fr.html"', self.f_index)
        self.assertNotIn('href="Fv.html"', self.f_index)
        fa = load_vendored_fa_html()
        fb = load_vendored_fb_html()
        self.assertIn("Item F:Chauvet Fragment", fa)
        self.assertIn("Item F:the Stephen-Chauvet Fragment", fb)
        self.assertIn("Rongorongo Fa", fa)
        self.assertIn("Rongorongo Fb", fb)
        self.assertIn('<h3><a name="Line_1">Line 1</a></h3>', fa)
        self.assertIn("<h3>Side b, line 1</h3>", fb)
        self.assertNotIn('<h3><a name="Line_1">', fb)
        fixtures = Path(__file__).parent / "fixtures"
        self.assertEqual(unpublished_f_html_names(fixtures), ())
        for directory, urls in (
            (FA_HTML_DIR, (CITED_CATALOG_URL, CITED_TABLETS_URL, CITED_F_INDEX_URL, CITED_FA_URL)),
            (FB_HTML_DIR, (CITED_FB_URL, CITED_F_INDEX_URL)),
        ):
            text = (directory / "ATTRIBUTION").read_text(encoding="utf-8")
            for url in urls:
                self.assertIn(url, text)
            self.assertIn("kohaumotu.org/rongorongo_org/copy.html", text)
            self.assertIn("tablet J", text)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parsed_json_matches_html_stems(self):
        """Vendored JSON is the mechanical parse of the HTML. No invented digits."""
        fa_json = load_fa_barthel_json()
        fb_json = load_fb_barthel_json()
        fa_pub = extract_f_published_tokens(load_vendored_fa_html(), SIDE_FA)
        fb_pub = extract_f_published_tokens(load_vendored_fb_html(), SIDE_FB)
        self.assertEqual(fa_json["tablet"], "F")
        self.assertEqual(fb_json["tablet"], "F")
        self.assertEqual(fa_json["side"], SIDE_FA)
        self.assertEqual(fb_json["side"], SIDE_FB)
        self.assertEqual(fa_json["source"]["url"], CITED_FA_URL)
        self.assertEqual(fb_json["source"]["url"], CITED_FB_URL)
        for name in FA_LINE_NAMES:
            self.assertEqual(fa_json["lines"][name], fa_pub[name])
            self.assertEqual(fa_json["stems"][name], self.by_side[SIDE_FA][int(name[2:]) - 1])
        for name in FB_LINE_NAMES:
            self.assertEqual(fb_json["lines"][name], fb_pub[name])
            self.assertEqual(fb_json["stems"][name], self.by_side[SIDE_FB][int(name[2:]) - 1])
        self.assertEqual(fa_json["lines"]["Fa6"], ["(2", "3)!*"])
        self.assertEqual(fa_json["stems"]["Fa6"], [])
        self.assertEqual(fb_json["lines"]["Fb1"], ["(6", "8)!*"])
        self.assertEqual(fb_json["stems"]["Fb1"], [])
        self.assertEqual(extract_published_tokens(load_vendored_fb_html(), SIDE_FB), {})
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_counts_and_known_islands_absent(self):
        """Per-side stem totals; G–K + n=25, H∩P∩Q, E n=9, Er7 4-gram are 0 on F."""
        for side in F_SIDES:
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
        """F's own repeating profile: longest n=0; no n≥4 freq≥2. Not the claim."""
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

    def test_existing_e_keiti_scoreboards_still_compute(self):
        """Cycle 80 E vendor lock and cycle 84 Er7 double stay."""
        prior = TestMamariKeitiVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_tradition_islands_absent()
        prior.test_longest_repeating_ngram_is_9_and_eightgrams_exist()
        prior.test_survey_matches_computed_lock()
        er7 = TestMamariKeitiEr7DoubleScoreboard()
        er7.setUp()
        er7.test_er7_hits_are_two_eightgrams()
        er7.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-85 F vendor lock."""
        lock = self.survey["tablet_f_chauvet_vendor"]
        self.assertEqual(lock["cycle"], 85)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_f"], "F")
        self.assertEqual(lock["name_f"], "Stephen-Chauvet Fragment")
        self.assertEqual(lock["catalog"], CITED_CATALOG_URL)
        self.assertEqual(lock["tablets_page"], CITED_TABLETS_URL)
        self.assertEqual(lock["f_index"], CITED_F_INDEX_URL)
        self.assertEqual(lock["fa_page"], CITED_FA_URL)
        self.assertEqual(lock["fb_page"], CITED_FB_URL)
        self.assertEqual(tuple(lock["f_pages"]), STANDING_F_ALL_LINES)
        self.assertEqual(lock["html_bytes"]["Fa"], STANDING_FA_BYTES)
        self.assertEqual(lock["html_bytes"]["Fb"], STANDING_FB_BYTES)
        self.assertEqual(lock["stem_totals"]["Fa"], STANDING_STEM_TOTALS[SIDE_FA])
        self.assertEqual(lock["stem_totals"]["Fb"], STANDING_STEM_TOTALS[SIDE_FB])
        self.assertEqual(tuple(lock["stem_counts"]["Fa"]), STANDING_FA_STEM_COUNTS)
        self.assertEqual(tuple(lock["stem_counts"]["Fb"]), STANDING_FB_STEM_COUNTS)
        locked_gk = {
            side: tuple(hits) for side, hits in lock["gk_island_hits"].items()
        }
        locked_hpq = {
            side: tuple(hits) for side, hits in lock["hpq_island_hits"].items()
        }
        self.assertEqual(locked_gk, STANDING_GK_ISLAND_HITS)
        self.assertEqual(locked_hpq, STANDING_HPQ_ISLAND_HITS)
        self.assertEqual(lock["e_n9_hits"]["Fa"], 0)
        self.assertEqual(lock["e_n9_hits"]["Fb"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Fa"], 0)
        self.assertEqual(lock["er7_4gram_hits"]["Fb"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Fa"], 0)
        self.assertEqual(lock["er7_8gram_hits"]["Fb"], 0)
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
        self.assertFalse(lock["fr_html"])
        self.assertFalse(lock["fv_html"])
        self.assertFalse(lock["f_html"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertTrue(lock["standing_d_echancree_vendor_unchanged"])
        self.assertTrue(lock["standing_q_vendor_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_maximals_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["cycle"], 80)
        self.assertEqual(self.survey["tablet_e_keiti_er7_double"]["cycle"], 84)
        self.assertTrue(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariChauvetVendorImageSnapshot(unittest.TestCase):
    """Cycle 85 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
