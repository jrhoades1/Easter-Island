"""Round 4 Track E: test published sign-sound values. Do not invent any.

A value is scored only when a named author stated it. Sets that argue the
script is syllabic, or that name a passage, but do not publish a sign-to-sound
list, are recorded and not filled in. ``MockProvider`` is accepted and never
called. Nothing here is adopted as a reading unless the pre-registered gate
says so.
"""

from __future__ import annotations

import json
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import permutations
from pathlib import Path
from typing import Any, Iterable

from agents.base.providers import MockProvider
from decipherment.old_rapanui import (
    cv_syllables_mapped,
    lexicon_headwords,
    primary_running_lines,
)
from decipherment.round2_trackb import LineText, is_calendar_stem, load_lines

REPO_ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = REPO_ROOT / "data" / "decipherment" / "round4e_expert_values.json"
DOC_PATH = REPO_ROOT / "docs" / "round4e_expert_values.md"

# The gate and the null sizes were fixed before any score was read.
ADOPT_FRACTION = 0.05
WINDOW_LENGTHS = (2, 3, 4)
FORMULA_WORDS = (2, 3, 4)
# Fischer's phallus phrase is five words. The draw needs that width.
# Five-word strings are not formula hits.
PHRASE_DRAW_WORDS = (2, 3, 4, 5)
RANDOM_TRIALS = 500
RANDOM_SEED = 41
FREQUENT_ALTERNATIVES = 30
GREAT_TRADITION = frozenset({"H", "P", "Q"})
# Confirmatory slice for the 200 = tangata retest. Gv6 is on tablet G, so it
# is outside this slice. The split is alphabetical, not chosen from hit counts.
HOLDOUT_TABLETS = frozenset("HIJKLMNOPQRSTUV")

PROTOCOL = {
    "id": "round4e_expert_values",
    "fixed_before_scores": True,
    "provider": "MockProvider",
    "windows": (
        "On one Barthel line, every span of 2, 3, or 4 stems in which every "
        "stem has a value in the map. A stem with no value ends the span. "
        "Overlapping spans are each counted."
    ),
    "word_hit": (
        "The syllables of the span are exactly one attested word of two or "
        "more syllables. Attested words are mapped (C)V shapes from the Round 3 "
        "lexicon and from the primary running text."
    ),
    "formula_hit": (
        "The syllables of the span are exactly the pronunciation of one "
        "contiguous sequence of 2, 3, or 4 words on one primary running-text "
        "line. Free segmentation is not allowed."
    ),
    "primary_score": (
        "The number of spans that are a word hit or a formula hit. A span "
        "counts once."
    ),
    "primary_lines": "Vendored Barthel tablets A–V, every line.",
    "descriptive_slices": (
        "Calendar Ca6 from stem 24 through Ca8 and the first two stems of Ca9; "
        "Gv6; tablets H, P, and Q. Slice counts are reported and are not "
        "separate tests."
    ),
    "null_a": (
        "Shuffled assignment. Two or more values are reassigned to the same "
        "signs in every order. One value has nothing to permute, so that value "
        "is reassigned to each of the 30 most frequent other stems on the same "
        "lines (tie broken by the sign id). p = (1 + alternatives at least as "
        "high) / (1 + alternatives)."
    ),
    "null_b": (
        "Random values of the same size and the same kind, 500 draws, seed 41. "
        "A syllable is drawn from attested syllable types. A word is drawn from "
        "attested words with the same syllable count. A phrase is drawn from "
        "attested running-text sequences with the same number of words. The "
        "published syllable string is left out of its own draw. Draws that "
        "repeat a syllable string inside one map are retried. Word and phrase "
        "lists are sorted before the draw, so seed 41 names one sequence."
    ),
    "p_value": "Fraction of null trials whose primary score is at least the observed score.",
    "multiple_comparison": (
        "Holm on the worse of the two null p-values, across every scored set "
        "including the tangata retest. A set is not adopted unless the observed "
        "score is above zero, both uncorrected p-values are at or under 0.05, "
        "and the Holm-adjusted worse p-value is at or under 0.05."
    ),
    "permutation_floor": (
        "With k distinct values there are k! assignments. If 1/k! is above "
        "0.05, the shuffle null cannot clear the gate. That limit is part of "
        "the test, not a reason to add trials after the fact."
    ),
    "empty_sets": (
        "A published argument that names no sign-to-sound pair is not given "
        "invented values and is not entered in the Holm family."
    ),
    "tangata_retest": (
        "Hypothesis, not a new proposal: sign 200 reads as the word tangata. "
        "Scored only on tablets H–V. Tablets A–G, which include the Gv6 "
        "genealogy, are not in the confirmatory count. The same two nulls are "
        "used. This hypothesis was already looked at on the pooled corpus in "
        "Round 3, so the hold-out is a confirmation slice, not an untouched sample."
    ),
    "adopt_fraction": ADOPT_FRACTION,
    "random_trials": RANDOM_TRIALS,
    "random_seed": RANDOM_SEED,
}


@dataclass(frozen=True)
class Value:
    """One cited sound. ``words`` are the citation spellings, in order."""

    sign: str
    words: tuple[str, ...]
    syllables: tuple[str, ...]
    citation: str
    status: str

    @property
    def kind(self) -> str:
        if len(self.words) > 1:
            return "phrase"
        if len(self.syllables) == 1:
            return "syllable"
        return "word"


@dataclass(frozen=True)
class ProposalSet:
    set_id: str
    author: str
    citation: str
    scored: bool
    summary: str
    values: tuple[Value, ...] = ()
    not_scored: tuple[dict[str, str], ...] = ()


def _syllables(words: Iterable[str]) -> tuple[str, ...]:
    syllables: list[str] = []
    for word in words:
        parsed = cv_syllables_mapped(word)
        if not parsed:
            raise ValueError(f"{word!r} is not a mapped (C)V value")
        syllables.extend(parsed)
    return tuple(syllables)


def _value(sign: str, words: tuple[str, ...], citation: str, status: str) -> Value:
    return Value(sign, words, _syllables(words), citation, status)


def proposal_sets() -> tuple[ProposalSet, ...]:
    """Published sets. Spellings are the authors' words, not a new reading."""
    jso = (
        "Davletshin 2012, Journal de la Société des Océanistes "
        "(https://journals.openedition.org/jso/6658)."
    )
    jps = (
        "Davletshin 2012, Journal of the Polynesian Society 121(3): 243–274, "
        "Numerals and phonetic complements in the Kohau rongorongo script."
    )
    fischer = (
        "Fischer 1995, Journal of the Polynesian Society 104: 303–321; "
        "the same sign values are restated in Fischer's further cosmogonic-text note."
    )
    return (
        ProposalSet(
            "davletshin_2012_names",
            "Davletshin 2012",
            jso,
            True,
            "Three sound values he states. He does not settle sign 200.",
            (
                _value("076", ("ko",), jso + " TB076 is (ko), the focus marker.", "proposed"),
                _value(
                    "021",
                    ("'a",),
                    jso + " If the ariki reading is right, TB021 spells ('a).",
                    "tentative",
                ),
                _value(
                    "530",
                    ("ariki",),
                    jso + " Tentative logogram ('ARIKI) for TB530.",
                    "tentative",
                ),
            ),
            (
                {
                    "sign": "200",
                    "status": "declined",
                    "note": (
                        "He considers a syllabic (te), so that 076-200 would be ko te, "
                        "and says he will not draw a conclusion about TB200."
                    ),
                },
            ),
        ),
        ProposalSet(
            "davletshin_2012_numerals",
            "Davletshin 2012",
            jps,
            True,
            "The crescent of the Mamari passage is the word tahi 'one'.",
            (
                _value(
                    "040",
                    ("tahi",),
                    jps
                    + " The Crescent in Ca6–Ca9, stemmed 040 in this corpus, reads tahi / e-tahi.",
                    "proposed",
                ),
            ),
            (
                {
                    "sign": "standing-man",
                    "status": "unresolved",
                    "note": (
                        "The Standing Man phonetic complement is hi or i. He does not choose, "
                        "so neither syllable is scored."
                    ),
                },
                {
                    "sign": "falling-squares",
                    "status": "unresolved",
                    "note": "A possible ru complement is one of three explanations he does not decide.",
                },
            ),
        ),
        ProposalSet(
            "davletshin_2022_cross_readings",
            "Davletshin 2022",
            "Davletshin 2022, Waka Kuaka 131(2): 185–220.",
            False,
            (
                "The abstract says twenty provisional values, eleven of them checked by "
                "cross-reading (seven logograms, four syllables). The sign-by-sign table "
                "was not in an open copy retrieved here, and it was not reconstructed."
            ),
        ),
        ProposalSet(
            "pozdniakov_pozdniakov_2007",
            "Pozdniakov and Pozdniakov 2007",
            (
                "Pozdniakov and Pozdniakov 2007, Forum for Anthropology and Culture 3. "
                "They reduce the inventory to about 52 signs and argue that the script "
                "is mostly syllabic. They do not publish a sign-to-syllable map."
            ),
            False,
            "No sign-sound pairs to apply. A map was not invented for them.",
        ),
        ProposalSet(
            "horley",
            "Horley",
            (
                "Horley 2005, Rapa Nui Journal 19(2), is an allograph paper already "
                "tested as an inventory. Later Horley papers used here discuss the "
                "calendar and the staff. No sign-sound list was found in the open text."
            ),
            False,
            "No sign-sound pairs to apply. A map was not invented.",
        ),
        ProposalSet(
            "guy_1990",
            "Guy 1990",
            "Guy 1990, Journal de la Société des Océanistes 91(2): 135–149.",
            False,
            (
                "Guy says some adjunct glyphs on the Mamari crescents may be syllabic "
                "rebuses for night names. The open text retrieved from Persée does not "
                "include the itemized list, so those values were not reconstructed."
            ),
        ),
        ProposalSet(
            "fischer_1995",
            "Fischer 1995",
            fischer,
            True,
            "Word and phrase values from the Santiago Staff example 606.76 700 8.",
            (
                _value("600", ("manu",), fischer + " Glyph 600 is manu 'bird'.", "tentative"),
                _value(
                    "606",
                    ("manu", "mau"),
                    fischer + " 606 is manu with the hand read mau.",
                    "tentative",
                ),
                _value("700", ("ika",), fischer + " Glyph 700 is ika 'fish'.", "tentative"),
                _value("008", ("ra'a",), fischer + " Glyph 8 is ra'a 'sun'.", "tentative"),
                _value(
                    "076",
                    ("ki", "ai", "ki", "roto", "ki"),
                    fischer + " The phallus in the triad is the phrase ki 'ai ki roto ki.",
                    "tentative",
                ),
            ),
        ),
        ProposalSet(
            "barthel_1958",
            "Barthel 1958",
            "Barthel 1958, Grundlagen zur Entzifferung der Osterinselschrift.",
            False,
            (
                "The retrievable Barthel claim used in this repository is that Ca6–Ca9 "
                "is a lunar calendar, including a full-moon figure. That is a content "
                "claim, not a sign-sound table, and it was not turned into syllables."
            ),
        ),
    )


def tangata_hypothesis() -> Value:
    """The Round 3 borderline lead. Labeled hypothesis. Not Davletshin's conclusion."""
    return _value(
        "200",
        ("tangata",),
        (
            "HYPOTHESIS. Round 3 Track C map H1 read sign 200 as Thomson's word "
            "tangata. Davletshin 2012 does not adopt a sound for TB200. "
            "Butinov and Knorozov read the sign as a title or as ko, not as this word."
        ),
        "hypothesis",
    )


@dataclass
class Language:
    words: frozenset[tuple[str, ...]]
    formulas: frozenset[tuple[str, ...]]
    syllables: tuple[str, ...]
    words_by_length: dict[int, tuple[tuple[str, ...], ...]]
    phrases_by_count: dict[int, tuple[tuple[str, ...], ...]]


def _add_sequence(
    buffer: list[tuple[str, ...]],
    formulas: set[tuple[str, ...]],
    phrases: dict[int, set[tuple[str, ...]]],
) -> None:
    if not buffer:
        return
    for width in PHRASE_DRAW_WORDS:
        if len(buffer) < width:
            continue
        for start in range(len(buffer) - width + 1):
            flat = tuple(syllable for word in buffer[start : start + width] for syllable in word)
            phrases[width].add(flat)
            if width in FORMULA_WORDS:
                formulas.add(flat)


def build_language() -> Language:
    """Attested words and short formulas from the Round 3 corpus."""
    words: set[tuple[str, ...]] = set()
    formulas: set[tuple[str, ...]] = set()
    syllable_types: set[str] = set()
    phrases: dict[int, set[tuple[str, ...]]] = {width: set() for width in PHRASE_DRAW_WORDS}

    def take(word: str) -> tuple[str, ...] | None:
        parsed = cv_syllables_mapped(word)
        if not parsed:
            return None
        words.add(parsed)
        syllable_types.update(parsed)
        return parsed

    for row in primary_running_lines():
        buffer: list[tuple[str, ...]] = []
        for word in row.words:
            parsed = take(word)
            if parsed is None:
                _add_sequence(buffer, formulas, phrases)
                buffer = []
                continue
            buffer.append(parsed)
        _add_sequence(buffer, formulas, phrases)
    for item in lexicon_headwords():
        take(item.word)

    by_length: dict[int, list[tuple[str, ...]]] = defaultdict(list)
    for shape in sorted(words):
        if len(shape) >= 2:
            by_length[len(shape)].append(shape)
    return Language(
        words=frozenset(shape for shape in words if len(shape) >= 2),
        formulas=frozenset(formulas),
        syllables=tuple(sorted(syllable_types)),
        words_by_length={key: tuple(value) for key, value in by_length.items()},
        phrases_by_count={key: tuple(sorted(value)) for key, value in phrases.items()},
    )


@dataclass(frozen=True)
class Span:
    line_id: str
    signs: tuple[str, ...]
    calendar: bool
    gv6: bool
    great_tradition: bool
    holdout: bool


def _calendar_span(line: LineText, start: int, width: int) -> bool:
    return all(is_calendar_stem(line, start + offset) for offset in range(width))


def collect_spans(lines: tuple[LineText, ...], signs: frozenset[str]) -> tuple[Span, ...]:
    spans: list[Span] = []
    for line in lines:
        flat = line.flat
        tablet = line.tablet
        for width in WINDOW_LENGTHS:
            if len(flat) < width:
                continue
            for start in range(len(flat) - width + 1):
                chunk = flat[start : start + width]
                if any(sign not in signs for sign in chunk):
                    continue
                spans.append(
                    Span(
                        line.line_id,
                        chunk,
                        _calendar_span(line, start, width),
                        line.side == "Gv" and line.number == 6,
                        tablet in GREAT_TRADITION,
                        tablet in HOLDOUT_TABLETS,
                    )
                )
    return tuple(spans)


def _read(signs: tuple[str, ...], mapping: dict[str, tuple[str, ...]]) -> tuple[str, ...]:
    return tuple(syllable for sign in signs for syllable in mapping[sign])


def score_spans(
    spans: tuple[Span, ...],
    mapping: dict[str, tuple[str, ...]],
    language: Language,
    *,
    keep: str | None = None,
) -> dict[str, Any]:
    """Primary score, the two components, and the descriptive slices."""
    word_hits = 0
    formula_hits = 0
    primary = 0
    slices = {name: 0 for name in ("calendar", "gv6", "great_tradition", "holdout", "corpus")}
    examples: list[dict[str, str]] = []
    for span in spans:
        if keep == "holdout" and not span.holdout:
            continue
        if keep == "explore" and span.holdout:
            continue
        syllables = _read(span.signs, mapping)
        word = syllables in language.words
        formula = syllables in language.formulas
        if not word and not formula:
            continue
        if keep is None or (keep == "holdout" and span.holdout) or (keep == "explore" and not span.holdout):
            primary += 1
            word_hits += int(word)
            formula_hits += int(formula)
            slices["corpus"] += 1
            if span.calendar:
                slices["calendar"] += 1
            if span.gv6:
                slices["gv6"] += 1
            if span.great_tradition:
                slices["great_tradition"] += 1
            if span.holdout:
                slices["holdout"] += 1
            if len(examples) < 12:
                kind = "word" if word and not formula else "formula" if formula and not word else "word+formula"
                examples.append(
                    {
                        "line": span.line_id,
                        "signs": " ".join(span.signs),
                        "syllables": "-".join(syllables),
                        "kind": kind,
                    }
                )
    return {
        "primary": primary,
        "word_hits": word_hits,
        "formula_hits": formula_hits,
        "slices": slices,
        "examples": examples,
        "spans": len(spans) if keep is None else sum(
            1 for span in spans if (span.holdout if keep == "holdout" else not span.holdout)
        ),
    }


def _mapping(values: tuple[Value, ...]) -> dict[str, tuple[str, ...]]:
    return {value.sign: value.syllables for value in values}


def _worse_gate(observed: int, shuffle_p: float, random_p: float) -> bool:
    if observed <= 0:
        return False
    return shuffle_p <= ADOPT_FRACTION and random_p <= ADOPT_FRACTION


def holm(p_values: list[tuple[str, float]]) -> dict[str, float]:
    """Holm step-down. Adjusted values stay in the original order's names."""
    count = len(p_values)
    ordered = sorted(p_values, key=lambda item: (item[1], item[0]))
    adjusted: dict[str, float] = {}
    running = 0.0
    for index, (name, raw) in enumerate(ordered):
        running = max(running, min(1.0, (count - index) * raw))
        adjusted[name] = running
    return adjusted


def _draw_replacement(
    value: Value,
    language: Language,
    rng: random.Random,
    banned: frozenset[tuple[str, ...]],
) -> tuple[str, ...] | None:
    if value.kind == "syllable":
        pool = [item for item in language.syllables if (item,) not in banned]
        if not pool:
            return None
        return (rng.choice(pool),)
    if value.kind == "word":
        pool = [
            item
            for item in language.words_by_length.get(len(value.syllables), ())
            if item not in banned
        ]
        if not pool:
            return None
        return rng.choice(pool)
    width = len(value.words)
    pool = [item for item in language.phrases_by_count.get(width, ()) if item not in banned]
    if not pool:
        return None
    return rng.choice(pool)


def random_scores(
    spans: tuple[Span, ...],
    values: tuple[Value, ...],
    language: Language,
    *,
    keep: str | None,
    seed: int,
) -> list[int]:
    """Primary scores of random value sets. Failed draws are omitted."""
    rng = random.Random(seed)
    scores: list[int] = []
    for _trial in range(RANDOM_TRIALS):
        banned: set[tuple[str, ...]] = set()
        mapping: dict[str, tuple[str, ...]] = {}
        failed = False
        for value in values:
            drawn = None
            for _attempt in range(40):
                candidate = _draw_replacement(value, language, rng, frozenset(banned | {value.syllables}))
                if candidate is None:
                    failed = True
                    break
                if candidate in banned:
                    continue
                drawn = candidate
                break
            if drawn is None:
                failed = True
                break
            banned.add(drawn)
            mapping[value.sign] = drawn
        if failed:
            continue
        scores.append(score_spans(spans, mapping, language, keep=keep)["primary"])
    return scores


def _p_from_scores(observed: int, scores: list[int]) -> dict[str, int | float]:
    trials = len(scores)
    ge = sum(1 for score in scores if score >= observed)
    return {
        "observed": observed,
        "ge": ge,
        "trials": trials,
        "p": (ge / trials) if trials else 1.0,
    }


def _permute_scores(
    spans: tuple[Span, ...],
    values: tuple[Value, ...],
    language: Language,
    *,
    keep: str | None,
) -> list[int]:
    signs = [value.sign for value in values]
    syllables = [value.syllables for value in values]
    scores: list[int] = []
    for order in permutations(syllables):
        mapping = dict(zip(signs, order))
        scores.append(score_spans(spans, mapping, language, keep=keep)["primary"])
    return scores


def _frequent_other_signs(lines: tuple[LineText, ...], used: frozenset[str], holdout_only: bool) -> tuple[str, ...]:
    counts: Counter[str] = Counter()
    for line in lines:
        if holdout_only and line.tablet not in HOLDOUT_TABLETS:
            continue
        for sign in line.flat:
            if sign not in used and sign != "000":
                counts[sign] += 1
    ranked = sorted(counts, key=lambda sign: (-counts[sign], sign))
    return tuple(ranked[:FREQUENT_ALTERNATIVES])


def _reassign_scores(
    lines: tuple[LineText, ...],
    language: Language,
    syllable: tuple[str, ...],
    alternatives: tuple[str, ...],
    *,
    keep: str | None,
) -> list[int]:
    scores: list[int] = []
    for sign in alternatives:
        spans = collect_spans(lines, frozenset({sign}))
        scores.append(score_spans(spans, {sign: syllable}, language, keep=keep)["primary"])
    return scores


def _null_block(observed: int, scores: list[int], method: str) -> dict[str, Any]:
    """Permutation and random draws use ge/trials.

    Reassignment does not include the real sign in ``scores``. The protocol
    puts that sign back: p = (1 + alternatives at least as high) / (1 + alternatives).
    """
    if method.startswith("reassign"):
        ge = 1 + sum(1 for score in scores if score >= observed)
        trials = 1 + len(scores)
        p = ge / trials if trials else 1.0
        block: dict[str, Any] = {"observed": observed, "ge": ge, "trials": trials, "p": p}
    else:
        block = _p_from_scores(observed, scores)
    block["method"] = method
    block["clears_uncorrected"] = bool(observed > 0 and block["p"] <= ADOPT_FRACTION)
    return block


def _score_set(
    item: ProposalSet,
    lines: tuple[LineText, ...],
    language: Language,
) -> dict[str, Any]:
    mapping = _mapping(item.values)
    spans = collect_spans(lines, frozenset(mapping))
    observed = score_spans(spans, mapping, language, keep=None)
    if len(item.values) == 1:
        alternatives = _frequent_other_signs(lines, frozenset(mapping), False)
        shuffle_scores = _reassign_scores(
            lines,
            language,
            item.values[0].syllables,
            alternatives,
            keep=None,
        )
        shuffle = _null_block(observed["primary"], shuffle_scores, "reassign_to_frequent_signs")
        shuffle["alternatives"] = list(alternatives)
    else:
        shuffle_scores = _permute_scores(spans, item.values, language, keep=None)
        shuffle = _null_block(observed["primary"], shuffle_scores, "permute_values")
    random_list = random_scores(spans, item.values, language, keep=None, seed=RANDOM_SEED)
    random_null = _null_block(observed["primary"], random_list, "random_values")
    worse = max(float(shuffle["p"]), float(random_null["p"]))
    return {
        "set_id": item.set_id,
        "author": item.author,
        "citation": item.citation,
        "summary": item.summary,
        "scored": True,
        "values": [
            {
                "sign": value.sign,
                "words": list(value.words),
                "syllables": list(value.syllables),
                "kind": value.kind,
                "status": value.status,
                "citation": value.citation,
            }
            for value in item.values
        ],
        "not_scored": [dict(note) for note in item.not_scored],
        "observed": observed,
        "shuffle": shuffle,
        "random": random_null,
        "worse_p": worse,
        "adopted": False,
    }


def _score_tangata(lines: tuple[LineText, ...], language: Language) -> dict[str, Any]:
    value = tangata_hypothesis()
    mapping = {value.sign: value.syllables}
    spans = collect_spans(lines, frozenset(mapping))
    confirmatory = score_spans(spans, mapping, language, keep="holdout")
    explore = score_spans(spans, mapping, language, keep="explore")
    alternatives = _frequent_other_signs(lines, frozenset({"200"}), True)
    shuffle_scores = _reassign_scores(
        lines,
        language,
        value.syllables,
        alternatives,
        keep="holdout",
    )
    shuffle = _null_block(confirmatory["primary"], shuffle_scores, "reassign_on_holdout")
    shuffle["alternatives"] = list(alternatives)
    random_list = random_scores(
        spans,
        (value,),
        language,
        keep="holdout",
        seed=RANDOM_SEED,
    )
    random_null = _null_block(confirmatory["primary"], random_list, "random_words_on_200")
    return {
        "set_id": "hypothesis_200_tangata",
        "label": "HYPOTHESIS",
        "citation": value.citation,
        "sign": "200",
        "words": ["tangata"],
        "syllables": list(value.syllables),
        "holdout_tablets": "".join(sorted(HOLDOUT_TABLETS)),
        "confirmatory": confirmatory,
        "explore_not_used_for_p": explore,
        "shuffle": shuffle,
        "random": random_null,
        "worse_p": max(float(shuffle["p"]), float(random_null["p"])),
        "adopted": False,
        "caveat": PROTOCOL["tangata_retest"],
    }


def _unscored_row(item: ProposalSet) -> dict[str, Any]:
    return {
        "set_id": item.set_id,
        "author": item.author,
        "citation": item.citation,
        "summary": item.summary,
        "scored": False,
        "values": [],
        "reason": "No published sign-sound list was retrieved. None was invented.",
    }


def run_round4_tracke(provider: MockProvider | None = None) -> dict[str, Any]:
    """Apply the pre-registered protocol. The provider is never called."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("MockProvider only")
    lines = load_lines()
    language = build_language()
    scored: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    for item in proposal_sets():
        if item.scored:
            scored.append(_score_set(item, lines, language))
        else:
            skipped.append(_unscored_row(item))
    tangata = _score_tangata(lines, language)
    family = [(row["set_id"], float(row["worse_p"])) for row in scored]
    family.append(("hypothesis_200_tangata", float(tangata["worse_p"])))
    adjusted = holm(family)
    adopted: list[str] = []
    for row in scored:
        row["holm_p"] = adjusted[row["set_id"]]
        row["adopted"] = bool(
            _worse_gate(row["observed"]["primary"], row["shuffle"]["p"], row["random"]["p"])
            and row["holm_p"] <= ADOPT_FRACTION
        )
        if row["adopted"]:
            adopted.append(row["set_id"])
    tangata["holm_p"] = adjusted["hypothesis_200_tangata"]
    tangata["adopted"] = bool(
        _worse_gate(tangata["confirmatory"]["primary"], tangata["shuffle"]["p"], tangata["random"]["p"])
        and tangata["holm_p"] <= ADOPT_FRACTION
    )
    if tangata["adopted"]:
        adopted.append(tangata["set_id"])
    return {
        "provider": "MockProvider",
        "provider_calls": 0,
        "reading": None,
        "adopted": adopted,
        "protocol": PROTOCOL,
        "language": {
            "word_shapes": len(language.words),
            "formula_shapes": len(language.formulas),
            "syllable_types": len(language.syllables),
        },
        "lines": len(lines),
        "scored": scored,
        "not_scored": skipped,
        "tangata": tangata,
        "holm": adjusted,
    }


def _pct(p: float) -> str:
    return f"{p:.3f}"


def _hits(block: dict[str, Any]) -> str:
    observed = block["observed"]
    return (
        f"{observed['primary']} spans "
        f"({observed['word_hits']} word, {observed['formula_hits']} formula) "
        f"out of {observed['spans']} valued spans"
    )


def render_markdown(result: dict[str, Any]) -> str:
    """Plain-English report. Numbers come from the run."""
    lines = [
        "# Round 4, Track E — Do the published sound values spell Rapanui?",
        "",
        "This is a test of other people's proposals. It is not a decipherment.",
        "No new reading was made up. Where a scholar did not publish a list of",
        "sign-to-sound pairs, that list was left empty.",
        "",
        f"Provider: {result['provider']}. Provider calls: {result['provider_calls']}.",
        f"Adopted readings: {result['adopted'] or 'none'}. `reading` is {result['reading']}.",
        "",
        "## What was tested",
        "",
        "Each published value was laid onto the Barthel stems of tablets A–V.",
        "A span of two, three, or four signs counts only when every sign in it",
        "has a value. The span scores when those sounds are exactly one attested",
        "Rapanui word, or exactly a short phrase that already occurs in the old",
        "Rapanui sample (Thomson's chants, Metoro's recitations, and Routledge's",
        "timo line, plus the public-domain word lists for single words).",
        "",
        "Two comparisons were fixed before the scores were read:",
        "",
        "1. Shuffle the published values among the same signs.",
        "2. Replace them with random attested sounds of the same size, 500 times,",
        "   seed 41. The word and phrase lists are sorted first, so that seed",
        "   always draws the same sequence.",
        "",
        "A proposal would have to beat both, at 5 percent, and still beat them",
        "after a Holm correction across every scored proposal, including the",
        "tangata retest. Calendar lines Ca6–Ca9, the Gv6 genealogy, and the",
        "Great Tradition tablets H, P, and Q are counted inside that corpus and",
        "also printed on their own. Those extra counts are not extra chances to pass.",
        "",
        f"Attested word-shapes of two or more syllables: {result['language']['word_shapes']}.",
        f"Attested short phrases: {result['language']['formula_shapes']}.",
        f"Syllable types available to the random draw: {result['language']['syllable_types']}.",
        "",
        "## Sets with no sound list",
        "",
        "These were looked up and not filled in.",
        "",
    ]
    for row in result["not_scored"]:
        lines.append(f"- **{row['author']}.** {row['summary']}")
    lines.extend(["", "## Scored proposals", ""])
    for row in result["scored"]:
        lines.append(f"### {row['author']}: {row['set_id']}")
        lines.append("")
        lines.append(row["summary"])
        lines.append("")
        lines.append("| Sign | Cited value | Kind | Status |")
        lines.append("| --- | --- | --- | --- |")
        for value in row["values"]:
            shown = " ".join(value["words"])
            lines.append(
                f"| `{value['sign']}` | {shown} ({'-'.join(value['syllables'])}) | {value['kind']} | {value['status']} |"
            )
        lines.append("")
        lines.append(f"Citation: {row['citation']}")
        lines.append("")
        observed = row["observed"]
        slices = observed["slices"]
        lines.append(f"Corpus: {_hits(row)}. Shuffle p = {_pct(row['shuffle']['p'])} ({row['shuffle']['ge']} of {row['shuffle']['trials']}, {row['shuffle']['method']}). Random p = {_pct(row['random']['p'])} ({row['random']['ge']} of {row['random']['trials']}). Holm-adjusted worse p = {_pct(row['holm_p'])}. Adopted: {row['adopted']}.")
        lines.append("")
        lines.append(
            "Inside that total, the calendar slice has "
            f"{slices['calendar']} hits, Gv6 has {slices['gv6']}, and the Great Tradition "
            f"(H, P, Q) has {slices['great_tradition']}."
        )
        if observed["spans"] and observed["primary"] == 0:
            lines.append(
                "Those signs do occur. Under this map their sounds are not an attested word "
                "or an attested short phrase, including on the calendar lines."
            )
        if observed["examples"]:
            lines.append("")
            lines.append("Examples of hits:")
            for example in observed["examples"]:
                lines.append(
                    f"- {example['line']}: `{example['signs']}` → {example['syllables']} ({example['kind']})"
                )
        if row["not_scored"]:
            lines.append("")
            for note in row["not_scored"]:
                lines.append(f"Not scored: {note['note']}")
        lines.append("")
    tangata = result["tangata"]
    conf = tangata["confirmatory"]
    lines.extend(
        [
            "## Retest: sign 200 as tangata",
            "",
            "This is a hypothesis, carried forward because Round 3 found a phrase",
            "score sitting on the 5 percent line and did not adopt it. Davletshin",
            "does not read sign 200 as tangata. The confirmatory count uses only",
            f"tablets {tangata['holdout_tablets']}. Tablet G, including the Gv6",
            "genealogy that suggested a 'man' sign, is not in that count.",
            "Tablets A–G were already in the earlier pooled look, so this slice",
            "is a check, not a fresh discovery.",
            "",
            f"Hold-out: {conf['primary']} spans ({conf['word_hits']} word, {conf['formula_hits']} formula) out of {conf['spans']} valued spans.",
            f"Shuffle p = {_pct(tangata['shuffle']['p'])} ({tangata['shuffle']['ge']} of {tangata['shuffle']['trials']}).",
            f"Random p = {_pct(tangata['random']['p'])} ({tangata['random']['ge']} of {tangata['random']['trials']}).",
            f"Holm-adjusted worse p = {_pct(tangata['holm_p'])}. Adopted: {tangata['adopted']}.",
            "",
            "The A–G count is printed so it can be seen, and it is not the p-value: "
            f"{tangata['explore_not_used_for_p']['primary']} spans.",
            "",
        ]
    )
    if conf["examples"]:
        lines.append("Hold-out examples:")
        lines.append("")
        for example in conf["examples"]:
            lines.append(
                f"- {example['line']}: `{example['signs']}` → {example['syllables']} ({example['kind']})"
            )
        lines.append("")
    lines.extend(
        [
            "## What this does not say",
            "",
            "Beating a shuffle would have meant these particular sounds, on these",
            "particular signs, spell real words more often than the same sounds",
            "swapped around. None of the scored sets is adopted. A miss does not",
            "prove the author wrong about a passage they were explaining. It means",
            "the values, applied as sounds across the corpus, do not spell the",
            "attested words and short phrases above the comparisons that were",
            "fixed in advance.",
            "",
            "The run uses MockProvider only. Provider calls: 0.",
            "",
        ]
    )
    return "\n".join(lines)


def render_json(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def write_outputs(result: dict[str, Any]) -> None:
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    DOC_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(render_json(result), encoding="utf-8")
    DOC_PATH.write_text(render_markdown(result), encoding="utf-8")
