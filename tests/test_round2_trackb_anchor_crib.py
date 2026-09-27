"""Round 2 Track B: anchor crib against a phonetic null and a logogram null.

Counts are recomputed from the vendored Barthel pages and the vendored
Rapanui word lists. MockProvider only. No reading is adopted here.
"""

from __future__ import annotations

import unittest
from collections import Counter
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round2_trackb import (
    ADOPT_FRACTION,
    NullCount,
    _windows,
    build_anchors,
    build_lexicon,
    cv_syllables,
    hypotheses,
    load_headwords,
    load_lines,
    run_round2_trackb,
)

DOC_PATH = Path(__file__).resolve().parents[1] / "docs" / "decipherment" / "round2_trackB_anchor_crib.md"

OUTSIDE_040 = (17, 9, 17, 1, 19, 2, 5, 10, 4, 0, 1, 0, 0, 1, 3, 8, 9, 12, 5, 0, 1, 0)
OUTSIDE_200 = (14, 31, 11, 10, 14, 2, 13, 54, 22, 0, 2, 0, 2, 5, 3, 55, 33, 16, 14, 3, 0, 3)
OUTSIDE_076 = (3, 8, 0, 0, 5, 0, 41, 8, 472, 0, 0, 0, 0, 1, 0, 6, 7, 0, 3, 32, 0, 0)


class TestCribUnits(unittest.TestCase):
    """Syllable rule and the adopt gate. No corpus shuffle."""

    def test_provider_must_be_mock(self):
        with self.assertRaises(TypeError):
            run_round2_trackb(object())

    def test_cv_keeps_real_onsets_and_drops_codas(self):
        self.assertEqual(cv_syllables("tangata"), ("ta", "nga", "ta"))
        self.assertEqual(cv_syllables("omotohi"), ("o", "mo", "to", "hi"))
        self.assertEqual(cv_syllables("marama"), ("ma", "ra", "ma"))
        self.assertEqual(cv_syllables("pō"), ("po",))
        self.assertEqual(cv_syllables("ina-ira"), ("i", "na", "i", "ra"))
        self.assertIsNone(cv_syllables("tantan"))
        lexicon, _forms, targets = build_lexicon(load_headwords())
        self.assertNotIn(("ta", "ta"), lexicon)
        self.assertIn(("ta", "nga", "ta"), targets)
        self.assertIn(("ma", "ra", "ma"), targets)
        self.assertNotIn(("po",), targets)

    def test_acrophony_is_the_first_syllable(self):
        by_name = {item.name: item.syllables() for item in hypotheses()}
        self.assertEqual(
            by_name["H1"],
            {"040": "po", "143": "ra", "152": "o", "200": "ta", "076": "u"},
        )
        self.assertEqual(
            by_name["H2"],
            {"040": "ma", "143": "ra", "152": "o", "200": "ko", "076": "po"},
        )
        self.assertEqual(
            by_name["H4"],
            {"040": "po", "143": "ra", "152": "o", "200": "ko", "076": "ta"},
        )

    def test_adopt_gate_needs_a_positive_score_past_the_fraction(self):
        self.assertEqual(ADOPT_FRACTION, 0.05)
        self.assertFalse(NullCount(0, 0, 500).survives)
        self.assertFalse(NullCount(10, 6, 100).survives)
        self.assertTrue(NullCount(10, 5, 100).survives)
        self.assertTrue(NullCount(11, 0, 500).survives)


class TestRound2TrackB(unittest.TestCase):
    """Locked measurements. One corpus run, shared by the methods."""

    @classmethod
    def setUpClass(cls):
        cls.provider = MockProvider()
        cls.report = run_round2_trackb(cls.provider)

    def test_provider_is_unused(self):
        self.assertEqual(self.provider.get_call_history(), [])

    def test_corpus_and_outside_counts(self):
        report = self.report
        self.assertEqual(report.corpus_stems, 14841)
        self.assertEqual(
            report.sign_totals,
            (("040", 152), ("143", 1), ("152", 1), ("200", 311), ("076", 682)),
        )
        self.assertEqual(
            dict(report.anchor_stem_counts),
            {
                ("040", "calendar"): 28,
                ("143", "calendar"): 1,
                ("152", "calendar"): 1,
                ("200", "gv6-chain"): 4,
                ("076", "gv6-chain"): 4,
                ("076", "staff-bracket"): 92,
            },
        )
        outside = dict(report.outside_by_tablet)
        self.assertEqual(outside["040"], OUTSIDE_040)
        self.assertEqual(outside["143"], tuple(0 for _ in range(22)))
        self.assertEqual(outside["152"], tuple(0 for _ in range(22)))
        self.assertEqual(outside["200"], OUTSIDE_200)
        self.assertEqual(outside["076"], OUTSIDE_076)
        self.assertEqual(sum(OUTSIDE_040), 124)
        self.assertEqual(sum(OUTSIDE_200), 307)
        self.assertEqual(sum(OUTSIDE_076), 586)
        positions = dict(report.outside_positions)
        self.assertEqual(dict(positions["040"]), {"mid": 121, "start": 3})
        self.assertEqual(dict(positions["200"]), {"end": 2, "mid": 297, "start": 8})
        self.assertEqual(dict(positions["076"]), {"end": 7, "mid": 579})

    def test_bracket_double_and_gv6_chain(self):
        lines = load_lines()
        anchors = build_anchors(lines)
        doubles = []
        for line in lines:
            if line.side != "Ia":
                continue
            for group_index, stems in enumerate(line.stems):
                if (line.number, group_index) not in anchors.bracket_groups:
                    continue
                if stems.count("076") > 1:
                    doubles.append((line.line_id, group_index, line.groups[group_index]))
        self.assertEqual(doubles, [("Ia7", 116, "076.076t")])
        self.assertEqual(len(anchors.bracket_groups), 91)
        self.assertEqual(self.report.gv6_chain, 4)
        self.assertEqual(self.report.gv6_handoffs, 3)
        self.assertEqual(self.report.gv6_quad, ("200", "769", "381", "002.076"))

    def test_frames_runs_and_separator(self):
        report = self.report
        self.assertEqual(report.outside_runs_040, ((1, 104), (2, 7), (3, 2)))
        self.assertEqual(
            report.outside_run_sites_040,
            (
                ("Bv2", 5, 2),
                ("Ra2", 0, 3),
                ("Rb2", 8, 2),
                ("Er1", 49, 2),
                ("Er2", 48, 2),
                ("Er6", 40, 2),
                ("Hv10", 29, 2),
                ("Cb4", 28, 2),
                ("Cb13", 15, 3),
            ),
        )
        self.assertEqual(
            report.frame_sites_040,
            (
                (("760", "006"), ("Ca10:11", "Ca10:22", "Ca10:30", "Ca11:6", "Ca11:18", "Ca12:1")),
                (("003", "003"), ("Cb10:31", "Ab2:27", "Ab3:8", "Ab3:35", "Ab5:19", "Ab5:46")),
                (("300", "300"), ("Er1:32", "Er2:12", "Er2:29", "Er4:3")),
            ),
        )
        self.assertEqual(report.separator_inside_full[0][1], 6)
        self.assertEqual(report.separator_inside_full[1][1], 1)
        self.assertEqual(report.separator_inside_full[2][1], 1)
        self.assertEqual(
            report.separator_outside,
            ((("670", "008"), 1), (("375", "041"), 1)),
        )
        nulls = dict(report.separator_null)
        self.assertEqual(nulls["length_at_least_3"].observed, 0)
        self.assertEqual(nulls["length_at_least_3"].positive, 9)
        self.assertEqual(nulls["length_at_least_3"].trials, 500)
        self.assertEqual(nulls["670 008"].ge, 313)
        self.assertEqual(nulls["375 041"].ge, 47)
        self.assertFalse(nulls["670 008"].survives)
        self.assertFalse(nulls["375 041"].survives)

    def test_logogram_and_suffix_nulls(self):
        report = self.report
        self.assertEqual(report.sky_breakdown, (("008", 3), ("041", 4)))
        self.assertEqual(report.sky_slots, 245)
        self.assertEqual(report.sky_null.observed, 7)
        self.assertEqual(report.sky_null.ge, 66)
        self.assertFalse(report.sky_null.survives)
        self.assertEqual(report.pair_null.observed, 11)
        self.assertEqual(report.pair_null.ge, 0)
        self.assertTrue(report.pair_null.survives)
        self.assertEqual(report.calendar_neighbor_null.observed, 49)
        self.assertEqual(report.calendar_neighbor_null.ge, 0)
        self.assertEqual(
            report.phrase_sites,
            (
                ("Ia", 3, 45, ("200", "690.090", "129.076")),
                ("Ia", 8, 94, ("200f", "023", "440.076")),
                ("Ia", 11, 117, ("200", "726", "571.076")),
                ("Ia", 12, 68, ("200?", "380.061x", "002V:076")),
                ("Ia", 14, 92, ("200", "700", "071.076")),
            ),
        )
        self.assertEqual(report.phrase_handoffs, 0)
        self.assertEqual(report.phrase_null.observed, 5)
        self.assertEqual(report.phrase_null.ge, 127)
        self.assertFalse(report.phrase_null.survives)
        self.assertEqual(report.phrase_trials_with_handoff, 0)
        self.assertEqual(report.slot_staff[0], 408)
        self.assertEqual(report.slot_staff[1], 393)
        self.assertEqual(report.slot_staff[2].ge, 0)
        self.assertEqual(report.slot_other[0], 105)
        self.assertEqual(report.slot_other[1], 97)
        self.assertEqual(report.slot_other[2].ge, 0)
        self.assertEqual(
            dict(report.roles_076),
            {"bare": 67, "medial": 8, "prefix": 15, "suffix": 493},
        )
        self.assertEqual(
            dict(report.roles_200),
            {"bare": 103, "medial": 9, "prefix": 154, "suffix": 22},
        )
        self.assertEqual(report.host_076[0], ("090", 50))
        self.assertEqual(report.host_076[1], ("430", 25))

    def test_phonetic_scores_and_no_adopted_reading(self):
        report = self.report
        self.assertEqual(report.lexicon_sizes, (656, 48, 54))
        self.assertEqual(report.adopted_readings, ())
        self.assertEqual(report.inside_crib_hits, (("H1", 0), ("H2", 0), ("H3", 0), ("H4", 0)))
        lines = load_lines()
        windows = _windows(lines, build_anchors(lines), outside=True)
        self.assertEqual(len(windows), 81)
        self.assertEqual(Counter(windows)[("200", "200")], 25)
        by_name = {item.name: item for item in report.hypotheses}
        h1 = by_name["H1"]
        self.assertEqual(
            h1.open_hits,
            ((("ta", "u"), 8), (("u", "ta"), 7), (("po", "u"), 2)),
        )
        self.assertEqual(h1.open_permutation.ge, 66)
        self.assertEqual(h1.open_permutation.trials, 120)
        self.assertEqual(h1.open_random.ge, 105)
        self.assertEqual(h1.open_random.positive, 298)
        self.assertEqual(h1.crib_hits, ())
        self.assertEqual(h1.crib_permutation.ge, 120)
        self.assertEqual(h1.crib_random.positive, 15)
        self.assertEqual(h1.phrase_hits, 0)
        self.assertEqual(h1.phrase_permutation.ge, 120)
        self.assertFalse(h1.reading_adopted)
        self.assertFalse(h1.open_permutation.survives)
        self.assertFalse(h1.open_random.survives)
        h2 = by_name["H2"]
        self.assertEqual(h2.open_hits, ())
        self.assertEqual(h2.open_permutation.ge, 120)
        self.assertEqual(h2.crib_random.ge, 500)
        self.assertFalse(h2.reading_adopted)
        h3 = by_name["H3"]
        self.assertEqual(h3.open_hits, ((("po", "u"), 2),))
        self.assertEqual(h3.open_permutation.ge, 88)
        self.assertEqual(h3.open_random.ge, 294)
        self.assertFalse(h3.reading_adopted)
        h4 = by_name["H4"]
        self.assertEqual(h4.open_hits, ((("ta", "po"), 3),))
        self.assertEqual(h4.open_permutation.ge, 92)
        self.assertEqual(h4.open_random.ge, 270)
        self.assertEqual(h4.phrase_hits, 0)
        self.assertFalse(h4.reading_adopted)
        for item in report.hypotheses:
            self.assertFalse(item.crib_permutation.survives)
            self.assertFalse(item.crib_random.survives)
            self.assertFalse(item.phrase_permutation.survives)

    def test_writeup_quotes_the_locks(self):
        text = DOC_PATH.read_text(encoding="utf-8")
        for snippet in (
            "No reading is adopted",
            "656",
            "48",
            "81",
            "66 of 120",
            "105 of 500",
            "15 of 500",
            "393 of 408",
            "97 of 105",
            "66 draws",
            "0 draws",
            "127 draws",
            "9 draws",
            "47 times",
            "313 times",
            "Churchill 1912",
            "Fuentes 1960",
            "Englert",
            "MockProvider",
            "tau",
            "tapo",
            "076.076t",
        ):
            self.assertIn(snippet, text)
        self.assertEqual(self.provider.get_call_history(), [])
