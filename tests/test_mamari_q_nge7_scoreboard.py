"""Q's repeating n≥7 grams vs the locked H/Q 7-gram.

Cycle 131 text-search lock. Uses already-vendored A–V and the
cycle-99/108 H/Q 7-gram. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
H∩P∩Q n≥8 or H–Q / H–P pairwise inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Enumerates every distinct contiguous n≥7 gram with freq≥2 on Q
(same per-line Barthel parser as the leak table / H n≥7
scoreboards). For each, whether it is an exact contiguous
substring of 072 450 052 551 003 600 003 (the 7-gram is a
substring of itself). Hypothesis: no independent repeating n≥7
(every such gram is a 7-gram substring). Measured: 2 repeating
n≥7; 1 is a substring; 1 independent. The independent 7-gram is
003 028 095 073 001 057 001 at Qr8[44] / Qv3[27] (Q-only;
off-Q 0). Cycle 128 already locked 0 repeating n≥8. Claim that
can lose: q_repeating_nge7_all_substrings_of_hq_7gram. The
claim is false (H vs Q n≥7 asymmetry: H has 0 independent, Q
has 1). Do not retune.

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
    INDEPENDENT_PLANT,
    STANDING_INDEPENDENT_COUNT as H_STANDING_INDEPENDENT_COUNT,
    STANDING_REPEATING_COUNT as H_STANDING_REPEATING_COUNT,
    STANDING_SUBSTRING_COUNT as H_STANDING_SUBSTRING_COUNT,
    TestMamariHNge7Scoreboard,
    independent_rows,
    is_hq_7gram_substring,
    repeating_nge7_grams,
)
from tests.test_mamari_h_nge8_scoreboard import (
    TestMamariHNge8Scoreboard,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
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
from tests.test_mamari_k_nge8_scoreboard import (
    TestMamariKNge8Scoreboard,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_q_nge8_scoreboard import (
    TestMamariQNge8Scoreboard,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides,
)
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    QR_LINE_NAMES,
    QV_LINE_NAMES,
    SIDE_QR,
    SIDE_QV,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 7
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N7 = GRAM7
STANDING_INDEP_N7 = (
    "003",
    "028",
    "095",
    "073",
    "001",
    "057",
    "001",
)
STANDING_REPEATING_COUNT = 2
STANDING_SUBSTRING_COUNT = 1
STANDING_INDEPENDENT_COUNT = 1
STANDING_COUNTS_BY_N = {7: 2}
STANDING_SUBSTRING_BY_N = {7: 1}
STANDING_INDEPENDENT_BY_N = {7: 1}
STANDING_LONGEST_N = 7
STANDING_ROWS = (
    (
        STANDING_N7,
        7,
        2,
        True,
        ((SIDE_QR, "Qr3", 43), (SIDE_QR, "Qr3", 52)),
    ),
    (
        STANDING_INDEP_N7,
        7,
        2,
        False,
        ((SIDE_QR, "Qr8", 44), (SIDE_QV, "Qv3", 27)),
    ),
)
STANDING_INDEPENDENT = tuple(
    (tokens, n, freq, sites)
    for tokens, n, freq, is_sub, sites in STANDING_ROWS
    if not is_sub
)
STANDING_INDEPENDENT_OFF_Q = (0,)
STANDING_INDEPENDENT_QR_HITS = (1,)
STANDING_INDEPENDENT_QV_HITS = (1,)
STANDING_INDEPENDENT_H_HITS = (0,)
STANDING_INDEPENDENT_P_HITS = (0,)
STANDING_KNOWN_DISTINCT = True
STANDING_N7_IN_SET = True
STANDING_INDEP_IN_SET = True
STANDING_N7_IS_SUBSTRING_OF_SELF = True
STANDING_INDEP_IS_SUBSTRING = False
STANDING_H_REPEATING_COUNT = H_STANDING_REPEATING_COUNT
STANDING_H_SUBSTRING_COUNT = H_STANDING_SUBSTRING_COUNT
STANDING_H_INDEPENDENT_COUNT = H_STANDING_INDEPENDENT_COUNT
STANDING_H_Q_NGE7_ASYMMETRY = True
STANDING_CLAIM = "q_repeating_nge7_all_substrings_of_hq_7gram"
STANDING_Q_REPEATING_NGE7_ALL_SUBSTRINGS_OF_HQ_7GRAM = False
STANDING_RESULT = "q_repeating_nge7"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def nge7_sites(
    gram: tuple[str, ...],
    q_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Qr then Qv. Search only."""
    hits = named_side_hits(q_sides[SIDE_QR], QR_LINE_NAMES, SIDE_QR, gram)
    hits += named_side_hits(q_sides[SIDE_QV], QV_LINE_NAMES, SIDE_QV, gram)
    return tuple(site_tuple(hit) for hit in hits)


def q_repeating_nge7_all_substrings_of_hq_7gram(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥7 is a 7-gram substring.

    The 7-gram is a substring of itself. An empty inventory is
    false here (the home 7-gram must be in the repeating set).
    """
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_q_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off Q. Counts only."""
    return sum(leaks_from_hits("Q", hits, tablets).values())


class TestQNge7Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted non-7-gram 7-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = STANDING_N7
        planted = INDEPENDENT_PLANT
        measured_indep = STANDING_INDEP_N7
        self.assertNotEqual(home, planted)
        self.assertNotEqual(home, measured_indep)
        self.assertNotEqual(planted, measured_indep)
        self.assertEqual(len(home), 7)
        self.assertEqual(len(planted), 7)
        self.assertEqual(len(measured_indep), 7)
        self.assertTrue(is_hq_7gram_substring(home))
        self.assertTrue(is_hq_7gram_substring(home[:7]))
        self.assertTrue(is_contiguous_substring(home, home))
        self.assertFalse(is_hq_7gram_substring(planted))
        self.assertFalse(is_hq_7gram_substring(measured_indep))
        self.assertFalse(is_hq_7gram_substring(home + ("999",)))
        self.assertTrue(is_hq_7gram_substring(home[1:]))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge7_grams(once_each, analyzer), ())
        self.assertFalse(q_repeating_nge7_all_substrings_of_hq_7gram(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_nge7_grams(twice_home, analyzer)
        self.assertGreaterEqual(len(home_only), 1)
        self.assertIn((home, 7, 2), home_only)
        home_rows = tuple(
            (gram, n, freq, is_hq_7gram_substring(gram), ())
            for gram, n, freq in home_only
        )
        self.assertTrue(q_repeating_nge7_all_substrings_of_hq_7gram(home_rows))
        self.assertEqual(independent_rows(home_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge7_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_hq_7gram_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(q_repeating_nge7_all_substrings_of_hq_7gram(both_rows))
        self.assertIn(planted, tuple(gram for gram, n, _freq in both if n == 7))
        twice_measured = [
            list(home),
            list(home),
            list(measured_indep),
            list(measured_indep),
        ]
        measured_both = repeating_nge7_grams(twice_measured, analyzer)
        measured_rows = tuple(
            (gram, n, freq, is_hq_7gram_substring(gram), ())
            for gram, n, freq in measured_both
        )
        self.assertFalse(q_repeating_nge7_all_substrings_of_hq_7gram(measured_rows))
        self.assertIn(measured_indep, tuple(gram for gram, n, _freq in measured_both if n == 7))
        gapped = [list(home[:4]) + ["999"] + list(home[4:]), list(home)]
        self.assertEqual(repeating_nge7_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "q_repeating_nge7_all_substrings_of_hq_7gram")
        self.assertFalse(STANDING_Q_REPEATING_NGE7_ALL_SUBSTRINGS_OF_HQ_7GRAM)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 1)
        self.assertFalse(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariQNge7Scoreboard(unittest.TestCase):
    """Cited-fixture Q repeating n≥7 vs the H/Q 7-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.q_sides = load_q_h_p_sides()
        measured = repeating_nge7_grams(self.by_tablet["Q"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_hq_7gram_substring(gram),
                nge7_sites(gram, self.q_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = q_repeating_nge7_all_substrings_of_hq_7gram(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_q = tuple(
            off_q_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_99_108_n7_not_invented(self):
        """H/Q 7-gram is a prior lock; the independent 7-gram is measured."""
        self.assertEqual(STANDING_N7, INVENTORY_LONGEST_TOKENS["H"])
        self.assertEqual(STANDING_N7, INVENTORY_LONGEST_TOKENS["Q"])
        self.assertEqual(INVENTORY_LONGEST_N["H"], 7)
        self.assertEqual(INVENTORY_LONGEST_N["Q"], 7)
        self.assertEqual(len(STANDING_N7), 7)
        self.assertEqual(len(STANDING_INDEP_N7), 7)
        self.assertEqual(
            STANDING_N7,
            ("072", "450", "052", "551", "003", "600", "003"),
        )
        self.assertEqual(
            STANDING_INDEP_N7,
            ("003", "028", "095", "073", "001", "057", "001"),
        )
        self.assertTrue(is_hq_7gram_substring(STANDING_N7))
        self.assertTrue(is_contiguous_substring(STANDING_N7, STANDING_N7))
        self.assertTrue(STANDING_N7_IS_SUBSTRING_OF_SELF)
        self.assertFalse(is_hq_7gram_substring(STANDING_INDEP_N7))
        self.assertFalse(is_contiguous_substring(STANDING_INDEP_N7, STANDING_N7))
        self.assertFalse(STANDING_INDEP_IS_SUBSTRING)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["Q"]["longest_tokens"]),
            STANDING_N7,
        )
        self.assertEqual(
            tuple(self.survey["hq_max_n_hpq_island_substring"]["tokens7"]),
            STANDING_N7,
        )
        self.assertEqual(self.survey["hq_max_n_hpq_island_substring"]["cycle"], 108)
        self.assertEqual(self.survey["hq_7gram_hq_pairwise_island_substring"]["cycle"], 109)
        self.assertEqual(self.survey["h_repeating_nge8"]["cycle"], 126)
        self.assertEqual(self.survey["h_repeating_nge7"]["cycle"], 127)
        self.assertEqual(self.survey["q_repeating_nge8"]["cycle"], 128)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertNotEqual(STANDING_N7, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_INDEP_N7, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_N7, STANDING_INDEP_N7)
        self.assertFalse(is_hq_7gram_substring(INDEPENDENT_PLANT))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_loses(self):
        """2 repeating n≥7; 1 substring; 1 independent. Claim is false."""
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
        self.assertEqual(STANDING_LONGEST_N, 7)
        self.assertFalse(q_repeating_nge7_all_substrings_of_hq_7gram(self.rows))
        self.assertEqual(self.claim_holds, STANDING_Q_REPEATING_NGE7_ALL_SUBSTRINGS_OF_HQ_7GRAM)
        self.assertFalse(STANDING_Q_REPEATING_NGE7_ALL_SUBSTRINGS_OF_HQ_7GRAM)
        self.assertEqual(STANDING_CLAIM, "q_repeating_nge7_all_substrings_of_hq_7gram")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        n8 = self.analyzer.extract_ngrams(self.by_tablet["Q"], n=8, min_frequency=2)
        self.assertEqual(n8, [])
        self.assertEqual(STANDING_H_REPEATING_COUNT, 1)
        self.assertEqual(STANDING_H_SUBSTRING_COUNT, 1)
        self.assertEqual(STANDING_H_INDEPENDENT_COUNT, 0)
        self.assertTrue(STANDING_H_Q_NGE7_ASYMMETRY)
        self.assertNotEqual(STANDING_REPEATING_COUNT, STANDING_H_REPEATING_COUNT)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, STANDING_H_INDEPENDENT_COUNT)
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
            self.assertEqual(is_hq_7gram_substring(gram), is_sub)
            self.assertEqual(nge7_sites(gram, self.q_sides), sites)
            self.assertEqual(len(sites), freq)
        self.assertIn(STANDING_N7, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 7))
        self.assertIn(STANDING_INDEP_N7, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 7))
        self.assertTrue(STANDING_N7_IN_SET)
        self.assertTrue(STANDING_INDEP_IN_SET)
        sevengrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 7)
        self.assertEqual(sevengrams, (STANDING_N7, STANDING_INDEP_N7))
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_the_measured_q_only_7gram(self):
        """Independent remainder is exactly 003 028 095 073 001 057 001."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertEqual(indep_tokens, (STANDING_INDEP_N7,))
        self.assertNotIn(STANDING_N7, indep_tokens)
        self.assertTrue(is_hq_7gram_substring(STANDING_N7))
        self.assertFalse(is_hq_7gram_substring(STANDING_INDEP_N7))
        self.assertFalse(is_hq_7gram_substring(INDEPENDENT_PLANT))
        self.assertNotIn(INDEPENDENT_PLANT, indep_tokens)
        self.assertFalse(is_contiguous_substring(STANDING_INDEP_N7, STANDING_N7))
        self.assertEqual(len(indep_tokens), 1)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_q_hits(self):
        """Independent Q sites span Qr/Qv; H=0; P=0; off-Q 0 on every tablet."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_q, STANDING_INDEPENDENT_OFF_Q)
        self.assertEqual(STANDING_INDEPENDENT_OFF_Q, (0,))
        for (gram, n, freq, sites), hits, off_hits in zip(
            self.independent,
            self.indep_hits_by_tablet,
            self.indep_off_q,
            strict=True,
        ):
            self.assertEqual(nge7_sites(gram, self.q_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("Q")], freq)
            self.assertEqual(ngram_hit_count(self.q_sides[SIDE_QR], gram), 1)
            self.assertEqual(ngram_hit_count(self.q_sides[SIDE_QV], gram), 1)
            self.assertEqual(ngram_hit_count(self.by_tablet["H"], gram), 0)
            self.assertEqual(ngram_hit_count(self.by_tablet["P"], gram), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "Q":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("Q", hits), {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = QR_LINE_NAMES if side == SIDE_QR else QV_LINE_NAMES
                stems = self.q_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
        self.assertEqual(
            nge7_sites(STANDING_INDEP_N7, self.q_sides),
            ((SIDE_QR, "Qr8", 44), (SIDE_QV, "Qv3", 27)),
        )
        self.assertEqual(tuple(STANDING_INDEPENDENT_QR_HITS), (1,))
        self.assertEqual(tuple(STANDING_INDEPENDENT_QV_HITS), (1,))
        self.assertEqual(tuple(STANDING_INDEPENDENT_H_HITS), (0,))
        self.assertEqual(tuple(STANDING_INDEPENDENT_P_HITS), (0,))
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(ngram_hit_count(self.q_sides[SIDE_QR], STANDING_N7), 2)
        self.assertEqual(ngram_hit_count(self.q_sides[SIDE_QV], STANDING_N7), 0)
        self.assertEqual(ngram_hit_count(self.by_tablet["H"], STANDING_N7), 2)
        self.assertEqual(ngram_hit_count(self.by_tablet["Q"], STANDING_N7), 2)
        self.assertEqual(ngram_hit_count(self.by_tablet["P"], STANDING_N7), 0)
        self.assertEqual(
            nge7_sites(STANDING_N7, self.q_sides),
            ((SIDE_QR, "Qr3", 43), (SIDE_QR, "Qr3", 52)),
        )
        home_hits = tablet_hit_counts(self.by_tablet, STANDING_N7, VENDORED_TABLETS)
        self.assertEqual(home_hits[VENDORED_TABLETS.index("H")], 2)
        self.assertEqual(home_hits[VENDORED_TABLETS.index("Q")], 2)
        self.assertEqual(home_hits[VENDORED_TABLETS.index("P")], 0)
        self.assertEqual(leaks_from_hits("Q", home_hits), {"H": 2})
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_130_128_127_126_108_109_and_w_scoreboards_still_compute(self):
        """Cycle 130 K n≥8, 128 Q n≥8, 127 H n≥7, 126 H n≥8, 108/109, and W stay."""
        prior_130 = TestMamariKNge8Scoreboard()
        prior_130.setUp()
        prior_130.test_counts_and_hypothesis_all_substrings_holds()
        prior_130.test_survey_matches_computed_lock()
        prior_128 = TestMamariQNge8Scoreboard()
        prior_128.setUp()
        prior_128.test_counts_and_hypothesis_all_substrings_holds()
        prior_128.test_survey_matches_computed_lock()
        prior_127 = TestMamariHNge7Scoreboard()
        prior_127.setUp()
        prior_127.test_counts_and_hypothesis_all_substrings_holds()
        prior_127.test_survey_matches_computed_lock()
        prior_126 = TestMamariHNge8Scoreboard()
        prior_126.setUp()
        prior_126.test_counts_and_hypothesis_all_substrings_holds()
        prior_126.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-131 n≥7 7-gram-substring lock."""
        lock = self.survey["q_repeating_nge7"]
        self.assertEqual(lock["cycle"], 131)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(tuple(lock["home_tokens7"]), STANDING_N7)
        self.assertEqual(tuple(lock["independent_tokens7"]), STANDING_INDEP_N7)
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
                "off_q_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_q_hits"]), STANDING_INDEPENDENT_OFF_Q)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n7_in_set"])
        self.assertTrue(lock["indep_in_set"])
        self.assertTrue(lock["n7_is_substring_of_self"])
        self.assertFalse(lock["indep_is_substring"])
        self.assertEqual(lock["h_repeating_count"], STANDING_H_REPEATING_COUNT)
        self.assertEqual(lock["h_substring_count"], STANDING_H_SUBSTRING_COUNT)
        self.assertEqual(lock["h_independent_count"], STANDING_H_INDEPENDENT_COUNT)
        self.assertTrue(lock["h_q_nge7_asymmetry"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["q_repeating_nge7_all_substrings_of_hq_7gram"])
        self.assertEqual(
            lock["q_repeating_nge7_all_substrings_of_hq_7gram"],
            STANDING_Q_REPEATING_NGE7_ALL_SUBSTRINGS_OF_HQ_7GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_h_repeating_nge7_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_h_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_p_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_k_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_hq_max_n_hpq_island_substring_unchanged"])
        self.assertTrue(lock["standing_hq_7gram_hq_pairwise_island_substring_unchanged"])
        self.assertTrue(lock["standing_g_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_e_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["h_repeating_nge7"]["cycle"], 127)
        self.assertEqual(self.survey["h_repeating_nge7"]["repeating_count"], 1)
        self.assertTrue(self.survey["h_repeating_nge7"]["h_repeating_nge7_all_substrings_of_hq_7gram"])
        self.assertEqual(self.survey["q_repeating_nge8"]["cycle"], 128)
        self.assertEqual(self.survey["q_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["q_repeating_nge8"]["q_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["h_repeating_nge8"]["cycle"], 126)
        self.assertEqual(self.survey["h_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["h_repeating_nge8"]["h_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["p_repeating_nge8"]["cycle"], 129)
        self.assertEqual(self.survey["p_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["p_repeating_nge8"]["p_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["k_repeating_nge8"]["cycle"], 130)
        self.assertEqual(self.survey["k_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["k_repeating_nge8"]["k_repeating_nge8_all_substrings_of_gk_islands"])
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
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["Q"]["longest_n"], 7)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariQNge7ImageSnapshot(unittest.TestCase):
    """Cycle 131 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
