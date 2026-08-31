"""I's leftover n=4 remaining remaining-after-090-076 remaining-after-430-076 remaining-after-076-020 remaining-after-076-010 vs next 2-gram.

Cycle 339 text-search lock. Uses already-vendored A–V and the
cycle-136 leftover n=4 maximal set (27 independent n=4 grams
that are not substrings of the four I 5-grams). Does not retune
that set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Population (locked, do not re-derive as a new claim): leftover
n=4 remaining remaining-after-090-076 remaining-after-430-076
remaining-after-076-020 remaining-after-076-010. Leftover n=4
remaining remaining-after-090-076 = N=11 leftover 4-grams that
do not contain 090 076. Cycle 328 LOSE unique most frequent
2-gram (5-way tie at K=2, G=430 076 largest-id). Cycle 329
HOLD: exactly 2 contain contiguous 430 076. Cycle 330 LOSE:
2-gram 430 076 is not I-only. Cycle 331 HOLD: leftover
4-grams that contain 430 076 are all I-only (extra I of those
4-grams=0). Cycle 332 LOSE unique most frequent 2-gram among
remaining-after-430-076 (N=9 leftover 4-grams that do not
contain 090 076 and do not contain contiguous 430 076).
unique_max false, 4-way tie at K=2: 076 020 / 076 010 /
020 010 / 010 079. G=076 020 largest-id labeling only.
Matching leftovers of labeled G: 076 020 010 050,
053 076 020 010. N_remaining after peeling G=7. Cycle 333
HOLD: exactly K=2 of those N=9 contain contiguous 076 020,
matching leftovers as labeled, N_remaining=7. Nested cycle
332 unique_max false stays nested. Cycle 334 HOLD: 2-gram
076 020 is I-only (N_I=12, N_off_I=0 / N_leak=0, leftover
matching sites 3 unique 2-gram sites Ia2[120]/Ia12[1]/
Ia14[110], extra I=9). Extra I ≠ 0 so all-inside-family is
false (skip analog of cycle 224). Leftover 4-grams that
contain 076 020 are I-only by implication of the 2-gram
I-only lock; do not spend a cycle re-locking that tautology
(unlike cycle 331, which was needed because cycle 330 2-gram
leaked). Extra-I 4-grams of 076 020 I-only is the same
tautology; skip. Nested leftover n=4 remaining I 090 076 020
peels stay nested. Cycle 335 LOSE unique most frequent
2-gram among remaining-after-076-020 (N=7 leftover 4-grams
that do not contain 090 076, do not contain contiguous
430 076, and do not contain contiguous 076 020). unique_max
false, 2-way tie at K=2: 076 010 / 010 079. G=076 010
largest-id labeling only. Matching leftovers of labeled G:
076 010 079 090, 072 076 010 079. N_remaining after peeling
G=5. Cycle 336 HOLD: exactly K=2 of those N=7 contain
contiguous 076 010, matching leftovers as labeled,
N_remaining=5. Nested cycle 335 unique_max false stays
nested. Cycle 337 LOSE: 2-gram 076 010 is not I-only
(N_I=11, N_off_I=3 including T at Ta4[4]/Ta5[10] plus S at
Sb4[18], extra I=8, leftover matching sites 3). Extra I ≠ 0
is recorded, not this cycle's claim. Do not re-lock 2-gram
I-only or all-I-inside-family (all-inside is false by extra
I=8). Cycle 338 HOLD: leftover 4-grams that contain 076 010
are all I-only (076 010 079 090 N_I=2 N_off_I=0 at
Ia5[110]/Ia5[139]; 072 076 010 079 N_I=2 N_off_I=0 at
Ia5[138]/Ia13[71]; extra I of the 4-grams=0, not hapax).
Nested cycle 337 2-gram leak stays nested (2-gram can leak
while 4-grams do not). Extra-I peel of those 4-grams is
closed (extra I=0). This cycle's N=5 population is leftover
n=4 remaining remaining-after-090-076 remaining-after-430-076
remaining-after-076-020 remaining-after-076-010: the 5 leftover
4-grams that do not contain 090 076, do not contain contiguous
430 076, do not contain contiguous 076 020, and do not contain
contiguous 076 010.

Already locked (do not re-lock): cycle 338, 337, 336, 335,
334, 333, 332, 331, 330, 329, 328, 222, leftover n=4 remaining
I 090 076 peels (288–327), leftover extra 090 076 peels,
cycles 220–221, or cycle 223. Do not claim leftover 4-gram
I-only or extra-I 4-gram I-only of 076 010 this cycle.

This cycle is leftover-inventory, not I-only of G. For each
remaining-after-076-010 leftover 4-gram, list its three
contiguous 2-grams. Count how many of the 5 contain each
2-gram (contain = the 2-gram is a substring of that leftover
4-gram). G = the 2-gram with the highest remaining-after-
076-010 leftover count. If a tie, pick the one whose first
token is the larger Barthel id, then the larger second token
(labeling only when unique_max is false). K = that count.

Prefer the unique-max 2-gram lock first (same shape as cycle
335 leftover n=4 remaining remaining-after-090-076 remaining-
after-430-076 remaining-after-076-020 unique most frequent
2-gram, which LOSE 2-way tie). Also analog cycle 332 leftover
n=4 remaining remaining-after-090-076 remaining-after-430-076
unique most frequent 2-gram (LOSE 4-way tie) and cycle 328
leftover n=4 remaining remaining-after-090-076 unique most
frequent 2-gram (LOSE 5-way tie). HOLD iff unique_max is true
(one 2-gram strictly outcounts every other among those 5).
LOSE on a tie (unique_max false), including a hapax pile. G
is largest-id labeling only on a tie; do not treat labeled G
as unique-max. Empty remainder does not lose HOLD.

Measured: N=5, N_distinct=15, hapax pile 15-way tie at K=1,
G=999 604 by largest-id tie-break, unique-max false. Matching
leftovers of the labeled G: 071 999 604 076. N_remaining after
peeling G = 4 (5−1). I vs off-I of G is not this cycle.
Nested cycle 338 leftover 4-grams all I-only 2/0 extra I=0,
cycle 337 2-gram 076 010 I-only 11/3 extra I=8, cycle 336
exactly-2-share 076 010, cycle 335 unique_max false, cycle
334 2-gram 076 020 I-only 12/0 extra I=9, cycle 333
exactly-2-share 076 020, cycle 332 unique_max false, cycle
331 leftover 4-grams all I-only 2/0 extra I=0, cycle 330
2-gram 430 076 I-only 30/16 extra I=26, cycle 329
exactly-2-share 430 076, cycle 328 unique_max false, cycle
222 leftover remaining K=5 / G=090 076 / N_without=11,
leftover n=4 remaining I 090 076 peel 288–327, leftover extra
090 076 peels, cycle 221 remaining 5-grams 4/4 I-only, cycle
220 leftover 000 5-gram 1/0, cycle 223 090 076 I-only 69/3,
cycle 208 leftover 4-gram 5/0, and cycle 171 076 071 43/0
stay. Claim that can lose:
i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram.
True only if leftover n=4 family counts stay 27/7/4/1,
exception present, leftover remaining=16, exactly 5 contain
090 076, N=11 remaining-after-090-076, exactly 2 contain
430 076, N=9 remaining-after-430-076, exactly 2 contain
076 020, N=7 remaining-after-076-020, exactly 2 contain
076 010, N=5 remaining-after-076-010, and G is uniquely the
most frequent under the tie-break. The claim is false.
Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
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
    TestMamariI2gram090076IOnlyScoreboard,
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
from tests.test_mamari_i_4gram_999_090_076_070_i_only_scoreboard import (
    GRAM4 as CYCLE208_GRAM4,
    STANDING_I_4GRAM_999_090_076_070_I_ONLY as CYCLE208_I_ONLY,
    STANDING_N_I as CYCLE208_N_I,
    STANDING_N_OFF_I as CYCLE208_N_OFF_I,
    TestMamariI4gram999090076070IOnlyScoreboard,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_I_ONLY,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
    TestMamariI5gram999090076070000IOnlyScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    STANDING_HYPOTHESIZED_N5,
    STANDING_LEFTOVER_N4_COUNT,
    STANDING_MAXIMALS,
    STANDING_N as CYCLE136_STANDING_N,
    TestMamariIIndependentNge4MaximalsScoreboard,
    leftover_n4_rows,
)
from tests.test_mamari_i_leftover_999_090_076_070_remaining_5grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY as CYCLE221_I_ONLY,
    STANDING_N_SEQUENCES as CYCLE221_N_SEQUENCES,
    TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    STANDING_WITH as CYCLE205_N_WITH,
    leftover_with_076_070,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    STANDING_WITH as CYCLE170_N_WITH,
    leftover_with_076_071,
)
from tests.test_mamari_i_leftover_n4_999_090_076_scoreboard import (
    STANDING_WITH as CYCLE166_N_WITH,
    leftover_with_999_090_076,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
    EXCEPTION_SITES,
    STANDING_LEFTOVER,
    TestMamariILeftoverN4Maximals076Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_430_076_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_ALL_I_ONLY as CYCLE331_CLAIM,
    STANDING_N_EXTRA as CYCLE331_N_EXTRA,
    STANDING_N_I_EACH as CYCLE331_N_I_EACH,
    STANDING_N_OFF_I_EACH as CYCLE331_N_OFF_I_EACH,
    STANDING_SEQUENCES as CYCLE331_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter0900764300764gramsIOnlyScoreboard,
    i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only,
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
    STANDING_N as CYCLE328_N,
    STANDING_N_DISTINCT as CYCLE328_N_DISTINCT,
    STANDING_N_TIED_AT_K as CYCLE328_N_TIED,
    STANDING_N_WITHOUT_G as CYCLE328_N_WITHOUT,
    STANDING_TIED_2GRAMS as CYCLE328_TIED,
    TestMamariILeftoverN4RemainingAfter090076Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_unique_max_2gram,
    leftover_remaining_after_090_076,
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
    GRAM2 as CYCLE332_GRAM2,
    LOCKED_G_090_076,
    LOCKED_G_430_076,
    STANDING_CLAIM as CYCLE332_CLAIM,
    STANDING_G as CYCLE332_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE332_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_UNIQUE_MAX_2GRAM as CYCLE332_UNIQUE_MAX_CLAIM,
    STANDING_K as CYCLE332_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE332_MATCHING,
    STANDING_N as CYCLE332_N,
    STANDING_N_DISTINCT as CYCLE332_N_DISTINCT,
    STANDING_N_REMAINING as CYCLE332_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE332_N_TIED,
    STANDING_N_WITHOUT_G as CYCLE332_N_WITHOUT,
    STANDING_RESULT as CYCLE332_RESULT,
    STANDING_TIED_2GRAMS as CYCLE332_TIED,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_unique_max_2gram,
    leftover_remaining_after_090_076_remaining_after_430_076,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_076_010_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_076_010_4GRAMS_ALL_I_ONLY as CYCLE338_CLAIM,
    STANDING_N_EXTRA as CYCLE338_N_EXTRA,
    STANDING_N_I_EACH as CYCLE338_N_I_EACH,
    STANDING_N_OFF_I_EACH as CYCLE338_N_OFF_I_EACH,
    STANDING_SEQUENCES as CYCLE338_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter0760200760104gramsIOnlyScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_076_010_4grams_all_i_only,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly2_076_010_scoreboard import (
    GRAM2 as CYCLE336_GRAM2,
    STANDING_G as CYCLE336_G,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_EXACTLY_2_SHARE_076_010 as CYCLE336_CLAIM,
    STANDING_K as CYCLE336_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE336_MATCHING,
    STANDING_N as CYCLE336_N,
    STANDING_N_REMAINING as CYCLE336_N_REMAINING,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020Exactly2076010Scoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_next_2gram_scoreboard import (
    GRAM2 as CYCLE335_GRAM2,
    LOCKED_G_076_020,
    STANDING_CLAIM as CYCLE335_CLAIM,
    STANDING_G as CYCLE335_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE335_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_UNIQUE_MAX_2GRAM as CYCLE335_UNIQUE_MAX_CLAIM,
    STANDING_K as CYCLE335_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE335_MATCHING,
    STANDING_N as CYCLE335_N,
    STANDING_N_DISTINCT as CYCLE335_N_DISTINCT,
    STANDING_N_REMAINING as CYCLE335_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE335_N_TIED,
    STANDING_N_WITHOUT_G as CYCLE335_N_WITHOUT,
    STANDING_RESULT as CYCLE335_RESULT,
    STANDING_TIED_2GRAMS as CYCLE335_TIED,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_unique_max_2gram,
    leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE222_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    STANDING_N_WITHOUT_G as CYCLE222_N_WITHOUT,
    TestMamariILeftoverN4RemainingNext2gramScoreboard,
    barthel_id,
    contiguous_2grams,
    i_leftover_n4_remaining_exactly_5_contain_090_076,
    leftover_is_remaining,
    leftover_n4_family_counts_hold,
    leftover_remaining_n4,
    leftover_remaining_with_g,
    leftover_remaining_without_g,
    rank_2grams,
    remaining_2gram_counts,
    select_g,
)
from tests.test_mamari_i_nge4_scoreboard import (
    STANDING_INDEPENDENT,
    STANDING_INDEPENDENT_COUNT,
    nge4_sites,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

LOCKED_G_076_010 = CYCLE336_GRAM2
STANDING_LEFTOVER_N4 = 27
STANDING_N_WITH_999_090_076 = 7
STANDING_N_WITH_076_071 = 4
STANDING_N_WITH_076_070 = 1
STANDING_N_EXCEPTION = 1
STANDING_N_REMAINING_GREATGREATGRANDPARENT = 16
STANDING_K_GREATGREATGRANDPARENT = 5
STANDING_N_REMAINING_GREATGRANDPARENT = 11
STANDING_K_GREATGRANDPARENT = 2
STANDING_N_REMAINING_GRANDPARENT = 9
STANDING_K_GRANDPARENT = 2
STANDING_N_REMAINING_PARENT = 7
STANDING_K_PARENT = 2
STANDING_N = 5
GRAM2 = ("999", "604")
STANDING_G = GRAM2
STANDING_N2 = 2
STANDING_K = 1
STANDING_N_WITHOUT_G = 4
STANDING_N_REMAINING = 4
STANDING_N_DISTINCT = 15
STANDING_N_TIED_AT_K = 15
STANDING_TIED_2GRAMS = (
    ("999", "604"),
    ("999", "029"),
    ("700", "076"),
    ("604", "076"),
    ("202", "076"),
    ("076", "999"),
    ("076", "076"),
    ("076", "053"),
    ("076", "011"),
    ("076", "006"),
    ("071", "999"),
    ("029", "076"),
    ("028", "076"),
    ("011", "076"),
    ("006", "055"),
)
STANDING_N_2GRAM_NEXT = 0
NEAR_MISS_076_010_079_090 = ("076", "010", "079", "090")
NEAR_MISS_072_076_010_079 = ("072", "076", "010", "079")
NEAR_MISS_076_020_010_050 = ("076", "020", "010", "050")
NEAR_MISS_053_076_020_010 = ("053", "076", "020", "010")
NEAR_MISS_430_076_001_076 = ("430", "076", "001", "076")
NEAR_MISS_430_076_049_400 = ("430", "076", "049", "400")
NEAR_MISS_090_076_020_010 = ("090", "076", "020", "010")
NEAR_MISS_021_090_076_087 = ("021", "090", "076", "087")
NEAR_MISS_600_090_076_011 = ("600", "090", "076", "011")
NEAR_MISS_999_021_090_076 = ("999", "021", "090", "076")
NEAR_MISS_090_076_057_600 = ("090", "076", "057", "600")
NEAR_MISS_999_090_076_070 = ("999", "090", "076", "070")
NEAR_MISS_071_065_071_999 = EXCEPTION_GRAM
STANDING_MATCHING_LEFTOVERS = (
    ("071", "999", "604", "076"),
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_KNOWN_DISTINCT = True
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_EXTRA_I_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram"
)
STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_MAX_2GRAM = (
    False
)
STANDING_RESULT = (
    "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2gram"
)
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_FAMILY_DOES_NOT_COUNT = True
STANDING_EXCEPTION_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
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
STANDING_EMPTY_REMAINDER_DOES_NOT_LOSE = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE335 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE332 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE328 = True
STANDING_SAME_AS_CYCLE328 = False
STANDING_SAME_AS_CYCLE332 = False
STANDING_SAME_AS_CYCLE333 = False
STANDING_SAME_AS_CYCLE334 = False
STANDING_SAME_AS_CYCLE335 = False
STANDING_SAME_AS_CYCLE336 = False
STANDING_SAME_AS_CYCLE337 = False
STANDING_SAME_AS_CYCLE338 = False


def leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    peeled_090_076: tuple[str, ...] = LOCKED_G_090_076,
    peeled_430_076: tuple[str, ...] = LOCKED_G_430_076,
    peeled_076_020: tuple[str, ...] = LOCKED_G_076_020,
    peeled_076_010: tuple[str, ...] = LOCKED_G_076_010,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 remaining 4-grams with neither 090 076 nor 430 076 nor 076 020 nor 076 010."""
    remaining_after_076_020 = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020(
        leftovers, peeled_090_076, peeled_430_076, peeled_076_020
    )
    return leftover_remaining_without_g(remaining_after_076_020, peeled_076_010)


def leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_with_g(
    remaining_after: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    needle: tuple[str, ...] = STANDING_G,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Remaining-after-076-010 leftovers that contain the labeled G."""
    return leftover_remaining_with_g(remaining_after, needle)


def leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_without_g(
    remaining_after: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    needle: tuple[str, ...] = STANDING_G,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Remaining-after-076-010 leftovers that do not contain the labeled G."""
    return leftover_remaining_without_g(remaining_after, needle)


def i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    expected_remaining_greatgreatgrandparent: int = STANDING_N_REMAINING_GREATGREATGRANDPARENT,
    expected_k_greatgreatgrandparent: int = STANDING_K_GREATGREATGRANDPARENT,
    expected_remaining_greatgrandparent: int = STANDING_N_REMAINING_GREATGRANDPARENT,
    expected_k_greatgrandparent: int = STANDING_K_GREATGRANDPARENT,
    expected_remaining_grandparent: int = STANDING_N_REMAINING_GRANDPARENT,
    expected_k_grandparent: int = STANDING_K_GRANDPARENT,
    expected_remaining_parent: int = STANDING_N_REMAINING_PARENT,
    expected_k_parent: int = STANDING_K_PARENT,
    expected_n: int = STANDING_N,
    peeled_090_076: tuple[str, ...] = LOCKED_G_090_076,
    peeled_430_076: tuple[str, ...] = LOCKED_G_430_076,
    peeled_076_020: tuple[str, ...] = LOCKED_G_076_020,
    peeled_076_010: tuple[str, ...] = LOCKED_G_076_010,
) -> bool:
    """True iff remaining-after-076-010 has a unique most frequent 2-gram."""
    if not leftover_n4_family_counts_hold(leftovers):
        return False
    remaining = leftover_remaining_n4(leftovers)
    if len(remaining) != expected_remaining_greatgreatgrandparent:
        return False
    if not i_leftover_n4_remaining_exactly_5_contain_090_076(leftovers):
        return False
    if len(leftover_remaining_with_g(remaining, peeled_090_076)) != expected_k_greatgreatgrandparent:
        return False
    remaining_after_090 = leftover_remaining_without_g(remaining, peeled_090_076)
    if len(remaining_after_090) != expected_remaining_greatgrandparent:
        return False
    if not i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(leftovers):
        return False
    if len(leftover_remaining_with_g(remaining_after_090, peeled_430_076)) != expected_k_greatgrandparent:
        return False
    remaining_after_430 = leftover_remaining_without_g(
        remaining_after_090, peeled_430_076
    )
    if len(remaining_after_430) != expected_remaining_grandparent:
        return False
    if not i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly_2_share_076_020(
        leftovers
    ):
        return False
    if len(leftover_remaining_with_g(remaining_after_430, peeled_076_020)) != expected_k_grandparent:
        return False
    remaining_after_076_020 = leftover_remaining_without_g(
        remaining_after_430, peeled_076_020
    )
    if len(remaining_after_076_020) != expected_remaining_parent:
        return False
    if not i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010(
        leftovers
    ):
        return False
    if len(leftover_remaining_with_g(remaining_after_076_020, peeled_076_010)) != expected_k_parent:
        return False
    remaining_after = leftover_remaining_without_g(
        remaining_after_076_020, peeled_076_010
    )
    if len(remaining_after) != expected_n:
        return False
    _gram, count, unique = select_g(remaining_after)
    if expected_n == 0:
        return True
    return bool(unique and count >= 1)


STANDING_REMAINING_GREATGREATGRANDPARENT = leftover_remaining_n4(STANDING_LEFTOVER)
STANDING_REMAINING_GREATGRANDPARENT = leftover_remaining_after_090_076(STANDING_LEFTOVER)
STANDING_REMAINING_GRANDPARENT = leftover_remaining_after_090_076_remaining_after_430_076(
    STANDING_LEFTOVER
)
STANDING_REMAINING_PARENT = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020(
    STANDING_LEFTOVER
)
STANDING_REMAINING = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
    STANDING_LEFTOVER
)
STANDING_WITH_ROWS = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_with_g(
    STANDING_REMAINING
)
STANDING_WITHOUT_ROWS = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_without_g(
    STANDING_REMAINING
)
STANDING_2GRAM_COUNTS = remaining_2gram_counts(STANDING_REMAINING)
STANDING_RANKED_2GRAMS = rank_2grams(STANDING_2GRAM_COUNTS)
STANDING_CONTAINS = tuple(
    is_contiguous_substring(GRAM2, gram) for gram, _n, _f, _s in STANDING_REMAINING
)


class TestILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next2gramHelpers(
    unittest.TestCase
):
    """Helpers on remaining-after-076-010 vs next 2-gram. No CV, no LLM."""

    def test_remaining_after_filter_and_unique_max_can_fail(self):
        """The 5 remaining-after-076-010 hapax-pile at 1; unique-max loses."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N4)
        remaining = leftover_remaining_n4(leftover)
        self.assertEqual(len(remaining), STANDING_N_REMAINING_GREATGREATGRANDPARENT)
        self.assertEqual(len(remaining), CYCLE222_N_REMAINING)
        remaining_greatgrandparent = leftover_remaining_after_090_076(leftover)
        self.assertEqual(len(remaining_greatgrandparent), STANDING_N_REMAINING_GREATGRANDPARENT)
        self.assertEqual(len(remaining_greatgrandparent), CYCLE328_N)
        remaining_grandparent = leftover_remaining_after_090_076_remaining_after_430_076(
            leftover
        )
        self.assertEqual(len(remaining_grandparent), STANDING_N_REMAINING_GRANDPARENT)
        self.assertEqual(len(remaining_grandparent), CYCLE332_N)
        remaining_parent = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020(
            leftover
        )
        self.assertEqual(len(remaining_parent), STANDING_N_REMAINING_PARENT)
        self.assertEqual(len(remaining_parent), CYCLE335_N)
        remaining_after = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
            leftover
        )
        self.assertEqual(remaining_after, STANDING_REMAINING)
        self.assertEqual(len(remaining_after), STANDING_N)
        self.assertEqual(len(remaining_after), 5)
        self.assertEqual(GRAM2, ("999", "604"))
        self.assertEqual(LOCKED_G_090_076, ("090", "076"))
        self.assertEqual(LOCKED_G_430_076, ("430", "076"))
        self.assertEqual(LOCKED_G_076_020, ("076", "020"))
        self.assertEqual(LOCKED_G_076_010, ("076", "010"))
        self.assertEqual(
            contiguous_2grams(("071", "999", "604", "076")),
            (("071", "999"), ("999", "604"), ("604", "076")),
        )
        self.assertTrue(leftover_is_remaining(("071", "999", "604", "076")))
        self.assertTrue(leftover_is_remaining(("028", "076", "011", "076")))
        self.assertTrue(leftover_is_remaining(("202", "076", "006", "055")))
        self.assertTrue(leftover_is_remaining(("076", "999", "029", "076")))
        self.assertTrue(leftover_is_remaining(("700", "076", "076", "053")))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_999_090_076_070))
        self.assertFalse(leftover_is_remaining(NEAR_MISS_071_065_071_999))
        self.assertFalse(
            is_contiguous_substring(LOCKED_G_090_076, ("071", "999", "604", "076"))
        )
        self.assertFalse(
            is_contiguous_substring(LOCKED_G_430_076, ("071", "999", "604", "076"))
        )
        self.assertFalse(
            is_contiguous_substring(LOCKED_G_076_020, ("071", "999", "604", "076"))
        )
        self.assertFalse(
            is_contiguous_substring(LOCKED_G_076_010, ("071", "999", "604", "076"))
        )
        self.assertTrue(
            is_contiguous_substring(LOCKED_G_076_010, NEAR_MISS_076_010_079_090)
        )
        self.assertTrue(
            is_contiguous_substring(LOCKED_G_076_020, NEAR_MISS_076_020_010_050)
        )
        self.assertTrue(
            is_contiguous_substring(LOCKED_G_430_076, NEAR_MISS_430_076_001_076)
        )
        self.assertTrue(
            is_contiguous_substring(LOCKED_G_090_076, NEAR_MISS_090_076_020_010)
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
                ()
            )
        )
        with_gram = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_with_g(
            remaining_after
        )
        without_gram = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_without_g(
            remaining_after
        )
        self.assertEqual(len(with_gram), STANDING_K)
        self.assertEqual(len(without_gram), STANDING_N_WITHOUT_G)
        self.assertEqual(with_gram, STANDING_WITH_ROWS)
        self.assertEqual(without_gram, STANDING_WITHOUT_ROWS)
        gram, count, unique = select_g(remaining_after)
        self.assertEqual(gram, STANDING_G)
        self.assertEqual(count, STANDING_K)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(STANDING_RANKED_2GRAMS[0], (STANDING_G, STANDING_K))
        tied = tuple(pair for pair, other in STANDING_RANKED_2GRAMS if other == STANDING_K)
        self.assertEqual(tied, STANDING_TIED_2GRAMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(len(STANDING_RANKED_2GRAMS), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_2GRAM_NEXT, 0)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
                leftover
            )
        )
        planted_family = leftover + (
            (("999", "090", "076", "999"), 4, 1, (("Ia", "Ia1", 0),)),
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
                planted_family
            )
        )
        replacements = {
            ("028", "076", "011", "076"): (
                ("999", "604", "011", "076"),
                4,
                1,
                (("Ia", "Ia1", 0),),
            ),
        }
        unique_leftover = tuple(replacements.get(row[0], row) for row in leftover)
        self.assertEqual(len(unique_leftover), STANDING_LEFTOVER_N4)
        self.assertTrue(leftover_n4_family_counts_hold(unique_leftover))
        self.assertEqual(
            len(leftover_remaining_n4(unique_leftover)),
            STANDING_N_REMAINING_GREATGREATGRANDPARENT,
        )
        unique_after = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
            unique_leftover
        )
        self.assertEqual(len(unique_after), STANDING_N)
        held_g, held_k, held_unique = select_g(unique_after)
        self.assertEqual(held_g, STANDING_G)
        self.assertEqual(held_k, 2)
        self.assertTrue(held_unique)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
                unique_leftover
            )
        )
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram",
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_MAX_2GRAM
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N)
        self.assertTrue(STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_EXTRA_I_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_EMPTY_REMAINDER_DOES_NOT_LOSE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE335)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE332)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE328)
        self.assertFalse(STANDING_SAME_AS_CYCLE328)
        self.assertFalse(STANDING_SAME_AS_CYCLE332)
        self.assertFalse(STANDING_SAME_AS_CYCLE333)
        self.assertFalse(STANDING_SAME_AS_CYCLE334)
        self.assertFalse(STANDING_SAME_AS_CYCLE335)
        self.assertFalse(STANDING_SAME_AS_CYCLE336)
        self.assertFalse(STANDING_SAME_AS_CYCLE337)
        self.assertFalse(STANDING_SAME_AS_CYCLE338)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_is_labeling_only_when_unique_max_false(self):
        """Largest-id tie-break labels G; it does not make unique_max true."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        remaining_after = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
            leftover
        )
        counts = remaining_2gram_counts(remaining_after)
        ranked = rank_2grams(counts)
        self.assertEqual(ranked[0][0], ("999", "604"))
        self.assertEqual(ranked[0][1], 1)
        self.assertEqual(barthel_id("999"), 999)
        self.assertGreater(barthel_id("999"), barthel_id("700"))
        self.assertGreater(barthel_id("604"), barthel_id("029"))
        for pair in STANDING_TIED_2GRAMS:
            self.assertEqual(counts[pair], STANDING_K)
        self.assertEqual(len(counts), STANDING_N_DISTINCT)
        self.assertEqual(len(ranked), STANDING_N_TIED_AT_K)
        gram, count, unique = select_g(remaining_after)
        self.assertEqual(gram, STANDING_G)
        self.assertEqual(count, STANDING_K)
        self.assertFalse(unique)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
                leftover
            )
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftovers_are_cycle_136_n4_not_5gram_substrings(self):
        """Cycle-136 leftover set: 27 n=4 maximals outside the four 5-grams."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        maximal_n4 = tuple(row for row in STANDING_MAXIMALS if row[1] == 4)
        self.assertEqual(len(maximal_n4), STANDING_LEFTOVER_N4)
        for gram, n, _freq, _sites in leftover:
            self.assertEqual(n, 4)
            self.assertEqual(len(gram), 4)
            for five in STANDING_HYPOTHESIZED_N5:
                self.assertFalse(is_contiguous_substring(gram, five))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
        self.assertTrue(STANDING_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_EXCEPTION_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next2gramScoreboard(
    unittest.TestCase
):
    """Cited-fixture remaining-after-076-010 next 2-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.remaining_greatgreatgrandparent = leftover_remaining_n4(self.leftover)
        self.remaining_greatgrandparent = leftover_remaining_after_090_076(self.leftover)
        self.remaining_grandparent = leftover_remaining_after_090_076_remaining_after_430_076(
            self.leftover
        )
        self.remaining_parent = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020(
            self.leftover
        )
        self.remaining = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
            self.leftover
        )
        self.with_gram = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_with_g(
            self.remaining
        )
        self.without_gram = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_without_g(
            self.remaining
        )
        self.claim_holds = (
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
                self.leftover
            )
        )

    def test_tokens_are_cycle_136_leftover_not_invented(self):
        """Leftover 27 is the cycle-136 lock, not a new inventory."""
        self.assertEqual(self.leftover, STANDING_LEFTOVER)
        self.assertEqual(leftover_n4_rows(), STANDING_LEFTOVER)
        self.assertEqual(len(STANDING_LEFTOVER), STANDING_LEFTOVER_N4)
        self.assertEqual(STANDING_LEFTOVER_N4, 27)
        self.assertEqual(STANDING_LEFTOVER_N4_COUNT, 27)
        prior = TestMamariIIndependentNge4MaximalsScoreboard()
        prior.setUp()
        self.assertEqual(len(prior.maximals), CYCLE136_STANDING_N)
        leftover_tokens = {gram for gram, _n, _f, _s in STANDING_LEFTOVER}
        maximal_n4 = {gram for gram, n, _f, _s in prior.maximals if n == 4}
        self.assertEqual(leftover_tokens, maximal_n4)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_leftover_n4_family_and_cycles_222_328_329_332_333_335_336(self):
        """Nested leftover n=4 27/7/4/1, 222 16/5/11, 328/329 11/2/9, 332/333 9/2/7, 335/336 7/2/5 stay."""
        self.assertTrue(leftover_n4_family_counts_hold(self.leftover))
        self.assertEqual(len(self.leftover), 27)
        self.assertEqual(len(leftover_with_999_090_076(self.leftover)), CYCLE166_N_WITH)
        self.assertEqual(len(leftover_with_076_071(self.leftover)), CYCLE170_N_WITH)
        self.assertEqual(len(leftover_with_076_070(self.leftover)), CYCLE205_N_WITH)
        self.assertIn(EXCEPTION_GRAM, {gram for gram, _n, _f, _s in self.leftover})
        self.assertEqual(EXCEPTION_GRAM, ("071", "065", "071", "999"))
        self.assertEqual(EXCEPTION_SITES, (("Ia", "Ia9", 1), ("Ia", "Ia9", 56)))
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(self.leftover))
        self.assertTrue(CYCLE222_CLAIM)
        self.assertTrue(CYCLE222_UNIQUE)
        self.assertEqual(CYCLE222_G, LOCKED_G_090_076)
        self.assertEqual(CYCLE222_K, 5)
        self.assertEqual(CYCLE222_N_REMAINING, 16)
        self.assertEqual(CYCLE222_N_WITHOUT, 11)
        self.assertEqual(len(self.remaining_greatgreatgrandparent), 16)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(self.leftover)
        )
        self.assertTrue(CYCLE329_CLAIM)
        self.assertEqual(CYCLE329_G, LOCKED_G_430_076)
        self.assertEqual(CYCLE329_K, 2)
        self.assertEqual(CYCLE329_N, 11)
        self.assertEqual(CYCLE329_N_REMAINING, 9)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in leftover_remaining_with_g(
                self.remaining_greatgrandparent, LOCKED_G_430_076
            )),
            CYCLE329_MATCHING,
        )
        self.assertEqual(len(self.remaining_greatgrandparent), 11)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly_2_share_076_020(
                self.leftover
            )
        )
        self.assertTrue(CYCLE333_CLAIM)
        self.assertEqual(CYCLE333_G, LOCKED_G_076_020)
        self.assertEqual(CYCLE333_K, 2)
        self.assertEqual(CYCLE333_N, 9)
        self.assertEqual(CYCLE333_N_REMAINING, 7)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in leftover_remaining_with_g(
                self.remaining_grandparent, LOCKED_G_076_020
            )),
            CYCLE333_MATCHING,
        )
        self.assertEqual(len(self.remaining_grandparent), 9)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010(
                self.leftover
            )
        )
        self.assertTrue(CYCLE336_CLAIM)
        self.assertEqual(CYCLE336_G, LOCKED_G_076_010)
        self.assertEqual(CYCLE336_K, 2)
        self.assertEqual(CYCLE336_N, 7)
        self.assertEqual(CYCLE336_N_REMAINING, 5)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in leftover_remaining_with_g(
                self.remaining_parent, LOCKED_G_076_010
            )),
            CYCLE336_MATCHING,
        )
        self.assertEqual(len(self.remaining_parent), 7)
        self.assertEqual(len(self.remaining), STANDING_N)
        self.assertEqual(STANDING_K_PARENT + STANDING_N, STANDING_N_REMAINING_PARENT)
        self.assertEqual(2 + 5, 7)
        self.assertEqual(STANDING_K_GRANDPARENT + STANDING_N_REMAINING_PARENT, 9)
        self.assertEqual(STANDING_K_GREATGRANDPARENT + STANDING_N_REMAINING_GRANDPARENT, 11)
        self.assertEqual(
            STANDING_K_GREATGREATGRANDPARENT + STANDING_N_REMAINING_GREATGRANDPARENT, 16
        )
        self.assertTrue(STANDING_CYCLE222_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE328_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE329_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE332_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE333_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE335_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE336_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remaining_after_5_unique_max_loses(self):
        """5 remaining-after-076-010; unique-max is false. Claim is false."""
        self.assertEqual(len(self.remaining), STANDING_N)
        self.assertEqual(len(self.remaining), 5)
        self.assertEqual(self.remaining, STANDING_REMAINING)
        self.assertEqual(len(self.with_gram), STANDING_K)
        self.assertEqual(len(self.without_gram), STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_K, 1)
        self.assertEqual(STANDING_N_WITHOUT_G, 4)
        self.assertEqual(STANDING_N, STANDING_K + STANDING_N_WITHOUT_G)
        gram, count, unique = select_g(self.remaining)
        self.assertEqual(gram, STANDING_G)
        self.assertEqual(count, STANDING_K)
        self.assertFalse(unique)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram(
                self.leftover
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_MAX_2GRAM,
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_MAX_2GRAM
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram",
        )
        self.assertEqual(
            tuple(is_contiguous_substring(GRAM2, gram) for gram, _n, _f, _s in self.remaining),
            STANDING_CONTAINS,
        )
        self.assertEqual(sum(1 for flag in STANDING_CONTAINS if flag), STANDING_K)
        self.assertEqual(
            sum(1 for flag in STANDING_CONTAINS if not flag),
            STANDING_N_WITHOUT_G,
        )
        for gram, _n, _freq, _sites in self.remaining:
            self.assertTrue("076" in gram)
            self.assertNotEqual(gram, EXCEPTION_GRAM)
            self.assertFalse(is_contiguous_substring(LOCKED_G_090_076, gram))
            self.assertFalse(is_contiguous_substring(LOCKED_G_430_076, gram))
            self.assertFalse(is_contiguous_substring(LOCKED_G_076_020, gram))
            self.assertFalse(is_contiguous_substring(LOCKED_G_076_010, gram))
            self.assertFalse(is_contiguous_substring(("999", "090", "076"), gram))
            self.assertFalse(is_contiguous_substring(("076", "071"), gram))
        self.assertEqual(len(STANDING_2GRAM_COUNTS), STANDING_N_DISTINCT)
        self.assertEqual(STANDING_N_DISTINCT, 15)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_remaining_after_only_the_expected_one_for_labeled_g(self):
        """Labeled G=999 604 matches one leftover; peeled 090 076 / 430 076 / 076 020 / 076 010 do not count."""
        self.assertEqual(self.with_gram, STANDING_WITH_ROWS)
        self.assertEqual(self.without_gram, STANDING_WITHOUT_ROWS)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _s in self.with_gram),
            STANDING_MATCHING_LEFTOVERS,
        )
        for gram, n, freq, _sites in self.without_gram:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertFalse(is_contiguous_substring(GRAM2, gram))
            self.assertNotIn(gram, STANDING_MATCHING_LEFTOVERS)
            self.assertEqual(len(contiguous_2grams(gram)), 3)
        for gram, n, freq, _sites in self.with_gram:
            self.assertEqual(n, 4)
            self.assertGreaterEqual(freq, 2)
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertIn(GRAM2, contiguous_2grams(gram))
        peeled_076_010 = {
            NEAR_MISS_076_010_079_090,
            NEAR_MISS_072_076_010_079,
        }
        peeled_076_020 = {
            NEAR_MISS_076_020_010_050,
            NEAR_MISS_053_076_020_010,
        }
        peeled_430 = {
            NEAR_MISS_430_076_001_076,
            NEAR_MISS_430_076_049_400,
        }
        peeled_090 = {
            NEAR_MISS_090_076_020_010,
            NEAR_MISS_021_090_076_087,
            NEAR_MISS_600_090_076_011,
            NEAR_MISS_999_021_090_076,
            NEAR_MISS_090_076_057_600,
        }
        remaining_tokens = {g for g, _n, _f, _s in self.remaining}
        parent_tokens = {g for g, _n, _f, _s in self.remaining_parent}
        grandparent_tokens = {g for g, _n, _f, _s in self.remaining_grandparent}
        greatgrandparent_tokens = {g for g, _n, _f, _s in self.remaining_greatgrandparent}
        for gram in peeled_076_010:
            self.assertNotIn(gram, remaining_tokens)
            self.assertIn(gram, parent_tokens)
            self.assertIn(gram, CYCLE336_MATCHING)
        for gram in peeled_076_020:
            self.assertNotIn(gram, remaining_tokens)
            self.assertNotIn(gram, parent_tokens)
            self.assertIn(gram, grandparent_tokens)
            self.assertIn(gram, CYCLE333_MATCHING)
        for gram in peeled_430:
            self.assertNotIn(gram, remaining_tokens)
            self.assertNotIn(gram, parent_tokens)
            self.assertNotIn(gram, grandparent_tokens)
            self.assertIn(gram, greatgrandparent_tokens)
            self.assertIn(gram, CYCLE329_MATCHING)
        for gram in peeled_090:
            self.assertNotIn(gram, remaining_tokens)
            self.assertNotIn(gram, parent_tokens)
            self.assertNotIn(gram, grandparent_tokens)
            self.assertNotIn(gram, greatgrandparent_tokens)
            self.assertIn(gram, CYCLE222_MATCHING)
        self.assertNotIn(NEAR_MISS_999_090_076_070, remaining_tokens)
        self.assertNotIn(NEAR_MISS_071_065_071_999, remaining_tokens)
        self.assertTrue(STANDING_I_VS_OFF_I_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_EXTRA_I_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_sites_on_i(self):
        """Remaining-after-076-010 leftover I sites; Ib unpublished."""
        self.assertEqual(self.remaining, STANDING_REMAINING)
        for gram, n, freq, sites in self.remaining:
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), freq)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
                self.assertNotEqual(line[:2], "Ib")
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_338_337_336_335_334_333_332_331_330_329_328_223_222_and_220_scoreboards_still_compute(self):
        """Cycle 338 2/0, 337 11/3, 336 K=2, 335 unique-max lose, 334 12/0 stay."""
        leftover = leftover_n4_rows()
        prior_338 = TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter0760200760104gramsIOnlyScoreboard()
        prior_338.setUp()
        prior_338.test_each_4gram_is_two_on_i_zero_off_i_not_hapax_and_claim_holds()
        prior_338.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE338_SEQUENCES, (
            ("076", "010", "079", "090"),
            ("072", "076", "010", "079"),
        ))
        self.assertEqual(CYCLE338_N_I_EACH, (2, 2))
        self.assertEqual(CYCLE338_N_OFF_I_EACH, (0, 0))
        self.assertEqual(CYCLE338_N_EXTRA, 0)
        self.assertTrue(CYCLE338_CLAIM)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_076_010_4grams_all_i_only(
                CYCLE338_N_I_EACH,
                CYCLE338_N_OFF_I_EACH,
            )
        )
        if not prior_338.claim_holds:
            self.fail("nested cycle 338 leftover 076 010 4-grams all I-only drifted")
        prior_337 = TestMamariI2gram076010IOnlyScoreboard()
        prior_337.setUp()
        prior_337.test_2gram_is_three_off_i_and_not_i_only()
        prior_337.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE337_N_I, 11)
        self.assertEqual(CYCLE337_N_OFF_I, 3)
        self.assertEqual(CYCLE337_N_EXTRA, 8)
        self.assertEqual(CYCLE337_GRAM2, LOCKED_G_076_010)
        self.assertFalse(CYCLE337_CLAIM)
        self.assertFalse(i_2gram_076_010_i_only(11, 3))
        if prior_337.claim_holds:
            self.fail("nested cycle 337 2-gram 076 010 I-only 11/3 drifted")
        prior_336 = TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020Exactly2076010Scoreboard()
        prior_336.setUp()
        prior_336.test_remaining_after_7_exactly_2_share_076_010_holds()
        prior_336.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE336_K, 2)
        self.assertEqual(CYCLE336_G, LOCKED_G_076_010)
        self.assertEqual(CYCLE336_N, 7)
        self.assertEqual(CYCLE336_N_REMAINING, 5)
        self.assertTrue(CYCLE336_CLAIM)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010(
                leftover
            )
        )
        if not prior_336.claim_holds:
            self.fail("nested cycle 336 leftover remaining-after-076-020 exactly-2-share-076 010 drifted")
        prior_335 = TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020Next2gramScoreboard()
        prior_335.setUp()
        prior_335.test_remaining_after_7_unique_max_loses()
        prior_335.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE335_K, 2)
        self.assertEqual(CYCLE335_G, LOCKED_G_076_010)
        self.assertEqual(CYCLE335_N, 7)
        self.assertEqual(CYCLE335_N_WITHOUT, 5)
        self.assertEqual(CYCLE335_N_DISTINCT, 19)
        self.assertEqual(CYCLE335_N_TIED, 2)
        self.assertEqual(CYCLE335_TIED[0], ("076", "010"))
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
        self.assertEqual(CYCLE334_GRAM2, LOCKED_G_076_020)
        self.assertTrue(CYCLE334_CLAIM)
        self.assertTrue(i_2gram_076_020_i_only(12, 0))
        if not prior_334.claim_holds:
            self.fail("nested cycle 334 2-gram 076 020 I-only 12/0 drifted")
        prior_333 = TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076Exactly2076020Scoreboard()
        prior_333.setUp()
        prior_333.test_remaining_after_9_exactly_2_share_076_020_holds()
        prior_333.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE333_K, 2)
        self.assertEqual(CYCLE333_G, LOCKED_G_076_020)
        self.assertEqual(CYCLE333_N, 9)
        self.assertEqual(CYCLE333_N_REMAINING, 7)
        self.assertTrue(CYCLE333_CLAIM)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly_2_share_076_020(
                leftover
            )
        )
        if not prior_333.claim_holds:
            self.fail("nested cycle 333 leftover remaining-after-430-076 exactly-2-share-076 020 drifted")
        prior_332 = TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076Next2gramScoreboard()
        prior_332.setUp()
        prior_332.test_remaining_after_9_unique_max_loses()
        prior_332.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE332_K, 2)
        self.assertEqual(CYCLE332_G, LOCKED_G_076_020)
        self.assertEqual(CYCLE332_N, 9)
        self.assertEqual(CYCLE332_N_WITHOUT, 7)
        self.assertEqual(CYCLE332_N_DISTINCT, 23)
        self.assertEqual(CYCLE332_N_TIED, 4)
        self.assertEqual(CYCLE332_TIED[0], ("076", "020"))
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
        self.assertEqual(CYCLE331_SEQUENCES, (
            ("430", "076", "001", "076"),
            ("430", "076", "049", "400"),
        ))
        self.assertEqual(CYCLE331_N_I_EACH, (2, 2))
        self.assertEqual(CYCLE331_N_OFF_I_EACH, (0, 0))
        self.assertEqual(CYCLE331_N_EXTRA, 0)
        self.assertTrue(CYCLE331_CLAIM)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                CYCLE331_N_I_EACH,
                CYCLE331_N_OFF_I_EACH,
            )
        )
        if not prior_331.claim_holds:
            self.fail("nested cycle 331 leftover 430 076 4-grams all I-only drifted")
        prior_330 = TestMamariI2gram430076IOnlyScoreboard()
        prior_330.setUp()
        prior_330.test_2gram_is_sixteen_off_i_and_not_i_only()
        prior_330.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE330_N_I, 30)
        self.assertEqual(CYCLE330_N_OFF_I, 16)
        self.assertEqual(CYCLE330_N_EXTRA, 26)
        self.assertEqual(CYCLE330_GRAM2, LOCKED_G_430_076)
        self.assertFalse(CYCLE330_CLAIM)
        self.assertFalse(i_2gram_430_076_i_only(30, 16))
        if prior_330.claim_holds:
            self.fail("nested cycle 330 2-gram 430 076 I-only 30/16 drifted")
        prior_329 = TestMamariILeftoverN4RemainingAfter090076Exactly2430076Scoreboard()
        prior_329.setUp()
        prior_329.test_remaining_after_11_exactly_2_share_430_076_holds()
        prior_329.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE329_K, 2)
        self.assertEqual(CYCLE329_G, LOCKED_G_430_076)
        self.assertTrue(CYCLE329_CLAIM)
        if not prior_329.claim_holds:
            self.fail("nested cycle 329 leftover remaining-after-090-076 exactly-2-share-430 076 drifted")
        prior_328 = TestMamariILeftoverN4RemainingAfter090076Next2gramScoreboard()
        prior_328.setUp()
        prior_328.test_remaining_after_11_unique_max_loses()
        prior_328.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE328_K, 2)
        self.assertEqual(CYCLE328_G, LOCKED_G_430_076)
        self.assertEqual(CYCLE328_N, 11)
        self.assertEqual(CYCLE328_N_WITHOUT, 9)
        self.assertEqual(CYCLE328_N_DISTINCT, 28)
        self.assertEqual(CYCLE328_N_TIED, 5)
        self.assertEqual(CYCLE328_TIED[0], ("430", "076"))
        self.assertFalse(CYCLE328_UNIQUE)
        self.assertFalse(CYCLE328_UNIQUE_MAX_CLAIM)
        self.assertFalse(i_leftover_n4_remaining_after_090_076_unique_max_2gram(leftover))
        if prior_328.claim_holds:
            self.fail("nested cycle 328 remaining-after-090-076 unique-max drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE223_N_I, 69)
        self.assertEqual(CYCLE223_N_OFF_I, 3)
        self.assertEqual(CYCLE223_GRAM2, LOCKED_G_090_076)
        self.assertFalse(CYCLE223_CLAIM)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(CYCLE222_CLAIM)
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
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
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
        self.assertEqual(prior_208.i_hits, CYCLE208_N_I)
        self.assertEqual(prior_208.off_i_hits, CYCLE208_N_OFF_I)
        self.assertTrue(CYCLE208_I_ONLY)
        if prior_208.i_hits != 5 or prior_208.off_i_hits != 0:
            self.fail("nested cycle 208 leftover 4-gram 5/0 drifted")
        prior_137 = TestMamariILeftoverN4Maximals076Scoreboard()
        prior_137.setUp()
        prior_137.test_counts_26_of_27_and_hypothesis_all_contain_loses()
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
        self.assertTrue(STANDING_CYCLE338_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE337_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE336_DOES_NOT_COUNT)
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
        """CORPUS_SURVEY.json records the cycle-339 remaining-after-076-010 lock."""
        lock = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2gram"
        ]
        self.assertEqual(lock["cycle"], 339)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(tuple(lock["G"]), STANDING_G)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["leftover_n4_count"], STANDING_LEFTOVER_N4)
        self.assertEqual(lock["N_leftover_n4"], 27)
        self.assertEqual(lock["N_with_999_090_076"], STANDING_N_WITH_999_090_076)
        self.assertEqual(lock["N_with_076_071"], STANDING_N_WITH_076_071)
        self.assertEqual(lock["N_with_076_070"], STANDING_N_WITH_076_070)
        self.assertEqual(lock["N_exception"], STANDING_N_EXCEPTION)
        self.assertEqual(tuple(lock["exception"]), EXCEPTION_GRAM)
        self.assertEqual(lock["N_remaining_greatgreatgrandparent"], STANDING_N_REMAINING_GREATGREATGRANDPARENT)
        self.assertEqual(lock["N_remaining_greatgreatgrandparent"], 16)
        self.assertEqual(lock["K_greatgreatgrandparent"], STANDING_K_GREATGREATGRANDPARENT)
        self.assertEqual(lock["K_greatgreatgrandparent"], 5)
        self.assertEqual(tuple(lock["peeled_2gram_090_076"]), LOCKED_G_090_076)
        self.assertEqual(lock["N_remaining_greatgrandparent"], STANDING_N_REMAINING_GREATGRANDPARENT)
        self.assertEqual(lock["N_remaining_greatgrandparent"], 11)
        self.assertEqual(lock["K_greatgrandparent"], STANDING_K_GREATGRANDPARENT)
        self.assertEqual(lock["K_greatgrandparent"], 2)
        self.assertEqual(tuple(lock["peeled_2gram_430_076"]), LOCKED_G_430_076)
        self.assertEqual(lock["N_remaining_grandparent"], STANDING_N_REMAINING_GRANDPARENT)
        self.assertEqual(lock["N_remaining_grandparent"], 9)
        self.assertEqual(lock["K_grandparent"], STANDING_K_GRANDPARENT)
        self.assertEqual(lock["K_grandparent"], 2)
        self.assertEqual(tuple(lock["peeled_2gram_076_020"]), LOCKED_G_076_020)
        self.assertEqual(lock["N_remaining_parent"], STANDING_N_REMAINING_PARENT)
        self.assertEqual(lock["N_remaining_parent"], 7)
        self.assertEqual(lock["K_parent"], STANDING_K_PARENT)
        self.assertEqual(lock["K_parent"], 2)
        self.assertEqual(tuple(lock["peeled_2gram"]), LOCKED_G_076_010)
        self.assertEqual(tuple(lock["peeled_2gram_076_010"]), LOCKED_G_076_010)
        self.assertEqual(lock["N"], STANDING_N)
        self.assertEqual(lock["N"], 5)
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 1)
        self.assertEqual(lock["N_with_g"], STANDING_K)
        self.assertEqual(lock["N_without_g"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_g"], 4)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 4)
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 15)
        self.assertEqual(lock["N_tied_at_k"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_k"], 15)
        measured_tied = [list(pair) for pair in STANDING_TIED_2GRAMS]
        self.assertEqual(lock["tied_2grams"], measured_tied)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(lock["matching_leftovers"], measured_matching)
        measured_remaining = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
                "constituent_2grams": [list(pair) for pair in contiguous_2grams(tokens)],
                "contains_g": is_contiguous_substring(GRAM2, tokens),
            }
            for tokens, n, freq, sites in STANDING_REMAINING
        ]
        self.assertEqual(lock["remaining"], measured_remaining)
        measured_ranked = [
            {"tokens": list(pair), "remaining_count": count}
            for pair, count in STANDING_RANKED_2GRAMS
        ]
        self.assertEqual(lock["ranked_2grams"], measured_ranked)
        histogram_top = [
            {"tokens": list(pair), "remaining_count": count}
            for pair, count in STANDING_RANKED_2GRAMS[:8]
        ]
        self.assertEqual(lock["histogram_top"], histogram_top)
        self.assertEqual(tuple(lock["contains_g"]), STANDING_CONTAINS)
        self.assertEqual(tuple(lock["near_miss_076_010_079_090"]), NEAR_MISS_076_010_079_090)
        self.assertEqual(tuple(lock["near_miss_072_076_010_079"]), NEAR_MISS_072_076_010_079)
        self.assertEqual(tuple(lock["near_miss_076_020_010_050"]), NEAR_MISS_076_020_010_050)
        self.assertEqual(tuple(lock["near_miss_053_076_020_010"]), NEAR_MISS_053_076_020_010)
        self.assertEqual(tuple(lock["near_miss_430_076_001_076"]), NEAR_MISS_430_076_001_076)
        self.assertEqual(tuple(lock["near_miss_430_076_049_400"]), NEAR_MISS_430_076_049_400)
        self.assertEqual(tuple(lock["near_miss_090_076_020_010"]), NEAR_MISS_090_076_020_010)
        self.assertEqual(tuple(lock["near_miss_021_090_076_087"]), NEAR_MISS_021_090_076_087)
        self.assertEqual(tuple(lock["near_miss_600_090_076_011"]), NEAR_MISS_600_090_076_011)
        self.assertEqual(tuple(lock["near_miss_999_021_090_076"]), NEAR_MISS_999_021_090_076)
        self.assertEqual(tuple(lock["near_miss_090_076_057_600"]), NEAR_MISS_090_076_057_600)
        self.assertEqual(tuple(lock["near_miss_999_090_076_070"]), NEAR_MISS_999_090_076_070)
        self.assertEqual(tuple(lock["near_miss_071_065_071_999"]), NEAR_MISS_071_065_071_999)
        self.assertTrue(lock["family_999_090_076_does_not_count"])
        self.assertTrue(lock["family_076_071_does_not_count"])
        self.assertTrue(lock["exception_071_065_071_999_does_not_count"])
        self.assertTrue(lock["peeled_090_076_does_not_count"])
        self.assertTrue(lock["peeled_430_076_does_not_count"])
        self.assertTrue(lock["peeled_076_020_does_not_count"])
        self.assertTrue(lock["peeled_076_010_does_not_count"])
        self.assertFalse(lock["g_uniquely_most_frequent"])
        self.assertEqual(lock["g_uniquely_most_frequent"], STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertFalse(lock["unique_max"])
        self.assertTrue(lock["unique_max_tie_break_is_labeling_only"])
        self.assertTrue(lock["empty_remainder_does_not_lose"])
        self.assertTrue(lock["i_vs_off_i_is_not_this_cycle"])
        self.assertTrue(lock["leftover_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["extra_i_4gram_i_only_is_not_this_cycle"])
        self.assertNotIn("N_I", lock)
        self.assertNotIn("N_off_I", lock)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(lock["ib_hits"], 0)
        self.assertEqual(lock["ib_sites"], [])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(
            lock["i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram"]
        )
        self.assertEqual(
            lock["i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_unique_max_2gram"],
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_MAX_2GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle222"])
        self.assertFalse(lock["same_as_cycle328"])
        self.assertFalse(lock["same_as_cycle329"])
        self.assertFalse(lock["same_as_cycle330"])
        self.assertFalse(lock["same_as_cycle331"])
        self.assertFalse(lock["same_as_cycle332"])
        self.assertFalse(lock["same_as_cycle333"])
        self.assertFalse(lock["same_as_cycle334"])
        self.assertFalse(lock["same_as_cycle335"])
        self.assertFalse(lock["same_as_cycle336"])
        self.assertFalse(lock["same_as_cycle337"])
        self.assertFalse(lock["same_as_cycle338"])
        self.assertTrue(lock["same_claim_shape_as_cycle335"])
        self.assertTrue(lock["same_claim_shape_as_cycle332"])
        self.assertTrue(lock["same_claim_shape_as_cycle328"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
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
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_076_010_4grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_2gram_076_010_i_only_unchanged"])
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
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_after_090_076_430_076_4grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_2gram_430_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_after_090_076_exactly2_430_076_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_after_090_076_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_999_090_076_070_remaining_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_5gram_999_090_076_070_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_999_090_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertTrue(lock["nested_cycle338_4grams_all_i_only"])
        self.assertEqual(lock["nested_cycle338_N_extra"], 0)
        self.assertFalse(lock["nested_cycle337_i_2gram_076_010_i_only"])
        self.assertEqual(lock["nested_cycle337_N_I"], 11)
        self.assertEqual(lock["nested_cycle337_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle337_N_extra"], 8)
        self.assertTrue(lock["nested_cycle336_exactly_2_share_076_010"])
        self.assertEqual(lock["nested_cycle336_K"], 2)
        self.assertEqual(lock["nested_cycle336_N"], 7)
        self.assertEqual(lock["nested_cycle336_N_remaining"], 5)
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
        prior_338 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_076_010_4grams_i_only"
        ]
        self.assertEqual(prior_338["cycle"], 338)
        self.assertTrue(
            prior_338["i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_076_010_4grams_all_i_only"]
        )
        self.assertEqual(prior_338["N_extra"], 0)
        prior_337 = self.survey["i_2gram_076_010_i_only"]
        self.assertEqual(prior_337["cycle"], 337)
        self.assertFalse(prior_337["i_2gram_076_010_i_only"])
        self.assertEqual(prior_337["N_I"], 11)
        self.assertEqual(prior_337["N_off_I"], 3)
        self.assertEqual(prior_337["N_extra"], 8)
        prior_336 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly2_076_010"
        ]
        self.assertEqual(prior_336["cycle"], 336)
        self.assertTrue(
            prior_336["i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_exactly_2_share_076_010"]
        )
        self.assertEqual(tuple(prior_336["G"]), ("076", "010"))
        self.assertEqual(prior_336["K"], 2)
        self.assertEqual(prior_336["N"], 7)
        self.assertEqual(prior_336["N_remaining"], 5)
        prior_335 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_next_2gram"
        ]
        self.assertEqual(prior_335["cycle"], 335)
        self.assertFalse(
            prior_335["i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_unique_max_2gram"]
        )
        self.assertFalse(prior_335["unique_max"])
        self.assertEqual(prior_335["K"], 2)
        self.assertEqual(tuple(prior_335["G"]), ("076", "010"))
        self.assertEqual(prior_335["N_without_g"], 5)
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
            prior_333["i_leftover_n4_remaining_after_090_076_remaining_after_430_076_exactly_2_share_076_020"]
        )
        self.assertEqual(tuple(prior_333["G"]), ("076", "020"))
        self.assertEqual(prior_333["K"], 2)
        self.assertEqual(prior_333["N"], 9)
        self.assertEqual(prior_333["N_remaining"], 7)
        prior_332 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_next_2gram"
        ]
        self.assertEqual(prior_332["cycle"], 332)
        self.assertFalse(
            prior_332["i_leftover_n4_remaining_after_090_076_remaining_after_430_076_unique_max_2gram"]
        )
        self.assertFalse(prior_332["unique_max"])
        self.assertEqual(prior_332["K"], 2)
        self.assertEqual(tuple(prior_332["G"]), ("076", "020"))
        self.assertEqual(prior_332["N_without_g"], 7)
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
        self.assertEqual(tuple(prior_328["G"]), ("430", "076"))
        self.assertEqual(prior_328["N_without_g"], 9)
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertEqual(prior_222["N_remaining"], 16)
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(tuple(prior_222["G"]), ("090", "076"))
        self.assertEqual(prior_222["N_without_g"], 11)
        self.assertTrue(prior_222["g_uniquely_most_frequent"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        prior_221 = self.survey["i_leftover_999_090_076_070_remaining_5grams_i_only"]
        self.assertEqual(prior_221["cycle"], 221)
        self.assertTrue(prior_221["i_leftover_999_090_076_070_remaining_5grams_i_only"])
        self.assertEqual(prior_221["N_remaining"], 4)
        prior_220 = self.survey["i_5gram_999_090_076_070_000_i_only"]
        self.assertEqual(prior_220["cycle"], 220)
        self.assertTrue(prior_220["i_5gram_999_090_076_070_000_i_only"])
        self.assertEqual(prior_220["N_I"], 1)
        self.assertEqual(prior_220["N_off_I"], 0)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"]["i_4gram_999_090_076_070_i_only"]
        )
        self.assertEqual(tuple(self.survey["i_4gram_999_090_076_070_i_only"]["tokens4"]), CYCLE208_GRAM4)
        peel_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(peel_288["cycle"], 288)
        self.assertEqual(peel_288["N_inside"], 13)
        self.assertEqual(peel_288["G"], "020")
        self.assertEqual(peel_288["K"], 4)
        peel_327 = self.survey[
            "i_leftover_n4_remaining_021_090_076_remaining_after_999_extra_i_fwd4_090_076_087_i_only"
        ]
        self.assertEqual(peel_327["cycle"], 327)
        self.assertTrue(
            peel_327["i_leftover_n4_remaining_021_090_076_remaining_after_999_extra_i_fwd4_090_076_087_all_i_only"]
        )
        extra = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(extra["cycle"], 225)
        self.assertEqual(extra["N_leftover"], 56)
        extra_rem = self.survey["i_leftover_extra_090_076_remaining_next_stem"]
        self.assertEqual(extra_rem["cycle"], 227)
        self.assertTrue(STANDING_I_SITE_PEEL_288_327_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_DO_NOT_COUNT)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
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


class TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next2gramImageSnapshot(
    unittest.TestCase
):
    """Cycle 339 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / Hamming 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
