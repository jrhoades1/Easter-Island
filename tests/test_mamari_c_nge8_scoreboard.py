"""C's repeating n≥8 grams vs the cycle-119 calendar 13-gram.

Cycle 120 text-search lock. Uses already-vendored A–V and the
cycle-24 / cycle-99 / cycle-118 / cycle-119 C representative
13-gram. Does not vendor a new tablet. Does not scrape X. W has
no Barthel (cycle 100); skip W. Does not redo G–K n≥8
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Enumerates every distinct contiguous n≥8 gram with freq≥2 on C
(same per-line Barthel parser as the leak table / C thirteengram
scoreboards). For each, whether it is an exact contiguous
substring of 040 040 040 040 040 390 041 378 041 670 008 078
711. Hypothesis: no independent repeating n≥8 (every such gram
is a 13-gram substring). Measured: 32 repeating n≥8; 21 are
substrings; 11 independent (Guy-delimiter + trailing 040, plus
the cycle-29/30 remainder 9-gram family). Claim that can lose:
c_repeating_nge8_all_substrings_of_n13. The claim is false. Do
not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_b_eightgram_scoreboard import (
    TestMamariBEightgramScoreboard,
)
from tests.test_mamari_c_thirteengram_scoreboard import (
    TestMamariCThirteengramScoreboard,
    thirteengram_sites,
)
from tests.test_mamari_ca_c_only_scoreboard import (
    CA_LINE_NAMES,
    GRAM13,
    SIDE_CA,
    SIDE_CB,
    STANDING_CA_SITES as CYCLE_118_CA_SITES,
    TestMamariCaCOnlyScoreboard,
    load_c_sides,
)
from tests.test_mamari_cb_side_b_scoreboard import CB_LINE_NAMES
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
from tests.test_mamari_remainder_9gram_motif_scoreboard import MOTIF_9GRAM
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_LONGEST_NGRAM as REMAINDER_9GRAM,
    STANDING_TOP_8GRAM as REMAINDER_8PREFIX,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 8
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N13 = GRAM13
STANDING_REPEATING_COUNT = 32
STANDING_SUBSTRING_COUNT = 21
STANDING_INDEPENDENT_COUNT = 11
STANDING_COUNTS_BY_N = {8: 10, 9: 8, 10: 6, 11: 4, 12: 3, 13: 1}
STANDING_SUBSTRING_BY_N = {8: 6, 9: 5, 10: 4, 11: 3, 12: 2, 13: 1}
STANDING_INDEPENDENT_BY_N = {8: 4, 9: 3, 10: 2, 11: 1, 12: 1, 13: 0}
STANDING_LONGEST_N = 13
REMAINDER_8SUFFIX = (
    "010",
    "070",
    "760",
    "040",
    "006",
    "430",
    "047",
    "002",
)
# (tokens, n, freq, is_n13_substring, sites)
STANDING_ROWS = (
    (("390", "041", "378", "041", "670", "008", "078", "711"), 8, 6, True, (("Ca", "Ca7", 6), ("Ca", "Ca7", 19), ("Ca", "Ca7", 33), ("Ca", "Ca8", 3), ("Ca", "Ca8", 15), ("Ca", "Ca8", 29))),
    (("040", "390", "041", "378", "041", "670", "008", "078"), 8, 5, True, (("Ca", "Ca7", 5), ("Ca", "Ca7", 18), ("Ca", "Ca8", 2), ("Ca", "Ca8", 14), ("Ca", "Ca8", 28))),
    (("040", "040", "040", "390", "041", "378", "041", "670"), 8, 3, True, (("Ca", "Ca7", 3), ("Ca", "Ca8", 0), ("Ca", "Ca8", 26))),
    (("040", "040", "390", "041", "378", "041", "670", "008"), 8, 3, True, (("Ca", "Ca7", 4), ("Ca", "Ca8", 1), ("Ca", "Ca8", 27))),
    (("041", "378", "041", "670", "008", "078", "711", "040"), 8, 3, False, (("Ca", "Ca7", 7), ("Ca", "Ca7", 34), ("Ca", "Ca8", 4))),
    (("040", "040", "040", "040", "040", "390", "041", "378"), 8, 2, True, (("Ca", "Ca7", 1), ("Ca", "Ca8", 24))),
    (("040", "040", "040", "040", "390", "041", "378", "041"), 8, 2, True, (("Ca", "Ca7", 2), ("Ca", "Ca8", 25))),
    (("378", "041", "670", "008", "078", "711", "040", "040"), 8, 2, False, (("Ca", "Ca7", 35), ("Ca", "Ca8", 5))),
    (("002", "010", "070", "760", "040", "006", "430", "047"), 8, 2, False, (("Ca", "Ca10", 26), ("Ca", "Ca11", 14))),
    (("010", "070", "760", "040", "006", "430", "047", "002"), 8, 2, False, (("Ca", "Ca10", 27), ("Ca", "Ca11", 15))),
    (("040", "390", "041", "378", "041", "670", "008", "078", "711"), 9, 5, True, (("Ca", "Ca7", 5), ("Ca", "Ca7", 18), ("Ca", "Ca8", 2), ("Ca", "Ca8", 14), ("Ca", "Ca8", 28))),
    (("040", "040", "040", "390", "041", "378", "041", "670", "008"), 9, 3, True, (("Ca", "Ca7", 3), ("Ca", "Ca8", 0), ("Ca", "Ca8", 26))),
    (("040", "040", "390", "041", "378", "041", "670", "008", "078"), 9, 3, True, (("Ca", "Ca7", 4), ("Ca", "Ca8", 1), ("Ca", "Ca8", 27))),
    (("390", "041", "378", "041", "670", "008", "078", "711", "040"), 9, 3, False, (("Ca", "Ca7", 6), ("Ca", "Ca7", 33), ("Ca", "Ca8", 3))),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041"), 9, 2, True, (("Ca", "Ca7", 1), ("Ca", "Ca8", 24))),
    (("040", "040", "040", "040", "390", "041", "378", "041", "670"), 9, 2, True, (("Ca", "Ca7", 2), ("Ca", "Ca8", 25))),
    (("041", "378", "041", "670", "008", "078", "711", "040", "040"), 9, 2, False, (("Ca", "Ca7", 34), ("Ca", "Ca8", 4))),
    (("002", "010", "070", "760", "040", "006", "430", "047", "002"), 9, 2, False, (("Ca", "Ca10", 26), ("Ca", "Ca11", 14))),
    (("040", "040", "040", "390", "041", "378", "041", "670", "008", "078"), 10, 3, True, (("Ca", "Ca7", 3), ("Ca", "Ca8", 0), ("Ca", "Ca8", 26))),
    (("040", "040", "390", "041", "378", "041", "670", "008", "078", "711"), 10, 3, True, (("Ca", "Ca7", 4), ("Ca", "Ca8", 1), ("Ca", "Ca8", 27))),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041", "670"), 10, 2, True, (("Ca", "Ca7", 1), ("Ca", "Ca8", 24))),
    (("040", "040", "040", "040", "390", "041", "378", "041", "670", "008"), 10, 2, True, (("Ca", "Ca7", 2), ("Ca", "Ca8", 25))),
    (("040", "390", "041", "378", "041", "670", "008", "078", "711", "040"), 10, 2, False, (("Ca", "Ca7", 5), ("Ca", "Ca8", 2))),
    (("390", "041", "378", "041", "670", "008", "078", "711", "040", "040"), 10, 2, False, (("Ca", "Ca7", 33), ("Ca", "Ca8", 3))),
    (("040", "040", "040", "390", "041", "378", "041", "670", "008", "078", "711"), 11, 3, True, (("Ca", "Ca7", 3), ("Ca", "Ca8", 0), ("Ca", "Ca8", 26))),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041", "670", "008"), 11, 2, True, (("Ca", "Ca7", 1), ("Ca", "Ca8", 24))),
    (("040", "040", "040", "040", "390", "041", "378", "041", "670", "008", "078"), 11, 2, True, (("Ca", "Ca7", 2), ("Ca", "Ca8", 25))),
    (("040", "040", "390", "041", "378", "041", "670", "008", "078", "711", "040"), 11, 2, False, (("Ca", "Ca7", 4), ("Ca", "Ca8", 1))),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041", "670", "008", "078"), 12, 2, True, (("Ca", "Ca7", 1), ("Ca", "Ca8", 24))),
    (("040", "040", "040", "040", "390", "041", "378", "041", "670", "008", "078", "711"), 12, 2, True, (("Ca", "Ca7", 2), ("Ca", "Ca8", 25))),
    (("040", "040", "040", "390", "041", "378", "041", "670", "008", "078", "711", "040"), 12, 2, False, (("Ca", "Ca7", 3), ("Ca", "Ca8", 0))),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041", "670", "008", "078", "711"), 13, 2, True, (("Ca", "Ca7", 1), ("Ca", "Ca8", 24))),
)
STANDING_INDEPENDENT = tuple(
    (tokens, n, freq, sites)
    for tokens, n, freq, is_sub, sites in STANDING_ROWS
    if not is_sub
)
STANDING_INDEPENDENT_OFF_C = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_CB_HITS = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_KNOWN_DISTINCT = True
STANDING_N13_IN_SET = True
STANDING_REMAINDER_IN_INDEPENDENT = True
STANDING_CLAIM = "c_repeating_nge8_all_substrings_of_n13"
STANDING_C_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N13 = False
STANDING_RESULT = "c_repeating_nge8"
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
    c_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Ca then Cb. Search only."""
    hits = named_side_hits(c_sides[SIDE_CA], CA_LINE_NAMES, SIDE_CA, gram)
    hits += named_side_hits(c_sides[SIDE_CB], CB_LINE_NAMES, SIDE_CB, gram)
    return tuple(site_tuple(hit) for hit in hits)


def is_n13_substring(
    gram: tuple[str, ...],
    n13: tuple[str, ...] = STANDING_N13,
) -> bool:
    """True iff gram is an exact contiguous run inside the 13-gram."""
    return is_contiguous_substring(gram, n13)


def independent_rows(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Rows that are not exact contiguous substrings of the 13-gram."""
    return tuple(
        (tokens, n, freq, sites)
        for tokens, n, freq, is_sub, sites in rows
        if not is_sub
    )


def c_repeating_nge8_all_substrings_of_n13(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥8 is a 13-gram substring."""
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_c_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off C. Counts only."""
    return sum(leaks_from_hits("C", hits, tablets).values())


class TestCNge8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted remainder 9-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = GRAM13
        planted = REMAINDER_9GRAM
        self.assertNotEqual(home, planted)
        self.assertEqual(len(home), 13)
        self.assertEqual(len(planted), 9)
        self.assertTrue(is_n13_substring(home))
        self.assertTrue(is_n13_substring(home[1:9]))
        self.assertFalse(is_n13_substring(planted))
        self.assertFalse(is_n13_substring(home + ("040",)))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge8_grams(once_each, analyzer), ())
        self.assertFalse(c_repeating_nge8_all_substrings_of_n13(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_nge8_grams(twice_home, analyzer)
        self.assertGreaterEqual(len(home_only), 1)
        self.assertIn((home, 13, 2), home_only)
        home_rows = tuple(
            (gram, n, freq, is_n13_substring(gram), ())
            for gram, n, freq in home_only
        )
        self.assertTrue(c_repeating_nge8_all_substrings_of_n13(home_rows))
        self.assertEqual(independent_rows(home_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge8_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_n13_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(c_repeating_nge8_all_substrings_of_n13(both_rows))
        self.assertIn(planted, tuple(gram for gram, n, _freq in both if n == 9))
        gapped = [list(home[:6]) + ["999"] + list(home[6:]), list(home)]
        self.assertEqual(repeating_nge8_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "c_repeating_nge8_all_substrings_of_n13")
        self.assertFalse(STANDING_C_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N13)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 11)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        self.assertFalse(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariCNge8Scoreboard(unittest.TestCase):
    """Cited-fixture C repeating n≥8 vs the calendar 13-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.c_sides = load_c_sides()
        measured = repeating_nge8_grams(self.by_tablet["C"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_n13_substring(gram),
                nge8_sites(gram, self.c_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = c_repeating_nge8_all_substrings_of_n13(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_c = tuple(
            off_c_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_119_and_29_not_invented(self):
        """Calendar 13-gram and remainder 9-gram are prior locks."""
        self.assertEqual(GRAM13, INVENTORY_LONGEST_TOKENS["C"])
        self.assertEqual(INVENTORY_LONGEST_N["C"], 13)
        self.assertEqual(len(GRAM13), 13)
        self.assertEqual(
            GRAM13,
            (
                "040",
                "040",
                "040",
                "040",
                "040",
                "390",
                "041",
                "378",
                "041",
                "670",
                "008",
                "078",
                "711",
            ),
        )
        self.assertEqual(REMAINDER_9GRAM, MOTIF_9GRAM)
        self.assertEqual(
            REMAINDER_9GRAM,
            ("002", "010", "070", "760", "040", "006", "430", "047", "002"),
        )
        self.assertEqual(REMAINDER_8PREFIX, REMAINDER_9GRAM[:8])
        self.assertEqual(REMAINDER_8SUFFIX, REMAINDER_9GRAM[1:])
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["longest_tokens"]),
            GRAM13,
        )
        self.assertEqual(tuple(self.survey["c_repeating_13grams"]["home_tokens13"]), GRAM13)
        self.assertEqual(self.survey["c_repeating_13grams"]["cycle"], 119)
        self.assertEqual(self.survey["tablet_c_mamari_ca_c_only"]["cycle"], 118)
        self.assertEqual(self.survey["repeating_ngram_profile"]["cycle"], 29)
        self.assertEqual(
            tuple(self.survey["repeating_ngram_profile"]["longest_tokens"]),
            REMAINDER_9GRAM,
        )
        self.assertNotEqual(GRAM13, REMAINDER_9GRAM)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_loses(self):
        """32 repeating n≥8; 21 substrings; 11 independent. Claim is false."""
        self.assertEqual(len(self.rows), STANDING_REPEATING_COUNT)
        self.assertEqual(self.substring_count, STANDING_SUBSTRING_COUNT)
        self.assertEqual(len(self.independent), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_REPEATING_COUNT, 32)
        self.assertEqual(STANDING_SUBSTRING_COUNT, 21)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 11)
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
        self.assertFalse(c_repeating_nge8_all_substrings_of_n13(self.rows))
        self.assertEqual(self.claim_holds, STANDING_C_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N13)
        self.assertFalse(STANDING_C_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N13)
        self.assertEqual(STANDING_CLAIM, "c_repeating_nge8_all_substrings_of_n13")
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
            self.assertEqual(is_n13_substring(gram), is_sub)
            self.assertEqual(nge8_sites(gram, self.c_sides), sites)
            self.assertEqual(len(sites), freq)
        self.assertIn(GRAM13, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 13))
        self.assertTrue(STANDING_N13_IN_SET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_delimiter_tail_and_remainder(self):
        """Independent grams are Guy+040 tails and the remainder 9-gram family."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertIn(REMAINDER_9GRAM, indep_tokens)
        self.assertIn(REMAINDER_8PREFIX, indep_tokens)
        self.assertIn(REMAINDER_8SUFFIX, indep_tokens)
        self.assertTrue(STANDING_REMAINDER_IN_INDEPENDENT)
        self.assertNotIn(GRAM13, indep_tokens)
        self.assertFalse(is_n13_substring(REMAINDER_9GRAM))
        self.assertFalse(is_n13_substring(REMAINDER_8PREFIX))
        self.assertFalse(is_n13_substring(REMAINDER_8SUFFIX))
        remainder_family = {REMAINDER_9GRAM, REMAINDER_8PREFIX, REMAINDER_8SUFFIX}
        delimiter_tails = tuple(
            gram for gram in indep_tokens if gram not in remainder_family
        )
        self.assertEqual(len(remainder_family), 3)
        self.assertEqual(len(delimiter_tails), 8)
        for gram in delimiter_tails:
            self.assertIn("711", gram)
            self.assertEqual(gram[-1], "040")
            self.assertFalse(is_n13_substring(gram))
            without_trailing_040 = tuple(
                token for index, token in enumerate(gram) if not (index >= gram.index("711") and token == "040")
            )
            self.assertTrue(is_n13_substring(without_trailing_040))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_c_hits(self):
        """Independent C sites; Cb=0; off-C 0 on every vendored tablet."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_c, STANDING_INDEPENDENT_OFF_C)
        self.assertEqual(STANDING_INDEPENDENT_OFF_C, (0,) * 11)
        for (gram, n, freq, sites), hits, off_hits in zip(
            self.independent,
            self.indep_hits_by_tablet,
            self.indep_off_c,
            strict=True,
        ):
            self.assertEqual(nge8_sites(gram, self.c_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("C")], freq)
            self.assertEqual(ngram_hit_count(self.c_sides[SIDE_CA], gram), freq)
            self.assertEqual(ngram_hit_count(self.c_sides[SIDE_CB], gram), 0)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "C":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("C", hits), {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = CA_LINE_NAMES if side == SIDE_CA else CB_LINE_NAMES
                stems = self.c_sides[side][names.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_CA)
                self.assertIn(line, ("Ca7", "Ca8", "Ca10", "Ca11"))
        remainder_sites = tuple(
            sites
            for gram, _n, _freq, sites in self.independent
            if gram in {REMAINDER_9GRAM, REMAINDER_8PREFIX, REMAINDER_8SUFFIX}
        )
        for sites in remainder_sites:
            self.assertTrue(all(line in ("Ca10", "Ca11") for _side, line, _i in sites))
        self.assertEqual(thirteengram_sites(GRAM13, self.c_sides), CYCLE_118_CA_SITES)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(tuple(STANDING_INDEPENDENT_CB_HITS), (0,) * 11)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_119_118_115_and_w_scoreboards_still_compute(self):
        """Cycle 119 C 13-grams, 118 C-only, 115 B eightgrams, and W stay."""
        prior_119 = TestMamariCThirteengramScoreboard()
        prior_119.setUp()
        prior_119.test_n_is_1_and_hypothesis_n_1_holds()
        prior_119.test_survey_matches_computed_lock()
        prior_118 = TestMamariCaCOnlyScoreboard()
        prior_118.setUp()
        prior_118.test_13gram_is_zero_off_c_and_c_only()
        prior_118.test_survey_matches_computed_lock()
        prior_115 = TestMamariBEightgramScoreboard()
        prior_115.setUp()
        prior_115.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-120 n≥8 substring lock."""
        lock = self.survey["c_repeating_nge8"]
        self.assertEqual(lock["cycle"], 120)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(tuple(lock["home_tokens13"]), GRAM13)
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
                "off_c_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_c_hits"]), STANDING_INDEPENDENT_OFF_C)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n13_in_set"])
        self.assertTrue(lock["remainder_in_independent"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["c_repeating_nge8_all_substrings_of_n13"])
        self.assertEqual(
            lock["c_repeating_nge8_all_substrings_of_n13"],
            STANDING_C_REPEATING_NGE8_ALL_SUBSTRINGS_OF_N13,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_c_repeating_13grams_unchanged"])
        self.assertTrue(lock["standing_c_mamari_ca_c_only_unchanged"])
        self.assertTrue(lock["standing_b_repeating_8grams_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["c_repeating_13grams"]["cycle"], 119)
        self.assertTrue(self.survey["c_repeating_13grams"]["c_has_exactly_1_repeating_13gram"])
        self.assertEqual(self.survey["tablet_c_mamari_ca_c_only"]["cycle"], 118)
        self.assertTrue(self.survey["tablet_c_mamari_ca_c_only"]["c_maxn_is_c_only"])
        self.assertEqual(self.survey["b_repeating_8grams"]["cycle"], 115)
        self.assertFalse(self.survey["b_repeating_8grams"]["b_has_exactly_2_repeating_8grams"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["longest_count"], 1)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCNge8ImageSnapshot(unittest.TestCase):
    """Cycle 120 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
