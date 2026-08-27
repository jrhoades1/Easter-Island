"""Image-side Mamari scoreboard: stock CV on Kohaumotu Ca7–Ca8 tracings.

input/tablets/sample_tablet.png is a synthetic CV dummy (circles/triangles),
not Mamari. Do not use it here.

Cataloger emits G00n cluster IDs. There is no G00n→Barthel map. Wide
connected blobs may be valley-split, but types are still unsigned-Hu
clusters, so Guy's delimiter is not the target. The honest proxy is a
repeating 8-gram of frequency ≥2.

That proxy is expected to fail until a mixed 8-gram actually repeats.
The delimiter-window scoreboard locks how many of the 8 published
delimiter slots share one G00n ID across Ca7/Ca8 repetitions (0–8).
Cycle 16 found no honest higher-res public Ca7–Ca8 raster; the
522×74 CEIPP GIFs remain the image-side ceiling. Cycle 17 searches
the full G00n sequence (concat + each line) and still finds no
repeating 8-gram; longest mixed n anywhere stays 2. Cycle 18 locks
nearest 8-window Hamming: concat min 3, published-window min 7.
"""

import random
import re
import unittest
from pathlib import Path

import cv2
import numpy as np

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from models.glyphs import BoundingBox, GlyphInstance, GlyphPosition
from processors.glyph_processor import GlyphProcessor, instances_to_line_sequences

SHUFFLE_SEED = 0

TRACING_DIR = Path(__file__).parent / "fixtures" / "mamari_ca7_ca8"
TRACING_NAMES = (
    "sca0701.gif",
    "sca0702.gif",
    "sca0703.gif",
    "sca0801.gif",
    "sca0802.gif",
    "sca0803.gif",
)
CLUSTER_ID = re.compile(r"^G\d{3}$")


def load_tracing_bgr(path: Path) -> np.ndarray:
    """Load a vendored tracing. Pillow fallback: OpenCV rejects sca0801.gif."""
    image = cv2.imread(str(path))
    if image is not None:
        return image
    from PIL import Image

    rgb = np.array(Image.open(path).convert("RGB"))
    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)


def process_tracings(
    paths: list[Path],
    processor: GlyphProcessor | None = None,
) -> list[GlyphInstance]:
    """Stock GlyphProcessor on the Ca7–Ca8 strips.

    Default processor uses unsigned log-Hu and the wide-ligature valley
    split. Pass a configured processor to keep a prior-cycle path.
    """
    processor = processor or GlyphProcessor()
    all_instances: list[GlyphInstance] = []
    for path in paths:
        image = load_tracing_bgr(path)
        instances = processor.detect_glyphs(image, path.name)
        instances = processor.assign_positions(instances)
        instances = processor.extract_features_batch(image, instances)
        all_instances.extend(instances)
    _, clustered = processor.cluster_glyphs(all_instances)
    return clustered


def shuffled_line_ids(lines: list[list[str]], seed: int) -> list[list[str]]:
    """Same cluster IDs, destroyed order. Line lengths are preserved."""
    rng = random.Random(seed)
    flat = [gid for line in lines for gid in line]
    rng.shuffle(flat)
    shuffled: list[list[str]] = []
    offset = 0
    for line in lines:
        shuffled.append(flat[offset : offset + len(line)])
        offset += len(line)
    return shuffled


def ca7_ca8_sequences(instances: list[GlyphInstance]) -> list[list[str]]:
    """Concatenate display strips into Ca7 and Ca8 reading-order sequences."""
    by_line: dict[str, list[GlyphInstance]] = {"07": [], "08": []}
    for inst in instances:
        if inst.position is None or not inst.cluster_id:
            continue
        stem = inst.source_image[3:5]
        if stem in by_line:
            by_line[stem].append(inst)
    sequences: list[list[str]] = []
    for stem in ("07", "08"):
        ordered = sorted(
            by_line[stem],
            key=lambda inst: (
                inst.source_image,
                inst.position.line_number,
                inst.position.position_in_line,
            ),
        )
        sequences.append([inst.cluster_id for inst in ordered])
    return sequences


class TestInstancesToLineSequences(unittest.TestCase):
    """Adapter reads GlyphInstance.position / cluster_id, not a fake lexicon."""

    def test_reading_order_by_line_and_position(self):
        bbox = BoundingBox(x=0, y=0, width=10, height=10)
        instances = [
            GlyphInstance(
                "b",
                "sca0801.gif",
                bbox,
                cluster_id="G002",
                position=GlyphPosition(0, 1, 2),
            ),
            GlyphInstance(
                "a",
                "sca0701.gif",
                bbox,
                cluster_id="G001",
                position=GlyphPosition(0, 0, 1),
            ),
            GlyphInstance(
                "c",
                "sca0801.gif",
                bbox,
                cluster_id="G003",
                position=GlyphPosition(0, 0, 2),
            ),
        ]
        self.assertEqual(
            instances_to_line_sequences(instances),
            [["G001"], ["G003", "G002"]],
        )


class TestMamariImageScoreboard(unittest.TestCase):
    """Stock CV → G00n sequences → n=8 scoreboard. MockProvider only."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.lines = ca7_ca8_sequences(self.instances)

    def test_stock_cv_emits_g00n_sequences(self):
        """Pipeline runs; IDs stay G00n; sample_tablet.png is not used."""
        self.assertTrue(self.instances, "stock processor detected no glyphs")
        self.assertEqual(len(self.lines), 2)
        self.assertTrue(self.lines[0], "Ca7 sequence empty")
        self.assertTrue(self.lines[1], "Ca8 sequence empty")
        for seq in self.lines:
            for cluster_id in seq:
                self.assertRegex(cluster_id, CLUSTER_ID)
        strip_seqs = instances_to_line_sequences(self.instances)
        self.assertTrue(strip_seqs)
        self.assertEqual(self.provider.get_call_history(), [])

    @unittest.expectedFailure
    def test_repeating_8gram_delimiter_proxy(self):
        """Repeating 8-gram (freq ≥2) is the image-side delimiter analogue.

        Expected to fail: no Barthel remapping; the global keep-ID pass
        still yields mixed 2-grams, not a repeating 8-gram.
        Delimiter-window slot matches stay 0/8.
        """
        ngrams = self.ngram_analyzer.extract_ngrams(self.lines, n=8, min_frequency=2)
        self.assertTrue(
            ngrams,
            "no repeating 8-grams from stock CV on Ca7–Ca8 tracings",
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_shuffled_image_sequences_share_no_repeating_8gram(self):
        """Same G00n tokens, shuffled: no shared repeating 8-gram."""
        shuffled = shuffled_line_ids(self.lines, SHUFFLE_SEED)
        original_flat = [gid for line in self.lines for gid in line]
        shuffled_flat = [gid for line in shuffled for gid in line]
        self.assertEqual(sorted(shuffled_flat), sorted(original_flat))
        self.assertNotEqual(shuffled, self.lines)

        original = self.ngram_analyzer.extract_ngrams(self.lines, n=8, min_frequency=2)
        shuffled_ngrams = self.ngram_analyzer.extract_ngrams(
            shuffled, n=8, min_frequency=2
        )
        shared = {gram for gram, _ in original} & {gram for gram, _ in shuffled_ngrams}
        self.assertEqual(shared, set())
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
