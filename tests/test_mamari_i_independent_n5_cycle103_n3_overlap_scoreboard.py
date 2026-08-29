"""I's cycle-136 independent n=5 maximals vs the cycle-103 I 5-gram.

Cycle 140 text-search lock. Uses already-vendored A–V and the
cycle-136 independent n=5 maximal set (4 independent 5-grams
that are not the cycle-103 I 5-gram family). Does not retune
the maximal set. Does not vendor a new tablet. Does not scrape
X. W has no Barthel (cycle 100); skip W. Does not redo H∩P∩Q
n≥8 or G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

For each independent n=5 maximal, every consecutive n≥3
substring it shares with 999 071 076 010 079 (empty is
allowed). Hypothesis: none of the 4 shares an n≥3 run.
Measured: 1 of 4 does — 076 010 079 006 700 shares
076 010 079 (n=3). The other three share none. Claim that
can lose: i_independent_n5_share_no_n3plus_with_cycle103_5gram.
The claim is false. Do not retune.

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
from tests.test_mamari_i_exception_n4_071_065_071_999_i_only_scoreboard import (
    TestMamariIExceptionN4071065071999IOnlyScoreboard,
)
from tests.test_mamari_i_independent_n5_076_scoreboard import (
    STANDING_N5,
    TestMamariIIndependentN5076Scoreboard,
    independent_n5_rows,
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
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    TestMamariILeftoverN4Maximals076Scoreboard,
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

HYPOTHESIS_SHARE_NO_N3PLUS = True
STANDING_INDEPENDENT_N5 = 4
STANDING_WITH_N3PLUS = 1
STANDING_WITHOUT_N3PLUS = 3
STANDING_SHARED_N3 = ("076", "010", "079")
STANDING_SHARED_BY_N5 = (
    (),
    (),
    (),
    (STANDING_SHARED_N3,),
)
STANDING_OVERLAP_TUPLES = (
    (MAXIMAL_N5_010, STANDING_SHARED_N3, 3),
)
STANDING_WITH_ROWS = (STANDING_N5[3],)
STANDING_WITHOUT_ROWS = STANDING_N5[:3]
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_independent_n5_share_no_n3plus_with_cycle103_5gram"
STANDING_I_INDEPENDENT_N5_SHARE_NO_N3PLUS_WITH_CYCLE103_5GRAM = False
STANDING_RESULT = "i_independent_n5_cycle103_n3_overlap"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
MIN_SHARED_N = 3


def consecutive_nge3(
    gram: tuple[str, ...],
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[str, ...], ...]:
    """Consecutive n≥3 substrings of gram, n then start index. Search only."""
    return tuple(
        gram[index : index + n]
        for n in range(min_n, len(gram) + 1)
        for index in range(len(gram) - n + 1)
    )


def shared_nge3_with_cycle103(
    gram: tuple[str, ...],
    cycle103: tuple[str, ...] = GRAM5,
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[str, ...], ...]:
    """Consecutive n≥3 substrings that sit in both gram and cycle-103."""
    locked = set(consecutive_nge3(cycle103, min_n))
    return tuple(run for run in consecutive_nge3(gram, min_n) if run in locked)


def overlap_tuples(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_N5,
    cycle103: tuple[str, ...] = GRAM5,
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[tuple[str, ...], tuple[str, ...], int], ...]:
    """(5-gram, shared n-gram, n) for every shared n≥3 run."""
    return tuple(
        (gram, shared, len(shared))
        for gram, _n, _freq, _sites in rows
        for shared in shared_nge3_with_cycle103(gram, cycle103, min_n)
    )


def n5_with_n3plus_overlap(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_N5,
    cycle103: tuple[str, ...] = GRAM5,
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Independent n=5 maximals that share an n≥3 run with cycle-103."""
    return tuple(
        row
        for row in rows
        if shared_nge3_with_cycle103(row[0], cycle103, min_n)
    )


def n5_without_n3plus_overlap(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_N5,
    cycle103: tuple[str, ...] = GRAM5,
    min_n: int = MIN_SHARED_N,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Independent n=5 maximals that share no n≥3 run with cycle-103."""
    return tuple(
        row
        for row in rows
        if not shared_nge3_with_cycle103(row[0], cycle103, min_n)
    )


def i_independent_n5_share_no_n3plus_with_cycle103_5gram(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    cycle103: tuple[str, ...] = GRAM5,
    min_n: int = MIN_SHARED_N,
) -> bool:
    """True iff every independent n=5 maximal shares no n≥3 with cycle-103.

    An empty n=5 set is false here (the cycle-136 independent n=5
    set must be present and every member must miss the overlap).
    """
    return bool(rows) and all(
        not shared_nge3_with_cycle103(gram, cycle103, min_n)
        for gram, _n, _freq, _sites in rows
    )


class TestIIndependentN5Cycle103N3OverlapHelpers(unittest.TestCase):
    """Helpers on cycle-136 n=5 tokens vs cycle-103. No CV, no LLM."""

    def test_shared_nge3_and_none_share_can_fail(self):
        """The four n=5 maximals lose; empty and a planted overlap lose."""
        provider = MockProvider()
        n5 = independent_n5_rows()
        self.assertEqual(n5, STANDING_N5)
        self.assertEqual(len(n5), STANDING_INDEPENDENT_N5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(consecutive_nge3(GRAM5), (
            ("999", "071", "076"),
            ("071", "076", "010"),
            ("076", "010", "079"),
            ("999", "071", "076", "010"),
            ("071", "076", "010", "079"),
            GRAM5,
        ))
        self.assertEqual(shared_nge3_with_cycle103(MAXIMAL_N5_430), ())
        self.assertEqual(shared_nge3_with_cycle103(MAXIMAL_N5_011), ())
        self.assertEqual(shared_nge3_with_cycle103(MAXIMAL_N5_400), ())
        self.assertEqual(
            shared_nge3_with_cycle103(MAXIMAL_N5_010),
            (STANDING_SHARED_N3,),
        )
        self.assertTrue(is_contiguous_substring(STANDING_SHARED_N3, MAXIMAL_N5_010))
        self.assertTrue(is_contiguous_substring(STANDING_SHARED_N3, GRAM5))
        self.assertFalse(is_contiguous_substring(STANDING_SHARED_N3, MAXIMAL_N5_430))
        self.assertFalse(i_independent_n5_share_no_n3plus_with_cycle103_5gram(()))
        with_overlap = n5_with_n3plus_overlap(n5)
        without_overlap = n5_without_n3plus_overlap(n5)
        self.assertEqual(len(with_overlap), STANDING_WITH_N3PLUS)
        self.assertEqual(len(without_overlap), STANDING_WITHOUT_N3PLUS)
        self.assertEqual(with_overlap, STANDING_WITH_ROWS)
        self.assertEqual(without_overlap, STANDING_WITHOUT_ROWS)
        self.assertFalse(
            i_independent_n5_share_no_n3plus_with_cycle103_5gram(with_overlap)
        )
        self.assertTrue(
            i_independent_n5_share_no_n3plus_with_cycle103_5gram(without_overlap)
        )
        self.assertFalse(i_independent_n5_share_no_n3plus_with_cycle103_5gram(n5))
        planted = (
            (MAXIMAL_N5_430, 5, 2, STANDING_N5[0][3]),
            (GRAM5, 5, 3, (("Ia", "Ia4", 6),)),
        )
        self.assertFalse(
            i_independent_n5_share_no_n3plus_with_cycle103_5gram(planted)
        )
        self.assertEqual(
            tuple(shared_nge3_with_cycle103(gram) for gram, _n, _f, _s in n5),
            STANDING_SHARED_BY_N5,
        )
        self.assertEqual(overlap_tuples(n5), STANDING_OVERLAP_TUPLES)
        self.assertEqual(STANDING_CLAIM, "i_independent_n5_share_no_n3plus_with_cycle103_5gram")
        self.assertFalse(STANDING_I_INDEPENDENT_N5_SHARE_NO_N3PLUS_WITH_CYCLE103_5GRAM)
        self.assertNotEqual(
            STANDING_I_INDEPENDENT_N5_SHARE_NO_N3PLUS_WITH_CYCLE103_5GRAM,
            HYPOTHESIS_SHARE_NO_N3PLUS,
        )
        self.assertEqual(
            STANDING_WITH_N3PLUS + STANDING_WITHOUT_N3PLUS,
            STANDING_INDEPENDENT_N5,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_n5s_are_cycle_136_maximals_not_i_5gram_family(self):
        """Cycle-136 n=5 maximals: 4 grams, none is the cycle-103 5-gram."""
        provider = MockProvider()
        n5 = independent_n5_rows()
        self.assertEqual(n5, STANDING_N5)
        maximal_n5 = tuple(row for row in STANDING_MAXIMALS if row[1] == 5)
        self.assertEqual(maximal_n5, STANDING_N5)
        self.assertEqual(len(maximal_n5), STANDING_INDEPENDENT_N5)
        tokens = tuple(gram for gram, _n, _f, _s in n5)
        self.assertEqual(
            tokens,
            (MAXIMAL_N5_430, MAXIMAL_N5_011, MAXIMAL_N5_400, MAXIMAL_N5_010),
        )
        self.assertEqual(set(tokens), set(STANDING_HYPOTHESIZED_N5))
        self.assertNotIn(GRAM5, tokens)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        leftover = leftover_n4_rows()
        leftover_tokens = {gram for gram, _n, _f, _s in leftover}
        for gram, n, _freq, _sites in n5:
            self.assertEqual(n, 5)
            self.assertEqual(len(gram), 5)
            self.assertNotIn(gram, leftover_tokens)
            self.assertNotEqual(gram, GRAM5)
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(GRAM5, gram))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIIndependentN5Cycle103N3OverlapScoreboard(unittest.TestCase):
    """Cited-fixture independent n=5 maximals vs cycle-103 n≥3. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.n5 = independent_n5_rows()
        self.with_overlap = n5_with_n3plus_overlap(self.n5)
        self.without_overlap = n5_without_n3plus_overlap(self.n5)
        self.overlaps = overlap_tuples(self.n5)
        self.claim_holds = i_independent_n5_share_no_n3plus_with_cycle103_5gram(
            self.n5
        )

    def test_tokens_are_cycle_136_n5_not_invented(self):
        """n=5 set is the cycle-136 lock, not a new inventory."""
        self.assertEqual(self.n5, STANDING_N5)
        self.assertEqual(independent_n5_rows(), STANDING_N5)
        self.assertEqual(len(STANDING_N5), STANDING_INDEPENDENT_N5)
        self.assertEqual(STANDING_INDEPENDENT_N5, 4)
        prior = TestMamariIIndependentNge4MaximalsScoreboard()
        prior.setUp()
        self.assertEqual(len(prior.maximals), STANDING_N)
        self.assertEqual(STANDING_N, 31)
        n5_tokens = {gram for gram, _n, _f, _s in STANDING_N5}
        maximal_n5 = {gram for gram, n, _f, _s in prior.maximals if n == 5}
        self.assertEqual(n5_tokens, maximal_n5)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 39)
        self.assertEqual(STANDING_LEFTOVER_N4_COUNT, 27)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["maximal_count"], 31)
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

    def test_counts_1_of_4_and_hypothesis_none_share_loses(self):
        """1 independent 5-gram shares n≥3; 3 do not. Claim is false."""
        self.assertEqual(len(self.n5), STANDING_INDEPENDENT_N5)
        self.assertEqual(len(self.with_overlap), STANDING_WITH_N3PLUS)
        self.assertEqual(len(self.without_overlap), STANDING_WITHOUT_N3PLUS)
        self.assertEqual(STANDING_WITH_N3PLUS, 1)
        self.assertEqual(STANDING_WITHOUT_N3PLUS, 3)
        self.assertEqual(
            STANDING_INDEPENDENT_N5,
            STANDING_WITH_N3PLUS + STANDING_WITHOUT_N3PLUS,
        )
        self.assertTrue(HYPOTHESIS_SHARE_NO_N3PLUS)
        self.assertFalse(
            i_independent_n5_share_no_n3plus_with_cycle103_5gram(self.n5)
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_INDEPENDENT_N5_SHARE_NO_N3PLUS_WITH_CYCLE103_5GRAM,
        )
        self.assertFalse(STANDING_I_INDEPENDENT_N5_SHARE_NO_N3PLUS_WITH_CYCLE103_5GRAM)
        self.assertEqual(
            STANDING_CLAIM,
            "i_independent_n5_share_no_n3plus_with_cycle103_5gram",
        )
        self.assertEqual(
            tuple(shared_nge3_with_cycle103(gram) for gram, _n, _f, _s in self.n5),
            STANDING_SHARED_BY_N5,
        )
        self.assertEqual(self.overlaps, STANDING_OVERLAP_TUPLES)
        self.assertEqual(len(self.overlaps), STANDING_WITH_N3PLUS)
        self.assertEqual(
            sum(1 for shared in STANDING_SHARED_BY_N5 if shared),
            STANDING_WITH_N3PLUS,
        )
        self.assertEqual(
            sum(1 for shared in STANDING_SHARED_BY_N5 if not shared),
            STANDING_WITHOUT_N3PLUS,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_5gram_overlaps_only_076_010_079(self):
        """Only 076 010 079 006 700 shares 076 010 079; the other three are empty."""
        self.assertEqual(self.with_overlap, STANDING_WITH_ROWS)
        self.assertEqual(self.without_overlap, STANDING_WITHOUT_ROWS)
        self.assertEqual(self.overlaps, STANDING_OVERLAP_TUPLES)
        self.assertEqual(STANDING_OVERLAP_TUPLES, (
            (MAXIMAL_N5_010, ("076", "010", "079"), 3),
        ))
        self.assertEqual(shared_nge3_with_cycle103(MAXIMAL_N5_430), ())
        self.assertEqual(shared_nge3_with_cycle103(MAXIMAL_N5_011), ())
        self.assertEqual(shared_nge3_with_cycle103(MAXIMAL_N5_400), ())
        self.assertEqual(
            shared_nge3_with_cycle103(MAXIMAL_N5_010),
            (("076", "010", "079"),),
        )
        for gram, n, freq, _sites in self.without_overlap:
            self.assertEqual(n, 5)
            self.assertEqual(freq, 2)
            self.assertEqual(shared_nge3_with_cycle103(gram), ())
            self.assertNotEqual(gram, GRAM5)
        for gram, n, freq, _sites in self.with_overlap:
            self.assertEqual(n, 5)
            self.assertEqual(freq, 2)
            self.assertEqual(gram, MAXIMAL_N5_010)
            self.assertNotEqual(gram, GRAM5)
            self.assertEqual(shared_nge3_with_cycle103(gram), (STANDING_SHARED_N3,))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n5_sites_on_i(self):
        """Independent n=5 I sites; Ib unpublished; each site matches the stems."""
        self.assertEqual(self.n5, STANDING_N5)
        for gram, n, freq, sites in self.n5:
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_139_138_137_136_103_and_w_scoreboards_still_compute(self):
        """Cycle 139 076, 138 I-only, 137 leftover 076, 136 maximals, 103 I-only, W stay."""
        prior_139 = TestMamariIIndependentN5076Scoreboard()
        prior_139.setUp()
        prior_139.test_counts_4_of_4_and_hypothesis_all_contain_holds()
        prior_139.test_survey_matches_computed_lock()
        prior_138 = TestMamariIExceptionN4071065071999IOnlyScoreboard()
        prior_138.setUp()
        prior_138.test_survey_matches_computed_lock()
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-140 n≥3 overlap lock."""
        lock = self.survey["i_independent_n5_cycle103_n3_overlap"]
        self.assertEqual(lock["cycle"], 140)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_no_n3plus"])
        self.assertEqual(lock["hypothesis_share_no_n3plus"], HYPOTHESIS_SHARE_NO_N3PLUS)
        self.assertEqual(lock["independent_n5_count"], STANDING_INDEPENDENT_N5)
        self.assertEqual(lock["N_independent_5grams"], STANDING_INDEPENDENT_N5)
        self.assertEqual(lock["with_n3plus_overlap_count"], STANDING_WITH_N3PLUS)
        self.assertEqual(lock["N_with_n3plus_overlap"], STANDING_WITH_N3PLUS)
        self.assertEqual(lock["without_n3plus_overlap_count"], STANDING_WITHOUT_N3PLUS)
        self.assertEqual(lock["N_without_n3plus_overlap"], STANDING_WITHOUT_N3PLUS)
        self.assertEqual(tuple(lock["cycle103_tokens5"]), GRAM5)
        measured_n5 = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
                "shared_nge3": [list(shared) for shared in shared_nge3_with_cycle103(tokens)],
            }
            for tokens, n, freq, sites in STANDING_N5
        ]
        self.assertEqual(lock["n5_maximals"], measured_n5)
        measured_overlaps = [
            {
                "tokens5": list(gram),
                "shared": list(shared),
                "n": n,
            }
            for gram, shared, n in STANDING_OVERLAP_TUPLES
        ]
        self.assertEqual(lock["overlaps"], measured_overlaps)
        measured_tuples = [
            [list(gram), list(shared), n]
            for gram, shared, n in STANDING_OVERLAP_TUPLES
        ]
        self.assertEqual(lock["overlap_tuples"], measured_tuples)
        self.assertEqual(
            tuple(tuple(tuple(run) for run in row) for row in lock["shared_by_n5"]),
            STANDING_SHARED_BY_N5,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_independent_n5_share_no_n3plus_with_cycle103_5gram"])
        self.assertEqual(
            lock["i_independent_n5_share_no_n3plus_with_cycle103_5gram"],
            STANDING_I_INDEPENDENT_N5_SHARE_NO_N3PLUS_WITH_CYCLE103_5GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_independent_n5_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_exception_n4_071_065_071_999_i_only_unchanged"])
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
        self.assertEqual(self.survey["i_independent_n5_maximals_076"]["cycle"], 139)
        self.assertTrue(
            self.survey["i_independent_n5_maximals_076"][
                "i_independent_n5_maximals_all_contain_076"
            ]
        )
        self.assertEqual(self.survey["i_exception_n4_071_065_071_999_i_only"]["cycle"], 138)
        self.assertTrue(
            self.survey["i_exception_n4_071_065_071_999_i_only"][
                "i_exception_n4_071_065_071_999_is_i_only"
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


class TestMamariIIndependentN5Cycle103N3OverlapImageSnapshot(unittest.TestCase):
    """Cycle 140 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
