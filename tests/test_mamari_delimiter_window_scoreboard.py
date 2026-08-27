"""Delimiter-window scoreboard: slot identity across published Ca7/Ca8 hits.

Not a G00n→Barthel type map. At each published Guy delimiter occurrence
on Ca7/Ca8, take the eight image G00n IDs in those same reading-order
slots (390 041 378 041 670 008 078 711). A slot matches if every
repetition has the same G00n ID there. Score is 0–8.

North-star beside the repeating 8-gram (freq ≥2). Glyph meanings are
not assigned.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from models.glyphs import GlyphInstance
from tests.test_mamari_calendar_scoreboard import DELIMITER_MOTIF
from processors.glyph_processor import (
    passes_delimiter_slot_gates,
    passes_type_consistency_gates,
    passes_wide_profile_allograph_gates,
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
    ("Ca7", 6, 14, ("G003", "G019", "G018", "G017", "G013", "G016", "G014", "G015")),
    ("Ca7", 19, 27, ("G021", "G024", "G020", "G031", "G004", "G032", "G033", "G005")),
    ("Ca7", 33, 41, ("G006", "G041", "G037", "G040", "G034", "G038", "G009", "G039")),
    ("Ca8", 3, 11, ("G003", "G046", "G049", "G045", "G048", "G009", "G011", "G005")),
    ("Ca8", 15, 23, ("G006", "G052", "G012", "G051", "G004", "G011", "G050", "G002")),
    ("Ca8", 29, 37, ("G058", "G062", "G061", "G063", "G012", "G055", "G057", "G054")),
)
STANDING_WINDOW_COUNT = 6
STANDING_SLOT_MATCHES = 0
# Pairwise slot merges that passed Hu/profile. No slot is unanimous.
STANDING_MERGED_SLOTS = (0, 4, 7)
STANDING_SLOT_UNIQUE_COUNTS = (4, 6, 6, 6, 5, 6, 6, 5)


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

    def test_cycle12_snapshot(self):
        """PR snapshot: 83/64 / 43+40, mixed 2-gram, no 8-gram, slots 0/8."""
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

        Cycle 12 merged passing pairs in slots 0, 4, and 7. No slot is
        unanimous — do not force a leftover occupant onto the merged
        pair. If a later change makes any slot unanimous, raise
        STANDING_SLOT_MATCHES. Not a type map.
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
        """Only the four passing same-slot pairs share an ID.

        Slot 0: CONS+WIDE (Ca7[6]/Ca8[3]) and WIDE-only (Ca7[33]/Ca8[15]).
        Slot 4: CONS (Ca7[23]/Ca8[19]). Slot 7: CONS (Ca7[26]/Ca8[10]).
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
        # A non-passing occupant in a merged slot keeps its own ID.
        self.assertFalse(passes_delimiter_slot_gates(lines[0][6], lines[0][19]))
        self.assertNotEqual(lines[0][6].cluster_id, lines[0][19].cluster_id)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
