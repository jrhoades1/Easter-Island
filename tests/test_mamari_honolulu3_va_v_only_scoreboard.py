"""Honolulu 3 (V) Va 4-gram off-V lock.

Cycle 101 text-search lock. Uses already-vendored Va from cycle 98
plus already-vendored A–U. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); do not invent W stems.
The 4-gram is the cycle-98 longest repeating n-gram. Cycle 99
already listed V's max as tablet-only (counts only). Cycle 95
already showed a different gram is S-only. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. Not a meaning dictionary.

Locks exact hits of 048 010 048 010 on every vendored tablet A–V.
Claim that can lose: v_only (V hits ≥ 2 and off-V hits == 0).
Va is exactly 2; every other vendored tablet is exact-0. Not an
n≥8 island. Not an exact match of the locked M n=4, N n=6, S n=7,
E n=9, or Er7 doubled 4-gram sequences.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    SIDE_VA,
    VA_HTML_PATH,
    VA_LINE_NAMES,
    TestMamariHonolulu3VendorScoreboard,
    load_v_sides,
)
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    STANDING_EIGHTGRAM_EXISTS as V_EIGHTGRAM_EXISTS,
)
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    STANDING_LONGEST_N as V_LONGEST_N,
)
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as V_N4_GRAM,
)
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    STANDING_VB_HTML,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
    GRAM4 as ER7_GRAM4,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    GRAM_N9 as E_GRAM_N9,
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
)
from tests.test_mamari_washington_sb2_s_only_scoreboard import (
    TestMamariWashingtonSb2SOnlyScoreboard,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as S_N7_GRAM,
)

GRAM4 = V_N4_GRAM
OFF_V_TABLETS = tuple(tablet for tablet in VENDORED_TABLETS if tablet != "V")
STANDING_V_HITS = 2
STANDING_VA_HITS = 2
STANDING_VB_HITS = 0
STANDING_VA_SITES = (
    (SIDE_VA, "Va1", 5),
    (SIDE_VA, "Va1", 7),
)
STANDING_VB_SITES = ()
STANDING_VA_SPANS = (("Va1", 5, 9), ("Va1", 7, 11))
STANDING_OFF_V_HITS = 0
STANDING_OFF_V_BY_TABLET = (0,) * len(OFF_V_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_V_HITS if tablet == "V" else 0 for tablet in VENDORED_TABLETS
)
STANDING_V_ONLY = True
STANDING_N_GE_8_ISLAND = False
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_SAME_AS_M_N4 = False
STANDING_SAME_AS_N_N6 = False
STANDING_SAME_AS_S_N7 = False
STANDING_SAME_AS_E_N9 = False
STANDING_SAME_AS_ER7_4 = False
STANDING_RESULT = "v_honolulu_va_v_only"
STANDING_CLAIM = "v_only"


def load_vendored_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A–V in letter order. No W stems."""
    raw = load_vendored_a_through_v()
    return {letter: raw[letter] for letter in VENDORED_TABLETS}


def is_v_only(v_hits: int, off_v_hits: int) -> bool:
    """True iff V hits ≥ 2 and off-V hits == 0."""
    return v_hits >= 2 and off_v_hits == 0


class TestHonolulu3VaVOnlyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("048", "010", "048", "010"))
        adjacent = [list(GRAM4), list(GRAM4)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4), 2)
        overlap = [["048", "010", "048", "010", "048", "010"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4), 2)
        gapped = [list(GRAM4[:2]) + ["999"] + list(GRAM4[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_v_only_requires_v_ge_2_and_zero_off_v(self):
        """Boolean is True only when V ≥ 2 and off-V is 0."""
        provider = MockProvider()
        self.assertTrue(is_v_only(2, 0))
        self.assertTrue(is_v_only(3, 0))
        self.assertFalse(is_v_only(2, 1))
        self.assertFalse(is_v_only(1, 0))
        self.assertFalse(is_v_only(0, 0))
        self.assertFalse(is_v_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "v_only")
        self.assertEqual(provider.get_call_history(), [])

    def test_4gram_is_not_locked_m_n_s_e_or_er7(self):
        """Va 4-gram is a different string from locked local grams."""
        provider = MockProvider()
        self.assertNotEqual(GRAM4, M_N4_GRAM)
        self.assertNotEqual(GRAM4, N_N6_GRAM)
        self.assertNotEqual(GRAM4, S_N7_GRAM)
        self.assertNotEqual(GRAM4, E_GRAM_N9)
        self.assertNotEqual(GRAM4, ER7_GRAM4)
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(N_N6_GRAM, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(S_N7_GRAM, ("004", "660", "081", "004", "660", "081", "004"))
        self.assertEqual(E_GRAM_N9, ("300", "040", "300", "028", "004", "430", "022", "380", "203"))
        self.assertEqual(ER7_GRAM4, ("092", "050", "006", "670"))
        self.assertFalse(STANDING_SAME_AS_M_N4)
        self.assertFalse(STANDING_SAME_AS_N_N6)
        self.assertFalse(STANDING_SAME_AS_S_N7)
        self.assertFalse(STANDING_SAME_AS_E_N9)
        self.assertFalse(STANDING_SAME_AS_ER7_4)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHonolulu3VaVOnlyScoreboard(unittest.TestCase):
    """Cited-fixture Va 4-gram off-V lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_v_sides()
        self.va_sites = named_side_hits(
            self.by_side[SIDE_VA],
            VA_LINE_NAMES,
            SIDE_VA,
            GRAM4,
        )
        self.va_hits = len(self.va_sites)
        self.vb_hits = STANDING_VB_HITS
        self.v_hits = self.va_hits + self.vb_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM4, VENDORED_TABLETS)
        self.off_v_counts = tablet_hit_counts(self.by_tablet, GRAM4, OFF_V_TABLETS)
        self.off_v_hits = sum(self.off_v_counts)

    def test_va1_hits_are_two_overlapping_4grams(self):
        """4-gram is cycle-98 longest; Va1[5] and Va1[7]; not n≥8."""
        self.assertEqual(GRAM4, V_N4_GRAM)
        self.assertEqual(GRAM4, ("048", "010", "048", "010"))
        self.assertEqual(len(GRAM4), V_LONGEST_N)
        self.assertEqual(V_LONGEST_N, 4)
        self.assertEqual(self.va_hits, STANDING_VA_HITS)
        self.assertEqual(STANDING_VA_HITS, 2)
        self.assertEqual(self.va_hits, ngram_hit_count(self.by_side[SIDE_VA], GRAM4))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.va_sites), STANDING_VA_SITES)
        for side, line, index in STANDING_VA_SITES:
            names = VA_LINE_NAMES
            stems = self.by_side[side][names.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), GRAM4)
            self.assertEqual(side, SIDE_VA)
            self.assertEqual(line, "Va1")
        self.assertEqual(
            tuple((line, start, start + 4) for _side, line, start in STANDING_VA_SITES),
            STANDING_VA_SPANS,
        )
        self.assertFalse(V_EIGHTGRAM_EXISTS)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(len(GRAM4), 4)
        self.assertLess(len(GRAM4), 8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_va_only_side_and_no_vb(self):
        """Only Va exists. Hits are Va1 only; Vb is unpublished 0."""
        fixtures = Path(__file__).parent / "fixtures"
        self.assertTrue(VA_HTML_PATH.is_file())
        self.assertTrue((fixtures / "honolulu_va_html" / "Va.html").exists())
        self.assertFalse((fixtures / "honolulu_va_html" / "Vb.html").exists())
        self.assertFalse(STANDING_VB_HTML)
        self.assertEqual(self.va_hits, STANDING_VA_HITS)
        self.assertEqual(self.vb_hits, STANDING_VB_HITS)
        self.assertEqual(STANDING_VB_HITS, 0)
        self.assertEqual(self.v_hits, STANDING_V_HITS)
        self.assertEqual(self.v_hits, STANDING_VA_HITS + STANDING_VB_HITS)
        self.assertEqual(STANDING_V_HITS, 2)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.va_sites), STANDING_VA_SITES)
        self.assertEqual(STANDING_VB_SITES, ())
        self.assertEqual(self.va_hits, ngram_hit_count(self.by_side[SIDE_VA], GRAM4))
        self.assertEqual(ngram_hit_count(self.by_tablet["V"], GRAM4), STANDING_V_HITS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_4gram_is_zero_off_v_and_v_only(self):
        """4-gram is 0 on A–U. Va has exactly 2. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_V_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTU"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_v_counts, STANDING_OFF_V_BY_TABLET)
        self.assertEqual(self.off_v_hits, STANDING_OFF_V_HITS)
        self.assertEqual(STANDING_OFF_V_HITS, 0)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM4))
            if tablet == "V":
                self.assertEqual(count, STANDING_V_HITS)
                self.assertEqual(count, 2)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(is_v_only(self.v_hits, self.off_v_hits), STANDING_V_ONLY)
        self.assertTrue(STANDING_V_ONLY)
        self.assertEqual(STANDING_CLAIM, "v_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(GRAM4, ("048", "010", "048", "010"))
        self.assertNotEqual(GRAM4, M_N4_GRAM)
        self.assertNotEqual(GRAM4, N_N6_GRAM)
        self.assertNotEqual(GRAM4, S_N7_GRAM)
        self.assertNotEqual(GRAM4, E_GRAM_N9)
        self.assertNotEqual(GRAM4, ER7_GRAM4)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_v_w_and_s_scoreboards_still_compute(self):
        """Cycle 98 V vendor, cycle 100 W unpublished, and cycle 95 S-only stay."""
        prior_v = TestMamariHonolulu3VendorScoreboard()
        prior_v.setUp()
        prior_v.test_longest_repeating_ngram_is_4()
        prior_v.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        prior_s = TestMamariWashingtonSb2SOnlyScoreboard()
        prior_s.setUp()
        prior_s.test_7gram_is_zero_off_s_and_s_only()
        prior_s.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-101 Va V-only lock."""
        lock = self.survey["tablet_v_honolulu_va_v_only"]
        self.assertEqual(lock["cycle"], 101)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_v"], "V")
        self.assertEqual(lock["name_v"], "Honolulu 3 [#3622]")
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], 4)
        self.assertEqual(lock["v_hits"], STANDING_V_HITS)
        self.assertEqual(lock["va_hits"], STANDING_VA_HITS)
        self.assertEqual(lock["vb_hits"], STANDING_VB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["va_sites"]),
            STANDING_VA_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["vb_sites"]), STANDING_VB_SITES)
        self.assertFalse(lock["vb_html"])
        self.assertFalse(lock["eightgram_exists"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertEqual(lock["off_v_hits"], STANDING_OFF_V_HITS)
        self.assertEqual(tuple(lock["off_v_tablets"]), OFF_V_TABLETS)
        self.assertEqual(tuple(lock["off_v_by_tablet"]), STANDING_OFF_V_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["v_only"], STANDING_V_ONLY)
        self.assertTrue(lock["v_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertEqual(tuple(lock["n_n6_tokens"]), N_N6_GRAM)
        self.assertEqual(tuple(lock["s_n7_tokens"]), S_N7_GRAM)
        self.assertEqual(tuple(lock["e_n9_tokens"]), E_GRAM_N9)
        self.assertEqual(tuple(lock["er7_4gram_tokens"]), ER7_GRAM4)
        self.assertFalse(lock["same_as_m_n4"])
        self.assertFalse(lock["same_as_n_n6"])
        self.assertFalse(lock["same_as_s_n7"])
        self.assertFalse(lock["same_as_e_n9"])
        self.assertFalse(lock["same_as_er7_4"])
        self.assertFalse(lock["w_barthel"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_v_honolulu_vendor_unchanged"])
        self.assertTrue(lock["standing_u_honolulu_vendor_unchanged"])
        self.assertTrue(lock["standing_t_honolulu_vendor_unchanged"])
        self.assertTrue(lock["standing_s_washington_sb2_s_only_unchanged"])
        self.assertTrue(lock["standing_s_washington_vendor_unchanged"])
        self.assertTrue(lock["standing_n_vienna_na1_n_only_unchanged"])
        self.assertTrue(lock["standing_m_vienna_ma2_m_only_unchanged"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_v_honolulu_vendor"]["cycle"], 98)
        self.assertEqual(
            tuple(self.survey["tablet_v_honolulu_vendor"]["longest_tokens"]),
            GRAM4,
        )
        self.assertFalse(self.survey["tablet_v_honolulu_vendor"]["eightgram_exists"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertTrue(self.survey["corpus_longest_n_inventory"]["rows"]["V"]["tablet_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertIsNone(self.survey["tablet_w_honolulu_unpublished"]["v_n4_hits"])
        self.assertEqual(self.survey["tablet_s_washington_sb2_s_only"]["cycle"], 95)
        self.assertTrue(self.survey["tablet_s_washington_sb2_s_only"]["s_only"])
        self.assertEqual(self.survey["tablet_n_vienna_na1_n_only"]["cycle"], 91)
        self.assertTrue(self.survey["tablet_n_vienna_na1_n_only"]["n_only"])
        self.assertEqual(self.survey["tablet_m_vienna_ma2_m_only"]["cycle"], 90)
        self.assertTrue(self.survey["tablet_m_vienna_ma2_m_only"]["m_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHonolulu3VaVOnlyImageSnapshot(unittest.TestCase):
    """Cycle 101 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
