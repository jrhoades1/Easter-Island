"""Published Barthel 040-run profile: Ca6–Ca9 maximal 040 sequences.

Cycle 25 text-search lock. Uses only the existing Kohaumotu / Guy
fixture (tests/fixtures/mamari_ca6_ca9_barthel.json). No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.

A run is a maximal consecutive 040 sequence. Each run locks line,
[start, end), length, and whether it immediately precedes a published
Guy delimiter window or a Ca6 315/375 first-delimiter variant. Also
locks the ordered list of run lengths per line.

040 is the published stem only. No lunar reading. Search lock, not a
merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from processors.glyph_processor import min_pairwise_window_hamming
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
from tests.test_mamari_position_alignment_scoreboard import (
    delimiter_spans,
    find_ngram_hits,
    published_ca7_ca8_stems,
)
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_UNIQUE_CLUSTERS,
    published_ca7_ca8_stem_counts,
    score_type_identity,
)

LINE_NAMES = ("Ca6", "Ca7", "Ca8", "Ca9")
STEM_040 = "040"
# Published first-delimiter substitutes for Guy's 378 slot. Fixture tokens.
FIRST_DELIMITER_VARIANTS = ("315", "375")

# (line, start, end, length, precedes_delimiter)
STANDING_040_RUNS = (
    ("Ca6", 8, 9, 1, False),
    ("Ca6", 10, 11, 1, False),
    ("Ca7", 0, 6, 6, True),
    ("Ca7", 14, 15, 1, False),
    ("Ca7", 16, 17, 1, False),
    ("Ca7", 18, 19, 1, True),
    ("Ca7", 28, 30, 2, False),
    ("Ca7", 41, 43, 2, False),
    ("Ca8", 0, 3, 3, True),
    ("Ca8", 11, 13, 2, False),
    ("Ca8", 14, 15, 1, True),
    ("Ca8", 24, 29, 5, True),
    ("Ca9", 0, 2, 2, False),
)
STANDING_040_RUN_COUNT = 13
STANDING_PRECEDING_DELIMITER_COUNT = 5
STANDING_RUN_LENGTHS_BY_LINE = {
    "Ca6": (1, 1),
    "Ca7": (6, 1, 1, 1, 2, 2),
    "Ca8": (3, 2, 1, 5),
    "Ca9": (2,),
}
# Guy 8-stems plus Ca6 315 (full 8) and 375 (short 4 at line end).
STANDING_PRECEDE_WINDOWS = (
    ("Ca6", 0, 8),
    ("Ca6", 12, 16),
    ("Ca7", 6, 14),
    ("Ca7", 19, 27),
    ("Ca7", 33, 41),
    ("Ca8", 3, 11),
    ("Ca8", 15, 23),
    ("Ca8", 29, 37),
)


@dataclass(frozen=True)
class Run040:
    """One maximal consecutive 040 span. Stems only; no meanings."""

    line: str
    start: int
    end: int
    length: int
    precedes_delimiter: bool


@dataclass(frozen=True)
class Run040Profile:
    """Full 040-run snapshot on the published Ca6–Ca9 fixture."""

    runs: tuple[Run040, ...]
    lengths_by_line: dict[str, tuple[int, ...]]
    windows: tuple[tuple[str, int, int], ...]


def run_tuple(run: Run040) -> tuple:
    """Stable lock row: line, span, length, precedes-delimiter."""
    return (run.line, run.start, run.end, run.length, run.precedes_delimiter)


def variant_motifs(
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    variants: tuple[str, ...] = FIRST_DELIMITER_VARIANTS,
) -> tuple[tuple[str, ...], ...]:
    """Guy motif with 315 or 375 in the 378 slot. Full 8, then short 4."""
    slot = motif.index("378")
    short_end = slot + 2
    rows: list[tuple[str, ...]] = []
    for variant in variants:
        rows.append(motif[:slot] + (variant,) + motif[slot + 1 :])
        rows.append(motif[:slot] + (variant,) + motif[slot + 1 : short_end])
    return tuple(rows)


def delimiter_and_variant_spans(
    lines: list[list[str]],
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> tuple[tuple[str, int, int], ...]:
    """Guy windows plus Ca6 315/375 first-delimiter variants. Longer wins."""
    starts: set[tuple[int, int]] = set()
    spans: list[tuple[str, int, int]] = []
    for line_index, start, end in delimiter_spans(lines, motif):
        starts.add((line_index, start))
        spans.append((line_names[line_index], start, end))
    for gram in variant_motifs(motif):
        n = len(gram)
        for line_index, start in find_ngram_hits(lines, gram):
            if (line_index, start) in starts:
                continue
            starts.add((line_index, start))
            spans.append((line_names[line_index], start, start + n))
    spans.sort(key=lambda row: (line_names.index(row[0]), row[1], row[2]))
    return tuple(spans)


def find_040_runs(
    lines: list[list[str]],
    stem: str = STEM_040,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> tuple[tuple[str, int, int, int], ...]:
    """Maximal consecutive 040 spans: (line, start, end, length)."""
    runs: list[tuple[str, int, int, int]] = []
    for line_index, sequence in enumerate(lines):
        i = 0
        n = len(sequence)
        while i < n:
            if sequence[i] != stem:
                i += 1
                continue
            start = i
            while i < n and sequence[i] == stem:
                i += 1
            runs.append((line_names[line_index], start, i, i - start))
    return tuple(runs)


def run_precedes_window(
    line: str,
    end: int,
    windows: tuple[tuple[str, int, int], ...] | list[tuple[str, int, int]],
) -> bool:
    """True if a published window starts on this line at end."""
    return any(w_line == line and w_start == end for w_line, w_start, _w_end in windows)


def score_040_run_profile(
    lines: list[list[str]],
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    stem: str = STEM_040,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> Run040Profile:
    """Build the 040-run profile. Search only; no type map."""
    windows = delimiter_and_variant_spans(lines, motif, line_names)
    runs = []
    lengths: dict[str, list[int]] = {name: [] for name in line_names}
    for line, start, end, length in find_040_runs(lines, stem, line_names):
        precedes = run_precedes_window(line, end, windows)
        runs.append(
            Run040(
                line=line,
                start=start,
                end=end,
                length=length,
                precedes_delimiter=precedes,
            )
        )
        lengths[line].append(length)
    return Run040Profile(
        runs=tuple(runs),
        lengths_by_line={name: tuple(lengths[name]) for name in line_names},
        windows=windows,
    )


class Test040RunProfileHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_maximal_runs_and_gaps(self):
        """Adjacent 040s merge; a gap splits; non-040 lines are empty."""
        lines = [
            ["040", "040", "040", "X"],
            ["040", "X", "040"],
            ["390", "041"],
        ]
        runs = find_040_runs(lines, line_names=("L0", "L1", "L2"))
        self.assertEqual(
            runs,
            (
                ("L0", 0, 3, 3),
                ("L1", 0, 1, 1),
                ("L1", 2, 3, 1),
            ),
        )

    def test_precedes_guy_window_and_ca6_variant(self):
        """Immediate 390 start is True; a gap before the window is False."""
        motif = DELIMITER_MOTIF
        variant = ("390", "041", "315", "041", "670", "008", "078", "711")
        lines = [
            ["040", "040"] + list(motif),
            ["040", "X"] + list(motif),
            ["040"] + list(variant),
        ]
        names = ("Ca7", "Ca8", "Ca6")
        profile = score_040_run_profile(lines, line_names=names)
        locked = tuple(run_tuple(run) for run in profile.runs)
        self.assertEqual(
            locked,
            (
                ("Ca7", 0, 2, 2, True),
                ("Ca8", 0, 1, 1, False),
                ("Ca6", 0, 1, 1, True),
            ),
        )
        self.assertIn(("Ca6", 1, 9), profile.windows)
        self.assertIn(("Ca7", 2, 10), profile.windows)
        self.assertEqual(profile.lengths_by_line["Ca7"], (2,))
        self.assertEqual(profile.lengths_by_line["Ca8"], (1,))
        self.assertEqual(profile.lengths_by_line["Ca6"], (1,))

    def test_short_375_variant_counts_as_window(self):
        """Line-end 390 041 375 041 is a first-delimiter variant."""
        lines = [["040", "390", "041", "375", "041"]]
        profile = score_040_run_profile(lines, line_names=("Ca6",))
        self.assertEqual(profile.windows, (("Ca6", 1, 5),))
        self.assertEqual(run_tuple(profile.runs[0]), ("Ca6", 0, 1, 1, True))
        self.assertNotIn("378", lines[0])


class TestMamari040RunProfileScoreboard(unittest.TestCase):
    """Published Ca6–Ca9 040-run lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.fixture = load_mamari_fixture()
        self.lines = fixture_line_stems(self.fixture)
        self.profile = score_040_run_profile(self.lines)

    def test_fixture_is_the_existing_published_passage(self):
        """Same cited fixture as the calendar scoreboard. No new numbers."""
        source = self.fixture["source"]
        self.assertIn("kohaumotu.org", source["primary"]["url"])
        self.assertEqual(tuple(self.fixture["lines"]), LINE_NAMES)
        self.assertEqual([len(line) for line in self.lines], [16, 43, 40, 2])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_run_table_is_standing_truth(self):
        """Lock every maximal 040 run: line, span, length, precedes-delimiter."""
        locked = tuple(run_tuple(run) for run in self.profile.runs)
        self.assertEqual(len(locked), STANDING_040_RUN_COUNT)
        self.assertEqual(locked, STANDING_040_RUNS)
        for run in self.profile.runs:
            self.assertEqual(run.length, run.end - run.start)
            self.assertGreater(run.length, 0)
            self.assertEqual(
                self.lines[LINE_NAMES.index(run.line)][run.start : run.end],
                [STEM_040] * run.length,
            )
            if run.end < len(self.lines[LINE_NAMES.index(run.line)]):
                self.assertNotEqual(
                    self.lines[LINE_NAMES.index(run.line)][run.end],
                    STEM_040,
                )
        preceding = [run for run in self.profile.runs if run.precedes_delimiter]
        self.assertEqual(len(preceding), STANDING_PRECEDING_DELIMITER_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_line_run_lengths_are_standing_truth(self):
        """Ordered run-length lists per line. Empty if a line had no 040."""
        self.assertEqual(self.profile.lengths_by_line, STANDING_RUN_LENGTHS_BY_LINE)
        for name in LINE_NAMES:
            expected = tuple(
                run.length for run in self.profile.runs if run.line == name
            )
            self.assertEqual(self.profile.lengths_by_line[name], expected)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_precede_windows_include_guy_and_ca6_variants(self):
        """Guy 8-stems plus Ca6 315/375 variants; no run precedes Ca6 variants."""
        self.assertEqual(self.profile.windows, STANDING_PRECEDE_WINDOWS)
        ca6 = [w for w in self.profile.windows if w[0] == "Ca6"]
        self.assertEqual(ca6, [("Ca6", 0, 8), ("Ca6", 12, 16)])
        self.assertEqual(self.lines[0][2], "315")
        self.assertEqual(self.lines[0][14], "375")
        self.assertNotIn("378", self.lines[0])
        ca6_runs = [run for run in self.profile.runs if run.line == "Ca6"]
        self.assertTrue(all(not run.precedes_delimiter for run in ca6_runs))
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamari040RunImageSnapshot(unittest.TestCase):
    """Cycle 25 does not touch clustering. 83/62 / Hamming 6 stays."""

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
