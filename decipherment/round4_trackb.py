"""Round 4, Track B: match sign units to Rapanui formulas by structure.

No phonetic value is assigned. A gloss is either quoted from a named
source or marked as a hypothesis. ``MockProvider`` is accepted and never
called.

The tests below were fixed before the Monte Carlo. Thresholds are not
fitted to the outcome.

Profile match. Each recurring sign-unit type and each Rapanui formula
type gets a vector of four order statistics: burstiness of within-line
gaps, rate at line start, rate at line end, and rate of abutting
repetition. The distance is the L1 gap between the two family means.
A within-line shuffle of the sign units, and a separate within-line
shuffle of the Rapanui words, are the nulls. A match requires the
observed distance to fall in the lower tail of both nulls, inside the
Bonferroni cut for the pre-registered pairs.

Zipf. The log-log slope of the formula spectrum is compared with the
sign-unit slope. The null rebuilds formulas after shuffling words inside
each line. A match also requires the absolute slope gap to sit inside
``ZIPF_SLOPE_TOLERANCE``. Word frequencies are unchanged by that shuffle,
so the word slope has no order-null and is reported as a description.

Creation chant. The repeated frame is the one Thomson printed for Ure
Vaeiko. Fischer 1995 proposed the same frame as the skeleton of several
tablets, including Mamari, and Guy 1998 rejected that reading. The sign
test looks for the same repeat-structure (two constant delimiters, or a
076 delimiter, tiling variable slots). It does not read a sign.

Genealogy. Gv6's ``200 X Y.076`` handoff is the published sign pattern.
The oral corpus and the Great Tradition are searched for a chain with
the same geometry: a constant opener and a slot that becomes the next
phrase's middle slot. Sound values are not used.
"""

from __future__ import annotations

import importlib.util
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable, Sequence

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import load_located_sides
from decipherment.old_rapanui import cv_syllables_mapped, primary_running_lines
from decipherment.round3_tracka import (
    GT_TABLETS,
    PRIMARY_SEGMENTER,
    UNITS_PATH,
    explode_hapax_chunks,
    greedy_segment,
    indel_cut_set,
    load_lines,
    load_merge_table,
    load_significant_passages,
    sign_cuts,
    utterances_cued,
)
from decipherment.round3_trackc import FORMULA_MIN_COUNT, _count_formulae, _cv_lines
from decipherment.track3_genealogy import (
    chain_links,
    extract_strict_phrases,
    group_stems,
    max_chain_run,
)
REPO_ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = REPO_ROOT / "data" / "decipherment" / "round4b_formula_match.json"
DOC_PATH = REPO_ROOT / "docs" / "decipherment" / "round4_trackB_formula_match.md"

_NATIVE_PATH = REPO_ROOT / "parsers" / "native_readings.py"
_NATIVE_SPEC = importlib.util.spec_from_file_location("rongorongo_native_readings", _NATIVE_PATH)
if _NATIVE_SPEC is None or _NATIVE_SPEC.loader is None:
    raise ImportError(f"cannot load {_NATIVE_PATH}")
_native = importlib.util.module_from_spec(_NATIVE_SPEC)
_NATIVE_SPEC.loader.exec_module(_native)
_FRAME = _native._FRAME
_PRODUCT = _native._PRODUCT
_WORD = _native._WORD
atua_matariri_verses = _native.atua_matariri_verses
load_barthel_lines = _native.load_barthel_lines
parse_atua_formula = _native.parse_atua_formula

# Pre-registered. Do not retune these after seeing a p-value.
FORMULA_WIDTH = 3
MIN_FAMILY = 8
MIN_PROFILE_FEATURES = 3
ZIPF_SLOPE_TOLERANCE = 0.15
ADOPT_FRACTION = 0.05
NULL_TRIALS = 400
SIGN_NULL_SEED = 0
LANGUAGE_NULL_SEED = 1
SKELETON_TRIALS = 400
SKELETON_SEED = 2
HANDOFF_TRIALS = 400
HANDOFF_SEED = 3
SKELETON_MIN_CYCLES = 4
SKELETON_TTR_MIN = 0.75
HANDOFF_MIN_LINKS = 3
CHILD_TTR_MIN = 0.75
BURSTINESS_MIN_GAPS = 2

PROFILE_FEATURES = ("burstiness", "p_initial", "p_final", "abutting_repeat")

PRIMARY_PAIRS: tuple[tuple[str, str], ...] = (
    ("all_recurring", "all_trigrams"),
    ("all_recurring", "words_min4"),
    ("monosign", "all_trigrams"),
    ("monosign", "words_min4"),
    ("multisign", "all_trigrams"),
    ("multisign", "words_min4"),
    ("gt_only", "all_trigrams"),
    ("also_outside", "all_trigrams"),
    ("all_recurring", "productive_frame"),
    ("all_recurring", "ko_initial"),
    ("multisign", "productive_frame"),
    ("multisign", "ko_initial"),
    ("all_recurring", "ki_te_initial"),
    ("multisign", "ki_te_initial"),
)

SKELETON_SIDES: tuple[str, ...] = (
    "Ca",
    "Cb",
    "Ra",
    "Rb",
    "Ia",
    "Gv",
    "Gr",
    "Hr",
    "Hv",
    "Pr",
    "Pv",
    "Qr",
    "Qv",
)
ELIDED_SIDES: tuple[str, ...] = ("Ca", "Cb", "Hr", "Hv", "Pr", "Pv", "Qr", "Qv")
GT_UNIT_TEXT = "GT-units"

# Printed and split spellings of the Thomson frame. Counted, not normalized
# into a reading. Fischer's published spelling is recorded beside them.
COPULA_SEQUENCES: tuple[tuple[str, ...], ...] = (
    ("ki", "ai", "kiroto"),
    ("kia", "ai", "kiroto"),
    ("ki", "ai", "ki", "roto"),
    ("ki", "ai", "ki", "roto", "ki"),
)
PRODUCT_SEQUENCES: tuple[tuple[str, ...], ...] = (
    ("ka", "pu", "te"),
    ("kapu", "te"),
    ("ka", "pu", "to"),
    ("kapu", "to"),
    ("mapu", "te"),
    ("ma", "pu", "te"),
)

SOURCES: tuple[dict[str, str], ...] = (
    {
        "id": "thomson_1891",
        "citation": "William J. Thomson, Te Pito te Henua, Report of the U.S. National Museum for 1889 (Washington, 1891), pp. 520–521.",
        "role": "Ure Vaeiko's Atua Matariri, the printed creation chant.",
    },
    {
        "id": "fischer_1995_jps",
        "citation": "Steven Roger Fischer, Preliminary Evidence for Cosmogonic Texts in Rapanui's Rongorongo Inscriptions, Journal of the Polynesian Society 104 (1995): 303–321.",
        "role": "Hypothesis: the Santiago Staff repeats the chant's procreation verse, with glyph 76 as the copula.",
    },
    {
        "id": "fischer_1995_rnj",
        "citation": "Steven Roger Fischer, Further Evidence for Cosmogonic Texts in the Rongorongo Inscriptions of Easter Island, Rapa Nui Journal 9(4) (December 1995).",
        "role": "Hypothesis: the oral frame is X ki 'ai ki roto ki 'a Y: ka pu te Z, and Mamari (his RR 2) is among the tablets said to carry the same kind of text, often without the phallic suffix.",
    },
    {
        "id": "guy_1998",
        "citation": "Jacques B. M. Guy, Anthropos 93 (1998): 552–555; Journal de la Société des Océanistes 107 (1998): 57–63.",
        "role": "Rejection of Fischer's cosmogonic reading. If the Gv genealogy is real, 076 is a patronymic mark.",
    },
    {
        "id": "barthel_1958_calendar",
        "citation": "Thomas S. Barthel, Grundlagen zur Entzifferung der Osterinselschrift (Hamburg, 1958), pp. 242–247.",
        "role": "Structural claim actually published for Mamari in the sources used here: Ca6–Ca9 is a lunar calendar. Not the creation chant. Already tested in Track 1.",
    },
    {
        "id": "barthel_metoro",
        "citation": "Barthel 1958 and Barthel 1963, Anthropos 58: 372–436, as cited by Fischer 1995 RNJ note 6; Kohaumotu rosetta/i.html.",
        "role": "Secondary statement that Barthel took Metoro's sign-words and read glyph 76 as a phallus. Hypothesis. This track does not apply those values.",
    },
    {
        "id": "butinov_1956",
        "citation": "N. A. Butinov and Y. V. Knorozov 1956, as reported by Davletshin 2012, Journal de la Société des Océanistes 134: 95–110; Guy 2003, Rapa Nui Journal 17(1); http://kohaumotu.org/rongorongo_org/rosetta/g.html.",
        "role": "Hypothesis: Gv6 is a genealogy, 200 a name introducer, 076 a patronymic. The handoff is what this track uses. The glosses are not applied.",
    },
    {
        "id": "round3_formulas",
        "citation": "Round 3 Track C, data and docs in this repository. 577 three-word formulas at count at least 4. The most frequent is ki te henua.",
        "role": "The formula inventory and the ki te frame. Structure only.",
    },
)


def _bonferroni(n_tests: int) -> float:
    if n_tests <= 0:
        raise ValueError("n_tests")
    return ADOPT_FRACTION / n_tests


def _round(value: Any, places: int = 6) -> Any:
    if isinstance(value, float):
        return round(value, places)
    if isinstance(value, dict):
        return {str(key): _round(item, places) for key, item in value.items()}
    if isinstance(value, list):
        return [_round(item, places) for item in value]
    if isinstance(value, tuple):
        return [_round(item, places) for item in value]
    return value


def _fraction(hits: int, trials: int) -> float | None:
    if trials <= 0:
        return None
    return hits / trials


def burstiness(gaps: Sequence[int]) -> float | None:
    """Goh and Barabási burstiness, population standard deviation.

    B = (sd - mean) / (sd + mean). Regular spacing is negative. At least
    two gaps are required. A zero denominator is undefined.
    """
    count = len(gaps)
    if count < BURSTINESS_MIN_GAPS:
        return None
    mean = sum(gaps) / count
    variance = sum((gap - mean) ** 2 for gap in gaps) / count
    deviation = math.sqrt(variance)
    denominator = deviation + mean
    if denominator == 0:
        return None
    return (deviation - mean) / denominator


def _occurrences(lines: Sequence[Sequence[str]], wanted: set[str] | None = None) -> dict[str, list[tuple[int, int, int]]]:
    """Map a type to (line index, start, line length) for every token."""
    found: dict[str, list[tuple[int, int, int]]] = defaultdict(list)
    for line_index, line in enumerate(lines):
        length = len(line)
        for start, token in enumerate(line):
            if wanted is not None and token not in wanted:
                continue
            found[token].append((line_index, start, length))
    return found


def _gram_occurrences(
    lines: Sequence[Sequence[str]],
    wanted: set[tuple[str, ...]],
    width: int,
) -> dict[tuple[str, ...], list[tuple[int, int, int]]]:
    found: dict[tuple[str, ...], list[tuple[int, int, int]]] = {gram: [] for gram in wanted}
    for line_index, line in enumerate(lines):
        length = len(line)
        if length < width:
            continue
        for start in range(length - width + 1):
            gram = tuple(line[start : start + width])
            bucket = found.get(gram)
            if bucket is not None:
                bucket.append((line_index, start, length))
    return found


def _profile(
    types: Sequence[Any],
    occurrences: dict[Any, list[tuple[int, int, int]]],
    width: int,
) -> dict[str, Any]:
    """Type-mean profile. Burstiness uses within-line start gaps only."""
    buckets: dict[str, list[float]] = {name: [] for name in PROFILE_FEATURES}
    for item in types:
        hits = occurrences.get(item, [])
        if not hits:
            continue
        total = len(hits)
        buckets["p_initial"].append(sum(1 for _line, start, _length in hits if start == 0) / total)
        buckets["p_final"].append(
            sum(1 for _line, start, length in hits if start + width == length) / total
        )
        places = {(line, start) for line, start, _length in hits}
        abutting = sum(1 for line, start, _length in hits if (line, start + width) in places)
        buckets["abutting_repeat"].append(abutting / total)
        by_line: dict[int, list[int]] = defaultdict(list)
        for line, start, _length in hits:
            by_line[line].append(start)
        gaps: list[int] = []
        for starts in by_line.values():
            starts.sort()
            gaps.extend(right - left for left, right in zip(starts, starts[1:]))
        score = burstiness(gaps)
        if score is not None:
            buckets["burstiness"].append(score)
    means: dict[str, float | None] = {}
    support: dict[str, int] = {}
    for name, values in buckets.items():
        support[name] = len(values)
        means[name] = (sum(values) / len(values)) if values else None
    if support["burstiness"] < MIN_FAMILY:
        means["burstiness"] = None
    return {"means": means, "support": support, "types": len(types)}


def profile_l1(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any] | None:
    """L1 of the family means. A feature drops out when either side lacks it."""
    if left["support"]["p_initial"] < MIN_FAMILY or right["support"]["p_initial"] < MIN_FAMILY:
        return None
    used: list[str] = []
    distance = 0.0
    for feature in PROFILE_FEATURES:
        first = left["means"][feature]
        second = right["means"][feature]
        if first is None or second is None:
            continue
        used.append(feature)
        distance += abs(first - second)
    if len(used) < MIN_PROFILE_FEATURES:
        return None
    return {"distance": distance, "features": used}


def trigram_counts(lines: Sequence[Sequence[str]]) -> Counter[tuple[str, ...]]:
    counts: Counter[tuple[str, ...]] = Counter()
    for line in lines:
        if len(line) < FORMULA_WIDTH:
            continue
        for start in range(len(line) - FORMULA_WIDTH + 1):
            counts[tuple(line[start : start + FORMULA_WIDTH])] += 1
    return counts


def _followers(lines: Sequence[Sequence[str]]) -> dict[tuple[str, str], set[str]]:
    """Words that follow each adjacent pair. One pair can head many formulas."""
    found: dict[tuple[str, str], set[str]] = defaultdict(set)
    for line in lines:
        for start in range(len(line) - 2):
            found[(line[start], line[start + 1])].add(line[start + 2])
    return found


def formula_families(
    lines: Sequence[Sequence[str]],
) -> tuple[dict[str, set[tuple[str, ...]]], Counter[tuple[str, ...]]]:
    """Structural classes. Membership uses the mapped word string only.

    ``productive_frame`` is not every repeated trigram. A trigram that
    occurs four times already drags its opening pair over that floor, so
    that rule would copy ``all_trigrams``. A frame here is an opening pair
    with at least four different third words.
    """
    trigrams = trigram_counts(lines)
    followers = _followers(lines)
    kept = {gram for gram, count in trigrams.items() if count >= FORMULA_MIN_COUNT}
    families = {
        "all_trigrams": kept,
        "productive_frame": {
            gram for gram in kept if len(followers[(gram[0], gram[1])]) >= SKELETON_MIN_CYCLES
        },
        "ko_initial": {gram for gram in kept if gram[0] == "ko"},
        "ki_te_initial": {gram for gram in kept if gram[0] == "ki" and gram[1] == "te"},
    }
    return families, trigrams


def productive_frame_count(lines: Sequence[Sequence[str]]) -> int:
    """Bigrams at the formula floor with at least four distinct followers."""
    pairs: Counter[tuple[str, str]] = Counter()
    followers: dict[tuple[str, str], set[str]] = defaultdict(set)
    for line in lines:
        for start in range(len(line) - 1):
            pair = (line[start], line[start + 1])
            pairs[pair] += 1
            if start + 2 < len(line):
                followers[pair].add(line[start + 2])
    return sum(
        1
        for pair, count in pairs.items()
        if count >= FORMULA_MIN_COUNT and len(followers[pair]) >= SKELETON_MIN_CYCLES
    )


def _rate(numerator: int, denominator: int) -> float | None:
    if denominator <= 0:
        return None
    return numerator / denominator


def zipf_slope(counts: Counter[Any], minimum: int) -> float | None:
    """OLS of log frequency on log rank. Ties break on the string form."""
    ranked = sorted(
        ((str(item), count) for item, count in counts.items() if count >= minimum),
        key=lambda item: (-item[1], item[0]),
    )
    if len(ranked) < 2:
        return None
    xs = [math.log(rank) for rank in range(1, len(ranked) + 1)]
    ys = [math.log(count) for _item, count in ranked]
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    variance = sum((value - mean_x) ** 2 for value in xs)
    if variance == 0:
        return None
    covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    return covariance / variance


def _shuffle_lines(lines: Sequence[Sequence[str]], rng: random.Random) -> list[list[str]]:
    shuffled: list[list[str]] = []
    for line in lines:
        row = list(line)
        rng.shuffle(row)
        shuffled.append(row)
    return shuffled


def _language_bundle(lines: Sequence[Sequence[str]]) -> dict[str, Any]:
    families, trigrams = formula_families(lines)
    formula_occ = _gram_occurrences(lines, families["all_trigrams"], FORMULA_WIDTH)
    profiles = {
        name: _profile(sorted(members), formula_occ, FORMULA_WIDTH) for name, members in families.items()
    }
    word_counts: Counter[str] = Counter(token for line in lines for token in line)
    word_types = sorted(token for token, count in word_counts.items() if count >= FORMULA_MIN_COUNT)
    word_occ = _occurrences(lines, set(word_types))
    profiles["words_min4"] = _profile(word_types, word_occ, 1)
    bigram_tokens = sum(max(0, len(line) - 1) for line in lines)
    frames = productive_frame_count(lines)
    return {
        "families": {name: len(members) for name, members in families.items()},
        "family_sets": families,
        "profiles": profiles,
        "trigrams": trigrams,
        "zipf_formulas": zipf_slope(trigrams, FORMULA_MIN_COUNT),
        "zipf_words": zipf_slope(word_counts, FORMULA_MIN_COUNT),
        "zipf_words_all": zipf_slope(word_counts, 1),
        "frames": frames,
        "frame_rate": _rate(frames, bigram_tokens),
        "bigram_tokens": bigram_tokens,
        "word_types_min4": len(word_types),
    }


def _sign_bundle(lines: Sequence[Sequence[str]], families: dict[str, list[str]]) -> dict[str, Any]:
    wanted: set[str] = set()
    for members in families.values():
        wanted.update(members)
    occurrences = _occurrences(lines, wanted)
    profiles = {name: _profile(members, occurrences, 1) for name, members in families.items()}
    counts: Counter[str] = Counter(
        token for line in lines for token in line if token in families["all_recurring"]
    )
    bigram_tokens = sum(max(0, len(line) - 1) for line in lines)
    frames = productive_frame_count(lines)
    return {
        "profiles": profiles,
        "zipf": zipf_slope(counts, 2),
        "zipf_floor4": zipf_slope(counts, FORMULA_MIN_COUNT),
        "frames": frames,
        "frame_rate": _rate(frames, bigram_tokens),
        "bigram_tokens": bigram_tokens,
    }


def longest_handoff(line: Sequence[str], ttr_min: float = CHILD_TTR_MIN) -> int:
    """Longest father-to-child chain whose child slot stays diverse.

    A phrase is three tokens. The opener is constant. The third token of
    one phrase is the second token of the next. Children equal to the
    opener are rejected. A chain counts only while its child type/token
    ratio stays at or above ``ttr_min``.
    """
    best = 0
    length = len(line)
    for start in range(length - 2):
        opener = line[start]
        children: list[str] = []
        previous: str | None = None
        index = start
        while index + 2 < length and line[index] == opener:
            child = line[index + 1]
            father = line[index + 2]
            if child == opener or father == opener:
                break
            if children and previous != child:
                break
            children.append(child)
            previous = father
            index += 3
            links = len(children) - 1
            if links > 0 and (len(set(children)) / len(children)) >= ttr_min:
                best = max(best, links)
    return best


def best_handoff_example(lines: Sequence[Sequence[str]], ttr_min: float = CHILD_TTR_MIN) -> dict[str, Any] | None:
    """One maximal chain, for the report. Words stay corpus words."""
    best: dict[str, Any] | None = None
    for line_index, line in enumerate(lines):
        length = len(line)
        for start in range(max(0, length - 2)):
            opener = line[start]
            children: list[str] = []
            fathers: list[str] = []
            previous: str | None = None
            index = start
            while index + 2 < length and line[index] == opener:
                child = line[index + 1]
                father = line[index + 2]
                if child == opener or father == opener:
                    break
                if children and previous != child:
                    break
                children.append(child)
                fathers.append(father)
                previous = father
                index += 3
                links = len(children) - 1
                diverse = links > 0 and (len(set(children)) / len(children)) >= ttr_min
                if not diverse:
                    continue
                if best is None or links > int(best["links"]):
                    best = {
                        "line_index": line_index,
                        "start": start,
                        "opener": opener,
                        "links": links,
                        "children": children[:8],
                        "fathers": fathers[:8],
                    }
    return best


def corpus_longest_handoff(lines: Sequence[Sequence[str]]) -> int:
    if not lines:
        return 0
    return max(longest_handoff(line) for line in lines)


def top_two(line: Sequence[str], minimum: int) -> tuple[str, str] | None:
    """The two most frequent tokens, ties broken by the token string."""
    counts = Counter(line)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    if len(ranked) < 2:
        return None
    if ranked[0][1] < minimum or ranked[1][1] < minimum:
        return None
    return ranked[0][0], ranked[1][0]


def best_tile_run(line: Sequence[str], first: str, second: str) -> list[tuple[tuple[str, ...], tuple[str, ...]]]:
    """Longest contiguous D1-slot-D2-slot run. Slots are non-empty and avoid both delimiters."""
    best: list[tuple[tuple[str, ...], tuple[str, ...]]] = []
    index = 0
    length = len(line)
    blocked = {first, second}
    while index < length:
        if line[index] != first:
            index += 1
            continue
        run: list[tuple[tuple[str, ...], tuple[str, ...]]] = []
        cursor = index
        while cursor < length and line[cursor] == first:
            slot1_end = cursor + 1
            while slot1_end < length and line[slot1_end] not in blocked:
                slot1_end += 1
            if slot1_end == cursor + 1 or slot1_end >= length or line[slot1_end] != second:
                break
            slot2_end = slot1_end + 1
            while slot2_end < length and line[slot2_end] not in blocked:
                slot2_end += 1
            if slot2_end == slot1_end + 1:
                break
            if slot2_end < length and line[slot2_end] != first:
                break
            run.append((tuple(line[cursor + 1 : slot1_end]), tuple(line[slot1_end + 1 : slot2_end])))
            cursor = slot2_end
        if len(run) > len(best):
            best = run
        index = max(cursor, index + 1)
    return best


def line_has_chant_tile(line: Sequence[str]) -> bool:
    """Two constant delimiters, at least four cycles, both slots diverse."""
    pair = top_two(line, SKELETON_MIN_CYCLES)
    if pair is None:
        return False
    run = best_tile_run(line, pair[0], pair[1])
    if len(run) < SKELETON_MIN_CYCLES:
        return False
    slot_a = len({left for left, _right in run}) / len(run)
    slot_b = len({right for _left, right in run}) / len(run)
    return slot_a >= SKELETON_TTR_MIN and slot_b >= SKELETON_TTR_MIN


def tile_line_count(lines: Sequence[Sequence[str]]) -> int:
    return sum(1 for line in lines if line_has_chant_tile(line))


def delimiter_gaps(line: Sequence[str], predicate: Callable[[str], bool]) -> list[int]:
    indexes = [index for index, token in enumerate(line) if predicate(token)]
    return [right - left - 1 for left, right in zip(indexes, indexes[1:])]


def gap_histogram(lines: Sequence[Sequence[str]], predicate: Callable[[str], bool]) -> Counter[int]:
    histogram: Counter[int] = Counter()
    for line in lines:
        histogram.update(delimiter_gaps(line, predicate))
    return histogram


def histogram_l1(observed: Counter[int], reference: Counter[int]) -> float | None:
    """L1 distance between two count histograms, after each is made to sum to 1."""
    left_total = sum(observed.values())
    right_total = sum(reference.values())
    if left_total <= 0 or right_total <= 0:
        return None
    keys = set(observed) | set(reference)
    return sum(
        abs((observed.get(key, 0) / left_total) - (reference.get(key, 0) / right_total)) for key in keys
    )


def slot_constancy(lines: Sequence[Sequence[str]]) -> float:
    """Highest modal rate in any slot of a non-overlapping triple cut.

    Three residues are tried. The elided XYZ claim predicts variable slots,
    which a shuffle also produces. A high value is a repeated slot-sign,
    not confirmation of an unwritten frame.
    """
    best = 0.0
    for offset in (0, 1, 2):
        slots: list[list[str]] = [[], [], []]
        for line in lines:
            usable = list(line[offset:])
            width = len(usable) // 3
            for index in range(width):
                triple = usable[index * 3 : index * 3 + 3]
                for slot, token in enumerate(triple):
                    slots[slot].append(token)
        for slot in slots:
            if not slot:
                continue
            rate = Counter(slot).most_common(1)[0][1] / len(slot)
            if rate > best:
                best = rate
    return best


def _most_frequent(lines: Sequence[Sequence[str]]) -> str | None:
    counts: Counter[str] = Counter(token for line in lines for token in line)
    if not counts:
        return None
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[0][0]


def _null_summary(observed: float, samples: Sequence[float | None], *, lower_tail: bool) -> dict[str, Any]:
    valid = [sample for sample in samples if sample is not None]
    if lower_tail:
        hits = sum(1 for sample in valid if sample <= observed + 1e-12)
    else:
        hits = sum(1 for sample in valid if sample + 1e-12 >= observed)
    undefined = len(samples) - len(valid)
    fraction = _fraction(hits, len(samples))
    return {
        "observed": observed,
        "null_mean": (sum(valid) / len(valid)) if valid else None,
        "hits": hits,
        "undefined": undefined,
        "trials": len(samples),
        "fraction": fraction,
        "lower_tail": lower_tail,
    }


def _tail_hit(summary: dict[str, Any] | None, alpha: float) -> bool:
    if summary is None:
        return False
    fraction = summary.get("fraction")
    return fraction is not None and fraction <= alpha


def _sequence_count(lines: Sequence[Sequence[str]], pattern: tuple[str, ...]) -> int:
    width = len(pattern)
    total = 0
    for line in lines:
        if len(line) < width:
            continue
        for start in range(len(line) - width + 1):
            if tuple(line[start : start + width]) == pattern:
                total += 1
    return total


def _chant_verses_on_line(tokens: Sequence[str]) -> int:
    """Full frames on one mapped line: X, copula, Y, product, Z, all non-empty."""
    hits = 0
    copulas = [(index, len(pattern)) for pattern in COPULA_SEQUENCES for index in _starts(tokens, pattern)]
    products = [(index, len(pattern)) for pattern in PRODUCT_SEQUENCES for index in _starts(tokens, pattern)]
    for copula_at, copula_len in copulas:
        if copula_at <= 0:
            continue
        for product_at, product_len in products:
            if product_at < copula_at + copula_len:
                continue
            if product_at == copula_at + copula_len:
                continue
            if product_at + product_len >= len(tokens):
                continue
            hits += 1
            break
    return hits


def _starts(tokens: Sequence[str], pattern: tuple[str, ...]) -> list[int]:
    width = len(pattern)
    return [
        index
        for index in range(len(tokens) - width + 1)
        if tuple(tokens[index : index + width]) == pattern
    ]


_GROUP_CACHE: dict[str, list[tuple[str, list[str]]]] = {}


def _warm_group_cache() -> None:
    """Read each vendored side once."""
    if "_warmed" in _GROUP_CACHE:
        return
    for located in load_located_sides():
        rows = [
            (f"{located.side}{number}", list(tokens))
            for number, tokens in located.lines
            if tokens
        ]
        _GROUP_CACHE[located.side] = rows
    for side in ("Ra", "Rb"):
        lines = load_barthel_lines(side)
        names = sorted(lines, key=lambda name: int(name[len(side) :]))
        _GROUP_CACHE[side] = [(name, list(lines[name])) for name in names if lines[name]]
    _GROUP_CACHE["_warmed"] = []


def _published_groups(side: str) -> list[tuple[str, list[str]]]:
    """Hyphen groups for one Barthel side, in published line order."""
    _warm_group_cache()
    try:
        return _GROUP_CACHE[side]
    except KeyError as exc:
        raise KeyError(side) from exc


def _stem_lines(group_rows: Sequence[tuple[str, list[str]]]) -> list[list[str]]:
    return [[stem for group in groups for stem in group_stems(group)] for _name, groups in group_rows]


def _bracket_census(group_rows: Sequence[tuple[str, list[str]]]) -> dict[str, Any]:
    phrases = 0
    links = 0
    longest = 0
    examples: list[dict[str, Any]] = []
    for name, groups in group_rows:
        found = extract_strict_phrases(groups, name)
        phrases += len(found)
        links += chain_links(found)
        longest = max(longest, max_chain_run(found))
        for phrase in found[:4]:
            if len(examples) < 6:
                examples.append(
                    {
                        "line": phrase.line,
                        "index": phrase.index,
                        "groups": list(phrase.groups),
                        "child": list(phrase.child),
                        "father": list(phrase.father),
                    }
                )
    return {"phrases": phrases, "links": links, "max_run": longest, "examples": examples}


def _load_sign_lines() -> dict[str, Any]:
    """mdl_cued units on H/P/Q. The 267 types must match the stored lexicon."""
    merge_table = load_merge_table()
    passages = load_significant_passages()
    lines = load_lines(merge_table)
    indel_cuts, _events = indel_cut_set(passages)
    cuts = sign_cuts(lines) | indel_cuts
    alphabet = len({stem.normalized for line in lines for stem in line.stems})
    trained = greedy_segment(
        explode_hapax_chunks(utterances_cued(lines, cuts)),
        objective="mdl",
        alphabet=alphabet,
    )
    locus_line = {stem.locus: stem.line for line in lines for stem in line.stems}
    gt_rows: dict[str, list[str]] = {}
    corpus_counts: Counter[tuple[str, ...]] = Counter()
    gt_counts: Counter[tuple[str, ...]] = Counter()
    tablets_of: dict[tuple[str, ...], set[str]] = defaultdict(set)
    for utterance in trained["utterances"]:
        if not utterance or not utterance[0].loci:
            continue
        line_name = locus_line[utterance[0].loci[0]]
        tablet = utterance[0].loci[0][0][0]
        tokens = []
        for word in utterance:
            if word.loci[0][0][0] != tablet:
                raise RuntimeError("a segmented utterance crosses tablets")
            corpus_counts[word.signs] += 1
            tokens.append("+".join(word.signs))
            if tablet in GT_TABLETS:
                gt_counts[word.signs] += 1
                tablets_of[word.signs].add(tablet)
        if tablet in GT_TABLETS:
            gt_rows.setdefault(line_name, []).extend(tokens)
    stored = json.loads(UNITS_PATH.read_text(encoding="utf-8"))
    expected = {tuple(unit["signs"]): int(unit["count"]) for unit in stored["lexicon"]["items"]}
    got = {signs: count for signs, count in gt_counts.items() if count >= 2}
    if got != expected:
        missing = sorted(set(expected) - set(got))[:5]
        extra = sorted(set(got) - set(expected))[:5]
        raise RuntimeError(f"mdl_cued lexicon drifted; missing {missing}, extra {extra}")
    families: dict[str, list[str]] = {
        "all_recurring": [],
        "monosign": [],
        "multisign": [],
        "gt_only": [],
        "also_outside": [],
        "ends_076": [],
        "marker_095": [],
    }
    catalog = []
    for signs, count in sorted(got.items(), key=lambda item: (-item[1], item[0])):
        unit_id = "+".join(signs)
        record = {
            "id": unit_id,
            "signs": list(signs),
            "length": len(signs),
            "count": count,
            "corpus_count": corpus_counts[signs],
            "tablets": sorted(tablets_of[signs]),
            "reading": None,
        }
        catalog.append(record)
        families["all_recurring"].append(unit_id)
        families["monosign" if len(signs) == 1 else "multisign"].append(unit_id)
        if corpus_counts[signs] == count:
            families["gt_only"].append(unit_id)
        else:
            families["also_outside"].append(unit_id)
        if signs[-1] == "076":
            families["ends_076"].append(unit_id)
        if signs == ("095",):
            families["marker_095"].append(unit_id)
    ordered = [gt_rows[name] for name in sorted(gt_rows)]
    stem_lines = [[stem.normalized for stem in line.stems] for line in lines if line.tablet in GT_TABLETS]
    multi_tablet = sum(1 for signs in got if len(tablets_of[signs]) > 1)
    return {
        "segmenter": PRIMARY_SEGMENTER,
        "lines": ordered,
        "line_names": sorted(gt_rows),
        "families": families,
        "catalog": catalog,
        "stem_lines": stem_lines,
        "multi_tablet_types": multi_tablet,
        "rounds": trained.get("rounds"),
    }


def _load_language() -> dict[str, Any]:
    rows = primary_running_lines(include_elliptical=True)
    raw = [list(row.words) for row in rows]
    _surface, syllable_groups, rejected = _cv_lines(raw)
    richness, ranked = _count_formulae(syllable_groups, FORMULA_WIDTH, FORMULA_MIN_COUNT)
    meta = []
    tokens: list[list[str]] = []
    for row in rows:
        line: list[str] = []
        for word in row.words:
            parsed = cv_syllables_mapped(word)
            if not parsed:
                continue
            line.append("".join(parsed))
        if line:
            tokens.append(line)
            meta.append({"source": row.source, "line_id": row.line_id, "elliptical": row.elliptical})
    if richness != 577:
        raise RuntimeError(f"three-word formula count is {richness}, not the Round 3 lock of 577")
    return {
        "lines": tokens,
        "meta": meta,
        "rejected": rejected,
        "formula_types": richness,
        "top_formulas": [{"formula": text, "count": count} for text, count in ranked[:12]],
    }


def _chant_block(language_lines: Sequence[Sequence[str]], meta: Sequence[dict[str, Any]]) -> dict[str, Any]:
    verses = atua_matariri_verses()
    parsed = parse_atua_formula(verses)
    gap_histogram_chant = Counter({int(key): int(value) for key, value in parsed["adjacent_gap_histogram"].items()})
    sequences = []
    for pattern in COPULA_SEQUENCES + PRODUCT_SEQUENCES:
        by_source: Counter[str] = Counter()
        mamari = 0
        for tokens, info in zip(language_lines, meta):
            count = _sequence_count([tokens], pattern)
            if count:
                by_source[info["source"]] += count
                if info["elliptical"] and str(info["line_id"]).lower().startswith("c"):
                    mamari += count
        sequences.append(
            {
                "pattern": " ".join(pattern),
                "total": sum(by_source.values()),
                "by_source": dict(by_source),
                "metoro_mamari": mamari,
            }
        )
    verse_hits = []
    for tokens, info in zip(language_lines, meta):
        count = _chant_verses_on_line(tokens)
        if count:
            verse_hits.append({"source": info["source"], "line_id": info["line_id"], "hits": count})
    slot_widths: Counter[str] = Counter()
    for verse in verses:
        frame = _FRAME.search(verse)
        if frame is None:
            continue
        product = _PRODUCT.search(verse, frame.end())
        if product is None:
            continue
        slots = {
            "x": verse[: frame.start()],
            "y": verse[frame.end() : product.start()],
            "z": verse[product.end() :],
        }
        for name, text in slots.items():
            slot_widths[f"{name}:{len(_WORD.findall(text))}"] += 1
    return {
        "verses": parsed["verse_count"],
        "full_formula": parsed["full_formula_count"],
        "adjacent_gaps": parsed["adjacent_gap_count"],
        "adjacent_gap_histogram": {str(key): value for key, value in sorted(gap_histogram_chant.items())},
        "gap_counter": gap_histogram_chant,
        "sequences": sequences,
        "mapped_verse_lines": verse_hits,
        "printed_slot_width_counts": dict(sorted(slot_widths.items())),
        "fischer_spelling": "X ki 'ai ki roto ki 'a Y: ka pu te Z",
        "status": "hypothesis",
    }


def _closeness_test(
    lines_of: dict[str, list[list[str]]],
    text_id: str,
    predicate: Callable[[str], bool],
    reference: Counter[int],
    rng: random.Random,
) -> dict[str, Any]:
    lines = lines_of[text_id]
    observed_hist = gap_histogram(lines, predicate)
    observed = histogram_l1(observed_hist, reference)
    gaps = sum(observed_hist.values())
    if observed is None:
        return {
            "text": text_id,
            "tested": False,
            "reason": "no_delimiter",
            "gaps": gaps,
            "histogram": {str(key): value for key, value in sorted(observed_hist.items())},
        }
    samples: list[float | None] = []
    for _trial in range(SKELETON_TRIALS):
        shuffled = _shuffle_lines(lines, rng)
        samples.append(histogram_l1(gap_histogram(shuffled, predicate), reference))
    summary = _null_summary(observed, samples, lower_tail=True)
    return {
        "text": text_id,
        "tested": True,
        "reason": None,
        "gaps": gaps,
        "histogram": {str(key): value for key, value in sorted(observed_hist.items())[:12]},
        "null": summary,
    }


def _upper_test(
    observed: float,
    samples: list[float],
) -> dict[str, Any]:
    return _null_summary(observed, samples, lower_tail=False)


def _run_matches(sign_lines: list[list[str]], sign_families: dict[str, list[str]], word_lines: list[list[str]]) -> dict[str, Any]:
    sign_fixed = _sign_bundle(sign_lines, sign_families)
    language_fixed = _language_bundle(word_lines)
    bonferroni = _bonferroni(len(PRIMARY_PAIRS))
    observed: dict[tuple[str, str], dict[str, Any] | None] = {}
    for sign_name, language_name in PRIMARY_PAIRS:
        observed[(sign_name, language_name)] = profile_l1(
            sign_fixed["profiles"][sign_name],
            language_fixed["profiles"][language_name],
        )
    sign_hits = Counter()
    sign_rng = random.Random(SIGN_NULL_SEED)
    for _trial in range(NULL_TRIALS):
        shuffled = _shuffle_lines(sign_lines, sign_rng)
        profiles = _sign_bundle(shuffled, sign_families)["profiles"]
        for pair, baseline in observed.items():
            if baseline is None:
                continue
            sample = profile_l1(profiles[pair[0]], language_fixed["profiles"][pair[1]])
            if sample is not None and sample["distance"] <= baseline["distance"] + 1e-12:
                sign_hits[pair] += 1
    language_hits = Counter()
    zipf_hits = 0
    zipf_undefined = 0
    zipf_samples: list[float] = []
    frame_hits_language = 0
    frame_hits_sign = 0
    sign_frame_rate = sign_fixed["frame_rate"]
    language_frame_rate = language_fixed["frame_rate"]
    frame_gap = None
    if sign_frame_rate is not None and language_frame_rate is not None:
        frame_gap = abs(sign_frame_rate - language_frame_rate)
    sign_frame_closer = 0
    language_frame_closer = 0
    language_rng = random.Random(LANGUAGE_NULL_SEED)
    sign_frame_rng = random.Random(SIGN_NULL_SEED + 17)
    for _trial in range(NULL_TRIALS):
        shuffled_words = _shuffle_lines(word_lines, language_rng)
        bundle = _language_bundle(shuffled_words)
        slope = bundle["zipf_formulas"]
        if slope is None or language_fixed["zipf_formulas"] is None or sign_fixed["zipf_floor4"] is None:
            zipf_undefined += 1
        else:
            real_gap = abs(sign_fixed["zipf_floor4"] - language_fixed["zipf_formulas"])
            sample_gap = abs(sign_fixed["zipf_floor4"] - slope)
            zipf_samples.append(sample_gap)
            if sample_gap <= real_gap + 1e-12:
                zipf_hits += 1
        if frame_gap is not None and bundle["frame_rate"] is not None and sign_frame_rate is not None:
            if abs(sign_frame_rate - bundle["frame_rate"]) <= frame_gap + 1e-12:
                language_frame_closer += 1
        for pair, baseline in observed.items():
            if baseline is None:
                continue
            sample = profile_l1(sign_fixed["profiles"][pair[0]], bundle["profiles"][pair[1]])
            if sample is not None and sample["distance"] <= baseline["distance"] + 1e-12:
                language_hits[pair] += 1
        if language_fixed["frames"] > 0 and bundle["frames"] >= language_fixed["frames"]:
            frame_hits_language += 1
    for _trial in range(NULL_TRIALS):
        shuffled_signs = _shuffle_lines(sign_lines, sign_frame_rng)
        sample_rate = _sign_bundle(shuffled_signs, sign_families)["frame_rate"]
        if (
            frame_gap is not None
            and sample_rate is not None
            and language_frame_rate is not None
            and abs(sample_rate - language_frame_rate) <= frame_gap + 1e-12
        ):
            sign_frame_closer += 1
        sample_frames = productive_frame_count(shuffled_signs)
        if sample_frames >= sign_fixed["frames"]:
            frame_hits_sign += 1
    rows = []
    for pair in PRIMARY_PAIRS:
        baseline = observed[pair]
        sign_fraction = _fraction(sign_hits[pair], NULL_TRIALS)
        language_fraction = _fraction(language_hits[pair], NULL_TRIALS)
        tested = baseline is not None
        raw = bool(
            tested
            and sign_fraction is not None
            and language_fraction is not None
            and sign_fraction <= ADOPT_FRACTION
            and language_fraction <= ADOPT_FRACTION
        )
        corrected = bool(
            tested
            and sign_fraction is not None
            and language_fraction is not None
            and sign_fraction <= bonferroni
            and language_fraction <= bonferroni
        )
        rows.append(
            {
                "sign_family": pair[0],
                "language_family": pair[1],
                "tested": tested,
                "distance": None if baseline is None else baseline["distance"],
                "features": [] if baseline is None else baseline["features"],
                "sign_null_hits": sign_hits[pair],
                "language_null_hits": language_hits[pair],
                "trials": NULL_TRIALS,
                "sign_p": sign_fraction,
                "language_p": language_fraction,
                "clears_uncorrected": raw,
                "match": corrected,
            }
        )
    real_zipf_gap = None
    if sign_fixed["zipf_floor4"] is not None and language_fixed["zipf_formulas"] is not None:
        real_zipf_gap = abs(sign_fixed["zipf_floor4"] - language_fixed["zipf_formulas"])
    zipf_valid = NULL_TRIALS - zipf_undefined
    zipf_p = _fraction(zipf_hits, zipf_valid)
    zipf_informative = zipf_valid >= (NULL_TRIALS // 2)
    zipf_match = bool(
        zipf_informative
        and real_zipf_gap is not None
        and real_zipf_gap <= ZIPF_SLOPE_TOLERANCE
        and zipf_p is not None
        and zipf_p <= ADOPT_FRACTION
    )
    return {
        "bonferroni": bonferroni,
        "pairs": rows,
        "sign_profiles": sign_fixed["profiles"],
        "language_profiles": language_fixed["profiles"],
        "family_sizes": {
            "signs": {name: len(members) for name, members in sign_families.items()},
            "language": language_fixed["families"],
            "words_min4": language_fixed["word_types_min4"],
        },
        "zipf": {
            "sign_units": sign_fixed["zipf"],
            "sign_units_floor4": sign_fixed["zipf_floor4"],
            "formulas": language_fixed["zipf_formulas"],
            "words_min4": language_fixed["zipf_words"],
            "words_all": language_fixed["zipf_words_all"],
            "absolute_gap_signs_formulas": real_zipf_gap,
            "tolerance": ZIPF_SLOPE_TOLERANCE,
            "null_hits": zipf_hits,
            "undefined": zipf_undefined,
            "valid": zipf_valid,
            "informative": zipf_informative,
            "trials": NULL_TRIALS,
            "p": zipf_p,
            "null_mean_gap": (sum(zipf_samples) / len(zipf_samples)) if zipf_samples else None,
            "match": zipf_match,
            "word_slope_null": "Within-line shuffle keeps word frequencies, so the word Zipf slope has no order-null.",
        },
        "productivity": {
            "sign_frames": sign_fixed["frames"],
            "sign_frame_rate": sign_fixed["frame_rate"],
            "sign_bigram_tokens": sign_fixed["bigram_tokens"],
            "language_frames": language_fixed["frames"],
            "language_frame_rate": language_fixed["frame_rate"],
            "language_bigram_tokens": language_fixed["bigram_tokens"],
            "rate_gap": frame_gap,
            "sign_closer_hits": sign_frame_closer,
            "language_closer_hits": language_frame_closer,
            "sign_richness_hits": frame_hits_sign,
            "language_richness_hits": frame_hits_language,
            "trials": NULL_TRIALS,
            "sign_closer_p": _fraction(sign_frame_closer, NULL_TRIALS),
            "language_closer_p": _fraction(language_frame_closer, NULL_TRIALS),
            "match": bool(
                frame_gap is not None
                and _fraction(sign_frame_closer, NULL_TRIALS) <= ADOPT_FRACTION
                and _fraction(language_frame_closer, NULL_TRIALS) <= ADOPT_FRACTION
            ),
        },
        "any_match": any(row["match"] for row in rows) or zipf_match,
        "any_uncorrected": any(row["clears_uncorrected"] for row in rows),
    }


def _run_skeleton(chant: dict[str, Any], sign_lines: list[list[str]]) -> dict[str, Any]:
    reference: Counter[int] = chant["gap_counter"]
    texts: dict[str, list[list[str]]] = {}
    stem_076: dict[str, int] = {}
    for side in SKELETON_SIDES:
        groups = _published_groups(side)
        stems = _stem_lines(groups)
        texts[side] = stems
        stem_076[side] = sum(line.count("076") for line in stems)
    texts[GT_UNIT_TEXT] = sign_lines
    rng = random.Random(SKELETON_SEED)
    suffixed = []
    for text_id in list(SKELETON_SIDES) + [GT_UNIT_TEXT]:
        if text_id == GT_UNIT_TEXT:
            predicate = lambda token: token.split("+")[-1] == "076"
        else:
            predicate = lambda token: token == "076"
        suffixed.append(_closeness_test(texts, text_id, predicate, reference, rng))
    top_token = []
    for text_id in list(SKELETON_SIDES) + [GT_UNIT_TEXT]:
        delimiter = _most_frequent(texts[text_id])
        if delimiter is None:
            top_token.append({"text": text_id, "tested": False, "reason": "empty"})
            continue
        row = _closeness_test(texts, text_id, lambda token, delimiter=delimiter: token == delimiter, reference, rng)
        row["delimiter"] = delimiter
        top_token.append(row)
    alpha_texts = _bonferroni(len(SKELETON_SIDES) + 1)
    for row in suffixed + top_token:
        null = row.get("null")
        row["match"] = bool(row.get("tested") and _tail_hit(null, alpha_texts))
    tile_rows = []
    tile_rng = random.Random(SKELETON_SEED + 1)
    for text_id in list(SKELETON_SIDES) + [GT_UNIT_TEXT]:
        lines = texts[text_id]
        observed = float(tile_line_count(lines))
        samples = [float(tile_line_count(_shuffle_lines(lines, tile_rng))) for _trial in range(SKELETON_TRIALS)]
        summary = _upper_test(observed, samples)
        tile_rows.append(
            {
                "text": text_id,
                "tiled_lines": int(observed),
                "null": summary,
                "match": _tail_hit(summary, alpha_texts),
            }
        )
    elided_rows = []
    elided_ids = list(ELIDED_SIDES) + [GT_UNIT_TEXT]
    elided_alpha = _bonferroni(len(elided_ids))
    elided_rng = random.Random(SKELETON_SEED + 2)
    for text_id in elided_ids:
        lines = texts[text_id]
        observed = slot_constancy(lines)
        samples = [slot_constancy(_shuffle_lines(lines, elided_rng)) for _trial in range(SKELETON_TRIALS)]
        summary = _upper_test(observed, samples)
        elided_rows.append(
            {
                "text": text_id,
                "modal_slot_rate": observed,
                "null": summary,
                "more_constant_than_chance": _tail_hit(summary, elided_alpha),
            }
        )
    return {
        "bonferroni_texts": alpha_texts,
        "elided_bonferroni": elided_alpha,
        "stem_076": stem_076,
        "suffixed_076": suffixed,
        "top_token_gaps": top_token,
        "two_frame_tiles": tile_rows,
        "elided_triples": elided_rows,
        "any_spacing_match": any(row["match"] for row in suffixed + top_token),
        "any_tile_match": any(row["match"] for row in tile_rows),
        "any_elided_marker": any(row["more_constant_than_chance"] for row in elided_rows),
        "note": (
            "A spacing or tile hit is a repeat-structure resemblance. "
            "reading stays null. Fischer's elided triad, with the function words unwritten, "
            "predicts variable slots and is not confirmed by a non-significant constancy test."
        ),
    }


def _run_genealogy(sign_pack: dict[str, Any], word_lines: list[list[str]]) -> dict[str, Any]:
    alpha = _bonferroni(3)
    streams = {
        "rapanui_words": word_lines,
        "gt_units": sign_pack["lines"],
        "gt_stems": sign_pack["stem_lines"],
    }
    rows = []
    rng = random.Random(HANDOFF_SEED)
    for name, lines in streams.items():
        observed = corpus_longest_handoff(lines)
        example = best_handoff_example(lines)
        samples = [corpus_longest_handoff(_shuffle_lines(lines, rng)) for _trial in range(HANDOFF_TRIALS)]
        at_least_3 = sum(1 for sample in samples if sample >= HANDOFF_MIN_LINKS)
        at_least_observed = sum(1 for sample in samples if sample >= observed)
        claim_p = _fraction(at_least_observed, HANDOFF_TRIALS)
        rows.append(
            {
                "stream": name,
                "longest_links": observed,
                "example": example,
                "trials": HANDOFF_TRIALS,
                "shuffles_reaching_gv6_length": at_least_3,
                "p_gv6_length": _fraction(at_least_3, HANDOFF_TRIALS),
                "shuffles_reaching_observed": at_least_observed,
                "p_at_least_observed": claim_p,
                "lines_up": observed >= HANDOFF_MIN_LINKS and claim_p is not None and claim_p <= alpha,
            }
        )
    brackets = {}
    for side in ("Gv", "Gr", "Ia", "Ca", "Cb", "Hr", "Hv", "Pr", "Pv", "Qr", "Qv"):
        brackets[side] = _bracket_census(_published_groups(side))
    gv6 = _published_groups("Gv")
    gv6_line = [groups for name, groups in gv6 if name == "Gv6"]
    if len(gv6_line) != 1:
        raise RuntimeError("Gv6 is missing")
    gv6_rng = random.Random(HANDOFF_SEED + 1)
    gv6_observed = _bracket_census([("Gv6", gv6_line[0])])
    gv6_samples = []
    for _trial in range(HANDOFF_TRIALS):
        shuffled = list(gv6_line[0])
        gv6_rng.shuffle(shuffled)
        gv6_samples.append(_bracket_census([("Gv6", shuffled)])["links"])
    gv6_hits = sum(1 for sample in gv6_samples if sample >= HANDOFF_MIN_LINKS)
    gt_groups = []
    for side in ("Hr", "Hv", "Pr", "Pv", "Qr", "Qv"):
        gt_groups.extend(_published_groups(side))
    gt_observed = _bracket_census(gt_groups)
    gt_rng = random.Random(HANDOFF_SEED + 2)
    gt_hits = 0
    for _trial in range(HANDOFF_TRIALS):
        shuffled_rows = [(name, _shuffle_tokens(groups, gt_rng)) for name, groups in gt_groups]
        if _bracket_census(shuffled_rows)["links"] >= HANDOFF_MIN_LINKS:
            gt_hits += 1
    return {
        "bonferroni": alpha,
        "threshold_links": HANDOFF_MIN_LINKS,
        "abstract_chains": rows,
        "bracket_by_side": brackets,
        "gv6": {
            "phrases": gv6_observed["phrases"],
            "links": gv6_observed["links"],
            "max_run": gv6_observed["max_run"],
            "examples": gv6_observed["examples"],
            "trials": HANDOFF_TRIALS,
            "shuffles_with_at_least_3_links": gv6_hits,
            "p": _fraction(gv6_hits, HANDOFF_TRIALS),
            "prior_null": "Track 3 already reported 0 of 5000 Gv6 shuffles with 3 handoffs.",
        },
        "great_tradition_bracket": {
            "phrases": gt_observed["phrases"],
            "links": gt_observed["links"],
            "max_run": gt_observed["max_run"],
            "trials": HANDOFF_TRIALS,
            "shuffles_with_at_least_3_links": gt_hits,
            "p": _fraction(gt_hits, HANDOFF_TRIALS),
            "lines_up": gt_observed["links"] >= HANDOFF_MIN_LINKS and (gt_hits / HANDOFF_TRIALS) <= ADOPT_FRACTION,
        },
        "any_oral_lineup": any(row["lines_up"] for row in rows if row["stream"] == "rapanui_words"),
        "any_gt_lineup": any(row["lines_up"] for row in rows if row["stream"] != "rapanui_words")
        or (gt_observed["links"] >= HANDOFF_MIN_LINKS and (gt_hits / HANDOFF_TRIALS) <= ADOPT_FRACTION),
    }


def _shuffle_tokens(tokens: list[str], rng: random.Random) -> list[str]:
    row = list(tokens)
    rng.shuffle(row)
    return row


def _fmt(value: Any, places: int = 3) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{places}f}"
    return str(value)


def _p_text(summary: dict[str, Any] | None) -> str:
    if not summary:
        return "n/a"
    fraction = summary.get("fraction")
    if fraction is None:
        return "n/a"
    return f"{summary['hits']}/{summary['trials']} = {_fmt(fraction)}"


def render_markdown(result: dict[str, Any]) -> str:
    """Plain-English note. Every number is taken from ``result``."""
    matches = result["matches"]
    skeleton = result["skeleton"]
    genealogy = result["genealogy"]
    chant = result["chant"]
    lines: list[str] = []
    add = lines.append
    add("# Round 4, Track B — Sign units against Rapanui formulas")
    add("")
    if result["verdict_code"] == "no_match":
        add("**Verdict: nothing matches.**")
    elif result["verdict_code"] == "spacing_only":
        add("**Verdict: the formulas do not match. A short-gap resemblance does, and it is not a reading.**")
    else:
        add("**Verdict: a pre-registered test cleared its bar. Read the paragraph below before treating that as a decipherment.**")
    add("")
    add(result["verdict"])
    add("")
    add("This note compares shapes of repetition. It does not match sounds, and it does not read a sign. `reading` is null. The provider is MockProvider and is never asked for a completion. Provider calls: 0.")
    add("")
    add("## What was compared")
    add("")
    add(f"The sign side is the {result['signs']['types']} recurring units from Round 3 Track A (`{result['signs']['segmenter']}` on tablets H, P, and Q). {result['signs']['multisign']} of them contain more than one stem. {result['signs']['multi_tablet_types']} occur on more than one of those three tablets. That cross-copy recurrence has no twin in the chants, which are not written out three times, so it is reported and not forced into the match score.")
    add("")
    add(f"The language side is the Round 3 running text: Thomson's chants without the love song, Metoro's recitations, and Routledge's timo formula. Mapped (C)V spellings are used, so `tagata` and `tangata` count as one word. Rejected tokens: {result['language']['rejected']}. Three-word formulas at count at least 4: {result['language']['formula_types']}, the same 577 as Round 3. The most frequent is still `{result['language']['top_formulas'][0]['formula']}` ({result['language']['top_formulas'][0]['count']}).")
    add("")
    add("The two ranked lists below are separate. Sharing a row does not pair a sign with a word.")
    add("")
    add("| Rank | Sign unit | H/P/Q count | Formula | Count |")
    add("| ---: | --- | ---: | --- | ---: |")
    for index in range(8):
        unit = result["signs"]["top"][index]
        formula = result["language"]["top_formulas"][index]
        add(
            f"| {index + 1} | `{unit['id']}` | {unit['count']} | `{formula['formula']}` | {formula['count']} |"
        )
    add("")
    add("## How a match was defined")
    add("")
    add("These rules were fixed before the shuffles ran.")
    add("")
    add("Each type gets four numbers: burstiness of the gaps between its repeats on the same line (population standard deviation; at least two gaps), the share of its hits that start a line, the share that finish a line, and the share that are immediately followed by the same type. For a three-word formula, \"immediately\" means the next copy starts where this copy ends. The family score is the mean of those numbers across types. Families with fewer than 8 types are described and not tested. Burstiness is left out of a comparison when fewer than 8 types have two gaps. The distance is the sum of absolute differences on the features that remain, and at least three features are required.")
    add("")
    add(f"The sign null shuffles units inside each Great Tradition line ({NULL_TRIALS} draws, seed {SIGN_NULL_SEED}). The language null shuffles words inside each chant line ({NULL_TRIALS} draws, seed {LANGUAGE_NULL_SEED}) and rebuilds the formulas. A pair matches only when both fractions are at or under {matches['bonferroni']:.4f}, which is 0.05 divided by {len(PRIMARY_PAIRS)} pairs. Clearing 0.05 on its own is recorded and is not a match.")
    add("")
    add(f"Zipf slopes are a separate test. Formula slopes are recomputed after the word shuffle. A match needs the absolute gap between the sign slope and the formula slope to be at most {ZIPF_SLOPE_TOLERANCE}, and the closeness p-value at or under 0.05. Shuffling words does not change word frequencies, so the word slope is described and not given a p-value.")
    add("")
    add("## Frequency, position, spacing")
    add("")
    zipf = matches["zipf"]
    add(
        f"Sign-unit Zipf slope, every recurring unit (count at least 2): {_fmt(zipf['sign_units'], 4)}. "
        f"The same units kept only when the count is at least 4, which is the formula floor: {_fmt(zipf['sign_units_floor4'], 4)}. "
        f"Three-word formula slope: {_fmt(zipf['formulas'], 4)}. Words at that floor: {_fmt(zipf['words_min4'], 4)}. "
        f"All words: {_fmt(zipf['words_all'], 4)}. The Zipf test uses the shared floor of 4. "
        f"Absolute gap between those sign units and the formulas: {_fmt(zipf['absolute_gap_signs_formulas'], 4)}. "
        f"Among shuffles that still had a formula slope, {zipf['null_hits']}/{zipf['valid']} were at least as close "
        f"(p = {_fmt(zipf['p'])}). Shuffles with no slope: {zipf['undefined']}. "
        "A p-value of zero here means the real formulas sit closer to the sign slope than the shuffled formulas do. "
        f"The leftover gap is still {_fmt(zipf['absolute_gap_signs_formulas'], 4)}, and the gate is {ZIPF_SLOPE_TOLERANCE}. "
        f"Within that tolerance: {zipf['match']}."
    )
    add("")
    add("Family sizes. Sign units: "
        + ", ".join(f"{name} {size}" for name, size in matches["family_sizes"]["signs"].items())
        + ". Formula classes: "
        + ", ".join(f"{name} {size}" for name, size in matches["family_sizes"]["language"].items())
        + f". Words at count at least 4: {matches['family_sizes']['words_min4']}.")
    add("")
    add("| Sign family | Language family | Distance | Sign shuffle p | Language shuffle p | Match |")
    add("| --- | --- | ---: | --- | --- | --- |")
    for row in matches["pairs"]:
        if not row["tested"]:
            add(f"| {row['sign_family']} | {row['language_family']} | n/a | not tested | not tested | no |")
            continue
        add(
            f"| {row['sign_family']} | {row['language_family']} | {_fmt(row['distance'], 4)} | "
            f"{row['sign_null_hits']}/{row['trials']} = {_fmt(row['sign_p'])} | "
            f"{row['language_null_hits']}/{row['trials']} = {_fmt(row['language_p'])} | "
            f"{'yes' if row['match'] else 'no'} |"
        )
    add("")
    productivity = matches["productivity"]
    add(
        f"Productive frames are bigrams that occur at least 4 times and are followed by at least 4 different next words. "
        f"Great Tradition units: {productivity['sign_frames']} such bigrams "
        f"(rate {_fmt(productivity['sign_frame_rate'], 4)} per adjacent pair). "
        f"Rapanui words: {productivity['language_frames']} "
        f"(rate {_fmt(productivity['language_frame_rate'], 4)}). "
        f"Closeness of those rates: sign shuffle p = {_fmt(productivity['sign_closer_p'])}, "
        f"word shuffle p = {_fmt(productivity['language_closer_p'])}. "
        "A low word-shuffle p-value means the real chant is closer to the sign rate than a shuffled chant is. "
        "A high sign-shuffle p-value means shuffling the signs usually gets at least as close, so the signs are not the side that carries a formula shape. "
        f"Match: {productivity['match']}."
    )
    add("")
    if not matches["any_match"] and not productivity["match"]:
        add("No pair, and not the Zipf test, and not the frame-rate test, clears its rule. The recurring sign units do not share a formula family's shape beyond chance.")
    add("")
    add("## The creation chant")
    add("")
    add("Thomson 1891, pp. 520–521, prints Ure Vaeiko's Atua Matariri. "
        f"Of {chant['verses']} verses, {chant['full_formula']} contain both the copula (`Ki ai Kiroto` or `Kia ai Kiroto`) and a product marker (`Kapu te`, `Kapu to`, or the one `Mapu te`). "
        f"There are {chant['adjacent_gaps']} gaps between adjacent full verses. "
        "The paraphrase \"X couples with Y and Z comes forth\" is Thomson's heading for the chant, not a sign reading.")
    add("")
    add("Fischer 1995, *Rapa Nui Journal* 9(4), writes the same frame as \"X ki 'ai ki roto ki 'a Y: ka pu te Z\" and says a further search found the same kind of text on Mamari (his RR 2), often without the phallic suffix he uses on the Staff. The Staff proposal is his *Journal of the Polynesian Society* paper the same year. Guy 1998, *Anthropos* 93: 552–555, rejects the reading. Barthel 1958, pp. 242–247, is a different Mamari claim: the lunar calendar on Ca6–Ca9, already tested in Track 1. Kohaumotu's staff note says Barthel read glyph 76 as a phallus; Fischer cites Barthel 1958 and 1963 for Metoro's sign-words. Those values stay hypotheses and are not used here.")
    add("")
    add("Mapped tokens in the running text, counted as spelled, not rewritten into Fischer's spacing:")
    add("")
    add("| Pattern | Total | Metoro on Mamari |")
    add("| --- | ---: | ---: |")
    for row in chant["sequences"]:
        add(f"| `{row['pattern']}` | {row['total']} | {row['metoro_mamari']} |")
    add("")
    if chant["mapped_verse_lines"]:
        add("Lines that contain a full mapped frame (non-empty X, Y, and Z):")
        add("")
        for row in chant["mapped_verse_lines"]:
            add(f"- {row['source']} `{row['line_id']}`: {row['hits']}")
        add("")
    else:
        add("No mapped line in the running text contains the full frame with a non-empty X, a non-empty Y, and a non-empty Z. Thomson's print has the frame; the syllable map splits `Kiroto` and `Kapu` into one word each (`kiroto`, `kapu`), so the pattern that fires is `ki ai kiroto` plus `kapu te`, when the chant section is one line.")
        add("")
    add(f"The sign test asks whether a passage repeats the way the chant repeats. Two constant delimiters must tile a line for at least {SKELETON_MIN_CYCLES} cycles, and both slots must have type/token ratio at least {SKELETON_TTR_MIN}. Separately, gaps between stem 076, and gaps between the single most frequent token, are compared with the chant's verse-gap histogram. The bar for {len(SKELETON_SIDES) + 1} texts is p ≤ {_fmt(skeleton['bonferroni_texts'], 4)}. A hit would be a spacing resemblance, not a reading.")
    add("")
    add("Stem 076 counts: " + ", ".join(f"{side} {count}" for side, count in skeleton["stem_076"].items()) + ".")
    add("")
    add("| Text | 076-gap p (closer than shuffle) | Most frequent sign, and its gap p | Tiled lines | Tile p |")
    add("| --- | --- | --- | ---: | --- |")
    tiles = {row["text"]: row for row in skeleton["two_frame_tiles"]}
    tops = {row["text"]: row for row in skeleton["top_token_gaps"]}
    for row in skeleton["suffixed_076"]:
        top = tops[row["text"]]
        tile = tiles[row["text"]]
        suffix_p = "no 076 gaps" if not row["tested"] else _p_text(row.get("null"))
        if not top.get("tested"):
            top_p = "not tested"
        else:
            top_p = f"`{top.get('delimiter')}`, {_p_text(top.get('null'))}"
        add(
            f"| {row['text']} | {suffix_p} | {top_p} | {tile['tiled_lines']} | {_p_text(tile['null'])} |"
        )
    add("")
    add(
        "On Ia and on Gv the most frequent sign is 076, so those two columns are one comparison written twice. "
        "The chant's 38 verse gaps are 18 of length 3, 15 of length 4, and five longer. "
        "Staff 076 has 550 gaps and peaks at 3 (197) and 4 (137). "
        "That is the resemblance Track 4 already measured. Gv's 35 gaps of 076 peak at 4 (13). "
        "Gr's most frequent sign is 001, with 47 gaps peaking at 3 (10). "
        "Closer than a shuffle is not the same as close: distances are on a scale from 0 to 2."
    )
    add("")
    add("Elided triads, the version Fischer offers for tablets that lack the phallic suffix: cut the line into threes and ask whether any slot repeats one sign more than a shuffle. A failure does not prove the unwritten-frame story. Variable slots are what a shuffle looks like too. The bar is p ≤ "
        f"{_fmt(skeleton['elided_bonferroni'], 4)}.")
    add("")
    add("| Text | Modal slot rate | Shuffles at least that high |")
    add("| --- | ---: | --- |")
    for row in skeleton["elided_triples"]:
        add(
            f"| {row['text']} | {_fmt(row['modal_slot_rate'], 4)} | {_p_text(row['null'])} |"
        )
    add("")
    add("## Gv6 and the Great Tradition")
    add("")
    gv6 = genealogy["gv6"]
    add("Butinov and Knorozov 1956, as reported by Davletshin 2012 and Guy 2003, treat a short passage on the verso of Small Santiago as a genealogy. The structure used here is the one Track 3 measured, not the English sentence. "
        f"Gv6 has {gv6['phrases']} phrases of the form `200 X Y.076` and {gv6['links']} father-to-child handoffs. "
        f"In {gv6['trials']} shuffles of that line, {gv6['shuffles_with_at_least_3_links']} produced at least 3 handoffs (p = {_fmt(gv6['p'])}). "
        "Track 3's larger null was 0 of 5000. The glosses \"200 = ko\" and \"076 = ure\" stay hypotheses and are not applied.")
    add("")
    add("The same bracket on other sides:")
    add("")
    add("| Side | Phrases | Handoff links | Longest run |")
    add("| --- | ---: | ---: | ---: |")
    for side, row in genealogy["bracket_by_side"].items():
        add(f"| {side} | {row['phrases']} | {row['links']} | {row['max_run']} |")
    gt_bracket = genealogy["great_tradition_bracket"]
    add("")
    add(
        f"Pooled H/P/Q groups: {gt_bracket['phrases']} phrases and {gt_bracket['links']} links. "
        f"Shuffles of those groups produce at least 3 links in "
        f"{gt_bracket['shuffles_with_at_least_3_links']}/{gt_bracket['trials']} trials. "
        "The Great Tradition does not contain the bracket, so there is no lineup to test. "
        f"The low chance rate only says a chain of that length is hard to get by shuffling. "
        f"Lines up: {gt_bracket['lines_up']}."
    )
    add("")
    add(f"An abstract chain ignores sign numbers. It needs a constant opener, a handoff of the third slot into the next middle slot, child-slot diversity at least {CHILD_TTR_MIN}, and at least {HANDOFF_MIN_LINKS} links, the Gv6 length. The bar for three streams is p ≤ {_fmt(genealogy['bonferroni'], 4)}.")
    add("")
    add("| Stream | Longest links | Shuffles reaching 3 links | Lines up |")
    add("| --- | ---: | --- | --- |")
    for row in genealogy["abstract_chains"]:
        add(
            f"| {row['stream']} | {row['longest_links']} | "
            f"{row['shuffles_reaching_gv6_length']}/{row['trials']} = {_fmt(row['p_gv6_length'])} | "
            f"{'yes' if row['lines_up'] else 'no'} |"
        )
    add("")
    for row in genealogy["abstract_chains"]:
        example = row["example"]
        if not example:
            add(f"{row['stream']}: no chain of even one handoff met the diversity rule.")
            continue
        children = " ".join(example["children"])
        link_word = "link" if example["links"] == 1 else "links"
        add(
            f"{row['stream']}: longest chain has {example['links']} {link_word}, opener `{example['opener']}`, "
            f"child slots `{children}`. That is a word or sign pattern in the sample. It is not a decipherment."
        )
    add("")
    add("## What this does not claim")
    add("")
    add("No test in this note adopts a reading. A gap histogram that peaks on 3 or 4, on a tablet and in a chant, is a shared scale. It does not say which sign is `ki`, `ai`, `roto`, or `pu`.")
    add("")
    add("No Barthel number is given a syllable or a gloss. Fischer's sentence and the genealogy's English wording stay in the source list as hypotheses. Metoro's words are a language sample. They are not re-paired with signs here; Track 4 already found they do not label the signs. A shared Zipf slope, or a shared habit of starting lines with a frequent item, would still not name a sign.")
    add("")
    add("The run uses `MockProvider` only. Provider calls: 0.")
    add("")
    return "\n".join(lines)


def _spacing_hits(skeleton: dict[str, Any]) -> list[str]:
    """Texts whose gap histogram beat the shuffle. A repeated 076 row is kept once."""
    hits: list[str] = []
    seen: set[tuple[str, str]] = set()
    for row in skeleton["suffixed_076"]:
        if not row.get("match"):
            continue
        hits.append(f"{row['text']} stem 076")
        seen.add((row["text"], "076"))
    for row in skeleton["top_token_gaps"]:
        if not row.get("match"):
            continue
        delimiter = str(row.get("delimiter"))
        if (row["text"], delimiter) in seen:
            continue
        hits.append(f"{row['text']} sign {delimiter}")
    return hits


def _verdict(matches: dict[str, Any], skeleton: dict[str, Any], genealogy: dict[str, Any]) -> dict[str, str]:
    formula = bool(matches["any_match"] or matches["productivity"]["match"])
    chant_tile = bool(skeleton["any_tile_match"])
    elided = bool(skeleton["any_elided_marker"])
    genealogy_hit = bool(genealogy["any_oral_lineup"] or genealogy["any_gt_lineup"])
    spacing = _spacing_hits(skeleton)
    if not formula and not chant_tile and not elided and not genealogy_hit and not spacing:
        text = (
            "Nothing matches. The 267 Great Tradition units do not share the rank, spacing, "
            "or line-position profile of the Rapanui formulas or of the words, beyond the "
            "shuffle nulls. Mamari and the Great Tradition do not repeat the creation chant's "
            "two-frame skeleton, and glyph 076 does not supply that skeleton there. Gv6's "
            "genealogy handoff remains a sign pattern on that one line and is not found as a "
            "formula in the chant corpus or among the repeated units on H, P, and Q."
        )
        return {"verdict_code": "no_match", "verdict": text}
    parts: list[str] = []
    if not formula:
        parts.append(
            "The formula profiles do not match. No sign-unit family is closer to a Rapanui "
            "formula family, or to the words, than both shuffles allow, and the Zipf slopes "
            "stay outside the pre-registered gap."
        )
    else:
        parts.append("A formula-profile or Zipf or frame-rate test cleared its bar.")
    if not genealogy_hit:
        parts.append(
            "Gv6's genealogy handoff is real on that one line and does not line up with a "
            "genealogical formula in the chant corpus or with the repeated units on H, P, and Q."
        )
    else:
        parts.append("A handoff chain of Gv6's length lined up.")
    if not chant_tile and not elided:
        parts.append(
            "Mamari has no glyph 076 and no two-frame tile. The Great Tradition units do not "
            "have that tile either. Fischer's elided triad is not distinguished from a shuffle."
        )
    if chant_tile:
        parts.append("A line tiled two delimiters the way the chant tiles its two frames. That is not a reading.")
    if elided:
        parts.append("A cut into threes had one slot more constant than its shuffle. That names no sign.")
    if spacing:
        joined = ", ".join(spacing)
        parts.append(
            f"A gap histogram is closer to the chant's verse gaps than its own shuffle on {joined}. "
            "The chant's gaps peak at 3 and 4 words. The sign gaps that clear the bar also peak on "
            "short distances. Track 4 already found this for Staff glyph 076 and did not treat it "
            "as a reading. The same limit holds here. Where the most frequent sign is 076, the "
            "second row repeats the first test. No sign is given the copula."
        )
    code = "spacing_only" if spacing and not (formula or chant_tile or elided or genealogy_hit) else "match"
    return {"verdict_code": code, "verdict": " ".join(parts)}


def run_round4_trackb(provider: MockProvider | None = None) -> dict[str, Any]:
    """Run the pre-registered comparisons and write the JSON and the note."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Round 4 Track B accepts MockProvider only")
    sign_pack = _load_sign_lines()
    language = _load_language()
    chant = _chant_block(language["lines"], language["meta"])
    matches = _run_matches(sign_pack["lines"], sign_pack["families"], language["lines"])
    skeleton = _run_skeleton(chant, sign_pack["lines"])
    genealogy = _run_genealogy(sign_pack, language["lines"])
    verdict = _verdict(matches, skeleton, genealogy)
    chant_public = {key: value for key, value in chant.items() if key != "gap_counter"}
    result = {
        "track": "round4b",
        "reading": None,
        "provider": "MockProvider",
        "provider_calls": len(provider.get_call_history()),
        "segmenter": sign_pack["segmenter"],
        "sources": list(SOURCES),
        "preregistration": {
            "formula_width": FORMULA_WIDTH,
            "formula_min_count": FORMULA_MIN_COUNT,
            "min_family": MIN_FAMILY,
            "zipf_slope_tolerance": ZIPF_SLOPE_TOLERANCE,
            "adopt_fraction": ADOPT_FRACTION,
            "null_trials": NULL_TRIALS,
            "sign_null_seed": SIGN_NULL_SEED,
            "language_null_seed": LANGUAGE_NULL_SEED,
            "skeleton_trials": SKELETON_TRIALS,
            "skeleton_seed": SKELETON_SEED,
            "handoff_trials": HANDOFF_TRIALS,
            "handoff_seed": HANDOFF_SEED,
            "skeleton_min_cycles": SKELETON_MIN_CYCLES,
            "skeleton_ttr_min": SKELETON_TTR_MIN,
            "handoff_min_links": HANDOFF_MIN_LINKS,
            "child_ttr_min": CHILD_TTR_MIN,
            "primary_pairs": [list(pair) for pair in PRIMARY_PAIRS],
            "skeleton_sides": list(SKELETON_SIDES),
        },
        "signs": {
            "segmenter": sign_pack["segmenter"],
            "types": len(sign_pack["families"]["all_recurring"]),
            "monosign": len(sign_pack["families"]["monosign"]),
            "multisign": len(sign_pack["families"]["multisign"]),
            "multi_tablet_types": sign_pack["multi_tablet_types"],
            "lines": len(sign_pack["lines"]),
            "top": sign_pack["catalog"][:12],
            "mdl_rounds": sign_pack["rounds"],
        },
        "language": {
            "rejected": language["rejected"],
            "formula_types": language["formula_types"],
            "lines": len(language["lines"]),
            "top_formulas": language["top_formulas"],
        },
        "chant": chant_public,
        "matches": matches,
        "skeleton": skeleton,
        "genealogy": genealogy,
        **verdict,
    }
    cleaned = _round(result)
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(cleaned, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    DOC_PATH.write_text(render_markdown(cleaned), encoding="utf-8")
    return cleaned


if __name__ == "__main__":
    run_round4_trackb(MockProvider())
