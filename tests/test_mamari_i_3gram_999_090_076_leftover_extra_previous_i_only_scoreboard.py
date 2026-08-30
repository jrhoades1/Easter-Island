"""I's cycle-261 leftover extra previous-999 3-gram 999 090 076 off-I lock.

Cycle 262 text-search lock. Uses already-vendored A–V and the
cycle-261 leftover extra previous-999 cluster (K_999=15 of
N_leftover_extra=56; N_remaining_after_999=41). Does not
retune that leftover extra previous-999 lock, leftover extra
share-one-previous-stem (cycle 260 lost), leftover extra
share-one-forward-stem (cycle 225 lost), leftover extra
sites, the leftover n=4 set, or the already-closed leftover
remaining family. Does not retune the forward peel of leftover
extra I 090 076 (cycles 225–259). Does not peel leftover extra
remaining-after-999 this cycle. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same claim-shape as cycle 212 (720 076 070 was I-only 3/0
after leftover previous-720) and cycle 232 (090 076 001 was
I-only 3/0). Extra I of this 3-gram is leftover-of-leftover,
same shape as cycle 245 extra I of 090 076 087. Cycle 207
lost: 090 076 070 is not I-only (8/1 on T). Cycle 223 lost:
090 076 is not I-only (69/3 on T). Cycle 167 already locked
this same 3-gram I-only 16/0 in leftover n=4 family context;
this cycle is the leftover extra previous-999 nested lock of
that 3-gram (do not retune 167). Cycle 220 5-gram
999 090 076 070 000 is a different n=5 (1/0). 090 076 without
999, 720 076 070, and 090 076 001 do not count as this
3-gram. Do not retune leftover n=4, 076-cells, or any
detector. Do not lock leftover extra remaining-after-999.
Off-I T sites of 090 076 are not this cycle except as off-I
of 999 090 076 if they match. Do not assume the I-only
result.

Locks exact consecutive hits of 999 090 076 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can
lose: i_3gram_999_090_076_i_only (I hits ≥ 1 and off-I hits
== 0). True only if N_off_I == 0. Extra I ≠ 0 does not make
the claim lose (still I-only); still lock extra I. Measured:
Ia is exactly 16 at Ia1[1]/Ia2[9]/Ia3[36]/Ia3[70]/Ia4[111]/
Ia4[153]/Ia5[1]/Ia5[22]/Ia6[91]/Ia7[67]/Ia7[128]/Ia9[27]/
Ia9[128]/Ia12[46]/Ia13[108]/Ia14[139]; Ib unpublished 0;
every other vendored tablet is exact-0. Leftover extra
previous-999 15 sites (090-starts) ⊆ those I 3-gram sites
(999-starts one token earlier). Extra I = 1 at Ia9[27]
(090-start Ia9[28] sits inside leftover n=4 remaining
999 090 076 057; leftover of leftover, not locked as
remaining-after-999). The claim is true. Not an n≥8 island.
Not the cycle-103 I 5-gram. Nested leftover extra previous-999
K_999=15 / N_remaining_after_999=41, leftover extra==56,
N_I==69, cycle 260 34 distinct G=999 K=15, cycle 220 5-gram
1/0, cycle 225 30 distinct G=070 K=8, cycle 223 69/3, and
cycle 207 8/1 stay.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_g_nge8_scoreboard import (
    nge8_sites,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES as CYCLE223_I_SITES,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_001_i_only_scoreboard import (
    GRAM3 as CYCLE232_GRAM3,
    STANDING_I_3GRAM_090_076_001_I_ONLY as CYCLE232_CLAIM,
    STANDING_I_SITES as CYCLE232_I_SITES,
    STANDING_N_I as CYCLE232_N_I,
    STANDING_N_OFF_I as CYCLE232_N_OFF_I,
    TestMamariI3gram090076001IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    GRAM3 as CYCLE245_GRAM3,
    STANDING_I_3GRAM_090_076_087_I_ONLY as CYCLE245_CLAIM,
    STANDING_N_EXTRA as CYCLE245_N_EXTRA,
    STANDING_N_I as CYCLE245_N_I,
    STANDING_N_OFF_I as CYCLE245_N_OFF_I,
    TestMamariI3gram090076087IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_720_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE212_GRAM3,
    STANDING_I_3GRAM_720_076_070_I_ONLY as CYCLE212_CLAIM,
    STANDING_I_SITES as CYCLE212_I_SITES,
    STANDING_N_I as CYCLE212_N_I,
    STANDING_N_OFF_I as CYCLE212_N_OFF_I,
    TestMamariI3gram720076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_I_SITES as CYCLE167_I_SITES,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
    i_3gram_999_090_076_i_only as cycle167_i_only,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    GRAM5 as CYCLE220_GRAM5,
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_CLAIM,
    STANDING_I_SITES as CYCLE220_I_SITES,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
    TestMamariI5gram999090076070000IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE225_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_K as CYCLE225_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    TestMamariILeftoverExtra090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    GRAM3_BACKWARD,
    STANDING_G as CYCLE261_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 as CYCLE261_CLAIM,
    STANDING_K_999 as CYCLE261_K_999,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE261_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
    STANDING_N_LEFTOVER_EXTRA as CYCLE261_N_LEFTOVER_EXTRA,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    leftover_extra_with_previous_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_G_SITES as CYCLE260_G_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    leftover_extra_previous_stems,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
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
from tests.test_mamari_keiti_n9_scoreboard import (
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_s_nge6_scoreboard import (
    nge6_sites,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    OFF_I_TABLETS,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    load_g_k_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SIDE_SA,
    SIDE_SB,
    load_s_sides,
)

HYPOTHESIS_I_ONLY = True
GRAM3 = GRAM3_BACKWARD
NEAR_MISS_720_076_070 = CYCLE212_GRAM3
NEAR_MISS_090_076_001 = CYCLE232_GRAM3
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076_087 = CYCLE245_GRAM3
NEAR_MISS_090_076 = GRAM2
NEAR_MISS_5GRAM = CYCLE220_GRAM5
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_I_HITS = 16
STANDING_IA_HITS = 16
STANDING_IB_HITS = 0
STANDING_N_ON_I = 16
STANDING_N_I = 16
STANDING_I_SITES = (
    (SIDE_IA, "Ia1", 1),
    (SIDE_IA, "Ia2", 9),
    (SIDE_IA, "Ia3", 36),
    (SIDE_IA, "Ia3", 70),
    (SIDE_IA, "Ia4", 111),
    (SIDE_IA, "Ia4", 153),
    (SIDE_IA, "Ia5", 1),
    (SIDE_IA, "Ia5", 22),
    (SIDE_IA, "Ia6", 91),
    (SIDE_IA, "Ia7", 67),
    (SIDE_IA, "Ia7", 128),
    (SIDE_IA, "Ia9", 27),
    (SIDE_IA, "Ia9", 128),
    (SIDE_IA, "Ia12", 46),
    (SIDE_IA, "Ia13", 108),
    (SIDE_IA, "Ia14", 139),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_MATCHING_SITES = CYCLE261_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_COUNT = 15
STANDING_LEFTOVER_MATCHING_PREVIOUS_4GRAMS = CYCLE261_MATCHING_PREVIOUS_4GRAMS
STANDING_LEFTOVER_3GRAM_SITES = (
    (SIDE_IA, "Ia1", 1),
    (SIDE_IA, "Ia2", 9),
    (SIDE_IA, "Ia3", 36),
    (SIDE_IA, "Ia3", 70),
    (SIDE_IA, "Ia4", 111),
    (SIDE_IA, "Ia4", 153),
    (SIDE_IA, "Ia5", 1),
    (SIDE_IA, "Ia5", 22),
    (SIDE_IA, "Ia6", 91),
    (SIDE_IA, "Ia7", 67),
    (SIDE_IA, "Ia7", 128),
    (SIDE_IA, "Ia9", 128),
    (SIDE_IA, "Ia12", 46),
    (SIDE_IA, "Ia13", 108),
    (SIDE_IA, "Ia14", 139),
)
STANDING_N_LEFTOVER = 15
STANDING_EXTRA_I_SITES = (
    (SIDE_IA, "Ia9", 27),
)
STANDING_N_EXTRA = 1
STANDING_EXTRA_I_090_076_SITES = (
    (SIDE_IA, "Ia9", 28),
)
STANDING_I_PREVIOUS_4GRAMS = (
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
    ("244", "999", "090", "076"),
    ("075", "999", "090", "076"),
    ("090", "999", "090", "076"),
    ("700", "999", "090", "076"),
    ("090", "999", "090", "076"),
)
STANDING_I_NEXT_4GRAMS = (
    ("999", "090", "076", "012"),
    ("999", "090", "076", "070"),
    ("999", "090", "076", "013"),
    ("999", "090", "076", "005"),
    ("999", "090", "076", "070"),
    ("999", "090", "076", "071"),
    ("999", "090", "076", "071"),
    ("999", "090", "076", "071"),
    ("999", "090", "076", "013"),
    ("999", "090", "076", "070"),
    ("999", "090", "076", "070"),
    ("999", "090", "076", "057"),
    ("999", "090", "076", "057"),
    ("999", "090", "076", "011"),
    ("999", "090", "076", "005"),
    ("999", "090", "076", "070"),
)
STANDING_I_SITE_ROWS = (
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia1",
        "index": 1,
        "previous_4gram": ("602", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia1", 2),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia2",
        "index": 9,
        "previous_4gram": ("070", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia2", 10),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia3",
        "index": 36,
        "previous_4gram": ("000", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia3", 37),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia3",
        "index": 70,
        "previous_4gram": ("499", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia3", 71),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia4",
        "index": 111,
        "previous_4gram": ("060", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia4", 112),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia4",
        "index": 153,
        "previous_4gram": ("254", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia4", 154),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia5",
        "index": 1,
        "previous_4gram": ("000", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia5", 2),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia5",
        "index": 22,
        "previous_4gram": ("381", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia5", 23),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia6",
        "index": 91,
        "previous_4gram": ("023", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia6", 92),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia7",
        "index": 67,
        "previous_4gram": ("064", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia7", 68),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia7",
        "index": 128,
        "previous_4gram": ("518", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia7", 129),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia9",
        "index": 27,
        "previous_4gram": ("244", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia9", 28),
        "in_cycle261_leftover_extra_15": False,
        "inside_leftover_n4_remaining": True,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia9",
        "index": 128,
        "previous_4gram": ("075", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia9", 129),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia12",
        "index": 46,
        "previous_4gram": ("090", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia12", 47),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia13",
        "index": 108,
        "previous_4gram": ("700", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia13", 109),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia14",
        "index": 139,
        "previous_4gram": ("090", "999", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia14", 140),
        "in_cycle261_leftover_extra_15": True,
        "inside_leftover_n4_remaining": False,
    },
)
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_OFF_I_BY_TABLET_NONZERO = {}
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_3gram_999_090_076_i_only"
STANDING_I_3GRAM_999_090_076_I_ONLY = True
STANDING_RESULT = "i_3gram_999_090_076_leftover_extra_previous_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE212_3GRAM = False
STANDING_SAME_AS_CYCLE220_5GRAM = False
STANDING_SAME_AS_CYCLE232_3GRAM = False
STANDING_SAME_AS_CYCLE245_3GRAM = False
STANDING_SAME_AS_CYCLE261 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE212 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE232 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245_EXTRA_I = True
STANDING_090_076_WITHOUT_999_DOES_NOT_COUNT = True
STANDING_720_076_070_DOES_NOT_COUNT = True
STANDING_090_076_001_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_5GRAM_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE261_K_999 = 15
STANDING_CYCLE261_G = "999"
STANDING_CYCLE261_N_REMAINING_AFTER_999 = 41
STANDING_CYCLE261_N_LEFTOVER_EXTRA = 56
STANDING_CYCLE223_N_I = 69


def leftover_extra_090_076_site_for_3gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """090 076 starts one token after 999 090 076."""
    side, line, index = site
    return (side, line, index + 1)


def leftover_extra_previous_999_3gram_sites(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra previous-999 090-starts shifted back to 999-starts."""
    return tuple((side, line, index - 1) for side, line, index in leftover_matching)


def leftover_extra_previous_999_subset(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover extra previous-999 15 sites ⊆ I 999 090 076 sites."""
    return set(leftover_extra_previous_999_3gram_sites(leftover_matching)).issubset(
        set(i_sites)
    )


def leftover_3gram_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 999 090 076 sites whose 090 076 is leftover extra previous-999."""
    leftover_set = set(leftover_matching)
    return tuple(
        site
        for site in i_sites
        if leftover_extra_090_076_site_for_3gram(site) in leftover_set
    )


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 999 090 076 sites that are not leftover extra previous-999."""
    leftover_set = set(leftover_matching)
    return tuple(
        site
        for site in i_sites
        if leftover_extra_090_076_site_for_3gram(site) not in leftover_set
    )


def site_previous_4gram_for_3gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """W 999 090 076 if a previous stem exists; None at start-of-line."""
    if tuple(stems[index : index + len(gram3)]) != gram3:
        return None
    if index < 1:
        return None
    return tuple(stems[index - 1 : index + len(gram3)])


def i_3gram_999_090_076_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0. Extra I does not lose."""
    return i_hits >= 1 and off_i_hits == 0


def named_off_i_sites(
    gram: tuple[str, ...] = GRAM3,
) -> tuple[tuple[str, str, int], ...]:
    """Named (side, line, index) hits on G, S, and T. Search only."""
    gk = load_g_k_sides()
    g_sites = nge8_sites(gram, gk)
    s_sites = nge6_sites(gram, load_s_sides())
    t = load_t_sides()
    t_sites = tuple(
        site_tuple(hit)
        for hit in named_side_hits(t[SIDE_TA], TA_LINE_NAMES, SIDE_TA, gram)
    )
    return g_sites + s_sites + t_sites


def i_site_row_as_survey(row: dict) -> dict:
    """JSON-ready site row (lists, not tuples)."""
    return {
        "tablet": row["tablet"],
        "side": row["side"],
        "line": row["line"],
        "index": row["index"],
        "previous_4gram": list(row["previous_4gram"]),
        "leftover_extra_090_076_site": list(row["leftover_extra_090_076_site"]),
        "in_cycle261_leftover_extra_15": row["in_cycle261_leftover_extra_15"],
        "inside_leftover_n4_remaining": row["inside_leftover_n4_remaining"],
    }


class TestI3gram999090076LeftoverExtraPreviousIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-261 leftover extra previous-999 3-gram. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 090 076 / 720 076 070 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3, CYCLE167_GRAM3)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["999", "090", "076", "999", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 2)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_720_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_001)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_087)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["720", "076", "070"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "001"]], GRAM3), 0)
        self.assertTrue(STANDING_090_076_WITHOUT_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_720_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_001_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_5GRAM_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Extra I does not lose."""
        provider = MockProvider()
        self.assertTrue(i_3gram_999_090_076_i_only(1, 0))
        self.assertTrue(i_3gram_999_090_076_i_only(15, 0))
        self.assertTrue(i_3gram_999_090_076_i_only(16, 0))
        self.assertFalse(i_3gram_999_090_076_i_only(16, 1))
        self.assertFalse(i_3gram_999_090_076_i_only(1, 1))
        self.assertFalse(i_3gram_999_090_076_i_only(0, 0))
        self.assertFalse(i_3gram_999_090_076_i_only(0, 1))
        self.assertEqual(
            i_3gram_999_090_076_i_only(16, 0),
            cycle167_i_only(16, 0),
        )
        self.assertEqual(STANDING_CLAIM, "i_3gram_999_090_076_i_only")
        self.assertTrue(STANDING_I_3GRAM_999_090_076_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(
            STANDING_I_3GRAM_999_090_076_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertNotEqual(STANDING_N_EXTRA, 0)
        self.assertTrue(STANDING_I_3GRAM_999_090_076_I_ONLY)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_fail(self):
        """Leftover extra previous-999 ⊆ I sites; extra is nonempty leftover-of-leftover."""
        provider = MockProvider()
        self.assertTrue(
            leftover_extra_previous_999_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(
            leftover_extra_previous_999_3gram_sites(),
            STANDING_LEFTOVER_3GRAM_SITES,
        )
        self.assertEqual(leftover_3gram_sites(), STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(len(extra_i_sites()), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertEqual(STANDING_N_LEFTOVER + STANDING_N_EXTRA, STANDING_N_I)
        self.assertEqual(
            leftover_extra_090_076_site_for_3gram(STANDING_EXTRA_I_SITES[0]),
            STANDING_EXTRA_I_090_076_SITES[0],
        )
        planted_extra = STANDING_I_SITES + ((SIDE_IA, "Ia1", 0),)
        self.assertFalse(
            leftover_extra_previous_999_subset(
                STANDING_LEFTOVER_MATCHING_SITES + ((SIDE_IA, "Ia1", 1),),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(len(extra_i_sites(planted_extra)), 2)
        dropped = tuple(
            site
            for site in STANDING_I_SITES
            if site != STANDING_LEFTOVER_3GRAM_SITES[0]
        )
        self.assertFalse(
            leftover_extra_previous_999_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                dropped,
            )
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle261_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-261 leftover extra previous G, not priors."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3[1:], GRAM2)
        self.assertEqual(GRAM3[0], CYCLE261_G)
        self.assertNotEqual(GRAM3, CYCLE212_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE232_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE245_GRAM3)
        self.assertNotEqual(GRAM3, GRAM2)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, CYCLE220_GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertTrue(is_contiguous_substring(GRAM3, CYCLE220_GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE212_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE220_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE232_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE245_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE261)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE212)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE232)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245_EXTRA_I)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertEqual(STANDING_N5, 5)
        self.assertLess(len(GRAM3), 8)
        for prev4 in STANDING_I_PREVIOUS_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, prev4))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_720_076_070))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_001))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM3))
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram999090076LeftoverExtraPreviousIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover extra previous-999 3-gram 999 090 076 off-I lock."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM3, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.off_i_sites = named_off_i_sites(GRAM3)
        self.previous_stems = leftover_extra_previous_stems(
            self.i_sides,
            STANDING_LEFTOVER_SITES,
            GRAM2,
        )
        self.leftover_matching = leftover_extra_with_previous_999(
            STANDING_LEFTOVER_SITES,
            self.previous_stems,
        )
        self.leftover = leftover_3gram_sites(self.i_sites, self.leftover_matching)
        self.extra = extra_i_sites(self.i_sites, self.leftover_matching)
        self.claim_holds = i_3gram_999_090_076_i_only(
            self.i_hits,
            self.off_i_hits,
        )
        self.previous_4grams = tuple(
            site_previous_4gram_for_3gram(
                line_stems_for_site(self.i_sides, site),
                site[2],
                GRAM3,
            )
            for site in self.i_sites
        )
        self.leftover_extra_090_076_sites = tuple(
            leftover_extra_090_076_site_for_3gram(site) for site in self.leftover
        )

    def test_tokens_are_cycle_261_leftover_not_retuned(self):
        """3-gram is the cycle-261 leftover extra previous G, not a new inventory."""
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3[1:], GRAM2)
        self.assertEqual(GRAM3[0], "999")
        prior_261 = self.survey["i_leftover_extra_090_076_previous_999"]
        self.assertEqual(prior_261["cycle"], 261)
        self.assertEqual(tuple(prior_261["backward_3gram"]), GRAM3)
        self.assertEqual(prior_261["G"], "999")
        self.assertEqual(prior_261["K"], 15)
        self.assertEqual(prior_261["K_999"], 15)
        self.assertEqual(prior_261["N_remaining_after_999"], 41)
        self.assertEqual(prior_261["N_leftover_extra"], 56)
        self.assertEqual(prior_261["N_I"], 69)
        self.assertEqual(CYCLE261_G, "999")
        self.assertEqual(CYCLE261_K_999, 15)
        self.assertEqual(CYCLE261_N_REMAINING_AFTER_999, 41)
        self.assertEqual(CYCLE261_N_LEFTOVER_EXTRA, 56)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertTrue(
            prior_261["i_leftover_extra_090_076_exactly_15_share_previous_999"]
        )
        measured_matching = [list(site) for site in CYCLE261_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_261["matching_leftover_extra_sites"]],
            measured_matching,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE261_MATCHING_PREVIOUS_4GRAMS],
            prior_261["matching_previous_4grams"],
        )
        self.assertEqual(self.leftover_matching, CYCLE261_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE261_K_999)
        self.assertEqual(STANDING_CYCLE261_K_999, 15)
        self.assertEqual(STANDING_CYCLE261_G, "999")
        self.assertEqual(STANDING_CYCLE261_N_REMAINING_AFTER_999, 41)
        self.assertEqual(STANDING_CYCLE261_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(STANDING_CYCLE223_N_I, 69)
        if (
            len(self.leftover_matching) != 15
            or CYCLE261_G != "999"
            or CYCLE261_K_999 != 15
            or CYCLE261_N_REMAINING_AFTER_999 != 41
            or CYCLE261_N_LEFTOVER_EXTRA != 56
            or CYCLE223_N_I != 69
        ):
            self.fail(
                "nested leftover extra previous-999 K_999=15 "
                "N_remaining=41 leftover extra=56 N_I=69 drifted"
            )
        prior_260 = self.survey["i_leftover_extra_090_076_previous_stem"]
        self.assertEqual(prior_260["cycle"], 260)
        self.assertEqual(prior_260["N_distinct_previous_stems"], 34)
        self.assertEqual(prior_260["G"], "999")
        self.assertEqual(prior_260["K"], 15)
        self.assertFalse(prior_260["i_leftover_extra_090_076_share_one_previous_stem"])
        if (
            prior_260["N_distinct_previous_stems"] != 34
            or prior_260["G"] != "999"
            or prior_260["K"] != 15
            or prior_260["i_leftover_extra_090_076_share_one_previous_stem"]
        ):
            self.fail("nested cycle 260 34 distinct G=999 K=15 drifted")
        prior_225 = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(prior_225["cycle"], 225)
        self.assertEqual(prior_225["N_distinct_next_stems"], 30)
        self.assertEqual(prior_225["G"], "070")
        self.assertEqual(prior_225["K"], 8)
        self.assertFalse(prior_225["i_leftover_extra_090_076_share_one_forward_stem"])
        if (
            prior_225["N_distinct_next_stems"] != 30
            or prior_225["G"] != "070"
            or prior_225["K"] != 8
            or prior_225["i_leftover_extra_090_076_share_one_forward_stem"]
        ):
            self.fail("nested cycle 225 30 distinct G=070 K=8 drifted")
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_220 = self.survey["i_5gram_999_090_076_070_000_i_only"]
        self.assertEqual(prior_220["cycle"], 220)
        self.assertEqual(prior_220["N_I"], 1)
        self.assertEqual(prior_220["N_off_I"], 0)
        self.assertTrue(prior_220["i_5gram_999_090_076_070_000_i_only"])
        prior_212 = self.survey["i_3gram_720_076_070_i_only"]
        self.assertEqual(prior_212["cycle"], 212)
        self.assertEqual(prior_212["N_I"], 3)
        self.assertEqual(prior_212["N_off_I"], 0)
        self.assertTrue(prior_212["i_3gram_720_076_070_i_only"])
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_sixteen_on_ia_and_leftover_extra_999_is_subset(self):
        """3-gram is 16 on Ia; Ib 0. Leftover extra previous-999 is 15 of those 16."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE167_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 16)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 16)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 16)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE261_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE260_G_SITES)
        self.assertNotEqual(self.leftover, STANDING_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 15)
        self.assertTrue(
            leftover_extra_previous_999_subset(
                self.leftover_matching,
                self.i_sites,
            )
        )
        self.assertEqual(self.leftover, STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.leftover), STANDING_N_LEFTOVER)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER, 15)
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertEqual(STANDING_N_LEFTOVER + STANDING_N_EXTRA, STANDING_N_I)
        self.assertEqual(self.leftover_extra_090_076_sites, CYCLE261_MATCHING_SITES)
        if self.i_hits != 16:
            self.fail("measured N_I drifted from 16")
        if self.leftover_matching != CYCLE261_MATCHING_SITES:
            self.fail("leftover extra previous-999 set drifted")
        if not leftover_extra_previous_999_subset(
            self.leftover_matching,
            self.i_sites,
        ):
            self.fail("leftover extra previous-999 15 sites not subset of I 999 090 076")
        if self.extra != STANDING_EXTRA_I_SITES:
            self.fail("extra I 999 090 076 leftover-of-leftover sites drifted")
        leftover_set = set(STANDING_LEFTOVER_3GRAM_SITES)
        extra_set = set(STANDING_EXTRA_I_SITES)
        for (side, line, index), prev4, nxt4, row in zip(
            STANDING_I_SITES,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            STANDING_I_SITE_ROWS,
            strict=True,
        ):
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N3]), prev4)
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), nxt4)
            self.assertEqual(
                site_previous_4gram_for_3gram(stems, index, GRAM3),
                prev4,
            )
            self.assertEqual(side, SIDE_IA)
            site = (side, line, index)
            gram2_site = leftover_extra_090_076_site_for_3gram(site)
            self.assertEqual((row["side"], row["line"], row["index"]), site)
            self.assertEqual(row["previous_4gram"], prev4)
            self.assertEqual(tuple(row["leftover_extra_090_076_site"]), gram2_site)
            if site in leftover_set:
                self.assertIn(gram2_site, STANDING_LEFTOVER_SITES)
                self.assertIn(gram2_site, CYCLE261_MATCHING_SITES)
                self.assertNotIn(gram2_site, CYCLE224_INSIDE_SITES)
                self.assertTrue(row["in_cycle261_leftover_extra_15"])
                self.assertFalse(row["inside_leftover_n4_remaining"])
            else:
                self.assertIn(site, extra_set)
                self.assertIn(gram2_site, CYCLE224_INSIDE_SITES)
                self.assertNotIn(gram2_site, STANDING_LEFTOVER_SITES)
                self.assertNotIn(gram2_site, CYCLE261_MATCHING_SITES)
                self.assertFalse(row["in_cycle261_leftover_extra_15"])
                self.assertTrue(row["inside_leftover_n4_remaining"])
            self.assertNotIn(site, CYCLE212_I_SITES)
            self.assertNotIn(site, CYCLE232_I_SITES)
            self.assertNotIn(site, CYCLE207_I_SITES)
        self.assertEqual(self.previous_4grams, STANDING_I_PREVIOUS_4GRAMS)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(STANDING_EXTRA_I_SITES, ((SIDE_IA, "Ia9", 27),))
        self.assertEqual(STANDING_EXTRA_I_090_076_SITES, ((SIDE_IA, "Ia9", 28),))
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[0], CYCLE223_I_SITES)
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[0], CYCLE224_INSIDE_SITES)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 16. T 090 076 is not this 3-gram."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, 0)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(STANDING_OFF_I_SITES, ())
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ())
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {})
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM3))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 16)
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM3), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM3), 0)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM3), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM3), 0)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM3), 0)
        self.assertEqual(named_off_i_sites(GRAM3), ())
        self.assertEqual(CYCLE223_OFF_I_SITES, (
            (SIDE_TA, "Ta5", 9),
            (SIDE_TA, "Ta7", 5),
            (SIDE_TA, "Ta9", 2),
        ))
        self.assertEqual(
            CYCLE223_OFF_I_FOLLOWING_3GRAMS,
            (("090", "076", "010"), ("090", "076", "126"), ("090", "076", "070")),
        )
        for site, following in zip(
            CYCLE223_OFF_I_SITES,
            CYCLE223_OFF_I_FOLLOWING_3GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + 2]), GRAM2)
            self.assertEqual(tuple(stems[index : index + 3]), following)
            self.assertNotEqual(following, GRAM3)
            if index >= 1:
                self.assertNotEqual(tuple(stems[index - 1 : index + 2]), GRAM3)
            self.assertNotIn(site, STANDING_I_SITES)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        ta9 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta9")]
        self.assertEqual(tuple(ta9[2:5]), CYCLE207_GRAM3)
        self.assertNotEqual(tuple(ta9[2:5]), GRAM3)
        if len(ta9) >= 5:
            self.assertNotEqual(tuple(ta9[1:4]), GRAM3)
        self.assertEqual(
            i_3gram_999_090_076_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_999_090_076_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_999_090_076_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_3GRAM_999_090_076_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_999_090_076_i_only")
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertTrue(self.claim_holds)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE212_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE220_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE232_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE245_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE261)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE212)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE232)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245_EXTRA_I)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        if self.off_i_hits != 0:
            self.fail("measured N_off_I drifted from 0")
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_261_260_225_223_220_212_207_167_and_w_still_compute(self):
        """Cycle 261 K=15/41, 260 34/999/15, 225 30/070/8, 223 69/3, 220 1/0, 212 3/0, 207 8/1, 167 16/0 stay."""
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(CYCLE261_G, "999")
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertEqual(prior_261.n_leftover_extra, 56)
        self.assertEqual(prior_261.matching, CYCLE261_MATCHING_SITES)
        self.assertTrue(prior_261.claim_holds)
        self.assertTrue(CYCLE261_CLAIM)
        if (
            prior_261.k_999 != 15
            or CYCLE261_G != "999"
            or prior_261.n_remaining_after_999 != 41
            or prior_261.n_leftover_extra != 56
        ):
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 N_remaining=41 drifted")
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertFalse(prior_260.claim_holds)
        self.assertFalse(CYCLE260_SHARE_ONE)
        if prior_260.n_distinct != 34 or CYCLE260_G != "999" or CYCLE260_K != 15:
            self.fail("nested cycle 260 34 distinct G=999 K=15 drifted")
        prior_225 = TestMamariILeftoverExtra090076ForwardStemScoreboard()
        prior_225.setUp()
        prior_225.test_counts_30_distinct_next_stems_and_claim_loses()
        prior_225.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(CYCLE225_G, "070")
        self.assertEqual(CYCLE225_K, 8)
        self.assertFalse(CYCLE225_SHARE_ONE)
        if CYCLE225_N_DISTINCT != 30 or CYCLE225_G != "070" or CYCLE225_K != 8:
            self.fail("nested cycle 225 30 distinct G=070 K=8 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, CYCLE223_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, CYCLE223_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_220 = TestMamariI5gram999090076070000IOnlyScoreboard()
        prior_220.setUp()
        prior_220.test_5gram_is_zero_off_i_and_i_only()
        prior_220.test_survey_matches_computed_lock()
        self.assertEqual(prior_220.i_hits, CYCLE220_N_I)
        self.assertEqual(prior_220.i_hits, 1)
        self.assertEqual(prior_220.off_i_hits, CYCLE220_N_OFF_I)
        self.assertEqual(prior_220.off_i_hits, 0)
        self.assertEqual(prior_220.i_sites, CYCLE220_I_SITES)
        self.assertTrue(prior_220.claim_holds)
        self.assertTrue(CYCLE220_CLAIM)
        if prior_220.i_hits != 1 or prior_220.off_i_hits != 0:
            self.fail("nested cycle 220 999 090 076 070 000 I-only 1/0 drifted")
        prior_212 = TestMamariI3gram720076070IOnlyScoreboard()
        prior_212.setUp()
        prior_212.test_3gram_is_zero_off_i_and_i_only()
        prior_212.test_survey_matches_computed_lock()
        self.assertEqual(prior_212.i_hits, CYCLE212_N_I)
        self.assertEqual(prior_212.i_hits, 3)
        self.assertEqual(prior_212.off_i_hits, CYCLE212_N_OFF_I)
        self.assertEqual(prior_212.off_i_hits, 0)
        self.assertEqual(prior_212.i_sites, CYCLE212_I_SITES)
        self.assertTrue(prior_212.claim_holds)
        self.assertTrue(CYCLE212_CLAIM)
        if prior_212.i_hits != 3 or prior_212.off_i_hits != 0:
            self.fail("nested cycle 212 720 076 070 I-only 3/0 drifted")
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
        self.assertEqual(prior_167.i_hits, CYCLE167_N_I)
        self.assertEqual(prior_167.i_hits, 16)
        self.assertEqual(prior_167.off_i_hits, CYCLE167_N_OFF_I)
        self.assertEqual(prior_167.off_i_hits, 0)
        self.assertEqual(prior_167.i_sites, CYCLE167_I_SITES)
        self.assertTrue(prior_167.claim_holds)
        self.assertTrue(CYCLE167_CLAIM)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_232 = TestMamariI3gram090076001IOnlyScoreboard()
        prior_232.setUp()
        prior_232.test_3gram_is_zero_off_i_and_i_only()
        prior_232.test_survey_matches_computed_lock()
        self.assertEqual(prior_232.i_hits, CYCLE232_N_I)
        self.assertEqual(prior_232.off_i_hits, CYCLE232_N_OFF_I)
        self.assertTrue(prior_232.claim_holds)
        self.assertTrue(CYCLE232_CLAIM)
        prior_245 = TestMamariI3gram090076087IOnlyScoreboard()
        prior_245.setUp()
        prior_245.test_3gram_is_zero_off_i_and_i_only()
        prior_245.test_survey_matches_computed_lock()
        self.assertEqual(prior_245.i_hits, CYCLE245_N_I)
        self.assertEqual(prior_245.off_i_hits, CYCLE245_N_OFF_I)
        self.assertEqual(CYCLE245_N_EXTRA, 3)
        self.assertTrue(prior_245.claim_holds)
        self.assertTrue(CYCLE245_CLAIM)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-262 leftover extra previous-999 3-gram I-only lock."""
        lock = self.survey["i_3gram_999_090_076_leftover_extra_previous_i_only"]
        self.assertEqual(lock["cycle"], 262)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 16)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_extra_previous_999_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(
            lock["leftover_extra_previous_999_count"],
            STANDING_LEFTOVER_MATCHING_COUNT,
        )
        self.assertEqual(lock["leftover_extra_previous_999_count"], 15)
        self.assertTrue(lock["leftover_extra_previous_999_subset_of_i_sites"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_3gram_sites"]),
            STANDING_LEFTOVER_3GRAM_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 15)
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_090_076_sites"]),
            STANDING_EXTRA_I_090_076_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_I_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_I_NEXT_4GRAMS],
            lock["i_next_4grams"],
        )
        self.assertEqual(
            [i_site_row_as_survey(row) for row in STANDING_I_SITE_ROWS],
            lock["i_site_rows"],
        )
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 0)
        self.assertEqual(
            [list(site) for site in STANDING_OFF_I_SITES],
            lock["off_i_sites"],
        )
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(
            tuple(lock["off_i_tablets_with_hits"]),
            STANDING_OFF_I_TABLETS_WITH_HITS,
        )
        self.assertEqual(
            lock["off_i_by_tablet_nonzero"],
            STANDING_OFF_I_BY_TABLET_NONZERO,
        )
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_3gram_999_090_076_i_only"])
        self.assertEqual(
            lock["i_3gram_999_090_076_i_only"],
            STANDING_I_3GRAM_999_090_076_I_ONLY,
        )
        self.assertTrue(lock["i_3gram_999_090_076_leftover_extra_previous_i_only"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle212_3gram"])
        self.assertFalse(lock["same_as_cycle220_5gram"])
        self.assertFalse(lock["same_as_cycle232_3gram"])
        self.assertFalse(lock["same_as_cycle245_3gram"])
        self.assertFalse(lock["same_as_cycle261"])
        self.assertTrue(lock["same_claim_shape_as_cycle212"])
        self.assertTrue(lock["same_claim_shape_as_cycle232"])
        self.assertTrue(lock["same_claim_shape_as_cycle245_extra_i"])
        self.assertTrue(lock["090_076_without_999_does_not_count"])
        self.assertTrue(lock["720_076_070_does_not_count"])
        self.assertTrue(lock["090_076_001_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["5gram_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_999_is_not_this_cycle"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle261_N_leftover_extra"], 56)
        self.assertEqual(lock["nested_cycle261_N_I"], 69)
        self.assertEqual(lock["nested_cycle260_N_distinct_previous_stems"], 34)
        self.assertEqual(lock["nested_cycle260_G"], "999")
        self.assertEqual(lock["nested_cycle260_K"], 15)
        self.assertFalse(lock["nested_cycle260_share_one_previous_stem"])
        self.assertEqual(lock["nested_cycle225_N_distinct_next_stems"], 30)
        self.assertEqual(lock["nested_cycle225_G"], "070")
        self.assertEqual(lock["nested_cycle225_K"], 8)
        self.assertFalse(lock["nested_cycle225_share_one_forward_stem"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle220_N_I"], 1)
        self.assertEqual(lock["nested_cycle220_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle212_N_I"], 3)
        self.assertEqual(lock["nested_cycle212_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_5gram_999_090_076_070_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_720_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_001_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_087_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["cycle"], 261)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_previous_999"][
                "i_leftover_extra_090_076_exactly_15_share_previous_999"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_999"]["K_999"],
            15,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_999"]["N_remaining_after_999"],
            41,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["cycle"], 260)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_stem"]["N_distinct_previous_stems"],
            34,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["cycle"], 225)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_forward_stem"]["N_distinct_next_stems"],
            30,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_5gram_999_090_076_070_000_i_only"]["cycle"], 220)
        self.assertTrue(
            self.survey["i_5gram_999_090_076_070_000_i_only"][
                "i_5gram_999_090_076_070_000_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["cycle"], 212)
        self.assertTrue(self.survey["i_3gram_720_076_070_i_only"]["i_3gram_720_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI3gram999090076LeftoverExtraPreviousIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 262 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
