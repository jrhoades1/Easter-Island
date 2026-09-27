"""Switchable sign inventories over Kohaumotu Barthel tokens.

None of these options is a decipherment. The Pozdniakov list is the published
basic-sign labels. It is not their unpublished allograph-merge table.
"""

from __future__ import annotations

import re
from collections import Counter

# Uncertainty and damage marks. Letters that remain are allograph suffixes
# (378y, 040a) or a leading orientation V, matching barthel_stems in
# tests/test_mamari_calendar_scoreboard.py.
_LETTERS = re.compile(r"[A-Za-z]+")
_SURFACE = re.compile(r"^(V?)(\d+)([A-Za-z]*)$")

# Pozdniakov & Pozdniakov 2007, as tabulated in the English Wikipedia article
# "Decipherment of rongorongo" (the article cites Forum for Anthropology and
# Culture 3, pp. 89–122, and notes that the underlying data analysis was not
# published). 27a is kept distinct from Barthel's inverted 27b in that table.
# 901 is Pozdniakov's own addition and is not a Barthel number.
# Citation chain: Pozdniakov 1996, Journal de la Société des Océanistes 103:
# 289–303, is the earlier parallel-text study; the 52-sign count is the 2007
# result (52 glyphs, said to cover 99.7% of the corpus, staff excluded).
POZDNIAKOV_52_LABELS: tuple[str, ...] = (
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "14",
    "15",
    "16",
    "22",
    "25",
    "27a",
    "28",
    "34",
    "38",
    "41",
    "44",
    "46",
    "47",
    "50",
    "52",
    "53",
    "59",
    "60",
    "61",
    "62",
    "63",
    "66",
    "67",
    "69",
    "70",
    "71",
    "74",
    "76",
    "91",
    "95",
    "99",
    "200",
    "240",
    "280",
    "380",
    "400",
    "530",
    "660",
    "700",
    "720",
    "730",
    "901",
)

# Wikipedia, citing Pozdniakov: Barthel 6 and 64 (the two hand shapes) behave
# as graphic variants in repeated phrases. This is one published pair, not
# the full merge table.
HAND_ALLOGRAPH_MERGE = {"064": "006"}

ILLEGIBLE = "000"
RESIDUAL = "RES"

INVENTORY_MODES = (
    "surface",
    "stem",
    "ligature_atomic",
    "pozdniakov_52",
    "frequency_core_52",
    "stem_merge_6_64",
)


def pozdniakov_barthel_stems() -> frozenset[str]:
    """Barthel stems named in the 52-label list.

    ``27a`` becomes ``027``. ``27b`` is not a separate label, so a bare stem
    ``027`` cannot be split. ``901`` is not a Barthel number and is omitted.
    The set therefore has 51 stems, not 52 signs.
    """
    stems: set[str] = set()
    for label in POZDNIAKOV_52_LABELS:
        digits = "".join(character for character in label if character.isdigit())
        if label == "901" or not digits:
            continue
        stems.add(digits.zfill(3))
    return frozenset(stems)


def _prepare(token: str) -> str | None:
    """Strip uncertainty marks. Drop parenthetical lacuna ranges."""
    token = token.strip()
    if not token or "(" in token or ")" in token:
        return None
    token = token.replace("?", "").replace("!", "").replace("*", "").strip()
    return token or None


def _stem_part(part: str) -> str | None:
    if part.startswith("V") and len(part) > 1 and part[1].isdigit():
        part = part[1:]
    part = _LETTERS.sub("", part)
    if part.isdigit():
        return part.zfill(3)
    return None


def _surface_part(part: str) -> str | None:
    match = _SURFACE.fullmatch(part)
    if match is None:
        return None
    return f"{match.group(1)}{match.group(2).zfill(3)}{match.group(3)}"


def encode_token(token: str, mode: str, *, drop_illegible: bool = True) -> list[str]:
    """Encode one Kohaumotu token (already split on hyphens)."""
    if mode not in {"surface", "stem", "ligature_atomic"}:
        raise ValueError(f"encode_token mode must be an encoding, not {mode}")
    cleaned = _prepare(token)
    if cleaned is None:
        return []
    if mode == "ligature_atomic":
        # Keep '.' and ':' so a stacked pair stays distinct from a dot ligature.
        # Illegible 000 components are removed; separators between the signs
        # that remain are kept.
        kept_pairs: list[tuple[str, str]] = []
        separator = ""
        for bit in re.split(r"([.:])", cleaned):
            if bit in ".:":
                separator = bit
                continue
            if not bit:
                continue
            stem = _stem_part(bit)
            if stem is None:
                return []
            if drop_illegible and stem == ILLEGIBLE:
                separator = ""
                continue
            kept_pairs.append((separator, stem))
            separator = ""
        if not kept_pairs:
            return []
        encoded = kept_pairs[0][1]
        for sep, stem in kept_pairs[1:]:
            encoded += (sep or ".") + stem
        return [encoded]

    signs: list[str] = []
    for part in re.split(r"[.:]", cleaned):
        if not part:
            continue
        if mode == "surface":
            sign = _surface_part(part)
        else:
            sign = _stem_part(part)
        if sign is None:
            continue
        if drop_illegible and _stem_part(part) == ILLEGIBLE:
            continue
        signs.append(sign)
    return signs


def encode_lines(
    lines: list[list[str]] | tuple[tuple[str, ...], ...],
    mode: str,
    *,
    drop_illegible: bool = True,
) -> list[list[str]]:
    """Encode every line. Empty lines are dropped."""
    if mode == "pozdniakov_52":
        encoded = encode_lines(lines, "stem", drop_illegible=drop_illegible)
        return collapse_to_core(encoded, pozdniakov_barthel_stems())
    if mode == "frequency_core_52":
        encoded = encode_lines(lines, "stem", drop_illegible=drop_illegible)
        return collapse_to_top(encoded, 52)
    if mode == "stem_merge_6_64":
        encoded = encode_lines(lines, "stem", drop_illegible=drop_illegible)
        return apply_merge(encoded, HAND_ALLOGRAPH_MERGE)
    if mode not in {"surface", "stem", "ligature_atomic"}:
        raise ValueError(f"unknown inventory mode {mode}")
    output: list[list[str]] = []
    for line in lines:
        signs = [
            sign
            for token in line
            for sign in encode_token(token, mode, drop_illegible=drop_illegible)
        ]
        if signs:
            output.append(signs)
    return output


def apply_merge(lines: list[list[str]], merges: dict[str, str]) -> list[list[str]]:
    """Replace signs according to an explicit map. Unknown signs stay."""
    return [[merges.get(sign, sign) for sign in line] for line in lines]


def collapse_to_core(lines: list[list[str]], core: frozenset[str] | set[str]) -> list[list[str]]:
    """Map every sign outside ``core`` to one residual class."""
    return [[sign if sign in core else RESIDUAL for sign in line] for line in lines]


def top_signs(lines: list[list[str]], k: int) -> list[str]:
    """Most frequent signs, ties broken by the sign string."""
    counts = Counter(sign for line in lines for sign in line)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [sign for sign, _count in ranked[:k]]


def collapse_to_top(lines: list[list[str]], k: int) -> list[list[str]]:
    """Keep the k most frequent signs and map the tail to one residual class."""
    keep = set(top_signs(lines, k))
    return collapse_to_core(lines, keep)


def coverage(lines: list[list[str]], keep: set[str] | frozenset[str]) -> float:
    """Fraction of tokens whose sign is in ``keep``."""
    total = 0
    inside = 0
    for line in lines:
        for sign in line:
            total += 1
            if sign in keep:
                inside += 1
    if total == 0:
        return 0.0
    return inside / total
