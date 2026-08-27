"""Nearest 8-window Hamming: full Ca7+Ca8, plus the six Guy windows.

Cycle 17 locked that no 8-gram repeats (Hamming 0 does not occur).
Cycle 18 recorded published-window min Hamming 7. Cycle 19 merges
one leftover crop pair (slot 7 Ca7[26]/Ca8[22]) that drops that
number to 6. Cycle 20 applies the two remaining crop-clear leftover
pairs (slot 2 and slot 3) together; published min stays 6, so those
extra merges stay off. Cycle 21 retries slot-0 leftovers under
{identity, hflip, vflip, 180°}; none clear the crop gate, so
published Hamming stays 6. Concat min stays 3 on the six-G001 night-sign
run.

No detector retune. No G00n→Barthel map. MockProvider only.
input/tablets/sample_tablet.png is a synthetic CV dummy, not Mamari.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import DELIMITER_MOTIF
from tests.test_mamari_delimiter_window_scoreboard import (
    STANDING_DELIMITER_WINDOWS,
    STANDING_SLOT0_INVARIANT_BEST,
    STANDING_SLOT_MATCHES,
    STANDING_SLOT_UNIQUE_COUNTS,
    WINDOW_LEN,
    delimiter_image_windows,
    score_delimiter_windows,
    window_tuple,
)
from processors.glyph_processor import GlyphProcessor, ProcessorConfig
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_position_alignment_scoreboard import (
    delimiter_spans,
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
from tests.test_mamari_unconstrained_ngram_scoreboard import (
    STANDING_LONGEST_MIXED_N,
    STANDING_UNCONSTRAINED_8GRAMS,
    concatenated_ca7_ca8,
    hit_overlaps_delimiter_span,
    score_unconstrained_ngrams,
)

# Concat search includes overlapping starts. Unique winner: adjacent
# windows on the six-G001 night-sign run at the head of Ca7.
STANDING_CONCAT_MIN_HAMMING = 3
STANDING_CONCAT_NEAREST_PAIR = (
    3,
    0,
    8,
    ("G001", "G001", "G001", "G001", "G001", "G001", "G004", "G021"),
    1,
    9,
    ("G001", "G001", "G001", "G001", "G001", "G004", "G021", "G020"),
    True,
    True,
)
# Cycle 18 published-window floor. Cycle 19 beats it with one crop merge.
CYCLE18_PUBLISHED_MIN_HAMMING = 7
CYCLE18_PUBLISHED_MIN_PAIR_COUNT = 4
# Published-window search after the slot-7 crop Hamming merge.
# Unique pair at 6: Ca7[19:27] vs Ca8[15:23] (G005 slot 4, G003 slot 7).
STANDING_PUBLISHED_MIN_HAMMING = 6
STANDING_PUBLISHED_MIN_PAIR_COUNT = 1
STANDING_PUBLISHED_NEAREST_PAIR = (
    6,
    "Ca7",
    19,
    27,
    ("G023", "G026", "G022", "G033", "G005", "G034", "G035", "G003"),
    "Ca8",
    15,
    23,
    ("G006", "G052", "G014", "G051", "G005", "G012", "G050", "G003"),
)
# 83/62 / published H / slot matches / mixed n
STANDING_BEFORE_AFTER = (
    (83, 62, 7, 0, 2),
    (83, 62, 6, 0, 2),
)
# Cycle 20 leftover-on experiment. Hamming stays 6; extra merges off.
CROP_LEFTOVERS_EXHAUSTED_AT_HAMMING = 6
LEFTOVER_ON_UNIQUE_CLUSTERS = 60
LEFTOVER_ON_SLOT_UNIQUE_COUNTS = (4, 6, 5, 5, 5, 6, 6, 4)
LEFTOVER_ON_PUBLISHED_MIN_PAIR_COUNT = 2
# instances, types, published H, slot unique, slot matches, mixed n
STANDING_LEFTOVER_BEFORE_AFTER = (
    (83, 62, 6, (4, 6, 6, 6, 5, 6, 6, 4), 0, 2),
    (83, 60, 6, (4, 6, 5, 5, 5, 6, 6, 4), 0, 2),
)
# Cycle 21: no slot-0 leftover clears flip/180 crop, so no merge.
SLOT0_INVARIANT_GATE_CLEARS = False
SLOT0_INVARIANT_HAMMING_BEFORE = STANDING_PUBLISHED_MIN_HAMMING
SLOT0_INVARIANT_HAMMING_AFTER = STANDING_PUBLISHED_MIN_HAMMING


@dataclass(frozen=True)
class Nearest8WindowScore:
    """Nearest length-8 Hamming snapshot. No type map."""

    concat_hamming: int
    concat_pair: tuple
    published_hamming: int
    published_pair: tuple
    published_min_pair_count: int
    instance_count: int
    unique_cluster_count: int
    window_matches: int


def hamming_distance(left: tuple[str, ...] | list[str], right: tuple[str, ...] | list[str]) -> int:
    """Positions that differ. Equal length required."""
    if len(left) != len(right):
        raise ValueError("Hamming requires equal-length windows")
    return sum(a != b for a, b in zip(left, right))


def sliding_windows(
    sequence: list[str] | tuple[str, ...], n: int = WINDOW_LEN
) -> tuple[tuple[int, int, tuple[str, ...]], ...]:
    """(start, end, gram) for every length-n window, reading order."""
    return tuple((i, i + n, tuple(sequence[i : i + n])) for i in range(len(sequence) - n + 1))


def nearest_sliding_pair(
    sequence: list[str] | tuple[str, ...], n: int = WINDOW_LEN
) -> tuple[int, tuple[int, int, tuple[str, ...]], tuple[int, int, tuple[str, ...]]]:
    """Min Hamming among distinct sliding windows. Tie → earliest starts."""
    windows = sliding_windows(sequence, n)
    if len(windows) < 2:
        raise ValueError("need at least two windows")
    best: tuple | None = None
    for i, left in enumerate(windows):
        for right in windows[i + 1 :]:
            rec = (hamming_distance(left[2], right[2]), left, right)
            if best is None or rec < best:
                best = rec
    assert best is not None
    return best


def nearest_published_pair(
    windows: tuple[tuple, ...] | list[tuple],
) -> tuple[int, tuple, tuple]:
    """Min Hamming among published (line, start, end, gram) rows."""
    if len(windows) < 2:
        raise ValueError("need at least two windows")
    best: tuple | None = None
    for i, left in enumerate(windows):
        for right in windows[i + 1 :]:
            rec = (hamming_distance(left[3], right[3]), left, right)
            if best is None or rec < best:
                best = rec
    assert best is not None
    return best


def published_pairs_at_hamming(
    windows: tuple[tuple, ...] | list[tuple], distance: int
) -> tuple[tuple, ...]:
    """Published window pairs whose Hamming equals distance."""
    rows: list[tuple] = []
    for i, left in enumerate(windows):
        for right in windows[i + 1 :]:
            if hamming_distance(left[3], right[3]) == distance:
                rows.append((left, right))
    return tuple(rows)


def concat_range_line_slices(
    start: int, end: int, ca7_len: int
) -> tuple[tuple[int, int, int], ...]:
    """Map concat [start, end) onto (line_index, local_start, local_end)."""
    slices: list[tuple[int, int, int]] = []
    if start < ca7_len:
        slices.append((0, start, min(end, ca7_len)))
    if end > ca7_len:
        slices.append((1, max(start, ca7_len) - ca7_len, end - ca7_len))
    return tuple(slices)


def concat_range_overlaps_delimiter(
    start: int,
    end: int,
    ca7_len: int,
    spans: list[tuple[int, int, int]],
) -> bool:
    """True if the concat window shares any index with a published span."""
    return any(
        hit_overlaps_delimiter_span(line, local_start, local_end, spans)
        for line, local_start, local_end in concat_range_line_slices(start, end, ca7_len)
    )


def concat_pair_tuple(
    hamming: int,
    left: tuple[int, int, tuple[str, ...]],
    right: tuple[int, int, tuple[str, ...]],
    ca7_len: int,
    spans: list[tuple[int, int, int]],
) -> tuple:
    """Lock row: Hamming, ranges, grams, delimiter-span overlap flags."""
    return (
        hamming,
        left[0],
        left[1],
        left[2],
        right[0],
        right[1],
        right[2],
        concat_range_overlaps_delimiter(left[0], left[1], ca7_len, spans),
        concat_range_overlaps_delimiter(right[0], right[1], ca7_len, spans),
    )


def published_pair_tuple(hamming: int, left: tuple, right: tuple) -> tuple:
    """Lock row: Hamming plus two published window rows."""
    return (hamming, *left, *right)


def score_nearest_8windows(
    instances,
    image_lines: list[list[str]],
    published_lines: list[list[str]],
) -> Nearest8WindowScore:
    """Search lock: nearest concat 8-windows and nearest published pair."""
    concat = concatenated_ca7_ca8(image_lines)[0]
    spans = delimiter_spans(published_lines, DELIMITER_MOTIF)
    ca7_len = len(image_lines[0]) if image_lines else 0
    concat_h, concat_left, concat_right = nearest_sliding_pair(concat, WINDOW_LEN)
    published_windows = tuple(
        window_tuple(window) for window in delimiter_image_windows(image_lines, published_lines)
    )
    pub_h, pub_left, pub_right = nearest_published_pair(published_windows)
    cluster_ids = [inst.cluster_id for inst in instances if inst.cluster_id]
    window = score_delimiter_windows(instances, image_lines, published_lines)
    return Nearest8WindowScore(
        concat_hamming=concat_h,
        concat_pair=concat_pair_tuple(
            concat_h, concat_left, concat_right, ca7_len, spans
        ),
        published_hamming=pub_h,
        published_pair=published_pair_tuple(pub_h, pub_left, pub_right),
        published_min_pair_count=len(
            published_pairs_at_hamming(published_windows, pub_h)
        ),
        instance_count=len(cluster_ids),
        unique_cluster_count=len(set(cluster_ids)),
        window_matches=window.slot_matches,
    )


class TestNearest8WindowHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_hamming_counts_differing_positions(self):
        self.assertEqual(hamming_distance(("A",) * 8, ("A",) * 8), 0)
        self.assertEqual(
            hamming_distance(
                ("A", "A", "A", "A", "A", "A", "B", "C"),
                ("A", "A", "A", "A", "A", "B", "C", "D"),
            ),
            3,
        )
        self.assertEqual(
            hamming_distance(tuple(f"L{i}" for i in range(8)), tuple(f"R{i}" for i in range(8))),
            8,
        )
        with self.assertRaises(ValueError):
            hamming_distance(("A", "B"), ("A", "B", "C"))

    def test_nearest_sliding_pair_prefers_earliest_tie(self):
        """Two Hamming-1 pairs: earliest starts win. No exact match."""
        seq = list("ABCDABCXPQRSPQRT")
        hamming, left, right = nearest_sliding_pair(seq, 4)
        self.assertEqual(hamming, 1)
        self.assertEqual(left, (0, 4, ("A", "B", "C", "D")))
        self.assertEqual(right, (4, 8, ("A", "B", "C", "X")))
        later = nearest_sliding_pair(seq[8:], 4)
        self.assertEqual(later[0], 1)
        self.assertEqual(later[1], (0, 4, ("P", "Q", "R", "S")))

    def test_overlapping_windows_are_eligible(self):
        """Adjacent overlapping starts can be the nearest pair."""
        seq = ["A"] * 6 + ["B", "C", "D"]
        hamming, left, right = nearest_sliding_pair(seq, 8)
        self.assertEqual(hamming, 3)
        self.assertEqual(left[0], 0)
        self.assertEqual(right[0], 1)
        self.assertEqual(left[2][:6], ("A",) * 6)
        self.assertNotEqual(left[2], right[2])

    def test_concat_range_maps_join_and_overlap(self):
        spans = [(0, 6, 14), (0, 33, 41), (1, 3, 11)]
        self.assertEqual(concat_range_line_slices(0, 8, 43), ((0, 0, 8),))
        self.assertEqual(concat_range_line_slices(43, 51, 43), ((1, 0, 8),))
        self.assertEqual(concat_range_line_slices(40, 48, 43), ((0, 40, 43), (1, 0, 5)))
        self.assertTrue(concat_range_overlaps_delimiter(0, 8, 43, spans))
        self.assertTrue(concat_range_overlaps_delimiter(1, 9, 43, spans))
        self.assertFalse(concat_range_overlaps_delimiter(14, 19, 43, spans))
        self.assertTrue(concat_range_overlaps_delimiter(40, 48, 43, spans))
        self.assertFalse(hit_overlaps_delimiter_span(0, 14, 19, spans))

    def test_published_nearest_is_min_hamming(self):
        windows = (
            ("Ca7", 0, 8, ("A", "B", "C", "D", "E", "F", "G", "H")),
            ("Ca7", 10, 18, ("A", "X", "C", "Y", "E", "Z", "G", "Q")),
            ("Ca8", 0, 8, ("A", "B", "C", "D", "E", "F", "G", "H")),
        )
        hamming, left, right = nearest_published_pair(windows)
        self.assertEqual(hamming, 0)
        self.assertEqual(left[0], "Ca7")
        self.assertEqual(right[0], "Ca8")
        self.assertEqual(len(published_pairs_at_hamming(windows, 0)), 1)
        self.assertEqual(len(published_pairs_at_hamming(windows, 4)), 2)


class TestMamariNearest8WindowScoreboard(unittest.TestCase):
    """Stock CV → nearest 8-window Hamming lock. MockProvider only."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.published_lines = published_ca7_ca8_stems()
        self.score = score_nearest_8windows(
            self.instances, self.image_lines, self.published_lines
        )

    def test_concat_nearest_8window_is_hamming_3(self):
        """Nearest concat pair is Hamming 3 at Ca7[0:8] vs Ca7[1:9].

        Adjacent overlapping windows on the six-G001 night-sign run plus
        the first two tokens of the first delimiter. Both overlap
        published Ca7[6:14). Hamming 0 still does not occur.
        """
        s = self.score
        self.assertEqual(s.concat_hamming, STANDING_CONCAT_MIN_HAMMING)
        self.assertEqual(s.concat_pair, STANDING_CONCAT_NEAREST_PAIR)
        self.assertGreater(s.concat_hamming, 0)
        self.assertTrue(s.concat_pair[-2] and s.concat_pair[-1])
        unconstrained = score_unconstrained_ngrams(
            self.instances,
            self.image_lines,
            self.published_lines,
            self.ngram_analyzer,
        )
        self.assertEqual(unconstrained.eightgrams_concat, STANDING_UNCONSTRAINED_8GRAMS)
        self.assertEqual(unconstrained.longest_mixed_n, STANDING_LONGEST_MIXED_N)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_published_windows_min_hamming_is_6(self):
        """Closest published Guy windows differ in 6 of 8 slots.

        Unique pair at 6: Ca7[19:27] vs Ca8[15:23] (G005 slot 4 from
        cycle 12, G003 slot 7 from the cycle-19 crop merge). Cycle 18
        floor was 7. Concat min stays 3 on the night-sign run.
        """
        s = self.score
        self.assertEqual(s.published_hamming, STANDING_PUBLISHED_MIN_HAMMING)
        self.assertEqual(s.published_pair, STANDING_PUBLISHED_NEAREST_PAIR)
        self.assertEqual(s.published_min_pair_count, STANDING_PUBLISHED_MIN_PAIR_COUNT)
        self.assertLess(s.published_hamming, CYCLE18_PUBLISHED_MIN_HAMMING)
        self.assertEqual(
            s.published_pair[1:5],
            STANDING_DELIMITER_WINDOWS[1],
        )
        self.assertEqual(
            s.published_pair[5:9],
            STANDING_DELIMITER_WINDOWS[4],
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_crop_hamming_before_after_table(self):
        """One crop merge: 83/62 stays; published H 7→6; slots 0/8; mixed n=2."""
        s = self.score
        after = (
            s.instance_count,
            s.unique_cluster_count,
            s.published_hamming,
            s.window_matches,
            STANDING_LONGEST_MIXED_N,
        )
        self.assertEqual(STANDING_BEFORE_AFTER[0], (83, 62, CYCLE18_PUBLISHED_MIN_HAMMING, 0, 2))
        self.assertEqual(after, STANDING_BEFORE_AFTER[1])
        unconstrained = score_unconstrained_ngrams(
            self.instances,
            self.image_lines,
            self.published_lines,
            self.ngram_analyzer,
        )
        self.assertEqual(unconstrained.longest_mixed_n, STANDING_LONGEST_MIXED_N)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_hamming_merge_off_restores_cycle18_published_7(self):
        """delimiter_slot_crop_hamming_merge=False keeps published H=7."""
        instances = process_tracings(
            self.paths, GlyphProcessor(ProcessorConfig(delimiter_slot_crop_hamming_merge=False))
        )
        image_lines = ca7_ca8_sequences(instances)
        score = score_nearest_8windows(instances, image_lines, self.published_lines)
        self.assertEqual(score.published_hamming, CYCLE18_PUBLISHED_MIN_HAMMING)
        self.assertEqual(score.published_min_pair_count, CYCLE18_PUBLISHED_MIN_PAIR_COUNT)
        self.assertEqual(score.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_crop_merges_exhausted_at_published_6(self):
        """Slot 2 + slot 3 leftover unions leave published Hamming at 6.

        Extra merges stay off. Turning them on drops types 62→60 and
        slot unique (4, 6, 6, 6, 5, 6, 6, 4)→(4, 6, 5, 5, 5, 6, 6, 4)
        but does not beat the cycle-19 published floor.
        """
        self.assertFalse(ProcessorConfig().delimiter_slot_crop_leftover_merge)
        self.assertEqual(
            STANDING_PUBLISHED_MIN_HAMMING, CROP_LEFTOVERS_EXHAUSTED_AT_HAMMING
        )
        leftover = process_tracings(
            self.paths,
            GlyphProcessor(ProcessorConfig(delimiter_slot_crop_leftover_merge=True)),
        )
        leftover_lines = ca7_ca8_sequences(leftover)
        leftover_score = score_nearest_8windows(
            leftover, leftover_lines, self.published_lines
        )
        leftover_window = score_delimiter_windows(
            leftover, leftover_lines, self.published_lines
        )
        leftover_unique = tuple(len(set(ids)) for ids in leftover_window.slot_ids)
        before = (
            self.score.instance_count,
            self.score.unique_cluster_count,
            self.score.published_hamming,
            STANDING_SLOT_UNIQUE_COUNTS,
            self.score.window_matches,
            STANDING_LONGEST_MIXED_N,
        )
        after = (
            leftover_score.instance_count,
            leftover_score.unique_cluster_count,
            leftover_score.published_hamming,
            leftover_unique,
            leftover_score.window_matches,
            STANDING_LONGEST_MIXED_N,
        )
        self.assertEqual(before, STANDING_LEFTOVER_BEFORE_AFTER[0])
        self.assertEqual(after, STANDING_LEFTOVER_BEFORE_AFTER[1])
        self.assertEqual(
            leftover_score.published_hamming, CROP_LEFTOVERS_EXHAUSTED_AT_HAMMING
        )
        self.assertEqual(leftover_score.unique_cluster_count, LEFTOVER_ON_UNIQUE_CLUSTERS)
        self.assertEqual(leftover_unique, LEFTOVER_ON_SLOT_UNIQUE_COUNTS)
        self.assertEqual(
            leftover_score.published_min_pair_count, LEFTOVER_ON_PUBLISHED_MIN_PAIR_COUNT
        )
        self.assertEqual(leftover_score.concat_hamming, STANDING_CONCAT_MIN_HAMMING)
        unconstrained = score_unconstrained_ngrams(
            leftover,
            leftover_lines,
            self.published_lines,
            self.ngram_analyzer,
        )
        self.assertEqual(unconstrained.longest_mixed_n, STANDING_LONGEST_MIXED_N)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_slot0_invariant_crop_leaves_published_hamming_6(self):
        """Flip/180 slot-0 leftovers fail the crop gate. Hamming stays 6.

        Best leftover is Ca7[33]/Ca8[29] hflip at NCC 0.247 / chamfer
        1.224. leftover_merge stays off. Turning invariant merge on
        does not change the snapshot.
        """
        self.assertFalse(ProcessorConfig().delimiter_slot_crop_leftover_merge)
        self.assertFalse(ProcessorConfig().delimiter_slot_crop_invariant_merge)
        self.assertFalse(SLOT0_INVARIANT_GATE_CLEARS)
        self.assertFalse(STANDING_SLOT0_INVARIANT_BEST[5])
        self.assertEqual(self.score.published_hamming, SLOT0_INVARIANT_HAMMING_BEFORE)
        invariant = process_tracings(
            self.paths,
            GlyphProcessor(ProcessorConfig(delimiter_slot_crop_invariant_merge=True)),
        )
        invariant_lines = ca7_ca8_sequences(invariant)
        invariant_score = score_nearest_8windows(
            invariant, invariant_lines, self.published_lines
        )
        self.assertEqual(invariant_score.published_hamming, SLOT0_INVARIANT_HAMMING_AFTER)
        self.assertEqual(
            invariant_score.published_hamming, STANDING_PUBLISHED_MIN_HAMMING
        )
        self.assertEqual(invariant_score.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(invariant_score.window_matches, STANDING_SLOT_MATCHES)
        self.assertEqual(invariant_score.concat_hamming, STANDING_CONCAT_MIN_HAMMING)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_standing_83_62_and_window_0_of_8(self):
        """Crop Hamming merge keeps 83/62 / 0/8. Types are remumbered."""
        s = self.score
        published_ca7, published_ca8 = published_ca7_ca8_stem_counts()
        identity = score_type_identity(
            self.instances,
            self.ngram_analyzer,
            published_ca7,
            published_ca8,
        )
        window = score_delimiter_windows(
            self.instances, self.image_lines, self.published_lines
        )
        self.assertEqual(s.instance_count, 83)
        self.assertEqual(s.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(s.window_matches, STANDING_SLOT_MATCHES)
        self.assertEqual(identity.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(identity.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(identity.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(window.slot_matches, 0)
        unique_counts = tuple(len(set(ids)) for ids in window.slot_ids)
        self.assertEqual(unique_counts, STANDING_SLOT_UNIQUE_COUNTS)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
