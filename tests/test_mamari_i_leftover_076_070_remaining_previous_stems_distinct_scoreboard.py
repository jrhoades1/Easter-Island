"""I's cycle-210 leftover remaining previous-stem distinct lock.

Cycle 214 text-search lock. Uses already-vendored A–V and the
cycle-210 leftover I sites of 2-gram 076 070 (the I sites that
are not 090-prefixed 090 076 070). Does not retune that 2-gram,
those leftover sites, the cycle-211 leftover-3 previous 720
cluster, or the leftover n=4 set. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

For each leftover I site, record the previous token immediately
before 076 070 when it exists (backward 3-gram X 076 070, and
previous 4-gram V X 076 070 when it exists). Start-of-line is
no-backward. Partition leftover sites into the already-locked
cycle-211 previous-720 cluster vs remaining. Remaining =
leftover I 076 070 sites whose previous stem is not 720.
Cycle 213 previous 4-grams of 720 076 070 I-only hapax 1/0 x3,
cycle 212 720 076 070 I-only 3/0, cycle 211 leftover N_share=3
/ N_leftover=11, cycle 210 leftover N_distinct=9, cycle 206
076 070 19/5 loss, and cycle 171 076 071 I-only 43/0 stay.
The 8 I 090 076 070 sites do not count as leftover. Off-I
076 070 sites do not count as leftover I. 076 071 is a
different 2-gram. Cycle 203 leftover 076 071 remaining
previous stems all distinct is a different 2-gram.

Claim that can lose:
i_leftover_076_070_remaining_previous_stems_distinct. True
only if N_distinct_remaining = N_remaining and N_remaining>=2.
Do not assume N_remaining=8; measure. Measured: N_leftover=11,
N_share_720=3, N_remaining=8, N_distinct_remaining=8,
N_no_backward=0. Remaining previous stems (each n=1): 571,
295, 048, 205, 099, 029, 604, 606. The claim is true. Same
claim-shape as cycle 203 (leftover 076 071 remaining previous
stems all distinct, N_remaining=24). Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_076_070_i_only_scoreboard import (
    GRAM2 as CYCLE206_GRAM2,
    STANDING_I_SITES as CYCLE206_I_SITES,
    STANDING_N_I as CYCLE206_N_I,
    STANDING_N_OFF_I as CYCLE206_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE206_OFF_I_SITES,
    TestMamariI2gram076070IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_I_SITES as CYCLE171_I_SITES,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    leftover_local_4grams,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_720_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE212_GRAM3,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE212_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE212_I_SITES,
    STANDING_N_I as CYCLE212_N_I,
    STANDING_N_OFF_I as CYCLE212_N_OFF_I,
    TestMamariI3gram720076070IOnlyScoreboard,
)
from tests.test_mamari_i_720_076_070_previous_4grams_i_only_scoreboard import (
    STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY as CYCLE213_I_ONLY,
    STANDING_N_I_053 as CYCLE213_N_I_053,
    STANDING_N_I_069 as CYCLE213_N_I_069,
    STANDING_N_I_999 as CYCLE213_N_I_999,
    STANDING_N_OFF_I_053 as CYCLE213_N_OFF_I_053,
    STANDING_N_OFF_I_069 as CYCLE213_N_OFF_I_069,
    STANDING_N_OFF_I_999 as CYCLE213_N_OFF_I_999,
    STANDING_SEQUENCES as CYCLE213_SEQUENCES,
    TestMamariI720076070Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_720_scoreboard import (
    GRAM3_BACKWARD,
    STEM_720,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE211_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE211_MATCHING_SITES,
    STANDING_N_LEFTOVER as CYCLE211_N_LEFTOVER,
    STANDING_N_SHARE as CYCLE211_N_SHARE,
    STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
    STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
    STANDING_WITHOUT_SITES as CYCLE211_WITHOUT_SITES,
    leftover_with_previous_720_076_070,
    leftover_without_previous_720_076_070,
    matching_leftover_local_4gram_rows,
    TestMamariILeftover076070Previous720Scoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_stem_scoreboard import (
    GRAM2,
    PREFIXED_STEM,
    STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM as CYCLE210_SHARE_ONE,
    STANDING_LEFTOVER_SITES,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE210_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE210_N_LEFTOVER,
    STANDING_N_NO_BACKWARD as CYCLE210_N_NO_BACKWARD,
    STANDING_N_090_PREFIXED as CYCLE210_N_090_PREFIXED,
    STANDING_PER_SITE_PREVIOUS_4GRAMS as CYCLE210_PREVIOUS_4GRAMS,
    STANDING_PREFIXED_I_SITES,
    leftover_2gram_sites_from_prefixed_3grams,
    split_i_076_070_sites,
    TestMamariILeftover076070PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    leftover_backward_3grams,
    leftover_previous_4grams,
    leftover_previous_stems,
    leftover_sites_without_backward,
    previous_stem_frequency_rows,
    previous_stem_frequency_table,
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_076_071_remaining_previous_stems_distinct_scoreboard import (
    STANDING_I_LEFTOVER_076_071_REMAINING_PREVIOUS_STEMS_ALL_DISTINCT as CYCLE203_CLAIM,
    STANDING_N_DISTINCT_REMAINING_PREVIOUS_STEMS as CYCLE203_N_DISTINCT,
    STANDING_N_REMAINING as CYCLE203_N_REMAINING,
    TestMamariILeftover076071RemainingPreviousStemsDistinctScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    GRAM2 as CYCLE205_GRAM2,
    NEAR_MISS_700_076_076_053,
    NEAR_MISS_999_090_076_071,
    STANDING_MATCHING_LEFTOVERS as CYCLE205_MATCHING_LEFTOVERS,
    TestMamariILeftoverN4076070Scoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    line_stems_for_site,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_REMAINING_DISTINCT = True
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
LOCKED_PREVIOUS_STEMS = frozenset({STEM_720})
STANDING_LOCKED_PREVIOUS_STEMS = (STEM_720,)
STANDING_N_I = CYCLE206_N_I
STANDING_N_090_PREFIXED = CYCLE210_N_090_PREFIXED
STANDING_N_LEFTOVER = 11
STANDING_N_SHARE_720 = 3
STANDING_N_REMAINING = 8
STANDING_N_DISTINCT_REMAINING = 8
STANDING_N_NO_BACKWARD = 0
STANDING_NO_BACKWARD_SITES = ()
STANDING_LOCKED_CLUSTER_SITES = CYCLE211_MATCHING_SITES
STANDING_REMAINING_SITES = CYCLE211_WITHOUT_SITES
STANDING_REMAINING_PREVIOUS_4GRAMS = (
    ("099", "571", "076", "070"),
    ("076", "295", "076", "070"),
    ("050", "048", "076", "070"),
    ("093", "205", "076", "070"),
    ("090", "099", "076", "070"),
    ("053", "029", "076", "070"),
    ("600", "604", "076", "070"),
    ("067", "606", "076", "070"),
)
STANDING_REMAINING_PREVIOUS_STEMS = (
    "571",
    "295",
    "048",
    "205",
    "099",
    "029",
    "604",
    "606",
)
STANDING_REMAINING_STEM_FREQUENCY = (
    (
        "571",
        1,
        ((SIDE_IA, "Ia1", 79),),
        (("099", "571", "076", "070"),),
    ),
    (
        "295",
        1,
        ((SIDE_IA, "Ia1", 141),),
        (("076", "295", "076", "070"),),
    ),
    (
        "048",
        1,
        ((SIDE_IA, "Ia2", 125),),
        (("050", "048", "076", "070"),),
    ),
    (
        "205",
        1,
        ((SIDE_IA, "Ia3", 123),),
        (("093", "205", "076", "070"),),
    ),
    (
        "099",
        1,
        ((SIDE_IA, "Ia5", 61),),
        (("090", "099", "076", "070"),),
    ),
    (
        "029",
        1,
        ((SIDE_IA, "Ia6", 144),),
        (("053", "029", "076", "070"),),
    ),
    (
        "604",
        1,
        ((SIDE_IA, "Ia13", 120),),
        (("600", "604", "076", "070"),),
    ),
    (
        "606",
        1,
        ((SIDE_IA, "Ia13", 140),),
        (("067", "606", "076", "070"),),
    ),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_070_remaining_previous_stems_distinct"
STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT = True
STANDING_RESULT = "i_leftover_076_070_remaining_previous_stems_distinct"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE213 = False
STANDING_SAME_AS_CYCLE212 = False
STANDING_SAME_AS_CYCLE211 = False
STANDING_SAME_AS_CYCLE210 = False
STANDING_SAME_AS_CYCLE203 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE203 = True
STANDING_090_PREFIXED_DOES_NOT_COUNT = True
STANDING_OFF_I_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_CYCLE211_720_CLUSTER_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_090_099_IS_REMAINING = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_remaining_sites(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
    locked: frozenset[str] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose previous stem exists and is not a locked cluster."""
    return tuple(
        site
        for site, back in zip(sites, backwards, strict=True)
        if back is not None and back[0] not in locked
    )


def leftover_remaining_previous_stems(
    backwards: tuple[tuple[str, ...] | None, ...],
    locked: frozenset[str] = LOCKED_PREVIOUS_STEMS,
) -> tuple[str, ...]:
    """Previous stems of leftover sites outside the locked 720 cluster."""
    return tuple(
        back[0]
        for back in backwards
        if back is not None and back[0] not in locked
    )


def remaining_previous_stem_is_shared(stems: tuple[str, ...]) -> bool:
    """True iff at least two remaining leftover sites share a previous stem."""
    return len(stems) != len(set(stems))


def i_leftover_076_070_remaining_previous_stems_distinct(
    n_remaining: int,
    n_distinct_remaining: int,
) -> bool:
    """True iff remaining leftover previous stems are all distinct.

    Claim holds only if N_distinct_remaining = N_remaining and
    N_remaining>=2. A singleton remaining set is not this claim.
    """
    return n_distinct_remaining == n_remaining and n_remaining >= 2


class TestILeftover076070RemainingPreviousStemsDistinctHelpers(unittest.TestCase):
    """Helpers on leftover I 076 070 remaining previous stems. No CV, no LLM."""

    def test_previous_requires_stem_before_2gram(self):
        """A previous stem is a 3-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE206_GRAM2)
        self.assertEqual(GRAM2, CYCLE205_GRAM2)
        self.assertEqual(GRAM3_BACKWARD, ("720", "076", "070"))
        self.assertEqual(STANDING_LOCKED_PREVIOUS_STEMS, ("720",))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        remaining_prev = ["099", "571", "076", "070", "720", "076"]
        self.assertEqual(site_previous_stem(remaining_prev, 2, GRAM2), "571")
        self.assertEqual(
            site_backward_3gram(remaining_prev, 2, GRAM2),
            ("571", "076", "070"),
        )
        self.assertEqual(
            site_previous_4gram(remaining_prev, 2, GRAM2),
            ("099", "571", "076", "070"),
        )
        self.assertNotIn("571", LOCKED_PREVIOUS_STEMS)
        locked_prev = ["069", "720", "076", "070", "720", "076"]
        self.assertEqual(site_previous_stem(locked_prev, 2, GRAM2), STEM_720)
        self.assertEqual(site_backward_3gram(locked_prev, 2, GRAM2), GRAM3_BACKWARD)
        self.assertIn(STEM_720, LOCKED_PREVIOUS_STEMS)
        start_of_line = ["076", "070", "090", "606"]
        self.assertIsNone(site_previous_stem(start_of_line, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(start_of_line, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(start_of_line, 0, GRAM2))
        mismatch_071 = ["720", "076", "071"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_distinct_requires_equal_counts_and_at_least_two(self):
        """Boolean is True only when N_distinct = N_remaining and N_remaining>=2."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_070_remaining_previous_stems_distinct(8, 8))
        self.assertTrue(i_leftover_076_070_remaining_previous_stems_distinct(2, 2))
        self.assertTrue(i_leftover_076_070_remaining_previous_stems_distinct(24, 24))
        self.assertFalse(i_leftover_076_070_remaining_previous_stems_distinct(8, 7))
        self.assertFalse(i_leftover_076_070_remaining_previous_stems_distinct(8, 9))
        self.assertFalse(i_leftover_076_070_remaining_previous_stems_distinct(11, 9))
        self.assertFalse(i_leftover_076_070_remaining_previous_stems_distinct(1, 1))
        self.assertFalse(i_leftover_076_070_remaining_previous_stems_distinct(0, 0))
        planted_stems = STANDING_REMAINING_PREVIOUS_STEMS + ("571",)
        self.assertTrue(remaining_previous_stem_is_shared(planted_stems))
        self.assertFalse(
            remaining_previous_stem_is_shared(STANDING_REMAINING_PREVIOUS_STEMS)
        )
        self.assertFalse(
            i_leftover_076_070_remaining_previous_stems_distinct(
                len(planted_stems),
                len(set(planted_stems)),
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_076_070_remaining_previous_stems_distinct",
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT,
            HYPOTHESIS_REMAINING_DISTINCT,
        )
        self.assertEqual(STANDING_N_SHARE_720 + STANDING_N_REMAINING, 11)
        self.assertEqual(STANDING_N_REMAINING, STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(provider.get_call_history(), [])

    def test_720_cluster_prefixed_off_i_and_076_071_do_not_count(self):
        """Locked 720 cluster, 090-prefixed I, off-I, leftover n=4, and 076 071 are not remaining."""
        provider = MockProvider()
        for site in STANDING_LOCKED_CLUSTER_SITES:
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        self.assertEqual(STANDING_LOCKED_CLUSTER_SITES, CYCLE211_MATCHING_SITES)
        self.assertEqual(len(STANDING_LOCKED_CLUSTER_SITES), STANDING_N_SHARE_720)
        self.assertTrue(STANDING_CYCLE211_720_CLUSTER_DOES_NOT_COUNT)
        for site in STANDING_PREFIXED_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LOCKED_CLUSTER_SITES)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertEqual(len(STANDING_PREFIXED_I_SITES), STANDING_N_090_PREFIXED)
        self.assertEqual(STANDING_N_090_PREFIXED, 8)
        for site in CYCLE206_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        self.assertEqual(len(CYCLE206_OFF_I_SITES), CYCLE206_N_OFF_I)
        self.assertEqual(CYCLE206_N_OFF_I, 5)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_REMAINING_SITES)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_LOCKED_CLUSTER_SITES)
        self.assertEqual(
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
            ("090", "099", "076", "070"),
        )
        self.assertTrue(STANDING_NEAR_MISS_090_099_IS_REMAINING)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertEqual(CYCLE203_N_REMAINING, 24)
        self.assertEqual(CYCLE203_N_DISTINCT, 24)
        self.assertTrue(CYCLE203_CLAIM)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE203)
        self.assertFalse(STANDING_SAME_AS_CYCLE203)
        self.assertEqual(CYCLE205_MATCHING_LEFTOVERS, (("999", "090", "076", "070"),))
        self.assertFalse(is_contiguous_substring(GRAM3_BACKWARD, CYCLE205_MATCHING_LEFTOVERS[0]))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_999_090_076_071))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_SAME_AS_CYCLE213)
        self.assertFalse(STANDING_SAME_AS_CYCLE212)
        self.assertFalse(STANDING_SAME_AS_CYCLE211)
        self.assertFalse(STANDING_SAME_AS_CYCLE210)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076070RemainingPreviousStemsDistinctScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover 076 070 remaining previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.measured_leftover, self.measured_prefixed = split_i_076_070_sites(
            self.i_sides,
            self.i_sites,
            GRAM2,
            PREFIXED_STEM,
        )
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.previous = leftover_previous_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.backwards = leftover_backward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.previous_4grams = leftover_previous_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.locked_sites = leftover_with_previous_720_076_070(
            self.leftover_sites,
            self.backwards,
        )
        self.remaining_sites = leftover_remaining_sites(
            self.leftover_sites,
            self.backwards,
        )
        self.without_720 = leftover_without_previous_720_076_070(
            self.leftover_sites,
            self.backwards,
        )
        self.no_backward = leftover_sites_without_backward(
            self.leftover_sites,
            self.previous,
        )
        self.remaining_previous_4grams = leftover_previous_4grams(
            self.i_sides,
            self.remaining_sites,
            GRAM2,
        )
        self.remaining_previous_stems = leftover_remaining_previous_stems(
            self.backwards
        )
        self.frequency = previous_stem_frequency_table(
            self.remaining_sites,
            self.remaining_previous_stems,
            self.remaining_previous_4grams,
        )
        self.n_i = len(self.i_sites)
        self.n_prefixed = len(self.measured_prefixed)
        self.n_leftover = len(self.measured_leftover)
        self.n_share = len(self.locked_sites)
        self.n_remaining = len(self.remaining_sites)
        self.n_distinct = len(set(self.remaining_previous_stems))
        self.n_no_backward = len(self.no_backward)
        self.claim_holds = i_leftover_076_070_remaining_previous_stems_distinct(
            self.n_remaining,
            self.n_distinct,
        )

    def test_tokens_and_sites_are_cycle_210_leftover_not_retuned(self):
        """2-gram and leftover 11 stay the cycle-213/212/211/210/206 locks."""
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM3_BACKWARD, ("720", "076", "070"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover, self.leftover_sites)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE210_N_LEFTOVER)
        self.assertEqual(CYCLE210_N_LEFTOVER, 11)
        self.assertEqual(self.i_sites, CYCLE206_I_SITES)
        self.assertEqual(len(self.i_sites), CYCLE206_N_I)
        self.assertEqual(CYCLE206_N_I, 19)
        self.assertEqual(self.n_i, 19)
        self.assertEqual(self.measured_prefixed, STANDING_PREFIXED_I_SITES)
        self.assertEqual(self.n_prefixed, STANDING_N_090_PREFIXED)
        self.assertEqual(STANDING_N_090_PREFIXED, 8)
        self.assertEqual(self.n_prefixed, CYCLE207_N_I)
        self.assertEqual(
            leftover_2gram_sites_from_prefixed_3grams(CYCLE207_I_SITES),
            STANDING_PREFIXED_I_SITES,
        )
        self.assertEqual(self.n_i - self.n_prefixed, self.n_leftover)
        self.assertEqual(19 - 8, 11)
        prior_213 = self.survey["i_720_076_070_previous_4grams_i_only"]
        self.assertEqual(prior_213["cycle"], 213)
        self.assertTrue(prior_213["i_720_076_070_previous_4grams_i_only"])
        self.assertTrue(CYCLE213_I_ONLY)
        self.assertEqual(prior_213["N_I_069"], CYCLE213_N_I_069)
        self.assertEqual(prior_213["N_off_I_069"], CYCLE213_N_OFF_I_069)
        self.assertEqual(prior_213["N_I_053"], CYCLE213_N_I_053)
        self.assertEqual(prior_213["N_off_I_053"], CYCLE213_N_OFF_I_053)
        self.assertEqual(prior_213["N_I_999"], CYCLE213_N_I_999)
        self.assertEqual(prior_213["N_off_I_999"], CYCLE213_N_OFF_I_999)
        self.assertEqual(prior_213["N_I_069"], 1)
        self.assertEqual(prior_213["N_off_I_069"], 0)
        self.assertEqual(prior_213["N_I_053"], 1)
        self.assertEqual(prior_213["N_off_I_053"], 0)
        self.assertEqual(prior_213["N_I_999"], 1)
        self.assertEqual(prior_213["N_off_I_999"], 0)
        self.assertEqual(
            [list(gram) for gram in CYCLE213_SEQUENCES],
            [row["tokens4"] for row in prior_213["sequences"]],
        )
        prior_212 = self.survey["i_3gram_720_076_070_i_only"]
        self.assertEqual(prior_212["cycle"], 212)
        self.assertEqual(tuple(prior_212["tokens3"]), CYCLE212_GRAM3)
        self.assertEqual(prior_212["N_I"], CYCLE212_N_I)
        self.assertEqual(prior_212["N_I"], 3)
        self.assertEqual(prior_212["N_off_I"], CYCLE212_N_OFF_I)
        self.assertEqual(prior_212["N_off_I"], 0)
        self.assertTrue(prior_212["i_3gram_720_076_070_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_212["i_sites"]),
            CYCLE212_I_SITES,
        )
        prior_211 = self.survey["i_leftover_076_070_previous_720"]
        self.assertEqual(prior_211["cycle"], 211)
        self.assertEqual(tuple(prior_211["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(prior_211["N_share"], CYCLE211_N_SHARE)
        self.assertEqual(prior_211["N_share"], 3)
        self.assertEqual(prior_211["N_leftover"], CYCLE211_N_LEFTOVER)
        self.assertEqual(prior_211["N_leftover"], 11)
        self.assertTrue(prior_211["i_leftover_076_070_previous_720"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_211["matching_leftover_sites"]),
            CYCLE211_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_211["without_sites"]),
            CYCLE211_WITHOUT_SITES,
        )
        prior_210 = self.survey["i_leftover_076_070_previous_stem"]
        self.assertEqual(prior_210["cycle"], 210)
        self.assertEqual(prior_210["N_leftover"], CYCLE210_N_LEFTOVER)
        self.assertEqual(prior_210["N_leftover"], 11)
        self.assertEqual(
            prior_210["N_distinct_previous_stems"],
            CYCLE210_N_DISTINCT,
        )
        self.assertEqual(prior_210["N_distinct_previous_stems"], 9)
        self.assertEqual(prior_210["N_no_backward"], CYCLE210_N_NO_BACKWARD)
        self.assertEqual(prior_210["N_no_backward"], 0)
        self.assertFalse(prior_210["i_leftover_076_070_share_one_previous_stem"])
        self.assertFalse(CYCLE210_SHARE_ONE)
        prior_206 = self.survey["i_2gram_076_070_i_only"]
        self.assertEqual(prior_206["cycle"], 206)
        self.assertFalse(prior_206["i_2gram_076_070_i_only"])
        self.assertEqual(prior_206["N_I"], CYCLE206_N_I)
        self.assertEqual(prior_206["N_I"], 19)
        self.assertEqual(prior_206["N_off_I"], CYCLE206_N_OFF_I)
        self.assertEqual(prior_206["N_off_I"], 5)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], CYCLE171_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], CYCLE171_N_OFF_I)
        self.assertEqual(prior_171["N_off_I"], 0)
        prior_203 = self.survey["i_leftover_076_071_remaining_previous_stems_distinct"]
        self.assertEqual(prior_203["cycle"], 203)
        self.assertEqual(prior_203["N_remaining"], 24)
        self.assertEqual(prior_203["N_distinct_remaining_previous_stems"], 24)
        self.assertTrue(prior_203["i_leftover_076_071_remaining_previous_stems_all_distinct"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_8_remaining_all_distinct_and_claim_holds(self):
        """N_leftover=11, N_share=3, N_remaining=8, N_distinct=8. Claim holds."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 11)
        self.assertEqual(self.n_share, STANDING_N_SHARE_720)
        self.assertEqual(STANDING_N_SHARE_720, 3)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING, 8)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING, 8)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(self.n_share + self.n_remaining + self.n_no_backward, self.n_leftover)
        self.assertEqual(self.n_leftover - self.n_share, self.n_remaining)
        self.assertEqual(11 - 3, 8)
        self.assertEqual(self.n_remaining, self.n_distinct)
        self.assertFalse(remaining_previous_stem_is_shared(self.remaining_previous_stems))
        self.assertTrue(
            i_leftover_076_070_remaining_previous_stems_distinct(
                self.n_remaining,
                self.n_distinct,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT)
        self.assertTrue(HYPOTHESIS_REMAINING_DISTINCT)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_076_070_remaining_previous_stems_distinct",
        )
        self.assertEqual(self.previous_4grams, CYCLE210_PREVIOUS_4GRAMS)
        if self.n_remaining != STANDING_N_REMAINING:
            self.fail("measured N_remaining drifted from 8")
        if self.n_distinct != self.n_remaining:
            self.fail("measured N_distinct_remaining != N_remaining")
        if remaining_previous_stem_is_shared(self.remaining_previous_stems):
            self.fail("a remaining leftover previous stem is shared")
        if self.n_leftover != 11 or self.n_share != 3:
            self.fail("nested cycle 210/211 leftover counts drifted")
        if self.n_i != 19 or self.n_prefixed != 8:
            self.fail("nested cycle 206/207 counts drifted; leftover cannot be trusted")
        self.assertEqual(len(set(STANDING_REMAINING_PREVIOUS_STEMS)), 8)
        self.assertEqual(len(STANDING_REMAINING_STEM_FREQUENCY), 8)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), 8)
        self.assertEqual(
            sum(count for _stem, count, _sites, _grams in self.frequency),
            8,
        )
        self.assertFalse(STANDING_SAME_AS_CYCLE213)
        self.assertFalse(STANDING_SAME_AS_CYCLE212)
        self.assertFalse(STANDING_SAME_AS_CYCLE211)
        self.assertFalse(STANDING_SAME_AS_CYCLE210)
        self.assertFalse(STANDING_SAME_AS_CYCLE203)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE203)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remaining_sites_inventory_and_disjoint_from_720_cluster(self):
        """Eight remaining leftover sites; previous stems unique; disjoint from leftover-3 720."""
        self.assertEqual(self.locked_sites, STANDING_LOCKED_CLUSTER_SITES)
        self.assertEqual(self.remaining_sites, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining_sites, CYCLE211_WITHOUT_SITES)
        self.assertEqual(self.remaining_sites, self.without_720)
        self.assertEqual(
            self.remaining_previous_4grams,
            STANDING_REMAINING_PREVIOUS_4GRAMS,
        )
        self.assertEqual(
            self.remaining_previous_stems,
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(self.frequency, STANDING_REMAINING_STEM_FREQUENCY)
        expected = (
            ((SIDE_IA, "Ia1", 79), ("099", "571", "076", "070"), "571"),
            ((SIDE_IA, "Ia1", 141), ("076", "295", "076", "070"), "295"),
            ((SIDE_IA, "Ia2", 125), ("050", "048", "076", "070"), "048"),
            ((SIDE_IA, "Ia3", 123), ("093", "205", "076", "070"), "205"),
            ((SIDE_IA, "Ia5", 61), ("090", "099", "076", "070"), "099"),
            ((SIDE_IA, "Ia6", 144), ("053", "029", "076", "070"), "029"),
            ((SIDE_IA, "Ia13", 120), ("600", "604", "076", "070"), "604"),
            ((SIDE_IA, "Ia13", 140), ("067", "606", "076", "070"), "606"),
        )
        for (site, prev4, stem), (want_site, want_prev4, want_stem) in zip(
            zip(
                self.remaining_sites,
                self.remaining_previous_4grams,
                self.remaining_previous_stems,
                strict=True,
            ),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(stems[index - 1], stem)
            self.assertNotEqual(stem, STEM_720)
            self.assertNotEqual(stem, PREFIXED_STEM)
            self.assertEqual(site_previous_stem(stems, index, GRAM2), stem)
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), (stem, "076", "070"))
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev4)
            self.assertEqual(prev4, want_prev4)
            self.assertEqual(site, want_site)
            self.assertEqual(stem, want_stem)
            self.assertEqual(prev4[1], stem)
            self.assertEqual(prev4[2:], GRAM2)
            self.assertNotEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, STANDING_PREFIXED_I_SITES)
            self.assertNotIn(site, CYCLE211_MATCHING_SITES)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(set(STANDING_REMAINING_SITES) & set(CYCLE211_MATCHING_SITES)), 0)
        for site in STANDING_LOCKED_CLUSTER_SITES:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(stems[index - 1], STEM_720)
            self.assertEqual(
                site_backward_3gram(stems, index, GRAM2),
                GRAM3_BACKWARD,
            )
            self.assertNotIn(site, self.remaining_sites)
        near_stems = line_stems_for_site(
            self.i_sides,
            STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
        )
        near_index = STANDING_NEAR_MISS_LEFTOVER_090_099_SITE[2]
        self.assertEqual(
            site_previous_4gram(near_stems, near_index, GRAM2),
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
        )
        self.assertEqual(site_previous_stem(near_stems, near_index, GRAM2), "099")
        self.assertIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, self.remaining_sites)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, self.locked_sites)
        for site in STANDING_PREFIXED_I_SITES:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(stems[index - 1], PREFIXED_STEM)
            self.assertEqual(
                tuple(stems[index - 1 : index + STANDING_N2]),
                CYCLE207_GRAM3,
            )
            self.assertNotIn(site, self.remaining_sites)
            self.assertNotIn(site, self.leftover_sites)
        for site in CYCLE206_OFF_I_SITES:
            self.assertNotIn(site, self.remaining_sites)
            self.assertNotIn(site, self.leftover_sites)
        for site in CYCLE212_I_SITES:
            leftover = (site[0], site[1], site[2] + 1)
            self.assertIn(leftover, self.locked_sites)
            self.assertNotIn(leftover, self.remaining_sites)
        measured_local = leftover_local_4grams(
            self.i_sides,
            self.remaining_sites,
            GRAM2,
        )
        for (site, prev4, _nxt), stem in zip(
            measured_local,
            self.remaining_previous_stems,
            strict=True,
        ):
            self.assertIsNotNone(prev4)
            self.assertEqual(prev4[1], stem)
            self.assertEqual(prev4[2:], GRAM2)
            self.assertNotEqual(prev4[1:], GRAM3_BACKWARD)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_213_212_211_210_and_171_scoreboards_still_compute(self):
        """Cycle 213 hapax 1/0 x3, 212 3/0, 211 N_share=3/11, 210 N_distinct=9, 171 43/0 stay."""
        prior_213 = TestMamariI720076070Previous4gramsIOnlyScoreboard()
        prior_213.setUp()
        prior_213.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_213.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE213_N_I_069, 1)
        self.assertEqual(CYCLE213_N_OFF_I_069, 0)
        self.assertEqual(CYCLE213_N_I_053, 1)
        self.assertEqual(CYCLE213_N_OFF_I_053, 0)
        self.assertEqual(CYCLE213_N_I_999, 1)
        self.assertEqual(CYCLE213_N_OFF_I_999, 0)
        self.assertTrue(CYCLE213_I_ONLY)
        prior_212 = TestMamariI3gram720076070IOnlyScoreboard()
        prior_212.setUp()
        prior_212.test_i_hits_are_three_on_ia_all_leftover()
        prior_212.test_3gram_is_zero_off_i_and_i_only()
        prior_212.test_survey_matches_computed_lock()
        self.assertEqual(prior_212.i_hits, 3)
        self.assertEqual(prior_212.off_i_hits, 0)
        self.assertEqual(prior_212.i_sites, CYCLE212_I_SITES)
        self.assertEqual(CYCLE212_N_I, 3)
        self.assertEqual(CYCLE212_N_OFF_I, 0)
        prior_211 = TestMamariILeftover076070Previous720Scoreboard()
        prior_211.setUp()
        prior_211.test_counts_3_of_11_and_hypothesis_n_3_holds()
        prior_211.test_survey_matches_computed_lock()
        self.assertEqual(prior_211.n_share, 3)
        self.assertEqual(prior_211.n_leftover, 11)
        self.assertEqual(CYCLE211_N_SHARE, 3)
        self.assertEqual(CYCLE211_N_LEFTOVER, 11)
        self.assertEqual(prior_211.with_sites, CYCLE211_MATCHING_SITES)
        self.assertEqual(prior_211.without_sites, self.remaining_sites)
        prior_210 = TestMamariILeftover076070PreviousStemScoreboard()
        prior_210.setUp()
        prior_210.test_counts_9_distinct_previous_stems_and_claim_loses()
        prior_210.test_survey_matches_computed_lock()
        self.assertEqual(prior_210.n_distinct, CYCLE210_N_DISTINCT)
        self.assertEqual(prior_210.n_leftover, CYCLE210_N_LEFTOVER)
        self.assertEqual(CYCLE210_N_DISTINCT, 9)
        self.assertEqual(CYCLE210_N_LEFTOVER, 11)
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        self.assertEqual(prior_206.i_hits, 19)
        self.assertEqual(prior_206.off_i_hits, 5)
        self.assertEqual(CYCLE206_N_I, 19)
        self.assertEqual(CYCLE206_N_OFF_I, 5)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(len(prior_171.i_sites), 43)
        self.assertEqual(prior_171.i_sites, CYCLE171_I_SITES)
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        prior_203 = TestMamariILeftover076071RemainingPreviousStemsDistinctScoreboard()
        prior_203.setUp()
        prior_203.test_counts_24_of_34_remaining_all_distinct_and_claim_holds()
        prior_203.test_survey_matches_computed_lock()
        self.assertEqual(prior_203.n_remaining, 24)
        self.assertEqual(prior_203.n_distinct, 24)
        self.assertEqual(CYCLE203_N_REMAINING, 24)
        self.assertEqual(CYCLE203_N_DISTINCT, 24)
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-214 leftover remaining previous-stem lock."""
        lock = self.survey["i_leftover_076_070_remaining_previous_stems_distinct"]
        self.assertEqual(lock["cycle"], 214)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_remaining_previous_stems_distinct"])
        self.assertEqual(
            lock["hypothesis_remaining_previous_stems_distinct"],
            HYPOTHESIS_REMAINING_DISTINCT,
        )
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["locked_previous_stems"]), STANDING_LOCKED_PREVIOUS_STEMS)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 19)
        self.assertEqual(lock["N_090_prefixed"], STANDING_N_090_PREFIXED)
        self.assertEqual(lock["N_090_prefixed"], 8)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 11)
        self.assertEqual(lock["N_leftover"], lock["N_I"] - lock["N_090_prefixed"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE210_PREVIOUS_4GRAMS],
            lock["leftover_previous_4grams"],
        )
        self.assertEqual(lock["N_share_720"], STANDING_N_SHARE_720)
        self.assertEqual(lock["N_share_720"], 3)
        self.assertEqual(lock["N_locked_cluster"], STANDING_N_SHARE_720)
        self.assertEqual(lock["N_locked_cluster"], 3)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 8)
        self.assertEqual(lock["N_remaining"], lock["N_leftover"] - lock["N_share_720"])
        self.assertEqual(
            lock["N_distinct_remaining_previous_stems"],
            STANDING_N_DISTINCT_REMAINING,
        )
        self.assertEqual(lock["N_distinct_remaining_previous_stems"], 8)
        self.assertEqual(lock["N_distinct_remaining"], 8)
        self.assertEqual(lock["N_no_backward"], STANDING_N_NO_BACKWARD)
        self.assertEqual(lock["N_no_backward"], 0)
        self.assertEqual(lock["no_backward_sites"], [])
        self.assertEqual(
            tuple(tuple(row) for row in lock["locked_cluster_sites"]),
            STANDING_LOCKED_CLUSTER_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_leftover_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_REMAINING_PREVIOUS_4GRAMS],
            lock["remaining_previous_4grams"],
        )
        self.assertEqual(
            tuple(lock["remaining_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(
            lock["remaining_leftover_local_4grams"],
            matching_leftover_local_4gram_rows(
                STANDING_REMAINING_SITES,
                STANDING_REMAINING_PREVIOUS_4GRAMS,
            ),
        )
        self.assertEqual(
            lock["remaining_previous_stem_frequency"],
            previous_stem_frequency_rows(STANDING_REMAINING_STEM_FREQUENCY),
        )
        self.assertEqual(len(lock["remaining_previous_stem_frequency"]), 8)
        for row in lock["remaining_previous_stem_frequency"]:
            self.assertEqual(row["count"], 1)
        self.assertEqual(
            [row["previous_stem"] for row in lock["remaining_previous_stem_frequency"]],
            list(STANDING_REMAINING_PREVIOUS_STEMS),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["prefixed_i_sites"]),
            STANDING_PREFIXED_I_SITES,
        )
        self.assertEqual(
            tuple(lock["near_miss_leftover_090_099_site"]),
            STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
        )
        self.assertEqual(
            tuple(lock["near_miss_leftover_090_099_previous_4gram"]),
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
        )
        self.assertTrue(lock["090_prefixed_does_not_count"])
        self.assertTrue(lock["near_miss_090_099_is_remaining"])
        self.assertTrue(lock["cycle211_720_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE211_MATCHING_SITES],
            lock["cycle211_matching_sites"],
        )
        self.assertEqual(lock["cycle211_N_share"], 3)
        self.assertTrue(lock["remaining_sites_disjoint_from_720_cluster"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_070_remaining_previous_stems_distinct"])
        self.assertEqual(
            lock["i_leftover_076_070_remaining_previous_stems_distinct"],
            STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle213"])
        self.assertFalse(lock["same_as_cycle212"])
        self.assertFalse(lock["same_as_cycle211"])
        self.assertFalse(lock["same_as_cycle210"])
        self.assertFalse(lock["same_as_cycle203"])
        self.assertTrue(lock["same_claim_shape_as_cycle_203"])
        self.assertTrue(lock["off_i_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_720_076_070_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_720_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_720_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_remaining_previous_stems_distinct_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["cycle"], 213)
        self.assertTrue(
            self.survey["i_720_076_070_previous_4grams_i_only"][
                "i_720_076_070_previous_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["N_I_069"], 1)
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["N_off_I_069"], 0)
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["N_I_053"], 1)
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["N_off_I_053"], 0)
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["N_I_999"], 1)
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["N_off_I_999"], 0)
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["cycle"], 212)
        self.assertTrue(
            self.survey["i_3gram_720_076_070_i_only"]["i_3gram_720_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["cycle"], 211)
        self.assertTrue(
            self.survey["i_leftover_076_070_previous_720"][
                "i_leftover_076_070_previous_720"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["N_share"], 3)
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["N_leftover"], 11)
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["cycle"], 210)
        self.assertEqual(
            self.survey["i_leftover_076_070_previous_stem"]["N_distinct_previous_stems"],
            9,
        )
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["N_leftover"], 11)
        self.assertFalse(
            self.survey["i_leftover_076_070_previous_stem"][
                "i_leftover_076_070_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(
            self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_previous_stems_distinct"]["cycle"],
            203,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_remaining_previous_stems_distinct"][
                "i_leftover_076_071_remaining_previous_stems_all_distinct"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_previous_stems_distinct"][
                "N_remaining"
            ],
            24,
        )
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
            ]
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
        self.assertTrue(
            self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"]
        )
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(
            self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"]
        )
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"],
            5,
        )
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover076070RemainingPreviousStemsDistinctImageSnapshot(
    unittest.TestCase
):
    """Cycle 214 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
