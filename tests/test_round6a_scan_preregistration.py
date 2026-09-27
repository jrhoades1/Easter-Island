"""Round 6A locks the headline counts before any higher-resolution image is used.

Alternatives are the codes already named in Round 5B, Round 3, and the
allograph notes. MockProvider is never called. No reading is assigned.
"""

from __future__ import annotations

import contextlib
import json
import tempfile
import unittest
from io import StringIO
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round5b_ceipp import build_report
from decipherment.round6a_preregistration import (
    DISAGREEMENTS,
    INSCRIBE_TABLETS,
    OUTPUT_PATH,
    build_preregistration,
    detach_suffix_076,
    headline_stats,
    normalize_choices,
    recompute,
)
from decipherment.track3_genealogy import group_stems

DOC_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "decipherment"
    / "round6a_scan_preregistration.md"
)

LOCKED_BASELINE = {
    "calendar_040": 28,
    "calendar_040_before_152": 13,
    "calendar_040_after_152": 13,
    "calendar_040_gaps": [2, 6, 3, 2, 5, 3, 5],
    "calendar_full_delimiters": 6,
    "calendar_152": 1,
    "calendar_143": 1,
    "gv6_phrases": 4,
    "gv6_handoffs": 3,
    "staff_076_after_999": 91,
    "staff_pure_999": 96,
    "staff_076_after_999_rate": 91 / 96,
    "parallel_span": 125,
    "parallel_matches": 107,
    "parallel_mismatches": 16,
    "parallel_bird_substitutions": 2,
    "corpus_bird_substitutions": 18,
}


class TestRound6aScanPreregistration(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = MockProvider()
        self.report = build_preregistration(self.provider)

    def test_provider_is_unused_and_no_reading_is_assigned(self) -> None:
        self.assertEqual(self.provider.get_call_history(), [])
        self.assertEqual(self.report["provider_calls"], 0)
        self.assertFalse(self.report["readings_assigned"])
        self.assertIsNone(self.report["reading"])
        self.assertFalse(self.report["images_fetched"])
        self.assertFalse(self.report["transcription_updated"])

    def test_baseline_matches_the_locked_headline_and_round_5b(self) -> None:
        self.assertEqual(self.report["baseline"], LOCKED_BASELINE)
        fresh = headline_stats(normalize_choices({}))
        self.assertEqual(fresh, LOCKED_BASELINE)
        round5b = build_report(MockProvider())
        self.assertEqual(round5b["stats_before"], LOCKED_BASELINE)
        self.assertEqual(round5b["stats_after"], LOCKED_BASELINE)

    def test_saved_record_matches_the_builder(self) -> None:
        saved = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(saved, self.report)
        self.assertEqual(len(saved["disagreements"]), 12)

    def test_inscribe_coverage_is_mamari_only(self) -> None:
        self.assertEqual(list(INSCRIBE_TABLETS), ["A", "B", "C", "D", "M", "N"])
        self.assertEqual(
            self.report["disagreement_ids_on_inscribe_tablets"],
            ["D01", "D02", "D03", "D04"],
        )
        self.assertEqual(
            self.report["disagreement_ids_outside_inscribe"],
            ["D05", "D06", "D07", "D08", "D09", "D10", "D11", "D12"],
        )
        self.assertEqual(
            self.report["inscribe"]["tablets_with_a_model_and_no_logged_disagreement"],
            ["A", "B", "D", "M", "N"],
        )
        for row in self.report["disagreements"]:
            covered = set(row["tablets"]).issubset(set(INSCRIBE_TABLETS))
            self.assertEqual(row["inscribe_covered"], covered)

    def test_every_single_choice_keeps_the_crescent_split_and_the_staff_rate(self) -> None:
        for row in self.report["disagreements"]:
            for alternative in row["alternatives"]:
                after = alternative["headline_after"]
                self.assertEqual(after["calendar_040"], 28)
                self.assertEqual(after["calendar_040_before_152"], 13)
                self.assertEqual(after["calendar_040_after_152"], 13)
                self.assertEqual(after["calendar_152"], 1)
                self.assertEqual(after["calendar_143"], 1)
                self.assertEqual(after["staff_076_after_999"], 91)
                self.assertEqual(after["staff_pure_999"], 96)
                self.assertEqual(after["staff_076_after_999_rate"], 91 / 96)
                self.assertEqual(after["parallel_span"], 125)
                self.assertEqual(self.provider.get_call_history(), [])

    def test_guy_star690_joins_two_delimiter_gaps(self) -> None:
        alternative = self._alternative("D01", "guy_1990_star690")
        self.assertEqual(
            alternative["headline_delta"],
            {
                "calendar_040_gaps": {
                    "before": [2, 6, 3, 2, 5, 3, 5],
                    "after": [2, 6, 3, 7, 3, 5],
                },
                "calendar_full_delimiters": {"before": 6, "after": 5, "by": -1},
            },
        )
        self.assertEqual(self._alternative("D02", "guy_1990_078_040")["headline_delta"], {})
        paired = self._combination("D01 and D02 together")
        self.assertEqual(paired["headline_delta"], alternative["headline_delta"])

    def test_parallel_choices_move_only_the_logged_columns(self) -> None:
        hand = self._alternative("D05", "ceipp_outline_006")
        self.assertEqual(hand["headline_delta"]["parallel_matches"], {"before": 107, "after": 106, "by": -1})
        self.assertEqual(hand["headline_delta"]["parallel_mismatches"], {"before": 16, "after": 17, "by": 1})
        self.assertEqual(hand["other_passage_match_changes"][0]["id"], "P007")
        self.assertEqual(hand["other_passage_match_changes"][0]["by"], -1)

        one_side = self._alternative("D06", "ceipp_vector_042_then_006")
        self.assertEqual(one_side["headline_delta"]["parallel_matches"]["after"], 105)
        other_side = self._alternative("D07", "ceipp_vector_042_then_006")
        self.assertEqual(other_side["headline_delta"]["parallel_matches"]["after"], 105)
        both = self._combination("D06 and D07 together")
        self.assertEqual(both["headline_delta"], {})

        birds = self._alternative("D08", "pozdniakov_1996_series_400_as_600")
        self.assertEqual(birds["headline_delta"]["parallel_matches"]["after"], 109)
        self.assertEqual(birds["headline_delta"]["parallel_bird_substitutions"], {"before": 2, "after": 0, "by": -2})
        self.assertEqual(birds["headline_delta"]["corpus_bird_substitutions"], {"before": 18, "after": 16, "by": -2})

        stacked = self._combination("D05, D06, and D08 together")
        self.assertEqual(stacked["headline_delta"]["parallel_matches"]["after"], 106)
        self.assertEqual(stacked["headline_delta"]["corpus_bird_substitutions"]["after"], 16)

    def test_gv6_regrouping_removes_the_handoffs_and_keeps_the_six_signs(self) -> None:
        from decipherment.round6a_preregistration import _gv6_groups

        raw = list(_gv6_groups())
        moved = detach_suffix_076(raw)
        raw_count = sum(group_stems(group).count("076") for group in raw)
        moved_count = sum(group_stems(group).count("076") for group in moved)
        self.assertEqual(raw_count, 6)
        self.assertEqual(moved_count, 6)
        alternative = self._alternative("D09", "davletshin_2012_076_opens_next_group")
        self.assertEqual(alternative["headline_delta"]["gv6_phrases"], {"before": 4, "after": 0, "by": -4})
        self.assertEqual(alternative["headline_delta"]["gv6_handoffs"], {"before": 3, "after": 0, "by": -3})

    def test_hr4_label_is_outside_the_headline_span(self) -> None:
        alternative = self._alternative("D12", "ceipp_outline_048")
        self.assertEqual(alternative["headline_delta"], {})
        change = alternative["other_passage_match_changes"]
        self.assertEqual(len(change), 1)
        self.assertEqual(change[0]["id"], "P015")
        self.assertEqual(change[0]["matches_before"], 30)
        self.assertEqual(change[0]["matches_after"], 31)
        self.assertFalse(change[0]["headline"])

    def test_rows_without_a_second_code_have_only_the_baseline(self) -> None:
        for disagreement_id in ("D03", "D04", "D10", "D11"):
            row = self._row(disagreement_id)
            self.assertEqual(len(row["alternatives"]), 1)
            self.assertTrue(row["alternatives"][0]["baseline"])
            self.assertEqual(row["alternatives"][0]["headline_delta"], {})
            self.assertTrue(row["no_other_code"])

    def test_every_alternative_cites_a_source(self) -> None:
        for row in DISAGREEMENTS:
            for alternative in row["alternatives"]:
                self.assertTrue(alternative["sources"])
                for source in alternative["sources"]:
                    self.assertTrue(source["name"])
                    self.assertTrue(source["detail"])

    def test_inscribe_evidence_accepts_mamari_and_rejects_the_other_tablets(self) -> None:
        accepted = recompute(
            {
                "provider": "MockProvider",
                "evidence": "inscribe",
                "choices": {"D01": "guy_1990_star690", "D02": "barthel_044_040"},
            },
            self.provider,
        )
        self.assertEqual(accepted["headline"]["calendar_040_gaps"], [2, 6, 3, 7, 3, 5])
        self.assertEqual(accepted["headline"]["calendar_040"], 28)
        self.assertFalse(accepted["transcription_updated"])
        self.assertFalse(accepted["images_fetched"])
        self.assertIsNone(accepted["reading"])
        for disagreement_id, choice in (
            ("D05", "ceipp_outline_006"),
            ("D08", "pozdniakov_1996_series_400_as_600"),
            ("D09", "davletshin_2012_076_opens_next_group"),
            ("D12", "ceipp_outline_048"),
        ):
            with self.assertRaises(ValueError):
                recompute(
                    {
                        "provider": "MockProvider",
                        "evidence": "inscribe",
                        "choices": {disagreement_id: choice},
                    },
                    self.provider,
                )

    def test_unknown_choices_and_loose_evidence_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            recompute(
                {"provider": "MockProvider", "evidence": "inscribe", "choices": {"D01": "690"}},
                self.provider,
            )
        with self.assertRaises(ValueError):
            recompute(
                {"provider": "MockProvider", "evidence": "counterfactual", "choices": {"D99": "barthel_041"}},
                self.provider,
            )
        with self.assertRaises(ValueError):
            recompute(
                {
                    "provider": "MockProvider",
                    "evidence": "later_image",
                    "choices": {"D05": "ceipp_outline_006"},
                },
                self.provider,
            )
        with self.assertRaises(ValueError):
            recompute(
                {
                    "provider": "MockProvider",
                    "evidence": "counterfactual",
                    "image_note": "a mesh",
                    "choices": {},
                },
                self.provider,
            )
        with self.assertRaises(TypeError):
            recompute({"provider": "MockProvider", "evidence": "counterfactual"}, provider=object())  # type: ignore[arg-type]

    def test_command_line_recomputes_a_verdict_file(self) -> None:
        from decipherment.round6a_preregistration import main

        verdict = {
            "provider": "MockProvider",
            "evidence": "counterfactual",
            "choices": {"D08": "pozdniakov_1996_series_400_as_600"},
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "verdict.json"
            path.write_text(json.dumps(verdict), encoding="utf-8")
            buffer = StringIO()
            with contextlib.redirect_stdout(buffer):
                status = main(["--verdict", str(path)])
            self.assertEqual(status, 0)
        payload = json.loads(buffer.getvalue())
        self.assertEqual(payload["headline"]["corpus_bird_substitutions"], 16)
        self.assertEqual(payload["headline"]["parallel_bird_substitutions"], 0)
        self.assertEqual(payload["provider_calls"], 0)
        self.assertIsNone(payload["reading"])

    def test_protocol_page_records_the_same_movements(self) -> None:
        doc = DOC_PATH.read_text(encoding="utf-8")
        self.assertIn("MockProvider", doc)
        self.assertIn("reading", doc)
        self.assertIn("2, 6, 3, 7, 3, 5", doc)
        self.assertIn("91 of 96", doc)
        self.assertIn("13 / 13", doc)
        for disagreement_id in (row["id"] for row in DISAGREEMENTS):
            self.assertIn(disagreement_id, doc)
        self.assertIn("A", doc)
        self.assertIn("Mamari", doc)
        self.assertIn("*690", doc)
        self.assertIn("078.040", doc)
        self.assertIn("Pozdniakov 1996", doc)
        self.assertIn("Davletshin 2012", doc)
        self.assertEqual(self.provider.get_call_history(), [])

    def _row(self, disagreement_id: str) -> dict:
        for row in self.report["disagreements"]:
            if row["id"] == disagreement_id:
                return row
        raise KeyError(disagreement_id)

    def _alternative(self, disagreement_id: str, alternative_id: str) -> dict:
        for alternative in self._row(disagreement_id)["alternatives"]:
            if alternative["id"] == alternative_id:
                return alternative
        raise KeyError(alternative_id)

    def _combination(self, label: str) -> dict:
        for row in self.report["checked_combinations"]:
            if row["label"] == label:
                return row
        raise KeyError(label)


if __name__ == "__main__":
    unittest.main()
