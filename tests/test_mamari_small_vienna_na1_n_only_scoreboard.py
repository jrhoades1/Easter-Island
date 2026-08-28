"""Small Vienna (N) Na1 6-gram off-N lock.

Cycle 91 text-search lock. Uses already-vendored Na/Nb from cycle 89
plus already-vendored A / B / C / D / E / F / G / K / H / P / Q /
I / J / L / M. Does not vendor a new tablet. Does not scrape O.
The 6-gram is the cycle-89 longest repeating n-gram. Cycle 90
already showed a different gram is M-only. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. Not a meaning dictionary.

Locks exact hits of 004 064 034 006 004 064 on every vendored
tablet and the Na vs Nb split. Claim that can lose: n_only
(N hits ≥ 2 and off-N hits == 0). Not an n≥8 island.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_keiti_n9_scoreboard import (
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    NA_HTML_PATH,
    NA_LINE_NAMES,
    NB_HTML_PATH,
    NB_LINE_NAMES,
    SIDE_NA,
    SIDE_NB,
    STANDING_LONGEST_SPANS,
    TestMamariSmallViennaVendorScoreboard,
    load_n_sides,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_EIGHTGRAM_EXISTS as N_EIGHTGRAM_EXISTS,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_N as N_LONGEST_N,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    VENDORED_TABLETS,
    TestMamariViennaMa2MOnlyScoreboard,
    load_vendored_by_tablet,
    tablet_hit_counts,
)

GRAM6 = N_N6_GRAM
OFF_N_TABLETS = tuple(tablet for tablet in VENDORED_TABLETS if tablet != "N")
STANDING_N_HITS = 2
STANDING_NA_HITS = 2
STANDING_NB_HITS = 0
STANDING_NA_SITES = (
    (SIDE_NA, "Na1", 3),
    (SIDE_NA, "Na1", 11),
)
STANDING_NB_SITES = ()
STANDING_OFF_N_HITS = 0
STANDING_OFF_N_BY_TABLET = (0,) * len(OFF_N_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_N_HITS if tablet == "N" else 0 for tablet in VENDORED_TABLETS
)
STANDING_N_ONLY = True
STANDING_N_GE_8_ISLAND = False
STANDING_NEW_TABLET = False
STANDING_RESULT = "n_vienna_na1_n_only"
STANDING_CLAIM = "n_only"


def is_n_only(n_hits: int, off_n_hits: int) -> bool:
    """True iff N hits ≥ 2 and off-N hits == 0."""
    return n_hits >= 2 and off_n_hits == 0


class TestSmallViennaNa1NOnlyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 6-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM6, ("004", "064", "034", "006", "004", "064"))
        adjacent = [list(GRAM6), list(GRAM6)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM6), 2)
        overlap = [["004", "064", "034", "006", "004", "064", "034", "006"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM6), 1)
        gapped = [list(GRAM6[:3]) + ["999"] + list(GRAM6[3:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM6), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM6), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_n_only_requires_n_ge_2_and_zero_off_n(self):
        """Boolean is True only when N ≥ 2 and off-N is 0."""
        provider = MockProvider()
        self.assertTrue(is_n_only(2, 0))
        self.assertTrue(is_n_only(3, 0))
        self.assertFalse(is_n_only(2, 1))
        self.assertFalse(is_n_only(1, 0))
        self.assertFalse(is_n_only(0, 0))
        self.assertFalse(is_n_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "n_only")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallViennaNa1NOnlyScoreboard(unittest.TestCase):
    """Cited-fixture Na1 6-gram off-N lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_n_sides()
        self.na_sites = named_side_hits(
            self.by_side[SIDE_NA],
            NA_LINE_NAMES,
            SIDE_NA,
            GRAM6,
        )
        self.nb_sites = named_side_hits(
            self.by_side[SIDE_NB],
            NB_LINE_NAMES,
            SIDE_NB,
            GRAM6,
        )
        self.na_hits = len(self.na_sites)
        self.nb_hits = len(self.nb_sites)
        self.n_hits = self.na_hits + self.nb_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM6)
        self.off_n_counts = tablet_hit_counts(self.by_tablet, GRAM6, OFF_N_TABLETS)
        self.off_n_hits = sum(self.off_n_counts)

    def test_na1_hits_are_two_6grams(self):
        """6-gram is cycle-89 longest; Na1[3] and Na1[11]; not n≥8."""
        self.assertEqual(GRAM6, N_N6_GRAM)
        self.assertEqual(GRAM6, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(len(GRAM6), N_LONGEST_N)
        self.assertEqual(N_LONGEST_N, 6)
        self.assertEqual(self.na_hits, STANDING_NA_HITS)
        self.assertEqual(STANDING_NA_HITS, 2)
        self.assertEqual(self.na_hits, ngram_hit_count(self.by_side[SIDE_NA], GRAM6))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.na_sites), STANDING_NA_SITES)
        for side, line, index in STANDING_NA_SITES:
            names = NA_LINE_NAMES
            stems = self.by_side[side][names.index(line)][index : index + 6]
            self.assertEqual(tuple(stems), GRAM6)
            self.assertEqual(side, SIDE_NA)
            self.assertEqual(line, "Na1")
        self.assertEqual(
            tuple((line, start, start + 6) for _side, line, start in STANDING_NA_SITES),
            STANDING_LONGEST_SPANS,
        )
        self.assertFalse(N_EIGHTGRAM_EXISTS)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(len(GRAM6), 6)
        self.assertLess(len(GRAM6), 8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_na_nb_split_is_na1_only(self):
        """Both Na and Nb exist. Hits are Na1 only; Nb is 0."""
        fixtures = Path(__file__).parent / "fixtures"
        self.assertTrue(NA_HTML_PATH.is_file())
        self.assertTrue(NB_HTML_PATH.is_file())
        self.assertTrue((fixtures / "vienna_na_html" / "Na.html").exists())
        self.assertTrue((fixtures / "vienna_nb_html" / "Nb.html").exists())
        self.assertEqual(self.na_hits, STANDING_NA_HITS)
        self.assertEqual(self.nb_hits, STANDING_NB_HITS)
        self.assertEqual(STANDING_NB_HITS, 0)
        self.assertEqual(self.n_hits, STANDING_N_HITS)
        self.assertEqual(self.n_hits, STANDING_NA_HITS + STANDING_NB_HITS)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.nb_sites), STANDING_NB_SITES)
        self.assertEqual(self.nb_hits, ngram_hit_count(self.by_side[SIDE_NB], GRAM6))
        self.assertEqual(ngram_hit_count(self.by_tablet["N"], GRAM6), STANDING_N_HITS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_6gram_is_zero_off_n_and_n_only(self):
        """6-gram is 0 on A, B, C, D, E, F, G, K, H, P, Q, I, J, L, M."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(
            VENDORED_TABLETS,
            ("A", "B", "C", "D", "E", "F", "G", "K", "H", "P", "Q", "I", "J", "L", "M", "N"),
        )
        self.assertEqual(
            OFF_N_TABLETS,
            ("A", "B", "C", "D", "E", "F", "G", "K", "H", "P", "Q", "I", "J", "L", "M"),
        )
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_n_counts, STANDING_OFF_N_BY_TABLET)
        self.assertEqual(self.off_n_hits, STANDING_OFF_N_HITS)
        self.assertEqual(STANDING_OFF_N_HITS, 0)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM6))
            if tablet == "N":
                self.assertEqual(count, STANDING_N_HITS)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(is_n_only(self.n_hits, self.off_n_hits), STANDING_N_ONLY)
        self.assertTrue(STANDING_N_ONLY)
        self.assertEqual(STANDING_CLAIM, "n_only")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_n_and_m_scoreboards_still_compute(self):
        """Cycle 89 N vendor lock and cycle 90 Ma2 M-only lock stay."""
        prior_n = TestMamariSmallViennaVendorScoreboard()
        prior_n.setUp()
        prior_n.test_longest_repeating_ngram_has_no_8gram()
        prior_n.test_survey_matches_computed_lock()
        prior_m = TestMamariViennaMa2MOnlyScoreboard()
        prior_m.setUp()
        prior_m.test_4gram_is_zero_off_m_and_m_only()
        prior_m.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-91 Na1 N-only lock."""
        lock = self.survey["tablet_n_vienna_na1_n_only"]
        self.assertEqual(lock["cycle"], 91)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_n"], "N")
        self.assertEqual(lock["name_n"], "Small Vienna")
        self.assertEqual(tuple(lock["tokens6"]), GRAM6)
        self.assertEqual(lock["n6"], 6)
        self.assertEqual(lock["n_hits"], STANDING_N_HITS)
        self.assertEqual(lock["na_hits"], STANDING_NA_HITS)
        self.assertEqual(lock["nb_hits"], STANDING_NB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["na_sites"]),
            STANDING_NA_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["nb_sites"]), STANDING_NB_SITES)
        self.assertFalse(lock["eightgram_exists"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertEqual(lock["off_n_hits"], STANDING_OFF_N_HITS)
        self.assertEqual(tuple(lock["off_n_tablets"]), OFF_N_TABLETS)
        self.assertEqual(tuple(lock["off_n_by_tablet"]), STANDING_OFF_N_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["n_only"], STANDING_N_ONLY)
        self.assertTrue(lock["n_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
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
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["cycle"], 89)
        self.assertEqual(tuple(self.survey["tablet_n_vienna_vendor"]["longest_tokens"]), GRAM6)
        self.assertFalse(self.survey["tablet_n_vienna_vendor"]["eightgram_exists"])
        self.assertEqual(self.survey["tablet_m_vienna_ma2_m_only"]["cycle"], 90)
        self.assertTrue(self.survey["tablet_m_vienna_ma2_m_only"]["m_only"])
        self.assertEqual(self.survey["tablet_m_vienna_ma2_m_only"]["off_m_hits"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallViennaNa1NOnlyImageSnapshot(unittest.TestCase):
    """Cycle 91 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
