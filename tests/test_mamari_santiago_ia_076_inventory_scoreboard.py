"""Santiago Ia 076 inventory: count, neighbors, gram cover, n=5 wraps.

Cycle 48 text-search lock. Uses the already-vendored Kohaumotu Ia.html
fixture (cycle 46). Raw stems; 999 is kept as a stem. No invented
Barthel. No Ib scrape. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents.

Locks 076 on Ia1–Ia14: total count, per-line counts, top left/right
neighbors (line-edge is not a stem), how many 076 hits sit inside
each post-split 5-gram plus 999 071 076 010 079, and whether any
076…076 wrap exists at n=5. Stems are ids only. No meanings.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from collections import Counter
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_600_inventory_scoreboard import motif_cover
from tests.test_mamari_600_sandwich_scoreboard import (
    SANDWICH,
    NeighborTop,
    neighbor_top_row,
    top_neighbor,
)
from tests.test_mamari_aruku_br_scoreboard import (
    BR_LINE_NAMES,
    STANDING_LONGEST_N as BR_LONGEST_N,
    STANDING_LONGEST_NGRAM as BR_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as BR_STEM_TOTAL,
    br_line_stems,
    extract_br_published_tokens,
    load_vendored_br_html,
    score_br_repeating_ngrams,
)
from tests.test_mamari_aruku_bv_scoreboard import (
    BV_LINE_NAMES,
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
    CB_LINE_NAMES,
    cb_line_stems,
    extract_cb_published_tokens,
    load_vendored_cb_html,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import (
    LINE_EDGE,
    MOTIF_9GRAM,
    hit_flanks,
    score_002_wraps,
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
from tests.test_mamari_santiago_ia_999_scoreboard import (
    STANDING_999_STEM_COUNT,
    STANDING_SPLIT_LONGEST_N,
    STANDING_SPLIT_LONGEST_NGRAMS,
    STEM_999,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    REMAINDER_LINE_NAMES,
    extract_ca_published_tokens,
    find_ngram_hits,
    load_corpus_survey,
    load_vendored_ca_html,
    remainder_line_stems,
    stem_hits,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    IA_HTML_DIR,
    IA_HTML_PATH,
    IA_LINE_NAMES,
    I_INDEX_HTML_PATH,
    STANDING_EIGHTGRAM_COUNT as IA_EIGHTGRAM_COUNT,
    STANDING_LONGEST_FREQ as IA_AS_STEM_LONGEST_FREQ,
    STANDING_LONGEST_N as IA_AS_STEM_LONGEST_N,
    STANDING_LONGEST_NGRAM as IA_AS_STEM_LONGEST_NGRAM,
    STANDING_LONGEST_SPANS as IA_AS_STEM_LONGEST_SPANS,
    STANDING_STEM_TOTAL as IA_STEM_TOTAL,
    extract_ia_published_tokens,
    ia_line_stems,
    load_vendored_ia_html,
    score_ia_repeating_ngrams,
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
    STANDING_AB_MOTIF_SPANS,
)
from tests.test_mamari_tahua_ab_scoreboard import (
    AB_LINE_NAMES,
    STANDING_LONGEST_N as AB_LONGEST_N,
    STANDING_LONGEST_NGRAM as AB_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as AB_STEM_TOTAL,
    ab_line_stems,
    extract_ab_published_tokens,
    load_vendored_ab_html,
    score_ab_repeating_ngrams,
)

STEM_076 = "076"
WRAP_N = 5
GRAM_430 = ("430", "076", "006", "000", "076")
GRAM_010 = ("076", "010", "079", "006", "700")
GRAM_011 = ("076", "011", "090", "090", "076")
GRAM_400 = ("400", "070", "076", "020", "010")
GRAM_999 = IA_AS_STEM_LONGEST_NGRAM
LOCKED_GRAMS = (GRAM_430, GRAM_010, GRAM_011, GRAM_400, GRAM_999)
STANDING_076_COUNT = 564
STANDING_076_LINE_COUNTS = (40, 46, 34, 35, 37, 36, 43, 44, 40, 49, 39, 35, 47, 39)
STANDING_076_LEFT_TOP = ("090", 69)
STANDING_076_RIGHT_TOP = ("071", 43)
STANDING_076_INSIDE = (
    (GRAM_430, 4),
    (GRAM_010, 2),
    (GRAM_011, 4),
    (GRAM_400, 2),
    (GRAM_999, 3),
)
STANDING_076_WRAP_EXISTS = True
STANDING_076_WRAP_COUNT = 221


@dataclass(frozen=True)
class Stem076Inventory:
    """076 count, neighbors, gram cover, and n=5 wraps. Ids only."""

    count: int
    line_counts: tuple[int, ...]
    left_top: NeighborTop
    right_top: NeighborTop
    inside: tuple[tuple[tuple[str, ...], int], ...]
    wrap_exists: bool
    wrap_count: int


def ia_076_hits(lines: list[list[str]]) -> tuple[tuple[str, int], ...]:
    """(line, index) for every stem 076. Search only."""
    return stem_hits(lines, STEM_076, IA_LINE_NAMES)


def ia_076_line_counts(lines: list[list[str]]) -> tuple[int, ...]:
    """076 count per Ia line in Barthel order."""
    return tuple(line.count(STEM_076) for line in lines)


def ia_076_neighbor_tops(lines: list[list[str]]) -> tuple[NeighborTop, NeighborTop]:
    """Top left/right neighbors of 076. Line-edge is not a stem."""
    left: Counter[str] = Counter()
    right: Counter[str] = Counter()
    for name, index in ia_076_hits(lines):
        before, after = hit_flanks(lines[IA_LINE_NAMES.index(name)], index, 1)
        if before is not LINE_EDGE:
            left[before] += 1
        if after is not LINE_EDGE:
            right[after] += 1
    return top_neighbor(left), top_neighbor(right)


def ia_076_inside_grams(
    lines: list[list[str]],
    grams: tuple[tuple[str, ...], ...] = LOCKED_GRAMS,
) -> tuple[tuple[tuple[str, ...], int], ...]:
    """How many 076 hits sit inside each locked 5-gram. Search only."""
    hits = set(ia_076_hits(lines))
    return tuple(
        (gram, len(hits & motif_cover(lines, IA_LINE_NAMES, gram)))
        for gram in grams
    )


def ia_076_wraps(lines: list[list[str]]):
    """Every n=5 window that starts and ends with 076."""
    return score_002_wraps(
        lines, IA_LINE_NAMES, n=WRAP_N, stem=STEM_076, motif=GRAM_011
    )


def score_ia_076_inventory(lines: list[list[str]]) -> Stem076Inventory:
    """076 inventory on raw Ia stems. 999 is kept."""
    wraps = ia_076_wraps(lines)
    left, right = ia_076_neighbor_tops(lines)
    return Stem076Inventory(
        count=len(ia_076_hits(lines)),
        line_counts=ia_076_line_counts(lines),
        left_top=left,
        right_top=right,
        inside=ia_076_inside_grams(lines),
        wrap_exists=bool(wraps),
        wrap_count=len(wraps),
    )


class TestSantiagoIa076Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_count_line_counts_and_neighbor_tops(self):
        """076 totals follow the lines; edge is dropped; majority then id."""
        lines = [[] for _ in IA_LINE_NAMES]
        lines[0] = ["090", "076", "071", "090", "076", "011"]
        lines[1] = ["076", "071"]
        provider = MockProvider()
        self.assertEqual(ia_076_hits(lines), (("Ia1", 1), ("Ia1", 4), ("Ia2", 0)))
        self.assertEqual(ia_076_line_counts(lines)[:2], (2, 1))
        self.assertEqual(sum(ia_076_line_counts(lines)), 3)
        left, right = ia_076_neighbor_tops(lines)
        self.assertEqual(neighbor_top_row(left, right), ("090", 2, "071", 2))
        self.assertEqual(top_neighbor(Counter({"090": 2, "071": 2})).stem, "071")
        self.assertEqual(top_neighbor(Counter()), NeighborTop(None, 0))
        self.assertEqual(provider.get_call_history(), [])

    def test_inside_grams_and_n5_wraps(self):
        """Cover counts 076 inside a 5-gram; 076…076 at n=5 is a wrap."""
        lines = [[] for _ in IA_LINE_NAMES]
        lines[0] = list(GRAM_430)
        lines[3] = list(GRAM_999)
        lines[5] = list(GRAM_010)
        provider = MockProvider()
        inside = dict(ia_076_inside_grams(lines))
        self.assertEqual(inside[GRAM_430], 2)
        self.assertEqual(inside[GRAM_010], 1)
        self.assertEqual(inside[GRAM_999], 1)
        self.assertEqual(inside[GRAM_011], 0)
        self.assertEqual(inside[GRAM_400], 0)
        self.assertEqual(find_ngram_hits(lines, GRAM_999), [(3, 0)])
        self.assertIn(STEM_999, lines[3])
        wraps = ia_076_wraps(lines)
        self.assertFalse(wraps)
        lines[11] = list(GRAM_011)
        wraps = ia_076_wraps(lines)
        self.assertEqual(len(wraps), 1)
        self.assertEqual(wraps[0].tokens, GRAM_011)
        self.assertTrue(wraps[0].is_motif)
        self.assertEqual(bool(wraps), True)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIa076InventoryScoreboard(unittest.TestCase):
    """Cited Ia.html 076 inventory lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.html = load_vendored_ia_html()
        self.published = extract_ia_published_tokens(self.html)
        self.lines = ia_line_stems(self.published)
        self.inventory = score_ia_076_inventory(self.lines)
        self.as_stem = score_ia_repeating_ngrams(self.lines, self.analyzer)

    def test_076_count_line_counts_and_neighbor_tops(self):
        """564 stems; per-line totals; top left 090×69; top right 071×43."""
        inv = self.inventory
        self.assertEqual(inv.count, STANDING_076_COUNT)
        self.assertEqual(inv.line_counts, STANDING_076_LINE_COUNTS)
        self.assertEqual(sum(inv.line_counts), STANDING_076_COUNT)
        self.assertEqual(len(inv.line_counts), len(IA_LINE_NAMES))
        self.assertEqual(neighbor_top_row(inv.left_top, inv.right_top), (
            STANDING_076_LEFT_TOP[0],
            STANDING_076_LEFT_TOP[1],
            STANDING_076_RIGHT_TOP[0],
            STANDING_076_RIGHT_TOP[1],
        ))
        self.assertEqual(sum(len(line) for line in self.lines), IA_STEM_TOTAL)
        self.assertEqual(sum(line.count(STEM_999) for line in self.lines), STANDING_999_STEM_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_076_inside_locked_5grams_and_n5_wraps(self):
        """Inside counts: 4 / 2 / 4 / 2 / 3. 076…076 wraps at n=5 exist."""
        inv = self.inventory
        self.assertEqual(inv.inside, STANDING_076_INSIDE)
        self.assertEqual(LOCKED_GRAMS, tuple(gram for gram, _count in STANDING_076_INSIDE))
        self.assertEqual(GRAM_999, IA_AS_STEM_LONGEST_NGRAM)
        self.assertEqual(self.as_stem.longest[0].tokens, GRAM_999)
        self.assertEqual(self.as_stem.longest[0].spans, IA_AS_STEM_LONGEST_SPANS)
        self.assertEqual(inv.wrap_exists, STANDING_076_WRAP_EXISTS)
        self.assertTrue(STANDING_076_WRAP_EXISTS)
        self.assertEqual(inv.wrap_count, STANDING_076_WRAP_COUNT)
        self.assertGreater(inv.wrap_count, 0)
        wraps = ia_076_wraps(self.lines)
        self.assertEqual(len(wraps), STANDING_076_WRAP_COUNT)
        self.assertTrue(any(wrap.tokens == GRAM_011 for wrap in wraps))
        self.assertFalse((IA_HTML_DIR / "Ib.html").exists())
        self.assertTrue(IA_HTML_PATH.is_file())
        self.assertTrue(I_INDEX_HTML_PATH.is_file())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_a_b_c_and_ia_scoreboards_still_compute(self):
        """Aa / Ab / Br / Bv / Guy / Ca 9-gram / sandwich / Ia 999 stay."""
        aa = aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html()))
        ab = ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html()))
        br = br_line_stems(extract_br_published_tokens(load_vendored_br_html()))
        bv = bv_line_stems(extract_bv_published_tokens(load_vendored_bv_html()))
        calendar = fixture_line_stems(load_mamari_fixture())
        remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        cb_lines = cb_line_stems(extract_cb_published_tokens(load_vendored_cb_html()))

        aa_profile = score_aa_repeating_ngrams(aa, self.analyzer)
        self.assertEqual(sum(len(line) for line in aa), AA_STEM_TOTAL)
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

        ab_profile = score_ab_repeating_ngrams(ab, self.analyzer)
        self.assertEqual(sum(len(line) for line in ab), AB_STEM_TOTAL)
        self.assertEqual(ab_profile.longest_n, AB_LONGEST_N)
        self.assertEqual(ab_profile.longest[0].tokens, AB_LONGEST_NGRAM)
        ab_motif = find_ngram_hits(ab, MOTIF_AB_9GRAM)
        self.assertEqual(len(ab_motif), STANDING_AB_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AB_LINE_NAMES[line_index], start, start + len(MOTIF_AB_9GRAM))
                for line_index, start in ab_motif
            ),
            STANDING_AB_MOTIF_SPANS,
        )

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

        guy_cal = find_ngram_hits(calendar, DELIMITER_MOTIF)
        guy_rem = find_ngram_hits(remainder, DELIMITER_MOTIF)
        guy_cb = find_ngram_hits(cb_lines, DELIMITER_MOTIF)
        self.assertTrue(guy_cal)
        self.assertEqual(guy_rem, [])
        self.assertEqual(guy_cb, [])

        motif_cal = find_ngram_hits(calendar, MOTIF_9GRAM)
        motif_rem = find_ngram_hits(remainder, MOTIF_9GRAM)
        motif_cb = find_ngram_hits(cb_lines, MOTIF_9GRAM)
        self.assertEqual(motif_cal, [])
        self.assertEqual(len(motif_rem), 2)
        self.assertEqual(motif_cb, [])

        self.assertEqual(find_ngram_hits(calendar, SANDWICH), [])
        self.assertEqual(find_ngram_hits(remainder, SANDWICH), [])
        self.assertEqual(find_ngram_hits(cb_lines, SANDWICH), [])
        self.assertEqual(find_ngram_hits(aa, SANDWICH), [])
        self.assertEqual(len(find_ngram_hits(ab, SANDWICH)), 3)
        self.assertEqual(find_ngram_hits(br, SANDWICH), [])
        self.assertEqual(find_ngram_hits(bv, SANDWICH), [])
        self.assertEqual(find_ngram_hits(self.lines, SANDWICH), [])

        cross = score_cb_5gram_ca_cross(
            CB_5GRAMS,
            calendar,
            CALENDAR_LINE_NAMES,
            remainder,
            REMAINDER_LINE_NAMES,
        )
        locked = tuple((row.tokens, row.calendar_hits, row.remainder_hits) for row in cross)
        self.assertEqual(locked, STANDING_CA_CROSS_TABLE)
        for gram in CB_5GRAMS:
            self.assertTrue(find_ngram_hits(cb_lines, gram))

        rem_profile = score_remainder_repeating_ngrams(remainder, self.analyzer)
        cb_profile = score_cb_repeating_ngrams(cb_lines, self.analyzer)
        self.assertEqual(rem_profile.longest_n, CA_REMAINDER_LONGEST_N)
        self.assertEqual(len(rem_profile.eightgrams), CA_REMAINDER_EIGHTGRAM_COUNT)
        self.assertGreaterEqual(CA_REMAINDER_EIGHTGRAM_COUNT, 1)
        self.assertEqual(cb_profile.longest_n, CB_LONGEST_N)
        self.assertEqual(len(cb_profile.eightgrams), CB_EIGHTGRAM_COUNT)
        self.assertEqual(CB_EIGHTGRAM_COUNT, 0)
        self.assertEqual(
            tuple(row.tokens for row in cb_profile.longest),
            tuple(tokens for tokens, _n, _freq, _spans in STANDING_LONGEST_NGRAMS),
        )
        self.assertEqual(self.as_stem.longest_n, IA_AS_STEM_LONGEST_N)
        self.assertEqual(self.as_stem.longest[0].tokens, IA_AS_STEM_LONGEST_NGRAM)
        self.assertEqual(self.as_stem.longest[0].freq, IA_AS_STEM_LONGEST_FREQ)
        self.assertEqual(len(self.as_stem.eightgrams), IA_EIGHTGRAM_COUNT)
        self.assertEqual(STANDING_SPLIT_LONGEST_N, 5)
        self.assertEqual(len(STANDING_SPLIT_LONGEST_NGRAMS), 4)
        self.assertEqual(tuple(BR_LINE_NAMES), tuple(f"Br{n}" for n in range(1, 11)))
        self.assertEqual(tuple(BV_LINE_NAMES), tuple(f"Bv{n}" for n in range(1, 13)))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-48 Ia 076 inventory."""
        lock = self.survey["santiago_ia_076_inventory"]
        self.assertEqual(lock["cycle"], 48)
        self.assertEqual(lock["passage"], "tablet_i_santiago_staff")
        self.assertEqual(lock["stem"], STEM_076)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertEqual(lock["stem_count"], STANDING_076_COUNT)
        self.assertEqual(lock["line_counts"], list(STANDING_076_LINE_COUNTS))
        self.assertEqual(tuple(lock["left_top"]), STANDING_076_LEFT_TOP)
        self.assertEqual(tuple(lock["right_top"]), STANDING_076_RIGHT_TOP)
        locked_inside = tuple(
            (tuple(tokens), count) for tokens, count in lock["inside_5grams"]
        )
        self.assertEqual(locked_inside, STANDING_076_INSIDE)
        self.assertEqual(lock["wrap_n"], WRAP_N)
        self.assertEqual(lock["wrap_exists"], STANDING_076_WRAP_EXISTS)
        self.assertEqual(lock["wrap_count"], STANDING_076_WRAP_COUNT)
        self.assertFalse(lock["ib_html"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_ia_999_locks_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["santiago_ia_999_break"]["cycle"], 47)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIa076ImageSnapshot(unittest.TestCase):
    """Cycle 48 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
