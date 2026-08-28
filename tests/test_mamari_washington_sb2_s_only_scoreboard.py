"""Great Washington (S) Sb2 7-gram off-S lock.

Cycle 95 text-search lock. Uses already-vendored Sa/Sb from cycle 94
plus already-vendored A / B / C / D / E / F / G / K / H / P / Q /
I / J / L / M / N / O / R. Does not vendor a new tablet. Does not
scrape T. The 7-gram is the cycle-94 longest repeating n-gram.
Cycle 91 already showed a different gram is N-only. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Locks exact hits of 004 660 081 004 660 081 004 on every vendored
tablet and the Sa vs Sb split. Claim that can lose: s_only
(S hits ≥ 2 and off-S hits == 0). Not an n≥8 island.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_atua_vendor_scoreboard import (
    SIDE_RA,
    SIDE_RB,
    load_r_sides,
)
from tests.test_mamari_boomerang_vendor_scoreboard import (
    SIDE_OA,
    load_o_sides,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_vienna_na1_n_only_scoreboard import (
    TestMamariSmallViennaNa1NOnlyScoreboard,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    load_vendored_by_tablet as load_vendored_a_through_n,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SA_HTML_PATH,
    SA_LINE_NAMES,
    SB_HTML_PATH,
    SB_LINE_NAMES,
    SIDE_SA,
    SIDE_SB,
    TestMamariWashingtonVendorScoreboard,
    load_s_sides,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_EIGHTGRAM_EXISTS as S_EIGHTGRAM_EXISTS,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_N as S_LONGEST_N,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as S_N7_GRAM,
)

GRAM7 = S_N7_GRAM
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
    "O",
    "R",
    "S",
)
OFF_S_TABLETS = tuple(tablet for tablet in VENDORED_TABLETS if tablet != "S")
STANDING_S_HITS = 2
STANDING_SA_HITS = 0
STANDING_SB_HITS = 2
STANDING_SA_SITES = ()
STANDING_SB_SITES = (
    (SIDE_SB, "Sb2", 15),
    (SIDE_SB, "Sb2", 18),
)
STANDING_SB_SPANS = (("Sb2", 15, 22), ("Sb2", 18, 25))
STANDING_OFF_S_HITS = 0
STANDING_OFF_S_BY_TABLET = (0,) * len(OFF_S_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_S_HITS if tablet == "S" else 0 for tablet in VENDORED_TABLETS
)
STANDING_S_ONLY = True
STANDING_N_GE_8_ISLAND = False
STANDING_NEW_TABLET = False
STANDING_RESULT = "s_washington_sb2_s_only"
STANDING_CLAIM = "s_only"


def load_vendored_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A–S. No T scrape."""
    by_tablet = load_vendored_a_through_n()
    o = load_o_sides()
    r = load_r_sides()
    s = load_s_sides()
    return {
        **by_tablet,
        "O": o[SIDE_OA],
        "R": r[SIDE_RA] + r[SIDE_RB],
        "S": s[SIDE_SA] + s[SIDE_SB],
    }


def is_s_only(s_hits: int, off_s_hits: int) -> bool:
    """True iff S hits ≥ 2 and off-S hits == 0."""
    return s_hits >= 2 and off_s_hits == 0


class TestWashingtonSb2SOnlyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 7-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM7, ("004", "660", "081", "004", "660", "081", "004"))
        adjacent = [list(GRAM7), list(GRAM7)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM7), 2)
        overlap = [["004", "660", "081", "004", "660", "081", "004", "660", "081", "004"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM7), 2)
        gapped = [list(GRAM7[:4]) + ["999"] + list(GRAM7[4:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM7), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM7), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_s_only_requires_s_ge_2_and_zero_off_s(self):
        """Boolean is True only when S ≥ 2 and off-S is 0."""
        provider = MockProvider()
        self.assertTrue(is_s_only(2, 0))
        self.assertTrue(is_s_only(3, 0))
        self.assertFalse(is_s_only(2, 1))
        self.assertFalse(is_s_only(1, 0))
        self.assertFalse(is_s_only(0, 0))
        self.assertFalse(is_s_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "s_only")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariWashingtonSb2SOnlyScoreboard(unittest.TestCase):
    """Cited-fixture Sb2 7-gram off-S lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_s_sides()
        self.sa_sites = named_side_hits(
            self.by_side[SIDE_SA],
            SA_LINE_NAMES,
            SIDE_SA,
            GRAM7,
        )
        self.sb_sites = named_side_hits(
            self.by_side[SIDE_SB],
            SB_LINE_NAMES,
            SIDE_SB,
            GRAM7,
        )
        self.sa_hits = len(self.sa_sites)
        self.sb_hits = len(self.sb_sites)
        self.s_hits = self.sa_hits + self.sb_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM7, VENDORED_TABLETS)
        self.off_s_counts = tablet_hit_counts(self.by_tablet, GRAM7, OFF_S_TABLETS)
        self.off_s_hits = sum(self.off_s_counts)

    def test_sb2_hits_are_two_overlapping_7grams(self):
        """7-gram is cycle-94 longest; Sb2[15] and Sb2[18]; not n≥8."""
        self.assertEqual(GRAM7, S_N7_GRAM)
        self.assertEqual(GRAM7, ("004", "660", "081", "004", "660", "081", "004"))
        self.assertEqual(len(GRAM7), S_LONGEST_N)
        self.assertEqual(S_LONGEST_N, 7)
        self.assertEqual(self.sb_hits, STANDING_SB_HITS)
        self.assertEqual(STANDING_SB_HITS, 2)
        self.assertEqual(self.sb_hits, ngram_hit_count(self.by_side[SIDE_SB], GRAM7))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.sb_sites), STANDING_SB_SITES)
        for side, line, index in STANDING_SB_SITES:
            names = SB_LINE_NAMES
            stems = self.by_side[side][names.index(line)][index : index + 7]
            self.assertEqual(tuple(stems), GRAM7)
            self.assertEqual(side, SIDE_SB)
            self.assertEqual(line, "Sb2")
        self.assertEqual(
            tuple((line, start, start + 7) for _side, line, start in STANDING_SB_SITES),
            STANDING_SB_SPANS,
        )
        self.assertFalse(S_EIGHTGRAM_EXISTS)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(len(GRAM7), 7)
        self.assertLess(len(GRAM7), 8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_sa_sb_split_is_sb2_only(self):
        """Both Sa and Sb exist. Hits are Sb2 only; Sa is 0."""
        fixtures = Path(__file__).parent / "fixtures"
        self.assertTrue(SA_HTML_PATH.is_file())
        self.assertTrue(SB_HTML_PATH.is_file())
        self.assertTrue((fixtures / "washington_sa_html" / "Sa.html").exists())
        self.assertTrue((fixtures / "washington_sb_html" / "Sb.html").exists())
        self.assertEqual(self.sa_hits, STANDING_SA_HITS)
        self.assertEqual(self.sb_hits, STANDING_SB_HITS)
        self.assertEqual(STANDING_SA_HITS, 0)
        self.assertEqual(self.s_hits, STANDING_S_HITS)
        self.assertEqual(self.s_hits, STANDING_SA_HITS + STANDING_SB_HITS)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.sa_sites), STANDING_SA_SITES)
        self.assertEqual(self.sa_hits, ngram_hit_count(self.by_side[SIDE_SA], GRAM7))
        self.assertEqual(ngram_hit_count(self.by_tablet["S"], GRAM7), STANDING_S_HITS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_7gram_is_zero_off_s_and_s_only(self):
        """7-gram is 0 on A, B, C, D, E, F, G, K, H, P, Q, I, J, L, M, N, O, R."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(
            VENDORED_TABLETS,
            (
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
                "O",
                "R",
                "S",
            ),
        )
        self.assertEqual(
            OFF_S_TABLETS,
            (
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
                "O",
                "R",
            ),
        )
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_s_counts, STANDING_OFF_S_BY_TABLET)
        self.assertEqual(self.off_s_hits, STANDING_OFF_S_HITS)
        self.assertEqual(STANDING_OFF_S_HITS, 0)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM7))
            if tablet == "S":
                self.assertEqual(count, STANDING_S_HITS)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(is_s_only(self.s_hits, self.off_s_hits), STANDING_S_ONLY)
        self.assertTrue(STANDING_S_ONLY)
        self.assertEqual(STANDING_CLAIM, "s_only")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_s_and_n_scoreboards_still_compute(self):
        """Cycle 94 S vendor lock and cycle 91 Na1 N-only lock stay."""
        prior_s = TestMamariWashingtonVendorScoreboard()
        prior_s.setUp()
        prior_s.test_longest_repeating_ngram_is_7()
        prior_s.test_survey_matches_computed_lock()
        prior_n = TestMamariSmallViennaNa1NOnlyScoreboard()
        prior_n.setUp()
        prior_n.test_6gram_is_zero_off_n_and_n_only()
        prior_n.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-95 Sb2 S-only lock."""
        lock = self.survey["tablet_s_washington_sb2_s_only"]
        self.assertEqual(lock["cycle"], 95)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_s"], "S")
        self.assertEqual(lock["name_s"], "Great Washington")
        self.assertEqual(tuple(lock["tokens7"]), GRAM7)
        self.assertEqual(lock["n7"], 7)
        self.assertEqual(lock["s_hits"], STANDING_S_HITS)
        self.assertEqual(lock["sa_hits"], STANDING_SA_HITS)
        self.assertEqual(lock["sb_hits"], STANDING_SB_HITS)
        self.assertEqual(tuple(tuple(row) for row in lock["sa_sites"]), STANDING_SA_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["sb_sites"]),
            STANDING_SB_SITES,
        )
        self.assertFalse(lock["eightgram_exists"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertEqual(lock["off_s_hits"], STANDING_OFF_S_HITS)
        self.assertEqual(tuple(lock["off_s_tablets"]), OFF_S_TABLETS)
        self.assertEqual(tuple(lock["off_s_by_tablet"]), STANDING_OFF_S_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["s_only"], STANDING_S_ONLY)
        self.assertTrue(lock["s_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_s_washington_vendor_unchanged"])
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
        self.assertEqual(self.survey["tablet_s_washington_vendor"]["cycle"], 94)
        self.assertEqual(
            tuple(self.survey["tablet_s_washington_vendor"]["longest_tokens"]),
            GRAM7,
        )
        self.assertFalse(self.survey["tablet_s_washington_vendor"]["eightgram_exists"])
        self.assertEqual(self.survey["tablet_n_vienna_na1_n_only"]["cycle"], 91)
        self.assertTrue(self.survey["tablet_n_vienna_na1_n_only"]["n_only"])
        self.assertEqual(self.survey["tablet_n_vienna_na1_n_only"]["off_n_hits"], 0)
        self.assertEqual(self.survey["tablet_m_vienna_ma2_m_only"]["cycle"], 90)
        self.assertTrue(self.survey["tablet_m_vienna_ma2_m_only"]["m_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariWashingtonSb2SOnlyImageSnapshot(unittest.TestCase):
    """Cycle 95 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
