"""E's repeating n≥8 grams vs the cycle-81 9-gram.

Cycle 124 text-search lock. Uses already-vendored A–V and the
cycle-80 / cycle-81 / cycle-83 / cycle-99 E representative
9-gram. Does not vendor a new tablet. Does not scrape X. W has
no Barthel (cycle 100); skip W. Does not redo G–K n≥8
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Enumerates every distinct contiguous n≥8 gram with freq≥2 on E
(same per-line Barthel parser as the leak table / E n=9
scoreboards). For each, whether it is an exact contiguous
substring of 300 040 300 028 004 430 022 380 203.
Hypothesis: no independent repeating n≥8 (every such gram is a
9-gram substring). Measured: 5 repeating n≥8; 3 are
substrings; 2 independent (the two cycle-83 independent Er
8-grams). Claim that can lose:
e_repeating_nge8_all_substrings_of_n9. The claim is false. Do
not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_a_independent_nge8_maximals_scoreboard import (
    TestMamariAIndependentNge8MaximalsScoreboard,
)
from tests.test_mamari_a_nge8_scoreboard import (
    TestMamariANge8Scoreboard,
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
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_keiti_eightgram_scoreboard import (
    STANDING_EIGHTGRAMS,
    STANDING_FROM_N9 as EIGHTGRAM_FROM_N9,
    STANDING_SITES as EIGHTGRAM_SITES,
    TestMamariKeitiEightgramScoreboard,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
    GRAM8 as ER7_DOUBLE_8GRAM,
    TestMamariKeitiEr7DoubleScoreboard,
)
from tests.test_mamari_keiti_ev_longest_scoreboard import (
    N9_PREFIX8,
    N9_SUFFIX8,
    STANDING_EV_HAS_N_GE_8,
    STANDING_EV_LONGEST_N,
    TestMamariKeitiEvLongestScoreboard,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    GRAM_N9,
    STANDING_ER_SITES as N9_ER_SITES,
    TestMamariKeitiN9Scoreboard,
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_keiti_vendor_scoreboard import (
    E_LINE_NAMES,
    SIDE_ER,
    SIDE_EV,
    STANDING_EIGHTGRAM_COUNT,
    STANDING_LONGEST_NGRAM,
    TestMamariKeitiVendorScoreboard,
    load_e_sides,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 8
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N9 = GRAM_N9
ER_8LEFT = (
    "040",
    "300",
    "040",
    "300",
    "028",
    "004",
    "430",
    "022",
)
ER_8DOUBLE = ER7_DOUBLE_8GRAM
STANDING_REPEATING_COUNT = 5
STANDING_SUBSTRING_COUNT = 3
STANDING_INDEPENDENT_COUNT = 2
STANDING_COUNTS_BY_N = {8: 4, 9: 1}
STANDING_SUBSTRING_BY_N = {8: 2, 9: 1}
STANDING_INDEPENDENT_BY_N = {8: 2, 9: 0}
STANDING_LONGEST_N = 9
# (tokens, n, freq, is_n9_substring, sites)
STANDING_ROWS = (
    (("040", "300", "028", "004", "430", "022", "380", "203"), 8, 3, True, (("Er", "Er2", 12), ("Er", "Er2", 29), ("Er", "Er3", 11))),
    (("300", "040", "300", "028", "004", "430", "022", "380"), 8, 2, True, (("Er", "Er2", 11), ("Er", "Er2", 28))),
    (("040", "300", "040", "300", "028", "004", "430", "022"), 8, 2, False, (("Er", "Er2", 27), ("Er", "Er4", 1))),
    (("092", "050", "006", "670", "092", "050", "006", "670"), 8, 2, False, (("Er", "Er7", 7), ("Er", "Er7", 11))),
    (("300", "040", "300", "028", "004", "430", "022", "380", "203"), 9, 2, True, (("Er", "Er2", 11), ("Er", "Er2", 28))),
)
STANDING_INDEPENDENT = tuple(
    (tokens, n, freq, sites)
    for tokens, n, freq, is_sub, sites in STANDING_ROWS
    if not is_sub
)
STANDING_INDEPENDENT_OFF_E = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_ER_HITS = (2,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_EV_HITS = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_KNOWN_DISTINCT = True
STANDING_N9_IN_SET = True
STANDING_ER_INDEPENDENT_8GRAMS_IN_INDEPENDENT = True
STANDING_CLAIM = "e_repeating_nge8_all_substrings_of_n9"
STANDING_E_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N9 = False
STANDING_RESULT = "e_repeating_nge8"
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
    e_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Er then Ev. Search only."""
    hits = named_side_hits(e_sides[SIDE_ER], E_LINE_NAMES[SIDE_ER], SIDE_ER, gram)
    hits += named_side_hits(e_sides[SIDE_EV], E_LINE_NAMES[SIDE_EV], SIDE_EV, gram)
    return tuple(site_tuple(hit) for hit in hits)


def is_n9_substring(
    gram: tuple[str, ...],
    n9: tuple[str, ...] = STANDING_N9,
) -> bool:
    """True iff gram is an exact contiguous run inside the 9-gram."""
    return is_contiguous_substring(gram, n9)


def independent_rows(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Rows that are not exact contiguous substrings of the 9-gram."""
    return tuple(
        (tokens, n, freq, sites)
        for tokens, n, freq, is_sub, sites in rows
        if not is_sub
    )


def e_repeating_nge8_all_substrings_of_n9(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥8 is a 9-gram substring."""
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_e_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off E. Counts only."""
    return sum(leaks_from_hits("E", hits, tablets).values())


class TestENge8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted Er 8-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = GRAM_N9
        planted = ER_8DOUBLE
        self.assertNotEqual(home, planted)
        self.assertEqual(len(home), 9)
        self.assertEqual(len(planted), 8)
        self.assertTrue(is_n9_substring(home))
        self.assertTrue(is_n9_substring(home[1:9]))
        self.assertTrue(is_n9_substring(home[:8]))
        self.assertFalse(is_n9_substring(planted))
        self.assertFalse(is_n9_substring(home + ("999",)))
        self.assertFalse(is_n9_substring(ER_8LEFT))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge8_grams(once_each, analyzer), ())
        self.assertFalse(e_repeating_nge8_all_substrings_of_n9(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_nge8_grams(twice_home, analyzer)
        self.assertGreaterEqual(len(home_only), 1)
        self.assertIn((home, 9, 2), home_only)
        home_rows = tuple(
            (gram, n, freq, is_n9_substring(gram), ())
            for gram, n, freq in home_only
        )
        self.assertTrue(e_repeating_nge8_all_substrings_of_n9(home_rows))
        self.assertEqual(independent_rows(home_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge8_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_n9_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(e_repeating_nge8_all_substrings_of_n9(both_rows))
        self.assertIn(planted, tuple(gram for gram, n, _freq in both if n == 8))
        gapped = [list(home[:5]) + ["999"] + list(home[5:]), list(home)]
        self.assertEqual(repeating_nge8_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "e_repeating_nge8_all_substrings_of_n9")
        self.assertFalse(STANDING_E_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N9)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 2)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertFalse(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariENge8Scoreboard(unittest.TestCase):
    """Cited-fixture E repeating n≥8 vs the Er 9-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.e_sides = load_e_sides()
        measured = repeating_nge8_grams(self.by_tablet["E"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_n9_substring(gram),
                nge8_sites(gram, self.e_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = e_repeating_nge8_all_substrings_of_n9(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_e = tuple(
            off_e_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_81_and_83_not_invented(self):
        """Er 9-gram and the two independent Er 8-grams are prior locks."""
        self.assertEqual(GRAM_N9, INVENTORY_LONGEST_TOKENS["E"])
        self.assertEqual(GRAM_N9, STANDING_LONGEST_NGRAM)
        self.assertEqual(INVENTORY_LONGEST_N["E"], 9)
        self.assertEqual(len(GRAM_N9), 9)
        self.assertEqual(
            GRAM_N9,
            (
                "300",
                "040",
                "300",
                "028",
                "004",
                "430",
                "022",
                "380",
                "203",
            ),
        )
        self.assertEqual(N9_PREFIX8, GRAM_N9[:8])
        self.assertEqual(N9_SUFFIX8, GRAM_N9[1:])
        self.assertEqual(ER_8LEFT, STANDING_EIGHTGRAMS[2])
        self.assertEqual(ER_8DOUBLE, STANDING_EIGHTGRAMS[3])
        self.assertEqual(ER_8DOUBLE, ER7_DOUBLE_8GRAM)
        self.assertEqual(EIGHTGRAM_FROM_N9, (True, True, False, False))
        self.assertEqual(STANDING_EIGHTGRAM_COUNT, 4)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["E"]["longest_tokens"]),
            GRAM_N9,
        )
        self.assertEqual(tuple(self.survey["tablet_e_keiti_n9_sites"]["tokens"]), GRAM_N9)
        self.assertEqual(self.survey["tablet_e_keiti_n9_sites"]["cycle"], 81)
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["cycle"], 80)
        self.assertEqual(self.survey["tablet_e_keiti_eightgrams"]["cycle"], 83)
        self.assertEqual(self.survey["tablet_e_keiti_ev_longest"]["cycle"], 82)
        self.assertEqual(self.survey["tablet_e_keiti_er7_double"]["cycle"], 84)
        self.assertEqual(
            tuple(tuple(row) for row in self.survey["tablet_e_keiti_eightgrams"]["tokens"]),
            STANDING_EIGHTGRAMS,
        )
        self.assertEqual(
            tuple(self.survey["tablet_e_keiti_er7_double"]["tokens8"]),
            ER_8DOUBLE,
        )
        self.assertNotEqual(GRAM_N9, ER_8LEFT)
        self.assertNotEqual(GRAM_N9, ER_8DOUBLE)
        self.assertNotEqual(ER_8LEFT, ER_8DOUBLE)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_loses(self):
        """5 repeating n≥8; 3 substrings; 2 independent. Claim is false."""
        self.assertEqual(len(self.rows), STANDING_REPEATING_COUNT)
        self.assertEqual(self.substring_count, STANDING_SUBSTRING_COUNT)
        self.assertEqual(len(self.independent), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_REPEATING_COUNT, 5)
        self.assertEqual(STANDING_SUBSTRING_COUNT, 3)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 2)
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
        self.assertEqual(indep_by_n, {k: v for k, v in STANDING_INDEPENDENT_BY_N.items() if v})
        self.assertEqual(max(by_n), STANDING_LONGEST_N)
        self.assertFalse(e_repeating_nge8_all_substrings_of_n9(self.rows))
        self.assertEqual(self.claim_holds, STANDING_E_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N9)
        self.assertFalse(STANDING_E_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N9)
        self.assertEqual(STANDING_CLAIM, "e_repeating_nge8_all_substrings_of_n9")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertFalse(STANDING_EV_HAS_N_GE_8)
        self.assertEqual(STANDING_EV_LONGEST_N, 6)
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
            self.assertEqual(is_n9_substring(gram), is_sub)
            self.assertEqual(nge8_sites(gram, self.e_sides), sites)
            self.assertEqual(len(sites), freq)
        self.assertIn(GRAM_N9, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 9))
        self.assertTrue(STANDING_N9_IN_SET)
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, STANDING_EIGHTGRAMS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_the_two_cycle_83_er_8grams(self):
        """Independent grams are exactly the two cycle-83 Er 8-grams."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertIn(ER_8LEFT, indep_tokens)
        self.assertIn(ER_8DOUBLE, indep_tokens)
        self.assertTrue(STANDING_ER_INDEPENDENT_8GRAMS_IN_INDEPENDENT)
        self.assertNotIn(GRAM_N9, indep_tokens)
        self.assertNotIn(N9_PREFIX8, indep_tokens)
        self.assertNotIn(N9_SUFFIX8, indep_tokens)
        self.assertFalse(is_n9_substring(ER_8LEFT))
        self.assertFalse(is_n9_substring(ER_8DOUBLE))
        self.assertTrue(is_n9_substring(N9_PREFIX8))
        self.assertTrue(is_n9_substring(N9_SUFFIX8))
        self.assertFalse(is_contiguous_substring(ER_8LEFT, GRAM_N9))
        self.assertFalse(is_contiguous_substring(ER_8DOUBLE, GRAM_N9))
        known = tuple(
            gram
            for gram, from_n9 in zip(STANDING_EIGHTGRAMS, EIGHTGRAM_FROM_N9, strict=True)
            if not from_n9
        )
        self.assertEqual(known, (ER_8LEFT, ER_8DOUBLE))
        self.assertEqual(indep_tokens, known)
        self.assertEqual(len(indep_tokens), 2)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_e_hits(self):
        """Independent E sites; Ev=0; off-E 0 on every vendored tablet."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_e, STANDING_INDEPENDENT_OFF_E)
        self.assertEqual(STANDING_INDEPENDENT_OFF_E, (0,) * 2)
        for (gram, n, freq, sites), hits, off_hits in zip(
            self.independent,
            self.indep_hits_by_tablet,
            self.indep_off_e,
            strict=True,
        ):
            self.assertEqual(nge8_sites(gram, self.e_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("E")], freq)
            self.assertEqual(ngram_hit_count(self.e_sides[SIDE_ER], gram), freq)
            self.assertEqual(ngram_hit_count(self.e_sides[SIDE_EV], gram), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "E":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("E", hits), {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = E_LINE_NAMES[side]
                stems = self.e_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_ER)
                self.assertIn(line, ("Er2", "Er4", "Er7"))
        self.assertEqual(
            nge8_sites(ER_8LEFT, self.e_sides),
            EIGHTGRAM_SITES[2],
        )
        self.assertEqual(
            nge8_sites(ER_8DOUBLE, self.e_sides),
            EIGHTGRAM_SITES[3],
        )
        self.assertEqual(nge8_sites(GRAM_N9, self.e_sides), N9_ER_SITES)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(tuple(STANDING_INDEPENDENT_ER_HITS), (2,) * 2)
        self.assertEqual(tuple(STANDING_INDEPENDENT_EV_HITS), (0,) * 2)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_123_122_83_and_w_scoreboards_still_compute(self):
        """Cycle 123 A maximals, 122 A n≥8, 83 E eightgrams, and W stay."""
        prior_123 = TestMamariAIndependentNge8MaximalsScoreboard()
        prior_123.setUp()
        prior_123.test_n_is_2_and_hypothesis_n_2_holds()
        prior_123.test_survey_matches_computed_lock()
        prior_122 = TestMamariANge8Scoreboard()
        prior_122.setUp()
        prior_122.test_counts_and_hypothesis_all_substrings_loses()
        prior_122.test_survey_matches_computed_lock()
        prior_83 = TestMamariKeitiEightgramScoreboard()
        prior_83.setUp()
        prior_83.test_has_independent_8gram_and_not_all_from_n9()
        prior_83.test_survey_matches_computed_lock()
        prior_81 = TestMamariKeitiN9Scoreboard()
        prior_81.setUp()
        prior_81.test_n9_is_er_only_at_er2()
        prior_81.test_survey_matches_computed_lock()
        prior_82 = TestMamariKeitiEvLongestScoreboard()
        prior_82.setUp()
        prior_82.test_ev_longest_is_n6_and_has_no_n_ge_8()
        prior_84 = TestMamariKeitiEr7DoubleScoreboard()
        prior_84.setUp()
        prior_84.test_survey_matches_computed_lock()
        prior_80 = TestMamariKeitiVendorScoreboard()
        prior_80.setUp()
        prior_80.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-124 n≥8 substring lock."""
        lock = self.survey["e_repeating_nge8"]
        self.assertEqual(lock["cycle"], 124)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(tuple(lock["home_tokens9"]), GRAM_N9)
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
                "off_e_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_e_hits"]), STANDING_INDEPENDENT_OFF_E)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n9_in_set"])
        self.assertTrue(lock["er_independent_8grams_in_independent"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["e_repeating_nge8_all_substrings_of_n9"])
        self.assertEqual(
            lock["e_repeating_nge8_all_substrings_of_n9"],
            STANDING_E_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N9,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_e_keiti_n9_sites_unchanged"])
        self.assertTrue(lock["standing_e_keiti_eightgrams_unchanged"])
        self.assertTrue(lock["standing_e_keiti_ev_longest_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertTrue(lock["standing_a_independent_nge8_maximals_unchanged"])
        self.assertTrue(lock["standing_a_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_c_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_e_keiti_n9_sites"]["cycle"], 81)
        self.assertTrue(self.survey["tablet_e_keiti_n9_sites"]["side_local"])
        self.assertEqual(self.survey["tablet_e_keiti_n9_sites"]["er_hits"], 2)
        self.assertEqual(self.survey["tablet_e_keiti_eightgrams"]["cycle"], 83)
        self.assertTrue(self.survey["tablet_e_keiti_eightgrams"]["has_independent_8gram"])
        self.assertEqual(self.survey["tablet_e_keiti_eightgrams"]["independent_count"], 2)
        self.assertEqual(self.survey["tablet_e_keiti_ev_longest"]["cycle"], 82)
        self.assertFalse(self.survey["tablet_e_keiti_ev_longest"]["ev_has_n_ge_8"])
        self.assertEqual(self.survey["tablet_e_keiti_er7_double"]["cycle"], 84)
        self.assertTrue(self.survey["tablet_e_keiti_er7_double"]["e_only"])
        self.assertEqual(self.survey["a_independent_nge8_maximals"]["cycle"], 123)
        self.assertTrue(self.survey["a_independent_nge8_maximals"]["a_independent_nge8_has_exactly_2_maximals"])
        self.assertEqual(self.survey["a_repeating_nge8"]["cycle"], 122)
        self.assertFalse(self.survey["a_repeating_nge8"]["a_repeating_nge8_all_substrings_of_n10"])
        self.assertEqual(self.survey["c_repeating_nge8"]["cycle"], 120)
        self.assertFalse(self.survey["c_repeating_nge8"]["c_repeating_nge8_all_substrings_of_n13"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["E"]["longest_n"], 9)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariENge8ImageSnapshot(unittest.TestCase):
    """Cycle 124 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
