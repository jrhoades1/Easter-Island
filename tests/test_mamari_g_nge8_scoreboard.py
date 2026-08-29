"""G's repeating n≥8 grams vs locked G–K island sequences.

Cycle 125 text-search lock. Uses already-vendored A–V and the
cycle-67 six maximal G–K islands (plus the cycle-76/78 n=25).
Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Does not redo G–K n≥8
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Enumerates every distinct contiguous n≥8 gram with freq≥2 on G
(same per-line Barthel parser as the leak table / G–K island
scoreboards). For each, whether it is an exact contiguous
substring of at least one locked G–K island. Hypothesis: no
independent repeating n≥8 (every such gram is an island
substring). Measured: 3 repeating n≥8; 0 are substrings; 3
independent (the cycle-99 G 9-gram and its two 8-grams). Claim
that can lose: g_repeating_nge8_all_substrings_of_gk_islands.
The claim is false. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
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
from tests.test_mamari_e_nge8_scoreboard import (
    TestMamariENge8Scoreboard,
)
from tests.test_mamari_gk_islands_zero_on_b_scoreboard import (
    TestMamariGkIslandsZeroOnBScoreboard,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
    matching_islands,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_gr_scoreboard import GR_LINE_NAMES
from tests.test_mamari_small_santiago_gv_scoreboard import GV_LINE_NAMES
from tests.test_mamari_small_santiago_london_grkv_block_scoreboard import (
    STANDING_COMBINED_SHARED_TOKENS,
)
from tests.test_mamari_small_santiago_london_grkv_maximal_scoreboard import (
    TestMamariSmallSantiagoLondonGrkvMaximalScoreboard,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
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
LOCKED_GK_ISLANDS = tuple(tokens for tokens, _n, _fg, _fk, _gs, _ks in STANDING_MAXIMALS)
STANDING_N25 = STANDING_COMBINED_SHARED_TOKENS
STANDING_N9 = INVENTORY_LONGEST_TOKENS["G"]
G_8PREFIX = STANDING_N9[:8]
G_8SUFFIX = STANDING_N9[1:]
STANDING_REPEATING_COUNT = 3
STANDING_SUBSTRING_COUNT = 0
STANDING_INDEPENDENT_COUNT = 3
STANDING_COUNTS_BY_N = {8: 2, 9: 1}
STANDING_SUBSTRING_BY_N = {}
STANDING_INDEPENDENT_BY_N = {8: 2, 9: 1}
STANDING_LONGEST_N = 9
# (tokens, n, freq, is_island_substring, sites)
STANDING_ROWS = (
    (G_8PREFIX, 8, 2, False, ((SIDE_GR, "Gr8", 0), (SIDE_GR, "Gr8", 20))),
    (G_8SUFFIX, 8, 2, False, ((SIDE_GR, "Gr8", 1), (SIDE_GR, "Gr8", 21))),
    (STANDING_N9, 9, 2, False, ((SIDE_GR, "Gr8", 0), (SIDE_GR, "Gr8", 20))),
)
STANDING_INDEPENDENT = tuple(
    (tokens, n, freq, sites)
    for tokens, n, freq, is_sub, sites in STANDING_ROWS
    if not is_sub
)
STANDING_INDEPENDENT_OFF_G = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_GR_HITS = (2,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_GV_HITS = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_K_HITS = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_KNOWN_DISTINCT = True
STANDING_N9_IN_SET = True
STANDING_N25_ALSO_MISSES = True
STANDING_CLAIM = "g_repeating_nge8_all_substrings_of_gk_islands"
STANDING_G_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS = False
STANDING_RESULT = "g_repeating_nge8"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def repeating_nge8_grams(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
) -> tuple[tuple[tuple[str, ...], int, int], ...]:
    """Distinct contiguous n≥8 grams with freq≥2. Search only."""
    rows: list[tuple[tuple[str, ...], int, int]] = []
    n = PROFILE_MIN_N
    while True:
        found = analyzer.extract_ngrams(lines, n=n, min_frequency=2)
        if not found:
            break
        rows.extend((gram, n, freq) for gram, freq in found)
        n += 1
    return tuple(rows)


def nge8_sites(
    gram: tuple[str, ...],
    g_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Gr then Gv. Search only."""
    hits = named_side_hits(g_sides[SIDE_GR], GR_LINE_NAMES, SIDE_GR, gram)
    hits += named_side_hits(g_sides[SIDE_GV], GV_LINE_NAMES, SIDE_GV, gram)
    return tuple(site_tuple(hit) for hit in hits)


def is_gk_island_substring(
    gram: tuple[str, ...],
    maximals: tuple = STANDING_MAXIMALS,
) -> bool:
    """True iff gram is an exact contiguous run inside a locked island."""
    return bool(matching_islands(gram, maximals))


def is_n25_substring(
    gram: tuple[str, ...],
    n25: tuple[str, ...] = STANDING_N25,
) -> bool:
    """True iff gram is an exact contiguous run inside the n=25."""
    return is_contiguous_substring(gram, n25)


def independent_rows(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Rows that are not exact contiguous substrings of any island."""
    return tuple(
        (tokens, n, freq, sites)
        for tokens, n, freq, is_sub, sites in rows
        if not is_sub
    )


def g_repeating_nge8_all_substrings_of_gk_islands(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥8 is a G–K island substring."""
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_g_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off G. Counts only."""
    return sum(leaks_from_hits("G", hits, tablets).values())


class TestGNge8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted Gr 8-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = STANDING_N9
        planted = GRAM_12[-8:]
        self.assertNotEqual(home, planted)
        self.assertEqual(len(home), 9)
        self.assertEqual(len(planted), 8)
        self.assertFalse(is_gk_island_substring(home))
        self.assertFalse(is_gk_island_substring(home[1:9]))
        self.assertFalse(is_gk_island_substring(home[:8]))
        self.assertTrue(is_gk_island_substring(planted))
        self.assertTrue(is_gk_island_substring(GRAM_12))
        self.assertTrue(is_gk_island_substring(GRAM_17[:8]))
        self.assertFalse(is_gk_island_substring(home + ("999",)))
        self.assertFalse(is_n25_substring(home))
        self.assertTrue(is_n25_substring(GRAM_15))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge8_grams(once_each, analyzer), ())
        self.assertFalse(g_repeating_nge8_all_substrings_of_gk_islands(()))
        twice_island = [list(planted), list(planted)]
        island_only = repeating_nge8_grams(twice_island, analyzer)
        self.assertGreaterEqual(len(island_only), 1)
        self.assertIn((planted, 8, 2), island_only)
        island_rows = tuple(
            (gram, n, freq, is_gk_island_substring(gram), ())
            for gram, n, freq in island_only
        )
        self.assertTrue(g_repeating_nge8_all_substrings_of_gk_islands(island_rows))
        self.assertEqual(independent_rows(island_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge8_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_gk_island_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(g_repeating_nge8_all_substrings_of_gk_islands(both_rows))
        self.assertIn(home, tuple(gram for gram, n, _freq in both if n == 9))
        gapped = [list(home[:5]) + ["999"] + list(home[5:]), list(home)]
        self.assertEqual(repeating_nge8_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "g_repeating_nge8_all_substrings_of_gk_islands")
        self.assertFalse(STANDING_G_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 3)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertFalse(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariGNge8Scoreboard(unittest.TestCase):
    """Cited-fixture G repeating n≥8 vs G–K islands. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.g_sides = load_g_k_sides()
        measured = repeating_nge8_grams(self.by_tablet["G"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_gk_island_substring(gram),
                nge8_sites(gram, self.g_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = g_repeating_nge8_all_substrings_of_gk_islands(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_g = tuple(
            off_g_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_67_islands_and_cycle_99_n9_not_invented(self):
        """G–K islands and the G 9-gram are prior locks."""
        self.assertEqual(len(LOCKED_GK_ISLANDS), STANDING_MAXIMAL_COUNT)
        self.assertEqual(STANDING_MAXIMAL_COUNT, 6)
        self.assertEqual(LOCKED_GK_ISLANDS[0], GRAM_17)
        self.assertEqual(LOCKED_GK_ISLANDS[1], GRAM_15)
        self.assertEqual(LOCKED_GK_ISLANDS[2], GRAM_13)
        self.assertEqual(LOCKED_GK_ISLANDS[3], GRAM_12)
        self.assertEqual(LOCKED_GK_ISLANDS[4], GRAM_10_KV)
        self.assertEqual(LOCKED_GK_ISLANDS[5], GRAM_10_KR)
        self.assertEqual(tuple(row[1] for row in STANDING_MAXIMALS), (17, 15, 13, 12, 10, 10))
        self.assertEqual(STANDING_N9, INVENTORY_LONGEST_TOKENS["G"])
        self.assertEqual(INVENTORY_LONGEST_N["G"], 9)
        self.assertEqual(len(STANDING_N9), 9)
        self.assertEqual(
            STANDING_N9,
            (
                "007",
                "006",
                "124",
                "006",
                "124",
                "098",
                "007",
                "059",
                "002",
            ),
        )
        self.assertEqual(G_8PREFIX, STANDING_N9[:8])
        self.assertEqual(G_8SUFFIX, STANDING_N9[1:])
        self.assertEqual(STANDING_N25[:15], STANDING_N25[:10] + GRAM_15[:5])
        self.assertEqual(STANDING_N25[10:], GRAM_15)
        self.assertEqual(
            tuple(tuple(row[0]) for row in self.survey["tablet_g_k_shared_n8_inventory"]["maximals"]),
            LOCKED_GK_ISLANDS,
        )
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["G"]["longest_tokens"]),
            STANDING_N9,
        )
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["cycle"], 67)
        self.assertEqual(self.survey["tablet_g_k_grkv_maximals"]["cycle"], 78)
        self.assertEqual(self.survey["gk_islands_zero_on_b"]["cycle"], 113)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertNotEqual(STANDING_N9, GRAM_17)
        self.assertNotEqual(STANDING_N9, GRAM_15)
        self.assertNotEqual(STANDING_N9, STANDING_N25)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_loses(self):
        """3 repeating n≥8; 0 substrings; 3 independent. Claim is false."""
        self.assertEqual(len(self.rows), STANDING_REPEATING_COUNT)
        self.assertEqual(self.substring_count, STANDING_SUBSTRING_COUNT)
        self.assertEqual(len(self.independent), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_REPEATING_COUNT, 3)
        self.assertEqual(STANDING_SUBSTRING_COUNT, 0)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 3)
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
        self.assertEqual(max(by_n), STANDING_LONGEST_N)
        self.assertFalse(g_repeating_nge8_all_substrings_of_gk_islands(self.rows))
        self.assertEqual(self.claim_holds, STANDING_G_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS)
        self.assertFalse(STANDING_G_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS)
        self.assertEqual(STANDING_CLAIM, "g_repeating_nge8_all_substrings_of_gk_islands")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_inventory_matches_standing_rows(self):
        """Measured grams, n, freq, substring flag, and sites match the lock."""
        self.assertEqual(self.rows, STANDING_ROWS)
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        for gram, n, freq, is_sub, sites in self.rows:
            self.assertEqual(len(gram), n)
            self.assertGreaterEqual(n, PROFILE_MIN_N)
            self.assertGreaterEqual(freq, 2)
            self.assertEqual(is_gk_island_substring(gram), is_sub)
            self.assertFalse(is_n25_substring(gram))
            self.assertEqual(nge8_sites(gram, self.g_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(matching_islands(gram, STANDING_MAXIMALS), ())
        self.assertIn(STANDING_N9, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 9))
        self.assertTrue(STANDING_N9_IN_SET)
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, (G_8PREFIX, G_8SUFFIX))
        self.assertTrue(STANDING_N25_ALSO_MISSES)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_the_cycle_99_g_n9_family(self):
        """Independent grams are exactly the G 9-gram and its two 8-grams."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertIn(G_8PREFIX, indep_tokens)
        self.assertIn(G_8SUFFIX, indep_tokens)
        self.assertIn(STANDING_N9, indep_tokens)
        self.assertEqual(indep_tokens, (G_8PREFIX, G_8SUFFIX, STANDING_N9))
        self.assertFalse(is_gk_island_substring(G_8PREFIX))
        self.assertFalse(is_gk_island_substring(G_8SUFFIX))
        self.assertFalse(is_gk_island_substring(STANDING_N9))
        self.assertFalse(is_contiguous_substring(STANDING_N9, GRAM_17))
        self.assertFalse(is_contiguous_substring(STANDING_N9, GRAM_15))
        self.assertFalse(is_contiguous_substring(STANDING_N9, GRAM_13))
        self.assertFalse(is_contiguous_substring(STANDING_N9, GRAM_12))
        self.assertFalse(is_contiguous_substring(STANDING_N9, GRAM_10_KV))
        self.assertFalse(is_contiguous_substring(STANDING_N9, GRAM_10_KR))
        self.assertFalse(is_contiguous_substring(STANDING_N9, STANDING_N25))
        for island in LOCKED_GK_ISLANDS:
            self.assertNotIn(island, indep_tokens)
            self.assertEqual(ngram_hit_count(self.by_tablet["G"], island), 1)
        self.assertEqual(len(indep_tokens), 3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_g_hits(self):
        """Independent G sites; Gv=0; K=0; off-G 0 on every vendored tablet."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_g, STANDING_INDEPENDENT_OFF_G)
        self.assertEqual(STANDING_INDEPENDENT_OFF_G, (0,) * 3)
        for (gram, n, freq, sites), hits, off_hits in zip(
            self.independent,
            self.indep_hits_by_tablet,
            self.indep_off_g,
            strict=True,
        ):
            self.assertEqual(nge8_sites(gram, self.g_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("G")], freq)
            self.assertEqual(ngram_hit_count(self.g_sides[SIDE_GR], gram), freq)
            self.assertEqual(ngram_hit_count(self.g_sides[SIDE_GV], gram), 0)
            self.assertEqual(ngram_hit_count(self.by_tablet["K"], gram), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "G":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("G", hits), {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = GR_LINE_NAMES if side == SIDE_GR else GV_LINE_NAMES
                stems = self.g_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_GR)
                self.assertEqual(line, "Gr8")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(tuple(STANDING_INDEPENDENT_GR_HITS), (2,) * 3)
        self.assertEqual(tuple(STANDING_INDEPENDENT_GV_HITS), (0,) * 3)
        self.assertEqual(tuple(STANDING_INDEPENDENT_K_HITS), (0,) * 3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_124_113_67_78_and_w_scoreboards_still_compute(self):
        """Cycle 124 E n≥8, 113 G–K on B, 67/78 islands, and W stay."""
        prior_124 = TestMamariENge8Scoreboard()
        prior_124.setUp()
        prior_124.test_counts_and_hypothesis_all_substrings_loses()
        prior_124.test_survey_matches_computed_lock()
        prior_113 = TestMamariGkIslandsZeroOnBScoreboard()
        prior_113.setUp()
        prior_113.test_six_of_six_are_exact_zero_on_b()
        prior_113.test_survey_matches_computed_lock()
        prior_67 = TestMamariSmallSantiagoLondonSharedN8Scoreboard()
        prior_67.setUp()
        prior_67.test_survey_matches_computed_lock()
        prior_78 = TestMamariSmallSantiagoLondonGrkvMaximalScoreboard()
        prior_78.setUp()
        prior_78.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-125 n≥8 island-substring lock."""
        lock = self.survey["g_repeating_nge8"]
        self.assertEqual(lock["cycle"], 125)
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
        self.assertEqual(tuple(lock["home_tokens9"]), STANDING_N9)
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
                "off_g_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_g_hits"]), STANDING_INDEPENDENT_OFF_G)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n9_in_set"])
        self.assertTrue(lock["n25_also_misses"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["g_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(
            lock["g_repeating_nge8_all_substrings_of_gk_islands"],
            STANDING_G_REPEATING_NGE8_ALL_SUBSTRINGS_OF_GK_ISLANDS,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_maximals_unchanged"])
        self.assertTrue(lock["standing_gk_islands_zero_on_b_unchanged"])
        self.assertTrue(lock["standing_e_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_a_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_c_repeating_nge8_unchanged"])
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
        self.assertEqual(self.survey["gk_islands_zero_on_b"]["cycle"], 113)
        self.assertEqual(self.survey["gk_islands_zero_on_b"]["gk_islands_zero_on_b"], 6)
        self.assertEqual(self.survey["e_repeating_nge8"]["cycle"], 124)
        self.assertFalse(self.survey["e_repeating_nge8"]["e_repeating_nge8_all_substrings_of_n9"])
        self.assertEqual(self.survey["a_repeating_nge8"]["cycle"], 122)
        self.assertFalse(self.survey["a_repeating_nge8"]["a_repeating_nge8_all_substrings_of_n10"])
        self.assertEqual(self.survey["c_repeating_nge8"]["cycle"], 120)
        self.assertFalse(self.survey["c_repeating_nge8"]["c_repeating_nge8_all_substrings_of_n13"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["G"]["longest_n"], 9)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariGNge8ImageSnapshot(unittest.TestCase):
    """Cycle 125 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
