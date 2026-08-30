"""I's cycle-136 leftover n=4 maximals vs n=2 076 070.

Cycle 205 text-search lock. Uses already-vendored A–V and the
cycle-136 leftover n=4 maximal set (27 independent n=4 grams
that are not substrings of the four I 5-grams). Does not retune
that set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Does not redo H∩P∩Q
n≥8 or G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Leftover 076 071 is now closed on both sides (cycles 170–204):
I-only 43/0; 34 leftover sites; forward clusters 076/600/090/700/061
plus 17 remaining hapax all I-only; previous clusters
700/090/604/099 plus 24 remaining hapax all I-only.
Same inventory move as cycle 166 (exactly 7 leftover n=4
maximals contain 999 090 076) and cycle 170 (exactly 4 leftover
n=4 maximals contain 076 071).

For each leftover n=4 maximal, whether it contains consecutive
2-token substring 076 070. 076 071 (999 090 076 071) does not
count. 076 076 (700 076 076 053) does not count. Hypothesis
N=1: exactly 1 of 27 does. Measured: 1 of 27 — 999 090 076 070.
The other 26 do not. Cycle 170 leftover n=4 vs 076 071 stays 4.
Cycle 166 leftover n=4 vs 999 090 076 stays 7. Cycle 136 leftover
n=4 set stays 27. Claim that can lose:
i_leftover_n4_exactly_1_contain_076_070.
True only if N_with_076_070=1. The claim is true.
Do not retune.

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
    STANDING_HYPOTHESIZED_N5,
    STANDING_LEFTOVER_N4_COUNT,
    STANDING_MAXIMALS,
    STANDING_N,
    TestMamariIIndependentNge4MaximalsScoreboard,
    leftover_n4_rows,
)
from tests.test_mamari_i_leftover_076_071_remaining_previous_4grams_i_only_scoreboard import (
    TestMamariILeftover076071RemainingPrevious4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    TestMamariILeftoverN4076071Scoreboard,
)
from tests.test_mamari_i_leftover_n4_999_090_076_scoreboard import (
    TestMamariILeftoverN4999090076Scoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
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

HYPOTHESIS_N = 1
STANDING_LEFTOVER_N4 = 27
GRAM2 = ("076", "070")
STANDING_N2 = 2
STANDING_WITH = 1
STANDING_WITHOUT = 26
NEAR_MISS_999_090_076_071 = ("999", "090", "076", "071")
NEAR_MISS_700_076_076_053 = ("700", "076", "076", "053")
STANDING_MATCHING_LEFTOVERS = (("999", "090", "076", "070"),)
STANDING_WITH_ROWS = tuple(
    row for row in STANDING_LEFTOVER if row[0] in STANDING_MATCHING_LEFTOVERS
)
STANDING_WITHOUT_ROWS = tuple(
    row for row in STANDING_LEFTOVER if row[0] not in STANDING_MATCHING_LEFTOVERS
)
STANDING_CONTAINS = tuple(
    is_contiguous_substring(GRAM2, gram) for gram, _n, _f, _s in STANDING_LEFTOVER
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_exactly_1_contain_076_070"
STANDING_I_LEFTOVER_N4_EXACTLY_1_CONTAIN_076_070 = True
STANDING_RESULT = "i_leftover_n4_076_070"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_076_071_DOES_NOT_COUNT = True


def gram_contains_076_070(
    gram: tuple[str, ...],
    needle: tuple[str, ...] = GRAM2,
) -> bool:
    """True iff 076 070 is a consecutive 2-token substring."""
    return is_contiguous_substring(needle, gram)


def leftover_with_076_070(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    needle: tuple[str, ...] = GRAM2,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that contain consecutive 076 070."""
    return tuple(row for row in leftovers if is_contiguous_substring(needle, row[0]))


def leftover_without_076_070(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    needle: tuple[str, ...] = GRAM2,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that do not contain consecutive 076 070."""
    return tuple(
        row for row in leftovers if not is_contiguous_substring(needle, row[0])
    )


def i_leftover_n4_exactly_1_contain_076_070(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    needle: tuple[str, ...] = GRAM2,
    expected: int = HYPOTHESIS_N,
) -> bool:
    """True iff exactly expected leftovers contain consecutive 076 070."""
    return len(leftover_with_076_070(leftovers, needle)) == expected


class TestILeftoverN4076070Helpers(unittest.TestCase):
    """Helpers on cycle-136 leftover n=4 vs 076 070. No CV, no LLM."""

    def test_contains_076_070_and_exactly_1_can_fail(self):
        """The 27 leftovers hold at 1; empty, 076 071-only, and a planted second lose."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N4)
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertTrue(gram_contains_076_070(("999", "090", "076", "070")))
        self.assertFalse(gram_contains_076_070(NEAR_MISS_999_090_076_071))
        self.assertFalse(gram_contains_076_070(NEAR_MISS_700_076_076_053))
        self.assertFalse(gram_contains_076_070(("076", "071", "009", "090")))
        self.assertFalse(gram_contains_076_070(("076", "071", "090", "999")))
        self.assertFalse(gram_contains_076_070(("090", "076", "057", "600")))
        self.assertTrue(
            is_contiguous_substring(("076", "071"), NEAR_MISS_999_090_076_071)
        )
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_999_090_076_071))
        self.assertTrue(
            is_contiguous_substring(("076", "076"), NEAR_MISS_700_076_076_053)
        )
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertFalse(i_leftover_n4_exactly_1_contain_076_070(()))
        with_gram = leftover_with_076_070(leftover)
        without_gram = leftover_without_076_070(leftover)
        self.assertEqual(len(with_gram), STANDING_WITH)
        self.assertEqual(len(without_gram), STANDING_WITHOUT)
        self.assertEqual(with_gram, STANDING_WITH_ROWS)
        self.assertEqual(without_gram, STANDING_WITHOUT_ROWS)
        self.assertTrue(i_leftover_n4_exactly_1_contain_076_070(leftover))
        self.assertTrue(i_leftover_n4_exactly_1_contain_076_070(with_gram))
        self.assertFalse(i_leftover_n4_exactly_1_contain_076_070(without_gram))
        self.assertFalse(i_leftover_n4_exactly_1_contain_076_070(()))
        planted = with_gram + (
            (("076", "070", "076", "070"), 4, 1, (("Ia", "Ia1", 0),)),
        )
        self.assertFalse(i_leftover_n4_exactly_1_contain_076_070(planted))
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_exactly_1_contain_076_070")
        self.assertTrue(STANDING_I_LEFTOVER_N4_EXACTLY_1_CONTAIN_076_070)
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_EXACTLY_1_CONTAIN_076_070,
            HYPOTHESIS_N == STANDING_WITH,
        )
        self.assertEqual(STANDING_WITH + STANDING_WITHOUT, STANDING_LEFTOVER_N4)
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
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4076070Scoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 vs 076 070. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.with_gram = leftover_with_076_070(self.leftover)
        self.without_gram = leftover_without_076_070(self.leftover)
        self.claim_holds = i_leftover_n4_exactly_1_contain_076_070(self.leftover)

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

    def test_counts_1_of_27_and_hypothesis_n_1_holds(self):
        """1 leftover contains 076 070; 26 do not. Claim is true."""
        self.assertEqual(len(self.leftover), STANDING_LEFTOVER_N4)
        self.assertEqual(len(self.with_gram), STANDING_WITH)
        self.assertEqual(len(self.without_gram), STANDING_WITHOUT)
        self.assertEqual(STANDING_WITH, 1)
        self.assertEqual(STANDING_WITHOUT, 26)
        self.assertEqual(STANDING_LEFTOVER_N4, STANDING_WITH + STANDING_WITHOUT)
        self.assertEqual(HYPOTHESIS_N, 1)
        self.assertTrue(i_leftover_n4_exactly_1_contain_076_070(self.leftover))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_EXACTLY_1_CONTAIN_076_070,
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_EXACTLY_1_CONTAIN_076_070)
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_exactly_1_contain_076_070")
        self.assertEqual(
            tuple(is_contiguous_substring(GRAM2, gram) for gram, _n, _f, _s in self.leftover),
            STANDING_CONTAINS,
        )
        self.assertEqual(sum(1 for flag in STANDING_CONTAINS if flag), STANDING_WITH)
        self.assertEqual(
            sum(1 for flag in STANDING_CONTAINS if not flag),
            STANDING_WITHOUT,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_leftover_only_the_expected_one(self):
        """One leftover contains 076 070; 076 071, 076 076, and the other 26 do not."""
        self.assertEqual(self.with_gram, STANDING_WITH_ROWS)
        self.assertEqual(self.without_gram, STANDING_WITHOUT_ROWS)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in self.with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
        for gram, n, freq, _sites in self.without_gram:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertFalse(gram_contains_076_070(gram))
            self.assertNotIn(gram, STANDING_MATCHING_LEFTOVERS)
        for gram, n, freq, _sites in self.with_gram:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertTrue(gram_contains_076_070(gram))
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertTrue(gram[:2] == GRAM2 or gram[1:3] == GRAM2 or gram[2:] == GRAM2)
        self.assertFalse(gram_contains_076_070(NEAR_MISS_999_090_076_071))
        self.assertFalse(gram_contains_076_070(NEAR_MISS_700_076_076_053))
        self.assertIn(
            NEAR_MISS_999_090_076_071,
            {g for g, _n, _f, _s in self.without_gram},
        )
        self.assertIn(
            NEAR_MISS_700_076_076_053,
            {g for g, _n, _f, _s in self.without_gram},
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_sites_on_i(self):
        """Leftover I sites; Ib unpublished; each site matches the locked stems."""
        self.assertEqual(self.leftover, STANDING_LEFTOVER)
        for gram, n, freq, sites in self.leftover:
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), freq)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_170_166_136_and_w_scoreboards_still_compute(self):
        """Cycle 170 leftover-4, 166 leftover-7, 136 leftover-27, 204, W stay."""
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_166 = TestMamariILeftoverN4999090076Scoreboard()
        prior_166.setUp()
        prior_166.test_counts_7_of_27_and_hypothesis_n_7_holds()
        prior_166.test_survey_matches_computed_lock()
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
        self.assertEqual(
            self.survey["i_independent_nge4_maximals"]["leftover_n4_count"],
            27,
        )
        prior_204 = TestMamariILeftover076071RemainingPrevious4gramsIOnlyScoreboard()
        prior_204.setUp()
        prior_204.test_survey_matches_computed_lock()
        prior_137 = TestMamariILeftoverN4Maximals076Scoreboard()
        prior_137.setUp()
        prior_137.test_counts_26_of_27_and_hypothesis_all_contain_loses()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        prior_135 = TestMamariINge4Scoreboard()
        prior_135.setUp()
        prior_135.test_counts_and_hypothesis_all_substrings_loses()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-205 leftover 076 070 lock."""
        lock = self.survey["i_leftover_n4_076_070"]
        self.assertEqual(lock["cycle"], 205)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["hypothesis_n"], 1)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["leftover_n4_count"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], 27)
        self.assertEqual(lock["with_076_070_count"], STANDING_WITH)
        self.assertEqual(lock["N_with_076_070"], STANDING_WITH)
        self.assertEqual(lock["N_with_076_070"], 1)
        self.assertEqual(lock["without_076_070_count"], STANDING_WITHOUT)
        self.assertEqual(lock["N_without_076_070"], STANDING_WITHOUT)
        self.assertEqual(lock["N_without_076_070"], 26)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(lock["matching_leftovers"], measured_matching)
        measured_leftovers = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
                "contains_076_070": is_contiguous_substring(GRAM2, tokens),
            }
            for tokens, n, freq, sites in STANDING_LEFTOVER
        ]
        self.assertEqual(lock["leftovers"], measured_leftovers)
        self.assertEqual(tuple(lock["contains_076_070"]), STANDING_CONTAINS)
        self.assertEqual(
            tuple(lock["near_miss_999_090_076_071"]),
            NEAR_MISS_999_090_076_071,
        )
        self.assertEqual(
            tuple(lock["near_miss_700_076_076_053"]),
            NEAR_MISS_700_076_076_053,
        )
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_exactly_1_contain_076_070"])
        self.assertEqual(
            lock["i_leftover_n4_exactly_1_contain_076_070"],
            STANDING_I_LEFTOVER_N4_EXACTLY_1_CONTAIN_076_070,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["same_inventory_move_as_cycle_166"])
        self.assertTrue(lock["same_inventory_move_as_cycle_170"])
        self.assertTrue(
            lock["standing_i_leftover_076_071_remaining_previous_4grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_999_090_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_repeating_nge4_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_previous_4grams_i_only"]["cycle"],
            204,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_remaining_previous_4grams_i_only"][
                "i_leftover_076_071_remaining_previous_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"]["i_leftover_n4_exactly_4_contain_076_071"]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["N_with_076_071"], 4)
        self.assertEqual(self.survey["i_leftover_n4_999_090_076"]["cycle"], 166)
        self.assertTrue(
            self.survey["i_leftover_n4_999_090_076"][
                "i_leftover_n4_exactly_7_contain_999_090_076"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_999_090_076"]["N_with_999_090_076"],
            7,
        )
        self.assertEqual(self.survey["i_leftover_n4_maximals_076"]["cycle"], 137)
        self.assertFalse(
            self.survey["i_leftover_n4_maximals_076"]["i_leftover_n4_maximals_all_contain_076"]
        )
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["maximal_count"], 31)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(
            self.survey["i_independent_nge4_maximals"]["i_independent_nge4_has_exactly_4_maximals"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertFalse(
            self.survey["i_repeating_nge4"]["i_repeating_nge4_all_substrings_of_i_5gram"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["independent_count"], 39)
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


class TestMamariILeftoverN4076070ImageSnapshot(unittest.TestCase):
    """Cycle 205 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
