"""Published Barthel non-040 cell inventory: Ca6–Ca9 stems in cells.

Cycle 27 text-search lock. Uses only the existing Kohaumotu / Guy
fixture (tests/fixtures/mamari_ca6_ca9_barthel.json) and the cycle-26
inter-delimiter cell table. No invented Barthel. No G00n→Barthel map.
No type merge. No detector retune.

For each distinct non-040 stem that appears inside a cell: stem, total
count, ordered hits (line, per-line cell index, position-in-cell), and
whether any hit is immediately adjacent to a published window. Adjacent
means the last token of a cell that faces a window, or the first token
of a cell that follows a window. Window tokens themselves are out of
scope. 040 is excluded.

Stems are ids only. No lunar reading. Search lock, not a merge and not
a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from processors.glyph_processor import min_pairwise_window_hamming
from tests.test_mamari_040_run_profile_scoreboard import LINE_NAMES, STEM_040
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_delimiter_cell_scoreboard import (
    FOLLOWING_CA6_VARIANT,
    FOLLOWING_GUY,
    STANDING_CELLS,
    STANDING_CELL_COUNT,
    DelimiterCell,
    score_delimiter_cells,
)
from tests.test_mamari_delimiter_window_scoreboard import (
    STANDING_SLOT_MATCHES,
    STANDING_SLOT_UNIQUE_COUNTS,
    score_delimiter_windows,
)
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_nearest_8window_scoreboard import STANDING_PUBLISHED_MIN_HAMMING
from tests.test_mamari_position_alignment_scoreboard import published_ca7_ca8_stems
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_UNIQUE_CLUSTERS,
    published_ca7_ca8_stem_counts,
    score_type_identity,
)

# (stem, count, hits, window_adjacent)
# hits: ((line, cell_index, position_in_cell), ...)
STANDING_NON040_INVENTORY = (
    ("010", 1, (("Ca6", 1, 1),), False),
    ("030", 1, (("Ca6", 1, 3),), True),
    ("074", 1, (("Ca7", 1, 1),), False),
    ("059", 1, (("Ca7", 1, 3),), False),
    ("044", 1, (("Ca7", 2, 0),), True),
    ("143", 1, (("Ca7", 2, 3),), False),
    ("152", 1, (("Ca7", 2, 4),), False),
    ("600", 2, (("Ca7", 2, 5), ("Ca8", 2, 0)), True),
    ("003", 1, (("Ca8", 1, 2),), False),
    ("280", 1, (("Ca8", 3, 0),), True),
    ("385", 2, (("Ca8", 3, 1), ("Ca8", 3, 2)), False),
)
STANDING_NON040_STEM_COUNT = 11
STANDING_NON040_HIT_COUNT = 13
STANDING_WINDOW_ADJACENT_STEM_COUNT = 4
STANDING_WINDOW_ADJACENT_STEMS = ("030", "044", "600", "280")


@dataclass(frozen=True)
class Non040Stem:
    """One non-040 stem collected from cells. Id only; no meaning."""

    stem: str
    count: int
    hits: tuple[tuple[str, int, int], ...]
    window_adjacent: bool


@dataclass(frozen=True)
class Non040Inventory:
    """Full non-040 inventory on the cycle-26 Ca6–Ca9 cell table."""

    rows: tuple[Non040Stem, ...]
    cells: tuple[DelimiterCell, ...]


def inventory_tuple(row: Non040Stem) -> tuple:
    """Stable lock row: stem, count, hits, window-adjacent."""
    return (row.stem, row.count, row.hits, row.window_adjacent)


def hit_is_window_adjacent(
    cell_index: int,
    position: int,
    cell: DelimiterCell,
) -> bool:
    """Last token facing a window, or first token of a cell after a window."""
    follows_window = cell_index > 0
    faces_window = cell.following_window is not None
    if cell.length == 0:
        return False
    return (position == 0 and follows_window) or (
        position == cell.length - 1 and faces_window
    )


def score_non040_inventory_from_cells(
    cells: tuple[DelimiterCell, ...] | list[DelimiterCell],
    stem: str = STEM_040,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> Non040Inventory:
    """Inventory distinct non-040 stems from a cell table. Search only."""
    rows_by_stem: dict[str, list[tuple[str, int, int]]] = {}
    adjacent_by_stem: dict[str, bool] = {}
    cells_by_line = {name: [] for name in line_names}
    for cell in cells:
        cells_by_line.setdefault(cell.line, []).append(cell)
    for name in line_names:
        for cell_index, cell in enumerate(cells_by_line.get(name, ())):
            for position, token in enumerate(cell.tokens):
                if token == stem:
                    continue
                rows_by_stem.setdefault(token, []).append(
                    (cell.line, cell_index, position)
                )
                adjacent = hit_is_window_adjacent(cell_index, position, cell)
                adjacent_by_stem[token] = adjacent_by_stem.get(token, False) or adjacent
    rows = tuple(
        Non040Stem(
            stem=token,
            count=len(hits),
            hits=tuple(hits),
            window_adjacent=adjacent_by_stem[token],
        )
        for token, hits in rows_by_stem.items()
    )
    return Non040Inventory(rows=rows, cells=tuple(cells))


def score_non040_inventory(
    lines: list[list[str]],
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    stem: str = STEM_040,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> Non040Inventory:
    """Build the inventory from cycle-26 cells of these lines. Search only."""
    profile = score_delimiter_cells(lines, motif=motif, stem=stem, line_names=line_names)
    return score_non040_inventory_from_cells(profile.cells, stem=stem, line_names=line_names)


class TestNon040InventoryHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_inventory_skips_040_and_window_tokens(self):
        """040 and Guy-window stems are out of the inventory."""
        motif = DELIMITER_MOTIF
        lines = [
            ["040", "010"] + list(motif) + ["044", "040", "600"],
            ["040", "040"],
        ]
        names = ("L0", "L1")
        inventory = score_non040_inventory(lines, line_names=names)
        locked = tuple(inventory_tuple(row) for row in inventory.rows)
        self.assertEqual(
            locked,
            (
                ("010", 1, (("L0", 0, 1),), True),
                ("044", 1, (("L0", 1, 0),), True),
                ("600", 1, (("L0", 1, 2),), False),
            ),
        )
        self.assertNotIn(STEM_040, [row.stem for row in inventory.rows])
        for token in motif:
            self.assertNotIn(token, [row.stem for row in inventory.rows])
        self.assertEqual(len(inventory.cells), 3)

    def test_window_adjacent_first_after_and_last_facing(self):
        """First-after-window and last-facing-window; trail last is not."""
        motif = DELIMITER_MOTIF
        lines = [
            ["040", "010", "030"] + list(motif) + ["044"] + list(motif) + ["280", "385"],
        ]
        inventory = score_non040_inventory(lines, line_names=("L0",))
        by_stem = {row.stem: row for row in inventory.rows}
        self.assertFalse(by_stem["010"].window_adjacent)
        self.assertTrue(by_stem["030"].window_adjacent)
        self.assertEqual(by_stem["030"].hits, (("L0", 0, 2),))
        self.assertTrue(by_stem["044"].window_adjacent)
        self.assertEqual(by_stem["044"].hits, (("L0", 1, 0),))
        self.assertTrue(by_stem["280"].window_adjacent)
        self.assertFalse(by_stem["385"].window_adjacent)
        self.assertEqual(by_stem["385"].hits, (("L0", 2, 1),))

    def test_ca6_variant_and_repeated_stem_any_adjacent(self):
        """315 variant counts as a window; any-hit adjacent is True."""
        variant = ("390", "041", "315", "041", "670", "008", "078", "711")
        lines = [["074"] + list(variant) + ["600", "040", "600"]]
        inventory = score_non040_inventory(lines, line_names=("Ca6",))
        self.assertEqual(
            [cell.following_window for cell in inventory.cells],
            [FOLLOWING_CA6_VARIANT, None],
        )
        by_stem = {row.stem: row for row in inventory.rows}
        self.assertTrue(by_stem["074"].window_adjacent)
        self.assertEqual(by_stem["600"].count, 2)
        self.assertEqual(by_stem["600"].hits, (("Ca6", 1, 0), ("Ca6", 1, 2)))
        self.assertTrue(by_stem["600"].window_adjacent)
        self.assertNotIn("378", lines[0])


class TestMamariNon040InventoryScoreboard(unittest.TestCase):
    """Published Ca6–Ca9 non-040 cell inventory lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.fixture = load_mamari_fixture()
        self.lines = fixture_line_stems(self.fixture)
        self.cell_profile = score_delimiter_cells(self.lines)
        self.profile = score_non040_inventory(self.lines)

    def test_fixture_is_the_existing_published_passage(self):
        """Same cited fixture as the calendar scoreboard. No new numbers."""
        source = self.fixture["source"]
        self.assertIn("kohaumotu.org", source["primary"]["url"])
        self.assertEqual(tuple(self.fixture["lines"]), LINE_NAMES)
        self.assertEqual([len(line) for line in self.lines], [16, 43, 40, 2])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_inventory_uses_cycle26_cell_table_only(self):
        """Rows come from STANDING_CELLS; window stems never enter."""
        self.assertEqual(len(self.cell_profile.cells), STANDING_CELL_COUNT)
        locked_cells = tuple(
            (
                cell.line,
                cell.start,
                cell.end,
                cell.tokens,
                cell.length,
                cell.count_040,
                cell.non_040,
                cell.following_window,
            )
            for cell in self.cell_profile.cells
        )
        self.assertEqual(locked_cells, STANDING_CELLS)
        from_cells = score_non040_inventory_from_cells(self.cell_profile.cells)
        self.assertEqual(
            tuple(inventory_tuple(row) for row in from_cells.rows),
            tuple(inventory_tuple(row) for row in self.profile.rows),
        )
        window_stems = {
            token
            for line, start, end in self.cell_profile.windows
            for token in self.lines[LINE_NAMES.index(line)][start:end]
        }
        inventory_stems = {row.stem for row in self.profile.rows}
        self.assertTrue(inventory_stems.isdisjoint(window_stems))
        self.assertNotIn(STEM_040, inventory_stems)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_inventory_table_is_standing_truth(self):
        """Lock every non-040 stem: count, cell hits, window-adjacent."""
        locked = tuple(inventory_tuple(row) for row in self.profile.rows)
        self.assertEqual(len(locked), STANDING_NON040_STEM_COUNT)
        self.assertEqual(locked, STANDING_NON040_INVENTORY)
        self.assertEqual(
            sum(row.count for row in self.profile.rows),
            STANDING_NON040_HIT_COUNT,
        )
        adjacent = [row.stem for row in self.profile.rows if row.window_adjacent]
        self.assertEqual(len(adjacent), STANDING_WINDOW_ADJACENT_STEM_COUNT)
        self.assertEqual(tuple(adjacent), STANDING_WINDOW_ADJACENT_STEMS)
        cells_by_line: dict[str, list[DelimiterCell]] = {name: [] for name in LINE_NAMES}
        for cell in self.cell_profile.cells:
            cells_by_line[cell.line].append(cell)
        seen = 0
        for row in self.profile.rows:
            self.assertEqual(row.count, len(row.hits))
            self.assertNotEqual(row.stem, STEM_040)
            any_adjacent = False
            for line, cell_index, position in row.hits:
                cell = cells_by_line[line][cell_index]
                self.assertEqual(cell.tokens[position], row.stem)
                any_adjacent = any_adjacent or hit_is_window_adjacent(
                    cell_index, position, cell
                )
                seen += 1
            self.assertEqual(row.window_adjacent, any_adjacent)
        self.assertEqual(seen, STANDING_NON040_HIT_COUNT)
        cell_non040 = [
            token
            for cell in self.cell_profile.cells
            for token in cell.tokens
            if token != STEM_040
        ]
        inventory_tokens = [
            row.stem for row in self.profile.rows for _hit in row.hits
        ]
        self.assertEqual(sorted(cell_non040), sorted(inventory_tokens))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_occupied_cell_hits_match_published_passage(self):
        """Occupied cells stay the cycle-26 token lists; hits point inside."""
        occupied = [cell for cell in self.cell_profile.cells if cell.length]
        self.assertEqual(
            [cell.tokens for cell in occupied],
            [
                ("040", "010", "040", "030"),
                ("040", "040", "040", "040", "040", "040"),
                ("040", "074", "040", "059", "040"),
                ("044", "040", "040", "143", "152", "600"),
                ("040", "040"),
                ("040", "040", "040"),
                ("040", "040", "003", "040"),
                ("600", "040", "040", "040", "040", "040"),
                ("280", "385", "385"),
                ("040", "040"),
            ],
        )
        self.assertEqual(occupied[0].following_window, FOLLOWING_CA6_VARIANT)
        self.assertEqual(
            [cell.following_window for cell in occupied if cell.line == "Ca7"],
            [FOLLOWING_GUY, FOLLOWING_GUY, FOLLOWING_GUY, None],
        )
        self.assertEqual(
            [cell.following_window for cell in occupied if cell.line == "Ca8"],
            [FOLLOWING_GUY, FOLLOWING_GUY, FOLLOWING_GUY, None],
        )
        self.assertIsNone(occupied[-1].following_window)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariNon040InventoryImageSnapshot(unittest.TestCase):
    """Cycle 27 does not touch clustering. 83/62 / Hamming 6 stays."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.published_lines = published_ca7_ca8_stems()

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. 83/62 / published Hamming 6 / 0/8."""
        published = self.published_lines
        window = score_delimiter_windows(self.instances, self.image_lines, published)
        published_ca7, published_ca8 = published_ca7_ca8_stem_counts()
        identity = score_type_identity(
            self.instances, self.analyzer, published_ca7, published_ca8
        )
        grams = tuple(w.image_ids for w in window.windows)
        self.assertEqual(window.instance_count, 83)
        self.assertEqual(window.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(identity.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(identity.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(min_pairwise_window_hamming(grams), STANDING_PUBLISHED_MIN_HAMMING)
        self.assertEqual(min_pairwise_window_hamming(grams), 6)
        self.assertEqual(window.slot_matches, STANDING_SLOT_MATCHES)
        unique_counts = tuple(len(set(ids)) for ids in window.slot_ids)
        self.assertEqual(unique_counts, STANDING_SLOT_UNIQUE_COUNTS)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
