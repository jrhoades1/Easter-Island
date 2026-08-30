"""I's leftover n=4 remaining vs most frequent constituent 2-gram.

Cycle 222 text-search lock. Uses already-vendored A–V and the
cycle-136 leftover n=4 maximal set (27 independent n=4 grams
that are not substrings of the four I 5-grams). Does not retune
that set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Nested leftover n=4 family locks stay: cycle 136 leftover 27;
cycle 166 exactly 7 contain 999 090 076; cycle 170 exactly 4
contain 076 071; cycle 205 exactly 1 contain 076 070
(999 090 076 070, already in the cycle-166 7); cycle 137
exception 071 065 071 999 (I-only 2/0, no 076). Remaining =
leftover n=4 minus those containing 999 090 076 or 076 071
or equal to 071 065 071 999. Nested-check N_remaining=16.

This cycle is leftover-inventory, not I-only of G. For each
remaining leftover 4-gram, list its three contiguous 2-grams.
Count how many remaining leftovers contain each 2-gram
(contain = the 2-gram is a substring of that leftover
4-gram). G = the 2-gram with the highest remaining-leftover
count. If a tie, pick the one whose first token is the larger
Barthel id, then the larger second token. K = that count.

Measured: G=090 076, K=5, N_remaining=16. Matching remaining
leftovers: 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, 090 076 057 600. G is uniquely the most
frequent (next counts are 3). I vs off-I of G is not this
cycle. Nested cycle 221 remaining 5-grams 4/4 I-only, cycle
208 leftover 4-gram 5/0, and cycle 171 076 071 43/0 stay.
Claim that can lose:
i_leftover_n4_remaining_exactly_5_contain_090_076.
True only if leftover n=4 family counts stay 27/7/4/1,
exception present, N_remaining=16, G is uniquely the most
frequent under the tie-break, and exactly K remaining
contain G. The claim is true. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
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
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    STANDING_HYPOTHESIZED_N5,
    STANDING_LEFTOVER_N4_COUNT,
    STANDING_MAXIMALS,
    STANDING_N,
    TestMamariIIndependentNge4MaximalsScoreboard,
    leftover_n4_rows,
)
from tests.test_mamari_i_leftover_999_090_076_070_remaining_5grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY as CYCLE221_I_ONLY,
    STANDING_N_SEQUENCES as CYCLE221_N_SEQUENCES,
    TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    GRAM2 as CYCLE205_GRAM2,
    STANDING_WITH as CYCLE205_N_WITH,
    TestMamariILeftoverN4076070Scoreboard,
    leftover_with_076_070,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    GRAM2 as CYCLE170_GRAM2,
    STANDING_WITH as CYCLE170_N_WITH,
    TestMamariILeftoverN4076071Scoreboard,
    leftover_with_076_071,
)
from tests.test_mamari_i_leftover_n4_999_090_076_scoreboard import (
    GRAM3 as CYCLE166_GRAM3,
    STANDING_WITH as CYCLE166_N_WITH,
    TestMamariILeftoverN4999090076Scoreboard,
    leftover_with_999_090_076,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
    EXCEPTION_SITES,
    STANDING_LEFTOVER,
    TestMamariILeftoverN4Maximals076Scoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    STANDING_INDEPENDENT,
    STANDING_INDEPENDENT_COUNT,
    TestMamariINge4Scoreboard,
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

HYPOTHESIS_K = 5
STANDING_LEFTOVER_N4 = 27
STANDING_N_WITH_999_090_076 = 7
STANDING_N_WITH_076_071 = 4
STANDING_N_WITH_076_070 = 1
STANDING_N_EXCEPTION = 1
STANDING_N_REMAINING = 16
GRAM2 = ("090", "076")
STANDING_G = GRAM2
STANDING_N2 = 2
STANDING_K = 5
STANDING_N_WITHOUT_G = 11
STANDING_N_2GRAM_NEXT = 3
EXCLUDED_999_090_076 = CYCLE166_GRAM3
EXCLUDED_076_071 = CYCLE170_GRAM2
NEAR_MISS_999_090_076_070 = ("999", "090", "076", "070")
NEAR_MISS_999_090_076_071 = ("999", "090", "076", "071")
NEAR_MISS_076_071_009_090 = ("076", "071", "009", "090")
NEAR_MISS_071_065_071_999 = EXCEPTION_GRAM
STANDING_MATCHING_LEFTOVERS = (
    ("090", "076", "020", "010"),
    ("021", "090", "076", "087"),
    ("600", "090", "076", "011"),
    ("999", "021", "090", "076"),
    ("090", "076", "057", "600"),
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_KNOWN_DISTINCT = True
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE = True
STANDING_CLAIM = "i_leftover_n4_remaining_exactly_5_contain_090_076"
STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 = True
STANDING_RESULT = "i_leftover_n4_remaining_next_2gram"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_FAMILY_DOES_NOT_COUNT = True
STANDING_EXCEPTION_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_is_remaining(
    gram: tuple[str, ...],
    family_999_090_076: tuple[str, ...] = EXCLUDED_999_090_076,
    family_076_071: tuple[str, ...] = EXCLUDED_076_071,
    exception: tuple[str, ...] = EXCEPTION_GRAM,
) -> bool:
    """True iff leftover n=4 is outside locked families and the no-076 exception."""
    if gram == exception:
        return False
    if is_contiguous_substring(family_999_090_076, gram):
        return False
    if is_contiguous_substring(family_076_071, gram):
        return False
    return True


def leftover_remaining_n4(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that still contain 076 but not locked families."""
    return tuple(row for row in leftovers if leftover_is_remaining(row[0]))


def contiguous_2grams(gram: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    """The three contiguous 2-grams of a leftover 4-gram."""
    return tuple(gram[index : index + 2] for index in range(len(gram) - 1))


def remaining_2gram_counts(
    remaining: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> Counter:
    """How many remaining leftovers contain each constituent 2-gram."""
    counts: Counter = Counter()
    for gram, _n, _freq, _sites in remaining:
        for pair in set(contiguous_2grams(gram)):
            counts[pair] += 1
    return counts


def barthel_id(token: str) -> int:
    """Integer Barthel id for the cycle-222 tie-break. Raw stem only."""
    return int(token)


def rank_2grams(
    counts: Counter,
) -> tuple[tuple[tuple[str, ...], int], ...]:
    """2-grams by remaining-leftover count, then larger Barthel ids."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0][0]), -barthel_id(item[0][1])),
        )
    )


def select_g(
    remaining: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> tuple[tuple[str, ...], int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining has no G."""
    ranked = rank_2grams(remaining_2gram_counts(remaining))
    if not ranked:
        return ((), 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _pair, other in ranked if other == count) == 1
    return (gram, count, unique)


def leftover_remaining_with_g(
    remaining: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    needle: tuple[str, ...] = STANDING_G,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Remaining leftover n=4 maximals that contain G as a substring."""
    return tuple(row for row in remaining if is_contiguous_substring(needle, row[0]))


def leftover_remaining_without_g(
    remaining: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    needle: tuple[str, ...] = STANDING_G,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Remaining leftover n=4 maximals that do not contain G."""
    return tuple(
        row for row in remaining if not is_contiguous_substring(needle, row[0])
    )


def leftover_n4_family_counts_hold(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> bool:
    """Nested 27/7/4/1 leftover n=4 family counts plus the no-076 exception."""
    if len(leftovers) != STANDING_LEFTOVER_N4:
        return False
    if len(leftover_with_999_090_076(leftovers)) != STANDING_N_WITH_999_090_076:
        return False
    if len(leftover_with_076_071(leftovers)) != STANDING_N_WITH_076_071:
        return False
    if len(leftover_with_076_070(leftovers)) != STANDING_N_WITH_076_070:
        return False
    if EXCEPTION_GRAM not in {gram for gram, _n, _f, _s in leftovers}:
        return False
    return True


def i_leftover_n4_remaining_exactly_5_contain_090_076(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    expected_g: tuple[str, ...] = STANDING_G,
    expected_k: int = HYPOTHESIS_K,
    expected_remaining: int = STANDING_N_REMAINING,
) -> bool:
    """True iff remaining=16, G is unique max, and exactly K contain G."""
    if not leftover_n4_family_counts_hold(leftovers):
        return False
    remaining = leftover_remaining_n4(leftovers)
    if len(remaining) != expected_remaining:
        return False
    gram, count, unique = select_g(remaining)
    if not unique or gram != expected_g or count != expected_k:
        return False
    return len(leftover_remaining_with_g(remaining, gram)) == expected_k


STANDING_REMAINING = leftover_remaining_n4(STANDING_LEFTOVER)
STANDING_WITH_ROWS = leftover_remaining_with_g(STANDING_REMAINING)
STANDING_WITHOUT_ROWS = leftover_remaining_without_g(STANDING_REMAINING)
STANDING_2GRAM_COUNTS = remaining_2gram_counts(STANDING_REMAINING)
STANDING_RANKED_2GRAMS = rank_2grams(STANDING_2GRAM_COUNTS)
STANDING_CONTAINS = tuple(
    is_contiguous_substring(GRAM2, gram) for gram, _n, _f, _s in STANDING_REMAINING
)


class TestILeftoverN4RemainingNext2gramHelpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining vs next 2-gram. No CV, no LLM."""

    def test_remaining_filter_and_exactly_5_can_fail(self):
        """The 16 remaining hold at G=090 076 K=5; empty, families, ties lose."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N4)
        remaining = leftover_remaining_n4(leftover)
        self.assertEqual(remaining, STANDING_REMAINING)
        self.assertEqual(len(remaining), STANDING_N_REMAINING)
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(contiguous_2grams(("090", "076", "020", "010")), (
            ("090", "076"),
            ("076", "020"),
            ("020", "010"),
        ))
        self.assertTrue(leftover_is_remaining(("090", "076", "020", "010")))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_999_090_076_070))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_999_090_076_071))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_076_071_009_090))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_071_065_071_999))
        self.assertTrue(is_contiguous_substring(GRAM2, ("090", "076", "020", "010")))
        self.assertTrue(is_contiguous_substring(GRAM2, ("999", "021", "090", "076")))
        self.assertFalse(is_contiguous_substring(GRAM2, ("028", "076", "011", "076")))
        self.assertFalse(i_leftover_n4_remaining_exactly_5_contain_090_076(()))
        with_gram = leftover_remaining_with_g(remaining)
        without_gram = leftover_remaining_without_g(remaining)
        self.assertEqual(len(with_gram), STANDING_K)
        self.assertEqual(len(without_gram), STANDING_N_WITHOUT_G)
        self.assertEqual(with_gram, STANDING_WITH_ROWS)
        self.assertEqual(without_gram, STANDING_WITHOUT_ROWS)
        gram, count, unique = select_g(remaining)
        self.assertEqual(gram, STANDING_G)
        self.assertEqual(count, STANDING_K)
        self.assertTrue(unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(STANDING_RANKED_2GRAMS[0], (STANDING_G, STANDING_K))
        self.assertEqual(STANDING_RANKED_2GRAMS[1][1], STANDING_N_2GRAM_NEXT)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        planted_family = leftover + (
            (("999", "090", "076", "999"), 4, 1, (("Ia", "Ia1", 0),)),
        )
        self.assertFalse(i_leftover_n4_remaining_exactly_5_contain_090_076(planted_family))
        planted_remaining = leftover + (
            (("028", "076", "011", "050"), 4, 1, (("Ia", "Ia1", 0),)),
        )
        self.assertEqual(len(leftover_remaining_n4(planted_remaining)), 17)
        self.assertFalse(i_leftover_n4_remaining_exactly_5_contain_090_076(planted_remaining))
        dropped = tuple(
            row for row in leftover if row[0] != ("090", "076", "020", "010")
        )
        self.assertFalse(i_leftover_n4_remaining_exactly_5_contain_090_076(dropped))
        replacements = {
            ("028", "076", "011", "076"): (
                ("076", "020", "076", "020"),
                4,
                1,
                (("Ia", "Ia1", 0),),
            ),
            ("071", "999", "604", "076"): (
                ("076", "020", "010", "076"),
                4,
                1,
                (("Ia", "Ia1", 1),),
            ),
        }
        tied_leftover = tuple(replacements.get(row[0], row) for row in leftover)
        self.assertEqual(len(tied_leftover), STANDING_LEFTOVER_N4)
        self.assertTrue(leftover_n4_family_counts_hold(tied_leftover))
        self.assertEqual(len(leftover_remaining_n4(tied_leftover)), STANDING_N_REMAINING)
        tied_g, tied_k, tied_unique = select_g(leftover_remaining_n4(tied_leftover))
        self.assertEqual(tied_g, STANDING_G)
        self.assertEqual(tied_k, 5)
        self.assertFalse(tied_unique)
        self.assertFalse(i_leftover_n4_remaining_exactly_5_contain_090_076(tied_leftover))
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_remaining_exactly_5_contain_090_076")
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076)
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076,
            HYPOTHESIS_K == STANDING_K,
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING)
        self.assertTrue(STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftovers_are_cycle_136_n4_not_5gram_substrings(self):
        """Cycle-136 leftover set: 27 n=4 maximals outside the four 5-grams."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        maximal_n4 = tuple(row for row in STANDING_MAXIMALS if row[1] == 4)
        self.assertEqual(len(maximal_n4), STANDING_LEFTOVER_N4)
        self.assertEqual(
            {gram for gram, _n, _f, _s in leftover},
            {gram for gram, _n, _f, _s in maximal_n4},
        )
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


class TestMamariILeftoverN4RemainingNext2gramScoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 remaining next 2-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.remaining = leftover_remaining_n4(self.leftover)
        self.with_gram = leftover_remaining_with_g(self.remaining)
        self.without_gram = leftover_remaining_without_g(self.remaining)
        self.claim_holds = i_leftover_n4_remaining_exactly_5_contain_090_076(
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
        self.assertEqual(len(prior.maximals), STANDING_N)
        self.assertEqual(STANDING_N, 31)
        leftover_tokens = {gram for gram, _n, _f, _s in STANDING_LEFTOVER}
        maximal_n4 = {gram for gram, n, _f, _s in prior.maximals if n == 4}
        self.assertEqual(leftover_tokens, maximal_n4)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 39)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(
            self.survey["i_independent_nge4_maximals"]["i_independent_nge4_has_exactly_4_maximals"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertEqual(self.survey["i_repeating_nge4"]["independent_count"], 39)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_leftover_n4_family_counts_27_7_4_1(self):
        """Nested leftover n=4 family counts stay 27/7/4/1; exception present."""
        self.assertTrue(leftover_n4_family_counts_hold(self.leftover))
        self.assertEqual(len(self.leftover), STANDING_LEFTOVER_N4)
        self.assertEqual(len(self.leftover), 27)
        self.assertEqual(len(leftover_with_999_090_076(self.leftover)), 7)
        self.assertEqual(len(leftover_with_999_090_076(self.leftover)), CYCLE166_N_WITH)
        self.assertEqual(len(leftover_with_076_071(self.leftover)), 4)
        self.assertEqual(len(leftover_with_076_071(self.leftover)), CYCLE170_N_WITH)
        self.assertEqual(len(leftover_with_076_070(self.leftover)), 1)
        self.assertEqual(len(leftover_with_076_070(self.leftover)), CYCLE205_N_WITH)
        self.assertEqual(EXCLUDED_999_090_076, ("999", "090", "076"))
        self.assertEqual(EXCLUDED_076_071, ("076", "071"))
        self.assertEqual(CYCLE205_GRAM2, ("076", "070"))
        self.assertIn(EXCEPTION_GRAM, {gram for gram, _n, _f, _s in self.leftover})
        self.assertEqual(EXCEPTION_GRAM, ("071", "065", "071", "999"))
        self.assertEqual(EXCEPTION_SITES, (("Ia", "Ia9", 1), ("Ia", "Ia9", 56)))
        overlap = {
            gram for gram, _n, _f, _s in leftover_with_999_090_076(self.leftover)
        } & {gram for gram, _n, _f, _s in leftover_with_076_071(self.leftover)}
        self.assertEqual(overlap, {("999", "090", "076", "071")})
        self.assertEqual(27 - 7 - 4 + 1 - 1, STANDING_N_REMAINING)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remaining_16_and_hypothesis_k_5_holds(self):
        """16 remaining; exactly 5 contain 090 076. Claim is true."""
        self.assertEqual(len(self.remaining), STANDING_N_REMAINING)
        self.assertEqual(len(self.remaining), 16)
        self.assertEqual(self.remaining, STANDING_REMAINING)
        self.assertEqual(len(self.with_gram), STANDING_K)
        self.assertEqual(len(self.without_gram), STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_K, 5)
        self.assertEqual(STANDING_N_WITHOUT_G, 11)
        self.assertEqual(STANDING_N_REMAINING, STANDING_K + STANDING_N_WITHOUT_G)
        self.assertEqual(HYPOTHESIS_K, 5)
        gram, count, unique = select_g(self.remaining)
        self.assertEqual(gram, STANDING_G)
        self.assertEqual(count, STANDING_K)
        self.assertTrue(unique)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(self.leftover))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076,
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076)
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_remaining_exactly_5_contain_090_076")
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
            self.assertFalse(is_contiguous_substring(EXCLUDED_999_090_076, gram))
            self.assertFalse(is_contiguous_substring(EXCLUDED_076_071, gram))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_remaining_only_the_expected_five(self):
        """Five remaining leftovers contain 090 076; locked families do not count."""
        self.assertEqual(self.with_gram, STANDING_WITH_ROWS)
        self.assertEqual(self.without_gram, STANDING_WITHOUT_ROWS)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in self.with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
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
        self.assertFalse(leftover_is_remaining(NEAR_MISS_999_090_076_070))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_999_090_076_071))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_076_071_009_090))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_071_065_071_999))
        self.assertNotIn(
            NEAR_MISS_999_090_076_070,
            {g for g, _n, _f, _s in self.remaining},
        )
        self.assertNotIn(
            NEAR_MISS_071_065_071_999,
            {g for g, _n, _f, _s in self.remaining},
        )
        self.assertTrue(STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_sites_on_i(self):
        """Remaining leftover I sites; Ib unpublished; each site matches stems."""
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

    def test_existing_221_208_205_170_166_171_and_w_scoreboards_still_compute(self):
        """Cycle 221 4/4, 208 5/0, leftover 27/7/4/1, 171 43/0, W stay."""
        prior_221 = TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard()
        prior_221.setUp()
        prior_221.test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_221.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE221_N_SEQUENCES, 4)
        self.assertTrue(CYCLE221_I_ONLY)
        if not prior_221.claim_holds:
            self.fail("nested cycle 221 remaining 5-grams 4/4 I-only drifted")
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
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_166 = TestMamariILeftoverN4999090076Scoreboard()
        prior_166.setUp()
        prior_166.test_counts_7_of_27_and_hypothesis_n_7_holds()
        prior_166.test_survey_matches_computed_lock()
        prior_137 = TestMamariILeftoverN4Maximals076Scoreboard()
        prior_137.setUp()
        prior_137.test_counts_26_of_27_and_hypothesis_all_contain_loses()
        prior_137.test_survey_matches_computed_lock()
        prior_136 = TestMamariIIndependentNge4MaximalsScoreboard()
        prior_136.setUp()
        prior_136.test_n_is_31_and_hypothesis_n_4_loses()
        prior_136.test_survey_matches_computed_lock()
        leftover_136 = leftover_n4_rows()
        self.assertEqual(len(leftover_136), 27)
        self.assertEqual(
            len([row for row in prior_136.maximals if row[1] == 4]),
            27,
        )
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
        prior_135 = TestMamariINge4Scoreboard()
        prior_135.setUp()
        prior_135.test_counts_and_hypothesis_all_substrings_loses()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-222 leftover remaining 2-gram lock."""
        lock = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(lock["cycle"], 222)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 5)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(tuple(lock["G"]), STANDING_G)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["leftover_n4_count"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], 27)
        self.assertEqual(lock["N_with_999_090_076"], STANDING_N_WITH_999_090_076)
        self.assertEqual(lock["N_with_999_090_076"], 7)
        self.assertEqual(lock["N_with_076_071"], STANDING_N_WITH_076_071)
        self.assertEqual(lock["N_with_076_071"], 4)
        self.assertEqual(lock["N_with_076_070"], STANDING_N_WITH_076_070)
        self.assertEqual(lock["N_with_076_070"], 1)
        self.assertEqual(lock["N_exception"], STANDING_N_EXCEPTION)
        self.assertEqual(tuple(lock["exception"]), EXCEPTION_GRAM)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 16)
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 5)
        self.assertEqual(lock["N_with_g"], STANDING_K)
        self.assertEqual(lock["N_without_g"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_g"], 11)
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
        measured_ranked = [
            {"tokens": list(pair), "remaining_count": count}
            for pair, count in STANDING_RANKED_2GRAMS
        ]
        self.assertEqual(lock["ranked_2grams"], measured_ranked)
        self.assertEqual(tuple(lock["contains_g"]), STANDING_CONTAINS)
        self.assertEqual(tuple(lock["near_miss_999_090_076_070"]), NEAR_MISS_999_090_076_070)
        self.assertEqual(tuple(lock["near_miss_999_090_076_071"]), NEAR_MISS_999_090_076_071)
        self.assertEqual(tuple(lock["near_miss_076_071_009_090"]), NEAR_MISS_076_071_009_090)
        self.assertEqual(tuple(lock["near_miss_071_065_071_999"]), NEAR_MISS_071_065_071_999)
        self.assertTrue(lock["family_999_090_076_does_not_count"])
        self.assertTrue(lock["family_076_071_does_not_count"])
        self.assertTrue(lock["exception_071_065_071_999_does_not_count"])
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertEqual(lock["g_uniquely_most_frequent"], STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(lock["i_vs_off_i_is_not_this_cycle"])
        self.assertNotIn("N_I", lock)
        self.assertNotIn("N_off_I", lock)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(lock["ib_hits"], 0)
        self.assertEqual(lock["ib_sites"], [])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertEqual(
            lock["i_leftover_n4_remaining_exactly_5_contain_090_076"],
            STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_leftover_999_090_076_070_remaining_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_999_090_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_repeating_nge4_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        prior_221 = self.survey["i_leftover_999_090_076_070_remaining_5grams_i_only"]
        self.assertEqual(prior_221["cycle"], 221)
        self.assertTrue(prior_221["i_leftover_999_090_076_070_remaining_5grams_i_only"])
        self.assertEqual(prior_221["N_remaining"], 4)
        self.assertEqual(prior_221["N_I_499"], 1)
        self.assertEqual(prior_221["N_off_I_499"], 0)
        self.assertEqual(prior_221["N_I_600"], 1)
        self.assertEqual(prior_221["N_off_I_600"], 0)
        self.assertEqual(prior_221["N_I_027"], 1)
        self.assertEqual(prior_221["N_off_I_027"], 0)
        self.assertEqual(prior_221["N_I_532"], 1)
        self.assertEqual(prior_221["N_off_I_532"], 0)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"]["i_4gram_999_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_off_I"], 0)
        self.assertEqual(tuple(self.survey["i_4gram_999_090_076_070_i_only"]["tokens4"]), CYCLE208_GRAM4)
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"]["i_leftover_n4_exactly_1_contain_076_070"]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["N_with_076_070"], 1)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"]["i_leftover_n4_exactly_4_contain_076_071"]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["N_with_076_071"], 4)
        self.assertEqual(self.survey["i_leftover_n4_999_090_076"]["cycle"], 166)
        self.assertTrue(
            self.survey["i_leftover_n4_999_090_076"]["i_leftover_n4_exactly_7_contain_999_090_076"]
        )
        self.assertEqual(self.survey["i_leftover_n4_999_090_076"]["N_with_999_090_076"], 7)
        self.assertEqual(self.survey["i_leftover_n4_maximals_076"]["cycle"], 137)
        self.assertFalse(
            self.survey["i_leftover_n4_maximals_076"]["i_leftover_n4_maximals_all_contain_076"]
        )
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["maximal_count"], 31)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariILeftoverN4RemainingNext2gramImageSnapshot(unittest.TestCase):
    """Cycle 222 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / Hamming 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
