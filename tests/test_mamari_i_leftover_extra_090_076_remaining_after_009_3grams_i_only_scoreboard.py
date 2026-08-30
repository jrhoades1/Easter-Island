"""I's cycle-285 leftover extra remaining-after-009 3-grams off-I lock.

Cycle 286 text-search lock. Uses already-vendored A–V and the
cycle-284 leftover extra remaining-after-009 I sites of 2-gram
090 076 (the 27 leftover extra with-previous sites whose
previous token is none of 999, 600, 090, 076, 071, 045, or
009). Does not retune leftover extra remaining-after-009
unique-max (cycle 284 lost: 27 hapax, G=724 K=1), leftover
extra remaining-after-009 previous 4-grams (cycle 285 held:
27/27 hapax 1/0), leftover extra remaining-after-045
previous-009 (cycle 281 K=2 N_remaining=27), leftover extra
sites, leftover n=4, or the already-closed leftover remaining
family. Does not retune the forward peel (225–259). Does not
overwrite cycle 167's 3-gram I-only 16/0 lock. Does not
overwrite cycles 268–285. Does not vendor a new tablet. Does
not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new
agents. Not a meaning dictionary.

Same claim-shape as cycle 258 leftover extra remaining-after-
000 3-grams all I-only 19/19 extra I=3, previous side instead
of forward, and cycle 245 (090 076 087 was I-only 5/0 extra
I=3 inside leftover n=4). Cycle 272 090 090 076 I-only lost
3/1 on T is the lose-path analog. Cycle 207 090 076 070 lost
8/1 on T. Cycle 284 leftover extra remaining-after-009
unique-max lost N_remaining_after_009=27 K=1 27-way tie
G=724, cycle 285 remaining-after-009 previous 4-grams all
I-only hapax 1/0 x27, cycle 283 2/0 hapax, cycle 282 2/0
extra I=0, cycle 258 19/19 extra I=3, cycle 223 69/3, and
cycle 167 16/0 stay. Nested-check leftover extra remaining-
after-009 unique-max false, N_remaining_after_009==27, K==1,
and all 27 previous 4-grams 1/0 (do not retune cycles
284/285). 3-grams W 090 076 for those 27 W are not yet
locked. Extra I of each (sites of W 090 076 not in leftover
extra remaining-after-009) is leftover-of-leftover, same
shape as cycle 245 extra I of 090 076 087 and cycle 258
extra I of remaining-after-000 3-grams. Do not confuse with
already-locked previous 3-grams (999/600/090/076/071/045/
009). Remaining-after-009 W is none of those. Do not peel
leftover extra I 090 076 previous stems this cycle. Do not
retune leftover n=4.

Locks exact consecutive hits of each leftover extra
remaining-after-009 3-gram W 090 076 on tablet I and on
every other vendored tablet A–H and J–V. The twenty-seven
3-grams: 048 090 076, 380 090 076, 011 090 076,
499 090 076, 497 090 076, 036 090 076, 092 090 076,
291 090 076, 522 090 076, 150 090 076, 078 090 076,
295 090 076, 000 090 076, 109 090 076, 052 090 076,
099 090 076, 700 090 076, 161 090 076, 010 090 076,
205 090 076, 382 090 076, 386 090 076, 008 090 076,
027 090 076, 724 090 076, 400 090 076, 326 090 076.
Measure; do not assume the stem list if nested-check
differs. Hypothesis: all 27 leftover extra remaining-after-
009 3-grams W 090 076 are I-only. Claim that can lose:
i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only.
True iff every one of those 27 3-grams has N_I ≥ 1 and
N_off_I = 0. Extra I ≠ 0 for some W does not make the
claim lose (still I-only); still lock extra I. This can
lose if any W 090 076 leaks off I (same shape as cycle 272
090 090 076 3/1 on T and cycle 207 090 076 070 8/1 on T).
Given 2-gram 090 076 already leaks on T, this is a real
lose path. Measured: N_i_only=27 / N_not_i_only=0; extra I
total=2 (000 extra I=1 at Ia8[113] inside leftover n=4
remaining 090 076 057 600; 008 extra I=1 at Ia12[82]
inside leftover n=4 remaining 090 076 020 010); no off-I
tablets. Nested leftover extra remaining-after-009 W 090
076 site ⊆ I W 090 076 sites for each W. The claim is
true. Do not assume; measure. Do not retune.

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
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
)
from tests.test_mamari_i_009_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_009_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE283_ALL_HAPAX,
    STANDING_N_I_ONLY as CYCLE283_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE283_N_NOT_I_ONLY,
    TestMamariI009090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_020010_COVERED,
    STANDING_LEFTOVER_057600_COVERED,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
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
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_009_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE282_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE282_EXTRA_I_SITES,
    STANDING_I_3GRAM_009_090_076_I_ONLY as CYCLE282_CLAIM,
    STANDING_I_SITES as CYCLE282_I_SITES,
    STANDING_N_EXTRA as CYCLE282_N_EXTRA,
    STANDING_N_I as CYCLE282_N_I,
    STANDING_N_OFF_I as CYCLE282_N_OFF_I,
    TestMamariI3gram009090076IOnlyScoreboard,
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
    STANDING_EXTRA_I_SITES as CYCLE245_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_087_I_ONLY as CYCLE245_CLAIM,
    STANDING_N_EXTRA as CYCLE245_N_EXTRA,
    STANDING_N_I as CYCLE245_N_I,
    STANDING_N_OFF_I as CYCLE245_N_OFF_I,
    TestMamariI3gram090076087IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE272_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE272_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_090_076_I_ONLY as CYCLE272_CLAIM,
    STANDING_I_SITES as CYCLE272_I_SITES,
    STANDING_N_EXTRA as CYCLE272_N_EXTRA,
    STANDING_N_I as CYCLE272_N_I,
    STANDING_N_OFF_I as CYCLE272_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE272_OFF_I_SITES,
    TestMamariI3gram090090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_I_SITES as CYCLE167_I_SITES,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    leftover_extra_backward_3grams,
    leftover_extra_previous_4grams,
    leftover_extra_previous_stems,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA_TOTAL,
    STANDING_N_I_ONLY as CYCLE258_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE258_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_prev4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY as CYCLE285_CLAIM,
    STANDING_N_I_ONLY as CYCLE285_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE285_N_NOT_I_ONLY,
    STANDING_REMAINING_PREVIOUS_4GRAMS as CYCLE285_PREVIOUS_4GRAMS,
    leftover_extra_remaining_after_009_continuing_sites,
    leftover_extra_remaining_after_009_line_initial_sites,
    leftover_extra_remaining_after_009_previous_4grams,
    TestMamariILeftoverExtra090076RemainingAfter009Prev4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_prev_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_009,
    STANDING_CYCLE281_009_SITES as CYCLE281_009_SITES,
    STANDING_G as CYCLE284_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE284_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_UNIQUE_PREVIOUS_STEM as CYCLE284_CLAIM,
    STANDING_K as CYCLE284_K,
    STANDING_N_DISTINCT_REMAINING as CYCLE284_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_009 as CYCLE284_N_REMAINING,
    STANDING_REMAINING_PREVIOUS_STEMS as CYCLE284_REMAINING_PREVIOUS_STEMS,
    STANDING_REMAINING_SITES as CYCLE284_REMAINING_SITES,
    i_leftover_extra_090_076_remaining_after_009_unique_previous_stem,
    leftover_extra_remaining_after_009,
    leftover_extra_remaining_after_009_nested_counts_hold,
    leftover_extra_remaining_after_009_previous_stems,
    leftover_extra_remaining_after_009_with_g,
    leftover_extra_remaining_after_009_with_previous,
    leftover_extra_remaining_after_009_without_previous,
    select_remaining_after_009_g,
    TestMamariILeftoverExtra090076RemainingAfter009PrevStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    line_stems_for_site,
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
STANDING_N_LEFTOVER = 56
STANDING_N_REMAINING_AFTER_009 = 27
STANDING_N_DISTINCT_REMAINING = 27
STANDING_REMAINING_SITES = CYCLE284_REMAINING_SITES
STANDING_REMAINING_PREVIOUS_STEMS = CYCLE284_REMAINING_PREVIOUS_STEMS
STANDING_SEQUENCES = tuple(
    (stem, "090", "076") for stem in STANDING_REMAINING_PREVIOUS_STEMS
)
STANDING_PREVIOUS_STEMS = STANDING_REMAINING_PREVIOUS_STEMS
STANDING_LOCKED_3GRAM_STEMS = LOCKED_PREVIOUS_STEMS_AFTER_009
STANDING_ROLES = ("leftover_extra_remaining_after_009",) * STANDING_N_REMAINING_AFTER_009
STANDING_N_I_EACH = (
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1,
)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_I_SITES = (
    ((SIDE_IA, "Ia1", 26),),
    ((SIDE_IA, "Ia1", 58),),
    ((SIDE_IA, "Ia1", 95),),
    ((SIDE_IA, "Ia2", 13),),
    ((SIDE_IA, "Ia2", 158),),
    ((SIDE_IA, "Ia3", 3),),
    ((SIDE_IA, "Ia4", 83),),
    ((SIDE_IA, "Ia4", 120),),
    ((SIDE_IA, "Ia4", 133),),
    ((SIDE_IA, "Ia4", 161),),
    ((SIDE_IA, "Ia4", 165),),
    ((SIDE_IA, "Ia5", 5),),
    ((SIDE_IA, "Ia5", 65), (SIDE_IA, "Ia8", 113)),
    ((SIDE_IA, "Ia5", 126),),
    ((SIDE_IA, "Ia6", 133),),
    ((SIDE_IA, "Ia7", 1),),
    ((SIDE_IA, "Ia7", 136),),
    ((SIDE_IA, "Ia8", 119),),
    ((SIDE_IA, "Ia10", 136),),
    ((SIDE_IA, "Ia10", 140),),
    ((SIDE_IA, "Ia12", 149),),
    ((SIDE_IA, "Ia13", 66),),
    ((SIDE_IA, "Ia12", 82), (SIDE_IA, "Ia13", 134)),
    ((SIDE_IA, "Ia13", 142),),
    ((SIDE_IA, "Ia14", 8),),
    ((SIDE_IA, "Ia14", 96),),
    ((SIDE_IA, "Ia14", 176),),
)
STANDING_LEFTOVER_MATCHING_SITES = tuple(
    (site,) for site in STANDING_REMAINING_SITES
)
STANDING_LEFTOVER_3GRAM_SITES = tuple(
    ((side, line, index - 1),) for side, line, index in STANDING_REMAINING_SITES
)
STANDING_EXTRA_I_SITES = (
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    ((SIDE_IA, "Ia8", 113),),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    ((SIDE_IA, "Ia12", 82),),
    (),
    (),
    (),
    (),
)
STANDING_N_EXTRA_EACH = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
)
STANDING_N_EXTRA_TOTAL = 2
STANDING_WS_WITH_EXTRA = ("000", "008")
STANDING_EXTRA_I_090_076_SITES = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia12", 83),
)
STANDING_I_PREVIOUS_4GRAMS = (
    (("027", "048", "090", "076"),),
    (("380", "380", "090", "076"),),
    (("076", "011", "090", "076"),),
    (("070", "499", "090", "076"),),
    (("050", "497", "090", "076"),),
    (("061", "036", "090", "076"),),
    (("090", "092", "090", "076"),),
    (("087", "291", "090", "076"),),
    (("460", "522", "090", "076"),),
    (("010", "150", "090", "076"),),
    (("087", "078", "090", "076"),),
    (("071", "295", "090", "076"),),
    (("490", "000", "090", "076"), ("607", "000", "090", "076")),
    (("090", "109", "090", "076"),),
    (("055", "052", "090", "076"),),
    (("000", "099", "090", "076"),),
    (("670", "700", "090", "076"),),
    (("076", "161", "090", "076"),),
    (("208", "010", "090", "076"),),
    (("072", "205", "090", "076"),),
    (("071", "382", "090", "076"),),
    (("011", "386", "090", "076"),),
    (("700", "008", "090", "076"), ("727", "008", "090", "076")),
    (("070", "027", "090", "076"),),
    (("724", "724", "090", "076"),),
    (("007", "400", "090", "076"),),
    (("600", "326", "090", "076"),),
)
STANDING_I_NEXT_4GRAMS = (
    (("048", "090", "076", "755"),),
    (("380", "090", "076", "470"),),
    (("011", "090", "076", "430"),),
    (("499", "090", "076", "600"),),
    (("497", "090", "076", "700"),),
    (("036", "090", "076", "070"),),
    (("092", "090", "076", "090"),),
    (("291", "090", "076", "386"),),
    (("522", "090", "076", "001"),),
    (("150", "090", "076", "087"),),
    (None,),
    (("295", "090", "076", "013"),),
    (("000", "090", "076", "071"), ("000", "090", "076", "057")),
    (("109", "090", "076", "505"),),
    (("052", "090", "076", "001"),),
    (("099", "090", "076", "280"),),
    (("700", "090", "076", "607"),),
    (("161", "090", "076", "070"),),
    (("010", "090", "076", "072"),),
    (("205", "090", "076", "000"),),
    (("382", "090", "076", "300"),),
    (("386", "090", "076", "013"),),
    (("008", "090", "076", "020"), ("008", "090", "076", "255")),
    (("027", "090", "076", "700"),),
    (("724", "090", "076", "530"),),
    (("400", "090", "076", "070"),),
    (("326", "090", "076", "670"),),
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_REMAINING_AFTER_009
STANDING_OFF_I_SITES = ((),) * STANDING_N_REMAINING_AFTER_009
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_TWO_ON_I = tuple(
    2 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_HITS_BY_TABLET_TWO_ON_I if n == 2 else STANDING_HITS_BY_TABLET_ONE_ON_I
    for n in STANDING_N_I_EACH
)
STANDING_N_I_ONLY = 27
STANDING_N_NOT_I_ONLY = 0
STANDING_LEAKING_3GRAMS = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_CYCLE281_009_EXCLUDED = True
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_CLAIM = (
    "i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only"
)
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_3GRAMS_ALL_I_ONLY = True
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_3GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_009_3grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167 = False
STANDING_SAME_AS_CYCLE207 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE245 = False
STANDING_SAME_AS_CYCLE258 = False
STANDING_SAME_AS_CYCLE272 = False
STANDING_SAME_AS_CYCLE282 = False
STANDING_SAME_AS_CYCLE284 = False
STANDING_SAME_AS_CYCLE285 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE258 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE272 = True
STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS = True
STANDING_PREVIOUS_STEMS_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_999_090_076_DOES_NOT_COUNT = True
STANDING_600_090_076_DOES_NOT_COUNT = True
STANDING_090_090_076_DOES_NOT_COUNT = True
STANDING_076_090_076_DOES_NOT_COUNT = True
STANDING_071_090_076_DOES_NOT_COUNT = True
STANDING_045_090_076_DOES_NOT_COUNT = True
STANDING_009_090_076_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_ARE_THIS_CYCLE_ONLY_IF_MATCHING_3GRAM = True
STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE = True
STANDING_CYCLE285_N_I_ONLY = 27
STANDING_CYCLE285_N_NOT_I_ONLY = 0
STANDING_CYCLE284_N_REMAINING = 27
STANDING_CYCLE284_K = 1
STANDING_CYCLE284_G = "724"
STANDING_CYCLE284_UNIQUE = False
STANDING_CYCLE283_N_I_ONLY = 2
STANDING_CYCLE283_N_NOT_I_ONLY = 0
STANDING_CYCLE282_N_I = 2
STANDING_CYCLE282_N_OFF_I = 0
STANDING_CYCLE282_N_EXTRA = 0
STANDING_CYCLE258_N_I_ONLY = 19
STANDING_CYCLE258_N_NOT_I_ONLY = 0
STANDING_CYCLE258_N_EXTRA = 3
STANDING_CYCLE245_N_I = 5
STANDING_CYCLE245_N_OFF_I = 0
STANDING_CYCLE245_N_EXTRA = 3
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3
STANDING_CYCLE272_N_I = 3
STANDING_CYCLE272_N_OFF_I = 1
STANDING_CYCLE167_N_I = 16
STANDING_CYCLE167_N_OFF_I = 0


def remaining_after_009_3grams(
    remaining_stems: tuple[str, ...] = STANDING_REMAINING_PREVIOUS_STEMS,
) -> tuple[tuple[str, ...], ...]:
    """3-grams W 090 076 for leftover extra remaining-after-009 previous stems."""
    return tuple((stem, "090", "076") for stem in remaining_stems)


def leftover_extra_090_076_site_for_3gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """090 076 starts one token after W 090 076."""
    side, line, index = site
    return (side, line, index + 1)


def leftover_extra_remaining_after_009_3gram_sites(
    leftover_matching: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-009 090-starts shifted to W-starts."""
    return tuple((side, line, index - 1) for side, line, index in leftover_matching)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_REMAINING_AFTER_009,
) -> bool:
    """True iff every remaining-after-009 3-gram is I-only.

    Extra I does not make the claim lose. Length must stay 27.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


def leftover_extra_remaining_after_009_3gram_subset(
    leftover_site: tuple[str, str, int],
    i_sites: tuple[tuple[str, str, int], ...],
) -> bool:
    """True iff leftover extra remaining-after-009 W-start ⊆ I W 090 076."""
    return leftover_extra_remaining_after_009_3gram_sites((leftover_site,))[0] in i_sites


def leftover_extra_remaining_after_009_3grams_subset_all(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites_each: tuple[tuple[tuple[str, str, int], ...], ...],
) -> bool:
    """True iff every remaining-after-009 site sits in its I 3-gram sites."""
    if len(leftover_sites) != len(i_sites_each):
        return False
    return all(
        leftover_extra_remaining_after_009_3gram_subset(site, sites)
        for site, sites in zip(leftover_sites, i_sites_each, strict=True)
    )


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...],
    leftover_matching: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """I W 090 076 sites that are not leftover extra remaining-after-009."""
    leftover_set = set(leftover_matching)
    return tuple(
        site
        for site in i_sites
        if leftover_extra_090_076_site_for_3gram(site) not in leftover_set
    )


def site_next_4gram_for_3gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...],
) -> tuple[str, ...] | None:
    """W 090 076 Y if a following stem exists; None at end-of-line."""
    if tuple(stems[index : index + len(gram3)]) != gram3:
        return None
    if index + len(gram3) >= len(stems):
        return None
    return tuple(stems[index : index + len(gram3) + 1])


class TestILeftoverExtra090076RemainingAfter0093gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-009 3-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. Locked 999/009 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("048", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[12], ("000", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[22], ("008", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[24], ("724", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("326", "090", "076"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_REMAINING_AFTER_009)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_REMAINING_AFTER_009)
        self.assertEqual(remaining_after_009_3grams(), STANDING_SEQUENCES)
        for gram, prev in zip(STANDING_SEQUENCES, STANDING_PREVIOUS_STEMS, strict=True):
            self.assertEqual(gram[1:], GRAM2)
            self.assertEqual(gram[0], prev)
            self.assertEqual(len(gram), STANDING_N3)
            self.assertNotIn(prev, STANDING_LOCKED_3GRAM_STEMS)
            self.assertNotEqual(gram, CYCLE167_GRAM3)
            self.assertNotEqual(gram, CYCLE207_GRAM3)
            self.assertNotEqual(gram, CYCLE245_GRAM3)
            self.assertNotEqual(gram, CYCLE272_GRAM3)
            self.assertNotEqual(gram, CYCLE282_GRAM3)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["048", "090", "076", "048", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:1]) + ["006"] + list(STANDING_SEQUENCES[0][1:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE272_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["999", "090", "076"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["009", "090", "076"]], STANDING_SEQUENCES[0]), 0)
        planted = ["027", "048", "090", "076"]
        self.assertEqual(site_previous_stem(planted, 2, GRAM2), "048")
        self.assertEqual(site_backward_3gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_previous_4gram(planted, 2, GRAM2), ("027", "048", "090", "076"))
        no_prev = ["090", "076", "012"]
        self.assertIsNone(site_previous_stem(no_prev, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(no_prev, 0, GRAM2))
        self.assertTrue(STANDING_999_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_009_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_090_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_3gram(self):
        """Boolean is True only when all remaining-after-009 3-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
                hold_ones,
                hold_zeros,
            )
        )
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
                (3,) + hold_ones[1:],
                hold_zeros,
            )
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
                hold_ones,
                tuple(lose_off),
            )
        )
        lose_off_mid = list(hold_zeros)
        lose_off_mid[24] = 1
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
                hold_ones,
                tuple(lose_off_mid),
            )
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
                tuple(lose_missing_i),
                hold_zeros,
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only((), ())
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
                hold_ones[:-1],
                hold_zeros[:-1],
            )
        )
        self.assertTrue(STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertEqual(STANDING_N_EXTRA_TOTAL, 2)
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_3GRAMS_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_3GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertFalse(CYCLE272_GRAM3[0] in STANDING_PREVIOUS_STEMS)
        self.assertEqual(CYCLE272_N_I, 3)
        self.assertEqual(CYCLE272_N_OFF_I, 1)
        self.assertFalse(CYCLE272_CLAIM)
        self.assertTrue(CYCLE245_CLAIM)
        self.assertEqual(CYCLE245_N_EXTRA, 3)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertEqual(CYCLE258_N_EXTRA_TOTAL, 3)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_be_nonempty(self):
        """Remaining-after-009 W-start ⊆ I sites; extra I can be nonempty."""
        provider = MockProvider()
        self.assertTrue(
            leftover_extra_remaining_after_009_3grams_subset_all(
                STANDING_REMAINING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(STANDING_N_EXTRA_EACH[12], 1)
        self.assertEqual(STANDING_N_EXTRA_EACH[22], 1)
        self.assertEqual(sum(STANDING_N_EXTRA_EACH), STANDING_N_EXTRA_TOTAL)
        self.assertEqual(
            extra_i_sites(STANDING_I_SITES[12], STANDING_LEFTOVER_MATCHING_SITES[12]),
            STANDING_EXTRA_I_SITES[12],
        )
        self.assertEqual(
            extra_i_sites(STANDING_I_SITES[22], STANDING_LEFTOVER_MATCHING_SITES[22]),
            STANDING_EXTRA_I_SITES[22],
        )
        self.assertEqual(STANDING_EXTRA_I_SITES[12], ((SIDE_IA, "Ia8", 113),))
        self.assertEqual(STANDING_EXTRA_I_SITES[22], ((SIDE_IA, "Ia12", 82),))
        self.assertEqual(
            leftover_extra_090_076_site_for_3gram(STANDING_EXTRA_I_SITES[12][0]),
            STANDING_EXTRA_I_090_076_SITES[0],
        )
        self.assertEqual(
            leftover_extra_090_076_site_for_3gram(STANDING_EXTRA_I_SITES[22][0]),
            STANDING_EXTRA_I_090_076_SITES[1],
        )
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[0], CYCLE224_INSIDE_SITES)
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[0], STANDING_LEFTOVER_057600_COVERED)
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[1], CYCLE224_INSIDE_SITES)
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[1], STANDING_LEFTOVER_020010_COVERED)
        planted_extra = STANDING_REMAINING_SITES + ((SIDE_IA, "Ia1", 1),)
        self.assertFalse(
            leftover_extra_remaining_after_009_3grams_subset_all(
                planted_extra,
                STANDING_I_SITES,
            )
        )
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter0093gramsIOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-009 3-gram off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.previous_stems = leftover_extra_previous_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.leftover_previous_4grams = leftover_extra_previous_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.backwards = leftover_extra_backward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.remaining = leftover_extra_remaining_after_009(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_extra_remaining_after_009_previous_stems(
            self.leftover_sites,
            self.previous_stems,
        )
        self.grams = remaining_after_009_3grams(self.remaining_stems)
        self.per_site_previous_4grams = leftover_extra_remaining_after_009_previous_4grams(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.line_initial = leftover_extra_remaining_after_009_line_initial_sites(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.continuing = leftover_extra_remaining_after_009_continuing_sites(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
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
        self.leftover_matching = tuple(
            leftover_extra_remaining_after_009_with_g(
                self.leftover_sites,
                self.previous_stems,
                stem,
            )
            for stem in self.remaining_stems
        )
        self.extra = tuple(
            extra_i_sites(sites, matching)
            for sites, matching in zip(
                self.i_sites,
                self.leftover_matching,
                strict=True,
            )
        )
        self.n_extra = tuple(len(row) for row in self.extra)
        self.g, self.k, self.unique = select_remaining_after_009_g(
            self.remaining_stems
        )
        self.unique_max = i_leftover_extra_090_076_remaining_after_009_unique_previous_stem(
            self.leftover_sites,
            self.previous_stems,
        )
        self.claim_holds = (
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
                self.n_i,
                self.n_off_i,
            )
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = len(self.grams) - self.n_i_only
        self.leaking = tuple(
            gram
            for gram, on, off in zip(self.grams, self.n_i, self.n_off_i, strict=True)
            if not sequence_is_i_only(on, off)
        )

    def test_tokens_and_sites_are_cycle_284_remaining_after_009_not_retuned(self):
        """3-grams stay the cycle-284 remaining-after-009 W. Nested 27/K=1/G=724 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(self.leftover_sites), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE284_REMAINING_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(len(self.remaining), STANDING_N_REMAINING_AFTER_009)
        self.assertEqual(STANDING_N_REMAINING_AFTER_009, 27)
        self.assertEqual(self.g, CYCLE284_G)
        self.assertEqual(self.g, "724")
        self.assertEqual(self.k, CYCLE284_K)
        self.assertEqual(self.k, 1)
        self.assertFalse(self.unique)
        self.assertFalse(CYCLE284_UNIQUE)
        self.assertFalse(self.unique_max)
        self.assertFalse(CYCLE284_CLAIM)
        if (
            len(self.remaining) != 27
            or self.k != 1
            or self.g != "724"
            or self.unique
            or self.unique_max
        ):
            self.fail("nested cycle 284 unique-max false N_remaining_after_009=27 K=1 G=724 drifted")
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.per_site_previous_4grams, CYCLE285_PREVIOUS_4GRAMS)
        self.assertEqual(self.line_initial, ())
        self.assertEqual(len(self.grams), STANDING_N_REMAINING_AFTER_009)
        self.assertTrue(all(stem is not None for stem in self.remaining_stems))
        self.assertTrue(all(gram is not None for gram in self.per_site_previous_4grams))
        for site in CYCLE281_009_SITES:
            self.assertNotIn(site, self.remaining)
        self.assertTrue(
            leftover_extra_remaining_after_009_nested_counts_hold(
                69,
                56,
                15,
                41,
                4,
                37,
                2,
                27,
            )
        )
        for prev in self.remaining_stems:
            self.assertNotIn(prev, LOCKED_PREVIOUS_STEMS_AFTER_009)
        prior_285 = self.survey["i_leftover_extra_090_076_remaining_after_009_prev4_i_only"]
        self.assertEqual(prior_285["cycle"], 285)
        self.assertEqual(prior_285["N_i_only"], 27)
        self.assertEqual(prior_285["N_not_i_only"], 0)
        self.assertTrue(prior_285["i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only"])
        self.assertTrue(CYCLE285_CLAIM)
        self.assertEqual(CYCLE285_N_I_ONLY, 27)
        self.assertEqual(CYCLE285_N_NOT_I_ONLY, 0)
        prior_284 = self.survey["i_leftover_extra_090_076_remaining_after_009_previous_stem"]
        self.assertEqual(prior_284["cycle"], 284)
        self.assertEqual(prior_284["N_remaining_after_009"], 27)
        self.assertEqual(prior_284["K"], 1)
        self.assertEqual(prior_284["G"], "724")
        self.assertFalse(prior_284["G_uniquely_most_frequent"])
        self.assertFalse(prior_284["i_leftover_extra_090_076_remaining_after_009_unique_previous_stem"])
        prior_283 = self.survey["i_009_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_283["cycle"], 283)
        self.assertEqual(prior_283["N_i_only"], 2)
        self.assertEqual(prior_283["N_not_i_only"], 0)
        prior_282 = self.survey["i_3gram_009_090_076_i_only"]
        self.assertEqual(prior_282["cycle"], 282)
        self.assertEqual(prior_282["N_I"], 2)
        self.assertEqual(prior_282["N_off_I"], 0)
        self.assertEqual(prior_282["N_extra"], 0)
        prior_258 = self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]
        self.assertEqual(prior_258["cycle"], 258)
        self.assertEqual(prior_258["N_i_only"], 19)
        self.assertEqual(prior_258["N_not_i_only"], 0)
        self.assertEqual(prior_258["N_extra_total"], 3)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        prior_272 = self.survey["i_3gram_090_090_076_i_only"]
        self.assertEqual(prior_272["cycle"], 272)
        self.assertEqual(prior_272["N_I"], 3)
        self.assertEqual(prior_272["N_off_I"], 1)
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_3gram_lock_extra_i_and_claim_holds(self):
        """Each remaining-after-009 3-gram is I-only. Extra I=2 does not lose."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.n_extra, STANDING_N_EXTRA_EACH)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(sum(self.n_extra), STANDING_N_EXTRA_TOTAL)
        self.assertEqual(STANDING_N_EXTRA_TOTAL, 2)
        self.assertEqual(self.leaking, STANDING_LEAKING_3GRAMS)
        self.assertEqual(self.leaking, ())
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_i_only, 27)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_not_i_only, 0)
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from 0")
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked remaining-after-009 3-grams")
        if self.leaking:
            self.fail("measured remaining-after-009 3-grams leaked off I")
        if self.extra != STANDING_EXTRA_I_SITES:
            self.fail("extra I leftover-of-leftover sites drifted")
        self.assertTrue(
            leftover_extra_remaining_after_009_3grams_subset_all(
                self.remaining,
                self.i_sites,
            )
        )
        for site, gram, prev, role, sites, matching, extra, n_on, n_off, n_ex, prevs, nexts in zip(
            STANDING_REMAINING_SITES,
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_EXTRA_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_N_EXTRA_EACH,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(matching, (site,))
            w_start = leftover_extra_remaining_after_009_3gram_sites((site,))[0]
            self.assertIn(w_start, sites)
            self.assertEqual(extra_i_sites(sites, matching), extra)
            self.assertEqual(len(extra), n_ex)
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] - 1 : site[2] + STANDING_N2]), gram)
            self.assertEqual(stems[site[2] - 1], prev)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N2]), GRAM2)
            self.assertEqual(site_backward_3gram(stems, site[2], GRAM2), gram)
            self.assertNotIn(prev, LOCKED_PREVIOUS_STEMS_AFTER_009)
            self.assertEqual(role, "leftover_extra_remaining_after_009")
            self.assertGreaterEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            for i_site, prev4, nxt4 in zip(sites, prevs, nexts, strict=True):
                line = line_stems_for_site(self.i_sides, i_site)
                idx = i_site[2]
                self.assertEqual(tuple(line[idx : idx + STANDING_N3]), gram)
                self.assertEqual(tuple(line[idx - 1 : idx + STANDING_N3]), prev4)
                self.assertEqual(site_next_4gram_for_3gram(line, idx, gram), nxt4)
                if i_site != w_start:
                    gram2_site = leftover_extra_090_076_site_for_3gram(i_site)
                    self.assertIn(gram2_site, CYCLE224_INSIDE_SITES)
                    self.assertNotIn(gram2_site, STANDING_LEFTOVER_SITES)
        self.assertEqual(STANDING_WS_WITH_EXTRA, ("000", "008"))
        self.assertIn((SIDE_IA, "Ia8", 114), CYCLE224_INSIDE_SITES)
        self.assertIn((SIDE_IA, "Ia8", 114), STANDING_LEFTOVER_057600_COVERED)
        self.assertIn((SIDE_IA, "Ia12", 83), CYCLE224_INSIDE_SITES)
        self.assertIn((SIDE_IA, "Ia12", 83), STANDING_LEFTOVER_020010_COVERED)
        self.assertIn(("090", "076", "057", "600"), CYCLE222_MATCHING)
        self.assertIn(("090", "076", "020", "010"), CYCLE222_MATCHING)
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        if not self.claim_holds:
            self.fail("measured remaining-after-009 3-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off, n_on in zip(self.hits_by_tablet, self.off_i, self.n_i, strict=True):
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
            self.assertEqual(hits[VENDORED_TABLETS.index("I")], n_on)
            self.assertEqual(sum(hits) - n_on, 0)
        t_sides = load_t_sides()
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
            if index >= 1:
                t_prev = (stems[index - 1], "090", "076")
                self.assertNotIn(t_prev, STANDING_SEQUENCES)
        self.assertEqual(CYCLE272_OFF_I_SITES, ((SIDE_TA, "Ta5", 8),))
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(
            i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only(
                self.n_i,
                self.n_off_i,
            ),
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_3GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE281_009_EXCLUDED)
        self.assertFalse(STANDING_SAME_AS_CYCLE207)
        self.assertFalse(STANDING_SAME_AS_CYCLE245)
        self.assertFalse(STANDING_SAME_AS_CYCLE258)
        self.assertFalse(STANDING_SAME_AS_CYCLE272)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE258)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE272)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_285_284_283_282_258_223_272_and_167_still_compute(self):
        """Cycle 285 27/27, 284 unique-max lose 27/K=1/G=724, 283 2/0, 282 2/0, 258 19/19 extra I=3, 223 69/3, 272 3/1, 167 16/0 stay."""
        prior_285 = TestMamariILeftoverExtra090076RemainingAfter009Prev4IOnlyScoreboard()
        prior_285.setUp()
        prior_285.test_each_4gram_is_one_on_i_zero_off_i_no_line_initial_and_claim_holds()
        prior_285.test_survey_matches_computed_lock()
        self.assertEqual(prior_285.n_i_only, 27)
        self.assertEqual(prior_285.n_not_i_only, 0)
        self.assertTrue(prior_285.claim_holds)
        self.assertTrue(CYCLE285_CLAIM)
        if prior_285.n_i_only != 27 or prior_285.n_not_i_only != 0:
            self.fail("nested cycle 285 remaining-after-009 previous 4-grams 27/27 hapax drifted")
        prior_284 = TestMamariILeftoverExtra090076RemainingAfter009PrevStemScoreboard()
        prior_284.setUp()
        prior_284.test_counts_27_remaining_all_hapax_g_724_k_1_and_hypothesis_loses()
        prior_284.test_survey_matches_computed_lock()
        self.assertEqual(prior_284.n_remaining, 27)
        self.assertEqual(prior_284.k, 1)
        self.assertEqual(prior_284.g, "724")
        self.assertFalse(prior_284.unique)
        self.assertFalse(prior_284.claim_holds)
        self.assertFalse(CYCLE284_CLAIM)
        if (
            prior_284.n_remaining != 27
            or prior_284.k != 1
            or prior_284.g != "724"
            or prior_284.unique
        ):
            self.fail("nested cycle 284 unique-max false N_remaining_after_009=27 K=1 G=724 drifted")
        prior_283 = TestMamariI009090076Previous4gramsIOnlyScoreboard()
        prior_283.setUp()
        prior_283.test_all_4grams_are_i_only_hapax_and_claim_holds()
        prior_283.test_survey_matches_computed_lock()
        self.assertEqual(prior_283.n_i_only, 2)
        self.assertEqual(prior_283.n_not_i_only, 0)
        self.assertTrue(prior_283.claim_holds)
        self.assertTrue(CYCLE283_ALL_HAPAX)
        if prior_283.n_i_only != 2 or prior_283.n_not_i_only != 0:
            self.fail("nested cycle 283 2/0 hapax drifted")
        prior_282 = TestMamariI3gram009090076IOnlyScoreboard()
        prior_282.setUp()
        prior_282.test_i_hits_are_two_on_ia_and_leftover_extra_009_is_subset()
        prior_282.test_3gram_is_zero_off_i_and_i_only()
        prior_282.test_survey_matches_computed_lock()
        self.assertEqual(prior_282.i_hits, CYCLE282_N_I)
        self.assertEqual(prior_282.off_i_hits, CYCLE282_N_OFF_I)
        self.assertEqual(len(prior_282.extra), CYCLE282_N_EXTRA)
        self.assertTrue(prior_282.claim_holds)
        self.assertTrue(CYCLE282_CLAIM)
        if prior_282.i_hits != 2 or prior_282.off_i_hits != 0 or prior_282.extra:
            self.fail("nested cycle 282 009 090 076 I-only 2/0 extra I=0 drifted")
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_258.test_survey_matches_computed_lock()
        self.assertEqual(prior_258.n_i_only, 19)
        self.assertEqual(prior_258.n_not_i_only, 0)
        self.assertEqual(sum(prior_258.n_extra), 3)
        self.assertTrue(prior_258.claim_holds)
        self.assertTrue(CYCLE258_CLAIM)
        if prior_258.n_i_only != 19 or prior_258.n_not_i_only != 0 or sum(prior_258.n_extra) != 3:
            self.fail("nested cycle 258 remaining-after-000 3-grams 19/19 extra I=3 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, CYCLE223_N_I)
        self.assertEqual(prior_223.off_i_hits, CYCLE223_N_OFF_I)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        self.assertEqual(len(CYCLE223_I_SITES), 69)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_272 = TestMamariI3gram090090076IOnlyScoreboard()
        prior_272.setUp()
        prior_272.test_3gram_is_one_off_i_and_not_i_only()
        prior_272.test_survey_matches_computed_lock()
        self.assertEqual(prior_272.i_hits, CYCLE272_N_I)
        self.assertEqual(prior_272.off_i_hits, CYCLE272_N_OFF_I)
        self.assertEqual(prior_272.off_i_sites, CYCLE272_OFF_I_SITES)
        self.assertEqual(len(prior_272.extra), CYCLE272_N_EXTRA)
        self.assertFalse(prior_272.claim_holds)
        self.assertFalse(CYCLE272_CLAIM)
        if prior_272.i_hits != 3 or prior_272.off_i_hits != 1:
            self.fail("nested cycle 272 090 090 076 leak 3/1 drifted")
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, CYCLE167_N_I)
        self.assertEqual(prior_167.off_i_hits, CYCLE167_N_OFF_I)
        self.assertEqual(prior_167.i_sites, CYCLE167_I_SITES)
        self.assertTrue(prior_167.claim_holds)
        self.assertTrue(CYCLE167_CLAIM)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_sites, CYCLE207_OFF_I_SITES)
        self.assertFalse(prior_207.claim_holds)
        prior_245 = TestMamariI3gram090076087IOnlyScoreboard()
        prior_245.setUp()
        prior_245.test_3gram_is_zero_off_i_and_i_only()
        prior_245.test_survey_matches_computed_lock()
        self.assertEqual(prior_245.i_hits, CYCLE245_N_I)
        self.assertEqual(prior_245.off_i_hits, CYCLE245_N_OFF_I)
        self.assertEqual(len(prior_245.extra), CYCLE245_N_EXTRA)
        self.assertTrue(prior_245.claim_holds)
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
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-286 remaining-after-009 3-gram I-only lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_009_3grams_i_only"]
        self.assertEqual(lock["cycle"], 286)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(lock["N_remaining_after_009"], STANDING_N_REMAINING_AFTER_009)
        self.assertEqual(lock["N_remaining_after_009"], 27)
        self.assertEqual(lock["N_distinct_remaining"], STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(lock["K"], 1)
        self.assertEqual(lock["G"], "724")
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertFalse(lock["i_leftover_extra_090_076_remaining_after_009_unique_previous_stem"])
        self.assertEqual(
            tuple(lock["locked_previous_stems_after_009"]),
            LOCKED_PREVIOUS_STEMS_AFTER_009,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_009_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_009_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["remaining_after_009_3grams"],
        )
        self.assertTrue(lock["cycle281_009_excluded"])
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_REMAINING_AFTER_009)
        for row, gram, site, prev, role, sites, matching, extra, n_on, n_off, n_ex, prevs, nexts in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_REMAINING_SITES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_EXTRA_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_N_EXTRA_EACH,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens3"]), gram)
            self.assertEqual(tuple(row["cycle284_site"]), site)
            self.assertEqual(row["previous_stem"], prev)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["ia_hits"], n_on)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["leftover_extra_remaining_after_009_sites"]),
                matching,
            )
            self.assertTrue(row["leftover_extra_remaining_after_009_subset_of_i_sites"])
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["extra_i_sites"]),
                extra,
            )
            self.assertEqual(row["N_extra"], n_ex)
            self.assertEqual(
                [list(gram4) for gram4 in prevs],
                row["i_previous_4grams"],
            )
            self.assertEqual(
                [list(gram4) if gram4 is not None else None for gram4 in nexts],
                row["i_next_4grams"],
            )
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(row["off_i_tablets_with_hits"], [])
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertTrue(row["i_only"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(tuple(lock["N_extra_each"]), STANDING_N_EXTRA_EACH)
        self.assertEqual(lock["N_extra_total"], 2)
        self.assertEqual(tuple(lock["ws_with_extra"]), STANDING_WS_WITH_EXTRA)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only"]
        )
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_009_3grams_i_only"]
        )
        self.assertEqual(lock["N_i_only"], 27)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["leaking_3grams"], [])
        self.assertEqual(lock["off_i_tablets_with_hits"], [])
        self.assertTrue(lock["extra_i_does_not_make_claim_lose"])
        self.assertEqual(lock["nested_cycle285_N_i_only"], 27)
        self.assertEqual(lock["nested_cycle285_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle284_N_remaining_after_009"], 27)
        self.assertEqual(lock["nested_cycle284_K"], 1)
        self.assertEqual(lock["nested_cycle284_G"], "724")
        self.assertFalse(lock["nested_cycle284_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle283_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle283_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle282_N_I"], 2)
        self.assertEqual(lock["nested_cycle282_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle282_N_extra"], 0)
        self.assertEqual(lock["nested_cycle258_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle258_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle258_N_extra_total"], 3)
        self.assertEqual(lock["nested_cycle245_N_I"], 5)
        self.assertEqual(lock["nested_cycle245_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle245_N_extra"], 3)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle272_N_I"], 3)
        self.assertEqual(lock["nested_cycle272_N_off_I"], 1)
        self.assertEqual(tuple(lock["nested_cycle272_off_i_sites"][0]), CYCLE272_OFF_I_SITES[0])
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167"])
        self.assertFalse(lock["same_as_cycle207"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle245"])
        self.assertFalse(lock["same_as_cycle258"])
        self.assertFalse(lock["same_as_cycle272"])
        self.assertFalse(lock["same_as_cycle282"])
        self.assertFalse(lock["same_as_cycle284"])
        self.assertFalse(lock["same_as_cycle285"])
        self.assertTrue(lock["same_claim_shape_as_cycle207"])
        self.assertTrue(lock["same_claim_shape_as_cycle245"])
        self.assertTrue(lock["same_claim_shape_as_cycle258"])
        self.assertTrue(lock["same_claim_shape_as_cycle272"])
        self.assertTrue(lock["do_not_peel_leftover_extra_i_previous_stems"])
        self.assertTrue(lock["previous_stems_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["999_090_076_does_not_count"])
        self.assertTrue(lock["600_090_076_does_not_count"])
        self.assertTrue(lock["090_090_076_does_not_count"])
        self.assertTrue(lock["076_090_076_does_not_count"])
        self.assertTrue(lock["071_090_076_does_not_count"])
        self.assertTrue(lock["045_090_076_does_not_count"])
        self.assertTrue(lock["009_090_076_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_are_this_cycle_only_if_matching_3gram"])
        self.assertTrue(lock["raw_stems_090_kept"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_009_prev4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_009_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_009_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_009_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_3gram_090_076_087_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_prev4_i_only"]["cycle"],
            285,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_previous_stem"]["cycle"],
            284,
        )
        self.assertEqual(self.survey["i_3gram_009_090_076_i_only"]["cycle"], 282)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]["cycle"],
            258,
        )
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["cycle"], 272)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter0093gramsIOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 286 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
