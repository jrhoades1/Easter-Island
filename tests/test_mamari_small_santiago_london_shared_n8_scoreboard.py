"""G–K exact shared stem n≥8 inventory and coverage.

Cycle 67 text-search lock. Uses already-vendored Gr.html, Gv.html,
Kr.html, Kv.html and the existing parsers. Does not scrape a new
tablet. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. Not a meaning dictionary.

Cycle 61 locked the longest shared n (Gr–Kr 17, Gr–Kv 15, Gv–K 2).
Cycle 66 locked the 15-gram sites. This cycle inventories every
exact shared n≥8: each distinct sequence, n, frequency on each
side, and line/index of hits. Combined G is Gr+Gv; combined K is
Kr+Kv. Also the four per-side pairs. Coverage is how many stems
on Gr/Gv/Kr/Kv sit inside at least one shared n≥8 (same-text vs
formula islands).

The 139 n≥8 rows are exactly the n≥8 subspans of six maximal
islands. All freq 1/1. Islands are position-disjoint. Gv is 0.
Not same-text. Not two formulas.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_second_passage_scoreboard import (
    find_ngram_hits,
    load_corpus_survey,
)
from tests.test_mamari_small_london_kr_scoreboard import (
    KR_LINE_NAMES,
    STANDING_STEM_TOTAL as KR_STEM_TOTAL,
)
from tests.test_mamari_small_london_kv_scoreboard import (
    KV_LINE_NAMES,
    STANDING_STEM_TOTAL as KV_STEM_TOTAL,
)
from tests.test_mamari_small_santiago_gr_scoreboard import (
    GR_LINE_NAMES,
    STANDING_STEM_TOTAL as GR_STEM_TOTAL,
)
from tests.test_mamari_small_santiago_gv_scoreboard import (
    GV_LINE_NAMES,
    STANDING_STEM_TOTAL as GV_STEM_TOTAL,
)
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import GRAM_17
from tests.test_mamari_small_santiago_london_gr_kv_15gram_scoreboard import (
    GRAM_15,
    TestMamariSmallSantiagoLondonGrKv15gramScoreboard,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    G_SIDES,
    K_SIDES,
    SIDE_GR,
    SIDE_GV,
    SIDE_KR,
    SIDE_KV,
    SIDE_PAIRS,
    STANDING_STEM_076_IN_LONGEST,
    concat_sides,
    load_g_k_sides,
    ngram_frequencies,
)

MIN_N = 8
LINE_NAMES = {
    SIDE_GR: GR_LINE_NAMES,
    SIDE_GV: GV_LINE_NAMES,
    SIDE_KR: KR_LINE_NAMES,
    SIDE_KV: KV_LINE_NAMES,
}
STEM_TOTALS = {
    SIDE_GR: GR_STEM_TOTAL,
    SIDE_GV: GV_STEM_TOTAL,
    SIDE_KR: KR_STEM_TOTAL,
    SIDE_KV: KV_STEM_TOTAL,
}
SIDES = (SIDE_GR, SIDE_GV, SIDE_KR, SIDE_KV)

GRAM_13 = (
    "073",
    "006",
    "206",
    "073",
    "006",
    "200",
    "073",
    "006",
    "222",
    "073",
    "006",
    "451",
    "073",
)
GRAM_12 = (
    "522",
    "045",
    "061",
    "009",
    "260",
    "001",
    "004",
    "711",
    "260",
    "001",
    "004",
    "711",
)
GRAM_10_KV = (
    "380",
    "001",
    "003",
    "005",
    "066",
    "380",
    "001",
    "003",
    "290",
    "001",
)
GRAM_10_KR = (
    "380",
    "001",
    "003",
    "597",
    "380",
    "001",
    "003",
    "059",
    "720",
    "380",
)

# (tokens, n, freq_g, freq_k, g_site, k_site); site = (side, line, index)
STANDING_MAXIMALS = (
    (GRAM_17, 17, 1, 1, (SIDE_GR, "Gr4", 3), (SIDE_KR, "Kr5", 0)),
    (GRAM_15, 15, 1, 1, (SIDE_GR, "Gr7", 0), (SIDE_KV, "Kv4", 7)),
    (GRAM_13, 13, 1, 1, (SIDE_GR, "Gr2", 4), (SIDE_KR, "Kr2", 16)),
    (GRAM_12, 12, 1, 1, (SIDE_GR, "Gr1", 4), (SIDE_KR, "Kr1", 2)),
    (GRAM_10_KV, 10, 1, 1, (SIDE_GR, "Gr6", 33), (SIDE_KV, "Kv3", 15)),
    (GRAM_10_KR, 10, 1, 1, (SIDE_GR, "Gr3", 28), (SIDE_KR, "Kr4", 12)),
)
STANDING_GR_KR_MAXIMALS = tuple(
    row for row in STANDING_MAXIMALS if row[5][0] == SIDE_KR
)
STANDING_GR_KV_MAXIMALS = tuple(
    row for row in STANDING_MAXIMALS if row[5][0] == SIDE_KV
)
STANDING_MAXIMAL_COUNT = 6
STANDING_DISTINCT_COUNT = 139
STANDING_BY_N = (35, 29, 23, 17, 13, 9, 6, 4, 2, 1)
STANDING_PER_SIDE_COUNTS = (
    (SIDE_GR, SIDE_KR, 97),
    (SIDE_GR, SIDE_KV, 42),
    (SIDE_GV, SIDE_KR, 0),
    (SIDE_GV, SIDE_KV, 0),
)
STANDING_COVERAGE = (
    (SIDE_GR, 77, GR_STEM_TOTAL),
    (SIDE_GV, 0, GV_STEM_TOTAL),
    (SIDE_KR, 52, KR_STEM_TOTAL),
    (SIDE_KV, 25, KV_STEM_TOTAL),
)
STANDING_COVERED_G = 77
STANDING_COVERED_K = 77
STANDING_SAME_TEXT = False
STANDING_TWO_FORMULAS = False
STANDING_FORMULA_ISLANDS = 6
STANDING_ISLANDS_DISJOINT = True
STANDING_NEW_TABLET = False
STANDING_RESULT = "gk_shared_n8_inventory"


@dataclass(frozen=True)
class SharedN8Row:
    """One exact shared n≥8. Ids only; no meanings."""

    tokens: tuple[str, ...]
    n: int
    freq_g: int
    freq_k: int
    hits_g: tuple[tuple[str, str, int], ...]
    hits_k: tuple[tuple[str, str, int], ...]


def row_tuple(row: SharedN8Row) -> tuple:
    """Stable lock row: tokens, n, freqs, hits."""
    return (row.tokens, row.n, row.freq_g, row.freq_k, row.hits_g, row.hits_k)


def named_hits(
    by_side: dict[str, list[list[str]]],
    sides: tuple[str, ...],
    gram: tuple[str, ...],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) for every exact hit on those sides."""
    hits: list[tuple[str, str, int]] = []
    for side in sides:
        names = LINE_NAMES[side]
        for line_index, start in find_ngram_hits(by_side[side], gram):
            hits.append((side, names[line_index], start))
    return tuple(hits)


def score_shared_n8(
    by_side: dict[str, list[list[str]]],
    left_sides: tuple[str, ...],
    right_sides: tuple[str, ...],
    min_n: int = MIN_N,
) -> tuple[SharedN8Row, ...]:
    """All exact shared stem n-grams with n≥min_n. Per-line windows."""
    left = concat_sides(by_side, left_sides)
    right = concat_sides(by_side, right_sides)
    max_n = min(
        max((len(sequence) for sequence in left), default=0),
        max((len(sequence) for sequence in right), default=0),
    )
    rows: list[SharedN8Row] = []
    for n in range(max_n, min_n - 1, -1):
        left_counts = ngram_frequencies(left, n)
        right_counts = ngram_frequencies(right, n)
        for tokens in sorted(set(left_counts) & set(right_counts)):
            rows.append(
                SharedN8Row(
                    tokens=tokens,
                    n=n,
                    freq_g=left_counts[tokens],
                    freq_k=right_counts[tokens],
                    hits_g=named_hits(by_side, left_sides, tokens),
                    hits_k=named_hits(by_side, right_sides, tokens),
                )
            )
    rows.sort(key=lambda row: (-row.n, row.tokens))
    return tuple(rows)


def expand_maximals(
    maximals: tuple[tuple, ...],
    min_n: int = MIN_N,
) -> tuple[SharedN8Row, ...]:
    """All n≥min_n subspans of maximal islands, with offset hit sites."""
    rows: list[SharedN8Row] = []
    for tokens, n, freq_g, freq_k, g_site, k_site in maximals:
        g_side, g_line, g_index = g_site
        k_side, k_line, k_index = k_site
        for length in range(n, min_n - 1, -1):
            for offset in range(n - length + 1):
                rows.append(
                    SharedN8Row(
                        tokens=tokens[offset : offset + length],
                        n=length,
                        freq_g=freq_g,
                        freq_k=freq_k,
                        hits_g=((g_side, g_line, g_index + offset),),
                        hits_k=((k_side, k_line, k_index + offset),),
                    )
                )
    rows.sort(key=lambda row: (-row.n, row.tokens))
    return tuple(rows)


def maximal_rows(rows: tuple[SharedN8Row, ...]) -> tuple[SharedN8Row, ...]:
    """Rows that are not a contiguous subspan of a longer shared row."""
    tokens = [row.tokens for row in rows]
    kept: list[SharedN8Row] = []
    for row in rows:
        contained = any(
            other[index : index + row.n] == row.tokens
            for other in tokens
            if len(other) > row.n
            for index in range(len(other) - row.n + 1)
        )
        if not contained:
            kept.append(row)
    return tuple(kept)


def covered_stem_count(
    lines: list[list[str]],
    grams: tuple[tuple[str, ...], ...] | list[tuple[str, ...]],
) -> tuple[int, int]:
    """Stems inside at least one gram, and the line-list total."""
    covered = 0
    total = 0
    for sequence in lines:
        total += len(sequence)
        flags = [False] * len(sequence)
        for gram in grams:
            n = len(gram)
            for start in range(len(sequence) - n + 1):
                if tuple(sequence[start : start + n]) == gram:
                    for index in range(start, start + n):
                        flags[index] = True
        covered += sum(flags)
    return covered, total


def score_coverage(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] | list[tuple[str, ...]],
) -> tuple[tuple[str, int, int], ...]:
    """(side, covered, total) for Gr/Gv/Kr/Kv."""
    return tuple(
        (side, *covered_stem_count(by_side[side], grams)) for side in SIDES
    )


def islands_disjoint(maximals: tuple[tuple, ...]) -> bool:
    """True iff no two maximal hits share a (side, line, index) stem."""
    occupied: set[tuple[str, str, int]] = set()
    for _tokens, n, _freq_g, _freq_k, g_site, k_site in maximals:
        for side, line, start in (g_site, k_site):
            for offset in range(n):
                key = (side, line, start + offset)
                if key in occupied:
                    return False
                occupied.add(key)
    return True


def count_by_n(rows: tuple[SharedN8Row, ...], min_n: int = MIN_N) -> tuple[int, ...]:
    """Counts for n = min_n .. max n in the inventory. Empty if none."""
    if not rows:
        return ()
    max_n = max(row.n for row in rows)
    return tuple(sum(1 for row in rows if row.n == n) for n in range(min_n, max_n + 1))


class TestSmallSantiagoLondonSharedN8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_min_n_excludes_short_and_records_hits(self):
        """n=7 share is dropped; n=8 is kept with line/index."""
        provider = MockProvider()
        by_side = {
            SIDE_GR: [["A", "B", "C", "D", "E", "F", "G", "H", "I"]],
            SIDE_GV: [["X"]],
            SIDE_KR: [["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"]],
            SIDE_KV: [["Y"]],
        }
        rows = score_shared_n8(by_side, G_SIDES, K_SIDES)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0].n, 9)
        self.assertEqual(rows[0].tokens, ("A", "B", "C", "D", "E", "F", "G", "H", "I"))
        self.assertEqual(rows[0].hits_g, ((SIDE_GR, "Gr1", 0),))
        self.assertEqual(rows[0].hits_k, ((SIDE_KR, "Kr1", 1),))
        self.assertEqual(rows[1].tokens, ("A", "B", "C", "D", "E", "F", "G", "H"))
        self.assertEqual(rows[2].tokens, ("B", "C", "D", "E", "F", "G", "H", "I"))
        self.assertEqual(expand_maximals(STANDING_MAXIMALS)[0].n, 17)
        self.assertEqual(len(expand_maximals(STANDING_MAXIMALS)), STANDING_DISTINCT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_coverage_unions_windows_and_ignores_other_side(self):
        """Overlapping 8-grams union; a private 8-gram is not coverage."""
        provider = MockProvider()
        lines = [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        grams = [("1", "2", "3", "4", "5", "6", "7", "8")]
        self.assertEqual(covered_stem_count(lines, grams), (8, 10))
        overlap = grams + [("2", "3", "4", "5", "6", "7", "8", "9")]
        self.assertEqual(covered_stem_count(lines, overlap), (9, 10))
        empty = covered_stem_count([["A", "B"]], [("1", "2", "3", "4", "5", "6", "7", "8")])
        self.assertEqual(empty, (0, 2))
        self.assertTrue(islands_disjoint(STANDING_MAXIMALS))
        self.assertEqual(STANDING_ISLANDS_DISJOINT, True)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonSharedN8Scoreboard(unittest.TestCase):
    """Cited-fixture G vs K n≥8 inventory and coverage lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_g_k_sides()
        self.combined = score_shared_n8(self.by_side, G_SIDES, K_SIDES)
        self.expanded = expand_maximals(STANDING_MAXIMALS)
        self.grams = tuple(row.tokens for row in self.combined)
        self.coverage = score_coverage(self.by_side, self.grams)
        self.per_side = tuple(
            (
                g_side,
                k_side,
                score_shared_n8(self.by_side, (g_side,), (k_side,)),
            )
            for g_side, k_side in SIDE_PAIRS
        )

    def test_inventory_tokens_n_freq_and_hits(self):
        """139 distinct n≥8; each matches a maximal subspan with freq 1/1."""
        self.assertEqual(len(self.combined), STANDING_DISTINCT_COUNT)
        self.assertEqual(len(self.expanded), STANDING_DISTINCT_COUNT)
        self.assertEqual(
            tuple(row_tuple(row) for row in self.combined),
            tuple(row_tuple(row) for row in self.expanded),
        )
        self.assertEqual(count_by_n(self.combined), STANDING_BY_N)
        self.assertEqual(len(maximal_rows(self.combined)), STANDING_MAXIMAL_COUNT)
        locked_maximals = tuple(
            (row.tokens, row.n, row.freq_g, row.freq_k, row.hits_g[0], row.hits_k[0])
            for row in maximal_rows(self.combined)
        )
        self.assertEqual(locked_maximals, STANDING_MAXIMALS)
        for row in self.combined:
            self.assertGreaterEqual(row.n, MIN_N)
            self.assertEqual(len(row.tokens), row.n)
            self.assertEqual((row.freq_g, row.freq_k), (1, 1))
            self.assertEqual(len(row.hits_g), 1)
            self.assertEqual(len(row.hits_k), 1)
            self.assertEqual("076" in row.tokens, STANDING_STEM_076_IN_LONGEST)
        self.assertEqual(self.combined[0].tokens, GRAM_17)
        self.assertEqual(self.combined[0].hits_g, ((SIDE_GR, "Gr4", 3),))
        self.assertEqual(self.combined[0].hits_k, ((SIDE_KR, "Kr5", 0),))
        tokens = [row.tokens for row in self.combined]
        self.assertEqual(len(tokens), len(set(tokens)))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_side_inventory_and_gv_empty(self):
        """Gr–Kr 97, Gr–Kv 42, Gv vs K none. Per-side rows are the partition."""
        counts = tuple((g_side, k_side, len(rows)) for g_side, k_side, rows in self.per_side)
        self.assertEqual(counts, STANDING_PER_SIDE_COUNTS)
        gr_kr = self.per_side[0][2]
        gr_kv = self.per_side[1][2]
        self.assertEqual(
            tuple(row_tuple(row) for row in gr_kr),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_GR_KR_MAXIMALS)),
        )
        self.assertEqual(
            tuple(row_tuple(row) for row in gr_kv),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_GR_KV_MAXIMALS)),
        )
        self.assertEqual(self.per_side[2][2], ())
        self.assertEqual(self.per_side[3][2], ())
        self.assertEqual(len(gr_kr) + len(gr_kv), STANDING_DISTINCT_COUNT)
        self.assertTrue(islands_disjoint(STANDING_MAXIMALS))
        self.assertEqual(STANDING_FORMULA_ISLANDS, STANDING_MAXIMAL_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_coverage_and_same_text_claim(self):
        """Gr 77/355, Gv 0/359, Kr 52/131, Kv 25/95. Not same-text; not two formulas."""
        self.assertEqual(self.coverage, STANDING_COVERAGE)
        maximal_grams = tuple(row[0] for row in STANDING_MAXIMALS)
        self.assertEqual(score_coverage(self.by_side, maximal_grams), STANDING_COVERAGE)
        by_side = {side: (covered, total) for side, covered, total in self.coverage}
        self.assertEqual(by_side[SIDE_GR], (77, GR_STEM_TOTAL))
        self.assertEqual(by_side[SIDE_GV], (0, GV_STEM_TOTAL))
        self.assertEqual(by_side[SIDE_KR], (52, KR_STEM_TOTAL))
        self.assertEqual(by_side[SIDE_KV], (25, KV_STEM_TOTAL))
        self.assertEqual(by_side[SIDE_GR][0] + by_side[SIDE_GV][0], STANDING_COVERED_G)
        self.assertEqual(by_side[SIDE_KR][0] + by_side[SIDE_KV][0], STANDING_COVERED_K)
        self.assertEqual(STANDING_COVERED_G, STANDING_COVERED_K)
        self.assertEqual(STANDING_SAME_TEXT, False)
        self.assertEqual(STANDING_TWO_FORMULAS, False)
        self.assertEqual(STANDING_FORMULA_ISLANDS, 6)
        self.assertFalse(STANDING_SAME_TEXT)
        self.assertFalse(STANDING_TWO_FORMULAS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gr_kv_15gram_scoreboard_still_computes(self):
        """Cycle 66 Gr vs Kv 15-gram site lock stays."""
        prior = TestMamariSmallSantiagoLondonGrKv15gramScoreboard()
        prior.setUp()
        prior.test_n_tokens_sites_and_17gram_relation()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-67 n≥8 inventory lock."""
        lock = self.survey["tablet_g_k_shared_n8_inventory"]
        self.assertEqual(lock["cycle"], 67)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], MIN_N)
        self.assertEqual(lock["distinct_count"], STANDING_DISTINCT_COUNT)
        self.assertEqual(lock["maximal_count"], STANDING_MAXIMAL_COUNT)
        self.assertEqual(tuple(lock["by_n"]), STANDING_BY_N)
        locked_maximals = tuple(
            (
                tuple(tokens),
                n,
                freq_g,
                freq_k,
                tuple(g_site),
                tuple(k_site),
            )
            for tokens, n, freq_g, freq_k, g_site, k_site in lock["maximals"]
        )
        self.assertEqual(locked_maximals, STANDING_MAXIMALS)
        locked_sides = tuple(
            (g_side, k_side, count) for g_side, k_side, count in lock["per_side_counts"]
        )
        self.assertEqual(locked_sides, STANDING_PER_SIDE_COUNTS)
        locked_coverage = tuple(
            (side, covered, total) for side, covered, total in lock["coverage"]
        )
        self.assertEqual(locked_coverage, STANDING_COVERAGE)
        self.assertEqual(lock["covered_g"], STANDING_COVERED_G)
        self.assertEqual(lock["covered_k"], STANDING_COVERED_K)
        self.assertEqual(lock["same_text"], STANDING_SAME_TEXT)
        self.assertEqual(lock["two_formulas"], STANDING_TWO_FORMULAS)
        self.assertEqual(lock["formula_islands"], STANDING_FORMULA_ISLANDS)
        self.assertEqual(lock["islands_disjoint"], STANDING_ISLANDS_DISJOINT)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["stem_076_in_inventory"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_gr_locks_unchanged"])
        self.assertTrue(lock["standing_gv_locks_unchanged"])
        self.assertTrue(lock["standing_kr_locks_unchanged"])
        self.assertTrue(lock["standing_kv_locks_unchanged"])
        self.assertTrue(lock["standing_gk_parallel_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_hits_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_sites_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_hamming_unchanged"])
        self.assertTrue(lock["standing_gk_380_001_003_unchanged"])
        self.assertTrue(lock["standing_gk_gr_kv_15gram_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_gr_kv_15gram_sites"]["cycle"], 66)
        self.assertEqual(self.survey["tablet_g_k_380_001_003_hits_per_fixture"]["cycle"], 65)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonSharedN8ImageSnapshot(unittest.TestCase):
    """Cycle 67 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
