"""Source-neutral rongorongo transcription files.

A transcription file is a UTF-8 CSV with one row per sign. The format is
documented in ``docs/decipherment/retest_harness.md``. Columns:

``tablet``      Barthel tablet letter, ``A``–``Y``.
``side``        Side code as Barthel/CEIPP write it: ``Aa``, ``Gv``, ``Ia``.
``line``        Line number on that side, as published (integer).
``position``    0-based group position in the line. A group is one
                hyphen-separated Barthel token: a single sign or a ligature.
``slot``        0-based sign position inside the group.
``sign``        Barthel sign number, three digits (``040``). Empty for a
                lacuna mark that carries no sign number.
``variant``     Optional allograph letters (``y`` in ``378y``, ``V``).
``uncertainty`` Optional edition marks: ``?`` uncertain, ``!`` damaged,
                ``*`` editor's mark, ``…`` broken edge. Empty when certain.
``join``        Joiner before this sign inside its group: ``.`` or ``:``.
                Empty for slot 0.
``raw``         Optional exact source text of this sign. When present it is
                used verbatim; otherwise the sign is written as
                ``sign + variant + uncertainty``.

Nothing here reads a reading into a sign. ``MockProvider`` is never needed.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from decipherment.barthel_corpus import LocatedSide, load_located_sides

REPO_ROOT = Path(__file__).resolve().parents[1]
BASELINE_CSV = REPO_ROOT / "data" / "decipherment" / "transcriptions" / "barthel_ceipp.csv"

FIELDS = ("tablet", "side", "line", "position", "slot", "sign", "variant", "uncertainty", "join", "raw")
REQUIRED = ("tablet", "side", "line", "position", "sign")
SOURCE_BARTHEL = "barthel_ceipp"

_ELEMENT = re.compile(
    r"^(?P<pre>[…?]*)(?P<orient>V?)(?P<code>\d+)(?P<variant>[A-Za-z]*)(?P<marks>[!?*…]*)$"
)
_SPLIT = re.compile(r"([.:])")
_SIDE = re.compile(r"^[A-Z][a-z]?$")


@dataclass(frozen=True)
class Corpus:
    """Ordered lines of raw Barthel-style groups, keyed by side and line number."""

    source: str
    lines: tuple[tuple[str, int, tuple[str, ...]], ...]

    def line(self, side: str, number: int) -> tuple[str, ...] | None:
        for row_side, row_number, groups in self.lines:
            if row_side == side and row_number == number:
                return groups
        return None

    def line_map(self) -> dict[str, tuple[str, ...]]:
        return {f"{side}{number}": groups for side, number, groups in self.lines}

    def side_lines(self, side: str) -> list[tuple[int, tuple[str, ...]]]:
        return [(number, groups) for row_side, number, groups in self.lines if row_side == side]

    @property
    def sides(self) -> tuple[str, ...]:
        seen: list[str] = []
        for side, _number, _groups in self.lines:
            if side not in seen:
                seen.append(side)
        return tuple(seen)

    @property
    def tablets(self) -> tuple[str, ...]:
        return tuple(sorted({side[0] for side in self.sides}))

    def located_sides(self) -> tuple[LocatedSide, ...]:
        """Same shape as ``barthel_corpus.load_located_sides``."""
        out = [
            LocatedSide(side=side, path=f"transcription:{self.source}", lines=tuple(self.side_lines(side)))
            for side in self.sides
        ]
        out.sort(key=lambda item: item.side)
        return tuple(out)

    def map_signs(self, mapping: Mapping[str, str]) -> "Corpus":
        """Replace whole sign numbers (``400`` -> ``600``). Variants and marks stay."""
        lines = []
        for side, number, groups in self.lines:
            new_groups = []
            for group in groups:
                parts = _SPLIT.split(group)
                rebuilt = []
                for part in parts:
                    match = _ELEMENT.match(part)
                    if match and match.group("code").zfill(3) in mapping:
                        code = mapping[match.group("code").zfill(3)]
                        part = match.group("pre") + match.group("orient") + code + match.group("variant") + match.group("marks")
                    rebuilt.append(part)
                new_groups.append("".join(rebuilt))
            lines.append((side, number, tuple(new_groups)))
        return Corpus(source=self.source, lines=tuple(lines))

    def restrict(self, tablets: Iterable[str]) -> "Corpus":
        keep = set(tablets)
        return Corpus(
            source=self.source,
            lines=tuple(row for row in self.lines if row[0][0] in keep),
        )


def split_element(text: str) -> dict[str, str]:
    """Fields for one sign element of a group."""
    match = _ELEMENT.match(text)
    if match is None:
        return {"sign": "", "variant": "", "uncertainty": ""}
    return {
        "sign": match.group("code").zfill(3),
        "variant": match.group("orient") + match.group("variant"),
        "uncertainty": match.group("pre") + match.group("marks"),
    }


def group_rows(tablet: str, side: str, line: int, position: int, group: str) -> list[dict[str, str]]:
    parts = _SPLIT.split(group)
    rows: list[dict[str, str]] = []
    join = ""
    for index, part in enumerate(parts):
        if index % 2 == 1:
            join = part
            continue
        fields = split_element(part)
        rows.append(
            {
                "tablet": tablet,
                "side": side,
                "line": str(line),
                "position": str(position),
                "slot": str(len(rows)),
                **fields,
                "join": join if rows else "",
                "raw": part,
            }
        )
        join = ""
    return rows


def corpus_rows(corpus: Corpus) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for side, number, groups in corpus.lines:
        for position, group in enumerate(groups):
            rows.extend(group_rows(side[0], side, number, position, group))
    return rows


def write_csv(corpus: Corpus, path: Path) -> int:
    rows = corpus_rows(corpus)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def _compose(row: Mapping[str, str]) -> str:
    raw = (row.get("raw") or "").strip()
    if raw:
        return raw
    return f"{row.get('sign') or ''}{row.get('variant') or ''}{row.get('uncertainty') or ''}"


class TranscriptionError(ValueError):
    pass


def read_csv(path: Path, source: str | None = None) -> Corpus:
    """Load a transcription CSV. Row order does not matter; position and slot do."""
    with Path(path).open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        header = reader.fieldnames or []
        missing = [name for name in REQUIRED if name not in header]
        if missing:
            raise TranscriptionError(f"{path}: missing columns {', '.join(missing)}")
        groups: dict[tuple[str, int], dict[int, list[tuple[int, str, str]]]] = {}
        order: list[tuple[str, int]] = []
        for number, row in enumerate(reader, start=2):
            side = (row["side"] or "").strip()
            tablet = (row["tablet"] or "").strip()
            if not _SIDE.match(side):
                raise TranscriptionError(f"{path}:{number}: bad side {side!r}")
            if tablet and tablet != side[0]:
                raise TranscriptionError(f"{path}:{number}: tablet {tablet} does not match side {side}")
            try:
                line = int(row["line"])
                position = int(row["position"])
                slot = int(row.get("slot") or 0)
            except ValueError as error:
                raise TranscriptionError(f"{path}:{number}: {error}") from error
            sign = (row.get("sign") or "").strip()
            if sign and not sign.isdigit():
                raise TranscriptionError(f"{path}:{number}: sign {sign!r} is not a Barthel number")
            key = (side, line)
            if key not in groups:
                groups[key] = {}
                order.append(key)
            groups[key].setdefault(position, []).append((slot, (row.get("join") or "").strip(), _compose(row)))
    lines = []
    for key in order:
        by_position = groups[key]
        positions = sorted(by_position)
        if positions != list(range(len(positions))):
            raise TranscriptionError(f"{path}: {key[0]}{key[1]} positions are not 0..n-1")
        tokens = []
        for position in positions:
            elements = sorted(by_position[position])
            text = ""
            for index, (_slot, join, element) in enumerate(elements):
                if index:
                    text += join or "."
                text += element
            tokens.append(text)
        lines.append((key[0], key[1], tuple(tokens)))
    return Corpus(source=source or Path(path).stem, lines=tuple(lines))


def barthel_corpus() -> Corpus:
    """The vendored Barthel/CEIPP corpus. Empty lines are dropped."""
    lines = []
    for side in load_located_sides():
        for number, tokens in side.lines:
            if tokens:
                lines.append((side.side, number, tuple(tokens)))
    return Corpus(source=SOURCE_BARTHEL, lines=tuple(lines))


def _parse_map(values: list[str]) -> dict[str, str]:
    mapping = {}
    for value in values:
        left, _, right = value.partition("=")
        if not left.isdigit() or not right.isdigit():
            raise SystemExit(f"--merge expects OLD=NEW, got {value!r}")
        mapping[left.zfill(3)] = right.zfill(3)
    return mapping


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    export = sub.add_parser("export", help="write the vendored Barthel/CEIPP corpus as a transcription CSV")
    export.add_argument("--out", type=Path, default=BASELINE_CSV)
    perturb = sub.add_parser("perturb", help="write a synthetic variant of a transcription")
    perturb.add_argument("--transcription", type=Path, default=BASELINE_CSV)
    perturb.add_argument("--merge", action="append", default=[], help="OLD=NEW sign number, repeatable")
    perturb.add_argument("--tablets", default="", help="keep only these tablet letters, e.g. AMN")
    perturb.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.command == "export":
        count = write_csv(barthel_corpus(), args.out)
    else:
        corpus = read_csv(args.transcription)
        if args.merge:
            corpus = corpus.map_signs(_parse_map(args.merge))
        if args.tablets:
            corpus = corpus.restrict(args.tablets)
        count = write_csv(corpus, args.out)
    print(f"wrote {count} sign rows to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
