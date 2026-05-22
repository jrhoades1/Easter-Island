"""Tests for the transliterated-corpus models, loader, and statistics."""

import os
import sys
import unittest

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.corpus import CorpusLine, RongorongoCorpus, Tablet
from processors.corpus_loader import CorpusFormatError, parse_rrt
from processors.corpus_statistics import CorpusStatistics


class TestCorpusModels(unittest.TestCase):
    """Tests for the corpus data models."""

    def test_line_glyphs_decomposes_ligatures(self):
        """A ligature token should split into its component glyphs."""
        line = CorpusLine(line_id="Ca1", tokens=["1", "6-700", "8"])
        self.assertEqual(line.glyphs(), ["1", "6", "700", "8"])

    def test_line_length_counts_written_tokens(self):
        """Line length counts as-written tokens, not decomposed glyphs."""
        line = CorpusLine(line_id="Ca1", tokens=["1", "6-700", "8"])
        self.assertEqual(line.length, 3)

    def test_tablet_glyph_and_token_aggregation(self):
        """Tablet aggregates glyphs (decomposed) and tokens (as written)."""
        tablet = Tablet(
            tablet_id="C",
            lines=[
                CorpusLine("Ca1", ["1", "2"]),
                CorpusLine("Ca2", ["6-700"]),
            ],
        )
        self.assertEqual(tablet.total_tokens, 3)
        self.assertEqual(tablet.all_glyphs(), ["1", "2", "6", "700"])

    def test_corpus_round_trip_serialization(self):
        """A corpus should survive a to_dict/from_dict round trip."""
        corpus = RongorongoCorpus(
            tablets=[
                Tablet(
                    tablet_id="C",
                    name="Mamari",
                    is_synthetic=True,
                    lines=[CorpusLine("Ca1", ["1", "6-700"])],
                )
            ]
        )
        restored = RongorongoCorpus.from_dict(corpus.to_dict())
        self.assertEqual(restored.tablets[0].name, "Mamari")
        self.assertTrue(restored.has_synthetic)
        self.assertEqual(restored.tablets[0].lines[0].tokens, ["1", "6-700"])


class TestCorpusLoader(unittest.TestCase):
    """Tests for the .rrt transliteration parser."""

    SAMPLE = """
# a comment
@tablet C
@name Mamari
@side recto
Ca1: 1 2 6 700
Ca2: 6-700 8
"""

    def test_parse_basic(self):
        """Parsing should produce a tablet with metadata and lines."""
        tablets = parse_rrt(self.SAMPLE)
        self.assertEqual(len(tablets), 1)
        tablet = tablets[0]
        self.assertEqual(tablet.tablet_id, "C")
        self.assertEqual(tablet.name, "Mamari")
        self.assertEqual(tablet.side, "recto")
        self.assertEqual(len(tablet.lines), 2)
        self.assertEqual(tablet.lines[0].tokens, ["1", "2", "6", "700"])

    def test_synthetic_directive(self):
        """The @synthetic directive should flag the tablet."""
        tablets = parse_rrt("@tablet X\n@synthetic\nXa1: 1 2\n")
        self.assertTrue(tablets[0].is_synthetic)

    def test_lines_before_tablet_use_default_id(self):
        """A line before any @tablet attaches to the default tablet id."""
        tablets = parse_rrt("Xa1: 1 2 3\n", default_tablet_id="stem")
        self.assertEqual(tablets[0].tablet_id, "stem")

    def test_unknown_directive_raises(self):
        """An unknown @directive should raise a format error."""
        with self.assertRaises(CorpusFormatError):
            parse_rrt("@bogus value\n")

    def test_malformed_line_raises(self):
        """A non-comment line without a colon should raise."""
        with self.assertRaises(CorpusFormatError):
            parse_rrt("this line has no colon\n")


class TestCorpusStatistics(unittest.TestCase):
    """Tests for the descriptive statistics engine."""

    def _corpus(self) -> RongorongoCorpus:
        return RongorongoCorpus(
            tablets=[
                Tablet(
                    tablet_id="T",
                    is_synthetic=True,
                    lines=[
                        CorpusLine("Ta1", ["1", "2", "3", "1", "2", "3"]),
                        CorpusLine("Ta2", ["1", "2", "3", "9"]),
                        CorpusLine("Ta3", ["1", "6-700"]),
                    ],
                )
            ]
        )

    def test_frequency_table_ranks_by_count(self):
        """The frequency table should be ordered by descending count."""
        report = CorpusStatistics().analyze(self._corpus())
        top = report.frequency_table[0]
        self.assertEqual(top.glyph, "1")
        self.assertEqual(top.count, 4)
        self.assertEqual(top.rank, 1)

    def test_ligature_decomposed_in_glyph_counts(self):
        """A ligature token contributes to each component glyph's count."""
        report = CorpusStatistics().analyze(self._corpus())
        counts = {e.glyph: e.count for e in report.frequency_table}
        self.assertEqual(counts["6"], 1)
        self.assertEqual(counts["700"], 1)
        self.assertEqual(report.ligature_token_count, 1)

    def test_hapax_detection(self):
        """Glyphs occurring exactly once should be counted as hapax."""
        report = CorpusStatistics().analyze(self._corpus())
        self.assertIn("9", report.hapax_glyphs)
        self.assertIn("6", report.hapax_glyphs)
        self.assertEqual(report.hapax_count, len(report.hapax_glyphs))

    def test_repeated_sequence_detection(self):
        """A sequence repeated within the corpus should be reported."""
        report = CorpusStatistics().analyze(self._corpus())
        found = [tuple(r.sequence) for r in report.repeated_sequences]
        self.assertIn(("1", "2", "3"), found)

    def test_synthetic_flag_propagates(self):
        """A synthetic corpus should produce a synthetic-flagged report."""
        report = CorpusStatistics().analyze(self._corpus())
        self.assertTrue(report.is_synthetic)

    def test_report_serialization(self):
        """The report should serialize to a JSON-compatible dict."""
        report = CorpusStatistics().analyze(self._corpus())
        data = report.to_dict()
        self.assertEqual(data["tablet_count"], 1)
        self.assertIn("frequency_table", data)
        self.assertIsInstance(data["ngrams"], dict)

    def test_empty_corpus_does_not_crash(self):
        """Analyzing an empty corpus should yield zeroed statistics."""
        report = CorpusStatistics().analyze(RongorongoCorpus())
        self.assertEqual(report.total_glyphs, 0)
        self.assertEqual(report.type_token_ratio, 0.0)


if __name__ == "__main__":
    unittest.main()
