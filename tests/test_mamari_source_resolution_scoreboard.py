"""Source-resolution scoreboard: cycle 16 GIF ceiling.

No honest higher-res public Ca7–Ca8 raster was available to vendor.
Ca.html PNGs are the same 522×74. ca.jpg has no published Ca7–Ca8
pixel bounds. lunar.html color GIFs fight THRESH_BINARY_INV. Do not
guess a crop. Standing lock stays 83/62 / 0/8 on the CEIPP GIFs.

Cataloger IDs stay G00n. No G00n→Barthel map. MockProvider only.
input/tablets/sample_tablet.png is a synthetic CV dummy, not Mamari.
"""

import json
import struct
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_delimiter_window_scoreboard import (
    STANDING_SLOT_MATCHES,
    STANDING_SLOT_UNIQUE_COUNTS,
    score_delimiter_windows,
)
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_neighbor_allograph_scoreboard import longest_mixed_repeating_n
from tests.test_mamari_position_alignment_scoreboard import published_ca7_ca8_stems
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_MIXED_REPEATING,
    STANDING_UNIQUE_CLUSTERS,
    mixed_repeating_ngrams,
    published_ca7_ca8_stem_counts,
    score_type_identity,
)

SURVEY_PATH = TRACING_DIR / "SOURCE_SURVEY.json"
GIF_PIXELS = {
    "sca0701.gif": (522, 74),
    "sca0702.gif": (522, 74),
    "sca0703.gif": (522, 74),
    "sca0801.gif": (522, 74),
    "sca0802.gif": (523, 74),
    "sca0803.gif": (522, 74),
}
GIF_MAX_PIXELS = (523, 74)
ALLOWED_FIXTURE_NAMES = frozenset(
    (*TRACING_NAMES, "ATTRIBUTION", "SOURCE_SURVEY.json")
)
FORBIDDEN_NAMES = frozenset(
    {
        "ca.jpg",
        "sample_tablet.png",
        "ca7a.gif",
        "ca7b.gif",
        "ca8a.gif",
        "ca8b.gif",
    }
)


def gif_logical_screen(path: Path) -> tuple[int, int]:
    """Logical-screen size from a GIF header. No decode, no crop."""
    data = path.read_bytes()
    if data[:6] not in (b"GIF87a", b"GIF89a"):
        raise ValueError(f"{path.name} is not a GIF")
    width, height = struct.unpack_from("<HH", data, 6)
    return width, height


def load_source_survey() -> dict:
    """Cycle-16 public-source survey. Offline; no live fetch."""
    with SURVEY_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


class TestGifLogicalScreen(unittest.TestCase):
    """Header parser for the 522×74 lock. No OpenCV."""

    def test_rejects_non_gif(self):
        path = Path(__file__)
        with self.assertRaises(ValueError):
            gif_logical_screen(path)


class TestMamariSourceResolutionScoreboard(unittest.TestCase):
    """Survey + standing lock. MockProvider only. No new image."""

    def setUp(self):
        self.survey = load_source_survey()
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)

    def test_survey_locks_gif_ceiling(self):
        """No published Ca7–Ca8 crop larger than 522×74 was vendored."""
        s = self.survey
        self.assertEqual(s["cycle"], 16)
        self.assertEqual(s["result"], "gif_ceiling")
        self.assertEqual(
            {name: tuple(size) for name, size in s["vendored"]["pixels"].items()},
            GIF_PIXELS,
        )
        self.assertEqual(s["vendored"]["max_pixels"], list(GIF_MAX_PIXELS))
        self.assertEqual(s["vendored"]["files"], list(TRACING_NAMES))
        lock = s["standing_lock"]
        self.assertEqual(lock["instances"], sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(lock["types"], STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(lock["window_matches"], STANDING_SLOT_MATCHES)
        self.assertEqual(lock["window_slots"], 8)
        self.assertFalse(lock["repeating_8gram"])
        for candidate in s["rejected"]:
            self.assertIsNone(
                candidate.get("crop_bounds"),
                f"{candidate['id']} must not invent crop bounds",
            )
        rejected_ids = {item["id"] for item in s["rejected"]}
        self.assertEqual(
            rejected_ids,
            {
                "ca_html_pngs",
                "ca_jpg",
                "lunar_color_gifs",
                "fischer_pngs",
                "svg_full_lines",
                "individualized_tr_pngs",
                "sample_tablet",
            },
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_vendored_gifs_are_522x74(self):
        """CEIPP strips stay ~522×74 (sca0802 is 523×74). GIF ceiling."""
        for path in self.paths:
            self.assertEqual(gif_logical_screen(path), GIF_PIXELS[path.name], path.name)
            self.assertLessEqual(gif_logical_screen(path)[0], GIF_MAX_PIXELS[0])
            self.assertEqual(gif_logical_screen(path)[1], GIF_MAX_PIXELS[1])
        self.assertEqual(self.survey["vendored"]["max_pixels"], list(GIF_MAX_PIXELS))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_fixture_dir_has_no_higher_res_raster(self):
        """Cycle 16 adds a survey, not a new Mamari image."""
        names = {path.name for path in TRACING_DIR.iterdir() if path.is_file()}
        self.assertEqual(names, ALLOWED_FIXTURE_NAMES)
        self.assertTrue((TRACING_DIR / "SOURCE_SURVEY.json").is_file())
        self.assertTrue((TRACING_DIR / "ATTRIBUTION").is_file())
        self.assertFalse(FORBIDDEN_NAMES & names)
        self.assertNotIn("sample_tablet.png", [path.name for path in self.paths])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_standing_lock_unchanged_on_gifs(self):
        """Same pipeline, same GIFs: 83/62 / 0/8. No repeating 8-gram."""
        instances = process_tracings(self.paths)
        image_lines = ca7_ca8_sequences(instances)
        published = published_ca7_ca8_stems()
        published_ca7, published_ca8 = published_ca7_ca8_stem_counts()
        identity = score_type_identity(
            instances,
            self.ngram_analyzer,
            published_ca7,
            published_ca8,
        )
        window = score_delimiter_windows(instances, image_lines, published)
        self.assertEqual(identity.instance_count, 83)
        self.assertEqual(identity.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(identity.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(
            mixed_repeating_ngrams(image_lines, self.ngram_analyzer),
            list(STANDING_MIXED_REPEATING),
        )
        self.assertEqual(longest_mixed_repeating_n(image_lines, self.ngram_analyzer), 2)
        self.assertEqual(
            self.ngram_analyzer.extract_ngrams(image_lines, n=8, min_frequency=2),
            [],
        )
        self.assertEqual(window.slot_matches, STANDING_SLOT_MATCHES)
        unique_counts = tuple(len(set(ids)) for ids in window.slot_ids)
        self.assertEqual(unique_counts, STANDING_SLOT_UNIQUE_COUNTS)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
