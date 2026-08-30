"""I's cycle-210 leftover 2-gram previous 720 cluster lock.

Cycle 211 text-search lock. Uses already-vendored A–V and the
cycle-210 leftover I sites of 2-gram 076 070 (the I sites that
are not 090-prefixed 090 076 070). Does not retune that 2-gram,
those leftover sites, the cycle-207 8 I 090 076 070 sites, or
the leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished Ib
is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each leftover I site, whether the previous token immediately
before 076 070 is 720 (backward 3-gram 720 076 070; the local
previous 4-gram ends with 720 076 070). Start-of-line is
no-backward. Cycle 210 leftover previous-stem N_leftover=11
N_distinct=9, cycle 209 extra 090 076 070 4-grams I-only hapax
1/0 x3, cycle 208 leftover 4-gram 999 090 076 070 I-only 5/0,
cycle 207 090 076 070 8/1 loss, cycle 206 076 070 19/5 loss,
and cycle 171 076 071 I-only 43/0 stay. The 8 I 090 076 070
sites do not count as leftover (none of them is 720 076 070).
Off-I 076 070 sites do not count as leftover I. 076 071 is a
different 2-gram. Cycle 191 leftover 076 071 previous 700 is
a different 2-gram and does not count.

Hypothesis N=3: exactly 3 of the leftover I 076 070 sites
share previous 3-gram 720 076 070. Do not assume 3; measure.
Measured: N_leftover=11, N_share=3 at Ia7[63] 069 720 076 070,
Ia8[172] 053 720 076 070, Ia9[120] 999 720 076 070;
N_without=8; N_no_backward=0. Claim that can lose:
i_leftover_076_070_previous_720. True only if N_share=3 and
N_leftover=11. The claim is true. Same claim-shape as cycle
191 (leftover 076 071 exactly 3 share previous 700 076 071).
Do not retune.

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
from tests.test_mamari_i_4gram_999_090_076_070_i_only_scoreboard import (
    STANDING_I_4GRAM_999_090_076_070_I_ONLY as CYCLE208_I_ONLY,
    STANDING_N_I as CYCLE208_N_I,
    STANDING_N_OFF_I as CYCLE208_N_OFF_I,
    TestMamariI4gram999090076070IOnlyScoreboard,
)
from tests.test_mamari_i_extra_090_076_070_4grams_i_only_scoreboard import (
    STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY as CYCLE209_I_ONLY,
    STANDING_N_I_036 as CYCLE209_N_I_036,
    STANDING_N_I_161 as CYCLE209_N_I_161,
    STANDING_N_I_400 as CYCLE209_N_I_400,
    STANDING_N_OFF_I_036 as CYCLE209_N_OFF_I_036,
    STANDING_N_OFF_I_161 as CYCLE209_N_OFF_I_161,
    STANDING_N_OFF_I_400 as CYCLE209_N_OFF_I_400,
    TestMamariIExtra0900760704gramsIOnlyScoreboard,
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
from tests.test_mamari_i_leftover_076_071_previous_700_scoreboard import (
    GRAM3_BACKWARD as CYCLE191_GRAM3_BACKWARD,
    STANDING_I_LEFTOVER_076_071_EXACTLY_3_PREVIOUS_700_076_071 as CYCLE191_CLAIM,
    STANDING_MATCHING_SITES as CYCLE191_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_700_076_071 as CYCLE191_N_WITH,
    TestMamariILeftover076071Previous700Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    leftover_backward_3grams,
    leftover_previous_4grams,
    leftover_previous_stems,
    leftover_sites_without_backward,
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
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

HYPOTHESIS_N = 3
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STEM_720 = "720"
GRAM3_BACKWARD = ("720", "076", "070")
STANDING_N_I = CYCLE206_N_I
STANDING_N_090_PREFIXED = CYCLE210_N_090_PREFIXED
STANDING_N_LEFTOVER = 11
STANDING_N_SHARE = 3
STANDING_N_WITH_PREVIOUS_720_076_070 = 3
STANDING_N_WITHOUT = 8
STANDING_N_NO_BACKWARD = 0
STANDING_NO_BACKWARD_SITES = ()
STANDING_PREFIXED_PREVIOUS_720_SITES = ()
STANDING_NEAR_MISS_LEFTOVER_090_099_SITE = (SIDE_IA, "Ia5", 61)
STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM = ("090", "099", "076", "070")
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia7", 63),
    (SIDE_IA, "Ia8", 172),
    (SIDE_IA, "Ia9", 120),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("069", "720", "076", "070"),
    ("053", "720", "076", "070"),
    ("999", "720", "076", "070"),
)
STANDING_WITHOUT_SITES = (
    (SIDE_IA, "Ia1", 79),
    (SIDE_IA, "Ia1", 141),
    (SIDE_IA, "Ia2", 125),
    (SIDE_IA, "Ia3", 123),
    (SIDE_IA, "Ia5", 61),
    (SIDE_IA, "Ia6", 144),
    (SIDE_IA, "Ia13", 120),
    (SIDE_IA, "Ia13", 140),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_070_previous_720"
STANDING_I_LEFTOVER_076_070_PREVIOUS_720 = True
STANDING_RESULT = "i_leftover_076_070_previous_720"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE210 = False
STANDING_SAME_AS_CYCLE191 = False
STANDING_090_PREFIXED_DOES_NOT_COUNT = True
STANDING_OFF_I_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_CYCLE191_PREVIOUS_700_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_090_099_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_with_previous_720_076_070(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
    needle: tuple[str, ...] = GRAM3_BACKWARD,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites whose backward 3-gram is 720 076 070."""
    return tuple(
        site
        for site, back in zip(sites, backwards, strict=True)
        if back == needle
    )


def leftover_without_previous_720_076_070(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
    needle: tuple[str, ...] = GRAM3_BACKWARD,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that have a previous stem other than 720, or none."""
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


def i_leftover_076_070_previous_720(
    n_share: int,
    n_leftover: int,
    expected_share: int = HYPOTHESIS_N,
    expected_leftover: int = STANDING_N_LEFTOVER,
) -> bool:
    """True iff N_share=3 and N_leftover=11."""
    return n_share == expected_share and n_leftover == expected_leftover


class TestILeftover076070Previous720Helpers(unittest.TestCase):
    """Helpers on leftover I 076 070 previous 720. No CV, no LLM."""

    def test_previous_requires_stem_720_before_2gram(self):
        """A previous 720 is a 3-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE206_GRAM2)
        self.assertEqual(GRAM2, CYCLE205_GRAM2)
        self.assertEqual(GRAM3_BACKWARD, ("720", "076", "070"))
        self.assertEqual(GRAM3_BACKWARD[1:], GRAM2)
        self.assertEqual(GRAM3_BACKWARD[0], STEM_720)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_720 = ["069", "720", "076", "070", "720", "076"]
        self.assertEqual(site_previous_stem(has_720, 2, GRAM2), STEM_720)
        self.assertEqual(site_backward_3gram(has_720, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_720, 2, GRAM2),
            ("069", "720", "076", "070"),
        )
        other_prev = ["000", "090", "076", "070", "004", "004"]
        self.assertEqual(site_previous_stem(other_prev, 2, GRAM2), PREFIXED_STEM)
        self.assertNotEqual(site_backward_3gram(other_prev, 2, GRAM2), GRAM3_BACKWARD)
        near_miss_099 = ["090", "099", "076", "070", "513", "001"]
        self.assertEqual(site_previous_stem(near_miss_099, 2, GRAM2), "099")
        self.assertEqual(
            site_previous_4gram(near_miss_099, 2, GRAM2),
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
        )
        self.assertNotEqual(site_backward_3gram(near_miss_099, 2, GRAM2), GRAM3_BACKWARD)
        start_of_line = ["076", "070", "090", "606"]
        self.assertIsNone(site_previous_stem(start_of_line, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(start_of_line, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(start_of_line, 0, GRAM2))
        mismatch_071 = ["720", "076", "071"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        self.assertIsNone(site_backward_3gram(mismatch_071, 1, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_3_of_11_can_fail(self):
        """Boolean is True only when N_share=3 and N_leftover=11."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_070_previous_720(3, 11))
        self.assertFalse(i_leftover_076_070_previous_720(0, 11))
        self.assertFalse(i_leftover_076_070_previous_720(2, 11))
        self.assertFalse(i_leftover_076_070_previous_720(4, 11))
        self.assertFalse(i_leftover_076_070_previous_720(1, 11))
        self.assertFalse(i_leftover_076_070_previous_720(3, 10))
        self.assertFalse(i_leftover_076_070_previous_720(3, 12))
        self.assertFalse(i_leftover_076_070_previous_720(3, 0))
        self.assertFalse(i_leftover_076_070_previous_720(11, 11))
        self.assertFalse(i_leftover_076_070_previous_720(9, 11))
        planted = STANDING_MATCHING_SITES + (STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,)
        planted_backs = (GRAM3_BACKWARD,) * 4
        self.assertEqual(
            leftover_with_previous_720_076_070(planted, planted_backs),
            planted,
        )
        self.assertFalse(i_leftover_076_070_previous_720(len(planted), 11))
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_070_previous_720")
        self.assertTrue(STANDING_I_LEFTOVER_076_070_PREVIOUS_720)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_070_PREVIOUS_720,
            HYPOTHESIS_N == STANDING_N_SHARE
            and STANDING_N_LEFTOVER == CYCLE210_N_LEFTOVER,
        )
        self.assertEqual(STANDING_N_SHARE + STANDING_N_WITHOUT, 11)
        self.assertEqual(STANDING_N_SHARE, STANDING_N_WITH_PREVIOUS_720_076_070)
        self.assertEqual(provider.get_call_history(), [])

    def test_prefixed_off_i_and_076_071_do_not_count(self):
        """090-prefixed I, off-I 076 070, leftover n=4, and 076 071 are not this cluster."""
        provider = MockProvider()
        self.assertEqual(STANDING_PREFIXED_PREVIOUS_720_SITES, ())
        for site in STANDING_PREFIXED_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertEqual(len(STANDING_PREFIXED_I_SITES), STANDING_N_090_PREFIXED)
        self.assertEqual(STANDING_N_090_PREFIXED, 8)
        for site in CYCLE206_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertEqual(len(CYCLE206_OFF_I_SITES), CYCLE206_N_OFF_I)
        self.assertEqual(CYCLE206_N_OFF_I, 5)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_LEFTOVER_SITES)
        self.assertIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_WITHOUT_SITES)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_MATCHING_SITES)
        self.assertEqual(
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM[1:],
            ("099", "076", "070"),
        )
        self.assertTrue(STANDING_NEAR_MISS_090_099_DOES_NOT_COUNT)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertNotEqual(GRAM3_BACKWARD, CYCLE191_GRAM3_BACKWARD)
        self.assertEqual(CYCLE191_GRAM3_BACKWARD, ("700", "076", "071"))
        self.assertEqual(CYCLE191_N_WITH, 3)
        self.assertTrue(CYCLE191_CLAIM)
        for site in CYCLE191_MATCHING_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE191_PREVIOUS_700_DOES_NOT_COUNT)
        self.assertEqual(CYCLE205_MATCHING_LEFTOVERS, (("999", "090", "076", "070"),))
        self.assertFalse(is_contiguous_substring(GRAM3_BACKWARD, CYCLE205_MATCHING_LEFTOVERS[0]))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_999_090_076_071))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_SAME_AS_CYCLE210)
        self.assertFalse(STANDING_SAME_AS_CYCLE191)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076070Previous720Scoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 070 previous-720 cluster. Mock only."""

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
        self.with_sites = leftover_with_previous_720_076_070(
            self.leftover_sites,
            self.backwards,
        )
        self.without_sites = leftover_without_previous_720_076_070(
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
        self.n_i = len(self.i_sites)
        self.n_prefixed = len(self.measured_prefixed)
        self.n_leftover = len(self.measured_leftover)
        self.n_share = len(self.with_sites)
        self.n_without = len(self.without_sites)
        self.n_no_backward = len(self.no_backward)
        self.claim_holds = i_leftover_076_070_previous_720(
            self.n_share,
            self.n_leftover,
        )

    def test_tokens_and_sites_are_cycle_210_leftover_not_retuned(self):
        """2-gram and leftover 11 stay the cycle-210/207/206 locks."""
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
        self.assertEqual(prior_210["previous_stem_frequency"][0]["previous_stem"], STEM_720)
        self.assertEqual(prior_210["previous_stem_frequency"][0]["count"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in prior_210["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE210_PREVIOUS_4GRAMS],
            prior_210["per_site_previous_4grams"],
        )
        prior_209 = self.survey["i_extra_090_076_070_4grams_i_only"]
        self.assertEqual(prior_209["cycle"], 209)
        self.assertTrue(prior_209["i_extra_090_076_070_4grams_i_only"])
        self.assertTrue(CYCLE209_I_ONLY)
        self.assertEqual(prior_209["N_I_036"], CYCLE209_N_I_036)
        self.assertEqual(prior_209["N_off_I_036"], CYCLE209_N_OFF_I_036)
        self.assertEqual(prior_209["N_I_161"], CYCLE209_N_I_161)
        self.assertEqual(prior_209["N_off_I_161"], CYCLE209_N_OFF_I_161)
        self.assertEqual(prior_209["N_I_400"], CYCLE209_N_I_400)
        self.assertEqual(prior_209["N_off_I_400"], CYCLE209_N_OFF_I_400)
        self.assertEqual(prior_209["N_I_036"], 1)
        self.assertEqual(prior_209["N_off_I_036"], 0)
        prior_208 = self.survey["i_4gram_999_090_076_070_i_only"]
        self.assertEqual(prior_208["cycle"], 208)
        self.assertTrue(prior_208["i_4gram_999_090_076_070_i_only"])
        self.assertTrue(CYCLE208_I_ONLY)
        self.assertEqual(prior_208["N_I"], CYCLE208_N_I)
        self.assertEqual(prior_208["N_I"], 5)
        self.assertEqual(prior_208["N_off_I"], CYCLE208_N_OFF_I)
        self.assertEqual(prior_208["N_off_I"], 0)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertEqual(prior_207["N_I"], CYCLE207_N_I)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(prior_207["N_off_I"], 1)
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
        prior_191 = self.survey["i_leftover_076_071_previous_700"]
        self.assertEqual(prior_191["cycle"], 191)
        self.assertEqual(prior_191["N_with_previous_700_076_071"], 3)
        self.assertTrue(prior_191["i_leftover_076_071_exactly_3_previous_700_076_071"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_3_of_11_and_hypothesis_n_3_holds(self):
        """N_leftover=11, N_share=3, N_without=8. Claim holds."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 11)
        self.assertEqual(self.n_share, STANDING_N_SHARE)
        self.assertEqual(STANDING_N_SHARE, 3)
        self.assertEqual(self.n_share, STANDING_N_WITH_PREVIOUS_720_076_070)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 8)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(self.n_share + self.n_without, self.n_leftover)
        self.assertEqual(HYPOTHESIS_N, 3)
        self.assertTrue(i_leftover_076_070_previous_720(self.n_share, self.n_leftover))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_070_PREVIOUS_720,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_070_PREVIOUS_720)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_070_previous_720")
        self.assertEqual(self.previous_4grams, CYCLE210_PREVIOUS_4GRAMS)
        self.assertEqual(self.n_leftover, 11)
        if self.n_share != 3:
            self.fail("measured N_share drifted from 3")
        if self.n_leftover != 11:
            self.fail("leftover N drifted from 11")
        if self.n_i != 19 or self.n_prefixed != 8:
            self.fail("nested cycle 206/207 counts drifted; leftover cannot be trusted")
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 19)
        self.assertEqual(self.n_prefixed, STANDING_N_090_PREFIXED)
        self.assertEqual(STANDING_N_090_PREFIXED, 8)
        self.assertFalse(STANDING_SAME_AS_CYCLE210)
        self.assertFalse(STANDING_SAME_AS_CYCLE191)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_sites_and_previous_4grams(self):
        """Three leftover sites share 720 076 070; previous 4-grams stay distinct."""
        self.assertEqual(self.with_sites, STANDING_MATCHING_SITES)
        self.assertEqual(self.without_sites, STANDING_WITHOUT_SITES)
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia7", 63), ("069", "720", "076", "070")),
            ((SIDE_IA, "Ia8", 172), ("053", "720", "076", "070")),
            ((SIDE_IA, "Ia9", 120), ("999", "720", "076", "070")),
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
            self.assertEqual(stems[index - 1], STEM_720)
            self.assertEqual(site_previous_stem(stems, index, GRAM2), STEM_720)
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), GRAM3_BACKWARD)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev4)
            self.assertEqual(prev4, want_prev4)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, STANDING_PREFIXED_I_SITES)
        self.assertEqual(len(set(STANDING_MATCHING_PREVIOUS_4GRAMS)), 3)
        for site in STANDING_WITHOUT_SITES:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            back = site_backward_3gram(stems, index, GRAM2)
            self.assertIsNotNone(back)
            self.assertNotEqual(back, GRAM3_BACKWARD)
            self.assertNotEqual(back[0], STEM_720)
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
        self.assertIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, self.without_sites)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, self.with_sites)
        for site in STANDING_PREFIXED_I_SITES:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(stems[index - 1], PREFIXED_STEM)
            self.assertEqual(
                tuple(stems[index - 1 : index + STANDING_N2]),
                CYCLE207_GRAM3,
            )
            self.assertNotEqual(
                site_backward_3gram(stems, index, GRAM2),
                GRAM3_BACKWARD,
            )
            self.assertNotIn(site, self.with_sites)
            self.assertNotIn(site, self.leftover_sites)
        for site in CYCLE206_OFF_I_SITES:
            self.assertNotIn(site, self.with_sites)
            self.assertNotIn(site, self.leftover_sites)
        measured_local = leftover_local_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
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
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_210_208_207_206_and_171_scoreboards_still_compute(self):
        """Cycle 210 N_leftover=11 N_distinct=9, 208 5/0, 207 8/1, 206 19/5, 171 43/0 stay."""
        prior_210 = TestMamariILeftover076070PreviousStemScoreboard()
        prior_210.setUp()
        prior_210.test_counts_9_distinct_previous_stems_and_claim_loses()
        prior_210.test_survey_matches_computed_lock()
        self.assertEqual(prior_210.n_leftover, 11)
        self.assertEqual(prior_210.n_distinct, 9)
        self.assertEqual(CYCLE210_N_LEFTOVER, 11)
        self.assertEqual(CYCLE210_N_DISTINCT, 9)
        prior_209 = TestMamariIExtra0900760704gramsIOnlyScoreboard()
        prior_209.setUp()
        prior_209.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_209.test_survey_matches_computed_lock()
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE208_N_I, 5)
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_191 = TestMamariILeftover076071Previous700Scoreboard()
        prior_191.setUp()
        prior_191.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_191.test_survey_matches_computed_lock()
        self.assertEqual(prior_191.n_with, 3)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-211 leftover previous-720 lock."""
        lock = self.survey["i_leftover_076_070_previous_720"]
        self.assertEqual(lock["cycle"], 211)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(lock["hypothesis_n"], 3)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["previous_stem"], STEM_720)
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
        self.assertEqual(
            leftover_local_4grams(self.i_sides, self.leftover_sites, GRAM2),
            tuple(
                (site, prev, nxt)
                for site, prev, nxt in leftover_local_4grams(
                    self.i_sides,
                    STANDING_LEFTOVER_SITES,
                    GRAM2,
                )
            ),
        )
        self.assertEqual(lock["N_share"], STANDING_N_SHARE)
        self.assertEqual(lock["N_share"], 3)
        self.assertEqual(
            lock["N_with_previous_720_076_070"],
            STANDING_N_WITH_PREVIOUS_720_076_070,
        )
        self.assertEqual(lock["N_with_previous_720_076_070"], 3)
        self.assertEqual(lock["N_share"], lock["N_with_previous_720_076_070"])
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 8)
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
        self.assertEqual(
            tuple(tuple(row) for row in lock["prefixed_i_sites"]),
            STANDING_PREFIXED_I_SITES,
        )
        self.assertEqual(lock["prefixed_previous_720_sites"], [])
        self.assertEqual(
            tuple(lock["near_miss_leftover_090_099_site"]),
            STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
        )
        self.assertEqual(
            tuple(lock["near_miss_leftover_090_099_previous_4gram"]),
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
        )
        self.assertTrue(lock["090_prefixed_does_not_count"])
        self.assertTrue(lock["near_miss_090_099_does_not_count"])
        self.assertTrue(lock["cycle191_previous_700_does_not_count"])
        self.assertEqual(
            [list(site) for site in CYCLE191_MATCHING_SITES],
            lock["cycle191_matching_sites"],
        )
        self.assertEqual(lock["cycle191_N_with_previous_700_076_071"], 3)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_070_previous_720"])
        self.assertEqual(
            lock["i_leftover_076_070_previous_720"],
            STANDING_I_LEFTOVER_076_070_PREVIOUS_720,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle210"])
        self.assertFalse(lock["same_as_cycle191"])
        self.assertTrue(lock["off_i_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_extra_090_076_070_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_700_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["cycle"], 210)
        self.assertEqual(
            self.survey["i_leftover_076_070_previous_stem"]["N_leftover"],
            11,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_previous_stem"]["N_distinct_previous_stems"],
            9,
        )
        self.assertFalse(
            self.survey["i_leftover_076_070_previous_stem"][
                "i_leftover_076_070_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["cycle"], 209)
        self.assertTrue(
            self.survey["i_extra_090_076_070_4grams_i_only"][
                "i_extra_090_076_070_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_I_036"], 1)
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_off_I_036"], 0)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"]["i_4gram_999_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(
            self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_700"]["cycle"], 191)
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_700"][
                "i_leftover_076_071_exactly_3_previous_700_076_071"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariILeftover076070Previous720ImageSnapshot(unittest.TestCase):
    """Cycle 211 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
