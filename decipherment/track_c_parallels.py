"""Round 2, Track C: parallel passages and substitution classes.

Approximate string matching on the vendored Barthel corpus. Sign numbers
only. No reading is assigned. ``MockProvider`` is accepted and never called.

The primary encoding splits ligatures (``.`` and ``:``) into stems. Passing
``decompose_ligatures=False`` keeps each ligature as one unit. Significance
is the best Smith-Waterman score of a match-bounded alignment against a
within-side shuffle of the same signs.
"""

from __future__ import annotations

import json
import random
from array import array
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import load_located_sides
from decipherment.inventories import encode_lines

REPO_ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = REPO_ROOT / "docs" / "decipherment" / "round2_trackC_parallels.md"
JSON_PATH = REPO_ROOT / "data" / "decipherment" / "substitution_classes.json"

# Pre-specified gates. They are not retuned to force a tablet pair in.
SEED = 3
MIN_SPAN = 8
MIN_IDENTITY = 0.80
MATCH = 2
MISMATCH = -1
GAP = -1
MAX_SEED_GAP = 18
SEED_BAND = 5
MARGIN = 10
MAX_BRIDGE = 12
BRIDGE_SLACK = 8
REPETITIVE_KMER = 30
NULL_TRIALS = 24
NULL_SEED = 0
PAIR_TRIALS = 400
PAIR_SEED = 7
INDEL_TRIALS = 400
INDEL_SEED = 11
MIN_SYSTEMATIC_COUNT = 3
# (1 + null_ge) / (trials + 1) <= 1/100. Compared in integers so the gate does not drift.
SYSTEMATIC_P_NUM = 1
SYSTEMATIC_P_DEN = 100
COVER_FRACTION = 0.70
OVERLAP_FRACTION = 0.50

# Tablet pairs named in the sources this track compares against.
# Status "published" means the pair is named there. It does not copy a locus.
PUBLISHED_PAIRS: dict[frozenset[str], dict[str, str]] = {
    frozenset({"H", "P"}): {
        "label": "H–P",
        "source": (
            "Kudrjavtsev 1949 collation of the Great Santiago (H) and "
            "Great St. Petersburg (P) tablets, as later editors use it "
            "(Barthel 1958: 151–157; Pozdniakov 1996; Horley 2007)"
        ),
    },
    frozenset({"H", "Q"}): {
        "label": "H–Q",
        "source": (
            "Same three-tablet parallel; Sproat 2003 records a 125-glyph "
            "approximate match between Great Santiago recto and Small "
            "St. Petersburg recto"
        ),
    },
    frozenset({"P", "Q"}): {
        "label": "P–Q",
        "source": (
            "Kudrjavtsev 1949 on the two St. Petersburg tablets; "
            "Barthel 1958; Pozdniakov 1996; Davletshin 2017 uses P as the "
            "reference copy against H and Q"
        ),
    },
    frozenset({"G", "K"}): {
        "label": "G–K",
        "source": (
            "Small Santiago (G) and London (K). Horley 2007 treats K as a "
            "copy of Gr. The vendored scoreboards lock an exact 17-stem "
            "share on Gr/Kr"
        ),
    },
    frozenset({"A", "R"}): {
        "label": "A–R",
        "source": (
            "Horley 2007: a passage shared by Tahua (A) and Atua Mata Riri (R), "
            "found after recoding signs into glyph elements"
        ),
    },
}

HAND_PAIR = ("006", "064")


@dataclass(frozen=True)
class SideText:
    """One side, ligatures already encoded, lines concatenated."""

    tablet: str
    side: str
    path: str
    signs: tuple[str, ...]
    spans: tuple[tuple[str, int, int], ...]

    def locate(self, index: int) -> tuple[str, int]:
        for name, start, end in self.spans:
            if start <= index < end:
                return name, index - start
        raise IndexError(index)

    def absolute(self, line: str, offset: int) -> int:
        for name, start, end in self.spans:
            if name == line:
                index = start + offset
                if index < start or index >= end:
                    raise IndexError(offset)
                return index
        raise KeyError(line)


@dataclass(frozen=True)
class Passage:
    """One match-bounded local alignment between two sides."""

    left_side: str
    right_side: str
    left_tablet: str
    right_tablet: str
    left_start: int
    left_end: int
    right_start: int
    right_end: int
    score: int
    matches: int
    mismatches: int
    gaps: int
    span: int
    identity_bp: int
    columns: tuple[tuple[str | None, str | None], ...]

    @property
    def aligned_length(self) -> int:
        return self.matches + self.mismatches + self.gaps

    @property
    def pair_key(self) -> frozenset[str]:
        return frozenset((self.left_tablet, self.right_tablet))


def load_side_texts(mode: str) -> tuple[SideText, ...]:
    """Encode every located side. ``mode`` is ``stem`` or ``ligature_atomic``."""
    texts: list[SideText] = []
    for raw in load_located_sides():
        signs: list[str] = []
        spans: list[tuple[str, int, int]] = []
        for number, tokens in raw.lines:
            encoded = encode_lines([list(tokens)], mode)
            row = encoded[0] if encoded else []
            start = len(signs)
            signs.extend(row)
            if row:
                spans.append((f"{raw.side}{number}", start, len(signs)))
        if not signs:
            continue
        texts.append(
            SideText(
                tablet=raw.side[0],
                side=raw.side,
                path=raw.path,
                signs=tuple(signs),
                spans=tuple(spans),
            )
        )
    texts.sort(key=lambda item: item.side)
    return tuple(texts)


def _path_score(columns: Iterable[tuple[str | None, str | None]]) -> int:
    score = 0
    for left, right in columns:
        if left is None or right is None:
            score += GAP
        elif left == right:
            score += MATCH
        else:
            score += MISMATCH
    return score


def _identity_bp(matches: int, aligned: int) -> int:
    if aligned <= 0:
        return 0
    return (10000 * matches + aligned // 2) // aligned


def smith_waterman(
    seq_a: list[str] | tuple[str, ...],
    seq_b: list[str] | tuple[str, ...],
) -> tuple[int, int, int, int, int, list[tuple[str | None, str | None]]]:
    """Local alignment.

    Returns ``(score, a_start, a_end, b_start, b_end, columns)`` on the
    untrimmed Smith-Waterman path. Ends are exclusive. An empty alignment
    returns zeros and an empty column list.
    """
    n = len(seq_a)
    m = len(seq_b)
    if n == 0 or m == 0:
        return 0, 0, 0, 0, 0, []
    width = m + 1
    scores = array("i", [0]) * ((n + 1) * width)
    best = 0
    best_i = 0
    best_j = 0
    for i in range(1, n + 1):
        sign_a = seq_a[i - 1]
        row = i * width
        prev = row - width
        for j in range(1, m + 1):
            diagonal = scores[prev + j - 1] + (MATCH if sign_a == seq_b[j - 1] else MISMATCH)
            up = scores[prev + j] + GAP
            left = scores[row + j - 1] + GAP
            value = diagonal
            if up > value:
                value = up
            if left > value:
                value = left
            if value < 0:
                value = 0
            scores[row + j] = value
            if value > best:
                best = value
                best_i = i
                best_j = j
    if best <= 0:
        return 0, 0, 0, 0, 0, []
    columns: list[tuple[str | None, str | None]] = []
    i = best_i
    j = best_j
    while i > 0 and j > 0 and scores[i * width + j] > 0:
        sign_a = seq_a[i - 1]
        sign_b = seq_b[j - 1]
        current = scores[i * width + j]
        diagonal_score = MATCH if sign_a == sign_b else MISMATCH
        if current == scores[(i - 1) * width + (j - 1)] + diagonal_score:
            columns.append((sign_a, sign_b))
            i -= 1
            j -= 1
        elif current == scores[(i - 1) * width + j] + GAP:
            columns.append((sign_a, None))
            i -= 1
        else:
            columns.append((None, sign_b))
            j -= 1
    columns.reverse()
    return best, i, best_i, j, best_j, columns


def _consumed(columns: Iterable[tuple[str | None, str | None]]) -> tuple[int, int]:
    left = 0
    right = 0
    for sign_a, sign_b in columns:
        if sign_a is not None:
            left += 1
        if sign_b is not None:
            right += 1
    return left, right


def _is_match(column: tuple[str | None, str | None]) -> bool:
    left, right = column
    return left is not None and left == right


def _column_counts(columns: list[tuple[str | None, str | None]]) -> tuple[int, int, int, int, int]:
    """Matches, mismatches, gaps, left signs consumed, right signs consumed."""
    matches = mismatches = gaps = left = right = 0
    for sign_a, sign_b in columns:
        if sign_a is not None:
            left += 1
        if sign_b is not None:
            right += 1
        if sign_a is not None and sign_a == sign_b:
            matches += 1
        elif sign_a is None or sign_b is None:
            gaps += 1
        else:
            mismatches += 1
    return matches, mismatches, gaps, left, right


def _maximal_ranges(columns: list[tuple[str | None, str | None]]) -> list[tuple[int, int]]:
    """Subpaths that clear the gate and are not contained in a longer one.

    A path can be 75% identical overall and still contain two exact islands.
    Keeping only the whole path would drop both. Containing ranges are dropped
    so a perfect 8-mer inside a passing 20-mer is reported once, as the 20-mer.
    """
    n = len(columns)
    if n < MIN_SPAN:
        return []
    # Prefix counts make each subpath check O(1).
    match_prefix = [0]
    left_prefix = [0]
    right_prefix = [0]
    for sign_a, sign_b in columns:
        match_prefix.append(match_prefix[-1] + (1 if sign_a is not None and sign_a == sign_b else 0))
        left_prefix.append(left_prefix[-1] + (1 if sign_a is not None else 0))
        right_prefix.append(right_prefix[-1] + (1 if sign_b is not None else 0))
    good: list[tuple[int, int]] = []
    min_identity = int(MIN_IDENTITY * 10000)
    for start in range(n):
        if not _is_match(columns[start]):
            continue
        for end in range(start + MIN_SPAN, n + 1):
            if not _is_match(columns[end - 1]):
                continue
            aligned = end - start
            matches = match_prefix[end] - match_prefix[start]
            if _identity_bp(matches, aligned) < min_identity:
                continue
            left = left_prefix[end] - left_prefix[start]
            right = right_prefix[end] - right_prefix[start]
            if max(left, right) < MIN_SPAN:
                continue
            good.append((start, end))
    maximal: list[tuple[int, int]] = []
    for start, end in sorted(good, key=lambda item: (item[0] - item[1], item[0])):
        if any(other_start <= start and end <= other_end for other_start, other_end in maximal):
            continue
        maximal.append((start, end))
    return maximal


def _passage_from_slice(
    left: SideText,
    right: SideText,
    full_a: int,
    full_b: int,
    columns: list[tuple[str | None, str | None]],
    start: int,
    end: int,
) -> Passage:
    prefix_a, prefix_b = _consumed(columns[:start])
    piece = columns[start:end]
    keep_a, keep_b = _consumed(piece)
    matches, mismatches, gaps, _left, _right = _column_counts(piece)
    return Passage(
        left_side=left.side,
        right_side=right.side,
        left_tablet=left.tablet,
        right_tablet=right.tablet,
        left_start=full_a + prefix_a,
        left_end=full_a + prefix_a + keep_a,
        right_start=full_b + prefix_b,
        right_end=full_b + prefix_b + keep_b,
        score=_path_score(piece),
        matches=matches,
        mismatches=mismatches,
        gaps=gaps,
        span=max(keep_a, keep_b),
        identity_bp=_identity_bp(matches, len(piece)),
        columns=tuple(piece),
    )


def align_window(
    left: SideText,
    right: SideText,
    a0: int,
    a1: int,
    b0: int,
    b1: int,
) -> list[Passage]:
    """Gated subpaths of one Smith-Waterman trace.

    The trace is the single best local path in the slice. Every maximal
    subpath that clears the length and identity gates is returned, so an
    exact island inside a looser path is kept.
    """
    if a1 <= a0 or b1 <= b0:
        return []
    _raw, start_a, _end_a, start_b, _end_b, columns = smith_waterman(
        left.signs[a0:a1], right.signs[b0:b1]
    )
    if not columns:
        return []
    full_a = a0 + start_a
    full_b = b0 + start_b
    return [
        _passage_from_slice(left, right, full_a, full_b, columns, start, end)
        for start, end in _maximal_ranges(columns)
    ]


def _kmer_index(signs: tuple[str, ...]) -> dict[tuple[str, ...], list[int]]:
    buckets: dict[tuple[str, ...], list[int]] = defaultdict(list)
    last = len(signs) - SEED + 1
    for index in range(max(0, last)):
        buckets[signs[index : index + SEED]].append(index)
    return buckets


def _cluster_hits(hits: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    if not hits:
        return []
    bands: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for i, j in hits:
        bands[(i - j) // SEED_BAND].append((i, j))
    chains: list[list[tuple[int, int]]] = []
    for group in bands.values():
        group.sort()
        current = [group[0]]
        prev_i, prev_j = group[0]
        for i, j in group[1:]:
            if i == prev_i and j == prev_j:
                continue
            forward = i > prev_i and j >= prev_j
            close = (i - prev_i) <= MAX_SEED_GAP and (j - prev_j) <= MAX_SEED_GAP
            if forward and close:
                current.append((i, j))
                prev_i, prev_j = i, j
            else:
                chains.append(current)
                current = [(i, j)]
                prev_i, prev_j = i, j
        chains.append(current)
    return chains


def _overlap_ratio(a0: int, a1: int, b0: int, b1: int) -> float:
    inter = min(a1, b1) - max(a0, b0)
    if inter <= 0:
        return 0.0
    shorter = min(a1 - a0, b1 - b0)
    if shorter <= 0:
        return 0.0
    return inter / shorter


def _same_locus(a: Passage, b: Passage) -> bool:
    return (
        _overlap_ratio(a.left_start, a.left_end, b.left_start, b.left_end) > OVERLAP_FRACTION
        and _overlap_ratio(a.right_start, a.right_end, b.right_start, b.right_end) > OVERLAP_FRACTION
    )


def _dedupe(passages: list[Passage]) -> list[Passage]:
    ranked = sorted(passages, key=lambda item: (-item.score, -item.span, item.left_start, item.right_start))
    kept: list[Passage] = []
    for passage in ranked:
        if any(_same_locus(passage, other) for other in kept):
            continue
        kept.append(passage)
    return kept


def _pair_bridge(a: Passage, b: Passage) -> bool:
    if a.left_start > b.left_start:
        a, b = b, a
    if b.right_start < a.right_start:
        return False
    left_gap = b.left_start - a.left_end
    right_gap = b.right_start - a.right_end
    if left_gap < -2 or right_gap < -2:
        return False
    if left_gap > MAX_BRIDGE or right_gap > MAX_BRIDGE:
        return False
    return abs(left_gap - right_gap) <= BRIDGE_SLACK


def _covers(host: Passage, piece: Passage) -> bool:
    return (
        _overlap_ratio(host.left_start, host.left_end, piece.left_start, piece.left_end) >= COVER_FRACTION
        and _overlap_ratio(host.right_start, host.right_end, piece.right_start, piece.right_end)
        >= COVER_FRACTION
    )


def _bridge(left: SideText, right: SideText, passages: list[Passage]) -> list[Passage]:
    current = list(passages)
    changed = True
    while changed:
        changed = False
        current.sort(key=lambda item: (item.left_start, item.right_start, -item.score))
        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                if not _pair_bridge(current[i], current[j]):
                    continue
                a0 = min(current[i].left_start, current[j].left_start)
                a1 = max(current[i].left_end, current[j].left_end)
                b0 = min(current[i].right_start, current[j].right_start)
                b1 = max(current[i].right_end, current[j].right_end)
                candidates = [
                    item
                    for item in align_window(left, right, a0, a1, b0, b1)
                    if _covers(item, current[i]) and _covers(item, current[j])
                ]
                if not candidates:
                    continue
                bridged = max(candidates, key=lambda item: (item.score, item.span))
                if bridged.score < max(current[i].score, current[j].score):
                    continue
                replacement = [item for index, item in enumerate(current) if index not in (i, j)]
                replacement.append(bridged)
                current = replacement
                changed = True
                break
            if changed:
                break
    return current


def _chain_bounds(chain: list[tuple[int, int]]) -> tuple[int, int, int, int]:
    i0 = min(i for i, _j in chain)
    i1 = max(i for i, _j in chain) + SEED
    j0 = min(j for _i, j in chain)
    j1 = max(j for _i, j in chain) + SEED
    return i0, i1, j0, j1


def _seed_covered(passage: Passage, i: int, j: int) -> bool:
    return (
        passage.left_start <= i
        and i + SEED <= passage.left_end
        and passage.right_start <= j
        and j + SEED <= passage.right_end
    )


def _split_chain(chain: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]] | None:
    """Split a chain at its widest forward gap so a failed window can be retried."""
    ordered = sorted(set(chain))
    if len(ordered) < 2:
        return None
    split_at = max(range(len(ordered) - 1), key=lambda index: ordered[index + 1][0] - ordered[index][0])
    left = ordered[: split_at + 1]
    right = ordered[split_at + 1 :]
    if not left or not right:
        return None
    return left, right


def _harvest_chain(
    left: SideText,
    right: SideText,
    chain: list[tuple[int, int]],
    seen: set[tuple[int, int, int, int]],
    depth: int = 0,
) -> list[Passage]:
    """Best gated path in the chain window, then any gated path the best one missed.

    One Smith-Waterman run returns a single local path. A chain that jumps a
    divergent stretch can hide a shorter exact island inside that window. Seeds
    the winning path does not cover are searched again. A window that fails the
    gate is split at its widest seed gap.
    """
    if not chain or depth > 24:
        return []
    i0, i1, j0, j1 = _chain_bounds(chain)
    if max(i1 - i0, j1 - j0) < MIN_SPAN and len(chain) < 2:
        return []
    a0 = max(0, i0 - MARGIN)
    b0 = max(0, j0 - MARGIN)
    a1 = min(len(left.signs), i1 + MARGIN)
    b1 = min(len(right.signs), j1 + MARGIN)
    window = (a0, a1, b0, b1)
    if window in seen:
        return []
    seen.add(window)
    passages = align_window(left, right, a0, a1, b0, b1)
    if not passages:
        parts = _split_chain(chain)
        if parts is None:
            return []
        return _harvest_chain(left, right, parts[0], seen, depth + 1) + _harvest_chain(
            left, right, parts[1], seen, depth + 1
        )
    found = list(passages)
    uncovered = [
        (i, j) for i, j in chain if not any(_seed_covered(passage, i, j) for passage in passages)
    ]
    if uncovered and len(uncovered) < len(chain):
        for sub in _cluster_hits(uncovered):
            found.extend(_harvest_chain(left, right, sub, seen, depth + 1))
    elif len(uncovered) == len(chain):
        parts = _split_chain(chain)
        if parts is not None:
            found.extend(_harvest_chain(left, right, parts[0], seen, depth + 1))
            found.extend(_harvest_chain(left, right, parts[1], seen, depth + 1))
    return found


def align_pair(left: SideText, right: SideText, index_right: dict[tuple[str, ...], list[int]]) -> list[Passage]:
    """Every gated local alignment between two sides of different tablets."""
    hits: list[tuple[int, int]] = []
    last = len(left.signs) - SEED + 1
    for i in range(max(0, last)):
        key = left.signs[i : i + SEED]
        positions = index_right.get(key)
        if not positions:
            continue
        if len(positions) > REPETITIVE_KMER and i % SEED != 0:
            continue
        hits.extend((i, j) for j in positions)
    found: list[Passage] = []
    seen: set[tuple[int, int, int, int]] = set()
    for chain in _cluster_hits(hits):
        found.extend(_harvest_chain(left, right, chain, seen))
    found = _dedupe(found)
    found = _bridge(left, right, found)
    return _dedupe(found)


def find_passages(sides: tuple[SideText, ...]) -> list[Passage]:
    """Cross-tablet passages. Sides of one tablet are not aligned."""
    indexes = {side.side: _kmer_index(side.signs) for side in sides}
    passages: list[Passage] = []
    for i, left in enumerate(sides):
        for right in sides[i + 1 :]:
            if left.tablet == right.tablet:
                continue
            passages.extend(align_pair(left, right, indexes[right.side]))
    return passages


def shuffle_sides(sides: tuple[SideText, ...], seed: int) -> tuple[SideText, ...]:
    """Each side keeps its own signs and its line spans. Order is destroyed."""
    generator = random.Random(seed)
    shuffled: list[SideText] = []
    for side in sides:
        signs = list(side.signs)
        generator.shuffle(signs)
        shuffled.append(
            SideText(
                tablet=side.tablet,
                side=side.side,
                path=side.path,
                signs=tuple(signs),
                spans=side.spans,
            )
        )
    return tuple(shuffled)


def null_max_scores(sides: tuple[SideText, ...], trials: int, seed: int) -> list[int]:
    """Best gated score in each within-side shuffle. Missing alignments score 0."""
    scores: list[int] = []
    for trial in range(trials):
        best = 0
        for passage in find_passages(shuffle_sides(sides, seed + trial)):
            if passage.score > best:
                best = passage.score
        scores.append(best)
    return scores


def _locus(side: SideText, start: int, end: int) -> dict[str, Any]:
    start_line, start_offset = side.locate(start)
    end_line, end_offset = side.locate(end - 1)
    if start_line == end_line:
        text = f"{start_line}:{start_offset}-{end_offset}"
    else:
        text = f"{start_line}:{start_offset}..{end_line}:{end_offset}"
    return {
        "side": side.side,
        "tablet": side.tablet,
        "start": start,
        "end": end,
        "start_line": start_line,
        "start_offset": start_offset,
        "end_line": end_line,
        "end_offset": end_offset,
        "locus": text,
    }


def _published_status(pair: frozenset[str]) -> dict[str, str]:
    info = PUBLISHED_PAIRS.get(pair)
    if info is None:
        tablets = "–".join(sorted(pair))
        return {
            "status": "uncited",
            "label": tablets,
            "source": (
                "This tablet pair is not among H–P, H–Q, P–Q, G–K, or A–R "
                "in the sources cited for this track"
            ),
        }
    return {"status": "published", "label": info["label"], "source": info["source"]}


def _column_groups(passages: list[dict[str, Any]]) -> list[list[tuple[str, str]]]:
    groups: list[list[tuple[str, str]]] = []
    for passage in passages:
        if not passage["significant"]:
            continue
        columns = [
            (left, right)
            for left, right in passage["columns"]
            if left is not None and right is not None
        ]
        groups.append(columns)
    return groups


def _observed_pairs(groups: list[list[tuple[str, str]]]) -> Counter[tuple[str, str]]:
    counts: Counter[tuple[str, str]] = Counter()
    for columns in groups:
        for left, right in columns:
            if left == right:
                continue
            counts[tuple(sorted((left, right)))] += 1
    return counts


def _pair_null(
    groups: list[list[tuple[str, str]]],
    observed: Counter[tuple[str, str]],
    trials: int,
    seed: int,
) -> tuple[dict[tuple[str, str], int], int]:
    """Re-pair signs that already occupy mismatch columns.

    Matches stay put. Shuffling every column would invent a much higher
    mismatch rate than an alignment that was required to be 80% identical,
    and that rate sits above any real substitution count. The null here
    asks whether the observed disagreements repeat the same pair.

    Returns ``(times the null count reached the observed count, family max)``.
    The family max is the largest count any pair reached in any trial.
    """
    mismatch_groups = [[(left, right) for left, right in columns if left != right] for columns in groups]
    generator = random.Random(seed)
    reached = {pair: 0 for pair in observed}
    family_max = 0
    for _trial in range(trials):
        counts: Counter[tuple[str, str]] = Counter()
        for columns in mismatch_groups:
            if len(columns) < 2:
                continue
            right = [sign for _left, sign in columns]
            generator.shuffle(right)
            for (left, _old), sign in zip(columns, right):
                if left == sign:
                    continue
                counts[tuple(sorted((left, sign)))] += 1
        if counts:
            family_max = max(family_max, max(counts.values()))
        for pair, count in observed.items():
            if counts.get(pair, 0) >= count:
                reached[pair] += 1
    return reached, family_max


def _indel_events(passage: dict[str, Any]) -> list[dict[str, str]]:
    """One event per extra sign that has a neighbor on both sides."""
    columns = passage["columns"]
    events: list[dict[str, str]] = []
    index = 0
    while index < len(columns):
        left, right = columns[index]
        if left is not None and right is None:
            host = "left"
        elif left is None and right is not None:
            host = "right"
        else:
            index += 1
            continue
        end = index + 1
        while end < len(columns):
            next_left, next_right = columns[end]
            if host == "left" and next_left is not None and next_right is None:
                end += 1
                continue
            if host == "right" and next_left is None and next_right is not None:
                end += 1
                continue
            break
        neighbor_left = _neighbor(columns, index, host, step=-1)
        neighbor_right = _neighbor(columns, end, host, step=1)
        if neighbor_left is None or neighbor_right is None:
            index = end
            continue
        for cursor in range(index, end):
            sign = columns[cursor][0] if host == "left" else columns[cursor][1]
            if sign is None:
                continue
            events.append(
                {
                    "sign": sign,
                    "left_neighbor": neighbor_left,
                    "right_neighbor": neighbor_right,
                    "host": host,
                    "passage_id": passage["id"],
                    "side": passage["left"]["side"] if host == "left" else passage["right"]["side"],
                }
            )
        index = end
    return events


def _neighbor(
    columns: list[list[str | None]] | list[tuple[str | None, str | None]],
    start: int,
    host: str,
    step: int,
) -> str | None:
    slot = 0 if host == "left" else 1
    index = start - 1 if step < 0 else start
    while 0 <= index < len(columns):
        sign = columns[index][slot]
        if sign is not None:
            return sign
        index += step
    return None


def _classify_patterns(
    counts: Counter[tuple[str, ...]],
    reached: dict[tuple[str, ...], int],
    family_max: int,
    trials: int,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for key, count in counts.items():
        ge_count = reached.get(key, 0)
        clears = (1 + ge_count) * SYSTEMATIC_P_DEN <= (trials + 1) * SYSTEMATIC_P_NUM
        if count >= MIN_SYSTEMATIC_COUNT and clears:
            kind = "systematic"
        elif count >= MIN_SYSTEMATIC_COUNT:
            kind = "recurrent"
        elif count == 2:
            kind = "double"
        else:
            kind = "hapax"
        rows.append(
            {
                "count": count,
                "null_ge": ge_count,
                "null_trials": trials,
                "above_family_max": count > family_max,
                "kind": kind,
                "key": list(key),
            }
        )
    rows.sort(key=lambda item: (-int(item["count"]), item["kind"], item["key"]))
    return rows


def _substitution_report(
    passages: list[dict[str, Any]],
    frequencies: Counter[str],
) -> dict[str, Any]:
    groups = _column_groups(passages)
    observed = _observed_pairs(groups)
    reached, family_max = _pair_null(groups, observed, PAIR_TRIALS, PAIR_SEED)
    classified = _classify_patterns(observed, reached, family_max, PAIR_TRIALS)
    examples: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for passage in passages:
        if not passage["significant"]:
            continue
        for left, right in passage["columns"]:
            if left is None or right is None or left == right:
                continue
            pair = tuple(sorted((left, right)))
            bucket = examples[pair]
            if len(bucket) >= 6:
                continue
            bucket.append(
                {
                    "passage_id": passage["id"],
                    "left_side": passage["left"]["side"],
                    "right_side": passage["right"]["side"],
                    "left_locus": passage["left"]["locus"],
                    "right_locus": passage["right"]["locus"],
                    "left_sign": left,
                    "right_sign": right,
                }
            )
    pairs: list[dict[str, Any]] = []
    for row in classified:
        key = tuple(row["key"])
        if row["kind"] == "hapax":
            continue
        pairs.append(
            {
                "a": key[0],
                "b": key[1],
                "count": row["count"],
                "kind": row["kind"],
                "null_ge": row["null_ge"],
                "null_trials": row["null_trials"],
                "above_family_max": row["above_family_max"],
                "examples": examples[key],
            }
        )
    systematic_edges = [(row["a"], row["b"], row["count"]) for row in pairs if row["kind"] == "systematic"]
    classes = _classes(systematic_edges, frequencies)
    merge: dict[str, str] = {}
    for item in classes:
        for member in item["members"]:
            merge[member] = item["representative"]
    hapax = sum(1 for row in classified if row["kind"] == "hapax")
    hand = next((row for row in pairs if row["a"] == HAND_PAIR[0] and row["b"] == HAND_PAIR[1]), None)
    hand_class = any(set(HAND_PAIR) <= set(item["members"]) for item in classes)
    return {
        "family_max_count": family_max,
        "pair_trials": PAIR_TRIALS,
        "pair_seed": PAIR_SEED,
        "min_systematic_count": MIN_SYSTEMATIC_COUNT,
        "hapax_pairs": hapax,
        "pairs": pairs,
        "classes": classes,
        "merge_table": dict(sorted(merge.items())),
        "hand_pair_006_064": {
            "pair": list(HAND_PAIR),
            "observed_count": 0 if hand is None else hand["count"],
            "kind": "absent" if hand is None else hand["kind"],
            "in_systematic_class": hand_class,
            "citation": (
                "Barthel 006 and 064 are the hand pair this repository already "
                "records from Pozdniakov's parallel phrases. This track does not "
                "force that merge."
            ),
        },
    }


def _classes(edges: list[tuple[str, str, int]], frequencies: Counter[str]) -> list[dict[str, Any]]:
    parent: dict[str, str] = {}

    def find(sign: str) -> str:
        parent.setdefault(sign, sign)
        while parent[sign] != sign:
            parent[sign] = parent[parent[sign]]
            sign = parent[sign]
        return sign

    def union(left: str, right: str) -> None:
        ra, rb = find(left), find(right)
        if ra == rb:
            return
        if ra < rb:
            parent[rb] = ra
        else:
            parent[ra] = rb

    for left, right, _count in edges:
        union(left, right)
    groups: dict[str, list[str]] = defaultdict(list)
    for sign in parent:
        groups[find(sign)].append(sign)
    edge_counts: dict[tuple[str, str], int] = {(left, right): count for left, right, count in edges}
    classes: list[dict[str, Any]] = []
    for members_unsorted in groups.values():
        members = sorted(members_unsorted)
        representative = min(members, key=lambda sign: (-frequencies.get(sign, 0), sign))
        member_set = set(members)
        class_edges = [
            {"a": left, "b": right, "count": count}
            for (left, right), count in sorted(edge_counts.items())
            if left in member_set and right in member_set
        ]
        classes.append(
            {
                "members": members,
                "representative": representative,
                "size": len(members),
                "wide": len(members) >= 8,
                "pair_count": sum(item["count"] for item in class_edges),
                "edges": class_edges,
                "corpus_counts": {sign: frequencies.get(sign, 0) for sign in members},
            }
        )
    classes.sort(key=lambda item: (-item["pair_count"], item["representative"]))
    for index, item in enumerate(classes, start=1):
        item["id"] = f"S{index:02d}"
    return classes


def _indel_report(passages: list[dict[str, Any]]) -> dict[str, Any]:
    significant = [passage for passage in passages if passage["significant"]]
    events: list[dict[str, str]] = []
    for passage in significant:
        events.extend(_indel_events(passage))
    observed: Counter[tuple[str, str, str]] = Counter(
        (event["sign"], event["left_neighbor"], event["right_neighbor"]) for event in events
    )
    generator = random.Random(INDEL_SEED)
    reached = {key: 0 for key in observed}
    family_max = 0
    if events:
        for _trial in range(INDEL_TRIALS):
            signs = [event["sign"] for event in events]
            generator.shuffle(signs)
            counts: Counter[tuple[str, str, str]] = Counter()
            for event, sign in zip(events, signs):
                counts[(sign, event["left_neighbor"], event["right_neighbor"])] += 1
            family_max = max(family_max, max(counts.values()))
            for key, count in observed.items():
                if counts.get(key, 0) >= count:
                    reached[key] += 1
    classified = _classify_patterns(observed, reached, family_max, INDEL_TRIALS)
    examples: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for event in events:
        key = (event["sign"], event["left_neighbor"], event["right_neighbor"])
        bucket = examples[key]
        if len(bucket) >= 6:
            continue
        bucket.append(
            {
                "passage_id": event["passage_id"],
                "side": event["side"],
                "host": event["host"],
            }
        )
    rows: list[dict[str, Any]] = []
    hapax = 0
    for row in classified:
        if row["kind"] == "hapax":
            hapax += 1
            continue
        key = tuple(row["key"])
        rows.append(
            {
                "sign": key[0],
                "left_neighbor": key[1],
                "right_neighbor": key[2],
                "count": row["count"],
                "kind": row["kind"],
                "null_ge": row["null_ge"],
                "null_trials": row["null_trials"],
                "above_family_max": row["above_family_max"],
                "examples": examples[key],
            }
        )
    return {
        "family_max_count": family_max,
        "indel_trials": INDEL_TRIALS,
        "indel_seed": INDEL_SEED,
        "events": len(events),
        "hapax_patterns": hapax,
        "patterns": rows,
    }


def _passage_dict(
    passage: Passage,
    sides: dict[str, SideText],
    significant: bool,
    identifier: str,
) -> dict[str, Any]:
    status = _published_status(passage.pair_key)
    record: dict[str, Any] = {
        "id": identifier,
        "left": _locus(sides[passage.left_side], passage.left_start, passage.left_end),
        "right": _locus(sides[passage.right_side], passage.right_start, passage.right_end),
        "score": passage.score,
        "span": passage.span,
        "matches": passage.matches,
        "mismatches": passage.mismatches,
        "gaps": passage.gaps,
        "aligned_length": passage.aligned_length,
        "identity_bp": passage.identity_bp,
        "significant": significant,
        "publication": status["status"],
        "publication_label": status["label"],
    }
    if significant:
        record["columns"] = [[left, right] for left, right in passage.columns]
    return record


def _compare(passages: list[dict[str, Any]]) -> dict[str, Any]:
    significant = [passage for passage in passages if passage["significant"]]
    found: dict[str, int] = {info["label"]: 0 for info in PUBLISHED_PAIRS.values()}
    uncited: Counter[str] = Counter()
    staff: Counter[str] = Counter()
    for passage in significant:
        label = passage["publication_label"]
        if passage["publication"] == "published":
            found[label] += 1
        else:
            uncited[label] += 1
        tablets = {passage["left"]["tablet"], passage["right"]["tablet"]}
        if "I" in tablets:
            other = next(iter(tablets - {"I"}))
            staff[other] += 1
    missing = [label for label, count in found.items() if count == 0]
    recovered = [label for label, count in found.items() if count > 0]
    return {
        "published_passage_counts": found,
        "published_recovered": recovered,
        "published_absent": missing,
        "uncited_pairs": [
            {"tablets": tablets, "passages": count}
            for tablets, count in sorted(uncited.items(), key=lambda item: (-item[1], item[0]))
        ],
        "staff_i_partners": [
            {"tablet": tablet, "passages": count}
            for tablet, count in sorted(staff.items())
        ],
    }


def analyze_encoding(
    mode: str,
    *,
    null_trials: int = NULL_TRIALS,
    keep_columns: bool = True,
) -> dict[str, Any]:
    """Passages, null, substitutions, and indels for one encoding."""
    sides = load_side_texts(mode)
    by_side = {side.side: side for side in sides}
    frequencies: Counter[str] = Counter(sign for side in sides for sign in side.signs)
    raw = find_passages(sides)
    null_scores = null_max_scores(sides, null_trials, NULL_SEED)
    threshold = max(null_scores) if null_scores else 0
    ranked = sorted(raw, key=lambda item: (-item.score, item.left_side, item.right_side, item.left_start))
    passages = [
        _passage_dict(
            passage,
            by_side,
            passage.score > threshold,
            f"P{index:03d}",
        )
        for index, passage in enumerate(ranked, start=1)
    ]
    if not keep_columns:
        for passage in passages:
            passage.pop("columns", None)
    substitutions = _substitution_report(passages, frequencies) if keep_columns else {}
    indels = _indel_report(passages) if keep_columns else {}
    comparison = _compare(passages)
    return {
        "encoding": mode,
        "decompose_ligatures": mode == "stem",
        "corpus": {
            "sides": [
                {
                    "side": side.side,
                    "tablet": side.tablet,
                    "path": side.path,
                    "signs": len(side.signs),
                    "lines": len(side.spans),
                }
                for side in sides
            ],
            "side_count": len(sides),
            "tokens": sum(frequencies.values()),
            "inventory": len(frequencies),
        },
        "gates": {
            "seed": SEED,
            "min_span": MIN_SPAN,
            "min_identity_bp": int(MIN_IDENTITY * 10000),
            "match": MATCH,
            "mismatch": MISMATCH,
            "gap": GAP,
            "null_trials": null_trials,
            "null_seed": NULL_SEED,
        },
        "null": {
            "scores": null_scores,
            "max_score": threshold,
            "median_score": _median(null_scores),
        },
        "passages": passages,
        "significant_passages": sum(1 for passage in passages if passage["significant"]),
        "candidate_passages": len(passages),
        "substitutions": substitutions,
        "indels": indels,
        "published_comparison": comparison,
    }


def _median(values: list[int]) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) // 2


def run_track_c(provider: MockProvider | None = None) -> dict[str, Any]:
    """Run both encodings. The provider is not asked for a completion."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Track C accepts MockProvider only")
    stem = analyze_encoding("stem")
    ligature = analyze_encoding("ligature_atomic", keep_columns=True)
    return {
        "track": "round2_trackC",
        "version": 1,
        "provider": "MockProvider",
        "readings_assigned": False,
        "primary_encoding": "stem",
        "stem": stem,
        "ligature_atomic": _ligature_summary(ligature),
        "merge_table": stem["substitutions"]["merge_table"],
    }


def _ligature_summary(full: dict[str, Any]) -> dict[str, Any]:
    """Keep ligature passages and classes, drop column strings to limit size."""
    passages = []
    for passage in full["passages"]:
        brief = {key: value for key, value in passage.items() if key != "columns"}
        passages.append(brief)
    summary = dict(full)
    summary["passages"] = passages
    return summary


def render_json(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def _bp(identity_bp: int) -> str:
    return f"{identity_bp / 10000:.4f}"


def _fraction(ge_count: int, trials: int) -> str:
    return f"{ge_count + 1}/{trials + 1}"


def _pair_row(subs: dict[str, Any], left: str, right: str) -> dict[str, Any] | None:
    a, b = sorted((left, right))
    for row in subs["pairs"]:
        if row["a"] == a and row["b"] == b:
            return row
    return None


def _class_holding(subs: dict[str, Any], left: str, right: str) -> dict[str, Any] | None:
    wanted = {left, right}
    for item in subs["classes"]:
        if wanted <= set(item["members"]):
            return item
    return None


def _pair_phrase(subs: dict[str, Any], left: str, right: str) -> str:
    row = _pair_row(subs, left, right)
    label = f"{left}/{right}"
    if row is None:
        return f"{label} is absent from pairs that occur at least twice"
    held = _class_holding(subs, left, right)
    detail = f"{label} has count {row['count']} and kind `{row['kind']}`"
    if held is not None:
        detail += (
            f" (class {held['id']}, representative {held['representative']})"
        )
    return detail


def render_markdown(result: dict[str, Any]) -> str:
    stem = result["stem"]
    ligature = result["ligature_atomic"]
    subs = stem["substitutions"]
    indels = stem["indels"]
    comparison = stem["published_comparison"]
    lines: list[str] = []
    lines.append("# Round 2, Track C — Parallel passages and substitution classes")
    lines.append("")
    lines.append(
        "This note finds repeated passages across tablets and the sign substitutions inside them. "
        "It assigns no readings. The provider is MockProvider and is never asked for a completion. "
        "Counts below are produced by `decipherment/track_c_parallels.py` from the vendored Kohaumotu Barthel HTML."
    )
    lines.append("")
    lines.append("## Corpus and encoding")
    lines.append("")
    lines.append(
        f"The loader is `load_located_sides`. Sides with no digit transcription are omitted "
        f"({stem['corpus']['side_count']} sides, {stem['corpus']['tokens']} stem tokens, "
        f"{stem['corpus']['inventory']} stem types). A tablet is the first letter of the side code, "
        "so Hr and Hv are one tablet and are not aligned to each other. Lines of one side are concatenated. "
        "A line name such as `Hr8` is the Kohaumotu line number. Offsets are 0-based and inclusive, "
        "the same convention as the H/P/Q scoreboards. The end offset in a same-line locus is inclusive."
    )
    lines.append("")
    lines.append(
        "The primary encoding is `stem`: ligatures written with `.` or `:` are split, allograph letters "
        "and a leading orientation `V` are stripped, and illegible `000` is dropped. That is ligature "
        "decomposition. The option `ligature_atomic` keeps each dot or colon ligature as one sign. "
        "The merge table other tracks should consume is the stem table."
    )
    lines.append("")
    lines.append("| Side | Tablet | Stems | Lines | Fixture |")
    lines.append("| --- | --- | ---: | ---: | --- |")
    for side in stem["corpus"]["sides"]:
        lines.append(
            f"| {side['side']} | {side['tablet']} | {side['signs']} | {side['lines']} | `{side['path']}` |"
        )
    lines.append("")
    lines.append("## Matching")
    lines.append("")
    lines.append(
        "Seeds are exact stem 3-mers. Seeds on one diagonal band are chained when the gap is at most "
        f"{MAX_SEED_GAP} signs. Each chain is extended by Smith-Waterman "
        "(Smith and Waterman 1981) with match +2, mismatch −1, and a linear gap −1. "
        "One trace can hold two exact islands separated by a looser stretch. Every maximal subpath "
        "that still clears the gates is kept, so the islands are not dropped with the stretch. "
        "A repetitive 3-mer, one that occurs more than "
        f"{REPETITIVE_KMER} times on the target side, is seeded on every third query position so a run "
        "cannot explode the hit list. Nearby gated hits on the same sides are joined and realigned when "
        f"the gap is at most {MAX_BRIDGE} signs and the two gap lengths differ by at most {BRIDGE_SLACK}."
    )
    lines.append("")
    lines.append(
        f"A passage is kept when the longer copy covers at least {MIN_SPAN} stems, identity is at least "
        f"{MIN_IDENTITY:.2f}, and both end columns are matches. Identity is matches divided by columns "
        "(matches, mismatches, and gaps). This is the same 20% error budget Sproat (2003) used, with two "
        "differences: Sproat also required the last two glyphs to match, and he searched fixed lengths "
        "from a suffix array (Manber and Myers 1993) with the edit distance in Sankoff and Kruskal (1983). "
        "This search uses local alignment and lets the length fall out of the path."
    )
    lines.append("")
    lines.append(
        f"The null shuffles signs inside each side ({NULL_TRIALS} trials, seed {NULL_SEED}) and reruns the "
        f"same search. Each side keeps its inventory and its length. The threshold is the best score seen "
        f"in any trial. A passage is significant when its score is higher than that maximum. "
        f"Here the null maximum is {stem['null']['max_score']} and the null median is {stem['null']['median_score']}. "
        f"Null trial maxima: {', '.join(str(score) for score in stem['null']['scores'])}."
    )
    lines.append("")
    lines.append(
        f"Gated passages: {stem['candidate_passages']}. Significant passages: {stem['significant_passages']}."
    )
    lines.append("")
    lines.append("## Passages")
    lines.append("")
    lines.append(
        "H in this corpus is the Great Santiago tablet, P is the Great St. Petersburg tablet, and Q is the "
        "Small St. Petersburg tablet. Small Santiago is G. The long parallel discussed as the Great Tradition "
        "is H/P/Q. G parallels London K."
    )
    lines.append("")
    lines.append(
        "| Id | Tablets | Loci | Span | Identity | Score | Mismatches | Gaps | Status |"
    )
    lines.append("| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |")
    for passage in stem["passages"]:
        if not passage["significant"]:
            continue
        loci = f"{passage['left']['locus']} ‖ {passage['right']['locus']}"
        lines.append(
            "| {id} | {label} | {loci} | {span} | {ident} | {score} | {mis} | {gaps} | {status} |".format(
                id=passage["id"],
                label=passage["publication_label"],
                loci=loci,
                span=passage["span"],
                ident=_bp(passage["identity_bp"]),
                score=passage["score"],
                mis=passage["mismatches"],
                gaps=passage["gaps"],
                status=passage["publication"],
            )
        )
    lines.append("")
    nonsig = [passage for passage in stem["passages"] if not passage["significant"]]
    if nonsig:
        lines.append(
            f"{len(nonsig)} gated passages score at or below the null maximum and stay out of the substitution counts. "
            "Their loci are in `data/decipherment/substitution_classes.json` under `stem.passages` with `significant` false."
        )
        lines.append("")
    lines.append("## Published parallels")
    lines.append("")
    lines.append(
        "Recovered published pairs: "
        + (", ".join(comparison["published_recovered"]) if comparison["published_recovered"] else "none")
        + ". Named pairs with no significant passage on this stemming: "
        + (", ".join(comparison["published_absent"]) if comparison["published_absent"] else "none")
        + "."
    )
    lines.append("")
    for info in PUBLISHED_PAIRS.values():
        count = comparison["published_passage_counts"][info["label"]]
        lines.append(f"- **{info['label']}** ({count} significant): {info['source']}.")
    lines.append("")
    if comparison["uncited_pairs"]:
        rendered = ", ".join(
            f"{item['tablets']} ({item['passages']})" for item in comparison["uncited_pairs"]
        )
        lines.append(
            "Significant pairs outside that named list, flagged here as uncited rather than as a claim of priority: "
            + rendered
            + ". Sproat (2003) already notes shorter matches between various tablets beyond the long H/P/Q and G/K blocks, "
            "without listing every pair in the synopsis this track uses."
        )
    else:
        lines.append(
            "Every significant pair is one of the named published pairs. No extra tablet pair cleared the null."
        )
    lines.append("")
    if comparison["staff_i_partners"]:
        partners = ", ".join(
            f"{item['tablet']} ({item['passages']})" for item in comparison["staff_i_partners"]
        )
        lines.append(
            f"Santiago Staff (I) shares significant passages with: {partners}. "
            "Sproat (2003) describes the Staff as an isolate under his match rules. A partner listed here cleared this track's null."
        )
    else:
        lines.append(
            "Santiago Staff (I) has no significant cross-tablet passage. That agrees with Sproat (2003), "
            "who found the Staff isolated, and with Pozdniakov (1996: 299) as cited by Horley (2007)."
        )
    lines.append("")
    sproat = [
        passage
        for passage in stem["passages"]
        if passage["significant"]
        and passage["left"]["locus"].startswith("Hr2:36")
        and passage["right"]["locus"].startswith("Qr2:0")
        and passage["span"] == 125
    ]
    if sproat:
        lines.append(
            "P001 is that Sproat anchor on this transcription: Great Santiago recto line 2 at offset 36 "
            f"({sproat[0]['left']['locus']}) against Small St. Petersburg recto line 2 at offset 0 "
            f"({sproat[0]['right']['locus']}), span {sproat[0]['span']}, identity {_bp(sproat[0]['identity_bp'])}, "
            f"score {sproat[0]['score']}."
        )
        lines.append("")
    lines.append(
        "Horley's A–R passage used a glyph-element transcription. An absence under Barthel stems means this "
        "encoding did not keep a span of 8 at identity 0.80 above the null. It is not a claim that his parallel is absent in his own encoding."
    )
    lines.append("")
    lines.append("## Substitution classes")
    lines.append("")
    lines.append(
        "Substitutions are mismatch columns in significant passages only. The pair is unordered. "
        f"The null re-pairs only those mismatch columns ({PAIR_TRIALS} trials, seed {PAIR_SEED}). "
        "Matches stay matched. A shuffle of every column would create far more mismatches than an "
        "alignment that already had to be 80% identical, and that artificial rate sits above the substitution counts. "
        f"The busiest pair in any trial reached {subs['family_max_count']}. "
        f"A pair is systematic when its count is at least {MIN_SYSTEMATIC_COUNT} and "
        f"(1 + null hits) / (trials + 1) is at most {SYSTEMATIC_P_NUM}/{SYSTEMATIC_P_DEN}. "
        "Recurrent pairs meet the count and miss that probability. Doubles and hapaxes are the scribal-noise bins. "
        "A double can have a small per-pair null hit count and still stay out of the merge table, because the count gate is 3. "
        f"Hapax pairs: {subs['hapax_pairs']}."
    )
    lines.append("")
    lines.append(
        "Classes are the connected components of systematic pairs. The representative is the member with the "
        "higher corpus count; ties take the smaller stem string. The merge table maps every member to that representative. "
        "It is a candidate allograph or homophone table for other tracks. It is not a decipherment, and a wide class "
        "(8 or more members) is a warning that transitivity may have chained distinct values."
    )
    lines.append("")
    above = [row for row in subs["pairs"] if row["kind"] == "systematic" and row["above_family_max"]]
    level = [row for row in subs["pairs"] if row["kind"] == "systematic" and not row["above_family_max"]]
    above_text = ", ".join(f"{row['a']}–{row['b']} ({row['count']})" for row in above) or "none"
    level_text = ", ".join(f"{row['a']}–{row['b']} ({row['count']})" for row in level) or "none"
    lines.append(
        f"Pairs whose count also exceeds the busiest null pair: {above_text}. "
        f"Pairs that clear the per-pair probability and do not exceed that busiest null count: {level_text}."
    )
    lines.append("")
    hand = subs["hand_pair_006_064"]
    lines.append(
        f"Hand pair 006/064: observed count {hand['observed_count']}, kind `{hand['kind']}`, "
        f"in a systematic class: {str(hand['in_systematic_class']).lower()}. {hand['citation']}"
    )
    lines.append("")
    if subs["classes"]:
        lines.append("| Class | Representative | Members | Pair count | Wide |")
        lines.append("| --- | --- | --- | ---: | --- |")
        for item in subs["classes"]:
            members = " ".join(item["members"])
            lines.append(
                f"| {item['id']} | {item['representative']} | {members} | {item['pair_count']} | {str(item['wide']).lower()} |"
            )
        lines.append("")
    else:
        lines.append("No systematic class cleared the null.")
        lines.append("")
    lines.append("| Signs | Count | Kind | Null (ge+1)/(trials+1) |")
    lines.append("| --- | ---: | --- | --- |")
    for row in subs["pairs"]:
        lines.append(
            f"| {row['a']} {row['b']} | {row['count']} | {row['kind']} | {_fraction(row['null_ge'], row['null_trials'])} |"
        )
    lines.append("")
    lines.append("### Merge table")
    lines.append("")
    if result["merge_table"]:
        lines.append("| From | To |")
        lines.append("| --- | --- |")
        for source, target in result["merge_table"].items():
            lines.append(f"| {source} | {target} |")
        lines.append("")
    else:
        lines.append("The merge table is empty.")
        lines.append("")
    lines.append("### Comparison with the Track A cited merges")
    lines.append("")
    lines.append(
        "Track A (`docs/decipherment/round2_trackA_variant_merge.md`, `decipherment/allographs.py`) "
        "applies published equivalences and reruns the syllabary test. This section places those rules "
        "next to the pairs above. The merge table stays the systematic classes from the alignments. "
        "A cited rule that misses the count or probability gate is left out of `merge_table`."
    )
    lines.append("")
    lines.append(
        f"{_pair_phrase(subs, '056', '084')}. Track A's `abstract_56_and_84` maps 084 to 056 "
        "(Guy 2006, citing Pozdniakov 1997, on the Pr1/Hr1 parallel; marked uncertain, one pair). "
        "The representative here is the more frequent stem, so the arrow in `merge_table` points at 084."
    )
    lines.append("")
    lines.append(
        f"{_pair_phrase(subs, '254', '256')}. That is one units-digit 4/6 pair inside codes 200–399, "
        "the range of Track A's uncertain `hand_digit_4_to_6` (Pozdniakov 1996: 296–297, as illustrated "
        f"by Guy 2006). {_pair_phrase(subs, '244', '246')}. {_pair_phrase(subs, '304', '306')}. "
        f"{_pair_phrase(subs, '045', '046')}. Series 000 is outside the range Track A rewrites."
    )
    lines.append("")
    lines.append(
        f"{_pair_phrase(subs, '400', '600')}. Track A's `gaping_mouth_to_bird` would rewrite every "
        "hundreds digit 3 or 4 as 6 (Pozdniakov 1996: 297). Track A marks that rewrite uncertain and "
        "keeps it out of the 2007 scheme, which still lists 380 and 400 as separate signs. The systematic "
        "edge here is this one pair."
    )
    lines.append("")
    lines.append(
        f"{_pair_phrase(subs, '006', '064')}. Track A's `hand_6_and_64` maps isolated 064 to 006 "
        "(Pozdniakov 1996: 296). The hand sentence above records the same absence; the pair is not added by hand."
    )
    lines.append("")
    lines.append(
        f"{_pair_phrase(subs, '048', '049')}. Track A's `horley_one_to_one` includes the suggested map "
        "049→048 (Horley 2005). The probability gate keeps it out of the merge table."
    )
    lines.append("")
    lines.append(
        f"{_pair_phrase(subs, '280', '290')}. Track A's `horley_expansions` writes 280 as the sequence "
        "070 002 when ligatures are split (Horley 2005). Class S07 is a substitution of two intact stems. "
        f"{_pair_phrase(subs, '381', '386')}. The same Horley note replaces 386 with 073 006 in one cited "
        "passage; this alignment keeps 386 as one stem."
    )
    lines.append("")
    lines.append(
        "Systematic pairs with no one-to-one rule in the Track A catalog: "
        f"{_pair_phrase(subs, '002', '021')}; {_pair_phrase(subs, '001', '011')}; "
        f"{_pair_phrase(subs, '008', '081')}; {_pair_phrase(subs, '381', '385')}."
    )
    lines.append("")
    lines.append("## Insertions and deletions")
    lines.append("")
    lines.append(
        "A gap with a neighbor on both sides is an optional sign relative to the other copy: the parallel "
        "continues without it. The pattern is the inserted sign plus those two neighbors. "
        f"The null shuffles inserted signs across the observed neighbor pairs ({INDEL_TRIALS} trials, seed {INDEL_SEED}). "
        f"The busiest pattern in any trial reached {indels['family_max_count']}. "
        f"Events: {indels['events']}. Hapax patterns: {indels['hapax_patterns']}. "
        "A pattern is systematic on the same count and probability gates as a substitution. "
        "That pattern is the distributional candidate for an optional particle, a determinative, or a boundary mark. "
        "This track does not choose among those functions."
    )
    lines.append("")
    if indels["patterns"]:
        lines.append("| Sign | Left | Right | Count | Kind | Null |")
        lines.append("| --- | --- | --- | ---: | --- | --- |")
        for row in indels["patterns"]:
            lines.append(
                f"| {row['sign']} | {row['left_neighbor']} | {row['right_neighbor']} | {row['count']} | {row['kind']} | {_fraction(row['null_ge'], row['null_trials'])} |"
            )
        lines.append("")
    else:
        lines.append("No indel pattern occurred twice.")
        lines.append("")
    lines.append("## Ligatures kept whole")
    lines.append("")
    lig_cmp = ligature["published_comparison"]
    lines.append(
        f"`ligature_atomic` uses the same gates and {ligature['gates']['null_trials']} shuffle trials. "
        f"Null maximum {ligature['null']['max_score']}. "
        f"Gated passages {ligature['candidate_passages']}, significant {ligature['significant_passages']}. "
        "Recovered published pairs: "
        + (", ".join(lig_cmp["published_recovered"]) if lig_cmp["published_recovered"] else "none")
        + ". Absent: "
        + (", ".join(lig_cmp["published_absent"]) if lig_cmp["published_absent"] else "none")
        + ". "
        f"Systematic ligature classes: {len(ligature['substitutions']['classes'])}"
        + (
            " ("
            + "; ".join(
                f"{item['id']} {' '.join(item['members'])}"
                for item in ligature["substitutions"]["classes"]
            )
            + ")"
            if ligature["substitutions"]["classes"]
            else ""
        )
        + ". Those classes are not the merge table. A ligature that stays in one cell cannot show a component substitution."
    )
    lines.append("")
    lines.append("## Sources")
    lines.append("")
    lines.append(
        "- Barthel, Thomas S. 1958. *Grundlagen zur Entzifferung der Osterinselschrift*. Hamburg: Cram, de Gruyter."
    )
    lines.append(
        "- Davletshin, Albert. 2017. “Allographs, Graphic Variants and Iconic Formulae in the Kohau Rongorongo Script of Rapa Nui (Easter Island).” *Journal of the Polynesian Society* 126."
    )
    lines.append(
        "- Guy, Jacques B. M. 2006. “General Properties of the Rongorongo Writing.” *Rapa Nui Journal* 20(1). Cited for the hand-digit examples and the 56/84 alternation, via Track A."
    )
    lines.append(
        "- Horley, Paul. 2005. *Rapa Nui Journal* 19(2): 107–116. The one-to-one suggestions and the 280 and 386 expansions, as encoded in Track A."
    )
    lines.append(
        "- Horley, Paul. 2007. “Structural Analysis of Rongorongo Inscriptions.” *Rapa Nui Journal* 21(1)."
    )
    lines.append(
        "- Kudrjavtsev, Boris. 1949. Cited by Davletshin 2017 for the St. Petersburg collation and a sign count on P and Q. The article title is not re-copied here."
    )
    lines.append(
        "- Pozdniakov, Konstantin. 1996. “Les bases du déchiffrement de l’écriture de l’île de Pâques.” *Journal de la Société des Océanistes* 103: 289–303."
    )
    lines.append(
        "- Manber, Udi, and Gene Myers. 1993. “Suffix Arrays: A New Method for On-Line String Searches.” *SIAM Journal on Computing* 22: 935–948. Sproat's index, not the index used here."
    )
    lines.append(
        "- Sankoff, David, and Joseph Kruskal, eds. 1983. *Time Warps, String Edits, and Macromolecules.* The edit-distance method Sproat cites."
    )
    lines.append(
        "- Smith, T. F., and M. S. Waterman. 1981. “Identification of Common Molecular Subsequences.” *Journal of Molecular Biology* 147: 195–197."
    )
    lines.append(
        "- Sproat, Richard. 2003. “Approximate String Matches in the rongorongo Corpus.” Archived at "
        "https://web.archive.org/web/20080517071219/http://compling.ai.uiuc.edu/rws/ror/ ."
    )
    lines.append("")
    lines.append("## What the classes are for")
    lines.append("")
    lines.append(
        "Other tracks can apply `merge_table` in `data/decipherment/substitution_classes.json` with "
        "`dict.get(sign, sign)`. Signs absent from the table stay themselves. The JSON also stores every "
        "systematic, recurrent, and double pair with counts and null hits, so a later track can refuse the "
        "transitive closure and use the edges alone."
    )
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    DOC_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(render_json(result), encoding="utf-8")
    DOC_PATH.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    write_outputs(run_track_c(MockProvider()))


if __name__ == "__main__":
    main()
