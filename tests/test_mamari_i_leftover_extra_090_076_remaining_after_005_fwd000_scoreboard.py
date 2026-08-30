"""I's cycle-253 leftover extra remaining-after-005 forward-000 cluster lock.

Cycle 253 text-search lock. Uses already-vendored A–V and the
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
K=2. Cycles 235–237 closed 700, 238–240 closed 530, 241–243
closed 280, 244–246 closed 087, 247–249 closed 011, and
250–252 closed 005 (K=2; I-only 2/0 extra I=0; two forward
4-grams hapax 1/0). Last remaining tied stem from cycle 234
is 000 at count 2. This cycle locks that last tied stem as
an exact-K claim on remaining-after-005.
Do not lock I-only of 090 076 000. Do not lock unique-max
remaining-after-005. Previous 4-grams of 090 076 005 are not
this cycle. Off-I T sites are not this cycle except as
matching remaining-after-005 000 sites if they happen to be
leftover extra (they should not be). I-only of leftover extra
4-grams is leftover-of-leftover for a later cycle. 076 071
and 076 070 do not count as this 2-gram. Inside-family sites
do not count as leftover extra. Do not count cycle 219
090 076 070 000 (T leak; leftover extra Ia14[140] next is
070) as remaining-after-005 090 076 000.

Leftover extra remaining-after-005 = leftover extra I 090 076
sites with a next token whose next token is none of 070, 071,
013, 001, 700, 530, 280, 087, 011, or 005. Nested-check leftover
extra N_leftover==56, N_with_next==55, N_no_next==1 at
Ia4[166], leftover extra exactly 8 share 070, leftover extra
remaining N_remaining==47 G=071 K=6, leftover extra
remaining-after-071 N_remaining2==41 G=013 K=5, leftover extra
remaining-after-013 N_remaining3==36 G=001 K=3, leftover extra
remaining-after-001 N_remaining4==33 exactly 2 share 700,
leftover extra remaining-after-700 N_remaining5==31 exactly 2
share 530, leftover extra remaining-after-530 N_remaining6==29
exactly 2 share 280, leftover extra remaining-after-280
N_remaining7==27 exactly 2 share 087, leftover extra
remaining-after-087 N_remaining8==25 exactly 2 share 011,
leftover extra remaining-after-011 N_remaining9==23 exactly 2
share 005 (do not retune cycles 225–250). Nested-check cycle
251 090 076 005 I-only 2/0 extra I=0 and cycle 252 two forward
4-grams 1/0 each (do not retune). Nested-check
N_remaining10==21 (23−2). Ia2[174] has next token 000 and is
remaining-after-005; it is not no-next (line ends after that
one token, so next 4-gram is None). Ia14[140] 090 076 070 000
is leftover extra forward 070, not remaining-after-005 000.

Hypothesis K=2: leftover extra remaining-after-005 includes
exactly 2 sites that share next stem 000 (forward 3-gram
090 076 000). Measured: K=2 at Ia2[174], Ia10[141]; next
4-grams None / 090 076 000 076. Cycle 234 listed 000×2 among
the 7-way tie; re-measured, not assumed. Claim that can lose:
i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000.
True iff K==2. The claim is true. Same claim-shape as cycle
226 (leftover extra exactly 8 share forward 070) and cycle
250 (remaining-after-011 exactly 2 share 005). This can lose
if remaining-after-005 does not contain exactly 2 000
next-stem sites, or if N_remaining10 ≠ 21. Nested cycle 252
2/2 hapax, cycle 251 2/0 extra I=0, cycle 250 K=2 / G=005,
cycle 249 4/4 hapax, cycle 234 7-way tie at 2, cycle 223
69/3, cycle 219 7/8 lose on T 000, and cycle 171 43/0 stay.
Do not assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""


import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_005_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_005_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE252_CLAIM,
    STANDING_N_I_ONLY as CYCLE252_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE252_N_NOT_I_ONLY,
    TestMamariI090076005Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_011_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_011_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE249_CLAIM,
    STANDING_N_I_ONLY as CYCLE249_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE249_N_NOT_I_ONLY,
    TestMamariI090076011Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_CLAIM,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
)
from tests.test_mamari_i_3gram_090_076_005_i_only_scoreboard import (
    GRAM3 as CYCLE251_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE251_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_005_I_ONLY as CYCLE251_CLAIM,
    STANDING_I_SITES as CYCLE251_I_SITES,
    STANDING_N_EXTRA as CYCLE251_N_EXTRA,
    STANDING_N_I as CYCLE251_N_I,
    STANDING_N_OFF_I as CYCLE251_N_OFF_I,
    TestMamariI3gram090076005IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_011_fwd005_scoreboard import (
    GRAM3_FORWARD as CYCLE250_GRAM3,
    STANDING_G as CYCLE250_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_011_EXACTLY_2_SHARE_005 as CYCLE250_CLAIM,
    STANDING_K as CYCLE250_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE250_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE250_MATCHING_SITES,
    STANDING_N_REMAINING9 as CYCLE250_N_REMAINING9,
    STANDING_N_WITHOUT as CYCLE250_N_WITHOUT,
    STANDING_REMAINING9_SITES as CYCLE250_REMAINING9_SITES,
    leftover_extra_remaining_after_011,
    leftover_extra_remaining_after_011_nested_counts_hold,
    leftover_extra_remaining_after_011_next_stems,
    leftover_extra_remaining_after_011_with_005,
    leftover_extra_remaining_after_011_without_005,
    TestMamariILeftoverExtra090076RemainingAfter011Fwd005Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_087_fwd011_scoreboard import (
    STANDING_G as CYCLE247_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_011 as CYCLE247_CLAIM,
    STANDING_K as CYCLE247_K,
    STANDING_MATCHING_SITES as CYCLE247_MATCHING_SITES,
    STANDING_N_REMAINING8 as CYCLE247_N_REMAINING8,
    STANDING_REMAINING8_SITES as CYCLE247_REMAINING8_SITES,
    leftover_extra_remaining_after_087,
    leftover_extra_remaining_after_087_with_011,
    leftover_extra_remaining_after_087_without_011,
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
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
    STANDING_I_SITES as CYCLE195_I_SITES,
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
    leftover_extra_with_forward_070,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_IA2_174,
    STANDING_IA2_174_NEXT_STEM,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_NO_NEXT_SITES,
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
    leftover_sites_with_next,
    leftover_sites_without_next,
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_fwd700_scoreboard import (
    STANDING_G as CYCLE235_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_2_SHARE_700 as CYCLE235_CLAIM,
    STANDING_K as CYCLE235_K,
    STANDING_MATCHING_SITES as CYCLE235_MATCHING_SITES,
    leftover_extra_remaining_after_001_with_700,
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
    leftover_extra_remaining_after_013,
    leftover_extra_remaining_after_013_with_g,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_071_next_stem_scoreboard import (
    STANDING_G as CYCLE228_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G as CYCLE228_CLAIM,
    STANDING_K as CYCLE228_K,
    STANDING_MATCHING_SITES as CYCLE228_MATCHING_SITES,
    STANDING_REMAINING2_SITES as CYCLE228_REMAINING2_SITES,
    leftover_extra_remaining_after_071,
    leftover_extra_remaining_after_071_with_g,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_700_fwd530_scoreboard import (
    STANDING_G as CYCLE238_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_700_EXACTLY_2_SHARE_530 as CYCLE238_CLAIM,
    STANDING_K as CYCLE238_K,
    STANDING_MATCHING_SITES as CYCLE238_MATCHING_SITES,
    leftover_extra_remaining_after_700,
    leftover_extra_remaining_after_700_with_530,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_530_fwd280_scoreboard import (
    STANDING_G as CYCLE241_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_530_EXACTLY_2_SHARE_280 as CYCLE241_CLAIM,
    STANDING_K as CYCLE241_K,
    STANDING_MATCHING_SITES as CYCLE241_MATCHING_SITES,
    leftover_extra_remaining_after_530,
    leftover_extra_remaining_after_530_with_280,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_280_fwd087_scoreboard import (
    STANDING_G as CYCLE244_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_280_EXACTLY_2_SHARE_087 as CYCLE244_CLAIM,
    STANDING_K as CYCLE244_K,
    STANDING_MATCHING_SITES as CYCLE244_MATCHING_SITES,
    leftover_extra_remaining_after_280,
    leftover_extra_remaining_after_280_with_087,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    STANDING_G as CYCLE227_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 as CYCLE227_CLAIM,
    STANDING_K as CYCLE227_K,
    STANDING_MATCHING_SITES as CYCLE227_MATCHING_SITES,
    STANDING_REMAINING_SITES as CYCLE227_REMAINING_SITES,
    leftover_extra_remaining,
    leftover_extra_remaining_with_g,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_K as CYCLE222_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING_LEFTOVERS,
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
from tests.test_mamari_i_3gram_090_076_001_i_only_scoreboard import (
    STANDING_I_SITES as CYCLE232_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_013_i_only_scoreboard import (
    STANDING_I_SITES as CYCLE229_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_700_i_only_scoreboard import (
    STANDING_I_SITES as CYCLE236_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_530_i_only_scoreboard import (
    STANDING_I_SITES as CYCLE239_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_280_i_only_scoreboard import (
    STANDING_I_SITES as CYCLE242_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    STANDING_I_SITES as CYCLE245_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE248_EXTRA_I_SITES,
    STANDING_I_SITES as CYCLE248_I_SITES,
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
LOCKED_FORWARD_STEM_087 = "087"
LOCKED_FORWARD_STEM_011 = "011"
LOCKED_FORWARD_STEM_005 = "005"
LOCKED_FORWARD_STEMS_AFTER_011 = (
    "070",
    "071",
    "013",
    "001",
    "700",
    "530",
    "280",
    "087",
    "011",
)
LOCKED_FORWARD_STEMS_AFTER_005 = (
    "070",
    "071",
    "013",
    "001",
    "700",
    "530",
    "280",
    "087",
    "011",
    "005",
)
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "000")
GRAM3_NESTED_005 = ("090", "076", "005")
GRAM3_NESTED_011 = ("090", "076", "011")
STANDING_IA2_159 = (SIDE_IA, "Ia2", 159)
STANDING_IA2_159_NEXT_STEM = "700"
STANDING_IA2_159_NEXT_4GRAM = ("090", "076", "700", "011")
STANDING_IA14_140 = (SIDE_IA, "Ia14", 140)
STANDING_IA14_140_NEXT_STEM = "070"
STANDING_IA14_140_NEXT_4GRAM = ("090", "076", "070", "000")
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
STANDING_TIED_STEMS_MINUS_700_530_280_087_011_005 = ("000",)
STANDING_N_TIED_MINUS_700_530_280_087_011_005 = 1
STANDING_OTHER_TIED_STEMS = ()
STANDING_N_SHARE_700 = 2
STANDING_N_REMAINING5 = 31
STANDING_N_SHARE_530 = 2
STANDING_N_REMAINING6 = 29
STANDING_N_SHARE_280 = 2
STANDING_N_REMAINING7 = 27
STANDING_N_SHARE_087 = 2
STANDING_N_REMAINING8 = 25
STANDING_N_SHARE_011 = 2
STANDING_N_REMAINING9 = 23
STANDING_N_SHARE_005 = 2
STANDING_N_REMAINING10 = 21
STANDING_G = "000"
STANDING_K = 2
STANDING_N_WITHOUT = 19
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_UNIQUE_MAX_REMAINING_AFTER_005_IS_NOT_THIS_CYCLE = True
STANDING_REMAINING9_SITES = CYCLE250_REMAINING9_SITES
STANDING_REMAINING10_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
    (SIDE_IA, "Ia2", 165),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia14", 177),
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia10", 141),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    None,
    ("090", "076", "000", "076"),
)
STANDING_IA2_174_HAS_NO_NEXT_4GRAM = True
STANDING_CYCLE234_000_SITES = CYCLE234_FREQUENCY[6][2]
STANDING_MATCHING_EQUALS_CYCLE234_000_SITES = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000 = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_005_fwd000"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE226 = False
STANDING_SAME_AS_CYCLE234 = False
STANDING_SAME_AS_CYCLE250 = False
STANDING_SAME_AS_CYCLE251 = False
STANDING_SAME_AS_CYCLE252 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE250 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_090_076_000_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_4GRAMS_OF_090_076_005_ARE_NOT_THIS_CYCLE = True
STANDING_OTHER_TIED_STEMS_NOT_LOCKED = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_090_076_070_000_IS_NOT_REMAINING_AFTER_005 = True
STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN = True


def leftover_extra_remaining_after_005(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_005,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra with-next sites whose next token is none of 070/071/013/001/700/530/280/087/011/005."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_005_next_stems(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_005,
) -> tuple[str, ...]:
    """Next stems of leftover extra remaining-after-005 sites."""
    locked_set = set(locked)
    return tuple(
        nxt
        for nxt in next_stems
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_005_with_000(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-005 sites whose next token is 000."""
    remaining10 = set(leftover_extra_remaining_after_005(sites, next_stems))
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem and site in remaining10
    )


def leftover_extra_remaining_after_005_without_000(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_005,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-005 sites whose next token is not 000."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set and nxt != stem
    )


def leftover_extra_remaining_after_005_nested_counts_hold(
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
    n_share_087: int,
    n_remaining8: int,
    n_share_011: int,
    n_remaining9: int,
    n_share_005: int,
    n_remaining10: int,
    expected_share_005: int = STANDING_N_SHARE_005,
    expected_remaining10: int = STANDING_N_REMAINING10,
) -> bool:
    """Nested leftover extra chain through remaining-after-005 N_remaining10==21."""
    return leftover_extra_remaining_after_011_nested_counts_hold(
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
        n_share_280,
        n_remaining7,
        n_share_087,
        n_remaining8,
        n_share_011,
        n_remaining9,
    ) and n_share_005 == expected_share_005 and n_remaining10 == expected_remaining10 and (
        n_remaining10 == n_remaining9 - n_share_005
    )


def matching_equals_cycle234_000_sites(
    matching_sites: tuple[tuple[str, str, int], ...],
    cycle234_sites: tuple[tuple[str, str, int], ...] = STANDING_CYCLE234_000_SITES,
) -> bool:
    """True iff remaining-after-005 090 076 000 sites equal cycle 234's 000 pair."""
    return matching_sites == cycle234_sites


def matching_leftover_extra_remaining_after_005_fwd000_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...] | None, ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-005 000 next-4-gram rows."""
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
                "next_4gram": list(next_gram) if next_gram is not None else None,
                "forward_3gram": list(GRAM3_FORWARD),
            }
        )
    return rows


def i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(
    k: int,
    expected: int = HYPOTHESIS_K,
) -> bool:
    """True iff K equals the hypothesized 2."""
    return k == expected


class TestILeftoverExtra090076RemainingAfter005Fwd000Helpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-005 forward 000. No CV, no LLM."""

    def test_forward_000_requires_remaining_after_005_next_stem(self):
        """Next stem 000 is remaining-after-005; locked 070/071/013/001/700/530/280/087/011/005 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "000"))
        self.assertEqual(GRAM3_NESTED_005, ("090", "076", "005"))
        self.assertEqual(GRAM3_NESTED_011, ("090", "076", "011"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("070", "071", "013", "001"))
        self.assertEqual(
            LOCKED_FORWARD_STEMS_AFTER_011,
            ("070", "071", "013", "001", "700", "530", "280", "087", "011"),
        )
        self.assertEqual(
            LOCKED_FORWARD_STEMS_AFTER_005,
            ("070", "071", "013", "001", "700", "530", "280", "087", "011", "005"),
        )
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_000 = ["999", "090", "076", "000", "076"]
        self.assertEqual(site_next_stem(has_000, 1, GRAM2), "000")
        self.assertEqual(site_forward_3gram(has_000, 1, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_000, 1, GRAM2),
            ("090", "076", "000", "076"),
        )
        has_005 = ["999", "090", "076", "005", "406"]
        self.assertEqual(site_next_stem(has_005, 1, GRAM2), "005")
        self.assertNotEqual(site_next_stem(has_005, 1, GRAM2), "000")
        has_070_000 = ["059", "090", "076", "070", "000"]
        self.assertEqual(site_next_stem(has_070_000, 1, GRAM2), "070")
        self.assertNotEqual(site_next_stem(has_070_000, 1, GRAM2), "000")
        self.assertEqual(site_next_4gram(has_070_000, 1, GRAM2), CYCLE219_LEAK_4GRAM)
        self.assertEqual(CYCLE219_LEAK_4GRAM, STANDING_IA14_140_NEXT_4GRAM)
        end_of_line = ["005", "406", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        one_token_then_eol = ["009", "009", "090", "076", "000"]
        self.assertEqual(site_next_stem(one_token_then_eol, 2, GRAM2), "000")
        self.assertEqual(site_forward_3gram(one_token_then_eol, 2, GRAM2), GRAM3_FORWARD)
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
            (SIDE_IA, "Ia1", 10),
            (SIDE_IA, "Ia1", 11),
        )
        planted_stems = (
            "000", "005", "011", "087", "280", "530", "700", "070", "071", "013", "001", None,
        )
        rem10 = leftover_extra_remaining_after_005(planted_sites, planted_stems)
        self.assertEqual(rem10, (planted_sites[0],))
        self.assertEqual(
            leftover_extra_remaining_after_005_with_000(planted_sites, planted_stems),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_extra_remaining_after_005_without_000(planted_sites, planted_stems),
            (),
        )
        rem9 = leftover_extra_remaining_after_011(planted_sites, planted_stems)
        self.assertEqual(rem9, (planted_sites[0], planted_sites[1]))
        self.assertEqual(
            leftover_extra_remaining_after_011_with_005(planted_sites, planted_stems),
            (planted_sites[1],),
        )
        self.assertNotIn(planted_sites[1], rem10)
        self.assertNotIn(planted_sites[2], rem10)
        self.assertNotIn(planted_sites[6], rem10)
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_IS_NOT_REMAINING_AFTER_005)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when K=2."""
        provider = MockProvider()
        self.assertTrue(i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(2))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(0))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(1))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(3))
        self.assertFalse(i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(21))
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 2),)
        planted_stems = ("000",) * 3
        self.assertEqual(
            leftover_extra_remaining_after_005_with_000(planted, planted_stems),
            planted,
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(len(planted))
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000,
            HYPOTHESIS_K == STANDING_K,
        )
        self.assertEqual(STANDING_N_SHARE_005 + STANDING_N_REMAINING10, STANDING_N_REMAINING9)
        self.assertEqual(2 + 21, 23)
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT, STANDING_N_REMAINING10)
        self.assertEqual(2 + 19, 21)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle234_000_site_agreement_and_tie_minus_700_530_280_087_011_005_can_fail(self):
        """Matching sites must equal cycle 234's Ia2[174]/Ia10[141]; unique-max stays unlocked."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle234_000_sites(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE234_000_SITES)
        self.assertEqual(STANDING_MATCHING_SITES, STANDING_CYCLE234_000_SITES)
        planted = STANDING_MATCHING_SITES[:-1]
        self.assertFalse(matching_equals_cycle234_000_sites(planted))
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(len(planted))
        )
        swapped = CYCLE250_MATCHING_SITES
        self.assertFalse(matching_equals_cycle234_000_sites(swapped))
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(len(swapped))
        )
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE250_MATCHING_SITES)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE235_MATCHING_SITES)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertTrue(STANDING_UNIQUE_MAX_REMAINING_AFTER_005_IS_NOT_THIS_CYCLE)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_TIED_STEMS, STANDING_TIED_STEMS)
        self.assertEqual(
            tuple(
                stem
                for stem in CYCLE234_TIED_STEMS
                if stem not in ("700", "530", "280", "087", "011", "005")
            ),
            STANDING_TIED_STEMS_MINUS_700_530_280_087_011_005,
        )
        self.assertEqual(
            len(STANDING_TIED_STEMS_MINUS_700_530_280_087_011_005),
            STANDING_N_TIED_MINUS_700_530_280_087_011_005,
        )
        self.assertEqual(STANDING_N_TIED_MINUS_700_530_280_087_011_005, 1)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertEqual(STANDING_OTHER_TIED_STEMS, ())
        self.assertTrue(STANDING_I_ONLY_OF_090_076_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_005_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE250)
        self.assertFalse(STANDING_SAME_AS_CYCLE250)
        self.assertFalse(STANDING_SAME_AS_CYCLE251)
        self.assertFalse(STANDING_SAME_AS_CYCLE252)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter005Fwd000Scoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-005 forward-000 lock. Mock only."""

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
        self.share_280 = leftover_extra_remaining_after_530_with_280(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining7 = leftover_extra_remaining_after_280(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_087 = leftover_extra_remaining_after_280_with_087(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining8 = leftover_extra_remaining_after_087(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_011 = leftover_extra_remaining_after_087_with_011(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining9 = leftover_extra_remaining_after_011(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining9_stems = leftover_extra_remaining_after_011_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_005 = leftover_extra_remaining_after_011_with_005(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining10 = leftover_extra_remaining_after_005(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining10_stems = leftover_extra_remaining_after_005_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.matching = leftover_extra_remaining_after_005_with_000(
            self.leftover_sites,
            self.next_stems,
        )
        self.without = leftover_extra_remaining_after_005_without_000(
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
        self.n_share_087 = len(self.share_087)
        self.n_remaining8 = len(self.remaining8)
        self.n_share_011 = len(self.share_011)
        self.n_remaining9 = len(self.remaining9)
        self.n_share_005 = len(self.share_005)
        self.n_remaining10 = len(self.remaining10)
        self.g, self.tiebreak_k, self.unique = select_remaining_after_001_g(
            self.remaining4_stems
        )
        self.k = len(self.matching)
        self.n_without = len(self.without)
        self.tied = tuple(
            stem for stem, count, _sites, _grams in self.frequency if count == 2
        )
        self.tied_minus_700_530_280_087_011_005 = tuple(
            stem
            for stem in self.tied
            if stem not in ("700", "530", "280", "087", "011", "005")
        )
        self.equals_cycle234_000 = matching_equals_cycle234_000_sites(self.matching)
        self.claim_holds = i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(
            self.k,
        )

    def test_tokens_and_nested_leftover_extra_through_005_not_retuned(self):
        """2-gram and leftover extra 56/55/1 through remaining-after-011 23/2/005 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "000"))
        self.assertEqual(GRAM3_NESTED_005, ("090", "076", "005"))
        self.assertEqual(GRAM3_NESTED_005, CYCLE251_GRAM3)
        self.assertEqual(GRAM3_NESTED_005, CYCLE250_GRAM3)
        self.assertNotEqual(GRAM3_FORWARD, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3_FORWARD, CYCLE219_LEAK_4GRAM[:3])
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
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_252 = self.survey["i_090_076_005_forward_4grams_i_only"]
        self.assertEqual(prior_252["cycle"], 252)
        self.assertEqual(prior_252["N_i_only"], 2)
        self.assertEqual(prior_252["N_not_i_only"], 0)
        self.assertTrue(prior_252["i_090_076_005_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE252_CLAIM)
        self.assertEqual(CYCLE252_N_I_ONLY, 2)
        self.assertEqual(CYCLE252_N_NOT_I_ONLY, 0)
        prior_251 = self.survey["i_3gram_090_076_005_i_only"]
        self.assertEqual(prior_251["cycle"], 251)
        self.assertEqual(prior_251["N_I"], 2)
        self.assertEqual(prior_251["N_off_I"], 0)
        self.assertEqual(prior_251["N_extra"], 0)
        self.assertTrue(prior_251["i_3gram_090_076_005_i_only"])
        self.assertTrue(CYCLE251_CLAIM)
        self.assertEqual(CYCLE251_N_I, 2)
        self.assertEqual(CYCLE251_N_OFF_I, 0)
        self.assertEqual(CYCLE251_N_EXTRA, 0)
        prior_250 = self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]
        self.assertEqual(prior_250["cycle"], 250)
        self.assertEqual(prior_250["G"], "005")
        self.assertEqual(prior_250["K"], 2)
        self.assertEqual(prior_250["N_remaining9"], 23)
        self.assertEqual(prior_250["N_without"], 21)
        self.assertTrue(prior_250["i_leftover_extra_090_076_remaining_after_011_exactly_2_share_005"])
        self.assertTrue(CYCLE250_CLAIM)
        self.assertEqual(CYCLE250_G, "005")
        self.assertEqual(CYCLE250_K, 2)
        self.assertEqual(CYCLE250_N_REMAINING9, 23)
        self.assertEqual(CYCLE250_N_WITHOUT, 21)
        prior_249 = self.survey["i_090_076_011_forward_4grams_i_only"]
        self.assertEqual(prior_249["cycle"], 249)
        self.assertEqual(prior_249["N_i_only"], 4)
        self.assertEqual(prior_249["N_not_i_only"], 0)
        self.assertTrue(prior_249["i_090_076_011_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE249_CLAIM)
        self.assertEqual(CYCLE249_N_I_ONLY, 4)
        self.assertEqual(CYCLE249_N_NOT_I_ONLY, 0)
        prior_234 = self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]
        self.assertEqual(prior_234["cycle"], 234)
        self.assertEqual(prior_234["N_remaining4"], 33)
        self.assertEqual(prior_234["N_tied_at_K"], 7)
        self.assertFalse(prior_234["G_uniquely_most_frequent"])
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_219 = self.survey["i_090_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_219["cycle"], 219)
        self.assertFalse(prior_219["i_090_076_070_forward_4grams_i_only"])
        self.assertEqual(prior_219["N_i_only"], 7)
        self.assertEqual(prior_219["N_not_i_only"], 1)
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_UNIQUE_MAX_REMAINING_AFTER_005_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_090_076_070_000_IS_NOT_REMAINING_AFTER_005)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_of_21_and_hypothesis_k_2_holds(self):
        """N_remaining10=21, 7-way-tie-minus-700-530-280-087-011-005 stays, K=2 share 000. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(self.n_share_070, STANDING_N_SHARE_070)
        self.assertEqual(self.share_070, CYCLE226_MATCHING_SITES)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(self.n_remaining, self.n_with_next - self.n_share_070)
        self.assertEqual(self.remaining, CYCLE227_REMAINING_SITES)
        self.assertEqual(self.n_share_071, STANDING_N_SHARE_071)
        self.assertEqual(self.share_071, CYCLE227_MATCHING_SITES)
        self.assertEqual(self.n_remaining2, STANDING_N_REMAINING2)
        self.assertEqual(self.remaining2, CYCLE228_REMAINING2_SITES)
        self.assertEqual(self.n_share_013, STANDING_N_SHARE_013)
        self.assertEqual(self.share_013, CYCLE228_MATCHING_SITES)
        self.assertEqual(self.n_remaining3, STANDING_N_REMAINING3)
        self.assertEqual(self.n_share_001, STANDING_N_SHARE_001)
        self.assertEqual(self.share_001, CYCLE231_MATCHING_SITES)
        self.assertEqual(self.n_remaining4, STANDING_N_REMAINING4)
        self.assertEqual(self.remaining4, CYCLE234_REMAINING4_SITES)
        self.assertEqual(self.n_share_700, STANDING_N_SHARE_700)
        self.assertEqual(self.share_700, CYCLE235_MATCHING_SITES)
        self.assertEqual(self.n_remaining5, STANDING_N_REMAINING5)
        self.assertEqual(self.n_share_530, STANDING_N_SHARE_530)
        self.assertEqual(self.share_530, CYCLE238_MATCHING_SITES)
        self.assertEqual(self.n_remaining6, STANDING_N_REMAINING6)
        self.assertEqual(self.n_share_280, STANDING_N_SHARE_280)
        self.assertEqual(self.share_280, CYCLE241_MATCHING_SITES)
        self.assertEqual(self.n_remaining7, STANDING_N_REMAINING7)
        self.assertEqual(self.n_share_087, STANDING_N_SHARE_087)
        self.assertEqual(self.share_087, CYCLE244_MATCHING_SITES)
        self.assertEqual(self.n_remaining8, STANDING_N_REMAINING8)
        self.assertEqual(self.n_remaining8, CYCLE247_N_REMAINING8)
        self.assertEqual(self.remaining8, CYCLE247_REMAINING8_SITES)
        self.assertEqual(self.n_share_011, STANDING_N_SHARE_011)
        self.assertEqual(self.share_011, CYCLE247_MATCHING_SITES)
        self.assertEqual(self.n_remaining9, STANDING_N_REMAINING9)
        self.assertEqual(STANDING_N_REMAINING9, 23)
        self.assertEqual(self.n_remaining9, CYCLE250_N_REMAINING9)
        self.assertEqual(self.n_remaining9, CYCLE247_N_REMAINING8 - self.n_share_011)
        self.assertEqual(self.remaining9, STANDING_REMAINING9_SITES)
        self.assertEqual(self.n_share_005, STANDING_N_SHARE_005)
        self.assertEqual(self.share_005, CYCLE250_MATCHING_SITES)
        self.assertEqual(self.share_005, CYCLE251_I_SITES)
        if self.share_005 != CYCLE250_MATCHING_SITES:
            self.fail("leftover extra remaining-after-011 2 share 005 drifted from cycle-250 pair")
        self.assertEqual(self.n_remaining10, STANDING_N_REMAINING10)
        self.assertEqual(STANDING_N_REMAINING10, 21)
        self.assertEqual(self.n_remaining10, CYCLE250_N_WITHOUT)
        self.assertEqual(self.n_remaining10, self.n_remaining9 - self.n_share_005)
        self.assertEqual(23 - 2, 21)
        if self.n_remaining10 != 21:
            self.fail("measured N_remaining10 drifted from 21")
        if self.n_remaining10 != self.n_remaining9 - self.n_share_005:
            self.fail("leftover extra remaining-after-005 filter disagrees with nested 23−2")
        self.assertTrue(
            leftover_extra_remaining_after_005_nested_counts_hold(
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
                self.n_share_087,
                self.n_remaining8,
                self.n_share_011,
                self.n_remaining9,
                self.n_share_005,
                self.n_remaining10,
            )
        )
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
            or self.n_remaining6 != 29
            or self.n_share_280 != 2
            or self.n_remaining7 != 27
            or self.n_share_087 != 2
            or self.n_remaining8 != 25
            or self.n_share_011 != 2
            or self.n_remaining9 != 23
            or self.n_share_005 != 2
        ):
            self.fail(
                "nested leftover extra 56/55/1 / 8 share 070 / remaining 47/6/071 / "
                "remaining-after-071 41/5/013 / remaining-after-013 36/3/001 / "
                "remaining-after-001 33/2/700 / remaining-after-700 31/2/530 / "
                "remaining-after-530 29/2/280 / remaining-after-280 27/2/087 / "
                "remaining-after-087 25/2/011 / remaining-after-011 23/2/005 drifted"
            )
        self.assertEqual(self.remaining10, STANDING_REMAINING10_SITES)
        self.assertEqual(len(self.remaining10), len(self.remaining10_stems))
        self.assertEqual(
            self.remaining10,
            leftover_extra_remaining_after_011_without_005(
                self.leftover_sites,
                self.next_stems,
            ),
        )
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.remaining10)
        self.assertIn(STANDING_IA2_174, self.remaining10)
        self.assertEqual(STANDING_IA2_174_NEXT_STEM, "000")
        self.assertNotIn(STANDING_IA2_159, self.remaining10)
        self.assertEqual(STANDING_IA2_159_NEXT_STEM, "700")
        self.assertNotIn(STANDING_IA14_140, self.remaining10)
        self.assertIn(STANDING_IA14_140, STANDING_LEFTOVER_SITES)
        self.assertIn(STANDING_IA14_140, self.share_070)
        self.assertEqual(STANDING_IA14_140_NEXT_STEM, "070")
        self.assertTrue(STANDING_090_076_070_000_IS_NOT_REMAINING_AFTER_005)
        for site in CYCLE251_I_SITES:
            self.assertNotIn(site, self.remaining10)
            self.assertNotIn(site, self.matching)
        for site in self.share_070:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_071:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_013:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_001:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_700:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_530:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_280:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_087:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_011:
            self.assertNotIn(site, self.remaining10)
        for site in self.share_005:
            self.assertNotIn(site, self.remaining10)
        self.assertEqual(self.n_distinct_remaining4, STANDING_N_DISTINCT_REMAINING4)
        self.assertEqual(self.g, "700")
        self.assertEqual(self.tiebreak_k, 2)
        self.assertFalse(self.unique)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertEqual(self.tied, STANDING_TIED_STEMS)
        self.assertEqual(self.tied, CYCLE234_TIED_STEMS)
        self.assertEqual(len(self.tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 7)
        self.assertEqual(
            self.tied_minus_700_530_280_087_011_005,
            STANDING_TIED_STEMS_MINUS_700_530_280_087_011_005,
        )
        self.assertEqual(
            len(self.tied_minus_700_530_280_087_011_005),
            STANDING_N_TIED_MINUS_700_530_280_087_011_005,
        )
        self.assertEqual(STANDING_N_TIED_MINUS_700_530_280_087_011_005, 1)
        if self.tied_minus_700_530_280_087_011_005 != STANDING_TIED_STEMS_MINUS_700_530_280_087_011_005:
            self.fail("nested cycle 234 7-way-tie-minus-700-530-280-087-011-005 drifted")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, HYPOTHESIS_K)
        self.assertEqual(STANDING_K, 2)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT)
        self.assertEqual(STANDING_N_WITHOUT, 19)
        self.assertEqual(self.k + self.n_without, self.n_remaining10)
        self.assertEqual(2 + 19, 21)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000(self.k)
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertTrue(self.equals_cycle234_000)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE234_000_SITES)
        if len(self.matching) != 2 or not self.equals_cycle234_000:
            self.fail("leftover extra remaining-after-005 000 set drifted from cycle-234 pair")
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE250)
        self.assertFalse(STANDING_SAME_AS_CYCLE251)
        self.assertFalse(STANDING_SAME_AS_CYCLE252)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE250)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_UNIQUE_MAX_REMAINING_AFTER_005_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertTrue(CYCLE226_CLAIM)
        self.assertTrue(CYCLE227_CLAIM)
        self.assertTrue(CYCLE228_CLAIM)
        self.assertTrue(CYCLE231_CLAIM)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertTrue(CYCLE235_CLAIM)
        self.assertTrue(CYCLE238_CLAIM)
        self.assertTrue(CYCLE241_CLAIM)
        self.assertTrue(CYCLE244_CLAIM)
        self.assertTrue(CYCLE247_CLAIM)
        self.assertTrue(CYCLE250_CLAIM)
        self.assertTrue(CYCLE251_CLAIM)
        self.assertTrue(CYCLE252_CLAIM)
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_remaining_after_005_sites_share_000(self):
        """Two leftover extra remaining-after-005 sites are 090 076 000."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia2", 174), None),
            ((SIDE_IA, "Ia10", 141), ("090", "076", "000", "076")),
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
            self.assertEqual(stems[index + STANDING_N2], "000")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "000")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            if want_nxt is not None:
                self.assertEqual(nxt[:3], GRAM3_FORWARD)
                self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_REMAINING10_SITES)
            self.assertIn(site, STANDING_REMAINING9_SITES)
            self.assertIn(site, CYCLE250_REMAINING9_SITES)
            self.assertIn(site, CYCLE247_REMAINING8_SITES)
            self.assertIn(site, CYCLE234_REMAINING4_SITES)
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
            self.assertNotIn(site, CYCLE244_MATCHING_SITES)
            self.assertNotIn(site, CYCLE245_I_SITES)
            self.assertNotIn(site, CYCLE247_MATCHING_SITES)
            self.assertNotIn(site, CYCLE248_I_SITES)
            self.assertNotIn(site, CYCLE248_EXTRA_I_SITES)
            self.assertNotIn(site, CYCLE250_MATCHING_SITES)
            self.assertNotIn(site, CYCLE251_I_SITES)
            self.assertNotIn(site, CYCLE207_I_SITES)
            self.assertNotIn(site, CYCLE195_I_SITES)
        self.assertEqual(self.matching, STANDING_CYCLE234_000_SITES)
        self.assertTrue(matching_equals_cycle234_000_sites(self.matching))
        self.assertIn(STANDING_IA2_174, self.matching)
        self.assertNotIn(STANDING_IA2_159, self.matching)
        self.assertNotIn(STANDING_IA14_140, self.matching)
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.matching)
        self.assertIn(STANDING_IA2_174, self.remaining10)
        self.assertNotIn(STANDING_IA2_159, self.remaining10)
        self.assertNotIn(STANDING_IA14_140, self.remaining10)
        self.assertEqual(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_IA2_174)],
            "000",
        )
        self.assertIsNone(
            self.next_4grams[STANDING_LEFTOVER_SITES.index(STANDING_IA2_174)]
        )
        self.assertTrue(STANDING_IA2_174_HAS_NO_NEXT_4GRAM)
        self.assertEqual(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_IA14_140)],
            "070",
        )
        self.assertEqual(
            self.next_4grams[STANDING_LEFTOVER_SITES.index(STANDING_IA14_140)],
            STANDING_IA14_140_NEXT_4GRAM,
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
            self.assertNotEqual(nxt, "000")
            self.assertNotEqual(nxt, "005")
            self.assertNotEqual(nxt, "011")
            self.assertNotEqual(nxt, "087")
            self.assertNotEqual(nxt, "280")
            self.assertNotEqual(nxt, "530")
            self.assertNotEqual(nxt, "700")
            self.assertNotEqual(nxt, "001")
            self.assertNotEqual(nxt, "013")
            self.assertNotEqual(nxt, "071")
            self.assertNotEqual(nxt, "070")
            self.assertIn(site, STANDING_REMAINING10_SITES)
        for site in self.share_005:
            self.assertNotIn(site, self.remaining10)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE250_MATCHING_SITES)
        self.assertEqual(STANDING_OTHER_TIED_STEMS, ())
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining10)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining10)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[9], "Ia10")
        self.assertTrue(STANDING_I_ONLY_OF_090_076_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_005_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_UNIQUE_MAX_REMAINING_AFTER_005_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_090_076_070_000_IS_NOT_REMAINING_AFTER_005)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_252_251_250_249_234_223_219_and_171_still_compute(self):
        """Cycle 252 2/2 hapax, 251 2/0 extra I=0, 250 K=2/G=005 N_remaining9=23, 249 4/4 hapax, 234 7-way tie, 223 69/3, 219 7/8 T 000, 171 43/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_252 = TestMamariI090076005Forward4gramsIOnlyScoreboard()
        prior_252.setUp()
        prior_252.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_252.test_survey_matches_computed_lock()
        self.assertEqual(prior_252.n_i_only, 2)
        self.assertEqual(prior_252.n_not_i_only, 0)
        self.assertTrue(prior_252.claim_holds)
        self.assertTrue(CYCLE252_CLAIM)
        if prior_252.n_i_only != 2 or prior_252.n_not_i_only != 0:
            self.fail("nested cycle 252 090 076 005 forward 4-grams 2/2 hapax drifted")
        prior_251 = TestMamariI3gram090076005IOnlyScoreboard()
        prior_251.setUp()
        prior_251.test_i_hits_are_two_on_ia_and_equal_leftover_extra_005()
        prior_251.test_3gram_is_zero_off_i_and_i_only()
        prior_251.test_survey_matches_computed_lock()
        self.assertEqual(prior_251.i_hits, CYCLE251_N_I)
        self.assertEqual(prior_251.i_hits, 2)
        self.assertEqual(prior_251.off_i_hits, CYCLE251_N_OFF_I)
        self.assertEqual(prior_251.off_i_hits, 0)
        self.assertEqual(len(prior_251.extra), CYCLE251_N_EXTRA)
        self.assertEqual(len(prior_251.extra), 0)
        self.assertEqual(prior_251.extra, CYCLE251_EXTRA_I_SITES)
        self.assertEqual(prior_251.i_sites, CYCLE251_I_SITES)
        self.assertTrue(prior_251.claim_holds)
        self.assertTrue(CYCLE251_CLAIM)
        if prior_251.i_hits != 2 or prior_251.off_i_hits != 0 or prior_251.extra:
            self.fail("nested cycle 251 090 076 005 I-only 2/0 extra I=0 drifted")
        prior_250 = TestMamariILeftoverExtra090076RemainingAfter011Fwd005Scoreboard()
        prior_250.setUp()
        prior_250.test_counts_2_of_23_and_hypothesis_k_2_holds()
        prior_250.test_survey_matches_computed_lock()
        self.assertEqual(prior_250.n_leftover, 56)
        self.assertEqual(prior_250.n_remaining9, 23)
        self.assertEqual(prior_250.k, 2)
        self.assertEqual(CYCLE250_G, "005")
        self.assertEqual(prior_250.matching, CYCLE250_MATCHING_SITES)
        self.assertEqual(self.share_005, prior_250.matching)
        self.assertTrue(prior_250.claim_holds)
        self.assertTrue(CYCLE250_CLAIM)
        if (
            prior_250.n_leftover != 56
            or prior_250.n_remaining9 != 23
            or prior_250.k != 2
        ):
            self.fail(
                "nested cycle 250 leftover extra remaining-after-011 exactly 2 share 005 drifted"
            )
        prior_249 = TestMamariI090076011Forward4gramsIOnlyScoreboard()
        prior_249.setUp()
        prior_249.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_249.test_survey_matches_computed_lock()
        self.assertEqual(prior_249.n_i_only, 4)
        self.assertEqual(prior_249.n_not_i_only, 0)
        self.assertTrue(prior_249.claim_holds)
        self.assertTrue(CYCLE249_CLAIM)
        if prior_249.n_i_only != 4 or prior_249.n_not_i_only != 0:
            self.fail("nested cycle 249 090 076 011 forward 4-grams 4/4 hapax drifted")
        prior_234 = TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard()
        prior_234.setUp()
        prior_234.test_counts_33_remaining4_g_700_k_2_and_hypothesis_loses()
        prior_234.test_survey_matches_computed_lock()
        self.assertEqual(prior_234.n_leftover, 56)
        self.assertEqual(prior_234.n_remaining4, 33)
        self.assertEqual(prior_234.n_distinct_remaining4, 26)
        self.assertEqual(prior_234.k, 2)
        self.assertFalse(prior_234.unique)
        self.assertEqual(prior_234.matching, CYCLE234_MATCHING_SITES)
        self.assertFalse(prior_234.claim_holds)
        self.assertFalse(CYCLE234_CLAIM)
        if (
            prior_234.n_leftover != 56
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
            tuple(
                stem
                for stem in tied
                if stem not in ("700", "530", "280", "087", "011", "005")
            ),
            STANDING_TIED_STEMS_MINUS_700_530_280_087_011_005,
        )
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, STANDING_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, STANDING_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertFalse(prior_223.claim_holds)
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
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertNotEqual(CYCLE219_LEAK_4GRAM, GRAM3_FORWARD + ("076",))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-253 leftover extra remaining-after-005 fwd000 lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]
        self.assertEqual(lock["cycle"], 253)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(tuple(lock["forward_3gram"]), ("090", "076", "000"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(
            tuple(lock["locked_forward_stems_after_011"]),
            LOCKED_FORWARD_STEMS_AFTER_011,
        )
        self.assertEqual(
            tuple(lock["locked_forward_stems_after_005"]),
            LOCKED_FORWARD_STEMS_AFTER_005,
        )
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(lock["N_share_070"], 8)
        self.assertEqual(lock["N_remaining"], 47)
        self.assertEqual(lock["N_share_071"], 6)
        self.assertEqual(lock["N_remaining2"], 41)
        self.assertEqual(lock["N_share_013"], 5)
        self.assertEqual(lock["N_remaining3"], 36)
        self.assertEqual(lock["N_share_001"], 3)
        self.assertEqual(lock["ia2_174_next_stem"], "000")
        self.assertEqual(lock["N_remaining4"], 33)
        self.assertEqual(lock["N_distinct_remaining4"], 26)
        self.assertEqual(lock["N_share_700"], 2)
        self.assertEqual(lock["N_remaining5"], 31)
        self.assertEqual(lock["N_share_530"], 2)
        self.assertEqual(lock["N_remaining6"], 29)
        self.assertEqual(lock["N_share_280"], 2)
        self.assertEqual(lock["N_remaining7"], 27)
        self.assertEqual(lock["N_share_087"], 2)
        self.assertEqual(lock["N_remaining8"], 25)
        self.assertEqual(lock["N_share_011"], 2)
        self.assertEqual(lock["N_remaining9"], STANDING_N_REMAINING9)
        self.assertEqual(lock["N_remaining9"], 23)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_011_sites"]),
            STANDING_REMAINING9_SITES,
        )
        self.assertEqual(lock["N_share_005"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_005_sites"]),
            CYCLE250_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining10"], STANDING_N_REMAINING10)
        self.assertEqual(lock["N_remaining10"], 21)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_005_sites"]),
            STANDING_REMAINING10_SITES,
        )
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "000")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], 7)
        self.assertEqual(
            tuple(lock["tied_stems_minus_700_530_280_087_011_005"]),
            STANDING_TIED_STEMS_MINUS_700_530_280_087_011_005,
        )
        self.assertEqual(lock["N_tied_minus_700_530_280_087_011_005"], 1)
        self.assertEqual(lock["N_without"], STANDING_N_WITHOUT)
        self.assertEqual(lock["N_without"], 19)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_005_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle234_000_sites"])
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_005_local_4grams"],
            matching_leftover_extra_remaining_after_005_fwd000_local_4gram_rows(),
        )
        self.assertTrue(lock["ia2_174_has_no_next_4gram"])
        self.assertEqual(lock["cycle252_N_i_only"], 2)
        self.assertEqual(lock["cycle252_N_not_i_only"], 0)
        self.assertEqual(lock["cycle251_N_I"], 2)
        self.assertEqual(lock["cycle251_N_off_I"], 0)
        self.assertEqual(lock["cycle251_N_extra"], 0)
        self.assertEqual(lock["cycle250_G"], "005")
        self.assertEqual(lock["cycle250_K"], 2)
        self.assertEqual(lock["cycle250_N_remaining9"], 23)
        self.assertEqual(lock["cycle249_N_i_only"], 4)
        self.assertEqual(lock["cycle249_N_not_i_only"], 0)
        self.assertEqual(lock["cycle234_N_remaining4"], 33)
        self.assertEqual(lock["cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["cycle234_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle223_N_I"], 69)
        self.assertEqual(lock["cycle223_N_off_I"], 3)
        self.assertEqual(lock["cycle219_N_i_only"], 7)
        self.assertEqual(lock["cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["cycle171_N_I"], 43)
        self.assertEqual(lock["cycle171_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle226"])
        self.assertFalse(lock["same_as_cycle234"])
        self.assertFalse(lock["same_as_cycle250"])
        self.assertFalse(lock["same_as_cycle251"])
        self.assertFalse(lock["same_as_cycle252"])
        self.assertTrue(lock["same_claim_shape_as_cycle226"])
        self.assertTrue(lock["same_claim_shape_as_cycle235"])
        self.assertTrue(lock["same_claim_shape_as_cycle250"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_090_076_000_is_not_this_cycle"])
        self.assertTrue(lock["previous_4grams_of_090_076_005_are_not_this_cycle"])
        self.assertTrue(lock["unique_max_remaining_after_005_is_not_this_cycle"])
        self.assertTrue(lock["other_tied_stems_not_locked"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["090_076_070_000_is_not_remaining_after_005"])
        self.assertEqual(lock["ia2_159_next_stem"], "700")
        self.assertEqual(lock["ia14_140_next_stem"], "070")
        self.assertEqual(
            tuple(lock["ia14_140_next_4gram"]),
            STANDING_IA14_140_NEXT_4GRAM,
        )
        self.assertTrue(lock["cycle224_no_next_4gram_is_not_no_next_token"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_090_076_005_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_005_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_011_fwd005_unchanged"])
        self.assertTrue(lock["standing_i_090_076_011_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_090_076_005_forward_4grams_i_only"]["cycle"], 252)
        self.assertTrue(
            self.survey["i_090_076_005_forward_4grams_i_only"][
                "i_090_076_005_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_005_i_only"]["cycle"], 251)
        self.assertTrue(self.survey["i_3gram_090_076_005_i_only"]["i_3gram_090_076_005_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_005_i_only"]["N_extra"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]["cycle"],
            250,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"][
                "i_leftover_extra_090_076_remaining_after_011_exactly_2_share_005"
            ]
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_090_076_070_forward_4grams_i_only"]["cycle"], 219)
        self.assertFalse(
            self.survey["i_090_076_070_forward_4grams_i_only"][
                "i_090_076_070_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
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


class TestMamariILeftoverExtra090076RemainingAfter005Fwd000ImageSnapshot(
    unittest.TestCase
):
    """Cycle 253 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
