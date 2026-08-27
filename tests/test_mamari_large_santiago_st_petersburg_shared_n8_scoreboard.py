"""H–P exact shared stem n≥8 inventory and coverage.

Cycle 69 text-search lock. Uses the cycle-69 vendored Hr.html,
Hv.html, Pr.html, Pv.html and the existing parsers. Does not
scrape Q. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Same lock as cycle 67 did for G vs K: distinct shared n≥8 count,
maximal disjoint islands (n + sequence + sites), and coverage
(stems inside a shared n≥8) on each H/P side. Combined H is
Hr+Hv; combined P is Pr+Pv. Also the four per-side pairs.

Claim that can lose: H and P are a parallel pair (shared n≥8
exists and is not just 1–2 short formulas).

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
    HP_SIDE_PAIRS,
    HP_SIDES,
    LINE_NAMES,
    P_SIDES,
    SIDE_HR,
    SIDE_HV,
    SIDE_PR,
    SIDE_PV,
    STANDING_STEM_TOTALS,
    TestMamariLargeSantiagoStPetersburgVendorScoreboard,
    load_h_p_sides,
)
from tests.test_mamari_second_passage_scoreboard import (
    find_ngram_hits,
    load_corpus_survey,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    concat_sides,
    ngram_frequencies,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    MIN_N,
    SharedN8Row,
    count_by_n,
    covered_stem_count,
    expand_maximals,
    islands_disjoint,
    maximal_rows,
    row_tuple,
)

STANDING_MAXIMALS = (
    (("060", "069", "162", "200", "200", "200", "052", "200", "081", "200", "001", "004", "064", "044", "004", "049", "004", "044", "004", "064", "202", "280"), 22, 1, 1, (SIDE_HR, "Hr5", 6), (SIDE_PR, "Pr4", 71)),
    (("002", "144", "002", "662", "680", "005", "010", "005", "052", "022", "243", "001", "004"), 13, 1, 1, (SIDE_HR, "Hr8", 0), (SIDE_PR, "Pr7", 29)),
    (("606", "001", "006", "001", "006", "109", "050", "755", "001", "063", "013", "006", "065"), 13, 1, 1, (SIDE_HR, "Hr4", 45), (SIDE_PR, "Pr4", 22)),
    (("052", "022", "343", "005", "099", "011", "007", "004", "600", "522", "606", "609"), 12, 1, 1, (SIDE_HR, "Hr7", 44), (SIDE_PR, "Pr7", 7)),
    (("062", "006", "001", "062", "006", "001", "062", "006", "001", "020", "064"), 11, 1, 1, (SIDE_HR, "Hr3", 27), (SIDE_PR, "Pr3", 14)),
    (("755", "003", "734", "003", "306", "003", "001", "009", "005", "006", "074"), 11, 1, 1, (SIDE_HR, "Hr1", 32), (SIDE_PR, "Pr1", 32)),
    (("781", "140", "004", "004", "206", "558", "065", "003", "200", "004", "022"), 11, 1, 1, (SIDE_HR, "Hr3", 15), (SIDE_PR, "Pr3", 2)),
    (("005", "002", "041", "220", "009", "220", "009", "440", "440", "440"), 10, 1, 1, (SIDE_HR, "Hr5", 36), (SIDE_PR, "Pr5", 9)),
    (("022", "200", "060", "235", "120", "120", "005", "011", "010", "070"), 10, 1, 1, (SIDE_HV, "Hv9", 10), (SIDE_PV, "Pv10", 36)),
    (("050", "504", "003", "144", "020", "003", "200", "006", "003", "180"), 10, 1, 1, (SIDE_HV, "Hv7", 26), (SIDE_PV, "Pv8", 69)),
    (("081", "420", "052", "002", "010", "010", "450", "010", "144"), 9, 1, 1, (SIDE_HV, "Hv3", 10), (SIDE_PV, "Pv5", 19)),
    (("522", "254", "301", "015", "301", "200", "001", "200", "063"), 9, 1, 1, (SIDE_HV, "Hv3", 36), (SIDE_PV, "Pv5", 45)),
    (("001", "099", "010", "001", "050", "001", "010", "022"), 8, 1, 1, (SIDE_HR, "Hr10", 16), (SIDE_PR, "Pr9", 33)),
    (("022", "050", "007", "144", "733", "384", "074", "224"), 8, 1, 1, (SIDE_HV, "Hv10", 40), (SIDE_PV, "Pv11", 47)),
    (("022", "052", "002", "010", "002", "010", "144", "700"), 8, 1, 1, (SIDE_HV, "Hv6", 34), (SIDE_PV, "Pv8", 3)),
    (("200", "015", "022", "008", "451", "015", "022", "005"), 8, 1, 1, (SIDE_HR, "Hr6", 1), (SIDE_PR, "Pr5", 66)),
    (("301", "004", "064", "004", "064", "209", "081", "050"), 8, 1, 1, (SIDE_HV, "Hv2", 32), (SIDE_PV, "Pv4", 50)),
    (("711", "034", "046", "007", "001", "600", "205", "571"), 8, 1, 1, (SIDE_HV, "Hv9", 62), (SIDE_PV, "Pv11", 1)),
)
STANDING_HR_PR_MAXIMALS = tuple(row for row in STANDING_MAXIMALS if row[5][0] == SIDE_PR)
STANDING_HV_PV_MAXIMALS = tuple(row for row in STANDING_MAXIMALS if row[5][0] == SIDE_PV)
STANDING_MAXIMAL_COUNT = 18
STANDING_DISTINCT_COUNT = 237
STANDING_BY_N = (63, 45, 33, 23, 16, 12, 9, 8, 7, 6, 5, 4, 3, 2, 1)
STANDING_PER_SIDE_COUNTS = (
    (SIDE_HR, SIDE_PR, 215),
    (SIDE_HR, SIDE_PV, 0),
    (SIDE_HV, SIDE_PR, 0),
    (SIDE_HV, SIDE_PV, 22),
)
STANDING_COVERAGE = (
    (SIDE_HR, 119, STANDING_STEM_TOTALS[SIDE_HR]),
    (SIDE_HV, 70, STANDING_STEM_TOTALS[SIDE_HV]),
    (SIDE_PR, 119, STANDING_STEM_TOTALS[SIDE_PR]),
    (SIDE_PV, 70, STANDING_STEM_TOTALS[SIDE_PV]),
)
STANDING_COVERED_H = 189
STANDING_COVERED_P = 189
STANDING_SHARED_N8_EXISTS = True
STANDING_TWO_SHORT_FORMULAS = False
STANDING_CLAIM_HOLDS = True
STANDING_SAME_TEXT = False
STANDING_ISLANDS_DISJOINT = True
STANDING_TABLET_Q_SCRAPED = False
STANDING_RESULT = "hp_shared_n8_inventory"


def named_hp_hits(
    by_side: dict[str, list[list[str]]],
    sides: tuple[str, ...],
    gram: tuple[str, ...],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) for every exact hit on those H/P sides."""
    hits: list[tuple[str, str, int]] = []
    for side in sides:
        names = LINE_NAMES[side]
        for line_index, start in find_ngram_hits(by_side[side], gram):
            hits.append((side, names[line_index], start))
    return tuple(hits)


def score_hp_shared_n8(
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
                    hits_g=named_hp_hits(by_side, left_sides, tokens),
                    hits_k=named_hp_hits(by_side, right_sides, tokens),
                )
            )
    rows.sort(key=lambda row: (-row.n, row.tokens))
    return tuple(rows)


def score_hp_coverage(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] | list[tuple[str, ...]],
) -> tuple[tuple[str, int, int], ...]:
    """(side, covered, total) for Hr/Hv/Pr/Pv."""
    return tuple(
        (side, *covered_stem_count(by_side[side], grams)) for side in HP_SIDES
    )


class TestLargeSantiagoStPetersburgSharedN8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_min_n_excludes_short_and_records_hits(self):
        """n=7 share is dropped; n=8 is kept with line/index."""
        provider = MockProvider()
        by_side = {
            SIDE_HR: [["A", "B", "C", "D", "E", "F", "G", "H", "I"]],
            SIDE_HV: [["X"]],
            SIDE_PR: [["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"]],
            SIDE_PV: [["Y"]],
        }
        rows = score_hp_shared_n8(by_side, H_SIDES, P_SIDES)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0].n, 9)
        self.assertEqual(rows[0].tokens, ("A", "B", "C", "D", "E", "F", "G", "H", "I"))
        self.assertEqual(rows[0].hits_g, ((SIDE_HR, "Hr1", 0),))
        self.assertEqual(rows[0].hits_k, ((SIDE_PR, "Pr1", 1),))
        self.assertEqual(len(expand_maximals(STANDING_MAXIMALS)), STANDING_DISTINCT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_coverage_unions_windows(self):
        """Overlapping 8-grams union; a private 8-gram is not coverage."""
        provider = MockProvider()
        lines = [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        grams = [("1", "2", "3", "4", "5", "6", "7", "8")]
        self.assertEqual(covered_stem_count(lines, grams), (8, 10))
        self.assertTrue(islands_disjoint(STANDING_MAXIMALS))
        self.assertEqual(STANDING_ISLANDS_DISJOINT, True)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariLargeSantiagoStPetersburgSharedN8Scoreboard(unittest.TestCase):
    """Cited-fixture H vs P n≥8 inventory and coverage lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_h_p_sides()
        self.combined = score_hp_shared_n8(self.by_side, H_SIDES, P_SIDES)
        self.expanded = expand_maximals(STANDING_MAXIMALS)
        self.grams = tuple(row.tokens for row in self.combined)
        self.coverage = score_hp_coverage(self.by_side, self.grams)
        self.per_side = tuple(
            (
                h_side,
                p_side,
                score_hp_shared_n8(self.by_side, (h_side,), (p_side,)),
            )
            for h_side, p_side in HP_SIDE_PAIRS
        )

    def test_inventory_tokens_n_freq_and_hits(self):
        """237 distinct n≥8; each matches a maximal subspan with freq 1/1."""
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
        tokens = [row.tokens for row in self.combined]
        self.assertEqual(len(tokens), len(set(tokens)))
        self.assertTrue(STANDING_SHARED_N8_EXISTS)
        self.assertFalse(STANDING_TWO_SHORT_FORMULAS)
        self.assertTrue(STANDING_CLAIM_HOLDS)
        self.assertGreater(STANDING_MAXIMAL_COUNT, 2)
        self.assertGreater(STANDING_MAXIMALS[0][1], 8)
        self.assertFalse(STANDING_TABLET_Q_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_side_inventory_and_cross_empty(self):
        """Hr–Pr 215, Hv–Pv 22, cross-side pairs none."""
        counts = tuple((h_side, p_side, len(rows)) for h_side, p_side, rows in self.per_side)
        self.assertEqual(counts, STANDING_PER_SIDE_COUNTS)
        hr_pr = self.per_side[0][2]
        hv_pv = self.per_side[3][2]
        self.assertEqual(
            tuple(row_tuple(row) for row in hr_pr),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_HR_PR_MAXIMALS)),
        )
        self.assertEqual(
            tuple(row_tuple(row) for row in hv_pv),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_HV_PV_MAXIMALS)),
        )
        self.assertEqual(self.per_side[1][2], ())
        self.assertEqual(self.per_side[2][2], ())
        self.assertEqual(len(hr_pr) + len(hv_pv), STANDING_DISTINCT_COUNT)
        self.assertTrue(islands_disjoint(STANDING_MAXIMALS))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_coverage_and_parallel_claim(self):
        """Hr 119/771, Hv 70/831, Pr 119/825, Pv 70/739. Parallel, not two formulas."""
        self.assertEqual(self.coverage, STANDING_COVERAGE)
        maximal_grams = tuple(row[0] for row in STANDING_MAXIMALS)
        self.assertEqual(score_hp_coverage(self.by_side, maximal_grams), STANDING_COVERAGE)
        by_side = {side: (covered, total) for side, covered, total in self.coverage}
        self.assertEqual(by_side[SIDE_HR], (119, STANDING_STEM_TOTALS[SIDE_HR]))
        self.assertEqual(by_side[SIDE_HV], (70, STANDING_STEM_TOTALS[SIDE_HV]))
        self.assertEqual(by_side[SIDE_PR], (119, STANDING_STEM_TOTALS[SIDE_PR]))
        self.assertEqual(by_side[SIDE_PV], (70, STANDING_STEM_TOTALS[SIDE_PV]))
        self.assertEqual(by_side[SIDE_HR][0] + by_side[SIDE_HV][0], STANDING_COVERED_H)
        self.assertEqual(by_side[SIDE_PR][0] + by_side[SIDE_PV][0], STANDING_COVERED_P)
        self.assertEqual(STANDING_COVERED_H, STANDING_COVERED_P)
        self.assertEqual(STANDING_SAME_TEXT, False)
        self.assertEqual(STANDING_TWO_SHORT_FORMULAS, False)
        self.assertTrue(STANDING_CLAIM_HOLDS)
        self.assertTrue(STANDING_SHARED_N8_EXISTS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_hp_vendor_scoreboard_still_computes(self):
        """Cycle 69 H/P vendor and G–K island-absent lock stays."""
        prior = TestMamariLargeSantiagoStPetersburgVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_gk_islands_absent()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-69 H/P n≥8 inventory lock."""
        lock = self.survey["tablet_h_p_shared_n8_inventory"]
        self.assertEqual(lock["cycle"], 69)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], MIN_N)
        self.assertEqual(lock["distinct_count"], STANDING_DISTINCT_COUNT)
        self.assertEqual(lock["maximal_count"], STANDING_MAXIMAL_COUNT)
        self.assertEqual(tuple(lock["by_n"]), STANDING_BY_N)
        locked_maximals = tuple(
            (
                tuple(tokens),
                n,
                freq_h,
                freq_p,
                tuple(h_site),
                tuple(p_site),
            )
            for tokens, n, freq_h, freq_p, h_site, p_site in lock["maximals"]
        )
        self.assertEqual(locked_maximals, STANDING_MAXIMALS)
        locked_sides = tuple(
            (h_side, p_side, count) for h_side, p_side, count in lock["per_side_counts"]
        )
        self.assertEqual(locked_sides, STANDING_PER_SIDE_COUNTS)
        locked_coverage = tuple(
            (side, covered, total) for side, covered, total in lock["coverage"]
        )
        self.assertEqual(locked_coverage, STANDING_COVERAGE)
        self.assertEqual(lock["covered_h"], STANDING_COVERED_H)
        self.assertEqual(lock["covered_p"], STANDING_COVERED_P)
        self.assertEqual(lock["shared_n8_exists"], STANDING_SHARED_N8_EXISTS)
        self.assertEqual(lock["two_short_formulas"], STANDING_TWO_SHORT_FORMULAS)
        self.assertEqual(lock["claim_holds"], STANDING_CLAIM_HOLDS)
        self.assertEqual(lock["same_text"], STANDING_SAME_TEXT)
        self.assertEqual(lock["islands_disjoint"], STANDING_ISLANDS_DISJOINT)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["tablet_q_scraped"])
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
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_h_p_grand_tradition_vendor"]["cycle"], 69)
        self.assertEqual(self.survey["tablet_g_k_island_off_gk_hits"]["cycle"], 68)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariLargeSantiagoStPetersburgSharedN8ImageSnapshot(unittest.TestCase):
    """Cycle 69 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
