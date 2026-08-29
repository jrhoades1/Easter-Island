"""I's repeating n≥4 grams vs the locked I 5-gram.

Cycle 135 text-search lock. Uses already-vendored A–V and the
cycle-46/99/103 I 5-gram. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented Barthel.
No G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Enumerates every distinct contiguous n≥4 gram with freq≥2 on I
(same per-line Barthel parser as the leak table / N n≥5
scoreboards). For each, whether it is an exact contiguous
substring of 999 071 076 010 079 (the 5-gram is a
substring of itself). Hypothesis: no independent repeating n≥4
(every such gram is a 5-gram substring). Measured: 42 repeating
n≥4; 3 are substrings; 39 independent. The two 4-grams are the
5-gram's prefix (freq 3 at Ia4[6]/[25]/Ia5[108]) and suffix
(freq 5 at those three interiors plus Ia12[33]/Ia14[82]). The
independent remainder is the four other cycle-103 tied n=5
grams plus 35 4-grams; all are I-only (off-I 0). Cycle 46
already locked longest n=5 and no n≥8. Claim that can lose:
i_repeating_nge4_all_substrings_of_i_5gram. The claim is
false (the 5-gram is not the only repeating n≥4). Do not
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
from tests.test_mamari_n_nge5_scoreboard import (
    TestMamariNNge5Scoreboard,
)
from tests.test_mamari_s_nge6_scoreboard import (
    TestMamariSNge6Scoreboard,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    STANDING_TIED_TOKENS5,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    STANDING_LONGEST_N as I_VENDOR_LONGEST_N,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    STANDING_LONGEST_NGRAM as I_N5_GRAM,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

PROFILE_MIN_N = 4
HYPOTHESIS_INDEPENDENT_EMPTY = True
STANDING_N5 = GRAM5
STANDING_N4_PREFIX = STANDING_N5[:4]
STANDING_N4_SUFFIX = STANDING_N5[1:]
STANDING_TIED_INDEP_N5 = STANDING_TIED_TOKENS5[1:]
INDEPENDENT_PLANT = H_INDEPENDENT_PLANT[:4]
STANDING_REPEATING_COUNT = 42
STANDING_SUBSTRING_COUNT = 3
STANDING_INDEPENDENT_COUNT = 39
STANDING_COUNTS_BY_N = {4: 37, 5: 5}
STANDING_SUBSTRING_BY_N = {4: 2, 5: 1}
STANDING_INDEPENDENT_BY_N = {4: 35, 5: 4}
STANDING_LONGEST_N = 5
# (tokens, n, freq, is_5gram_substring, sites)
STANDING_ROWS = (
    (('999', '090', '076', '070'), 4, 5, False, (('Ia', 'Ia2', 9), ('Ia', 'Ia4', 111), ('Ia', 'Ia7', 67), ('Ia', 'Ia7', 128), ('Ia', 'Ia14', 139))),
    (('071', '076', '010', '079'), 4, 5, True, (('Ia', 'Ia4', 7), ('Ia', 'Ia4', 26), ('Ia', 'Ia5', 109), ('Ia', 'Ia12', 33), ('Ia', 'Ia14', 82))),
    (('090', '076', '020', '010'), 4, 4, False, (('Ia', 'Ia2', 119), ('Ia', 'Ia4', 86), ('Ia', 'Ia5', 143), ('Ia', 'Ia12', 83))),
    (('430', '076', '006', '000'), 4, 3, False, (('Ia', 'Ia1', 129), ('Ia', 'Ia4', 139), ('Ia', 'Ia14', 162))),
    (('028', '076', '011', '076'), 4, 3, False, (('Ia', 'Ia1', 136), ('Ia', 'Ia4', 125), ('Ia', 'Ia14', 78))),
    (('999', '071', '076', '010'), 4, 3, True, (('Ia', 'Ia4', 6), ('Ia', 'Ia4', 25), ('Ia', 'Ia5', 108))),
    (('021', '090', '076', '087'), 4, 3, False, (('Ia', 'Ia4', 116), ('Ia', 'Ia5', 27), ('Ia', 'Ia6', 77))),
    (('999', '090', '076', '071'), 4, 3, False, (('Ia', 'Ia4', 153), ('Ia', 'Ia5', 1), ('Ia', 'Ia5', 22))),
    (('071', '999', '604', '076'), 4, 2, False, (('Ia', 'Ia1', 63), ('Ia', 'Ia9', 3))),
    (('076', '006', '000', '076'), 4, 2, False, (('Ia', 'Ia1', 130), ('Ia', 'Ia14', 163))),
    (('600', '090', '076', '011'), 4, 2, False, (('Ia', 'Ia2', 106), ('Ia', 'Ia14', 53))),
    (('076', '020', '010', '050'), 4, 2, False, (('Ia', 'Ia2', 120), ('Ia', 'Ia14', 110))),
    (('000', '999', '090', '076'), 4, 2, False, (('Ia', 'Ia3', 35), ('Ia', 'Ia5', 0))),
    (('999', '090', '076', '013'), 4, 2, False, (('Ia', 'Ia3', 36), ('Ia', 'Ia6', 91))),
    (('999', '205', '076', '071'), 4, 2, False, (('Ia', 'Ia3', 51), ('Ia', 'Ia3', 79))),
    (('999', '090', '076', '005'), 4, 2, False, (('Ia', 'Ia3', 70), ('Ia', 'Ia13', 108))),
    (('076', '010', '079', '090'), 4, 2, False, (('Ia', 'Ia5', 110), ('Ia', 'Ia5', 139))),
    (('072', '076', '010', '079'), 4, 2, False, (('Ia', 'Ia5', 138), ('Ia', 'Ia13', 71))),
    (('076', '071', '009', '090'), 4, 2, False, (('Ia', 'Ia5', 161), ('Ia', 'Ia12', 71))),
    (('076', '010', '079', '006'), 4, 2, False, (('Ia', 'Ia6', 19), ('Ia', 'Ia13', 72))),
    (('010', '079', '006', '700'), 4, 2, False, (('Ia', 'Ia6', 20), ('Ia', 'Ia13', 73))),
    (('202', '076', '006', '055'), 4, 2, False, (('Ia', 'Ia6', 48), ('Ia', 'Ia12', 119))),
    (('076', '071', '090', '999'), 4, 2, False, (('Ia', 'Ia7', 166), ('Ia', 'Ia14', 136))),
    (('076', '999', '029', '076'), 4, 2, False, (('Ia', 'Ia8', 30), ('Ia', 'Ia10', 144))),
    (('999', '021', '090', '076'), 4, 2, False, (('Ia', 'Ia8', 104), ('Ia', 'Ia13', 15))),
    (('090', '076', '057', '600'), 4, 2, False, (('Ia', 'Ia8', 114), ('Ia', 'Ia9', 28))),
    (('700', '076', '076', '053'), 4, 2, False, (('Ia', 'Ia8', 167), ('Ia', 'Ia9', 32))),
    (('071', '065', '071', '999'), 4, 2, False, (('Ia', 'Ia9', 1), ('Ia', 'Ia9', 56))),
    (('999', '090', '076', '057'), 4, 2, False, (('Ia', 'Ia9', 27), ('Ia', 'Ia9', 128))),
    (('430', '076', '001', '076'), 4, 2, False, (('Ia', 'Ia10', 103), ('Ia', 'Ia13', 156))),
    (('053', '076', '020', '010'), 4, 2, False, (('Ia', 'Ia12', 0), ('Ia', 'Ia14', 109))),
    (('076', '011', '090', '090'), 4, 2, False, (('Ia', 'Ia12', 39), ('Ia', 'Ia14', 102))),
    (('011', '090', '090', '076'), 4, 2, False, (('Ia', 'Ia12', 40), ('Ia', 'Ia14', 103))),
    (('090', '999', '090', '076'), 4, 2, False, (('Ia', 'Ia12', 45), ('Ia', 'Ia14', 138))),
    (('400', '070', '076', '020'), 4, 2, False, (('Ia', 'Ia13', 85), ('Ia', 'Ia14', 126))),
    (('070', '076', '020', '010'), 4, 2, False, (('Ia', 'Ia13', 86), ('Ia', 'Ia14', 127))),
    (('430', '076', '049', '400'), 4, 2, False, (('Ia', 'Ia13', 170), ('Ia', 'Ia14', 63))),
    (('999', '071', '076', '010', '079'), 5, 3, True, (('Ia', 'Ia4', 6), ('Ia', 'Ia4', 25), ('Ia', 'Ia5', 108))),
    (('430', '076', '006', '000', '076'), 5, 2, False, (('Ia', 'Ia1', 129), ('Ia', 'Ia14', 162))),
    (('076', '010', '079', '006', '700'), 5, 2, False, (('Ia', 'Ia6', 19), ('Ia', 'Ia13', 72))),
    (('076', '011', '090', '090', '076'), 5, 2, False, (('Ia', 'Ia12', 39), ('Ia', 'Ia14', 102))),
    (('400', '070', '076', '020', '010'), 5, 2, False, (('Ia', 'Ia13', 85), ('Ia', 'Ia14', 126))),
)
STANDING_INDEPENDENT = tuple(
    (tokens, n, freq, sites)
    for tokens, n, freq, is_sub, sites in STANDING_ROWS
    if not is_sub
)
STANDING_INDEPENDENT_OFF_I = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_INDEPENDENT_IA_HITS = tuple(freq for _tokens, _n, freq, _sites in STANDING_INDEPENDENT)
STANDING_INDEPENDENT_IB_HITS = (0,) * STANDING_INDEPENDENT_COUNT
STANDING_N5_SITES = ((SIDE_IA, "Ia4", 6), (SIDE_IA, "Ia4", 25), (SIDE_IA, "Ia5", 108))
STANDING_N4_PREFIX_SITES = STANDING_N5_SITES
STANDING_N4_SUFFIX_SITES = (
    (SIDE_IA, "Ia4", 7),
    (SIDE_IA, "Ia4", 26),
    (SIDE_IA, "Ia5", 109),
    (SIDE_IA, "Ia12", 33),
    (SIDE_IA, "Ia14", 82),
)
STANDING_KNOWN_DISTINCT = True
STANDING_N5_IN_SET = True
STANDING_N4_PREFIX_IN_SET = True
STANDING_N4_SUFFIX_IN_SET = True
STANDING_TIED_INDEP_IN_SET = True
STANDING_N5_IS_SUBSTRING_OF_SELF = True
STANDING_N4_PREFIX_IS_SUBSTRING = True
STANDING_N4_SUFFIX_IS_SUBSTRING = True
STANDING_CLAIM = "i_repeating_nge4_all_substrings_of_i_5gram"
STANDING_I_REPEATING_NGE4_ALL_SUBSTRINGS_OF_I_5GRAM = False
STANDING_RESULT = "i_repeating_nge4"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def repeating_nge4_grams(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
) -> tuple[tuple[tuple[str, ...], int, int], ...]:
    """Distinct contiguous n≥4 grams with freq≥2. Search only."""
    rows: list[tuple[tuple[str, ...], int, int]] = []
    n = PROFILE_MIN_N
    while True:
        found = analyzer.extract_ngrams(lines, n=n, min_frequency=2)
        if not found:
            break
        rows.extend((gram, n, freq) for gram, freq in found)
        n += 1
    return tuple(rows)


def nge4_sites(
    gram: tuple[str, ...],
    i_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Ia. Ib is unpublished. Search only."""
    hits = named_side_hits(i_sides[SIDE_IA], IA_LINE_NAMES, SIDE_IA, gram)
    return tuple(site_tuple(hit) for hit in hits)


def is_i_5gram_substring(
    gram: tuple[str, ...],
    n5: tuple[str, ...] = STANDING_N5,
) -> bool:
    """True iff gram is an exact contiguous run inside the I 5-gram."""
    return is_contiguous_substring(gram, n5)


def i_repeating_nge4_all_substrings_of_i_5gram(
    rows: tuple[tuple[tuple[str, ...], int, int, bool, tuple], ...],
) -> bool:
    """True iff every repeating n≥4 is a 5-gram substring.

    The 5-gram is a substring of itself. An empty inventory is
    false here (the home 5-gram must be in the repeating set).
    """
    return bool(rows) and all(is_sub for _tokens, _n, _freq, is_sub, _sites in rows)


def off_i_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off I. Counts only."""
    return sum(leaks_from_hits("I", hits, tablets).values())


class TestINge4Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_all_substrings_can_fail(self):
        """Freq 1 is excluded; a planted non-5-gram 4-gram fails the claim."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = STANDING_N5
        prefix = STANDING_N4_PREFIX
        suffix = STANDING_N4_SUFFIX
        planted = INDEPENDENT_PLANT
        measured_indep = STANDING_TIED_INDEP_N5[0]
        self.assertNotEqual(home, planted)
        self.assertNotEqual(prefix, planted)
        self.assertNotEqual(suffix, planted)
        self.assertNotEqual(home, measured_indep)
        self.assertNotEqual(planted, measured_indep)
        self.assertEqual(len(home), 5)
        self.assertEqual(len(prefix), 4)
        self.assertEqual(len(suffix), 4)
        self.assertEqual(len(planted), 4)
        self.assertEqual(len(measured_indep), 5)
        self.assertTrue(is_i_5gram_substring(home))
        self.assertTrue(is_i_5gram_substring(home[:5]))
        self.assertTrue(is_contiguous_substring(home, home))
        self.assertTrue(is_i_5gram_substring(prefix))
        self.assertTrue(is_i_5gram_substring(suffix))
        self.assertTrue(is_i_5gram_substring(home[1:]))
        self.assertFalse(is_i_5gram_substring(planted))
        self.assertFalse(is_i_5gram_substring(measured_indep))
        self.assertFalse(is_i_5gram_substring(home + ("999",)))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_nge4_grams(once_each, analyzer), ())
        self.assertFalse(i_repeating_nge4_all_substrings_of_i_5gram(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_nge4_grams(twice_home, analyzer)
        self.assertGreaterEqual(len(home_only), 1)
        self.assertIn((home, 5, 2), home_only)
        self.assertIn((prefix, 4, 2), home_only)
        self.assertIn((suffix, 4, 2), home_only)
        home_rows = tuple(
            (gram, n, freq, is_i_5gram_substring(gram), ())
            for gram, n, freq in home_only
        )
        self.assertTrue(i_repeating_nge4_all_substrings_of_i_5gram(home_rows))
        self.assertEqual(independent_rows(home_rows), ())
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_nge4_grams(twice_each, analyzer)
        both_rows = tuple(
            (gram, n, freq, is_i_5gram_substring(gram), ())
            for gram, n, freq in both
        )
        self.assertFalse(i_repeating_nge4_all_substrings_of_i_5gram(both_rows))
        self.assertIn(planted, tuple(gram for gram, n, _freq in both if n == 4))
        twice_measured = [
            list(home),
            list(home),
            list(measured_indep),
            list(measured_indep),
        ]
        measured_both = repeating_nge4_grams(twice_measured, analyzer)
        measured_rows = tuple(
            (gram, n, freq, is_i_5gram_substring(gram), ())
            for gram, n, freq in measured_both
        )
        self.assertFalse(i_repeating_nge4_all_substrings_of_i_5gram(measured_rows))
        self.assertIn(measured_indep, tuple(gram for gram, n, _freq in measured_both if n == 5))
        gapped = [list(home[:2]) + ["600"] + list(home[2:]), list(home)]
        self.assertEqual(repeating_nge4_grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "i_repeating_nge4_all_substrings_of_i_5gram")
        self.assertFalse(STANDING_I_REPEATING_NGE4_ALL_SUBSTRINGS_OF_I_5GRAM)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 39)
        self.assertFalse(HYPOTHESIS_INDEPENDENT_EMPTY and STANDING_INDEPENDENT_COUNT == 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariINge4Scoreboard(unittest.TestCase):
    """Cited-fixture I repeating n≥4 vs the I 5-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.i_sides = load_i_sides()
        measured = repeating_nge4_grams(self.by_tablet["I"], self.analyzer)
        self.rows = tuple(
            (
                gram,
                n,
                freq,
                is_i_5gram_substring(gram),
                nge4_sites(gram, self.i_sides),
            )
            for gram, n, freq in measured
        )
        self.independent = independent_rows(self.rows)
        self.substring_count = sum(1 for _g, _n, _f, is_sub, _s in self.rows if is_sub)
        self.claim_holds = i_repeating_nge4_all_substrings_of_i_5gram(self.rows)
        self.indep_hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram, _n, _freq, _sites in self.independent
        )
        self.indep_off_i = tuple(
            off_i_hit_total(hits) for hits in self.indep_hits_by_tablet
        )

    def test_tokens_are_cycle_46_99_103_n5_not_invented(self):
        """I 5-gram is a prior lock; both 4-grams are its measured slices."""
        self.assertEqual(STANDING_N5, INVENTORY_LONGEST_TOKENS["I"])
        self.assertEqual(STANDING_N5, I_N5_GRAM)
        self.assertEqual(STANDING_N5, GRAM5)
        self.assertEqual(INVENTORY_LONGEST_N["I"], 5)
        self.assertEqual(I_VENDOR_LONGEST_N, 5)
        self.assertEqual(len(STANDING_N5), 5)
        self.assertEqual(len(STANDING_N4_PREFIX), 4)
        self.assertEqual(len(STANDING_N4_SUFFIX), 4)
        self.assertEqual(
            STANDING_N5,
            ("999", "071", "076", "010", "079"),
        )
        self.assertEqual(
            STANDING_N4_PREFIX,
            ("999", "071", "076", "010"),
        )
        self.assertEqual(
            STANDING_N4_SUFFIX,
            ("071", "076", "010", "079"),
        )
        self.assertEqual(STANDING_N4_PREFIX, STANDING_N5[:4])
        self.assertEqual(STANDING_N4_SUFFIX, STANDING_N5[1:])
        self.assertEqual(
            STANDING_TIED_INDEP_N5,
            (
                ("430", "076", "006", "000", "076"),
                ("076", "010", "079", "006", "700"),
                ("076", "011", "090", "090", "076"),
                ("400", "070", "076", "020", "010"),
            ),
        )
        self.assertTrue(is_i_5gram_substring(STANDING_N5))
        self.assertTrue(is_contiguous_substring(STANDING_N5, STANDING_N5))
        self.assertTrue(STANDING_N5_IS_SUBSTRING_OF_SELF)
        self.assertTrue(is_i_5gram_substring(STANDING_N4_PREFIX))
        self.assertTrue(is_i_5gram_substring(STANDING_N4_SUFFIX))
        self.assertTrue(STANDING_N4_PREFIX_IS_SUBSTRING)
        self.assertTrue(STANDING_N4_SUFFIX_IS_SUBSTRING)
        for tied in STANDING_TIED_INDEP_N5:
            self.assertFalse(is_i_5gram_substring(tied))
            self.assertNotEqual(tied, STANDING_N5)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_tokens"]),
            STANDING_N5,
        )
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_staff"]["longest_tokens"]),
            STANDING_N5,
        )
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            STANDING_N5,
        )
        self.assertEqual(
            tuple(tuple(row) for row in self.survey["tablet_i_santiago_ia_i_only"]["tied_tokens5"]),
            STANDING_TIED_TOKENS5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertEqual(self.survey["p_repeating_nge6"]["cycle"], 132)
        self.assertNotEqual(STANDING_N5, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_N4_PREFIX, INDEPENDENT_PLANT)
        self.assertNotEqual(STANDING_N4_SUFFIX, INDEPENDENT_PLANT)
        self.assertFalse(is_i_5gram_substring(INDEPENDENT_PLANT))
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_and_hypothesis_all_substrings_loses(self):
        """42 repeating n≥4; 3 substrings; 39 independent. Claim is false."""
        self.assertEqual(len(self.rows), STANDING_REPEATING_COUNT)
        self.assertEqual(self.substring_count, STANDING_SUBSTRING_COUNT)
        self.assertEqual(len(self.independent), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_REPEATING_COUNT, 42)
        self.assertEqual(STANDING_SUBSTRING_COUNT, 3)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 39)
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
        self.assertEqual(STANDING_LONGEST_N, 5)
        self.assertFalse(i_repeating_nge4_all_substrings_of_i_5gram(self.rows))
        self.assertEqual(self.claim_holds, STANDING_I_REPEATING_NGE4_ALL_SUBSTRINGS_OF_I_5GRAM)
        self.assertFalse(STANDING_I_REPEATING_NGE4_ALL_SUBSTRINGS_OF_I_5GRAM)
        self.assertEqual(STANDING_CLAIM, "i_repeating_nge4_all_substrings_of_i_5gram")
        self.assertTrue(HYPOTHESIS_INDEPENDENT_EMPTY)
        self.assertNotEqual(STANDING_INDEPENDENT_COUNT, 0)
        n6 = self.analyzer.extract_ngrams(self.by_tablet["I"], n=6, min_frequency=2)
        self.assertEqual(n6, [])
        n7 = self.analyzer.extract_ngrams(self.by_tablet["I"], n=7, min_frequency=2)
        self.assertEqual(n7, [])
        n8 = self.analyzer.extract_ngrams(self.by_tablet["I"], n=8, min_frequency=2)
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
            self.assertEqual(is_i_5gram_substring(gram), is_sub)
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(len(sites), freq)
        self.assertIn(STANDING_N5, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 5))
        self.assertIn(
            STANDING_N4_PREFIX,
            tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 4),
        )
        self.assertIn(
            STANDING_N4_SUFFIX,
            tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 4),
        )
        for tied in STANDING_TIED_INDEP_N5:
            self.assertIn(tied, tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 5))
        self.assertTrue(STANDING_N5_IN_SET)
        self.assertTrue(STANDING_N4_PREFIX_IN_SET)
        self.assertTrue(STANDING_N4_SUFFIX_IN_SET)
        self.assertTrue(STANDING_TIED_INDEP_IN_SET)
        fourgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 4)
        self.assertEqual(len(fourgrams), 37)
        self.assertIn(STANDING_N4_PREFIX, fourgrams)
        self.assertIn(STANDING_N4_SUFFIX, fourgrams)
        fivegrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 5)
        self.assertEqual(fivegrams, (STANDING_N5,) + STANDING_TIED_INDEP_N5)
        sixgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 6)
        self.assertEqual(sixgrams, ())
        eightgrams = tuple(gram for gram, n, _f, _s, _sites in self.rows if n == 8)
        self.assertEqual(eightgrams, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_set_is_the_measured_remainder(self):
        """Independent remainder is 39 I-local grams off the I 5-gram."""
        indep_tokens = tuple(gram for gram, _n, _freq, _sites in self.independent)
        self.assertEqual(len(indep_tokens), 39)
        self.assertNotIn(STANDING_N5, indep_tokens)
        self.assertNotIn(STANDING_N4_PREFIX, indep_tokens)
        self.assertNotIn(STANDING_N4_SUFFIX, indep_tokens)
        self.assertTrue(is_i_5gram_substring(STANDING_N5))
        self.assertTrue(is_i_5gram_substring(STANDING_N4_PREFIX))
        self.assertTrue(is_i_5gram_substring(STANDING_N4_SUFFIX))
        self.assertFalse(is_i_5gram_substring(INDEPENDENT_PLANT))
        self.assertNotIn(INDEPENDENT_PLANT, indep_tokens)
        for tied in STANDING_TIED_INDEP_N5:
            self.assertIn(tied, indep_tokens)
            self.assertFalse(is_i_5gram_substring(tied))
        self.assertEqual(
            tuple(gram for gram, n, _freq, _sites in self.independent if n == 5),
            STANDING_TIED_INDEP_N5,
        )
        self.assertEqual(
            sum(1 for _gram, n, _freq, _sites in self.independent if n == 4),
            35,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_independent_sites_and_off_i_hits(self):
        """Independent Ia sites match freq; Ib unpublished 0; off-I 0."""
        self.assertEqual(self.independent, STANDING_INDEPENDENT)
        self.assertEqual(self.indep_off_i, STANDING_INDEPENDENT_OFF_I)
        self.assertEqual(STANDING_INDEPENDENT_OFF_I, (0,) * 39)
        self.assertEqual(self.indep_off_i, (0,) * STANDING_INDEPENDENT_COUNT)
        for (gram, n, freq, sites), hits, off_hits in zip(
            self.independent,
            self.indep_hits_by_tablet,
            self.indep_off_i,
            strict=True,
        ):
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("I")], freq)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), freq)
            self.assertEqual(ngram_hit_count(self.by_tablet["I"], gram), freq)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "I":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("I", hits), {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
        self.assertEqual(tuple(STANDING_INDEPENDENT_IA_HITS), tuple(
            freq for _tokens, _n, freq, _sites in STANDING_INDEPENDENT
        ))
        self.assertEqual(tuple(STANDING_INDEPENDENT_IB_HITS), (0,) * 39)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        for gram, n, freq, is_sub, sites in self.rows:
            if is_sub:
                self.assertTrue(is_i_5gram_substring(gram))
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), freq)
            self.assertEqual(ngram_hit_count(self.by_tablet["I"], gram), freq)
            hits = tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            self.assertEqual(hits[VENDORED_TABLETS.index("I")], freq)
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                if letter != "I":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks_from_hits("I", hits), {})
            self.assertEqual(off_i_hit_total(hits), 0)
        self.assertEqual(nge4_sites(STANDING_N5, self.i_sides), STANDING_N5_SITES)
        self.assertEqual(nge4_sites(STANDING_N4_PREFIX, self.i_sides), STANDING_N4_PREFIX_SITES)
        self.assertEqual(nge4_sites(STANDING_N4_SUFFIX, self.i_sides), STANDING_N4_SUFFIX_SITES)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_134_133_103_46_and_w_scoreboards_still_compute(self):
        """Cycle 134 N n≥5, 133 S n≥6, 103 I-only, and W stay."""
        prior_134 = TestMamariNNge5Scoreboard()
        prior_134.setUp()
        prior_134.test_counts_and_hypothesis_all_substrings_holds()
        prior_134.test_survey_matches_computed_lock()
        prior_133 = TestMamariSNge6Scoreboard()
        prior_133.setUp()
        prior_133.test_counts_and_hypothesis_all_substrings_holds()
        prior_133.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-135 n≥4 5-gram-substring lock."""
        lock = self.survey["i_repeating_nge4"]
        self.assertEqual(lock["cycle"], 135)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["repeating_count"], STANDING_REPEATING_COUNT)
        self.assertEqual(lock["substring_count"], STANDING_SUBSTRING_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertEqual(lock["counts_by_n"], {str(k): v for k, v in STANDING_COUNTS_BY_N.items()})
        self.assertEqual(tuple(lock["home_tokens5"]), STANDING_N5)
        self.assertEqual(tuple(lock["home_tokens4_prefix"]), STANDING_N4_PREFIX)
        self.assertEqual(tuple(lock["home_tokens4_suffix"]), STANDING_N4_SUFFIX)
        self.assertEqual(
            tuple(tuple(row) for row in lock["tied_independent_tokens5"]),
            STANDING_TIED_INDEP_N5,
        )
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
                "off_i_hits": 0,
            }
            for tokens, n, freq, sites in STANDING_INDEPENDENT
        ]
        self.assertEqual(lock["independent"], indep_lock)
        self.assertEqual(tuple(lock["independent_off_i_hits"]), STANDING_INDEPENDENT_OFF_I)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["n5_in_set"])
        self.assertTrue(lock["n4_prefix_in_set"])
        self.assertTrue(lock["n4_suffix_in_set"])
        self.assertTrue(lock["tied_indep_in_set"])
        self.assertTrue(lock["n5_is_substring_of_self"])
        self.assertTrue(lock["n4_prefix_is_substring"])
        self.assertTrue(lock["n4_suffix_is_substring"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_repeating_nge4_all_substrings_of_i_5gram"])
        self.assertEqual(
            lock["i_repeating_nge4_all_substrings_of_i_5gram"],
            STANDING_I_REPEATING_NGE4_ALL_SUBSTRINGS_OF_I_5GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_p_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_q_repeating_nge7_unchanged"])
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
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertEqual(self.survey["n_repeating_nge5"]["repeating_count"], 3)
        self.assertTrue(self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"])
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertEqual(self.survey["s_repeating_nge6"]["repeating_count"], 3)
        self.assertTrue(self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(self.survey["p_repeating_nge6"]["cycle"], 132)
        self.assertEqual(self.survey["p_repeating_nge6"]["repeating_count"], 2)
        self.assertFalse(self.survey["p_repeating_nge6"]["p_repeating_nge6_all_substrings_of_p_6gram"])
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            STANDING_N5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["q_repeating_nge7"]["cycle"], 131)
        self.assertEqual(self.survey["q_repeating_nge7"]["repeating_count"], 2)
        self.assertFalse(self.survey["q_repeating_nge7"]["q_repeating_nge7_all_substrings_of_hq_7gram"])
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
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"], 5)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariINge4ImageSnapshot(unittest.TestCase):
    """Cycle 135 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
