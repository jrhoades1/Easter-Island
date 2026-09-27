"""Round 4 Track E: published sound values, pre-registered, MockProvider only.

No reading is adopted. Counts are recomputed from the vendored corpus.
"""

from __future__ import annotations

import unittest

from agents.base.providers import MockProvider
from decipherment.old_rapanui import cv_syllables_mapped
from decipherment.round4_tracke import (
    DOC_PATH,
    JSON_PATH,
    PROTOCOL,
    proposal_sets,
    render_json,
    render_markdown,
    run_round4_tracke,
    tangata_hypothesis,
)


class GuardProvider(MockProvider):
    def __init__(self) -> None:
        super().__init__()
        self.calls = 0

    def complete(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        self.calls += 1
        raise AssertionError("MockProvider must not be called")


class TestRound4TrackE(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.provider = GuardProvider()
        cls.result = run_round4_tracke(cls.provider)

    def test_provider_is_unused_and_nothing_is_adopted(self) -> None:
        self.assertEqual(self.provider.calls, 0)
        self.assertEqual(self.result["provider"], "MockProvider")
        self.assertEqual(self.result["provider_calls"], 0)
        self.assertIsNone(self.result["reading"])
        self.assertEqual(self.result["adopted"], [])
        self.assertTrue(PROTOCOL["fixed_before_scores"])

    def test_empty_sets_were_not_filled_in(self) -> None:
        skipped = {row["set_id"] for row in self.result["not_scored"]}
        self.assertEqual(
            skipped,
            {
                "davletshin_2022_cross_readings",
                "pozdniakov_pozdniakov_2007",
                "horley",
                "guy_1990",
                "barthel_1958",
            },
        )
        for row in self.result["not_scored"]:
            self.assertEqual(row["values"], [])
            self.assertIn("invented", row["reason"].lower())

    def test_scored_values_match_the_cited_spellings(self) -> None:
        by_id = {item.set_id: item for item in proposal_sets()}
        names = by_id["davletshin_2012_names"]
        self.assertEqual(
            [(value.sign, value.words) for value in names.values],
            [("076", ("ko",)), ("021", ("'a",)), ("530", ("ariki",))],
        )
        self.assertEqual(cv_syllables_mapped("ko"), ("ko",))
        self.assertEqual(cv_syllables_mapped("'a"), ("'a",))
        self.assertEqual(cv_syllables_mapped("ariki"), ("a", "ri", "ki"))
        numerals = by_id["davletshin_2012_numerals"]
        self.assertEqual(numerals.values[0].words, ("tahi",))
        self.assertEqual(cv_syllables_mapped("tahi"), ("ta", "hi"))
        fischer = by_id["fischer_1995"]
        self.assertEqual(
            [value.sign for value in fischer.values],
            ["600", "606", "700", "008", "076"],
        )
        phallus = fischer.values[-1]
        self.assertEqual(phallus.words, ("ki", "ai", "ki", "roto", "ki"))
        tangata = tangata_hypothesis()
        self.assertEqual(tangata.status, "hypothesis")
        self.assertEqual(tangata.syllables, ("ta", "nga", "ta"))
        declined = " ".join(note["note"] for note in names.not_scored)
        self.assertIn("will not draw a conclusion", declined)
        scored_signs = {
            value["sign"]
            for row in self.result["scored"]
            for value in row["values"]
        }
        self.assertNotIn("200", scored_signs)

    def test_holm_covers_every_scored_set_and_the_retest(self) -> None:
        expected = {row["set_id"] for row in self.result["scored"]}
        expected.add("hypothesis_200_tangata")
        self.assertEqual(set(self.result["holm"]), expected)
        for row in self.result["scored"]:
            self.assertFalse(row["adopted"])
            self.assertGreaterEqual(row["holm_p"], row["worse_p"] - 1e-12)
            self.assertIn("calendar", row["observed"]["slices"])
            self.assertIn("gv6", row["observed"]["slices"])
            self.assertIn("great_tradition", row["observed"]["slices"])
        tangata = self.result["tangata"]
        self.assertEqual(tangata["label"], "HYPOTHESIS")
        self.assertIn("G", tangata["caveat"])
        self.assertNotIn("G", tangata["holdout_tablets"])
        self.assertFalse(tangata["adopted"])
        self.assertLessEqual(tangata["holm_p"], 1.0)

    def test_published_counts_stay_put(self) -> None:
        by_id = {row["set_id"]: row for row in self.result["scored"]}
        names = by_id["davletshin_2012_names"]
        self.assertEqual(names["observed"]["primary"], 2)
        self.assertEqual((names["shuffle"]["ge"], names["shuffle"]["trials"]), (4, 6))
        self.assertEqual((names["random"]["ge"], names["random"]["trials"]), (457, 500))
        numerals = by_id["davletshin_2012_numerals"]
        self.assertEqual(numerals["observed"]["primary"], 0)
        self.assertEqual(numerals["observed"]["spans"], 41)
        self.assertEqual(numerals["shuffle"]["p"], 1.0)
        self.assertEqual(numerals["random"]["p"], 1.0)
        fischer = by_id["fischer_1995"]
        self.assertEqual(fischer["observed"]["primary"], 26)
        self.assertEqual(fischer["observed"]["slices"]["great_tradition"], 14)
        self.assertEqual((fischer["shuffle"]["ge"], fischer["shuffle"]["trials"]), (30, 120))
        self.assertEqual((fischer["random"]["ge"], fischer["random"]["trials"]), (39, 500))
        tangata = self.result["tangata"]
        self.assertEqual(tangata["confirmatory"]["primary"], 16)
        self.assertEqual(tangata["confirmatory"]["spans"], 20)
        self.assertEqual(tangata["explore_not_used_for_p"]["primary"], 9)
        self.assertEqual((tangata["shuffle"]["ge"], tangata["shuffle"]["trials"]), (2, 31))
        self.assertEqual((tangata["random"]["ge"], tangata["random"]["trials"]), (7, 500))
        self.assertAlmostEqual(tangata["holm_p"], 0.25806451612903225)

    def test_written_files_match_the_run(self) -> None:
        self.assertEqual(JSON_PATH.read_text(encoding="utf-8"), render_json(self.result))
        self.assertEqual(DOC_PATH.read_text(encoding="utf-8"), render_markdown(self.result))
        text = DOC_PATH.read_text(encoding="utf-8")
        self.assertIn("not a decipherment", text)
        self.assertIn("Holm", text)
        self.assertIn("tangata", text)
        self.assertIn("MockProvider", text)


if __name__ == "__main__":
    unittest.main()
