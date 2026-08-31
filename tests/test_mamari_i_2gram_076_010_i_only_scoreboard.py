"""I's cycle-336 leftover remaining-after-076-020 2-gram 076 010 off-I lock.

Cycle 337 text-search lock. Uses already-vendored A–V and the
cycle-336 leftover n=4 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 labeled G=076 010
(exactly K=2 of N=7). Does not retune that 2-gram, the leftover
n=4 set, cycle 336 exactly-2-share, cycle 335 unique-max, cycle
334 2-gram 076 020 I-only, cycle 333 exactly-2-share, cycle 332
unique-max, cycle 331 leftover 4-gram I-only, cycle 330 2-gram
430 076 I-only, cycle 329 exactly-2-share, cycle 328 unique-max,
cycle 222, leftover n=4 remaining I 090 076 peels (288–327),
leftover extra 090 076 peels, cycles 220–221, or cycle 223.
Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented Barthel.
No G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Same claim-shape as cycle 334 (2-gram 076 020 I-only held 12/0
extra I=9 after cycle 333 exactly 2 share 076 020). Also analog
cycle 330 (2-gram 430 076 I-only lost 30/16 including T after
cycle 329 exactly 2 share 430 076) and cycle 223 (2-gram 090 076
I-only lost 69/3 on T after cycle 222 exactly 5 contain 090 076).
This cycle is the new 2-gram 076 010 only. 076 020 is a different
2-gram (already held 12/0). 430 076 is a different 2-gram
(already lost 30/16). 090 076 is a different 2-gram (already
lost 69/3). Nested cycle 46 Santiago longest n=5
999 071 076 010 079 (freq 3) and split 5-gram 076 010 079 006 700
stay nested. Extra I of 2-gram 076 010 may include those I sites
plus other I sites. Extra I ≠ 0 is recorded, not this cycle's
claim. Do not re-lock those. Do not skip this I-only lock
because of that overlap. Do not retune leftover n=4, leftover
extra peels, 076-cells, or any detector. Do not lock leftover
4-gram I-only or all-I-inside-family this cycle (skip analog of
cycle 224 until extra I is measured; extra I ≠ 0 so all-inside
is false). Do not assume the I-only result.

Locks exact consecutive hits of 076 010 on tablet I and on every
other vendored tablet A–H and J–V. Claim that can lose:
i_2gram_076_010_i_only (I hits ≥ 1 and off-I hits == 0). True
only if N_off_I == 0. Measured: Ia is exactly 11; Ib unpublished
0; off-I is 3 on S (1 Sb4[18]) and T (2 Ta4[4]/Ta5[10]). T is
among the leaks. Leftover matching sites are the unique I
076 010 sites inside the two remaining-after-076-020 leftovers
076 010 079 090 / 072 076 010 079 (Ia5[110]/Ia5[139]/Ia13[72];
3). Leftover 4-gram starts are Ia5[110]/Ia5[139]/Ia5[138]/
Ia13[71]; Ia5[139] is shared by both leftovers. Extra I = 8
(I occurrences outside those leftover matching sites). Extra I
includes cycle-46 5-gram 076 010 sites Ia4[8]/Ia4[27] and split
5-gram site Ia6[19]; Ia5[110] of the cycle-46 5-gram and
Ia13[72] of the split 5-gram are leftover matching, not extra I.
Extra I ≠ 0 does not make the claim lose (still I-only if
N_off_I=0); still lock extra I. The claim is false. Not an n≥8
island. Not the cycle-103 I 5-gram. Nested cycle 336
exactly-2-share-076 010, cycle 335 unique_max false, cycle 334
12/0, cycle 333 K=2, cycle 332 unique_max false, cycle 331
leftover 4-grams all I-only, cycle 330 30/16, cycle 329 K=2,
cycle 328 unique_max false, cycle 222 K=5 / G=090 076, leftover
n=4 remaining I 090 076 peels (288–327), leftover extra 090 076
peels, cycles 220–221, and cycle 223 69/3 stay.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_br_scoreboard import BR_LINE_NAMES
from tests.test_mamari_aruku_bv_scoreboard import BV_LINE_NAMES
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_g_nge8_scoreboard import (
    nge8_sites as g_nge8_sites,
)
from tests.test_mamari_h_nge8_scoreboard import (
    nge8_sites as h_nge8_sites,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
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
from tests.test_mamari_i_3gram_090_076_020_i_only_scoreboard import (
    GRAM3 as CYCLE290_GRAM3,
    STANDING_I_3GRAM_090_076_020_I_ONLY as CYCLE290_CLAIM,
    STANDING_N_EXTRA as CYCLE290_N_EXTRA,
    STANDING_N_I as CYCLE290_N_I,
    STANDING_N_OFF_I as CYCLE290_N_OFF_I,
    TestMamariI3gram090076020IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_I_ONLY,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
    TestMamariI5gram999090076070000IOnlyScoreboard,
)
from tests.test_mamari_i_independent_076_010_079_006_700_preceded_072_scoreboard import (
    GRAM5_INDEPENDENT as CYCLE139_GRAM5,
    STANDING_I_SITES as CYCLE139_SITES,
)
from tests.test_mamari_i_leftover_999_090_076_070_remaining_5grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY as CYCLE221_I_ONLY,
    STANDING_N_SEQUENCES as CYCLE221_N_SEQUENCES,
    TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_430_076_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_ALL_I_ONLY as CYCLE331_CLAIM,
    STANDING_N_EXTRA as CYCLE331_N_EXTRA,
    TestMamariILeftoverN4RemainingAfter0900764300764gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_exactly2_430_076_scoreboard import (
    GRAM2 as CYCLE329_GRAM2,
    STANDING_G as CYCLE329_G,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_EXACTLY_2_SHARE_430_076 as CYCLE329_CLAIM,
    STANDING_K as CYCLE329_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE329_MATCHING,
    STANDING_N as CYCLE329_N,
    STANDING_N_REMAINING as CYCLE329_N_REMAINING,
    TestMamariILeftoverN4RemainingAfter090076Exactly2430076Scoreboard,
    i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_next_2gram_scoreboard import (
    STANDING_G as CYCLE328_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE328_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_UNIQUE_MAX_2GRAM as CYCLE328_UNIQUE_MAX_CLAIM,
    STANDING_K as CYCLE328_K,
    TestMamariILeftoverN4RemainingAfter090076Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_unique_max_2gram,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly2_076_020_scoreboard import (
    GRAM2 as CYCLE333_GRAM2,
    STANDING_G as CYCLE333_G,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_EXACTLY_2_SHARE_076_020 as CYCLE333_CLAIM,
    STANDING_K as CYCLE333_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE333_MATCHING,
    STANDING_N as CYCLE333_N,
    STANDING_N_REMAINING as CYCLE333_N_REMAINING,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076Exactly2076020Scoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly_2_share_076_020,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_next_2gram_scoreboard import (
    STANDING_G as CYCLE332_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE332_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_UNIQUE_MAX_2GRAM as CYCLE332_UNIQUE_MAX_CLAIM,
    STANDING_K as CYCLE332_K,
    STANDING_N as CYCLE332_N,
    STANDING_N_REMAINING as CYCLE332_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE332_N_TIED,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_unique_max_2gram,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly2_076_010_scoreboard import (
    GRAM2 as CYCLE336_GRAM2,
    STANDING_G as CYCLE336_G,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_EXACTLY_2_SHARE_076_010 as CYCLE336_CLAIM,
    STANDING_K as CYCLE336_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE336_MATCHING,
    STANDING_N as CYCLE336_N,
    STANDING_N_REMAINING as CYCLE336_N_REMAINING,
    STANDING_WITH_ROWS as CYCLE336_WITH_ROWS,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020Exactly2076010Scoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_next_2gram_scoreboard import (
    STANDING_G as CYCLE335_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE335_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_UNIQUE_MAX_2GRAM as CYCLE335_UNIQUE_MAX_CLAIM,
    STANDING_K as CYCLE335_K,
    STANDING_N as CYCLE335_N,
    STANDING_N_REMAINING as CYCLE335_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE335_N_TIED,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_unique_max_2gram,
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
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    SIDE_BR,
    SIDE_BV,
    is_contiguous_substring,
    load_b_sides,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_n_nge5_scoreboard import (
    nge5_sites,
)
from tests.test_mamari_q_nge7_scoreboard import (
    nge7_sites,
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
    STANDING_IA_SITES as CYCLE103_SITES,
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
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    load_n_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SIDE_SA,
    SIDE_SB,
    SB_LINE_NAMES,
    load_s_sides,
)

HYPOTHESIS_I_ONLY = True
GRAM2 = CYCLE336_GRAM2
NEAR_MISS_090_076 = CYCLE223_GRAM2
NEAR_MISS_430_076 = CYCLE330_GRAM2
NEAR_MISS_076_020 = CYCLE334_GRAM2
NEAR_MISS_090_076_020 = CYCLE290_GRAM3
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_076_071 = CYCLE171_GRAM2
NEAR_MISS_076_010_079_090 = ("076", "010", "079", "090")
NEAR_MISS_072_076_010_079 = ("072", "076", "010", "079")
NEAR_MISS_076_020_010_050 = ("076", "020", "010", "050")
NEAR_MISS_053_076_020_010 = ("053", "076", "020", "010")
NEAR_MISS_430_076_001_076 = ("430", "076", "001", "076")
NEAR_MISS_430_076_049_400 = ("430", "076", "049", "400")
NEAR_MISS_SPLIT_5GRAM = CYCLE139_GRAM5
STANDING_N2 = 2
STANDING_I_HITS = 11
STANDING_IA_HITS = 11
STANDING_IB_HITS = 0
STANDING_N_ON_I = 11
STANDING_N_I = 11
STANDING_I_SITES = (
    (SIDE_IA, "Ia1", 145),
    (SIDE_IA, "Ia4", 8),
    (SIDE_IA, "Ia4", 27),
    (SIDE_IA, "Ia5", 110),
    (SIDE_IA, "Ia5", 139),
    (SIDE_IA, "Ia6", 19),
    (SIDE_IA, "Ia12", 34),
    (SIDE_IA, "Ia13", 72),
    (SIDE_IA, "Ia14", 83),
    (SIDE_IA, "Ia14", 93),
    (SIDE_IA, "Ia14", 146),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_4GRAM_SITES = (
    (SIDE_IA, "Ia5", 110),
    (SIDE_IA, "Ia5", 139),
    (SIDE_IA, "Ia5", 138),
    (SIDE_IA, "Ia13", 71),
)
STANDING_LEFTOVER_MATCHING_4GRAMS = (
    NEAR_MISS_076_010_079_090,
    NEAR_MISS_076_010_079_090,
    NEAR_MISS_072_076_010_079,
    NEAR_MISS_072_076_010_079,
)
STANDING_LEFTOVER_MATCHING_SITES = (
    (SIDE_IA, "Ia5", 110),
    (SIDE_IA, "Ia5", 139),
    (SIDE_IA, "Ia13", 72),
)
STANDING_LEFTOVER_MATCHING_COUNT = 3
STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS = (
    ("076", "010", "079", "090"),
    ("076", "010", "079", "090"),
    ("076", "010", "079", "006"),
)
STANDING_EXTRA_I_SITES = (
    (SIDE_IA, "Ia1", 145),
    (SIDE_IA, "Ia4", 8),
    (SIDE_IA, "Ia4", 27),
    (SIDE_IA, "Ia6", 19),
    (SIDE_IA, "Ia12", 34),
    (SIDE_IA, "Ia14", 83),
    (SIDE_IA, "Ia14", 93),
    (SIDE_IA, "Ia14", 146),
)
STANDING_N_EXTRA = 8
STANDING_CYCLE46_2GRAM_SITES = (
    (SIDE_IA, "Ia4", 8),
    (SIDE_IA, "Ia4", 27),
    (SIDE_IA, "Ia5", 110),
)
STANDING_CYCLE46_IN_MATCHING = ((SIDE_IA, "Ia5", 110),)
STANDING_CYCLE46_IN_EXTRA = (
    (SIDE_IA, "Ia4", 8),
    (SIDE_IA, "Ia4", 27),
)
STANDING_N_CYCLE46_OVERLAP = 3
STANDING_N_CYCLE46_IN_MATCHING = 1
STANDING_N_CYCLE46_IN_EXTRA = 2
STANDING_SPLIT_5GRAM_2GRAM_SITES = (
    (SIDE_IA, "Ia6", 19),
    (SIDE_IA, "Ia13", 72),
)
STANDING_SPLIT_5GRAM_IN_MATCHING = ((SIDE_IA, "Ia13", 72),)
STANDING_SPLIT_5GRAM_IN_EXTRA = ((SIDE_IA, "Ia6", 19),)
STANDING_N_SPLIT_5GRAM_OVERLAP = 2
STANDING_N_SPLIT_5GRAM_IN_MATCHING = 1
STANDING_N_SPLIT_5GRAM_IN_EXTRA = 1
STANDING_I_PREVIOUS_4GRAMS = (
    ("072", "076", "010", "044"),
    ("071", "076", "010", "079"),
    ("071", "076", "010", "079"),
    ("071", "076", "010", "079"),
    ("072", "076", "010", "079"),
    ("630", "076", "010", "079"),
    ("071", "076", "010", "079"),
    ("072", "076", "010", "079"),
    ("071", "076", "010", "079"),
    ("107", "076", "010", "007"),
    ("430", "076", "010", "007"),
)
STANDING_I_NEXT_4GRAMS = (
    ("076", "010", "044", "027"),
    ("076", "010", "079", "071"),
    ("076", "010", "079", "522"),
    ("076", "010", "079", "090"),
    ("076", "010", "079", "090"),
    ("076", "010", "079", "006"),
    ("076", "010", "079", "029"),
    ("076", "010", "079", "006"),
    ("076", "010", "079", "053"),
    ("076", "010", "007", "400"),
    ("076", "010", "007", "090"),
)
STANDING_OFF_I_HITS = 3
STANDING_N_OFF_I = 3
STANDING_N_LEAK = 3
STANDING_OFF_I_SITES = (
    (SIDE_SB, "Sb4", 18),
    (SIDE_TA, "Ta4", 4),
    (SIDE_TA, "Ta5", 10),
)
STANDING_OFF_I_PREVIOUS_4GRAMS = (
    ("092", "076", "010", "381"),
    ("420", "076", "010", "044"),
    ("090", "076", "010", "002"),
)
STANDING_OFF_I_FOLLOWING_3GRAMS = (
    ("076", "010", "381"),
    ("076", "010", "044"),
    ("076", "010", "002"),
)
STANDING_N_T = 2
STANDING_T_SITES = (
    (SIDE_TA, "Ta4", 4),
    (SIDE_TA, "Ta5", 10),
)
STANDING_T_AMONG_LEAKS = True
STANDING_OFF_I_TABLETS_WITH_HITS = ("S", "T")
STANDING_OFF_I_BY_TABLET_NONZERO = {
    "S": 1,
    "T": 2,
}
STANDING_OFF_I_BY_TABLET = tuple(
    STANDING_OFF_I_BY_TABLET_NONZERO.get(tablet, 0) for tablet in OFF_I_TABLETS
)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS
    if tablet == "I"
    else STANDING_OFF_I_BY_TABLET_NONZERO.get(tablet, 0)
    for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_2gram_076_010_i_only"
STANDING_I_2GRAM_076_010_I_ONLY = False
STANDING_RESULT = "i_2gram_076_010_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = False
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE223_2GRAM = False
STANDING_SAME_AS_CYCLE290_3GRAM = False
STANDING_SAME_AS_CYCLE330_2GRAM = False
STANDING_SAME_AS_CYCLE334_2GRAM = False
STANDING_SAME_AS_CYCLE336 = False
STANDING_SAME_AS_CYCLE335 = False
STANDING_SAME_AS_CYCLE333 = False
STANDING_SAME_AS_CYCLE332 = False
STANDING_SAME_AS_CYCLE331 = False
STANDING_SAME_AS_CYCLE329 = False
STANDING_SAME_AS_CYCLE328 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE334 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE330 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE223 = True
STANDING_090_076_DOES_NOT_COUNT = True
STANDING_430_076_DOES_NOT_COUNT = True
STANDING_076_020_DOES_NOT_COUNT = True
STANDING_090_076_020_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_CYCLE46_5GRAM_DOES_NOT_COUNT = True
STANDING_SPLIT_5GRAM_DOES_NOT_COUNT = True
STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_ALL_I_INSIDE_FAMILY_IS_NOT_THIS_CYCLE = True
STANDING_ALL_I_INSIDE_FAMILY = False
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


def i_2gram_076_010_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


def leftover_2gram_offset(
    gram: tuple[str, ...],
    needle: tuple[str, ...] = GRAM2,
) -> int:
    """Index of contiguous G inside a leftover 4-gram."""
    width = len(needle)
    for index in range(len(gram) - width + 1):
        if gram[index : index + width] == needle:
            return index
    raise ValueError(f"{needle} is not a contiguous substring of {gram}")


def leftover_4gram_sites(
    with_rows: tuple = CYCLE336_WITH_ROWS,
) -> tuple[tuple[str, str, int], ...]:
    """I start sites of leftover remaining-after-076-020 4-grams that contain G."""
    return tuple(site for _gram, _n, _f, sites in with_rows for site in sites)


def leftover_matching_sites(
    with_rows: tuple = CYCLE336_WITH_ROWS,
    needle: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, str, int], ...]:
    """Unique I 076 010 sites inside leftover remaining-after-076-020 4-grams."""
    seen: list[tuple[str, str, int]] = []
    seen_set: set[tuple[str, str, int]] = set()
    for gram, _n, _f, sites in with_rows:
        offset = leftover_2gram_offset(gram, needle)
        for side, line, index in sites:
            site = (side, line, index + offset)
            if site not in seen_set:
                seen_set.add(site)
                seen.append(site)
    return tuple(
        sorted(seen, key=lambda site: (IA_LINE_NAMES.index(site[1]), site[2]))
    )


def leftover_matching_subset(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover matching 076 010 sites ⊆ I 076 010."""
    return set(leftover_sites).issubset(set(i_sites))


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 076 010 sites outside leftover 076 010 079 090 / 072 076 010 079."""
    leftover_set = set(leftover_matching)
    return tuple(site for site in i_sites if site not in leftover_set)


def cycle46_2gram_sites(
    cycle103_5gram_sites: tuple[tuple[str, str, int], ...] = CYCLE103_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """2-gram 076 010 sites inside cycle-46/103 999 071 076 010 079."""
    return tuple((side, line, index + 2) for side, line, index in cycle103_5gram_sites)


def named_b_sites(
    gram: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, str, int], ...]:
    """Named (side, line, index) hits on Br then Bv. Search only."""
    b = load_b_sides()
    br = tuple(
        site_tuple(hit)
        for hit in named_side_hits(b[SIDE_BR], BR_LINE_NAMES, SIDE_BR, gram)
    )
    bv = tuple(
        site_tuple(hit)
        for hit in named_side_hits(b[SIDE_BV], BV_LINE_NAMES, SIDE_BV, gram)
    )
    return br + bv


def named_off_i_sites(
    gram: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, str, int], ...]:
    """Named (side, line, index) hits on B, G, H, N, Q, S, and T."""
    gk = load_g_k_sides()
    hpq = load_q_h_p_sides()
    t = load_t_sides()
    t_sites = tuple(
        site_tuple(hit)
        for hit in named_side_hits(t[SIDE_TA], TA_LINE_NAMES, SIDE_TA, gram)
    )
    return (
        named_b_sites(gram)
        + g_nge8_sites(gram, gk)
        + h_nge8_sites(gram, hpq)
        + nge5_sites(gram, load_n_sides())
        + nge7_sites(gram, hpq)
        + nge6_sites(gram, load_s_sides())
        + t_sites
    )


class TestI2gram076010IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-336 leftover remaining 2-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 2-gram counts; a gap is not a hit. 076 020 / 430 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "010"))
        self.assertEqual(GRAM2, CYCLE336_GRAM2)
        self.assertEqual(GRAM2, CYCLE336_G)
        adjacent = [list(GRAM2), list(GRAM2)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM2), 2)
        overlap = [["076", "010", "076", "010"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM2), 2)
        gapped = [list(GRAM2[:1]) + ["020"] + list(GRAM2[1:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM2), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_430_076)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_020)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([["010", "076"]], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_010_079_090)], GRAM2), 1)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_072_076_010_079)], GRAM2), 1)
        self.assertEqual(ngram_hit_count([list(GRAM5)], GRAM2), 1)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_SPLIT_5GRAM)], GRAM2), 1)
        self.assertEqual(leftover_2gram_offset(NEAR_MISS_076_010_079_090), 0)
        self.assertEqual(leftover_2gram_offset(NEAR_MISS_072_076_010_079), 1)
        self.assertTrue(STANDING_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_430_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_020_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_020_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 11/3 loses."""
        provider = MockProvider()
        self.assertTrue(i_2gram_076_010_i_only(1, 0))
        self.assertTrue(i_2gram_076_010_i_only(11, 0))
        self.assertFalse(i_2gram_076_010_i_only(11, 3))
        self.assertFalse(i_2gram_076_010_i_only(11, 1))
        self.assertFalse(i_2gram_076_010_i_only(1, 1))
        self.assertFalse(i_2gram_076_010_i_only(0, 0))
        self.assertFalse(i_2gram_076_010_i_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "i_2gram_076_010_i_only")
        self.assertFalse(STANDING_I_2GRAM_076_010_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertNotEqual(
            STANDING_I_2GRAM_076_010_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_fail(self):
        """Leftover matching ⊆ I sites; extra I is nonempty and recorded."""
        provider = MockProvider()
        self.assertTrue(
            leftover_matching_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(leftover_matching_sites(), STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(leftover_4gram_sites(), STANDING_LEFTOVER_4GRAM_SITES)
        self.assertEqual(extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(len(extra_i_sites()), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 8)
        self.assertEqual(
            STANDING_N_I,
            STANDING_LEFTOVER_MATCHING_COUNT + STANDING_N_EXTRA,
        )
        self.assertEqual(3 + 8, 11)
        self.assertNotEqual(STANDING_N_EXTRA, 0)
        self.assertFalse(STANDING_ALL_I_INSIDE_FAMILY)
        planted_foreign = (SIDE_IA, "Ia99", 999)
        planted_extra = STANDING_I_SITES + (planted_foreign,)
        self.assertFalse(
            leftover_matching_subset(
                STANDING_LEFTOVER_MATCHING_SITES + (planted_foreign,),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(len(extra_i_sites(planted_extra)), 9)
        dropped = tuple(
            site for site in STANDING_I_SITES if site != STANDING_LEFTOVER_MATCHING_SITES[0]
        )
        self.assertFalse(
            leftover_matching_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                dropped,
            )
        )
        self.assertEqual(cycle46_2gram_sites(), STANDING_CYCLE46_2GRAM_SITES)
        self.assertEqual(CYCLE139_SITES, STANDING_SPLIT_5GRAM_2GRAM_SITES)
        self.assertEqual(provider.get_call_history(), [])

    def test_2gram_is_cycle336_g_not_the_cycle_103_5gram(self):
        """2-gram is cycle-336 G, not 076 020, 430 076, 090 076, or the 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM2, CYCLE336_GRAM2)
        self.assertEqual(GRAM2, CYCLE336_G)
        self.assertNotEqual(GRAM2, CYCLE334_GRAM2)
        self.assertNotEqual(GRAM2, CYCLE330_GRAM2)
        self.assertNotEqual(GRAM2, CYCLE223_GRAM2)
        self.assertNotEqual(GRAM2, CYCLE290_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM5))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_SPLIT_5GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE223_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE290_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE330_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE334_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE336)
        self.assertFalse(STANDING_SAME_AS_CYCLE335)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE334)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE330)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE223)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N2, 2)
        self.assertLess(len(GRAM2), 8)
        for leftover in CYCLE336_MATCHING:
            self.assertTrue(is_contiguous_substring(GRAM2, leftover))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_076_010_079_090))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_072_076_010_079))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_076_020))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_090_076))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_430_076))
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_ALL_I_INSIDE_FAMILY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_CYCLE46_5GRAM_DOES_NOT_COUNT)
        self.assertTrue(STANDING_SPLIT_5GRAM_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI2gram076010IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover remaining 2-gram 076 010 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM2)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.leftover_matching = leftover_matching_sites()
        self.leftover_4grams = leftover_4gram_sites()
        self.extra = extra_i_sites(self.i_sites, self.leftover_matching)
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM2, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM2, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.off_i_sites = named_off_i_sites(GRAM2)
        self.claim_holds = i_2gram_076_010_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_336_g_not_retuned(self):
        """2-gram is the cycle-336 leftover remaining G, not a new inventory."""
        self.assertEqual(GRAM2, CYCLE336_GRAM2)
        self.assertEqual(GRAM2, ("076", "010"))
        self.assertEqual(GRAM2, CYCLE336_G)
        prior_336 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly2_076_010"
        ]
        self.assertEqual(prior_336["cycle"], 336)
        self.assertEqual(tuple(prior_336["tokens2"]), GRAM2)
        self.assertEqual(tuple(prior_336["G"]), CYCLE336_G)
        self.assertEqual(prior_336["K"], CYCLE336_K)
        self.assertEqual(prior_336["K"], 2)
        self.assertEqual(prior_336["N"], CYCLE336_N)
        self.assertEqual(prior_336["N"], 7)
        self.assertEqual(prior_336["N_remaining"], CYCLE336_N_REMAINING)
        self.assertEqual(prior_336["N_remaining"], 5)
        measured_matching = [list(gram) for gram in CYCLE336_MATCHING]
        self.assertEqual(prior_336["matching_leftovers"], measured_matching)
        self.assertTrue(
            prior_336[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010"
            ]
        )
        self.assertTrue(prior_336["i_vs_off_i_is_not_this_cycle"])
        self.assertTrue(prior_336["twogram_i_only_is_not_this_cycle"])
        self.assertNotIn("N_I", prior_336)
        self.assertNotIn("N_off_I", prior_336)
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertNotEqual(GRAM2, CYCLE334_GRAM2)
        self.assertNotEqual(GRAM2, CYCLE330_GRAM2)
        self.assertNotEqual(GRAM2, CYCLE223_GRAM2)
        self.assertNotEqual(GRAM2, CYCLE290_GRAM3)
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_ALL_I_INSIDE_FAMILY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_CYCLE336_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_eleven_on_ia_with_extra_i(self):
        """2-gram is 11 on Ia; Ib unpublished 0. Extra I is 8. N_I must not drift."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 11)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 11)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 11)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM2, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM2), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 3)
        self.assertEqual(self.leftover_4grams, STANDING_LEFTOVER_4GRAM_SITES)
        self.assertEqual(len(self.leftover_4grams), 4)
        self.assertTrue(leftover_matching_subset(self.leftover_matching, self.i_sites))
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 8)
        self.assertEqual(
            self.i_hits,
            STANDING_LEFTOVER_MATCHING_COUNT + STANDING_N_EXTRA,
        )
        self.assertNotEqual(STANDING_N_EXTRA, 0)
        self.assertFalse(STANDING_ALL_I_INSIDE_FAMILY)
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N2]
            self.assertEqual(tuple(stems), GRAM2)
            self.assertEqual(side, SIDE_IA)
            self.assertNotEqual(line[:2], "Ib")
        for site, leftover4 in zip(
            STANDING_LEFTOVER_4GRAM_SITES,
            STANDING_LEFTOVER_MATCHING_4GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), leftover4)
            offset = leftover_2gram_offset(leftover4)
            two = (side, line, index + offset)
            self.assertIn(two, STANDING_LEFTOVER_MATCHING_SITES)
            self.assertIn(two, STANDING_I_SITES)
            self.assertNotIn(two, STANDING_EXTRA_I_SITES)
        for site, next4 in zip(
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), next4)
            self.assertIn(site, STANDING_I_SITES)
            self.assertNotIn(site, STANDING_EXTRA_I_SITES)
        for site, prev4, next4 in zip(
            STANDING_I_SITES,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index - 1 : index + 3]), prev4)
            self.assertEqual(tuple(stems[index : index + 4]), next4)
        self.assertEqual(cycle46_2gram_sites(), STANDING_CYCLE46_2GRAM_SITES)
        self.assertEqual(STANDING_N_CYCLE46_OVERLAP, 3)
        self.assertEqual(STANDING_N_CYCLE46_IN_MATCHING, 1)
        self.assertEqual(STANDING_N_CYCLE46_IN_EXTRA, 2)
        for site in STANDING_CYCLE46_2GRAM_SITES:
            self.assertIn(site, STANDING_I_SITES)
        for site in STANDING_CYCLE46_IN_MATCHING:
            self.assertIn(site, STANDING_LEFTOVER_MATCHING_SITES)
            self.assertNotIn(site, STANDING_EXTRA_I_SITES)
        for site in STANDING_CYCLE46_IN_EXTRA:
            self.assertIn(site, STANDING_EXTRA_I_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(CYCLE139_SITES, STANDING_SPLIT_5GRAM_2GRAM_SITES)
        self.assertEqual(STANDING_N_SPLIT_5GRAM_OVERLAP, 2)
        self.assertEqual(STANDING_N_SPLIT_5GRAM_IN_MATCHING, 1)
        self.assertEqual(STANDING_N_SPLIT_5GRAM_IN_EXTRA, 1)
        for site in STANDING_SPLIT_5GRAM_2GRAM_SITES:
            self.assertIn(site, STANDING_I_SITES)
        for site in STANDING_SPLIT_5GRAM_IN_MATCHING:
            self.assertIn(site, STANDING_LEFTOVER_MATCHING_SITES)
            self.assertNotIn(site, STANDING_EXTRA_I_SITES)
        for site in STANDING_SPLIT_5GRAM_IN_EXTRA:
            self.assertIn(site, STANDING_EXTRA_I_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(
            STANDING_I_SITES[0],
            (SIDE_IA, "Ia1", 145),
        )
        self.assertEqual(
            STANDING_I_SITES[3],
            (SIDE_IA, "Ia5", 110),
        )
        self.assertEqual(
            STANDING_I_SITES[10],
            (SIDE_IA, "Ia14", 146),
        )
        self.assertFalse(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_2gram_is_three_off_i_and_not_i_only(self):
        """2-gram is 3 off-I on S and T including T Ta4[4]/Ta5[10]. Claim loses."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, STANDING_N_LEAK)
        self.assertEqual(STANDING_N_OFF_I, 3)
        self.assertNotEqual(STANDING_N_OFF_I, 0)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(len(STANDING_OFF_I_SITES), STANDING_N_OFF_I)
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ("S", "T"))
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {"S": 1, "T": 2})
        self.assertEqual(STANDING_N_T, 2)
        self.assertEqual(STANDING_T_SITES, ((SIDE_TA, "Ta4", 4), (SIDE_TA, "Ta5", 10)))
        self.assertTrue(STANDING_T_AMONG_LEAKS)
        for site in STANDING_T_SITES:
            self.assertIn(site, STANDING_OFF_I_SITES)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM2))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 11)
            elif tablet in STANDING_OFF_I_BY_TABLET_NONZERO:
                self.assertEqual(count, STANDING_OFF_I_BY_TABLET_NONZERO[tablet])
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM2), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM2), 0)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM2), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM2), 1)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM2), 2)
        b = load_b_sides()
        self.assertEqual(ngram_hit_count(b[SIDE_BR], GRAM2), 0)
        self.assertEqual(ngram_hit_count(b[SIDE_BV], GRAM2), 0)
        side_stems = {
            SIDE_SB: (s_sides[SIDE_SB], SB_LINE_NAMES),
            SIDE_TA: (t_sides[SIDE_TA], TA_LINE_NAMES),
        }
        for (side, line, index), prev4, follow3 in zip(
            STANDING_OFF_I_SITES,
            STANDING_OFF_I_PREVIOUS_4GRAMS,
            STANDING_OFF_I_FOLLOWING_3GRAMS,
            strict=True,
        ):
            stems, names = side_stems[side]
            line_stems = stems[names.index(line)]
            self.assertEqual(tuple(line_stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(line_stems[index - 1 : index + 3]), prev4)
            self.assertEqual(tuple(line_stems[index : index + 3]), follow3)
        self.assertEqual(
            i_2gram_076_010_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_2GRAM_076_010_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_2GRAM_076_010_I_ONLY,
        )
        self.assertFalse(self.claim_holds)
        self.assertFalse(STANDING_I_2GRAM_076_010_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_2gram_076_010_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE223_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE290_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE330_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE334_2GRAM)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_ALL_I_INSIDE_FAMILY_IS_NOT_THIS_CYCLE)
        self.assertFalse(STANDING_ALL_I_INSIDE_FAMILY)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_336_335_334_333_332_331_330_329_328_223_222_and_220_scoreboards_still_compute(self):
        """Cycle 336 K=2, 335 unique-max lose, 334 12/0, 330 30/16, 223 69/3 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, CYCLE223_GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        self.assertTrue(CYCLE222_CLAIM)
        prior_336 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020Exactly2076010Scoreboard()
        )
        prior_336.setUp()
        prior_336.test_remaining_after_7_exactly_2_share_076_010_holds()
        prior_336.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE336_K, 2)
        self.assertEqual(CYCLE336_G, GRAM2)
        self.assertTrue(CYCLE336_CLAIM)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010(
                leftover
            )
        )
        if not prior_336.claim_holds:
            self.fail(
                "nested cycle 336 leftover remaining-after-076-020 exactly-2-share-076 010 drifted"
            )
        prior_335 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020Next2gramScoreboard()
        )
        prior_335.setUp()
        prior_335.test_remaining_after_7_unique_max_loses()
        prior_335.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE335_K, 2)
        self.assertEqual(CYCLE335_G, GRAM2)
        self.assertEqual(CYCLE335_N, 7)
        self.assertEqual(CYCLE335_N_REMAINING, 5)
        self.assertEqual(CYCLE335_N_TIED, 2)
        self.assertFalse(CYCLE335_UNIQUE)
        self.assertFalse(CYCLE335_UNIQUE_MAX_CLAIM)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_unique_max_2gram(
                leftover
            )
        )
        if prior_335.claim_holds:
            self.fail("nested cycle 335 remaining-after-076-020 unique-max drifted")
        prior_334 = TestMamariI2gram076020IOnlyScoreboard()
        prior_334.setUp()
        prior_334.test_2gram_is_zero_off_i_and_i_only()
        prior_334.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE334_N_I, 12)
        self.assertEqual(CYCLE334_N_OFF_I, 0)
        self.assertEqual(CYCLE334_N_EXTRA, 9)
        self.assertEqual(CYCLE334_GRAM2, CYCLE333_G)
        self.assertTrue(CYCLE334_CLAIM)
        self.assertTrue(i_2gram_076_020_i_only(12, 0))
        if not prior_334.claim_holds:
            self.fail("nested cycle 334 2-gram 076 020 I-only 12/0 drifted")
        prior_333 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076Exactly2076020Scoreboard()
        )
        prior_333.setUp()
        prior_333.test_remaining_after_9_exactly_2_share_076_020_holds()
        prior_333.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE333_K, 2)
        self.assertEqual(CYCLE333_G, CYCLE334_GRAM2)
        self.assertEqual(CYCLE333_N, 9)
        self.assertEqual(CYCLE333_N_REMAINING, 7)
        self.assertTrue(CYCLE333_CLAIM)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly_2_share_076_020(
                leftover
            )
        )
        if not prior_333.claim_holds:
            self.fail(
                "nested cycle 333 leftover remaining-after-430-076 exactly-2-share-076 020 drifted"
            )
        prior_332 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076Next2gramScoreboard()
        )
        prior_332.setUp()
        prior_332.test_remaining_after_9_unique_max_loses()
        prior_332.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE332_K, 2)
        self.assertEqual(CYCLE332_G, CYCLE334_GRAM2)
        self.assertEqual(CYCLE332_N, 9)
        self.assertEqual(CYCLE332_N_REMAINING, 7)
        self.assertEqual(CYCLE332_N_TIED, 4)
        self.assertFalse(CYCLE332_UNIQUE)
        self.assertFalse(CYCLE332_UNIQUE_MAX_CLAIM)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_unique_max_2gram(
                leftover
            )
        )
        if prior_332.claim_holds:
            self.fail("nested cycle 332 remaining-after-430-076 unique-max drifted")
        prior_331 = TestMamariILeftoverN4RemainingAfter0900764300764gramsIOnlyScoreboard()
        prior_331.setUp()
        prior_331.test_each_4gram_is_two_on_i_zero_off_i_not_hapax_and_claim_holds()
        prior_331.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE331_CLAIM)
        self.assertEqual(CYCLE331_N_EXTRA, 0)
        if not prior_331.claim_holds:
            self.fail("nested cycle 331 leftover 430 076 4-grams all I-only drifted")
        prior_330 = TestMamariI2gram430076IOnlyScoreboard()
        prior_330.setUp()
        prior_330.test_2gram_is_sixteen_off_i_and_not_i_only()
        prior_330.test_survey_matches_computed_lock()
        self.assertEqual(prior_330.i_hits, CYCLE330_N_I)
        self.assertEqual(prior_330.i_hits, 30)
        self.assertEqual(prior_330.off_i_hits, CYCLE330_N_OFF_I)
        self.assertEqual(prior_330.off_i_hits, 16)
        self.assertEqual(CYCLE330_N_EXTRA, 26)
        self.assertFalse(prior_330.claim_holds)
        self.assertFalse(CYCLE330_CLAIM)
        self.assertFalse(i_2gram_430_076_i_only(30, 16))
        if prior_330.i_hits != 30 or prior_330.off_i_hits != 16:
            self.fail("nested cycle 330 430 076 I-only 30/16 drifted")
        prior_329 = TestMamariILeftoverN4RemainingAfter090076Exactly2430076Scoreboard()
        prior_329.setUp()
        prior_329.test_remaining_after_11_exactly_2_share_430_076_holds()
        prior_329.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE329_K, 2)
        self.assertEqual(CYCLE329_G, CYCLE330_GRAM2)
        self.assertEqual(CYCLE329_N, 11)
        self.assertEqual(CYCLE329_N_REMAINING, 9)
        self.assertEqual(CYCLE329_MATCHING, (
            ("430", "076", "001", "076"),
            ("430", "076", "049", "400"),
        ))
        self.assertTrue(CYCLE329_CLAIM)
        self.assertTrue(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(leftover))
        if not prior_329.claim_holds:
            self.fail("nested cycle 329 leftover remaining-after-090-076 exactly-2-share-430 076 drifted")
        prior_328 = TestMamariILeftoverN4RemainingAfter090076Next2gramScoreboard()
        prior_328.setUp()
        prior_328.test_remaining_after_11_unique_max_loses()
        prior_328.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE328_K, 2)
        self.assertEqual(CYCLE328_G, CYCLE329_GRAM2)
        self.assertFalse(CYCLE328_UNIQUE)
        self.assertFalse(CYCLE328_UNIQUE_MAX_CLAIM)
        self.assertFalse(i_leftover_n4_remaining_after_090_076_unique_max_2gram(leftover))
        if prior_328.claim_holds:
            self.fail("nested cycle 328 remaining-after-090-076 unique-max drifted")
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
        prior_290 = TestMamariI3gram090076020IOnlyScoreboard()
        prior_290.setUp()
        prior_290.test_3gram_is_zero_off_i_and_i_only()
        prior_290.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE290_N_I, 4)
        self.assertEqual(CYCLE290_N_OFF_I, 0)
        self.assertEqual(CYCLE290_N_EXTRA, 0)
        self.assertTrue(CYCLE290_CLAIM)
        if CYCLE290_N_I != 4 or CYCLE290_N_OFF_I != 0 or CYCLE290_N_EXTRA != 0:
            self.fail("nested cycle 290 leftover n=4 remaining 090 076 020 I-only 4/0 drifted")
        prior_221 = TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard()
        prior_221.setUp()
        prior_221.test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_221.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE221_N_SEQUENCES, 4)
        self.assertTrue(CYCLE221_I_ONLY)
        if not prior_221.claim_holds:
            self.fail("nested cycle 221 remaining 5-grams 4/4 I-only drifted")
        prior_220 = TestMamariI5gram999090076070000IOnlyScoreboard()
        prior_220.setUp()
        prior_220.test_5gram_is_zero_off_i_and_i_only()
        prior_220.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE220_N_I, 1)
        self.assertEqual(CYCLE220_N_OFF_I, 0)
        self.assertTrue(CYCLE220_I_ONLY)
        if CYCLE220_N_I != 1 or CYCLE220_N_OFF_I != 0:
            self.fail("nested cycle 220 leftover 000 5-gram 1/0 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_CYCLE335_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE334_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE333_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE332_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE331_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE330_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE329_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE328_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE222_DOES_NOT_COUNT)
        self.assertTrue(STANDING_I_SITE_PEEL_288_327_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_DO_NOT_COUNT)
        self.assertTrue(STANDING_CYCLES_220_221_DO_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE223_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-337 2-gram I-only loss."""
        lock = self.survey["i_2gram_076_010_i_only"]
        self.assertEqual(lock["cycle"], 337)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 11)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_4gram_sites"]),
            STANDING_LEFTOVER_4GRAM_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_4grams"]),
            STANDING_LEFTOVER_MATCHING_4GRAMS,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(lock["leftover_matching_count"], 3)
        self.assertTrue(lock["leftover_matching_subset_of_i_sites"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_next_4grams"]),
            STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 8)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle46_2gram_sites"]),
            STANDING_CYCLE46_2GRAM_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle46_in_matching"]),
            STANDING_CYCLE46_IN_MATCHING,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle46_in_extra"]),
            STANDING_CYCLE46_IN_EXTRA,
        )
        self.assertEqual(lock["N_cycle46_overlap"], 3)
        self.assertEqual(lock["N_cycle46_in_matching"], 1)
        self.assertEqual(lock["N_cycle46_in_extra"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["split_5gram_2gram_sites"]),
            STANDING_SPLIT_5GRAM_2GRAM_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["split_5gram_in_matching"]),
            STANDING_SPLIT_5GRAM_IN_MATCHING,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["split_5gram_in_extra"]),
            STANDING_SPLIT_5GRAM_IN_EXTRA,
        )
        self.assertEqual(lock["N_split_5gram_overlap"], 2)
        self.assertEqual(lock["N_split_5gram_in_matching"], 1)
        self.assertEqual(lock["N_split_5gram_in_extra"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_previous_4grams"]),
            STANDING_I_PREVIOUS_4GRAMS,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_next_4grams"]),
            STANDING_I_NEXT_4GRAMS,
        )
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 3)
        self.assertEqual(lock["N_leak"], STANDING_N_LEAK)
        self.assertEqual(
            tuple(tuple(row) for row in lock["off_i_sites"]),
            STANDING_OFF_I_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["off_i_previous_4grams"]),
            STANDING_OFF_I_PREVIOUS_4GRAMS,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["off_i_following_3grams"]),
            STANDING_OFF_I_FOLLOWING_3GRAMS,
        )
        self.assertEqual(lock["N_T"], STANDING_N_T)
        self.assertEqual(lock["N_T"], 2)
        self.assertEqual(tuple(tuple(row) for row in lock["t_sites"]), STANDING_T_SITES)
        self.assertTrue(lock["t_among_leaks"])
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
        self.assertFalse(lock["i_2gram_076_010_i_only"])
        self.assertEqual(
            lock["i_2gram_076_010_i_only"],
            STANDING_I_2GRAM_076_010_I_ONLY,
        )
        self.assertFalse(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle223_2gram"])
        self.assertFalse(lock["same_as_cycle290_3gram"])
        self.assertFalse(lock["same_as_cycle330_2gram"])
        self.assertFalse(lock["same_as_cycle334_2gram"])
        self.assertFalse(lock["same_as_cycle336"])
        self.assertFalse(lock["same_as_cycle335"])
        self.assertFalse(lock["same_as_cycle333"])
        self.assertFalse(lock["same_as_cycle332"])
        self.assertFalse(lock["same_as_cycle331"])
        self.assertFalse(lock["same_as_cycle329"])
        self.assertFalse(lock["same_as_cycle328"])
        self.assertTrue(lock["same_claim_shape_as_cycle334"])
        self.assertTrue(lock["same_claim_shape_as_cycle330"])
        self.assertTrue(lock["same_claim_shape_as_cycle223"])
        self.assertTrue(lock["090_076_does_not_count"])
        self.assertTrue(lock["430_076_does_not_count"])
        self.assertTrue(lock["076_020_does_not_count"])
        self.assertTrue(lock["090_076_020_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["cycle46_5gram_does_not_count"])
        self.assertTrue(lock["split_5gram_does_not_count"])
        self.assertTrue(lock["leftover_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["all_i_inside_family_is_not_this_cycle"])
        self.assertFalse(lock["all_i_inside_family"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
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
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly2_076_010_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_next_2gram_unchanged"]
        )
        self.assertTrue(lock["standing_i_2gram_076_020_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly2_076_020_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_next_2gram_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_after_090_076_430_076_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_430_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_after_090_076_exactly2_430_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_after_090_076_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_020_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_999_090_076_070_remaining_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_5gram_999_090_076_070_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertTrue(lock["nested_cycle336_exactly_2_share_076_010"])
        self.assertEqual(lock["nested_cycle336_K"], 2)
        self.assertEqual(lock["nested_cycle336_N"], 7)
        self.assertEqual(lock["nested_cycle336_N_remaining"], 5)
        self.assertTrue(lock["nested_cycle335_unique_max_false"])
        self.assertFalse(lock["nested_cycle335_unique_max"])
        self.assertEqual(lock["nested_cycle335_K"], 2)
        self.assertEqual(lock["nested_cycle335_N_tied_at_k"], 2)
        self.assertTrue(lock["nested_cycle334_i_2gram_076_020_i_only"])
        self.assertEqual(lock["nested_cycle334_N_I"], 12)
        self.assertEqual(lock["nested_cycle334_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle334_N_extra"], 9)
        self.assertTrue(lock["nested_cycle333_exactly_2_share_076_020"])
        self.assertEqual(lock["nested_cycle333_K"], 2)
        self.assertEqual(lock["nested_cycle333_N"], 9)
        self.assertEqual(lock["nested_cycle333_N_remaining"], 7)
        self.assertFalse(lock["nested_cycle332_unique_max"])
        self.assertEqual(lock["nested_cycle332_K"], 2)
        self.assertEqual(lock["nested_cycle332_N_tied_at_k"], 4)
        self.assertTrue(lock["nested_cycle331_4grams_all_i_only"])
        self.assertEqual(lock["nested_cycle331_N_extra"], 0)
        self.assertFalse(lock["nested_cycle330_i_2gram_430_076_i_only"])
        self.assertEqual(lock["nested_cycle330_N_I"], 30)
        self.assertEqual(lock["nested_cycle330_N_off_I"], 16)
        self.assertEqual(lock["nested_cycle330_N_extra"], 26)
        self.assertTrue(lock["nested_cycle329_exactly_2_share_430_076"])
        self.assertEqual(lock["nested_cycle329_K"], 2)
        self.assertEqual(lock["nested_cycle329_N_remaining"], 9)
        self.assertFalse(lock["nested_cycle328_unique_max"])
        self.assertEqual(lock["nested_cycle328_K"], 2)
        self.assertEqual(lock["nested_cycle328_N_tied_at_k"], 5)
        prior_336 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly2_076_010"
        ]
        self.assertEqual(prior_336["cycle"], 336)
        self.assertTrue(
            prior_336[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010"
            ]
        )
        self.assertEqual(tuple(prior_336["G"]), ("076", "010"))
        self.assertEqual(prior_336["K"], 2)
        self.assertEqual(prior_336["N"], 7)
        self.assertTrue(prior_336["i_vs_off_i_is_not_this_cycle"])
        prior_335 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_next_2gram"
        ]
        self.assertEqual(prior_335["cycle"], 335)
        self.assertFalse(
            prior_335[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_unique_max_2gram"
            ]
        )
        self.assertFalse(prior_335["unique_max"])
        self.assertEqual(prior_335["N"], 7)
        self.assertEqual(prior_335["K"], 2)
        self.assertEqual(tuple(prior_335["G"]), ("076", "010"))
        self.assertEqual(prior_335["N_remaining"], 5)
        self.assertEqual(prior_335["N_distinct"], 19)
        self.assertEqual(prior_335["N_tied_at_k"], 2)
        prior_334 = self.survey["i_2gram_076_020_i_only"]
        self.assertEqual(prior_334["cycle"], 334)
        self.assertTrue(prior_334["i_2gram_076_020_i_only"])
        self.assertEqual(prior_334["N_I"], 12)
        self.assertEqual(prior_334["N_off_I"], 0)
        self.assertEqual(prior_334["N_extra"], 9)
        prior_333 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly2_076_020"
        ]
        self.assertEqual(prior_333["cycle"], 333)
        self.assertTrue(
            prior_333[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly_2_share_076_020"
            ]
        )
        self.assertEqual(tuple(prior_333["G"]), ("076", "020"))
        self.assertEqual(prior_333["K"], 2)
        self.assertEqual(prior_333["N"], 9)
        prior_332 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_next_2gram"
        ]
        self.assertEqual(prior_332["cycle"], 332)
        self.assertFalse(
            prior_332["i_leftover_n4_remaining_after_090_076_remaining_after_430_076_unique_max_2gram"]
        )
        self.assertFalse(prior_332["unique_max"])
        self.assertEqual(prior_332["N"], 9)
        self.assertEqual(prior_332["K"], 2)
        self.assertEqual(tuple(prior_332["G"]), ("076", "020"))
        self.assertEqual(prior_332["N_remaining"], 7)
        self.assertEqual(prior_332["N_distinct"], 23)
        self.assertEqual(prior_332["N_tied_at_k"], 4)
        prior_331 = self.survey["i_leftover_n4_remaining_after_090_076_430_076_4grams_i_only"]
        self.assertEqual(prior_331["cycle"], 331)
        self.assertTrue(prior_331["i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only"])
        self.assertEqual(prior_331["N_extra"], 0)
        prior_330 = self.survey["i_2gram_430_076_i_only"]
        self.assertEqual(prior_330["cycle"], 330)
        self.assertFalse(prior_330["i_2gram_430_076_i_only"])
        self.assertEqual(prior_330["N_I"], 30)
        self.assertEqual(prior_330["N_off_I"], 16)
        self.assertEqual(prior_330["N_extra"], 26)
        prior_329 = self.survey["i_leftover_n4_remaining_after_090_076_exactly2_430_076"]
        self.assertEqual(prior_329["cycle"], 329)
        self.assertTrue(prior_329["i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076"])
        self.assertEqual(tuple(prior_329["G"]), ("430", "076"))
        self.assertEqual(prior_329["K"], 2)
        self.assertEqual(prior_329["N"], 11)
        self.assertEqual(prior_329["N_remaining"], 9)
        prior_328 = self.survey["i_leftover_n4_remaining_after_090_076_next_2gram"]
        self.assertEqual(prior_328["cycle"], 328)
        self.assertFalse(prior_328["i_leftover_n4_remaining_after_090_076_unique_max_2gram"])
        self.assertFalse(prior_328["unique_max"])
        self.assertEqual(prior_328["K"], 2)
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertEqual(tuple(prior_222["G"]), ("090", "076"))
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(prior_222["N_remaining"], 16)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], CYCLE223_N_I)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], CYCLE223_N_OFF_I)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["cycle"], 290)
        self.assertTrue(self.survey["i_3gram_090_076_020_i_only"]["i_3gram_090_076_020_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["N_I"], 4)
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["N_extra"], 0)
        self.assertEqual(self.survey["i_leftover_999_090_076_070_remaining_5grams_i_only"]["cycle"], 221)
        self.assertTrue(
            self.survey["i_leftover_999_090_076_070_remaining_5grams_i_only"][
                "i_leftover_999_090_076_070_remaining_5grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_5gram_999_090_076_070_000_i_only"]["cycle"], 220)
        self.assertTrue(self.survey["i_5gram_999_090_076_070_000_i_only"]["i_5gram_999_090_076_070_000_i_only"])
        peel_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(peel_288["cycle"], 288)
        self.assertEqual(peel_288["N_inside"], 13)
        self.assertEqual(peel_288["G"], "020")
        self.assertEqual(peel_288["K"], 4)
        extra = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(extra["cycle"], 225)
        self.assertEqual(extra["N_leftover"], 56)
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
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_freq"], 3)
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


class TestMamariI2gram076010IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 337 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
