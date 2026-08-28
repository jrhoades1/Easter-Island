"""G–K same-side inter-island gaps on existing G/K fixtures.

Cycle 75 text-search lock. Uses already-vendored Gr/Kr/Kv, the
cycle-67 six maximal n≥8 islands, and their already-known
line/index sites (Gr line/index order). Does not scrape a new
tablet. Raw stems. No invented Barthel. No G00n→Barthel map.
No type merge. No detector retune. No CV. No new agents. Not a
meaning dictionary. Does not retune the G–K reading-order claim.

Comparable gaps are same-side only: Gr–Kr after islands 1→2,
2→3, 3→4; Gr–Kv after islands 5→6. The Gr-only stretch between
islands 4 and 5 is a documented Kr→Kv side-switch, not a
comparable gap. Gv stays 0.

For each comparable gap lock intervening stem counts, the
longest exact shared n-gram, whether that n is ≥8, and whether
the full gap strings match.

Claim that can lose: the gaps are also shared (copied pages)
vs only the islands match (waypoints). Operationalized as
cycle 74: copied_pages iff any comparable gap has shared n≥8.

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import re
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_hpq_island_recto_gap_scoreboard import (
    TestMamariHpqIslandRectoGapScoreboard,
    longest_shared_ngram,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_island_off_gk_scoreboard import (
    TestMamariSmallSantiagoLondonIslandOffGkScoreboard,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    G_SIDES,
    K_SIDES,
    SIDE_GR,
    SIDE_GV,
    SIDE_KR,
    SIDE_KV,
    load_g_k_sides,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    GRAM_10_KR,
    GRAM_10_KV,
    GRAM_12,
    GRAM_13,
    LINE_NAMES,
    STANDING_GR_KR_MAXIMALS,
    STANDING_GR_KV_MAXIMALS,
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    STANDING_NEW_TABLET,
    SharedN8Row,
    maximal_rows,
    score_shared_n8,
)
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import GRAM_17
from tests.test_mamari_small_santiago_london_gr_kv_15gram_scoreboard import GRAM_15

MIN_SHARED_N8 = 8
STANDING_GR_COUNT = 6
STANDING_KR_COUNT = 4
STANDING_KV_COUNT = 2
STANDING_GV_COUNT = 0
STANDING_GR_ORDER = (
    (GRAM_12, 12, (SIDE_GR, "Gr1", 4)),
    (GRAM_13, 13, (SIDE_GR, "Gr2", 4)),
    (GRAM_10_KR, 10, (SIDE_GR, "Gr3", 28)),
    (GRAM_17, 17, (SIDE_GR, "Gr4", 3)),
    (GRAM_10_KV, 10, (SIDE_GR, "Gr6", 33)),
    (GRAM_15, 15, (SIDE_GR, "Gr7", 0)),
)
STANDING_KR_ORDER = (
    (GRAM_12, 12, (SIDE_KR, "Kr1", 2)),
    (GRAM_13, 13, (SIDE_KR, "Kr2", 16)),
    (GRAM_10_KR, 10, (SIDE_KR, "Kr4", 12)),
    (GRAM_17, 17, (SIDE_KR, "Kr5", 0)),
)
STANDING_KV_ORDER = (
    (GRAM_10_KV, 10, (SIDE_KV, "Kv3", 15)),
    (GRAM_15, 15, (SIDE_KV, "Kv4", 7)),
)
STANDING_GAP_COUNT = 4
STANDING_GAP_ISLANDS = ((1, 2), (2, 3), (3, 4), (5, 6))
STANDING_GAP_PAIRS = (("Gr", "Kr"), ("Gr", "Kr"), ("Gr", "Kr"), ("Gr", "Kv"))
STANDING_GAPS = (
    (28, 28, 4, ("022", "062", "001", "099"), False),
    (51, 41, 7, ("470", "001", "430", "580", "380", "001", "003"), False),
    (5, 2, 0, (), False),
    (11, 11, 10, ("380", "001", "003", "003", "003", "004", "215", "380", "001", "003"), False),
)
STANDING_SIDE_SWITCH_AFTER = 4
STANDING_SIDE_SWITCH_BEFORE = 5
STANDING_SIDE_SWITCH_LEN_GR = 102
STANDING_SIDE_SWITCH_COMPARABLE = False
STANDING_ANY_SHARED_N_GE_8 = True
STANDING_ANY_FULL_MATCH = False
STANDING_COPIED_PAGES = True
STANDING_WAYPOINTS = False
STANDING_GV_IN_GAPS = False
STANDING_TABLET_D_SCRAPED = False
STANDING_RESULT = "gk_island_gaps"


@dataclass(frozen=True)
class GapRow:
    """One same-side inter-island gap: lengths + longest shared n. Ids only."""

    after: int
    before: int
    pair: tuple[str, str]
    len_g: int
    len_k: int
    shared_n: int
    shared_tokens: tuple[str, ...]
    full_match: bool
    n_ge_8: bool

    def lock_tuple(self) -> tuple:
        """Stable 4-gap table row."""
        return (
            self.len_g,
            self.len_k,
            self.shared_n,
            self.shared_tokens,
            self.full_match,
        )


def line_then_index(site: tuple[str, str, int]) -> tuple[int, int]:
    """(line number, index) from a (side, line_name, index) site."""
    _side, line_name, index = site
    match = re.search(r"(\d+)$", line_name)
    if match is None:
        raise ValueError(f"no line number in {line_name!r}")
    return (int(match.group(1)), index)


def island_from_shared_row(row: SharedN8Row) -> tuple:
    """(tokens, n, g_site, k_site) from a scored maximal row."""
    return (row.tokens, row.n, row.hits_g[0], row.hits_k[0])


def island_from_maximal(row: tuple) -> tuple:
    """Unpack a cycle-67 maximal tuple to (tokens, n, g_site, k_site)."""
    tokens, n, _freq_g, _freq_k, g_site, k_site = row
    return (tokens, n, g_site, k_site)


def split_kr_kv(
    islands: tuple[tuple, ...],
) -> tuple[tuple[tuple, ...], tuple[tuple, ...]]:
    """Kr-sided and Kv-sided partitions. No mixing."""
    kr = tuple(island for island in islands if island[3][0] == SIDE_KR)
    kv = tuple(island for island in islands if island[3][0] == SIDE_KV)
    return kr, kv


def order_on(
    islands: tuple[tuple, ...],
    site_index: int,
) -> tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...]:
    """Sort islands by line then index of that tablet's site."""
    sorted_islands = sorted(
        islands, key=lambda island: line_then_index(island[site_index])
    )
    return tuple(
        (island[0], island[1], island[site_index]) for island in sorted_islands
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


def score_same_side_gaps(
    by_side: dict[str, list[list[str]]],
    gr_order: tuple = STANDING_GR_ORDER,
    kr_order: tuple = STANDING_KR_ORDER,
    kv_order: tuple = STANDING_KV_ORDER,
) -> tuple[GapRow, ...]:
    """Four same-side gaps. Side-switch 4→5 is not a row."""
    pairs = (
        (1, 2, ("Gr", "Kr"), gr_order[0], gr_order[1], kr_order[0], kr_order[1]),
        (2, 3, ("Gr", "Kr"), gr_order[1], gr_order[2], kr_order[1], kr_order[2]),
        (3, 4, ("Gr", "Kr"), gr_order[2], gr_order[3], kr_order[2], kr_order[3]),
        (5, 6, ("Gr", "Kv"), gr_order[4], gr_order[5], kv_order[0], kv_order[1]),
    )
    rows: list[GapRow] = []
    for after, before, pair, left_g, right_g, left_k, right_k in pairs:
        stems_g = intervening_stems(by_side, left_g, right_g)
        stems_k = intervening_stems(by_side, left_k, right_k)
        shared_n, shared_tokens = longest_shared_ngram(stems_g, stems_k)
        rows.append(
            GapRow(
                after=after,
                before=before,
                pair=pair,
                len_g=len(stems_g),
                len_k=len(stems_k),
                shared_n=shared_n,
                shared_tokens=shared_tokens,
                full_match=stems_g == stems_k,
                n_ge_8=shared_n >= MIN_SHARED_N8,
            )
        )
    return tuple(rows)


def side_switch_len_gr(
    by_side: dict[str, list[list[str]]],
    gr_order: tuple = STANDING_GR_ORDER,
) -> int:
    """Gr-only stem count between islands 4 and 5. Not a comparable gap."""
    return len(intervening_stems(by_side, gr_order[3], gr_order[4]))


def any_shared_n_ge_8(rows: tuple[GapRow, ...]) -> bool:
    """True iff any comparable gap shares an n≥8."""
    return any(row.n_ge_8 for row in rows)


def any_full_match(rows: tuple[GapRow, ...]) -> bool:
    """True iff any comparable gap's two strings are identical."""
    return any(row.full_match for row in rows)


def copied_pages(rows: tuple[GapRow, ...]) -> bool:
    """True iff any comparable gap has shared n≥8. Same as cycle 74."""
    return any_shared_n_ge_8(rows)


def waypoints(rows: tuple[GapRow, ...]) -> bool:
    """True iff no comparable gap has shared n≥8."""
    return not copied_pages(rows)


class TestSmallSantiagoLondonIslandGapHelpers(unittest.TestCase):
    """Helpers on synthetic sites. No CV, no LLM."""

    def test_intervening_stems_same_line_and_across_lines(self):
        """Gap is exclusive of both islands; empty when they abut."""
        provider = MockProvider()
        by_side = {
            SIDE_GR: [
                ["A", "B", "C", "D", "E", "F"],
                ["G", "H", "I", "J"],
            ],
        }
        left = (("A", "B"), 2, (SIDE_GR, "Gr1", 0))
        right = (("E", "F"), 2, (SIDE_GR, "Gr1", 4))
        self.assertEqual(intervening_stems(by_side, left, right), ["C", "D"])
        abut = (("C", "D"), 2, (SIDE_GR, "Gr1", 2))
        self.assertEqual(intervening_stems(by_side, left, abut), [])
        cross_right = (("I", "J"), 2, (SIDE_GR, "Gr2", 2))
        self.assertEqual(
            intervening_stems(by_side, left, cross_right),
            ["C", "D", "E", "F", "G", "H"],
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_share_full_match_and_n8_claim(self):
        """Pairwise n, full-match, and the copied-pages / waypoints poles."""
        provider = MockProvider()
        shared = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        n, tokens = longest_shared_ngram(shared, shared)
        self.assertEqual(n, 9)
        self.assertEqual(tokens, tuple(shared))
        self.assertTrue(shared == list(shared))
        left = ["A", "B", "C", "D", "E", "F", "G", "H"]
        right = ["A", "B", "C", "D", "E", "F", "G", "X"]
        n, tokens = longest_shared_ngram(left, right)
        self.assertEqual(n, 7)
        self.assertEqual(tokens, ("A", "B", "C", "D", "E", "F", "G"))
        self.assertFalse(left == right)
        empty = longest_shared_ngram(["1", "2"], ["9", "8"])
        self.assertEqual(empty, (0, ()))
        planted = (
            GapRow(1, 2, ("Gr", "Kr"), 8, 8, 4, ("A", "B", "C", "D"), False, False),
            GapRow(5, 6, ("Gr", "Kv"), 11, 11, 10, tuple(shared[:10]), False, True),
        )
        self.assertTrue(any_shared_n_ge_8(planted))
        self.assertFalse(any_full_match(planted))
        self.assertTrue(copied_pages(planted))
        self.assertFalse(waypoints(planted))
        none = (
            GapRow(1, 2, ("Gr", "Kr"), 8, 8, 4, ("A", "B", "C", "D"), False, False),
        )
        self.assertFalse(any_shared_n_ge_8(none))
        self.assertFalse(copied_pages(none))
        self.assertTrue(waypoints(none))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonIslandGapScoreboard(unittest.TestCase):
    """Cited-fixture G–K same-side inter-island gap lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_g_k_sides()
        self.combined = score_shared_n8(self.by_side, G_SIDES, K_SIDES)
        self.maximals = tuple(
            island_from_shared_row(row) for row in maximal_rows(self.combined)
        )
        self.standing = tuple(island_from_maximal(row) for row in STANDING_MAXIMALS)
        self.kr, self.kv = split_kr_kv(self.maximals)
        self.gr_order = order_on(self.maximals, 2)
        self.kr_order = order_on(self.kr, 3)
        self.kv_order = order_on(self.kv, 3)
        self.gaps = score_same_side_gaps(
            self.by_side, self.gr_order, self.kr_order, self.kv_order
        )
        self.switch_len = side_switch_len_gr(self.by_side, self.gr_order)

    def test_four_gap_table_lengths_and_longest_shared_n(self):
        """Four same-side gaps: stem counts + longest shared n. One n≥8."""
        self.assertEqual(self.maximals, self.standing)
        self.assertEqual(self.gr_order, STANDING_GR_ORDER)
        self.assertEqual(self.kr_order, STANDING_KR_ORDER)
        self.assertEqual(self.kv_order, STANDING_KV_ORDER)
        self.assertEqual(len(self.gr_order), STANDING_GR_COUNT)
        self.assertEqual(len(self.kr_order), STANDING_KR_COUNT)
        self.assertEqual(len(self.kv_order), STANDING_KV_COUNT)
        self.assertEqual(len(self.kr) + len(self.kv), STANDING_MAXIMAL_COUNT)
        self.assertEqual(len(STANDING_GR_KR_MAXIMALS), STANDING_KR_COUNT)
        self.assertEqual(len(STANDING_GR_KV_MAXIMALS), STANDING_KV_COUNT)
        self.assertEqual(len(self.gaps), STANDING_GAP_COUNT)
        locked = tuple(row.lock_tuple() for row in self.gaps)
        self.assertEqual(locked, STANDING_GAPS)
        self.assertEqual(tuple((row.after, row.before) for row in self.gaps), STANDING_GAP_ISLANDS)
        self.assertEqual(tuple(row.pair for row in self.gaps), STANDING_GAP_PAIRS)
        for row, standing in zip(self.gaps, STANDING_GAPS):
            self.assertEqual(row.lock_tuple(), standing)
            self.assertEqual(row.len_g, standing[0])
            self.assertEqual(row.len_k, standing[1])
            self.assertEqual(row.shared_n, standing[2])
            self.assertEqual(row.shared_tokens, standing[3])
            self.assertEqual(row.full_match, standing[4])
            self.assertEqual(row.n_ge_8, row.shared_n >= MIN_SHARED_N8)
            self.assertEqual(row.full_match, False)
        self.assertEqual(any_shared_n_ge_8(self.gaps), STANDING_ANY_SHARED_N_GE_8)
        self.assertEqual(any_full_match(self.gaps), STANDING_ANY_FULL_MATCH)
        self.assertEqual(copied_pages(self.gaps), STANDING_COPIED_PAGES)
        self.assertEqual(waypoints(self.gaps), STANDING_WAYPOINTS)
        self.assertTrue(STANDING_ANY_SHARED_N_GE_8)
        self.assertFalse(STANDING_ANY_FULL_MATCH)
        self.assertTrue(STANDING_COPIED_PAGES)
        self.assertFalse(STANDING_WAYPOINTS)
        self.assertEqual(self.gaps[0].n_ge_8, False)
        self.assertEqual(self.gaps[1].n_ge_8, False)
        self.assertEqual(self.gaps[2].n_ge_8, False)
        self.assertEqual(self.gaps[3].n_ge_8, True)
        self.assertEqual(self.switch_len, STANDING_SIDE_SWITCH_LEN_GR)
        self.assertFalse(STANDING_SIDE_SWITCH_COMPARABLE)
        self.assertEqual(
            (STANDING_SIDE_SWITCH_AFTER, STANDING_SIDE_SWITCH_BEFORE),
            (4, 5),
        )
        self.assertNotIn((4, 5), STANDING_GAP_ISLANDS)
        for island in self.maximals:
            self.assertEqual(island[2][0], SIDE_GR)
            self.assertNotEqual(island[2][0], SIDE_GV)
        self.assertEqual(STANDING_GV_COUNT, 0)
        self.assertFalse(STANDING_GV_IN_GAPS)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        tokens_at = []
        for tokens, n, (side, line, index) in (
            *self.gr_order,
            *self.kr_order,
            *self.kv_order,
        ):
            names = LINE_NAMES[side]
            got = tuple(self.by_side[side][names.index(line)][index : index + n])
            tokens_at.append(got == tokens)
        self.assertTrue(all(tokens_at))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_island_off_gk_scoreboard_still_computes(self):
        """Cycle 68 off-G/K island-absent lock stays."""
        prior = TestMamariSmallSantiagoLondonIslandOffGkScoreboard()
        prior.setUp()
        prior.test_six_by_eight_hit_table()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_hpq_island_recto_gap_scoreboard_still_computes(self):
        """Cycle 74 H/P/Q recto-gap lock stays."""
        prior = TestMamariHpqIslandRectoGapScoreboard()
        prior.setUp()
        prior.test_three_gap_table_lengths_and_longest_shared_n()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-75 4-gap table."""
        lock = self.survey["tablet_g_k_island_gaps"]
        self.assertEqual(lock["cycle"], 75)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["gap_count"], STANDING_GAP_COUNT)
        locked = tuple(
            (
                len_g,
                len_k,
                shared_n,
                tuple(shared_tokens),
                full_match,
            )
            for len_g, len_k, shared_n, shared_tokens, full_match in lock["gaps"]
        )
        self.assertEqual(locked, STANDING_GAPS)
        self.assertEqual(
            tuple((after, before) for after, before in lock["gap_islands"]),
            STANDING_GAP_ISLANDS,
        )
        self.assertEqual(
            tuple(tuple(pair) for pair in lock["gap_pairs"]),
            STANDING_GAP_PAIRS,
        )
        self.assertEqual(lock["any_shared_n_ge_8"], STANDING_ANY_SHARED_N_GE_8)
        self.assertTrue(lock["any_shared_n_ge_8"])
        self.assertEqual(lock["any_full_match"], STANDING_ANY_FULL_MATCH)
        self.assertFalse(lock["any_full_match"])
        self.assertEqual(lock["copied_pages"], STANDING_COPIED_PAGES)
        self.assertTrue(lock["copied_pages"])
        self.assertEqual(lock["waypoints"], STANDING_WAYPOINTS)
        self.assertFalse(lock["waypoints"])
        switch = lock["side_switch"]
        self.assertEqual(switch["after"], STANDING_SIDE_SWITCH_AFTER)
        self.assertEqual(switch["before"], STANDING_SIDE_SWITCH_BEFORE)
        self.assertEqual(switch["len_gr"], STANDING_SIDE_SWITCH_LEN_GR)
        self.assertEqual(switch["comparable"], STANDING_SIDE_SWITCH_COMPARABLE)
        self.assertFalse(switch["comparable"])
        self.assertEqual(lock["gv_in_gaps"], STANDING_GV_IN_GAPS)
        self.assertFalse(lock["gv_in_gaps"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertTrue(lock["standing_hpq_island_recto_order_unchanged"])
        self.assertTrue(lock["standing_hpq_island_recto_gaps_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_island_off_gk_hits"]["cycle"], 68)
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["cycle"], 67)
        self.assertEqual(self.survey["tablet_h_p_q_island_recto_gaps"]["cycle"], 74)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonIslandGapImageSnapshot(unittest.TestCase):
    """Cycle 75 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
