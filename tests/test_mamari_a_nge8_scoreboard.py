"""A's repeating n≥8 grams vs the cycle-117 10-gram.

Cycle 122 text-search lock. Uses already-vendored A–V and the
cycle-36 / cycle-99 / cycle-116 / cycle-117 A representative
10-gram. Does not vendor a new tablet. Does not scrape X. W has
no Barthel (cycle 100); skip W. Does not redo G–K n≥8
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Enumerates every distinct contiguous n≥8 gram with freq≥2 on A
(same per-line Barthel parser as the leak table / A tengram
scoreboards). For each, whether it is an exact contiguous
substring of 080 004 280 182 048 022 025 025 009 005.
Hypothesis: no independent repeating n≥8 (every such gram is a
10-gram substring). Measured: 10 repeating n≥8; 6 are
substrings; 4 independent (the cycle-38/39 Ab 9-gram family plus
one other Ab 8-gram). Claim that can lose:
a_repeating_nge8_all_substrings_of_n10. The claim is false. Do
not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_a_tengram_scoreboard import (
    TestMamariATengramScoreboard,
    tengram_sites,
)
from tests.test_mamari_c_independent_nge8_maximals_scoreboard import (
    TestMamariCIndependentNge8MaximalsScoreboard,
)
from tests.test_mamari_c_nge8_scoreboard import (
    TestMamariCNge8Scoreboard,
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
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_tahua_aa_a_only_scoreboard import (
    GRAM10,
    SIDE_AA,
    SIDE_AB,
    STANDING_AA_SITES as CYCLE_116_AA_SITES,
    TestMamariTahuaAaAOnlyScoreboard,
    load_a_sides,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import (
    MOTIF_10GRAM,
    PREFIX_8GRAM as AA_8PREFIX,
)
from tests.test_mamari_tahua_aa_scoreboard import AA_LINE_NAMES
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import (
    MOTIF_AB_9GRAM,
    PREFIX_AB_8GRAM,
)
from tests.test_mamari_tahua_ab_scoreboard import (
    AB_LINE_NAMES,
    STANDING_EIGHTGRAM_COUNT as AB_EIGHTGRAM_COUNT,
    STANDING_LONGEST_NGRAM as AB_9GRAM,
    STANDING_TOP_8GRAM as AB_8PREFIX,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 8
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N10 = GRAM10
AB_8SUFFIX = (
    "003",
    "004",
    "600",
    "004",
    "003",
    "040",
    "003",
    "050",
)
AB_8EXTRA = (
    "003",
    "741",
    "003",
    "445",
    "003",
    "719",
    "450",
    "052",
)
STANDING_REPEATING_COUNT = 10
STANDING_SUBSTRING_COUNT = 6
STANDING_INDEPENDENT_COUNT = 4
STANDING_COUNTS_BY_N = {8: 6, 9: 3, 10: 1}
STANDING_SUBSTRING_BY_N = {8: 3, 9: 2, 10: 1}
STANDING_INDEPENDENT_BY_N = {8: 3, 9: 1, 10: 0}
STANDING_LONGEST_N = 10
# (tokens, n, freq, is_n10_substring, sites)
STANDING_ROWS = (
    (("080", "004", "280", "182", "048", "022", "025", "025"), 8, 2, True, (("Aa", "Aa7", 55), ("Aa", "Aa7", 88))),
    (("004", "280", "182", "048", "022", "025", "025", "009"), 8, 2, True, (("Aa", "Aa7", 56), ("Aa", "Aa7", 89))),
    (("280", "182", "048", "022", "025", "025", "009", "005"), 8, 2, True, (("Aa", "Aa7", 57), ("Aa", "Aa7", 90))),
    (("605", "003", "004", "600", "004", "003", "040", "003"), 8, 2, False, (("Ab", "Ab3", 2), ("Ab", "Ab5", 13))),
    (("003", "004", "600", "004", "003", "040", "003", "050"), 8, 2, False, (("Ab", "Ab3", 3), ("Ab", "Ab5", 14))),
    (("003", "741", "003", "445", "003", "719", "450", "052"), 8, 2, False, (("Ab", "Ab3", 22), ("Ab", "Ab5", 34))),
    (("080", "004", "280", "182", "048", "022", "025", "025", "009"), 9, 2, True, (("Aa", "Aa7", 55), ("Aa", "Aa7", 88))),
    (("004", "280", "182", "048", "022", "025", "025", "009", "005"), 9, 2, True, (("Aa", "Aa7", 56), ("Aa", "Aa7", 89))),
    (("605", "003", "004", "600", "004", "003", "040", "003", "050"), 9, 2, False, (("Ab", "Ab3", 2), ("Ab", "Ab5", 13))),
    (("080", "004", "280", "182", "048", "022", "025", "025", "009", "005"), 10, 2, True, (("Aa", "Aa7", 55), ("Aa", "Aa7", 88))),
)
STANDING_INDEPENDENT = tuple(
    (tokens, n, freq, sites)
    for tokens, n, freq, is_sub, sites in STANDING_ROWS
    if not is_sub
)
STANDING_INDEPENDENT_OFF_A = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_AA_HITS = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_AB_HITS = (2,) * STANDING_INDEPENDENT_COUNT
STANDING_KNOWN_DISTINCT = True
STANDING_N10_IN_SET = True
STANDING_AB_9GRAM_IN_INDEPENDENT = True
STANDING_AB_EXTRA_8_IN_INDEPENDENT = True
STANDING_CLAIM = "a_repeating_nge8_all_substrings_of_n10"
STANDING_A_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N10 = False
STANDING_RESULT = "a_repeating_nge8"
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
    a_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Aa then Ab. Search only."""
    hits = named_side_hits(a_sides[SIDE_AA], AA_LINE_NAMES, SIDE_AA, gram)
    hits += named_side_hits(a_sides[SIDE_AB], AB_LINE_NAMES, SIDE_AB, gram)
    return tuple(site_tuple(hit) for hit in hits)


def is_n10_substring(
    gram: tuple[str, ...],
    n10: tuple[str, ...] = STANDING_N10,
) -> bool:
    """True iff gram is an exact contiguous run inside the 10-gram."""
    return is_contiguous_substring(gram, n10)


def independent_rows(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Rows that are not exact contiguous substrings of the 10-gram."""
    return tuple(
        (tokens, n, freq, sites)
        for tokens, n, freq, is_sub, sites in rows
        if not is_sub
    )


def a_repeating_nge8_all_substrings_of_n10(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥8 is a 10-gram substring."""
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_a_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off A. Counts only."""
    return sum(leaks_from_hits("A", hits, tablets).values())


class TestANge8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted Ab 9-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = GRAM10
        planted = AB_9GRAM
        self.assertNotEqual(home, planted)
        self.assertEqual(len(home), 10)
        self.assertEqual(len(planted), 9)
        self.assertTrue(is_n10_substring(home))
        self.assertTrue(is_n10_substring(home[1:9]))
        self.assertFalse(is_n10_substring(planted))
        self.assertFalse(is_n10_substring(home + ("999",)))
        self.assertFalse(is_n10_substring(AB_8EXTRA))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge8_grams(once_each, analyzer), ())
        self.assertFalse(a_repeating_nge8_all_substrings_of_n10(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_nge8_grams(twice_home, analyzer)
        self.assertGreaterEqual(len(home_only), 1)
        self.assertIn((home, 10, 2), home_only)
        home_rows = tuple(
            (gram, n, freq, is_n10_substring(gram), ())
            for gram, n, freq in home_only
        )
        self.assertTrue(a_repeating_nge8_all_substrings_of_n10(home_rows))
        self.assertEqual(independent_rows(home_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge8_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_n10_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(a_repeating_nge8_all_substrings_of_n10(both_rows))
        self.assertIn(planted, tuple(gram for gram, n, _freq in both if n == 9))
        gapped = [list(home[:6]) + ["999"] + list(home[6:]), list(home)]
        self.assertEqual(repeating_nge8_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "a_repeating_nge8_all_substrings_of_n10")
        self.assertFalse(STANDING_A_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N10)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 4)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertFalse(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariANge8Scoreboard(unittest.TestCase):
    """Cited-fixture A repeating n≥8 vs the Aa 10-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.a_sides = load_a_sides()
        measured = repeating_nge8_grams(self.by_tablet["A"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_n10_substring(gram),
                nge8_sites(gram, self.a_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = a_repeating_nge8_all_substrings_of_n10(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_a = tuple(
            off_a_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_117_and_38_not_invented(self):
        """Aa 10-gram and Ab 9-gram are prior locks."""
        self.assertEqual(GRAM10, INVENTORY_LONGEST_TOKENS["A"])
        self.assertEqual(GRAM10, MOTIF_10GRAM)
        self.assertEqual(INVENTORY_LONGEST_N["A"], 10)
        self.assertEqual(len(GRAM10), 10)
        self.assertEqual(
            GRAM10,
            (
                "080",
                "004",
                "280",
                "182",
                "048",
                "022",
                "025",
                "025",
                "009",
                "005",
            ),
        )
        self.assertEqual(AB_9GRAM, MOTIF_AB_9GRAM)
        self.assertEqual(
            AB_9GRAM,
            ("605", "003", "004", "600", "004", "003", "040", "003", "050"),
        )
        self.assertEqual(AB_8PREFIX, PREFIX_AB_8GRAM)
        self.assertEqual(AB_8PREFIX, AB_9GRAM[:8])
        self.assertEqual(AB_8SUFFIX, AB_9GRAM[1:])
        self.assertEqual(AA_8PREFIX, GRAM10[:8])
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["longest_tokens"]),
            GRAM10,
        )
        self.assertEqual(tuple(self.survey["a_repeating_10grams"]["home_tokens10"]), GRAM10)
        self.assertEqual(self.survey["a_repeating_10grams"]["cycle"], 117)
        self.assertEqual(self.survey["tablet_a_tahua_aa_a_only"]["cycle"], 116)
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["cycle"], 37)
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["cycle"], 39)
        self.assertEqual(
            tuple(self.survey["tahua_ab_9gram_motif"]["motif_tokens"]),
            AB_9GRAM,
        )
        self.assertEqual(self.survey["tablet_a_tahua_side_b"]["cycle"], 38)
        self.assertEqual(self.survey["tablet_a_tahua_side_b"]["eightgram_count"], 3)
        self.assertEqual(AB_EIGHTGRAM_COUNT, 3)
        self.assertNotEqual(GRAM10, AB_9GRAM)
        self.assertNotEqual(GRAM10, AB_8EXTRA)
        self.assertNotEqual(AB_9GRAM, AB_8EXTRA)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_loses(self):
        """10 repeating n≥8; 6 substrings; 4 independent. Claim is false."""
        self.assertEqual(len(self.rows), STANDING_REPEATING_COUNT)
        self.assertEqual(self.substring_count, STANDING_SUBSTRING_COUNT)
        self.assertEqual(len(self.independent), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_REPEATING_COUNT, 10)
        self.assertEqual(STANDING_SUBSTRING_COUNT, 6)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 4)
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
        self.assertFalse(a_repeating_nge8_all_substrings_of_n10(self.rows))
        self.assertEqual(self.claim_holds, STANDING_A_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N10)
        self.assertFalse(STANDING_A_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N10)
        self.assertEqual(STANDING_CLAIM, "a_repeating_nge8_all_substrings_of_n10")
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
            self.assertEqual(is_n10_substring(gram), is_sub)
            self.assertEqual(nge8_sites(gram, self.a_sides), sites)
            self.assertEqual(len(sites), freq)
        self.assertIn(GRAM10, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 10))
        self.assertTrue(STANDING_N10_IN_SET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_ab_9gram_family_and_extra_8(self):
        """Independent grams are the Ab 9-gram family plus one other Ab 8-gram."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertIn(AB_9GRAM, indep_tokens)
        self.assertIn(AB_8PREFIX, indep_tokens)
        self.assertIn(AB_8SUFFIX, indep_tokens)
        self.assertIn(AB_8EXTRA, indep_tokens)
        self.assertTrue(STANDING_AB_9GRAM_IN_INDEPENDENT)
        self.assertTrue(STANDING_AB_EXTRA_8_IN_INDEPENDENT)
        self.assertNotIn(GRAM10, indep_tokens)
        self.assertFalse(is_n10_substring(AB_9GRAM))
        self.assertFalse(is_n10_substring(AB_8PREFIX))
        self.assertFalse(is_n10_substring(AB_8SUFFIX))
        self.assertFalse(is_n10_substring(AB_8EXTRA))
        self.assertFalse(is_contiguous_substring(AB_8EXTRA, AB_9GRAM))
        ab_family = {AB_9GRAM, AB_8PREFIX, AB_8SUFFIX}
        extras = tuple(gram for gram in indep_tokens if gram not in ab_family)
        self.assertEqual(len(ab_family), 3)
        self.assertEqual(len(extras), 1)
        self.assertEqual(extras, (AB_8EXTRA,))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_a_hits(self):
        """Independent A sites; Aa=0; off-A 0 on every vendored tablet."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_a, STANDING_INDEPENDENT_OFF_A)
        self.assertEqual(STANDING_INDEPENDENT_OFF_A, (0,) * 4)
        for (gram, n, freq, sites), hits, off_hits in zip(
            self.independent,
            self.indep_hits_by_tablet,
            self.indep_off_a,
            strict=True,
        ):
            self.assertEqual(nge8_sites(gram, self.a_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("A")], freq)
            self.assertEqual(ngram_hit_count(self.a_sides[SIDE_AA], gram), 0)
            self.assertEqual(ngram_hit_count(self.a_sides[SIDE_AB], gram), freq)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "A":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("A", hits), {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = AA_LINE_NAMES if side == SIDE_AA else AB_LINE_NAMES
                stems = self.a_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_AB)
                self.assertIn(line, ("Ab3", "Ab5"))
        family_sites = tuple(
            sites
            for gram, _n, _freq, sites in self.independent
            if gram in {AB_9GRAM, AB_8PREFIX, AB_8SUFFIX}
        )
        for sites in family_sites:
            self.assertTrue(all(line in ("Ab3", "Ab5") for _side, line, _i in sites))
        self.assertEqual(tengram_sites(GRAM10, self.a_sides), CYCLE_116_AA_SITES)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(tuple(STANDING_INDEPENDENT_AA_HITS), (0,) * 4)
        self.assertEqual(tuple(STANDING_INDEPENDENT_AB_HITS), (2,) * 4)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_121_120_117_and_w_scoreboards_still_compute(self):
        """Cycle 121 C maximals, 120 C n≥8, 117 A 10-grams, and W stay."""
        prior_121 = TestMamariCIndependentNge8MaximalsScoreboard()
        prior_121.setUp()
        prior_121.test_n_is_3_and_hypothesis_n_2_loses()
        prior_121.test_survey_matches_computed_lock()
        prior_120 = TestMamariCNge8Scoreboard()
        prior_120.setUp()
        prior_120.test_counts_and_hypothesis_all_substrings_loses()
        prior_120.test_survey_matches_computed_lock()
        prior_117 = TestMamariATengramScoreboard()
        prior_117.setUp()
        prior_117.test_n_is_1_and_hypothesis_n_1_holds()
        prior_117.test_survey_matches_computed_lock()
        prior_116 = TestMamariTahuaAaAOnlyScoreboard()
        prior_116.setUp()
        prior_116.test_10gram_is_zero_off_a_and_a_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-122 n≥8 substring lock."""
        lock = self.survey["a_repeating_nge8"]
        self.assertEqual(lock["cycle"], 122)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(tuple(lock["home_tokens10"]), GRAM10)
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
                "off_a_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_a_hits"]), STANDING_INDEPENDENT_OFF_A)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n10_in_set"])
        self.assertTrue(lock["ab_9gram_in_independent"])
        self.assertTrue(lock["ab_extra_8_in_independent"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["a_repeating_nge8_all_substrings_of_n10"])
        self.assertEqual(
            lock["a_repeating_nge8_all_substrings_of_n10"],
            STANDING_A_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N10,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_a_repeating_10grams_unchanged"])
        self.assertTrue(lock["standing_c_independent_nge8_maximals_unchanged"])
        self.assertTrue(lock["standing_c_repeating_nge8_unchanged"])
        self.assertTrue(lock["standing_tahua_aa_a_only_unchanged"])
        self.assertTrue(lock["standing_tahua_ab_9gram_motif_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["a_repeating_10grams"]["cycle"], 117)
        self.assertTrue(self.survey["a_repeating_10grams"]["a_has_exactly_1_repeating_10gram"])
        self.assertEqual(self.survey["c_independent_nge8_maximals"]["cycle"], 121)
        self.assertFalse(self.survey["c_independent_nge8_maximals"]["c_independent_nge8_has_exactly_2_maximals"])
        self.assertEqual(self.survey["c_repeating_nge8"]["cycle"], 120)
        self.assertFalse(self.survey["c_repeating_nge8"]["c_repeating_nge8_all_substrings_of_n13"])
        self.assertEqual(self.survey["tablet_a_tahua_aa_a_only"]["cycle"], 116)
        self.assertTrue(self.survey["tablet_a_tahua_aa_a_only"]["a_10gram_is_a_only"])
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["cycle"], 39)
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["motif_freq"], 2)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["longest_count"], 1)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariANge8ImageSnapshot(unittest.TestCase):
    """Cycle 122 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
