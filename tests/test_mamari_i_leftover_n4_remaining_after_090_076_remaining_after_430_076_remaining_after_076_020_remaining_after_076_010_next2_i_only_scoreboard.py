"""I's leftover n=4 remaining remaining-after-090-076 remaining-after-430-076 remaining-after-076-020 remaining-after-076-010 leftover 4-gram next-2-grams I-only lock.

Cycle 375 text-search lock. Uses already-vendored A–V and the
cycle-340 leftover n=4 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 remaining-
after-076-010 leftover matching sites of the five leftover
4-grams (N=11). Next 2-gram = the two tokens immediately
after leftover matching leftover 4-gram ends. This is a
different window from cycle 349 leftover 2-grams of leftover
4-grams (tokens IN leftover 4-grams), from cycle 351 previous
2-grams (previous stem plus first leftover token), from cycle
370 next 1-grams (single next token), and from extra-I next-1-
gram 2-grams of I-only / leaking next 1-grams (cycles 371–
372). Does not retune leftover 4-gram I-only (cycle 340 extra
I=0), leftover 2-gram I-only LOSE (cycle 349 9/6 extra I=116),
previous 2-gram I-only LOSE (cycle 351 7/4 extra I=16), leftover
1-gram / previous 1-gram / next 1-gram peels, extra-I leftover-1
/ previous-1 / next-1 peels, unique next stem unique_max false
G=760 labeling only (cycle 343; do not peel labeled G with
exactly-1-share), or forward 5-grams (cycle 344 hapax 11/0 extra
I=0). Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Unpublished Ib is 0. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning dictionary.

Population (locked, do not re-derive as a new claim): leftover
n=4 remaining remaining-after-090-076 remaining-after-430-076
remaining-after-076-020 remaining-after-076-010 leftover 4-grams
that do not contain 090 076 (N=11 leftover matching sites).
Next-1-gram peel of leftover 4-grams is closed (cycle 370 LOSE
N_i_only=2 N_leak=9 extra I=772; cycles 371–374 extra-I next-1
peels stay nested). Leftover 2-grams, previous 2-grams, leftover
1-grams, previous 1-grams, and next 1-grams are already nested.
This cycle is the skipped analog of leftover 2-grams / previous
2-grams for the two tokens after leftover 4-gram ends.

Already locked (record overlap only, do not re-lock): nested
leftover 4-gram I-only extra I=0, leftover 2-gram I-only LOSE,
previous 2-gram I-only LOSE, leftover 1-gram / previous 1-gram /
next 1-gram peels, extra-I leftover-1-gram peels of I-only
leftover 1-grams HOLD, extra-I previous-1-gram 2-grams of I-only
previous 1-grams HOLD, extra-I next-1-gram 2-grams of I-only
next 1-grams HOLD extra I of the 2-grams=0, and extra-I leaking
leftover-1 / previous-1 / next-1 peels stay nested.

Same claim-shape as cycle 370 leftover remaining-after-076-010
next 1-grams of leftover 4-grams I-only LOSE and cycle 349
leftover 2-grams of leftover 4-grams I-only LOSE. A leftover
4-gram / leftover 2-gram / previous 2-gram / next 1-gram lock
does NOT imply the two tokens after leftover matching leftover
4-gram ends are I-only (that 2-gram can appear elsewhere,
including off I). That is the claim that can lose. Extra I ≠ 0
does not make the claim lose (still I-only); still lock extra I.
Do not peel labeled G with exactly-1-share.

Locks exact consecutive hits of each leftover remaining-after-
076-010 next 2-gram on tablet I and on every other vendored
tablet A–H and J–V. The eleven next 2-grams in leftover-
matching-site order: 295 076 / 002 076 / 071 076 / 460 050 /
000 700 / 076 600 / 760 036 / 022 280 / 048 700 / 720 076 /
177 700. Claim that can lose:
i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only.
True iff leftover matching sites still compute as those 11,
every leftover matching site has two following tokens so the
2-gram set is complete relative to N=11 (N_with_next2=11
N_no_next2=0), and every such 2-gram has N_I ≥ 1 and N_off_I = 0
(N_leak=0 per 2-gram). Incomplete-set relative to N=11 is LOSE
if any site lacks two following tokens. HOLD requires every next
2-gram to have N_off_I=0 / N_leak=0. Extra I ≠ 0 does not make
the claim lose. Measured: 295 076 N_I=1 N_off_I=0 extra I=0
hapax leftover matching Ia1[140]; 002 076 N_I=11 N_off_I=3 extra
I=10 leftover matching Ia4[129] leak G; 071 076 N_I=21 N_off_I=0
extra I=20 leftover matching Ia14[82]; 460 050 N_I=1 N_off_I=0
extra I=0 hapax leftover matching Ia1[67]; 000 700 N_I=1
N_off_I=3 extra I=0 leftover matching Ia9[7] leak O/S; 076 600
N_I=16 N_off_I=1 extra I=15 leftover matching Ia6[52] leak G;
760 036 N_I=1 N_off_I=0 extra I=0 hapax leftover matching
Ia12[123]; 022 280 N_I=1 N_off_I=1 extra I=0 leftover matching
Ia8[34] leak C; 048 700 N_I=1 N_off_I=5 extra I=0 leftover
matching Ia10[148] leak G/H/P/Q; 720 076 N_I=5 N_off_I=0 extra
I=4 leftover matching Ia8[171]; 177 700 N_I=1 N_off_I=0 extra
I=0 hapax leftover matching Ia9[36]. Leftover matching leftover
4-gram sites remain 11. Leftover matching next-2-gram sites are
11. Extra I of the next 2-grams is 49. N_i_only=6, N_leak=5
(0 hit T), N_hapax=4, N_with_next2=11, N_no_next2=0, leftover
matching leftover-2=0 leftover matching next-2=0, Ib unpublished
0. The claim is false. Do not retune.

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
from tests.test_mamari_i_2gram_076_010_i_only_scoreboard import (
    GRAM2 as CYCLE337_GRAM2,
    STANDING_I_2GRAM_076_010_I_ONLY as CYCLE337_CLAIM,
    STANDING_N_I as CYCLE337_N_I,
    STANDING_N_OFF_I as CYCLE337_N_OFF_I,
    TestMamariI2gram076010IOnlyScoreboard,
    i_2gram_076_010_i_only,
)
from tests.test_mamari_i_2gram_076_020_i_only_scoreboard import (
    STANDING_I_2GRAM_076_020_I_ONLY as CYCLE334_CLAIM,
    STANDING_N_I as CYCLE334_N_I,
    STANDING_N_OFF_I as CYCLE334_N_OFF_I,
    TestMamariI2gram076020IOnlyScoreboard,
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
    i_2gram_090_076_i_only,
)
from tests.test_mamari_i_2gram_430_076_i_only_scoreboard import (
    STANDING_I_2GRAM_430_076_I_ONLY as CYCLE330_CLAIM,
    STANDING_N_I as CYCLE330_N_I,
    STANDING_N_OFF_I as CYCLE330_N_OFF_I,
    TestMamariI2gram430076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_1grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_1GRAMS_ALL_I_ONLY as CYCLE358_CLAIM,
    STANDING_N_EXTRA as CYCLE358_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE358_N_I_ONLY,
    STANDING_N_LEAK as CYCLE358_N_LEAK,
    STANDING_SEQUENCES as CYCLE358_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760101gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_2grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_2GRAMS_ALL_I_ONLY as CYCLE349_CLAIM,
    STANDING_N_EXTRA as CYCLE349_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE349_N_I_ONLY,
    STANDING_N_LEAK as CYCLE349_N_LEAK,
    STANDING_SEQUENCES as CYCLE349_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760102gramsIOnlyScoreboard,
    leftover_matching_2gram_sites_each,
    leftover_remaining_2grams,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_4GRAMS_ALL_I_ONLY as CYCLE340_CLAIM,
    STANDING_LEFTOVER_MATCHING_4GRAMS as CYCLE340_MATCHING_4GRAMS,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE340_LEFTOVER_MATCHING,
    STANDING_N as CYCLE340_N,
    STANDING_N_EXTRA as CYCLE340_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE340_N_I_ONLY,
    STANDING_SEQUENCES as CYCLE340_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760104gramsIOnlyScoreboard,
    leftover_matching_4gram_sites,
    leftover_remaining_grams,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_leak_next1_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_EXTRA_I_LEAK_NEXT1_4GRAMS_ALL_I_ONLY as CYCLE374_CLAIM,
    STANDING_N_LEAK as CYCLE374_N_LEAK,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraILeakNext14gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_next1_2grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_EXTRA_I_NEXT1_2GRAMS_ALL_I_ONLY as CYCLE371_CLAIM,
    STANDING_N_EXTRA as CYCLE371_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE371_N_I_ONLY,
    STANDING_N_LEAK as CYCLE371_N_LEAK,
    STANDING_SEQUENCES as CYCLE371_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraINext12gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_prev1_2grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_EXTRA_I_PREV1_2GRAMS_ALL_I_ONLY as CYCLE361_CLAIM,
    STANDING_N_EXTRA as CYCLE361_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE361_N_I_ONLY,
    STANDING_N_LEAK as CYCLE361_N_LEAK,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_fwd5_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_FORWARD_5GRAMS_ALL_I_ONLY as CYCLE344_CLAIM,
    STANDING_N_I_ONLY as CYCLE344_N_I_ONLY,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Fwd5IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next1_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT_1GRAMS_ALL_I_ONLY as CYCLE370_CLAIM,
    STANDING_LEFTOVER_MATCHING_NEXT1_SITES as CYCLE370_NEXT1_SITES,
    STANDING_N_EXTRA as CYCLE370_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE370_N_I_ONLY,
    STANDING_N_LEAK as CYCLE370_N_LEAK,
    STANDING_N_NO_NEXT as CYCLE370_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE370_N_WITH_NEXT,
    STANDING_SEQUENCES as CYCLE370_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next1IOnlyScoreboard,
    leftover_remaining_next1,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2gram_scoreboard import (
    leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_stem_scoreboard import (
    STANDING_G as CYCLE343_G,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_UNIQUE_NEXT_STEM as CYCLE343_CLAIM,
    STANDING_NEXT_STEMS as CYCLE343_NEXT_STEMS,
    leftover_4gram_next_stems,
    site_next_stem_after_4gram,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_prev1_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_PREVIOUS_1GRAMS_ALL_I_ONLY as CYCLE360_CLAIM,
    STANDING_N_EXTRA as CYCLE360_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE360_N_I_ONLY,
    STANDING_N_LEAK as CYCLE360_N_LEAK,
    STANDING_SEQUENCES as CYCLE360_SEQUENCES,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_prev2_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_PREVIOUS_2GRAMS_ALL_I_ONLY as CYCLE351_CLAIM,
    STANDING_N_EXTRA as CYCLE351_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE351_N_I_ONLY,
    STANDING_N_LEAK as CYCLE351_N_LEAK,
    STANDING_SEQUENCES as CYCLE351_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Prev2IOnlyScoreboard,
    leftover_4gram_previous_2grams,
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
GRAM2_295_076 = ("295", "076")
GRAM2_002_076 = ("002", "076")
GRAM2_071_076 = ("071", "076")
GRAM2_460_050 = ("460", "050")
GRAM2_000_700 = ("000", "700")
GRAM2_076_600 = ("076", "600")
GRAM2_760_036 = ("760", "036")
GRAM2_022_280 = ("022", "280")
GRAM2_048_700 = ("048", "700")
GRAM2_720_076 = ("720", "076")
GRAM2_177_700 = ("177", "700")
STANDING_SEQUENCES = (
    GRAM2_295_076,
    GRAM2_002_076,
    GRAM2_071_076,
    GRAM2_460_050,
    GRAM2_000_700,
    GRAM2_076_600,
    GRAM2_760_036,
    GRAM2_022_280,
    GRAM2_048_700,
    GRAM2_720_076,
    GRAM2_177_700,
)
STANDING_NEXT_STEMS = CYCLE343_NEXT_STEMS
STANDING_PARENT_4GRAMS = CYCLE340_MATCHING_4GRAMS
STANDING_N = 11
STANDING_N_4GRAMS = 5
STANDING_N1 = 1
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I_EACH = (1, 11, 21, 1, 1, 16, 1, 1, 1, 5, 1)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_LEFTOVER_MATCHING_4GRAM_SITES = CYCLE340_LEFTOVER_MATCHING
STANDING_LEFTOVER_MATCHING_COUNT = 11
STANDING_LEFTOVER_MATCHING_NEXT2_SITES = CYCLE370_NEXT1_SITES
STANDING_LEFTOVER_MATCHING_SITES_EACH = (
    ((SIDE_IA, "Ia1", 140),),
    ((SIDE_IA, "Ia4", 129),),
    ((SIDE_IA, "Ia14", 82),),
    ((SIDE_IA, "Ia1", 67),),
    ((SIDE_IA, "Ia9", 7),),
    ((SIDE_IA, "Ia6", 52),),
    ((SIDE_IA, "Ia12", 123),),
    ((SIDE_IA, "Ia8", 34),),
    ((SIDE_IA, "Ia10", 148),),
    ((SIDE_IA, "Ia8", 171),),
    ((SIDE_IA, "Ia9", 36),),
)
STANDING_LEFTOVER_MATCHING_NEXT2_COUNT = 11
STANDING_N_MATCHING_EACH = (1,) * STANDING_N
STANDING_N_EXTRA_EACH = (0, 10, 20, 0, 0, 15, 0, 0, 0, 4, 0)
STANDING_N_EXTRA = 49
STANDING_N_WITH_NEXT2 = 11
STANDING_N_NO_NEXT2 = 0
STANDING_N_LINE_FINAL = 0
STANDING_NO_NEXT2_SITES = ()
STANDING_ALL_SITES_HAVE_NEXT_2GRAM = True
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0, 3, 0, 0, 3, 1, 0, 1, 5, 0, 0)
STANDING_N_LEAK_EACH = STANDING_N_OFF_I_EACH
STANDING_N_T_EACH = (0,) * STANDING_N
STANDING_N_LEAK_HIT_T = 0
STANDING_HITS_BY_TABLET = (
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 3, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
)
STANDING_OFF_I_BY_TABLET = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
)
STANDING_OFF_I_TABLETS_WITH_HITS = (
    (),
    ("G",),
    (),
    (),
    ("O", "S"),
    ("G",),
    (),
    ("C",),
    ("G", "H", "P", "Q"),
    (),
    (),
)
STANDING_N_I_ONLY = 6
STANDING_N_NOT_I_ONLY = 5
STANDING_N_LEAKING = 5
STANDING_N_LEAK = 5
STANDING_LEAKING_2GRAMS = (
    GRAM2_002_076,
    GRAM2_000_700,
    GRAM2_076_600,
    GRAM2_022_280,
    GRAM2_048_700,
)
STANDING_I_ONLY_2GRAMS = (
    GRAM2_295_076,
    GRAM2_071_076,
    GRAM2_460_050,
    GRAM2_760_036,
    GRAM2_720_076,
    GRAM2_177_700,
)
STANDING_I_SITES = (
    ((SIDE_IA, "Ia1", 140),),
    (
        (SIDE_IA, "Ia4", 35),
        (SIDE_IA, "Ia4", 129),
        (SIDE_IA, "Ia7", 20),
        (SIDE_IA, "Ia9", 49),
        (SIDE_IA, "Ia9", 78),
        (SIDE_IA, "Ia11", 19),
        (SIDE_IA, "Ia11", 137),
        (SIDE_IA, "Ia11", 141),
        (SIDE_IA, "Ia12", 103),
        (SIDE_IA, "Ia13", 161),
        (SIDE_IA, "Ia14", 87),
    ),
    (
        (SIDE_IA, "Ia2", 42),
        (SIDE_IA, "Ia2", 44),
        (SIDE_IA, "Ia3", 82),
        (SIDE_IA, "Ia4", 7),
        (SIDE_IA, "Ia4", 26),
        (SIDE_IA, "Ia5", 109),
        (SIDE_IA, "Ia7", 50),
        (SIDE_IA, "Ia7", 174),
        (SIDE_IA, "Ia8", 62),
        (SIDE_IA, "Ia12", 26),
        (SIDE_IA, "Ia12", 33),
        (SIDE_IA, "Ia13", 6),
        (SIDE_IA, "Ia13", 23),
        (SIDE_IA, "Ia13", 150),
        (SIDE_IA, "Ia13", 154),
        (SIDE_IA, "Ia14", 50),
        (SIDE_IA, "Ia14", 82),
        (SIDE_IA, "Ia14", 114),
        (SIDE_IA, "Ia14", 135),
        (SIDE_IA, "Ia14", 154),
        (SIDE_IA, "Ia14", 167),
    ),
    ((SIDE_IA, "Ia1", 67),),
    ((SIDE_IA, "Ia9", 7),),
    (
        (SIDE_IA, "Ia1", 90),
        (SIDE_IA, "Ia1", 117),
        (SIDE_IA, "Ia1", 150),
        (SIDE_IA, "Ia2", 15),
        (SIDE_IA, "Ia2", 112),
        (SIDE_IA, "Ia6", 52),
        (SIDE_IA, "Ia6", 165),
        (SIDE_IA, "Ia8", 164),
        (SIDE_IA, "Ia10", 20),
        (SIDE_IA, "Ia11", 79),
        (SIDE_IA, "Ia11", 83),
        (SIDE_IA, "Ia11", 91),
        (SIDE_IA, "Ia11", 115),
        (SIDE_IA, "Ia11", 138),
        (SIDE_IA, "Ia12", 111),
        (SIDE_IA, "Ia13", 78),
    ),
    ((SIDE_IA, "Ia12", 123),),
    ((SIDE_IA, "Ia8", 34),),
    ((SIDE_IA, "Ia10", 148),),
    (
        (SIDE_IA, "Ia5", 90),
        (SIDE_IA, "Ia6", 126),
        (SIDE_IA, "Ia7", 62),
        (SIDE_IA, "Ia8", 171),
        (SIDE_IA, "Ia9", 119),
    ),
    ((SIDE_IA, "Ia9", 36),),
)
STANDING_HAPAX_EACH = (
    True,
    False,
    False,
    True,
    False,
    False,
    True,
    False,
    False,
    False,
    True,
)
STANDING_N_HAPAX = 4
STANDING_N_HAPAX_I_ONLY = 4
STANDING_N_NOT_HAPAX = 7
STANDING_LEFTOVER_MATCHING_LEFTOVER2 = 0
STANDING_LEFTOVER_MATCHING_NEXT2_OF_LEFTOVER2 = 0
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_NOT_REQUIRED = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only"
)
STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT_2GRAMS_ALL_I_ONLY = (
    False
)
STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT2_I_ONLY = (
    False
)
STANDING_RESULT = (
    "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next2_i_only"
)
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_CYCLE349 = False
STANDING_SAME_AS_CYCLE351 = False
STANDING_SAME_AS_CYCLE370 = False
STANDING_SAME_AS_CYCLE371 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE349 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE351 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE370 = True
STANDING_LABELED_G_DOES_NOT_COUNT = True
STANDING_PEEL_LABELED_G_IS_TAUTOLOGY = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_STEM = True
STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_2GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_2GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_1GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_1GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_NEXT_1GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_UNIQUE_NEXT_STEM_IS_NOT_THIS_CYCLE = True
STANDING_FORWARD_5GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_EXTRA_I_NEXT1_2GRAMS_ARE_NOT_THIS_CYCLE = True
STANDING_EXTRA_I_LEAK_NEXT1_PEELS_ARE_NOT_THIS_CYCLE = True
STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE = True
STANDING_INCOMPLETE_SET_IS_LOSE = True


def next_2gram_site(
    leftover_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Next 2-gram starts immediately after leftover 4-gram."""
    side, line, index = leftover_site
    return (side, line, index + 4)


def leftover_4gram_site_for_next2(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Leftover 4-gram starts four tokens before the next-2 start."""
    side, line, index = site
    return (side, line, index - 4)


def site_next_2gram_after_4gram(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...],
) -> tuple[str, ...] | None:
    """Two tokens after leftover 4-gram; None if line-final or only one follows."""
    first = site_next_stem_after_4gram(stems, index, gram4)
    if first is None:
        return None
    second_index = index + len(gram4) + 1
    if second_index >= len(stems):
        return None
    return (first, stems[second_index])


def leftover_4gram_next_2grams(
    i_sides: dict[str, list[list[str]]] | None = None,
    leftover_sites: tuple[tuple[str, str, int], ...] | None = None,
    grams4: tuple[tuple[str, ...], ...] = STANDING_PARENT_4GRAMS,
) -> tuple[tuple[str, ...] | None, ...]:
    """Next 2-grams in leftover-matching-site order; None if incomplete."""
    if i_sides is None:
        i_sides = load_i_sides()
    if leftover_sites is None:
        leftover_sites = leftover_matching_4gram_sites()
    return tuple(
        site_next_2gram_after_4gram(line_stems_for_site(i_sides, site), site[2], gram)
        for site, gram in zip(leftover_sites, grams4, strict=True)
    )


def leftover_remaining_next2(
    i_sides: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple[str, ...], ...]:
    """Next 2-grams that exist (drops None)."""
    return tuple(gram for gram in leftover_4gram_next_2grams(i_sides) if gram is not None)


def leftover_matching_next2_sites(
    leftover_sites: tuple[tuple[str, str, int], ...] | None = None,
    next_2grams: tuple[tuple[str, ...] | None, ...] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching next-2-gram starts (sites that have two following tokens)."""
    if leftover_sites is None:
        leftover_sites = leftover_matching_4gram_sites()
    if next_2grams is None:
        next_2grams = leftover_4gram_next_2grams()
    return tuple(
        next_2gram_site(site)
        for site, gram in zip(leftover_sites, next_2grams, strict=True)
        if gram is not None
    )


def leftover_matching_next2_sites_each(
    leftover_sites: tuple[tuple[str, str, int], ...] | None = None,
    sequences: tuple[tuple[str, ...], ...] = STANDING_SEQUENCES,
) -> tuple[tuple[tuple[str, str, int], ...], ...]:
    """Per next 2-gram leftover matching next-2-gram sites."""
    if leftover_sites is None:
        leftover_sites = leftover_matching_4gram_sites()
    next_2grams = leftover_4gram_next_2grams()
    next_sites = leftover_matching_next2_sites(leftover_sites, next_2grams)
    buckets: dict[tuple[str, ...], list[tuple[str, str, int]]] = {
        gram: [] for gram in sequences
    }
    for gram, site in zip(
        (g for g in next_2grams if g is not None),
        next_sites,
        strict=True,
    ):
        buckets[gram].append(site)
    return tuple(tuple(buckets[gram]) for gram in sequences)


def extra_i_sites_of_2gram(
    i_sites: tuple[tuple[str, str, int], ...],
    leftover_matching: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """I 2-gram sites outside leftover matching next-2-gram sites."""
    leftover_set = set(leftover_matching)
    return tuple(site for site in i_sites if site not in leftover_set)


def leftover_matching_equals_next2_minus_four(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_4GRAM_SITES,
    matching_next2_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_NEXT2_SITES,
) -> bool:
    """True iff leftover matching 4-gram sites equal next-2 starts minus four."""
    measured = set(leftover_4gram_site_for_next2(site) for site in matching_next2_sites)
    return set(leftover_sites) == measured


def leftover_matching_leftover2_of_next2(
    sequences: tuple[tuple[str, ...], ...] = STANDING_SEQUENCES,
    leftover_2grams: tuple[tuple[str, ...], ...] | None = None,
) -> tuple[tuple[str, ...], ...]:
    """Next 2-grams that are also leftover matching leftover 2-grams."""
    if leftover_2grams is None:
        leftover_2grams = leftover_remaining_2grams()
    leftover_set = set(leftover_2grams)
    return tuple(gram for gram in sequences if gram in leftover_set)


def leftover_matching_next2_of_leftover2(
    next2_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_NEXT2_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching next-2 starts that are leftover matching leftover-2 starts."""
    leftover2_sites = {
        site for group in leftover_matching_2gram_sites_each() for site in group
    }
    return tuple(site for site in next2_sites if site in leftover2_sites)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def sequence_is_hapax(n_i: int, n_off_i: int) -> bool:
    """True iff N_I==1 and N_off_I=0."""
    return n_i == 1 and n_off_i == 0


def leaking_2grams(
    sequences: tuple[tuple[str, ...], ...],
    n_off_i: tuple[int, ...],
) -> tuple[tuple[str, ...], ...]:
    """Next 2-grams with N_off_I>0."""
    return tuple(
        gram
        for gram, off in zip(sequences, n_off_i, strict=True)
        if off > 0
    )


def leftover_next2_survey_rows() -> list[dict]:
    """Per-2-gram survey rows: leftover matching next-2 sites + counts."""
    rows = []
    for gram, parent, matching, leftover4, n_on, n_off, n_ex, hits, off_counts, off_tabs, hapax in zip(
        STANDING_SEQUENCES,
        STANDING_PARENT_4GRAMS,
        STANDING_LEFTOVER_MATCHING_SITES_EACH,
        STANDING_LEFTOVER_MATCHING_4GRAM_SITES,
        STANDING_N_I_EACH,
        STANDING_N_OFF_I_EACH,
        STANDING_N_EXTRA_EACH,
        STANDING_HITS_BY_TABLET,
        STANDING_OFF_I_BY_TABLET,
        STANDING_OFF_I_TABLETS_WITH_HITS,
        STANDING_HAPAX_EACH,
        strict=True,
    ):
        rows.append(
            {
                "tokens2": list(gram),
                "parent_4gram": list(parent),
                "leftover_matching_next2_sites": [list(site) for site in matching],
                "leftover_matching_4gram_site": list(leftover4),
                "leftover_matching_count": len(matching),
                "N_I": n_on,
                "N_on_I": n_on,
                "ia_hits": n_on,
                "ib_hits": STANDING_IB_HITS,
                "N_off_I": n_off,
                "N_leak": n_off,
                "N_extra": n_ex,
                "hits_by_tablet": list(hits),
                "off_i_by_tablet": list(off_counts),
                "off_i_tablets_with_hits": list(off_tabs),
                "i_only": n_off == 0 and n_on >= 1,
                "hapax": hapax,
            }
        )
    return rows


def i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    sequences: tuple[tuple[str, ...], ...] = STANDING_SEQUENCES,
    expected_n: int = STANDING_N,
    leftover_sites: tuple[tuple[str, str, int], ...] | None = None,
    next_2grams: tuple[tuple[str, ...] | None, ...] | None = None,
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
) -> bool:
    """True iff all leftover remaining-after-076-010 next 2-grams are I-only.

    Claim holds only if leftover matching sites still compute as
    those 11, every leftover matching site has two following tokens
    so the 2-gram set is complete relative to N=11, the five leftover
    4-grams still compute, and every next 2-gram has N_I>=1 and
    N_off_I=0. Extra I does not make the claim lose. Incomplete set
    is LOSE. Nested leftover 4-gram / leftover 2-gram LOSE / previous
    2-gram LOSE / next 1-gram LOSE / extra-I next-1 peels do not make
    this claim lose.
    """
    if leftovers is None:
        leftovers = leftover_n4_rows()
    remaining_grams = leftover_remaining_grams(leftovers)
    if leftover_sites is None:
        leftover_sites = leftover_matching_4gram_sites()
    if next_2grams is None:
        next_2grams = leftover_4gram_next_2grams()
    return (
        remaining_grams == CYCLE340_SEQUENCES
        and leftover_sites == STANDING_LEFTOVER_MATCHING_4GRAM_SITES
        and len(leftover_sites) == expected_n
        and None not in next_2grams
        and len(next_2grams) == expected_n
        and tuple(next_2grams) == sequences
        and len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next2IOnlyHelpers(
    unittest.TestCase
):
    """Helpers on leftover remaining-after-076-010 next 2-grams. No CV, no LLM."""

    def test_counts_require_exact_tokens(self):
        """Next 2-grams are two tokens after leftover 4-grams, not leftover/prev/extra-I."""
        provider = MockProvider()
        self.assertEqual(leftover_remaining_next2(), STANDING_SEQUENCES)
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N)
        self.assertEqual(
            tuple(gram[0] for gram in STANDING_SEQUENCES),
            CYCLE343_NEXT_STEMS,
        )
        self.assertEqual(leftover_remaining_grams(), CYCLE340_SEQUENCES)
        leftover_2 = leftover_remaining_2grams()
        self.assertEqual(leftover_2, CYCLE349_SEQUENCES)
        self.assertNotEqual(STANDING_SEQUENCES, leftover_2)
        self.assertNotEqual(STANDING_SEQUENCES, CYCLE351_SEQUENCES)
        self.assertNotEqual(STANDING_SEQUENCES, CYCLE371_SEQUENCES)
        for gram in STANDING_SEQUENCES:
            self.assertNotIn(gram, leftover_2)
            self.assertNotIn(gram, CYCLE351_SEQUENCES)
            self.assertEqual(len(gram), STANDING_N2)
        next1 = leftover_remaining_next1()
        self.assertEqual(next1, CYCLE370_SEQUENCES)
        for gram, tok1 in zip(STANDING_SEQUENCES, next1, strict=True):
            self.assertEqual(gram[:1], tok1)
        self.assertEqual(leftover_matching_leftover2_of_next2(), ())
        self.assertEqual(leftover_matching_next2_of_leftover2(), ())
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        self.assertEqual(ngram_hit_count([["295", "076", "295", "076"]], GRAM2_295_076), 2)
        self.assertEqual(ngram_hit_count([["295", "000", "076"]], GRAM2_295_076), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM2_295_076), 0)
        self.assertTrue(STANDING_LEFTOVER_2GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_2GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_NEXT_1GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_EXTRA_I_NEXT1_2GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PEEL_LABELED_G_IS_TAUTOLOGY)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_2gram(self):
        """Boolean is True only when all eleven next 2-grams are I-only."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        hold_ones = (3,) * STANDING_N
        hold_zeros = (0,) * STANDING_N
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only(
                hold_ones, hold_zeros, leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only(
                hold_ones, (1,) + (0,) * 10, leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only(
                (0,) + hold_ones[1:], hold_zeros, leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only(
                hold_ones[:10], hold_zeros[:10], leftovers=leftover
            )
        )
        incomplete = leftover_4gram_next_2grams()[:-1] + (None,)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only(
                hold_ones, hold_zeros, leftovers=leftover, next_2grams=incomplete
            )
        )
        self.assertTrue(sequence_is_i_only(1, 0))
        self.assertTrue(sequence_is_i_only(21, 0))
        self.assertFalse(sequence_is_i_only(11, 3))
        self.assertFalse(sequence_is_i_only(0, 0))
        self.assertTrue(sequence_is_hapax(1, 0))
        self.assertFalse(sequence_is_hapax(21, 0))
        self.assertEqual(leaking_2grams(STANDING_SEQUENCES, hold_zeros), ())
        self.assertEqual(
            leaking_2grams(STANDING_SEQUENCES, STANDING_N_OFF_I_EACH),
            STANDING_LEAKING_2GRAMS,
        )
        self.assertTrue(STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertTrue(STANDING_INCOMPLETE_SET_IS_LOSE)
        self.assertEqual(STANDING_N_EXTRA, 49)
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT_2GRAMS_ALL_I_ONLY
        )
        self.assertNotEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT_2GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_and_extra_i_of_next2(self):
        """Next-2 sites sit four tokens after leftover 4-gram starts; extra I is 49."""
        provider = MockProvider()
        measured = leftover_matching_next2_sites()
        self.assertEqual(measured, STANDING_LEFTOVER_MATCHING_NEXT2_SITES)
        self.assertEqual(measured, CYCLE370_NEXT1_SITES)
        self.assertEqual(
            leftover_matching_4gram_sites(),
            STANDING_LEFTOVER_MATCHING_4GRAM_SITES,
        )
        self.assertTrue(leftover_matching_equals_next2_minus_four())
        self.assertEqual(len(STANDING_LEFTOVER_MATCHING_4GRAM_SITES), 11)
        self.assertEqual(
            leftover_matching_next2_sites_each(),
            STANDING_LEFTOVER_MATCHING_SITES_EACH,
        )
        self.assertEqual(
            sum(len(sites) for sites in STANDING_LEFTOVER_MATCHING_SITES_EACH),
            STANDING_LEFTOVER_MATCHING_NEXT2_COUNT,
        )
        self.assertEqual(STANDING_N_MATCHING_EACH, (1,) * 11)
        self.assertEqual(sum(STANDING_N_EXTRA_EACH), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 49)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_LEFTOVER2, 0)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_NEXT2_OF_LEFTOVER2, 0)
        planted = (SIDE_IA, "Ia99", 999)
        self.assertEqual(
            extra_i_sites_of_2gram(STANDING_I_SITES[0], STANDING_LEFTOVER_MATCHING_SITES_EACH[0]),
            (),
        )
        self.assertEqual(extra_i_sites_of_2gram((planted,), (planted,)), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next2IOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture remaining-after-076-010 next 2-grams I-only. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.remaining_after = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
            self.leftover
        )
        self.remaining_4grams = leftover_remaining_grams(self.leftover)
        self.stems = leftover_4gram_next_stems(self.i_sides)
        self.next2_or_none = leftover_4gram_next_2grams(self.i_sides)
        self.grams = leftover_remaining_next2(self.i_sides)
        self.leftover_matching_4 = leftover_matching_4gram_sites(self.remaining_after)
        self.leftover_matching_next2 = leftover_matching_next2_sites(
            self.leftover_matching_4, self.next2_or_none
        )
        self.leftover_matching_each = leftover_matching_next2_sites_each(
            self.leftover_matching_4
        )
        self.by_tablet = load_vendored_by_tablet()
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in STANDING_SEQUENCES)
        self.ia_hits = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) for gram in STANDING_SEQUENCES
        )
        self.i_hits = self.ia_hits
        self.extra = tuple(
            extra_i_sites_of_2gram(sites, matching)
            for sites, matching in zip(
                self.i_sites, self.leftover_matching_each, strict=True
            )
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in STANDING_SEQUENCES
        )
        self.off_i_counts = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in STANDING_SEQUENCES
        )
        self.off_i_hits = tuple(sum(counts) for counts in self.off_i_counts)
        self.claim_holds = i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only(
            self.i_hits,
            self.off_i_hits,
            leftovers=self.leftover,
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.i_hits, self.off_i_hits, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = len(self.grams) - self.n_i_only
        self.n_leak = sum(1 for off in self.off_i_hits if off > 0)
        self.leaking = leaking_2grams(self.grams, self.off_i_hits)
        self.hapax_each = tuple(
            sequence_is_hapax(on, off)
            for on, off in zip(self.i_hits, self.off_i_hits, strict=True)
        )
        self.n_with_next2 = sum(1 for gram in self.next2_or_none if gram is not None)
        self.n_no_next2 = sum(1 for gram in self.next2_or_none if gram is None)

    def test_tokens_are_two_after_leftover_4grams_not_retuned(self):
        """Next 2-grams are leftover+4/+5, not leftover/prev/extra-I 2-grams."""
        self.assertEqual(self.remaining_4grams, CYCLE340_SEQUENCES)
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.next2_or_none, STANDING_SEQUENCES)
        self.assertEqual(self.stems, CYCLE343_NEXT_STEMS)
        self.assertEqual(len(self.grams), STANDING_N)
        self.assertEqual(len(self.remaining_after), CYCLE340_N)
        self.assertEqual(len(self.remaining_after), 5)
        self.assertEqual(self.n_with_next2, STANDING_N_WITH_NEXT2)
        self.assertEqual(self.n_no_next2, STANDING_N_NO_NEXT2)
        self.assertEqual(self.n_with_next2, 11)
        self.assertEqual(self.n_no_next2, 0)
        self.assertEqual(CYCLE370_N_WITH_NEXT, 11)
        self.assertEqual(CYCLE370_N_NO_NEXT, 0)
        self.assertFalse(CYCLE370_CLAIM)
        self.assertFalse(CYCLE343_CLAIM)
        self.assertEqual(CYCLE343_G, "760")
        prior_370 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next1_i_only"
        ]
        self.assertEqual(prior_370["cycle"], 370)
        self.assertFalse(
            prior_370[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_1grams_all_i_only"
            ]
        )
        self.assertEqual(prior_370["N_i_only"], 2)
        self.assertEqual(prior_370["N_leak"], 9)
        prior_349 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_2grams_i_only"
        ]
        self.assertEqual(prior_349["cycle"], 349)
        self.assertFalse(
            prior_349[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_2grams_all_i_only"
            ]
        )
        prior_351 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_prev2_i_only"
        ]
        self.assertEqual(prior_351["cycle"], 351)
        self.assertFalse(
            prior_351[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_previous_2grams_all_i_only"
            ]
        )
        prior_371 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_next1_2grams_i_only"
        ]
        self.assertEqual(prior_371["cycle"], 371)
        self.assertTrue(
            prior_371[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_next1_2grams_all_i_only"
            ]
        )
        self.assertEqual(prior_371["N_extra"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_STEM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_2gram_lock_extra_i_and_claim_loses(self):
        """Six next 2-grams are I-only; five leak. Extra I of 2-grams is 49. LOSE."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.ia_hits, STANDING_N_I_EACH)
        self.assertEqual(self.i_hits, STANDING_N_I_EACH)
        self.assertEqual(self.off_i_hits, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.leftover_matching_4, STANDING_LEFTOVER_MATCHING_4GRAM_SITES)
        self.assertEqual(len(self.leftover_matching_4), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(self.leftover_matching_next2, STANDING_LEFTOVER_MATCHING_NEXT2_SITES)
        self.assertEqual(self.leftover_matching_each, STANDING_LEFTOVER_MATCHING_SITES_EACH)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(
            tuple(len(sites) for sites in self.extra),
            STANDING_N_EXTRA_EACH,
        )
        self.assertEqual(sum(len(sites) for sites in self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 49)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertTrue(STANDING_ALL_SITES_HAVE_NEXT_2GRAM)
        tablet_t = VENDORED_TABLETS.index("T")
        for gram, sites, matching, leftover4, extra, n_on, n_off, n_ex, n_t, parent, hits, hapax in zip(
            STANDING_SEQUENCES,
            self.i_sites,
            STANDING_LEFTOVER_MATCHING_SITES_EACH,
            STANDING_LEFTOVER_MATCHING_4GRAM_SITES,
            self.extra,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_N_EXTRA_EACH,
            STANDING_N_T_EACH,
            STANDING_PARENT_4GRAMS,
            STANDING_HITS_BY_TABLET,
            STANDING_HAPAX_EACH,
            strict=True,
        ):
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), n_on)
            self.assertGreaterEqual(n_on, 1)
            self.assertEqual(len(matching), 1)
            self.assertEqual(len(extra), n_ex)
            self.assertEqual(n_on, 1 + n_ex)
            self.assertEqual(extra_i_sites_of_2gram(sites, matching), extra)
            self.assertEqual(leftover_4gram_site_for_next2(matching[0]), leftover4)
            self.assertEqual(sequence_is_i_only(n_on, n_off), n_off == 0)
            self.assertEqual(sequence_is_hapax(n_on, n_off), hapax)
            self.assertEqual(len(parent), STANDING_N4)
            self.assertEqual(hits[tablet_t], n_t)
            for tablet, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                if tablet == "I":
                    self.assertEqual(count, n_on)
            for side, line, index in matching:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N2]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
                self.assertNotEqual(line[:2], "Ib")
                self.assertIn((side, line, index), sites)
        self.assertEqual(leftover_matching_leftover2_of_next2(), ())
        self.assertEqual(leftover_matching_next2_of_leftover2(), ())
        self.assertEqual(self.leaking, STANDING_LEAKING_2GRAMS)
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_i_only, 6)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_leak, STANDING_N_LEAK)
        self.assertEqual(self.n_leak, 5)
        self.assertEqual(self.hapax_each, STANDING_HAPAX_EACH)
        self.assertEqual(STANDING_N_HAPAX, 4)
        self.assertEqual(STANDING_N_LEAK_HIT_T, 0)
        self.assertEqual(sum(1 for n_t in STANDING_N_T_EACH if n_t), 0)
        self.assertEqual(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only(
                self.i_hits,
                self.off_i_hits,
                leftovers=self.leftover,
            ),
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT_2GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT_2GRAMS_ALL_I_ONLY,
        )
        self.assertFalse(self.claim_holds)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only",
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_cycle374_371_370_351_349_340_still_lock_and_are_not_relocked(self):
        """Leftover 4-gram HOLD and leftover/prev2/next1 LOSE stay; not this cycle."""
        self.assertTrue(CYCLE340_CLAIM)
        self.assertEqual(CYCLE340_N_EXTRA, 0)
        self.assertEqual(CYCLE340_N_I_ONLY, 5)
        self.assertEqual(len(CYCLE340_LEFTOVER_MATCHING), 11)
        self.assertFalse(CYCLE349_CLAIM)
        self.assertEqual(CYCLE349_N_I_ONLY, 9)
        self.assertEqual(CYCLE349_N_LEAK, 6)
        self.assertEqual(CYCLE349_N_EXTRA, 116)
        self.assertFalse(CYCLE351_CLAIM)
        self.assertEqual(CYCLE351_N_I_ONLY, 7)
        self.assertEqual(CYCLE351_N_LEAK, 4)
        self.assertEqual(CYCLE351_N_EXTRA, 16)
        self.assertFalse(CYCLE358_CLAIM)
        self.assertEqual(CYCLE358_N_I_ONLY, 1)
        self.assertEqual(CYCLE358_N_LEAK, 11)
        self.assertEqual(CYCLE358_N_EXTRA, 916)
        self.assertFalse(CYCLE360_CLAIM)
        self.assertEqual(CYCLE360_N_I_ONLY, 1)
        self.assertEqual(CYCLE360_N_LEAK, 10)
        self.assertEqual(CYCLE360_N_EXTRA, 832)
        self.assertTrue(CYCLE361_CLAIM)
        self.assertEqual(CYCLE361_N_I_ONLY, 4)
        self.assertEqual(CYCLE361_N_LEAK, 0)
        self.assertEqual(CYCLE361_N_EXTRA, 0)
        self.assertFalse(CYCLE370_CLAIM)
        self.assertEqual(CYCLE370_N_I_ONLY, 2)
        self.assertEqual(CYCLE370_N_LEAK, 9)
        self.assertEqual(CYCLE370_N_EXTRA, 772)
        self.assertTrue(CYCLE371_CLAIM)
        self.assertEqual(CYCLE371_N_I_ONLY, 1)
        self.assertEqual(CYCLE371_N_LEAK, 0)
        self.assertEqual(CYCLE371_N_EXTRA, 0)
        self.assertFalse(CYCLE374_CLAIM)
        self.assertEqual(CYCLE374_N_LEAK, 0)
        self.assertTrue(CYCLE344_CLAIM)
        self.assertEqual(CYCLE344_N_I_ONLY, 11)
        self.assertFalse(CYCLE343_CLAIM)
        self.assertEqual(CYCLE343_G, "760")
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_2GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_2GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_NEXT_1GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_EXTRA_I_NEXT1_2GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_EXTRA_I_LEAK_NEXT1_PEELS_ARE_NOT_THIS_CYCLE)
        self.assertEqual(STANDING_N_EXTRA, 49)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_374_through_222_and_220_scoreboards_still_compute(self):
        """Cycle 374 leak-next1 4-grams LOSE, 371 extra-I next1 2-grams HOLD, 370 next1 LOSE stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, CYCLE223_GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(CYCLE222_CLAIM)
        prior_374 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraILeakNext14gramsIOnlyScoreboard()
        )
        prior_374.setUp()
        prior_374.test_survey_matches_computed_lock()
        self.assertFalse(CYCLE374_CLAIM)
        if prior_374.claim_holds:
            self.fail("nested cycle 374 leftover remaining-after-076-010 extra-I leaking next-1-gram 4-grams I-only drifted")
        prior_371 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraINext12gramsIOnlyScoreboard()
        )
        prior_371.setUp()
        prior_371.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE371_CLAIM)
        if not prior_371.claim_holds:
            self.fail("nested cycle 371 leftover remaining-after-076-010 extra-I next-1-gram 2-grams of I-only next 1-grams drifted")
        prior_370 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next1IOnlyScoreboard()
        )
        prior_370.setUp()
        prior_370.test_each_1gram_lock_extra_i_and_claim_loses()
        prior_370.test_survey_matches_computed_lock()
        self.assertFalse(CYCLE370_CLAIM)
        if prior_370.claim_holds:
            self.fail("nested cycle 370 leftover remaining-after-076-010 next 1-grams I-only drifted")
        prior_351 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Prev2IOnlyScoreboard()
        )
        prior_351.setUp()
        prior_351.test_each_2gram_lock_extra_i_and_claim_loses()
        prior_351.test_survey_matches_computed_lock()
        self.assertFalse(CYCLE351_CLAIM)
        if prior_351.claim_holds:
            self.fail("nested cycle 351 leftover remaining-after-076-010 previous 2-grams I-only drifted")
        prior_349 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760102gramsIOnlyScoreboard()
        )
        prior_349.setUp()
        prior_349.test_each_2gram_lock_extra_i_and_claim_loses()
        prior_349.test_survey_matches_computed_lock()
        self.assertFalse(CYCLE349_CLAIM)
        if prior_349.claim_holds:
            self.fail("nested cycle 349 leftover remaining-after-076-010 leftover 2-grams I-only drifted")
        prior_344 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Fwd5IOnlyScoreboard()
        )
        prior_344.setUp()
        prior_344.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE344_CLAIM)
        if not prior_344.claim_holds:
            self.fail("nested cycle 344 leftover remaining-after-076-010 forward 5-grams all I-only drifted")
        prior_340 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760104gramsIOnlyScoreboard()
        )
        prior_340.setUp()
        prior_340.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE340_CLAIM)
        if not prior_340.claim_holds:
            self.fail("nested cycle 340 leftover remaining-after-076-010 4-grams all I-only drifted")
        prior_337 = TestMamariI2gram076010IOnlyScoreboard()
        prior_337.setUp()
        prior_337.test_2gram_is_three_off_i_and_not_i_only()
        prior_337.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE337_N_I, 11)
        self.assertEqual(CYCLE337_N_OFF_I, 3)
        self.assertFalse(CYCLE337_CLAIM)
        self.assertFalse(i_2gram_076_010_i_only(11, 3))
        prior_334 = TestMamariI2gram076020IOnlyScoreboard()
        prior_334.setUp()
        prior_334.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE334_N_I, 12)
        self.assertEqual(CYCLE334_N_OFF_I, 0)
        self.assertTrue(CYCLE334_CLAIM)
        prior_330 = TestMamariI2gram430076IOnlyScoreboard()
        prior_330.setUp()
        prior_330.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE330_N_I, 30)
        self.assertEqual(CYCLE330_N_OFF_I, 16)
        self.assertFalse(CYCLE330_CLAIM)
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE223_N_I, 69)
        self.assertEqual(CYCLE223_N_OFF_I, 3)
        self.assertFalse(CYCLE223_CLAIM)
        self.assertFalse(i_2gram_090_076_i_only(69, 3))
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-375 next 2-gram I-only lose."""
        lock = self.survey[STANDING_RESULT]
        self.assertEqual(lock["cycle"], 375)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(lock["n1"], STANDING_N1)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N"], STANDING_N)
        self.assertEqual(lock["N"], 11)
        self.assertEqual(lock["N_4grams"], STANDING_N_4GRAMS)
        self.assertEqual(lock["N_4grams"], 5)
        self.assertEqual(lock["N_sequences"], STANDING_N)
        self.assertEqual(lock["N_2grams"], STANDING_N)
        self.assertEqual(lock["N_distinct_2grams"], STANDING_N)
        self.assertEqual(lock["N_with_next2"], STANDING_N_WITH_NEXT2)
        self.assertEqual(lock["N_no_next2"], STANDING_N_NO_NEXT2)
        self.assertEqual(lock["N_with_next2"], 11)
        self.assertEqual(lock["N_no_next2"], 0)
        measured_4 = [list(gram) for gram in CYCLE340_SEQUENCES]
        self.assertEqual(lock["tokens4"], measured_4)
        measured_2 = [list(gram) for gram in STANDING_SEQUENCES]
        self.assertEqual(lock["tokens2"], measured_2)
        self.assertEqual(lock["next_stems"], list(CYCLE343_NEXT_STEMS))
        self.assertEqual(
            tuple(tuple(site_row) for site_row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_4GRAM_SITES,
        )
        self.assertEqual(
            tuple(tuple(site_row) for site_row in lock["leftover_matching_next2_sites"]),
            STANDING_LEFTOVER_MATCHING_NEXT2_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(lock["leftover_matching_count"], 11)
        self.assertEqual(
            lock["leftover_matching_next2_count"],
            STANDING_LEFTOVER_MATCHING_NEXT2_COUNT,
        )
        self.assertEqual(lock["leftover_matching_next2_count"], 11)
        self.assertTrue(lock["leftover_matching_equals_next2_minus_four"])
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 49)
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["hapax_not_required"])
        self.assertTrue(lock["extra_i_does_not_make_claim_lose"])
        self.assertTrue(lock["all_sites_have_next_2gram"])
        self.assertTrue(lock["incomplete_set_is_lose"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N)
        self.assertEqual(rows, leftover_next2_survey_rows())
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(tuple(lock["N_extra_each"]), STANDING_N_EXTRA_EACH)
        self.assertEqual(tuple(lock["hapax_each"]), STANDING_HAPAX_EACH)
        leaking_lock = [tuple(row) for row in lock["leaking_2grams"]]
        self.assertEqual(leaking_lock, list(STANDING_LEAKING_2GRAMS))
        self.assertEqual(lock["N_leaking"], 5)
        self.assertEqual(lock["N_leak"], 5)
        self.assertEqual(lock["N_leak_hit_T"], 0)
        self.assertEqual(lock["leftover_matching_leftover2"], 0)
        self.assertEqual(lock["leftover_matching_next2_of_leftover2"], 0)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(
            lock[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2grams_all_i_only"
            ]
        )
        self.assertFalse(
            lock[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next2_i_only"
            ]
        )
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_i_only"], 6)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], 5)
        self.assertEqual(lock["N_hapax"], 4)
        self.assertEqual(lock["N_hapax_i_only"], 4)
        self.assertEqual(
            lock["i_only_2grams"],
            [list(gram) for gram in STANDING_I_ONLY_2GRAMS],
        )
        self.assertFalse(lock["nested_cycle374_extra_i_leak_next1_4grams_all_i_only"])
        self.assertEqual(lock["nested_cycle374_N_leak"], 0)
        self.assertTrue(lock["nested_cycle371_extra_i_next1_2grams_all_i_only"])
        self.assertEqual(lock["nested_cycle371_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle371_N_leak"], 0)
        self.assertEqual(lock["nested_cycle371_N_extra"], 0)
        self.assertFalse(lock["nested_cycle370_next_1grams_all_i_only"])
        self.assertEqual(lock["nested_cycle370_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle370_N_leak"], 9)
        self.assertEqual(lock["nested_cycle370_N_extra"], 772)
        self.assertTrue(lock["nested_cycle361_extra_i_prev1_2grams_all_i_only"])
        self.assertEqual(lock["nested_cycle361_N_i_only"], 4)
        self.assertFalse(lock["nested_cycle360_previous_1grams_all_i_only"])
        self.assertEqual(lock["nested_cycle360_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle360_N_leak"], 10)
        self.assertFalse(lock["nested_cycle358_1grams_all_i_only"])
        self.assertEqual(lock["nested_cycle358_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle358_N_leak"], 11)
        self.assertFalse(lock["nested_cycle351_previous_2grams_all_i_only"])
        self.assertEqual(lock["nested_cycle351_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle351_N_leak"], 4)
        self.assertEqual(lock["nested_cycle351_N_extra"], 16)
        self.assertFalse(lock["nested_cycle349_2grams_all_i_only"])
        self.assertEqual(lock["nested_cycle349_N_i_only"], 9)
        self.assertEqual(lock["nested_cycle349_N_leak"], 6)
        self.assertEqual(lock["nested_cycle349_N_extra"], 116)
        self.assertTrue(lock["nested_cycle344_forward_5grams_all_i_only"])
        self.assertFalse(lock["nested_cycle343_unique_max"])
        self.assertEqual(lock["nested_cycle343_G"], "760")
        self.assertTrue(lock["nested_cycle340_4grams_all_i_only"])
        self.assertEqual(lock["nested_cycle340_N_extra"], 0)
        self.assertEqual(lock["nested_cycle340_N_i_only"], 5)
        self.assertEqual(lock["nested_cycle340_leftover_matching_count"], 11)
        self.assertEqual(lock["nested_cycle337_N_I"], 11)
        self.assertEqual(lock["nested_cycle337_N_off_I"], 3)
        self.assertFalse(lock["nested_cycle337_i_2gram_076_010_i_only"])
        self.assertEqual(lock["nested_cycle334_N_I"], 12)
        self.assertEqual(lock["nested_cycle334_N_off_I"], 0)
        self.assertFalse(lock["nested_cycle330_i_2gram_430_076_i_only"])
        self.assertEqual(lock["nested_cycle330_N_I"], 30)
        self.assertEqual(lock["nested_cycle330_N_off_I"], 16)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle222_K"], 5)
        self.assertEqual(lock["nested_cycle222_N_remaining"], 16)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_cycle349"])
        self.assertFalse(lock["same_as_cycle351"])
        self.assertFalse(lock["same_as_cycle370"])
        self.assertFalse(lock["same_as_cycle371"])
        self.assertTrue(lock["same_claim_shape_as_cycle349"])
        self.assertTrue(lock["same_claim_shape_as_cycle351"])
        self.assertTrue(lock["same_claim_shape_as_cycle370"])
        self.assertTrue(lock["labeled_G_does_not_count"])
        self.assertTrue(lock["peel_labeled_G_is_tautology"])
        self.assertTrue(lock["do_not_peel_a_specific_stem"])
        self.assertTrue(lock["leftover_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["leftover_2gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["previous_2gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["leftover_1gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["previous_1gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["next_1gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["unique_next_stem_is_not_this_cycle"])
        self.assertTrue(lock["forward_5gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["extra_i_next1_2grams_are_not_this_cycle"])
        self.assertTrue(lock["extra_i_leak_next1_peels_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        for cycle in range(328, 375):
            self.assertTrue(lock[f"do_not_relock_cycle{cycle}"])
        self.assertTrue(lock["do_not_relock_cycle222"])
        self.assertTrue(lock["do_not_relock_cycles_288_327"])
        self.assertTrue(lock["do_not_relock_leftover_extra_peels"])
        self.assertTrue(lock["do_not_relock_cycles_220_221"])
        self.assertTrue(lock["do_not_relock_cycle223"])
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next1_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_2grams_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_prev2_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only_unchanged"
            ]
        )
        self.assertTrue(lock["standing_i_2gram_076_010_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_020_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_430_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
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


class TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Next2IOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 375 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
