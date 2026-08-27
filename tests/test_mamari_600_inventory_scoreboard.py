"""600 inventory lock: hits, flanks, motif membership, calendar adjacency.

Cycle 40 text-search lock. Uses only the already-vendored fixtures:
Ca calendar, Ca remainder, Cb, Aa, Ab. No invented Barthel. No other
tablet. No G00n→Barthel map. No type merge. No detector retune. No CV.

For every 600 stem hit: tablet/side, line, index, one published token
on each side (or line-edge), whether the index sits inside a locked
motif (Guy window / Ca 9-gram / Aa 10-gram / Ab 9-gram), and whether
it is window-adjacent on the calendar (last token facing a Guy window,
or first token of a cell after one). Totals per fixture. Stems are
ids only. No meanings.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from collections import Counter
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
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
    STANDING_600_HITS as CB_600_HITS,
    STANDING_STEM_TOTAL as CB_STEM_TOTAL,
    cb_line_stems,
    extract_cb_published_tokens,
    load_vendored_cb_html,
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
    STANDING_600_HITS as REMAINDER_600_HITS,
    STANDING_REMAINDER_STEM_TOTAL,
    cell_table,
    extract_ca_published_tokens,
    find_ngram_hits,
    hit_is_window_adjacent,
    load_corpus_survey,
    load_vendored_ca_html,
    published_windows,
    remainder_line_stems,
    stem_hits,
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

STEM_600 = "600"
PASSAGE_CALENDAR = "ca6_ca9_calendar"
PASSAGE_REMAINDER = "ca_side_a_remainder"
PASSAGE_CB = "tablet_c_side_b"
PASSAGE_AA = "tablet_a_tahua_side_a"
PASSAGE_AB = "tablet_a_tahua_side_b"
PASSAGE_ORDER = (
    PASSAGE_CALENDAR,
    PASSAGE_REMAINDER,
    PASSAGE_CB,
    PASSAGE_AA,
    PASSAGE_AB,
)
STANDING_CALENDAR_STEM_TOTAL = 101
STANDING_COUNTS = {
    PASSAGE_CALENDAR: 2,
    PASSAGE_REMAINDER: 5,
    PASSAGE_CB: 2,
    PASSAGE_AA: 23,
    PASSAGE_AB: 32,
}
STANDING_TOTAL = 64
STANDING_INSIDE_GUY = 0
STANDING_INSIDE_CA_9GRAM = 0
STANDING_INSIDE_AA_10GRAM = 0
STANDING_INSIDE_AB_9GRAM = 2
STANDING_CALENDAR_WINDOW_ADJACENT = 2
STANDING_CALENDAR_HITS = (("Ca7", 32), ("Ca8", 23))
STANDING_AB_MOTIF_600_HITS = (("Ab3", 5), ("Ab5", 16))
# (passage, tablet, side, line, index, before, after,
#  inside_guy, inside_ca_9gram, inside_aa_10gram, inside_ab_9gram,
#  calendar_window_adjacent)
STANDING_HITS = (
    (PASSAGE_CALENDAR, "C", "a", "Ca7", 32, "152", "390", False, False, False, False, True),
    (PASSAGE_CALENDAR, "C", "a", "Ca8", 23, "711", "040", False, False, False, False, True),
    (PASSAGE_REMAINDER, "C", "a", "Ca1", 14, "290", "001", False, False, False, False, False),
    (PASSAGE_REMAINDER, "C", "a", "Ca1", 17, "007", "385", False, False, False, False, False),
    (PASSAGE_REMAINDER, "C", "a", "Ca2", 8, "225", "755", False, False, False, False, False),
    (PASSAGE_REMAINDER, "C", "a", "Ca5", 23, "007", "001", False, False, False, False, False),
    (PASSAGE_REMAINDER, "C", "a", "Ca6", 19, "070", "773", False, False, False, False, False),
    (PASSAGE_CB, "C", "b", "Cb2", 21, "001", "064", False, False, False, False, False),
    (PASSAGE_CB, "C", "b", "Cb10", 29, "004", "003", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa2", 101, "004", "741", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 0, LINE_EDGE, "060", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 6, "003", "004", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 9, "061", "004", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 23, "631", "075", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 25, "075", "007", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 29, "631", "075", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 32, "008", "007", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 37, "700", "075", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa3", 39, "075", "007", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa4", 3, "004", "007", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa4", 76, "073", "004", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa4", 81, "004", "007", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa4", 99, "074", "004", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa4", 110, "004", "040", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa4", 113, "004", LINE_EDGE, False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa5", 15, "670", "755", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa5", 30, "608", "366", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa5", 89, "008", "446", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa6", 59, "200", "300", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa6", 81, "064", "200", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa8", 7, "205", "025", False, False, False, False, False),
    (PASSAGE_AA, "A", "a", "Aa8", 113, "631", "593", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab1", 6, "020", "007", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab1", 66, "091", "001", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab1", 81, "091", "001", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab1", 88, "020", "007", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab1", 99, "091", "001", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab2", 29, "003", "060", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab2", 32, "003", "060", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab2", 35, "003", "666", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab2", 37, "666", "060", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab2", 40, "003", "004", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab2", 98, "660", "603", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab2", 102, "306", "007", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab3", 5, "004", "004", False, False, False, True, False),
    (PASSAGE_AB, "A", "b", "Ab3", 33, "003", "003", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab3", 49, "007", "630", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab3", 63, "003", "003", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab3", 116, "070", "022", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab4", 68, "065", "065", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab4", 70, "065", "065", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab5", 16, "004", "004", False, False, False, True, False),
    (PASSAGE_AB, "A", "b", "Ab5", 56, "007", "445", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab5", 106, "008", "074", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab6", 24, "741", "742", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab6", 39, "005", "048", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab7", 17, "004", "004", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab7", 43, "055", "002", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab7", 60, "742", "360", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab8", 42, "006", "144", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab8", 45, "008", "001", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab8", 78, "001", "007", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab8", 91, "004", "461", False, False, False, False, False),
    (PASSAGE_AB, "A", "b", "Ab8", 96, "002", "001", False, False, False, False, False),
)


@dataclass(frozen=True)
class PassageSpec:
    """One already-vendored fixture. Search only; no scrape."""

    passage: str
    tablet: str
    side: str
    lines: list
    line_names: tuple[str, ...]
    calendar_adjacent: bool = False


@dataclass(frozen=True)
class Stem600Hit:
    """One 600 stem hit. Id only; no meaning."""

    passage: str
    tablet: str
    side: str
    line: str
    index: int
    before: str | None
    after: str | None
    inside_guy_window: bool
    inside_ca_9gram: bool
    inside_aa_10gram: bool
    inside_ab_9gram: bool
    calendar_window_adjacent: bool


@dataclass(frozen=True)
class Stem600Inventory:
    """Full 600 inventory on the five existing fixtures."""

    hits: tuple[Stem600Hit, ...]
    counts: dict[str, int]


def inventory_row(hit: Stem600Hit) -> tuple:
    """Stable lock row: passage, tablet/side, line, index, flanks, motifs, adj."""
    return (
        hit.passage,
        hit.tablet,
        hit.side,
        hit.line,
        hit.index,
        hit.before,
        hit.after,
        hit.inside_guy_window,
        hit.inside_ca_9gram,
        hit.inside_aa_10gram,
        hit.inside_ab_9gram,
        hit.calendar_window_adjacent,
    )


def motif_cover(
    lines: list[list[str]],
    line_names: tuple[str, ...],
    motif: tuple[str, ...],
) -> set[tuple[str, int]]:
    """(line, index) covered by any exact motif hit. Search only."""
    covered: set[tuple[str, int]] = set()
    n = len(motif)
    for line_index, start in find_ngram_hits(lines, motif):
        name = line_names[line_index]
        for offset in range(n):
            covered.add((name, start + offset))
    return covered


def score_passage_600(spec: PassageSpec, stem: str = STEM_600) -> tuple[Stem600Hit, ...]:
    """600 hits on one passage with flanks and motif flags. Search only."""
    guy = motif_cover(spec.lines, spec.line_names, DELIMITER_MOTIF)
    ca9 = motif_cover(spec.lines, spec.line_names, MOTIF_9GRAM)
    aa10 = motif_cover(spec.lines, spec.line_names, MOTIF_10GRAM)
    ab9 = motif_cover(spec.lines, spec.line_names, MOTIF_AB_9GRAM)
    windows = ()
    cells = ()
    if spec.calendar_adjacent:
        windows = published_windows(spec.lines, line_names=spec.line_names)
        cells = cell_table(spec.lines, windows, spec.line_names)
    hits: list[Stem600Hit] = []
    for line, index in stem_hits(spec.lines, stem, line_names=spec.line_names):
        sequence = spec.lines[spec.line_names.index(line)]
        before, after = hit_flanks(sequence, index, 1)
        adjacent = False
        if spec.calendar_adjacent:
            adjacent = hit_is_window_adjacent(line, index, cells, windows)
        key = (line, index)
        hits.append(
            Stem600Hit(
                passage=spec.passage,
                tablet=spec.tablet,
                side=spec.side,
                line=line,
                index=index,
                before=before,
                after=after,
                inside_guy_window=key in guy,
                inside_ca_9gram=key in ca9,
                inside_aa_10gram=key in aa10,
                inside_ab_9gram=key in ab9,
                calendar_window_adjacent=adjacent,
            )
        )
    return tuple(hits)


def score_600_inventory(passages: tuple[PassageSpec, ...] | list[PassageSpec]) -> Stem600Inventory:
    """Concatenate per-passage 600 rows. Search only."""
    hits = tuple(hit for spec in passages for hit in score_passage_600(spec))
    counts = {spec.passage: 0 for spec in passages}
    for hit in hits:
        counts[hit.passage] += 1
    return Stem600Inventory(hits=hits, counts=counts)


def existing_passage_specs() -> tuple[PassageSpec, ...]:
    """The five already-vendored fixtures. No new tablet."""
    return (
        PassageSpec(
            PASSAGE_CALENDAR,
            "C",
            "a",
            fixture_line_stems(load_mamari_fixture()),
            CALENDAR_LINE_NAMES,
            calendar_adjacent=True,
        ),
        PassageSpec(
            PASSAGE_REMAINDER,
            "C",
            "a",
            remainder_line_stems(extract_ca_published_tokens(load_vendored_ca_html())),
            REMAINDER_LINE_NAMES,
        ),
        PassageSpec(
            PASSAGE_CB,
            "C",
            "b",
            cb_line_stems(extract_cb_published_tokens(load_vendored_cb_html())),
            CB_LINE_NAMES,
        ),
        PassageSpec(
            PASSAGE_AA,
            "A",
            "a",
            aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html())),
            AA_LINE_NAMES,
        ),
        PassageSpec(
            PASSAGE_AB,
            "A",
            "b",
            ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html())),
            AB_LINE_NAMES,
        ),
    )


class TestStem600InventoryHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_flanks_medial_and_line_edge(self):
        """Medial 600 keeps neighbors; start/end of line is LINE_EDGE."""
        lines = [["600", "040"], ["152", "600", "390"]]
        spec = PassageSpec("syn", "X", "a", lines, ("L0", "L1"))
        provider = MockProvider()
        rows = tuple(inventory_row(hit) for hit in score_passage_600(spec))
        self.assertEqual(
            rows,
            (
                ("syn", "X", "a", "L0", 0, LINE_EDGE, "040", False, False, False, False, False),
                ("syn", "X", "a", "L1", 1, "152", "390", False, False, False, False, False),
            ),
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_inside_locked_motif_only_when_span_covers(self):
        """600 inside the Ab 9-gram is flagged; a lone 600 is not."""
        motif = MOTIF_AB_9GRAM
        lines = [list(motif), ["600", "040", "600"]]
        spec = PassageSpec("syn", "A", "b", lines, ("L0", "L1"))
        provider = MockProvider()
        hits = score_passage_600(spec)
        self.assertEqual(stem_hits(lines, STEM_600, ("L0", "L1")), (("L0", 3), ("L1", 0), ("L1", 2)))
        self.assertEqual(motif[STANDING_600_SLOT], STEM_600)
        self.assertTrue(hits[0].inside_ab_9gram)
        self.assertFalse(hits[1].inside_ab_9gram)
        self.assertFalse(hits[2].inside_ab_9gram)
        self.assertFalse(any(hit.inside_guy_window for hit in hits))
        self.assertFalse(any(hit.inside_ca_9gram for hit in hits))
        self.assertFalse(any(hit.inside_aa_10gram for hit in hits))
        self.assertEqual(provider.get_call_history(), [])

    def test_calendar_window_adjacent_last_facing_and_first_after(self):
        """Last facing Guy / first after Guy; no window is not adjacent."""
        motif = DELIMITER_MOTIF
        lines = [["152", "600"] + list(motif) + ["600", "040"], ["600"]]
        names = ("L0", "L1")
        spec = PassageSpec("cal", "C", "a", lines, names, calendar_adjacent=True)
        provider = MockProvider()
        hits = score_passage_600(spec)
        self.assertEqual([(hit.line, hit.index) for hit in hits], [("L0", 1), ("L0", 10), ("L1", 0)])
        self.assertTrue(hits[0].calendar_window_adjacent)
        self.assertTrue(hits[1].calendar_window_adjacent)
        self.assertFalse(hits[2].calendar_window_adjacent)
        self.assertFalse(any(hit.inside_guy_window for hit in hits))
        empty = PassageSpec("off", "C", "a", [["600", "040"]], ("L0",))
        lone = score_passage_600(empty)
        self.assertEqual(len(lone), 1)
        self.assertFalse(lone[0].calendar_window_adjacent)
        self.assertEqual(provider.get_call_history(), [])

    def test_empty_passage_and_per_fixture_counts(self):
        """No 600 is an empty table; counts follow the passage list."""
        empty = PassageSpec("e", "C", "a", [["040", "010"]], ("L0",))
        filled = PassageSpec("f", "A", "a", [["600"], ["004", "600"]], ("L0", "L1"))
        provider = MockProvider()
        inventory = score_600_inventory((empty, filled))
        self.assertEqual(inventory.counts, {"e": 0, "f": 2})
        self.assertEqual(len(inventory.hits), 2)
        self.assertEqual(score_passage_600(empty), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamari600InventoryScoreboard(unittest.TestCase):
    """Cited-fixture 600 inventory lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.passages = existing_passage_specs()
        self.inventory = score_600_inventory(self.passages)
        self.rows = tuple(inventory_row(hit) for hit in self.inventory.hits)
        self.by_passage = {spec.passage: spec for spec in self.passages}

    def test_uses_existing_fixtures_only(self):
        """Five already-vendored passages; no other tablet is scraped."""
        self.assertEqual(tuple(spec.passage for spec in self.passages), PASSAGE_ORDER)
        self.assertEqual(
            sum(len(line) for line in self.by_passage[PASSAGE_CALENDAR].lines),
            STANDING_CALENDAR_STEM_TOTAL,
        )
        self.assertEqual(
            sum(len(line) for line in self.by_passage[PASSAGE_REMAINDER].lines),
            STANDING_REMAINDER_STEM_TOTAL,
        )
        self.assertEqual(
            sum(len(line) for line in self.by_passage[PASSAGE_CB].lines),
            CB_STEM_TOTAL,
        )
        self.assertEqual(
            sum(len(line) for line in self.by_passage[PASSAGE_AA].lines),
            AA_STEM_TOTAL,
        )
        self.assertEqual(
            sum(len(line) for line in self.by_passage[PASSAGE_AB].lines),
            AB_STEM_TOTAL,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_full_600_hit_table(self):
        """Every 600 hit locks tablet/side, line, index, flanks, motifs, adj."""
        self.assertEqual(self.rows, STANDING_HITS)
        self.assertEqual(len(self.rows), STANDING_TOTAL)
        self.assertEqual(len(self.inventory.hits), STANDING_TOTAL)
        for hit in self.inventory.hits:
            sequence = self.by_passage[hit.passage].lines[
                self.by_passage[hit.passage].line_names.index(hit.line)
            ]
            self.assertEqual(sequence[hit.index], STEM_600)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_fixture_counts(self):
        """Calendar 2, remainder 5, Cb 2, Aa 23, Ab 32."""
        self.assertEqual(self.inventory.counts, STANDING_COUNTS)
        counted = Counter(hit.passage for hit in self.inventory.hits)
        self.assertEqual(dict(counted), STANDING_COUNTS)
        self.assertEqual(sum(STANDING_COUNTS.values()), STANDING_TOTAL)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_known_600_facts(self):
        """Calendar window-adjacent; remainder/Cb locations; Ab 9-gram slot 3."""
        calendar = [hit for hit in self.inventory.hits if hit.passage == PASSAGE_CALENDAR]
        self.assertEqual(tuple((hit.line, hit.index) for hit in calendar), STANDING_CALENDAR_HITS)
        self.assertTrue(all(hit.calendar_window_adjacent for hit in calendar))
        self.assertEqual(sum(hit.calendar_window_adjacent for hit in self.inventory.hits), STANDING_CALENDAR_WINDOW_ADJACENT)

        remainder = [hit for hit in self.inventory.hits if hit.passage == PASSAGE_REMAINDER]
        self.assertEqual(tuple((hit.line, hit.index) for hit in remainder), REMAINDER_600_HITS)
        self.assertFalse(any(hit.calendar_window_adjacent for hit in remainder))
        self.assertFalse(any(hit.inside_ca_9gram for hit in remainder))

        cb = [hit for hit in self.inventory.hits if hit.passage == PASSAGE_CB]
        self.assertEqual(tuple((hit.line, hit.index) for hit in cb), CB_600_HITS)

        ab_motif = [
            (hit.line, hit.index)
            for hit in self.inventory.hits
            if hit.inside_ab_9gram
        ]
        self.assertEqual(tuple(ab_motif), STANDING_AB_MOTIF_600_HITS)
        for line, start, end in STANDING_AB_MOTIF_SPANS:
            self.assertEqual(end - start, len(MOTIF_AB_9GRAM))
            self.assertIn((line, start + STANDING_600_SLOT), STANDING_AB_MOTIF_600_HITS)

        self.assertEqual(sum(hit.inside_guy_window for hit in self.inventory.hits), STANDING_INSIDE_GUY)
        self.assertEqual(sum(hit.inside_ca_9gram for hit in self.inventory.hits), STANDING_INSIDE_CA_9GRAM)
        self.assertEqual(sum(hit.inside_aa_10gram for hit in self.inventory.hits), STANDING_INSIDE_AA_10GRAM)
        self.assertEqual(sum(hit.inside_ab_9gram for hit in self.inventory.hits), STANDING_INSIDE_AB_9GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_scoreboards_still_compute(self):
        """Guy / Ca 9-gram / Aa 10-gram / Ab 9-gram / Cb 5-grams stay."""
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
        """CORPUS_SURVEY.json records the cycle-40 600 inventory."""
        lock = self.survey["stem_600_inventory"]
        self.assertEqual(lock["cycle"], 40)
        self.assertEqual(lock["stem"], STEM_600)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(lock["total"], STANDING_TOTAL)
        self.assertEqual(lock["counts"], STANDING_COUNTS)
        self.assertEqual(lock["inside_guy_window"], STANDING_INSIDE_GUY)
        self.assertEqual(lock["inside_ca_9gram"], STANDING_INSIDE_CA_9GRAM)
        self.assertEqual(lock["inside_aa_10gram"], STANDING_INSIDE_AA_10GRAM)
        self.assertEqual(lock["inside_ab_9gram"], STANDING_INSIDE_AB_9GRAM)
        self.assertEqual(lock["calendar_window_adjacent"], STANDING_CALENDAR_WINDOW_ADJACENT)
        self.assertEqual(
            [tuple(hit) for hit in lock["hits"]],
            list(STANDING_HITS),
        )
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["cycle"], 39)
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["cycle"], 37)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamari600InventoryImageSnapshot(unittest.TestCase):
    """Cycle 40 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
