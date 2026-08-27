"""Unit tests for the glyph processor."""

import os
import tempfile
import unittest

import cv2
import numpy as np

from models.glyphs import BoundingBox, GlyphInstance
from processors.glyph_processor import (
    GlyphProcessor,
    ProcessorConfig,
    vertical_valley_cuts,
)


def create_test_glyph(shape: str, size: int = 50) -> np.ndarray:
    """Generate a simple shape as a test glyph.

    Args:
        shape: One of 'circle', 'square', 'triangle'.
        size: Size of the output image.

    Returns:
        Grayscale image with the shape.
    """
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


def create_glyph_row(shapes: list[str], glyph_size: int = 50, spacing: int = 10) -> np.ndarray:
    """Create an image with a row of glyphs.

    Args:
        shapes: List of shape names.
        glyph_size: Size of each glyph.
        spacing: Spacing between glyphs.

    Returns:
        Image containing the row of glyphs.
    """
    width = len(shapes) * glyph_size + (len(shapes) - 1) * spacing + 20
    height = glyph_size + 20
    img = np.ones((height, width), dtype=np.uint8) * 255

    x = 10
    for shape in shapes:
        glyph = create_test_glyph(shape, glyph_size)
        img[10 : 10 + glyph_size, x : x + glyph_size] = glyph
        x += glyph_size + spacing

    return img


def create_multiline_image(
    lines: list[list[str]], glyph_size: int = 50, h_spacing: int = 10, v_spacing: int = 20
) -> np.ndarray:
    """Create an image with multiple lines of glyphs.

    Args:
        lines: List of lines, each line is a list of shape names.
        glyph_size: Size of each glyph.
        h_spacing: Horizontal spacing between glyphs.
        v_spacing: Vertical spacing between lines.

    Returns:
        Image containing multiple lines of glyphs.
    """
    max_cols = max(len(line) for line in lines)
    width = max_cols * glyph_size + (max_cols - 1) * h_spacing + 20
    height = len(lines) * glyph_size + (len(lines) - 1) * v_spacing + 20
    img = np.ones((height, width), dtype=np.uint8) * 255

    y = 10
    for line in lines:
        x = 10
        for shape in line:
            glyph = create_test_glyph(shape, glyph_size)
            img[y : y + glyph_size, x : x + glyph_size] = glyph
            x += glyph_size + h_spacing
        y += glyph_size + v_spacing

    return img


class TestImageLoading(unittest.TestCase):
    """Tests for image loading functionality."""

    def setUp(self):
        self.processor = GlyphProcessor()
        self.temp_dir = tempfile.mkdtemp()

    def test_load_image(self):
        """Test loading an image from file path."""
        # Create a test image
        img = create_test_glyph("circle", 50)
        path = os.path.join(self.temp_dir, "test.png")
        cv2.imwrite(path, img)

        loaded = self.processor.load_image(path)
        self.assertIsNotNone(loaded)
        self.assertEqual(loaded.shape[:2], (50, 50))

    def test_load_image_not_found(self):
        """Test handling of missing file."""
        result = self.processor.load_image("/nonexistent/path/image.png")
        self.assertIsNone(result)

    def test_load_image_invalid(self):
        """Test handling of invalid/corrupted file."""
        # Create a non-image file
        path = os.path.join(self.temp_dir, "notanimage.png")
        with open(path, "w") as f:
            f.write("this is not an image")

        result = self.processor.load_image(path)
        self.assertIsNone(result)


class TestPreprocessing(unittest.TestCase):
    """Tests for image preprocessing."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_convert_grayscale_color(self):
        """Test converting color image to grayscale."""
        color_img = np.zeros((50, 50, 3), dtype=np.uint8)
        color_img[:, :, 2] = 255  # Red channel

        gray = self.processor.convert_grayscale(color_img)
        self.assertEqual(len(gray.shape), 2)
        self.assertEqual(gray.shape, (50, 50))

    def test_convert_grayscale_already_gray(self):
        """Test handling of already grayscale image."""
        gray_img = np.zeros((50, 50), dtype=np.uint8)
        result = self.processor.convert_grayscale(gray_img)
        self.assertEqual(result.shape, (50, 50))

    def test_adaptive_threshold(self):
        """Test adaptive thresholding."""
        gray_img = create_test_glyph("circle", 50)
        binary = self.processor.apply_threshold(gray_img)

        self.assertEqual(binary.shape, gray_img.shape)
        # Should be binary (only 0 and 255)
        unique = np.unique(binary)
        self.assertTrue(all(v in [0, 255] for v in unique))

    def test_denoise(self):
        """Test noise removal with Gaussian blur."""
        noisy = np.random.randint(0, 255, (50, 50), dtype=np.uint8)
        denoised = self.processor.denoise(noisy)

        self.assertEqual(denoised.shape, noisy.shape)
        # Denoised should be smoother (lower variance in local regions)

    def test_preprocess_pipeline(self):
        """Test the full preprocessing chain."""
        # Create a color image with a glyph
        color_img = np.ones((60, 60, 3), dtype=np.uint8) * 255
        cv2.circle(color_img, (30, 30), 15, (0, 0, 0), -1)

        binary = self.processor.preprocess(color_img)

        self.assertEqual(len(binary.shape), 2)  # Should be grayscale
        unique = np.unique(binary)
        self.assertTrue(all(v in [0, 255] for v in unique))  # Should be binary


class TestGlyphDetection(unittest.TestCase):
    """Tests for glyph detection."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_detect_single_glyph(self):
        """Test detecting one glyph in an image."""
        img = create_test_glyph("circle", 50)
        # Add white border
        padded = np.ones((70, 70), dtype=np.uint8) * 255
        padded[10:60, 10:60] = img

        instances = self.processor.detect_glyphs(padded, "test.png")
        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].source_image, "test.png")

    def test_detect_multiple_glyphs(self):
        """Test detecting a row of glyphs."""
        img = create_glyph_row(["circle", "square", "triangle", "circle", "square"])
        instances = self.processor.detect_glyphs(img, "row.png")
        self.assertEqual(len(instances), 5)

    def test_detect_no_glyphs(self):
        """Test empty image returns empty list."""
        blank = np.ones((100, 100), dtype=np.uint8) * 255
        instances = self.processor.detect_glyphs(blank, "blank.png")
        self.assertEqual(len(instances), 0)

    def test_detect_filters_small_contours(self):
        """Test that small noise is filtered out."""
        img = np.ones((100, 100), dtype=np.uint8) * 255
        # Add a valid glyph
        cv2.circle(img, (50, 50), 20, 0, -1)
        # Add tiny noise dots
        cv2.circle(img, (10, 10), 2, 0, -1)
        cv2.circle(img, (90, 90), 2, 0, -1)

        instances = self.processor.detect_glyphs(img, "test.png")
        # Should only detect the large circle
        self.assertEqual(len(instances), 1)

    def test_detect_filters_large_contours(self):
        """Test that oversized regions are filtered out."""
        config = ProcessorConfig(max_contour_area=1000)
        processor = GlyphProcessor(config)

        img = np.ones((200, 200), dtype=np.uint8) * 255
        # Add a huge rectangle (too big)
        cv2.rectangle(img, (20, 20), (180, 180), 0, -1)
        # Add a small circle (valid)
        cv2.circle(img, (100, 100), 10, 255, -1)  # White circle inside

        instances = processor.detect_glyphs(img, "test.png")
        # The large contour should be filtered
        self.assertLessEqual(len(instances), 1)

    def test_bounding_box_extraction(self):
        """Test that bounding boxes are correct."""
        img = np.ones((100, 100), dtype=np.uint8) * 255
        cv2.rectangle(img, (20, 30), (50, 70), 0, -1)

        instances = self.processor.detect_glyphs(img, "test.png")
        self.assertEqual(len(instances), 1)

        bbox = instances[0].bounding_box
        # Check approximate bounds (with padding)
        self.assertLessEqual(bbox.x, 20)
        self.assertLessEqual(bbox.y, 30)
        self.assertGreaterEqual(bbox.x + bbox.width, 50)
        self.assertGreaterEqual(bbox.y + bbox.height, 70)

    def test_bounding_box_padding(self):
        """Test that bounding box padding is applied."""
        config = ProcessorConfig(bbox_padding=10)
        processor = GlyphProcessor(config)

        img = np.ones((100, 100), dtype=np.uint8) * 255
        cv2.rectangle(img, (30, 30), (50, 50), 0, -1)

        instances = processor.detect_glyphs(img, "test.png")
        self.assertEqual(len(instances), 1)

        bbox = instances[0].bounding_box
        # With 10px padding, box should extend beyond the shape
        self.assertLessEqual(bbox.x, 25)  # 30 - 5 (default would be)
        self.assertLessEqual(bbox.y, 25)


def _bridged_lobes(
    widths: list[int],
    height: int = 50,
    gap: int = 16,
    bridge_h: int = 4,
    pad: int = 10,
) -> np.ndarray:
    """One connected contour: filled rectangles joined by a thin bridge."""
    total_w = sum(widths) + gap * (len(widths) - 1) + 2 * pad
    img = np.ones((height + 2 * pad, total_w), dtype=np.uint8) * 255
    x = pad
    center_y = pad + height // 2
    for i, width in enumerate(widths):
        cv2.rectangle(img, (x, pad), (x + width - 1, pad + height - 1), 0, -1)
        if i < len(widths) - 1:
            by0 = center_y - bridge_h // 2
            cv2.rectangle(
                img, (x + width, by0), (x + width + gap, by0 + bridge_h), 0, -1
            )
        x += width + gap
    return img


class TestVerticalValleyCuts(unittest.TestCase):
    """Pure projection helper. No Mamari GIFs."""

    def test_single_deep_valley(self):
        col = np.array([20] * 20 + [3] * 5 + [20] * 20, dtype=float)
        cuts = vertical_valley_cuts(col, valley_ratio=0.40, min_part_width=12, max_parts=3)
        self.assertEqual(len(cuts), 1)
        self.assertGreater(cuts[0], 18)
        self.assertLess(cuts[0], 27)

    def test_two_valleys_for_three_parts(self):
        col = np.array(
            [20] * 18 + [2] * 4 + [20] * 18 + [2] * 4 + [20] * 18, dtype=float
        )
        cuts = vertical_valley_cuts(col, valley_ratio=0.40, min_part_width=12, max_parts=3)
        self.assertEqual(len(cuts), 2)

    def test_no_valley_on_flat_profile(self):
        col = np.ones(50, dtype=float) * 20
        self.assertEqual(vertical_valley_cuts(col), [])


class TestWideLigatureSplit(unittest.TestCase):
    """Valley split on a clean binary (255=ink). Preprocess is not the unit."""

    def _ink_lobes(self, widths: list[int], height: int = 50, gap: int = 16) -> tuple:
        pad = 5
        total_w = sum(widths) + gap * (len(widths) - 1) + 2 * pad
        binary = np.zeros((height + 2 * pad, total_w), dtype=np.uint8)
        x = pad
        cy = pad + height // 2
        for i, width in enumerate(widths):
            cv2.rectangle(binary, (x, pad), (x + width - 1, pad + height - 1), 255, -1)
            if i < len(widths) - 1:
                cv2.rectangle(binary, (x + width, cy - 1), (x + width + gap, cy + 1), 255, -1)
            x += width + gap
        bbox = BoundingBox(x=0, y=0, width=binary.shape[1], height=binary.shape[0])
        return binary, bbox

    def test_bridged_pair_splits_into_two(self):
        binary, bbox = self._ink_lobes([32, 32])
        parts = GlyphProcessor().split_wide_ligature(binary, bbox)
        self.assertEqual(len(parts), 2)

    def test_three_lobes_split_into_three(self):
        binary, bbox = self._ink_lobes([32, 32, 32])
        parts = GlyphProcessor().split_wide_ligature(binary, bbox)
        self.assertEqual(len(parts), 3)

    def test_split_can_be_disabled(self):
        img = _bridged_lobes([32, 32])
        processor = GlyphProcessor(ProcessorConfig(split_wide_ligatures=False))
        instances = processor.detect_glyphs(img, "pair.png")
        self.assertEqual(len(instances), 1)

    def test_unsplit_detect_is_not_marked(self):
        img = np.ones((70, 100), dtype=np.uint8) * 255
        cv2.rectangle(img, (10, 10), (90, 60), 0, -1)
        instances = GlyphProcessor().detect_glyphs(img, "solid.png")
        self.assertEqual(len(instances), 1)
        self.assertFalse(instances[0].from_ligature_split)

    def test_solid_wide_box_does_not_split(self):
        img = np.ones((70, 100), dtype=np.uint8) * 255
        cv2.rectangle(img, (10, 10), (90, 60), 0, -1)
        instances = GlyphProcessor().detect_glyphs(img, "solid.png")
        self.assertEqual(len(instances), 1)

    def test_tall_thin_stem_does_not_split(self):
        img = np.ones((80, 40), dtype=np.uint8) * 255
        cv2.rectangle(img, (8, 6), (28, 72), 0, -1)
        instances = GlyphProcessor().detect_glyphs(img, "stem.png")
        self.assertEqual(len(instances), 1)


class TestLineDetection(unittest.TestCase):
    """Tests for line detection."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_detect_single_line(self):
        """Test detecting a single horizontal line."""
        img = create_glyph_row(["circle", "square", "triangle"])
        instances = self.processor.detect_glyphs(img, "test.png")
        lines = self.processor.detect_lines(instances)

        self.assertEqual(len(lines), 1)
        self.assertEqual(len(lines[0]), 3)

    def test_detect_multiple_lines(self):
        """Test detecting multiple lines."""
        img = create_multiline_image(
            [
                ["circle", "square"],
                ["triangle", "circle", "square"],
                ["square"],
            ]
        )
        instances = self.processor.detect_glyphs(img, "test.png")
        lines = self.processor.detect_lines(instances)

        self.assertEqual(len(lines), 3)

    def test_assign_glyphs_to_lines(self):
        """Test that glyphs are correctly grouped by line."""
        img = create_multiline_image(
            [
                ["circle", "square", "triangle"],
                ["square", "circle"],
            ]
        )
        instances = self.processor.detect_glyphs(img, "test.png")
        instances = self.processor.assign_positions(instances)

        # Check line numbers
        line_numbers = set(inst.position.line_number for inst in instances if inst.position)
        self.assertEqual(len(line_numbers), 2)

    def test_line_ordering(self):
        """Test that lines are ordered top to bottom."""
        img = create_multiline_image([["circle"], ["square"], ["triangle"]])
        instances = self.processor.detect_glyphs(img, "test.png")
        instances = self.processor.assign_positions(instances)

        # Sort by y-position of bounding box
        sorted_by_y = sorted(instances, key=lambda i: i.bounding_box.y)

        # Line numbers should increase with y
        prev_line = -1
        for inst in sorted_by_y:
            if inst.position:
                self.assertGreaterEqual(inst.position.line_number, prev_line)
                prev_line = inst.position.line_number

    def test_position_in_line(self):
        """Test that glyphs are ordered left to right within a line."""
        img = create_glyph_row(["circle", "square", "triangle", "circle"])
        instances = self.processor.detect_glyphs(img, "test.png")
        instances = self.processor.assign_positions(instances)

        # Sort by x-position
        sorted_by_x = sorted(instances, key=lambda i: i.bounding_box.x)

        # Position in line should increase with x
        for i, inst in enumerate(sorted_by_x):
            if inst.position:
                self.assertEqual(inst.position.position_in_line, i)


class TestFeatureExtraction(unittest.TestCase):
    """Tests for feature extraction."""

    def setUp(self):
        self.processor = GlyphProcessor()

    def test_extract_hu_moments(self):
        """Test calculating Hu moments."""
        glyph = create_test_glyph("circle", 64)
        moments = self.processor.compute_hu_moments(glyph)

        self.assertEqual(len(moments), 7)
        self.assertTrue(all(isinstance(m, float) for m in moments))
        self.assertTrue(all(m >= 0.0 for m in moments))

    def test_unsigned_hu_is_abs_of_signed_log_hu(self):
        """Unsigned log-Hu is |signed log-Hu|. Detection is not involved."""
        glyph = create_test_glyph("triangle", 64)
        signed = GlyphProcessor(ProcessorConfig(hu_sign_mode="signed"))
        unsigned = GlyphProcessor(ProcessorConfig(hu_sign_mode="unsigned"))
        signed_vec = signed.compute_hu_moments(glyph)
        unsigned_vec = unsigned.compute_hu_moments(glyph)
        self.assertEqual(unsigned_vec, [abs(v) for v in signed_vec])
        self.assertEqual(self.processor.compute_hu_moments(glyph), unsigned_vec)

    def test_unsigned_hu_collapses_reflection_sign_flip(self):
        """Horizontal flip: signed Hu5–Hu7 can diverge; unsigned should not."""
        glyph = create_test_glyph("triangle", 64)
        flipped = cv2.flip(glyph, 1)
        signed = GlyphProcessor(ProcessorConfig(hu_sign_mode="signed"))
        unsigned = GlyphProcessor(ProcessorConfig(hu_sign_mode="unsigned"))
        signed_d = float(
            np.linalg.norm(
                np.asarray(signed.compute_hu_moments(glyph))
                - np.asarray(signed.compute_hu_moments(flipped))
            )
        )
        unsigned_d = float(
            np.linalg.norm(
                np.asarray(unsigned.compute_hu_moments(glyph))
                - np.asarray(unsigned.compute_hu_moments(flipped))
            )
        )
        self.assertLess(unsigned_d, signed_d)
        self.assertLess(unsigned_d, 1.0)

    def test_invalid_hu_sign_mode_rejected(self):
        processor = GlyphProcessor(ProcessorConfig(hu_sign_mode="bogus"))
        with self.assertRaises(ValueError):
            processor.compute_hu_moments(create_test_glyph("circle", 64))

    def test_hu_moments_rotation_invariant(self):
        """Test that same glyph rotated gives similar moments."""
        # Create original glyph
        glyph1 = create_test_glyph("triangle", 64)

        # Create rotated version
        center = (32, 32)
        matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
        glyph2 = cv2.warpAffine(glyph1, matrix, (64, 64), borderValue=255)

        moments1 = self.processor.compute_hu_moments(glyph1)
        moments2 = self.processor.compute_hu_moments(glyph2)

        # First few moments should be similar (not exact due to interpolation)
        for m1, m2 in zip(moments1[:4], moments2[:4]):
            self.assertAlmostEqual(m1, m2, delta=1.0)

    def test_extract_features_normalized(self):
        """Test that features are properly computed."""
        img = create_test_glyph("square", 64)
        padded = np.ones((80, 80), dtype=np.uint8) * 255
        padded[8:72, 8:72] = img

        instances = self.processor.detect_glyphs(padded, "test.png")
        self.assertEqual(len(instances), 1)

        features = self.processor.extract_features(padded, instances[0])
        self.assertEqual(len(features), 7)  # 7 Hu moments

    def test_feature_vector_length(self):
        """Test that feature vectors have consistent length."""
        shapes = ["circle", "square", "triangle"]
        all_features = []

        for shape in shapes:
            glyph = create_test_glyph(shape, 64)
            padded = np.ones((80, 80), dtype=np.uint8) * 255
            padded[8:72, 8:72] = glyph

            instances = self.processor.detect_glyphs(padded, f"{shape}.png")
            if instances:
                features = self.processor.extract_features(padded, instances[0])
                all_features.append(features)

        # All feature vectors should have the same length
        lengths = [len(f) for f in all_features]
        self.assertEqual(len(set(lengths)), 1)

    def test_extract_features_batch(self):
        """Test extracting features for multiple glyphs."""
        img = create_glyph_row(["circle", "square", "triangle"])
        instances = self.processor.detect_glyphs(img, "test.png")

        instances = self.processor.extract_features_batch(img, instances)

        for inst in instances:
            self.assertEqual(len(inst.features), 7)
            self.assertTrue(all(isinstance(f, float) for f in inst.features))
            self.assertEqual(len(inst.ink_profile), self.processor.config.wide_profile_bins)
            self.assertEqual(
                len(inst.glyph_crop),
                self.processor.config.target_glyph_size[0]
                * self.processor.config.target_glyph_size[1],
            )


class TestGlyphImageOperations(unittest.TestCase):
    """Tests for glyph image extraction and saving."""

    def setUp(self):
        self.processor = GlyphProcessor()
        self.temp_dir = tempfile.mkdtemp()

    def test_extract_glyph_image(self):
        """Test extracting a glyph image from source."""
        img = np.ones((100, 100), dtype=np.uint8) * 255
        cv2.circle(img, (50, 50), 20, 0, -1)

        bbox = BoundingBox(x=25, y=25, width=50, height=50)
        extracted = self.processor.extract_glyph_image(img, bbox)

        # Should be resized to target size
        self.assertEqual(extracted.shape, self.processor.config.target_glyph_size)

    def test_save_glyph_image(self):
        """Test saving an extracted glyph to disk."""
        img = np.ones((100, 100), dtype=np.uint8) * 255
        cv2.circle(img, (50, 50), 20, 0, -1)

        bbox = BoundingBox(x=25, y=25, width=50, height=50)
        instance = GlyphInstance(
            instance_id="test_0001",
            source_image="test.png",
            bounding_box=bbox,
        )

        path = self.processor.save_glyph_image(img, instance, self.temp_dir)

        self.assertTrue(os.path.exists(path))
        self.assertEqual(instance.image_path, path)

        # Load and verify
        loaded = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.assertIsNotNone(loaded)
        self.assertEqual(loaded.shape, self.processor.config.target_glyph_size)


if __name__ == "__main__":
    unittest.main()
