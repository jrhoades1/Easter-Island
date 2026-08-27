"""Santiago Ia inter-076 cells: count, lengths, empty, 090|076|071, top tuples.

Cycle 49 text-search lock. Uses the already-vendored Kohaumotu Ia.html
fixture (cycle 46). Raw stems; 999 is kept as a stem. No invented
Barthel. No Ib scrape. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents.

A cell is the token sequence between consecutive 076s on the same
line, plus a leading cell before the first 076 and a trailing cell
after the last, per line. A line with no 076 is one cell covering
the line. Empty leading/trailing/interior cells are kept. 076 is a
stem id only — not a list marker, delimiter, or punctuation.

Locks on Ia1–Ia14: cell count, length min/median/max and the top 5
lengths with counts, empty-cell count, how many exact 2-cell
patterns 090 |076| 071 exist, and the three most common non-empty
cell token tuples (count, then earliest tuple). Stems are ids only.
No meanings.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from collections import Counter
from dataclasses import dataclass
from statistics import median

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_600_sandwich_scoreboard import SANDWICH
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
from tests.test_mamari_santiago_ia_076_inventory_scoreboard import (
    STANDING_076_COUNT,
    STANDING_076_INSIDE,
    STANDING_076_LEFT_TOP,
    STANDING_076_LINE_COUNTS,
    STANDING_076_RIGHT_TOP,
    STANDING_076_WRAP_COUNT,
    STANDING_076_WRAP_EXISTS,
    STEM_076,
    neighbor_top_row,
    score_ia_076_inventory,
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

CELL_LEFT = "090"
CELL_RIGHT = "071"
EXACT_PAIR = (CELL_LEFT, CELL_RIGHT)
TOP_LENGTHS_N = 5
TOP_NONEMPTY_N = 3

STANDING_CELL_COUNT = 578
STANDING_EMPTY_CELL_COUNT = 17
STANDING_LENGTH_MIN = 0
STANDING_LENGTH_MEDIAN = 3
STANDING_LENGTH_MAX = 11
STANDING_TOP_LENGTHS = ((3, 203), (4, 138), (1, 66), (2, 63), (5, 47))
STANDING_EXACT_090_076_071 = 1
STANDING_TOP_NONEMPTY = (
    (("071",), 6),
    (("011",), 5),
    (("001",), 4),
)


@dataclass(frozen=True)
class Stem076Cell:
    """One inter-076 token span. Ids only; no meanings."""

    line: str
    start: int
    end: int
    tokens: tuple[str, ...]
    length: int


@dataclass(frozen=True)
class Stem076CellProfile:
    """Inter-076 cell snapshot on raw Ia stems. 999 is kept."""

    cells: tuple[Stem076Cell, ...]
    cell_count: int
    empty_count: int
    length_min: int
    length_median: float
    length_max: int
    top_lengths: tuple[tuple[int, int], ...]
    exact_090_076_071: int
    top_nonempty: tuple[tuple[tuple[str, ...], int], ...]


def ia_076_cells(
    lines: list[list[str]],
    line_names: tuple[str, ...] = IA_LINE_NAMES,
    stem: str = STEM_076,
) -> tuple[Stem076Cell, ...]:
    """Partition each line into cells around stem 076. Search only."""
    cells: list[Stem076Cell] = []
    for name, sequence in zip(line_names, lines):
        hits = [index for index, token in enumerate(sequence) if token == stem]
        starts = [0] + [index + 1 for index in hits]
        ends = hits + [len(sequence)]
        for start, end in zip(starts, ends):
            tokens = tuple(sequence[start:end])
            cells.append(
                Stem076Cell(
                    line=name,
                    start=start,
                    end=end,
                    tokens=tokens,
                    length=end - start,
                )
            )
    return tuple(cells)


def exact_090_076_071_count(cells: tuple[Stem076Cell, ...] | list[Stem076Cell]) -> int:
    """Count adjacent cells that are exactly 090 |076| 071. Search only."""
    count = 0
    for left, right in zip(cells, cells[1:]):
        if left.line != right.line:
            continue
        if left.tokens == (CELL_LEFT,) and right.tokens == (CELL_RIGHT,):
            count += 1
    return count


def top_lengths(
    cells: tuple[Stem076Cell, ...] | list[Stem076Cell],
    n: int = TOP_LENGTHS_N,
) -> tuple[tuple[int, int], ...]:
    """Most common cell lengths, then earliest length. Search only."""
    hist = Counter(cell.length for cell in cells)
    ranked = sorted(hist.items(), key=lambda item: (-item[1], item[0]))
    return tuple(ranked[:n])


def top_nonempty_cells(
    cells: tuple[Stem076Cell, ...] | list[Stem076Cell],
    n: int = TOP_NONEMPTY_N,
) -> tuple[tuple[tuple[str, ...], int], ...]:
    """Most common non-empty token tuples, then earliest tuple. Search only."""
    hist = Counter(cell.tokens for cell in cells if cell.tokens)
    ranked = sorted(hist.items(), key=lambda item: (-item[1], item[0]))
    return tuple(ranked[:n])


def score_ia_076_cells(lines: list[list[str]]) -> Stem076CellProfile:
    """Inter-076 cells on raw Ia stems. 999 is kept."""
    cells = ia_076_cells(lines)
    lengths = [cell.length for cell in cells]
    return Stem076CellProfile(
        cells=cells,
        cell_count=len(cells),
        empty_count=sum(1 for length in lengths if length == 0),
        length_min=min(lengths) if lengths else 0,
        length_median=median(lengths) if lengths else 0,
        length_max=max(lengths) if lengths else 0,
        top_lengths=top_lengths(cells),
        exact_090_076_071=exact_090_076_071_count(cells),
        top_nonempty=top_nonempty_cells(cells),
    )


class TestSantiagoIa076CellHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_cells_partition_line_around_076(self):
        """Leading, inter-076, and trailing cells; empty when flush or doubled."""
        lines = [[] for _ in IA_LINE_NAMES]
        lines[0] = ["090", "076", "071", "011", "076", "001"]
        lines[1] = ["076", "076"]
        lines[2] = ["430", "011"]
        provider = MockProvider()
        cells = ia_076_cells(lines)
        ia1 = [cell for cell in cells if cell.line == "Ia1"]
        ia2 = [cell for cell in cells if cell.line == "Ia2"]
        ia3 = [cell for cell in cells if cell.line == "Ia3"]
        self.assertEqual(
            [(cell.start, cell.end, cell.tokens, cell.length) for cell in ia1],
            [
                (0, 1, ("090",), 1),
                (2, 4, ("071", "011"), 2),
                (5, 6, ("001",), 1),
            ],
        )
        self.assertEqual(
            [(cell.start, cell.end, cell.tokens) for cell in ia2],
            [(0, 0, ()), (1, 1, ()), (2, 2, ())],
        )
        self.assertEqual(ia3, [Stem076Cell("Ia3", 0, 2, ("430", "011"), 2)])
        self.assertTrue(all(STEM_076 not in cell.tokens for cell in cells))
        self.assertEqual(exact_090_076_071_count(ia1), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_exact_pair_and_top_nonempty_tiebreak(self):
        """090 |076| 071 counts singleton cells; ties take the earliest tuple."""
        lines = [[] for _ in IA_LINE_NAMES]
        lines[0] = ["090", "076", "071", "076", "071"]
        lines[1] = ["011", "076", "001", "076", "430"]
        lines[2] = ["011"]
        provider = MockProvider()
        profile = score_ia_076_cells(lines)
        self.assertEqual(profile.exact_090_076_071, 1)
        self.assertEqual(exact_090_076_071_count(profile.cells), 1)
        self.assertEqual(
            top_nonempty_cells(profile.cells),
            ((("011",), 2), (("001",), 1), (("071",), 1)),
        )
        self.assertEqual(profile.top_nonempty[0], (("011",), 2))
        self.assertEqual(profile.empty_count, 1)
        self.assertEqual(profile.cell_count, 3 + 3 + 1 + (len(IA_LINE_NAMES) - 3))
        self.assertEqual(top_lengths(profile.cells)[0][0], 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIa076CellScoreboard(unittest.TestCase):
    """Cited Ia.html inter-076 cell lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.html = load_vendored_ia_html()
        self.published = extract_ia_published_tokens(self.html)
        self.lines = ia_line_stems(self.published)
        self.profile = score_ia_076_cells(self.lines)
        self.inventory = score_ia_076_inventory(self.lines)
        self.as_stem = score_ia_repeating_ngrams(self.lines, self.analyzer)

    def test_cell_count_empty_and_lengths(self):
        """578 cells; 17 empty; lengths min 0 / median 3 / max 11; top 5."""
        prof = self.profile
        self.assertEqual(prof.cell_count, STANDING_CELL_COUNT)
        self.assertEqual(len(prof.cells), STANDING_CELL_COUNT)
        self.assertEqual(prof.empty_count, STANDING_EMPTY_CELL_COUNT)
        self.assertEqual(self.inventory.count, STANDING_076_COUNT)
        self.assertEqual(self.inventory.line_counts, STANDING_076_LINE_COUNTS)
        self.assertEqual(prof.cell_count, STANDING_076_COUNT + len(IA_LINE_NAMES))
        self.assertEqual(prof.length_min, STANDING_LENGTH_MIN)
        self.assertEqual(prof.length_median, STANDING_LENGTH_MEDIAN)
        self.assertEqual(prof.length_max, STANDING_LENGTH_MAX)
        self.assertEqual(prof.top_lengths, STANDING_TOP_LENGTHS)
        self.assertTrue(all(STEM_076 not in cell.tokens for cell in prof.cells))
        self.assertEqual(sum(len(line) for line in self.lines), IA_STEM_TOTAL)
        self.assertEqual(sum(line.count(STEM_999) for line in self.lines), STANDING_999_STEM_COUNT)
        for name, sequence in zip(IA_LINE_NAMES, self.lines):
            rebuilt: list[str] = []
            line_cells = [cell for cell in prof.cells if cell.line == name]
            rebuilt.extend(line_cells[0].tokens)
            for cell in line_cells[1:]:
                rebuilt.append(STEM_076)
                rebuilt.extend(cell.tokens)
            self.assertEqual(rebuilt, sequence)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_exact_090_076_071_and_top_nonempty(self):
        """One exact 090 |076| 071 pair; top tuples 071 / 011 / 001."""
        prof = self.profile
        self.assertEqual(prof.exact_090_076_071, STANDING_EXACT_090_076_071)
        self.assertEqual(EXACT_PAIR, (STANDING_076_LEFT_TOP[0], STANDING_076_RIGHT_TOP[0]))
        self.assertEqual(neighbor_top_row(self.inventory.left_top, self.inventory.right_top), (
            STANDING_076_LEFT_TOP[0],
            STANDING_076_LEFT_TOP[1],
            STANDING_076_RIGHT_TOP[0],
            STANDING_076_RIGHT_TOP[1],
        ))
        self.assertEqual(prof.top_nonempty, STANDING_TOP_NONEMPTY)
        self.assertEqual(len(prof.top_nonempty), TOP_NONEMPTY_N)
        self.assertTrue(all(tokens for tokens, _count in prof.top_nonempty))
        self.assertFalse((IA_HTML_DIR / "Ib.html").exists())
        self.assertTrue(IA_HTML_PATH.is_file())
        self.assertTrue(I_INDEX_HTML_PATH.is_file())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_a_b_c_and_ia_scoreboards_still_compute(self):
        """Aa / Ab / Br / Bv / Guy / Ca 9-gram / sandwich / Ia 076 stay."""
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
        self.assertEqual(self.as_stem.longest[0].spans, IA_AS_STEM_LONGEST_SPANS)
        self.assertEqual(len(self.as_stem.eightgrams), IA_EIGHTGRAM_COUNT)
        self.assertEqual(self.inventory.inside, STANDING_076_INSIDE)
        self.assertEqual(self.inventory.wrap_exists, STANDING_076_WRAP_EXISTS)
        self.assertEqual(self.inventory.wrap_count, STANDING_076_WRAP_COUNT)
        self.assertEqual(STANDING_SPLIT_LONGEST_N, 5)
        self.assertEqual(len(STANDING_SPLIT_LONGEST_NGRAMS), 4)
        self.assertEqual(tuple(BR_LINE_NAMES), tuple(f"Br{n}" for n in range(1, 11)))
        self.assertEqual(tuple(BV_LINE_NAMES), tuple(f"Bv{n}" for n in range(1, 13)))
        self.assertEqual(tuple(CB_LINE_NAMES), tuple(f"Cb{n}" for n in range(1, 15)))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-49 Ia inter-076 cells."""
        lock = self.survey["santiago_ia_076_cells"]
        self.assertEqual(lock["cycle"], 49)
        self.assertEqual(lock["passage"], "tablet_i_santiago_staff")
        self.assertEqual(lock["stem"], STEM_076)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertEqual(lock["cell_count"], STANDING_CELL_COUNT)
        self.assertEqual(lock["empty_count"], STANDING_EMPTY_CELL_COUNT)
        self.assertEqual(lock["length_min"], STANDING_LENGTH_MIN)
        self.assertEqual(lock["length_median"], STANDING_LENGTH_MEDIAN)
        self.assertEqual(lock["length_max"], STANDING_LENGTH_MAX)
        locked_lengths = tuple(tuple(row) for row in lock["top_lengths"])
        self.assertEqual(locked_lengths, STANDING_TOP_LENGTHS)
        self.assertEqual(lock["exact_090_076_071"], STANDING_EXACT_090_076_071)
        locked_top = tuple((tuple(tokens), count) for tokens, count in lock["top_nonempty"])
        self.assertEqual(locked_top, STANDING_TOP_NONEMPTY)
        self.assertFalse(lock["ib_html"])
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
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIa076CellImageSnapshot(unittest.TestCase):
    """Cycle 49 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
