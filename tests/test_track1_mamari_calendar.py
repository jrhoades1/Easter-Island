"""Track 1: Mamari Ca6–Ca9 lunar calendar as a search anchor.

Uses the vendored Barthel encodings only (Kohaumotu Ca.html via the
existing parsers, and the already-locked Ca6–Ca9 fixture). Does not
invent transcriptions, merge Barthel numbers, or assign new meanings.

MockProvider is constructed so this module cannot call an LLM. Glyph
readings below are either cited or marked hypothesis. Search lock,
not a translation.
"""

import random
import unittest
from dataclasses import dataclass

from agents.base.providers.mock_provider import MockProvider
from tests.test_mamari_040_run_profile_scoreboard import delimiter_and_variant_spans
from tests.test_mamari_aruku_br_scoreboard import BR_LINE_NAMES
from tests.test_mamari_aruku_bv_scoreboard import BV_LINE_NAMES
from tests.test_mamari_atua_vendor_scoreboard import RA_LINE_NAMES, RB_LINE_NAMES
from tests.test_mamari_boomerang_vendor_scoreboard import OA_LINE_NAMES
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_ca_c_only_scoreboard import CA_LINE_NAMES, load_c_sides
from tests.test_mamari_cb_side_b_scoreboard import CB_LINE_NAMES
from tests.test_mamari_chauvet_vendor_scoreboard import FA_LINE_NAMES, FB_LINE_NAMES
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_SIDES,
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_echancree_vendor_scoreboard import DA_LINE_NAMES, DB_LINE_NAMES
from tests.test_mamari_honolulu2_vendor_scoreboard import UA_LINE_NAMES
from tests.test_mamari_honolulu3_vendor_scoreboard import VA_LINE_NAMES
from tests.test_mamari_honolulu_vendor_scoreboard import TA_LINE_NAMES
from tests.test_mamari_keiti_vendor_scoreboard import ER_LINE_NAMES, EV_LINE_NAMES
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    HR_LINE_NAMES,
    HV_LINE_NAMES,
    PR_LINE_NAMES,
    PV_LINE_NAMES,
)
from tests.test_mamari_reimiro2_vendor_scoreboard import LA_LINE_NAMES
from tests.test_mamari_reimiro_vendor_scoreboard import JA_LINE_NAMES
from tests.test_mamari_santiago_ia_scoreboard import IA_LINE_NAMES
from tests.test_mamari_second_passage_scoreboard import (
    calendar_published_tokens,
    calendar_start_index,
    extract_ca_published_tokens,
    load_vendored_ca_html,
    published_stems,
)
from tests.test_mamari_small_london_kr_scoreboard import KR_LINE_NAMES
from tests.test_mamari_small_london_kv_scoreboard import KV_LINE_NAMES
from tests.test_mamari_small_santiago_gr_scoreboard import GR_LINE_NAMES
from tests.test_mamari_small_santiago_gv_scoreboard import GV_LINE_NAMES
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    QR_LINE_NAMES,
    QV_LINE_NAMES,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import NA_LINE_NAMES, NB_LINE_NAMES
from tests.test_mamari_tahua_aa_scoreboard import AA_LINE_NAMES
from tests.test_mamari_tahua_ab_scoreboard import AB_LINE_NAMES
from tests.test_mamari_vienna_vendor_scoreboard import MA_LINE_NAMES
from tests.test_mamari_washington_vendor_scoreboard import SA_LINE_NAMES, SB_LINE_NAMES

CALENDAR_LINES = ("Ca6", "Ca7", "Ca8", "Ca9")
STEM_040 = "040"
STEM_041 = "041"
STEM_143 = "143"
STEM_152 = "152"
# Guy 1990 writes the third delimiter sign as 378y, with 315y / 375 as the
# Ca6 variants kept distinct by the fixture. Allograph-tolerant search
# allows only that published slot to vary. It does not merge 040 with 041.
DELIMITER_SLOT = 2
DELIMITER_SLOT_FAMILY = ("315", "375", "378")
DELIMITER_TAIL = ("670", "008", "078", "711")
DELIMITER_OPENING = ("390", "041")
SHORT_DELIMITER = ("390", "041", "375", "041")
FULL_MOON_BIGRAM = ("143", "152")
CODA = ("280", "385", "385")
CONTEXT = 3

# Guy 1990: 12 × glyph 40A before 152, back to the first eight-glyph group;
# 13 × glyph 40A after 152, forward to the last eight-glyph group.
# Measured on the vendored stems (see the scoreboard). The forward count
# matches. The backward count does not. Do not retune the transcription.
GUY_040_BEFORE_152 = 12
GUY_040_AFTER_152 = 13

# Recorded Rapanui night-list lengths as stated by Wieczorek 2011 from
# Englert 1948, Thomson 1891, and Métraux 1940. Not glyph readings.
ENGLERT_NIGHTS = 28
THOMSON_NIGHTS = 29
METRAUX_NIGHTS = 30
NIGHT_BAND = (28, 29, 30)
# Kokore series lengths in the aligned Englert / Thomson / Métraux lists
# (six numbered kokore before the named first-quarter nights; five after
# full moon). Lengths only. No name is assigned to a Barthel number.
KOKORE_EARLY = 6
KOKORE_LATE = 5

SHUFFLE_SEED = 0
SHUFFLE_DRAWS = 5000

SIDE_LINE_NAMES = {
    "Aa": AA_LINE_NAMES,
    "Ab": AB_LINE_NAMES,
    "Br": BR_LINE_NAMES,
    "Bv": BV_LINE_NAMES,
    "Ca": CA_LINE_NAMES,
    "Cb": CB_LINE_NAMES,
    "Da": DA_LINE_NAMES,
    "Db": DB_LINE_NAMES,
    "Er": ER_LINE_NAMES,
    "Ev": EV_LINE_NAMES,
    "Fa": FA_LINE_NAMES,
    "Fb": FB_LINE_NAMES,
    "Gr": GR_LINE_NAMES,
    "Gv": GV_LINE_NAMES,
    "Hr": HR_LINE_NAMES,
    "Hv": HV_LINE_NAMES,
    "Ia": IA_LINE_NAMES,
    "Ja": JA_LINE_NAMES,
    "Kr": KR_LINE_NAMES,
    "Kv": KV_LINE_NAMES,
    "La": LA_LINE_NAMES,
    "Ma": MA_LINE_NAMES,
    "Na": NA_LINE_NAMES,
    "Nb": NB_LINE_NAMES,
    "Oa": OA_LINE_NAMES,
    "Pr": PR_LINE_NAMES,
    "Pv": PV_LINE_NAMES,
    "Qr": QR_LINE_NAMES,
    "Qv": QV_LINE_NAMES,
    "Ra": RA_LINE_NAMES,
    "Rb": RB_LINE_NAMES,
    "Sa": SA_LINE_NAMES,
    "Sb": SB_LINE_NAMES,
    "Ta": TA_LINE_NAMES,
    "Ua": UA_LINE_NAMES,
    "Va": VA_LINE_NAMES,
}

# Locked measurements. A mismatch fails; do not edit these to fit a reading.
STANDING_CALENDAR_STEMS = 101
STANDING_CALENDAR_STEMS_BY_LINE = (16, 43, 40, 2)
STANDING_CA6_STEM_START = 24
STANDING_040 = 28
STANDING_041 = 16
STANDING_041_OUTSIDE_WINDOWS = 0
STANDING_143 = 1
STANDING_152 = 1
STANDING_040_BEFORE_152 = 13
STANDING_040_AFTER_152 = 13
STANDING_040_BETWEEN_DELIMITERS = (2, 6, 3, 2, 5, 3, 5)
STANDING_AFTER_LAST_DELIMITER = ("280", "385", "385", "040", "040")
STANDING_RUNS_BEFORE_152 = (1, 1, 6, 1, 1, 1, 2)
STANDING_RUNS_AFTER_152 = (5, 2, 1, 5, 2)
STANDING_WITHIN_LINE_RUNS_GE5 = (("Ca7", 0, 6, 6), ("Ca8", 24, 29, 5))
STANDING_SHUFFLE_HITS = 0
STANDING_CHI_A_B_C_D = (28, 73, 124, 14616)
STANDING_CHI_NUMERATOR = 2376887638931856
STANDING_CHI_DENOMINATOR = 3323951482720
STANDING_CORPUS_STEMS = 14841
STANDING_CORPUS_040 = 152
STANDING_CORPUS_041 = 54
STANDING_040_BY_TABLET = (
    17, 9, 45, 1, 19, 2, 5, 10, 4, 0, 1, 0, 0, 1, 3, 8, 9, 12, 5, 0, 1, 0,
)
STANDING_041_BY_TABLET = (
    5, 6, 21, 2, 7, 0, 0, 6, 1, 0, 0, 0, 0, 0, 0, 4, 1, 0, 1, 0, 0, 0,
)
STANDING_GUY8 = (
    ("Ca7", 6, ("040", "040", "040"), ("040", "074", "040")),
    ("Ca7", 19, ("040", "059", "040"), ("044", "040", "040")),
    ("Ca7", 33, ("143", "152", "600"), ("040", "040")),
    ("Ca8", 3, ("040", "040", "040"), ("040", "040", "003")),
    ("Ca8", 15, ("040", "003", "040"), ("600", "040", "040")),
    ("Ca8", 29, ("040", "040", "040"), ("280", "385", "385")),
)
STANDING_VARIANT_315 = (
    ("Ca6", 24, ("280", "001", "006"), ("040", "010", "040")),
)
STANDING_VARIANT_375_FULL = ()
STANDING_SHORT_375 = (("Ca6", 36, ("010", "040", "030"), ()),)
STANDING_FULL_MOON_BIGRAM = (
    ("Ca7", 30, ("044", "040", "040"), ("600", "390", "041")),
)
STANDING_CODA = (
    ("Ca5", 18, ("036", "550", "022"), ("038", "007", "600")),
    ("Ca8", 37, ("008", "078", "711"), ()),
)
STANDING_OPENING_HITS = 8
STANDING_TAIL_HITS = 7
STANDING_600_040 = (("A", 1), ("B", 1), ("C", 1), ("N", 1), ("P", 1))
STANDING_HTML_STAR_DIFFERENCES = (
    ("Ca6", 10, "041", "041*"),
    ("Ca7", 31, "040", "040*"),
    ("Ca8", 29, "385", "385*"),
)


@dataclass(frozen=True)
class CorpusHit:
    """One exact hit. Line context does not cross a line break."""

    line: str
    index: int
    left: tuple[str, ...]
    right: tuple[str, ...]


def fisher_yates(items: list[str], rng: random.Random) -> list[str]:
    """In-place-equivalent shuffle with an explicit Fisher–Yates step."""
    shuffled = list(items)
    for index in range(len(shuffled) - 1, 0, -1):
        swap = rng.randrange(index + 1)
        shuffled[index], shuffled[swap] = shuffled[swap], shuffled[index]
    return shuffled


def flatten(lines: list[list[str]]) -> list[str]:
    """Reading order. Line breaks are not signs."""
    return [stem for line in lines for stem in line]


def line_names_for(letter: str) -> tuple[str, ...]:
    """Published line ids for one vendored tablet, side order as locked."""
    names: list[str] = []
    for side in STANDING_SIDES[letter]:
        names.extend(SIDE_LINE_NAMES[side])
    return tuple(names)


def ordered_corpus() -> dict[str, list[list[str]]]:
    """A–V in Barthel line order.

    Tablet C in the older concatenated loader splits Ca6 and Ca9 into
    calendar vs remainder slices. Those slices contain the same stems,
    but not in line order. This track searches the intact Ca1–Ca14 and
    Cb1–Cb14 lines. W has no vendored Barthel page and is omitted.
    """
    by_tablet = dict(load_vendored_a_through_v())
    sides = load_c_sides()
    by_tablet["C"] = sides["Ca"] + sides["Cb"]
    return by_tablet


def ngram_sites(
    lines: list[list[str]],
    names: tuple[str, ...],
    gram: tuple[str, ...],
    context: int = CONTEXT,
) -> tuple[CorpusHit, ...]:
    """Exact contiguous hits with up to `context` stems on each side."""
    width = len(gram)
    hits: list[CorpusHit] = []
    for line_index, sequence in enumerate(lines):
        for start in range(len(sequence) - width + 1):
            if tuple(sequence[start : start + width]) != gram:
                continue
            hits.append(
                CorpusHit(
                    names[line_index],
                    start,
                    tuple(sequence[max(0, start - context) : start]),
                    tuple(sequence[start + width : start + width + context]),
                )
            )
    return tuple(hits)


def delimiter_family_gram(slot: str) -> tuple[str, ...]:
    """Guy's eight-stem delimiter with one published third-slot variant."""
    if slot not in DELIMITER_SLOT_FAMILY:
        raise ValueError(slot)
    gram = list(DELIMITER_MOTIF)
    gram[DELIMITER_SLOT] = slot
    return tuple(gram)


def maximal_run_lengths(sequence: list[str], stem: str = STEM_040) -> tuple[int, ...]:
    """Lengths of maximal consecutive runs of `stem`."""
    lengths: list[int] = []
    index = 0
    while index < len(sequence):
        if sequence[index] != stem:
            index += 1
            continue
        start = index
        while index < len(sequence) and sequence[index] == stem:
            index += 1
        lengths.append(index - start)
    return tuple(lengths)


def within_line_runs(
    lines: list[list[str]],
    names: tuple[str, ...],
    stem: str = STEM_040,
    min_length: int = 5,
) -> tuple[tuple[str, int, int, int], ...]:
    """(line, start, end, length) for within-line runs of at least min_length."""
    runs: list[tuple[str, int, int, int]] = []
    for line_index, sequence in enumerate(lines):
        index = 0
        while index < len(sequence):
            if sequence[index] != stem:
                index += 1
                continue
            start = index
            while index < len(sequence) and sequence[index] == stem:
                index += 1
            if index - start >= min_length:
                runs.append((names[line_index], start, index, index - start))
    return tuple(runs)


def calendar_windows(
    lines: list[list[str]],
) -> tuple[tuple[str, int, int], ...]:
    """Guy windows plus the Ca6 315/375 variants, on the fixture lines."""
    return delimiter_and_variant_spans(lines, DELIMITER_MOTIF, CALENDAR_LINES)


def _global_index(lines: list[list[str]], line: str, index: int) -> int:
    offset = 0
    for name, sequence in zip(CALENDAR_LINES, lines):
        if name == line:
            return offset + index
        offset += len(sequence)
    raise KeyError(line)


def full_delimiter_bounds(
    lines: list[list[str]],
) -> tuple[tuple[int, int], ...]:
    """Global [start, end) of each 8-stem delimiter, short 4-gram excluded."""
    bounds = []
    for line, start, end in calendar_windows(lines):
        if end - start == len(DELIMITER_MOTIF):
            bounds.append((_global_index(lines, line, start), _global_index(lines, line, end)))
    return tuple(bounds)


def guy_040_counts(lines: list[list[str]]) -> tuple[int, int]:
    """040 stems between the first and last 8-stem delimiters, split at 152.

    The count is strictly after the first full delimiter and strictly before
    the last full delimiter. Glyph 152 itself is not a 040.
    """
    sequence = flatten(lines)
    bounds = full_delimiter_bounds(lines)
    first_end = bounds[0][1]
    last_start = bounds[-1][0]
    at_152 = sequence.index(STEM_152)
    before = sequence[first_end:at_152].count(STEM_040)
    after = sequence[at_152 + 1 : last_start].count(STEM_040)
    return before, after


def between_delimiter_040(lines: list[list[str]]) -> tuple[int, ...]:
    """040 counts in each gap between successive delimiter windows."""
    sequence = flatten(lines)
    events = []
    for line, start, end in calendar_windows(lines):
        events.append(
            (_global_index(lines, line, start), _global_index(lines, line, end))
        )
    events.sort()
    gaps = []
    for previous, current in zip(events, events[1:]):
        gaps.append(sequence[previous[1] : current[0]].count(STEM_040))
    return tuple(gaps)


def after_last_delimiter(lines: list[list[str]]) -> tuple[str, ...]:
    """Stems from the end of the last 8-stem delimiter through Ca9.

    The Ca6 short window ends earlier in the passage, so the cut is the
    last full delimiter, not that short window.
    """
    sequence = flatten(lines)
    last_end = max(end for _start, end in full_delimiter_bounds(lines))
    return tuple(sequence[last_end:])


def stem_outside_windows(lines: list[list[str]], stem: str) -> int:
    """How many `stem` tokens sit outside delimiter windows."""
    masked = [[False] * len(sequence) for sequence in lines]
    for line, start, end in calendar_windows(lines):
        row = CALENDAR_LINES.index(line)
        for index in range(start, end):
            masked[row][index] = True
    return sum(
        1
        for row, sequence in enumerate(lines)
        for index, token in enumerate(sequence)
        if token == stem and not masked[row][index]
    )


def runs_split_at_152(lines: list[list[str]]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Maximal 040-run lengths before and after the unique 152.

    Delimiters stay in the sequence, so they break runs. Line breaks do not.
    """
    sequence = flatten(lines)
    at_152 = sequence.index(STEM_152)
    return (
        maximal_run_lengths(sequence[:at_152]),
        maximal_run_lengths(sequence[at_152 + 1 :]),
    )


def kokore_pattern(sequence: list[str]) -> bool:
    """True when a 6-run of 040 sits before 152 and a 5-run sits after.

    Lengths are the recorded kokore series (6 and 5), not fitted constants.
    """
    at_152 = sequence.index(STEM_152)
    before = maximal_run_lengths(sequence[:at_152])
    after = maximal_run_lengths(sequence[at_152 + 1 :])
    return KOKORE_EARLY in before and KOKORE_LATE in after


def shuffle_kokore_hits(
    sequence: list[str],
    draws: int = SHUFFLE_DRAWS,
    seed: int = SHUFFLE_SEED,
) -> int:
    """Draws whose shuffled multiset still shows the 6-before / 5-after pattern."""
    rng = random.Random(seed)
    return sum(1 for _ in range(draws) if kokore_pattern(fisher_yates(sequence, rng)))


def chi_square_terms(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    """Numerator and denominator of the 2×2 chi-square statistic.

    a = calendar 040, b = calendar other stems,
    c = rest-of-corpus 040, d = rest-of-corpus other stems.
    Stems are not independent, so this is a rate comparison, not a p-value.
    """
    total = a + b + c + d
    numerator = (a * d - b * c) ** 2 * total
    denominator = (a + b) * (c + d) * (a + c) * (b + d)
    return numerator, denominator


def in_night_band(count: int) -> bool:
    """True when count is 28, 29, or 30."""
    return count in NIGHT_BAND


def unigram_counts(
    by_tablet: dict[str, list[list[str]]],
    stem: str,
) -> tuple[int, ...]:
    """Per-tablet stem counts in VENDORED_TABLETS order."""
    return tuple(
        sum(line.count(stem) for line in by_tablet[letter]) for letter in VENDORED_TABLETS
    )


def tablet_hit_table(
    by_tablet: dict[str, list[list[str]]],
    names: dict[str, tuple[str, ...]],
    gram: tuple[str, ...],
) -> tuple[CorpusHit, ...]:
    """Exact hits on every vendored tablet, in tablet-letter order."""
    hits: list[CorpusHit] = []
    for letter in VENDORED_TABLETS:
        hits.extend(ngram_sites(by_tablet[letter], names[letter], gram))
    return tuple(hits)


def hit_tuple(hit: CorpusHit) -> tuple:
    """Stable lock row."""
    return (hit.line, hit.index, hit.left, hit.right)


class TestTrack1Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def setUp(self):
        self.provider = MockProvider()

    def test_kokore_pattern_needs_both_runs_around_152(self):
        """A 6-run before 152 and a 5-run after; either side alone fails."""
        good = ["040"] * 6 + ["152"] + ["040"] * 5
        self.assertTrue(kokore_pattern(good))
        self.assertFalse(kokore_pattern(["040"] * 6 + ["152"] + ["040"] * 4))
        self.assertFalse(kokore_pattern(["040"] * 5 + ["152"] + ["040"] * 5))
        self.assertFalse(kokore_pattern(["040"] * 6 + ["999"] + ["040"] * 5 + ["152"]))
        blocked = ["040"] * 3 + ["041"] + ["040"] * 3 + ["152"] + ["040"] * 5
        self.assertFalse(kokore_pattern(blocked))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_shuffle_preserves_the_multiset(self):
        """Fisher–Yates moves tokens and does not drop them."""
        original = ["152", "040", "041", "040"]
        shuffled = fisher_yates(original, random.Random(SHUFFLE_SEED))
        self.assertEqual(sorted(shuffled), sorted(original))
        self.assertEqual(fisher_yates(original, random.Random(1)), fisher_yates(original, random.Random(1)))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_night_band_is_the_recorded_list_lengths(self):
        """28, 29, and 30 are in band. 26 and 31 are not."""
        self.assertEqual((ENGLERT_NIGHTS, THOMSON_NIGHTS, METRAUX_NIGHTS), NIGHT_BAND)
        self.assertTrue(in_night_band(28))
        self.assertTrue(in_night_band(29))
        self.assertTrue(in_night_band(30))
        self.assertFalse(in_night_band(26))
        self.assertFalse(in_night_band(31))
        self.assertEqual(KOKORE_EARLY, 6)
        self.assertEqual(KOKORE_LATE, 5)
        self.assertEqual(self.provider.get_call_history(), [])


class TestTrack1MamariCalendar(unittest.TestCase):
    """Vendored Mamari calendar anchors. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.fixture = load_mamari_fixture()
        self.calendar = fixture_line_stems(self.fixture)
        self.flat = flatten(self.calendar)
        self.by_tablet = ordered_corpus()
        self.names = {letter: line_names_for(letter) for letter in VENDORED_TABLETS}
        self.published = extract_ca_published_tokens(load_vendored_ca_html())

    def test_fixture_stems_are_the_ca_html_calendar_slice(self):
        """Ca.html and the fixture differ only by three damage stars.

        barthel_stems strips those stars, so the calendar slice of the
        full side is the fixture. The calendar starts at the first 390.041
        on Ca6 and keeps only the first two stems of Ca9.
        """
        differences = []
        sliced = calendar_published_tokens(self.published)
        for name in CALENDAR_LINES:
            fixture_tokens = self.fixture["lines"][name]
            html_tokens = sliced[name]
            self.assertEqual(len(fixture_tokens), len(html_tokens))
            for index, (fixture_token, html_token) in enumerate(zip(fixture_tokens, html_tokens)):
                if fixture_token != html_token:
                    differences.append((name, index, fixture_token, html_token))
        self.assertEqual(tuple(differences), STANDING_HTML_STAR_DIFFERENCES)

        start = calendar_start_index(self.published["Ca6"])
        stem_start = len(published_stems(self.published["Ca6"][:start]))
        self.assertEqual(stem_start, STANDING_CA6_STEM_START)
        ca = self.by_tablet["C"][: len(CA_LINE_NAMES)]
        ca6, ca7, ca8, ca9 = ca[5], ca[6], ca[7], ca[8]
        self.assertEqual(ca6[stem_start:], self.calendar[0])
        self.assertEqual(ca7, self.calendar[1])
        self.assertEqual(ca8, self.calendar[2])
        self.assertEqual(ca9[:2], self.calendar[3])
        self.assertEqual(tuple(len(line) for line in self.calendar), STANDING_CALENDAR_STEMS_BY_LINE)
        self.assertEqual(len(self.flat), STANDING_CALENDAR_STEMS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_corpus_line_names_match_the_vendored_sides(self):
        """Every A–V line keeps its published id. W is not in the corpus."""
        self.assertNotIn("W", VENDORED_TABLETS)
        partitioned = load_vendored_a_through_v()["C"]
        intact = self.by_tablet["C"]
        self.assertEqual(
            sorted(stem for line in partitioned for stem in line),
            sorted(stem for line in intact for stem in line),
        )
        self.assertEqual(self.names["C"], CA_LINE_NAMES + CB_LINE_NAMES)
        for letter in VENDORED_TABLETS:
            self.assertEqual(len(self.names[letter]), len(self.by_tablet[letter]))
            self.assertEqual(self.names[letter][0][:1], letter)
        total = sum(len(line) for letter in VENDORED_TABLETS for line in self.by_tablet[letter])
        self.assertEqual(total, STANDING_CORPUS_STEMS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_night_sign_and_delimiter_counts(self):
        """Mechanical counts. 041 inside this passage sits only in delimiters."""
        self.assertEqual(self.flat.count(STEM_040), STANDING_040)
        self.assertEqual(self.flat.count(STEM_041), STANDING_041)
        self.assertEqual(self.flat.count(STEM_143), STANDING_143)
        self.assertEqual(self.flat.count(STEM_152), STANDING_152)
        self.assertEqual(stem_outside_windows(self.calendar, STEM_041), STANDING_041_OUTSIDE_WINDOWS)
        before, after = guy_040_counts(self.calendar)
        self.assertEqual(before, STANDING_040_BEFORE_152)
        self.assertEqual(after, STANDING_040_AFTER_152)
        self.assertNotEqual(before, GUY_040_BEFORE_152)
        self.assertEqual(after, GUY_040_AFTER_152)
        self.assertEqual(between_delimiter_040(self.calendar), STANDING_040_BETWEEN_DELIMITERS)
        self.assertEqual(after_last_delimiter(self.calendar), STANDING_AFTER_LAST_DELIMITER)
        between = sum(STANDING_040_BETWEEN_DELIMITERS)
        self.assertEqual(between, 26)
        self.assertEqual(between + 2, STANDING_040)
        self.assertTrue(in_night_band(STANDING_040))
        self.assertFalse(in_night_band(between))
        # 143 and 152 added on top of the 28 crescents is 30, still inside
        # the recorded band. That addition is a hypothesis, not a second 040.
        self.assertEqual(STANDING_040 + STANDING_143 + STANDING_152, 30)
        self.assertTrue(in_night_band(STANDING_040 + STANDING_143 + STANDING_152))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_kokore_run_pattern_beats_a_token_shuffle(self):
        """A 6-run before 152 and a 5-run after is absent in 5000 shuffles."""
        before, after = runs_split_at_152(self.calendar)
        self.assertEqual(before, STANDING_RUNS_BEFORE_152)
        self.assertEqual(after, STANDING_RUNS_AFTER_152)
        self.assertIn(KOKORE_EARLY, before)
        self.assertIn(KOKORE_LATE, after)
        self.assertTrue(kokore_pattern(self.flat))
        hits = shuffle_kokore_hits(self.flat)
        self.assertEqual(hits, STANDING_SHUFFLE_HITS)
        within = []
        for letter in VENDORED_TABLETS:
            within.extend(
                within_line_runs(self.by_tablet[letter], self.names[letter], min_length=5)
            )
        self.assertEqual(tuple(within), STANDING_WITHIN_LINE_RUNS_GE5)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_040_is_enriched_in_the_calendar_passage(self):
        """Calendar 040 rate versus the rest of A–V. Counts only."""
        calendar_040 = self.flat.count(STEM_040)
        calendar_n = len(self.flat)
        corpus_040 = sum(unigram_counts(self.by_tablet, STEM_040))
        corpus_n = sum(len(line) for letter in VENDORED_TABLETS for line in self.by_tablet[letter])
        rest_040 = corpus_040 - calendar_040
        rest_n = corpus_n - calendar_n
        terms = (
            calendar_040,
            calendar_n - calendar_040,
            rest_040,
            rest_n - rest_040,
        )
        self.assertEqual(terms, STANDING_CHI_A_B_C_D)
        self.assertEqual(corpus_040, STANDING_CORPUS_040)
        numerator, denominator = chi_square_terms(*terms)
        self.assertEqual(numerator, STANDING_CHI_NUMERATOR)
        self.assertEqual(denominator, STANDING_CHI_DENOMINATOR)
        self.assertGreater(numerator / denominator, 100)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_exact_anchors_and_allograph_tolerant_delimiters(self):
        """Exact hits, then the published 315/375/378 delimiter slot.

        Crescent-number family {040, 041} is counted and not equated.
        600 040 is a negative control: it occurs outside C.
        """
        guy8 = delimiter_family_gram("378")
        var315 = delimiter_family_gram("315")
        var375 = delimiter_family_gram("375")
        self.assertEqual(guy8, DELIMITER_MOTIF)
        guy_hits = tablet_hit_table(self.by_tablet, self.names, guy8)
        hit_315 = tablet_hit_table(self.by_tablet, self.names, var315)
        hit_375 = tablet_hit_table(self.by_tablet, self.names, var375)
        short_hits = tablet_hit_table(self.by_tablet, self.names, SHORT_DELIMITER)
        bigram_hits = tablet_hit_table(self.by_tablet, self.names, FULL_MOON_BIGRAM)
        coda_hits = tablet_hit_table(self.by_tablet, self.names, CODA)
        opening_hits = tablet_hit_table(self.by_tablet, self.names, DELIMITER_OPENING)
        tail_hits = tablet_hit_table(self.by_tablet, self.names, DELIMITER_TAIL)
        pair_600 = ("600", "040")
        leak = []
        for letter in VENDORED_TABLETS:
            count = len(ngram_sites(self.by_tablet[letter], self.names[letter], pair_600))
            if count:
                leak.append((letter, count))

        self.assertEqual(tuple(hit_tuple(hit) for hit in guy_hits), STANDING_GUY8)
        self.assertEqual(tuple(hit_tuple(hit) for hit in hit_315), STANDING_VARIANT_315)
        self.assertEqual(tuple(hit_tuple(hit) for hit in hit_375), STANDING_VARIANT_375_FULL)
        self.assertEqual(tuple(hit_tuple(hit) for hit in short_hits), STANDING_SHORT_375)
        self.assertEqual(tuple(hit_tuple(hit) for hit in bigram_hits), STANDING_FULL_MOON_BIGRAM)
        self.assertEqual(tuple(hit_tuple(hit) for hit in coda_hits), STANDING_CODA)
        self.assertEqual(len(opening_hits), STANDING_OPENING_HITS)
        self.assertEqual(len(tail_hits), STANDING_TAIL_HITS)
        self.assertTrue(all(hit.line.startswith("Ca") for hit in opening_hits))
        self.assertTrue(all(hit.line.startswith("Ca") for hit in tail_hits))
        self.assertEqual(tuple(leak), STANDING_600_040)

        counts_040 = unigram_counts(self.by_tablet, STEM_040)
        counts_041 = unigram_counts(self.by_tablet, STEM_041)
        self.assertEqual(counts_040, STANDING_040_BY_TABLET)
        self.assertEqual(counts_041, STANDING_041_BY_TABLET)
        self.assertEqual(sum(counts_040), STANDING_CORPUS_040)
        self.assertEqual(sum(counts_041), STANDING_CORPUS_041)
        # Family total is the sum of the two exact counts, not a third type.
        self.assertEqual(
            tuple(a + b for a, b in zip(counts_040, counts_041)),
            tuple(a + b for a, b in zip(STANDING_040_BY_TABLET, STANDING_041_BY_TABLET)),
        )
        self.assertEqual(sum(unigram_counts(self.by_tablet, STEM_143)), 1)
        self.assertEqual(sum(unigram_counts(self.by_tablet, STEM_152)), 1)
        self.assertEqual(self.provider.get_call_history(), [])
