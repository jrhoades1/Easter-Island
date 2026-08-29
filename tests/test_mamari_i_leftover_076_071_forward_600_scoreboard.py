"""I's cycle-172 leftover 2-gram forward 600 cluster lock.

Cycle 176 text-search lock. Uses already-vendored A–V and the
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
is 600 (forward 3-gram 076 071 600; the local next 4-gram
starts with 076 071 600). End-of-line is no-forward. The 9
inside-family sites do not count as leftover (including
Ia3[81] 076 071 076 385). Cycle 173's five leftover
076 071 076 sites are a different cluster and do not count
toward this 600 cluster. 071 999 and 076 076 do not count
as this 2-gram. Same inventory move as cycle 173: lock the
next-largest leftover continuation cluster (after cycle 173
N=5 forward 076, this is N=4 forward 600).

Hypothesis N=4: exactly 4 of the 34 leftover sites share
forward 3-gram 076 071 600. Measured: N_leftover=34,
N_with_forward_076_071_600=4 at Ia2[104] 076 071 600 090,
Ia2[169] 076 071 600 009, Ia9[10] 076 071 600 999,
Ia14[106] 076 071 600 053; N_without=30; N_no_forward=0.
Claim that can lose:
i_leftover_076_071_exactly_4_forward_076_071_600. True only
if N_with_forward_076_071_600=4. The claim is true. Do not
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
from tests.test_mamari_i_3gram_076_071_076_i_only_scoreboard import (
    TestMamariI3gram076071076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_inside_family_scoreboard import (
    leftover_sites_from_membership,
    membership_for_sites,
)
from tests.test_mamari_i_076_071_076_forward_4grams_i_only_scoreboard import (
    TestMamariI076071076Forward4gramsIOnlyScoreboard,
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

HYPOTHESIS_N = 4
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("076", "071", "600")
STANDING_N_LEFTOVER = 34
STANDING_N_WITH_FORWARD_076_071_600 = 4
STANDING_N_WITHOUT = 30
STANDING_N_NO_FORWARD = 0
STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS = 34
STANDING_NO_FORWARD_SITES = ()
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia2", 104),
    (SIDE_IA, "Ia2", 169),
    (SIDE_IA, "Ia9", 10),
    (SIDE_IA, "Ia14", 106),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("076", "071", "600", "090"),
    ("076", "071", "600", "009"),
    ("076", "071", "600", "999"),
    ("076", "071", "600", "053"),
)
STANDING_WITHOUT_SITES = (
    (SIDE_IA, "Ia1", 86),
    (SIDE_IA, "Ia1", 163),
    (SIDE_IA, "Ia2", 43),
    (SIDE_IA, "Ia2", 51),
    (SIDE_IA, "Ia3", 13),
    (SIDE_IA, "Ia3", 85),
    (SIDE_IA, "Ia3", 110),
    (SIDE_IA, "Ia3", 133),
    (SIDE_IA, "Ia3", 147),
    (SIDE_IA, "Ia5", 67),
    (SIDE_IA, "Ia5", 79),
    (SIDE_IA, "Ia5", 134),
    (SIDE_IA, "Ia6", 117),
    (SIDE_IA, "Ia7", 32),
    (SIDE_IA, "Ia7", 48),
    (SIDE_IA, "Ia8", 27),
    (SIDE_IA, "Ia12", 6),
    (SIDE_IA, "Ia12", 19),
    (SIDE_IA, "Ia12", 59),
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
    (SIDE_IA, "Ia14", 166),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_071_exactly_4_forward_076_071_600"
STANDING_I_LEFTOVER_076_071_EXACTLY_4_FORWARD_076_071_600 = True
STANDING_RESULT = "i_leftover_076_071_forward_600"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE173 = False
STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED = True
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_CYCLE173_076_CLUSTER_DOES_NOT_COUNT = True


def leftover_with_forward_076_071_600(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
    needle: tuple[str, ...] = GRAM3_FORWARD,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose forward 3-gram is 076 071 600."""
    return tuple(
        site
        for site, fwd in zip(sites, forwards, strict=True)
        if fwd == needle
    )


def leftover_without_forward_076_071_600(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
    needle: tuple[str, ...] = GRAM3_FORWARD,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that have a next stem other than 600, or none."""
    return tuple(
        site
        for site, fwd in zip(sites, forwards, strict=True)
        if fwd != needle
    )


def i_leftover_076_071_exactly_4_forward_076_071_600(
    n_with_forward_076_071_600: int,
    expected: int = HYPOTHESIS_N,
) -> bool:
    """True iff N_with_forward_076_071_600 equals the hypothesized 4."""
    return n_with_forward_076_071_600 == expected


class TestILeftover076071Forward600Helpers(unittest.TestCase):
    """Helpers on cycle-172 leftover 076 071 sites. No CV, no LLM."""

    def test_forward_requires_next_stem_after_2gram(self):
        """A next stem is a 3-gram; end-of-line is no-forward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM3_FORWARD, ("076", "071", "600"))
        self.assertEqual(GRAM3_FORWARD[:STANDING_N2], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_next = ["005", "633", "076", "071", "600", "090"]
        self.assertEqual(site_forward_3gram(has_next, 2, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_next, 2, GRAM2),
            ("076", "071", "600", "090"),
        )
        other_next = ["027", "200", "076", "071", "090", "606"]
        self.assertEqual(
            site_forward_3gram(other_next, 2, GRAM2),
            ("076", "071", "090"),
        )
        self.assertNotEqual(site_forward_3gram(other_next, 2, GRAM2), GRAM3_FORWARD)
        cycle173_next = ["430", "071", "076", "071", "076", "021"]
        self.assertEqual(
            site_forward_3gram(cycle173_next, 2, GRAM2),
            CYCLE173_GRAM3_FORWARD,
        )
        self.assertNotEqual(
            site_forward_3gram(cycle173_next, 2, GRAM2),
            GRAM3_FORWARD,
        )
        end_of_line = ["027", "200", "076", "071"]
        self.assertIsNone(site_forward_3gram(end_of_line, 2, GRAM2))
        self.assertIsNone(site_next_4gram(end_of_line, 2, GRAM2))
        mismatch = ["076", "070", "600", "090"]
        self.assertIsNone(site_forward_3gram(mismatch, 0, GRAM2))
        gapped = ["076", "072", "600"]
        self.assertIsNone(site_forward_3gram(gapped, 0, GRAM2))
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_4_can_fail(self):
        """Boolean is True only when N_with_forward_076_071_600=4."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_071_exactly_4_forward_076_071_600(4))
        self.assertFalse(i_leftover_076_071_exactly_4_forward_076_071_600(0))
        self.assertFalse(i_leftover_076_071_exactly_4_forward_076_071_600(3))
        self.assertFalse(i_leftover_076_071_exactly_4_forward_076_071_600(5))
        self.assertFalse(i_leftover_076_071_exactly_4_forward_076_071_600(34))
        self.assertFalse(i_leftover_076_071_exactly_4_forward_076_071_600(1))
        planted = STANDING_MATCHING_SITES + (CYCLE173_MATCHING_SITES[0],)
        planted_forwards = (GRAM3_FORWARD,) * 5
        self.assertEqual(
            leftover_with_forward_076_071_600(planted, planted_forwards),
            planted,
        )
        self.assertFalse(
            i_leftover_076_071_exactly_4_forward_076_071_600(len(planted))
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_exactly_4_forward_076_071_600")
        self.assertTrue(STANDING_I_LEFTOVER_076_071_EXACTLY_4_FORWARD_076_071_600)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_071_EXACTLY_4_FORWARD_076_071_600,
            HYPOTHESIS_N == STANDING_N_WITH_FORWARD_076_071_600,
        )
        self.assertEqual(STANDING_N_WITH_FORWARD_076_071_600 + STANDING_N_WITHOUT, 34)
        self.assertEqual(provider.get_call_history(), [])

    def test_inside_family_cycle173_and_near_misses_do_not_count(self):
        """Inside Ia3[81], cycle-173 076 cluster, 071 999, and 076 076 are not this 600 cluster."""
        provider = MockProvider()
        self.assertIn(STANDING_INSIDE_FORWARD_076_SITE, STANDING_INSIDE_SITES)
        self.assertNotIn(STANDING_INSIDE_FORWARD_076_SITE, STANDING_LEFTOVER_SITES)
        self.assertNotIn(STANDING_INSIDE_FORWARD_076_SITE, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertEqual(
            STANDING_INSIDE_FORWARD_076_NEXT_4GRAM[:3],
            CYCLE173_GRAM3_FORWARD,
        )
        self.assertNotEqual(
            STANDING_INSIDE_FORWARD_076_NEXT_4GRAM[:3],
            GRAM3_FORWARD,
        )
        for site in CYCLE173_MATCHING_SITES:
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_WITHOUT_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE173_076_CLUSTER_DOES_NOT_COUNT)
        self.assertEqual(CYCLE173_N_WITH, 5)
        self.assertEqual(CYCLE173_GRAM3_FORWARD, ("076", "071", "076"))
        self.assertNotEqual(GRAM3_FORWARD, CYCLE173_GRAM3_FORWARD)
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
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076071Forward600Scoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 071 forward-600 cluster. Mock only."""

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
        self.with_sites = leftover_with_forward_076_071_600(
            self.leftover_sites,
            self.forwards,
        )
        self.without_sites = leftover_without_forward_076_071_600(
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
        self.claim_holds = i_leftover_076_071_exactly_4_forward_076_071_600(
            self.n_with,
        )

    def test_tokens_and_sites_are_cycle_172_leftover_not_retuned(self):
        """2-gram and leftover 34 stay the cycle-172/171/170 locks."""
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM3_FORWARD, ("076", "071", "600"))
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
        prior_175 = self.survey["i_076_071_076_forward_4grams_i_only"]
        self.assertEqual(prior_175["cycle"], 175)
        self.assertTrue(prior_175["i_076_071_076_forward_4grams_i_only"])
        prior_174 = self.survey["i_3gram_076_071_076_i_only"]
        self.assertEqual(prior_174["cycle"], 174)
        self.assertTrue(prior_174["i_3gram_076_071_076_i_only"])
        self.assertEqual(prior_174["N_I"], 6)
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_4_of_34_and_hypothesis_n_4_holds(self):
        """N_leftover=34, N_with=4, N_without=30. Claim holds."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 34)
        self.assertEqual(self.n_with, STANDING_N_WITH_FORWARD_076_071_600)
        self.assertEqual(STANDING_N_WITH_FORWARD_076_071_600, 4)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 30)
        self.assertEqual(self.n_no_forward, STANDING_N_NO_FORWARD)
        self.assertEqual(STANDING_N_NO_FORWARD, 0)
        self.assertEqual(self.no_forward, STANDING_NO_FORWARD_SITES)
        self.assertEqual(self.n_with + self.n_without, self.n_leftover)
        self.assertEqual(HYPOTHESIS_N, 4)
        self.assertTrue(i_leftover_076_071_exactly_4_forward_076_071_600(self.n_with))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_071_EXACTLY_4_FORWARD_076_071_600,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_071_EXACTLY_4_FORWARD_076_071_600)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_exactly_4_forward_076_071_600")
        self.assertEqual(self.next_4grams, CYCLE172_NEXT_4GRAMS)
        self.assertEqual(len(set(self.next_4grams)), STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_LEFTOVER_NEXT_4GRAMS, 34)
        self.assertTrue(STANDING_SHARE_ONE_FORWARD_4GRAM_NOT_LOCKED)
        self.assertFalse(STANDING_SAME_AS_CYCLE173)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_sites_and_next_4grams(self):
        """Four leftover sites share 076 071 600; next 4-grams stay distinct."""
        self.assertEqual(self.with_sites, STANDING_MATCHING_SITES)
        self.assertEqual(self.without_sites, STANDING_WITHOUT_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia2", 104), ("076", "071", "600", "090")),
            ((SIDE_IA, "Ia2", 169), ("076", "071", "600", "009")),
            ((SIDE_IA, "Ia9", 10), ("076", "071", "600", "999")),
            ((SIDE_IA, "Ia14", 106), ("076", "071", "600", "053")),
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
            self.assertEqual(stems[index + STANDING_N2], "600")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
        self.assertEqual(len(set(STANDING_MATCHING_NEXT_4GRAMS)), 4)
        for site in STANDING_WITHOUT_SITES:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            fwd = site_forward_3gram(stems, index, GRAM2)
            self.assertIsNotNone(fwd)
            self.assertNotEqual(fwd, GRAM3_FORWARD)
            self.assertNotEqual(fwd[2], "600")
        for site, nxt in zip(CYCLE173_MATCHING_SITES, CYCLE173_MATCHING_NEXT_4GRAMS):
            self.assertIn(site, self.without_sites)
            self.assertNotIn(site, self.with_sites)
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), CYCLE173_GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), nxt)
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

    def test_existing_175_174_173_172_171_170_103_and_w_scoreboards_still_compute(self):
        """Cycle 175 I-only 4-grams, 174 I-only, 173 N=5, 172 leftover 34, 171, 170, 103, W stay."""
        prior_175 = TestMamariI076071076Forward4gramsIOnlyScoreboard()
        prior_175.setUp()
        prior_175.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_175.test_survey_matches_computed_lock()
        prior_174 = TestMamariI3gram076071076IOnlyScoreboard()
        prior_174.setUp()
        prior_174.test_3gram_is_zero_off_i_and_i_only()
        prior_174.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-176 leftover forward-600 lock."""
        lock = self.survey["i_leftover_076_071_forward_600"]
        self.assertEqual(lock["cycle"], 176)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["hypothesis_n"], 4)
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
        self.assertEqual(lock["N_with_forward_076_071_600"], STANDING_N_WITH_FORWARD_076_071_600)
        self.assertEqual(lock["N_with_forward_076_071_600"], 4)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 30)
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
        self.assertTrue(lock["share_one_forward_4gram_not_locked"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_071_exactly_4_forward_076_071_600"])
        self.assertEqual(
            lock["i_leftover_076_071_exactly_4_forward_076_071_600"],
            STANDING_I_LEFTOVER_076_071_EXACTLY_4_FORWARD_076_071_600,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle173"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["other_leftover_n4_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
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
        self.assertEqual(self.survey["i_076_071_076_forward_4grams_i_only"]["cycle"], 175)
        self.assertTrue(
            self.survey["i_076_071_076_forward_4grams_i_only"][
                "i_076_071_076_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["cycle"], 174)
        self.assertTrue(self.survey["i_3gram_076_071_076_i_only"]["i_3gram_076_071_076_i_only"])
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["N_off_I"], 0)
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
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover076071Forward600ImageSnapshot(unittest.TestCase):
    """Cycle 176 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
