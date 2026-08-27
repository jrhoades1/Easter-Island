"""600 sandwich lock: 004 600 004 hits and per-fixture neighbor tops.

Cycle 41 text-search lock. Uses only the already-vendored fixtures
and the cycle-40 600 inventory: Ca calendar, Ca remainder, Cb, Aa, Ab.
No invented Barthel. No other tablet. No G00n→Barthel map. No type
merge. No detector retune. No CV.

Locks every exact 004 600 004 hit (line, [start, end), whether that
hit is the Ab 9-gram 600 slot). Also locks the top left-neighbor and
top right-neighbor of 600 per fixture (stem, count). Line-edge is
not a stem. Equal counts break by earliest stem id. Stems are ids
only. No meanings.
Cycle 42 locks the Ab7 sandwich 9-window Hamming vs
the Ab 9-gram motif.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from collections import Counter
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
    STANDING_AB_MOTIF_600_HITS,
    STANDING_CALENDAR_STEM_TOTAL,
    STANDING_COUNTS,
    STANDING_TOTAL,
    STEM_600,
    PassageSpec,
    existing_passage_specs,
    score_600_inventory,
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
from tests.test_mamari_cb_side_b_scoreboard import STANDING_STEM_TOTAL as CB_STEM_TOTAL
from tests.test_mamari_remainder_9gram_motif_scoreboard import LINE_EDGE, MOTIF_9GRAM
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
    STANDING_REMAINDER_STEM_TOTAL,
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
    STANDING_STEM_TOTAL as AA_STEM_TOTAL,
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
)

SANDWICH = ("004", "600", "004")
# (passage, tablet, side, line, start, end, ab_9gram_slot)
STANDING_SANDWICH_HITS = (
    (PASSAGE_AB, "A", "b", "Ab3", 4, 7, True),
    (PASSAGE_AB, "A", "b", "Ab5", 15, 18, True),
    (PASSAGE_AB, "A", "b", "Ab7", 16, 19, False),
)
STANDING_SANDWICH_COUNTS = {
    PASSAGE_CALENDAR: 0,
    PASSAGE_REMAINDER: 0,
    PASSAGE_CB: 0,
    PASSAGE_AA: 0,
    PASSAGE_AB: 3,
}
STANDING_SANDWICH_TOTAL = 3
STANDING_SANDWICH_AB_9GRAM_SLOT = 2
# (left_stem, left_count, right_stem, right_count) — line-edge excluded.
STANDING_NEIGHBOR_TOPS = {
    PASSAGE_CALENDAR: ("152", 1, "040", 1),
    PASSAGE_REMAINDER: ("007", 2, "001", 2),
    PASSAGE_CB: ("001", 1, "003", 1),
    PASSAGE_AA: ("004", 5, "007", 5),
    PASSAGE_AB: ("003", 6, "001", 5),
}


@dataclass(frozen=True)
class SandwichHit:
    """One 004 600 004 hit. Ids only; no meaning."""

    passage: str
    tablet: str
    side: str
    line: str
    start: int
    end: int
    ab_9gram_slot: bool


@dataclass(frozen=True)
class NeighborTop:
    """Top 600 neighbor on one side. Stem id and count."""

    stem: str | None
    count: int


@dataclass(frozen=True)
class SandwichLock:
    """Sandwich table plus per-fixture 600 neighbor tops."""

    hits: tuple[SandwichHit, ...]
    counts: dict[str, int]
    neighbor_tops: dict[str, tuple[NeighborTop, NeighborTop]]


def sandwich_row(hit: SandwichHit) -> tuple:
    """Stable lock row: passage, tablet/side, line, [start, end), slot."""
    return (
        hit.passage,
        hit.tablet,
        hit.side,
        hit.line,
        hit.start,
        hit.end,
        hit.ab_9gram_slot,
    )


def neighbor_top_row(left: NeighborTop, right: NeighborTop) -> tuple:
    """Stable lock row: left stem/count, right stem/count."""
    return (left.stem, left.count, right.stem, right.count)


def ab_9gram_slot_starts(
    lines: list[list[str]],
    line_names: tuple[str, ...],
) -> set[tuple[str, int]]:
    """Sandwich starts whose 600 is the Ab 9-gram slot-3 token."""
    starts: set[tuple[str, int]] = set()
    n = len(MOTIF_AB_9GRAM)
    for line_index, start in find_ngram_hits(lines, MOTIF_AB_9GRAM):
        starts.add((line_names[line_index], start + STANDING_600_SLOT - 1))
    assert n == 9
    return starts


def score_sandwich_hits(
    spec: PassageSpec,
    sandwich: tuple[str, ...] = SANDWICH,
) -> tuple[SandwichHit, ...]:
    """Exact 004 600 004 hits on one passage. Search only."""
    slots = ab_9gram_slot_starts(spec.lines, spec.line_names)
    hits: list[SandwichHit] = []
    n = len(sandwich)
    for line_index, start in find_ngram_hits(spec.lines, sandwich):
        name = spec.line_names[line_index]
        hits.append(
            SandwichHit(
                passage=spec.passage,
                tablet=spec.tablet,
                side=spec.side,
                line=name,
                start=start,
                end=start + n,
                ab_9gram_slot=(name, start) in slots,
            )
        )
    return tuple(hits)


def neighbor_counts(hits) -> tuple[Counter, Counter]:
    """Left/right stem counts of 600 hits. Line-edge is not a stem."""
    left: Counter = Counter()
    right: Counter = Counter()
    for hit in hits:
        if hit.before is not LINE_EDGE:
            left[hit.before] += 1
        if hit.after is not LINE_EDGE:
            right[hit.after] += 1
    return left, right


def top_neighbor(counts: Counter) -> NeighborTop:
    """Highest count, then earliest stem id. Empty is (None, 0)."""
    if not counts:
        return NeighborTop(None, 0)
    stem, count = min(counts.items(), key=lambda item: (-item[1], item[0]))
    return NeighborTop(stem, count)


def score_sandwich_lock(
    passages: tuple[PassageSpec, ...] | list[PassageSpec],
) -> SandwichLock:
    """Sandwich table and 600 neighbor tops on the existing inventory."""
    inventory = score_600_inventory(passages)
    hits = tuple(hit for spec in passages for hit in score_sandwich_hits(spec))
    counts = {spec.passage: 0 for spec in passages}
    for hit in hits:
        counts[hit.passage] += 1
    tops: dict[str, tuple[NeighborTop, NeighborTop]] = {}
    for spec in passages:
        passage_hits = [hit for hit in inventory.hits if hit.passage == spec.passage]
        left, right = neighbor_counts(passage_hits)
        tops[spec.passage] = (top_neighbor(left), top_neighbor(right))
    return SandwichLock(hits=hits, counts=counts, neighbor_tops=tops)


class TestStem600SandwichHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_sandwich_and_ab_9gram_slot_flag(self):
        """004 600 004 is flagged only when it is the Ab 9-gram 600 slot."""
        motif = MOTIF_AB_9GRAM
        lines = [list(motif), ["074", "004", "600", "004", "074"], ["004", "600"]]
        spec = PassageSpec("syn", "A", "b", lines, ("L0", "L1", "L2"))
        provider = MockProvider()
        rows = tuple(sandwich_row(hit) for hit in score_sandwich_hits(spec))
        self.assertEqual(
            rows,
            (
                ("syn", "A", "b", "L0", 2, 5, True),
                ("syn", "A", "b", "L1", 1, 4, False),
            ),
        )
        self.assertEqual(motif[STANDING_600_SLOT - 1 : STANDING_600_SLOT + 2], SANDWICH)
        self.assertEqual(provider.get_call_history(), [])

    def test_empty_passage_has_no_sandwich(self):
        """A passage without 004 600 004 is an empty table."""
        spec = PassageSpec("e", "C", "a", [["040", "600", "010"]], ("L0",))
        provider = MockProvider()
        self.assertEqual(score_sandwich_hits(spec), ())
        self.assertEqual(provider.get_call_history(), [])

    def test_neighbor_top_majority_tie_and_line_edge(self):
        """Majority wins; equal counts take the earlier stem; edge is dropped."""
        provider = MockProvider()
        majority = Counter({"004": 3, "003": 2})
        self.assertEqual(top_neighbor(majority), NeighborTop("004", 3))
        tied = Counter({"711": 1, "152": 1})
        self.assertEqual(top_neighbor(tied), NeighborTop("152", 1))
        self.assertEqual(top_neighbor(Counter()), NeighborTop(None, 0))
        lines = [["600", "040"], ["152", "600", "390"], ["711", "600", "040"]]
        spec = PassageSpec("syn", "C", "a", lines, ("L0", "L1", "L2"))
        lock = score_sandwich_lock((spec,))
        left, right = lock.neighbor_tops["syn"]
        self.assertEqual(neighbor_top_row(left, right), ("152", 1, "040", 2))
        self.assertEqual(lock.hits, ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamari600SandwichScoreboard(unittest.TestCase):
    """Cited-fixture 004 600 004 sandwich lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.passages = existing_passage_specs()
        self.lock = score_sandwich_lock(self.passages)
        self.rows = tuple(sandwich_row(hit) for hit in self.lock.hits)
        self.by_passage = {spec.passage: spec for spec in self.passages}
        self.inventory = score_600_inventory(self.passages)

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
        self.assertEqual(self.inventory.counts, STANDING_COUNTS)
        self.assertEqual(len(self.inventory.hits), STANDING_TOTAL)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_sandwich_table(self):
        """Every 004 600 004 hit locks line, span, and Ab 9-gram slot."""
        self.assertEqual(self.rows, STANDING_SANDWICH_HITS)
        self.assertEqual(len(self.rows), STANDING_SANDWICH_TOTAL)
        self.assertEqual(self.lock.counts, STANDING_SANDWICH_COUNTS)
        self.assertEqual(sum(STANDING_SANDWICH_COUNTS.values()), STANDING_SANDWICH_TOTAL)
        counted = Counter(hit.passage for hit in self.lock.hits)
        self.assertEqual(dict(counted), {PASSAGE_AB: STANDING_SANDWICH_TOTAL})
        for hit in self.lock.hits:
            sequence = self.by_passage[hit.passage].lines[
                self.by_passage[hit.passage].line_names.index(hit.line)
            ]
            self.assertEqual(tuple(sequence[hit.start : hit.end]), SANDWICH)
            self.assertEqual(sequence[hit.start + 1], STEM_600)
        slot_hits = tuple(
            (hit.line, hit.start + 1) for hit in self.lock.hits if hit.ab_9gram_slot
        )
        self.assertEqual(slot_hits, STANDING_AB_MOTIF_600_HITS)
        self.assertEqual(sum(hit.ab_9gram_slot for hit in self.lock.hits), STANDING_SANDWICH_AB_9GRAM_SLOT)
        for line, start, end in STANDING_AB_MOTIF_SPANS:
            self.assertEqual(end - start, len(MOTIF_AB_9GRAM))
            self.assertIn((line, start + STANDING_600_SLOT - 1, start + STANDING_600_SLOT + 2), [
                (hit.line, hit.start, hit.end) for hit in self.lock.hits if hit.ab_9gram_slot
            ])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_fixture_neighbor_tops(self):
        """Top left/right 600 neighbor per fixture: stem and count."""
        for passage, expected in STANDING_NEIGHBOR_TOPS.items():
            left, right = self.lock.neighbor_tops[passage]
            self.assertEqual(neighbor_top_row(left, right), expected)
        self.assertEqual(
            {passage: neighbor_top_row(*tops) for passage, tops in self.lock.neighbor_tops.items()},
            STANDING_NEIGHBOR_TOPS,
        )
        for spec in self.passages:
            hits = [hit for hit in self.inventory.hits if hit.passage == spec.passage]
            left, right = neighbor_counts(hits)
            self.assertEqual(top_neighbor(left).stem, STANDING_NEIGHBOR_TOPS[spec.passage][0])
            self.assertEqual(top_neighbor(left).count, STANDING_NEIGHBOR_TOPS[spec.passage][1])
            self.assertEqual(top_neighbor(right).stem, STANDING_NEIGHBOR_TOPS[spec.passage][2])
            self.assertEqual(top_neighbor(right).count, STANDING_NEIGHBOR_TOPS[spec.passage][3])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_scoreboards_still_compute(self):
        """Guy / Ca 9-gram / Aa 10-gram / Ab 9-gram / 600 inventory stay."""
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
        """CORPUS_SURVEY.json records the cycle-41 004 600 004 sandwich."""
        lock = self.survey["stem_600_sandwich"]
        self.assertEqual(lock["cycle"], 41)
        self.assertEqual(lock["sandwich"], list(SANDWICH))
        self.assertEqual(lock["stem"], STEM_600)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(lock["total"], STANDING_SANDWICH_TOTAL)
        self.assertEqual(lock["counts"], STANDING_SANDWICH_COUNTS)
        self.assertEqual(lock["ab_9gram_slot"], STANDING_SANDWICH_AB_9GRAM_SLOT)
        self.assertEqual([tuple(hit) for hit in lock["hits"]], list(STANDING_SANDWICH_HITS))
        tops = {
            passage: tuple(row)
            for passage, row in lock["neighbor_tops"].items()
        }
        self.assertEqual(tops, STANDING_NEIGHBOR_TOPS)
        self.assertEqual(self.survey["stem_600_inventory"]["cycle"], 40)
        self.assertEqual(self.survey["stem_600_inventory"]["total"], STANDING_TOTAL)
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["cycle"], 39)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamari600SandwichImageSnapshot(unittest.TestCase):
    """Cycle 41 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
