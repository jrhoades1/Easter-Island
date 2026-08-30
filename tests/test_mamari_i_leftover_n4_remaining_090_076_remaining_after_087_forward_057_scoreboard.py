"""I's cycle-294 leftover n=4 remaining remaining-after-087 forward-057 lock.

Cycle 295 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–287), leftover n=4 remaining
share-one-forward-stem (cycle 288 lost), leftover n=4
remaining exactly 4 share next 020 (cycle 289), leftover n=4
remaining remaining-after-020 unique next stem (cycle 292),
leftover n=4 remaining remaining-after-020 exactly 3 share
next 087 (cycle 293), or leftover n=4 remaining remaining-
after-087 unique next stem (cycle 294 lost). Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle
100); skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8
or G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Cycle 294 leftover n=4 remaining remaining-after-087 unique
next stem LOST: unique-max false, 2-way tie at K=2 (057/011),
G=057 largest-id, N_remaining_after_087=6, N_with_next=6,
N_no_next=0, N_distinct=4, hapax=2 (607/021). Unique-max G/K
is inventory; this cycle peels 057 as exact-K. Same lose path
as cycle 234 / cycle 270 (tie at K=2). Same claim-shape as
cycle 235 leftover extra remaining-after-001 exactly 2 share
700 and cycle 271 leftover extra remaining-after-600 exactly
2 share previous 090 (exactly K share G after a unique-max
lose with a K=2 tie, largest-id first), leftover n=4 remaining
remaining-after-087 next 057 instead of leftover extra
remaining-after-001/600. Do not peel remaining-after-057 this
cycle. Do not peel 011 this cycle. Do not retune leftover n=4.
Do not retune leftover extra peels. Do not lock leftover n=4
remaining remaining-after-057 next stems this cycle. Do not
lock I-only of leftover n=4 remaining 090 076 057 this cycle
(cycle 258 already owns the 3-gram). Off-I T sites are not
this cycle. 076 071 and 076 070 do not count as this 2-gram.
Leftover extra sites do not count as leftover n=4 remaining.

Hypothesis K=2: leftover n=4 remaining remaining-after-087 I
090 076 sites include exactly 2 that share next stem 057
(forward 3-gram 090 076 057). Nested-check leftover n=4
remaining N_inside==13, K_020==4, N_remaining_after_020==9,
K_087==3, N_remaining_after_087==6 (do not retune
224/288/289/292/293/294). Nested-check cycle 294: unique-max
false, 2-way tie at K=2 (057/011), G=057 largest-id,
N_distinct=4, hapax=2 (do not retune). Count leftover n=4
remaining remaining-after-087 I 090 076 sites whose next
token is 057. Cycle 294 listed Ia8[114]/Ia9[28]; measure, do
not assume if nested-check differs. N_remaining_after_057 =
N_remaining_after_087 − K_057. 057 is still a max-K next
token of remaining-after-087 (tied at K=2; largest-id G=057).
Nested-check each next-057 remaining-after-087 site ⊆ leftover
n=4 remaining remaining-after-087 and has next token 057.
Nested-check (compute, do not retune) cycle 258 extra I of
leftover extra remaining-after-000 090 076 057 at
Ia8[114]/Ia9[28]: whether leftover n=4 remaining remaining-
after-087 057 sites equal those extra I 090-starts. Extra I
mismatch does not make this claim lose; still lock the
overlap. Claim that can lose:
i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057.
True iff K_057==2 among leftover n=4 remaining remaining-
after-087 I 090 076 and 057 is still a max-K next token of
remaining-after-087. The claim is true. This can lose if
nested-check K differs from 2, or if 057 is no longer max-K.
Nested cycle 294 unique-max false 2-way tie G=057 K=2
N_remaining=6, cycle 293 K_087=3, cycle 292 unique-max G=087
K=3, cycle 259 extra-I fwd4 090 076 057 600 2/0, cycle 258
extra I=2 of 057, cycle 224 13/56, and cycle 223 69/3 stay.
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
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE258_EXTRA_I_SITES_EACH,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_I_SITES as CYCLE258_I_SITES_EACH,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE258_N_I_ONLY,
    STANDING_REMAINING11_NEXT_STEMS as CYCLE258_REMAINING11_NEXT_STEMS,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_BY_X as CYCLE259_EXTRA_I_BY_X,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_N_I_ONLY as CYCLE259_N_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_fwd700_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_2_SHARE_700 as CYCLE235_CLAIM,
    STANDING_K as CYCLE235_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_090_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE271_CLAIM,
    STANDING_K_090 as CYCLE271_K_090,
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
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_forward_087_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087 as CYCLE293_CLAIM,
    STANDING_K_087 as CYCLE293_K_087,
    STANDING_MATCHING_SITES as CYCLE293_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_020 as CYCLE293_N_REMAINING_AFTER_020,
    STANDING_N_REMAINING_AFTER_087 as CYCLE293_N_REMAINING_AFTER_087,
    STANDING_REMAINING_AFTER_087_SITES as CYCLE293_REMAINING_AFTER_087_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter020Forward087Scoreboard,
    leftover_n4_remaining_remaining_after_020_with_forward_087,
    leftover_n4_remaining_remaining_after_020_without_forward_087,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_scoreboard import (
    STANDING_G as CYCLE292_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE292_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_UNIQUE_NEXT_STEM as CYCLE292_CLAIM,
    STANDING_K as CYCLE292_K,
    STANDING_MATCHING_SITES as CYCLE292_MATCHING_SITES,
    STANDING_N_DISTINCT as CYCLE292_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_020 as CYCLE292_N_REMAINING,
    STANDING_REMAINING_SITES as CYCLE292_REMAINING_SITES,
    leftover_n4_remaining_remaining_after_020,
    leftover_n4_remaining_remaining_after_020_nested_counts_hold,
    leftover_n4_remaining_remaining_after_020_next_stems,
    leftover_n4_remaining_remaining_after_020_with_next,
    leftover_n4_remaining_remaining_after_020_without_next,
    TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_087_next_stem_scoreboard import (
    LOCKED_FORWARD_STEMS,
    STANDING_G as CYCLE294_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE294_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_UNIQUE_NEXT_STEM as CYCLE294_CLAIM,
    STANDING_K as CYCLE294_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE294_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE294_MATCHING_SITES,
    STANDING_N_DISTINCT as CYCLE294_N_DISTINCT,
    STANDING_N_HAPAX as CYCLE294_N_HAPAX,
    STANDING_N_REMAINING_AFTER_087 as CYCLE294_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE294_N_TIED,
    STANDING_REMAINING_SITES as CYCLE294_REMAINING_SITES,
    STANDING_TIED_STEMS as CYCLE294_TIED_STEMS,
    leftover_n4_remaining_remaining_after_087,
    leftover_n4_remaining_remaining_after_087_nested_counts_hold,
    leftover_n4_remaining_remaining_after_087_next_stems,
    leftover_n4_remaining_remaining_after_087_with_g,
    leftover_n4_remaining_remaining_after_087_with_next,
    leftover_n4_remaining_remaining_after_087_without_g,
    leftover_n4_remaining_remaining_after_087_without_next,
    matching_leftover_n4_remaining_remaining_after_087_local_4gram_rows,
    remaining_after_087_next_stem_counts,
    select_remaining_after_087_g,
    TestMamariILeftoverN4Remaining090076RemainingAfter087NextStemScoreboard,
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

HYPOTHESIS_K = 2
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "057")
GRAM3_NESTED_020_TOKENS = ("090", "076", "020")
GRAM3_NESTED_087 = ("090", "076", "087")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_NEXT_INSIDE = 13
STANDING_N_NO_NEXT_INSIDE = 0
STANDING_K_020 = 4
STANDING_N_REMAINING_AFTER_020 = 9
STANDING_K_087 = 3
STANDING_N_REMAINING_AFTER_087 = 6
STANDING_N_WITH_NEXT = 6
STANDING_N_NO_NEXT = 0
STANDING_NO_NEXT_SITES = ()
STANDING_N_DISTINCT = 4
STANDING_N_HAPAX = 2
STANDING_K = 2
STANDING_K_057 = 2
STANDING_G = "057"
STANDING_N_WITHOUT = 4
STANDING_N_REMAINING_AFTER_057 = 4
STANDING_N_TIED_AT_K = 2
STANDING_TIED_STEMS = ("057", "011")
STANDING_OTHER_TIED_STEMS = ("011",)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "057", "600"),
    ("090", "076", "057", "600"),
)
STANDING_REMAINING_AFTER_057_SITES = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia13", 17),
    (SIDE_IA, "Ia14", 54),
)
CYCLE258_EXTRA_I_057 = CYCLE259_EXTRA_I_BY_X["057"]
STANDING_MATCHING_EQUALS_CYCLE294_G_SITES = True
STANDING_MATCHING_EQUALS_CYCLE258_EXTRA_I = True
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_057_STILL_MAX_K = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057"
)
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057 = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_087_forward_057"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE235 = False
STANDING_SAME_AS_CYCLE271 = False
STANDING_SAME_AS_CYCLE289 = False
STANDING_SAME_AS_CYCLE293 = False
STANDING_SAME_AS_CYCLE294 = False
STANDING_SAME_AS_CYCLE258 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE271 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_057_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_REMAINING_AFTER_057 = True
STANDING_DO_NOT_PEEL_011 = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_057_NOT_LOCKED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_CYCLE167_268_294_NOT_OVERWRITTEN = True
STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE = True
STANDING_OTHER_TIED_STEMS_NOT_LOCKED = True


def leftover_n4_remaining_remaining_after_087_with_forward_057(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-087 sites whose next token is 057."""
    return leftover_n4_remaining_remaining_after_087_with_g(
        sites,
        next_stems,
        stem=stem,
        locked=locked,
    )


def leftover_n4_remaining_remaining_after_087_without_forward_057(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-087 sites whose next token is not 057."""
    return leftover_n4_remaining_remaining_after_087_without_g(
        sites,
        next_stems,
        stem=stem,
        locked=locked,
    )


def remaining_after_087_057_still_max_k(
    remaining_stems: tuple[str, ...],
    stem: str = STANDING_G,
) -> bool:
    """True iff 057 is still a max-K next token of remaining-after-087."""
    counts = remaining_after_087_next_stem_counts(remaining_stems)
    if not counts:
        return False
    return counts.get(stem, 0) == max(counts.values())


def matching_equals_cycle294_g_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle294_g_sites: tuple[tuple[str, str, int], ...] = CYCLE294_MATCHING_SITES,
) -> bool:
    """True iff remaining-after-087 next-057 sites equal the cycle-294 G set."""
    return matching_sites == cycle294_g_sites


def matching_equals_cycle258_extra_i_057(
    matching_sites: tuple[tuple[str, str, int], ...],
    extra_i: tuple[tuple[str, str, int], ...] = CYCLE258_EXTRA_I_057,
) -> bool:
    """True iff remaining-after-087 next-057 sites equal cycle-258 extra I of 057."""
    return matching_sites == extra_i


def next_057_sites_subset_of_remaining_after_087(
    matching_sites: tuple[tuple[str, str, int], ...],
    remaining: tuple[tuple[str, str, int], ...],
    next_stems_by_site: dict[tuple[str, str, int], str | None],
    stem: str = STANDING_G,
) -> bool:
    """True iff each next-057 site ⊆ remaining-after-087 and has next token 057."""
    remaining_set = set(remaining)
    return all(
        site in remaining_set and next_stems_by_site.get(site) == stem
        for site in matching_sites
    )


def i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
    k: int,
    still_max_k: bool,
    g: str | None,
    expected: int = HYPOTHESIS_K,
    expected_g: str = STANDING_G,
) -> bool:
    """True iff K_057 equals 2 and 057 is still a max-K next token."""
    return k == expected and still_max_k and g == expected_g


class TestILeftoverN4Remaining090076RemainingAfter087Forward057Helpers(
    unittest.TestCase
):
    """Helpers on leftover n=4 remaining remaining-after-087 next 057. No CV, no LLM."""

    def test_forward_057_requires_stem_after_2gram_and_not_020_or_087(self):
        """Next stem 057 is 090 076 057; next 020/087 are not remaining-after-087."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "057"))
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(GRAM3_NESTED_020_TOKENS, GRAM3_NESTED_020)
        self.assertEqual(GRAM3_NESTED_087, ("090", "076", "087"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("020", "087"))
        self.assertEqual(GRAM3_FORWARD[:STANDING_N2], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_057 = ["090", "076", "057", "600"]
        self.assertEqual(site_next_stem(has_057, 0, GRAM2), "057")
        self.assertEqual(site_forward_3gram(has_057, 0, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_057, 0, GRAM2),
            ("090", "076", "057", "600"),
        )
        has_020 = ["090", "076", "020", "010"]
        self.assertEqual(site_next_stem(has_020, 0, GRAM2), "020")
        self.assertNotEqual(site_next_stem(has_020, 0, GRAM2), "057")
        has_087 = ["090", "076", "087", "291"]
        self.assertEqual(site_next_stem(has_087, 0, GRAM2), "087")
        self.assertNotEqual(site_next_stem(has_087, 0, GRAM2), "057")
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
            (SIDE_IA, "Ia1", 4),
        )
        planted_stems = ("057", "020", "087", None, "011")
        self.assertEqual(
            leftover_n4_remaining_remaining_after_087_with_forward_057(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_087_without_forward_057(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[4],),
        )
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when K=2 and 057 is still a max-K next token."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                2, True, "057"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                0, True, "057"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                1, True, "057"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                3, True, "057"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                6, True, "057"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                2, False, "057"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                2, True, "011"
            )
        )
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 2),)
        planted_stems = ("057",) * 3
        self.assertEqual(
            leftover_n4_remaining_remaining_after_087_with_forward_057(
                planted,
                planted_stems,
            ),
            planted,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                len(planted), True, "057"
            )
        )
        self.assertFalse(remaining_after_087_057_still_max_k(("011", "011", "057")))
        self.assertTrue(remaining_after_087_057_still_max_k(("057", "057", "011", "011")))
        self.assertFalse(remaining_after_087_057_still_max_k(()))
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057,
            HYPOTHESIS_K == STANDING_K_057 and STANDING_057_STILL_MAX_K,
        )
        self.assertEqual(
            STANDING_K_057 + STANDING_N_REMAINING_AFTER_057,
            STANDING_N_REMAINING_AFTER_087,
        )
        self.assertEqual(2 + 4, 6)
        self.assertEqual(
            STANDING_K_087 + STANDING_N_REMAINING_AFTER_087,
            STANDING_N_REMAINING_AFTER_020,
        )
        self.assertEqual(3 + 6, 9)
        self.assertEqual(STANDING_K_020 + STANDING_N_REMAINING_AFTER_020, STANDING_N_INSIDE)
        self.assertEqual(4 + 9, 13)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle294_set_and_cycle258_extra_can_diverge(self):
        """Cycle-294 G-site equality and cycle-258 extra I of 057 equality can fail."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle294_g_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE294_G_SITES)
        self.assertTrue(matching_equals_cycle258_extra_i_057(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE258_EXTRA_I)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle294_g_set(planted))
        self.assertFalse(matching_equals_cycle258_extra_i_057(planted))
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                len(planted), True, "057"
            )
        )
        self.assertTrue(STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_057)
        self.assertTrue(STANDING_DO_NOT_PEEL_011)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_057_NOT_LOCKED)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_057_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE271)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE271)
        self.assertFalse(STANDING_SAME_AS_CYCLE294)
        self.assertFalse(STANDING_SAME_AS_CYCLE258)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter087Forward057Scoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-087 forward-057 lock. Mock only."""

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
        self.remaining_after_020 = leftover_n4_remaining_remaining_after_020(
            self.inside_sites,
            self.next_stems,
        )
        self.share_087 = leftover_n4_remaining_remaining_after_020_with_forward_087(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining = leftover_n4_remaining_remaining_after_087(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_087_next_stems(
            self.inside_sites,
            self.next_stems,
        )
        self.with_next = leftover_n4_remaining_remaining_after_087_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next = leftover_n4_remaining_remaining_after_087_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.matching = leftover_n4_remaining_remaining_after_087_with_forward_057(
            self.inside_sites,
            self.next_stems,
        )
        self.without = leftover_n4_remaining_remaining_after_087_without_forward_057(
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
        self.n_remaining_after_020 = len(self.remaining_after_020)
        self.k_087 = len(self.share_087)
        self.n_remaining = len(self.remaining)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.k = len(self.matching)
        self.k_057 = self.k
        self.n_without = len(self.without)
        self.n_remaining_after_057 = self.n_remaining - self.k_057
        self.g, self.unique_k, self.unique = select_remaining_after_087_g(
            self.remaining_stems
        )
        self.still_max_k = remaining_after_087_057_still_max_k(self.remaining_stems)
        self.tied = tuple(
            stem
            for stem, count in remaining_after_087_next_stem_counts(
                self.remaining_stems
            ).items()
            if count == self.unique_k
        )
        self.equals_cycle294 = matching_equals_cycle294_g_set(self.matching)
        self.equals_cycle258 = matching_equals_cycle258_extra_i_057(self.matching)
        self.next_by_site = dict(zip(self.inside_sites, self.next_stems, strict=True))
        self.subset_ok = next_057_sites_subset_of_remaining_after_087(
            self.matching,
            self.remaining,
            self.next_by_site,
        )
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                self.k_057,
                self.still_max_k,
                self.g,
            )
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_4_9_3_6_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/4/9/3/6 stay the cycle-294/293/289/224 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "057"))
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(GRAM3_NESTED_087, ("090", "076", "087"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("020", "087"))
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
        prior_294 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]
        self.assertEqual(prior_294["cycle"], 294)
        self.assertEqual(prior_294["G"], "057")
        self.assertEqual(prior_294["K"], 2)
        self.assertEqual(prior_294["N_remaining_after_087"], 6)
        self.assertEqual(prior_294["N_distinct"], 4)
        self.assertEqual(prior_294["N_hapax"], 2)
        self.assertFalse(prior_294["G_uniquely_most_frequent"])
        self.assertEqual(tuple(prior_294["tied_stems_at_K"]), ("057", "011"))
        self.assertEqual(prior_294["N_tied_at_K"], 2)
        self.assertFalse(
            prior_294["i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem"]
        )
        self.assertFalse(CYCLE294_CLAIM)
        self.assertEqual(CYCLE294_G, "057")
        self.assertEqual(CYCLE294_K, 2)
        self.assertEqual(CYCLE294_N_REMAINING, 6)
        self.assertEqual(CYCLE294_N_DISTINCT, 4)
        self.assertEqual(CYCLE294_N_HAPAX, 2)
        self.assertEqual(CYCLE294_N_TIED, 2)
        self.assertEqual(CYCLE294_TIED_STEMS, ("057", "011"))
        self.assertFalse(CYCLE294_UNIQUE)
        if (
            prior_294["G"] != "057"
            or prior_294["K"] != 2
            or prior_294["N_remaining_after_087"] != 6
            or prior_294["N_distinct"] != 4
            or prior_294["N_hapax"] != 2
            or prior_294["G_uniquely_most_frequent"]
            or prior_294["N_tied_at_K"] != 2
            or tuple(prior_294["tied_stems_at_K"]) != ("057", "011")
        ):
            self.fail(
                "nested cycle 294 unique-max false 2-way tie G=057 K=2 "
                "N_remaining=6 distinct=4 hapax=2 drifted"
            )
        prior_293 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]
        self.assertEqual(prior_293["cycle"], 293)
        self.assertEqual(prior_293["K_087"], 3)
        self.assertEqual(prior_293["N_remaining_after_087"], 6)
        self.assertTrue(
            prior_293[
                "i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087"
            ]
        )
        self.assertTrue(CYCLE293_CLAIM)
        self.assertEqual(CYCLE293_K_087, 3)
        self.assertEqual(CYCLE293_N_REMAINING_AFTER_087, 6)
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
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["N_inside"], 13)
        self.assertEqual(prior_288["N_distinct_next_stems"], 6)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        self.assertFalse(CYCLE288_SHARE_ONE)
        prior_258 = self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]
        self.assertEqual(prior_258["cycle"], 258)
        self.assertEqual(prior_258["N_i_only"], 19)
        self.assertEqual(prior_258["N_extra_total"], 3)
        self.assertTrue(prior_258["i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only"])
        self.assertTrue(CYCLE258_CLAIM)
        self.assertEqual(CYCLE258_N_I_ONLY, 19)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        prior_259 = self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]
        self.assertEqual(prior_259["cycle"], 259)
        self.assertEqual(prior_259["N_i_only"], 2)
        self.assertEqual(prior_259["N_not_i_only"], 0)
        self.assertTrue(
            prior_259["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only"]
        )
        self.assertTrue(CYCLE259_CLAIM)
        self.assertEqual(CYCLE259_N_I_ONLY, 2)
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
        unused_235 = CYCLE235_K
        self.assertEqual(unused_235, 2)
        self.assertTrue(CYCLE235_CLAIM)
        unused_271 = CYCLE271_K_090
        self.assertEqual(unused_271, 2)
        self.assertTrue(CYCLE271_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_057_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_057)
        self.assertTrue(STANDING_DO_NOT_PEEL_011)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_057_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_268_294_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_of_6_and_hypothesis_k_2_holds(self):
        """N_remaining_after_087=6, K_057=2. 057 still max-K. Claim holds."""
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
                self.n_remaining_after_020,
            )
        )
        self.assertEqual(self.n_remaining_after_020, STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(self.k_087, STANDING_K_087)
        self.assertEqual(STANDING_K_087, CYCLE293_K_087)
        self.assertEqual(STANDING_K_087, 3)
        if self.k_087 != 3:
            self.fail("nested cycle 293 K_087 drifted from 3")
        self.assertTrue(
            leftover_n4_remaining_remaining_after_087_nested_counts_hold(
                self.n_inside,
                self.k_020,
                self.n_remaining_after_020,
                self.k_087,
                self.n_remaining,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, CYCLE294_N_REMAINING)
        self.assertEqual(self.n_remaining, CYCLE293_N_REMAINING_AFTER_087)
        self.assertEqual(self.n_remaining, self.n_remaining_after_020 - self.k_087)
        self.assertEqual(9 - 3, 6)
        if self.n_remaining != 6:
            self.fail("measured N_remaining_after_087 drifted from 6")
        self.assertEqual(self.remaining, CYCLE294_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE293_REMAINING_AFTER_087_SITES)
        self.assertEqual(
            self.remaining,
            leftover_n4_remaining_remaining_after_020_without_forward_087(
                self.inside_sites,
                self.next_stems,
            ),
        )
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 6)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 0)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_remaining)
        self.assertEqual(6 + 0, 6)
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(self.k_057, STANDING_K_057)
        self.assertEqual(STANDING_K_057, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_057, 2)
        self.assertEqual(STANDING_K, CYCLE294_K)
        self.assertEqual(STANDING_G, "057")
        self.assertEqual(STANDING_G, CYCLE294_G)
        self.assertEqual(self.g, "057")
        self.assertEqual(self.unique_k, 2)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertFalse(CYCLE294_UNIQUE)
        self.assertTrue(self.still_max_k)
        self.assertTrue(STANDING_057_STILL_MAX_K)
        self.assertEqual(frozenset(self.tied), frozenset(STANDING_TIED_STEMS))
        self.assertEqual(len(self.tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 2)
        self.assertEqual(STANDING_OTHER_TIED_STEMS, ("011",))
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 4)
        self.assertEqual(self.n_remaining_after_057, STANDING_N_REMAINING_AFTER_057)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, 4)
        self.assertEqual(self.k_057 + self.n_remaining_after_057, self.n_remaining)
        self.assertEqual(2 + 4, 6)
        if self.k_057 != 2:
            self.fail("nested-check K_057 drifted from 2")
        if not self.still_max_k or self.g != "057":
            self.fail("057 is no longer a max-K next token of remaining-after-087")
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057(
                self.k_057,
                self.still_max_k,
                self.g,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE294_MATCHING_SITES)
        self.assertTrue(self.equals_cycle294)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE294_G_SITES)
        self.assertTrue(matching_equals_cycle294_g_set(self.matching))
        self.assertEqual(len(CYCLE294_MATCHING_SITES), CYCLE294_K)
        self.assertEqual(CYCLE294_K, 2)
        if len(self.matching) != 2 or not self.equals_cycle294:
            self.fail(
                "leftover n=4 remaining remaining-after-087 next-057 set drifted from cycle-294 G set"
            )
        self.assertTrue(self.subset_ok)
        self.assertTrue(
            next_057_sites_subset_of_remaining_after_087(
                self.matching,
                self.remaining,
                self.next_by_site,
            )
        )
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE271)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE294)
        self.assertFalse(STANDING_SAME_AS_CYCLE258)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE271)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_057_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_057)
        self.assertTrue(STANDING_DO_NOT_PEEL_011)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_057_NOT_LOCKED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT)
        self.assertFalse(CYCLE294_CLAIM)
        self.assertTrue(CYCLE293_CLAIM)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertTrue(CYCLE289_CLAIM)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE292_N_DISTINCT, 5)
        self.assertEqual(CYCLE294_N_DISTINCT, 4)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_remaining_after_087_sites_have_next_057(self):
        """Two remaining-after-087 leftover n=4 remaining sites are 090 076 057."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        self.assertEqual(self.matching_next_4grams, CYCLE294_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia8", 114), ("090", "076", "057", "600")),
            ((SIDE_IA, "Ia9", 28), ("090", "076", "057", "600")),
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
            self.assertEqual(stems[index + STANDING_N2], "057")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "057")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, self.remaining)
            self.assertIn(site, CYCLE294_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE289_MATCHING_SITES)
            self.assertNotIn(site, CYCLE292_MATCHING_SITES)
            self.assertNotIn(site, CYCLE293_MATCHING_SITES)
            self.assertIn(site, CYCLE294_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE294_MATCHING_SITES)
        self.assertTrue(matching_equals_cycle294_g_set(self.matching))
        self.assertTrue(self.subset_ok)
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "057")
            self.assertNotEqual(nxt, "087")
            self.assertNotEqual(nxt, "020")
            self.assertIn(site, self.remaining)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, CYCLE294_MATCHING_SITES)
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_057_SITES)
        self.assertEqual(len(self.without), STANDING_N_REMAINING_AFTER_057)
        for site in self.share_020:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE289_MATCHING_SITES)
        for site in self.share_087:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE293_MATCHING_SITES)
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
            matching_leftover_n4_remaining_remaining_after_087_local_4gram_rows(),
            matching_leftover_n4_remaining_remaining_after_087_local_4gram_rows(
                STANDING_MATCHING_SITES,
                STANDING_MATCHING_NEXT_4GRAMS,
            ),
        )
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_057)
        self.assertTrue(STANDING_DO_NOT_PEEL_011)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_057_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_cycle258_extra_i_057_equals_matching_057(self):
        """Cycle 258 extra I of 090 076 057 equals leftover n=4 remaining remaining-after-087 057."""
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        self.assertIn("057", CYCLE258_REMAINING11_NEXT_STEMS)
        extra_057_index = CYCLE258_REMAINING11_NEXT_STEMS.index("057")
        self.assertEqual(CYCLE258_EXTRA_I_SITES_EACH[extra_057_index], CYCLE258_EXTRA_I_057)
        self.assertEqual(CYCLE258_EXTRA_I_057, STANDING_MATCHING_SITES)
        self.assertEqual(
            CYCLE258_EXTRA_I_057,
            (
                (SIDE_IA, "Ia8", 114),
                (SIDE_IA, "Ia9", 28),
            ),
        )
        self.assertEqual(CYCLE259_EXTRA_I_BY_X["057"], STANDING_MATCHING_SITES)
        self.assertTrue(matching_equals_cycle258_extra_i_057(self.matching))
        self.assertTrue(self.equals_cycle258)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE258_EXTRA_I)
        self.assertEqual(self.matching, CYCLE258_EXTRA_I_057)
        for site in self.matching:
            self.assertIn(site, CYCLE258_EXTRA_I_057)
            self.assertIn(site, CYCLE259_EXTRA_I_BY_X["057"])
        leftover_extra_057 = tuple(
            site
            for site in CYCLE258_I_SITES_EACH[extra_057_index]
            if site not in CYCLE258_EXTRA_I_057
        )
        self.assertEqual(leftover_extra_057, ((SIDE_IA, "Ia9", 129),))
        for site in leftover_extra_057:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        overlap = tuple(site for site in self.matching if site in CYCLE258_EXTRA_I_057)
        self.assertEqual(overlap, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE)
        prior_258 = self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]
        self.assertEqual(prior_258["cycle"], 258)
        self.assertEqual(prior_258["N_i_only"], 19)
        self.assertEqual(prior_258["N_extra_total"], 3)
        extra_258 = tuple(
            tuple(tuple(row) for row in seq["extra_i_sites"])
            for seq in prior_258["sequences"]
        )
        self.assertEqual(extra_258[extra_057_index], CYCLE258_EXTRA_I_057)
        self.assertEqual(extra_258[extra_057_index], self.matching)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_294_293_292_259_258_224_223_still_compute(self):
        """Cycle 294 057/2/6/4 tie, 293 K_087=3, 292 G=087 K=3, 259 2/0, 258 extra I=2 of 057, 224 13/56, 223 69/3 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_294 = TestMamariILeftoverN4Remaining090076RemainingAfter087NextStemScoreboard()
        prior_294.setUp()
        prior_294.test_counts_6_remaining_g_057_k_2_tie_and_hypothesis_loses()
        prior_294.test_survey_matches_computed_lock()
        self.assertEqual(prior_294.g, "057")
        self.assertEqual(prior_294.k, 2)
        self.assertEqual(prior_294.n_remaining, 6)
        self.assertEqual(prior_294.n_distinct, 4)
        self.assertFalse(prior_294.unique)
        self.assertFalse(prior_294.claim_holds)
        self.assertFalse(CYCLE294_CLAIM)
        self.assertEqual(CYCLE294_G, "057")
        self.assertEqual(CYCLE294_K, 2)
        self.assertEqual(CYCLE294_N_REMAINING, 6)
        self.assertEqual(CYCLE294_N_DISTINCT, 4)
        if (
            prior_294.g != "057"
            or prior_294.k != 2
            or prior_294.n_remaining != 6
            or prior_294.n_distinct != 4
            or prior_294.unique
            or prior_294.claim_holds
        ):
            self.fail(
                "nested cycle 294 unique-max false G=057 K=2 N_remaining=6 distinct=4 drifted"
            )
        prior_293 = TestMamariILeftoverN4Remaining090076RemainingAfter020Forward087Scoreboard()
        prior_293.setUp()
        prior_293.test_counts_3_of_9_and_hypothesis_k_3_holds()
        prior_293.test_survey_matches_computed_lock()
        self.assertEqual(prior_293.k_087, 3)
        self.assertEqual(prior_293.n_remaining_after_087, 6)
        self.assertEqual(prior_293.matching, CYCLE293_MATCHING_SITES)
        self.assertEqual(self.share_087, prior_293.matching)
        self.assertEqual(self.remaining, prior_293.without)
        self.assertTrue(prior_293.claim_holds)
        self.assertTrue(CYCLE293_CLAIM)
        if prior_293.k_087 != 3 or prior_293.n_remaining_after_087 != 6:
            self.fail(
                "nested cycle 293 leftover n=4 remaining remaining-after-020 exactly 3 share 087 / N_remaining=6 drifted"
            )
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
        if (
            prior_292.g != "087"
            or prior_292.k != 3
            or prior_292.n_remaining != 9
            or not prior_292.unique
        ):
            self.fail(
                "nested cycle 292 unique-max G=087 K=3 N_remaining=9 drifted"
            )
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(prior_259.n_i_only, 2)
        self.assertEqual(prior_259.n_not_i_only, 0)
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        self.assertEqual(CYCLE259_N_I_ONLY, 2)
        if prior_259.n_i_only != 2 or prior_259.n_not_i_only != 0:
            self.fail("nested cycle 259 extra-I fwd4 090 076 057 600 2/0 drifted")
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_258.test_survey_matches_computed_lock()
        extra_057_index = CYCLE258_REMAINING11_NEXT_STEMS.index("057")
        self.assertEqual(prior_258.n_i_only, 19)
        self.assertEqual(len(prior_258.extra[extra_057_index]), 2)
        self.assertEqual(prior_258.extra[extra_057_index], CYCLE258_EXTRA_I_057)
        self.assertEqual(prior_258.extra[extra_057_index], self.matching)
        self.assertTrue(prior_258.claim_holds)
        self.assertTrue(CYCLE258_CLAIM)
        if prior_258.n_i_only != 19 or len(prior_258.extra[extra_057_index]) != 2:
            self.fail("nested cycle 258 remaining-after-000 3-grams 19/19 extra I=2 of 057 drifted")
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
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_057)
        self.assertTrue(STANDING_DO_NOT_PEEL_011)
        self.assertTrue(STANDING_CYCLE167_268_294_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-295 leftover n=4 remaining remaining-after-087 057 lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_forward_057"]
        self.assertEqual(lock["cycle"], 295)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(tuple(lock["forward_3gram"]), ("090", "076", "057"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(tuple(lock["locked_forward_stems"]), ("020", "087"))
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
        self.assertEqual(lock["K_087"], STANDING_K_087)
        self.assertEqual(lock["K_087"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_087_sites"]),
            CYCLE293_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_087"], STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(lock["N_remaining_after_087"], 6)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_087_sites"]),
            CYCLE294_REMAINING_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 6)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 0)
        self.assertEqual(lock["no_next_sites"], [])
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 4)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 2)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "057")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertEqual(lock["K_057"], STANDING_K_057)
        self.assertEqual(lock["K_057"], 2)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 4)
        self.assertEqual(lock["N_remaining_after_057"], STANDING_N_REMAINING_AFTER_057)
        self.assertEqual(lock["N_remaining_after_057"], 4)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertTrue(lock["057_still_max_K"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 2)
        self.assertEqual(tuple(lock["other_tied_stems"]), STANDING_OTHER_TIED_STEMS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_remaining_after_087_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_remaining_after_087_sites"]),
            CYCLE294_MATCHING_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle294_g_sites"])
        self.assertEqual(
            lock["matching_equals_cycle294_g_sites"],
            STANDING_MATCHING_EQUALS_CYCLE294_G_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle258_extra_i"])
        self.assertEqual(
            lock["matching_equals_cycle258_extra_i"],
            STANDING_MATCHING_EQUALS_CYCLE258_EXTRA_I,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_remaining_after_087_local_4grams"],
            matching_leftover_n4_remaining_remaining_after_087_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_057_sites"]),
            STANDING_REMAINING_AFTER_057_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle294_G_sites"]),
            CYCLE294_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle258_extra_i_057_sites"]),
            CYCLE258_EXTRA_I_057,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["overlap_with_cycle258_extra_i_057"]),
            STANDING_MATCHING_SITES,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057"]
        )
        self.assertEqual(
            lock["i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057"],
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057,
        )
        self.assertEqual(lock["nested_cycle294_G"], "057")
        self.assertEqual(lock["nested_cycle294_K"], 2)
        self.assertEqual(lock["nested_cycle294_N_remaining_after_087"], 6)
        self.assertEqual(lock["nested_cycle294_N_distinct"], 4)
        self.assertEqual(lock["nested_cycle294_N_hapax"], 2)
        self.assertFalse(lock["nested_cycle294_unique_next_stem"])
        self.assertEqual(lock["nested_cycle294_N_tied_at_K"], 2)
        self.assertEqual(tuple(lock["nested_cycle294_tied_stems"]), ("057", "011"))
        self.assertEqual(lock["nested_cycle293_K_087"], 3)
        self.assertEqual(lock["nested_cycle293_N_remaining_after_087"], 6)
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
        self.assertEqual(lock["nested_cycle259_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle259_N_not_i_only"], 0)
        self.assertTrue(lock["nested_cycle259_extra_i_fwd4_all_i_only"])
        self.assertEqual(lock["nested_cycle258_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle258_N_extra"], 3)
        self.assertEqual(lock["nested_cycle258_extra_I_of_057"], 2)
        self.assertTrue(lock["nested_cycle258_3grams_all_i_only"])
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle235_K"], 2)
        self.assertTrue(lock["nested_cycle235_exactly_2_share_700"])
        self.assertEqual(lock["nested_cycle271_K_090"], 2)
        self.assertTrue(lock["nested_cycle271_exactly_2_share_previous_090"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle235"])
        self.assertFalse(lock["same_as_cycle271"])
        self.assertFalse(lock["same_as_cycle289"])
        self.assertFalse(lock["same_as_cycle293"])
        self.assertFalse(lock["same_as_cycle294"])
        self.assertFalse(lock["same_as_cycle258"])
        self.assertTrue(lock["same_claim_shape_as_cycle235"])
        self.assertTrue(lock["same_claim_shape_as_cycle271"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_leftover_n4_remaining_090_076_057_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_remaining_after_057"])
        self.assertTrue(lock["do_not_peel_011"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_057_not_locked"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["cycle167_268_294_not_overwritten"])
        self.assertTrue(lock["extra_i_mismatch_does_not_lose"])
        self.assertTrue(lock["other_tied_stems_not_locked"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_087_next_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_forward_087_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_020_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_fwd700_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_090_unchanged"]
        )
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]["cycle"],
            294,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]["G"],
            "057",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]["K"],
            2,
        )
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"][
                "i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]["cycle"],
            293,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]["K_087"],
            3,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["cycle"],
            292,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["G"],
            "087",
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_020"]["cycle"], 289)
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_020"]["K"], 4)
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]["cycle"],
            259,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]["N_i_only"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]["cycle"],
            258,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]["N_extra_total"],
            3,
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


class TestMamariILeftoverN4Remaining090076RemainingAfter087Forward057ImageSnapshot(
    unittest.TestCase
):
    """Cycle 295 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
