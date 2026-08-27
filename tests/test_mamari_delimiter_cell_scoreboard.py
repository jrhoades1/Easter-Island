"""Published Barthel inter-delimiter cells: Ca6–Ca9 token gaps.

Cycle 26 text-search lock. Uses only the existing Kohaumotu / Guy
fixture (tests/fixtures/mamari_ca6_ca9_barthel.json). No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.

A cell is the token sequence from the end of one published Guy window
(or Ca6 315/375 first-delimiter variant) to the start of the next,
plus a leading cell before the first window and a trailing cell after
the last, per line. A line with no window is one cell covering the
line. Empty leading/trailing cells are kept when a window sits on a
line edge.

Each cell locks line, [start, end), tokens, length, 040-count,
non-040 tokens in order, and following-window kind (guy /
ca6-variant / none). 040 is the published stem only. No lunar
reading. Search lock, not a merge and not a translation.
MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from processors.glyph_processor import min_pairwise_window_hamming
from tests.test_mamari_040_run_profile_scoreboard import (
    LINE_NAMES,
    STANDING_PRECEDE_WINDOWS,
    STEM_040,
    delimiter_and_variant_spans,
    variant_motifs,
)
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
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

FOLLOWING_GUY = "guy"
FOLLOWING_CA6_VARIANT = "ca6-variant"

# (line, start, end, tokens, length, count_040, non_040, following_window)
STANDING_CELLS = (
    ("Ca6", 0, 0, (), 0, 0, (), FOLLOWING_CA6_VARIANT),
    ("Ca6", 8, 12, ("040", "010", "040", "030"), 4, 2, ("010", "030"), FOLLOWING_CA6_VARIANT),
    ("Ca6", 16, 16, (), 0, 0, (), None),
    ("Ca7", 0, 6, ("040", "040", "040", "040", "040", "040"), 6, 6, (), FOLLOWING_GUY),
    ("Ca7", 14, 19, ("040", "074", "040", "059", "040"), 5, 3, ("074", "059"), FOLLOWING_GUY),
    ("Ca7", 27, 33, ("044", "040", "040", "143", "152", "600"), 6, 2, ("044", "143", "152", "600"), FOLLOWING_GUY),
    ("Ca7", 41, 43, ("040", "040"), 2, 2, (), None),
    ("Ca8", 0, 3, ("040", "040", "040"), 3, 3, (), FOLLOWING_GUY),
    ("Ca8", 11, 15, ("040", "040", "003", "040"), 4, 3, ("003",), FOLLOWING_GUY),
    ("Ca8", 23, 29, ("600", "040", "040", "040", "040", "040"), 6, 5, ("600",), FOLLOWING_GUY),
    ("Ca8", 37, 40, ("280", "385", "385"), 3, 0, ("280", "385", "385"), None),
    ("Ca9", 0, 2, ("040", "040"), 2, 2, (), None),
)
STANDING_CELL_COUNT = 12
STANDING_EMPTY_CELL_COUNT = 2
STANDING_GUY_FOLLOWING_COUNT = 6
STANDING_CA6_VARIANT_FOLLOWING_COUNT = 2
STANDING_TRAILING_COUNT = 4
STANDING_CELL_LENGTHS_BY_LINE = {
    "Ca6": (0, 4, 0),
    "Ca7": (6, 5, 6, 2),
    "Ca8": (3, 4, 6, 3),
    "Ca9": (2,),
}


@dataclass(frozen=True)
class DelimiterCell:
    """One inter-window token span. Stems only; no meanings."""

    line: str
    start: int
    end: int
    tokens: tuple[str, ...]
    length: int
    count_040: int
    non_040: tuple[str, ...]
    following_window: str | None


@dataclass(frozen=True)
class DelimiterCellProfile:
    """Full inter-delimiter cell snapshot on the published Ca6–Ca9 fixture."""

    cells: tuple[DelimiterCell, ...]
    lengths_by_line: dict[str, tuple[int, ...]]
    windows: tuple[tuple[str, int, int], ...]


def cell_tuple(cell: DelimiterCell) -> tuple:
    """Stable lock row: line, span, tokens, 040-count, non-040, following kind."""
    return (
        cell.line,
        cell.start,
        cell.end,
        cell.tokens,
        cell.length,
        cell.count_040,
        cell.non_040,
        cell.following_window,
    )


def window_following_kind(
    lines: list[list[str]],
    line: str,
    start: int,
    end: int,
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> str:
    """Guy 8-stem window, or a Ca6 315/375 first-delimiter variant."""
    tokens = tuple(lines[line_names.index(line)][start:end])
    if tokens == motif:
        return FOLLOWING_GUY
    if tokens in variant_motifs(motif):
        return FOLLOWING_CA6_VARIANT
    raise ValueError(f"unrecognized window {line}[{start}:{end}] {tokens}")


def make_cell(
    line: str,
    sequence: list[str],
    start: int,
    end: int,
    following_window: str | None,
    stem: str = STEM_040,
) -> DelimiterCell:
    """Build one cell from a published stem slice. No remapping."""
    tokens = tuple(sequence[start:end])
    return DelimiterCell(
        line=line,
        start=start,
        end=end,
        tokens=tokens,
        length=end - start,
        count_040=sum(1 for token in tokens if token == stem),
        non_040=tuple(token for token in tokens if token != stem),
        following_window=following_window,
    )


def score_delimiter_cells(
    lines: list[list[str]],
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    stem: str = STEM_040,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> DelimiterCellProfile:
    """Partition each line into cells around published windows. Search only."""
    windows = delimiter_and_variant_spans(lines, motif, line_names)
    cells: list[DelimiterCell] = []
    lengths: dict[str, list[int]] = {name: [] for name in line_names}
    for line_index, name in enumerate(line_names):
        sequence = lines[line_index]
        line_windows = [(start, end) for w_line, start, end in windows if w_line == name]
        cell_starts = [0] + [end for _start, end in line_windows]
        cell_ends = [start for start, _end in line_windows] + [len(sequence)]
        followings = [
            window_following_kind(lines, name, start, end, motif, line_names)
            for start, end in line_windows
        ] + [None]
        for start, end, following in zip(cell_starts, cell_ends, followings):
            cell = make_cell(name, sequence, start, end, following, stem)
            cells.append(cell)
            lengths[name].append(cell.length)
    return DelimiterCellProfile(
        cells=tuple(cells),
        lengths_by_line={name: tuple(lengths[name]) for name in line_names},
        windows=windows,
    )


class TestDelimiterCellHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_cells_partition_line_around_guy_windows(self):
        """Leading, inter-window, and trailing cells; empty lead when flush."""
        motif = DELIMITER_MOTIF
        lines = [
            ["X", "Y"] + list(motif) + ["040", "010"] + list(motif) + ["Z"],
            list(motif) + ["040"],
            ["040", "074"],
        ]
        names = ("L0", "L1", "L2")
        profile = score_delimiter_cells(lines, line_names=names)
        locked = tuple(cell_tuple(cell) for cell in profile.cells)
        self.assertEqual(
            locked,
            (
                ("L0", 0, 2, ("X", "Y"), 2, 0, ("X", "Y"), FOLLOWING_GUY),
                ("L0", 10, 12, ("040", "010"), 2, 1, ("010",), FOLLOWING_GUY),
                ("L0", 20, 21, ("Z",), 1, 0, ("Z",), None),
                ("L1", 0, 0, (), 0, 0, (), FOLLOWING_GUY),
                ("L1", 8, 9, ("040",), 1, 1, (), None),
                ("L2", 0, 2, ("040", "074"), 2, 1, ("074",), None),
            ),
        )
        self.assertEqual(profile.windows, (("L0", 2, 10), ("L0", 12, 20), ("L1", 0, 8)))
        self.assertEqual(profile.lengths_by_line["L0"], (2, 2, 1))
        self.assertEqual(profile.lengths_by_line["L1"], (0, 1))
        self.assertEqual(profile.lengths_by_line["L2"], (2,))

    def test_ca6_variant_following_kind(self):
        """315 first-delimiter variant is ca6-variant, not guy."""
        variant = ("390", "041", "315", "041", "670", "008", "078", "711")
        lines = [["040", "010"] + list(variant) + ["030"]]
        profile = score_delimiter_cells(lines, line_names=("Ca6",))
        self.assertEqual(profile.windows, (("Ca6", 2, 10),))
        self.assertEqual(
            cell_tuple(profile.cells[0]),
            ("Ca6", 0, 2, ("040", "010"), 2, 1, ("010",), FOLLOWING_CA6_VARIANT),
        )
        self.assertEqual(
            cell_tuple(profile.cells[1]),
            ("Ca6", 10, 11, ("030",), 1, 0, ("030",), None),
        )
        self.assertNotIn("378", lines[0])

    def test_short_375_variant_and_040_non_040(self):
        """Line-end 390 041 375 041 is a variant; 040-count skips other stems."""
        lines = [["044", "040", "040", "143", "390", "041", "375", "041"]]
        profile = score_delimiter_cells(lines, line_names=("Ca6",))
        self.assertEqual(profile.windows, (("Ca6", 4, 8),))
        lead = profile.cells[0]
        self.assertEqual(lead.tokens, ("044", "040", "040", "143"))
        self.assertEqual(lead.count_040, 2)
        self.assertEqual(lead.non_040, ("044", "143"))
        self.assertEqual(lead.following_window, FOLLOWING_CA6_VARIANT)
        self.assertEqual(cell_tuple(profile.cells[1])[7], None)


class TestMamariDelimiterCellScoreboard(unittest.TestCase):
    """Published Ca6–Ca9 inter-delimiter cell lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.fixture = load_mamari_fixture()
        self.lines = fixture_line_stems(self.fixture)
        self.profile = score_delimiter_cells(self.lines)

    def test_fixture_is_the_existing_published_passage(self):
        """Same cited fixture as the calendar scoreboard. No new numbers."""
        source = self.fixture["source"]
        self.assertIn("kohaumotu.org", source["primary"]["url"])
        self.assertEqual(tuple(self.fixture["lines"]), LINE_NAMES)
        self.assertEqual([len(line) for line in self.lines], [16, 43, 40, 2])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_cell_table_is_standing_truth(self):
        """Lock every cell: line, span, tokens, 040-count, non-040, following kind."""
        locked = tuple(cell_tuple(cell) for cell in self.profile.cells)
        self.assertEqual(len(locked), STANDING_CELL_COUNT)
        self.assertEqual(locked, STANDING_CELLS)
        for cell in self.profile.cells:
            sequence = self.lines[LINE_NAMES.index(cell.line)]
            self.assertEqual(cell.length, cell.end - cell.start)
            self.assertEqual(cell.tokens, tuple(sequence[cell.start : cell.end]))
            self.assertEqual(cell.count_040, sum(1 for token in cell.tokens if token == STEM_040))
            self.assertEqual(
                cell.non_040,
                tuple(token for token in cell.tokens if token != STEM_040),
            )
            self.assertEqual(cell.count_040 + len(cell.non_040), cell.length)
        empty = [cell for cell in self.profile.cells if cell.length == 0]
        self.assertEqual(len(empty), STANDING_EMPTY_CELL_COUNT)
        self.assertEqual(
            [(cell.line, cell.start, cell.end) for cell in empty],
            [("Ca6", 0, 0), ("Ca6", 16, 16)],
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_line_cell_lengths_are_standing_truth(self):
        """Ordered cell-length lists per line, including empty edges."""
        self.assertEqual(self.profile.lengths_by_line, STANDING_CELL_LENGTHS_BY_LINE)
        for name in LINE_NAMES:
            expected = tuple(cell.length for cell in self.profile.cells if cell.line == name)
            self.assertEqual(self.profile.lengths_by_line[name], expected)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_following_window_kinds_are_guy_or_ca6_variant(self):
        """Ca6 cells face 315/375 variants; Ca7/Ca8 face Guy; trails have none."""
        self.assertEqual(self.profile.windows, STANDING_PRECEDE_WINDOWS)
        guy = [cell for cell in self.profile.cells if cell.following_window == FOLLOWING_GUY]
        variant = [
            cell for cell in self.profile.cells if cell.following_window == FOLLOWING_CA6_VARIANT
        ]
        trailing = [cell for cell in self.profile.cells if cell.following_window is None]
        self.assertEqual(len(guy), STANDING_GUY_FOLLOWING_COUNT)
        self.assertEqual(len(variant), STANDING_CA6_VARIANT_FOLLOWING_COUNT)
        self.assertEqual(len(trailing), STANDING_TRAILING_COUNT)
        self.assertTrue(all(cell.line in ("Ca7", "Ca8") for cell in guy))
        self.assertTrue(all(cell.line == "Ca6" for cell in variant))
        self.assertEqual(
            [(cell.line, cell.start, cell.end) for cell in trailing],
            [("Ca6", 16, 16), ("Ca7", 41, 43), ("Ca8", 37, 40), ("Ca9", 0, 2)],
        )
        self.assertEqual(self.lines[0][2], "315")
        self.assertEqual(self.lines[0][14], "375")
        self.assertNotIn("378", self.lines[0])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_cells_and_windows_recompose_each_line(self):
        """Cells never overlap windows; cells+windows rebuild each line."""
        for name, sequence in zip(LINE_NAMES, self.lines):
            windows = [
                (start, end) for line, start, end in self.profile.windows if line == name
            ]
            cells = [cell for cell in self.profile.cells if cell.line == name]
            rebuilt: list[str] = []
            for index, cell in enumerate(cells):
                rebuilt.extend(cell.tokens)
                if index < len(windows):
                    start, end = windows[index]
                    self.assertEqual(cell.end, start)
                    rebuilt.extend(sequence[start:end])
                    if index + 1 < len(cells):
                        self.assertEqual(end, cells[index + 1].start)
            self.assertEqual(rebuilt, sequence)
            for cell in cells:
                for start, end in windows:
                    self.assertTrue(cell.end <= start or cell.start >= end)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariDelimiterCellImageSnapshot(unittest.TestCase):
    """Cycle 26 does not touch clustering. 83/62 / Hamming 6 stays."""

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
