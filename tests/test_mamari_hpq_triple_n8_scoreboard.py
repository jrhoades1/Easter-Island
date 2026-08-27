"""H∩P∩Q exact shared stem n≥8 inventory and coverage.

Cycle 71 text-search lock. Uses already-vendored Hr/Hv, Pr/Pv,
Qr/Qv and the existing parsers. Does not scrape D. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. Not a meaning dictionary.

Pairwise cycle 69/70 locked H vs P, Q vs H, and Q vs P. This
cycle locks the triple: distinct n≥8 present on all three
tablets, maximal disjoint islands (n + sequence + one site per
tablet), and coverage on each of the six sides.

Claim that can lose: the triple set is empty, 1–2 short
formulas, or a real multi-island tradition.

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
    P_SIDES,
    SIDE_HR,
    SIDE_HV,
    SIDE_PR,
    SIDE_PV,
    STANDING_STEM_TOTALS as HP_STEM_TOTALS,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    concat_sides,
    ngram_frequencies,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    MIN_N,
    count_by_n,
    covered_stem_count,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    TestMamariSmallStPetersburgSharedN8Scoreboard,
    load_q_h_p_sides,
    named_qhp_hits,
    score_pair_coverage,
)
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    Q_SIDES,
    SIDE_QR,
    SIDE_QV,
    STANDING_STEM_TOTALS as Q_STEM_TOTALS,
)

HPQ_SIDES = H_SIDES + P_SIDES + Q_SIDES
HPQ_SIDE_TRIPLES = (
    (SIDE_HR, SIDE_PR, SIDE_QR),
    (SIDE_HR, SIDE_PR, SIDE_QV),
    (SIDE_HR, SIDE_PV, SIDE_QR),
    (SIDE_HR, SIDE_PV, SIDE_QV),
    (SIDE_HV, SIDE_PR, SIDE_QR),
    (SIDE_HV, SIDE_PR, SIDE_QV),
    (SIDE_HV, SIDE_PV, SIDE_QR),
    (SIDE_HV, SIDE_PV, SIDE_QV),
)

STANDING_MAXIMALS = (
    (("002", "144", "002", "662", "680", "005", "010", "005", "052", "022", "243", "001"), 12, 1, 1, 1, (SIDE_HR, "Hr8", 0), (SIDE_PR, "Pr7", 29), (SIDE_QR, "Qr7", 47)),
    (("062", "006", "001", "062", "006", "001", "062", "006", "001", "020", "064"), 11, 1, 1, 1, (SIDE_HR, "Hr3", 27), (SIDE_PR, "Pr3", 14), (SIDE_QR, "Qr3", 7)),
    (("005", "002", "041", "220", "009", "220", "009", "440", "440", "440"), 10, 1, 1, 1, (SIDE_HR, "Hr5", 36), (SIDE_PR, "Pr5", 9), (SIDE_QR, "Qr5", 15)),
    (("005", "099", "011", "007", "004", "600", "522", "606"), 8, 1, 1, 1, (SIDE_HR, "Hr7", 47), (SIDE_PR, "Pr7", 10), (SIDE_QR, "Qr7", 28)),
    (("301", "004", "064", "004", "064", "209", "081", "050"), 8, 1, 1, 1, (SIDE_HV, "Hv2", 32), (SIDE_PV, "Pv4", 50), (SIDE_QV, "Qv5", 11)),
)
STANDING_HR_PR_QR_MAXIMALS = tuple(
    row for row in STANDING_MAXIMALS if row[5][0] == SIDE_HR
)
STANDING_HV_PV_QV_MAXIMALS = tuple(
    row for row in STANDING_MAXIMALS if row[5][0] == SIDE_HV
)
STANDING_MAXIMAL_COUNT = 5
STANDING_DISTINCT_COUNT = 33
STANDING_BY_N = (14, 9, 6, 3, 1)
STANDING_PER_SIDE_COUNTS = (
    (SIDE_HR, SIDE_PR, SIDE_QR, 32),
    (SIDE_HR, SIDE_PR, SIDE_QV, 0),
    (SIDE_HR, SIDE_PV, SIDE_QR, 0),
    (SIDE_HR, SIDE_PV, SIDE_QV, 0),
    (SIDE_HV, SIDE_PR, SIDE_QR, 0),
    (SIDE_HV, SIDE_PR, SIDE_QV, 0),
    (SIDE_HV, SIDE_PV, SIDE_QR, 0),
    (SIDE_HV, SIDE_PV, SIDE_QV, 1),
)
STANDING_COVERAGE = (
    (SIDE_HR, 41, HP_STEM_TOTALS[SIDE_HR]),
    (SIDE_HV, 8, HP_STEM_TOTALS[SIDE_HV]),
    (SIDE_PR, 41, HP_STEM_TOTALS[SIDE_PR]),
    (SIDE_PV, 8, HP_STEM_TOTALS[SIDE_PV]),
    (SIDE_QR, 41, Q_STEM_TOTALS[SIDE_QR]),
    (SIDE_QV, 8, Q_STEM_TOTALS[SIDE_QV]),
)
STANDING_COVERED_H = 49
STANDING_COVERED_P = 49
STANDING_COVERED_Q = 49
STANDING_EMPTY = False
STANDING_TWO_SHORT_FORMULAS = False
STANDING_MULTI_ISLAND_TRADITION = True
STANDING_SAME_TEXT = False
STANDING_ISLANDS_DISJOINT = True
STANDING_TABLET_D_SCRAPED = False
STANDING_NEW_TABLET = False
STANDING_RESULT = "hpq_triple_n8_inventory"


@dataclass(frozen=True)
class TripleN8Row:
    """One exact H∩P∩Q n≥8. Ids only; no meanings."""

    tokens: tuple[str, ...]
    n: int
    freq_h: int
    freq_p: int
    freq_q: int
    hits_h: tuple[tuple[str, str, int], ...]
    hits_p: tuple[tuple[str, str, int], ...]
    hits_q: tuple[tuple[str, str, int], ...]


def triple_row_tuple(row: TripleN8Row) -> tuple:
    """Stable lock row: tokens, n, freqs, hits."""
    return (
        row.tokens,
        row.n,
        row.freq_h,
        row.freq_p,
        row.freq_q,
        row.hits_h,
        row.hits_p,
        row.hits_q,
    )


def score_hpq_triple_n8(
    by_side: dict[str, list[list[str]]],
    h_sides: tuple[str, ...],
    p_sides: tuple[str, ...],
    q_sides: tuple[str, ...],
    min_n: int = MIN_N,
) -> tuple[TripleN8Row, ...]:
    """All exact stem n-grams with n≥min_n on H and P and Q."""
    h_lines = concat_sides(by_side, h_sides)
    p_lines = concat_sides(by_side, p_sides)
    q_lines = concat_sides(by_side, q_sides)
    max_n = min(
        max((len(sequence) for sequence in h_lines), default=0),
        max((len(sequence) for sequence in p_lines), default=0),
        max((len(sequence) for sequence in q_lines), default=0),
    )
    rows: list[TripleN8Row] = []
    for n in range(max_n, min_n - 1, -1):
        h_counts = ngram_frequencies(h_lines, n)
        p_counts = ngram_frequencies(p_lines, n)
        q_counts = ngram_frequencies(q_lines, n)
        for tokens in sorted(set(h_counts) & set(p_counts) & set(q_counts)):
            rows.append(
                TripleN8Row(
                    tokens=tokens,
                    n=n,
                    freq_h=h_counts[tokens],
                    freq_p=p_counts[tokens],
                    freq_q=q_counts[tokens],
                    hits_h=named_qhp_hits(by_side, h_sides, tokens),
                    hits_p=named_qhp_hits(by_side, p_sides, tokens),
                    hits_q=named_qhp_hits(by_side, q_sides, tokens),
                )
            )
    rows.sort(key=lambda row: (-row.n, row.tokens))
    return tuple(rows)


def expand_triple_maximals(
    maximals: tuple[tuple, ...],
    min_n: int = MIN_N,
) -> tuple[TripleN8Row, ...]:
    """All n≥min_n subspans of triple islands, with offset hit sites."""
    rows: list[TripleN8Row] = []
    for tokens, n, freq_h, freq_p, freq_q, h_site, p_site, q_site in maximals:
        h_side, h_line, h_index = h_site
        p_side, p_line, p_index = p_site
        q_side, q_line, q_index = q_site
        for length in range(n, min_n - 1, -1):
            for offset in range(n - length + 1):
                rows.append(
                    TripleN8Row(
                        tokens=tokens[offset : offset + length],
                        n=length,
                        freq_h=freq_h,
                        freq_p=freq_p,
                        freq_q=freq_q,
                        hits_h=((h_side, h_line, h_index + offset),),
                        hits_p=((p_side, p_line, p_index + offset),),
                        hits_q=((q_side, q_line, q_index + offset),),
                    )
                )
    rows.sort(key=lambda row: (-row.n, row.tokens))
    return tuple(rows)


def maximal_triple_rows(rows: tuple[TripleN8Row, ...]) -> tuple[TripleN8Row, ...]:
    """Rows that are not a contiguous subspan of a longer triple row."""
    tokens = [row.tokens for row in rows]
    kept: list[TripleN8Row] = []
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


def islands_disjoint_triple(maximals: tuple[tuple, ...]) -> bool:
    """True iff no two maximal hits share a (side, line, index) stem."""
    occupied: set[tuple[str, str, int]] = set()
    for _tokens, n, _fh, _fp, _fq, h_site, p_site, q_site in maximals:
        for side, line, start in (h_site, p_site, q_site):
            for offset in range(n):
                key = (side, line, start + offset)
                if key in occupied:
                    return False
                occupied.add(key)
    return True


class TestHpqTripleN8Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_min_n_excludes_short_and_records_hits(self):
        """n=7 share is dropped; n=8 is kept with line/index on all three."""
        provider = MockProvider()
        by_side = load_q_h_p_sides()
        by_side[SIDE_HR] = [["A", "B", "C", "D", "E", "F", "G", "H", "I"]]
        by_side[SIDE_HV] = [["X"]]
        by_side[SIDE_PR] = [["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"]]
        by_side[SIDE_PV] = [["Y"]]
        by_side[SIDE_QR] = [["W", "A", "B", "C", "D", "E", "F", "G", "H", "I"]]
        by_side[SIDE_QV] = [["V"]]
        rows = score_hpq_triple_n8(by_side, H_SIDES, P_SIDES, Q_SIDES)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0].n, 9)
        self.assertEqual(rows[0].tokens, ("A", "B", "C", "D", "E", "F", "G", "H", "I"))
        self.assertEqual(rows[0].hits_h, ((SIDE_HR, "Hr1", 0),))
        self.assertEqual(rows[0].hits_p, ((SIDE_PR, "Pr1", 1),))
        self.assertEqual(rows[0].hits_q, ((SIDE_QR, "Qr1", 1),))
        self.assertEqual(len(expand_triple_maximals(STANDING_MAXIMALS)), STANDING_DISTINCT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_coverage_unions_windows(self):
        """Overlapping 8-grams union; a private 8-gram is not coverage."""
        provider = MockProvider()
        lines = [["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
        grams = [("1", "2", "3", "4", "5", "6", "7", "8")]
        self.assertEqual(covered_stem_count(lines, grams), (8, 10))
        self.assertTrue(islands_disjoint_triple(STANDING_MAXIMALS))
        self.assertEqual(STANDING_ISLANDS_DISJOINT, True)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHpqTripleN8Scoreboard(unittest.TestCase):
    """Cited-fixture H∩P∩Q n≥8 inventory and coverage lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_q_h_p_sides()
        self.combined = score_hpq_triple_n8(self.by_side, H_SIDES, P_SIDES, Q_SIDES)
        self.expanded = expand_triple_maximals(STANDING_MAXIMALS)
        self.grams = tuple(row.tokens for row in self.combined)
        self.coverage = score_pair_coverage(self.by_side, HPQ_SIDES, self.grams)
        self.per_side = tuple(
            (
                h_side,
                p_side,
                q_side,
                score_hpq_triple_n8(self.by_side, (h_side,), (p_side,), (q_side,)),
            )
            for h_side, p_side, q_side in HPQ_SIDE_TRIPLES
        )

    def test_inventory_tokens_n_freq_and_hits(self):
        """33 distinct triple n≥8; each matches a maximal subspan with freq 1/1/1."""
        self.assertEqual(len(self.combined), STANDING_DISTINCT_COUNT)
        self.assertEqual(len(self.expanded), STANDING_DISTINCT_COUNT)
        self.assertEqual(
            tuple(triple_row_tuple(row) for row in self.combined),
            tuple(triple_row_tuple(row) for row in self.expanded),
        )
        self.assertEqual(count_by_n(self.combined), STANDING_BY_N)
        self.assertEqual(len(maximal_triple_rows(self.combined)), STANDING_MAXIMAL_COUNT)
        locked = tuple(
            (
                row.tokens,
                row.n,
                row.freq_h,
                row.freq_p,
                row.freq_q,
                row.hits_h[0],
                row.hits_p[0],
                row.hits_q[0],
            )
            for row in maximal_triple_rows(self.combined)
        )
        self.assertEqual(locked, STANDING_MAXIMALS)
        for row in self.combined:
            self.assertGreaterEqual(row.n, MIN_N)
            self.assertEqual(len(row.tokens), row.n)
            self.assertEqual((row.freq_h, row.freq_p, row.freq_q), (1, 1, 1))
            self.assertEqual(len(row.hits_h), 1)
            self.assertEqual(len(row.hits_p), 1)
            self.assertEqual(len(row.hits_q), 1)
        self.assertEqual(len({row.tokens for row in self.combined}), STANDING_DISTINCT_COUNT)
        self.assertFalse(STANDING_EMPTY)
        self.assertFalse(STANDING_TWO_SHORT_FORMULAS)
        self.assertTrue(STANDING_MULTI_ISLAND_TRADITION)
        self.assertGreater(STANDING_MAXIMAL_COUNT, 2)
        self.assertGreater(STANDING_MAXIMALS[0][1], 8)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_side_inventory_and_cross_empty(self):
        """Hr–Pr–Qr 32, Hv–Pv–Qv 1, cross-side triples none."""
        counts = tuple(
            (h_side, p_side, q_side, len(rows))
            for h_side, p_side, q_side, rows in self.per_side
        )
        self.assertEqual(counts, STANDING_PER_SIDE_COUNTS)
        hr_pr_qr = self.per_side[0][3]
        hv_pv_qv = self.per_side[7][3]
        self.assertEqual(
            tuple(triple_row_tuple(row) for row in hr_pr_qr),
            tuple(triple_row_tuple(row) for row in expand_triple_maximals(STANDING_HR_PR_QR_MAXIMALS)),
        )
        self.assertEqual(
            tuple(triple_row_tuple(row) for row in hv_pv_qv),
            tuple(triple_row_tuple(row) for row in expand_triple_maximals(STANDING_HV_PV_QV_MAXIMALS)),
        )
        for index in range(1, 7):
            self.assertEqual(self.per_side[index][3], ())
        self.assertEqual(len(hr_pr_qr) + len(hv_pv_qv), STANDING_DISTINCT_COUNT)
        self.assertTrue(islands_disjoint_triple(STANDING_MAXIMALS))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_coverage_and_tradition_claim(self):
        """Hr/Pr/Qr 41, Hv/Pv/Qv 8 (49/tablet). Multi-island, not empty or two formulas."""
        self.assertEqual(self.coverage, STANDING_COVERAGE)
        maximal_grams = tuple(row[0] for row in STANDING_MAXIMALS)
        self.assertEqual(
            score_pair_coverage(self.by_side, HPQ_SIDES, maximal_grams),
            STANDING_COVERAGE,
        )
        by_side = {side: (covered, total) for side, covered, total in self.coverage}
        self.assertEqual(by_side[SIDE_HR], (41, HP_STEM_TOTALS[SIDE_HR]))
        self.assertEqual(by_side[SIDE_HV], (8, HP_STEM_TOTALS[SIDE_HV]))
        self.assertEqual(by_side[SIDE_PR], (41, HP_STEM_TOTALS[SIDE_PR]))
        self.assertEqual(by_side[SIDE_PV], (8, HP_STEM_TOTALS[SIDE_PV]))
        self.assertEqual(by_side[SIDE_QR], (41, Q_STEM_TOTALS[SIDE_QR]))
        self.assertEqual(by_side[SIDE_QV], (8, Q_STEM_TOTALS[SIDE_QV]))
        self.assertEqual(by_side[SIDE_HR][0] + by_side[SIDE_HV][0], STANDING_COVERED_H)
        self.assertEqual(by_side[SIDE_PR][0] + by_side[SIDE_PV][0], STANDING_COVERED_P)
        self.assertEqual(by_side[SIDE_QR][0] + by_side[SIDE_QV][0], STANDING_COVERED_Q)
        self.assertEqual(STANDING_COVERED_H, STANDING_COVERED_P)
        self.assertEqual(STANDING_COVERED_P, STANDING_COVERED_Q)
        self.assertEqual(STANDING_SAME_TEXT, False)
        self.assertEqual(STANDING_EMPTY, False)
        self.assertEqual(STANDING_TWO_SHORT_FORMULAS, False)
        self.assertTrue(STANDING_MULTI_ISLAND_TRADITION)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_q_hp_shared_n8_still_computes(self):
        """Cycle 70 Q vs H/P n≥8 inventory lock stays."""
        prior = TestMamariSmallStPetersburgSharedN8Scoreboard()
        prior.setUp()
        prior.test_q_vs_h_inventory_tokens_n_freq_and_hits()
        prior.test_q_vs_p_inventory_tokens_n_freq_and_hits()
        prior.test_coverage_and_parallel_claim()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-71 H∩P∩Q n≥8 inventory."""
        lock = self.survey["tablet_h_p_q_triple_n8_inventory"]
        self.assertEqual(lock["cycle"], 71)
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
                freq_q,
                tuple(h_site),
                tuple(p_site),
                tuple(q_site),
            )
            for tokens, n, freq_h, freq_p, freq_q, h_site, p_site, q_site in lock["maximals"]
        )
        self.assertEqual(locked_maximals, STANDING_MAXIMALS)
        self.assertEqual(
            tuple((h, p, q, count) for h, p, q, count in lock["per_side_counts"]),
            STANDING_PER_SIDE_COUNTS,
        )
        self.assertEqual(
            tuple((side, covered, total) for side, covered, total in lock["coverage"]),
            STANDING_COVERAGE,
        )
        self.assertEqual(lock["covered_h"], STANDING_COVERED_H)
        self.assertEqual(lock["covered_p"], STANDING_COVERED_P)
        self.assertEqual(lock["covered_q"], STANDING_COVERED_Q)
        self.assertEqual(lock["empty"], STANDING_EMPTY)
        self.assertEqual(lock["two_short_formulas"], STANDING_TWO_SHORT_FORMULAS)
        self.assertEqual(lock["multi_island_tradition"], STANDING_MULTI_ISLAND_TRADITION)
        self.assertEqual(lock["same_text"], STANDING_SAME_TEXT)
        self.assertEqual(lock["islands_disjoint"], STANDING_ISLANDS_DISJOINT)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_hp_shared_n8_unchanged"])
        self.assertTrue(lock["standing_q_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_q_shared_n8_inventory"]["cycle"], 70)
        self.assertEqual(self.survey["tablet_h_p_shared_n8_inventory"]["cycle"], 69)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHpqTripleN8ImageSnapshot(unittest.TestCase):
    """Cycle 71 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
