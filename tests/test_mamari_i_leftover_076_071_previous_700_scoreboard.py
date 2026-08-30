"""I's cycle-172 leftover 2-gram previous 700 cluster lock.

Cycle 191 text-search lock. Uses already-vendored A–V and the
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

For each leftover site, whether the previous token immediately
before 076 071 is 700 (backward 3-gram 700 076 071; the local
previous 4-gram ends with 700 076 071). Start-of-line is
no-backward. Cycle 190 leftover previous-stem N_distinct=28,
cycle 172 leftover N=34, and cycle 171 I-only 43/0 stay. The
9 inside-family sites do not count as leftover (none of them
is 700 076 071). Cycle 182's three leftover 076 071 700
forward sites are a different 3-gram and do not count toward
this previous-700 cluster except where a leftover site
independently also has previous 700. Ia9[10] 700 604 076 071
is leftover but previous stem 604, not 700. 071 999 and
076 076 do not count as this 2-gram.

Hypothesis N=3: exactly 3 of the 34 leftover sites share
previous 3-gram 700 076 071. Measured: N_leftover=34,
N_with_previous_700_076_071=3 at Ia1[163] 090 700 076 071,
Ia2[51] 999 700 076 071, Ia13[128] 040 700 076 071;
N_without=31; N_no_backward=0. Claim that can lose:
i_leftover_076_071_exactly_3_previous_700_076_071. True only
if N_with_previous_700_076_071=3. The claim is true. Do not
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
from tests.test_mamari_i_leftover_076_071_forward_700_scoreboard import (
    GRAM3_FORWARD as CYCLE182_GRAM3_FORWARD,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE182_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE182_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_700 as CYCLE182_N_WITH,
    TestMamariILeftover076071Forward700Scoreboard,
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

HYPOTHESIS_N = 3
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STEM_700 = "700"
GRAM3_BACKWARD = ("700", "076", "071")
STANDING_N_LEFTOVER = 34
STANDING_N_WITH_PREVIOUS_700_076_071 = 3
STANDING_N_WITHOUT = 31
STANDING_N_NO_BACKWARD = 0
STANDING_NO_BACKWARD_SITES = ()
STANDING_INSIDE_PREVIOUS_700_SITES = ()
STANDING_NEAR_MISS_LEFTOVER_700_604_SITE = (SIDE_IA, "Ia9", 10)
STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM = ("700", "604", "076", "071")
STANDING_NEAR_MISS_INSIDE_700_071_SITE = (SIDE_IA, "Ia14", 136)
STANDING_NEAR_MISS_INSIDE_700_071_PREVIOUS_4GRAM = ("700", "071", "076", "071")
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia1", 163),
    (SIDE_IA, "Ia2", 51),
    (SIDE_IA, "Ia13", 128),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("090", "700", "076", "071"),
    ("999", "700", "076", "071"),
    ("040", "700", "076", "071"),
)
STANDING_WITHOUT_SITES = (
    (SIDE_IA, "Ia1", 86),
    (SIDE_IA, "Ia2", 43),
    (SIDE_IA, "Ia2", 104),
    (SIDE_IA, "Ia2", 169),
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
    (SIDE_IA, "Ia9", 10),
    (SIDE_IA, "Ia12", 6),
    (SIDE_IA, "Ia12", 19),
    (SIDE_IA, "Ia12", 59),
    (SIDE_IA, "Ia12", 63),
    (SIDE_IA, "Ia13", 44),
    (SIDE_IA, "Ia13", 54),
    (SIDE_IA, "Ia13", 92),
    (SIDE_IA, "Ia13", 101),
    (SIDE_IA, "Ia13", 114),
    (SIDE_IA, "Ia13", 149),
    (SIDE_IA, "Ia13", 153),
    (SIDE_IA, "Ia14", 81),
    (SIDE_IA, "Ia14", 106),
    (SIDE_IA, "Ia14", 166),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_071_exactly_3_previous_700_076_071"
STANDING_I_LEFTOVER_076_071_EXACTLY_3_PREVIOUS_700_076_071 = True
STANDING_RESULT = "i_leftover_076_071_previous_700"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE190 = False
STANDING_SAME_AS_CYCLE182 = False
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_CYCLE182_FORWARD_700_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_700_604_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_with_previous_700_076_071(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
    needle: tuple[str, ...] = GRAM3_BACKWARD,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose backward 3-gram is 700 076 071."""
    return tuple(
        site
        for site, back in zip(sites, backwards, strict=True)
        if back == needle
    )


def leftover_without_previous_700_076_071(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
    needle: tuple[str, ...] = GRAM3_BACKWARD,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that have a previous stem other than 700, or none."""
    return tuple(
        site
        for site, back in zip(sites, backwards, strict=True)
        if back != needle
    )


def matching_leftover_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover previous-4-gram rows."""
    rows = []
    for (side, line, index), prev_gram in zip(
        leftover_sites,
        previous_4grams,
        strict=True,
    ):
        rows.append(
            {
                "tablet": "I",
                "side": side,
                "line": line,
                "index": index,
                "previous_4gram": list(prev_gram),
                "backward_3gram": list(prev_gram[1:]),
            }
        )
    return rows


def i_leftover_076_071_exactly_3_previous_700_076_071(
    n_with_previous_700_076_071: int,
    expected: int = HYPOTHESIS_N,
) -> bool:
    """True iff N_with_previous_700_076_071 equals the hypothesized 3."""
    return n_with_previous_700_076_071 == expected


class TestILeftover076071Previous700Helpers(unittest.TestCase):
    """Helpers on cycle-172 leftover 076 071 previous 700. No CV, no LLM."""

    def test_previous_requires_stem_700_before_2gram(self):
        """A previous 700 is a 3-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM3_BACKWARD, ("700", "076", "071"))
        self.assertEqual(GRAM3_BACKWARD[1:], GRAM2)
        self.assertEqual(GRAM3_BACKWARD[0], STEM_700)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_700 = ["090", "700", "076", "071", "700", "076"]
        self.assertEqual(site_previous_stem(has_700, 2, GRAM2), STEM_700)
        self.assertEqual(site_backward_3gram(has_700, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_700, 2, GRAM2),
            ("090", "700", "076", "071"),
        )
        other_prev = ["000", "090", "076", "071", "004", "004"]
        self.assertEqual(site_previous_stem(other_prev, 2, GRAM2), "090")
        self.assertNotEqual(site_backward_3gram(other_prev, 2, GRAM2), GRAM3_BACKWARD)
        near_miss_604 = ["700", "604", "076", "071", "513", "001"]
        self.assertEqual(site_previous_stem(near_miss_604, 2, GRAM2), "604")
        self.assertEqual(
            site_previous_4gram(near_miss_604, 2, GRAM2),
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
        )
        self.assertNotEqual(site_backward_3gram(near_miss_604, 2, GRAM2), GRAM3_BACKWARD)
        start_of_line = ["076", "071", "090", "606"]
        self.assertIsNone(site_previous_stem(start_of_line, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(start_of_line, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(start_of_line, 0, GRAM2))
        mismatch = ["700", "076", "070"]
        self.assertIsNone(site_previous_stem(mismatch, 1, GRAM2))
        self.assertIsNone(site_backward_3gram(mismatch, 1, GRAM2))
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_3_can_fail(self):
        """Boolean is True only when N_with_previous_700_076_071=3."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_071_exactly_3_previous_700_076_071(3))
        self.assertFalse(i_leftover_076_071_exactly_3_previous_700_076_071(0))
        self.assertFalse(i_leftover_076_071_exactly_3_previous_700_076_071(2))
        self.assertFalse(i_leftover_076_071_exactly_3_previous_700_076_071(4))
        self.assertFalse(i_leftover_076_071_exactly_3_previous_700_076_071(5))
        self.assertFalse(i_leftover_076_071_exactly_3_previous_700_076_071(28))
        self.assertFalse(i_leftover_076_071_exactly_3_previous_700_076_071(34))
        self.assertFalse(i_leftover_076_071_exactly_3_previous_700_076_071(1))
        planted = STANDING_MATCHING_SITES + (STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,)
        planted_backs = (GRAM3_BACKWARD,) * 4
        self.assertEqual(
            leftover_with_previous_700_076_071(planted, planted_backs),
            planted,
        )
        self.assertFalse(
            i_leftover_076_071_exactly_3_previous_700_076_071(len(planted))
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_exactly_3_previous_700_076_071")
        self.assertTrue(STANDING_I_LEFTOVER_076_071_EXACTLY_3_PREVIOUS_700_076_071)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_071_EXACTLY_3_PREVIOUS_700_076_071,
            HYPOTHESIS_N == STANDING_N_WITH_PREVIOUS_700_076_071,
        )
        self.assertEqual(STANDING_N_WITH_PREVIOUS_700_076_071 + STANDING_N_WITHOUT, 34)
        self.assertEqual(provider.get_call_history(), [])

    def test_inside_family_forward_cluster_and_near_misses_do_not_count(self):
        """Inside family, cycle-182 forward 700, 700 604, 071 999, and 076 076 are not this cluster."""
        provider = MockProvider()
        self.assertEqual(STANDING_INSIDE_PREVIOUS_700_SITES, ())
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertIn(STANDING_NEAR_MISS_INSIDE_700_071_SITE, STANDING_INSIDE_SITES)
        self.assertNotIn(STANDING_NEAR_MISS_INSIDE_700_071_SITE, STANDING_LEFTOVER_SITES)
        self.assertNotEqual(
            STANDING_NEAR_MISS_INSIDE_700_071_PREVIOUS_4GRAM[1:],
            GRAM3_BACKWARD,
        )
        self.assertEqual(
            STANDING_NEAR_MISS_INSIDE_700_071_PREVIOUS_4GRAM[1:],
            ("071", "076", "071"),
        )
        self.assertIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, STANDING_LEFTOVER_SITES)
        self.assertIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, STANDING_WITHOUT_SITES)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, STANDING_MATCHING_SITES)
        self.assertEqual(
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM[1:],
            ("604", "076", "071"),
        )
        self.assertTrue(STANDING_NEAR_MISS_700_604_DOES_NOT_COUNT)
        for site in CYCLE182_MATCHING_SITES:
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            if site == (SIDE_IA, "Ia1", 163):
                self.assertIn(site, STANDING_MATCHING_SITES)
            else:
                self.assertIn(site, STANDING_WITHOUT_SITES)
                self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE182_FORWARD_700_DOES_NOT_COUNT)
        self.assertEqual(CYCLE182_N_WITH, 3)
        self.assertEqual(CYCLE182_GRAM3_FORWARD, ("076", "071", "700"))
        self.assertNotEqual(GRAM3_BACKWARD, CYCLE182_GRAM3_FORWARD)
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
        self.assertFalse(STANDING_SAME_AS_CYCLE190)
        self.assertFalse(STANDING_SAME_AS_CYCLE182)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076071Previous700Scoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 071 previous-700 cluster. Mock only."""

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
        self.with_sites = leftover_with_previous_700_076_071(
            self.leftover_sites,
            self.backwards,
        )
        self.without_sites = leftover_without_previous_700_076_071(
            self.leftover_sites,
            self.backwards,
        )
        self.no_backward = leftover_sites_without_backward(
            self.leftover_sites,
            self.previous,
        )
        self.matching_previous_4grams = leftover_previous_4grams(
            self.i_sides,
            self.with_sites,
            GRAM2,
        )
        self.n_leftover = len(self.leftover_sites)
        self.n_with = len(self.with_sites)
        self.n_without = len(self.without_sites)
        self.n_no_backward = len(self.no_backward)
        self.claim_holds = i_leftover_076_071_exactly_3_previous_700_076_071(
            self.n_with,
        )

    def test_tokens_and_sites_are_cycle_172_leftover_not_retuned(self):
        """2-gram and leftover 34 stay the cycle-190/172/171 locks."""
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM3_BACKWARD, ("700", "076", "071"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
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
        self.assertEqual(prior_190["previous_stem_frequency"][0]["previous_stem"], STEM_700)
        self.assertEqual(prior_190["previous_stem_frequency"][0]["count"], 3)
        prior_182 = self.survey["i_leftover_076_071_forward_700"]
        self.assertEqual(prior_182["cycle"], 182)
        self.assertEqual(tuple(prior_182["forward_3gram"]), CYCLE182_GRAM3_FORWARD)
        self.assertEqual(prior_182["N_with_forward_076_071_700"], 3)
        self.assertTrue(prior_182["i_leftover_076_071_exactly_3_forward_076_071_700"])
        prior_172 = self.survey["i_2gram_076_071_inside_family"]
        self.assertEqual(prior_172["cycle"], 172)
        self.assertEqual(prior_172["N_leftover"], 34)
        self.assertFalse(prior_172["i_2gram_076_071_all_inside_leftover_n4_family"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_172["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE172_PREVIOUS_4GRAMS],
            prior_172["leftover_previous_4grams"],
        )
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
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_3_of_34_and_hypothesis_n_3_holds(self):
        """N_leftover=34, N_with=3, N_without=31. Claim holds."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 34)
        self.assertEqual(self.n_with, STANDING_N_WITH_PREVIOUS_700_076_071)
        self.assertEqual(STANDING_N_WITH_PREVIOUS_700_076_071, 3)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 31)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(self.n_with + self.n_without, self.n_leftover)
        self.assertEqual(HYPOTHESIS_N, 3)
        self.assertTrue(i_leftover_076_071_exactly_3_previous_700_076_071(self.n_with))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_071_EXACTLY_3_PREVIOUS_700_076_071,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_071_EXACTLY_3_PREVIOUS_700_076_071)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_exactly_3_previous_700_076_071")
        self.assertEqual(self.previous_4grams, CYCLE172_PREVIOUS_4GRAMS)
        self.assertEqual(self.n_leftover, 34)
        if self.n_with != 3:
            self.fail("measured N_with_previous_700_076_071 drifted from 3")
        if self.n_leftover != 34:
            self.fail("leftover N drifted from 34")
        self.assertFalse(STANDING_SAME_AS_CYCLE190)
        self.assertFalse(STANDING_SAME_AS_CYCLE182)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_sites_and_previous_4grams(self):
        """Three leftover sites share 700 076 071; previous 4-grams stay distinct."""
        self.assertEqual(self.with_sites, STANDING_MATCHING_SITES)
        self.assertEqual(self.without_sites, STANDING_WITHOUT_SITES)
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia1", 163), ("090", "700", "076", "071")),
            ((SIDE_IA, "Ia2", 51), ("999", "700", "076", "071")),
            ((SIDE_IA, "Ia13", 128), ("040", "700", "076", "071")),
        )
        for (site, prev4), (want_site, want_prev4) in zip(
            zip(self.with_sites, self.matching_previous_4grams, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N2]), GRAM3_BACKWARD)
            self.assertEqual(stems[index - 1], STEM_700)
            self.assertEqual(site_previous_stem(stems, index, GRAM2), STEM_700)
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), GRAM3_BACKWARD)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev4)
            self.assertEqual(prev4, want_prev4)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, STANDING_INSIDE_SITES)
        self.assertEqual(len(set(STANDING_MATCHING_PREVIOUS_4GRAMS)), 3)
        for site in STANDING_WITHOUT_SITES:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            back = site_backward_3gram(stems, index, GRAM2)
            self.assertIsNotNone(back)
            self.assertNotEqual(back, GRAM3_BACKWARD)
            self.assertNotEqual(back[0], STEM_700)
        near_stems = line_stems_for_site(
            self.i_sides,
            STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,
        )
        near_index = STANDING_NEAR_MISS_LEFTOVER_700_604_SITE[2]
        self.assertEqual(
            site_previous_4gram(near_stems, near_index, GRAM2),
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
        )
        self.assertEqual(site_previous_stem(near_stems, near_index, GRAM2), "604")
        self.assertIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, self.without_sites)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, self.with_sites)
        for site, nxt in zip(CYCLE182_MATCHING_SITES, CYCLE182_MATCHING_NEXT_4GRAMS):
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), CYCLE182_GRAM3_FORWARD)
            self.assertEqual(nxt[:3], CYCLE182_GRAM3_FORWARD)
            if site == (SIDE_IA, "Ia1", 163):
                self.assertIn(site, self.with_sites)
                self.assertEqual(
                    site_backward_3gram(stems, index, GRAM2),
                    GRAM3_BACKWARD,
                )
            else:
                self.assertIn(site, self.without_sites)
                self.assertNotIn(site, self.with_sites)
                self.assertNotEqual(
                    site_backward_3gram(stems, index, GRAM2),
                    GRAM3_BACKWARD,
                )
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, self.with_sites)
            self.assertNotIn(site, self.leftover_sites)
            inside_stems = line_stems_for_site(self.i_sides, site)
            inside_index = site[2]
            inside_back = site_backward_3gram(inside_stems, inside_index, GRAM2)
            self.assertNotEqual(inside_back, GRAM3_BACKWARD)
        inside_stems = line_stems_for_site(
            self.i_sides,
            STANDING_NEAR_MISS_INSIDE_700_071_SITE,
        )
        inside_index = STANDING_NEAR_MISS_INSIDE_700_071_SITE[2]
        self.assertEqual(
            site_previous_4gram(inside_stems, inside_index, GRAM2),
            STANDING_NEAR_MISS_INSIDE_700_071_PREVIOUS_4GRAM,
        )
        self.assertEqual(site_previous_stem(inside_stems, inside_index, GRAM2), "071")
        self.assertNotIn(STANDING_NEAR_MISS_INSIDE_700_071_SITE, self.with_sites)
        measured_local = leftover_local_4grams(self.i_sides, self.leftover_sites)
        for (site, prev4, _nxt), back in zip(
            measured_local,
            self.backwards,
            strict=True,
        ):
            self.assertIsNotNone(prev4)
            self.assertEqual(prev4[1:], back)
            self.assertEqual(prev4[2:], GRAM2)
            if site in STANDING_MATCHING_SITES:
                self.assertEqual(back, GRAM3_BACKWARD)
            else:
                self.assertNotEqual(back, GRAM3_BACKWARD)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_190_172_171_scoreboards_still_compute(self):
        """Cycle 190 N_distinct=28, 172 leftover-34, and 171 I-only 43/0 stay."""
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
        prior_182 = TestMamariILeftover076071Forward700Scoreboard()
        prior_182.setUp()
        prior_182.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_182.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-191 leftover previous-700 lock."""
        lock = self.survey["i_leftover_076_071_previous_700"]
        self.assertEqual(lock["cycle"], 191)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["hypothesis_n"], 3)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["previous_stem"], STEM_700)
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
        self.assertEqual(
            lock["N_with_previous_700_076_071"],
            STANDING_N_WITH_PREVIOUS_700_076_071,
        )
        self.assertEqual(lock["N_with_previous_700_076_071"], 3)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 31)
        self.assertEqual(lock["N_no_backward"], STANDING_N_NO_BACKWARD)
        self.assertEqual(lock["N_no_backward"], 0)
        self.assertEqual(lock["no_backward_sites"], [])
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_local_4grams"],
            matching_leftover_local_4gram_rows(
                STANDING_MATCHING_SITES,
                STANDING_MATCHING_PREVIOUS_4GRAMS,
            ),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["without_sites"]),
            STANDING_WITHOUT_SITES,
        )
        self.assertEqual(lock["inside_previous_700_sites"], [])
        self.assertEqual(
            tuple(lock["near_miss_leftover_700_604_site"]),
            STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,
        )
        self.assertEqual(
            tuple(lock["near_miss_leftover_700_604_previous_4gram"]),
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
        )
        self.assertEqual(
            tuple(lock["near_miss_inside_700_071_site"]),
            STANDING_NEAR_MISS_INSIDE_700_071_SITE,
        )
        self.assertEqual(
            tuple(lock["near_miss_inside_700_071_previous_4gram"]),
            STANDING_NEAR_MISS_INSIDE_700_071_PREVIOUS_4GRAM,
        )
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["near_miss_700_604_does_not_count"])
        self.assertTrue(lock["cycle182_forward_700_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE182_MATCHING_SITES],
            lock["cycle182_matching_sites"],
        )
        self.assertEqual(lock["cycle182_N_with_forward_076_071_700"], 3)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_071_exactly_3_previous_700_076_071"])
        self.assertEqual(
            lock["i_leftover_076_071_exactly_3_previous_700_076_071"],
            STANDING_I_LEFTOVER_076_071_EXACTLY_3_PREVIOUS_700_076_071,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle190"])
        self.assertFalse(lock["same_as_cycle182"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["other_leftover_n4_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_700_unchanged"])
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
        self.assertEqual(self.survey["i_leftover_076_071_forward_700"]["cycle"], 182)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_700"][
                "i_leftover_076_071_exactly_3_forward_076_071_700"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["cycle"], 172)
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_leftover"], 34)
        self.assertFalse(
            self.survey["i_2gram_076_071_inside_family"][
                "i_2gram_076_071_all_inside_leftover_n4_family"
            ]
        )
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


class TestMamariILeftover076071Previous700ImageSnapshot(unittest.TestCase):
    """Cycle 191 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
