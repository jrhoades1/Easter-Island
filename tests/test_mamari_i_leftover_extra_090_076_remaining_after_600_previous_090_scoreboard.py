"""I's cycle-270 leftover extra remaining-after-600 previous-090 lock.

Cycle 271 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not retune
the forward peel of leftover extra I 090 076 (cycles 225–259).
Does not overwrite cycle 167's 3-gram I-only 16/0 lock. Does
not overwrite cycle 268's 3-gram I-only 6/0 lock. Does not
overwrite cycle 269's previous-4 I-only hapax lock. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Cycle 270 leftover extra remaining-after-600 unique-max
previous stem LOST: 5-way tie at K=2 (090/076/071/045/009),
G=090 by largest-id, N_remaining_after_600=37, distinct=32,
hapax=27. Unique-max G/K is inventory; this cycle peels 090
as exact-K. Same lose path as cycle 234 (tie at K=2), not
cycle 256 all-hapax. Same claim-shape as cycle 235 (exactly
K share G after a unique-max lose with a K=2 tie, largest-id
first) and cycle 264 (exactly 2 share previous 090), leftover
extra remaining-after-600 previous 090 instead of remaining-
after-001 forward 700 / I 999 090 076 previous 090. Cycle 264
K_090=2 is a different cluster (previous of I 999 090 076);
do not confuse with leftover extra remaining-after-600
previous 090. Do not peel remaining-after-090 this cycle.
Do not retune leftover n=4. Do not retune the forward peel.
Off-I T sites are not this cycle.

Hypothesis K=2: leftover extra remaining-after-600 I 090 076
sites include exactly 2 that share previous stem 090
(backward 3-gram 090 090 076). Nested-check leftover extra
set leftover extra==56, N_I==69, K_999==15,
N_remaining_after_999==41, K_600==4, N_remaining_after_600==37
(do not retune 223/224/260/261/266/267/270). Nested-check
cycle 270: unique-max false, 5-way tie at K=2
(090/076/071/045/009), G=090 largest-id, distinct=32,
hapax=27 (do not retune). Measured: K_090=2 at Ia12[42],
Ia14[105]; those matching remaining-after-600 sites equal
the cycle-270 G sites. N_remaining_after_090=35 (37−2).
090 is still a max-K previous token (tied at K=2; largest-id
G=090). Claim that can lose:
i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090.
True only if K_090==2 among leftover extra remaining-after-600
I 090 076. The claim is true. This can lose if nested-check K
differs from 2. Nested cycle 270 unique-max false 5-way K=2
G=090, cycle 267 K_600=4 N_remaining_after_600=37, cycle 266
unique-max G=600 K=4, cycle 264 K_090=2 of I 999 090 076
(different cluster), cycle 261 K_999=15, cycle 223 69/3, and
cycle 207 8/1 on T stay. Do not assume the result; measure.
Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
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
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_600_090_076_i_only_scoreboard import (
    STANDING_I_3GRAM_600_090_076_I_ONLY as CYCLE268_CLAIM,
    STANDING_N_I as CYCLE268_N_I,
    STANDING_N_OFF_I as CYCLE268_N_OFF_I,
    TestMamariI3gram600090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_600_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_600_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE269_ALL_HAPAX,
    STANDING_N_I_ONLY as CYCLE269_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE269_N_NOT_HAPAX,
    TestMamariI600090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_999_090_076_previous_090_scoreboard import (
    STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE264_CLAIM,
    STANDING_K_090 as CYCLE264_K_090,
    STANDING_MATCHING_SITES as CYCLE264_MATCHING_SITES,
    TestMamariI999090076Previous090Scoreboard,
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
    STANDING_N_LEFTOVER_EXTRA as CYCLE261_N_LEFTOVER_EXTRA,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    leftover_extra_with_previous_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE260_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    leftover_extra_backward_3grams,
    leftover_extra_previous_4grams,
    leftover_extra_previous_stems,
    leftover_sites_with_previous,
    leftover_sites_without_previous,
    select_previous_g,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_fwd700_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_2_SHARE_700 as CYCLE235_CLAIM,
    STANDING_K as CYCLE235_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_600,
    STANDING_G as CYCLE270_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE270_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE270_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE270_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE270_N_DISTINCT,
    STANDING_N_HAPAX_REMAINING as CYCLE270_N_HAPAX,
    STANDING_N_REMAINING_AFTER_600 as CYCLE270_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED_AT_K,
    STANDING_REMAINING_SITES as CYCLE270_REMAINING_SITES,
    STANDING_TIED_STEMS as CYCLE270_TIED_STEMS,
    leftover_extra_remaining_after_600,
    leftover_extra_remaining_after_600_nested_counts_hold,
    leftover_extra_remaining_after_600_previous_stems,
    leftover_extra_remaining_after_600_with_g,
    leftover_extra_remaining_after_600_with_previous,
    leftover_extra_remaining_after_600_without_g,
    leftover_extra_remaining_after_600_without_previous,
    matching_leftover_extra_remaining_after_600_local_4gram_rows,
    remaining_after_600_previous_stem_frequency_table,
    select_remaining_after_600_g,
    TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_600_scoreboard import (
    STANDING_G as CYCLE267_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_EXACTLY_4_SHARE_PREVIOUS_600 as CYCLE267_CLAIM,
    STANDING_K_600 as CYCLE267_K_600,
    STANDING_MATCHING_SITES as CYCLE267_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_600 as CYCLE267_N_REMAINING_AFTER_600,
    leftover_extra_remaining_after_999_without_previous_600,
    TestMamariILeftoverExtra090076RemainingAfter999Previous600Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_999,
    STANDING_G as CYCLE266_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE266_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM as CYCLE266_CLAIM,
    STANDING_K as CYCLE266_K,
    STANDING_MATCHING_SITES as CYCLE266_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE266_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_999 as CYCLE266_N_REMAINING,
    leftover_extra_remaining_after_999,
    leftover_extra_remaining_after_999_nested_counts_hold,
    leftover_extra_remaining_after_999_previous_stems,
    leftover_extra_remaining_after_999_with_g,
    leftover_extra_remaining_after_999_without_g,
    select_remaining_after_999_g,
    TestMamariILeftoverExtra090076RemainingAfter999PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
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
LOCKED_PREVIOUS_STEM_999 = "999"
LOCKED_PREVIOUS_STEM_600 = "600"
LOCKED_PREVIOUS_STEM_090 = "090"
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_BACKWARD = ("090", "090", "076")
GRAM3_NESTED_600 = ("600", "090", "076")
GRAM3_NESTED_999 = ("999", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS_LEFTOVER = 56
STANDING_N_NO_PREVIOUS_LEFTOVER = 0
STANDING_K_999 = 15
STANDING_N_REMAINING_AFTER_999 = 41
STANDING_K_600 = 4
STANDING_N_REMAINING_AFTER_600 = 37
STANDING_N_WITH_PREVIOUS = 37
STANDING_N_NO_PREVIOUS = 0
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT_REMAINING = 32
STANDING_N_HAPAX_REMAINING = 27
STANDING_K = 2
STANDING_K_090 = 2
STANDING_G = "090"
STANDING_N_WITHOUT = 35
STANDING_N_REMAINING_AFTER_090 = 35
STANDING_N_TIED_AT_K = 5
STANDING_TIED_STEMS = ("090", "076", "071", "045", "009")
STANDING_OTHER_TIED_STEMS = ("076", "071", "045", "009")
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_090_STILL_MAX_K = True
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia12", 42),
    (SIDE_IA, "Ia14", 105),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("011", "090", "090", "076"),
    ("011", "090", "090", "076"),
)
STANDING_MATCHING_EQUALS_CYCLE270_G_SITES = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090"
)
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090 = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_600_previous_090"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE235 = False
STANDING_SAME_AS_CYCLE264 = False
STANDING_SAME_AS_CYCLE266 = False
STANDING_SAME_AS_CYCLE267 = False
STANDING_SAME_AS_CYCLE270 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE264 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_REMAINING_AFTER_090 = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_090_NOT_LOCKED = True
STANDING_CYCLE264_IS_DIFFERENT_CLUSTER = True
STANDING_OTHER_TIED_STEMS_NOT_LOCKED = True
STANDING_I_ONLY_OF_090_090_076_IS_NOT_THIS_CYCLE = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE167_NOT_OVERWRITTEN = True
STANDING_CYCLE268_NOT_OVERWRITTEN = True
STANDING_CYCLE269_NOT_OVERWRITTEN = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True


def leftover_extra_remaining_after_600_with_previous_090(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-600 sites whose previous token is 090."""
    return leftover_extra_remaining_after_600_with_g(
        sites,
        previous_stems,
        stem=stem,
        locked=locked,
    )


def leftover_extra_remaining_after_600_without_previous_090(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-600 sites whose previous token is not 090."""
    return leftover_extra_remaining_after_600_without_g(
        sites,
        previous_stems,
        stem=stem,
        locked=locked,
    )


def matching_equals_cycle270_g_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle270_g_sites: tuple[tuple[str, str, int], ...] = CYCLE270_MATCHING_SITES,
) -> bool:
    """True iff remaining-after-600 previous-090 sites equal the cycle-270 G set."""
    return matching_sites == cycle270_g_sites


def matching_leftover_extra_remaining_after_600_previous_090_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-600 previous-090 rows."""
    return matching_leftover_extra_remaining_after_600_local_4gram_rows(
        leftover_sites,
        previous_4grams,
    )


def i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(
    k: int,
    expected: int = HYPOTHESIS_K,
) -> bool:
    """True iff K_090 equals the hypothesized 2."""
    return k == expected


class TestILeftoverExtra090076RemainingAfter600Previous090Helpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-600 previous 090. No CV, no LLM."""

    def test_previous_090_requires_remaining_after_600_previous_stem(self):
        """Previous stem 090 is remaining-after-600; locked 999/600 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("090", "090", "076"))
        self.assertEqual(GRAM3_NESTED_600, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_999, ("999", "090", "076"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_600, ("999", "600"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_999, ("999",))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_090 = ["011", "090", "090", "076"]
        self.assertEqual(site_previous_stem(has_090, 2, GRAM2), "090")
        self.assertEqual(site_backward_3gram(has_090, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_090, 2, GRAM2),
            ("011", "090", "090", "076"),
        )
        has_600 = ["076", "600", "090", "076"]
        self.assertEqual(site_previous_stem(has_600, 2, GRAM2), "600")
        self.assertNotEqual(site_previous_stem(has_600, 2, GRAM2), "090")
        has_999 = ["000", "999", "090", "076"]
        self.assertEqual(site_previous_stem(has_999, 2, GRAM2), "999")
        self.assertNotEqual(site_previous_stem(has_999, 2, GRAM2), "090")
        other_prev = ["093", "045", "090", "076"]
        self.assertEqual(site_previous_stem(other_prev, 2, GRAM2), "045")
        self.assertNotEqual(site_backward_3gram(other_prev, 2, GRAM2), GRAM3_BACKWARD)
        one_token_before = ["090", "090", "076"]
        self.assertEqual(site_previous_stem(one_token_before, 1, GRAM2), "090")
        self.assertEqual(site_backward_3gram(one_token_before, 1, GRAM2), GRAM3_BACKWARD)
        self.assertIsNone(site_previous_4gram(one_token_before, 1, GRAM2))
        line_initial = ["090", "076", "012"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        mismatch_071 = ["090", "076", "071", "090"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        mismatch_070 = ["090", "076", "070", "090"]
        self.assertIsNone(site_previous_stem(mismatch_070, 1, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
        )
        planted_stems = ("090", "999", "600", None, "045")
        rem = leftover_extra_remaining_after_600(planted_sites, planted_stems)
        self.assertEqual(rem, (planted_sites[0], planted_sites[3], planted_sites[4]))
        self.assertEqual(
            leftover_extra_remaining_after_600_with_previous_090(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_extra_remaining_after_600_without_previous_090(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[4],),
        )
        self.assertNotIn(planted_sites[1], rem)
        self.assertNotIn(planted_sites[2], rem)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when K=2."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(2)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(0)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(1)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(3)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(4)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(35)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(37)
        )
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 15),)
        planted_stems = ("090",) * 3
        self.assertEqual(
            leftover_extra_remaining_after_600_with_previous_090(
                planted,
                planted_stems,
            ),
            planted,
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(
                len(planted)
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090,
            HYPOTHESIS_K == STANDING_K_090,
        )
        self.assertEqual(
            STANDING_K_090 + STANDING_N_REMAINING_AFTER_090,
            STANDING_N_REMAINING_AFTER_600,
        )
        self.assertEqual(2 + 35, 37)
        self.assertEqual(STANDING_K_600 + STANDING_N_REMAINING_AFTER_600, STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(4 + 37, 41)
        self.assertEqual(STANDING_K_999 + STANDING_N_REMAINING_AFTER_999, STANDING_N_LEFTOVER)
        self.assertEqual(15 + 41, 56)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle270_site_agreement_and_cycle264_cluster_can_diverge(self):
        """Matching sites must equal cycle 270's pair; cycle 264 is a different cluster."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle270_g_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE270_G_SITES)
        self.assertEqual(STANDING_MATCHING_SITES, CYCLE270_MATCHING_SITES)
        self.assertEqual(STANDING_MATCHING_PREVIOUS_4GRAMS, CYCLE270_MATCHING_PREVIOUS_4GRAMS)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle270_g_set(planted))
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(
                len(planted)
            )
        )
        swapped = ((SIDE_IA, "Ia12", 46), (SIDE_IA, "Ia14", 139))
        self.assertFalse(matching_equals_cycle270_g_set(swapped))
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(
                len(swapped)
            )
        )
        self.assertEqual(swapped, CYCLE264_MATCHING_SITES)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE264_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE264_IS_DIFFERENT_CLUSTER)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
            self.assertNotIn(site, CYCLE270_REMAINING_SITES)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertFalse(CYCLE270_UNIQUE)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(CYCLE270_N_TIED_AT_K, 5)
        self.assertEqual(CYCLE270_TIED_STEMS, STANDING_TIED_STEMS)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_I_ONLY_OF_090_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_090)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_090_NOT_LOCKED)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE264)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE264)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertTrue(CYCLE235_CLAIM)
        self.assertEqual(CYCLE235_K, 2)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter600Previous090Scoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-600 previous-090 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.previous_stems = leftover_extra_previous_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.backwards = leftover_extra_backward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.previous_4grams = leftover_extra_previous_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.share_999 = leftover_extra_with_previous_999(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_after_999 = leftover_extra_remaining_after_999(
            self.leftover_sites,
            self.previous_stems,
        )
        self.share_600 = leftover_extra_remaining_after_999_with_g(
            self.leftover_sites,
            self.previous_stems,
            "600",
        )
        self.remaining = leftover_extra_remaining_after_600(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_extra_remaining_after_600_previous_stems(
            self.leftover_sites,
            self.previous_stems,
        )
        self.with_previous = leftover_extra_remaining_after_600_with_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.no_previous = leftover_extra_remaining_after_600_without_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.matching = leftover_extra_remaining_after_600_with_previous_090(
            self.leftover_sites,
            self.previous_stems,
        )
        self.without = leftover_extra_remaining_after_600_without_previous_090(
            self.leftover_sites,
            self.previous_stems,
        )
        self.frequency = remaining_after_600_previous_stem_frequency_table(
            self.leftover_sites,
            self.previous_stems,
            self.backwards,
        )
        self.matching_previous_4grams = leftover_extra_previous_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = CYCLE224_N_INSIDE
        self.n_leftover = len(self.leftover_sites)
        self.n_leftover_extra = self.n_leftover
        self.n_with_previous_leftover = len(
            leftover_sites_with_previous(self.leftover_sites, self.previous_stems)
        )
        self.n_no_previous_leftover = len(
            leftover_sites_without_previous(self.leftover_sites, self.previous_stems)
        )
        self.k_999 = len(self.share_999)
        self.n_remaining_after_999 = len(self.remaining_after_999)
        self.k_600 = len(self.share_600)
        self.n_remaining = len(self.remaining)
        self.n_with_previous = len(self.with_previous)
        self.n_no_previous = len(self.no_previous)
        self.n_distinct = len(self.frequency)
        self.g, self.tiebreak_k, self.unique = select_remaining_after_600_g(
            self.remaining_stems
        )
        self.k = len(self.matching)
        self.k_090 = self.k
        self.n_without = len(self.without)
        self.n_remaining_after_090 = self.n_remaining - self.k_090
        self.tied = tuple(
            stem for stem, count, _sites, _grams in self.frequency if count == 2
        )
        self.equals_cycle270 = matching_equals_cycle270_g_set(self.matching)
        self.claim_holds = (
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(
                self.k_090,
            )
        )

    def test_tokens_and_nested_leftover_extra_56_69_k999_15_k600_4_not_retuned(self):
        """2-gram and leftover extra 56 / N_I=69 / K_999=15 / K_600=4 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("090", "090", "076"))
        self.assertEqual(GRAM3_NESTED_600, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_999, ("999", "090", "076"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_270 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]
        self.assertEqual(prior_270["cycle"], 270)
        self.assertEqual(prior_270["G"], "090")
        self.assertEqual(prior_270["K"], 2)
        self.assertEqual(prior_270["N_remaining_after_600"], 37)
        self.assertEqual(prior_270["N_distinct_remaining"], 32)
        self.assertEqual(prior_270["N_hapax_remaining"], 27)
        self.assertFalse(prior_270["G_uniquely_most_frequent"])
        self.assertEqual(tuple(prior_270["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(prior_270["N_tied_at_K"], 5)
        self.assertFalse(
            prior_270["i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"]
        )
        self.assertFalse(CYCLE270_CLAIM)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_REMAINING, 37)
        self.assertEqual(CYCLE270_N_DISTINCT, 32)
        self.assertEqual(CYCLE270_N_HAPAX, 27)
        self.assertFalse(CYCLE270_UNIQUE)
        if (
            prior_270["G"] != "090"
            or prior_270["K"] != 2
            or prior_270["N_remaining_after_600"] != 37
            or prior_270["N_distinct_remaining"] != 32
            or prior_270["N_hapax_remaining"] != 27
            or prior_270["G_uniquely_most_frequent"]
            or prior_270["N_tied_at_K"] != 5
        ):
            self.fail(
                "nested cycle 270 unique-max false 5-way K=2 G=090 N_remaining=37 "
                "distinct=32 hapax=27 drifted"
            )
        prior_267 = self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]
        self.assertEqual(prior_267["cycle"], 267)
        self.assertEqual(prior_267["K_600"], 4)
        self.assertEqual(prior_267["N_remaining_after_600"], 37)
        self.assertTrue(
            prior_267[
                "i_leftover_extra_090_076_remaining_after_999_exactly_4_share_previous_600"
            ]
        )
        self.assertTrue(CYCLE267_CLAIM)
        self.assertEqual(CYCLE267_K_600, 4)
        self.assertEqual(CYCLE267_N_REMAINING_AFTER_600, 37)
        prior_266 = self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]
        self.assertEqual(prior_266["cycle"], 266)
        self.assertEqual(prior_266["G"], "600")
        self.assertEqual(prior_266["K"], 4)
        self.assertEqual(prior_266["N_remaining_after_999"], 41)
        self.assertEqual(prior_266["N_distinct_remaining"], 33)
        self.assertTrue(prior_266["G_uniquely_most_frequent"])
        self.assertTrue(CYCLE266_CLAIM)
        self.assertEqual(CYCLE266_G, "600")
        self.assertEqual(CYCLE266_K, 4)
        self.assertTrue(CYCLE266_UNIQUE)
        prior_264 = self.survey["i_999_090_076_previous_090"]
        self.assertEqual(prior_264["cycle"], 264)
        self.assertEqual(prior_264["K_090"], 2)
        self.assertTrue(prior_264["i_999_090_076_exactly_2_share_previous_090"])
        self.assertTrue(CYCLE264_CLAIM)
        self.assertEqual(CYCLE264_K_090, 2)
        self.assertNotEqual(CYCLE264_MATCHING_SITES, STANDING_MATCHING_SITES)
        prior_261 = self.survey["i_leftover_extra_090_076_previous_999"]
        self.assertEqual(prior_261["cycle"], 261)
        self.assertEqual(prior_261["K_999"], 15)
        self.assertEqual(prior_261["N_remaining_after_999"], 41)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertEqual(CYCLE261_K_999, 15)
        prior_260 = self.survey["i_leftover_extra_090_076_previous_stem"]
        self.assertEqual(prior_260["cycle"], 260)
        self.assertEqual(prior_260["N_distinct_previous_stems"], 34)
        self.assertEqual(prior_260["G"], "999")
        self.assertEqual(prior_260["K"], 15)
        self.assertFalse(prior_260["i_leftover_extra_090_076_share_one_previous_stem"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_090)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE268_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE269_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_of_37_and_hypothesis_k_2_holds(self):
        """N_remaining_after_600=37, 5-way tie stays, K_090=2. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_previous_leftover, STANDING_N_WITH_PREVIOUS_LEFTOVER)
        self.assertEqual(STANDING_N_WITH_PREVIOUS_LEFTOVER, 56)
        self.assertEqual(self.n_no_previous_leftover, STANDING_N_NO_PREVIOUS_LEFTOVER)
        self.assertEqual(STANDING_N_NO_PREVIOUS_LEFTOVER, 0)
        self.assertEqual(self.k_999, STANDING_K_999)
        self.assertEqual(STANDING_K_999, 15)
        self.assertEqual(self.share_999, CYCLE261_MATCHING_SITES)
        if self.k_999 != 15:
            self.fail("nested cycle 261 K_999 drifted from 15")
        self.assertEqual(self.n_remaining_after_999, STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(STANDING_N_REMAINING_AFTER_999, 41)
        self.assertEqual(self.n_remaining_after_999, CYCLE261_N_REMAINING_AFTER_999)
        self.assertEqual(self.n_remaining_after_999, CYCLE266_N_REMAINING)
        self.assertEqual(self.n_remaining_after_999, self.n_leftover - self.k_999)
        self.assertEqual(56 - 15, 41)
        if self.n_remaining_after_999 != 41:
            self.fail("measured N_remaining_after_999 drifted from 41")
        self.assertEqual(self.k_600, STANDING_K_600)
        self.assertEqual(STANDING_K_600, 4)
        self.assertEqual(self.share_600, CYCLE267_MATCHING_SITES)
        self.assertEqual(self.share_600, CYCLE266_MATCHING_SITES)
        if self.k_600 != 4:
            self.fail("nested cycle 267 K_600 drifted from 4")
        self.assertTrue(
            leftover_extra_remaining_after_600_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining_after_999,
                self.k_600,
                self.n_remaining,
            )
        )
        self.assertTrue(
            leftover_extra_remaining_after_999_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining_after_999,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(STANDING_N_REMAINING_AFTER_600, 37)
        self.assertEqual(self.n_remaining, CYCLE267_N_REMAINING_AFTER_600)
        self.assertEqual(self.n_remaining, CYCLE270_N_REMAINING)
        self.assertEqual(self.n_remaining, self.n_remaining_after_999 - self.k_600)
        self.assertEqual(41 - 4, 37)
        if self.n_remaining != 37:
            self.fail("measured N_remaining_after_600 drifted from 37")
        if self.n_remaining != self.n_remaining_after_999 - self.k_600:
            self.fail("leftover extra remaining-after-600 filter disagrees with nested 41−4")
        self.assertEqual(self.remaining, CYCLE270_REMAINING_SITES)
        self.assertEqual(
            self.remaining,
            leftover_extra_remaining_after_999_without_previous_600(
                self.leftover_sites,
                self.previous_stems,
            ),
        )
        self.assertEqual(
            self.remaining,
            leftover_extra_remaining_after_999_without_g(
                self.leftover_sites,
                self.previous_stems,
                "600",
            ),
        )
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 37)
        self.assertEqual(self.n_no_previous, STANDING_N_NO_PREVIOUS)
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertEqual(self.no_previous, STANDING_NO_PREVIOUS_SITES)
        self.assertEqual(self.n_with_previous + self.n_no_previous, self.n_remaining)
        self.assertEqual(37 + 0, 37)
        for site in self.share_999:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in self.share_600:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING, 32)
        self.assertEqual(self.n_distinct, CYCLE270_N_DISTINCT)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "090")
        self.assertEqual(STANDING_G, CYCLE270_G)
        self.assertEqual(self.tiebreak_k, 2)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertFalse(CYCLE270_UNIQUE)
        self.assertTrue(STANDING_090_STILL_MAX_K)
        self.assertEqual(self.tied, STANDING_TIED_STEMS)
        self.assertEqual(self.tied, CYCLE270_TIED_STEMS)
        self.assertEqual(len(self.tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 5)
        self.assertEqual(STANDING_N_TIED_AT_K, CYCLE270_N_TIED_AT_K)
        if len(self.tied) != 5 or self.tied != CYCLE270_TIED_STEMS:
            self.fail("nested cycle 270 5-way tie at 2 drifted")
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX_REMAINING)
        self.assertEqual(STANDING_N_HAPAX_REMAINING, 27)
        self.assertEqual(CYCLE270_N_HAPAX, 27)
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(self.k_090, STANDING_K_090)
        self.assertEqual(STANDING_K_090, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_090, 2)
        self.assertEqual(STANDING_K, CYCLE270_K)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 35)
        self.assertEqual(self.n_remaining_after_090, STANDING_N_REMAINING_AFTER_090)
        self.assertEqual(STANDING_N_REMAINING_AFTER_090, 35)
        self.assertEqual(self.k_090 + self.n_remaining_after_090, self.n_remaining)
        self.assertEqual(2 + 35, 37)
        if self.k_090 != 2:
            self.fail("nested-check K_090 drifted from 2")
        leftover_g, leftover_k, leftover_unique = select_previous_g(self.previous_stems)
        self.assertEqual(leftover_g, "999")
        self.assertEqual(leftover_k, 15)
        self.assertTrue(leftover_unique)
        rem999_g, rem999_k, rem999_unique = select_remaining_after_999_g(
            leftover_extra_remaining_after_999_previous_stems(
                self.leftover_sites,
                self.previous_stems,
            )
        )
        self.assertEqual(rem999_g, "600")
        self.assertEqual(rem999_k, 4)
        self.assertTrue(rem999_unique)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090(
                self.k_090
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE270_MATCHING_SITES)
        self.assertTrue(self.equals_cycle270)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE270_G_SITES)
        self.assertTrue(matching_equals_cycle270_g_set(self.matching))
        if len(self.matching) != 2 or not self.equals_cycle270:
            self.fail(
                "leftover extra remaining-after-600 previous-090 set drifted from cycle-270 pair"
            )
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE264)
        self.assertFalse(STANDING_SAME_AS_CYCLE266)
        self.assertFalse(STANDING_SAME_AS_CYCLE267)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE264)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_090)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_090_NOT_LOCKED)
        self.assertTrue(STANDING_CYCLE264_IS_DIFFERENT_CLUSTER)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_I_ONLY_OF_090_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertTrue(CYCLE266_CLAIM)
        self.assertTrue(CYCLE264_CLAIM)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertEqual(CYCLE266_N_DISTINCT, 33)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_remaining_after_600_sites_have_previous_090(self):
        """Two remaining-after-600 leftover extra sites are 090 090 076."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(self.matching_previous_4grams, CYCLE270_MATCHING_PREVIOUS_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia12", 42), ("011", "090", "090", "076")),
            ((SIDE_IA, "Ia14", 105), ("011", "090", "090", "076")),
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
            self.assertEqual(stems[index - 1], "090")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "090")
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), GRAM3_BACKWARD)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev)
            self.assertEqual(prev4, want_prev)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, self.remaining)
            self.assertIn(site, CYCLE270_REMAINING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE261_MATCHING_SITES)
            self.assertNotIn(site, CYCLE267_MATCHING_SITES)
            self.assertNotIn(site, CYCLE264_MATCHING_SITES)
            self.assertIn(site, CYCLE270_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE270_MATCHING_SITES)
        self.assertTrue(matching_equals_cycle270_g_set(self.matching))
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            prev = site_previous_stem(stems, index, GRAM2)
            self.assertIsNotNone(prev)
            self.assertNotEqual(prev, "090")
            self.assertNotEqual(prev, "600")
            self.assertNotEqual(prev, "999")
            self.assertIn(site, self.remaining)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE270_MATCHING_SITES)
        for site in self.share_999:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE261_MATCHING_SITES)
        for site in self.share_600:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE267_MATCHING_SITES)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in CYCLE264_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for stem in STANDING_OTHER_TIED_STEMS:
            other = leftover_extra_remaining_after_600_with_g(
                self.leftover_sites,
                self.previous_stems,
                stem,
            )
            self.assertEqual(len(other), 2)
            self.assertNotEqual(other, self.matching)
            for site in other:
                self.assertNotIn(site, self.matching)
                self.assertIn(site, self.remaining)
        self.assertEqual(len(self.without), STANDING_N_REMAINING_AFTER_090)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, prev4, _nxt4), want in zip(
            local,
            STANDING_MATCHING_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertEqual(prev4, want)
        self.assertEqual(
            matching_leftover_extra_remaining_after_600_previous_090_local_4gram_rows(),
            matching_leftover_extra_remaining_after_600_local_4gram_rows(
                STANDING_MATCHING_SITES,
                STANDING_MATCHING_PREVIOUS_4GRAMS,
            ),
        )
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_090)
        self.assertTrue(STANDING_CYCLE264_IS_DIFFERENT_CLUSTER)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_270_267_266_264_261_223_and_207_still_compute(self):
        """Cycle 270 5-way lose, 267 K_600=4, 266 600/4, 264 K_090=2, 261 K_999=15, 223 69/3, 207 8/1 stay."""
        prior_270 = TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard()
        prior_270.setUp()
        prior_270.test_counts_37_remaining_g_090_k_2_five_way_tie_and_hypothesis_loses()
        prior_270.test_survey_matches_computed_lock()
        self.assertEqual(prior_270.g, "090")
        self.assertEqual(prior_270.k, 2)
        self.assertEqual(prior_270.n_remaining, 37)
        self.assertEqual(prior_270.n_distinct, 32)
        self.assertFalse(prior_270.unique)
        self.assertFalse(prior_270.claim_holds)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_REMAINING, 37)
        self.assertEqual(CYCLE270_N_DISTINCT, 32)
        self.assertEqual(prior_270.matching, CYCLE270_MATCHING_SITES)
        self.assertEqual(self.matching, prior_270.matching)
        if (
            prior_270.g != "090"
            or prior_270.k != 2
            or prior_270.n_remaining != 37
            or prior_270.n_distinct != 32
            or prior_270.unique
            or prior_270.claim_holds
        ):
            self.fail(
                "nested cycle 270 leftover extra remaining-after-600 37 / "
                "32 distinct / 5-way tie G=090 K=2 drifted"
            )
        tied = tuple(
            stem for stem, count, _sites, _grams in prior_270.frequency if count == 2
        )
        self.assertEqual(tied, CYCLE270_TIED_STEMS)
        self.assertEqual(len(tied), 5)
        prior_267 = TestMamariILeftoverExtra090076RemainingAfter999Previous600Scoreboard()
        prior_267.setUp()
        prior_267.test_counts_4_of_41_and_hypothesis_k_4_holds()
        prior_267.test_survey_matches_computed_lock()
        self.assertEqual(prior_267.k_600, 4)
        self.assertEqual(prior_267.n_remaining_after_600, 37)
        self.assertTrue(prior_267.claim_holds)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertEqual(CYCLE267_G, "600")
        self.assertEqual(CYCLE267_K_600, 4)
        if prior_267.k_600 != 4 or prior_267.n_remaining_after_600 != 37:
            self.fail("nested cycle 267 K_600=4 N_remaining_after_600=37 drifted")
        prior_266 = TestMamariILeftoverExtra090076RemainingAfter999PreviousStemScoreboard()
        prior_266.setUp()
        prior_266.test_counts_41_remaining_g_600_k_4_and_hypothesis_holds()
        prior_266.test_survey_matches_computed_lock()
        self.assertEqual(prior_266.g, "600")
        self.assertEqual(prior_266.k, 4)
        self.assertTrue(prior_266.unique)
        self.assertTrue(prior_266.claim_holds)
        self.assertTrue(CYCLE266_CLAIM)
        if prior_266.g != "600" or prior_266.k != 4 or not prior_266.unique:
            self.fail("nested cycle 266 unique-max G=600 K=4 drifted")
        prior_264 = TestMamariI999090076Previous090Scoreboard()
        prior_264.setUp()
        prior_264.test_counts_exactly_2_share_previous_090_and_hypothesis_holds()
        prior_264.test_survey_matches_computed_lock()
        self.assertEqual(prior_264.k_090, 2)
        self.assertEqual(prior_264.matching, CYCLE264_MATCHING_SITES)
        self.assertTrue(prior_264.claim_holds)
        self.assertTrue(CYCLE264_CLAIM)
        self.assertEqual(CYCLE264_K_090, 2)
        self.assertNotEqual(prior_264.matching, self.matching)
        if prior_264.k_090 != 2:
            self.fail("nested cycle 264 K_090=2 drifted")
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertTrue(prior_261.claim_holds)
        self.assertTrue(CYCLE261_CLAIM)
        if prior_261.k_999 != 15 or prior_261.n_remaining_after_999 != 41:
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 drifted")
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(prior_260.g, "999")
        self.assertEqual(prior_260.k, 15)
        self.assertFalse(prior_260.claim_holds)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertTrue(CYCLE260_UNIQUE)
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
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, 16)
        self.assertEqual(prior_167.off_i_hits, 0)
        self.assertTrue(CYCLE167_CLAIM)
        self.assertEqual(CYCLE167_N_I, 16)
        self.assertEqual(CYCLE167_N_OFF_I, 0)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_269 = TestMamariI600090076Previous4gramsIOnlyScoreboard()
        prior_269.setUp()
        prior_269.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE269_ALL_HAPAX)
        self.assertEqual(CYCLE269_N_I_ONLY, 6)
        self.assertEqual(CYCLE269_N_NOT_HAPAX, 0)
        prior_268 = TestMamariI3gram600090076IOnlyScoreboard()
        prior_268.setUp()
        prior_268.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE268_CLAIM)
        self.assertEqual(CYCLE268_N_I, 6)
        self.assertEqual(CYCLE268_N_OFF_I, 0)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        unused = CYCLE207_GRAM3
        self.assertEqual(unused, ("090", "076", "070"))
        unused_n = STANDING_N_I
        self.assertEqual(unused_n, 69)
        unused_270 = CYCLE270_N_REMAINING
        self.assertEqual(unused_270, 37)
        unused_266 = CYCLE266_N_REMAINING
        self.assertEqual(unused_266, 41)
        unused_264 = CYCLE264_K_090
        self.assertEqual(unused_264, 2)
        unused_261 = CYCLE261_N_LEFTOVER_EXTRA
        self.assertEqual(unused_261, 56)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_090)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE268_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE269_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-271 leftover extra remaining-after-600 previous-090 lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]
        self.assertEqual(lock["cycle"], 271)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(tuple(lock["backward_3gram"]), ("090", "090", "076"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(
            tuple(lock["locked_previous_stems_after_600"]),
            LOCKED_PREVIOUS_STEMS_AFTER_600,
        )
        self.assertEqual(tuple(lock["locked_previous_stems_after_600"]), ("999", "600"))
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_previous_leftover"], STANDING_N_WITH_PREVIOUS_LEFTOVER)
        self.assertEqual(lock["N_no_previous_leftover"], STANDING_N_NO_PREVIOUS_LEFTOVER)
        self.assertEqual(lock["K_999"], STANDING_K_999)
        self.assertEqual(lock["K_999"], 15)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_999_sites"]),
            CYCLE261_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_999"], STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(lock["N_remaining_after_999"], 41)
        self.assertEqual(lock["K_600"], STANDING_K_600)
        self.assertEqual(lock["K_600"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_600_sites"]),
            CYCLE267_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_600"], STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(lock["N_remaining_after_600"], 37)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_600_sites"]),
            CYCLE270_REMAINING_SITES,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 37)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(lock["N_distinct_remaining"], STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(lock["N_distinct_remaining"], 32)
        self.assertEqual(lock["N_hapax_remaining"], STANDING_N_HAPAX_REMAINING)
        self.assertEqual(lock["N_hapax_remaining"], 27)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "090")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertEqual(lock["K_090"], STANDING_K_090)
        self.assertEqual(lock["K_090"], 2)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertTrue(lock["090_still_max_K"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 5)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 35)
        self.assertEqual(lock["N_remaining_after_090"], STANDING_N_REMAINING_AFTER_090)
        self.assertEqual(lock["N_remaining_after_090"], 35)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_600_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_600_sites"]),
            CYCLE270_MATCHING_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle270_g_sites"])
        self.assertEqual(
            lock["matching_equals_cycle270_g_sites"],
            STANDING_MATCHING_EQUALS_CYCLE270_G_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_600_local_4grams"],
            matching_leftover_extra_remaining_after_600_previous_090_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle270_G_sites"]),
            CYCLE270_MATCHING_SITES,
        )
        self.assertEqual(lock["cycle270_N_remaining_after_600"], CYCLE270_N_REMAINING)
        self.assertEqual(lock["cycle270_N_remaining_after_600"], 37)
        self.assertEqual(lock["cycle270_N_distinct_remaining"], CYCLE270_N_DISTINCT)
        self.assertEqual(lock["cycle270_N_distinct_remaining"], 32)
        self.assertEqual(lock["cycle270_N_hapax_remaining"], CYCLE270_N_HAPAX)
        self.assertEqual(lock["cycle270_N_hapax_remaining"], 27)
        self.assertEqual(lock["cycle270_N_tied_at_K"], CYCLE270_N_TIED_AT_K)
        self.assertEqual(lock["cycle270_N_tied_at_K"], 5)
        self.assertEqual(tuple(lock["cycle270_tied_stems_at_K"]), CYCLE270_TIED_STEMS)
        self.assertFalse(lock["cycle270_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle270_G"], CYCLE270_G)
        self.assertEqual(lock["cycle270_G"], "090")
        self.assertEqual(lock["cycle270_K"], CYCLE270_K)
        self.assertEqual(lock["cycle270_K"], 2)
        self.assertFalse(lock["cycle270_unique_previous_stem"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090"]
        )
        self.assertEqual(
            lock["i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090"],
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090,
        )
        self.assertEqual(lock["nested_cycle270_G"], "090")
        self.assertEqual(lock["nested_cycle270_K"], 2)
        self.assertEqual(lock["nested_cycle270_N_remaining_after_600"], 37)
        self.assertEqual(lock["nested_cycle270_N_distinct_remaining"], 32)
        self.assertEqual(lock["nested_cycle270_N_hapax_remaining"], 27)
        self.assertEqual(lock["nested_cycle270_N_tied_at_K"], 5)
        self.assertFalse(lock["nested_cycle270_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle267_K_600"], 4)
        self.assertEqual(lock["nested_cycle267_N_remaining_after_600"], 37)
        self.assertEqual(lock["nested_cycle266_G"], "600")
        self.assertEqual(lock["nested_cycle266_K"], 4)
        self.assertTrue(lock["nested_cycle266_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle264_K_090"], 2)
        self.assertTrue(lock["nested_cycle264_exactly_2_share_previous_090"])
        self.assertTrue(lock["nested_cycle264_is_different_cluster"])
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle235"])
        self.assertFalse(lock["same_as_cycle264"])
        self.assertFalse(lock["same_as_cycle266"])
        self.assertFalse(lock["same_as_cycle267"])
        self.assertFalse(lock["same_as_cycle270"])
        self.assertTrue(lock["same_claim_shape_as_cycle235"])
        self.assertTrue(lock["same_claim_shape_as_cycle264"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_remaining_after_090"])
        self.assertTrue(lock["leftover_extra_remaining_after_090_not_locked"])
        self.assertTrue(lock["cycle264_is_different_cluster"])
        self.assertTrue(lock["other_tied_stems_not_locked"])
        self.assertTrue(lock["i_only_of_090_090_076_is_not_this_cycle"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle167_not_overwritten"])
        self.assertTrue(lock["cycle268_not_overwritten"])
        self.assertTrue(lock["cycle269_not_overwritten"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["raw_stems_090_kept"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_600_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_999_090_076_previous_090_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["cycle"],
            270,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["G"],
            "090",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["K"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "N_remaining_after_600"
            ],
            37,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "N_tied_at_K"
            ],
            5,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "G_uniquely_most_frequent"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["cycle"],
            267,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["K_600"],
            4,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]["cycle"],
            266,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]["G"],
            "600",
        )
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["cycle"], 264)
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["K_090"], 2)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["cycle"], 261)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["K_999"], 15)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
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


class TestMamariILeftoverExtra090076RemainingAfter600Previous090ImageSnapshot(
    unittest.TestCase
):
    """Cycle 271 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
