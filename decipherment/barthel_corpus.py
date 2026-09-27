"""Load vendored Kohaumotu Barthel lines.

The HTML snapshots under ``tests/fixtures`` are the corpus. JSON files that
repeat the same side are not loaded again. The Mamari calendar extract is a
slice of ``Ca.html`` and is not added a second time.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from html import unescape
from pathlib import Path

# Tablet-side filenames only: Aa.html, Ca.html, W.html. Index pages
# (A_index.html) and catalog pages do not match.
_SIDE_FILENAME = re.compile(r"^[A-Z][a-z]?\.html$")
_LINE_ANCHOR = re.compile(r'<h3><a name="Line_(\d+)">', re.IGNORECASE)
_SIDE_LINE = re.compile(r"<h3>\s*Side\s+[ab],\s*line\s+(\d+)\s*</h3>", re.IGNORECASE)
_TD = re.compile(r"<td[^>]*>([^<]*)</td>", re.IGNORECASE)

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = REPO_ROOT / "tests" / "fixtures"


@dataclass(frozen=True)
class BarthelSide:
    """One inscribed side, in published line order."""

    side: str
    path: str
    lines: tuple[tuple[str, ...], ...]

    @property
    def token_count(self) -> int:
        return sum(len(line) for line in self.lines)


def _line_chunks(html: str) -> list[tuple[int, str]]:
    """Return (line_number, html_after_header) for either Kohaumotu header."""
    anchors = [(int(match.group(1)), match.end()) for match in _LINE_ANCHOR.finditer(html)]
    if not anchors:
        anchors = [(int(match.group(1)), match.end()) for match in _SIDE_LINE.finditer(html)]
    chunks: list[tuple[int, str]] = []
    for index, (number, start) in enumerate(anchors):
        end = anchors[index + 1][1] if index + 1 < len(anchors) else len(html)
        # The next header's match end is past the header. Cut at the next
        # header start instead so the following line's <td> is not reused.
        if index + 1 < len(anchors):
            next_header = html.rfind("<h3", 0, anchors[index + 1][1])
            if next_header != -1:
                end = next_header
        chunks.append((number, html[start:end]))
    return chunks


def _tokens_in_chunk(chunk: str) -> tuple[str, ...]:
    """Hyphen-separated Barthel tokens from one line's HTML.

    Image cells and cells with no digit are skipped. Parenthetical lacuna
    ranges such as ``(6-8)!`` are kept here as raw tokens; the inventory
    encoder drops them.
    """
    tokens: list[str] = []
    for cell in _TD.findall(chunk):
        text = unescape(cell).strip()
        if not text or not any(character.isdigit() for character in text):
            continue
        for part in text.split("-"):
            part = part.strip()
            if part:
                tokens.append(part)
    return tuple(tokens)


def numbered_tokens_from_html(html: str) -> tuple[tuple[int, tuple[str, ...]], ...]:
    """``(line_number, tokens)`` in published order.

    Line numbers are the Kohaumotu ``Line_N`` anchors. Empty lines are kept
    so a missing anchor is still visible to the caller.
    """
    return tuple((number, _tokens_in_chunk(chunk)) for number, chunk in _line_chunks(html))


def tokens_from_html(html: str) -> tuple[tuple[str, ...], ...]:
    """Hyphen-separated Barthel tokens from <td> text.

    Image cells and cells with no digit are skipped. Parenthetical lacuna
    ranges such as ``(6-8)!`` are kept here as raw tokens; the inventory
    encoder drops them.
    """
    return tuple(tokens for _number, tokens in numbered_tokens_from_html(html))


@dataclass(frozen=True)
class LocatedSide:
    """One inscribed side with Kohaumotu line numbers kept."""

    side: str
    path: str
    lines: tuple[tuple[int, tuple[str, ...]], ...]

    @property
    def token_count(self) -> int:
        return sum(len(tokens) for _number, tokens in self.lines)


def _load_raw_sides(fixtures: Path) -> list[tuple[str, str, tuple[tuple[int, tuple[str, ...]], ...]]]:
    """Side code, repo-relative path, and numbered raw tokens.

    Index pages and sides with no digit transcription are omitted. ``L.html``
    beside ``La.html`` is an index page and contributes no tokens.
    """
    found: list[tuple[str, str, tuple[tuple[int, tuple[str, ...]], ...]]] = []
    if not fixtures.is_dir():
        return found
    for path in sorted(fixtures.rglob("*.html")):
        if not _SIDE_FILENAME.match(path.name):
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        lines = numbered_tokens_from_html(html)
        if not any(tokens for _number, tokens in lines):
            continue
        relative = path.relative_to(fixtures.parent.parent).as_posix()
        found.append((path.stem, relative, lines))
    return found


def load_located_sides(fixtures: Path = FIXTURES) -> tuple[LocatedSide, ...]:
    """Every vendored side, with published line numbers."""
    sides = [
        LocatedSide(side=side, path=path, lines=lines)
        for side, path, lines in _load_raw_sides(fixtures)
    ]
    sides.sort(key=lambda item: item.side)
    return tuple(sides)


def load_barthel_sides(fixtures: Path = FIXTURES) -> tuple[BarthelSide, ...]:
    """Every vendored side HTML that contains at least one Barthel token."""
    sides = [
        BarthelSide(
            side=side,
            path=path,
            lines=tuple(tokens for _number, tokens in lines),
        )
        for side, path, lines in _load_raw_sides(fixtures)
    ]
    sides.sort(key=lambda item: item.side)
    return tuple(sides)
