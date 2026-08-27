"""Wikimedia Mamari C-a photo vs the Kohaumotu GIF ceiling.

Cycle 49 vendors the public Chauvet 1935 / Widow Hoare photograph of
tablet C side a from Wikimedia Commons (GFDL / CC BY-SA 3.0). The
verified upload path is 1/14/, not 4/4e. INSCRIBE was not scraped.

Pixels per calendar line: 2040×1424 / 14 published Ca.html lines vs
the concatenated Ca7/Ca8 CEIPP GIF wraps. The photo is strictly
larger. An equal-split Ca6–Ca9 crop of the measured tablet bbox is
also larger per line. No published crop bounds exist.

Stock CV on that crop does not emit the published 43+40 stems, so
published-window Hamming cannot be rescored. Detector is not retuned.
GIF lock stays 83/62 / Hamming 6. No G00n→Barthel map. MockProvider
only.
"""

import hashlib
import json
import struct
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from processors.glyph_processor import GlyphProcessor, ProcessorConfig
from tests.test_mamari_delimiter_window_scoreboard import delimiter_image_windows
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    load_tracing_bgr,
    process_tracings,
)
from tests.test_mamari_nearest_8window_scoreboard import (
    STANDING_PUBLISHED_MIN_HAMMING,
    score_nearest_8windows,
)
from tests.test_mamari_position_alignment_scoreboard import published_ca7_ca8_stems
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_source_resolution_scoreboard import GIF_PIXELS, gif_logical_screen
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_UNIQUE_CLUSTERS,
    published_ca7_ca8_stem_counts,
)

PHOTO_DIR = Path(__file__).parent / "fixtures" / "mamari_c_a_wikimedia"
PHOTO_PATH = PHOTO_DIR / "Rongorongo_C-a_Mamari.jpg"
SURVEY_PATH = PHOTO_DIR / "PIXEL_SURVEY.json"
ATTRIBUTION_PATH = PHOTO_DIR / "ATTRIBUTION"

PHOTO_SIZE = (2040, 1424)
PHOTO_BYTES = 547228
PHOTO_SHA1 = "4d2b3e539d0167d68adea43c3274e894625f1beb"
COMMONS_PAGE = "https://commons.wikimedia.org/wiki/File:Rongorongo_C-a_Mamari.jpg"
UPLOAD_URL = "https://upload.wikimedia.org/wikipedia/commons/1/14/Rongorongo_C-a_Mamari.jpg"
SIDE_A_LINE_COUNT = 14
CALENDAR_LINE_COUNT = 4
GIF_LINE_PIXELS = {"Ca7": 115884, "Ca8": 115958}
GIF_MAX_LINE_PIXELS = 115958
# Measured tablet extent; 14-way split yields Ca6–Ca9. Not a published plate.
TABLET_BBOX = (71, 59, 1914, 1279)
CALENDAR_CROP = (71, 515, 1914, 366)
CALENDAR_STRIPS = {
    "Ca6": (71, 515, 1914, 92),
    "Ca7": (71, 607, 1914, 91),
    "Ca8": (71, 698, 1914, 91),
    "Ca9": (71, 789, 1914, 92),
}


def jpeg_sof_size(path: Path) -> tuple[int, int]:
    """SOF width×height from a JPEG header. No pixel decode."""
    data = path.read_bytes()
    if data[:2] != b"\xff\xd8":
        raise ValueError(f"{path.name} is not a JPEG")
    index = 2
    while index < len(data) - 3:
        if data[index] != 0xFF:
            index += 1
            continue
        marker = data[index + 1]
        if marker in (0xD8, 0xD9) or marker in (0x00, 0x01) or 0xD0 <= marker <= 0xD7:
            index += 2
            continue
        seglen = struct.unpack_from(">H", data, index + 2)[0]
        if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            _precision, height, width = struct.unpack_from(">BHH", data, index + 4)
            return width, height
        index += 2 + seglen
    raise ValueError(f"{path.name} has no SOF")


def gif_line_pixels() -> dict[str, int]:
    """Concatenated wrap-strip pixels for each vendored Ca7/Ca8 line."""
    totals = {"Ca7": 0, "Ca8": 0}
    for name in TRACING_NAMES:
        width, height = gif_logical_screen(TRACING_DIR / name)
        totals["Ca7" if name.startswith("sca07") else "Ca8"] += width * height
    return totals


def load_pixel_survey() -> dict:
    """Cycle-49 photo pixel lock. Offline; no live fetch."""
    with SURVEY_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def slice_bgr(image, box: tuple[int, int, int, int]):
    """axis-aligned crop: (x, y, w, h)."""
    x, y, width, height = box
    return image[y : y + height, x : x + width]


def process_calendar_strips(image, processor: GlyphProcessor | None = None):
    """Stock GlyphProcessor on the four equal-split Ca6–Ca9 strips."""
    processor = processor or GlyphProcessor()
    instances = []
    for name, box in CALENDAR_STRIPS.items():
        strip = slice_bgr(image, box)
        found = processor.detect_glyphs(strip, f"{name}.jpg")
        found = processor.assign_positions(found)
        found = processor.extract_features_batch(strip, found)
        instances.extend(found)
    _, clustered = processor.cluster_glyphs(instances)
    return clustered


def photo_ca7_ca8_ids(instances) -> list[list[str]]:
    """Reading-order G00n sequences for the Ca7 and Ca8 strips."""
    sequences = []
    for name in ("Ca7.jpg", "Ca8.jpg"):
        ordered = sorted(
            (
                inst
                for inst in instances
                if inst.source_image == name and inst.cluster_id and inst.position
            ),
            key=lambda inst: (inst.position.line_number, inst.position.position_in_line),
        )
        sequences.append([inst.cluster_id for inst in ordered])
    return sequences


def equal_split_band(bbox: tuple[int, int, int, int], start: int, end: int, lines: int):
    """Inclusive-start exclusive-end band of an equal line split."""
    x, y, width, height = bbox
    return (x, y + start * height // lines, width, y + end * height // lines - (y + start * height // lines))


class TestJpegSof(unittest.TestCase):
    """Header parser for the 2040×1424 lock. No OpenCV."""

    def test_rejects_non_jpeg(self):
        with self.assertRaises(ValueError):
            jpeg_sof_size(Path(__file__))


class TestMamariWikimediaCaPhotoScoreboard(unittest.TestCase):
    """Vendored photo pixels vs GIFs. MockProvider only."""

    def setUp(self):
        self.survey = load_pixel_survey()
        self.provider = MockProvider()
        self.assertTrue(PHOTO_PATH.is_file())
        self.assertTrue(ATTRIBUTION_PATH.is_file())

    def test_vendored_jpeg_is_2040x1424(self):
        """Commons C-a original is 2040×1424. Path is 1/14/, not 4/4e."""
        data = PHOTO_PATH.read_bytes()
        self.assertEqual(jpeg_sof_size(PHOTO_PATH), PHOTO_SIZE)
        self.assertEqual(len(data), PHOTO_BYTES)
        self.assertEqual(hashlib.sha1(data).hexdigest(), PHOTO_SHA1)
        s = self.survey["vendored"]
        self.assertEqual(s["pixels"], list(PHOTO_SIZE))
        self.assertEqual(s["bytes"], PHOTO_BYTES)
        self.assertEqual(s["sha1"], PHOTO_SHA1)
        self.assertEqual(s["upload_url"], UPLOAD_URL)
        self.assertEqual(s["commons_page"], COMMONS_PAGE)
        self.assertNotIn("/4/4e/", s["upload_url"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_attribution_names_source_license_and_hoare(self):
        """ATTRIBUTION records Commons URL, GFDL / CC BY-SA, Chauvet/Hoare."""
        text = ATTRIBUTION_PATH.read_text(encoding="utf-8")
        self.assertIn(COMMONS_PAGE, text)
        self.assertIn(UPLOAD_URL, text)
        self.assertIn("Chauvet", text)
        self.assertIn("Widow Hoare", text)
        self.assertIn("GFDL", text)
        self.assertIn("CC BY-SA 3.0", text)
        self.assertIn("INSCRIBE", text)
        self.assertIn("not scraped", text.lower())
        self.assertFalse(self.survey["inscribe_scraped"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_photo_has_more_pixels_per_calendar_line_than_gifs(self):
        """2040×1424 / 14 Ca lines beats the GIF wrap totals. Crop does too."""
        gif = gif_line_pixels()
        self.assertEqual(gif, GIF_LINE_PIXELS)
        self.assertEqual(max(gif.values()), GIF_MAX_LINE_PIXELS)
        for name, expected in GIF_PIXELS.items():
            self.assertEqual(gif_logical_screen(TRACING_DIR / name), expected)
        full = PHOTO_SIZE[0] * PHOTO_SIZE[1]
        self.assertEqual(full, self.survey["photo_full_pixels"])
        self.assertGreater(full, GIF_MAX_LINE_PIXELS * SIDE_A_LINE_COUNT)
        x, y, width, height = CALENDAR_CROP
        crop_pixels = width * height
        self.assertEqual(CALENDAR_CROP, equal_split_band(TABLET_BBOX, 5, 9, SIDE_A_LINE_COUNT))
        self.assertEqual(crop_pixels, self.survey["derived_crop_pixels"])
        self.assertGreater(crop_pixels, GIF_MAX_LINE_PIXELS * CALENDAR_LINE_COUNT)
        self.assertTrue(self.survey["strictly_larger_per_calendar_line"])
        self.assertTrue(self.survey["derived_crop_strictly_larger_per_line"])
        self.assertIsNone(self.survey["published_crop_bounds"])
        self.assertEqual(self.survey["side_a_lines"], SIDE_A_LINE_COUNT)
        corpus = load_corpus_survey()["wikimedia_c_a_photo"]
        self.assertEqual(corpus["cycle"], 49)
        self.assertEqual(corpus["result"], "photo_larger_published_hamming_unaligned")
        self.assertTrue(corpus["strictly_larger_per_calendar_line"])
        self.assertFalse(corpus["published_hamming_rescored"])
        self.assertFalse(corpus["detector_retuned"])
        self.assertEqual(corpus["image_track"], "parked")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stock_cv_on_crop_cannot_rescore_published_hamming(self):
        """Larger photo, but crop lengths ≠ 43+40. Hamming not rescored."""
        self.assertFalse(self.survey["published_hamming_rescored"])
        self.assertFalse(self.survey["detector_retuned"])
        self.assertTrue(ProcessorConfig().delimiter_slot_crop_hamming_merge)
        self.assertFalse(ProcessorConfig().delimiter_slot_crop_leftover_merge)
        image = load_tracing_bgr(PHOTO_PATH)
        self.assertEqual(image.shape[1], PHOTO_SIZE[0])
        self.assertEqual(image.shape[0], PHOTO_SIZE[1])
        crop = slice_bgr(image, CALENDAR_CROP)
        self.assertEqual(crop.shape[1], CALENDAR_CROP[2])
        self.assertEqual(crop.shape[0], CALENDAR_CROP[3])
        instances = process_calendar_strips(image)
        self.assertTrue(instances)
        lines = photo_ca7_ca8_ids(instances)
        published_ca7, published_ca8 = published_ca7_ca8_stem_counts()
        self.assertEqual((published_ca7, published_ca8), (43, 40))
        self.assertNotEqual((len(lines[0]), len(lines[1])), (43, 40))
        published = published_ca7_ca8_stems()
        with self.assertRaises(ValueError):
            delimiter_image_windows(lines, published)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariWikimediaCaPhotoImageSnapshot(unittest.TestCase):
    """Cycle 49 does not retune clustering. 83/62 / Hamming 6 stays."""

    def test_gif_scoreboard_still_hamming_6(self):
        """Existing published-window lock is unchanged on the CEIPP GIFs."""
        paths = [TRACING_DIR / name for name in TRACING_NAMES]
        provider = MockProvider()
        instances = process_tracings(paths)
        image_lines = ca7_ca8_sequences(instances)
        score = score_nearest_8windows(instances, image_lines, published_ca7_ca8_stems())
        self.assertEqual(score.instance_count, 83)
        self.assertEqual(score.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(score.published_hamming, STANDING_PUBLISHED_MIN_HAMMING)
        self.assertEqual(score.published_hamming, 6)
        survey = load_corpus_survey()
        image = survey["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)
        self.assertEqual(load_pixel_survey()["standing_image_lock"], image)
        self.assertEqual(provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
