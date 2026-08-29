"""I's cycle-136 leftover n=4 maximals vs independent n=5 n≥3 overlap.

Cycle 159 text-search lock. Uses already-vendored A–V and the
cycle-136 leftover n=4 maximal set (27 independent n=4 grams
that are not substrings of the four I 5-grams) plus the four
independent I n=5 maximals (cycles 136/139). Does not retune
either set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Does not redo H∩P∩Q
n≥8 or G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

For each leftover n=4 maximal, whether it shares any consecutive
n≥3 token substring with at least one independent n=5 maximal
(n=2 does not count). Hypothesis N=5: exactly 5 of 27 do.
Measured: 5 of 27 share an n=3 run — 072 076 010 079 and
076 010 079 090 vs 076 010 079 006 700 (overlap 076 010 079);
053 076 020 010, 090 076 020 010, and 076 020 010 050 vs
400 070 076 020 010 (overlap 076 020 010). The other 22 share
none. Cycle 140 locked 1 of 4 independent 5-grams vs cycle-103;
this cycle is leftover n=4 vs the independent 5-grams, not vs
cycle-103. Cycle 158 leftover prefixes stay I-only hapax.
Claim that can lose:
i_leftover_n4_exactly_5_share_n3plus_with_independent_n5.
True only if N_with_n3plus_overlap=5. The claim is true.
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
from tests.test_mamari_i_independent_n5_076_scoreboard import (
    STANDING_N5,
    TestMamariIIndependentN5076Scoreboard,
    independent_n5_rows,
)
from tests.test_mamari_i_independent_n5_cycle103_n3_overlap_scoreboard import (
    TestMamariIIndependentN5Cycle103N3OverlapScoreboard,
    consecutive_nge3,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
    MAXIMAL_N5_011,
    MAXIMAL_N5_400,
    MAXIMAL_N5_430,
    STANDING_HYPOTHESIZED_N5,
    STANDING_LEFTOVER_N4_COUNT,
    STANDING_MAXIMALS,
    STANDING_N,
    TestMamariIIndependentNge4MaximalsScoreboard,
    leftover_n4_rows,
)
from tests.test_mamari_i_leftover_023_077_400_070_076_i_only_scoreboard import (
    TestMamariILeftover023077400070076IOnlyScoreboard,
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

HYPOTHESIS_N = 5
STANDING_LEFTOVER_N4 = 27
STANDING_INDEPENDENT_N5 = 4
STANDING_WITH_N3PLUS = 5
STANDING_WITHOUT_N3PLUS = 22
STANDING_SHARED_076_010_079 = ("076", "010", "079")
STANDING_SHARED_076_020_010 = ("076", "020", "010")
STANDING_OVERLAP_TUPLES = (
    (("090", "076", "020", "010"), MAXIMAL_N5_400, STANDING_SHARED_076_020_010, 3),
    (("076", "020", "010", "050"), MAXIMAL_N5_400, STANDING_SHARED_076_020_010, 3),
    (("076", "010", "079", "090"), MAXIMAL_N5_010, STANDING_SHARED_076_010_079, 3),
    (("072", "076", "010", "079"), MAXIMAL_N5_010, STANDING_SHARED_076_010_079, 3),
    (("053", "076", "020", "010"), MAXIMAL_N5_400, STANDING_SHARED_076_020_010, 3),
)
STANDING_OVERLAPPING_LEFTOVERS = tuple(gram for gram, _five, _run, _n in STANDING_OVERLAP_TUPLES)
STANDING_WITH_ROWS = tuple(
    row for row in STANDING_LEFTOVER if row[0] in STANDING_OVERLAPPING_LEFTOVERS
)
STANDING_WITHOUT_ROWS = tuple(
    row for row in STANDING_LEFTOVER if row[0] not in STANDING_OVERLAPPING_LEFTOVERS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"
STANDING_I_LEFTOVER_N4_EXACTLY_5_SHARE_N3PLUS_WITH_INDEPENDENT_N5 = True
STANDING_RESULT = "i_leftover_n4_independent_n5_n3_overlap"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_VS_CYCLE103 = False
MIN_SHARED_N = 3


def leftover_n4_overlaps_with_n5(
    leftover: tuple[str, ...],
    n5s: tuple[tuple[str, ...], ...] = STANDING_HYPOTHESIZED_N5,
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[tuple[str, ...], tuple[str, ...], int], ...]:
    """(independent 5-gram, shared n-gram, n) for leftover n≥3 runs."""
    leftover_runs = set(consecutive_nge3(leftover, min_n))
    return tuple(
        (five, run, len(run))
        for five in n5s
        for run in consecutive_nge3(five, min_n)
        if run in leftover_runs
    )


def overlap_tuples(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    n5s: tuple[tuple[str, ...], ...] = STANDING_HYPOTHESIZED_N5,
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], int], ...]:
    """(leftover, independent 5-gram, overlap tokens, n) for every n≥3 hit."""
    return tuple(
        (gram, five, shared, n)
        for gram, _n, _freq, _sites in leftovers
        for five, shared, n in leftover_n4_overlaps_with_n5(gram, n5s, min_n)
    )


def leftover_with_n3plus_overlap(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    n5s: tuple[tuple[str, ...], ...] = STANDING_HYPOTHESIZED_N5,
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that share an n≥3 run with an independent 5-gram."""
    return tuple(
        row
        for row in leftovers
        if leftover_n4_overlaps_with_n5(row[0], n5s, min_n)
    )


def leftover_without_n3plus_overlap(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    n5s: tuple[tuple[str, ...], ...] = STANDING_HYPOTHESIZED_N5,
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that share no n≥3 run with any independent 5-gram."""
    return tuple(
        row
        for row in leftovers
        if not leftover_n4_overlaps_with_n5(row[0], n5s, min_n)
    )


def i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    n5s: tuple[tuple[str, ...], ...] = STANDING_HYPOTHESIZED_N5,
    min_n: int = MIN_SHARED_N,
    expected: int = HYPOTHESIS_N,
) -> bool:
    """True iff exactly expected leftovers share an n≥3 run with the n=5 set."""
    return len(leftover_with_n3plus_overlap(leftovers, n5s, min_n)) == expected


class TestILeftoverN4IndependentN5N3OverlapHelpers(unittest.TestCase):
    """Helpers on cycle-136 leftover n=4 vs independent n=5. No CV, no LLM."""

    def test_shared_nge3_and_exactly_5_can_fail(self):
        """The 27 leftovers hold at 5; empty, 0, and a planted sixth lose."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        n5 = independent_n5_rows()
        n5_tokens = tuple(gram for gram, _n, _f, _s in n5)
        self.assertEqual(leftover, STANDING_LEFTOVER)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N4)
        self.assertEqual(n5, STANDING_N5)
        self.assertEqual(len(n5), STANDING_INDEPENDENT_N5)
        self.assertEqual(
            leftover_n4_overlaps_with_n5(("090", "076", "020", "010"), n5_tokens),
            ((MAXIMAL_N5_400, STANDING_SHARED_076_020_010, 3),),
        )
        self.assertEqual(
            leftover_n4_overlaps_with_n5(("076", "020", "010", "050"), n5_tokens),
            ((MAXIMAL_N5_400, STANDING_SHARED_076_020_010, 3),),
        )
        self.assertEqual(
            leftover_n4_overlaps_with_n5(("053", "076", "020", "010"), n5_tokens),
            ((MAXIMAL_N5_400, STANDING_SHARED_076_020_010, 3),),
        )
        self.assertEqual(
            leftover_n4_overlaps_with_n5(("076", "010", "079", "090"), n5_tokens),
            ((MAXIMAL_N5_010, STANDING_SHARED_076_010_079, 3),),
        )
        self.assertEqual(
            leftover_n4_overlaps_with_n5(("072", "076", "010", "079"), n5_tokens),
            ((MAXIMAL_N5_010, STANDING_SHARED_076_010_079, 3),),
        )
        self.assertEqual(leftover_n4_overlaps_with_n5(("430", "076", "001", "076"), n5_tokens), ())
        self.assertEqual(leftover_n4_overlaps_with_n5(("028", "076", "011", "076"), n5_tokens), ())
        self.assertEqual(leftover_n4_overlaps_with_n5(("202", "076", "006", "055"), n5_tokens), ())
        self.assertEqual(leftover_n4_overlaps_with_n5(("600", "090", "076", "011"), n5_tokens), ())
        self.assertTrue(is_contiguous_substring(STANDING_SHARED_076_020_010, MAXIMAL_N5_400))
        self.assertTrue(is_contiguous_substring(STANDING_SHARED_076_010_079, MAXIMAL_N5_010))
        self.assertFalse(is_contiguous_substring(("430", "076", "001", "076"), MAXIMAL_N5_430))
        self.assertFalse(is_contiguous_substring(("090", "076", "020", "010"), MAXIMAL_N5_400))
        self.assertFalse(i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(()))
        with_overlap = leftover_with_n3plus_overlap(leftover, n5_tokens)
        without_overlap = leftover_without_n3plus_overlap(leftover, n5_tokens)
        self.assertEqual(len(with_overlap), STANDING_WITH_N3PLUS)
        self.assertEqual(len(without_overlap), STANDING_WITHOUT_N3PLUS)
        self.assertEqual(with_overlap, STANDING_WITH_ROWS)
        self.assertEqual(without_overlap, STANDING_WITHOUT_ROWS)
        self.assertTrue(i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(leftover))
        self.assertTrue(i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(with_overlap))
        self.assertFalse(i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(without_overlap))
        self.assertFalse(i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(with_overlap[:4]))
        planted = with_overlap + (
            (("430", "076", "006", "000"), 4, 1, (("Ia", "Ia1", 129),)),
        )
        self.assertFalse(i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(planted))
        self.assertEqual(overlap_tuples(leftover, n5_tokens), STANDING_OVERLAP_TUPLES)
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5")
        self.assertTrue(STANDING_I_LEFTOVER_N4_EXACTLY_5_SHARE_N3PLUS_WITH_INDEPENDENT_N5)
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_EXACTLY_5_SHARE_N3PLUS_WITH_INDEPENDENT_N5,
            HYPOTHESIS_N == STANDING_WITH_N3PLUS,
        )
        self.assertEqual(
            STANDING_WITH_N3PLUS + STANDING_WITHOUT_N3PLUS,
            STANDING_LEFTOVER_N4,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftovers_are_cycle_136_n4_not_5gram_substrings(self):
        """Cycle-136 leftover set: 27 n=4 maximals outside the four 5-grams."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        n5 = independent_n5_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        maximal_n4 = tuple(row for row in STANDING_MAXIMALS if row[1] == 4)
        self.assertEqual(len(maximal_n4), STANDING_LEFTOVER_N4)
        self.assertEqual(
            {gram for gram, _n, _f, _s in leftover},
            {gram for gram, _n, _f, _s in maximal_n4},
        )
        tokens5 = tuple(gram for gram, _n, _f, _s in n5)
        self.assertEqual(
            tokens5,
            (MAXIMAL_N5_430, MAXIMAL_N5_011, MAXIMAL_N5_400, MAXIMAL_N5_010),
        )
        self.assertEqual(set(tokens5), set(STANDING_HYPOTHESIZED_N5))
        self.assertNotIn(GRAM5, tokens5)
        for gram, n, _freq, _sites in leftover:
            self.assertEqual(n, 4)
            self.assertEqual(len(gram), 4)
            for five in STANDING_HYPOTHESIZED_N5:
                self.assertFalse(is_contiguous_substring(gram, five))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
        self.assertFalse(STANDING_VS_CYCLE103)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4IndependentN5N3OverlapScoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 vs independent n=5 n≥3. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.n5 = independent_n5_rows()
        self.n5_tokens = tuple(gram for gram, _n, _f, _s in self.n5)
        self.with_overlap = leftover_with_n3plus_overlap(self.leftover, self.n5_tokens)
        self.without_overlap = leftover_without_n3plus_overlap(self.leftover, self.n5_tokens)
        self.overlaps = overlap_tuples(self.leftover, self.n5_tokens)
        self.claim_holds = i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(
            self.leftover, self.n5_tokens
        )

    def test_tokens_are_cycle_136_leftover_and_n5_not_invented(self):
        """Leftover 27 and independent 4 are the cycle-136 lock, not a new inventory."""
        self.assertEqual(self.leftover, STANDING_LEFTOVER)
        self.assertEqual(leftover_n4_rows(), STANDING_LEFTOVER)
        self.assertEqual(len(STANDING_LEFTOVER), STANDING_LEFTOVER_N4)
        self.assertEqual(STANDING_LEFTOVER_N4, 27)
        self.assertEqual(STANDING_LEFTOVER_N4_COUNT, 27)
        self.assertEqual(self.n5, STANDING_N5)
        self.assertEqual(len(STANDING_N5), STANDING_INDEPENDENT_N5)
        self.assertEqual(STANDING_INDEPENDENT_N5, 4)
        prior = TestMamariIIndependentNge4MaximalsScoreboard()
        prior.setUp()
        self.assertEqual(len(prior.maximals), STANDING_N)
        self.assertEqual(STANDING_N, 31)
        leftover_tokens = {gram for gram, _n, _f, _s in STANDING_LEFTOVER}
        maximal_n4 = {gram for gram, n, _f, _s in prior.maximals if n == 4}
        self.assertEqual(leftover_tokens, maximal_n4)
        n5_tokens = {gram for gram, _n, _f, _s in STANDING_N5}
        maximal_n5 = {gram for gram, n, _f, _s in prior.maximals if n == 5}
        self.assertEqual(n5_tokens, maximal_n5)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 39)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(
            self.survey["i_independent_nge4_maximals"]["i_independent_nge4_has_exactly_4_maximals"]
        )
        hypothesized = tuple(
            tuple(row) for row in self.survey["i_independent_nge4_maximals"]["hypothesized_tokens5"]
        )
        self.assertEqual(set(hypothesized), set(STANDING_HYPOTHESIZED_N5))
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertEqual(self.survey["i_repeating_nge4"]["independent_count"], 39)
        self.assertNotIn(GRAM5, n5_tokens)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_5_of_27_and_hypothesis_n_5_holds(self):
        """5 leftovers share n≥3; 22 do not. Claim is true."""
        self.assertEqual(len(self.leftover), STANDING_LEFTOVER_N4)
        self.assertEqual(len(self.with_overlap), STANDING_WITH_N3PLUS)
        self.assertEqual(len(self.without_overlap), STANDING_WITHOUT_N3PLUS)
        self.assertEqual(STANDING_WITH_N3PLUS, 5)
        self.assertEqual(STANDING_WITHOUT_N3PLUS, 22)
        self.assertEqual(
            STANDING_LEFTOVER_N4,
            STANDING_WITH_N3PLUS + STANDING_WITHOUT_N3PLUS,
        )
        self.assertEqual(HYPOTHESIS_N, 5)
        self.assertTrue(
            i_leftover_n4_exactly_5_share_n3plus_with_independent_n5(self.leftover)
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_EXACTLY_5_SHARE_N3PLUS_WITH_INDEPENDENT_N5,
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_EXACTLY_5_SHARE_N3PLUS_WITH_INDEPENDENT_N5)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5",
        )
        self.assertEqual(self.overlaps, STANDING_OVERLAP_TUPLES)
        self.assertEqual(len(self.overlaps), STANDING_WITH_N3PLUS)
        self.assertEqual(
            tuple(gram for gram, _five, _run, _n in self.overlaps),
            STANDING_OVERLAPPING_LEFTOVERS,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_leftover_overlaps_only_the_expected_five(self):
        """Five leftovers share n=3; n=2 pairs and the other 22 are empty."""
        self.assertEqual(self.with_overlap, STANDING_WITH_ROWS)
        self.assertEqual(self.without_overlap, STANDING_WITHOUT_ROWS)
        self.assertEqual(self.overlaps, STANDING_OVERLAP_TUPLES)
        self.assertEqual(
            STANDING_OVERLAPPING_LEFTOVERS,
            (
                ("090", "076", "020", "010"),
                ("076", "020", "010", "050"),
                ("076", "010", "079", "090"),
                ("072", "076", "010", "079"),
                ("053", "076", "020", "010"),
            ),
        )
        self.assertNotIn(MAXIMAL_N5_430[:4], {gram for gram, _n, _f, _s in self.leftover})
        self.assertTrue(leftover_n4_overlaps_with_n5(MAXIMAL_N5_430[:4]))
        for gram, n, freq, _sites in self.without_overlap:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertEqual(leftover_n4_overlaps_with_n5(gram), ())
            self.assertNotIn(gram, STANDING_OVERLAPPING_LEFTOVERS)
        for leftover, five, shared, n in self.overlaps:
            self.assertEqual(n, 3)
            self.assertEqual(len(shared), 3)
            self.assertTrue(is_contiguous_substring(shared, leftover))
            self.assertTrue(is_contiguous_substring(shared, five))
            self.assertFalse(is_contiguous_substring(leftover, five))
            self.assertIn(five, (MAXIMAL_N5_400, MAXIMAL_N5_010))
            self.assertNotIn(five, (MAXIMAL_N5_430, MAXIMAL_N5_011))
        self.assertEqual(leftover_n4_overlaps_with_n5(("430", "076", "001", "076")), ())
        self.assertTrue(is_contiguous_substring(("430", "076"), MAXIMAL_N5_430))
        self.assertTrue(is_contiguous_substring(("076", "006"), MAXIMAL_N5_430))
        self.assertTrue(is_contiguous_substring(("076", "011"), MAXIMAL_N5_011))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_and_n5_sites_on_i(self):
        """Leftover and independent n=5 I sites; Ib unpublished; stems match."""
        self.assertEqual(self.leftover, STANDING_LEFTOVER)
        self.assertEqual(self.n5, STANDING_N5)
        for gram, n, freq, sites in self.leftover + self.n5:
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), freq)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
        self.assertEqual(
            STANDING_N5[0][3],
            (("Ia", "Ia1", 129), ("Ia", "Ia14", 162)),
        )
        self.assertEqual(
            STANDING_N5[1][3],
            (("Ia", "Ia12", 39), ("Ia", "Ia14", 102)),
        )
        self.assertEqual(
            STANDING_N5[2][3],
            (("Ia", "Ia13", 85), ("Ia", "Ia14", 126)),
        )
        self.assertEqual(
            STANDING_N5[3][3],
            (("Ia", "Ia6", 19), ("Ia", "Ia13", 72)),
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_VS_CYCLE103)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_158_140_137_136_103_and_w_scoreboards_still_compute(self):
        """Cycle 158 I-only, 140 cycle-103 n≥3, 137 leftover 076, 136 maximals, 103, W stay."""
        prior_158 = TestMamariILeftover023077400070076IOnlyScoreboard()
        prior_158.setUp()
        prior_158.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_158.test_survey_matches_computed_lock()
        prior_140 = TestMamariIIndependentN5Cycle103N3OverlapScoreboard()
        prior_140.setUp()
        prior_140.test_counts_1_of_4_and_hypothesis_none_share_loses()
        prior_140.test_survey_matches_computed_lock()
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
        prior_139 = TestMamariIIndependentN5076Scoreboard()
        prior_139.setUp()
        prior_139.test_counts_4_of_4_and_hypothesis_all_contain_holds()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-159 leftover n=4 vs n=5 n≥3 lock."""
        lock = self.survey["i_leftover_n4_independent_n5_n3_overlap"]
        self.assertEqual(lock["cycle"], 159)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["hypothesis_n"], 5)
        self.assertEqual(lock["leftover_n4_count"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], 27)
        self.assertEqual(lock["independent_n5_count"], STANDING_INDEPENDENT_N5)
        self.assertEqual(lock["N_independent_n5"], STANDING_INDEPENDENT_N5)
        self.assertEqual(lock["with_n3plus_overlap_count"], STANDING_WITH_N3PLUS)
        self.assertEqual(lock["N_with_n3plus_overlap"], STANDING_WITH_N3PLUS)
        self.assertEqual(lock["N_with_n3plus_overlap"], 5)
        self.assertEqual(lock["without_n3plus_overlap_count"], STANDING_WITHOUT_N3PLUS)
        self.assertEqual(lock["N_without_n3plus_overlap"], STANDING_WITHOUT_N3PLUS)
        self.assertEqual(lock["N_without_n3plus_overlap"], 22)
        measured_n5 = [list(gram) for gram, _n, _f, _s in STANDING_N5]
        self.assertEqual(lock["independent_n5"], measured_n5)
        measured_overlapping = [list(gram) for gram in STANDING_OVERLAPPING_LEFTOVERS]
        self.assertEqual(lock["overlapping_leftovers"], measured_overlapping)
        measured_tuples = [
            [list(leftover), list(five), list(shared), n]
            for leftover, five, shared, n in STANDING_OVERLAP_TUPLES
        ]
        self.assertEqual(lock["overlap_tuples"], measured_tuples)
        measured_overlaps = [
            {
                "leftover": list(leftover),
                "independent_n5": list(five),
                "overlap": list(shared),
                "n": n,
            }
            for leftover, five, shared, n in STANDING_OVERLAP_TUPLES
        ]
        self.assertEqual(lock["overlaps"], measured_overlaps)
        measured_leftovers = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
                "has_n3plus_overlap": bool(leftover_n4_overlaps_with_n5(tokens)),
                "overlaps": [
                    {
                        "independent_n5": list(five),
                        "overlap": list(shared),
                        "n": shared_n,
                    }
                    for five, shared, shared_n in leftover_n4_overlaps_with_n5(tokens)
                ],
            }
            for tokens, n, freq, sites in STANDING_LEFTOVER
        ]
        self.assertEqual(lock["leftovers"], measured_leftovers)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"])
        self.assertEqual(
            lock["i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"],
            STANDING_I_LEFTOVER_N4_EXACTLY_5_SHARE_N3PLUS_WITH_INDEPENDENT_N5,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["vs_cycle103"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_023_077_400_070_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_cycle103_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_maximals_076_unchanged"])
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
        self.assertEqual(self.survey["i_leftover_023_077_400_070_076_i_only"]["cycle"], 158)
        self.assertTrue(
            self.survey["i_leftover_023_077_400_070_076_i_only"][
                "i_leftover_023_077_400_070_076_both_i_only"
            ]
        )
        self.assertEqual(self.survey["i_independent_n5_cycle103_n3_overlap"]["cycle"], 140)
        self.assertFalse(
            self.survey["i_independent_n5_cycle103_n3_overlap"][
                "i_independent_n5_share_no_n3plus_with_cycle103_5gram"
            ]
        )
        self.assertEqual(
            self.survey["i_independent_n5_cycle103_n3_overlap"]["N_with_n3plus_overlap"],
            1,
        )
        self.assertEqual(self.survey["i_independent_n5_maximals_076"]["cycle"], 139)
        self.assertTrue(
            self.survey["i_independent_n5_maximals_076"][
                "i_independent_n5_maximals_all_contain_076"
            ]
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


class TestMamariILeftoverN4IndependentN5N3OverlapImageSnapshot(unittest.TestCase):
    """Cycle 159 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
