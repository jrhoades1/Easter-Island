"""Reframed closed-tradition hold-out of the locked leftover-6 next-15 grams.

Cycle 848 text-search lock. Uses already-vendored A–V and the
cycle-493 leftover n=6 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 remaining-
after-076-010 next 15-grams (15 sequences; parent N=18; three
line-final holes at Ia8[167], Ia8[166], and Ia8[165]).
HEAD-check: that gram list exists and is not yet locked under
this reframed rule. Cycle 493 already locked the I-only claim
on these 15-grams as incomplete-set LOSE (N_with_next15=15,
N_no_next15=3, N_i_only=15, N_leak=0). Cycle 847 already locked
the reframed claim on the cycle-491 next-14 grams as
incomplete-set LOSE. This cycle does not re-lock either claim,
and does not re-lock Cycles 832–847.

Claim that can lose: each existing next-15 gram is an exact
contiguous hit on ≥1 of H/P/Q and exact-0 on A/B/C. hits_I is
recorded and is not a leak. HOLD needs that claim true for a
complete population with zero A/B/C leak. Leak onto A/B/C is
leak LOSE. An empty H/P/Q hit set, or a parent set that still
has a line-final hole, is incomplete-set LOSE.

Named claim: cycle493_next15_reframed_closed_tradition_hpq_ge1_exact0_abc.

Measured on the 15 with-next15 grams: N=15, N_hpq_ge1=0,
N_hpq_ge2=0, N_exact0_abc=15, N_i_ge1=15, N_exact0_i=0,
N_leak=0, N_hold=0, hits_I=15. Parent N=18, N_with_next15=15,
N_no_next15=3 (Ia8[167], Ia8[166], Ia8[165]). Every scored gram
is exact-0 on H/P/Q and on A/B/C and an exact contiguous hit
once on I. The next-14 hapax 604 076 071 600 999 050 076 000
002 999 076 092 535 999 extends to 604 076 071 600 999 050 076
000 002 999 076 092 535 999 208 at Ia9[9] and hits I once. All
fifteen next-14 grams extend; no new hole. Verdict:
incomplete-set LOSE.

Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Does not reopen leftover-6
next/prev window peels (next-side exhausted at cycle 831;
prev-side eighteen-hole 0/18 since cycle 800). Leftover-6
prev-1 has no locked gram list; do not invent that peel.
Do not launch leftover-6 previous 10-grams, leftover 10-grams,
next 15-grams as a peel, next 16-grams as a peel, prev-184, or
next-185. The cycle-495 next-16 I-only list stays the named
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
from tests.test_mamari_i_leftover_n6_next14_closed_tradition_hpq_abc_scoreboard import (
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
    HPQ_TABLETS,
    MIN_HPQ_TABLETS,
    PREV1_N6_SCOREBOARD,
    PROBE_TABLETS,
    STANDING_HITS_I as CYCLE847_HITS_I,
    STANDING_N_HOLD as CYCLE847_N_HOLD,
    STANDING_N_LEAK as CYCLE847_N_LEAK,
    STANDING_NEXT_CHEAP_LOCK as CYCLE847_NEXT_CHEAP_LOCK,
    STANDING_NO_NEXT14_SITES as CYCLE847_NO_NEXT14_SITES,
    STANDING_RESULT as CYCLE847_RESULT,
    STANDING_SEQUENCES as CYCLE847_SEQUENCES,
    STANDING_SITES as CYCLE847_SITES,
    STANDING_VERDICT as CYCLE847_VERDICT,
    absent_hit_sum,
    hpq_tablets_hit,
    reframed_verdict,
    row_holds,
    row_leaks,
    score_reframed_closed_tradition,
    summarize,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next15_i_only_scoreboard import (
    HYPOTHESIS_ALL_I_ONLY as CYCLE493_HYPOTHESIS_ALL_I_ONLY,
    STANDING_I_LEFTOVER_N6_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT15_I_ONLY as CYCLE493_ALL_I_ONLY_CLAIM,
    STANDING_LEFTOVER_MATCHING_NEXT15_SITES as CYCLE493_SITES,
    STANDING_N as CYCLE493_N,
    STANDING_N_I_EACH as CYCLE493_N_I_EACH,
    STANDING_N_I_ONLY as CYCLE493_N_I_ONLY,
    STANDING_N_LEAK as CYCLE493_N_LEAK,
    STANDING_N_NO_NEXT15 as CYCLE493_N_NO_NEXT15,
    STANDING_N_SEQUENCES as CYCLE493_N_SEQUENCES,
    STANDING_N_WITH_NEXT15 as CYCLE493_N_WITH_NEXT15,
    STANDING_NO_NEXT15_SITES as CYCLE493_NO_NEXT15_SITES,
    STANDING_RESULT as CYCLE493_RESULT,
    STANDING_SEQUENCES as CYCLE493_SEQUENCES,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next16_i_only_scoreboard import (
    HYPOTHESIS_ALL_I_ONLY as CYCLE495_HYPOTHESIS_ALL_I_ONLY,
    STANDING_I_LEFTOVER_N6_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT16_I_ONLY as CYCLE495_ALL_I_ONLY_CLAIM,
    STANDING_N as CYCLE495_N,
    STANDING_N_I_ONLY as CYCLE495_N_I_ONLY,
    STANDING_N_LEAK as CYCLE495_N_LEAK,
    STANDING_N_NO_NEXT16 as CYCLE495_N_NO_NEXT16,
    STANDING_N_SEQUENCES as CYCLE495_N_SEQUENCES,
    STANDING_N_WITH_NEXT16 as CYCLE495_N_WITH_NEXT16,
    STANDING_NO_NEXT16_SITES as CYCLE495_NO_NEXT16_SITES,
    STANDING_RESULT as CYCLE495_RESULT,
    STANDING_SEQUENCES as CYCLE495_SEQUENCES,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

STANDING_N = 15
STANDING_N_PARENT = 18
STANDING_N_WITH_NEXT15 = 15
STANDING_N_NO_NEXT15 = 3
STANDING_NO_NEXT15_SITES = CYCLE493_NO_NEXT15_SITES
STANDING_PARENT_COMPLETE = False
STANDING_HITS_EACH = (0, 0, 0, 0, 0, 0, 1)
STANDING_HITS = (STANDING_HITS_EACH,) * STANDING_N
STANDING_SITES = CYCLE493_SITES
STANDING_SEQUENCES = CYCLE493_SEQUENCES
STANDING_N_HPQ_GE1 = 0
STANDING_N_HPQ_GE2 = 0
STANDING_N_EXACT0_ABC = 15
STANDING_N_I_GE1 = 15
STANDING_N_EXACT0_I = 0
STANDING_N_LEAK = 0
STANDING_N_HOLD = 0
STANDING_HOLD_INDEXES = ()
STANDING_INCOMPLETE_INDEXES = tuple(range(STANDING_N))
STANDING_I_GT1_INDEXES = ()
STANDING_NEXT14_HAPAX_STILL_HAPAX = (3,)
STANDING_NEXT14_ALL_EXTEND = True
STANDING_HITS_H = 0
STANDING_HITS_P = 0
STANDING_HITS_Q = 0
STANDING_HITS_A = 0
STANDING_HITS_B = 0
STANDING_HITS_C = 0
STANDING_HITS_I = 15
STANDING_VERDICT = "incomplete-set LOSE"
STANDING_CLAIM_HOLDS = False
STANDING_CLAIM = "leftover6_next15_reframed_closed_tradition_hpq_ge1_and_exact0_abc"
STANDING_RESULT = "i_leftover_n6_next15_closed_tradition_hpq_abc"
STANDING_AXIS = "closed-tradition-reframed"
STANDING_FROM_CYCLE = 493
STANDING_I_ONLY_ALREADY_LOCKED = True
STANDING_I_ONLY_CYCLE = 493
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
STANDING_DO_NOT_RELOCK_CYCLES_832_847 = True
STANDING_WINDOW_PEELS_CLOSED = True
STANDING_PREV1_GRAM_LIST_ABSENT = True
STANDING_DO_NOT_LAUNCH_PREV1_PEEL = True
STANDING_DO_NOT_LAUNCH_PREV10 = True
STANDING_DO_NOT_LAUNCH_LEFTOVER_10GRAMS = True
STANDING_DO_NOT_LAUNCH_NEXT13 = True
STANDING_DO_NOT_LAUNCH_NEXT14 = True
STANDING_DO_NOT_LAUNCH_NEXT15 = True
STANDING_DO_NOT_LAUNCH_NEXT16 = True
STANDING_DO_NOT_LAUNCH_PREV184 = True
STANDING_DO_NOT_LAUNCH_NEXT185 = True
STANDING_NEW_TABLET = False
STANDING_I_IN_ABSENT_SET = False
STANDING_NAMED_BY_CYCLE847 = (
    "cycle493_next15_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NEXT_CHEAP_LOCK = (
    "cycle495_next16_reframed_closed_tradition_hpq_ge1_exact0_abc"
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


class TestMamariILeftoverN6Next15ClosedTraditionHpqAbcScoreboard(unittest.TestCase):
    """Cycle 848 reframed closed-tradition lock on the cycle-493 next-15 population."""

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

    def test_population_is_the_locked_cycle_493_next15_grams(self):
        """Fifteen next-15 sequences and sites come from cycle 493. None invented."""
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N)
        self.assertEqual(len(STANDING_SITES), STANDING_N)
        self.assertEqual(STANDING_SEQUENCES, CYCLE493_SEQUENCES)
        self.assertEqual(STANDING_SITES, CYCLE493_SITES)
        self.assertEqual(CYCLE493_N, STANDING_N_PARENT)
        self.assertEqual(CYCLE493_N, 18)
        self.assertEqual(CYCLE493_N_SEQUENCES, 15)
        self.assertEqual(STANDING_N_WITH_NEXT15, CYCLE493_N_WITH_NEXT15)
        self.assertEqual(STANDING_N_NO_NEXT15, CYCLE493_N_NO_NEXT15)
        self.assertEqual(
            STANDING_NO_NEXT15_SITES,
            (("Ia", "Ia8", 167), ("Ia", "Ia8", 166), ("Ia", "Ia8", 165)),
        )
        self.assertEqual(STANDING_NO_NEXT15_SITES, CYCLE847_NO_NEXT14_SITES)
        self.assertFalse(STANDING_PARENT_COMPLETE)
        self.assertTrue(CYCLE493_HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE493_ALL_I_ONLY_CLAIM)
        self.assertEqual(CYCLE493_N_I_ONLY, 15)
        self.assertEqual(CYCLE493_N_LEAK, 0)
        self.assertEqual(STANDING_FROM_CYCLE, 493)
        self.assertEqual(len(self.rows), 15)
        for row, tokens, site in zip(self.rows, STANDING_SEQUENCES, STANDING_SITES, strict=True):
            self.assertEqual(row.tokens, tokens)
            self.assertEqual(row.site, site)
            self.assertEqual(len(row.tokens), 15)
        prior = self.survey[CYCLE493_RESULT]
        all_i_only_key = (
            "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
            "remaining_after_076_020_remaining_after_076_010_next_15grams_all_i_only"
        )
        self.assertEqual(CYCLE493_RESULT, (
            "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
            "remaining_after_076_020_remaining_after_076_010_next15_i_only"
        ))
        self.assertEqual(prior["cycle"], 493)
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_sequences"], 15)
        self.assertEqual(prior["N_6grams"], 18)
        self.assertTrue(prior["hypothesis_all_i_only"])
        self.assertFalse(prior[all_i_only_key])
        self.assertFalse(prior[CYCLE493_RESULT])
        self.assertEqual(prior["N_i_only"], 15)
        self.assertEqual(prior["N_leak"], 0)
        self.assertEqual(prior["N_no_next15"], 3)
        self.assertEqual(prior["N_with_next15"], 15)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE847, self.survey)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_prior_locks_stay_locked(self):
        """Do not re-lock cycle 493 I-only or the cycle 832–847 boards."""
        parent = self.survey[CYCLE457_RESULT]
        self.assertEqual(parent["cycle"], STANDING_PARENT_I_LOCAL_CYCLE)
        self.assertTrue(parent["hypothesis_all_i_only"])
        self.assertEqual(parent["N"], 18)
        self.assertEqual(parent["N_leak"], 0)
        self.assertTrue(STANDING_DO_NOT_RELOCK_PARENT_I_LOCAL)
        self.assertTrue(STANDING_I_ONLY_ALREADY_LOCKED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_I_ONLY)
        self.assertEqual(STANDING_I_ONLY_CYCLE, 493)
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
        next14 = self.survey[CYCLE847_RESULT]
        self.assertEqual(next14["cycle"], STANDING_NEXT14_REFRAMED_CYCLE)
        self.assertEqual(next14["verdict"], CYCLE847_VERDICT)
        self.assertEqual(next14["verdict"], "incomplete-set LOSE")
        self.assertEqual(next14["N_hold"], CYCLE847_N_HOLD)
        self.assertEqual(next14["N_hold"], 0)
        self.assertEqual(next14["N_leak"], CYCLE847_N_LEAK)
        self.assertEqual(next14["N_leak"], 0)
        self.assertEqual(next14["hits_I"], CYCLE847_HITS_I)
        self.assertEqual(next14["hits_I"], 15)
        self.assertEqual(next14["N_hpq_ge1"], 0)
        self.assertEqual(next14["N_exact0_abc"], 15)
        self.assertEqual(next14["N_with_next14"], 15)
        self.assertEqual(next14["N_no_next14"], 3)
        self.assertEqual(next14["next_cheap_lock"], STANDING_NAMED_BY_CYCLE847)
        self.assertEqual(next14["next_cheap_lock"], CYCLE847_NEXT_CHEAP_LOCK)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE847, self.survey)
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
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLES_832_847)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_measured_table_is_incomplete_set_lose(self):
        """H/P/Q and A/B/C are exact-0. hits_I is 15 and is not a leak."""
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
        self.assertEqual(self.summary["hits_I"], 15)
        self.assertEqual(tuple(row.hits[-1] for row in self.rows), CYCLE493_N_I_EACH)
        self.assertEqual(CYCLE493_N_I_EACH, (1,) * STANDING_N)
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
        self.assertTrue(STANDING_NEXT14_ALL_EXTEND)
        for n14, n15, site14, site15 in zip(
            CYCLE847_SEQUENCES, STANDING_SEQUENCES, CYCLE847_SITES, STANDING_SITES, strict=True
        ):
            self.assertEqual(n15[:14], n14)
            self.assertEqual(site15, site14)
        still = self.rows[STANDING_NEXT14_HAPAX_STILL_HAPAX[0]]
        self.assertEqual(
            still.tokens,
            (
                "604", "076", "071", "600", "999", "050", "076", "000",
                "002", "999", "076", "092", "535", "999", "208",
            ),
        )
        self.assertEqual(still.site, ("Ia", "Ia9", 9))
        self.assertEqual(still.as_map()["I"], 1)
        self.assertEqual(still.tokens[:14], CYCLE847_SEQUENCES[3])
        self.assertEqual(CYCLE847_SITES[3], ("Ia", "Ia9", 9))
        dropped_tokens = CYCLE840_SEQUENCES[CYCLE841_NEXT7_DROPPED_INDEX]
        dropped_site = CYCLE840_SITES[CYCLE841_NEXT7_DROPPED_INDEX]
        self.assertEqual(
            dropped_tokens,
            ("720", "076", "070", "701", "214", "076", "298"),
        )
        self.assertEqual(dropped_site, ("Ia", "Ia8", 171))
        self.assertFalse(any(tokens[:7] == dropped_tokens for tokens in STANDING_SEQUENCES))
        self.assertIn(("Ia", "Ia8", 165), STANDING_NO_NEXT15_SITES)
        self.assertEqual(STANDING_HOLD_INDEXES, ())
        self.assertEqual(STANDING_I_GT1_INDEXES, ())
        self.assertEqual(len(STANDING_INCOMPLETE_INDEXES), STANDING_N)
        self.assertEqual(self.verdict, STANDING_VERDICT)
        self.assertEqual(self.verdict, "incomplete-set LOSE")
        self.assertFalse(STANDING_CLAIM_HOLDS)
        self.assertFalse(STANDING_PARENT_COMPLETE)
        self.assertEqual(STANDING_N_NO_NEXT15, 3)
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
        self.assertTrue(STANDING_PREV1_GRAM_LIST_ABSENT)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_PREV1_PEEL)
        self.assertFalse(PREV1_N6_SCOREBOARD.exists())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_next_cheap_lock_is_the_locked_cycle_495_next16_list(self):
        """Cycle 495 next-16 I-only stays locked. Cycle 849 holds the reframed score."""
        self.assertEqual(CYCLE495_N, 18)
        self.assertEqual(CYCLE495_N_SEQUENCES, 15)
        self.assertEqual(len(CYCLE495_SEQUENCES), 15)
        self.assertTrue(all(len(tokens) == 16 for tokens in CYCLE495_SEQUENCES))
        self.assertTrue(CYCLE495_HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE495_ALL_I_ONLY_CLAIM)
        self.assertEqual(CYCLE495_N_I_ONLY, 15)
        self.assertEqual(CYCLE495_N_LEAK, 0)
        self.assertEqual(CYCLE495_N_WITH_NEXT16, 15)
        self.assertEqual(CYCLE495_N_NO_NEXT16, 3)
        self.assertEqual(
            CYCLE495_NO_NEXT16_SITES,
            (("Ia", "Ia8", 167), ("Ia", "Ia8", 166), ("Ia", "Ia8", 165)),
        )
        prior = self.survey[CYCLE495_RESULT]
        all_i_only_key = (
            "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
            "remaining_after_076_020_remaining_after_076_010_next_16grams_all_i_only"
        )
        self.assertEqual(prior["cycle"], 495)
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_sequences"], 15)
        self.assertEqual(prior["N_6grams"], 18)
        self.assertTrue(prior["hypothesis_all_i_only"])
        self.assertFalse(prior[all_i_only_key])
        self.assertFalse(prior[CYCLE495_RESULT])
        self.assertEqual(prior["N_i_only"], 15)
        self.assertEqual(prior["N_leak"], 0)
        self.assertEqual(prior["N_no_next16"], 3)
        self.assertEqual(prior["N_with_next16"], 15)
        self.assertNotIn(STANDING_NEXT_CHEAP_LOCK, self.survey)
        successor = self.survey["i_leftover_n6_next16_closed_tradition_hpq_abc"]
        self.assertEqual(successor["cycle"], 849)
        self.assertEqual(successor["verdict"], "incomplete-set LOSE")
        self.assertEqual(successor["N_hold"], 0)
        self.assertEqual(successor["N_leak"], 0)
        self.assertEqual(
            STANDING_NEXT_CHEAP_LOCK,
            "cycle495_next16_reframed_closed_tradition_hpq_ge1_exact0_abc",
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-848 incomplete-set LOSE table."""
        lock = self.survey[STANDING_RESULT]
        self.assertEqual(lock["cycle"], 848)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["axis"], STANDING_AXIS)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertEqual(lock["verdict"], STANDING_VERDICT)
        self.assertEqual(lock["verdict"], self.verdict)
        self.assertFalse(lock["claim_holds"])
        self.assertEqual(lock["claim_holds"], STANDING_CLAIM_HOLDS)
        self.assertEqual(lock["N"], self.summary["N"])
        self.assertEqual(lock["N_parent"], STANDING_N_PARENT)
        self.assertEqual(lock["N_with_next15"], STANDING_N_WITH_NEXT15)
        self.assertEqual(lock["N_no_next15"], STANDING_N_NO_NEXT15)
        self.assertFalse(lock["parent_complete"])
        self.assertEqual(
            tuple(tuple(site) for site in lock["no_next15_sites"]),
            STANDING_NO_NEXT15_SITES,
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
        self.assertTrue(lock["do_not_relock_cycles_832_847"])
        self.assertTrue(lock["window_peels_closed"])
        self.assertTrue(lock["prev1_gram_list_absent"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev1"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev10"])
        self.assertTrue(lock["do_not_launch_leftover_10grams"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next13"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next14"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next15"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next16"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev184"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next185"])
        self.assertEqual(lock["named_by_cycle847"], STANDING_NAMED_BY_CYCLE847)
        self.assertEqual(lock["next_cheap_lock"], STANDING_NEXT_CHEAP_LOCK)
        self.assertEqual(tuple(lock["hold_indexes"]), STANDING_HOLD_INDEXES)
        self.assertEqual(tuple(lock["incomplete_indexes"]), STANDING_INCOMPLETE_INDEXES)
        self.assertEqual(tuple(lock["i_gt1_indexes"]), STANDING_I_GT1_INDEXES)
        self.assertEqual(
            tuple(lock["next14_hapax_still_hapax"]),
            STANDING_NEXT14_HAPAX_STILL_HAPAX,
        )
        self.assertTrue(lock["next14_all_extend"])
        self.assertEqual(lock["next14_all_extend"], STANDING_NEXT14_ALL_EXTEND)
        self.assertNotIn("leak_index", lock)
        self.assertNotIn(STANDING_NAMED_BY_CYCLE847, self.survey)
        self.assertNotIn(STANDING_NEXT_CHEAP_LOCK, self.survey)
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["from_cycle"], STANDING_FROM_CYCLE)
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(len(lock["rows"]), 15)
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
