"""Q–P pairwise n≥8 islands that are exact-0 on H.

Cycle 112 text-search lock. Uses already-vendored A–V and the
cycle-70 eight maximal Q–P pairwise islands. Does not vendor a
new tablet. Does not scrape X. W has no Barthel (cycle 100); skip
W. Does not redo Q–P pairwise n≥8 or H∩P∩Q triple inventories.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Locks exact contiguous H hit counts of those 8 locked Q∩P
sequences (same Barthel parser as the cycle-110 H–Q vs P and
cycle-111 H–P vs Q locks) and how many are exact-0 on H.
Arithmetic 8−5=3 is a hypothesis, not a lock: four cycle-71
triples are proper substrings of longer Q–P islands that
themselves miss H. Claim that can lose:
qp_islands_zero_on_h_count_holds (measured N equals the locked
count).

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
from tests.test_mamari_hp_islands_zero_on_q_scoreboard import (
    TestMamariHpIslandsZeroOnQScoreboard,
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
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
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
    STANDING_QP_MAXIMAL_COUNT,
    STANDING_QP_MAXIMALS,
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

LOCKED_QP_ISLANDS = tuple(
    tokens for tokens, _n, _fq, _fp, _qs, _ps in STANDING_QP_MAXIMALS
)
LOCKED_TRIPLE_ISLANDS = tuple(
    tokens for tokens, _n, _fh, _fp, _fq, _h, _p, _q in STANDING_MAXIMALS
)
STANDING_ZERO_ON_H_INDICES = (0, 1, 2, 3, 4, 5, 6)
STANDING_HIT_ON_H_INDICES = (7,)
STANDING_ZERO_ON_H_NS = (17, 15, 13, 12, 11, 10, 9)
STANDING_HIT_ON_H_NS = (8,)
STANDING_HIT_H_SITES = (
    ((SIDE_HR, "Hr7", 47),),
)
STANDING_QP_ISLANDS_ZERO_ON_H = 7
STANDING_QP_ISLANDS_HIT_ON_H = 1
STANDING_QP_ISLANDS_ZERO_ON_H_COUNT_HOLDS = True
STANDING_ARITHMETIC_8_MINUS_5 = 3
STANDING_ARITHMETIC_8_MINUS_5_HOLDS = False
STANDING_N17_IS_ZERO_ON_H = True
STANDING_TRIPLE_ISLANDS_HIT_ON_H = True
STANDING_TRIPLE_ISLANDS_ZERO_ON_H = 0
STANDING_EXACT_TRIPLE_IN_QP8 = 1
STANDING_TRIPLE_PROPER_SUBSTRING_OF_QP = 4
STANDING_TRIPLE_N12_PARENT_INDEX = 2
STANDING_TRIPLE_N12_PARENT_OFFSETS = (1,)
STANDING_TRIPLE_N11_PARENT_INDEX = 1
STANDING_TRIPLE_N11_PARENT_OFFSETS = (0,)
STANDING_TRIPLE_N10_PARENT_INDEX = 4
STANDING_TRIPLE_N10_PARENT_OFFSETS = (0,)
STANDING_TRIPLE_N8_VERSO_PARENT_INDEX = 3
STANDING_TRIPLE_N8_VERSO_PARENT_OFFSETS = (0,)
STANDING_CLAIM = "qp_islands_zero_on_h_count_holds"
STANDING_RESULT = "qp_islands_zero_on_h"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_HYPOTHESIS_N = 3


def island_h_sites(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Exact contiguous H sites of one locked Q–P island sequence."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    return named_qhp_hits(by_side, H_SIDES, tokens)


def island_h_hits(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> int:
    """Exact contiguous H hit count. Search only."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    return ngram_hit_count(concat_sides(by_side, H_SIDES), tokens)


def island_is_zero_on_h(
    tokens: tuple[str, ...],
    by_side: dict[str, list[list[str]]] | None = None,
) -> bool:
    """True iff the island sequence is exact-0 on H."""
    return island_h_hits(tokens, by_side) == 0


def classify_qp_islands(
    maximals: tuple = STANDING_QP_MAXIMALS,
    by_side: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple, ...]:
    """(tokens, n, q_site, p_site, h_hits, h_sites, zero_on_h) per island."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    rows = []
    for tokens, n, _fq, _fp, q_site, p_site in maximals:
        h_sites = island_h_sites(tokens, by_side)
        h_hits = len(h_sites)
        rows.append((tokens, n, q_site, p_site, h_hits, h_sites, h_hits == 0))
    return tuple(rows)


def zero_on_h_count(
    maximals: tuple = STANDING_QP_MAXIMALS,
    by_side: dict[str, list[list[str]]] | None = None,
) -> int:
    """How many locked Q–P islands are exact-0 on H."""
    return sum(1 for *_rest, zero in classify_qp_islands(maximals, by_side) if zero)


def qp_islands_zero_on_h_count_holds(
    measured: int,
    locked: int = STANDING_QP_ISLANDS_ZERO_ON_H,
) -> bool:
    """True iff measured N equals the locked count. The claim that can lose."""
    return measured == locked


class TestQpIslandsZeroOnHHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_contiguous_h_hits_classify_zero_versus_hit(self):
        """A planted H run counts; a gap or a miss is exact-0."""
        provider = MockProvider()
        planted = ("111", "222", "333", "444", "555", "666", "777", "888")
        miss = ("000", "000", "000", "000", "000", "000", "000", "000")
        self.assertEqual(ngram_hit_count([list(planted)], planted), 1)
        self.assertEqual(ngram_hit_count([list(planted[:4]) + ["999"] + list(planted[4:])], planted), 0)
        self.assertEqual(ngram_hit_count([[]], planted), 0)
        by_side = load_h_p_q_sides()
        by_side[SIDE_HR] = [list(planted)]
        by_side[SIDE_HV] = [[]]
        planted_row = (planted, 8, 1, 1, (SIDE_QR, "Qr1", 0), (SIDE_PR, "Pr1", 0))
        miss_row = (miss, 8, 1, 1, (SIDE_QR, "Qr1", 1), (SIDE_PR, "Pr1", 1))
        self.assertEqual(island_h_hits(planted, by_side), 1)
        self.assertEqual(island_h_sites(planted, by_side), ((SIDE_HR, LINE_NAMES[SIDE_HR][0], 0),))
        self.assertFalse(island_is_zero_on_h(planted, by_side))
        self.assertEqual(island_h_hits(miss, by_side), 0)
        self.assertEqual(island_h_sites(miss, by_side), ())
        self.assertTrue(island_is_zero_on_h(miss, by_side))
        classified = classify_qp_islands((planted_row, miss_row), by_side)
        self.assertEqual(classified[0][4], 1)
        self.assertFalse(classified[0][6])
        self.assertEqual(classified[1][4], 0)
        self.assertTrue(classified[1][6])
        self.assertEqual(zero_on_h_count((planted_row, miss_row), by_side), 1)
        self.assertTrue(qp_islands_zero_on_h_count_holds(7, 7))
        self.assertFalse(qp_islands_zero_on_h_count_holds(3, 7))
        self.assertEqual(STANDING_CLAIM, "qp_islands_zero_on_h_count_holds")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariQpIslandsZeroOnHScoreboard(unittest.TestCase):
    """Cited-fixture Q–P islands vs exact H hits. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.hpq_sides = load_h_p_q_sides()
        self.rows = classify_qp_islands(STANDING_QP_MAXIMALS, self.hpq_sides)
        self.measured_n = zero_on_h_count(STANDING_QP_MAXIMALS, self.hpq_sides)
        self.claim_holds = qp_islands_zero_on_h_count_holds(self.measured_n)
        self.zero_rows = tuple(row for row in self.rows if row[6])
        self.hit_rows = tuple(row for row in self.rows if not row[6])
        self.triple_h_hits = tuple(
            island_h_hits(tokens, self.hpq_sides) for tokens in LOCKED_TRIPLE_ISLANDS
        )

    def test_islands_are_the_locked_cycle_70_qp_maximals(self):
        """Eight sequences come from cycle 70. None invented."""
        self.assertEqual(len(LOCKED_QP_ISLANDS), STANDING_QP_MAXIMAL_COUNT)
        self.assertEqual(STANDING_QP_MAXIMAL_COUNT, 8)
        self.assertEqual(len(STANDING_QP_MAXIMALS), 8)
        self.assertEqual(LOCKED_QP_ISLANDS, tuple(row[0] for row in STANDING_QP_MAXIMALS))
        self.assertEqual(STANDING_QP_MAXIMALS[0][1], 17)
        self.assertEqual(STANDING_QP_MAXIMALS[0][4], (SIDE_QV, "Qv4", 12))
        self.assertEqual(STANDING_QP_MAXIMALS[0][5], (SIDE_PV, "Pv3", 30))
        self.assertEqual(
            self.survey["tablet_q_shared_n8_inventory"]["q_vs_p"]["maximal_count"], 8
        )
        self.assertEqual(
            self.survey["tablet_q_shared_n8_inventory"]["q_vs_p"]["maximals"][0][1], 17
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_seven_of_eight_are_exact_zero_on_h(self):
        """Measured N is 7. Arithmetic 8−5=3 does not hold."""
        self.assertEqual(len(self.rows), 8)
        self.assertEqual(self.measured_n, STANDING_QP_ISLANDS_ZERO_ON_H)
        self.assertEqual(STANDING_QP_ISLANDS_ZERO_ON_H, 7)
        self.assertEqual(len(self.zero_rows), 7)
        self.assertEqual(len(self.hit_rows), STANDING_QP_ISLANDS_HIT_ON_H)
        self.assertEqual(STANDING_QP_ISLANDS_HIT_ON_H, 1)
        self.assertEqual(self.measured_n + len(self.hit_rows), 8)
        self.assertEqual(
            tuple(i for i, row in enumerate(self.rows) if row[6]),
            STANDING_ZERO_ON_H_INDICES,
        )
        self.assertEqual(
            tuple(i for i, row in enumerate(self.rows) if not row[6]),
            STANDING_HIT_ON_H_INDICES,
        )
        self.assertEqual(tuple(row[1] for row in self.zero_rows), STANDING_ZERO_ON_H_NS)
        self.assertEqual(tuple(row[1] for row in self.hit_rows), STANDING_HIT_ON_H_NS)
        for tokens, n, q_site, p_site, h_hits, h_sites, zero in self.zero_rows:
            self.assertTrue(zero)
            self.assertEqual(h_hits, 0)
            self.assertEqual(h_sites, ())
            self.assertEqual(island_h_hits(tokens, self.hpq_sides), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, tokens, VENDORED_TABLETS)[
                    VENDORED_TABLETS.index("H")
                ],
                0,
            )
            self.assertGreaterEqual(n, 8)
            self.assertEqual(len(tokens), n)
        self.assertEqual(STANDING_ARITHMETIC_8_MINUS_5, STANDING_HYPOTHESIS_N)
        self.assertEqual(STANDING_ARITHMETIC_8_MINUS_5, 3)
        self.assertFalse(STANDING_ARITHMETIC_8_MINUS_5_HOLDS)
        self.assertNotEqual(self.measured_n, STANDING_ARITHMETIC_8_MINUS_5)
        self.assertEqual(self.claim_holds, STANDING_QP_ISLANDS_ZERO_ON_H_COUNT_HOLDS)
        self.assertTrue(STANDING_QP_ISLANDS_ZERO_ON_H_COUNT_HOLDS)
        self.assertTrue(qp_islands_zero_on_h_count_holds(self.measured_n))
        self.assertFalse(qp_islands_zero_on_h_count_holds(3))
        self.assertEqual(STANDING_CLAIM, "qp_islands_zero_on_h_count_holds")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n17_from_cycle_70_is_in_the_zero_on_h_set(self):
        """Cycle-70 maximal Q∩P n=17 is one of the seven exact-0 rows."""
        tokens_17, n_17, q_17, p_17, h_hits_17, h_sites_17, zero_17 = self.rows[0]
        self.assertEqual(tokens_17, STANDING_QP_MAXIMALS[0][0])
        self.assertEqual(n_17, 17)
        self.assertEqual(q_17, STANDING_QP_MAXIMALS[0][4])
        self.assertEqual(p_17, STANDING_QP_MAXIMALS[0][5])
        self.assertEqual(q_17, (SIDE_QV, "Qv4", 12))
        self.assertEqual(p_17, (SIDE_PV, "Pv3", 30))
        self.assertEqual(h_hits_17, 0)
        self.assertEqual(h_sites_17, ())
        self.assertTrue(zero_17)
        self.assertTrue(STANDING_N17_IS_ZERO_ON_H)
        self.assertIn(self.rows[0], self.zero_rows)
        self.assertEqual(
            self.survey["tablet_q_shared_n8_inventory"]["q_vs_p"]["maximals"][0][1], 17
        )
        for side, line, index in (q_17, p_17):
            stems = self.hpq_sides[side][LINE_NAMES[side].index(line)][index : index + 17]
            self.assertEqual(tuple(stems), STANDING_QP_MAXIMALS[0][0])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_one_h_hit_is_the_exact_triple_member_of_the_eight(self):
        """The one Q–P island with an H hit is the exact cycle-71 n=8 triple."""
        self.assertEqual(len(LOCKED_TRIPLE_ISLANDS), STANDING_TRIPLE_COUNT)
        self.assertEqual(STANDING_TRIPLE_COUNT, 5)
        exact_triples = tuple(
            tokens for tokens in LOCKED_QP_ISLANDS if tokens in LOCKED_TRIPLE_ISLANDS
        )
        self.assertEqual(len(exact_triples), STANDING_EXACT_TRIPLE_IN_QP8)
        self.assertEqual(STANDING_EXACT_TRIPLE_IN_QP8, 1)
        self.assertEqual(tuple(row[0] for row in self.hit_rows), exact_triples)
        for (tokens, n, q_site, p_site, h_hits, h_sites, zero), expected_sites in zip(
            self.hit_rows, STANDING_HIT_H_SITES, strict=True
        ):
            self.assertFalse(zero)
            self.assertEqual(h_hits, 1)
            self.assertEqual(h_sites, expected_sites)
            self.assertIn(tokens, LOCKED_TRIPLE_ISLANDS)
            self.assertGreaterEqual(n, 8)
            for side, line, index in (q_site, p_site) + h_sites:
                stems = self.hpq_sides[side][LINE_NAMES[side].index(line)][
                    index : index + n
                ]
                self.assertEqual(tuple(stems), tokens)
        self.assertEqual(self.hit_rows[0][1], 8)
        self.assertEqual(self.hit_rows[0][2], (SIDE_QR, "Qr7", 28))
        self.assertEqual(self.hit_rows[0][3], (SIDE_PR, "Pr7", 10))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_five_triple_islands_all_hit_h(self):
        """All five locked H∩P∩Q islands have H hits. None are 0 on H."""
        self.assertEqual(len(self.triple_h_hits), 5)
        self.assertTrue(all(hits >= 1 for hits in self.triple_h_hits))
        self.assertEqual(sum(1 for hits in self.triple_h_hits if hits == 0), 0)
        self.assertTrue(STANDING_TRIPLE_ISLANDS_HIT_ON_H)
        self.assertEqual(STANDING_TRIPLE_ISLANDS_ZERO_ON_H, 0)
        for tokens, n, _fh, _fp, _fq, h_site, p_site, q_site in STANDING_MAXIMALS:
            h_hits = island_h_hits(tokens, self.hpq_sides)
            h_sites = island_h_sites(tokens, self.hpq_sides)
            self.assertGreaterEqual(h_hits, 1)
            self.assertIn(h_site, h_sites)
            self.assertFalse(island_is_zero_on_h(tokens, self.hpq_sides))
            self.assertGreaterEqual(n, 8)
        # Four triples are proper substrings of longer Q–P islands that miss H.
        triple_n12 = STANDING_MAXIMALS[0][0]
        parent_13 = STANDING_QP_MAXIMALS[STANDING_TRIPLE_N12_PARENT_INDEX]
        self.assertEqual(parent_13[1], 13)
        self.assertEqual(parent_13[4], (SIDE_QR, "Qr7", 46))
        self.assertEqual(parent_13[5], (SIDE_PR, "Pr7", 28))
        self.assertEqual(
            substring_offsets(triple_n12, parent_13[0]),
            STANDING_TRIPLE_N12_PARENT_OFFSETS,
        )
        self.assertFalse(is_contiguous_substring(parent_13[0], triple_n12))
        self.assertTrue(self.rows[STANDING_TRIPLE_N12_PARENT_INDEX][6])
        triple_n11 = STANDING_MAXIMALS[1][0]
        parent_15 = STANDING_QP_MAXIMALS[STANDING_TRIPLE_N11_PARENT_INDEX]
        self.assertEqual(parent_15[1], 15)
        self.assertEqual(parent_15[4], (SIDE_QR, "Qr3", 7))
        self.assertEqual(parent_15[5], (SIDE_PR, "Pr3", 14))
        self.assertEqual(
            substring_offsets(triple_n11, parent_15[0]),
            STANDING_TRIPLE_N11_PARENT_OFFSETS,
        )
        self.assertFalse(is_contiguous_substring(parent_15[0], triple_n11))
        self.assertTrue(self.rows[STANDING_TRIPLE_N11_PARENT_INDEX][6])
        triple_n10 = STANDING_MAXIMALS[2][0]
        parent_11 = STANDING_QP_MAXIMALS[STANDING_TRIPLE_N10_PARENT_INDEX]
        self.assertEqual(parent_11[1], 11)
        self.assertEqual(parent_11[4], (SIDE_QR, "Qr5", 15))
        self.assertEqual(parent_11[5], (SIDE_PR, "Pr5", 9))
        self.assertEqual(
            substring_offsets(triple_n10, parent_11[0]),
            STANDING_TRIPLE_N10_PARENT_OFFSETS,
        )
        self.assertFalse(is_contiguous_substring(parent_11[0], triple_n10))
        self.assertTrue(self.rows[STANDING_TRIPLE_N10_PARENT_INDEX][6])
        triple_n8_verso = STANDING_MAXIMALS[4][0]
        parent_12 = STANDING_QP_MAXIMALS[STANDING_TRIPLE_N8_VERSO_PARENT_INDEX]
        self.assertEqual(parent_12[1], 12)
        self.assertEqual(parent_12[4], (SIDE_QV, "Qv5", 11))
        self.assertEqual(parent_12[5], (SIDE_PV, "Pv4", 50))
        self.assertEqual(
            substring_offsets(triple_n8_verso, parent_12[0]),
            STANDING_TRIPLE_N8_VERSO_PARENT_OFFSETS,
        )
        self.assertFalse(is_contiguous_substring(parent_12[0], triple_n8_verso))
        self.assertTrue(self.rows[STANDING_TRIPLE_N8_VERSO_PARENT_INDEX][6])
        self.assertEqual(STANDING_TRIPLE_PROPER_SUBSTRING_OF_QP, 4)
        proper = 0
        for tokens in LOCKED_TRIPLE_ISLANDS:
            if tokens in LOCKED_QP_ISLANDS:
                continue
            parents = [
                i
                for i, qp in enumerate(LOCKED_QP_ISLANDS)
                if is_contiguous_substring(tokens, qp)
            ]
            self.assertTrue(parents)
            self.assertTrue(all(self.rows[i][6] for i in parents))
            proper += 1
        self.assertEqual(proper, STANDING_TRIPLE_PROPER_SUBSTRING_OF_QP)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_pairwise_triple_and_w_scoreboards_still_compute(self):
        """Cycle 70 Q–P pairwise, cycle 71 triples, cycles 110–111, and W stay."""
        prior_qp = TestMamariSmallStPetersburgSharedN8Scoreboard()
        prior_qp.setUp()
        prior_qp.test_q_vs_p_inventory_tokens_n_freq_and_hits()
        prior_qp.test_survey_matches_computed_lock()
        prior_triple = TestMamariHpqTripleN8Scoreboard()
        prior_triple.setUp()
        prior_triple.test_inventory_tokens_n_freq_and_hits()
        prior_triple.test_survey_matches_computed_lock()
        prior_110 = TestMamariHqIslandsZeroOnPScoreboard()
        prior_110.setUp()
        prior_110.test_twelve_of_fifteen_are_exact_zero_on_p()
        prior_110.test_survey_matches_computed_lock()
        prior_111 = TestMamariHpIslandsZeroOnQScoreboard()
        prior_111.setUp()
        prior_111.test_fifteen_of_eighteen_are_exact_zero_on_q()
        prior_111.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-112 zero-on-H count."""
        lock = self.survey["qp_islands_zero_on_h"]
        self.assertEqual(lock["cycle"], 112)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["island_count"], STANDING_QP_MAXIMAL_COUNT)
        self.assertEqual(lock["island_count"], 8)
        self.assertEqual(lock["qp_islands_zero_on_h"], STANDING_QP_ISLANDS_ZERO_ON_H)
        self.assertEqual(lock["qp_islands_zero_on_h"], 7)
        self.assertEqual(lock["qp_islands_hit_on_h"], STANDING_QP_ISLANDS_HIT_ON_H)
        self.assertEqual(lock["from_cycle"], 70)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["qp_islands_zero_on_h_count_holds"])
        self.assertEqual(
            lock["qp_islands_zero_on_h_count_holds"],
            STANDING_QP_ISLANDS_ZERO_ON_H_COUNT_HOLDS,
        )
        self.assertEqual(lock["arithmetic_8_minus_5"], STANDING_ARITHMETIC_8_MINUS_5)
        self.assertFalse(lock["arithmetic_8_minus_5_holds"])
        self.assertEqual(
            lock["arithmetic_8_minus_5_holds"], STANDING_ARITHMETIC_8_MINUS_5_HOLDS
        )
        self.assertTrue(lock["n17_is_zero_on_h"])
        self.assertEqual(lock["n17_is_zero_on_h"], STANDING_N17_IS_ZERO_ON_H)
        self.assertEqual(tuple(lock["zero_on_h_ns"]), STANDING_ZERO_ON_H_NS)
        self.assertEqual(tuple(lock["hit_on_h_ns"]), STANDING_HIT_ON_H_NS)
        self.assertEqual(tuple(lock["zero_on_h_indices"]), STANDING_ZERO_ON_H_INDICES)
        self.assertEqual(tuple(lock["hit_on_h_indices"]), STANDING_HIT_ON_H_INDICES)
        self.assertEqual(len(lock["islands"]), 8)
        for computed, recorded in zip(self.rows, lock["islands"], strict=True):
            tokens, n, q_site, p_site, h_hits, h_sites, zero = computed
            self.assertEqual(tuple(recorded["tokens"]), tokens)
            self.assertEqual(recorded["n"], n)
            self.assertEqual(tuple(recorded["q_site"]), q_site)
            self.assertEqual(tuple(recorded["p_site"]), p_site)
            self.assertEqual(recorded["h_hits"], h_hits)
            self.assertEqual(tuple(tuple(site) for site in recorded["h_sites"]), h_sites)
            self.assertEqual(recorded["zero_on_h"], zero)
            self.assertEqual(recorded["exact_triple"], tokens in LOCKED_TRIPLE_ISLANDS)
        n17 = lock["islands"][0]
        self.assertEqual(tuple(n17["tokens"]), STANDING_QP_MAXIMALS[0][0])
        self.assertEqual(n17["n"], 17)
        self.assertTrue(n17["zero_on_h"])
        self.assertEqual(n17["h_hits"], 0)
        self.assertEqual(lock["triple_island_count"], STANDING_TRIPLE_COUNT)
        self.assertTrue(lock["triple_islands_hit_on_h"])
        self.assertEqual(lock["triple_islands_zero_on_h"], 0)
        self.assertEqual(lock["exact_triple_in_qp8"], STANDING_EXACT_TRIPLE_IN_QP8)
        self.assertEqual(
            lock["triple_proper_substring_of_qp"], STANDING_TRIPLE_PROPER_SUBSTRING_OF_QP
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
            self.assertGreaterEqual(recorded["h_hits"], 1)
            self.assertFalse(recorded["zero_on_h"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_q_shared_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hq_islands_zero_on_p_unchanged"])
        self.assertTrue(lock["standing_hp_islands_zero_on_q_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_q_shared_n8_inventory"]["cycle"], 70)
        self.assertEqual(
            self.survey["tablet_q_shared_n8_inventory"]["q_vs_p"]["maximal_count"], 8
        )
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertEqual(
            self.survey["tablet_h_p_q_triple_n8_inventory"]["maximal_count"], 5
        )
        self.assertEqual(self.survey["hq_islands_zero_on_p"]["cycle"], 110)
        self.assertEqual(self.survey["hq_islands_zero_on_p"]["hq_islands_zero_on_p"], 12)
        self.assertFalse(self.survey["hq_islands_zero_on_p"]["arithmetic_15_minus_5_holds"])
        self.assertEqual(self.survey["hp_islands_zero_on_q"]["cycle"], 111)
        self.assertEqual(self.survey["hp_islands_zero_on_q"]["hp_islands_zero_on_q"], 15)
        self.assertFalse(self.survey["hp_islands_zero_on_q"]["arithmetic_18_minus_5_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariQpIslandsZeroOnHImageSnapshot(unittest.TestCase):
    """Cycle 112 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
