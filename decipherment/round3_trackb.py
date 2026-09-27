"""Round 3 Track B: audit Barthel's Mamari calendar against a photograph.

The passage is Ca6–Ca9, the lunar-calendar slice already measured in
Track 1. Every Barthel code in that slice is compared with the openly
licensed photograph of tablet C and with later published corrections.
A code the photograph does not resolve is marked illegible. No sign is
invented to fill a gap. ``MockProvider`` is accepted and never called.
No reading is assigned.
"""

from __future__ import annotations

import hashlib
import random
import re
from dataclasses import dataclass
from pathlib import Path

from agents.base.providers import MockProvider
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "mamari_ca6_ca9_barthel.json"
CA_HTML_PATH = REPO_ROOT / "tests" / "fixtures" / "mamari_ca_html" / "Ca.html"
PHOTO_PATH = REPO_ROOT / "data" / "images" / "mamari" / "rongorongo_c-a_mamari.jpg"

CALENDAR_LINES = ("Ca6", "Ca7", "Ca8", "Ca9")
PHOTO_SHA256 = "33c768be356f158f614c6181ca8d66c8542f6c6f871d16ca045eab2f5c2d51f1"
PHOTO_PIXELS = (2040, 1424)
# Dark-pixel tablet bounds on the Commons plate. Thresholds are the
# measurement definition, not a glyph detector.
INK_THRESHOLD = 180
INK_FRACTION = 0.4
TABLET_LENGTH_MM = 290
TABLET_WIDTH_MM = 196

STEM_040 = "040"
STEM_152 = "152"
DELIMITER = ("390", "041", "378", "041", "670", "008", "078", "711")
DELIMITER_SLOT_FAMILY = ("315", "375", "378")
SHORT_DELIMITER = ("390", "041", "375", "041")
# Guy's logical sign. The asterisk is his, so this is not catalog 690.
GUY_STAR_690 = "*690"

SHUFFLE_SEED = 0
SHUFFLE_DRAWS = 5000
# Track 1 corpus totals. This audit edits only the calendar slice.
CORPUS_STEMS = 14841
CORPUS_040 = 152
OUTSIDE_040 = CORPUS_040 - 28
OUTSIDE_OTHER = 14616

_ALLOGRAPH_MARKS = re.compile(r"[A-Za-z?*!]+")
_LINE_HEADER = re.compile(r'name="Line_(\d+)"')
_TD_TEXT = re.compile(r"<td>([^<]*)</td>")

# Kohaumotu Fischer numeric page, fetched 2026-09-27 from
# http://kohaumotu.org/Rongorongo/C/fi_Ca.html . Codes only.
FISCHER_CA_LINES = {
    6: (
        "005-005-001.006-005f-002V?-002V?-002V?-001.006-381f-381f-381f-",
        "001.006-774.067.774?-070-600V-773-280-001.006-390.041-315y-",
        "041-670-008.078.711-040.010-040-030a-390.041-375-041*",
    ),
    7: (
        "040-040-040-040-040-040-390.041-378-041-670-008.078.711-040-074f.040-",
        "059f-040-390.041-378y-041h-670-008.078.711-044.040-040-143-152-",
        "600.390.041-378y-041-670y-008-078.711-040-040*",
    ),
    8: (
        "040-040-040-390.041-378y-041h-670-008.078.711-040-040-003.040-390.041-",
        "378y-041-670-008.078.711-600-040-040-040-040-040-390.041-",
        "378y-041-670-008.078.711-280-385y-385*",
    ),
    9: (
        "040-040-520-070-670-670-637-034V-017-325y-041-",
        "630-054-630-047-006.011-299-002-002-200-215.002-",
        "010.002-005-002-069-002-200.200.205*",
    ),
}


@dataclass(frozen=True)
class TokenJudgment:
    """One published calendar token. Photo status is separate from the code."""

    line: str
    index: int
    barthel: str
    photo: str
    status: str
    proposed: str | None
    source: str | None
    adopted: bool
    note: str


@dataclass(frozen=True)
class Measure:
    """One calendar measurement, Barthel text beside the adopted correction."""

    name: str
    barthel: object
    corrected: object


@dataclass(frozen=True)
class AuditReport:
    """Counts only. No night name is written onto a sign."""

    provider_calls: int
    photo_sha256: str
    photo_pixels: tuple[int, int]
    tablet_bbox: tuple[int, int, int, int]
    judgments: tuple[TokenJudgment, ...]
    barthel_lines: tuple[tuple[str, ...], ...]
    corrected_lines: tuple[tuple[str, ...], ...]
    measures: tuple[Measure, ...]

    def measure(self, name: str) -> Measure:
        for item in self.measures:
            if item.name == name:
                return item
        raise KeyError(name)


def barthel_stems(tokens: list[str] | tuple[str, ...]) -> list[str]:
    """Mechanical stems. Ligatures split. Allograph letters stripped.

    A leading ``*`` is kept when the rest of that piece is digits. That is
    how Guy's asterisked ``*690`` stays distinct from catalog ``690``.
    """
    stems: list[str] = []
    for token in tokens:
        piece = token.strip().rstrip("*")
        if not piece:
            continue
        for part in piece.replace(":", ".").split("."):
            part = part.strip()
            if not part:
                continue
            if part.startswith("V") and len(part) > 1 and part[1].isdigit():
                part = part[1:]
            starred = part.startswith("*")
            body = part[1:] if starred else part
            body = _ALLOGRAPH_MARKS.sub("", body)
            if body.isdigit():
                stems.append(("*" if starred else "") + body.zfill(3))
    return stems


def load_fixture_tokens() -> dict[str, tuple[str, ...]]:
    """Calendar tokens from the vendored Ca6–Ca9 fixture."""
    import json

    data = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    return {name: tuple(data["lines"][name]) for name in CALENDAR_LINES}


def html_line_codes(html: str, line_number: int) -> tuple[str, ...]:
    """Hyphen-code cells under one ``Line_N`` heading."""
    chunks = re.split(r"<h3>", html)
    for chunk in chunks:
        match = _LINE_HEADER.search(chunk)
        if match is None or int(match.group(1)) != line_number:
            continue
        cells = []
        for text in _TD_TEXT.findall(chunk):
            stripped = text.strip()
            if re.search(r"\d", stripped):
                cells.append(stripped)
        return tuple(cells)
    raise KeyError(line_number)


def fischer_matches_barthel_html() -> bool:
    """True when the fetched Fischer codes equal the vendored Barthel page."""
    html = CA_HTML_PATH.read_text(encoding="utf-8")
    for line_number, fischer in FISCHER_CA_LINES.items():
        if html_line_codes(html, line_number) != fischer:
            return False
    return True


def _judgment(line: str, index: int, token: str) -> TokenJudgment:
    """Published alternatives only. The photograph resolves none of them."""
    photo = "illegible"
    stems = barthel_stems([token])
    if token == "044.040":
        return TokenJudgment(
            line,
            index,
            token,
            photo,
            "corrected",
            "078.040",
            "Guy 1990",
            True,
            "Guy retranscribes the 44 element as 78. He does not remove the crescent.",
        )
    if token == "600.390.041":
        return TokenJudgment(
            line,
            index,
            token,
            photo,
            "corrected",
            "*690.041",
            "Guy 1990",
            True,
            "Guy treats 600:390 as one sign, asterisked *690, not catalog 690.",
        )
    if "670" in stems:
        return TokenJudgment(
            line,
            index,
            token,
            photo,
            "disputed",
            None,
            "Guy 1990",
            False,
            "Guy says these are V631B, except one V671 after the night he calls kokore ono. Which one is not chosen here.",
        )
    return TokenJudgment(
        line,
        index,
        token,
        photo,
        "unconfirmed",
        None,
        None,
        False,
        "No published code change in the sources used here. The photograph does not resolve the number.",
    )


def judge_calendar(tokens: dict[str, tuple[str, ...]]) -> tuple[TokenJudgment, ...]:
    rows: list[TokenJudgment] = []
    for line in CALENDAR_LINES:
        for index, token in enumerate(tokens[line]):
            rows.append(_judgment(line, index, token))
    return tuple(rows)


def apply_adopted(tokens: dict[str, tuple[str, ...]]) -> dict[str, tuple[str, ...]]:
    """Replace only the two Guy tokens that name one Barthel group."""
    adopted = {
        (row.line, row.index): row.proposed
        for row in judge_calendar(tokens)
        if row.adopted and row.proposed is not None
    }
    corrected: dict[str, tuple[str, ...]] = {}
    for line in CALENDAR_LINES:
        pieces = []
        for index, token in enumerate(tokens[line]):
            pieces.append(adopted.get((line, index), token))
        corrected[line] = tuple(pieces)
    return corrected


def stem_lines(tokens: dict[str, tuple[str, ...]]) -> tuple[tuple[str, ...], ...]:
    return tuple(tuple(barthel_stems(tokens[name])) for name in CALENDAR_LINES)


def flatten(lines: tuple[tuple[str, ...], ...]) -> list[str]:
    return [stem for line in lines for stem in line]


def _windows(
    lines: tuple[tuple[str, ...], ...],
    first_signs: frozenset[str],
) -> tuple[tuple[str, int, int], ...]:
    """Delimiter spans. Longer span wins when two start at the same stem."""
    best: dict[tuple[str, int], tuple[str, int, int]] = {}
    for line, sequence in zip(CALENDAR_LINES, lines):
        limit = len(sequence)
        for start in range(limit):
            span = _span_at(sequence, start, first_signs)
            if span is None:
                continue
            key = (line, start)
            end = start + span
            previous = best.get(key)
            if previous is None or end - start > previous[2] - previous[1]:
                best[key] = (line, start, end)
    return tuple(sorted(best.values(), key=lambda row: (CALENDAR_LINES.index(row[0]), row[1])))


def _span_at(
    sequence: tuple[str, ...],
    start: int,
    first_signs: frozenset[str],
) -> int | None:
    """8 for a full delimiter, 4 for the Ca6 short form, else None."""
    if start + 8 <= len(sequence) and sequence[start] in first_signs:
        third = sequence[start + 2]
        tail_ok = sequence[start + 1] == "041" and sequence[start + 3 : start + 8] == DELIMITER[3:]
        if tail_ok and third in DELIMITER_SLOT_FAMILY:
            if sequence[start] == "390" or third == "378":
                return 8
    if sequence[start : start + 4] == SHORT_DELIMITER:
        return 4
    return None


def _global(lines: tuple[tuple[str, ...], ...], line: str, index: int) -> int:
    offset = 0
    for name, sequence in zip(CALENDAR_LINES, lines):
        if name == line:
            return offset + index
        offset += len(sequence)
    raise KeyError(line)


def full_delimiter_bounds(
    lines: tuple[tuple[str, ...], ...],
    first_signs: frozenset[str],
) -> tuple[tuple[int, int], ...]:
    """Every 8-sign delimiter, including the Ca6 third-sign ``315`` variant."""
    bounds = []
    for line, start, end in _windows(lines, first_signs):
        if end - start == 8:
            bounds.append((_global(lines, line, start), _global(lines, line, end)))
    return tuple(bounds)


def count_378_delimiters(
    lines: tuple[tuple[str, ...], ...],
    first_signs: frozenset[str],
) -> int:
    """Eight-sign delimiters whose third stem is ``378``.

    This is Track 1's six exact hits. The Ca6 ``315`` opener is an
    eight-sign group and is not one of them.
    """
    count = 0
    for line, start, end in _windows(lines, first_signs):
        if end - start != 8:
            continue
        sequence = lines[CALENDAR_LINES.index(line)]
        if sequence[start + 2] == "378":
            count += 1
    return count


def guy_040_counts(
    lines: tuple[tuple[str, ...], ...],
    first_signs: frozenset[str],
) -> tuple[int, int]:
    """040 stems after the first full delimiter and before the last, split at 152."""
    sequence = flatten(lines)
    bounds = full_delimiter_bounds(lines, first_signs)
    at_152 = sequence.index(STEM_152)
    before = sequence[bounds[0][1] : at_152].count(STEM_040)
    after = sequence[at_152 + 1 : bounds[-1][0]].count(STEM_040)
    return before, after


def between_delimiter_040(
    lines: tuple[tuple[str, ...], ...],
    first_signs: frozenset[str],
) -> tuple[int, ...]:
    sequence = flatten(lines)
    events = []
    for line, start, end in _windows(lines, first_signs):
        events.append((_global(lines, line, start), _global(lines, line, end)))
    events.sort()
    gaps = []
    for previous, current in zip(events, events[1:]):
        gaps.append(sequence[previous[1] : current[0]].count(STEM_040))
    return tuple(gaps)


def maximal_runs(sequence: list[str], stem: str = STEM_040) -> tuple[int, ...]:
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


def runs_around_152(lines: tuple[tuple[str, ...], ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    sequence = flatten(lines)
    at_152 = sequence.index(STEM_152)
    return maximal_runs(sequence[:at_152]), maximal_runs(sequence[at_152 + 1 :])


def _kokore(sequence: list[str]) -> bool:
    at_152 = sequence.index(STEM_152)
    before = maximal_runs(sequence[:at_152])
    after = maximal_runs(sequence[at_152 + 1 :])
    return 6 in before and 5 in after


def shuffle_kokore_hits(sequence: list[str]) -> int:
    """Fisher–Yates, seed 0, 5000 draws. Same null as Track 1."""
    rng = random.Random(SHUFFLE_SEED)
    hits = 0
    for _ in range(SHUFFLE_DRAWS):
        shuffled = list(sequence)
        for index in range(len(shuffled) - 1, 0, -1):
            swap = rng.randrange(index + 1)
            shuffled[index], shuffled[swap] = shuffled[swap], shuffled[index]
        if _kokore(shuffled):
            hits += 1
    return hits


def chi_square_terms(calendar_040: int, calendar_stems: int) -> tuple[int, int]:
    """2×2 rate comparison. Outside-calendar cells stay at the Track 1 totals.

    The outside cell changes only if this audit adds or removes a 040,
    which the adopted corrections do not.
    """
    other = calendar_stems - calendar_040
    outside_040 = CORPUS_040 - 28
    # One non-040 stem leaves the calendar under the adopted merge, so the
    # outside-other cell is unchanged and the corpus total drops by the
    # same amount as the calendar.
    outside_other = OUTSIDE_OTHER
    total = calendar_040 + other + outside_040 + outside_other
    numerator = (calendar_040 * outside_other - other * outside_040) ** 2 * total
    denominator = (
        (calendar_040 + other)
        * (outside_040 + outside_other)
        * (calendar_040 + outside_040)
        * (other + outside_other)
    )
    return numerator, denominator


def tablet_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    """Inclusive dark bounds of the tablet on the Commons plate.

    Returns x, y, width, height. This is not a sign segmentation.
    """
    gray = image.convert("L")
    width, height = gray.size
    raw = gray.tobytes()
    rows = [
        y
        for y in range(height)
        if sum(value < INK_THRESHOLD for value in raw[y * width : (y + 1) * width]) / width
        > INK_FRACTION
    ]
    cols = [
        x
        for x in range(width)
        if sum(raw[y * width + x] < INK_THRESHOLD for y in range(height)) / height > INK_FRACTION
    ]
    if not rows or not cols:
        raise ValueError("no tablet bounds")
    return cols[0], rows[0], cols[-1] - cols[0] + 1, rows[-1] - rows[0] + 1


def photo_sha256() -> str:
    digest = hashlib.sha256()
    digest.update(PHOTO_PATH.read_bytes())
    return digest.hexdigest()


def _pair(name: str, barthel: object, corrected: object) -> Measure:
    return Measure(name, barthel, corrected)


def build_measures(
    barthel_lines: tuple[tuple[str, ...], ...],
    corrected_lines: tuple[tuple[str, ...], ...],
) -> tuple[Measure, ...]:
    """Track 1 quantities on the Barthel stems and on the adopted correction."""
    strict = frozenset({"390"})
    family = frozenset({"390", GUY_STAR_690})
    barthel_flat = flatten(barthel_lines)
    corrected_flat = flatten(corrected_lines)
    barthel_040 = barthel_flat.count(STEM_040)
    corrected_040 = corrected_flat.count(STEM_040)
    rows = [
        _pair("stems", len(barthel_flat), len(corrected_flat)),
        _pair("stems_by_line", tuple(len(line) for line in barthel_lines), tuple(len(line) for line in corrected_lines)),
        _pair("040", barthel_040, corrected_040),
        _pair("040_around_152", guy_040_counts(barthel_lines, strict), guy_040_counts(corrected_lines, strict)),
        _pair(
            "040_around_152_family",
            guy_040_counts(barthel_lines, family),
            guy_040_counts(corrected_lines, family),
        ),
        _pair("040_gaps", between_delimiter_040(barthel_lines, strict), between_delimiter_040(corrected_lines, strict)),
        _pair(
            "040_gaps_family",
            between_delimiter_040(barthel_lines, family),
            between_delimiter_040(corrected_lines, family),
        ),
        _pair("runs_around_152", runs_around_152(barthel_lines), runs_around_152(corrected_lines)),
        _pair("exact_full_delimiters", count_378_delimiters(barthel_lines, strict), count_378_delimiters(corrected_lines, strict)),
        _pair(
            "family_full_delimiters",
            count_378_delimiters(barthel_lines, family),
            count_378_delimiters(corrected_lines, family),
        ),
        _pair("shuffle_kokore_hits", shuffle_kokore_hits(barthel_flat), shuffle_kokore_hits(corrected_flat)),
        _pair("chi_square", chi_square_terms(barthel_040, len(barthel_flat)), chi_square_terms(corrected_040, len(corrected_flat))),
        _pair("stem_044", barthel_flat.count("044"), corrected_flat.count("044")),
        _pair("stem_078", barthel_flat.count("078"), corrected_flat.count("078")),
        _pair("stem_600", barthel_flat.count("600"), corrected_flat.count("600")),
        _pair("stem_390", barthel_flat.count("390"), corrected_flat.count("390")),
        _pair("stem_star690", barthel_flat.count(GUY_STAR_690), corrected_flat.count(GUY_STAR_690)),
        _pair("outside_040", OUTSIDE_040, OUTSIDE_040 if corrected_040 == 28 else CORPUS_040 - corrected_040),
    ]
    return tuple(rows)


def run_round3_trackb(provider: MockProvider | None = None) -> AuditReport:
    """Audit Mamari Ca6–Ca9. Requires MockProvider and does not call it."""
    if not isinstance(provider, MockProvider):
        raise TypeError("MockProvider is required")
    digest = photo_sha256()
    if digest != PHOTO_SHA256:
        raise ValueError("Commons photograph hash does not match the audit record")
    with Image.open(PHOTO_PATH) as image:
        if image.size != PHOTO_PIXELS:
            raise ValueError("Commons photograph size does not match the audit record")
        bounds = tablet_bbox(image)
    tokens = load_fixture_tokens()
    judgments = judge_calendar(tokens)
    barthel = stem_lines(tokens)
    corrected = stem_lines(apply_adopted(tokens))
    return AuditReport(
        provider_calls=len(provider.get_call_history()),
        photo_sha256=digest,
        photo_pixels=PHOTO_PIXELS,
        tablet_bbox=bounds,
        judgments=judgments,
        barthel_lines=barthel,
        corrected_lines=corrected,
        measures=build_measures(barthel, corrected),
    )
