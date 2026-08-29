"""P's repeating n≥6 grams vs the locked P 6-gram.

Cycle 132 text-search lock. Uses already-vendored A–V and the
cycle-99/107 P 6-gram. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
H∩P∩Q n≥8 or H–Q / H–P / Q–P pairwise inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Enumerates every distinct contiguous n≥6 gram with freq≥2 on P
(same per-line Barthel parser as the leak table / P n≥8
scoreboards). For each, whether it is an exact contiguous
substring of 062 006 001 062 006 001 (the 6-gram is a
substring of itself). Hypothesis: no independent repeating n≥6
(every such gram is a 6-gram substring). Measured: 2 repeating
n≥6; 1 is a substring; 1 independent. The independent 6-gram is
021 010 021 010 144 599 at Pv6[19] / Pv7[54] (P-only;
off-P 0). Cycle 129 already locked 0 repeating n≥8 and 0 n=7.
Claim that can lose: p_repeating_nge6_all_substrings_of_p_6gram.
The claim is false (the 6-gram is not the only repeating n≥6).
Do not retune.

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
from tests.test_mamari_h_nge7_scoreboard import (
    INDEPENDENT_PLANT as H_INDEPENDENT_PLANT,
    TestMamariHNge7Scoreboard,
    independent_rows,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_hq_7gram_hq_pairwise_island_substring_scoreboard import (
    TestMamariHq7gramHqPairwiseIslandSubstringScoreboard,
)
from tests.test_mamari_hq_max_n_hpq_island_substring_scoreboard import (
    TestMamariHqMaxNHpqIslandSubstringScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    PR_LINE_NAMES,
    PV_LINE_NAMES,
    SIDE_PR,
    SIDE_PV,
)
from tests.test_mamari_p_max_n_hpq_island_substring_scoreboard import (
    GRAM6,
    TestMamariPMaxNHpqIslandSubstringScoreboard,
)
from tests.test_mamari_p_nge8_scoreboard import (
    TestMamariPNge8Scoreboard,
)
from tests.test_mamari_q_nge7_scoreboard import (
    TestMamariQNge7Scoreboard,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 6
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N6 = GRAM6
STANDING_INDEP_N6 = (
    "021",
    "010",
    "021",
    "010",
    "144",
    "599",
)
INDEPENDENT_PLANT = H_INDEPENDENT_PLANT[:6]
STANDING_REPEATING_COUNT = 2
STANDING_SUBSTRING_COUNT = 1
STANDING_INDEPENDENT_COUNT = 1
STANDING_COUNTS_BY_N = {6: 2}
STANDING_SUBSTRING_BY_N = {6: 1}
STANDING_INDEPENDENT_BY_N = {6: 1}
STANDING_LONGEST_N = 6
STANDING_ROWS = (
    (
        STANDING_N6,
        6,
        2,
        True,
        ((SIDE_PR, "Pr3", 14), (SIDE_PR, "Pr3", 17)),
    ),
    (
        STANDING_INDEP_N6,
        6,
        2,
        False,
        ((SIDE_PV, "Pv6", 19), (SIDE_PV, "Pv7", 54)),
    ),
)
STANDING_INDEPENDENT = tuple(
    (tokens, n, freq, sites)
    for tokens, n, freq, is_sub, sites in STANDING_ROWS
    if not is_sub
)
STANDING_INDEPENDENT_OFF_P = (0,)
STANDING_INDEPENDENT_PR_HITS = (0,)
STANDING_INDEPENDENT_PV_HITS = (2,)
STANDING_INDEPENDENT_H_HITS = (0,)
STANDING_INDEPENDENT_Q_HITS = (0,)
STANDING_KNOWN_DISTINCT = True
STANDING_N6_IN_SET = True
STANDING_INDEP_IN_SET = True
STANDING_N6_IS_SUBSTRING_OF_SELF = True
STANDING_INDEP_IS_SUBSTRING = False
STANDING_CLAIM = "p_repeating_nge6_all_substrings_of_p_6gram"
STANDING_P_REPEATING_NGE6_ALL_SUBSTRINGS_OF_P_6GRAM = False
STANDING_RESULT = "p_repeating_nge6"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def repeating_nge6_grams(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
) -> tuple[tuple[tuple[str, ...], int, int], ...]:
    """Distinct contiguous n≥6 grams with freq≥2. Search only."""
    rows: list[tuple[tuple[str, ...], int, int]] = []
    n = PROFILE_MIN_N
    while True:
        found = analyzer.extract_ngrams(lines, n=n, min_frequency=2)
        if not found:
            break
        rows.extend((gram, n, freq) for gram, freq in found)
        n += 1
    return tuple(rows)


def nge6_sites(
    gram: tuple[str, ...],
    p_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Pr then Pv. Search only."""
    hits = named_side_hits(p_sides[SIDE_PR], PR_LINE_NAMES, SIDE_PR, gram)
    hits += named_side_hits(p_sides[SIDE_PV], PV_LINE_NAMES, SIDE_PV, gram)
    return tuple(site_tuple(hit) for hit in hits)


def is_p_6gram_substring(
    gram: tuple[str, ...],
    n6: tuple[str, ...] = STANDING_N6,
) -> bool:
    """True iff gram is an exact contiguous run inside the P 6-gram."""
    return is_contiguous_substring(gram, n6)


def p_repeating_nge6_all_substrings_of_p_6gram(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥6 is a 6-gram substring.

    The 6-gram is a substring of itself. An empty inventory is
    false here (the home 6-gram must be in the repeating set).
    """
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_p_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off P. Counts only."""
    return sum(leaks_from_hits("P", hits, tablets).values())


class TestPNge6Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted non-6-gram 6-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = STANDING_N6
        planted = INDEPENDENT_PLANT
        measured_indep = STANDING_INDEP_N6
        self.assertNotEqual(home, planted)
        self.assertNotEqual(home, measured_indep)
        self.assertNotEqual(planted, measured_indep)
        self.assertEqual(len(home), 6)
        self.assertEqual(len(planted), 6)
        self.assertEqual(len(measured_indep), 6)
        self.assertTrue(is_p_6gram_substring(home))
        self.assertTrue(is_p_6gram_substring(home[:6]))
        self.assertTrue(is_contiguous_substring(home, home))
        self.assertFalse(is_p_6gram_substring(planted))
        self.assertFalse(is_p_6gram_substring(measured_indep))
        self.assertFalse(is_p_6gram_substring(home + ("999",)))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge6_grams(once_each, analyzer), ())
        self.assertFalse(p_repeating_nge6_all_substrings_of_p_6gram(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_nge6_grams(twice_home, analyzer)
        self.assertGreaterEqual(len(home_only), 1)
        self.assertIn((home, 6, 2), home_only)
        home_rows = tuple(
            (gram, n, freq, is_p_6gram_substring(gram), ())
            for gram, n, freq in home_only
        )
        self.assertTrue(p_repeating_nge6_all_substrings_of_p_6gram(home_rows))
        self.assertEqual(independent_rows(home_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge6_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_p_6gram_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(p_repeating_nge6_all_substrings_of_p_6gram(both_rows))
        self.assertIn(planted, tuple(gram for gram, n, _freq in both if n == 6))
        twice_measured = [
            list(home),
            list(home),
            list(measured_indep),
            list(measured_indep),
        ]
        measured_both = repeating_nge6_grams(twice_measured, analyzer)
        measured_rows = tuple(
            (gram, n, freq, is_p_6gram_substring(gram), ())
            for gram, n, freq in measured_both
        )
        self.assertFalse(p_repeating_nge6_all_substrings_of_p_6gram(measured_rows))
        self.assertIn(measured_indep, tuple(gram for gram, n, _freq in measured_both if n == 6))
        gapped = [list(home[:3]) + ["999"] + list(home[3:]), list(home)]
        self.assertEqual(repeating_nge6_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "p_repeating_nge6_all_substrings_of_p_6gram")
        self.assertFalse(STANDING_P_REPEATING_NGE6_ALL_SUBSTRINGS_OF_P_6GRAM)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 1)
        self.assertFalse(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariPNge6Scoreboard(unittest.TestCase):
    """Cited-fixture P repeating n≥6 vs the P 6-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.p_sides = load_q_h_p_sides()
        measured = repeating_nge6_grams(self.by_tablet["P"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_p_6gram_substring(gram),
                nge6_sites(gram, self.p_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = p_repeating_nge6_all_substrings_of_p_6gram(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_p = tuple(
            off_p_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_99_107_n6_not_invented(self):
        """P 6-gram is a prior lock; the independent 6-gram is measured."""
        self.assertEqual(STANDING_N6, INVENTORY_LONGEST_TOKENS["P"])
        self.assertEqual(INVENTORY_LONGEST_N["P"], 6)
        self.assertEqual(len(STANDING_N6), 6)
        self.assertEqual(len(STANDING_INDEP_N6), 6)
        self.assertEqual(
            STANDING_N6,
            ("062", "006", "001", "062", "006", "001"),
        )
        self.assertEqual(
            STANDING_INDEP_N6,
            ("021", "010", "021", "010", "144", "599"),
        )
        self.assertTrue(is_p_6gram_substring(STANDING_N6))
        self.assertTrue(is_contiguous_substring(STANDING_N6, STANDING_N6))
        self.assertTrue(STANDING_N6_IS_SUBSTRING_OF_SELF)
        self.assertFalse(is_p_6gram_substring(STANDING_INDEP_N6))
        self.assertFalse(is_contiguous_substring(STANDING_INDEP_N6, STANDING_N6))
        self.assertFalse(STANDING_INDEP_IS_SUBSTRING)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["P"]["longest_tokens"]),
            STANDING_N6,
        )
        self.assertEqual(
            tuple(self.survey["p_max_n_hpq_island_substring"]["tokens6"]),
            STANDING_N6,
        )
        self.assertEqual(self.survey["p_max_n_hpq_island_substring"]["cycle"], 107)
        self.assertEqual(self.survey["p_repeating_nge8"]["cycle"], 129)
        self.assertEqual(self.survey["q_repeating_nge7"]["cycle"], 131)
        self.assertEqual(self.survey["h_repeating_nge7"]["cycle"], 127)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertNotEqual(STANDING_N6, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_INDEP_N6, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_N6, STANDING_INDEP_N6)
        self.assertFalse(is_p_6gram_substring(INDEPENDENT_PLANT))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_loses(self):
        """2 repeating n≥6; 1 substring; 1 independent. Claim is false."""
        self.assertEqual(len(self.rows), STANDING_REPEATING_COUNT)
        self.assertEqual(self.substring_count, STANDING_SUBSTRING_COUNT)
        self.assertEqual(len(self.independent), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_REPEATING_COUNT, 2)
        self.assertEqual(STANDING_SUBSTRING_COUNT, 1)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 1)
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
        self.assertEqual(STANDING_LONGEST_N, 6)
        self.assertFalse(p_repeating_nge6_all_substrings_of_p_6gram(self.rows))
        self.assertEqual(self.claim_holds, STANDING_P_REPEATING_NGE6_ALL_SUBSTRINGS_OF_P_6GRAM)
        self.assertFalse(STANDING_P_REPEATING_NGE6_ALL_SUBSTRINGS_OF_P_6GRAM)
        self.assertEqual(STANDING_CLAIM, "p_repeating_nge6_all_substrings_of_p_6gram")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        n7 = self.analyzer.extract_ngrams(self.by_tablet["P"], n=7, min_frequency=2)
        self.assertEqual(n7, [])
        n8 = self.analyzer.extract_ngrams(self.by_tablet["P"], n=8, min_frequency=2)
        self.assertEqual(n8, [])
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
            self.assertEqual(is_p_6gram_substring(gram), is_sub)
            self.assertEqual(nge6_sites(gram, self.p_sides), sites)
            self.assertEqual(len(sites), freq)
        self.assertIn(STANDING_N6, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6))
        self.assertIn(STANDING_INDEP_N6, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6))
        self.assertTrue(STANDING_N6_IN_SET)
        self.assertTrue(STANDING_INDEP_IN_SET)
        sixgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6)
        self.assertEqual(sixgrams, (STANDING_N6, STANDING_INDEP_N6))
        sevengrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 7)
        self.assertEqual(sevengrams, ())
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_the_measured_p_only_6gram(self):
        """Independent remainder is exactly 021 010 021 010 144 599."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertEqual(indep_tokens, (STANDING_INDEP_N6,))
        self.assertNotIn(STANDING_N6, indep_tokens)
        self.assertTrue(is_p_6gram_substring(STANDING_N6))
        self.assertFalse(is_p_6gram_substring(STANDING_INDEP_N6))
        self.assertFalse(is_p_6gram_substring(INDEPENDENT_PLANT))
        self.assertNotIn(INDEPENDENT_PLANT, indep_tokens)
        self.assertFalse(is_contiguous_substring(STANDING_INDEP_N6, STANDING_N6))
        self.assertEqual(len(indep_tokens), 1)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_p_hits(self):
        """Independent P sites span Pv only; H=0; Q=0; off-P 0 on every tablet."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_p, STANDING_INDEPENDENT_OFF_P)
        self.assertEqual(STANDING_INDEPENDENT_OFF_P, (0,))
        for (gram, n, freq, sites), hits, off_hits in zip(
            self.independent,
            self.indep_hits_by_tablet,
            self.indep_off_p,
            strict=True,
        ):
            self.assertEqual(nge6_sites(gram, self.p_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("P")], freq)
            self.assertEqual(ngram_hit_count(self.p_sides[SIDE_PR], gram), 0)
            self.assertEqual(ngram_hit_count(self.p_sides[SIDE_PV], gram), 2)
            self.assertEqual(ngram_hit_count(self.by_tablet["H"], gram), 0)
            self.assertEqual(ngram_hit_count(self.by_tablet["Q"], gram), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "P":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("P", hits), {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = PR_LINE_NAMES if side == SIDE_PR else PV_LINE_NAMES
                stems = self.p_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
        self.assertEqual(
            nge6_sites(STANDING_INDEP_N6, self.p_sides),
            ((SIDE_PV, "Pv6", 19), (SIDE_PV, "Pv7", 54)),
        )
        self.assertEqual(tuple(STANDING_INDEPENDENT_PR_HITS), (0,))
        self.assertEqual(tuple(STANDING_INDEPENDENT_PV_HITS), (2,))
        self.assertEqual(tuple(STANDING_INDEPENDENT_H_HITS), (0,))
        self.assertEqual(tuple(STANDING_INDEPENDENT_Q_HITS), (0,))
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(ngram_hit_count(self.p_sides[SIDE_PR], STANDING_N6), 2)
        self.assertEqual(ngram_hit_count(self.p_sides[SIDE_PV], STANDING_N6), 0)
        self.assertEqual(ngram_hit_count(self.by_tablet["H"], STANDING_N6), 2)
        self.assertEqual(ngram_hit_count(self.by_tablet["P"], STANDING_N6), 2)
        self.assertEqual(ngram_hit_count(self.by_tablet["Q"], STANDING_N6), 2)
        self.assertEqual(
            nge6_sites(STANDING_N6, self.p_sides),
            ((SIDE_PR, "Pr3", 14), (SIDE_PR, "Pr3", 17)),
        )
        home_hits = tablet_hit_counts(self.by_tablet, STANDING_N6, VENDORED_TABLETS)
        self.assertEqual(home_hits[VENDORED_TABLETS.index("H")], 2)
        self.assertEqual(home_hits[VENDORED_TABLETS.index("P")], 2)
        self.assertEqual(home_hits[VENDORED_TABLETS.index("Q")], 2)
        self.assertEqual(leaks_from_hits("P", home_hits), {"H": 2, "Q": 2})
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_131_129_127_107_108_109_and_w_scoreboards_still_compute(self):
        """Cycle 131 Q n≥7, 129 P n≥8, 127 H n≥7, 107 P 6-gram, 108/109, and W stay."""
        prior_131 = TestMamariQNge7Scoreboard()
        prior_131.setUp()
        prior_131.test_counts_and_hypothesis_all_substrings_loses()
        prior_131.test_survey_matches_computed_lock()
        prior_129 = TestMamariPNge8Scoreboard()
        prior_129.setUp()
        prior_129.test_counts_and_hypothesis_all_substrings_holds()
        prior_129.test_survey_matches_computed_lock()
        prior_127 = TestMamariHNge7Scoreboard()
        prior_127.setUp()
        prior_127.test_counts_and_hypothesis_all_substrings_holds()
        prior_127.test_survey_matches_computed_lock()
        prior_107 = TestMamariPMaxNHpqIslandSubstringScoreboard()
        prior_107.setUp()
        prior_107.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-132 n≥6 6-gram-substring lock."""
        lock = self.survey["p_repeating_nge6"]
        self.assertEqual(lock["cycle"], 132)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(tuple(lock["home_tokens6"]), STANDING_N6)
        self.assertEqual(tuple(lock["independent_tokens6"]), STANDING_INDEP_N6)
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
                "off_p_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_p_hits"]), STANDING_INDEPENDENT_OFF_P)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n6_in_set"])
        self.assertTrue(lock["indep_in_set"])
        self.assertTrue(lock["n6_is_substring_of_self"])
        self.assertFalse(lock["indep_is_substring"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["p_repeating_nge6_all_substrings_of_p_6gram"])
        self.assertEqual(
            lock["p_repeating_nge6_all_substrings_of_p_6gram"],
            STANDING_P_REPEATING_NGE6_ALL_SUBSTRINGS_OF_P_6GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_p_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge7_unchanged"])
        self.assertTrue(lock["standing_h_repeating_nge7_unchanged"])
        self.assertTrue(lock["standing_p_max_n_hpq_island_substring_unchanged"])
        self.assertTrue(lock["standing_hq_max_n_hpq_island_substring_unchanged"])
        self.assertTrue(lock["standing_hq_7gram_hq_pairwise_island_substring_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_h_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_k_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["p_repeating_nge8"]["cycle"], 129)
        self.assertEqual(self.survey["p_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["p_repeating_nge8"]["p_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["q_repeating_nge7"]["cycle"], 131)
        self.assertEqual(self.survey["q_repeating_nge7"]["repeating_count"], 2)
        self.assertFalse(self.survey["q_repeating_nge7"]["q_repeating_nge7_all_substrings_of_hq_7gram"])
        self.assertEqual(self.survey["h_repeating_nge7"]["cycle"], 127)
        self.assertEqual(self.survey["h_repeating_nge7"]["repeating_count"], 1)
        self.assertTrue(self.survey["h_repeating_nge7"]["h_repeating_nge7_all_substrings_of_hq_7gram"])
        self.assertEqual(self.survey["p_max_n_hpq_island_substring"]["cycle"], 107)
        self.assertTrue(
            self.survey["p_max_n_hpq_island_substring"]["p_max_n_is_hpq_island_substring"]
        )
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
        self.assertEqual(self.survey["q_repeating_nge8"]["cycle"], 128)
        self.assertEqual(self.survey["q_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["q_repeating_nge8"]["q_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["h_repeating_nge8"]["cycle"], 126)
        self.assertEqual(self.survey["h_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["h_repeating_nge8"]["h_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["k_repeating_nge8"]["cycle"], 130)
        self.assertEqual(self.survey["k_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["k_repeating_nge8"]["k_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["P"]["longest_n"], 6)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariPNge6ImageSnapshot(unittest.TestCase):
    """Cycle 132 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
