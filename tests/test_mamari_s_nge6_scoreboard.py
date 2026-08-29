"""S's repeating n≥6 grams vs the locked S 7-gram.

Cycle 133 text-search lock. Uses already-vendored A–V and the
cycle-94/95 S 7-gram. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented Barthel.
No G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Enumerates every distinct contiguous n≥6 gram with freq≥2 on S
(same per-line Barthel parser as the leak table / P n≥6
scoreboards). For each, whether it is an exact contiguous
substring of 004 660 081 004 660 081 004 (the 7-gram is a
substring of itself). Hypothesis: no independent repeating n≥6
(every such gram is a 7-gram substring). Measured: 3 repeating
n≥6; 3 are substrings; 0 independent. The two 6-grams are the
7-gram's prefix and suffix at Sb2[15]/[18] and Sb2[16]/[19].
Cycle 94 already locked longest n=7 and no n≥8. Claim that can
lose: s_repeating_nge6_all_substrings_of_s_7gram. The claim is
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
    TestMamariHNge7Scoreboard,
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
    repeating_nge6_grams,
)
from tests.test_mamari_q_nge7_scoreboard import (
    TestMamariQNge7Scoreboard,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts
from tests.test_mamari_washington_sb2_s_only_scoreboard import (
    GRAM7,
    TestMamariWashingtonSb2SOnlyScoreboard,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SA_LINE_NAMES,
    SB_LINE_NAMES,
    SIDE_SA,
    SIDE_SB,
    TestMamariWashingtonVendorScoreboard,
    load_s_sides,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_N as S_VENDOR_LONGEST_N,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as S_N7_GRAM,
)

PROFILE_MIN_N = 6
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N7 = GRAM7
STANDING_N6_PREFIX = STANDING_N7[:6]
STANDING_N6_SUFFIX = STANDING_N7[1:]
INDEPENDENT_PLANT = H_INDEPENDENT_PLANT[:6]
STANDING_REPEATING_COUNT = 3
STANDING_SUBSTRING_COUNT = 3
STANDING_INDEPENDENT_COUNT = 0
STANDING_COUNTS_BY_N = {6: 2, 7: 1}
STANDING_SUBSTRING_BY_N = {6: 2, 7: 1}
STANDING_INDEPENDENT_BY_N = {}
STANDING_LONGEST_N = 7
STANDING_ROWS = (
    (
        STANDING_N6_PREFIX,
        6,
        2,
        True,
        ((SIDE_SB, "Sb2", 15), (SIDE_SB, "Sb2", 18)),
    ),
    (
        STANDING_N6_SUFFIX,
        6,
        2,
        True,
        ((SIDE_SB, "Sb2", 16), (SIDE_SB, "Sb2", 19)),
    ),
    (
        STANDING_N7,
        7,
        2,
        True,
        ((SIDE_SB, "Sb2", 15), (SIDE_SB, "Sb2", 18)),
    ),
)
STANDING_INDEPENDENT = ()
STANDING_INDEPENDENT_OFF_S = ()
STANDING_INDEPENDENT_SA_HITS = ()
STANDING_INDEPENDENT_SB_HITS = ()
STANDING_KNOWN_DISTINCT = True
STANDING_N7_IN_SET = True
STANDING_N6_PREFIX_IN_SET = True
STANDING_N6_SUFFIX_IN_SET = True
STANDING_N7_IS_SUBSTRING_OF_SELF = True
STANDING_N6_PREFIX_IS_SUBSTRING = True
STANDING_N6_SUFFIX_IS_SUBSTRING = True
STANDING_CLAIM = "s_repeating_nge6_all_substrings_of_s_7gram"
STANDING_S_REPEATING_NGE6_ALL_SUBSTRINGS_OF_S_7GRAM = True
STANDING_RESULT = "s_repeating_nge6"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def nge6_sites(
    gram: tuple[str, ...],
    s_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Sa then Sb. Search only."""
    hits = named_side_hits(s_sides[SIDE_SA], SA_LINE_NAMES, SIDE_SA, gram)
    hits += named_side_hits(s_sides[SIDE_SB], SB_LINE_NAMES, SIDE_SB, gram)
    return tuple(site_tuple(hit) for hit in hits)


def is_s_7gram_substring(
    gram: tuple[str, ...],
    n7: tuple[str, ...] = STANDING_N7,
) -> bool:
    """True iff gram is an exact contiguous run inside the S 7-gram."""
    return is_contiguous_substring(gram, n7)


def s_repeating_nge6_all_substrings_of_s_7gram(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥6 is a 7-gram substring.

    The 7-gram is a substring of itself. An empty inventory is
    false here (the home 7-gram must be in the repeating set).
    """
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_s_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off S. Counts only."""
    return sum(leaks_from_hits("S", hits, tablets).values())


class TestSNge6Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted non-7-gram 6-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = STANDING_N7
        prefix = STANDING_N6_PREFIX
        suffix = STANDING_N6_SUFFIX
        planted = INDEPENDENT_PLANT
        self.assertNotEqual(home, planted)
        self.assertNotEqual(prefix, planted)
        self.assertNotEqual(suffix, planted)
        self.assertEqual(len(home), 7)
        self.assertEqual(len(prefix), 6)
        self.assertEqual(len(suffix), 6)
        self.assertEqual(len(planted), 6)
        self.assertTrue(is_s_7gram_substring(home))
        self.assertTrue(is_s_7gram_substring(home[:7]))
        self.assertTrue(is_contiguous_substring(home, home))
        self.assertTrue(is_s_7gram_substring(prefix))
        self.assertTrue(is_s_7gram_substring(suffix))
        self.assertTrue(is_s_7gram_substring(home[1:]))
        self.assertFalse(is_s_7gram_substring(planted))
        self.assertFalse(is_s_7gram_substring(home + ("999",)))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge6_grams(once_each, analyzer), ())
        self.assertFalse(s_repeating_nge6_all_substrings_of_s_7gram(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_nge6_grams(twice_home, analyzer)
        self.assertGreaterEqual(len(home_only), 1)
        self.assertIn((home, 7, 2), home_only)
        self.assertIn((prefix, 6, 2), home_only)
        self.assertIn((suffix, 6, 2), home_only)
        home_rows = tuple(
            (gram, n, freq, is_s_7gram_substring(gram), ())
            for gram, n, freq in home_only
        )
        self.assertTrue(s_repeating_nge6_all_substrings_of_s_7gram(home_rows))
        self.assertEqual(independent_rows(home_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge6_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_s_7gram_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(s_repeating_nge6_all_substrings_of_s_7gram(both_rows))
        self.assertIn(planted, tuple(gram for gram, n, _freq in both if n == 6))
        gapped = [list(home[:4]) + ["999"] + list(home[4:]), list(home)]
        self.assertEqual(repeating_nge6_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "s_repeating_nge6_all_substrings_of_s_7gram")
        self.assertTrue(STANDING_S_REPEATING_NGE6_ALL_SUBSTRINGS_OF_S_7GRAM)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSNge6Scoreboard(unittest.TestCase):
    """Cited-fixture S repeating n≥6 vs the S 7-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.s_sides = load_s_sides()
        measured = repeating_nge6_grams(self.by_tablet["S"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_s_7gram_substring(gram),
                nge6_sites(gram, self.s_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = s_repeating_nge6_all_substrings_of_s_7gram(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_s = tuple(
            off_s_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_94_95_n7_not_invented(self):
        """S 7-gram is a prior lock; both 6-grams are its measured slices."""
        self.assertEqual(STANDING_N7, INVENTORY_LONGEST_TOKENS["S"])
        self.assertEqual(STANDING_N7, S_N7_GRAM)
        self.assertEqual(STANDING_N7, GRAM7)
        self.assertEqual(INVENTORY_LONGEST_N["S"], 7)
        self.assertEqual(S_VENDOR_LONGEST_N, 7)
        self.assertEqual(len(STANDING_N7), 7)
        self.assertEqual(len(STANDING_N6_PREFIX), 6)
        self.assertEqual(len(STANDING_N6_SUFFIX), 6)
        self.assertEqual(
            STANDING_N7,
            ("004", "660", "081", "004", "660", "081", "004"),
        )
        self.assertEqual(
            STANDING_N6_PREFIX,
            ("004", "660", "081", "004", "660", "081"),
        )
        self.assertEqual(
            STANDING_N6_SUFFIX,
            ("660", "081", "004", "660", "081", "004"),
        )
        self.assertEqual(STANDING_N6_PREFIX, STANDING_N7[:6])
        self.assertEqual(STANDING_N6_SUFFIX, STANDING_N7[1:])
        self.assertTrue(is_s_7gram_substring(STANDING_N7))
        self.assertTrue(is_contiguous_substring(STANDING_N7, STANDING_N7))
        self.assertTrue(STANDING_N7_IS_SUBSTRING_OF_SELF)
        self.assertTrue(is_s_7gram_substring(STANDING_N6_PREFIX))
        self.assertTrue(is_s_7gram_substring(STANDING_N6_SUFFIX))
        self.assertTrue(STANDING_N6_PREFIX_IS_SUBSTRING)
        self.assertTrue(STANDING_N6_SUFFIX_IS_SUBSTRING)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["S"]["longest_tokens"]),
            STANDING_N7,
        )
        self.assertEqual(
            tuple(self.survey["tablet_s_washington_vendor"]["longest_tokens"]),
            STANDING_N7,
        )
        self.assertEqual(
            tuple(self.survey["tablet_s_washington_sb2_s_only"]["tokens7"]),
            STANDING_N7,
        )
        self.assertEqual(self.survey["tablet_s_washington_vendor"]["cycle"], 94)
        self.assertEqual(self.survey["tablet_s_washington_sb2_s_only"]["cycle"], 95)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["p_repeating_nge6"]["cycle"], 132)
        self.assertEqual(self.survey["q_repeating_nge7"]["cycle"], 131)
        self.assertEqual(self.survey["h_repeating_nge7"]["cycle"], 127)
        self.assertNotEqual(STANDING_N7, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_N6_PREFIX, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_N6_SUFFIX, INDEPENDENT_PLANT)
        self.assertFalse(is_s_7gram_substring(INDEPENDENT_PLANT))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_holds(self):
        """3 repeating n≥6; 3 substrings; 0 independent. Claim is true."""
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
        self.assertEqual(STANDING_LONGEST_N, 7)
        self.assertTrue(s_repeating_nge6_all_substrings_of_s_7gram(self.rows))
        self.assertEqual(self.claim_holds, STANDING_S_REPEATING_NGE6_ALL_SUBSTRINGS_OF_S_7GRAM)
        self.assertTrue(STANDING_S_REPEATING_NGE6_ALL_SUBSTRINGS_OF_S_7GRAM)
        self.assertEqual(STANDING_CLAIM, "s_repeating_nge6_all_substrings_of_s_7gram")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 0)
        n8 = self.analyzer.extract_ngrams(self.by_tablet["S"], n=8, min_frequency=2)
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
            self.assertEqual(is_s_7gram_substring(gram), is_sub)
            self.assertEqual(nge6_sites(gram, self.s_sides), sites)
            self.assertEqual(len(sites), freq)
        self.assertIn(STANDING_N7, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 7))
        self.assertIn(
            STANDING_N6_PREFIX,
            tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6),
        )
        self.assertIn(
            STANDING_N6_SUFFIX,
            tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6),
        )
        self.assertTrue(STANDING_N7_IN_SET)
        self.assertTrue(STANDING_N6_PREFIX_IN_SET)
        self.assertTrue(STANDING_N6_SUFFIX_IN_SET)
        sixgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6)
        self.assertEqual(sixgrams, (STANDING_N6_PREFIX, STANDING_N6_SUFFIX))
        sevengrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 7)
        self.assertEqual(sevengrams, (STANDING_N7,))
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_empty(self):
        """No S-local repeating n≥6 remainder off the S 7-gram."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertEqual(indep_tokens, ())
        self.assertNotIn(STANDING_N7, indep_tokens)
        self.assertNotIn(STANDING_N6_PREFIX, indep_tokens)
        self.assertNotIn(STANDING_N6_SUFFIX, indep_tokens)
        self.assertTrue(is_s_7gram_substring(STANDING_N7))
        self.assertTrue(is_s_7gram_substring(STANDING_N6_PREFIX))
        self.assertTrue(is_s_7gram_substring(STANDING_N6_SUFFIX))
        self.assertFalse(is_s_7gram_substring(INDEPENDENT_PLANT))
        self.assertNotIn(INDEPENDENT_PLANT, indep_tokens)
        self.assertEqual(len(indep_tokens), 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_home_sites_and_off_s_hits(self):
        """All three grams are Sb2-only; Sa=0; off-S 0; empty independent."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_s, STANDING_INDEPENDENT_OFF_S)
        self.assertEqual(STANDING_INDEPENDENT_OFF_S, ())
        self.assertEqual(self.indep_hits_by_tablet, ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_SA_HITS), ())
        self.assertEqual(tuple(STANDING_INDEPENDENT_SB_HITS), ())
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        for gram, n, freq, is_sub, sites in self.rows:
            self.assertTrue(is_sub)
            self.assertEqual(nge6_sites(gram, self.s_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(ngram_hit_count(self.s_sides[SIDE_SA], gram), 0)
            self.assertEqual(ngram_hit_count(self.s_sides[SIDE_SB], gram), freq)
            self.assertEqual(ngram_hit_count(self.by_tablet["S"], gram), freq)
            hits = tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            self.assertEqual(hits[VENDORED_TABLETS.index("S")], freq)
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "S":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("S", hits), {})
            self.assertEqual(off_s_hit_total(hits), 0)
            for side, line, index in sites:
                names = SA_LINE_NAMES if side == SIDE_SA else SB_LINE_NAMES
                stems = self.s_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_SB)
                self.assertEqual(line, "Sb2")
        self.assertEqual(
            nge6_sites(STANDING_N7, self.s_sides),
            ((SIDE_SB, "Sb2", 15), (SIDE_SB, "Sb2", 18)),
        )
        self.assertEqual(
            nge6_sites(STANDING_N6_PREFIX, self.s_sides),
            ((SIDE_SB, "Sb2", 15), (SIDE_SB, "Sb2", 18)),
        )
        self.assertEqual(
            nge6_sites(STANDING_N6_SUFFIX, self.s_sides),
            ((SIDE_SB, "Sb2", 16), (SIDE_SB, "Sb2", 19)),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_132_131_127_95_94_and_w_scoreboards_still_compute(self):
        """Cycle 132 P n≥6, 131 Q n≥7, 127 H n≥7, 95/94 S, and W stay."""
        prior_132 = TestMamariPNge6Scoreboard()
        prior_132.setUp()
        prior_132.test_counts_and_hypothesis_all_substrings_loses()
        prior_132.test_survey_matches_computed_lock()
        prior_131 = TestMamariQNge7Scoreboard()
        prior_131.setUp()
        prior_131.test_counts_and_hypothesis_all_substrings_loses()
        prior_131.test_survey_matches_computed_lock()
        prior_127 = TestMamariHNge7Scoreboard()
        prior_127.setUp()
        prior_127.test_counts_and_hypothesis_all_substrings_holds()
        prior_127.test_survey_matches_computed_lock()
        prior_95 = TestMamariWashingtonSb2SOnlyScoreboard()
        prior_95.setUp()
        prior_95.test_7gram_is_zero_off_s_and_s_only()
        prior_95.test_survey_matches_computed_lock()
        prior_94 = TestMamariWashingtonVendorScoreboard()
        prior_94.setUp()
        prior_94.test_longest_repeating_ngram_is_7()
        prior_94.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-133 n≥6 7-gram-substring lock."""
        lock = self.survey["s_repeating_nge6"]
        self.assertEqual(lock["cycle"], 133)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(tuple(lock["home_tokens7"]), STANDING_N7)
        self.assertEqual(tuple(lock["home_tokens6_prefix"]), STANDING_N6_PREFIX)
        self.assertEqual(tuple(lock["home_tokens6_suffix"]), STANDING_N6_SUFFIX)
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
                "off_s_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_s_hits"]), STANDING_INDEPENDENT_OFF_S)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n7_in_set"])
        self.assertTrue(lock["n6_prefix_in_set"])
        self.assertTrue(lock["n6_suffix_in_set"])
        self.assertTrue(lock["n7_is_substring_of_self"])
        self.assertTrue(lock["n6_prefix_is_substring"])
        self.assertTrue(lock["n6_suffix_is_substring"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(
            lock["s_repeating_nge6_all_substrings_of_s_7gram"],
            STANDING_S_REPEATING_NGE6_ALL_SUBSTRINGS_OF_S_7GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_p_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge7_unchanged"])
        self.assertTrue(lock["standing_h_repeating_nge7_unchanged"])
        self.assertTrue(lock["standing_s_washington_sb2_s_only_unchanged"])
        self.assertTrue(lock["standing_s_washington_vendor_unchanged"])
        self.assertTrue(lock["standing_p_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_h_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_k_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_g_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["p_repeating_nge6"]["cycle"], 132)
        self.assertEqual(self.survey["p_repeating_nge6"]["repeating_count"], 2)
        self.assertFalse(self.survey["p_repeating_nge6"]["p_repeating_nge6_all_substrings_of_p_6gram"])
        self.assertEqual(self.survey["q_repeating_nge7"]["cycle"], 131)
        self.assertEqual(self.survey["q_repeating_nge7"]["repeating_count"], 2)
        self.assertFalse(self.survey["q_repeating_nge7"]["q_repeating_nge7_all_substrings_of_hq_7gram"])
        self.assertEqual(self.survey["h_repeating_nge7"]["cycle"], 127)
        self.assertEqual(self.survey["h_repeating_nge7"]["repeating_count"], 1)
        self.assertTrue(self.survey["h_repeating_nge7"]["h_repeating_nge7_all_substrings_of_hq_7gram"])
        self.assertEqual(self.survey["tablet_s_washington_sb2_s_only"]["cycle"], 95)
        self.assertTrue(self.survey["tablet_s_washington_sb2_s_only"]["s_only"])
        self.assertEqual(
            tuple(self.survey["tablet_s_washington_sb2_s_only"]["tokens7"]),
            STANDING_N7,
        )
        self.assertEqual(self.survey["tablet_s_washington_vendor"]["cycle"], 94)
        self.assertEqual(self.survey["tablet_s_washington_vendor"]["longest_n"], 7)
        self.assertFalse(self.survey["tablet_s_washington_vendor"]["eightgram_exists"])
        self.assertEqual(self.survey["p_repeating_nge8"]["cycle"], 129)
        self.assertEqual(self.survey["p_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["p_repeating_nge8"]["p_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["q_repeating_nge8"]["cycle"], 128)
        self.assertEqual(self.survey["q_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["q_repeating_nge8"]["q_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["h_repeating_nge8"]["cycle"], 126)
        self.assertEqual(self.survey["h_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["h_repeating_nge8"]["h_repeating_nge8_all_substrings_of_hpq_islands"])
        self.assertEqual(self.survey["k_repeating_nge8"]["cycle"], 130)
        self.assertEqual(self.survey["k_repeating_nge8"]["repeating_count"], 0)
        self.assertTrue(self.survey["k_repeating_nge8"]["k_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(self.survey["g_repeating_nge8"]["cycle"], 125)
        self.assertFalse(self.survey["g_repeating_nge8"]["g_repeating_nge8_all_substrings_of_gk_islands"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["S"]["longest_n"], 7)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSNge6ImageSnapshot(unittest.TestCase):
    """Cycle 133 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
