"""I's cycle-244 leftover extra remaining-after-280 forward-087 cluster lock.

Cycle 244 text-search lock. Uses already-vendored A–V and the
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

Cycle 234 lost unique most frequent remaining-after-001 next
stem: N_remaining4=33, 7-way tie at count 2, tie-break G=700
K=2. Cycle 235 locked exactly 2 share 700. Cycles 236–237
closed that 700 cluster at n=4 forward (2/0 I-only; two
forward 4-grams hapax 1/0). Cycle 238 locked exactly 2 share
530. Cycles 239–240 closed that 530 cluster at n=4 forward
(2/0 I-only; two forward 4-grams hapax 1/0). Cycle 241 locked
exactly 2 share 280. Cycles 242–243 closed that 280 cluster
at n=4 forward (2/0 I-only; two forward 4-grams hapax 1/0).
This cycle locks the next tied stem as an exact-K claim on
remaining-after-280.
Do not lock I-only of 090 076 087. Do not lock unique-max
remaining-after-280. Do not lock the other three tied stems
(011/005/000). Do not lock previous 4-grams of
090 076 280. Off-I T sites are not this cycle. I-only of
leftover extra 4-grams is leftover-of-leftover for a later
cycle. 076 071 and 076 070 do not count as this 2-gram.
Inside-family sites do not count as leftover extra.

Leftover extra remaining-after-280 = leftover extra I 090 076
sites with a next token whose next token is none of 070, 071,
013, 001, 700, 530, or 280. Nested-check leftover extra
N_leftover==56, N_with_next==55, N_no_next==1 at Ia4[166],
leftover extra exactly 8 share 070, leftover extra remaining
N_remaining==47 G=071 K=6, leftover extra remaining-after-071
N_remaining2==41 G=013 K=5, leftover extra remaining-after-013
N_remaining3==36 G=001 K=3, leftover extra remaining-after-001
N_remaining4==33 exactly 2 share 700, leftover extra
remaining-after-700 N_remaining5==31 exactly 2 share 530,
leftover extra remaining-after-530 N_remaining6==29 exactly 2
share 280 (do not retune cycles 225–241). Nested-check cycle
242 090 076 280 I-only 2/0 and cycle 243 two forward 4-grams
1/0 each (do not retune). Nested-check N_remaining7==27
(29−2). Ia2[174] has next token 000 and is remaining-after-280;
it is not no-next.

Hypothesis K=2: leftover extra remaining-after-280 includes
exactly 2 sites that share next stem 087 (forward 3-gram
090 076 087). Measured: K=2 at Ia3[87], Ia4[162]; next
4-grams 090 076 087 499 / 090 076 087 078. Cycle 234 listed
087×2 among the 7-way tie; re-measured, not assumed. Claim
that can lose:
i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087.
True iff K==2. The claim is true. Same claim-shape as cycle
226 (leftover extra exactly 8 share forward 070) and cycle
241 (remaining-after-530 exactly 2 share 280). This can lose
if remaining-after-280 does not contain exactly 2 087
next-stem sites, or if N_remaining7 ≠ 27. Nested cycle 243
2/0 hapax, cycle 242 2/0, cycle 241 K=2 / G=280, cycle 240
2/0 hapax, cycle 239 2/0, cycle 238 K=2 / G=530, cycle 237
2/0 hapax, cycle 236 2/0, cycle 234 7-way tie at 2, cycle
233 3/0 hapax, cycle 232 3/0, cycle 223 69/3, cycle 195 6/0,
and cycle 171 43/0 stay. Do not assume the result; measure.
Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""


import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_001_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_001_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE233_CLAIM,
    STANDING_N_I_ONLY as CYCLE233_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE233_N_NOT_I_ONLY,
    TestMamariI090076001Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_013_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE230_CLAIM,
    STANDING_N_I_ONLY as CYCLE230_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE230_N_NOT_I_ONLY,
    TestMamariI090076013Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_530_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_530_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE240_CLAIM,
    STANDING_N_I_ONLY as CYCLE240_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE240_N_NOT_I_ONLY,
    TestMamariI090076530Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_280_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_280_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE243_CLAIM,
    STANDING_N_I_ONLY as CYCLE243_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE243_N_NOT_I_ONLY,
    TestMamariI090076280Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_280_i_only_scoreboard import (
    GRAM3 as CYCLE242_GRAM3,
    STANDING_I_3GRAM_090_076_280_I_ONLY as CYCLE242_CLAIM,
    STANDING_I_SITES as CYCLE242_I_SITES,
    STANDING_N_I as CYCLE242_N_I,
    STANDING_N_OFF_I as CYCLE242_N_OFF_I,
    TestMamariI3gram090076280IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_530_fwd280_scoreboard import (
    GRAM3_FORWARD as CYCLE241_GRAM3,
    STANDING_G as CYCLE241_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_530_EXACTLY_2_SHARE_280 as CYCLE241_CLAIM,
    STANDING_K as CYCLE241_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE241_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE241_MATCHING_SITES,
    STANDING_N_REMAINING6 as CYCLE241_N_REMAINING6,
    STANDING_N_WITHOUT as CYCLE241_N_WITHOUT,
    STANDING_REMAINING6_SITES as CYCLE241_REMAINING6_SITES,
    leftover_extra_remaining_after_530,
    leftover_extra_remaining_after_530_nested_counts_hold,
    leftover_extra_remaining_after_530_next_stems,
    leftover_extra_remaining_after_530_with_280,
    leftover_extra_remaining_after_530_without_280,
    TestMamariILeftoverExtra090076RemainingAfter530Fwd280Scoreboard,
)
from tests.test_mamari_i_090_076_700_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_700_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE237_CLAIM,
    STANDING_N_I_ONLY as CYCLE237_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE237_N_NOT_I_ONLY,
    TestMamariI090076700Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
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
from tests.test_mamari_i_3gram_090_076_001_i_only_scoreboard import (
    GRAM3 as CYCLE232_GRAM3,
    STANDING_I_3GRAM_090_076_001_I_ONLY as CYCLE232_CLAIM,
    STANDING_I_SITES as CYCLE232_I_SITES,
    STANDING_N_I as CYCLE232_N_I,
    STANDING_N_OFF_I as CYCLE232_N_OFF_I,
    TestMamariI3gram090076001IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_013_i_only_scoreboard import (
    GRAM3 as CYCLE229_GRAM3,
    STANDING_I_3GRAM_090_076_013_I_ONLY as CYCLE229_CLAIM,
    STANDING_I_SITES as CYCLE229_I_SITES,
    STANDING_N_I as CYCLE229_N_I,
    STANDING_N_OFF_I as CYCLE229_N_OFF_I,
    TestMamariI3gram090076013IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
    STANDING_I_3GRAM_090_076_071_I_ONLY as CYCLE195_CLAIM,
    STANDING_I_SITES as CYCLE195_I_SITES,
    STANDING_N_I as CYCLE195_N_I,
    STANDING_N_OFF_I as CYCLE195_N_OFF_I,
    TestMamariI3gram090076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_530_i_only_scoreboard import (
    GRAM3 as CYCLE239_GRAM3,
    STANDING_I_3GRAM_090_076_530_I_ONLY as CYCLE239_CLAIM,
    STANDING_I_SITES as CYCLE239_I_SITES,
    STANDING_N_I as CYCLE239_N_I,
    STANDING_N_OFF_I as CYCLE239_N_OFF_I,
    TestMamariI3gram090076530IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_700_i_only_scoreboard import (
    GRAM3 as CYCLE236_GRAM3,
    STANDING_I_3GRAM_090_076_700_I_ONLY as CYCLE236_CLAIM,
    STANDING_I_SITES as CYCLE236_I_SITES,
    STANDING_N_I as CYCLE236_N_I,
    STANDING_N_OFF_I as CYCLE236_N_OFF_I,
    TestMamariI3gram090076700IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_070_scoreboard import (
    STANDING_G as CYCLE226_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070 as CYCLE226_CLAIM,
    STANDING_K as CYCLE226_K,
    STANDING_MATCHING_SITES as CYCLE226_MATCHING_SITES,
    STANDING_N_LEFTOVER as CYCLE226_N_LEFTOVER,
    leftover_extra_with_forward_070,
    TestMamariILeftoverExtra090076Forward070Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_IA2_174,
    STANDING_IA2_174_NEXT_STEM,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE225_N_LEFTOVER,
    STANDING_NO_NEXT_SITES,
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
    leftover_sites_with_next,
    leftover_sites_without_next,
    site_next_stem,
    TestMamariILeftoverExtra090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_fwd700_scoreboard import (
    GRAM3_FORWARD as CYCLE235_GRAM3,
    STANDING_G as CYCLE235_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_2_SHARE_700 as CYCLE235_CLAIM,
    STANDING_K as CYCLE235_K,
    STANDING_MATCHING_SITES as CYCLE235_MATCHING_SITES,
    STANDING_N_REMAINING4 as CYCLE235_N_REMAINING4,
    STANDING_N_WITHOUT as CYCLE235_N_WITHOUT,
    STANDING_OTHER_TIED_STEMS as CYCLE235_OTHER_TIED_STEMS,
    leftover_extra_remaining_after_001_with_700,
    TestMamariILeftoverExtra090076RemainingAfter001Fwd700Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    LOCKED_FORWARD_STEMS,
    STANDING_G as CYCLE234_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G as CYCLE234_CLAIM,
    STANDING_K as CYCLE234_K,
    STANDING_MATCHING_SITES as CYCLE234_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING4 as CYCLE234_N_DISTINCT,
    STANDING_N_REMAINING4 as CYCLE234_N_REMAINING4,
    STANDING_N_SHARE_001 as CYCLE234_N_SHARE_001,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
    STANDING_REMAINING4_FREQUENCY as CYCLE234_FREQUENCY,
    STANDING_REMAINING4_SITES as CYCLE234_REMAINING4_SITES,
    STANDING_TIED_STEMS as CYCLE234_TIED_STEMS,
    leftover_extra_remaining_after_001,
    leftover_extra_remaining_after_001_next_stems,
    leftover_extra_remaining_after_001_with_g,
    remaining_after_001_next_stem_frequency_table,
    select_remaining_after_001_g,
    TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_013_next_stem_scoreboard import (
    STANDING_G as CYCLE231_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_013_EXACTLY_K_SHARE_G as CYCLE231_CLAIM,
    STANDING_K as CYCLE231_K,
    STANDING_MATCHING_SITES as CYCLE231_MATCHING_SITES,
    STANDING_N_REMAINING3 as CYCLE231_N_REMAINING3,
    STANDING_N_WITHOUT_G as CYCLE231_N_WITHOUT_G,
    STANDING_REMAINING3_SITES as CYCLE231_REMAINING3_SITES,
    leftover_extra_remaining_after_013,
    leftover_extra_remaining_after_013_with_g,
    TestMamariILeftoverExtra090076RemainingAfter013NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_071_next_stem_scoreboard import (
    STANDING_G as CYCLE228_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G as CYCLE228_CLAIM,
    STANDING_K as CYCLE228_K,
    STANDING_MATCHING_SITES as CYCLE228_MATCHING_SITES,
    STANDING_REMAINING2_SITES as CYCLE228_REMAINING2_SITES,
    leftover_extra_remaining_after_071,
    leftover_extra_remaining_after_071_with_g,
    TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_700_fwd530_scoreboard import (
    GRAM3_FORWARD as CYCLE238_GRAM3,
    STANDING_G as CYCLE238_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_700_EXACTLY_2_SHARE_530 as CYCLE238_CLAIM,
    STANDING_K as CYCLE238_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE238_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE238_MATCHING_SITES,
    STANDING_N_REMAINING5 as CYCLE238_N_REMAINING5,
    STANDING_N_WITHOUT as CYCLE238_N_WITHOUT,
    STANDING_REMAINING5_SITES as CYCLE238_REMAINING5_SITES,
    leftover_extra_remaining_after_700,
    leftover_extra_remaining_after_700_nested_counts_hold,
    leftover_extra_remaining_after_700_with_530,
    leftover_extra_remaining_after_700_without_530,
    TestMamariILeftoverExtra090076RemainingAfter700Fwd530Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    STANDING_G as CYCLE227_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 as CYCLE227_CLAIM,
    STANDING_K as CYCLE227_K,
    STANDING_MATCHING_SITES as CYCLE227_MATCHING_SITES,
    STANDING_REMAINING_SITES as CYCLE227_REMAINING_SITES,
    leftover_extra_remaining,
    leftover_extra_remaining_with_g,
    TestMamariILeftoverExtra090076RemainingNextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
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
LOCKED_FORWARD_STEM_070 = "070"
LOCKED_FORWARD_STEM_071 = "071"
LOCKED_FORWARD_STEM_013 = "013"
LOCKED_FORWARD_STEM_001 = "001"
LOCKED_FORWARD_STEM_700 = "700"
LOCKED_FORWARD_STEM_530 = "530"
LOCKED_FORWARD_STEM_280 = "280"
LOCKED_FORWARD_STEMS_AFTER_700 = ("070", "071", "013", "001", "700")
LOCKED_FORWARD_STEMS_AFTER_530 = ("070", "071", "013", "001", "700", "530")
LOCKED_FORWARD_STEMS_AFTER_280 = ("070", "071", "013", "001", "700", "530", "280")
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "087")
GRAM3_NESTED_280 = ("090", "076", "280")
GRAM3_NESTED_530 = ("090", "076", "530")
GRAM3_NESTED_700 = ("090", "076", "700")
GRAM3_NESTED_001 = ("090", "076", "001")
GRAM3_NESTED_013 = ("090", "076", "013")
GRAM3_NESTED_071 = ("090", "076", "071")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_WITH_NEXT = 55
STANDING_N_NO_NEXT = 1
STANDING_N_SHARE_070 = 8
STANDING_N_REMAINING = 47
STANDING_N_SHARE_071 = 6
STANDING_N_REMAINING2 = 41
STANDING_N_SHARE_013 = 5
STANDING_N_REMAINING3 = 36
STANDING_N_SHARE_001 = 3
STANDING_N_REMAINING4 = 33
STANDING_N_DISTINCT_REMAINING4 = 26
STANDING_N_TIED_AT_K = 7
STANDING_TIED_STEMS = ("700", "530", "280", "087", "011", "005", "000")
STANDING_TIED_STEMS_MINUS_700 = ("530", "280", "087", "011", "005", "000")
STANDING_N_TIED_MINUS_700 = 6
STANDING_TIED_STEMS_MINUS_700_530 = ("280", "087", "011", "005", "000")
STANDING_N_TIED_MINUS_700_530 = 5
STANDING_TIED_STEMS_MINUS_700_530_280 = ("087", "011", "005", "000")
STANDING_N_TIED_MINUS_700_530_280 = 4
STANDING_OTHER_TIED_STEMS = ("011", "005", "000")
STANDING_N_SHARE_700 = 2
STANDING_N_REMAINING5 = 31
STANDING_N_SHARE_530 = 2
STANDING_N_REMAINING6 = 29
STANDING_N_SHARE_280 = 2
STANDING_N_REMAINING7 = 27
STANDING_G = "087"
STANDING_K = 2
STANDING_N_WITHOUT = 25
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_UNIQUE_MAX_REMAINING_AFTER_280_IS_NOT_THIS_CYCLE = True
STANDING_REMAINING7_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
    (SIDE_IA, "Ia2", 165),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia3", 71),
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 47),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 109),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia14", 177),
)
STANDING_REMAINING6_SITES = CYCLE241_REMAINING6_SITES
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia4", 162),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "087", "499"),
    ("090", "076", "087", "078"),
)
STANDING_CYCLE234_087_SITES = CYCLE234_FREQUENCY[3][2]
STANDING_CYCLE234_280_SITES = CYCLE234_FREQUENCY[2][2]
STANDING_MATCHING_EQUALS_CYCLE234_087_SITES = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087"
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_280_EXACTLY_2_SHARE_087 = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_280_fwd087"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE226 = False
STANDING_SAME_AS_CYCLE234 = False
STANDING_SAME_AS_CYCLE235 = False
STANDING_SAME_AS_CYCLE236 = False
STANDING_SAME_AS_CYCLE237 = False
STANDING_SAME_AS_CYCLE238 = False
STANDING_SAME_AS_CYCLE239 = False
STANDING_SAME_AS_CYCLE240 = False
STANDING_SAME_AS_CYCLE241 = False
STANDING_SAME_AS_CYCLE242 = False
STANDING_SAME_AS_CYCLE243 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE238 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE241 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_090_076_087_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_4GRAMS_OF_090_076_280_ARE_NOT_THIS_CYCLE = True
STANDING_OTHER_TIED_STEMS_NOT_LOCKED = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN = True


def leftover_extra_remaining_after_280(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_280,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra with-next sites whose next token is none of 070/071/013/001/700/530/280."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_280_next_stems(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_280,
) -> tuple[str, ...]:
    """Next stems of leftover extra remaining-after-280 sites."""
    locked_set = set(locked)
    return tuple(
        nxt
        for nxt in next_stems
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_280_with_087(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-280 sites whose next token is 087."""
    remaining7 = set(leftover_extra_remaining_after_280(sites, next_stems))
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem and site in remaining7
    )


def leftover_extra_remaining_after_280_without_087(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_280,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-280 sites whose next token is not 087."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set and nxt != stem
    )


def leftover_extra_remaining_after_280_nested_counts_hold(
    n_leftover: int,
    n_with_next: int,
    n_no_next: int,
    n_share_070: int,
    n_remaining: int,
    n_share_071: int,
    n_remaining2: int,
    n_share_013: int,
    n_remaining3: int,
    n_share_001: int,
    n_remaining4: int,
    n_share_700: int,
    n_remaining5: int,
    n_share_530: int,
    n_remaining6: int,
    n_share_280: int,
    n_remaining7: int,
    expected_share_280: int = STANDING_N_SHARE_280,
    expected_remaining7: int = STANDING_N_REMAINING7,
) -> bool:
    """Nested leftover extra chain through remaining-after-280 N_remaining7==27."""
    return leftover_extra_remaining_after_530_nested_counts_hold(
        n_leftover,
        n_with_next,
        n_no_next,
        n_share_070,
        n_remaining,
        n_share_071,
        n_remaining2,
        n_share_013,
        n_remaining3,
        n_share_001,
        n_remaining4,
        n_share_700,
        n_remaining5,
        n_share_530,
        n_remaining6,
    ) and n_share_280 == expected_share_280 and n_remaining7 == expected_remaining7 and (
        n_remaining7 == n_remaining6 - n_share_280
    )


def matching_equals_cycle234_087_sites(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle234_sites: tuple[tuple[str, str, int], ...] = STANDING_CYCLE234_087_SITES,
) -> bool:
    """True iff remaining-after-280 090 076 087 sites equal cycle 234's 087 pair."""
    return matching_sites == cycle234_sites


def matching_leftover_extra_remaining_after_280_fwd087_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-280 087 next-4-gram rows."""
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


def i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(
    k: int,
    expected: int = HYPOTHESIS_K,
) -> bool:
    """True iff K equals the hypothesized 2."""
    return k == expected


class TestILeftoverExtra090076RemainingAfter280Fwd087Helpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-280 forward 087. No CV, no LLM."""

    def test_forward_087_requires_remaining_after_280_next_stem(self):
        """Next stem 087 is remaining-after-280; locked 070/071/013/001/700/530/280 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "087"))
        self.assertEqual(GRAM3_NESTED_280, ("090", "076", "280"))
        self.assertEqual(GRAM3_NESTED_530, ("090", "076", "530"))
        self.assertEqual(GRAM3_NESTED_700, ("090", "076", "700"))
        self.assertEqual(GRAM3_NESTED_001, ("090", "076", "001"))
        self.assertEqual(GRAM3_NESTED_013, ("090", "076", "013"))
        self.assertEqual(GRAM3_NESTED_071, ("090", "076", "071"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("070", "071", "013", "001"))
        self.assertEqual(LOCKED_FORWARD_STEMS_AFTER_700, ("070", "071", "013", "001", "700"))
        self.assertEqual(
            LOCKED_FORWARD_STEMS_AFTER_530,
            ("070", "071", "013", "001", "700", "530"),
        )
        self.assertEqual(
            LOCKED_FORWARD_STEMS_AFTER_280,
            ("070", "071", "013", "001", "700", "530", "280"),
        )
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_087 = ["999", "090", "076", "087", "499"]
        self.assertEqual(site_next_stem(has_087, 1, GRAM2), "087")
        self.assertEqual(site_forward_3gram(has_087, 1, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_087, 1, GRAM2),
            ("090", "076", "087", "499"),
        )
        has_280 = ["999", "090", "076", "280", "139"]
        self.assertEqual(site_next_stem(has_280, 1, GRAM2), "280")
        self.assertNotEqual(site_next_stem(has_280, 1, GRAM2), "087")
        has_530 = ["999", "090", "076", "530", "090"]
        self.assertEqual(site_next_stem(has_530, 1, GRAM2), "530")
        self.assertNotEqual(site_next_stem(has_530, 1, GRAM2), "087")
        has_700 = ["999", "090", "076", "700", "011"]
        self.assertEqual(site_next_stem(has_700, 1, GRAM2), "700")
        self.assertNotEqual(site_next_stem(has_700, 1, GRAM2), "087")
        has_001 = ["999", "090", "076", "001", "048"]
        self.assertEqual(site_next_stem(has_001, 1, GRAM2), "001")
        self.assertNotEqual(site_next_stem(has_001, 1, GRAM2), "087")
        has_013 = ["999", "090", "076", "013", "073"]
        self.assertEqual(site_next_stem(has_013, 1, GRAM2), "013")
        self.assertNotEqual(site_next_stem(has_013, 1, GRAM2), "087")
        has_071 = ["999", "090", "076", "071", "633"]
        self.assertEqual(site_next_stem(has_071, 1, GRAM2), "071")
        self.assertNotEqual(site_next_stem(has_071, 1, GRAM2), "087")
        has_070 = ["999", "090", "076", "070", "499"]
        self.assertEqual(site_next_stem(has_070, 1, GRAM2), "070")
        self.assertNotEqual(site_next_stem(has_070, 1, GRAM2), "087")
        end_of_line = ["087", "078", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        one_token_then_eol = ["009", "009", "090", "076", "000"]
        self.assertEqual(site_next_stem(one_token_then_eol, 2, GRAM2), "000")
        self.assertIsNone(site_next_4gram(one_token_then_eol, 2, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
            (SIDE_IA, "Ia1", 5),
            (SIDE_IA, "Ia1", 6),
            (SIDE_IA, "Ia1", 7),
            (SIDE_IA, "Ia1", 8),
            (SIDE_IA, "Ia1", 9),
        )
        planted_stems = ("087", "280", "530", "700", "070", "071", "013", "001", None, "011")
        rem7 = leftover_extra_remaining_after_280(planted_sites, planted_stems)
        self.assertEqual(rem7, (planted_sites[0], planted_sites[9]))
        self.assertEqual(
            leftover_extra_remaining_after_280_with_087(planted_sites, planted_stems),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_extra_remaining_after_280_without_087(planted_sites, planted_stems),
            (planted_sites[9],),
        )
        self.assertNotIn(planted_sites[1], rem7)
        self.assertNotIn(planted_sites[2], rem7)
        self.assertNotIn(planted_sites[3], rem7)
        self.assertNotIn(planted_sites[4], rem7)
        self.assertNotIn(planted_sites[5], rem7)
        self.assertNotIn(planted_sites[6], rem7)
        self.assertNotIn(planted_sites[7], rem7)
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when K=2."""
        provider = MockProvider()
        self.assertTrue(i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(2))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(0))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(1))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(3))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(6))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(29))
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 2),)
        planted_stems = ("087",) * 3
        self.assertEqual(
            leftover_extra_remaining_after_280_with_087(planted, planted_stems),
            planted,
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(len(planted))
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_280_EXACTLY_2_SHARE_087
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_280_EXACTLY_2_SHARE_087,
            HYPOTHESIS_K == STANDING_K,
        )
        self.assertEqual(STANDING_N_SHARE_280 + STANDING_N_REMAINING7, STANDING_N_REMAINING6)
        self.assertEqual(2 + 27, 29)
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT, STANDING_N_REMAINING7)
        self.assertEqual(2 + 25, 27)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle234_280_site_agreement_and_tie_minus_700_530_can_fail(self):
        """Matching sites must equal cycle 234's Ia3[87]/Ia4[162]; unique-max stays unlocked."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle234_087_sites(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE234_087_SITES)
        self.assertEqual(STANDING_MATCHING_SITES, STANDING_CYCLE234_087_SITES)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle234_087_sites(planted))
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(len(planted))
        )
        swapped = ((SIDE_IA, "Ia7", 2), (SIDE_IA, "Ia7", 113))
        self.assertFalse(matching_equals_cycle234_087_sites(swapped))
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(len(swapped))
        )
        self.assertEqual(swapped, CYCLE241_MATCHING_SITES)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE241_MATCHING_SITES)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE238_MATCHING_SITES)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE235_MATCHING_SITES)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(STANDING_UNIQUE_MAX_REMAINING_AFTER_280_IS_NOT_THIS_CYCLE)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_TIED_STEMS, STANDING_TIED_STEMS)
        self.assertEqual(
            tuple(stem for stem in CYCLE234_TIED_STEMS if stem not in ("700", "530", "280")),
            STANDING_TIED_STEMS_MINUS_700_530_280,
        )
        self.assertEqual(len(STANDING_TIED_STEMS_MINUS_700_530_280), STANDING_N_TIED_MINUS_700_530_280)
        self.assertEqual(STANDING_N_TIED_MINUS_700_530_280, 4)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_087_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_280_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE238)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE241)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE238)
        self.assertFalse(STANDING_SAME_AS_CYCLE241)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter280Fwd087Scoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-280 forward-087 lock. Mock only."""

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
        self.share_070 = leftover_extra_with_forward_070(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining = leftover_extra_remaining(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_071 = leftover_extra_remaining_with_g(
            self.leftover_sites,
            self.next_stems,
            LOCKED_FORWARD_STEM_071,
        )
        self.remaining2 = leftover_extra_remaining_after_071(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_013 = leftover_extra_remaining_after_071_with_g(
            self.leftover_sites,
            self.next_stems,
            LOCKED_FORWARD_STEM_013,
        )
        self.remaining3 = leftover_extra_remaining_after_013(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_001 = leftover_extra_remaining_after_013_with_g(
            self.leftover_sites,
            self.next_stems,
            LOCKED_FORWARD_STEM_001,
        )
        self.remaining4 = leftover_extra_remaining_after_001(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining4_stems = leftover_extra_remaining_after_001_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_700 = leftover_extra_remaining_after_001_with_700(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining5 = leftover_extra_remaining_after_700(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_530 = leftover_extra_remaining_after_700_with_530(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining6 = leftover_extra_remaining_after_530(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining6_stems = leftover_extra_remaining_after_530_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_280 = leftover_extra_remaining_after_530_with_280(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining7 = leftover_extra_remaining_after_280(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining7_stems = leftover_extra_remaining_after_280_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.matching = leftover_extra_remaining_after_280_with_087(
            self.leftover_sites,
            self.next_stems,
        )
        self.without = leftover_extra_remaining_after_280_without_087(
            self.leftover_sites,
            self.next_stems,
        )
        self.frequency = remaining_after_001_next_stem_frequency_table(
            self.leftover_sites,
            self.next_stems,
            self.forwards,
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
        self.n_share_070 = len(self.share_070)
        self.n_remaining = len(self.remaining)
        self.n_share_071 = len(self.share_071)
        self.n_remaining2 = len(self.remaining2)
        self.n_share_013 = len(self.share_013)
        self.n_remaining3 = len(self.remaining3)
        self.n_share_001 = len(self.share_001)
        self.n_remaining4 = len(self.remaining4)
        self.n_distinct_remaining4 = len(self.frequency)
        self.n_share_700 = len(self.share_700)
        self.n_remaining5 = len(self.remaining5)
        self.n_share_530 = len(self.share_530)
        self.n_remaining6 = len(self.remaining6)
        self.n_share_280 = len(self.share_280)
        self.n_remaining7 = len(self.remaining7)
        self.g, self.tiebreak_k, self.unique = select_remaining_after_001_g(
            self.remaining4_stems
        )
        self.k = len(self.matching)
        self.n_without = len(self.without)
        self.tied = tuple(
            stem for stem, count, _sites, _grams in self.frequency if count == 2
        )
        self.tied_minus_700 = tuple(stem for stem in self.tied if stem != "700")
        self.tied_minus_700_530 = tuple(
            stem for stem in self.tied if stem not in ("700", "530")
        )
        self.tied_minus_700_530_280 = tuple(
            stem for stem in self.tied if stem not in ("700", "530", "280")
        )
        self.equals_cycle234_087 = matching_equals_cycle234_087_sites(self.matching)
        self.claim_holds = i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(
            self.k,
        )

    def test_tokens_and_nested_leftover_extra_through_530_not_retuned(self):
        """2-gram and leftover extra 56/55/1 through remaining-after-530 29/2/280 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "087"))
        self.assertEqual(GRAM3_NESTED_280, ("090", "076", "280"))
        self.assertEqual(GRAM3_NESTED_530, ("090", "076", "530"))
        self.assertEqual(GRAM3_NESTED_530, CYCLE239_GRAM3)
        self.assertEqual(GRAM3_NESTED_530, CYCLE238_GRAM3)
        self.assertEqual(GRAM3_NESTED_700, ("090", "076", "700"))
        self.assertEqual(GRAM3_NESTED_700, CYCLE236_GRAM3)
        self.assertEqual(GRAM3_NESTED_700, CYCLE235_GRAM3)
        self.assertEqual(GRAM3_NESTED_001, ("090", "076", "001"))
        self.assertEqual(GRAM3_NESTED_001, CYCLE232_GRAM3)
        self.assertEqual(GRAM3_NESTED_013, ("090", "076", "013"))
        self.assertEqual(GRAM3_NESTED_013, CYCLE229_GRAM3)
        self.assertEqual(GRAM3_NESTED_071, ("090", "076", "071"))
        self.assertEqual(GRAM3_NESTED_071, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM3_FORWARD, CYCLE207_GRAM3)
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
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
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE226_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_243 = self.survey["i_090_076_280_forward_4grams_i_only"]
        self.assertEqual(prior_243["cycle"], 243)
        self.assertEqual(prior_243["N_i_only"], 2)
        self.assertEqual(prior_243["N_not_i_only"], 0)
        self.assertTrue(prior_243["i_090_076_280_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE243_CLAIM)
        self.assertEqual(CYCLE243_N_I_ONLY, 2)
        self.assertEqual(CYCLE243_N_NOT_I_ONLY, 0)
        prior_242 = self.survey["i_3gram_090_076_280_i_only"]
        self.assertEqual(prior_242["cycle"], 242)
        self.assertEqual(prior_242["N_I"], 2)
        self.assertEqual(prior_242["N_off_I"], 0)
        self.assertTrue(prior_242["i_3gram_090_076_280_i_only"])
        self.assertTrue(CYCLE242_CLAIM)
        self.assertEqual(CYCLE242_N_I, 2)
        self.assertEqual(CYCLE242_N_OFF_I, 0)
        prior_241 = self.survey["i_leftover_extra_090_076_remaining_after_530_fwd280"]
        self.assertEqual(prior_241["cycle"], 241)
        self.assertEqual(prior_241["G"], "280")
        self.assertEqual(prior_241["K"], 2)
        self.assertEqual(prior_241["N_remaining6"], 29)
        self.assertEqual(prior_241["N_without"], 27)
        self.assertTrue(prior_241["i_leftover_extra_090_076_remaining_after_530_exactly_2_share_280"])
        self.assertTrue(CYCLE241_CLAIM)
        self.assertEqual(CYCLE241_G, "280")
        self.assertEqual(CYCLE241_K, 2)
        self.assertEqual(CYCLE241_N_REMAINING6, 29)
        self.assertEqual(CYCLE241_N_WITHOUT, 27)
        prior_240 = self.survey["i_090_076_530_forward_4grams_i_only"]
        self.assertEqual(prior_240["cycle"], 240)
        self.assertEqual(prior_240["N_i_only"], 2)
        self.assertEqual(prior_240["N_not_i_only"], 0)
        self.assertTrue(prior_240["i_090_076_530_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE240_CLAIM)
        self.assertEqual(CYCLE240_N_I_ONLY, 2)
        self.assertEqual(CYCLE240_N_NOT_I_ONLY, 0)
        prior_239 = self.survey["i_3gram_090_076_530_i_only"]
        self.assertEqual(prior_239["cycle"], 239)
        self.assertEqual(prior_239["N_I"], 2)
        self.assertEqual(prior_239["N_off_I"], 0)
        self.assertTrue(prior_239["i_3gram_090_076_530_i_only"])
        self.assertTrue(CYCLE239_CLAIM)
        self.assertEqual(CYCLE239_N_I, 2)
        self.assertEqual(CYCLE239_N_OFF_I, 0)
        prior_238 = self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]
        self.assertEqual(prior_238["cycle"], 238)
        self.assertEqual(prior_238["G"], "530")
        self.assertEqual(prior_238["K"], 2)
        self.assertEqual(prior_238["N_remaining5"], 31)
        self.assertEqual(prior_238["N_without"], 29)
        self.assertTrue(prior_238["i_leftover_extra_090_076_remaining_after_700_exactly_2_share_530"])
        self.assertTrue(CYCLE238_CLAIM)
        self.assertEqual(CYCLE238_G, "530")
        self.assertEqual(CYCLE238_K, 2)
        self.assertEqual(CYCLE238_N_REMAINING5, 31)
        self.assertEqual(CYCLE238_N_WITHOUT, 29)
        prior_237 = self.survey["i_090_076_700_forward_4grams_i_only"]
        self.assertEqual(prior_237["cycle"], 237)
        self.assertEqual(prior_237["N_i_only"], 2)
        self.assertEqual(prior_237["N_not_i_only"], 0)
        self.assertTrue(prior_237["i_090_076_700_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE237_CLAIM)
        self.assertEqual(CYCLE237_N_I_ONLY, 2)
        self.assertEqual(CYCLE237_N_NOT_I_ONLY, 0)
        prior_236 = self.survey["i_3gram_090_076_700_i_only"]
        self.assertEqual(prior_236["cycle"], 236)
        self.assertEqual(prior_236["N_I"], 2)
        self.assertEqual(prior_236["N_off_I"], 0)
        self.assertTrue(prior_236["i_3gram_090_076_700_i_only"])
        self.assertTrue(CYCLE236_CLAIM)
        self.assertEqual(CYCLE236_N_I, 2)
        self.assertEqual(CYCLE236_N_OFF_I, 0)
        prior_235 = self.survey["i_leftover_extra_090_076_remaining_after_001_fwd700"]
        self.assertEqual(prior_235["cycle"], 235)
        self.assertEqual(prior_235["G"], "700")
        self.assertEqual(prior_235["K"], 2)
        self.assertEqual(prior_235["N_remaining4"], 33)
        self.assertEqual(prior_235["N_without"], 31)
        self.assertTrue(prior_235["i_leftover_extra_090_076_remaining_after_001_exactly_2_share_700"])
        self.assertTrue(CYCLE235_CLAIM)
        self.assertEqual(CYCLE235_G, "700")
        self.assertEqual(CYCLE235_K, 2)
        self.assertEqual(CYCLE235_N_REMAINING4, 33)
        self.assertEqual(CYCLE235_N_WITHOUT, 31)
        prior_234 = self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]
        self.assertEqual(prior_234["cycle"], 234)
        self.assertEqual(prior_234["N_leftover"], 56)
        self.assertEqual(prior_234["N_with_next"], 55)
        self.assertEqual(prior_234["N_no_next"], 1)
        self.assertEqual(prior_234["N_share_070"], 8)
        self.assertEqual(prior_234["N_remaining"], 47)
        self.assertEqual(prior_234["N_share_071"], 6)
        self.assertEqual(prior_234["N_remaining2"], 41)
        self.assertEqual(prior_234["N_share_013"], 5)
        self.assertEqual(prior_234["N_remaining3"], 36)
        self.assertEqual(prior_234["N_share_001"], 3)
        self.assertEqual(prior_234["N_remaining4"], 33)
        self.assertEqual(prior_234["N_distinct_remaining4"], 26)
        self.assertEqual(prior_234["G"], "700")
        self.assertEqual(prior_234["K"], 2)
        self.assertFalse(prior_234["G_uniquely_most_frequent"])
        self.assertEqual(prior_234["N_tied_at_K"], 7)
        self.assertEqual(tuple(prior_234["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertFalse(prior_234["i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G"])
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE234_G, "700")
        self.assertEqual(CYCLE234_K, 2)
        self.assertEqual(CYCLE234_N_REMAINING4, 33)
        self.assertEqual(CYCLE234_N_DISTINCT, 26)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertFalse(CYCLE234_UNIQUE)
        prior_233 = self.survey["i_090_076_001_forward_4grams_i_only"]
        self.assertEqual(prior_233["cycle"], 233)
        self.assertEqual(prior_233["N_I"], 3)
        self.assertEqual(prior_233["N_i_only"], 3)
        self.assertEqual(prior_233["N_not_i_only"], 0)
        self.assertTrue(prior_233["i_090_076_001_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE233_CLAIM)
        self.assertEqual(CYCLE233_N_I_ONLY, 3)
        self.assertEqual(CYCLE233_N_NOT_I_ONLY, 0)
        prior_232 = self.survey["i_3gram_090_076_001_i_only"]
        self.assertEqual(prior_232["cycle"], 232)
        self.assertEqual(prior_232["N_I"], 3)
        self.assertEqual(prior_232["N_off_I"], 0)
        self.assertTrue(prior_232["i_3gram_090_076_001_i_only"])
        self.assertTrue(CYCLE232_CLAIM)
        self.assertEqual(CYCLE232_N_I, 3)
        self.assertEqual(CYCLE232_N_OFF_I, 0)
        prior_231 = self.survey["i_leftover_extra_090_076_remaining_after_013_next_stem"]
        self.assertEqual(prior_231["cycle"], 231)
        self.assertEqual(prior_231["N_remaining3"], 36)
        self.assertEqual(prior_231["G"], "001")
        self.assertEqual(prior_231["K"], 3)
        self.assertEqual(prior_231["N_without_G"], 33)
        self.assertTrue(CYCLE231_CLAIM)
        self.assertEqual(CYCLE231_G, "001")
        self.assertEqual(CYCLE231_K, 3)
        self.assertEqual(CYCLE231_N_REMAINING3, 36)
        self.assertEqual(CYCLE231_N_WITHOUT_G, 33)
        prior_230 = self.survey["i_090_076_013_forward_4grams_i_only"]
        self.assertEqual(prior_230["cycle"], 230)
        self.assertEqual(prior_230["N_i_only"], 5)
        self.assertEqual(prior_230["N_not_i_only"], 0)
        self.assertTrue(CYCLE230_CLAIM)
        self.assertEqual(CYCLE230_N_I_ONLY, 5)
        self.assertEqual(CYCLE230_N_NOT_I_ONLY, 0)
        prior_229 = self.survey["i_3gram_090_076_013_i_only"]
        self.assertEqual(prior_229["cycle"], 229)
        self.assertEqual(prior_229["N_I"], 5)
        self.assertEqual(prior_229["N_off_I"], 0)
        self.assertTrue(CYCLE229_CLAIM)
        self.assertEqual(CYCLE229_N_I, 5)
        self.assertEqual(CYCLE229_N_OFF_I, 0)
        prior_228 = self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]
        self.assertEqual(prior_228["cycle"], 228)
        self.assertEqual(prior_228["N_remaining2"], 41)
        self.assertEqual(prior_228["G"], "013")
        self.assertEqual(prior_228["K"], 5)
        self.assertTrue(CYCLE228_CLAIM)
        self.assertEqual(CYCLE228_G, "013")
        self.assertEqual(CYCLE228_K, 5)
        prior_227 = self.survey["i_leftover_extra_090_076_remaining_next_stem"]
        self.assertEqual(prior_227["cycle"], 227)
        self.assertEqual(prior_227["N_remaining"], 47)
        self.assertEqual(prior_227["G"], "071")
        self.assertEqual(prior_227["K"], 6)
        self.assertTrue(CYCLE227_CLAIM)
        self.assertEqual(CYCLE227_G, "071")
        self.assertEqual(CYCLE227_K, 6)
        prior_226 = self.survey["i_leftover_extra_090_076_forward_070"]
        self.assertEqual(prior_226["cycle"], 226)
        self.assertEqual(prior_226["G"], "070")
        self.assertEqual(prior_226["K"], 8)
        self.assertTrue(CYCLE226_CLAIM)
        self.assertEqual(CYCLE226_G, "070")
        self.assertEqual(CYCLE226_K, 8)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_195 = self.survey["i_3gram_090_076_071_i_only"]
        self.assertEqual(prior_195["cycle"], 195)
        self.assertEqual(prior_195["N_I"], 6)
        self.assertEqual(prior_195["N_off_I"], 0)
        self.assertTrue(CYCLE195_CLAIM)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_087_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_280_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_UNIQUE_MAX_REMAINING_AFTER_280_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_of_29_and_hypothesis_k_2_holds(self):
        """N_remaining7=27, 7-way-tie-minus-700-530-280 stays, K=2 share 087. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 55)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 1)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ((SIDE_IA, "Ia4", 166),))
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_leftover)
        self.assertEqual(55 + 1, 56)
        self.assertEqual(self.n_share_070, STANDING_N_SHARE_070)
        self.assertEqual(STANDING_N_SHARE_070, 8)
        self.assertEqual(self.share_070, CYCLE226_MATCHING_SITES)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING, 47)
        self.assertEqual(self.n_remaining, self.n_with_next - self.n_share_070)
        self.assertEqual(55 - 8, 47)
        self.assertEqual(self.remaining, CYCLE227_REMAINING_SITES)
        self.assertEqual(self.n_share_071, STANDING_N_SHARE_071)
        self.assertEqual(STANDING_N_SHARE_071, 6)
        self.assertEqual(self.share_071, CYCLE227_MATCHING_SITES)
        self.assertEqual(self.share_071, CYCLE195_I_SITES)
        if self.share_071 != CYCLE195_I_SITES:
            self.fail("leftover extra remaining 6 share 071 drifted from cycle-195 I set")
        self.assertEqual(self.n_remaining2, STANDING_N_REMAINING2)
        self.assertEqual(STANDING_N_REMAINING2, 41)
        self.assertEqual(self.n_remaining2, self.n_remaining - self.n_share_071)
        self.assertEqual(47 - 6, 41)
        self.assertEqual(self.remaining2, CYCLE228_REMAINING2_SITES)
        self.assertEqual(self.n_share_013, STANDING_N_SHARE_013)
        self.assertEqual(STANDING_N_SHARE_013, 5)
        self.assertEqual(self.share_013, CYCLE228_MATCHING_SITES)
        self.assertEqual(self.share_013, CYCLE229_I_SITES)
        if self.share_013 != CYCLE229_I_SITES:
            self.fail("leftover extra remaining-after-071 5 share 013 drifted from cycle-229 I set")
        self.assertEqual(self.n_remaining3, STANDING_N_REMAINING3)
        self.assertEqual(STANDING_N_REMAINING3, 36)
        self.assertEqual(self.n_remaining3, self.n_remaining2 - self.n_share_013)
        self.assertEqual(41 - 5, 36)
        self.assertEqual(self.remaining3, CYCLE231_REMAINING3_SITES)
        self.assertEqual(self.n_share_001, STANDING_N_SHARE_001)
        self.assertEqual(STANDING_N_SHARE_001, CYCLE234_N_SHARE_001)
        self.assertEqual(self.share_001, CYCLE231_MATCHING_SITES)
        self.assertEqual(self.share_001, CYCLE232_I_SITES)
        if self.share_001 != CYCLE232_I_SITES:
            self.fail("leftover extra remaining-after-013 3 share 001 drifted from cycle-232 I set")
        self.assertEqual(self.n_remaining4, STANDING_N_REMAINING4)
        self.assertEqual(STANDING_N_REMAINING4, 33)
        self.assertEqual(self.n_remaining4, CYCLE234_N_REMAINING4)
        self.assertEqual(self.n_remaining4, self.n_remaining3 - self.n_share_001)
        self.assertEqual(36 - 3, 33)
        self.assertEqual(self.remaining4, CYCLE234_REMAINING4_SITES)
        self.assertEqual(self.n_share_700, STANDING_N_SHARE_700)
        self.assertEqual(STANDING_N_SHARE_700, 2)
        self.assertEqual(self.share_700, CYCLE235_MATCHING_SITES)
        self.assertEqual(self.share_700, CYCLE236_I_SITES)
        if self.share_700 != CYCLE235_MATCHING_SITES:
            self.fail("leftover extra remaining-after-001 2 share 700 drifted from cycle-235 pair")
        self.assertEqual(self.n_remaining5, STANDING_N_REMAINING5)
        self.assertEqual(STANDING_N_REMAINING5, 31)
        self.assertEqual(self.n_remaining5, CYCLE238_N_REMAINING5)
        self.assertEqual(self.n_remaining5, self.n_remaining4 - self.n_share_700)
        self.assertEqual(33 - 2, 31)
        self.assertEqual(self.remaining5, CYCLE238_REMAINING5_SITES)
        self.assertEqual(self.n_share_530, STANDING_N_SHARE_530)
        self.assertEqual(STANDING_N_SHARE_530, 2)
        self.assertEqual(self.share_530, CYCLE238_MATCHING_SITES)
        self.assertEqual(self.share_530, CYCLE239_I_SITES)
        if self.share_530 != CYCLE238_MATCHING_SITES:
            self.fail("leftover extra remaining-after-700 2 share 530 drifted from cycle-238 pair")
        if (
            self.n_leftover != 56
            or self.n_with_next != 55
            or self.n_no_next != 1
            or self.n_share_070 != 8
            or self.n_remaining != 47
            or self.n_share_071 != 6
            or self.n_remaining2 != 41
            or self.n_share_013 != 5
            or self.n_remaining3 != 36
            or self.n_share_001 != 3
            or self.n_remaining4 != 33
            or self.n_share_700 != 2
            or self.n_remaining5 != 31
            or self.n_share_530 != 2
            or self.n_share_280 != 2
        ):
            self.fail(
                "nested leftover extra 56/55/1 / 8 share 070 / remaining 47/6/071 / "
                "remaining-after-071 41/5/013 / remaining-after-013 36/3/001 / "
                "remaining-after-001 33/2/700 / remaining-after-700 31/2/530 / "
                "remaining-after-530 29/2/280 drifted"
            )
        self.assertTrue(
            leftover_extra_remaining_after_280_nested_counts_hold(
                self.n_leftover,
                self.n_with_next,
                self.n_no_next,
                self.n_share_070,
                self.n_remaining,
                self.n_share_071,
                self.n_remaining2,
                self.n_share_013,
                self.n_remaining3,
                self.n_share_001,
                self.n_remaining4,
                self.n_share_700,
                self.n_remaining5,
                self.n_share_530,
                self.n_remaining6,
                self.n_share_280,
                self.n_remaining7,
            )
        )
        self.assertEqual(self.n_remaining6, STANDING_N_REMAINING6)
        self.assertEqual(STANDING_N_REMAINING6, 29)
        self.assertEqual(self.n_remaining6, CYCLE241_N_REMAINING6)
        self.assertEqual(self.n_remaining6, CYCLE238_N_WITHOUT)
        self.assertEqual(self.n_remaining6, self.n_remaining5 - self.n_share_530)
        self.assertEqual(31 - 2, 29)
        self.assertEqual(self.n_share_280, STANDING_N_SHARE_280)
        self.assertEqual(STANDING_N_SHARE_280, 2)
        self.assertEqual(self.share_280, CYCLE241_MATCHING_SITES)
        self.assertEqual(self.share_280, CYCLE242_I_SITES)
        if self.share_280 != CYCLE241_MATCHING_SITES:
            self.fail("leftover extra remaining-after-530 2 share 280 drifted from cycle-241 pair")
        self.assertEqual(self.n_remaining7, STANDING_N_REMAINING7)
        self.assertEqual(STANDING_N_REMAINING7, 27)
        self.assertEqual(self.n_remaining7, CYCLE241_N_WITHOUT)
        self.assertEqual(self.n_remaining7, self.n_remaining6 - self.n_share_280)
        self.assertEqual(29 - 2, 27)
        if self.n_remaining7 != 27:
            self.fail("measured N_remaining7 drifted from 27")
        if self.n_remaining7 != self.n_remaining6 - self.n_share_280:
            self.fail("leftover extra remaining-after-280 filter disagrees with nested 29−2")
        self.assertEqual(self.remaining6, STANDING_REMAINING6_SITES)
        self.assertEqual(self.remaining6, CYCLE241_REMAINING6_SITES)
        self.assertEqual(self.remaining7, STANDING_REMAINING7_SITES)
        self.assertEqual(len(self.remaining7), len(self.remaining7_stems))
        self.assertEqual(
            self.remaining7,
            leftover_extra_remaining_after_530_without_280(
                self.leftover_sites,
                self.next_stems,
            ),
        )
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.remaining7)
        self.assertIn(STANDING_IA2_174, self.remaining7)
        self.assertEqual(STANDING_IA2_174_NEXT_STEM, "000")
        for site in self.share_070:
            self.assertNotIn(site, self.remaining7)
        for site in self.share_071:
            self.assertNotIn(site, self.remaining7)
        for site in self.share_013:
            self.assertNotIn(site, self.remaining7)
        for site in self.share_001:
            self.assertNotIn(site, self.remaining7)
        for site in self.share_700:
            self.assertNotIn(site, self.remaining7)
        for site in self.share_530:
            self.assertNotIn(site, self.remaining7)
        for site in self.share_280:
            self.assertNotIn(site, self.remaining7)
        self.assertEqual(self.n_distinct_remaining4, STANDING_N_DISTINCT_REMAINING4)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING4, 26)
        self.assertEqual(self.n_distinct_remaining4, CYCLE234_N_DISTINCT)
        self.assertEqual(self.g, "700")
        self.assertEqual(self.tiebreak_k, 2)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertEqual(self.tied, STANDING_TIED_STEMS)
        self.assertEqual(self.tied, CYCLE234_TIED_STEMS)
        self.assertEqual(len(self.tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 7)
        self.assertEqual(self.tied_minus_700, STANDING_TIED_STEMS_MINUS_700)
        self.assertEqual(len(self.tied_minus_700), STANDING_N_TIED_MINUS_700)
        self.assertEqual(STANDING_N_TIED_MINUS_700, 6)
        self.assertEqual(self.tied_minus_700_530, STANDING_TIED_STEMS_MINUS_700_530)
        self.assertEqual(len(self.tied_minus_700_530), STANDING_N_TIED_MINUS_700_530)
        self.assertEqual(STANDING_N_TIED_MINUS_700_530, 5)
        self.assertEqual(self.tied_minus_700_530_280, STANDING_TIED_STEMS_MINUS_700_530_280)
        self.assertEqual(len(self.tied_minus_700_530_280), STANDING_N_TIED_MINUS_700_530_280)
        self.assertEqual(STANDING_N_TIED_MINUS_700_530_280, 4)
        if self.tied_minus_700_530_280 != STANDING_TIED_STEMS_MINUS_700_530_280:
            self.fail("nested cycle 234 7-way-tie-minus-700-530-280 drifted")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, HYPOTHESIS_K)
        self.assertEqual(STANDING_K, 2)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 25)
        self.assertEqual(self.k + self.n_without, self.n_remaining7)
        self.assertEqual(2 + 25, 27)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087(self.k)
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_280_EXACTLY_2_SHARE_087,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_280_EXACTLY_2_SHARE_087
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertTrue(self.equals_cycle234_087)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE234_087_SITES)
        self.assertTrue(matching_equals_cycle234_087_sites(self.matching))
        if len(self.matching) != 2 or not self.equals_cycle234_087:
            self.fail("leftover extra remaining-after-280 087 set drifted from cycle-234 pair")
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE236)
        self.assertFalse(STANDING_SAME_AS_CYCLE237)
        self.assertFalse(STANDING_SAME_AS_CYCLE238)
        self.assertFalse(STANDING_SAME_AS_CYCLE239)
        self.assertFalse(STANDING_SAME_AS_CYCLE240)
        self.assertFalse(STANDING_SAME_AS_CYCLE241)
        self.assertFalse(STANDING_SAME_AS_CYCLE242)
        self.assertFalse(STANDING_SAME_AS_CYCLE243)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE238)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE241)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_087_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_280_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_UNIQUE_MAX_REMAINING_AFTER_280_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertTrue(CYCLE226_CLAIM)
        self.assertTrue(CYCLE227_CLAIM)
        self.assertTrue(CYCLE228_CLAIM)
        self.assertTrue(CYCLE229_CLAIM)
        self.assertTrue(CYCLE230_CLAIM)
        self.assertTrue(CYCLE231_CLAIM)
        self.assertTrue(CYCLE232_CLAIM)
        self.assertTrue(CYCLE233_CLAIM)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertTrue(CYCLE235_CLAIM)
        self.assertTrue(CYCLE236_CLAIM)
        self.assertTrue(CYCLE237_CLAIM)
        self.assertTrue(CYCLE238_CLAIM)
        self.assertTrue(CYCLE239_CLAIM)
        self.assertTrue(CYCLE240_CLAIM)
        self.assertTrue(CYCLE241_CLAIM)
        self.assertTrue(CYCLE242_CLAIM)
        self.assertTrue(CYCLE243_CLAIM)
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_remaining_after_280_sites_share_280(self):
        """Two leftover extra remaining-after-280 sites are 090 076 087."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia3", 87), ("090", "076", "087", "499")),
            ((SIDE_IA, "Ia4", 162), ("090", "076", "087", "078")),
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
            self.assertEqual(stems[index + STANDING_N2], "087")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "087")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_REMAINING7_SITES)
            self.assertIn(site, STANDING_REMAINING6_SITES)
            self.assertIn(site, CYCLE241_REMAINING6_SITES)
            self.assertIn(site, CYCLE238_REMAINING5_SITES)
            self.assertIn(site, CYCLE234_REMAINING4_SITES)
            self.assertIn(site, CYCLE231_REMAINING3_SITES)
            self.assertIn(site, CYCLE228_REMAINING2_SITES)
            self.assertIn(site, CYCLE227_REMAINING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE226_MATCHING_SITES)
            self.assertNotIn(site, CYCLE227_MATCHING_SITES)
            self.assertNotIn(site, CYCLE228_MATCHING_SITES)
            self.assertNotIn(site, CYCLE229_I_SITES)
            self.assertNotIn(site, CYCLE231_MATCHING_SITES)
            self.assertNotIn(site, CYCLE232_I_SITES)
            self.assertNotIn(site, CYCLE235_MATCHING_SITES)
            self.assertNotIn(site, CYCLE236_I_SITES)
            self.assertNotIn(site, CYCLE238_MATCHING_SITES)
            self.assertNotIn(site, CYCLE239_I_SITES)
            self.assertNotIn(site, CYCLE241_MATCHING_SITES)
            self.assertNotIn(site, CYCLE242_I_SITES)
            self.assertNotIn(site, CYCLE207_I_SITES)
            self.assertNotIn(site, CYCLE195_I_SITES)
        self.assertEqual(self.matching, STANDING_CYCLE234_087_SITES)
        self.assertTrue(matching_equals_cycle234_087_sites(self.matching))
        self.assertNotIn(STANDING_IA2_174, self.matching)
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.matching)
        self.assertIn(STANDING_IA2_174, self.remaining7)
        self.assertEqual(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_IA2_174)],
            "000",
        )
        self.assertIsNone(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_NO_NEXT_SITES[0])]
        )
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "087")
            self.assertNotEqual(nxt, "280")
            self.assertNotEqual(nxt, "530")
            self.assertNotEqual(nxt, "700")
            self.assertNotEqual(nxt, "001")
            self.assertNotEqual(nxt, "013")
            self.assertNotEqual(nxt, "071")
            self.assertNotEqual(nxt, "070")
            self.assertIn(site, STANDING_REMAINING7_SITES)
        for site in self.share_070:
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
        for site in self.share_071:
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE195_I_SITES)
        for site in self.share_013:
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE229_I_SITES)
        for site in self.share_001:
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE232_I_SITES)
        for site in self.share_700:
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE235_MATCHING_SITES)
            self.assertIn(site, CYCLE236_I_SITES)
        for site in self.share_530:
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE238_MATCHING_SITES)
            self.assertIn(site, CYCLE239_I_SITES)
        for site in self.share_280:
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE241_MATCHING_SITES)
            self.assertIn(site, CYCLE242_I_SITES)
        other_tied = tuple(
            stem for stem in STANDING_TIED_STEMS_MINUS_700_530_280 if stem != "087"
        )
        self.assertEqual(other_tied, STANDING_OTHER_TIED_STEMS)
        self.assertEqual(other_tied, ("011", "005", "000"))
        for stem in other_tied:
            other = leftover_extra_remaining_after_001_with_g(
                self.leftover_sites,
                self.next_stems,
                stem,
            )
            self.assertEqual(len(other), 2)
            self.assertNotEqual(other, self.matching)
            for site in other:
                self.assertNotIn(site, self.matching)
                self.assertIn(site, self.remaining7)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining7)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertTrue(STANDING_I_ONLY_OF_090_076_087_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_280_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_UNIQUE_MAX_REMAINING_AFTER_280_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_240_239_238_237_236_234_233_232_223_195_and_171_still_compute(self):
        """Cycle 243 2/0 hapax, 242 2/0, 241 K=2/G=280, 240 2/0 hapax, 239 2/0, 238 K=2/G=530, 237 2/0 hapax, 236 2/0, 234 7-way tie, 233 3/0, 232 3/0, 223 69/3, 195 6/0, 171 43/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_243 = TestMamariI090076280Forward4gramsIOnlyScoreboard()
        prior_243.setUp()
        prior_243.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_243.test_survey_matches_computed_lock()
        self.assertEqual(prior_243.n_i_only, 2)
        self.assertEqual(prior_243.n_not_i_only, 0)
        self.assertTrue(prior_243.claim_holds)
        self.assertTrue(CYCLE243_CLAIM)
        if prior_243.n_i_only != 2 or prior_243.n_not_i_only != 0:
            self.fail("nested cycle 243 090 076 280 forward 4-grams 2/0 hapax drifted")
        prior_242 = TestMamariI3gram090076280IOnlyScoreboard()
        prior_242.setUp()
        prior_242.test_i_hits_are_two_on_ia_and_equal_leftover_extra_280()
        prior_242.test_3gram_is_zero_off_i_and_i_only()
        prior_242.test_survey_matches_computed_lock()
        self.assertEqual(prior_242.i_hits, CYCLE242_N_I)
        self.assertEqual(prior_242.i_hits, 2)
        self.assertEqual(prior_242.off_i_hits, CYCLE242_N_OFF_I)
        self.assertEqual(prior_242.off_i_hits, 0)
        self.assertEqual(prior_242.i_sites, CYCLE242_I_SITES)
        self.assertEqual(self.share_280, CYCLE242_I_SITES)
        self.assertTrue(prior_242.claim_holds)
        self.assertTrue(CYCLE242_CLAIM)
        if prior_242.i_hits != 2 or prior_242.off_i_hits != 0:
            self.fail("nested cycle 242 090 076 280 I-only 2/0 drifted")
        prior_241 = TestMamariILeftoverExtra090076RemainingAfter530Fwd280Scoreboard()
        prior_241.setUp()
        prior_241.test_counts_2_of_29_and_hypothesis_k_2_holds()
        prior_241.test_survey_matches_computed_lock()
        self.assertEqual(prior_241.n_leftover, 56)
        self.assertEqual(prior_241.n_remaining6, 29)
        self.assertEqual(prior_241.k, 2)
        self.assertEqual(CYCLE241_G, "280")
        self.assertEqual(prior_241.matching, CYCLE241_MATCHING_SITES)
        self.assertEqual(self.share_280, prior_241.matching)
        self.assertTrue(prior_241.claim_holds)
        self.assertTrue(CYCLE241_CLAIM)
        if (
            prior_241.n_leftover != 56
            or prior_241.n_remaining6 != 29
            or prior_241.k != 2
        ):
            self.fail(
                "nested cycle 241 leftover extra remaining-after-530 exactly 2 share 280 drifted"
            )
        prior_240 = TestMamariI090076530Forward4gramsIOnlyScoreboard()
        prior_240.setUp()
        prior_240.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_240.test_survey_matches_computed_lock()
        self.assertEqual(prior_240.n_i_only, 2)
        self.assertEqual(prior_240.n_not_i_only, 0)
        self.assertTrue(prior_240.claim_holds)
        self.assertTrue(CYCLE240_CLAIM)
        if prior_240.n_i_only != 2 or prior_240.n_not_i_only != 0:
            self.fail("nested cycle 240 090 076 530 forward 4-grams 2/0 hapax drifted")
        prior_239 = TestMamariI3gram090076530IOnlyScoreboard()
        prior_239.setUp()
        prior_239.test_i_hits_are_two_on_ia_and_equal_leftover_extra_530()
        prior_239.test_3gram_is_zero_off_i_and_i_only()
        prior_239.test_survey_matches_computed_lock()
        self.assertEqual(prior_239.i_hits, CYCLE239_N_I)
        self.assertEqual(prior_239.i_hits, 2)
        self.assertEqual(prior_239.off_i_hits, CYCLE239_N_OFF_I)
        self.assertEqual(prior_239.off_i_hits, 0)
        self.assertEqual(prior_239.i_sites, CYCLE239_I_SITES)
        self.assertEqual(self.share_530, CYCLE239_I_SITES)
        self.assertTrue(prior_239.claim_holds)
        self.assertTrue(CYCLE239_CLAIM)
        if prior_239.i_hits != 2 or prior_239.off_i_hits != 0:
            self.fail("nested cycle 239 090 076 530 I-only 2/0 drifted")
        prior_238 = TestMamariILeftoverExtra090076RemainingAfter700Fwd530Scoreboard()
        prior_238.setUp()
        prior_238.test_counts_2_of_31_and_hypothesis_k_2_holds()
        prior_238.test_survey_matches_computed_lock()
        self.assertEqual(prior_238.n_leftover, 56)
        self.assertEqual(prior_238.n_remaining5, 31)
        self.assertEqual(prior_238.k, 2)
        self.assertEqual(CYCLE238_G, "530")
        self.assertEqual(prior_238.matching, CYCLE238_MATCHING_SITES)
        self.assertEqual(self.share_530, prior_238.matching)
        self.assertTrue(prior_238.claim_holds)
        self.assertTrue(CYCLE238_CLAIM)
        if (
            prior_238.n_leftover != 56
            or prior_238.n_remaining5 != 31
            or prior_238.k != 2
        ):
            self.fail(
                "nested cycle 238 leftover extra remaining-after-700 exactly 2 share 530 drifted"
            )
        prior_237 = TestMamariI090076700Forward4gramsIOnlyScoreboard()
        prior_237.setUp()
        prior_237.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_237.test_survey_matches_computed_lock()
        self.assertEqual(prior_237.n_i_only, 2)
        self.assertEqual(prior_237.n_not_i_only, 0)
        self.assertTrue(prior_237.claim_holds)
        self.assertTrue(CYCLE237_CLAIM)
        if prior_237.n_i_only != 2 or prior_237.n_not_i_only != 0:
            self.fail("nested cycle 237 090 076 700 forward 4-grams 2/0 hapax drifted")
        prior_236 = TestMamariI3gram090076700IOnlyScoreboard()
        prior_236.setUp()
        prior_236.test_i_hits_are_two_on_ia_and_equal_leftover_extra_700()
        prior_236.test_3gram_is_zero_off_i_and_i_only()
        prior_236.test_survey_matches_computed_lock()
        self.assertEqual(prior_236.i_hits, CYCLE236_N_I)
        self.assertEqual(prior_236.i_hits, 2)
        self.assertEqual(prior_236.off_i_hits, CYCLE236_N_OFF_I)
        self.assertEqual(prior_236.off_i_hits, 0)
        self.assertEqual(prior_236.i_sites, CYCLE236_I_SITES)
        self.assertEqual(self.share_700, CYCLE236_I_SITES)
        self.assertTrue(prior_236.claim_holds)
        self.assertTrue(CYCLE236_CLAIM)
        if prior_236.i_hits != 2 or prior_236.off_i_hits != 0:
            self.fail("nested cycle 236 090 076 700 I-only 2/0 drifted")
        prior_235 = TestMamariILeftoverExtra090076RemainingAfter001Fwd700Scoreboard()
        prior_235.setUp()
        prior_235.test_counts_2_of_33_and_hypothesis_k_2_holds()
        prior_235.test_survey_matches_computed_lock()
        self.assertEqual(prior_235.n_leftover, 56)
        self.assertEqual(prior_235.n_remaining4, 33)
        self.assertEqual(prior_235.k, 2)
        self.assertEqual(CYCLE235_G, "700")
        self.assertEqual(prior_235.matching, CYCLE235_MATCHING_SITES)
        self.assertEqual(self.share_700, prior_235.matching)
        self.assertTrue(prior_235.claim_holds)
        self.assertTrue(CYCLE235_CLAIM)
        if (
            prior_235.n_leftover != 56
            or prior_235.n_remaining4 != 33
            or prior_235.k != 2
        ):
            self.fail(
                "nested cycle 235 leftover extra remaining-after-001 exactly 2 share 700 drifted"
            )
        prior_234 = TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard()
        prior_234.setUp()
        prior_234.test_counts_33_remaining4_g_700_k_2_and_hypothesis_loses()
        prior_234.test_survey_matches_computed_lock()
        self.assertEqual(prior_234.n_leftover, 56)
        self.assertEqual(prior_234.n_with_next, 55)
        self.assertEqual(prior_234.n_no_next, 1)
        self.assertEqual(prior_234.n_remaining4, 33)
        self.assertEqual(prior_234.n_distinct_remaining4, 26)
        self.assertEqual(prior_234.k, 2)
        self.assertEqual(CYCLE234_G, "700")
        self.assertFalse(prior_234.unique)
        self.assertEqual(prior_234.matching, CYCLE234_MATCHING_SITES)
        self.assertFalse(prior_234.claim_holds)
        self.assertFalse(CYCLE234_CLAIM)
        if (
            prior_234.n_leftover != 56
            or prior_234.n_with_next != 55
            or prior_234.n_no_next != 1
            or prior_234.n_remaining4 != 33
            or prior_234.n_distinct_remaining4 != 26
            or prior_234.k != 2
            or prior_234.unique
        ):
            self.fail(
                "nested cycle 234 leftover extra remaining-after-001 33 / "
                "26 distinct / 7-way tie G=700 K=2 drifted"
            )
        tied = tuple(
            stem for stem, count, _sites, _grams in prior_234.frequency if count == 2
        )
        self.assertEqual(tied, CYCLE234_TIED_STEMS)
        self.assertEqual(len(tied), 7)
        self.assertEqual(
            tuple(stem for stem in tied if stem not in ("700", "530", "280")),
            STANDING_TIED_STEMS_MINUS_700_530_280,
        )
        prior_233 = TestMamariI090076001Forward4gramsIOnlyScoreboard()
        prior_233.setUp()
        prior_233.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_233.test_survey_matches_computed_lock()
        self.assertEqual(prior_233.n_i_only, 3)
        self.assertEqual(prior_233.n_not_i_only, 0)
        self.assertTrue(prior_233.claim_holds)
        self.assertTrue(CYCLE233_CLAIM)
        if prior_233.n_i_only != 3 or prior_233.n_not_i_only != 0:
            self.fail("nested cycle 233 090 076 001 forward 4-grams 3/0 hapax drifted")
        prior_232 = TestMamariI3gram090076001IOnlyScoreboard()
        prior_232.setUp()
        prior_232.test_i_hits_are_three_on_ia_and_equal_leftover_extra_001()
        prior_232.test_3gram_is_zero_off_i_and_i_only()
        prior_232.test_survey_matches_computed_lock()
        self.assertEqual(prior_232.i_hits, CYCLE232_N_I)
        self.assertEqual(prior_232.i_hits, 3)
        self.assertEqual(prior_232.off_i_hits, CYCLE232_N_OFF_I)
        self.assertEqual(prior_232.off_i_hits, 0)
        self.assertEqual(prior_232.i_sites, CYCLE232_I_SITES)
        self.assertEqual(self.share_001, CYCLE232_I_SITES)
        self.assertTrue(prior_232.claim_holds)
        self.assertTrue(CYCLE232_CLAIM)
        if prior_232.i_hits != 3 or prior_232.off_i_hits != 0:
            self.fail("nested cycle 232 090 076 001 I-only 3/0 drifted")
        prior_231 = TestMamariILeftoverExtra090076RemainingAfter013NextStemScoreboard()
        prior_231.setUp()
        prior_231.test_counts_36_remaining3_g_001_k_3_and_hypothesis_holds()
        prior_231.test_survey_matches_computed_lock()
        self.assertEqual(prior_231.n_leftover, 56)
        self.assertEqual(prior_231.n_remaining3, 36)
        self.assertEqual(prior_231.k, 3)
        self.assertEqual(CYCLE231_G, "001")
        self.assertTrue(prior_231.claim_holds)
        self.assertTrue(CYCLE231_CLAIM)
        prior_230 = TestMamariI090076013Forward4gramsIOnlyScoreboard()
        prior_230.setUp()
        prior_230.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_230.test_survey_matches_computed_lock()
        self.assertEqual(prior_230.n_i_only, 5)
        self.assertEqual(prior_230.n_not_i_only, 0)
        self.assertTrue(prior_230.claim_holds)
        self.assertTrue(CYCLE230_CLAIM)
        if prior_230.n_i_only != 5 or prior_230.n_not_i_only != 0:
            self.fail("nested cycle 230 090 076 013 forward 4-grams 5/0 hapax drifted")
        prior_229 = TestMamariI3gram090076013IOnlyScoreboard()
        prior_229.setUp()
        prior_229.test_i_hits_are_five_on_ia_and_equal_leftover_extra_013()
        prior_229.test_3gram_is_zero_off_i_and_i_only()
        prior_229.test_survey_matches_computed_lock()
        self.assertEqual(prior_229.i_hits, CYCLE229_N_I)
        self.assertEqual(prior_229.i_hits, 5)
        self.assertEqual(prior_229.off_i_hits, CYCLE229_N_OFF_I)
        self.assertEqual(prior_229.off_i_hits, 0)
        self.assertEqual(prior_229.i_sites, CYCLE229_I_SITES)
        self.assertEqual(self.share_013, CYCLE229_I_SITES)
        self.assertTrue(prior_229.claim_holds)
        self.assertTrue(CYCLE229_CLAIM)
        if prior_229.i_hits != 5 or prior_229.off_i_hits != 0:
            self.fail("nested cycle 229 090 076 013 I-only 5/0 drifted")
        prior_228 = TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard()
        prior_228.setUp()
        prior_228.test_counts_41_remaining2_g_013_k_5_and_hypothesis_holds()
        prior_228.test_survey_matches_computed_lock()
        self.assertEqual(prior_228.n_leftover, 56)
        self.assertEqual(prior_228.n_remaining2, 41)
        self.assertEqual(prior_228.k, 5)
        self.assertEqual(CYCLE228_G, "013")
        self.assertTrue(prior_228.claim_holds)
        self.assertTrue(CYCLE228_CLAIM)
        prior_227 = TestMamariILeftoverExtra090076RemainingNextStemScoreboard()
        prior_227.setUp()
        prior_227.test_counts_47_remaining_g_071_k_6_and_hypothesis_holds()
        prior_227.test_survey_matches_computed_lock()
        self.assertEqual(prior_227.n_leftover, 56)
        self.assertEqual(prior_227.n_remaining, 47)
        self.assertEqual(prior_227.k, 6)
        self.assertEqual(CYCLE227_G, "071")
        self.assertTrue(prior_227.claim_holds)
        self.assertTrue(CYCLE227_CLAIM)
        prior_226 = TestMamariILeftoverExtra090076Forward070Scoreboard()
        prior_226.setUp()
        prior_226.test_counts_8_of_56_and_hypothesis_k_8_holds()
        prior_226.test_survey_matches_computed_lock()
        self.assertEqual(prior_226.n_leftover, 56)
        self.assertEqual(prior_226.k, 8)
        self.assertEqual(CYCLE226_G, "070")
        self.assertTrue(prior_226.claim_holds)
        self.assertTrue(CYCLE226_CLAIM)
        prior_225 = TestMamariILeftoverExtra090076ForwardStemScoreboard()
        prior_225.setUp()
        prior_225.test_counts_30_distinct_next_stems_and_claim_loses()
        prior_225.test_survey_matches_computed_lock()
        self.assertEqual(prior_225.n_leftover, 56)
        self.assertEqual(prior_225.n_distinct, 30)
        self.assertEqual(prior_225.g, "070")
        self.assertEqual(prior_225.k, 8)
        self.assertFalse(prior_225.claim_holds)
        self.assertFalse(CYCLE225_SHARE_ONE)
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
        prior_195 = TestMamariI3gram090076071IOnlyScoreboard()
        prior_195.setUp()
        prior_195.test_i_hits_are_six_on_ia()
        prior_195.test_3gram_is_zero_off_i_and_i_only()
        prior_195.test_survey_matches_computed_lock()
        self.assertEqual(prior_195.i_hits, CYCLE195_N_I)
        self.assertEqual(prior_195.i_hits, 6)
        self.assertEqual(prior_195.off_i_hits, CYCLE195_N_OFF_I)
        self.assertEqual(prior_195.off_i_hits, 0)
        self.assertEqual(prior_195.i_sites, CYCLE195_I_SITES)
        self.assertEqual(self.share_071, CYCLE195_I_SITES)
        self.assertTrue(prior_195.claim_holds)
        self.assertTrue(CYCLE195_CLAIM)
        if prior_195.i_hits != 6 or prior_195.off_i_hits != 0:
            self.fail("nested cycle 195 090 076 071 I-only 6/0 drifted")
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
        """CORPUS_SURVEY.json records the cycle-244 leftover extra remaining-after-280 fwd087 lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_280_fwd087"]
        self.assertEqual(lock["cycle"], 244)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(tuple(lock["forward_3gram"]), ("090", "076", "087"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(tuple(lock["locked_forward_stems"]), ("070", "071", "013", "001"))
        self.assertEqual(
            tuple(lock["locked_forward_stems_after_700"]),
            LOCKED_FORWARD_STEMS_AFTER_700,
        )
        self.assertEqual(
            tuple(lock["locked_forward_stems_after_530"]),
            LOCKED_FORWARD_STEMS_AFTER_530,
        )
        self.assertEqual(
            tuple(lock["locked_forward_stems_after_280"]),
            LOCKED_FORWARD_STEMS_AFTER_280,
        )
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
        self.assertEqual(lock["N_share_070"], STANDING_N_SHARE_070)
        self.assertEqual(lock["N_share_070"], 8)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 47)
        self.assertEqual(lock["N_share_071"], STANDING_N_SHARE_071)
        self.assertEqual(lock["N_share_071"], 6)
        self.assertEqual(lock["N_remaining2"], STANDING_N_REMAINING2)
        self.assertEqual(lock["N_remaining2"], 41)
        self.assertEqual(lock["N_share_013"], STANDING_N_SHARE_013)
        self.assertEqual(lock["N_share_013"], 5)
        self.assertEqual(lock["N_remaining3"], STANDING_N_REMAINING3)
        self.assertEqual(lock["N_remaining3"], 36)
        self.assertEqual(lock["N_share_001"], STANDING_N_SHARE_001)
        self.assertEqual(lock["N_share_001"], 3)
        self.assertEqual(lock["ia2_174_next_stem"], STANDING_IA2_174_NEXT_STEM)
        self.assertEqual(lock["ia2_174_next_stem"], "000")
        self.assertEqual(lock["N_remaining4"], STANDING_N_REMAINING4)
        self.assertEqual(lock["N_remaining4"], 33)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_001_sites"]),
            CYCLE234_REMAINING4_SITES,
        )
        self.assertEqual(lock["N_distinct_remaining4"], STANDING_N_DISTINCT_REMAINING4)
        self.assertEqual(lock["N_distinct_remaining4"], 26)
        self.assertEqual(lock["N_share_700"], STANDING_N_SHARE_700)
        self.assertEqual(lock["N_share_700"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_700_sites"]),
            CYCLE235_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining5"], STANDING_N_REMAINING5)
        self.assertEqual(lock["N_remaining5"], 31)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_700_sites"]),
            CYCLE238_REMAINING5_SITES,
        )
        self.assertEqual(lock["N_share_530"], STANDING_N_SHARE_530)
        self.assertEqual(lock["N_share_530"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_530_sites"]),
            CYCLE238_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining6"], STANDING_N_REMAINING6)
        self.assertEqual(lock["N_remaining6"], 29)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_530_sites"]),
            STANDING_REMAINING6_SITES,
        )
        self.assertEqual(lock["N_share_280"], STANDING_N_SHARE_280)
        self.assertEqual(lock["N_share_280"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_280_sites"]),
            CYCLE241_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining7"], STANDING_N_REMAINING7)
        self.assertEqual(lock["N_remaining7"], 27)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_280_sites"]),
            STANDING_REMAINING7_SITES,
        )
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "087")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 7)
        self.assertEqual(
            tuple(lock["tied_stems_minus_700"]),
            STANDING_TIED_STEMS_MINUS_700,
        )
        self.assertEqual(lock["N_tied_minus_700"], STANDING_N_TIED_MINUS_700)
        self.assertEqual(lock["N_tied_minus_700"], 6)
        self.assertEqual(
            tuple(lock["tied_stems_minus_700_530"]),
            STANDING_TIED_STEMS_MINUS_700_530,
        )
        self.assertEqual(lock["N_tied_minus_700_530"], STANDING_N_TIED_MINUS_700_530)
        self.assertEqual(lock["N_tied_minus_700_530"], 5)
        self.assertEqual(
            tuple(lock["tied_stems_minus_700_530_280"]),
            STANDING_TIED_STEMS_MINUS_700_530_280,
        )
        self.assertEqual(lock["N_tied_minus_700_530_280"], STANDING_N_TIED_MINUS_700_530_280)
        self.assertEqual(lock["N_tied_minus_700_530_280"], 4)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 25)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_280_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle234_087_sites"])
        self.assertEqual(
            lock["matching_equals_cycle234_087_sites"],
            STANDING_MATCHING_EQUALS_CYCLE234_087_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_280_local_4grams"],
            matching_leftover_extra_remaining_after_280_fwd087_local_4gram_rows(),
        )
        self.assertEqual(lock["cycle243_N_i_only"], CYCLE243_N_I_ONLY)
        self.assertEqual(lock["cycle243_N_i_only"], 2)
        self.assertEqual(lock["cycle243_N_not_i_only"], CYCLE243_N_NOT_I_ONLY)
        self.assertEqual(lock["cycle243_N_not_i_only"], 0)
        self.assertEqual(lock["cycle242_N_I"], CYCLE242_N_I)
        self.assertEqual(lock["cycle242_N_I"], 2)
        self.assertEqual(lock["cycle242_N_off_I"], CYCLE242_N_OFF_I)
        self.assertEqual(lock["cycle242_N_off_I"], 0)
        self.assertEqual(lock["cycle241_G"], CYCLE241_G)
        self.assertEqual(lock["cycle241_G"], "280")
        self.assertEqual(lock["cycle241_K"], CYCLE241_K)
        self.assertEqual(lock["cycle241_K"], 2)
        self.assertEqual(lock["cycle241_N_remaining6"], CYCLE241_N_REMAINING6)
        self.assertEqual(lock["cycle241_N_remaining6"], 29)
        self.assertEqual(lock["cycle240_N_i_only"], CYCLE240_N_I_ONLY)
        self.assertEqual(lock["cycle240_N_i_only"], 2)
        self.assertEqual(lock["cycle240_N_not_i_only"], CYCLE240_N_NOT_I_ONLY)
        self.assertEqual(lock["cycle240_N_not_i_only"], 0)
        self.assertEqual(lock["cycle239_N_I"], CYCLE239_N_I)
        self.assertEqual(lock["cycle239_N_I"], 2)
        self.assertEqual(lock["cycle239_N_off_I"], CYCLE239_N_OFF_I)
        self.assertEqual(lock["cycle239_N_off_I"], 0)
        self.assertEqual(lock["cycle238_G"], CYCLE238_G)
        self.assertEqual(lock["cycle238_G"], "530")
        self.assertEqual(lock["cycle238_K"], CYCLE238_K)
        self.assertEqual(lock["cycle238_K"], 2)
        self.assertEqual(lock["cycle238_N_remaining5"], CYCLE238_N_REMAINING5)
        self.assertEqual(lock["cycle238_N_remaining5"], 31)
        self.assertEqual(lock["cycle237_N_i_only"], CYCLE237_N_I_ONLY)
        self.assertEqual(lock["cycle237_N_i_only"], 2)
        self.assertEqual(lock["cycle237_N_not_i_only"], CYCLE237_N_NOT_I_ONLY)
        self.assertEqual(lock["cycle237_N_not_i_only"], 0)
        self.assertEqual(lock["cycle236_N_I"], CYCLE236_N_I)
        self.assertEqual(lock["cycle236_N_I"], 2)
        self.assertEqual(lock["cycle236_N_off_I"], CYCLE236_N_OFF_I)
        self.assertEqual(lock["cycle236_N_off_I"], 0)
        self.assertEqual(lock["cycle235_G"], CYCLE235_G)
        self.assertEqual(lock["cycle235_G"], "700")
        self.assertEqual(lock["cycle235_K"], CYCLE235_K)
        self.assertEqual(lock["cycle235_K"], 2)
        self.assertEqual(lock["cycle235_N_remaining4"], CYCLE235_N_REMAINING4)
        self.assertEqual(lock["cycle235_N_remaining4"], 33)
        self.assertEqual(lock["cycle234_N_remaining4"], CYCLE234_N_REMAINING4)
        self.assertEqual(lock["cycle234_N_remaining4"], 33)
        self.assertEqual(lock["cycle234_N_distinct_remaining4"], CYCLE234_N_DISTINCT)
        self.assertEqual(lock["cycle234_N_distinct_remaining4"], 26)
        self.assertEqual(lock["cycle234_N_tied_at_K"], CYCLE234_N_TIED_AT_K)
        self.assertEqual(lock["cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["cycle234_G_uniquely_most_frequent"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087"])
        self.assertEqual(
            lock["i_leftover_extra_090_076_remaining_after_280_exactly_2_share_087"],
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_280_EXACTLY_2_SHARE_087,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle226"])
        self.assertFalse(lock["same_as_cycle234"])
        self.assertFalse(lock["same_as_cycle235"])
        self.assertFalse(lock["same_as_cycle236"])
        self.assertFalse(lock["same_as_cycle237"])
        self.assertFalse(lock["same_as_cycle238"])
        self.assertFalse(lock["same_as_cycle239"])
        self.assertFalse(lock["same_as_cycle240"])
        self.assertFalse(lock["same_as_cycle241"])
        self.assertFalse(lock["same_as_cycle242"])
        self.assertFalse(lock["same_as_cycle243"])
        self.assertTrue(lock["same_claim_shape_as_cycle226"])
        self.assertTrue(lock["same_claim_shape_as_cycle235"])
        self.assertTrue(lock["same_claim_shape_as_cycle238"])
        self.assertTrue(lock["same_claim_shape_as_cycle241"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_090_076_087_is_not_this_cycle"])
        self.assertTrue(lock["previous_4grams_of_090_076_280_are_not_this_cycle"])
        self.assertTrue(lock["unique_max_remaining_after_280_is_not_this_cycle"])
        self.assertTrue(lock["other_tied_stems_not_locked"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle224_no_next_4gram_is_not_no_next_token"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_090_076_280_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_280_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_530_fwd280_unchanged"])
        self.assertTrue(lock["standing_i_090_076_530_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_530_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_700_fwd530_unchanged"])
        self.assertTrue(lock["standing_i_090_076_700_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_700_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_fwd700_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_001_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_001_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_013_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_013_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_013_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_071_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_090_076_280_forward_4grams_i_only"]["cycle"], 243)
        self.assertTrue(
            self.survey["i_090_076_280_forward_4grams_i_only"][
                "i_090_076_280_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_280_forward_4grams_i_only"]["N_i_only"], 2)
        self.assertEqual(self.survey["i_090_076_280_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_280_i_only"]["cycle"], 242)
        self.assertTrue(self.survey["i_3gram_090_076_280_i_only"]["i_3gram_090_076_280_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_280_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_280_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_530_fwd280"]["cycle"],
            241,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_530_fwd280"][
                "i_leftover_extra_090_076_remaining_after_530_exactly_2_share_280"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_530_fwd280"]["G"],
            "280",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_530_fwd280"]["K"],
            2,
        )
        self.assertEqual(self.survey["i_090_076_530_forward_4grams_i_only"]["cycle"], 240)
        self.assertTrue(
            self.survey["i_090_076_530_forward_4grams_i_only"][
                "i_090_076_530_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_530_forward_4grams_i_only"]["N_i_only"], 2)
        self.assertEqual(self.survey["i_090_076_530_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_530_i_only"]["cycle"], 239)
        self.assertTrue(self.survey["i_3gram_090_076_530_i_only"]["i_3gram_090_076_530_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_530_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_530_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]["cycle"],
            238,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"][
                "i_leftover_extra_090_076_remaining_after_700_exactly_2_share_530"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]["G"],
            "530",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]["K"],
            2,
        )
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["cycle"], 237)
        self.assertTrue(
            self.survey["i_090_076_700_forward_4grams_i_only"][
                "i_090_076_700_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["N_i_only"], 2)
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["cycle"], 236)
        self.assertTrue(self.survey["i_3gram_090_076_700_i_only"]["i_3gram_090_076_700_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_fwd700"]["cycle"],
            235,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_001_fwd700"][
                "i_leftover_extra_090_076_remaining_after_001_exactly_2_share_700"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_fwd700"]["G"],
            "700",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_fwd700"]["K"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]["cycle"],
            234,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"][
                "i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]["N_remaining4"],
            33,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]["N_tied_at_K"],
            7,
        )
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["cycle"], 233)
        self.assertTrue(
            self.survey["i_090_076_001_forward_4grams_i_only"][
                "i_090_076_001_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["N_i_only"], 3)
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["cycle"], 232)
        self.assertTrue(self.survey["i_3gram_090_076_001_i_only"]["i_3gram_090_076_001_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["cycle"], 195)
        self.assertTrue(self.survey["i_3gram_090_076_071_i_only"]["i_3gram_090_076_071_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariILeftoverExtra090076RemainingAfter280Fwd087ImageSnapshot(
    unittest.TestCase
):
    """Cycle 244 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
