"""I's leftover remaining 5-grams of 999 090 076 070 off-I lock.

Cycle 221 text-search lock. Uses already-vendored A–V and the
cycle-208 leftover 4-gram 999 090 076 070 plus the four leftover
sites that are not the cycle-220 000 5-gram. Does not retune
those 5-grams, the leftover n=4 set, or the cycle-220 000
5-gram. Does not vendor a new tablet. Does not scrape X. W
has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Same claim-shape as cycle 209 (extra 090 076 070 4-grams all
I-only hapax 1/0) and cycle 220 (leftover 000 5-gram I-only
1/0). Cycle 220 holds: leftover 5-gram 999 090 076 070 000
I-only 1/0. Cycle 219 lost: I 090 076 070 forward 4-grams
I-only 7/8; leak 090 076 070 000 on T Ta9[2]. Cycle 208
holds: leftover 4-gram 999 090 076 070 I-only 5/0. Cycle
207 lost: 090 076 070 I-only 8/1 on T. Cycle 171 holds:
076 071 I-only 43/0. This cycle is the four remaining
leftover 5-grams only. Exclude already-locked
999 090 076 070 000. 090 076 070 X without leading 999 is
a different 4-gram. Do not retune the leftover n=4 set. Do
not assume the I-only result.

Locks exact consecutive hits of each remaining leftover
5-gram on tablet I and on every other vendored tablet A–H
and J–V. The four 5-grams: 999 090 076 070 499 at Ia2[9],
999 090 076 070 600 at Ia4[111], 999 090 076 070 027 at
Ia7[67], 999 090 076 070 532 at Ia7[128]. Hypothesis: all
four are I-only. Measured: each N_I=1 at the leftover n=4
start; all N_off_I=0. Claim that can lose:
i_leftover_999_090_076_070_remaining_5grams_i_only. True
only if ALL four have N_off_I=0 and N_I>=1. The claim is
true. Do not assume hapax; measure. Do not retune.

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
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
)
from tests.test_mamari_i_2gram_076_070_i_only_scoreboard import (
    GRAM2 as CYCLE206_GRAM2,
    STANDING_N_I as CYCLE206_N_I,
    STANDING_N_OFF_I as CYCLE206_N_OFF_I,
    TestMamariI2gram076070IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_3GRAM_090_076_070_I_ONLY as CYCLE207_I_ONLY,
    STANDING_LEFTOVER_3GRAM_SITES as CYCLE207_LEFTOVER_3GRAM_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_PREVIOUS_4GRAM as CYCLE207_OFF_I_PREVIOUS_4GRAM,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
    leftover_contained_3gram_sites as cycle207_leftover_3gram_sites,
    named_off_i_sites as cycle207_named_off_i_sites,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
)
from tests.test_mamari_i_4gram_999_090_076_070_i_only_scoreboard import (
    GRAM4 as CYCLE208_GRAM4,
    STANDING_I_4GRAM_999_090_076_070_I_ONLY as CYCLE208_I_ONLY,
    STANDING_I_SITES as CYCLE208_I_SITES,
    STANDING_LEFTOVER_4GRAM_SITES as CYCLE208_LEFTOVER_4GRAM_SITES,
    STANDING_N_I as CYCLE208_N_I,
    STANDING_N_OFF_I as CYCLE208_N_OFF_I,
    TestMamariI4gram999090076070IOnlyScoreboard,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    GRAM5 as CYCLE220_GRAM5,
    NEAR_MISS_059_090_076_070_000,
    NEAR_MISS_999_090_076_070_027,
    NEAR_MISS_999_090_076_070_499,
    NEAR_MISS_999_090_076_070_532,
    NEAR_MISS_999_090_076_070_600,
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_I_ONLY,
    STANDING_I_SITES as CYCLE220_I_SITES,
    STANDING_LEFTOVER_NEXT_STEMS as CYCLE220_LEFTOVER_NEXT_STEMS,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
    TestMamariI5gram999090076070000IOnlyScoreboard,
    extra_i_sites as leftover_extra_i_sites,
    leftover_contained_5gram_sites,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_I_ONLY,
    STANDING_N_I_EACH as CYCLE219_N_I_EACH,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_N_OFF_I_EACH as CYCLE219_N_OFF_I_EACH,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    STANDING_OFF_I_SITES_000 as CYCLE219_OFF_I_SITES,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    GRAM2 as CYCLE205_GRAM2,
    NEAR_MISS_700_076_076_053,
    NEAR_MISS_999_090_076_071,
    STANDING_MATCHING_LEFTOVERS,
    STANDING_WITH_ROWS,
    TestMamariILeftoverN4076070Scoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5 as CYCLE103_GRAM5,
    IA_LINE_NAMES,
    OFF_I_TABLETS,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_gv_scoreboard import GV_LINE_NAMES
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    load_g_k_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SB_LINE_NAMES,
    SIDE_SA,
    SIDE_SB,
    load_s_sides,
)

HYPOTHESIS_ALL_I_ONLY = True
STANDING_N4 = 4
STANDING_N5 = 5
GRAM5_499 = NEAR_MISS_999_090_076_070_499
GRAM5_600 = NEAR_MISS_999_090_076_070_600
GRAM5_027 = NEAR_MISS_999_090_076_070_027
GRAM5_532 = NEAR_MISS_999_090_076_070_532
STANDING_SEQUENCES = (GRAM5_499, GRAM5_600, GRAM5_027, GRAM5_532)
STANDING_NEXT_STEMS = ("499", "600", "027", "532")
NEAR_MISS_999_090_076_070_000 = CYCLE220_GRAM5
NEAR_MISS_090_076_070_000 = CYCLE219_LEAK_4GRAM
NEAR_MISS_999_090_076_070 = CYCLE208_GRAM4
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_076_070 = CYCLE206_GRAM2
NEAR_MISS_999_090_076 = CYCLE167_GRAM3
NEAR_MISS_059_090_076_070 = CYCLE207_OFF_I_PREVIOUS_4GRAM
STANDING_N_SEQUENCES = 4
STANDING_LEFTOVER_N4 = STANDING_MATCHING_LEFTOVERS[0]
STANDING_LEFTOVER_N4_SITES = STANDING_WITH_ROWS[0][3]
STANDING_LOCKED_000_SITE = CYCLE220_I_SITES[0]
STANDING_REMAINING_LEFTOVER_N4_SITES = (
    (SIDE_IA, "Ia2", 9),
    (SIDE_IA, "Ia4", 111),
    (SIDE_IA, "Ia7", 67),
    (SIDE_IA, "Ia7", 128),
)
STANDING_N_I_499 = 1
STANDING_N_I_600 = 1
STANDING_N_I_027 = 1
STANDING_N_I_532 = 1
STANDING_N_ON_I_499 = 1
STANDING_N_ON_I_600 = 1
STANDING_N_ON_I_027 = 1
STANDING_N_ON_I_532 = 1
STANDING_I_SITES_499 = ((SIDE_IA, "Ia2", 9),)
STANDING_I_SITES_600 = ((SIDE_IA, "Ia4", 111),)
STANDING_I_SITES_027 = ((SIDE_IA, "Ia7", 67),)
STANDING_I_SITES_532 = ((SIDE_IA, "Ia7", 128),)
STANDING_I_SITES = (
    STANDING_I_SITES_499,
    STANDING_I_SITES_600,
    STANDING_I_SITES_027,
    STANDING_I_SITES_532,
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_INSIDE_LEFTOVER_EACH = (1, 1, 1, 1)
STANDING_N_EXTRA_EACH = (0, 0, 0, 0)
STANDING_EXTRA_I_SITES = ((), (), (), ())
STANDING_N_OFF_I_499 = 0
STANDING_N_OFF_I_600 = 0
STANDING_N_OFF_I_027 = 0
STANDING_N_OFF_I_532 = 0
STANDING_OFF_I_SITES_499 = ()
STANDING_OFF_I_SITES_600 = ()
STANDING_OFF_I_SITES_027 = ()
STANDING_OFF_I_SITES_532 = ()
STANDING_OFF_I_SITES = (
    STANDING_OFF_I_SITES_499,
    STANDING_OFF_I_SITES_600,
    STANDING_OFF_I_SITES_027,
    STANDING_OFF_I_SITES_532,
)
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_CLAIM = "i_leftover_999_090_076_070_remaining_5grams_i_only"
STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_999_090_076_070_remaining_5grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE220_5GRAM = False
STANDING_SAME_AS_CYCLE219_LEAK_4GRAM = False
STANDING_SAME_AS_CYCLE208_4GRAM = False
STANDING_SAME_CLAIM_SHAPE_AS_209_220 = True
STANDING_000_5GRAM_DOES_NOT_COUNT = True
STANDING_090_076_070_X_WITHOUT_999_DOES_NOT_COUNT = True
STANDING_059_090_076_070_000_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_999_090_076_070_remaining_5grams_i_only(
    n_i_499: int,
    n_off_i_499: int,
    n_i_600: int,
    n_off_i_600: int,
    n_i_027: int,
    n_off_i_027: int,
    n_i_532: int,
    n_off_i_532: int,
) -> bool:
    """True iff all four remaining leftover 5-grams are I-only.

    Claim holds only if every gram has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1.
    """
    return (
        sequence_is_i_only(n_i_499, n_off_i_499)
        and sequence_is_i_only(n_i_600, n_off_i_600)
        and sequence_is_i_only(n_i_027, n_off_i_027)
        and sequence_is_i_only(n_i_532, n_off_i_532)
    )


class TestILeftover999090076070Remaining5gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on leftover remaining 5-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 5-gram counts; a gap is not a hit. Locked 000 / T leak are not."""
        provider = MockProvider()
        self.assertEqual(GRAM5_499, ("999", "090", "076", "070", "499"))
        self.assertEqual(GRAM5_600, ("999", "090", "076", "070", "600"))
        self.assertEqual(GRAM5_027, ("999", "090", "076", "070", "027"))
        self.assertEqual(GRAM5_532, ("999", "090", "076", "070", "532"))
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:4], CYCLE208_GRAM4)
            self.assertEqual(gram[1:4], CYCLE207_GRAM3)
            self.assertEqual(len(gram), STANDING_N5)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["999", "090", "076", "070", "499", "999", "090", "076", "070", "499"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM5_499), 2)
        gapped = [list(GRAM5_499[:2]) + ["006"] + list(GRAM5_499[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM5_499), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM5_499), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070_000)], GRAM5_499), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070_000)], GRAM5_600), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070)], GRAM5_027), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_059_090_076_070_000)], GRAM5_532), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM5_499), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_070)], GRAM5_600), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076)], GRAM5_027), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], GRAM5_532), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM5_499), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE103_GRAM5)], GRAM5_600), 0)
        self.assertTrue(STANDING_000_5GRAM_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_X_WITHOUT_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_059_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_5gram(self):
        """Boolean is True only when all four remaining 5-grams are I-only."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertTrue(
            i_leftover_999_090_076_070_remaining_5grams_i_only(2, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 1, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 0, 1, 1, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 0, 1, 0, 1, 1, 1, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 0, 1, 0, 1, 0, 1, 1)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(0, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 0, 0, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 0, 1, 0, 0, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 0, 1, 0, 1, 0, 0, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(0, 0, 0, 0, 0, 0, 0, 0)
        )
        self.assertFalse(
            i_leftover_999_090_076_070_remaining_5grams_i_only(1, 1, 1, 1, 1, 1, 1, 1)
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_999_090_076_070_remaining_5grams_i_only",
        )
        self.assertTrue(STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_5grams_are_leftover_plus_remaining_next_not_000(self):
        """5-grams stay leftover n=4 + remaining next stems; locked 000 is not."""
        provider = MockProvider()
        self.assertEqual(CYCLE208_GRAM4, ("999", "090", "076", "070"))
        self.assertEqual(CYCLE220_GRAM5, ("999", "090", "076", "070", "000"))
        self.assertEqual(CYCLE220_LEFTOVER_NEXT_STEMS, ("499", "600", "027", "532", "000"))
        self.assertEqual(STANDING_NEXT_STEMS, ("499", "600", "027", "532"))
        self.assertNotIn("000", STANDING_NEXT_STEMS)
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        self.assertEqual(STANDING_N_SEQUENCES, 4)
        for gram, next_stem in zip(STANDING_SEQUENCES, STANDING_NEXT_STEMS, strict=True):
            self.assertEqual(gram[:4], STANDING_LEFTOVER_N4)
            self.assertEqual(gram[4], next_stem)
            self.assertNotEqual(gram, CYCLE220_GRAM5)
            self.assertNotEqual(gram, CYCLE208_GRAM4)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, CYCLE207_GRAM3)
            self.assertNotEqual(gram, CYCLE103_GRAM5)
            self.assertNotEqual(gram, NEAR_MISS_059_090_076_070_000)
            self.assertTrue(is_contiguous_substring(CYCLE208_GRAM4, gram))
            self.assertTrue(is_contiguous_substring(CYCLE207_GRAM3, gram))
            self.assertTrue(is_contiguous_substring(CYCLE206_GRAM2, gram))
            self.assertTrue(is_contiguous_substring(CYCLE167_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, CYCLE220_GRAM5))
            self.assertFalse(is_contiguous_substring(CYCLE220_GRAM5, gram))
            self.assertFalse(is_contiguous_substring(NEAR_MISS_059_090_076_070_000, gram))
            self.assertFalse(is_contiguous_substring(CYCLE195_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE171_GRAM2, gram))
        self.assertEqual(STANDING_REMAINING_LEFTOVER_N4_SITES + (STANDING_LOCKED_000_SITE,), CYCLE208_I_SITES)
        self.assertEqual(STANDING_LOCKED_000_SITE, (SIDE_IA, "Ia14", 139))
        self.assertNotIn(STANDING_LOCKED_000_SITE, STANDING_REMAINING_LEFTOVER_N4_SITES)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE220_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219_LEAK_4GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE208_4GRAM)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_209_220)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(GRAM5_499), STANDING_N5)
        self.assertLess(STANDING_N5, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover remaining 5-gram off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.by_tablet = load_vendored_by_tablet()
        self.grams = STANDING_SEQUENCES
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams)
        self.n_i = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) + STANDING_IB_HITS
            for gram in self.grams
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.grams
        )
        self.off_i = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in self.grams
        )
        self.n_off_i = tuple(sum(row) for row in self.off_i)
        self.off_i_sites = tuple(
            cycle207_named_off_i_sites(gram) for gram in self.grams
        )
        self.leftover_5gram = tuple(
            leftover_contained_5gram_sites(
                STANDING_LEFTOVER_N4_SITES,
                self.i_sides,
                gram,
            )
            for gram in self.grams
        )
        self.extra = tuple(
            leftover_extra_i_sites(sites, leftover)
            for sites, leftover in zip(self.i_sites, self.leftover_5gram, strict=True)
        )
        self.claim_holds = i_leftover_999_090_076_070_remaining_5grams_i_only(
            *sum(zip(self.n_i, self.n_off_i, strict=True), ())
        )

    def test_tokens_and_sites_are_leftover_remaining_not_000(self):
        """5-grams stay leftover n=4 + remaining next stems; 000 is excluded."""
        self.assertEqual(CYCLE208_GRAM4, ("999", "090", "076", "070"))
        self.assertEqual(STANDING_LEFTOVER_N4, CYCLE208_GRAM4)
        self.assertEqual(STANDING_LEFTOVER_N4_SITES, CYCLE208_I_SITES)
        self.assertEqual(STANDING_LEFTOVER_N4_SITES, CYCLE208_LEFTOVER_4GRAM_SITES)
        self.assertEqual(STANDING_NEXT_STEMS, ("499", "600", "027", "532"))
        prior_220 = self.survey["i_5gram_999_090_076_070_000_i_only"]
        self.assertEqual(prior_220["cycle"], 220)
        self.assertEqual(tuple(prior_220["tokens5"]), CYCLE220_GRAM5)
        self.assertEqual(prior_220["N_I"], CYCLE220_N_I)
        self.assertEqual(prior_220["N_I"], 1)
        self.assertEqual(prior_220["N_off_I"], CYCLE220_N_OFF_I)
        self.assertEqual(prior_220["N_off_I"], 0)
        self.assertTrue(prior_220["i_5gram_999_090_076_070_000_i_only"])
        self.assertTrue(CYCLE220_I_ONLY)
        self.assertEqual(tuple(prior_220["leftover_next_stems"]), CYCLE220_LEFTOVER_NEXT_STEMS)
        self.assertEqual(
            tuple(tuple(row) for row in prior_220["i_sites"]),
            CYCLE220_I_SITES,
        )
        prior_208 = self.survey["i_4gram_999_090_076_070_i_only"]
        self.assertEqual(prior_208["cycle"], 208)
        self.assertEqual(tuple(prior_208["tokens4"]), CYCLE208_GRAM4)
        self.assertEqual(prior_208["N_I"], CYCLE208_N_I)
        self.assertEqual(prior_208["N_I"], 5)
        self.assertEqual(prior_208["N_off_I"], CYCLE208_N_OFF_I)
        self.assertEqual(prior_208["N_off_I"], 0)
        self.assertTrue(prior_208["i_4gram_999_090_076_070_i_only"])
        self.assertTrue(CYCLE208_I_ONLY)
        self.assertEqual(
            tuple(tuple(row) for row in prior_208["i_sites"]),
            CYCLE208_I_SITES,
        )
        prior_205 = self.survey["i_leftover_n4_076_070"]
        self.assertEqual(prior_205["cycle"], 205)
        self.assertEqual(tuple(prior_205["tokens2"]), CYCLE205_GRAM2)
        self.assertEqual(prior_205["N_with_076_070"], 1)
        self.assertEqual(prior_205["N_without_076_070"], 26)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(prior_205["matching_leftovers"], measured_matching)
        self.assertTrue(prior_205["i_leftover_n4_exactly_1_contain_076_070"])
        for gram in STANDING_SEQUENCES:
            self.assertNotEqual(gram, CYCLE220_GRAM5)
            self.assertNotEqual(gram, CYCLE208_GRAM4)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, NEAR_MISS_059_090_076_070_000)
            self.assertNotEqual(gram, CYCLE103_GRAM5)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_I=1/1/1/1, N_off_I=0/0/0/0. All I-only. Claim holds."""
        standing_on = (
            STANDING_N_I_499,
            STANDING_N_I_600,
            STANDING_N_I_027,
            STANDING_N_I_532,
        )
        standing_off = (
            STANDING_N_OFF_I_499,
            STANDING_N_OFF_I_600,
            STANDING_N_OFF_I_027,
            STANDING_N_OFF_I_532,
        )
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, standing_on)
        self.assertEqual(standing_on, (1, 1, 1, 1))
        self.assertEqual(self.n_off_i, standing_off)
        self.assertEqual(standing_off, (0, 0, 0, 0))
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(self.leftover_5gram, STANDING_I_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        if self.n_i != (1, 1, 1, 1):
            self.fail("measured N_I drifted from the locked 1/1/1/1")
        if self.n_off_i != (0, 0, 0, 0):
            self.fail("measured N_off_I drifted from the locked 0/0/0/0")
        leftover_next = []
        for leftover_site, start, gram, next_stem, leftover5, extra in zip(
            STANDING_REMAINING_LEFTOVER_N4_SITES,
            (
                STANDING_I_SITES_499[0],
                STANDING_I_SITES_600[0],
                STANDING_I_SITES_027[0],
                STANDING_I_SITES_532[0],
            ),
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            self.leftover_5gram,
            self.extra,
            strict=True,
        ):
            self.assertEqual(leftover_site, start)
            stems = self.i_sides[start[0]][IA_LINE_NAMES.index(start[1])]
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N5]), gram)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), CYCLE208_GRAM4)
            self.assertEqual(stems[start[2] + 4], next_stem)
            self.assertNotEqual(stems[start[2] + 4], "000")
            self.assertEqual(tuple(stems[start[2] + 1 : start[2] + 5]), ("090", "076", "070", next_stem))
            leftover_next.append(stems[start[2] + 4])
            self.assertEqual(leftover5, (start,))
            self.assertEqual(extra, ())
            self.assertNotEqual(gram, CYCLE220_GRAM5)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, NEAR_MISS_059_090_076_070_000)
        self.assertEqual(tuple(leftover_next), STANDING_NEXT_STEMS)
        locked_stems = self.i_sides[SIDE_IA][IA_LINE_NAMES.index("Ia14")]
        self.assertEqual(tuple(locked_stems[139:144]), CYCLE220_GRAM5)
        self.assertEqual(STANDING_LOCKED_000_SITE, (SIDE_IA, "Ia14", 139))
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off in zip(self.hits_by_tablet, self.off_i, strict=True):
            self.assertEqual(hits, STANDING_HITS_BY_TABLET_ONE_ON_I)
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
        for tablet, *counts in zip(
            VENDORED_TABLETS,
            *self.hits_by_tablet,
            strict=True,
        ):
            for count, gram in zip(counts, self.grams, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, 1 if tablet == "I" else 0)
        gk = load_g_k_sides()
        s_sides = load_s_sides()
        t_sides = load_t_sides()
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(gk[SIDE_GR], gram), 0)
            self.assertEqual(ngram_hit_count(gk[SIDE_GV], gram), 0)
            self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], gram), 0)
            self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], gram), 0)
            self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], gram), 0)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE220_GRAM5), 0)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE219_LEAK_4GRAM), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE207_GRAM3), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE208_GRAM4), 0)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], NEAR_MISS_059_090_076_070_000), 1)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], CYCLE206_GRAM2), 2)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], CYCLE206_GRAM2), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE206_GRAM2), 2)
        for side, line, index in CYCLE207_OFF_I_SITES:
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + 3]), CYCLE207_GRAM3)
            self.assertEqual(tuple(stems[index : index + 4]), CYCLE219_LEAK_4GRAM)
            self.assertEqual(
                tuple(stems[index - 1 : index + 4]),
                NEAR_MISS_059_090_076_070_000,
            )
            for gram in STANDING_SEQUENCES:
                self.assertNotEqual(tuple(stems[index - 1 : index + 4]), gram)
        self.assertEqual(CYCLE219_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(CYCLE207_OFF_I_SITES, CYCLE219_OFF_I_SITES)
        ta9 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta9")]
        self.assertEqual(tuple(ta9[1:6]), NEAR_MISS_059_090_076_070_000)
        self.assertEqual(tuple(ta9[2:6]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(tuple(ta9[2:5]), CYCLE207_GRAM3)
        gv3 = gk[SIDE_GV][GV_LINE_NAMES.index("Gv3")]
        self.assertEqual(tuple(gv3[33:35]), CYCLE206_GRAM2)
        self.assertNotIn(tuple(gv3[31:36]), STANDING_SEQUENCES)
        gv4 = gk[SIDE_GV][GV_LINE_NAMES.index("Gv4")]
        self.assertEqual(tuple(gv4[1:3]), CYCLE206_GRAM2)
        self.assertNotIn(tuple(gv4[0:5]), STANDING_SEQUENCES)
        sb8 = s_sides[SIDE_SB][SB_LINE_NAMES.index("Sb8")]
        self.assertEqual(tuple(sb8[17:19]), CYCLE206_GRAM2)
        self.assertNotIn(tuple(sb8[15:20]), STANDING_SEQUENCES)
        leftover_3gram = cycle207_leftover_3gram_sites(STANDING_LEFTOVER_N4_SITES)
        self.assertEqual(leftover_3gram, CYCLE207_LEFTOVER_3GRAM_SITES)
        self.assertEqual(
            i_leftover_999_090_076_070_remaining_5grams_i_only(
                *sum(zip(self.n_i, self.n_off_i, strict=True), ())
            ),
            STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_999_090_076_070_remaining_5grams_i_only",
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE220_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219_LEAK_4GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE208_4GRAM)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_209_220)
        self.assertTrue(STANDING_000_5GRAM_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_X_WITHOUT_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_059_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertTrue(CYCLE220_I_ONLY)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertTrue(CYCLE208_I_ONLY)
        self.assertFalse(CYCLE207_I_ONLY)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_220_219_208_207_and_171_scoreboards_still_compute(self):
        """Cycle 220 1/0, 219 leak 1/1 on T, 208 5/0, 207 8/1, 171 43/0 stay."""
        prior_220 = TestMamariI5gram999090076070000IOnlyScoreboard()
        prior_220.setUp()
        prior_220.test_5gram_is_zero_off_i_and_i_only()
        prior_220.test_survey_matches_computed_lock()
        self.assertEqual(prior_220.i_hits, CYCLE220_N_I)
        self.assertEqual(prior_220.i_hits, 1)
        self.assertEqual(prior_220.off_i_hits, CYCLE220_N_OFF_I)
        self.assertEqual(prior_220.off_i_hits, 0)
        self.assertTrue(prior_220.claim_holds)
        self.assertTrue(CYCLE220_I_ONLY)
        if prior_220.i_hits != 1 or prior_220.off_i_hits != 0:
            self.fail("nested cycle 220 leftover 000 5-gram 1/0 drifted")
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertEqual(prior_219.n_i, CYCLE219_N_I_EACH)
        self.assertEqual(prior_219.n_off_i, CYCLE219_N_OFF_I_EACH)
        self.assertEqual(CYCLE219_N_I_EACH, (1,) * 8)
        self.assertEqual(CYCLE219_N_OFF_I_EACH, (0, 0, 0, 0, 0, 0, 0, 1))
        self.assertEqual(prior_219.n_i[-1], 1)
        self.assertEqual(prior_219.n_off_i[-1], 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertEqual(CYCLE219_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(prior_219.off_i_sites[-1], CYCLE219_OFF_I_SITES)
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        if prior_219.n_i[-1] != 1 or prior_219.n_off_i[-1] != 1:
            self.fail("nested cycle 219 leak 090 076 070 000 1/1 drifted")
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
        self.assertEqual(prior_208.i_hits, CYCLE208_N_I)
        self.assertEqual(prior_208.i_hits, 5)
        self.assertEqual(prior_208.off_i_hits, CYCLE208_N_OFF_I)
        self.assertEqual(prior_208.off_i_hits, 0)
        self.assertTrue(prior_208.claim_holds)
        self.assertTrue(CYCLE208_I_ONLY)
        if prior_208.i_hits != 5 or prior_208.off_i_hits != 0:
            self.fail("nested cycle 208 leftover 4-gram 5/0 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        self.assertFalse(CYCLE207_I_ONLY)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 8/1 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        self.assertEqual(prior_206.i_hits, CYCLE206_N_I)
        self.assertEqual(prior_206.i_hits, 19)
        self.assertEqual(prior_206.off_i_hits, CYCLE206_N_OFF_I)
        self.assertEqual(prior_206.off_i_hits, 5)
        if prior_206.i_hits != 19 or prior_206.off_i_hits != 5:
            self.fail("nested cycle 206 19/5 drifted")
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-221 remaining 5-gram I-only hold."""
        lock = self.survey["i_leftover_999_090_076_070_remaining_5grams_i_only"]
        self.assertEqual(lock["cycle"], 221)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens4"]), CYCLE208_GRAM4)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_sequences"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_I_4gram"], CYCLE208_N_I)
        self.assertEqual(lock["N_I_4gram"], 5)
        self.assertEqual(lock["N_off_I_4gram"], CYCLE208_N_OFF_I)
        self.assertEqual(lock["N_off_I_4gram"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_sites"]),
            STANDING_LEFTOVER_N4_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_leftover_n4_sites"]),
            STANDING_REMAINING_LEFTOVER_N4_SITES,
        )
        self.assertEqual(tuple(lock["locked_000_site"]), STANDING_LOCKED_000_SITE)
        self.assertEqual(lock["N_remaining"], 4)
        self.assertEqual(tuple(lock["next_stems"]), STANDING_NEXT_STEMS)
        self.assertEqual(tuple(lock["leftover_next_stems"]), CYCLE220_LEFTOVER_NEXT_STEMS)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 4)
        standing_on = (
            STANDING_N_I_499,
            STANDING_N_I_600,
            STANDING_N_I_027,
            STANDING_N_I_532,
        )
        standing_off = (
            STANDING_N_OFF_I_499,
            STANDING_N_OFF_I_600,
            STANDING_N_OFF_I_027,
            STANDING_N_OFF_I_532,
        )
        standing_off_sites = (
            STANDING_OFF_I_SITES_499,
            STANDING_OFF_I_SITES_600,
            STANDING_OFF_I_SITES_027,
            STANDING_OFF_I_SITES_532,
        )
        for row, gram, leftover_site, start, next_stem, sites, n_on, n_off, off_sites in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_REMAINING_LEFTOVER_N4_SITES,
            (
                STANDING_I_SITES_499[0],
                STANDING_I_SITES_600[0],
                STANDING_I_SITES_027[0],
                STANDING_I_SITES_532[0],
            ),
            STANDING_NEXT_STEMS,
            STANDING_I_SITES,
            standing_on,
            standing_off,
            standing_off_sites,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens5"]), gram)
            self.assertEqual(tuple(row["leftover_n4_site"]), leftover_site)
            self.assertEqual(tuple(row["i_5gram_start"]), start)
            self.assertEqual(row["next_stem"], next_stem)
            self.assertEqual(row["role"], "remaining_leftover")
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["ia_hits"], 1)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["ib_sites"]),
                STANDING_IB_SITES,
            )
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["leftover_5gram_sites"]),
                sites,
            )
            self.assertEqual(row["N_inside_leftover"], 1)
            self.assertEqual(row["N_extra"], 0)
            self.assertEqual(row["extra_i_sites"], [])
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["off_i_sites"]),
                off_sites,
            )
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(
                tuple(row["hits_by_tablet"]),
                STANDING_HITS_BY_TABLET_ONE_ON_I,
            )
            self.assertTrue(row["i_only"])
        self.assertEqual(lock["N_I_499"], STANDING_N_I_499)
        self.assertEqual(lock["N_off_I_499"], STANDING_N_OFF_I_499)
        self.assertEqual(lock["N_I_600"], STANDING_N_I_600)
        self.assertEqual(lock["N_off_I_600"], STANDING_N_OFF_I_600)
        self.assertEqual(lock["N_I_027"], STANDING_N_I_027)
        self.assertEqual(lock["N_off_I_027"], STANDING_N_OFF_I_027)
        self.assertEqual(lock["N_I_532"], STANDING_N_I_532)
        self.assertEqual(lock["N_off_I_532"], STANDING_N_OFF_I_532)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_999_090_076_070_remaining_5grams_i_only"])
        self.assertEqual(
            lock["i_leftover_999_090_076_070_remaining_5grams_i_only"],
            STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle220_5gram"])
        self.assertFalse(lock["same_as_cycle219_leak_4gram"])
        self.assertFalse(lock["same_as_cycle208_4gram"])
        self.assertTrue(lock["same_claim_shape_as_cycles_209_220"])
        self.assertTrue(lock["000_5gram_does_not_count"])
        self.assertTrue(lock["090_076_070_X_without_999_does_not_count"])
        self.assertTrue(lock["059_090_076_070_000_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_5gram_999_090_076_070_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        prior_220 = self.survey["i_5gram_999_090_076_070_000_i_only"]
        self.assertEqual(prior_220["cycle"], 220)
        self.assertTrue(prior_220["i_5gram_999_090_076_070_000_i_only"])
        self.assertEqual(prior_220["N_I"], 1)
        self.assertEqual(prior_220["N_off_I"], 0)
        prior_219 = self.survey["i_090_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_219["cycle"], 219)
        self.assertFalse(prior_219["i_090_076_070_forward_4grams_i_only"])
        self.assertEqual(prior_219["N_i_only"], 7)
        self.assertEqual(prior_219["N_not_i_only"], 1)
        self.assertEqual(tuple(prior_219["N_I_each"]), CYCLE219_N_I_EACH)
        self.assertEqual(tuple(prior_219["N_off_I_each"]), CYCLE219_N_OFF_I_EACH)
        self.assertEqual(tuple(prior_219["off_i_forward_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(prior_219["sequences"][-1]["N_I"], 1)
        self.assertEqual(prior_219["sequences"][-1]["N_off_I"], 1)
        self.assertFalse(prior_219["sequences"][-1]["i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_219["sequences"][-1]["off_i_sites"]),
            CYCLE219_OFF_I_SITES,
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"][
                "i_4gram_999_090_076_070_i_only"
            ]
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], CYCLE207_N_I)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], CYCLE206_N_I)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], CYCLE206_N_OFF_I)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["N_with_076_070"], 1)
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["N_without_076_070"], 26)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            CYCLE103_GRAM5,
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


class TestMamariILeftover999090076070Remaining5gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 221 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
