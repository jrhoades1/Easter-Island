"""I's cycle-172 leftover 2-gram forward 061 cluster lock.

Cycle 185 text-search lock. Uses already-vendored A–V and the
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

For each leftover site, whether the next token after 076 071
is 061 (forward 3-gram 076 071 061; the local next 4-gram
starts with 076 071 061). End-of-line is no-forward. The 9
inside-family sites do not count as leftover (none of them
is 076 071 061). Cycle 173's five leftover 076 071 076
sites, cycle 176's four leftover 076 071 600 sites, cycle
179's three leftover 076 071 090 sites, and cycle 182's
three leftover 076 071 700 sites are different clusters
and do not count toward this 061 cluster. 071 999 and
076 076 do not count as this 2-gram. Same inventory move
as cycles 173, 176, 179, and 182: lock the next-largest
leftover continuation cluster (after cycle 173 N=5 forward
076, cycle 176 N=4 forward 600, cycle 179 N=3 forward 090,
and cycle 182 N=3 forward 700, this is N=2 forward 061).
Cycle 184's three 076 071 700 forward 4-grams stay I-only
hapax 1/0.

Hypothesis N=2: exactly 2 of the 34 leftover sites share
forward 3-gram 076 071 061. Measured: N_leftover=34,
N_with_forward_076_071_061=2 at Ia3[147] 076 071 061 011,
Ia12[59] 076 071 061 290; N_without=32; N_no_forward=0.
Claim that can lose:
i_leftover_076_071_exactly_2_forward_076_071_061. True only
if N_with_forward_076_071_061=2. The claim is true. Do not
retune.

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
from tests.test_mamari_i_076_071_700_forward_4grams_i_only_scoreboard import (
    TestMamariI076071700Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_3gram_076_071_700_i_only_scoreboard import (
    TestMamariI3gram076071700IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_inside_family_scoreboard import (
    leftover_sites_from_membership,
    membership_for_sites,
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

HYPOTHESIS_N = 2
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("076", "071", "061")
STANDING_N_LEFTOVER = 34
STANDING_N_WITH_FORWARD_076_071_061 = 2
STANDING_N_WITHOUT = 32
STANDING_N_NO_FORWARD = 0
STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS = 34
STANDING_NO_FORWARD_SITES = ()
STANDING_INSIDE_FORWARD_061_SITES = ()
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia3", 147),
    (SIDE_IA, "Ia12", 59),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("076", "071", "061", "011"),
    ("076", "071", "061", "290"),
)
STANDING_WITHOUT_SITES = (
    (SIDE_IA, "Ia1", 86),
    (SIDE_IA, "Ia1", 163),
    (SIDE_IA, "Ia2", 43),
    (SIDE_IA, "Ia2", 51),
    (SIDE_IA, "Ia2", 104),
    (SIDE_IA, "Ia2", 169),
    (SIDE_IA, "Ia3", 13),
    (SIDE_IA, "Ia3", 85),
    (SIDE_IA, "Ia3", 110),
    (SIDE_IA, "Ia3", 133),
    (SIDE_IA, "Ia5", 67),
    (SIDE_IA, "Ia5", 79),
    (SIDE_IA, "Ia5", 134),
    (SIDE_IA, "Ia6", 117),
    (SIDE_IA, "Ia7", 32),
    (SIDE_IA, "Ia7", 48),
    (SIDE_IA, "Ia8", 27),
    (SIDE_IA, "Ia9", 10),
    (SIDE_IA, "Ia12", 6),
    (SIDE_IA, "Ia12", 19),
    (SIDE_IA, "Ia12", 63),
    (SIDE_IA, "Ia13", 44),
    (SIDE_IA, "Ia13", 54),
    (SIDE_IA, "Ia13", 92),
    (SIDE_IA, "Ia13", 101),
    (SIDE_IA, "Ia13", 114),
    (SIDE_IA, "Ia13", 128),
    (SIDE_IA, "Ia13", 149),
    (SIDE_IA, "Ia13", 153),
    (SIDE_IA, "Ia14", 81),
    (SIDE_IA, "Ia14", 106),
    (SIDE_IA, "Ia14", 166),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_071_exactly_2_forward_076_071_061"
STANDING_I_LEFTOVER_076_071_EXACTLY_2_FORWARD_076_071_061 = True
STANDING_RESULT = "i_leftover_076_071_forward_061"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE173 = False
STANDING_SAME_AS_CYCLE176 = False
STANDING_SAME_AS_CYCLE179 = False
STANDING_SAME_AS_CYCLE182 = False
STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED = True
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_CYCLE173_076_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE176_600_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE179_090_CLUSTER_DOES_NOT_COUNT = True
STANDING_CYCLE182_700_CLUSTER_DOES_NOT_COUNT = True


def leftover_with_forward_076_071_061(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
    needle: tuple[str, ...] = GRAM3_FORWARD,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose forward 3-gram is 076 071 061."""
    return tuple(
        site
        for site, fwd in zip(sites, forwards, strict=True)
        if fwd == needle
    )


def leftover_without_forward_076_071_061(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
    needle: tuple[str, ...] = GRAM3_FORWARD,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that have a next stem other than 061, or none."""
    return tuple(
        site
        for site, fwd in zip(sites, forwards, strict=True)
        if fwd != needle
    )


def i_leftover_076_071_exactly_2_forward_076_071_061(
    n_with_forward_076_071_061: int,
    expected: int = HYPOTHESIS_N,
) -> bool:
    """True iff N_with_forward_076_071_061 equals the hypothesized 2."""
    return n_with_forward_076_071_061 == expected


class TestILeftover076071Forward061Helpers(unittest.TestCase):
    """Helpers on cycle-172 leftover 076 071 sites. No CV, no LLM."""

    def test_forward_requires_next_stem_after_2gram(self):
        """A next stem is a 3-gram; end-of-line is no-forward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM3_FORWARD, ("076", "071", "061"))
        self.assertEqual(GRAM3_FORWARD[:STANDING_N2], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_next = ["600", "604", "076", "071", "061", "011"]
        self.assertEqual(site_forward_3gram(has_next, 2, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_next, 2, GRAM2),
            ("076", "071", "061", "011"),
        )
        other_next = ["050", "606", "076", "071", "061", "290"]
        self.assertEqual(site_forward_3gram(other_next, 2, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(other_next, 2, GRAM2),
            ("076", "071", "061", "290"),
        )
        cycle176_next = ["005", "633", "076", "071", "600", "090"]
        self.assertEqual(
            site_forward_3gram(cycle176_next, 2, GRAM2),
            CYCLE176_GRAM3_FORWARD,
        )
        self.assertNotEqual(site_forward_3gram(cycle176_next, 2, GRAM2), GRAM3_FORWARD)
        cycle173_next = ["430", "071", "076", "071", "076", "021"]
        self.assertEqual(
            site_forward_3gram(cycle173_next, 2, GRAM2),
            CYCLE173_GRAM3_FORWARD,
        )
        self.assertNotEqual(
            site_forward_3gram(cycle173_next, 2, GRAM2),
            GRAM3_FORWARD,
        )
        cycle179_next = ["027", "200", "076", "071", "090", "606"]
        self.assertEqual(
            site_forward_3gram(cycle179_next, 2, GRAM2),
            CYCLE179_GRAM3_FORWARD,
        )
        self.assertNotEqual(
            site_forward_3gram(cycle179_next, 2, GRAM2),
            GRAM3_FORWARD,
        )
        cycle182_next = ["090", "700", "076", "071", "700", "076"]
        self.assertEqual(
            site_forward_3gram(cycle182_next, 2, GRAM2),
            CYCLE182_GRAM3_FORWARD,
        )
        self.assertNotEqual(
            site_forward_3gram(cycle182_next, 2, GRAM2),
            GRAM3_FORWARD,
        )
        end_of_line = ["027", "200", "076", "071"]
        self.assertIsNone(site_forward_3gram(end_of_line, 2, GRAM2))
        self.assertIsNone(site_next_4gram(end_of_line, 2, GRAM2))
        mismatch = ["076", "070", "061", "011"]
        self.assertIsNone(site_forward_3gram(mismatch, 0, GRAM2))
        gapped = ["076", "072", "061"]
        self.assertIsNone(site_forward_3gram(gapped, 0, GRAM2))
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when N_with_forward_076_071_061=2."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_071_exactly_2_forward_076_071_061(2))
        self.assertFalse(i_leftover_076_071_exactly_2_forward_076_071_061(0))
        self.assertFalse(i_leftover_076_071_exactly_2_forward_076_071_061(1))
        self.assertFalse(i_leftover_076_071_exactly_2_forward_076_071_061(3))
        self.assertFalse(i_leftover_076_071_exactly_2_forward_076_071_061(4))
        self.assertFalse(i_leftover_076_071_exactly_2_forward_076_071_061(5))
        self.assertFalse(i_leftover_076_071_exactly_2_forward_076_071_061(34))
        planted = STANDING_MATCHING_SITES + (CYCLE182_MATCHING_SITES[0],)
        planted_forwards = (GRAM3_FORWARD,) * 3
        self.assertEqual(
            leftover_with_forward_076_071_061(planted, planted_forwards),
            planted,
        )
        self.assertFalse(
            i_leftover_076_071_exactly_2_forward_076_071_061(len(planted))
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_exactly_2_forward_076_071_061")
        self.assertTrue(STANDING_I_LEFTOVER_076_071_EXACTLY_2_FORWARD_076_071_061)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_071_EXACTLY_2_FORWARD_076_071_061,
            HYPOTHESIS_N == STANDING_N_WITH_FORWARD_076_071_061,
        )
        self.assertEqual(STANDING_N_WITH_FORWARD_076_071_061 + STANDING_N_WITHOUT, 34)
        self.assertEqual(provider.get_call_history(), [])

    def test_inside_family_prior_clusters_and_near_misses_do_not_count(self):
        """Inside family, cycle-173 076, 176 600, 179 090, 182 700, 071 999, and 076 076 are not this 061 cluster."""
        provider = MockProvider()
        self.assertEqual(STANDING_INSIDE_FORWARD_061_SITES, ())
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertIn(STANDING_INSIDE_FORWARD_076_SITE, STANDING_INSIDE_SITES)
        self.assertNotIn(STANDING_INSIDE_FORWARD_076_SITE, STANDING_LEFTOVER_SITES)
        self.assertNotEqual(
            STANDING_INSIDE_FORWARD_076_NEXT_4GRAM[:3],
            GRAM3_FORWARD,
        )
        for site in STANDING_INSIDE_FORWARD_090_SITES:
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertEqual(STANDING_INSIDE_FORWARD_090_NEXT_4GRAM, ("076", "071", "090", "999"))
        self.assertNotEqual(STANDING_INSIDE_FORWARD_090_NEXT_4GRAM[:3], GRAM3_FORWARD)
        for site in CYCLE173_MATCHING_SITES:
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_WITHOUT_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE173_076_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(CYCLE173_N_WITH, 5)
        self.assertEqual(CYCLE173_GRAM3_FORWARD, ("076", "071", "076"))
        self.assertNotEqual(GRAM3_FORWARD, CYCLE173_GRAM3_FORWARD)
        for site in CYCLE176_MATCHING_SITES:
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_WITHOUT_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE176_600_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(CYCLE176_N_WITH, 4)
        self.assertEqual(CYCLE176_GRAM3_FORWARD, ("076", "071", "600"))
        self.assertNotEqual(GRAM3_FORWARD, CYCLE176_GRAM3_FORWARD)
        for site in CYCLE179_MATCHING_SITES:
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_WITHOUT_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE179_090_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(CYCLE179_N_WITH, 3)
        self.assertEqual(CYCLE179_GRAM3_FORWARD, ("076", "071", "090"))
        self.assertNotEqual(GRAM3_FORWARD, CYCLE179_GRAM3_FORWARD)
        for site in CYCLE182_MATCHING_SITES:
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_WITHOUT_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE182_700_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(CYCLE182_N_WITH, 3)
        self.assertEqual(CYCLE182_GRAM3_FORWARD, ("076", "071", "700"))
        self.assertNotEqual(GRAM3_FORWARD, CYCLE182_GRAM3_FORWARD)
        locked_clusters = (
            set(CYCLE173_MATCHING_SITES)
            | set(CYCLE176_MATCHING_SITES)
            | set(CYCLE179_MATCHING_SITES)
            | set(CYCLE182_MATCHING_SITES)
        )
        self.assertEqual(len(locked_clusters), 5 + 4 + 3 + 3)
        for site in STANDING_MATCHING_SITES:
            self.assertNotIn(site, locked_clusters)
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertTrue(
            is_contiguous_substring(("071", "999"), NEAR_MISS_071_065_071_999)
        )
        self.assertTrue(
            is_contiguous_substring(("076", "076"), NEAR_MISS_700_076_076_053)
        )
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED)
        self.assertEqual(STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS, 34)
        self.assertEqual(len(set(CYCLE172_NEXT_4GRAMS)), 34)
        self.assertFalse(STANDING_SAME_AS_CYCLE173)
        self.assertFalse(STANDING_SAME_AS_CYCLE176)
        self.assertFalse(STANDING_SAME_AS_CYCLE179)
        self.assertFalse(STANDING_SAME_AS_CYCLE182)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076071Forward061Scoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 071 forward-061 cluster. Mock only."""

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
        self.with_sites = leftover_with_forward_076_071_061(
            self.leftover_sites,
            self.forwards,
        )
        self.without_sites = leftover_without_forward_076_071_061(
            self.leftover_sites,
            self.forwards,
        )
        self.no_forward = leftover_sites_without_forward(
            self.leftover_sites,
            self.forwards,
        )
        self.matching_next_4grams = leftover_next_4grams(
            self.i_sides,
            self.with_sites,
            GRAM2,
        )
        self.n_leftover = len(self.leftover_sites)
        self.n_with = len(self.with_sites)
        self.n_without = len(self.without_sites)
        self.n_no_forward = len(self.no_forward)
        self.claim_holds = i_leftover_076_071_exactly_2_forward_076_071_061(
            self.n_with,
        )

    def test_tokens_and_sites_are_cycle_172_leftover_not_retuned(self):
        """2-gram and leftover 34 stay the cycle-172/171/170 locks."""
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM3_FORWARD, ("076", "071", "061"))
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
        prior_184 = self.survey["i_076_071_700_forward_4grams_i_only"]
        self.assertEqual(prior_184["cycle"], 184)
        self.assertTrue(prior_184["i_076_071_700_forward_4grams_i_only"])
        prior_183 = self.survey["i_3gram_076_071_700_i_only"]
        self.assertEqual(prior_183["cycle"], 183)
        self.assertTrue(prior_183["i_3gram_076_071_700_i_only"])
        self.assertEqual(prior_183["N_I"], 3)
        self.assertEqual(prior_183["N_off_I"], 0)
        prior_182 = self.survey["i_leftover_076_071_forward_700"]
        self.assertEqual(prior_182["cycle"], 182)
        self.assertEqual(tuple(prior_182["tokens2"]), GRAM2)
        self.assertEqual(tuple(prior_182["forward_3gram"]), CYCLE182_GRAM3_FORWARD)
        self.assertEqual(prior_182["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_182["N_with_forward_076_071_700"], 3)
        self.assertTrue(prior_182["i_leftover_076_071_exactly_3_forward_076_071_700"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_182["matching_leftover_sites"]),
            CYCLE182_MATCHING_SITES,
        )
        prior_179 = self.survey["i_leftover_076_071_forward_090"]
        self.assertEqual(prior_179["cycle"], 179)
        self.assertEqual(tuple(prior_179["tokens2"]), GRAM2)
        self.assertEqual(tuple(prior_179["forward_3gram"]), CYCLE179_GRAM3_FORWARD)
        self.assertEqual(prior_179["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_179["N_with_forward_076_071_090"], 3)
        self.assertTrue(prior_179["i_leftover_076_071_exactly_3_forward_076_071_090"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_179["matching_leftover_sites"]),
            CYCLE179_MATCHING_SITES,
        )
        prior_176 = self.survey["i_leftover_076_071_forward_600"]
        self.assertEqual(prior_176["cycle"], 176)
        self.assertEqual(tuple(prior_176["tokens2"]), GRAM2)
        self.assertEqual(tuple(prior_176["forward_3gram"]), CYCLE176_GRAM3_FORWARD)
        self.assertEqual(prior_176["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_176["N_with_forward_076_071_600"], 4)
        self.assertTrue(prior_176["i_leftover_076_071_exactly_4_forward_076_071_600"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_176["matching_leftover_sites"]),
            CYCLE176_MATCHING_SITES,
        )
        prior_173 = self.survey["i_leftover_076_071_forward_076"]
        self.assertEqual(prior_173["cycle"], 173)
        self.assertEqual(tuple(prior_173["tokens2"]), GRAM2)
        self.assertEqual(tuple(prior_173["forward_3gram"]), CYCLE173_GRAM3_FORWARD)
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_of_34_and_hypothesis_n_2_holds(self):
        """N_leftover=34, N_with=2, N_without=32. Claim holds."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 34)
        self.assertEqual(self.n_with, STANDING_N_WITH_FORWARD_076_071_061)
        self.assertEqual(STANDING_N_WITH_FORWARD_076_071_061, 2)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 32)
        self.assertEqual(self.n_no_forward, STANDING_N_NO_FORWARD)
        self.assertEqual(STANDING_N_NO_FORWARD, 0)
        self.assertEqual(self.no_forward, STANDING_NO_FORWARD_SITES)
        self.assertEqual(self.n_with + self.n_without, self.n_leftover)
        self.assertEqual(HYPOTHESIS_N, 2)
        self.assertTrue(i_leftover_076_071_exactly_2_forward_076_071_061(self.n_with))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_071_EXACTLY_2_FORWARD_076_071_061,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_071_EXACTLY_2_FORWARD_076_071_061)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_exactly_2_forward_076_071_061")
        self.assertEqual(self.next_4grams, CYCLE172_NEXT_4GRAMS)
        self.assertEqual(len(set(self.next_4grams)), STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS, 34)
        self.assertTrue(STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED)
        self.assertFalse(STANDING_SAME_AS_CYCLE173)
        self.assertFalse(STANDING_SAME_AS_CYCLE176)
        self.assertFalse(STANDING_SAME_AS_CYCLE179)
        self.assertFalse(STANDING_SAME_AS_CYCLE182)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_sites_and_next_4grams(self):
        """Two leftover sites share 076 071 061; next 4-grams stay distinct."""
        self.assertEqual(self.with_sites, STANDING_MATCHING_SITES)
        self.assertEqual(self.without_sites, STANDING_WITHOUT_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia3", 147), ("076", "071", "061", "011")),
            ((SIDE_IA, "Ia12", 59), ("076", "071", "061", "290")),
        )
        for (site, nxt), (want_site, want_nxt) in zip(
            zip(self.with_sites, self.matching_next_4grams, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3_FORWARD)
            self.assertEqual(stems[index + STANDING_N2], "061")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
        self.assertEqual(len(set(STANDING_MATCHING_NEXT_4GRAMS)), 2)
        for site in STANDING_WITHOUT_SITES:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            fwd = site_forward_3gram(stems, index, GRAM2)
            self.assertIsNotNone(fwd)
            self.assertNotEqual(fwd, GRAM3_FORWARD)
            self.assertNotEqual(fwd[2], "061")
        locked_clusters = (
            (CYCLE173_MATCHING_SITES, CYCLE173_MATCHING_NEXT_4GRAMS, CYCLE173_GRAM3_FORWARD),
            (CYCLE176_MATCHING_SITES, CYCLE176_MATCHING_NEXT_4GRAMS, CYCLE176_GRAM3_FORWARD),
            (CYCLE179_MATCHING_SITES, CYCLE179_MATCHING_NEXT_4GRAMS, CYCLE179_GRAM3_FORWARD),
            (CYCLE182_MATCHING_SITES, CYCLE182_MATCHING_NEXT_4GRAMS, CYCLE182_GRAM3_FORWARD),
        )
        for prior_sites, prior_next, prior_gram3 in locked_clusters:
            for site, nxt in zip(prior_sites, prior_next):
                self.assertIn(site, self.without_sites)
                self.assertNotIn(site, self.with_sites)
                stems = line_stems_for_site(self.i_sides, site)
                index = site[2]
                self.assertEqual(site_forward_3gram(stems, index, GRAM2), prior_gram3)
                self.assertEqual(site_next_4gram(stems, index, GRAM2), nxt)
                self.assertNotEqual(prior_gram3, GRAM3_FORWARD)
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, self.with_sites)
            self.assertNotIn(site, self.leftover_sites)
            inside_stems = line_stems_for_site(self.i_sides, site)
            inside_index = site[2]
            inside_fwd = site_forward_3gram(inside_stems, inside_index, GRAM2)
            self.assertNotEqual(inside_fwd, GRAM3_FORWARD)
        for site in STANDING_INSIDE_FORWARD_090_SITES:
            self.assertNotIn(site, self.with_sites)
            self.assertNotIn(site, self.leftover_sites)
            inside_stems = line_stems_for_site(self.i_sides, site)
            inside_index = site[2]
            self.assertEqual(
                site_next_4gram(inside_stems, inside_index, GRAM2),
                STANDING_INSIDE_FORWARD_090_NEXT_4GRAM,
            )
        self.assertNotIn(STANDING_INSIDE_FORWARD_076_SITE, self.with_sites)
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_184_183_182_179_176_173_172_171_170_103_and_w_scoreboards_still_compute(self):
        """Cycle 184 I-only 4-grams, 183 I-only, 182 leftover-3, 179 leftover-3, 176 leftover-4, 173 leftover-5, 172 leftover-34 stay."""
        prior_184 = TestMamariI076071700Forward4gramsIOnlyScoreboard()
        prior_184.setUp()
        prior_184.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_184.test_survey_matches_computed_lock()
        prior_183 = TestMamariI3gram076071700IOnlyScoreboard()
        prior_183.setUp()
        prior_183.test_3gram_is_zero_off_i_and_i_only()
        prior_183.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-185 leftover forward-061 lock."""
        lock = self.survey["i_leftover_076_071_forward_061"]
        self.assertEqual(lock["cycle"], 185)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["hypothesis_n"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
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
        self.assertEqual(lock["N_with_forward_076_071_061"], STANDING_N_WITH_FORWARD_076_071_061)
        self.assertEqual(lock["N_with_forward_076_071_061"], 2)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 32)
        self.assertEqual(lock["N_no_forward"], STANDING_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(lock["no_forward_sites"], [])
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_local_4grams"],
            matching_leftover_local_4gram_rows(
                STANDING_MATCHING_SITES,
                STANDING_MATCHING_NEXT_4GRAMS,
            ),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["without_sites"]),
            STANDING_WITHOUT_SITES,
        )
        self.assertEqual(
            lock["N_distinct_leftover_next_4grams"],
            STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS,
        )
        self.assertEqual(lock["N_distinct_leftover_next_4grams"], 34)
        self.assertEqual(lock["inside_forward_061_sites"], [])
        self.assertEqual(
            [list(site) for site in STANDING_INSIDE_FORWARD_090_SITES],
            lock["inside_forward_090_sites"],
        )
        self.assertEqual(
            tuple(lock["inside_forward_090_next_4gram"]),
            STANDING_INSIDE_FORWARD_090_NEXT_4GRAM,
        )
        self.assertEqual(
            tuple(lock["inside_forward_076_site"]),
            STANDING_INSIDE_FORWARD_076_SITE,
        )
        self.assertEqual(
            tuple(lock["inside_forward_076_next_4gram"]),
            STANDING_INSIDE_FORWARD_076_NEXT_4GRAM,
        )
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
        self.assertTrue(lock["share_one_forward_4gram_not_locked"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_071_exactly_2_forward_076_071_061"])
        self.assertEqual(
            lock["i_leftover_076_071_exactly_2_forward_076_071_061"],
            STANDING_I_LEFTOVER_076_071_EXACTLY_2_FORWARD_076_071_061,
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
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["other_leftover_n4_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
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
        self.assertEqual(self.survey["i_076_071_700_forward_4grams_i_only"]["cycle"], 184)
        self.assertTrue(
            self.survey["i_076_071_700_forward_4grams_i_only"][
                "i_076_071_700_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_076_071_700_i_only"]["cycle"], 183)
        self.assertTrue(
            self.survey["i_3gram_076_071_700_i_only"]["i_3gram_076_071_700_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_076_071_700_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_076_071_700_i_only"]["N_off_I"], 0)
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
        self.assertEqual(self.survey["i_leftover_076_071_forward_700"]["N_without"], 31)
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
        self.assertEqual(self.survey["i_leftover_076_071_forward_090"]["N_without"], 31)
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
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["N_without"], 29)
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
        self.assertEqual(self.survey["i_3gram_999_090_076_inside_family"]["cycle"], 168)
        self.assertFalse(
            self.survey["i_3gram_999_090_076_inside_family"][
                "i_3gram_999_090_076_all_inside_leftover_n4_family"
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
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover076071Forward061ImageSnapshot(unittest.TestCase):
    """Cycle 185 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
