"""I's cycle-296 leftover n=4 remaining remaining-after-057 forward-011 lock.

Cycle 297 text-search lock. Uses already-vendored A–V and the
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
next 087 (cycle 293), leftover n=4 remaining remaining-
after-087 unique next stem (cycle 294 lost), leftover n=4
remaining remaining-after-087 exactly 2 share next 057
(cycle 295), or leftover n=4 remaining remaining-after-057
unique next stem (cycle 296). Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Cycle 296 leftover n=4 remaining remaining-after-057 unique
next stem HOLDS: unique-max true, G=011 K=2, N_remaining_
after_057=4, N_with_next=4, N_no_next=0, N_distinct=3,
hapax=2 (607/021). Unique-max G/K is inventory; this cycle
peels 011 as exact-K. Same claim-shape as cycle 235 leftover
extra remaining-after-001 exactly 2 share 700 and cycle 295
leftover n=4 remaining remaining-after-087 exactly 2 share
next 057 (exactly K share unique-max G), leftover n=4
remaining remaining-after-057 next 011 instead of leftover
extra remaining-after-001 / leftover n=4 remaining remaining-
after-087. Hold-path analog cycle 293 leftover n=4 remaining
remaining-after-020 exactly 3 share next 087 after unique-max
HOLD. Do not peel remaining-after-011 this cycle. Do not
retune leftover n=4. Do not retune leftover extra peels. Do
not lock leftover n=4 remaining remaining-after-011 next
stems this cycle. Do not lock I-only of leftover n=4 remaining
090 076 011 this cycle (cycle 248 already owns the 3-gram).
Off-I T sites are not this cycle. 076 071 and 076 070 do not
count as this 2-gram. Leftover extra sites do not count as
leftover n=4 remaining.

Hypothesis K=2: leftover n=4 remaining remaining-after-057 I
090 076 sites include exactly 2 that share next stem 011
(forward 3-gram 090 076 011). Nested-check leftover n=4
remaining N_inside==13, K_020==4, N_remaining_after_020==9,
K_087==3, N_remaining_after_087==6, K_057==2,
N_remaining_after_057==4 (do not retune
224/288/289/292/293/294/295/296). Nested-check cycle 296:
unique-max true, G=011 K=2, N_distinct=3 (do not retune).
Count leftover n=4 remaining remaining-after-057 I 090 076
sites whose next token is 011. Cycle 296 listed Ia2[107]/
Ia14[54]; measure, do not assume if nested-check differs.
N_remaining_after_011 = N_remaining_after_057 − K_011.
Unique-max next of remaining-after-057 is still 011. Nested-
check each next-011 remaining-after-057 site ⊆ leftover n=4
remaining remaining-after-057 and has next token 011.
Nested-check (compute, do not retune) cycle 248 extra I of
leftover extra 090 076 011: whether leftover n=4 remaining
remaining-after-057 011 sites equal those extra I 090-starts.
Extra I mismatch does not make this claim lose; still lock
the overlap. Claim that can lose:
i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011.
True iff K_011==2 among leftover n=4 remaining remaining-
after-057 I 090 076 and unique-max next of remaining-after-
057 is still 011. The claim is true. This can lose if
nested-check K differs from 2, or if unique-max is no longer
011. Nested cycle 296 unique-max G=011 K=2 N_remaining=4
distinct=3, cycle 295 K_057=2, cycle 294 unique-max false
2-way tie, cycle 248 4/0 extra I=2, cycle 247 leftover extra
exactly 2 share 011, cycle 224 13/56, and cycle 223 69/3
stay. Do not assume the result; measure. Do not retune.

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
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    GRAM3 as CYCLE248_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE248_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_011_I_ONLY as CYCLE248_CLAIM,
    STANDING_I_SITES as CYCLE248_I_SITES,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE248_LEFTOVER_MATCHING_SITES,
    STANDING_N_EXTRA as CYCLE248_N_EXTRA,
    STANDING_N_I as CYCLE248_N_I,
    STANDING_N_OFF_I as CYCLE248_N_OFF_I,
    TestMamariI3gram090076011IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_fwd700_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_2_SHARE_700 as CYCLE235_CLAIM,
    STANDING_K as CYCLE235_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_087_fwd011_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_011 as CYCLE247_CLAIM,
    STANDING_K as CYCLE247_K,
    STANDING_MATCHING_SITES as CYCLE247_MATCHING_SITES,
    TestMamariILeftoverExtra090076RemainingAfter087Fwd011Scoreboard,
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
    STANDING_MATCHING_EQUALS_CYCLE245_EXTRA_I as CYCLE293_EQUALS_245,
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
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_057_next_stem_scoreboard import (
    LOCKED_FORWARD_STEMS,
    STANDING_G as CYCLE296_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE296_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_UNIQUE_NEXT_STEM as CYCLE296_CLAIM,
    STANDING_K as CYCLE296_K,
    STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I as CYCLE296_EQUALS_248,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE296_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE296_MATCHING_SITES,
    STANDING_N_DISTINCT as CYCLE296_N_DISTINCT,
    STANDING_N_HAPAX as CYCLE296_N_HAPAX,
    STANDING_N_REMAINING_AFTER_057 as CYCLE296_N_REMAINING,
    STANDING_REMAINING_SITES as CYCLE296_REMAINING_SITES,
    leftover_n4_remaining_remaining_after_057,
    leftover_n4_remaining_remaining_after_057_nested_counts_hold,
    leftover_n4_remaining_remaining_after_057_next_stems,
    leftover_n4_remaining_remaining_after_057_with_g,
    leftover_n4_remaining_remaining_after_057_with_next,
    leftover_n4_remaining_remaining_after_057_without_g,
    leftover_n4_remaining_remaining_after_057_without_next,
    matching_equals_cycle248_extra_i,
    matching_leftover_n4_remaining_remaining_after_057_local_4gram_rows,
    remaining_after_057_next_stem_counts,
    select_remaining_after_057_g,
    TestMamariILeftoverN4Remaining090076RemainingAfter057NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_087_forward_057_scoreboard import (
    CYCLE258_EXTRA_I_057,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057 as CYCLE295_CLAIM,
    STANDING_K_057 as CYCLE295_K_057,
    STANDING_MATCHING_EQUALS_CYCLE258_EXTRA_I as CYCLE295_EQUALS_258,
    STANDING_MATCHING_SITES as CYCLE295_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_057 as CYCLE295_N_REMAINING_AFTER_057,
    STANDING_N_REMAINING_AFTER_087 as CYCLE295_N_REMAINING_AFTER_087,
    STANDING_REMAINING_AFTER_057_SITES as CYCLE295_REMAINING_AFTER_057_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter087Forward057Scoreboard,
    leftover_n4_remaining_remaining_after_087_with_forward_057,
    leftover_n4_remaining_remaining_after_087_without_forward_057,
    matching_equals_cycle258_extra_i_057,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_087_next_stem_scoreboard import (
    STANDING_G as CYCLE294_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE294_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_UNIQUE_NEXT_STEM as CYCLE294_CLAIM,
    STANDING_K as CYCLE294_K,
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
    leftover_n4_remaining_remaining_after_087_with_next,
    leftover_n4_remaining_remaining_after_087_without_next,
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
GRAM3_FORWARD = ("090", "076", "011")
GRAM3_NESTED_020_TOKENS = ("090", "076", "020")
GRAM3_NESTED_087 = ("090", "076", "087")
GRAM3_NESTED_057 = ("090", "076", "057")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_NEXT_INSIDE = 13
STANDING_N_NO_NEXT_INSIDE = 0
STANDING_K_020 = 4
STANDING_N_REMAINING_AFTER_020 = 9
STANDING_K_087 = 3
STANDING_N_REMAINING_AFTER_087 = 6
STANDING_K_057 = 2
STANDING_N_REMAINING_AFTER_057 = 4
STANDING_N_WITH_NEXT = 4
STANDING_N_NO_NEXT = 0
STANDING_NO_NEXT_SITES = ()
STANDING_N_DISTINCT = 3
STANDING_N_HAPAX = 2
STANDING_K = 2
STANDING_K_011 = 2
STANDING_G = "011"
STANDING_N_WITHOUT = 2
STANDING_N_REMAINING_AFTER_011 = 2
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia14", 54),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "011", "027"),
    ("090", "076", "011", "400"),
)
STANDING_REMAINING_AFTER_011_SITES = (
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia13", 17),
)
STANDING_MATCHING_EQUALS_CYCLE296_G_SITES = True
STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I = True
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_UNIQUE_MAX_STILL_011 = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011"
)
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011 = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_057_forward_011"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE235 = False
STANDING_SAME_AS_CYCLE247 = False
STANDING_SAME_AS_CYCLE248 = False
STANDING_SAME_AS_CYCLE293 = False
STANDING_SAME_AS_CYCLE295 = False
STANDING_SAME_AS_CYCLE296 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE295 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_011_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_REMAINING_AFTER_011 = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_011_NOT_LOCKED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_CYCLE167_268_296_NOT_OVERWRITTEN = True
STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE = True


def leftover_n4_remaining_remaining_after_057_with_forward_011(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-057 sites whose next token is 011."""
    return leftover_n4_remaining_remaining_after_057_with_g(
        sites,
        next_stems,
        stem=stem,
        locked=locked,
    )


def leftover_n4_remaining_remaining_after_057_without_forward_011(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-057 sites whose next token is not 011."""
    return leftover_n4_remaining_remaining_after_057_without_g(
        sites,
        next_stems,
        stem=stem,
        locked=locked,
    )


def remaining_after_057_011_still_unique_max(
    remaining_stems: tuple[str, ...],
    stem: str = STANDING_G,
) -> bool:
    """True iff unique-max next of remaining-after-057 is still 011."""
    gram, _count, unique = select_remaining_after_057_g(remaining_stems)
    return unique and gram == stem


def matching_equals_cycle296_g_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle296_g_sites: tuple[tuple[str, str, int], ...] = CYCLE296_MATCHING_SITES,
) -> bool:
    """True iff remaining-after-057 next-011 sites equal the cycle-296 G set."""
    return matching_sites == cycle296_g_sites


def next_011_sites_subset_of_remaining_after_057(
    matching_sites: tuple[tuple[str, str, int], ...],
    remaining: tuple[tuple[str, str, int], ...],
    next_stems_by_site: dict[tuple[str, str, int], str | None],
    stem: str = STANDING_G,
) -> bool:
    """True iff each next-011 site ⊆ remaining-after-057 and has next token 011."""
    remaining_set = set(remaining)
    return all(
        site in remaining_set and next_stems_by_site.get(site) == stem
        for site in matching_sites
    )


def i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
    k: int,
    unique: bool,
    g: str | None,
    expected: int = HYPOTHESIS_K,
    expected_g: str = STANDING_G,
) -> bool:
    """True iff K_011 equals 2 and unique-max next is still 011."""
    return k == expected and unique and g == expected_g


class TestILeftoverN4Remaining090076RemainingAfter057Forward011Helpers(
    unittest.TestCase
):
    """Helpers on leftover n=4 remaining remaining-after-057 next 011. No CV, no LLM."""

    def test_forward_011_requires_stem_after_2gram_and_not_020_087_057(self):
        """Next stem 011 is 090 076 011; next 020/087/057 are not remaining-after-057."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "011"))
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(GRAM3_NESTED_020_TOKENS, GRAM3_NESTED_020)
        self.assertEqual(GRAM3_NESTED_087, ("090", "076", "087"))
        self.assertEqual(GRAM3_NESTED_057, ("090", "076", "057"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("020", "087", "057"))
        self.assertEqual(GRAM3_FORWARD[:STANDING_N2], GRAM2)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_011 = ["090", "076", "011", "027"]
        self.assertEqual(site_next_stem(has_011, 0, GRAM2), "011")
        self.assertEqual(site_forward_3gram(has_011, 0, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_011, 0, GRAM2),
            ("090", "076", "011", "027"),
        )
        has_057 = ["090", "076", "057", "600"]
        self.assertEqual(site_next_stem(has_057, 0, GRAM2), "057")
        self.assertNotEqual(site_next_stem(has_057, 0, GRAM2), "011")
        has_087 = ["090", "076", "087", "291"]
        self.assertEqual(site_next_stem(has_087, 0, GRAM2), "087")
        self.assertNotEqual(site_next_stem(has_087, 0, GRAM2), "011")
        has_020 = ["090", "076", "020", "010"]
        self.assertEqual(site_next_stem(has_020, 0, GRAM2), "020")
        self.assertNotEqual(site_next_stem(has_020, 0, GRAM2), "011")
        other_next = ["600", "090", "076", "607", "999"]
        self.assertEqual(site_next_stem(other_next, 1, GRAM2), "607")
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
            (SIDE_IA, "Ia1", 5),
        )
        planted_stems = ("011", "020", "087", "057", None, "607")
        self.assertEqual(
            leftover_n4_remaining_remaining_after_057_with_forward_011(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_057_without_forward_011(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[5],),
        )
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when K=2 and unique-max G is 011."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                2, True, "011"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                0, True, "011"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                1, True, "011"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                3, True, "011"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                4, True, "011"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                2, False, "011"
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                2, True, "057"
            )
        )
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 2),)
        planted_stems = ("011",) * 3
        self.assertEqual(
            leftover_n4_remaining_remaining_after_057_with_forward_011(
                planted,
                planted_stems,
            ),
            planted,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                len(planted), True, "011"
            )
        )
        self.assertTrue(remaining_after_057_011_still_unique_max(("011", "011", "607")))
        self.assertFalse(remaining_after_057_011_still_unique_max(("011", "607", "021")))
        self.assertFalse(remaining_after_057_011_still_unique_max(("011", "011", "607", "607")))
        self.assertFalse(remaining_after_057_011_still_unique_max(()))
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011,
            HYPOTHESIS_K == STANDING_K_011 and STANDING_UNIQUE_MAX_STILL_011,
        )
        self.assertEqual(
            STANDING_K_011 + STANDING_N_REMAINING_AFTER_011,
            STANDING_N_REMAINING_AFTER_057,
        )
        self.assertEqual(2 + 2, 4)
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

    def test_cycle296_set_and_cycle248_extra_can_diverge(self):
        """Cycle-296 G-site equality and cycle-248 extra I of 011 equality can fail."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle296_g_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE296_G_SITES)
        self.assertTrue(matching_equals_cycle248_extra_i(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle296_g_set(planted))
        self.assertFalse(matching_equals_cycle248_extra_i(planted))
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                len(planted), True, "011"
            )
        )
        self.assertTrue(STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_011)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_011_NOT_LOCKED)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE295)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE247)
        self.assertFalse(STANDING_SAME_AS_CYCLE248)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE295)
        self.assertFalse(STANDING_SAME_AS_CYCLE296)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter057Forward011Scoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-057 forward-011 lock. Mock only."""

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
        self.remaining_after_087 = leftover_n4_remaining_remaining_after_087(
            self.inside_sites,
            self.next_stems,
        )
        self.share_057 = leftover_n4_remaining_remaining_after_087_with_forward_057(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining = leftover_n4_remaining_remaining_after_057(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_057_next_stems(
            self.inside_sites,
            self.next_stems,
        )
        self.with_next = leftover_n4_remaining_remaining_after_057_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next = leftover_n4_remaining_remaining_after_057_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.matching = leftover_n4_remaining_remaining_after_057_with_forward_011(
            self.inside_sites,
            self.next_stems,
        )
        self.without = leftover_n4_remaining_remaining_after_057_without_forward_011(
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
        self.n_remaining_after_087 = len(self.remaining_after_087)
        self.k_057 = len(self.share_057)
        self.n_remaining = len(self.remaining)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.k = len(self.matching)
        self.k_011 = self.k
        self.n_without = len(self.without)
        self.n_remaining_after_011 = self.n_remaining - self.k_011
        self.g, self.unique_k, self.unique = select_remaining_after_057_g(
            self.remaining_stems
        )
        self.still_unique_max = remaining_after_057_011_still_unique_max(
            self.remaining_stems
        )
        self.equals_cycle296 = matching_equals_cycle296_g_set(self.matching)
        self.equals_cycle248 = matching_equals_cycle248_extra_i(self.matching)
        self.next_by_site = dict(zip(self.inside_sites, self.next_stems, strict=True))
        self.subset_ok = next_011_sites_subset_of_remaining_after_057(
            self.matching,
            self.remaining,
            self.next_by_site,
        )
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                self.k_011,
                self.unique,
                self.g,
            )
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_4_9_3_6_2_4_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/4/9/3/6/2/4 stay prior locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "011"))
        self.assertEqual(GRAM3_FORWARD, CYCLE248_GRAM3)
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(GRAM3_NESTED_087, ("090", "076", "087"))
        self.assertEqual(GRAM3_NESTED_057, ("090", "076", "057"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("020", "087", "057"))
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
        prior_296 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"]
        self.assertEqual(prior_296["cycle"], 296)
        self.assertEqual(prior_296["G"], "011")
        self.assertEqual(prior_296["K"], 2)
        self.assertEqual(prior_296["N_remaining_after_057"], 4)
        self.assertEqual(prior_296["N_distinct"], 3)
        self.assertTrue(prior_296["G_uniquely_most_frequent"])
        self.assertTrue(
            prior_296["i_leftover_n4_remaining_090_076_remaining_after_057_unique_next_stem"]
        )
        self.assertTrue(CYCLE296_CLAIM)
        self.assertEqual(CYCLE296_G, "011")
        self.assertEqual(CYCLE296_K, 2)
        self.assertEqual(CYCLE296_N_REMAINING, 4)
        self.assertEqual(CYCLE296_N_DISTINCT, 3)
        self.assertTrue(CYCLE296_UNIQUE)
        if (
            prior_296["G"] != "011"
            or prior_296["K"] != 2
            or prior_296["N_remaining_after_057"] != 4
            or prior_296["N_distinct"] != 3
            or not prior_296["G_uniquely_most_frequent"]
            or not prior_296["i_leftover_n4_remaining_090_076_remaining_after_057_unique_next_stem"]
        ):
            self.fail(
                "nested cycle 296 unique-max G=011 K=2 N_remaining=4 distinct=3 drifted"
            )
        prior_295 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_forward_057"]
        self.assertEqual(prior_295["cycle"], 295)
        self.assertEqual(prior_295["K_057"], 2)
        self.assertEqual(prior_295["N_remaining_after_057"], 4)
        self.assertEqual(prior_295["N_remaining_after_087"], 6)
        self.assertTrue(
            prior_295["i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057"]
        )
        self.assertTrue(CYCLE295_CLAIM)
        self.assertEqual(CYCLE295_K_057, 2)
        self.assertEqual(CYCLE295_N_REMAINING_AFTER_057, 4)
        self.assertEqual(CYCLE295_N_REMAINING_AFTER_087, 6)
        prior_294 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]
        self.assertEqual(prior_294["cycle"], 294)
        self.assertEqual(prior_294["G"], "057")
        self.assertEqual(prior_294["K"], 2)
        self.assertEqual(prior_294["N_remaining_after_087"], 6)
        self.assertEqual(prior_294["N_distinct"], 4)
        self.assertFalse(prior_294["G_uniquely_most_frequent"])
        self.assertFalse(CYCLE294_CLAIM)
        self.assertEqual(CYCLE294_G, "057")
        self.assertEqual(CYCLE294_K, 2)
        self.assertEqual(CYCLE294_N_REMAINING, 6)
        self.assertEqual(CYCLE294_N_DISTINCT, 4)
        self.assertFalse(CYCLE294_UNIQUE)
        prior_293 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]
        self.assertEqual(prior_293["cycle"], 293)
        self.assertEqual(prior_293["K_087"], 3)
        self.assertEqual(prior_293["N_remaining_after_087"], 6)
        self.assertTrue(
            prior_293["i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087"]
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
        prior_248 = self.survey["i_3gram_090_076_011_i_only"]
        self.assertEqual(prior_248["cycle"], 248)
        self.assertEqual(prior_248["N_I"], 4)
        self.assertEqual(prior_248["N_off_I"], 0)
        self.assertEqual(prior_248["N_extra"], 2)
        self.assertTrue(prior_248["i_3gram_090_076_011_i_only"])
        self.assertTrue(CYCLE248_CLAIM)
        self.assertEqual(CYCLE248_N_I, 4)
        self.assertEqual(CYCLE248_N_OFF_I, 0)
        self.assertEqual(CYCLE248_N_EXTRA, 2)
        prior_247 = self.survey["i_leftover_extra_090_076_remaining_after_087_fwd011"]
        self.assertEqual(prior_247["cycle"], 247)
        self.assertEqual(prior_247["K"], 2)
        self.assertTrue(prior_247["i_leftover_extra_090_076_remaining_after_087_exactly_2_share_011"])
        self.assertTrue(CYCLE247_CLAIM)
        self.assertEqual(CYCLE247_K, 2)
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
        unused_296_hapax = CYCLE296_N_HAPAX
        self.assertEqual(unused_296_hapax, 2)
        unused_294_hapax = CYCLE294_N_HAPAX
        self.assertEqual(unused_294_hapax, 2)
        unused_294_tied = CYCLE294_N_TIED
        self.assertEqual(unused_294_tied, 2)
        unused_294_tied_stems = CYCLE294_TIED_STEMS
        self.assertEqual(unused_294_tied_stems, ("057", "011"))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_011)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_011_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_268_296_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_of_4_and_hypothesis_k_2_holds(self):
        """N_remaining_after_057=4, K_011=2. Unique-max still 011. Claim holds."""
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
                self.n_remaining_after_087,
            )
        )
        self.assertEqual(self.k_057, STANDING_K_057)
        self.assertEqual(STANDING_K_057, CYCLE295_K_057)
        self.assertEqual(STANDING_K_057, 2)
        if self.k_057 != 2:
            self.fail("nested cycle 295 K_057 drifted from 2")
        self.assertTrue(
            leftover_n4_remaining_remaining_after_057_nested_counts_hold(
                self.n_inside,
                self.k_020,
                self.n_remaining_after_020,
                self.k_087,
                self.n_remaining_after_087,
                self.k_057,
                self.n_remaining,
            )
        )
        self.assertEqual(self.n_remaining_after_087, STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, CYCLE294_N_REMAINING)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_057)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, 4)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, CYCLE296_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, CYCLE295_N_REMAINING_AFTER_057)
        self.assertEqual(self.n_remaining, self.n_remaining_after_087 - self.k_057)
        self.assertEqual(6 - 2, 4)
        if self.n_remaining != 4:
            self.fail("measured N_remaining_after_057 drifted from 4")
        self.assertEqual(self.remaining, CYCLE296_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE295_REMAINING_AFTER_057_SITES)
        self.assertEqual(
            self.remaining,
            leftover_n4_remaining_remaining_after_087_without_forward_057(
                self.inside_sites,
                self.next_stems,
            ),
        )
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 4)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 0)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_remaining)
        self.assertEqual(4 + 0, 4)
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(self.k_011, STANDING_K_011)
        self.assertEqual(STANDING_K_011, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_011, 2)
        self.assertEqual(STANDING_K, CYCLE296_K)
        self.assertEqual(STANDING_G, "011")
        self.assertEqual(STANDING_G, CYCLE296_G)
        self.assertEqual(self.g, "011")
        self.assertEqual(self.unique_k, 2)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(CYCLE296_UNIQUE)
        self.assertTrue(self.still_unique_max)
        self.assertTrue(STANDING_UNIQUE_MAX_STILL_011)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 2)
        self.assertEqual(self.n_remaining_after_011, STANDING_N_REMAINING_AFTER_011)
        self.assertEqual(STANDING_N_REMAINING_AFTER_011, 2)
        self.assertEqual(self.k_011 + self.n_remaining_after_011, self.n_remaining)
        self.assertEqual(2 + 2, 4)
        if self.k_011 != 2:
            self.fail("nested-check K_011 drifted from 2")
        if self.g != "011" or not self.unique:
            self.fail("unique-max next is no longer 011")
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011(
                self.k_011,
                self.unique,
                self.g,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, CYCLE296_MATCHING_SITES)
        self.assertTrue(self.equals_cycle296)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE296_G_SITES)
        self.assertTrue(matching_equals_cycle296_g_set(self.matching))
        self.assertEqual(len(CYCLE296_MATCHING_SITES), CYCLE296_K)
        self.assertEqual(CYCLE296_K, 2)
        if len(self.matching) != 2 or not self.equals_cycle296:
            self.fail(
                "leftover n=4 remaining remaining-after-057 next-011 set drifted from cycle-296 G set"
            )
        self.assertTrue(self.subset_ok)
        self.assertTrue(
            next_011_sites_subset_of_remaining_after_057(
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
        self.assertFalse(STANDING_SAME_AS_CYCLE247)
        self.assertFalse(STANDING_SAME_AS_CYCLE248)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE295)
        self.assertFalse(STANDING_SAME_AS_CYCLE296)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE293)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE295)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_011)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_011_NOT_LOCKED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT)
        self.assertTrue(CYCLE296_CLAIM)
        self.assertTrue(CYCLE295_CLAIM)
        self.assertFalse(CYCLE294_CLAIM)
        self.assertTrue(CYCLE293_CLAIM)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertTrue(CYCLE289_CLAIM)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE292_N_DISTINCT, 5)
        self.assertEqual(CYCLE294_N_DISTINCT, 4)
        self.assertEqual(CYCLE296_N_DISTINCT, 3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_remaining_after_057_sites_have_next_011(self):
        """Two remaining-after-057 leftover n=4 remaining sites are 090 076 011."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        self.assertEqual(self.matching_next_4grams, CYCLE296_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia2", 107), ("090", "076", "011", "027")),
            ((SIDE_IA, "Ia14", 54), ("090", "076", "011", "400")),
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
            self.assertEqual(stems[index + STANDING_N2], "011")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "011")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, self.remaining)
            self.assertIn(site, CYCLE296_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE289_MATCHING_SITES)
            self.assertNotIn(site, CYCLE292_MATCHING_SITES)
            self.assertNotIn(site, CYCLE293_MATCHING_SITES)
            self.assertNotIn(site, CYCLE294_MATCHING_SITES)
            self.assertNotIn(site, CYCLE295_MATCHING_SITES)
            self.assertIn(site, CYCLE296_MATCHING_SITES)
            self.assertIn(site, CYCLE248_EXTRA_I_SITES)
            self.assertIn(site, CYCLE248_I_SITES)
        self.assertEqual(self.matching, CYCLE296_MATCHING_SITES)
        self.assertTrue(matching_equals_cycle296_g_set(self.matching))
        self.assertTrue(self.subset_ok)
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "011")
            self.assertNotEqual(nxt, "057")
            self.assertNotEqual(nxt, "087")
            self.assertNotEqual(nxt, "020")
            self.assertIn(site, self.remaining)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, CYCLE296_MATCHING_SITES)
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_011_SITES)
        self.assertEqual(len(self.without), STANDING_N_REMAINING_AFTER_011)
        for site in self.share_020:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE289_MATCHING_SITES)
        for site in self.share_087:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE293_MATCHING_SITES)
        for site in self.share_057:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE295_MATCHING_SITES)
            self.assertIn(site, CYCLE258_EXTRA_I_057)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in CYCLE247_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        for site in CYCLE248_LEFTOVER_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(
            matching_leftover_n4_remaining_remaining_after_057_local_4gram_rows(),
            matching_leftover_n4_remaining_remaining_after_057_local_4gram_rows(
                STANDING_MATCHING_SITES,
                STANDING_MATCHING_NEXT_4GRAMS,
            ),
        )
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_011)
        self.assertTrue(STANDING_I_ONLY_OF_LEFTOVER_N4_REMAINING_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_cycle248_extra_i_011_equals_matching_011(self):
        """Cycle 248 extra I 090-starts equal leftover n=4 remaining remaining-after-057 011."""
        self.assertEqual(CYCLE248_N_EXTRA, 2)
        self.assertEqual(CYCLE248_EXTRA_I_SITES, STANDING_MATCHING_SITES)
        self.assertEqual(
            CYCLE248_EXTRA_I_SITES,
            (
                (SIDE_IA, "Ia2", 107),
                (SIDE_IA, "Ia14", 54),
            ),
        )
        self.assertTrue(matching_equals_cycle248_extra_i(self.matching))
        self.assertTrue(self.equals_cycle248)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I)
        self.assertEqual(self.matching, CYCLE248_EXTRA_I_SITES)
        for site in self.matching:
            self.assertIn(site, CYCLE248_I_SITES)
            self.assertIn(site, CYCLE248_EXTRA_I_SITES)
        leftover_extra_011 = tuple(
            site for site in CYCLE248_I_SITES if site not in CYCLE248_EXTRA_I_SITES
        )
        self.assertEqual(leftover_extra_011, CYCLE247_MATCHING_SITES)
        for site in leftover_extra_011:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        overlap = tuple(site for site in self.matching if site in CYCLE248_EXTRA_I_SITES)
        self.assertEqual(overlap, STANDING_MATCHING_SITES)
        self.assertTrue(STANDING_EXTRA_I_MISMATCH_DOES_NOT_LOSE)
        prior_248 = self.survey["i_3gram_090_076_011_i_only"]
        self.assertEqual(prior_248["cycle"], 248)
        self.assertEqual(prior_248["N_I"], 4)
        self.assertEqual(prior_248["N_off_I"], 0)
        self.assertEqual(prior_248["N_extra"], 2)
        extra_248 = tuple(tuple(row) for row in prior_248["extra_i_sites"])
        self.assertEqual(extra_248, CYCLE248_EXTRA_I_SITES)
        self.assertEqual(extra_248, self.matching)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_296_295_294_248_247_224_223_still_compute(self):
        """Cycle 296 011/2/4/3, 295 K_057=2, 294 unique-max false, 248 4/0 extra I=2, 247 leftover extra 011, 224 13/56, 223 69/3 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_296 = TestMamariILeftoverN4Remaining090076RemainingAfter057NextStemScoreboard()
        prior_296.setUp()
        prior_296.test_counts_4_remaining_g_011_k_2_and_hypothesis_holds()
        prior_296.test_survey_matches_computed_lock()
        self.assertEqual(prior_296.g, "011")
        self.assertEqual(prior_296.k, 2)
        self.assertEqual(prior_296.n_remaining, 4)
        self.assertEqual(prior_296.n_distinct, 3)
        self.assertTrue(prior_296.unique)
        self.assertTrue(prior_296.claim_holds)
        self.assertTrue(CYCLE296_CLAIM)
        self.assertEqual(CYCLE296_G, "011")
        self.assertEqual(CYCLE296_K, 2)
        self.assertEqual(CYCLE296_N_REMAINING, 4)
        self.assertEqual(CYCLE296_N_DISTINCT, 3)
        if (
            prior_296.g != "011"
            or prior_296.k != 2
            or prior_296.n_remaining != 4
            or prior_296.n_distinct != 3
            or not prior_296.unique
            or not prior_296.claim_holds
        ):
            self.fail(
                "nested cycle 296 unique-max G=011 K=2 N_remaining=4 distinct=3 drifted"
            )
        prior_295 = TestMamariILeftoverN4Remaining090076RemainingAfter087Forward057Scoreboard()
        prior_295.setUp()
        prior_295.test_counts_2_of_6_and_hypothesis_k_2_holds()
        prior_295.test_survey_matches_computed_lock()
        self.assertEqual(prior_295.k_057, 2)
        self.assertEqual(prior_295.n_remaining_after_057, 4)
        self.assertEqual(prior_295.matching, CYCLE295_MATCHING_SITES)
        self.assertEqual(self.share_057, prior_295.matching)
        self.assertEqual(self.remaining, prior_295.without)
        self.assertTrue(prior_295.equals_cycle258)
        self.assertTrue(prior_295.claim_holds)
        self.assertTrue(CYCLE295_CLAIM)
        if (
            prior_295.k_057 != 2
            or prior_295.n_remaining_after_057 != 4
            or not prior_295.equals_cycle258
        ):
            self.fail(
                "nested cycle 295 leftover n=4 remaining remaining-after-087 exactly 2 share 057 / N_remaining=4 drifted"
            )
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
        prior_247 = TestMamariILeftoverExtra090076RemainingAfter087Fwd011Scoreboard()
        prior_247.setUp()
        prior_247.test_counts_2_of_29_and_hypothesis_k_2_holds()
        prior_247.test_survey_matches_computed_lock()
        self.assertEqual(prior_247.k, 2)
        self.assertEqual(prior_247.matching, CYCLE247_MATCHING_SITES)
        self.assertTrue(prior_247.claim_holds)
        self.assertTrue(CYCLE247_CLAIM)
        if prior_247.k != 2 or not prior_247.claim_holds:
            self.fail("nested cycle 247 leftover extra remaining-after-087 exactly 2 share 011 drifted")
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
        unused_293 = CYCLE293_EQUALS_245
        self.assertTrue(unused_293)
        unused_295_eq = CYCLE295_EQUALS_258
        self.assertTrue(unused_295_eq)
        unused_296_eq = CYCLE296_EQUALS_248
        self.assertTrue(unused_296_eq)
        unused_258 = matching_equals_cycle258_extra_i_057
        self.assertTrue(callable(unused_258))
        unused_020_with = leftover_n4_remaining_remaining_after_020_with_next
        unused_020_without = leftover_n4_remaining_remaining_after_020_without_next
        unused_020_stems = leftover_n4_remaining_remaining_after_020_next_stems
        unused_087_with = leftover_n4_remaining_remaining_after_087_with_next
        unused_087_without = leftover_n4_remaining_remaining_after_087_without_next
        unused_087_stems = leftover_n4_remaining_remaining_after_087_next_stems
        unused_without_020 = leftover_n4_remaining_without_forward_020
        unused_without_087 = leftover_n4_remaining_remaining_after_020_without_forward_087
        unused_counts = remaining_after_057_next_stem_counts
        unused_289_rem = CYCLE289_REMAINING_AFTER_020_SITES
        unused_292_match = CYCLE292_MATCHING_SITES
        unused_293_rem = CYCLE293_REMAINING_AFTER_087_SITES
        unused_294_sites = CYCLE294_REMAINING_SITES
        unused_293_n020 = CYCLE293_N_REMAINING_AFTER_020
        unused_292_sites = CYCLE292_REMAINING_SITES
        self.assertTrue(callable(unused_020_with))
        self.assertTrue(callable(unused_020_without))
        self.assertTrue(callable(unused_020_stems))
        self.assertTrue(callable(unused_087_with))
        self.assertTrue(callable(unused_087_without))
        self.assertTrue(callable(unused_087_stems))
        self.assertTrue(callable(unused_without_020))
        self.assertTrue(callable(unused_without_087))
        self.assertTrue(callable(unused_counts))
        self.assertEqual(len(unused_289_rem), 9)
        self.assertEqual(len(unused_292_match), 3)
        self.assertEqual(len(unused_293_rem), 6)
        self.assertEqual(len(unused_294_sites), 6)
        self.assertEqual(unused_293_n020, 9)
        self.assertEqual(len(unused_292_sites), 9)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_011)
        self.assertTrue(STANDING_CYCLE167_268_296_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-297 leftover n=4 remaining remaining-after-057 011 lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_forward_011"]
        self.assertEqual(lock["cycle"], 297)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(tuple(lock["forward_3gram"]), ("090", "076", "011"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(tuple(lock["locked_forward_stems"]), ("020", "087", "057"))
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
        self.assertEqual(lock["K_057"], STANDING_K_057)
        self.assertEqual(lock["K_057"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_057_sites"]),
            CYCLE295_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_057"], STANDING_N_REMAINING_AFTER_057)
        self.assertEqual(lock["N_remaining_after_057"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_057_sites"]),
            CYCLE296_REMAINING_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 4)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 0)
        self.assertEqual(lock["no_next_sites"], [])
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 3)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 2)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "011")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertEqual(lock["K_011"], STANDING_K_011)
        self.assertEqual(lock["K_011"], 2)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 2)
        self.assertEqual(lock["N_remaining_after_011"], STANDING_N_REMAINING_AFTER_011)
        self.assertEqual(lock["N_remaining_after_011"], 2)
        self.assertTrue(lock["G_uniquely_most_frequent"])
        self.assertTrue(lock["unique_max_still_011"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_remaining_after_057_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_remaining_after_057_sites"]),
            CYCLE296_MATCHING_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle296_g_sites"])
        self.assertEqual(
            lock["matching_equals_cycle296_g_sites"],
            STANDING_MATCHING_EQUALS_CYCLE296_G_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle248_extra_i"])
        self.assertEqual(
            lock["matching_equals_cycle248_extra_i"],
            STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_remaining_after_057_local_4grams"],
            matching_leftover_n4_remaining_remaining_after_057_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_011_sites"]),
            STANDING_REMAINING_AFTER_011_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle296_G_sites"]),
            CYCLE296_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle248_extra_i_sites"]),
            CYCLE248_EXTRA_I_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["overlap_with_cycle248_extra_i"]),
            STANDING_MATCHING_SITES,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011"]
        )
        self.assertEqual(
            lock["i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011"],
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011,
        )
        self.assertEqual(lock["nested_cycle296_G"], "011")
        self.assertEqual(lock["nested_cycle296_K"], 2)
        self.assertEqual(lock["nested_cycle296_N_remaining_after_057"], 4)
        self.assertEqual(lock["nested_cycle296_N_distinct"], 3)
        self.assertTrue(lock["nested_cycle296_unique_next_stem"])
        self.assertEqual(lock["nested_cycle295_K_057"], 2)
        self.assertEqual(lock["nested_cycle295_N_remaining_after_057"], 4)
        self.assertTrue(lock["nested_cycle295_extra_i_overlap"])
        self.assertEqual(lock["nested_cycle294_G"], "057")
        self.assertEqual(lock["nested_cycle294_K"], 2)
        self.assertEqual(lock["nested_cycle294_N_remaining_after_087"], 6)
        self.assertEqual(lock["nested_cycle294_N_distinct"], 4)
        self.assertFalse(lock["nested_cycle294_unique_next_stem"])
        self.assertEqual(lock["nested_cycle294_N_tied_at_K"], 2)
        self.assertEqual(tuple(lock["nested_cycle294_tied_stems"]), ("057", "011"))
        self.assertEqual(lock["nested_cycle293_K_087"], 3)
        self.assertEqual(lock["nested_cycle293_N_remaining_after_087"], 6)
        self.assertTrue(lock["nested_cycle293_extra_i_overlap"])
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
        self.assertEqual(lock["nested_cycle248_N_I"], 4)
        self.assertEqual(lock["nested_cycle248_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle248_N_extra"], 2)
        self.assertTrue(lock["nested_cycle248_i_only"])
        self.assertEqual(lock["nested_cycle247_K"], 2)
        self.assertTrue(lock["nested_cycle247_exactly_2_share_011"])
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle235_K"], 2)
        self.assertTrue(lock["nested_cycle235_exactly_2_share_700"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle235"])
        self.assertFalse(lock["same_as_cycle247"])
        self.assertFalse(lock["same_as_cycle248"])
        self.assertFalse(lock["same_as_cycle293"])
        self.assertFalse(lock["same_as_cycle295"])
        self.assertFalse(lock["same_as_cycle296"])
        self.assertTrue(lock["same_claim_shape_as_cycle235"])
        self.assertTrue(lock["same_claim_shape_as_cycle293"])
        self.assertTrue(lock["same_claim_shape_as_cycle295"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_leftover_n4_remaining_090_076_011_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_remaining_after_011"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_011_not_locked"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["cycle167_268_296_not_overwritten"])
        self.assertTrue(lock["extra_i_mismatch_does_not_lose"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_057_next_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_087_forward_057_unchanged"]
        )
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
        self.assertTrue(lock["standing_i_3gram_090_076_011_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_087_fwd011_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_fwd700_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"]["cycle"],
            296,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"]["G"],
            "011",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"]["K"],
            2,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"][
                "i_leftover_n4_remaining_090_076_remaining_after_057_unique_next_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_forward_057"]["cycle"],
            295,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_forward_057"]["K_057"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]["cycle"],
            294,
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
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["cycle"], 248)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_I"], 4)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_extra"], 2)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_087_fwd011"]["cycle"],
            247,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_087_fwd011"]["K"],
            2,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_087_fwd011"][
                "i_leftover_extra_090_076_remaining_after_087_exactly_2_share_011"
            ]
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


class TestMamariILeftoverN4Remaining090076RemainingAfter057Forward011ImageSnapshot(
    unittest.TestCase
):
    """Cycle 297 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
