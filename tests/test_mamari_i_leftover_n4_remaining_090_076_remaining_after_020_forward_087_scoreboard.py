"""I's cycle-292 leftover n=4 remaining remaining-after-020 forward-087 lock.

Cycle 293 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–287), leftover n=4 remaining
share-one-forward-stem (cycle 288 lost), leftover n=4
remaining exactly 4 share next 020 (cycle 289), 3-gram
090 076 020 I-only (cycle 290), I 090 076 020 forward
4-grams (cycle 291), or leftover n=4 remaining remaining-
after-020 unique next stem (cycle 292). Does not vendor a
new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Cycle 288 leftover n=4 remaining I 090 076 share-one-forward-
stem LOST: unique-max G=020 K=4. Frequency includes 087×3.
Cycle 289 leftover n=4 remaining exactly 4 share next 020
HOLDS; N_remaining_after_020=9. Cycle 292 leftover n=4
remaining remaining-after-020 unique next stem HOLDS: G=087
K=3, N_remaining_after_020=9, N_with_next=9, N_no_next=0,
N_distinct=5, unique_max true. Unique-max G/K is inventory;
this cycle peels 087 as exact-K. Do not peel remaining-after-
087 this cycle. Do not retune leftover n=4. Do not retune
leftover extra peels. Do not lock I-only of leftover n=4
remaining 090 076 087 this cycle (cycle 245 already owns the
3-gram; leftover n=4 remaining 087 may be its extra I).
Off-I T sites are not this cycle. 076 071 and 076 070 do not
count as this 2-gram. Leftover extra sites do not count as
leftover n=4 remaining.

Hypothesis K=3: leftover n=4 remaining remaining-after-020 I
090 076 sites include exactly 3 that share next stem 087
(forward 3-gram 090 076 087). Nested-check leftover n=4
remaining N_inside==13, K_020==4, N_remaining_after_020==9
(do not retune 224/288/289). Nested-check cycle 292: unique-
max true, G=087 K=3, N_distinct=5 (do not retune). Count
leftover n=4 remaining remaining-after-020 I 090 076 sites
whose next token is 087. Cycle 292 listed Ia4[117]/Ia5[28]/
Ia6[78]; measure, do not assume if nested-check differs.
N_remaining_after_087 = N_remaining_after_020 − K_087.
Unique-max next of remaining-after-020 is still 087. Nested-
check each next-087 remaining-after-020 site ⊆ leftover n=4
remaining remaining-after-020 and has next token 087.
Nested-check (compute, do not retune) cycle 245 extra I=3 of
leftover extra 090 076 087: whether leftover n=4 remaining
remaining-after-020 087 sites equal those extra I 090-starts.
Extra I mismatch does not make this claim lose; still lock
the overlap. Claim that can lose:
i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087.
True iff K_087==3 among leftover n=4 remaining remaining-
after-020 I 090 076 and unique-max next of remaining-after-
020 is still 087. The claim is true. Same claim-shape as
cycle 267 (leftover extra remaining-after-999 exactly 4 share
previous 600) and cycle 289 (leftover n=4 remaining exactly 4
share next 020), leftover n=4 remaining remaining-after-020 /
next 087 instead of leftover extra remaining-after-999 /
previous 600. This can lose if nested-check K differs from 3,
or if unique-max is no longer 087. Nested cycle 292 unique-
max G=087 K=3 N_remaining=9 distinct=5, cycle 289 K_020=4,
cycle 288 N_distinct=6 unique-max G=020 K=4, cycle 245 5/0
extra I=3, cycle 224 13/56, and cycle 223 69/3 stay. Do not
assume the result; measure. Do not retune.

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
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    GRAM3 as CYCLE245_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE245_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_087_I_ONLY as CYCLE245_CLAIM,
    STANDING_I_SITES as CYCLE245_I_SITES,
    STANDING_N_EXTRA as CYCLE245_N_EXTRA,
    STANDING_N_I as CYCLE245_N_I,
    STANDING_N_OFF_I as CYCLE245_N_OFF_I,
    TestMamariI3gram090076087IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_600_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_EXACTLY_4_SHARE_PREVIOUS_600 as CYCLE267_CLAIM,
    STANDING_K_600 as CYCLE267_K_600,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_020_scoreboard import (
    GRAM3_FORWARD as GRAM3_NESTED_020,
    STANDING_G as CYCLE289_G,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020 as CYCLE289_CLAIM,
    STANDING_K as CYCLE289_K,
    STANDING_MATCHING_SITES as CYCLE289_MATCHING_SITES,
    STANDING_N_INSIDE as CYCLE289_N_INSIDE,
    STANDING_N_REMAINING_AFTER_020 as CYCLE289_N_REMAINING_AFTER_020,
    STANDING_REMAINING_AFTER_020_SITES as CYCLE289_REMAINING_AFTER_020_SITES,
    TestMamariILeftoverN4Remaining090076Forward020Scoreboard,
    leftover_n4_remaining_with_forward_020,
    leftover_n4_remaining_without_forward_020,
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
    leftover_n4_remaining_forward_3grams,
    leftover_n4_remaining_next_4grams,
    leftover_n4_remaining_next_stems,
    leftover_n4_remaining_sites_with_next,
    leftover_n4_remaining_sites_without_next,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_scoreboard import (
    LOCKED_FORWARD_STEMS,
    STANDING_G as CYCLE292_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE292_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_UNIQUE_NEXT_STEM as CYCLE292_CLAIM,
    STANDING_K as CYCLE292_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE292_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE292_MATCHING_SITES,
    STANDING_N_DISTINCT as CYCLE292_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_020 as CYCLE292_N_REMAINING,
    STANDING_REMAINING_SITES as CYCLE292_REMAINING_SITES,
    leftover_n4_remaining_remaining_after_020,
    leftover_n4_remaining_remaining_after_020_nested_counts_hold,
    leftover_n4_remaining_remaining_after_020_next_stems,
    leftover_n4_remaining_remaining_after_020_with_g,
    leftover_n4_remaining_remaining_after_020_with_next,
    leftover_n4_remaining_remaining_after_020_without_g,
    leftover_n4_remaining_remaining_after_020_without_next,
    matching_leftover_n4_remaining_remaining_after_020_local_4gram_rows,
    select_remaining_after_020_g,
    TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard,
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

HYPOTHESIS_K = 3
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "087")
GRAM3_NESTED_020_TOKENS = ("090", "076", "020")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_NEXT_INSIDE = 13
STANDING_N_NO_NEXT_INSIDE = 0
STANDING_K_020 = 4
STANDING_N_REMAINING_AFTER_020 = 9
STANDING_N_WITH_NEXT = 9
STANDING_N_NO_NEXT = 0
STANDING_NO_NEXT_SITES = ()
STANDING_N_DISTINCT = 5
STANDING_K = 3
STANDING_K_087 = 3
STANDING_G = "087"
STANDING_N_WITHOUT = 6
STANDING_N_REMAINING_AFTER_087 = 6
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia4", 117),
    (SIDE_IA, "Ia5", 28),
    (SIDE_IA, "Ia6", 78),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "087", "291"),
    ("090", "076", "087", "224"),
    ("090", "076", "087", "755"),
)
STANDING_REMAINING_AFTER_087_SITES = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
    (SIDE_IA, "Ia13", 17),
    (SIDE_IA, "Ia14", 54),
)
STANDING_MATCHING_EQUALS_CYCLE292_G_SITES = True
STANDING_MATCHING_EQUALS_CYCLE245_EXTRA_I = True
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_UNIQUE_MAX_STILL_087 = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087"
)
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087 = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE267 = False
STANDING_SAME_AS_CYCLE289 = False
STANDING_SAME_AS_CYCLE292 = False
STANDING_SAME_AS_CYCLE245 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE289 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_087_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_REMAINING_AFTER_087 = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_087_NOT_LOCKED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_CYCLE167_268_292_NOT_OVERWRITTEN = True
STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE = True


def leftover_n4_remaining_remaining_after_020_with_forward_087(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-020 sites whose next token is 087."""
    return leftover_n4_remaining_remaining_after_020_with_g(
        sites,
        next_stems,
        stem=stem,
        locked=locked,
    )


def leftover_n4_remaining_remaining_after_020_without_forward_087(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-020 sites whose next token is not 087."""
    return leftover_n4_remaining_remaining_after_020_without_g(
        sites,
        next_stems,
        stem=stem,
        locked=locked,
    )


def matching_equals_cycle292_g_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle292_g_sites: tuple[tuple[str, str, int], ...] = CYCLE292_MATCHING_SITES,
) -> bool:
    """True iff remaining-after-020 next-087 sites equal the cycle-292 G set."""
    return matching_sites == cycle292_g_sites


def matching_equals_cycle245_extra_i(
    matching_sites: tuple[tuple[str, str, int], ...],
    extra_i: tuple[tuple[str, str, int], ...] = CYCLE245_EXTRA_I_SITES,
) -> bool:
    """True iff remaining-after-020 next-087 sites equal cycle-245 extra I 090-starts."""
    return matching_sites == extra_i


def next_087_sites_subset_of_remaining_after_020(
    matching_sites: tuple[tuple[str, str, int], ...],
    remaining: tuple[tuple[str, str, int], ...],
    next_stems_by_site: dict[tuple[str, str, int], str | None],
    stem: str = STANDING_G,
) -> bool:
    """True iff each next-087 site ⊆ remaining-after-020 and has next token 087."""
    remaining_set = set(remaining)
    return all(
        site in remaining_set and next_stems_by_site.get(site) == stem
        for site in matching_sites
    )


def i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
    k: int,
    unique: bool,
    g: str | None,
    expected: int = HYPOTHESIS_K,
    expected_g: str = STANDING_G,
) -> bool:
    """True iff K_087 equals 3 and unique-max next is still 087."""
    return k == expected and unique and g == expected_g


class TestILeftoverN4Remaining090076RemainingAfter020Forward087Helpers(
    unittest.TestCase
):
    """Helpers on leftover n=4 remaining remaining-after-020 next 087. No CV, no LLM."""

    def test_forward_087_requires_stem_after_2gram_and_not_020(self):
        """Next stem 087 is 090 076 087; next 020 is not remaining-after-020."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "087"))
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(GRAM3_NESTED_020_TOKENS, GRAM3_NESTED_020)
        self.assertEqual(GRAM3_FORWARD[:STANDING_N2], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_087 = ["090", "076", "087", "291"]
        self.assertEqual(site_next_stem(has_087, 0, GRAM2), "087")
        self.assertEqual(site_forward_3gram(has_087, 0, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_087, 0, GRAM2),
            ("090", "076", "087", "291"),
        )
        has_020 = ["090", "076", "020", "010"]
        self.assertEqual(site_next_stem(has_020, 0, GRAM2), "020")
        self.assertNotEqual(site_next_stem(has_020, 0, GRAM2), "087")
        other_next = ["600", "090", "076", "011", "027"]
        self.assertEqual(site_next_stem(other_next, 1, GRAM2), "011")
        self.assertNotEqual(site_forward_3gram(other_next, 1, GRAM2), GRAM3_FORWARD)
        end_of_line = ["999", "021", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
        )
        planted_stems = ("087", "020", None, "011")
        self.assertEqual(
            leftover_n4_remaining_remaining_after_020_with_forward_087(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_020_without_forward_087(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[3],),
        )
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_3_can_fail(self):
        """Boolean is True only when K=3 and unique-max G is 087."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                3, True, "087"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                0, True, "087"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                2, True, "087"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                4, True, "087"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                9, True, "087"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                3, False, "087"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                3, True, "020"
            )
        )
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 2),)
        planted_stems = ("087",) * 4
        self.assertEqual(
            leftover_n4_remaining_remaining_after_020_with_forward_087(
                planted,
                planted_stems,
            ),
            planted,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                len(planted), True, "087"
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087,
            HYPOTHESIS_K == STANDING_K_087 and STANDING_UNIQUE_MAX_STILL_087,
        )
        self.assertEqual(
            STANDING_K_087 + STANDING_N_REMAINING_AFTER_087,
            STANDING_N_REMAINING_AFTER_020,
        )
        self.assertEqual(3 + 6, 9)
        self.assertEqual(STANDING_K_020 + STANDING_N_REMAINING_AFTER_020, STANDING_N_INSIDE)
        self.assertEqual(4 + 9, 13)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle292_set_and_cycle245_extra_can_diverge(self):
        """Cycle-292 G-site equality and cycle-245 extra I equality can fail."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle292_g_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE292_G_SITES)
        self.assertTrue(matching_equals_cycle245_extra_i(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE245_EXTRA_I)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle292_g_set(planted))
        self.assertFalse(matching_equals_cycle245_extra_i(planted))
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                len(planted), True, "087"
            )
        )
        self.assertTrue(STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_087)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_087_NOT_LOCKED)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_087_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE267)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE245)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter020Forward087Scoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-020 forward-087 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.inside_sites = STANDING_INSIDE_SITES
        self.next_stems = leftover_n4_remaining_next_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.forwards = leftover_n4_remaining_forward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.with_next_inside = leftover_n4_remaining_sites_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next_inside = leftover_n4_remaining_sites_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.share_020 = leftover_n4_remaining_with_forward_020(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining = leftover_n4_remaining_remaining_after_020(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_020_next_stems(
            self.inside_sites,
            self.next_stems,
        )
        self.with_next = leftover_n4_remaining_remaining_after_020_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next = leftover_n4_remaining_remaining_after_020_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.matching = leftover_n4_remaining_remaining_after_020_with_forward_087(
            self.inside_sites,
            self.next_stems,
        )
        self.without = leftover_n4_remaining_remaining_after_020_without_forward_087(
            self.inside_sites,
            self.next_stems,
        )
        self.matching_next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_next_inside = len(self.with_next_inside)
        self.n_no_next_inside = len(self.no_next_inside)
        self.k_020 = len(self.share_020)
        self.n_remaining = len(self.remaining)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.k = len(self.matching)
        self.k_087 = self.k
        self.n_without = len(self.without)
        self.n_remaining_after_087 = self.n_remaining - self.k_087
        self.g, self.unique_k, self.unique = select_remaining_after_020_g(
            self.remaining_stems
        )
        self.equals_cycle292 = matching_equals_cycle292_g_set(self.matching)
        self.equals_cycle245 = matching_equals_cycle245_extra_i(self.matching)
        self.next_by_site = dict(zip(self.inside_sites, self.next_stems, strict=True))
        self.subset_ok = next_087_sites_subset_of_remaining_after_020(
            self.matching,
            self.remaining,
            self.next_by_site,
        )
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                self.k_087,
                self.unique,
                self.g,
            )
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_4_9_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/4/9 stay the cycle-289/288/224 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "087"))
        self.assertEqual(GRAM3_FORWARD, CYCLE245_GRAM3)
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
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
        self.assertEqual(STANDING_N_INSIDE, CYCLE289_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_292 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]
        self.assertEqual(prior_292["cycle"], 292)
        self.assertEqual(prior_292["G"], "087")
        self.assertEqual(prior_292["K"], 3)
        self.assertEqual(prior_292["N_remaining_after_020"], 9)
        self.assertEqual(prior_292["N_distinct"], 5)
        self.assertTrue(prior_292["G_uniquely_most_frequent"])
        self.assertTrue(
            prior_292["i_leftover_n4_remaining_090_076_remaining_after_020_unique_next_stem"]
        )
        self.assertTrue(CYCLE292_CLAIM)
        self.assertEqual(CYCLE292_G, "087")
        self.assertEqual(CYCLE292_K, 3)
        self.assertEqual(CYCLE292_N_REMAINING, 9)
        self.assertEqual(CYCLE292_N_DISTINCT, 5)
        self.assertTrue(CYCLE292_UNIQUE)
        if (
            prior_292["G"] != "087"
            or prior_292["K"] != 3
            or prior_292["N_remaining_after_020"] != 9
            or prior_292["N_distinct"] != 5
            or not prior_292["G_uniquely_most_frequent"]
            or not prior_292["i_leftover_n4_remaining_090_076_remaining_after_020_unique_next_stem"]
        ):
            self.fail(
                "nested cycle 292 unique-max G=087 K=3 N_remaining=9 distinct=5 drifted"
            )
        prior_289 = self.survey["i_leftover_n4_remaining_090_076_forward_020"]
        self.assertEqual(prior_289["cycle"], 289)
        self.assertEqual(prior_289["N_inside"], 13)
        self.assertEqual(prior_289["G"], "020")
        self.assertEqual(prior_289["K"], 4)
        self.assertEqual(prior_289["N_remaining_after_020"], 9)
        self.assertTrue(prior_289["i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"])
        self.assertTrue(CYCLE289_CLAIM)
        self.assertEqual(CYCLE289_G, "020")
        self.assertEqual(CYCLE289_K, 4)
        self.assertEqual(CYCLE289_N_REMAINING_AFTER_020, 9)
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
        prior_245 = self.survey["i_3gram_090_076_087_i_only"]
        self.assertEqual(prior_245["cycle"], 245)
        self.assertEqual(prior_245["N_I"], 5)
        self.assertEqual(prior_245["N_off_I"], 0)
        self.assertEqual(prior_245["N_extra"], 3)
        self.assertTrue(prior_245["i_3gram_090_076_087_i_only"])
        self.assertTrue(CYCLE245_CLAIM)
        self.assertEqual(CYCLE245_N_I, 5)
        self.assertEqual(CYCLE245_N_OFF_I, 0)
        self.assertEqual(CYCLE245_N_EXTRA, 3)
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
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_087_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_087)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_087_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_268_292_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_3_of_9_and_hypothesis_k_3_holds(self):
        """N_remaining_after_020=9, K_087=3. Unique-max still 087. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next_inside, STANDING_N_WITH_NEXT_INSIDE)
        self.assertEqual(STANDING_N_WITH_NEXT_INSIDE, 13)
        self.assertEqual(self.n_no_next_inside, STANDING_N_NO_NEXT_INSIDE)
        self.assertEqual(STANDING_N_NO_NEXT_INSIDE, 0)
        self.assertEqual(self.k_020, STANDING_K_020)
        self.assertEqual(STANDING_K_020, CYCLE289_K)
        self.assertEqual(STANDING_K_020, 4)
        self.assertEqual(self.share_020, CYCLE289_MATCHING_SITES)
        if self.k_020 != 4:
            self.fail("nested cycle 289 K_020 drifted from 4")
        self.assertTrue(
            leftover_n4_remaining_remaining_after_020_nested_counts_hold(
                self.n_inside,
                self.n_with_next_inside,
                self.k_020,
                self.n_remaining,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, CYCLE289_N_REMAINING_AFTER_020)
        self.assertEqual(self.n_remaining, CYCLE292_N_REMAINING)
        self.assertEqual(self.n_remaining, self.n_inside - self.k_020)
        self.assertEqual(13 - 4, 9)
        if self.n_remaining != 9:
            self.fail("measured N_remaining_after_020 drifted from 9")
        self.assertEqual(self.remaining, CYCLE292_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE289_REMAINING_AFTER_020_SITES)
        self.assertEqual(
            self.remaining,
            leftover_n4_remaining_without_forward_020(
                self.inside_sites,
                self.next_stems,
            ),
        )
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 9)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 0)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_remaining)
        self.assertEqual(9 + 0, 9)
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(self.k_087, STANDING_K_087)
        self.assertEqual(STANDING_K_087, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_087, 3)
        self.assertEqual(STANDING_K, CYCLE292_K)
        self.assertEqual(STANDING_G, "087")
        self.assertEqual(STANDING_G, CYCLE292_G)
        self.assertEqual(self.g, "087")
        self.assertEqual(self.unique_k, 3)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(STANDING_UNIQUE_MAX_STILL_087)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 6)
        self.assertEqual(self.n_remaining_after_087, STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(self.k_087 + self.n_remaining_after_087, self.n_remaining)
        self.assertEqual(3 + 6, 9)
        if self.k_087 != 3:
            self.fail("nested-check K_087 drifted from 3")
        if self.g != "087" or not self.unique:
            self.fail("unique-max next is no longer 087")
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087(
                self.k_087,
                self.unique,
                self.g,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE292_MATCHING_SITES)
        self.assertTrue(self.equals_cycle292)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE292_G_SITES)
        self.assertTrue(matching_equals_cycle292_g_set(self.matching))
        self.assertEqual(len(CYCLE292_MATCHING_SITES), CYCLE292_K)
        self.assertEqual(CYCLE292_K, 3)
        if len(self.matching) != 3 or not self.equals_cycle292:
            self.fail(
                "leftover n=4 remaining remaining-after-020 next-087 set drifted from cycle-292 G set"
            )
        self.assertTrue(self.subset_ok)
        self.assertTrue(
            next_087_sites_subset_of_remaining_after_020(
                self.matching,
                self.remaining,
                self.next_by_site,
            )
        )
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE267)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE245)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE267)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE289)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_087_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_087)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_087_NOT_LOCKED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertTrue(CYCLE289_CLAIM)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE292_N_DISTINCT, 5)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_remaining_after_020_sites_have_next_087(self):
        """Three remaining-after-020 leftover n=4 remaining sites are 090 076 087."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        self.assertEqual(self.matching_next_4grams, CYCLE292_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia4", 117), ("090", "076", "087", "291")),
            ((SIDE_IA, "Ia5", 28), ("090", "076", "087", "224")),
            ((SIDE_IA, "Ia6", 78), ("090", "076", "087", "755")),
        )
        for (site, nxt), (want_site, want_nxt) in zip(
            zip(self.matching, self.matching_next_4grams, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3_FORWARD)
            self.assertEqual(stems[index + STANDING_N2], "087")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "087")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, self.remaining)
            self.assertIn(site, CYCLE292_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE289_MATCHING_SITES)
            self.assertIn(site, CYCLE292_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE292_MATCHING_SITES)
        self.assertTrue(matching_equals_cycle292_g_set(self.matching))
        self.assertTrue(self.subset_ok)
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "087")
            self.assertNotEqual(nxt, "020")
            self.assertIn(site, self.remaining)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, CYCLE292_MATCHING_SITES)
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_087_SITES)
        self.assertEqual(len(self.without), STANDING_N_REMAINING_AFTER_087)
        for site in self.share_020:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE289_MATCHING_SITES)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(
            matching_leftover_n4_remaining_remaining_after_020_local_4gram_rows(),
            matching_leftover_n4_remaining_remaining_after_020_local_4gram_rows(
                STANDING_MATCHING_SITES,
                STANDING_MATCHING_NEXT_4GRAMS,
            ),
        )
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_087)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_087_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_cycle245_extra_i_equals_matching_087(self):
        """Cycle 245 extra I 090-starts equal leftover n=4 remaining remaining-after-020 087."""
        self.assertEqual(CYCLE245_N_EXTRA, 3)
        self.assertEqual(CYCLE245_EXTRA_I_SITES, STANDING_MATCHING_SITES)
        self.assertEqual(
            CYCLE245_EXTRA_I_SITES,
            (
                (SIDE_IA, "Ia4", 117),
                (SIDE_IA, "Ia5", 28),
                (SIDE_IA, "Ia6", 78),
            ),
        )
        self.assertTrue(matching_equals_cycle245_extra_i(self.matching))
        self.assertTrue(self.equals_cycle245)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE245_EXTRA_I)
        self.assertEqual(self.matching, CYCLE245_EXTRA_I_SITES)
        for site in self.matching:
            self.assertIn(site, CYCLE245_I_SITES)
            self.assertIn(site, CYCLE245_EXTRA_I_SITES)
        leftover_extra_087 = tuple(
            site for site in CYCLE245_I_SITES if site not in CYCLE245_EXTRA_I_SITES
        )
        for site in leftover_extra_087:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        overlap = tuple(site for site in self.matching if site in CYCLE245_EXTRA_I_SITES)
        self.assertEqual(overlap, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE)
        prior_245 = self.survey["i_3gram_090_076_087_i_only"]
        self.assertEqual(prior_245["cycle"], 245)
        self.assertEqual(prior_245["N_I"], 5)
        self.assertEqual(prior_245["N_off_I"], 0)
        self.assertEqual(prior_245["N_extra"], 3)
        extra_245 = tuple(tuple(row) for row in prior_245["extra_i_sites"])
        self.assertEqual(extra_245, CYCLE245_EXTRA_I_SITES)
        self.assertEqual(extra_245, self.matching)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_292_289_288_245_224_223_still_compute(self):
        """Cycle 292 087/3/9/5, 289 K_020=4, 288 N_distinct=6 G=020 K=4, 245 5/0 extra I=3, 224 13/56, 223 69/3 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_292 = TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard()
        prior_292.setUp()
        prior_292.test_counts_9_remaining_g_087_k_3_and_hypothesis_holds()
        prior_292.test_survey_matches_computed_lock()
        self.assertEqual(prior_292.g, "087")
        self.assertEqual(prior_292.k, 3)
        self.assertEqual(prior_292.n_remaining, 9)
        self.assertEqual(prior_292.n_distinct, 5)
        self.assertTrue(prior_292.unique)
        self.assertTrue(prior_292.claim_holds)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertEqual(CYCLE292_G, "087")
        self.assertEqual(CYCLE292_K, 3)
        self.assertEqual(CYCLE292_N_REMAINING, 9)
        self.assertEqual(CYCLE292_N_DISTINCT, 5)
        if (
            prior_292.g != "087"
            or prior_292.k != 3
            or prior_292.n_remaining != 9
            or prior_292.n_distinct != 5
            or not prior_292.unique
            or not prior_292.claim_holds
        ):
            self.fail(
                "nested cycle 292 unique-max G=087 K=3 N_remaining=9 distinct=5 drifted"
            )
        prior_289 = TestMamariILeftoverN4Remaining090076Forward020Scoreboard()
        prior_289.setUp()
        prior_289.test_counts_4_of_13_and_hypothesis_k_4_holds()
        prior_289.test_survey_matches_computed_lock()
        self.assertEqual(prior_289.n_inside, 13)
        self.assertEqual(prior_289.k, 4)
        self.assertEqual(CYCLE289_G, "020")
        self.assertEqual(prior_289.n_remaining_after_020, 9)
        self.assertEqual(prior_289.matching, CYCLE289_MATCHING_SITES)
        self.assertEqual(self.share_020, prior_289.matching)
        self.assertEqual(self.remaining, prior_289.without)
        self.assertTrue(prior_289.claim_holds)
        self.assertTrue(CYCLE289_CLAIM)
        if (
            prior_289.n_inside != 13
            or prior_289.k != 4
            or prior_289.n_remaining_after_020 != 9
        ):
            self.fail(
                "nested cycle 289 leftover n=4 remaining exactly 4 share 020 / N_remaining=9 drifted"
            )
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_inside, 13)
        self.assertEqual(prior_288.n_with_next, 13)
        self.assertEqual(prior_288.n_no_next, 0)
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        if (
            prior_288.n_inside != 13
            or prior_288.n_with_next != 13
            or prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or not prior_288.unique_max
        ):
            self.fail(
                "nested cycle 288 leftover n=4 remaining 13/13/0 N_distinct=6 G=020 K=4 unique-max drifted"
            )
        prior_245 = TestMamariI3gram090076087IOnlyScoreboard()
        prior_245.setUp()
        prior_245.test_i_hits_are_five_on_ia_and_leftover_extra_087_is_subset()
        prior_245.test_3gram_is_zero_off_i_and_i_only()
        prior_245.test_survey_matches_computed_lock()
        self.assertEqual(prior_245.i_hits, CYCLE245_N_I)
        self.assertEqual(prior_245.i_hits, 5)
        self.assertEqual(prior_245.off_i_hits, CYCLE245_N_OFF_I)
        self.assertEqual(prior_245.off_i_hits, 0)
        self.assertEqual(len(prior_245.extra), CYCLE245_N_EXTRA)
        self.assertEqual(len(prior_245.extra), 3)
        self.assertEqual(prior_245.extra, CYCLE245_EXTRA_I_SITES)
        self.assertEqual(prior_245.extra, self.matching)
        self.assertTrue(prior_245.claim_holds)
        self.assertTrue(CYCLE245_CLAIM)
        if prior_245.i_hits != 5 or prior_245.off_i_hits != 0 or len(prior_245.extra) != 3:
            self.fail("nested cycle 245 090 076 087 I-only 5/0 extra I=3 drifted")
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
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_087)
        self.assertTrue(STANDING_CYCLE167_268_292_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-293 leftover n=4 remaining remaining-after-020 087 lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]
        self.assertEqual(lock["cycle"], 293)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 3)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(tuple(lock["forward_3gram"]), ("090", "076", "087"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(tuple(lock["locked_forward_stems"]), ("020",))
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
        self.assertEqual(lock["N_with_next_inside"], STANDING_N_WITH_NEXT_INSIDE)
        self.assertEqual(lock["N_with_next_inside"], 13)
        self.assertEqual(lock["N_no_next_inside"], STANDING_N_NO_NEXT_INSIDE)
        self.assertEqual(lock["N_no_next_inside"], 0)
        self.assertEqual(lock["K_020"], STANDING_K_020)
        self.assertEqual(lock["K_020"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_020_sites"]),
            CYCLE289_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_020"], STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(lock["N_remaining_after_020"], 9)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_020_sites"]),
            CYCLE292_REMAINING_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 9)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 0)
        self.assertEqual(lock["no_next_sites"], [])
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 5)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "087")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 3)
        self.assertEqual(lock["K_087"], STANDING_K_087)
        self.assertEqual(lock["K_087"], 3)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 6)
        self.assertEqual(lock["N_remaining_after_087"], STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(lock["N_remaining_after_087"], 6)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertTrue(lock["unique_max_still_087"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_remaining_after_020_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_remaining_after_020_sites"]),
            CYCLE292_MATCHING_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle292_g_sites"])
        self.assertEqual(
            lock["matching_equals_cycle292_g_sites"],
            STANDING_MATCHING_EQUALS_CYCLE292_G_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle245_extra_i"])
        self.assertEqual(
            lock["matching_equals_cycle245_extra_i"],
            STANDING_MATCHING_EQUALS_CYCLE245_EXTRA_I,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_remaining_after_020_local_4grams"],
            matching_leftover_n4_remaining_remaining_after_020_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_087_sites"]),
            STANDING_REMAINING_AFTER_087_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle292_G_sites"]),
            CYCLE292_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle245_extra_i_sites"]),
            CYCLE245_EXTRA_I_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["overlap_with_cycle245_extra_i"]),
            STANDING_MATCHING_SITES,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087"]
        )
        self.assertEqual(
            lock["i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087"],
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087,
        )
        self.assertEqual(lock["nested_cycle292_G"], "087")
        self.assertEqual(lock["nested_cycle292_K"], 3)
        self.assertEqual(lock["nested_cycle292_N_remaining_after_020"], 9)
        self.assertEqual(lock["nested_cycle292_N_distinct"], 5)
        self.assertTrue(lock["nested_cycle292_unique_next_stem"])
        self.assertEqual(lock["nested_cycle289_K_020"], 4)
        self.assertEqual(lock["nested_cycle289_N_remaining_after_020"], 9)
        self.assertEqual(lock["nested_cycle288_N_distinct"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertFalse(lock["nested_cycle288_share_one_forward_stem"])
        self.assertEqual(lock["nested_cycle245_N_I"], 5)
        self.assertEqual(lock["nested_cycle245_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle245_N_extra"], 3)
        self.assertTrue(lock["nested_cycle245_i_only"])
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle267_K_600"], 4)
        self.assertTrue(lock["nested_cycle267_exactly_4_share_previous_600"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle267"])
        self.assertFalse(lock["same_as_cycle289"])
        self.assertFalse(lock["same_as_cycle292"])
        self.assertFalse(lock["same_as_cycle245"])
        self.assertTrue(lock["same_claim_shape_as_cycle267"])
        self.assertTrue(lock["same_claim_shape_as_cycle289"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_leftover_n4_remaining_090_076_087_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_remaining_after_087"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_087_not_locked"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["cycle167_268_292_not_overwritten"])
        self.assertTrue(lock["extra_i_mismatch_does_not_lose"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_020_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_087_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_600_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["cycle"],
            292,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["G"],
            "087",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["K"],
            3,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"][
                "N_remaining_after_020"
            ],
            9,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["N_distinct"],
            5,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"][
                "i_leftover_n4_remaining_090_076_remaining_after_020_unique_next_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_020"]["cycle"], 289)
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_020"]["K"], 4)
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"]["N_remaining_after_020"],
            9,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["N_distinct_next_stems"],
            6,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["G"], "020")
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["K"], 4)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["cycle"], 245)
        self.assertTrue(self.survey["i_3gram_090_076_087_i_only"]["i_3gram_090_076_087_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["N_extra"], 3)
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


class TestMamariILeftoverN4Remaining090076RemainingAfter020Forward087ImageSnapshot(
    unittest.TestCase
):
    """Cycle 293 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
