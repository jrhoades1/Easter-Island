"""Write the Track 2 note and its figures from a ``run_track2`` result."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

from decipherment.rapanui import PHONOLOGICAL_CV_CEILING

DOCS_DIR = Path(__file__).resolve().parents[1] / "docs" / "decipherment"
FIGURES = DOCS_DIR / "figures"

_COLORS = ("#1b4f72", "#0e6655", "#922b21", "#6c3483", "#b9770e")


def _fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "—"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def _svg_chart(
    path: Path,
    series: dict[str, dict[str, list[Any]]],
    x_key: str,
    y_key: str,
    title: str,
    x_label: str,
    y_label: str,
    *,
    log_x: bool = False,
    log_y: bool = False,
) -> None:
    width, height = 760, 440
    left, right, top, bottom = 64, 16, 36, 72
    plot_w = width - left - right
    plot_h = height - top - bottom

    def tx(value: float) -> float:
        return math.log(value) if log_x else value

    def ty(value: float) -> float:
        return math.log(value) if log_y else value

    xs: list[float] = []
    ys: list[float] = []
    prepared: list[tuple[str, list[float], list[float]]] = []
    for name, points in series.items():
        row_x = [tx(float(item)) for item in points[x_key] if float(item) > 0]
        row_y = [ty(float(item)) for item in points[y_key] if float(item) > 0]
        # log filters must stay paired. Rebuild from raw pairs.
        paired_x: list[float] = []
        paired_y: list[float] = []
        for raw_x, raw_y in zip(points[x_key], points[y_key]):
            if float(raw_x) <= 0 or float(raw_y) <= 0:
                continue
            paired_x.append(tx(float(raw_x)))
            paired_y.append(ty(float(raw_y)))
        if not paired_x:
            continue
        prepared.append((name, paired_x, paired_y))
        xs.extend(paired_x)
        ys.extend(paired_y)
    if not xs:
        path.write_text("<svg xmlns='http://www.w3.org/2000/svg'/>", encoding="utf-8")
        return
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    if min_x == max_x:
        max_x += 1
    if min_y == max_y:
        max_y += 1

    def sx(value: float) -> float:
        return left + (value - min_x) / (max_x - min_x) * plot_w

    def sy(value: float) -> float:
        return top + (1 - (value - min_y) / (max_y - min_y)) * plot_h

    parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}'>",
        "<rect width='100%' height='100%' fill='#fbfaf6'/>",
        f"<text x='{left}' y='22' font-family='sans-serif' font-size='16'>{title}</text>",
        f"<line x1='{left}' y1='{top}' x2='{left}' y2='{top + plot_h}' stroke='#333'/>",
        f"<line x1='{left}' y1='{top + plot_h}' x2='{left + plot_w}' y2='{top + plot_h}' stroke='#333'/>",
        f"<text x='{left + plot_w / 2}' y='{height - 18}' text-anchor='middle' "
        f"font-family='sans-serif' font-size='12'>{x_label}</text>",
        f"<text x='16' y='{top + plot_h / 2}' transform='rotate(-90 16 {top + plot_h / 2})' "
        f"text-anchor='middle' font-family='sans-serif' font-size='12'>{y_label}</text>",
    ]
    legend_x = left + 8
    for index, (name, row_x, row_y) in enumerate(prepared):
        color = _COLORS[index % len(_COLORS)]
        polyline = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in zip(row_x, row_y))
        parts.append(
            f"<polyline fill='none' stroke='{color}' stroke-width='1.6' points='{polyline}'/>"
        )
        parts.append(
            f"<text x='{legend_x}' y='{top + 14 + index * 14}' fill='{color}' "
            f"font-family='sans-serif' font-size='11'>{name}</text>"
        )
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def _heaps_table(result: dict[str, Any]) -> str:
    rows = [
        ("Barthel stems", result["stem"]),
        ("Surface allographs", result["surface"]),
        ("Ligatures kept whole", result["ligature_atomic"]),
        ("Rapanui syllables", result["syllables"]),
        ("Rapanui words", result["words"]),
    ]
    checkpoints = ["100", "250", "500", "1000", "2000", "4000", "8000"]
    header = "| Sample | Tokens | Types | β | " + " | ".join(f"V({n})" for n in checkpoints) + " |"
    rule = "|---|---:|---:|---:|" + "|".join("---:" for _n in checkpoints) + "|"
    body = []
    for name, block in rows:
        cells = [
            name,
            str(block["tokens"]),
            str(block["inventory"]),
            _fmt(block["heaps_beta"]),
        ]
        for n in checkpoints:
            cells.append(
                _fmt(block["heaps_at"].get(n), 0) if block["heaps_at"].get(n) is not None else "—"
            )
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, rule, *body])


def _entropy_table(result: dict[str, Any]) -> str:
    rows = [
        ("Barthel stems", result["stem"]),
        ("Shuffled stems", result["shuffle"]),
        ("Rigid cycle", result["rigid"]),
        ("Uniform random", result["random"]),
        ("Rapanui syllables", result["syllables"]),
        ("Rapanui words", result["words"]),
    ]
    lines = [
        "| Sample | h1 unigram | h2 conditional (MLE) | h2 Laplace | h2 Laplace / log2 V | XX rate |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, block in rows:
        repetition = block["repetition"]
        lines.append(
            "| "
            + " | ".join(
                [
                    name,
                    _fmt(block["h1_unigram"]),
                    _fmt(block["h2_conditional_mle"]),
                    _fmt(block["h2_conditional_laplace"]),
                    _fmt(block["h2_over_log2_v"]),
                    _fmt(repetition["xx_rate"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def render_report(result: dict[str, Any]) -> str:
    """Markdown note. Numbers come only from ``result``."""
    verdict = result["verdict"]
    primary = result["primary_rapanui"]
    alignment = result["alignment"]
    label = verdict["label"]
    if alignment["adopted"]:
        adopted = (
            "The frequency-rank alignment beat the null bijections under a syllabic verdict. "
            "It is still a hypothesis, not a reading. Pairs are not glossed."
        )
    else:
        adopted = (
            "A frequency-rank alignment was scored against random bijections. "
            "It is not proposed. Adoption requires a syllabic verdict and a transition "
            "cosine that beats 95% of the bijections. Neither condition is treated as a reading."
        )
    side_rows = "\n".join(
        f"| {side['side']} | {side['stem_tokens']} | `{side['path']}` |" for side in result["sides"]
    )
    stem_rows = "\n".join(f"| {row['sign']} | {row['count']} |" for row in result["top_stems"])
    syllable_rows = "\n".join(
        f"| {row['syllable']} | {row['count']} |" for row in result["top_syllables"]
    )
    rao_rows = []
    by_k = {point["k"]: point for point in result["rao_stem"]}
    syl_by_k = {point["k"]: point for point in result["rao_syllables"]}
    word_by_k = {point["k"]: point for point in result["rao_words"]}
    for k in sorted(by_k):
        rao_rows.append(
            "| "
            + " | ".join(
                [
                    str(k),
                    _fmt(by_k[k]["h2_laplace"]),
                    _fmt(syl_by_k[k]["h2_laplace"]) if k in syl_by_k else "—",
                    _fmt(word_by_k[k]["h2_laplace"]) if k in word_by_k else "—",
                ]
            )
            + " |"
        )
    return f"""# Track 2: does rongorongo behave like a Rapanui syllabary?

**Verdict: {label}.** {verdict["why"][:1].upper()}{verdict["why"][1:]}. This is a statistical classification of the vendored Barthel corpus against a Rapanui sample. It is not a decipherment, and it does not assign a reading to any sign.

Structure index of Barthel stems against a shuffle of the same stems: {_fmt(verdict["structure_index"])}. At {verdict["n_matched_syllables"]} tokens, stem types = {verdict["inventory_stem_at_syllable_n"]} and Rapanui syllable types = {verdict["inventory_syllables_at_n"]} (ratio {_fmt(verdict["ratio_stem_to_syllables"])}). At {verdict["n_matched_words"]} tokens, stem types = {verdict["inventory_stem_at_word_n"]} and Rapanui word types = {verdict["inventory_words_at_n"]} (ratio {_fmt(verdict["ratio_stem_to_words"])}). The phonological (C)V ceiling used as a reference is {PHONOLOGICAL_CV_CEILING}. Full stem inventory: {result["stem"]["inventory"]} types in {result["stem"]["tokens"]} tokens.

Dropping {result["duplicate_stem_lines"]} exact duplicate stem lines leaves the class **{result["deduped_verdict"]}** ({result["deduped_stem_inventory"]} types, {result["deduped_stem_tokens"]} tokens).

{adopted}

## Corpus

Barthel numbers are read from the Kohaumotu HTML already under `tests/fixtures`. Hyphen-separated `<td>` text is copied. Sides with no digit transcription are skipped. JSON twins of the same side, and the Mamari calendar extract, are not added again. Drawings and transliteration follow C.E.I.P.P. after Thomas Barthel; the hosted copy is Kohaumotu (`http://kohaumotu.org/rongorongo_org/copy.html`: copy and non-profit distribution with the source acknowledged). Barthel's catalog is Thomas S. Barthel, *Grundlagen zur Entzifferung der Osterinselschrift* (Hamburg, 1958).

{result["side_count"]} sides are in the sample.

| Side | Stem tokens | Vendored file |
|---|---:|---|
{side_rows}

Illegible `000` is dropped ({result["illegible_stems_dropped"]} stem tokens). Parenthetical lacuna ranges such as `(6-8)!` are dropped. Ligatures written with `.` or `:` are split in the stem inventory. Letter suffixes (`378y`, `040a`) and a leading orientation `V` are stripped, which is the same mechanical stem used by the Mamari scoreboards. Those choices are the `stem` mode below.

The Rapanui sample is documented in `data/rapanui/SOURCES.md`. Primary running text: Thomson 1891 chants, love song excluded, orthography `{primary["orthography"]}` ({primary["syllables"]} syllables, {primary["words"]} words, {primary["words_rejected"]} words rejected). Strict Thomson syllables: {result["thomson_strict_syllables"]} (rejected words {result["thomson_strict_rejected_words"]}). Mapped Thomson syllables: {result["thomson_mapped_syllables"]} (inventory {result["thomson_mapped_inventory"]}). Wikipedia `lang=rap` spans, strict: {result["wikipedia_strict_syllables"]} syllables, inventory {result["wikipedia_strict_inventory"]}. Wikipedia spans are not pooled into the chant conditional entropy.

## Sign-variant options

Each mode is switchable in `decipherment.inventories.encode_lines`.

| Mode | What it does | Types in this run |
|---|---|---:|
| `surface` | Split ligatures; keep allograph letters | {result["surface"]["inventory"]} |
| `stem` | Split ligatures; strip allograph letters. Primary sample | {result["stem"]["inventory"]} |
| `ligature_atomic` | Keep dot and colon ligatures as one sign | {result["ligature_atomic"]["inventory"]} |
| `pozdniakov_52` | Collapse stems outside the published basic list to `RES` | {result["pozdniakov_52"]["inventory"]} |
| `frequency_core_52` | Keep the 52 most frequent stems; collapse the tail to `RES` | {result["frequency_core_52"]["inventory"]} |
| `stem_merge_6_64` | Map Barthel `064` to `006` | {result["hand_allograph_6_64"]["inventory_after_merge"]} |

Pozdniakov's 52 labels ({result["pozdniakov_label_count"]} names, including `27a` and `901`) are the list printed from Pozdniakov & Pozdniakov 2007. `901` is not a Barthel number. `27a` is stored as stem `027`, which also absorbs Barthel `27b` because the stemmer cannot see the inversion. The Barthel-applicable set therefore has {result["pozdniakov_barthel_stem_count"]} stems. Membership coverage of stem tokens is {_fmt(result["pozdniakov_52"]["coverage_of_stem_tokens"])}. That is not the 99.7% figure: the published merge table that would fold other Barthel numbers into these signs is not in this repository, and it is not invented here. {result["pozdniakov_52"]["note"]}

`frequency_core_52` coverage is {_fmt(result["frequency_core_52"]["coverage_of_stem_tokens"])}. {result["frequency_core_52"]["note"]}

The hand pair is the one substitution Wikipedia attributes to Pozdniakov's parallel phrases: sign 6 and sign 64. Stem `064` occurs {result["hand_allograph_6_64"]["tokens_064"]} times; stem `006` occurs {result["hand_allograph_6_64"]["tokens_006"]} times. The flag defaults off.

Citations: Konstantin Pozdniakov, "Les bases du déchiffrement de l'écriture de l'île de Pâques," *Journal de la Société des Océanistes* 103 (1996): 289–303. Igor Pozdniakov and Konstantin Pozdniakov, "Rapanui writing and the Rapanui language: preliminary results of a statistical analysis," *Forum for Anthropology and Culture* 3 (2007): 89–122. The 52-sign count and the 99.7% claim are the 2007 result. The 1996 paper is the parallel-text study those later counts rest on.

## Inventory growth

Heaps exponent β is the OLS slope of log(types) on log(tokens) for n ≥ 50. V(n) is types in the first n tokens. A syllabary of a five-vowel (C)V language should flatten near the phonological ceiling of {PHONOLOGICAL_CV_CEILING} (10 consonants × 5 vowels + 5 bare vowels; the "ten consonants and five vowels" count is the vendored Wikipedia phonology section, and the full crossing is an assumption).

{_heaps_table(result)}

![Inventory growth](figures/heaps.svg)

## Zipf

Slope and R² are OLS of log(frequency) on log(rank). The second pair drops hapaxes, which otherwise sit on a horizontal line at frequency 1.

| Sample | Slope (all ranks) | R² | Slope (frequency ≥ 2) | R² |
|---|---:|---:|---:|---:|
| Barthel stems | {_fmt(result["stem"]["zipf_slope"])} | {_fmt(result["stem"]["zipf_r2"])} | {_fmt(result["stem"]["zipf_slope_freq_ge2"])} | {_fmt(result["stem"]["zipf_r2_freq_ge2"])} |
| Rapanui syllables | {_fmt(result["syllables"]["zipf_slope"])} | {_fmt(result["syllables"]["zipf_r2"])} | {_fmt(result["syllables"]["zipf_slope_freq_ge2"])} | {_fmt(result["syllables"]["zipf_r2_freq_ge2"])} |
| Rapanui words | {_fmt(result["words"]["zipf_slope"])} | {_fmt(result["words"]["zipf_r2"])} | {_fmt(result["words"]["zipf_slope_freq_ge2"])} | {_fmt(result["words"]["zipf_r2_freq_ge2"])} |

![Rank against frequency](figures/zipf.svg)

Most frequent stems and syllables (primary samples). Frequency order is not a reading.

| Stem | Count |
|---|---:|
{stem_rows}

| Syllable | Count |
|---|---:|
{syllable_rows}

## Conditional entropy

h1 is the unigram entropy. h2 is H(next | previous) inside lines, which is the conditional entropy in Rao et al., *Science* (2009), "Entropic Evidence for Linguistic Structure in the Indus Script." Laplace h2 uses add-one smoothing over the observed inventory. Dividing Laplace h2 by log2(V) is reported and is not a gate. On this corpus the rigid cycle has MLE h2 = {_fmt(result["rigid"]["h2_conditional_mle"])} and Laplace h2 / log2(V) = {_fmt(result["rigid"]["h2_over_log2_v"])}: add-one smoothing pushes the ratio toward 1 whenever the inventory is large and most successors are unseen. The structure index is `1 - h2(text) / h2(shuffle)` on the MLE, so the shuffle keeps the same inventory, the same line lengths, and the same token frequencies. Stem structure index = {_fmt(verdict["structure_index"])}. Syllable structure index = {_fmt(result["syllable_structure_index"])}. Word structure index = {_fmt(result["word_structure_index"])}. The word index is inflated by hapaxes: a word seen once has only one observed successor. Sproat's critique stands: a mid-range conditional entropy by itself does not prove that a sign system is writing. The class above uses the stem structure index only as a gate, then uses inventory size.

{_entropy_table(result)}

Rao-style curves: Laplace h2 after keeping the k most frequent types and collapsing the rest to one residual class. Step size 20.

| k | Stems | Syllables | Words |
|---:|---:|---:|---:|
{chr(10).join(rao_rows)}

![Conditional entropy by token-set size](figures/entropy.svg)

Adjacent repetition (XX) is in the entropy table. ABAB rate (a repeated pair that is not XX): stems {_fmt(result["stem"]["repetition"]["abab_rate"])}, syllables {_fmt(result["syllables"]["repetition"]["abab_rate"])}, words {_fmt(result["words"]["repetition"]["abab_rate"])}. Full reduplication of a parsed word (the syllable string is two identical halves): {result["word_reduplication"]["full_reduplications"]} / {result["word_reduplication"]["parsed_words"]} = {_fmt(result["word_reduplication"]["rate"])}. Hapax stems: {result["stem"]["hapax"]} of {result["stem"]["inventory"]}.

## Position in the line

Among types with frequency at least 10, the share that occur in initial, medial, and final position. For stems the boundary is the inscribed line. For syllables the boundary is the orthographic word (first syllable, interior syllables, last syllable). Those are different boundaries. The chant sample is four long sections, so inscribed-line edges on the syllable stream are not used.

| Sample | Boundary | Frequent types | In all three positions |
|---|---|---:|---:|
| Barthel stems | inscribed line | {result["stem"]["position"]["frequent_types"]} | {_fmt(result["stem"]["position"]["frequent_in_all_three_rate"])} |
| Rapanui syllables | word edge | {result["syllable_word_edges"]["frequent_types"]} | {_fmt(result["syllable_word_edges"]["frequent_in_all_three_rate"])} |
| Rapanui words | chant section | {result["words"]["position"]["frequent_types"]} | {_fmt(result["words"]["position"]["frequent_in_all_three_rate"])} |

## Frequency alignment

{alignment["adopt_rule"]}

k = {alignment["k"]}. Permutations = {alignment["permutations"]}. Transition-matrix cosine = {_fmt(alignment["cosine"])}. Fraction of random bijections with cosine at least that high = {_fmt(alignment["cosine_null_ge_fraction"])}. Spearman correlation of self-repetition rates = {_fmt(alignment["repetition_spearman"])}. Fraction of bijections with Spearman at least that high = {_fmt(alignment["repetition_null_ge_fraction"])}. Adopted = {alignment["adopted"]}.

No sign is given a gloss. `reading` is {alignment["reading"]}.

## Decision rule

The rule is `classify_writing_system` in `decipherment/track2.py`.

1. Structure index below {STRUCTURE_FLOOR}: non-linguistic (no order beyond the unigram shuffle).
2. Structure index above {STRUCTURE_CEILING}: non-linguistic (rigid).
3. Else, at n = min(stem tokens, syllable tokens): syllabic if stem types ≤ {SYLLABIC_ABSOLUTE_MAX} and stem types / syllable types ≤ {SYLLABIC_RATIO}.
4. Else, at n = min(stem tokens, word tokens): logographic if stem types ≥ {LOGOGRAPHIC_ABSOLUTE_MIN} and stem types / word types ≥ {LOGOGRAPHIC_RATIO}.
5. Else: mixed.

Thresholds were set before the corpus totals were used to edit them. Duplicate-line removal is a sensitivity check, not the primary label.

## What this does not claim

The class is not a translation. A mixed label means the Barthel-stem sequences are language-like in order and sit between a Rapanui syllabary and a Rapanui word list in inventory growth. It does not identify which signs are syllabic and which are logographic. Pozdniakov's 99.7% coverage is not reproduced here, because the allograph merges that produced it are not vendored. Thomson's chants are a damaged 19th-century record; the strict orthography throws away words the filter cannot parse, and the mapped orthography is an explicit substitution list. Conditional entropy is one comparison among several, and a value inside the linguistic band is not, by itself, proof of writing.

The run uses `MockProvider` only. Provider calls: {result["provider_calls"]}.
"""


# Imported lazily by the constants reference above. The thresholds live in track2
# and are repeated in the prose via these names.
from decipherment.track2 import (  # noqa: E402
    LOGOGRAPHIC_ABSOLUTE_MIN,
    LOGOGRAPHIC_RATIO,
    STRUCTURE_CEILING,
    STRUCTURE_FLOOR,
    SYLLABIC_ABSOLUTE_MAX,
    SYLLABIC_RATIO,
)


def write_report(result: dict[str, Any], docs_dir: Path = DOCS_DIR) -> Path:
    """Write the note and three SVG figures. Returns the markdown path."""
    figures = docs_dir / "figures"
    figures.mkdir(parents=True, exist_ok=True)
    _svg_chart(
        figures / "heaps.svg",
        result["plots"]["heaps"],
        "n",
        "types",
        "Distinct types against tokens",
        "Tokens",
        "Distinct types",
    )
    _svg_chart(
        figures / "zipf.svg",
        result["plots"]["zipf"],
        "rank",
        "frequency",
        "Rank against frequency",
        "Rank (log)",
        "Frequency (log)",
        log_x=True,
        log_y=True,
    )
    rao = {
        "Barthel stems": {
            "k": [point["k"] for point in result["rao_stem"]],
            "h2": [point["h2_laplace"] for point in result["rao_stem"]],
        },
        "Rapanui syllables": {
            "k": [point["k"] for point in result["rao_syllables"]],
            "h2": [point["h2_laplace"] for point in result["rao_syllables"]],
        },
        "Rapanui words": {
            "k": [point["k"] for point in result["rao_words"]],
            "h2": [point["h2_laplace"] for point in result["rao_words"]],
        },
    }
    _svg_chart(
        figures / "entropy.svg",
        rao,
        "k",
        "h2",
        "Laplace conditional entropy by token-set size",
        "Most frequent types kept (k)",
        "h2 (bits)",
    )
    path = docs_dir / "track2_syllabary_test.md"
    path.write_text(render_report(result), encoding="utf-8")
    return path
