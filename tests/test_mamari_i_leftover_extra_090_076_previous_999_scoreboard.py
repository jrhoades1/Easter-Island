"""I's cycle-260 leftover extra 2-gram previous-999 cluster lock.

Cycle 261 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not retune
the forward peel of leftover extra I 090 076 (cycles 225–259).
Does not peel leftover-of-leftover extra I this cycle. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Cycle 260 lost share-one-previous-stem: N_leftover_extra=56,
N_with_previous=56, N_no_previous=0, N_distinct=34, most
frequent previous stem G=999 K=15 (report; that claim is
share-one, not exactly-K). Unique-max G=999 K=15 is inventory
for this peel; unique-max alone did not make share-one true.
This cycle locks the largest leftover extra previous cluster
instead. Do not lock leftover extra remaining-after-999
previous stems. Off-I T sites are not this cycle. I-only of
leftover extra 4-grams is leftover-of-leftover for a later
cycle. 076 071 and 076 070 do not count as this 2-gram.
Inside-family sites do not count as leftover extra. Inside-
family 999 090 076 (leftover n=4 remaining 999 021 090 076)
does not count.

Hypothesis K=15: leftover extra I 090 076 sites include
exactly 15 that share previous stem 999 (backward 3-gram
999 090 076). Nested-check leftover extra set N_I==69,
leftover extra==56, N_with_previous==56, N_no_previous==0
(do not retune cycles 223/224/260). Nested-check cycle 260:
share-one-previous-stem false, 34 distinct previous stems,
unique-max G=999 K=15 (do not retune). Nested-check cycle
225: share-one-forward-stem false, 30 distinct next stems,
G=070 K=8 (do not retune). Measured: K_999=15 at Ia1[2],
Ia2[10], Ia3[37], Ia3[71], Ia4[112], Ia4[154], Ia5[2],
Ia5[23], Ia6[92], Ia7[68], Ia7[129], Ia9[129], Ia12[47],
Ia13[109], Ia14[140]; those matching leftover extra sites
equal the cycle-260 G sites. N_remaining_after_999=41
(56−15). Unique-max previous is still 999. Claim that can
lose: i_leftover_extra_090_076_exactly_15_share_previous_999.
True only if K_999==15 and unique-max previous is still 999.
The claim is true. Same claim-shape as cycle 226 (leftover
extra 090 076 exactly 8 share forward 070), previous 999
instead of forward 070. This can lose if nested-check K
differs from 15, or if unique-max is no longer 999. Nested
cycle 260 34 distinct G=999 K=15, cycle 259 extra-I 4-grams
2/0, cycle 258 19/19 extra I=3, cycle 257 19/19 hapax,
cycle 256 unique-max false N_remaining11=19 K=1 G=755,
cycle 226 exactly 8 share forward 070, cycle 225 30
distinct G=070 K=8, cycle 223 69/3, and cycle 207 8/1 stay.
Do not assume the result; measure. Do not retune.

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
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
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
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_070_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070 as CYCLE226_CLAIM,
    STANDING_K as CYCLE226_K,
    STANDING_MATCHING_SITES as CYCLE226_MATCHING,
    TestMamariILeftoverExtra090076Forward070Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE225_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_K as CYCLE225_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE225_N_LEFTOVER,
    STANDING_N_NO_NEXT as CYCLE225_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE225_N_WITH_NEXT,
    TestMamariILeftoverExtra090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_G_SITES as CYCLE260_G_SITES,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE260_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE260_N_LEFTOVER,
    STANDING_N_LEFTOVER_EXTRA as CYCLE260_N_LEFTOVER_EXTRA,
    STANDING_N_NO_PREVIOUS as CYCLE260_N_NO_PREVIOUS,
    STANDING_N_WITH_PREVIOUS as CYCLE260_N_WITH_PREVIOUS,
    STANDING_NO_PREVIOUS_SITES,
    leftover_extra_backward_3grams,
    leftover_extra_previous_4grams,
    leftover_extra_previous_stems,
    leftover_sites_with_previous,
    leftover_sites_without_previous,
    select_previous_g,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE257_CLAIM,
    TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    STANDING_G as CYCLE256_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
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

HYPOTHESIS_K = 15
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_BACKWARD = ("999", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS = 56
STANDING_N_NO_PREVIOUS = 0
STANDING_K = 15
STANDING_K_999 = 15
STANDING_G = "999"
STANDING_N_WITHOUT = 41
STANDING_N_REMAINING_AFTER_999 = 41
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia2", 10),
    (SIDE_IA, "Ia3", 37),
    (SIDE_IA, "Ia3", 71),
    (SIDE_IA, "Ia4", 112),
    (SIDE_IA, "Ia4", 154),
    (SIDE_IA, "Ia5", 2),
    (SIDE_IA, "Ia5", 23),
    (SIDE_IA, "Ia6", 92),
    (SIDE_IA, "Ia7", 68),
    (SIDE_IA, "Ia7", 129),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia12", 47),
    (SIDE_IA, "Ia13", 109),
    (SIDE_IA, "Ia14", 140),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("602", "999", "090", "076"),
    ("070", "999", "090", "076"),
    ("000", "999", "090", "076"),
    ("499", "999", "090", "076"),
    ("060", "999", "090", "076"),
    ("254", "999", "090", "076"),
    ("000", "999", "090", "076"),
    ("381", "999", "090", "076"),
    ("023", "999", "090", "076"),
    ("064", "999", "090", "076"),
    ("518", "999", "090", "076"),
    ("075", "999", "090", "076"),
    ("090", "999", "090", "076"),
    ("700", "999", "090", "076"),
    ("090", "999", "090", "076"),
)
STANDING_MATCHING_EQUALS_CYCLE260_G_SITES = True
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_UNIQUE_MAX_STILL_999 = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_exactly_15_share_previous_999"
STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 = True
STANDING_RESULT = "i_leftover_extra_090_076_previous_999"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE226 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226 = True
STANDING_SAME_AS_CYCLE260 = False
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_OF_LEFTOVER_EXTRA_I_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_NOT_LOCKED = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_INSIDE_FAMILY_999_090_076_DOES_NOT_COUNT = True


def leftover_extra_with_previous_999(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites whose previous token is 999."""
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev == stem
    )


def leftover_extra_without_previous_999(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites whose previous token is not 999, or none."""
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev != stem
    )


def matching_equals_cycle260_g_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle260_g_sites: tuple[tuple[str, str, int], ...] = CYCLE260_G_SITES,
) -> bool:
    """True iff leftover extra previous-999 sites equal the cycle-260 G set."""
    return matching_sites == cycle260_g_sites


def matching_leftover_extra_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra previous-4-gram rows."""
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


def i_leftover_extra_090_076_exactly_15_share_previous_999(
    k: int,
    unique: bool,
    g: str | None,
    expected: int = HYPOTHESIS_K,
    expected_g: str = STANDING_G,
) -> bool:
    """True iff K_999 equals 15 and unique-max previous is still 999."""
    return k == expected and unique and g == expected_g


class TestILeftoverExtra090076Previous999Helpers(unittest.TestCase):
    """Helpers on leftover extra I 090 076 previous 999. No CV, no LLM."""

    def test_previous_999_requires_stem_before_2gram(self):
        """Previous stem 999 is 999 090 076; line-initial is no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("999", "090", "076"))
        self.assertEqual(GRAM3_BACKWARD[1:], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_999 = ["602", "999", "090", "076", "012", "076"]
        self.assertEqual(site_previous_stem(has_999, 2, GRAM2), "999")
        self.assertEqual(site_backward_3gram(has_999, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_999, 2, GRAM2),
            ("602", "999", "090", "076"),
        )
        other_prev = ["093", "045", "090", "076"]
        self.assertEqual(site_previous_stem(other_prev, 2, GRAM2), "045")
        self.assertNotEqual(site_backward_3gram(other_prev, 2, GRAM2), GRAM3_BACKWARD)
        one_token_before = ["999", "090", "076"]
        self.assertEqual(site_previous_stem(one_token_before, 1, GRAM2), "999")
        self.assertEqual(site_backward_3gram(one_token_before, 1, GRAM2), GRAM3_BACKWARD)
        self.assertIsNone(site_previous_4gram(one_token_before, 1, GRAM2))
        line_initial = ["090", "076", "012"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(line_initial, 0, GRAM2))
        mismatch_071 = ["999", "076", "071", "090"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        mismatch_070 = ["999", "076", "070", "090"]
        self.assertIsNone(site_previous_stem(mismatch_070, 1, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_999_090_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_15_can_fail(self):
        """Boolean is True only when K=15 and unique-max G is 999."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_extra_090_076_exactly_15_share_previous_999(15, True, "999")
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(0, True, "999")
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(8, True, "999")
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(14, True, "999")
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(16, True, "999")
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(56, True, "999")
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(15, False, "999")
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(15, True, "600")
        )
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 15),)
        planted_stems = ("999",) * 16
        self.assertEqual(
            leftover_extra_with_previous_999(planted, planted_stems),
            planted,
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(len(planted), True, "999")
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_exactly_15_share_previous_999",
        )
        self.assertTrue(STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999)
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999,
            HYPOTHESIS_K == STANDING_K_999 and STANDING_UNIQUE_MAX_STILL_999,
        )
        self.assertEqual(STANDING_K_999 + STANDING_N_REMAINING_AFTER_999, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(15 + 41, 56)
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT, STANDING_N_LEFTOVER)
        self.assertEqual(provider.get_call_history(), [])

    def test_inside_family_and_cycle260_set_can_diverge(self):
        """Inside leftover n=4 remaining is not leftover extra; cycle-260 equality can fail."""
        provider = MockProvider()
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(matching_equals_cycle260_g_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE260_G_SITES)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle260_g_set(planted))
        self.assertFalse(
            i_leftover_extra_090_076_exactly_15_share_previous_999(len(planted), True, "999")
        )
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_NOT_LOCKED)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE260)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076Previous999Scoreboard(unittest.TestCase):
    """Cited-fixture leftover extra 090 076 previous-999 lock. Mock only."""

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
        self.with_previous = leftover_sites_with_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.no_previous = leftover_sites_without_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.matching = leftover_extra_with_previous_999(
            self.leftover_sites,
            self.previous_stems,
        )
        self.without = leftover_extra_without_previous_999(
            self.leftover_sites,
            self.previous_stems,
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
        self.n_with_previous = len(self.with_previous)
        self.n_no_previous = len(self.no_previous)
        self.k = len(self.matching)
        self.k_999 = self.k
        self.n_without = len(self.without)
        self.n_remaining_after_999 = self.n_leftover_extra - self.k_999
        self.g, self.unique_k, self.unique = select_previous_g(self.previous_stems)
        self.equals_cycle260 = matching_equals_cycle260_g_set(self.matching)
        self.claim_holds = i_leftover_extra_090_076_exactly_15_share_previous_999(
            self.k_999,
            self.unique,
            self.g,
        )

    def test_tokens_and_sites_are_cycle_260_leftover_extra_not_retuned(self):
        """2-gram and leftover extra 56/56/0 stay the cycle-260/224/223 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("999", "090", "076"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_i, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE260_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_260 = self.survey["i_leftover_extra_090_076_previous_stem"]
        self.assertEqual(prior_260["cycle"], 260)
        self.assertEqual(prior_260["N_leftover"], 56)
        self.assertEqual(prior_260["N_leftover_extra"], 56)
        self.assertEqual(prior_260["N_with_previous"], 56)
        self.assertEqual(prior_260["N_no_previous"], 0)
        self.assertEqual(prior_260["N_distinct_previous_stems"], 34)
        self.assertEqual(prior_260["G"], "999")
        self.assertEqual(prior_260["K"], 15)
        self.assertTrue(prior_260["g_uniquely_most_frequent"])
        self.assertFalse(prior_260["i_leftover_extra_090_076_share_one_previous_stem"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_260["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        if (
            prior_260["N_distinct_previous_stems"] != 34
            or prior_260["G"] != "999"
            or prior_260["K"] != 15
            or prior_260["i_leftover_extra_090_076_share_one_previous_stem"]
        ):
            self.fail("nested cycle 260 34 distinct G=999 K=15 share-one-previous lost drifted")
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertFalse(CYCLE224_ALL_INSIDE)
        prior_225 = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(prior_225["cycle"], 225)
        self.assertFalse(prior_225["i_leftover_extra_090_076_share_one_forward_stem"])
        self.assertEqual(prior_225["N_distinct_next_stems"], 30)
        self.assertEqual(prior_225["G"], "070")
        self.assertEqual(prior_225["K"], 8)
        if (
            prior_225["N_distinct_next_stems"] != 30
            or prior_225["G"] != "070"
            or prior_225["K"] != 8
            or prior_225["i_leftover_extra_090_076_share_one_forward_stem"]
        ):
            self.fail("nested cycle 225 30 distinct G=070 K=8 share-one-forward lost drifted")
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_OF_LEFTOVER_EXTRA_I_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_NOT_LOCKED)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_15_of_56_and_hypothesis_k_15_holds(self):
        """N_leftover_extra=56, N_with_previous=56, K_999=15. Claim holds."""
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
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, CYCLE260_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 56)
        self.assertEqual(self.n_no_previous, STANDING_N_NO_PREVIOUS)
        self.assertEqual(STANDING_N_NO_PREVIOUS, CYCLE260_N_NO_PREVIOUS)
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertEqual(self.no_previous, STANDING_NO_PREVIOUS_SITES)
        self.assertEqual(STANDING_NO_PREVIOUS_SITES, ())
        self.assertEqual(self.n_with_previous + self.n_no_previous, self.n_leftover)
        self.assertEqual(56 + 0, 56)
        if (
            self.n_leftover_extra != 56
            or self.n_with_previous != 56
            or self.n_no_previous != 0
        ):
            self.fail("nested cycle 260 leftover extra 56/56/0 drifted")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(self.k_999, STANDING_K_999)
        self.assertEqual(STANDING_K_999, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_999, 15)
        self.assertEqual(STANDING_K, CYCLE260_K)
        self.assertEqual(STANDING_G, "999")
        self.assertEqual(STANDING_G, CYCLE260_G)
        self.assertEqual(self.g, "999")
        self.assertEqual(self.unique_k, 15)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(STANDING_UNIQUE_MAX_STILL_999)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 41)
        self.assertEqual(self.n_remaining_after_999, STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(STANDING_N_REMAINING_AFTER_999, 41)
        self.assertEqual(self.k_999 + self.n_remaining_after_999, self.n_leftover_extra)
        self.assertEqual(15 + 41, 56)
        if self.k_999 != 15:
            self.fail("nested-check K_999 drifted from 15")
        if self.g != "999" or not self.unique:
            self.fail("unique-max previous is no longer 999")
        self.assertTrue(
            i_leftover_extra_090_076_exactly_15_share_previous_999(
                self.k_999,
                self.unique,
                self.g,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999,
        )
        self.assertTrue(STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_exactly_15_share_previous_999",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE260_G_SITES)
        self.assertTrue(self.equals_cycle260)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE260_G_SITES)
        self.assertTrue(matching_equals_cycle260_g_set(self.matching))
        self.assertEqual(len(CYCLE260_G_SITES), CYCLE260_K)
        self.assertEqual(CYCLE260_K, 15)
        if len(self.matching) != 15 or not self.equals_cycle260:
            self.fail("leftover extra previous-999 set drifted from cycle-260 G set")
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE260)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_OF_LEFTOVER_EXTRA_I_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_NOT_LOCKED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_sites_equal_cycle_260_g(self):
        """Fifteen leftover extra sites are 999 090 076 and equal cycle-260 G."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
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
            self.assertEqual(stems[index - 1], "999")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "999")
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), GRAM3_BACKWARD)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev)
            self.assertEqual(prev4, want_prev)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertIn(site, CYCLE260_G_SITES)
        self.assertEqual(self.matching, CYCLE260_G_SITES)
        self.assertTrue(matching_equals_cycle260_g_set(self.matching))
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            prev = site_previous_stem(stems, index, GRAM2)
            self.assertNotEqual(prev, "999")
            self.assertNotIn(site, CYCLE260_G_SITES)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.matching)
        self.assertEqual(len(self.without), STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_260_259_258_257_256_226_225_223_and_207_still_compute(self):
        """Cycle 260 34/999/15, 259 2/0, 258 19/19 extra I=3, 257 19/19, 256 19/K=1/G=755, 226 K=8, 225 30/070/8, 223 69/3, 207 8/1 stay."""
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_leftover_extra, 56)
        self.assertEqual(prior_260.n_with_previous, 56)
        self.assertEqual(prior_260.n_no_previous, 0)
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(prior_260.g, "999")
        self.assertEqual(prior_260.k, 15)
        self.assertTrue(prior_260.unique)
        self.assertFalse(prior_260.claim_holds)
        self.assertFalse(CYCLE260_SHARE_ONE)
        if (
            prior_260.n_leftover_extra != 56
            or prior_260.n_with_previous != 56
            or prior_260.n_no_previous != 0
            or prior_260.n_distinct != 34
            or prior_260.g != "999"
            or prior_260.k != 15
        ):
            self.fail("nested cycle 260 leftover extra 56/56/0 N_distinct=34 G=999 K=15 drifted")
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(prior_259.n_i_only, 2)
        self.assertEqual(prior_259.n_not_i_only, 0)
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        if prior_259.n_i_only != 2 or prior_259.n_not_i_only != 0:
            self.fail("nested cycle 259 extra-I 4-grams 2/0 drifted")
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_258.test_survey_matches_computed_lock()
        self.assertEqual(prior_258.n_i_only, 19)
        self.assertEqual(prior_258.n_not_i_only, 0)
        self.assertEqual(sum(prior_258.n_extra), 3)
        self.assertTrue(prior_258.claim_holds)
        self.assertTrue(CYCLE258_CLAIM)
        if (
            prior_258.n_i_only != 19
            or prior_258.n_not_i_only != 0
            or sum(prior_258.n_extra) != 3
        ):
            self.fail("nested cycle 258 remaining-after-000 3-grams 19/19 extra I=3 drifted")
        prior_257 = TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard()
        prior_257.setUp()
        prior_257.test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds()
        prior_257.test_survey_matches_computed_lock()
        self.assertEqual(prior_257.n_i_only, 19)
        self.assertEqual(prior_257.n_not_i_only, 0)
        self.assertTrue(prior_257.claim_holds)
        self.assertTrue(CYCLE257_CLAIM)
        if prior_257.n_i_only != 19 or prior_257.n_not_i_only != 0:
            self.fail("nested cycle 257 remaining-after-000 forward 4-grams 19/19 hapax drifted")
        prior_256 = TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard()
        prior_256.setUp()
        prior_256.test_counts_19_remaining11_all_hapax_g_755_k_1_and_hypothesis_loses()
        prior_256.test_survey_matches_computed_lock()
        self.assertEqual(prior_256.n_remaining11, 19)
        self.assertEqual(prior_256.k, 1)
        self.assertEqual(prior_256.g, "755")
        self.assertFalse(prior_256.unique)
        self.assertFalse(prior_256.claim_holds)
        self.assertFalse(CYCLE256_CLAIM)
        if (
            prior_256.n_remaining11 != 19
            or prior_256.k != 1
            or prior_256.g != "755"
            or prior_256.unique
        ):
            self.fail("nested cycle 256 unique-max false N_remaining11=19 K=1 G=755 drifted")
        prior_226 = TestMamariILeftoverExtra090076Forward070Scoreboard()
        prior_226.setUp()
        prior_226.test_counts_8_of_56_and_hypothesis_k_8_holds()
        prior_226.test_survey_matches_computed_lock()
        self.assertEqual(prior_226.k, CYCLE226_K)
        self.assertEqual(prior_226.k, 8)
        self.assertEqual(prior_226.matching, CYCLE226_MATCHING)
        self.assertTrue(prior_226.claim_holds)
        self.assertTrue(CYCLE226_CLAIM)
        if prior_226.k != 8 or not prior_226.claim_holds:
            self.fail("nested cycle 226 leftover extra exactly 8 share forward 070 drifted")
        prior_225 = TestMamariILeftoverExtra090076ForwardStemScoreboard()
        prior_225.setUp()
        prior_225.test_counts_30_distinct_next_stems_and_claim_loses()
        prior_225.test_survey_matches_computed_lock()
        self.assertEqual(prior_225.n_leftover, CYCLE225_N_LEFTOVER)
        self.assertEqual(prior_225.n_leftover, 56)
        self.assertEqual(prior_225.n_with_next, CYCLE225_N_WITH_NEXT)
        self.assertEqual(prior_225.n_no_next, CYCLE225_N_NO_NEXT)
        self.assertEqual(prior_225.n_distinct, CYCLE225_N_DISTINCT)
        self.assertEqual(prior_225.n_distinct, 30)
        self.assertEqual(prior_225.g, CYCLE225_G)
        self.assertEqual(prior_225.g, "070")
        self.assertEqual(prior_225.k, CYCLE225_K)
        self.assertEqual(prior_225.k, 8)
        self.assertFalse(prior_225.claim_holds)
        self.assertFalse(CYCLE225_SHARE_ONE)
        if (
            prior_225.n_distinct != 30
            or prior_225.g != "070"
            or prior_225.k != 8
            or prior_225.claim_holds
        ):
            self.fail("nested cycle 225 share-one-forward lost 30 distinct G=070 K=8 drifted")
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
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        unused = CYCLE207_GRAM3
        self.assertEqual(unused, ("090", "076", "070"))
        unused_n = CYCLE224_N_I
        self.assertEqual(unused_n, 69)
        unused_256 = CYCLE256_N_REMAINING11
        self.assertEqual(unused_256, 19)
        unused_256k = CYCLE256_K
        self.assertEqual(unused_256k, 1)
        unused_256g = CYCLE256_G
        self.assertEqual(unused_256g, "755")
        unused_260_extra = CYCLE260_N_LEFTOVER_EXTRA
        self.assertEqual(unused_260_extra, 56)
        unused_260_unique = CYCLE260_UNIQUE
        self.assertTrue(unused_260_unique)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_OF_LEFTOVER_EXTRA_I_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-261 leftover extra previous-999 lock."""
        lock = self.survey["i_leftover_extra_090_076_previous_999"]
        self.assertEqual(lock["cycle"], 261)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 15)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
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
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 56)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "999")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 15)
        self.assertEqual(lock["K_999"], STANDING_K_999)
        self.assertEqual(lock["K_999"], 15)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 41)
        self.assertEqual(lock["N_remaining_after_999"], STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(lock["N_remaining_after_999"], 41)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertTrue(lock["unique_max_still_999"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_sites"]),
            CYCLE260_G_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle260_g_sites"])
        self.assertEqual(
            lock["matching_equals_cycle260_g_sites"],
            STANDING_MATCHING_EQUALS_CYCLE260_G_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_local_4grams"],
            matching_leftover_extra_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle260_G_sites"]),
            CYCLE260_G_SITES,
        )
        self.assertEqual(lock["cycle260_N_distinct_previous_stems"], CYCLE260_N_DISTINCT)
        self.assertEqual(lock["cycle260_N_distinct_previous_stems"], 34)
        self.assertEqual(lock["cycle260_G"], CYCLE260_G)
        self.assertEqual(lock["cycle260_K"], CYCLE260_K)
        self.assertEqual(lock["cycle260_K"], 15)
        self.assertFalse(lock["cycle260_share_one_previous_stem"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_extra_090_076_exactly_15_share_previous_999"])
        self.assertEqual(
            lock["i_leftover_extra_090_076_exactly_15_share_previous_999"],
            STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999,
        )
        self.assertEqual(lock["nested_cycle259_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle259_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle258_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle258_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle258_N_extra"], 3)
        self.assertEqual(lock["nested_cycle257_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle257_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle256_N_remaining11"], 19)
        self.assertEqual(lock["nested_cycle256_K"], 1)
        self.assertEqual(lock["nested_cycle256_G"], "755")
        self.assertFalse(lock["nested_cycle256_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle226_K"], 8)
        self.assertTrue(lock["nested_cycle226_exactly_8_share_forward_070"])
        self.assertEqual(lock["nested_cycle225_N_distinct_next_stems"], 30)
        self.assertEqual(lock["nested_cycle225_G"], "070")
        self.assertEqual(lock["nested_cycle225_K"], 8)
        self.assertFalse(lock["nested_cycle225_share_one_forward_stem"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle226"])
        self.assertTrue(lock["same_claim_shape_as_cycle226"])
        self.assertFalse(lock["same_as_cycle260"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["leftover_of_leftover_extra_i_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_remaining_after_999_not_locked"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["inside_family_999_090_076_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["cycle"], 260)
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_previous_stem"][
                "i_leftover_extra_090_076_share_one_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_stem"]["N_distinct_previous_stems"],
            34,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["G"], "999")
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["K"], 15)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["cycle"], 226)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_forward_070"][
                "i_leftover_extra_090_076_exactly_8_share_forward_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["K"], 8)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["cycle"], 225)
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_forward_stem"][
                "i_leftover_extra_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_forward_stem"]["N_distinct_next_stems"],
            30,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["K"], 8)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]["cycle"],
            259,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]["cycle"],
            258,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]["cycle"],
            257,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]["cycle"],
            256,
        )
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_I"], 69)
        self.assertEqual(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"],
            13,
        )
        self.assertEqual(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"],
            56,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
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


class TestMamariILeftoverExtra090076Previous999ImageSnapshot(unittest.TestCase):
    """Cycle 261 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
