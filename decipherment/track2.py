"""Track 2: does the vendored Barthel corpus behave like a Rapanui syllabary?

The decision rule is fixed in this module. It is a statistical classification,
not a reading. ``MockProvider`` is accepted and never called.
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import load_barthel_sides
from decipherment.inventories import (
    HAND_ALLOGRAPH_MERGE,
    INVENTORY_MODES,
    POZDNIAKOV_52_LABELS,
    apply_merge,
    coverage,
    encode_lines,
    pozdniakov_barthel_stems,
    top_signs,
)
from decipherment.metrics import (
    conditional_entropy_mle,
    frequency_alignment,
    inventory_at,
    random_lines,
    rao_curve,
    rigid_lines,
    shuffle_lines,
    structure_index,
    summarize,
    token_count,
    word_edge_profile,
)
from decipherment.rapanui import (
    PHONOLOGICAL_CV_CEILING,
    build_sample,
    is_full_reduplication,
    load_thomson_word_lines,
    load_wikipedia_word_lines,
    primary_thomson_sample,
    syllabify_word,
)

# Pre-specified gates. Do not retune these to force a class.
STRUCTURE_FLOOR = 0.05
STRUCTURE_CEILING = 0.85
SYLLABIC_RATIO = 1.6
SYLLABIC_ABSOLUTE_MAX = 120
LOGOGRAPHIC_RATIO = 0.7
LOGOGRAPHIC_ABSOLUTE_MIN = 250
ADOPT_NULL_FRACTION = 0.05
HEAPS_CHECKPOINTS = (100, 250, 500, 1000, 2000, 4000, 8000)


def _public_summary(
    summary: dict[str, Any], checkpoints: tuple[int, ...] = HEAPS_CHECKPOINTS
) -> dict[str, Any]:
    curve = summary.pop("curve")
    heaps_at = {}
    tokens = int(summary["tokens"])
    for n in checkpoints:
        heaps_at[str(n)] = inventory_at(curve, n) if n <= tokens else None
    summary["heaps_at"] = heaps_at
    summary["curve_length"] = len(curve) - 1
    # Stash the curve for the caller, then the public copy omits it.
    summary["_curve"] = curve
    return summary


def _without_curve(summary: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in summary.items() if key != "_curve"}


def classify_writing_system(
    stem: dict[str, Any],
    syllables: dict[str, Any],
    words: dict[str, Any],
    shuffled_h2: float,
) -> dict[str, Any]:
    """Classify stem sequences against syllable and word samples.

    Non-linguistic first, using the structure index against a shuffle of the
    same tokens. Laplace conditional entropy divided by log2(V) is not a gate:
    add-one smoothing drives that ratio toward 1 for any large undersampled
    inventory, including a rigid cycle whose unsmoothed h2 is 0.

    Otherwise compare inventories at the same token count. Syllabic means the
    stem inventory at that count stays near the syllable inventory and under
    the absolute syllabic cap. Logographic means it is already in the same
    size band as the word inventory. The middle band is mixed.
    """
    h2 = float(stem["h2_conditional_mle"])
    structure = structure_index(h2, shuffled_h2)
    relative = float(stem["h2_over_log2_v"])
    n_syl = min(int(stem["tokens"]), int(syllables["tokens"]))
    n_word = min(int(stem["tokens"]), int(words["tokens"]))
    v_stem_syl = inventory_at(stem["_curve"], n_syl)
    v_syl = inventory_at(syllables["_curve"], n_syl)
    v_stem_word = inventory_at(stem["_curve"], n_word)
    v_word = inventory_at(words["_curve"], n_word)
    ratio_syl = (v_stem_syl / v_syl) if v_syl else float("inf")
    ratio_word = (v_stem_word / v_word) if v_word else float("inf")
    close_syl = v_stem_syl <= SYLLABIC_ABSOLUTE_MAX and ratio_syl <= SYLLABIC_RATIO
    close_word = v_stem_word >= LOGOGRAPHIC_ABSOLUTE_MIN and ratio_word >= LOGOGRAPHIC_RATIO

    if structure < STRUCTURE_FLOOR:
        label = "non-linguistic"
        why = "sign order is not tighter than a shuffle of the same signs"
    elif structure > STRUCTURE_CEILING:
        label = "non-linguistic"
        why = "sign order is nearly rigid compared with a shuffle of the same signs"
    elif close_syl:
        label = "syllabic"
        why = "at the same token count the stem inventory stays near the Rapanui syllable inventory"
    elif close_word:
        label = "logographic"
        why = "at the same token count the stem inventory is in the same size band as Rapanui words"
    else:
        label = "mixed"
        why = "the stem inventory is larger than a Rapanui syllabary and smaller than the Rapanui word inventory at the same token count"

    return {
        "label": label,
        "why": why,
        "structure_index": structure,
        "relative_h2_laplace": relative,
        "n_matched_syllables": n_syl,
        "inventory_stem_at_syllable_n": v_stem_syl,
        "inventory_syllables_at_n": v_syl,
        "ratio_stem_to_syllables": ratio_syl,
        "n_matched_words": n_word,
        "inventory_stem_at_word_n": v_stem_word,
        "inventory_words_at_n": v_word,
        "ratio_stem_to_words": ratio_word,
        "close_to_syllables": close_syl,
        "close_to_words": close_word,
        "phonological_cv_ceiling": PHONOLOGICAL_CV_CEILING,
    }


def _dedupe(lines: list[list[str]]) -> list[list[str]]:
    seen: set[tuple[str, ...]] = set()
    kept: list[list[str]] = []
    for line in lines:
        key = tuple(line)
        if key in seen:
            continue
        seen.add(key)
        kept.append(line)
    return kept


def run_track2(provider: MockProvider | None = None) -> dict[str, Any]:
    """Run the comparison. The provider is not asked for a completion."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Track 2 accepts MockProvider only")

    sides = load_barthel_sides()
    raw_lines = [list(line) for side in sides for line in side.lines]
    stem_lines_with_illegible = encode_lines(raw_lines, "stem", drop_illegible=False)
    stem_lines = encode_lines(raw_lines, "stem")
    illegible_dropped = token_count(stem_lines_with_illegible) - token_count(stem_lines)
    surface_lines = encode_lines(raw_lines, "surface")
    ligature_lines = encode_lines(raw_lines, "ligature_atomic")
    pozdniakov_lines = encode_lines(raw_lines, "pozdniakov_52")
    frequency_lines = encode_lines(raw_lines, "frequency_core_52")
    merged_lines = apply_merge(stem_lines, HAND_ALLOGRAPH_MERGE)

    thomson_words = load_thomson_word_lines(include_love_song=False)
    primary = primary_thomson_sample()
    strict = build_sample("thomson_strict", thomson_words, "strict")
    mapped = build_sample("thomson_mapped", thomson_words, "mapped")
    wiki_words = load_wikipedia_word_lines()
    wiki = build_sample("wikipedia_strict", wiki_words, "strict")

    syllable_lines = [list(line) for line in primary.syllable_lines]
    word_lines = [list(line) for line in primary.word_lines]

    stem = _public_summary(summarize(stem_lines))
    syllables = _public_summary(summarize(syllable_lines))
    words = _public_summary(summarize(word_lines))
    shuffled = shuffle_lines(stem_lines)
    shuffled_summary = _public_summary(summarize(shuffled))
    rigid = _public_summary(summarize(rigid_lines(stem_lines)))
    random_summary = _public_summary(summarize(random_lines(stem_lines)))
    surface = _public_summary(summarize(surface_lines))
    ligature = _public_summary(summarize(ligature_lines))

    verdict = classify_writing_system(
        stem,
        syllables,
        words,
        float(shuffled_summary["h2_conditional_mle"]),
    )
    deduped_lines = _dedupe(stem_lines)
    deduped = _public_summary(summarize(deduped_lines))
    deduped_shuf = shuffle_lines(deduped_lines, seed=0)
    deduped_verdict = classify_writing_system(
        deduped,
        syllables,
        words,
        float(summarize(deduped_shuf)["h2_conditional_mle"]),
    )

    core = pozdniakov_barthel_stems()
    top52 = set(top_signs(stem_lines, 52))
    stem_counts = Counter(sign for line in stem_lines for sign in line)
    syllable_groups: list[list[str]] = []
    reduplicated_words = 0
    for line in primary.word_lines:
        for word in line:
            parsed = syllabify_word(word, primary.orthography)
            if not parsed:
                continue
            syllable_groups.append(parsed)
            if is_full_reduplication(parsed):
                reduplicated_words += 1
    syllable_structure = structure_index(
        float(syllables["h2_conditional_mle"]),
        conditional_entropy_mle(shuffle_lines(syllable_lines, seed=0)),
    )
    word_structure = structure_index(
        float(words["h2_conditional_mle"]),
        conditional_entropy_mle(shuffle_lines(word_lines, seed=0)),
    )

    alignment = frequency_alignment(stem_lines, syllable_lines)
    adopted = (
        verdict["label"] == "syllabic"
        and alignment["cosine_null_ge_fraction"] is not None
        and float(alignment["cosine_null_ge_fraction"]) <= ADOPT_NULL_FRACTION
    )
    alignment["adopted"] = adopted
    alignment["adopt_rule"] = (
        "Adopt only if the verdict is syllabic and the rank alignment's "
        "transition cosine beats at least 95% of random bijections "
        f"(null fraction <= {ADOPT_NULL_FRACTION}). Adoption is still a "
        "hypothesis, not a reading."
    )

    if provider.get_call_history():
        raise RuntimeError("Track 2 must not call the language-model provider")

    def _ranks(lines: list[list[str]], limit: int = 120) -> dict[str, list[int]]:
        counts = Counter(token for line in lines for token in line)
        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]
        return {
            "rank": list(range(1, len(ranked) + 1)),
            "frequency": [count for _sign, count in ranked],
        }

    def _heaps_points(summary: dict[str, Any], points: int = 160) -> dict[str, list[int]]:
        curve = summary["_curve"]
        last = len(curve) - 1
        if last <= 1:
            return {"n": [], "types": []}
        if last <= points:
            ns = list(range(1, last + 1))
        else:
            ns = [1 + round(index * (last - 1) / (points - 1)) for index in range(points)]
        return {"n": ns, "types": [curve[n] for n in ns]}

    result: dict[str, Any] = {
        "provider": provider.name,
        "provider_calls": len(provider.get_call_history()),
        "inventory_modes": list(INVENTORY_MODES),
        "pozdniakov_labels": list(POZDNIAKOV_52_LABELS),
        "pozdniakov_label_count": len(POZDNIAKOV_52_LABELS),
        "pozdniakov_barthel_stem_count": len(core),
        "sides": [
            {
                "side": side.side,
                "path": side.path,
                "raw_tokens": side.token_count,
                "stem_tokens": token_count(
                    encode_lines([list(line) for line in side.lines], "stem")
                ),
                "lines": len(side.lines),
            }
            for side in sides
        ],
        "side_count": len(sides),
        "illegible_stems_dropped": illegible_dropped,
        "stem": _without_curve(stem),
        "surface": _without_curve(surface),
        "ligature_atomic": _without_curve(ligature),
        "syllables": _without_curve(syllables),
        "words": _without_curve(words),
        "shuffle": _without_curve(shuffled_summary),
        "rigid": _without_curve(rigid),
        "random": _without_curve(random_summary),
        "primary_rapanui": {
            "name": primary.name,
            "orthography": primary.orthography,
            "words": primary.word_count,
            "syllables": primary.syllable_count,
            "words_rejected": primary.words_rejected,
            "sections": len(primary.word_lines),
        },
        "thomson_strict_syllables": strict.syllable_count,
        "thomson_strict_rejected_words": strict.words_rejected,
        "thomson_mapped_syllables": mapped.syllable_count,
        "thomson_mapped_inventory": len({syl for line in mapped.syllable_lines for syl in line}),
        "wikipedia_strict_syllables": wiki.syllable_count,
        "wikipedia_strict_inventory": len({syl for line in wiki.syllable_lines for syl in line}),
        "wikipedia_strict_rejected_words": wiki.words_rejected,
        "pozdniakov_52": {
            "inventory": len({sign for line in pozdniakov_lines for sign in line}),
            "coverage_of_stem_tokens": coverage(stem_lines, core),
            "note": (
                "Membership in the published 51 Barthel stems (27a→027, 901 absent). "
                "Signs outside that list collapse to RES. This is not Pozdniakov's "
                "unpublished allograph merge, so coverage is not expected to reach 99.7%."
            ),
        },
        "frequency_core_52": {
            "inventory": len({sign for line in frequency_lines for sign in line}),
            "coverage_of_stem_tokens": coverage(stem_lines, top52),
            "note": (
                "Top 52 Barthel stems by frequency in this corpus, tail collapsed to RES. "
                "A frequency cutoff, not the Pozdniakov catalog."
            ),
        },
        "hand_allograph_6_64": {
            "merge": dict(HAND_ALLOGRAPH_MERGE),
            "tokens_064": stem_counts.get("064", 0),
            "tokens_006": stem_counts.get("006", 0),
            "inventory_after_merge": len({sign for line in merged_lines for sign in line}),
        },
        "duplicate_stem_lines": len(stem_lines) - len(deduped_lines),
        "deduped_stem_tokens": int(deduped["tokens"]),
        "deduped_stem_inventory": int(deduped["inventory"]),
        "deduped_verdict": deduped_verdict["label"],
        "syllable_structure_index": syllable_structure,
        "word_structure_index": word_structure,
        "word_reduplication": {
            "parsed_words": len(syllable_groups),
            "full_reduplications": reduplicated_words,
            "rate": (reduplicated_words / len(syllable_groups)) if syllable_groups else 0.0,
        },
        "syllable_word_edges": word_edge_profile(syllable_groups),
        "verdict": verdict,
        "alignment": alignment,
        "rao_stem": rao_curve(stem_lines),
        "rao_syllables": rao_curve(syllable_lines),
        "rao_words": rao_curve(word_lines),
        "top_stems": [
            {"sign": sign, "count": stem_counts[sign]} for sign in top_signs(stem_lines, 15)
        ],
        "plots": {
            "heaps": {
                "Barthel stems": _heaps_points(stem),
                "Rapanui syllables": _heaps_points(syllables),
                "Rapanui words": _heaps_points(words),
                "Ligatures kept whole": _heaps_points(ligature),
                "Shuffled stems": _heaps_points(shuffled_summary),
            },
            "zipf": {
                "Barthel stems": _ranks(stem_lines),
                "Rapanui syllables": _ranks(syllable_lines),
                "Rapanui words": _ranks(word_lines),
            },
        },
    }
    # Counters.most_common breaks ties by insertion order. Force a stable tie break.
    syllable_counts = Counter(syllable for line in syllable_lines for syllable in line)
    result["top_syllables"] = [
        {"syllable": syllable, "count": syllable_counts[syllable]}
        for syllable in sorted(
            syllable_counts,
            key=lambda item: (-syllable_counts[item], item),
        )[:15]
    ]
    return result
