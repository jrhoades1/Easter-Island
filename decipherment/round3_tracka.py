"""Round 3, Track A: segment the Great Tradition into word-sized units.

Sign strings only. No phonetic values and no glosses. The provider is
MockProvider and is never asked for a completion.

Normalization uses the Track C systematic merge table. Segmentation is
rule cuts (group-final 076, the sign 095, pure 999 bars, and parallel
indel edges) plus two unsupervised searches trained on the whole corpus,
each with and without those cuts held open: a two-part minimum
description length search, and a greedy mode search for the Goldwater,
Griffiths, and Johnson (2009) unigram Dirichlet-process model. A short
Gibbs sweep starts from that mode and is reported as a stability check.
"""

from __future__ import annotations

import json
import math
import random
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import load_located_sides
from decipherment.inventories import encode_token
from decipherment.metrics import zipf_fit
from decipherment.rapanui import primary_thomson_sample, syllabify_word
from decipherment.track_c_parallels import JSON_PATH as SUBSTITUTION_JSON
from decipherment.track_c_parallels import load_side_texts

REPO_ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = REPO_ROOT / "docs" / "decipherment" / "round3_trackA_segmentation.md"
UNITS_PATH = REPO_ROOT / "data" / "decipherment" / "candidate_units.json"

GT_TABLETS = frozenset({"H", "P", "Q"})
SIGN_076 = "076"
SIGN_095 = "095"
SIGN_999 = "999"

# Fixed before any comparison with Thomson word lengths.
MAX_WORD_LENGTH = 12
DP_ALPHA = 20.0
P_STOP = 0.5
GIBBS_SWEEPS = 5
GIBBS_SEED = 0
NULL_TRIALS = 24
NULL_SEED = 0
AGREEMENT_NULL_TRIALS = 200
AGREEMENT_NULL_SEED = 1
MIN_UNIT_COUNT = 2
MIN_MERGE_COUNT = 2
MAX_CONTEXTS = 5
MAX_ROUNDS = 8000
MOVE_TOLERANCE = 1e-6

SEGMENTERS = ("rules", "mdl", "mdl_cued", "dp", "dp_cued")
PRIMARY_SEGMENTER = "mdl_cued"
UNSUPERVISED = ("mdl", "mdl_cued", "dp", "dp_cued")
CUED_SEGMENTERS = frozenset({"rules", "mdl_cued", "dp_cued", "gibbs_cued"})


@dataclass(frozen=True, slots=True)
class Stem:
    """One ligature-decomposed stem, with the group slot it sits in."""

    side: str
    tablet: str
    line: str
    line_number: int
    index: int
    offset: int
    raw: str
    normalized: str
    group_final: bool
    group_len: int

    @property
    def locus(self) -> tuple[str, int]:
        return (self.side, self.index)

    @property
    def pure_999(self) -> bool:
        return self.group_len == 1 and self.raw == SIGN_999


@dataclass(frozen=True, slots=True)
class Line:
    side: str
    tablet: str
    line: str
    stems: tuple[Stem, ...]


@dataclass(frozen=True, slots=True)
class Word:
    signs: tuple[str, ...]
    loci: tuple[tuple[str, int], ...]

    @property
    def length(self) -> int:
        return len(self.signs)


Utterances = list[list[Word]]


def load_merge_table(path: Path = SUBSTITUTION_JSON) -> dict[str, str]:
    """Track C systematic merge. Unknown signs stay themselves."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    table = payload["merge_table"]
    if not isinstance(table, dict) or not table:
        raise ValueError("substitution_classes.json has no merge_table")
    return {str(key): str(value) for key, value in table.items()}


def load_significant_passages(path: Path = SUBSTITUTION_JSON) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    passages = payload["stem"]["passages"]
    kept = [passage for passage in passages if passage.get("significant")]
    if any("columns" not in passage for passage in kept):
        raise ValueError("a significant passage is missing alignment columns")
    return kept


def assert_columns_match(lines: Sequence[Line], passages: Sequence[dict[str, Any]]) -> None:
    """Passage columns are indexes into the unnormalized stem sequence."""
    raw = {stem.locus: stem.raw for line in lines for stem in line.stems}
    for passage in passages:
        cursors = {
            "left": int(passage["left"]["start"]),
            "right": int(passage["right"]["start"]),
        }
        sides = {"left": passage["left"]["side"], "right": passage["right"]["side"]}
        for left, right in passage["columns"]:
            pair = {"left": left, "right": right}
            for host, sign in pair.items():
                if sign is None:
                    continue
                locus = (sides[host], cursors[host])
                if raw.get(locus) != sign:
                    raise RuntimeError(f"{passage['id']} {host} at {locus} is {raw.get(locus)}, not {sign}")
                cursors[host] += 1


def load_lines(merge_table: dict[str, str]) -> tuple[Line, ...]:
    """Stem lines whose concatenation matches Track C's stem encoding."""
    reference = {side.side: side.signs for side in load_side_texts("stem")}
    lines: list[Line] = []
    for raw in load_located_sides():
        absolute = 0
        flat: list[str] = []
        for number, tokens in raw.lines:
            stems: list[Stem] = []
            line_name = f"{raw.side}{number}"
            for token in tokens:
                encoded = encode_token(token, "stem")
                group_len = len(encoded)
                for pos, sign in enumerate(encoded):
                    stems.append(
                        Stem(
                            side=raw.side,
                            tablet=raw.side[0],
                            line=line_name,
                            line_number=number,
                            index=absolute,
                            offset=len(stems),
                            raw=sign,
                            normalized=merge_table.get(sign, sign),
                            group_final=pos == group_len - 1,
                            group_len=group_len,
                        )
                    )
                    flat.append(sign)
                    absolute += 1
            if stems:
                lines.append(
                    Line(
                        side=raw.side,
                        tablet=raw.side[0],
                        line=line_name,
                        stems=tuple(stems),
                    )
                )
        expected = reference.get(raw.side)
        if not flat:
            if expected:
                raise RuntimeError(f"stem index drift on {raw.side}")
            continue
        if tuple(flat) != expected:
            raise RuntimeError(f"stem index drift on {raw.side}")
    return tuple(lines)


def permute_line(line: Line, rng: random.Random) -> Line:
    """Shuffle signs inside one line. Group slots stay put."""
    order = list(range(len(line.stems)))
    rng.shuffle(order)
    moved: list[Stem] = []
    for slot, source_index in enumerate(order):
        dest = line.stems[slot]
        src = line.stems[source_index]
        moved.append(
            Stem(
                side=dest.side,
                tablet=dest.tablet,
                line=dest.line,
                line_number=dest.line_number,
                index=dest.index,
                offset=dest.offset,
                raw=src.raw,
                normalized=src.normalized,
                group_final=dest.group_final,
                group_len=dest.group_len,
            )
        )
    return Line(side=line.side, tablet=line.tablet, line=line.line, stems=tuple(moved))


def shuffle_lines(lines: Sequence[Line], seed: int) -> tuple[Line, ...]:
    rng = random.Random(seed)
    return tuple(permute_line(line, rng) for line in lines)


def indel_runs(passage: dict[str, Any]) -> list[dict[str, Any]]:
    """Internal insertion runs, the same neighbor gate as Track C.

    Each run is one contiguous gap on one copy, with a matched sign on
    both sides of the gap. ``events`` counts inserted signs.
    """
    columns = passage["columns"]
    left_cursor = int(passage["left"]["start"])
    right_cursor = int(passage["right"]["start"])
    left_at: list[int | None] = []
    right_at: list[int | None] = []
    for left, right in columns:
        left_at.append(None if left is None else left_cursor)
        right_at.append(None if right is None else right_cursor)
        if left is not None:
            left_cursor += 1
        if right is not None:
            right_cursor += 1
    if left_cursor != int(passage["left"]["end"]) or right_cursor != int(passage["right"]["end"]):
        raise RuntimeError(f"column span does not match locus of {passage['id']}")

    def previous(indexes: list[int | None], start: int) -> int | None:
        cursor = start - 1
        while cursor >= 0:
            if indexes[cursor] is not None:
                return indexes[cursor]
            cursor -= 1
        return None

    def following(indexes: list[int | None], start: int) -> int | None:
        cursor = start
        while cursor < len(indexes):
            if indexes[cursor] is not None:
                return indexes[cursor]
            cursor += 1
        return None

    runs: list[dict[str, Any]] = []
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
        host_at = left_at if host == "left" else right_at
        other_at = right_at if host == "left" else left_at
        if previous(host_at, index) is None or following(host_at, end) is None:
            index = end
            continue
        host_side = passage["left"]["side"] if host == "left" else passage["right"]["side"]
        other_side = passage["right"]["side"] if host == "left" else passage["left"]["side"]
        inserted = [host_at[cursor] for cursor in range(index, end)]
        runs.append(
            {
                "passage_id": passage["id"],
                "host_side": host_side,
                "other_side": other_side,
                "inserted": inserted,
                "host_before": previous(host_at, index),
                "other_before": previous(other_at, index),
                "events": len(inserted),
            }
        )
        index = end
    return runs


def indel_cut_set(passages: Sequence[dict[str, Any]]) -> tuple[set[tuple[str, int]], int]:
    """Boundary after each edge of an internal indel. Returns cuts and event count."""
    cuts: set[tuple[str, int]] = set()
    events = 0
    for passage in passages:
        for run in indel_runs(passage):
            events += int(run["events"])
            inserted: list[int] = run["inserted"]
            cuts.add((run["host_side"], run["host_before"]))
            cuts.add((run["host_side"], inserted[-1]))
            if run["other_before"] is not None:
                cuts.add((run["other_side"], run["other_before"]))
    return cuts, events


def sign_cuts(lines: Sequence[Line]) -> set[tuple[str, int]]:
    """076-final, both sides of 095, and both sides of a pure 999 bar."""
    cuts: set[tuple[str, int]] = set()
    for line in lines:
        for position, stem in enumerate(line.stems):
            if stem.group_final and stem.raw == SIGN_076:
                cuts.add(stem.locus)
            if stem.raw == SIGN_095 or stem.pure_999:
                cuts.add(stem.locus)
                if position > 0:
                    cuts.add(line.stems[position - 1].locus)
    return cuts


def utterances_unigram(lines: Sequence[Line]) -> Utterances:
    utterances: Utterances = []
    for line in lines:
        words = [
            Word((stem.normalized,), (stem.locus,))
            for stem in line.stems
        ]
        if words:
            utterances.append(words)
    return utterances


def utterances_cued(lines: Sequence[Line], cuts: set[tuple[str, int]]) -> Utterances:
    """One utterance per rule chunk. Pure 999 bars are dropped."""
    utterances: Utterances = []
    for line in lines:
        signs: list[str] = []
        loci: list[tuple[str, int]] = []

        def flush() -> None:
            if not signs:
                return
            if signs == [SIGN_999]:
                signs.clear()
                loci.clear()
                return
            utterances.append([Word(tuple(signs), tuple(loci))])
            signs.clear()
            loci.clear()

        for stem in line.stems:
            signs.append(stem.normalized)
            loci.append(stem.locus)
            if stem.locus in cuts:
                flush()
        flush()
    return utterances


def rule_words(lines: Sequence[Line], cuts: set[tuple[str, int]]) -> Utterances:
    """The rule segmentation is the cue chunks, including no further splits."""
    return utterances_cued(lines, cuts)


def explode_hapax_chunks(utterances: Utterances) -> Utterances:
    """Replace a one-off multi-sign chunk with its stems.

    A chunk that occurs once is not a repeated unit. Starting the cued
    search from those stems avoids peeling each long hapax one move at a
    time. A chunk that occurs twice or more is left whole, so the search
    can keep it or split it.
    """
    counts: Counter[tuple[str, ...]] = Counter(
        utterance[0].signs for utterance in utterances if len(utterance) == 1
    )
    exploded: Utterances = []
    for utterance in utterances:
        if len(utterance) == 1 and len(utterance[0].signs) > 1 and counts[utterance[0].signs] == 1:
            word = utterance[0]
            exploded.append(
                [Word((sign,), (word.loci[offset],)) for offset, sign in enumerate(word.signs)]
            )
        else:
            exploded.append(list(utterance))
    return exploded


def _positive(counts: Counter[tuple[str, ...]]) -> list[tuple[tuple[str, ...], int]]:
    return [(word, count) for word, count in counts.items() if count > 0]


def mdl_bits(counts: Counter[tuple[str, ...]], alphabet: int) -> float:
    """Two-part code: spell each type with an end marker, then index the tokens.

    The spelling alphabet has ``alphabet + 1`` symbols (the stems in use, plus
    an end-of-word marker). Token indexes use the empirical unigram.
    """
    total = sum(count for _word, count in _positive(counts))
    if total <= 0:
        return 0.0
    log_alphabet = math.log2(alphabet + 1)
    lexicon = 0.0
    sum_c_log_c = 0.0
    for word, count in _positive(counts):
        lexicon += (len(word) + 1) * log_alphabet
        sum_c_log_c += count * math.log2(count)
    return lexicon - sum_c_log_c + total * math.log2(total)


def _log_p0(length: int, log_unit: float) -> float:
    return length * log_unit


def dp_logprob(counts: Counter[tuple[str, ...]], alphabet: int, alpha: float) -> float:
    """Joint log probability of the word tokens under the unigram DP.

    Closed form of the predictive rule ``(n_w + α P0(w)) / (n + α)``.
    ``P0(w) = (P_STOP / alphabet) ** length(w)``, which sums to 1 over
    every non-empty word when ``P_STOP`` is 1/2.
    """
    total = 0
    log_prob = 0.0
    log_unit = math.log(P_STOP) - math.log(alphabet)
    for word, count in _positive(counts):
        total += count
        log_eps = math.log(alpha) + _log_p0(len(word), log_unit)
        if log_eps < -700.0:
            log_prob += log_eps + math.lgamma(count)
        else:
            epsilon = math.exp(log_eps)
            log_prob += math.lgamma(count + epsilon) - math.lgamma(epsilon)
    if total <= 0:
        return 0.0
    return log_prob - math.lgamma(alpha + total) + math.lgamma(alpha)


def _census(
    utterances: Utterances, max_length: int
) -> tuple[Counter[tuple[str, ...]], Counter[tuple[tuple[str, ...], tuple[str, ...]]], Counter[tuple[str, ...]]]:
    counts: Counter[tuple[str, ...]] = Counter()
    adjacent: Counter[tuple[tuple[str, ...], tuple[str, ...]]] = Counter()
    doubled: Counter[tuple[str, ...]] = Counter()
    for utterance in utterances:
        for word in utterance:
            counts[word.signs] += 1
        index = 0
        size = len(utterance)
        while index < size:
            end = index + 1
            while end < size and utterance[end].signs == utterance[index].signs:
                end += 1
            run = end - index
            current = utterance[index].signs
            if run >= 2 and 2 * len(current) <= max_length:
                doubled[current] += run // 2
            if index > 0:
                previous = utterance[index - 1].signs
                if previous != current and len(previous) + len(current) <= max_length:
                    adjacent[(previous, current)] += 1
            index = end
    return counts, adjacent, doubled


def _c_log_c(count: int) -> float:
    if count <= 0:
        return 0.0
    return count * math.log2(count)


def _mdl_delta(
    counts: Counter[tuple[str, ...]],
    total: int,
    changes: dict[tuple[str, ...], int],
    alphabet: int,
) -> tuple[float, int]:
    """Return (new_bits - old_bits, new_total) for an absolute count update."""
    log_alphabet = math.log2(alphabet + 1)
    old_mass = 0
    new_mass = 0
    data_delta = 0.0
    lexicon_delta = 0.0
    for word, new_count in changes.items():
        old_count = counts.get(word, 0)
        old_mass += old_count
        new_mass += new_count
        data_delta += -_c_log_c(new_count) + _c_log_c(old_count)
        old_on = old_count > 0
        new_on = new_count > 0
        if old_on != new_on:
            cost = (len(word) + 1) * log_alphabet
            lexicon_delta += cost if new_on else -cost
    new_total = total + (new_mass - old_mass)
    if total > 0:
        data_delta -= total * math.log2(total)
    if new_total > 0:
        data_delta += new_total * math.log2(new_total)
    return lexicon_delta + data_delta, new_total


def _dp_delta(
    counts: Counter[tuple[str, ...]],
    total: int,
    changes: dict[tuple[str, ...], int],
    alphabet: int,
    alpha: float,
    log_unit: float,
) -> float:
    """Return new_logprob - old_logprob."""

    def energy(word: tuple[str, ...], count: int) -> float:
        if count <= 0:
            return 0.0
        log_eps = math.log(alpha) + _log_p0(len(word), log_unit)
        if log_eps < -700.0:
            return log_eps + math.lgamma(count)
        epsilon = math.exp(log_eps)
        return math.lgamma(count + epsilon) - math.lgamma(epsilon)

    delta = 0.0
    old_mass = 0
    new_mass = 0
    for word, new_count in changes.items():
        old_count = counts.get(word, 0)
        old_mass += old_count
        new_mass += new_count
        delta += energy(word, new_count) - energy(word, old_count)
    new_total = total + (new_mass - old_mass)
    # Joint uses -lgamma(α + N) + lgamma(α). The lgamma(α) term cancels.
    if total > 0:
        delta += math.lgamma(alpha + total)
    if new_total > 0:
        delta -= math.lgamma(alpha + new_total)
    return delta


def _merge_changes(
    counts: Counter[tuple[str, ...]], left: tuple[str, ...], right: tuple[str, ...], times: int
) -> dict[tuple[str, ...], int]:
    fused = left + right
    affected = {left, right, fused}

    def updated(word: tuple[str, ...]) -> int:
        count = counts.get(word, 0)
        if left != right:
            if word == left:
                count -= times
            if word == right:
                count -= times
        elif word == left:
            count -= 2 * times
        if word == fused:
            count += times
        return count

    return {word: updated(word) for word in affected}


def _split_changes(
    counts: Counter[tuple[str, ...]], word: tuple[str, ...], cut: int
) -> dict[tuple[str, ...], int]:
    times = counts[word]
    left, right = word[:cut], word[cut:]
    affected = {word, left, right}

    def updated(key: tuple[str, ...]) -> int:
        count = 0 if key == word else counts.get(key, 0)
        if left == right:
            if key == left:
                count += 2 * times
        else:
            if key == left:
                count += times
            if key == right:
                count += times
        return count

    return {key: updated(key) for key in affected}


def _decompose_changes(
    counts: Counter[tuple[str, ...]], word: tuple[str, ...]
) -> dict[tuple[str, ...], int]:
    times = counts[word]
    pieces: Counter[tuple[str, ...]] = Counter((sign,) for sign in word)
    affected = set(pieces) | {word}

    def updated(key: tuple[str, ...]) -> int:
        count = 0 if key == word else counts.get(key, 0)
        count += pieces.get(key, 0) * times
        return count

    return {key: updated(key) for key in affected}


def _apply_counts(counts: Counter[tuple[str, ...]], changes: dict[tuple[str, ...], int]) -> None:
    for word, count in changes.items():
        if count <= 0:
            counts.pop(word, None)
        else:
            counts[word] = count


def _apply_merge(utterances: Utterances, left: tuple[str, ...], right: tuple[str, ...]) -> int:
    fused = left + right
    performed = 0
    for index, utterance in enumerate(utterances):
        output: list[Word] = []
        cursor = 0
        while cursor < len(utterance):
            if (
                cursor + 1 < len(utterance)
                and utterance[cursor].signs == left
                and utterance[cursor + 1].signs == right
            ):
                output.append(
                    Word(fused, utterance[cursor].loci + utterance[cursor + 1].loci)
                )
                performed += 1
                cursor += 2
            else:
                output.append(utterance[cursor])
                cursor += 1
        utterances[index] = output
    return performed


def _apply_split(utterances: Utterances, word: tuple[str, ...], cut: int) -> None:
    left, right = word[:cut], word[cut:]
    for index, utterance in enumerate(utterances):
        output: list[Word] = []
        for token in utterance:
            if token.signs == word:
                output.append(Word(left, token.loci[:cut]))
                output.append(Word(right, token.loci[cut:]))
            else:
                output.append(token)
        utterances[index] = output


def _apply_decompose(utterances: Utterances, word: tuple[str, ...]) -> None:
    for index, utterance in enumerate(utterances):
        output: list[Word] = []
        for token in utterance:
            if token.signs == word:
                for offset, sign in enumerate(token.signs):
                    output.append(Word((sign,), (token.loci[offset],)))
            else:
                output.append(token)
        utterances[index] = output


def _payload_signs(signs: tuple[str, ...]) -> str:
    return "+".join(signs)


def greedy_segment(
    utterances: Utterances,
    *,
    objective: str,
    alphabet: int,
    max_length: int = MAX_WORD_LENGTH,
    alpha: float = DP_ALPHA,
    verify: bool = False,
) -> dict[str, Any]:
    """Greedy merges, binary splits, and full decompositions until none help.

    ``objective`` is ``mdl`` (lower two-part codelength) or ``dp`` (higher
    unigram-DP joint probability). One move per round. Ties take the
    lexicographically smaller payload.
    """
    if objective not in {"mdl", "dp"}:
        raise ValueError(objective)
    working = [list(utterance) for utterance in utterances]
    counts, _adjacent, _doubled = _census(working, max_length)
    log_unit = math.log(P_STOP) - math.log(alphabet)
    if objective == "mdl":
        score = mdl_bits(counts, alphabet)
    else:
        score = dp_logprob(counts, alphabet, alpha)
    rounds = 0
    while rounds < MAX_ROUNDS:
        total = sum(counts.values())
        _counts, adjacent, doubled = _census(working, max_length)
        counts = _counts
        best_improvement = 0.0
        best_payload: str | None = None
        best_change: dict[tuple[str, ...], int] | None = None
        best_kind: tuple[Any, ...] | None = None

        def consider(
            improvement: float,
            payload: str,
            changes: dict[tuple[str, ...], int],
            kind: tuple[Any, ...],
        ) -> None:
            nonlocal best_improvement, best_payload, best_change, best_kind
            if improvement <= MOVE_TOLERANCE:
                return
            if best_payload is None or improvement > best_improvement + MOVE_TOLERANCE or (
                abs(improvement - best_improvement) <= MOVE_TOLERANCE and payload < best_payload
            ):
                best_improvement = improvement
                best_payload = payload
                best_change = changes
                best_kind = kind

        for (left, right), times in adjacent.items():
            if times < MIN_MERGE_COUNT:
                continue
            changes = _merge_changes(counts, left, right, times)
            payload = f"M|{_payload_signs(left)}|{_payload_signs(right)}"
            if objective == "mdl":
                delta, _new_total = _mdl_delta(counts, total, changes, alphabet)
                improvement = -delta
            else:
                improvement = _dp_delta(counts, total, changes, alphabet, alpha, log_unit)
            consider(improvement, payload, changes, ("M", left, right))
        for left, times in doubled.items():
            if times < MIN_MERGE_COUNT:
                continue
            changes = _merge_changes(counts, left, left, times)
            payload = f"M|{_payload_signs(left)}|{_payload_signs(left)}"
            if objective == "mdl":
                delta, _new_total = _mdl_delta(counts, total, changes, alphabet)
                improvement = -delta
            else:
                improvement = _dp_delta(counts, total, changes, alphabet, alpha, log_unit)
            consider(improvement, payload, changes, ("M", left, left))
        for word, count in list(counts.items()):
            if count <= 0 or len(word) < 2:
                continue
            for cut in range(1, len(word)):
                changes = _split_changes(counts, word, cut)
                payload = f"S|{_payload_signs(word)}|{cut}"
                if objective == "mdl":
                    delta, _new_total = _mdl_delta(counts, total, changes, alphabet)
                    improvement = -delta
                else:
                    improvement = _dp_delta(counts, total, changes, alphabet, alpha, log_unit)
                consider(improvement, payload, changes, ("S", word, cut))
            if len(word) > 2:
                changes = _decompose_changes(counts, word)
                payload = f"D|{_payload_signs(word)}"
                if objective == "mdl":
                    delta, _new_total = _mdl_delta(counts, total, changes, alphabet)
                    improvement = -delta
                else:
                    improvement = _dp_delta(counts, total, changes, alphabet, alpha, log_unit)
                consider(improvement, payload, changes, ("D", word))
        if best_kind is None or best_change is None:
            break
        kind = best_kind[0]
        if kind == "M":
            performed = _apply_merge(working, best_kind[1], best_kind[2])
            if performed <= 0:
                raise RuntimeError("merge candidate was not present")
        elif kind == "S":
            _apply_split(working, best_kind[1], best_kind[2])
        else:
            _apply_decompose(working, best_kind[1])
        _apply_counts(counts, best_change)
        if verify:
            rescanned, _again_adjacent, _again_doubled = _census(working, max_length)
            if dict(rescanned) != dict(counts):
                raise RuntimeError("segmentation counts drifted from the tokens")
        if objective == "mdl":
            updated = mdl_bits(counts, alphabet)
            if updated > score - 1e-4:
                raise RuntimeError("MDL move did not shorten the code")
        else:
            updated = dp_logprob(counts, alphabet, alpha)
            if updated < score + 1e-4:
                raise RuntimeError("DP move did not raise the joint probability")
        score = updated
        rounds += 1
    else:
        raise RuntimeError(f"segmentation did not converge within {MAX_ROUNDS} rounds")
    return {
        "utterances": working,
        "counts": counts,
        "rounds": rounds,
        "score": score,
        "objective": objective,
    }


def _log_pred(count: int, log_p0: float, total: int, alpha: float) -> float:
    """log (count + α P0) - log(total + α), with P0 passed as a log."""
    log_eps = math.log(alpha) + log_p0
    log_den = math.log(total + alpha)
    if count <= 0:
        return log_eps - log_den
    log_count = math.log(count)
    gap = log_eps - log_count
    if gap > 40.0:
        log_num = log_eps + math.log1p(math.exp(-gap))
    else:
        log_num = log_count + math.log1p(math.exp(gap))
    return log_num - log_den


def _sigmoid(log_odds: float) -> float:
    if log_odds >= 0:
        return 1.0 / (1.0 + math.exp(-log_odds))
    return math.exp(log_odds) / (1.0 + math.exp(log_odds))


def gibbs_refine(
    utterances: Utterances,
    *,
    alphabet: int,
    alpha: float = DP_ALPHA,
    sweeps: int = GIBBS_SWEEPS,
    seed: int = GIBBS_SEED,
    max_length: int = MAX_WORD_LENGTH,
) -> dict[str, Any]:
    """Site-wise Gibbs sampler for the unigram DP, started at ``utterances``.

    The returned segmentation is the end-of-sweep state with the highest
    joint log probability, including the initial state. Cue chunks are
    separate utterances, so a sweep cannot cross a cue.
    """
    rng = random.Random(seed)
    log_unit = math.log(P_STOP) - math.log(alphabet)
    sign_rows: list[list[str]] = []
    locus_rows: list[list[tuple[str, int]]] = []
    boundary_rows: list[list[bool]] = []
    for utterance in utterances:
        signs: list[str] = []
        loci: list[tuple[str, int]] = []
        boundaries: list[bool] = []
        for word in utterance:
            for offset, sign in enumerate(word.signs):
                signs.append(sign)
                loci.append(word.loci[offset])
                boundaries.append(offset == len(word.signs) - 1)
        if boundaries:
            boundaries.pop()
        sign_rows.append(signs)
        locus_rows.append(loci)
        boundary_rows.append(boundaries)

    counts: Counter[tuple[str, ...]] = Counter()
    for utterance in utterances:
        for word in utterance:
            counts[word.signs] += 1

    def words_of(row: int, boundaries: Sequence[bool]) -> list[tuple[str, ...]]:
        signs = sign_rows[row]
        output: list[tuple[str, ...]] = []
        start = 0
        for index, cut in enumerate(boundaries):
            if cut:
                output.append(tuple(signs[start : index + 1]))
                start = index + 1
        output.append(tuple(signs[start:]))
        return output

    def snapshot(boundaries: list[list[bool]]) -> float:
        snapshot_counts: Counter[tuple[str, ...]] = Counter()
        for row, cuts in enumerate(boundaries):
            for word in words_of(row, cuts):
                snapshot_counts[word] += 1
        return dp_logprob(snapshot_counts, alphabet, alpha)

    best_score = snapshot(boundary_rows)
    best_boundaries = [list(row) for row in boundary_rows]
    sites = [
        (row, index)
        for row, cuts in enumerate(boundary_rows)
        for index in range(len(cuts))
    ]
    for _sweep in range(sweeps):
        rng.shuffle(sites)
        for row, index in sites:
            cuts = boundary_rows[row]
            signs = sign_rows[row]
            left = index
            while left > 0 and not cuts[left - 1]:
                left -= 1
            right = index + 1
            while right < len(cuts) and not cuts[right]:
                right += 1
            # Span signs[left:right+1] is one word if the site is off,
            # or two words split after ``index`` if the site is on.
            span_end = right + 1
            if cuts[index]:
                left_word = tuple(signs[left : index + 1])
                right_word = tuple(signs[index + 1 : span_end])
                current = (left_word, right_word)
            else:
                current = (tuple(signs[left:span_end]),)
            for word in current:
                counts[word] -= 1
                if counts[word] <= 0:
                    del counts[word]
            total = sum(counts.values())
            left_word = tuple(signs[left : index + 1])
            right_word = tuple(signs[index + 1 : span_end])
            joined = tuple(signs[left:span_end])
            if len(joined) > max_length:
                chosen_split = True
            else:
                log_split = _log_pred(
                    counts.get(left_word, 0), _log_p0(len(left_word), log_unit), total, alpha
                )
                right_count = counts.get(right_word, 0) + (1 if left_word == right_word else 0)
                log_split += _log_pred(
                    right_count, _log_p0(len(right_word), log_unit), total + 1, alpha
                )
                log_join = _log_pred(
                    counts.get(joined, 0), _log_p0(len(joined), log_unit), total, alpha
                )
                chosen_split = rng.random() < _sigmoid(log_split - log_join)
            if chosen_split:
                counts[left_word] += 1
                counts[right_word] += 1
                cuts[index] = True
            else:
                counts[joined] += 1
                cuts[index] = False
        score = snapshot(boundary_rows)
        if score > best_score:
            best_score = score
            best_boundaries = [list(row) for row in boundary_rows]

    refined: Utterances = []
    flips = 0
    considered = 0
    for row, utterance in enumerate(utterances):
        initial = boundary_rows_initial(utterance)
        chosen = best_boundaries[row]
        for before, after in zip(initial, chosen):
            considered += 1
            flips += int(before != after)
        words: list[Word] = []
        signs = sign_rows[row]
        loci = locus_rows[row]
        start = 0
        extended = list(chosen) + [True]
        for index, cut in enumerate(extended):
            if cut:
                words.append(Word(tuple(signs[start : index + 1]), tuple(loci[start : index + 1])))
                start = index + 1
        refined.append(words)
    return {
        "utterances": refined,
        "score": best_score,
        "sites": considered,
        "flips": flips,
        "sweeps": sweeps,
        "seed": seed,
    }


def boundary_rows_initial(utterance: Sequence[Word]) -> list[bool]:
    boundaries: list[bool] = []
    for word in utterance:
        for offset in range(len(word.signs)):
            boundaries.append(offset == len(word.signs) - 1)
    if boundaries:
        boundaries.pop()
    return boundaries


def boundary_ends(utterances: Iterable[Sequence[Word]]) -> set[tuple[str, int]]:
    """Locus of the last sign of each word."""
    ends: set[tuple[str, int]] = set()
    for utterance in utterances:
        for word in utterance:
            if word.loci:
                ends.add(word.loci[-1])
    return ends


def delimiter_loci(lines: Sequence[Line]) -> set[tuple[str, int]]:
    return {stem.locus for line in lines for stem in line.stems if stem.pure_999}


def internal_sites(lines: Sequence[Line], tablets: frozenset[str] | None = None) -> list[tuple[str, int]]:
    sites: list[tuple[str, int]] = []
    for line in lines:
        if tablets is not None and line.tablet not in tablets:
            continue
        for stem, _nxt in zip(line.stems, line.stems[1:]):
            sites.append(stem.locus)
    return sites


def boundary_f1(
    left_cuts: set[tuple[str, int]],
    right_cuts: set[tuple[str, int]],
    sites: Sequence[tuple[str, int]],
) -> dict[str, float | int]:
    true_positive = 0
    left_positive = 0
    right_positive = 0
    for site in sites:
        in_left = site in left_cuts
        in_right = site in right_cuts
        left_positive += int(in_left)
        right_positive += int(in_right)
        true_positive += int(in_left and in_right)
    precision = true_positive / left_positive if left_positive else 0.0
    recall = true_positive / right_positive if right_positive else 0.0
    if precision + recall == 0:
        score = 0.0
    else:
        score = 2 * precision * recall / (precision + recall)
    return {
        "sites": len(sites),
        "true_positive": true_positive,
        "left_cuts": left_positive,
        "right_cuts": right_positive,
        "precision": precision,
        "recall": recall,
        "f1": score,
    }


def _stem_index(lines: Sequence[Line]) -> dict[tuple[str, int], Stem]:
    return {stem.locus: stem for line in lines for stem in line.stems}


def parallel_site_pairs(
    passages: Sequence[dict[str, Any]],
    stems: dict[tuple[str, int], Stem],
    *,
    passage_id: str | None = None,
) -> list[tuple[tuple[str, int], tuple[str, int]]]:
    """Adjacent match columns whose signs are neighbors on both copies."""
    pairs: list[tuple[tuple[str, int], tuple[str, int]]] = []
    seen: set[tuple[tuple[str, int], tuple[str, int]]] = set()
    for passage in passages:
        if passage_id is not None and passage["id"] != passage_id:
            continue
        tablets = {passage["left"]["tablet"], passage["right"]["tablet"]}
        if passage_id is None and not tablets <= GT_TABLETS:
            continue
        columns = passage["columns"]
        left_cursor = int(passage["left"]["start"])
        right_cursor = int(passage["right"]["start"])
        left_side = passage["left"]["side"]
        right_side = passage["right"]["side"]
        previous: tuple[tuple[str, int], tuple[str, int]] | None = None
        for left, right in columns:
            left_locus = None if left is None else (left_side, left_cursor)
            right_locus = None if right is None else (right_side, right_cursor)
            if left is not None:
                left_cursor += 1
            if right is not None:
                right_cursor += 1
            if left_locus is None or right_locus is None:
                previous = None
                continue
            if previous is not None:
                left_prev, right_prev = previous
                left_stem = stems[left_locus]
                right_stem = stems[right_locus]
                neighbors = (
                    left_locus[1] == left_prev[1] + 1
                    and right_locus[1] == right_prev[1] + 1
                    and stems[left_prev].line == left_stem.line
                    and stems[right_prev].line == right_stem.line
                )
                if neighbors:
                    pair = (left_prev, right_prev)
                    if pair not in seen:
                        seen.add(pair)
                        pairs.append(pair)
            previous = (left_locus, right_locus)
    return pairs


def parallel_f1(
    pairs: Sequence[tuple[tuple[str, int], tuple[str, int]]],
    cuts: set[tuple[str, int]],
) -> dict[str, float | int]:
    both = 0
    left_only = 0
    right_only = 0
    neither = 0
    for left, right in pairs:
        left_cut = left in cuts
        right_cut = right in cuts
        if left_cut and right_cut:
            both += 1
        elif left_cut:
            left_only += 1
        elif right_cut:
            right_only += 1
        else:
            neither += 1
    denominator = 2 * both + left_only + right_only
    score = (2 * both / denominator) if denominator else 0.0
    sites = len(pairs)
    return {
        "sites": sites,
        "both_cut": both,
        "left_only": left_only,
        "right_only": right_only,
        "neither": neither,
        "agreement": (both + neither) / sites if sites else 0.0,
        "f1": score,
    }


def parallel_f1_null(
    pairs: Sequence[tuple[tuple[str, int], tuple[str, int]]],
    cuts: set[tuple[str, int]],
    trials: int,
    seed: int,
) -> dict[str, float | int]:
    """Shuffle each copy's cuts across the paired sites, preserving counts."""
    observed = parallel_f1(pairs, cuts)
    if not pairs:
        return {**observed, "null_ge": 0, "null_mean_f1": 0.0, "trials": trials}
    left_flags = [left in cuts for left, _right in pairs]
    right_flags = [right in cuts for _left, right in pairs]
    left_total = sum(left_flags)
    right_total = sum(right_flags)
    rng = random.Random(seed)
    ge_count = 0
    total_f1 = 0.0
    indexes = list(range(len(pairs)))
    for _trial in range(trials):
        left_on = set(rng.sample(indexes, left_total)) if left_total else set()
        right_on = set(rng.sample(indexes, right_total)) if right_total else set()
        both = sum(1 for index in indexes if index in left_on and index in right_on)
        left_only = left_total - both
        right_only = right_total - both
        denominator = 2 * both + left_only + right_only
        score = (2 * both / denominator) if denominator else 0.0
        total_f1 += score
        if score + 1e-12 >= float(observed["f1"]):
            ge_count += 1
    return {
        **observed,
        "null_ge": ge_count,
        "null_mean_f1": total_f1 / trials,
        "trials": trials,
        "seed": seed,
    }


def _lengths_of(utterances: Iterable[Sequence[Word]], tablets: frozenset[str] | None) -> list[int]:
    lengths: list[int] = []
    for utterance in utterances:
        for word in utterance:
            if not word.loci:
                continue
            if tablets is not None and word.loci[0][0][0] not in tablets:
                continue
            lengths.append(word.length)
    return lengths


def _type_counts(
    utterances: Iterable[Sequence[Word]], tablets: frozenset[str] | None
) -> Counter[tuple[str, ...]]:
    counts: Counter[tuple[str, ...]] = Counter()
    for utterance in utterances:
        for word in utterance:
            if not word.loci:
                continue
            if tablets is not None and word.loci[0][0][0] not in tablets:
                continue
            counts[word.signs] += 1
    return counts


def repeated_multisign(counts: Counter[tuple[str, ...]]) -> int:
    return sum(1 for word, count in counts.items() if len(word) >= 2 and count >= 2)


def _median(values: Sequence[int]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2


def _histogram(values: Sequence[int], cap: int = MAX_WORD_LENGTH) -> dict[str, int]:
    bins = {str(length): 0 for length in range(1, cap + 1)}
    bins[f"{cap + 1}+"] = 0
    for value in values:
        if value <= 0:
            continue
        if value > cap:
            bins[f"{cap + 1}+"] += 1
        else:
            bins[str(value)] += 1
    return bins


def _mean(values: Sequence[int]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def total_variation(left: dict[str, int], right: dict[str, int]) -> float:
    left_total = sum(left.values())
    right_total = sum(right.values())
    if left_total == 0 or right_total == 0:
        return 0.0
    keys = set(left) | set(right)
    distance = 0.0
    for key in keys:
        distance += abs(left.get(key, 0) / left_total - right.get(key, 0) / right_total)
    return 0.5 * distance


def length_report(values: Sequence[int]) -> dict[str, Any]:
    histogram = _histogram(values)
    return {
        "tokens": len(values),
        "mean": _mean(values),
        "median": _median(values),
        "max": max(values) if values else 0,
        "at_cap": histogram.get(str(MAX_WORD_LENGTH), 0),
        "histogram": histogram,
    }


def frequency_report(counts: Counter[tuple[str, ...]]) -> dict[str, Any]:
    tokens = ["+".join(word) for word, count in counts.items() for _index in range(count)]
    fit = zipf_fit([tokens]) if tokens else {"slope": None, "r2": None, "ranks": 0}
    types = len(counts)
    hapaxes = sum(1 for count in counts.values() if count == 1)
    return {
        "types": types,
        "tokens": sum(counts.values()),
        "hapaxes": hapaxes,
        "repeated_types": sum(1 for count in counts.values() if count >= MIN_UNIT_COUNT),
        "repeated_multisign_types": repeated_multisign(counts),
        "zipf_slope": fit["slope"],
        "zipf_r2": fit["r2"],
    }


def thomson_reference() -> dict[str, Any]:
    """Word length in (C)V syllables, and word frequency, from Thomson 1891."""
    sample = primary_thomson_sample()
    lengths: list[int] = []
    words: list[str] = []
    for line in sample.word_lines:
        for word in line:
            syllables = syllabify_word(word, sample.orthography)
            if not syllables:
                continue
            lengths.append(len(syllables))
            words.append(word)
    counts = Counter(words)
    fit = zipf_fit([words])
    return {
        "sample": sample.name,
        "orthography": sample.orthography,
        "word_tokens": sample.word_count,
        "words_rejected": sample.words_rejected,
        "words": len(words),
        "syllables": sum(lengths),
        "types": len(counts),
        "length": length_report(lengths),
        "zipf_slope": fit["slope"],
        "zipf_r2": fit["r2"],
        "hapaxes": sum(1 for count in counts.values() if count == 1),
    }


def sign_roles(lines: Sequence[Line], utterances: Utterances) -> dict[str, dict[str, int]]:
    """Where group-final 076 and every 095 sit inside proposed units.

    ``singleton`` is a one-sign unit. ``suffix`` ends a longer unit.
    ``initial`` and ``medial`` are inside a unit. ``absent`` was dropped,
    which is how a pure 999 bar is treated and should not happen for these signs.
    """
    placed: dict[tuple[str, int], tuple[tuple[str, ...], int]] = {}
    for utterance in utterances:
        for word in utterance:
            for offset, locus in enumerate(word.loci):
                placed[locus] = (word.signs, offset)
    roles = {
        "group_final_076": Counter(),
        "sign_095": Counter(),
    }
    for line in lines:
        for stem in line.stems:
            if stem.group_final and stem.raw == SIGN_076:
                key = "group_final_076"
            elif stem.raw == SIGN_095:
                key = "sign_095"
            else:
                continue
            found = placed.get(stem.locus)
            if found is None:
                roles[key]["absent"] += 1
                continue
            signs, offset = found
            if len(signs) == 1:
                roles[key]["singleton"] += 1
            elif offset == len(signs) - 1:
                roles[key]["suffix"] += 1
            elif offset == 0:
                roles[key]["initial"] += 1
            else:
                roles[key]["medial"] += 1
    empty = {"singleton": 0, "suffix": 0, "initial": 0, "medial": 0, "absent": 0}
    return {
        name: {**empty, **dict(counts)}
        for name, counts in roles.items()
    }


def _round(value: Any, places: int = 6) -> Any:
    if isinstance(value, float):
        return round(value, places)
    return value


def _cue_recall(
    lines: Sequence[Line],
    ends: set[tuple[str, int]],
    predicate: Any,
) -> dict[str, int | float]:
    sites = [stem.locus for line in lines for stem in line.stems if predicate(stem)]
    recovered = sum(1 for site in sites if site in ends)
    return {
        "cues": len(sites),
        "recovered": recovered,
        "rate": (recovered / len(sites)) if sites else 0.0,
    }


def segmenter_cuts(
    name: str,
    utterances: Utterances,
    delimiters: set[tuple[str, int]],
) -> set[tuple[str, int]]:
    """Word-final loci. Cued segmenters also cut at a dropped 999 bar."""
    ends = boundary_ends(utterances)
    if name in CUED_SEGMENTERS:
        return ends | delimiters
    return ends


def segment_corpus(
    lines: Sequence[Line],
    cuts: set[tuple[str, int]],
    *,
    alphabet: int,
    with_gibbs: bool,
) -> dict[str, Any]:
    """Rules, MDL, and DP, each cued and uncued. Gibbs refines the DP modes."""
    rule_utterances = rule_words(lines, cuts)
    cued_seed = explode_hapax_chunks(utterances_cued(lines, cuts))
    mdl = greedy_segment(utterances_unigram(lines), objective="mdl", alphabet=alphabet)
    mdl_cued = greedy_segment(cued_seed, objective="mdl", alphabet=alphabet)
    dp = greedy_segment(utterances_unigram(lines), objective="dp", alphabet=alphabet)
    dp_cued = greedy_segment(cued_seed, objective="dp", alphabet=alphabet)
    gibbs = None
    gibbs_cued = None
    if with_gibbs:
        gibbs = gibbs_refine(dp["utterances"], alphabet=alphabet)
        gibbs_cued = gibbs_refine(dp_cued["utterances"], alphabet=alphabet, seed=GIBBS_SEED + 1)
    stored = {
        "rules": {"utterances": rule_utterances, "rounds": 0, "score": None, "objective": "rules"},
        "mdl": mdl,
        "mdl_cued": mdl_cued,
        "dp": dp,
        "dp_cued": dp_cued,
    }
    if gibbs is not None and gibbs_cued is not None:
        stored["gibbs"] = gibbs
        stored["gibbs_cued"] = gibbs_cued
    return stored


def _null_row(
    observed: float,
    samples: Sequence[float],
    *,
    higher_is_structure: bool,
) -> dict[str, Any]:
    if higher_is_structure:
        ge_count = sum(1 for sample in samples if sample + 1e-9 >= observed)
    else:
        ge_count = sum(1 for sample in samples if sample <= observed + 1e-9)
    return {
        "observed": observed,
        "null_mean": (sum(samples) / len(samples)) if samples else 0.0,
        "null_min": min(samples) if samples else 0.0,
        "null_max": max(samples) if samples else 0.0,
        "null_reached": ge_count,
        "trials": len(samples),
        "higher_is_structure": higher_is_structure,
    }


_NULL_LINES: tuple[Line, ...] | None = None
_NULL_ALPHABET = 0
_NULL_SEED = 0


def _null_init(lines: tuple[Line, ...], alphabet: int, seed: int) -> None:
    global _NULL_LINES, _NULL_ALPHABET, _NULL_SEED
    _NULL_LINES = lines
    _NULL_ALPHABET = alphabet
    _NULL_SEED = seed


def _null_worker(trial: int) -> dict[str, dict[str, float]]:
    """One within-line shuffle. Sign cues are recomputed; indel cues are not."""
    if _NULL_LINES is None:
        raise RuntimeError("null worker was not initialized")
    shuffled = shuffle_lines(_NULL_LINES, _NULL_SEED + trial)
    trained = segment_corpus(shuffled, sign_cuts(shuffled), alphabet=_NULL_ALPHABET, with_gibbs=False)
    sign_count = sum(len(line.stems) for line in shuffled)
    out: dict[str, dict[str, float]] = {}
    for name in UNSUPERVISED:
        counts = _type_counts(trained[name]["utterances"], None)
        score = float(trained[name]["score"])
        code = score / sign_count if name.startswith("mdl") else -score / sign_count
        out[name] = {
            "repeated": float(repeated_multisign(counts)),
            "mean_length": _mean(_lengths_of(trained[name]["utterances"], GT_TABLETS)),
            "code": code,
        }
    return out


def run_nulls(
    lines: Sequence[Line],
    alphabet: int,
    trials: int,
    seed: int,
) -> dict[str, Any]:
    """Retrain MDL and DP on within-line shuffles.

    Indel cuts stay empty: a shuffled line has no parallel passage. Sign
    cues (076-final, 095, pure 999) are recomputed from where those signs
    landed. Track C already found that a sign shuffle yields no significant
    passage, which is why this null does not rerun the aligner. Trials run
    in a process pool; each trial's seed is ``seed + trial``.
    """
    import multiprocessing as mp

    frozen = tuple(lines)
    workers = min(4, trials) if trials else 1
    if trials <= 1 or workers == 1:
        _null_init(frozen, alphabet, seed)
        rows = [_null_worker(trial) for trial in range(trials)]
    else:
        context = mp.get_context("fork")
        with context.Pool(
            processes=workers,
            initializer=_null_init,
            initargs=(frozen, alphabet, seed),
        ) as pool:
            rows = pool.map(_null_worker, range(trials))
    bucket: dict[str, dict[str, list[float]]] = {
        name: {"repeated": [], "mean_length": [], "code": []} for name in UNSUPERVISED
    }
    for row in rows:
        for name in UNSUPERVISED:
            bucket[name]["repeated"].append(row[name]["repeated"])
            bucket[name]["mean_length"].append(row[name]["mean_length"])
            bucket[name]["code"].append(row[name]["code"])
    return bucket


def _contexts(
    utterances: Utterances, target: tuple[str, ...], stems: dict[tuple[str, int], Stem]
) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    seen_sides: set[str] = set()
    for utterance in utterances:
        for index, word in enumerate(utterance):
            if word.signs != target or not word.loci:
                continue
            side = word.loci[0][0]
            if side[0] not in GT_TABLETS:
                continue
            if side in seen_sides and len(found) >= 2:
                continue
            previous = list(utterance[index - 1].signs) if index > 0 else None
            nxt = list(utterance[index + 1].signs) if index + 1 < len(utterance) else None
            locus = word.loci[0]
            stem = stems[locus]
            found.append(
                {
                    "side": side,
                    "line": stem.line,
                    "offset": stem.offset,
                    "locus": f"{stem.line}:{stem.offset}",
                    "previous": previous,
                    "next": nxt,
                }
            )
            seen_sides.add(side)
            if len(found) >= MAX_CONTEXTS:
                return found
    return found


def build_lexicon(
    stored: dict[str, Any],
    stems: dict[tuple[str, int], Stem],
) -> list[dict[str, Any]]:
    """Recurrent Great Tradition units under the primary segmenter. Unread."""
    per_segmenter = {
        name: _type_counts(payload["utterances"], GT_TABLETS) for name, payload in stored.items()
    }
    corpus_counts = _type_counts(stored[PRIMARY_SEGMENTER]["utterances"], None)
    primary = per_segmenter[PRIMARY_SEGMENTER]
    units: list[dict[str, Any]] = []
    for signs, count in primary.items():
        if count < MIN_UNIT_COUNT:
            continue
        also = [
            name
            for name, counts in per_segmenter.items()
            if name != PRIMARY_SEGMENTER and counts.get(signs, 0) >= MIN_UNIT_COUNT
        ]
        units.append(
            {
                "signs": list(signs),
                "length": len(signs),
                "count": count,
                "corpus_count": corpus_counts.get(signs, 0),
                "sides": sorted(
                    {
                        word.loci[0][0]
                        for utterance in stored[PRIMARY_SEGMENTER]["utterances"]
                        for word in utterance
                        if word.signs == signs
                        and word.loci
                        and word.loci[0][0][0] in GT_TABLETS
                    }
                ),
                "also_found_by": also,
                "ends_with_076": signs[-1] == SIGN_076,
                "is_095": signs == (SIGN_095,),
                "contexts": _contexts(stored[PRIMARY_SEGMENTER]["utterances"], signs, stems),
                "reading": None,
            }
        )
    units.sort(key=lambda item: (-int(item["count"]), int(item["length"]), item["signs"]))
    return units


def _gt_passage_count(passages: Sequence[dict[str, Any]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for passage in passages:
        tablets = tuple(sorted((passage["left"]["tablet"], passage["right"]["tablet"])))
        if set(tablets) <= GT_TABLETS:
            counts["–".join(tablets)] += 1
    return dict(sorted(counts.items()))


def _normalized_match_delta(
    passages: Sequence[dict[str, Any]], merge_table: dict[str, str], gt_only: bool
) -> dict[str, int]:
    raw_matches = 0
    normalized_matches = 0
    compared = 0
    for passage in passages:
        tablets = {passage["left"]["tablet"], passage["right"]["tablet"]}
        if gt_only and not tablets <= GT_TABLETS:
            continue
        for left, right in passage["columns"]:
            if left is None or right is None:
                continue
            compared += 1
            raw_matches += int(left == right)
            normalized_matches += int(
                merge_table.get(left, left) == merge_table.get(right, right)
            )
    return {
        "compared": compared,
        "raw_matches": raw_matches,
        "normalized_matches": normalized_matches,
        "mismatches_resolved": normalized_matches - raw_matches,
    }


def _segmenter_summary(
    name: str,
    payload: dict[str, Any],
    lines: Sequence[Line],
    reference_histogram: dict[str, int],
) -> dict[str, Any]:
    gt_lengths = _lengths_of(payload["utterances"], GT_TABLETS)
    corpus_lengths = _lengths_of(payload["utterances"], None)
    gt_counts = _type_counts(payload["utterances"], GT_TABLETS)
    corpus_counts = _type_counts(payload["utterances"], None)
    gt_length = length_report(gt_lengths)
    return {
        "name": name,
        "objective": payload.get("objective"),
        "rounds": payload.get("rounds"),
        "score": payload.get("score"),
        "gibbs_flips": payload.get("flips"),
        "gibbs_sites": payload.get("sites"),
        "great_tradition": {
            "length": gt_length,
            "frequency": frequency_report(gt_counts),
            "length_total_variation_vs_thomson_syllables": total_variation(
                gt_length["histogram"], reference_histogram
            ),
        },
        "corpus": {
            "length": length_report(corpus_lengths),
            "frequency": frequency_report(corpus_counts),
        },
    }


def _agreement_matrix(
    stored: dict[str, Any],
    sites: Sequence[tuple[str, int]],
    delimiters: set[tuple[str, int]],
) -> dict[str, dict[str, Any]]:
    ends = {
        name: segmenter_cuts(name, payload["utterances"], delimiters)
        for name, payload in stored.items()
    }
    matrix: dict[str, dict[str, Any]] = {}
    names = list(stored)
    for left in names:
        matrix[left] = {}
        for right in names:
            if left == right:
                continue
            matrix[left][right] = boundary_f1(ends[left], ends[right], sites)
    return matrix


def run_round3_tracka(provider: MockProvider | None = None) -> dict[str, Any]:
    """Segment the corpus and evaluate the Great Tradition. No readings."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Round 3 Track A accepts MockProvider only")
    merge_table = load_merge_table()
    passages = load_significant_passages()
    lines = load_lines(merge_table)
    assert_columns_match(lines, passages)
    indel_cuts, indel_events = indel_cut_set(passages)
    cuts = sign_cuts(lines) | indel_cuts
    alphabet = len({stem.normalized for line in lines for stem in line.stems})
    raw_alphabet = len({stem.raw for line in lines for stem in line.stems})
    stored = segment_corpus(lines, cuts, alphabet=alphabet, with_gibbs=True)
    stems = _stem_index(lines)
    thomson = thomson_reference()
    summaries = {
        name: _segmenter_summary(
            name, payload, lines, thomson["length"]["histogram"]
        )
        for name, payload in stored.items()
    }
    sites = internal_sites(lines, GT_TABLETS)
    delimiters = delimiter_loci(lines)
    matrix = _agreement_matrix(stored, sites, delimiters)
    pairs = parallel_site_pairs(passages, stems)
    p001_pairs = parallel_site_pairs(passages, stems, passage_id="P001")
    parallel: dict[str, Any] = {}
    for name, payload in stored.items():
        ends = segmenter_cuts(name, payload["utterances"], delimiters)
        parallel[name] = {
            "great_tradition": parallel_f1_null(
                pairs, ends, AGREEMENT_NULL_TRIALS, AGREEMENT_NULL_SEED
            ),
            "p001": parallel_f1(p001_pairs, ends),
        }
    nulls = run_nulls(lines, alphabet, NULL_TRIALS, NULL_SEED)
    null_report: dict[str, Any] = {}
    sign_total = sum(len(line.stems) for line in lines)
    for name in UNSUPERVISED:
        observed_repeated = float(summaries[name]["corpus"]["frequency"]["repeated_multisign_types"])
        observed_mean = float(summaries[name]["great_tradition"]["length"]["mean"])
        score = float(stored[name]["score"])
        if name.startswith("mdl"):
            observed_code = score / sign_total
            code_higher = False
        else:
            observed_code = -score / sign_total
            code_higher = False
        null_report[name] = {
            "repeated_multisign_types": _null_row(
                observed_repeated, nulls[name]["repeated"], higher_is_structure=True
            ),
            "great_tradition_mean_length": _null_row(
                observed_mean, nulls[name]["mean_length"], higher_is_structure=True
            ),
            "code_per_sign": _null_row(
                observed_code, nulls[name]["code"], higher_is_structure=code_higher
            ),
        }
    rewrites = Counter(
        stem.raw
        for line in lines
        for stem in line.stems
        if stem.raw != stem.normalized
    )
    lexicon = build_lexicon(stored, stems)
    gt_lines = [line for line in lines if line.tablet in GT_TABLETS]
    result = {
        "track": "round3_trackA",
        "version": 1,
        "provider": "MockProvider",
        "provider_calls": 0,
        "readings_assigned": False,
        "unread": True,
        "primary_segmenter": PRIMARY_SEGMENTER,
        "parameters": {
            "max_word_length": MAX_WORD_LENGTH,
            "dp_alpha": DP_ALPHA,
            "p_stop": P_STOP,
            "gibbs_sweeps": GIBBS_SWEEPS,
            "gibbs_seed": GIBBS_SEED,
            "null_trials": NULL_TRIALS,
            "null_seed": NULL_SEED,
            "agreement_null_trials": AGREEMENT_NULL_TRIALS,
            "agreement_null_seed": AGREEMENT_NULL_SEED,
            "min_unit_count": MIN_UNIT_COUNT,
            "min_merge_count": MIN_MERGE_COUNT,
            "encoding": "stem",
            "normalization": "track_c_merge_table",
        },
        "corpus": {
            "tokens": sign_total,
            "raw_inventory": raw_alphabet,
            "normalized_inventory": alphabet,
            "lines": len(lines),
            "rewrites": dict(sorted(rewrites.items())),
            "rewrite_tokens": sum(rewrites.values()),
        },
        "great_tradition": {
            "tablets": sorted(GT_TABLETS),
            "sides": sorted({line.side for line in gt_lines}),
            "tokens": sum(len(line.stems) for line in gt_lines),
            "lines": len(gt_lines),
        },
        "cues": {
            "indel_events": indel_events,
            "indel_cut_loci": len(indel_cuts),
            "sign_cut_loci": len(sign_cuts(lines)),
            "union_cut_loci": len(cuts),
            "group_final_076": sum(
                1
                for line in lines
                for stem in line.stems
                if stem.group_final and stem.raw == SIGN_076
            ),
            "sign_095": sum(1 for line in lines for stem in line.stems if stem.raw == SIGN_095),
            "pure_999": sum(1 for line in lines for stem in line.stems if stem.pure_999),
            "great_tradition_group_final_076": sum(
                1
                for line in gt_lines
                for stem in line.stems
                if stem.group_final and stem.raw == SIGN_076
            ),
            "great_tradition_095": sum(
                1 for line in gt_lines for stem in line.stems if stem.raw == SIGN_095
            ),
            "great_tradition_pure_999": sum(
                1 for line in gt_lines for stem in line.stems if stem.pure_999
            ),
        },
        "passages": {
            "significant": len(passages),
            "great_tradition_pairs": _gt_passage_count(passages),
            "normalization_all": _normalized_match_delta(passages, merge_table, False),
            "normalization_great_tradition": _normalized_match_delta(passages, merge_table, True),
            "p001": {
                "locus_left": "Hr2:36..Hr4:0",
                "locus_right": "Qr2:0..Qr3:65",
                "span": 125,
                "parallel_sites": len(p001_pairs),
            },
        },
        "thomson": thomson,
        "segmenters": summaries,
        "agreement": matrix,
        "parallel_agreement": parallel,
        "nulls": null_report,
        "cue_recovery": {
            name: {
                "group_final_076": _cue_recall(
                    lines,
                    segmenter_cuts(name, payload["utterances"], delimiters),
                    lambda stem: stem.group_final and stem.raw == SIGN_076,
                ),
                "sign_095_after": _cue_recall(
                    lines,
                    segmenter_cuts(name, payload["utterances"], delimiters),
                    lambda stem: stem.raw == SIGN_095,
                ),
                "roles": sign_roles(lines, payload["utterances"]),
            }
            for name, payload in stored.items()
        },
        "lexicon": {
            "segmenter": PRIMARY_SEGMENTER,
            "min_count": MIN_UNIT_COUNT,
            "scope": "great_tradition",
            "units": len(lexicon),
            "consensus_units": sum(1 for unit in lexicon if unit["also_found_by"]),
            "ends_with_076": sum(1 for unit in lexicon if unit["ends_with_076"]),
            "items": lexicon,
        },
    }
    return _sanitize(result)


def _sanitize(value: Any) -> Any:
    if isinstance(value, float):
        return round(value, 6)
    if isinstance(value, dict):
        return {str(key): _sanitize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return value


def render_json(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def _fmt(value: Any, places: int = 4) -> str:
    if isinstance(value, float):
        return f"{value:.{places}f}"
    return str(value)


def _histogram_row(histogram: dict[str, int]) -> str:
    keys = [str(length) for length in range(1, MAX_WORD_LENGTH + 1)] + [f"{MAX_WORD_LENGTH + 1}+"]
    return " | ".join(str(histogram.get(key, 0)) for key in keys)


def render_markdown(result: dict[str, Any]) -> str:
    """Prose report. Numbers come from ``result`` so the note cannot drift."""
    corpus = result["corpus"]
    gt = result["great_tradition"]
    cues = result["cues"]
    passages = result["passages"]
    thomson = result["thomson"]
    lexicon = result["lexicon"]
    lines: list[str] = []
    add = lines.append
    add("# Round 3, Track A — Segmenting the Great Tradition")
    add("")
    add(
        "This note cuts the Great Tradition (tablets H, P, and Q) into repeated "
        "sign-strings of roughly word length. It assigns no readings. A unit is a "
        "string of Barthel stems, nothing else. The provider is MockProvider and "
        "is never asked for a completion. Provider calls: "
        f"{result['provider_calls']}."
    )
    add("")
    add("## What is being segmented")
    add("")
    add(
        "The encoding is the Track C stem encoding: ligatures written with `.` or "
        "`:` are split, allograph letters and a leading orientation `V` are stripped, "
        "and illegible `000` is dropped. A Barthel group is one hyphen-separated "
        "Kohaumotu token. Lines stay lines. Tablets H, P, and Q are the Great "
        "Santiago tablet and the two St. Petersburg tablets, the three copies "
        "Track C aligned."
    )
    add("")
    add(
        f"Corpus: {corpus['tokens']} stems, {corpus['lines']} lines, "
        f"{corpus['raw_inventory']} stem types before normalization and "
        f"{corpus['normalized_inventory']} after it. "
        f"Great Tradition: {gt['tokens']} stems on {', '.join(gt['sides'])} "
        f"({gt['lines']} lines)."
    )
    add("")
    add("## Normalization")
    add("")
    add(
        "Each stem is rewritten by `merge_table` in "
        "`data/decipherment/substitution_classes.json`. The table is the eight "
        "systematic classes from Round 2 Track C. A sign that is not listed stays "
        "itself. The representative is the more frequent member of the class, so "
        "`400` becomes `600`, `011` becomes `001`, `021` becomes `002`, `056` "
        "becomes `084`, `081` becomes `008`, `256` becomes `254`, `290` becomes "
        "`280`, and `385` becomes `381`. This is an allograph-or-homophone "
        "candidate, not a decipherment. `076` and `095` are not in the table."
    )
    add("")
    add(
        f"Tokens rewritten: {corpus['rewrite_tokens']}. "
        + ", ".join(f"`{sign}` {count}" for sign, count in corpus["rewrites"].items())
        + "."
    )
    add("")
    norm = passages["normalization_great_tradition"]
    norm_all = passages["normalization_all"]
    add(
        "On matched columns of significant H/P/Q passages, raw identity is "
        f"{norm['raw_matches']}/{norm['compared']} and normalized identity is "
        f"{norm['normalized_matches']}/{norm['compared']}. The merge resolves "
        f"{norm['mismatches_resolved']} mismatches. Across every significant "
        f"passage the same count is {norm_all['mismatches_resolved']} "
        f"({norm_all['raw_matches']}/{norm_all['compared']} raw, "
        f"{norm_all['normalized_matches']}/{norm_all['compared']} normalized)."
    )
    add("")
    add("## Rule cuts")
    add("")
    add(
        "Four cuts are taken from earlier rounds. They are boundaries, not glosses."
    )
    add("")
    add(
        "- **Group-final `076`.** Round 2 Track B found that `076` ends its group "
        "corpus-wide, suffix-like, and refused a phonetic value. A cut is placed "
        "after a stem `076` that is the last stem of its Barthel group. A medial "
        "`076` is not a cut."
    )
    add(
        "- **`095`.** Round 2 Track C found `095` as a systematic insertion between "
        "`003` and `006`. Every `095` is its own segment: a cut before it and a "
        "cut after it. The note does not decide whether that sign is a particle, "
        "a determinative, or a boundary mark."
    )
    add(
        "- **Pure `999`.** On the Staff a group whose only stem is `999` is the "
        "vertical bar (Round 1 Track 3). Those bars are utterance breaks and are "
        "left out of the lexicon. The Great Tradition has "
        f"{cues['great_tradition_pure_999']} such bars."
    )
    add(
        "- **Parallel indels.** In a significant passage, a run of signs present "
        "on only one copy, with a matched neighbor on both sides, is an insertion. "
        "Cuts fall before and after that run, and between the two neighbors on "
        "the copy that lacks it. Track C counted these events; this track reuses "
        "the stored columns rather than searching again."
    )
    add("")
    add(
        f"Group-final `076`: {cues['group_final_076']} corpus-wide, "
        f"{cues['great_tradition_group_final_076']} on H/P/Q. "
        f"Sign `095`: {cues['sign_095']} corpus-wide, "
        f"{cues['great_tradition_095']} on H/P/Q. "
        f"Pure `999`: {cues['pure_999']}. "
        f"Indel events: {cues['indel_events']}, at {cues['indel_cut_loci']} loci. "
        f"Union of cue loci: {cues['union_cut_loci']}."
    )
    add("")
    add(
        "The rule segmenter emits exactly those chunks. On H/P/Q, `076` is rare, "
        "so a rule chunk can be many groups long. That is a result about the "
        "cues, not a claim that a whole line is one word. The unsupervised "
        "searches are allowed to cut inside a chunk. They are not allowed to "
        "join across a cue when the cued version is the one being trained."
    )
    add("")
    add("## Unsupervised segmentation")
    add("")
    add(
        "Both searches train on every line of every tablet, then the Great "
        "Tradition lines are read back out. The uncued search sees one utterance "
        "per inscribed line, each stem its own starting token. The cued search "
        "sees one utterance per rule chunk, and a pure `999` is not a token. "
        f"No word is created by a merge longer than {MAX_WORD_LENGTH} stems. "
        "The cap was set before the Thomson comparison. A rule chunk that occurs "
        "once is opened back into stems before the cued search starts. A chunk "
        "that occurs twice or more starts as one token, so the search can keep "
        "it or split it. The rule segmenter itself does not open those chunks."
    )
    add("")
    add(
        "**Minimum description length.** The code has two parts. Each lexicon "
        "type is spelled with the normalized stem alphabet plus an end marker, "
        "at `log2(V + 1)` bits per symbol. The corpus is then a sequence of "
        "pointers into that lexicon, at the empirical unigram cost. Search is "
        "greedy. Each round applies the single merge, the single binary split, "
        "or the single full decomposition into stems that shortens the code the "
        "most. A merge is offered only when that adjacent pair occurs at least "
        f"{MIN_MERGE_COUNT} times. One occurrence cannot become a repeated unit, "
        "and the code does not pay to spell it. Ties take the lexicographically "
        "smaller move. This is in the "
        "family of Brent (1999) and of Morfessor Baseline (Creutz and Lagus 2002), "
        "adapted to an unsegmented sign stream rather than to a list of already "
        "bounded words. It is not those programs."
    )
    add("")
    add(
        "**Unigram Dirichlet process.** The predictive probability of a word is "
        "`(n_w + α P0(w)) / (n + α)`, the Goldwater, Griffiths, and Johnson "
        f"(2009) unigram model, with α = {DP_ALPHA}. The base measure is "
        f"`P0(w) = ({P_STOP} / V) ^ length(w)`. With the stop probability at "
        "one half, that distribution sums to 1 over every non-empty word and "
        "expects short words (mean length 2). That bias is prior, not a fit to "
        "Rapanui. Search is greedy on the joint probability: the same three "
        "move types, with the same twice-or-more gate on merges, kept when they "
        "raise the joint. This is a mode search, not "
        "a draw from the posterior. A site-wise Gibbs sweep of "
        f"{GIBBS_SWEEPS} passes, seeds {GIBBS_SEED} and {GIBBS_SEED + 1}, then "
        "starts from each DP segmentation. The sweep cannot cross a cue, because "
        "cues are utterance breaks. The state kept is the end-of-sweep sample "
        "with the highest joint, or the start if no sweep beats it."
    )
    add("")
    add(
        "A site-wise sampler started from one stem per word almost never proposes "
        "a new multi-sign word when the inventory is several hundred stems: the "
        "base measure of an unseen bigram is tiny next to the count of a frequent "
        "stem. The greedy move looks at every repeated collocation at once, which "
        "is the search the inventory size allows. The Gibbs sweep is there to "
        "see whether that mode is locally stable."
    )
    add("")
    add("## Length, frequency, and the Thomson chants")
    add("")
    add(
        "The comparison text is the Thomson 1891 chant sample already used in "
        f"Track 2 (`{thomson['sample']}`, orthography `{thomson['orthography']}`), "
        "love song excluded. A word's length is its number of (C)V syllables. "
        f"The sample has {thomson['word_tokens']} word tokens and rejects "
        f"{thomson['words_rejected']}. Lengths use the {thomson['words']} words "
        f"that yield at least one syllable ({thomson['syllables']} syllables, "
        f"{thomson['types']} word types). Mean length {_fmt(thomson['length']['mean'])}, "
        f"median {_fmt(thomson['length']['median'])}, "
        f"Zipf slope {_fmt(thomson['zipf_slope'])}. "
        "Sign-segment length and syllable-word length are different units. A "
        "similar mean is not evidence that a stem is a syllable, and it is not "
        "a reading."
    )
    add("")
    header = " | ".join(str(length) for length in range(1, MAX_WORD_LENGTH + 1))
    add(f"| Source | Tokens | Types | Mean | Median | Zipf | TV vs Thomson | {header} | 13+ |")
    add("| --- | ---: | ---: | ---: | ---: | ---: | ---: | " + " ---: |" * (MAX_WORD_LENGTH + 1))
    add(
        f"| Thomson words | {thomson['words']} | {thomson['types']} | "
        f"{_fmt(thomson['length']['mean'])} | {_fmt(thomson['length']['median'])} | "
        f"{_fmt(thomson['zipf_slope'])} | 0 | {_histogram_row(thomson['length']['histogram'])} |"
    )
    for name in list(SEGMENTERS) + ["gibbs", "gibbs_cued"]:
        summary = result["segmenters"][name]
        block = summary["great_tradition"]
        add(
            f"| {name} on H/P/Q | {block['length']['tokens']} | {block['frequency']['types']} | "
            f"{_fmt(block['length']['mean'])} | {_fmt(block['length']['median'])} | "
            f"{_fmt(block['frequency']['zipf_slope'])} | "
            f"{_fmt(block['length_total_variation_vs_thomson_syllables'])} | "
            f"{_histogram_row(block['length']['histogram'])} |"
        )
    add("")
    add(
        "TV is the total-variation distance between the length histograms. "
        "Zipf is the OLS slope of log frequency on log rank."
    )
    add("")
    add("Corpus-wide, the same segmenters (this is the training text, not only H/P/Q):")
    add("")
    add("| Segmenter | Rounds | Tokens | Types | Repeated multi-sign types | Mean length |")
    add("| --- | ---: | ---: | ---: | ---: | ---: |")
    for name in list(SEGMENTERS) + ["gibbs", "gibbs_cued"]:
        summary = result["segmenters"][name]
        block = summary["corpus"]
        add(
            f"| {name} | {summary['rounds']} | {block['length']['tokens']} | "
            f"{block['frequency']['types']} | {block['frequency']['repeated_multisign_types']} | "
            f"{_fmt(block['length']['mean'])} |"
        )
    add("")
    add("## Agreement")
    add("")
    add(
        "Boundary F1 on Great Tradition line-internal sites. A site is the point "
        "between two successive stems of one line. The figure treats the row's "
        "cuts as the prediction and the column's cuts as the reference."
    )
    add("")
    names = list(SEGMENTERS) + ["gibbs", "gibbs_cued"]
    add("|  | " + " | ".join(names) + " |")
    add("| --- | " + " ---: |" * len(names))
    for left in names:
        cells = []
        for right in names:
            if left == right:
                cells.append("—")
            else:
                cells.append(_fmt(result["agreement"][left][right]["f1"]))
        add(f"| {left} | " + " | ".join(cells) + " |")
    add("")
    add(
        "Parallel agreement uses significant H–P, H–Q, and P–Q passages only "
        f"({sum(passages['great_tradition_pairs'].values())} passages: "
        + ", ".join(
            f"{label} {count}" for label, count in passages["great_tradition_pairs"].items()
        )
        + "). A site is a pair of adjacent matched columns, the two stems neighbors "
        "on both copies and inside one line on both copies. Overlapping passages "
        "contribute a site once. F1 counts a cut that falls on both copies. A "
        "segmenter that leaves almost every stem as its own unit cuts at nearly "
        "every site, so both copies agree by both cutting and F1 sits near 1. "
        "The null keeps each copy's number of cuts and shuffles their positions "
        f"({AGREEMENT_NULL_TRIALS} draws, seed {AGREEMENT_NULL_SEED}). "
        "`null_reached` is how many draws match or beat the observed F1. That "
        "comparison is the one a near-unigram segmentation does not get for free."
    )
    add("")
    add("| Segmenter | Sites | Both cut | F1 | Agreement | Null mean F1 | Null reached |")
    add("| --- | ---: | ---: | ---: | ---: | ---: | ---: |")
    for name in names:
        block = result["parallel_agreement"][name]["great_tradition"]
        add(
            f"| {name} | {block['sites']} | {block['both_cut']} | {_fmt(block['f1'])} | "
            f"{_fmt(block['agreement'])} | {_fmt(block['null_mean_f1'])} | {block['null_ge']} |"
        )
    add("")
    p001 = passages["p001"]
    add(
        f"P001 is the 125-sign H/Q passage ({p001['locus_left']} ‖ {p001['locus_right']}, "
        f"span {p001['span']}). Comparable sites inside it: {p001['parallel_sites']}."
    )
    add("")
    add("| Segmenter | Both cut | F1 | Agreement |")
    add("| --- | ---: | ---: | ---: |")
    for name in names:
        block = result["parallel_agreement"][name]["p001"]
        add(
            f"| {name} | {block['both_cut']} | {_fmt(block['f1'])} | {_fmt(block['agreement'])} |"
        )
    add("")
    add(
        "Cue recovery is the share of group-final `076` stems, and of `095` stems, "
        "that end a proposed unit. Ending a unit is automatic when nearly every "
        "stem is its own unit, so the next table splits those signs into a "
        "one-sign unit, the end of a longer unit, or a place inside a unit. "
        "The rule segmenter and every cued segmenter keep both signs at a cut "
        "by construction."
    )
    add("")
    add("| Segmenter | `076`-final recovered | `095` recovered | `076` alone | `076` suffix | `076` inside | `095` alone | `095` inside |")
    add("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for name in names:
        block = result["cue_recovery"][name]
        role_076 = block["roles"]["group_final_076"]
        role_095 = block["roles"]["sign_095"]
        inside_076 = role_076["initial"] + role_076["medial"]
        inside_095 = role_095["initial"] + role_095["medial"]
        add(
            f"| {name} | {block['group_final_076']['recovered']}/"
            f"{block['group_final_076']['cues']} | "
            f"{block['sign_095_after']['recovered']}/{block['sign_095_after']['cues']} | "
            f"{role_076['singleton']} | {role_076['suffix']} | {inside_076} | "
            f"{role_095['singleton']} | {inside_095} |"
        )
    add("")
    gibbs = result["segmenters"]["gibbs"]
    gibbs_cued = result["segmenters"]["gibbs_cued"]
    add(
        f"Gibbs changed {gibbs['gibbs_flips']} of {gibbs['gibbs_sites']} uncued "
        f"boundary sites relative to the DP mode, and {gibbs_cued['gibbs_flips']} of "
        f"{gibbs_cued['gibbs_sites']} cued sites. A flip is a site whose on/off "
        "state in the kept sample differs from the greedy DP segmentation."
    )
    add("")
    add("## Shuffled lines")
    add("")
    add(
        f"Each null trial permutes stems inside each line ({NULL_TRIALS} trials, "
        f"seed {NULL_SEED}) and retrains MDL and the DP search, with and without "
        "recomputed sign cues. Line lengths and the stem inventory of each line "
        "stay. Order does not. Indel cues are not recomputed: the shuffle breaks "
        "the parallels, and Track C's own sign-shuffle already produced no "
        "significant passage. `076`, `095`, and pure `999` are recomputed from "
        "the signs that landed in each group slot."
    )
    add("")
    add(
        "Two scores are the test. Repeated multi-sign types (length at least 2, "
        "count at least 2, corpus-wide) should be higher on the real text if the "
        "segmenter is finding repeated strings rather than inventory artifacts. "
        "Codelength per sign should be lower on the real text: bits per sign for "
        "MDL, nats per sign for the negative DP log probability. "
        "`null_reached` counts trials that tie or beat the real text. "
        "Mean length on H/P/Q is reported beside them and is not a gate."
    )
    add("")
    add("| Segmenter | Statistic | Observed | Null mean | Null min | Null max | Null reached |")
    add("| --- | --- | ---: | ---: | ---: | ---: | ---: |")
    for name in UNSUPERVISED:
        for statistic, label in (
            ("repeated_multisign_types", "Repeated multi-sign types"),
            ("code_per_sign", "Code per sign"),
            ("great_tradition_mean_length", "H/P/Q mean length"),
        ):
            block = result["nulls"][name][statistic]
            add(
                f"| {name} | {label} | {_fmt(block['observed'])} | {_fmt(block['null_mean'])} | "
                f"{_fmt(block['null_min'])} | {_fmt(block['null_max'])} | {block['null_reached']} |"
            )
    add("")
    add("## Candidate lexicon")
    add("")
    add(
        f"The lexicon is the Great Tradition inventory of `{PRIMARY_SEGMENTER}`: "
        f"units with count at least {MIN_UNIT_COUNT}. "
        f"{lexicon['units']} units, of which {lexicon['consensus_units']} also "
        f"occur at least twice under another segmenter, and {lexicon['ends_with_076']} "
        "end in `076`. `corpus_count` is the same string under the same segmenter "
        "on the whole corpus, Staff included. `also_found_by` lists the other "
        "segmenters. Contexts are up to five Great Tradition loci, with the "
        "previous and next unit. `reading` is null on every row."
    )
    add("")
    add(
        "The strings are unread. Ending in `076`, or being the single sign `095`, "
        "is a distributional flag carried over from the cue definitions. It is "
        "not a gloss, a particle reading, or a suffix reading."
    )
    add("")
    multi = [item for item in lexicon["items"] if item["length"] >= 2]
    over_cap = [item for item in multi if item["length"] > MAX_WORD_LENGTH]
    unigrams = [item for item in lexicon["items"] if item["length"] == 1]
    add(
        f"Of those, {len(multi)} contain two or more stems and {len(unigrams)} "
        "are single stems. The table is the twenty most frequent multi-sign units. "
        "The single-stem units with the highest H/P/Q counts are "
        + ", ".join(f"`{item['signs'][0]}` {item['count']}" for item in unigrams[:6])
        + "."
    )
    if over_cap:
        listed = ", ".join(
            f"`{'+'.join(item['signs'])}` (length {item['length']}, count {item['count']})"
            for item in sorted(over_cap, key=lambda item: (-item["length"], -item["count"]))
        )
        add("")
        add(
            f"{len(over_cap)} multi-sign units are longer than the merge cap of "
            f"{MAX_WORD_LENGTH}. The search cannot build a word that long by merging. "
            "These are repeated rule chunks it left unsplit: "
            + listed
            + "."
        )
    add("")
    add("| Signs | Length | H/P/Q count | Corpus count | Sides | Also found by |")
    add("| --- | ---: | ---: | ---: | --- | --- |")
    for item in multi[:20]:
        also = ", ".join(item["also_found_by"]) if item["also_found_by"] else "—"
        add(
            f"| `{'+'.join(item['signs'])}` | {item['length']} | {item['count']} | "
            f"{item['corpus_count']} | {', '.join(item['sides'])} | {also} |"
        )
    add("")
    add(
        f"The full list is `data/decipherment/candidate_units.json` "
        f"({lexicon['units']} units)."
    )
    add("")
    add("## What this does not claim")
    add("")
    add(
        "No stem is given a Rapanui syllable, a word, or a meaning. The primary "
        f"segmenter is `{PRIMARY_SEGMENTER}` because the task asked for the Round 1 "
        "and Round 2 cuts to be available to the search, not because its length "
        "histogram sits closer to Thomson than another row does. The DP base "
        "measure already prefers short units, so a mean near the Thomson mean "
        "would not be an independent confirmation. Shuffled-line scores are the "
        "check on whether repeated multi-sign units are an artifact of the "
        "unigram frequencies. Parallel F1 is the check on whether two copies of "
        "the same passage receive the same cuts. Neither check produces a translation."
    )
    add("")
    add("## Sources")
    add("")
    add(
        "- Brent, Michael R. 1999. “An Efficient, Probabilistically Sound Algorithm "
        "for Segmentation and Word Discovery.” *Machine Learning* 34."
    )
    add(
        "- Creutz, Mathias, and Krista Lagus. 2002. “Unsupervised Discovery of "
        "Morphemes.” In *Proceedings of the ACL Workshop on Morphological and "
        "Phonological Learning*."
    )
    add(
        "- Goldwater, Sharon, Thomas L. Griffiths, and Mark Johnson. 2009. "
        "“A Bayesian Framework for Word Segmentation: Exploring the Effects of "
        "Context.” *Cognition* 112."
    )
    add(
        "- The cue citations are the Round 1 and Round 2 notes in this directory: "
        "group-final `076` (Track B), `095` between `003` and `006` and the "
        "substitution classes (Track C), Staff `999` bars (Track 3), and the "
        "Thomson 1891 chant sample (Track 2)."
    )
    add("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    DOC_PATH.parent.mkdir(parents=True, exist_ok=True)
    UNITS_PATH.parent.mkdir(parents=True, exist_ok=True)
    UNITS_PATH.write_text(render_json(result), encoding="utf-8")
    DOC_PATH.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    result = run_round3_tracka(MockProvider())
    write_outputs(result)


if __name__ == "__main__":
    main()
