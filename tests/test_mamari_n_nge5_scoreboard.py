"""N's repeating n≥5 grams vs the locked N 6-gram.

Cycle 134 text-search lock. Uses already-vendored A–V and the
cycle-89/91 N 6-gram. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented Barthel.
No G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Enumerates every distinct contiguous n≥5 gram with freq≥2 on N
(same per-line Barthel parser as the leak table / S n≥6
scoreboards). For each, whether it is an exact contiguous
substring of 004 064 034 006 004 064 (the 6-gram is a
substring of itself). Hypothesis: no independent repeating n≥5
(every such gram is a 6-gram substring). Measured: 3 repeating
n≥5; 3 are substrings; 0 independent. The two 5-grams are the
6-gram's prefix and suffix at Na1[3]/[11] and Na1[4]/[12].
Cycle 89 already locked longest n=6 and no n≥8. Claim that can
lose: n_repeating_nge5_all_substrings_of_n_6gram. The claim is
true. Do not retune.

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
    independent_rows,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_p_nge6_scoreboard import (
    TestMamariPNge6Scoreboard,
)
from tests.test_mamari_s_nge6_scoreboard import (
    TestMamariSNge6Scoreboard,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_vienna_na1_n_only_scoreboard import (
    GRAM6,
    TestMamariSmallViennaNa1NOnlyScoreboard,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    NA_LINE_NAMES,
    NB_LINE_NAMES,
    SIDE_NA,
    SIDE_NB,
    TestMamariSmallViennaVendorScoreboard,
    load_n_sides,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_N as N_VENDOR_LONGEST_N,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 5
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N6 = GRAM6
STANDING_N5_PREFIX = STANDING_N6[:5]
STANDING_N5_SUFFIX = STANDING_N6[1:]
INDEPENDENT_PLANT = H_INDEPENDENT_PLANT[:5]
STANDING_REPEATING_COUNT = 3
STANDING_SUBSTRING_COUNT = 3
STANDING_INDEPENDENT_COUNT = 0
STANDING_COUNTS_BY_N = {5: 2, 6: 1}
STANDING_SUBSTRING_BY_N = {5: 2, 6: 1}
STANDING_INDEPENDENT_BY_N = {}
STANDING_LONGEST_N = 6
STANDING_ROWS = (
    (
        STANDING_N5_PREFIX,
        5,
        2,
        True,
        ((SIDE_NA, "Na1", 3), (SIDE_NA, "Na1", 11)),
    ),
    (
        STANDING_N5_SUFFIX,
        5,
        2,
        True,
        ((SIDE_NA, "Na1", 4), (SIDE_NA, "Na1", 12)),
    ),
    (
        STANDING_N6,
        6,
        2,
        True,
        ((SIDE_NA, "Na1", 3), (SIDE_NA, "Na1", 11)),
    ),
)
STANDING_INDEPENDENT = ()
STANDING_INDEPENDENT_OFF_N = ()
STANDING_INDEPENDENT_NA_HITS = ()
STANDING_INDEPENDENT_NB_HITS = ()
STANDING_KNOWN_DISTINCT = True
STANDING_N6_IN_SET = True
STANDING_N5_PREFIX_IN_SET = True
STANDING_N5_SUFFIX_IN_SET = True
STANDING_N6_IS_SUBSTRING_OF_SELF = True
STANDING_N5_PREFIX_IS_SUBSTRING = True
STANDING_N5_SUFFIX_IS_SUBSTRING = True
STANDING_CLAIM = "n_repeating_nge5_all_substrings_of_n_6gram"
STANDING_N_REPEATING_NGE5_ALL_SUBSTRINGS_OF_N_6GRAM = True
STANDING_RESULT = "n_repeating_nge5"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def repeating_nge5_grams(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
) -> tuple[tuple[tuple[str, ...], int, int], ...]:
    """Distinct contiguous n≥5 grams with freq≥2. Search only."""
    rows: list[tuple[tuple[str, ...], int, int]] = []
    n = PROFILE_MIN_N
    while True:
        found = analyzer.extract_ngrams(lines, n=n, min_frequency=2)
        if not found:
            break
        rows.extend((gram, n, freq) for gram, freq in found)
        n += 1
    return tuple(rows)


def nge5_sites(
    gram: tuple[str, ...],
    n_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Na then Nb. Search only."""
    hits = named_side_hits(n_sides[SIDE_NA], NA_LINE_NAMES, SIDE_NA, gram)
    hits += named_side_hits(n_sides[SIDE_NB], NB_LINE_NAMES, SIDE_NB, gram)
    return tuple(site_tuple(hit) for hit in hits)


def is_n_6gram_substring(
    gram: tuple[str, ...],
    n6: tuple[str, ...] = STANDING_N6,
) -> bool:
    """True iff gram is an exact contiguous run inside the N 6-gram."""
    return is_contiguous_substring(gram, n6)


def n_repeating_nge5_all_substrings_of_n_6gram(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥5 is a 6-gram substring.

    The 6-gram is a substring of itself. An empty inventory is
    false here (the home 6-gram must be in the repeating set).
    """
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_n_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off N. Counts only."""
    return sum(leaks_from_hits("N", hits, tablets).values())


class TestNNge5Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted non-6-gram 5-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = STANDING_N6
        prefix = STANDING_N5_PREFIX
        suffix = STANDING_N5_SUFFIX
        planted = INDEPENDENT_PLANT
        self.assertNotEqual(home, planted)
        self.assertNotEqual(prefix, planted)
        self.assertNotEqual(suffix, planted)
        self.assertEqual(len(home), 6)
        self.assertEqual(len(prefix), 5)
        self.assertEqual(len(suffix), 5)
        self.assertEqual(len(planted), 5)
        self.assertTrue(is_n_6gram_substring(home))
        self.assertTrue(is_n_6gram_substring(home[:6]))
        self.assertTrue(is_contiguous_substring(home, home))
        self.assertTrue(is_n_6gram_substring(prefix))
        self.assertTrue(is_n_6gram_substring(suffix))
        self.assertTrue(is_n_6gram_substring(home[1:]))
        self.assertFalse(is_n_6gram_substring(planted))
        self.assertFalse(is_n_6gram_substring(home + ("999",)))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge5_grams(once_each, analyzer), ())
        self.assertFalse(n_repeating_nge5_all_substrings_of_n_6gram(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_nge5_grams(twice_home, analyzer)
        self.assertGreaterEqual(len(home_only), 1)
        self.assertIn((home, 6, 2), home_only)
        self.assertIn((prefix, 5, 2), home_only)
        self.assertIn((suffix, 5, 2), home_only)
        home_rows = tuple(
            (gram, n, freq, is_n_6gram_substring(gram), ())
            for gram, n, freq in home_only
        )
        self.assertTrue(n_repeating_nge5_all_substrings_of_n_6gram(home_rows))
        self.assertEqual(independent_rows(home_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge5_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_n_6gram_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(n_repeating_nge5_all_substrings_of_n_6gram(both_rows))
        self.assertIn(planted, tuple(gram for gram, n, _freq in both if n == 5))
        gapped = [list(home[:3]) + ["999"] + list(home[3:]), list(home)]
        self.assertEqual(repeating_nge5_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "n_repeating_nge5_all_substrings_of_n_6gram")
        self.assertTrue(STANDING_N_REPEATING_NGE5_ALL_SUBSTRINGS_OF_N_6GRAM)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariNNge5Scoreboard(unittest.TestCase):
    """Cited-fixture N repeating n≥5 vs the N 6-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.n_sides = load_n_sides()
        measured = repeating_nge5_grams(self.by_tablet["N"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_n_6gram_substring(gram),
                nge5_sites(gram, self.n_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = n_repeating_nge5_all_substrings_of_n_6gram(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_n = tuple(
            off_n_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_89_91_n6_not_invented(self):
        """N 6-gram is a prior lock; both 5-grams are its measured slices."""
        self.assertEqual(STANDING_N6, INVENTORY_LONGEST_TOKENS["N"])
        self.assertEqual(STANDING_N6, N_N6_GRAM)
        self.assertEqual(STANDING_N6, GRAM6)
        self.assertEqual(INVENTORY_LONGEST_N["N"], 6)
        self.assertEqual(N_VENDOR_LONGEST_N, 6)
        self.assertEqual(len(STANDING_N6), 6)
        self.assertEqual(len(STANDING_N5_PREFIX), 5)
        self.assertEqual(len(STANDING_N5_SUFFIX), 5)
        self.assertEqual(
            STANDING_N6,
            ("004", "064", "034", "006", "004", "064"),
        )
        self.assertEqual(
            STANDING_N5_PREFIX,
            ("004", "064", "034", "006", "004"),
        )
        self.assertEqual(
            STANDING_N5_SUFFIX,
            ("064", "034", "006", "004", "064"),
        )
        self.assertEqual(STANDING_N5_PREFIX, STANDING_N6[:5])
        self.assertEqual(STANDING_N5_SUFFIX, STANDING_N6[1:])
        self.assertTrue(is_n_6gram_substring(STANDING_N6))
        self.assertTrue(is_contiguous_substring(STANDING_N6, STANDING_N6))
        self.assertTrue(STANDING_N6_IS_SUBSTRING_OF_SELF)
        self.assertTrue(is_n_6gram_substring(STANDING_N5_PREFIX))
        self.assertTrue(is_n_6gram_substring(STANDING_N5_SUFFIX))
        self.assertTrue(STANDING_N5_PREFIX_IS_SUBSTRING)
        self.assertTrue(STANDING_N5_SUFFIX_IS_SUBSTRING)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["N"]["longest_tokens"]),
            STANDING_N6,
        )
        self.assertEqual(
            tuple(self.survey["tablet_n_vienna_vendor"]["longest_tokens"]),
            STANDING_N6,
        )
        self.assertEqual(
            tuple(self.survey["tablet_n_vienna_na1_n_only"]["tokens6"]),
            STANDING_N6,
        )
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["cycle"], 89)
        self.assertEqual(self.survey["tablet_n_vienna_na1_n_only"]["cycle"], 91)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertEqual(self.survey["p_repeating_nge6"]["cycle"], 132)
        self.assertEqual(self.survey["q_repeating_nge7"]["cycle"], 131)
        self.assertNotEqual(STANDING_N6, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_N5_PREFIX, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_N5_SUFFIX, INDEPENDENT_PLANT)
        self.assertFalse(is_n_6gram_substring(INDEPENDENT_PLANT))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_holds(self):
        """3 repeating n≥5; 3 substrings; 0 independent. Claim is true."""
        self.assertEqual(len(self.rows), STANDING_REPEATING_COUNT)
        self.assertEqual(self.substring_count, STANDING_SUBSTRING_COUNT)
        self.assertEqual(len(self.independent), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_REPEATING_COUNT, 3)
        self.assertEqual(STANDING_SUBSTRING_COUNT, 3)
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
        self.assertEqual(max(by_n), STANDING_LONGEST_N)
        self.assertEqual(STANDING_LONGEST_N, 6)
        self.assertTrue(n_repeating_nge5_all_substrings_of_n_6gram(self.rows))
        self.assertEqual(self.claim_holds, STANDING_N_REPEATING_NGE5_ALL_SUBSTRINGS_OF_N_6GRAM)
        self.assertTrue(STANDING_N_REPEATING_NGE5_ALL_SUBSTRINGS_OF_N_6GRAM)
        self.assertEqual(STANDING_CLAIM, "n_repeating_nge5_all_substrings_of_n_6gram")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        n7 = self.analyzer.extract_ngrams(self.by_tablet["N"], n=7, min_frequency=2)
        self.assertEqual(n7, [])
        n8 = self.analyzer.extract_ngrams(self.by_tablet["N"], n=8, min_frequency=2)
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
            self.assertEqual(is_n_6gram_substring(gram), is_sub)
            self.assertEqual(nge5_sites(gram, self.n_sides), sites)
            self.assertEqual(len(sites), freq)
        self.assertIn(STANDING_N6, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6))
        self.assertIn(
            STANDING_N5_PREFIX,
            tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 5),
        )
        self.assertIn(
            STANDING_N5_SUFFIX,
            tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 5),
        )
        self.assertTrue(STANDING_N6_IN_SET)
        self.assertTrue(STANDING_N5_PREFIX_IN_SET)
        self.assertTrue(STANDING_N5_SUFFIX_IN_SET)
        fivegrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 5)
        self.assertEqual(fivegrams, (STANDING_N5_PREFIX, STANDING_N5_SUFFIX))
        sixgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6)
        self.assertEqual(sixgrams, (STANDING_N6,))
        sevengrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 7)
        self.assertEqual(sevengrams, ())
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_empty(self):
        """No N-local repeating n≥5 remainder off the N 6-gram."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertEqual(indep_tokens, ())
        self.assertNotIn(STANDING_N6, indep_tokens)
        self.assertNotIn(STANDING_N5_PREFIX, indep_tokens)
        self.assertNotIn(STANDING_N5_SUFFIX, indep_tokens)
        self.assertTrue(is_n_6gram_substring(STANDING_N6))
        self.assertTrue(is_n_6gram_substring(STANDING_N5_PREFIX))
        self.assertTrue(is_n_6gram_substring(STANDING_N5_SUFFIX))
        self.assertFalse(is_n_6gram_substring(INDEPENDENT_PLANT))
        self.assertNotIn(INDEPENDENT_PLANT, indep_tokens)
        self.assertEqual(len(indep_tokens), 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_home_sites_and_off_n_hits(self):
        """All three grams are Na1-only; Nb=0; off-N 0; empty independent."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_n, STANDING_INDEPENDENT_OFF_N)
        self.assertEqual(STANDING_INDEPENDENT_OFF_N, ())
        self.assertEqual(self.indep_hits_by_tablet, ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_NA_HITS), ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_NB_HITS), ())
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        for gram, n, freq, is_sub, sites in self.rows:
            self.assertTrue(is_sub)
            self.assertEqual(nge5_sites(gram, self.n_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(ngram_hit_count(self.n_sides[SIDE_NA], gram), freq)
            self.assertEqual(ngram_hit_count(self.n_sides[SIDE_NB], gram), 0)
            self.assertEqual(ngram_hit_count(self.by_tablet["N"], gram), freq)
            hits = tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            self.assertEqual(hits[VENDORED_TABLETS.index("N")], freq)
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "N":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("N", hits), {})
            self.assertEqual(off_n_hit_total(hits), 0)
            for side, line, index in sites:
                names = NA_LINE_NAMES if side == SIDE_NA else NB_LINE_NAMES
                stems = self.n_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_NA)
                self.assertEqual(line, "Na1")
        self.assertEqual(
            nge5_sites(STANDING_N6, self.n_sides),
            ((SIDE_NA, "Na1", 3), (SIDE_NA, "Na1", 11)),
        )
        self.assertEqual(
            nge5_sites(STANDING_N5_PREFIX, self.n_sides),
            ((SIDE_NA, "Na1", 3), (SIDE_NA, "Na1", 11)),
        )
        self.assertEqual(
            nge5_sites(STANDING_N5_SUFFIX, self.n_sides),
            ((SIDE_NA, "Na1", 4), (SIDE_NA, "Na1", 12)),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_133_132_91_89_and_w_scoreboards_still_compute(self):
        """Cycle 133 S n≥6, 132 P n≥6, 91/89 N, and W stay."""
        prior_133 = TestMamariSNge6Scoreboard()
        prior_133.setUp()
        prior_133.test_counts_and_hypothesis_all_substrings_holds()
        prior_133.test_survey_matches_computed_lock()
        prior_132 = TestMamariPNge6Scoreboard()
        prior_132.setUp()
        prior_132.test_counts_and_hypothesis_all_substrings_loses()
        prior_132.test_survey_matches_computed_lock()
        prior_91 = TestMamariSmallViennaNa1NOnlyScoreboard()
        prior_91.setUp()
        prior_91.test_6gram_is_zero_off_n_and_n_only()
        prior_91.test_survey_matches_computed_lock()
        prior_89 = TestMamariSmallViennaVendorScoreboard()
        prior_89.setUp()
        prior_89.test_longest_repeating_ngram_has_no_8gram()
        prior_89.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-134 n≥5 6-gram-substring lock."""
        lock = self.survey["n_repeating_nge5"]
        self.assertEqual(lock["cycle"], 134)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(tuple(lock["home_tokens6"]), STANDING_N6)
        self.assertEqual(tuple(lock["home_tokens5_prefix"]), STANDING_N5_PREFIX)
        self.assertEqual(tuple(lock["home_tokens5_suffix"]), STANDING_N5_SUFFIX)
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
                "off_n_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_n_hits"]), STANDING_INDEPENDENT_OFF_N)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n6_in_set"])
        self.assertTrue(lock["n5_prefix_in_set"])
        self.assertTrue(lock["n5_suffix_in_set"])
        self.assertTrue(lock["n6_is_substring_of_self"])
        self.assertTrue(lock["n5_prefix_is_substring"])
        self.assertTrue(lock["n5_suffix_is_substring"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["n_repeating_nge5_all_substrings_of_n_6gram"])
        self.assertEqual(
            lock["n_repeating_nge5_all_substrings_of_n_6gram"],
            STANDING_N_REPEATING_NGE5_ALL_SUBSTRINGS_OF_N_6GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_p_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge7_unchanged"])
        self.assertTrue(lock["standing_n_vienna_na1_n_only_unchanged"])
        self.assertTrue(lock["standing_n_vienna_vendor_unchanged"])
        self.assertTrue(lock["standing_p_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_h_repeating_nge7_unchanged"])
        self.assertTrue(lock["standing_h_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_k_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_g_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertEqual(self.survey["s_repeating_nge6"]["repeating_count"], 3)
        self.assertTrue(self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(self.survey["p_repeating_nge6"]["cycle"], 132)
        self.assertEqual(self.survey["p_repeating_nge6"]["repeating_count"], 2)
        self.assertFalse(self.survey["p_repeating_nge6"]["p_repeating_nge6_all_substrings_of_p_6gram"])
        self.assertEqual(self.survey["q_repeating_nge7"]["cycle"], 131)
        self.assertEqual(self.survey["q_repeating_nge7"]["repeating_count"], 2)
        self.assertFalse(self.survey["q_repeating_nge7"]["q_repeating_nge7_all_substrings_of_hq_7gram"])
        self.assertEqual(self.survey["tablet_n_vienna_na1_n_only"]["cycle"], 91)
        self.assertTrue(self.survey["tablet_n_vienna_na1_n_only"]["n_only"])
        self.assertEqual(
            tuple(self.survey["tablet_n_vienna_na1_n_only"]["tokens6"]),
            STANDING_N6,
        )
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["cycle"], 89)
        self.assertEqual(self.survey["tablet_n_vienna_vendor"]["longest_n"], 6)
        self.assertFalse(self.survey["tablet_n_vienna_vendor"]["eightgram_exists"])
        self.assertEqual(self.survey["p_repeating_nge8"]["cycle"], 129)
        self.assertEqual(self.survey["p_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["p_repeating_nge8"]["p_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["q_repeating_nge8"]["cycle"], 128)
        self.assertEqual(self.survey["q_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["q_repeating_nge8"]["q_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["h_repeating_nge7"]["cycle"], 127)
        self.assertEqual(self.survey["h_repeating_nge7"]["repeating_count"], 1)
        self.assertTrue(self.survey["h_repeating_nge7"]["h_repeating_nge7_all_substrings_of_hq_7gram"])
        self.assertEqual(self.survey["h_repeating_nge8"]["cycle"], 126)
        self.assertEqual(self.survey["h_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["h_repeating_nge8"]["h_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["k_repeating_nge8"]["cycle"], 130)
        self.assertEqual(self.survey["k_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["k_repeating_nge8"]["k_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(self.survey["g_repeating_nge8"]["cycle"], 125)
        self.assertFalse(self.survey["g_repeating_nge8"]["g_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["N"]["longest_n"], 6)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariNNge5ImageSnapshot(unittest.TestCase):
    """Cycle 134 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
