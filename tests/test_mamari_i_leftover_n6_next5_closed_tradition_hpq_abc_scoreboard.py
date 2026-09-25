"""Reframed closed-tradition hold-out of the locked leftover-6 next-5 grams.

Cycle 838 text-search lock. Uses already-vendored A–V and the
cycle-473 leftover n=6 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 remaining-
after-076-010 next 5-grams (N=18). HEAD-check: that gram list
exists and is not yet locked under this reframed rule. Cycle
473 already locked the I-only claim on these 5-grams as HOLD
(N_i_only=18, N_leak=0, N_no_next5=0). Cycle 837 already
locked the reframed claim on the cycle-470 next-4 grams as
incomplete-set LOSE. This cycle does not re-lock either claim,
and does not re-lock Cycles 832–836.

Claim that can lose: each of the 18 locked next-5 grams is an
exact contiguous hit on ≥1 of H/P/Q and exact-0 on A/B/C.
hits_I is recorded and is not a leak. HOLD needs that claim
true for the whole population (N_hold=18, N_leak=0). Leak onto
A/B/C is leak LOSE. An empty H/P/Q hit set with zero A/B/C hits
is incomplete-set LOSE.

Measured: N=18, N_hpq_ge1=0, N_hpq_ge2=0, N_exact0_abc=18,
N_i_ge1=18, N_exact0_i=0, N_leak=0, N_hold=0, hits_I=18.
Every gram is exact-0 on H/P/Q and on A/B/C and an exact
contiguous hit once on I. The next-4 hapax grams stay hapax
once extended: 604 076 071 600 999 at Ia9[9] hits I once;
720 076 070 701 214 at Ia8[171] hits I once. Verdict:
incomplete-set LOSE.

Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Does not reopen leftover-6
next/prev window peels (next-side exhausted at cycle 831;
prev-side eighteen-hole 0/18 since cycle 800). Leftover-6
prev-1 has no locked gram list; do not invent that peel.
Do not launch leftover-6 prev-184 or leftover-6 next-185.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Search lock, not a merge and not a translation. MockProvider only.
"""

from pathlib import Path
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    load_vendored_a_through_v,
)
from tests.test_mamari_i_leftover_n6_closed_tradition_hpq_abc_scoreboard import (
    ABSENT_TABLETS,
    CYCLE832_RESULT,
    HPQ_TABLETS,
    MIN_HPQ_TABLETS,
    PROBE_TABLETS,
    STANDING_RESULT as CYCLE833_RESULT,
    absent_hit_sum,
    hpq_tablets_hit,
    reframed_verdict,
    row_holds,
    row_leaks,
    score_reframed_closed_tradition,
    summarize,
)
from tests.test_mamari_i_leftover_n6_next1_closed_tradition_hpq_abc_scoreboard import (
    STANDING_RESULT as CYCLE834_RESULT,
    STANDING_VERDICT as CYCLE834_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next2_closed_tradition_hpq_abc_scoreboard import (
    STANDING_RESULT as CYCLE835_RESULT,
    STANDING_VERDICT as CYCLE835_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next3_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE836_HITS_I,
    STANDING_N_HOLD as CYCLE836_N_HOLD,
    STANDING_N_LEAK as CYCLE836_N_LEAK,
    STANDING_RESULT as CYCLE836_RESULT,
    STANDING_VERDICT as CYCLE836_VERDICT,
)
from tests.test_mamari_i_leftover_n6_next4_closed_tradition_hpq_abc_scoreboard import (
    STANDING_HITS_I as CYCLE837_HITS_I,
    STANDING_N_HOLD as CYCLE837_N_HOLD,
    STANDING_N_LEAK as CYCLE837_N_LEAK,
    STANDING_NEXT_CHEAP_LOCK as CYCLE837_NEXT_CHEAP_LOCK,
    STANDING_RESULT as CYCLE837_RESULT,
    STANDING_VERDICT as CYCLE837_VERDICT,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_6grams_i_only_scoreboard import (
    STANDING_RESULT as CYCLE457_RESULT,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next5_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N6_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT_5GRAMS_ALL_I_ONLY as CYCLE473_I_ONLY,
    STANDING_LEFTOVER_MATCHING_NEXT5_SITES as CYCLE473_SITES,
    STANDING_N as CYCLE473_N,
    STANDING_N_I_EACH as CYCLE473_N_I_EACH,
    STANDING_N_I_ONLY as CYCLE473_N_I_ONLY,
    STANDING_N_LEAK as CYCLE473_N_LEAK,
    STANDING_N_NO_NEXT5 as CYCLE473_N_NO_NEXT5,
    STANDING_RESULT as CYCLE473_RESULT,
    STANDING_SEQUENCES as CYCLE473_SEQUENCES,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next6_i_only_scoreboard import (
    HYPOTHESIS_ALL_I_ONLY as CYCLE475_HYPOTHESIS_ALL_I_ONLY,
    STANDING_I_LEFTOVER_N6_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT_6GRAMS_ALL_I_ONLY as CYCLE475_ALL_I_ONLY_CLAIM,
    STANDING_N as CYCLE475_N,
    STANDING_N_I_ONLY as CYCLE475_N_I_ONLY,
    STANDING_N_LEAK as CYCLE475_N_LEAK,
    STANDING_N_NO_NEXT6 as CYCLE475_N_NO_NEXT6,
    STANDING_N_SEQUENCES as CYCLE475_N_SEQUENCES,
    STANDING_N_WITH_NEXT6 as CYCLE475_N_WITH_NEXT6,
    STANDING_NO_NEXT6_SITES as CYCLE475_NO_NEXT6_SITES,
    STANDING_RESULT as CYCLE475_RESULT,
    STANDING_SEQUENCES as CYCLE475_SEQUENCES,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

CYCLE831_SURVEY_KEY = (
    "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
    "remaining_after_076_020_remaining_after_076_010_next184_i_only"
)
PREV1_N6_SCOREBOARD = Path(
    "tests/test_mamari_i_leftover_n6_remaining_after_090_076_"
    "remaining_after_430_076_remaining_after_076_020_"
    "remaining_after_076_010_prev1_i_only_scoreboard.py"
)

STANDING_N = 18
STANDING_HITS_EACH = (0, 0, 0, 0, 0, 0, 1)
STANDING_HITS = (STANDING_HITS_EACH,) * STANDING_N
STANDING_SITES = CYCLE473_SITES
STANDING_SEQUENCES = CYCLE473_SEQUENCES
STANDING_N_HPQ_GE1 = 0
STANDING_N_HPQ_GE2 = 0
STANDING_N_EXACT0_ABC = 18
STANDING_N_I_GE1 = 18
STANDING_N_EXACT0_I = 0
STANDING_N_LEAK = 0
STANDING_N_HOLD = 0
STANDING_HOLD_INDEXES = ()
STANDING_INCOMPLETE_INDEXES = tuple(range(STANDING_N))
STANDING_I_GT1_INDEXES = ()
STANDING_NEXT4_HAPAX_STILL_HAPAX = (3, 14)
STANDING_HITS_H = 0
STANDING_HITS_P = 0
STANDING_HITS_Q = 0
STANDING_HITS_A = 0
STANDING_HITS_B = 0
STANDING_HITS_C = 0
STANDING_HITS_I = 18
STANDING_VERDICT = "incomplete-set LOSE"
STANDING_CLAIM_HOLDS = False
STANDING_CLAIM = "leftover6_next5_reframed_closed_tradition_hpq_ge1_and_exact0_abc"
STANDING_RESULT = "i_leftover_n6_next5_closed_tradition_hpq_abc"
STANDING_AXIS = "closed-tradition-reframed"
STANDING_FROM_CYCLE = 473
STANDING_I_ONLY_ALREADY_LOCKED = True
STANDING_I_ONLY_CYCLE = 473
STANDING_PARENT_I_LOCAL_CYCLE = 457
STANDING_NEXT1_REFRAMED_CYCLE = 834
STANDING_NEXT2_REFRAMED_CYCLE = 835
STANDING_NEXT3_REFRAMED_CYCLE = 836
STANDING_NEXT4_REFRAMED_CYCLE = 837
STANDING_DO_NOT_RELOCK_I_ONLY = True
STANDING_DO_NOT_RELOCK_PARENT_I_LOCAL = True
STANDING_DO_NOT_RELOCK_NEXT1_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT2_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT3_REFRAMED = True
STANDING_DO_NOT_RELOCK_NEXT4_REFRAMED = True
STANDING_DO_NOT_RELOCK_CYCLES_832_837 = True
STANDING_WINDOW_PEELS_CLOSED = True
STANDING_PREV1_GRAM_LIST_ABSENT = True
STANDING_DO_NOT_LAUNCH_PREV1_PEEL = True
STANDING_DO_NOT_LAUNCH_PREV184 = True
STANDING_DO_NOT_LAUNCH_NEXT185 = True
STANDING_NEW_TABLET = False
STANDING_I_IN_ABSENT_SET = False
STANDING_NAMED_BY_CYCLE837 = (
    "cycle473_next5_reframed_closed_tradition_hpq_ge1_exact0_abc"
)
STANDING_NEXT_CHEAP_LOCK = (
    "cycle475_next6_reframed_closed_tradition_hpq_ge1_exact0_abc"
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


class TestMamariILeftoverN6Next5ClosedTraditionHpqAbcScoreboard(unittest.TestCase):
    """Cycle 838 reframed closed-tradition lock on the cycle-473 next-5 population."""

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

    def test_population_is_the_locked_cycle_473_next5_grams(self):
        """Eighteen next-5 sequences and sites come from cycle 473. None invented."""
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N)
        self.assertEqual(len(STANDING_SITES), STANDING_N)
        self.assertEqual(STANDING_SEQUENCES, CYCLE473_SEQUENCES)
        self.assertEqual(STANDING_SITES, CYCLE473_SITES)
        self.assertEqual(CYCLE473_N, 18)
        self.assertTrue(CYCLE473_I_ONLY)
        self.assertEqual(CYCLE473_N_I_ONLY, 18)
        self.assertEqual(CYCLE473_N_LEAK, 0)
        self.assertEqual(CYCLE473_N_NO_NEXT5, 0)
        self.assertEqual(STANDING_FROM_CYCLE, 473)
        self.assertEqual(len(self.rows), 18)
        for row, tokens, site in zip(self.rows, STANDING_SEQUENCES, STANDING_SITES, strict=True):
            self.assertEqual(row.tokens, tokens)
            self.assertEqual(row.site, site)
            self.assertEqual(len(row.tokens), 5)
        prior = self.survey[CYCLE473_RESULT]
        self.assertEqual(prior["cycle"], 473)
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_5grams"], 18)
        self.assertTrue(prior["hypothesis_all_i_only"])
        self.assertTrue(prior[CYCLE473_RESULT])
        self.assertEqual(prior["N_i_only"], 18)
        self.assertEqual(prior["N_leak"], 0)
        self.assertEqual(prior["N_no_next5"], 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_prior_locks_stay_locked(self):
        """Do not re-lock cycle 473 I-only or the cycle 832–837 boards."""
        parent = self.survey[CYCLE457_RESULT]
        self.assertEqual(parent["cycle"], STANDING_PARENT_I_LOCAL_CYCLE)
        self.assertTrue(parent["hypothesis_all_i_only"])
        self.assertEqual(parent["N"], 18)
        self.assertEqual(parent["N_leak"], 0)
        self.assertTrue(STANDING_DO_NOT_RELOCK_PARENT_I_LOCAL)
        self.assertTrue(STANDING_I_ONLY_ALREADY_LOCKED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_I_ONLY)
        self.assertEqual(STANDING_I_ONLY_CYCLE, 473)
        self.assertFalse(STANDING_I_IN_ABSENT_SET)
        self.assertEqual(ABSENT_TABLETS, ("A", "B", "C"))
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
        self.assertEqual(next4["next_cheap_lock"], STANDING_NAMED_BY_CYCLE837)
        self.assertEqual(next4["next_cheap_lock"], CYCLE837_NEXT_CHEAP_LOCK)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT1_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT2_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT3_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_NEXT4_REFRAMED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLES_832_837)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_measured_table_is_incomplete_set_lose(self):
        """H/P/Q and A/B/C are exact-0. hits_I is 18 and is not a leak."""
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
        self.assertEqual(self.summary["hits_I"], 18)
        self.assertEqual(tuple(row.hits[-1] for row in self.rows), CYCLE473_N_I_EACH)
        self.assertEqual(CYCLE473_N_I_EACH, (1,) * STANDING_N)
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
        once_a = self.rows[STANDING_NEXT4_HAPAX_STILL_HAPAX[0]]
        self.assertEqual(once_a.tokens, ("604", "076", "071", "600", "999"))
        self.assertEqual(once_a.site, ("Ia", "Ia9", 9))
        self.assertEqual(once_a.as_map()["I"], 1)
        once_b = self.rows[STANDING_NEXT4_HAPAX_STILL_HAPAX[1]]
        self.assertEqual(once_b.tokens, ("720", "076", "070", "701", "214"))
        self.assertEqual(once_b.site, ("Ia", "Ia8", 171))
        self.assertEqual(once_b.as_map()["I"], 1)
        self.assertEqual(STANDING_HOLD_INDEXES, ())
        self.assertEqual(STANDING_I_GT1_INDEXES, ())
        self.assertEqual(len(STANDING_INCOMPLETE_INDEXES), STANDING_N)
        self.assertEqual(self.verdict, STANDING_VERDICT)
        self.assertEqual(self.verdict, "incomplete-set LOSE")
        self.assertFalse(STANDING_CLAIM_HOLDS)
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
        self.assertTrue(STANDING_PREV1_GRAM_LIST_ABSENT)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_PREV1_PEEL)
        self.assertFalse(PREV1_N6_SCOREBOARD.exists())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_next_cheap_lock_is_the_locked_cycle_475_next6_list(self):
        """Cycle 475 next-6 grams are already locked and not yet reframed."""
        self.assertEqual(CYCLE475_N, 18)
        self.assertEqual(CYCLE475_N_SEQUENCES, 17)
        self.assertEqual(len(CYCLE475_SEQUENCES), 17)
        self.assertTrue(all(len(tokens) == 6 for tokens in CYCLE475_SEQUENCES))
        self.assertTrue(CYCLE475_HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE475_ALL_I_ONLY_CLAIM)
        self.assertEqual(CYCLE475_N_I_ONLY, 17)
        self.assertEqual(CYCLE475_N_LEAK, 0)
        self.assertEqual(CYCLE475_N_WITH_NEXT6, 17)
        self.assertEqual(CYCLE475_N_NO_NEXT6, 1)
        self.assertEqual(CYCLE475_NO_NEXT6_SITES, (("Ia", "Ia8", 167),))
        prior = self.survey[CYCLE475_RESULT]
        all_i_only_key = (
            "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
            "remaining_after_076_020_remaining_after_076_010_next_6grams_all_i_only"
        )
        self.assertEqual(prior["cycle"], 475)
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_sequences"], 17)
        self.assertEqual(prior["N_6grams"], 18)
        self.assertTrue(prior["hypothesis_all_i_only"])
        self.assertFalse(prior[all_i_only_key])
        self.assertFalse(prior[CYCLE475_RESULT])
        self.assertEqual(prior["N_i_only"], 17)
        self.assertEqual(prior["N_leak"], 0)
        self.assertEqual(prior["N_no_next6"], 1)
        self.assertEqual(prior["N_with_next6"], 17)
        self.assertNotIn(
            "i_leftover_n6_next6_closed_tradition_hpq_abc",
            self.survey,
        )
        self.assertEqual(
            STANDING_NEXT_CHEAP_LOCK,
            "cycle475_next6_reframed_closed_tradition_hpq_ge1_exact0_abc",
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-838 incomplete-set LOSE table."""
        lock = self.survey[STANDING_RESULT]
        self.assertEqual(lock["cycle"], 838)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["axis"], STANDING_AXIS)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertEqual(lock["verdict"], STANDING_VERDICT)
        self.assertEqual(lock["verdict"], self.verdict)
        self.assertFalse(lock["claim_holds"])
        self.assertEqual(lock["claim_holds"], STANDING_CLAIM_HOLDS)
        self.assertEqual(lock["N"], self.summary["N"])
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
        self.assertTrue(lock["do_not_relock_cycles_832_837"])
        self.assertTrue(lock["window_peels_closed"])
        self.assertTrue(lock["prev1_gram_list_absent"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev1"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev184"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next185"])
        self.assertEqual(lock["named_by_cycle837"], STANDING_NAMED_BY_CYCLE837)
        self.assertEqual(lock["next_cheap_lock"], STANDING_NEXT_CHEAP_LOCK)
        self.assertEqual(tuple(lock["hold_indexes"]), STANDING_HOLD_INDEXES)
        self.assertEqual(tuple(lock["incomplete_indexes"]), STANDING_INCOMPLETE_INDEXES)
        self.assertEqual(tuple(lock["i_gt1_indexes"]), STANDING_I_GT1_INDEXES)
        self.assertEqual(
            tuple(lock["next4_hapax_still_hapax"]),
            STANDING_NEXT4_HAPAX_STILL_HAPAX,
        )
        self.assertNotIn("leak_index", lock)
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["from_cycle"], STANDING_FROM_CYCLE)
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(len(lock["rows"]), 18)
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
