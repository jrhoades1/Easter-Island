"""A's cycle-122 independent n≥8 grams collapsed to maximals.

Cycle 123 text-search lock. Uses already-vendored A–V and the
cycle-122 independent n≥8 set (4 grams that are not substrings
of the Aa 10-gram). Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
G–K n≥8 inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

A gram is maximal iff it is not a contiguous substring of a
longer independent gram. Hypothesis N_maximals=2: the cycle-38/39
Ab 9-gram and the leftover Ab 8-gram. Measured N=2: those two.
Every independent n≥8 is a contiguous substring of exactly one
of them. Claim that can lose:
a_independent_nge8_has_exactly_2_maximals. The claim is true.
Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_a_nge8_scoreboard import (
    AB_8EXTRA,
    AB_8PREFIX,
    AB_8SUFFIX,
    AB_9GRAM,
    STANDING_INDEPENDENT,
    STANDING_INDEPENDENT_COUNT,
    TestMamariANge8Scoreboard,
    independent_rows,
    is_n10_substring,
    nge8_sites,
)
from tests.test_mamari_a_tengram_scoreboard import (
    TestMamariATengramScoreboard,
)
from tests.test_mamari_c_independent_nge8_maximals_scoreboard import (
    TestMamariCIndependentNge8MaximalsScoreboard,
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
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_tahua_aa_a_only_scoreboard import (
    GRAM10,
    SIDE_AA,
    SIDE_AB,
    load_a_sides,
)
from tests.test_mamari_tahua_aa_scoreboard import AA_LINE_NAMES
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import (
    MOTIF_AB_9GRAM,
    PREFIX_AB_8GRAM,
)
from tests.test_mamari_tahua_ab_scoreboard import AB_LINE_NAMES

HYPOTHESIS_N = 2
STANDING_N = 2
STANDING_NONMAXIMAL_COUNT = 2
MAXIMAL_N9 = AB_9GRAM
MAXIMAL_N8 = AB_8EXTRA
STANDING_MAXIMALS = (
    (MAXIMAL_N9, 9, 2, (("Ab", "Ab3", 2), ("Ab", "Ab5", 13))),
    (MAXIMAL_N8, 8, 2, (("Ab", "Ab3", 22), ("Ab", "Ab5", 34))),
)
STANDING_MAXIMAL_NS = (9, 8)
STANDING_CONTAINING = (
    (0,),
    (0,),
    (1,),
    (0,),
)
STANDING_SHARED_CORE = ()
STANDING_SHARED_CORE_COUNT = 0
STANDING_EXACTLY_ONE_NONMAXIMAL_COUNT = 2
STANDING_TWO_MAXIMAL_NONMAXIMAL_COUNT = 0
STANDING_EVERY_INDEPENDENT_IN_AT_LEAST_ONE = True
STANDING_EVERY_NONMAXIMAL_EXACTLY_ONE = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "a_independent_nge8_has_exactly_2_maximals"
STANDING_A_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS = True
STANDING_RESULT = "a_independent_nge8_maximals"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def a_independent_nge8_has_exactly_2_maximals(
    maximals: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> bool:
    """True iff the independent set collapses to exactly two maximals."""
    return len(maximals) == HYPOTHESIS_N


class TestAIndependentNge8MaximalHelpers(unittest.TestCase):
    """Helpers on cycle-122 tokens. No CV, no LLM."""

    def test_nested_family_is_one_maximal_and_n_equals_2_can_fail(self):
        """Ab 9-gram nest is one maximal; 8-grams alone are 3; full set holds N=2."""
        provider = MockProvider()
        family = tuple(
            row
            for row in STANDING_INDEPENDENT
            if is_contiguous_substring(row[0], MAXIMAL_N9)
        )
        one = independent_maximals(family)
        self.assertEqual(len(one), 1)
        self.assertEqual(one[0][0], MAXIMAL_N9)
        self.assertFalse(a_independent_nge8_has_exactly_2_maximals(one))
        self.assertTrue(every_nonmaximal_is_substring_of_exactly_one(family, one))
        leftover_only = tuple(
            row for row in STANDING_INDEPENDENT if row[0] == MAXIMAL_N8
        )
        leftover = independent_maximals(leftover_only)
        self.assertEqual(len(leftover), 1)
        self.assertEqual(leftover[0][0], MAXIMAL_N8)
        self.assertFalse(a_independent_nge8_has_exactly_2_maximals(leftover))
        eight_only = tuple(row for row in STANDING_INDEPENDENT if row[1] == 8)
        three = independent_maximals(eight_only)
        self.assertEqual(len(three), 3)
        self.assertFalse(a_independent_nge8_has_exactly_2_maximals(three))
        two = independent_maximals(STANDING_INDEPENDENT)
        self.assertEqual(len(two), HYPOTHESIS_N)
        self.assertEqual(two, STANDING_MAXIMALS)
        self.assertTrue(a_independent_nge8_has_exactly_2_maximals(two))
        self.assertFalse(a_independent_nge8_has_exactly_2_maximals(()))
        self.assertFalse(is_contained_in_longer(MAXIMAL_N9, (MAXIMAL_N8,)))
        self.assertFalse(is_contained_in_longer(MAXIMAL_N8, (MAXIMAL_N9,)))
        self.assertTrue(is_contained_in_longer(AB_8PREFIX, (AB_9GRAM,)))
        self.assertTrue(is_contained_in_longer(AB_8SUFFIX, (AB_9GRAM,)))
        self.assertFalse(is_n10_substring(MAXIMAL_N9))
        self.assertFalse(is_n10_substring(MAXIMAL_N8))
        self.assertEqual(STANDING_CLAIM, "a_independent_nge8_has_exactly_2_maximals")
        self.assertTrue(STANDING_A_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS)
        self.assertEqual(STANDING_N, 2)
        self.assertEqual(STANDING_N, HYPOTHESIS_N)
        self.assertEqual(provider.get_call_history(), [])

    def test_every_independent_sits_in_exactly_one_maximal(self):
        """No shared core: each independent gram belongs to one maximal."""
        provider = MockProvider()
        maximals = independent_maximals(STANDING_INDEPENDENT)
        self.assertEqual(maximals, STANDING_MAXIMALS)
        self.assertTrue(is_contiguous_substring(AB_8PREFIX, MAXIMAL_N9))
        self.assertTrue(is_contiguous_substring(AB_8SUFFIX, MAXIMAL_N9))
        self.assertFalse(is_contiguous_substring(AB_8EXTRA, MAXIMAL_N9))
        self.assertFalse(is_contiguous_substring(MAXIMAL_N9, MAXIMAL_N8))
        self.assertEqual(containing_maximal_indexes(AB_8PREFIX, maximals), (0,))
        self.assertEqual(containing_maximal_indexes(AB_8SUFFIX, maximals), (0,))
        self.assertEqual(containing_maximal_indexes(AB_8EXTRA, maximals), (1,))
        self.assertEqual(containing_maximal_indexes(AB_9GRAM, maximals), (0,))
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
        self.assertEqual(STANDING_SHARED_CORE, ())
        self.assertEqual(STANDING_SHARED_CORE_COUNT, 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariAIndependentNge8MaximalsScoreboard(unittest.TestCase):
    """Cited-fixture A independent n≥8 maximals. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.a_sides = load_a_sides()
        prior = TestMamariANge8Scoreboard()
        prior.setUp()
        self.independent = prior.independent
        self.maximals = independent_maximals(self.independent)
        self.containing = membership_rows(self.independent, self.maximals)
        self.claim_holds = a_independent_nge8_has_exactly_2_maximals(self.maximals)

    def test_tokens_are_cycle_122_independent_not_invented(self):
        """Independent set is the cycle-122 lock, not a new inventory."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 4)
        prior = TestMamariANge8Scoreboard()
        prior.setUp()
        self.assertEqual(prior.independent, STANDING_INDEPENDENT)
        self.assertEqual(independent_rows(prior.rows), STANDING_INDEPENDENT)
        self.assertEqual(MAXIMAL_N9, AB_9GRAM)
        self.assertEqual(MAXIMAL_N9, MOTIF_AB_9GRAM)
        self.assertEqual(AB_8PREFIX, PREFIX_AB_8GRAM)
        self.assertEqual(AB_8PREFIX, AB_9GRAM[:8])
        self.assertEqual(AB_8SUFFIX, AB_9GRAM[1:])
        self.assertEqual(MAXIMAL_N8, AB_8EXTRA)
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in STANDING_INDEPENDENT)
        self.assertIn(MAXIMAL_N9, indep_tokens)
        self.assertIn(MAXIMAL_N8, indep_tokens)
        self.assertIn(AB_8PREFIX, indep_tokens)
        self.assertIn(AB_8SUFFIX, indep_tokens)
        self.assertNotIn(GRAM10, indep_tokens)
        self.assertFalse(is_contiguous_substring(MAXIMAL_N8, MAXIMAL_N9))
        self.assertFalse(is_contiguous_substring(MAXIMAL_N9, MAXIMAL_N8))
        self.assertFalse(is_contiguous_substring(MAXIMAL_N9, GRAM10))
        self.assertFalse(is_contiguous_substring(MAXIMAL_N8, GRAM10))
        self.assertEqual(self.survey["a_repeating_nge8"]["cycle"], 122)
        self.assertEqual(self.survey["a_repeating_nge8"]["independent_count"], 4)
        self.assertFalse(self.survey["a_repeating_nge8"]["a_repeating_nge8_all_substrings_of_n10"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n_is_2_and_hypothesis_n_2_holds(self):
        """4 independent grams collapse to 2 maximals. Claim is true."""
        self.assertEqual(len(self.maximals), STANDING_N)
        self.assertEqual(STANDING_N, 2)
        self.assertEqual(HYPOTHESIS_N, 2)
        self.assertEqual(STANDING_N, HYPOTHESIS_N)
        self.assertTrue(a_independent_nge8_has_exactly_2_maximals(self.maximals))
        self.assertEqual(self.claim_holds, STANDING_A_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS)
        self.assertTrue(STANDING_A_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS)
        self.assertEqual(STANDING_CLAIM, "a_independent_nge8_has_exactly_2_maximals")
        self.assertEqual(tuple(row[1] for row in self.maximals), STANDING_MAXIMAL_NS)
        self.assertEqual(STANDING_NONMAXIMAL_COUNT, STANDING_INDEPENDENT_COUNT - STANDING_N)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_maximals_and_membership_match_standing(self):
        """Measured maximals, sites, and membership match the lock."""
        self.assertEqual(self.maximals, STANDING_MAXIMALS)
        self.assertEqual(self.containing, STANDING_CONTAINING)
        self.assertEqual(len(STANDING_MAXIMALS), STANDING_N)
        for gram, n, freq, sites in self.maximals:
            self.assertEqual(len(gram), n)
            self.assertGreaterEqual(n, 8)
            self.assertGreaterEqual(freq, 2)
            self.assertEqual(len(sites), freq)
            self.assertFalse(is_contained_in_longer(
                gram,
                tuple(other for other, _n, _f, _s in STANDING_INDEPENDENT),
            ))
        maximal_tokens = tuple(gram for gram, _n, _f, _s in self.maximals)
        self.assertEqual(maximal_tokens, (MAXIMAL_N9, MAXIMAL_N8))
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
            self.assertIn(gram, {AB_8PREFIX, AB_8SUFFIX})
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

    def test_maximal_sites_on_a(self):
        """Maximal A sites; Aa=0; each site matches the locked stems."""
        self.assertEqual(self.maximals, STANDING_MAXIMALS)
        for gram, n, freq, sites in self.maximals:
            self.assertEqual(nge8_sites(gram, self.a_sides), sites)
            self.assertEqual(ngram_hit_count(self.a_sides[SIDE_AA], gram), 0)
            self.assertEqual(ngram_hit_count(self.a_sides[SIDE_AB], gram), freq)
            for side, line, index in sites:
                names = AA_LINE_NAMES if side == SIDE_AA else AB_LINE_NAMES
                stems = self.a_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_AB)
                self.assertIn(line, ("Ab3", "Ab5"))
        self.assertEqual(STANDING_MAXIMALS[0][3], (("Ab", "Ab3", 2), ("Ab", "Ab5", 13)))
        self.assertEqual(STANDING_MAXIMALS[1][3], (("Ab", "Ab3", 22), ("Ab", "Ab5", 34)))
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_122_121_117_and_w_scoreboards_still_compute(self):
        """Cycle 122 A n≥8, 121 C maximals, 117 A 10-grams, and W stay."""
        prior_122 = TestMamariANge8Scoreboard()
        prior_122.setUp()
        prior_122.test_counts_and_hypothesis_all_substrings_loses()
        prior_122.test_survey_matches_computed_lock()
        prior_121 = TestMamariCIndependentNge8MaximalsScoreboard()
        prior_121.setUp()
        prior_121.test_n_is_3_and_hypothesis_n_2_loses()
        prior_121.test_survey_matches_computed_lock()
        prior_117 = TestMamariATengramScoreboard()
        prior_117.setUp()
        prior_117.test_n_is_1_and_hypothesis_n_1_holds()
        prior_117.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-123 independent maximal lock."""
        lock = self.survey["a_independent_nge8_maximals"]
        self.assertEqual(lock["cycle"], 123)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["maximal_count"], STANDING_N)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["nonmaximal_count"], STANDING_NONMAXIMAL_COUNT)
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
        self.assertTrue(lock["a_independent_nge8_has_exactly_2_maximals"])
        self.assertEqual(
            lock["a_independent_nge8_has_exactly_2_maximals"],
            STANDING_A_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_a_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_c_independent_nge8_maximals_unchanged"])
        self.assertTrue(lock["standing_c_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_a_repeating_10grams_unchanged"])
        self.assertTrue(lock["standing_tahua_aa_a_only_unchanged"])
        self.assertTrue(lock["standing_tahua_ab_9gram_motif_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["a_repeating_nge8"]["cycle"], 122)
        self.assertFalse(self.survey["a_repeating_nge8"]["a_repeating_nge8_all_substrings_of_n10"])
        self.assertEqual(self.survey["c_independent_nge8_maximals"]["cycle"], 121)
        self.assertFalse(
            self.survey["c_independent_nge8_maximals"]["c_independent_nge8_has_exactly_2_maximals"]
        )
        self.assertEqual(self.survey["c_repeating_nge8"]["cycle"], 120)
        self.assertFalse(self.survey["c_repeating_nge8"]["c_repeating_nge8_all_substrings_of_n13"])
        self.assertEqual(self.survey["a_repeating_10grams"]["cycle"], 117)
        self.assertTrue(self.survey["a_repeating_10grams"]["a_has_exactly_1_repeating_10gram"])
        self.assertEqual(self.survey["tablet_a_tahua_aa_a_only"]["cycle"], 116)
        self.assertTrue(self.survey["tablet_a_tahua_aa_a_only"]["a_10gram_is_a_only"])
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["cycle"], 39)
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["motif_freq"], 2)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["longest_count"], 1)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariAIndependentNge8MaximalsImageSnapshot(unittest.TestCase):
    """Cycle 123 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
