"""I's cycle-225 leftover extra 2-gram forward-070 cluster lock.

Cycle 226 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Cycle 225 lost share-one-forward-stem: N_leftover=56,
N_with_next=55, N_no_next=1 at Ia4[166] only, N_distinct=30,
most frequent next stem G=070 K=8 (report; that claim is
share-one, not exactly-K). Ia2[174] has next token 000, not
no-next. This cycle locks the largest leftover extra
continuation cluster instead. Do not lock leftover extra
remaining next stems. Off-I T sites are not this cycle.
I-only of leftover extra 4-grams is leftover-of-leftover
for a later cycle. 076 071 and 076 070 do not count as this
2-gram. Inside-family sites do not count as leftover extra.

Hypothesis K=8: leftover extra I 090 076 sites with a next
token include exactly 8 that share next stem 070 (forward
3-gram 090 076 070). Nested-check leftover extra set
N_leftover==56, N_with_next==55, N_no_next==1 (do not retune
cycle 225). Nested-check cycle 207 N_I==8 for 090 076 070
(do not retune). Measured: K=8 at Ia2[10], Ia3[4], Ia4[112],
Ia7[68], Ia7[129], Ia8[120], Ia14[97], Ia14[140]; those
matching leftover extra sites equal the cycle-207 I
090 076 070 set. Claim that can lose:
i_leftover_extra_090_076_exactly_8_share_forward_070. True
only if K==8. The claim is true. Same claim-shape as cycle
173 (leftover 076 071 exactly 5 share forward 076 071 076).
This can lose if leftover extra does not contain all 8 I
090 076 070 sites (some might have been inside leftover n=4
remaining) or if K≠8. Nested cycle 225 N_distinct=30 G=070
K=8, cycle 223 69/3, cycle 222 leftover remaining K=5,
cycle 207 8/1, and cycle 171 43/0 stay. Do not assume the
result; measure. Do not retune.

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
    leftover_local_4grams,
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
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    STANDING_I_LEFTOVER_076_071_EXACTLY_5_FORWARD_076_071_076 as CYCLE173_CLAIM,
    STANDING_N_LEFTOVER as CYCLE173_N_LEFTOVER,
    STANDING_N_WITH_FORWARD_076_071_076 as CYCLE173_N_WITH,
    site_forward_3gram,
    site_next_4gram,
    TestMamariILeftover076071Forward076Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE225_G,
    STANDING_G_SITES as CYCLE225_G_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_IA2_174,
    STANDING_IA2_174_NEXT_STEM,
    STANDING_K as CYCLE225_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE225_N_LEFTOVER,
    STANDING_N_NO_NEXT as CYCLE225_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE225_N_WITH_NEXT,
    STANDING_NO_NEXT_SITES,
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
    leftover_sites_with_next,
    leftover_sites_without_next,
    site_next_stem,
    TestMamariILeftoverExtra090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
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

HYPOTHESIS_K = 8
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "070")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_WITH_NEXT = 55
STANDING_N_NO_NEXT = 1
STANDING_K = 8
STANDING_G = "070"
STANDING_N_WITHOUT = 48
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia2", 10),
    (SIDE_IA, "Ia3", 4),
    (SIDE_IA, "Ia4", 112),
    (SIDE_IA, "Ia7", 68),
    (SIDE_IA, "Ia7", 129),
    (SIDE_IA, "Ia8", 120),
    (SIDE_IA, "Ia14", 97),
    (SIDE_IA, "Ia14", 140),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "070", "499"),
    ("090", "076", "070", "200"),
    ("090", "076", "070", "600"),
    ("090", "076", "070", "027"),
    ("090", "076", "070", "532"),
    ("090", "076", "070", "071"),
    ("090", "076", "070", "073"),
    ("090", "076", "070", "000"),
)
STANDING_MATCHING_EQUALS_CYCLE207_I_SITES = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_exactly_8_share_forward_070"
STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070 = True
STANDING_RESULT = "i_leftover_extra_090_076_forward_070"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE173 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE173 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_NEXT_STEMS_NOT_LOCKED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN = True


def leftover_extra_with_forward_070(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites whose next token is 070."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem
    )


def leftover_extra_without_forward_070(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites whose next token is not 070, or none."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt != stem
    )


def matching_equals_cycle207_i_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle207_i_sites: tuple[tuple[str, str, int], ...] = CYCLE207_I_SITES,
) -> bool:
    """True iff leftover extra 090 076 070 sites equal the cycle-207 I set."""
    return matching_sites == cycle207_i_sites


def matching_leftover_extra_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra next-4-gram rows."""
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


def i_leftover_extra_090_076_exactly_8_share_forward_070(
    k: int,
    expected: int = HYPOTHESIS_K,
) -> bool:
    """True iff K equals the hypothesized 8."""
    return k == expected


class TestILeftoverExtra090076Forward070Helpers(unittest.TestCase):
    """Helpers on leftover extra I 090 076 forward 070. No CV, no LLM."""

    def test_forward_070_requires_stem_after_2gram(self):
        """Next stem 070 is 090 076 070; end-of-line is no-next."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "070"))
        self.assertEqual(GRAM3_FORWARD, CYCLE207_GRAM3)
        self.assertEqual(GRAM3_FORWARD[:STANDING_N2], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_070 = ["999", "090", "076", "070", "499"]
        self.assertEqual(site_next_stem(has_070, 1, GRAM2), "070")
        self.assertEqual(site_forward_3gram(has_070, 1, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_070, 1, GRAM2),
            ("090", "076", "070", "499"),
        )
        other_next = ["602", "999", "090", "076", "012", "076"]
        self.assertEqual(site_next_stem(other_next, 2, GRAM2), "012")
        self.assertNotEqual(site_forward_3gram(other_next, 2, GRAM2), GRAM3_FORWARD)
        one_token_then_eol = ["009", "009", "090", "076", "000"]
        self.assertEqual(site_next_stem(one_token_then_eol, 2, GRAM2), "000")
        self.assertNotEqual(site_next_stem(one_token_then_eol, 2, GRAM2), "070")
        self.assertIsNone(site_next_4gram(one_token_then_eol, 2, GRAM2))
        end_of_line = ["087", "078", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        self.assertIsNone(site_forward_3gram(end_of_line, 2, GRAM2))
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_8_can_fail(self):
        """Boolean is True only when K=8."""
        provider = MockProvider()
        self.assertTrue(i_leftover_extra_090_076_exactly_8_share_forward_070(8))
        self.assertFalse(i_leftover_extra_090_076_exactly_8_share_forward_070(0))
        self.assertFalse(i_leftover_extra_090_076_exactly_8_share_forward_070(5))
        self.assertFalse(i_leftover_extra_090_076_exactly_8_share_forward_070(7))
        self.assertFalse(i_leftover_extra_090_076_exactly_8_share_forward_070(9))
        self.assertFalse(i_leftover_extra_090_076_exactly_8_share_forward_070(55))
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 2),)
        planted_stems = ("070",) * 9
        self.assertEqual(
            leftover_extra_with_forward_070(planted, planted_stems),
            planted,
        )
        self.assertFalse(
            i_leftover_extra_090_076_exactly_8_share_forward_070(len(planted))
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_extra_090_076_exactly_8_share_forward_070")
        self.assertTrue(STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070)
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070,
            HYPOTHESIS_K == STANDING_K,
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT, STANDING_N_LEFTOVER)
        self.assertEqual(8 + 48, 56)
        self.assertEqual(provider.get_call_history(), [])

    def test_inside_family_and_cycle207_set_can_diverge(self):
        """Inside leftover n=4 remaining is not leftover extra; cycle-207 equality can fail."""
        provider = MockProvider()
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(matching_equals_cycle207_i_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE207_I_SITES)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle207_i_set(planted))
        self.assertFalse(
            i_leftover_extra_090_076_exactly_8_share_forward_070(len(planted))
        )
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE173)
        self.assertFalse(STANDING_SAME_AS_CYCLE173)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076Forward070Scoreboard(unittest.TestCase):
    """Cited-fixture leftover extra 090 076 forward-070 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.next_stems = leftover_extra_next_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.forwards = leftover_extra_forward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.with_next = leftover_sites_with_next(self.leftover_sites, self.next_stems)
        self.no_next = leftover_sites_without_next(self.leftover_sites, self.next_stems)
        self.matching = leftover_extra_with_forward_070(
            self.leftover_sites,
            self.next_stems,
        )
        self.without = leftover_extra_without_forward_070(
            self.leftover_sites,
            self.next_stems,
        )
        self.matching_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = CYCLE224_N_INSIDE
        self.n_leftover = len(self.leftover_sites)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.k = len(self.matching)
        self.n_without = len(self.without)
        self.equals_cycle207 = matching_equals_cycle207_i_set(self.matching)
        self.claim_holds = i_leftover_extra_090_076_exactly_8_share_forward_070(
            self.k,
        )

    def test_tokens_and_sites_are_cycle_225_leftover_extra_not_retuned(self):
        """2-gram and leftover extra 56/55/1 stay the cycle-225/224/223/222 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "070"))
        self.assertEqual(GRAM3_FORWARD, CYCLE207_GRAM3)
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
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE225_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_225 = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(prior_225["cycle"], 225)
        self.assertEqual(prior_225["N_leftover"], 56)
        self.assertEqual(prior_225["N_with_next"], 55)
        self.assertEqual(prior_225["N_no_next"], 1)
        self.assertEqual(prior_225["N_distinct_next_stems"], 30)
        self.assertEqual(prior_225["G"], "070")
        self.assertEqual(prior_225["K"], 8)
        self.assertFalse(prior_225["i_leftover_extra_090_076_share_one_forward_stem"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_225["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
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
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        if prior_207["N_I"] != 8 or prior_207["N_off_I"] != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_8_of_56_and_hypothesis_k_8_holds(self):
        """N_leftover=56, N_with_next=55, N_no_next=1, K=8. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, CYCLE225_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 55)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, CYCLE225_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 1)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ((SIDE_IA, "Ia4", 166),))
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_leftover)
        self.assertEqual(55 + 1, 56)
        if self.n_leftover != 56 or self.n_with_next != 55 or self.n_no_next != 1:
            self.fail("nested cycle 225 leftover extra 56/55/1 drifted")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, HYPOTHESIS_K)
        self.assertEqual(STANDING_K, 8)
        self.assertEqual(STANDING_K, CYCLE225_K)
        self.assertEqual(STANDING_G, "070")
        self.assertEqual(STANDING_G, CYCLE225_G)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 48)
        self.assertEqual(self.k + self.n_without, self.n_leftover)
        self.assertEqual(8 + 48, 56)
        self.assertTrue(i_leftover_extra_090_076_exactly_8_share_forward_070(self.k))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070,
        )
        self.assertTrue(STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070)
        self.assertEqual(STANDING_CLAIM, "i_leftover_extra_090_076_exactly_8_share_forward_070")
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE207_I_SITES)
        self.assertEqual(self.matching, CYCLE225_G_SITES)
        self.assertTrue(self.equals_cycle207)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE207_I_SITES)
        self.assertTrue(matching_equals_cycle207_i_set(self.matching))
        self.assertEqual(len(CYCLE207_I_SITES), CYCLE207_N_I)
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        if len(self.matching) != 8 or not self.equals_cycle207:
            self.fail("leftover extra 090 076 070 set drifted from cycle-207 I set")
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE173)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE173)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_sites_equal_cycle_207(self):
        """Eight leftover extra sites are 090 076 070 and equal cycle-207 I."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia2", 10), ("090", "076", "070", "499")),
            ((SIDE_IA, "Ia3", 4), ("090", "076", "070", "200")),
            ((SIDE_IA, "Ia4", 112), ("090", "076", "070", "600")),
            ((SIDE_IA, "Ia7", 68), ("090", "076", "070", "027")),
            ((SIDE_IA, "Ia7", 129), ("090", "076", "070", "532")),
            ((SIDE_IA, "Ia8", 120), ("090", "076", "070", "071")),
            ((SIDE_IA, "Ia14", 97), ("090", "076", "070", "073")),
            ((SIDE_IA, "Ia14", 140), ("090", "076", "070", "000")),
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
            self.assertEqual(stems[index + STANDING_N2], "070")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "070")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertIn(site, CYCLE207_I_SITES)
        self.assertEqual(self.matching, CYCLE207_I_SITES)
        self.assertTrue(matching_equals_cycle207_i_set(self.matching))
        self.assertEqual(STANDING_LEFTOVER_SITES[13], STANDING_IA2_174)
        self.assertEqual(STANDING_LEFTOVER_SITES[24], STANDING_NO_NEXT_SITES[0])
        self.assertEqual(self.next_stems[13], STANDING_IA2_174_NEXT_STEM)
        self.assertEqual(self.next_stems[13], "000")
        self.assertIsNone(self.next_stems[24])
        self.assertNotIn(STANDING_IA2_174, self.matching)
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.matching)
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertNotEqual(nxt, "070")
            self.assertNotIn(site, CYCLE207_I_SITES)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_225_223_222_207_173_and_171_still_compute(self):
        """Cycle 225 56/55/1 / 30 / G=070 K=8, 223 69/3, 222 K=5, 207 8/1, 173 5, 171 43/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_225 = TestMamariILeftoverExtra090076ForwardStemScoreboard()
        prior_225.setUp()
        prior_225.test_counts_30_distinct_next_stems_and_claim_loses()
        prior_225.test_survey_matches_computed_lock()
        self.assertEqual(prior_225.n_leftover, 56)
        self.assertEqual(prior_225.n_with_next, 55)
        self.assertEqual(prior_225.n_no_next, 1)
        self.assertEqual(prior_225.n_distinct, 30)
        self.assertEqual(prior_225.g, "070")
        self.assertEqual(prior_225.k, 8)
        self.assertFalse(prior_225.claim_holds)
        self.assertFalse(CYCLE225_SHARE_ONE)
        if (
            prior_225.n_leftover != 56
            or prior_225.n_with_next != 55
            or prior_225.n_no_next != 1
            or prior_225.n_distinct != 30
            or prior_225.k != 8
        ):
            self.fail("nested cycle 225 leftover extra 56/55/1 N_distinct=30 G=070 K=8 drifted")
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
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
        prior_173 = TestMamariILeftover076071Forward076Scoreboard()
        prior_173.setUp()
        prior_173.test_counts_5_of_34_and_hypothesis_n_5_holds()
        prior_173.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE173_N_LEFTOVER, 34)
        self.assertEqual(CYCLE173_N_WITH, 5)
        self.assertTrue(CYCLE173_CLAIM)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-226 leftover extra forward-070 lock."""
        lock = self.survey["i_leftover_extra_090_076_forward_070"]
        self.assertEqual(lock["cycle"], 226)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 8)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 55)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(lock["ia2_174_next_stem"], STANDING_IA2_174_NEXT_STEM)
        self.assertEqual(lock["ia2_174_next_stem"], "000")
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "070")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 8)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 48)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_sites"]),
            CYCLE207_I_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle207_i_sites"])
        self.assertEqual(
            lock["matching_equals_cycle207_i_sites"],
            STANDING_MATCHING_EQUALS_CYCLE207_I_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_local_4grams"],
            matching_leftover_extra_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle207_i_sites"]),
            CYCLE207_I_SITES,
        )
        self.assertEqual(lock["cycle207_N_I"], CYCLE207_N_I)
        self.assertEqual(lock["cycle207_N_I"], 8)
        self.assertEqual(lock["cycle207_N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(lock["cycle207_N_off_I"], 1)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_extra_090_076_exactly_8_share_forward_070"])
        self.assertEqual(
            lock["i_leftover_extra_090_076_exactly_8_share_forward_070"],
            STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle173"])
        self.assertTrue(lock["same_claim_shape_as_cycle173"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_remaining_next_stems_not_locked"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle224_no_next_4gram_is_not_no_next_token"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_076_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["cycle"], 225)
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_forward_stem"][
                "i_leftover_extra_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["N_with_next"], 55)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["N_no_next"], 1)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_forward_stem"]["N_distinct_next_stems"],
            30,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["K"], 8)
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
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["cycle"], 173)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_076"][
                "i_leftover_076_071_exactly_5_forward_076_071_076"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["N_leftover"], 34)
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


class TestMamariILeftoverExtra090076Forward070ImageSnapshot(unittest.TestCase):
    """Cycle 226 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
