"""Reframed closed-tradition hold-out of the locked leftover-6 next-1 grams.

Cycle 834 text-search lock. Uses already-vendored A–V and the
cycle-458 leftover n=6 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 remaining-
after-076-010 next 1-grams (N=18). HEAD-check: that gram list
exists and is not yet locked under this reframed rule. The
cycle-457 I-local claim is the parent 6-grams, not these
1-grams, and stays locked. Cycle 458 already locked the I-only
claim on these 1-grams as LOSE (N_i_only=2, N_leak=16 off I).
This cycle does not re-lock either claim.

Claim that can lose: each of the 18 locked next-1 grams is an
exact contiguous hit on ≥1 of H/P/Q and exact-0 on A/B/C.
hits_I is recorded and is not a leak. HOLD needs that claim
true for the whole population (N_hold=18, N_leak=0). Leak onto
A/B/C is leak LOSE. An empty H/P/Q hit set with zero A/B/C hits
is incomplete-set LOSE.

Measured: N=18, N_hpq_ge1=15, N_hpq_ge2=14, N_exact0_abc=3,
N_i_ge1=18, N_exact0_i=0, N_leak=15, N_hold=1, hits_I=1591.
One gram holds (604 at Ia9[9]: H=2, P=1, A=B=C=0). Two grams
are exact-0 on A/B/C and on H/P/Q (999, 177). Fifteen grams
hit A, B, or C. Verdict: leak LOSE.

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
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_6grams_i_only_scoreboard import (
    STANDING_RESULT as CYCLE457_RESULT,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next1_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N6_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_NEXT1_I_ONLY as CYCLE458_I_ONLY,
    STANDING_LEFTOVER_MATCHING_NEXT1_SITES as CYCLE458_SITES,
    STANDING_N as CYCLE458_N,
    STANDING_N_I_ONLY as CYCLE458_N_I_ONLY,
    STANDING_N_LEAK as CYCLE458_N_LEAK,
    STANDING_RESULT as CYCLE458_RESULT,
    STANDING_SEQUENCES as CYCLE458_SEQUENCES,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next2_i_only_scoreboard import (
    STANDING_N as CYCLE463_N,
    STANDING_N_I_ONLY as CYCLE463_N_I_ONLY,
    STANDING_N_LEAK as CYCLE463_N_LEAK,
    STANDING_RESULT as CYCLE463_RESULT,
    STANDING_SEQUENCES as CYCLE463_SEQUENCES,
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
STANDING_HITS = (
    (0, 0, 0, 1, 0, 0, 2),
    (28, 23, 10, 17, 15, 7, 14),
    (0, 2, 0, 1, 0, 2, 4),
    (2, 1, 0, 0, 0, 0, 16),
    (34, 22, 10, 19, 20, 17, 62),
    (6, 6, 30, 11, 9, 19, 38),
    (16, 16, 7, 14, 4, 8, 16),
    (16, 16, 7, 14, 4, 8, 16),
    (43, 34, 15, 45, 38, 19, 15),
    (0, 0, 0, 0, 0, 0, 97),
    (34, 22, 10, 19, 20, 17, 62),
    (19, 15, 10, 20, 7, 1, 18),
    (12, 13, 5, 15, 2, 17, 32),
    (8, 6, 7, 3, 8, 0, 564),
    (2, 0, 1, 1, 0, 0, 8),
    (8, 6, 7, 3, 8, 0, 564),
    (34, 22, 10, 19, 20, 17, 62),
    (0, 0, 0, 0, 0, 0, 1),
)
STANDING_SITES = CYCLE458_SITES
STANDING_SEQUENCES = CYCLE458_SEQUENCES
STANDING_N_HPQ_GE1 = 15
STANDING_N_HPQ_GE2 = 14
STANDING_N_EXACT0_ABC = 3
STANDING_N_I_GE1 = 18
STANDING_N_EXACT0_I = 0
STANDING_N_LEAK = 15
STANDING_N_HOLD = 1
STANDING_HOLD_INDEX = 3
STANDING_INCOMPLETE_INDEXES = (9, 17)
STANDING_HITS_H = 262
STANDING_HITS_P = 204
STANDING_HITS_Q = 129
STANDING_HITS_A = 202
STANDING_HITS_B = 155
STANDING_HITS_C = 132
STANDING_HITS_I = 1591
STANDING_VERDICT = "leak LOSE"
STANDING_CLAIM_HOLDS = False
STANDING_CLAIM = "leftover6_next1_reframed_closed_tradition_hpq_ge1_and_exact0_abc"
STANDING_RESULT = "i_leftover_n6_next1_closed_tradition_hpq_abc"
STANDING_AXIS = "closed-tradition-reframed"
STANDING_FROM_CYCLE = 458
STANDING_I_ONLY_ALREADY_LOCKED = True
STANDING_I_ONLY_CYCLE = 458
STANDING_PARENT_I_LOCAL_CYCLE = 457
STANDING_DO_NOT_RELOCK_I_ONLY = True
STANDING_DO_NOT_RELOCK_PARENT_I_LOCAL = True
STANDING_WINDOW_PEELS_CLOSED = True
STANDING_PREV1_GRAM_LIST_ABSENT = True
STANDING_DO_NOT_LAUNCH_PREV1_PEEL = True
STANDING_DO_NOT_LAUNCH_PREV184 = True
STANDING_DO_NOT_LAUNCH_NEXT185 = True
STANDING_NEW_TABLET = False
STANDING_I_IN_ABSENT_SET = False
STANDING_NEXT_CHEAP_LOCK = (
    "cycle463_next2_reframed_closed_tradition_hpq_ge1_exact0_abc"
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


class TestMamariILeftoverN6Next1ClosedTraditionHpqAbcScoreboard(unittest.TestCase):
    """Cycle 834 reframed closed-tradition lock on the cycle-458 next-1 population."""

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

    def test_population_is_the_locked_cycle_458_next1_grams(self):
        """Eighteen next-1 sequences and sites come from cycle 458. None invented."""
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N)
        self.assertEqual(len(STANDING_SITES), STANDING_N)
        self.assertEqual(STANDING_SEQUENCES, CYCLE458_SEQUENCES)
        self.assertEqual(STANDING_SITES, CYCLE458_SITES)
        self.assertEqual(CYCLE458_N, 18)
        self.assertFalse(CYCLE458_I_ONLY)
        self.assertEqual(CYCLE458_N_I_ONLY, 2)
        self.assertEqual(CYCLE458_N_LEAK, 16)
        self.assertEqual(STANDING_FROM_CYCLE, 458)
        self.assertEqual(len(self.rows), 18)
        for row, tokens, site in zip(self.rows, STANDING_SEQUENCES, STANDING_SITES, strict=True):
            self.assertEqual(row.tokens, tokens)
            self.assertEqual(row.site, site)
            self.assertEqual(len(row.tokens), 1)
        prior = self.survey[CYCLE458_RESULT]
        self.assertEqual(prior["cycle"], 458)
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_1grams"], 18)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_parent_i_local_and_cycle_458_i_only_stay_locked(self):
        """Do not re-lock cycle 457 I-local or the cycle 458 I-only LOSE."""
        parent = self.survey[CYCLE457_RESULT]
        self.assertEqual(parent["cycle"], STANDING_PARENT_I_LOCAL_CYCLE)
        self.assertTrue(parent["hypothesis_all_i_only"])
        self.assertEqual(parent["N"], 18)
        self.assertEqual(parent["N_leak"], 0)
        self.assertTrue(STANDING_DO_NOT_RELOCK_PARENT_I_LOCAL)
        self.assertTrue(STANDING_I_ONLY_ALREADY_LOCKED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_I_ONLY)
        self.assertEqual(STANDING_I_ONLY_CYCLE, 458)
        self.assertFalse(STANDING_I_IN_ABSENT_SET)
        self.assertEqual(ABSENT_TABLETS, ("A", "B", "C"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_measured_table_is_leak_lose(self):
        """Fifteen grams hit A/B/C. One holds. Two are I-source only."""
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
        self.assertEqual(self.summary["N_leak"], 15)
        self.assertEqual(self.summary["N_hold"], 1)
        self.assertEqual(self.summary["N_hpq_ge1"], 15)
        for index, row in enumerate(self.rows):
            self.assertEqual(row.hits, STANDING_HITS[index])
            hits = row.as_map()
            self.assertGreaterEqual(hits["I"], 1)
        hold = self.rows[STANDING_HOLD_INDEX]
        self.assertEqual(hold.tokens, ("604",))
        self.assertEqual(hold.site, ("Ia", "Ia9", 9))
        self.assertTrue(row_holds(hold.as_map()))
        self.assertFalse(row_leaks(hold.as_map()))
        self.assertEqual(hpq_tablets_hit(hold.as_map()), 2)
        self.assertEqual(absent_hit_sum(hold.as_map()), 0)
        for index in STANDING_INCOMPLETE_INDEXES:
            hits = self.rows[index].as_map()
            self.assertEqual(hpq_tablets_hit(hits), 0)
            self.assertEqual(absent_hit_sum(hits), 0)
            self.assertFalse(row_holds(hits))
            self.assertFalse(row_leaks(hits))
        self.assertEqual(self.verdict, STANDING_VERDICT)
        self.assertEqual(self.verdict, "leak LOSE")
        self.assertFalse(STANDING_CLAIM_HOLDS)
        self.assertEqual(STANDING_AXIS, "closed-tradition-reframed")
        self.assertEqual(MIN_HPQ_TABLETS, 1)
        self.assertEqual(PROBE_TABLETS, HPQ_TABLETS + ABSENT_TABLETS + ("I",))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_cycle_833_stays_on_the_parent_6grams(self):
        """Cycle 833's incomplete-set LOSE is the 6-grams, not these next-1 grams."""
        prior = self.survey[CYCLE833_RESULT]
        self.assertEqual(prior["cycle"], 833)
        self.assertEqual(prior["verdict"], "incomplete-set LOSE")
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_hpq_ge1"], 0)
        self.assertEqual(prior["N_leak"], 0)
        self.assertEqual(prior["hits_I"], 18)
        self.assertEqual(prior["from_cycle"], 457)
        self.assertNotEqual(prior["claim"], STANDING_CLAIM)
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

    def test_next_cheap_lock_is_the_locked_cycle_463_next2_list(self):
        """Cycle 463 next-2 grams are already locked and not yet reframed."""
        self.assertEqual(CYCLE463_N, 18)
        self.assertEqual(len(CYCLE463_SEQUENCES), 18)
        self.assertTrue(all(len(tokens) == 2 for tokens in CYCLE463_SEQUENCES))
        self.assertEqual(CYCLE463_N_I_ONLY, 12)
        self.assertEqual(CYCLE463_N_LEAK, 6)
        prior = self.survey[CYCLE463_RESULT]
        self.assertEqual(prior["cycle"], 463)
        self.assertEqual(prior["N"], 18)
        self.assertNotIn(STANDING_NEXT_CHEAP_LOCK, self.survey)
        self.assertEqual(STANDING_NEXT_CHEAP_LOCK,
            "cycle463_next2_reframed_closed_tradition_hpq_ge1_exact0_abc")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-834 leak LOSE table."""
        lock = self.survey[STANDING_RESULT]
        self.assertEqual(lock["cycle"], 834)
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
        self.assertTrue(lock["window_peels_closed"])
        self.assertTrue(lock["prev1_gram_list_absent"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev1"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev184"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next185"])
        self.assertEqual(lock["next_cheap_lock"], STANDING_NEXT_CHEAP_LOCK)
        self.assertEqual(lock["hold_index"], STANDING_HOLD_INDEX)
        self.assertEqual(tuple(lock["incomplete_indexes"]), STANDING_INCOMPLETE_INDEXES)
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
