"""I's cycle-172 leftover 2-gram remaining next-stem distinct lock.

Cycle 188 text-search lock. Uses already-vendored A–V and the
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

For each leftover site, record the next token after 076 071
(forward 3-gram 076 071 X and next 4-gram 076 071 X Y when
they exist). End-of-line is no-forward. Partition leftover
sites into already-locked clusters (next stem in {076, 600,
090, 700, 061}) vs remaining. Cycle 173 leftover-5, cycle
176 leftover-4, cycle 179 leftover-3, cycle 182 leftover-3,
and cycle 185 leftover-2 are the locked clusters (5+4+3+3+2
= 17). The remaining 17 are the leftover sites whose next
stem is not in that set. Cycle 173 recorded leftover next
4-grams; this cycle re-measures them from fixtures and does
not treat those as assumed. The 9 inside-family sites do
not count as leftover. 071 999 and 076 076 do not count as
this 2-gram.

Claim that can lose:
i_leftover_076_071_remaining_next_stems_all_distinct. True
only if N_remaining=17 and N_distinct_remaining_next_stems=17
and N_no_forward=0. Measured: N_leftover=34, N_locked_cluster=17,
N_remaining=17, N_distinct_remaining_next_stems=17,
N_no_forward=0. The claim is true. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    STANDING_CONTAINERS,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_NEXT_4GRAMS as CYCLE172_NEXT_4GRAMS,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE172_N_LEFTOVER,
    leftover_local_4grams,
    TestMamariI2gram076071InsideFamilyScoreboard,
)
from tests.test_mamari_i_076_071_061_forward_4grams_i_only_scoreboard import (
    TestMamariI076071061Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_3gram_076_071_061_i_only_scoreboard import (
    TestMamariI3gram076071061IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_inside_family_scoreboard import (
    leftover_sites_from_membership,
    membership_for_sites,
)
from tests.test_mamari_i_leftover_076_071_forward_061_scoreboard import (
    GRAM3_FORWARD as CYCLE185_GRAM3_FORWARD,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE185_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE185_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_061 as CYCLE185_N_WITH,
    TestMamariILeftover076071Forward061Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    GRAM3_FORWARD as CYCLE173_GRAM3_FORWARD,
    STANDING_INSIDE_FORWARD_076_NEXT_4GRAM,
    STANDING_INSIDE_FORWARD_076_SITE,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE173_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE173_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_076 as CYCLE173_N_WITH,
    leftover_forward_3grams,
    leftover_next_4grams,
    leftover_sites_without_forward,
    matching_leftover_local_4gram_rows,
    site_forward_3gram,
    site_next_4gram,
    TestMamariILeftover076071Forward076Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_090_scoreboard import (
    GRAM3_FORWARD as CYCLE179_GRAM3_FORWARD,
    STANDING_INSIDE_FORWARD_090_NEXT_4GRAM,
    STANDING_INSIDE_FORWARD_090_SITES,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE179_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE179_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_090 as CYCLE179_N_WITH,
    TestMamariILeftover076071Forward090Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_600_scoreboard import (
    GRAM3_FORWARD as CYCLE176_GRAM3_FORWARD,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE176_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE176_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_600 as CYCLE176_N_WITH,
    TestMamariILeftover076071Forward600Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_700_scoreboard import (
    GRAM3_FORWARD as CYCLE182_GRAM3_FORWARD,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE182_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE182_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_700 as CYCLE182_N_WITH,
    TestMamariILeftover076071Forward700Scoreboard,
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

HYPOTHESIS_N_REMAINING = 17
HYPOTHESIS_N_DISTINCT = 17
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
LOCKED_NEXT_STEMS = frozenset({"076", "600", "090", "700", "061"})
STANDING_LOCKED_NEXT_STEMS = ("076", "600", "090", "700", "061")
STANDING_N_LEFTOVER = 34
STANDING_N_LOCKED_CLUSTER = 17
STANDING_N_REMAINING = 17
STANDING_N_DISTINCT_REMAINING_NEXT_STEMS = 17
STANDING_N_NO_FORWARD = 0
STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS = 34
STANDING_NO_FORWARD_SITES = ()
STANDING_LOCKED_CLUSTER_SITES = (
    (SIDE_IA, "Ia1", 86),
    (SIDE_IA, "Ia1", 163),
    (SIDE_IA, "Ia2", 43),
    (SIDE_IA, "Ia2", 104),
    (SIDE_IA, "Ia2", 169),
    (SIDE_IA, "Ia3", 85),
    (SIDE_IA, "Ia3", 147),
    (SIDE_IA, "Ia9", 10),
    (SIDE_IA, "Ia12", 19),
    (SIDE_IA, "Ia12", 59),
    (SIDE_IA, "Ia13", 54),
    (SIDE_IA, "Ia13", 92),
    (SIDE_IA, "Ia13", 149),
    (SIDE_IA, "Ia13", 153),
    (SIDE_IA, "Ia14", 81),
    (SIDE_IA, "Ia14", 106),
    (SIDE_IA, "Ia14", 166),
)
STANDING_REMAINING_SITES = (
    (SIDE_IA, "Ia2", 51),
    (SIDE_IA, "Ia3", 13),
    (SIDE_IA, "Ia3", 110),
    (SIDE_IA, "Ia3", 133),
    (SIDE_IA, "Ia5", 67),
    (SIDE_IA, "Ia5", 79),
    (SIDE_IA, "Ia5", 134),
    (SIDE_IA, "Ia6", 117),
    (SIDE_IA, "Ia7", 32),
    (SIDE_IA, "Ia7", 48),
    (SIDE_IA, "Ia8", 27),
    (SIDE_IA, "Ia12", 6),
    (SIDE_IA, "Ia12", 63),
    (SIDE_IA, "Ia13", 44),
    (SIDE_IA, "Ia13", 101),
    (SIDE_IA, "Ia13", 114),
    (SIDE_IA, "Ia13", 128),
)
STANDING_REMAINING_NEXT_4GRAMS = (
    ("076", "071", "010", "660"),
    ("076", "071", "274", "604"),
    ("076", "071", "018", "049"),
    ("076", "071", "202", "604"),
    ("076", "071", "004", "004"),
    ("076", "071", "078", "999"),
    ("076", "071", "496", "999"),
    ("076", "071", "632", "670"),
    ("076", "071", "183", "430"),
    ("076", "071", "071", "076"),
    ("076", "071", "070", "076"),
    ("076", "071", "513", "001"),
    ("076", "071", "607", "208"),
    ("076", "071", "002", "536"),
    ("076", "071", "729", "073"),
    ("076", "071", "021", "090"),
    ("076", "071", "670", "009"),
)
STANDING_REMAINING_NEXT_STEMS = (
    "010",
    "274",
    "018",
    "202",
    "004",
    "078",
    "496",
    "632",
    "183",
    "071",
    "070",
    "513",
    "607",
    "002",
    "729",
    "021",
    "670",
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_071_remaining_next_stems_all_distinct"
STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT = True
STANDING_RESULT = "i_leftover_076_071_remaining_next_stems_distinct"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE173 = False
STANDING_SAME_AS_CYCLE176 = False
STANDING_SAME_AS_CYCLE179 = False
STANDING_SAME_AS_CYCLE182 = False
STANDING_SAME_AS_CYCLE185 = False
STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED = True
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_CYCLE173_076_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE176_600_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE179_090_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE182_700_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE185_061_CLUSTER_DOES_NOT_COUNT = True


def next_stem_of_forward(fwd: tuple[str, ...] | None) -> str | None:
    """Next stem X from forward 3-gram 076 071 X; None if no-forward."""
    if fwd is None:
        return None
    return fwd[2]


def leftover_locked_cluster_sites(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
    locked: frozenset[str] = LOCKED_NEXT_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose next stem is in the locked cluster set."""
    return tuple(
        site
        for site, fwd in zip(sites, forwards, strict=True)
        if next_stem_of_forward(fwd) in locked
    )


def leftover_remaining_sites(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
    locked: frozenset[str] = LOCKED_NEXT_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose next stem exists and is not a locked cluster."""
    return tuple(
        site
        for site, fwd in zip(sites, forwards, strict=True)
        if (stem := next_stem_of_forward(fwd)) is not None and stem not in locked
    )


def leftover_remaining_next_stems(
    forwards: tuple[tuple[str, ...] | None, ...],
    locked: frozenset[str] = LOCKED_NEXT_STEMS,
) -> tuple[str, ...]:
    """Next stems of leftover sites outside the locked clusters."""
    return tuple(
        stem
        for fwd in forwards
        if (stem := next_stem_of_forward(fwd)) is not None and stem not in locked
    )


def remaining_next_stem_is_shared(stems: tuple[str, ...]) -> bool:
    """True iff at least two remaining leftover sites share a next stem."""
    return len(stems) != len(set(stems))


def i_leftover_076_071_remaining_next_stems_all_distinct(
    n_remaining: int,
    n_distinct_remaining_next_stems: int,
    n_no_forward: int,
    expected_remaining: int = HYPOTHESIS_N_REMAINING,
    expected_distinct: int = HYPOTHESIS_N_DISTINCT,
) -> bool:
    """True iff N_remaining=17, N_distinct=17, and N_no_forward=0."""
    return (
        n_remaining == expected_remaining
        and n_distinct_remaining_next_stems == expected_distinct
        and n_no_forward == 0
    )


class TestILeftover076071RemainingNextStemsDistinctHelpers(unittest.TestCase):
    """Helpers on cycle-172 leftover 076 071 remaining stems. No CV, no LLM."""

    def test_forward_requires_next_stem_after_2gram(self):
        """A next stem is a 3-gram; end-of-line is no-forward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(STANDING_LOCKED_NEXT_STEMS, ("076", "600", "090", "700", "061"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        remaining_next = ["147", "076", "076", "071", "010", "660"]
        self.assertEqual(
            site_forward_3gram(remaining_next, 2, GRAM2),
            ("076", "071", "010"),
        )
        self.assertEqual(
            site_next_4gram(remaining_next, 2, GRAM2),
            ("076", "071", "010", "660"),
        )
        self.assertEqual(
            next_stem_of_forward(site_forward_3gram(remaining_next, 2, GRAM2)),
            "010",
        )
        self.assertNotIn("010", LOCKED_NEXT_STEMS)
        cycle185_next = ["600", "604", "076", "071", "061", "011"]
        self.assertEqual(
            site_forward_3gram(cycle185_next, 2, GRAM2),
            CYCLE185_GRAM3_FORWARD,
        )
        self.assertIn(
            next_stem_of_forward(site_forward_3gram(cycle185_next, 2, GRAM2)),
            LOCKED_NEXT_STEMS,
        )
        cycle182_next = ["090", "700", "076", "071", "700", "076"]
        self.assertEqual(
            site_forward_3gram(cycle182_next, 2, GRAM2),
            CYCLE182_GRAM3_FORWARD,
        )
        cycle179_next = ["027", "200", "076", "071", "090", "606"]
        self.assertEqual(
            site_forward_3gram(cycle179_next, 2, GRAM2),
            CYCLE179_GRAM3_FORWARD,
        )
        cycle176_next = ["005", "633", "076", "071", "600", "090"]
        self.assertEqual(
            site_forward_3gram(cycle176_next, 2, GRAM2),
            CYCLE176_GRAM3_FORWARD,
        )
        cycle173_next = ["430", "071", "076", "071", "076", "021"]
        self.assertEqual(
            site_forward_3gram(cycle173_next, 2, GRAM2),
            CYCLE173_GRAM3_FORWARD,
        )
        end_of_line = ["027", "200", "076", "071"]
        self.assertIsNone(site_forward_3gram(end_of_line, 2, GRAM2))
        self.assertIsNone(site_next_4gram(end_of_line, 2, GRAM2))
        self.assertIsNone(next_stem_of_forward(None))
        mismatch = ["076", "070", "010", "660"]
        self.assertIsNone(site_forward_3gram(mismatch, 0, GRAM2))
        self.assertEqual(provider.get_call_history(), [])

    def test_all_distinct_can_fail(self):
        """Boolean is True only when N_remaining=17, N_distinct=17, N_no_forward=0."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_076_071_remaining_next_stems_all_distinct(17, 17, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_next_stems_all_distinct(16, 16, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_next_stems_all_distinct(18, 18, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_next_stems_all_distinct(17, 16, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_next_stems_all_distinct(17, 17, 1)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_next_stems_all_distinct(34, 34, 0)
        )
        self.assertFalse(
            i_leftover_076_071_remaining_next_stems_all_distinct(0, 0, 0)
        )
        planted_stems = STANDING_REMAINING_NEXT_STEMS + ("010",)
        self.assertTrue(remaining_next_stem_is_shared(planted_stems))
        self.assertFalse(remaining_next_stem_is_shared(STANDING_REMAINING_NEXT_STEMS))
        self.assertFalse(
            i_leftover_076_071_remaining_next_stems_all_distinct(
                len(planted_stems),
                len(set(planted_stems)),
                0,
            )
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_remaining_next_stems_all_distinct")
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT,
            HYPOTHESIS_N_REMAINING == STANDING_N_REMAINING
            and HYPOTHESIS_N_DISTINCT == STANDING_N_DISTINCT_REMAINING_NEXT_STEMS
            and STANDING_N_NO_FORWARD == 0,
        )
        self.assertEqual(
            STANDING_N_LOCKED_CLUSTER + STANDING_N_REMAINING + STANDING_N_NO_FORWARD,
            34,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_locked_clusters_inside_family_and_near_misses_do_not_count(self):
        """Locked 076/600/090/700/061 clusters, inside family, 071 999, and 076 076 are not remaining."""
        provider = MockProvider()
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LOCKED_CLUSTER_SITES)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertIn(STANDING_INSIDE_FORWARD_076_SITE, STANDING_INSIDE_SITES)
        self.assertNotIn(STANDING_INSIDE_FORWARD_076_SITE, STANDING_REMAINING_SITES)
        self.assertEqual(
            STANDING_INSIDE_FORWARD_076_NEXT_4GRAM[:3],
            CYCLE173_GRAM3_FORWARD,
        )
        for site in STANDING_INSIDE_FORWARD_090_SITES:
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        self.assertEqual(STANDING_INSIDE_FORWARD_090_NEXT_4GRAM, ("076", "071", "090", "999"))
        locked_clusters = (
            (CYCLE173_MATCHING_SITES, CYCLE173_N_WITH, CYCLE173_GRAM3_FORWARD, "076"),
            (CYCLE176_MATCHING_SITES, CYCLE176_N_WITH, CYCLE176_GRAM3_FORWARD, "600"),
            (CYCLE179_MATCHING_SITES, CYCLE179_N_WITH, CYCLE179_GRAM3_FORWARD, "090"),
            (CYCLE182_MATCHING_SITES, CYCLE182_N_WITH, CYCLE182_GRAM3_FORWARD, "700"),
            (CYCLE185_MATCHING_SITES, CYCLE185_N_WITH, CYCLE185_GRAM3_FORWARD, "061"),
        )
        for prior_sites, n_with, gram3, stem in locked_clusters:
            self.assertEqual(len(prior_sites), n_with)
            self.assertEqual(gram3[2], stem)
            self.assertIn(stem, LOCKED_NEXT_STEMS)
            for site in prior_sites:
                self.assertIn(site, STANDING_LEFTOVER_SITES)
                self.assertIn(site, STANDING_LOCKED_CLUSTER_SITES)
                self.assertNotIn(site, STANDING_REMAINING_SITES)
        self.assertTrue(STANDING_CYCLE173_076_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE176_600_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE179_090_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE182_700_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE185_061_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(CYCLE173_N_WITH, 5)
        self.assertEqual(CYCLE176_N_WITH, 4)
        self.assertEqual(CYCLE179_N_WITH, 3)
        self.assertEqual(CYCLE182_N_WITH, 3)
        self.assertEqual(CYCLE185_N_WITH, 2)
        locked_set = (
            set(CYCLE173_MATCHING_SITES)
            | set(CYCLE176_MATCHING_SITES)
            | set(CYCLE179_MATCHING_SITES)
            | set(CYCLE182_MATCHING_SITES)
            | set(CYCLE185_MATCHING_SITES)
        )
        self.assertEqual(len(locked_set), 5 + 4 + 3 + 3 + 2)
        self.assertEqual(locked_set, set(STANDING_LOCKED_CLUSTER_SITES))
        self.assertEqual(len(set(STANDING_REMAINING_SITES) & locked_set), 0)
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED)
        self.assertEqual(STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS, 34)
        self.assertEqual(len(set(CYCLE172_NEXT_4GRAMS)), 34)
        self.assertFalse(STANDING_SAME_AS_CYCLE173)
        self.assertFalse(STANDING_SAME_AS_CYCLE176)
        self.assertFalse(STANDING_SAME_AS_CYCLE179)
        self.assertFalse(STANDING_SAME_AS_CYCLE182)
        self.assertFalse(STANDING_SAME_AS_CYCLE185)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076071RemainingNextStemsDistinctScoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 071 remaining next-stem lock. Mock only."""

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
        self.forwards = leftover_forward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.next_4grams = leftover_next_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.locked_sites = leftover_locked_cluster_sites(
            self.leftover_sites,
            self.forwards,
        )
        self.remaining_sites = leftover_remaining_sites(
            self.leftover_sites,
            self.forwards,
        )
        self.no_forward = leftover_sites_without_forward(
            self.leftover_sites,
            self.forwards,
        )
        self.remaining_next_4grams = leftover_next_4grams(
            self.i_sides,
            self.remaining_sites,
            GRAM2,
        )
        self.remaining_next_stems = leftover_remaining_next_stems(self.forwards)
        self.n_leftover = len(self.leftover_sites)
        self.n_locked = len(self.locked_sites)
        self.n_remaining = len(self.remaining_sites)
        self.n_distinct = len(set(self.remaining_next_stems))
        self.n_no_forward = len(self.no_forward)
        self.claim_holds = i_leftover_076_071_remaining_next_stems_all_distinct(
            self.n_remaining,
            self.n_distinct,
            self.n_no_forward,
        )

    def test_tokens_and_sites_are_cycle_172_leftover_not_retuned(self):
        """2-gram and leftover 34 stay the cycle-172/171/170 locks."""
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(STANDING_LOCKED_NEXT_STEMS, ("076", "600", "090", "700", "061"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover, self.leftover_sites)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE172_N_LEFTOVER)
        self.assertEqual(CYCLE172_N_LEFTOVER, 34)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 43)
        self.assertEqual(len(STANDING_INSIDE_SITES), STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 9)
        self.assertEqual(STANDING_N_INSIDE + STANDING_N_LEFTOVER, STANDING_N_I)
        prior_187 = self.survey["i_076_071_061_forward_4grams_i_only"]
        self.assertEqual(prior_187["cycle"], 187)
        self.assertTrue(prior_187["i_076_071_061_forward_4grams_i_only"])
        prior_186 = self.survey["i_3gram_076_071_061_i_only"]
        self.assertEqual(prior_186["cycle"], 186)
        self.assertTrue(prior_186["i_3gram_076_071_061_i_only"])
        self.assertEqual(prior_186["N_I"], 2)
        self.assertEqual(prior_186["N_off_I"], 0)
        prior_185 = self.survey["i_leftover_076_071_forward_061"]
        self.assertEqual(prior_185["cycle"], 185)
        self.assertEqual(tuple(prior_185["tokens2"]), GRAM2)
        self.assertEqual(tuple(prior_185["forward_3gram"]), CYCLE185_GRAM3_FORWARD)
        self.assertEqual(prior_185["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_185["N_with_forward_076_071_061"], 2)
        self.assertTrue(prior_185["i_leftover_076_071_exactly_2_forward_076_071_061"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_185["matching_leftover_sites"]),
            CYCLE185_MATCHING_SITES,
        )
        prior_182 = self.survey["i_leftover_076_071_forward_700"]
        self.assertEqual(prior_182["cycle"], 182)
        self.assertEqual(prior_182["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_182["N_with_forward_076_071_700"], 3)
        self.assertTrue(prior_182["i_leftover_076_071_exactly_3_forward_076_071_700"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_182["matching_leftover_sites"]),
            CYCLE182_MATCHING_SITES,
        )
        prior_179 = self.survey["i_leftover_076_071_forward_090"]
        self.assertEqual(prior_179["cycle"], 179)
        self.assertEqual(prior_179["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_179["N_with_forward_076_071_090"], 3)
        self.assertTrue(prior_179["i_leftover_076_071_exactly_3_forward_076_071_090"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_179["matching_leftover_sites"]),
            CYCLE179_MATCHING_SITES,
        )
        prior_176 = self.survey["i_leftover_076_071_forward_600"]
        self.assertEqual(prior_176["cycle"], 176)
        self.assertEqual(prior_176["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_176["N_with_forward_076_071_600"], 4)
        self.assertTrue(prior_176["i_leftover_076_071_exactly_4_forward_076_071_600"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_176["matching_leftover_sites"]),
            CYCLE176_MATCHING_SITES,
        )
        prior_173 = self.survey["i_leftover_076_071_forward_076"]
        self.assertEqual(prior_173["cycle"], 173)
        self.assertEqual(prior_173["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_173["N_with_forward_076_071_076"], 5)
        self.assertTrue(prior_173["i_leftover_076_071_exactly_5_forward_076_071_076"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_173["matching_leftover_sites"]),
            CYCLE173_MATCHING_SITES,
        )
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
            [list(gram) for gram in CYCLE172_NEXT_4GRAMS],
            prior_172["leftover_next_4grams"],
        )
        self.assertFalse(prior_172["i_2gram_076_071_all_inside_leftover_n4_family"])
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        prior_170 = self.survey["i_leftover_n4_076_071"]
        self.assertEqual(prior_170["cycle"], 170)
        self.assertEqual(prior_170["N_with_076_071"], 4)
        self.assertTrue(prior_170["i_leftover_n4_exactly_4_contain_076_071"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED)
        self.assertTrue(STANDING_CYCLE173_076_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE176_600_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE179_090_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE182_700_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE185_061_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_17_of_34_remaining_all_distinct_and_claim_holds(self):
        """N_leftover=34, N_locked=17, N_remaining=17, N_distinct=17. Claim holds."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 34)
        self.assertEqual(self.n_locked, STANDING_N_LOCKED_CLUSTER)
        self.assertEqual(STANDING_N_LOCKED_CLUSTER, 17)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING, 17)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_REMAINING_NEXT_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING_NEXT_STEMS, 17)
        self.assertEqual(self.n_no_forward, STANDING_N_NO_FORWARD)
        self.assertEqual(STANDING_N_NO_FORWARD, 0)
        self.assertEqual(self.no_forward, STANDING_NO_FORWARD_SITES)
        self.assertEqual(
            self.n_locked + self.n_remaining + self.n_no_forward,
            self.n_leftover,
        )
        self.assertEqual(HYPOTHESIS_N_REMAINING, 17)
        self.assertEqual(HYPOTHESIS_N_DISTINCT, 17)
        self.assertEqual(self.n_remaining, self.n_distinct)
        self.assertFalse(remaining_next_stem_is_shared(self.remaining_next_stems))
        self.assertTrue(
            i_leftover_076_071_remaining_next_stems_all_distinct(
                self.n_remaining,
                self.n_distinct,
                self.n_no_forward,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_remaining_next_stems_all_distinct")
        self.assertEqual(self.next_4grams, CYCLE172_NEXT_4GRAMS)
        self.assertEqual(len(set(self.next_4grams)), STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS, 34)
        self.assertTrue(STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED)
        self.assertFalse(STANDING_SAME_AS_CYCLE173)
        self.assertFalse(STANDING_SAME_AS_CYCLE176)
        self.assertFalse(STANDING_SAME_AS_CYCLE179)
        self.assertFalse(STANDING_SAME_AS_CYCLE182)
        self.assertFalse(STANDING_SAME_AS_CYCLE185)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remaining_sites_next_4grams_and_disjoint_from_locked_clusters(self):
        """Seventeen remaining leftover sites; next stems unique; disjoint from locked 5+4+3+3+2."""
        self.assertEqual(self.locked_sites, STANDING_LOCKED_CLUSTER_SITES)
        self.assertEqual(self.remaining_sites, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining_next_4grams, STANDING_REMAINING_NEXT_4GRAMS)
        self.assertEqual(self.remaining_next_stems, STANDING_REMAINING_NEXT_STEMS)
        expected = (
            ((SIDE_IA, "Ia2", 51), ("076", "071", "010", "660"), "010"),
            ((SIDE_IA, "Ia3", 13), ("076", "071", "274", "604"), "274"),
            ((SIDE_IA, "Ia3", 110), ("076", "071", "018", "049"), "018"),
            ((SIDE_IA, "Ia3", 133), ("076", "071", "202", "604"), "202"),
            ((SIDE_IA, "Ia5", 67), ("076", "071", "004", "004"), "004"),
            ((SIDE_IA, "Ia5", 79), ("076", "071", "078", "999"), "078"),
            ((SIDE_IA, "Ia5", 134), ("076", "071", "496", "999"), "496"),
            ((SIDE_IA, "Ia6", 117), ("076", "071", "632", "670"), "632"),
            ((SIDE_IA, "Ia7", 32), ("076", "071", "183", "430"), "183"),
            ((SIDE_IA, "Ia7", 48), ("076", "071", "071", "076"), "071"),
            ((SIDE_IA, "Ia8", 27), ("076", "071", "070", "076"), "070"),
            ((SIDE_IA, "Ia12", 6), ("076", "071", "513", "001"), "513"),
            ((SIDE_IA, "Ia12", 63), ("076", "071", "607", "208"), "607"),
            ((SIDE_IA, "Ia13", 44), ("076", "071", "002", "536"), "002"),
            ((SIDE_IA, "Ia13", 101), ("076", "071", "729", "073"), "729"),
            ((SIDE_IA, "Ia13", 114), ("076", "071", "021", "090"), "021"),
            ((SIDE_IA, "Ia13", 128), ("076", "071", "670", "009"), "670"),
        )
        for (site, nxt, stem), (want_site, want_nxt, want_stem) in zip(
            zip(
                self.remaining_sites,
                self.remaining_next_4grams,
                self.remaining_next_stems,
                strict=True,
            ),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(stems[index + STANDING_N2], want_stem)
            self.assertEqual(stems[index + STANDING_N2], stem)
            self.assertNotIn(stem, LOCKED_NEXT_STEMS)
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), ("076", "071", stem))
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], ("076", "071", stem))
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
        self.assertEqual(len(set(STANDING_REMAINING_NEXT_STEMS)), 17)
        self.assertEqual(len(set(STANDING_REMAINING_NEXT_4GRAMS)), 17)
        locked_clusters = (
            (CYCLE173_MATCHING_SITES, CYCLE173_MATCHING_NEXT_4GRAMS, CYCLE173_GRAM3_FORWARD),
            (CYCLE176_MATCHING_SITES, CYCLE176_MATCHING_NEXT_4GRAMS, CYCLE176_GRAM3_FORWARD),
            (CYCLE179_MATCHING_SITES, CYCLE179_MATCHING_NEXT_4GRAMS, CYCLE179_GRAM3_FORWARD),
            (CYCLE182_MATCHING_SITES, CYCLE182_MATCHING_NEXT_4GRAMS, CYCLE182_GRAM3_FORWARD),
            (CYCLE185_MATCHING_SITES, CYCLE185_MATCHING_NEXT_4GRAMS, CYCLE185_GRAM3_FORWARD),
        )
        locked_set = set()
        for prior_sites, prior_next, prior_gram3 in locked_clusters:
            self.assertIn(prior_gram3[2], LOCKED_NEXT_STEMS)
            for site, nxt in zip(prior_sites, prior_next, strict=True):
                self.assertIn(site, self.locked_sites)
                self.assertNotIn(site, self.remaining_sites)
                locked_set.add(site)
                stems = line_stems_for_site(self.i_sides, site)
                index = site[2]
                self.assertEqual(site_forward_3gram(stems, index, GRAM2), prior_gram3)
                self.assertEqual(site_next_4gram(stems, index, GRAM2), nxt)
        self.assertEqual(len(locked_set), 17)
        self.assertEqual(locked_set, set(STANDING_LOCKED_CLUSTER_SITES))
        self.assertEqual(set(self.remaining_sites) & locked_set, set())
        self.assertEqual(
            set(self.leftover_sites),
            set(self.remaining_sites) | locked_set,
        )
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, self.remaining_sites)
            self.assertNotIn(site, self.leftover_sites)
            inside_stems = line_stems_for_site(self.i_sides, site)
            inside_index = site[2]
            inside_fwd = site_forward_3gram(inside_stems, inside_index, GRAM2)
            if inside_fwd is not None:
                self.assertNotIn(site, self.remaining_sites)
        self.assertNotIn(STANDING_INSIDE_FORWARD_076_SITE, self.remaining_sites)
        self.assertNotIn(STANDING_INSIDE_FORWARD_076_SITE, self.leftover_sites)
        inside_stems = line_stems_for_site(
            self.i_sides,
            STANDING_INSIDE_FORWARD_076_SITE,
        )
        inside_index = STANDING_INSIDE_FORWARD_076_SITE[2]
        self.assertEqual(
            site_next_4gram(inside_stems, inside_index, GRAM2),
            STANDING_INSIDE_FORWARD_076_NEXT_4GRAM,
        )
        for site in STANDING_INSIDE_FORWARD_090_SITES:
            self.assertNotIn(site, self.remaining_sites)
            self.assertNotIn(site, self.leftover_sites)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_187_186_185_182_179_176_173_172_171_170_103_and_w_scoreboards_still_compute(self):
        """Cycle 187/186 I-only, 185 leftover-2, 182 leftover-3, 179 leftover-3, 176 leftover-4, 173 leftover-5, 172 leftover-34 stay."""
        prior_187 = TestMamariI076071061Forward4gramsIOnlyScoreboard()
        prior_187.setUp()
        prior_187.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_187.test_survey_matches_computed_lock()
        prior_186 = TestMamariI3gram076071061IOnlyScoreboard()
        prior_186.setUp()
        prior_186.test_3gram_is_zero_off_i_and_i_only()
        prior_186.test_survey_matches_computed_lock()
        prior_185 = TestMamariILeftover076071Forward061Scoreboard()
        prior_185.setUp()
        prior_185.test_counts_2_of_34_and_hypothesis_n_2_holds()
        prior_185.test_survey_matches_computed_lock()
        prior_182 = TestMamariILeftover076071Forward700Scoreboard()
        prior_182.setUp()
        prior_182.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_182.test_survey_matches_computed_lock()
        prior_179 = TestMamariILeftover076071Forward090Scoreboard()
        prior_179.setUp()
        prior_179.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_179.test_survey_matches_computed_lock()
        prior_176 = TestMamariILeftover076071Forward600Scoreboard()
        prior_176.setUp()
        prior_176.test_counts_4_of_34_and_hypothesis_n_4_holds()
        prior_176.test_survey_matches_computed_lock()
        prior_173 = TestMamariILeftover076071Forward076Scoreboard()
        prior_173.setUp()
        prior_173.test_counts_5_of_34_and_hypothesis_n_5_holds()
        prior_173.test_survey_matches_computed_lock()
        prior_172 = TestMamariI2gram076071InsideFamilyScoreboard()
        prior_172.setUp()
        prior_172.test_forty_three_sites_split_9_inside_34_leftover_and_claim_loses()
        prior_172.test_survey_matches_computed_lock()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-188 leftover remaining next-stem lock."""
        lock = self.survey["i_leftover_076_071_remaining_next_stems_distinct"]
        self.assertEqual(lock["cycle"], 188)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n_remaining"], HYPOTHESIS_N_REMAINING)
        self.assertEqual(lock["hypothesis_n_remaining"], 17)
        self.assertEqual(lock["hypothesis_n_distinct"], HYPOTHESIS_N_DISTINCT)
        self.assertEqual(lock["hypothesis_n_distinct"], 17)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["locked_next_stems"]), STANDING_LOCKED_NEXT_STEMS)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 34)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE172_NEXT_4GRAMS],
            lock["leftover_next_4grams"],
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
        self.assertEqual(lock["N_locked_cluster"], 17)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 17)
        self.assertEqual(
            lock["N_distinct_remaining_next_stems"],
            STANDING_N_DISTINCT_REMAINING_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_remaining_next_stems"], 17)
        self.assertEqual(lock["N_no_forward"], STANDING_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(lock["no_forward_sites"], [])
        self.assertEqual(
            tuple(tuple(row) for row in lock["locked_cluster_sites"]),
            STANDING_LOCKED_CLUSTER_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_leftover_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_REMAINING_NEXT_4GRAMS],
            lock["remaining_next_4grams"],
        )
        self.assertEqual(tuple(lock["remaining_next_stems"]), STANDING_REMAINING_NEXT_STEMS)
        self.assertEqual(
            lock["remaining_leftover_local_4grams"],
            matching_leftover_local_4gram_rows(
                STANDING_REMAINING_SITES,
                STANDING_REMAINING_NEXT_4GRAMS,
            ),
        )
        self.assertEqual(
            lock["N_distinct_leftover_next_4grams"],
            STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS,
        )
        self.assertEqual(lock["N_distinct_leftover_next_4grams"], 34)
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["cycle173_076_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE173_MATCHING_SITES],
            lock["cycle173_matching_sites"],
        )
        self.assertEqual(lock["cycle173_N_with_forward_076_071_076"], 5)
        self.assertTrue(lock["cycle176_600_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE176_MATCHING_SITES],
            lock["cycle176_matching_sites"],
        )
        self.assertEqual(lock["cycle176_N_with_forward_076_071_600"], 4)
        self.assertTrue(lock["cycle179_090_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE179_MATCHING_SITES],
            lock["cycle179_matching_sites"],
        )
        self.assertEqual(lock["cycle179_N_with_forward_076_071_090"], 3)
        self.assertTrue(lock["cycle182_700_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE182_MATCHING_SITES],
            lock["cycle182_matching_sites"],
        )
        self.assertEqual(lock["cycle182_N_with_forward_076_071_700"], 3)
        self.assertTrue(lock["cycle185_061_cluster_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE185_MATCHING_SITES],
            lock["cycle185_matching_sites"],
        )
        self.assertEqual(lock["cycle185_N_with_forward_076_071_061"], 2)
        self.assertTrue(lock["remaining_sites_disjoint_from_locked_clusters"])
        self.assertTrue(lock["share_one_forward_4gram_not_locked"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_071_remaining_next_stems_all_distinct"])
        self.assertEqual(
            lock["i_leftover_076_071_remaining_next_stems_all_distinct"],
            STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle173"])
        self.assertFalse(lock["same_as_cycle176"])
        self.assertFalse(lock["same_as_cycle179"])
        self.assertFalse(lock["same_as_cycle182"])
        self.assertFalse(lock["same_as_cycle185"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["other_leftover_n4_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle173_leftover_next_4grams_remeasured"])
        self.assertTrue(lock["standing_i_076_071_061_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_076_071_061_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_061_unchanged"])
        self.assertTrue(lock["standing_i_076_071_700_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_076_071_700_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_700_unchanged"])
        self.assertTrue(lock["standing_i_076_071_090_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_076_071_090_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_090_unchanged"])
        self.assertTrue(lock["standing_i_076_071_600_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_076_071_600_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_600_unchanged"])
        self.assertTrue(lock["standing_i_076_071_076_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_076_071_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_076_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_076_071_061_forward_4grams_i_only"]["cycle"], 187)
        self.assertTrue(
            self.survey["i_076_071_061_forward_4grams_i_only"][
                "i_076_071_061_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_076_071_061_i_only"]["cycle"], 186)
        self.assertTrue(
            self.survey["i_3gram_076_071_061_i_only"]["i_3gram_076_071_061_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_076_071_061_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_076_071_061_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_076_071_forward_061"]["cycle"], 185)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_061"][
                "i_leftover_076_071_exactly_2_forward_076_071_061"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_061"]["N_with_forward_076_071_061"],
            2,
        )
        self.assertEqual(self.survey["i_leftover_076_071_forward_700"]["cycle"], 182)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_700"][
                "i_leftover_076_071_exactly_3_forward_076_071_700"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_700"]["N_with_forward_076_071_700"],
            3,
        )
        self.assertEqual(self.survey["i_leftover_076_071_forward_090"]["cycle"], 179)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_090"][
                "i_leftover_076_071_exactly_3_forward_076_071_090"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_090"]["N_with_forward_076_071_090"],
            3,
        )
        self.assertEqual(self.survey["i_leftover_076_071_forward_600"]["cycle"], 176)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_600"][
                "i_leftover_076_071_exactly_4_forward_076_071_600"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_600"]["N_with_forward_076_071_600"],
            4,
        )
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["cycle"], 173)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_076"][
                "i_leftover_076_071_exactly_5_forward_076_071_076"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_076"]["N_with_forward_076_071_076"],
            5,
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
            self.survey["i_leftover_n4_076_071"][
                "i_leftover_n4_exactly_4_contain_076_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["N_with_076_071"], 4)
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
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover076071RemainingNextStemsDistinctImageSnapshot(unittest.TestCase):
    """Cycle 188 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
