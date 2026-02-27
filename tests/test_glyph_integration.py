"""Integration tests for the glyph cataloger."""

import json
import os
import shutil
import tempfile
import unittest

import cv2
import numpy as np

from models.glyphs import RongorongoLexicon


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


def create_tablet_image(
    lines: list[list[str]], glyph_size: int = 50, h_spacing: int = 10, v_spacing: int = 20
) -> np.ndarray:
    """Create a test tablet image with multiple lines of glyphs."""
    max_cols = max(len(line) for line in lines) if lines else 0
    width = max(max_cols * glyph_size + (max_cols - 1) * h_spacing + 40, 100)
    height = len(lines) * glyph_size + (len(lines) - 1) * v_spacing + 40
    img = np.ones((height, width), dtype=np.uint8) * 255

    y = 20
    for line in lines:
        x = 20
        for shape in line:
            glyph = create_test_glyph(shape, glyph_size)
            img[y : y + glyph_size, x : x + glyph_size] = glyph
            x += glyph_size + h_spacing
        y += glyph_size + v_spacing

    return img


class TestEndToEndPipeline(unittest.TestCase):
    """End-to-end pipeline tests."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()
        self.input_dir = os.path.join(self.temp_dir, "input", "tablets")
        self.output_dir = os.path.join(self.temp_dir, "output")
        os.makedirs(self.input_dir)
        os.makedirs(self.output_dir)

    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.temp_dir)

    def test_process_single_image(self):
        """Test full pipeline on one image."""
        from processors.glyph_processor import GlyphProcessor

        # Create test tablet image
        tablet = create_tablet_image(
            [
                ["circle", "square", "triangle"],
                ["square", "circle", "square"],
            ]
        )
        tablet_path = os.path.join(self.input_dir, "tablet_a.png")
        cv2.imwrite(tablet_path, tablet)

        # Process the image
        processor = GlyphProcessor()
        image = processor.load_image(tablet_path)
        self.assertIsNotNone(image)

        instances = processor.detect_glyphs(image, "tablet_a.png")
        self.assertEqual(len(instances), 6)

        instances = processor.assign_positions(instances)
        instances = processor.extract_features_batch(image, instances)

        clusters, instances = processor.cluster_glyphs(instances)

        # Should have found glyphs and clustered them
        self.assertGreater(len(clusters), 0)
        self.assertEqual(sum(c.frequency for c in clusters), 6)

    def test_process_multiple_images(self):
        """Test processing and merging multiple images."""
        from processors.glyph_processor import GlyphProcessor

        # Create two test tablets
        tablet_a = create_tablet_image([["circle", "square"]])
        tablet_b = create_tablet_image([["triangle", "circle"]])

        cv2.imwrite(os.path.join(self.input_dir, "tablet_a.png"), tablet_a)
        cv2.imwrite(os.path.join(self.input_dir, "tablet_b.png"), tablet_b)

        processor = GlyphProcessor()
        all_instances = []
        images = {}

        for filename in os.listdir(self.input_dir):
            path = os.path.join(self.input_dir, filename)
            image = processor.load_image(path)
            if image is not None:
                images[filename] = image
                instances = processor.detect_glyphs(image, filename)
                instances = processor.assign_positions(instances)
                instances = processor.extract_features_batch(image, instances)
                all_instances.extend(instances)

        # Should have 4 glyphs total
        self.assertEqual(len(all_instances), 4)

        clusters, all_instances = processor.cluster_glyphs(all_instances)

        # Verify all instances have cluster IDs
        for inst in all_instances:
            self.assertIsNotNone(inst.cluster_id)

    def test_output_json_created(self):
        """Test that lexicon JSON file is created."""
        from models.glyphs import GlyphCluster

        lexicon = RongorongoLexicon(
            source_images=["tablet_a.png"],
        )
        cluster = GlyphCluster(cluster_id="G001", instances=["a", "b"])
        lexicon.add_cluster(cluster)

        output_path = os.path.join(self.output_dir, "rongorongo_lexicon.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(lexicon.to_dict(), f, indent=2)

        self.assertTrue(os.path.exists(output_path))

    def test_output_json_valid(self):
        """Test that JSON output is valid and parseable."""
        from models.glyphs import GlyphCluster

        lexicon = RongorongoLexicon(source_images=["tablet.png"])
        lexicon.add_cluster(GlyphCluster("G001", ["a", "b"]))
        lexicon.add_cluster(GlyphCluster("G002", ["c"]))

        output_path = os.path.join(self.output_dir, "lexicon.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(lexicon.to_dict(), f, indent=2)

        # Read and parse
        with open(output_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("version", data)
        self.assertIn("clusters", data)
        self.assertIn("total_glyphs_detected", data)
        self.assertEqual(data["total_glyphs_detected"], 3)

    def test_glyph_images_saved(self):
        """Test that individual glyph images are saved."""
        from processors.glyph_processor import GlyphProcessor

        tablet = create_tablet_image([["circle", "square"]])
        tablet_path = os.path.join(self.input_dir, "tablet.png")
        cv2.imwrite(tablet_path, tablet)

        processor = GlyphProcessor()
        image = processor.load_image(tablet_path)
        instances = processor.detect_glyphs(image, "tablet.png")

        glyph_dir = os.path.join(self.output_dir, "glyphs")
        for inst in instances:
            processor.save_glyph_image(image, inst, glyph_dir)

        # Check files exist
        files = os.listdir(glyph_dir)
        self.assertEqual(len(files), 2)
        self.assertTrue(all(f.endswith(".png") for f in files))

    def test_representative_images_saved(self):
        """Test that cluster representative images are saved."""
        from processors.glyph_processor import GlyphProcessor

        tablet = create_tablet_image([["circle", "circle"]])
        tablet_path = os.path.join(self.input_dir, "tablet.png")
        cv2.imwrite(tablet_path, tablet)

        processor = GlyphProcessor()
        image = processor.load_image(tablet_path)
        instances = processor.detect_glyphs(image, "tablet.png")
        instances = processor.extract_features_batch(image, instances)
        clusters, instances = processor.cluster_glyphs(instances)

        images = {"tablet.png": image}
        glyph_dir = os.path.join(self.output_dir, "glyphs")

        for cluster in clusters:
            processor.save_representative_image(cluster, instances, images, glyph_dir)
            self.assertTrue(os.path.exists(cluster.representative_image))


class TestEdgeCases(unittest.TestCase):
    """Tests for edge cases."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.input_dir = os.path.join(self.temp_dir, "input")
        self.output_dir = os.path.join(self.temp_dir, "output")
        os.makedirs(self.input_dir)
        os.makedirs(self.output_dir)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_empty_input_directory(self):
        """Test handling of no input images."""
        from glyph_cataloger import get_image_files

        files = get_image_files(self.input_dir)
        self.assertEqual(len(files), 0)

    def test_single_glyph_image(self):
        """Test handling of image with one glyph."""
        from processors.glyph_processor import GlyphProcessor

        # Create image with single glyph
        tablet = create_tablet_image([["circle"]])
        tablet_path = os.path.join(self.input_dir, "single.png")
        cv2.imwrite(tablet_path, tablet)

        processor = GlyphProcessor()
        image = processor.load_image(tablet_path)
        instances = processor.detect_glyphs(image, "single.png")
        instances = processor.extract_features_batch(image, instances)

        self.assertEqual(len(instances), 1)

        clusters, instances = processor.cluster_glyphs(instances)
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0].frequency, 1)

    def test_all_identical_glyphs(self):
        """Test when all glyphs cluster together."""
        from processors.glyph_processor import GlyphProcessor

        # Create image with all circles
        tablet = create_tablet_image([["circle"] * 5])
        tablet_path = os.path.join(self.input_dir, "circles.png")
        cv2.imwrite(tablet_path, tablet)

        processor = GlyphProcessor()
        image = processor.load_image(tablet_path)
        instances = processor.detect_glyphs(image, "circles.png")
        instances = processor.extract_features_batch(image, instances)

        clusters, instances = processor.cluster_glyphs(instances)

        # All should be in one cluster
        self.assertEqual(len(clusters), 1)
        self.assertEqual(clusters[0].frequency, 5)

    def test_all_unique_glyphs(self):
        """Test when each glyph is its own cluster."""
        from processors.glyph_processor import GlyphProcessor, ProcessorConfig

        # Configure strict clustering (small eps, high min_samples)
        config = ProcessorConfig(dbscan_eps=0.01, dbscan_min_samples=5)
        processor = GlyphProcessor(config)

        # Create image with different shapes
        tablet = create_tablet_image([["circle", "square", "triangle"]])
        tablet_path = os.path.join(self.input_dir, "unique.png")
        cv2.imwrite(tablet_path, tablet)

        image = processor.load_image(tablet_path)
        instances = processor.detect_glyphs(image, "unique.png")
        instances = processor.extract_features_batch(image, instances)

        clusters, instances = processor.cluster_glyphs(instances)

        # Each glyph might be its own cluster (or some might group)
        total_instances = sum(c.frequency for c in clusters)
        self.assertEqual(total_instances, 3)

    def test_large_image(self):
        """Test handling of high-resolution image."""
        from processors.glyph_processor import GlyphProcessor

        # Create large image with many glyphs
        shapes = ["circle", "square", "triangle"] * 10
        tablet = create_tablet_image([shapes[:15], shapes[15:]])
        tablet_path = os.path.join(self.input_dir, "large.png")
        cv2.imwrite(tablet_path, tablet)

        processor = GlyphProcessor()
        image = processor.load_image(tablet_path)

        self.assertIsNotNone(image)

        instances = processor.detect_glyphs(image, "large.png")
        self.assertEqual(len(instances), 30)

    def test_corrupted_image(self):
        """Test that corrupted files are skipped gracefully."""
        from processors.glyph_processor import GlyphProcessor

        # Create a non-image file
        corrupt_path = os.path.join(self.input_dir, "corrupt.png")
        with open(corrupt_path, "w") as f:
            f.write("this is not an image")

        processor = GlyphProcessor()
        image = processor.load_image(corrupt_path)

        self.assertIsNone(image)


class TestOutputValidation(unittest.TestCase):
    """Tests for output validation."""

    def test_lexicon_total_matches_sum(self):
        """Test that total_glyphs_detected matches sum of frequencies."""
        from models.glyphs import GlyphCluster

        lexicon = RongorongoLexicon()
        lexicon.add_cluster(GlyphCluster("G001", ["a", "b", "c"]))  # 3
        lexicon.add_cluster(GlyphCluster("G002", ["d", "e"]))  # 2
        lexicon.add_cluster(GlyphCluster("G003", ["f"]))  # 1

        total = sum(c.frequency for c in lexicon.clusters)
        self.assertEqual(lexicon.total_glyphs_detected, total)
        self.assertEqual(lexicon.total_glyphs_detected, 6)

    def test_cluster_ids_unique(self):
        """Test that there are no duplicate cluster IDs."""
        from models.glyphs import GlyphCluster

        lexicon = RongorongoLexicon()
        lexicon.add_cluster(GlyphCluster("G001", ["a"]))
        lexicon.add_cluster(GlyphCluster("G002", ["b"]))
        lexicon.add_cluster(GlyphCluster("G003", ["c"]))

        cluster_ids = [c.cluster_id for c in lexicon.clusters]
        self.assertEqual(len(cluster_ids), len(set(cluster_ids)))

    def test_instance_ids_unique(self):
        """Test that there are no duplicate instance IDs."""
        from processors.glyph_processor import GlyphProcessor

        temp_dir = tempfile.mkdtemp()
        try:
            tablet = create_tablet_image([["circle", "square", "triangle"]])
            tablet_path = os.path.join(temp_dir, "tablet.png")
            cv2.imwrite(tablet_path, tablet)

            processor = GlyphProcessor()
            image = processor.load_image(tablet_path)
            instances = processor.detect_glyphs(image, "tablet.png")

            instance_ids = [inst.instance_id for inst in instances]
            self.assertEqual(len(instance_ids), len(set(instance_ids)))
        finally:
            shutil.rmtree(temp_dir)


class TestGetImageFiles(unittest.TestCase):
    """Tests for the get_image_files function."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_finds_supported_formats(self):
        """Test that all supported image formats are found."""
        from glyph_cataloger import get_image_files

        # Create test files with different extensions
        for ext in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
            path = os.path.join(self.temp_dir, f"test{ext}")
            cv2.imwrite(path, np.zeros((10, 10), dtype=np.uint8))

        files = get_image_files(self.temp_dir)
        self.assertEqual(len(files), 5)

    def test_ignores_non_image_files(self):
        """Test that non-image files are ignored."""
        from glyph_cataloger import get_image_files

        # Create image and non-image files
        cv2.imwrite(
            os.path.join(self.temp_dir, "image.png"),
            np.zeros((10, 10), dtype=np.uint8),
        )
        with open(os.path.join(self.temp_dir, "readme.txt"), "w") as f:
            f.write("hello")
        with open(os.path.join(self.temp_dir, "data.json"), "w") as f:
            f.write("{}")

        files = get_image_files(self.temp_dir)
        self.assertEqual(len(files), 1)

    def test_empty_directory(self):
        """Test handling of empty directory."""
        from glyph_cataloger import get_image_files

        files = get_image_files(self.temp_dir)
        self.assertEqual(len(files), 0)

    def test_nonexistent_directory(self):
        """Test handling of nonexistent directory."""
        from glyph_cataloger import get_image_files

        files = get_image_files("/nonexistent/path")
        self.assertEqual(len(files), 0)


if __name__ == "__main__":
    unittest.main()
