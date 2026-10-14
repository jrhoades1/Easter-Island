"""Retest harness: transcription files in, headline tests out.

The baseline file must reproduce the recorded counts exactly, nulls
included. A synthetic Pozdniakov 400 -> 600 merge must move the counts
the way the stored alignments predict. MockProvider only; no network.
"""

from __future__ import annotations

import contextlib
import csv
import io
import tempfile
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment import retest
from decipherment.round5b_ceipp import _bird_pair
from decipherment.round6a_preregistration import headline_stats, normalize_choices
from decipherment.track3_genealogy import group_stems
from decipherment.transcription import (
    BASELINE_CSV,
    FIELDS,
    TranscriptionError,
    barthel_corpus,
    read_csv,
    write_csv,
)

DOCUMENTED = {
    ("calendar_040", "calendar_040"): 28,
    ("calendar_040", "calendar_040_before_152"): 13,
    ("calendar_040", "calendar_040_after_152"): 13,
    ("calendar_040", "calendar_stems"): 101,
    ("calendar_040", "calendar_143"): 1,
    ("calendar_040", "kokore_runs_6_before_5_after"): True,
    ("gv6_handoff", "gv6_phrases"): 4,
    ("gv6_handoff", "gv6_handoffs"): 3,
    ("gv6_handoff", "gv6_groups"): 28,
    ("staff_bar_076", "staff_076_after_999"): 91,
    ("staff_bar_076", "staff_pure_999"): 96,
    ("staff_076_gaps", "staff_076"): 564,
    ("staff_076_gaps", "staff_076_gaps"): 550,
    ("staff_076_gaps", "staff_076_gap_len3"): 197,
    ("staff_076_gaps", "staff_076_gap_len4"): 137,
    ("group_final_076", "staff_final_076"): 393,
    ("group_final_076", "staff_eligible_groups"): 408,
    ("group_final_076", "other_final_076"): 97,
    ("group_final_076", "other_eligible_groups"): 105,
    ("parallels", "significant_passages"): 99,
    ("parallels", "systematic_substitution_pairs"): 8,
    ("parallels", "pair_400_600"): 9,
    ("hq_headline", "parallel_span"): 125,
    ("hq_headline", "parallel_matches"): 107,
    ("hq_headline", "parallel_mismatches"): 16,
    ("bird_swaps", "cross_hundred_same_class"): 18,
    ("bird_swaps", "cross_hundred_classified"): 34,
    ("bird_swaps", "corpus_bird_substitutions_fixed_alignment"): 18,
}

DOCUMENTED_NULLS = {
    ("calendar_040", "kokore_shuffle"): (0, 5000),
    ("gv6_handoff", "gv6_group_shuffle"): (0, 5000),
    ("gv6_handoff", "gv_verso_shuffle"): (0, 2000),
    ("staff_bar_076", "staff_keep_bars_shuffle"): (0, 2000),
    ("staff_076_gaps", "staff_line_shuffle_len3"): (0, 1000),
    ("group_final_076", "staff_random_slot"): (0, 500),
    ("group_final_076", "other_random_slot"): (0, 500),
    ("bird_swaps", "class_label_shuffle"): (23, 500),
}


class TestTranscriptionFormat(unittest.TestCase):
    def test_baseline_file_round_trips(self):
        self.assertEqual(read_csv(BASELINE_CSV).lines, barthel_corpus().lines)

    def test_committed_file_matches_converter(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.csv"
            write_csv(barthel_corpus(), path)
            self.assertEqual(path.read_bytes(), BASELINE_CSV.read_bytes())

    def test_file_without_raw_column_keeps_every_stem(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bare.csv"
            with BASELINE_CSV.open(encoding="utf-8") as src, path.open("w", encoding="utf-8", newline="") as dst:
                reader = csv.DictReader(src)
                fields = [name for name in FIELDS if name != "raw"]
                writer = csv.DictWriter(dst, fieldnames=fields, extrasaction="ignore")
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)
            bare = read_csv(path).line_map()
        for name, groups in barthel_corpus().line_map().items():
            self.assertEqual(
                [group_stems(g) for g in bare[name]], [group_stems(g) for g in groups], name
            )

    def test_bad_rows_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.csv"
            path.write_text("tablet,side,line,position,sign\nA,Aa,1,0,04x\n", encoding="utf-8")
            with self.assertRaises(TranscriptionError):
                read_csv(path)
            path.write_text("tablet,side,line,position,sign\nA,Aa,1,1,040\n", encoding="utf-8")
            with self.assertRaises(TranscriptionError):
                read_csv(path)
            path.write_text("tablet,side,line,sign\nA,Aa,1,040\n", encoding="utf-8")
            with self.assertRaises(TranscriptionError):
                read_csv(path)


class TestBaselineReproduces(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.provider = MockProvider()
        cls.result = retest.run_tests(read_csv(BASELINE_CSV), provider=cls.provider)
        cls.baseline = retest.load_baseline()

    def test_provider_not_called(self):
        self.assertEqual(self.provider.get_call_history(), [])
        self.assertEqual(self.result["provider_calls"], 0)

    def test_matches_stored_baseline_exactly(self):
        for test_id, row in self.result["tests"].items():
            stored = self.baseline["tests"][test_id]
            self.assertEqual(row["values"], stored["values"], test_id)
            self.assertEqual(row["nulls"], stored["nulls"], test_id)

    def test_matches_documented_counts(self):
        for (test_id, key), expected in DOCUMENTED.items():
            self.assertEqual(self.result["tests"][test_id]["values"][key], expected, (test_id, key))
        for (test_id, key), (ge, trials) in DOCUMENTED_NULLS.items():
            null = self.result["tests"][test_id]["nulls"][key]
            self.assertEqual((null["ge"], null["trials"]), (ge, trials), (test_id, key))
        self.assertEqual(
            self.result["tests"]["calendar_delimiters"]["values"]["calendar_040_gaps"], [2, 6, 3, 2, 5, 3, 5]
        )

    def test_matches_round6a_headline_bundle(self):
        bundle = headline_stats(normalize_choices({}))
        mine = {}
        for row in self.result["tests"].values():
            mine.update(row["values"])
        for key in (
            "calendar_040", "calendar_040_before_152", "calendar_040_after_152", "calendar_040_gaps",
            "calendar_full_delimiters", "calendar_152", "calendar_143", "gv6_phrases", "gv6_handoffs",
            "staff_076_after_999", "staff_pure_999", "parallel_span", "parallel_matches",
            "parallel_mismatches", "parallel_bird_substitutions",
        ):
            self.assertEqual(mine[key], bundle[key], key)
        self.assertEqual(mine["corpus_bird_substitutions_fixed_alignment"], bundle["corpus_bird_substitutions"])

    def test_every_finding_holds_unchanged(self):
        rows = retest.compare(self.result, self.baseline)
        self.assertEqual({row["status"] for row in rows}, {retest.STATUS_SAME})
        self.assertEqual(len(rows), len(retest.TESTS))


class TestPozdniakovMerge(unittest.TestCase):
    """Every 400 rewritten as 600 (Pozdniakov's bird-head merge), corpus-wide."""

    @classmethod
    def setUpClass(cls):
        cls.base = retest.load_baseline()
        cls.corpus = read_csv(BASELINE_CSV).map_signs({"400": "600"})
        cls.result = retest.run_tests(cls.corpus, nulls=False)
        cls.rows = {row["id"]: row for row in retest.compare(cls.result, cls.base)}

    def values(self, test_id):
        return self.result["tests"][test_id]["values"]

    def test_no_400_remains(self):
        stems = [s for _side, _n, groups in self.corpus.lines for g in groups for s in group_stems(g)]
        self.assertNotIn("400", stems)
        self.assertEqual(stems.count("600"), 342 + 81)

    def test_calendar_gv6_and_staff_do_not_move(self):
        for test_id in ("calendar_040", "calendar_delimiters", "gv6_handoff", "staff_bar_076", "staff_076_gaps", "group_final_076"):
            self.assertEqual(self.values(test_id), self.base["tests"][test_id]["values"], test_id)

    def test_hq_gains_the_400_600_columns(self):
        headline = next(p for p in retest._stored_passages() if p["id"] == retest.HEADLINE_PASSAGE_ID)
        swapped = sum(1 for left, right in headline["columns"] if {left, right} == {"400", "600"})
        self.assertEqual(swapped, 1)
        self.assertEqual(self.values("hq_headline")["parallel_matches"], 107 + swapped)
        self.assertEqual(self.values("hq_headline")["parallel_mismatches"], 16 - swapped)
        self.assertEqual(self.rows["hq_headline"]["status"], retest.STATUS_CHANGED)

    def test_fixed_alignment_birds_follow_the_merge(self):
        """On the stored alignment, 400 columns opposite a 6xx sign stop counting,
        and 401/405 opposite a former 400 become cross-hundred bird pairs."""
        def merged(sign):
            return "600" if sign == "400" else sign

        lost = gained = after = 0
        for passage in retest._stored_passages():
            for left, right in passage["columns"]:
                before = _bird_pair(left, right)
                now = _bird_pair(merged(left), merged(right))
                lost += before and not now
                gained += now and not before
                after += now
        self.assertEqual((lost, gained), (13, 2))
        self.assertEqual(after, 18 - 13 + 2)
        self.assertEqual(self.values("bird_swaps")["corpus_bird_substitutions_fixed_alignment"], after)

    def test_parallel_search_loses_the_400_600_pair(self):
        values = self.values("parallels")
        self.assertEqual(values["pair_400_600"], 0)
        self.assertEqual(values["systematic_substitution_pairs"], 7)
        self.assertNotIn("400-600x9", values["systematic_pairs"])
        self.assertLess(self.values("bird_swaps")["cross_hundred_same_class"], 18)


class TestPartialCorpus(unittest.TestCase):
    def test_a_m_n_only(self):
        corpus = read_csv(BASELINE_CSV).restrict("AMN")
        self.assertEqual(corpus.tablets, ("A", "M", "N"))
        result = retest.run_tests(corpus, nulls=False)
        rows = {row["id"]: row for row in retest.compare(result, retest.load_baseline())}
        for test_id in ("calendar_040", "calendar_delimiters", "gv6_handoff", "staff_bar_076",
                        "staff_076_gaps", "parallels", "hq_headline", "bird_swaps"):
            self.assertEqual(rows[test_id]["status"], retest.STATUS_NA, test_id)
            self.assertTrue(rows[test_id]["reason"])
        self.assertTrue(rows["group_final_076"]["status"].endswith("(partial corpus)"))
        markdown = retest.render_markdown(result, list(rows.values()))
        self.assertIn("not computable", markdown)

    def test_cli_writes_table(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "c.csv"
            write_csv(read_csv(BASELINE_CSV).restrict("C"), path)
            out = Path(tmp) / "out"
            with contextlib.redirect_stdout(io.StringIO()):
                code = retest.main(["--transcription", str(path), "--out-dir", str(out), "--no-nulls"])
            self.assertEqual(code, 0)
            table = (out / "comparison.md").read_text(encoding="utf-8")
            self.assertIn("holds (same)", table)
            self.assertTrue((out / "results.json").exists())


if __name__ == "__main__":
    unittest.main()
