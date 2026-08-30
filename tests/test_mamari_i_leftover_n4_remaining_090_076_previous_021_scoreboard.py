"""I's cycle-302 leftover n=4 remaining previous-021 lock.

Cycle 303 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–259 forward; 260–287 previous),
leftover n=4 remaining forward peel (288–301), leftover extra
I 090 076 previous-stem (cycle 260), leftover extra
remaining-after-999 previous 600 (cycle 267), leftover n=4
remaining unique previous stem (cycle 302), leftover n=4
remaining remaining-after-011 3-grams (cycle 300), or
remaining-after-011 extra-I 4-grams (cycle 301). Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Cycle 302 leftover n=4 remaining unique previous stem HOLDS:
N=13, N_line_initial=0, unique_max true, G=021 K=5,
N_distinct=8, G sites Ia4[117]/Ia5[28]/Ia6[78]/Ia8[106]/
Ia13[17], N_remaining after peeling G=8. Unique-max G/K is
inventory; this cycle peels 021 as exact-K. Do not peel
remaining-after-021 this cycle. Do not lock 3-gram
021 090 076 I-only this cycle (that is the next lock if this
HOLD). Off-I T sites are not this cycle. 076 071 and 076 070
do not count as this 2-gram. Leftover extra sites do not
count as leftover n=4 remaining.

Hypothesis K=5: leftover n=4 remaining I 090 076 sites
include exactly 5 that share previous stem 021 (backward
3-gram 021 090 076). Nested-check leftover n=4 remaining
N_inside==13, N_line_initial==0, unique_max true, G=021 K=5,
N_distinct=8 (do not retune 224/288/302). Nested leftover
n=4 remaining 13 / 4 / 9 / 3 / 6 / 2 / 4 / 2 / 2 still
computes (do not retune 288–297). Count leftover n=4
remaining I 090 076 sites whose previous token is 021.
Cycle 302 listed Ia4[117]/Ia5[28]/Ia6[78]/Ia8[106]/Ia13[17];
measure, do not assume if nested-check differs. Ia8[106] /
Ia13[17] are also remaining-after-011 (cycle 298 hapax next
607/021). N_remaining_after_021 = N_inside − K_021.
Unique-max previous of leftover n=4 remaining is still 021.
Claim that can lose:
i_leftover_n4_remaining_090_076_exactly_5_share_previous_021.
True iff K_021==5 among leftover n=4 remaining I 090 076 and
unique-max previous is still 021. The claim is true. Same
claim-shape as cycle 267 (leftover extra remaining-after-999
exactly 4 share previous 600) and cycle 293 (leftover n=4
remaining remaining-after-020 exactly 3 share next 087),
leftover n=4 remaining / previous 021 instead of leftover
extra remaining-after-999 / previous 600. This can lose if
nested-check K differs from 5, if unique-max is no longer
021, if N leftover n=4 remaining != 13, or if the site list
no longer computes. Nested cycle 302 unique-max G=021 K=5
N=13 distinct=8, cycle 288 unique-max G=020 K=4 share-one
lost, cycle 301 090 076 607 073 1/0, cycle 224 13/56, and
cycle 223 69/3 stay. Nested overlap of previous-021 sites
with leftover extra previous-999 (cycle 261) is empty;
overlap with leftover extra remaining-after-000 extra I
(cycles 258/259) is Ia8[106] only; overlap with remaining-
after-011 is Ia8[106]/Ia13[17]; record, do not fail K_021
on it. Do not assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES,
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
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 as CYCLE261_CLAIM,
    STANDING_K_999 as CYCLE261_K_999,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE260_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE258_N_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_BY_X as CYCLE259_EXTRA_I_BY_X,
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_N_I_ONLY as CYCLE259_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE259_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
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
    STANDING_N_NO_NEXT as CYCLE288_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE288_N_WITH_NEXT,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE302_G,
    STANDING_G_SITES as CYCLE302_G_SITES,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE302_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_UNIQUE_PREVIOUS_STEM as CYCLE302_CLAIM,
    STANDING_K as CYCLE302_K,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE302_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE302_MATCHING_SITES,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE302_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE302_N_INSIDE,
    STANDING_N_LINE_INITIAL as CYCLE302_N_LINE_INITIAL,
    STANDING_N_REMAINING_AFTER_G as CYCLE302_N_REMAINING,
    STANDING_NESTED_LEFTOVER_N4_REMAINING as CYCLE302_NESTED,
    STANDING_REMAINING_AFTER_G_SITES as CYCLE302_REMAINING_SITES,
    leftover_n4_remaining_backward_3grams,
    leftover_n4_remaining_g_overlap_sites,
    leftover_n4_remaining_previous_4grams,
    leftover_n4_remaining_previous_stems,
    leftover_n4_remaining_sites_with_previous,
    leftover_n4_remaining_sites_without_previous,
    leftover_n4_remaining_with_previous_g,
    leftover_n4_remaining_without_previous_g,
    select_previous_g,
    TestMamariILeftoverN4Remaining090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_3GRAMS_ALL_I_ONLY as CYCLE300_CLAIM,
    STANDING_N_I_ONLY as CYCLE300_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE300_N_NOT_I_ONLY,
    TestMamariILeftoverN4Remaining090076RemainingAfter0113gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE301_CLAIM,
    STANDING_N_I_ONLY as CYCLE301_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE301_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE301_SEQUENCES,
    TestMamariILeftoverN4Remaining090076RemainingAfter011ExtraIFwd4IOnlyScoreboard,
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
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_scoreboard import (
    STANDING_REMAINING_AFTER_011_SITES as CYCLE297_REMAINING_AFTER_011_SITES,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    TestMamariILeftoverN4RemainingNext2gramScoreboard,
    i_leftover_n4_remaining_exactly_5_contain_090_076,
    leftover_n4_family_counts_hold,
    leftover_n4_rows,
    leftover_remaining_n4,
    leftover_remaining_with_g,
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

HYPOTHESIS_K = 5
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_BACKWARD = ("021", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS = 13
STANDING_N_LINE_INITIAL = 0
STANDING_N_NO_PREVIOUS = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT_PREVIOUS_STEMS = 8
STANDING_K = 5
STANDING_K_021 = 5
STANDING_G = "021"
STANDING_N_WITHOUT = 8
STANDING_N_REMAINING_AFTER_021 = 8
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia4", 117),
    (SIDE_IA, "Ia5", 28),
    (SIDE_IA, "Ia6", 78),
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia13", 17),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("600", "021", "090", "076"),
    ("007", "021", "090", "076"),
    ("150", "021", "090", "076"),
    ("999", "021", "090", "076"),
    ("999", "021", "090", "076"),
)
STANDING_REMAINING_AFTER_021_SITES = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
    (SIDE_IA, "Ia12", 83),
    (SIDE_IA, "Ia14", 54),
)
STANDING_MATCHING_EQUALS_CYCLE302_G_SITES = True
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_UNIQUE_MAX_STILL_021 = True
STANDING_OVERLAP_CYCLE261_PREVIOUS_999 = ()
STANDING_OVERLAP_CYCLE258_EXTRA_I = ((SIDE_IA, "Ia8", 106),)
STANDING_OVERLAP_CYCLE259_EXTRA_I = ((SIDE_IA, "Ia8", 106),)
STANDING_OVERLAP_REMAINING_AFTER_011 = (
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia13", 17),
)
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_remaining_090_076_exactly_5_share_previous_021"
STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021 = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_previous_021"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE260 = False
STANDING_SAME_AS_CYCLE267 = False
STANDING_SAME_AS_CYCLE293 = False
STANDING_SAME_AS_CYCLE300 = False
STANDING_SAME_AS_CYCLE301 = False
STANDING_SAME_AS_CYCLE302 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_021_090_076_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_REMAINING_AFTER_021 = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_NOT_LOCKED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_PREVIOUS_STEM_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_PREVIOUS_600_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_UNIQUE_PREVIOUS_STEM_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_AFTER_011_3GRAMS_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_AFTER_011_EXTRA_I_FWD4_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_NESTED_LEFTOVER_N4_REMAINING = (13, 4, 9, 3, 6, 2, 4, 2, 2)


def leftover_n4_remaining_with_previous_021(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose previous token is 021."""
    return leftover_n4_remaining_with_previous_g(sites, previous_stems, stem=stem)


def leftover_n4_remaining_without_previous_021(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose previous token is not 021."""
    return leftover_n4_remaining_without_previous_g(sites, previous_stems, stem=stem)


def matching_equals_cycle302_g_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle302_g_sites: tuple[tuple[str, str, int], ...] = CYCLE302_MATCHING_SITES,
) -> bool:
    """True iff leftover n=4 remaining previous-021 sites equal the cycle-302 G set."""
    return matching_sites == cycle302_g_sites


def matching_leftover_n4_remaining_previous_021_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover n=4 remaining previous-021 previous-4-gram rows."""
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


def i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(
    k: int,
    unique: bool,
    g: str | None,
    expected: int = HYPOTHESIS_K,
    expected_g: str = STANDING_G,
) -> bool:
    """True iff K_021 equals 5 and unique-max previous is still 021."""
    return k == expected and unique and g == expected_g


class TestILeftoverN4Remaining090076Previous021Helpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining previous 021. No CV, no LLM."""

    def test_previous_021_requires_stem_before_2gram(self):
        """Previous stem 021 is 021 090 076; line-initial is no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("021", "090", "076"))
        self.assertEqual(GRAM3_BACKWARD[1:], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_021 = ["600", "021", "090", "076", "087"]
        self.assertEqual(site_previous_stem(has_021, 2, GRAM2), "021")
        self.assertEqual(site_backward_3gram(has_021, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_021, 2, GRAM2),
            ("600", "021", "090", "076"),
        )
        other_prev = ["071", "600", "090", "076"]
        self.assertEqual(site_previous_stem(other_prev, 2, GRAM2), "600")
        self.assertNotEqual(site_backward_3gram(other_prev, 2, GRAM2), GRAM3_BACKWARD)
        one_token_before = ["021", "090", "076"]
        self.assertEqual(site_previous_stem(one_token_before, 1, GRAM2), "021")
        self.assertEqual(site_backward_3gram(one_token_before, 1, GRAM2), GRAM3_BACKWARD)
        self.assertIsNone(site_previous_4gram(one_token_before, 1, GRAM2))
        line_initial = ["090", "076", "087"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(line_initial, 0, GRAM2))
        mismatch_071 = ["021", "076", "071", "090"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        mismatch_070 = ["021", "076", "070", "090"]
        self.assertIsNone(site_previous_stem(mismatch_070, 1, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
        )
        planted_stems = ("021", "600", None, "999")
        self.assertEqual(
            leftover_n4_remaining_with_previous_021(planted_sites, planted_stems),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_n4_remaining_without_previous_021(planted_sites, planted_stems),
            (planted_sites[1], planted_sites[2], planted_sites[3]),
        )
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_5_can_fail(self):
        """Boolean is True only when K=5 and unique-max G is 021."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(5, True, "021")
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(0, True, "021")
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(4, True, "021")
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(6, True, "021")
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(13, True, "021")
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(5, False, "021")
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(5, True, "600")
        )
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 15),)
        planted_stems = ("021",) * 6
        self.assertEqual(
            leftover_n4_remaining_with_previous_021(planted, planted_stems),
            planted,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(
                len(planted), True, "021"
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_exactly_5_share_previous_021",
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021)
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021,
            HYPOTHESIS_K == STANDING_K_021 and STANDING_UNIQUE_MAX_STILL_021,
        )
        self.assertEqual(
            STANDING_K_021 + STANDING_N_REMAINING_AFTER_021,
            STANDING_N_INSIDE,
        )
        self.assertEqual(5 + 8, 13)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle302_set_and_overlap_can_diverge(self):
        """Cycle-302 G-site equality can fail; overlap does not make K_021 lose."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle302_g_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE302_G_SITES)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle302_g_set(planted))
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(
                len(planted), True, "021"
            )
        )
        self.assertEqual(STANDING_OVERLAP_REMAINING_AFTER_011, CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_021)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_NOT_LOCKED)
        self.assertTrue(STANDING_I_ONLY_OF_021_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE267)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE302)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076Previous021Scoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 remaining previous-021 lock. Mock only."""

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
        self.with_previous = leftover_n4_remaining_sites_with_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.line_initial = leftover_n4_remaining_sites_without_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.matching = leftover_n4_remaining_with_previous_021(
            self.inside_sites,
            self.previous_stems,
        )
        self.without = leftover_n4_remaining_without_previous_021(
            self.inside_sites,
            self.previous_stems,
        )
        self.matching_previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_previous = len(self.with_previous)
        self.n_line_initial = len(self.line_initial)
        self.k = len(self.matching)
        self.k_021 = self.k
        self.n_without = len(self.without)
        self.n_remaining_after_021 = self.n_inside - self.k_021
        self.g, self.unique_k, self.unique = select_previous_g(self.previous_stems)
        self.equals_cycle302 = matching_equals_cycle302_g_set(self.matching)
        self.overlap_261 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE261_MATCHING_SITES,
        )
        self.overlap_258 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_after_011 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE297_REMAINING_AFTER_011_SITES,
        )
        self.claim_holds = i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(
            self.k_021,
            self.unique,
            self.g,
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_not_retuned(self):
        """2-gram and leftover n=4 remaining 13 / 4 / 9 / 3 / 6 / 2 / 4 / 2 / 2 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_BACKWARD, ("021", "090", "076"))
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
        self.assertEqual(STANDING_N_INSIDE, CYCLE302_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_302 = self.survey["i_leftover_n4_remaining_090_076_previous_stem"]
        self.assertEqual(prior_302["cycle"], 302)
        self.assertEqual(prior_302["G"], "021")
        self.assertEqual(prior_302["K"], 5)
        self.assertEqual(prior_302["N_inside"], 13)
        self.assertEqual(prior_302["N_line_initial"], 0)
        self.assertEqual(prior_302["N_distinct_previous_stems"], 8)
        self.assertTrue(prior_302["G_uniquely_most_frequent"])
        self.assertTrue(prior_302["i_leftover_n4_remaining_090_076_unique_previous_stem"])
        self.assertTrue(CYCLE302_CLAIM)
        self.assertEqual(CYCLE302_G, "021")
        self.assertEqual(CYCLE302_K, 5)
        self.assertEqual(CYCLE302_N_INSIDE, 13)
        self.assertEqual(CYCLE302_N_LINE_INITIAL, 0)
        self.assertEqual(CYCLE302_N_DISTINCT, 8)
        self.assertTrue(CYCLE302_UNIQUE)
        if (
            prior_302["G"] != "021"
            or prior_302["K"] != 5
            or prior_302["N_inside"] != 13
            or prior_302["N_line_initial"] != 0
            or prior_302["N_distinct_previous_stems"] != 8
            or not prior_302["G_uniquely_most_frequent"]
            or not prior_302["i_leftover_n4_remaining_090_076_unique_previous_stem"]
        ):
            self.fail(
                "nested cycle 302 unique-max G=021 K=5 N=13 N_line_initial=0 distinct=8 drifted"
            )
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["N_inside"], 13)
        self.assertEqual(prior_288["N_with_next"], 13)
        self.assertEqual(prior_288["N_no_next"], 0)
        self.assertEqual(prior_288["N_distinct_next_stems"], 6)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        prior_301 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"
        ]
        self.assertEqual(prior_301["cycle"], 301)
        self.assertEqual(prior_301["N_i_only"], 1)
        self.assertEqual(prior_301["N_not_i_only"], 0)
        self.assertEqual(tuple(prior_301["extra_i_forward_4grams"][0]), CYCLE301_SEQUENCES[0])
        self.assertEqual(CYCLE301_SEQUENCES[0], ("090", "076", "607", "073"))
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
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, CYCLE302_NESTED)
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
        unused_288_n = CYCLE288_N_WITH_NEXT
        self.assertEqual(unused_288_n, 13)
        unused_288_no = CYCLE288_N_NO_NEXT
        self.assertEqual(unused_288_no, 0)
        unused_267 = CYCLE267_K_600
        self.assertEqual(unused_267, 4)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_021_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_021)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PREVIOUS_STEM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_UNIQUE_PREVIOUS_STEM_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_5_of_13_and_hypothesis_k_5_holds(self):
        """N_inside=13, K_021=5. Unique-max still 021. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        if self.n_inside != 13:
            self.fail("leftover n=4 remaining I 090 076 N drifted from 13")
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 13)
        self.assertEqual(self.n_line_initial, STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertEqual(self.n_line_initial, STANDING_N_NO_PREVIOUS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertEqual(self.n_with_previous + self.n_line_initial, self.n_inside)
        self.assertEqual(13 + 0, 13)
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(self.k_021, STANDING_K_021)
        self.assertEqual(STANDING_K_021, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_021, 5)
        self.assertEqual(STANDING_K, CYCLE302_K)
        self.assertEqual(STANDING_G, "021")
        self.assertEqual(STANDING_G, CYCLE302_G)
        self.assertEqual(self.g, "021")
        self.assertEqual(self.unique_k, 5)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(STANDING_UNIQUE_MAX_STILL_021)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 8)
        self.assertEqual(self.n_remaining_after_021, STANDING_N_REMAINING_AFTER_021)
        self.assertEqual(STANDING_N_REMAINING_AFTER_021, 8)
        self.assertEqual(STANDING_N_REMAINING_AFTER_021, CYCLE302_N_REMAINING)
        self.assertEqual(self.k_021 + self.n_remaining_after_021, self.n_inside)
        self.assertEqual(5 + 8, 13)
        if self.k_021 != 5:
            self.fail("nested-check K_021 drifted from 5")
        if self.g != "021" or not self.unique:
            self.fail("unique-max previous is no longer 021")
        self.assertTrue(
            i_leftover_n4_remaining_090_076_exactly_5_share_previous_021(
                self.k_021,
                self.unique,
                self.g,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021,
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_exactly_5_share_previous_021",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE302_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE302_G_SITES)
        self.assertTrue(self.equals_cycle302)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE302_G_SITES)
        self.assertTrue(matching_equals_cycle302_g_set(self.matching))
        self.assertEqual(len(CYCLE302_MATCHING_SITES), CYCLE302_K)
        self.assertEqual(CYCLE302_K, 5)
        if len(self.matching) != 5 or not self.equals_cycle302:
            self.fail(
                "leftover n=4 remaining previous-021 set drifted from cycle-302 G set"
            )
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_021_SITES)
        self.assertEqual(self.without, CYCLE302_REMAINING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE260)
        self.assertFalse(STANDING_SAME_AS_CYCLE267)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE300)
        self.assertFalse(STANDING_SAME_AS_CYCLE301)
        self.assertFalse(STANDING_SAME_AS_CYCLE302)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_021_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_021)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_NOT_LOCKED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT)
        self.assertTrue(CYCLE302_CLAIM)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertEqual(CYCLE302_N_DISTINCT, 8)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_n4_remaining_sites_have_previous_021(self):
        """Five leftover n=4 remaining sites are 021 090 076."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(self.matching_previous_4grams, CYCLE302_MATCHING_PREVIOUS_4GRAMS)
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
            self.assertEqual(stems[index - 1], "021")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "021")
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), GRAM3_BACKWARD)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev)
            self.assertEqual(prev4, want_prev)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, CYCLE302_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE302_MATCHING_SITES)
        self.assertTrue(matching_equals_cycle302_g_set(self.matching))
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            prev = site_previous_stem(stems, index, GRAM2)
            self.assertIsNotNone(prev)
            self.assertNotEqual(prev, "021")
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, CYCLE302_MATCHING_SITES)
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_021_SITES)
        self.assertEqual(len(self.without), STANDING_N_REMAINING_AFTER_021)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, prev4, _nxt4), want in zip(
            local,
            STANDING_MATCHING_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertEqual(prev4, want)
        self.assertEqual(
            matching_leftover_n4_remaining_previous_021_local_4gram_rows(),
            matching_leftover_n4_remaining_previous_021_local_4gram_rows(
                STANDING_MATCHING_SITES,
                STANDING_MATCHING_PREVIOUS_4GRAMS,
            ),
        )
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_021)
        self.assertTrue(STANDING_I_ONLY_OF_021_090_076_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_overlap_remaining_after_011_and_258_259_recorded(self):
        """Previous-021 sites overlap remaining-after-011 at Ia8[106]/Ia13[17]; 258/259 at Ia8[106]."""
        self.assertEqual(self.overlap_261, STANDING_OVERLAP_CYCLE261_PREVIOUS_999)
        self.assertEqual(self.overlap_261, ())
        self.assertEqual(self.overlap_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258, ((SIDE_IA, "Ia8", 106),))
        self.assertEqual(self.overlap_after_011, STANDING_OVERLAP_REMAINING_AFTER_011)
        self.assertEqual(
            self.overlap_after_011,
            ((SIDE_IA, "Ia8", 106), (SIDE_IA, "Ia13", 17)),
        )
        self.assertEqual(self.overlap_after_011, CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_BY_X["607"])
        self.assertIn((SIDE_IA, "Ia8", 106), STANDING_MATCHING_SITES)
        self.assertIn((SIDE_IA, "Ia13", 17), STANDING_MATCHING_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertIn((SIDE_IA, "Ia13", 17), CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertNotIn((SIDE_IA, "Ia13", 17), CYCLE259_EXTRA_I_SITES)
        for site in CYCLE261_MATCHING_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        for site in CYCLE267_MATCHING_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(self.claim_holds)
        self.assertEqual(CYCLE261_K_999, 15)
        self.assertEqual(CYCLE261_N_REMAINING_AFTER_999, 41)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        self.assertEqual(len(CYCLE259_EXTRA_I_SITES), 3)
        self.assertEqual(CYCLE259_N_I_ONLY, 2)
        self.assertEqual(CYCLE259_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertTrue(CYCLE259_CLAIM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_302_301_300_288_267_261_260_224_223_still_compute(self):
        """Cycle 302 021/5/13/8, 301 1/0, 300 2/0, 288 G=020 K=4, 267 K_600=4, 261 15/41, 260 34/999/15, 224 13/56, 223 69/3 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_302 = TestMamariILeftoverN4Remaining090076PreviousStemScoreboard()
        prior_302.setUp()
        prior_302.test_counts_8_distinct_previous_stems_g_021_k_5_and_claim_holds()
        prior_302.test_survey_matches_computed_lock()
        self.assertEqual(prior_302.g, "021")
        self.assertEqual(prior_302.k, 5)
        self.assertEqual(prior_302.n_inside, 13)
        self.assertEqual(prior_302.n_line_initial, 0)
        self.assertEqual(prior_302.n_distinct, 8)
        self.assertTrue(prior_302.unique)
        self.assertTrue(prior_302.claim_holds)
        self.assertTrue(CYCLE302_CLAIM)
        self.assertEqual(CYCLE302_G, "021")
        self.assertEqual(CYCLE302_K, 5)
        self.assertEqual(CYCLE302_N_INSIDE, 13)
        self.assertEqual(CYCLE302_N_DISTINCT, 8)
        if (
            prior_302.g != "021"
            or prior_302.k != 5
            or prior_302.n_inside != 13
            or prior_302.n_distinct != 8
            or not prior_302.unique
            or not prior_302.claim_holds
        ):
            self.fail(
                "nested cycle 302 unique-max G=021 K=5 N=13 distinct=8 drifted"
            )
        prior_301 = TestMamariILeftoverN4Remaining090076RemainingAfter011ExtraIFwd4IOnlyScoreboard()
        prior_301.setUp()
        prior_301.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_301.test_survey_matches_computed_lock()
        self.assertEqual(prior_301.n_i_only, 1)
        self.assertEqual(prior_301.n_not_i_only, 0)
        self.assertTrue(prior_301.claim_holds)
        self.assertTrue(CYCLE301_CLAIM)
        self.assertEqual(CYCLE301_N_I_ONLY, 1)
        self.assertEqual(CYCLE301_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE301_SEQUENCES[0], ("090", "076", "607", "073"))
        if prior_301.n_i_only != 1 or prior_301.n_not_i_only != 0:
            self.fail("nested cycle 301 extra-I 4-gram 090 076 607 073 1/0 drifted")
        prior_300 = TestMamariILeftoverN4Remaining090076RemainingAfter0113gramsIOnlyScoreboard()
        prior_300.setUp()
        prior_300.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_300.test_survey_matches_computed_lock()
        self.assertEqual(prior_300.n_i_only, CYCLE300_N_I_ONLY)
        self.assertEqual(prior_300.n_i_only, 2)
        self.assertEqual(prior_300.n_not_i_only, CYCLE300_N_NOT_I_ONLY)
        self.assertEqual(prior_300.n_not_i_only, 0)
        self.assertTrue(prior_300.claim_holds)
        self.assertTrue(CYCLE300_CLAIM)
        if prior_300.n_i_only != 2 or prior_300.n_not_i_only != 0:
            self.fail("nested cycle 300 remaining-after-011 3-grams 2/0 drifted")
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_inside, CYCLE288_N_INSIDE)
        self.assertEqual(prior_288.n_inside, 13)
        self.assertEqual(prior_288.n_with_next, CYCLE288_N_WITH_NEXT)
        self.assertEqual(prior_288.n_no_next, CYCLE288_N_NO_NEXT)
        self.assertEqual(prior_288.n_distinct, CYCLE288_N_DISTINCT)
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, CYCLE288_G)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, CYCLE288_K)
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        if (
            prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or prior_288.claim_holds
        ):
            self.fail("nested cycle 288 share-one-forward lost 6 distinct G=020 K=4 drifted")
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
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertTrue(CYCLE261_CLAIM)
        if prior_261.k_999 != 15 or prior_261.n_remaining_after_999 != 41:
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 N_remaining=41 drifted")
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertTrue(CYCLE260_UNIQUE)
        self.assertFalse(CYCLE260_SHARE_ONE)
        if prior_260.n_distinct != 34 or CYCLE260_G != "999" or CYCLE260_K != 15:
            self.fail("nested cycle 260 34 distinct G=999 K=15 drifted")
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(prior_259.n_i_only, 2)
        self.assertEqual(prior_259.n_not_i_only, 0)
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        if prior_259.n_i_only != 2 or prior_259.n_not_i_only != 0:
            self.fail("nested cycle 259 leftover extra remaining-after-000 extra-I 4-grams 2/0 drifted")
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_258.test_survey_matches_computed_lock()
        self.assertTrue(prior_258.claim_holds)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertEqual(CYCLE258_N_I_ONLY, 19)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        if prior_258.n_i_only != 19 or sum(prior_258.n_extra) != 3:
            self.fail("nested cycle 258 leftover extra remaining-after-000 3-grams 19/0 extra I=3 drifted")
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
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_021)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-303 leftover n=4 remaining previous-021 lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_previous_021"]
        self.assertEqual(lock["cycle"], 303)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 5)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(tuple(lock["backward_3gram"]), ("021", "090", "076"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
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
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 13)
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(
            lock["N_distinct_previous_stems"],
            STANDING_N_DISTINCT_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_distinct_previous_stems"], 8)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "021")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 5)
        self.assertEqual(lock["K_021"], STANDING_K_021)
        self.assertEqual(lock["K_021"], 5)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 8)
        self.assertEqual(lock["N_remaining_after_021"], STANDING_N_REMAINING_AFTER_021)
        self.assertEqual(lock["N_remaining_after_021"], 8)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertTrue(lock["unique_max_still_021"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_sites"]),
            CYCLE302_MATCHING_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle302_g_sites"])
        self.assertEqual(
            lock["matching_equals_cycle302_g_sites"],
            STANDING_MATCHING_EQUALS_CYCLE302_G_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_previous_021_local_4grams"],
            matching_leftover_n4_remaining_previous_021_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_021_sites"]),
            STANDING_REMAINING_AFTER_021_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle302_G_sites"]),
            CYCLE302_MATCHING_SITES,
        )
        self.assertEqual(lock["overlap_cycle261_previous_999_sites"], [])
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE258_EXTRA_I],
            lock["overlap_cycle258_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE259_EXTRA_I],
            lock["overlap_cycle259_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_REMAINING_AFTER_011],
            lock["overlap_remaining_after_011_sites"],
        )
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertEqual(
            list(STANDING_NESTED_LEFTOVER_N4_REMAINING),
            lock["nested_leftover_n4_remaining"],
        )
        self.assertEqual(lock["nested_cycle302_G"], "021")
        self.assertEqual(lock["nested_cycle302_K"], 5)
        self.assertEqual(lock["nested_cycle302_N_inside"], 13)
        self.assertEqual(lock["nested_cycle302_N_line_initial"], 0)
        self.assertEqual(lock["nested_cycle302_N_distinct_previous_stems"], 8)
        self.assertTrue(lock["nested_cycle302_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle301_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle301_N_not_i_only"], 0)
        self.assertEqual(
            tuple(lock["nested_cycle301_extra_i_4gram"]),
            ("090", "076", "607", "073"),
        )
        self.assertEqual(lock["nested_cycle300_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle300_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertFalse(lock["nested_cycle288_share_one_forward_stem"])
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle267_K_600"], 4)
        self.assertTrue(lock["nested_cycle267_exactly_4_share_previous_600"])
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle260_N_distinct_previous_stems"], 34)
        self.assertEqual(lock["nested_cycle260_G"], "999")
        self.assertEqual(lock["nested_cycle260_K"], 15)
        self.assertFalse(lock["nested_cycle260_share_one_previous_stem"])
        self.assertEqual(lock["nested_cycle259_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle259_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle258_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle258_N_extra"], 3)
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_remaining_090_076_exactly_5_share_previous_021"])
        self.assertEqual(
            lock["i_leftover_n4_remaining_090_076_exactly_5_share_previous_021"],
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle260"])
        self.assertFalse(lock["same_as_cycle267"])
        self.assertFalse(lock["same_as_cycle293"])
        self.assertFalse(lock["same_as_cycle300"])
        self.assertFalse(lock["same_as_cycle301"])
        self.assertFalse(lock["same_as_cycle302"])
        self.assertTrue(lock["same_claim_shape_as_cycle267"])
        self.assertTrue(lock["same_claim_shape_as_cycle293"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_021_090_076_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_remaining_after_021"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_021_not_locked"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_extra_previous_stem_is_not_this_cycle"])
        self.assertTrue(
            lock["leftover_extra_remaining_after_999_previous_600_is_not_this_cycle"]
        )
        self.assertTrue(
            lock["leftover_n4_remaining_unique_previous_stem_is_not_this_cycle"]
        )
        self.assertTrue(lock["leftover_n4_remaining_after_011_3grams_is_not_this_cycle"])
        self.assertTrue(
            lock["leftover_n4_remaining_after_011_extra_i_fwd4_is_not_this_cycle"]
        )
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_previous_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_011_3grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_600_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_stem"]["cycle"],
            302,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_stem"]["G"],
            "021",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_stem"]["K"],
            5,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_previous_stem"][
                "i_leftover_n4_remaining_090_076_unique_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"][
                "cycle"
            ],
            301,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"][
                "N_i_only"
            ],
            1,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_3grams_i_only"][
                "cycle"
            ],
            300,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"],
            288,
        )
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"][
                "i_leftover_n4_remaining_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["G"],
            "020",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["K"],
            4,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["cycle"],
            267,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["K_600"],
            4,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["cycle"], 260)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["cycle"], 261)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"][
                "cycle"
            ],
            259,
        )
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


class TestMamariILeftoverN4Remaining090076Previous021ImageSnapshot(unittest.TestCase):
    """Cycle 303 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
