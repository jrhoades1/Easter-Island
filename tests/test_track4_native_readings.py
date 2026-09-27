"""Track 4: Ure Vaeiko's chants and Metoro's sign-words vs Barthel codes.

Locks counts from the vendored Thomson and Jaussen/Kohaumotu texts and
the vendored Barthel fixtures. No invented Barthel numbers. No glyph
meanings. Fischer's copula gloss is not a result of this test.

Search comparison, not a translation. MockProvider only. No network.
"""

import unittest

from agents.base.providers import MockProvider
from parsers.native_readings import (
    SHUFFLE_SEED,
    SHUFFLE_TRIALS,
    track4_report,
)
from tests.test_mamari_santiago_ia_076_inventory_scoreboard import STANDING_076_COUNT


class TestTrack4NativeReadings(unittest.TestCase):
    """Cited chant formulas, staff spacing, and Metoro consistency."""

    @classmethod
    def setUpClass(cls):
        cls.provider = MockProvider()
        cls.report = track4_report()

    def test_mock_provider_is_not_called(self):
        """The comparison does not ask a model for a reading."""
        self.assertEqual(self.provider.name, "mock")
        self.assertEqual(self.provider._call_history, [])

    def test_atua_matariri_formula_counts(self):
        """Thomson 1891 pp. 520–521: 48 verses, 41 with the copula frame."""
        formula = self.report["formula"]
        self.assertEqual(formula["verse_count"], 48)
        self.assertEqual(formula["full_formula_count"], 41)
        self.assertEqual(formula["frame_count"], 41)
        self.assertEqual(formula["product_count"], 41)
        self.assertEqual(formula["adjacent_gap_count"], 38)
        self.assertEqual(formula["adjacent_gap_histogram"], {3: 18, 4: 15, 5: 3, 6: 1, 7: 1})
        self.assertEqual(formula["adjacent_gap_mode3"], 18)
        self.assertEqual(formula["repeated_x_count"], 3)
        self.assertEqual(formula["repeated_y_count"], 1)
        self.assertEqual(formula["repeated_z_count"], 1)
        self.assertEqual(
            formula["repeated_names"],
            {"x": ["atua metua", "kuhikia", "tikitehatu"], "y": ["hiuaoioi"], "z": ["ngaatu"]},
        )

    def test_other_chants_do_not_use_the_copula_frame(self):
        """Apai, Eaha, Ka ihi uiga, and Ate repeat their own lines, not 'ki ai kiroto'."""
        frames = self.report["frames"]
        self.assertEqual(frames["atua_frame"], 41)
        self.assertEqual(frames["apai_frame"], 0)
        self.assertEqual(frames["apai_apai"], 5)
        self.assertEqual(frames["eaha_frame"], 10)
        self.assertEqual(frames["ka_ihi_frame"], 4)
        self.assertEqual(frames["ka_ihi_auwe"], 5)
        self.assertEqual(frames["ate_frame"], 0)
        self.assertEqual(frames["ate_hoa"], 5)

    def test_tablet_r_has_no_076_triad(self):
        """Plates XXXVIII–XXXIX are Barthel R. Glyph 076 does not occur."""
        self.assertEqual(self.report["tablet_r_lines"], 17)
        self.assertEqual(self.report["tablet_r_stems"], 490)
        self.assertEqual(self.report["tablet_r_076"], 0)
        assigned = self.report["assigned"]["atua_matariri"]
        self.assertEqual(assigned["stems"], 490)
        self.assertEqual(assigned["stem_076"], 0)

    def test_assigned_tablets_are_not_076_texts(self):
        """Later plate identifications. None of them is the staff's 076 pattern."""
        assigned = self.report["assigned"]
        self.assertEqual(assigned["apai"]["stems"], 886)
        self.assertEqual(assigned["apai"]["stem_076"], 5)
        self.assertEqual(assigned["eaha"]["stems"], 787)
        self.assertEqual(assigned["eaha"]["stem_076"], 3)
        self.assertEqual(assigned["ka_ihi_uiga"]["stems"], 266)
        self.assertEqual(assigned["ka_ihi_uiga"]["stem_076"], 0)
        self.assertEqual(assigned["ate_a_renga"]["stems"], 1004)
        self.assertEqual(assigned["ate_a_renga"]["stem_076"], 0)

    def test_staff_076_spacing_beats_a_line_shuffle(self):
        """Glyph 076 on the staff is spaced more tightly than chance.

        564 is the already-locked Ia inventory count. Interior gaps are
        the runs between successive 076s, one fewer per line than the
        delimiter count when every line has at least one 076.
        """
        staff = self.report["staff"]
        self.assertEqual(staff["seed"], SHUFFLE_SEED)
        self.assertEqual(staff["trials"], SHUFFLE_TRIALS)
        self.assertEqual(staff["stem_total"], 2469)
        self.assertEqual(staff["delimiter_count"], STANDING_076_COUNT)
        self.assertEqual(staff["delimiter_count"], 564)
        self.assertEqual(staff["interior_gap_count"], 550)
        self.assertEqual(staff["interior_gap_len3"], 197)
        self.assertEqual(
            staff["interior_gap_histogram"],
            {0: 14, 1: 57, 2: 59, 3: 197, 4: 137, 5: 43, 6: 15, 7: 13, 8: 9, 9: 3, 10: 2, 11: 1},
        )
        self.assertEqual(staff["chant_gap_bins"], (0, 0, 0, 18, 15, 5))
        self.assertEqual(staff["staff_gap_bins"], (14, 57, 59, 197, 137, 86))
        self.assertEqual(staff["l1_scaled"], 5222)
        self.assertEqual(staff["null_len3_ge_observed"], 0)
        self.assertEqual(staff["null_l1_le_observed"], 0)

    def test_metoro_pairs_only_where_counts_match(self):
        """78 of 83 lines are not one Jaussen group per vendored Barthel token."""
        metoro = self.report["metoro"]
        self.assertEqual(metoro["metoro_line_count"], 83)
        self.assertEqual(metoro["matched_line_count"], 5)
        self.assertEqual(metoro["mismatched_line_count"], 78)
        self.assertEqual(metoro["matched_lines"], ("Ab1", "Cb8", "Ca2", "Ev1", "Ev8"))
        self.assertEqual(metoro["paired_positions"], 220)
        self.assertEqual(metoro["ab1_positions"], 82)

    def test_metoro_phrases_are_not_a_consistent_code(self):
        """Same Barthel code, same phrase: the shuffle reaches the observed rate.

        The one half-share is 741 with 'mo te ariki' on 2 of 4 hits.
        That phrase is not a meaning of 741.
        """
        metoro = self.report["metoro"]
        self.assertEqual(metoro["trials"], SHUFFLE_TRIALS)
        self.assertEqual(metoro["seed"], SHUFFLE_SEED)
        self.assertEqual(metoro["code_types_n_ge3"], 24)
        self.assertEqual(metoro["code_modal_hits"], 26)
        self.assertEqual(metoro["code_modal_total"], 116)
        self.assertEqual(metoro["code_majority_types"], 1)
        self.assertEqual(metoro["null_code_modal_ge"], 136)
        self.assertEqual(metoro["stem_types_n_ge3"], 25)
        self.assertEqual(metoro["stem_modal_hits"], 27)
        self.assertEqual(metoro["stem_modal_total"], 144)
        self.assertEqual(metoro["stem_majority_types"], 1)
        self.assertEqual(metoro["stem_majority_rows"], (("741", 4, 2, "mo te ariki"),))
        self.assertEqual(metoro["null_stem_modal_ge"], 282)
        self.assertEqual(metoro["content_jaccard_milli"], 24)
        self.assertEqual(metoro["null_jaccard_ge"], 37)
        self.assertEqual(metoro["ab1_stem_types_n_ge3"], 14)
        self.assertEqual(metoro["ab1_modal_hits"], 15)
        self.assertEqual(metoro["ab1_modal_total"], 61)
        self.assertEqual(metoro["ab1_majority_types"], 1)
        self.assertEqual(metoro["null_ab1_modal_ge"], 239)
        self.assertGreater(metoro["null_code_modal_ge"], 50)
        self.assertGreater(metoro["null_stem_modal_ge"], 50)
        self.assertGreater(metoro["null_ab1_modal_ge"], 50)
