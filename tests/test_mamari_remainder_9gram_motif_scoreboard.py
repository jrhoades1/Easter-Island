"""Remainder 9-gram motif lock: hits, flanks, wraps, calendar-absent.

Cycle 30 text-search lock. Uses the already-vendored Kohaumotu Ca.html
remainder (cycle 28) AND the existing 101-stem Ca6–Ca9 calendar fixture.
No invented Barthel. No Cb.html scrape. No G00n→Barthel map. No type
merge. No detector retune. No CV.

The cycle-29 longest remainder n-gram is locked as a motif: exact
9-gram hits, exact 8-prefix hits, one published token on each side of
every hit (or line-edge), and every n=9 002…002 wrap on both fixtures.
The motif is absent from the calendar passage.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_calendar_scoreboard import (
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_LONGEST_NGRAM,
    STANDING_LONGEST_SPANS,
    STANDING_TOP_8GRAM,
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

MOTIF_9GRAM = STANDING_LONGEST_NGRAM
PREFIX_8GRAM = STANDING_TOP_8GRAM
WRAP_N = 9
WRAP_STEM = "002"
LINE_EDGE = None

# (line, start, end, before, after) — after/before is LINE_EDGE at a line end.
STANDING_REMAINDER_MOTIF_HITS = (
    ("Ca10", 26, 35, "002", "290"),
    ("Ca11", 14, 23, "290", "004"),
)
STANDING_REMAINDER_PREFIX8_HITS = (
    ("Ca10", 26, 34, "002", "002"),
    ("Ca11", 14, 22, "290", "002"),
)
# (tokens, line, start, end, is_motif)
STANDING_REMAINDER_WRAPS = (
    (("002", "002", "200", "215", "002", "010", "002", "005", "002"), "Ca9", 16, 25, False),
    (("002", "010", "070", "760", "040", "006", "400", "002", "002"), "Ca10", 18, 27, False),
    (MOTIF_9GRAM, "Ca10", 26, 35, True),
    (MOTIF_9GRAM, "Ca11", 14, 23, True),
    (("002", "004", "760", "002", "002", "004", "760", "002", "002"), "Ca11", 22, 31, False),
    (("002", "004", "760", "002", "002", "002", "004", "763", "002"), "Ca11", 26, 35, False),
)
STANDING_REMAINDER_WRAP_COUNT = 6
STANDING_REMAINDER_OTHER_WRAP_COUNT = 4
STANDING_CALENDAR_MOTIF_HITS = ()
STANDING_CALENDAR_PREFIX8_HITS = ()
STANDING_CALENDAR_WRAPS = ()
STANDING_CALENDAR_WRAP_COUNT = 0
STANDING_CALENDAR_ABSENT = True


@dataclass(frozen=True)
class MotifHit:
    """One exact n-gram hit with one-token flanks. Stems only; no meanings."""

    line: str
    start: int
    end: int
    before: str | None
    after: str | None


@dataclass(frozen=True)
class WrapHit:
    """One n=9 window that starts and ends with 002. Stems only."""

    tokens: tuple[str, ...]
    line: str
    start: int
    end: int
    is_motif: bool


@dataclass(frozen=True)
class MotifScore:
    """9-gram / 8-prefix / wrap snapshot on one published fixture."""

    motif_hits: tuple[MotifHit, ...]
    prefix_hits: tuple[MotifHit, ...]
    wraps: tuple[WrapHit, ...]


def hit_tuple(hit: MotifHit) -> tuple:
    """Stable lock row: line, [start, end), before, after."""
    return (hit.line, hit.start, hit.end, hit.before, hit.after)


def wrap_tuple(hit: WrapHit) -> tuple:
    """Stable lock row: tokens, line, [start, end), is_motif."""
    return (hit.tokens, hit.line, hit.start, hit.end, hit.is_motif)


def hit_flanks(
    sequence: list[str],
    start: int,
    n: int,
) -> tuple[str | None, str | None]:
    """Token immediately before and after [start, start+n), or LINE_EDGE."""
    before = sequence[start - 1] if start > 0 else LINE_EDGE
    end = start + n
    after = sequence[end] if end < len(sequence) else LINE_EDGE
    return before, after


def score_motif_hits(
    lines: list[list[str]],
    gram: tuple[str, ...],
    line_names: tuple[str, ...],
) -> tuple[MotifHit, ...]:
    """Exact hits of gram with one-token flanks. Search only."""
    n = len(gram)
    hits: list[MotifHit] = []
    for line_index, start in find_ngram_hits(lines, gram):
        before, after = hit_flanks(lines[line_index], start, n)
        hits.append(
            MotifHit(
                line=line_names[line_index],
                start=start,
                end=start + n,
                before=before,
                after=after,
            )
        )
    return tuple(hits)


def score_002_wraps(
    lines: list[list[str]],
    line_names: tuple[str, ...],
    n: int = WRAP_N,
    stem: str = WRAP_STEM,
    motif: tuple[str, ...] = MOTIF_9GRAM,
) -> tuple[WrapHit, ...]:
    """Every n-window that starts and ends with stem. Search only."""
    wraps: list[WrapHit] = []
    for line_index, sequence in enumerate(lines):
        for start in range(len(sequence) - n + 1):
            tokens = tuple(sequence[start : start + n])
            if tokens[0] != stem or tokens[-1] != stem:
                continue
            wraps.append(
                WrapHit(
                    tokens=tokens,
                    line=line_names[line_index],
                    start=start,
                    end=start + n,
                    is_motif=tokens == motif,
                )
            )
    return tuple(wraps)


def score_9gram_motif(
    lines: list[list[str]],
    line_names: tuple[str, ...],
    motif: tuple[str, ...] = MOTIF_9GRAM,
    prefix: tuple[str, ...] = PREFIX_8GRAM,
) -> MotifScore:
    """Hits, 8-prefix hits, and 002…002 wraps on one fixture."""
    return MotifScore(
        motif_hits=score_motif_hits(lines, motif, line_names),
        prefix_hits=score_motif_hits(lines, prefix, line_names),
        wraps=score_002_wraps(lines, line_names, motif=motif),
    )


class TestRemainder9gramMotifHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_flanks_medial_and_line_edge(self):
        """Medial hits keep neighbors; start/end of line is LINE_EDGE."""
        motif = MOTIF_9GRAM
        prefix = PREFIX_8GRAM
        lines = [list(motif), ["X"] + list(motif) + ["Y"]]
        names = ("L0", "L1")
        provider = MockProvider()
        score = score_9gram_motif(lines, names)
        self.assertEqual(
            tuple(hit_tuple(hit) for hit in score.motif_hits),
            (
                ("L0", 0, 9, LINE_EDGE, LINE_EDGE),
                ("L1", 1, 10, "X", "Y"),
            ),
        )
        self.assertEqual(
            tuple(hit_tuple(hit) for hit in score.prefix_hits),
            (
                ("L0", 0, 8, LINE_EDGE, "002"),
                ("L1", 1, 9, "X", "002"),
            ),
        )
        self.assertEqual(prefix, motif[:-1])
        self.assertEqual(provider.get_call_history(), [])

    def test_wrap_other_than_motif_is_counted(self):
        """A different 002…002 n=9 window is a wrap, not the motif."""
        other = ("002", "111", "222", "333", "444", "555", "666", "777", "002")
        lines = [list(MOTIF_9GRAM), list(other)]
        provider = MockProvider()
        wraps = score_002_wraps(lines, ("L0", "L1"))
        self.assertEqual(len(wraps), 2)
        self.assertTrue(wraps[0].is_motif)
        self.assertFalse(wraps[1].is_motif)
        self.assertEqual(wraps[1].tokens, other)
        self.assertEqual(provider.get_call_history(), [])

    def test_empty_passage_is_absent(self):
        """A passage with no 002 has no motif, prefix, or wrap."""
        lines = [["040", "010", "040", "030"], ["040", "040"]]
        provider = MockProvider()
        score = score_9gram_motif(lines, ("C0", "C1"))
        self.assertEqual(score.motif_hits, ())
        self.assertEqual(score.prefix_hits, ())
        self.assertEqual(score.wraps, ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariRemainder9gramMotifScoreboard(unittest.TestCase):
    """Cited remainder + calendar 9-gram motif lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        self.calendar = fixture_line_stems(load_mamari_fixture())
        self.remainder_score = score_9gram_motif(
            self.remainder, REMAINDER_LINE_NAMES
        )
        self.calendar_score = score_9gram_motif(
            self.calendar, CALENDAR_LINE_NAMES
        )

    def test_checks_both_published_fixtures(self):
        """Remainder 416 stems and calendar 101 stems are both scored."""
        self.assertEqual(sum(len(line) for line in self.remainder), 416)
        self.assertEqual(sum(len(line) for line in self.calendar), 101)
        self.assertEqual(tuple(CALENDAR_LINE_NAMES), ("Ca6", "Ca7", "Ca8", "Ca9"))
        self.assertNotEqual(self.remainder, self.calendar)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remainder_motif_hits_and_flanks(self):
        """9-gram hits are Ca10[26:35] / Ca11[14:23] with published flanks."""
        hits = tuple(hit_tuple(hit) for hit in self.remainder_score.motif_hits)
        self.assertEqual(hits, STANDING_REMAINDER_MOTIF_HITS)
        self.assertEqual(
            tuple((line, start, end) for line, start, end, _before, _after in hits),
            STANDING_LONGEST_SPANS,
        )
        self.assertEqual(MOTIF_9GRAM, STANDING_LONGEST_NGRAM)
        self.assertEqual(len(hits), 2)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remainder_prefix8_hits_and_flanks(self):
        """8-prefix hits share the 9-gram starts; after-token is the wrap 002."""
        hits = tuple(hit_tuple(hit) for hit in self.remainder_score.prefix_hits)
        self.assertEqual(hits, STANDING_REMAINDER_PREFIX8_HITS)
        self.assertEqual(PREFIX_8GRAM, STANDING_TOP_8GRAM)
        self.assertEqual(PREFIX_8GRAM, MOTIF_9GRAM[:-1])
        motif_starts = [(line, start) for line, start, _end, _b, _a in STANDING_REMAINDER_MOTIF_HITS]
        prefix_starts = [(line, start) for line, start, _end, _b, _a in hits]
        self.assertEqual(prefix_starts, motif_starts)
        after_tokens = [after for _line, _start, _end, _before, after in hits]
        self.assertEqual(after_tokens, ["002", "002"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_remainder_002_wraps_at_n9(self):
        """Six 002…002 n=9 wraps; four are not the motif."""
        wraps = tuple(wrap_tuple(hit) for hit in self.remainder_score.wraps)
        self.assertEqual(wraps, STANDING_REMAINDER_WRAPS)
        self.assertEqual(len(wraps), STANDING_REMAINDER_WRAP_COUNT)
        other = tuple(row for row in wraps if not row[-1])
        motif = tuple(row for row in wraps if row[-1])
        self.assertEqual(len(other), STANDING_REMAINDER_OTHER_WRAP_COUNT)
        self.assertEqual(len(motif), 2)
        self.assertEqual(
            tuple(row[0] for row in motif),
            (MOTIF_9GRAM, MOTIF_9GRAM),
        )
        self.assertTrue(all(row[0][0] == WRAP_STEM and row[0][-1] == WRAP_STEM for row in wraps))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_calendar_motif_absent(self):
        """Calendar Ca6–Ca9 has no 9-gram, no 8-prefix, and no 002…002 n=9 wrap."""
        s = self.calendar_score
        self.assertEqual(tuple(hit_tuple(hit) for hit in s.motif_hits), STANDING_CALENDAR_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in s.prefix_hits), STANDING_CALENDAR_PREFIX8_HITS)
        self.assertEqual(tuple(wrap_tuple(hit) for hit in s.wraps), STANDING_CALENDAR_WRAPS)
        self.assertEqual(len(s.wraps), STANDING_CALENDAR_WRAP_COUNT)
        absent = not s.motif_hits and not s.prefix_hits and not s.wraps
        self.assertEqual(absent, STANDING_CALENDAR_ABSENT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-30 9-gram motif lock."""
        lock = self.survey["remainder_9gram_motif"]
        self.assertEqual(lock["cycle"], 30)
        self.assertEqual(lock["motif_tokens"], list(MOTIF_9GRAM))
        self.assertEqual(lock["prefix8_tokens"], list(PREFIX_8GRAM))
        self.assertEqual(
            [tuple(hit) for hit in lock["remainder_motif_hits"]],
            list(STANDING_REMAINDER_MOTIF_HITS),
        )
        self.assertEqual(
            [tuple(hit) for hit in lock["remainder_prefix8_hits"]],
            list(STANDING_REMAINDER_PREFIX8_HITS),
        )
        self.assertEqual(lock["remainder_wrap_n9_count"], STANDING_REMAINDER_WRAP_COUNT)
        self.assertEqual(
            lock["remainder_wrap_n9_other_count"],
            STANDING_REMAINDER_OTHER_WRAP_COUNT,
        )
        self.assertEqual(
            [
                (tuple(tokens), line, start, end)
                for tokens, line, start, end in lock["remainder_wrap_n9_other"]
            ],
            [
                (tokens, line, start, end)
                for tokens, line, start, end, is_motif in STANDING_REMAINDER_WRAPS
                if not is_motif
            ],
        )
        self.assertEqual(lock["calendar_motif_hits"], [])
        self.assertEqual(lock["calendar_prefix8_hits"], [])
        self.assertEqual(lock["calendar_wrap_n9_count"], STANDING_CALENDAR_WRAP_COUNT)
        self.assertTrue(lock["calendar_absent"])
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariRemainder9gramMotifImageSnapshot(unittest.TestCase):
    """Cycle 30 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
