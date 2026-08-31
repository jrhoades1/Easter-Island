"""I's leftover n=4 remaining remaining-after-600 previous-4-grams I-only lock.

Cycle 309 text-search lock. Uses already-vendored A–V and the
cycle-308 leftover n=4 remaining remaining-after-021
remaining-after-600 I sites of 2-gram 090 076 (the 6 leftover
n=4 remaining sites whose previous token is neither 021 nor
600). Does not retune those leftover n=4 remaining remaining-
after-600 unique-max (cycle 308 lost: 6 hapax, G=999 K=1,
N_distinct=6), leftover n=4 remaining remaining-after-021
exactly 2 share previous 600 (cycle 307), leftover n=4
remaining remaining-after-021 unique previous stem (cycle
306), leftover extra remaining-after-009 previous 4-grams
(cycle 285), leftover extra remaining-after-000 forward
4-grams (cycle 257), leftover extra remaining-after-000
extra-I 4-grams (cycle 259), leftover extra remaining-after-
600 unique previous stem (cycle 270 lost), leftover n=4
remaining remaining-after-011 forward 4-grams (cycle 299),
leftover extra remaining-after-000 extra I (cycles 258/259),
or leftover n=4 remaining remaining-after-087 next 057
(cycle 295, Ia8[114]/Ia9[28]). Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new
agents. Not a meaning dictionary.

Same claim-shape as cycle 299 leftover n=4 remaining
remaining-after-011 forward 4-grams all I-only hapax 1/0 x2
after cycle 298 unique-max lost, cycle 285 leftover extra
remaining-after-009 previous 4-grams all I-only hapax 1/0
x27 after cycle 284 unique-max lost, and cycle 257 leftover
extra remaining-after-000 forward 4-grams all I-only hapax
1/0 x19 after cycle 256 unique-max lost. Cycle 308 leftover
n=4 remaining remaining-after-600 unique-max lost N=6 K=1
6-way tie G=999; do not lock "exactly 1 share previous 999"
(tautology on a hapax pile). Nested-check leftover n=4
remaining remaining-after-600 unique-max false,
N_remaining_after_600==6, K==1, N_distinct==6, G=999 (do
not retune cycle 308). Nested-check each remaining-after-600
site has a previous token and a 4th token (prev-of-prev).
If a site is line-initial after the previous stem (3-gram
W 090 076 with no 4th token X), lock that as no previous
4-gram rather than inventing one; that site then does not
count as a 4-gram hapax and the I-only-4-gram claim loses
because the 4-gram set is incomplete relative to N=6.
Measure; do not assume all six have a 4th token. Cycle 308
N_line_initial=0 so all 6 should have a previous token.
Do not peel a specific remaining-after-600 stem this cycle.
Do not re-lock leftover extra remaining-after-009 previous
4-grams, leftover extra remaining-after-000 fwd 4-grams,
leftover extra remaining-after-000 extra-I 4-grams, leftover
extra remaining-after-600 unique previous stem, leftover
n=4 remaining remaining-after-011 fwd 4-grams, leftover n=4
remaining remaining-after-021 unique previous stem, leftover
n=4 remaining remaining-after-021 previous-600, leftover
extra remaining-after-000 extra I, or leftover n=4 remaining
remaining-after-087 next 057. Off-I T sites are this cycle
only as off-I of a remaining-after-600 previous 4-gram if
they match.

Locks exact consecutive hits of each continuing leftover
n=4 remaining remaining-after-600 previous 4-gram on tablet
I and on every other vendored tablet A–H and J–V. The six
4-grams: 570 591 090 076 at Ia2[119], 090 076 090 076 at
Ia4[86], 079 090 090 076 at Ia5[143], 607 000 090 076 at
Ia8[114], 244 999 090 076 at Ia9[28], 700 008 090 076 at
Ia12[83]. Cycle 308 reported G site Ia9[28]
244 999 090 076. Do not assume hapax; count each from
fixtures. Hypothesis: all continuing remaining-after-600
previous 4-grams are I-only. Measured: each N_I=1 at the
previous-4 start two tokens before the cycle-308 remaining-
after-600 site; all N_off_I=0; no remaining-after-600 site
is line-initial (all 6 have a 4th token). Claim that can
lose:
i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only.
True iff N_remaining_after_600==6, the six sites still
compute as remaining-after-600 leftover n=4 remaining I
090 076, every remaining-after-600 site has a previous
4-gram, and every such 4-gram has N_I ≥ 1 and N_off_I = 0
(hapax 1/0 expected given K=1). This can lose if any leaks
off I (same shape as cycle 219 090 076 070 000 1/1 on T),
if N_remaining_after_600 != 6, if a site is line-initial
so the 4-gram set is incomplete relative to N=6, or if the
six sites no longer compute as remaining-after-600. The
claim is true. Nested overlap: remaining-after-600 overlaps
leftover extra remaining-after-000 extra I (cycles 258/259)
and leftover n=4 remaining remaining-after-087 next 057
(cycle 295) at Ia8[114]/Ia9[28]. Record, do not fail the
I-only claim on it. Nested leftover n=4 remaining 13 / 4 /
9 / 3 / 6 / 2 / 4 / 2 / 2, nested remaining-after-021 N=8
unique-max true G=600 K=2 N_distinct=7, nested remaining-
after-600 unique-max false G=999 K=1 N_distinct=6, cycle
308 unique-max lose, cycle 307 K_600=2, cycle 303 K_021=5,
cycle 288 unique-max G=020 K=4 share-one lost, cycle 224
13/56, and cycle 223 69/3 stay. Do not assume hapax;
measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES as CYCLE223_I_SITES,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_CLAIM,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE217_CLAIM,
    STANDING_N_I_EACH as CYCLE217_N_I_EACH,
    STANDING_N_OFF_I_EACH as CYCLE217_N_OFF_I_EACH,
    TestMamariILeftover076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_BY_X as CYCLE259_EXTRA_I_BY_X,
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_SEQUENCES as CYCLE259_SEQUENCES,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE257_CLAIM,
    STANDING_N_I_ONLY as CYCLE257_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE257_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE257_SEQUENCES,
    TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_prev4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY as CYCLE285_CLAIM,
    STANDING_N_I_ONLY as CYCLE285_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE285_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE285_SEQUENCES,
    TestMamariILeftoverExtra090076RemainingAfter009Prev4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    STANDING_G as CYCLE270_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE270_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED,
    TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_previous_021_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021 as CYCLE303_CLAIM,
    STANDING_K_021 as CYCLE303_K_021,
    STANDING_MATCHING_SITES as CYCLE303_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_021 as CYCLE303_N_REMAINING_AFTER_021,
    TestMamariILeftoverN4Remaining090076Previous021Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_previous_stem_scoreboard import (
    leftover_n4_remaining_backward_3grams,
    leftover_n4_remaining_g_overlap_sites,
    leftover_n4_remaining_previous_4grams,
    leftover_n4_remaining_previous_stems,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE299_CLAIM,
    STANDING_N_I_ONLY as CYCLE299_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE299_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE299_SEQUENCES,
    TestMamariILeftoverN4Remaining090076RemainingAfter011Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_next_stem_scoreboard import (
    STANDING_K_011,
    STANDING_K_020,
    STANDING_K_057,
    STANDING_K_087,
    STANDING_N_REMAINING_AFTER_011,
    STANDING_N_REMAINING_AFTER_020,
    STANDING_N_REMAINING_AFTER_057,
    STANDING_N_REMAINING_AFTER_087,
    leftover_n4_remaining_remaining_after_011_nested_counts_hold,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_021_previous_600_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_EXACTLY_2_SHARE_PREVIOUS_600 as CYCLE307_CLAIM,
    STANDING_K_600 as CYCLE307_K_600,
    STANDING_MATCHING_SITES as CYCLE307_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_600 as CYCLE307_N_REMAINING_AFTER_600,
    leftover_n4_remaining_remaining_after_021_without_previous_600,
    TestMamariILeftoverN4Remaining090076RemainingAfter021Previous600Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS as LOCKED_PREVIOUS_STEMS_AFTER_021,
    STANDING_G as CYCLE306_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE306_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM as CYCLE306_CLAIM,
    STANDING_K as CYCLE306_K,
    STANDING_N_DISTINCT as CYCLE306_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_021 as CYCLE306_N_REMAINING,
    leftover_n4_remaining_remaining_after_021_nested_counts_hold,
    TestMamariILeftoverN4Remaining090076RemainingAfter021PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_087_forward_057_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057 as CYCLE295_CLAIM,
    STANDING_K_057 as CYCLE295_K_057,
    STANDING_MATCHING_SITES as CYCLE295_MATCHING_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter087Forward057Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_600,
    STANDING_G as CYCLE308_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE308_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE308_CLAIM,
    STANDING_K as CYCLE308_K,
    STANDING_K_021,
    STANDING_K_600,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE308_G_PREVIOUS_4GRAM,
    STANDING_MATCHING_SITES as CYCLE308_G_SITES,
    STANDING_N_DISTINCT as CYCLE308_N_DISTINCT,
    STANDING_N_INSIDE,
    STANDING_N_LINE_INITIAL as CYCLE308_N_LINE_INITIAL,
    STANDING_N_REMAINING_AFTER_021,
    STANDING_N_REMAINING_AFTER_600,
    STANDING_N_REMAINING_AFTER_600 as CYCLE308_N_REMAINING_AFTER_600,
    STANDING_NESTED_LEFTOVER_N4_REMAINING,
    STANDING_OVERLAP_CYCLE258_EXTRA_I as CYCLE308_OVERLAP_258,
    STANDING_OVERLAP_CYCLE259_EXTRA_I as CYCLE308_OVERLAP_259,
    STANDING_OVERLAP_DOES_NOT_LOSE as CYCLE308_OVERLAP_DOES_NOT_LOSE,
    STANDING_REMAINING_PREVIOUS_STEMS as CYCLE308_REMAINING_PREVIOUS_STEMS,
    STANDING_REMAINING_SITES as CYCLE308_REMAINING_SITES,
    STANDING_TIED_STEMS as CYCLE308_TIED_STEMS,
    leftover_n4_remaining_remaining_after_600,
    leftover_n4_remaining_remaining_after_600_nested_counts_hold,
    leftover_n4_remaining_remaining_after_600_previous_stems,
    leftover_n4_remaining_remaining_after_600_without_previous,
    leftover_n4_remaining_remaining_after_600_with_previous,
    select_remaining_after_600_g,
    TestMamariILeftoverN4Remaining090076RemainingAfter600PreviousStemScoreboard,
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
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_ALL_I_ONLY = True
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I = 69
STANDING_N_INSIDE_LOCK = STANDING_N_INSIDE
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_REMAINING_AFTER_600_LOCK = STANDING_N_REMAINING_AFTER_600
STANDING_REMAINING_SITES = CYCLE308_REMAINING_SITES
STANDING_REMAINING_PREVIOUS_STEMS = CYCLE308_REMAINING_PREVIOUS_STEMS
STANDING_REMAINING_PREVIOUS_4GRAMS = (
    ("570", "591", "090", "076"),
    ("090", "076", "090", "076"),
    ("079", "090", "090", "076"),
    ("607", "000", "090", "076"),
    ("244", "999", "090", "076"),
    ("700", "008", "090", "076"),
)
STANDING_SEQUENCES = STANDING_REMAINING_PREVIOUS_4GRAMS
STANDING_N_CONTINUING = 6
STANDING_N_4GRAMS = 6
STANDING_N_NO_PREVIOUS = 0
STANDING_N_LINE_INITIAL = 0
STANDING_CONTINUING_SITES = STANDING_REMAINING_SITES
STANDING_LINE_INITIAL_SITES = ()
STANDING_NO_PREVIOUS_SITES = ()
STANDING_PREVIOUS_STEMS = STANDING_REMAINING_PREVIOUS_STEMS
STANDING_ROLES = ("leftover_n4_remaining_remaining_after_600",) * STANDING_N_CONTINUING
STANDING_N_I_EACH = (1, 1, 1, 1, 1, 1)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_I_SITES = tuple(
    ((side, line, index - 2),) for side, line, index in STANDING_CONTINUING_SITES
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0, 0, 0, 0, 0, 0)
STANDING_OFF_I_SITES = ((), (), (), (), (), ())
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (STANDING_HITS_BY_TABLET_ONE_ON_I,) * STANDING_N_CONTINUING
STANDING_N_I_ONLY = 6
STANDING_N_HAPAX_I_ONLY = 6
STANDING_N_NOT_I_ONLY = 0
STANDING_N_LEAK_OFF_I = 0
STANDING_LEAKING_4GRAMS = ()
STANDING_HAPAX_EACH = (True, True, True, True, True, True)
STANDING_ALL_REMAINING_HAVE_PREVIOUS_TOKEN = True
STANDING_ALL_REMAINING_HAVE_FOURTH_TOKEN = True
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_OVERLAP_CYCLE258_EXTRA_I = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_OVERLAP_CYCLE259_EXTRA_I = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_OVERLAP_CYCLE295_NEXT_057 = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_OVERLAP_CYCLE258_EXTRA_I_057 = True
STANDING_OVERLAP_CYCLE259_EXTRA_I_057 = True
STANDING_IA2_IA4_IA5_IA12_OVERLAP_258_259_295 = False
STANDING_OVERLAP_CYCLE257_FWD4_4GRAM = ("090", "076", "090", "076")
STANDING_OVERLAP_CYCLE257_FWD4 = True
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only"
)
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_PREVIOUS_4GRAMS_ALL_I_ONLY = (
    True
)
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_PREVIOUS_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_600_prev4_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE257 = False
STANDING_SAME_AS_CYCLE258 = False
STANDING_SAME_AS_CYCLE259 = False
STANDING_SAME_AS_CYCLE270 = False
STANDING_SAME_AS_CYCLE285 = False
STANDING_SAME_AS_CYCLE288 = False
STANDING_SAME_AS_CYCLE295 = False
STANDING_SAME_AS_CYCLE299 = False
STANDING_SAME_AS_CYCLE303 = False
STANDING_SAME_AS_CYCLE306 = False
STANDING_SAME_AS_CYCLE307 = False
STANDING_SAME_AS_CYCLE308 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE217 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE257 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE285 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE299 = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_DO_NOT_PEEL_999 = True
STANDING_DO_NOT_LOCK_EXACTLY_1_SHARE_PREVIOUS_999 = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_009_PREV4_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_FWD4_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXTRA_I_FWD4_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_600_UNIQUE_MAX_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_011_FWD4_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_PREVIOUS_600_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXTRA_I_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_087_NEXT_057_IS_NOT_THIS_CYCLE = True
STANDING_021_090_076_DOES_NOT_COUNT = True
STANDING_600_090_076_DOES_NOT_COUNT = True
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_ARE_THIS_CYCLE_ONLY_IF_MATCHING_4GRAM = True
STANDING_CYCLE308_N_REMAINING_AFTER_600 = 6
STANDING_CYCLE308_K = 1
STANDING_CYCLE308_G = "999"
STANDING_CYCLE308_UNIQUE = False
STANDING_CYCLE308_N_DISTINCT = 6
STANDING_CYCLE307_K_600 = 2
STANDING_CYCLE306_G = "600"
STANDING_CYCLE306_K = 2
STANDING_CYCLE306_N_REMAINING = 8
STANDING_CYCLE306_N_DISTINCT = 7
STANDING_CYCLE306_UNIQUE = True
STANDING_CYCLE303_K_021 = 5
STANDING_CYCLE299_N_I_ONLY = 2
STANDING_CYCLE299_N_NOT_I_ONLY = 0
STANDING_CYCLE295_K_057 = 2
STANDING_CYCLE288_G = "020"
STANDING_CYCLE288_K = 4
STANDING_CYCLE285_N_I_ONLY = 27
STANDING_CYCLE285_N_NOT_I_ONLY = 0
STANDING_CYCLE257_N_I_ONLY = 19
STANDING_CYCLE257_N_NOT_I_ONLY = 0
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3


def leftover_previous_4gram_start_site(
    remaining_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Previous 4-gram starts two tokens before the remaining-after-600 site."""
    side, line, index = remaining_site
    return (side, line, index - 2)


def leftover_n4_remaining_remaining_after_600_previous_4grams(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_previous_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per remaining-after-600 site previous 4-gram or None if line-initial after W."""
    locked_set = set(locked)
    return tuple(
        gram
        for prev, gram in zip(
            leftover_previous_stems,
            leftover_previous_4grams,
            strict=True,
        )
        if prev is not None and prev not in locked_set
    )


def leftover_n4_remaining_remaining_after_600_line_initial_sites(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_previous_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-600 sites with a previous stem and no 4th token X."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev, gram in zip(
            leftover_sites,
            leftover_previous_stems,
            leftover_previous_4grams,
            strict=True,
        )
        if prev is not None and prev not in locked_set and gram is None
    )


def leftover_n4_remaining_remaining_after_600_continuing_sites(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_previous_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-600 sites that continue to a 4th token X."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev, gram in zip(
            leftover_sites,
            leftover_previous_stems,
            leftover_previous_4grams,
            strict=True,
        )
        if prev is not None and prev not in locked_set and gram is not None
    )


def continuing_previous_4grams(
    per_site_previous_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct-preserving continuing remaining-after-600 previous 4-grams."""
    return tuple(gram for gram in per_site_previous_4grams if gram is not None)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def sequence_is_hapax_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff hapax on I (N_I=1) and N_off_I=0."""
    return n_i == 1 and n_off_i == 0


def i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    n_remaining: int,
    n_line_initial: int,
    remaining_sites: tuple[tuple[str, str, int], ...],
    expected_n: int = STANDING_N_REMAINING_AFTER_600_LOCK,
    expected_sites: tuple[tuple[str, str, int], ...] = STANDING_REMAINING_SITES,
) -> bool:
    """True iff remaining-after-600 N=6, complete 4-grams, all I-only.

    Loses if any 4-gram appears off I, if N_remaining_after_600 != 6,
    if a site is line-initial so the 4-gram set is incomplete relative
    to N=6, or if the six sites no longer compute as remaining-after-
    600 leftover n=4 remaining I 090 076. Hapax is not assumed; N_I
    may be greater than 1.
    """
    return (
        n_remaining == expected_n
        and remaining_sites == expected_sites
        and n_line_initial == 0
        and len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestILeftoverN4Remaining090076RemainingAfter600Prev4IOnlyHelpers(
    unittest.TestCase
):
    """Helpers on leftover n=4 remaining remaining-after-600 previous 4-grams."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 021 / 600 / 070 000 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("570", "591", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[4], ("244", "999", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("700", "008", "090", "076"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_CONTINUING)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_CONTINUING)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[2:], GRAM2)
            self.assertEqual(len(gram), STANDING_N4)
            self.assertNotEqual(gram[1:], ("021", "090", "076"))
            self.assertNotEqual(gram[1:], ("600", "090", "076"))
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotIn(gram, CYCLE259_SEQUENCES)
            self.assertNotIn(gram, CYCLE285_SEQUENCES)
            self.assertNotIn(gram, CYCLE299_SEQUENCES)
            if gram == STANDING_OVERLAP_CYCLE257_FWD4_4GRAM:
                self.assertIn(gram, CYCLE257_SEQUENCES)
            else:
                self.assertNotIn(gram, CYCLE257_SEQUENCES)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["570", "591", "090", "076", "570", "591", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [
            list(STANDING_SEQUENCES[0][:2])
            + ["006"]
            + list(STANDING_SEQUENCES[0][2:])
        ]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(
            ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0
        )
        self.assertEqual(
            ngram_hit_count([["021", "090", "076"]], STANDING_SEQUENCES[0]), 0
        )
        self.assertEqual(
            ngram_hit_count([["600", "090", "076"]], STANDING_SEQUENCES[0]), 0
        )
        planted = ["570", "591", "090", "076"]
        self.assertEqual(site_previous_4gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_backward_3gram(planted, 2, GRAM2), ("591", "090", "076"))
        line_initial_after_w = ["591", "090", "076"]
        self.assertEqual(site_previous_stem(line_initial_after_w, 1, GRAM2), "591")
        self.assertEqual(
            site_backward_3gram(line_initial_after_w, 1, GRAM2),
            ("591", "090", "076"),
        )
        self.assertIsNone(site_previous_4gram(line_initial_after_w, 1, GRAM2))
        no_prev = ["090", "076", "020"]
        self.assertIsNone(site_previous_stem(no_prev, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(no_prev, 0, GRAM2))
        self.assertTrue(STANDING_021_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_600_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_zero_off_i_n6_and_complete_4grams(self):
        """Boolean is True only when N=6, no line-initial, and all 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_N_REMAINING_AFTER_600_LOCK,
                0,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                (2, 1, 1, 1, 1, 1),
                hold_zeros,
                STANDING_N_REMAINING_AFTER_600_LOCK,
                0,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                hold_ones,
                (1, 0, 0, 0, 0, 0),
                STANDING_N_REMAINING_AFTER_600_LOCK,
                0,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                (0, 1, 1, 1, 1, 1),
                hold_zeros,
                STANDING_N_REMAINING_AFTER_600_LOCK,
                0,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                hold_ones,
                hold_zeros,
                5,
                0,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_N_REMAINING_AFTER_600_LOCK,
                1,
                STANDING_REMAINING_SITES,
            )
        )
        drifted = STANDING_REMAINING_SITES[:-1] + ((SIDE_IA, "Ia14", 54),)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_N_REMAINING_AFTER_600_LOCK,
                0,
                drifted,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                (),
                (),
                0,
                0,
                (),
            )
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_PREVIOUS_4GRAMS_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_PREVIOUS_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_DO_NOT_LOCK_EXACTLY_1_SHARE_PREVIOUS_999)
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertTrue(CYCLE217_CLAIM)
        self.assertTrue(CYCLE257_CLAIM)
        self.assertEqual(CYCLE257_N_I_ONLY, 19)
        self.assertTrue(CYCLE285_CLAIM)
        self.assertEqual(CYCLE285_N_I_ONLY, 27)
        self.assertTrue(CYCLE299_CLAIM)
        self.assertEqual(CYCLE299_N_I_ONLY, 2)
        self.assertFalse(CYCLE308_CLAIM)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_308_remaining_after_600_previous_not_retuned(self):
        """4-grams stay the cycle-308 remaining-after-600 previouss; 021 / 600 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(STANDING_REMAINING_SITES, CYCLE308_REMAINING_SITES)
        self.assertEqual(
            STANDING_REMAINING_PREVIOUS_STEMS, CYCLE308_REMAINING_PREVIOUS_STEMS
        )
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE308_N_REMAINING_AFTER_600)
        self.assertEqual(CYCLE308_N_REMAINING_AFTER_600, 6)
        self.assertEqual(CYCLE308_N_DISTINCT, 6)
        self.assertEqual(CYCLE308_G, "999")
        self.assertEqual(CYCLE308_K, 1)
        self.assertFalse(CYCLE308_UNIQUE)
        self.assertFalse(CYCLE308_CLAIM)
        self.assertEqual(CYCLE308_TIED_STEMS, ("999", "591", "090", "076", "008", "000"))
        self.assertEqual(len(set(STANDING_PREVIOUS_STEMS)), 6)
        self.assertEqual(len(set(STANDING_SEQUENCES)), 6)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(STANDING_SEQUENCES[4], CYCLE308_G_PREVIOUS_4GRAM[0])
        self.assertEqual(STANDING_CONTINUING_SITES[4], CYCLE308_G_SITES[0])
        for gram, prev in zip(STANDING_SEQUENCES, STANDING_PREVIOUS_STEMS, strict=True):
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertEqual(gram[1], prev)
            self.assertNotIn(prev, LOCKED_PREVIOUS_STEMS_AFTER_600)
            self.assertNotEqual(gram[1:], ("021", "090", "076"))
            self.assertNotEqual(gram[1:], ("600", "090", "076"))
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram[2:], CYCLE171_GRAM2)
        for site, start in zip(
            STANDING_CONTINUING_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(leftover_previous_4gram_start_site(site), start)
            self.assertEqual(start[2], site[2] - 2)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE257)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE285)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE299)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_PEEL_999)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_SAME_AS_CYCLE308)
        self.assertFalse(STANDING_SAME_AS_CYCLE299)
        self.assertFalse(STANDING_SAME_AS_CYCLE285)
        self.assertFalse(STANDING_SAME_AS_CYCLE257)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter600Prev4IOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-600 previous-4 I-only lock."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.inside_sites = STANDING_INSIDE_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.previous_stems = leftover_n4_remaining_previous_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.leftover_previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.backwards = leftover_n4_remaining_backward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.remaining = leftover_n4_remaining_remaining_after_600(
            self.inside_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_600_previous_stems(
            self.inside_sites,
            self.previous_stems,
        )
        self.with_previous = leftover_n4_remaining_remaining_after_600_with_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.no_previous = leftover_n4_remaining_remaining_after_600_without_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.per_site_previous_4grams = leftover_n4_remaining_remaining_after_600_previous_4grams(
            self.inside_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.line_initial = leftover_n4_remaining_remaining_after_600_line_initial_sites(
            self.inside_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.continuing = leftover_n4_remaining_remaining_after_600_continuing_sites(
            self.inside_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.grams = continuing_previous_4grams(self.per_site_previous_4grams)
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams)
        self.n_i = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) + STANDING_IB_HITS
            for gram in self.grams
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.grams
        )
        self.off_i = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in self.grams
        )
        self.n_off_i = tuple(sum(row) for row in self.off_i)
        self.g, self.k, self.unique = select_remaining_after_600_g(
            self.remaining_stems
        )
        self.n_remaining = len(self.remaining)
        self.n_line_initial = len(self.line_initial)
        self.overlap_258 = leftover_n4_remaining_g_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259 = leftover_n4_remaining_g_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_258_057 = leftover_n4_remaining_g_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_BY_X["057"],
        )
        self.overlap_259_057 = leftover_n4_remaining_g_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_BY_X["057"],
        )
        self.overlap_295 = leftover_n4_remaining_g_overlap_sites(
            self.remaining,
            CYCLE295_MATCHING_SITES,
        )
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
                self.n_remaining,
                self.n_line_initial,
                self.remaining,
            )
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_hapax_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_hapax_i_only(on, off)
        )
        self.n_not_i_only = len(self.grams) - self.n_i_only
        self.n_leak_off_i = sum(1 for off in self.n_off_i if off > 0)
        self.leaking = tuple(
            gram
            for gram, on, off in zip(self.grams, self.n_i, self.n_off_i, strict=True)
            if not sequence_is_i_only(on, off)
        )

    def test_tokens_and_sites_are_cycle_308_remaining_after_600_not_retuned(self):
        """4-grams stay the cycle-308 remaining-after-600 lock. Nested 6/K=1/G=999 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(len(self.inside_sites), STANDING_N_INSIDE_LOCK)
        self.assertEqual(STANDING_N_INSIDE_LOCK, CYCLE224_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE_LOCK, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE308_REMAINING_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(len(self.remaining), STANDING_N_REMAINING_AFTER_600_LOCK)
        self.assertEqual(STANDING_N_REMAINING_AFTER_600_LOCK, 6)
        self.assertEqual(len(set(self.remaining_stems)), CYCLE308_N_DISTINCT)
        self.assertEqual(self.g, CYCLE308_G)
        self.assertEqual(self.g, "999")
        self.assertEqual(self.k, CYCLE308_K)
        self.assertEqual(self.k, 1)
        self.assertFalse(self.unique)
        self.assertFalse(CYCLE308_UNIQUE)
        self.assertFalse(CYCLE308_CLAIM)
        if (
            len(self.remaining) != 6
            or self.k != 1
            or self.g != "999"
            or self.unique
            or CYCLE308_CLAIM
        ):
            self.fail(
                "nested cycle 308 unique-max false N_remaining_after_600=6 K=1 G=999 drifted"
            )
        self.assertEqual(self.per_site_previous_4grams, STANDING_REMAINING_PREVIOUS_4GRAMS)
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.continuing, STANDING_CONTINUING_SITES)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(self.line_initial, ())
        self.assertEqual(self.no_previous, STANDING_NO_PREVIOUS_SITES)
        self.assertEqual(len(self.grams), STANDING_N_CONTINUING)
        self.assertEqual(STANDING_N_CONTINUING, 6)
        self.assertEqual(STANDING_N_4GRAMS, 6)
        self.assertEqual(len(self.line_initial), STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertTrue(all(stem is not None for stem in self.remaining_stems))
        self.assertTrue(all(gram is not None for gram in self.per_site_previous_4grams))
        self.assertEqual(self.with_previous, self.remaining)
        self.assertEqual(self.no_previous, ())
        self.assertEqual(
            self.remaining,
            leftover_n4_remaining_remaining_after_021_without_previous_600(
                self.inside_sites,
                self.previous_stems,
            ),
        )
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_nested_counts_hold(
                13,
                4,
                9,
                3,
                6,
                2,
                4,
                2,
                2,
            )
        )
        self.assertTrue(
            leftover_n4_remaining_remaining_after_021_nested_counts_hold(
                13,
                0,
                5,
                8,
            )
        )
        self.assertTrue(
            leftover_n4_remaining_remaining_after_600_nested_counts_hold(
                13,
                0,
                5,
                8,
                2,
                6,
            )
        )
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, (13, 4, 9, 3, 6, 2, 4, 2, 2))
        self.assertEqual(STANDING_K_020, 4)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(STANDING_K_087, 3)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(STANDING_K_057, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, 4)
        self.assertEqual(STANDING_K_011, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_011, 2)
        self.assertEqual(STANDING_K_021, 5)
        self.assertEqual(STANDING_N_REMAINING_AFTER_021, 8)
        self.assertEqual(STANDING_K_600, 2)
        prior_308 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem"
        ]
        self.assertEqual(prior_308["cycle"], 308)
        self.assertEqual(prior_308["N_remaining_after_600"], 6)
        self.assertEqual(prior_308["K"], 1)
        self.assertEqual(prior_308["G"], "999")
        self.assertEqual(prior_308["N_distinct"], 6)
        self.assertFalse(prior_308["G_uniquely_most_frequent"])
        self.assertFalse(
            prior_308[
                "i_leftover_n4_remaining_090_076_remaining_after_600_unique_previous_stem"
            ]
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_308["remaining_after_600_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(prior_308["remaining_after_600_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        prior_257 = self.survey[
            "i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"
        ]
        self.assertEqual(prior_257["cycle"], 257)
        self.assertEqual(prior_257["N_i_only"], 19)
        self.assertEqual(prior_257["N_not_i_only"], 0)
        self.assertTrue(CYCLE257_CLAIM)
        prior_285 = self.survey[
            "i_leftover_extra_090_076_remaining_after_009_prev4_i_only"
        ]
        self.assertEqual(prior_285["cycle"], 285)
        self.assertEqual(prior_285["N_i_only"], 27)
        self.assertTrue(CYCLE285_CLAIM)
        prior_299 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_011_fwd4_i_only"
        ]
        self.assertEqual(prior_299["cycle"], 299)
        self.assertEqual(prior_299["N_i_only"], 2)
        self.assertTrue(CYCLE299_CLAIM)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_LOCK_EXACTLY_1_SHARE_PREVIOUS_999)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_no_line_initial_and_claim_holds(self):
        """Each remaining-after-600 previous 4-gram is N_I=1, N_off_I=0. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1, 1, 1, 1, 1, 1))
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0, 0, 0, 0, 0, 0))
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.line_initial, ())
        self.assertEqual(self.leaking, STANDING_LEAKING_4GRAMS)
        self.assertEqual(self.leaking, ())
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_i_only, 6)
        self.assertEqual(self.n_hapax_i_only, STANDING_N_HAPAX_I_ONLY)
        self.assertEqual(self.n_hapax_i_only, 6)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_not_i_only, 0)
        self.assertEqual(self.n_leak_off_i, STANDING_N_LEAK_OFF_I)
        self.assertEqual(self.n_leak_off_i, 0)
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from 0")
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked remaining-after-600 hapax")
        if self.line_initial:
            self.fail("measured line-initial remaining-after-600 set drifted from empty")
        if self.leaking:
            self.fail("measured remaining-after-600 previous 4-grams leaked off I")
        if self.n_remaining != 6:
            self.fail("measured N_remaining_after_600 drifted from 6")
        for site, start, gram, prev, role, sites, n_on, n_off, hapax in zip(
            STANDING_CONTINUING_SITES,
            (row[0] for row in STANDING_I_SITES),
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_HAPAX_EACH,
            strict=True,
        ):
            self.assertEqual(leftover_previous_4gram_start_site(site), start)
            self.assertEqual(sites, (start,))
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2] + 1], prev)
            self.assertEqual(tuple(stems[start[2] + 2 : start[2] + 4]), GRAM2)
            self.assertEqual(site_previous_4gram(stems, site[2], GRAM2), gram)
            self.assertGreaterEqual(site[2], 2)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[1:], ("021", "090", "076"))
            self.assertNotEqual(gram[1:], ("600", "090", "076"))
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotIn(prev, LOCKED_PREVIOUS_STEMS_AFTER_600)
            self.assertEqual(role, "leftover_n4_remaining_remaining_after_600")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertTrue(sequence_is_hapax_i_only(n_on, n_off))
            self.assertTrue(hapax)
        if not self.claim_holds:
            self.fail("measured remaining-after-600 previous 4-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_ALL_REMAINING_HAVE_PREVIOUS_TOKEN)
        self.assertTrue(STANDING_ALL_REMAINING_HAVE_FOURTH_TOKEN)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off in zip(self.hits_by_tablet, self.off_i, strict=True):
            self.assertEqual(hits, STANDING_HITS_BY_TABLET_ONE_ON_I)
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
        for tablet, *counts in zip(
            VENDORED_TABLETS,
            *self.hits_by_tablet,
            strict=True,
        ):
            for count, gram in zip(counts, self.grams, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, 1 if tablet == "I" else 0)
        self.assertEqual(
            i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
                self.n_remaining,
                self.n_line_initial,
                self.remaining,
            ),
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_PREVIOUS_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_PREVIOUS_4GRAMS_ALL_I_ONLY
        )
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE257)
        self.assertFalse(STANDING_SAME_AS_CYCLE285)
        self.assertFalse(STANDING_SAME_AS_CYCLE299)
        self.assertFalse(STANDING_SAME_AS_CYCLE308)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE257)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE285)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE299)
        self.assertTrue(STANDING_021_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_600_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_009_PREV4_IS_NOT_THIS_CYCLE)
        self.assertTrue(
            STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_FWD4_IS_NOT_THIS_CYCLE
        )
        self.assertTrue(
            STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXTRA_I_FWD4_IS_NOT_THIS_CYCLE
        )
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_LOCK_EXACTLY_1_SHARE_PREVIOUS_999)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        for site in CYCLE307_MATCHING_SITES:
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        for site in CYCLE303_MATCHING_SITES:
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        for site in CYCLE223_OFF_I_SITES:
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        for gram in CYCLE285_SEQUENCES:
            self.assertNotIn(gram, STANDING_SEQUENCES)
        for gram in CYCLE257_SEQUENCES:
            if gram == STANDING_OVERLAP_CYCLE257_FWD4_4GRAM:
                self.assertIn(gram, STANDING_SEQUENCES)
            else:
                self.assertNotIn(gram, STANDING_SEQUENCES)
        for gram in CYCLE299_SEQUENCES:
            self.assertNotIn(gram, STANDING_SEQUENCES)
        self.assertEqual(STANDING_SEQUENCES[1], STANDING_OVERLAP_CYCLE257_FWD4_4GRAM)
        self.assertIn(STANDING_OVERLAP_CYCLE257_FWD4_4GRAM, CYCLE257_SEQUENCES)
        self.assertTrue(STANDING_OVERLAP_CYCLE257_FWD4)
        self.assertNotIn(STANDING_SEQUENCES[3], CYCLE259_SEQUENCES)
        self.assertNotIn(STANDING_SEQUENCES[4], CYCLE259_SEQUENCES)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        unused_021_lock = LOCKED_PREVIOUS_STEMS_AFTER_021
        self.assertEqual(unused_021_lock, ("021",))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_overlap_cycle258_259_295_recorded_does_not_lose(self):
        """Ia8[114]/Ia9[28] overlap cycle 258/259 extra I 057 and cycle 295 next 057. Record, do not fail."""
        self.assertEqual(self.overlap_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258_057, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259_057, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_295, STANDING_OVERLAP_CYCLE295_NEXT_057)
        self.assertEqual(
            self.overlap_258,
            ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
        )
        self.assertEqual(self.overlap_258, CYCLE308_OVERLAP_258)
        self.assertEqual(self.overlap_259, CYCLE308_OVERLAP_259)
        self.assertTrue(STANDING_OVERLAP_CYCLE258_EXTRA_I_057)
        self.assertTrue(STANDING_OVERLAP_CYCLE259_EXTRA_I_057)
        self.assertFalse(STANDING_IA2_IA4_IA5_IA12_OVERLAP_258_259_295)
        self.assertIn((SIDE_IA, "Ia8", 114), CYCLE259_EXTRA_I_SITES)
        self.assertIn((SIDE_IA, "Ia9", 28), CYCLE259_EXTRA_I_SITES)
        self.assertIn((SIDE_IA, "Ia8", 114), CYCLE259_EXTRA_I_BY_X["057"])
        self.assertIn((SIDE_IA, "Ia9", 28), CYCLE259_EXTRA_I_BY_X["057"])
        self.assertIn((SIDE_IA, "Ia8", 114), CYCLE295_MATCHING_SITES)
        self.assertIn((SIDE_IA, "Ia9", 28), CYCLE295_MATCHING_SITES)
        self.assertNotIn((SIDE_IA, "Ia2", 119), CYCLE259_EXTRA_I_SITES)
        self.assertNotIn((SIDE_IA, "Ia4", 86), CYCLE259_EXTRA_I_SITES)
        self.assertNotIn((SIDE_IA, "Ia5", 143), CYCLE259_EXTRA_I_SITES)
        self.assertNotIn((SIDE_IA, "Ia12", 83), CYCLE259_EXTRA_I_SITES)
        self.assertNotIn((SIDE_IA, "Ia8", 106), self.remaining)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(CYCLE308_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(self.claim_holds)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        self.assertEqual(len(CYCLE259_EXTRA_I_SITES), 3)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertTrue(CYCLE259_CLAIM)
        self.assertTrue(CYCLE295_CLAIM)
        self.assertEqual(CYCLE295_K_057, 2)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_308_307_306_303_299_295_288_285_270_259_257_224_223_still_compute(self):
        """Cycle 308 unique-max lose, 307 K_600=2, 306 G=600 K=2, 303 K_021=5, 299/285/257 analogs, 295 K_057=2, 288 G=020 K=4, 270 5-way, 259 extra-I, 224 13/56, 223 69/3 stay."""
        prior_308 = TestMamariILeftoverN4Remaining090076RemainingAfter600PreviousStemScoreboard()
        prior_308.setUp()
        prior_308.test_counts_6_remaining_all_hapax_g_999_k_1_and_hypothesis_loses()
        prior_308.test_survey_matches_computed_lock()
        self.assertEqual(prior_308.n_remaining, 6)
        self.assertEqual(prior_308.k, 1)
        self.assertEqual(prior_308.g, "999")
        self.assertEqual(prior_308.n_distinct, 6)
        self.assertFalse(prior_308.unique)
        self.assertFalse(prior_308.claim_holds)
        self.assertFalse(CYCLE308_CLAIM)
        self.assertEqual(CYCLE308_N_REMAINING_AFTER_600, 6)
        self.assertEqual(CYCLE308_K, 1)
        self.assertEqual(CYCLE308_G, "999")
        self.assertEqual(CYCLE308_N_DISTINCT, 6)
        if (
            prior_308.n_remaining != 6
            or prior_308.k != 1
            or prior_308.g != "999"
            or prior_308.unique
            or prior_308.n_distinct != 6
        ):
            self.fail(
                "nested cycle 308 unique-max false N_remaining_after_600=6 K=1 G=999 drifted"
            )
        prior_307 = TestMamariILeftoverN4Remaining090076RemainingAfter021Previous600Scoreboard()
        prior_307.setUp()
        prior_307.test_counts_2_of_8_and_hypothesis_k_2_holds()
        prior_307.test_survey_matches_computed_lock()
        self.assertEqual(prior_307.k_600, 2)
        self.assertEqual(prior_307.n_remaining_after_600, 6)
        self.assertEqual(prior_307.matching, CYCLE307_MATCHING_SITES)
        self.assertTrue(prior_307.claim_holds)
        self.assertTrue(CYCLE307_CLAIM)
        self.assertEqual(CYCLE307_K_600, 2)
        self.assertEqual(CYCLE307_N_REMAINING_AFTER_600, 6)
        if prior_307.k_600 != 2 or prior_307.n_remaining_after_600 != 6:
            self.fail(
                "nested cycle 307 leftover n=4 remaining remaining-after-021 exactly 2 share 600 drifted"
            )
        prior_306 = TestMamariILeftoverN4Remaining090076RemainingAfter021PreviousStemScoreboard()
        prior_306.setUp()
        prior_306.test_counts_8_remaining_g_600_k_2_and_hypothesis_holds()
        prior_306.test_survey_matches_computed_lock()
        self.assertEqual(prior_306.g, "600")
        self.assertEqual(prior_306.k, 2)
        self.assertEqual(prior_306.n_remaining, 8)
        self.assertEqual(prior_306.n_distinct, 7)
        self.assertTrue(prior_306.unique)
        self.assertTrue(prior_306.claim_holds)
        self.assertTrue(CYCLE306_CLAIM)
        self.assertEqual(CYCLE306_G, "600")
        self.assertEqual(CYCLE306_K, 2)
        self.assertEqual(CYCLE306_N_REMAINING, 8)
        self.assertEqual(CYCLE306_N_DISTINCT, 7)
        self.assertTrue(CYCLE306_UNIQUE)
        if (
            prior_306.g != "600"
            or prior_306.k != 2
            or prior_306.n_remaining != 8
            or prior_306.n_distinct != 7
            or not prior_306.unique
        ):
            self.fail(
                "nested cycle 306 unique-max G=600 K=2 N_remaining=8 distinct=7 drifted"
            )
        prior_303 = TestMamariILeftoverN4Remaining090076Previous021Scoreboard()
        prior_303.setUp()
        prior_303.test_counts_5_of_13_and_hypothesis_k_5_holds()
        prior_303.test_survey_matches_computed_lock()
        self.assertEqual(prior_303.k_021, 5)
        self.assertEqual(prior_303.n_remaining_after_021, 8)
        self.assertTrue(prior_303.claim_holds)
        self.assertTrue(CYCLE303_CLAIM)
        self.assertEqual(CYCLE303_K_021, 5)
        self.assertEqual(CYCLE303_N_REMAINING_AFTER_021, 8)
        if prior_303.k_021 != 5 or prior_303.n_remaining_after_021 != 8:
            self.fail(
                "nested cycle 303 leftover n=4 remaining exactly 5 share 021 drifted"
            )
        prior_299 = TestMamariILeftoverN4Remaining090076RemainingAfter011Fwd4IOnlyScoreboard()
        prior_299.setUp()
        prior_299.test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds()
        prior_299.test_survey_matches_computed_lock()
        self.assertEqual(prior_299.n_i_only, 2)
        self.assertEqual(prior_299.n_not_i_only, 0)
        self.assertTrue(prior_299.claim_holds)
        self.assertTrue(CYCLE299_CLAIM)
        self.assertEqual(CYCLE299_N_I_ONLY, 2)
        self.assertEqual(CYCLE299_N_NOT_I_ONLY, 0)
        if prior_299.n_i_only != 2 or prior_299.n_not_i_only != 0:
            self.fail(
                "nested cycle 299 leftover n=4 remaining remaining-after-011 forward 4-grams 2/0 drifted"
            )
        prior_295 = TestMamariILeftoverN4Remaining090076RemainingAfter087Forward057Scoreboard()
        prior_295.setUp()
        prior_295.test_counts_2_of_6_and_hypothesis_k_2_holds()
        prior_295.test_survey_matches_computed_lock()
        self.assertEqual(prior_295.k_057, 2)
        self.assertEqual(prior_295.matching, CYCLE295_MATCHING_SITES)
        self.assertTrue(prior_295.claim_holds)
        self.assertTrue(CYCLE295_CLAIM)
        self.assertEqual(CYCLE295_K_057, 2)
        if prior_295.k_057 != 2:
            self.fail(
                "nested cycle 295 leftover n=4 remaining remaining-after-087 exactly 2 share 057 drifted"
            )
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        if prior_288.g != "020" or prior_288.k != 4 or not prior_288.unique_max:
            self.fail("nested cycle 288 unique-max G=020 K=4 share-one lost drifted")
        prior_285 = TestMamariILeftoverExtra090076RemainingAfter009Prev4IOnlyScoreboard()
        prior_285.setUp()
        prior_285.test_each_4gram_is_one_on_i_zero_off_i_no_line_initial_and_claim_holds()
        prior_285.test_survey_matches_computed_lock()
        self.assertEqual(prior_285.n_i_only, 27)
        self.assertEqual(prior_285.n_not_i_only, 0)
        self.assertTrue(prior_285.claim_holds)
        self.assertTrue(CYCLE285_CLAIM)
        self.assertEqual(CYCLE285_N_I_ONLY, 27)
        self.assertEqual(CYCLE285_N_NOT_I_ONLY, 0)
        if prior_285.n_i_only != 27 or prior_285.n_not_i_only != 0:
            self.fail(
                "nested cycle 285 leftover extra remaining-after-009 previous 4-grams 27/0 drifted"
            )
        prior_270 = TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard()
        prior_270.setUp()
        prior_270.test_counts_37_remaining_g_090_k_2_five_way_tie_and_hypothesis_loses()
        prior_270.test_survey_matches_computed_lock()
        self.assertEqual(prior_270.g, "090")
        self.assertEqual(prior_270.k, 2)
        self.assertFalse(prior_270.unique)
        self.assertFalse(prior_270.claim_holds)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_TIED, 5)
        self.assertFalse(CYCLE270_UNIQUE)
        if prior_270.g != "090" or prior_270.k != 2 or prior_270.unique:
            self.fail(
                "nested cycle 270 leftover extra remaining-after-600 unique-max false G=090 K=2 5-way tie drifted"
            )
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE258_CLAIM)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        prior_257 = TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard()
        prior_257.setUp()
        prior_257.test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds()
        prior_257.test_survey_matches_computed_lock()
        self.assertEqual(prior_257.n_i_only, 19)
        self.assertEqual(prior_257.n_not_i_only, 0)
        self.assertTrue(prior_257.claim_holds)
        self.assertTrue(CYCLE257_CLAIM)
        self.assertEqual(CYCLE257_N_I_ONLY, 19)
        self.assertEqual(CYCLE257_N_NOT_I_ONLY, 0)
        if prior_257.n_i_only != 19 or prior_257.n_not_i_only != 0:
            self.fail(
                "nested cycle 257 leftover extra remaining-after-000 forward 4-grams 19/0 drifted"
            )
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        if CYCLE224_N_INSIDE != 13 or CYCLE224_N_LEFTOVER != 56:
            self.fail("nested cycle 224 13/56 drifted")
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
        self.assertEqual(len(CYCLE223_I_SITES), 69)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_217 = TestMamariILeftover076070Forward4gramsIOnlyScoreboard()
        prior_217.setUp()
        prior_217.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_217.test_survey_matches_computed_lock()
        self.assertTrue(prior_217.claim_holds)
        self.assertTrue(CYCLE217_CLAIM)
        if sum(CYCLE217_N_I_EACH) != 11 or sum(CYCLE217_N_OFF_I_EACH) != 0:
            self.fail("nested cycle 217 leftover 076 070 forward 4-grams 11/11 hapax drifted")
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertEqual(prior_219.n_i_only, 7)
        self.assertEqual(prior_219.n_not_i_only, 1)
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_CLAIM)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_LOCK_EXACTLY_1_SHARE_PREVIOUS_999)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-309 remaining-after-600 previous-4 I-only lock."""
        lock = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_600_prev4_i_only"
        ]
        self.assertEqual(lock["cycle"], 309)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(
            tuple(lock["locked_previous_stems_after_600"]),
            LOCKED_PREVIOUS_STEMS_AFTER_600,
        )
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE_LOCK)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(lock["N_remaining_after_600"], STANDING_N_REMAINING_AFTER_600_LOCK)
        self.assertEqual(lock["N_remaining_after_600"], 6)
        self.assertEqual(lock["N_4grams"], STANDING_N_4GRAMS)
        self.assertEqual(lock["N_4grams"], 6)
        self.assertEqual(lock["N_continuing"], STANDING_N_CONTINUING)
        self.assertEqual(lock["N_continuing"], 6)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["K"], 1)
        self.assertEqual(lock["G"], "999")
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertFalse(
            lock["i_leftover_n4_remaining_090_076_remaining_after_600_unique_previous_stem"]
        )
        self.assertEqual(lock["N_distinct"], 6)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_600_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_600_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["remaining_after_600_previous_4grams"],
        )
        self.assertEqual(lock["line_initial_remaining_after_600_sites"], [])
        self.assertEqual(
            tuple(tuple(row) for row in lock["continuing_sites"]),
            STANDING_CONTINUING_SITES,
        )
        self.assertTrue(lock["all_remaining_after_600_have_previous_token"])
        self.assertTrue(lock["all_remaining_after_600_have_fourth_token"])
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_CONTINUING)
        for row, gram, site, prev, role, sites, n_on, n_off, hapax in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CONTINUING_SITES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_HAPAX_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle308_site"]), site)
            self.assertEqual(row["previous_stem"], prev)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["ia_hits"], 1)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["ib_sites"]),
                STANDING_IB_SITES,
            )
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(row["off_i_tablets_with_hits"], [])
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(
                tuple(row["hits_by_tablet"]),
                STANDING_HITS_BY_TABLET_ONE_ON_I,
            )
            self.assertTrue(row["i_only"])
            self.assertTrue(row["hapax"])
            self.assertTrue(row["hapax_on_I"])
            self.assertEqual(row["hapax_on_I"], hapax)
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(tuple(lock["hapax_each"]), STANDING_HAPAX_EACH)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock[
                "i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only"
            ]
        )
        self.assertTrue(
            lock[
                "i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_i_only"
            ]
        )
        self.assertEqual(lock["N_i_only"], 6)
        self.assertEqual(lock["N_hapax_i_only"], 6)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["N_leak_off_i"], 0)
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE258_EXTRA_I],
            lock["overlap_cycle258_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE259_EXTRA_I],
            lock["overlap_cycle259_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE295_NEXT_057],
            lock["overlap_cycle295_next_057_sites"],
        )
        self.assertTrue(lock["overlap_cycle258_extra_i_057"])
        self.assertTrue(lock["overlap_cycle259_extra_i_057"])
        self.assertFalse(lock["ia2_ia4_ia5_ia12_overlap_cycle258_259_295"])
        self.assertEqual(
            tuple(lock["overlap_cycle257_fwd4_4gram"]),
            STANDING_OVERLAP_CYCLE257_FWD4_4GRAM,
        )
        self.assertTrue(lock["overlap_cycle257_fwd4"])
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertEqual(lock["nested_leftover_n4_remaining"], [13, 4, 9, 3, 6, 2, 4, 2, 2])
        self.assertEqual(lock["nested_cycle308_N_remaining_after_600"], 6)
        self.assertEqual(lock["nested_cycle308_K"], 1)
        self.assertEqual(lock["nested_cycle308_G"], "999")
        self.assertEqual(lock["nested_cycle308_N_distinct"], 6)
        self.assertFalse(lock["nested_cycle308_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle307_K_600"], 2)
        self.assertEqual(lock["nested_cycle307_N_remaining_after_600"], 6)
        self.assertEqual(lock["nested_cycle306_G"], "600")
        self.assertEqual(lock["nested_cycle306_K"], 2)
        self.assertEqual(lock["nested_cycle306_N_remaining_after_021"], 8)
        self.assertEqual(lock["nested_cycle306_N_distinct"], 7)
        self.assertTrue(lock["nested_cycle306_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle303_K_021"], 5)
        self.assertEqual(lock["nested_cycle303_N_remaining_after_021"], 8)
        self.assertEqual(lock["nested_cycle299_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle299_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle295_K_057"], 2)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertTrue(lock["nested_cycle288_G_uniquely_most_frequent"])
        self.assertFalse(lock["nested_cycle288_share_one_forward_stem"])
        self.assertEqual(lock["nested_cycle285_N_i_only"], 27)
        self.assertEqual(lock["nested_cycle285_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle270_G"], "090")
        self.assertEqual(lock["nested_cycle270_K"], 2)
        self.assertEqual(lock["nested_cycle270_N_tied_at_K"], 5)
        self.assertFalse(lock["nested_cycle270_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle259_N_extra_i"], 3)
        self.assertEqual(lock["nested_cycle258_N_extra"], 3)
        self.assertEqual(lock["nested_cycle257_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle257_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle219_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["nested_cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["nested_cycle217_N_i_only"], 11)
        self.assertEqual(lock["nested_cycle217_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle171_N_I"], 43)
        self.assertEqual(lock["nested_cycle171_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle257"])
        self.assertFalse(lock["same_as_cycle258"])
        self.assertFalse(lock["same_as_cycle259"])
        self.assertFalse(lock["same_as_cycle270"])
        self.assertFalse(lock["same_as_cycle285"])
        self.assertFalse(lock["same_as_cycle288"])
        self.assertFalse(lock["same_as_cycle295"])
        self.assertFalse(lock["same_as_cycle299"])
        self.assertFalse(lock["same_as_cycle303"])
        self.assertFalse(lock["same_as_cycle306"])
        self.assertFalse(lock["same_as_cycle307"])
        self.assertFalse(lock["same_as_cycle308"])
        self.assertTrue(lock["same_claim_shape_as_cycle217"])
        self.assertTrue(lock["same_claim_shape_as_cycle257"])
        self.assertTrue(lock["same_claim_shape_as_cycle285"])
        self.assertTrue(lock["same_claim_shape_as_cycle299"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["do_not_peel_999"])
        self.assertTrue(lock["do_not_lock_exactly_1_share_previous_999"])
        self.assertTrue(lock["leftover_extra_remaining_after_009_prev4_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_remaining_after_000_fwd4_is_not_this_cycle"])
        self.assertTrue(
            lock["leftover_extra_remaining_after_000_extra_i_fwd4_is_not_this_cycle"]
        )
        self.assertTrue(
            lock["leftover_extra_remaining_after_600_unique_max_is_not_this_cycle"]
        )
        self.assertTrue(
            lock["leftover_n4_remaining_remaining_after_011_fwd4_is_not_this_cycle"]
        )
        self.assertTrue(
            lock[
                "leftover_n4_remaining_remaining_after_021_unique_previous_stem_is_not_this_cycle"
            ]
        )
        self.assertTrue(
            lock["leftover_n4_remaining_remaining_after_021_previous_600_is_not_this_cycle"]
        )
        self.assertTrue(
            lock["leftover_extra_remaining_after_000_extra_i_is_not_this_cycle"]
        )
        self.assertTrue(
            lock["leftover_n4_remaining_remaining_after_087_next_057_is_not_this_cycle"]
        )
        self.assertTrue(lock["021_090_076_does_not_count"])
        self.assertTrue(lock["600_090_076_does_not_count"])
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_are_this_cycle_only_if_matching_4gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_090_076_remaining_after_021_previous_600_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem_unchanged"
            ]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_previous_021_unchanged"]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_090_076_remaining_after_011_fwd4_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_extra_090_076_remaining_after_009_prev4_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_090_076_remaining_after_087_forward_057_unchanged"
            ]
        )
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"]
        )
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey[
                "i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem"
            ]["cycle"],
            308,
        )
        self.assertFalse(
            self.survey[
                "i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem"
            ]["i_leftover_n4_remaining_090_076_remaining_after_600_unique_previous_stem"]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"][
                "cycle"
            ],
            257,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter600Prev4IOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 309 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
