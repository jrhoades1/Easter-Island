"""Type-identity scoreboard: stock CV cluster IDs on Ca7–Ca8 tracings.

Locks current type-identity metrics so later cycles can be scored.
Stock feature is unsigned log-Hu. Detection is not retuned.
Does not invent G00n→Barthel maps.

input/tablets/sample_tablet.png is a synthetic CV dummy, not Mamari.
"""

import unittest
from dataclasses import dataclass

import numpy as np

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from models.glyphs import BoundingBox, GlyphInstance, GlyphPosition
from processors.glyph_processor import GlyphProcessor, ProcessorConfig
from tests.test_mamari_calendar_scoreboard import barthel_stems, load_mamari_fixture
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)

# Cycle 22 locks published 8-crop window strips below the crop
# gate (best NCC 0.244 / chamfer 2.137 identity); 83/62 / H=6.
# Cycle 21 locks slot-0 flip/180 crop leftovers below the gate
# (best NCC 0.247 / chamfer 1.224); published H stays 6.
# Cycle 20 locks leftover crop pairs exhausted at published H=6
# (slot 2 + slot 3 together do not drop Hamming). Cycle 19 drops
# published-window min Hamming 7→6 with one crop merge and keeps
# 83/62 / 0/8 / mixed n=2. Cycle 18 locked nearest
# 8-window Hamming (concat 3 / published 7). Cycle 17 searched the
# full G00n sequence (not Guy windows): no repeating 8-gram;
# longest mixed n=2. Cycle 16 found no honest higher-res public
# Ca7–Ca8 raster (GIF ceiling). Cycle 15 global keep-ID gate after
# DBSCAN dropped two types vs cycle 14 (83/64).
# Window stays 0/8. Cycle 13 was the same 83/64 (crop leftovers fail).
# Cycle 11 was 83/66 / mixed
# G003 G008. Cycle 9 was 83/62 / mixed 3-gram (same type count, different
# clustering). Cycle 4 was 67 types. Cycle 3 was 75/58. Cycle 2 was 65.
# Cycle 1 signed lock was 71.
STANDING_INSTANCES_PER_STRIP = {
    "sca0701.gif": 14,
    "sca0702.gif": 16,
    "sca0703.gif": 13,
    "sca0801.gif": 14,
    "sca0802.gif": 14,
    "sca0803.gif": 12,
}
CYCLE3_INSTANCES_PER_STRIP = {
    "sca0701.gif": 14,
    "sca0702.gif": 14,
    "sca0703.gif": 11,
    "sca0801.gif": 12,
    "sca0802.gif": 12,
    "sca0803.gif": 12,
}
STANDING_UNIQUE_CLUSTERS = 62
CYCLE14_UNIQUE_CLUSTERS = 64
CYCLE11_UNIQUE_CLUSTERS = 66
CYCLE9_UNIQUE_CLUSTERS = 62
CYCLE4_UNIQUE_CLUSTERS = 67
CYCLE3_UNIQUE_CLUSTERS = 58
CYCLE2_UNSIGNED_UNIQUE_CLUSTERS = 65
CYCLE1_SIGNED_UNIQUE_CLUSTERS = 71
STANDING_MAX_REPEATING_N = 5
STANDING_CA7_LEN = 43
STANDING_CA8_LEN = 40
CYCLE3_CA7_LEN = 39
CYCLE3_CA8_LEN = 36
STANDING_HAS_MIXED_REPEATING = True
STANDING_MIXED_REPEATING = (
    (("G007", "G006"), 2),
    (("G011", "G013"), 2),
)
CYCLE14_MIXED_REPEATING = (
    (("G007", "G006"), 2),
)
CYCLE11_MIXED_REPEATING = (
    (("G003", "G008"), 2),
)
CYCLE9_MIXED_REPEATING = (
    (("G004", "G003"), 3),
    (("G009", "G004"), 2),
    (("G009", "G004", "G003"), 2),
)
STANDING_SPLIT_FRAGMENT_COUNT = 12

# Opening night-sign run on sca0701 is six thin crescents; the next blob is a
# wide ligature (~71px). Isolate by the opening narrow run, not by G00n ID.
CRESCENT_MAX_WIDTH = 40
CRESCENT_COUNT = 6
MAX_N = 8


@dataclass(frozen=True)
class TypeIdentityScore:
    """Stock-CV type-identity snapshot. No Barthel remapping."""

    instances_per_strip: dict[str, int]
    instance_count: int
    unique_cluster_count: int
    unique_instance_ratio: float
    max_repeating_n: int
    ca7_length: int
    ca8_length: int
    published_ca7_stems: int
    published_ca8_stems: int
    has_mixed_repeating: bool


def published_ca7_ca8_stem_counts() -> tuple[int, int]:
    """Mechanical Barthel-stem counts from the published Ca6–Ca9 fixture."""
    lines = load_mamari_fixture()["lines"]
    return len(barthel_stems(lines["Ca7"])), len(barthel_stems(lines["Ca8"]))


def max_repeating_n(sequences: list[list[str]], analyzer: NgramAnalyzer, max_n: int = MAX_N) -> int:
    """Largest n in 1..max_n that has any n-gram with frequency ≥2. 0 if none."""
    found = 0
    for n in range(1, max_n + 1):
        if analyzer.extract_ngrams(sequences, n=n, min_frequency=2):
            found = n
    return found


def mixed_repeating_ngrams(
    sequences: list[list[str]], analyzer: NgramAnalyzer, max_n: int = MAX_N
) -> list[tuple[tuple[str, ...], int]]:
    """Mixed n-grams of length >= 2 with freq >= 2, shortest n first."""
    found: list[tuple[tuple[str, ...], int]] = []
    for n in range(2, max_n + 1):
        for gram, freq in analyzer.extract_ngrams(sequences, n=n, min_frequency=2):
            if len(set(gram)) > 1:
                found.append((gram, freq))
    return found


def has_mixed_repeating_ngram(
    sequences: list[list[str]], analyzer: NgramAnalyzer, max_n: int = MAX_N
) -> bool:
    """True if any n-gram of length >= 2 with freq >= 2 uses more than one type."""
    return bool(mixed_repeating_ngrams(sequences, analyzer, max_n))


def score_type_identity(
    instances: list[GlyphInstance],
    analyzer: NgramAnalyzer,
    published_ca7: int,
    published_ca8: int,
) -> TypeIdentityScore:
    """Record stock type-identity metrics. IDs stay G00n."""
    per_strip = {name: 0 for name in TRACING_NAMES}
    cluster_ids: list[str] = []
    for inst in instances:
        if inst.source_image in per_strip:
            per_strip[inst.source_image] += 1
        if inst.cluster_id:
            cluster_ids.append(inst.cluster_id)

    unique = len(set(cluster_ids))
    count = len(cluster_ids)
    lines = ca7_ca8_sequences(instances)
    return TypeIdentityScore(
        instances_per_strip=per_strip,
        instance_count=count,
        unique_cluster_count=unique,
        unique_instance_ratio=(unique / count) if count else 0.0,
        max_repeating_n=max_repeating_n(lines, analyzer),
        ca7_length=len(lines[0]) if lines else 0,
        ca8_length=len(lines[1]) if len(lines) > 1 else 0,
        published_ca7_stems=published_ca7,
        published_ca8_stems=published_ca8,
        has_mixed_repeating=has_mixed_repeating_ngram(lines, analyzer),
    )


def isolate_sca0701_opening_crescents(instances: list[GlyphInstance]) -> list[GlyphInstance]:
    """First consecutive narrow detections on sca0701 (published opening 040 run)."""
    strip = [
        inst
        for inst in instances
        if inst.source_image == "sca0701.gif" and inst.position is not None
    ]
    strip.sort(key=lambda inst: (inst.position.line_number, inst.position.position_in_line))
    crescents: list[GlyphInstance] = []
    for inst in strip:
        if inst.bounding_box.width >= CRESCENT_MAX_WIDTH:
            break
        crescents.append(inst)
    return crescents


def pairwise_log_hu_distances(
    instances: list[GlyphInstance],
) -> list[tuple[str, str, float]]:
    """Euclidean distances on stored 7-d log-Hu vectors (unsigned or signed)."""
    pairs: list[tuple[str, str, float]] = []
    for i, left in enumerate(instances):
        feat_i = np.asarray(left.features, dtype=float)
        label_i = left.cluster_id or left.instance_id
        for right in instances[i + 1 :]:
            feat_j = np.asarray(right.features, dtype=float)
            label_j = right.cluster_id or right.instance_id
            pairs.append((label_i, label_j, float(np.linalg.norm(feat_i - feat_j))))
    return pairs


class TestPublishedStemCounts(unittest.TestCase):
    """Verify the fixture still yields 43 / 40 stems before using those targets."""

    def test_ca7_ca8_stem_counts(self):
        ca7, ca8 = published_ca7_ca8_stem_counts()
        self.assertEqual((ca7, ca8), (43, 40))


class TestTypeIdentityHelpers(unittest.TestCase):
    """Helpers on synthetic instances. No CV, no LLM."""

    def test_max_repeating_n_stops_at_unigrams(self):
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        sequences = [["A", "B", "A"], ["C", "D"]]
        self.assertEqual(max_repeating_n(sequences, analyzer), 1)
        self.assertFalse(has_mixed_repeating_ngram(sequences, analyzer))
        self.assertEqual(provider.get_call_history(), [])

    def test_mixed_repeating_ngram_requires_two_types(self):
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        sequences = [["A", "B", "A", "B"], ["C", "D"]]
        self.assertTrue(has_mixed_repeating_ngram(sequences, analyzer))
        self.assertEqual(
            mixed_repeating_ngrams(sequences, analyzer),
            [(("A", "B"), 2)],
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_isolate_opening_run_stops_at_wide_glyph(self):
        bbox_n = BoundingBox(x=0, y=0, width=26, height=66)
        bbox_w = BoundingBox(x=130, y=0, width=71, height=67)
        instances = []
        for i in range(6):
            instances.append(
                GlyphInstance(
                    f"c{i}",
                    "sca0701.gif",
                    bbox_n,
                    cluster_id=f"G{i + 1:03d}",
                    position=GlyphPosition(0, i, 7),
                )
            )
        instances.append(
            GlyphInstance(
                "wide",
                "sca0701.gif",
                bbox_w,
                cluster_id="G099",
                position=GlyphPosition(0, 6, 7),
            )
        )
        crescents = isolate_sca0701_opening_crescents(instances)
        self.assertEqual(len(crescents), CRESCENT_COUNT)
        self.assertEqual([c.cluster_id for c in crescents], [f"G{i:03d}" for i in range(1, 7)])

    def test_pairwise_log_hu_euclidean(self):
        bbox = BoundingBox(x=0, y=0, width=10, height=10)
        a = GlyphInstance("a", "sca0701.gif", bbox, features=[0.0] * 7, cluster_id="G001")
        b = GlyphInstance("b", "sca0701.gif", bbox, features=[3.0] + [0.0] * 6, cluster_id="G002")
        pairs = pairwise_log_hu_distances([a, b])
        self.assertEqual(len(pairs), 1)
        self.assertEqual(pairs[0][:2], ("G001", "G002"))
        self.assertAlmostEqual(pairs[0][2], 3.0)


class TestMamariTypeIdentityScoreboard(unittest.TestCase):
    """Stock CV → type-identity snapshot. MockProvider only."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.published_ca7, self.published_ca8 = published_ca7_ca8_stem_counts()
        self.score = score_type_identity(
            self.instances,
            self.ngram_analyzer,
            self.published_ca7,
            self.published_ca8,
        )

    def test_standing_type_identity_snapshot(self):
        """Record stock identity metrics. Later cycles score against this lock."""
        s = self.score
        self.assertEqual(s.instances_per_strip, STANDING_INSTANCES_PER_STRIP)
        self.assertEqual(s.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(s.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertLess(s.unique_cluster_count, CYCLE14_UNIQUE_CLUSTERS)
        self.assertLess(s.unique_cluster_count, CYCLE11_UNIQUE_CLUSTERS)
        self.assertEqual(s.unique_cluster_count, CYCLE9_UNIQUE_CLUSTERS)
        self.assertGreater(s.unique_cluster_count, CYCLE3_UNIQUE_CLUSTERS)
        self.assertLess(s.unique_cluster_count, CYCLE4_UNIQUE_CLUSTERS)
        self.assertLess(s.unique_cluster_count, CYCLE1_SIGNED_UNIQUE_CLUSTERS)
        self.assertEqual(
            mixed_repeating_ngrams(ca7_ca8_sequences(self.instances), self.ngram_analyzer),
            list(STANDING_MIXED_REPEATING),
        )
        self.assertAlmostEqual(
            s.unique_instance_ratio,
            STANDING_UNIQUE_CLUSTERS / s.instance_count,
            places=6,
        )
        self.assertEqual(s.max_repeating_n, STANDING_MAX_REPEATING_N)
        self.assertEqual(s.has_mixed_repeating, STANDING_HAS_MIXED_REPEATING)
        self.assertEqual(s.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(s.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(s.published_ca7_stems, 43)
        self.assertEqual(s.published_ca8_stems, 40)
        self.assertEqual(s.ca7_length, s.published_ca7_stems)
        self.assertEqual(s.ca8_length, s.published_ca8_stems)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_split_fragments_are_marked(self):
        """Four 3-part valley splits: 12 parts carry from_ligature_split."""
        marked = [inst for inst in self.instances if inst.from_ligature_split]
        self.assertEqual(len(marked), STANDING_SPLIT_FRAGMENT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_sca0701_opening_crescents_share_one_id(self):
        """Same-line stitch merges the six crescents; Hu residual still > eps."""
        crescents = isolate_sca0701_opening_crescents(self.instances)
        self.assertEqual(len(crescents), CRESCENT_COUNT)
        ids = [inst.cluster_id for inst in crescents]
        self.assertEqual(len(set(ids)), 1, f"crescents should share an ID: {ids}")
        pairs = pairwise_log_hu_distances(crescents)
        self.assertEqual(len(pairs), CRESCENT_COUNT * (CRESCENT_COUNT - 1) // 2)
        eps = ProcessorConfig().dbscan_eps
        distances = [dist for _a, _b, dist in pairs]
        self.assertTrue(all(dist > eps for dist in distances), pairs)
        # Closest pair still just above eps; farthest is now ~3.4, not ~80.
        self.assertGreater(min(distances), eps)
        self.assertLess(min(distances), 1.0)
        self.assertGreater(max(distances), 3.0)
        self.assertLess(max(distances), 4.0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_split_disabled_restores_cycle3_snapshot(self):
        """split_wide_ligatures=False keeps the cycle-3 75/58 / 39+36 lock."""
        raw = GlyphProcessor(
            ProcessorConfig(
                split_wide_ligatures=False,
                delimiter_slot_merge=False,
                global_type_consistency_merge=False,
            )
        )
        instances = process_tracings(self.paths, processor=raw)
        score = score_type_identity(
            instances,
            self.ngram_analyzer,
            self.published_ca7,
            self.published_ca8,
        )
        self.assertEqual(score.instances_per_strip, CYCLE3_INSTANCES_PER_STRIP)
        self.assertEqual(score.unique_cluster_count, CYCLE3_UNIQUE_CLUSTERS)
        self.assertEqual(score.ca7_length, CYCLE3_CA7_LEN)
        self.assertEqual(score.ca8_length, CYCLE3_CA8_LEN)
        crescents = isolate_sca0701_opening_crescents(instances)
        ids = [inst.cluster_id for inst in crescents]
        self.assertEqual(len(set(ids)), 1, ids)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_global_merge_disabled_restores_cycle14_snapshot(self):
        """global_type_consistency_merge=False keeps the cycle-14 64-type lock."""
        raw = GlyphProcessor(ProcessorConfig(global_type_consistency_merge=False))
        instances = process_tracings(self.paths, processor=raw)
        score = score_type_identity(
            instances,
            self.ngram_analyzer,
            self.published_ca7,
            self.published_ca8,
        )
        self.assertEqual(score.unique_cluster_count, CYCLE14_UNIQUE_CLUSTERS)
        self.assertEqual(
            mixed_repeating_ngrams(ca7_ca8_sequences(instances), self.ngram_analyzer),
            list(CYCLE14_MIXED_REPEATING),
        )
        self.assertEqual(score.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(score.ca8_length, STANDING_CA8_LEN)
        crescents = isolate_sca0701_opening_crescents(instances)
        ids = [inst.cluster_id for inst in crescents]
        self.assertEqual(len(set(ids)), 1, ids)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_slot_merge_disabled_restores_cycle11_snapshot(self):
        """delimiter_slot_merge=False keeps the cycle-11 66-type / G003 G008 lock."""
        raw = GlyphProcessor(
            ProcessorConfig(
                delimiter_slot_merge=False,
                global_type_consistency_merge=False,
            )
        )
        instances = process_tracings(self.paths, processor=raw)
        score = score_type_identity(
            instances,
            self.ngram_analyzer,
            self.published_ca7,
            self.published_ca8,
        )
        self.assertEqual(score.unique_cluster_count, CYCLE11_UNIQUE_CLUSTERS)
        self.assertEqual(
            mixed_repeating_ngrams(ca7_ca8_sequences(instances), self.ngram_analyzer),
            list(CYCLE11_MIXED_REPEATING),
        )
        self.assertEqual(score.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(score.ca8_length, STANDING_CA8_LEN)
        crescents = isolate_sca0701_opening_crescents(instances)
        ids = [inst.cluster_id for inst in crescents]
        self.assertEqual(len(set(ids)), 1, ids)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_inconsistent_split_disabled_restores_cycle9_snapshot(self):
        """split_inconsistent_types=False keeps the cycle-9 62-type / 3-gram lock."""
        raw = GlyphProcessor(
            ProcessorConfig(
                split_inconsistent_types=False,
                delimiter_slot_merge=False,
                global_type_consistency_merge=False,
            )
        )
        instances = process_tracings(self.paths, processor=raw)
        score = score_type_identity(
            instances,
            self.ngram_analyzer,
            self.published_ca7,
            self.published_ca8,
        )
        self.assertEqual(score.unique_cluster_count, CYCLE9_UNIQUE_CLUSTERS)
        self.assertEqual(
            mixed_repeating_ngrams(ca7_ca8_sequences(instances), self.ngram_analyzer),
            list(CYCLE9_MIXED_REPEATING),
        )
        self.assertEqual(score.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(score.ca8_length, STANDING_CA8_LEN)
        crescents = isolate_sca0701_opening_crescents(instances)
        ids = [inst.cluster_id for inst in crescents]
        self.assertEqual(len(set(ids)), 1, ids)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_split_fragment_merge_disabled_restores_cycle4_snapshot(self):
        """Cycle-4 path: no split-fragment stitch and no consistency split."""
        raw = GlyphProcessor(
            ProcessorConfig(
                split_fragment_allograph_merge=False,
                split_inconsistent_types=False,
                delimiter_slot_merge=False,
                global_type_consistency_merge=False,
            )
        )
        instances = process_tracings(self.paths, processor=raw)
        score = score_type_identity(
            instances,
            self.ngram_analyzer,
            self.published_ca7,
            self.published_ca8,
        )
        self.assertEqual(score.unique_cluster_count, CYCLE4_UNIQUE_CLUSTERS)
        self.assertFalse(score.has_mixed_repeating)
        self.assertEqual(score.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(score.ca8_length, STANDING_CA8_LEN)
        crescents = isolate_sca0701_opening_crescents(instances)
        ids = [inst.cluster_id for inst in crescents]
        self.assertEqual(len(set(ids)), 1, ids)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_merge_disabled_restores_cycle2_snapshot(self):
        """same_line_allograph_merge=False keeps the cycle-2 65-type lock."""
        raw = GlyphProcessor(
            ProcessorConfig(
                same_line_allograph_merge=False,
                split_wide_ligatures=False,
                delimiter_slot_merge=False,
                global_type_consistency_merge=False,
            )
        )
        instances = process_tracings(self.paths, processor=raw)
        score = score_type_identity(
            instances,
            self.ngram_analyzer,
            self.published_ca7,
            self.published_ca8,
        )
        self.assertEqual(score.unique_cluster_count, CYCLE2_UNSIGNED_UNIQUE_CLUSTERS)
        crescents = isolate_sca0701_opening_crescents(instances)
        ids = [inst.cluster_id for inst in crescents]
        self.assertEqual(len(set(ids)), CRESCENT_COUNT, ids)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_signed_hu_preserves_cycle1_snapshot(self):
        """hu_sign_mode='signed' keeps the cycle-1 71-type / sign-flip lock."""
        signed = GlyphProcessor(
            ProcessorConfig(
                hu_sign_mode="signed",
                same_line_allograph_merge=False,
                split_wide_ligatures=False,
                delimiter_slot_merge=False,
                global_type_consistency_merge=False,
            )
        )
        instances = process_tracings(self.paths, processor=signed)
        score = score_type_identity(
            instances,
            self.ngram_analyzer,
            self.published_ca7,
            self.published_ca8,
        )
        self.assertEqual(score.instance_count, sum(CYCLE3_INSTANCES_PER_STRIP.values()))
        self.assertEqual(score.unique_cluster_count, CYCLE1_SIGNED_UNIQUE_CLUSTERS)
        crescents = isolate_sca0701_opening_crescents(instances)
        ids = [inst.cluster_id for inst in crescents]
        self.assertEqual(len(set(ids)), CRESCENT_COUNT, ids)
        distances = [dist for _a, _b, dist in pairwise_log_hu_distances(crescents)]
        self.assertGreater(min(distances), ProcessorConfig().dbscan_eps)
        self.assertGreater(max(distances), 50.0)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
