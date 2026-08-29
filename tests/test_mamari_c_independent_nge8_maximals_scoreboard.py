"""C's cycle-120 independent n≥8 grams collapsed to maximals.

Cycle 121 text-search lock. Uses already-vendored A–V and the
cycle-120 independent n≥8 set (11 grams that are not substrings
of the calendar 13-gram). Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
G–K n≥8 inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

A gram is maximal iff it is not a contiguous substring of a
longer independent gram. Hypothesis N_maximals=2: the n=12
Guy+trailing-040 tail and the cycle-29/30 remainder 9-gram.
Measured N=3: those two plus the two-trailing-040 tail, which
is not a substring of the n=12. Claim that can lose:
c_independent_nge8_has_exactly_2_maximals. The claim is false.
Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_ca_c_only_scoreboard import (
    CA_LINE_NAMES,
    GRAM13,
    SIDE_CA,
    SIDE_CB,
    TestMamariCaCOnlyScoreboard,
    load_c_sides,
)
from tests.test_mamari_c_nge8_scoreboard import (
    STANDING_INDEPENDENT,
    STANDING_INDEPENDENT_COUNT,
    TestMamariCNge8Scoreboard,
    independent_rows,
    is_n13_substring,
    nge8_sites,
)
from tests.test_mamari_c_thirteengram_scoreboard import (
    TestMamariCThirteengramScoreboard,
)
from tests.test_mamari_cb_side_b_scoreboard import CB_LINE_NAMES
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import MOTIF_9GRAM
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_LONGEST_NGRAM as REMAINDER_9GRAM,
    STANDING_TOP_8GRAM as REMAINDER_8PREFIX,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

REMAINDER_8SUFFIX = (
    "010",
    "070",
    "760",
    "040",
    "006",
    "430",
    "047",
    "002",
)
HYPOTHESIS_N = 2
STANDING_N = 3
STANDING_NONMAXIMAL_COUNT = 8
MAXIMAL_N12 = (
    "040",
    "040",
    "040",
    "390",
    "041",
    "378",
    "041",
    "670",
    "008",
    "078",
    "711",
    "040",
)
MAXIMAL_N10 = (
    "390",
    "041",
    "378",
    "041",
    "670",
    "008",
    "078",
    "711",
    "040",
    "040",
)
MAXIMAL_N9 = REMAINDER_9GRAM
STANDING_MAXIMALS = (
    (MAXIMAL_N12, 12, 2, (("Ca", "Ca7", 3), ("Ca", "Ca8", 0))),
    (MAXIMAL_N10, 10, 2, (("Ca", "Ca7", 33), ("Ca", "Ca8", 3))),
    (MAXIMAL_N9, 9, 2, (("Ca", "Ca10", 26), ("Ca", "Ca11", 14))),
)
STANDING_MAXIMAL_NS = (12, 10, 9)
STANDING_CONTAINING = (
    (0, 1),
    (1,),
    (2,),
    (2,),
    (0, 1),
    (1,),
    (2,),
    (0,),
    (1,),
    (0,),
    (0,),
)
STANDING_SHARED_CORE = (
    ("041", "378", "041", "670", "008", "078", "711", "040"),
    ("390", "041", "378", "041", "670", "008", "078", "711", "040"),
)
STANDING_SHARED_CORE_COUNT = 2
STANDING_EXACTLY_ONE_NONMAXIMAL_COUNT = 6
STANDING_TWO_MAXIMAL_NONMAXIMAL_COUNT = 2
STANDING_EVERY_INDEPENDENT_IN_AT_LEAST_ONE = True
STANDING_EVERY_NONMAXIMAL_EXACTLY_ONE = False
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "c_independent_nge8_has_exactly_2_maximals"
STANDING_C_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS = False
STANDING_RESULT = "c_independent_nge8_maximals"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def is_contained_in_longer(
    gram: tuple[str, ...],
    tokens_list: tuple[tuple[str, ...], ...] | list[tuple[str, ...]],
) -> bool:
    """True iff gram is a contiguous run inside a strictly longer gram."""
    return any(
        is_contiguous_substring(gram, other)
        for other in tokens_list
        if len(other) > len(gram)
    )


def independent_maximals(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Independent grams that are not substrings of a longer independent gram."""
    tokens = tuple(gram for gram, _n, _freq, _sites in rows)
    kept = tuple(
        row for row in rows if not is_contained_in_longer(row[0], tokens)
    )
    return tuple(sorted(kept, key=lambda row: (-row[1], row[3][0] if row[3] else ())))


def containing_maximal_indexes(
    gram: tuple[str, ...],
    maximals: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> tuple[int, ...]:
    """Indexes of maximals that contain gram as a contiguous run."""
    return tuple(
        index
        for index, (tokens, _n, _freq, _sites) in enumerate(maximals)
        if is_contiguous_substring(gram, tokens)
    )


def membership_rows(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    maximals: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> tuple[tuple[int, ...], ...]:
    """Per-independent-gram maximal membership indexes."""
    return tuple(containing_maximal_indexes(gram, maximals) for gram, _n, _f, _s in rows)


def every_independent_in_at_least_one_maximal(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    maximals: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> bool:
    """True iff every independent gram sits inside at least one maximal."""
    return bool(rows) and bool(maximals) and all(
        containing_maximal_indexes(gram, maximals) for gram, _n, _f, _s in rows
    )


def every_nonmaximal_is_substring_of_exactly_one(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    maximals: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> bool:
    """True iff every non-maximal independent gram sits in exactly one maximal."""
    maximal_tokens = {tokens for tokens, _n, _freq, _sites in maximals}
    counts = [
        len(containing_maximal_indexes(gram, maximals))
        for gram, _n, _freq, _sites in rows
        if gram not in maximal_tokens
    ]
    return bool(counts) and all(count == 1 for count in counts)


def c_independent_nge8_has_exactly_2_maximals(
    maximals: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
) -> bool:
    """True iff the independent set collapses to exactly two maximals."""
    return len(maximals) == HYPOTHESIS_N


class TestCIndependentNge8MaximalHelpers(unittest.TestCase):
    """Helpers on cycle-120 tokens. No CV, no LLM."""

    def test_nested_family_is_one_maximal_and_n_equals_2_can_fail(self):
        """Remainder nest is one maximal; two families hold N=2; the third loses."""
        provider = MockProvider()
        remainder_family = tuple(
            row for row in STANDING_INDEPENDENT if row[0] in {
                REMAINDER_9GRAM,
                REMAINDER_8PREFIX,
                REMAINDER_8SUFFIX,
            }
        )
        one = independent_maximals(remainder_family)
        self.assertEqual(len(one), 1)
        self.assertEqual(one[0][0], REMAINDER_9GRAM)
        self.assertFalse(c_independent_nge8_has_exactly_2_maximals(one))
        self.assertTrue(every_nonmaximal_is_substring_of_exactly_one(remainder_family, one))
        hypothesized = tuple(
            row
            for row in STANDING_INDEPENDENT
            if is_contiguous_substring(row[0], MAXIMAL_N12)
            or is_contiguous_substring(row[0], MAXIMAL_N9)
        )
        two = independent_maximals(hypothesized)
        self.assertEqual(len(two), HYPOTHESIS_N)
        self.assertTrue(c_independent_nge8_has_exactly_2_maximals(two))
        three = independent_maximals(STANDING_INDEPENDENT)
        self.assertEqual(len(three), STANDING_N)
        self.assertEqual(three, STANDING_MAXIMALS)
        self.assertFalse(c_independent_nge8_has_exactly_2_maximals(three))
        self.assertFalse(c_independent_nge8_has_exactly_2_maximals(()))
        self.assertFalse(is_contained_in_longer(MAXIMAL_N12, (MAXIMAL_N10, MAXIMAL_N9)))
        self.assertFalse(is_contained_in_longer(MAXIMAL_N10, (MAXIMAL_N12, MAXIMAL_N9)))
        self.assertFalse(is_contained_in_longer(MAXIMAL_N9, (MAXIMAL_N12, MAXIMAL_N10)))
        self.assertTrue(is_contained_in_longer(REMAINDER_8PREFIX, (REMAINDER_9GRAM,)))
        self.assertTrue(is_contained_in_longer(REMAINDER_8SUFFIX, (REMAINDER_9GRAM,)))
        self.assertFalse(is_n13_substring(MAXIMAL_N12))
        self.assertFalse(is_n13_substring(MAXIMAL_N10))
        self.assertFalse(is_n13_substring(MAXIMAL_N9))
        self.assertEqual(STANDING_CLAIM, "c_independent_nge8_has_exactly_2_maximals")
        self.assertFalse(STANDING_C_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS)
        self.assertEqual(STANDING_N, 3)
        self.assertNotEqual(STANDING_N, HYPOTHESIS_N)
        self.assertEqual(provider.get_call_history(), [])

    def test_shared_core_sits_in_two_maximals(self):
        """Guy+single-040 core is a substring of both calendar tails, not one."""
        provider = MockProvider()
        maximals = independent_maximals(STANDING_INDEPENDENT)
        self.assertEqual(maximals, STANDING_MAXIMALS)
        self.assertTrue(is_contiguous_substring(STANDING_SHARED_CORE[0], MAXIMAL_N12))
        self.assertTrue(is_contiguous_substring(STANDING_SHARED_CORE[0], MAXIMAL_N10))
        self.assertTrue(is_contiguous_substring(STANDING_SHARED_CORE[1], MAXIMAL_N12))
        self.assertTrue(is_contiguous_substring(STANDING_SHARED_CORE[1], MAXIMAL_N10))
        self.assertEqual(containing_maximal_indexes(STANDING_SHARED_CORE[0], maximals), (0, 1))
        self.assertEqual(containing_maximal_indexes(STANDING_SHARED_CORE[1], maximals), (0, 1))
        self.assertFalse(
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


class TestMamariCIndependentNge8MaximalsScoreboard(unittest.TestCase):
    """Cited-fixture C independent n≥8 maximals. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.c_sides = load_c_sides()
        prior = TestMamariCNge8Scoreboard()
        prior.setUp()
        self.independent = prior.independent
        self.maximals = independent_maximals(self.independent)
        self.containing = membership_rows(self.independent, self.maximals)
        self.claim_holds = c_independent_nge8_has_exactly_2_maximals(self.maximals)

    def test_tokens_are_cycle_120_independent_not_invented(self):
        """Independent set is the cycle-120 lock, not a new inventory."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 11)
        prior = TestMamariCNge8Scoreboard()
        prior.setUp()
        self.assertEqual(prior.independent, STANDING_INDEPENDENT)
        self.assertEqual(independent_rows(prior.rows), STANDING_INDEPENDENT)
        self.assertEqual(MAXIMAL_N9, REMAINDER_9GRAM)
        self.assertEqual(MAXIMAL_N9, MOTIF_9GRAM)
        self.assertEqual(REMAINDER_8PREFIX, REMAINDER_9GRAM[:8])
        self.assertEqual(REMAINDER_8SUFFIX, REMAINDER_9GRAM[1:])
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in STANDING_INDEPENDENT)
        self.assertIn(MAXIMAL_N12, indep_tokens)
        self.assertIn(MAXIMAL_N10, indep_tokens)
        self.assertIn(MAXIMAL_N9, indep_tokens)
        self.assertNotIn(GRAM13, indep_tokens)
        self.assertFalse(is_contiguous_substring(MAXIMAL_N10, MAXIMAL_N12))
        self.assertFalse(is_contiguous_substring(MAXIMAL_N12, MAXIMAL_N10))
        self.assertFalse(is_contiguous_substring(MAXIMAL_N9, MAXIMAL_N12))
        self.assertFalse(is_contiguous_substring(MAXIMAL_N9, MAXIMAL_N10))
        self.assertEqual(self.survey["c_repeating_nge8"]["cycle"], 120)
        self.assertEqual(self.survey["c_repeating_nge8"]["independent_count"], 11)
        self.assertFalse(self.survey["c_repeating_nge8"]["c_repeating_nge8_all_substrings_of_n13"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n_is_3_and_hypothesis_n_2_loses(self):
        """11 independent grams collapse to 3 maximals. Claim is false."""
        self.assertEqual(len(self.maximals), STANDING_N)
        self.assertEqual(STANDING_N, 3)
        self.assertEqual(HYPOTHESIS_N, 2)
        self.assertNotEqual(STANDING_N, HYPOTHESIS_N)
        self.assertFalse(c_independent_nge8_has_exactly_2_maximals(self.maximals))
        self.assertEqual(self.claim_holds, STANDING_C_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS)
        self.assertFalse(STANDING_C_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS)
        self.assertEqual(STANDING_CLAIM, "c_independent_nge8_has_exactly_2_maximals")
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
        self.assertEqual(maximal_tokens, (MAXIMAL_N12, MAXIMAL_N10, MAXIMAL_N9))
        nonmaximals = tuple(
            row for row in STANDING_INDEPENDENT if row[0] not in set(maximal_tokens)
        )
        self.assertEqual(len(nonmaximals), STANDING_NONMAXIMAL_COUNT)
        two_count = 0
        one_count = 0
        for gram, _n, _freq, _sites in nonmaximals:
            indexes = containing_maximal_indexes(gram, self.maximals)
            self.assertGreaterEqual(len(indexes), 1)
            if len(indexes) == 1:
                one_count += 1
            elif len(indexes) == 2:
                two_count += 1
                self.assertIn(gram, STANDING_SHARED_CORE)
            else:
                self.fail(f"{gram} sits in {indexes}")
        self.assertEqual(one_count, STANDING_EXACTLY_ONE_NONMAXIMAL_COUNT)
        self.assertEqual(two_count, STANDING_TWO_MAXIMAL_NONMAXIMAL_COUNT)
        self.assertEqual(two_count, STANDING_SHARED_CORE_COUNT)
        self.assertTrue(every_independent_in_at_least_one_maximal(self.independent, self.maximals))
        self.assertFalse(every_nonmaximal_is_substring_of_exactly_one(self.independent, self.maximals))
        self.assertEqual(
            STANDING_EVERY_INDEPENDENT_IN_AT_LEAST_ONE,
            True,
        )
        self.assertFalse(STANDING_EVERY_NONMAXIMAL_EXACTLY_ONE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_maximal_sites_on_c(self):
        """Maximal C sites; Cb=0; each site matches the locked stems."""
        self.assertEqual(self.maximals, STANDING_MAXIMALS)
        for gram, n, freq, sites in self.maximals:
            self.assertEqual(nge8_sites(gram, self.c_sides), sites)
            self.assertEqual(ngram_hit_count(self.c_sides[SIDE_CA], gram), freq)
            self.assertEqual(ngram_hit_count(self.c_sides[SIDE_CB], gram), 0)
            for side, line, index in sites:
                names = CA_LINE_NAMES if side == SIDE_CA else CB_LINE_NAMES
                stems = self.c_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_CA)
                self.assertIn(line, ("Ca7", "Ca8", "Ca10", "Ca11"))
        self.assertEqual(STANDING_MAXIMALS[0][3], (("Ca", "Ca7", 3), ("Ca", "Ca8", 0)))
        self.assertEqual(STANDING_MAXIMALS[1][3], (("Ca", "Ca7", 33), ("Ca", "Ca8", 3)))
        self.assertEqual(STANDING_MAXIMALS[2][3], (("Ca", "Ca10", 26), ("Ca", "Ca11", 14)))
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_120_119_118_and_w_scoreboards_still_compute(self):
        """Cycle 120 n≥8, 119 C 13-grams, 118 C-only, and W stay."""
        prior_120 = TestMamariCNge8Scoreboard()
        prior_120.setUp()
        prior_120.test_counts_and_hypothesis_all_substrings_loses()
        prior_120.test_survey_matches_computed_lock()
        prior_119 = TestMamariCThirteengramScoreboard()
        prior_119.setUp()
        prior_119.test_n_is_1_and_hypothesis_n_1_holds()
        prior_119.test_survey_matches_computed_lock()
        prior_118 = TestMamariCaCOnlyScoreboard()
        prior_118.setUp()
        prior_118.test_13gram_is_zero_off_c_and_c_only()
        prior_118.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-121 independent maximal lock."""
        lock = self.survey["c_independent_nge8_maximals"]
        self.assertEqual(lock["cycle"], 121)
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
        self.assertFalse(lock["every_nonmaximal_exactly_one"])
        self.assertEqual(
            lock["every_nonmaximal_exactly_one"],
            STANDING_EVERY_NONMAXIMAL_EXACTLY_ONE,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["c_independent_nge8_has_exactly_2_maximals"])
        self.assertEqual(
            lock["c_independent_nge8_has_exactly_2_maximals"],
            STANDING_C_INDEPENDENT_NGE8_HAS_EXACTLY_2_MAXIMALS,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_c_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_c_repeating_13grams_unchanged"])
        self.assertTrue(lock["standing_c_mamari_ca_c_only_unchanged"])
        self.assertTrue(lock["standing_b_repeating_8grams_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["c_repeating_nge8"]["cycle"], 120)
        self.assertFalse(self.survey["c_repeating_nge8"]["c_repeating_nge8_all_substrings_of_n13"])
        self.assertEqual(self.survey["c_repeating_13grams"]["cycle"], 119)
        self.assertTrue(self.survey["c_repeating_13grams"]["c_has_exactly_1_repeating_13gram"])
        self.assertEqual(self.survey["tablet_c_mamari_ca_c_only"]["cycle"], 118)
        self.assertTrue(self.survey["tablet_c_mamari_ca_c_only"]["c_maxn_is_c_only"])
        self.assertEqual(self.survey["b_repeating_8grams"]["cycle"], 115)
        self.assertFalse(self.survey["b_repeating_8grams"]["b_has_exactly_2_repeating_8grams"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["longest_count"], 1)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCIndependentNge8MaximalsImageSnapshot(unittest.TestCase):
    """Cycle 121 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
