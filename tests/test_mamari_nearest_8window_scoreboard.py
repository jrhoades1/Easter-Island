"""Nearest 8-window Hamming: full Ca7+Ca8, plus the six Guy windows.

Cycle 17 locked that no 8-gram repeats (Hamming 0 does not occur).
Cycle 18 records the nearest pair of length-8 G00n windows on the
concatenated Ca7+Ca8 sequence, and the nearest pair among the six
published delimiter windows. Distance is Hamming (positions that differ).

No clustering change. No detector retune. No G00n→Barthel map.
MockProvider only. Search lock, not a merge.
input/tablets/sample_tablet.png is a synthetic CV dummy, not Mamari.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import DELIMITER_MOTIF
from tests.test_mamari_delimiter_window_scoreboard import (
    STANDING_DELIMITER_WINDOWS,
    STANDING_SLOT_MATCHES,
    STANDING_SLOT_UNIQUE_COUNTS,
    WINDOW_LEN,
    delimiter_image_windows,
    score_delimiter_windows,
    window_tuple,
)
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
    ("G001", "G001", "G001", "G001", "G001", "G001", "G003", "G021"),
    1,
    9,
    ("G001", "G001", "G001", "G001", "G001", "G003", "G021", "G020"),
    True,
    True,
)
# Published-window search. Four pairs sit at 7 (cycle-12 merged slots).
# First in reading order: Ca7[6:14] vs Ca8[3:11], shared G003 at slot 0.
STANDING_PUBLISHED_MIN_HAMMING = 7
STANDING_PUBLISHED_MIN_PAIR_COUNT = 4
STANDING_PUBLISHED_NEAREST_PAIR = (
    7,
    "Ca7",
    6,
    14,
    ("G003", "G021", "G020", "G019", "G015", "G018", "G016", "G017"),
    "Ca8",
    3,
    11,
    ("G003", "G011", "G013", "G047", "G049", "G009", "G012", "G005"),
)


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

    def test_published_windows_min_hamming_is_7(self):
        """Closest published Guy windows differ in 7 of 8 slots.

        First pair at 7: Ca7[6:14] vs Ca8[3:11] (shared G003 at slot 0).
        Four pairs sit at 7 — one shared ID each, the cycle-12 merges.
        This 7 is the published-window number to beat.
        """
        s = self.score
        self.assertEqual(s.published_hamming, STANDING_PUBLISHED_MIN_HAMMING)
        self.assertEqual(s.published_pair, STANDING_PUBLISHED_NEAREST_PAIR)
        self.assertEqual(s.published_min_pair_count, STANDING_PUBLISHED_MIN_PAIR_COUNT)
        self.assertEqual(
            s.published_pair[1:5],
            STANDING_DELIMITER_WINDOWS[0],
        )
        self.assertEqual(
            s.published_pair[5:9],
            STANDING_DELIMITER_WINDOWS[3],
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_standing_83_62_and_window_0_of_8(self):
        """Search lock does not change clustering. 83/62 / 0/8 stays."""
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
