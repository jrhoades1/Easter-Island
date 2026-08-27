"""Small Santiago Gv 076 inventory: count, density, neighbors, wraps.

Cycle 57 text-search lock. Uses the already-vendored Kohaumotu Gv.html
fixture (cycle 56). Raw stems. No new tablet. No invented Barthel.
No G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents.

Locks 076 on Gv1–Gv8: hit count, per-line density, top left/right
neighbors (line-edge is not a stem), and 076…076 wrap count at n=5
(or the longest 076-wrap if n=5 is empty). Stems are ids only. No
meanings.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from collections import Counter
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_600_sandwich_scoreboard import (
    NeighborTop,
    neighbor_top_row,
    top_neighbor,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import (
    LINE_EDGE,
    hit_flanks,
    score_002_wraps,
)
from tests.test_mamari_santiago_ia_076_inventory_scoreboard import STEM_076
from tests.test_mamari_second_passage_scoreboard import (
    load_corpus_survey,
    stem_hits,
)
from tests.test_mamari_small_santiago_gv_scoreboard import (
    GV_HTML_PATH,
    GV_LINE_NAMES,
    STANDING_076_HITS,
    STANDING_STEM_COUNTS,
    STANDING_STEM_TOTAL,
    TestMamariSmallSantiagoGvScoreboard,
    extract_gv_published_tokens,
    gv_line_stems,
    load_vendored_gv_html,
)

WRAP_N = 5
STANDING_076_COUNT = STANDING_076_HITS
STANDING_076_LINE_COUNTS = (11, 6, 7, 5, 1, 6, 4, 3)
STANDING_076_LINE_DENSITIES = tuple(
    count / stems
    for count, stems in zip(STANDING_076_LINE_COUNTS, STANDING_STEM_COUNTS)
)
STANDING_076_LEFT_TOP = ("430", 5)
STANDING_076_RIGHT_TOP = ("200", 5)
STANDING_076_WRAP_N = WRAP_N
STANDING_076_WRAP_EXISTS = True
STANDING_076_WRAP_COUNT = 5


@dataclass(frozen=True)
class Gv076Inventory:
    """Gv 076 count, per-line density, neighbors, and wraps. Ids only."""

    count: int
    line_counts: tuple[int, ...]
    line_densities: tuple[float, ...]
    left_top: NeighborTop
    right_top: NeighborTop
    wrap_n: int
    wrap_exists: bool
    wrap_count: int


def gv_076_hits(lines: list[list[str]]) -> tuple[tuple[str, int], ...]:
    """(line, index) for every stem 076. Search only."""
    return stem_hits(lines, STEM_076, GV_LINE_NAMES)


def gv_076_line_counts(lines: list[list[str]]) -> tuple[int, ...]:
    """076 count per Gv line in Barthel order."""
    return tuple(line.count(STEM_076) for line in lines)


def gv_076_line_densities(lines: list[list[str]]) -> tuple[float, ...]:
    """076 hits / stems per Gv line. Empty line is 0.0."""
    return tuple(
        (line.count(STEM_076) / len(line) if line else 0.0) for line in lines
    )


def gv_076_neighbor_tops(lines: list[list[str]]) -> tuple[NeighborTop, NeighborTop]:
    """Top left/right neighbors of 076. Line-edge is not a stem."""
    left: Counter[str] = Counter()
    right: Counter[str] = Counter()
    for name, index in gv_076_hits(lines):
        before, after = hit_flanks(lines[GV_LINE_NAMES.index(name)], index, 1)
        if before is not LINE_EDGE:
            left[before] += 1
        if after is not LINE_EDGE:
            right[after] += 1
    return top_neighbor(left), top_neighbor(right)


def gv_076_wraps(lines: list[list[str]], n: int = WRAP_N):
    """Every n-window that starts and ends with 076."""
    return score_002_wraps(lines, GV_LINE_NAMES, n=n, stem=STEM_076, motif=())


def longest_076_wraps(
    lines: list[list[str]],
    min_n: int = 2,
) -> tuple[int, tuple]:
    """Longest 076…076 wrap window and its hits. Empty is (0, ())."""
    max_len = max((len(line) for line in lines), default=0)
    for n in range(max_len, min_n - 1, -1):
        wraps = gv_076_wraps(lines, n)
        if wraps:
            return n, wraps
    return 0, ()


def score_gv_076_inventory(lines: list[list[str]]) -> Gv076Inventory:
    """076 inventory on raw Gv stems. n=5 wraps, else longest wrap."""
    n5 = gv_076_wraps(lines, WRAP_N)
    if n5:
        wrap_n, wraps = WRAP_N, n5
    else:
        wrap_n, wraps = longest_076_wraps(lines)
    left, right = gv_076_neighbor_tops(lines)
    return Gv076Inventory(
        count=len(gv_076_hits(lines)),
        line_counts=gv_076_line_counts(lines),
        line_densities=gv_076_line_densities(lines),
        left_top=left,
        right_top=right,
        wrap_n=wrap_n,
        wrap_exists=bool(wraps),
        wrap_count=len(wraps),
    )


class TestSmallSantiagoGv076Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_count_density_and_neighbor_tops(self):
        """076 totals follow the lines; edge is dropped; density is hits/stems."""
        lines = [[] for _ in GV_LINE_NAMES]
        lines[0] = ["430", "076", "200", "430", "076", "200"]
        lines[1] = ["076"]
        provider = MockProvider()
        self.assertEqual(gv_076_hits(lines), (("Gv1", 1), ("Gv1", 4), ("Gv2", 0)))
        self.assertEqual(gv_076_line_counts(lines)[:2], (2, 1))
        self.assertEqual(gv_076_line_densities(lines)[:2], (2 / 6, 1.0))
        self.assertEqual(sum(gv_076_line_counts(lines)), 3)
        left, right = gv_076_neighbor_tops(lines)
        self.assertEqual(neighbor_top_row(left, right), ("430", 2, "200", 2))
        self.assertEqual(top_neighbor(Counter()), NeighborTop(None, 0))
        self.assertEqual(provider.get_call_history(), [])

    def test_n5_wraps_or_longest_076_wrap(self):
        """n=5 076…076 is preferred; empty n=5 falls back to longest wrap."""
        lines = [[] for _ in GV_LINE_NAMES]
        lines[0] = ["076", "200", "076"]
        provider = MockProvider()
        self.assertEqual(gv_076_wraps(lines), ())
        wrap_n, wraps = longest_076_wraps(lines)
        self.assertEqual(wrap_n, 3)
        self.assertEqual(len(wraps), 1)
        self.assertEqual(wraps[0].tokens, ("076", "200", "076"))
        fallback = score_gv_076_inventory(lines)
        self.assertEqual(fallback.wrap_n, 3)
        self.assertEqual(fallback.wrap_count, 1)
        self.assertTrue(fallback.wrap_exists)
        lines[5] = ["076", "074", "031", "086", "076"]
        n5 = gv_076_wraps(lines)
        self.assertEqual(len(n5), 1)
        self.assertEqual(n5[0].tokens, ("076", "074", "031", "086", "076"))
        preferred = score_gv_076_inventory(lines)
        self.assertEqual(preferred.wrap_n, WRAP_N)
        self.assertEqual(preferred.wrap_count, 1)
        empty = score_gv_076_inventory([[] for _ in GV_LINE_NAMES])
        self.assertEqual(empty.wrap_n, 0)
        self.assertEqual(empty.wrap_count, 0)
        self.assertFalse(empty.wrap_exists)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoGv076InventoryScoreboard(unittest.TestCase):
    """Cited Gv.html 076 inventory lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.html = load_vendored_gv_html()
        self.published = extract_gv_published_tokens(self.html)
        self.lines = gv_line_stems(self.published)
        self.inventory = score_gv_076_inventory(self.lines)

    def test_076_count_line_density_and_neighbor_tops(self):
        """43 stems; per-line density; top left 430×5; top right 200×5."""
        inv = self.inventory
        self.assertEqual(inv.count, STANDING_076_COUNT)
        self.assertEqual(inv.line_counts, STANDING_076_LINE_COUNTS)
        self.assertEqual(inv.line_densities, STANDING_076_LINE_DENSITIES)
        self.assertEqual(sum(inv.line_counts), STANDING_076_COUNT)
        self.assertEqual(len(inv.line_counts), len(GV_LINE_NAMES))
        self.assertEqual(len(inv.line_densities), len(GV_LINE_NAMES))
        self.assertEqual(
            neighbor_top_row(inv.left_top, inv.right_top),
            (
                STANDING_076_LEFT_TOP[0],
                STANDING_076_LEFT_TOP[1],
                STANDING_076_RIGHT_TOP[0],
                STANDING_076_RIGHT_TOP[1],
            ),
        )
        self.assertEqual([len(line) for line in self.lines], list(STANDING_STEM_COUNTS))
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_STEM_TOTAL)
        self.assertTrue(GV_HTML_PATH.is_file())
        self.assertEqual(STEM_076, "076")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_076_n5_wraps(self):
        """076…076 wraps at n=5 exist. Count is 5. No new tablet."""
        inv = self.inventory
        self.assertEqual(inv.wrap_n, STANDING_076_WRAP_N)
        self.assertEqual(inv.wrap_exists, STANDING_076_WRAP_EXISTS)
        self.assertTrue(STANDING_076_WRAP_EXISTS)
        self.assertEqual(inv.wrap_count, STANDING_076_WRAP_COUNT)
        self.assertGreater(inv.wrap_count, 0)
        wraps = gv_076_wraps(self.lines)
        self.assertEqual(len(wraps), STANDING_076_WRAP_COUNT)
        self.assertTrue(all(wrap.tokens[0] == STEM_076 for wrap in wraps))
        self.assertTrue(all(wrap.tokens[-1] == STEM_076 for wrap in wraps))
        self.assertTrue(all(len(wrap.tokens) == WRAP_N for wrap in wraps))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gv_scoreboard_still_computes(self):
        """Cycle 56 Gv vendor lock and prior A/B/C/Ia/Gr scoreboards stay."""
        prior = TestMamariSmallSantiagoGvScoreboard()
        prior.setUp()
        prior.test_parent_catalog_selects_and_vendors_gv()
        prior.test_stem_count_motifs_076_rate_and_090_076_071()
        prior.test_existing_gr_and_scoreboards_still_compute()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-57 Gv 076 inventory."""
        lock = self.survey["small_santiago_gv_076_inventory"]
        self.assertEqual(lock["cycle"], 57)
        self.assertEqual(lock["passage"], "tablet_g_small_santiago_verso")
        self.assertEqual(lock["stem"], STEM_076)
        self.assertEqual(lock["stem_count"], STANDING_076_COUNT)
        self.assertEqual(lock["line_counts"], list(STANDING_076_LINE_COUNTS))
        self.assertEqual(lock["line_densities"], list(STANDING_076_LINE_DENSITIES))
        self.assertEqual(tuple(lock["left_top"]), STANDING_076_LEFT_TOP)
        self.assertEqual(tuple(lock["right_top"]), STANDING_076_RIGHT_TOP)
        self.assertEqual(lock["wrap_n"], STANDING_076_WRAP_N)
        self.assertEqual(lock["wrap_exists"], STANDING_076_WRAP_EXISTS)
        self.assertEqual(lock["wrap_count"], STANDING_076_WRAP_COUNT)
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_gv_locks_unchanged"])
        self.assertTrue(lock["standing_gr_locks_unchanged"])
        self.assertTrue(lock["standing_ia_076_locks_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_small_santiago_verso_gv"]["cycle"], 56)
        self.assertEqual(self.survey["tablet_g_small_santiago_verso_gv"]["stem_076_hits"], 43)
        self.assertEqual(self.survey["santiago_ia_076_inventory"]["cycle"], 48)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoGv076ImageSnapshot(unittest.TestCase):
    """Cycle 57 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
