"""H∩P∩Q recto inter-island gaps on existing H/P/Q fixtures.

Cycle 74 text-search lock. Uses already-vendored Hr/Pr/Qr, the
cycle-73 four-island recto order, and the existing parsers.
Existing line/index sites only. Does not scrape a new tablet.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary. Verso island stays out.

For each of the three gaps (after island 1 to before 2; after 2
to before 3; after 3 to before 4), take the intervening stem
sequence on Hr, Pr, and Qr. Lock gap length (stem count) on each
tablet, the longest exact shared n-gram among the three gap
strings (pairwise H–P / H–Q / P–Q if the triple is empty), and
whether any gap has a triple-shared n≥8.

Claim that can lose: the gaps are also shared (copied pages) vs
only the islands match (waypoints).

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_hpq_island_recto_order_scoreboard import (
    STANDING_HR_ORDER,
    STANDING_PR_ORDER,
    STANDING_QR_ORDER,
    STANDING_RECTO_COUNT,
    STANDING_TOKEN_ORDER,
    TestMamariHpqIslandRectoOrderScoreboard,
    island_from_triple_row,
    order_on,
    split_recto_verso,
)
from tests.test_mamari_hpq_triple_n8_scoreboard import (
    load_q_h_p_sides,
    maximal_triple_rows,
    score_hpq_triple_n8,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
    P_SIDES,
    SIDE_HR,
    SIDE_PR,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    ngram_frequencies,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import LINE_NAMES
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    Q_SIDES,
    SIDE_QR,
)

MIN_TRIPLE_N8 = 8
STANDING_GAP_COUNT = 3
STANDING_GAPS = (
    (164, 184, 123, 7, ("003", "027", "003", "086", "003", "060", "003"), 22, 31, 7),
    (158, 178, 122, 7, ("430", "214", "002", "203", "027", "090", "545"), 11, 13, 7),
    (10, 11, 11, 2, ("095", "003"), 2, 2, 3),
)
STANDING_ANY_TRIPLE_N_GE_8 = False
STANDING_COPIED_PAGES = False
STANDING_WAYPOINTS = True
STANDING_VERSO_IN_GAPS = False
STANDING_NEW_TABLET = False
STANDING_TABLET_D_SCRAPED = False
STANDING_RESULT = "hpq_island_recto_gaps"


@dataclass(frozen=True)
class GapRow:
    """One inter-island gap: lengths + longest shared n. Ids only."""

    after: int
    before: int
    len_h: int
    len_p: int
    len_q: int
    shared_n: int
    shared_tokens: tuple[str, ...]
    hp_n: int
    hq_n: int
    pq_n: int
    triple_n_ge_8: bool

    def lock_tuple(self) -> tuple:
        """Stable 3-gap table row."""
        return (
            self.len_h,
            self.len_p,
            self.len_q,
            self.shared_n,
            self.shared_tokens,
            self.hp_n,
            self.hq_n,
            self.pq_n,
        )


def intervening_stems(
    by_side: dict[str, list[list[str]]],
    left: tuple[tuple[str, ...], int, tuple[str, str, int]],
    right: tuple[tuple[str, ...], int, tuple[str, str, int]],
) -> list[str]:
    """Stem sequence after the left island and before the right island."""
    _tokens, n, (side, start_line, start_index) = left
    _rt, _rn, (_rs, end_line, end_index) = right
    lines = by_side[side]
    names = LINE_NAMES[side]
    start_li = names.index(start_line)
    end_li = names.index(end_line)
    first = start_index + n
    if start_li == end_li:
        return list(lines[start_li][first:end_index])
    stems = list(lines[start_li][first:])
    for line_index in range(start_li + 1, end_li):
        stems.extend(lines[line_index])
    stems.extend(lines[end_li][:end_index])
    return stems


def longest_shared_ngram(*sequences: list[str]) -> tuple[int, tuple[str, ...]]:
    """Longest exact shared n-gram. Ties break by lex-smallest tokens."""
    if not sequences:
        return (0, ())
    max_n = min((len(sequence) for sequence in sequences), default=0)
    for n in range(max_n, 0, -1):
        common = set.intersection(
            *(set(ngram_frequencies([sequence], n)) for sequence in sequences)
        )
        if common:
            return (n, min(common))
    return (0, ())


def share_for_gaps(
    stems_h: list[str],
    stems_p: list[str],
    stems_q: list[str],
) -> tuple[int, tuple[str, ...], int, int, int]:
    """Triple longest n, or pairwise ns when the triple is empty."""
    shared_n, shared_tokens = longest_shared_ngram(stems_h, stems_p, stems_q)
    hp_n, _hp = longest_shared_ngram(stems_h, stems_p)
    hq_n, _hq = longest_shared_ngram(stems_h, stems_q)
    pq_n, _pq = longest_shared_ngram(stems_p, stems_q)
    return (shared_n, shared_tokens, hp_n, hq_n, pq_n)


def score_recto_gaps(
    by_side: dict[str, list[list[str]]],
    hr_order: tuple = STANDING_HR_ORDER,
    pr_order: tuple = STANDING_PR_ORDER,
    qr_order: tuple = STANDING_QR_ORDER,
) -> tuple[GapRow, ...]:
    """Three inter-island gaps on Hr / Pr / Qr. Verso is not a gap."""
    rows: list[GapRow] = []
    for index in range(len(hr_order) - 1):
        stems_h = intervening_stems(by_side, hr_order[index], hr_order[index + 1])
        stems_p = intervening_stems(by_side, pr_order[index], pr_order[index + 1])
        stems_q = intervening_stems(by_side, qr_order[index], qr_order[index + 1])
        shared_n, shared_tokens, hp_n, hq_n, pq_n = share_for_gaps(
            stems_h, stems_p, stems_q
        )
        rows.append(
            GapRow(
                after=index + 1,
                before=index + 2,
                len_h=len(stems_h),
                len_p=len(stems_p),
                len_q=len(stems_q),
                shared_n=shared_n,
                shared_tokens=shared_tokens,
                hp_n=hp_n,
                hq_n=hq_n,
                pq_n=pq_n,
                triple_n_ge_8=shared_n >= MIN_TRIPLE_N8,
            )
        )
    return tuple(rows)


def any_triple_n_ge_8(rows: tuple[GapRow, ...]) -> bool:
    """True iff any gap's three strings share an n≥8."""
    return any(row.triple_n_ge_8 for row in rows)


class TestHpqIslandRectoGapHelpers(unittest.TestCase):
    """Helpers on synthetic sites. No CV, no LLM."""

    def test_intervening_stems_same_line_and_across_lines(self):
        """Gap is exclusive of both islands; empty when they abut."""
        provider = MockProvider()
        by_side = {
            SIDE_HR: [
                ["A", "B", "C", "D", "E", "F"],
                ["G", "H", "I", "J"],
            ],
        }
        left = (("A", "B"), 2, (SIDE_HR, "Hr1", 0))
        right = (("E", "F"), 2, (SIDE_HR, "Hr1", 4))
        self.assertEqual(intervening_stems(by_side, left, right), ["C", "D"])
        abut = (("C", "D"), 2, (SIDE_HR, "Hr1", 2))
        self.assertEqual(intervening_stems(by_side, left, abut), [])
        cross_right = (("I", "J"), 2, (SIDE_HR, "Hr2", 2))
        self.assertEqual(
            intervening_stems(by_side, left, cross_right),
            ["C", "D", "E", "F", "G", "H"],
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_triple_share_or_pairwise_fallback(self):
        """Triple wins when present; pairwise ns remain when it is empty."""
        provider = MockProvider()
        shared = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        n, tokens, hp_n, hq_n, pq_n = share_for_gaps(shared, shared, shared)
        self.assertEqual(n, 9)
        self.assertEqual(tokens, tuple(shared))
        self.assertEqual((hp_n, hq_n, pq_n), (9, 9, 9))
        h = ["A", "B", "C", "D", "E", "F", "G", "H"]
        p = ["A", "B", "C", "D", "E", "F", "G", "X"]
        q = ["Z", "Z", "Z", "Z", "Z", "Z", "Z", "Y"]
        n, tokens, hp_n, hq_n, pq_n = share_for_gaps(h, p, q)
        self.assertEqual(n, 0)
        self.assertEqual(tokens, ())
        self.assertEqual(hp_n, 7)
        self.assertEqual(hq_n, 0)
        self.assertEqual(pq_n, 0)
        self.assertFalse(any_triple_n_ge_8(()))
        planted = (
            GapRow(1, 2, 8, 8, 8, 9, tuple(shared), 9, 9, 9, True),
            GapRow(2, 3, 3, 3, 3, 2, ("095", "003"), 2, 2, 2, False),
        )
        self.assertTrue(any_triple_n_ge_8(planted))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHpqIslandRectoGapScoreboard(unittest.TestCase):
    """Cited-fixture H/P/Q recto inter-island gap lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_q_h_p_sides()
        self.combined = score_hpq_triple_n8(self.by_side, H_SIDES, P_SIDES, Q_SIDES)
        self.maximals = tuple(
            island_from_triple_row(row)
            for row in maximal_triple_rows(self.combined)
        )
        self.recto, self.verso = split_recto_verso(self.maximals)
        self.hr_order = order_on(self.recto, "h")
        self.pr_order = order_on(self.recto, "p")
        self.qr_order = order_on(self.recto, "q")
        self.gaps = score_recto_gaps(
            self.by_side, self.hr_order, self.pr_order, self.qr_order
        )

    def test_three_gap_table_lengths_and_longest_shared_n(self):
        """Three gaps: stem counts + longest shared n. No triple n≥8."""
        self.assertEqual(self.hr_order, STANDING_HR_ORDER)
        self.assertEqual(self.pr_order, STANDING_PR_ORDER)
        self.assertEqual(self.qr_order, STANDING_QR_ORDER)
        self.assertEqual(token_order_len(), STANDING_RECTO_COUNT)
        self.assertEqual(len(self.gaps), STANDING_GAP_COUNT)
        self.assertEqual(len(self.gaps), STANDING_RECTO_COUNT - 1)
        locked = tuple(row.lock_tuple() for row in self.gaps)
        self.assertEqual(locked, STANDING_GAPS)
        for row, standing in zip(self.gaps, STANDING_GAPS):
            self.assertEqual(row.lock_tuple(), standing)
            self.assertEqual(row.len_h, standing[0])
            self.assertEqual(row.len_p, standing[1])
            self.assertEqual(row.len_q, standing[2])
            self.assertEqual(row.shared_n, standing[3])
            self.assertEqual(row.shared_tokens, standing[4])
            self.assertEqual((row.hp_n, row.hq_n, row.pq_n), standing[5:])
            self.assertEqual(row.triple_n_ge_8, row.shared_n >= MIN_TRIPLE_N8)
            self.assertLess(row.shared_n, MIN_TRIPLE_N8)
        self.assertEqual(any_triple_n_ge_8(self.gaps), STANDING_ANY_TRIPLE_N_GE_8)
        self.assertFalse(STANDING_ANY_TRIPLE_N_GE_8)
        self.assertFalse(STANDING_COPIED_PAGES)
        self.assertTrue(STANDING_WAYPOINTS)
        self.assertFalse(STANDING_VERSO_IN_GAPS)
        self.assertEqual(len(self.verso), 1)
        for row in self.gaps:
            self.assertEqual(row.after + 1, row.before)
        self.assertEqual(tuple(row.after for row in self.gaps), (1, 2, 3))
        self.assertEqual(self.hr_order[0][2][0], SIDE_HR)
        self.assertEqual(self.pr_order[0][2][0], SIDE_PR)
        self.assertEqual(self.qr_order[0][2][0], SIDE_QR)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_hpq_island_recto_order_scoreboard_still_computes(self):
        """Cycle 73 recto-island reading-order lock stays."""
        prior = TestMamariHpqIslandRectoOrderScoreboard()
        prior.setUp()
        prior.test_recto_orders_match_and_verso_is_separate()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-74 3-gap table."""
        lock = self.survey["tablet_h_p_q_island_recto_gaps"]
        self.assertEqual(lock["cycle"], 74)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["gap_count"], STANDING_GAP_COUNT)
        locked = tuple(
            (
                len_h,
                len_p,
                len_q,
                shared_n,
                tuple(shared_tokens),
                hp_n,
                hq_n,
                pq_n,
            )
            for len_h, len_p, len_q, shared_n, shared_tokens, hp_n, hq_n, pq_n in lock["gaps"]
        )
        self.assertEqual(locked, STANDING_GAPS)
        self.assertEqual(lock["any_triple_n_ge_8"], STANDING_ANY_TRIPLE_N_GE_8)
        self.assertFalse(lock["any_triple_n_ge_8"])
        self.assertEqual(lock["copied_pages"], STANDING_COPIED_PAGES)
        self.assertFalse(lock["copied_pages"])
        self.assertEqual(lock["waypoints"], STANDING_WAYPOINTS)
        self.assertTrue(lock["waypoints"])
        self.assertEqual(lock["verso_in_gaps"], STANDING_VERSO_IN_GAPS)
        self.assertFalse(lock["verso_in_gaps"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_hpq_island_recto_order_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hp_shared_n8_unchanged"])
        self.assertTrue(lock["standing_q_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_h_p_q_island_recto_order"]["cycle"], 73)
        self.assertEqual(self.survey["tablet_h_p_q_island_off_hpq_hits"]["cycle"], 72)
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


def token_order_len() -> int:
    """Recto island count from the cycle-73 token order."""
    return len(STANDING_TOKEN_ORDER)


class TestMamariHpqIslandRectoGapImageSnapshot(unittest.TestCase):
    """Cycle 74 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
