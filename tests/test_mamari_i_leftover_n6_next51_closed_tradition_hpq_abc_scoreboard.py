"""Reframed closed-tradition hold-out of the locked leftover-6 next-51 grams.

Cycle 884 text-search lock. Uses already-vendored A–V and the
cycle-565 leftover n=6 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 remaining-
after-076-010 next 51-grams (12 sequences; parent N=18; six
holes at Ia10[144], Ia10[143], Ia10[142], Ia8[167], Ia8[166],
and Ia8[165]). HEAD-check: that gram list exists and is not yet
locked under this reframed rule. Cycle 565 already locked the
I-only claim on these 51-grams as incomplete-set LOSE
(N_with_next51=12, N_no_next51=6, N_i_only=12, N_leak=0). Cycle
883 already locked the reframed claim on the cycle-563 next-50
grams as incomplete-set LOSE. This cycle does not re-lock either
claim, and does not re-lock Cycles 832–883.

Claim that can lose: each existing next-51 gram is an exact
contiguous hit on ≥1 of H/P/Q and exact-0 on A/B/C. hits_I is
recorded and is not a leak. HOLD needs that claim true for a
complete population with zero A/B/C leak. Leak onto A/B/C is
leak LOSE. An empty H/P/Q hit set, or a parent set that still
has a hole, is incomplete-set LOSE.

Named claim: cycle565_next51_reframed_closed_tradition_hpq_ge1_exact0_abc.

Measured on the 12 with-next51 grams: N=12, N_hpq_ge1=0,
N_hpq_ge2=0, N_exact0_abc=12, N_i_ge1=12, N_exact0_i=0,
N_leak=0, N_hold=0, hits_I=12. Parent N=18, N_with_next51=12,
N_no_next51=6 (Ia10[144], Ia10[143], Ia10[142], Ia8[167],
Ia8[166], Ia8[165]). Every scored gram is exact-0 on H/P/Q and
on A/B/C and an exact contiguous hit once on I. The next-50 hapax
604 076 071 600 999 050 076 000 002 999 076 092 535 999 208 076 532 244 999
090 076 057 600 700 076 076 053 177 700 076 057 741 430 076 532 200 059 076
074 379 002 076 244 280 001 076 532 071 065 071 at Ia9[9] extends
to 604 076 071 600 999 050 076 000 002 999 076 092 535 999 208 076 532 244 999
090 076 057 600 700 076 076 053 177 700 076 057 741 430 076 532 200 059 076
074 379 002 076 244 280 001 076 532 071 065 071 999 at Ia9[9]
and hits I once. All twelve next-50 grams extend; no new hole.
Verdict: incomplete-set LOSE.

Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Does not reopen leftover-6
next/prev window peels (next-side exhausted at cycle 831;
prev-side eighteen-hole 0/18 since cycle 800). Leftover-6
prev-1 has no locked gram list; do not invent that peel.
Do not launch leftover-6 previous 10-grams, leftover 10-grams,
next 51-grams as a peel, next 52-grams as a peel, prev-184, or
next-185. The cycle-567 next-52 I-only list stays the named
next lock and is not re-scored. Raw stems. No invented Barthel.
No G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Search lock, not a merge and not a translation. MockProvider only.
"""




import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    load_vendored_a_through_v,
)
from tests.test_mamari_i_leftover_n6_next24_closed_tradition_hpq_abc_scoreboard import (
    ABSENT_TABLETS,
    CYCLE457_RESULT,
    CYCLE489_ALL_I_ONLY_CLAIM,
    CYCLE489_HYPOTHESIS_ALL_I_ONLY,
    CYCLE489_N,
    CYCLE489_N_I_ONLY,
    CYCLE489_N_LEAK,
    CYCLE489_N_NO_NEXT13,
    CYCLE489_N_SEQUENCES,
    CYCLE489_N_WITH_NEXT13,
    CYCLE489_NO_NEXT13_SITES,
    CYCLE489_RESULT,
    CYCLE501_ALL_I_ONLY_CLAIM,
    CYCLE501_HYPOTHESIS_ALL_I_ONLY,
    CYCLE501_N,
    CYCLE501_N_I_ONLY,
    CYCLE501_N_LEAK,
    CYCLE501_N_NO_NEXT19,
    CYCLE501_N_SEQUENCES,
    CYCLE501_N_WITH_NEXT19,
    CYCLE501_NO_NEXT19_SITES,
    CYCLE501_RESULT,
    CYCLE503_ALL_I_ONLY_CLAIM,
    CYCLE503_HYPOTHESIS_ALL_I_ONLY,
    CYCLE503_N,
    CYCLE503_N_I_ONLY,
    CYCLE503_N_LEAK,
    CYCLE503_N_NO_NEXT20,
    CYCLE503_N_SEQUENCES,
    CYCLE503_N_WITH_NEXT20,
    CYCLE503_NO_NEXT20_SITES,
    CYCLE503_RESULT,
    CYCLE831_SURVEY_KEY,
    CYCLE832_RESULT,
    CYCLE833_RESULT,
    CYCLE834_RESULT,
    CYCLE834_VERDICT,
    CYCLE835_RESULT,
    CYCLE835_VERDICT,
    CYCLE836_HITS_I,
    CYCLE836_N_HOLD,
    CYCLE836_N_LEAK,
    CYCLE836_RESULT,
    CYCLE836_VERDICT,
    CYCLE837_HITS_I,
    CYCLE837_N_HOLD,
    CYCLE837_N_LEAK,
    CYCLE837_RESULT,
    CYCLE837_VERDICT,
    CYCLE838_HITS_I,
    CYCLE838_N_HOLD,
    CYCLE838_N_LEAK,
    CYCLE838_RESULT,
    CYCLE838_VERDICT,
    CYCLE839_HITS_I,
    CYCLE839_N_HOLD,
    CYCLE839_N_LEAK,
    CYCLE839_RESULT,
    CYCLE839_VERDICT,
    CYCLE840_HITS_I,
    CYCLE840_N_HOLD,
    CYCLE840_N_LEAK,
    CYCLE840_RESULT,
    CYCLE840_SEQUENCES,
    CYCLE840_SITES,
    CYCLE840_VERDICT,
    CYCLE841_NEXT7_DROPPED_INDEX,
    CYCLE843_HITS_I,
    CYCLE843_N_HOLD,
    CYCLE843_N_LEAK,
    CYCLE843_RESULT,
    CYCLE843_VERDICT,
    CYCLE848_HITS_I,
    CYCLE848_N_HOLD,
    CYCLE848_N_LEAK,
    CYCLE848_NEXT_CHEAP_LOCK,
    CYCLE848_RESULT,
    CYCLE848_VERDICT,
    CYCLE849_HITS_I,
    CYCLE849_N_HOLD,
    CYCLE849_N_LEAK,
    CYCLE849_NEXT_CHEAP_LOCK,
    CYCLE849_RESULT,
    CYCLE849_VERDICT,
    CYCLE850_HITS_I,
    CYCLE850_N_HOLD,
    CYCLE850_N_LEAK,
    CYCLE850_NEXT_CHEAP_LOCK,
    CYCLE850_RESULT,
    CYCLE850_VERDICT,
    CYCLE852_HITS_I,
    CYCLE852_N_HOLD,
    CYCLE852_N_LEAK,
    CYCLE852_RESULT,
    CYCLE852_VERDICT,
    HPQ_TABLETS,
    MIN_HPQ_TABLETS,
    PREV1_N6_SCOREBOARD,
    PROBE_TABLETS,
    CYCLE853_HITS_I,
    CYCLE853_N_HOLD,
    CYCLE853_N_LEAK,
    CYCLE853_NO_NEXT20_SITES,
    CYCLE853_RESULT,
    CYCLE853_SEQUENCES,
    CYCLE853_SITES,
    CYCLE853_VERDICT,
    CYCLE854_HITS_I,
    CYCLE854_N_HOLD,
    CYCLE854_N_LEAK,
    CYCLE854_NO_NEXT21_SITES,
    CYCLE854_RESULT,
    CYCLE854_SEQUENCES,
    CYCLE854_SITES,
    CYCLE854_VERDICT,
    CYCLE856_HITS_I,
    CYCLE856_N_HOLD,
    CYCLE856_N_LEAK,
    CYCLE856_NO_NEXT23_SITES,
    CYCLE856_RESULT,
    CYCLE856_SEQUENCES,
    CYCLE856_SITES,
    CYCLE856_VERDICT,
    STANDING_HITS_I as CYCLE857_HITS_I,
    STANDING_N_HOLD as CYCLE857_N_HOLD,
    STANDING_N_LEAK as CYCLE857_N_LEAK,
    STANDING_NO_NEXT24_SITES as CYCLE857_NO_NEXT24_SITES,
    STANDING_RESULT as CYCLE857_RESULT,
    STANDING_SEQUENCES as CYCLE857_SEQUENCES,
    STANDING_SITES as CYCLE857_SITES,
    STANDING_VERDICT as CYCLE857_VERDICT,
    CYCLE855_HITS_I,
    CYCLE855_N_HOLD,
    CYCLE855_N_LEAK,
    CYCLE855_NO_NEXT22_SITES,
    CYCLE855_RESULT,
    CYCLE855_SEQUENCES,
    CYCLE855_SITES,
    CYCLE855_VERDICT,
    absent_hit_sum,
    hpq_tablets_hit,
    reframed_verdict,
    row_holds,
    row_leaks,
    score_reframed_closed_tradition,
    summarize,
)
from tests.test_mamari_i_leftover_n6_next25_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE858_HITS_I,
    STANDING_N_HOLD as CYCLE858_N_HOLD,
    STANDING_N_LEAK as CYCLE858_N_LEAK,
    STANDING_NO_NEXT25_SITES as CYCLE858_NO_NEXT25_SITES,
    STANDING_RESULT as CYCLE858_RESULT,
    STANDING_SEQUENCES as CYCLE858_SEQUENCES,
    STANDING_SITES as CYCLE858_SITES,
    STANDING_VERDICT as CYCLE858_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next26_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE859_HITS_I,
    STANDING_N_HOLD as CYCLE859_N_HOLD,
    STANDING_N_LEAK as CYCLE859_N_LEAK,
    STANDING_NO_NEXT26_SITES as CYCLE859_NO_NEXT26_SITES,
    STANDING_RESULT as CYCLE859_RESULT,
    STANDING_SEQUENCES as CYCLE859_SEQUENCES,
    STANDING_SITES as CYCLE859_SITES,
    STANDING_VERDICT as CYCLE859_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next27_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE860_HITS_I,
    STANDING_N_HOLD as CYCLE860_N_HOLD,
    STANDING_N_LEAK as CYCLE860_N_LEAK,
    STANDING_NO_NEXT27_SITES as CYCLE860_NO_NEXT27_SITES,
    STANDING_RESULT as CYCLE860_RESULT,
    STANDING_SEQUENCES as CYCLE860_SEQUENCES,
    STANDING_SITES as CYCLE860_SITES,
    STANDING_VERDICT as CYCLE860_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next28_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE861_HITS_I,
    STANDING_N_HOLD as CYCLE861_N_HOLD,
    STANDING_N_LEAK as CYCLE861_N_LEAK,
    STANDING_NO_NEXT28_SITES as CYCLE861_NO_NEXT28_SITES,
    STANDING_RESULT as CYCLE861_RESULT,
    STANDING_SEQUENCES as CYCLE861_SEQUENCES,
    STANDING_SITES as CYCLE861_SITES,
    STANDING_VERDICT as CYCLE861_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next29_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE862_HITS_I,
    STANDING_N_HOLD as CYCLE862_N_HOLD,
    STANDING_N_LEAK as CYCLE862_N_LEAK,
    STANDING_RESULT as CYCLE862_RESULT,
    STANDING_VERDICT as CYCLE862_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next30_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE863_HITS_I,
    STANDING_N_HOLD as CYCLE863_N_HOLD,
    STANDING_N_LEAK as CYCLE863_N_LEAK,
    STANDING_NO_NEXT30_SITES as CYCLE863_NO_NEXT30_SITES,
    STANDING_RESULT as CYCLE863_RESULT,
    STANDING_SEQUENCES as CYCLE863_SEQUENCES,
    STANDING_SITES as CYCLE863_SITES,
    STANDING_VERDICT as CYCLE863_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next31_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE864_HITS_I,
    STANDING_N_HOLD as CYCLE864_N_HOLD,
    STANDING_N_LEAK as CYCLE864_N_LEAK,
    STANDING_NO_NEXT31_SITES as CYCLE864_NO_NEXT31_SITES,
    STANDING_RESULT as CYCLE864_RESULT,
    STANDING_SEQUENCES as CYCLE864_SEQUENCES,
    STANDING_SITES as CYCLE864_SITES,
    STANDING_VERDICT as CYCLE864_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next32_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE865_HITS_I,
    STANDING_N_HOLD as CYCLE865_N_HOLD,
    STANDING_N_LEAK as CYCLE865_N_LEAK,
    STANDING_NO_NEXT32_SITES as CYCLE865_NO_NEXT32_SITES,
    STANDING_RESULT as CYCLE865_RESULT,
    STANDING_SEQUENCES as CYCLE865_SEQUENCES,
    STANDING_SITES as CYCLE865_SITES,
    STANDING_VERDICT as CYCLE865_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next33_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE866_HITS_I,
    STANDING_N_HOLD as CYCLE866_N_HOLD,
    STANDING_N_LEAK as CYCLE866_N_LEAK,
    STANDING_NO_NEXT33_SITES as CYCLE866_NO_NEXT33_SITES,
    STANDING_RESULT as CYCLE866_RESULT,
    STANDING_SEQUENCES as CYCLE866_SEQUENCES,
    STANDING_SITES as CYCLE866_SITES,
    STANDING_VERDICT as CYCLE866_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next34_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE867_HITS_I,
    STANDING_N_HOLD as CYCLE867_N_HOLD,
    STANDING_N_LEAK as CYCLE867_N_LEAK,
    STANDING_NO_NEXT34_SITES as CYCLE867_NO_NEXT34_SITES,
    STANDING_RESULT as CYCLE867_RESULT,
    STANDING_SEQUENCES as CYCLE867_SEQUENCES,
    STANDING_SITES as CYCLE867_SITES,
    STANDING_VERDICT as CYCLE867_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next35_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE868_HITS_I,
    STANDING_N_HOLD as CYCLE868_N_HOLD,
    STANDING_N_LEAK as CYCLE868_N_LEAK,
    STANDING_NO_NEXT35_SITES as CYCLE868_NO_NEXT35_SITES,
    STANDING_RESULT as CYCLE868_RESULT,
    STANDING_SEQUENCES as CYCLE868_SEQUENCES,
    STANDING_SITES as CYCLE868_SITES,
    STANDING_VERDICT as CYCLE868_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next36_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE869_HITS_I,
    STANDING_N_HOLD as CYCLE869_N_HOLD,
    STANDING_N_LEAK as CYCLE869_N_LEAK,
    STANDING_NO_NEXT36_SITES as CYCLE869_NO_NEXT36_SITES,
    STANDING_RESULT as CYCLE869_RESULT,
    STANDING_SEQUENCES as CYCLE869_SEQUENCES,
    STANDING_SITES as CYCLE869_SITES,
    STANDING_VERDICT as CYCLE869_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next37_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE870_HITS_I,
    STANDING_N_HOLD as CYCLE870_N_HOLD,
    STANDING_N_LEAK as CYCLE870_N_LEAK,
    STANDING_NO_NEXT37_SITES as CYCLE870_NO_NEXT37_SITES,
    STANDING_RESULT as CYCLE870_RESULT,
    STANDING_SEQUENCES as CYCLE870_SEQUENCES,
    STANDING_SITES as CYCLE870_SITES,
    STANDING_VERDICT as CYCLE870_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next38_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE871_HITS_I,
    STANDING_N_HOLD as CYCLE871_N_HOLD,
    STANDING_N_LEAK as CYCLE871_N_LEAK,
    STANDING_NO_NEXT38_SITES as CYCLE871_NO_NEXT38_SITES,
    STANDING_RESULT as CYCLE871_RESULT,
    STANDING_SEQUENCES as CYCLE871_SEQUENCES,
    STANDING_SITES as CYCLE871_SITES,
    STANDING_VERDICT as CYCLE871_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next39_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE872_HITS_I,
    STANDING_N_HOLD as CYCLE872_N_HOLD,
    STANDING_N_LEAK as CYCLE872_N_LEAK,
    STANDING_NO_NEXT39_SITES as CYCLE872_NO_NEXT39_SITES,
    STANDING_RESULT as CYCLE872_RESULT,
    STANDING_SEQUENCES as CYCLE872_SEQUENCES,
    STANDING_SITES as CYCLE872_SITES,
    STANDING_VERDICT as CYCLE872_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next40_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE873_HITS_I,
    STANDING_N_HOLD as CYCLE873_N_HOLD,
    STANDING_N_LEAK as CYCLE873_N_LEAK,
    STANDING_NO_NEXT40_SITES as CYCLE873_NO_NEXT40_SITES,
    STANDING_RESULT as CYCLE873_RESULT,
    STANDING_SEQUENCES as CYCLE873_SEQUENCES,
    STANDING_SITES as CYCLE873_SITES,
    STANDING_VERDICT as CYCLE873_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next41_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE874_HITS_I,
    STANDING_N_HOLD as CYCLE874_N_HOLD,
    STANDING_N_LEAK as CYCLE874_N_LEAK,
    STANDING_RESULT as CYCLE874_RESULT,
    STANDING_VERDICT as CYCLE874_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next42_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE875_HITS_I,
    STANDING_N_HOLD as CYCLE875_N_HOLD,
    STANDING_N_LEAK as CYCLE875_N_LEAK,
    STANDING_NO_NEXT42_SITES as CYCLE875_NO_NEXT42_SITES,
    STANDING_RESULT as CYCLE875_RESULT,
    STANDING_SEQUENCES as CYCLE875_SEQUENCES,
    STANDING_SITES as CYCLE875_SITES,
    STANDING_VERDICT as CYCLE875_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next43_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE876_HITS_I,
    STANDING_N_HOLD as CYCLE876_N_HOLD,
    STANDING_N_LEAK as CYCLE876_N_LEAK,
    STANDING_NO_NEXT43_SITES as CYCLE876_NO_NEXT43_SITES,
    STANDING_RESULT as CYCLE876_RESULT,
    STANDING_SEQUENCES as CYCLE876_SEQUENCES,
    STANDING_SITES as CYCLE876_SITES,
    STANDING_VERDICT as CYCLE876_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next44_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE877_HITS_I,
    STANDING_N_HOLD as CYCLE877_N_HOLD,
    STANDING_N_LEAK as CYCLE877_N_LEAK,
    STANDING_NO_NEXT44_SITES as CYCLE877_NO_NEXT44_SITES,
    STANDING_RESULT as CYCLE877_RESULT,
    STANDING_SEQUENCES as CYCLE877_SEQUENCES,
    STANDING_SITES as CYCLE877_SITES,
    STANDING_VERDICT as CYCLE877_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next45_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE878_HITS_I,
    STANDING_N_HOLD as CYCLE878_N_HOLD,
    STANDING_N_LEAK as CYCLE878_N_LEAK,
    STANDING_NO_NEXT45_SITES as CYCLE878_NO_NEXT45_SITES,
    STANDING_RESULT as CYCLE878_RESULT,
    STANDING_SEQUENCES as CYCLE878_SEQUENCES,
    STANDING_SITES as CYCLE878_SITES,
    STANDING_VERDICT as CYCLE878_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next46_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE879_HITS_I,
    STANDING_N_HOLD as CYCLE879_N_HOLD,
    STANDING_N_LEAK as CYCLE879_N_LEAK,
    STANDING_NO_NEXT46_SITES as CYCLE879_NO_NEXT46_SITES,
    STANDING_RESULT as CYCLE879_RESULT,
    STANDING_SEQUENCES as CYCLE879_SEQUENCES,
    STANDING_SITES as CYCLE879_SITES,
    STANDING_VERDICT as CYCLE879_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next47_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE880_HITS_I,
    STANDING_N_HOLD as CYCLE880_N_HOLD,
    STANDING_N_LEAK as CYCLE880_N_LEAK,
    STANDING_NO_NEXT47_SITES as CYCLE880_NO_NEXT47_SITES,
    STANDING_RESULT as CYCLE880_RESULT,
    STANDING_SEQUENCES as CYCLE880_SEQUENCES,
    STANDING_SITES as CYCLE880_SITES,
    STANDING_VERDICT as CYCLE880_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next48_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE881_HITS_I,
    STANDING_N_HOLD as CYCLE881_N_HOLD,
    STANDING_N_LEAK as CYCLE881_N_LEAK,
    STANDING_NO_NEXT48_SITES as CYCLE881_NO_NEXT48_SITES,
    STANDING_RESULT as CYCLE881_RESULT,
    STANDING_SEQUENCES as CYCLE881_SEQUENCES,
    STANDING_SITES as CYCLE881_SITES,
    STANDING_VERDICT as CYCLE881_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next49_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE882_HITS_I,
    STANDING_N_HOLD as CYCLE882_N_HOLD,
    STANDING_N_LEAK as CYCLE882_N_LEAK,
    STANDING_NO_NEXT49_SITES as CYCLE882_NO_NEXT49_SITES,
    STANDING_RESULT as CYCLE882_RESULT,
    STANDING_SEQUENCES as CYCLE882_SEQUENCES,
    STANDING_SITES as CYCLE882_SITES,
    STANDING_VERDICT as CYCLE882_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next50_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE883_HITS_I,
    STANDING_N_HOLD as CYCLE883_N_HOLD,
    STANDING_N_LEAK as CYCLE883_N_LEAK,
    STANDING_NO_NEXT50_SITES as CYCLE883_NO_NEXT50_SITES,
    STANDING_RESULT as CYCLE883_RESULT,
    STANDING_SEQUENCES as CYCLE883_SEQUENCES,
    STANDING_SITES as CYCLE883_SITES,
    STANDING_VERDICT as CYCLE883_VERDICT,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next51_i_only_scoreboard import (
    HYPOTHESIS_ALL_I_ONLY as CYCLE565_HYPOTHESIS_ALL_I_ONLY,
    STANDING_I_LEFTOVER_N6_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT51_I_ONLY as CYCLE565_ALL_I_ONLY_CLAIM,
    STANDING_LEFTOVER_MATCHING_NEXT51_SITES as CYCLE565_SITES,
    STANDING_N as CYCLE565_N,
    STANDING_N_I_EACH as CYCLE565_N_I_EACH,
    STANDING_N_I_ONLY as CYCLE565_N_I_ONLY,
    STANDING_N_LEAK as CYCLE565_N_LEAK,
    STANDING_N_NO_NEXT51 as CYCLE565_N_NO_NEXT51,
    STANDING_N_SEQUENCES as CYCLE565_N_SEQUENCES,
    STANDING_N_WITH_NEXT51 as CYCLE565_N_WITH_NEXT51,
    STANDING_NO_NEXT51_SITES as CYCLE565_NO_NEXT51_SITES,
    STANDING_RESULT as CYCLE565_RESULT,
    STANDING_SEQUENCES as CYCLE565_SEQUENCES,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next52_i_only_scoreboard import (
    HYPOTHESIS_ALL_I_ONLY as CYCLE567_HYPOTHESIS_ALL_I_ONLY,
    STANDING_I_LEFTOVER_N6_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT52_I_ONLY as CYCLE567_ALL_I_ONLY_CLAIM,
    STANDING_N as CYCLE567_N,
    STANDING_N_I_ONLY as CYCLE567_N_I_ONLY,
    STANDING_N_LEAK as CYCLE567_N_LEAK,
    STANDING_N_NO_NEXT52 as CYCLE567_N_NO_NEXT52,
    STANDING_N_SEQUENCES as CYCLE567_N_SEQUENCES,
    STANDING_N_WITH_NEXT52 as CYCLE567_N_WITH_NEXT52,
    STANDING_NO_NEXT52_SITES as CYCLE567_NO_NEXT52_SITES,
    STANDING_RESULT as CYCLE567_RESULT,
    STANDING_SEQUENCES as CYCLE567_SEQUENCES,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey


STANDING_N = 12
STANDING_N_PARENT = 18
STANDING_N_WITH_NEXT51 = 12
STANDING_N_NO_NEXT51 = 6
STANDING_NO_NEXT51_SITES = CYCLE565_NO_NEXT51_SITES
STANDING_PARENT_COMPLETE = False
STANDING_HITS_EACH = (0, 0, 0, 0, 0, 0, 1)
STANDING_HITS = (STANDING_HITS_EACH,) * STANDING_N
STANDING_SITES = CYCLE565_SITES
STANDING_SEQUENCES = CYCLE565_SEQUENCES
STANDING_N_HPQ_GE1 = 0
STANDING_N_HPQ_GE2 = 0
STANDING_N_EXACT0_ABC = 12
STANDING_N_I_GE1 = 12
STANDING_N_EXACT0_I = 0
STANDING_N_LEAK = 0
STANDING_N_HOLD = 0
STANDING_HOLD_INDEXES = ()
STANDING_INCOMPLETE_INDEXES = tuple(range(STANDING_N))
STANDING_I_GT1_INDEXES = ()
STANDING_NEXT50_HAPAX_STILL_HAPAX = (3,)
STANDING_NEXT50_ALL_EXTEND = True
STANDING_HITS_H = 0
STANDING_HITS_P = 0
STANDING_HITS_Q = 0
STANDING_HITS_A = 0
STANDING_HITS_B = 0
STANDING_HITS_C = 0
STANDING_HITS_I = 12
STANDING_VERDICT = "incomplete-set LOSE"
STANDING_CLAIM_HOLDS = False
STANDING_CLAIM = "leftover6_next51_reframed_closed_tradition_hpq_ge1_and_exact0_abc"
STANDING_RESULT = "i_leftover_n6_next51_closed_tradition_hpq_abc"
STANDING_AXIS = "closed-tradition-reframed"
STANDING_FROM_CYCLE = 565
STANDING_I_ONLY_ALREADY_LOCKED = True
STANDING_I_ONLY_CYCLE = 565
STANDING_PARENT_I_LOCAL_CYCLE = 457
STANDING_NEXT1_REFRAMED_CYCLE = 834
STANDING_NEXT2_REFRAMED_CYCLE = 835
STANDING_NEXT3_REFRAMED_CYCLE = 836
STANDING_NEXT4_REFRAMED_CYCLE = 837
STANDING_NEXT5_REFRAMED_CYCLE = 838
STANDING_NEXT6_REFRAMED_CYCLE = 839
STANDING_NEXT7_REFRAMED_CYCLE = 840
STANDING_NEXT8_REFRAMED_CYCLE = 841
STANDING_NEXT9_REFRAMED_CYCLE = 842
STANDING_NEXT10_REFRAMED_CYCLE = 843
STANDING_NEXT11_REFRAMED_CYCLE = 844
STANDING_NEXT12_REFRAMED_CYCLE = 845
STANDING_NEXT13_REFRAMED_CYCLE = 846
STANDING_NEXT14_REFRAMED_CYCLE = 847
STANDING_NEXT15_REFRAMED_CYCLE = 848
STANDING_NEXT16_REFRAMED_CYCLE = 849
STANDING_NEXT17_REFRAMED_CYCLE = 850
STANDING_NEXT18_REFRAMED_CYCLE = 851
STANDING_NEXT19_REFRAMED_CYCLE = 852
STANDING_NEXT20_REFRAMED_CYCLE = 853
STANDING_NEXT21_REFRAMED_CYCLE = 854
STANDING_NEXT22_REFRAMED_CYCLE = 855
STANDING_NEXT23_REFRAMED_CYCLE = 856
STANDING_NEXT24_REFRAMED_CYCLE = 857
STANDING_NEXT25_REFRAMED_CYCLE = 858
STANDING_NEXT26_REFRAMED_CYCLE = 859
STANDING_NEXT27_REFRAMED_CYCLE = 860
STANDING_NEXT28_REFRAMED_CYCLE = 861
STANDING_NEXT29_REFRAMED_CYCLE = 862
STANDING_NEXT30_REFRAMED_CYCLE = 863
STANDING_NEXT31_REFRAMED_CYCLE = 864
STANDING_NEXT32_REFRAMED_CYCLE = 865
STANDING_NEXT33_REFRAMED_CYCLE = 866
STANDING_NEXT34_REFRAMED_CYCLE = 867
STANDING_NEXT35_REFRAMED_CYCLE = 868
STANDING_NEXT36_REFRAMED_CYCLE = 869
STANDING_NEXT37_REFRAMED_CYCLE = 870
STANDING_NEXT38_REFRAMED_CYCLE = 871
STANDING_NEXT39_REFRAMED_CYCLE = 872
STANDING_NEXT40_REFRAMED_CYCLE = 873
STANDING_NEXT41_REFRAMED_CYCLE = 874
STANDING_NEXT42_REFRAMED_CYCLE = 875
STANDING_NEXT43_REFRAMED_CYCLE = 876
STANDING_NEXT44_REFRAMED_CYCLE = 877
STANDING_NEXT45_REFRAMED_CYCLE = 878
STANDING_NEXT46_REFRAMED_CYCLE = 879
STANDING_NEXT47_REFRAMED_CYCLE = 880
STANDING_NEXT48_REFRAMED_CYCLE = 881
STANDING_NEXT49_REFRAMED_CYCLE = 882
STANDING_NEXT50_REFRAMED_CYCLE = 883
STANDING_DO_NOT_RELOCK_I_ONLY = True
STANDING_DO_NOT_RELOCK_PARENT_I_LOCAL = True
STANDING_DO_NOT_RELOCK_NEXT1_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT2_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT3_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT4_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT5_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT6_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT7_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT8_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT9_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT10_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT11_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT12_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT13_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT14_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT15_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT16_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT17_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT18_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT19_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT20_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT21_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT22_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT23_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT24_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT25_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT26_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT27_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT28_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT29_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT30_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT31_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT32_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT33_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT34_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT35_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT36_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT37_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT38_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT39_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT40_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT41_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT42_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT43_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT44_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT45_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT46_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT47_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT48_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT49_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT50_REFRAMED = True
STANDING_DO_NOT_RELOCK_CYCLES_832_883 = True
STANDING_WINDOW_PEELS_CLOSED = True
STANDING_PREV1_GRAM_LIST_ABSENT = True
STANDING_DO_NOT_LAUNCH_PREV1_PEEL = True
STANDING_DO_NOT_LAUNCH_PREV10 = True
STANDING_DO_NOT_LAUNCH_LEFTOVER_10GRAMS = True
STANDING_DO_NOT_LAUNCH_NEXT13 = True
STANDING_DO_NOT_LAUNCH_NEXT14 = True
STANDING_DO_NOT_LAUNCH_NEXT15 = True
STANDING_DO_NOT_LAUNCH_NEXT16 = True
STANDING_DO_NOT_LAUNCH_NEXT17 = True
STANDING_DO_NOT_LAUNCH_NEXT18 = True
STANDING_DO_NOT_LAUNCH_NEXT19 = True
STANDING_DO_NOT_LAUNCH_NEXT20 = True
STANDING_DO_NOT_LAUNCH_NEXT21 = True
STANDING_DO_NOT_LAUNCH_NEXT22 = True
STANDING_DO_NOT_LAUNCH_NEXT23 = True
STANDING_DO_NOT_LAUNCH_NEXT24 = True
STANDING_DO_NOT_LAUNCH_NEXT25 = True
STANDING_DO_NOT_LAUNCH_NEXT26 = True
STANDING_DO_NOT_LAUNCH_NEXT27 = True
STANDING_DO_NOT_LAUNCH_NEXT28 = True
STANDING_DO_NOT_LAUNCH_NEXT29 = True
STANDING_DO_NOT_LAUNCH_NEXT30 = True
STANDING_DO_NOT_LAUNCH_NEXT31 = True
STANDING_DO_NOT_LAUNCH_NEXT32 = True
STANDING_DO_NOT_LAUNCH_NEXT33 = True
STANDING_DO_NOT_LAUNCH_NEXT34 = True
STANDING_DO_NOT_LAUNCH_NEXT35 = True
STANDING_DO_NOT_LAUNCH_NEXT36 = True
STANDING_DO_NOT_LAUNCH_NEXT37 = True
STANDING_DO_NOT_LAUNCH_NEXT38 = True
STANDING_DO_NOT_LAUNCH_NEXT39 = True
STANDING_DO_NOT_LAUNCH_NEXT40 = True
STANDING_DO_NOT_LAUNCH_NEXT41 = True
STANDING_DO_NOT_LAUNCH_NEXT42 = True
STANDING_DO_NOT_LAUNCH_NEXT43 = True
STANDING_DO_NOT_LAUNCH_NEXT44 = True
STANDING_DO_NOT_LAUNCH_NEXT45 = True
STANDING_DO_NOT_LAUNCH_NEXT46 = True
STANDING_DO_NOT_LAUNCH_NEXT47 = True
STANDING_DO_NOT_LAUNCH_NEXT48 = True
STANDING_DO_NOT_LAUNCH_NEXT49 = True
STANDING_DO_NOT_LAUNCH_NEXT50 = True
STANDING_DO_NOT_LAUNCH_NEXT51 = True
STANDING_DO_NOT_LAUNCH_NEXT52 = True
STANDING_DO_NOT_LAUNCH_PREV184 = True
STANDING_DO_NOT_LAUNCH_NEXT185 = True
STANDING_NEW_TABLET = False
STANDING_I_IN_ABSENT_SET = False
STANDING_NAMED_BY_CYCLE853 = (
    "cycle505_next21_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE854 = (
    "cycle507_next22_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE855 = (
    "cycle509_next23_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE856 = (
    "cycle511_next24_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE857 = (
    "cycle513_next25_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE858 = (
    "cycle515_next26_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE859 = (
    "cycle517_next27_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE860 = (
    "cycle519_next28_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE861 = (
    "cycle521_next29_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE862 = (
    "cycle523_next30_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE863 = (
    "cycle525_next31_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE864 = (
    "cycle527_next32_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE865 = (
    "cycle529_next33_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE866 = (
    "cycle531_next34_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE867 = (
    "cycle533_next35_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE868 = (
    "cycle535_next36_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE869 = (
    "cycle537_next37_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE870 = (
    "cycle539_next38_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE871 = (
    "cycle541_next39_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE872 = (
    "cycle543_next40_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE873 = (
    "cycle545_next41_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE874 = (
    "cycle547_next42_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE875 = (
    "cycle549_next43_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE876 = (
    "cycle551_next44_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE877 = (
    "cycle553_next45_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE878 = (
    "cycle555_next46_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE879 = (
    "cycle557_next47_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE880 = (
    "cycle559_next48_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE881 = (
    "cycle561_next49_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE882 = (
    "cycle563_next50_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NAMED_BY_CYCLE883 = (
    "cycle565_next51_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NEXT_CHEAP_LOCK = (
    "cycle567_next52_reframed_closed_tradition_hpq_ge1_exact0_abc"
)

STANDING_ORDER_ALREADY_LOCKED = (
    ("tablet_h_p_q_island_recto_order", 73),
    ("tablet_g_k_island_reading_order", 74),
)
STANDING_GAPS_ALREADY_LOCKED = (
    ("tablet_h_p_q_island_recto_gaps", 74),
    ("tablet_h_p_q_island_recto_gap1_pairwise", 75),
    ("tablet_g_k_island_gaps", 75),
)
STANDING_INVENTORY_ALREADY_LOCKED = (
    ("santiago_ia_076_inventory", 48),
    ("corpus_longest_n_inventory", 99),
)



class TestMamariILeftoverN6Next51ClosedTraditionHpqAbcScoreboard(unittest.TestCase):
    """Cycle 884 reframed closed-tradition lock on the cycle-565 next-51 population."""

    @classmethod
    def setUpClass(cls):
        cls.by_tablet = load_vendored_a_through_v()
        cls.rows = score_reframed_closed_tradition(
            cls.by_tablet,
            sequences=STANDING_SEQUENCES,
            sites=STANDING_SITES,
        )
        cls.summary = summarize(cls.rows)
        cls.verdict = reframed_verdict(cls.rows)
        cls.survey = load_corpus_survey()

    def setUp(self):
        self.provider = MockProvider()


    def test_population_is_the_locked_cycle_565_next51_grams(self):
        """Twelve next-51 sequences and sites come from cycle 565. None invented."""
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N)
        self.assertEqual(len(STANDING_SITES), STANDING_N)
        self.assertEqual(STANDING_SEQUENCES, CYCLE565_SEQUENCES)
        self.assertEqual(STANDING_SITES, CYCLE565_SITES)
        self.assertEqual(CYCLE565_N, STANDING_N_PARENT)
        self.assertEqual(CYCLE565_N, 18)
        self.assertEqual(CYCLE565_N_SEQUENCES, 12)
        self.assertEqual(STANDING_N_WITH_NEXT51, CYCLE565_N_WITH_NEXT51)
        self.assertEqual(STANDING_N_NO_NEXT51, CYCLE565_N_NO_NEXT51)
        self.assertEqual(
            STANDING_NO_NEXT51_SITES,
            (
                ("Ia", "Ia10", 144),
                ("Ia", "Ia10", 143),
                ("Ia", "Ia10", 142),
                ("Ia", "Ia8", 167),
                ("Ia", "Ia8", 166),
                ("Ia", "Ia8", 165),
            ),
        )
        self.assertEqual(STANDING_NO_NEXT51_SITES, CYCLE883_NO_NEXT50_SITES)
        self.assertFalse(STANDING_PARENT_COMPLETE)
        self.assertTrue(CYCLE565_HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE565_ALL_I_ONLY_CLAIM)
        self.assertEqual(CYCLE565_N_I_ONLY, 12)
        self.assertEqual(CYCLE565_N_LEAK, 0)
        self.assertEqual(STANDING_FROM_CYCLE, 565)
        self.assertEqual(len(self.rows), 12)
        for row, tokens, site in zip(self.rows, STANDING_SEQUENCES, STANDING_SITES, strict=True):
            self.assertEqual(row.tokens, tokens)
            self.assertEqual(row.site, site)
            self.assertEqual(len(row.tokens), 51)
        prior = self.survey[CYCLE565_RESULT]
        all_i_only_key = (
            "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
            "remaining_after_076_020_remaining_after_076_010_next_51grams_all_i_only"
        )
        self.assertEqual(CYCLE565_RESULT, (
            "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
            "remaining_after_076_020_remaining_after_076_010_next51_i_only"
        ))
        self.assertEqual(prior["cycle"], 565)
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_sequences"], 12)
        self.assertEqual(prior["N_6grams"], 18)
        self.assertTrue(prior["hypothesis_all_i_only"])
        self.assertFalse(prior[all_i_only_key])
        self.assertFalse(prior[CYCLE565_RESULT])
        self.assertEqual(prior["N_i_only"], 12)
        self.assertEqual(prior["N_leak"], 0)
        self.assertEqual(prior["N_no_next51"], 6)
        self.assertEqual(prior["N_with_next51"], 12)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE883, self.survey)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_prior_locks_stay_locked(self):
        """Do not re-lock cycle 565 I-only or the cycle 832–883 boards."""
        parent = self.survey[CYCLE457_RESULT]
        self.assertEqual(parent["cycle"], STANDING_PARENT_I_LOCAL_CYCLE)
        self.assertTrue(parent["hypothesis_all_i_only"])
        self.assertEqual(parent["N"], 18)
        self.assertEqual(parent["N_leak"], 0)
        self.assertTrue(STANDING_DO_NOT_RELOCK_PARENT_I_LOCAL)
        self.assertTrue(STANDING_I_ONLY_ALREADY_LOCKED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_I_ONLY)
        self.assertEqual(STANDING_I_ONLY_CYCLE, 565)
        self.assertFalse(STANDING_I_IN_ABSENT_SET)
        self.assertEqual(ABSENT_TABLETS, ("A", "B", "C"))
        cycle489 = self.survey[CYCLE489_RESULT]
        self.assertEqual(cycle489["cycle"], 489)
        self.assertEqual(cycle489["N"], CYCLE489_N)
        self.assertEqual(cycle489["N_sequences"], CYCLE489_N_SEQUENCES)
        self.assertTrue(cycle489["hypothesis_all_i_only"])
        self.assertTrue(CYCLE489_HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE489_ALL_I_ONLY_CLAIM)
        self.assertEqual(cycle489["N_i_only"], CYCLE489_N_I_ONLY)
        self.assertEqual(cycle489["N_leak"], CYCLE489_N_LEAK)
        self.assertEqual(cycle489["N_with_next13"], CYCLE489_N_WITH_NEXT13)
        self.assertEqual(cycle489["N_no_next13"], CYCLE489_N_NO_NEXT13)
        self.assertEqual(
            tuple(tuple(site) for site in cycle489["no_next13_sites"]),
            CYCLE489_NO_NEXT13_SITES,
        )
        cycle501 = self.survey[CYCLE501_RESULT]
        self.assertEqual(cycle501["cycle"], 501)
        self.assertEqual(cycle501["N"], CYCLE501_N)
        self.assertEqual(cycle501["N_sequences"], CYCLE501_N_SEQUENCES)
        self.assertTrue(cycle501["hypothesis_all_i_only"])
        self.assertTrue(CYCLE501_HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE501_ALL_I_ONLY_CLAIM)
        self.assertEqual(cycle501["N_i_only"], CYCLE501_N_I_ONLY)
        self.assertEqual(cycle501["N_leak"], CYCLE501_N_LEAK)
        self.assertEqual(cycle501["N_with_next19"], CYCLE501_N_WITH_NEXT19)
        self.assertEqual(cycle501["N_no_next19"], CYCLE501_N_NO_NEXT19)
        self.assertEqual(
            tuple(tuple(site) for site in cycle501["no_next19_sites"]),
            CYCLE501_NO_NEXT19_SITES,
        )

        cycle503 = self.survey[CYCLE503_RESULT]
        self.assertEqual(cycle503["cycle"], 503)
        self.assertEqual(cycle503["N"], CYCLE503_N)
        self.assertEqual(cycle503["N_sequences"], CYCLE503_N_SEQUENCES)
        self.assertTrue(cycle503["hypothesis_all_i_only"])
        self.assertTrue(CYCLE503_HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE503_ALL_I_ONLY_CLAIM)
        self.assertEqual(cycle503["N_i_only"], CYCLE503_N_I_ONLY)
        self.assertEqual(cycle503["N_leak"], CYCLE503_N_LEAK)
        self.assertEqual(cycle503["N_with_next20"], CYCLE503_N_WITH_NEXT20)
        self.assertEqual(cycle503["N_no_next20"], CYCLE503_N_NO_NEXT20)
        self.assertEqual(
            tuple(tuple(site) for site in cycle503["no_next20_sites"]),
            CYCLE503_NO_NEXT20_SITES,
        )
        cycle832 = self.survey[CYCLE832_RESULT]
        self.assertEqual(cycle832["cycle"], 832)
        self.assertEqual(cycle832["verdict"], "leak LOSE")
        self.assertEqual(cycle832["N_leak"], 18)
        cycle833 = self.survey[CYCLE833_RESULT]
        self.assertEqual(cycle833["cycle"], 833)
        self.assertEqual(cycle833["verdict"], "incomplete-set LOSE")
        self.assertEqual(cycle833["N_hpq_ge1"], 0)
        self.assertEqual(cycle833["N_leak"], 0)
        next1 = self.survey[CYCLE834_RESULT]
        self.assertEqual(next1["cycle"], STANDING_NEXT1_REFRAMED_CYCLE)
        self.assertEqual(next1["verdict"], CYCLE834_VERDICT)
        self.assertEqual(next1["verdict"], "leak LOSE")
        self.assertEqual(next1["N_hold"], 1)
        self.assertEqual(next1["N_leak"], 15)
        next2 = self.survey[CYCLE835_RESULT]
        self.assertEqual(next2["cycle"], STANDING_NEXT2_REFRAMED_CYCLE)
        self.assertEqual(next2["verdict"], CYCLE835_VERDICT)
        self.assertEqual(next2["verdict"], "leak LOSE")
        self.assertEqual(next2["N_hold"], 2)
        self.assertEqual(next2["N_leak"], 1)
        next3 = self.survey[CYCLE836_RESULT]
        self.assertEqual(next3["cycle"], STANDING_NEXT3_REFRAMED_CYCLE)
        self.assertEqual(next3["verdict"], CYCLE836_VERDICT)
        self.assertEqual(next3["verdict"], "incomplete-set LOSE")
        self.assertEqual(next3["N_hold"], CYCLE836_N_HOLD)
        self.assertEqual(next3["N_hold"], 0)
        self.assertEqual(next3["N_leak"], CYCLE836_N_LEAK)
        self.assertEqual(next3["N_leak"], 0)
        self.assertEqual(next3["hits_I"], CYCLE836_HITS_I)
        self.assertEqual(next3["hits_I"], 21)
        next4 = self.survey[CYCLE837_RESULT]
        self.assertEqual(next4["cycle"], STANDING_NEXT4_REFRAMED_CYCLE)
        self.assertEqual(next4["verdict"], CYCLE837_VERDICT)
        self.assertEqual(next4["verdict"], "incomplete-set LOSE")
        self.assertEqual(next4["N_hold"], CYCLE837_N_HOLD)
        self.assertEqual(next4["N_hold"], 0)
        self.assertEqual(next4["N_leak"], CYCLE837_N_LEAK)
        self.assertEqual(next4["N_leak"], 0)
        self.assertEqual(next4["hits_I"], CYCLE837_HITS_I)
        self.assertEqual(next4["hits_I"], 18)
        next5 = self.survey[CYCLE838_RESULT]
        self.assertEqual(next5["cycle"], STANDING_NEXT5_REFRAMED_CYCLE)
        self.assertEqual(next5["verdict"], CYCLE838_VERDICT)
        self.assertEqual(next5["verdict"], "incomplete-set LOSE")
        self.assertEqual(next5["N_hold"], CYCLE838_N_HOLD)
        self.assertEqual(next5["N_hold"], 0)
        self.assertEqual(next5["N_leak"], CYCLE838_N_LEAK)
        self.assertEqual(next5["N_leak"], 0)
        self.assertEqual(next5["hits_I"], CYCLE838_HITS_I)
        self.assertEqual(next5["hits_I"], 18)
        next6 = self.survey[CYCLE839_RESULT]
        self.assertEqual(next6["cycle"], STANDING_NEXT6_REFRAMED_CYCLE)
        self.assertEqual(next6["verdict"], CYCLE839_VERDICT)
        self.assertEqual(next6["verdict"], "incomplete-set LOSE")
        self.assertEqual(next6["N_hold"], CYCLE839_N_HOLD)
        self.assertEqual(next6["N_hold"], 0)
        self.assertEqual(next6["N_leak"], CYCLE839_N_LEAK)
        self.assertEqual(next6["N_leak"], 0)
        self.assertEqual(next6["hits_I"], CYCLE839_HITS_I)
        self.assertEqual(next6["hits_I"], 17)
        self.assertEqual(next6["N_hpq_ge1"], 0)
        next7 = self.survey[CYCLE840_RESULT]
        self.assertEqual(next7["cycle"], STANDING_NEXT7_REFRAMED_CYCLE)
        self.assertEqual(next7["verdict"], CYCLE840_VERDICT)
        self.assertEqual(next7["verdict"], "incomplete-set LOSE")
        self.assertEqual(next7["N_hold"], CYCLE840_N_HOLD)
        self.assertEqual(next7["N_hold"], 0)
        self.assertEqual(next7["N_leak"], CYCLE840_N_LEAK)
        self.assertEqual(next7["N_leak"], 0)
        self.assertEqual(next7["hits_I"], CYCLE840_HITS_I)
        self.assertEqual(next7["hits_I"], 16)
        self.assertEqual(next7["N_hpq_ge1"], 0)
        next8 = self.survey["i_leftover_n6_next8_closed_tradition_hpq_abc"]
        self.assertEqual(next8["cycle"], STANDING_NEXT8_REFRAMED_CYCLE)
        self.assertEqual(next8["verdict"], "incomplete-set LOSE")
        self.assertEqual(next8["N_hold"], 0)
        self.assertEqual(next8["N_leak"], 0)
        self.assertEqual(next8["hits_I"], 15)
        self.assertEqual(next8["N_hpq_ge1"], 0)
        next9 = self.survey["i_leftover_n6_next9_closed_tradition_hpq_abc"]
        self.assertEqual(next9["cycle"], STANDING_NEXT9_REFRAMED_CYCLE)
        self.assertEqual(next9["verdict"], "incomplete-set LOSE")
        self.assertEqual(next9["N_hold"], 0)
        self.assertEqual(next9["N_leak"], 0)
        self.assertEqual(next9["hits_I"], 15)
        self.assertEqual(next9["N_hpq_ge1"], 0)
        next10 = self.survey[CYCLE843_RESULT]
        self.assertEqual(next10["cycle"], STANDING_NEXT10_REFRAMED_CYCLE)
        self.assertEqual(next10["verdict"], CYCLE843_VERDICT)
        self.assertEqual(next10["verdict"], "incomplete-set LOSE")
        self.assertEqual(next10["N_hold"], CYCLE843_N_HOLD)
        self.assertEqual(next10["N_hold"], 0)
        self.assertEqual(next10["N_leak"], CYCLE843_N_LEAK)
        self.assertEqual(next10["N_leak"], 0)
        self.assertEqual(next10["hits_I"], CYCLE843_HITS_I)
        self.assertEqual(next10["hits_I"], 15)
        self.assertEqual(next10["N_hpq_ge1"], 0)
        next11 = self.survey["i_leftover_n6_next11_closed_tradition_hpq_abc"]
        self.assertEqual(next11["cycle"], STANDING_NEXT11_REFRAMED_CYCLE)
        self.assertEqual(next11["verdict"], "incomplete-set LOSE")
        self.assertEqual(next11["N_hold"], 0)
        self.assertEqual(next11["N_leak"], 0)
        self.assertEqual(next11["hits_I"], 15)
        self.assertEqual(next11["N_hpq_ge1"], 0)
        self.assertEqual(next11["N_exact0_abc"], 15)
        next12 = self.survey["i_leftover_n6_next12_closed_tradition_hpq_abc"]
        self.assertEqual(next12["cycle"], STANDING_NEXT12_REFRAMED_CYCLE)
        self.assertEqual(next12["verdict"], "incomplete-set LOSE")
        self.assertEqual(next12["N_hold"], 0)
        self.assertEqual(next12["N_leak"], 0)
        self.assertEqual(next12["hits_I"], 15)
        self.assertEqual(next12["N_hpq_ge1"], 0)
        self.assertEqual(next12["N_exact0_abc"], 15)
        next13 = self.survey["i_leftover_n6_next13_closed_tradition_hpq_abc"]
        self.assertEqual(next13["cycle"], STANDING_NEXT13_REFRAMED_CYCLE)
        self.assertEqual(next13["verdict"], "incomplete-set LOSE")
        self.assertEqual(next13["N_hold"], 0)
        self.assertEqual(next13["N_leak"], 0)
        self.assertEqual(next13["hits_I"], 15)
        self.assertEqual(next13["N_hpq_ge1"], 0)
        self.assertEqual(next13["N_exact0_abc"], 15)
        next14 = self.survey["i_leftover_n6_next14_closed_tradition_hpq_abc"]
        self.assertEqual(next14["cycle"], STANDING_NEXT14_REFRAMED_CYCLE)
        self.assertEqual(next14["verdict"], "incomplete-set LOSE")
        self.assertEqual(next14["N_hold"], 0)
        self.assertEqual(next14["N_leak"], 0)
        self.assertEqual(next14["hits_I"], 15)
        self.assertEqual(next14["N_hpq_ge1"], 0)
        self.assertEqual(next14["N_exact0_abc"], 15)
        next15 = self.survey[CYCLE848_RESULT]
        self.assertEqual(next15["cycle"], STANDING_NEXT15_REFRAMED_CYCLE)
        self.assertEqual(next15["verdict"], CYCLE848_VERDICT)
        self.assertEqual(next15["verdict"], "incomplete-set LOSE")
        self.assertEqual(next15["N_hold"], CYCLE848_N_HOLD)
        self.assertEqual(next15["N_hold"], 0)
        self.assertEqual(next15["N_leak"], CYCLE848_N_LEAK)
        self.assertEqual(next15["N_leak"], 0)
        self.assertEqual(next15["hits_I"], CYCLE848_HITS_I)
        self.assertEqual(next15["hits_I"], 15)
        self.assertEqual(next15["N_hpq_ge1"], 0)
        self.assertEqual(next15["N_exact0_abc"], 15)
        self.assertEqual(next15["next_cheap_lock"], CYCLE848_NEXT_CHEAP_LOCK)
        next16 = self.survey[CYCLE849_RESULT]
        self.assertEqual(next16["cycle"], STANDING_NEXT16_REFRAMED_CYCLE)
        self.assertEqual(next16["verdict"], CYCLE849_VERDICT)
        self.assertEqual(next16["verdict"], "incomplete-set LOSE")
        self.assertEqual(next16["N_hold"], CYCLE849_N_HOLD)
        self.assertEqual(next16["N_hold"], 0)
        self.assertEqual(next16["N_leak"], CYCLE849_N_LEAK)
        self.assertEqual(next16["N_leak"], 0)
        self.assertEqual(next16["hits_I"], CYCLE849_HITS_I)
        self.assertEqual(next16["hits_I"], 15)
        self.assertEqual(next16["N_hpq_ge1"], 0)
        self.assertEqual(next16["N_exact0_abc"], 15)
        self.assertEqual(next16["N_with_next16"], 15)
        self.assertEqual(next16["N_no_next16"], 3)
        self.assertEqual(next16["next_cheap_lock"], CYCLE849_NEXT_CHEAP_LOCK)
        next17 = self.survey[CYCLE850_RESULT]
        self.assertEqual(next17["cycle"], STANDING_NEXT17_REFRAMED_CYCLE)
        self.assertEqual(next17["verdict"], CYCLE850_VERDICT)
        self.assertEqual(next17["verdict"], "incomplete-set LOSE")
        self.assertEqual(next17["N_hold"], CYCLE850_N_HOLD)
        self.assertEqual(next17["N_hold"], 0)
        self.assertEqual(next17["N_leak"], CYCLE850_N_LEAK)
        self.assertEqual(next17["N_leak"], 0)
        self.assertEqual(next17["hits_I"], CYCLE850_HITS_I)
        self.assertEqual(next17["hits_I"], 15)
        self.assertEqual(next17["N_hpq_ge1"], 0)
        self.assertEqual(next17["N_exact0_abc"], 15)
        self.assertEqual(next17["N_with_next17"], 15)
        self.assertEqual(next17["N_no_next17"], 3)
        self.assertEqual(next17["next_cheap_lock"], CYCLE850_NEXT_CHEAP_LOCK)
        next18 = self.survey["i_leftover_n6_next18_closed_tradition_hpq_abc"]
        self.assertEqual(next18["cycle"], STANDING_NEXT18_REFRAMED_CYCLE)
        self.assertEqual(next18["verdict"], "incomplete-set LOSE")
        self.assertEqual(next18["N_hold"], 0)
        self.assertEqual(next18["N_leak"], 0)
        self.assertEqual(next18["hits_I"], 15)
        self.assertEqual(next18["N_hpq_ge1"], 0)
        self.assertEqual(next18["N_exact0_abc"], 15)
        self.assertEqual(next18["N_with_next18"], 15)
        self.assertEqual(next18["N_no_next18"], 3)
        next19 = self.survey[CYCLE852_RESULT]
        self.assertEqual(next19["cycle"], STANDING_NEXT19_REFRAMED_CYCLE)
        self.assertEqual(next19["verdict"], CYCLE852_VERDICT)
        self.assertEqual(next19["verdict"], "incomplete-set LOSE")
        self.assertEqual(next19["N_hold"], CYCLE852_N_HOLD)
        self.assertEqual(next19["N_hold"], 0)
        self.assertEqual(next19["N_leak"], CYCLE852_N_LEAK)
        self.assertEqual(next19["N_leak"], 0)
        self.assertEqual(next19["hits_I"], CYCLE852_HITS_I)
        self.assertEqual(next19["hits_I"], 15)
        self.assertEqual(next19["N_hpq_ge1"], 0)
        self.assertEqual(next19["N_exact0_abc"], 15)
        self.assertEqual(next19["N_with_next19"], 15)
        self.assertEqual(next19["N_no_next19"], 3)
        self.assertEqual(next19["next_cheap_lock"], "cycle503_next20_reframed_closed_tradition_hpq_ge1_exact0_abc")
        self.assertNotIn("cycle503_next20_reframed_closed_tradition_hpq_ge1_exact0_abc", self.survey)

        next20 = self.survey[CYCLE853_RESULT]
        self.assertEqual(next20["cycle"], STANDING_NEXT20_REFRAMED_CYCLE)
        self.assertEqual(next20["verdict"], CYCLE853_VERDICT)
        self.assertEqual(next20["verdict"], "incomplete-set LOSE")
        self.assertEqual(next20["N_hold"], CYCLE853_N_HOLD)
        self.assertEqual(next20["N_hold"], 0)
        self.assertEqual(next20["N_leak"], CYCLE853_N_LEAK)
        self.assertEqual(next20["N_leak"], 0)
        self.assertEqual(next20["hits_I"], CYCLE853_HITS_I)
        self.assertEqual(next20["hits_I"], 15)
        self.assertEqual(next20["N_hpq_ge1"], 0)
        self.assertEqual(next20["N_exact0_abc"], 15)
        self.assertEqual(next20["N_with_next20"], 15)
        self.assertEqual(next20["N_no_next20"], 3)
        self.assertEqual(next20["next_cheap_lock"], STANDING_NAMED_BY_CYCLE853)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE853, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT1_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT2_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT3_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT4_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT5_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT6_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT7_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT8_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT9_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT10_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT11_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT12_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT13_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT14_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT15_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT16_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT17_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT18_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT19_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT20_REFRAMED)

        next21 = self.survey[CYCLE854_RESULT]
        self.assertEqual(next21["cycle"], STANDING_NEXT21_REFRAMED_CYCLE)
        self.assertEqual(next21["verdict"], CYCLE854_VERDICT)
        self.assertEqual(next21["verdict"], "incomplete-set LOSE")
        self.assertEqual(next21["N_hold"], CYCLE854_N_HOLD)
        self.assertEqual(next21["N_hold"], 0)
        self.assertEqual(next21["N_leak"], CYCLE854_N_LEAK)
        self.assertEqual(next21["N_leak"], 0)
        self.assertEqual(next21["hits_I"], CYCLE854_HITS_I)
        self.assertEqual(next21["hits_I"], 15)
        self.assertEqual(next21["N_hpq_ge1"], 0)
        self.assertEqual(next21["N_exact0_abc"], 15)
        self.assertEqual(next21["N_with_next21"], 15)
        self.assertEqual(next21["N_no_next21"], 3)
        self.assertEqual(next21["next_cheap_lock"], STANDING_NAMED_BY_CYCLE854)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE854, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT21_REFRAMED)
        next22 = self.survey[CYCLE855_RESULT]
        self.assertEqual(next22["cycle"], STANDING_NEXT22_REFRAMED_CYCLE)
        self.assertEqual(next22["verdict"], CYCLE855_VERDICT)
        self.assertEqual(next22["verdict"], "incomplete-set LOSE")
        self.assertEqual(next22["N_hold"], CYCLE855_N_HOLD)
        self.assertEqual(next22["N_hold"], 0)
        self.assertEqual(next22["N_leak"], CYCLE855_N_LEAK)
        self.assertEqual(next22["N_leak"], 0)
        self.assertEqual(next22["hits_I"], CYCLE855_HITS_I)
        self.assertEqual(next22["hits_I"], 15)
        self.assertEqual(next22["N_hpq_ge1"], 0)
        self.assertEqual(next22["N_exact0_abc"], 15)
        self.assertEqual(next22["N_with_next22"], 15)
        self.assertEqual(next22["N_no_next22"], 3)
        self.assertEqual(next22["next_cheap_lock"], STANDING_NAMED_BY_CYCLE855)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE855, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT22_REFRAMED)
        next23 = self.survey[CYCLE856_RESULT]
        self.assertEqual(next23["cycle"], STANDING_NEXT23_REFRAMED_CYCLE)
        self.assertEqual(next23["verdict"], CYCLE856_VERDICT)
        self.assertEqual(next23["verdict"], "incomplete-set LOSE")
        self.assertEqual(next23["N_hold"], CYCLE856_N_HOLD)
        self.assertEqual(next23["N_hold"], 0)
        self.assertEqual(next23["N_leak"], CYCLE856_N_LEAK)
        self.assertEqual(next23["N_leak"], 0)
        self.assertEqual(next23["hits_I"], CYCLE856_HITS_I)
        self.assertEqual(next23["hits_I"], 15)
        self.assertEqual(next23["N_hpq_ge1"], 0)
        self.assertEqual(next23["N_exact0_abc"], 15)
        self.assertEqual(next23["N_with_next23"], 15)
        self.assertEqual(next23["N_no_next23"], 3)
        self.assertEqual(next23["next_cheap_lock"], STANDING_NAMED_BY_CYCLE856)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE856, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT23_REFRAMED)
        next24 = self.survey[CYCLE857_RESULT]
        self.assertEqual(next24["cycle"], STANDING_NEXT24_REFRAMED_CYCLE)
        self.assertEqual(next24["verdict"], CYCLE857_VERDICT)
        self.assertEqual(next24["verdict"], "incomplete-set LOSE")
        self.assertEqual(next24["N_hold"], CYCLE857_N_HOLD)
        self.assertEqual(next24["N_hold"], 0)
        self.assertEqual(next24["N_leak"], CYCLE857_N_LEAK)
        self.assertEqual(next24["N_leak"], 0)
        self.assertEqual(next24["hits_I"], CYCLE857_HITS_I)
        self.assertEqual(next24["hits_I"], 15)
        self.assertEqual(next24["N_hpq_ge1"], 0)
        self.assertEqual(next24["N_exact0_abc"], 15)
        self.assertEqual(next24["N_with_next24"], 15)
        self.assertEqual(next24["N_no_next24"], 3)
        self.assertEqual(next24["next_cheap_lock"], STANDING_NAMED_BY_CYCLE857)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE857, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT24_REFRAMED)
        next25 = self.survey[CYCLE858_RESULT]
        self.assertEqual(next25["cycle"], STANDING_NEXT25_REFRAMED_CYCLE)
        self.assertEqual(next25["verdict"], CYCLE858_VERDICT)
        self.assertEqual(next25["verdict"], "incomplete-set LOSE")
        self.assertEqual(next25["N_hold"], CYCLE858_N_HOLD)
        self.assertEqual(next25["N_hold"], 0)
        self.assertEqual(next25["N_leak"], CYCLE858_N_LEAK)
        self.assertEqual(next25["N_leak"], 0)
        self.assertEqual(next25["hits_I"], CYCLE858_HITS_I)
        self.assertEqual(next25["hits_I"], 15)
        self.assertEqual(next25["N_hpq_ge1"], 0)
        self.assertEqual(next25["N_exact0_abc"], 15)
        self.assertEqual(next25["N_with_next25"], 15)
        self.assertEqual(next25["N_no_next25"], 3)
        self.assertEqual(next25["next_cheap_lock"], STANDING_NAMED_BY_CYCLE858)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE858, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT25_REFRAMED)
        next26 = self.survey[CYCLE859_RESULT]
        self.assertEqual(next26["cycle"], STANDING_NEXT26_REFRAMED_CYCLE)
        self.assertEqual(next26["verdict"], CYCLE859_VERDICT)
        self.assertEqual(next26["verdict"], "incomplete-set LOSE")
        self.assertEqual(next26["N_hold"], CYCLE859_N_HOLD)
        self.assertEqual(next26["N_hold"], 0)
        self.assertEqual(next26["N_leak"], CYCLE859_N_LEAK)
        self.assertEqual(next26["N_leak"], 0)
        self.assertEqual(next26["hits_I"], CYCLE859_HITS_I)
        self.assertEqual(next26["hits_I"], 15)
        self.assertEqual(next26["N_hpq_ge1"], 0)
        self.assertEqual(next26["N_exact0_abc"], 15)
        self.assertEqual(next26["N_with_next26"], 15)
        self.assertEqual(next26["N_no_next26"], 3)
        self.assertEqual(next26["next_cheap_lock"], STANDING_NAMED_BY_CYCLE859)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE859, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT26_REFRAMED)
        next27 = self.survey[CYCLE860_RESULT]
        self.assertEqual(next27["cycle"], STANDING_NEXT27_REFRAMED_CYCLE)
        self.assertEqual(next27["verdict"], CYCLE860_VERDICT)
        self.assertEqual(next27["verdict"], "incomplete-set LOSE")
        self.assertEqual(next27["N_hold"], CYCLE860_N_HOLD)
        self.assertEqual(next27["N_hold"], 0)
        self.assertEqual(next27["N_leak"], CYCLE860_N_LEAK)
        self.assertEqual(next27["N_leak"], 0)
        self.assertEqual(next27["hits_I"], CYCLE860_HITS_I)
        self.assertEqual(next27["hits_I"], 15)
        self.assertEqual(next27["N_hpq_ge1"], 0)
        self.assertEqual(next27["N_exact0_abc"], 15)
        self.assertEqual(next27["N_with_next27"], 15)
        self.assertEqual(next27["N_no_next27"], 3)
        self.assertEqual(next27["next_cheap_lock"], STANDING_NAMED_BY_CYCLE860)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE860, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT27_REFRAMED)
        next28 = self.survey[CYCLE861_RESULT]
        self.assertEqual(next28["cycle"], STANDING_NEXT28_REFRAMED_CYCLE)
        self.assertEqual(next28["verdict"], CYCLE861_VERDICT)
        self.assertEqual(next28["verdict"], "incomplete-set LOSE")
        self.assertEqual(next28["N_hold"], CYCLE861_N_HOLD)
        self.assertEqual(next28["N_hold"], 0)
        self.assertEqual(next28["N_leak"], CYCLE861_N_LEAK)
        self.assertEqual(next28["N_leak"], 0)
        self.assertEqual(next28["hits_I"], CYCLE861_HITS_I)
        self.assertEqual(next28["hits_I"], 15)
        self.assertEqual(next28["N_hpq_ge1"], 0)
        self.assertEqual(next28["N_exact0_abc"], 15)
        self.assertEqual(next28["N_with_next28"], 15)
        self.assertEqual(next28["N_no_next28"], 3)
        self.assertEqual(next28["next_cheap_lock"], STANDING_NAMED_BY_CYCLE861)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE861, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT28_REFRAMED)
        next29 = self.survey[CYCLE862_RESULT]
        self.assertEqual(next29["cycle"], STANDING_NEXT29_REFRAMED_CYCLE)
        self.assertEqual(next29["verdict"], CYCLE862_VERDICT)
        self.assertEqual(next29["verdict"], "incomplete-set LOSE")
        self.assertEqual(next29["N_hold"], CYCLE862_N_HOLD)
        self.assertEqual(next29["N_hold"], 0)
        self.assertEqual(next29["N_leak"], CYCLE862_N_LEAK)
        self.assertEqual(next29["N_leak"], 0)
        self.assertEqual(next29["hits_I"], CYCLE862_HITS_I)
        self.assertEqual(next29["hits_I"], 15)
        self.assertEqual(next29["N_hpq_ge1"], 0)
        self.assertEqual(next29["N_exact0_abc"], 15)
        self.assertEqual(next29["N_with_next29"], 15)
        self.assertEqual(next29["N_no_next29"], 3)
        self.assertEqual(next29["next_cheap_lock"], STANDING_NAMED_BY_CYCLE862)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE862, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT29_REFRAMED)
        next30 = self.survey[CYCLE863_RESULT]
        self.assertEqual(next30["cycle"], STANDING_NEXT30_REFRAMED_CYCLE)
        self.assertEqual(next30["verdict"], CYCLE863_VERDICT)
        self.assertEqual(next30["verdict"], "incomplete-set LOSE")
        self.assertEqual(next30["N_hold"], CYCLE863_N_HOLD)
        self.assertEqual(next30["N_hold"], 0)
        self.assertEqual(next30["N_leak"], CYCLE863_N_LEAK)
        self.assertEqual(next30["N_leak"], 0)
        self.assertEqual(next30["hits_I"], CYCLE863_HITS_I)
        self.assertEqual(next30["hits_I"], 15)
        self.assertEqual(next30["N_hpq_ge1"], 0)
        self.assertEqual(next30["N_exact0_abc"], 15)
        self.assertEqual(next30["N_with_next30"], 15)
        self.assertEqual(next30["N_no_next30"], 3)
        self.assertEqual(next30["next_cheap_lock"], STANDING_NAMED_BY_CYCLE863)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE863, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT30_REFRAMED)
        next31 = self.survey[CYCLE864_RESULT]
        self.assertEqual(next31["cycle"], STANDING_NEXT31_REFRAMED_CYCLE)
        self.assertEqual(next31["verdict"], CYCLE864_VERDICT)
        self.assertEqual(next31["verdict"], "incomplete-set LOSE")
        self.assertEqual(next31["N_hold"], CYCLE864_N_HOLD)
        self.assertEqual(next31["N_hold"], 0)
        self.assertEqual(next31["N_leak"], CYCLE864_N_LEAK)
        self.assertEqual(next31["N_leak"], 0)
        self.assertEqual(next31["hits_I"], CYCLE864_HITS_I)
        self.assertEqual(next31["hits_I"], 15)
        self.assertEqual(next31["N_hpq_ge1"], 0)
        self.assertEqual(next31["N_exact0_abc"], 15)
        self.assertEqual(next31["N_with_next31"], 15)
        self.assertEqual(next31["N_no_next31"], 3)
        self.assertEqual(next31["next_cheap_lock"], STANDING_NAMED_BY_CYCLE864)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE864, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT31_REFRAMED)
        next32 = self.survey[CYCLE865_RESULT]
        self.assertEqual(next32["cycle"], STANDING_NEXT32_REFRAMED_CYCLE)
        self.assertEqual(next32["verdict"], CYCLE865_VERDICT)
        self.assertEqual(next32["verdict"], "incomplete-set LOSE")
        self.assertEqual(next32["N_hold"], CYCLE865_N_HOLD)
        self.assertEqual(next32["N_hold"], 0)
        self.assertEqual(next32["N_leak"], CYCLE865_N_LEAK)
        self.assertEqual(next32["N_leak"], 0)
        self.assertEqual(next32["hits_I"], CYCLE865_HITS_I)
        self.assertEqual(next32["hits_I"], 15)
        self.assertEqual(next32["N_hpq_ge1"], 0)
        self.assertEqual(next32["N_exact0_abc"], 15)
        self.assertEqual(next32["N_with_next32"], 15)
        self.assertEqual(next32["N_no_next32"], 3)
        self.assertEqual(next32["next_cheap_lock"], STANDING_NAMED_BY_CYCLE865)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE865, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT32_REFRAMED)
        next33 = self.survey[CYCLE866_RESULT]
        self.assertEqual(next33["cycle"], STANDING_NEXT33_REFRAMED_CYCLE)
        self.assertEqual(next33["verdict"], CYCLE866_VERDICT)
        self.assertEqual(next33["verdict"], "incomplete-set LOSE")
        self.assertEqual(next33["N_hold"], CYCLE866_N_HOLD)
        self.assertEqual(next33["N_hold"], 0)
        self.assertEqual(next33["N_leak"], CYCLE866_N_LEAK)
        self.assertEqual(next33["N_leak"], 0)
        self.assertEqual(next33["hits_I"], CYCLE866_HITS_I)
        self.assertEqual(next33["hits_I"], 15)
        self.assertEqual(next33["N_hpq_ge1"], 0)
        self.assertEqual(next33["N_exact0_abc"], 15)
        self.assertEqual(next33["N_with_next33"], 15)
        self.assertEqual(next33["N_no_next33"], 3)
        self.assertEqual(next33["next_cheap_lock"], STANDING_NAMED_BY_CYCLE866)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE866, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT33_REFRAMED)
        next34 = self.survey[CYCLE867_RESULT]
        self.assertEqual(next34["cycle"], STANDING_NEXT34_REFRAMED_CYCLE)
        self.assertEqual(next34["verdict"], CYCLE867_VERDICT)
        self.assertEqual(next34["verdict"], "incomplete-set LOSE")
        self.assertEqual(next34["N_hold"], CYCLE867_N_HOLD)
        self.assertEqual(next34["N_hold"], 0)
        self.assertEqual(next34["N_leak"], CYCLE867_N_LEAK)
        self.assertEqual(next34["N_leak"], 0)
        self.assertEqual(next34["hits_I"], CYCLE867_HITS_I)
        self.assertEqual(next34["hits_I"], 15)
        self.assertEqual(next34["N_hpq_ge1"], 0)
        self.assertEqual(next34["N_exact0_abc"], 15)
        self.assertEqual(next34["N_with_next34"], 15)
        self.assertEqual(next34["N_no_next34"], 3)
        self.assertEqual(next34["next_cheap_lock"], STANDING_NAMED_BY_CYCLE867)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE867, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT34_REFRAMED)
        next35 = self.survey[CYCLE868_RESULT]
        self.assertEqual(next35["cycle"], STANDING_NEXT35_REFRAMED_CYCLE)
        self.assertEqual(next35["verdict"], CYCLE868_VERDICT)
        self.assertEqual(next35["verdict"], "incomplete-set LOSE")
        self.assertEqual(next35["N_hold"], CYCLE868_N_HOLD)
        self.assertEqual(next35["N_hold"], 0)
        self.assertEqual(next35["N_leak"], CYCLE868_N_LEAK)
        self.assertEqual(next35["N_leak"], 0)
        self.assertEqual(next35["hits_I"], CYCLE868_HITS_I)
        self.assertEqual(next35["hits_I"], 15)
        self.assertEqual(next35["N_hpq_ge1"], 0)
        self.assertEqual(next35["N_exact0_abc"], 15)
        self.assertEqual(next35["N_with_next35"], 15)
        self.assertEqual(next35["N_no_next35"], 3)
        self.assertEqual(next35["next_cheap_lock"], STANDING_NAMED_BY_CYCLE868)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE868, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT35_REFRAMED)
        next36 = self.survey[CYCLE869_RESULT]
        self.assertEqual(next36["cycle"], STANDING_NEXT36_REFRAMED_CYCLE)
        self.assertEqual(next36["verdict"], CYCLE869_VERDICT)
        self.assertEqual(next36["verdict"], "incomplete-set LOSE")
        self.assertEqual(next36["N_hold"], CYCLE869_N_HOLD)
        self.assertEqual(next36["N_hold"], 0)
        self.assertEqual(next36["N_leak"], CYCLE869_N_LEAK)
        self.assertEqual(next36["N_leak"], 0)
        self.assertEqual(next36["hits_I"], CYCLE869_HITS_I)
        self.assertEqual(next36["hits_I"], 15)
        self.assertEqual(next36["N_hpq_ge1"], 0)
        self.assertEqual(next36["N_exact0_abc"], 15)
        self.assertEqual(next36["N_with_next36"], 15)
        self.assertEqual(next36["N_no_next36"], 3)
        self.assertEqual(next36["next_cheap_lock"], STANDING_NAMED_BY_CYCLE869)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE869, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT36_REFRAMED)
        next37 = self.survey[CYCLE870_RESULT]
        self.assertEqual(next37["cycle"], STANDING_NEXT37_REFRAMED_CYCLE)
        self.assertEqual(next37["verdict"], CYCLE870_VERDICT)
        self.assertEqual(next37["verdict"], "incomplete-set LOSE")
        self.assertEqual(next37["N_hold"], CYCLE870_N_HOLD)
        self.assertEqual(next37["N_hold"], 0)
        self.assertEqual(next37["N_leak"], CYCLE870_N_LEAK)
        self.assertEqual(next37["N_leak"], 0)
        self.assertEqual(next37["hits_I"], CYCLE870_HITS_I)
        self.assertEqual(next37["hits_I"], 15)
        self.assertEqual(next37["N_hpq_ge1"], 0)
        self.assertEqual(next37["N_exact0_abc"], 15)
        self.assertEqual(next37["N_with_next37"], 15)
        self.assertEqual(next37["N_no_next37"], 3)
        self.assertEqual(next37["next_cheap_lock"], STANDING_NAMED_BY_CYCLE870)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE870, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT37_REFRAMED)
        next38 = self.survey[CYCLE871_RESULT]
        self.assertEqual(next38["cycle"], STANDING_NEXT38_REFRAMED_CYCLE)
        self.assertEqual(next38["verdict"], CYCLE871_VERDICT)
        self.assertEqual(next38["verdict"], "incomplete-set LOSE")
        self.assertEqual(next38["N_hold"], CYCLE871_N_HOLD)
        self.assertEqual(next38["N_hold"], 0)
        self.assertEqual(next38["N_leak"], CYCLE871_N_LEAK)
        self.assertEqual(next38["N_leak"], 0)
        self.assertEqual(next38["hits_I"], CYCLE871_HITS_I)
        self.assertEqual(next38["hits_I"], 15)
        self.assertEqual(next38["N_hpq_ge1"], 0)
        self.assertEqual(next38["N_exact0_abc"], 15)
        self.assertEqual(next38["N_with_next38"], 15)
        self.assertEqual(next38["N_no_next38"], 3)
        self.assertEqual(next38["next_cheap_lock"], STANDING_NAMED_BY_CYCLE871)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE871, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT38_REFRAMED)
        next39 = self.survey[CYCLE872_RESULT]
        self.assertEqual(next39["cycle"], STANDING_NEXT39_REFRAMED_CYCLE)
        self.assertEqual(next39["verdict"], CYCLE872_VERDICT)
        self.assertEqual(next39["verdict"], "incomplete-set LOSE")
        self.assertEqual(next39["N_hold"], CYCLE872_N_HOLD)
        self.assertEqual(next39["N_hold"], 0)
        self.assertEqual(next39["N_leak"], CYCLE872_N_LEAK)
        self.assertEqual(next39["N_leak"], 0)
        self.assertEqual(next39["hits_I"], CYCLE872_HITS_I)
        self.assertEqual(next39["hits_I"], 15)
        self.assertEqual(next39["N_hpq_ge1"], 0)
        self.assertEqual(next39["N_exact0_abc"], 15)
        self.assertEqual(next39["N_with_next39"], 15)
        self.assertEqual(next39["N_no_next39"], 3)
        self.assertEqual(next39["next_cheap_lock"], STANDING_NAMED_BY_CYCLE872)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE872, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT39_REFRAMED)
        next40 = self.survey[CYCLE873_RESULT]
        self.assertEqual(next40["cycle"], STANDING_NEXT40_REFRAMED_CYCLE)
        self.assertEqual(next40["verdict"], CYCLE873_VERDICT)
        self.assertEqual(next40["verdict"], "incomplete-set LOSE")
        self.assertEqual(next40["N_hold"], CYCLE873_N_HOLD)
        self.assertEqual(next40["N_hold"], 0)
        self.assertEqual(next40["N_leak"], CYCLE873_N_LEAK)
        self.assertEqual(next40["N_leak"], 0)
        self.assertEqual(next40["hits_I"], CYCLE873_HITS_I)
        self.assertEqual(next40["hits_I"], 15)
        self.assertEqual(next40["N_hpq_ge1"], 0)
        self.assertEqual(next40["N_exact0_abc"], 15)
        self.assertEqual(next40["N_with_next40"], 15)
        self.assertEqual(next40["N_no_next40"], 3)
        self.assertEqual(next40["next_cheap_lock"], STANDING_NAMED_BY_CYCLE873)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE873, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT40_REFRAMED)
        next41 = self.survey[CYCLE874_RESULT]
        self.assertEqual(next41["cycle"], STANDING_NEXT41_REFRAMED_CYCLE)
        self.assertEqual(next41["verdict"], CYCLE874_VERDICT)
        self.assertEqual(next41["verdict"], "incomplete-set LOSE")
        self.assertEqual(next41["N_hold"], CYCLE874_N_HOLD)
        self.assertEqual(next41["N_hold"], 0)
        self.assertEqual(next41["N_leak"], CYCLE874_N_LEAK)
        self.assertEqual(next41["N_leak"], 0)
        self.assertEqual(next41["hits_I"], CYCLE874_HITS_I)
        self.assertEqual(next41["hits_I"], 15)
        self.assertEqual(next41["N_hpq_ge1"], 0)
        self.assertEqual(next41["N_exact0_abc"], 15)
        self.assertEqual(next41["N_with_next41"], 15)
        self.assertEqual(next41["N_no_next41"], 3)
        self.assertEqual(next41["next_cheap_lock"], STANDING_NAMED_BY_CYCLE874)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE874, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT41_REFRAMED)
        next42 = self.survey[CYCLE875_RESULT]
        self.assertEqual(next42["cycle"], STANDING_NEXT42_REFRAMED_CYCLE)
        self.assertEqual(next42["verdict"], CYCLE875_VERDICT)
        self.assertEqual(next42["verdict"], "incomplete-set LOSE")
        self.assertEqual(next42["N_hold"], CYCLE875_N_HOLD)
        self.assertEqual(next42["N_hold"], 0)
        self.assertEqual(next42["N_leak"], CYCLE875_N_LEAK)
        self.assertEqual(next42["N_leak"], 0)
        self.assertEqual(next42["hits_I"], CYCLE875_HITS_I)
        self.assertEqual(next42["hits_I"], 15)
        self.assertEqual(next42["N_hpq_ge1"], 0)
        self.assertEqual(next42["N_exact0_abc"], 15)
        self.assertEqual(next42["N_with_next42"], 15)
        self.assertEqual(next42["N_no_next42"], 3)
        self.assertEqual(next42["next_cheap_lock"], STANDING_NAMED_BY_CYCLE875)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE875, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT42_REFRAMED)
        next43 = self.survey[CYCLE876_RESULT]
        self.assertEqual(next43["cycle"], STANDING_NEXT43_REFRAMED_CYCLE)
        self.assertEqual(next43["verdict"], CYCLE876_VERDICT)
        self.assertEqual(next43["verdict"], "incomplete-set LOSE")
        self.assertEqual(next43["N_hold"], CYCLE876_N_HOLD)
        self.assertEqual(next43["N_hold"], 0)
        self.assertEqual(next43["N_leak"], CYCLE876_N_LEAK)
        self.assertEqual(next43["N_leak"], 0)
        self.assertEqual(next43["hits_I"], CYCLE876_HITS_I)
        self.assertEqual(next43["hits_I"], 14)
        self.assertEqual(next43["N_hpq_ge1"], 0)
        self.assertEqual(next43["N_exact0_abc"], 14)
        self.assertEqual(next43["N_with_next43"], 14)
        self.assertEqual(next43["N_no_next43"], 4)
        self.assertEqual(next43["next_cheap_lock"], STANDING_NAMED_BY_CYCLE876)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE876, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT43_REFRAMED)
        next44 = self.survey[CYCLE877_RESULT]
        self.assertEqual(next44["cycle"], STANDING_NEXT44_REFRAMED_CYCLE)
        self.assertEqual(next44["verdict"], CYCLE877_VERDICT)
        self.assertEqual(next44["verdict"], "incomplete-set LOSE")
        self.assertEqual(next44["N_hold"], CYCLE877_N_HOLD)
        self.assertEqual(next44["N_hold"], 0)
        self.assertEqual(next44["N_leak"], CYCLE877_N_LEAK)
        self.assertEqual(next44["N_leak"], 0)
        self.assertEqual(next44["hits_I"], CYCLE877_HITS_I)
        self.assertEqual(next44["hits_I"], 13)
        self.assertEqual(next44["N_hpq_ge1"], 0)
        self.assertEqual(next44["N_exact0_abc"], 13)
        self.assertEqual(next44["N_with_next44"], 13)
        self.assertEqual(next44["N_no_next44"], 5)
        self.assertEqual(next44["next_cheap_lock"], STANDING_NAMED_BY_CYCLE877)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE877, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT44_REFRAMED)
        next45 = self.survey[CYCLE878_RESULT]
        self.assertEqual(next45["cycle"], STANDING_NEXT45_REFRAMED_CYCLE)
        self.assertEqual(next45["verdict"], CYCLE878_VERDICT)
        self.assertEqual(next45["verdict"], "incomplete-set LOSE")
        self.assertEqual(next45["N_hold"], CYCLE878_N_HOLD)
        self.assertEqual(next45["N_hold"], 0)
        self.assertEqual(next45["N_leak"], CYCLE878_N_LEAK)
        self.assertEqual(next45["N_leak"], 0)
        self.assertEqual(next45["hits_I"], CYCLE878_HITS_I)
        self.assertEqual(next45["hits_I"], 12)
        self.assertEqual(next45["N_hpq_ge1"], 0)
        self.assertEqual(next45["N_exact0_abc"], 12)
        self.assertEqual(next45["N_with_next45"], 12)
        self.assertEqual(next45["N_no_next45"], 6)
        self.assertEqual(next45["next_cheap_lock"], STANDING_NAMED_BY_CYCLE878)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE878, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT45_REFRAMED)
        next46 = self.survey[CYCLE879_RESULT]
        self.assertEqual(next46["cycle"], STANDING_NEXT46_REFRAMED_CYCLE)
        self.assertEqual(next46["verdict"], CYCLE879_VERDICT)
        self.assertEqual(next46["verdict"], "incomplete-set LOSE")
        self.assertEqual(next46["N_hold"], CYCLE879_N_HOLD)
        self.assertEqual(next46["N_hold"], 0)
        self.assertEqual(next46["N_leak"], CYCLE879_N_LEAK)
        self.assertEqual(next46["N_leak"], 0)
        self.assertEqual(next46["hits_I"], CYCLE879_HITS_I)
        self.assertEqual(next46["hits_I"], 12)
        self.assertEqual(next46["N_hpq_ge1"], 0)
        self.assertEqual(next46["N_exact0_abc"], 12)
        self.assertEqual(next46["N_with_next46"], 12)
        self.assertEqual(next46["N_no_next46"], 6)
        self.assertEqual(next46["next_cheap_lock"], STANDING_NAMED_BY_CYCLE879)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE879, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT46_REFRAMED)
        next47 = self.survey[CYCLE880_RESULT]
        self.assertEqual(next47["cycle"], STANDING_NEXT47_REFRAMED_CYCLE)
        self.assertEqual(next47["verdict"], CYCLE880_VERDICT)
        self.assertEqual(next47["verdict"], "incomplete-set LOSE")
        self.assertEqual(next47["N_hold"], CYCLE880_N_HOLD)
        self.assertEqual(next47["N_hold"], 0)
        self.assertEqual(next47["N_leak"], CYCLE880_N_LEAK)
        self.assertEqual(next47["N_leak"], 0)
        self.assertEqual(next47["hits_I"], CYCLE880_HITS_I)
        self.assertEqual(next47["hits_I"], 12)
        self.assertEqual(next47["N_hpq_ge1"], 0)
        self.assertEqual(next47["N_exact0_abc"], 12)
        self.assertEqual(next47["N_with_next47"], 12)
        self.assertEqual(next47["N_no_next47"], 6)
        self.assertEqual(next47["next_cheap_lock"], STANDING_NAMED_BY_CYCLE880)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE880, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT47_REFRAMED)
        next48 = self.survey[CYCLE881_RESULT]
        self.assertEqual(next48["cycle"], STANDING_NEXT48_REFRAMED_CYCLE)
        self.assertEqual(next48["verdict"], CYCLE881_VERDICT)
        self.assertEqual(next48["verdict"], "incomplete-set LOSE")
        self.assertEqual(next48["N_hold"], CYCLE881_N_HOLD)
        self.assertEqual(next48["N_hold"], 0)
        self.assertEqual(next48["N_leak"], CYCLE881_N_LEAK)
        self.assertEqual(next48["N_leak"], 0)
        self.assertEqual(next48["hits_I"], CYCLE881_HITS_I)
        self.assertEqual(next48["hits_I"], 12)
        self.assertEqual(next48["N_hpq_ge1"], 0)
        self.assertEqual(next48["N_exact0_abc"], 12)
        self.assertEqual(next48["N_with_next48"], 12)
        self.assertEqual(next48["N_no_next48"], 6)
        self.assertEqual(next48["next_cheap_lock"], STANDING_NAMED_BY_CYCLE881)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE881, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT48_REFRAMED)
        next49 = self.survey[CYCLE882_RESULT]
        self.assertEqual(next49["cycle"], STANDING_NEXT49_REFRAMED_CYCLE)
        self.assertEqual(next49["verdict"], CYCLE882_VERDICT)
        self.assertEqual(next49["verdict"], "incomplete-set LOSE")
        self.assertEqual(next49["N_hold"], CYCLE882_N_HOLD)
        self.assertEqual(next49["N_hold"], 0)
        self.assertEqual(next49["N_leak"], CYCLE882_N_LEAK)
        self.assertEqual(next49["N_leak"], 0)
        self.assertEqual(next49["hits_I"], CYCLE882_HITS_I)
        self.assertEqual(next49["hits_I"], 12)
        self.assertEqual(next49["N_hpq_ge1"], 0)
        self.assertEqual(next49["N_exact0_abc"], 12)
        self.assertEqual(next49["N_with_next49"], 12)
        self.assertEqual(next49["N_no_next49"], 6)
        self.assertEqual(next49["next_cheap_lock"], STANDING_NAMED_BY_CYCLE882)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE882, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT49_REFRAMED)
        next50 = self.survey[CYCLE883_RESULT]
        self.assertEqual(next50["cycle"], STANDING_NEXT50_REFRAMED_CYCLE)
        self.assertEqual(next50["verdict"], CYCLE883_VERDICT)
        self.assertEqual(next50["verdict"], "incomplete-set LOSE")
        self.assertEqual(next50["N_hold"], CYCLE883_N_HOLD)
        self.assertEqual(next50["N_hold"], 0)
        self.assertEqual(next50["N_leak"], CYCLE883_N_LEAK)
        self.assertEqual(next50["N_leak"], 0)
        self.assertEqual(next50["hits_I"], CYCLE883_HITS_I)
        self.assertEqual(next50["hits_I"], 12)
        self.assertEqual(next50["N_hpq_ge1"], 0)
        self.assertEqual(next50["N_exact0_abc"], 12)
        self.assertEqual(next50["N_with_next50"], 12)
        self.assertEqual(next50["N_no_next50"], 6)
        self.assertEqual(next50["next_cheap_lock"], STANDING_NAMED_BY_CYCLE883)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE883, self.survey)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT50_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLES_832_883)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_measured_table_is_incomplete_set_lose(self):
        """H/P/Q and A/B/C are exact-0. hits_I is 12 and is not a leak."""
        self.assertEqual(self.summary["N"], STANDING_N)
        self.assertEqual(self.summary["N_hpq_ge1"], STANDING_N_HPQ_GE1)
        self.assertEqual(self.summary["N_hpq_ge2"], STANDING_N_HPQ_GE2)
        self.assertEqual(self.summary["N_exact0_abc"], STANDING_N_EXACT0_ABC)
        self.assertEqual(self.summary["N_i_ge1"], STANDING_N_I_GE1)
        self.assertEqual(self.summary["N_exact0_i"], STANDING_N_EXACT0_I)
        self.assertEqual(self.summary["N_leak"], STANDING_N_LEAK)
        self.assertEqual(self.summary["N_hold"], STANDING_N_HOLD)
        self.assertEqual(self.summary["hits_H"], STANDING_HITS_H)
        self.assertEqual(self.summary["hits_P"], STANDING_HITS_P)
        self.assertEqual(self.summary["hits_Q"], STANDING_HITS_Q)
        self.assertEqual(self.summary["hits_A"], STANDING_HITS_A)
        self.assertEqual(self.summary["hits_B"], STANDING_HITS_B)
        self.assertEqual(self.summary["hits_C"], STANDING_HITS_C)
        self.assertEqual(self.summary["hits_I"], STANDING_HITS_I)
        self.assertEqual(self.summary["N_hpq_ge1"], 0)
        self.assertEqual(self.summary["N_leak"], 0)
        self.assertEqual(self.summary["N_hold"], 0)
        self.assertEqual(self.summary["hits_I"], 12)
        self.assertEqual(tuple(row.hits[-1] for row in self.rows), CYCLE565_N_I_EACH)
        self.assertEqual(CYCLE565_N_I_EACH, (1,) * STANDING_N)
        for index, row in enumerate(self.rows):
            self.assertEqual(row.hits, STANDING_HITS[index])
            hits = row.as_map()
            self.assertEqual(hits["I"], 1)
            self.assertEqual(hits["H"], 0)
            self.assertEqual(hits["P"], 0)
            self.assertEqual(hits["Q"], 0)
            self.assertEqual(hits["A"], 0)
            self.assertEqual(hits["B"], 0)
            self.assertEqual(hits["C"], 0)
            self.assertFalse(row_holds(hits))
            self.assertFalse(row_leaks(hits))
            self.assertEqual(hpq_tablets_hit(hits), 0)
            self.assertEqual(absent_hit_sum(hits), 0)
            self.assertIn(index, STANDING_INCOMPLETE_INDEXES)
        self.assertTrue(STANDING_NEXT50_ALL_EXTEND)
        for n50, n51, site50, site51 in zip(
            CYCLE883_SEQUENCES, STANDING_SEQUENCES, CYCLE883_SITES, STANDING_SITES, strict=True
        ):
            self.assertEqual(n51[:50], n50)
            self.assertEqual(site51, site50)
        still = self.rows[STANDING_NEXT50_HAPAX_STILL_HAPAX[0]]
        self.assertEqual(
            still.tokens,
            (
                "604", "076", "071", "600", "999", "050", "076", "000",
                "002", "999", "076", "092", "535", "999", "208", "076",
                "532", "244", "999", "090", "076", "057", "600", "700",
                "076", "076", "053", "177", "700", "076", "057", "741",
                "430", "076", "532", "200", "059", "076", "074", "379",
                "002", "076", "244", "280", "001", "076", "532", "071",
                "065", "071", "999",
            ),
        )
        self.assertEqual(still.site, ("Ia", "Ia9", 9))
        self.assertEqual(still.as_map()["I"], 1)
        self.assertEqual(still.tokens[:50], CYCLE883_SEQUENCES[3])
        self.assertEqual(CYCLE883_SITES[3], ("Ia", "Ia9", 9))
        dropped_tokens = CYCLE840_SEQUENCES[CYCLE841_NEXT7_DROPPED_INDEX]
        dropped_site = CYCLE840_SITES[CYCLE841_NEXT7_DROPPED_INDEX]
        self.assertEqual(
            dropped_tokens,
            ("720", "076", "070", "701", "214", "076", "298"),
        )
        self.assertEqual(dropped_site, ("Ia", "Ia8", 171))
        self.assertFalse(any(tokens[:7] == dropped_tokens for tokens in STANDING_SEQUENCES))
        self.assertIn(("Ia", "Ia10", 144), STANDING_NO_NEXT51_SITES)
        self.assertIn(("Ia", "Ia10", 143), STANDING_NO_NEXT51_SITES)
        self.assertIn(("Ia", "Ia10", 142), STANDING_NO_NEXT51_SITES)
        self.assertIn(("Ia", "Ia8", 167), STANDING_NO_NEXT51_SITES)
        self.assertIn(("Ia", "Ia8", 166), STANDING_NO_NEXT51_SITES)
        self.assertIn(("Ia", "Ia8", 165), STANDING_NO_NEXT51_SITES)
        self.assertEqual(STANDING_HOLD_INDEXES, ())
        self.assertEqual(STANDING_I_GT1_INDEXES, ())
        self.assertEqual(len(STANDING_INCOMPLETE_INDEXES), STANDING_N)
        self.assertEqual(self.verdict, STANDING_VERDICT)
        self.assertEqual(self.verdict, "incomplete-set LOSE")
        self.assertFalse(STANDING_CLAIM_HOLDS)
        self.assertFalse(STANDING_PARENT_COMPLETE)
        self.assertEqual(STANDING_N_NO_NEXT51, 6)
        self.assertEqual(STANDING_AXIS, "closed-tradition-reframed")
        self.assertEqual(MIN_HPQ_TABLETS, 1)
        self.assertEqual(PROBE_TABLETS, HPQ_TABLETS + ABSENT_TABLETS + ("I",))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_window_peels_closed_and_prev1_list_is_absent(self):
        """No new peel. Prev-1 of leftover-6 is not a locked gram list."""
        for key, cycle in STANDING_ORDER_ALREADY_LOCKED:
            self.assertEqual(self.survey[key]["cycle"], cycle)
        for key, cycle in STANDING_GAPS_ALREADY_LOCKED:
            self.assertEqual(self.survey[key]["cycle"], cycle)
        for key, cycle in STANDING_INVENTORY_ALREADY_LOCKED:
            self.assertEqual(self.survey[key]["cycle"], cycle)
        prior = self.survey[CYCLE831_SURVEY_KEY]
        self.assertEqual(prior["cycle"], 831)
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_with_next184"], 0)
        self.assertEqual(prior["N_no_next184"], 18)
        self.assertTrue(STANDING_WINDOW_PEELS_CLOSED)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_PREV184)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT185)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_PREV10)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_LEFTOVER_10GRAMS)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT13)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT14)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT15)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT16)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT17)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT18)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT19)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT20)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT21)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT22)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT23)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT24)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT25)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT26)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT27)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT28)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT29)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT30)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT31)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT32)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT33)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT34)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT35)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT36)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT37)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT38)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT39)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT40)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT41)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT42)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT43)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT44)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT45)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT46)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT47)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT48)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT49)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT50)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT51)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT52)
        self.assertTrue(STANDING_PREV1_GRAM_LIST_ABSENT)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_PREV1_PEEL)
        self.assertFalse(PREV1_N6_SCOREBOARD.exists())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_next_cheap_lock_is_the_locked_cycle_567_next52_list(self):
        """Cycle 567 next-52 I-only list stays locked. The claim name is not a survey key."""
        self.assertEqual(CYCLE567_N, 18)
        self.assertEqual(CYCLE567_N_SEQUENCES, 12)
        self.assertEqual(len(CYCLE567_SEQUENCES), 12)
        self.assertTrue(all(len(tokens) == 52 for tokens in CYCLE567_SEQUENCES))
        self.assertTrue(CYCLE567_HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE567_ALL_I_ONLY_CLAIM)
        self.assertEqual(CYCLE567_N_I_ONLY, 12)
        self.assertEqual(CYCLE567_N_LEAK, 0)
        self.assertEqual(CYCLE567_N_WITH_NEXT52, 12)
        self.assertEqual(CYCLE567_N_NO_NEXT52, 6)
        self.assertEqual(
            CYCLE567_NO_NEXT52_SITES,
            (
                ("Ia", "Ia10", 144),
                ("Ia", "Ia10", 143),
                ("Ia", "Ia10", 142),
                ("Ia", "Ia8", 167),
                ("Ia", "Ia8", 166),
                ("Ia", "Ia8", 165),
            ),
        )
        prior = self.survey[CYCLE567_RESULT]
        all_i_only_key = (
            "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
            "remaining_after_076_020_remaining_after_076_010_next_52grams_all_i_only"
        )
        self.assertEqual(CYCLE567_RESULT, (
            "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
            "remaining_after_076_020_remaining_after_076_010_next52_i_only"
        ))
        self.assertEqual(prior["cycle"], 567)
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_sequences"], 12)
        self.assertEqual(prior["N_6grams"], 18)
        self.assertTrue(prior["hypothesis_all_i_only"])
        self.assertFalse(prior[all_i_only_key])
        self.assertFalse(prior[CYCLE567_RESULT])
        self.assertEqual(prior["N_i_only"], 12)
        self.assertEqual(prior["N_leak"], 0)
        self.assertEqual(prior["N_no_next52"], 6)
        self.assertEqual(prior["N_with_next52"], 12)
        self.assertNotIn(STANDING_NEXT_CHEAP_LOCK, self.survey)
        self.assertNotIn("i_leftover_n6_next52_closed_tradition_hpq_abc", self.survey)
        self.assertEqual(
            STANDING_NEXT_CHEAP_LOCK,
            "cycle567_next52_reframed_closed_tradition_hpq_ge1_exact0_abc",
        )
        self.assertEqual(self.provider.get_call_history(), [])


    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-884 incomplete-set LOSE table."""
        lock = self.survey[STANDING_RESULT]
        self.assertEqual(lock["cycle"], 884)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["axis"], STANDING_AXIS)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertEqual(lock["verdict"], STANDING_VERDICT)
        self.assertEqual(lock["verdict"], self.verdict)
        self.assertFalse(lock["claim_holds"])
        self.assertEqual(lock["claim_holds"], STANDING_CLAIM_HOLDS)
        self.assertEqual(lock["N"], self.summary["N"])
        self.assertEqual(lock["N_parent"], STANDING_N_PARENT)
        self.assertEqual(lock["N_with_next51"], STANDING_N_WITH_NEXT51)
        self.assertEqual(lock["N_no_next51"], STANDING_N_NO_NEXT51)
        self.assertFalse(lock["parent_complete"])
        self.assertEqual(
            tuple(tuple(site) for site in lock["no_next51_sites"]),
            STANDING_NO_NEXT51_SITES,
        )
        self.assertEqual(lock["N_hpq_ge1"], self.summary["N_hpq_ge1"])
        self.assertEqual(lock["N_hpq_ge2"], self.summary["N_hpq_ge2"])
        self.assertEqual(lock["N_exact0_abc"], self.summary["N_exact0_abc"])
        self.assertEqual(lock["N_i_ge1"], self.summary["N_i_ge1"])
        self.assertEqual(lock["N_exact0_i"], self.summary["N_exact0_i"])
        self.assertEqual(lock["N_leak"], self.summary["N_leak"])
        self.assertEqual(lock["N_hold"], self.summary["N_hold"])
        self.assertEqual(lock["hits_H"], self.summary["hits_H"])
        self.assertEqual(lock["hits_P"], self.summary["hits_P"])
        self.assertEqual(lock["hits_Q"], self.summary["hits_Q"])
        self.assertEqual(lock["hits_A"], self.summary["hits_A"])
        self.assertEqual(lock["hits_B"], self.summary["hits_B"])
        self.assertEqual(lock["hits_C"], self.summary["hits_C"])
        self.assertEqual(lock["hits_I"], self.summary["hits_I"])
        self.assertEqual(lock["min_hpq"], MIN_HPQ_TABLETS)
        self.assertEqual(tuple(lock["absent_tablets"]), ABSENT_TABLETS)
        self.assertEqual(tuple(lock["probe_tablets"]), PROBE_TABLETS)
        self.assertFalse(lock["i_in_absent_set"])
        self.assertTrue(lock["i_only_already_locked"])
        self.assertEqual(lock["i_only_cycle"], STANDING_I_ONLY_CYCLE)
        self.assertTrue(lock["do_not_relock_i_only"])
        self.assertEqual(lock["parent_i_local_cycle"], STANDING_PARENT_I_LOCAL_CYCLE)
        self.assertTrue(lock["do_not_relock_parent_i_local"])
        self.assertEqual(lock["next1_reframed_cycle"], STANDING_NEXT1_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next1_reframed"])
        self.assertEqual(lock["next2_reframed_cycle"], STANDING_NEXT2_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next2_reframed"])
        self.assertEqual(lock["next3_reframed_cycle"], STANDING_NEXT3_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next3_reframed"])
        self.assertEqual(lock["next4_reframed_cycle"], STANDING_NEXT4_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next4_reframed"])
        self.assertEqual(lock["next5_reframed_cycle"], STANDING_NEXT5_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next5_reframed"])
        self.assertEqual(lock["next6_reframed_cycle"], STANDING_NEXT6_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next6_reframed"])
        self.assertEqual(lock["next7_reframed_cycle"], STANDING_NEXT7_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next7_reframed"])
        self.assertEqual(lock["next8_reframed_cycle"], STANDING_NEXT8_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next8_reframed"])
        self.assertEqual(lock["next9_reframed_cycle"], STANDING_NEXT9_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next9_reframed"])
        self.assertEqual(lock["next10_reframed_cycle"], STANDING_NEXT10_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next10_reframed"])
        self.assertEqual(lock["next11_reframed_cycle"], STANDING_NEXT11_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next11_reframed"])
        self.assertEqual(lock["next12_reframed_cycle"], STANDING_NEXT12_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next12_reframed"])
        self.assertEqual(lock["next13_reframed_cycle"], STANDING_NEXT13_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next13_reframed"])
        self.assertEqual(lock["next14_reframed_cycle"], STANDING_NEXT14_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next14_reframed"])
        self.assertEqual(lock["next15_reframed_cycle"], STANDING_NEXT15_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next15_reframed"])
        self.assertEqual(lock["next16_reframed_cycle"], STANDING_NEXT16_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next16_reframed"])
        self.assertEqual(lock["next17_reframed_cycle"], STANDING_NEXT17_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next17_reframed"])
        self.assertEqual(lock["next18_reframed_cycle"], STANDING_NEXT18_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next18_reframed"])
        self.assertEqual(lock["next19_reframed_cycle"], STANDING_NEXT19_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next19_reframed"])
        self.assertEqual(lock["next20_reframed_cycle"], STANDING_NEXT20_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next20_reframed"])
        self.assertEqual(lock["next21_reframed_cycle"], STANDING_NEXT21_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next21_reframed"])
        self.assertEqual(lock["next22_reframed_cycle"], STANDING_NEXT22_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next22_reframed"])
        self.assertEqual(lock["next23_reframed_cycle"], STANDING_NEXT23_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next23_reframed"])
        self.assertEqual(lock["next24_reframed_cycle"], STANDING_NEXT24_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next24_reframed"])
        self.assertEqual(lock["next25_reframed_cycle"], STANDING_NEXT25_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next25_reframed"])
        self.assertEqual(lock["next26_reframed_cycle"], STANDING_NEXT26_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next26_reframed"])
        self.assertEqual(lock["next27_reframed_cycle"], STANDING_NEXT27_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next27_reframed"])
        self.assertEqual(lock["next28_reframed_cycle"], STANDING_NEXT28_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next28_reframed"])
        self.assertEqual(lock["next29_reframed_cycle"], STANDING_NEXT29_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next29_reframed"])
        self.assertEqual(lock["next30_reframed_cycle"], STANDING_NEXT30_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next30_reframed"])
        self.assertEqual(lock["next31_reframed_cycle"], STANDING_NEXT31_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next31_reframed"])
        self.assertEqual(lock["next32_reframed_cycle"], STANDING_NEXT32_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next32_reframed"])
        self.assertEqual(lock["next33_reframed_cycle"], STANDING_NEXT33_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next33_reframed"])
        self.assertEqual(lock["next34_reframed_cycle"], STANDING_NEXT34_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next34_reframed"])
        self.assertEqual(lock["next35_reframed_cycle"], STANDING_NEXT35_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next35_reframed"])
        self.assertEqual(lock["next36_reframed_cycle"], STANDING_NEXT36_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next36_reframed"])
        self.assertEqual(lock["next37_reframed_cycle"], STANDING_NEXT37_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next37_reframed"])
        self.assertEqual(lock["next38_reframed_cycle"], STANDING_NEXT38_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next38_reframed"])
        self.assertEqual(lock["next39_reframed_cycle"], STANDING_NEXT39_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next39_reframed"])
        self.assertEqual(lock["next40_reframed_cycle"], STANDING_NEXT40_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next40_reframed"])
        self.assertEqual(lock["next41_reframed_cycle"], STANDING_NEXT41_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next41_reframed"])
        self.assertEqual(lock["next42_reframed_cycle"], STANDING_NEXT42_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next42_reframed"])
        self.assertEqual(lock["next43_reframed_cycle"], STANDING_NEXT43_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next43_reframed"])
        self.assertEqual(lock["next44_reframed_cycle"], STANDING_NEXT44_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next44_reframed"])
        self.assertEqual(lock["next45_reframed_cycle"], STANDING_NEXT45_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next45_reframed"])
        self.assertEqual(lock["next46_reframed_cycle"], STANDING_NEXT46_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next46_reframed"])
        self.assertEqual(lock["next47_reframed_cycle"], STANDING_NEXT47_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next47_reframed"])
        self.assertEqual(lock["next48_reframed_cycle"], STANDING_NEXT48_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next48_reframed"])
        self.assertEqual(lock["next49_reframed_cycle"], STANDING_NEXT49_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next49_reframed"])
        self.assertEqual(lock["next50_reframed_cycle"], STANDING_NEXT50_REFRAMED_CYCLE)
        self.assertTrue(lock["do_not_relock_next50_reframed"])
        self.assertTrue(lock["do_not_relock_cycles_832_883"])
        self.assertTrue(lock["window_peels_closed"])
        self.assertTrue(lock["prev1_gram_list_absent"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev1"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev10"])
        self.assertTrue(lock["do_not_launch_leftover_10grams"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next13"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next14"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next15"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next16"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next17"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next18"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next19"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next20"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next21"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next22"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next23"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next24"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next25"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next26"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next27"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next28"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next29"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next30"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next31"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next32"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next33"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next34"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next35"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next36"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next37"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next38"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next39"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next40"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next41"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next42"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next43"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next44"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next45"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next46"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next47"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next48"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next49"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next50"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next51"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next52"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev184"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next185"])
        self.assertEqual(lock["named_by_cycle872"], STANDING_NAMED_BY_CYCLE872)
        self.assertEqual(lock["named_by_cycle873"], STANDING_NAMED_BY_CYCLE873)
        self.assertEqual(lock["named_by_cycle874"], STANDING_NAMED_BY_CYCLE874)
        self.assertEqual(lock["named_by_cycle875"], STANDING_NAMED_BY_CYCLE875)
        self.assertEqual(lock["named_by_cycle876"], STANDING_NAMED_BY_CYCLE876)
        self.assertEqual(lock["named_by_cycle877"], STANDING_NAMED_BY_CYCLE877)
        self.assertEqual(lock["named_by_cycle878"], STANDING_NAMED_BY_CYCLE878)
        self.assertEqual(lock["named_by_cycle879"], STANDING_NAMED_BY_CYCLE879)
        self.assertEqual(lock["named_by_cycle880"], STANDING_NAMED_BY_CYCLE880)
        self.assertEqual(lock["named_by_cycle881"], STANDING_NAMED_BY_CYCLE881)
        self.assertEqual(lock["named_by_cycle882"], STANDING_NAMED_BY_CYCLE882)
        self.assertEqual(lock["named_by_cycle883"], STANDING_NAMED_BY_CYCLE883)
        self.assertEqual(lock["next_cheap_lock"], STANDING_NEXT_CHEAP_LOCK)
        self.assertEqual(tuple(lock["hold_indexes"]), STANDING_HOLD_INDEXES)
        self.assertEqual(tuple(lock["incomplete_indexes"]), STANDING_INCOMPLETE_INDEXES)
        self.assertEqual(tuple(lock["i_gt1_indexes"]), STANDING_I_GT1_INDEXES)
        self.assertEqual(
            tuple(lock["next50_hapax_still_hapax"]),
            STANDING_NEXT50_HAPAX_STILL_HAPAX,
        )
        self.assertTrue(lock["next50_all_extend"])
        self.assertEqual(lock["next50_all_extend"], STANDING_NEXT50_ALL_EXTEND)
        self.assertNotIn("leak_index", lock)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE882, self.survey)
        self.assertNotIn(STANDING_NEXT_CHEAP_LOCK, self.survey)
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["from_cycle"], STANDING_FROM_CYCLE)
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(len(lock["rows"]), 12)
        for recorded, row in zip(lock["rows"], self.rows, strict=True):
            self.assertEqual(tuple(recorded["tokens"]), row.tokens)
            self.assertEqual(tuple(recorded["site"]), row.site)
            self.assertEqual(tuple(recorded["hits"]), row.hits)
            self.assertEqual(recorded["tablets"], list(PROBE_TABLETS))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = self.survey["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)
        self.assertEqual(self.provider.get_call_history(), [])
