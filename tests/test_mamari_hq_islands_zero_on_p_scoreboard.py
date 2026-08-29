"""H–Q pairwise n≥8 islands that are exact-0 on P.

Cycle 110 text-search lock. Uses already-vendored A–V and the
cycle-70 fifteen maximal Q–H pairwise islands. Does not vendor a
new tablet. Does not scrape X. W has no Barthel (cycle 100); skip
W. Does not redo H–Q pairwise n≥8 or H∩P∩Q triple inventories.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Locks exact contiguous P hit counts of those 15 locked H∩Q
sequences (same Barthel parser as the other island scoreboards)
and how many are exact-0 on P. Arithmetic 15−5=10 is a
hypothesis, not a lock: two cycle-71 triples are proper
substrings of longer H–Q islands that themselves miss P. Claim
that can lose: hq_islands_zero_on_p_count_holds (measured N
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
from tests.test_mamari_hq_7gram_hq_pairwise_island_substring_scoreboard import (
    STANDING_ISLAND_31_H_SITE,
    STANDING_ISLAND_31_N,
    STANDING_ISLAND_31_Q_SITE,
    STANDING_ISLAND_31_TOKENS,
    STANDING_MAXIMAL_P_HITS,
    TestMamariHq7gramHqPairwiseIslandSubstringScoreboard,
)
from tests.test_mamari_hpq_triple_n8_scoreboard import (
    STANDING_MAXIMAL_COUNT as STANDING_TRIPLE_COUNT,
    STANDING_MAXIMALS,
    TestMamariHpqTripleN8Scoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
    substring_offsets,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    P_SIDES,
    SIDE_HR,
    SIDE_HV,
    SIDE_PR,
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
    STANDING_QH_MAXIMAL_COUNT,
    STANDING_QH_MAXIMALS,
    TestMamariSmallStPetersburgSharedN8Scoreboard,
    named_qhp_hits,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides as load_h_p_q_sides,
)
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    SIDE_QR,
    SIDE_QV,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

LOCKED_HQ_ISLANDS = tuple(
    tokens for tokens, _n, _fq, _fh, _qs, _hs in STANDING_QH_MAXIMALS
)
LOCKED_TRIPLE_ISLANDS = tuple(
    tokens for tokens, _n, _fh, _fp, _fq, _h, _p, _q in STANDING_MAXIMALS
)
STANDING_ZERO_ON_P_INDICES = (0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 14)
STANDING_HIT_ON_P_INDICES = (6, 7, 13)
STANDING_ZERO_ON_P_NS = (31, 15, 15, 14, 13, 13, 11, 10, 10, 10, 10, 8)
STANDING_HIT_ON_P_NS = (12, 11, 8)
STANDING_HIT_P_SITES = (
    ((SIDE_PR, "Pr7", 29),),
    ((SIDE_PR, "Pr3", 14),),
    ((SIDE_PR, "Pr7", 10),),
)
STANDING_HQ_ISLANDS_ZERO_ON_P = 12
STANDING_HQ_ISLANDS_HIT_ON_P = 3
STANDING_HQ_ISLANDS_ZERO_ON_P_COUNT_HOLDS = True
STANDING_ARITHMETIC_15_MINUS_5 = 10
STANDING_ARITHMETIC_15_MINUS_5_HOLDS = False
STANDING_N31_IS_ZERO_ON_P = True
STANDING_TRIPLE_ISLANDS_HIT_ON_P = True
STANDING_TRIPLE_ISLANDS_ZERO_ON_P = 0
STANDING_EXACT_TRIPLE_IN_HQ15 = 3
STANDING_TRIPLE_PROPER_SUBSTRING_OF_HQ = 2
STANDING_TRIPLE_N10_PARENT_INDEX = 2
STANDING_TRIPLE_N10_PARENT_OFFSETS = (5,)
STANDING_TRIPLE_N8_VERSO_PARENT_INDEX = 3
STANDING_TRIPLE_N8_VERSO_PARENT_OFFSETS = (6,)
STANDING_CLAIM = "hq_islands_zero_on_p_count_holds"
STANDING_RESULT = "hq_islands_zero_on_p"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_HYPOTHESIS_N = 10


def island_p_sites(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Exact contiguous P sites of one locked H–Q island sequence."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    return named_qhp_hits(by_side, P_SIDES, tokens)


def island_p_hits(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> int:
    """Exact contiguous P hit count. Search only."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    return ngram_hit_count(concat_sides(by_side, P_SIDES), tokens)


def island_is_zero_on_p(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> bool:
    """True iff the island sequence is exact-0 on P."""
    return island_p_hits(tokens, by_side) == 0


def classify_hq_islands(
    maximals: tuple = STANDING_QH_MAXIMALS,
    by_side: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple, ...]:
    """(tokens, n, h_site, q_site, p_hits, p_sites, zero_on_p) per island."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    rows = []
    for tokens, n, _fq, _fh, q_site, h_site in maximals:
        p_sites = island_p_sites(tokens, by_side)
        p_hits = len(p_sites)
        rows.append((tokens, n, h_site, q_site, p_hits, p_sites, p_hits == 0))
    return tuple(rows)


def zero_on_p_count(
    maximals: tuple = STANDING_QH_MAXIMALS,
    by_side: dict[str, list[list[str]]] | None = None,
) -> int:
    """How many locked H–Q islands are exact-0 on P."""
    return sum(1 for *_rest, zero in classify_hq_islands(maximals, by_side) if zero)


def hq_islands_zero_on_p_count_holds(
    measured: int,
    locked: int = STANDING_HQ_ISLANDS_ZERO_ON_P,
) -> bool:
    """True iff measured N equals the locked count. The claim that can lose."""
    return measured == locked


class TestHqIslandsZeroOnPHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_contiguous_p_hits_classify_zero_versus_hit(self):
        """A planted P run counts; a gap or a miss is exact-0."""
        provider = MockProvider()
        planted = ("111", "222", "333", "444", "555", "666", "777", "888")
        miss = ("000", "000", "000", "000", "000", "000", "000", "000")
        self.assertEqual(ngram_hit_count([list(planted)], planted), 1)
        self.assertEqual(ngram_hit_count([list(planted[:4]) + ["999"] + list(planted[4:])], planted), 0)
        self.assertEqual(ngram_hit_count([[]], planted), 0)
        by_side = load_h_p_q_sides()
        by_side[SIDE_PR] = [list(planted)]
        by_side[SIDE_PV] = [[]]
        planted_row = (planted, 8, 1, 1, (SIDE_QR, "Qr1", 0), (SIDE_HR, "Hr1", 0))
        miss_row = (miss, 8, 1, 1, (SIDE_QR, "Qr1", 1), (SIDE_HR, "Hr1", 1))
        self.assertEqual(island_p_hits(planted, by_side), 1)
        self.assertEqual(island_p_sites(planted, by_side), ((SIDE_PR, LINE_NAMES[SIDE_PR][0], 0),))
        self.assertFalse(island_is_zero_on_p(planted, by_side))
        self.assertEqual(island_p_hits(miss, by_side), 0)
        self.assertEqual(island_p_sites(miss, by_side), ())
        self.assertTrue(island_is_zero_on_p(miss, by_side))
        classified = classify_hq_islands((planted_row, miss_row), by_side)
        self.assertEqual(classified[0][4], 1)
        self.assertFalse(classified[0][6])
        self.assertEqual(classified[1][4], 0)
        self.assertTrue(classified[1][6])
        self.assertEqual(zero_on_p_count((planted_row, miss_row), by_side), 1)
        self.assertTrue(hq_islands_zero_on_p_count_holds(12, 12))
        self.assertFalse(hq_islands_zero_on_p_count_holds(10, 12))
        self.assertEqual(STANDING_CLAIM, "hq_islands_zero_on_p_count_holds")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHqIslandsZeroOnPScoreboard(unittest.TestCase):
    """Cited-fixture H–Q islands vs exact P hits. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.hpq_sides = load_h_p_q_sides()
        self.rows = classify_hq_islands(STANDING_QH_MAXIMALS, self.hpq_sides)
        self.measured_n = zero_on_p_count(STANDING_QH_MAXIMALS, self.hpq_sides)
        self.claim_holds = hq_islands_zero_on_p_count_holds(self.measured_n)
        self.zero_rows = tuple(row for row in self.rows if row[6])
        self.hit_rows = tuple(row for row in self.rows if not row[6])
        self.triple_p_hits = tuple(
            island_p_hits(tokens, self.hpq_sides) for tokens in LOCKED_TRIPLE_ISLANDS
        )

    def test_islands_are_the_locked_cycle_70_qh_maximals(self):
        """Fifteen sequences come from cycle 70. None invented."""
        self.assertEqual(len(LOCKED_HQ_ISLANDS), STANDING_QH_MAXIMAL_COUNT)
        self.assertEqual(STANDING_QH_MAXIMAL_COUNT, 15)
        self.assertEqual(len(STANDING_QH_MAXIMALS), 15)
        self.assertEqual(LOCKED_HQ_ISLANDS, tuple(row[0] for row in STANDING_QH_MAXIMALS))
        self.assertEqual(STANDING_QH_MAXIMALS[0][0], STANDING_ISLAND_31_TOKENS)
        self.assertEqual(STANDING_QH_MAXIMALS[0][1], 31)
        self.assertEqual(STANDING_QH_MAXIMALS[0][5], STANDING_ISLAND_31_H_SITE)
        self.assertEqual(STANDING_QH_MAXIMALS[0][4], STANDING_ISLAND_31_Q_SITE)
        self.assertEqual(
            self.survey["tablet_q_shared_n8_inventory"]["q_vs_h"]["maximal_count"], 15
        )
        self.assertEqual(
            self.survey["tablet_q_shared_n8_inventory"]["q_vs_h"]["maximals"][0][1], 31
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_twelve_of_fifteen_are_exact_zero_on_p(self):
        """Measured N is 12. Arithmetic 15−5=10 does not hold."""
        self.assertEqual(len(self.rows), 15)
        self.assertEqual(self.measured_n, STANDING_HQ_ISLANDS_ZERO_ON_P)
        self.assertEqual(STANDING_HQ_ISLANDS_ZERO_ON_P, 12)
        self.assertEqual(len(self.zero_rows), 12)
        self.assertEqual(len(self.hit_rows), STANDING_HQ_ISLANDS_HIT_ON_P)
        self.assertEqual(STANDING_HQ_ISLANDS_HIT_ON_P, 3)
        self.assertEqual(self.measured_n + len(self.hit_rows), 15)
        self.assertEqual(
            tuple(i for i, row in enumerate(self.rows) if row[6]),
            STANDING_ZERO_ON_P_INDICES,
        )
        self.assertEqual(
            tuple(i for i, row in enumerate(self.rows) if not row[6]),
            STANDING_HIT_ON_P_INDICES,
        )
        self.assertEqual(tuple(row[1] for row in self.zero_rows), STANDING_ZERO_ON_P_NS)
        self.assertEqual(tuple(row[1] for row in self.hit_rows), STANDING_HIT_ON_P_NS)
        for tokens, n, h_site, q_site, p_hits, p_sites, zero in self.zero_rows:
            self.assertTrue(zero)
            self.assertEqual(p_hits, 0)
            self.assertEqual(p_sites, ())
            self.assertEqual(island_p_hits(tokens, self.hpq_sides), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, tokens, VENDORED_TABLETS)[
                    VENDORED_TABLETS.index("P")
                ],
                0,
            )
            self.assertGreaterEqual(n, 8)
            self.assertEqual(len(tokens), n)
        self.assertEqual(STANDING_ARITHMETIC_15_MINUS_5, STANDING_HYPOTHESIS_N)
        self.assertEqual(STANDING_ARITHMETIC_15_MINUS_5, 10)
        self.assertFalse(STANDING_ARITHMETIC_15_MINUS_5_HOLDS)
        self.assertNotEqual(self.measured_n, STANDING_ARITHMETIC_15_MINUS_5)
        self.assertEqual(self.claim_holds, STANDING_HQ_ISLANDS_ZERO_ON_P_COUNT_HOLDS)
        self.assertTrue(STANDING_HQ_ISLANDS_ZERO_ON_P_COUNT_HOLDS)
        self.assertTrue(hq_islands_zero_on_p_count_holds(self.measured_n))
        self.assertFalse(hq_islands_zero_on_p_count_holds(10))
        self.assertEqual(STANDING_CLAIM, "hq_islands_zero_on_p_count_holds")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n31_from_cycle_109_is_in_the_zero_on_p_set(self):
        """Cycle-109 maximal H∩Q n=31 is one of the twelve exact-0 rows."""
        tokens_31, n_31, h_31, q_31, p_hits_31, p_sites_31, zero_31 = self.rows[0]
        self.assertEqual(tokens_31, STANDING_ISLAND_31_TOKENS)
        self.assertEqual(n_31, STANDING_ISLAND_31_N)
        self.assertEqual(n_31, 31)
        self.assertEqual(h_31, STANDING_ISLAND_31_H_SITE)
        self.assertEqual(q_31, STANDING_ISLAND_31_Q_SITE)
        self.assertEqual(h_31, (SIDE_HR, "Hr3", 39))
        self.assertEqual(q_31, (SIDE_QR, "Qr3", 19))
        self.assertEqual(p_hits_31, 0)
        self.assertEqual(p_sites_31, ())
        self.assertTrue(zero_31)
        self.assertTrue(STANDING_N31_IS_ZERO_ON_P)
        self.assertIn(self.rows[0], self.zero_rows)
        self.assertEqual(STANDING_MAXIMAL_P_HITS, 0)
        self.assertEqual(
            self.survey["hq_7gram_hq_pairwise_island_substring"]["maximal_p_hits"], 0
        )
        for side, line, index in (h_31, q_31):
            stems = self.hpq_sides[side][LINE_NAMES[side].index(line)][index : index + 31]
            self.assertEqual(tuple(stems), STANDING_ISLAND_31_TOKENS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_three_p_hits_are_the_exact_triple_members_of_the_fifteen(self):
        """The three H–Q islands with P hits are exact cycle-71 triples."""
        self.assertEqual(len(LOCKED_TRIPLE_ISLANDS), STANDING_TRIPLE_COUNT)
        self.assertEqual(STANDING_TRIPLE_COUNT, 5)
        exact_triples = tuple(
            tokens for tokens in LOCKED_HQ_ISLANDS if tokens in LOCKED_TRIPLE_ISLANDS
        )
        self.assertEqual(len(exact_triples), STANDING_EXACT_TRIPLE_IN_HQ15)
        self.assertEqual(STANDING_EXACT_TRIPLE_IN_HQ15, 3)
        self.assertEqual(tuple(row[0] for row in self.hit_rows), exact_triples)
        for (tokens, n, h_site, q_site, p_hits, p_sites, zero), expected_sites in zip(
            self.hit_rows, STANDING_HIT_P_SITES, strict=True
        ):
            self.assertFalse(zero)
            self.assertEqual(p_hits, 1)
            self.assertEqual(p_sites, expected_sites)
            self.assertIn(tokens, LOCKED_TRIPLE_ISLANDS)
            self.assertGreaterEqual(n, 8)
            for side, line, index in (h_site, q_site) + p_sites:
                stems = self.hpq_sides[side][LINE_NAMES[side].index(line)][
                    index : index + n
                ]
                self.assertEqual(tuple(stems), tokens)
        self.assertEqual(self.hit_rows[0][1], 12)
        self.assertEqual(self.hit_rows[0][2], (SIDE_HR, "Hr8", 0))
        self.assertEqual(self.hit_rows[0][3], (SIDE_QR, "Qr7", 47))
        self.assertEqual(self.hit_rows[1][1], 11)
        self.assertEqual(self.hit_rows[1][2], (SIDE_HR, "Hr3", 27))
        self.assertEqual(self.hit_rows[1][3], (SIDE_QR, "Qr3", 7))
        self.assertEqual(self.hit_rows[2][1], 8)
        self.assertEqual(self.hit_rows[2][2], (SIDE_HR, "Hr7", 47))
        self.assertEqual(self.hit_rows[2][3], (SIDE_QR, "Qr7", 28))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_five_triple_islands_all_hit_p(self):
        """All five locked H∩P∩Q islands have P hits. None are 0 on P."""
        self.assertEqual(len(self.triple_p_hits), 5)
        self.assertTrue(all(hits >= 1 for hits in self.triple_p_hits))
        self.assertEqual(sum(1 for hits in self.triple_p_hits if hits == 0), 0)
        self.assertTrue(STANDING_TRIPLE_ISLANDS_HIT_ON_P)
        self.assertEqual(STANDING_TRIPLE_ISLANDS_ZERO_ON_P, 0)
        for tokens, n, _fh, _fp, _fq, h_site, p_site, q_site in STANDING_MAXIMALS:
            p_hits = island_p_hits(tokens, self.hpq_sides)
            p_sites = island_p_sites(tokens, self.hpq_sides)
            self.assertGreaterEqual(p_hits, 1)
            self.assertIn(p_site, p_sites)
            self.assertFalse(island_is_zero_on_p(tokens, self.hpq_sides))
            self.assertGreaterEqual(n, 8)
        # Two triples are proper substrings of longer H–Q islands that miss P.
        triple_n10 = STANDING_MAXIMALS[2][0]
        parent_15 = STANDING_QH_MAXIMALS[STANDING_TRIPLE_N10_PARENT_INDEX]
        self.assertEqual(parent_15[1], 15)
        self.assertEqual(substring_offsets(triple_n10, parent_15[0]), STANDING_TRIPLE_N10_PARENT_OFFSETS)
        self.assertFalse(is_contiguous_substring(parent_15[0], triple_n10))
        self.assertTrue(self.rows[STANDING_TRIPLE_N10_PARENT_INDEX][6])
        triple_n8_verso = STANDING_MAXIMALS[4][0]
        parent_14 = STANDING_QH_MAXIMALS[STANDING_TRIPLE_N8_VERSO_PARENT_INDEX]
        self.assertEqual(parent_14[1], 14)
        self.assertEqual(parent_14[5], (SIDE_HV, "Hv2", 26))
        self.assertEqual(parent_14[4], (SIDE_QV, "Qv5", 5))
        self.assertEqual(
            substring_offsets(triple_n8_verso, parent_14[0]),
            STANDING_TRIPLE_N8_VERSO_PARENT_OFFSETS,
        )
        self.assertFalse(is_contiguous_substring(parent_14[0], triple_n8_verso))
        self.assertTrue(self.rows[STANDING_TRIPLE_N8_VERSO_PARENT_INDEX][6])
        self.assertEqual(STANDING_TRIPLE_PROPER_SUBSTRING_OF_HQ, 2)
        proper = 0
        for tokens in LOCKED_TRIPLE_ISLANDS:
            if tokens in LOCKED_HQ_ISLANDS:
                continue
            parents = [
                i
                for i, hq in enumerate(LOCKED_HQ_ISLANDS)
                if is_contiguous_substring(tokens, hq)
            ]
            self.assertTrue(parents)
            self.assertTrue(all(self.rows[i][6] for i in parents))
            proper += 1
        self.assertEqual(proper, STANDING_TRIPLE_PROPER_SUBSTRING_OF_HQ)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_pairwise_triple_and_w_scoreboards_still_compute(self):
        """Cycle 70 H–Q pairwise, cycle 71 triples, cycle 109, and W stay."""
        prior_qh = TestMamariSmallStPetersburgSharedN8Scoreboard()
        prior_qh.setUp()
        prior_qh.test_q_vs_h_inventory_tokens_n_freq_and_hits()
        prior_qh.test_survey_matches_computed_lock()
        prior_triple = TestMamariHpqTripleN8Scoreboard()
        prior_triple.setUp()
        prior_triple.test_inventory_tokens_n_freq_and_hits()
        prior_triple.test_survey_matches_computed_lock()
        prior_109 = TestMamariHq7gramHqPairwiseIslandSubstringScoreboard()
        prior_109.setUp()
        prior_109.test_maximal_hq_extension_is_n31_and_p_is_zero()
        prior_109.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-110 zero-on-P count."""
        lock = self.survey["hq_islands_zero_on_p"]
        self.assertEqual(lock["cycle"], 110)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["island_count"], STANDING_QH_MAXIMAL_COUNT)
        self.assertEqual(lock["island_count"], 15)
        self.assertEqual(lock["hq_islands_zero_on_p"], STANDING_HQ_ISLANDS_ZERO_ON_P)
        self.assertEqual(lock["hq_islands_zero_on_p"], 12)
        self.assertEqual(lock["hq_islands_hit_on_p"], STANDING_HQ_ISLANDS_HIT_ON_P)
        self.assertEqual(lock["from_cycle"], 70)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["hq_islands_zero_on_p_count_holds"])
        self.assertEqual(
            lock["hq_islands_zero_on_p_count_holds"],
            STANDING_HQ_ISLANDS_ZERO_ON_P_COUNT_HOLDS,
        )
        self.assertEqual(lock["arithmetic_15_minus_5"], STANDING_ARITHMETIC_15_MINUS_5)
        self.assertFalse(lock["arithmetic_15_minus_5_holds"])
        self.assertEqual(
            lock["arithmetic_15_minus_5_holds"], STANDING_ARITHMETIC_15_MINUS_5_HOLDS
        )
        self.assertTrue(lock["n31_is_zero_on_p"])
        self.assertEqual(lock["n31_is_zero_on_p"], STANDING_N31_IS_ZERO_ON_P)
        self.assertEqual(tuple(lock["zero_on_p_ns"]), STANDING_ZERO_ON_P_NS)
        self.assertEqual(tuple(lock["hit_on_p_ns"]), STANDING_HIT_ON_P_NS)
        self.assertEqual(tuple(lock["zero_on_p_indices"]), STANDING_ZERO_ON_P_INDICES)
        self.assertEqual(tuple(lock["hit_on_p_indices"]), STANDING_HIT_ON_P_INDICES)
        self.assertEqual(len(lock["islands"]), 15)
        for computed, recorded in zip(self.rows, lock["islands"], strict=True):
            tokens, n, h_site, q_site, p_hits, p_sites, zero = computed
            self.assertEqual(tuple(recorded["tokens"]), tokens)
            self.assertEqual(recorded["n"], n)
            self.assertEqual(tuple(recorded["h_site"]), h_site)
            self.assertEqual(tuple(recorded["q_site"]), q_site)
            self.assertEqual(recorded["p_hits"], p_hits)
            self.assertEqual(tuple(tuple(site) for site in recorded["p_sites"]), p_sites)
            self.assertEqual(recorded["zero_on_p"], zero)
            self.assertEqual(recorded["exact_triple"], tokens in LOCKED_TRIPLE_ISLANDS)
        n31 = lock["islands"][0]
        self.assertEqual(tuple(n31["tokens"]), STANDING_ISLAND_31_TOKENS)
        self.assertEqual(n31["n"], 31)
        self.assertTrue(n31["zero_on_p"])
        self.assertEqual(n31["p_hits"], 0)
        self.assertEqual(lock["triple_island_count"], STANDING_TRIPLE_COUNT)
        self.assertTrue(lock["triple_islands_hit_on_p"])
        self.assertEqual(lock["triple_islands_zero_on_p"], 0)
        self.assertEqual(lock["exact_triple_in_hq15"], STANDING_EXACT_TRIPLE_IN_HQ15)
        self.assertEqual(
            lock["triple_proper_substring_of_hq"], STANDING_TRIPLE_PROPER_SUBSTRING_OF_HQ
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
            self.assertGreaterEqual(recorded["p_hits"], 1)
            self.assertFalse(recorded["zero_on_p"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_q_shared_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hq_7gram_hq_pairwise_island_substring_unchanged"])
        self.assertTrue(lock["standing_hq_max_n_hpq_island_substring_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_q_shared_n8_inventory"]["cycle"], 70)
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertEqual(
            self.survey["tablet_h_p_q_triple_n8_inventory"]["maximal_count"], 5
        )
        self.assertEqual(self.survey["hq_7gram_hq_pairwise_island_substring"]["cycle"], 109)
        self.assertTrue(
            self.survey["hq_7gram_hq_pairwise_island_substring"][
                "hq_7gram_is_hq_pairwise_island_substring"
            ]
        )
        self.assertEqual(self.survey["hq_max_n_hpq_island_substring"]["cycle"], 108)
        self.assertFalse(
            self.survey["hq_max_n_hpq_island_substring"]["hq_max_n_is_hpq_island_substring"]
        )
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHqIslandsZeroOnPImageSnapshot(unittest.TestCase):
    """Cycle 110 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
