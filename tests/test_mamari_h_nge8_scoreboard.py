"""H's repeating n≥8 grams vs locked H∩P∩Q island sequences.

Cycle 126 text-search lock. Uses already-vendored A–V and the
cycle-71 five maximal H∩P∩Q islands. Does not vendor a new
tablet. Does not scrape X. W has no Barthel (cycle 100); skip W.
Does not redo H∩P∩Q n≥8 or H–Q / H–P pairwise inventories.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Enumerates every distinct contiguous n≥8 gram with freq≥2 on H
(same per-line Barthel parser as the leak table / H∩P∩Q island
scoreboards). For each, whether it is an exact contiguous
substring of at least one locked H∩P∩Q triple island.
Hypothesis: no H-local (or pairwise-only) repeating n≥8 (every
such gram is a triple-island substring). Measured: 0 repeating
n≥8; 0 are substrings; 0 independent. H's longest repeating
gram remains the cycle-99/108 H/Q 7-gram. The five triple
islands are each freq 1 on H, so they do not count as
H-repeats. Claim that can lose:
h_repeating_nge8_all_substrings_of_hpq_islands. The claim is
true (empty repeating set; no independent remainder). Do not
retune.

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
from tests.test_mamari_g_nge8_scoreboard import (
    TestMamariGNge8Scoreboard,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_hpq_island_off_hpq_scoreboard import (
    LOCKED_ISLANDS,
)
from tests.test_mamari_hpq_triple_n8_scoreboard import (
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    TestMamariHpqTripleN8Scoreboard,
)
from tests.test_mamari_hq_7gram_hq_pairwise_island_substring_scoreboard import (
    TestMamariHq7gramHqPairwiseIslandSubstringScoreboard,
)
from tests.test_mamari_hq_max_n_hpq_island_substring_scoreboard import (
    GRAM7,
    TestMamariHqMaxNHpqIslandSubstringScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    HR_LINE_NAMES,
    HV_LINE_NAMES,
    SIDE_HR,
    SIDE_HV,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 8
HYPOTHESIS_INDEPENDENT_EMPTY = True
LOCKED_HPQ_ISLANDS = tuple(
    tokens for tokens, _n, _fh, _fp, _fq, _hs, _ps, _qs in STANDING_MAXIMALS
)
STANDING_N7 = GRAM7
ISLAND_8GRAM = LOCKED_HPQ_ISLANDS[3]
ISLAND_8VERSO = LOCKED_HPQ_ISLANDS[4]
ISLAND_12_PREFIX8 = LOCKED_HPQ_ISLANDS[0][:8]
INDEPENDENT_PLANT = (
    "007",
    "006",
    "124",
    "006",
    "124",
    "098",
    "007",
    "059",
)
STANDING_REPEATING_COUNT = 0
STANDING_SUBSTRING_COUNT = 0
STANDING_INDEPENDENT_COUNT = 0
STANDING_COUNTS_BY_N = {}
STANDING_SUBSTRING_BY_N = {}
STANDING_INDEPENDENT_BY_N = {}
STANDING_LONGEST_N = 0
STANDING_ROWS = ()
STANDING_INDEPENDENT = ()
STANDING_INDEPENDENT_OFF_H = ()
STANDING_INDEPENDENT_HR_HITS = ()
STANDING_INDEPENDENT_HV_HITS = ()
STANDING_INDEPENDENT_P_HITS = ()
STANDING_INDEPENDENT_Q_HITS = ()
STANDING_ISLAND_FREQ_ON_H = (1, 1, 1, 1, 1)
STANDING_KNOWN_DISTINCT = True
STANDING_N7_IN_SET = False
STANDING_ISLANDS_FREQ1_ON_H = True
STANDING_CLAIM = "h_repeating_nge8_all_substrings_of_hpq_islands"
STANDING_H_REPEATING_NGE8_ALL_SUBSTRINGS_OF_HPQ_ISLANDS = True
STANDING_RESULT = "h_repeating_nge8"
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
    h_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Hr then Hv. Search only."""
    hits = named_side_hits(h_sides[SIDE_HR], HR_LINE_NAMES, SIDE_HR, gram)
    hits += named_side_hits(h_sides[SIDE_HV], HV_LINE_NAMES, SIDE_HV, gram)
    return tuple(site_tuple(hit) for hit in hits)


def matching_hpq_islands(
    gram: tuple[str, ...],
    maximals: tuple = STANDING_MAXIMALS,
) -> tuple[tuple, ...]:
    """Locked triple islands whose tokens contain gram as a contiguous run."""
    rows = []
    for tokens, n, _fh, _fp, _fq, h_site, p_site, q_site in maximals:
        if is_contiguous_substring(gram, tokens):
            rows.append((tokens, n, h_site, p_site, q_site))
    return tuple(rows)


def is_hpq_island_substring(
    gram: tuple[str, ...],
    maximals: tuple = STANDING_MAXIMALS,
) -> bool:
    """True iff gram is an exact contiguous run inside a locked island."""
    return bool(matching_hpq_islands(gram, maximals))


def independent_rows(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Rows that are not exact contiguous substrings of any island."""
    return tuple(
        (tokens, n, freq, sites)
        for tokens, n, freq, is_sub, sites in rows
        if not is_sub
    )


def h_repeating_nge8_all_substrings_of_hpq_islands(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥8 is an H∩P∩Q island substring.

    The empty inventory is true: H has no repeating n≥8, so none
    fail the island-substring test (no H-local remainder).
    """
    return all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_h_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off H. Counts only."""
    return sum(leaks_from_hits("H", hits, tablets).values())


class TestHNge8Helpers(unittest.TestCase):
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
        self.assertFalse(is_hpq_island_substring(home))
        self.assertTrue(is_hpq_island_substring(planted))
        self.assertTrue(is_hpq_island_substring(LOCKED_HPQ_ISLANDS[0]))
        self.assertTrue(is_hpq_island_substring(ISLAND_12_PREFIX8))
        self.assertTrue(is_hpq_island_substring(ISLAND_8VERSO))
        self.assertTrue(is_hpq_island_substring(LOCKED_HPQ_ISLANDS[1][:8]))
        self.assertFalse(is_hpq_island_substring(home + ("999",)))
        self.assertFalse(is_hpq_island_substring(STANDING_N7))
        self.assertEqual(len(STANDING_N7), 7)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge8_grams(once_each, analyzer), ())
        self.assertTrue(h_repeating_nge8_all_substrings_of_hpq_islands(()))
        twice_island = [list(planted), list(planted)]
        island_only = repeating_nge8_grams(twice_island, analyzer)
        self.assertGreaterEqual(len(island_only), 1)
        self.assertIn((planted, 8, 2), island_only)
        island_rows = tuple(
            (gram, n, freq, is_hpq_island_substring(gram), ())
            for gram, n, freq in island_only
        )
        self.assertTrue(h_repeating_nge8_all_substrings_of_hpq_islands(island_rows))
        self.assertEqual(independent_rows(island_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge8_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_hpq_island_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(h_repeating_nge8_all_substrings_of_hpq_islands(both_rows))
        self.assertIn(home, tuple(gram for gram, n, _freq in both if n == 8))
        gapped = [list(home[:4]) + ["999"] + list(home[4:]), list(home)]
        self.assertEqual(repeating_nge8_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "h_repeating_nge8_all_substrings_of_hpq_islands")
        self.assertTrue(STANDING_H_REPEATING_NGE8_ALL_SUBSTRINGS_OF_HPQ_ISLANDS)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHNge8Scoreboard(unittest.TestCase):
    """Cited-fixture H repeating n≥8 vs H∩P∩Q islands. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.h_sides = load_q_h_p_sides()
        measured = repeating_nge8_grams(self.by_tablet["H"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_hpq_island_substring(gram),
                nge8_sites(gram, self.h_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = h_repeating_nge8_all_substrings_of_hpq_islands(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_h = tuple(
            off_h_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_71_islands_and_cycle_99_n7_not_invented(self):
        """H∩P∩Q islands and the H/Q 7-gram are prior locks."""
        self.assertEqual(len(LOCKED_HPQ_ISLANDS), STANDING_MAXIMAL_COUNT)
        self.assertEqual(STANDING_MAXIMAL_COUNT, 5)
        self.assertEqual(LOCKED_HPQ_ISLANDS, LOCKED_ISLANDS)
        self.assertEqual(
            LOCKED_HPQ_ISLANDS[0],
            ("002", "144", "002", "662", "680", "005", "010", "005", "052", "022", "243", "001"),
        )
        self.assertEqual(
            LOCKED_HPQ_ISLANDS[1],
            ("062", "006", "001", "062", "006", "001", "062", "006", "001", "020", "064"),
        )
        self.assertEqual(
            LOCKED_HPQ_ISLANDS[2],
            ("005", "002", "041", "220", "009", "220", "009", "440", "440", "440"),
        )
        self.assertEqual(
            LOCKED_HPQ_ISLANDS[3],
            ("005", "099", "011", "007", "004", "600", "522", "606"),
        )
        self.assertEqual(
            LOCKED_HPQ_ISLANDS[4],
            ("301", "004", "064", "004", "064", "209", "081", "050"),
        )
        self.assertEqual(tuple(row[1] for row in STANDING_MAXIMALS), (12, 11, 10, 8, 8))
        self.assertEqual(STANDING_N7, INVENTORY_LONGEST_TOKENS["H"])
        self.assertEqual(INVENTORY_LONGEST_N["H"], 7)
        self.assertEqual(len(STANDING_N7), 7)
        self.assertEqual(
            STANDING_N7,
            ("072", "450", "052", "551", "003", "600", "003"),
        )
        self.assertEqual(
            tuple(tuple(row[0]) for row in self.survey["tablet_h_p_q_triple_n8_inventory"]["maximals"]),
            LOCKED_HPQ_ISLANDS,
        )
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["H"]["longest_tokens"]),
            STANDING_N7,
        )
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertEqual(self.survey["hq_max_n_hpq_island_substring"]["cycle"], 108)
        self.assertEqual(self.survey["hq_7gram_hq_pairwise_island_substring"]["cycle"], 109)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertNotEqual(STANDING_N7, LOCKED_HPQ_ISLANDS[0])
        self.assertNotEqual(STANDING_N7, LOCKED_HPQ_ISLANDS[3])
        self.assertFalse(is_hpq_island_substring(STANDING_N7))
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
        self.assertTrue(h_repeating_nge8_all_substrings_of_hpq_islands(self.rows))
        self.assertEqual(self.claim_holds, STANDING_H_REPEATING_NGE8_ALL_SUBSTRINGS_OF_HPQ_ISLANDS)
        self.assertTrue(STANDING_H_REPEATING_NGE8_ALL_SUBSTRINGS_OF_HPQ_ISLANDS)
        self.assertEqual(STANDING_CLAIM, "h_repeating_nge8_all_substrings_of_hpq_islands")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        n7 = self.analyzer.extract_ngrams(self.by_tablet["H"], n=7, min_frequency=2)
        self.assertEqual(n7, [(STANDING_N7, 2)])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_inventory_matches_standing_rows(self):
        """Measured grams, n, freq, substring flag, and sites match the lock."""
        self.assertEqual(self.rows, STANDING_ROWS)
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_ROWS, ())
        self.assertFalse(STANDING_N7_IN_SET)
        self.assertNotIn(STANDING_N7, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 7))
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_empty(self):
        """No H-local or pairwise-only repeating n≥8 remainder."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertEqual(indep_tokens, ())
        self.assertNotIn(STANDING_N7, indep_tokens)
        self.assertFalse(is_hpq_island_substring(STANDING_N7))
        self.assertFalse(is_contiguous_substring(STANDING_N7, LOCKED_HPQ_ISLANDS[0]))
        self.assertFalse(is_contiguous_substring(STANDING_N7, LOCKED_HPQ_ISLANDS[1]))
        self.assertFalse(is_contiguous_substring(STANDING_N7, LOCKED_HPQ_ISLANDS[2]))
        self.assertFalse(is_contiguous_substring(STANDING_N7, LOCKED_HPQ_ISLANDS[3]))
        self.assertFalse(is_contiguous_substring(STANDING_N7, LOCKED_HPQ_ISLANDS[4]))
        for island in LOCKED_HPQ_ISLANDS:
            self.assertNotIn(island, indep_tokens)
            self.assertEqual(ngram_hit_count(self.by_tablet["H"], island), 1)
            self.assertEqual(ngram_hit_count(self.by_tablet["P"], island), 1)
            self.assertEqual(ngram_hit_count(self.by_tablet["Q"], island), 1)
        self.assertEqual(len(indep_tokens), 0)
        self.assertTrue(STANDING_ISLANDS_FREQ1_ON_H)
        self.assertEqual(STANDING_ISLAND_FREQ_ON_H, (1,) * STANDING_MAXIMAL_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_h_hits(self):
        """Empty independent set; no off-H remainder to count."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_h, STANDING_INDEPENDENT_OFF_H)
        self.assertEqual(STANDING_INDEPENDENT_OFF_H, ())
        self.assertEqual(self.indep_hits_by_tablet, ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_HR_HITS), ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_HV_HITS), ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_P_HITS), ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_Q_HITS), ())
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(ngram_hit_count(self.h_sides[SIDE_HR], STANDING_N7), 2)
        self.assertEqual(ngram_hit_count(self.h_sides[SIDE_HV], STANDING_N7), 0)
        self.assertEqual(
            nge8_sites(STANDING_N7, self.h_sides),
            ((SIDE_HR, "Hr3", 63), (SIDE_HR, "Hr3", 72)),
        )
        self.assertEqual(
            nge8_sites(ISLAND_8GRAM, self.h_sides),
            ((SIDE_HR, "Hr7", 47),),
        )
        self.assertEqual(
            nge8_sites(ISLAND_8VERSO, self.h_sides),
            ((SIDE_HV, "Hv2", 32),),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_125_71_108_109_and_w_scoreboards_still_compute(self):
        """Cycle 125 G n≥8, 71 H∩P∩Q, 108/109 H/Q 7-gram, and W stay."""
        prior_125 = TestMamariGNge8Scoreboard()
        prior_125.setUp()
        prior_125.test_counts_and_hypothesis_all_substrings_loses()
        prior_125.test_survey_matches_computed_lock()
        prior_71 = TestMamariHpqTripleN8Scoreboard()
        prior_71.setUp()
        prior_71.test_survey_matches_computed_lock()
        prior_108 = TestMamariHqMaxNHpqIslandSubstringScoreboard()
        prior_108.setUp()
        prior_108.test_survey_matches_computed_lock()
        prior_109 = TestMamariHq7gramHqPairwiseIslandSubstringScoreboard()
        prior_109.setUp()
        prior_109.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-126 n≥8 island-substring lock."""
        lock = self.survey["h_repeating_nge8"]
        self.assertEqual(lock["cycle"], 126)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(lock["island_count"], STANDING_MAXIMAL_COUNT)
        self.assertEqual(tuple(lock["island_ns"]), (12, 11, 10, 8, 8))
        self.assertEqual(
            tuple(tuple(tokens) for tokens in lock["islands"]),
            LOCKED_HPQ_ISLANDS,
        )
        self.assertEqual(tuple(lock["home_tokens7"]), STANDING_N7)
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
                "off_h_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_h_hits"]), STANDING_INDEPENDENT_OFF_H)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertFalse(lock["n7_in_set"])
        self.assertTrue(lock["islands_freq1_on_h"])
        self.assertEqual(tuple(lock["island_freq_on_h"]), STANDING_ISLAND_FREQ_ON_H)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["h_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(
            lock["h_repeating_nge8_all_substrings_of_hpq_islands"],
            STANDING_H_REPEATING_NGE8_ALL_SUBSTRINGS_OF_HPQ_ISLANDS,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hq_max_n_hpq_island_substring_unchanged"])
        self.assertTrue(lock["standing_hq_7gram_hq_pairwise_island_substring_unchanged"])
        self.assertTrue(lock["standing_g_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_e_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["maximal_count"], 5)
        self.assertTrue(self.survey["tablet_h_p_q_triple_n8_inventory"]["islands_disjoint"])
        self.assertEqual(self.survey["hq_max_n_hpq_island_substring"]["cycle"], 108)
        self.assertFalse(
            self.survey["hq_max_n_hpq_island_substring"]["hq_max_n_is_hpq_island_substring"]
        )
        self.assertEqual(self.survey["hq_7gram_hq_pairwise_island_substring"]["cycle"], 109)
        self.assertTrue(
            self.survey["hq_7gram_hq_pairwise_island_substring"][
                "hq_7gram_is_hq_pairwise_island_substring"
            ]
        )
        self.assertEqual(self.survey["g_repeating_nge8"]["cycle"], 125)
        self.assertFalse(self.survey["g_repeating_nge8"]["g_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(self.survey["e_repeating_nge8"]["cycle"], 124)
        self.assertFalse(self.survey["e_repeating_nge8"]["e_repeating_nge8_all_substrings_of_n9"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["H"]["longest_n"], 7)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHNge8ImageSnapshot(unittest.TestCase):
    """Cycle 126 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
