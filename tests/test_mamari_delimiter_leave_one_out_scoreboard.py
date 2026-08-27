"""Calendar Guy 8-gram leave-one-out: hold out one window at a time.

Cycle 49 text-search lock. Uses only the existing Kohaumotu / Guy
fixture (tests/fixtures/mamari_ca6_ca9_barthel.json). No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. No live LLM.

The calendar scoreboard recovers Guy's 8-stem delimiter as the top
8-gram when the whole Ca6–Ca9 passage is mined. That can be circular:
the structure is in the same text you score. This lock holds out ONE
published Guy window, mines extract_ngrams(n=8, min_frequency=2) on
the remaining calendar stems only, and records whether the 8-gram is
still recovered as a repeating 8-gram and whether it is still the
unique top 8-gram. Repeat for every exact Guy window. Ca6 315/375
first-delimiter variants are not remapped and are not windows.

The held-out line is split at the hole so n-grams do not cross a
join that was never published. Search lock, not a rate table, not a
merge, and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    find_ngram_hits,
    load_corpus_survey,
)

PROFILE_N = 8
PROFILE_MIN_FREQ = 2
# Exact Guy windows on Ca7/Ca8. Ca6 315/375 variants are excluded.
STANDING_GUY_WINDOWS = (
    ("Ca7", 6, 14),
    ("Ca7", 19, 27),
    ("Ca7", 33, 41),
    ("Ca8", 3, 11),
    ("Ca8", 15, 23),
    ("Ca8", 29, 37),
)
STANDING_WINDOW_COUNT = 6
# (window_index, recovered, still_top). still_top is unique highest freq.
# Holding out Ca7[33:41] leaves Guy tied at freq 5 with
# 040 390 041 378 041 670 008 078, so still-top is no.
STANDING_LOO_TABLE = (
    (0, True, True),
    (1, True, True),
    (2, True, False),
    (3, True, True),
    (4, True, True),
    (5, True, True),
)
STANDING_HELD_OUT_STEM_TOTAL = 93
STANDING_FULL_STEM_TOTAL = 101
STANDING_FULL_TOP_8GRAM_FREQ = 6
STANDING_TIE_WINDOW_INDEX = 2
STANDING_TIE_8GRAM = ("040", "390", "041", "378", "041", "670", "008", "078")
STANDING_TIE_FREQ = 5


@dataclass(frozen=True)
class LeaveOneOutRow:
    """One held-out Guy window. Recovery flags only; no meanings."""

    window_index: int
    recovered: bool
    still_top: bool


@dataclass(frozen=True)
class LeaveOneOutLock:
    """Leave-one-out snapshot on the published Ca6–Ca9 fixture."""

    windows: tuple[tuple[str, int, int], ...]
    table: tuple[LeaveOneOutRow, ...]


def loo_tuple(row: LeaveOneOutRow) -> tuple[int, bool, bool]:
    """Stable lock row: window index, recovered, still-top."""
    return (row.window_index, row.recovered, row.still_top)


def guy_windows(
    lines: list[list[str]],
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    line_names: tuple[str, ...] = CALENDAR_LINE_NAMES,
) -> tuple[tuple[str, int, int], ...]:
    """Exact Guy 8-gram spans in reading order. Search only."""
    n = len(motif)
    return tuple(
        (line_names[line_index], start, start + n)
        for line_index, start in find_ngram_hits(lines, motif)
    )


def hold_out_window_stems(
    lines: list[list[str]],
    window: tuple[str, int, int],
    line_names: tuple[str, ...] = CALENDAR_LINE_NAMES,
) -> list[list[str]]:
    """Remaining calendar stems with one Guy window removed.

    The held-out line is split at the hole so n-grams do not cross an
    unpublished join. Other lines stay intact. Empty fragments drop.
    """
    name, start, end = window
    held = line_names.index(name)
    remaining: list[list[str]] = []
    for index, sequence in enumerate(lines):
        if index != held:
            if sequence:
                remaining.append(list(sequence))
            continue
        left = sequence[:start]
        right = sequence[end:]
        if left:
            remaining.append(list(left))
        if right:
            remaining.append(list(right))
    return remaining


def motif_recovery(
    grams: list[tuple[tuple[str, ...], int]],
    motif: tuple[str, ...],
) -> tuple[bool, bool]:
    """Recovered at freq ≥2, and uniquely the highest-frequency 8-gram."""
    freqs = {gram: freq for gram, freq in grams}
    recovered = motif in freqs
    others = [freq for gram, freq in grams if gram != motif]
    still_top = recovered and (not others or freqs[motif] > max(others))
    return recovered, still_top


def score_leave_one_out(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    line_names: tuple[str, ...] = CALENDAR_LINE_NAMES,
    min_frequency: int = PROFILE_MIN_FREQ,
) -> LeaveOneOutLock:
    """Hold out each Guy window; mine remaining stems. Search only."""
    windows = guy_windows(lines, motif, line_names)
    rows: list[LeaveOneOutRow] = []
    n = len(motif)
    for index, window in enumerate(windows):
        remaining = hold_out_window_stems(lines, window, line_names)
        grams = analyzer.extract_ngrams(remaining, n=n, min_frequency=min_frequency)
        recovered, still_top = motif_recovery(grams, motif)
        rows.append(
            LeaveOneOutRow(
                window_index=index,
                recovered=recovered,
                still_top=still_top,
            )
        )
    return LeaveOneOutLock(windows=windows, table=tuple(rows))


class TestDelimiterLeaveOneOutHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_two_copies_hold_one_kills_recovery(self):
        """Two motif lines; hold one out: remaining freq is 1, not recovered."""
        motif = DELIMITER_MOTIF
        lines = [list(motif), list(motif)]
        names = ("L0", "L1")
        remaining = hold_out_window_stems(lines, ("L0", 0, 8), names)
        self.assertEqual(remaining, [list(motif)])
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        grams = analyzer.extract_ngrams(remaining, n=8, min_frequency=2)
        recovered, still_top = motif_recovery(grams, motif)
        self.assertFalse(recovered)
        self.assertFalse(still_top)
        self.assertEqual(grams, [])
        self.assertEqual(provider.get_call_history(), [])

    def test_three_copies_hold_one_still_recovers_as_top(self):
        """Three motif lines; hold one out: freq 2, unique top."""
        motif = DELIMITER_MOTIF
        lines = [list(motif), list(motif), list(motif)]
        names = ("L0", "L1", "L2")
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        lock = score_leave_one_out(lines, analyzer, line_names=names)
        self.assertEqual(lock.windows, (("L0", 0, 8), ("L1", 0, 8), ("L2", 0, 8)))
        self.assertEqual(
            tuple(loo_tuple(row) for row in lock.table),
            ((0, True, True), (1, True, True), (2, True, True)),
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_or_outrank_is_not_still_top(self):
        """Recovered can stay true while unique-top fails."""
        motif = DELIMITER_MOTIF
        other = ("AAA",) * 8
        # Three motif + three other: hold one motif → motif freq 2, other 3.
        lines = [list(motif), list(motif), list(motif), list(other), list(other), list(other)]
        names = ("M0", "M1", "M2", "O0", "O1", "O2")
        remaining = hold_out_window_stems(lines, ("M0", 0, 8), names)
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        grams = analyzer.extract_ngrams(remaining, n=8, min_frequency=2)
        recovered, still_top = motif_recovery(grams, motif)
        self.assertTrue(recovered)
        self.assertFalse(still_top)
        freqs = dict(grams)
        self.assertEqual(freqs[motif], 2)
        self.assertEqual(freqs[other], 3)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariDelimiterLeaveOneOutScoreboard(unittest.TestCase):
    """Published Ca6–Ca9 Guy-window leave-one-out lock. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.fixture = load_mamari_fixture()
        self.lines = fixture_line_stems(self.fixture)
        self.survey = load_corpus_survey()
        self.lock = score_leave_one_out(self.lines, self.analyzer)

    def test_fixture_is_the_existing_published_passage(self):
        """Same cited fixture as the calendar scoreboard. No new numbers."""
        source = self.fixture["source"]
        self.assertIn("kohaumotu.org", source["primary"]["url"])
        self.assertEqual(tuple(self.fixture["lines"]), CALENDAR_LINE_NAMES)
        self.assertEqual([len(line) for line in self.lines], [16, 43, 40, 2])
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_FULL_STEM_TOTAL)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_guy_windows_are_the_six_exact_8grams(self):
        """Locked window list is exact Guy on Ca7/Ca8. Variants are out."""
        self.assertEqual(self.lock.windows, STANDING_GUY_WINDOWS)
        self.assertEqual(len(self.lock.windows), STANDING_WINDOW_COUNT)
        self.assertEqual(guy_windows(self.lines), STANDING_GUY_WINDOWS)
        for name, start, end in self.lock.windows:
            tokens = tuple(self.lines[CALENDAR_LINE_NAMES.index(name)][start:end])
            self.assertEqual(tokens, DELIMITER_MOTIF)
            self.assertEqual(end - start, PROFILE_N)
        ca6 = self.lines[0]
        self.assertNotIn("378", ca6)
        self.assertIn("315", ca6)
        self.assertIn("375", ca6)
        self.assertTrue(all(name != "Ca6" for name, _s, _e in self.lock.windows))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leave_one_out_table_is_standing_truth(self):
        """Lock window index, recovered, still-top for each Guy window."""
        locked = tuple(loo_tuple(row) for row in self.lock.table)
        self.assertEqual(locked, STANDING_LOO_TABLE)
        self.assertEqual(len(locked), STANDING_WINDOW_COUNT)
        for index, row in enumerate(self.lock.table):
            self.assertEqual(row.window_index, index)
            window = self.lock.windows[index]
            remaining = hold_out_window_stems(self.lines, window)
            self.assertEqual(
                sum(len(sequence) for sequence in remaining),
                STANDING_HELD_OUT_STEM_TOTAL,
            )
            held_name, held_start, held_end = window
            held_line = self.lines[CALENDAR_LINE_NAMES.index(held_name)]
            self.assertEqual(tuple(held_line[held_start:held_end]), DELIMITER_MOTIF)
            grams = self.analyzer.extract_ngrams(
                remaining, n=PROFILE_N, min_frequency=PROFILE_MIN_FREQ
            )
            recovered, still_top = motif_recovery(grams, DELIMITER_MOTIF)
            self.assertEqual((index, recovered, still_top), STANDING_LOO_TABLE[index])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_dropping_ca7_600_window_kills_unique_top(self):
        """Ca7[33:41] hold-out: recovered yes, still-top no (tie at freq 5)."""
        row = self.lock.table[STANDING_TIE_WINDOW_INDEX]
        self.assertEqual(self.lock.windows[STANDING_TIE_WINDOW_INDEX], ("Ca7", 33, 41))
        self.assertTrue(row.recovered)
        self.assertFalse(row.still_top)
        remaining = hold_out_window_stems(
            self.lines, self.lock.windows[STANDING_TIE_WINDOW_INDEX]
        )
        grams = self.analyzer.extract_ngrams(
            remaining, n=PROFILE_N, min_frequency=PROFILE_MIN_FREQ
        )
        freqs = dict(grams)
        self.assertEqual(freqs[DELIMITER_MOTIF], STANDING_TIE_FREQ)
        self.assertEqual(freqs[STANDING_TIE_8GRAM], STANDING_TIE_FREQ)
        self.assertFalse(freqs[DELIMITER_MOTIF] > freqs[STANDING_TIE_8GRAM])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_full_passage_still_recovers_guy_as_unique_top(self):
        """Existing calendar claim is unchanged on the whole 101-stem text."""
        grams = self.analyzer.extract_ngrams(
            self.lines, n=PROFILE_N, min_frequency=PROFILE_MIN_FREQ
        )
        self.assertTrue(grams)
        self.assertEqual(grams[0][0], DELIMITER_MOTIF)
        self.assertEqual(grams[0][1], STANDING_FULL_TOP_8GRAM_FREQ)
        recovered, still_top = motif_recovery(grams, DELIMITER_MOTIF)
        self.assertTrue(recovered)
        self.assertTrue(still_top)
        self.assertGreater(grams[0][1], grams[1][1])
        self.assertEqual(grams[1][0], STANDING_TIE_8GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-49 leave-one-out table."""
        lock = self.survey["calendar_delimiter_leave_one_out"]
        self.assertEqual(lock["cycle"], 49)
        self.assertEqual(lock["passage"], "ca6_ca9_calendar")
        self.assertEqual(lock["fixture"], "tests/fixtures/mamari_ca6_ca9_barthel.json")
        self.assertEqual(lock["n"], PROFILE_N)
        self.assertEqual(lock["min_frequency"], PROFILE_MIN_FREQ)
        self.assertEqual(lock["window_count"], STANDING_WINDOW_COUNT)
        self.assertEqual(
            [tuple(window) for window in lock["windows"]],
            list(STANDING_GUY_WINDOWS),
        )
        self.assertEqual(
            [tuple(row) for row in lock["table"]],
            list(STANDING_LOO_TABLE),
        )
        self.assertTrue(lock["all_recovered"])
        self.assertFalse(lock["all_still_top"])
        self.assertEqual(lock["tie_window_index"], STANDING_TIE_WINDOW_INDEX)
        self.assertEqual(tuple(lock["tie_8gram"]), STANDING_TIE_8GRAM)
        self.assertTrue(lock["ca6_variants_excluded"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_ia_999_locks_unchanged"])
        self.assertTrue(lock["standing_ia_076_locks_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["santiago_ia_076_inventory"]["cycle"], 48)
        self.assertEqual(self.survey["santiago_ia_999_break"]["cycle"], 47)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["wikimedia_c_a_photo"]["cycle"], 49)
        self.assertTrue(self.survey["wikimedia_c_a_photo"]["strictly_larger_per_calendar_line"])
        self.assertFalse(self.survey["wikimedia_c_a_photo"]["published_hamming_rescored"])
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariDelimiterLeaveOneOutImageSnapshot(unittest.TestCase):
    """Cycle 49 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
