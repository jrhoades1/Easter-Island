"""I's leftover n=4 remaining remaining-after-090-076 exactly 2 share 430 076.

Cycle 329 text-search lock. Uses already-vendored A–V and the
cycle-136 leftover n=4 maximal set (27 independent n=4 grams
that are not substrings of the four I 5-grams). Does not retune
that set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Population (locked, do not re-derive as a new claim): leftover
n=4 remaining remaining-after-090-076. After cycle 221 closed
leftover n=4 999 090 076 070 at n=5, leftover n=4 remaining
was N=16 (cycle 222). Cycle 222 HOLD: exactly 5 of those 16
contain 2-gram 090 076. Remaining-after-090-076 = N=11 leftover
4-grams that do not contain 090 076. Cycle 328 LOSE: among
those N=11 there is no unique most frequent contiguous 2-gram
(unique_max false, 5-way tie at K=2, G=430 076 by largest-id
labeling, N_distinct=28). Matching leftovers of labeled G:
430 076 001 076, 430 076 049 400. N_remaining after peeling
G=9. This cycle locks exactly-K for that labeled G.

Already locked (record overlap only, do not re-lock): cycle
328 unique-max 2-gram LOSE stays nested. Cycle 222 exactly-5-
contain-090 076 and leftover n=4 remaining I 090 076 peels
(288–327). Leftover extra 090 076 peels; cycles 220–221.

This cycle is leftover-inventory, not I-only of G. HOLD iff
exactly K=2 of the N=11 remaining-after-090-076 leftover
4-grams contain contiguous 2-gram 430 076, and those two are
430 076 001 076 and 430 076 049 400. LOSE if K≠2 or the
matching set differs. Record N=11, K, G=430 076, both matching
4-grams, N_remaining after peeling G (=9). Nested cycle 328
unique_max false stays nested.

Analog: cycle 289 leftover n=4 remaining exactly 4 share next
020 HOLD after cycle 288 share-one-forward-stem LOSE
(unique-max true but claim was share-one; still the exactly-K
peel pattern). Closer: cycle 271 leftover extra remaining-
after-600 exactly 2 share previous 090 HOLD after cycle 270
unique previous stem LOSE (tie). Also cycle 222 exactly 5
contain 090 076 HOLD.

Measured: N=11, K=2, G=430 076, matching leftovers
430 076 001 076 and 430 076 049 400, N_remaining=9.
unique_max stays false (nested cycle 328). Claim that can
lose: i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076.
True only if leftover n=4 family counts stay 27/7/4/1,
exception present, parent remaining=16, exactly 5 contain
090 076, N=11 remaining-after-090-076, exactly K=2 contain
430 076, and the matching set is those two 4-grams. The
claim is true. Do not retune.

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
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_4gram_999_090_076_070_i_only_scoreboard import (
    GRAM4 as CYCLE208_GRAM4,
    STANDING_I_4GRAM_999_090_076_070_I_ONLY as CYCLE208_I_ONLY,
    STANDING_N_I as CYCLE208_N_I,
    STANDING_N_OFF_I as CYCLE208_N_OFF_I,
    TestMamariI4gram999090076070IOnlyScoreboard,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_I_ONLY,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
    TestMamariI5gram999090076070000IOnlyScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    STANDING_HYPOTHESIZED_N5,
    STANDING_LEFTOVER_N4_COUNT,
    STANDING_MAXIMALS,
    STANDING_N as CYCLE136_STANDING_N,
    TestMamariIIndependentNge4MaximalsScoreboard,
    leftover_n4_rows,
)
from tests.test_mamari_i_leftover_999_090_076_070_remaining_5grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY as CYCLE221_I_ONLY,
    STANDING_N_SEQUENCES as CYCLE221_N_SEQUENCES,
    TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    STANDING_WITH as CYCLE205_N_WITH,
    leftover_with_076_070,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    STANDING_WITH as CYCLE170_N_WITH,
    leftover_with_076_071,
)
from tests.test_mamari_i_leftover_n4_999_090_076_scoreboard import (
    STANDING_WITH as CYCLE166_N_WITH,
    leftover_with_999_090_076,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
    EXCEPTION_SITES,
    STANDING_LEFTOVER,
    TestMamariILeftoverN4Maximals076Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_next_2gram_scoreboard import (
    GRAM2 as CYCLE328_GRAM2,
    LOCKED_G_090_076,
    STANDING_CLAIM as CYCLE328_CLAIM,
    STANDING_G as CYCLE328_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE328_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_UNIQUE_MAX_2GRAM as CYCLE328_UNIQUE_MAX_CLAIM,
    STANDING_K as CYCLE328_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE328_MATCHING,
    STANDING_N as CYCLE328_N,
    STANDING_N_DISTINCT as CYCLE328_N_DISTINCT,
    STANDING_N_TIED_AT_K as CYCLE328_N_TIED,
    STANDING_N_WITHOUT_G as CYCLE328_N_WITHOUT,
    STANDING_RESULT as CYCLE328_RESULT,
    STANDING_TIED_2GRAMS as CYCLE328_TIED,
    TestMamariILeftoverN4RemainingAfter090076Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_unique_max_2gram,
    leftover_remaining_after_090_076,
    leftover_remaining_after_090_076_with_g,
    leftover_remaining_after_090_076_without_g,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE222_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    STANDING_N_WITHOUT_G as CYCLE222_N_WITHOUT,
    TestMamariILeftoverN4RemainingNext2gramScoreboard,
    contiguous_2grams,
    i_leftover_n4_remaining_exactly_5_contain_090_076,
    leftover_is_remaining,
    leftover_n4_family_counts_hold,
    leftover_remaining_n4,
    leftover_remaining_with_g,
    leftover_remaining_without_g,
    remaining_2gram_counts,
    select_g,
)
from tests.test_mamari_i_nge4_scoreboard import (
    STANDING_INDEPENDENT,
    STANDING_INDEPENDENT_COUNT,
    nge4_sites,
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
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_K = 2
STANDING_LEFTOVER_N4 = 27
STANDING_N_WITH_999_090_076 = 7
STANDING_N_WITH_076_071 = 4
STANDING_N_WITH_076_070 = 1
STANDING_N_EXCEPTION = 1
STANDING_N_REMAINING_PARENT = 16
STANDING_K_PARENT = 5
STANDING_N = 11
GRAM2 = ("430", "076")
STANDING_G = GRAM2
STANDING_N2 = 2
STANDING_K = 2
STANDING_N_WITHOUT_G = 9
STANDING_N_REMAINING = 9
STANDING_N_DISTINCT = 28
STANDING_N_TIED_AT_K = 5
STANDING_TIED_2GRAMS = (
    ("430", "076"),
    ("076", "020"),
    ("076", "010"),
    ("020", "010"),
    ("010", "079"),
)
NEAR_MISS_090_076_020_010 = ("090", "076", "020", "010")
NEAR_MISS_021_090_076_087 = ("021", "090", "076", "087")
NEAR_MISS_600_090_076_011 = ("600", "090", "076", "011")
NEAR_MISS_999_021_090_076 = ("999", "021", "090", "076")
NEAR_MISS_090_076_057_600 = ("090", "076", "057", "600")
NEAR_MISS_999_090_076_070 = ("999", "090", "076", "070")
NEAR_MISS_071_065_071_999 = EXCEPTION_GRAM
NEAR_MISS_076_020_010_050 = ("076", "020", "010", "050")
NEAR_MISS_076_010_079_090 = ("076", "010", "079", "090")
STANDING_MATCHING_LEFTOVERS = (
    ("430", "076", "001", "076"),
    ("430", "076", "049", "400"),
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_KNOWN_DISTINCT = True
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_UNIQUE_MAX = False
STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE = True
STANDING_CLAIM = "i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076"
STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_EXACTLY_2_SHARE_430_076 = True
STANDING_RESULT = "i_leftover_n4_remaining_after_090_076_exactly2_430_076"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_FAMILY_DOES_NOT_COUNT = True
STANDING_EXCEPTION_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE328_DOES_NOT_COUNT = True
STANDING_CYCLE222_DOES_NOT_COUNT = True
STANDING_I_SITE_PEEL_288_327_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_PEELS_DO_NOT_COUNT = True
STANDING_CYCLES_220_221_DO_NOT_COUNT = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE271 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE289 = True
STANDING_SAME_AS_CYCLE222 = False
STANDING_SAME_AS_CYCLE271 = False
STANDING_SAME_AS_CYCLE289 = False
STANDING_SAME_AS_CYCLE328 = False


def leftover_remaining_after_090_076_matching_set(
    remaining_after: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    needle: tuple[str, ...] = STANDING_G,
) -> tuple[tuple[str, ...], ...]:
    """Tokens of remaining-after-090-076 leftovers that contain G."""
    return tuple(
        gram for gram, _n, _f, _s in leftover_remaining_after_090_076_with_g(
            remaining_after, needle
        )
    )


def matching_set_is_labeled_g_pair(
    matching: tuple[tuple[str, ...], ...],
    expected: tuple[tuple[str, ...], ...] = STANDING_MATCHING_LEFTOVERS,
) -> bool:
    """True iff the matching leftovers are exactly the labeled G pair."""
    return matching == expected


def i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    expected_remaining_parent: int = STANDING_N_REMAINING_PARENT,
    expected_k_parent: int = STANDING_K_PARENT,
    expected_n: int = STANDING_N,
    expected_k: int = HYPOTHESIS_K,
    expected_g: tuple[str, ...] = STANDING_G,
    expected_matching: tuple[tuple[str, ...], ...] = STANDING_MATCHING_LEFTOVERS,
    peeled: tuple[str, ...] = LOCKED_G_090_076,
) -> bool:
    """True iff exactly K=2 of N=11 remaining-after-090-076 contain G."""
    if not leftover_n4_family_counts_hold(leftovers):
        return False
    remaining = leftover_remaining_n4(leftovers)
    if len(remaining) != expected_remaining_parent:
        return False
    if not i_leftover_n4_remaining_exactly_5_contain_090_076(leftovers):
        return False
    if len(leftover_remaining_with_g(remaining, peeled)) != expected_k_parent:
        return False
    remaining_after = leftover_remaining_without_g(remaining, peeled)
    if len(remaining_after) != expected_n:
        return False
    matching = leftover_remaining_after_090_076_matching_set(
        remaining_after, expected_g
    )
    if len(matching) != expected_k:
        return False
    return matching_set_is_labeled_g_pair(matching, expected_matching)


STANDING_REMAINING_PARENT = leftover_remaining_n4(STANDING_LEFTOVER)
STANDING_REMAINING = leftover_remaining_after_090_076(STANDING_LEFTOVER)
STANDING_WITH_ROWS = leftover_remaining_after_090_076_with_g(STANDING_REMAINING)
STANDING_WITHOUT_ROWS = leftover_remaining_after_090_076_without_g(STANDING_REMAINING)
STANDING_MATCHING_TOKENS = leftover_remaining_after_090_076_matching_set(
    STANDING_REMAINING
)
STANDING_2GRAM_COUNTS = remaining_2gram_counts(STANDING_REMAINING)
STANDING_CONTAINS = tuple(
    is_contiguous_substring(GRAM2, gram) for gram, _n, _f, _s in STANDING_REMAINING
)


class TestILeftoverN4RemainingAfter090076Exactly2430076Helpers(unittest.TestCase):
    """Helpers on remaining-after-090-076 exactly 2 share 430 076. No CV, no LLM."""

    def test_exactly_2_can_fail_on_k_or_matching_set(self):
        """N=11 holds at K=2 matching pair; empty, K≠2, and swapped set lose."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N4)
        remaining = leftover_remaining_n4(leftover)
        self.assertEqual(len(remaining), STANDING_N_REMAINING_PARENT)
        self.assertEqual(len(remaining), CYCLE222_N_REMAINING)
        remaining_after = leftover_remaining_after_090_076(leftover)
        self.assertEqual(remaining_after, STANDING_REMAINING)
        self.assertEqual(len(remaining_after), STANDING_N)
        self.assertEqual(len(remaining_after), 11)
        self.assertEqual(GRAM2, ("430", "076"))
        self.assertEqual(LOCKED_G_090_076, ("090", "076"))
        self.assertEqual(contiguous_2grams(("430", "076", "001", "076")), (
            ("430", "076"),
            ("076", "001"),
            ("001", "076"),
        ))
        self.assertTrue(leftover_is_remaining(("430", "076", "001", "076")))
        self.assertTrue(leftover_is_remaining(("430", "076", "049", "400")))
        self.assertTrue(leftover_is_remaining(("028", "076", "011", "076")))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_999_090_076_070))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(LOCKED_G_090_076, ("430", "076", "001", "076")))
        self.assertTrue(is_contiguous_substring(LOCKED_G_090_076, NEAR_MISS_090_076_020_010))
        self.assertTrue(is_contiguous_substring(GRAM2, ("430", "076", "001", "076")))
        self.assertTrue(is_contiguous_substring(GRAM2, ("430", "076", "049", "400")))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_076_020_010_050))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_076_010_079_090))
        self.assertFalse(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(()))
        with_gram = leftover_remaining_after_090_076_with_g(remaining_after)
        without_gram = leftover_remaining_after_090_076_without_g(remaining_after)
        matching = leftover_remaining_after_090_076_matching_set(remaining_after)
        self.assertEqual(len(with_gram), STANDING_K)
        self.assertEqual(len(without_gram), STANDING_N_WITHOUT_G)
        self.assertEqual(with_gram, STANDING_WITH_ROWS)
        self.assertEqual(without_gram, STANDING_WITHOUT_ROWS)
        self.assertEqual(matching, STANDING_MATCHING_LEFTOVERS)
        self.assertTrue(matching_set_is_labeled_g_pair(matching))
        gram, count, unique = select_g(remaining_after)
        self.assertEqual(gram, STANDING_G)
        self.assertEqual(count, STANDING_K)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertFalse(STANDING_UNIQUE_MAX)
        self.assertTrue(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(leftover))
        planted_family = leftover + (
            (("999", "090", "076", "999"), 4, 1, (("Ia", "Ia1", 0),)),
        )
        self.assertFalse(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(planted_family))
        replacements_k3 = {
            ("028", "076", "011", "076"): (
                ("430", "076", "011", "050"),
                4,
                1,
                (("Ia", "Ia1", 0),),
            ),
        }
        extra_g = tuple(replacements_k3.get(row[0], row) for row in leftover)
        self.assertEqual(len(extra_g), STANDING_LEFTOVER_N4)
        self.assertTrue(leftover_n4_family_counts_hold(extra_g))
        extra_after = leftover_remaining_after_090_076(extra_g)
        self.assertEqual(len(extra_after), STANDING_N)
        extra_matching = leftover_remaining_after_090_076_matching_set(extra_after)
        self.assertEqual(len(extra_matching), 3)
        self.assertFalse(matching_set_is_labeled_g_pair(extra_matching))
        self.assertFalse(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(extra_g))
        dropped = tuple(
            row for row in leftover if row[0] != ("430", "076", "001", "076")
        )
        self.assertFalse(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(dropped))
        replacements_swap = {
            ("430", "076", "049", "400"): (
                ("076", "020", "010", "430"),
                4,
                2,
                (("Ia", "Ia13", 170), ("Ia", "Ia14", 63)),
            ),
            ("076", "020", "010", "050"): (
                ("430", "076", "020", "010"),
                4,
                2,
                (("Ia", "Ia2", 120), ("Ia", "Ia14", 110)),
            ),
        }
        swapped = tuple(replacements_swap.get(row[0], row) for row in leftover)
        self.assertEqual(len(swapped), STANDING_LEFTOVER_N4)
        self.assertTrue(leftover_n4_family_counts_hold(swapped))
        swapped_after = leftover_remaining_after_090_076(swapped)
        self.assertEqual(len(swapped_after), STANDING_N)
        swapped_matching = leftover_remaining_after_090_076_matching_set(swapped_after)
        self.assertEqual(len(swapped_matching), STANDING_K)
        self.assertFalse(matching_set_is_labeled_g_pair(swapped_matching))
        self.assertFalse(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(swapped))
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076")
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_EXACTLY_2_SHARE_430_076)
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_EXACTLY_2_SHARE_430_076,
            HYPOTHESIS_K == STANDING_K,
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N)
        self.assertEqual(2 + 9, 11)
        self.assertTrue(STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE271)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE222)
        self.assertFalse(STANDING_SAME_AS_CYCLE271)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE328)
        self.assertEqual(provider.get_call_history(), [])

    def test_nested_cycle328_unique_max_stays_false(self):
        """Cycle 328 unique-max LOSE stays nested; exactly-K is this claim."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        remaining_after = leftover_remaining_after_090_076(leftover)
        gram, count, unique = select_g(remaining_after)
        self.assertEqual(gram, CYCLE328_G)
        self.assertEqual(gram, STANDING_G)
        self.assertEqual(count, CYCLE328_K)
        self.assertEqual(count, STANDING_K)
        self.assertFalse(unique)
        self.assertFalse(CYCLE328_UNIQUE)
        self.assertFalse(CYCLE328_UNIQUE_MAX_CLAIM)
        self.assertFalse(i_leftover_n4_remaining_after_090_076_unique_max_2gram(leftover))
        self.assertEqual(CYCLE328_CLAIM, "i_leftover_n4_remaining_after_090_076_unique_max_2gram")
        self.assertEqual(CYCLE328_N, 11)
        self.assertEqual(CYCLE328_N_WITHOUT, 9)
        self.assertEqual(CYCLE328_N_DISTINCT, 28)
        self.assertEqual(CYCLE328_N_TIED, 5)
        self.assertEqual(CYCLE328_TIED, STANDING_TIED_2GRAMS)
        self.assertEqual(CYCLE328_MATCHING, STANDING_MATCHING_LEFTOVERS)
        self.assertEqual(CYCLE328_GRAM2, GRAM2)
        self.assertTrue(STANDING_CYCLE328_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftovers_are_cycle_136_n4_not_5gram_substrings(self):
        """Cycle-136 leftover set: 27 n=4 maximals outside the four 5-grams."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        maximal_n4 = tuple(row for row in STANDING_MAXIMALS if row[1] == 4)
        self.assertEqual(len(maximal_n4), STANDING_LEFTOVER_N4)
        for gram, n, _freq, _sites in leftover:
            self.assertEqual(n, 4)
            self.assertEqual(len(gram), 4)
            for five in STANDING_HYPOTHESIZED_N5:
                self.assertFalse(is_contiguous_substring(gram, five))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
        self.assertTrue(STANDING_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_EXCEPTION_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4RemainingAfter090076Exactly2430076Scoreboard(unittest.TestCase):
    """Cited-fixture remaining-after-090-076 exactly 2 share 430 076. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.remaining_parent = leftover_remaining_n4(self.leftover)
        self.remaining = leftover_remaining_after_090_076(self.leftover)
        self.with_gram = leftover_remaining_after_090_076_with_g(self.remaining)
        self.without_gram = leftover_remaining_after_090_076_without_g(self.remaining)
        self.matching = leftover_remaining_after_090_076_matching_set(self.remaining)
        self.claim_holds = i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(
            self.leftover
        )

    def test_tokens_are_cycle_136_leftover_not_invented(self):
        """Leftover 27 is the cycle-136 lock, not a new inventory."""
        self.assertEqual(self.leftover, STANDING_LEFTOVER)
        self.assertEqual(leftover_n4_rows(), STANDING_LEFTOVER)
        self.assertEqual(len(STANDING_LEFTOVER), STANDING_LEFTOVER_N4)
        self.assertEqual(STANDING_LEFTOVER_N4, 27)
        self.assertEqual(STANDING_LEFTOVER_N4_COUNT, 27)
        prior = TestMamariIIndependentNge4MaximalsScoreboard()
        prior.setUp()
        self.assertEqual(len(prior.maximals), CYCLE136_STANDING_N)
        leftover_tokens = {gram for gram, _n, _f, _s in STANDING_LEFTOVER}
        maximal_n4 = {gram for gram, n, _f, _s in prior.maximals if n == 4}
        self.assertEqual(leftover_tokens, maximal_n4)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_leftover_n4_family_and_cycle_222_16_5_11(self):
        """Nested leftover n=4 27/7/4/1 and cycle 222 remaining 16/5/11 stay."""
        self.assertTrue(leftover_n4_family_counts_hold(self.leftover))
        self.assertEqual(len(self.leftover), 27)
        self.assertEqual(len(leftover_with_999_090_076(self.leftover)), CYCLE166_N_WITH)
        self.assertEqual(len(leftover_with_076_071(self.leftover)), CYCLE170_N_WITH)
        self.assertEqual(len(leftover_with_076_070(self.leftover)), CYCLE205_N_WITH)
        self.assertIn(EXCEPTION_GRAM, {gram for gram, _n, _f, _s in self.leftover})
        self.assertEqual(EXCEPTION_GRAM, ("071", "065", "071", "999"))
        self.assertEqual(EXCEPTION_SITES, (("Ia", "Ia9", 1), ("Ia", "Ia9", 56)))
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(self.leftover))
        self.assertTrue(CYCLE222_CLAIM)
        self.assertTrue(CYCLE222_UNIQUE)
        self.assertEqual(CYCLE222_G, LOCKED_G_090_076)
        self.assertEqual(CYCLE222_K, 5)
        self.assertEqual(CYCLE222_N_REMAINING, 16)
        self.assertEqual(CYCLE222_N_WITHOUT, 11)
        self.assertEqual(len(self.remaining_parent), 16)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in leftover_remaining_with_g(self.remaining_parent)),
            CYCLE222_MATCHING,
        )
        self.assertEqual(len(self.remaining), STANDING_N)
        self.assertEqual(STANDING_K_PARENT + STANDING_N, STANDING_N_REMAINING_PARENT)
        self.assertEqual(5 + 11, 16)
        self.assertTrue(STANDING_CYCLE222_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remaining_after_11_exactly_2_share_430_076_holds(self):
        """11 remaining-after-090-076; exactly 2 share 430 076. Claim is true."""
        self.assertEqual(len(self.remaining), STANDING_N)
        self.assertEqual(len(self.remaining), 11)
        self.assertEqual(self.remaining, STANDING_REMAINING)
        self.assertEqual(len(self.with_gram), STANDING_K)
        self.assertEqual(len(self.without_gram), STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_K, 2)
        self.assertEqual(STANDING_N_WITHOUT_G, 9)
        self.assertEqual(STANDING_N_REMAINING, 9)
        self.assertEqual(STANDING_N, STANDING_K + STANDING_N_WITHOUT_G)
        self.assertEqual(self.matching, STANDING_MATCHING_LEFTOVERS)
        self.assertTrue(matching_set_is_labeled_g_pair(self.matching))
        gram, count, unique = select_g(self.remaining)
        self.assertEqual(gram, STANDING_G)
        self.assertEqual(count, STANDING_K)
        self.assertFalse(unique)
        self.assertTrue(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(self.leftover))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_EXACTLY_2_SHARE_430_076,
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_EXACTLY_2_SHARE_430_076)
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076")
        self.assertEqual(
            tuple(is_contiguous_substring(GRAM2, gram) for gram, _n, _f, _s in self.remaining),
            STANDING_CONTAINS,
        )
        self.assertEqual(sum(1 for flag in STANDING_CONTAINS if flag), STANDING_K)
        self.assertEqual(
            sum(1 for flag in STANDING_CONTAINS if not flag),
            STANDING_N_WITHOUT_G,
        )
        for gram, _n, _freq, _sites in self.remaining:
            self.assertTrue("076" in gram)
            self.assertNotEqual(gram, EXCEPTION_GRAM)
            self.assertFalse(is_contiguous_substring(LOCKED_G_090_076, gram))
            self.assertFalse(is_contiguous_substring(("999", "090", "076"), gram))
            self.assertFalse(is_contiguous_substring(("076", "071"), gram))
        self.assertEqual(len(STANDING_2GRAM_COUNTS), STANDING_N_DISTINCT)
        self.assertEqual(STANDING_N_DISTINCT, 28)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_remaining_after_only_the_expected_two_for_labeled_g(self):
        """Labeled G=430 076 matches two leftovers; peeled 090 076 do not count."""
        self.assertEqual(self.with_gram, STANDING_WITH_ROWS)
        self.assertEqual(self.without_gram, STANDING_WITHOUT_ROWS)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in self.with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
        self.assertEqual(self.matching, STANDING_MATCHING_TOKENS)
        for gram, n, freq, _sites in self.without_gram:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertFalse(is_contiguous_substring(GRAM2, gram))
            self.assertNotIn(gram, STANDING_MATCHING_LEFTOVERS)
            self.assertEqual(len(contiguous_2grams(gram)), 3)
        for gram, n, freq, _sites in self.with_gram:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertIn(GRAM2, contiguous_2grams(gram))
        peeled = {
            NEAR_MISS_090_076_020_010,
            NEAR_MISS_021_090_076_087,
            NEAR_MISS_600_090_076_011,
            NEAR_MISS_999_021_090_076,
            NEAR_MISS_090_076_057_600,
        }
        remaining_tokens = {g for g, _n, _f, _s in self.remaining}
        for gram in peeled:
            self.assertNotIn(gram, remaining_tokens)
            self.assertIn(gram, CYCLE222_MATCHING)
        self.assertNotIn(NEAR_MISS_999_090_076_070, remaining_tokens)
        self.assertNotIn(NEAR_MISS_071_065_071_999, remaining_tokens)
        self.assertTrue(STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_sites_on_i(self):
        """Remaining-after-090-076 leftover I sites; Ib unpublished."""
        self.assertEqual(self.remaining, STANDING_REMAINING)
        for gram, n, freq, sites in self.remaining:
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), freq)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
                self.assertNotEqual(line[:2], "Ib")
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_328_222_221_220_208_171_and_w_scoreboards_still_compute(self):
        """Cycle 328 unique-max lose, 222 K=5, 221 4/4, 220 1/0, 208 5/0, 171 43/0 stay."""
        prior_328 = TestMamariILeftoverN4RemainingAfter090076Next2gramScoreboard()
        prior_328.setUp()
        prior_328.test_remaining_after_11_unique_max_loses()
        prior_328.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE328_K, 2)
        self.assertEqual(CYCLE328_G, STANDING_G)
        self.assertFalse(CYCLE328_UNIQUE)
        self.assertFalse(CYCLE328_UNIQUE_MAX_CLAIM)
        if prior_328.claim_holds:
            self.fail("nested cycle 328 remaining-after-090-076 unique-max drifted")
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(CYCLE222_CLAIM)
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
        prior_221 = TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard()
        prior_221.setUp()
        prior_221.test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_221.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE221_N_SEQUENCES, 4)
        self.assertTrue(CYCLE221_I_ONLY)
        if not prior_221.claim_holds:
            self.fail("nested cycle 221 remaining 5-grams 4/4 I-only drifted")
        prior_220 = TestMamariI5gram999090076070000IOnlyScoreboard()
        prior_220.setUp()
        prior_220.test_5gram_is_zero_off_i_and_i_only()
        prior_220.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE220_N_I, 1)
        self.assertEqual(CYCLE220_N_OFF_I, 0)
        self.assertTrue(CYCLE220_I_ONLY)
        if CYCLE220_N_I != 1 or CYCLE220_N_OFF_I != 0:
            self.fail("nested cycle 220 leftover 000 5-gram 1/0 drifted")
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
        self.assertEqual(prior_208.i_hits, CYCLE208_N_I)
        self.assertEqual(prior_208.off_i_hits, CYCLE208_N_OFF_I)
        self.assertTrue(CYCLE208_I_ONLY)
        if prior_208.i_hits != 5 or prior_208.off_i_hits != 0:
            self.fail("nested cycle 208 leftover 4-gram 5/0 drifted")
        prior_137 = TestMamariILeftoverN4Maximals076Scoreboard()
        prior_137.setUp()
        prior_137.test_counts_26_of_27_and_hypothesis_all_contain_loses()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_CYCLES_220_221_DO_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-329 remaining-after-090-076 exactly-2 lock."""
        lock = self.survey["i_leftover_n4_remaining_after_090_076_exactly2_430_076"]
        self.assertEqual(lock["cycle"], 329)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(tuple(lock["G"]), STANDING_G)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["leftover_n4_count"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], 27)
        self.assertEqual(lock["N_with_999_090_076"], STANDING_N_WITH_999_090_076)
        self.assertEqual(lock["N_with_076_071"], STANDING_N_WITH_076_071)
        self.assertEqual(lock["N_with_076_070"], STANDING_N_WITH_076_070)
        self.assertEqual(lock["N_exception"], STANDING_N_EXCEPTION)
        self.assertEqual(tuple(lock["exception"]), EXCEPTION_GRAM)
        self.assertEqual(lock["N_remaining_parent"], STANDING_N_REMAINING_PARENT)
        self.assertEqual(lock["N_remaining_parent"], 16)
        self.assertEqual(lock["K_parent"], STANDING_K_PARENT)
        self.assertEqual(lock["K_parent"], 5)
        self.assertEqual(tuple(lock["peeled_2gram"]), LOCKED_G_090_076)
        self.assertEqual(lock["N"], STANDING_N)
        self.assertEqual(lock["N"], 11)
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertEqual(lock["N_with_g"], STANDING_K)
        self.assertEqual(lock["N_without_g"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_g"], 9)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 9)
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 28)
        self.assertEqual(lock["N_tied_at_k"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_k"], 5)
        measured_tied = [list(pair) for pair in STANDING_TIED_2GRAMS]
        self.assertEqual(lock["tied_2grams"], measured_tied)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(lock["matching_leftovers"], measured_matching)
        measured_remaining = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
                "constituent_2grams": [list(pair) for pair in contiguous_2grams(tokens)],
                "contains_g": is_contiguous_substring(GRAM2, tokens),
            }
            for tokens, n, freq, sites in STANDING_REMAINING
        ]
        self.assertEqual(lock["remaining"], measured_remaining)
        self.assertEqual(tuple(lock["contains_g"]), STANDING_CONTAINS)
        self.assertEqual(tuple(lock["near_miss_090_076_020_010"]), NEAR_MISS_090_076_020_010)
        self.assertEqual(tuple(lock["near_miss_021_090_076_087"]), NEAR_MISS_021_090_076_087)
        self.assertEqual(tuple(lock["near_miss_600_090_076_011"]), NEAR_MISS_600_090_076_011)
        self.assertEqual(tuple(lock["near_miss_999_021_090_076"]), NEAR_MISS_999_021_090_076)
        self.assertEqual(tuple(lock["near_miss_090_076_057_600"]), NEAR_MISS_090_076_057_600)
        self.assertEqual(tuple(lock["near_miss_999_090_076_070"]), NEAR_MISS_999_090_076_070)
        self.assertEqual(tuple(lock["near_miss_071_065_071_999"]), NEAR_MISS_071_065_071_999)
        self.assertTrue(lock["family_999_090_076_does_not_count"])
        self.assertTrue(lock["family_076_071_does_not_count"])
        self.assertTrue(lock["exception_071_065_071_999_does_not_count"])
        self.assertTrue(lock["peeled_090_076_does_not_count"])
        self.assertFalse(lock["g_uniquely_most_frequent"])
        self.assertEqual(lock["g_uniquely_most_frequent"], STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertFalse(lock["unique_max"])
        self.assertEqual(lock["unique_max"], STANDING_UNIQUE_MAX)
        self.assertTrue(lock["unique_max_tie_break_is_labeling_only"])
        self.assertTrue(lock["nested_cycle328_unique_max_false"])
        self.assertTrue(lock["i_vs_off_i_is_not_this_cycle"])
        self.assertNotIn("N_I", lock)
        self.assertNotIn("N_off_I", lock)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(lock["ib_hits"], 0)
        self.assertEqual(lock["ib_sites"], [])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076"])
        self.assertEqual(
            lock["i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076"],
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_EXACTLY_2_SHARE_430_076,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle222"])
        self.assertFalse(lock["same_as_cycle271"])
        self.assertFalse(lock["same_as_cycle289"])
        self.assertFalse(lock["same_as_cycle328"])
        self.assertTrue(lock["same_claim_shape_as_cycle222"])
        self.assertTrue(lock["same_claim_shape_as_cycle271"])
        self.assertTrue(lock["same_claim_shape_as_cycle289"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["do_not_relock_cycle328"])
        self.assertTrue(lock["do_not_relock_cycle222"])
        self.assertTrue(lock["do_not_relock_cycles_288_327"])
        self.assertTrue(lock["do_not_relock_leftover_extra_peels"])
        self.assertTrue(lock["do_not_relock_cycles_220_221"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_after_090_076_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_999_090_076_070_remaining_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_5gram_999_090_076_070_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_999_090_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        prior_328 = self.survey["i_leftover_n4_remaining_after_090_076_next_2gram"]
        self.assertEqual(prior_328["cycle"], 328)
        self.assertFalse(prior_328["i_leftover_n4_remaining_after_090_076_unique_max_2gram"])
        self.assertFalse(prior_328["unique_max"])
        self.assertEqual(prior_328["N"], 11)
        self.assertEqual(prior_328["K"], 2)
        self.assertEqual(tuple(prior_328["G"]), ("430", "076"))
        self.assertEqual(prior_328["N_remaining"], 9)
        self.assertEqual(prior_328["N_distinct"], 28)
        self.assertEqual(prior_328["N_tied_at_k"], 5)
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertEqual(prior_222["N_remaining"], 16)
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(tuple(prior_222["G"]), ("090", "076"))
        self.assertEqual(prior_222["N_without_g"], 11)
        self.assertTrue(prior_222["g_uniquely_most_frequent"])
        prior_221 = self.survey["i_leftover_999_090_076_070_remaining_5grams_i_only"]
        self.assertEqual(prior_221["cycle"], 221)
        self.assertTrue(prior_221["i_leftover_999_090_076_070_remaining_5grams_i_only"])
        self.assertEqual(prior_221["N_remaining"], 4)
        prior_220 = self.survey["i_5gram_999_090_076_070_000_i_only"]
        self.assertEqual(prior_220["cycle"], 220)
        self.assertTrue(prior_220["i_5gram_999_090_076_070_000_i_only"])
        self.assertEqual(prior_220["N_I"], 1)
        self.assertEqual(prior_220["N_off_I"], 0)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"]["i_4gram_999_090_076_070_i_only"]
        )
        self.assertEqual(tuple(self.survey["i_4gram_999_090_076_070_i_only"]["tokens4"]), CYCLE208_GRAM4)
        peel_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(peel_288["cycle"], 288)
        self.assertEqual(peel_288["N_inside"], 13)
        self.assertEqual(peel_288["G"], "020")
        self.assertEqual(peel_288["K"], 4)
        peel_327 = self.survey[
            "i_leftover_n4_remaining_021_090_076_remaining_after_999_extra_i_fwd4_090_076_087_i_only"
        ]
        self.assertEqual(peel_327["cycle"], 327)
        self.assertTrue(
            peel_327["i_leftover_n4_remaining_021_090_076_remaining_after_999_extra_i_fwd4_090_076_087_all_i_only"]
        )
        extra = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(extra["cycle"], 225)
        self.assertEqual(extra["N_leftover"], 56)
        extra_rem = self.survey["i_leftover_extra_090_076_remaining_next_stem"]
        self.assertEqual(extra_rem["cycle"], 227)
        cycle271 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]
        self.assertEqual(cycle271["cycle"], 271)
        self.assertTrue(
            cycle271["i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090"]
        )
        cycle289 = self.survey["i_leftover_n4_remaining_090_076_forward_020"]
        self.assertEqual(cycle289["cycle"], 289)
        self.assertTrue(cycle289["i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"])
        self.assertTrue(STANDING_I_SITE_PEEL_288_327_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_DO_NOT_COUNT)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(CYCLE328_RESULT, "i_leftover_n4_remaining_after_090_076_next_2gram")
        self.assertEqual(CYCLE222_GRAM2, ("090", "076"))
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4RemainingAfter090076Exactly2430076ImageSnapshot(unittest.TestCase):
    """Cycle 329 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / Hamming 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
