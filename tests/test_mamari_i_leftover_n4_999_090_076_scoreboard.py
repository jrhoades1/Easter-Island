"""I's cycle-136 leftover n=4 maximals vs n=3 999 090 076.

Cycle 166 text-search lock. Uses already-vendored A–V and the
cycle-136 leftover n=4 maximal set (27 independent n=4 grams
that are not substrings of the four I 5-grams). Does not retune
that set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Does not redo H∩P∩Q
n≥8 or G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

For each leftover n=4 maximal, whether it contains consecutive
3-token substring 999 090 076. n=2 (090 076 without 999) does
not count. Hypothesis N=7: exactly 7 of 27 do. Measured: 7 of
27 — 999 090 076 070, 999 090 076 071, 000 999 090 076,
999 090 076 013, 999 090 076 005, 999 090 076 057, and
090 999 090 076. The other 20 do not (including 600 090 076 011
and 999 021 090 076). Cycle 165 leftover forward 4-grams stay
I-only hapax 1/0. Cycle 159 leftover n=4 vs independent n=5
n≥3 overlap stays 5. Claim that can lose:
i_leftover_n4_exactly_7_contain_999_090_076.
True only if N_with_999_090_076=7. The claim is true.
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
from tests.test_mamari_i_leftover_076_020_010_forward_4grams_i_only_scoreboard import (
    TestMamariILeftover076020010Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_independent_n5_n3_overlap_scoreboard import (
    TestMamariILeftoverN4IndependentN5N3OverlapScoreboard,
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

HYPOTHESIS_N = 7
STANDING_LEFTOVER_N4 = 27
GRAM3 = ("999", "090", "076")
STANDING_N3 = 3
STANDING_WITH = 7
STANDING_WITHOUT = 20
NEAR_MISS_N2_090_076 = ("600", "090", "076", "011")
NEAR_MISS_999_021_090_076 = ("999", "021", "090", "076")
STANDING_MATCHING_LEFTOVERS = (
    ("999", "090", "076", "070"),
    ("999", "090", "076", "071"),
    ("000", "999", "090", "076"),
    ("999", "090", "076", "013"),
    ("999", "090", "076", "005"),
    ("999", "090", "076", "057"),
    ("090", "999", "090", "076"),
)
STANDING_WITH_ROWS = tuple(
    row for row in STANDING_LEFTOVER if row[0] in STANDING_MATCHING_LEFTOVERS
)
STANDING_WITHOUT_ROWS = tuple(
    row for row in STANDING_LEFTOVER if row[0] not in STANDING_MATCHING_LEFTOVERS
)
STANDING_CONTAINS = tuple(
    is_contiguous_substring(GRAM3, gram) for gram, _n, _f, _s in STANDING_LEFTOVER
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_exactly_7_contain_999_090_076"
STANDING_I_LEFTOVER_N4_EXACTLY_7_CONTAIN_999_090_076 = True
STANDING_RESULT = "i_leftover_n4_999_090_076"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_N2_DOES_NOT_COUNT = True


def gram_contains_999_090_076(
    gram: tuple[str, ...],
    needle: tuple[str, ...] = GRAM3,
) -> bool:
    """True iff 999 090 076 is a consecutive 3-token substring."""
    return is_contiguous_substring(needle, gram)


def leftover_with_999_090_076(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    needle: tuple[str, ...] = GRAM3,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that contain consecutive 999 090 076."""
    return tuple(row for row in leftovers if is_contiguous_substring(needle, row[0]))


def leftover_without_999_090_076(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    needle: tuple[str, ...] = GRAM3,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that do not contain consecutive 999 090 076."""
    return tuple(
        row for row in leftovers if not is_contiguous_substring(needle, row[0])
    )


def i_leftover_n4_exactly_7_contain_999_090_076(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    needle: tuple[str, ...] = GRAM3,
    expected: int = HYPOTHESIS_N,
) -> bool:
    """True iff exactly expected leftovers contain consecutive 999 090 076."""
    return len(leftover_with_999_090_076(leftovers, needle)) == expected


class TestILeftoverN4999090076Helpers(unittest.TestCase):
    """Helpers on cycle-136 leftover n=4 vs 999 090 076. No CV, no LLM."""

    def test_contains_999_090_076_and_exactly_7_can_fail(self):
        """The 27 leftovers hold at 7; empty, n=2-only, and a planted eighth lose."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N4)
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertTrue(gram_contains_999_090_076(("999", "090", "076", "070")))
        self.assertTrue(gram_contains_999_090_076(("000", "999", "090", "076")))
        self.assertTrue(gram_contains_999_090_076(("090", "999", "090", "076")))
        self.assertFalse(gram_contains_999_090_076(NEAR_MISS_N2_090_076))
        self.assertFalse(gram_contains_999_090_076(NEAR_MISS_999_021_090_076))
        self.assertFalse(gram_contains_999_090_076(("021", "090", "076", "087")))
        self.assertFalse(gram_contains_999_090_076(("090", "076", "057", "600")))
        self.assertTrue(is_contiguous_substring(("090", "076"), NEAR_MISS_N2_090_076))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_N2_090_076))
        self.assertTrue(is_contiguous_substring(("999", "021", "090"), NEAR_MISS_999_021_090_076))
        self.assertTrue(is_contiguous_substring(("021", "090", "076"), NEAR_MISS_999_021_090_076))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_999_021_090_076))
        self.assertFalse(i_leftover_n4_exactly_7_contain_999_090_076(()))
        with_gram = leftover_with_999_090_076(leftover)
        without_gram = leftover_without_999_090_076(leftover)
        self.assertEqual(len(with_gram), STANDING_WITH)
        self.assertEqual(len(without_gram), STANDING_WITHOUT)
        self.assertEqual(with_gram, STANDING_WITH_ROWS)
        self.assertEqual(without_gram, STANDING_WITHOUT_ROWS)
        self.assertTrue(i_leftover_n4_exactly_7_contain_999_090_076(leftover))
        self.assertTrue(i_leftover_n4_exactly_7_contain_999_090_076(with_gram))
        self.assertFalse(i_leftover_n4_exactly_7_contain_999_090_076(without_gram))
        self.assertFalse(i_leftover_n4_exactly_7_contain_999_090_076(with_gram[:6]))
        planted = with_gram + (
            (("999", "090", "076", "999"), 4, 1, (("Ia", "Ia1", 0),)),
        )
        self.assertFalse(i_leftover_n4_exactly_7_contain_999_090_076(planted))
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_exactly_7_contain_999_090_076")
        self.assertTrue(STANDING_I_LEFTOVER_N4_EXACTLY_7_CONTAIN_999_090_076)
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_EXACTLY_7_CONTAIN_999_090_076,
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
        self.assertTrue(STANDING_N2_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4999090076Scoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 vs 999 090 076. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.with_gram = leftover_with_999_090_076(self.leftover)
        self.without_gram = leftover_without_999_090_076(self.leftover)
        self.claim_holds = i_leftover_n4_exactly_7_contain_999_090_076(self.leftover)

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

    def test_counts_7_of_27_and_hypothesis_n_7_holds(self):
        """7 leftovers contain 999 090 076; 20 do not. Claim is true."""
        self.assertEqual(len(self.leftover), STANDING_LEFTOVER_N4)
        self.assertEqual(len(self.with_gram), STANDING_WITH)
        self.assertEqual(len(self.without_gram), STANDING_WITHOUT)
        self.assertEqual(STANDING_WITH, 7)
        self.assertEqual(STANDING_WITHOUT, 20)
        self.assertEqual(STANDING_LEFTOVER_N4, STANDING_WITH + STANDING_WITHOUT)
        self.assertEqual(HYPOTHESIS_N, 7)
        self.assertTrue(i_leftover_n4_exactly_7_contain_999_090_076(self.leftover))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_EXACTLY_7_CONTAIN_999_090_076,
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_EXACTLY_7_CONTAIN_999_090_076)
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_exactly_7_contain_999_090_076")
        self.assertEqual(
            tuple(is_contiguous_substring(GRAM3, gram) for gram, _n, _f, _s in self.leftover),
            STANDING_CONTAINS,
        )
        self.assertEqual(sum(1 for flag in STANDING_CONTAINS if flag), STANDING_WITH)
        self.assertEqual(
            sum(1 for flag in STANDING_CONTAINS if not flag),
            STANDING_WITHOUT,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_leftover_only_the_expected_seven(self):
        """Seven leftovers contain 999 090 076; n=2 pairs and the other 20 do not."""
        self.assertEqual(self.with_gram, STANDING_WITH_ROWS)
        self.assertEqual(self.without_gram, STANDING_WITHOUT_ROWS)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in self.with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
        for gram, n, freq, _sites in self.without_gram:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertFalse(gram_contains_999_090_076(gram))
            self.assertNotIn(gram, STANDING_MATCHING_LEFTOVERS)
        for gram, n, freq, _sites in self.with_gram:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertTrue(gram_contains_999_090_076(gram))
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertTrue(gram[:3] == GRAM3 or gram[1:] == GRAM3)
        self.assertFalse(gram_contains_999_090_076(NEAR_MISS_N2_090_076))
        self.assertFalse(gram_contains_999_090_076(NEAR_MISS_999_021_090_076))
        self.assertIn(NEAR_MISS_N2_090_076, {g for g, _n, _f, _s in self.without_gram})
        self.assertIn(
            NEAR_MISS_999_021_090_076,
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

    def test_existing_165_159_137_136_103_and_w_scoreboards_still_compute(self):
        """Cycle 165 I-only, 159 n≥3, 137 leftover 076, 136 maximals, 103, W stay."""
        prior_165 = TestMamariILeftover076020010Forward4gramsIOnlyScoreboard()
        prior_165.setUp()
        prior_165.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_165.test_survey_matches_computed_lock()
        prior_159 = TestMamariILeftoverN4IndependentN5N3OverlapScoreboard()
        prior_159.setUp()
        prior_159.test_counts_5_of_27_and_hypothesis_n_5_holds()
        prior_159.test_survey_matches_computed_lock()
        prior_137 = TestMamariILeftoverN4Maximals076Scoreboard()
        prior_137.setUp()
        prior_137.test_counts_26_of_27_and_hypothesis_all_contain_loses()
        prior_137.test_survey_matches_computed_lock()
        prior_136 = TestMamariIIndependentNge4MaximalsScoreboard()
        prior_136.setUp()
        prior_136.test_n_is_31_and_hypothesis_n_4_loses()
        prior_136.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-166 leftover 999 090 076 lock."""
        lock = self.survey["i_leftover_n4_999_090_076"]
        self.assertEqual(lock["cycle"], 166)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["hypothesis_n"], 7)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["leftover_n4_count"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], 27)
        self.assertEqual(lock["with_999_090_076_count"], STANDING_WITH)
        self.assertEqual(lock["N_with_999_090_076"], STANDING_WITH)
        self.assertEqual(lock["N_with_999_090_076"], 7)
        self.assertEqual(lock["without_999_090_076_count"], STANDING_WITHOUT)
        self.assertEqual(lock["N_without_999_090_076"], STANDING_WITHOUT)
        self.assertEqual(lock["N_without_999_090_076"], 20)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(lock["matching_leftovers"], measured_matching)
        measured_leftovers = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
                "contains_999_090_076": is_contiguous_substring(GRAM3, tokens),
            }
            for tokens, n, freq, sites in STANDING_LEFTOVER
        ]
        self.assertEqual(lock["leftovers"], measured_leftovers)
        self.assertEqual(tuple(lock["contains_999_090_076"]), STANDING_CONTAINS)
        self.assertEqual(tuple(lock["near_miss_n2_090_076"]), NEAR_MISS_N2_090_076)
        self.assertEqual(
            tuple(lock["near_miss_999_021_090_076"]),
            NEAR_MISS_999_021_090_076,
        )
        self.assertTrue(lock["n2_090_076_without_999_does_not_count"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_exactly_7_contain_999_090_076"])
        self.assertEqual(
            lock["i_leftover_n4_exactly_7_contain_999_090_076"],
            STANDING_I_LEFTOVER_N4_EXACTLY_7_CONTAIN_999_090_076,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"])
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
            self.survey["i_leftover_076_020_010_forward_4grams_i_only"]["cycle"], 165
        )
        self.assertTrue(
            self.survey["i_leftover_076_020_010_forward_4grams_i_only"][
                "i_leftover_076_020_010_forward_4grams_all_i_only"
            ]
        )
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


class TestMamariILeftoverN4999090076ImageSnapshot(unittest.TestCase):
    """Cycle 166 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
