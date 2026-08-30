"""I's cycle-273 leftover extra remaining-after-076 previous-071 lock.

Cycle 275 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not retune
the forward peel of leftover extra I 090 076 (cycles 225–259).
Does not overwrite cycle 167's 3-gram I-only 16/0 lock. Does
not overwrite cycle 268's 3-gram I-only 6/0 lock. Does not
overwrite cycle 269's previous-4 I-only hapax lock. Does not
overwrite cycle 271's leftover extra remaining-after-600
previous-090 lock. Does not overwrite cycle 273's leftover
extra remaining-after-600 remaining-after-090 previous-076
lock. Does not retune cycle 272's 3-gram 090 090 076 I-only
lose 3/1 on T extra I=1. Does not retune cycle 274's 3-gram
076 090 076 I-only lose 3/1 on T extra I=1. Does not peel T /
extra-I of 090 090 076 or of 076 090 076. Does not vendor a
new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new
agents. Not a meaning dictionary.

Cycle 270 leftover extra remaining-after-600 unique-max
previous stem LOST: 5-way tie at K=2 (090/076/071/045/009),
G=090 by largest-id, N_remaining_after_600=37. Cycle 271
peeled 090 as exact-K: leftover extra remaining-after-600
exactly 2 share previous 090 HOLDS at Ia12[42]/Ia14[105];
N_remaining_after_090=35. Cycle 272 locked 3-gram 090 090 076
I-only and LOST 3/1 on T; do not retune 272 and do not peel
its T / extra-I this cycle. Cycle 273 peeled 076 as exact-K:
leftover extra remaining-after-600 remaining-after-090
exactly 2 share previous 076 HOLDS at Ia2[165]/Ia13[152];
N_remaining_after_090_and_076=33. Cycle 274 locked 3-gram
076 090 076 I-only and LOST 3/1 on T; do not retune 274 and
do not peel its T / extra-I this cycle. Next tied stem by the
same largest-id order is 071. Do not peel 045/009 this cycle.
Do not lock 3-gram 071 090 076 I-only this cycle. Do not
retune leftover n=4. Do not retune the forward peel. Do not
retune previous-999 / previous-600 / previous-090 /
previous-076 clusters. Off-I T sites are not this cycle.

Hypothesis K=2: leftover extra remaining-after-600
remaining-after-090 remaining-after-076 I 090 076 sites
include exactly 2 that share previous stem 071 (backward
3-gram 071 090 076). Nested-check leftover extra remaining-
after-600 remaining-after-090 exactly 2 share previous 076,
K_076==2, N_remaining_after_090_and_076==33, leftover
extra==56, N_I==69 (do not retune 223/224/270/271/272/273/274).
On the remaining-after-090-and-076 population (leftover extra
I 090 076 whose previous token is none of 600/090/076; N=33;
also not 999 because remaining-after-600 already peeled 999),
count previous-token frequencies. Lock K_071, the sites, and
N_remaining_after_090_and_076_and_071 = 33 − K_071. Nested-
check cycle 270's 5-way still includes 071 at K=2 on
remaining-after-600 (before subtracting 090/076), so after
peeling 090 and 076 the remaining-after-090-and-076 K_071 is
expected 2 unless those two 071 sites were the 090 or 076
sites (they should not be: previous 071 vs previous 090/076).
Measured: K_071=2 at Ia3[87], Ia7[88]; those matching
remaining-after-090-and-076 sites equal the cycle-270
remaining-after-600 previous-071 pair. N_remaining_after_090_and_076_and_071=31
(33−2). Claim that can lose:
i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071.
True only if K_071==2 among leftover extra remaining-after-076
I 090 076. The claim is true. This can lose if nested-check K
differs from 2. Nested cycle 274 3/1 on T extra I=1, cycle 273
K_076=2 N_remaining_after_090_and_076=33 previous 4-grams
076 076 090 076 / 071 076 090 076, cycle 272 3/1 on T extra
I=1, cycle 271 K_090=2 N_remaining_after_090=35, cycle 270
unique-max false 5-way K=2 G=090, and cycle 268 6/0 extra I=2
stay. Do not assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
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
from tests.test_mamari_i_3gram_076_090_076_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE274_EXTRA_I_SITES,
    STANDING_I_3GRAM_076_090_076_I_ONLY as CYCLE274_CLAIM,
    STANDING_I_SITES as CYCLE274_I_SITES,
    STANDING_N_EXTRA as CYCLE274_N_EXTRA,
    STANDING_N_I as CYCLE274_N_I,
    STANDING_N_OFF_I as CYCLE274_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE274_OFF_I_SITES,
    TestMamariI3gram076090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_090_076_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE272_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_090_076_I_ONLY as CYCLE272_CLAIM,
    STANDING_I_SITES as CYCLE272_I_SITES,
    STANDING_N_EXTRA as CYCLE272_N_EXTRA,
    STANDING_N_I as CYCLE272_N_I,
    STANDING_N_OFF_I as CYCLE272_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE272_OFF_I_SITES,
    TestMamariI3gram090090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_600_090_076_i_only_scoreboard import (
    STANDING_I_3GRAM_600_090_076_I_ONLY as CYCLE268_CLAIM,
    STANDING_N_EXTRA as CYCLE268_N_EXTRA,
    STANDING_N_I as CYCLE268_N_I,
    STANDING_N_OFF_I as CYCLE268_N_OFF_I,
    TestMamariI3gram600090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_600_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_600_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE269_ALL_HAPAX,
    STANDING_N_I_ONLY as CYCLE269_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE269_N_NOT_HAPAX,
    TestMamariI600090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_999_090_076_previous_090_scoreboard import (
    STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE264_CLAIM,
    STANDING_K_090 as CYCLE264_K_090,
    STANDING_MATCHING_SITES as CYCLE264_MATCHING_SITES,
    TestMamariI999090076Previous090Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 as CYCLE261_CLAIM,
    STANDING_K_999 as CYCLE261_K_999,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
    STANDING_N_LEFTOVER_EXTRA as CYCLE261_N_LEFTOVER_EXTRA,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    leftover_extra_with_previous_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE260_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    leftover_extra_backward_3grams,
    leftover_extra_previous_4grams,
    leftover_extra_previous_stems,
    leftover_sites_with_previous,
    leftover_sites_without_previous,
    select_previous_g,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_fwd700_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_2_SHARE_700 as CYCLE235_CLAIM,
    STANDING_K as CYCLE235_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_prev076_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_090,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_EXACTLY_2_SHARE_PREVIOUS_076 as CYCLE273_CLAIM,
    STANDING_K_076 as CYCLE273_K_076,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE273_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE273_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_090 as CYCLE273_N_REMAINING_AFTER_090,
    STANDING_N_REMAINING_AFTER_090_AND_076 as CYCLE273_N_REMAINING_AFTER_090_AND_076,
    STANDING_REMAINING_AFTER_090_AND_076_SITES as CYCLE273_REMAINING_AFTER_090_AND_076_SITES,
    leftover_extra_remaining_after_090,
    leftover_extra_remaining_after_090_nested_counts_hold,
    leftover_extra_remaining_after_090_previous_stems,
    leftover_extra_remaining_after_090_with_previous_076,
    leftover_extra_remaining_after_090_without_previous_076,
    TestMamariILeftoverExtra090076RemainingAfter600Prev076Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_090_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE271_CLAIM,
    STANDING_K_090 as CYCLE271_K_090,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE271_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE271_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_090 as CYCLE271_N_REMAINING_AFTER_090,
    leftover_extra_remaining_after_600_with_previous_090,
    leftover_extra_remaining_after_600_without_previous_090,
    TestMamariILeftoverExtra090076RemainingAfter600Previous090Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_600,
    STANDING_G as CYCLE270_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE270_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_MATCHING_SITES as CYCLE270_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE270_N_DISTINCT,
    STANDING_N_HAPAX_REMAINING as CYCLE270_N_HAPAX,
    STANDING_N_REMAINING_AFTER_600 as CYCLE270_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED_AT_K,
    STANDING_REMAINING_FREQUENCY as CYCLE270_FREQUENCY,
    STANDING_REMAINING_SITES as CYCLE270_REMAINING_SITES,
    STANDING_TIED_STEMS as CYCLE270_TIED_STEMS,
    leftover_extra_remaining_after_600,
    leftover_extra_remaining_after_600_nested_counts_hold,
    leftover_extra_remaining_after_600_previous_stems,
    leftover_extra_remaining_after_600_with_g,
    leftover_extra_remaining_after_600_with_previous,
    leftover_extra_remaining_after_600_without_g,
    leftover_extra_remaining_after_600_without_previous,
    remaining_after_600_previous_stem_frequency_table,
    select_remaining_after_600_g,
    TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_600_scoreboard import (
    STANDING_G as CYCLE267_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_EXACTLY_4_SHARE_PREVIOUS_600 as CYCLE267_CLAIM,
    STANDING_K_600 as CYCLE267_K_600,
    STANDING_MATCHING_SITES as CYCLE267_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_600 as CYCLE267_N_REMAINING_AFTER_600,
    leftover_extra_remaining_after_999_without_previous_600,
    leftover_extra_remaining_after_999_with_g,
    TestMamariILeftoverExtra090076RemainingAfter999Previous600Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_999,
    STANDING_G as CYCLE266_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE266_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM as CYCLE266_CLAIM,
    STANDING_K as CYCLE266_K,
    leftover_extra_remaining_after_999,
    leftover_extra_remaining_after_999_nested_counts_hold,
    leftover_extra_remaining_after_999_previous_stems,
    select_remaining_after_999_g,
    TestMamariILeftoverExtra090076RemainingAfter999PreviousStemScoreboard,
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

HYPOTHESIS_K = 2
LOCKED_PREVIOUS_STEM_999 = "999"
LOCKED_PREVIOUS_STEM_600 = "600"
LOCKED_PREVIOUS_STEM_090 = "090"
LOCKED_PREVIOUS_STEM_076 = "076"
LOCKED_PREVIOUS_STEM_071 = "071"
LOCKED_PREVIOUS_STEMS_AFTER_076 = (
    LOCKED_PREVIOUS_STEM_999,
    LOCKED_PREVIOUS_STEM_600,
    LOCKED_PREVIOUS_STEM_090,
    LOCKED_PREVIOUS_STEM_076,
)
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_BACKWARD = ("071", "090", "076")
GRAM3_NESTED_076 = ("076", "090", "076")
GRAM3_NESTED_090 = ("090", "090", "076")
GRAM3_NESTED_600 = ("600", "090", "076")
GRAM3_NESTED_999 = ("999", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS_LEFTOVER = 56
STANDING_N_NO_PREVIOUS_LEFTOVER = 0
STANDING_K_999 = 15
STANDING_N_REMAINING_AFTER_999 = 41
STANDING_K_600 = 4
STANDING_N_REMAINING_AFTER_600 = 37
STANDING_K_090 = 2
STANDING_N_REMAINING_AFTER_090 = 35
STANDING_K_076 = 2
STANDING_N_REMAINING_AFTER_090_AND_076 = 33
STANDING_N_WITH_PREVIOUS = 33
STANDING_N_NO_PREVIOUS = 0
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT_REMAINING_AFTER_090_AND_076 = 30
STANDING_K = 2
STANDING_K_071 = 2
STANDING_G = "071"
STANDING_N_WITHOUT = 31
STANDING_N_REMAINING_AFTER_090_AND_076_AND_071 = 31
STANDING_N_TIED_AT_K_AFTER_600 = 5
STANDING_TIED_STEMS_AFTER_600 = ("090", "076", "071", "045", "009")
STANDING_OTHER_TIED_STEMS = ("045", "009")
STANDING_CYCLE270_K_071 = 2
STANDING_071_STILL_MAX_K_AFTER_600 = True
STANDING_REMAINING_AFTER_090_AND_076_SITES = (
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 159),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia3", 4),
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia4", 134),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia4", 166),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 66),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia5", 164),
    (SIDE_IA, "Ia6", 134),
    (SIDE_IA, "Ia7", 2),
    (SIDE_IA, "Ia7", 88),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia8", 120),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 67),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia13", 143),
    (SIDE_IA, "Ia14", 9),
    (SIDE_IA, "Ia14", 97),
    (SIDE_IA, "Ia14", 177),
)
STANDING_REMAINING_AFTER_090_AND_076_PREVIOUS_STEMS = (
    "045",
    "048",
    "380",
    "011",
    "499",
    "045",
    "497",
    "009",
    "036",
    "071",
    "092",
    "291",
    "522",
    "150",
    "078",
    "295",
    "000",
    "109",
    "009",
    "052",
    "099",
    "071",
    "700",
    "161",
    "010",
    "205",
    "382",
    "386",
    "008",
    "027",
    "724",
    "400",
    "326",
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia7", 88),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("076", "071", "090", "076"),
    ("092", "071", "090", "076"),
)
STANDING_CYCLE270_071_SITES = (
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia7", 88),
)
STANDING_MATCHING_EQUALS_CYCLE270_071_SITES = True
STANDING_REMAINING_AFTER_090_AND_076_AND_071_SITES = (
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 159),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia3", 4),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia4", 134),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia4", 166),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 66),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia5", 164),
    (SIDE_IA, "Ia6", 134),
    (SIDE_IA, "Ia7", 2),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia8", 120),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 67),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia13", 143),
    (SIDE_IA, "Ia14", 9),
    (SIDE_IA, "Ia14", 97),
    (SIDE_IA, "Ia14", 177),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071"
)
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_EXACTLY_2_SHARE_PREVIOUS_071 = True
STANDING_RESULT = (
    "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_previous_071"
)
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE235 = False
STANDING_SAME_AS_CYCLE264 = False
STANDING_SAME_AS_CYCLE270 = False
STANDING_SAME_AS_CYCLE271 = False
STANDING_SAME_AS_CYCLE272 = False
STANDING_SAME_AS_CYCLE273 = False
STANDING_SAME_AS_CYCLE274 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE271 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE273 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_045_009 = True
STANDING_I_ONLY_OF_071_090_076_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_RETUNE_272 = True
STANDING_DO_NOT_RETUNE_274 = True
STANDING_DO_NOT_PEEL_T_OR_EXTRA_I_OF_090_090_076 = True
STANDING_DO_NOT_PEEL_T_OR_EXTRA_I_OF_076_090_076 = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_PREVIOUS_999_600_090_076_NOT_RETUNED = True
STANDING_CYCLE167_NOT_OVERWRITTEN = True
STANDING_CYCLE268_NOT_OVERWRITTEN = True
STANDING_CYCLE269_NOT_OVERWRITTEN = True
STANDING_CYCLE271_NOT_OVERWRITTEN = True
STANDING_CYCLE272_NOT_RETUNED = True
STANDING_CYCLE273_NOT_OVERWRITTEN = True
STANDING_CYCLE274_NOT_RETUNED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_CYCLE264_IS_DIFFERENT_CLUSTER = True


def leftover_extra_remaining_after_090_and_076(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_076,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites whose previous token is not 999, 600, 090, or 076."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev not in locked_set
    )


def leftover_extra_remaining_after_090_and_076_previous_stems(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_076,
) -> tuple[str, ...]:
    """Previous stems of remaining-after-090-and-076 sites that have a previous token."""
    locked_set = set(locked)
    return tuple(
        prev
        for prev in previous_stems
        if prev is not None and prev not in locked_set
    )


def leftover_extra_remaining_after_090_and_076_with_previous_071(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_076,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-090-and-076 sites whose previous token is 071."""
    remaining = set(leftover_extra_remaining_after_090_and_076(sites, previous_stems, locked))
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev == stem and site in remaining
    )


def leftover_extra_remaining_after_090_and_076_without_previous_071(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_076,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-090-and-076 sites whose previous token is not 071."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev is not None and prev not in locked_set and prev != stem
    )


def leftover_extra_remaining_after_600_with_previous_071(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-600 sites whose previous token is 071."""
    return leftover_extra_remaining_after_600_with_g(
        sites,
        previous_stems,
        stem=stem,
        locked=locked,
    )


def matching_equals_cycle270_071_set(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle270_071_sites: tuple[tuple[str, str, int], ...] = STANDING_CYCLE270_071_SITES,
) -> bool:
    """True iff remaining-after-076 previous-071 sites equal the cycle-270 071 pair."""
    return matching_sites == cycle270_071_sites


def matching_leftover_extra_remaining_after_090_and_076_previous_071_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-076 previous-071 rows."""
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


def leftover_extra_remaining_after_090_and_076_nested_counts_hold(
    n_i: int,
    n_leftover: int,
    k_999: int,
    n_remaining_after_999: int,
    k_600: int,
    n_remaining_after_600: int,
    k_090: int,
    n_remaining_after_090: int,
    k_076: int,
    n_remaining_after_090_and_076: int,
    expected_i: int = STANDING_N_I,
    expected_leftover: int = STANDING_N_LEFTOVER,
    expected_k_999: int = STANDING_K_999,
    expected_remaining_999: int = STANDING_N_REMAINING_AFTER_999,
    expected_k_600: int = STANDING_K_600,
    expected_remaining_600: int = STANDING_N_REMAINING_AFTER_600,
    expected_k_090: int = STANDING_K_090,
    expected_remaining_090: int = STANDING_N_REMAINING_AFTER_090,
    expected_k_076: int = STANDING_K_076,
    expected_remaining_076: int = STANDING_N_REMAINING_AFTER_090_AND_076,
) -> bool:
    """Nested leftover extra 69/56, K_999=15, K_600=4, K_090=2, K_076=2, remaining-after-076=33."""
    return (
        n_i == expected_i
        and n_leftover == expected_leftover
        and k_999 == expected_k_999
        and n_remaining_after_999 == expected_remaining_999
        and k_600 == expected_k_600
        and n_remaining_after_600 == expected_remaining_600
        and k_090 == expected_k_090
        and n_remaining_after_090 == expected_remaining_090
        and k_076 == expected_k_076
        and n_remaining_after_090_and_076 == expected_remaining_076
        and n_remaining_after_999 == n_leftover - k_999
        and n_remaining_after_600 == n_remaining_after_999 - k_600
        and n_remaining_after_090 == n_remaining_after_600 - k_090
        and n_remaining_after_090_and_076 == n_remaining_after_090 - k_076
    )


def i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(
    k: int,
    expected: int = HYPOTHESIS_K,
) -> bool:
    """True iff K_071 equals the hypothesized 2."""
    return k == expected


class TestILeftoverExtra090076RemainingAfter076Previous071Helpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-076 previous 071. No CV, no LLM."""

    def test_previous_071_requires_remaining_after_076_previous_stem(self):
        """Previous stem 071 is remaining-after-076; locked 999/600/090/076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("071", "090", "076"))
        self.assertEqual(GRAM3_NESTED_076, ("076", "090", "076"))
        self.assertEqual(GRAM3_NESTED_090, ("090", "090", "076"))
        self.assertEqual(GRAM3_NESTED_600, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_999, ("999", "090", "076"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_076, ("999", "600", "090", "076"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_090, ("999", "600", "090"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_600, ("999", "600"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_999, ("999",))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_071 = ["076", "071", "090", "076"]
        self.assertEqual(site_previous_stem(has_071, 2, GRAM2), "071")
        self.assertEqual(site_backward_3gram(has_071, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_071, 2, GRAM2),
            ("076", "071", "090", "076"),
        )
        has_092_071 = ["092", "071", "090", "076"]
        self.assertEqual(site_previous_stem(has_092_071, 2, GRAM2), "071")
        self.assertEqual(
            site_previous_4gram(has_092_071, 2, GRAM2),
            ("092", "071", "090", "076"),
        )
        has_076 = ["071", "076", "090", "076"]
        self.assertEqual(site_previous_stem(has_076, 2, GRAM2), "076")
        self.assertNotEqual(site_previous_stem(has_076, 2, GRAM2), "071")
        has_090 = ["011", "090", "090", "076"]
        self.assertEqual(site_previous_stem(has_090, 2, GRAM2), "090")
        self.assertNotEqual(site_previous_stem(has_090, 2, GRAM2), "071")
        has_600 = ["076", "600", "090", "076"]
        self.assertEqual(site_previous_stem(has_600, 2, GRAM2), "600")
        self.assertNotEqual(site_previous_stem(has_600, 2, GRAM2), "071")
        has_999 = ["000", "999", "090", "076"]
        self.assertEqual(site_previous_stem(has_999, 2, GRAM2), "999")
        self.assertNotEqual(site_previous_stem(has_999, 2, GRAM2), "071")
        other_prev = ["093", "045", "090", "076"]
        self.assertEqual(site_previous_stem(other_prev, 2, GRAM2), "045")
        self.assertNotEqual(site_backward_3gram(other_prev, 2, GRAM2), GRAM3_BACKWARD)
        one_token_before = ["071", "090", "076"]
        self.assertEqual(site_previous_stem(one_token_before, 1, GRAM2), "071")
        self.assertEqual(site_backward_3gram(one_token_before, 1, GRAM2), GRAM3_BACKWARD)
        self.assertIsNone(site_previous_4gram(one_token_before, 1, GRAM2))
        line_initial = ["090", "076", "012"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        mismatch_071 = ["090", "076", "071", "090"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        mismatch_070 = ["090", "076", "070", "090"]
        self.assertIsNone(site_previous_stem(mismatch_070, 1, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
            (SIDE_IA, "Ia1", 5),
            (SIDE_IA, "Ia1", 6),
        )
        planted_stems = ("071", "076", "090", "999", "600", None, "045")
        rem = leftover_extra_remaining_after_090_and_076(planted_sites, planted_stems)
        self.assertEqual(rem, (planted_sites[0], planted_sites[5], planted_sites[6]))
        self.assertEqual(
            leftover_extra_remaining_after_090_and_076_with_previous_071(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_extra_remaining_after_090_and_076_without_previous_071(
                planted_sites,
                planted_stems,
            ),
            (planted_sites[6],),
        )
        self.assertNotIn(planted_sites[1], rem)
        self.assertNotIn(planted_sites[2], rem)
        self.assertNotIn(planted_sites[3], rem)
        self.assertNotIn(planted_sites[4], rem)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when K=2."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(2)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(0)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(1)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(3)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(31)
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(33)
        )
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 15),)
        planted_stems = ("071",) * 3
        self.assertEqual(
            leftover_extra_remaining_after_090_and_076_with_previous_071(
                planted,
                planted_stems,
            ),
            planted,
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(
                len(planted)
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_EXACTLY_2_SHARE_PREVIOUS_071
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_EXACTLY_2_SHARE_PREVIOUS_071,
            HYPOTHESIS_K == STANDING_K_071,
        )
        self.assertEqual(
            STANDING_K_071 + STANDING_N_REMAINING_AFTER_090_AND_076_AND_071,
            STANDING_N_REMAINING_AFTER_090_AND_076,
        )
        self.assertEqual(2 + 31, 33)
        self.assertEqual(STANDING_K_076 + STANDING_N_REMAINING_AFTER_090_AND_076, STANDING_N_REMAINING_AFTER_090)
        self.assertEqual(2 + 33, 35)
        self.assertEqual(STANDING_K_090 + STANDING_N_REMAINING_AFTER_090, STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(2 + 35, 37)
        self.assertEqual(STANDING_K_600 + STANDING_N_REMAINING_AFTER_600, STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(4 + 37, 41)
        self.assertEqual(STANDING_K_999 + STANDING_N_REMAINING_AFTER_999, STANDING_N_LEFTOVER)
        self.assertEqual(15 + 41, 56)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle270_071_sites_survive_peeling_090_and_076_and_are_not_090_or_076_sites(self):
        """Cycle-270 previous-071 pair is disjoint from previous-090/076; peeling them keeps K_071=2."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle270_071_set(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE270_071_SITES)
        self.assertEqual(STANDING_MATCHING_SITES, STANDING_CYCLE270_071_SITES)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE273_MATCHING_SITES)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE271_MATCHING_SITES)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE270_MATCHING_SITES)
        for site in STANDING_MATCHING_SITES:
            self.assertNotIn(site, CYCLE273_MATCHING_SITES)
            self.assertNotIn(site, CYCLE271_MATCHING_SITES)
            self.assertIn(site, CYCLE270_REMAINING_SITES)
            self.assertIn(site, CYCLE273_REMAINING_AFTER_090_AND_076_SITES)
        for site in CYCLE273_MATCHING_SITES:
            self.assertNotIn(site, STANDING_MATCHING_SITES)
            self.assertNotIn(site, STANDING_REMAINING_AFTER_090_AND_076_SITES)
        for site in CYCLE271_MATCHING_SITES:
            self.assertNotIn(site, STANDING_MATCHING_SITES)
            self.assertNotIn(site, STANDING_REMAINING_AFTER_090_AND_076_SITES)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle270_071_set(planted))
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(
                len(planted)
            )
        )
        swapped = CYCLE273_MATCHING_SITES
        self.assertFalse(matching_equals_cycle270_071_set(swapped))
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(
                len(swapped)
            )
        )
        self.assertEqual(CYCLE270_TIED_STEMS, STANDING_TIED_STEMS_AFTER_600)
        self.assertIn("071", CYCLE270_TIED_STEMS)
        self.assertEqual(CYCLE270_N_TIED_AT_K, 5)
        self.assertEqual(STANDING_CYCLE270_K_071, 2)
        for stem, count, sites, _grams in CYCLE270_FREQUENCY:
            if stem == "071":
                self.assertEqual(count, 2)
                self.assertEqual(sites, STANDING_CYCLE270_071_SITES)
        self.assertTrue(STANDING_DO_NOT_PEEL_045_009)
        self.assertTrue(STANDING_I_ONLY_OF_071_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_RETUNE_272)
        self.assertTrue(STANDING_DO_NOT_RETUNE_274)
        self.assertTrue(STANDING_DO_NOT_PEEL_T_OR_EXTRA_I_OF_090_090_076)
        self.assertTrue(STANDING_DO_NOT_PEEL_T_OR_EXTRA_I_OF_076_090_076)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE271)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE273)
        self.assertFalse(STANDING_SAME_AS_CYCLE273)
        self.assertFalse(STANDING_SAME_AS_CYCLE274)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertTrue(CYCLE271_CLAIM)
        self.assertFalse(CYCLE272_CLAIM)
        self.assertTrue(CYCLE273_CLAIM)
        self.assertFalse(CYCLE274_CLAIM)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter600Prev071Scoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-076 previous-071 lock. Mock only."""

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
        self.share_999 = leftover_extra_with_previous_999(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_after_999 = leftover_extra_remaining_after_999(
            self.leftover_sites,
            self.previous_stems,
        )
        self.share_600 = leftover_extra_remaining_after_999_with_g(
            self.leftover_sites,
            self.previous_stems,
            "600",
        )
        self.remaining_after_600 = leftover_extra_remaining_after_600(
            self.leftover_sites,
            self.previous_stems,
        )
        self.share_090 = leftover_extra_remaining_after_600_with_previous_090(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_after_090 = leftover_extra_remaining_after_090(
            self.leftover_sites,
            self.previous_stems,
        )
        self.share_076 = leftover_extra_remaining_after_090_with_previous_076(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining = leftover_extra_remaining_after_090_and_076(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_extra_remaining_after_090_and_076_previous_stems(
            self.leftover_sites,
            self.previous_stems,
        )
        self.with_previous = leftover_extra_remaining_after_600_with_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.no_previous_600 = leftover_extra_remaining_after_600_without_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.matching = leftover_extra_remaining_after_090_and_076_with_previous_071(
            self.leftover_sites,
            self.previous_stems,
        )
        self.without = leftover_extra_remaining_after_090_and_076_without_previous_071(
            self.leftover_sites,
            self.previous_stems,
        )
        self.share_071_after_600 = leftover_extra_remaining_after_600_with_previous_071(
            self.leftover_sites,
            self.previous_stems,
        )
        self.frequency_600 = remaining_after_600_previous_stem_frequency_table(
            self.leftover_sites,
            self.previous_stems,
            self.backwards,
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
        self.n_with_previous_leftover = len(
            leftover_sites_with_previous(self.leftover_sites, self.previous_stems)
        )
        self.n_no_previous_leftover = len(
            leftover_sites_without_previous(self.leftover_sites, self.previous_stems)
        )
        self.k_999 = len(self.share_999)
        self.n_remaining_after_999 = len(self.remaining_after_999)
        self.k_600 = len(self.share_600)
        self.n_remaining_after_600 = len(self.remaining_after_600)
        self.k_090 = len(self.share_090)
        self.n_remaining_after_090 = len(self.remaining_after_090)
        self.k_076 = len(self.share_076)
        self.n_remaining_after_090_and_076 = len(self.remaining)
        self.n_with_previous = len(self.remaining_stems)
        self.n_no_previous = self.n_remaining_after_090_and_076 - self.n_with_previous
        self.k = len(self.matching)
        self.k_071 = self.k
        self.n_without = len(self.without)
        self.n_remaining_after_090_and_076_and_071 = (
            self.n_remaining_after_090_and_076 - self.k_071
        )
        self.k_071_after_600 = len(self.share_071_after_600)
        self.tied_after_600 = tuple(
            stem for stem, count, _sites, _grams in self.frequency_600 if count == 2
        )
        self.equals_cycle270_071 = matching_equals_cycle270_071_set(self.matching)
        self.claim_holds = i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(
            self.k_071,
        )

    def test_tokens_and_nested_leftover_extra_56_69_k076_2_n33_not_retuned(self):
        """2-gram and leftover extra 56 / N_I=69 / K_076=2 / N_remaining_after_090_and_076=33 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("071", "090", "076"))
        self.assertEqual(GRAM3_NESTED_076, ("076", "090", "076"))
        self.assertEqual(GRAM3_NESTED_090, ("090", "090", "076"))
        self.assertEqual(GRAM3_NESTED_600, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_999, ("999", "090", "076"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_273 = self.survey[
            "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"
        ]
        self.assertEqual(prior_273["cycle"], 273)
        self.assertEqual(prior_273["K_076"], 2)
        self.assertEqual(prior_273["N_remaining_after_090"], 35)
        self.assertEqual(prior_273["N_remaining_after_090_and_076"], 33)
        self.assertEqual(prior_273["N_leftover_extra"], 56)
        self.assertEqual(prior_273["N_I"], 69)
        self.assertTrue(
            prior_273[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_exactly_2_share_previous_076"
            ]
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE273_MATCHING_PREVIOUS_4GRAMS],
            prior_273["matching_previous_4grams"],
        )
        self.assertTrue(CYCLE273_CLAIM)
        self.assertEqual(CYCLE273_K_076, 2)
        self.assertEqual(CYCLE273_N_REMAINING_AFTER_090_AND_076, 33)
        if (
            prior_273["K_076"] != 2
            or prior_273["N_remaining_after_090_and_076"] != 33
            or prior_273["N_leftover_extra"] != 56
            or prior_273["N_I"] != 69
        ):
            self.fail(
                "nested cycle 273 K_076=2 N_remaining_after_090_and_076=33 leftover extra=56 N_I=69 drifted"
            )
        prior_274 = self.survey["i_3gram_076_090_076_i_only"]
        self.assertEqual(prior_274["cycle"], 274)
        self.assertEqual(prior_274["N_I"], 3)
        self.assertEqual(prior_274["N_off_I"], 1)
        self.assertEqual(prior_274["N_extra"], 1)
        self.assertFalse(prior_274["i_3gram_076_090_076_i_only"])
        self.assertFalse(CYCLE274_CLAIM)
        self.assertEqual(CYCLE274_N_I, 3)
        self.assertEqual(CYCLE274_N_OFF_I, 1)
        self.assertEqual(CYCLE274_N_EXTRA, 1)
        prior_271 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]
        self.assertEqual(prior_271["cycle"], 271)
        self.assertEqual(prior_271["K_090"], 2)
        self.assertEqual(prior_271["N_remaining_after_090"], 35)
        self.assertTrue(CYCLE271_CLAIM)
        self.assertEqual(CYCLE271_K_090, 2)
        self.assertEqual(CYCLE271_N_REMAINING_AFTER_090, 35)
        prior_272 = self.survey["i_3gram_090_090_076_i_only"]
        self.assertEqual(prior_272["cycle"], 272)
        self.assertEqual(prior_272["N_I"], 3)
        self.assertEqual(prior_272["N_off_I"], 1)
        self.assertEqual(prior_272["N_extra"], 1)
        self.assertFalse(prior_272["i_3gram_090_090_076_i_only"])
        self.assertFalse(CYCLE272_CLAIM)
        prior_270 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]
        self.assertEqual(prior_270["cycle"], 270)
        self.assertEqual(prior_270["G"], "090")
        self.assertEqual(prior_270["K"], 2)
        self.assertEqual(prior_270["N_remaining_after_600"], 37)
        self.assertFalse(prior_270["G_uniquely_most_frequent"])
        self.assertEqual(tuple(prior_270["tied_stems_at_K"]), STANDING_TIED_STEMS_AFTER_600)
        self.assertIn("071", prior_270["tied_stems_at_K"])
        self.assertEqual(prior_270["N_tied_at_K"], 5)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        prior_268 = self.survey["i_3gram_600_090_076_i_only"]
        self.assertEqual(prior_268["cycle"], 268)
        self.assertEqual(prior_268["N_I"], 6)
        self.assertEqual(prior_268["N_off_I"], 0)
        self.assertEqual(prior_268["N_extra"], 2)
        self.assertTrue(prior_268["i_3gram_600_090_076_i_only"])
        self.assertTrue(CYCLE268_CLAIM)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_045_009)
        self.assertTrue(STANDING_I_ONLY_OF_071_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_RETUNE_272)
        self.assertTrue(STANDING_DO_NOT_RETUNE_274)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_PREVIOUS_999_600_090_076_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE268_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE269_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE271_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE272_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE273_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE274_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_of_33_and_hypothesis_k_2_holds(self):
        """N_remaining_after_090_and_076=33, cycle-270 071 still K=2, K_071=2. Claim holds."""
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
        self.assertEqual(self.n_with_previous_leftover, STANDING_N_WITH_PREVIOUS_LEFTOVER)
        self.assertEqual(STANDING_N_WITH_PREVIOUS_LEFTOVER, 56)
        self.assertEqual(self.n_no_previous_leftover, STANDING_N_NO_PREVIOUS_LEFTOVER)
        self.assertEqual(STANDING_N_NO_PREVIOUS_LEFTOVER, 0)
        self.assertEqual(self.k_999, STANDING_K_999)
        self.assertEqual(STANDING_K_999, 15)
        self.assertEqual(self.share_999, CYCLE261_MATCHING_SITES)
        if self.k_999 != 15:
            self.fail("nested cycle 261 K_999 drifted from 15")
        self.assertEqual(self.n_remaining_after_999, STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(STANDING_N_REMAINING_AFTER_999, 41)
        self.assertEqual(self.k_600, STANDING_K_600)
        self.assertEqual(STANDING_K_600, 4)
        self.assertEqual(self.share_600, CYCLE267_MATCHING_SITES)
        if self.k_600 != 4:
            self.fail("nested cycle 267 K_600 drifted from 4")
        self.assertEqual(self.n_remaining_after_600, STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(STANDING_N_REMAINING_AFTER_600, 37)
        self.assertEqual(self.remaining_after_600, CYCLE270_REMAINING_SITES)
        self.assertEqual(self.k_090, STANDING_K_090)
        self.assertEqual(STANDING_K_090, 2)
        self.assertEqual(self.share_090, CYCLE271_MATCHING_SITES)
        if self.k_090 != 2:
            self.fail("nested-check K_090 drifted from 2")
        self.assertEqual(self.n_remaining_after_090, STANDING_N_REMAINING_AFTER_090)
        self.assertEqual(STANDING_N_REMAINING_AFTER_090, 35)
        self.assertEqual(self.n_remaining_after_090, CYCLE271_N_REMAINING_AFTER_090)
        self.assertEqual(self.n_remaining_after_090, self.n_remaining_after_600 - self.k_090)
        self.assertEqual(37 - 2, 35)
        if self.n_remaining_after_090 != 35:
            self.fail("measured N_remaining_after_090 drifted from 35")
        self.assertEqual(self.k_076, STANDING_K_076)
        self.assertEqual(STANDING_K_076, 2)
        self.assertEqual(self.share_076, CYCLE273_MATCHING_SITES)
        if self.k_076 != 2:
            self.fail("nested-check K_076 drifted from 2")
        self.assertEqual(self.n_remaining_after_090_and_076, STANDING_N_REMAINING_AFTER_090_AND_076)
        self.assertEqual(STANDING_N_REMAINING_AFTER_090_AND_076, 33)
        self.assertEqual(self.n_remaining_after_090_and_076, CYCLE273_N_REMAINING_AFTER_090_AND_076)
        self.assertEqual(
            self.n_remaining_after_090_and_076,
            self.n_remaining_after_090 - self.k_076,
        )
        self.assertEqual(35 - 2, 33)
        if self.n_remaining_after_090_and_076 != 33:
            self.fail("measured N_remaining_after_090_and_076 drifted from 33")
        self.assertTrue(
            leftover_extra_remaining_after_090_and_076_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining_after_999,
                self.k_600,
                self.n_remaining_after_600,
                self.k_090,
                self.n_remaining_after_090,
                self.k_076,
                self.n_remaining_after_090_and_076,
            )
        )
        self.assertTrue(
            leftover_extra_remaining_after_090_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining_after_999,
                self.k_600,
                self.n_remaining_after_600,
                self.k_090,
                self.n_remaining_after_090,
            )
        )
        self.assertTrue(
            leftover_extra_remaining_after_600_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining_after_999,
                self.k_600,
                self.n_remaining_after_600,
            )
        )
        self.assertTrue(
            leftover_extra_remaining_after_999_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining_after_999,
            )
        )
        self.assertEqual(self.remaining, STANDING_REMAINING_AFTER_090_AND_076_SITES)
        self.assertEqual(self.remaining, CYCLE273_REMAINING_AFTER_090_AND_076_SITES)
        self.assertEqual(
            self.remaining_stems,
            STANDING_REMAINING_AFTER_090_AND_076_PREVIOUS_STEMS,
        )
        self.assertEqual(
            self.remaining,
            leftover_extra_remaining_after_090_without_previous_076(
                self.leftover_sites,
                self.previous_stems,
            ),
        )
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 33)
        self.assertEqual(self.n_no_previous, STANDING_N_NO_PREVIOUS)
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertEqual(
            self.n_with_previous + self.n_no_previous,
            self.n_remaining_after_090_and_076,
        )
        self.assertEqual(33 + 0, 33)
        for site in self.share_999:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in self.share_600:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in self.share_090:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in self.share_076:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        self.assertEqual(self.tied_after_600, STANDING_TIED_STEMS_AFTER_600)
        self.assertEqual(self.tied_after_600, CYCLE270_TIED_STEMS)
        self.assertIn("071", self.tied_after_600)
        self.assertEqual(len(self.tied_after_600), STANDING_N_TIED_AT_K_AFTER_600)
        self.assertEqual(STANDING_N_TIED_AT_K_AFTER_600, 5)
        if "071" not in self.tied_after_600 or self.k_071_after_600 != 2:
            self.fail("nested cycle 270 5-way no longer includes 071 at K=2")
        self.assertEqual(self.k_071_after_600, STANDING_CYCLE270_K_071)
        self.assertEqual(STANDING_CYCLE270_K_071, 2)
        self.assertEqual(self.share_071_after_600, STANDING_CYCLE270_071_SITES)
        self.assertEqual(self.share_071_after_600, self.matching)
        self.assertTrue(STANDING_071_STILL_MAX_K_AFTER_600)
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(self.k_071, STANDING_K_071)
        self.assertEqual(STANDING_K_071, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_071, 2)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 31)
        self.assertEqual(
            self.n_remaining_after_090_and_076_and_071,
            STANDING_N_REMAINING_AFTER_090_AND_076_AND_071,
        )
        self.assertEqual(STANDING_N_REMAINING_AFTER_090_AND_076_AND_071, 31)
        self.assertEqual(
            self.k_071 + self.n_remaining_after_090_and_076_and_071,
            self.n_remaining_after_090_and_076,
        )
        self.assertEqual(2 + 31, 33)
        if self.k_071 != 2:
            self.fail("nested-check K_071 drifted from 2")
        leftover_g, leftover_k, leftover_unique = select_previous_g(self.previous_stems)
        self.assertEqual(leftover_g, "999")
        self.assertEqual(leftover_k, 15)
        self.assertTrue(leftover_unique)
        rem999_g, rem999_k, rem999_unique = select_remaining_after_999_g(
            leftover_extra_remaining_after_999_previous_stems(
                self.leftover_sites,
                self.previous_stems,
            )
        )
        self.assertEqual(rem999_g, "600")
        self.assertEqual(rem999_k, 4)
        self.assertTrue(rem999_unique)
        rem600_g, rem600_k, rem600_unique = select_remaining_after_600_g(
            leftover_extra_remaining_after_600_previous_stems(
                self.leftover_sites,
                self.previous_stems,
            )
        )
        self.assertEqual(rem600_g, "090")
        self.assertEqual(rem600_k, 2)
        self.assertFalse(rem600_unique)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071(
                self.k_071
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_EXACTLY_2_SHARE_PREVIOUS_071,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_EXACTLY_2_SHARE_PREVIOUS_071
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_090_AND_076_AND_071_SITES)
        self.assertTrue(self.equals_cycle270_071)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE270_071_SITES)
        self.assertTrue(matching_equals_cycle270_071_set(self.matching))
        if len(self.matching) != 2 or not self.equals_cycle270_071:
            self.fail(
                "leftover extra remaining-after-076 previous-071 set drifted from cycle-270 071 pair"
            )
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE264)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertFalse(STANDING_SAME_AS_CYCLE271)
        self.assertFalse(STANDING_SAME_AS_CYCLE272)
        self.assertFalse(STANDING_SAME_AS_CYCLE273)
        self.assertFalse(STANDING_SAME_AS_CYCLE274)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE271)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE273)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_045_009)
        self.assertTrue(STANDING_I_ONLY_OF_071_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_RETUNE_272)
        self.assertTrue(STANDING_DO_NOT_RETUNE_274)
        self.assertTrue(STANDING_DO_NOT_PEEL_T_OR_EXTRA_I_OF_090_090_076)
        self.assertTrue(STANDING_DO_NOT_PEEL_T_OR_EXTRA_I_OF_076_090_076)
        self.assertTrue(STANDING_CYCLE264_IS_DIFFERENT_CLUSTER)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertFalse(CYCLE274_CLAIM)
        self.assertTrue(CYCLE273_CLAIM)
        self.assertFalse(CYCLE272_CLAIM)
        self.assertTrue(CYCLE271_CLAIM)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertTrue(CYCLE268_CLAIM)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertTrue(CYCLE266_CLAIM)
        self.assertTrue(CYCLE264_CLAIM)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_remaining_after_076_sites_have_previous_071(self):
        """Two remaining-after-090-and-076 leftover extra sites are 071 090 076."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia3", 87), ("076", "071", "090", "076")),
            ((SIDE_IA, "Ia7", 88), ("092", "071", "090", "076")),
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
            self.assertEqual(stems[index - 1], "071")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "071")
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), GRAM3_BACKWARD)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev)
            self.assertEqual(prev4, want_prev)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, self.remaining)
            self.assertIn(site, CYCLE270_REMAINING_SITES)
            self.assertIn(site, CYCLE273_REMAINING_AFTER_090_AND_076_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE261_MATCHING_SITES)
            self.assertNotIn(site, CYCLE267_MATCHING_SITES)
            self.assertNotIn(site, CYCLE271_MATCHING_SITES)
            self.assertNotIn(site, CYCLE273_MATCHING_SITES)
            self.assertNotIn(site, CYCLE264_MATCHING_SITES)
            self.assertIn(site, STANDING_CYCLE270_071_SITES)
        self.assertEqual(self.matching, STANDING_CYCLE270_071_SITES)
        self.assertTrue(matching_equals_cycle270_071_set(self.matching))
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            prev = site_previous_stem(stems, index, GRAM2)
            self.assertIsNotNone(prev)
            self.assertNotEqual(prev, "071")
            self.assertNotEqual(prev, "076")
            self.assertNotEqual(prev, "090")
            self.assertNotEqual(prev, "600")
            self.assertNotEqual(prev, "999")
            self.assertIn(site, self.remaining)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_CYCLE270_071_SITES)
        for site in self.share_999:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE261_MATCHING_SITES)
        for site in self.share_600:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE267_MATCHING_SITES)
        for site in self.share_090:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE271_MATCHING_SITES)
        for site in self.share_076:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE273_MATCHING_SITES)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in CYCLE264_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in CYCLE272_I_SITES:
            self.assertNotIn(site, self.matching)
        for site in CYCLE274_I_SITES:
            self.assertNotIn(site, self.matching)
        for stem in STANDING_OTHER_TIED_STEMS:
            other = leftover_extra_remaining_after_090_and_076_with_previous_071(
                self.leftover_sites,
                self.previous_stems,
                stem,
            )
            self.assertEqual(len(other), 2)
            self.assertNotEqual(other, self.matching)
            for site in other:
                self.assertNotIn(site, self.matching)
                self.assertIn(site, self.remaining)
        self.assertEqual(len(self.without), STANDING_N_REMAINING_AFTER_090_AND_076_AND_071)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, prev4, _nxt4), want in zip(
            local,
            STANDING_MATCHING_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertEqual(prev4, want)
        self.assertEqual(
            matching_leftover_extra_remaining_after_090_and_076_previous_071_local_4gram_rows(),
            [
                {
                    "tablet": "I",
                    "side": SIDE_IA,
                    "line": "Ia3",
                    "index": 87,
                    "previous_4gram": ["076", "071", "090", "076"],
                    "backward_3gram": ["071", "090", "076"],
                },
                {
                    "tablet": "I",
                    "side": SIDE_IA,
                    "line": "Ia7",
                    "index": 88,
                    "previous_4gram": ["092", "071", "090", "076"],
                    "backward_3gram": ["071", "090", "076"],
                },
            ],
        )
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertTrue(STANDING_DO_NOT_PEEL_045_009)
        self.assertTrue(STANDING_I_ONLY_OF_071_090_076_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_CYCLE264_IS_DIFFERENT_CLUSTER)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_274_273_272_271_270_268_and_223_still_compute(self):
        """Cycle 274 3/1 extra I=1, 273 K_076=2/33, 272 3/1, 271 K_090=2/35, 270 5-way G=090, 268 6/0 stay."""
        prior_274 = TestMamariI3gram076090076IOnlyScoreboard()
        prior_274.setUp()
        prior_274.test_3gram_is_one_off_i_and_not_i_only()
        prior_274.test_survey_matches_computed_lock()
        self.assertEqual(prior_274.i_hits, CYCLE274_N_I)
        self.assertEqual(prior_274.i_hits, 3)
        self.assertEqual(prior_274.off_i_hits, CYCLE274_N_OFF_I)
        self.assertEqual(prior_274.off_i_hits, 1)
        self.assertEqual(prior_274.i_sites, CYCLE274_I_SITES)
        self.assertEqual(prior_274.off_i_sites, CYCLE274_OFF_I_SITES)
        self.assertEqual(len(prior_274.extra), 1)
        self.assertEqual(prior_274.extra, CYCLE274_EXTRA_I_SITES)
        self.assertFalse(prior_274.claim_holds)
        self.assertFalse(CYCLE274_CLAIM)
        self.assertEqual(CYCLE274_N_I, 3)
        self.assertEqual(CYCLE274_N_OFF_I, 1)
        self.assertEqual(CYCLE274_N_EXTRA, 1)
        if prior_274.i_hits != 3 or prior_274.off_i_hits != 1 or len(prior_274.extra) != 1:
            self.fail("nested cycle 274 076 090 076 I-only 3/1 extra I=1 drifted")
        prior_273 = TestMamariILeftoverExtra090076RemainingAfter600Prev076Scoreboard()
        prior_273.setUp()
        prior_273.test_counts_2_of_35_and_hypothesis_k_2_holds()
        prior_273.test_survey_matches_computed_lock()
        self.assertEqual(prior_273.k_076, 2)
        self.assertEqual(prior_273.n_remaining_after_090_and_076, 33)
        self.assertEqual(prior_273.matching, CYCLE273_MATCHING_SITES)
        self.assertEqual(prior_273.matching_previous_4grams, CYCLE273_MATCHING_PREVIOUS_4GRAMS)
        self.assertTrue(prior_273.claim_holds)
        self.assertTrue(CYCLE273_CLAIM)
        self.assertEqual(CYCLE273_K_076, 2)
        self.assertEqual(CYCLE273_N_REMAINING_AFTER_090_AND_076, 33)
        self.assertEqual(
            CYCLE273_MATCHING_PREVIOUS_4GRAMS,
            (("076", "076", "090", "076"), ("071", "076", "090", "076")),
        )
        if (
            prior_273.k_076 != 2
            or prior_273.n_remaining_after_090_and_076 != 33
            or prior_273.matching_previous_4grams != CYCLE273_MATCHING_PREVIOUS_4GRAMS
        ):
            self.fail(
                "nested cycle 273 leftover extra remaining-after-600 remaining-after-090 "
                "previous-076 K_076=2 N_remaining_after_090_and_076=33 drifted"
            )
        prior_272 = TestMamariI3gram090090076IOnlyScoreboard()
        prior_272.setUp()
        prior_272.test_3gram_is_one_off_i_and_not_i_only()
        prior_272.test_survey_matches_computed_lock()
        self.assertEqual(prior_272.i_hits, CYCLE272_N_I)
        self.assertEqual(prior_272.i_hits, 3)
        self.assertEqual(prior_272.off_i_hits, CYCLE272_N_OFF_I)
        self.assertEqual(prior_272.off_i_hits, 1)
        self.assertEqual(prior_272.i_sites, CYCLE272_I_SITES)
        self.assertEqual(prior_272.off_i_sites, CYCLE272_OFF_I_SITES)
        self.assertEqual(len(prior_272.extra), 1)
        self.assertEqual(prior_272.extra, CYCLE272_EXTRA_I_SITES)
        self.assertFalse(prior_272.claim_holds)
        self.assertFalse(CYCLE272_CLAIM)
        if prior_272.i_hits != 3 or prior_272.off_i_hits != 1 or len(prior_272.extra) != 1:
            self.fail("nested cycle 272 090 090 076 I-only 3/1 extra I=1 drifted")
        prior_271 = TestMamariILeftoverExtra090076RemainingAfter600Previous090Scoreboard()
        prior_271.setUp()
        prior_271.test_counts_2_of_37_and_hypothesis_k_2_holds()
        prior_271.test_survey_matches_computed_lock()
        self.assertEqual(prior_271.k_090, 2)
        self.assertEqual(prior_271.n_remaining_after_090, 35)
        self.assertEqual(prior_271.matching, CYCLE271_MATCHING_SITES)
        self.assertEqual(prior_271.matching_previous_4grams, CYCLE271_MATCHING_PREVIOUS_4GRAMS)
        self.assertTrue(prior_271.claim_holds)
        self.assertTrue(CYCLE271_CLAIM)
        self.assertEqual(CYCLE271_K_090, 2)
        self.assertEqual(CYCLE271_N_REMAINING_AFTER_090, 35)
        if (
            prior_271.k_090 != 2
            or prior_271.n_remaining_after_090 != 35
            or prior_271.matching_previous_4grams != CYCLE271_MATCHING_PREVIOUS_4GRAMS
        ):
            self.fail(
                "nested cycle 271 K_090=2 N_remaining_after_090=35 both previous 4-grams "
                "011 090 090 076 drifted"
            )
        prior_270 = TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard()
        prior_270.setUp()
        prior_270.test_counts_37_remaining_g_090_k_2_five_way_tie_and_hypothesis_loses()
        prior_270.test_survey_matches_computed_lock()
        self.assertEqual(prior_270.g, "090")
        self.assertEqual(prior_270.k, 2)
        self.assertEqual(prior_270.n_remaining, 37)
        self.assertEqual(prior_270.n_distinct, 32)
        self.assertFalse(prior_270.unique)
        self.assertFalse(prior_270.claim_holds)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_REMAINING, 37)
        self.assertEqual(CYCLE270_N_DISTINCT, 32)
        self.assertEqual(CYCLE270_N_HAPAX, 27)
        tied = tuple(
            stem for stem, count, _sites, _grams in prior_270.frequency if count == 2
        )
        self.assertEqual(tied, CYCLE270_TIED_STEMS)
        self.assertIn("071", tied)
        self.assertEqual(len(tied), 5)
        if (
            prior_270.g != "090"
            or prior_270.k != 2
            or prior_270.n_remaining != 37
            or prior_270.unique
            or prior_270.claim_holds
            or "071" not in tied
        ):
            self.fail(
                "nested cycle 270 leftover extra remaining-after-600 37 / "
                "5-way tie G=090 K=2 including 071 drifted"
            )
        prior_268 = TestMamariI3gram600090076IOnlyScoreboard()
        prior_268.setUp()
        prior_268.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE268_CLAIM)
        self.assertEqual(CYCLE268_N_I, 6)
        self.assertEqual(CYCLE268_N_OFF_I, 0)
        self.assertEqual(CYCLE268_N_EXTRA, 2)
        prior_267 = TestMamariILeftoverExtra090076RemainingAfter999Previous600Scoreboard()
        prior_267.setUp()
        prior_267.test_counts_4_of_41_and_hypothesis_k_4_holds()
        prior_267.test_survey_matches_computed_lock()
        self.assertEqual(prior_267.k_600, 4)
        self.assertEqual(prior_267.n_remaining_after_600, 37)
        self.assertTrue(prior_267.claim_holds)
        self.assertTrue(CYCLE267_CLAIM)
        if prior_267.k_600 != 4 or prior_267.n_remaining_after_600 != 37:
            self.fail("nested cycle 267 K_600=4 N_remaining_after_600=37 drifted")
        prior_266 = TestMamariILeftoverExtra090076RemainingAfter999PreviousStemScoreboard()
        prior_266.setUp()
        prior_266.test_counts_41_remaining_g_600_k_4_and_hypothesis_holds()
        prior_266.test_survey_matches_computed_lock()
        self.assertEqual(prior_266.g, "600")
        self.assertEqual(prior_266.k, 4)
        self.assertTrue(prior_266.unique)
        self.assertTrue(prior_266.claim_holds)
        self.assertTrue(CYCLE266_CLAIM)
        if prior_266.g != "600" or prior_266.k != 4 or not prior_266.unique:
            self.fail("nested cycle 266 unique-max G=600 K=4 drifted")
        prior_264 = TestMamariI999090076Previous090Scoreboard()
        prior_264.setUp()
        prior_264.test_counts_exactly_2_share_previous_090_and_hypothesis_holds()
        prior_264.test_survey_matches_computed_lock()
        self.assertEqual(prior_264.k_090, 2)
        self.assertEqual(prior_264.matching, CYCLE264_MATCHING_SITES)
        self.assertTrue(prior_264.claim_holds)
        self.assertTrue(CYCLE264_CLAIM)
        self.assertEqual(CYCLE264_K_090, 2)
        self.assertNotEqual(prior_264.matching, self.matching)
        if prior_264.k_090 != 2:
            self.fail("nested cycle 264 K_090=2 drifted")
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertTrue(prior_261.claim_holds)
        self.assertTrue(CYCLE261_CLAIM)
        if prior_261.k_999 != 15 or prior_261.n_remaining_after_999 != 41:
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 drifted")
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(prior_260.g, "999")
        self.assertEqual(prior_260.k, 15)
        self.assertFalse(prior_260.claim_holds)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertTrue(CYCLE260_UNIQUE)
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
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, 16)
        self.assertEqual(prior_167.off_i_hits, 0)
        self.assertTrue(CYCLE167_CLAIM)
        self.assertEqual(CYCLE167_N_I, 16)
        self.assertEqual(CYCLE167_N_OFF_I, 0)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_269 = TestMamariI600090076Previous4gramsIOnlyScoreboard()
        prior_269.setUp()
        prior_269.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE269_ALL_HAPAX)
        self.assertEqual(CYCLE269_N_I_ONLY, 6)
        self.assertEqual(CYCLE269_N_NOT_HAPAX, 0)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        unused = CYCLE207_GRAM3
        self.assertEqual(unused, ("090", "076", "070"))
        unused_n = STANDING_N_I
        self.assertEqual(unused_n, 69)
        unused_273 = CYCLE273_N_REMAINING_AFTER_090_AND_076
        self.assertEqual(unused_273, 33)
        unused_271 = CYCLE271_N_REMAINING_AFTER_090
        self.assertEqual(unused_271, 35)
        unused_270 = CYCLE270_N_REMAINING
        self.assertEqual(unused_270, 37)
        unused_268 = CYCLE268_N_EXTRA
        self.assertEqual(unused_268, 2)
        unused_264 = CYCLE264_K_090
        self.assertEqual(unused_264, 2)
        unused_261 = CYCLE261_N_LEFTOVER_EXTRA
        self.assertEqual(unused_261, 56)
        unused_235 = CYCLE235_K
        self.assertEqual(unused_235, 2)
        unused_267_g = CYCLE267_G
        self.assertEqual(unused_267_g, "600")
        unused_266_unique = CYCLE266_UNIQUE
        self.assertTrue(unused_266_unique)
        unused_266_k = CYCLE266_K
        self.assertEqual(unused_266_k, 4)
        unused_267_n = CYCLE267_N_REMAINING_AFTER_600
        self.assertEqual(unused_267_n, 37)
        unused_261_rem = CYCLE261_N_REMAINING_AFTER_999
        self.assertEqual(unused_261_rem, 41)
        unused_no_prev = leftover_sites_without_previous
        self.assertTrue(callable(unused_no_prev))
        unused_with_prev = leftover_sites_with_previous
        self.assertTrue(callable(unused_with_prev))
        unused_235_claim = CYCLE235_CLAIM
        self.assertTrue(unused_235_claim)
        unused_without_090 = leftover_extra_remaining_after_600_without_previous_090
        self.assertTrue(callable(unused_without_090))
        unused_without_600 = leftover_extra_remaining_after_999_without_previous_600
        self.assertTrue(callable(unused_without_600))
        unused_without_g = leftover_extra_remaining_after_600_without_g
        self.assertTrue(callable(unused_without_g))
        unused_after_090_stems = leftover_extra_remaining_after_090_previous_stems
        self.assertTrue(callable(unused_after_090_stems))
        unused_after_090 = leftover_extra_remaining_after_090
        self.assertTrue(callable(unused_after_090))
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_DO_NOT_PEEL_045_009)
        self.assertTrue(STANDING_DO_NOT_RETUNE_272)
        self.assertTrue(STANDING_DO_NOT_RETUNE_274)
        self.assertTrue(STANDING_DO_NOT_PEEL_T_OR_EXTRA_I_OF_090_090_076)
        self.assertTrue(STANDING_DO_NOT_PEEL_T_OR_EXTRA_I_OF_076_090_076)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE268_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE269_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE271_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE272_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE273_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE274_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-275 leftover extra remaining-after-076 previous-071 lock."""
        lock = self.survey[
            "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_previous_071"
        ]
        self.assertEqual(lock["cycle"], 275)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(tuple(lock["backward_3gram"]), ("071", "090", "076"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(
            tuple(lock["locked_previous_stems_after_076"]),
            LOCKED_PREVIOUS_STEMS_AFTER_076,
        )
        self.assertEqual(
            tuple(lock["locked_previous_stems_after_076"]),
            ("999", "600", "090", "076"),
        )
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
        self.assertEqual(lock["N_with_previous_leftover"], STANDING_N_WITH_PREVIOUS_LEFTOVER)
        self.assertEqual(lock["N_no_previous_leftover"], STANDING_N_NO_PREVIOUS_LEFTOVER)
        self.assertEqual(lock["K_999"], STANDING_K_999)
        self.assertEqual(lock["K_999"], 15)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_999_sites"]),
            CYCLE261_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_999"], STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(lock["N_remaining_after_999"], 41)
        self.assertEqual(lock["K_600"], STANDING_K_600)
        self.assertEqual(lock["K_600"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_600_sites"]),
            CYCLE267_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_600"], STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(lock["N_remaining_after_600"], 37)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_600_sites"]),
            CYCLE270_REMAINING_SITES,
        )
        self.assertEqual(lock["K_090"], STANDING_K_090)
        self.assertEqual(lock["K_090"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_090_sites"]),
            CYCLE271_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_090"], STANDING_N_REMAINING_AFTER_090)
        self.assertEqual(lock["N_remaining_after_090"], 35)
        self.assertEqual(lock["K_076"], STANDING_K_076)
        self.assertEqual(lock["K_076"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_076_sites"]),
            CYCLE273_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_090_and_076"], STANDING_N_REMAINING_AFTER_090_AND_076)
        self.assertEqual(lock["N_remaining_after_090_and_076"], 33)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_090_and_076_sites"]),
            STANDING_REMAINING_AFTER_090_AND_076_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_090_and_076_previous_stems"]),
            STANDING_REMAINING_AFTER_090_AND_076_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 33)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(
            lock["N_distinct_remaining_after_090_and_076"],
            STANDING_N_DISTINCT_REMAINING_AFTER_090_AND_076,
        )
        self.assertEqual(lock["N_distinct_remaining_after_090_and_076"], 30)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "071")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertEqual(lock["K_071"], STANDING_K_071)
        self.assertEqual(lock["K_071"], 2)
        self.assertEqual(lock["cycle270_K_071"], STANDING_CYCLE270_K_071)
        self.assertEqual(lock["cycle270_K_071"], 2)
        self.assertTrue(lock["071_still_max_K_after_600"])
        self.assertEqual(tuple(lock["tied_stems_at_K_after_600"]), STANDING_TIED_STEMS_AFTER_600)
        self.assertEqual(lock["N_tied_at_K_after_600"], STANDING_N_TIED_AT_K_AFTER_600)
        self.assertEqual(lock["N_tied_at_K_after_600"], 5)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 31)
        self.assertEqual(
            lock["N_remaining_after_090_and_076_and_071"],
            STANDING_N_REMAINING_AFTER_090_AND_076_AND_071,
        )
        self.assertEqual(lock["N_remaining_after_090_and_076_and_071"], 31)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_090_and_076_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_090_and_076_sites"]),
            STANDING_CYCLE270_071_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle270_071_sites"])
        self.assertEqual(
            lock["matching_equals_cycle270_071_sites"],
            STANDING_MATCHING_EQUALS_CYCLE270_071_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_090_and_076_local_4grams"],
            matching_leftover_extra_remaining_after_090_and_076_previous_071_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_090_and_076_and_071_sites"]),
            STANDING_REMAINING_AFTER_090_AND_076_AND_071_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle270_071_sites"]),
            STANDING_CYCLE270_071_SITES,
        )
        self.assertEqual(lock["cycle270_N_remaining_after_600"], CYCLE270_N_REMAINING)
        self.assertEqual(lock["cycle270_N_remaining_after_600"], 37)
        self.assertEqual(lock["cycle270_N_distinct_remaining"], CYCLE270_N_DISTINCT)
        self.assertEqual(lock["cycle270_N_distinct_remaining"], 32)
        self.assertEqual(lock["cycle270_N_hapax_remaining"], CYCLE270_N_HAPAX)
        self.assertEqual(lock["cycle270_N_hapax_remaining"], 27)
        self.assertEqual(lock["cycle270_N_tied_at_K"], CYCLE270_N_TIED_AT_K)
        self.assertEqual(lock["cycle270_N_tied_at_K"], 5)
        self.assertEqual(tuple(lock["cycle270_tied_stems_at_K"]), CYCLE270_TIED_STEMS)
        self.assertIn("071", lock["cycle270_tied_stems_at_K"])
        self.assertFalse(lock["cycle270_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle270_G"], CYCLE270_G)
        self.assertEqual(lock["cycle270_G"], "090")
        self.assertEqual(lock["cycle270_K"], CYCLE270_K)
        self.assertEqual(lock["cycle270_K"], 2)
        self.assertFalse(lock["cycle270_unique_previous_stem"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071"
            ]
        )
        self.assertEqual(
            lock[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_exactly_2_share_previous_071"
            ],
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_EXACTLY_2_SHARE_PREVIOUS_071,
        )
        self.assertEqual(lock["nested_cycle274_N_I"], 3)
        self.assertEqual(lock["nested_cycle274_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle274_N_extra"], 1)
        self.assertFalse(lock["nested_cycle274_i_only"])
        self.assertEqual(lock["nested_cycle273_K_076"], 2)
        self.assertEqual(lock["nested_cycle273_N_remaining_after_090"], 35)
        self.assertEqual(lock["nested_cycle273_N_remaining_after_090_and_076"], 33)
        self.assertEqual(
            [list(gram) for gram in CYCLE273_MATCHING_PREVIOUS_4GRAMS],
            lock["nested_cycle273_matching_previous_4grams"],
        )
        self.assertTrue(lock["nested_cycle273_exactly_2_share_previous_076"])
        self.assertEqual(lock["nested_cycle272_N_I"], 3)
        self.assertEqual(lock["nested_cycle272_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle272_N_extra"], 1)
        self.assertFalse(lock["nested_cycle272_i_only"])
        self.assertEqual(lock["nested_cycle271_K_090"], 2)
        self.assertEqual(lock["nested_cycle271_N_remaining_after_090"], 35)
        self.assertEqual(
            [list(gram) for gram in CYCLE271_MATCHING_PREVIOUS_4GRAMS],
            lock["nested_cycle271_matching_previous_4grams"],
        )
        self.assertTrue(lock["nested_cycle271_exactly_2_share_previous_090"])
        self.assertEqual(lock["nested_cycle270_G"], "090")
        self.assertEqual(lock["nested_cycle270_K"], 2)
        self.assertEqual(lock["nested_cycle270_N_remaining_after_600"], 37)
        self.assertEqual(lock["nested_cycle270_N_distinct_remaining"], 32)
        self.assertEqual(lock["nested_cycle270_N_hapax_remaining"], 27)
        self.assertEqual(lock["nested_cycle270_N_tied_at_K"], 5)
        self.assertFalse(lock["nested_cycle270_unique_previous_stem"])
        self.assertIn("071", lock["nested_cycle270_tied_stems_at_K"])
        self.assertEqual(lock["nested_cycle268_N_I"], 6)
        self.assertEqual(lock["nested_cycle268_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle268_N_extra"], 2)
        self.assertEqual(lock["nested_cycle267_K_600"], 4)
        self.assertEqual(lock["nested_cycle267_N_remaining_after_600"], 37)
        self.assertEqual(lock["nested_cycle266_G"], "600")
        self.assertEqual(lock["nested_cycle266_K"], 4)
        self.assertTrue(lock["nested_cycle266_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle264_K_090"], 2)
        self.assertTrue(lock["nested_cycle264_exactly_2_share_previous_090"])
        self.assertTrue(lock["nested_cycle264_is_different_cluster"])
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle235"])
        self.assertFalse(lock["same_as_cycle264"])
        self.assertFalse(lock["same_as_cycle270"])
        self.assertFalse(lock["same_as_cycle271"])
        self.assertFalse(lock["same_as_cycle272"])
        self.assertFalse(lock["same_as_cycle273"])
        self.assertFalse(lock["same_as_cycle274"])
        self.assertTrue(lock["same_claim_shape_as_cycle235"])
        self.assertTrue(lock["same_claim_shape_as_cycle271"])
        self.assertTrue(lock["same_claim_shape_as_cycle273"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_045_009"])
        self.assertTrue(lock["i_only_of_071_090_076_is_not_this_cycle"])
        self.assertTrue(lock["do_not_retune_272"])
        self.assertTrue(lock["do_not_retune_274"])
        self.assertTrue(lock["do_not_peel_t_or_extra_i_of_090_090_076"])
        self.assertTrue(lock["do_not_peel_t_or_extra_i_of_076_090_076"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["previous_999_600_090_076_not_retuned"])
        self.assertTrue(lock["cycle167_not_overwritten"])
        self.assertTrue(lock["cycle268_not_overwritten"])
        self.assertTrue(lock["cycle269_not_overwritten"])
        self.assertTrue(lock["cycle271_not_overwritten"])
        self.assertTrue(lock["cycle272_not_retuned"])
        self.assertTrue(lock["cycle273_not_overwritten"])
        self.assertTrue(lock["cycle274_not_retuned"])
        self.assertTrue(lock["cycle264_is_different_cluster"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["raw_stems_090_kept"])
        self.assertTrue(lock["standing_i_3gram_076_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076_unchanged"]
        )
        self.assertTrue(lock["standing_i_3gram_090_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_090_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_3gram_600_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_600_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_999_090_076_previous_090_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"]["cycle"],
            273,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"][
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_exactly_2_share_previous_076"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"]["K_076"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"][
                "N_remaining_after_090_and_076"
            ],
            33,
        )
        self.assertEqual(self.survey["i_3gram_076_090_076_i_only"]["cycle"], 274)
        self.assertEqual(self.survey["i_3gram_076_090_076_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_076_090_076_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_076_090_076_i_only"]["N_extra"], 1)
        self.assertFalse(self.survey["i_3gram_076_090_076_i_only"]["i_3gram_076_090_076_i_only"])
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]["cycle"],
            271,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"][
                "i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]["K_090"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"][
                "N_remaining_after_090"
            ],
            35,
        )
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["cycle"], 272)
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["N_extra"], 1)
        self.assertFalse(self.survey["i_3gram_090_090_076_i_only"]["i_3gram_090_090_076_i_only"])
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["cycle"],
            270,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["G"],
            "090",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["K"],
            2,
        )
        self.assertIn(
            "071",
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "tied_stems_at_K"
            ],
        )
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["cycle"], 268)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_extra"], 2)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["cycle"],
            267,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["K_600"],
            4,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]["cycle"],
            266,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]["G"],
            "600",
        )
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["cycle"], 264)
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["K_090"], 2)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["cycle"], 261)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["K_999"], 15)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
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


class TestMamariILeftoverExtra090076RemainingAfter600Prev071ImageSnapshot(
    unittest.TestCase
):
    """Cycle 275 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
