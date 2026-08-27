"""Wide-profile scoreboard: column-ink corr on cycle-7 delimiter neighbors.

Cycle 7 could not stretch mixed G009 G004 G003: left Ca8 neighbors are
wide (aspect > 0.5) with Hu > 3.0; right neighbors have Hu close but
area/width ~2.2. Cycle 8 asks whether a cheap column-ink profile
correlation, used only on wide boxes, can merge those neighbors.

Honest result: left-pair 32-bin Pearson is ~0.04. Do not force a
4-gram. Tall-thin Hu gates are unchanged. Glyph meanings are not
assigned.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from models.glyphs import BoundingBox, GlyphInstance, GlyphPosition
from processors.glyph_processor import (
    ProcessorConfig,
    _bbox_aspect,
    passes_same_line_allograph_gates,
    passes_split_fragment_allograph_gates,
    passes_wide_profile_allograph_gates,
    profile_correlation,
)
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_neighbor_allograph_scoreboard import (
    CA8_3GRAM_HITS,
    ca7_ca8_instances,
    corresponding_neighbors,
    longest_mixed_repeating_n,
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

# 32-bin Pearson on full-box column ink of the cycle-7 Ca8 neighbors.
STANDING_LEFT_PROFILE_CORR = 0.043
STANDING_RIGHT_PROFILE_CORR = 0.462
MAX_N = 8


@dataclass(frozen=True)
class WideNeighborScore:
    """Column-ink profile comparison of two reading-order neighbors."""

    side: str
    index_a: int
    index_b: int
    aspect_a: float
    aspect_b: float
    both_wide: bool
    profile_correlation: float
    passes_wide_profile: bool
    passes_same_line: bool
    passes_split_fragment: bool


def score_wide_neighbors(lines, hits, side, config=None) -> WideNeighborScore:
    """Score cycle-7 corresponding neighbors with the wide-profile gate."""
    cfg = config or ProcessorConfig()
    base = corresponding_neighbors(lines, hits, side, cfg)
    a = lines[1][base.index_a]
    b = lines[1][base.index_b]
    both_wide = (
        _bbox_aspect(a) > cfg.allograph_max_aspect
        and _bbox_aspect(b) > cfg.allograph_max_aspect
    )
    corr = profile_correlation(a.ink_profile, b.ink_profile, cfg.wide_profile_bins)
    return WideNeighborScore(
        side=side,
        index_a=base.index_a,
        index_b=base.index_b,
        aspect_a=_bbox_aspect(a),
        aspect_b=_bbox_aspect(b),
        both_wide=both_wide,
        profile_correlation=corr,
        passes_wide_profile=passes_wide_profile_allograph_gates(a, b, cfg),
        passes_same_line=base.passes_same_line,
        passes_split_fragment=base.passes_split_fragment,
    )


class TestWideProfileHelpers(unittest.TestCase):
    """Helpers on synthetic instances. No CV, no LLM."""

    def test_wide_gate_requires_aspect_and_high_corr(self):
        ramp = [float(i) for i in range(32)]
        wide = GlyphInstance(
            "w",
            "s.gif",
            BoundingBox(0, 0, 72, 66),
            features=[0.0] * 7,
            ink_profile=ramp,
            position=GlyphPosition(0, 0, 2),
        )
        match = GlyphInstance(
            "m",
            "s.gif",
            BoundingBox(80, 0, 75, 65),
            features=[4.0] + [0.0] * 6,
            ink_profile=ramp,
            position=GlyphPosition(0, 1, 2),
        )
        thin = GlyphInstance(
            "t",
            "s.gif",
            BoundingBox(0, 0, 26, 66),
            features=[0.0] * 7,
            ink_profile=ramp,
            position=GlyphPosition(0, 0, 2),
        )
        self.assertTrue(passes_wide_profile_allograph_gates(wide, match))
        self.assertFalse(passes_wide_profile_allograph_gates(wide, thin))
        self.assertFalse(passes_same_line_allograph_gates(wide, match))
        self.assertFalse(passes_split_fragment_allograph_gates(wide, match))


class TestMamariWideProfileScoreboard(unittest.TestCase):
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

    def test_cycle7_snapshot_unchanged(self):
        """PR snapshot: 83/66 / 43+40, mixed 2-gram, no 8-gram."""
        cluster_ids = [inst.cluster_id for inst in self.instances if inst.cluster_id]
        self.assertEqual(len(cluster_ids), sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(len(set(cluster_ids)), STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(len(self.image_lines[0]), STANDING_CA7_LEN)
        self.assertEqual(len(self.image_lines[1]), STANDING_CA8_LEN)
        mixed = mixed_repeating_ngrams(self.image_lines, self.ngram_analyzer)
        self.assertEqual(mixed, list(STANDING_MIXED_REPEATING))
        self.assertEqual(
            longest_mixed_repeating_n(self.image_lines, self.ngram_analyzer), 2
        )
        eight = self.ngram_analyzer.extract_ngrams(
            self.image_lines, n=8, min_frequency=2
        )
        self.assertEqual(eight, [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ca8_left_neighbors_profile_corr_is_poor(self):
        """Left pair is size-similar and wide; column-ink Pearson is ~0.04.

        Conservative threshold (0.85) is above this pair and above the
        observed adjacent-wide max on Ca7–Ca8 (~0.70). No merge.
        """
        left = score_wide_neighbors(self.instance_lines, CA8_3GRAM_HITS, "left")
        self.assertEqual((left.index_a, left.index_b), (6, 17))
        self.assertTrue(left.both_wide)
        self.assertGreater(left.aspect_a, self.cfg.allograph_max_aspect)
        self.assertGreater(left.aspect_b, self.cfg.allograph_max_aspect)
        self.assertAlmostEqual(
            left.profile_correlation, STANDING_LEFT_PROFILE_CORR, places=2
        )
        self.assertLess(left.profile_correlation, 0.15)
        self.assertLess(
            left.profile_correlation, self.cfg.wide_profile_min_correlation
        )
        self.assertFalse(left.passes_wide_profile)
        self.assertFalse(left.passes_same_line)
        self.assertFalse(left.passes_split_fragment)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ca8_right_neighbors_are_not_both_wide(self):
        """Right pair: one tall-thin, so the wide-only gate does not apply.

        Column-ink Pearson is mid (~0.46) and still below the threshold.
        """
        right = score_wide_neighbors(self.instance_lines, CA8_3GRAM_HITS, "right")
        self.assertEqual((right.index_a, right.index_b), (10, 21))
        self.assertLessEqual(right.aspect_a, self.cfg.allograph_max_aspect)
        self.assertGreater(right.aspect_b, self.cfg.allograph_max_aspect)
        self.assertFalse(right.both_wide)
        self.assertAlmostEqual(
            right.profile_correlation, STANDING_RIGHT_PROFILE_CORR, places=2
        )
        self.assertLess(
            right.profile_correlation, self.cfg.wide_profile_min_correlation
        )
        self.assertFalse(right.passes_wide_profile)
        self.assertFalse(right.passes_same_line)
        self.assertFalse(right.passes_split_fragment)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_mixed_hits_still_delimiter_aligned(self):
        """Standing mixed hits are the remaining 2-gram; still delimiter-aligned."""
        self.assertEqual(len(STANDING_MIXED_HITS), 2)
        self.assertTrue(all(row[5] and row[6] for row in STANDING_MIXED_HITS))
        self.assertEqual(
            [row[3] for row in STANDING_MIXED_HITS if len(row[3]) == 3],
            [],
        )
        self.assertEqual(
            longest_mixed_repeating_n(self.image_lines, self.ngram_analyzer), 2
        )
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
