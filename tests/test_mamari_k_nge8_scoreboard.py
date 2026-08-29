"""K's repeating n≥8 grams vs locked G–K island sequences.

Cycle 130 text-search lock. Uses already-vendored A–V and the
cycle-67 six maximal G–K islands (plus the cycle-76/78 n=25).
Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Does not redo G–K n≥8 inventories.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Enumerates every distinct contiguous n≥8 gram with freq≥2 on K
(same per-line Barthel parser as the leak table / G–K island
scoreboards). For each, whether it is an exact contiguous
substring of at least one locked G–K island. Hypothesis: no
K-local repeating n≥8 (every such gram is an island substring;
expect N=0 given the cycle-99 inventory max n=4). Measured: 0
repeating n≥8; 0 are substrings; 0 independent. K's longest
repeating gram remains the cycle-99/105 4-gram, itself a G–K
n=12 substring. The six islands are each freq 1 on K, so they
do not count as K-repeats. The cycle-106 doubled 8-gram suffix
is also freq 1 on K. Claim that can lose:
k_repeating_nge8_all_substrings_of_gk_islands. The claim is
true (empty repeating set; no independent remainder; G vs K
n≥8 asymmetry: G has 3 independent, K has 0). Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_b_gk_doubled_8gram_scoreboard import (
    GRAM8,
    TestMamariBGkDoubled8gramScoreboard,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_N as INVENTORY_LONGEST_N,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_TOKENS as INVENTORY_LONGEST_TOKENS,
)
from tests.test_mamari_corpus_max_n_leak_table_scoreboard import leaks_from_hits
from tests.test_mamari_g_nge8_scoreboard import (
    G_8PREFIX,
    LOCKED_GK_ISLANDS,
    STANDING_INDEPENDENT as G_STANDING_INDEPENDENT,
    STANDING_INDEPENDENT_COUNT as G_STANDING_INDEPENDENT_COUNT,
    STANDING_N9,
    STANDING_N25,
    STANDING_REPEATING_COUNT as G_STANDING_REPEATING_COUNT,
    TestMamariGNge8Scoreboard,
    independent_rows,
    is_gk_island_substring,
    is_n25_substring,
    repeating_nge8_grams,
)
from tests.test_mamari_gk_islands_zero_on_b_scoreboard import (
    TestMamariGkIslandsZeroOnBScoreboard,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    GRAM4,
    TestMamariKMaxNGkIslandSubstringScoreboard,
    is_contiguous_substring,
    matching_islands,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_p_nge8_scoreboard import (
    TestMamariPNge8Scoreboard,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_london_kr_scoreboard import KR_LINE_NAMES
from tests.test_mamari_small_london_kv_scoreboard import KV_LINE_NAMES
from tests.test_mamari_small_santiago_london_grkv_maximal_scoreboard import (
    TestMamariSmallSantiagoLondonGrkvMaximalScoreboard,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_KR,
    SIDE_KV,
    load_g_k_sides,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    GRAM_10_KR,
    GRAM_10_KV,
    GRAM_12,
    GRAM_13,
    GRAM_15,
    GRAM_17,
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    TestMamariSmallSantiagoLondonSharedN8Scoreboard,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 8
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N4 = GRAM4
STANDING_DOUBLED8 = GRAM8
STANDING_REPEATING_COUNT = 0
STANDING_SUBSTRING_COUNT = 0
STANDING_INDEPENDENT_COUNT = 0
STANDING_COUNTS_BY_N = {}
STANDING_SUBSTRING_BY_N = {}
STANDING_INDEPENDENT_BY_N = {}
STANDING_LONGEST_N = 0
STANDING_ROWS = ()
STANDING_INDEPENDENT = ()
STANDING_INDEPENDENT_OFF_K = ()
STANDING_INDEPENDENT_KR_HITS = ()
STANDING_INDEPENDENT_KV_HITS = ()
STANDING_INDEPENDENT_G_HITS = ()
STANDING_INDEPENDENT_B_HITS = ()
STANDING_ISLAND_FREQ_ON_K = (1, 1, 1, 1, 1, 1)
STANDING_DOUBLED8_FREQ_ON_K = 1
STANDING_N25_FREQ_ON_K = 0
STANDING_KNOWN_DISTINCT = True
STANDING_N4_IN_SET = False
STANDING_DOUBLED8_IN_SET = False
STANDING_N4_IS_GK_ISLAND_SUBSTRING = True
STANDING_DOUBLED8_IS_GK_ISLAND_SUBSTRING = True
STANDING_ISLANDS_FREQ1_ON_K = True
STANDING_G_REPEATING_COUNT = G_STANDING_REPEATING_COUNT
STANDING_G_INDEPENDENT_COUNT = G_STANDING_INDEPENDENT_COUNT
STANDING_G_K_NGE8_ASYMMETRY = True
STANDING_CLAIM = "k_repeating_nge8_all_substrings_of_gk_islands"
STANDING_K_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS = True
STANDING_RESULT = "k_repeating_nge8"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
INDEPENDENT_PLANT = G_8PREFIX
ISLAND_8GRAM = GRAM_12[-8:]


def nge8_sites(
    gram: tuple[str, ...],
    k_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Kr then Kv. Search only."""
    hits = named_side_hits(k_sides[SIDE_KR], KR_LINE_NAMES, SIDE_KR, gram)
    hits += named_side_hits(k_sides[SIDE_KV], KV_LINE_NAMES, SIDE_KV, gram)
    return tuple(site_tuple(hit) for hit in hits)


def k_repeating_nge8_all_substrings_of_gk_islands(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥8 is a G–K island substring.

    The empty inventory is true: K has no repeating n≥8, so none
    fail the island-substring test (no K-local remainder).
    """
    return all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_k_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off K. Counts only."""
    return sum(leaks_from_hits("K", hits, tablets).values())


class TestKNge8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted non-island 8-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = INDEPENDENT_PLANT
        planted = ISLAND_8GRAM
        self.assertNotEqual(home, planted)
        self.assertEqual(len(home), 8)
        self.assertEqual(len(planted), 8)
        self.assertEqual(planted, STANDING_DOUBLED8)
        self.assertFalse(is_gk_island_substring(home))
        self.assertTrue(is_gk_island_substring(planted))
        self.assertTrue(is_gk_island_substring(LOCKED_GK_ISLANDS[0]))
        self.assertTrue(is_gk_island_substring(GRAM_12))
        self.assertTrue(is_gk_island_substring(GRAM_17[:8]))
        self.assertTrue(is_gk_island_substring(GRAM_12[-8:]))
        self.assertFalse(is_gk_island_substring(home + ("999",)))
        self.assertTrue(is_gk_island_substring(STANDING_N4))
        self.assertEqual(len(STANDING_N4), 4)
        self.assertTrue(STANDING_N4_IS_GK_ISLAND_SUBSTRING)
        self.assertTrue(STANDING_DOUBLED8_IS_GK_ISLAND_SUBSTRING)
        self.assertFalse(is_n25_substring(home))
        self.assertTrue(is_n25_substring(GRAM_15))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge8_grams(once_each, analyzer), ())
        self.assertTrue(k_repeating_nge8_all_substrings_of_gk_islands(()))
        twice_island = [list(planted), list(planted)]
        island_only = repeating_nge8_grams(twice_island, analyzer)
        self.assertGreaterEqual(len(island_only), 1)
        self.assertIn((planted, 8, 2), island_only)
        island_rows = tuple(
            (gram, n, freq, is_gk_island_substring(gram), ())
            for gram, n, freq in island_only
        )
        self.assertTrue(k_repeating_nge8_all_substrings_of_gk_islands(island_rows))
        self.assertEqual(independent_rows(island_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge8_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_gk_island_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(k_repeating_nge8_all_substrings_of_gk_islands(both_rows))
        self.assertIn(home, tuple(gram for gram, n, _freq in both if n == 8))
        gapped = [list(home[:4]) + ["999"] + list(home[4:]), list(home)]
        self.assertEqual(repeating_nge8_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "k_repeating_nge8_all_substrings_of_gk_islands")
        self.assertTrue(STANDING_K_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariKNge8Scoreboard(unittest.TestCase):
    """Cited-fixture K repeating n≥8 vs G–K islands. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.k_sides = load_g_k_sides()
        measured = repeating_nge8_grams(self.by_tablet["K"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_gk_island_substring(gram),
                nge8_sites(gram, self.k_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = k_repeating_nge8_all_substrings_of_gk_islands(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_k = tuple(
            off_k_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_67_islands_and_cycle_99_n4_not_invented(self):
        """G–K islands and the K 4-gram are prior locks."""
        self.assertEqual(len(LOCKED_GK_ISLANDS), STANDING_MAXIMAL_COUNT)
        self.assertEqual(STANDING_MAXIMAL_COUNT, 6)
        self.assertEqual(LOCKED_GK_ISLANDS[0], GRAM_17)
        self.assertEqual(LOCKED_GK_ISLANDS[1], GRAM_15)
        self.assertEqual(LOCKED_GK_ISLANDS[2], GRAM_13)
        self.assertEqual(LOCKED_GK_ISLANDS[3], GRAM_12)
        self.assertEqual(LOCKED_GK_ISLANDS[4], GRAM_10_KV)
        self.assertEqual(LOCKED_GK_ISLANDS[5], GRAM_10_KR)
        self.assertEqual(tuple(row[1] for row in STANDING_MAXIMALS), (17, 15, 13, 12, 10, 10))
        self.assertEqual(STANDING_N4, INVENTORY_LONGEST_TOKENS["K"])
        self.assertEqual(INVENTORY_LONGEST_N["K"], 4)
        self.assertEqual(len(STANDING_N4), 4)
        self.assertEqual(STANDING_N4, ("260", "001", "004", "711"))
        self.assertEqual(STANDING_DOUBLED8, ("260", "001", "004", "711", "260", "001", "004", "711"))
        self.assertEqual(STANDING_DOUBLED8, GRAM_12[4:])
        self.assertEqual(
            tuple(tuple(row[0]) for row in self.survey["tablet_g_k_shared_n8_inventory"]["maximals"]),
            LOCKED_GK_ISLANDS,
        )
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["K"]["longest_tokens"]),
            STANDING_N4,
        )
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["cycle"], 67)
        self.assertEqual(self.survey["tablet_g_k_grkv_maximals"]["cycle"], 78)
        self.assertEqual(self.survey["k_max_n_gk_island_substring"]["cycle"], 105)
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["cycle"], 106)
        self.assertEqual(self.survey["g_repeating_nge8"]["cycle"], 125)
        self.assertEqual(self.survey["p_repeating_nge8"]["cycle"], 129)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertNotEqual(STANDING_N4, GRAM_17)
        self.assertNotEqual(STANDING_N4, GRAM_12)
        self.assertTrue(is_gk_island_substring(STANDING_N4))
        self.assertTrue(is_contiguous_substring(STANDING_N4, GRAM_12))
        self.assertTrue(STANDING_N4_IS_GK_ISLAND_SUBSTRING)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_holds(self):
        """0 repeating n≥8; 0 substrings; 0 independent. Claim is true."""
        self.assertEqual(len(self.rows), STANDING_REPEATING_COUNT)
        self.assertEqual(self.substring_count, STANDING_SUBSTRING_COUNT)
        self.assertEqual(len(self.independent), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_REPEATING_COUNT, 0)
        self.assertEqual(STANDING_SUBSTRING_COUNT, 0)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertEqual(
            STANDING_SUBSTRING_COUNT + STANDING_INDEPENDENT_COUNT,
            STANDING_REPEATING_COUNT,
        )
        by_n = {}
        sub_by_n = {}
        indep_by_n = {}
        for _gram, n, _freq, is_sub, _sites in self.rows:
            by_n[n] = by_n.get(n, 0) + 1
            if is_sub:
                sub_by_n[n] = sub_by_n.get(n, 0) + 1
            else:
                indep_by_n[n] = indep_by_n.get(n, 0) + 1
        self.assertEqual(by_n, STANDING_COUNTS_BY_N)
        self.assertEqual(sub_by_n, STANDING_SUBSTRING_BY_N)
        self.assertEqual(indep_by_n, STANDING_INDEPENDENT_BY_N)
        self.assertEqual(STANDING_LONGEST_N, 0)
        self.assertEqual(by_n, {})
        self.assertTrue(k_repeating_nge8_all_substrings_of_gk_islands(self.rows))
        self.assertEqual(self.claim_holds, STANDING_K_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS)
        self.assertTrue(STANDING_K_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS)
        self.assertEqual(STANDING_CLAIM, "k_repeating_nge8_all_substrings_of_gk_islands")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        n4 = self.analyzer.extract_ngrams(self.by_tablet["K"], n=4, min_frequency=2)
        self.assertIn((STANDING_N4, 2), n4)
        n5 = self.analyzer.extract_ngrams(self.by_tablet["K"], n=5, min_frequency=2)
        self.assertEqual(n5, [])
        n6 = self.analyzer.extract_ngrams(self.by_tablet["K"], n=6, min_frequency=2)
        self.assertEqual(n6, [])
        n7 = self.analyzer.extract_ngrams(self.by_tablet["K"], n=7, min_frequency=2)
        self.assertEqual(n7, [])
        n8 = self.analyzer.extract_ngrams(self.by_tablet["K"], n=8, min_frequency=2)
        self.assertEqual(n8, [])
        self.assertEqual(G_STANDING_REPEATING_COUNT, 3)
        self.assertEqual(G_STANDING_INDEPENDENT_COUNT, 3)
        self.assertTrue(STANDING_G_K_NGE8_ASYMMETRY)
        self.assertNotEqual(STANDING_REPEATING_COUNT, G_STANDING_REPEATING_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_inventory_matches_standing_rows(self):
        """Measured grams, n, freq, substring flag, and sites match the lock."""
        self.assertEqual(self.rows, STANDING_ROWS)
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_ROWS, ())
        self.assertFalse(STANDING_N4_IN_SET)
        self.assertFalse(STANDING_DOUBLED8_IN_SET)
        self.assertNotIn(STANDING_N4, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 4))
        self.assertNotIn(STANDING_DOUBLED8, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8))
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_empty(self):
        """No K-local repeating n≥8 remainder. Islands and doubled 8-gram are freq 1."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertEqual(indep_tokens, ())
        self.assertNotIn(STANDING_N4, indep_tokens)
        self.assertNotIn(STANDING_DOUBLED8, indep_tokens)
        self.assertTrue(is_gk_island_substring(STANDING_N4))
        self.assertTrue(is_gk_island_substring(STANDING_DOUBLED8))
        self.assertFalse(is_contiguous_substring(STANDING_N4, GRAM_17))
        self.assertFalse(is_contiguous_substring(STANDING_N4, GRAM_15))
        self.assertFalse(is_contiguous_substring(STANDING_N4, GRAM_13))
        self.assertTrue(is_contiguous_substring(STANDING_N4, GRAM_12))
        self.assertFalse(is_contiguous_substring(STANDING_N4, GRAM_10_KV))
        self.assertFalse(is_contiguous_substring(STANDING_N4, GRAM_10_KR))
        self.assertEqual(matching_islands(STANDING_N4, STANDING_MAXIMALS)[0][1], 12)
        self.assertFalse(is_contiguous_substring(STANDING_N4, STANDING_N25))
        self.assertFalse(is_n25_substring(STANDING_N4))
        for island in LOCKED_GK_ISLANDS:
            self.assertNotIn(island, indep_tokens)
            self.assertEqual(ngram_hit_count(self.by_tablet["G"], island), 1)
            self.assertEqual(ngram_hit_count(self.by_tablet["K"], island), 1)
        self.assertEqual(ngram_hit_count(self.by_tablet["K"], STANDING_DOUBLED8), 1)
        self.assertEqual(ngram_hit_count(self.by_tablet["K"], STANDING_N25), 0)
        self.assertEqual(ngram_hit_count(self.by_tablet["K"], STANDING_N9), 0)
        self.assertEqual(len(indep_tokens), 0)
        self.assertTrue(STANDING_ISLANDS_FREQ1_ON_K)
        self.assertEqual(STANDING_ISLAND_FREQ_ON_K, (1,) * STANDING_MAXIMAL_COUNT)
        self.assertEqual(STANDING_DOUBLED8_FREQ_ON_K, 1)
        self.assertEqual(STANDING_N25_FREQ_ON_K, 0)
        for gram, _n, _freq, _sites in G_STANDING_INDEPENDENT:
            self.assertEqual(ngram_hit_count(self.by_tablet["K"], gram), 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_k_hits(self):
        """Empty independent set; no off-K remainder to count."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_k, STANDING_INDEPENDENT_OFF_K)
        self.assertEqual(STANDING_INDEPENDENT_OFF_K, ())
        self.assertEqual(self.indep_hits_by_tablet, ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_KR_HITS), ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_KV_HITS), ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_G_HITS), ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_B_HITS), ())
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(ngram_hit_count(self.k_sides[SIDE_KR], STANDING_N4), 2)
        self.assertEqual(ngram_hit_count(self.k_sides[SIDE_KV], STANDING_N4), 0)
        self.assertEqual(
            nge8_sites(STANDING_N4, self.k_sides),
            ((SIDE_KR, "Kr1", 6), (SIDE_KR, "Kr1", 10)),
        )
        self.assertEqual(
            nge8_sites(STANDING_DOUBLED8, self.k_sides),
            ((SIDE_KR, "Kr1", 6),),
        )
        self.assertEqual(
            nge8_sites(GRAM_17, self.k_sides),
            ((SIDE_KR, "Kr5", 0),),
        )
        self.assertEqual(
            nge8_sites(GRAM_15, self.k_sides),
            ((SIDE_KV, "Kv4", 7),),
        )
        self.assertEqual(
            nge8_sites(GRAM_13, self.k_sides),
            ((SIDE_KR, "Kr2", 16),),
        )
        self.assertEqual(
            nge8_sites(GRAM_12, self.k_sides),
            ((SIDE_KR, "Kr1", 2),),
        )
        self.assertEqual(
            nge8_sites(GRAM_10_KV, self.k_sides),
            ((SIDE_KV, "Kv3", 15),),
        )
        self.assertEqual(
            nge8_sites(GRAM_10_KR, self.k_sides),
            ((SIDE_KR, "Kr4", 12),),
        )
        self.assertEqual(nge8_sites(STANDING_N25, self.k_sides), ())
        self.assertEqual(nge8_sites(STANDING_N9, self.k_sides), ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_129_125_105_106_67_78_113_and_w_scoreboards_still_compute(self):
        """Cycle 129 P n≥8, 125 G n≥8, 105/106 K/B, 67/78 islands, 113, W stay."""
        prior_129 = TestMamariPNge8Scoreboard()
        prior_129.setUp()
        prior_129.test_counts_and_hypothesis_all_substrings_holds()
        prior_129.test_survey_matches_computed_lock()
        prior_125 = TestMamariGNge8Scoreboard()
        prior_125.setUp()
        prior_125.test_counts_and_hypothesis_all_substrings_loses()
        prior_125.test_survey_matches_computed_lock()
        prior_105 = TestMamariKMaxNGkIslandSubstringScoreboard()
        prior_105.setUp()
        prior_105.test_survey_matches_computed_lock()
        prior_106 = TestMamariBGkDoubled8gramScoreboard()
        prior_106.setUp()
        prior_106.test_survey_matches_computed_lock()
        prior_67 = TestMamariSmallSantiagoLondonSharedN8Scoreboard()
        prior_67.setUp()
        prior_67.test_survey_matches_computed_lock()
        prior_78 = TestMamariSmallSantiagoLondonGrkvMaximalScoreboard()
        prior_78.setUp()
        prior_78.test_survey_matches_computed_lock()
        prior_113 = TestMamariGkIslandsZeroOnBScoreboard()
        prior_113.setUp()
        prior_113.test_six_of_six_are_exact_zero_on_b()
        prior_113.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-130 n≥8 island-substring lock."""
        lock = self.survey["k_repeating_nge8"]
        self.assertEqual(lock["cycle"], 130)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(lock["island_count"], STANDING_MAXIMAL_COUNT)
        self.assertEqual(tuple(lock["island_ns"]), (17, 15, 13, 12, 10, 10))
        self.assertEqual(
            tuple(tuple(tokens) for tokens in lock["islands"]),
            LOCKED_GK_ISLANDS,
        )
        self.assertEqual(tuple(lock["home_tokens4"]), STANDING_N4)
        self.assertEqual(tuple(lock["doubled8_tokens"]), STANDING_DOUBLED8)
        self.assertEqual(tuple(lock["n25_tokens"]), STANDING_N25)
        measured_tokens = [
            [list(tokens), n, freq, is_sub, [list(site) for site in sites]]
            for tokens, n, freq, is_sub, sites in STANDING_ROWS
        ]
        self.assertEqual(lock["rows"], measured_tokens)
        indep_lock = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
                "off_k_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_k_hits"]), STANDING_INDEPENDENT_OFF_K)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertFalse(lock["n4_in_set"])
        self.assertFalse(lock["doubled8_in_set"])
        self.assertTrue(lock["n4_is_gk_island_substring"])
        self.assertTrue(lock["doubled8_is_gk_island_substring"])
        self.assertTrue(lock["islands_freq1_on_k"])
        self.assertEqual(tuple(lock["island_freq_on_k"]), STANDING_ISLAND_FREQ_ON_K)
        self.assertEqual(lock["doubled8_freq_on_k"], STANDING_DOUBLED8_FREQ_ON_K)
        self.assertEqual(lock["n25_freq_on_k"], STANDING_N25_FREQ_ON_K)
        self.assertEqual(lock["g_repeating_count"], STANDING_G_REPEATING_COUNT)
        self.assertEqual(lock["g_independent_count"], STANDING_G_INDEPENDENT_COUNT)
        self.assertTrue(lock["g_k_nge8_asymmetry"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["k_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(
            lock["k_repeating_nge8_all_substrings_of_gk_islands"],
            STANDING_K_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_maximals_unchanged"])
        self.assertTrue(lock["standing_gk_islands_zero_on_b_unchanged"])
        self.assertTrue(lock["standing_k_max_n_gk_island_substring_unchanged"])
        self.assertTrue(lock["standing_b_gk_doubled_8gram_unchanged"])
        self.assertTrue(lock["standing_g_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_p_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_h_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_e_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["cycle"], 67)
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["maximal_count"], 6)
        self.assertTrue(self.survey["tablet_g_k_shared_n8_inventory"]["islands_disjoint"])
        self.assertEqual(self.survey["tablet_g_k_grkv_maximals"]["cycle"], 78)
        self.assertEqual(self.survey["tablet_g_k_grkv_maximals"]["gr_kv_maximals"], [10, 25])
        self.assertTrue(self.survey["tablet_g_k_grkv_maximals"]["island6_is_suffix"])
        self.assertEqual(self.survey["k_max_n_gk_island_substring"]["cycle"], 105)
        self.assertTrue(self.survey["k_max_n_gk_island_substring"]["k_max_n_is_gk_island_substring"])
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["cycle"], 106)
        self.assertTrue(self.survey["b_gk_doubled_8gram"]["b_has_gk_doubled_8gram"])
        self.assertEqual(self.survey["gk_islands_zero_on_b"]["cycle"], 113)
        self.assertEqual(self.survey["gk_islands_zero_on_b"]["gk_islands_zero_on_b"], 6)
        self.assertEqual(self.survey["g_repeating_nge8"]["cycle"], 125)
        self.assertEqual(self.survey["g_repeating_nge8"]["repeating_count"], 3)
        self.assertFalse(self.survey["g_repeating_nge8"]["g_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(self.survey["p_repeating_nge8"]["cycle"], 129)
        self.assertEqual(self.survey["p_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["p_repeating_nge8"]["p_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["q_repeating_nge8"]["cycle"], 128)
        self.assertEqual(self.survey["q_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["q_repeating_nge8"]["q_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["h_repeating_nge8"]["cycle"], 126)
        self.assertEqual(self.survey["h_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["h_repeating_nge8"]["h_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["e_repeating_nge8"]["cycle"], 124)
        self.assertFalse(self.survey["e_repeating_nge8"]["e_repeating_nge8_all_substrings_of_n9"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["K"]["longest_n"], 4)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariKNge8ImageSnapshot(unittest.TestCase):
    """Cycle 130 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
