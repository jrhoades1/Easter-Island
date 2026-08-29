"""G–K n≥8 maximal islands that are exact-0 on B.

Cycle 113 text-search lock. Uses already-vendored A–V and the
cycle-67 six maximal G–K islands. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W. Does
not redo G–K n≥8 inventories and does not retune those islands.
Does not redo H/P/Q pairwise third-tablet counts (cycles
110–112). Raw stems. No invented Barthel. No G00n→Barthel map.
No type merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Locks exact contiguous B hit counts of those 6 locked G∩K
sequences (same Barthel parser as the cycle-105/106 B sites)
and how many are exact-0 on B. Hypothesis N=6 (only the
cycle-105 4-gram / cycle-106 doubled 8-gram suffix leaks, not
any full island) is measured, not assumed. Claim that can lose:
gk_islands_zero_on_b_count_holds (measured N equals the locked
count). Restates that the n=12 island is in the zero set
(cycle 106) and that the doubled 8-gram is a suffix, not one
of the six maximals.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_br_scoreboard import BR_LINE_NAMES
from tests.test_mamari_aruku_bv_scoreboard import BV_LINE_NAMES
from tests.test_mamari_b_gk_doubled_8gram_scoreboard import (
    GRAM8,
    STANDING_B_HITS as CYCLE_106_B_HITS,
    STANDING_B_SITES as CYCLE_106_B_SITES,
    STANDING_ISLAND12_B_HITS,
    TestMamariBGkDoubled8GramScoreboard,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    GRAM4,
    TestMamariKMaxNGkIslandSubstringScoreboard,
    is_contiguous_substring,
    load_b_sides,
    substring_offsets,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_london_kr_scoreboard import KR_LINE_NAMES
from tests.test_mamari_small_london_kv_scoreboard import KV_LINE_NAMES
from tests.test_mamari_small_santiago_gr_scoreboard import GR_LINE_NAMES
from tests.test_mamari_small_santiago_gv_scoreboard import GV_LINE_NAMES
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import GRAM_17
from tests.test_mamari_small_santiago_london_gr_kv_15gram_scoreboard import GRAM_15
from tests.test_mamari_small_santiago_london_island_off_gk_scoreboard import (
    TestMamariSmallSantiagoLondonIslandOffGkScoreboard,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    SIDE_KR,
    SIDE_KV,
    load_g_k_sides,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    GRAM_10_KR,
    GRAM_10_KV,
    GRAM_12,
    GRAM_13,
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    TestMamariSmallSantiagoLondonSharedN8Scoreboard,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

SIDE_BR = "Br"
SIDE_BV = "Bv"
LOCKED_GK_ISLANDS = tuple(tokens for tokens, _n, _fg, _fk, _gs, _ks in STANDING_MAXIMALS)
STANDING_ZERO_ON_B_INDICES = (0, 1, 2, 3, 4, 5)
STANDING_HIT_ON_B_INDICES = ()
STANDING_ZERO_ON_B_NS = (17, 15, 13, 12, 10, 10)
STANDING_HIT_ON_B_NS = ()
STANDING_GK_ISLANDS_ZERO_ON_B = 6
STANDING_GK_ISLANDS_HIT_ON_B = 0
STANDING_GK_ISLANDS_ZERO_ON_B_COUNT_HOLDS = True
STANDING_N12_INDEX = 3
STANDING_N12_IS_ZERO_ON_B = True
STANDING_DOUBLED_8GRAM_IS_MAXIMAL = False
STANDING_DOUBLED_8GRAM_IS_N12_SUFFIX = True
STANDING_DOUBLED_8GRAM_B_HITS = 1
STANDING_CLAIM = "gk_islands_zero_on_b_count_holds"
STANDING_RESULT = "gk_islands_zero_on_b"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_HYPOTHESIS_N = 6
STANDING_HYPOTHESIS_N_HOLDS = True
LINE_NAMES = {
    SIDE_BR: BR_LINE_NAMES,
    SIDE_BV: BV_LINE_NAMES,
    SIDE_GR: GR_LINE_NAMES,
    SIDE_GV: GV_LINE_NAMES,
    SIDE_KR: KR_LINE_NAMES,
    SIDE_KV: KV_LINE_NAMES,
}


def island_b_sites(
    tokens: tuple[str, ...],
    b_sides: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Exact contiguous B sites of one locked G–K island sequence."""
    if b_sides is None:
        b_sides = load_b_sides()
    return tuple(
        site_tuple(hit)
        for hit in named_side_hits(b_sides[SIDE_BR], BR_LINE_NAMES, SIDE_BR, tokens)
        + named_side_hits(b_sides[SIDE_BV], BV_LINE_NAMES, SIDE_BV, tokens)
    )


def island_b_hits(
    tokens: tuple[str, ...],
    b_sides: dict[str, list[list[str]]] | None = None,
) -> int:
    """Exact contiguous B hit count. Search only."""
    return len(island_b_sites(tokens, b_sides))


def island_is_zero_on_b(
    tokens: tuple[str, ...],
    b_sides: dict[str, list[list[str]]] | None = None,
) -> bool:
    """True iff the island sequence is exact-0 on B."""
    return island_b_hits(tokens, b_sides) == 0


def classify_gk_islands(
    maximals: tuple = STANDING_MAXIMALS,
    b_sides: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple, ...]:
    """(tokens, n, g_site, k_site, b_hits, b_sites, zero_on_b) per island."""
    if b_sides is None:
        b_sides = load_b_sides()
    rows = []
    for tokens, n, _fg, _fk, g_site, k_site in maximals:
        b_sites = island_b_sites(tokens, b_sides)
        b_hits = len(b_sites)
        rows.append((tokens, n, g_site, k_site, b_hits, b_sites, b_hits == 0))
    return tuple(rows)


def zero_on_b_count(
    maximals: tuple = STANDING_MAXIMALS,
    b_sides: dict[str, list[list[str]]] | None = None,
) -> int:
    """How many locked G–K islands are exact-0 on B."""
    return sum(1 for *_rest, zero in classify_gk_islands(maximals, b_sides) if zero)


def gk_islands_zero_on_b_count_holds(
    measured: int,
    locked: int = STANDING_GK_ISLANDS_ZERO_ON_B,
) -> bool:
    """True iff measured N equals the locked count. The claim that can lose."""
    return measured == locked


def doubled_8gram_is_maximal(
    gram8: tuple[str, ...] = GRAM8,
    maximals: tuple = STANDING_MAXIMALS,
) -> bool:
    """True iff the cycle-106 doubled 8-gram is itself a locked maximal."""
    return gram8 in tuple(tokens for tokens, *_rest in maximals)


def doubled_8gram_is_n12_suffix(
    gram8: tuple[str, ...] = GRAM8,
    island12: tuple[str, ...] = GRAM_12,
) -> bool:
    """True iff the 8-gram is exactly the n=12 island's trailing eight stems."""
    return gram8 == island12[-8:] and len(gram8) == 8


class TestGkIslandsZeroOnBHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_contiguous_b_hits_classify_zero_versus_hit(self):
        """A planted B run counts; a gap or a miss is exact-0."""
        provider = MockProvider()
        planted = ("111", "222", "333", "444", "555", "666", "777", "888")
        miss = ("000", "000", "000", "000", "000", "000", "000", "000")
        self.assertEqual(ngram_hit_count([list(planted)], planted), 1)
        self.assertEqual(
            ngram_hit_count([list(planted[:4]) + ["999"] + list(planted[4:])], planted),
            0,
        )
        self.assertEqual(ngram_hit_count([[]], planted), 0)
        b_sides = load_b_sides()
        b_sides[SIDE_BR] = [list(planted)]
        b_sides[SIDE_BV] = [[]]
        planted_row = (planted, 8, 1, 1, (SIDE_GR, "Gr1", 0), (SIDE_KR, "Kr1", 0))
        miss_row = (miss, 8, 1, 1, (SIDE_GR, "Gr1", 1), (SIDE_KR, "Kr1", 1))
        self.assertEqual(island_b_hits(planted, b_sides), 1)
        self.assertEqual(
            island_b_sites(planted, b_sides),
            ((SIDE_BR, BR_LINE_NAMES[0], 0),),
        )
        self.assertFalse(island_is_zero_on_b(planted, b_sides))
        self.assertEqual(island_b_hits(miss, b_sides), 0)
        self.assertEqual(island_b_sites(miss, b_sides), ())
        self.assertTrue(island_is_zero_on_b(miss, b_sides))
        classified = classify_gk_islands((planted_row, miss_row), b_sides)
        self.assertEqual(classified[0][4], 1)
        self.assertFalse(classified[0][6])
        self.assertEqual(classified[1][4], 0)
        self.assertTrue(classified[1][6])
        self.assertEqual(zero_on_b_count((planted_row, miss_row), b_sides), 1)
        self.assertTrue(gk_islands_zero_on_b_count_holds(6, 6))
        self.assertFalse(gk_islands_zero_on_b_count_holds(5, 6))
        self.assertFalse(doubled_8gram_is_maximal())
        self.assertTrue(doubled_8gram_is_n12_suffix())
        self.assertEqual(STANDING_CLAIM, "gk_islands_zero_on_b_count_holds")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariGkIslandsZeroOnBScoreboard(unittest.TestCase):
    """Cited-fixture G–K islands vs exact B hits. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.b_sides = load_b_sides()
        self.gk_sides = load_g_k_sides()
        self.rows = classify_gk_islands(STANDING_MAXIMALS, self.b_sides)
        self.measured_n = zero_on_b_count(STANDING_MAXIMALS, self.b_sides)
        self.claim_holds = gk_islands_zero_on_b_count_holds(self.measured_n)
        self.zero_rows = tuple(row for row in self.rows if row[6])
        self.hit_rows = tuple(row for row in self.rows if not row[6])

    def test_islands_are_the_locked_cycle_67_gk_maximals(self):
        """Six sequences come from cycle 67. None invented."""
        self.assertEqual(len(LOCKED_GK_ISLANDS), STANDING_MAXIMAL_COUNT)
        self.assertEqual(STANDING_MAXIMAL_COUNT, 6)
        self.assertEqual(len(STANDING_MAXIMALS), 6)
        self.assertEqual(LOCKED_GK_ISLANDS, tuple(row[0] for row in STANDING_MAXIMALS))
        self.assertEqual(STANDING_MAXIMALS[0][0], GRAM_17)
        self.assertEqual(STANDING_MAXIMALS[0][1], 17)
        self.assertEqual(STANDING_MAXIMALS[1][0], GRAM_15)
        self.assertEqual(STANDING_MAXIMALS[1][1], 15)
        self.assertEqual(STANDING_MAXIMALS[2][0], GRAM_13)
        self.assertEqual(STANDING_MAXIMALS[2][1], 13)
        self.assertEqual(STANDING_MAXIMALS[3][0], GRAM_12)
        self.assertEqual(STANDING_MAXIMALS[3][1], 12)
        self.assertEqual(STANDING_MAXIMALS[4][0], GRAM_10_KV)
        self.assertEqual(STANDING_MAXIMALS[4][1], 10)
        self.assertEqual(STANDING_MAXIMALS[5][0], GRAM_10_KR)
        self.assertEqual(STANDING_MAXIMALS[5][1], 10)
        self.assertEqual(tuple(row[1] for row in STANDING_MAXIMALS), STANDING_ZERO_ON_B_NS)
        self.assertEqual(
            self.survey["tablet_g_k_shared_n8_inventory"]["maximal_count"], 6
        )
        self.assertEqual(
            self.survey["tablet_g_k_shared_n8_inventory"]["maximals"][3][1], 12
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_six_of_six_are_exact_zero_on_b(self):
        """Measured N is 6. Hypothesis N=6 holds: no full island hits B."""
        self.assertEqual(len(self.rows), 6)
        self.assertEqual(self.measured_n, STANDING_GK_ISLANDS_ZERO_ON_B)
        self.assertEqual(STANDING_GK_ISLANDS_ZERO_ON_B, 6)
        self.assertEqual(len(self.zero_rows), 6)
        self.assertEqual(len(self.hit_rows), STANDING_GK_ISLANDS_HIT_ON_B)
        self.assertEqual(STANDING_GK_ISLANDS_HIT_ON_B, 0)
        self.assertEqual(self.measured_n + len(self.hit_rows), 6)
        self.assertEqual(
            tuple(i for i, row in enumerate(self.rows) if row[6]),
            STANDING_ZERO_ON_B_INDICES,
        )
        self.assertEqual(
            tuple(i for i, row in enumerate(self.rows) if not row[6]),
            STANDING_HIT_ON_B_INDICES,
        )
        self.assertEqual(tuple(row[1] for row in self.zero_rows), STANDING_ZERO_ON_B_NS)
        self.assertEqual(tuple(row[1] for row in self.hit_rows), STANDING_HIT_ON_B_NS)
        for tokens, n, g_site, k_site, b_hits, b_sites, zero in self.zero_rows:
            self.assertTrue(zero)
            self.assertEqual(b_hits, 0)
            self.assertEqual(b_sites, ())
            self.assertEqual(island_b_hits(tokens, self.b_sides), 0)
            self.assertEqual(ngram_hit_count(self.by_tablet["B"], tokens), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, tokens, VENDORED_TABLETS)[
                    VENDORED_TABLETS.index("B")
                ],
                0,
            )
            self.assertGreaterEqual(n, 8)
            self.assertEqual(len(tokens), n)
            for side, line, index in (g_site, k_site):
                names = LINE_NAMES[side]
                stems = self.gk_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), tokens)
        self.assertEqual(STANDING_HYPOTHESIS_N, 6)
        self.assertTrue(STANDING_HYPOTHESIS_N_HOLDS)
        self.assertEqual(self.measured_n, STANDING_HYPOTHESIS_N)
        self.assertEqual(self.claim_holds, STANDING_GK_ISLANDS_ZERO_ON_B_COUNT_HOLDS)
        self.assertTrue(STANDING_GK_ISLANDS_ZERO_ON_B_COUNT_HOLDS)
        self.assertTrue(gk_islands_zero_on_b_count_holds(self.measured_n))
        self.assertFalse(gk_islands_zero_on_b_count_holds(5))
        self.assertEqual(STANDING_CLAIM, "gk_islands_zero_on_b_count_holds")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n12_from_cycle_106_is_in_the_zero_on_b_set(self):
        """Cycle-106 / cycle-67 n=12 island is one of the six exact-0 rows."""
        tokens_12, n_12, g_12, k_12, b_hits_12, b_sites_12, zero_12 = self.rows[
            STANDING_N12_INDEX
        ]
        self.assertEqual(tokens_12, GRAM_12)
        self.assertEqual(n_12, 12)
        self.assertEqual(g_12, (SIDE_GR, "Gr1", 4))
        self.assertEqual(k_12, (SIDE_KR, "Kr1", 2))
        self.assertEqual(b_hits_12, 0)
        self.assertEqual(b_sites_12, ())
        self.assertTrue(zero_12)
        self.assertTrue(STANDING_N12_IS_ZERO_ON_B)
        self.assertIn(self.rows[STANDING_N12_INDEX], self.zero_rows)
        self.assertEqual(STANDING_ISLAND12_B_HITS, 0)
        self.assertEqual(ngram_hit_count(self.by_tablet["B"], GRAM_12), 0)
        self.assertEqual(
            self.survey["b_gk_doubled_8gram"]["island12_b_hits"], 0
        )
        for side, line, index in (g_12, k_12):
            stems = self.gk_sides[side][LINE_NAMES[side].index(line)][index : index + 12]
            self.assertEqual(tuple(stems), GRAM_12)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_doubled_8gram_is_a_suffix_not_a_maximal(self):
        """Cycle-106 8-gram leaks on B; it is not one of the six maximals."""
        self.assertEqual(GRAM8, ("260", "001", "004", "711", "260", "001", "004", "711"))
        self.assertEqual(GRAM8, GRAM4 + GRAM4)
        self.assertEqual(GRAM8, GRAM_12[4:])
        self.assertTrue(doubled_8gram_is_n12_suffix(GRAM8, GRAM_12))
        self.assertTrue(STANDING_DOUBLED_8GRAM_IS_N12_SUFFIX)
        self.assertFalse(doubled_8gram_is_maximal(GRAM8, STANDING_MAXIMALS))
        self.assertFalse(STANDING_DOUBLED_8GRAM_IS_MAXIMAL)
        self.assertNotIn(GRAM8, LOCKED_GK_ISLANDS)
        self.assertTrue(is_contiguous_substring(GRAM8, GRAM_12))
        self.assertEqual(substring_offsets(GRAM8, GRAM_12), (4,))
        for tokens in LOCKED_GK_ISLANDS:
            if tokens == GRAM_12:
                self.assertTrue(is_contiguous_substring(GRAM8, tokens))
            else:
                self.assertFalse(is_contiguous_substring(GRAM8, tokens))
        self.assertEqual(ngram_hit_count(self.by_tablet["B"], GRAM8), STANDING_DOUBLED_8GRAM_B_HITS)
        self.assertEqual(STANDING_DOUBLED_8GRAM_B_HITS, CYCLE_106_B_HITS)
        self.assertEqual(STANDING_DOUBLED_8GRAM_B_HITS, 1)
        self.assertEqual(
            island_b_sites(GRAM8, self.b_sides),
            CYCLE_106_B_SITES,
        )
        self.assertEqual(CYCLE_106_B_SITES, ((SIDE_BV, "Bv8", 21),))
        self.assertGreater(STANDING_DOUBLED_8GRAM_B_HITS, 0)
        self.assertEqual(STANDING_GK_ISLANDS_HIT_ON_B, 0)
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["n_ge_8_island"], False)
        self.assertTrue(self.survey["b_gk_doubled_8gram"]["suffix_only_on_b"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_island_suffix_and_w_scoreboards_still_compute(self):
        """Cycle 67 n≥8, cycle 68 off-G/K, cycles 105–106, and W stay."""
        prior_n8 = TestMamariSmallSantiagoLondonSharedN8Scoreboard()
        prior_n8.setUp()
        prior_n8.test_inventory_tokens_n_freq_and_hits()
        prior_n8.test_survey_matches_computed_lock()
        prior_off = TestMamariSmallSantiagoLondonIslandOffGkScoreboard()
        prior_off.setUp()
        prior_off.test_six_by_eight_hit_table()
        prior_off.test_survey_matches_computed_lock()
        prior_105 = TestMamariKMaxNGkIslandSubstringScoreboard()
        prior_105.setUp()
        prior_105.test_4gram_is_substring_of_locked_n12_island_only()
        prior_105.test_survey_matches_computed_lock()
        prior_106 = TestMamariBGkDoubled8GramScoreboard()
        prior_106.setUp()
        prior_106.test_n12_island_remains_zero_on_b()
        prior_106.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-113 zero-on-B count."""
        lock = self.survey["gk_islands_zero_on_b"]
        self.assertEqual(lock["cycle"], 113)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["island_count"], STANDING_MAXIMAL_COUNT)
        self.assertEqual(lock["island_count"], 6)
        self.assertEqual(lock["gk_islands_zero_on_b"], STANDING_GK_ISLANDS_ZERO_ON_B)
        self.assertEqual(lock["gk_islands_zero_on_b"], 6)
        self.assertEqual(lock["gk_islands_hit_on_b"], STANDING_GK_ISLANDS_HIT_ON_B)
        self.assertEqual(lock["from_cycle"], 67)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["gk_islands_zero_on_b_count_holds"])
        self.assertEqual(
            lock["gk_islands_zero_on_b_count_holds"],
            STANDING_GK_ISLANDS_ZERO_ON_B_COUNT_HOLDS,
        )
        self.assertEqual(lock["hypothesis_n"], STANDING_HYPOTHESIS_N)
        self.assertTrue(lock["hypothesis_n_holds"])
        self.assertEqual(lock["hypothesis_n_holds"], STANDING_HYPOTHESIS_N_HOLDS)
        self.assertTrue(lock["n12_is_zero_on_b"])
        self.assertEqual(lock["n12_is_zero_on_b"], STANDING_N12_IS_ZERO_ON_B)
        self.assertEqual(lock["n12_index"], STANDING_N12_INDEX)
        self.assertEqual(tuple(lock["zero_on_b_ns"]), STANDING_ZERO_ON_B_NS)
        self.assertEqual(tuple(lock["hit_on_b_ns"]), STANDING_HIT_ON_B_NS)
        self.assertEqual(tuple(lock["zero_on_b_indices"]), STANDING_ZERO_ON_B_INDICES)
        self.assertEqual(tuple(lock["hit_on_b_indices"]), STANDING_HIT_ON_B_INDICES)
        self.assertEqual(len(lock["islands"]), 6)
        for computed, recorded in zip(self.rows, lock["islands"], strict=True):
            tokens, n, g_site, k_site, b_hits, b_sites, zero = computed
            self.assertEqual(tuple(recorded["tokens"]), tokens)
            self.assertEqual(recorded["n"], n)
            self.assertEqual(tuple(recorded["g_site"]), g_site)
            self.assertEqual(tuple(recorded["k_site"]), k_site)
            self.assertEqual(recorded["b_hits"], b_hits)
            self.assertEqual(tuple(tuple(site) for site in recorded["b_sites"]), b_sites)
            self.assertEqual(recorded["zero_on_b"], zero)
        n12 = lock["islands"][STANDING_N12_INDEX]
        self.assertEqual(tuple(n12["tokens"]), GRAM_12)
        self.assertEqual(n12["n"], 12)
        self.assertTrue(n12["zero_on_b"])
        self.assertEqual(n12["b_hits"], 0)
        self.assertEqual(tuple(lock["tokens8"]), GRAM8)
        self.assertFalse(lock["doubled_8gram_is_maximal"])
        self.assertEqual(
            lock["doubled_8gram_is_maximal"], STANDING_DOUBLED_8GRAM_IS_MAXIMAL
        )
        self.assertTrue(lock["doubled_8gram_is_n12_suffix"])
        self.assertEqual(
            lock["doubled_8gram_is_n12_suffix"], STANDING_DOUBLED_8GRAM_IS_N12_SUFFIX
        )
        self.assertEqual(lock["doubled_8gram_b_hits"], STANDING_DOUBLED_8GRAM_B_HITS)
        self.assertEqual(
            tuple(tuple(site) for site in lock["doubled_8gram_b_sites"]),
            CYCLE_106_B_SITES,
        )
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertTrue(lock["standing_k_max_n_gk_island_substring_unchanged"])
        self.assertTrue(lock["standing_b_gk_doubled_8gram_unchanged"])
        self.assertTrue(lock["standing_hq_islands_zero_on_p_unchanged"])
        self.assertTrue(lock["standing_hp_islands_zero_on_q_unchanged"])
        self.assertTrue(lock["standing_qp_islands_zero_on_h_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["cycle"], 67)
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["maximal_count"], 6)
        self.assertEqual(self.survey["tablet_g_k_island_off_gk_hits"]["cycle"], 68)
        self.assertFalse(self.survey["tablet_g_k_island_off_gk_hits"]["any_off_gk"])
        self.assertEqual(self.survey["k_max_n_gk_island_substring"]["cycle"], 105)
        self.assertTrue(
            self.survey["k_max_n_gk_island_substring"]["k_max_n_is_gk_island_substring"]
        )
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["cycle"], 106)
        self.assertTrue(self.survey["b_gk_doubled_8gram"]["b_has_gk_doubled_8gram"])
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["island12_b_hits"], 0)
        self.assertFalse(self.survey["b_gk_doubled_8gram"]["n_ge_8_island"])
        self.assertEqual(self.survey["hq_islands_zero_on_p"]["cycle"], 110)
        self.assertEqual(self.survey["hq_islands_zero_on_p"]["hq_islands_zero_on_p"], 12)
        self.assertEqual(self.survey["hp_islands_zero_on_q"]["cycle"], 111)
        self.assertEqual(self.survey["hp_islands_zero_on_q"]["hp_islands_zero_on_q"], 15)
        self.assertEqual(self.survey["qp_islands_zero_on_h"]["cycle"], 112)
        self.assertEqual(self.survey["qp_islands_zero_on_h"]["qp_islands_zero_on_h"], 7)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariGkIslandsZeroOnBImageSnapshot(unittest.TestCase):
    """Cycle 113 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
