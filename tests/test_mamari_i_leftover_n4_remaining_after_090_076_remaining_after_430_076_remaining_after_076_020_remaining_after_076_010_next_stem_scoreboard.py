"""I's leftover n=4 remaining remaining-after-090-076 remaining-after-430-076 remaining-after-076-020 remaining-after-076-010 leftover 4-gram next-stem lock.

Cycle 343 text-search lock. Uses already-vendored A–V and the
cycle-340 leftover n=4 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 remaining-
after-076-010 leftover matching sites of the five leftover
4-grams (N=11). Does not retune leftover 4-gram I-only
(cycle 340 extra I=0), leftover 3-gram I-only (cycle 341
extra I=5), extra-I 4-gram I-only (cycle 342 hapax 10/0),
cycle 339 unique-max 2-gram, cycle 338 leftover 4-gram
I-only, cycle 337 2-gram 076 010 I-only LOSE, cycle 336
exactly-K, cycle 335 unique-max, cycle 334 2-gram 076 020
I-only, cycle 333 exactly-2-share, cycle 332 unique-max,
cycle 331 leftover 4-gram I-only, cycle 330 2-gram 430 076
I-only, cycle 329 exactly-2-share, cycle 328 unique-max,
cycle 222, leftover n=4 remaining I 090 076 peels (288–327),
leftover extra 090 076 peels, or cycles 220–221 / 223. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Population (locked, do not re-derive as a new claim): leftover
n=4 remaining remaining-after-090-076 N=11 leftover 4-grams
that do not contain 090 076. Cycle 328–338 remaining-after-
090-076 2-gram peels stay nested (430 076 / 076 020 /
076 010). Cycle 339 LOSE unique most frequent 2-gram among
remaining-after-076-010 (N=5 leftover 4-grams: 028 076 011 076,
071 999 604 076, 202 076 006 055, 076 999 029 076,
700 076 076 053). unique_max false, hapax pile (15-way tie
at K=1). G=999 604 largest-id labeling only. Cycle 340 HOLD:
those five leftover 4-grams are all I-only (extra I of the
4-grams=0, leftover matching sites=11, N_not_hapax=5). Extra-I
peel of leftover 4-grams is closed. Cycle 341 HOLD:
contiguous 3-grams of those five leftover 4-grams are all
I-only (N_i_only=10 N_leak=0 extra I of the 3-grams=5). Extra
I sites: 076 011 076 extra I=2 at Ia2[56]/Ia13[12];
999 604 076 extra I=3 at Ia2[132]/Ia5[82]/Ia7[77]. Cycle 342
HOLD: extra-I 4-grams of leftover 3-grams with extra I are
all I-only (10 hapax 1/0 at those five extra I 3-gram sites,
prev and next each). Extra-I peel of leftover 3-grams is
closed. Nested cycle 341 leftover 3-gram I-only extra I=5
stays nested. Nested cycle 340 leftover 4-gram I-only extra
I=0 stays nested. This cycle's population is leftover
matching sites of the five leftover 4-grams (11 sites). Next
stem = the token immediately after each leftover 4-gram. Do
not re-lock leftover 4-gram I-only, leftover 3-gram I-only,
extra-I 4-gram I-only, or unique most frequent 2-gram inside
leftover 4-grams.

Already locked (record overlap only, do not re-lock): nested
cycle 342 extra-I 4-gram I-only HOLD hapax 10/0 stays nested.
Cycle 341 leftover 3-gram I-only HOLD extra I=5 stays nested.
Cycle 340 leftover 4-gram I-only HOLD extra I=0 stays nested.
Cycle 339, 338, 337, 336, 335, 334, 333, 332, 331, 330, 329,
328, 222, leftover n=4 remaining I 090 076 peels (288–327),
leftover extra 090 076 peels, cycles 220–221, cycle 223.

Same claim-shape as cycle 288 leftover n=4 remaining I
090 076 unique next stem LOSE (6 distinct, G=020 K=4). Also
analog cycle 292 leftover n=4 remaining remaining-after-020
unique next stem HOLD (G=087 K=3). Also analog cycle 298
leftover n=4 remaining remaining-after-011 unique next stem
LOSE (hapax pile G=607 K=1). Do not claim leftover 5-grams
I-only or exactly-K-share this cycle.

HOLD iff unique_max (one next stem strictly outcounts every
other among those 11 leftover matching sites). LOSE on a
tie (unique_max false), including a hapax pile. G is
largest-id labeling only on a tie; do not treat labeled G
as unique-max. Empty remainder would not lose HOLD.

Claim that can lose:
i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem.
True iff leftover matching sites still compute as those 11
and one next stem strictly outcounts every other among
sites that have a next token, or N_with_next==0. This can
lose the same way cycle 298 lost (hapax pile) and cycle 288
lost share-one (6 distinct). Measured: N=11, N_with_next=11,
N_no_next=0, N_distinct=11, hapax pile 11-way tie at K=1,
G=760 by largest-id labeling only, unique-max false. Matching
site of labeled G: Ia12[119] (202 076 006 055 then 760).
N_without_G=10. Nested cycle 342 extra-I 4-grams I-only
hapax 10/0, cycle 341 leftover 3-grams I-only extra I=5,
cycle 340 leftover 4-grams I-only extra I=0 leftover
matching sites 11, and cycle 339 unique_max false hapax
pile stay nested. The claim is false. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_076_010_i_only_scoreboard import (
    GRAM2 as CYCLE337_GRAM2,
    STANDING_I_2GRAM_076_010_I_ONLY as CYCLE337_CLAIM,
    STANDING_N_EXTRA as CYCLE337_N_EXTRA,
    STANDING_N_I as CYCLE337_N_I,
    STANDING_N_OFF_I as CYCLE337_N_OFF_I,
    TestMamariI2gram076010IOnlyScoreboard,
    i_2gram_076_010_i_only,
)
from tests.test_mamari_i_2gram_076_020_i_only_scoreboard import (
    GRAM2 as CYCLE334_GRAM2,
    STANDING_I_2GRAM_076_020_I_ONLY as CYCLE334_CLAIM,
    STANDING_N_EXTRA as CYCLE334_N_EXTRA,
    STANDING_N_I as CYCLE334_N_I,
    STANDING_N_OFF_I as CYCLE334_N_OFF_I,
    TestMamariI2gram076020IOnlyScoreboard,
    i_2gram_076_020_i_only,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2 as CYCLE223_GRAM2,
    STANDING_I_2GRAM_090_076_I_ONLY as CYCLE223_CLAIM,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
    i_2gram_090_076_i_only,
)
from tests.test_mamari_i_2gram_430_076_i_only_scoreboard import (
    GRAM2 as CYCLE330_GRAM2,
    STANDING_I_2GRAM_430_076_I_ONLY as CYCLE330_CLAIM,
    STANDING_N_EXTRA as CYCLE330_N_EXTRA,
    STANDING_N_I as CYCLE330_N_I,
    STANDING_N_OFF_I as CYCLE330_N_OFF_I,
    TestMamariI2gram430076IOnlyScoreboard,
    i_2gram_430_076_i_only,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    leftover_sites_with_next,
    leftover_sites_without_next,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_DISTINCT_REMAINING11 as CYCLE256_N_DISTINCT,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    barthel_id,
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
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_next_stem_scoreboard import (
    STANDING_G as CYCLE298_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE298_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_UNIQUE_NEXT_STEM as CYCLE298_CLAIM,
    STANDING_K as CYCLE298_K,
    STANDING_N_DISTINCT as CYCLE298_N_DISTINCT,
    STANDING_N_HAPAX as CYCLE298_N_HAPAX,
    STANDING_N_REMAINING_AFTER_011 as CYCLE298_N_REMAINING,
    TestMamariILeftoverN4Remaining090076RemainingAfter011NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_scoreboard import (
    STANDING_G as CYCLE292_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE292_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_UNIQUE_NEXT_STEM as CYCLE292_CLAIM,
    STANDING_K as CYCLE292_K,
    STANDING_N_DISTINCT as CYCLE292_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_020 as CYCLE292_N_REMAINING,
    TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_076_010_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_076_010_4GRAMS_ALL_I_ONLY as CYCLE338_CLAIM,
    STANDING_N_EXTRA as CYCLE338_N_EXTRA,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter0760200760104gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_3GRAMS_ALL_I_ONLY as CYCLE341_CLAIM,
    STANDING_N as CYCLE341_N,
    STANDING_N_EXTRA as CYCLE341_N_EXTRA,
    STANDING_N_I_EACH as CYCLE341_N_I_EACH,
    STANDING_N_I_ONLY as CYCLE341_N_I_ONLY,
    STANDING_N_LEAK as CYCLE341_N_LEAK,
    STANDING_N_OFF_I_EACH as CYCLE341_N_OFF_I_EACH,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760103gramsIOnlyScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_all_i_only,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only_scoreboard import (
    GRAM4_028,
    GRAM4_071,
    GRAM4_076,
    GRAM4_202,
    GRAM4_700,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_4GRAMS_ALL_I_ONLY as CYCLE340_CLAIM,
    STANDING_LEFTOVER_MATCHING_4GRAMS as CYCLE340_MATCHING_4GRAMS,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE340_LEFTOVER_MATCHING,
    STANDING_N as CYCLE340_N,
    STANDING_N_EXTRA as CYCLE340_N_EXTRA,
    STANDING_N_I_EACH as CYCLE340_N_I_EACH,
    STANDING_N_I_ONLY as CYCLE340_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE340_N_NOT_HAPAX,
    STANDING_N_OFF_I_EACH as CYCLE340_N_OFF_I_EACH,
    STANDING_SEQUENCES as CYCLE340_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760104gramsIOnlyScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_all_i_only,
    leftover_matching_4gram_sites,
    leftover_remaining_grams,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_EXTRA_I_4GRAMS_ALL_I_ONLY as CYCLE342_CLAIM,
    STANDING_N as CYCLE342_N,
    STANDING_N_HAPAX_I_ONLY as CYCLE342_N_HAPAX,
    STANDING_N_I_ONLY as CYCLE342_N_I_ONLY,
    STANDING_N_LEAK as CYCLE342_N_LEAK,
    STANDING_SEQUENCES as CYCLE342_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraI4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2gram_scoreboard import (
    GRAM2 as CYCLE339_GRAM2,
    STANDING_G as CYCLE339_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE339_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_MAX_2GRAM as CYCLE339_UNIQUE_MAX_CLAIM,
    STANDING_K as CYCLE339_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE339_MATCHING,
    STANDING_N as CYCLE339_N,
    STANDING_N_DISTINCT as CYCLE339_N_DISTINCT,
    STANDING_N_REMAINING as CYCLE339_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE339_N_TIED,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram,
    leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    STANDING_G as CYCLE222_G,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    TestMamariILeftoverN4RemainingNext2gramScoreboard,
    leftover_n4_family_counts_hold,
    leftover_n4_rows,
    leftover_remaining_n4,
    leftover_remaining_with_g,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    line_stems_for_site,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_UNIQUE_MAX = True
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_N_4GRAMS = 5
STANDING_N = 11
STANDING_LEFTOVER_MATCHING_SITES = CYCLE340_LEFTOVER_MATCHING
STANDING_LEFTOVER_MATCHING_4GRAMS = CYCLE340_MATCHING_4GRAMS
STANDING_NEXT_STEMS = (
    "295",
    "002",
    "071",
    "460",
    "000",
    "076",
    "760",
    "022",
    "048",
    "720",
    "177",
)
STANDING_N_WITH_NEXT = 11
STANDING_N_NO_NEXT = 0
STANDING_NO_NEXT_SITES = ()
STANDING_N_DISTINCT = 11
STANDING_N_HAPAX = 11
STANDING_G = "760"
STANDING_K = 1
STANDING_N_WITHOUT_G = 10
STANDING_N_TIED_AT_K = 11
STANDING_TIED_STEMS = (
    "760",
    "720",
    "460",
    "295",
    "177",
    "076",
    "071",
    "048",
    "022",
    "002",
    "000",
)
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_MATCHING_SITES = ((SIDE_IA, "Ia12", 119),)
STANDING_MATCHING_4GRAM = GRAM4_202
STANDING_MATCHING_NEXT_5GRAMS = (("202", "076", "006", "055", "760"),)
STANDING_WITHOUT_G_SITES = (
    (SIDE_IA, "Ia1", 136),
    (SIDE_IA, "Ia4", 125),
    (SIDE_IA, "Ia14", 78),
    (SIDE_IA, "Ia1", 63),
    (SIDE_IA, "Ia9", 3),
    (SIDE_IA, "Ia6", 48),
    (SIDE_IA, "Ia8", 30),
    (SIDE_IA, "Ia10", 144),
    (SIDE_IA, "Ia8", 167),
    (SIDE_IA, "Ia9", 32),
)
STANDING_FREQUENCY = (
    ("760", 1, ((SIDE_IA, "Ia12", 119),), (("202", "076", "006", "055", "760"),)),
    ("720", 1, ((SIDE_IA, "Ia8", 167),), (("700", "076", "076", "053", "720"),)),
    ("460", 1, ((SIDE_IA, "Ia1", 63),), (("071", "999", "604", "076", "460"),)),
    ("295", 1, ((SIDE_IA, "Ia1", 136),), (("028", "076", "011", "076", "295"),)),
    ("177", 1, ((SIDE_IA, "Ia9", 32),), (("700", "076", "076", "053", "177"),)),
    ("076", 1, ((SIDE_IA, "Ia6", 48),), (("202", "076", "006", "055", "076"),)),
    ("071", 1, ((SIDE_IA, "Ia14", 78),), (("028", "076", "011", "076", "071"),)),
    ("048", 1, ((SIDE_IA, "Ia10", 144),), (("076", "999", "029", "076", "048"),)),
    ("022", 1, ((SIDE_IA, "Ia8", 30),), (("076", "999", "029", "076", "022"),)),
    ("002", 1, ((SIDE_IA, "Ia4", 125),), (("028", "076", "011", "076", "002"),)),
    ("000", 1, ((SIDE_IA, "Ia9", 3),), (("071", "999", "604", "076", "000"),)),
)
NEAR_MISS_090_076 = CYCLE223_GRAM2
NEAR_MISS_430_076 = CYCLE330_GRAM2
NEAR_MISS_076_020 = CYCLE334_GRAM2
NEAR_MISS_076_010 = CYCLE337_GRAM2
NEAR_MISS_076_071 = CYCLE171_GRAM2
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem"
)
STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_NEXT_STEM = (
    False
)
STANDING_RESULT = (
    "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_stem"
)
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE222 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_AS_CYCLE288 = False
STANDING_SAME_AS_CYCLE292 = False
STANDING_SAME_AS_CYCLE298 = False
STANDING_SAME_AS_CYCLE339 = False
STANDING_SAME_AS_CYCLE340 = False
STANDING_SAME_AS_CYCLE341 = False
STANDING_SAME_AS_CYCLE342 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE288 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE298 = True
STANDING_LABELED_G_DOES_NOT_COUNT = True
STANDING_EMPTY_REMAINDER_DOES_NOT_LOSE = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_STEM = True
STANDING_DO_NOT_CLAIM_5GRAMS_I_ONLY = True
STANDING_DO_NOT_CLAIM_EXACTLY_K_SHARE = True
STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_3GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_EXTRA_I_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_UNIQUE_MAX_2GRAM_IS_NOT_THIS_CYCLE = True
STANDING_090_076_DOES_NOT_COUNT = True
STANDING_430_076_DOES_NOT_COUNT = True
STANDING_076_020_DOES_NOT_COUNT = True
STANDING_076_010_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_CYCLE342_DOES_NOT_COUNT = True
STANDING_CYCLE341_DOES_NOT_COUNT = True
STANDING_CYCLE340_DOES_NOT_COUNT = True
STANDING_CYCLE339_DOES_NOT_COUNT = True
STANDING_CYCLE338_DOES_NOT_COUNT = True
STANDING_CYCLE337_DOES_NOT_COUNT = True
STANDING_CYCLE336_DOES_NOT_COUNT = True
STANDING_CYCLE335_DOES_NOT_COUNT = True
STANDING_CYCLE334_DOES_NOT_COUNT = True
STANDING_CYCLE333_DOES_NOT_COUNT = True
STANDING_CYCLE332_DOES_NOT_COUNT = True
STANDING_CYCLE331_DOES_NOT_COUNT = True
STANDING_CYCLE330_DOES_NOT_COUNT = True
STANDING_CYCLE329_DOES_NOT_COUNT = True
STANDING_CYCLE328_DOES_NOT_COUNT = True
STANDING_CYCLE222_DOES_NOT_COUNT = True
STANDING_I_SITE_PEEL_288_327_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_PEELS_DO_NOT_COUNT = True
STANDING_CYCLES_220_221_DO_NOT_COUNT = True
STANDING_CYCLE223_DOES_NOT_COUNT = True
STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL = True


def site_next_stem_after_4gram(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...],
) -> str | None:
    """Next stem after leftover 4-gram; None at line-final or mismatch."""
    if tuple(stems[index : index + len(gram4)]) != gram4:
        return None
    next_index = index + len(gram4)
    if next_index >= len(stems):
        return None
    return stems[next_index]


def site_next_5gram_after_4gram(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...],
) -> tuple[str, ...] | None:
    """Leftover 4-gram plus next stem; None at line-final or mismatch."""
    nxt = site_next_stem_after_4gram(stems, index, gram4)
    if nxt is None:
        return None
    return gram4 + (nxt,)


def leftover_4gram_next_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    grams: tuple[tuple[str, ...], ...] = STANDING_LEFTOVER_MATCHING_4GRAMS,
) -> tuple[str | None, ...]:
    """Per-site next stem after each leftover matching 4-gram."""
    return tuple(
        site_next_stem_after_4gram(line_stems_for_site(i_sides, site), site[2], gram)
        for site, gram in zip(sites, grams, strict=True)
    )


def leftover_4gram_next_5grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    grams: tuple[tuple[str, ...], ...] = STANDING_LEFTOVER_MATCHING_4GRAMS,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site leftover 4-gram plus next stem."""
    return tuple(
        site_next_5gram_after_4gram(line_stems_for_site(i_sides, site), site[2], gram)
        for site, gram in zip(sites, grams, strict=True)
    )


def leftover_4gram_sites_with_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching 4-gram sites that have a next token."""
    return leftover_sites_with_next(sites, next_stems)


def leftover_4gram_sites_without_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching 4-gram sites that are line-final (no next token)."""
    return leftover_sites_without_next(sites, next_stems)


def leftover_4gram_with_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching 4-gram sites whose next token is G."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem
    )


def leftover_4gram_without_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching 4-gram sites whose next token is not G."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt != stem
    )


def leftover_4gram_next_stem_counts(next_stems: tuple[str, ...]) -> Counter:
    """Counts of next stems among leftover matching 4-gram sites with a next token."""
    return Counter(next_stems)


def rank_leftover_4gram_next_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Next stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_leftover_4gram_next_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remainder has no G."""
    ranked = rank_leftover_4gram_next_stems(
        leftover_4gram_next_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def leftover_4gram_next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    next_5grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Next-stem frequency: highest count first, then larger id."""
    with_next = leftover_4gram_sites_with_next(sites, next_stems)
    with_next_stems = tuple(nxt for nxt in next_stems if nxt is not None)
    with_next_5 = tuple(gram for gram in next_5grams if gram is not None)
    ranked = rank_leftover_4gram_next_stems(
        leftover_4gram_next_stem_counts(with_next_stems)
    )
    rows = []
    for stem, count in ranked:
        stem_sites = tuple(
            site
            for site, nxt in zip(with_next, with_next_stems, strict=True)
            if nxt == stem
        )
        stem_grams = tuple(
            gram
            for nxt, gram in zip(with_next_stems, with_next_5, strict=True)
            if nxt == stem
        )
        rows.append((stem, count, stem_sites, stem_grams))
    return tuple(rows)


def leftover_4gram_next_stem_frequency_rows(
    frequency: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_FREQUENCY,
) -> list[dict]:
    """Survey-shaped next-stem frequency rows."""
    return [
        {
            "next_stem": stem,
            "count": count,
            "leftover_matching_sites": [list(site) for site in sites],
            "next_5grams": [list(gram) for gram in grams],
        }
        for stem, count, sites, grams in frequency
    ]


def leftover_4gram_next_stem_nested_counts_hold(
    n_sites: int,
    n_with_next: int,
    n_no_next: int,
    expected_n: int = STANDING_N,
    expected_with_next: int = STANDING_N_WITH_NEXT,
    expected_no_next: int = STANDING_N_NO_NEXT,
) -> bool:
    """Nested leftover matching sites 11/11/0."""
    return (
        n_sites == expected_n
        and n_with_next == expected_with_next
        and n_no_next == expected_no_next
        and n_with_next + n_no_next == n_sites
    )


def i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    expected_n: int = STANDING_N,
) -> bool:
    """True iff leftover matching 4-grams have a unique most frequent next stem.

    Empty remainder (no next tokens) does not lose HOLD. A tie at max K,
    including a hapax pile, loses. Labeled G is not unique-max.
    """
    if len(sites) != expected_n or len(next_stems) != expected_n:
        return False
    with_next = tuple(nxt for nxt in next_stems if nxt is not None)
    if not with_next:
        return True
    _gram, _count, unique = select_leftover_4gram_next_g(with_next)
    return bool(unique)


class TestILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010NextStemHelpers(
    unittest.TestCase
):
    """Helpers on leftover remaining-after-076-010 4-gram next stems. No CV, no LLM."""

    def test_next_stem_is_token_immediately_after_leftover_4gram(self):
        """Next stem is index+4; mismatch or line-final is None."""
        provider = MockProvider()
        planted = ["028", "076", "011", "076", "295", "076"]
        self.assertEqual(
            site_next_stem_after_4gram(planted, 0, GRAM4_028),
            "295",
        )
        self.assertEqual(
            site_next_5gram_after_4gram(planted, 0, GRAM4_028),
            ("028", "076", "011", "076", "295"),
        )
        self.assertIsNone(site_next_stem_after_4gram(["028", "076", "011", "076"], 0, GRAM4_028))
        self.assertIsNone(site_next_5gram_after_4gram(["028", "076", "011", "076"], 0, GRAM4_028))
        mismatch = ["090", "076", "011", "076", "295"]
        self.assertIsNone(site_next_stem_after_4gram(mismatch, 0, GRAM4_028))
        self.assertNotEqual(NEAR_MISS_090_076, GRAM4_028[:2])
        self.assertFalse(
            any(
                pair == NEAR_MISS_090_076
                for gram in CYCLE340_SEQUENCES
                for pair in (gram[0:2], gram[1:3], gram[2:4])
            )
        )
        self.assertTrue(STANDING_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_430_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_020_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_010_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_3GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_EXTRA_I_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_UNIQUE_MAX_2GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_CLAIM_5GRAMS_I_ONLY)
        self.assertTrue(STANDING_DO_NOT_CLAIM_EXACTLY_K_SHARE)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_can_fail_and_empty_remainder_holds(self):
        """Boolean is True only on unique-max or empty remainder. Hapax pile loses."""
        provider = MockProvider()
        sites = STANDING_LEFTOVER_MATCHING_SITES
        stems = STANDING_NEXT_STEMS
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem(
                sites,
                stems,
            )
        )
        g, k, unique = select_leftover_4gram_next_g(stems)
        self.assertEqual(g, "760")
        self.assertEqual(k, 1)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_NEXT_STEM
        )
        empty = (None,) * STANDING_N
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem(
                sites,
                empty,
            )
        )
        self.assertEqual(select_leftover_4gram_next_g(()), (None, 0, False))
        self.assertTrue(STANDING_EMPTY_REMAINDER_DOES_NOT_LOSE)
        all_one = ("760",) * STANDING_N
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem(
                sites,
                all_one,
            )
        )
        hold_g, hold_k, hold_unique = select_leftover_4gram_next_g(all_one)
        self.assertEqual(hold_g, "760")
        self.assertEqual(hold_k, 11)
        self.assertTrue(hold_unique)
        two_way = ("760",) * 5 + ("720",) * 5 + ("000",)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem(
                sites,
                two_way,
            )
        )
        tie_g, tie_k, tie_unique = select_leftover_4gram_next_g(("760", "720", "760", "720"))
        self.assertEqual(tie_g, "760")
        self.assertEqual(tie_k, 2)
        self.assertFalse(tie_unique)
        drifted = sites[:-1]
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem(
                drifted,
                stems[:-1],
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem",
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N)
        self.assertEqual(1 + 10, 11)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_STEM)
        self.assertTrue(STANDING_LABELED_G_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal leftover-4-gram next counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"760": 1, "720": 1, "000": 1})
        ranked = rank_leftover_4gram_next_stems(counts)
        self.assertEqual(ranked[0], ("760", 1))
        self.assertEqual(ranked[1], ("720", 1))
        self.assertEqual(ranked[-1], ("000", 1))
        self.assertEqual(select_leftover_4gram_next_g(("720", "760"))[0], "760")
        self.assertFalse(select_leftover_4gram_next_g(("720", "760"))[2])
        self.assertEqual(select_leftover_4gram_next_g(("760", "760", "720"))[0], "760")
        self.assertTrue(select_leftover_4gram_next_g(("760", "760", "720"))[2])
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE288)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE298)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE288)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE298)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertFalse(CYCLE298_UNIQUE)
        self.assertFalse(CYCLE298_CLAIM)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertFalse(CYCLE256_CLAIM)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010NextStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture remaining-after-076-010 leftover 4-gram next-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.remaining_after = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
            self.leftover
        )
        self.remaining_4grams = leftover_remaining_grams(self.leftover)
        self.sites = leftover_matching_4gram_sites(self.remaining_after)
        self.next_stems = leftover_4gram_next_stems(
            self.i_sides,
            self.sites,
            STANDING_LEFTOVER_MATCHING_4GRAMS,
        )
        self.next_5grams = leftover_4gram_next_5grams(
            self.i_sides,
            self.sites,
            STANDING_LEFTOVER_MATCHING_4GRAMS,
        )
        self.with_next = leftover_4gram_sites_with_next(self.sites, self.next_stems)
        self.no_next = leftover_4gram_sites_without_next(self.sites, self.next_stems)
        self.matching = leftover_4gram_with_g(self.sites, self.next_stems)
        self.without = leftover_4gram_without_g(self.sites, self.next_stems)
        self.frequency = leftover_4gram_next_stem_frequency_table(
            self.sites,
            self.next_stems,
            self.next_5grams,
        )
        self.n_sites = len(self.sites)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.n_distinct = len(self.frequency)
        self.g, self.k, self.unique = select_leftover_4gram_next_g(
            tuple(nxt for nxt in self.next_stems if nxt is not None)
        )
        self.n_without = len(self.without)
        self.claim_holds = i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem(
            self.sites,
            self.next_stems,
        )

    def test_tokens_are_cycle_340_leftover_matching_sites_not_retuned(self):
        """Five leftover 4-grams and 11 leftover matching sites stay the cycle-340 lock."""
        self.assertEqual(self.remaining_4grams, CYCLE340_SEQUENCES)
        self.assertEqual(
            self.remaining_4grams,
            (GRAM4_028, GRAM4_071, GRAM4_202, GRAM4_076, GRAM4_700),
        )
        self.assertEqual(len(self.remaining_4grams), STANDING_N_4GRAMS)
        self.assertEqual(STANDING_N_4GRAMS, CYCLE340_N)
        self.assertEqual(STANDING_N_4GRAMS, 5)
        self.assertEqual(self.sites, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(self.sites, CYCLE340_LEFTOVER_MATCHING)
        self.assertEqual(len(self.sites), STANDING_N)
        self.assertEqual(STANDING_N, 11)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_4GRAMS, CYCLE340_MATCHING_4GRAMS)
        for site, gram in zip(self.sites, STANDING_LEFTOVER_MATCHING_4GRAMS, strict=True):
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N4]), gram)
            self.assertEqual(len(gram), STANDING_N4)
            self.assertNotIn(NEAR_MISS_090_076, (gram[0:2], gram[1:3], gram[2:4]))
            self.assertNotIn(NEAR_MISS_430_076, (gram[0:2], gram[1:3], gram[2:4]))
            self.assertNotIn(NEAR_MISS_076_020, (gram[0:2], gram[1:3], gram[2:4]))
            self.assertNotIn(NEAR_MISS_076_010, (gram[0:2], gram[1:3], gram[2:4]))
        self.assertTrue(leftover_n4_family_counts_hold(self.leftover))
        self.assertEqual(len(leftover_remaining_n4(self.leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(self.leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(self.leftover))), 5)
        self.assertEqual(len(self.remaining_after), 5)
        self.assertTrue(CYCLE340_CLAIM)
        self.assertEqual(CYCLE340_N_EXTRA, 0)
        self.assertEqual(CYCLE340_N_I_ONLY, 5)
        self.assertEqual(CYCLE340_N_NOT_HAPAX, 5)
        self.assertEqual(CYCLE340_N_I_EACH, (3, 2, 2, 2, 2))
        self.assertEqual(CYCLE340_N_OFF_I_EACH, (0, 0, 0, 0, 0))
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_all_i_only(
                (3, 2, 2, 2, 2), (0, 0, 0, 0, 0)
            )
        )
        self.assertTrue(STANDING_CYCLE340_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_11_sites_hapax_pile_g_760_k_1_and_hypothesis_loses(self):
        """N=11, N_with_next=11, N_distinct=11, G=760 K=1 unique-max false. Claim loses."""
        self.assertEqual(self.n_sites, STANDING_N)
        self.assertEqual(STANDING_N, 11)
        self.assertEqual(self.next_stems, STANDING_NEXT_STEMS)
        self.assertTrue(
            leftover_4gram_next_stem_nested_counts_hold(
                self.n_sites,
                self.n_with_next,
                self.n_no_next,
            )
        )
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 11)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 0)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ())
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_sites)
        self.assertEqual(11 + 0, 11)
        self.assertEqual(self.with_next, self.sites)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT)
        self.assertEqual(STANDING_N_DISTINCT, 11)
        self.assertEqual(self.frequency, STANDING_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "760")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 1)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "760")
        self.assertEqual(self.frequency[0][1], 1)
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 11)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX)
        self.assertEqual(STANDING_N_HAPAX, 11)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 10)
        self.assertEqual(self.k + self.n_without, self.n_sites)
        self.assertEqual(1 + 10, 11)
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.without, STANDING_WITHOUT_G_SITES)
        self.assertFalse(self.claim_holds)
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_NEXT_STEM,
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_NEXT_STEM
        )
        self.assertNotEqual(self.claim_holds, HYPOTHESIS_UNIQUE_MAX)
        self.assertTrue(STANDING_LABELED_G_DOES_NOT_COUNT)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_STEM)
        self.assertTrue(STANDING_DO_NOT_CLAIM_5GRAMS_I_ONLY)
        self.assertTrue(STANDING_DO_NOT_CLAIM_EXACTLY_K_SHARE)
        self.assertTrue(STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE288)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE298)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE288)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE298)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_INSIDE, 13)
        self.assertEqual(CYCLE288_N_WITH_NEXT, 13)
        self.assertEqual(CYCLE288_N_NO_NEXT, 0)
        self.assertEqual(CYCLE292_G, "087")
        self.assertEqual(CYCLE292_K, 3)
        self.assertEqual(CYCLE292_N_REMAINING, 9)
        self.assertEqual(CYCLE292_N_DISTINCT, 5)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertEqual(CYCLE298_G, "607")
        self.assertEqual(CYCLE298_K, 1)
        self.assertEqual(CYCLE298_N_REMAINING, 2)
        self.assertEqual(CYCLE298_N_DISTINCT, 2)
        self.assertEqual(CYCLE298_N_HAPAX, 2)
        self.assertFalse(CYCLE298_UNIQUE)
        self.assertFalse(CYCLE298_CLAIM)
        self.assertEqual(CYCLE256_G, "755")
        self.assertEqual(CYCLE256_K, 1)
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE256_N_DISTINCT, 19)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_labeled_g_is_ia12_760_labeling_only(self):
        """Labeled G=760 is Ia12[119] after 202 076 006 055. Labeling only."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(STANDING_MATCHING_SITES, ((SIDE_IA, "Ia12", 119),))
        self.assertEqual(STANDING_MATCHING_4GRAM, GRAM4_202)
        matching_5 = leftover_4gram_next_5grams(
            self.i_sides,
            self.matching,
            (STANDING_MATCHING_4GRAM,),
        )
        self.assertEqual(matching_5, STANDING_MATCHING_NEXT_5GRAMS)
        self.assertEqual(STANDING_MATCHING_NEXT_5GRAMS, (("202", "076", "006", "055", "760"),))
        site = self.matching[0]
        stems = line_stems_for_site(self.i_sides, site)
        index = site[2]
        self.assertEqual(tuple(stems[index : index + STANDING_N4]), GRAM4_202)
        self.assertEqual(site_next_stem_after_4gram(stems, index, GRAM4_202), "760")
        self.assertEqual(
            site_next_5gram_after_4gram(stems, index, GRAM4_202),
            ("202", "076", "006", "055", "760"),
        )
        self.assertEqual(stems[index + STANDING_N4], "760")
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            gram = STANDING_LEFTOVER_MATCHING_4GRAMS[self.sites.index(site)]
            nxt = site_next_stem_after_4gram(stems, site[2], gram)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "760")
            self.assertIn(site, STANDING_WITHOUT_G_SITES)
        self.assertNotIn(STANDING_MATCHING_SITES[0], self.without)
        self.assertTrue(STANDING_LABELED_G_DOES_NOT_COUNT)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_STEM)
        self.assertTrue(STANDING_DO_NOT_CLAIM_EXACTLY_K_SHARE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_cycle342_341_340_339_still_hold_and_are_not_relocked(self):
        """Extra-I 4-grams / leftover 3-grams / leftover 4-grams / unique-max 2-gram stay."""
        self.assertTrue(CYCLE342_CLAIM)
        self.assertEqual(CYCLE342_N, 10)
        self.assertEqual(CYCLE342_N_I_ONLY, 10)
        self.assertEqual(CYCLE342_N_HAPAX, 10)
        self.assertEqual(CYCLE342_N_LEAK, 0)
        self.assertEqual(len(CYCLE342_SEQUENCES), 10)
        self.assertTrue(CYCLE341_CLAIM)
        self.assertEqual(CYCLE341_N_I_EACH, (3, 5, 2, 5, 2, 2, 2, 2, 2, 2))
        self.assertEqual(CYCLE341_N_OFF_I_EACH, (0,) * 10)
        self.assertEqual(CYCLE341_N_EXTRA, 5)
        self.assertEqual(CYCLE341_N_I_ONLY, 10)
        self.assertEqual(CYCLE341_N_LEAK, 0)
        self.assertEqual(CYCLE341_N, 10)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_all_i_only(
                CYCLE341_N_I_EACH, CYCLE341_N_OFF_I_EACH
            )
        )
        self.assertTrue(CYCLE340_CLAIM)
        self.assertEqual(CYCLE340_N_I_EACH, (3, 2, 2, 2, 2))
        self.assertEqual(CYCLE340_N_OFF_I_EACH, (0, 0, 0, 0, 0))
        self.assertEqual(CYCLE340_N_EXTRA, 0)
        self.assertEqual(CYCLE340_N_I_ONLY, 5)
        self.assertEqual(CYCLE340_N_NOT_HAPAX, 5)
        self.assertEqual(len(CYCLE340_LEFTOVER_MATCHING), 11)
        self.assertFalse(CYCLE339_UNIQUE)
        self.assertFalse(CYCLE339_UNIQUE_MAX_CLAIM)
        self.assertEqual(CYCLE339_K, 1)
        self.assertEqual(CYCLE339_N, 5)
        self.assertEqual(CYCLE339_N_REMAINING, 4)
        self.assertEqual(CYCLE339_N_TIED, 15)
        self.assertEqual(CYCLE339_N_DISTINCT, 15)
        self.assertEqual(CYCLE339_G, ("999", "604"))
        self.assertEqual(CYCLE339_MATCHING, (GRAM4_071,))
        self.assertTrue(STANDING_CYCLE342_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE341_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE340_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE339_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_3GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_EXTRA_I_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_UNIQUE_MAX_2GRAM_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_342_341_340_339_337_298_292_288_223_and_222_scoreboards_still_compute(self):
        """Cycle 342 hapax 10/0, 341 10/0 extra I=5, 340 5/0, 298/292/288 next-stem stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, CYCLE223_GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(CYCLE222_CLAIM)
        prior_342 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraI4gramsIOnlyScoreboard()
        )
        prior_342.setUp()
        prior_342.test_each_extra_i_4gram_is_i_only_hapax_and_claim_holds()
        prior_342.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE342_CLAIM)
        self.assertEqual(CYCLE342_N_I_ONLY, 10)
        self.assertEqual(CYCLE342_N_HAPAX, 10)
        self.assertEqual(CYCLE342_N_LEAK, 0)
        if not prior_342.claim_holds:
            self.fail("nested cycle 342 leftover remaining-after-076-010 extra-I 4-grams all I-only drifted")
        prior_341 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760103gramsIOnlyScoreboard()
        )
        prior_341.setUp()
        prior_341.test_each_3gram_is_i_only_extra_five_and_claim_holds()
        prior_341.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE341_CLAIM)
        self.assertEqual(CYCLE341_N_I_ONLY, 10)
        self.assertEqual(CYCLE341_N_EXTRA, 5)
        self.assertEqual(CYCLE341_N_LEAK, 0)
        if not prior_341.claim_holds:
            self.fail("nested cycle 341 leftover remaining-after-076-010 3-grams all I-only drifted")
        prior_340 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760104gramsIOnlyScoreboard()
        )
        prior_340.setUp()
        prior_340.test_each_4gram_is_i_only_not_hapax_extra_zero_and_claim_holds()
        prior_340.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE340_CLAIM)
        self.assertEqual(CYCLE340_N_EXTRA, 0)
        if not prior_340.claim_holds:
            self.fail("nested cycle 340 leftover remaining-after-076-010 4-grams all I-only drifted")
        prior_339 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next2gramScoreboard()
        )
        prior_339.setUp()
        prior_339.test_remaining_after_5_unique_max_loses()
        prior_339.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE339_K, 1)
        self.assertEqual(CYCLE339_G, CYCLE339_GRAM2)
        self.assertEqual(CYCLE339_N, 5)
        self.assertEqual(CYCLE339_N_REMAINING, 4)
        self.assertEqual(CYCLE339_N_TIED, 15)
        self.assertEqual(CYCLE339_N_DISTINCT, 15)
        self.assertFalse(CYCLE339_UNIQUE)
        self.assertFalse(CYCLE339_UNIQUE_MAX_CLAIM)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
                leftover
            )
        )
        if prior_339.claim_holds:
            self.fail("nested cycle 339 remaining-after-076-010 unique-max drifted")
        prior_338 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter0760200760104gramsIOnlyScoreboard()
        )
        prior_338.setUp()
        prior_338.test_each_4gram_is_two_on_i_zero_off_i_not_hapax_and_claim_holds()
        prior_338.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE338_CLAIM)
        self.assertEqual(CYCLE338_N_EXTRA, 0)
        if not prior_338.claim_holds:
            self.fail("nested cycle 338 leftover 076 010 4-grams all I-only drifted")
        prior_337 = TestMamariI2gram076010IOnlyScoreboard()
        prior_337.setUp()
        prior_337.test_2gram_is_three_off_i_and_not_i_only()
        prior_337.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE337_N_I, 11)
        self.assertEqual(CYCLE337_N_OFF_I, 3)
        self.assertEqual(CYCLE337_N_EXTRA, 8)
        self.assertFalse(CYCLE337_CLAIM)
        self.assertFalse(i_2gram_076_010_i_only(11, 3))
        if prior_337.claim_holds:
            self.fail("nested cycle 337 2-gram 076 010 I-only 11/3 drifted")
        prior_334 = TestMamariI2gram076020IOnlyScoreboard()
        prior_334.setUp()
        prior_334.test_2gram_is_zero_off_i_and_i_only()
        prior_334.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE334_N_I, 12)
        self.assertEqual(CYCLE334_N_OFF_I, 0)
        self.assertEqual(CYCLE334_N_EXTRA, 9)
        self.assertTrue(CYCLE334_CLAIM)
        self.assertTrue(i_2gram_076_020_i_only(12, 0))
        if not prior_334.claim_holds:
            self.fail("nested cycle 334 2-gram 076 020 I-only 12/0 drifted")
        prior_330 = TestMamariI2gram430076IOnlyScoreboard()
        prior_330.setUp()
        prior_330.test_2gram_is_sixteen_off_i_and_not_i_only()
        prior_330.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE330_N_I, 30)
        self.assertEqual(CYCLE330_N_OFF_I, 16)
        self.assertEqual(CYCLE330_N_EXTRA, 26)
        self.assertFalse(CYCLE330_CLAIM)
        self.assertFalse(i_2gram_430_076_i_only(30, 16))
        if prior_330.claim_holds:
            self.fail("nested cycle 330 2-gram 430 076 I-only 30/16 drifted")
        prior_298 = TestMamariILeftoverN4Remaining090076RemainingAfter011NextStemScoreboard()
        prior_298.setUp()
        prior_298.test_counts_2_remaining_g_607_k_1_hapax_and_hypothesis_loses()
        prior_298.test_survey_matches_computed_lock()
        self.assertFalse(CYCLE298_CLAIM)
        self.assertFalse(CYCLE298_UNIQUE)
        self.assertEqual(CYCLE298_G, "607")
        self.assertEqual(CYCLE298_K, 1)
        if prior_298.claim_holds or CYCLE298_UNIQUE:
            self.fail("nested cycle 298 leftover n=4 remaining remaining-after-011 unique next stem hapax pile G=607 K=1 drifted")
        prior_292 = TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard()
        prior_292.setUp()
        prior_292.test_counts_9_remaining_g_087_k_3_and_hypothesis_holds()
        prior_292.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE292_CLAIM)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertEqual(CYCLE292_G, "087")
        self.assertEqual(CYCLE292_K, 3)
        if not prior_292.claim_holds or CYCLE292_G != "087" or CYCLE292_K != 3:
            self.fail("nested cycle 292 leftover n=4 remaining remaining-after-020 unique-max G=087 K=3 drifted")
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
            self.fail("nested cycle 288 leftover n=4 remaining 13/13/0 N_distinct=6 G=020 K=4 unique-max drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, CYCLE223_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, CYCLE223_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        self.assertFalse(CYCLE223_CLAIM)
        self.assertFalse(i_2gram_090_076_i_only(69, 3))
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_CYCLE342_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE341_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE340_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE339_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE338_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE222_DOES_NOT_COUNT)
        self.assertTrue(STANDING_I_SITE_PEEL_288_327_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_DO_NOT_COUNT)
        self.assertTrue(STANDING_CYCLES_220_221_DO_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE223_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-343 leftover 4-gram next-stem lose."""
        lock = self.survey[STANDING_RESULT]
        self.assertEqual(lock["cycle"], 343)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["N"], STANDING_N)
        self.assertEqual(lock["N"], 11)
        self.assertEqual(lock["N_4grams"], STANDING_N_4GRAMS)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(
            [list(gram) for gram in CYCLE340_SEQUENCES],
            lock["leftover_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], 11)
        self.assertEqual(tuple(lock["next_stems"]), STANDING_NEXT_STEMS)
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 11)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 11)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 11)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "760")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 1)
        self.assertFalse(lock["unique_max"])
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 11)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 10)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_5GRAMS],
            lock["matching_next_5grams"],
        )
        self.assertEqual(
            lock["next_stem_frequency"],
            leftover_4gram_next_stem_frequency_rows(),
        )
        self.assertEqual(lock["nested_cycle342_extra_i_4grams_all_i_only"], True)
        self.assertEqual(lock["nested_cycle342_N_i_only"], 10)
        self.assertEqual(lock["nested_cycle342_N_hapax_i_only"], 10)
        self.assertEqual(lock["nested_cycle342_N_leak"], 0)
        self.assertEqual(lock["nested_cycle341_3grams_all_i_only"], True)
        self.assertEqual(lock["nested_cycle341_N_extra"], 5)
        self.assertEqual(lock["nested_cycle341_N_i_only"], 10)
        self.assertEqual(lock["nested_cycle341_N_leak"], 0)
        self.assertEqual(lock["nested_cycle340_4grams_all_i_only"], True)
        self.assertEqual(lock["nested_cycle340_N_extra"], 0)
        self.assertEqual(lock["nested_cycle340_N_i_only"], 5)
        self.assertEqual(lock["nested_cycle340_leftover_matching_count"], 11)
        self.assertEqual(lock["nested_cycle339_unique_max"], False)
        self.assertEqual(lock["nested_cycle339_K"], 1)
        self.assertEqual(lock["nested_cycle339_N"], 5)
        self.assertEqual(lock["nested_cycle339_N_remaining"], 4)
        self.assertEqual(lock["nested_cycle339_N_tied_at_k"], 15)
        self.assertEqual(tuple(lock["nested_cycle339_G"]), ("999", "604"))
        self.assertEqual(lock["nested_cycle338_4grams_all_i_only"], True)
        self.assertEqual(lock["nested_cycle338_N_extra"], 0)
        self.assertEqual(lock["nested_cycle337_N_I"], 11)
        self.assertEqual(lock["nested_cycle337_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle337_N_extra"], 8)
        self.assertEqual(lock["nested_cycle337_i_2gram_076_010_i_only"], False)
        self.assertEqual(lock["nested_cycle334_N_I"], 12)
        self.assertEqual(lock["nested_cycle334_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle334_N_extra"], 9)
        self.assertEqual(lock["nested_cycle330_i_2gram_430_076_i_only"], False)
        self.assertEqual(lock["nested_cycle330_N_I"], 30)
        self.assertEqual(lock["nested_cycle330_N_off_I"], 16)
        self.assertEqual(lock["nested_cycle298_unique_max"], False)
        self.assertEqual(lock["nested_cycle298_G"], "607")
        self.assertEqual(lock["nested_cycle298_K"], 1)
        self.assertEqual(lock["nested_cycle292_unique_max"], True)
        self.assertEqual(lock["nested_cycle292_G"], "087")
        self.assertEqual(lock["nested_cycle292_K"], 3)
        self.assertEqual(lock["nested_cycle288_N_distinct"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertFalse(lock["nested_cycle288_share_one"])
        self.assertEqual(lock["nested_cycle256_G"], "755")
        self.assertEqual(lock["nested_cycle256_K"], 1)
        self.assertFalse(lock["nested_cycle256_unique_max"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle222_K"], 5)
        self.assertEqual(lock["nested_cycle222_N_remaining"], 16)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(
            lock[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_next_stem"
            ]
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle222"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertFalse(lock["same_as_cycle288"])
        self.assertFalse(lock["same_as_cycle292"])
        self.assertFalse(lock["same_as_cycle298"])
        self.assertFalse(lock["same_as_cycle339"])
        self.assertFalse(lock["same_as_cycle340"])
        self.assertFalse(lock["same_as_cycle341"])
        self.assertFalse(lock["same_as_cycle342"])
        self.assertTrue(lock["same_claim_shape_as_cycle256"])
        self.assertTrue(lock["same_claim_shape_as_cycle288"])
        self.assertTrue(lock["same_claim_shape_as_cycle292"])
        self.assertTrue(lock["same_claim_shape_as_cycle298"])
        self.assertTrue(lock["labeled_g_does_not_count"])
        self.assertTrue(lock["empty_remainder_does_not_lose"])
        self.assertTrue(lock["do_not_peel_a_specific_stem"])
        self.assertTrue(lock["do_not_claim_5grams_i_only"])
        self.assertTrue(lock["do_not_claim_exactly_k_share"])
        self.assertTrue(lock["leftover_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["leftover_3gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["extra_i_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["unique_max_2gram_is_not_this_cycle"])
        self.assertTrue(lock["090_076_does_not_count"])
        self.assertTrue(lock["430_076_does_not_count"])
        self.assertTrue(lock["076_020_does_not_count"])
        self.assertTrue(lock["076_010_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["do_not_relock_cycle342"])
        self.assertTrue(lock["do_not_relock_cycle341"])
        self.assertTrue(lock["do_not_relock_cycle340"])
        self.assertTrue(lock["do_not_relock_cycle339"])
        self.assertTrue(lock["do_not_relock_cycle338"])
        self.assertTrue(lock["do_not_relock_cycle337"])
        self.assertTrue(lock["do_not_relock_cycle336"])
        self.assertTrue(lock["do_not_relock_cycle335"])
        self.assertTrue(lock["do_not_relock_cycle334"])
        self.assertTrue(lock["do_not_relock_cycle333"])
        self.assertTrue(lock["do_not_relock_cycle332"])
        self.assertTrue(lock["do_not_relock_cycle331"])
        self.assertTrue(lock["do_not_relock_cycle330"])
        self.assertTrue(lock["do_not_relock_cycle329"])
        self.assertTrue(lock["do_not_relock_cycle328"])
        self.assertTrue(lock["do_not_relock_cycle222"])
        self.assertTrue(lock["do_not_relock_cycles_288_327"])
        self.assertTrue(lock["do_not_relock_leftover_extra_peels"])
        self.assertTrue(lock["do_not_relock_cycles_220_221"])
        self.assertTrue(lock["do_not_relock_cycle223"])
        self.assertTrue(lock["g_k_is_inventory_for_later_peel"])
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_4grams_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2gram_unchanged"
            ]
        )
        self.assertTrue(lock["standing_i_2gram_076_010_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_020_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_430_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_011_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        prior_342 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_4grams_i_only"
        ]
        self.assertEqual(prior_342["cycle"], 342)
        self.assertTrue(
            prior_342[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_4grams_all_i_only"
            ]
        )
        self.assertEqual(prior_342["N_i_only"], 10)
        prior_341 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_i_only"
        ]
        self.assertEqual(prior_341["cycle"], 341)
        self.assertTrue(
            prior_341[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_all_i_only"
            ]
        )
        self.assertEqual(prior_341["N_extra"], 5)
        prior_340 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only"
        ]
        self.assertEqual(prior_340["cycle"], 340)
        self.assertTrue(
            prior_340[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_all_i_only"
            ]
        )
        self.assertEqual(prior_340["N_extra"], 0)
        prior_339 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2gram"
        ]
        self.assertEqual(prior_339["cycle"], 339)
        self.assertFalse(prior_339["unique_max"])
        self.assertEqual(prior_339["K"], 1)
        self.assertEqual(prior_339["N"], 5)
        prior_298 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_next_stem"]
        self.assertEqual(prior_298["cycle"], 298)
        self.assertFalse(prior_298["i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem"])
        self.assertEqual(prior_298["G"], "607")
        self.assertEqual(prior_298["K"], 1)
        prior_292 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]
        self.assertEqual(prior_292["cycle"], 292)
        self.assertTrue(prior_292["i_leftover_n4_remaining_090_076_remaining_after_020_unique_next_stem"])
        self.assertEqual(prior_292["G"], "087")
        self.assertEqual(prior_292["K"], 3)
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["N_distinct_next_stems"], 6)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
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


class TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010NextStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 343 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
