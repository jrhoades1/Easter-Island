"""Tablet C side b: vendored Kohaumotu Cb.html search lock.

Cycle 32 text-search lock. Copies Barthel tokens from the already-used
Kohaumotu tablet-C source verso (Cb.html, navbar link from the cited
Ca.html). Digits come from that HTML. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.

Locks four Cb-only claims: Guy's 8-stem delimiter frequency and spans,
whether the remainder 9-gram motif appears, 002…002 n=9 wrap count and
how many share a non-bookend interior stem with the motif, and the 600
count. Bookend 002 is not a delimiter. Ca remainder / calendar locks
are unchanged. Cycle 33 locks this verso's n≥4 freq≥2 profile.

Search lock, not a merge and not a translation. MockProvider only.
"""

import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_calendar_scoreboard import DELIMITER_MOTIF
from tests.test_mamari_remainder_002_wrap_family_scoreboard import (
    family_tuple,
    score_wrap_family,
    wraps_sharing_interior,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import (
    MOTIF_9GRAM,
    WRAP_N,
    WRAP_STEM,
    score_002_wraps,
)
from tests.test_mamari_second_passage_scoreboard import (
    STEM_600,
    _LINE_HEADER,
    find_ngram_hits,
    load_corpus_survey,
    published_stems,
    stem_hits,
)

CB_HTML_DIR = Path(__file__).parent / "fixtures" / "mamari_cb_html"
CB_HTML_PATH = CB_HTML_DIR / "Cb.html"
CITED_CB_URL = "http://kohaumotu.org/Rongorongo/C/Cb.html"
CITED_CA_URL = "http://kohaumotu.org/Rongorongo/C/Ca.html"

CB_LINE_NAMES = tuple(f"Cb{n}" for n in range(1, 15))
STANDING_HTML_BYTES = 7877
STANDING_STEM_COUNTS = (39, 35, 38, 38, 34, 34, 32, 36, 37, 35, 34, 36, 36, 23)
STANDING_STEM_TOTAL = 487
STANDING_GUY_DELIMITER_PRESENT = False
STANDING_GUY_DELIMITER_FREQ = 0
STANDING_GUY_DELIMITER_SPANS = ()
STANDING_MOTIF_PRESENT = False
STANDING_MOTIF_HITS = ()
STANDING_600_COUNT = 2
STANDING_600_HITS = (("Cb2", 21), ("Cb10", 29))
# (tokens, line, start, end, is_motif, position_matches, shared_interior, shares)
STANDING_WRAP_FAMILY = (
    (
        ("002", "095", "066", "760", "004", "027", "066", "004", "002"),
        "Cb7",
        12,
        21,
        False,
        3,
        ("760",),
        True,
    ),
    (
        ("002", "004", "002", "070", "095", "001", "095", "205", "002"),
        "Cb8",
        17,
        26,
        False,
        2,
        ("070",),
        True,
    ),
    (
        ("002", "044", "660", "077", "000", "003", "077", "000", "002"),
        "Cb9",
        5,
        14,
        False,
        2,
        (),
        False,
    ),
    (
        ("002", "208", "546", "410", "095", "095", "095", "445", "002"),
        "Cb9",
        28,
        37,
        False,
        2,
        (),
        False,
    ),
)
STANDING_WRAP_COUNT = 4
STANDING_WRAPS_SHARING_INTERIOR = 2


def load_vendored_cb_html() -> str:
    """Return the vendored Kohaumotu Cb.html snapshot."""
    return CB_HTML_PATH.read_text(encoding="utf-8")


def extract_cb_published_tokens(html: str) -> dict[str, list[str]]:
    """Copy hyphen-separated Barthel tokens from Cb.html <td> text.

    Same mechanical copy as Ca.html. Does not invent numbers. Image
    cells are skipped.
    """
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"Cb{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def cb_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Cb1–Cb14 as stem sequences. Search only."""
    return [published_stems(published[name]) for name in CB_LINE_NAMES]


class TestCbSideBHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_extracts_hyphen_tokens_and_skips_image_cells(self):
        """Only digit-bearing <td> text is copied; lines are named CbN."""
        html = (
            '<h3><a name="Line_1">Line 1</a></h3>'
            "<table><tr><td><img src='x.png' /></td></tr>"
            "<tr><td>001-280-005-</td></tr></table>"
            '<h3><a name="Line_2">Line 2</a></h3>'
            "<table><tr><td>600.064-002*</td></tr></table>"
        )
        published = extract_cb_published_tokens(html)
        self.assertEqual(published["Cb1"], ["001", "280", "005"])
        self.assertEqual(published["Cb2"], ["600.064", "002*"])

    def test_colon_ligature_splits_like_ca(self):
        """':' is a published ligature mark, same as Ca.html."""
        self.assertEqual(published_stems(["095:042", "004.600"]), ["095", "042", "004", "600"])


class TestMamariCbSideBScoreboard(unittest.TestCase):
    """Cited Cb.html lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.html = load_vendored_cb_html()
        self.published = extract_cb_published_tokens(self.html)
        self.lines = cb_line_stems(self.published)
        self.wraps = score_002_wraps(self.lines, CB_LINE_NAMES)
        self.family = score_wrap_family(self.wraps)

    def test_vendored_html_is_the_cited_cb_page(self):
        """Snapshot is Kohaumotu Cb.html, verso of the cited Ca.html."""
        self.assertTrue(CB_HTML_PATH.is_file())
        self.assertTrue((CB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertEqual(CB_HTML_PATH.stat().st_size, STANDING_HTML_BYTES)
        self.assertIn("Item C:Mamari", self.html)
        self.assertIn("Side b", self.html)
        self.assertIn("Rongorongo Cb", self.html)
        self.assertIn("Ca.html", self.html)
        self.assertEqual(list(self.published), list(CB_LINE_NAMES))
        lock = self.survey["tablet_c_side_b"]
        self.assertEqual(lock["source_page"], CITED_CB_URL)
        self.assertEqual(lock["result"], "cb_html_vendored")
        attribution = (CB_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn(CITED_CB_URL, attribution)
        self.assertIn(CITED_CA_URL, attribution)
        self.assertIn("kohaumotu.org/rongorongo_org/copy.html", attribution)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_guys_8stem_delimiter_is_absent(self):
        """Guy 390 041 378 041 670 008 078 711 does not occur on Cb."""
        hits = find_ngram_hits(self.lines, DELIMITER_MOTIF)
        spans = tuple(
            (CB_LINE_NAMES[line_index], start, start + len(DELIMITER_MOTIF))
            for line_index, start in hits
        )
        self.assertEqual(len(hits), STANDING_GUY_DELIMITER_FREQ)
        self.assertEqual(spans, STANDING_GUY_DELIMITER_SPANS)
        self.assertEqual(bool(hits), STANDING_GUY_DELIMITER_PRESENT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_9gram_motif_is_absent(self):
        """Remainder motif 002 010 070 760 040 006 430 047 002 is absent."""
        hits = find_ngram_hits(self.lines, MOTIF_9GRAM)
        self.assertEqual(hits, [])
        self.assertEqual(bool(hits), STANDING_MOTIF_PRESENT)
        self.assertEqual(STANDING_MOTIF_HITS, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_002_wraps_and_interior_overlap(self):
        """Four 002…002 n=9 wraps; two share a motif interior stem."""
        locked = tuple(family_tuple(row) for row in self.family)
        self.assertEqual(len(self.wraps), STANDING_WRAP_COUNT)
        self.assertEqual(len(locked), STANDING_WRAP_COUNT)
        self.assertEqual(locked, STANDING_WRAP_FAMILY)
        self.assertEqual(
            wraps_sharing_interior(self.family),
            STANDING_WRAPS_SHARING_INTERIOR,
        )
        self.assertTrue(
            all(row[0][0] == WRAP_STEM and row[0][-1] == WRAP_STEM for row in locked)
        )
        self.assertTrue(all(len(row[0]) == WRAP_N for row in locked))
        self.assertTrue(all(not row[4] for row in locked))
        sharing = tuple(row for row in self.family if row.shares_interior_stem)
        self.assertEqual(len(sharing), STANDING_WRAPS_SHARING_INTERIOR)
        self.assertEqual(
            tuple(row.shared_interior_stems for row in sharing),
            (("760",), ("070",)),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_600_count(self):
        """Two 600 hits: Cb2[21] and Cb10[29]."""
        hits = stem_hits(self.lines, STEM_600, line_names=CB_LINE_NAMES)
        self.assertEqual(hits, STANDING_600_HITS)
        self.assertEqual(len(hits), STANDING_600_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-32 Cb lock."""
        lock = self.survey["tablet_c_side_b"]
        self.assertEqual(lock["cycle"], 32)
        self.assertEqual(lock["html_bytes"], STANDING_HTML_BYTES)
        self.assertEqual(lock["lines"], list(CB_LINE_NAMES))
        self.assertEqual(lock["stem_count"], STANDING_STEM_TOTAL)
        self.assertEqual(lock["stem_counts_by_line"], list(STANDING_STEM_COUNTS))
        self.assertEqual(
            [len(line) for line in self.lines],
            list(STANDING_STEM_COUNTS),
        )
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_STEM_TOTAL)
        self.assertEqual(lock["guy_8stem_delimiter"], STANDING_GUY_DELIMITER_PRESENT)
        self.assertEqual(lock["guy_8stem_delimiter_freq"], STANDING_GUY_DELIMITER_FREQ)
        self.assertEqual(lock["guy_8stem_delimiter_spans"], [])
        self.assertEqual(lock["motif_9gram"], STANDING_MOTIF_PRESENT)
        self.assertEqual(lock["motif_9gram_freq"], 0)
        self.assertEqual(lock["motif_9gram_spans"], [])
        self.assertEqual(lock["wrap_n"], WRAP_N)
        self.assertEqual(lock["bookend_stem"], WRAP_STEM)
        self.assertEqual(lock["wrap_count"], STANDING_WRAP_COUNT)
        self.assertEqual(
            [
                (
                    tuple(tokens),
                    line,
                    start,
                    end,
                    is_motif,
                    position_matches,
                    tuple(shared),
                    shares,
                )
                for tokens, line, start, end, is_motif, position_matches, shared, shares
                in lock["wraps"]
            ],
            list(STANDING_WRAP_FAMILY),
        )
        self.assertEqual(
            lock["wraps_sharing_interior_stem"],
            STANDING_WRAPS_SHARING_INTERIOR,
        )
        self.assertEqual(lock["stem_600_count"], STANDING_600_COUNT)
        self.assertEqual(
            [tuple(hit) for hit in lock["stem_600_hits"]],
            list(STANDING_600_HITS),
        )
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCbSideBImageSnapshot(unittest.TestCase):
    """Cycle 32 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
