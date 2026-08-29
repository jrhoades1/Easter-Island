"""I's cycle-159 leftover overlap 3-gram off-I lock.

Cycle 160 text-search lock. Uses already-vendored A–V and the
cycle-159 leftover overlap 3-gram 076 020 010 (the n≥3 run
shared by leftover n=4 maximals 090 076 020 010, 076 020 010
050, and 053 076 020 010 with independent I 5-gram
400 070 076 020 010). Does not retune that 3-gram. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 141 (076 010 079 was I-only 8/0).
This cycle is the new overlap 3-gram 076 020 010 only. Do
not retune 076 010 079 (already chased cycles 140–152).

Locks exact consecutive hits of 076 020 010 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can
lose: i_overlap_3gram_076_020_010_is_i_only (I hits ≥ 1 and
off-I hits == 0). Ia is exactly 12 at Ia2[120]/Ia4[87]/
Ia4[158]/Ia5[56]/Ia5[144]/Ia6[102]/Ia12[1]/Ia12[84]/
Ia13[48]/Ia13[87]/Ia14[110]/Ia14[128]; Ib unpublished 0;
every other vendored tablet is exact-0. Not an n≥8 island.
Not the cycle-103 I 5-gram (it is the independent 5-gram's
suffix-3).

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
    MAXIMAL_N5_400,
)
from tests.test_mamari_i_leftover_n4_independent_n5_n3_overlap_scoreboard import (
    STANDING_SHARED_076_010_079,
    STANDING_SHARED_076_020_010,
    TestMamariILeftoverN4IndependentN5N3OverlapScoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    OFF_I_TABLETS,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_I_ONLY = True
GRAM3 = STANDING_SHARED_076_020_010
STANDING_N3 = 3
STANDING_I_HITS = 12
STANDING_IA_HITS = 12
STANDING_IB_HITS = 0
STANDING_N_ON_I = 12
STANDING_I_SITES = (
    (SIDE_IA, "Ia2", 120),
    (SIDE_IA, "Ia4", 87),
    (SIDE_IA, "Ia4", 158),
    (SIDE_IA, "Ia5", 56),
    (SIDE_IA, "Ia5", 144),
    (SIDE_IA, "Ia6", 102),
    (SIDE_IA, "Ia12", 1),
    (SIDE_IA, "Ia12", 84),
    (SIDE_IA, "Ia13", 48),
    (SIDE_IA, "Ia13", 87),
    (SIDE_IA, "Ia14", 110),
    (SIDE_IA, "Ia14", 128),
)
STANDING_IB_SITES = ()
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_overlap_3gram_076_020_010_is_i_only"
STANDING_I_OVERLAP_3GRAM_076_020_010_IS_I_ONLY = True
STANDING_RESULT = "i_overlap_3gram_076_020_010_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE141_3GRAM = False


def i_overlap_3gram_076_020_010_is_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


class TestIOverlap3gram076020010IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-159 leftover overlap tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "020", "010"))
        self.assertEqual(GRAM3, STANDING_SHARED_076_020_010)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["076", "020", "010", "076", "020", "010"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 2)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0."""
        provider = MockProvider()
        self.assertTrue(i_overlap_3gram_076_020_010_is_i_only(1, 0))
        self.assertTrue(i_overlap_3gram_076_020_010_is_i_only(12, 0))
        self.assertFalse(i_overlap_3gram_076_020_010_is_i_only(1, 1))
        self.assertFalse(i_overlap_3gram_076_020_010_is_i_only(0, 0))
        self.assertFalse(i_overlap_3gram_076_020_010_is_i_only(0, 12))
        self.assertEqual(STANDING_CLAIM, "i_overlap_3gram_076_020_010_is_i_only")
        self.assertTrue(STANDING_I_OVERLAP_3GRAM_076_020_010_IS_I_ONLY)
        self.assertEqual(
            STANDING_I_OVERLAP_3GRAM_076_020_010_IS_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_overlap_3gram_is_cycle159_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-159 leftover, a substring of 400 070 076 020 010."""
        provider = MockProvider()
        self.assertEqual(GRAM3, STANDING_SHARED_076_020_010)
        self.assertNotEqual(GRAM3, STANDING_SHARED_076_010_079)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_400, ("400", "070", "076", "020", "010"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertTrue(is_contiguous_substring(GRAM3, MAXIMAL_N5_400))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM3, MAXIMAL_N5_010))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertLess(len(GRAM3), 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIOverlap3gram076020010IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover overlap 3-gram off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM3, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.claim_holds = i_overlap_3gram_076_020_010_is_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_159_leftover_not_retuned(self):
        """3-gram is the cycle-159 leftover lock, not a new inventory."""
        self.assertEqual(GRAM3, STANDING_SHARED_076_020_010)
        self.assertEqual(GRAM3, ("076", "020", "010"))
        prior_159 = self.survey["i_leftover_n4_independent_n5_n3_overlap"]
        self.assertEqual(prior_159["cycle"], 159)
        shared = {tuple(row["overlap"]) for row in prior_159["overlaps"]}
        self.assertIn(GRAM3, shared)
        self.assertIn(STANDING_SHARED_076_010_079, shared)
        self.assertEqual(prior_159["with_n3plus_overlap_count"], 5)
        self.assertTrue(prior_159["i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"])
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, STANDING_SHARED_076_010_079)
        self.assertTrue(is_contiguous_substring(GRAM3, MAXIMAL_N5_400))
        self.assertFalse(is_contiguous_substring(GRAM3, MAXIMAL_N5_010))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_twelve_on_ia(self):
        """Overlap 3-gram is 12 on Ia; Ib unpublished 0."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 12)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, 12)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N3]
            self.assertEqual(tuple(stems), GRAM3)
            self.assertEqual(side, SIDE_IA)
        self.assertEqual(
            STANDING_I_SITES[:3],
            ((SIDE_IA, "Ia2", 120), (SIDE_IA, "Ia4", 87), (SIDE_IA, "Ia4", 158)),
        )
        self.assertEqual(
            STANDING_I_SITES[9],
            (SIDE_IA, "Ia13", 87),
        )
        self.assertEqual(
            STANDING_I_SITES[11],
            (SIDE_IA, "Ia14", 128),
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 12. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, 0)
        self.assertEqual(STANDING_OFF_I_SITES, ())
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM3))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 12)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(
            i_overlap_3gram_076_020_010_is_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_OVERLAP_3GRAM_076_020_010_IS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_OVERLAP_3GRAM_076_020_010_IS_I_ONLY,
        )
        self.assertTrue(STANDING_I_OVERLAP_3GRAM_076_020_010_IS_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_overlap_3gram_076_020_010_is_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_159_141_103_and_w_scoreboards_still_compute(self):
        """Cycle 159 overlap, 141 I-only, 103 I-only, and W stay."""
        prior_159 = TestMamariILeftoverN4IndependentN5N3OverlapScoreboard()
        prior_159.setUp()
        prior_159.test_counts_5_of_27_and_hypothesis_n_5_holds()
        prior_159.test_survey_matches_computed_lock()
        prior_141 = TestMamariIOverlap3gram076010079IOnlyScoreboard()
        prior_141.setUp()
        prior_141.test_3gram_is_zero_off_i_and_i_only()
        prior_141.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-160 overlap 3-gram I-only lock."""
        lock = self.survey["i_overlap_3gram_076_020_010_i_only"]
        self.assertEqual(lock["cycle"], 160)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(
            [list(site) for site in STANDING_OFF_I_SITES],
            lock["off_i_sites"],
        )
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_overlap_3gram_076_020_010_is_i_only"])
        self.assertEqual(
            lock["i_overlap_3gram_076_020_010_is_i_only"],
            STANDING_I_OVERLAP_3GRAM_076_020_010_IS_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle141_3gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_n4_independent_n5_n3_overlap"]["cycle"], 159)
        self.assertTrue(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"][
                "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"]["N_with_n3plus_overlap"],
            5,
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["cycle"], 141)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_010_079_i_only"][
                "i_overlap_3gram_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["N_on_I"], 8)
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertTrue(self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"])
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"], 5)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariIOverlap3gram076020010IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 160 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
