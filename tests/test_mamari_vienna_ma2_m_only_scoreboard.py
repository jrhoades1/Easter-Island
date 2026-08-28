"""Great Vienna (M) Ma2 4-gram off-M lock.

Cycle 90 text-search lock. Uses already-vendored Ma from cycle 88
plus already-vendored A / B / C / D / E / F / G / K / H / P / Q /
I / J / L / N. Does not vendor a new tablet. Does not scrape O.
The 4-gram is the cycle-88 longest repeating n-gram. Cycle 89
already showed exact-0 on N. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

Locks exact hits of 006 022 006 022 on every vendored tablet and
whether it appears on Mb (there is no Mb). Claim that can lose:
m_only (Ma hits ≥ 2 and off-M hits == 0). Not an n≥8 island.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_chauvet_vendor_scoreboard import (
    SIDE_FA,
    SIDE_FB,
    load_f_sides,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    load_off_e_by_tablet,
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_keiti_vendor_scoreboard import (
    SIDE_ER,
    SIDE_EV,
    load_e_sides,
)
from tests.test_mamari_reimiro2_vendor_scoreboard import (
    SIDE_LA,
    load_l_sides,
)
from tests.test_mamari_reimiro_vendor_scoreboard import (
    SIDE_JA,
    load_j_sides,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    SIDE_NA,
    SIDE_NB,
    TestMamariSmallViennaVendorScoreboard,
    load_n_sides,
)
from tests.test_mamari_vienna_vendor_scoreboard import (
    MA_LINE_NAMES,
    SIDE_MA,
    STANDING_EIGHTGRAM_EXISTS as M_EIGHTGRAM_EXISTS,
    STANDING_LONGEST_N as M_LONGEST_N,
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
    STANDING_MB_HTML,
    TestMamariViennaVendorScoreboard,
    load_m_sides,
    unpublished_m_html_names,
)

GRAM4 = M_N4_GRAM
VENDORED_TABLETS = (
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "K",
    "H",
    "P",
    "Q",
    "I",
    "J",
    "L",
    "M",
    "N",
)
OFF_M_TABLETS = tuple(tablet for tablet in VENDORED_TABLETS if tablet != "M")
STANDING_MA_HITS = 2
STANDING_MA_SITES = (
    (SIDE_MA, "Ma2", 5),
    (SIDE_MA, "Ma2", 7),
)
STANDING_MB_HITS = 0
STANDING_OFF_M_HITS = 0
STANDING_OFF_M_BY_TABLET = (0,) * len(OFF_M_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_MA_HITS if tablet == "M" else 0 for tablet in VENDORED_TABLETS
)
STANDING_M_ONLY = True
STANDING_N_GE_8_ISLAND = False
STANDING_NEW_TABLET = False
STANDING_RESULT = "m_vienna_ma2_m_only"
STANDING_CLAIM = "m_only"


def load_vendored_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A–N. No O scrape."""
    off_e = load_off_e_by_tablet()
    e = load_e_sides()
    f = load_f_sides()
    j = load_j_sides()
    l = load_l_sides()
    m = load_m_sides()
    n = load_n_sides()
    return {
        "A": off_e["A"],
        "B": off_e["B"],
        "C": off_e["C"],
        "D": off_e["D"],
        "E": e[SIDE_ER] + e[SIDE_EV],
        "F": f[SIDE_FA] + f[SIDE_FB],
        "G": off_e["G"],
        "K": off_e["K"],
        "H": off_e["H"],
        "P": off_e["P"],
        "Q": off_e["Q"],
        "I": off_e["I"],
        "J": j[SIDE_JA],
        "L": l[SIDE_LA],
        "M": m[SIDE_MA],
        "N": n[SIDE_NA] + n[SIDE_NB],
    }


def tablet_hit_counts(
    by_tablet: dict[str, list[list[str]]],
    gram: tuple[str, ...] = GRAM4,
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> tuple[int, ...]:
    """Hit counts on locked vendored tablets. Search only."""
    return tuple(ngram_hit_count(by_tablet[tablet], gram) for tablet in tablets)


def is_m_only(ma_hits: int, off_m_hits: int) -> bool:
    """True iff Ma hits ≥ 2 and off-M hits == 0."""
    return ma_hits >= 2 and off_m_hits == 0


class TestViennaMa2MOnlyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("006", "022", "006", "022"))
        adjacent = [list(GRAM4), list(GRAM4)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4), 2)
        overlap = [["006", "022", "006", "022", "006", "022"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4), 2)
        gapped = [list(GRAM4[:2]) + ["999"] + list(GRAM4[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_m_only_requires_ma_ge_2_and_zero_off_m(self):
        """Boolean is True only when Ma ≥ 2 and off-M is 0."""
        provider = MockProvider()
        self.assertTrue(is_m_only(2, 0))
        self.assertTrue(is_m_only(3, 0))
        self.assertFalse(is_m_only(2, 1))
        self.assertFalse(is_m_only(1, 0))
        self.assertFalse(is_m_only(0, 0))
        self.assertFalse(is_m_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "m_only")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariViennaMa2MOnlyScoreboard(unittest.TestCase):
    """Cited-fixture Ma2 4-gram off-M lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_m_sides()
        self.ma_sites = named_side_hits(
            self.by_side[SIDE_MA],
            MA_LINE_NAMES,
            SIDE_MA,
            GRAM4,
        )
        self.ma_hits = len(self.ma_sites)
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM4)
        self.off_m_counts = tablet_hit_counts(self.by_tablet, GRAM4, OFF_M_TABLETS)
        self.off_m_hits = sum(self.off_m_counts)

    def test_ma2_hits_are_two_overlapping_4grams(self):
        """4-gram is cycle-88 longest; Ma2[5] and Ma2[7]; not n≥8."""
        self.assertEqual(GRAM4, M_N4_GRAM)
        self.assertEqual(GRAM4, ("006", "022", "006", "022"))
        self.assertEqual(len(GRAM4), M_LONGEST_N)
        self.assertEqual(M_LONGEST_N, 4)
        self.assertEqual(self.ma_hits, STANDING_MA_HITS)
        self.assertEqual(STANDING_MA_HITS, 2)
        self.assertEqual(self.ma_hits, ngram_hit_count(self.by_side[SIDE_MA], GRAM4))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.ma_sites), STANDING_MA_SITES)
        for side, line, index in STANDING_MA_SITES:
            names = MA_LINE_NAMES
            stems = self.by_side[side][names.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), GRAM4)
            self.assertEqual(side, SIDE_MA)
            self.assertEqual(line, "Ma2")
        self.assertFalse(M_EIGHTGRAM_EXISTS)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(len(GRAM4), 4)
        self.assertLess(len(GRAM4), 8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_no_mb_and_4gram_absent_there(self):
        """There is no Mb. Hits on the missing side stay 0."""
        fixtures = Path(__file__).parent / "fixtures"
        self.assertFalse(STANDING_MB_HTML)
        self.assertFalse((fixtures / "vienna_ma_html" / "Mb.html").exists())
        self.assertEqual(unpublished_m_html_names(fixtures), ())
        self.assertEqual(STANDING_MB_HITS, 0)
        self.assertNotIn("Mb", self.by_tablet)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_4gram_is_zero_off_m_and_m_only(self):
        """4-gram is 0 on A, B, C, D, E, F, G, K, H, P, Q, I, J, L, N."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(
            VENDORED_TABLETS,
            ("A", "B", "C", "D", "E", "F", "G", "K", "H", "P", "Q", "I", "J", "L", "M", "N"),
        )
        self.assertEqual(OFF_M_TABLETS, ("A", "B", "C", "D", "E", "F", "G", "K", "H", "P", "Q", "I", "J", "L", "N"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_m_counts, STANDING_OFF_M_BY_TABLET)
        self.assertEqual(self.off_m_hits, STANDING_OFF_M_HITS)
        self.assertEqual(STANDING_OFF_M_HITS, 0)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM4))
            if tablet == "M":
                self.assertEqual(count, STANDING_MA_HITS)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(is_m_only(self.ma_hits, self.off_m_hits), STANDING_M_ONLY)
        self.assertTrue(STANDING_M_ONLY)
        self.assertEqual(STANDING_CLAIM, "m_only")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_m_and_n_scoreboards_still_compute(self):
        """Cycle 88 M vendor lock and cycle 89 N vendor lock stay."""
        prior_m = TestMamariViennaVendorScoreboard()
        prior_m.setUp()
        prior_m.test_longest_repeating_ngram_has_no_8gram()
        prior_m.test_survey_matches_computed_lock()
        prior_n = TestMamariSmallViennaVendorScoreboard()
        prior_n.setUp()
        prior_n.test_stem_counts_and_known_islands_absent()
        prior_n.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-90 Ma2 M-only lock."""
        lock = self.survey["tablet_m_vienna_ma2_m_only"]
        self.assertEqual(lock["cycle"], 90)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_m"], "M")
        self.assertEqual(lock["name_m"], "Great Vienna")
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], 4)
        self.assertEqual(lock["ma_hits"], STANDING_MA_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["ma_sites"]),
            STANDING_MA_SITES,
        )
        self.assertEqual(lock["mb_hits"], STANDING_MB_HITS)
        self.assertFalse(lock["mb_html"])
        self.assertFalse(lock["eightgram_exists"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertEqual(lock["off_m_hits"], STANDING_OFF_M_HITS)
        self.assertEqual(tuple(lock["off_m_tablets"]), OFF_M_TABLETS)
        self.assertEqual(tuple(lock["off_m_by_tablet"]), STANDING_OFF_M_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["m_only"], STANDING_M_ONLY)
        self.assertTrue(lock["m_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_m_vienna_vendor_unchanged"])
        self.assertTrue(lock["standing_n_vienna_vendor_unchanged"])
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
        self.assertEqual(self.survey["tablet_m_vienna_vendor"]["cycle"], 88)
        self.assertEqual(tuple(self.survey["tablet_m_vienna_vendor"]["longest_tokens"]), GRAM4)
        self.assertFalse(self.survey["tablet_m_vienna_vendor"]["eightgram_exists"])
        self.assertFalse(self.survey["tablet_m_vienna_vendor"]["mb_html"])
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["cycle"], 89)
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["m_n4_hits"]["Na"], 0)
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["m_n4_hits"]["Nb"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariViennaMa2MOnlyImageSnapshot(unittest.TestCase):
    """Cycle 90 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
