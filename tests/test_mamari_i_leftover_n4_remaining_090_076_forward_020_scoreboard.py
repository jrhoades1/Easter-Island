"""I's cycle-288 leftover n=4 remaining 2-gram forward-020 cluster lock.

Cycle 289 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–287), or the already-closed
leftover remaining family. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Cycle 288 lost share-one-forward-stem: N_inside=13,
N_with_next=13, N_no_next=0, N_distinct=6, most frequent next
stem G=020 K=4 (report; that claim is share-one, not
exactly-K), unique-max true. Unique-max G/K is inventory for
this peel. Measuring which leftover n=4 remaining I 090 076
sites have next 020 is not a leftover n=4 retune. Do not lock
leftover n=4 remaining remaining-after-020 next stems. Do not
lock I-only of 3-gram 090 076 020 this cycle (later cycle if
this holds, analog of cycle 227 leftover extra remaining-
after-070 unique-max / cycle 236 leftover extra 3-gram
090 076 700 I-only after the exactly-K peel). Off-I T sites
are not this cycle. 076 071 and 076 070 do not count as this
2-gram. Leftover extra sites do not count as leftover n=4
remaining.

Hypothesis K=4: leftover n=4 remaining I 090 076 sites with a
next token include exactly 4 that share next stem 020
(forward 3-gram 090 076 020). Nested-check leftover n=4
remaining N_inside==13, N_with_next==13, N_no_next==0,
N_distinct==6, unique-max true, G=020 K=4 (do not retune
cycle 288). Nested-check leftover extra remaining-after-009
extra I 008 090 076 at Ia12[82] / 090-start Ia12[83] is one
leftover n=4 remaining 090 076 020 site (do not retune
286/287). Measured: K=4 at Ia2[119], Ia4[86], Ia5[143],
Ia12[83]; those matching leftover n=4 remaining sites equal
the cycle-288 G=020 sites / leftover 090 076 020 010 covered
set. N_remaining_after_020=9 (N_inside-K). Nested Ia12[83] ∈
those sites. Claim that can lose:
i_leftover_n4_remaining_090_076_exactly_4_share_forward_020.
True only if K==4. The claim is true. Same claim-shape as
cycle 226 (leftover extra exactly 8 share forward 070). This
can lose if leftover n=4 remaining does not contain exactly 4
I 090 076 020 sites or if the measured sites differ from
cycle 288's 020×4 inventory. Nested cycle 288 N_distinct=6
G=020 K=4 unique-max true, cycle 226 leftover extra exactly 8
share 070, cycle 224 13/56, cycle 223 69/3, and cycle 222
leftover remaining K=5 stay. Do not assume the result;
measure. Do not retune.

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
    STANDING_LEFTOVER_020010_COVERED,
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
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_070_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070 as CYCLE226_CLAIM,
    STANDING_K as CYCLE226_K,
    STANDING_MATCHING_SITES as CYCLE226_MATCHING_SITES,
    STANDING_N_LEFTOVER as CYCLE226_N_LEFTOVER,
    TestMamariILeftoverExtra090076Forward070Scoreboard,
    leftover_extra_with_forward_070,
    leftover_extra_without_forward_070,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE225_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_K as CYCLE225_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only_scoreboard import (
    STANDING_EXTRA_I_090_076_SITES as CYCLE287_EXTRA_I_090_076_SITES,
    STANDING_EXTRA_I_BY_W as CYCLE287_EXTRA_I_BY_W,
    STANDING_EXTRA_I_SITES as CYCLE287_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_EXTRA_I_PREV4_ALL_I_ONLY as CYCLE287_CLAIM,
    STANDING_N_EXTRA_I as CYCLE287_N_EXTRA_I,
    STANDING_N_I_ONLY as CYCLE287_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE287_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter009ExtraIPrev4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_SITES as CYCLE288_G_SITES,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE288_N_INSIDE,
    STANDING_N_NO_NEXT as CYCLE288_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE288_N_WITH_NEXT,
    STANDING_NO_NEXT_SITES as CYCLE288_NO_NEXT_SITES,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
    leftover_n4_remaining_forward_3grams,
    leftover_n4_remaining_next_4grams,
    leftover_n4_remaining_next_stems,
    leftover_n4_remaining_sites_with_next,
    leftover_n4_remaining_sites_without_next,
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

HYPOTHESIS_K = 4
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "020")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_NEXT = 13
STANDING_N_NO_NEXT = 0
STANDING_NO_NEXT_SITES = ()
STANDING_N_DISTINCT_NEXT_STEMS = 6
STANDING_K = 4
STANDING_G = "020"
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_N_REMAINING_AFTER_020 = 9
STANDING_MATCHING_SITES = STANDING_LEFTOVER_020010_COVERED
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "020", "010"),
    ("090", "076", "020", "010"),
    ("090", "076", "020", "010"),
    ("090", "076", "020", "010"),
)
STANDING_IA12_82 = (SIDE_IA, "Ia12", 82)
STANDING_IA12_83 = (SIDE_IA, "Ia12", 83)
STANDING_REMAINING_AFTER_020_SITES = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia4", 117),
    (SIDE_IA, "Ia5", 28),
    (SIDE_IA, "Ia6", 78),
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
    (SIDE_IA, "Ia13", 17),
    (SIDE_IA, "Ia14", 54),
)
STANDING_MATCHING_EQUALS_CYCLE288_G_SITES = True
STANDING_IA12_83_IN_MATCHING = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"
STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020 = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_forward_020"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE226 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_3GRAM_090_076_020_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True


def leftover_n4_remaining_with_forward_020(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose next token is 020."""
    return leftover_extra_with_forward_070(sites, next_stems, stem)


def leftover_n4_remaining_without_forward_020(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose next token is not 020, or none."""
    return leftover_extra_without_forward_070(sites, next_stems, stem)


def matching_equals_cycle288_g_sites(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle288_g_sites: tuple[tuple[str, str, int], ...] = CYCLE288_G_SITES,
) -> bool:
    """True iff leftover n=4 remaining 090 076 020 sites equal cycle-288 G sites."""
    return matching_sites == cycle288_g_sites


def ia12_83_in_matching(
    matching_sites: tuple[tuple[str, str, int], ...],
    site: tuple[str, str, int] = STANDING_IA12_83,
) -> bool:
    """True iff leftover n=4 remaining Ia12[83] is one 090 076 020 site."""
    return site in matching_sites


def extra_i_008_090_076_090_start_is_matching_020(
    extra_i_090_start: tuple[str, str, int] = STANDING_IA12_83,
    matching_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
) -> bool:
    """True iff leftover extra remaining-after-009 extra I 008 090-start is 020."""
    return extra_i_090_start in matching_sites


def matching_leftover_n4_remaining_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover n=4 remaining next-4-gram rows."""
    rows = []
    for (side, line, index), next_gram in zip(
        leftover_sites,
        next_4grams,
        strict=True,
    ):
        rows.append(
            {
                "tablet": "I",
                "side": side,
                "line": line,
                "index": index,
                "next_4gram": list(next_gram),
                "forward_3gram": list(next_gram[:3]),
            }
        )
    return rows


def i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(
    k: int,
    expected: int = HYPOTHESIS_K,
) -> bool:
    """True iff K equals the hypothesized 4."""
    return k == expected


class TestILeftoverN4Remaining090076Forward020Helpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining I 090 076 forward 020. No CV, no LLM."""

    def test_forward_020_requires_stem_after_2gram(self):
        """Next stem 020 is 090 076 020; end-of-line is no-next."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "020"))
        self.assertEqual(GRAM3_FORWARD[:STANDING_N2], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_020 = ["090", "076", "020", "010"]
        self.assertEqual(site_next_stem(has_020, 0, GRAM2), "020")
        self.assertEqual(site_forward_3gram(has_020, 0, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_020, 0, GRAM2),
            ("090", "076", "020", "010"),
        )
        other_next = ["600", "090", "076", "011", "027"]
        self.assertEqual(site_next_stem(other_next, 1, GRAM2), "011")
        self.assertNotEqual(site_forward_3gram(other_next, 1, GRAM2), GRAM3_FORWARD)
        family_end_then_next = ["999", "021", "090", "076", "607", "755"]
        self.assertEqual(site_next_stem(family_end_then_next, 2, GRAM2), "607")
        self.assertNotEqual(
            site_forward_3gram(family_end_then_next, 2, GRAM2),
            GRAM3_FORWARD,
        )
        end_of_line = ["999", "021", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        self.assertIsNone(site_forward_3gram(end_of_line, 2, GRAM2))
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_4_can_fail(self):
        """Boolean is True only when K=4."""
        provider = MockProvider()
        self.assertTrue(i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(4))
        self.assertFalse(i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(0))
        self.assertFalse(i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(3))
        self.assertFalse(i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(5))
        self.assertFalse(i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(8))
        self.assertFalse(i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(13))
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 2),)
        planted_stems = ("020",) * 5
        self.assertEqual(
            leftover_n4_remaining_with_forward_020(planted, planted_stems),
            planted,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(len(planted))
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_exactly_4_share_forward_020",
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020)
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020,
            HYPOTHESIS_K == STANDING_K,
        )
        self.assertEqual(STANDING_K + STANDING_N_REMAINING_AFTER_020, STANDING_N_INSIDE)
        self.assertEqual(4 + 9, 13)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle288_set_and_ia12_83_can_diverge(self):
        """Cycle-288 G-site equality and nested Ia12[83] membership can fail."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle288_g_sites(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE288_G_SITES)
        self.assertTrue(ia12_83_in_matching(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_IA12_83_IN_MATCHING)
        self.assertTrue(
            extra_i_008_090_076_090_start_is_matching_020(STANDING_IA12_83)
        )
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle288_g_sites(planted))
        self.assertFalse(ia12_83_in_matching(planted))
        self.assertFalse(
            i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(len(planted))
        )
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_3GRAM_090_076_020_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076Forward020Scoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 remaining 090 076 forward-020 lock. Mock only."""

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
        self.with_next = leftover_n4_remaining_sites_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next = leftover_n4_remaining_sites_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.matching = leftover_n4_remaining_with_forward_020(
            self.inside_sites,
            self.next_stems,
        )
        self.without = leftover_n4_remaining_without_forward_020(
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
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.k = len(self.matching)
        self.n_remaining_after_020 = len(self.without)
        self.equals_cycle288 = matching_equals_cycle288_g_sites(self.matching)
        self.ia12_83_in = ia12_83_in_matching(self.matching)
        self.claim_holds = i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(
            self.k,
        )

    def test_tokens_and_sites_are_cycle_288_inside_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/13/0 stay the cycle-288/224 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "020"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_i, 69)
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
        self.assertEqual(
            tuple(tuple(row) for row in prior_288["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_288["G_sites"]),
            CYCLE288_G_SITES,
        )
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
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertEqual(prior_222["K"], CYCLE222_K)
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(tuple(prior_222["G"]), CYCLE222_G)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertTrue(CYCLE222_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_3GRAM_090_076_020_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_4_of_13_and_hypothesis_k_4_holds(self):
        """N_inside=13, N_with_next=13, N_no_next=0, K=4. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, CYCLE288_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 13)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, CYCLE288_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 0)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, CYCLE288_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ())
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_inside)
        self.assertEqual(13 + 0, 13)
        if self.n_inside != 13 or self.n_with_next != 13 or self.n_no_next != 0:
            self.fail("nested cycle 288 leftover n=4 remaining 13/13/0 drifted")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, HYPOTHESIS_K)
        self.assertEqual(STANDING_K, 4)
        self.assertEqual(STANDING_K, CYCLE288_K)
        self.assertEqual(STANDING_G, "020")
        self.assertEqual(STANDING_G, CYCLE288_G)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 6)
        self.assertEqual(self.n_remaining_after_020, STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(self.k + self.n_remaining_after_020, self.n_inside)
        self.assertEqual(4 + 9, 13)
        self.assertTrue(i_leftover_n4_remaining_090_076_exactly_4_share_forward_020(self.k))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020,
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_exactly_4_share_forward_020",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE288_G_SITES)
        self.assertEqual(self.matching, STANDING_LEFTOVER_020010_COVERED)
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_020_SITES)
        self.assertTrue(self.equals_cycle288)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE288_G_SITES)
        self.assertTrue(matching_equals_cycle288_g_sites(self.matching))
        self.assertTrue(self.ia12_83_in)
        self.assertTrue(STANDING_IA12_83_IN_MATCHING)
        self.assertIn(STANDING_IA12_83, self.matching)
        if len(self.matching) != 4 or not self.equals_cycle288:
            self.fail("leftover n=4 remaining 090 076 020 set drifted from cycle-288 G sites")
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_3GRAM_090_076_020_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_n4_remaining_sites_equal_cycle_288(self):
        """Four leftover n=4 remaining sites are 090 076 020 and equal cycle-288 G."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia2", 119), ("090", "076", "020", "010")),
            ((SIDE_IA, "Ia4", 86), ("090", "076", "020", "010")),
            ((SIDE_IA, "Ia5", 143), ("090", "076", "020", "010")),
            ((SIDE_IA, "Ia12", 83), ("090", "076", "020", "010")),
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
            self.assertEqual(stems[index + STANDING_N2], "020")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "020")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, CYCLE288_G_SITES)
            self.assertIn(site, STANDING_LEFTOVER_020010_COVERED)
        self.assertEqual(self.matching, CYCLE288_G_SITES)
        self.assertTrue(matching_equals_cycle288_g_sites(self.matching))
        self.assertIn(STANDING_IA12_83, self.matching)
        self.assertTrue(ia12_83_in_matching(self.matching))
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertNotEqual(nxt, "020")
            self.assertNotIn(site, CYCLE288_G_SITES)
            self.assertIn(site, STANDING_INSIDE_SITES)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_extra_i_008_090_076_ia12_83_is_one_matching_site(self):
        """Leftover extra remaining-after-009 extra I 008 at Ia12[82] / 090-start Ia12[83] is 020."""
        self.assertEqual(CYCLE287_N_EXTRA_I, 2)
        self.assertEqual(
            CYCLE287_EXTRA_I_SITES,
            ((SIDE_IA, "Ia8", 113), (SIDE_IA, "Ia12", 82)),
        )
        self.assertEqual(
            CYCLE287_EXTRA_I_090_076_SITES,
            ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia12", 83)),
        )
        self.assertEqual(CYCLE287_EXTRA_I_BY_W["008"], (STANDING_IA12_82,))
        self.assertEqual(STANDING_IA12_82, (SIDE_IA, "Ia12", 82))
        self.assertEqual(STANDING_IA12_83, (SIDE_IA, "Ia12", 83))
        self.assertEqual(CYCLE287_EXTRA_I_090_076_SITES[1], STANDING_IA12_83)
        self.assertIn(STANDING_IA12_83, STANDING_INSIDE_SITES)
        self.assertIn(STANDING_IA12_83, STANDING_MATCHING_SITES)
        self.assertIn(STANDING_IA12_83, STANDING_LEFTOVER_020010_COVERED)
        self.assertTrue(extra_i_008_090_076_090_start_is_matching_020())
        self.assertTrue(ia12_83_in_matching(self.matching))
        stems_008 = line_stems_for_site(self.i_sides, STANDING_IA12_82)
        self.assertEqual(tuple(stems_008[82:85]), ("008", "090", "076"))
        stems_090 = line_stems_for_site(self.i_sides, STANDING_IA12_83)
        self.assertEqual(tuple(stems_090[83:86]), ("090", "076", "020"))
        self.assertEqual(site_next_stem(stems_090, 83, GRAM2), "020")
        prior_287 = self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]
        self.assertEqual(prior_287["cycle"], 287)
        self.assertEqual(prior_287["N_extra_i"], 2)
        self.assertEqual(prior_287["N_i_only"], 2)
        self.assertEqual(prior_287["N_not_i_only"], 0)
        self.assertTrue(prior_287["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only"])
        extra_009_090 = tuple(tuple(row) for row in prior_287["extra_i_090_076_sites"])
        self.assertEqual(extra_009_090, CYCLE287_EXTRA_I_090_076_SITES)
        self.assertIn(STANDING_IA12_83, extra_009_090)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_288_226_224_223_222_still_compute(self):
        """Cycle 288 13/13/0 N_distinct=6 G=020 K=4, 226 K=8, 224 13/56, 223 69/3, 222 K=5 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
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
            or prior_288.n_no_next != 0
            or prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or not prior_288.unique_max
        ):
            self.fail("nested cycle 288 leftover n=4 remaining 13/13/0 N_distinct=6 G=020 K=4 unique-max drifted")
        prior_226 = TestMamariILeftoverExtra090076Forward070Scoreboard()
        prior_226.setUp()
        prior_226.test_counts_8_of_56_and_hypothesis_k_8_holds()
        prior_226.test_survey_matches_computed_lock()
        self.assertEqual(prior_226.k, CYCLE226_K)
        self.assertEqual(prior_226.k, 8)
        self.assertEqual(prior_226.n_leftover, CYCLE226_N_LEFTOVER)
        self.assertEqual(prior_226.n_leftover, 56)
        self.assertTrue(prior_226.claim_holds)
        self.assertTrue(CYCLE226_CLAIM)
        self.assertEqual(prior_226.matching, CYCLE226_MATCHING_SITES)
        if prior_226.k != 8 or not prior_226.claim_holds:
            self.fail("nested cycle 226 leftover extra exactly 8 share 070 drifted")
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
        prior_287 = TestMamariILeftoverExtra090076RemainingAfter009ExtraIPrev4IOnlyScoreboard()
        prior_287.setUp()
        prior_287.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE287_N_I_ONLY, 2)
        self.assertEqual(CYCLE287_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE287_CLAIM)
        if CYCLE287_N_I_ONLY != 2 or CYCLE287_N_NOT_I_ONLY != 0:
            self.fail("nested cycle 287 extra-I previous 4-grams 2/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(CYCLE225_G, "070")
        self.assertEqual(CYCLE225_K, 8)
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-289 leftover n=4 remaining forward-020 lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_forward_020"]
        self.assertEqual(lock["cycle"], 289)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 4)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
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
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 13)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(
            lock["N_distinct_next_stems"],
            STANDING_N_DISTINCT_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_next_stems"], 6)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "020")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 4)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertEqual(
            lock["g_uniquely_most_frequent"],
            STANDING_G_UNIQUELY_MOST_FREQUENT,
        )
        self.assertEqual(lock["N_remaining_after_020"], STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(lock["N_remaining_after_020"], 9)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_sites"]),
            CYCLE288_G_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle288_g_sites"])
        self.assertEqual(
            lock["matching_equals_cycle288_g_sites"],
            STANDING_MATCHING_EQUALS_CYCLE288_G_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_local_4grams"],
            matching_leftover_n4_remaining_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_020_sites"]),
            STANDING_REMAINING_AFTER_020_SITES,
        )
        self.assertTrue(lock["ia12_83_in_matching"])
        self.assertEqual(lock["ia12_83_in_matching"], STANDING_IA12_83_IN_MATCHING)
        self.assertEqual(tuple(lock["ia12_83"]), STANDING_IA12_83)
        self.assertEqual(tuple(lock["ia12_82"]), STANDING_IA12_82)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"])
        self.assertEqual(
            lock["i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"],
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle226"])
        self.assertTrue(lock["same_claim_shape_as_cycle226"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["3gram_090_076_020_i_only_is_not_this_cycle"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_020_next_stems_not_locked"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_070_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"][
                "i_leftover_n4_remaining_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["N_inside"], 13)
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["N_with_next"], 13)
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["N_no_next"], 0)
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["N_distinct_next_stems"],
            6,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["G"], "020")
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["K"], 4)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["g_uniquely_most_frequent"]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["cycle"], 226)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_forward_070"][
                "i_leftover_extra_090_076_exactly_8_share_forward_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["K"], 8)
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
        self.assertFalse(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"][
                "i_090_076_all_inside_leftover_n4_remaining_family"
            ]
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_leftover_n4_remaining_next_2gram"]["cycle"], 222)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_next_2gram"][
                "i_leftover_n4_remaining_exactly_5_contain_090_076"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_next_2gram"]["K"], 5)
        self.assertEqual(tuple(self.survey["i_leftover_n4_remaining_next_2gram"]["G"]), GRAM2)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]["cycle"],
            287,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]["N_i_only"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]["N_not_i_only"],
            0,
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
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076Forward020ImageSnapshot(unittest.TestCase):
    """Cycle 289 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
