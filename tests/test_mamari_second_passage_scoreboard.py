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
window-adjacent (no windows); 040-run and cell counts. Cycle 29 locks
the remainder n≥4 freq≥2 profile on this same fixture. Cycle 30
locks that 9-gram as a motif (hits, flanks, wrap-count,
calendar-absent). Image track stays parked. MockProvider only.
"""

import json
import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    barthel_stems,
    fixture_line_stems,
    load_mamari_fixture,
)

STEM_040 = "040"
STEM_600 = "600"
FIRST_DELIMITER_VARIANTS = ("315", "375")

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


def find_ngram_hits(sequences: list[list[str]], gram: tuple[str, ...]) -> list[tuple[int, int]]:
    """(line_index, start) for every occurrence of gram."""
    n = len(gram)
    hits: list[tuple[int, int]] = []
    for line_index, sequence in enumerate(sequences):
        for start in range(len(sequence) - n + 1):
            if tuple(sequence[start : start + n]) == gram:
                hits.append((line_index, start))
    return hits


def variant_motifs(
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    variants: tuple[str, ...] = FIRST_DELIMITER_VARIANTS,
) -> tuple[tuple[str, ...], ...]:
    """Guy motif with 315 or 375 in the 378 slot. Full 8, then short 4."""
    slot = motif.index("378")
    short_end = slot + 2
    rows: list[tuple[str, ...]] = []
    for variant in variants:
        rows.append(motif[:slot] + (variant,) + motif[slot + 1 :])
        rows.append(motif[:slot] + (variant,) + motif[slot + 1 : short_end])
    return tuple(rows)


def published_windows(
    lines: list[list[str]],
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    line_names: tuple[str, ...] = REMAINDER_LINE_NAMES,
) -> tuple[tuple[str, int, int], ...]:
    """Guy windows plus Ca6 315/375 variants. Search only."""
    starts: set[tuple[int, int]] = set()
    spans: list[tuple[str, int, int]] = []
    for line_index, start in find_ngram_hits(lines, motif):
        starts.add((line_index, start))
        spans.append((line_names[line_index], start, start + len(motif)))
    for gram in variant_motifs(motif):
        n = len(gram)
        for line_index, start in find_ngram_hits(lines, gram):
            if (line_index, start) in starts:
                continue
            starts.add((line_index, start))
            spans.append((line_names[line_index], start, start + n))
    spans.sort(key=lambda row: (line_names.index(row[0]), row[1], row[2]))
    return tuple(spans)


def cell_table(
    lines: list[list[str]],
    windows: tuple[tuple[str, int, int], ...],
    line_names: tuple[str, ...] = REMAINDER_LINE_NAMES,
) -> tuple[tuple[str, int, int, int], ...]:
    """Inter-window cells: (line, start, end, length). Empty edges kept."""
    cells: list[tuple[str, int, int, int]] = []
    for name, sequence in zip(line_names, lines):
        line_windows = [(start, end) for line, start, end in windows if line == name]
        starts = [0] + [end for _start, end in line_windows]
        ends = [start for start, _end in line_windows] + [len(sequence)]
        for start, end in zip(starts, ends):
            cells.append((name, start, end, end - start))
    return tuple(cells)


def run_040_table(
    lines: list[list[str]],
    windows: tuple[tuple[str, int, int], ...],
    stem: str = STEM_040,
    line_names: tuple[str, ...] = REMAINDER_LINE_NAMES,
) -> tuple[tuple[str, int, int, int, bool], ...]:
    """Maximal 040 runs: (line, start, end, length, precedes_window)."""
    runs: list[tuple[str, int, int, int, bool]] = []
    for name, sequence in zip(line_names, lines):
        index = 0
        n = len(sequence)
        while index < n:
            if sequence[index] != stem:
                index += 1
                continue
            start = index
            while index < n and sequence[index] == stem:
                index += 1
            precedes = any(
                line == name and w_start == index for line, w_start, _w_end in windows
            )
            runs.append((name, start, index, index - start, precedes))
    return tuple(runs)


def stem_hits(
    lines: list[list[str]],
    stem: str,
    line_names: tuple[str, ...] = REMAINDER_LINE_NAMES,
) -> tuple[tuple[str, int], ...]:
    """(line, index) for every stem hit."""
    return tuple(
        (line_names[line_index], start)
        for line_index, sequence in enumerate(lines)
        for start, token in enumerate(sequence)
        if token == stem
    )


def hit_is_window_adjacent(
    line: str,
    index: int,
    cells: tuple[tuple[str, int, int, int], ...],
    windows: tuple[tuple[str, int, int], ...],
) -> bool:
    """Last token facing a window, or first token of a cell after a window."""
    line_cells = [cell for cell in cells if cell[0] == line]
    for cell_index, (name, start, end, length) in enumerate(line_cells):
        if index < start or index >= end or length == 0:
            continue
        position = index - start
        follows_window = cell_index > 0
        faces_window = any(w_line == name and w_start == end for w_line, w_start, _w_end in windows)
        return (position == 0 and follows_window) or (
            position == length - 1 and faces_window
        )
    return False


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
        empty = ["001"]
        published = {
            "Ca1": empty,
            "Ca2": empty,
            "Ca3": empty,
            "Ca4": empty,
            "Ca5": empty,
            "Ca6": ["005", "600V", "390.041", "315y", "041"],
            "Ca7": ["040", "040"],
            "Ca8": ["280"],
            "Ca9": ["040", "040", "520", "070"],
            "Ca10": empty,
            "Ca11": empty,
            "Ca12": empty,
            "Ca13": empty,
            "Ca14": empty,
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

    def test_600_window_adjacent_needs_a_window(self):
        """First-after-window / last-facing-window; no window is not adjacent."""
        motif = DELIMITER_MOTIF
        lines = [["600"] + list(motif) + ["600", "040"], ["600"]]
        names = ("L0", "L1")
        windows = published_windows(lines, line_names=names)
        cells = cell_table(lines, windows, line_names=names)
        self.assertEqual(windows, (("L0", 1, 9),))
        self.assertTrue(hit_is_window_adjacent("L0", 0, cells, windows))
        self.assertTrue(hit_is_window_adjacent("L0", 9, cells, windows))
        self.assertFalse(hit_is_window_adjacent("L1", 0, cells, windows))
        empty = published_windows([["600", "040"]], line_names=("L0",))
        self.assertEqual(empty, ())
        self.assertFalse(
            hit_is_window_adjacent(
                "L0", 0, cell_table([["600", "040"]], empty, ("L0",)), empty
            )
        )


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
        self.windows = published_windows(self.lines)
        self.cells = cell_table(self.lines, self.windows)
        self.runs = run_040_table(self.lines, self.windows)

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
        self.assertEqual(self.windows, ())
        self.assertEqual(len(self.windows), STANDING_WINDOW_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_600_is_present_but_not_window_adjacent(self):
        """Five 600 hits; no window, so none are window-adjacent."""
        hits = stem_hits(self.lines, STEM_600)
        self.assertEqual(hits, STANDING_600_HITS)
        self.assertEqual(len(hits), STANDING_600_COUNT)
        adjacent = any(
            hit_is_window_adjacent(line, index, self.cells, self.windows)
            for line, index in hits
        )
        self.assertEqual(adjacent, STANDING_600_WINDOW_ADJACENT)
        self.assertFalse(adjacent)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_040_run_and_cell_counts(self):
        """Six length-1 040 runs on Ca10–Ca12; twelve windowless cells."""
        self.assertEqual(len(self.runs), STANDING_040_RUN_COUNT)
        self.assertEqual(self.runs, STANDING_040_RUNS)
        self.assertEqual(
            tuple(length for _line, _start, _end, length, _pre in self.runs),
            STANDING_040_RUN_LENGTHS,
        )
        self.assertEqual(
            sum(length for _line, _start, _end, length, _pre in self.runs),
            STANDING_040_TOKEN_COUNT,
        )
        self.assertTrue(all(not precedes for _line, _start, _end, _length, precedes in self.runs))
        self.assertEqual(len(self.cells), STANDING_CELL_COUNT)
        self.assertEqual(
            sum(1 for _line, _start, _end, length in self.cells if length == 0),
            STANDING_EMPTY_CELL_COUNT,
        )
        self.assertEqual(self.windows, ())
        self.assertEqual(
            tuple(length for _line, _start, _end, length in self.cells),
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
        image = self.survey["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
