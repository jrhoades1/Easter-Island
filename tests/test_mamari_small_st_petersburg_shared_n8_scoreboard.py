"""Q vs H and Q vs P exact shared stem n≥8 inventory and coverage.

Cycle 70 text-search lock. Uses the cycle-70 vendored Qr.html /
Qv.html, the cycle-69 Hr/Hv/Pr/Pv fixtures, and the existing
parsers. Does not scrape D. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same lock as cycle 69 did for H vs P: distinct shared n≥8 count,
maximal disjoint islands (n + sequence + sites), and coverage
(stems inside a shared n≥8) on each side. Combined Q is Qr+Qv.

Claim that can lose: Q participates in the H/P parallel (shared
n≥8 with H and/or P exists and is not 1–2 short formulas).

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_large_santiago_st_petersburg_shared_n8_scoreboard import (
    TestMamariLargeSantiagoStPetersburgSharedN8Scoreboard,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
    LINE_NAMES as HP_LINE_NAMES,
    P_SIDES,
    SIDE_HR,
    SIDE_HV,
    SIDE_PR,
    SIDE_PV,
    STANDING_STEM_TOTALS as HP_STEM_TOTALS,
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
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    Q_LINE_NAMES,
    Q_SIDES,
    SIDE_QR,
    SIDE_QV,
    STANDING_STEM_TOTALS as Q_STEM_TOTALS,
    TestMamariSmallStPetersburgVendorScoreboard,
    load_q_sides,
)

LINE_NAMES = {**HP_LINE_NAMES, **Q_LINE_NAMES}
QH_SIDE_PAIRS = (
    (SIDE_QR, SIDE_HR),
    (SIDE_QR, SIDE_HV),
    (SIDE_QV, SIDE_HR),
    (SIDE_QV, SIDE_HV),
)
QP_SIDE_PAIRS = (
    (SIDE_QR, SIDE_PR),
    (SIDE_QR, SIDE_PV),
    (SIDE_QV, SIDE_PR),
    (SIDE_QV, SIDE_PV),
)

STANDING_QH_MAXIMALS = (
    (("003", "004", "600", "004", "006", "042", "003", "050", "003", "093", "003", "027", "003", "086", "003", "060", "003", "093", "003", "254", "003", "093", "003", "205", "072", "450", "052", "551", "003", "600", "003"), 31, 1, 1, (SIDE_QR, "Qr3", 19), (SIDE_HR, "Hr3", 39)),
    (("003", "306", "003", "084", "004", "280", "200", "048", "254", "755", "003", "734", "003", "306", "003"), 15, 1, 1, (SIDE_QR, "Qr1", 3), (SIDE_HR, "Hr1", 23)),
    (("631", "208", "200", "005", "021", "005", "002", "041", "220", "009", "220", "009", "440", "440", "440"), 15, 1, 1, (SIDE_QR, "Qr5", 10), (SIDE_HR, "Hr5", 31)),
    (("700", "061", "739", "040", "140", "316", "301", "004", "064", "004", "064", "209", "081", "050"), 14, 1, 1, (SIDE_QV, "Qv5", 5), (SIDE_HV, "Hv2", 26)),
    (("050", "600", "430", "076", "430", "076", "076", "063", "004", "064", "670", "700", "470"), 13, 1, 1, (SIDE_QR, "Qr9", 17), (SIDE_HR, "Hr9", 21)),
    (("520", "381", "008", "001", "008", "739", "065", "306", "431", "200", "276", "011", "385"), 13, 1, 1, (SIDE_QR, "Qr6", 0), (SIDE_HR, "Hr6", 32)),
    (("002", "144", "002", "662", "680", "005", "010", "005", "052", "022", "243", "001"), 12, 1, 1, (SIDE_QR, "Qr7", 47), (SIDE_HR, "Hr8", 0)),
    (("062", "006", "001", "062", "006", "001", "062", "006", "001", "020", "064"), 11, 1, 1, (SIDE_QR, "Qr3", 7), (SIDE_HR, "Hr3", 27)),
    (("381", "072", "450", "052", "551", "003", "600", "003", "385", "003", "670"), 11, 1, 1, (SIDE_QR, "Qr3", 51), (SIDE_HR, "Hr3", 71)),
    (("004", "064", "087", "430", "214", "002", "203", "027", "090", "545"), 10, 1, 1, (SIDE_QR, "Qr6", 28), (SIDE_HR, "Hr6", 62)),
    (("400", "072", "002", "003", "072", "002", "430", "072", "002", "200"), 10, 1, 1, (SIDE_QV, "Qv8", 0), (SIDE_HV, "Hv5", 29)),
    (("500", "440", "280", "002", "040", "050", "216", "001", "366", "076"), 10, 1, 1, (SIDE_QR, "Qr6", 40), (SIDE_HR, "Hr7", 2)),
    (("720", "244", "381", "002", "631", "099", "721", "022", "001", "062"), 10, 1, 1, (SIDE_QR, "Qr2", 3), (SIDE_HR, "Hr2", 39)),
    (("005", "099", "011", "007", "004", "600", "522", "606"), 8, 1, 1, (SIDE_QR, "Qr7", 28), (SIDE_HR, "Hr7", 47)),
    (("430", "002", "010", "002", "010", "144", "026", "006"), 8, 1, 1, (SIDE_QV, "Qv7", 35), (SIDE_HV, "Hv4", 53)),
)
STANDING_QP_MAXIMALS = (
    (("206", "430", "600", "027", "700", "011", "078", "308", "034", "021", "021", "380", "020", "385", "205", "001", "381"), 17, 1, 1, (SIDE_QV, "Qv4", 12), (SIDE_PV, "Pv3", 30)),
    (("062", "006", "001", "062", "006", "001", "062", "006", "001", "020", "064", "202", "003", "004", "600"), 15, 1, 1, (SIDE_QR, "Qr3", 7), (SIDE_PR, "Pr3", 14)),
    (("022", "002", "144", "002", "662", "680", "005", "010", "005", "052", "022", "243", "001"), 13, 1, 1, (SIDE_QR, "Qr7", 46), (SIDE_PR, "Pr7", 28)),
    (("301", "004", "064", "004", "064", "209", "081", "050", "450", "052", "240", "069"), 12, 1, 1, (SIDE_QV, "Qv5", 11), (SIDE_PV, "Pv4", 50)),
    (("005", "002", "041", "220", "009", "220", "009", "440", "440", "440", "440"), 11, 1, 1, (SIDE_QR, "Qr5", 15), (SIDE_PR, "Pr5", 9)),
    (("020", "004", "021", "020", "280", "021", "027", "600", "209", "600"), 10, 1, 1, (SIDE_QV, "Qv3", 2), (SIDE_PV, "Pv2", 18)),
    (("755", "006", "770", "060", "070", "061", "001", "061", "386"), 9, 1, 1, (SIDE_QR, "Qr9", 46), (SIDE_PR, "Pr9", 11)),
    (("005", "099", "011", "007", "004", "600", "522", "606"), 8, 1, 1, (SIDE_QR, "Qr7", 28), (SIDE_PR, "Pr7", 10)),
)
STANDING_QR_HR_MAXIMALS = tuple(row for row in STANDING_QH_MAXIMALS if row[5][0] == SIDE_HR)
STANDING_QV_HV_MAXIMALS = tuple(row for row in STANDING_QH_MAXIMALS if row[5][0] == SIDE_HV)
STANDING_QR_PR_MAXIMALS = tuple(row for row in STANDING_QP_MAXIMALS if row[5][0] == SIDE_PR)
STANDING_QV_PV_MAXIMALS = tuple(row for row in STANDING_QP_MAXIMALS if row[5][0] == SIDE_PV)
STANDING_QH_MAXIMAL_COUNT = 15
STANDING_QP_MAXIMAL_COUNT = 8
STANDING_QH_DISTINCT_COUNT = 503
STANDING_QP_DISTINCT_COUNT = 147
STANDING_QH_BY_N = (86, 71, 58, 45, 36, 29, 23, 19, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
STANDING_QP_BY_N = (39, 31, 24, 18, 13, 9, 6, 4, 2, 1)
STANDING_QH_PER_SIDE_COUNTS = (
    (SIDE_QR, SIDE_HR, 468),
    (SIDE_QR, SIDE_HV, 0),
    (SIDE_QV, SIDE_HR, 0),
    (SIDE_QV, SIDE_HV, 35),
)
STANDING_QP_PER_SIDE_COUNTS = (
    (SIDE_QR, SIDE_PR, 71),
    (SIDE_QR, SIDE_PV, 0),
    (SIDE_QV, SIDE_PR, 0),
    (SIDE_QV, SIDE_PV, 76),
)
STANDING_QH_COVERAGE = (
    (SIDE_QR, 159, Q_STEM_TOTALS[SIDE_QR]),
    (SIDE_QV, 32, Q_STEM_TOTALS[SIDE_QV]),
    (SIDE_HR, 159, HP_STEM_TOTALS[SIDE_HR]),
    (SIDE_HV, 32, HP_STEM_TOTALS[SIDE_HV]),
)
STANDING_QP_COVERAGE = (
    (SIDE_QR, 56, Q_STEM_TOTALS[SIDE_QR]),
    (SIDE_QV, 39, Q_STEM_TOTALS[SIDE_QV]),
    (SIDE_PR, 56, HP_STEM_TOTALS[SIDE_PR]),
    (SIDE_PV, 39, HP_STEM_TOTALS[SIDE_PV]),
)
STANDING_QH_COVERED_Q = 191
STANDING_QH_COVERED_H = 191
STANDING_QP_COVERED_Q = 95
STANDING_QP_COVERED_P = 95
STANDING_SHARED_N8_EXISTS = True
STANDING_TWO_SHORT_FORMULAS = False
STANDING_CLAIM_HOLDS = True
STANDING_SAME_TEXT = False
STANDING_ISLANDS_DISJOINT = True
STANDING_TABLET_D_SCRAPED = False
STANDING_RESULT = "q_hp_shared_n8_inventory"


def load_q_h_p_sides() -> dict[str, list[list[str]]]:
    """Qr / Qv plus cycle-69 H/P stems. No D scrape."""
    return {**load_h_p_sides(), **load_q_sides()}


def named_qhp_hits(
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


def score_qhp_shared_n8(
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
                    hits_g=named_qhp_hits(by_side, left_sides, tokens),
                    hits_k=named_qhp_hits(by_side, right_sides, tokens),
                )
            )
    rows.sort(key=lambda row: (-row.n, row.tokens))
    return tuple(rows)


def score_pair_coverage(
    by_side: dict[str, list[list[str]]],
    sides: tuple[str, ...],
    grams: tuple[tuple[str, ...], ...] | list[tuple[str, ...]],
) -> tuple[tuple[str, int, int], ...]:
    """(side, covered, total) for the named sides."""
    return tuple((side, *covered_stem_count(by_side[side], grams)) for side in sides)


class TestSmallStPetersburgSharedN8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_min_n_excludes_short_and_records_hits(self):
        """n=7 share is dropped; n=8 is kept with line/index."""
        provider = MockProvider()
        by_side = load_q_h_p_sides()
        by_side[SIDE_QR] = [["A", "B", "C", "D", "E", "F", "G", "H", "I"]]
        by_side[SIDE_QV] = [["X"]]
        by_side[SIDE_HR] = [["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"]]
        by_side[SIDE_HV] = [["Y"]]
        rows = score_qhp_shared_n8(by_side, Q_SIDES, H_SIDES)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0].n, 9)
        self.assertEqual(rows[0].tokens, ("A", "B", "C", "D", "E", "F", "G", "H", "I"))
        self.assertEqual(rows[0].hits_g, ((SIDE_QR, "Qr1", 0),))
        self.assertEqual(rows[0].hits_k, ((SIDE_HR, "Hr1", 1),))
        self.assertEqual(len(expand_maximals(STANDING_QH_MAXIMALS)), STANDING_QH_DISTINCT_COUNT)
        self.assertEqual(len(expand_maximals(STANDING_QP_MAXIMALS)), STANDING_QP_DISTINCT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_coverage_unions_windows(self):
        """Overlapping 8-grams union; a private 8-gram is not coverage."""
        provider = MockProvider()
        lines = [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        grams = [("1", "2", "3", "4", "5", "6", "7", "8")]
        self.assertEqual(covered_stem_count(lines, grams), (8, 10))
        self.assertTrue(islands_disjoint(STANDING_QH_MAXIMALS))
        self.assertTrue(islands_disjoint(STANDING_QP_MAXIMALS))
        self.assertEqual(STANDING_ISLANDS_DISJOINT, True)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallStPetersburgSharedN8Scoreboard(unittest.TestCase):
    """Cited-fixture Q vs H and Q vs P n≥8 inventory lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_q_h_p_sides()
        self.qh = score_qhp_shared_n8(self.by_side, Q_SIDES, H_SIDES)
        self.qp = score_qhp_shared_n8(self.by_side, Q_SIDES, P_SIDES)
        self.qh_coverage = score_pair_coverage(
            self.by_side, Q_SIDES + H_SIDES, tuple(row.tokens for row in self.qh)
        )
        self.qp_coverage = score_pair_coverage(
            self.by_side, Q_SIDES + P_SIDES, tuple(row.tokens for row in self.qp)
        )
        self.qh_per_side = tuple(
            (q_side, h_side, score_qhp_shared_n8(self.by_side, (q_side,), (h_side,)))
            for q_side, h_side in QH_SIDE_PAIRS
        )
        self.qp_per_side = tuple(
            (q_side, p_side, score_qhp_shared_n8(self.by_side, (q_side,), (p_side,)))
            for q_side, p_side in QP_SIDE_PAIRS
        )

    def test_q_vs_h_inventory_tokens_n_freq_and_hits(self):
        """503 distinct Q–H n≥8; each matches a maximal subspan with freq 1/1."""
        self.assertEqual(len(self.qh), STANDING_QH_DISTINCT_COUNT)
        self.assertEqual(len(expand_maximals(STANDING_QH_MAXIMALS)), STANDING_QH_DISTINCT_COUNT)
        self.assertEqual(
            tuple(row_tuple(row) for row in self.qh),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_QH_MAXIMALS)),
        )
        self.assertEqual(count_by_n(self.qh), STANDING_QH_BY_N)
        self.assertEqual(len(maximal_rows(self.qh)), STANDING_QH_MAXIMAL_COUNT)
        locked = tuple(
            (row.tokens, row.n, row.freq_g, row.freq_k, row.hits_g[0], row.hits_k[0])
            for row in maximal_rows(self.qh)
        )
        self.assertEqual(locked, STANDING_QH_MAXIMALS)
        for row in self.qh:
            self.assertGreaterEqual(row.n, MIN_N)
            self.assertEqual(len(row.tokens), row.n)
            self.assertEqual((row.freq_g, row.freq_k), (1, 1))
            self.assertEqual(len(row.hits_g), 1)
            self.assertEqual(len(row.hits_k), 1)
        self.assertEqual(len({row.tokens for row in self.qh}), STANDING_QH_DISTINCT_COUNT)
        self.assertTrue(STANDING_SHARED_N8_EXISTS)
        self.assertFalse(STANDING_TWO_SHORT_FORMULAS)
        self.assertTrue(STANDING_CLAIM_HOLDS)
        self.assertGreater(STANDING_QH_MAXIMAL_COUNT, 2)
        self.assertGreater(STANDING_QH_MAXIMALS[0][1], 8)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_q_vs_p_inventory_tokens_n_freq_and_hits(self):
        """147 distinct Q–P n≥8; each matches a maximal subspan with freq 1/1."""
        self.assertEqual(len(self.qp), STANDING_QP_DISTINCT_COUNT)
        self.assertEqual(len(expand_maximals(STANDING_QP_MAXIMALS)), STANDING_QP_DISTINCT_COUNT)
        self.assertEqual(
            tuple(row_tuple(row) for row in self.qp),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_QP_MAXIMALS)),
        )
        self.assertEqual(count_by_n(self.qp), STANDING_QP_BY_N)
        self.assertEqual(len(maximal_rows(self.qp)), STANDING_QP_MAXIMAL_COUNT)
        locked = tuple(
            (row.tokens, row.n, row.freq_g, row.freq_k, row.hits_g[0], row.hits_k[0])
            for row in maximal_rows(self.qp)
        )
        self.assertEqual(locked, STANDING_QP_MAXIMALS)
        for row in self.qp:
            self.assertGreaterEqual(row.n, MIN_N)
            self.assertEqual(len(row.tokens), row.n)
            self.assertEqual((row.freq_g, row.freq_k), (1, 1))
            self.assertEqual(len(row.hits_g), 1)
            self.assertEqual(len(row.hits_k), 1)
        self.assertEqual(len({row.tokens for row in self.qp}), STANDING_QP_DISTINCT_COUNT)
        self.assertGreater(STANDING_QP_MAXIMAL_COUNT, 2)
        self.assertGreater(STANDING_QP_MAXIMALS[0][1], 8)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_side_inventory_and_cross_empty(self):
        """Qr–Hr 468, Qv–Hv 35, Qr–Pr 71, Qv–Pv 76; cross-side pairs none."""
        qh_counts = tuple((q, h, len(rows)) for q, h, rows in self.qh_per_side)
        qp_counts = tuple((q, p, len(rows)) for q, p, rows in self.qp_per_side)
        self.assertEqual(qh_counts, STANDING_QH_PER_SIDE_COUNTS)
        self.assertEqual(qp_counts, STANDING_QP_PER_SIDE_COUNTS)
        qr_hr = self.qh_per_side[0][2]
        qv_hv = self.qh_per_side[3][2]
        qr_pr = self.qp_per_side[0][2]
        qv_pv = self.qp_per_side[3][2]
        self.assertEqual(
            tuple(row_tuple(row) for row in qr_hr),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_QR_HR_MAXIMALS)),
        )
        self.assertEqual(
            tuple(row_tuple(row) for row in qv_hv),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_QV_HV_MAXIMALS)),
        )
        self.assertEqual(
            tuple(row_tuple(row) for row in qr_pr),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_QR_PR_MAXIMALS)),
        )
        self.assertEqual(
            tuple(row_tuple(row) for row in qv_pv),
            tuple(row_tuple(row) for row in expand_maximals(STANDING_QV_PV_MAXIMALS)),
        )
        self.assertEqual(self.qh_per_side[1][2], ())
        self.assertEqual(self.qh_per_side[2][2], ())
        self.assertEqual(self.qp_per_side[1][2], ())
        self.assertEqual(self.qp_per_side[2][2], ())
        self.assertEqual(len(qr_hr) + len(qv_hv), STANDING_QH_DISTINCT_COUNT)
        self.assertEqual(len(qr_pr) + len(qv_pv), STANDING_QP_DISTINCT_COUNT)
        self.assertTrue(islands_disjoint(STANDING_QH_MAXIMALS))
        self.assertTrue(islands_disjoint(STANDING_QP_MAXIMALS))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_coverage_and_parallel_claim(self):
        """Q–H 191/191 and Q–P 95/95. Parallel, not two short formulas."""
        self.assertEqual(self.qh_coverage, STANDING_QH_COVERAGE)
        self.assertEqual(self.qp_coverage, STANDING_QP_COVERAGE)
        qh_grams = tuple(row[0] for row in STANDING_QH_MAXIMALS)
        qp_grams = tuple(row[0] for row in STANDING_QP_MAXIMALS)
        self.assertEqual(
            score_pair_coverage(self.by_side, Q_SIDES + H_SIDES, qh_grams),
            STANDING_QH_COVERAGE,
        )
        self.assertEqual(
            score_pair_coverage(self.by_side, Q_SIDES + P_SIDES, qp_grams),
            STANDING_QP_COVERAGE,
        )
        qh = {side: (covered, total) for side, covered, total in self.qh_coverage}
        qp = {side: (covered, total) for side, covered, total in self.qp_coverage}
        self.assertEqual(qh[SIDE_QR][0] + qh[SIDE_QV][0], STANDING_QH_COVERED_Q)
        self.assertEqual(qh[SIDE_HR][0] + qh[SIDE_HV][0], STANDING_QH_COVERED_H)
        self.assertEqual(qp[SIDE_QR][0] + qp[SIDE_QV][0], STANDING_QP_COVERED_Q)
        self.assertEqual(qp[SIDE_PR][0] + qp[SIDE_PV][0], STANDING_QP_COVERED_P)
        self.assertEqual(STANDING_QH_COVERED_Q, STANDING_QH_COVERED_H)
        self.assertEqual(STANDING_QP_COVERED_Q, STANDING_QP_COVERED_P)
        self.assertEqual(STANDING_SAME_TEXT, False)
        self.assertEqual(STANDING_TWO_SHORT_FORMULAS, False)
        self.assertTrue(STANDING_CLAIM_HOLDS)
        self.assertTrue(STANDING_SHARED_N8_EXISTS)
        self.assertTrue(bool(self.qh) or bool(self.qp))
        self.assertGreater(STANDING_QH_MAXIMAL_COUNT + STANDING_QP_MAXIMAL_COUNT, 2)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_hp_shared_n8_and_q_vendor_still_compute(self):
        """Cycle 69 H/P n≥8 and cycle-70 Q vendor locks stay."""
        prior = TestMamariLargeSantiagoStPetersburgSharedN8Scoreboard()
        prior.setUp()
        prior.test_inventory_tokens_n_freq_and_hits()
        prior.test_coverage_and_parallel_claim()
        prior.test_survey_matches_computed_lock()
        vendor = TestMamariSmallStPetersburgVendorScoreboard()
        vendor.setUp()
        vendor.test_stem_counts_and_gk_islands_absent()
        vendor.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-70 Q vs H/P n≥8 inventory."""
        lock = self.survey["tablet_q_shared_n8_inventory"]
        self.assertEqual(lock["cycle"], 70)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["min_n"], MIN_N)
        self.assertEqual(lock["q_vs_h"]["distinct_count"], STANDING_QH_DISTINCT_COUNT)
        self.assertEqual(lock["q_vs_h"]["maximal_count"], STANDING_QH_MAXIMAL_COUNT)
        self.assertEqual(tuple(lock["q_vs_h"]["by_n"]), STANDING_QH_BY_N)
        self.assertEqual(lock["q_vs_p"]["distinct_count"], STANDING_QP_DISTINCT_COUNT)
        self.assertEqual(lock["q_vs_p"]["maximal_count"], STANDING_QP_MAXIMAL_COUNT)
        self.assertEqual(tuple(lock["q_vs_p"]["by_n"]), STANDING_QP_BY_N)
        locked_qh = tuple(
            (tuple(tokens), n, freq_q, freq_h, tuple(q_site), tuple(h_site))
            for tokens, n, freq_q, freq_h, q_site, h_site in lock["q_vs_h"]["maximals"]
        )
        locked_qp = tuple(
            (tuple(tokens), n, freq_q, freq_p, tuple(q_site), tuple(p_site))
            for tokens, n, freq_q, freq_p, q_site, p_site in lock["q_vs_p"]["maximals"]
        )
        self.assertEqual(locked_qh, STANDING_QH_MAXIMALS)
        self.assertEqual(locked_qp, STANDING_QP_MAXIMALS)
        self.assertEqual(
            tuple((q, h, count) for q, h, count in lock["q_vs_h"]["per_side_counts"]),
            STANDING_QH_PER_SIDE_COUNTS,
        )
        self.assertEqual(
            tuple((q, p, count) for q, p, count in lock["q_vs_p"]["per_side_counts"]),
            STANDING_QP_PER_SIDE_COUNTS,
        )
        self.assertEqual(
            tuple((side, covered, total) for side, covered, total in lock["q_vs_h"]["coverage"]),
            STANDING_QH_COVERAGE,
        )
        self.assertEqual(
            tuple((side, covered, total) for side, covered, total in lock["q_vs_p"]["coverage"]),
            STANDING_QP_COVERAGE,
        )
        self.assertEqual(lock["q_vs_h"]["covered_q"], STANDING_QH_COVERED_Q)
        self.assertEqual(lock["q_vs_h"]["covered_h"], STANDING_QH_COVERED_H)
        self.assertEqual(lock["q_vs_p"]["covered_q"], STANDING_QP_COVERED_Q)
        self.assertEqual(lock["q_vs_p"]["covered_p"], STANDING_QP_COVERED_P)
        self.assertEqual(lock["shared_n8_exists"], STANDING_SHARED_N8_EXISTS)
        self.assertEqual(lock["two_short_formulas"], STANDING_TWO_SHORT_FORMULAS)
        self.assertEqual(lock["claim_holds"], STANDING_CLAIM_HOLDS)
        self.assertEqual(lock["same_text"], STANDING_SAME_TEXT)
        self.assertEqual(lock["islands_disjoint"], STANDING_ISLANDS_DISJOINT)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_hp_vendor_unchanged"])
        self.assertTrue(lock["standing_hp_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_q_small_st_petersburg_vendor"]["cycle"], 70)
        self.assertEqual(self.survey["tablet_h_p_shared_n8_inventory"]["cycle"], 69)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallStPetersburgSharedN8ImageSnapshot(unittest.TestCase):
    """Cycle 70 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
