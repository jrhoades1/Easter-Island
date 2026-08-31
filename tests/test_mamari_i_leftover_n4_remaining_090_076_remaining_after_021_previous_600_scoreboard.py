"""I's cycle-306 leftover n=4 remaining remaining-after-021 previous-600 lock.

Cycle 307 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–287), leftover n=4 remaining
forward peel (288–301), leftover n=4 remaining unique
previous stem (cycle 302), leftover n=4 remaining exactly 5
share previous 021 (cycle 303), 3-gram 021 090 076 I-only
(cycle 304), leftover n=4 remaining previous-021 4-grams
(cycle 305), leftover n=4 remaining remaining-after-021
unique previous stem (cycle 306), leftover extra remaining-
after-999 previous 600 (cycle 267), 3-gram 600 090 076
I-only (cycle 268), leftover extra 600 090 076 previous
4-grams (cycle 269), or leftover n=4 remaining remaining-
after-057 next 011 (cycle 297). Does not vendor a new
tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or
G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Cycle 306 leftover n=4 remaining remaining-after-021 unique
previous stem HOLDS: unique_max true, G=600 K=2,
N_remaining_after_021=8, N_line_initial=0, N_distinct=7.
G sites Ia2[107]/Ia14[54] (leftover n=4 remaining
600 090 076 011; previous 4-grams 071 600 090 076 /
175 600 090 076). N_remaining after peeling G=6 (hapax
previous stems 999 / 591 / 090 / 076 / 008 / 000).
Unique-max G/K is inventory; this cycle peels 600 as
exact-K. Do not peel remaining-after-600 this cycle. Do not
lock 3-gram 600 090 076 I-only this cycle (already cycle
268). Off-I T sites are not this cycle. 076 071 and 076 070
do not count as this 2-gram. Leftover extra sites do not
count as leftover n=4 remaining.

Hypothesis K=2: leftover n=4 remaining remaining-after-021 I
090 076 sites include exactly 2 that share previous stem 600
(backward 3-gram 600 090 076). Nested-check leftover n=4
remaining N_inside==13, N_line_initial==0, K_021==5,
N_remaining_after_021==8 (do not retune 224/288/302/303).
Nested leftover n=4 remaining 13 / 4 / 9 / 3 / 6 / 2 / 4 /
2 / 2 still computes (do not retune 288–297). Nested
remaining-after-021: N=8 N_line_initial=0 unique_max true
G=600 K=2 N_distinct=7 (do not retune cycle 306). Count
remaining-after-021 leftover n=4 remaining I 090 076 sites
whose previous token is 600. Cycle 306 listed Ia2[107] /
Ia14[54]; measure, do not assume if nested-check differs.
Those two sites are also leftover n=4 remaining remaining-
after-057 next-011 (cycle 297) and leftover extra 090 076
011 extra I (cycle 248). N_remaining_after_600 =
N_remaining_after_021 − K_600. Unique-max previous of
remaining-after-021 is still 600. Claim that can lose:
i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600.
True iff K_600==2 among leftover n=4 remaining remaining-
after-021 I 090 076 and unique-max previous of remaining-
after-021 is still 600. The claim is true. Same claim-shape
as cycle 267 (leftover extra remaining-after-999 exactly 4
share previous 600) and cycle 293 (leftover n=4 remaining
remaining-after-020 exactly 3 share next 087), leftover n=4
remaining remaining-after-021 / previous 600 instead of
leftover extra remaining-after-999 / previous 600. This can
lose if nested-check K differs from 2, if unique-max is no
longer 600, if N_remaining_after_021 != 8, or if the site
list no longer computes. Nested overlap of previous-600
remaining-after-021 sites with leftover extra remaining-
after-999 previous-600 extra I (cycle 268 extra I=2 of
600 090 076), leftover extra 090 076 011 extra I (cycle
248), and leftover n=4 remaining remaining-after-057 next
011 (cycle 297) is Ia2[107]/Ia14[54]; remaining-after-011
sites Ia8[106]/Ia13[17] are previous-021, so they are not
remaining-after-021; record, do not fail K_600 on it.
Nested cycle 306 unique-max true G=600 K=2, cycle 305
previous-021 4-grams I-only N_not_hapax=1, cycle 304 5/0
extra I=0, cycle 303 K_021=5, cycle 288 unique-max G=020
K=4 share-one lost, cycle 224 13/56, and cycle 223 69/3
stay. Do not assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_021_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY as CYCLE305_CLAIM,
    STANDING_N_HAPAX_I_ONLY as CYCLE305_N_HAPAX,
    STANDING_N_I_ONLY as CYCLE305_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE305_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE305_N_NOT_I_ONLY,
    TestMamariI021090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_600011_COVERED,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
    leftover_local_4grams,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_OFF_I,
    STANDING_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_021_090_076_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE304_EXTRA_I_SITES,
    STANDING_I_3GRAM_021_090_076_I_ONLY as CYCLE304_CLAIM,
    STANDING_N_EXTRA as CYCLE304_N_EXTRA,
    STANDING_N_I as CYCLE304_N_I,
    STANDING_N_OFF_I as CYCLE304_N_OFF_I,
    TestMamariI3gram021090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE248_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_011_I_ONLY as CYCLE248_CLAIM,
    STANDING_N_EXTRA as CYCLE248_N_EXTRA,
    STANDING_N_I as CYCLE248_N_I,
    STANDING_N_OFF_I as CYCLE248_N_OFF_I,
    TestMamariI3gram090076011IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_600_090_076_i_only_scoreboard import (
    STANDING_EXTRA_I_090_076_SITES as CYCLE268_EXTRA_I_090_076_SITES,
    STANDING_EXTRA_I_SITES as CYCLE268_EXTRA_I_SITES,
    STANDING_I_3GRAM_600_090_076_I_ONLY as CYCLE268_CLAIM,
    STANDING_N_EXTRA as CYCLE268_N_EXTRA,
    STANDING_N_I as CYCLE268_N_I,
    STANDING_N_OFF_I as CYCLE268_N_OFF_I,
    TestMamariI3gram600090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_600_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_EXACTLY_4_SHARE_PREVIOUS_600 as CYCLE267_CLAIM,
    STANDING_K_600 as CYCLE267_K_600,
    STANDING_MATCHING_SITES as CYCLE267_MATCHING_SITES,
    TestMamariILeftoverExtra090076RemainingAfter999Previous600Scoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE288_N_INSIDE,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_previous_021_scoreboard import (
    GRAM3_BACKWARD as GRAM3_NESTED_021,
    STANDING_G as CYCLE303_G,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021 as CYCLE303_CLAIM,
    STANDING_K_021 as CYCLE303_K_021,
    STANDING_MATCHING_SITES as CYCLE303_MATCHING_SITES,
    STANDING_NESTED_LEFTOVER_N4_REMAINING as CYCLE303_NESTED,
    STANDING_N_REMAINING_AFTER_021 as CYCLE303_N_REMAINING_AFTER_021,
    STANDING_REMAINING_AFTER_021_SITES as CYCLE303_REMAINING_AFTER_021_SITES,
    leftover_n4_remaining_with_previous_021,
    leftover_n4_remaining_without_previous_021,
    TestMamariILeftoverN4Remaining090076Previous021Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_previous_stem_scoreboard import (
    leftover_n4_remaining_backward_3grams,
    leftover_n4_remaining_g_overlap_sites,
    leftover_n4_remaining_previous_4grams,
    leftover_n4_remaining_previous_stems,
    leftover_n4_remaining_sites_with_previous,
    leftover_n4_remaining_sites_without_previous,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_next_stem_scoreboard import (
    STANDING_K_011,
    STANDING_K_020,
    STANDING_K_057,
    STANDING_K_087,
    STANDING_N_REMAINING_AFTER_011,
    STANDING_N_REMAINING_AFTER_020,
    STANDING_N_REMAINING_AFTER_057,
    STANDING_N_REMAINING_AFTER_087,
    leftover_n4_remaining_remaining_after_011_nested_counts_hold,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_forward_087_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087 as CYCLE293_CLAIM,
    STANDING_K_087 as CYCLE293_K_087,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS,
    STANDING_G as CYCLE306_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE306_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM as CYCLE306_CLAIM,
    STANDING_K as CYCLE306_K,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE306_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE306_MATCHING_SITES,
    STANDING_NESTED_LEFTOVER_N4_REMAINING as CYCLE306_NESTED,
    STANDING_N_DISTINCT as CYCLE306_N_DISTINCT,
    STANDING_N_HAPAX as CYCLE306_N_HAPAX,
    STANDING_N_LINE_INITIAL as CYCLE306_N_LINE_INITIAL,
    STANDING_N_REMAINING_AFTER_021 as CYCLE306_N_REMAINING,
    STANDING_N_WITHOUT_G as CYCLE306_N_WITHOUT_G,
    STANDING_REMAINING_PREVIOUS_STEMS as CYCLE306_REMAINING_PREVIOUS_STEMS,
    STANDING_REMAINING_SITES as CYCLE306_REMAINING_SITES,
    leftover_n4_remaining_remaining_after_021,
    leftover_n4_remaining_remaining_after_021_nested_counts_hold,
    leftover_n4_remaining_remaining_after_021_previous_stems,
    leftover_n4_remaining_remaining_after_021_with_g,
    leftover_n4_remaining_remaining_after_021_with_previous,
    leftover_n4_remaining_remaining_after_021_without_g,
    leftover_n4_remaining_remaining_after_021_without_previous,
    matching_leftover_n4_remaining_remaining_after_021_local_4gram_rows,
    select_remaining_after_021_g,
    TestMamariILeftoverN4Remaining090076RemainingAfter021PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011 as CYCLE297_CLAIM,
    STANDING_MATCHING_SITES as CYCLE297_MATCHING_SITES,
    STANDING_REMAINING_AFTER_011_SITES as CYCLE297_REMAINING_AFTER_011_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter057Forward011Scoreboard,
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

HYPOTHESIS_K = 2
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_BACKWARD = ("600", "090", "076")
GRAM3_NESTED_021_TOKENS = ("021", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS_INSIDE = 13
STANDING_N_LINE_INITIAL_INSIDE = 0
STANDING_K_021 = 5
STANDING_N_REMAINING_AFTER_021 = 8
STANDING_N_WITH_PREVIOUS = 8
STANDING_N_LINE_INITIAL = 0
STANDING_N_NO_PREVIOUS = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT = 7
STANDING_N_HAPAX = 6
STANDING_K = 2
STANDING_K_600 = 2
STANDING_G = "600"
STANDING_N_WITHOUT = 6
STANDING_N_REMAINING_AFTER_600 = 6
STANDING_REMAINING_AFTER_600_HAPAX_STEMS = (
    "999",
    "591",
    "090",
    "076",
    "008",
    "000",
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia14", 54),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("071", "600", "090", "076"),
    ("175", "600", "090", "076"),
)
STANDING_REMAINING_AFTER_600_SITES = (
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
    (SIDE_IA, "Ia12", 83),
)
STANDING_REMAINING_AFTER_600_PREVIOUS_STEMS = (
    "591",
    "076",
    "090",
    "000",
    "999",
    "008",
)
STANDING_MATCHING_EQUALS_CYCLE306_G_SITES = True
STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I = True
STANDING_MATCHING_EQUALS_CYCLE268_EXTRA_I_090_076 = True
STANDING_MATCHING_EQUALS_CYCLE297_NEXT_011 = True
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_UNIQUE_MAX_STILL_600 = True
STANDING_OVERLAP_CYCLE248_EXTRA_I = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia14", 54),
)
STANDING_OVERLAP_CYCLE268_EXTRA_I = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia14", 54),
)
STANDING_OVERLAP_CYCLE297_NEXT_011 = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia14", 54),
)
STANDING_OVERLAP_CYCLE267_PREVIOUS_600 = ()
STANDING_OVERLAP_REMAINING_AFTER_011 = ()
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600"
)
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_EXACTLY_2_SHARE_PREVIOUS_600 = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_021_previous_600"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE267 = False
STANDING_SAME_AS_CYCLE268 = False
STANDING_SAME_AS_CYCLE293 = False
STANDING_SAME_AS_CYCLE297 = False
STANDING_SAME_AS_CYCLE303 = False
STANDING_SAME_AS_CYCLE306 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_3GRAM_600_090_076_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_REMAINING_AFTER_600 = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_600_NOT_LOCKED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_PREVIOUS_600_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_600_090_076_PREVIOUS_4GRAMS_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_057_NEXT_011_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_NESTED_LEFTOVER_N4_REMAINING = (13, 4, 9, 3, 6, 2, 4, 2, 2)


def leftover_n4_remaining_remaining_after_021_with_previous_600(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-021 sites whose previous token is 600."""
    return leftover_n4_remaining_remaining_after_021_with_g(
        sites,
        previous_stems,
        stem=stem,
        locked=locked,
    )


def leftover_n4_remaining_remaining_after_021_without_previous_600(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-021 sites whose previous token is not 600."""
    return leftover_n4_remaining_remaining_after_021_without_g(
        sites,
        previous_stems,
        stem=stem,
        locked=locked,
    )


def matching_equals_cycle306_g_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle306_g_sites: tuple[tuple[str, str, int], ...] = CYCLE306_MATCHING_SITES,
) -> bool:
    """True iff remaining-after-021 previous-600 sites equal the cycle-306 G set."""
    return matching_sites == cycle306_g_sites


def i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
    k: int,
    unique: bool,
    g: str | None,
    n_remaining: int = STANDING_N_REMAINING_AFTER_021,
    expected: int = HYPOTHESIS_K,
    expected_g: str = STANDING_G,
    expected_remaining: int = STANDING_N_REMAINING_AFTER_021,
) -> bool:
    """True iff K_600 equals 2, unique-max previous is still 600, and remaining-after-021 is 8."""
    return (
        k == expected
        and unique
        and g == expected_g
        and n_remaining == expected_remaining
    )


class TestILeftoverN4Remaining090076RemainingAfter021Previous600Helpers(
    unittest.TestCase
):
    """Helpers on leftover n=4 remaining remaining-after-021 previous 600. No CV, no LLM."""

    def test_previous_600_requires_stem_before_2gram_and_not_021(self):
        """Previous stem 600 is 600 090 076; previous 021 is not remaining-after-021."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_021, ("021", "090", "076"))
        self.assertEqual(GRAM3_NESTED_021_TOKENS, GRAM3_NESTED_021)
        self.assertEqual(GRAM3_BACKWARD[1:], GRAM2)
        self.assertEqual(LOCKED_PREVIOUS_STEMS, ("021",))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_600 = ["071", "600", "090", "076", "011"]
        self.assertEqual(site_previous_stem(has_600, 2, GRAM2), "600")
        self.assertEqual(site_backward_3gram(has_600, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_600, 2, GRAM2),
            ("071", "600", "090", "076"),
        )
        has_021 = ["600", "021", "090", "076"]
        self.assertEqual(site_previous_stem(has_021, 2, GRAM2), "021")
        self.assertNotEqual(site_previous_stem(has_021, 2, GRAM2), "600")
        other_prev = ["093", "591", "090", "076"]
        self.assertEqual(site_previous_stem(other_prev, 2, GRAM2), "591")
        self.assertNotEqual(site_backward_3gram(other_prev, 2, GRAM2), GRAM3_BACKWARD)
        one_token_before = ["600", "090", "076"]
        self.assertEqual(site_previous_stem(one_token_before, 1, GRAM2), "600")
        self.assertEqual(site_backward_3gram(one_token_before, 1, GRAM2), GRAM3_BACKWARD)
        self.assertIsNone(site_previous_4gram(one_token_before, 1, GRAM2))
        line_initial = ["090", "076", "011"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        mismatch_071 = ["600", "076", "071", "090"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        mismatch_070 = ["600", "076", "070", "090"]
        self.assertIsNone(site_previous_stem(mismatch_070, 1, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
        )
        planted_stems = ("600", "021", None, "999")
        self.assertEqual(
            leftover_n4_remaining_remaining_after_021_with_previous_600(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_021_without_previous_600(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[3],),
        )
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_3GRAM_600_090_076_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when K=2, unique-max G is 600, and remaining-after-021 is 8."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                2, True, "600", 8
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                0, True, "600", 8
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                1, True, "600", 8
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                3, True, "600", 8
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                4, True, "600", 8
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                5, True, "600", 8
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                2, False, "600", 8
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                2, True, "999", 8
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                2, True, "600", 7
            )
        )
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 15),)
        planted_stems = ("600",) * 3
        self.assertEqual(
            leftover_n4_remaining_remaining_after_021_with_previous_600(
                planted,
                planted_stems,
            ),
            planted,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                len(planted), True, "600", 8
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_EXACTLY_2_SHARE_PREVIOUS_600
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_EXACTLY_2_SHARE_PREVIOUS_600,
            HYPOTHESIS_K == STANDING_K_600 and STANDING_UNIQUE_MAX_STILL_600,
        )
        self.assertEqual(
            STANDING_K_600 + STANDING_N_REMAINING_AFTER_600,
            STANDING_N_REMAINING_AFTER_021,
        )
        self.assertEqual(2 + 6, 8)
        self.assertEqual(STANDING_K_021 + STANDING_N_REMAINING_AFTER_021, STANDING_N_INSIDE)
        self.assertEqual(5 + 8, 13)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle306_set_and_overlap_can_diverge(self):
        """Cycle-306 G-site equality can fail; overlap does not make K_600 lose."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle306_g_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE306_G_SITES)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle306_g_set(planted))
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                len(planted), True, "600", 8
            )
        )
        self.assertEqual(STANDING_OVERLAP_CYCLE248_EXTRA_I, CYCLE248_EXTRA_I_SITES)
        self.assertEqual(STANDING_OVERLAP_CYCLE268_EXTRA_I, CYCLE268_EXTRA_I_090_076_SITES)
        self.assertEqual(STANDING_OVERLAP_CYCLE297_NEXT_011, CYCLE297_MATCHING_SITES)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_600)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_600_NOT_LOCKED)
        self.assertTrue(STANDING_3GRAM_600_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE267)
        self.assertFalse(STANDING_SAME_AS_CYCLE268)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE297)
        self.assertFalse(STANDING_SAME_AS_CYCLE303)
        self.assertFalse(STANDING_SAME_AS_CYCLE306)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter021Previous600Scoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-021 previous-600 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.inside_sites = STANDING_INSIDE_SITES
        self.previous_stems = leftover_n4_remaining_previous_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.backwards = leftover_n4_remaining_backward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.with_previous_inside = leftover_n4_remaining_sites_with_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.line_initial_inside = leftover_n4_remaining_sites_without_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.share_021 = leftover_n4_remaining_with_previous_021(
            self.inside_sites,
            self.previous_stems,
        )
        self.remaining = leftover_n4_remaining_remaining_after_021(
            self.inside_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_021_previous_stems(
            self.inside_sites,
            self.previous_stems,
        )
        self.with_previous = leftover_n4_remaining_remaining_after_021_with_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.line_initial = leftover_n4_remaining_remaining_after_021_without_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.matching = leftover_n4_remaining_remaining_after_021_with_previous_600(
            self.inside_sites,
            self.previous_stems,
        )
        self.without = leftover_n4_remaining_remaining_after_021_without_previous_600(
            self.inside_sites,
            self.previous_stems,
        )
        self.matching_previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.remaining_after_600_stems = leftover_n4_remaining_previous_stems(
            self.i_sides,
            self.without,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_previous_inside = len(self.with_previous_inside)
        self.n_line_initial_inside = len(self.line_initial_inside)
        self.k_021 = len(self.share_021)
        self.n_remaining = len(self.remaining)
        self.n_with_previous = len(self.with_previous)
        self.n_line_initial = len(self.line_initial)
        self.k = len(self.matching)
        self.k_600 = self.k
        self.n_without = len(self.without)
        self.n_remaining_after_600 = self.n_remaining - self.k_600
        self.g, self.unique_k, self.unique = select_remaining_after_021_g(
            self.remaining_stems
        )
        self.equals_cycle306 = matching_equals_cycle306_g_set(self.matching)
        self.overlap_248 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE248_EXTRA_I_SITES,
        )
        self.overlap_268 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE268_EXTRA_I_090_076_SITES,
        )
        self.overlap_297 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE297_MATCHING_SITES,
        )
        self.overlap_267 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE267_MATCHING_SITES,
        )
        self.overlap_after_011 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE297_REMAINING_AFTER_011_SITES,
        )
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                self.k_600,
                self.unique,
                self.g,
                self.n_remaining,
            )
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_5_8_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/0/5/8 stay the cycle-306/303/224 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_021, ("021", "090", "076"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(len(STANDING_INSIDE_SITES), STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE224_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE288_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_306 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"
        ]
        self.assertEqual(prior_306["cycle"], 306)
        self.assertEqual(prior_306["G"], "600")
        self.assertEqual(prior_306["K"], 2)
        self.assertEqual(prior_306["N_remaining_after_021"], 8)
        self.assertEqual(prior_306["N_line_initial"], 0)
        self.assertEqual(prior_306["N_distinct"], 7)
        self.assertTrue(prior_306["G_uniquely_most_frequent"])
        self.assertTrue(
            prior_306["i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem"]
        )
        self.assertTrue(CYCLE306_CLAIM)
        self.assertEqual(CYCLE306_G, "600")
        self.assertEqual(CYCLE306_K, 2)
        self.assertEqual(CYCLE306_N_REMAINING, 8)
        self.assertEqual(CYCLE306_N_LINE_INITIAL, 0)
        self.assertEqual(CYCLE306_N_DISTINCT, 7)
        self.assertTrue(CYCLE306_UNIQUE)
        if (
            prior_306["G"] != "600"
            or prior_306["K"] != 2
            or prior_306["N_remaining_after_021"] != 8
            or prior_306["N_line_initial"] != 0
            or prior_306["N_distinct"] != 7
            or not prior_306["G_uniquely_most_frequent"]
            or not prior_306[
                "i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem"
            ]
        ):
            self.fail(
                "nested cycle 306 unique-max G=600 K=2 N_remaining=8 N_line_initial=0 distinct=7 drifted"
            )
        prior_305 = self.survey["i_021_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_305["cycle"], 305)
        self.assertEqual(prior_305["N_i_only"], 4)
        self.assertEqual(prior_305["N_hapax_i_only"], 3)
        self.assertEqual(prior_305["N_not_hapax"], 1)
        self.assertEqual(prior_305["N_not_i_only"], 0)
        self.assertTrue(prior_305["i_021_090_076_previous_4grams_all_i_only"])
        self.assertTrue(CYCLE305_CLAIM)
        self.assertEqual(CYCLE305_N_I_ONLY, 4)
        self.assertEqual(CYCLE305_N_HAPAX, 3)
        self.assertEqual(CYCLE305_N_NOT_HAPAX, 1)
        self.assertEqual(CYCLE305_N_NOT_I_ONLY, 0)
        prior_304 = self.survey["i_3gram_021_090_076_i_only"]
        self.assertEqual(prior_304["cycle"], 304)
        self.assertEqual(prior_304["N_I"], 5)
        self.assertEqual(prior_304["N_off_I"], 0)
        self.assertEqual(prior_304["N_extra"], 0)
        self.assertTrue(prior_304["i_3gram_021_090_076_i_only"])
        self.assertTrue(CYCLE304_CLAIM)
        prior_303 = self.survey["i_leftover_n4_remaining_090_076_previous_021"]
        self.assertEqual(prior_303["cycle"], 303)
        self.assertEqual(prior_303["K_021"], 5)
        self.assertEqual(prior_303["N_remaining_after_021"], 8)
        self.assertTrue(
            prior_303["i_leftover_n4_remaining_090_076_exactly_5_share_previous_021"]
        )
        self.assertTrue(CYCLE303_CLAIM)
        self.assertEqual(CYCLE303_G, "021")
        self.assertEqual(CYCLE303_K_021, 5)
        self.assertEqual(CYCLE303_N_REMAINING_AFTER_021, 8)
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertFalse(CYCLE224_ALL_INSIDE)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_nested_counts_hold(
                13, 4, 9, 3, 6, 2, 4, 2, 2
            )
        )
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, (13, 4, 9, 3, 6, 2, 4, 2, 2))
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, CYCLE303_NESTED)
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, CYCLE306_NESTED)
        self.assertEqual(STANDING_K_020, 4)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(STANDING_K_087, 3)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(STANDING_K_057, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, 4)
        self.assertEqual(STANDING_K_011, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_011, 2)
        unused_224_n = CYCLE224_N_I
        self.assertEqual(unused_224_n, 69)
        unused_267 = CYCLE267_K_600
        self.assertEqual(unused_267, 4)
        self.assertTrue(CYCLE267_CLAIM)
        unused_293 = CYCLE293_K_087
        self.assertEqual(unused_293, 3)
        self.assertTrue(CYCLE293_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_3GRAM_600_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_600)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_600_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_PREVIOUS_600_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_IS_NOT_THIS_CYCLE)
        self.assertTrue(
            STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM_IS_NOT_THIS_CYCLE
        )
        self.assertTrue(
            STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_057_NEXT_011_IS_NOT_THIS_CYCLE
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_of_8_and_hypothesis_k_2_holds(self):
        """N_remaining_after_021=8, K_600=2. Unique-max still 600. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_previous_inside, STANDING_N_WITH_PREVIOUS_INSIDE)
        self.assertEqual(STANDING_N_WITH_PREVIOUS_INSIDE, 13)
        self.assertEqual(self.n_line_initial_inside, STANDING_N_LINE_INITIAL_INSIDE)
        self.assertEqual(STANDING_N_LINE_INITIAL_INSIDE, 0)
        self.assertEqual(self.k_021, STANDING_K_021)
        self.assertEqual(STANDING_K_021, CYCLE303_K_021)
        self.assertEqual(STANDING_K_021, 5)
        self.assertEqual(self.share_021, CYCLE303_MATCHING_SITES)
        self.assertTrue(
            leftover_n4_remaining_remaining_after_021_nested_counts_hold(
                self.n_inside,
                self.n_line_initial_inside,
                self.k_021,
                self.n_remaining,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_021)
        self.assertEqual(STANDING_N_REMAINING_AFTER_021, 8)
        self.assertEqual(STANDING_N_REMAINING_AFTER_021, CYCLE303_N_REMAINING_AFTER_021)
        self.assertEqual(self.n_remaining, CYCLE306_N_REMAINING)
        self.assertEqual(self.n_remaining, self.n_inside - self.k_021)
        self.assertEqual(13 - 5, 8)
        if self.n_remaining != 8:
            self.fail("measured N_remaining_after_021 drifted from 8")
        if self.n_remaining != self.n_inside - self.k_021:
            self.fail(
                "leftover n=4 remaining remaining-after-021 filter disagrees with nested 13−5"
            )
        self.assertEqual(self.remaining, CYCLE306_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE303_REMAINING_AFTER_021_SITES)
        self.assertEqual(self.remaining_stems, CYCLE306_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(
            self.remaining,
            leftover_n4_remaining_without_previous_021(
                self.inside_sites,
                self.previous_stems,
            ),
        )
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 8)
        self.assertEqual(self.n_line_initial, STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertEqual(self.n_line_initial, STANDING_N_NO_PREVIOUS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertEqual(self.n_with_previous + self.n_line_initial, self.n_remaining)
        self.assertEqual(8 + 0, 8)
        for site in self.share_021:
            self.assertNotIn(site, self.remaining)
        for site in CYCLE297_REMAINING_AFTER_011_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertIn(site, CYCLE303_MATCHING_SITES)
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(self.k_600, STANDING_K_600)
        self.assertEqual(STANDING_K_600, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_600, 2)
        self.assertEqual(STANDING_K, CYCLE306_K)
        self.assertEqual(STANDING_G, "600")
        self.assertEqual(STANDING_G, CYCLE306_G)
        self.assertEqual(self.g, "600")
        self.assertEqual(self.unique_k, 2)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(STANDING_UNIQUE_MAX_STILL_600)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 6)
        self.assertEqual(self.n_without, CYCLE306_N_WITHOUT_G)
        self.assertEqual(self.n_remaining_after_600, STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(STANDING_N_REMAINING_AFTER_600, 6)
        self.assertEqual(self.k_600 + self.n_remaining_after_600, self.n_remaining)
        self.assertEqual(2 + 6, 8)
        if self.k_600 != 2:
            self.fail("nested-check K_600 drifted from 2")
        if self.g != "600" or not self.unique:
            self.fail("unique-max previous is no longer 600")
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600(
                self.k_600,
                self.unique,
                self.g,
                self.n_remaining,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_EXACTLY_2_SHARE_PREVIOUS_600,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_EXACTLY_2_SHARE_PREVIOUS_600
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE306_MATCHING_SITES)
        self.assertEqual(self.matching, STANDING_LEFTOVER_600011_COVERED)
        self.assertTrue(self.equals_cycle306)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE306_G_SITES)
        self.assertTrue(matching_equals_cycle306_g_set(self.matching))
        self.assertEqual(len(CYCLE306_MATCHING_SITES), CYCLE306_K)
        self.assertEqual(CYCLE306_K, 2)
        if len(self.matching) != 2 or not self.equals_cycle306:
            self.fail(
                "leftover n=4 remaining remaining-after-021 previous-600 set drifted from cycle-306 G set"
            )
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_600_SITES)
        self.assertEqual(
            tuple(self.remaining_after_600_stems),
            STANDING_REMAINING_AFTER_600_PREVIOUS_STEMS,
        )
        self.assertEqual(
            set(self.remaining_after_600_stems),
            set(STANDING_REMAINING_AFTER_600_HAPAX_STEMS),
        )
        self.assertEqual(len(set(self.remaining_after_600_stems)), 6)
        self.assertEqual(CYCLE306_N_HAPAX, 6)
        self.assertEqual(STANDING_N_HAPAX, 6)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE267)
        self.assertFalse(STANDING_SAME_AS_CYCLE268)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE297)
        self.assertFalse(STANDING_SAME_AS_CYCLE303)
        self.assertFalse(STANDING_SAME_AS_CYCLE306)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_3GRAM_600_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_600)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_600_NOT_LOCKED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT)
        self.assertTrue(CYCLE306_CLAIM)
        self.assertTrue(CYCLE303_CLAIM)
        self.assertTrue(CYCLE304_CLAIM)
        self.assertTrue(CYCLE305_CLAIM)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertTrue(CYCLE268_CLAIM)
        self.assertTrue(CYCLE293_CLAIM)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE306_N_DISTINCT, 7)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_remaining_after_021_sites_have_previous_600(self):
        """Two remaining-after-021 leftover n=4 remaining sites are 600 090 076."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(self.matching_previous_4grams, CYCLE306_MATCHING_PREVIOUS_4GRAMS)
        expected = tuple(
            zip(STANDING_MATCHING_SITES, STANDING_MATCHING_PREVIOUS_4GRAMS, strict=True)
        )
        for (site, prev4), (want_site, want_prev) in zip(
            zip(self.matching, self.matching_previous_4grams, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N2]), GRAM3_BACKWARD)
            self.assertEqual(stems[index - 1], "600")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "600")
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), GRAM3_BACKWARD)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev)
            self.assertEqual(prev4, want_prev)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, self.remaining)
            self.assertIn(site, CYCLE306_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE303_MATCHING_SITES)
            self.assertNotIn(site, CYCLE297_REMAINING_AFTER_011_SITES)
            self.assertIn(site, CYCLE306_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE306_MATCHING_SITES)
        self.assertTrue(matching_equals_cycle306_g_set(self.matching))
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            prev = site_previous_stem(stems, index, GRAM2)
            self.assertIsNotNone(prev)
            self.assertNotEqual(prev, "600")
            self.assertNotEqual(prev, "021")
            self.assertIn(site, self.remaining)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, CYCLE306_MATCHING_SITES)
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_600_SITES)
        self.assertEqual(len(self.without), STANDING_N_REMAINING_AFTER_600)
        for site in self.share_021:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE303_MATCHING_SITES)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in CYCLE267_MATCHING_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, prev4, _nxt4), want in zip(
            local,
            STANDING_MATCHING_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertEqual(prev4, want)
        self.assertEqual(
            matching_leftover_n4_remaining_remaining_after_021_local_4gram_rows(),
            matching_leftover_n4_remaining_remaining_after_021_local_4gram_rows(
                STANDING_MATCHING_SITES,
                STANDING_MATCHING_PREVIOUS_4GRAMS,
            ),
        )
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_600)
        self.assertTrue(STANDING_3GRAM_600_090_076_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_overlap_248_268_297_recorded_remaining_after_011_empty(self):
        """Previous-600 remaining-after-021 sites equal cycle 248/268 extra I and cycle 297 next-011."""
        self.assertEqual(self.overlap_248, STANDING_OVERLAP_CYCLE248_EXTRA_I)
        self.assertEqual(self.overlap_248, CYCLE248_EXTRA_I_SITES)
        self.assertEqual(
            self.overlap_248,
            ((SIDE_IA, "Ia2", 107), (SIDE_IA, "Ia14", 54)),
        )
        self.assertEqual(self.overlap_268, STANDING_OVERLAP_CYCLE268_EXTRA_I)
        self.assertEqual(self.overlap_268, CYCLE268_EXTRA_I_090_076_SITES)
        self.assertEqual(self.overlap_297, STANDING_OVERLAP_CYCLE297_NEXT_011)
        self.assertEqual(self.overlap_297, CYCLE297_MATCHING_SITES)
        self.assertEqual(self.overlap_267, STANDING_OVERLAP_CYCLE267_PREVIOUS_600)
        self.assertEqual(self.overlap_267, ())
        self.assertEqual(self.overlap_after_011, STANDING_OVERLAP_REMAINING_AFTER_011)
        self.assertEqual(self.overlap_after_011, ())
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE268_EXTRA_I_090_076)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE297_NEXT_011)
        self.assertEqual(self.matching, CYCLE248_EXTRA_I_SITES)
        self.assertEqual(self.matching, CYCLE268_EXTRA_I_090_076_SITES)
        self.assertEqual(self.matching, CYCLE297_MATCHING_SITES)
        self.assertNotIn((SIDE_IA, "Ia8", 106), self.remaining)
        self.assertNotIn((SIDE_IA, "Ia13", 17), self.remaining)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE303_MATCHING_SITES)
        self.assertIn((SIDE_IA, "Ia13", 17), CYCLE303_MATCHING_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertIn((SIDE_IA, "Ia13", 17), CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertEqual(CYCLE268_EXTRA_I_SITES, ((SIDE_IA, "Ia2", 106), (SIDE_IA, "Ia14", 53)))
        self.assertEqual(CYCLE268_N_EXTRA, 2)
        self.assertEqual(CYCLE268_N_I, 6)
        self.assertEqual(CYCLE268_N_OFF_I, 0)
        self.assertTrue(CYCLE268_CLAIM)
        self.assertEqual(CYCLE248_N_EXTRA, 2)
        self.assertEqual(CYCLE248_N_I, 4)
        self.assertEqual(CYCLE248_N_OFF_I, 0)
        self.assertTrue(CYCLE248_CLAIM)
        self.assertTrue(CYCLE297_CLAIM)
        for site in CYCLE267_MATCHING_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.matching)
            self.assertNotIn(site, self.remaining)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(self.claim_holds)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_306_305_304_303_297_288_268_267_248_224_223_still_compute(self):
        """Cycle 306 G=600 K=2, 305 N_not_hapax=1, 304 5/0 extra I=0, 303 K_021=5, 297 next-011, 288 G=020 K=4, 268 6/0 extra I=2, 267 K_600=4, 248 extra I=2, 224 13/56, 223 69/3 stay."""
        prior_306 = TestMamariILeftoverN4Remaining090076RemainingAfter021PreviousStemScoreboard()
        prior_306.setUp()
        prior_306.test_counts_8_remaining_g_600_k_2_and_hypothesis_holds()
        prior_306.test_survey_matches_computed_lock()
        self.assertEqual(prior_306.g, "600")
        self.assertEqual(prior_306.k, 2)
        self.assertEqual(prior_306.n_remaining, 8)
        self.assertEqual(prior_306.n_line_initial, 0)
        self.assertEqual(prior_306.n_distinct, 7)
        self.assertTrue(prior_306.unique)
        self.assertTrue(prior_306.claim_holds)
        self.assertTrue(CYCLE306_CLAIM)
        if (
            prior_306.g != "600"
            or prior_306.k != 2
            or prior_306.n_remaining != 8
            or prior_306.n_distinct != 7
            or not prior_306.unique
            or not prior_306.claim_holds
        ):
            self.fail(
                "nested cycle 306 unique-max G=600 K=2 N_remaining=8 distinct=7 drifted"
            )
        prior_305 = TestMamariI021090076Previous4gramsIOnlyScoreboard()
        prior_305.setUp()
        prior_305.test_all_4grams_are_i_only_not_all_hapax_and_claim_holds()
        prior_305.test_survey_matches_computed_lock()
        self.assertEqual(prior_305.n_i_only, 4)
        self.assertEqual(prior_305.n_hapax_i_only, 3)
        self.assertEqual(prior_305.n_not_hapax, 1)
        self.assertEqual(prior_305.n_not_i_only, 0)
        self.assertTrue(prior_305.claim_holds)
        self.assertTrue(CYCLE305_CLAIM)
        if (
            prior_305.n_i_only != 4
            or prior_305.n_hapax_i_only != 3
            or prior_305.n_not_hapax != 1
            or prior_305.n_not_i_only != 0
            or not prior_305.claim_holds
        ):
            self.fail(
                "nested cycle 305 previous-021 4-grams I-only N_i_only=4 N_hapax=3 N_not_hapax=1 N_leak=0 drifted"
            )
        prior_304 = TestMamariI3gram021090076IOnlyScoreboard()
        prior_304.setUp()
        prior_304.test_i_hits_are_five_on_ia_and_leftover_n4_remaining_021_is_subset()
        prior_304.test_3gram_is_zero_off_i_and_i_only()
        prior_304.test_survey_matches_computed_lock()
        self.assertEqual(prior_304.i_hits, 5)
        self.assertEqual(prior_304.off_i_hits, 0)
        self.assertEqual(len(prior_304.extra), 0)
        self.assertEqual(prior_304.extra, CYCLE304_EXTRA_I_SITES)
        self.assertTrue(prior_304.claim_holds)
        self.assertTrue(CYCLE304_CLAIM)
        self.assertEqual(CYCLE304_N_I, 5)
        self.assertEqual(CYCLE304_N_OFF_I, 0)
        self.assertEqual(CYCLE304_N_EXTRA, 0)
        if prior_304.i_hits != 5 or prior_304.off_i_hits != 0 or prior_304.extra:
            self.fail("nested cycle 304 021 090 076 I-only 5/0 extra I=0 drifted")
        prior_303 = TestMamariILeftoverN4Remaining090076Previous021Scoreboard()
        prior_303.setUp()
        prior_303.test_counts_5_of_13_and_hypothesis_k_5_holds()
        prior_303.test_survey_matches_computed_lock()
        self.assertEqual(prior_303.k_021, 5)
        self.assertEqual(prior_303.n_remaining_after_021, 8)
        self.assertEqual(prior_303.matching, CYCLE303_MATCHING_SITES)
        self.assertEqual(self.share_021, prior_303.matching)
        self.assertEqual(self.remaining, prior_303.without)
        self.assertTrue(prior_303.claim_holds)
        self.assertTrue(CYCLE303_CLAIM)
        if (
            prior_303.k_021 != 5
            or prior_303.n_remaining_after_021 != 8
            or not prior_303.claim_holds
        ):
            self.fail(
                "nested cycle 303 leftover n=4 remaining exactly 5 share 021 / N_remaining=8 drifted"
            )
        prior_297 = TestMamariILeftoverN4Remaining090076RemainingAfter057Forward011Scoreboard()
        prior_297.setUp()
        prior_297.test_counts_2_of_4_and_hypothesis_k_2_holds()
        prior_297.test_survey_matches_computed_lock()
        self.assertEqual(prior_297.matching, CYCLE297_MATCHING_SITES)
        self.assertEqual(prior_297.matching, self.matching)
        self.assertTrue(prior_297.claim_holds)
        self.assertTrue(CYCLE297_CLAIM)
        if prior_297.matching != CYCLE297_MATCHING_SITES or not prior_297.claim_holds:
            self.fail("nested cycle 297 leftover n=4 remaining remaining-after-057 next 011 drifted")
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_inside, 13)
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        if (
            prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or not prior_288.unique_max
            or prior_288.claim_holds
        ):
            self.fail("nested cycle 288 share-one-forward lost 6 distinct G=020 K=4 unique-max drifted")
        prior_268 = TestMamariI3gram600090076IOnlyScoreboard()
        prior_268.setUp()
        prior_268.test_3gram_is_zero_off_i_and_i_only()
        prior_268.test_survey_matches_computed_lock()
        self.assertEqual(prior_268.i_hits, 6)
        self.assertEqual(prior_268.off_i_hits, 0)
        self.assertEqual(len(prior_268.extra), 2)
        self.assertEqual(prior_268.extra, CYCLE268_EXTRA_I_SITES)
        self.assertTrue(prior_268.claim_holds)
        self.assertTrue(CYCLE268_CLAIM)
        if prior_268.i_hits != 6 or prior_268.off_i_hits != 0 or len(prior_268.extra) != 2:
            self.fail("nested cycle 268 600 090 076 I-only 6/0 extra I=2 drifted")
        prior_267 = TestMamariILeftoverExtra090076RemainingAfter999Previous600Scoreboard()
        prior_267.setUp()
        prior_267.test_counts_4_of_41_and_hypothesis_k_4_holds()
        prior_267.test_survey_matches_computed_lock()
        self.assertEqual(prior_267.k_600, 4)
        self.assertEqual(prior_267.matching, CYCLE267_MATCHING_SITES)
        self.assertTrue(prior_267.claim_holds)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertEqual(CYCLE267_K_600, 4)
        if prior_267.k_600 != 4 or not prior_267.claim_holds:
            self.fail("nested cycle 267 leftover extra remaining-after-999 previous-600 K_600=4 drifted")
        prior_248 = TestMamariI3gram090076011IOnlyScoreboard()
        prior_248.setUp()
        prior_248.test_3gram_is_zero_off_i_and_i_only()
        prior_248.test_survey_matches_computed_lock()
        self.assertEqual(prior_248.i_hits, CYCLE248_N_I)
        self.assertEqual(prior_248.i_hits, 4)
        self.assertEqual(prior_248.off_i_hits, CYCLE248_N_OFF_I)
        self.assertEqual(prior_248.off_i_hits, 0)
        self.assertEqual(len(prior_248.extra), CYCLE248_N_EXTRA)
        self.assertEqual(len(prior_248.extra), 2)
        self.assertEqual(prior_248.extra, CYCLE248_EXTRA_I_SITES)
        self.assertEqual(prior_248.extra, self.matching)
        self.assertTrue(prior_248.claim_holds)
        self.assertTrue(CYCLE248_CLAIM)
        if prior_248.i_hits != 4 or prior_248.off_i_hits != 0 or len(prior_248.extra) != 2:
            self.fail("nested cycle 248 090 076 011 I-only 4/0 extra I=2 drifted")
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        if prior_224.n_inside != 13 or prior_224.n_leftover != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, STANDING_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, STANDING_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, STANDING_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_600)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-307 leftover n=4 remaining remaining-after-021 previous-600 lock."""
        lock = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_021_previous_600"
        ]
        self.assertEqual(lock["cycle"], 307)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(tuple(lock["backward_3gram"]), ("600", "090", "076"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_previous_stems"]), LOCKED_PREVIOUS_STEMS)
        self.assertEqual(tuple(lock["locked_previous_stems"]), ("021",))
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_with_previous_inside"], STANDING_N_WITH_PREVIOUS_INSIDE)
        self.assertEqual(lock["N_with_previous_inside"], 13)
        self.assertEqual(lock["N_line_initial_inside"], STANDING_N_LINE_INITIAL_INSIDE)
        self.assertEqual(lock["N_line_initial_inside"], 0)
        self.assertEqual(lock["K_021"], STANDING_K_021)
        self.assertEqual(lock["K_021"], 5)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_021_sites"]),
            CYCLE303_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_021"], STANDING_N_REMAINING_AFTER_021)
        self.assertEqual(lock["N_remaining_after_021"], 8)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_021_sites"]),
            CYCLE306_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_021_previous_stems"]),
            CYCLE306_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 8)
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 7)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 6)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "600")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertEqual(lock["K_600"], STANDING_K_600)
        self.assertEqual(lock["K_600"], 2)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 6)
        self.assertEqual(lock["N_remaining_after_600"], STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(lock["N_remaining_after_600"], 6)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertTrue(lock["unique_max_still_600"])
        self.assertEqual(
            tuple(
                tuple(row)
                for row in lock["matching_leftover_n4_remaining_remaining_after_021_sites"]
            ),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(
                tuple(row)
                for row in lock["matching_leftover_n4_remaining_remaining_after_021_sites"]
            ),
            CYCLE306_MATCHING_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle306_g_sites"])
        self.assertEqual(
            lock["matching_equals_cycle306_g_sites"],
            STANDING_MATCHING_EQUALS_CYCLE306_G_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle248_extra_i"])
        self.assertTrue(lock["matching_equals_cycle268_extra_i_090_076"])
        self.assertTrue(lock["matching_equals_cycle297_next_011"])
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_remaining_after_021_local_4grams"],
            matching_leftover_n4_remaining_remaining_after_021_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_600_sites"]),
            STANDING_REMAINING_AFTER_600_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_600_previous_stems"]),
            STANDING_REMAINING_AFTER_600_PREVIOUS_STEMS,
        )
        self.assertEqual(
            set(lock["remaining_after_600_hapax_stems"]),
            set(STANDING_REMAINING_AFTER_600_HAPAX_STEMS),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle306_G_sites"]),
            CYCLE306_MATCHING_SITES,
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE248_EXTRA_I],
            lock["overlap_cycle248_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE268_EXTRA_I],
            lock["overlap_cycle268_extra_i_090_076_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE297_NEXT_011],
            lock["overlap_cycle297_next_011_sites"],
        )
        self.assertEqual(lock["overlap_cycle267_previous_600_sites"], [])
        self.assertEqual(lock["overlap_remaining_after_011_sites"], [])
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertEqual(
            list(STANDING_NESTED_LEFTOVER_N4_REMAINING),
            lock["nested_leftover_n4_remaining"],
        )
        self.assertEqual(lock["nested_cycle306_G"], "600")
        self.assertEqual(lock["nested_cycle306_K"], 2)
        self.assertEqual(lock["nested_cycle306_N_remaining_after_021"], 8)
        self.assertEqual(lock["nested_cycle306_N_line_initial"], 0)
        self.assertEqual(lock["nested_cycle306_N_distinct"], 7)
        self.assertTrue(lock["nested_cycle306_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle305_N_i_only"], 4)
        self.assertEqual(lock["nested_cycle305_N_hapax_i_only"], 3)
        self.assertEqual(lock["nested_cycle305_N_not_hapax"], 1)
        self.assertEqual(lock["nested_cycle305_N_not_i_only"], 0)
        self.assertTrue(lock["nested_cycle305_previous_4grams_all_i_only"])
        self.assertEqual(lock["nested_cycle304_N_I"], 5)
        self.assertEqual(lock["nested_cycle304_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle304_N_extra"], 0)
        self.assertEqual(lock["nested_cycle303_K_021"], 5)
        self.assertEqual(lock["nested_cycle303_N_remaining_after_021"], 8)
        self.assertEqual(lock["nested_cycle297_K_011"], 2)
        self.assertTrue(lock["nested_cycle297_exactly_2_share_forward_011"])
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertFalse(lock["nested_cycle288_share_one_forward_stem"])
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle268_N_I"], 6)
        self.assertEqual(lock["nested_cycle268_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle268_N_extra"], 2)
        self.assertTrue(lock["nested_cycle268_i_only"])
        self.assertEqual(lock["nested_cycle267_K_600"], 4)
        self.assertTrue(lock["nested_cycle267_exactly_4_share_previous_600"])
        self.assertEqual(lock["nested_cycle248_N_I"], 4)
        self.assertEqual(lock["nested_cycle248_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle248_N_extra"], 2)
        self.assertTrue(lock["nested_cycle248_i_only"])
        self.assertEqual(lock["nested_cycle293_K_087"], 3)
        self.assertTrue(lock["nested_cycle293_exactly_3_share_forward_087"])
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600"]
        )
        self.assertEqual(
            lock["i_leftover_n4_remaining_090_076_remaining_after_021_exactly_2_share_previous_600"],
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_EXACTLY_2_SHARE_PREVIOUS_600,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle267"])
        self.assertFalse(lock["same_as_cycle268"])
        self.assertFalse(lock["same_as_cycle293"])
        self.assertFalse(lock["same_as_cycle297"])
        self.assertFalse(lock["same_as_cycle303"])
        self.assertFalse(lock["same_as_cycle306"])
        self.assertTrue(lock["same_claim_shape_as_cycle267"])
        self.assertTrue(lock["same_claim_shape_as_cycle293"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["3gram_600_090_076_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_remaining_after_600"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_600_not_locked"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(
            lock["leftover_extra_remaining_after_999_previous_600_is_not_this_cycle"]
        )
        self.assertTrue(lock["leftover_extra_600_090_076_previous_4grams_is_not_this_cycle"])
        self.assertTrue(lock["leftover_n4_remaining_previous_021_is_not_this_cycle"])
        self.assertTrue(
            lock["leftover_n4_remaining_remaining_after_021_unique_previous_stem_is_not_this_cycle"]
        )
        self.assertTrue(
            lock["leftover_n4_remaining_remaining_after_057_next_011_is_not_this_cycle"]
        )
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_021_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_021_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_previous_021_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_3gram_600_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_600_unchanged"]
        )
        self.assertTrue(lock["standing_i_3gram_090_076_011_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"][
                "cycle"
            ],
            306,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"][
                "G"
            ],
            "600",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"][
                "K"
            ],
            2,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"][
                "i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_021_090_076_previous_4grams_i_only"]["cycle"], 305)
        self.assertEqual(self.survey["i_021_090_076_previous_4grams_i_only"]["N_not_hapax"], 1)
        self.assertEqual(self.survey["i_3gram_021_090_076_i_only"]["cycle"], 304)
        self.assertEqual(self.survey["i_3gram_021_090_076_i_only"]["N_extra"], 0)
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_021"]["cycle"],
            303,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_021"]["K_021"],
            5,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_forward_011"][
                "cycle"
            ],
            297,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["cycle"], 268)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_extra"], 2)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["cycle"],
            267,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["K_600"],
            4,
        )
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["cycle"], 248)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_extra"], 2)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"], 13)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter021Previous600ImageSnapshot(
    unittest.TestCase
):
    """Cycle 307 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
