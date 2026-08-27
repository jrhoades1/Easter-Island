"""Unit tests for glyph data models."""

import json
import unittest
from datetime import datetime

from models.glyphs import (
    BoundingBox,
    GlyphCluster,
    GlyphInstance,
    GlyphPosition,
    PositionStats,
    RongorongoLexicon,
)


class TestBoundingBox(unittest.TestCase):
    """Tests for BoundingBox dataclass."""

    def test_creation(self):
        """Test creating a bounding box with x, y, width, height."""
        bbox = BoundingBox(x=10, y=20, width=30, height=40)
        self.assertEqual(bbox.x, 10)
        self.assertEqual(bbox.y, 20)
        self.assertEqual(bbox.width, 30)
        self.assertEqual(bbox.height, 40)

    def test_area(self):
        """Test area calculation."""
        bbox = BoundingBox(x=0, y=0, width=10, height=20)
        self.assertEqual(bbox.area, 200)

    def test_area_zero(self):
        """Test area with zero dimensions."""
        bbox = BoundingBox(x=5, y=5, width=0, height=10)
        self.assertEqual(bbox.area, 0)

    def test_center(self):
        """Test center point calculation."""
        bbox = BoundingBox(x=10, y=20, width=30, height=40)
        self.assertEqual(bbox.center, (25, 40))

    def test_center_odd_dimensions(self):
        """Test center with odd dimensions (integer division)."""
        bbox = BoundingBox(x=0, y=0, width=11, height=11)
        self.assertEqual(bbox.center, (5, 5))

    def test_to_dict(self):
        """Test serialization to dictionary."""
        bbox = BoundingBox(x=10, y=20, width=30, height=40)
        d = bbox.to_dict()
        self.assertEqual(d, {"x": 10, "y": 20, "width": 30, "height": 40})

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {"x": 10, "y": 20, "width": 30, "height": 40}
        bbox = BoundingBox.from_dict(d)
        self.assertEqual(bbox.x, 10)
        self.assertEqual(bbox.y, 20)
        self.assertEqual(bbox.width, 30)
        self.assertEqual(bbox.height, 40)

    def test_overlaps_true(self):
        """Test overlap detection when boxes overlap."""
        bbox1 = BoundingBox(x=0, y=0, width=20, height=20)
        bbox2 = BoundingBox(x=10, y=10, width=20, height=20)
        self.assertTrue(bbox1.overlaps(bbox2))
        self.assertTrue(bbox2.overlaps(bbox1))

    def test_overlaps_false_horizontal(self):
        """Test no overlap when boxes are horizontally separated."""
        bbox1 = BoundingBox(x=0, y=0, width=10, height=10)
        bbox2 = BoundingBox(x=20, y=0, width=10, height=10)
        self.assertFalse(bbox1.overlaps(bbox2))

    def test_overlaps_false_vertical(self):
        """Test no overlap when boxes are vertically separated."""
        bbox1 = BoundingBox(x=0, y=0, width=10, height=10)
        bbox2 = BoundingBox(x=0, y=20, width=10, height=10)
        self.assertFalse(bbox1.overlaps(bbox2))

    def test_overlaps_touching_edge(self):
        """Test no overlap when boxes touch at edge."""
        bbox1 = BoundingBox(x=0, y=0, width=10, height=10)
        bbox2 = BoundingBox(x=10, y=0, width=10, height=10)
        self.assertFalse(bbox1.overlaps(bbox2))


class TestGlyphPosition(unittest.TestCase):
    """Tests for GlyphPosition dataclass."""

    def test_creation(self):
        """Test creating a glyph position."""
        pos = GlyphPosition(line_number=1, position_in_line=5, total_in_line=10)
        self.assertEqual(pos.line_number, 1)
        self.assertEqual(pos.position_in_line, 5)
        self.assertEqual(pos.total_in_line, 10)

    def test_creation_defaults(self):
        """Test default value for total_in_line."""
        pos = GlyphPosition(line_number=0, position_in_line=0)
        self.assertEqual(pos.total_in_line, 0)

    def test_to_dict(self):
        """Test serialization to dictionary."""
        pos = GlyphPosition(line_number=1, position_in_line=5, total_in_line=10)
        d = pos.to_dict()
        self.assertEqual(d, {"line_number": 1, "position_in_line": 5, "total_in_line": 10})

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {"line_number": 2, "position_in_line": 3, "total_in_line": 8}
        pos = GlyphPosition.from_dict(d)
        self.assertEqual(pos.line_number, 2)
        self.assertEqual(pos.position_in_line, 3)
        self.assertEqual(pos.total_in_line, 8)

    def test_comparison_different_lines(self):
        """Test comparison - different lines."""
        pos1 = GlyphPosition(line_number=1, position_in_line=5)
        pos2 = GlyphPosition(line_number=2, position_in_line=0)
        self.assertTrue(pos1 < pos2)
        self.assertFalse(pos2 < pos1)

    def test_comparison_same_line(self):
        """Test comparison - same line, different positions."""
        pos1 = GlyphPosition(line_number=1, position_in_line=3)
        pos2 = GlyphPosition(line_number=1, position_in_line=5)
        self.assertTrue(pos1 < pos2)
        self.assertFalse(pos2 < pos1)

    def test_comparison_equal(self):
        """Test comparison - equal positions."""
        pos1 = GlyphPosition(line_number=1, position_in_line=3)
        pos2 = GlyphPosition(line_number=1, position_in_line=3)
        self.assertFalse(pos1 < pos2)
        self.assertFalse(pos2 < pos1)


class TestGlyphInstance(unittest.TestCase):
    """Tests for GlyphInstance dataclass."""

    def test_creation(self):
        """Test creating a glyph instance with required fields."""
        bbox = BoundingBox(x=10, y=20, width=30, height=40)
        instance = GlyphInstance(
            instance_id="tablet_0001",
            source_image="tablet.png",
            bounding_box=bbox,
        )
        self.assertEqual(instance.instance_id, "tablet_0001")
        self.assertEqual(instance.source_image, "tablet.png")
        self.assertEqual(instance.bounding_box, bbox)

    def test_defaults(self):
        """Test default values for optional fields."""
        bbox = BoundingBox(x=0, y=0, width=10, height=10)
        instance = GlyphInstance(
            instance_id="test_0001",
            source_image="test.png",
            bounding_box=bbox,
        )
        self.assertEqual(instance.features, [])
        self.assertEqual(instance.ink_profile, [])
        self.assertIsNone(instance.cluster_id)
        self.assertIsNone(instance.position)
        self.assertEqual(instance.confidence, 1.0)
        self.assertIsNone(instance.image_path)

    def test_to_dict(self):
        """Test full serialization to dictionary."""
        bbox = BoundingBox(x=10, y=20, width=30, height=40)
        pos = GlyphPosition(line_number=1, position_in_line=2, total_in_line=5)
        instance = GlyphInstance(
            instance_id="tablet_0001",
            source_image="tablet.png",
            bounding_box=bbox,
            cluster_id="G001",
            position=pos,
            confidence=0.95,
            image_path="output/glyphs/tablet_0001.png",
        )
        d = instance.to_dict()
        self.assertEqual(d["instance_id"], "tablet_0001")
        self.assertEqual(d["source_image"], "tablet.png")
        self.assertEqual(d["cluster_id"], "G001")
        self.assertEqual(d["confidence"], 0.95)
        self.assertEqual(d["image_path"], "output/glyphs/tablet_0001.png")
        self.assertIn("bounding_box", d)
        self.assertIn("position", d)

    def test_to_dict_excludes_features(self):
        """Test that features are excluded from serialization."""
        bbox = BoundingBox(x=0, y=0, width=10, height=10)
        instance = GlyphInstance(
            instance_id="test_0001",
            source_image="test.png",
            bounding_box=bbox,
            features=[1.0, 2.0, 3.0],
        )
        d = instance.to_dict()
        self.assertNotIn("features", d)

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {
            "instance_id": "tablet_0001",
            "source_image": "tablet.png",
            "bounding_box": {"x": 10, "y": 20, "width": 30, "height": 40},
            "cluster_id": "G001",
            "position": {"line_number": 1, "position_in_line": 2, "total_in_line": 5},
            "confidence": 0.95,
        }
        instance = GlyphInstance.from_dict(d)
        self.assertEqual(instance.instance_id, "tablet_0001")
        self.assertEqual(instance.cluster_id, "G001")
        self.assertEqual(instance.bounding_box.x, 10)
        self.assertEqual(instance.position.line_number, 1)

    def test_generate_id(self):
        """Test instance ID generation."""
        id1 = GlyphInstance.generate_id("tablet_a.png", 0)
        self.assertEqual(id1, "tablet_a_0000")

        id2 = GlyphInstance.generate_id("path/to/image.jpg", 42)
        self.assertEqual(id2, "image_0042")


class TestGlyphCluster(unittest.TestCase):
    """Tests for GlyphCluster dataclass."""

    def test_creation(self):
        """Test creating a cluster with cluster_id and instances."""
        cluster = GlyphCluster(
            cluster_id="G001",
            instances=["inst_0001", "inst_0002", "inst_0003"],
        )
        self.assertEqual(cluster.cluster_id, "G001")
        self.assertEqual(len(cluster.instances), 3)

    def test_frequency(self):
        """Test that frequency matches instance count."""
        cluster = GlyphCluster(
            cluster_id="G001",
            instances=["inst_0001", "inst_0002"],
        )
        self.assertEqual(cluster.frequency, 2)

    def test_frequency_empty(self):
        """Test frequency with no instances."""
        cluster = GlyphCluster(cluster_id="G001")
        self.assertEqual(cluster.frequency, 0)

    def test_add_instance(self):
        """Test adding an instance updates frequency."""
        cluster = GlyphCluster(cluster_id="G001")
        self.assertEqual(cluster.frequency, 0)

        cluster.add_instance("inst_0001")
        self.assertEqual(cluster.frequency, 1)

        cluster.add_instance("inst_0002")
        self.assertEqual(cluster.frequency, 2)

    def test_add_instance_no_duplicates(self):
        """Test that adding duplicate instance doesn't increase frequency."""
        cluster = GlyphCluster(cluster_id="G001")
        cluster.add_instance("inst_0001")
        cluster.add_instance("inst_0001")
        self.assertEqual(cluster.frequency, 1)

    def test_to_dict(self):
        """Test serialization with all statistics."""
        cluster = GlyphCluster(
            cluster_id="G001",
            instances=["inst_0001", "inst_0002"],
            representative_image="output/glyphs/G001_representative.png",
            positions=PositionStats(
                line_distribution={1: 2, 2: 1},
                avg_position_in_line=0.35,
                common_neighbors=["G002", "G003"],
            ),
        )
        d = cluster.to_dict()
        self.assertEqual(d["cluster_id"], "G001")
        self.assertEqual(d["frequency"], 2)
        self.assertEqual(d["representative_image"], "output/glyphs/G001_representative.png")
        self.assertIn("positions", d)

    def test_from_dict(self):
        """Test deserialization from dictionary."""
        d = {
            "cluster_id": "G005",
            "instances": ["a", "b", "c"],
            "representative_image": "img.png",
            "positions": {"line_distribution": {"1": 2}, "avg_position_in_line": 0.5},
        }
        cluster = GlyphCluster.from_dict(d)
        self.assertEqual(cluster.cluster_id, "G005")
        self.assertEqual(cluster.frequency, 3)
        self.assertEqual(cluster.representative_image, "img.png")

    def test_generate_id(self):
        """Test cluster ID generation in format G001, G002, etc."""
        self.assertEqual(GlyphCluster.generate_id(1), "G001")
        self.assertEqual(GlyphCluster.generate_id(42), "G042")
        self.assertEqual(GlyphCluster.generate_id(100), "G100")


class TestRongorongoLexicon(unittest.TestCase):
    """Tests for RongorongoLexicon dataclass."""

    def test_creation_empty(self):
        """Test creating an empty lexicon."""
        lexicon = RongorongoLexicon()
        self.assertEqual(lexicon.version, "1.0.0")
        self.assertEqual(lexicon.total_glyphs_detected, 0)
        self.assertEqual(lexicon.unique_glyph_types, 0)
        self.assertEqual(lexicon.source_images, [])
        self.assertEqual(lexicon.clusters, [])

    def test_add_cluster(self):
        """Test adding clusters and updating statistics."""
        lexicon = RongorongoLexicon()

        cluster1 = GlyphCluster(cluster_id="G001", instances=["a", "b", "c"])
        cluster2 = GlyphCluster(cluster_id="G002", instances=["d", "e"])

        lexicon.add_cluster(cluster1)
        self.assertEqual(lexicon.unique_glyph_types, 1)
        self.assertEqual(lexicon.total_glyphs_detected, 3)

        lexicon.add_cluster(cluster2)
        self.assertEqual(lexicon.unique_glyph_types, 2)
        self.assertEqual(lexicon.total_glyphs_detected, 5)

    def test_get_cluster(self):
        """Test getting a cluster by ID."""
        lexicon = RongorongoLexicon()
        cluster = GlyphCluster(cluster_id="G001", instances=["a"])
        lexicon.add_cluster(cluster)

        found = lexicon.get_cluster("G001")
        self.assertEqual(found, cluster)

        not_found = lexicon.get_cluster("G999")
        self.assertIsNone(not_found)

    def test_to_json(self):
        """Test full JSON serialization."""
        lexicon = RongorongoLexicon(
            version="1.0.0",
            created_at=datetime(2026, 1, 20, 10, 30, 0),
            source_images=["tablet_a.png", "tablet_b.png"],
        )
        cluster = GlyphCluster(cluster_id="G001", instances=["a", "b"])
        lexicon.add_cluster(cluster)

        d = lexicon.to_dict()
        json_str = json.dumps(d)

        self.assertIn("version", json_str)
        self.assertIn("created_at", json_str)
        self.assertIn("total_glyphs_detected", json_str)
        self.assertIn("unique_glyph_types", json_str)
        self.assertIn("clusters", json_str)

    def test_from_json(self):
        """Test loading from JSON."""
        d = {
            "version": "1.0.0",
            "created_at": "2026-01-20T10:30:00",
            "source_images": ["tablet.png"],
            "clusters": [
                {"cluster_id": "G001", "instances": ["a", "b"], "positions": {}},
            ],
            "statistics": {"hapax_legomena": 0},
        }
        lexicon = RongorongoLexicon.from_dict(d)
        self.assertEqual(lexicon.version, "1.0.0")
        self.assertEqual(len(lexicon.clusters), 1)
        self.assertEqual(lexicon.clusters[0].cluster_id, "G001")

    def test_compute_statistics(self):
        """Test computing lexicon statistics."""
        lexicon = RongorongoLexicon()

        # Add some clusters with different frequencies
        cluster1 = GlyphCluster(cluster_id="G001", instances=["a", "b", "c"])  # 3
        cluster2 = GlyphCluster(cluster_id="G002", instances=["d"])  # 1 (hapax)
        cluster3 = GlyphCluster(cluster_id="G003", instances=["e", "f"])  # 2

        lexicon.add_cluster(cluster1)
        lexicon.add_cluster(cluster2)
        lexicon.add_cluster(cluster3)

        # Create mock instances with positions
        bbox = BoundingBox(x=0, y=0, width=10, height=10)
        instances = [
            GlyphInstance("a", "tablet.png", bbox, position=GlyphPosition(0, 0, 3)),
            GlyphInstance("b", "tablet.png", bbox, position=GlyphPosition(0, 1, 3)),
            GlyphInstance("c", "tablet.png", bbox, position=GlyphPosition(0, 2, 3)),
            GlyphInstance("d", "tablet.png", bbox, position=GlyphPosition(1, 0, 2)),
            GlyphInstance("e", "tablet.png", bbox, position=GlyphPosition(1, 1, 2)),
            GlyphInstance("f", "tablet.png", bbox, position=GlyphPosition(2, 0, 1)),
        ]

        lexicon.compute_statistics(instances)

        self.assertEqual(lexicon.statistics.hapax_legomena, 1)
        self.assertIn("G001", lexicon.statistics.most_frequent_glyphs)


if __name__ == "__main__":
    unittest.main()
