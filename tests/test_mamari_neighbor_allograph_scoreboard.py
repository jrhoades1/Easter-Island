"""Neighbor-allograph scoreboard: can the delimiter 3-gram stretch?

Cycle 6 locked mixed G009 G004 G003 on two Ca8 delimiter slices
(670 008 078 and 041 670 008) plus a Ca7 G004 G003 (078 711).
Cycle 7 asks whether tokens immediately left or right of those hits
share a type under the existing unsigned-Hu / area / width gates —
not a stem lookup table.

Honest result: neither corresponding Ca8 neighbor pair passes. Do not
force a 4-gram. Glyph meanings are not assigned.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from models.glyphs import BoundingBox, GlyphInstance, GlyphPosition
from processors.glyph_processor import (
    ProcessorConfig,
    _bbox_area_ratio,
    _bbox_aspect,
    _bbox_width_ratio,
    _hu_distance,
    passes_same_line_allograph_gates,
    passes_split_fragment_allograph_gates,
)
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_position_alignment_scoreboard import STANDING_MIXED_HITS
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_MIXED_REPEATING,
    STANDING_UNIQUE_CLUSTERS,
    mixed_repeating_ngrams,
)

LINE_NAMES = ("Ca7", "Ca8")
# Repeating mixed 3-gram and the Ca7 2-gram it shares a tail with.
CA8_3GRAM_HITS = (
    ("Ca8", 7, 10),
    ("Ca8", 18, 21),
)
CA7_2GRAM_HIT = ("Ca7", 39, 41)
MAX_N = 8


@dataclass(frozen=True)
class NeighborPairScore:
    """Unsigned-Hu / bbox comparison of two reading-order neighbors."""

    side: str
    line_a: str
    index_a: int
    line_b: str
    index_b: int
    hu_distance: float
    area_ratio: float
    width_ratio: float
    aspect_a: float
    aspect_b: float
    passes_same_line: bool
    passes_split_fragment: bool


def ca7_ca8_instances(instances: list[GlyphInstance]) -> list[list[GlyphInstance]]:
    """Same reading order as ca7_ca8_sequences, keeping the instances."""
    by_line: dict[str, list[GlyphInstance]] = {"07": [], "08": []}
    for inst in instances:
        if inst.position is None or not inst.cluster_id:
            continue
        stem = inst.source_image[3:5]
        if stem in by_line:
            by_line[stem].append(inst)
    ordered: list[list[GlyphInstance]] = []
    for stem in ("07", "08"):
        ordered.append(
            sorted(
                by_line[stem],
                key=lambda inst: (
                    inst.source_image,
                    inst.position.line_number,
                    inst.position.position_in_line,
                ),
            )
        )
    return ordered


def neighbor_index(start: int, end: int, side: str, length: int) -> int | None:
    """Reading-order index immediately left or right of [start, end)."""
    if side == "left":
        index = start - 1
    elif side == "right":
        index = end
    else:
        raise ValueError(f"side must be 'left' or 'right', got {side!r}")
    if 0 <= index < length:
        return index
    return None


def score_neighbor_pair(
    lines: list[list[GlyphInstance]],
    line_a: str,
    index_a: int,
    line_b: str,
    index_b: int,
    side: str,
    config: ProcessorConfig | None = None,
) -> NeighborPairScore:
    """Apply existing allograph gates to one neighbor pair. No stem map."""
    cfg = config or ProcessorConfig()
    a = lines[LINE_NAMES.index(line_a)][index_a]
    b = lines[LINE_NAMES.index(line_b)][index_b]
    return NeighborPairScore(
        side=side,
        line_a=line_a,
        index_a=index_a,
        line_b=line_b,
        index_b=index_b,
        hu_distance=_hu_distance(a, b),
        area_ratio=_bbox_area_ratio(a, b),
        width_ratio=_bbox_width_ratio(a, b),
        aspect_a=_bbox_aspect(a),
        aspect_b=_bbox_aspect(b),
        passes_same_line=passes_same_line_allograph_gates(a, b, cfg),
        passes_split_fragment=passes_split_fragment_allograph_gates(a, b, cfg),
    )


def corresponding_neighbors(
    lines: list[list[GlyphInstance]],
    hits: tuple[tuple[str, int, int], ...],
    side: str,
    config: ProcessorConfig | None = None,
) -> NeighborPairScore:
    """Score the two corresponding left or right neighbors of a hit pair."""
    if len(hits) != 2:
        raise ValueError("corresponding_neighbors expects exactly two hits")
    indexes = []
    for line, start, end in hits:
        length = len(lines[LINE_NAMES.index(line)])
        index = neighbor_index(start, end, side, length)
        if index is None:
            raise ValueError(f"no {side} neighbor for {line}[{start}:{end}]")
        indexes.append((line, index))
    return score_neighbor_pair(
        lines, indexes[0][0], indexes[0][1], indexes[1][0], indexes[1][1], side, config
    )


def longest_mixed_repeating_n(
    sequences: list[list[str]], analyzer: NgramAnalyzer, max_n: int = MAX_N
) -> int:
    """Largest mixed n-gram length with frequency ≥2. 0 if none."""
    found = 0
    for gram, _freq in mixed_repeating_ngrams(sequences, analyzer, max_n):
        found = max(found, len(gram))
    return found


class TestNeighborAllographHelpers(unittest.TestCase):
    """Helpers on synthetic instances. No CV, no LLM."""

    def _box(
        self,
        instance_id: str,
        width: int,
        height: int = 66,
        features: list[float] | None = None,
    ) -> GlyphInstance:
        return GlyphInstance(
            instance_id=instance_id,
            source_image="synth.gif",
            bounding_box=BoundingBox(x=0, y=0, width=width, height=height),
            features=features if features is not None else [0.0] * 7,
            position=GlyphPosition(0, 0, 1),
        )

    def test_neighbor_index_left_and_right(self):
        self.assertEqual(neighbor_index(7, 10, "left", 40), 6)
        self.assertEqual(neighbor_index(7, 10, "right", 40), 10)
        self.assertIsNone(neighbor_index(0, 3, "left", 40))
        self.assertIsNone(neighbor_index(38, 40, "right", 40))

    def test_gate_helpers_match_stock_thresholds(self):
        close = self._box("a", 26, features=[0.0] * 7)
        other = self._box("b", 26, features=[0.8] + [0.0] * 6)
        self.assertTrue(passes_same_line_allograph_gates(close, other))
        self.assertTrue(passes_split_fragment_allograph_gates(close, other))

        far = self._box("c", 26, features=[3.0] + [0.0] * 6)
        self.assertTrue(passes_same_line_allograph_gates(close, far))
        self.assertFalse(passes_split_fragment_allograph_gates(close, far))

        too_far = self._box("d", 26, features=[3.6] + [0.0] * 6)
        self.assertFalse(passes_same_line_allograph_gates(close, too_far))
        self.assertFalse(passes_split_fragment_allograph_gates(close, too_far))

        wide = self._box("e", 55, features=[0.8] + [0.0] * 6)
        self.assertFalse(passes_same_line_allograph_gates(close, wide))
        self.assertFalse(passes_split_fragment_allograph_gates(close, wide))

    def test_corresponding_neighbors_on_synthetic_lines(self):
        left_a = self._box("la", 75, height=65, features=[0.0] * 7)
        left_b = self._box("lb", 72, features=[3.4] + [0.0] * 6)
        core = [self._box("g", 20) for _ in range(3)]
        lines = [
            [],
            [left_a, *core, self._box("ra", 26)]
            + [self._box("pad", 20) for _ in range(6)]
            + [left_b, *core, self._box("rb", 55)],
        ]
        score = corresponding_neighbors(lines, (("Ca8", 1, 4), ("Ca8", 12, 15)), "left")
        self.assertEqual((score.line_a, score.index_a), ("Ca8", 0))
        self.assertEqual((score.line_b, score.index_b), ("Ca8", 11))
        self.assertFalse(score.passes_same_line)
        self.assertFalse(score.passes_split_fragment)


class TestMamariNeighborAllographScoreboard(unittest.TestCase):
    """Stock CV neighbors of the cycle-6 mixed hits. MockProvider only."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.instance_lines = ca7_ca8_instances(self.instances)
        self.cfg = ProcessorConfig()

    def test_cycle6_snapshot_unchanged(self):
        """PR snapshot: 83/62 / 43+40, two mixed 2-grams, no 8-gram."""
        cluster_ids = [inst.cluster_id for inst in self.instances if inst.cluster_id]
        self.assertEqual(len(cluster_ids), sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(len(set(cluster_ids)), STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(len(self.image_lines[0]), STANDING_CA7_LEN)
        self.assertEqual(len(self.image_lines[1]), STANDING_CA8_LEN)
        mixed = mixed_repeating_ngrams(self.image_lines, self.ngram_analyzer)
        self.assertEqual(mixed, list(STANDING_MIXED_REPEATING))
        self.assertEqual(longest_mixed_repeating_n(self.image_lines, self.ngram_analyzer), 2)
        eight = self.ngram_analyzer.extract_ngrams(
            self.image_lines, n=8, min_frequency=2
        )
        self.assertEqual(eight, [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ca8_3gram_neighbors_fail_existing_gates(self):
        """Left pair is Hu-far for the split stitch and too wide for tall-thin.

        Right pair is Hu-close but area/width ~2.2, so both gate sets reject
        it. No honest 4-gram merge across the two Ca8 repetitions.
        """
        left = corresponding_neighbors(self.instance_lines, CA8_3GRAM_HITS, "left")
        right = corresponding_neighbors(self.instance_lines, CA8_3GRAM_HITS, "right")

        self.assertEqual((left.index_a, left.index_b), (6, 17))
        self.assertEqual((right.index_a, right.index_b), (10, 21))

        # Size-similar wide figures; Hu sits above the split gate (2.0).
        self.assertGreater(left.hu_distance, self.cfg.split_allograph_max_hu_distance)
        self.assertGreater(left.hu_distance, 3.0)
        self.assertLess(left.area_ratio, self.cfg.allograph_max_area_ratio)
        self.assertLess(left.width_ratio, self.cfg.split_allograph_max_width_ratio)
        self.assertGreater(left.aspect_a, self.cfg.allograph_max_aspect)
        self.assertGreater(left.aspect_b, self.cfg.allograph_max_aspect)
        self.assertFalse(left.passes_same_line)
        self.assertFalse(left.passes_split_fragment)

        # Hu under both thresholds; bbox scale is not.
        self.assertLess(right.hu_distance, self.cfg.split_allograph_max_hu_distance)
        self.assertGreater(right.area_ratio, 2.0)
        self.assertGreater(right.width_ratio, 2.0)
        self.assertGreater(right.area_ratio, self.cfg.allograph_max_area_ratio)
        self.assertGreater(right.width_ratio, self.cfg.split_allograph_max_width_ratio)
        self.assertFalse(right.passes_same_line)
        self.assertFalse(right.passes_split_fragment)

        self.assertEqual(self.provider.get_call_history(), [])

    def test_ca7_2gram_neighbors_do_not_complete_a_4gram(self):
        """Ca7 2-gram neighbors vs each Ca8 3-gram neighbor, same side.

        One right-hand pair (Ca7[41] vs Ca8[10]) passes both gate sets, but
        the other Ca8 right-neighbor does not, so no repeating 4-gram.
        Left-hand Ca7 vs Ca8 pairs fail both sets.
        """
        ca7_line, ca7_start, ca7_end = CA7_2GRAM_HIT
        passing = 0
        for side in ("left", "right"):
            ca7_idx = neighbor_index(
                ca7_start, ca7_end, side, len(self.instance_lines[0])
            )
            self.assertIsNotNone(ca7_idx)
            for line, start, end in CA8_3GRAM_HITS:
                ca8_idx = neighbor_index(start, end, side, len(self.instance_lines[1]))
                self.assertIsNotNone(ca8_idx)
                score = score_neighbor_pair(
                    self.instance_lines,
                    ca7_line,
                    ca7_idx,
                    line,
                    ca8_idx,
                    side,
                    self.cfg,
                )
                if score.passes_same_line or score.passes_split_fragment:
                    passing += 1
                    self.assertEqual(side, "right")
                    self.assertEqual((score.index_a, score.index_b), (41, 10))
        self.assertEqual(passing, 1)
        self.assertEqual(longest_mixed_repeating_n(self.image_lines, self.ngram_analyzer), 2)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_cycle6_hits_still_delimiter_aligned(self):
        """G007 G006 stays off the delimiter; G011 G013 is on it, not a slot match."""
        off = [row for row in STANDING_MIXED_HITS if row[3] == ("G007", "G006")]
        on = [row for row in STANDING_MIXED_HITS if row[3] == ("G011", "G013")]
        self.assertEqual(len(off), 2)
        self.assertEqual(len(on), 2)
        self.assertFalse(any(row[5] or row[6] for row in off))
        self.assertTrue(all(row[5] and row[6] for row in on))
        self.assertEqual(
            [row[3] for row in STANDING_MIXED_HITS if len(row[3]) == 3],
            [],
        )
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
