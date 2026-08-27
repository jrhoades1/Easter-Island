"""Remainder 002…002 n=9 wrap family: overlap with the 9-gram motif.

Cycle 31 text-search lock. Uses the already-vendored Kohaumotu Ca.html
remainder (cycle 28) and the cycle-30 wrap finder. No invented Barthel.
No Cb.html scrape. No G00n→Barthel map. No type merge. No detector
retune. No CV.

Locks every remainder n=9 window that starts and ends with 002: line,
span, nine tokens, whether it is the motif, how many positions match
the motif, and which interior stems appear in both the wrap and the
motif. Bookend 002 is not counted as a shared interior stem and is not
called a delimiter.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_calendar_scoreboard import (
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import (
    MOTIF_9GRAM,
    STANDING_REMAINDER_WRAP_COUNT,
    STANDING_REMAINDER_WRAPS,
    WRAP_N,
    WRAP_STEM,
    WrapHit,
    score_002_wraps,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    REMAINDER_LINE_NAMES,
    extract_ca_published_tokens,
    load_corpus_survey,
    load_vendored_ca_html,
    remainder_line_stems,
)

MOTIF_INTERIOR = MOTIF_9GRAM[1:-1]


@dataclass(frozen=True)
class WrapFamilyRow:
    """One remainder wrap plus motif overlap. Stems only; no meanings."""

    tokens: tuple[str, ...]
    line: str
    start: int
    end: int
    is_motif: bool
    position_matches: int
    shared_interior_stems: tuple[str, ...]
    shares_interior_stem: bool


def wrap_interior(tokens: tuple[str, ...]) -> tuple[str, ...]:
    """Tokens between the 002 bookends. Search only."""
    return tokens[1:-1]


def position_match_count(
    tokens: tuple[str, ...],
    motif: tuple[str, ...] = MOTIF_9GRAM,
) -> int:
    """How many of the nine aligned positions equal the motif."""
    return sum(left == right for left, right in zip(tokens, motif, strict=True))


def shared_interior_stems(
    tokens: tuple[str, ...],
    motif: tuple[str, ...] = MOTIF_9GRAM,
    bookend: str = WRAP_STEM,
) -> tuple[str, ...]:
    """Motif-order unique interior stems also in the wrap interior.

    Bookend 002 is excluded even if it sits inside a wrap.
    """
    wrap_set = set(wrap_interior(tokens))
    seen: set[str] = set()
    shared: list[str] = []
    for stem in wrap_interior(motif):
        if stem == bookend or stem in seen or stem not in wrap_set:
            continue
        seen.add(stem)
        shared.append(stem)
    return tuple(shared)


def score_wrap_family(
    wraps: tuple[WrapHit, ...],
    motif: tuple[str, ...] = MOTIF_9GRAM,
) -> tuple[WrapFamilyRow, ...]:
    """Overlap table for every wrap against the motif. Search only."""
    rows: list[WrapFamilyRow] = []
    for wrap in wraps:
        shared = shared_interior_stems(wrap.tokens, motif)
        rows.append(
            WrapFamilyRow(
                tokens=wrap.tokens,
                line=wrap.line,
                start=wrap.start,
                end=wrap.end,
                is_motif=wrap.is_motif,
                position_matches=position_match_count(wrap.tokens, motif),
                shared_interior_stems=shared,
                shares_interior_stem=bool(shared),
            )
        )
    return tuple(rows)


def family_tuple(row: WrapFamilyRow) -> tuple:
    """Stable lock row: tokens, line, span, is_motif, matches, shared, shares."""
    return (
        row.tokens,
        row.line,
        row.start,
        row.end,
        row.is_motif,
        row.position_matches,
        row.shared_interior_stems,
        row.shares_interior_stem,
    )


def wraps_sharing_interior(rows: tuple[WrapFamilyRow, ...]) -> int:
    """How many wraps share any non-bookend interior stem with the motif."""
    return sum(1 for row in rows if row.shares_interior_stem)


def other_wraps_sharing_interior(rows: tuple[WrapFamilyRow, ...]) -> int:
    """Non-motif wraps that share any non-bookend interior stem."""
    return sum(1 for row in rows if row.shares_interior_stem and not row.is_motif)


# (tokens, line, start, end, is_motif, position_matches, shared_interior, shares)
STANDING_WRAP_FAMILY = (
    (
        ("002", "002", "200", "215", "002", "010", "002", "005", "002"),
        "Ca9",
        16,
        25,
        False,
        2,
        ("010",),
        True,
    ),
    (
        ("002", "010", "070", "760", "040", "006", "400", "002", "002"),
        "Ca10",
        18,
        27,
        False,
        7,
        ("010", "070", "760", "040", "006"),
        True,
    ),
    (MOTIF_9GRAM, "Ca10", 26, 35, True, 9, MOTIF_INTERIOR, True),
    (MOTIF_9GRAM, "Ca11", 14, 23, True, 9, MOTIF_INTERIOR, True),
    (
        ("002", "004", "760", "002", "002", "004", "760", "002", "002"),
        "Ca11",
        22,
        31,
        False,
        2,
        ("760",),
        True,
    ),
    (
        ("002", "004", "760", "002", "002", "002", "004", "763", "002"),
        "Ca11",
        26,
        35,
        False,
        2,
        ("760",),
        True,
    ),
)
STANDING_WRAP_FAMILY_COUNT = 6
STANDING_WRAPS_SHARING_INTERIOR = 6
STANDING_OTHER_WRAPS_SHARING_INTERIOR = 4
STANDING_CALENDAR_WRAP_FAMILY = ()


class TestRemainder002WrapFamilyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_motif_matches_itself_on_all_nine_positions(self):
        """The motif row is 9 positional matches and the full interior set."""
        provider = MockProvider()
        wrap = WrapHit(MOTIF_9GRAM, "L0", 0, WRAP_N, True)
        row = score_wrap_family((wrap,))[0]
        self.assertEqual(row.position_matches, WRAP_N)
        self.assertEqual(row.shared_interior_stems, MOTIF_INTERIOR)
        self.assertTrue(row.shares_interior_stem)
        self.assertTrue(row.is_motif)
        self.assertNotIn(WRAP_STEM, row.shared_interior_stems)
        self.assertEqual(provider.get_call_history(), [])

    def test_bookend_002_in_interior_is_not_shared(self):
        """A mid-window 002 is not a shared interior stem with the motif."""
        other = ("002", "002", "999", "888", "777", "666", "555", "444", "002")
        provider = MockProvider()
        wrap = WrapHit(other, "L0", 0, WRAP_N, False)
        row = score_wrap_family((wrap,))[0]
        self.assertEqual(row.position_matches, 2)
        self.assertEqual(row.shared_interior_stems, ())
        self.assertFalse(row.shares_interior_stem)
        self.assertIn(WRAP_STEM, wrap_interior(other))
        self.assertNotIn(WRAP_STEM, MOTIF_INTERIOR)
        self.assertEqual(provider.get_call_history(), [])

    def test_shared_interior_uses_motif_order(self):
        """Overlap lists motif interior stems in motif order, unique."""
        other = ("002", "006", "760", "010", "760", "999", "010", "888", "002")
        provider = MockProvider()
        shared = shared_interior_stems(other)
        self.assertEqual(shared, ("010", "760", "006"))
        self.assertEqual(position_match_count(other), 2)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariRemainder002WrapFamilyScoreboard(unittest.TestCase):
    """Cited remainder 002…002 n=9 family lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        self.calendar = fixture_line_stems(load_mamari_fixture())
        self.remainder_wraps = score_002_wraps(
            self.remainder, REMAINDER_LINE_NAMES
        )
        self.family = score_wrap_family(self.remainder_wraps)
        self.calendar_family = score_wrap_family(
            score_002_wraps(self.calendar, CALENDAR_LINE_NAMES)
        )

    def test_family_is_the_six_remainder_wraps(self):
        """Six remainder wraps; same order and spans as the cycle-30 lock."""
        locked = tuple(family_tuple(row) for row in self.family)
        self.assertEqual(len(locked), STANDING_WRAP_FAMILY_COUNT)
        self.assertEqual(len(locked), STANDING_REMAINDER_WRAP_COUNT)
        self.assertEqual(locked, STANDING_WRAP_FAMILY)
        wrap_keys = tuple(
            (tokens, line, start, end, is_motif)
            for tokens, line, start, end, is_motif, _m, _s, _sh in locked
        )
        self.assertEqual(wrap_keys, STANDING_REMAINDER_WRAPS)
        self.assertTrue(
            all(row[0][0] == WRAP_STEM and row[0][-1] == WRAP_STEM for row in locked)
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_interior_overlap_counts(self):
        """All six wraps share a non-bookend interior stem with the motif."""
        self.assertEqual(
            wraps_sharing_interior(self.family),
            STANDING_WRAPS_SHARING_INTERIOR,
        )
        self.assertEqual(
            other_wraps_sharing_interior(self.family),
            STANDING_OTHER_WRAPS_SHARING_INTERIOR,
        )
        self.assertEqual(STANDING_WRAPS_SHARING_INTERIOR, STANDING_WRAP_FAMILY_COUNT)
        self.assertEqual(STANDING_OTHER_WRAPS_SHARING_INTERIOR, 4)
        self.assertTrue(all(row.shares_interior_stem for row in self.family))
        self.assertTrue(all(WRAP_STEM not in row.shared_interior_stems for row in self.family))
        motif_rows = tuple(row for row in self.family if row.is_motif)
        other_rows = tuple(row for row in self.family if not row.is_motif)
        self.assertEqual(len(motif_rows), 2)
        self.assertEqual(len(other_rows), 4)
        self.assertEqual(
            tuple(row.position_matches for row in motif_rows),
            (9, 9),
        )
        self.assertEqual(
            tuple(row.shared_interior_stems for row in other_rows),
            (("010",), ("010", "070", "760", "040", "006"), ("760",), ("760",)),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_calendar_has_no_wrap_family(self):
        """Calendar Ca6–Ca9 still has no 002…002 n=9 wrap."""
        self.assertEqual(
            tuple(family_tuple(row) for row in self.calendar_family),
            STANDING_CALENDAR_WRAP_FAMILY,
        )
        self.assertEqual(wraps_sharing_interior(self.calendar_family), 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-31 wrap-family lock."""
        lock = self.survey["remainder_002_wrap_family"]
        self.assertEqual(lock["cycle"], 31)
        self.assertEqual(lock["wrap_n"], WRAP_N)
        self.assertEqual(lock["bookend_stem"], WRAP_STEM)
        self.assertEqual(lock["motif_tokens"], list(MOTIF_9GRAM))
        self.assertEqual(lock["wrap_count"], STANDING_WRAP_FAMILY_COUNT)
        self.assertEqual(
            [
                (
                    tuple(tokens),
                    line,
                    start,
                    end,
                    is_motif,
                    position_matches,
                    tuple(shared),
                    shares,
                )
                for tokens, line, start, end, is_motif, position_matches, shared, shares
                in lock["wraps"]
            ],
            list(STANDING_WRAP_FAMILY),
        )
        self.assertEqual(
            lock["wraps_sharing_interior_stem"],
            STANDING_WRAPS_SHARING_INTERIOR,
        )
        self.assertEqual(
            lock["other_wraps_sharing_interior_stem"],
            STANDING_OTHER_WRAPS_SHARING_INTERIOR,
        )
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariRemainder002WrapFamilyImageSnapshot(unittest.TestCase):
    """Cycle 31 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
