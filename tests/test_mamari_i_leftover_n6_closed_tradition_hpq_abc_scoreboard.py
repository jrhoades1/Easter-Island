"""Reframed closed-tradition hold-out of the locked leftover-6 grams.

Cycle 833 text-search lock. Uses already-vendored A–V and the
cycle-457 leftover n=6 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 remaining-
after-076-010 leftover 6-grams (N=18). HEAD-check: the I-local
claim (exact contiguous on I and exact-0 on A/B/C/H/P/Q) is
already the cycle-457 all-tablet I-only HOLD (exact-1 on I,
exact-0 on every other vendored tablet). This cycle does not
re-lock it. Cycle 832 put I in the absent set and locked leak
LOSE. The novel claim drops I from the absent set.

Claim that can lose: each of the 18 locked leftover-6 grams is
an exact contiguous hit on ≥1 of H/P/Q and exact-0 on A/B/C.
hits_I is recorded and is not a leak. HOLD needs that claim
true for the whole population (N_hold=18, N_leak=0). Leak onto
A/B/C is leak LOSE. An empty H/P/Q hit set with zero A/B/C hits
is incomplete-set LOSE.

Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Does not reopen leftover-6
next/prev window peels (next-side exhausted at cycle 831;
prev-side eighteen-hole 0/18 since cycle 800). Do not launch
leftover-6 prev-184 or leftover-6 next-185. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning dictionary.

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_i_leftover_n6_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_6grams_i_only_scoreboard import (
    STANDING_HITS_BY_TABLET_ONE_ON_I as CYCLE457_HITS_ONE_ON_I,
    STANDING_I_LEFTOVER_N6_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_ALL_I_ONLY as CYCLE457_I_ONLY,
    STANDING_LEFTOVER_MATCHING_COUNT as CYCLE457_N,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE457_SITES,
    STANDING_N as CYCLE457_STANDING_N,
    STANDING_RESULT as CYCLE457_RESULT,
    STANDING_SEQUENCES as CYCLE457_SEQUENCES,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HPQ_TABLETS = ("H", "P", "Q")
ABSENT_TABLETS = ("A", "B", "C")
PROBE_TABLETS = HPQ_TABLETS + ABSENT_TABLETS + ("I",)
MIN_HPQ_TABLETS = 1

CYCLE832_RESULT = "i_leftover_n6_closed_tradition_hpq_abci"
CYCLE831_SURVEY_KEY = (
    "i_leftover_n6_remaining_after_090_076_remaining_after_430_076_"
    "remaining_after_076_020_remaining_after_076_010_next184_i_only"
)

STANDING_N = 18
STANDING_HITS_EACH = (0, 0, 0, 0, 0, 0, 1)
STANDING_HITS = (STANDING_HITS_EACH,) * STANDING_N
STANDING_SITES = CYCLE457_SITES
STANDING_SEQUENCES = CYCLE457_SEQUENCES
STANDING_N_HPQ_GE1 = 0
STANDING_N_HPQ_GE2 = 0
STANDING_N_EXACT0_ABC = 18
STANDING_N_I_GE1 = 18
STANDING_N_EXACT0_I = 0
STANDING_N_LEAK = 0
STANDING_N_HOLD = 0
STANDING_HITS_H = 0
STANDING_HITS_P = 0
STANDING_HITS_Q = 0
STANDING_HITS_A = 0
STANDING_HITS_B = 0
STANDING_HITS_C = 0
STANDING_HITS_I = 18
STANDING_VERDICT = "incomplete-set LOSE"
STANDING_CLAIM_HOLDS = False
STANDING_CLAIM = "leftover6_reframed_closed_tradition_hpq_ge1_and_exact0_abc"
STANDING_RESULT = "i_leftover_n6_closed_tradition_hpq_abc"
STANDING_AXIS = "closed-tradition-reframed"
STANDING_FROM_CYCLE = 457
STANDING_I_LOCAL_ALREADY_LOCKED = True
STANDING_I_LOCAL_CYCLE = 457
STANDING_WINDOW_PEELS_CLOSED = True
STANDING_DO_NOT_LAUNCH_PREV184 = True
STANDING_DO_NOT_LAUNCH_NEXT185 = True
STANDING_DO_NOT_RELOCK_I_LOCAL = True
STANDING_NEW_TABLET = False
STANDING_I_IN_ABSENT_SET = False
STANDING_NEXT_CHEAP_LOCK = (
    "cycle458_next1_reframed_closed_tradition_hpq_ge1_exact0_abc"
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


@dataclass(frozen=True)
class ReframedClosedTraditionRow:
    """One leftover-6 gram's exact hit counts. Ids only."""

    tokens: tuple[str, ...]
    site: tuple[str, str, int]
    hits: tuple[int, ...]

    def as_map(self) -> dict[str, int]:
        return dict(zip(PROBE_TABLETS, self.hits, strict=True))


def hpq_tablets_hit(hits: dict[str, int]) -> int:
    """How many of H/P/Q have at least one exact contiguous hit."""
    return sum(1 for tablet in HPQ_TABLETS if hits[tablet] >= 1)


def absent_hit_sum(hits: dict[str, int]) -> int:
    """Exact hit total on the absent set A/B/C. I is not in that set."""
    return sum(hits[tablet] for tablet in ABSENT_TABLETS)


def row_holds(hits: dict[str, int]) -> bool:
    """True iff ≥1 of H/P/Q hits and A/B/C are exact-0."""
    return hpq_tablets_hit(hits) >= MIN_HPQ_TABLETS and absent_hit_sum(hits) == 0


def row_leaks(hits: dict[str, int]) -> bool:
    """True iff any A/B/C tablet has an exact hit. An I hit is not a leak."""
    return absent_hit_sum(hits) > 0


def reframed_verdict(rows: tuple[ReframedClosedTraditionRow, ...]) -> str:
    """HOLD, leak LOSE, or incomplete-set LOSE. Leak wins if both fail."""
    if not rows:
        return "incomplete-set LOSE"
    if any(row_leaks(row.as_map()) for row in rows):
        return "leak LOSE"
    if all(row_holds(row.as_map()) for row in rows):
        return "HOLD"
    return "incomplete-set LOSE"


def score_reframed_closed_tradition(
    by_tablet: dict[str, list[list[str]]],
    sequences: tuple[tuple[str, ...], ...] = STANDING_SEQUENCES,
    sites: tuple[tuple[str, str, int], ...] = STANDING_SITES,
) -> tuple[ReframedClosedTraditionRow, ...]:
    """Exact contiguous probe counts. Search only."""
    rows = []
    for tokens, site in zip(sequences, sites, strict=True):
        hits = tuple(ngram_hit_count(by_tablet[tablet], tokens) for tablet in PROBE_TABLETS)
        rows.append(ReframedClosedTraditionRow(tokens=tokens, site=site, hits=hits))
    return tuple(rows)


def summarize(rows: tuple[ReframedClosedTraditionRow, ...]) -> dict[str, int]:
    """Population counts for the locked table. Search only."""
    maps = [row.as_map() for row in rows]
    return {
        "N": len(rows),
        "N_hpq_ge1": sum(1 for hits in maps if hpq_tablets_hit(hits) >= 1),
        "N_hpq_ge2": sum(1 for hits in maps if hpq_tablets_hit(hits) >= 2),
        "N_exact0_abc": sum(
            1 for hits in maps if hits["A"] == hits["B"] == hits["C"] == 0
        ),
        "N_i_ge1": sum(1 for hits in maps if hits["I"] >= 1),
        "N_exact0_i": sum(1 for hits in maps if hits["I"] == 0),
        "N_leak": sum(1 for hits in maps if row_leaks(hits)),
        "N_hold": sum(1 for hits in maps if row_holds(hits)),
        "hits_H": sum(hits["H"] for hits in maps),
        "hits_P": sum(hits["P"] for hits in maps),
        "hits_Q": sum(hits["Q"] for hits in maps),
        "hits_A": sum(hits["A"] for hits in maps),
        "hits_B": sum(hits["B"] for hits in maps),
        "hits_C": sum(hits["C"] for hits in maps),
        "hits_I": sum(hits["I"] for hits in maps),
    }


class TestReframedClosedTraditionHelpers(unittest.TestCase):
    """Helpers on synthetic counts. No CV, no LLM."""

    def test_hold_needs_one_hpq_tablet_and_exact_zero_abc(self):
        """A planted H hit with A/B/C at 0 holds. An A hit leaks. I alone is incomplete."""
        provider = MockProvider()
        hold = {"H": 1, "P": 0, "Q": 0, "A": 0, "B": 0, "C": 0, "I": 1}
        leak_a = {"H": 1, "P": 1, "Q": 1, "A": 1, "B": 0, "C": 0, "I": 1}
        i_only = {"H": 0, "P": 0, "Q": 0, "A": 0, "B": 0, "C": 0, "I": 1}
        empty = {"H": 0, "P": 0, "Q": 0, "A": 0, "B": 0, "C": 0, "I": 0}
        self.assertTrue(row_holds(hold))
        self.assertFalse(row_leaks(hold))
        self.assertFalse(row_holds(leak_a))
        self.assertTrue(row_leaks(leak_a))
        self.assertFalse(row_holds(i_only))
        self.assertFalse(row_leaks(i_only))
        self.assertFalse(row_holds(empty))
        self.assertFalse(row_leaks(empty))
        held = ReframedClosedTraditionRow(
            tokens=("1",), site=("H", "Hr1", 0), hits=(1, 0, 0, 0, 0, 0, 1)
        )
        leaked = ReframedClosedTraditionRow(
            tokens=("1",), site=("A", "Aa1", 0), hits=(0, 0, 0, 1, 0, 0, 0)
        )
        i_local = ReframedClosedTraditionRow(
            tokens=("1",), site=("I", "Ia1", 0), hits=(0, 0, 0, 0, 0, 0, 1)
        )
        self.assertEqual(reframed_verdict((held,)), "HOLD")
        self.assertEqual(reframed_verdict((leaked,)), "leak LOSE")
        self.assertEqual(reframed_verdict((held, leaked)), "leak LOSE")
        self.assertEqual(reframed_verdict((i_local,)), "incomplete-set LOSE")
        self.assertEqual(reframed_verdict(()), "incomplete-set LOSE")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN6ClosedTraditionHpqAbcScoreboard(unittest.TestCase):
    """Cycle 833 reframed closed-tradition lock on the cycle-457 leftover-6 population."""

    @classmethod
    def setUpClass(cls):
        cls.by_tablet = load_vendored_a_through_v()
        cls.rows = score_reframed_closed_tradition(cls.by_tablet)
        cls.summary = summarize(cls.rows)
        cls.verdict = reframed_verdict(cls.rows)
        cls.survey = load_corpus_survey()

    def setUp(self):
        self.provider = MockProvider()

    def test_population_is_the_locked_cycle_457_leftover_6grams(self):
        """Eighteen sequences and sites come from cycle 457. None invented."""
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N)
        self.assertEqual(len(STANDING_SITES), STANDING_N)
        self.assertEqual(STANDING_SEQUENCES, CYCLE457_SEQUENCES)
        self.assertEqual(STANDING_SITES, CYCLE457_SITES)
        self.assertEqual(CYCLE457_N, 18)
        self.assertEqual(CYCLE457_STANDING_N, 18)
        self.assertTrue(CYCLE457_I_ONLY)
        self.assertEqual(STANDING_FROM_CYCLE, 457)
        self.assertEqual(len(self.rows), 18)
        for row, tokens, site in zip(self.rows, STANDING_SEQUENCES, STANDING_SITES, strict=True):
            self.assertEqual(row.tokens, tokens)
            self.assertEqual(row.site, site)
            self.assertEqual(len(row.tokens), 6)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_local_already_locked_on_cycle_457(self):
        """Exact-1 on I and exact-0 on A/B/C/H/P/Q is the cycle-457 I-only HOLD."""
        prior = self.survey[CYCLE457_RESULT]
        self.assertEqual(prior["cycle"], STANDING_I_LOCAL_CYCLE)
        self.assertTrue(prior["hypothesis_all_i_only"])
        self.assertEqual(prior["N"], 18)
        self.assertEqual(prior["N_leak"], 0)
        self.assertTrue(prior["complete_set"])
        self.assertEqual(CYCLE457_HITS_ONE_ON_I, tuple(
            1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
        ))
        for tablet in ("A", "B", "C", "H", "P", "Q"):
            index = VENDORED_TABLETS.index(tablet)
            self.assertEqual(CYCLE457_HITS_ONE_ON_I[index], 0)
        self.assertEqual(CYCLE457_HITS_ONE_ON_I[VENDORED_TABLETS.index("I")], 1)
        self.assertTrue(STANDING_I_LOCAL_ALREADY_LOCKED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_I_LOCAL)
        self.assertFalse(STANDING_I_IN_ABSENT_SET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_measured_table_is_incomplete_set_lose(self):
        """H/P/Q are exact-0, A/B/C are exact-0, and each gram hits I once."""
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
        for row in self.rows:
            self.assertEqual(row.hits, STANDING_HITS_EACH)
            hits = row.as_map()
            self.assertEqual(hits["I"], 1)
            self.assertEqual(hits["H"], 0)
            self.assertEqual(hits["P"], 0)
            self.assertEqual(hits["Q"], 0)
            self.assertEqual(hits["A"], 0)
            self.assertEqual(hits["B"], 0)
            self.assertEqual(hits["C"], 0)
            self.assertFalse(row_leaks(hits))
            self.assertFalse(row_holds(hits))
            self.assertEqual(hpq_tablets_hit(hits), 0)
            self.assertEqual(absent_hit_sum(hits), 0)
        self.assertEqual(self.verdict, STANDING_VERDICT)
        self.assertEqual(self.verdict, "incomplete-set LOSE")
        self.assertFalse(STANDING_CLAIM_HOLDS)
        self.assertEqual(STANDING_AXIS, "closed-tradition-reframed")
        self.assertEqual(MIN_HPQ_TABLETS, 1)
        self.assertEqual(ABSENT_TABLETS, ("A", "B", "C"))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_cycle_832_kept_i_in_the_absent_set(self):
        """Cycle 832's leak LOSE is the same hit table with I counted as absent."""
        prior = self.survey[CYCLE832_RESULT]
        self.assertEqual(prior["cycle"], 832)
        self.assertEqual(prior["verdict"], "leak LOSE")
        self.assertEqual(prior["N_leak"], 18)
        self.assertEqual(prior["N_hpq_ge1"], 0)
        self.assertEqual(prior["N_hpq_ge2"], 0)
        self.assertEqual(prior["N_exact0_abc"], 18)
        self.assertEqual(prior["hits_I"], 18)
        self.assertEqual(prior["leak_tablet"], "I")
        self.assertTrue(prior["do_not_launch_cycle_833"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_order_gap_inventory_already_locked_and_window_peels_closed(self):
        """Those axes stay prior locks. This note does not open another peel."""
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-833 incomplete-set LOSE table."""
        lock = self.survey[STANDING_RESULT]
        self.assertEqual(lock["cycle"], 833)
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
        self.assertTrue(lock["i_local_already_locked"])
        self.assertEqual(lock["i_local_cycle"], STANDING_I_LOCAL_CYCLE)
        self.assertTrue(lock["do_not_relock_i_local"])
        self.assertTrue(lock["window_peels_closed"])
        self.assertTrue(lock["do_not_launch_leftover_n6_prev184"])
        self.assertTrue(lock["do_not_launch_leftover_n6_next185"])
        self.assertEqual(lock["next_cheap_lock"], STANDING_NEXT_CHEAP_LOCK)
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
