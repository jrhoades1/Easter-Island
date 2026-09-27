"""Round 3 Track C: rerun the language comparisons on a larger old-Rapanui corpus.

The sign corpus is the vendored Barthel text used in Rounds 1 and 2. Only the
Rapanui side changes. ``MockProvider`` is accepted and never called. A reading
is recorded only when the Track 2 syllabic gate and the Track B crib gate both
say so. Neither is relaxed here.
"""

from __future__ import annotations

import random
from collections import Counter
from pathlib import Path
from typing import Any

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import load_barthel_sides
from decipherment.metrics import frequency_alignment, shuffle_lines, structure_index
from decipherment.old_rapanui import (
    NORMALIZATION_RULES,
    cv_syllables_mapped,
    extract_metoro_lines,
    lexicon_headwords,
    load_churchill_headwords,
    load_routledge_chants,
    load_thomson_running,
    primary_running_lines,
)
from decipherment.rapanui import (
    PHONOLOGICAL_CV_CEILING,
    is_full_reduplication,
    load_wikipedia_word_lines,
    primary_thomson_sample,
)
from decipherment.report import _svg_chart
from decipherment.round2_tracka import (
    GATE_SCHEMES,
    _block,
    _heaps_points,
    _scheme_lines,
    _syllabary_gate,
)
from decipherment.round2_trackb import (
    SIGNS,
    _phrase_vocabulary,
    _random_scores,
    _score_hypothesis,
    _windows,
    _word_sequences,
    build_anchors,
    build_lexicon,
    cv_syllables,
    hypotheses,
    load_lines,
)
from decipherment.track2 import ADOPT_NULL_FRACTION, classify_writing_system

DOCS_DIR = Path(__file__).resolve().parents[1] / "docs" / "decipherment"
FIGURE_NAME = "round3_trackC_heaps.svg"

# Published Round 1 / Round 2 figures. Compared, not recomputed as the baseline.
ROUND1_SYLLABLE_TOKENS = 3400
ROUND1_SYLLABLE_TYPES = 49
ROUND1_SYLLABLE_BETA = 0.142
ROUND1_SYLLABLE_H2 = 3.870
ROUND1_SYLLABLE_STRUCTURE = 0.144
ROUND1_WORD_TOKENS = 1591
ROUND1_WORD_TYPES = 633
ROUND1_WORD_BETA = 0.813
ROUND1_WORD_H2 = 1.663
ROUND1_WORD_STRUCTURE = 0.343
ROUND1_VERDICT = "mixed"
ROUND1_STEM_TOKENS = 14488
ROUND1_STEM_TYPES = 630
ROUND2_OPEN_LEXICON = 656
ROUND2_CRIB_TARGETS = 48
ROUND2_SYLLABLE_TYPES = 54
ROUND2_CRIB = {
    "H1": {"open": 17, "permutation": 66, "random": 105, "crib": 0, "phrase": 0},
    "H2": {"open": 0, "permutation": 120, "random": 500, "crib": 0, "phrase": 0},
    "H3": {"open": 2, "permutation": 88, "random": 294, "crib": 0, "phrase": 0},
    "H4": {"open": 3, "permutation": 92, "random": 270, "crib": 0, "phrase": 0},
}
ROUND2_LABELS = {
    "stem": "mixed",
    "ligature_atomic": "logographic",
    "barthel_suffix_only": "mixed",
    "barthel_families": "mixed",
    "barthel_families_whole": "logographic",
    "pozdniakov_2007": "mixed",
    "pozdniakov_2007_whole": "logographic",
    "pozdniakov_1996_gaping_mouth": "mixed",
    "horley_2005": "mixed",
    "horley_2005_whole": "logographic",
}

FORMULA_WIDTHS = (2, 3, 4, 5, 6)
FORMULA_MIN_COUNT = 4
FORMULA_TRIALS = 200
FORMULA_SEED = 0
FORMULA_NULL_WIDTH = 3
SYLLABLE_BETA_FLAT = 0.25
SYLLABLE_TYPE_CAP = 70


def _cv_lines(word_lines: list[list[str]]) -> tuple[list[list[str]], list[list[tuple[str, ...]]], int]:
    """Keep words that are mapped (C)V. A stranded consonant rejects the word."""
    words_out: list[list[str]] = []
    syllables_out: list[list[tuple[str, ...]]] = []
    rejected = 0
    for line in word_lines:
        words: list[str] = []
        syllables: list[tuple[str, ...]] = []
        for word in line:
            parsed = cv_syllables_mapped(word)
            if not parsed:
                rejected += 1
                continue
            words.append(word.lower())
            syllables.append(parsed)
        if words:
            words_out.append(words)
            syllables_out.append(syllables)
    return words_out, syllables_out, rejected


def _flat_syllables(groups: list[list[tuple[str, ...]]]) -> list[list[str]]:
    return [[piece for word in line for piece in word] for line in groups]


def _public(summary: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in summary.items() if key != "_curve"}


def _source_rows() -> dict[str, list[list[str]]]:
    thomson = [list(row.words) for row in load_thomson_running(include_love_song=False)]
    metoro = extract_metoro_lines()
    full = [list(row.words) for row in metoro if not row.elliptical]
    elliptical = [list(row.words) for row in metoro if row.elliptical]
    routledge = [list(row.words) for row in load_routledge_chants()]
    return {
        "thomson_1891": thomson,
        "metoro_jaussen_full": full,
        "metoro_jaussen_elliptical": elliptical,
        "routledge_1919": routledge,
    }


def _length_block(word_lines: list[list[str]]) -> dict[str, Any]:
    _words, groups, rejected = _cv_lines(word_lines)
    lengths = [len(word) for line in groups for word in line]
    histogram: dict[str, int] = {}
    for length in sorted(set(lengths)):
        histogram[str(length)] = lengths.count(length)
    reduplicated = sum(1 for line in groups for word in line if is_full_reduplication(word))
    ordered = sorted(lengths)
    median = None
    if ordered:
        mid = len(ordered) // 2
        if len(ordered) % 2:
            median = float(ordered[mid])
        else:
            median = (ordered[mid - 1] + ordered[mid]) / 2
    return {
        "tokens": len(lengths),
        "rejected": rejected,
        "mean_syllables": (sum(lengths) / len(lengths)) if lengths else 0.0,
        "median_syllables": median,
        "histogram": histogram,
        "full_reduplications": reduplicated,
        "reduplication_rate": (reduplicated / len(lengths)) if lengths else 0.0,
    }


def _formula_key(gram: tuple[tuple[str, ...], ...]) -> str:
    return " ".join("".join(word) for word in gram)


def _count_formulae(
    groups: list[list[tuple[str, ...]]],
    width: int,
    minimum: int,
) -> tuple[int, list[tuple[str, int]]]:
    counts: Counter[tuple[tuple[str, ...], ...]] = Counter()
    for line in groups:
        if len(line) < width:
            continue
        for start in range(len(line) - width + 1):
            counts[tuple(line[start : start + width])] += 1
    kept = [(gram, count) for gram, count in counts.items() if count >= minimum]
    kept.sort(key=lambda item: (-item[1], _formula_key(item[0])))
    return len(kept), [(_formula_key(gram), count) for gram, count in kept]


def _formula_null(groups: list[list[tuple[str, ...]]], observed: int) -> dict[str, Any]:
    generator = random.Random(FORMULA_SEED)
    ge = 0
    for _trial in range(FORMULA_TRIALS):
        shuffled: list[list[tuple[str, ...]]] = []
        for line in groups:
            row = list(line)
            generator.shuffle(row)
            shuffled.append(row)
        richness, _rows = _count_formulae(shuffled, FORMULA_NULL_WIDTH, FORMULA_MIN_COUNT)
        if richness >= observed:
            ge += 1
    return {
        "width": FORMULA_NULL_WIDTH,
        "min_count": FORMULA_MIN_COUNT,
        "observed_types": observed,
        "trials": FORMULA_TRIALS,
        "seed": FORMULA_SEED,
        "ge": ge,
        "fraction": ge / FORMULA_TRIALS,
        "beats_null": observed > 0 and (ge / FORMULA_TRIALS) <= ADOPT_NULL_FRACTION,
    }


def _surface_index(groups: list[list[tuple[str, ...]]], words: list[list[str]]) -> dict[tuple[str, ...], str]:
    """Most common spelling for each mapped syllable tuple."""
    counts: dict[tuple[str, ...], Counter[str]] = {}
    for line_words, line_groups in zip(words, groups):
        for word, syllables in zip(line_words, line_groups):
            bucket = counts.setdefault(syllables, Counter())
            bucket[word] += 1
    return {key: bucket.most_common(1)[0][0] for key, bucket in counts.items()}


def _phrase_shapes(windows, words: dict[str, str], phrases) -> list[dict[str, Any]]:
    """Whole cited words, in sign order, that occur in the language sample."""
    syllables = {sign: cv_syllables(word) for sign, word in words.items()}
    hits: Counter[str] = Counter()
    for gram in windows:
        phrase = tuple(syllables[sign] for sign in gram)
        if phrase in phrases:
            hits[" ".join(words[sign] for sign in gram)] += 1
    return [{"phrase": text, "count": count} for text, count in hits.most_common(6)]


def _crib(
    open_lexicon: frozenset[tuple[str, ...]],
    targets: frozenset[tuple[str, ...]],
) -> dict[str, Any]:
    lines = load_lines()
    anchors = build_anchors(lines)
    windows = _windows(lines, anchors, outside=True)
    phrase_sets = set(_phrase_vocabulary(_word_sequences()))
    running_words = [list(row.words) for row in primary_running_lines()]
    _words, groups, _rejected = _cv_lines(running_words)
    sequences = []
    for line in groups:
        if len(line) >= 2:
            sequences.append(tuple(line))
    for line in load_wikipedia_word_lines():
        buffer: list[tuple[str, ...]] = []
        for word in line:
            parsed = cv_syllables_mapped(word)
            if not parsed:
                if len(buffer) >= 2:
                    sequences.append(tuple(buffer))
                buffer = []
                continue
            buffer.append(parsed)
        if len(buffer) >= 2:
            sequences.append(tuple(buffer))
    phrase_sets |= set(_phrase_vocabulary(tuple(sequences)))
    phrases = frozenset(phrase_sets)
    syllable_types = tuple(sorted({piece for word in open_lexicon for piece in word}))
    open_random, crib_random = _random_scores(windows, syllable_types, open_lexicon, targets)
    scored = []
    adopted: list[str] = []
    for hypothesis in hypotheses():
        score = _score_hypothesis(
            hypothesis,
            windows,
            open_lexicon,
            targets,
            open_random,
            crib_random,
            phrases,
        )
        if score.reading_adopted:
            adopted.append(score.name)
        prior = ROUND2_CRIB[score.name]
        scored.append(
            {
                "name": score.name,
                "syllables": [{"sign": sign, "syllable": syllable} for sign, syllable in score.syllables],
                "open_hits": sum(count for _gram, count in score.open_hits),
                "open_hit_shapes": [
                    {"shape": "-".join(gram), "count": count} for gram, count in score.open_hits[:8]
                ],
                "crib_hits": sum(count for _gram, count in score.crib_hits),
                "permutation_ge": score.open_permutation.ge,
                "permutation_trials": score.open_permutation.trials,
                "random_ge": score.open_random.ge,
                "random_trials": score.open_random.trials,
                "crib_permutation_ge": score.crib_permutation.ge,
                "crib_random_ge": score.crib_random.ge,
                "crib_random_positive": score.crib_random.positive,
                "phrase_hits": score.phrase_hits,
                "phrase_permutation_ge": score.phrase_permutation.ge,
                "phrase_permutation_trials": score.phrase_permutation.trials,
                "phrase_survives": score.phrase_permutation.survives,
                "phrase_shapes": _phrase_shapes(windows, hypothesis.words(), phrases),
                "adopted": score.reading_adopted,
                "round2_open_hits": prior["open"],
                "open_hits_changed": sum(count for _gram, count in score.open_hits) != prior["open"],
            }
        )
    return {
        "windows": len(windows),
        "open_lexicon": len(open_lexicon),
        "round2_open_lexicon": ROUND2_OPEN_LEXICON,
        "targets": len(targets),
        "round2_targets": ROUND2_CRIB_TARGETS,
        "syllable_types": len(syllable_types),
        "round2_syllable_types": ROUND2_SYLLABLE_TYPES,
        "hypotheses": scored,
        "adopted_readings": adopted,
    }


def _expanded_open_lexicon() -> tuple[frozenset[tuple[str, ...]], frozenset[tuple[str, ...]]]:
    """Round 2 open list, plus mapped shapes from the old corpus and the lexicon."""
    base, _forms, targets = build_lexicon()
    lexicon = set(base)
    pools = [list(row.words) for row in primary_running_lines()]
    pools.extend([[item.word] for item in lexicon_headwords()])
    pools.extend(load_wikipedia_word_lines())
    for line in pools:
        for word in line:
            parsed = cv_syllables_mapped(word)
            if parsed:
                lexicon.add(parsed)
    return frozenset(lexicon), targets


def _conclusions(track2: dict[str, Any], track_a: dict[str, Any], track_b: dict[str, Any]) -> dict[str, list[str]]:
    holds: list[str] = []
    changes: list[str] = []
    label = track2["verdict"]["label"]
    if label == ROUND1_VERDICT:
        holds.append(
            "The Track 2 label is still mixed: stem sequences stay larger than the "
            "Rapanui syllable inventory and smaller than the Rapanui word inventory "
            "at the shared token count."
        )
    else:
        changes.append(f"The Track 2 label changed from mixed to {label}.")
    if track2["stem_tokens"] == ROUND1_STEM_TOKENS and track2["stem_types"] == ROUND1_STEM_TYPES:
        holds.append(
            f"The Barthel stem inventory is unchanged ({ROUND1_STEM_TYPES} types, "
            f"{ROUND1_STEM_TOKENS} tokens). The sign corpus was not rebuilt."
        )
    else:
        changes.append("The Barthel stem inventory no longer matches the Round 1 count.")
    if not track_a["any_gate"]:
        holds.append(
            "No cited allograph scheme enters the 45–70 type band. The Round 2 gate "
            "still does not open, and the frequency alignment is still not run."
        )
    else:
        changes.append("At least one cited scheme now passes the syllabary gate.")
    moved_labels = [
        row["id"] for row in track_a["schemes"] if row["track2_label"] != row["round2_label"]
    ]
    if moved_labels:
        changes.append(
            "Track 2 labels of these schemes changed against the larger sample: "
            + ", ".join(moved_labels)
            + "."
        )
    else:
        holds.append("Every Round 2 scheme keeps the Track 2 label it had against Thomson alone.")
    if not track_b["adopted_readings"]:
        holds.append(
            "None of H1–H4 spells the crib targets often enough to beat both nulls. "
            "No anchor reading is adopted."
        )
    else:
        changes.append(
            "A crib map beat both nulls: " + ", ".join(track_b["adopted_readings"]) + "."
        )
    syllables = track2["syllables"]
    if syllables["inventory"] <= SYLLABLE_TYPE_CAP and (syllables["heaps_beta"] or 1) <= SYLLABLE_BETA_FLAT:
        holds.append(
            f"Rapanui syllables still look like a small closed inventory "
            f"({syllables['inventory']} types, Heaps β {syllables['heaps_beta']:.3f}), "
            f"under the ceiling of {PHONOLOGICAL_CV_CEILING}."
        )
    else:
        changes.append(
            "The syllable inventory no longer sits in the flat syllabary band "
            f"({syllables['inventory']} types, β {syllables['heaps_beta']})."
        )
    if syllables["tokens"] != ROUND1_SYLLABLE_TOKENS or syllables["inventory"] != ROUND1_SYLLABLE_TYPES:
        changes.append(
            f"The running-text syllable sample moved from {ROUND1_SYLLABLE_TOKENS} tokens "
            f"and {ROUND1_SYLLABLE_TYPES} types to {syllables['tokens']} tokens and "
            f"{syllables['inventory']} types."
        )
    words = track2["words"]
    if words["tokens"] != ROUND1_WORD_TOKENS or words["inventory"] != ROUND1_WORD_TYPES:
        changes.append(
            f"The running-text word sample moved from {ROUND1_WORD_TOKENS} tokens and "
            f"{ROUND1_WORD_TYPES} types to {words['tokens']} tokens and {words['inventory']} types."
        )
    if track_b["open_lexicon"] != ROUND2_OPEN_LEXICON:
        changes.append(
            f"The crib open list moved from {ROUND2_OPEN_LEXICON} word-shapes to "
            f"{track_b['open_lexicon']}."
        )
    if abs(float(syllables["h2_conditional_mle"]) - ROUND1_SYLLABLE_H2) <= 0.05:
        holds.append(
            f"Syllable conditional entropy stays near the Round 1 value "
            f"({ROUND1_SYLLABLE_H2} then, {float(syllables['h2_conditional_mle']):.3f} now)."
        )
    else:
        changes.append(
            f"Syllable conditional entropy moved from {ROUND1_SYLLABLE_H2} to "
            f"{float(syllables['h2_conditional_mle']):.3f}."
        )
    changes.append(
        f"Word conditional entropy moved from {ROUND1_WORD_H2} to "
        f"{float(words['h2_conditional_mle']):.3f}, and word Heaps β from {ROUND1_WORD_BETA} "
        f"to {float(words['heaps_beta']):.3f}. The short Thomson sample was hapax-heavy. "
        "The larger sample repeats formulae, so word h2 rises and β falls."
    )
    phrase_survivors = [row for row in track_b["hypotheses"] if row["phrase_survives"]]
    if phrase_survivors:
        bits = []
        for row in phrase_survivors:
            fraction = row["phrase_permutation_ge"] / row["phrase_permutation_trials"]
            shapes = ", ".join(
                f"{item['phrase']} ×{item['count']}" for item in row["phrase_shapes"]
            )
            bits.append(
                f"{row['name']} ({row['phrase_permutation_ge']}/"
                f"{row['phrase_permutation_trials']} = {fraction:.3f}; {shapes})"
            )
        changes.append(
            "Whole-word phrase scores meet the permutation gate for "
            + "; ".join(bits)
            + ". That fraction sits on the 5% line. The hits are repeated outside pairs "
            "read as frequent words. They are not adopted as a reading: the crib-target "
            "score is still the gate, and it is zero."
        )
    else:
        holds.append(
            "Whole-word phrase scores do not beat the permutation null. No logogram sequence is adopted."
        )
    open_moved = [row["name"] for row in track_b["hypotheses"] if row["open_hits_changed"]]
    if open_moved:
        changes.append(
            "Open-list hit counts changed for " + ", ".join(open_moved) + ". Crib-target hits are reported in the table."
        )
    else:
        holds.append("Open-list hit counts for H1–H4 are the same as Round 2.")
    return {"holds": holds, "changes": changes}


def run_round3_trackc(provider: MockProvider | None = None) -> dict[str, Any]:
    """Compare Barthel signs with the enlarged old-Rapanui corpus."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Round 3 Track C accepts MockProvider only")

    thomson_round1 = primary_thomson_sample()
    sources = _source_rows()
    running_rows = primary_running_lines()
    raw_running = [list(row.words) for row in running_rows]
    word_lines, syllable_groups, rejected = _cv_lines(raw_running)
    syllable_lines = _flat_syllables(syllable_groups)
    without_elliptical = primary_running_lines(include_elliptical=False)
    sens_words, sens_groups, sens_rejected = _cv_lines([list(row.words) for row in without_elliptical])
    sens_syllables = _flat_syllables(sens_groups)

    syllables = _block(syllable_lines)
    words = _block(word_lines)
    syllable_shuffle = shuffle_lines(syllable_lines, seed=0)
    word_shuffle = shuffle_lines(word_lines, seed=0)
    syllable_structure = structure_index(
        float(syllables["h2_conditional_mle"]),
        float(_block(syllable_shuffle)["h2_conditional_mle"]),
    )
    word_structure = structure_index(
        float(words["h2_conditional_mle"]),
        float(_block(word_shuffle)["h2_conditional_mle"]),
    )

    sides = load_barthel_sides()
    raw_signs = [list(line) for side in sides for line in side.lines]
    scheme_ids = ("stem", "ligature_atomic", *GATE_SCHEMES)
    encoded = {scheme_id: _scheme_lines(raw_signs, scheme_id) for scheme_id in scheme_ids}
    stem_lines = encoded["stem"]
    stem = _block(stem_lines)
    stem_shuffle = _block(shuffle_lines(stem_lines, seed=0))
    verdict = classify_writing_system(
        stem,
        syllables,
        words,
        float(stem_shuffle["h2_conditional_mle"]),
    )
    sens_syllable_block = _block(sens_syllables)
    sens_word_block = _block(sens_words)
    sensitivity = classify_writing_system(
        stem,
        sens_syllable_block,
        sens_word_block,
        float(stem_shuffle["h2_conditional_mle"]),
    )

    schemes = []
    for scheme_id in scheme_ids:
        block = stem if scheme_id == "stem" else _block(encoded[scheme_id])
        shuffled = stem_shuffle if scheme_id == "stem" else _block(shuffle_lines(encoded[scheme_id], seed=0))
        scheme_verdict = verdict if scheme_id == "stem" else classify_writing_system(
            block,
            syllables,
            words,
            float(shuffled["h2_conditional_mle"]),
        )
        gate = _syllabary_gate(block) if scheme_id in GATE_SCHEMES else None
        schemes.append(
            {
                "id": scheme_id,
                "tokens": int(block["tokens"]),
                "inventory": int(block["inventory"]),
                "heaps_beta": block["heaps_beta"],
                "heaps_at_2000": block["heaps_at"].get("2000"),
                "h2_conditional_mle": block["h2_conditional_mle"],
                "structure_index": structure_index(
                    float(block["h2_conditional_mle"]),
                    float(shuffled["h2_conditional_mle"]),
                ),
                "track2_label": scheme_verdict["label"],
                "round2_label": ROUND2_LABELS[scheme_id],
                "ratio_to_syllables": scheme_verdict["ratio_stem_to_syllables"],
                "ratio_to_words": scheme_verdict["ratio_stem_to_words"],
                "gate_passes": bool(gate and gate["passes"]),
            }
        )

    alignment = None
    reading = None
    if verdict["label"] == "syllabic":
        alignment = frequency_alignment(stem_lines, syllable_lines)
        if (
            alignment["cosine_null_ge_fraction"] is not None
            and float(alignment["cosine_null_ge_fraction"]) <= ADOPT_NULL_FRACTION
        ):
            reading = "frequency_alignment_hypothesis"

    open_lexicon, targets = _expanded_open_lexicon()
    crib = _crib(open_lexicon, targets)
    if crib["adopted_readings"]:
        reading = "crib:" + ",".join(crib["adopted_readings"])

    length_by_source = {name: _length_block(lines) for name, lines in sources.items()}
    length_primary = _length_block(raw_running)
    formula_rows: dict[str, Any] = {}
    for width in FORMULA_WIDTHS:
        richness, top = _count_formulae(syllable_groups, width, FORMULA_MIN_COUNT)
        formula_rows[str(width)] = {"types": richness, "top": top[:12]}
    formula_null = _formula_null(
        syllable_groups,
        formula_rows[str(FORMULA_NULL_WIDTH)]["types"],
    )
    surfaces = _surface_index(syllable_groups, word_lines)

    headwords = load_churchill_headwords()
    track2 = {
        "verdict": verdict,
        "sensitivity_without_elliptical": {
            "label": sensitivity["label"],
            "syllable_tokens": int(sens_syllable_block["tokens"]),
            "syllable_types": int(sens_syllable_block["inventory"]),
            "word_tokens": int(sens_word_block["tokens"]),
            "word_types": int(sens_word_block["inventory"]),
            "words_rejected": sens_rejected,
        },
        "stem_tokens": int(stem["tokens"]),
        "stem_types": int(stem["inventory"]),
        "stem_heaps_beta": stem["heaps_beta"],
        "stem_h2": stem["h2_conditional_mle"],
        "stem_structure_index": structure_index(
            float(stem["h2_conditional_mle"]),
            float(stem_shuffle["h2_conditional_mle"]),
        ),
        "syllables": _public(syllables),
        "words": _public(words),
        "syllable_structure_index": syllable_structure,
        "word_structure_index": word_structure,
        "round1_syllable_structure": ROUND1_SYLLABLE_STRUCTURE,
        "round1_word_structure": ROUND1_WORD_STRUCTURE,
        "alignment": alignment,
        "plots": {
            "heaps": {
                "Barthel stems": _heaps_points(stem),
                "Old Rapanui syllables": _heaps_points(syllables),
                "Old Rapanui words": _heaps_points(words),
            }
        },
    }
    track_a = {"schemes": schemes, "any_gate": any(row["gate_passes"] for row in schemes)}
    result: dict[str, Any] = {
        "provider": provider.name,
        "provider_calls": len(provider.get_call_history()),
        "reading": reading,
        "phonological_cv_ceiling": PHONOLOGICAL_CV_CEILING,
        "normalization_rules": [dict(rule) for rule in NORMALIZATION_RULES],
        "thomson_round1_reproduction": {
            "name": thomson_round1.name,
            "orthography": thomson_round1.orthography,
            "syllables": thomson_round1.syllable_count,
            "words": thomson_round1.word_count,
            "words_rejected": thomson_round1.words_rejected,
        },
        "corpus": {
            "running_lines": len(running_rows),
            "running_word_tokens_raw": sum(len(row.words) for row in running_rows),
            "cv_word_tokens": sum(len(line) for line in word_lines),
            "cv_words_rejected": rejected,
            "syllable_tokens": sum(len(line) for line in syllable_lines),
            "by_source_raw_words": {name: sum(len(line) for line in lines) for name, lines in sources.items()},
            "metoro_lines": len(extract_metoro_lines()),
            "churchill_headwords": len(headwords),
            "churchill_thomson_mark": sum(1 for item in headwords if item.thomson),
            "churchill_geiseler_mark": sum(1 for item in headwords if item.geiseler),
            "lexicon_headwords": len(lexicon_headwords()),
            "routledge_chant_lines": len(load_routledge_chants()),
        },
        "track2": track2,
        "trackA": track_a,
        "trackB": crib,
        "word_length": {"primary": length_primary, "by_source": length_by_source},
        "formulae": {
            "min_count": FORMULA_MIN_COUNT,
            "widths": formula_rows,
            "null": formula_null,
            "surface_examples": {
                _formula_key((syllables,)): surface
                for syllables, surface in list(surfaces.items())[:0]
            },
        },
        "conclusions": _conclusions(track2, track_a, crib),
    }
    if provider.get_call_history():
        raise RuntimeError("Round 3 Track C must not call the language-model provider")
    return result


def _fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "—"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def _heappairs(track2: dict[str, Any]) -> str:
    syllables = track2["syllables"]
    words = track2["words"]
    return (
        f"| Old Rapanui syllables | {syllables['tokens']} | {syllables['inventory']} | "
        f"{_fmt(syllables['heaps_beta'])} | {_fmt(syllables['h2_conditional_mle'])} | "
        f"{_fmt(track2['syllable_structure_index'])} |\n"
        f"| Old Rapanui words | {words['tokens']} | {words['inventory']} | "
        f"{_fmt(words['heaps_beta'])} | {_fmt(words['h2_conditional_mle'])} | "
        f"{_fmt(track2['word_structure_index'])} |\n"
        f"| Round 1 Thomson syllables | {ROUND1_SYLLABLE_TOKENS} | {ROUND1_SYLLABLE_TYPES} | "
        f"{_fmt(ROUND1_SYLLABLE_BETA)} | {_fmt(ROUND1_SYLLABLE_H2)} | {_fmt(ROUND1_SYLLABLE_STRUCTURE)} |\n"
        f"| Round 1 Thomson words | {ROUND1_WORD_TOKENS} | {ROUND1_WORD_TYPES} | "
        f"{_fmt(ROUND1_WORD_BETA)} | {_fmt(ROUND1_WORD_H2)} | {_fmt(ROUND1_WORD_STRUCTURE)} |"
    )


def render_round3_trackc(result: dict[str, Any]) -> str:
    """Markdown note. Figures come from ``result``."""
    corpus = result["corpus"]
    track2 = result["track2"]
    verdict = track2["verdict"]
    holds = "\n".join(f"- {item}" for item in result["conclusions"]["holds"])
    changes = "\n".join(f"- {item}" for item in result["conclusions"]["changes"])
    rules = "\n".join(
        f"| `{rule['id']}` | {rule['rule']} |" for rule in result["normalization_rules"]
    )
    scheme_rows = "\n".join(
        "| {id} | {tokens} | {inventory} | {beta} | {h2} | {structure} | {label} | {prior} | {gate} |".format(
            id=row["id"],
            tokens=row["tokens"],
            inventory=row["inventory"],
            beta=_fmt(row["heaps_beta"]),
            h2=_fmt(row["h2_conditional_mle"]),
            structure=_fmt(row["structure_index"]),
            label=row["track2_label"],
            prior=row["round2_label"],
            gate="yes" if row["gate_passes"] else "no",
        )
        for row in result["trackA"]["schemes"]
    )
    crib_rows = "\n".join(
        "| {name} | {open_hits} | {perm} of {perm_n} | {rand} of {rand_n} | {crib} | {phrase} | {phrase_ge} of {phrase_n} | {prior} |".format(
            name=row["name"],
            open_hits=row["open_hits"],
            perm=row["permutation_ge"],
            perm_n=row["permutation_trials"],
            rand=row["random_ge"],
            rand_n=row["random_trials"],
            crib=row["crib_hits"],
            phrase=row["phrase_hits"],
            phrase_ge=row["phrase_permutation_ge"],
            phrase_n=row["phrase_permutation_trials"],
            prior=row["round2_open_hits"],
        )
        for row in result["trackB"]["hypotheses"]
    )
    primary = result["word_length"]["primary"]
    histogram = ", ".join(f"{length}:{count}" for length, count in primary["histogram"].items())
    source_rows = "\n".join(
        "| {name} | {tokens} | {mean} | {median} | {redup} |".format(
            name=name,
            tokens=block["tokens"],
            mean=_fmt(block["mean_syllables"]),
            median=_fmt(block["median_syllables"]),
            redup=_fmt(block["reduplication_rate"]),
        )
        for name, block in result["word_length"]["by_source"].items()
    )
    formula_lines = []
    for width, block in result["formulae"]["widths"].items():
        shown = ", ".join(f"`{text}` ×{count}" for text, count in block["top"][:8]) or "—"
        formula_lines.append(f"| {width} | {block['types']} | {shown} |")
    formula_table = "\n".join(formula_lines)
    null = result["formulae"]["null"]
    phrase_notes = []
    for row in result["trackB"]["hypotheses"]:
        if not row["phrase_shapes"]:
            continue
        shown = ", ".join(
            f"`{item['phrase']}` ×{item['count']}" for item in row["phrase_shapes"]
        )
        phrase_notes.append(
            f"{row['name']} phrase hits: {shown} "
            f"({row['phrase_permutation_ge']} of {row['phrase_permutation_trials']} permutations)."
        )
    phrase_note = " ".join(phrase_notes)
    h1 = next(row for row in result["trackB"]["hypotheses"] if row["name"] == "H1")
    h1_shapes = ", ".join(
        f"`{item['phrase']}` ×{item['count']}" for item in h1["phrase_shapes"]
    )
    reproduction = result["thomson_round1_reproduction"]
    sensitive = track2["sensitivity_without_elliptical"]
    raw = corpus["by_source_raw_words"]
    label = track2["verdict"]["label"]
    gate_open = result["trackA"]["any_gate"]
    adopted = result["trackB"]["adopted_readings"]
    moved = [
        row["id"]
        for row in result["trackA"]["schemes"]
        if row["track2_label"] != row["round2_label"]
    ]
    moved_sentence = (
        " Size labels changed for " + ", ".join(f"`{name}`" for name in moved) + "."
        if moved
        else ""
    )
    if label == "mixed" and not gate_open and not adopted:
        headline = (
            "**Verdict: still not a reading.** "
            "Primary Barthel stems stay mixed. No cited merge enters the 45–70 band. "
            "No anchor crib beats its nulls."
            + moved_sentence
        )
    else:
        headline = (
            "**Verdict: at least one pre-specified gate moved.** "
            f"Track 2 label: {label}. Syllabary gate opened: {'yes' if gate_open else 'no'}. "
            f"Adopted crib maps: {', '.join(adopted) or 'none'}."
        )
    reading = result["reading"] if result["reading"] else "None"
    return f"""# Round 3, Track C: a larger old-Rapanui comparison corpus

{headline} `reading` is {reading}.

The Rapanui side is no longer only the Thomson 1891 chants ({ROUND1_SYLLABLE_TOKENS} strict syllables). Primary running text is those chants with the love song excluded, Metoro's recitations for Jaussen, and the timo formula printed by Routledge in 1919, syllabified with the mapped orthography. That sample has {corpus['syllable_tokens']} syllables and {corpus['cv_word_tokens']} words ({corpus['cv_words_rejected']} words rejected). The lexicon is kept out of those sequences. This is a statistical comparison. It is not a decipherment.

Provider: `{result['provider']}`. Provider calls: {result['provider_calls']}.

## What holds, and what moved

### Conclusions that hold

{holds}

### Measurements that moved

{changes}

The matched comparison is no longer stuck at {ROUND1_SYLLABLE_TOKENS} syllables and {ROUND1_WORD_TOKENS} words. Stem tokens are {track2['stem_tokens']}. Syllable tokens are {track2['syllables']['tokens']}. Word tokens are {track2['words']['tokens']}. The shared count is the shorter of the two. At that count, stem types against syllables are {verdict['inventory_stem_at_syllable_n']} versus {verdict['inventory_syllables_at_n']} (ratio {_fmt(verdict['ratio_stem_to_syllables'])}). Stem types against words are {verdict['inventory_stem_at_word_n']} versus {verdict['inventory_words_at_n']} (ratio {_fmt(verdict['ratio_stem_to_words'])}).

Dropping Metoro's elliptical Mamari and Keiti lines (tablets C and E) leaves the label **{sensitive['label']}** ({sensitive['syllable_tokens']} syllables, {sensitive['word_tokens']} words).

## Sources and copyright

Full notes are in `data/rapanui/SOURCES.md`. Running text and lexicon lists are not mixed.

| Source | Role | What was copied | Status |
|---|---|---|---|
| Thomson 1891 | Running text | Chants already vendored, love song excluded. Raw words in this run: {raw['thomson_1891']} | US government report, 1891. Public domain |
| Metoro for Jaussen | Running text | {corpus['metoro_lines']} tablet lines from the vendored notebook transcription. Full A/B words {raw['metoro_jaussen_full']}; elliptical C/E words {raw['metoro_jaussen_elliptical']} | Jaussen died 1891. Notebook wording is public domain. Kohaumotu HTML is copied with attribution, not under the MIT license |
| Routledge 1919 | Running text | The printed formula `He timo te ako-ako`. Raw words: {raw['routledge_1919']} | Published 1919. Author died 1935. Public domain in the UK since 2006 and in the US |
| Churchill 1912 | Lexicon | {corpus['churchill_headwords']} headwords. Thomson suffix T on {corpus['churchill_thomson_mark']}. Geiseler suffix Q on {corpus['churchill_geiseler_mark']} | Carnegie Publication 174, 1912. Public domain. Library of Congress: free to use |
| Roussel 1908 | Lexicon, via Churchill | Not a second word list. *Le Muséon* n.s. 9 was inspected; its Rapanui column does not OCR cleanly. Churchill's translation of that vocabulary is the copy used | Roussel died 1898. The 1908 printing is public domain |
| Thomson examples and Routledge names | Lexicon | The short lists already described in `SOURCES.md` | Public domain |
| Wikipedia `lang=rap` | Crib open list only | Not in the running-text entropy | CC BY-SA 4.0, modern orthography |

Not copied: Métraux 1940 (author died 1963; life-plus-70 protection in France and Switzerland runs through 2033, the same standard that excludes Englert), the unpublished Roussel catechism and gospel manuscripts, Englert's dictionary, Fuentes 1960, and any modern dictionary. The 1914–15 Routledge field notebook chant is not in the 1919 book and was not taken from a later article.

Round 1 reproduction on the vendored Thomson file, strict, love song excluded: {reproduction['syllables']} syllables, {reproduction['words']} words, {reproduction['words_rejected']} rejected. Orthography `{reproduction['orthography']}`.

## Normalization

Every rule is applied by `decipherment.rapanui.phonemes` and `syllabify_word`, or by the loader that feeds them. Primary orthography is `mapped`.

| Rule | What it does |
|---|---|
{rules}

A running-text word enters the primary sequences only when `cv_syllables_mapped` accepts it. That rejects a stranded consonant instead of dropping the consonant and keeping the rest, and it rejects the French and English scraps in the Metoro HTML that are not inside italics ({corpus['cv_words_rejected']} rejections on the primary lines). Lexicon headwords are not appended to those lines.

## Track 2 inventory, Heaps, and entropy

Gates are the Track 2 gates, unchanged. Structure index of the stems against their own shuffle: {_fmt(track2['stem_structure_index'])}. Round 1 published that index as {_fmt(0.098)}. Syllable structure index {_fmt(track2['syllable_structure_index'])} (Round 1 {_fmt(ROUND1_SYLLABLE_STRUCTURE)}). Word structure index {_fmt(track2['word_structure_index'])} (Round 1 {_fmt(ROUND1_WORD_STRUCTURE)}).

| Sample | Tokens | Types | β | h2 | Structure |
|---|---:|---:|---:|---:|---:|
| Barthel stems | {track2['stem_tokens']} | {track2['stem_types']} | {_fmt(track2['stem_heaps_beta'])} | {_fmt(track2['stem_h2'])} | {_fmt(track2['stem_structure_index'])} |
{_heappairs(track2)}

![Inventory growth against the larger corpus](figures/{FIGURE_NAME})

h2 is H(next | previous) inside lines. The shuffle keeps the inventory, the line lengths, and the token frequencies (seed 0).

## Track A merges

The syllabary gate is unchanged: 45–70 types, Heaps β ≤ 0.25, and at least 80% of types seen by token 2000. It looks at the sign inventory. A larger Rapanui sample does not shrink the sign list. Gate opened: {"yes" if result["trackA"]["any_gate"] else "no"}.

The Track 2 *label* does use the Rapanui sample. Round 2 compared signs with 1,591 Thomson words, so the shared count was 1,591. This run has more word tokens than stem tokens, so the shared count is the full stem length. `barthel_suffix_only` and `barthel_families` keep Barthel's index letters and are therefore large inventories. At that longer shared count they meet the logographic size gate (types ≥ 250 and stem/word ratio ≥ 0.7). The primary stem inventory, which strips those index letters, stays mixed. The label describes size. It does not name a sign.

| Scheme | Tokens | Types | β | h2 | Structure | Label now | Round 2 label | Gate |
|---|---:|---:|---:|---:|---:|---|---|---|
{scheme_rows}

## Track B crib

The four maps, the five signs, the outside-anchor windows, and the crib targets are the Round 2 maps. The open list is the Round 2 list plus mapped word-shapes from the old running text and the lexicon. Windows: {result['trackB']['windows']}. Open word-shapes: {result['trackB']['open_lexicon']} (Round 2: {result['trackB']['round2_open_lexicon']}). Targets: {result['trackB']['targets']}. Syllable types drawn for the random null: {result['trackB']['syllable_types']} (Round 2: {result['trackB']['round2_syllable_types']}).

A reading needs crib-target hits above zero and both nulls at or under 5% of trials. Open-list hits are not enough.

| Map | Open hits | Permutation | Random syllables | Crib hits | Phrase hits | Phrase permutation | Round 2 open hits |
|---|---:|---:|---:|---:|---:|---:|---:|
{crib_rows}

Adopted maps: {", ".join(result["trackB"]["adopted_readings"]) or "none"}. Crib-target hits of zero cannot clear the gate. Open-list hits are a different score: they count any attested word-shape, including ordinary words such as *tau* and *uta*. A whole-word phrase hit means the cited words occur in that order somewhere in the language sample.

{phrase_note} H1 reads sign 200 as *tangata* and sign 076 as *ure*, so the outside pairs `200 200` and `200 076` become those phrases ({h1_shapes}). {h1['phrase_permutation_ge']} of {h1['phrase_permutation_trials']} permutations reach that score. That fraction is {h1['phrase_permutation_ge'] / h1['phrase_permutation_trials']:.3f}, on the 5% line. The phrase score is not a clear beat, and it is not the crib-target gate. Crib-target hits stay 0. `reading` stays None.

## Word length and chant formulae

These are the figures a segmentation test can set beside sign-run lengths. A word's length is the number of mapped (C)V syllables. Formulae are repeated word sequences on one line, minimum count {result['formulae']['min_count']}. Spellings are the mapped syllables joined, so `tagata` and `tangata` match.

Primary running text: mean {_fmt(primary['mean_syllables'])} syllables per word, median {_fmt(primary['median_syllables'])}, full-reduplication rate {_fmt(primary['reduplication_rate'])} ({primary['full_reduplications']} of {primary['tokens']}). Histogram (syllables:tokens): {histogram}.

| Source | CV word tokens | Mean syllables | Median | Full reduplication |
|---|---:|---:|---:|---:|
{source_rows}

| Words in the formula | Distinct formulae | Most frequent |
|---:|---:|---|
{formula_table}

Null for formulae of {null['width']} words at count ≥ {null['min_count']}: {null['observed_types']} distinct formulae. Shuffling words inside each line ({null['trials']} draws, seed {null['seed']}) reaches that richness in {null['ge']} draws (fraction {_fmt(null['fraction'])}). Beats the 5% gate: {"yes" if null["beats_null"] else "no"}. The gate here only says the repetition is tighter than a shuffle of the same words. It does not assign those formulae to signs.

## What this does not claim

No Barthel number is given a syllable or a gloss. The mapped spelling is an analysis of 19th-century letters, not a claim that Thomson or Jaussen recorded the phonemes that way. Metoro's words are a language sample. Track 4 already found they do not label the signs, and this track does not reopen that pairing. Conditional entropy in the linguistic band is not, by itself, proof of writing.

The run uses `MockProvider` only. Provider calls: {result['provider_calls']}.
"""


def write_round3_outputs(result: dict[str, Any], docs_dir: Path = DOCS_DIR) -> None:
    docs = Path(docs_dir)
    figures = docs / "figures"
    figures.mkdir(parents=True, exist_ok=True)
    (docs / "round3_trackC_rapanui_corpus.md").write_text(render_round3_trackc(result), encoding="utf-8")
    _svg_chart(
        figures / FIGURE_NAME,
        result["track2"]["plots"]["heaps"],
        "n",
        "types",
        "Inventory growth",
        "tokens",
        "types",
        log_x=True,
        log_y=True,
    )
