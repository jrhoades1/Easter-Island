"""I's cycle-135 independent n≥4 grams collapsed to maximals.

Cycle 136 text-search lock. Uses already-vendored A–V and the
cycle-135 independent n≥4 set (39 grams that are not substrings
of the I 5-gram). Does not vendor a new tablet. Does not scrape
X. W has no Barthel (cycle 100); skip W. Does not redo H∩P∩Q
n≥8 or G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

A gram is maximal iff it is not a contiguous substring of a
longer independent gram. Hypothesis N_maximals=4: the four
other cycle-103 tied n=5 grams. Measured N=31: those four
plus 27 leftover n=4 grams that are not substrings of any of
the four 5-grams. The eight non-maximals are the 4-prefixes
and 4-suffixes of those four 5-grams; each sits in exactly
one maximal. Claim that can lose:
i_independent_nge4_has_exactly_4_maximals. The claim is
false. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_a_independent_nge8_maximals_scoreboard import (
    TestMamariAIndependentNge8MaximalsScoreboard,
)
from tests.test_mamari_c_independent_nge8_maximals_scoreboard import (
    containing_maximal_indexes,
    every_independent_in_at_least_one_maximal,
    every_nonmaximal_is_substring_of_exactly_one,
    independent_maximals,
    is_contained_in_longer,
    membership_rows,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    STANDING_INDEPENDENT,
    STANDING_INDEPENDENT_COUNT,
    STANDING_TIED_INDEP_N5,
    TestMamariINge4Scoreboard,
    independent_rows,
    is_i_5gram_substring,
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

HYPOTHESIS_N = 4
STANDING_N = 31
STANDING_NONMAXIMAL_COUNT = 8
STANDING_LEFTOVER_N4_COUNT = 27
MAXIMAL_N5_430 = (
    "430",
    "076",
    "006",
    "000",
    "076",
)
MAXIMAL_N5_011 = (
    "076",
    "011",
    "090",
    "090",
    "076",
)
MAXIMAL_N5_400 = (
    "400",
    "070",
    "076",
    "020",
    "010",
)
MAXIMAL_N5_010 = (
    "076",
    "010",
    "079",
    "006",
    "700",
)
N5_430_PREFIX = MAXIMAL_N5_430[:4]
N5_430_SUFFIX = MAXIMAL_N5_430[1:]
N5_011_PREFIX = MAXIMAL_N5_011[:4]
N5_011_SUFFIX = MAXIMAL_N5_011[1:]
N5_400_PREFIX = MAXIMAL_N5_400[:4]
N5_400_SUFFIX = MAXIMAL_N5_400[1:]
N5_010_PREFIX = MAXIMAL_N5_010[:4]
N5_010_SUFFIX = MAXIMAL_N5_010[1:]
STANDING_HYPOTHESIZED_N5 = (
    MAXIMAL_N5_430,
    MAXIMAL_N5_010,
    MAXIMAL_N5_011,
    MAXIMAL_N5_400,
)
STANDING_NESTED_N4 = (
    N5_430_PREFIX,
    N5_430_SUFFIX,
    N5_010_PREFIX,
    N5_010_SUFFIX,
    N5_011_PREFIX,
    N5_011_SUFFIX,
    N5_400_PREFIX,
    N5_400_SUFFIX,
)
STANDING_MAXIMALS = (
    (MAXIMAL_N5_430, 5, 2, (("Ia", "Ia1", 129), ("Ia", "Ia14", 162))),
    (MAXIMAL_N5_011, 5, 2, (("Ia", "Ia12", 39), ("Ia", "Ia14", 102))),
    (MAXIMAL_N5_400, 5, 2, (("Ia", "Ia13", 85), ("Ia", "Ia14", 126))),
    (MAXIMAL_N5_010, 5, 2, (("Ia", "Ia6", 19), ("Ia", "Ia13", 72))),
    (("071", "999", "604", "076"), 4, 2, (("Ia", "Ia1", 63), ("Ia", "Ia9", 3))),
    (("028", "076", "011", "076"), 4, 3, (("Ia", "Ia1", 136), ("Ia", "Ia4", 125), ("Ia", "Ia14", 78))),
    (("430", "076", "001", "076"), 4, 2, (("Ia", "Ia10", 103), ("Ia", "Ia13", 156))),
    (("053", "076", "020", "010"), 4, 2, (("Ia", "Ia12", 0), ("Ia", "Ia14", 109))),
    (("090", "999", "090", "076"), 4, 2, (("Ia", "Ia12", 45), ("Ia", "Ia14", 138))),
    (("430", "076", "049", "400"), 4, 2, (("Ia", "Ia13", 170), ("Ia", "Ia14", 63))),
    (("999", "090", "076", "070"), 4, 5, (("Ia", "Ia2", 9), ("Ia", "Ia4", 111), ("Ia", "Ia7", 67), ("Ia", "Ia7", 128), ("Ia", "Ia14", 139))),
    (("600", "090", "076", "011"), 4, 2, (("Ia", "Ia2", 106), ("Ia", "Ia14", 53))),
    (("090", "076", "020", "010"), 4, 4, (("Ia", "Ia2", 119), ("Ia", "Ia4", 86), ("Ia", "Ia5", 143), ("Ia", "Ia12", 83))),
    (("076", "020", "010", "050"), 4, 2, (("Ia", "Ia2", 120), ("Ia", "Ia14", 110))),
    (("000", "999", "090", "076"), 4, 2, (("Ia", "Ia3", 35), ("Ia", "Ia5", 0))),
    (("999", "090", "076", "013"), 4, 2, (("Ia", "Ia3", 36), ("Ia", "Ia6", 91))),
    (("999", "205", "076", "071"), 4, 2, (("Ia", "Ia3", 51), ("Ia", "Ia3", 79))),
    (("999", "090", "076", "005"), 4, 2, (("Ia", "Ia3", 70), ("Ia", "Ia13", 108))),
    (("021", "090", "076", "087"), 4, 3, (("Ia", "Ia4", 116), ("Ia", "Ia5", 27), ("Ia", "Ia6", 77))),
    (("999", "090", "076", "071"), 4, 3, (("Ia", "Ia4", 153), ("Ia", "Ia5", 1), ("Ia", "Ia5", 22))),
    (("076", "010", "079", "090"), 4, 2, (("Ia", "Ia5", 110), ("Ia", "Ia5", 139))),
    (("072", "076", "010", "079"), 4, 2, (("Ia", "Ia5", 138), ("Ia", "Ia13", 71))),
    (("076", "071", "009", "090"), 4, 2, (("Ia", "Ia5", 161), ("Ia", "Ia12", 71))),
    (("202", "076", "006", "055"), 4, 2, (("Ia", "Ia6", 48), ("Ia", "Ia12", 119))),
    (("076", "071", "090", "999"), 4, 2, (("Ia", "Ia7", 166), ("Ia", "Ia14", 136))),
    (("076", "999", "029", "076"), 4, 2, (("Ia", "Ia8", 30), ("Ia", "Ia10", 144))),
    (("999", "021", "090", "076"), 4, 2, (("Ia", "Ia8", 104), ("Ia", "Ia13", 15))),
    (("090", "076", "057", "600"), 4, 2, (("Ia", "Ia8", 114), ("Ia", "Ia9", 28))),
    (("700", "076", "076", "053"), 4, 2, (("Ia", "Ia8", 167), ("Ia", "Ia9", 32))),
    (("071", "065", "071", "999"), 4, 2, (("Ia", "Ia9", 1), ("Ia", "Ia9", 56))),
    (("999", "090", "076", "057"), 4, 2, (("Ia", "Ia9", 27), ("Ia", "Ia9", 128))),
)
STANDING_MAXIMAL_NS = (
    5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
)
STANDING_CONTAINING = (
    (10,),
    (12,),
    (0,),
    (5,),
    (18,),
    (19,),
    (4,),
    (0,),
    (11,),
    (13,),
    (14,),
    (15,),
    (16,),
    (17,),
    (20,),
    (21,),
    (22,),
    (3,),
    (3,),
    (23,),
    (24,),
    (25,),
    (26,),
    (27,),
    (28,),
    (29,),
    (30,),
    (6,),
    (7,),
    (1,),
    (1,),
    (8,),
    (2,),
    (2,),
    (9,),
    (0,),
    (3,),
    (1,),
    (2,),
)
STANDING_SHARED_CORE = ()
STANDING_SHARED_CORE_COUNT = 0
STANDING_EXACTLY_ONE_NONMAXIMAL_COUNT = 8
STANDING_TWO_MAXIMAL_NONMAXIMAL_COUNT = 0
STANDING_EVERY_INDEPENDENT_IN_AT_LEAST_ONE = True
STANDING_EVERY_NONMAXIMAL_EXACTLY_ONE = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_independent_nge4_has_exactly_4_maximals"
STANDING_I_INDEPENDENT_NGE4_HAS_EXACTLY_4_MAXIMALS = False
STANDING_RESULT = "i_independent_nge4_maximals"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def leftover_n4_rows(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_INDEPENDENT,
    hypothesized: tuple[tuple[str, ...], ...] = STANDING_HYPOTHESIZED_N5,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Independent n=4 grams that are not substrings of the four n=5 grams."""
    return tuple(
        row
        for row in rows
        if row[1] == 4
        and not any(is_contiguous_substring(row[0], five) for five in hypothesized)
    )


def hypothesized_family_rows(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_INDEPENDENT,
    hypothesized: tuple[tuple[str, ...], ...] = STANDING_HYPOTHESIZED_N5,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Independent grams that sit inside at least one hypothesized n=5 gram."""
    return tuple(
        row
        for row in rows
        if any(is_contiguous_substring(row[0], five) for five in hypothesized)
    )


def i_independent_nge4_has_exactly_4_maximals(
    maximals: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> bool:
    """True iff the independent set collapses to exactly four maximals."""
    return len(maximals) == HYPOTHESIS_N


class TestIIndependentNge4MaximalHelpers(unittest.TestCase):
    """Helpers on cycle-135 tokens. No CV, no LLM."""

    def test_nested_family_is_four_maximals_and_n_equals_4_can_fail(self):
        """Four 5-grams hold N=4; leftover 4-grams and the full set lose."""
        provider = MockProvider()
        one_family = tuple(
            row
            for row in STANDING_INDEPENDENT
            if is_contiguous_substring(row[0], MAXIMAL_N5_430)
        )
        one = independent_maximals(one_family)
        self.assertEqual(len(one), 1)
        self.assertEqual(one[0][0], MAXIMAL_N5_430)
        self.assertFalse(i_independent_nge4_has_exactly_4_maximals(one))
        self.assertTrue(every_nonmaximal_is_substring_of_exactly_one(one_family, one))
        hypothesized = hypothesized_family_rows()
        four = independent_maximals(hypothesized)
        self.assertEqual(len(four), HYPOTHESIS_N)
        self.assertEqual(
            tuple(row[0] for row in four),
            (MAXIMAL_N5_430, MAXIMAL_N5_011, MAXIMAL_N5_400, MAXIMAL_N5_010),
        )
        self.assertTrue(i_independent_nge4_has_exactly_4_maximals(four))
        leftover = leftover_n4_rows()
        leftover_max = independent_maximals(leftover)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N4_COUNT)
        self.assertEqual(len(leftover_max), STANDING_LEFTOVER_N4_COUNT)
        self.assertEqual(
            {gram for gram, _n, _f, _s in leftover_max},
            {gram for gram, _n, _f, _s in leftover},
        )
        self.assertFalse(i_independent_nge4_has_exactly_4_maximals(leftover_max))
        thirty_one = independent_maximals(STANDING_INDEPENDENT)
        self.assertEqual(len(thirty_one), STANDING_N)
        self.assertEqual(thirty_one, STANDING_MAXIMALS)
        self.assertFalse(i_independent_nge4_has_exactly_4_maximals(thirty_one))
        self.assertFalse(i_independent_nge4_has_exactly_4_maximals(()))
        for five in STANDING_HYPOTHESIZED_N5:
            others = tuple(g for g in STANDING_HYPOTHESIZED_N5 if g != five)
            self.assertFalse(is_contained_in_longer(five, others))
            self.assertFalse(is_i_5gram_substring(five))
        self.assertTrue(is_contained_in_longer(N5_430_PREFIX, (MAXIMAL_N5_430,)))
        self.assertTrue(is_contained_in_longer(N5_430_SUFFIX, (MAXIMAL_N5_430,)))
        self.assertTrue(is_contained_in_longer(N5_010_PREFIX, (MAXIMAL_N5_010,)))
        self.assertTrue(is_contained_in_longer(N5_010_SUFFIX, (MAXIMAL_N5_010,)))
        self.assertTrue(is_contained_in_longer(N5_011_PREFIX, (MAXIMAL_N5_011,)))
        self.assertTrue(is_contained_in_longer(N5_011_SUFFIX, (MAXIMAL_N5_011,)))
        self.assertTrue(is_contained_in_longer(N5_400_PREFIX, (MAXIMAL_N5_400,)))
        self.assertTrue(is_contained_in_longer(N5_400_SUFFIX, (MAXIMAL_N5_400,)))
        self.assertEqual(STANDING_CLAIM, "i_independent_nge4_has_exactly_4_maximals")
        self.assertFalse(STANDING_I_INDEPENDENT_NGE4_HAS_EXACTLY_4_MAXIMALS)
        self.assertEqual(STANDING_N, 31)
        self.assertNotEqual(STANDING_N, HYPOTHESIS_N)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_n4s_are_not_substrings_of_the_four_5grams(self):
        """27 leftover n=4 grams sit in none of the hypothesized 5-grams."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N4_COUNT)
        for gram, n, _freq, _sites in leftover:
            self.assertEqual(n, 4)
            for five in STANDING_HYPOTHESIZED_N5:
                self.assertFalse(is_contiguous_substring(gram, five))
            self.assertFalse(is_contained_in_longer(
                gram,
                tuple(other for other, _n, _f, _s in STANDING_INDEPENDENT),
            ))
        maximals = independent_maximals(STANDING_INDEPENDENT)
        leftover_tokens = {gram for gram, _n, _f, _s in leftover}
        maximal_tokens = {gram for gram, _n, _f, _s in maximals}
        self.assertTrue(leftover_tokens.issubset(maximal_tokens))
        self.assertEqual(len(maximal_tokens), STANDING_N)
        self.assertEqual(STANDING_SHARED_CORE, ())
        self.assertEqual(STANDING_SHARED_CORE_COUNT, 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_every_independent_sits_in_exactly_one_maximal(self):
        """No shared core: each independent gram belongs to one maximal."""
        provider = MockProvider()
        maximals = independent_maximals(STANDING_INDEPENDENT)
        self.assertEqual(maximals, STANDING_MAXIMALS)
        self.assertTrue(is_contiguous_substring(N5_430_PREFIX, MAXIMAL_N5_430))
        self.assertTrue(is_contiguous_substring(N5_430_SUFFIX, MAXIMAL_N5_430))
        self.assertTrue(is_contiguous_substring(N5_010_PREFIX, MAXIMAL_N5_010))
        self.assertTrue(is_contiguous_substring(N5_010_SUFFIX, MAXIMAL_N5_010))
        self.assertTrue(is_contiguous_substring(N5_011_PREFIX, MAXIMAL_N5_011))
        self.assertTrue(is_contiguous_substring(N5_011_SUFFIX, MAXIMAL_N5_011))
        self.assertTrue(is_contiguous_substring(N5_400_PREFIX, MAXIMAL_N5_400))
        self.assertTrue(is_contiguous_substring(N5_400_SUFFIX, MAXIMAL_N5_400))
        self.assertEqual(containing_maximal_indexes(N5_430_PREFIX, maximals), (0,))
        self.assertEqual(containing_maximal_indexes(N5_430_SUFFIX, maximals), (0,))
        self.assertEqual(containing_maximal_indexes(N5_011_PREFIX, maximals), (1,))
        self.assertEqual(containing_maximal_indexes(N5_011_SUFFIX, maximals), (1,))
        self.assertEqual(containing_maximal_indexes(N5_400_PREFIX, maximals), (2,))
        self.assertEqual(containing_maximal_indexes(N5_400_SUFFIX, maximals), (2,))
        self.assertEqual(containing_maximal_indexes(N5_010_PREFIX, maximals), (3,))
        self.assertEqual(containing_maximal_indexes(N5_010_SUFFIX, maximals), (3,))
        self.assertEqual(containing_maximal_indexes(MAXIMAL_N5_430, maximals), (0,))
        self.assertTrue(
            every_nonmaximal_is_substring_of_exactly_one(STANDING_INDEPENDENT, maximals)
        )
        self.assertTrue(
            every_independent_in_at_least_one_maximal(STANDING_INDEPENDENT, maximals)
        )
        self.assertEqual(
            membership_rows(STANDING_INDEPENDENT, maximals),
            STANDING_CONTAINING,
        )
        self.assertFalse(every_nonmaximal_is_substring_of_exactly_one((), maximals))
        self.assertFalse(every_independent_in_at_least_one_maximal((), maximals))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIIndependentNge4MaximalsScoreboard(unittest.TestCase):
    """Cited-fixture I independent n≥4 maximals. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        prior = TestMamariINge4Scoreboard()
        prior.setUp()
        self.independent = prior.independent
        self.maximals = independent_maximals(self.independent)
        self.containing = membership_rows(self.independent, self.maximals)
        self.claim_holds = i_independent_nge4_has_exactly_4_maximals(self.maximals)

    def test_tokens_are_cycle_135_independent_not_invented(self):
        """Independent set is the cycle-135 lock, not a new inventory."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 39)
        prior = TestMamariINge4Scoreboard()
        prior.setUp()
        self.assertEqual(prior.independent, STANDING_INDEPENDENT)
        self.assertEqual(independent_rows(prior.rows), STANDING_INDEPENDENT)
        self.assertEqual(STANDING_HYPOTHESIZED_N5, STANDING_TIED_INDEP_N5)
        self.assertEqual(MAXIMAL_N5_430, STANDING_TIED_INDEP_N5[0])
        self.assertEqual(MAXIMAL_N5_010, STANDING_TIED_INDEP_N5[1])
        self.assertEqual(MAXIMAL_N5_011, STANDING_TIED_INDEP_N5[2])
        self.assertEqual(MAXIMAL_N5_400, STANDING_TIED_INDEP_N5[3])
        self.assertEqual(N5_430_PREFIX, MAXIMAL_N5_430[:4])
        self.assertEqual(N5_430_SUFFIX, MAXIMAL_N5_430[1:])
        self.assertEqual(N5_010_PREFIX, MAXIMAL_N5_010[:4])
        self.assertEqual(N5_010_SUFFIX, MAXIMAL_N5_010[1:])
        self.assertEqual(N5_011_PREFIX, MAXIMAL_N5_011[:4])
        self.assertEqual(N5_011_SUFFIX, MAXIMAL_N5_011[1:])
        self.assertEqual(N5_400_PREFIX, MAXIMAL_N5_400[:4])
        self.assertEqual(N5_400_SUFFIX, MAXIMAL_N5_400[1:])
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in STANDING_INDEPENDENT)
        for five in STANDING_HYPOTHESIZED_N5:
            self.assertIn(five, indep_tokens)
            self.assertFalse(is_contiguous_substring(five, GRAM5))
            self.assertFalse(is_i_5gram_substring(five))
        self.assertNotIn(GRAM5, indep_tokens)
        for nested in STANDING_NESTED_N4:
            self.assertIn(nested, indep_tokens)
        for five in STANDING_HYPOTHESIZED_N5:
            for other in STANDING_HYPOTHESIZED_N5:
                if five is other:
                    continue
                self.assertFalse(is_contiguous_substring(five, other))
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertEqual(self.survey["i_repeating_nge4"]["independent_count"], 39)
        self.assertFalse(self.survey["i_repeating_nge4"]["i_repeating_nge4_all_substrings_of_i_5gram"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n_is_31_and_hypothesis_n_4_loses(self):
        """39 independent grams collapse to 31 maximals. Claim is false."""
        self.assertEqual(len(self.maximals), STANDING_N)
        self.assertEqual(STANDING_N, 31)
        self.assertEqual(HYPOTHESIS_N, 4)
        self.assertNotEqual(STANDING_N, HYPOTHESIS_N)
        self.assertFalse(i_independent_nge4_has_exactly_4_maximals(self.maximals))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_INDEPENDENT_NGE4_HAS_EXACTLY_4_MAXIMALS,
        )
        self.assertFalse(STANDING_I_INDEPENDENT_NGE4_HAS_EXACTLY_4_MAXIMALS)
        self.assertEqual(STANDING_CLAIM, "i_independent_nge4_has_exactly_4_maximals")
        self.assertEqual(tuple(row[1] for row in self.maximals), STANDING_MAXIMAL_NS)
        self.assertEqual(STANDING_NONMAXIMAL_COUNT, STANDING_INDEPENDENT_COUNT - STANDING_N)
        self.assertEqual(STANDING_LEFTOVER_N4_COUNT, 27)
        self.assertEqual(
            STANDING_N,
            HYPOTHESIS_N + STANDING_LEFTOVER_N4_COUNT,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_maximals_and_membership_match_standing(self):
        """Measured maximals, sites, and membership match the lock."""
        self.assertEqual(self.maximals, STANDING_MAXIMALS)
        self.assertEqual(self.containing, STANDING_CONTAINING)
        self.assertEqual(len(STANDING_MAXIMALS), STANDING_N)
        for gram, n, freq, sites in self.maximals:
            self.assertEqual(len(gram), n)
            self.assertGreaterEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertEqual(len(sites), freq)
            self.assertFalse(is_contained_in_longer(
                gram,
                tuple(other for other, _n, _f, _s in STANDING_INDEPENDENT),
            ))
        maximal_tokens = tuple(gram for gram, _n, _f, _s in self.maximals)
        self.assertEqual(
            maximal_tokens[:4],
            (MAXIMAL_N5_430, MAXIMAL_N5_011, MAXIMAL_N5_400, MAXIMAL_N5_010),
        )
        self.assertEqual(sum(1 for gram in maximal_tokens if len(gram) == 5), 4)
        self.assertEqual(sum(1 for gram in maximal_tokens if len(gram) == 4), 27)
        nonmaximals = tuple(
            row for row in STANDING_INDEPENDENT if row[0] not in set(maximal_tokens)
        )
        self.assertEqual(len(nonmaximals), STANDING_NONMAXIMAL_COUNT)
        one_count = 0
        two_count = 0
        for gram, _n, _freq, _sites in nonmaximals:
            indexes = containing_maximal_indexes(gram, self.maximals)
            self.assertEqual(len(indexes), 1)
            one_count += 1
            self.assertIn(gram, STANDING_NESTED_N4)
        self.assertEqual(one_count, STANDING_EXACTLY_ONE_NONMAXIMAL_COUNT)
        self.assertEqual(two_count, STANDING_TWO_MAXIMAL_NONMAXIMAL_COUNT)
        self.assertEqual(two_count, STANDING_SHARED_CORE_COUNT)
        self.assertTrue(every_independent_in_at_least_one_maximal(self.independent, self.maximals))
        self.assertTrue(every_nonmaximal_is_substring_of_exactly_one(self.independent, self.maximals))
        self.assertEqual(
            STANDING_EVERY_INDEPENDENT_IN_AT_LEAST_ONE,
            True,
        )
        self.assertTrue(STANDING_EVERY_NONMAXIMAL_EXACTLY_ONE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_maximal_sites_on_i(self):
        """Maximal I sites; Ib unpublished; each site matches the locked stems."""
        self.assertEqual(self.maximals, STANDING_MAXIMALS)
        for gram, n, freq, sites in self.maximals:
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), freq)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
        self.assertEqual(
            STANDING_MAXIMALS[0][3],
            (("Ia", "Ia1", 129), ("Ia", "Ia14", 162)),
        )
        self.assertEqual(
            STANDING_MAXIMALS[1][3],
            (("Ia", "Ia12", 39), ("Ia", "Ia14", 102)),
        )
        self.assertEqual(
            STANDING_MAXIMALS[2][3],
            (("Ia", "Ia13", 85), ("Ia", "Ia14", 126)),
        )
        self.assertEqual(
            STANDING_MAXIMALS[3][3],
            (("Ia", "Ia6", 19), ("Ia", "Ia13", 72)),
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_135_123_103_and_w_scoreboards_still_compute(self):
        """Cycle 135 I n≥4, 123 A maximals, 103 I-only, and W stay."""
        prior_135 = TestMamariINge4Scoreboard()
        prior_135.setUp()
        prior_135.test_counts_and_hypothesis_all_substrings_loses()
        prior_135.test_survey_matches_computed_lock()
        prior_123 = TestMamariAIndependentNge8MaximalsScoreboard()
        prior_123.setUp()
        prior_123.test_n_is_2_and_hypothesis_n_2_holds()
        prior_123.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-136 independent maximal lock."""
        lock = self.survey["i_independent_nge4_maximals"]
        self.assertEqual(lock["cycle"], 136)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["maximal_count"], STANDING_N)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["nonmaximal_count"], STANDING_NONMAXIMAL_COUNT)
        self.assertEqual(lock["leftover_n4_count"], STANDING_LEFTOVER_N4_COUNT)
        measured_maximals = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
            }
            for tokens, n, freq, sites in STANDING_MAXIMALS
        ]
        self.assertEqual(lock["maximals"], measured_maximals)
        self.assertEqual(tuple(lock["maximal_ns"]), STANDING_MAXIMAL_NS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["containing"]),
            STANDING_CONTAINING,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["hypothesized_tokens5"]),
            STANDING_HYPOTHESIZED_N5,
        )
        self.assertEqual(lock["shared_core_count"], STANDING_SHARED_CORE_COUNT)
        self.assertEqual(
            lock["exactly_one_nonmaximal_count"],
            STANDING_EXACTLY_ONE_NONMAXIMAL_COUNT,
        )
        self.assertEqual(
            lock["two_maximal_nonmaximal_count"],
            STANDING_TWO_MAXIMAL_NONMAXIMAL_COUNT,
        )
        self.assertTrue(lock["every_independent_in_at_least_one"])
        self.assertEqual(
            lock["every_independent_in_at_least_one"],
            STANDING_EVERY_INDEPENDENT_IN_AT_LEAST_ONE,
        )
        self.assertTrue(lock["every_nonmaximal_exactly_one"])
        self.assertEqual(
            lock["every_nonmaximal_exactly_one"],
            STANDING_EVERY_NONMAXIMAL_EXACTLY_ONE,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_independent_nge4_has_exactly_4_maximals"])
        self.assertEqual(
            lock["i_independent_nge4_has_exactly_4_maximals"],
            STANDING_I_INDEPENDENT_NGE4_HAS_EXACTLY_4_MAXIMALS,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_repeating_nge4_unchanged"])
        self.assertTrue(lock["standing_a_independent_nge8_maximals_unchanged"])
        self.assertTrue(lock["standing_c_independent_nge8_maximals_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertFalse(
            self.survey["i_repeating_nge4"]["i_repeating_nge4_all_substrings_of_i_5gram"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["independent_count"], 39)
        self.assertEqual(self.survey["a_independent_nge8_maximals"]["cycle"], 123)
        self.assertTrue(
            self.survey["a_independent_nge8_maximals"]["a_independent_nge8_has_exactly_2_maximals"]
        )
        self.assertEqual(self.survey["c_independent_nge8_maximals"]["cycle"], 121)
        self.assertFalse(
            self.survey["c_independent_nge8_maximals"]["c_independent_nge8_has_exactly_2_maximals"]
        )
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


class TestMamariIIndependentNge4MaximalsImageSnapshot(unittest.TestCase):
    """Cycle 136 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
