"""Second published Barthel passage: remainder of cited Ca.html.

Cycle 28 text-search lock. The first passage is the existing 101-stem
Ca6–Ca9 calendar fixture. This cycle vendors the already-cited
Kohaumotu Ca.html and copies the other published Barthel tokens from
that page. No invented numbers. No uncited scrape. No G00n→Barthel
map. No type merge. No detector retune.

Second passage = Ca1–Ca5, Ca6 prefix before the first 390.041, Ca9
tail after the two opening 040s, and Ca10–Ca14. Ca7–Ca8 are entirely
inside the first passage.

Locks at a high level: Guy's 8-stem delimiter is absent; 600 is not
window-adjacent (no windows); 040-run and cell counts. Image track
stays parked. MockProvider only.
"""

import json
import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from processors.glyph_processor import min_pairwise_window_hamming
from tests.test_mamari_040_run_profile_scoreboard import (
    STEM_040,
    run_tuple,
    score_040_run_profile,
    variant_motifs,
)
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    barthel_stems,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_delimiter_cell_scoreboard import score_delimiter_cells
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
from tests.test_mamari_nearest_8window_scoreboard import STANDING_PUBLISHED_MIN_HAMMING
from tests.test_mamari_non040_inventory_scoreboard import score_non040_inventory
from tests.test_mamari_position_alignment_scoreboard import (
    find_ngram_hits,
    published_ca7_ca8_stems,
)
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_UNIQUE_CLUSTERS,
    published_ca7_ca8_stem_counts,
    score_type_identity,
)

CA_HTML_DIR = Path(__file__).parent / "fixtures" / "mamari_ca_html"
CA_HTML_PATH = CA_HTML_DIR / "Ca.html"
SURVEY_PATH = CA_HTML_DIR / "CORPUS_SURVEY.json"
CITED_CA_URL = "http://kohaumotu.org/Rongorongo/C/Ca.html"

CALENDAR_LINE_NAMES = ("Ca6", "Ca7", "Ca8", "Ca9")
REMAINDER_LINE_NAMES = (
    "Ca1",
    "Ca2",
    "Ca3",
    "Ca4",
    "Ca5",
    "Ca6",
    "Ca9",
    "Ca10",
    "Ca11",
    "Ca12",
    "Ca13",
    "Ca14",
)
CALENDAR_START_TOKEN = "390.041"
CALENDAR_CA9_NIGHT_SIGNS = 2

STANDING_CALENDAR_STEM_COUNTS = (16, 43, 40, 2)
STANDING_REMAINDER_STEM_COUNTS = (40, 35, 39, 36, 38, 24, 30, 36, 37, 33, 33, 35)
STANDING_REMAINDER_STEM_TOTAL = 416
STANDING_GUY_DELIMITER_PRESENT = False
STANDING_CA6_VARIANT_PRESENT = False
STANDING_WINDOW_COUNT = 0
STANDING_600_COUNT = 5
STANDING_600_WINDOW_ADJACENT = False
STANDING_600_HITS = (("Ca1", 14), ("Ca1", 17), ("Ca2", 8), ("Ca5", 23), ("Ca6", 19))
STANDING_040_RUN_COUNT = 6
STANDING_040_TOKEN_COUNT = 6
STANDING_040_RUN_LENGTHS = (1, 1, 1, 1, 1, 1)
STANDING_040_RUNS = (
    ("Ca10", 11, 12, 1, False),
    ("Ca10", 22, 23, 1, False),
    ("Ca10", 30, 31, 1, False),
    ("Ca11", 6, 7, 1, False),
    ("Ca11", 18, 19, 1, False),
    ("Ca12", 1, 2, 1, False),
)
STANDING_CELL_COUNT = 12
STANDING_EMPTY_CELL_COUNT = 0
STANDING_HTML_BYTES = 8015
_LINE_HEADER = re.compile(r'<h3><a name="Line_(\d+)">')


def load_corpus_survey() -> dict:
    """Cycle-28 cited-source survey. Offline; no live fetch."""
    with SURVEY_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_vendored_ca_html() -> str:
    """Return the vendored Kohaumotu Ca.html snapshot."""
    return CA_HTML_PATH.read_text(encoding="utf-8")


def extract_ca_published_tokens(html: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Ca.html <td> text.

    Does not invent numbers. Image cells are skipped. Line 14 has no
    trailing <hr />, so the split is on Line_N headers only.
    """
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"Ca{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def calendar_start_index(ca6: list[str]) -> int:
    """First published 390.041 on Ca6. Same bound as the calendar fixture."""
    for index, token in enumerate(ca6):
        if token.startswith(CALENDAR_START_TOKEN):
            return index
    raise ValueError("Ca6 has no published 390.041 calendar start")


def calendar_published_tokens(published: dict[str, list[str]]) -> dict[str, list[str]]:
    """Ca6–Ca9 calendar slice already vendored in the first fixture."""
    start = calendar_start_index(published["Ca6"])
    return {
        "Ca6": published["Ca6"][start:],
        "Ca7": published["Ca7"],
        "Ca8": published["Ca8"],
        "Ca9": published["Ca9"][:CALENDAR_CA9_NIGHT_SIGNS],
    }


def remainder_published_tokens(published: dict[str, list[str]]) -> dict[str, list[str]]:
    """Published Ca.html tokens outside the 101-stem calendar extract."""
    start = calendar_start_index(published["Ca6"])
    return {
        "Ca1": published["Ca1"],
        "Ca2": published["Ca2"],
        "Ca3": published["Ca3"],
        "Ca4": published["Ca4"],
        "Ca5": published["Ca5"],
        "Ca6": published["Ca6"][:start],
        "Ca9": published["Ca9"][CALENDAR_CA9_NIGHT_SIGNS:],
        "Ca10": published["Ca10"],
        "Ca11": published["Ca11"],
        "Ca12": published["Ca12"],
        "Ca13": published["Ca13"],
        "Ca14": published["Ca14"],
    }


def published_stems(tokens: list[str]) -> list[str]:
    """Mechanical stems. Same as barthel_stems, plus ':' ligature split.

    Kohaumotu writes stacked ligatures with ':' (047:005, 042:009).
    The calendar fixture has none, so barthel_stems splits only on '.'.
    Rewriting ':' to '.' keeps those published numbers; it does not
    remap types.
    """
    return barthel_stems([token.replace(":", ".") for token in tokens])


def remainder_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Remainder slices as stem sequences, REMAINDER_LINE_NAMES order."""
    remainder = remainder_published_tokens(published)
    return [published_stems(remainder[name]) for name in REMAINDER_LINE_NAMES]


class TestSecondPassageHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>001-009-755-</td></tr>"
            "<tr><td>600V-009*</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>047:005-040-</td></tr></table>"
        )
        published = extract_ca_published_tokens(html)
        self.assertEqual(published["Ca1"], ["001", "009", "755", "600V", "009*"])
        self.assertEqual(published["Ca2"], ["047:005", "040"])

    def test_colon_ligature_splits_like_dot(self):
        """':' is a published ligature mark, not a dropped token."""
        self.assertEqual(published_stems(["047:005", "390.041"]), ["047", "005", "390", "041"])
        self.assertEqual(barthel_stems(["047:005"]), [])
        self.assertEqual(published_stems(["600V", "002V?", "000!"]), ["600", "002", "000"])

    def test_calendar_and_remainder_partition_ca6_ca9(self):
        """Ca6/Ca9 split on the published calendar bounds; Ca7–Ca8 stay first."""
        published = {
            "Ca6": ["005", "600V", "390.041", "315y", "041"],
            "Ca7": ["040", "040"],
            "Ca8": ["280"],
            "Ca9": ["040", "040", "520", "070"],
            "Ca1": ["001"],
        }
        calendar = calendar_published_tokens(published)
        remainder = remainder_published_tokens(published)
        self.assertEqual(calendar["Ca6"], ["390.041", "315y", "041"])
        self.assertEqual(remainder["Ca6"], ["005", "600V"])
        self.assertEqual(calendar["Ca9"], ["040", "040"])
        self.assertEqual(remainder["Ca9"], ["520", "070"])
        self.assertEqual(calendar["Ca7"], ["040", "040"])
        self.assertNotIn("Ca7", remainder)
        self.assertNotIn("Ca8", remainder)


class TestMamariSecondPassageScoreboard(unittest.TestCase):
    """Cited Ca.html remainder lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.html = load_vendored_ca_html()
        self.published = extract_ca_published_tokens(self.html)
        self.calendar = calendar_published_tokens(self.published)
        self.remainder = remainder_published_tokens(self.published)
        self.lines = remainder_line_stems(self.published)
        self.cells = score_delimiter_cells(self.lines, line_names=REMAINDER_LINE_NAMES)
        self.runs = score_040_run_profile(self.lines, line_names=REMAINDER_LINE_NAMES)
        self.inventory = score_non040_inventory(
            self.lines, line_names=REMAINDER_LINE_NAMES
        )

    def test_vendored_html_is_the_cited_ca_page(self):
        """Snapshot is the already-cited Ca.html; 14 published lines."""
        self.assertTrue(CA_HTML_PATH.is_file())
        self.assertTrue((CA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertEqual(CA_HTML_PATH.stat().st_size, STANDING_HTML_BYTES)
        self.assertIn("Item C:Mamari", self.html)
        self.assertEqual(list(self.published), [f"Ca{n}" for n in range(1, 15)])
        self.assertEqual(self.survey["second_passage"]["source_page"], CITED_CA_URL)
        first = load_mamari_fixture()
        self.assertEqual(first["source"]["primary"]["url"], CITED_CA_URL)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_calendar_extract_matches_existing_fixture(self):
        """HTML Ca6–Ca9 calendar slice is the 101-stem first passage."""
        fixture = fixture_line_stems(load_mamari_fixture())
        extracted = [
            barthel_stems(self.calendar[name]) for name in CALENDAR_LINE_NAMES
        ]
        self.assertEqual(extracted, fixture)
        self.assertEqual(
            [len(line) for line in extracted],
            list(STANDING_CALENDAR_STEM_COUNTS),
        )
        self.assertEqual(sum(len(line) for line in extracted), 101)
        self.assertEqual(self.calendar["Ca9"], ["040", "040"])
        self.assertTrue(self.calendar["Ca6"][0].startswith(CALENDAR_START_TOKEN))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remainder_is_the_other_published_tokens(self):
        """Second passage is Ca.html minus the calendar extract. 416 stems."""
        self.assertEqual(tuple(self.remainder), REMAINDER_LINE_NAMES)
        self.assertEqual(
            [len(line) for line in self.lines],
            list(STANDING_REMAINDER_STEM_COUNTS),
        )
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_REMAINDER_STEM_TOTAL)
        self.assertNotIn("Ca7", self.remainder)
        self.assertNotIn("Ca8", self.remainder)
        self.assertEqual(self.remainder["Ca6"][-1], "001.006")
        self.assertEqual(self.remainder["Ca9"][0], "520")
        rebuilt_ca6 = self.remainder["Ca6"] + self.calendar["Ca6"]
        rebuilt_ca9 = self.calendar["Ca9"] + self.remainder["Ca9"]
        self.assertEqual(rebuilt_ca6, self.published["Ca6"])
        self.assertEqual(rebuilt_ca9, self.published["Ca9"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_guys_8stem_delimiter_is_absent(self):
        """Guy 390 041 378 041 670 008 078 711 does not occur."""
        hits = find_ngram_hits(self.lines, DELIMITER_MOTIF)
        self.assertEqual(hits, [])
        self.assertEqual(bool(hits), STANDING_GUY_DELIMITER_PRESENT)
        eightgrams = self.analyzer.extract_ngrams(self.lines, n=8, min_frequency=2)
        self.assertNotIn(DELIMITER_MOTIF, [gram for gram, _freq in eightgrams])
        for variant in variant_motifs(DELIMITER_MOTIF):
            self.assertEqual(find_ngram_hits(self.lines, variant), [])
        self.assertEqual(self.cells.windows, ())
        self.assertEqual(len(self.cells.windows), STANDING_WINDOW_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_600_is_present_but_not_window_adjacent(self):
        """Five 600 hits; no window, so none are window-adjacent."""
        hits = [
            (REMAINDER_LINE_NAMES[line_index], start)
            for line_index, sequence in enumerate(self.lines)
            for start, token in enumerate(sequence)
            if token == "600"
        ]
        self.assertEqual(tuple(hits), STANDING_600_HITS)
        self.assertEqual(len(hits), STANDING_600_COUNT)
        by_stem = {row.stem: row for row in self.inventory.rows}
        self.assertEqual(by_stem["600"].count, STANDING_600_COUNT)
        self.assertEqual(by_stem["600"].window_adjacent, STANDING_600_WINDOW_ADJACENT)
        self.assertFalse(by_stem["600"].window_adjacent)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_040_run_and_cell_counts(self):
        """Six length-1 040 runs on Ca10–Ca12; twelve windowless cells."""
        locked = tuple(run_tuple(run) for run in self.runs.runs)
        self.assertEqual(len(locked), STANDING_040_RUN_COUNT)
        self.assertEqual(locked, STANDING_040_RUNS)
        self.assertEqual(
            tuple(run.length for run in self.runs.runs),
            STANDING_040_RUN_LENGTHS,
        )
        self.assertEqual(
            sum(run.length for run in self.runs.runs),
            STANDING_040_TOKEN_COUNT,
        )
        self.assertTrue(all(not run.precedes_delimiter for run in self.runs.runs))
        self.assertEqual(len(self.cells.cells), STANDING_CELL_COUNT)
        self.assertEqual(
            sum(1 for cell in self.cells.cells if cell.length == 0),
            STANDING_EMPTY_CELL_COUNT,
        )
        self.assertTrue(all(cell.following_window is None for cell in self.cells.cells))
        self.assertEqual(
            tuple(cell.length for cell in self.cells.cells),
            STANDING_REMAINDER_STEM_COUNTS,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json is the standing cycle-28 lock."""
        second = self.survey["second_passage"]
        self.assertEqual(self.survey["cycle"], 28)
        self.assertEqual(self.survey["result"], "second_passage_vendored")
        self.assertEqual(self.survey["first_passage"]["stem_count"], 101)
        self.assertEqual(second["stem_count"], STANDING_REMAINDER_STEM_TOTAL)
        self.assertEqual(second["line_slices"], list(REMAINDER_LINE_NAMES))
        self.assertEqual(second["stem_counts_by_line"], list(STANDING_REMAINDER_STEM_COUNTS))
        self.assertEqual(second["guy_8stem_delimiter"], STANDING_GUY_DELIMITER_PRESENT)
        self.assertEqual(second["ca6_variant_delimiter"], STANDING_CA6_VARIANT_PRESENT)
        self.assertEqual(second["window_count"], STANDING_WINDOW_COUNT)
        self.assertEqual(second["stem_600_count"], STANDING_600_COUNT)
        self.assertEqual(second["stem_600_window_adjacent"], STANDING_600_WINDOW_ADJACENT)
        self.assertEqual(
            [tuple(hit) for hit in second["stem_600_hits"]],
            list(STANDING_600_HITS),
        )
        self.assertEqual(second["run_040_count"], STANDING_040_RUN_COUNT)
        self.assertEqual(second["run_040_token_count"], STANDING_040_TOKEN_COUNT)
        self.assertEqual(second["run_040_lengths"], list(STANDING_040_RUN_LENGTHS))
        self.assertEqual(second["cell_count"], STANDING_CELL_COUNT)
        rejected = {item["id"] for item in self.survey["rejected"]}
        self.assertEqual(
            rejected,
            {
                "lunar_html",
                "ca0708_html",
                "fi_ca_html",
                "ca07_html",
                "svg_full_lines",
                "guy_1990_plates",
                "horley_2011",
                "cb_html",
            },
        )
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSecondPassageImageSnapshot(unittest.TestCase):
    """Cycle 28 does not touch clustering. 83/62 / Hamming 6 stays."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.published_lines = published_ca7_ca8_stems()

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. 83/62 / published Hamming 6 / 0/8."""
        published = self.published_lines
        window = score_delimiter_windows(self.instances, self.image_lines, published)
        published_ca7, published_ca8 = published_ca7_ca8_stem_counts()
        identity = score_type_identity(
            self.instances, self.analyzer, published_ca7, published_ca8
        )
        grams = tuple(w.image_ids for w in window.windows)
        self.assertEqual(window.instance_count, 83)
        self.assertEqual(window.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(identity.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(identity.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(min_pairwise_window_hamming(grams), STANDING_PUBLISHED_MIN_HAMMING)
        self.assertEqual(min_pairwise_window_hamming(grams), 6)
        self.assertEqual(window.slot_matches, STANDING_SLOT_MATCHES)
        unique_counts = tuple(len(set(ids)) for ids in window.slot_ids)
        self.assertEqual(unique_counts, STANDING_SLOT_UNIQUE_COUNTS)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
