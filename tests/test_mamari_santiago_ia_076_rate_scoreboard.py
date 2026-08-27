"""076 rate per existing fixture: hits, stems, rate, threshold.

Cycle 50 text-search lock. Uses only the already-vendored fixtures:
Ca calendar, Ca remainder, Cb, Aa, Ab, Br, Bv, Ia. No new tablet.
Raw stems; 999 is kept. No invented Barthel. No G00n→Barthel map.
No type merge. No detector retune. No CV. No new agents.

Eight-row table: per fixture, 076 hit count, stem count, rate
(hits/stems), and whether rate ≥ 0.10. 076 is a stem id only —
not a list marker, delimiter, or punctuation. No meanings.

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
    PASSAGE_REMAINDER,
    STANDING_CALENDAR_STEM_TOTAL,
)
from tests.test_mamari_600_sandwich_scoreboard import SANDWICH
from tests.test_mamari_aruku_br_scoreboard import (
    STANDING_LONGEST_N as BR_LONGEST_N,
    STANDING_LONGEST_NGRAM as BR_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as BR_STEM_TOTAL,
    br_line_stems,
    extract_br_published_tokens,
    load_vendored_br_html,
    score_br_repeating_ngrams,
)
from tests.test_mamari_aruku_bv_scoreboard import (
    STANDING_LONGEST_N as BV_LONGEST_N,
    STANDING_LONGEST_NGRAM as BV_8GRAM,
    STANDING_STEM_TOTAL as BV_STEM_TOTAL,
    bv_line_stems,
    extract_bv_published_tokens,
    load_vendored_bv_html,
    score_bv_repeating_ngrams,
)
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
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
from tests.test_mamari_cb_side_b_scoreboard import (
    STANDING_STEM_TOTAL as CB_STEM_TOTAL,
    cb_line_stems,
    extract_cb_published_tokens,
    load_vendored_cb_html,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import MOTIF_9GRAM
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CA_REMAINDER_EIGHTGRAM_COUNT,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CA_REMAINDER_LONGEST_N,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_santiago_ia_076_cell_scoreboard import (
    STANDING_CELL_COUNT,
    STANDING_EMPTY_CELL_COUNT,
    STANDING_LENGTH_MEDIAN,
    STANDING_TOP_LENGTHS,
    score_ia_076_cells,
)
from tests.test_mamari_santiago_ia_076_inventory_scoreboard import (
    STANDING_076_COUNT,
    STEM_076,
    score_ia_076_inventory,
)
from tests.test_mamari_santiago_ia_999_scoreboard import STANDING_999_STEM_COUNT
from tests.test_mamari_santiago_ia_scoreboard import (
    IA_HTML_DIR,
    STANDING_LONGEST_N as IA_AS_STEM_LONGEST_N,
    STANDING_LONGEST_NGRAM as IA_AS_STEM_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as IA_STEM_TOTAL,
    extract_ia_published_tokens,
    ia_line_stems,
    load_vendored_ia_html,
    score_ia_repeating_ngrams,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    REMAINDER_LINE_NAMES,
    STANDING_REMAINDER_STEM_TOTAL,
    extract_ca_published_tokens,
    find_ngram_hits,
    load_corpus_survey,
    load_vendored_ca_html,
    remainder_line_stems,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import (
    MOTIF_10GRAM,
    STANDING_AA_MOTIF_FREQ,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    STANDING_LONGEST_N as AA_LONGEST_N,
    STANDING_LONGEST_NGRAM as AA_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as AA_STEM_TOTAL,
    STANDING_TOP_8GRAM as AA_TOP_8GRAM,
    aa_line_stems,
    extract_aa_published_tokens,
    load_vendored_aa_html,
    score_aa_repeating_ngrams,
)
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import (
    MOTIF_AB_9GRAM,
    STANDING_AB_MOTIF_FREQ,
)
from tests.test_mamari_tahua_ab_scoreboard import (
    STANDING_LONGEST_N as AB_LONGEST_N,
    STANDING_LONGEST_NGRAM as AB_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as AB_STEM_TOTAL,
    ab_line_stems,
    extract_ab_published_tokens,
    load_vendored_ab_html,
    score_ab_repeating_ngrams,
)

PASSAGE_BR = "tablet_b_aruku_kurenga_recto"
PASSAGE_BV = "tablet_b_aruku_kurenga_verso"
PASSAGE_IA = "tablet_i_santiago_staff"
PASSAGE_ORDER = (
    PASSAGE_CALENDAR,
    PASSAGE_REMAINDER,
    PASSAGE_CB,
    PASSAGE_AA,
    PASSAGE_AB,
    PASSAGE_BR,
    PASSAGE_BV,
    PASSAGE_IA,
)
RATE_THRESHOLD = 0.10
STANDING_ROW_COUNT = 8
STANDING_AA_076_HITS = 3
STANDING_BR_076_HITS = 4
STANDING_BV_076_HITS = 4
STANDING_ONLY_IA_GE_THRESHOLD = True

# (passage, hits, stems, rate, ge_0.10)
STANDING_TABLE = (
    (PASSAGE_CALENDAR, 0, STANDING_CALENDAR_STEM_TOTAL, 0 / STANDING_CALENDAR_STEM_TOTAL, False),
    (PASSAGE_REMAINDER, 0, STANDING_REMAINDER_STEM_TOTAL, 0 / STANDING_REMAINDER_STEM_TOTAL, False),
    (PASSAGE_CB, 0, CB_STEM_TOTAL, 0 / CB_STEM_TOTAL, False),
    (PASSAGE_AA, STANDING_AA_076_HITS, AA_STEM_TOTAL, STANDING_AA_076_HITS / AA_STEM_TOTAL, False),
    (PASSAGE_AB, 0, AB_STEM_TOTAL, 0 / AB_STEM_TOTAL, False),
    (PASSAGE_BR, STANDING_BR_076_HITS, BR_STEM_TOTAL, STANDING_BR_076_HITS / BR_STEM_TOTAL, False),
    (PASSAGE_BV, STANDING_BV_076_HITS, BV_STEM_TOTAL, STANDING_BV_076_HITS / BV_STEM_TOTAL, False),
    (PASSAGE_IA, STANDING_076_COUNT, IA_STEM_TOTAL, STANDING_076_COUNT / IA_STEM_TOTAL, True),
)


@dataclass(frozen=True)
class Stem076RateRow:
    """One fixture's 076 rate. Ids only; no meanings."""

    passage: str
    hits: int
    stems: int
    rate: float
    ge_threshold: bool


def score_076_rate(
    lines: list[list[str]],
    passage: str,
    stem: str = STEM_076,
    threshold: float = RATE_THRESHOLD,
) -> Stem076RateRow:
    """076 hits / stem count on one fixture. Search only."""
    hits = sum(line.count(stem) for line in lines)
    stems = sum(len(line) for line in lines)
    rate = hits / stems if stems else 0.0
    return Stem076RateRow(
        passage=passage,
        hits=hits,
        stems=stems,
        rate=rate,
        ge_threshold=rate >= threshold,
    )


def rate_row_tuple(row: Stem076RateRow) -> tuple[str, int, int, float, bool]:
    """Stable lock row: passage, hits, stems, rate, ge_0.10."""
    return (row.passage, row.hits, row.stems, row.rate, row.ge_threshold)


def existing_076_rate_lines() -> dict[str, list[list[str]]]:
    """Load the eight already-vendored fixtures. No new scrape."""
    return {
        PASSAGE_CALENDAR: fixture_line_stems(load_mamari_fixture()),
        PASSAGE_REMAINDER: remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        ),
        PASSAGE_CB: cb_line_stems(extract_cb_published_tokens(load_vendored_cb_html())),
        PASSAGE_AA: aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html())),
        PASSAGE_AB: ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html())),
        PASSAGE_BR: br_line_stems(extract_br_published_tokens(load_vendored_br_html())),
        PASSAGE_BV: bv_line_stems(extract_bv_published_tokens(load_vendored_bv_html())),
        PASSAGE_IA: ia_line_stems(extract_ia_published_tokens(load_vendored_ia_html())),
    }


def score_076_rate_table(
    by_passage: dict[str, list[list[str]]],
) -> tuple[Stem076RateRow, ...]:
    """Eight-row 076 rate table in locked passage order. Search only."""
    return tuple(score_076_rate(by_passage[passage], passage) for passage in PASSAGE_ORDER)


class TestSantiagoIa076RateHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_rate_is_hits_over_stems_and_threshold(self):
        """1/10 meets 0.10; 1/11 does not; empty stems are rate 0."""
        provider = MockProvider()
        at = score_076_rate([[STEM_076] + ["001"] * 9], "syn")
        self.assertEqual(rate_row_tuple(at), ("syn", 1, 10, 0.10, True))
        below = score_076_rate([[STEM_076] + ["001"] * 10], "syn")
        self.assertEqual(below.hits, 1)
        self.assertEqual(below.stems, 11)
        self.assertEqual(below.rate, 1 / 11)
        self.assertFalse(below.ge_threshold)
        empty = score_076_rate([[]], "empty")
        self.assertEqual(rate_row_tuple(empty), ("empty", 0, 0, 0.0, False))
        self.assertEqual(provider.get_call_history(), [])

    def test_table_follows_passage_order(self):
        """Scorer walks PASSAGE_ORDER; missing key is an error."""
        provider = MockProvider()
        by_passage = {passage: [[]] for passage in PASSAGE_ORDER}
        by_passage[PASSAGE_AA] = [[STEM_076, STEM_076, "001"]]
        table = score_076_rate_table(by_passage)
        self.assertEqual(tuple(row.passage for row in table), PASSAGE_ORDER)
        self.assertEqual(len(table), STANDING_ROW_COUNT)
        self.assertEqual(rate_row_tuple(table[3])[1:3], (2, 3))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIa076RateScoreboard(unittest.TestCase):
    """Cited-fixture 076 rate lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_passage = existing_076_rate_lines()
        self.table = score_076_rate_table(self.by_passage)
        self.locked = tuple(rate_row_tuple(row) for row in self.table)

    def test_eight_row_076_rate_table(self):
        """Hits / stems / rate / ≥0.10 on the eight existing fixtures."""
        self.assertEqual(self.locked, STANDING_TABLE)
        self.assertEqual(len(self.locked), STANDING_ROW_COUNT)
        self.assertEqual(tuple(row.passage for row in self.table), PASSAGE_ORDER)
        for row, standing in zip(self.table, STANDING_TABLE):
            passage, hits, stems, rate, ge_threshold = standing
            self.assertEqual(row.passage, passage)
            self.assertEqual(row.hits, hits)
            self.assertEqual(row.stems, stems)
            self.assertEqual(row.rate, rate)
            self.assertEqual(row.rate, hits / stems)
            self.assertEqual(row.ge_threshold, ge_threshold)
            self.assertEqual(row.ge_threshold, row.rate >= RATE_THRESHOLD)
            self.assertEqual(row.stems, sum(len(line) for line in self.by_passage[passage]))
            self.assertEqual(
                row.hits,
                sum(line.count(STEM_076) for line in self.by_passage[passage]),
            )
        ge_passages = tuple(row.passage for row in self.table if row.ge_threshold)
        self.assertEqual(ge_passages, (PASSAGE_IA,))
        self.assertEqual(bool(ge_passages) and len(ge_passages) == 1, STANDING_ONLY_IA_GE_THRESHOLD)
        self.assertEqual(self.table[-1].hits, STANDING_076_COUNT)
        self.assertFalse((IA_HTML_DIR / "Ib.html").exists())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_a_b_c_and_ia_scoreboards_still_compute(self):
        """Aa / Ab / Br / Bv / Guy / Ca 9-gram / sandwich / Ia 076 stay."""
        calendar = self.by_passage[PASSAGE_CALENDAR]
        remainder = self.by_passage[PASSAGE_REMAINDER]
        cb_lines = self.by_passage[PASSAGE_CB]
        aa = self.by_passage[PASSAGE_AA]
        ab = self.by_passage[PASSAGE_AB]
        br = self.by_passage[PASSAGE_BR]
        bv = self.by_passage[PASSAGE_BV]
        ia = self.by_passage[PASSAGE_IA]

        aa_profile = score_aa_repeating_ngrams(aa, self.analyzer)
        self.assertEqual(sum(len(line) for line in aa), AA_STEM_TOTAL)
        self.assertEqual(aa_profile.longest_n, AA_LONGEST_N)
        self.assertEqual(aa_profile.longest[0].tokens, AA_LONGEST_NGRAM)
        self.assertEqual(aa_profile.top_8gram.tokens, AA_TOP_8GRAM)
        self.assertEqual(len(find_ngram_hits(aa, MOTIF_10GRAM)), STANDING_AA_MOTIF_FREQ)

        ab_profile = score_ab_repeating_ngrams(ab, self.analyzer)
        self.assertEqual(sum(len(line) for line in ab), AB_STEM_TOTAL)
        self.assertEqual(ab_profile.longest_n, AB_LONGEST_N)
        self.assertEqual(ab_profile.longest[0].tokens, AB_LONGEST_NGRAM)
        self.assertEqual(len(find_ngram_hits(ab, MOTIF_AB_9GRAM)), STANDING_AB_MOTIF_FREQ)

        br_profile = score_br_repeating_ngrams(br, self.analyzer)
        self.assertEqual(sum(len(line) for line in br), BR_STEM_TOTAL)
        self.assertEqual(br_profile.longest_n, BR_LONGEST_N)
        self.assertEqual(br_profile.longest[0].tokens, BR_LONGEST_NGRAM)
        self.assertIsNone(br_profile.top_8gram)

        bv_profile = score_bv_repeating_ngrams(bv, self.analyzer)
        self.assertEqual(sum(len(line) for line in bv), BV_STEM_TOTAL)
        self.assertEqual(bv_profile.longest_n, BV_LONGEST_N)
        self.assertEqual(bv_profile.longest[0].tokens, BV_8GRAM)
        self.assertEqual(len(find_ngram_hits(bv, BV_8GRAM)), 2)

        self.assertTrue(find_ngram_hits(calendar, DELIMITER_MOTIF))
        self.assertEqual(find_ngram_hits(remainder, DELIMITER_MOTIF), [])
        self.assertEqual(find_ngram_hits(cb_lines, DELIMITER_MOTIF), [])
        self.assertEqual(find_ngram_hits(calendar, MOTIF_9GRAM), [])
        self.assertEqual(len(find_ngram_hits(remainder, MOTIF_9GRAM)), 2)
        self.assertEqual(find_ngram_hits(cb_lines, MOTIF_9GRAM), [])

        self.assertEqual(find_ngram_hits(calendar, SANDWICH), [])
        self.assertEqual(find_ngram_hits(remainder, SANDWICH), [])
        self.assertEqual(find_ngram_hits(cb_lines, SANDWICH), [])
        self.assertEqual(find_ngram_hits(aa, SANDWICH), [])
        self.assertEqual(len(find_ngram_hits(ab, SANDWICH)), 3)
        self.assertEqual(find_ngram_hits(br, SANDWICH), [])
        self.assertEqual(find_ngram_hits(bv, SANDWICH), [])
        self.assertEqual(find_ngram_hits(ia, SANDWICH), [])

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
        ia_profile = score_ia_repeating_ngrams(ia, self.analyzer)
        inventory = score_ia_076_inventory(ia)
        cells = score_ia_076_cells(ia)
        self.assertEqual(rem_profile.longest_n, CA_REMAINDER_LONGEST_N)
        self.assertEqual(len(rem_profile.eightgrams), CA_REMAINDER_EIGHTGRAM_COUNT)
        self.assertEqual(cb_profile.longest_n, CB_LONGEST_N)
        self.assertEqual(len(cb_profile.eightgrams), CB_EIGHTGRAM_COUNT)
        self.assertEqual(CB_EIGHTGRAM_COUNT, 0)
        self.assertEqual(
            tuple(row.tokens for row in cb_profile.longest),
            tuple(tokens for tokens, _n, _freq, _spans in STANDING_LONGEST_NGRAMS),
        )
        self.assertEqual(ia_profile.longest_n, IA_AS_STEM_LONGEST_N)
        self.assertEqual(ia_profile.longest[0].tokens, IA_AS_STEM_LONGEST_NGRAM)
        self.assertEqual(inventory.count, STANDING_076_COUNT)
        self.assertEqual(cells.cell_count, STANDING_CELL_COUNT)
        self.assertEqual(cells.empty_count, STANDING_EMPTY_CELL_COUNT)
        self.assertEqual(cells.length_median, STANDING_LENGTH_MEDIAN)
        self.assertEqual(cells.top_lengths, STANDING_TOP_LENGTHS)
        self.assertEqual(sum(line.count("999") for line in ia), STANDING_999_STEM_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-50 076 rate table."""
        lock = self.survey["stem_076_rate_per_fixture"]
        self.assertEqual(lock["cycle"], 50)
        self.assertEqual(lock["stem"], STEM_076)
        self.assertEqual(lock["threshold"], RATE_THRESHOLD)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(lock["only_ia_ge_threshold"], STANDING_ONLY_IA_GE_THRESHOLD)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        locked = tuple(
            (
                passage,
                hits,
                stems,
                (hits / stems) if stems else 0.0,
                ge_threshold,
            )
            for passage, hits, stems, ge_threshold in lock["table"]
        )
        self.assertEqual(locked, STANDING_TABLE)
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_ia_999_locks_unchanged"])
        self.assertTrue(lock["standing_ia_076_locks_unchanged"])
        self.assertTrue(lock["standing_ia_076_cells_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["santiago_ia_076_cells"]["cycle"], 49)
        self.assertEqual(self.survey["santiago_ia_076_inventory"]["cycle"], 48)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIa076RateImageSnapshot(unittest.TestCase):
    """Cycle 50 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
