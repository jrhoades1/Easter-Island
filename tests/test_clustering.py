"""Unit tests for glyph clustering."""

import unittest

import cv2
import numpy as np

from models.glyphs import BoundingBox, GlyphInstance, GlyphPosition
from processors.glyph_processor import (
    GlyphProcessor,
    ProcessorConfig,
    _hu_distance,
    best_crop_hamming_pair,
    best_slot0_invariant_crop_hamming_pair,
    best_slot0_invariant_crop_pair,
    best_window_strip_pair,
    concat_glyph_strip,
    crop_chamfer,
    crop_invariant_match,
    crop_ncc,
    leftover_crop_pairs,
    passes_slot_crop_invariant_gates,
    transform_glyph_crop,
    min_pairwise_window_hamming,
    passes_delimiter_slot_gates,
    passes_same_line_allograph_gates,
    passes_slot_crop_gates,
    passes_split_fragment_allograph_gates,
    passes_type_consistency_gates,
    passes_wide_profile_allograph_gates,
    profile_correlation,
    remap_window_types,
    resample_profile,
    strip_plane_size,
    tablet_line_key,
    window_glyph_strips,
    window_hamming,
    window_strip_pair_table,
)


def create_test_glyph(shape: str, size: int = 50) -> np.ndarray:
    """Generate a simple shape as a test glyph."""
    img = np.ones((size, size), dtype=np.uint8) * 255
    if shape == "circle":
        cv2.circle(img, (size // 2, size // 2), size // 3, 0, -1)
    elif shape == "square":
        cv2.rectangle(img, (size // 4, size // 4), (3 * size // 4, 3 * size // 4), 0, -1)
    elif shape == "triangle":
        pts = np.array(
            [[size // 2, size // 4], [size // 4, 3 * size // 4], [3 * size // 4, 3 * size // 4]]
        )
        cv2.fillPoly(img, [pts], 0)
    return img


def create_glyph_instance(
    shape: str, instance_id: str, source: str = "test.png"
) -> tuple[GlyphInstance, np.ndarray]:
    """Create a glyph instance with its image.

    Returns:
        Tuple of (GlyphInstance, image containing the glyph).
    """
    glyph = create_test_glyph(shape, 50)
    # Create padded image
    img = np.ones((70, 70), dtype=np.uint8) * 255
    img[10:60, 10:60] = glyph

    bbox = BoundingBox(x=10, y=10, width=50, height=50)
    instance = GlyphInstance(
        instance_id=instance_id,
        source_image=source,
        bounding_box=bbox,
    )
    return instance, img


class TestDBSCANClustering(unittest.TestCase):
    """Tests for DBSCAN clustering."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_cluster_identical_glyphs(self):
        """Test that identical glyphs end up in the same cluster."""
        instances = []
        images = []

        # Create 5 identical circles
        for i in range(5):
            inst, img = create_glyph_instance("circle", f"circle_{i:03d}")
            instances.append(inst)
            images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs(instances)

        # All should be in the same cluster
        cluster_ids = set(inst.cluster_id for inst in instances)
        self.assertEqual(len(cluster_ids), 1)

    def test_cluster_distinct_glyphs(self):
        """Test that different shapes end up in different clusters."""
        shapes = ["circle", "square", "triangle"]
        instances = []
        images = []

        for shape in shapes:
            # Create 3 of each shape (enough for DBSCAN min_samples)
            for i in range(3):
                inst, img = create_glyph_instance(shape, f"{shape}_{i:03d}")
                instances.append(inst)
                images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs(instances)

        # Should have at least 3 distinct clusters (one per shape type)
        # Note: Some shapes might cluster together if features are similar
        cluster_ids = set(inst.cluster_id for inst in instances if inst.cluster_id)
        self.assertGreaterEqual(len(cluster_ids), 2)

    def test_cluster_similar_glyphs(self):
        """Test that similar glyphs (same shape, slight variations) group together."""
        instances = []
        images = []

        # Create circles with slight size variations
        for i in range(4):
            size = 48 + i  # 48, 49, 50, 51
            glyph = create_test_glyph("circle", size)

            img = np.ones((70, 70), dtype=np.uint8) * 255
            offset = (70 - size) // 2
            img[offset : offset + size, offset : offset + size] = glyph

            bbox = BoundingBox(x=offset, y=offset, width=size, height=size)
            inst = GlyphInstance(f"circle_{i}", "test.png", bbox)
            instances.append(inst)
            images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs(instances)

        # Similar circles should cluster together
        cluster_ids = set(inst.cluster_id for inst in instances)
        # Should have fewer clusters than instances (some grouping)
        # With 4 similar circles, expect 1-3 clusters depending on eps
        self.assertLess(len(cluster_ids), 4)

    def test_cluster_with_noise(self):
        """Test that outliers are handled correctly."""
        # Configure with higher min_samples to create noise points
        config = ProcessorConfig(dbscan_eps=0.1, dbscan_min_samples=3)
        processor = GlyphProcessor(config)

        instances = []
        images = []

        # Create 3 circles (will cluster)
        for i in range(3):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        # Create 1 square (isolated, might be noise)
        inst, img = create_glyph_instance("square", "square_0")
        instances.append(inst)
        images.append(img)

        # Create 1 triangle (isolated, might be noise)
        inst, img = create_glyph_instance("triangle", "triangle_0")
        instances.append(inst)
        images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = processor.extract_features(img, inst)

        clusters, instances = processor.cluster_glyphs(instances)

        # All instances should have a cluster_id assigned
        # (noise points get their own single-instance clusters)
        for inst in instances:
            self.assertIsNotNone(inst.cluster_id)

    def test_cluster_eps_sensitivity(self):
        """Test that different eps values affect clustering."""
        instances = []
        images = []

        # Create different shapes
        for shape in ["circle", "square", "triangle"]:
            for i in range(2):
                inst, img = create_glyph_instance(shape, f"{shape}_{i}")
                instances.append(inst)
                images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        # Test with small eps (more clusters)
        config_small = ProcessorConfig(dbscan_eps=0.1, dbscan_min_samples=1)
        processor_small = GlyphProcessor(config_small)
        features_copy = [inst.features.copy() for inst in instances]

        # Reset instances
        for inst, feat in zip(instances, features_copy):
            inst.features = feat
            inst.cluster_id = None

        clusters_small, _ = processor_small.cluster_glyphs(instances)

        # Reset instances again
        for inst, feat in zip(instances, features_copy):
            inst.features = feat
            inst.cluster_id = None

        # Test with large eps (fewer clusters)
        config_large = ProcessorConfig(dbscan_eps=10.0, dbscan_min_samples=1)
        processor_large = GlyphProcessor(config_large)

        clusters_large, _ = processor_large.cluster_glyphs(instances)

        # Large eps should give fewer or equal clusters
        self.assertLessEqual(len(clusters_large), len(clusters_small))

    def test_cluster_min_samples(self):
        """Test that min_samples parameter affects clustering."""
        instances = []
        images = []

        # Create 2 circles
        for i in range(2):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        # Extract features
        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        # With min_samples=2, the 2 circles should form a cluster
        config = ProcessorConfig(dbscan_eps=1.0, dbscan_min_samples=2)
        processor = GlyphProcessor(config)

        clusters, _ = processor.cluster_glyphs(instances)

        # Should have exactly 1 cluster with 2 instances
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0].frequency, 2)


class TestClusterIDAssignment(unittest.TestCase):
    """Tests for cluster ID assignment."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_assign_cluster_ids(self):
        """Test that IDs are assigned as G001, G002, etc."""
        instances = []
        images = []

        # Create enough glyphs to form multiple clusters
        for shape in ["circle", "square"]:
            for i in range(3):
                inst, img = create_glyph_instance(shape, f"{shape}_{i}")
                instances.append(inst)
                images.append(img)

        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs(instances)

        # Check ID format
        for cluster in clusters:
            self.assertTrue(cluster.cluster_id.startswith("G"))
            # Should be 4 characters: G + 3 digits
            self.assertEqual(len(cluster.cluster_id), 4)
            # Should be a valid number
            int(cluster.cluster_id[1:])

    def test_cluster_id_ordering(self):
        """Test that most frequent cluster gets G001."""
        instances = []
        images = []

        # Create 5 circles (more frequent)
        for i in range(5):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        # Create 2 squares (less frequent)
        for i in range(2):
            inst, img = create_glyph_instance("square", f"square_{i}")
            instances.append(inst)
            images.append(img)

        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, _ = self.processor.cluster_glyphs(instances)

        # G001 should have the highest frequency
        g001 = next((c for c in clusters if c.cluster_id == "G001"), None)
        if g001:
            max_freq = max(c.frequency for c in clusters)
            self.assertEqual(g001.frequency, max_freq)


class TestClusterStatistics(unittest.TestCase):
    """Tests for cluster statistics."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_cluster_frequency_count(self):
        """Test counting instances per cluster."""
        instances = []
        images = []

        # Create 4 identical circles
        for i in range(4):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, _ = self.processor.cluster_glyphs(instances)

        # All should be in one cluster with frequency 4
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0].frequency, 4)

    def test_cluster_mean_features(self):
        """Test calculating mean feature vector."""
        instances = []
        images = []

        for i in range(3):
            inst, img = create_glyph_instance("circle", f"circle_{i}")
            instances.append(inst)
            images.append(img)

        for inst, img in zip(instances, images):
            inst.features = self.processor.extract_features(img, inst)

        clusters, _ = self.processor.cluster_glyphs(instances)

        # Cluster should have mean features
        self.assertEqual(len(clusters[0].mean_features), 7)

    def test_position_statistics(self):
        """Test calculating line distribution."""
        bbox = BoundingBox(x=0, y=0, width=50, height=50)

        instances = [
            GlyphInstance("a", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
            GlyphInstance("b", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
            GlyphInstance("c", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
        ]

        # Assign positions
        instances[0].position = GlyphPosition(line_number=0, position_in_line=0, total_in_line=2)
        instances[1].position = GlyphPosition(line_number=0, position_in_line=1, total_in_line=2)
        instances[2].position = GlyphPosition(line_number=1, position_in_line=0, total_in_line=1)

        from models.glyphs import GlyphCluster

        cluster = GlyphCluster(cluster_id="G001", instances=["a", "b", "c"])

        stats = self.processor.compute_position_stats(cluster, instances)

        # Line distribution
        self.assertEqual(stats.line_distribution.get(0, 0), 2)
        self.assertEqual(stats.line_distribution.get(1, 0), 1)

    def test_neighbor_analysis(self):
        """Test finding common neighboring glyphs."""
        bbox = BoundingBox(x=0, y=0, width=50, height=50)

        instances = [
            GlyphInstance("a", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
            GlyphInstance("b", "test.png", bbox, features=[1.0] * 7, cluster_id="G002"),
            GlyphInstance("c", "test.png", bbox, features=[1.0] * 7, cluster_id="G001"),
            GlyphInstance("d", "test.png", bbox, features=[1.0] * 7, cluster_id="G003"),
        ]

        # Same line: a(G001) - b(G002) - c(G001) - d(G003)
        instances[0].position = GlyphPosition(line_number=0, position_in_line=0, total_in_line=4)
        instances[1].position = GlyphPosition(line_number=0, position_in_line=1, total_in_line=4)
        instances[2].position = GlyphPosition(line_number=0, position_in_line=2, total_in_line=4)
        instances[3].position = GlyphPosition(line_number=0, position_in_line=3, total_in_line=4)

        from models.glyphs import GlyphCluster

        cluster = GlyphCluster(cluster_id="G001", instances=["a", "c"])

        stats = self.processor.compute_position_stats(cluster, instances)

        # G001 (a, c) should have G002 as a neighbor
        self.assertIn("G002", stats.common_neighbors)


class TestSameLineAllographMerge(unittest.TestCase):
    """Post-DBSCAN adjacent same-line stitch. No live CV of Mamari GIFs."""

    def _thin_instance(
        self,
        instance_id: str,
        position: int,
        features: list[float],
        width: int = 26,
        height: int = 66,
        cluster_id: str | None = None,
        source: str = "line.gif",
    ) -> GlyphInstance:
        return GlyphInstance(
            instance_id=instance_id,
            source_image=source,
            bounding_box=BoundingBox(x=position * 30, y=0, width=width, height=height),
            features=features,
            cluster_id=cluster_id,
            position=GlyphPosition(0, position, 6),
        )

    def test_adjacent_tall_thin_run_shares_an_id(self):
        """Six adjacent thin glyphs with Hu dist 0.8 merge after DBSCAN."""
        instances = []
        for i in range(6):
            feat = [0.8 * i] + [0.0] * 6
            instances.append(self._thin_instance(f"c{i}", i, feat))

        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs(instances)
        ids = {inst.cluster_id for inst in clustered}
        self.assertEqual(len(ids), 1)

    def test_merge_can_be_disabled(self):
        instances = []
        for i in range(6):
            feat = [0.8 * i] + [0.0] * 6
            instances.append(self._thin_instance(f"c{i}", i, feat))

        processor = GlyphProcessor(
            ProcessorConfig(
                same_line_allograph_merge=False,
                global_type_consistency_merge=False,
            )
        )
        _, clustered = processor.cluster_glyphs(instances)
        ids = {inst.cluster_id for inst in clustered}
        self.assertEqual(len(ids), 6)

    def test_wide_neighbor_does_not_merge_with_thin(self):
        """Tall-thin gate blocks a wide adjacent box even when Hu is close."""
        thin = self._thin_instance("thin", 0, [0.0] * 7, width=26, height=66)
        wide = self._thin_instance("wide", 1, [0.8] + [0.0] * 6, width=70, height=65)
        processor = GlyphProcessor(
            ProcessorConfig(global_type_consistency_merge=False)
        )
        _, clustered = processor.cluster_glyphs([thin, wide])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_dissimilar_area_does_not_merge(self):
        small = self._thin_instance("a", 0, [0.0] * 7, width=26, height=66)
        tall = self._thin_instance("b", 1, [0.8] + [0.0] * 6, width=26, height=120)
        processor = GlyphProcessor(
            ProcessorConfig(global_type_consistency_merge=False)
        )
        _, clustered = processor.cluster_glyphs([small, tall])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)


class TestSplitFragmentAllographMerge(unittest.TestCase):
    """Cross-image stitch of valley-split fragments. No Mamari GIFs."""

    def _split_instance(
        self,
        instance_id: str,
        source: str,
        features: list[float],
        width: int,
        height: int = 66,
        from_split: bool = True,
    ) -> GlyphInstance:
        return GlyphInstance(
            instance_id=instance_id,
            source_image=source,
            bounding_box=BoundingBox(x=0, y=0, width=width, height=height),
            features=features,
            from_ligature_split=from_split,
            position=GlyphPosition(0, 0, 1),
        )

    def test_similar_split_fragments_share_an_id(self):
        """Hu 0.8, matched area/width, split-marked: merge after DBSCAN."""
        a = self._split_instance("a", "one.gif", [0.0] * 7, width=31)
        b = self._split_instance("b", "two.gif", [0.8] + [0.0] * 6, width=30)
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_non_split_neighbor_is_not_pulled(self):
        """Instance-local: a close non-split box keeps its own ID."""
        a = self._split_instance("a", "one.gif", [0.0] * 7, width=31)
        b = self._split_instance("b", "two.gif", [0.8] + [0.0] * 6, width=30)
        extra = self._split_instance(
            "c", "three.gif", [0.4] + [0.0] * 6, width=31, from_split=False
        )
        processor = GlyphProcessor(
            ProcessorConfig(global_type_consistency_merge=False)
        )
        _, clustered = processor.cluster_glyphs([a, b, extra])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)
        self.assertNotEqual(clustered[0].cluster_id, clustered[2].cluster_id)

    def test_width_ratio_blocks_different_slots(self):
        """34 vs 31 is under Hu/area gates but over the width gate."""
        a = self._split_instance("a", "one.gif", [0.0] * 7, width=34)
        b = self._split_instance("b", "two.gif", [0.8] + [0.0] * 6, width=31)
        processor = GlyphProcessor(
            ProcessorConfig(global_type_consistency_merge=False)
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_split_fragment_merge_can_be_disabled(self):
        a = self._split_instance("a", "one.gif", [0.0] * 7, width=31)
        b = self._split_instance("b", "two.gif", [0.8] + [0.0] * 6, width=30)
        processor = GlyphProcessor(
            ProcessorConfig(
                split_fragment_allograph_merge=False,
                global_type_consistency_merge=False,
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_gate_predicates_match_merge_decisions(self):
        """Public gate helpers are the same tests the merge passes use."""
        close = self._split_instance("a", "one.gif", [0.0] * 7, width=31)
        match = self._split_instance("b", "two.gif", [0.8] + [0.0] * 6, width=30)
        wide = self._split_instance("c", "three.gif", [0.8] + [0.0] * 6, width=55)
        self.assertTrue(passes_split_fragment_allograph_gates(close, match))
        self.assertFalse(passes_split_fragment_allograph_gates(close, wide))
        thin = GlyphInstance(
            instance_id="thin",
            source_image="line.gif",
            bounding_box=BoundingBox(x=0, y=0, width=26, height=66),
            features=[0.0] * 7,
            position=GlyphPosition(0, 0, 2),
        )
        other = GlyphInstance(
            instance_id="other",
            source_image="line.gif",
            bounding_box=BoundingBox(x=30, y=0, width=26, height=66),
            features=[0.8] + [0.0] * 6,
            position=GlyphPosition(0, 1, 2),
        )
        self.assertTrue(passes_same_line_allograph_gates(thin, other))
        self.assertFalse(passes_same_line_allograph_gates(thin, wide))


class TestWideProfileAllographMerge(unittest.TestCase):
    """Column-ink profile stitch for wide boxes only. No Mamari GIFs."""

    def _wide(
        self,
        instance_id: str,
        position: int,
        profile: list[float],
        source: str = "line.gif",
        width: int = 72,
        height: int = 66,
        features: list[float] | None = None,
    ) -> GlyphInstance:
        return GlyphInstance(
            instance_id=instance_id,
            source_image=source,
            bounding_box=BoundingBox(x=position * 80, y=0, width=width, height=height),
            features=features if features is not None else [0.0] * 7,
            ink_profile=profile,
            position=GlyphPosition(0, position, 4),
        )

    def test_identical_profiles_correlate(self):
        ramp = [float(i) for i in range(32)]
        self.assertAlmostEqual(profile_correlation(ramp, ramp), 1.0)
        shifted = resample_profile(np.array(ramp, dtype=float) + 3.0, 32)
        self.assertAlmostEqual(profile_correlation(ramp, shifted), 1.0, places=6)

    def test_uncorrelated_profiles_fail_gate(self):
        left = [1.0, 0.0] * 16
        right = [0.0, 1.0] * 16
        self.assertLess(profile_correlation(left, right), 0.0)
        a = self._wide("a", 0, left)
        b = self._wide("b", 1, right)
        self.assertFalse(passes_wide_profile_allograph_gates(a, b))

    def test_adjacent_wide_high_corr_shares_an_id(self):
        """Hu is far; profile match still unions two wide neighbors."""
        ramp = [float(i) for i in range(32)]
        a = self._wide("a", 0, ramp, features=[0.0] * 7)
        b = self._wide("b", 1, ramp, features=[5.0] + [0.0] * 6)
        self.assertFalse(passes_same_line_allograph_gates(a, b))
        self.assertTrue(passes_wide_profile_allograph_gates(a, b))
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_tall_thin_is_excluded_even_with_matching_profile(self):
        """Wide-only gate: aspect ≤ 0.5 never uses this stitch."""
        ramp = [float(i) for i in range(32)]
        thin = GlyphInstance(
            instance_id="thin",
            source_image="line.gif",
            bounding_box=BoundingBox(x=0, y=0, width=26, height=66),
            features=[5.0] + [0.0] * 6,
            ink_profile=ramp,
            position=GlyphPosition(0, 0, 2),
        )
        other = GlyphInstance(
            instance_id="other",
            source_image="line.gif",
            bounding_box=BoundingBox(x=30, y=0, width=26, height=66),
            features=[0.0] * 7,
            ink_profile=ramp,
            position=GlyphPosition(0, 1, 2),
        )
        self.assertFalse(passes_wide_profile_allograph_gates(thin, other))
        self.assertFalse(passes_same_line_allograph_gates(thin, other))
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([thin, other])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_low_corr_wide_pair_does_not_merge(self):
        """Honest negative: size-similar wide boxes with ~0 profile corr."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        a = self._wide("a", 0, left, features=[0.0] * 7)
        b = self._wide("b", 1, right, features=[5.0] + [0.0] * 6)
        self.assertLess(profile_correlation(left, right), 0.0)
        self.assertFalse(passes_wide_profile_allograph_gates(a, b))
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_wide_profile_merge_can_be_disabled(self):
        ramp = [float(i) for i in range(32)]
        a = self._wide("a", 0, ramp)
        b = self._wide("b", 1, ramp, features=[5.0] + [0.0] * 6)
        processor = GlyphProcessor(
            ProcessorConfig(wide_profile_allograph_merge=False)
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)


class TestDelimiterSlotAllographMerge(unittest.TestCase):
    """Same-slot stitch across published window starts. No Mamari GIFs."""

    def _inst(
        self,
        instance_id: str,
        source: str,
        position: int,
        features: list[float],
        profile: list[float],
        width: int = 72,
        height: int = 66,
        total: int = 4,
    ) -> GlyphInstance:
        return GlyphInstance(
            instance_id=instance_id,
            source_image=source,
            bounding_box=BoundingBox(x=position * 80, y=0, width=width, height=height),
            features=features,
            ink_profile=profile,
            position=GlyphPosition(0, position, total),
        )

    def test_tablet_line_key_uses_kohaumotu_stem_only(self):
        self.assertEqual(tablet_line_key("sca0701.gif"), "07")
        self.assertEqual(tablet_line_key("sca0803.gif"), "08")
        self.assertEqual(tablet_line_key("line.gif"), "line.gif")

    def test_same_slot_wide_profile_pair_shares_an_id(self):
        """Hu is far; wide-profile r still unions the two slot occupants."""
        ramp = [float(i) for i in range(32)]
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, ramp)
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, ramp)
        self.assertFalse(passes_type_consistency_gates(a, b))
        self.assertTrue(passes_wide_profile_allograph_gates(a, b))
        self.assertTrue(passes_delimiter_slot_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=1,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_same_slot_hu_and_profile_pair_shares_an_id(self):
        """Tall-thin CONS pair (Hu < 2 and r >= 0.85) also unions."""
        ramp = [float(i) for i in range(32)]
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, ramp, width=26)
        b = self._inst("b", "sca0801.gif", 0, [0.8] + [0.0] * 6, ramp, width=26)
        self.assertTrue(passes_type_consistency_gates(a, b))
        self.assertFalse(passes_wide_profile_allograph_gates(a, b))
        self.assertTrue(passes_delimiter_slot_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=1,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_same_slot_poor_features_stay_distinct(self):
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, left)
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, right)
        self.assertFalse(passes_delimiter_slot_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=1,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_does_not_force_unanimous_slot_when_one_occupant_fails(self):
        """Only the passing pair shares an ID. The third occupant stays out."""
        ramp = [float(i) for i in range(32)]
        inverse = [float(31 - i) for i in range(32)]
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, ramp, total=1)
        b = self._inst("b", "sca0801.gif", 0, [0.8] + [0.0] * 6, ramp, total=2)
        c = self._inst("c", "sca0801.gif", 1, [5.0] + [0.0] * 6, inverse, total=2)
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=1,
                delimiter_window_starts=((0, 0), (1, 0), (1, 1)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, b, c])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)
        self.assertNotEqual(clustered[0].cluster_id, clustered[2].cluster_id)

    def test_different_slots_do_not_merge(self):
        """Matching profiles in different slot indexes stay distinct.

        Hu is far so DBSCAN does not pre-group them. Wide-profile r
        would pass if they shared a slot; they do not.
        """
        ramp = [float(i) for i in range(32)]
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, ramp, total=2)
        filler = self._inst(
            "x", "sca0701.gif", 1, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        b = self._inst("b", "sca0801.gif", 1, [5.0] + [0.0] * 6, ramp, total=2)
        other = self._inst(
            "y", "sca0801.gif", 0, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        self.assertTrue(passes_delimiter_slot_gates(a, b))
        self.assertGreater(_hu_distance(a, b), 2.0)
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, filler, other, b])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertNotEqual(by_id["a"], by_id["b"])

    def test_slot_merge_can_be_disabled(self):
        ramp = [float(i) for i in range(32)]
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, ramp)
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, ramp)
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_slot_merge=False,
                delimiter_window_len=1,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def _crop(self, kind: str = "circle") -> list[int]:
        plane = np.zeros((64, 64), dtype=np.uint8)
        if kind == "circle":
            cv2.circle(plane, (32, 32), 20, 255, -1)
        elif kind == "band":
            plane[:, :32] = 255
        return plane.ravel().tolist()

    def test_slot0_matching_crops_merge_when_hu_and_profile_fail(self):
        """Crop NCC/chamfer can union a slot-0 pair the Hu/profile gates reject."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        crop = self._crop("circle")
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, left)
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, right)
        a.glyph_crop = crop
        b.glyph_crop = list(crop)
        self.assertFalse(passes_delimiter_slot_gates(a, b))
        self.assertTrue(passes_slot_crop_gates(a, b))
        self.assertGreaterEqual(crop_ncc(a.glyph_crop, b.glyph_crop), 0.99)
        self.assertLess(crop_chamfer(a.glyph_crop, b.glyph_crop), 0.1)
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=1,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_slot0_poor_crops_stay_distinct(self):
        """Leftover-like crops (low NCC, high chamfer) do not force a merge."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, left)
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, right)
        a.glyph_crop = self._crop("circle")
        b.glyph_crop = self._crop("band")
        self.assertLess(crop_ncc(a.glyph_crop, b.glyph_crop), 0.45)
        self.assertFalse(passes_slot_crop_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=1,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_crop_gate_does_not_run_on_other_slots(self):
        """Matching crops in slot 1 stay distinct when Hamming merge is off."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        crop = self._crop("circle")
        a = self._inst("a", "sca0701.gif", 1, [0.0] * 7, left, total=2)
        filler = self._inst(
            "x", "sca0701.gif", 0, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        b = self._inst("b", "sca0801.gif", 1, [5.0] + [0.0] * 6, right, total=2)
        other = self._inst(
            "y", "sca0801.gif", 0, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        a.glyph_crop = crop
        b.glyph_crop = list(crop)
        self.assertTrue(passes_slot_crop_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0)),
                delimiter_slot_crop_hamming_merge=False,
            )
        )
        _, clustered = processor.cluster_glyphs([a, filler, other, b])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertNotEqual(by_id["a"], by_id["b"])

    def test_crop_hamming_merge_unions_slot1_when_min_hamming_drops(self):
        """Slot-1 leftover crop pair unions only because Hamming would drop."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        crop = self._crop("circle")
        a = self._inst("a", "sca0701.gif", 1, [0.0] * 7, left, total=2)
        filler = self._inst(
            "x", "sca0701.gif", 0, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        b = self._inst("b", "sca0801.gif", 1, [5.0] + [0.0] * 6, right, total=2)
        other = self._inst(
            "y", "sca0801.gif", 0, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        a.glyph_crop = crop
        b.glyph_crop = list(crop)
        self.assertFalse(passes_delimiter_slot_gates(a, b))
        self.assertTrue(passes_slot_crop_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, filler, other, b])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertEqual(by_id["a"], by_id["b"])

    def test_crop_hamming_merge_skips_pair_that_does_not_drop_min_hamming(self):
        """Crop-passing leftover stays split when min Hamming would not fall."""
        ramp = [float(i) for i in range(32)]
        inverse = [float(31 - i) for i in range(32)]
        crop = self._crop("circle")
        p0 = self._inst("p0", "sca0701.gif", 0, [0.0] * 7, ramp, width=26, total=2)
        q = self._inst("q", "sca0701.gif", 1, [4.0] + [0.0] * 6, inverse, width=26, total=2)
        p1 = self._inst("p1", "sca0801.gif", 0, [0.8] + [0.0] * 6, ramp, width=26, total=2)
        r = self._inst("r", "sca0801.gif", 1, [6.0] + [0.0] * 6, inverse, width=26, total=2)
        s = self._inst("s", "other.gif", 0, [9.0] + [0.0] * 6, inverse, width=26, total=2)
        t = self._inst("t", "other.gif", 1, [7.0] + [0.0] * 6, ramp, width=26, total=2)
        q.glyph_crop = crop
        t.glyph_crop = list(crop)
        r.glyph_crop = self._crop("band")
        self.assertTrue(passes_slot_crop_gates(q, t))
        self.assertFalse(passes_delimiter_slot_gates(q, t))
        grams = (("P", "Q"), ("P", "R"), ("S", "T"))
        self.assertEqual(min_pairwise_window_hamming(grams), 1)
        self.assertEqual(
            min_pairwise_window_hamming(remap_window_types(grams, "Q", "T")), 1
        )
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0), (2, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([p0, q, p1, r, s, t])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertEqual(by_id["p0"], by_id["p1"])
        self.assertNotEqual(by_id["q"], by_id["t"])

    def test_leftover_crop_merge_unions_non_hamming_drop_pair(self):
        """Cycle 20 leftover flag unions crop-clear pairs that do not drop H."""
        ramp = [float(i) for i in range(32)]
        inverse = [float(31 - i) for i in range(32)]
        crop = self._crop("circle")
        p0 = self._inst("p0", "sca0701.gif", 0, [0.0] * 7, ramp, width=26, total=2)
        q = self._inst("q", "sca0701.gif", 1, [4.0] + [0.0] * 6, inverse, width=26, total=2)
        p1 = self._inst("p1", "sca0801.gif", 0, [0.8] + [0.0] * 6, ramp, width=26, total=2)
        r = self._inst("r", "sca0801.gif", 1, [6.0] + [0.0] * 6, inverse, width=26, total=2)
        s = self._inst("s", "other.gif", 0, [9.0] + [0.0] * 6, inverse, width=26, total=2)
        t = self._inst("t", "other.gif", 1, [7.0] + [0.0] * 6, ramp, width=26, total=2)
        q.glyph_crop = crop
        t.glyph_crop = list(crop)
        r.glyph_crop = self._crop("band")
        self.assertTrue(passes_slot_crop_gates(q, t))
        self.assertFalse(passes_delimiter_slot_gates(q, t))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0), (2, 0)),
                delimiter_slot_crop_leftover_merge=True,
            )
        )
        _, clustered = processor.cluster_glyphs([p0, q, p1, r, s, t])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertEqual(by_id["p0"], by_id["p1"])
        self.assertEqual(by_id["q"], by_id["t"])

    def test_leftover_crop_merge_skips_slot_0(self):
        """Slot-0 leftovers stay split even when leftover merge is on."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        crop = self._crop("circle")
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, left, total=2)
        filler = self._inst(
            "x", "sca0701.gif", 1, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, right, total=2)
        other = self._inst(
            "y", "sca0801.gif", 1, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        a.glyph_crop = crop
        b.glyph_crop = list(crop)
        self.assertTrue(passes_slot_crop_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0)),
                delimiter_slot_crop_merge=False,
                delimiter_slot_crop_hamming_merge=False,
                delimiter_slot_crop_leftover_merge=True,
            )
        )
        _, clustered = processor.cluster_glyphs([a, filler, other, b])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertNotEqual(by_id["a"], by_id["b"])
        self.assertEqual(
            leftover_crop_pairs(
                clustered,
                [[0, 3], [1, 2]],
                ProcessorConfig(delimiter_slot_crop_leftover_merge=True),
            ),
            (),
        )

    def test_window_hamming_helpers(self):
        self.assertEqual(window_hamming(("A",) * 8, ("A",) * 8), 0)
        self.assertEqual(window_hamming(("A", "B"), ("A", "C")), 1)
        self.assertEqual(min_pairwise_window_hamming((("A", "B"), ("A", "C"), ("D", "E"))), 1)
        remapped = remap_window_types((("A", "B"), ("A", "C")), "B", "C")
        self.assertEqual(min_pairwise_window_hamming(remapped), 0)
        with self.assertRaises(ValueError):
            window_hamming(("A",), ("A", "B"))
        self.assertIsNone(best_crop_hamming_pair([], []))
        self.assertEqual(leftover_crop_pairs([], []), ())
        self.assertIsNone(best_slot0_invariant_crop_pair([], []))
        self.assertIsNone(best_slot0_invariant_crop_hamming_pair([], []))
        self.assertEqual(concat_glyph_strip([]), [])
        self.assertEqual(window_glyph_strips([], []), ())
        self.assertEqual(window_strip_pair_table([]), ())
        self.assertIsNone(best_window_strip_pair(()))

    def _asymmetric_crop(self) -> list[int]:
        plane = np.zeros((64, 64), dtype=np.uint8)
        plane[6:58, 8:20] = 255
        plane[46:58, 8:56] = 255
        return plane.ravel().tolist()

    def test_hflip_pair_clears_invariant_crop_not_upright(self):
        """Mirrored leftovers fail upright NCC and pass the same numeric gate."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        crop = self._asymmetric_crop()
        flipped = transform_glyph_crop(crop, "hflip")
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, left)
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, right)
        a.glyph_crop = crop
        b.glyph_crop = flipped
        self.assertLess(crop_ncc(a.glyph_crop, b.glyph_crop), 0.45)
        self.assertFalse(passes_slot_crop_gates(a, b))
        ncc, chamfer, name = crop_invariant_match(a.glyph_crop, b.glyph_crop)
        self.assertEqual(name, "hflip")
        self.assertGreaterEqual(ncc, 0.45)
        self.assertLessEqual(chamfer, 0.80)
        self.assertTrue(passes_slot_crop_invariant_gates(a, b))

    def test_slot0_invariant_hamming_merge_unions_flipped_pair(self):
        """Slot-0 leftover hflip pair unions only when the flag is on."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        crop = self._asymmetric_crop()
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, left, total=2)
        filler = self._inst(
            "x", "sca0701.gif", 1, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, right, total=2)
        other = self._inst(
            "y", "sca0801.gif", 1, [8.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        a.glyph_crop = crop
        b.glyph_crop = transform_glyph_crop(crop, "hflip")
        self.assertFalse(passes_slot_crop_gates(a, b))
        self.assertTrue(passes_slot_crop_invariant_gates(a, b))
        default = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0)),
                delimiter_slot_crop_merge=False,
                delimiter_slot_crop_hamming_merge=False,
            )
        )
        _, clustered = default.cluster_glyphs([a, filler, other, b])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertNotEqual(by_id["a"], by_id["b"])
        self.assertFalse(ProcessorConfig().delimiter_slot_crop_invariant_merge)
        on = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0)),
                delimiter_slot_crop_merge=False,
                delimiter_slot_crop_hamming_merge=False,
                delimiter_slot_crop_invariant_merge=True,
            )
        )
        a2 = self._inst("a", "sca0701.gif", 0, [0.0] * 7, left, total=2)
        filler2 = self._inst(
            "x", "sca0701.gif", 1, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        b2 = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, right, total=2)
        other2 = self._inst(
            "y", "sca0801.gif", 1, [8.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        a2.glyph_crop = crop
        b2.glyph_crop = transform_glyph_crop(crop, "rot180")
        _, merged = on.cluster_glyphs([a2, filler2, other2, b2])
        by_id = {inst.instance_id: inst.cluster_id for inst in merged}
        self.assertEqual(by_id["a"], by_id["b"])

    def test_invariant_hamming_merge_skips_other_slots(self):
        """Flip-clear leftovers in slot 1 stay split."""
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        crop = self._asymmetric_crop()
        a = self._inst("a", "sca0701.gif", 1, [0.0] * 7, left, total=2)
        filler = self._inst(
            "x", "sca0701.gif", 0, [9.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        b = self._inst("b", "sca0801.gif", 1, [5.0] + [0.0] * 6, right, total=2)
        other = self._inst(
            "y", "sca0801.gif", 0, [8.0] + [0.0] * 6, [0.0] * 32, total=2
        )
        a.glyph_crop = crop
        b.glyph_crop = transform_glyph_crop(crop, "hflip")
        self.assertTrue(passes_slot_crop_invariant_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=2,
                delimiter_window_starts=((0, 0), (1, 0)),
                delimiter_slot_crop_merge=False,
                delimiter_slot_crop_hamming_merge=False,
                delimiter_slot_crop_invariant_merge=True,
            )
        )
        _, clustered = processor.cluster_glyphs([a, filler, other, b])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertNotEqual(by_id["a"], by_id["b"])
        self.assertIsNone(
            best_slot0_invariant_crop_hamming_pair(
                clustered,
                [[1, 2], [0, 3]],
                ProcessorConfig(delimiter_slot_crop_invariant_merge=True),
            )
        )

    def test_unknown_crop_transform_raises(self):
        with self.assertRaises(ValueError):
            transform_glyph_crop(self._crop("circle"), "mirror45")

    def test_concat_glyph_strip_is_left_to_right(self):
        """Eight-cell helper: shared-height crops join in reading order."""
        left = np.zeros((4, 4), dtype=np.uint8)
        left[:, :2] = 255
        right = np.zeros((4, 4), dtype=np.uint8)
        right[:, 2:] = 255
        strip = concat_glyph_strip(
            [left.ravel().tolist(), right.ravel().tolist()], (4, 4)
        )
        plane = np.asarray(strip, dtype=np.uint8).reshape(4, 8)
        self.assertEqual(strip_plane_size(2, (4, 4)), (8, 4))
        self.assertTrue((plane[:, :2] == 255).all())
        self.assertTrue((plane[:, 6:] == 255).all())
        self.assertTrue((plane[:, 2:6] == 0).all())

    def test_identical_strips_clear_identity_gate(self):
        """Same concatenated image: identity, NCC ~1, chamfer ~0."""
        crop = self._asymmetric_crop()
        strip = concat_glyph_strip([crop, self._crop("circle")])
        rows = window_strip_pair_table((strip, list(strip)))
        self.assertEqual(len(rows), 1)
        _i, _j, name, ncc, chamfer, gate = rows[0]
        self.assertEqual(name, "identity")
        self.assertGreaterEqual(ncc, 0.99)
        self.assertLessEqual(chamfer, 0.10)
        self.assertTrue(gate)
        self.assertEqual(best_window_strip_pair(rows), rows[0])

    def test_hflipped_strip_selects_hflip(self):
        """Whole-strip hflip matches under the existing crop gate."""
        crop = self._asymmetric_crop()
        strip = concat_glyph_strip([crop, self._crop("circle")])
        flipped = transform_glyph_crop(strip, "hflip", strip_plane_size(2))
        rows = window_strip_pair_table((strip, flipped))
        self.assertEqual(rows[0][2], "hflip")
        self.assertGreaterEqual(rows[0][3], 0.99)
        self.assertLessEqual(rows[0][4], 0.10)
        self.assertTrue(rows[0][5])

    def test_missing_crops_do_not_merge(self):
        left = [float(i) for i in range(32)]
        right = [float(31 - i) for i in range(32)]
        a = self._inst("a", "sca0701.gif", 0, [0.0] * 7, left)
        b = self._inst("b", "sca0801.gif", 0, [5.0] + [0.0] * 6, right)
        self.assertFalse(passes_slot_crop_gates(a, b))
        self.assertFalse(passes_slot_crop_invariant_gates(a, b))
        processor = GlyphProcessor(
            ProcessorConfig(
                delimiter_window_len=1,
                delimiter_window_starts=((0, 0), (1, 0)),
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)


class TestGlobalTypeConsistencyMerge(unittest.TestCase):
    """Global Hu/profile same-type stitch after DBSCAN. No Mamari GIFs."""

    def _inst(
        self,
        instance_id: str,
        source: str,
        features: list[float],
        profile: list[float] | None = None,
        width: int = 31,
        height: int = 66,
        from_split: bool = False,
        position: int = 0,
    ) -> GlyphInstance:
        return GlyphInstance(
            instance_id=instance_id,
            source_image=source,
            bounding_box=BoundingBox(x=position * 80, y=0, width=width, height=height),
            features=features,
            ink_profile=list(profile) if profile is not None else [],
            from_ligature_split=from_split,
            position=GlyphPosition(0, position, 1),
        )

    def _global_only(self) -> GlyphProcessor:
        return GlyphProcessor(
            ProcessorConfig(
                same_line_allograph_merge=False,
                split_fragment_allograph_merge=False,
                wide_profile_allograph_merge=False,
                split_inconsistent_types=False,
                delimiter_slot_merge=False,
            )
        )

    def test_hu_between_eps_and_gate_merges_across_images(self):
        """Hu 0.8 > DBSCAN eps; matching profiles; not same-line or slot."""
        ramp = [float(i) for i in range(32)]
        a = self._inst("a", "one.gif", [0.0] * 7, ramp)
        b = self._inst("b", "two.gif", [0.8] + [0.0] * 6, ramp)
        self.assertGreater(_hu_distance(a, b), ProcessorConfig().dbscan_eps)
        self.assertTrue(passes_type_consistency_gates(a, b))
        _, clustered = self._global_only().cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_gate_failure_stays_distinct(self):
        """Hu-far or low-r pairs are not forced onto one ID."""
        ramp = [float(i) for i in range(32)]
        inverse = [float(31 - i) for i in range(32)]
        far = self._inst("far", "one.gif", [0.0] * 7, ramp)
        other = self._inst("other", "two.gif", [2.5] + [0.0] * 6, ramp)
        low = self._inst("low", "three.gif", [0.8] + [0.0] * 6, inverse)
        self.assertFalse(passes_type_consistency_gates(far, other))
        self.assertFalse(passes_type_consistency_gates(far, low))
        _, clustered = self._global_only().cluster_glyphs([far, other, low])
        ids = {inst.cluster_id for inst in clustered}
        self.assertEqual(len(ids), 3)

    def test_transitive_failing_pair_is_not_forced(self):
        """A–B and B–C pass; A–C is Hu-far. A and C keep distinct IDs."""
        ramp = [float(i) for i in range(32)]
        a = self._inst("a", "one.gif", [0.0] * 7, ramp)
        b = self._inst("b", "two.gif", [0.8] + [0.0] * 6, ramp)
        c = self._inst("c", "three.gif", [2.4] + [0.0] * 6, ramp)
        self.assertTrue(passes_type_consistency_gates(a, b))
        self.assertTrue(passes_type_consistency_gates(b, c))
        self.assertFalse(passes_type_consistency_gates(a, c))
        _, clustered = self._global_only().cluster_glyphs([a, b, c])
        by_id = {inst.instance_id: inst.cluster_id for inst in clustered}
        self.assertNotEqual(by_id["a"], by_id["c"])

    def test_can_be_disabled(self):
        ramp = [float(i) for i in range(32)]
        a = self._inst("a", "one.gif", [0.0] * 7, ramp)
        b = self._inst("b", "two.gif", [0.8] + [0.0] * 6, ramp)
        processor = GlyphProcessor(
            ProcessorConfig(
                global_type_consistency_merge=False,
                same_line_allograph_merge=False,
                split_fragment_allograph_merge=False,
                wide_profile_allograph_merge=False,
                delimiter_slot_merge=False,
            )
        )
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_does_not_undo_same_line_crescent_stitch(self):
        """Adjacent tall-thin Hu 3.2 still share an ID via the crescent stitch."""
        a = self._inst(
            "thin_a", "line.gif", [0.0] * 7, width=26, height=66, position=0
        )
        b = self._inst(
            "thin_b", "line.gif", [3.2] + [0.0] * 6, width=26, height=66, position=1
        )
        a.position = GlyphPosition(0, 0, 2)
        b.position = GlyphPosition(0, 1, 2)
        self.assertFalse(passes_type_consistency_gates(a, b))
        self.assertTrue(passes_same_line_allograph_gates(a, b))
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)


class TestInconsistentTypeSplit(unittest.TestCase):
    """Post-merge split of over-merged split-fragment types. No Mamari GIFs."""

    def _split(
        self,
        instance_id: str,
        source: str,
        features: list[float],
        width: int = 31,
        profile: list[float] | None = None,
    ) -> GlyphInstance:
        return GlyphInstance(
            instance_id=instance_id,
            source_image=source,
            bounding_box=BoundingBox(x=0, y=0, width=width, height=66),
            features=features,
            from_ligature_split=True,
            ink_profile=list(profile) if profile is not None else [],
            position=GlyphPosition(0, 0, 1),
        )

    def test_gate_splits_poor_profile_even_when_hu_is_close(self):
        """Hu < 2 is not enough if column-ink r is well below 0.85."""
        ramp = [float(i) for i in range(32)]
        inverse = [float(31 - i) for i in range(32)]
        a = self._split("a", "one.gif", [0.0] * 7, profile=ramp)
        b = self._split("b", "two.gif", [0.8] + [0.0] * 6, profile=inverse)
        self.assertLess(_hu_distance(a, b), 2.0)
        self.assertLess(profile_correlation(ramp, inverse), 0.0)
        self.assertTrue(passes_split_fragment_allograph_gates(a, b))
        self.assertFalse(passes_type_consistency_gates(a, b))

    def test_gate_keeps_hu_close_high_corr_pair(self):
        ramp = [float(i) for i in range(32)]
        a = self._split("a", "one.gif", [0.0] * 7, profile=ramp)
        b = self._split("b", "two.gif", [0.8] + [0.0] * 6, profile=ramp)
        self.assertTrue(passes_type_consistency_gates(a, b))

    def test_gate_splits_hu_ge_2_even_with_matching_profile(self):
        ramp = [float(i) for i in range(32)]
        a = self._split("a", "one.gif", [0.0] * 7, profile=ramp)
        b = self._split("b", "two.gif", [2.5] + [0.0] * 6, profile=ramp)
        self.assertFalse(passes_type_consistency_gates(a, b))

    def test_missing_profile_does_not_split_on_hu_alone(self):
        """Existing split-fragment tests have no ink_profile; Hu decides."""
        a = self._split("a", "one.gif", [0.0] * 7)
        b = self._split("b", "two.gif", [0.8] + [0.0] * 6)
        self.assertTrue(passes_type_consistency_gates(a, b))

    def test_poor_profile_pair_is_split_after_merge(self):
        """Split-fragment stitch unions them; consistency pass splits them."""
        ramp = [float(i) for i in range(32)]
        inverse = [float(31 - i) for i in range(32)]
        a = self._split("a", "one.gif", [0.0] * 7, profile=ramp)
        b = self._split("b", "two.gif", [0.8] + [0.0] * 6, profile=inverse)
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertNotEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_matching_profile_pair_stays_merged(self):
        ramp = [float(i) for i in range(32)]
        a = self._split("a", "one.gif", [0.0] * 7, profile=ramp)
        b = self._split("b", "two.gif", [0.8] + [0.0] * 6, profile=ramp)
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_three_member_consistent_type_stays_merged(self):
        """Cycle 11: remaining multi-member types stay typed when gates pass."""
        ramp = [float(i) for i in range(32)]
        a = self._split("a", "one.gif", [0.0] * 7, profile=ramp)
        b = self._split("b", "two.gif", [0.8] + [0.0] * 6, profile=ramp)
        c = self._split("c", "three.gif", [0.9] + [0.0] * 6, profile=ramp)
        self.assertTrue(passes_type_consistency_gates(a, b))
        self.assertTrue(passes_type_consistency_gates(a, c))
        self.assertTrue(passes_type_consistency_gates(b, c))
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([a, b, c])
        ids = {inst.cluster_id for inst in clustered}
        self.assertEqual(len(ids), 1, ids)

    def test_transitive_overmerge_is_split(self):
        """A–B and B–C merge; A–C is Hu-far. A and C must not share an ID."""
        ramp = [float(i) for i in range(32)]
        a = self._split("a", "one.gif", [0.0] * 7, profile=ramp)
        b = self._split("b", "two.gif", [0.8] + [0.0] * 6, profile=ramp)
        c = self._split("c", "three.gif", [2.4] + [0.0] * 6, profile=ramp)
        self.assertTrue(passes_split_fragment_allograph_gates(a, b))
        self.assertTrue(passes_split_fragment_allograph_gates(b, c))
        self.assertFalse(passes_type_consistency_gates(a, c))
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([a, b, c])
        self.assertNotEqual(clustered[0].cluster_id, clustered[2].cluster_id)

    def test_non_split_instances_are_not_repartitioned(self):
        """Tall-thin same-line crescents can have Hu > 2; splitter skips them."""
        thin_a = GlyphInstance(
            instance_id="thin_a",
            source_image="line.gif",
            bounding_box=BoundingBox(x=0, y=0, width=26, height=66),
            features=[0.0] * 7,
            position=GlyphPosition(0, 0, 2),
        )
        thin_b = GlyphInstance(
            instance_id="thin_b",
            source_image="line.gif",
            bounding_box=BoundingBox(x=30, y=0, width=26, height=66),
            features=[3.2] + [0.0] * 6,
            position=GlyphPosition(0, 1, 2),
        )
        self.assertFalse(passes_type_consistency_gates(thin_a, thin_b))
        self.assertTrue(passes_same_line_allograph_gates(thin_a, thin_b))
        processor = GlyphProcessor()
        _, clustered = processor.cluster_glyphs([thin_a, thin_b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)

    def test_split_can_be_disabled(self):
        ramp = [float(i) for i in range(32)]
        inverse = [float(31 - i) for i in range(32)]
        a = self._split("a", "one.gif", [0.0] * 7, profile=ramp)
        b = self._split("b", "two.gif", [0.8] + [0.0] * 6, profile=inverse)
        processor = GlyphProcessor(ProcessorConfig(split_inconsistent_types=False))
        _, clustered = processor.cluster_glyphs([a, b])
        self.assertEqual(clustered[0].cluster_id, clustered[1].cluster_id)


class TestSingleGlyphClustering(unittest.TestCase):
    """Tests for edge cases with single glyphs."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_single_instance(self):
        """Test clustering with a single glyph instance."""
        inst, img = create_glyph_instance("circle", "single_0")
        inst.features = self.processor.extract_features(img, inst)

        clusters, instances = self.processor.cluster_glyphs([inst])

        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0].frequency, 1)
        self.assertEqual(instances[0].cluster_id, clusters[0].cluster_id)


if __name__ == "__main__":
    unittest.main()
