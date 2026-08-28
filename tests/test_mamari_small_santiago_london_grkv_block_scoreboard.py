"""Gr–Kv islands 5 + gap + 6: one block vs two islands plus filler.

Cycle 76 text-search lock. Uses already-vendored Gr.html and Kv.html,
the cycle-67/74 island-5 and island-6 sites, and the cycle-75
Gr–Kv 5→6 gap 10-gram. Does not scrape a new tablet. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning dictionary.

Measure the stem window from island 5 start through island 6 end
on Gr and on Kv. Lock lengths, whether the cycle-75 10-gram sits
immediately after island 5 and immediately before island 6 (no
extra stems), Hamming / exact match of those windows, whether
the combined 5+gap+6 string is itself a shared n≥8, and whether
that combined string is one maximal run.

Claim that can lose: the span is one contiguous shared passage
(one_block) vs two separate islands with shared filler
(two_islands_plus_filler).

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_hpq_island_recto_gap_scoreboard import longest_shared_ngram
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_17gram_hamming_scoreboard import (
    hamming_distance,
)
from tests.test_mamari_small_santiago_london_gr_kv_15gram_scoreboard import GRAM_15
from tests.test_mamari_small_santiago_london_island_gap_scoreboard import (
    STANDING_GAPS,
    STANDING_GR_ORDER,
    STANDING_KV_ORDER,
    TestMamariSmallSantiagoLondonIslandGapScoreboard,
    intervening_stems,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    SIDE_KR,
    SIDE_KV,
    load_g_k_sides,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    GRAM_10_KV,
    LINE_NAMES,
    STANDING_NEW_TABLET,
    maximal_rows,
    score_shared_n8,
)

MIN_SHARED_N8 = 8
ISLAND_5_GR = STANDING_GR_ORDER[4]
ISLAND_6_GR = STANDING_GR_ORDER[5]
ISLAND_5_KV = STANDING_KV_ORDER[0]
ISLAND_6_KV = STANDING_KV_ORDER[1]
STANDING_GAP_10GRAM = STANDING_GAPS[3][3]
STANDING_WINDOW_GR = (
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
    "066",
    "380",
    "001",
    "003",
    "003",
    "003",
    "004",
    "215",
    "380",
    "001",
    "003",
    "079",
    "450",
    "019",
    "069",
    "380",
    "001",
    "003",
    "162",
    "522",
    "050",
    "002",
    "450",
    "380",
    "001",
    "003",
)
STANDING_WINDOW_KV = (
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
    "009",
    "380",
    "001",
    "003",
    "003",
    "003",
    "004",
    "215",
    "380",
    "001",
    "003",
    "079",
    "450",
    "019",
    "069",
    "380",
    "001",
    "003",
    "162",
    "522",
    "050",
    "002",
    "450",
    "380",
    "001",
    "003",
)
STANDING_LEN_GR = 36
STANDING_LEN_KV = 36
STANDING_HAMMING = 1
STANDING_EXACT_MATCH = False
STANDING_MISMATCH = (10, "066", "009")
STANDING_IMMEDIATELY_AFTER_ISLAND_5 = False
STANDING_IMMEDIATELY_BEFORE_ISLAND_6 = True
STANDING_COMBINED_SHARED_N = 25
STANDING_COMBINED_SHARED_TOKENS = STANDING_GAP_10GRAM + GRAM_15
STANDING_COMBINED_SHARED_N_GE_8 = True
STANDING_COMBINED_IS_ONE_MAXIMAL = False
STANDING_FLATTENED_MAXIMAL_COUNT = 2
STANDING_FLATTENED_MAXIMAL_NS = (25, 10)
STANDING_ONE_BLOCK = False
STANDING_TWO_ISLANDS_PLUS_FILLER = True
STANDING_TABLET_D_SCRAPED = False
STANDING_RESULT = "gk_grkv_block"


@dataclass(frozen=True)
class GrKvBlock:
    """Island-5-through-6 windows on Gr and Kv. Ids only."""

    window_gr: tuple[str, ...]
    window_kv: tuple[str, ...]
    len_gr: int
    len_kv: int
    hamming: int
    exact_match: bool
    immediately_after_island_5: bool
    immediately_before_island_6: bool
    combined_shared_n: int
    combined_shared_tokens: tuple[str, ...]
    combined_shared_n_ge_8: bool
    combined_is_one_maximal: bool
    flattened_maximal_ns: tuple[int, ...]
    one_block: bool
    two_islands_plus_filler: bool


def span_stems(
    by_side: dict[str, list[list[str]]],
    left: tuple[tuple[str, ...], int, tuple[str, str, int]],
    right: tuple[tuple[str, ...], int, tuple[str, str, int]],
) -> list[str]:
    """Stem sequence from left-island start through right-island end."""
    _tokens, _n, (side, start_line, start_index) = left
    _rt, rn, (_rs, end_line, end_index) = right
    lines = by_side[side]
    names = LINE_NAMES[side]
    start_li = names.index(start_line)
    end_li = names.index(end_line)
    last = end_index + rn
    if start_li == end_li:
        return list(lines[start_li][start_index:last])
    stems = list(lines[start_li][start_index:])
    for line_index in range(start_li + 1, end_li):
        stems.extend(lines[line_index])
    stems.extend(lines[end_li][:last])
    return stems


def immediately_after(gap: list[str] | tuple[str, ...], gram: tuple[str, ...]) -> bool:
    """True iff gram is a prefix of the gap (no extra stems after the left island)."""
    n = len(gram)
    return n > 0 and len(gap) >= n and tuple(gap[:n]) == gram


def immediately_before(gap: list[str] | tuple[str, ...], gram: tuple[str, ...]) -> bool:
    """True iff gram is a suffix of the gap (no extra stems before the right island)."""
    n = len(gram)
    return n > 0 and len(gap) >= n and tuple(gap[-n:]) == gram


def flattened_maximals(
    window_gr: list[str] | tuple[str, ...],
    window_kv: list[str] | tuple[str, ...],
):
    """Cycle-67 maximal finder on each window as one flattened line."""
    by_side = {
        SIDE_GR: [list(window_gr)],
        SIDE_GV: [[]],
        SIDE_KR: [[]],
        SIDE_KV: [list(window_kv)],
    }
    return maximal_rows(score_shared_n8(by_side, (SIDE_GR,), (SIDE_KV,)))


def combined_is_one_maximal(
    window_gr: list[str] | tuple[str, ...],
    window_kv: list[str] | tuple[str, ...],
    maximals=None,
) -> bool:
    """True iff the full equal windows are themselves the one maximal n≥8."""
    if maximals is None:
        maximals = flattened_maximals(window_gr, window_kv)
    if len(maximals) != 1:
        return False
    if list(window_gr) != list(window_kv):
        return False
    return maximals[0].n == len(window_gr) and maximals[0].tokens == tuple(window_gr)


def is_one_block(exact_match: bool, one_maximal: bool) -> bool:
    """True iff the span is one exact shared maximal run."""
    return exact_match and one_maximal


def is_two_islands_plus_filler(
    exact_match: bool,
    one_maximal: bool,
    shared_n_ge_8: bool,
) -> bool:
    """True iff the span shares n≥8 but stays two maximals with a mismatch."""
    return (not exact_match) and (not one_maximal) and shared_n_ge_8


def score_grkv_block(
    by_side: dict[str, list[list[str]]],
    gr_left: tuple = ISLAND_5_GR,
    gr_right: tuple = ISLAND_6_GR,
    kv_left: tuple = ISLAND_5_KV,
    kv_right: tuple = ISLAND_6_KV,
) -> GrKvBlock:
    """Windows, adjacency, Hamming, and the one_block / filler poles."""
    window_gr = span_stems(by_side, gr_left, gr_right)
    window_kv = span_stems(by_side, kv_left, kv_right)
    gap_gr = intervening_stems(by_side, gr_left, gr_right)
    gap_kv = intervening_stems(by_side, kv_left, kv_right)
    _gap_n, gap_tokens = longest_shared_ngram(gap_gr, gap_kv)
    after = immediately_after(gap_gr, gap_tokens) and immediately_after(
        gap_kv, gap_tokens
    )
    before = immediately_before(gap_gr, gap_tokens) and immediately_before(
        gap_kv, gap_tokens
    )
    exact = window_gr == window_kv
    hamm = hamming_distance(window_gr, window_kv)
    shared_n, shared_tokens = longest_shared_ngram(window_gr, window_kv)
    maximals = flattened_maximals(window_gr, window_kv)
    one_maximal = combined_is_one_maximal(window_gr, window_kv, maximals)
    shared_n_ge_8 = shared_n >= MIN_SHARED_N8
    return GrKvBlock(
        window_gr=tuple(window_gr),
        window_kv=tuple(window_kv),
        len_gr=len(window_gr),
        len_kv=len(window_kv),
        hamming=hamm,
        exact_match=exact,
        immediately_after_island_5=after,
        immediately_before_island_6=before,
        combined_shared_n=shared_n,
        combined_shared_tokens=shared_tokens,
        combined_shared_n_ge_8=shared_n_ge_8,
        combined_is_one_maximal=one_maximal,
        flattened_maximal_ns=tuple(row.n for row in maximals),
        one_block=is_one_block(exact, one_maximal),
        two_islands_plus_filler=is_two_islands_plus_filler(
            exact, one_maximal, shared_n_ge_8
        ),
    )


class TestSmallSantiagoLondonGrkvBlockHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_span_includes_islands_intervening_excludes_them(self):
        """Window is island + gap + island; gap is exclusive."""
        provider = MockProvider()
        by_side = {
            SIDE_GR: [
                ["A", "B", "C", "D", "E", "F"],
                ["G", "H", "I", "J"],
            ],
        }
        left = (("A", "B"), 2, (SIDE_GR, "Gr1", 0))
        right = (("I", "J"), 2, (SIDE_GR, "Gr2", 2))
        self.assertEqual(
            span_stems(by_side, left, right),
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        )
        self.assertEqual(
            intervening_stems(by_side, left, right),
            ["C", "D", "E", "F", "G", "H"],
        )
        same = (("C", "D"), 2, (SIDE_GR, "Gr1", 2))
        self.assertEqual(span_stems(by_side, left, same), ["A", "B", "C", "D"])
        self.assertEqual(intervening_stems(by_side, left, same), [])
        self.assertEqual(provider.get_call_history(), [])

    def test_adjacency_and_one_block_vs_filler_poles(self):
        """Exact shared window is one_block; one mismatch is two islands + filler."""
        provider = MockProvider()
        gram = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
        self.assertTrue(immediately_after(gram + ("X",), gram))
        self.assertFalse(immediately_before(gram + ("X",), gram))
        self.assertTrue(immediately_before(("X",) + gram, gram))
        self.assertFalse(immediately_after(("X",) + gram, gram))
        self.assertFalse(immediately_after((), gram))
        matched = list(GRAM_10_KV) + list(gram) + list(GRAM_15)
        self.assertTrue(combined_is_one_maximal(matched, matched))
        self.assertTrue(is_one_block(True, True))
        self.assertFalse(is_two_islands_plus_filler(True, True, True))
        left = list(GRAM_10_KV) + ["066"] + list(gram) + list(GRAM_15)
        right = list(GRAM_10_KV) + ["009"] + list(gram) + list(GRAM_15)
        self.assertEqual(hamming_distance(left, right), 1)
        self.assertFalse(combined_is_one_maximal(left, right))
        self.assertEqual(
            tuple(row.n for row in flattened_maximals(left, right)),
            (25, 10),
        )
        self.assertFalse(is_one_block(False, False))
        self.assertTrue(is_two_islands_plus_filler(False, False, True))
        self.assertFalse(is_one_block(False, False))
        self.assertFalse(is_two_islands_plus_filler(False, False, False))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonGrkvBlockScoreboard(unittest.TestCase):
    """Cited-fixture Gr–Kv 5–6 one-block vs filler lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_g_k_sides()
        self.block = score_grkv_block(self.by_side)

    def test_windows_adjacency_hamming_and_block_claim(self):
        """36/36, Hamming 1, 10-gram before island 6 only; two islands + filler."""
        self.assertEqual(self.block.window_gr, STANDING_WINDOW_GR)
        self.assertEqual(self.block.window_kv, STANDING_WINDOW_KV)
        self.assertEqual(self.block.len_gr, STANDING_LEN_GR)
        self.assertEqual(self.block.len_kv, STANDING_LEN_KV)
        self.assertEqual(self.block.len_gr, 36)
        self.assertEqual(self.block.len_kv, 36)
        self.assertEqual(len(GRAM_10_KV) + 11 + len(GRAM_15), STANDING_LEN_GR)
        self.assertEqual(self.block.hamming, STANDING_HAMMING)
        self.assertEqual(self.block.hamming, 1)
        self.assertEqual(self.block.exact_match, STANDING_EXACT_MATCH)
        self.assertFalse(self.block.exact_match)
        self.assertEqual(
            (
                STANDING_MISMATCH[0],
                self.block.window_gr[STANDING_MISMATCH[0]],
                self.block.window_kv[STANDING_MISMATCH[0]],
            ),
            STANDING_MISMATCH,
        )
        self.assertEqual(
            self.block.immediately_after_island_5,
            STANDING_IMMEDIATELY_AFTER_ISLAND_5,
        )
        self.assertEqual(
            self.block.immediately_before_island_6,
            STANDING_IMMEDIATELY_BEFORE_ISLAND_6,
        )
        self.assertFalse(STANDING_IMMEDIATELY_AFTER_ISLAND_5)
        self.assertTrue(STANDING_IMMEDIATELY_BEFORE_ISLAND_6)
        gap_gr = intervening_stems(self.by_side, ISLAND_5_GR, ISLAND_6_GR)
        gap_kv = intervening_stems(self.by_side, ISLAND_5_KV, ISLAND_6_KV)
        self.assertEqual(len(gap_gr), 11)
        self.assertEqual(len(gap_kv), 11)
        self.assertEqual(tuple(gap_gr[1:]), STANDING_GAP_10GRAM)
        self.assertEqual(tuple(gap_kv[1:]), STANDING_GAP_10GRAM)
        self.assertFalse(immediately_after(gap_gr, STANDING_GAP_10GRAM))
        self.assertFalse(immediately_after(gap_kv, STANDING_GAP_10GRAM))
        self.assertTrue(immediately_before(gap_gr, STANDING_GAP_10GRAM))
        self.assertTrue(immediately_before(gap_kv, STANDING_GAP_10GRAM))
        self.assertEqual(self.block.combined_shared_n, STANDING_COMBINED_SHARED_N)
        self.assertEqual(
            self.block.combined_shared_tokens,
            STANDING_COMBINED_SHARED_TOKENS,
        )
        self.assertEqual(
            self.block.combined_shared_n_ge_8,
            STANDING_COMBINED_SHARED_N_GE_8,
        )
        self.assertTrue(STANDING_COMBINED_SHARED_N_GE_8)
        self.assertGreaterEqual(self.block.combined_shared_n, MIN_SHARED_N8)
        self.assertEqual(
            self.block.combined_is_one_maximal,
            STANDING_COMBINED_IS_ONE_MAXIMAL,
        )
        self.assertFalse(STANDING_COMBINED_IS_ONE_MAXIMAL)
        self.assertEqual(
            self.block.flattened_maximal_ns,
            STANDING_FLATTENED_MAXIMAL_NS,
        )
        self.assertEqual(
            len(self.block.flattened_maximal_ns),
            STANDING_FLATTENED_MAXIMAL_COUNT,
        )
        self.assertEqual(self.block.one_block, STANDING_ONE_BLOCK)
        self.assertEqual(
            self.block.two_islands_plus_filler,
            STANDING_TWO_ISLANDS_PLUS_FILLER,
        )
        self.assertFalse(STANDING_ONE_BLOCK)
        self.assertTrue(STANDING_TWO_ISLANDS_PLUS_FILLER)
        self.assertNotEqual(STANDING_ONE_BLOCK, STANDING_TWO_ISLANDS_PLUS_FILLER)
        self.assertEqual(
            tuple(span_stems(self.by_side, ISLAND_5_GR, ISLAND_6_GR)),
            tuple(GRAM_10_KV) + tuple(gap_gr) + tuple(GRAM_15),
        )
        self.assertEqual(
            tuple(span_stems(self.by_side, ISLAND_5_KV, ISLAND_6_KV)),
            tuple(GRAM_10_KV) + tuple(gap_kv) + tuple(GRAM_15),
        )
        self.assertEqual(ISLAND_5_GR[0], GRAM_10_KV)
        self.assertEqual(ISLAND_6_GR[0], GRAM_15)
        self.assertEqual(ISLAND_5_GR[2], (SIDE_GR, "Gr6", 33))
        self.assertEqual(ISLAND_6_GR[2], (SIDE_GR, "Gr7", 0))
        self.assertEqual(ISLAND_5_KV[2], (SIDE_KV, "Kv3", 15))
        self.assertEqual(ISLAND_6_KV[2], (SIDE_KV, "Kv4", 7))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_island_gap_scoreboard_still_computes(self):
        """Cycle 75 G–K same-side gap lock stays."""
        prior = TestMamariSmallSantiagoLondonIslandGapScoreboard()
        prior.setUp()
        prior.test_four_gap_table_lengths_and_longest_shared_n()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-76 Gr–Kv 5–6 block lock."""
        lock = self.survey["tablet_g_k_grkv_block"]
        self.assertEqual(lock["cycle"], 76)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["len_gr"], STANDING_LEN_GR)
        self.assertEqual(lock["len_kv"], STANDING_LEN_KV)
        self.assertEqual(tuple(lock["window_gr"]), STANDING_WINDOW_GR)
        self.assertEqual(tuple(lock["window_kv"]), STANDING_WINDOW_KV)
        self.assertEqual(lock["hamming"], STANDING_HAMMING)
        self.assertEqual(lock["exact_match"], STANDING_EXACT_MATCH)
        self.assertFalse(lock["exact_match"])
        self.assertEqual(tuple(lock["mismatch"]), STANDING_MISMATCH)
        self.assertEqual(
            lock["immediately_after_island_5"],
            STANDING_IMMEDIATELY_AFTER_ISLAND_5,
        )
        self.assertEqual(
            lock["immediately_before_island_6"],
            STANDING_IMMEDIATELY_BEFORE_ISLAND_6,
        )
        self.assertFalse(lock["immediately_after_island_5"])
        self.assertTrue(lock["immediately_before_island_6"])
        self.assertEqual(tuple(lock["gap_10gram"]), STANDING_GAP_10GRAM)
        self.assertEqual(lock["combined_shared_n"], STANDING_COMBINED_SHARED_N)
        self.assertEqual(
            tuple(lock["combined_shared_tokens"]),
            STANDING_COMBINED_SHARED_TOKENS,
        )
        self.assertEqual(
            lock["combined_shared_n_ge_8"],
            STANDING_COMBINED_SHARED_N_GE_8,
        )
        self.assertTrue(lock["combined_shared_n_ge_8"])
        self.assertEqual(
            lock["combined_is_one_maximal"],
            STANDING_COMBINED_IS_ONE_MAXIMAL,
        )
        self.assertFalse(lock["combined_is_one_maximal"])
        self.assertEqual(
            tuple(lock["flattened_maximal_ns"]),
            STANDING_FLATTENED_MAXIMAL_NS,
        )
        self.assertEqual(lock["one_block"], STANDING_ONE_BLOCK)
        self.assertEqual(
            lock["two_islands_plus_filler"],
            STANDING_TWO_ISLANDS_PLUS_FILLER,
        )
        self.assertFalse(lock["one_block"])
        self.assertTrue(lock["two_islands_plus_filler"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertTrue(lock["standing_gk_island_reading_order_unchanged"])
        self.assertTrue(lock["standing_gk_island_gaps_unchanged"])
        self.assertTrue(lock["standing_hpq_island_recto_gaps_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_island_gaps"]["cycle"], 75)
        self.assertEqual(self.survey["tablet_g_k_island_reading_order"]["cycle"], 74)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonGrkvBlockImageSnapshot(unittest.TestCase):
    """Cycle 76 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
