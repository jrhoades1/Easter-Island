"""I's cycle-172 leftover 2-gram remaining previous-stem distinct lock.

Cycle 203 text-search lock. Uses already-vendored A–V and the
cycle-172 leftover 34 sites of 2-gram 076 071 (the I sites
that do not sit inside leftover n=4 maximals 999 090 076 071,
999 205 076 071, 076 071 009 090, or 076 071 090 999). Does
not retune that 2-gram, those leftover sites, or the leftover
n=4 set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each leftover site, record the previous token immediately
before 076 071 (backward 3-gram W 076 071 and previous 4-gram
V W 076 071 when they exist). Start-of-line is no-backward.
Partition leftover sites into already-locked clusters
(previous stem in {700, 090, 604, 099}) vs remaining. Cycle
191 leftover-3, cycle 194 leftover-3, cycle 197 leftover-2,
and cycle 200 leftover-2 are the locked clusters (3+3+2+2
= 10). The remaining 24 are the leftover sites whose previous
stem is not in that set. Cycle 190 recorded leftover previous
4-grams; this cycle re-measures them from fixtures and does
not treat those as assumed. The 9 inside-family sites do
not count as leftover. 071 999 and 076 076 do not count as
this 2-gram.

Claim that can lose:
i_leftover_076_071_remaining_previous_stems_all_distinct. True
only if N_remaining=24 and N_distinct_remaining_previous_stems=24
and N_no_backward=0. Measured: N_leftover=34, N_locked_cluster=10,
N_remaining=24, N_distinct_remaining_previous_stems=24,
N_no_backward=0. The claim is true. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES as CYCLE171_I_SITES,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    STANDING_CONTAINERS,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_PREVIOUS_4GRAMS as CYCLE172_PREVIOUS_4GRAMS,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE172_N_LEFTOVER,
    leftover_local_4grams,
    TestMamariI2gram076071InsideFamilyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_inside_family_scoreboard import (
    leftover_sites_from_membership,
    membership_for_sites,
)
from tests.test_mamari_i_leftover_076_071_previous_090_scoreboard import (
    GRAM3_BACKWARD as CYCLE194_GRAM3_BACKWARD,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE194_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE194_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_090_076_071 as CYCLE194_N_WITH,
    TestMamariILeftover076071Previous090Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_099_scoreboard import (
    GRAM3_BACKWARD as CYCLE200_GRAM3_BACKWARD,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE200_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE200_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_099_076_071 as CYCLE200_N_WITH,
    matching_leftover_local_4gram_rows,
    TestMamariILeftover076071Previous099Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_604_scoreboard import (
    GRAM3_BACKWARD as CYCLE197_GRAM3_BACKWARD,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE197_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE197_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_604_076_071 as CYCLE197_N_WITH,
    TestMamariILeftover076071Previous604Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_700_scoreboard import (
    GRAM3_BACKWARD as CYCLE191_GRAM3_BACKWARD,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE191_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE191_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_700_076_071 as CYCLE191_N_WITH,
    STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM as CYCLE191_NEAR_MISS_700_604_PREVIOUS_4GRAM,
    STANDING_NEAR_MISS_LEFTOVER_700_604_SITE as CYCLE191_NEAR_MISS_700_604_SITE,
    TestMamariILeftover076071Previous700Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE190_N_DISTINCT,
    STANDING_N_NO_BACKWARD as CYCLE190_N_NO_BACKWARD,
    STANDING_N_WITH_BACKWARD as CYCLE190_N_WITH_BACKWARD,
    leftover_backward_3grams,
    leftover_previous_4grams,
    leftover_previous_stems,
    leftover_sites_without_backward,
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
    TestMamariILeftover076071PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    NEAR_MISS_071_065_071_999,
    NEAR_MISS_700_076_076_053,
    TestMamariILeftoverN4076071Scoreboard,
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

HYPOTHESIS_N_REMAINING = 24
HYPOTHESIS_N_DISTINCT = 24
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
LOCKED_PREVIOUS_STEMS = frozenset({"700", "090", "604", "099"})
STANDING_LOCKED_PREVIOUS_STEMS = ("700", "090", "604", "099")
STANDING_N_LEFTOVER = 34
STANDING_N_LOCKED_CLUSTER = 10
STANDING_N_REMAINING = 24
STANDING_N_DISTINCT_REMAINING_PREVIOUS_STEMS = 24
STANDING_N_NO_BACKWARD = 0
STANDING_NO_BACKWARD_SITES = ()
STANDING_LOCKED_CLUSTER_SITES = (
    (SIDE_IA, "Ia1", 163),
    (SIDE_IA, "Ia2", 51),
    (SIDE_IA, "Ia3", 147),
    (SIDE_IA, "Ia5", 67),
    (SIDE_IA, "Ia6", 117),
    (SIDE_IA, "Ia9", 10),
    (SIDE_IA, "Ia12", 6),
    (SIDE_IA, "Ia13", 128),
    (SIDE_IA, "Ia13", 153),
    (SIDE_IA, "Ia14", 106),
)
STANDING_REMAINING_SITES = (
    (SIDE_IA, "Ia1", 86),
    (SIDE_IA, "Ia2", 43),
    (SIDE_IA, "Ia2", 104),
    (SIDE_IA, "Ia2", 169),
    (SIDE_IA, "Ia3", 13),
    (SIDE_IA, "Ia3", 85),
    (SIDE_IA, "Ia3", 110),
    (SIDE_IA, "Ia3", 133),
    (SIDE_IA, "Ia5", 79),
    (SIDE_IA, "Ia5", 134),
    (SIDE_IA, "Ia7", 32),
    (SIDE_IA, "Ia7", 48),
    (SIDE_IA, "Ia8", 27),
    (SIDE_IA, "Ia12", 19),
    (SIDE_IA, "Ia12", 59),
    (SIDE_IA, "Ia12", 63),
    (SIDE_IA, "Ia13", 44),
    (SIDE_IA, "Ia13", 54),
    (SIDE_IA, "Ia13", 92),
    (SIDE_IA, "Ia13", 101),
    (SIDE_IA, "Ia13", 114),
    (SIDE_IA, "Ia13", 149),
    (SIDE_IA, "Ia14", 81),
    (SIDE_IA, "Ia14", 166),
)
STANDING_REMAINING_PREVIOUS_4GRAMS = (
    ("027", "200", "076", "071"),
    ("430", "071", "076", "071"),
    ("005", "633", "076", "071"),
    ("147", "076", "076", "071"),
    ("205", "225", "076", "071"),
    ("076", "385", "076", "071"),
    ("530", "298", "076", "071"),
    ("070", "205", "076", "071"),
    ("999", "406", "076", "071"),
    ("071", "072", "076", "071"),
    ("076", "999", "076", "071"),
    ("400", "222", "076", "071"),
    ("002", "514", "076", "071"),
    ("490", "440", "076", "071"),
    ("050", "606", "076", "071"),
    ("061", "290", "076", "071"),
    ("002", "009", "076", "071"),
    ("999", "007", "076", "071"),
    ("073", "006", "076", "071"),
    ("042", "730", "076", "071"),
    ("084", "600", "076", "071"),
    ("006", "048", "076", "071"),
    ("076", "011", "076", "071"),
    ("006", "000", "076", "071"),
)
STANDING_REMAINING_PREVIOUS_STEMS = (
    "200",
    "071",
    "633",
    "076",
    "225",
    "385",
    "298",
    "205",
    "406",
    "072",
    "999",
    "222",
    "514",
    "440",
    "606",
    "290",
    "009",
    "007",
    "006",
    "730",
    "600",
    "048",
    "011",
    "000",
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_071_remaining_previous_stems_all_distinct"
STANDING_I_LEFTOVER_076_071_REMAINING_PREVIOUS_STEMS_ALL_DISTINCT = True
STANDING_RESULT = "i_leftover_076_071_remaining_previous_stems_distinct"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE191 = False
STANDING_SAME_AS_CYCLE194 = False
STANDING_SAME_AS_CYCLE197 = False
STANDING_SAME_AS_CYCLE200 = False
STANDING_SAME_AS_CYCLE190 = False
STANDING_SHARE_ONE_PREVIOUS_STEM_NOT_LOCKED = True
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_CYCLE191_700_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE194_090_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE197_604_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE200_099_CLUSTER_DOES_NOT_COUNT = True


def previous_stem_of_backward(back: tuple[str, ...] | None) -> str | None:
    """Previous stem W from backward 3-gram W 076 071; None if no-backward."""
    if back is None:
        return None
    return back[0]


def leftover_locked_cluster_sites(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
    locked: frozenset[str] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose previous stem is in the locked cluster set."""
    return tuple(
        site
        for site, back in zip(sites, backwards, strict=True)
        if previous_stem_of_backward(back) in locked
    )


def leftover_remaining_sites(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
    locked: frozenset[str] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose previous stem exists and is not a locked cluster."""
    return tuple(
        site
        for site, back in zip(sites, backwards, strict=True)
        if (stem := previous_stem_of_backward(back)) is not None and stem not in locked
    )


def leftover_remaining_previous_stems(
    backwards: tuple[tuple[str, ...] | None, ...],
    locked: frozenset[str] = LOCKED_PREVIOUS_STEMS,
) -> tuple[str, ...]:
    """Previous stems of leftover sites outside the locked clusters."""
    return tuple(
        stem
        for back in backwards
        if (stem := previous_stem_of_backward(back)) is not None and stem not in locked
    )


def remaining_previous_stem_is_shared(stems: tuple[str, ...]) -> bool:
    """True iff at least two remaining leftover sites share a previous stem."""
    return len(stems) != len(set(stems))


def i_leftover_076_071_remaining_previous_stems_all_distinct(
    n_remaining: int,
    n_distinct_remaining_previous_stems: int,
    n_no_backward: int,
    expected_remaining: int = HYPOTHESIS_N_REMAINING,
    expected_distinct: int = HYPOTHESIS_N_DISTINCT,
) -> bool:
    """True iff N_remaining=24, N_distinct=24, and N_no_backward=0."""
    return (
        n_remaining == expected_remaining
        and n_distinct_remaining_previous_stems == expected_distinct
        and n_no_backward == 0
    )


class TestILeftover076071RemainingPreviousStemsDistinctHelpers(unittest.TestCase):
    """Helpers on cycle-172 leftover 076 071 remaining previous stems. No CV, no LLM."""

    def test_previous_requires_stem_before_2gram(self):
        """A previous stem is a 3-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(STANDING_LOCKED_PREVIOUS_STEMS, ("700", "090", "604", "099"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        remaining_prev = ["027", "200", "076", "071", "090", "606"]
        self.assertEqual(site_previous_stem(remaining_prev, 2, GRAM2), "200")
        self.assertEqual(
            site_backward_3gram(remaining_prev, 2, GRAM2),
            ("200", "076", "071"),
        )
        self.assertEqual(
            site_previous_4gram(remaining_prev, 2, GRAM2),
            ("027", "200", "076", "071"),
        )
        self.assertEqual(
            previous_stem_of_backward(site_backward_3gram(remaining_prev, 2, GRAM2)),
            "200",
        )
        self.assertNotIn("200", LOCKED_PREVIOUS_STEMS)
        cycle200_prev = ["430", "099", "076", "071", "632", "670"]
        self.assertEqual(
            site_backward_3gram(cycle200_prev, 2, GRAM2),
            CYCLE200_GRAM3_BACKWARD,
        )
        self.assertIn(
            previous_stem_of_backward(site_backward_3gram(cycle200_prev, 2, GRAM2)),
            LOCKED_PREVIOUS_STEMS,
        )
        cycle197_prev = ["600", "604", "076", "071", "061", "011"]
        self.assertEqual(
            site_backward_3gram(cycle197_prev, 2, GRAM2),
            CYCLE197_GRAM3_BACKWARD,
        )
        cycle194_prev = ["000", "090", "076", "071", "004", "004"]
        self.assertEqual(
            site_backward_3gram(cycle194_prev, 2, GRAM2),
            CYCLE194_GRAM3_BACKWARD,
        )
        cycle191_prev = ["090", "700", "076", "071", "700", "076"]
        self.assertEqual(
            site_backward_3gram(cycle191_prev, 2, GRAM2),
            CYCLE191_GRAM3_BACKWARD,
        )
        start_of_line = ["076", "071", "090", "606"]
        self.assertIsNone(site_previous_stem(start_of_line, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(start_of_line, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(start_of_line, 0, GRAM2))
        self.assertIsNone(previous_stem_of_backward(None))
        mismatch = ["200", "076", "070"]
        self.assertIsNone(site_previous_stem(mismatch, 1, GRAM2))
        self.assertEqual(provider.get_call_history(), [])

    def test_all_distinct_can_fail(self):
        """Boolean is True only when N_remaining=24, N_distinct=24, N_no_backward=0."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_076_071_remaining_previous_stems_all_distinct(24, 24, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_previous_stems_all_distinct(23, 23, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_previous_stems_all_distinct(25, 25, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_previous_stems_all_distinct(24, 23, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_previous_stems_all_distinct(24, 24, 1)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_previous_stems_all_distinct(34, 34, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_previous_stems_all_distinct(0, 0, 0)
        )
        planted_stems = STANDING_REMAINING_PREVIOUS_STEMS + ("200",)
        self.assertTrue(remaining_previous_stem_is_shared(planted_stems))
        self.assertFalse(
            remaining_previous_stem_is_shared(STANDING_REMAINING_PREVIOUS_STEMS)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_previous_stems_all_distinct(
                len(planted_stems),
                len(set(planted_stems)),
                0,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_076_071_remaining_previous_stems_all_distinct",
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_PREVIOUS_STEMS_ALL_DISTINCT)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_071_REMAINING_PREVIOUS_STEMS_ALL_DISTINCT,
            HYPOTHESIS_N_REMAINING == STANDING_N_REMAINING
            and HYPOTHESIS_N_DISTINCT == STANDING_N_DISTINCT_REMAINING_PREVIOUS_STEMS
            and STANDING_N_NO_BACKWARD == 0,
        )
        self.assertEqual(
            STANDING_N_LOCKED_CLUSTER + STANDING_N_REMAINING + STANDING_N_NO_BACKWARD,
            34,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_locked_clusters_inside_family_and_near_misses_do_not_count(self):
        """Locked 700/090/604/099 clusters, inside family, 071 999, and 076 076 are not remaining."""
        provider = MockProvider()
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LOCKED_CLUSTER_SITES)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        locked_clusters = (
            (CYCLE191_MATCHING_SITES, CYCLE191_N_WITH, CYCLE191_GRAM3_BACKWARD, "700"),
            (CYCLE194_MATCHING_SITES, CYCLE194_N_WITH, CYCLE194_GRAM3_BACKWARD, "090"),
            (CYCLE197_MATCHING_SITES, CYCLE197_N_WITH, CYCLE197_GRAM3_BACKWARD, "604"),
            (CYCLE200_MATCHING_SITES, CYCLE200_N_WITH, CYCLE200_GRAM3_BACKWARD, "099"),
        )
        for prior_sites, n_with, gram3, stem in locked_clusters:
            self.assertEqual(len(prior_sites), n_with)
            self.assertEqual(gram3[0], stem)
            self.assertIn(stem, LOCKED_PREVIOUS_STEMS)
            for site in prior_sites:
                self.assertIn(site, STANDING_LEFTOVER_SITES)
                self.assertIn(site, STANDING_LOCKED_CLUSTER_SITES)
                self.assertNotIn(site, STANDING_REMAINING_SITES)
        self.assertTrue(STANDING_CYCLE191_700_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE194_090_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE197_604_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE200_099_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(CYCLE191_N_WITH, 3)
        self.assertEqual(CYCLE194_N_WITH, 3)
        self.assertEqual(CYCLE197_N_WITH, 2)
        self.assertEqual(CYCLE200_N_WITH, 2)
        locked_set = (
            set(CYCLE191_MATCHING_SITES)
            | set(CYCLE194_MATCHING_SITES)
            | set(CYCLE197_MATCHING_SITES)
            | set(CYCLE200_MATCHING_SITES)
        )
        self.assertEqual(len(locked_set), 3 + 3 + 2 + 2)
        self.assertEqual(locked_set, set(STANDING_LOCKED_CLUSTER_SITES))
        self.assertEqual(len(set(STANDING_REMAINING_SITES) & locked_set), 0)
        self.assertIn(CYCLE191_NEAR_MISS_700_604_SITE, STANDING_LOCKED_CLUSTER_SITES)
        self.assertNotIn(CYCLE191_NEAR_MISS_700_604_SITE, STANDING_REMAINING_SITES)
        self.assertEqual(CYCLE191_NEAR_MISS_700_604_SITE, (SIDE_IA, "Ia9", 10))
        self.assertEqual(
            CYCLE191_NEAR_MISS_700_604_PREVIOUS_4GRAM,
            ("700", "604", "076", "071"),
        )
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_SHARE_ONE_PREVIOUS_STEM_NOT_LOCKED)
        self.assertFalse(STANDING_SAME_AS_CYCLE191)
        self.assertFalse(STANDING_SAME_AS_CYCLE194)
        self.assertFalse(STANDING_SAME_AS_CYCLE197)
        self.assertFalse(STANDING_SAME_AS_CYCLE200)
        self.assertFalse(STANDING_SAME_AS_CYCLE190)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076071RemainingPreviousStemsDistinctScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover 076 071 remaining previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.membership = membership_for_sites(
            self.i_sides,
            self.i_sites,
            STANDING_CONTAINERS,
            GRAM2,
        )
        self.measured_leftover = leftover_sites_from_membership(
            self.i_sites,
            self.membership,
        )
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
        self.locked_sites = leftover_locked_cluster_sites(
            self.leftover_sites,
            self.backwards,
        )
        self.remaining_sites = leftover_remaining_sites(
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
        self.n_leftover = len(self.leftover_sites)
        self.n_locked = len(self.locked_sites)
        self.n_remaining = len(self.remaining_sites)
        self.n_distinct = len(set(self.remaining_previous_stems))
        self.n_no_backward = len(self.no_backward)
        self.claim_holds = i_leftover_076_071_remaining_previous_stems_all_distinct(
            self.n_remaining,
            self.n_distinct,
            self.n_no_backward,
        )

    def test_tokens_and_sites_are_cycle_172_leftover_not_retuned(self):
        """2-gram and leftover 34 stay the cycle-200/197/194/191/190/172/171 locks."""
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(STANDING_LOCKED_PREVIOUS_STEMS, ("700", "090", "604", "099"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover, self.leftover_sites)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE172_N_LEFTOVER)
        self.assertEqual(CYCLE172_N_LEFTOVER, 34)
        self.assertEqual(self.i_sites, CYCLE171_I_SITES)
        self.assertEqual(len(self.i_sites), CYCLE171_N_I)
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(len(STANDING_INSIDE_SITES), STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 9)
        self.assertEqual(STANDING_N_INSIDE + STANDING_N_LEFTOVER, CYCLE171_N_I)
        prior_200 = self.survey["i_leftover_076_071_previous_099"]
        self.assertEqual(prior_200["cycle"], 200)
        self.assertEqual(tuple(prior_200["backward_3gram"]), CYCLE200_GRAM3_BACKWARD)
        self.assertEqual(prior_200["N_leftover"], 34)
        self.assertEqual(prior_200["N_with_previous_099_076_071"], CYCLE200_N_WITH)
        self.assertEqual(prior_200["N_with_previous_099_076_071"], 2)
        self.assertTrue(prior_200["i_leftover_076_071_exactly_2_previous_099_076_071"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_200["matching_leftover_sites"]),
            CYCLE200_MATCHING_SITES,
        )
        prior_197 = self.survey["i_leftover_076_071_previous_604"]
        self.assertEqual(prior_197["cycle"], 197)
        self.assertEqual(tuple(prior_197["backward_3gram"]), CYCLE197_GRAM3_BACKWARD)
        self.assertEqual(prior_197["N_leftover"], 34)
        self.assertEqual(prior_197["N_with_previous_604_076_071"], CYCLE197_N_WITH)
        self.assertEqual(prior_197["N_with_previous_604_076_071"], 2)
        self.assertTrue(prior_197["i_leftover_076_071_exactly_2_previous_604_076_071"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_197["matching_leftover_sites"]),
            CYCLE197_MATCHING_SITES,
        )
        prior_194 = self.survey["i_leftover_076_071_previous_090"]
        self.assertEqual(prior_194["cycle"], 194)
        self.assertEqual(tuple(prior_194["backward_3gram"]), CYCLE194_GRAM3_BACKWARD)
        self.assertEqual(prior_194["N_leftover"], 34)
        self.assertEqual(prior_194["N_with_previous_090_076_071"], CYCLE194_N_WITH)
        self.assertEqual(prior_194["N_with_previous_090_076_071"], 3)
        self.assertTrue(prior_194["i_leftover_076_071_exactly_3_previous_090_076_071"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_194["matching_leftover_sites"]),
            CYCLE194_MATCHING_SITES,
        )
        prior_191 = self.survey["i_leftover_076_071_previous_700"]
        self.assertEqual(prior_191["cycle"], 191)
        self.assertEqual(tuple(prior_191["backward_3gram"]), CYCLE191_GRAM3_BACKWARD)
        self.assertEqual(prior_191["N_leftover"], 34)
        self.assertEqual(prior_191["N_with_previous_700_076_071"], CYCLE191_N_WITH)
        self.assertEqual(prior_191["N_with_previous_700_076_071"], 3)
        self.assertTrue(prior_191["i_leftover_076_071_exactly_3_previous_700_076_071"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_191["matching_leftover_sites"]),
            CYCLE191_MATCHING_SITES,
        )
        prior_190 = self.survey["i_leftover_076_071_previous_stem"]
        self.assertEqual(prior_190["cycle"], 190)
        self.assertEqual(prior_190["N_leftover"], 34)
        self.assertEqual(prior_190["N_with_backward"], CYCLE190_N_WITH_BACKWARD)
        self.assertEqual(prior_190["N_with_backward"], 34)
        self.assertEqual(prior_190["N_no_backward"], CYCLE190_N_NO_BACKWARD)
        self.assertEqual(prior_190["N_no_backward"], 0)
        self.assertEqual(
            prior_190["N_distinct_previous_stems"],
            CYCLE190_N_DISTINCT,
        )
        self.assertEqual(prior_190["N_distinct_previous_stems"], 28)
        self.assertFalse(prior_190["i_leftover_076_071_share_one_previous_stem"])
        prior_172 = self.survey["i_2gram_076_071_inside_family"]
        self.assertEqual(prior_172["cycle"], 172)
        self.assertEqual(tuple(prior_172["tokens2"]), GRAM2)
        self.assertEqual(prior_172["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_172["N_leftover"], 34)
        self.assertEqual(
            tuple(tuple(row) for row in prior_172["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE172_PREVIOUS_4GRAMS],
            prior_172["leftover_previous_4grams"],
        )
        self.assertFalse(prior_172["i_2gram_076_071_all_inside_leftover_n4_family"])
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], CYCLE171_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], CYCLE171_N_OFF_I)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_SHARE_ONE_PREVIOUS_STEM_NOT_LOCKED)
        self.assertTrue(STANDING_CYCLE191_700_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE194_090_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE197_604_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE200_099_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_24_of_34_remaining_all_distinct_and_claim_holds(self):
        """N_leftover=34, N_locked=10, N_remaining=24, N_distinct=24. Claim holds."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 34)
        self.assertEqual(self.n_locked, STANDING_N_LOCKED_CLUSTER)
        self.assertEqual(STANDING_N_LOCKED_CLUSTER, 10)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING, 24)
        self.assertEqual(
            self.n_distinct,
            STANDING_N_DISTINCT_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(STANDING_N_DISTINCT_REMAINING_PREVIOUS_STEMS, 24)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(
            self.n_locked + self.n_remaining + self.n_no_backward,
            self.n_leftover,
        )
        self.assertEqual(HYPOTHESIS_N_REMAINING, 24)
        self.assertEqual(HYPOTHESIS_N_DISTINCT, 24)
        self.assertEqual(self.n_remaining, self.n_distinct)
        self.assertFalse(remaining_previous_stem_is_shared(self.remaining_previous_stems))
        self.assertTrue(
            i_leftover_076_071_remaining_previous_stems_all_distinct(
                self.n_remaining,
                self.n_distinct,
                self.n_no_backward,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_071_REMAINING_PREVIOUS_STEMS_ALL_DISTINCT,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_PREVIOUS_STEMS_ALL_DISTINCT)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_076_071_remaining_previous_stems_all_distinct",
        )
        self.assertEqual(self.previous_4grams, CYCLE172_PREVIOUS_4GRAMS)
        if self.n_remaining != 24:
            self.fail("measured N_remaining drifted from 24")
        if self.n_distinct != 24:
            self.fail("measured N_distinct_remaining_previous_stems drifted from 24")
        if remaining_previous_stem_is_shared(self.remaining_previous_stems):
            self.fail("a remaining leftover previous stem is shared")
        self.assertTrue(STANDING_SHARE_ONE_PREVIOUS_STEM_NOT_LOCKED)
        self.assertFalse(STANDING_SAME_AS_CYCLE191)
        self.assertFalse(STANDING_SAME_AS_CYCLE194)
        self.assertFalse(STANDING_SAME_AS_CYCLE197)
        self.assertFalse(STANDING_SAME_AS_CYCLE200)
        self.assertFalse(STANDING_SAME_AS_CYCLE190)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remaining_sites_previous_4grams_and_disjoint_from_locked_clusters(self):
        """Twenty-four remaining leftover sites; previous stems unique; disjoint from locked 3+3+2+2."""
        self.assertEqual(self.locked_sites, STANDING_LOCKED_CLUSTER_SITES)
        self.assertEqual(self.remaining_sites, STANDING_REMAINING_SITES)
        self.assertEqual(
            self.remaining_previous_4grams,
            STANDING_REMAINING_PREVIOUS_4GRAMS,
        )
        self.assertEqual(
            self.remaining_previous_stems,
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        expected = (
            ((SIDE_IA, "Ia1", 86), ("027", "200", "076", "071"), "200"),
            ((SIDE_IA, "Ia2", 43), ("430", "071", "076", "071"), "071"),
            ((SIDE_IA, "Ia2", 104), ("005", "633", "076", "071"), "633"),
            ((SIDE_IA, "Ia2", 169), ("147", "076", "076", "071"), "076"),
            ((SIDE_IA, "Ia3", 13), ("205", "225", "076", "071"), "225"),
            ((SIDE_IA, "Ia3", 85), ("076", "385", "076", "071"), "385"),
            ((SIDE_IA, "Ia3", 110), ("530", "298", "076", "071"), "298"),
            ((SIDE_IA, "Ia3", 133), ("070", "205", "076", "071"), "205"),
            ((SIDE_IA, "Ia5", 79), ("999", "406", "076", "071"), "406"),
            ((SIDE_IA, "Ia5", 134), ("071", "072", "076", "071"), "072"),
            ((SIDE_IA, "Ia7", 32), ("076", "999", "076", "071"), "999"),
            ((SIDE_IA, "Ia7", 48), ("400", "222", "076", "071"), "222"),
            ((SIDE_IA, "Ia8", 27), ("002", "514", "076", "071"), "514"),
            ((SIDE_IA, "Ia12", 19), ("490", "440", "076", "071"), "440"),
            ((SIDE_IA, "Ia12", 59), ("050", "606", "076", "071"), "606"),
            ((SIDE_IA, "Ia12", 63), ("061", "290", "076", "071"), "290"),
            ((SIDE_IA, "Ia13", 44), ("002", "009", "076", "071"), "009"),
            ((SIDE_IA, "Ia13", 54), ("999", "007", "076", "071"), "007"),
            ((SIDE_IA, "Ia13", 92), ("073", "006", "076", "071"), "006"),
            ((SIDE_IA, "Ia13", 101), ("042", "730", "076", "071"), "730"),
            ((SIDE_IA, "Ia13", 114), ("084", "600", "076", "071"), "600"),
            ((SIDE_IA, "Ia13", 149), ("006", "048", "076", "071"), "048"),
            ((SIDE_IA, "Ia14", 81), ("076", "011", "076", "071"), "011"),
            ((SIDE_IA, "Ia14", 166), ("006", "000", "076", "071"), "000"),
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
            self.assertEqual(stems[index - 1], want_stem)
            self.assertEqual(stems[index - 1], stem)
            self.assertNotIn(stem, LOCKED_PREVIOUS_STEMS)
            self.assertEqual(site_previous_stem(stems, index, GRAM2), stem)
            self.assertEqual(
                site_backward_3gram(stems, index, GRAM2),
                (stem, "076", "071"),
            )
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev4)
            self.assertEqual(prev4, want_prev4)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], (stem, "076", "071"))
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, CYCLE191_MATCHING_SITES)
            self.assertNotIn(site, CYCLE194_MATCHING_SITES)
            self.assertNotIn(site, CYCLE197_MATCHING_SITES)
            self.assertNotIn(site, CYCLE200_MATCHING_SITES)
        self.assertEqual(len(set(STANDING_REMAINING_PREVIOUS_STEMS)), 24)
        self.assertEqual(len(set(STANDING_REMAINING_PREVIOUS_4GRAMS)), 24)
        locked_clusters = (
            (
                CYCLE191_MATCHING_SITES,
                CYCLE191_MATCHING_PREVIOUS_4GRAMS,
                CYCLE191_GRAM3_BACKWARD,
            ),
            (
                CYCLE194_MATCHING_SITES,
                CYCLE194_MATCHING_PREVIOUS_4GRAMS,
                CYCLE194_GRAM3_BACKWARD,
            ),
            (
                CYCLE197_MATCHING_SITES,
                CYCLE197_MATCHING_PREVIOUS_4GRAMS,
                CYCLE197_GRAM3_BACKWARD,
            ),
            (
                CYCLE200_MATCHING_SITES,
                CYCLE200_MATCHING_PREVIOUS_4GRAMS,
                CYCLE200_GRAM3_BACKWARD,
            ),
        )
        locked_set = set()
        for prior_sites, prior_prev, prior_gram3 in locked_clusters:
            self.assertIn(prior_gram3[0], LOCKED_PREVIOUS_STEMS)
            for site, prev4 in zip(prior_sites, prior_prev, strict=True):
                self.assertIn(site, self.locked_sites)
                self.assertNotIn(site, self.remaining_sites)
                locked_set.add(site)
                stems = line_stems_for_site(self.i_sides, site)
                index = site[2]
                self.assertEqual(site_backward_3gram(stems, index, GRAM2), prior_gram3)
                self.assertEqual(site_previous_4gram(stems, index, GRAM2), prev4)
        self.assertEqual(len(locked_set), 10)
        self.assertEqual(locked_set, set(STANDING_LOCKED_CLUSTER_SITES))
        self.assertEqual(set(self.remaining_sites) & locked_set, set())
        self.assertEqual(
            set(self.leftover_sites),
            set(self.remaining_sites) | locked_set,
        )
        self.assertEqual(
            set(STANDING_REMAINING_SITES) & set(CYCLE191_MATCHING_SITES),
            set(),
        )
        self.assertEqual(
            set(STANDING_REMAINING_SITES) & set(CYCLE194_MATCHING_SITES),
            set(),
        )
        self.assertEqual(
            set(STANDING_REMAINING_SITES) & set(CYCLE197_MATCHING_SITES),
            set(),
        )
        self.assertEqual(
            set(STANDING_REMAINING_SITES) & set(CYCLE200_MATCHING_SITES),
            set(),
        )
        self.assertIn(CYCLE191_NEAR_MISS_700_604_SITE, self.locked_sites)
        self.assertNotIn(CYCLE191_NEAR_MISS_700_604_SITE, self.remaining_sites)
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, self.remaining_sites)
            self.assertNotIn(site, self.leftover_sites)
            inside_stems = line_stems_for_site(self.i_sides, site)
            inside_index = site[2]
            inside_prev = site_previous_stem(inside_stems, inside_index, GRAM2)
            if inside_prev is not None:
                self.assertNotIn(site, self.remaining_sites)
        measured_local = leftover_local_4grams(self.i_sides, self.leftover_sites)
        for (site, prev4, _nxt), back in zip(
            measured_local,
            self.backwards,
            strict=True,
        ):
            self.assertIsNotNone(prev4)
            self.assertEqual(prev4[1:], back)
            self.assertEqual(prev4[2:], GRAM2)
            if site in STANDING_REMAINING_SITES:
                self.assertNotIn(back[0], LOCKED_PREVIOUS_STEMS)
            else:
                self.assertIn(back[0], LOCKED_PREVIOUS_STEMS)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_200_197_194_191_190_172_171_scoreboards_still_compute(self):
        """Cycle 200 leftover-2, 197 leftover-2, 194 leftover-3, 191 leftover-3, 190 N_distinct=28, 172 leftover-34 stay."""
        prior_200 = TestMamariILeftover076071Previous099Scoreboard()
        prior_200.setUp()
        prior_200.test_counts_2_of_34_and_hypothesis_n_2_holds()
        prior_200.test_survey_matches_computed_lock()
        self.assertEqual(prior_200.n_with, 2)
        self.assertEqual(prior_200.n_leftover, 34)
        self.assertEqual(CYCLE200_N_WITH, 2)
        self.assertEqual(prior_200.with_sites, CYCLE200_MATCHING_SITES)
        self.assertEqual(
            set(self.remaining_sites) & set(prior_200.with_sites),
            set(),
        )
        prior_197 = TestMamariILeftover076071Previous604Scoreboard()
        prior_197.setUp()
        prior_197.test_counts_2_of_34_and_hypothesis_n_2_holds()
        prior_197.test_survey_matches_computed_lock()
        self.assertEqual(prior_197.n_with, 2)
        self.assertEqual(prior_197.n_leftover, 34)
        self.assertEqual(CYCLE197_N_WITH, 2)
        self.assertEqual(prior_197.with_sites, CYCLE197_MATCHING_SITES)
        self.assertEqual(
            set(self.remaining_sites) & set(prior_197.with_sites),
            set(),
        )
        prior_194 = TestMamariILeftover076071Previous090Scoreboard()
        prior_194.setUp()
        prior_194.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_194.test_survey_matches_computed_lock()
        self.assertEqual(prior_194.n_with, 3)
        self.assertEqual(prior_194.n_leftover, 34)
        self.assertEqual(CYCLE194_N_WITH, 3)
        self.assertEqual(prior_194.with_sites, CYCLE194_MATCHING_SITES)
        self.assertEqual(
            set(self.remaining_sites) & set(prior_194.with_sites),
            set(),
        )
        prior_191 = TestMamariILeftover076071Previous700Scoreboard()
        prior_191.setUp()
        prior_191.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_191.test_survey_matches_computed_lock()
        self.assertEqual(prior_191.n_with, 3)
        self.assertEqual(prior_191.n_leftover, 34)
        self.assertEqual(CYCLE191_N_WITH, 3)
        self.assertEqual(prior_191.with_sites, CYCLE191_MATCHING_SITES)
        self.assertEqual(
            set(self.remaining_sites) & set(prior_191.with_sites),
            set(),
        )
        prior_190 = TestMamariILeftover076071PreviousStemScoreboard()
        prior_190.setUp()
        prior_190.test_counts_28_distinct_previous_stems_and_claim_loses()
        prior_190.test_survey_matches_computed_lock()
        self.assertEqual(prior_190.n_distinct, 28)
        self.assertEqual(prior_190.n_leftover, 34)
        self.assertEqual(CYCLE190_N_DISTINCT, 28)
        prior_172 = TestMamariI2gram076071InsideFamilyScoreboard()
        prior_172.setUp()
        prior_172.test_forty_three_sites_split_9_inside_34_leftover_and_claim_loses()
        prior_172.test_survey_matches_computed_lock()
        self.assertEqual(prior_172.n_leftover, 34)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(len(prior_171.i_sites), 43)
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-203 leftover remaining previous-stem lock."""
        lock = self.survey["i_leftover_076_071_remaining_previous_stems_distinct"]
        self.assertEqual(lock["cycle"], 203)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n_remaining"], HYPOTHESIS_N_REMAINING)
        self.assertEqual(lock["hypothesis_n_remaining"], 24)
        self.assertEqual(lock["hypothesis_n_distinct"], HYPOTHESIS_N_DISTINCT)
        self.assertEqual(lock["hypothesis_n_distinct"], 24)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(
            tuple(lock["locked_previous_stems"]),
            STANDING_LOCKED_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 34)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE172_PREVIOUS_4GRAMS],
            lock["leftover_previous_4grams"],
        )
        self.assertEqual(
            leftover_local_4grams(self.i_sides, self.leftover_sites),
            tuple(
                (site, prev, nxt)
                for site, prev, nxt in leftover_local_4grams(
                    self.i_sides,
                    STANDING_LEFTOVER_SITES,
                )
            ),
        )
        self.assertEqual(lock["N_locked_cluster"], STANDING_N_LOCKED_CLUSTER)
        self.assertEqual(lock["N_locked_cluster"], 10)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 24)
        self.assertEqual(
            lock["N_distinct_remaining_previous_stems"],
            STANDING_N_DISTINCT_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_distinct_remaining_previous_stems"], 24)
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
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["cycle191_700_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE191_MATCHING_SITES],
            lock["cycle191_matching_sites"],
        )
        self.assertEqual(lock["cycle191_N_with_previous_700_076_071"], 3)
        self.assertTrue(lock["cycle194_090_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE194_MATCHING_SITES],
            lock["cycle194_matching_sites"],
        )
        self.assertEqual(lock["cycle194_N_with_previous_090_076_071"], 3)
        self.assertTrue(lock["cycle197_604_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE197_MATCHING_SITES],
            lock["cycle197_matching_sites"],
        )
        self.assertEqual(lock["cycle197_N_with_previous_604_076_071"], 2)
        self.assertTrue(lock["cycle200_099_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE200_MATCHING_SITES],
            lock["cycle200_matching_sites"],
        )
        self.assertEqual(lock["cycle200_N_with_previous_099_076_071"], 2)
        self.assertTrue(lock["remaining_sites_disjoint_from_locked_clusters"])
        self.assertTrue(lock["share_one_previous_stem_not_locked"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_071_remaining_previous_stems_all_distinct"])
        self.assertEqual(
            lock["i_leftover_076_071_remaining_previous_stems_all_distinct"],
            STANDING_I_LEFTOVER_076_071_REMAINING_PREVIOUS_STEMS_ALL_DISTINCT,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle191"])
        self.assertFalse(lock["same_as_cycle194"])
        self.assertFalse(lock["same_as_cycle197"])
        self.assertFalse(lock["same_as_cycle200"])
        self.assertFalse(lock["same_as_cycle190"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["other_leftover_n4_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle190_leftover_previous_4grams_remeasured"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_099_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_604_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_090_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_700_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_076_071_previous_099"]["cycle"], 200)
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_099"]["N_with_previous_099_076_071"],
            2,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_099"][
                "i_leftover_076_071_exactly_2_previous_099_076_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_604"]["cycle"], 197)
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_604"]["N_with_previous_604_076_071"],
            2,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_604"][
                "i_leftover_076_071_exactly_2_previous_604_076_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_090"]["cycle"], 194)
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_090"]["N_with_previous_090_076_071"],
            3,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_090"][
                "i_leftover_076_071_exactly_3_previous_090_076_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_700"]["cycle"], 191)
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_700"]["N_with_previous_700_076_071"],
            3,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_700"][
                "i_leftover_076_071_exactly_3_previous_700_076_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_stem"]["cycle"], 190)
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_stem"]["N_distinct_previous_stems"],
            28,
        )
        self.assertFalse(
            self.survey["i_leftover_076_071_previous_stem"][
                "i_leftover_076_071_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["cycle"], 172)
        self.assertFalse(
            self.survey["i_2gram_076_071_inside_family"][
                "i_2gram_076_071_all_inside_leftover_n4_family"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"]["i_leftover_n4_exactly_4_contain_076_071"]
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


class TestMamariILeftover076071RemainingPreviousStemsDistinctImageSnapshot(
    unittest.TestCase
):
    """Cycle 203 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
