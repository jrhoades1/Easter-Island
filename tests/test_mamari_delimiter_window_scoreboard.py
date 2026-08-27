"""Delimiter-window scoreboard: slot identity across published Ca7/Ca8 hits.

Not a G00n→Barthel type map. At each published Guy delimiter occurrence
on Ca7/Ca8, take the eight image G00n IDs in those same reading-order
slots (390 041 378 041 670 008 078 711). A slot matches if every
repetition has the same G00n ID there. Score is 0–8.

Cycle 13 crop-compares the four slot-0 leftovers (NCC / chamfer on the
bbox image). None pass, so the lock stays 0/8.

Cycle 14 is an alignment search, not a merge: joint offsets of the
published window STARTS on the existing G00n sequence. Best offset is
0. Slot matches stay 0/8.

Cycle 15 applies the keep-ID gate globally after DBSCAN (Hu < 2.0,
r ≥ 0.85 when profiles exist). Types 64→62. Slot matches stay 0/8;
slot unique stays (4, 6, 6, 6, 5, 6, 6, 5). The gate is not lowered.
Cycle 16 found no honest higher-res public Ca7–Ca8 raster; GIF
ceiling, lock unchanged. Cycle 17 searches the full G00n sequence
(not these six windows) and still finds no repeating 8-gram.
Cycle 18 locked nearest 8-window Hamming among these six at 7
(first pair Ca7[6:14] vs Ca8[3:11]); concat min is 3.
Cycle 19 merges one leftover crop pair that drops published
Hamming to 6 (slot 7: Ca7[26] vs Ca8[22]). Cycle 20 applies the
other two crop-passing leftovers together (slot 2 and slot 3);
published min stays 6, so those extra merges stay off.
Glyph meanings are not assigned.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from models.glyphs import GlyphInstance
from tests.test_mamari_calendar_scoreboard import DELIMITER_MOTIF
from processors.glyph_processor import (
    GlyphProcessor,
    ProcessorConfig,
    _hu_distance,
    crop_chamfer,
    crop_ncc,
    leftover_crop_pairs,
    min_pairwise_window_hamming,
    passes_delimiter_slot_gates,
    passes_slot_crop_gates,
    passes_type_consistency_gates,
    passes_wide_profile_allograph_gates,
    profile_correlation,
    remap_window_types,
)
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_neighbor_allograph_scoreboard import (
    ca7_ca8_instances,
    longest_mixed_repeating_n,
)
from tests.test_mamari_position_alignment_scoreboard import (
    LINE_NAMES,
    delimiter_spans,
    published_ca7_ca8_stems,
)
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_MIXED_REPEATING,
    STANDING_UNIQUE_CLUSTERS,
    mixed_repeating_ngrams,
)

WINDOW_LEN = len(DELIMITER_MOTIF)

# Six published delimiter occurrences on Ca7/Ca8 (3 + 3).
STANDING_DELIMITER_WINDOWS = (
    ("Ca7", 6, 14, ("G004", "G021", "G020", "G019", "G015", "G018", "G016", "G017")),
    ("Ca7", 19, 27, ("G023", "G026", "G022", "G033", "G005", "G034", "G035", "G003")),
    ("Ca7", 33, 41, ("G006", "G043", "G039", "G042", "G036", "G040", "G009", "G041")),
    ("Ca8", 3, 11, ("G004", "G011", "G013", "G047", "G049", "G009", "G012", "G003")),
    ("Ca8", 15, 23, ("G006", "G052", "G014", "G051", "G005", "G012", "G050", "G003")),
    ("Ca8", 29, 37, ("G011", "G013", "G060", "G061", "G014", "G055", "G057", "G054")),
)
STANDING_WINDOW_COUNT = 6
STANDING_SLOT_MATCHES = 0
# Pairwise slot merges that passed Hu/profile or the cycle-19 crop
# Hamming gate. No slot is unanimous.
STANDING_MERGED_SLOTS = (0, 4, 7)
STANDING_SLOT_UNIQUE_COUNTS = (4, 6, 6, 6, 5, 6, 6, 4)
# Slot-0 reading-order occupants (line, index). Four unique IDs remain.
SLOT0_OCCUPANTS = (
    ("Ca7", 6),
    ("Ca7", 19),
    ("Ca7", 33),
    ("Ca8", 3),
    ("Ca8", 15),
    ("Ca8", 29),
)
# (left, right, ncc, chamfer, column-ink r, crop_pass, already_merged)
# NCC/chamfer from the stored 64x64 bbox crop. Merged-pair floor is
# 0.504 / 0.544; leftover ceiling is 0.229 / 1.017. Column-ink leftover
# max r 0.584 is below the 0.70 adjacent-nonmatch ceiling — r stays 0.85.
STANDING_SLOT0_CROP_PAIRS = (
    (("Ca7", 6), ("Ca7", 19), 0.055, 1.860, 0.348, False, False),
    (("Ca7", 6), ("Ca7", 33), 0.214, 1.241, 0.502, False, False),
    (("Ca7", 6), ("Ca8", 3), 0.504, 0.544, 0.944, True, True),
    (("Ca7", 6), ("Ca8", 15), 0.198, 1.222, 0.523, False, False),
    (("Ca7", 6), ("Ca8", 29), 0.081, 1.620, 0.181, False, False),
    (("Ca7", 19), ("Ca7", 33), -0.010, 1.756, 0.071, False, False),
    (("Ca7", 19), ("Ca8", 3), 0.072, 1.892, 0.289, False, False),
    (("Ca7", 19), ("Ca8", 15), -0.009, 1.760, 0.125, False, False),
    (("Ca7", 19), ("Ca8", 29), -0.051, 2.385, -0.111, False, False),
    (("Ca7", 33), ("Ca8", 3), 0.209, 1.214, 0.504, False, False),
    (("Ca7", 33), ("Ca8", 15), 0.909, 0.117, 0.991, True, True),
    (("Ca7", 33), ("Ca8", 29), 0.157, 1.017, 0.584, False, False),
    (("Ca8", 3), ("Ca8", 15), 0.229, 1.194, 0.524, False, False),
    (("Ca8", 3), ("Ca8", 29), 0.057, 1.838, 0.217, False, False),
    (("Ca8", 15), ("Ca8", 29), 0.144, 1.068, 0.541, False, False),
)
# Cycle 19: leftover same-slot crop pairs that clear NCC/chamfer.
# Only slot 7 Ca7[26] vs Ca8[22] also drops published min Hamming.
# Cycle 20: slot 2 + slot 3 together still leave min Hamming at 6.
# (slot, left, right, ncc, chamfer, r, crop_pass, drops_hamming)
STANDING_CROP_HAMMING_CANDIDATES = (
    (7, ("Ca7", 26), ("Ca8", 22), 0.700, 0.357, 0.882, True, True),
    (2, ("Ca7", 8), ("Ca8", 31), 0.640, 0.548, 0.753, True, False),
    (3, ("Ca7", 9), ("Ca8", 32), 0.470, 0.784, 0.735, True, False),
)
STANDING_CROP_HAMMING_MERGE = STANDING_CROP_HAMMING_CANDIDATES[0]
STANDING_LEFTOVER_CROP_PAIRS = STANDING_CROP_HAMMING_CANDIDATES[1:]

# Joint stem-index offsets applied to every published start. Same N
# for all six windows. Per-window free search would mix slots.
WINDOW_OFFSETS = (-2, -1, 0, 1, 2)
PUBLISHED_WINDOW_STARTS = (
    (0, 6),
    (0, 19),
    (0, 33),
    (1, 3),
    (1, 15),
    (1, 29),
)
# Joint offset table on the standing G00n sequence. Every offset is
# 0/8. Offset 0 is uniquely best (mean unique 5.375); -2 / -1 are
# 5.500; +1 / +2 are 5.625 after the slot-7 crop merge.
# (offset, matches, unique-count 8-tuple)
STANDING_OFFSET_TABLE = (
    (-2, 0, (6, 5, 4, 6, 6, 6, 5, 6)),
    (-1, 0, (5, 4, 6, 6, 6, 5, 6, 6)),
    (0, 0, (4, 6, 6, 6, 5, 6, 6, 4)),
    (1, 0, (6, 6, 6, 5, 6, 6, 4, 6)),
    (2, 0, (6, 6, 5, 6, 6, 4, 6, 6)),
)
STANDING_BEST_OFFSET = 0
STANDING_BEST_OFFSET_MATCHES = 0
STANDING_BEST_OFFSET_UNIQUE_COUNTS = STANDING_SLOT_UNIQUE_COUNTS


@dataclass(frozen=True)
class DelimiterWindow:
    """One published delimiter span with the aligned image G00n IDs."""

    line: str
    start: int
    end: int
    image_ids: tuple[str, ...]
    published_stems: tuple[str, ...]


@dataclass(frozen=True)
class DelimiterWindowScore:
    """How many of the 8 delimiter slots share a G00n ID across hits."""

    windows: tuple[DelimiterWindow, ...]
    slot_ids: tuple[tuple[str, ...], ...]
    slot_matches: int
    instance_count: int
    unique_cluster_count: int
    ca7_length: int
    ca8_length: int


def delimiter_image_windows(
    image_lines: list[list[str]],
    published_lines: list[list[str]],
    motif: tuple[str, ...] = DELIMITER_MOTIF,
) -> list[DelimiterWindow]:
    """Image G00n windows at published delimiter indexes. No type map."""
    if len(image_lines) != len(published_lines):
        raise ValueError("image and published line counts differ")
    for image, published in zip(image_lines, published_lines):
        if len(image) != len(published):
            raise ValueError("image and published stem lengths differ")

    windows: list[DelimiterWindow] = []
    for line_index, start, end in delimiter_spans(published_lines, motif):
        windows.append(
            DelimiterWindow(
                line=LINE_NAMES[line_index],
                start=start,
                end=end,
                image_ids=tuple(image_lines[line_index][start:end]),
                published_stems=tuple(published_lines[line_index][start:end]),
            )
        )
    return windows


def slot_ids_across_windows(
    windows: list[DelimiterWindow] | tuple[DelimiterWindow, ...],
    window_len: int = WINDOW_LEN,
) -> tuple[tuple[str, ...], ...]:
    """Per-slot G00n IDs, one tuple per delimiter slot."""
    return tuple(
        tuple(window.image_ids[slot] for window in windows) for slot in range(window_len)
    )


def slot_match_count(slot_ids: tuple[tuple[str, ...], ...]) -> int:
    """How many slots have one G00n ID across every repetition (0–8)."""
    return sum(1 for ids in slot_ids if len(set(ids)) == 1)


def window_tuple(window: DelimiterWindow) -> tuple:
    """Stable lock row: line, span, image IDs."""
    return (window.line, window.start, window.end, window.image_ids)


@dataclass(frozen=True)
class WindowOffsetRow:
    """Slot identity at one joint start offset. No re-clustering."""

    offset: int
    starts: tuple[tuple[int, int], ...]
    slot_matches: int
    unique_counts: tuple[int, ...]
    mean_unique: float
    in_bounds: bool


def shift_window_starts(
    starts: tuple[tuple[int, int], ...],
    offset: int,
) -> tuple[tuple[int, int], ...]:
    """Add the same stem-index offset to every published start."""
    return tuple((line, start + offset) for line, start in starts)


def windows_in_bounds(
    image_lines: list[list[str]],
    starts: tuple[tuple[int, int], ...],
    window_len: int = WINDOW_LEN,
) -> bool:
    """True if every shifted 8-slot window sits inside its line."""
    for line, start in starts:
        if line < 0 or line >= len(image_lines):
            return False
        seq = image_lines[line]
        if start < 0 or start + window_len > len(seq):
            return False
    return True


def windows_at_starts(
    image_lines: list[list[str]],
    starts: tuple[tuple[int, int], ...],
    window_len: int = WINDOW_LEN,
    published_lines: list[list[str]] | None = None,
) -> list[DelimiterWindow]:
    """G00n 8-slots at given starts. Existing sequence only."""
    windows: list[DelimiterWindow] = []
    for line, start in starts:
        end = start + window_len
        stems: tuple[str, ...] = ()
        if published_lines is not None:
            stems = tuple(published_lines[line][start:end])
        windows.append(
            DelimiterWindow(
                line=LINE_NAMES[line],
                start=start,
                end=end,
                image_ids=tuple(image_lines[line][start:end]),
                published_stems=stems,
            )
        )
    return windows


def score_window_offset(
    image_lines: list[list[str]],
    starts: tuple[tuple[int, int], ...] = PUBLISHED_WINDOW_STARTS,
    offset: int = 0,
    window_len: int = WINDOW_LEN,
) -> WindowOffsetRow:
    """Slot matches and unique counts at one joint offset."""
    shifted = shift_window_starts(starts, offset)
    if not windows_in_bounds(image_lines, shifted, window_len):
        empty = (0,) * window_len
        return WindowOffsetRow(offset, shifted, 0, empty, float("inf"), False)
    windows = windows_at_starts(image_lines, shifted, window_len)
    slots = slot_ids_across_windows(windows, window_len)
    unique = tuple(len(set(ids)) for ids in slots)
    return WindowOffsetRow(
        offset=offset,
        starts=shifted,
        slot_matches=slot_match_count(slots),
        unique_counts=unique,
        mean_unique=sum(unique) / len(unique),
        in_bounds=True,
    )


def sweep_window_offsets(
    image_lines: list[list[str]],
    starts: tuple[tuple[int, int], ...] = PUBLISHED_WINDOW_STARTS,
    offsets: tuple[int, ...] = WINDOW_OFFSETS,
    window_len: int = WINDOW_LEN,
) -> tuple[WindowOffsetRow, ...]:
    """Score every joint offset on the existing G00n sequence."""
    return tuple(
        score_window_offset(image_lines, starts, offset, window_len)
        for offset in offsets
    )


def best_window_offset(
    rows: tuple[WindowOffsetRow, ...] | list[WindowOffsetRow],
) -> WindowOffsetRow:
    """Max slot matches, then min mean unique IDs. Tie → offset 0."""
    valid = [row for row in rows if row.in_bounds]
    if not valid:
        raise ValueError("no in-bounds window offsets")
    return min(
        valid,
        key=lambda row: (
            -row.slot_matches,
            row.mean_unique,
            abs(row.offset),
            row.offset,
        ),
    )


def offset_table_tuple(
    rows: tuple[WindowOffsetRow, ...] | list[WindowOffsetRow],
) -> tuple[tuple[int, int, tuple[int, ...]], ...]:
    """Lock row: offset, matches, unique-count 8-tuple."""
    return tuple((row.offset, row.slot_matches, row.unique_counts) for row in rows)


def slot0_instance(lines: list[list], line: str, index: int):
    """Slot-0 occupant at a published Ca7/Ca8 reading-order index."""
    return lines[0 if line == "Ca7" else 1][index]


def slot0_crop_row(left, right) -> tuple:
    """(ncc, chamfer, column-ink r, crop_pass, already_same_id)."""
    return (
        crop_ncc(left.glyph_crop, right.glyph_crop),
        crop_chamfer(left.glyph_crop, right.glyph_crop),
        profile_correlation(left.ink_profile, right.ink_profile),
        passes_slot_crop_gates(left, right),
        left.cluster_id == right.cluster_id,
    )


def score_delimiter_windows(
    instances: list[GlyphInstance],
    image_lines: list[list[str]],
    published_lines: list[list[str]],
) -> DelimiterWindowScore:
    """Record slot matches plus the standing 83/64 / 43+40 lock."""
    windows = delimiter_image_windows(image_lines, published_lines)
    slots = slot_ids_across_windows(windows)
    cluster_ids = [inst.cluster_id for inst in instances if inst.cluster_id]
    return DelimiterWindowScore(
        windows=tuple(windows),
        slot_ids=slots,
        slot_matches=slot_match_count(slots),
        instance_count=len(cluster_ids),
        unique_cluster_count=len(set(cluster_ids)),
        ca7_length=len(image_lines[0]) if image_lines else 0,
        ca8_length=len(image_lines[1]) if len(image_lines) > 1 else 0,
    )


class TestDelimiterWindowHelpers(unittest.TestCase):
    """Helpers on synthetic windows. No CV, no LLM."""

    def test_slot_match_count_is_unanimous_identity(self):
        windows = [
            DelimiterWindow(
                "Ca7",
                0,
                8,
                ("A", "B", "C", "D", "E", "F", "G", "H"),
                DELIMITER_MOTIF,
            ),
            DelimiterWindow(
                "Ca8",
                0,
                8,
                ("A", "B", "X", "D", "Y", "F", "G", "Z"),
                DELIMITER_MOTIF,
            ),
        ]
        slots = slot_ids_across_windows(windows)
        self.assertEqual(slot_match_count(slots), 5)
        self.assertEqual(slots[0], ("A", "A"))
        self.assertEqual(slots[2], ("C", "X"))

    def test_all_distinct_slots_score_zero(self):
        windows = [
            DelimiterWindow("Ca7", 0, 8, tuple(f"L{i}" for i in range(8)), DELIMITER_MOTIF),
            DelimiterWindow("Ca8", 0, 8, tuple(f"R{i}" for i in range(8)), DELIMITER_MOTIF),
        ]
        self.assertEqual(slot_match_count(slot_ids_across_windows(windows)), 0)

    def test_windows_follow_published_spans(self):
        image = [
            ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "X"],
            ["Y", "A", "B", "C", "D", "E", "F", "G", "H"],
        ]
        published = [
            list(DELIMITER_MOTIF) + ["040"],
            ["040"] + list(DELIMITER_MOTIF),
        ]
        windows = delimiter_image_windows(image, published)
        self.assertEqual(
            [window_tuple(window) for window in windows],
            [
                ("Ca7", 0, 8, ("G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8")),
                ("Ca8", 1, 9, ("A", "B", "C", "D", "E", "F", "G", "H")),
            ],
        )
        self.assertTrue(all(window.published_stems == DELIMITER_MOTIF for window in windows))

    def test_joint_offset_shifts_every_start(self):
        starts = ((0, 6), (1, 3))
        self.assertEqual(shift_window_starts(starts, -2), ((0, 4), (1, 1)))
        self.assertEqual(shift_window_starts(starts, 2), ((0, 8), (1, 5)))
        self.assertTrue(windows_in_bounds([["x"] * 16, ["y"] * 16], ((0, 0), (1, 8))))
        self.assertFalse(windows_in_bounds([["x"] * 10], ((0, 3),)))

    def test_best_offset_prefers_matches_then_mean_unique(self):
        def _row(offset, matches, unique):
            mean = sum(unique) / len(unique)
            return WindowOffsetRow(offset, ((0, offset),), matches, unique, mean, True)

        table = (
            _row(-1, 0, (6, 6, 6, 6, 6, 6, 6, 6)),
            _row(0, 1, (5, 6, 6, 6, 6, 6, 6, 6)),
            _row(1, 1, (4, 4, 4, 4, 4, 4, 4, 4)),
        )
        best = best_window_offset(table)
        self.assertEqual(best.offset, 1)
        self.assertEqual(best.slot_matches, 1)
        tied = (
            _row(-2, 0, (5, 5, 5, 5, 5, 5, 5, 5)),
            _row(0, 0, (5, 5, 5, 5, 5, 5, 5, 5)),
            _row(2, 0, (5, 5, 5, 5, 5, 5, 5, 5)),
        )
        self.assertEqual(best_window_offset(tied).offset, 0)


class TestMamariDelimiterWindowScoreboard(unittest.TestCase):
    """Stock CV IDs at published Ca7/Ca8 delimiter spans. MockProvider only."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.published_lines = published_ca7_ca8_stems()
        self.score = score_delimiter_windows(
            self.instances, self.image_lines, self.published_lines
        )

    def test_cycle13_snapshot(self):
        """PR snapshot: 83/62 / 43+40, two mixed 2-grams, no 8-gram, slots 0/8."""
        s = self.score
        self.assertEqual(s.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(s.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(s.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(s.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(
            mixed_repeating_ngrams(self.image_lines, self.ngram_analyzer),
            list(STANDING_MIXED_REPEATING),
        )
        self.assertEqual(
            longest_mixed_repeating_n(self.image_lines, self.ngram_analyzer), 2
        )
        eight = self.ngram_analyzer.extract_ngrams(
            self.image_lines, n=8, min_frequency=2
        )
        self.assertEqual(eight, [])
        self.assertEqual(s.slot_matches, STANDING_SLOT_MATCHES)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_joint_window_offset_sweep_locks_best(self):
        """Best joint start offset on the existing G00n sequence.

        Alignment search, not a merge. Same offset for all six published
        starts. Clustering stays put. -2 / -1 / 0 all score 0/8 with
        mean unique 5.500; 0 wins the tie. Default starts stay put
        because no offset has matches > 0.
        """
        rows = sweep_window_offsets(self.image_lines)
        table = offset_table_tuple(rows)
        best = best_window_offset(rows)
        self.assertEqual(table, STANDING_OFFSET_TABLE)
        self.assertEqual(best.offset, STANDING_BEST_OFFSET)
        self.assertEqual(best.slot_matches, STANDING_BEST_OFFSET_MATCHES)
        self.assertEqual(best.unique_counts, STANDING_BEST_OFFSET_UNIQUE_COUNTS)
        self.assertEqual(best.slot_matches, STANDING_SLOT_MATCHES)
        self.assertTrue(all(row.in_bounds for row in rows))
        self.assertEqual(
            [row.offset for row in rows],
            list(WINDOW_OFFSETS),
        )
        # Default pipeline starts stay at the published indexes.
        self.assertEqual(best.offset, 0)
        self.assertEqual(best.starts, PUBLISHED_WINDOW_STARTS)
        self.assertEqual(
            ProcessorConfig().delimiter_window_starts,
            PUBLISHED_WINDOW_STARTS,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_published_windows_are_guys_delimiter(self):
        """Each Ca7/Ca8 published span is exactly the 8-stem motif."""
        s = self.score
        self.assertEqual(len(s.windows), STANDING_WINDOW_COUNT)
        self.assertEqual(len(s.windows), len(STANDING_DELIMITER_WINDOWS))
        for window in s.windows:
            self.assertEqual(window.published_stems, DELIMITER_MOTIF)
            self.assertEqual(len(window.image_ids), WINDOW_LEN)
        self.assertEqual(
            [window_tuple(window) for window in s.windows],
            list(STANDING_DELIMITER_WINDOWS),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_delimiter_slot_matches_are_standing_truth(self):
        """0 of 8 slots share one G00n ID across the six repetitions.

        Cycle 12 merged passing pairs in slots 0, 4, and 7. Cycle 13
        crop-compared the four slot-0 IDs; leftovers fail NCC/chamfer.
        Cycle 15 global keep-ID clustering drops two types and does not
        make any slot unanimous; unique count stays 4 and matches stay
        0/8. Do not force a leftover occupant onto the merged pair and
        do not lower the gate. If a later change makes any slot
        unanimous, raise STANDING_SLOT_MATCHES. Not a type map.
        """
        s = self.score
        self.assertEqual(s.slot_matches, STANDING_SLOT_MATCHES)
        self.assertEqual(s.slot_matches, 0)
        self.assertEqual(len(s.slot_ids), WINDOW_LEN)
        unique_counts = tuple(len(set(ids)) for ids in s.slot_ids)
        self.assertEqual(unique_counts, STANDING_SLOT_UNIQUE_COUNTS)
        self.assertEqual(
            tuple(i for i, n in enumerate(unique_counts) if n < STANDING_WINDOW_COUNT),
            STANDING_MERGED_SLOTS,
        )
        for ids in s.slot_ids:
            self.assertEqual(len(ids), STANDING_WINDOW_COUNT)
            self.assertGreater(len(set(ids)), 1)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_merged_pairs_pass_honest_gates(self):
        """Passing same-slot pairs share an ID.

        Slot 0: CONS+WIDE (Ca7[6]/Ca8[3]) and WIDE-only (Ca7[33]/Ca8[15]).
        Slot 4: CONS (Ca7[23]/Ca8[19]). Slot 7: CONS (Ca7[26]/Ca8[10])
        plus the cycle-19 crop Hamming pair (Ca7[26]/Ca8[22]).
        Other occupants in those slots stay distinct.
        """
        lines = ca7_ca8_instances(self.instances)
        pairs = (
            (lines[0][6], lines[1][3], True, True),
            (lines[0][33], lines[1][15], False, True),
            (lines[0][23], lines[1][19], True, False),
            (lines[0][26], lines[1][10], True, False),
        )
        for left, right, expect_cons, expect_wide in pairs:
            self.assertEqual(expect_cons, passes_type_consistency_gates(left, right))
            self.assertEqual(expect_wide, passes_wide_profile_allograph_gates(left, right))
            self.assertTrue(passes_delimiter_slot_gates(left, right))
            self.assertEqual(left.cluster_id, right.cluster_id)
        crop_left = lines[0][26]
        crop_right = lines[1][22]
        self.assertFalse(passes_delimiter_slot_gates(crop_left, crop_right))
        self.assertTrue(passes_slot_crop_gates(crop_left, crop_right))
        self.assertEqual(crop_left.cluster_id, crop_right.cluster_id)
        # A non-passing occupant in a merged slot keeps its own ID.
        self.assertFalse(passes_delimiter_slot_gates(lines[0][6], lines[0][19]))
        self.assertNotEqual(lines[0][6].cluster_id, lines[0][19].cluster_id)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_slot0_crop_table_is_standing_truth(self):
        """Leftover slot-0 pairs fail crop gates. Do not force 1/8.

        Already-merged pairs sit at NCC 0.504 / 0.544 and 0.909 / 0.117.
        The strongest leftover is NCC 0.229 / chamfer 1.017. Column-ink
        leftover max r is 0.584 — below the 0.70 adjacent-nonmatch
        ceiling — so r is not lowered. Lock 4 unique IDs, not 1.
        """
        lines = ca7_ca8_instances(self.instances)
        unique_slot0 = {window.image_ids[0] for window in self.score.windows}
        self.assertEqual(len(unique_slot0), STANDING_SLOT_UNIQUE_COUNTS[0])
        self.assertEqual(len(unique_slot0), 4)
        self.assertEqual(self.score.slot_matches, 0)
        for left_key, right_key, ncc, chamfer, corr, crop_pass, merged in (
            STANDING_SLOT0_CROP_PAIRS
        ):
            left = slot0_instance(lines, *left_key)
            right = slot0_instance(lines, *right_key)
            got_ncc, got_chamfer, got_corr, got_crop, got_merged = slot0_crop_row(
                left, right
            )
            self.assertAlmostEqual(got_ncc, ncc, places=3, msg=(left_key, right_key))
            self.assertAlmostEqual(
                got_chamfer, chamfer, places=3, msg=(left_key, right_key)
            )
            self.assertAlmostEqual(got_corr, corr, places=3, msg=(left_key, right_key))
            self.assertEqual(got_crop, crop_pass, (left_key, right_key))
            self.assertEqual(got_merged, merged, (left_key, right_key))
            if not merged:
                self.assertFalse(passes_slot_crop_gates(left, right))
                self.assertNotEqual(left.cluster_id, right.cluster_id)
        leftover_ncc = [
            row[2]
            for row in STANDING_SLOT0_CROP_PAIRS
            if not row[6]
        ]
        leftover_chamfer = [
            row[3]
            for row in STANDING_SLOT0_CROP_PAIRS
            if not row[6]
        ]
        leftover_r = [
            row[4]
            for row in STANDING_SLOT0_CROP_PAIRS
            if not row[6]
        ]
        self.assertLess(max(leftover_ncc), 0.45)
        self.assertGreater(min(leftover_chamfer), 0.80)
        self.assertLess(max(leftover_r), 0.70)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_one_crop_pair_drops_published_hamming(self):
        """Cycle 19: only slot 7 Ca7[26]/Ca8[22] clears crop and drops H.

        Gate stays NCC >= 0.45 / chamfer <= 0.80. Hu 2.32 fails keep-ID.
        Slot 2 G020/G060 and slot 3 G019/G061 pass crop but would leave
        published min Hamming at 7 alone, and at 6 together, so they
        stay distinct. Extra leftover merges stay off.
        """
        lines = ca7_ca8_instances(self.instances)
        grams = tuple(window.image_ids for window in self.score.windows)
        cycle18_grams = (
            ("G003", "G021", "G020", "G019", "G015", "G018", "G016", "G017"),
            ("G023", "G026", "G022", "G033", "G004", "G034", "G035", "G005"),
            ("G006", "G043", "G039", "G042", "G036", "G040", "G009", "G041"),
            ("G003", "G011", "G013", "G047", "G049", "G009", "G012", "G005"),
            ("G006", "G052", "G014", "G051", "G004", "G012", "G050", "G002"),
            ("G011", "G013", "G060", "G061", "G014", "G055", "G057", "G054"),
        )
        self.assertEqual(min_pairwise_window_hamming(cycle18_grams), 7)
        self.assertEqual(min_pairwise_window_hamming(grams), 6)
        for slot, left_key, right_key, ncc, chamfer, corr, crop_pass, drops in (
            STANDING_CROP_HAMMING_CANDIDATES
        ):
            left = slot0_instance(lines, *left_key)
            right = slot0_instance(lines, *right_key)
            got_ncc = crop_ncc(left.glyph_crop, right.glyph_crop)
            got_chamfer = crop_chamfer(left.glyph_crop, right.glyph_crop)
            got_corr = profile_correlation(left.ink_profile, right.ink_profile)
            self.assertAlmostEqual(got_ncc, ncc, places=3, msg=(slot, left_key))
            self.assertAlmostEqual(got_chamfer, chamfer, places=3, msg=(slot, left_key))
            self.assertAlmostEqual(got_corr, corr, places=3, msg=(slot, left_key))
            self.assertEqual(passes_slot_crop_gates(left, right), crop_pass)
            self.assertFalse(passes_delimiter_slot_gates(left, right))
            simulated = min_pairwise_window_hamming(
                remap_window_types(cycle18_grams, *{
                    7: ("G005", "G002"),
                    2: ("G020", "G060"),
                    3: ("G019", "G061"),
                }[slot])
            )
            self.assertEqual(simulated < 7, drops, (slot, left_key, right_key))
            if drops:
                self.assertGreaterEqual(_hu_distance(left, right), 2.0)
                self.assertEqual(left.cluster_id, right.cluster_id)
            else:
                self.assertNotEqual(left.cluster_id, right.cluster_id)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_crop_pairs_stay_split_when_hamming_stays_6(self):
        """Cycle 20: leftover-on unions slot 2+3; published H stays 6.

        Default leftover merge is off. Slot 0 leftovers stay split.
        """
        self.assertFalse(ProcessorConfig().delimiter_slot_crop_leftover_merge)
        lines = ca7_ca8_instances(self.instances)
        for slot, left_key, right_key, ncc, chamfer, corr, crop_pass, drops in (
            STANDING_LEFTOVER_CROP_PAIRS
        ):
            left = slot0_instance(lines, *left_key)
            right = slot0_instance(lines, *right_key)
            self.assertTrue(crop_pass)
            self.assertTrue(passes_slot_crop_gates(left, right))
            self.assertFalse(drops)
            self.assertNotEqual(left.cluster_id, right.cluster_id, (slot, left_key))
        leftover_instances = process_tracings(
            self.paths,
            GlyphProcessor(ProcessorConfig(delimiter_slot_crop_leftover_merge=True)),
        )
        leftover_lines = ca7_ca8_instances(leftover_instances)
        leftover_image = ca7_ca8_sequences(leftover_instances)
        leftover_windows = delimiter_image_windows(leftover_image, self.published_lines)
        leftover_grams = tuple(window.image_ids for window in leftover_windows)
        self.assertEqual(min_pairwise_window_hamming(leftover_grams), 6)
        leftover_slots = slot_ids_across_windows(leftover_windows)
        self.assertEqual(
            tuple(len(set(ids)) for ids in leftover_slots),
            (4, 6, 5, 5, 5, 6, 6, 4),
        )
        self.assertEqual(slot_match_count(leftover_slots), 0)
        for slot, left_key, right_key, *_rest in STANDING_LEFTOVER_CROP_PAIRS:
            left = slot0_instance(leftover_lines, *left_key)
            right = slot0_instance(leftover_lines, *right_key)
            self.assertEqual(left.cluster_id, right.cluster_id, (slot, left_key))
        leftover_slot0 = leftover_slots[0]
        self.assertEqual(len(set(leftover_slot0)), 4)
        index = {id(inst): i for i, inst in enumerate(leftover_instances)}
        slot_members = [[] for _ in range(WINDOW_LEN)]
        for line_index, start in ProcessorConfig().delimiter_window_starts:
            line = leftover_lines[line_index]
            for slot in range(WINDOW_LEN):
                slot_members[slot].append(index[id(line[start + slot])])
        self.assertEqual(leftover_crop_pairs(leftover_instances, slot_members), ())
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
