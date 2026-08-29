"""H–P pairwise n≥8 islands that are exact-0 on Q.

Cycle 111 text-search lock. Uses already-vendored A–V and the
cycle-69 eighteen maximal H–P pairwise islands. Does not vendor a
new tablet. Does not scrape X. W has no Barthel (cycle 100); skip
W. Does not redo H–P pairwise n≥8 or H∩P∩Q triple inventories.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Locks exact contiguous Q hit counts of those 18 locked H∩P
sequences (same Barthel parser as the cycle-110 H–Q vs P lock)
and how many are exact-0 on Q. Arithmetic 18−5=13 is a
hypothesis, not a lock: two cycle-71 triples are proper
substrings of longer H–P islands that themselves miss Q. Claim
that can lose: hp_islands_zero_on_q_count_holds (measured N
equals the locked count).

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_hpq_island_recto_gap1_pairwise_scoreboard import (
    STANDING_HP_H_SITE,
    STANDING_HP_N,
    STANDING_HP_P_SITE,
    STANDING_HP_TOKENS,
    TestMamariHpqIslandRectoGap1PairwiseScoreboard,
)
from tests.test_mamari_hpq_triple_n8_scoreboard import (
    STANDING_MAXIMAL_COUNT as STANDING_TRIPLE_COUNT,
    STANDING_MAXIMALS,
    TestMamariHpqTripleN8Scoreboard,
)
from tests.test_mamari_hq_islands_zero_on_p_scoreboard import (
    TestMamariHqIslandsZeroOnPScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
    substring_offsets,
)
from tests.test_mamari_large_santiago_st_petersburg_shared_n8_scoreboard import (
    STANDING_MAXIMAL_COUNT as STANDING_HP_MAXIMAL_COUNT,
    STANDING_MAXIMALS as STANDING_HP_MAXIMALS,
    TestMamariLargeSantiagoStPetersburgSharedN8Scoreboard,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    SIDE_HR,
    SIDE_HV,
    SIDE_PR,
    SIDE_PV,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    concat_sides,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    LINE_NAMES,
    named_qhp_hits,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides as load_h_p_q_sides,
)
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    Q_SIDES,
    SIDE_QR,
    SIDE_QV,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

LOCKED_HP_ISLANDS = tuple(
    tokens for tokens, _n, _fh, _fp, _hs, _ps in STANDING_HP_MAXIMALS
)
LOCKED_TRIPLE_ISLANDS = tuple(
    tokens for tokens, _n, _fh, _fp, _fq, _h, _p, _q in STANDING_MAXIMALS
)
STANDING_ZERO_ON_Q_INDICES = (0, 1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17)
STANDING_HIT_ON_Q_INDICES = (4, 7, 16)
STANDING_ZERO_ON_Q_NS = (22, 13, 13, 12, 11, 11, 10, 10, 9, 9, 8, 8, 8, 8, 8)
STANDING_HIT_ON_Q_NS = (11, 10, 8)
STANDING_HIT_Q_SITES = (
    ((SIDE_QR, "Qr3", 7),),
    ((SIDE_QR, "Qr5", 15),),
    ((SIDE_QV, "Qv5", 11),),
)
STANDING_HP_ISLANDS_ZERO_ON_Q = 15
STANDING_HP_ISLANDS_HIT_ON_Q = 3
STANDING_HP_ISLANDS_ZERO_ON_Q_COUNT_HOLDS = True
STANDING_ARITHMETIC_18_MINUS_5 = 13
STANDING_ARITHMETIC_18_MINUS_5_HOLDS = False
STANDING_N22_IS_ZERO_ON_Q = True
STANDING_TRIPLE_ISLANDS_HIT_ON_Q = True
STANDING_TRIPLE_ISLANDS_ZERO_ON_Q = 0
STANDING_EXACT_TRIPLE_IN_HP18 = 3
STANDING_TRIPLE_PROPER_SUBSTRING_OF_HP = 2
STANDING_TRIPLE_N12_PARENT_INDEX = 1
STANDING_TRIPLE_N12_PARENT_OFFSETS = (0,)
STANDING_TRIPLE_N8_PARENT_INDEX = 3
STANDING_TRIPLE_N8_PARENT_OFFSETS = (3,)
STANDING_CLAIM = "hp_islands_zero_on_q_count_holds"
STANDING_RESULT = "hp_islands_zero_on_q"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_HYPOTHESIS_N = 13


def island_q_sites(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Exact contiguous Q sites of one locked H–P island sequence."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    return named_qhp_hits(by_side, Q_SIDES, tokens)


def island_q_hits(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> int:
    """Exact contiguous Q hit count. Search only."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    return ngram_hit_count(concat_sides(by_side, Q_SIDES), tokens)


def island_is_zero_on_q(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> bool:
    """True iff the island sequence is exact-0 on Q."""
    return island_q_hits(tokens, by_side) == 0


def classify_hp_islands(
    maximals: tuple = STANDING_HP_MAXIMALS,
    by_side: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple, ...]:
    """(tokens, n, h_site, p_site, q_hits, q_sites, zero_on_q) per island."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    rows = []
    for tokens, n, _fh, _fp, h_site, p_site in maximals:
        q_sites = island_q_sites(tokens, by_side)
        q_hits = len(q_sites)
        rows.append((tokens, n, h_site, p_site, q_hits, q_sites, q_hits == 0))
    return tuple(rows)


def zero_on_q_count(
    maximals: tuple = STANDING_HP_MAXIMALS,
    by_side: dict[str, list[list[str]]] | None = None,
) -> int:
    """How many locked H–P islands are exact-0 on Q."""
    return sum(1 for *_rest, zero in classify_hp_islands(maximals, by_side) if zero)


def hp_islands_zero_on_q_count_holds(
    measured: int,
    locked: int = STANDING_HP_ISLANDS_ZERO_ON_Q,
) -> bool:
    """True iff measured N equals the locked count. The claim that can lose."""
    return measured == locked


class TestHpIslandsZeroOnQHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_contiguous_q_hits_classify_zero_versus_hit(self):
        """A planted Q run counts; a gap or a miss is exact-0."""
        provider = MockProvider()
        planted = ("111", "222", "333", "444", "555", "666", "777", "888")
        miss = ("000", "000", "000", "000", "000", "000", "000", "000")
        self.assertEqual(ngram_hit_count([list(planted)], planted), 1)
        self.assertEqual(ngram_hit_count([list(planted[:4]) + ["999"] + list(planted[4:])], planted), 0)
        self.assertEqual(ngram_hit_count([[]], planted), 0)
        by_side = load_h_p_q_sides()
        by_side[SIDE_QR] = [list(planted)]
        by_side[SIDE_QV] = [[]]
        planted_row = (planted, 8, 1, 1, (SIDE_HR, "Hr1", 0), (SIDE_PR, "Pr1", 0))
        miss_row = (miss, 8, 1, 1, (SIDE_HR, "Hr1", 1), (SIDE_PR, "Pr1", 1))
        self.assertEqual(island_q_hits(planted, by_side), 1)
        self.assertEqual(island_q_sites(planted, by_side), ((SIDE_QR, LINE_NAMES[SIDE_QR][0], 0),))
        self.assertFalse(island_is_zero_on_q(planted, by_side))
        self.assertEqual(island_q_hits(miss, by_side), 0)
        self.assertEqual(island_q_sites(miss, by_side), ())
        self.assertTrue(island_is_zero_on_q(miss, by_side))
        classified = classify_hp_islands((planted_row, miss_row), by_side)
        self.assertEqual(classified[0][4], 1)
        self.assertFalse(classified[0][6])
        self.assertEqual(classified[1][4], 0)
        self.assertTrue(classified[1][6])
        self.assertEqual(zero_on_q_count((planted_row, miss_row), by_side), 1)
        self.assertTrue(hp_islands_zero_on_q_count_holds(15, 15))
        self.assertFalse(hp_islands_zero_on_q_count_holds(13, 15))
        self.assertEqual(STANDING_CLAIM, "hp_islands_zero_on_q_count_holds")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHpIslandsZeroOnQScoreboard(unittest.TestCase):
    """Cited-fixture H–P islands vs exact Q hits. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.hpq_sides = load_h_p_q_sides()
        self.rows = classify_hp_islands(STANDING_HP_MAXIMALS, self.hpq_sides)
        self.measured_n = zero_on_q_count(STANDING_HP_MAXIMALS, self.hpq_sides)
        self.claim_holds = hp_islands_zero_on_q_count_holds(self.measured_n)
        self.zero_rows = tuple(row for row in self.rows if row[6])
        self.hit_rows = tuple(row for row in self.rows if not row[6])
        self.triple_q_hits = tuple(
            island_q_hits(tokens, self.hpq_sides) for tokens in LOCKED_TRIPLE_ISLANDS
        )

    def test_islands_are_the_locked_cycle_69_hp_maximals(self):
        """Eighteen sequences come from cycle 69. None invented."""
        self.assertEqual(len(LOCKED_HP_ISLANDS), STANDING_HP_MAXIMAL_COUNT)
        self.assertEqual(STANDING_HP_MAXIMAL_COUNT, 18)
        self.assertEqual(len(STANDING_HP_MAXIMALS), 18)
        self.assertEqual(LOCKED_HP_ISLANDS, tuple(row[0] for row in STANDING_HP_MAXIMALS))
        self.assertEqual(STANDING_HP_MAXIMALS[0][0], STANDING_HP_TOKENS)
        self.assertEqual(STANDING_HP_MAXIMALS[0][1], 22)
        self.assertEqual(STANDING_HP_MAXIMALS[0][4], STANDING_HP_H_SITE)
        self.assertEqual(STANDING_HP_MAXIMALS[0][5], STANDING_HP_P_SITE)
        self.assertEqual(
            self.survey["tablet_h_p_shared_n8_inventory"]["maximal_count"], 18
        )
        self.assertEqual(
            self.survey["tablet_h_p_shared_n8_inventory"]["maximals"][0][1], 22
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_fifteen_of_eighteen_are_exact_zero_on_q(self):
        """Measured N is 15. Arithmetic 18−5=13 does not hold."""
        self.assertEqual(len(self.rows), 18)
        self.assertEqual(self.measured_n, STANDING_HP_ISLANDS_ZERO_ON_Q)
        self.assertEqual(STANDING_HP_ISLANDS_ZERO_ON_Q, 15)
        self.assertEqual(len(self.zero_rows), 15)
        self.assertEqual(len(self.hit_rows), STANDING_HP_ISLANDS_HIT_ON_Q)
        self.assertEqual(STANDING_HP_ISLANDS_HIT_ON_Q, 3)
        self.assertEqual(self.measured_n + len(self.hit_rows), 18)
        self.assertEqual(
            tuple(i for i, row in enumerate(self.rows) if row[6]),
            STANDING_ZERO_ON_Q_INDICES,
        )
        self.assertEqual(
            tuple(i for i, row in enumerate(self.rows) if not row[6]),
            STANDING_HIT_ON_Q_INDICES,
        )
        self.assertEqual(tuple(row[1] for row in self.zero_rows), STANDING_ZERO_ON_Q_NS)
        self.assertEqual(tuple(row[1] for row in self.hit_rows), STANDING_HIT_ON_Q_NS)
        for tokens, n, h_site, p_site, q_hits, q_sites, zero in self.zero_rows:
            self.assertTrue(zero)
            self.assertEqual(q_hits, 0)
            self.assertEqual(q_sites, ())
            self.assertEqual(island_q_hits(tokens, self.hpq_sides), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, tokens, VENDORED_TABLETS)[
                    VENDORED_TABLETS.index("Q")
                ],
                0,
            )
            self.assertGreaterEqual(n, 8)
            self.assertEqual(len(tokens), n)
        self.assertEqual(STANDING_ARITHMETIC_18_MINUS_5, STANDING_HYPOTHESIS_N)
        self.assertEqual(STANDING_ARITHMETIC_18_MINUS_5, 13)
        self.assertFalse(STANDING_ARITHMETIC_18_MINUS_5_HOLDS)
        self.assertNotEqual(self.measured_n, STANDING_ARITHMETIC_18_MINUS_5)
        self.assertEqual(self.claim_holds, STANDING_HP_ISLANDS_ZERO_ON_Q_COUNT_HOLDS)
        self.assertTrue(STANDING_HP_ISLANDS_ZERO_ON_Q_COUNT_HOLDS)
        self.assertTrue(hp_islands_zero_on_q_count_holds(self.measured_n))
        self.assertFalse(hp_islands_zero_on_q_count_holds(13))
        self.assertEqual(STANDING_CLAIM, "hp_islands_zero_on_q_count_holds")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n22_from_cycle_75_is_in_the_zero_on_q_set(self):
        """Cycle-75 maximal H∩P n=22 is one of the fifteen exact-0 rows."""
        tokens_22, n_22, h_22, p_22, q_hits_22, q_sites_22, zero_22 = self.rows[0]
        self.assertEqual(tokens_22, STANDING_HP_TOKENS)
        self.assertEqual(n_22, STANDING_HP_N)
        self.assertEqual(n_22, 22)
        self.assertEqual(h_22, STANDING_HP_H_SITE)
        self.assertEqual(p_22, STANDING_HP_P_SITE)
        self.assertEqual(h_22, (SIDE_HR, "Hr5", 6))
        self.assertEqual(p_22, (SIDE_PR, "Pr4", 71))
        self.assertEqual(q_hits_22, 0)
        self.assertEqual(q_sites_22, ())
        self.assertTrue(zero_22)
        self.assertTrue(STANDING_N22_IS_ZERO_ON_Q)
        self.assertIn(self.rows[0], self.zero_rows)
        self.assertEqual(
            self.survey["tablet_h_p_q_island_recto_gap1_pairwise"]["hp_n"], 22
        )
        for side, line, index in (h_22, p_22):
            stems = self.hpq_sides[side][LINE_NAMES[side].index(line)][index : index + 22]
            self.assertEqual(tuple(stems), STANDING_HP_TOKENS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_three_q_hits_are_the_exact_triple_members_of_the_eighteen(self):
        """The three H–P islands with Q hits are exact cycle-71 triples."""
        self.assertEqual(len(LOCKED_TRIPLE_ISLANDS), STANDING_TRIPLE_COUNT)
        self.assertEqual(STANDING_TRIPLE_COUNT, 5)
        exact_triples = tuple(
            tokens for tokens in LOCKED_HP_ISLANDS if tokens in LOCKED_TRIPLE_ISLANDS
        )
        self.assertEqual(len(exact_triples), STANDING_EXACT_TRIPLE_IN_HP18)
        self.assertEqual(STANDING_EXACT_TRIPLE_IN_HP18, 3)
        self.assertEqual(tuple(row[0] for row in self.hit_rows), exact_triples)
        for (tokens, n, h_site, p_site, q_hits, q_sites, zero), expected_sites in zip(
            self.hit_rows, STANDING_HIT_Q_SITES, strict=True
        ):
            self.assertFalse(zero)
            self.assertEqual(q_hits, 1)
            self.assertEqual(q_sites, expected_sites)
            self.assertIn(tokens, LOCKED_TRIPLE_ISLANDS)
            self.assertGreaterEqual(n, 8)
            for side, line, index in (h_site, p_site) + q_sites:
                stems = self.hpq_sides[side][LINE_NAMES[side].index(line)][
                    index : index + n
                ]
                self.assertEqual(tuple(stems), tokens)
        self.assertEqual(self.hit_rows[0][1], 11)
        self.assertEqual(self.hit_rows[0][2], (SIDE_HR, "Hr3", 27))
        self.assertEqual(self.hit_rows[0][3], (SIDE_PR, "Pr3", 14))
        self.assertEqual(self.hit_rows[1][1], 10)
        self.assertEqual(self.hit_rows[1][2], (SIDE_HR, "Hr5", 36))
        self.assertEqual(self.hit_rows[1][3], (SIDE_PR, "Pr5", 9))
        self.assertEqual(self.hit_rows[2][1], 8)
        self.assertEqual(self.hit_rows[2][2], (SIDE_HV, "Hv2", 32))
        self.assertEqual(self.hit_rows[2][3], (SIDE_PV, "Pv4", 50))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_five_triple_islands_all_hit_q(self):
        """All five locked H∩P∩Q islands have Q hits. None are 0 on Q."""
        self.assertEqual(len(self.triple_q_hits), 5)
        self.assertTrue(all(hits >= 1 for hits in self.triple_q_hits))
        self.assertEqual(sum(1 for hits in self.triple_q_hits if hits == 0), 0)
        self.assertTrue(STANDING_TRIPLE_ISLANDS_HIT_ON_Q)
        self.assertEqual(STANDING_TRIPLE_ISLANDS_ZERO_ON_Q, 0)
        for tokens, n, _fh, _fp, _fq, h_site, p_site, q_site in STANDING_MAXIMALS:
            q_hits = island_q_hits(tokens, self.hpq_sides)
            q_sites = island_q_sites(tokens, self.hpq_sides)
            self.assertGreaterEqual(q_hits, 1)
            self.assertIn(q_site, q_sites)
            self.assertFalse(island_is_zero_on_q(tokens, self.hpq_sides))
            self.assertGreaterEqual(n, 8)
        # Two triples are proper substrings of longer H–P islands that miss Q.
        triple_n12 = STANDING_MAXIMALS[0][0]
        parent_13 = STANDING_HP_MAXIMALS[STANDING_TRIPLE_N12_PARENT_INDEX]
        self.assertEqual(parent_13[1], 13)
        self.assertEqual(parent_13[4], (SIDE_HR, "Hr8", 0))
        self.assertEqual(parent_13[5], (SIDE_PR, "Pr7", 29))
        self.assertEqual(
            substring_offsets(triple_n12, parent_13[0]),
            STANDING_TRIPLE_N12_PARENT_OFFSETS,
        )
        self.assertFalse(is_contiguous_substring(parent_13[0], triple_n12))
        self.assertTrue(self.rows[STANDING_TRIPLE_N12_PARENT_INDEX][6])
        triple_n8 = STANDING_MAXIMALS[3][0]
        parent_12 = STANDING_HP_MAXIMALS[STANDING_TRIPLE_N8_PARENT_INDEX]
        self.assertEqual(parent_12[1], 12)
        self.assertEqual(parent_12[4], (SIDE_HR, "Hr7", 44))
        self.assertEqual(parent_12[5], (SIDE_PR, "Pr7", 7))
        self.assertEqual(
            substring_offsets(triple_n8, parent_12[0]),
            STANDING_TRIPLE_N8_PARENT_OFFSETS,
        )
        self.assertFalse(is_contiguous_substring(parent_12[0], triple_n8))
        self.assertTrue(self.rows[STANDING_TRIPLE_N8_PARENT_INDEX][6])
        self.assertEqual(STANDING_TRIPLE_PROPER_SUBSTRING_OF_HP, 2)
        proper = 0
        for tokens in LOCKED_TRIPLE_ISLANDS:
            if tokens in LOCKED_HP_ISLANDS:
                continue
            parents = [
                i
                for i, hp in enumerate(LOCKED_HP_ISLANDS)
                if is_contiguous_substring(tokens, hp)
            ]
            self.assertTrue(parents)
            self.assertTrue(all(self.rows[i][6] for i in parents))
            proper += 1
        self.assertEqual(proper, STANDING_TRIPLE_PROPER_SUBSTRING_OF_HP)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_pairwise_triple_and_w_scoreboards_still_compute(self):
        """Cycle 69 H–P pairwise, cycle 71 triples, cycle 110, and W stay."""
        prior_hp = TestMamariLargeSantiagoStPetersburgSharedN8Scoreboard()
        prior_hp.setUp()
        prior_hp.test_inventory_tokens_n_freq_and_hits()
        prior_hp.test_survey_matches_computed_lock()
        prior_triple = TestMamariHpqTripleN8Scoreboard()
        prior_triple.setUp()
        prior_triple.test_inventory_tokens_n_freq_and_hits()
        prior_triple.test_survey_matches_computed_lock()
        prior_110 = TestMamariHqIslandsZeroOnPScoreboard()
        prior_110.setUp()
        prior_110.test_twelve_of_fifteen_are_exact_zero_on_p()
        prior_110.test_survey_matches_computed_lock()
        prior_75 = TestMamariHpqIslandRectoGap1PairwiseScoreboard()
        prior_75.setUp()
        prior_75.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-111 zero-on-Q count."""
        lock = self.survey["hp_islands_zero_on_q"]
        self.assertEqual(lock["cycle"], 111)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["island_count"], STANDING_HP_MAXIMAL_COUNT)
        self.assertEqual(lock["island_count"], 18)
        self.assertEqual(lock["hp_islands_zero_on_q"], STANDING_HP_ISLANDS_ZERO_ON_Q)
        self.assertEqual(lock["hp_islands_zero_on_q"], 15)
        self.assertEqual(lock["hp_islands_hit_on_q"], STANDING_HP_ISLANDS_HIT_ON_Q)
        self.assertEqual(lock["from_cycle"], 69)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["hp_islands_zero_on_q_count_holds"])
        self.assertEqual(
            lock["hp_islands_zero_on_q_count_holds"],
            STANDING_HP_ISLANDS_ZERO_ON_Q_COUNT_HOLDS,
        )
        self.assertEqual(lock["arithmetic_18_minus_5"], STANDING_ARITHMETIC_18_MINUS_5)
        self.assertFalse(lock["arithmetic_18_minus_5_holds"])
        self.assertEqual(
            lock["arithmetic_18_minus_5_holds"], STANDING_ARITHMETIC_18_MINUS_5_HOLDS
        )
        self.assertTrue(lock["n22_is_zero_on_q"])
        self.assertEqual(lock["n22_is_zero_on_q"], STANDING_N22_IS_ZERO_ON_Q)
        self.assertEqual(tuple(lock["zero_on_q_ns"]), STANDING_ZERO_ON_Q_NS)
        self.assertEqual(tuple(lock["hit_on_q_ns"]), STANDING_HIT_ON_Q_NS)
        self.assertEqual(tuple(lock["zero_on_q_indices"]), STANDING_ZERO_ON_Q_INDICES)
        self.assertEqual(tuple(lock["hit_on_q_indices"]), STANDING_HIT_ON_Q_INDICES)
        self.assertEqual(len(lock["islands"]), 18)
        for computed, recorded in zip(self.rows, lock["islands"], strict=True):
            tokens, n, h_site, p_site, q_hits, q_sites, zero = computed
            self.assertEqual(tuple(recorded["tokens"]), tokens)
            self.assertEqual(recorded["n"], n)
            self.assertEqual(tuple(recorded["h_site"]), h_site)
            self.assertEqual(tuple(recorded["p_site"]), p_site)
            self.assertEqual(recorded["q_hits"], q_hits)
            self.assertEqual(tuple(tuple(site) for site in recorded["q_sites"]), q_sites)
            self.assertEqual(recorded["zero_on_q"], zero)
            self.assertEqual(recorded["exact_triple"], tokens in LOCKED_TRIPLE_ISLANDS)
        n22 = lock["islands"][0]
        self.assertEqual(tuple(n22["tokens"]), STANDING_HP_TOKENS)
        self.assertEqual(n22["n"], 22)
        self.assertTrue(n22["zero_on_q"])
        self.assertEqual(n22["q_hits"], 0)
        self.assertEqual(lock["triple_island_count"], STANDING_TRIPLE_COUNT)
        self.assertTrue(lock["triple_islands_hit_on_q"])
        self.assertEqual(lock["triple_islands_zero_on_q"], 0)
        self.assertEqual(lock["exact_triple_in_hp18"], STANDING_EXACT_TRIPLE_IN_HP18)
        self.assertEqual(
            lock["triple_proper_substring_of_hp"], STANDING_TRIPLE_PROPER_SUBSTRING_OF_HP
        )
        self.assertEqual(len(lock["triples"]), 5)
        for tokens, n, _fh, _fp, _fq, h_site, p_site, q_site in STANDING_MAXIMALS:
            recorded = next(
                row
                for row in lock["triples"]
                if tuple(row["tokens"]) == tokens
            )
            self.assertEqual(recorded["n"], n)
            self.assertEqual(tuple(recorded["h_site"]), h_site)
            self.assertEqual(tuple(recorded["p_site"]), p_site)
            self.assertEqual(tuple(recorded["q_site"]), q_site)
            self.assertGreaterEqual(recorded["q_hits"], 1)
            self.assertFalse(recorded["zero_on_q"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_hp_shared_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hq_islands_zero_on_p_unchanged"])
        self.assertTrue(lock["standing_hpq_island_recto_gap1_pairwise_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_h_p_shared_n8_inventory"]["cycle"], 69)
        self.assertEqual(self.survey["tablet_h_p_shared_n8_inventory"]["maximal_count"], 18)
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertEqual(
            self.survey["tablet_h_p_q_triple_n8_inventory"]["maximal_count"], 5
        )
        self.assertEqual(self.survey["hq_islands_zero_on_p"]["cycle"], 110)
        self.assertEqual(self.survey["hq_islands_zero_on_p"]["hq_islands_zero_on_p"], 12)
        self.assertFalse(self.survey["hq_islands_zero_on_p"]["arithmetic_15_minus_5_holds"])
        self.assertEqual(self.survey["tablet_h_p_q_island_recto_gap1_pairwise"]["cycle"], 75)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHpIslandsZeroOnQImageSnapshot(unittest.TestCase):
    """Cycle 111 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
