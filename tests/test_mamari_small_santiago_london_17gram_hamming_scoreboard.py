"""G–K 17-gram nearest other 17-window Hamming.

Cycle 64 / focused-batch 3 of 5. Uses only the already-vendored
fixtures. No new tablet. Exact 17-gram from cycle 61/62/63. Raw
stems. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents.

Locks the nearest length-17 window by Hamming vs that motif after
excluding the two exact hits. Also locks best Hamming per fixture
and whether any non-exact window has Hamming ≤ 4. Stem ids only —
not meanings. Image stays parked Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_br_scoreboard import BR_LINE_NAMES
from tests.test_mamari_aruku_bv_scoreboard import BV_LINE_NAMES
from tests.test_mamari_cb_side_b_scoreboard import CB_LINE_NAMES
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    PASSAGE_AA,
    PASSAGE_AB,
    PASSAGE_BR,
    PASSAGE_BV,
    PASSAGE_CALENDAR,
    PASSAGE_CB,
    PASSAGE_IA,
    PASSAGE_REMAINDER,
)
from tests.test_mamari_santiago_ia_scoreboard import IA_LINE_NAMES
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    REMAINDER_LINE_NAMES,
    load_corpus_survey,
)
from tests.test_mamari_small_london_kr_scoreboard import KR_LINE_NAMES
from tests.test_mamari_small_london_kv_scoreboard import KV_LINE_NAMES
from tests.test_mamari_small_santiago_gr_scoreboard import GR_LINE_NAMES
from tests.test_mamari_small_santiago_gv_scoreboard import GV_LINE_NAMES
from tests.test_mamari_small_santiago_gv_430_076_200_ngram_scoreboard import (
    PASSAGE_GR,
    PASSAGE_GV,
)
from tests.test_mamari_small_santiago_london_17gram_flank_scoreboard import (
    STANDING_GR_SITE,
    STANDING_KR_SITE,
    TestMamariSmallSantiagoLondon17gramFlankScoreboard,
)
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import (
    GRAM_17,
    PASSAGE_KR,
    PASSAGE_KV,
    PASSAGE_ORDER,
    STANDING_COMBINED_N,
    STANDING_NEW_TABLET,
    STANDING_ROW_COUNT,
    STANDING_STEM_076_IN_LONGEST,
    existing_gk_17gram_lines,
)
from tests.test_mamari_tahua_aa_scoreboard import AA_LINE_NAMES
from tests.test_mamari_tahua_ab_scoreboard import AB_LINE_NAMES

HAMMING_LE = 4
PASSAGE_LINE_NAMES = {
    PASSAGE_CALENDAR: CALENDAR_LINE_NAMES,
    PASSAGE_REMAINDER: REMAINDER_LINE_NAMES,
    PASSAGE_CB: CB_LINE_NAMES,
    PASSAGE_AA: AA_LINE_NAMES,
    PASSAGE_AB: AB_LINE_NAMES,
    PASSAGE_BR: BR_LINE_NAMES,
    PASSAGE_BV: BV_LINE_NAMES,
    PASSAGE_IA: IA_LINE_NAMES,
    PASSAGE_GR: GR_LINE_NAMES,
    PASSAGE_GV: GV_LINE_NAMES,
    PASSAGE_KR: KR_LINE_NAMES,
    PASSAGE_KV: KV_LINE_NAMES,
}

# (passage, line, start, end, hamming)
STANDING_NEAREST = (PASSAGE_KV, "Kv3", 5, 22, 6)
STANDING_NEAREST_TOKENS = (
    "380",
    "001",
    "003",
    "003",
    "246",
    "003",
    "380",
    "001",
    "003",
    "400",
    "380",
    "001",
    "003",
    "005",
    "066",
    "380",
    "001",
)
STANDING_NEAREST_HAMMING = 6
STANDING_ANY_LE4 = False
STANDING_EXACT_COUNT = 2
# (passage, hamming, line, start)
STANDING_BEST_TABLE = (
    (PASSAGE_CALENDAR, 16, "Ca8", 1),
    (PASSAGE_REMAINDER, 12, "Ca3", 0),
    (PASSAGE_CB, 10, "Cb3", 4),
    (PASSAGE_AA, 14, "Aa4", 30),
    (PASSAGE_AB, 13, "Ab6", 102),
    (PASSAGE_BR, 14, "Br4", 32),
    (PASSAGE_BV, 14, "Bv4", 0),
    (PASSAGE_IA, 14, "Ia14", 116),
    (PASSAGE_GR, 9, "Gr3", 22),
    (PASSAGE_GV, 15, "Gv1", 10),
    (PASSAGE_KR, 9, "Kr4", 2),
    (PASSAGE_KV, 6, "Kv3", 5),
)
STANDING_BEST_HAMMINGS = tuple(row[1] for row in STANDING_BEST_TABLE)


@dataclass(frozen=True)
class HammingWindow:
    """One length-17 window vs the motif. Ids only; no meaning."""

    passage: str
    line: str
    start: int
    end: int
    tokens: tuple[str, ...]
    hamming: int


@dataclass(frozen=True)
class NearestHammingLock:
    """Nearest non-exact 17-window plus best Hamming per fixture."""

    nearest: HammingWindow
    per_fixture: tuple[HammingWindow, ...]
    any_le4: bool
    exact_count: int


def hamming_distance(left: tuple[str, ...] | list[str], right: tuple[str, ...] | list[str]) -> int:
    """Positions that differ. Equal length required."""
    if len(left) != len(right):
        raise ValueError("Hamming requires equal-length windows")
    return sum(a != b for a, b in zip(left, right))


def window_row(hit: HammingWindow) -> tuple:
    """Stable lock row: passage, line, [start, end), Hamming."""
    return (hit.passage, hit.line, hit.start, hit.end, hit.hamming)


def best_row(hit: HammingWindow) -> tuple:
    """Stable per-fixture lock: passage, Hamming, line, start."""
    return (hit.passage, hit.hamming, hit.line, hit.start)


def window_sort_key(hit: HammingWindow) -> tuple:
    """Min Hamming; tie → earliest passage, line, start."""
    return (
        hit.hamming,
        PASSAGE_ORDER.index(hit.passage),
        PASSAGE_LINE_NAMES[hit.passage].index(hit.line),
        hit.start,
    )


def score_passage_windows(
    lines: list[list[str]],
    line_names: tuple[str, ...],
    passage: str,
    gram: tuple[str, ...] = GRAM_17,
) -> tuple[HammingWindow, ...]:
    """Every in-line 17-window vs gram. Search only."""
    n = len(gram)
    rows: list[HammingWindow] = []
    for line_index, sequence in enumerate(lines):
        for start in range(len(sequence) - n + 1):
            tokens = tuple(sequence[start : start + n])
            rows.append(
                HammingWindow(
                    passage=passage,
                    line=line_names[line_index],
                    start=start,
                    end=start + n,
                    tokens=tokens,
                    hamming=hamming_distance(tokens, gram),
                )
            )
    return tuple(rows)


def nearest_nonexact(windows: tuple[HammingWindow, ...] | list[HammingWindow]) -> HammingWindow | None:
    """Min Hamming among windows that are not exact motif hits."""
    others = [hit for hit in windows if hit.hamming]
    if not others:
        return None
    return min(others, key=window_sort_key)


def any_nonexact_hamming_le(
    windows: tuple[HammingWindow, ...] | list[HammingWindow],
    limit: int = HAMMING_LE,
) -> bool:
    """True iff a non-exact window has Hamming ≤ limit."""
    return any(hit.hamming and hit.hamming <= limit for hit in windows)


def score_gk_17gram_hamming(
    by_passage: dict[str, list[list[str]]],
    gram: tuple[str, ...] = GRAM_17,
    line_names: dict[str, tuple[str, ...]] = PASSAGE_LINE_NAMES,
) -> NearestHammingLock:
    """Nearest non-exact 17-window and best Hamming per fixture."""
    all_windows: list[HammingWindow] = []
    best_rows: list[HammingWindow] = []
    exact_count = 0
    for passage in PASSAGE_ORDER:
        windows = score_passage_windows(by_passage[passage], line_names[passage], passage, gram)
        all_windows.extend(windows)
        exact_count += sum(1 for hit in windows if not hit.hamming)
        nearest = nearest_nonexact(windows)
        if nearest is None:
            raise AssertionError(f"{passage} has no non-exact 17-window")
        best_rows.append(nearest)
    nearest = nearest_nonexact(all_windows)
    if nearest is None:
        raise AssertionError("no non-exact 17-window on the twelve fixtures")
    return NearestHammingLock(
        nearest=nearest,
        per_fixture=tuple(best_rows),
        any_le4=any_nonexact_hamming_le(all_windows),
        exact_count=exact_count,
    )


class TestSmallSantiagoLondon17gramHammingHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_hamming_and_nearest_excludes_exact(self):
        """Exact motif is 0; a one-token miss is 1; exact hits are dropped."""
        provider = MockProvider()
        gram = GRAM_17
        miss = ("X",) + gram[1:]
        self.assertEqual(hamming_distance(gram, gram), 0)
        self.assertEqual(hamming_distance(miss, gram), 1)
        with self.assertRaises(ValueError):
            hamming_distance(gram, gram[:-1])
        names = ("L0", "L1")
        lines = [list(gram), list(miss)]
        windows = score_passage_windows(lines, names, "synth", gram)
        self.assertEqual(tuple(hit.hamming for hit in windows), (0, 1))
        nearest = nearest_nonexact(windows)
        self.assertIsNotNone(nearest)
        self.assertEqual(window_row(nearest), ("synth", "L1", 0, 17, 1))
        self.assertTrue(any_nonexact_hamming_le(windows, 4))
        self.assertFalse(any_nonexact_hamming_le(windows, 0))
        self.assertIsNone(nearest_nonexact(windows[:1]))
        self.assertEqual(len(gram), STANDING_COMBINED_N)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_breaks_to_earliest_start(self):
        """Equal Hamming keeps the earlier line/start."""
        provider = MockProvider()
        gram = GRAM_17
        miss_a = ("A",) + gram[1:]
        miss_b = ("B",) + gram[1:]
        lines = [list(miss_b), list(miss_a)]
        windows = score_passage_windows(lines, ("L0", "L1"), "synth", gram)
        nearest = nearest_nonexact(windows)
        self.assertEqual(nearest.line, "L0")
        self.assertEqual(nearest.hamming, 1)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondon17gramHammingScoreboard(unittest.TestCase):
    """Cited-fixture G–K 17-gram nearest Hamming lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_gk_17gram_lines()
        self.lock = score_gk_17gram_hamming(self.by_passage)
        self.locked_nearest = window_row(self.lock.nearest)
        self.locked_table = tuple(best_row(hit) for hit in self.lock.per_fixture)

    def test_nearest_window_and_le4_flag(self):
        """Kv3[5] Hamming 6 is nearest; no non-exact window is ≤ 4."""
        self.assertEqual(self.locked_nearest, STANDING_NEAREST)
        self.assertEqual(self.lock.nearest.tokens, STANDING_NEAREST_TOKENS)
        self.assertEqual(self.lock.nearest.hamming, STANDING_NEAREST_HAMMING)
        self.assertEqual(self.lock.nearest.line, "Kv3")
        self.assertEqual(self.lock.nearest.start, 5)
        self.assertEqual(self.lock.any_le4, STANDING_ANY_LE4)
        self.assertFalse(STANDING_ANY_LE4)
        self.assertEqual(self.lock.exact_count, STANDING_EXACT_COUNT)
        self.assertEqual(len(GRAM_17), STANDING_COMBINED_N)
        self.assertEqual("076" in GRAM_17, STANDING_STEM_076_IN_LONGEST)
        self.assertFalse(STANDING_STEM_076_IN_LONGEST)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_best_hamming_per_fixture(self):
        """Twelve-row nearest non-exact 17-window Hamming table."""
        self.assertEqual(self.locked_table, STANDING_BEST_TABLE)
        self.assertEqual(len(self.lock.per_fixture), STANDING_ROW_COUNT)
        self.assertEqual(tuple(hit.passage for hit in self.lock.per_fixture), PASSAGE_ORDER)
        self.assertEqual(
            tuple(hit.hamming for hit in self.lock.per_fixture),
            STANDING_BEST_HAMMINGS,
        )
        self.assertEqual(min(STANDING_BEST_HAMMINGS), STANDING_NEAREST_HAMMING)
        self.assertEqual(self.lock.per_fixture[-1].line, "Kv3")
        self.assertGreater(min(STANDING_BEST_HAMMINGS), HAMMING_LE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_exact_hits_are_the_cycle63_sites(self):
        """Excluded Hamming-0 windows are Gr4[3] and Kr5[0] only."""
        exact = []
        for passage in PASSAGE_ORDER:
            for hit in score_passage_windows(
                self.by_passage[passage],
                PASSAGE_LINE_NAMES[passage],
                passage,
            ):
                if not hit.hamming:
                    exact.append((hit.passage, hit.line, hit.start))
        self.assertEqual(
            tuple(exact),
            (
                (STANDING_GR_SITE[0], STANDING_GR_SITE[1], STANDING_GR_SITE[2]),
                (STANDING_KR_SITE[0], STANDING_KR_SITE[1], STANDING_KR_SITE[2]),
            ),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_17gram_flank_scoreboard_still_computes(self):
        """Cycle 63 site/flank lock stays."""
        prior = TestMamariSmallSantiagoLondon17gramFlankScoreboard()
        prior.setUp()
        prior.test_gr_and_kr_hit_sites_and_flanks()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-64 nearest Hamming lock."""
        lock = self.survey["tablet_g_k_17gram_nearest_hamming"]
        self.assertEqual(lock["cycle"], 64)
        self.assertEqual(lock["focused_batch"], 3)
        self.assertEqual(lock["focused_batch_of"], 5)
        self.assertEqual(tuple(lock["tokens"]), GRAM_17)
        self.assertEqual(lock["n"], STANDING_COMBINED_N)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(tuple(lock["nearest"]), STANDING_NEAREST)
        self.assertEqual(tuple(lock["nearest_tokens"]), STANDING_NEAREST_TOKENS)
        self.assertEqual(lock["best_hamming"], STANDING_NEAREST_HAMMING)
        self.assertEqual(lock["any_nonexact_hamming_le_4"], STANDING_ANY_LE4)
        self.assertEqual(lock["exact_count"], STANDING_EXACT_COUNT)
        self.assertEqual(lock["hamming_le"], HAMMING_LE)
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(tuple(lock["best_hammings"]), STANDING_BEST_HAMMINGS)
        locked = tuple(tuple(row) for row in lock["table"])
        self.assertEqual(locked, STANDING_BEST_TABLE)
        self.assertFalse(lock["stem_076_in_gram"])
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
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_17gram_hit_sites"]["cycle"], 63)
        self.assertEqual(self.survey["tablet_g_k_17gram_hits_per_fixture"]["cycle"], 62)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondon17gramHammingImageSnapshot(unittest.TestCase):
    """Cycle 64 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
