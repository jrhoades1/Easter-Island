"""Ab7 sandwich 9-window Hamming vs the Ab 9-gram motif.

Cycle 42 text-search lock. Uses the already-vendored Kohaumotu Ab.html
fixture only. No invented Barthel. No other tablet. No G00n→Barthel
map. No type merge. No detector retune. No CV.

The cycle-41 Ab7[16:19] 004 600 004 sandwich is not the Ab 9-gram
600 slot. Lock the unique 9-window that places that 600 at slot 3
(same 0-based slot as 605 003 004 600 004 003 040 003 050): tokens,
Hamming vs the motif, and one published token on each side (or
line-edge). Also lock how many other Ab 9-windows with 600 at
slot 3 have Hamming < 9 besides the two exact motif hits.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_600_inventory_scoreboard import (
    PASSAGE_AA,
    PASSAGE_AB,
    PASSAGE_CALENDAR,
    PASSAGE_CB,
    PASSAGE_ORDER,
    PASSAGE_REMAINDER,
    STEM_600,
    existing_passage_specs,
    score_600_inventory,
)
from tests.test_mamari_600_sandwich_scoreboard import (
    SANDWICH,
    STANDING_SANDWICH_HITS,
    STANDING_SANDWICH_TOTAL,
    score_sandwich_lock,
)
from tests.test_mamari_calendar_scoreboard import DELIMITER_MOTIF
from tests.test_mamari_cb_5gram_ca_cross_scoreboard import (
    CB_5GRAMS,
    STANDING_CA_CROSS_TABLE,
    score_cb_5gram_ca_cross,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CB_EIGHTGRAM_COUNT,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CB_LONGEST_N,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_NGRAMS,
    score_cb_repeating_ngrams,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import (
    LINE_EDGE,
    MOTIF_9GRAM,
    hit_flanks,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CA_REMAINDER_EIGHTGRAM_COUNT,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CA_REMAINDER_LONGEST_N,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    REMAINDER_LINE_NAMES,
    find_ngram_hits,
    load_corpus_survey,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import (
    MOTIF_10GRAM,
    STANDING_AA_MOTIF_FREQ,
    STANDING_AA_MOTIF_SPANS,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    AA_LINE_NAMES,
    STANDING_LONGEST_N as AA_LONGEST_N,
    STANDING_LONGEST_NGRAM as AA_LONGEST_NGRAM,
    STANDING_TOP_8GRAM as AA_TOP_8GRAM,
    score_aa_repeating_ngrams,
)
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import (
    MOTIF_AB_9GRAM,
    STANDING_600_SLOT,
    STANDING_AB_MOTIF_FREQ,
    STANDING_AB_MOTIF_SPANS,
)
from tests.test_mamari_tahua_ab_scoreboard import (
    AB_LINE_NAMES,
    STANDING_STEM_TOTAL as AB_STEM_TOTAL,
    ab_line_stems,
    extract_ab_published_tokens,
    load_vendored_ab_html,
)

HAMMING_BELOW = 9
STANDING_SANDWICH_LINE = "Ab7"
STANDING_SANDWICH_START = 16
STANDING_SANDWICH_END = 19
STANDING_SANDWICH_600_INDEX = 17
STANDING_WINDOW_IN_RANGE = True
STANDING_WINDOW_START = 14
STANDING_WINDOW_END = 23
STANDING_WINDOW_TOKENS = (
    "606",
    "074",
    "004",
    "600",
    "004",
    "074",
    "450",
    "074",
    "040",
)
STANDING_WINDOW_HAMMING = 6
STANDING_WINDOW_BEFORE = "009"
STANDING_WINDOW_AFTER = "004"
# (line, start, end, tokens, hamming, before, after)
STANDING_AB7_WINDOW = (
    STANDING_SANDWICH_LINE,
    STANDING_WINDOW_START,
    STANDING_WINDOW_END,
    STANDING_WINDOW_TOKENS,
    STANDING_WINDOW_HAMMING,
    STANDING_WINDOW_BEFORE,
    STANDING_WINDOW_AFTER,
)
STANDING_SLOT3_600_COUNT = 32
STANDING_MOTIF_SLOT3_HITS = 2
STANDING_OTHER_BELOW_HAMMING_9 = 30


@dataclass(frozen=True)
class SlotWindow:
    """One 9-window with 600 at the motif slot. Ids only; no meaning."""

    line: str
    start: int
    end: int
    tokens: tuple[str, ...]
    hamming: int
    before: str | None
    after: str | None
    is_motif: bool


@dataclass(frozen=True)
class Ab7HammingLock:
    """Ab7 sandwich window plus slot-3-600 Hamming census on Ab."""

    window: SlotWindow
    slot3_windows: tuple[SlotWindow, ...]
    other_below_hamming_9: int


def hamming_distance(left: tuple[str, ...] | list[str], right: tuple[str, ...] | list[str]) -> int:
    """Positions that differ. Equal length required."""
    if len(left) != len(right):
        raise ValueError("Hamming requires equal-length windows")
    return sum(a != b for a, b in zip(left, right))


def window_row(hit: SlotWindow) -> tuple:
    """Stable lock row: line, [start, end), tokens, Hamming, flanks."""
    return (hit.line, hit.start, hit.end, hit.tokens, hit.hamming, hit.before, hit.after)


def aligned_window(
    sequence: list[str],
    stem_index: int,
    slot: int = STANDING_600_SLOT,
    n: int = 9,
) -> tuple[int, int, tuple[str, ...]] | None:
    """9-window that places stem_index at slot, or None if out of range."""
    start = stem_index - slot
    end = start + n
    if start < 0 or end > len(sequence):
        return None
    return start, end, tuple(sequence[start:end])


def score_slot3_600_windows(
    lines: list[list[str]],
    line_names: tuple[str, ...],
    motif: tuple[str, ...] = MOTIF_AB_9GRAM,
    stem: str = STEM_600,
    slot: int = STANDING_600_SLOT,
) -> tuple[SlotWindow, ...]:
    """Every 9-window with stem at slot. Hamming vs motif. Search only."""
    n = len(motif)
    rows: list[SlotWindow] = []
    for line_index, sequence in enumerate(lines):
        for start in range(len(sequence) - n + 1):
            tokens = tuple(sequence[start : start + n])
            if tokens[slot] != stem:
                continue
            before, after = hit_flanks(sequence, start, n)
            rows.append(
                SlotWindow(
                    line=line_names[line_index],
                    start=start,
                    end=start + n,
                    tokens=tokens,
                    hamming=hamming_distance(tokens, motif),
                    before=before,
                    after=after,
                    is_motif=tokens == motif,
                )
            )
    return tuple(rows)


def score_ab7_hamming(
    lines: list[list[str]],
    line_names: tuple[str, ...] = AB_LINE_NAMES,
    sandwich_line: str = STANDING_SANDWICH_LINE,
    sandwich_start: int = STANDING_SANDWICH_START,
    sandwich: tuple[str, ...] = SANDWICH,
    motif: tuple[str, ...] = MOTIF_AB_9GRAM,
    slot: int = STANDING_600_SLOT,
    below: int = HAMMING_BELOW,
) -> Ab7HammingLock:
    """Ab7 sandwich slot-3 window and other slot-3-600 Hamming < 9."""
    sequence = lines[line_names.index(sandwich_line)]
    stem_index = sandwich_start + sandwich.index(STEM_600)
    aligned = aligned_window(sequence, stem_index, slot, len(motif))
    if aligned is None:
        raise AssertionError("Ab7 sandwich 9-window is out of range")
    start, end, tokens = aligned
    before, after = hit_flanks(sequence, start, len(motif))
    window = SlotWindow(
        line=sandwich_line,
        start=start,
        end=end,
        tokens=tokens,
        hamming=hamming_distance(tokens, motif),
        before=before,
        after=after,
        is_motif=tokens == motif,
    )
    slot3 = score_slot3_600_windows(lines, line_names, motif, STEM_600, slot)
    other = sum(1 for hit in slot3 if not hit.is_motif and hit.hamming < below)
    return Ab7HammingLock(window=window, slot3_windows=slot3, other_below_hamming_9=other)


class TestAb79gramHammingHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_aligned_window_in_and_out_of_range(self):
        """Slot-3 alignment is in range only when three tokens sit on each side."""
        motif = MOTIF_AB_9GRAM
        sequence = ["X"] + list(motif) + ["Y"]
        provider = MockProvider()
        self.assertEqual(
            aligned_window(sequence, 4, STANDING_600_SLOT, 9),
            (1, 10, motif),
        )
        self.assertIsNone(aligned_window(["004", "600", "004"], 1, STANDING_600_SLOT, 9))
        self.assertEqual(motif[STANDING_600_SLOT], STEM_600)
        self.assertEqual(provider.get_call_history(), [])

    def test_slot3_600_hamming_and_other_below_9(self):
        """Exact motif is Hamming 0; a one-token mismatch is 1; slot 3 caps at 8."""
        motif = MOTIF_AB_9GRAM
        near = ("999",) + motif[1:]
        other = ("111", "222", "333", STEM_600, "444", "555", "666", "777", "888")
        lines = [list(motif), list(near), list(other), ["004", STEM_600, "004"]]
        names = ("L0", "L1", "L2", "L3")
        provider = MockProvider()
        rows = score_slot3_600_windows(lines, names)
        self.assertEqual(
            tuple((hit.line, hit.start, hit.hamming, hit.is_motif) for hit in rows),
            (("L0", 0, 0, True), ("L1", 0, 1, False), ("L2", 0, 8, False)),
        )
        self.assertEqual(hamming_distance(near, motif), 1)
        self.assertEqual(hamming_distance(other, motif), 8)
        self.assertLess(rows[2].hamming, HAMMING_BELOW)
        other_below = sum(1 for hit in rows if not hit.is_motif and hit.hamming < HAMMING_BELOW)
        self.assertEqual(other_below, 2)
        self.assertEqual(provider.get_call_history(), [])

    def test_ab7_style_sandwich_window(self):
        """Sandwich 600 at slot 3 yields tokens, Hamming, and flanks."""
        sandwich_start = 2
        sequence = ["P0", "P1", "004", STEM_600, "004", "R0", "R1", "R2", "R3", "Z"]
        provider = MockProvider()
        lock = score_ab7_hamming(
            [sequence],
            ("L0",),
            sandwich_line="L0",
            sandwich_start=sandwich_start,
        )
        self.assertEqual(tuple(sequence[sandwich_start : sandwich_start + 3]), SANDWICH)
        self.assertEqual(lock.window.start, sandwich_start + 1 - STANDING_600_SLOT)
        self.assertEqual(lock.window.tokens, ("P0", "P1", "004", STEM_600, "004", "R0", "R1", "R2", "R3"))
        self.assertEqual(lock.window.tokens[STANDING_600_SLOT], STEM_600)
        self.assertEqual(lock.window.hamming, 6)
        self.assertEqual(lock.window.before, LINE_EDGE)
        self.assertEqual(lock.window.after, "Z")
        self.assertFalse(lock.window.is_motif)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariAb79gramHammingScoreboard(unittest.TestCase):
    """Cited Ab.html Ab7 sandwich Hamming lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.ab = ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html()))
        self.lock = score_ab7_hamming(self.ab)
        self.passages = existing_passage_specs()
        self.by_passage = {spec.passage: spec for spec in self.passages}

    def test_uses_existing_ab_fixture_only(self):
        """Ab 926 stems are scored; no other tablet is scraped."""
        self.assertEqual(sum(len(line) for line in self.ab), AB_STEM_TOTAL)
        self.assertEqual(tuple(AB_LINE_NAMES), tuple(f"Ab{n}" for n in range(1, 9)))
        self.assertEqual(self.by_passage[PASSAGE_AB].lines, self.ab)
        self.assertEqual(tuple(spec.passage for spec in self.passages), PASSAGE_ORDER)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ab7_sandwich_window_tokens_hamming_and_flanks(self):
        """Ab7[16:19] 600 sits in Ab7[14:23]; Hamming 6; flanks 009 / 004."""
        window = self.lock.window
        sequence = self.ab[AB_LINE_NAMES.index(STANDING_SANDWICH_LINE)]
        self.assertEqual(tuple(sequence[STANDING_SANDWICH_START:STANDING_SANDWICH_END]), SANDWICH)
        self.assertEqual(sequence[STANDING_SANDWICH_600_INDEX], STEM_600)
        aligned = aligned_window(sequence, STANDING_SANDWICH_600_INDEX)
        self.assertIsNotNone(aligned)
        self.assertEqual(bool(aligned), STANDING_WINDOW_IN_RANGE)
        self.assertEqual(aligned, (STANDING_WINDOW_START, STANDING_WINDOW_END, STANDING_WINDOW_TOKENS))
        self.assertEqual(window_row(window), STANDING_AB7_WINDOW)
        self.assertEqual(window.tokens, STANDING_WINDOW_TOKENS)
        self.assertEqual(window.hamming, STANDING_WINDOW_HAMMING)
        self.assertEqual(window.before, STANDING_WINDOW_BEFORE)
        self.assertEqual(window.after, STANDING_WINDOW_AFTER)
        self.assertEqual(window.tokens[STANDING_600_SLOT], STEM_600)
        self.assertEqual(hamming_distance(window.tokens, MOTIF_AB_9GRAM), STANDING_WINDOW_HAMMING)
        self.assertEqual(window.tokens[2:5], SANDWICH)
        self.assertFalse(window.is_motif)
        self.assertNotEqual(window.tokens, MOTIF_AB_9GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_other_slot3_600_windows_below_hamming_9(self):
        """Besides the two motif hits, 30 slot-3-600 windows have Hamming < 9."""
        slot3 = self.lock.slot3_windows
        motif_hits = tuple(hit for hit in slot3 if hit.is_motif)
        other_below = tuple(
            hit for hit in slot3 if not hit.is_motif and hit.hamming < HAMMING_BELOW
        )
        self.assertEqual(len(slot3), STANDING_SLOT3_600_COUNT)
        self.assertEqual(len(motif_hits), STANDING_MOTIF_SLOT3_HITS)
        self.assertEqual(len(motif_hits), STANDING_AB_MOTIF_FREQ)
        self.assertEqual(
            tuple((hit.line, hit.start, hit.end) for hit in motif_hits),
            STANDING_AB_MOTIF_SPANS,
        )
        self.assertEqual({hit.hamming for hit in motif_hits}, {0})
        self.assertEqual(len(other_below), STANDING_OTHER_BELOW_HAMMING_9)
        self.assertEqual(self.lock.other_below_hamming_9, STANDING_OTHER_BELOW_HAMMING_9)
        self.assertEqual(
            STANDING_OTHER_BELOW_HAMMING_9,
            STANDING_SLOT3_600_COUNT - STANDING_MOTIF_SLOT3_HITS,
        )
        self.assertTrue(STANDING_OTHER_BELOW_HAMMING_9 > 0)
        ab7 = [hit for hit in slot3 if hit.line == STANDING_SANDWICH_LINE and hit.start == STANDING_WINDOW_START]
        self.assertEqual(len(ab7), 1)
        self.assertIn(ab7[0], other_below)
        for hit in slot3:
            self.assertEqual(hit.tokens[STANDING_600_SLOT], STEM_600)
            self.assertLessEqual(hit.hamming, 8)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_scoreboards_still_compute(self):
        """Guy / Ca 9-gram / Aa 10-gram / Ab 9-gram / sandwich stay."""
        calendar = self.by_passage[PASSAGE_CALENDAR].lines
        remainder = self.by_passage[PASSAGE_REMAINDER].lines
        cb_lines = self.by_passage[PASSAGE_CB].lines
        aa = self.by_passage[PASSAGE_AA].lines
        ab = self.by_passage[PASSAGE_AB].lines

        aa_profile = score_aa_repeating_ngrams(aa, self.analyzer)
        self.assertEqual(aa_profile.longest_n, AA_LONGEST_N)
        self.assertEqual(aa_profile.longest[0].tokens, AA_LONGEST_NGRAM)
        self.assertEqual(aa_profile.top_8gram.tokens, AA_TOP_8GRAM)
        aa_motif = find_ngram_hits(aa, MOTIF_10GRAM)
        self.assertEqual(len(aa_motif), STANDING_AA_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AA_LINE_NAMES[line_index], start, start + len(MOTIF_10GRAM))
                for line_index, start in aa_motif
            ),
            STANDING_AA_MOTIF_SPANS,
        )

        self.assertTrue(find_ngram_hits(calendar, DELIMITER_MOTIF))
        self.assertEqual(find_ngram_hits(remainder, DELIMITER_MOTIF), [])
        self.assertEqual(find_ngram_hits(cb_lines, DELIMITER_MOTIF), [])

        self.assertEqual(find_ngram_hits(calendar, MOTIF_9GRAM), [])
        self.assertEqual(len(find_ngram_hits(remainder, MOTIF_9GRAM)), 2)
        self.assertEqual(find_ngram_hits(cb_lines, MOTIF_9GRAM), [])

        ab_motif = find_ngram_hits(ab, MOTIF_AB_9GRAM)
        self.assertEqual(len(ab_motif), STANDING_AB_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AB_LINE_NAMES[line_index], start, start + len(MOTIF_AB_9GRAM))
                for line_index, start in ab_motif
            ),
            STANDING_AB_MOTIF_SPANS,
        )
        self.assertEqual(find_ngram_hits(aa, MOTIF_AB_9GRAM), [])
        self.assertEqual(find_ngram_hits(calendar, SANDWICH), [])
        self.assertEqual(find_ngram_hits(remainder, SANDWICH), [])
        self.assertEqual(find_ngram_hits(cb_lines, SANDWICH), [])
        self.assertEqual(find_ngram_hits(aa, SANDWICH), [])

        sandwich = score_sandwich_lock(self.passages)
        self.assertEqual(
            tuple(
                (
                    hit.passage,
                    hit.tablet,
                    hit.side,
                    hit.line,
                    hit.start,
                    hit.end,
                    hit.ab_9gram_slot,
                )
                for hit in sandwich.hits
            ),
            STANDING_SANDWICH_HITS,
        )
        self.assertEqual(len(sandwich.hits), STANDING_SANDWICH_TOTAL)
        inventory = score_600_inventory(self.passages)
        self.assertEqual(inventory.counts[PASSAGE_AB], 32)

        cross = score_cb_5gram_ca_cross(
            CB_5GRAMS,
            calendar,
            CALENDAR_LINE_NAMES,
            remainder,
            REMAINDER_LINE_NAMES,
        )
        locked = tuple((row.tokens, row.calendar_hits, row.remainder_hits) for row in cross)
        self.assertEqual(locked, STANDING_CA_CROSS_TABLE)

        rem_profile = score_remainder_repeating_ngrams(remainder, self.analyzer)
        cb_profile = score_cb_repeating_ngrams(cb_lines, self.analyzer)
        self.assertEqual(rem_profile.longest_n, CA_REMAINDER_LONGEST_N)
        self.assertEqual(len(rem_profile.eightgrams), CA_REMAINDER_EIGHTGRAM_COUNT)
        self.assertEqual(cb_profile.longest_n, CB_LONGEST_N)
        self.assertEqual(len(cb_profile.eightgrams), CB_EIGHTGRAM_COUNT)
        self.assertEqual(CB_EIGHTGRAM_COUNT, 0)
        self.assertEqual(
            tuple(row.tokens for row in cb_profile.longest),
            tuple(tokens for tokens, _n, _freq, _spans in STANDING_LONGEST_NGRAMS),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-42 Ab7 Hamming lock."""
        lock = self.survey["ab7_9gram_hamming"]
        self.assertEqual(lock["cycle"], 42)
        self.assertEqual(lock["passage"], PASSAGE_AB)
        self.assertEqual(lock["sandwich"], list(SANDWICH))
        self.assertEqual(lock["sandwich_span"], [STANDING_SANDWICH_LINE, STANDING_SANDWICH_START, STANDING_SANDWICH_END])
        self.assertEqual(lock["stem"], STEM_600)
        self.assertEqual(lock["stem_slot"], STANDING_600_SLOT)
        self.assertEqual(lock["motif_tokens"], list(MOTIF_AB_9GRAM))
        self.assertTrue(lock["window_in_range"])
        self.assertEqual(
            lock["window"],
            [
                STANDING_SANDWICH_LINE,
                STANDING_WINDOW_START,
                STANDING_WINDOW_END,
                list(STANDING_WINDOW_TOKENS),
                STANDING_WINDOW_HAMMING,
                STANDING_WINDOW_BEFORE,
                STANDING_WINDOW_AFTER,
            ],
        )
        self.assertEqual(lock["hamming"], STANDING_WINDOW_HAMMING)
        self.assertEqual(lock["slot3_600_count"], STANDING_SLOT3_600_COUNT)
        self.assertEqual(lock["motif_hits"], STANDING_MOTIF_SLOT3_HITS)
        self.assertEqual(lock["other_below_hamming_9"], STANDING_OTHER_BELOW_HAMMING_9)
        self.assertEqual(self.survey["stem_600_sandwich"]["cycle"], 41)
        self.assertEqual(self.survey["stem_600_inventory"]["cycle"], 40)
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["cycle"], 39)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariAb79gramHammingImageSnapshot(unittest.TestCase):
    """Cycle 42 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
