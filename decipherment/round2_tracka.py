"""Round 2 Track A: allograph merges, then the Track 2 syllabary comparison.

The syllabary gate below was taken from the requested band (about 45–70
types, and a curve that flattens) and from the Round 1 baselines already
in ``docs/decipherment/track2_syllabary_test.md``. It is not tuned to the
merged inventories. ``MockProvider`` is accepted and never called.
No sign is given a reading.
"""

from __future__ import annotations

import random
from collections import Counter
from typing import Any

from agents.base.providers import MockProvider
from decipherment.allographs import MERGE_RULES, SCHEMA_IDS, encode_scheme_lines
from decipherment.barthel_corpus import load_barthel_sides
from decipherment.inventories import encode_lines, pozdniakov_barthel_stems
from decipherment.metrics import (
    frequency_alignment,
    inventory_at,
    shuffle_lines,
    structure_index,
    summarize,
)
from decipherment.rapanui import PHONOLOGICAL_CV_CEILING, primary_thomson_sample
from decipherment.track2 import (
    ADOPT_NULL_FRACTION,
    HEAPS_CHECKPOINTS,
    classify_writing_system,
)

# Pre-registered. Round 1 syllables: 49 types, Heaps β ≈ 0.14, and the whole
# inventory is already present by 2,000 tokens. Round 1 stems: 630 types,
# β ≈ 0.42. The band is the one named for this track. β must sit on the
# syllable side of the gap between those two published baselines.
SYLLABARY_TYPE_MIN = 45
SYLLABARY_TYPE_MAX = 70
HEAPS_BETA_MAX = 0.25
EARLY_INVENTORY_MIN = 0.80
EARLY_N = 2000

# Cited schemes the gate is allowed to consider. Residual-bin collapses are
# not in this tuple: forcing the tail into RES makes 52 types by construction.
GATE_SCHEMES = (
    "barthel_suffix_only",
    "barthel_families",
    "barthel_families_whole",
    "pozdniakov_2007",
    "pozdniakov_2007_whole",
    "pozdniakov_1996_gaping_mouth",
    "horley_2005",
    "horley_2005_whole",
)


def _heaps_at(curve: list[int], tokens: int) -> dict[str, int | None]:
    found: dict[str, int | None] = {}
    for n in HEAPS_CHECKPOINTS:
        found[str(n)] = inventory_at(curve, n) if n <= tokens else None
    return found


def _block(lines: list[list[str]]) -> dict[str, Any]:
    summary = summarize(lines)
    curve = summary.pop("curve")
    tokens = int(summary["tokens"])
    summary["heaps_at"] = _heaps_at(curve, tokens)
    summary["_curve"] = curve
    return summary


def _public(summary: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in summary.items() if key != "_curve"}


def _syllabary_gate(summary: dict[str, Any]) -> dict[str, Any]:
    inventory = int(summary["inventory"])
    beta = summary["heaps_beta"]
    tokens = int(summary["tokens"])
    early_types = inventory_at(summary["_curve"], EARLY_N) if tokens >= EARLY_N else None
    early_share = (early_types / inventory) if early_types is not None and inventory else None
    count_ok = SYLLABARY_TYPE_MIN <= inventory <= SYLLABARY_TYPE_MAX
    beta_ok = beta is not None and float(beta) <= HEAPS_BETA_MAX
    early_ok = early_share is not None and early_share >= EARLY_INVENTORY_MIN
    return {
        "type_min": SYLLABARY_TYPE_MIN,
        "type_max": SYLLABARY_TYPE_MAX,
        "heaps_beta_max": HEAPS_BETA_MAX,
        "early_n": EARLY_N,
        "early_inventory_min": EARLY_INVENTORY_MIN,
        "inventory": inventory,
        "heaps_beta": beta,
        "early_types": early_types,
        "early_share": early_share,
        "count_in_band": count_ok,
        "beta_flattens": beta_ok,
        "early_share_flattens": early_ok,
        "passes": bool(count_ok and beta_ok and early_ok),
    }


def _initial_rates(groups: list[list[str]], types: list[str]) -> list[float]:
    """Share of each type's tokens that sit in first position of a group."""
    wanted = set(types)
    initial = {item: 0 for item in types}
    total = {item: 0 for item in types}
    for group in groups:
        for index, token in enumerate(group):
            if token not in wanted:
                continue
            total[token] += 1
            if index == 0:
                initial[token] += 1
    return [(initial[item] / total[item]) if total[item] else 0.0 for item in types]


def _ranked(lines: list[list[str]], k: int) -> list[str]:
    counts = Counter(token for line in lines for token in line)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [sign for sign, _count in ordered[:k]]


def _average_ranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda index: (values[index], index))
    ranks = [0.0 for _value in values]
    start = 0
    while start < len(order):
        end = start
        while end + 1 < len(order) and values[order[end + 1]] == values[order[start]]:
            end += 1
        average = (start + 1 + end + 1) / 2
        for position in range(start, end + 1):
            ranks[order[position]] = average
        start = end + 1
    return ranks


def _spearman(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    rank_x = _average_ranks(xs)
    rank_y = _average_ranks(ys)
    mean_x = sum(rank_x) / n
    mean_y = sum(rank_y) / n
    var_x = sum((x - mean_x) ** 2 for x in rank_x) ** 0.5
    var_y = sum((y - mean_y) ** 2 for y in rank_y) ** 0.5
    if var_x == 0 or var_y == 0:
        return 0.0
    covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(rank_x, rank_y))
    return covariance / (var_x * var_y)


def positional_alignment(
    sign_lines: list[list[str]],
    syllable_groups: list[list[str]],
    *,
    k: int = 30,
    permutations: int = 200,
    seed: int = 1,
) -> dict[str, Any]:
    """Frequency-rank pairing, then Spearman of initial-position rates.

    Sign edges are inscribed lines. Syllable groups must be one group per
    orthographic word, not a whole chant section. Those boundaries are not
    the same kind of edge. The pairing is a hypothesis. ``reading`` is None.
    """
    sign_items = _ranked(sign_lines, k)
    syllable_items = _ranked(syllable_groups, k)
    width = min(len(sign_items), len(syllable_items))
    sign_items = sign_items[:width]
    syllable_items = syllable_items[:width]
    if width < 5:
        return {
            "k": width,
            "permutations": 0,
            "initial_spearman": None,
            "initial_null_ge_fraction": None,
            "hypothesis_only": True,
            "reading": None,
        }
    sign_rates = _initial_rates(sign_lines, sign_items)
    syllable_rates = _initial_rates(syllable_groups, syllable_items)
    observed = _spearman(sign_rates, syllable_rates)
    generator = random.Random(seed)
    ge_count = 0
    for _draw in range(permutations):
        permutation = list(range(width))
        generator.shuffle(permutation)
        shuffled = [syllable_rates[index] for index in permutation]
        if _spearman(sign_rates, shuffled) >= observed:
            ge_count += 1
    return {
        "k": width,
        "permutations": permutations,
        "initial_spearman": observed,
        "initial_null_ge_fraction": ge_count / permutations,
        "boundary_sign": "inscribed line",
        "boundary_syllable": "orthographic word",
        "hypothesis_only": True,
        "reading": None,
    }


def _scheme_lines(
    raw_lines: list[list[str]],
    scheme_id: str,
) -> list[list[str]]:
    if scheme_id == "stem":
        return encode_lines(raw_lines, "stem")
    if scheme_id == "ligature_atomic":
        return encode_lines(raw_lines, "ligature_atomic")
    decompose = not scheme_id.endswith("_whole")
    scheme = scheme_id[: -len("_whole")] if scheme_id.endswith("_whole") else scheme_id
    if scheme not in SCHEMA_IDS:
        raise ValueError(f"unknown scheme id {scheme_id}")
    return encode_scheme_lines(raw_lines, scheme, decompose_ligatures=decompose)


def _coverage(lines: list[list[str]], core: frozenset[str]) -> float:
    total = 0
    inside = 0
    for line in lines:
        for sign in line:
            total += 1
            digits = sign[:3]
            suffix = sign[3:]
            if digits == "027" and suffix == "b":
                continue
            if digits in core or (digits == "027" and suffix == "a"):
                inside += 1
    if total == 0:
        return 0.0
    return inside / total


def _top(lines: list[list[str]], limit: int = 8) -> list[dict[str, Any]]:
    counts = Counter(sign for line in lines for sign in line)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]
    return [{"sign": sign, "count": count} for sign, count in ordered]


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


def run_round2_tracka(provider: MockProvider | None = None) -> dict[str, Any]:
    """Merge variants under each cited scheme and compare with Rapanui.

    The provider is not asked for a completion.
    """
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Round 2 Track A accepts MockProvider only")

    sides = load_barthel_sides()
    raw_lines = [list(line) for side in sides for line in side.lines]
    primary = primary_thomson_sample()
    syllable_lines = [list(line) for line in primary.syllable_lines]
    word_lines = [list(line) for line in primary.word_lines]
    syllable_groups = _word_syllable_groups(primary)

    syllables = _block(syllable_lines)
    words = _block(word_lines)
    syllable_shuffle = shuffle_lines(syllable_lines, seed=0)
    word_shuffle = shuffle_lines(word_lines, seed=0)

    scheme_ids = (
        "stem",
        "ligature_atomic",
        "barthel_suffix_only",
        "barthel_families",
        "barthel_families_whole",
        "pozdniakov_2007",
        "pozdniakov_2007_whole",
        "pozdniakov_1996_gaping_mouth",
        "horley_2005",
        "horley_2005_whole",
    )
    encoded = {scheme_id: _scheme_lines(raw_lines, scheme_id) for scheme_id in scheme_ids}
    blocks = {scheme_id: _block(lines) for scheme_id, lines in encoded.items()}
    shuffles = {
        scheme_id: _block(shuffle_lines(lines, seed=0)) for scheme_id, lines in encoded.items()
    }

    core = pozdniakov_barthel_stems()
    schemes: dict[str, Any] = {}
    for scheme_id in scheme_ids:
        block = blocks[scheme_id]
        shuffled = shuffles[scheme_id]
        verdict = classify_writing_system(
            block,
            syllables,
            words,
            float(shuffled["h2_conditional_mle"]),
        )
        gate = _syllabary_gate(block) if scheme_id in GATE_SCHEMES else None
        record: dict[str, Any] = {
            "id": scheme_id,
            "decompose_ligatures": not scheme_id.endswith("_whole") and scheme_id != "ligature_atomic",
            "tokens": int(block["tokens"]),
            "inventory": int(block["inventory"]),
            "hapax": int(block["hapax"]),
            "heaps_beta": block["heaps_beta"],
            "heaps_at": block["heaps_at"],
            "h1_unigram": block["h1_unigram"],
            "h2_conditional_mle": block["h2_conditional_mle"],
            "h2_conditional_laplace": block["h2_conditional_laplace"],
            "h2_over_log2_v": block["h2_over_log2_v"],
            "zipf_slope": block["zipf_slope"],
            "zipf_r2": block["zipf_r2"],
            "repetition": block["repetition"],
            "position": block["position"],
            "shuffle_h2_conditional_mle": shuffled["h2_conditional_mle"],
            "structure_index": structure_index(
                float(block["h2_conditional_mle"]),
                float(shuffled["h2_conditional_mle"]),
            ),
            "track2_label": verdict["label"],
            "ratio_to_syllables": verdict["ratio_stem_to_syllables"],
            "ratio_to_words": verdict["ratio_stem_to_words"],
            "inventory_at_syllable_n": verdict["inventory_stem_at_syllable_n"],
            "inventory_at_word_n": verdict["inventory_stem_at_word_n"],
            "top": _top(encoded[scheme_id]),
            "gate": gate,
            "uses_residual": False,
        }
        if scheme_id.startswith("pozdniakov"):
            record["coverage_of_published_barthel_stems"] = _coverage(encoded[scheme_id], core)
        schemes[scheme_id] = record

    triggered = [scheme_id for scheme_id, record in schemes.items() if record["gate"] and record["gate"]["passes"]]
    alignments: dict[str, Any] = {}
    if triggered:
        for scheme_id in triggered:
            frequency = frequency_alignment(encoded[scheme_id], syllable_lines)
            frequency["hypothesis_only"] = True
            frequency["reading"] = None
            frequency["adopted"] = False
            positional = positional_alignment(encoded[scheme_id], syllable_groups)
            alignments[scheme_id] = {
                "frequency": frequency,
                "positional": positional,
                "note": (
                    "Hypothesis only. The rank pairing is not a reading. "
                    "Adoption of the Track 2 cosine rule would still not assign a value."
                ),
            }

    if provider.get_call_history():
        raise RuntimeError("Round 2 Track A must not call the language-model provider")

    return {
        "provider": provider.name,
        "provider_calls": len(provider.get_call_history()),
        "side_count": len(sides),
        "phonological_cv_ceiling": PHONOLOGICAL_CV_CEILING,
        "primary_rapanui": {
            "name": primary.name,
            "orthography": primary.orthography,
            "words": primary.word_count,
            "syllables": primary.syllable_count,
            "words_rejected": primary.words_rejected,
        },
        "rules": [
            {
                "rule_id": rule.rule_id,
                "schemes": list(rule.schemes),
                "uncertain": rule.uncertain,
                "citation": rule.citation,
                "statement": rule.statement,
            }
            for rule in MERGE_RULES
        ],
        "schemes": schemes,
        "syllables": _public(syllables),
        "words": _public(words),
        "syllable_structure_index": structure_index(
            float(syllables["h2_conditional_mle"]),
            float(summarize(syllable_shuffle)["h2_conditional_mle"]),
        ),
        "word_structure_index": structure_index(
            float(words["h2_conditional_mle"]),
            float(summarize(word_shuffle)["h2_conditional_mle"]),
        ),
        "syllable_word_edges": _word_edges(primary),
        "gate_schemes": list(GATE_SCHEMES),
        "alignment_triggered": triggered,
        "alignments": alignments,
        "reading": None,
        "plots": {
            "heaps": {
                "Round 1 stems": _heaps_points(blocks["stem"]),
                "Barthel families": _heaps_points(blocks["barthel_families"]),
                "Pozdniakov 2007": _heaps_points(blocks["pozdniakov_2007"]),
                "Horley 2005": _heaps_points(blocks["horley_2005"]),
                "Rapanui syllables": _heaps_points(syllables),
                "Rapanui words": _heaps_points(words),
            }
        },
    }


def _word_syllable_groups(primary: Any) -> list[list[str]]:
    from decipherment.rapanui import syllabify_word

    groups: list[list[str]] = []
    for line in primary.word_lines:
        for word in line:
            parsed = syllabify_word(word, primary.orthography)
            if parsed:
                groups.append(parsed)
    return groups


def _word_edges(primary: Any) -> dict[str, Any]:
    from decipherment.metrics import word_edge_profile

    profile = word_edge_profile(_word_syllable_groups(primary))
    profile["boundary"] = "orthographic word"
    return profile


def _fmt(value: Any, digits: int = 3) -> str:
    if value is None:
        return "—"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def _rule_table(result: dict[str, Any]) -> str:
    lines = [
        "| Rule | Schemes | Uncertain | What it does |",
        "|---|---|---|---|",
    ]
    for rule in result["rules"]:
        schemes = ", ".join(f"`{item}`" for item in rule["schemes"])
        flag = "yes" if rule["uncertain"] else "no"
        lines.append(
            f"| `{rule['rule_id']}` | {schemes} | {flag} | {rule['statement']} |"
        )
    return "\n".join(lines)


def _citation_list(result: dict[str, Any]) -> str:
    lines = []
    for rule in result["rules"]:
        lines.append(f"- `{rule['rule_id']}`: {rule['citation']}")
    return "\n".join(lines)


_SCHEME_LABELS = {
    "stem": "Round 1 stems",
    "ligature_atomic": "Ligatures kept whole",
    "barthel_suffix_only": "Barthel suffixes only",
    "barthel_families": "Barthel families",
    "barthel_families_whole": "Barthel families, ligatures whole",
    "pozdniakov_2007": "Pozdniakov 2007",
    "pozdniakov_2007_whole": "Pozdniakov 2007, ligatures whole",
    "pozdniakov_1996_gaping_mouth": "Pozdniakov 1996 gaping-mouth",
    "horley_2005": "Horley 2005",
    "horley_2005_whole": "Horley 2005, ligatures whole",
}


def _compare_table(result: dict[str, Any]) -> str:
    header = (
        "| Scheme | Ligatures split | Tokens | Types | β | V(2000) | h2 | "
        "Structure | Track 2 label | Gate |"
    )
    rule = "|---|---|---:|---:|---:|---:|---:|---:|---|---|"
    body = []
    order = list(_SCHEME_LABELS)
    for scheme_id in order:
        record = result["schemes"][scheme_id]
        split = "yes" if record["decompose_ligatures"] else "no"
        v2000 = record["heaps_at"].get("2000")
        if record["gate"] is None:
            gate = "baseline"
        elif record["gate"]["passes"]:
            gate = "pass"
        else:
            gate = "no"
        body.append(
            "| "
            + " | ".join(
                [
                    _SCHEME_LABELS[scheme_id],
                    split,
                    str(record["tokens"]),
                    str(record["inventory"]),
                    _fmt(record["heaps_beta"]),
                    _fmt(v2000, 0) if v2000 is not None else "—",
                    _fmt(record["h2_conditional_mle"]),
                    _fmt(record["structure_index"]),
                    record["track2_label"],
                    gate,
                ]
            )
            + " |"
        )
    syllables = result["syllables"]
    words = result["words"]
    body.append(
        "| Rapanui syllables | — | "
        + " | ".join(
            [
                str(syllables["tokens"]),
                str(syllables["inventory"]),
                _fmt(syllables["heaps_beta"]),
                _fmt(syllables["heaps_at"].get("2000"), 0),
                _fmt(syllables["h2_conditional_mle"]),
                _fmt(result["syllable_structure_index"]),
                "—",
                "baseline",
            ]
        )
        + " |"
    )
    body.append(
        "| Rapanui words | — | "
        + " | ".join(
            [
                str(words["tokens"]),
                str(words["inventory"]),
                _fmt(words["heaps_beta"]),
                "—",
                _fmt(words["h2_conditional_mle"]),
                _fmt(result["word_structure_index"]),
                "—",
                "baseline",
            ]
        )
        + " |"
    )
    return "\n".join([header, rule, *body])


def _verdict_paragraph(result: dict[str, Any]) -> str:
    triggered = result["alignment_triggered"]
    stem = result["schemes"]["stem"]["inventory"]
    barthel = result["schemes"]["barthel_families"]["inventory"]
    suffix = result["schemes"]["barthel_suffix_only"]["inventory"]
    pozd = result["schemes"]["pozdniakov_2007"]["inventory"]
    horley = result["schemes"]["horley_2005"]["inventory"]
    gaping = result["schemes"]["pozdniakov_1996_gaping_mouth"]["inventory"]
    if triggered:
        names = ", ".join(_SCHEME_LABELS[scheme_id] for scheme_id in triggered)
        return (
            f"**Verdict: hypothesis only.** {names} landed in the pre-registered "
            f"syllabary band ({SYLLABARY_TYPE_MIN}–{SYLLABARY_TYPE_MAX} types, "
            f"Heaps β ≤ {HEAPS_BETA_MAX}, and at least {EARLY_INVENTORY_MIN:.0%} of "
            f"the inventory present by token {EARLY_N}). The frequency and positional "
            "pairings below are a hypothesis. They are not readings. `reading` is None."
        )
    return (
        f"**Verdict: still not a syllabary.** Cited merges do not bring the sign list "
        f"into the {SYLLABARY_TYPE_MIN}–{SYLLABARY_TYPE_MAX} band, and the curves do not "
        f"flatten the way the Thomson syllables do. Round 1 stems: {stem} types. "
        f"Barthel's own suffix rules, with the index letters he used to keep signs apart: "
        f"{suffix} types. Round 1 had stripped those index letters, which is why its "
        f"inventory is the smaller one. The same suffix rules plus Guy's uncertain "
        f"catalog corrections: {barthel} types. Pozdniakov's published "
        f"hand merges, ligatures split, no residual bin: {pozd} types. The uncertain "
        f"1996 hundreds-digit rewrite of series 300 and 400: {gaping} types. Horley's "
        f"explicit (uncertain) equivalences and decompositions: {horley} types. "
        "The frequency alignment against Rapanui syllables was not run. No sign is paired "
        "with a syllable. `reading` is None."
    )


def render_round2_tracka(result: dict[str, Any]) -> str:
    """Markdown note. Numbers come from ``run_round2_tracka``."""
    stem = result["schemes"]["stem"]
    syllables = result["syllables"]
    words = result["words"]
    pozd = result["schemes"]["pozdniakov_2007"]
    primary = result["primary_rapanui"]
    edges = result["syllable_word_edges"]
    lines = [
        "# Round 2, Track A: merge sign variants and rerun the syllabary test",
        "",
        _verdict_paragraph(result),
        "",
        "This is a statistical comparison of the vendored Barthel corpus with the Thomson 1891 "
        "Rapanui sample used in Track 2. It is not a decipherment.",
        "",
        "## Corpus",
        "",
        "Barthel numbers are the Kohaumotu HTML under `tests/fixtures`, the same sides as "
        f"Track 2 ({result['side_count']} sides). Illegible `000` is dropped. Parenthetical "
        "lacunae are dropped. The Rapanui sample is Thomson 1891, love song excluded, "
        f"orthography `{primary['orthography']}` "
        f"({primary['syllables']} syllables, {primary['words']} words, "
        f"{primary['words_rejected']} words rejected). "
        "Wikipedia spans are not added. Details and the chant source notes are in "
        "`docs/decipherment/track2_syllabary_test.md` and `data/rapanui/SOURCES.md`.",
        "",
        f"Round 1 stem baseline on this run: {stem['tokens']} tokens, {stem['inventory']} types, "
        f"Heaps β {_fmt(stem['heaps_beta'])}. "
        f"Syllables: {syllables['tokens']} tokens, {syllables['inventory']} types, "
        f"β {_fmt(syllables['heaps_beta'])}. "
        f"Words: {words['tokens']} tokens, {words['inventory']} types, "
        f"β {_fmt(words['heaps_beta'])}. "
        f"The (C)V ceiling used in Track 2 is {result['phonological_cv_ceiling']}.",
        "",
        "## Merge rules",
        "",
        "Each scheme is a switch in `decipherment.allographs.encode_scheme_lines`. "
        "Ligature decomposition is a separate switch. A dot or a colon splits "
        "`606.076` into `606` and `076`, and `999.440.076` into `999`, `440`, and `076`. "
        "With the switch off, those stay one token, and one-to-one maps still rewrite "
        "each component. Stacks are not reordered.",
        "",
        "Barthel's hundreds digit is a head class (0–1 geometric, 2 ears, 3–4 open mouth, "
        "5 miscellaneous, 6 beak, 7 other animals), and the tens and units digits are limb "
        "shapes (Barthel 1958: 40–41; Guy 2006). That is a classification, not an allograph "
        "merge. This track does not collapse every code in a hundreds series into one sign. "
        "The one hundreds-digit rewrite that is run is Pozdniakov's 1996 proposal, on its "
        "own scheme, and it is marked uncertain because the 2007 inventory still lists "
        "380 and 400 separately.",
        "",
        "Barthel 1971's figure of about 120 unanalyzable elements was not published as a "
        "list and is not reconstructed. Pozdniakov's claim that 52 glyphs cover 99.7% of "
        "the corpus (staff excluded) depends on a merge table that was not published. "
        "Signs outside the published basic list are left as themselves. They are not "
        "folded into a residual bin. Track 2's `pozdniakov_52` mode did that collapse "
        "and is not repeated here.",
        "",
        _rule_table(result),
        "",
        "### Citations",
        "",
        _citation_list(result),
        "",
        "## Inventory, entropy, and shuffled controls",
        "",
        "Heaps β is the OLS slope of log(types) on log(tokens) for n ≥ 50, the same "
        "definition as Track 2. h2 is H(next | previous) inside lines (Rao et al., "
        "Science 2009). The structure index is `1 - h2(text) / h2(shuffle)` on the "
        "unsmoothed conditional entropy. The shuffle keeps the inventory, the line "
        "lengths, and the token frequencies (seed 0). "
        f"Syllable structure index {_fmt(result['syllable_structure_index'])}. "
        f"Word structure index {_fmt(result['word_structure_index'])}.",
        "",
        "The Track 2 label uses `classify_writing_system` unchanged: non-linguistic if "
        "the structure index is below 0.05 or above 0.85; otherwise syllabic if, at the "
        "shared token count, types ≤ 120 and the ratio to the syllable inventory ≤ 1.6; "
        "otherwise logographic if types ≥ 250 and the ratio to the word inventory ≥ 0.7; "
        "otherwise mixed. That label is not the gate for the alignment. "
        "Whole ligatures are labeled logographic because, at 1,591 tokens, the compound "
        "inventory is already in the word band. The label describes that size.",
        "",
        _compare_table(result),
        "",
        "![Inventory growth under the cited merges](figures/round2_trackA_heaps.svg)",
        "",
        "### Gate",
        "",
        f"A scheme enters the syllabary comparison only if it has {SYLLABARY_TYPE_MIN}–"
        f"{SYLLABARY_TYPE_MAX} types, Heaps β ≤ {HEAPS_BETA_MAX}, and at least "
        f"{EARLY_INVENTORY_MIN:.0%} of its types already seen by token {EARLY_N}. "
        "Those three cuts were set from the requested band and from the Round 1 "
        "syllable curve (49 types, β about 0.14, inventory complete by 2,000 tokens) "
        "and the Round 1 stem curve (β about 0.42). They were not edited after the "
        "merged counts were known. A residual bin cannot pass, because it manufactures "
        "the type count.",
        "",
        _gate_lines(result),
        "",
        "## Position",
        "",
        "Among types with frequency at least 10, the share that occur in initial, "
        "medial, and final position. For signs the boundary is the inscribed line. "
        "For syllables the boundary is the orthographic word. Those are different "
        "boundaries, as in Track 2.",
        "",
        _position_table(result),
        "",
        f"Syllable word-edge rate (frequent types in all three word positions): "
        f"{_fmt(edges['frequent_in_all_three_rate'])} "
        f"({edges['frequent_in_all_three']} of {edges['frequent_types']}).",
        "",
        "## Frequency and positional alignment",
        "",
        _alignment_section(result),
        "",
        "## What this does not claim",
        "",
        "No Barthel code is given a Rapanui syllable, a gloss, or a name. Horley 2005 "
        "also suggested syllable values for a few elements, including a reading of "
        "glyph 200; those values are not used. The 1996 hundreds-digit rewrite is not "
        "Pozdniakov's 2007 inventory. Coverage of the published basic Barthel stems "
        f"after the 2007 hand merges is {_fmt(pozd.get('coverage_of_published_barthel_stems'))}. "
        "That is not 99.7%. Bare `027` is not split into 27a and 27b, because the "
        "undifferentiated code does not say which one it was. One `027b` and the "
        "`027x` forms are kept apart from `027a` only in the Pozdniakov schemes, and "
        "the x-to-27b step is marked uncertain.",
        "",
        "The Track 2 label is a size comparison with the Thomson sample. "
        "Split-ligature rows stay mixed. Whole-ligature rows meet the logographic size gate. "
        "The label does not say what the signs mean. "
        "Thomson's chants are a damaged 19th-century record. Conditional entropy in "
        "the linguistic band is not, by itself, proof of writing (Sproat's critique, "
        "as in Track 2).",
        "",
        f"The run uses `MockProvider` only. Provider calls: {result['provider_calls']}.",
        "",
    ]
    return "\n".join(lines)


def _gate_lines(result: dict[str, Any]) -> str:
    if result["alignment_triggered"]:
        names = ", ".join(f"`{scheme_id}`" for scheme_id in result["alignment_triggered"])
        return f"Schemes that pass: {names}."
    checked = ", ".join(f"`{scheme_id}`" for scheme_id in result["gate_schemes"])
    return f"None of {checked} pass. The alignment is not run."


def _position_table(result: dict[str, Any]) -> str:
    lines = [
        "| Scheme | Frequent types | In all three line positions |",
        "|---|---:|---:|",
    ]
    for scheme_id, label in _SCHEME_LABELS.items():
        position = result["schemes"][scheme_id]["position"]
        lines.append(
            f"| {label} | {position['frequent_types']} | {_fmt(position['frequent_in_all_three_rate'])} |"
        )
    return "\n".join(lines)


def _alignment_section(result: dict[str, Any]) -> str:
    if not result["alignment_triggered"]:
        return (
            "Not run. The pre-registered rule is to align frequencies and positions "
            "only if a cited scheme is inside the syllabary band and its inventory "
            "curve flattens. None did. Track 2 already scored an unmerged stem "
            "alignment and did not adopt it; that score is not reused as a reading here."
        )
    chunks = [
        "Run only for schemes that passed the gate. Each pairing is rank order, "
        "not a decipherment. The null is a random bijection of the same two lists "
        f"({200} permutations). Adoption of Track 2's cosine rule "
        f"(null fraction ≤ {ADOPT_NULL_FRACTION}) is still not a reading, and "
        "`adopted` is left false on purpose: this track does not assign values.",
        "",
    ]
    for scheme_id, payload in result["alignments"].items():
        frequency = payload["frequency"]
        positional = payload["positional"]
        chunks.append(f"### {_SCHEME_LABELS[scheme_id]}")
        chunks.append("")
        chunks.append(
            f"Transition cosine {_fmt(frequency['cosine'])}. "
            f"Fraction of bijections at least that high: {_fmt(frequency['cosine_null_ge_fraction'])}. "
            f"Self-repetition Spearman {_fmt(frequency['repetition_spearman'])}. "
            f"Null fraction {_fmt(frequency['repetition_null_ge_fraction'])}. "
            f"Initial-position Spearman {_fmt(positional['initial_spearman'])}. "
            f"Null fraction {_fmt(positional['initial_null_ge_fraction'])}. "
            "Sign edges are inscribed lines; syllable edges are words. "
            "`reading` is None."
        )
        chunks.append("")
        chunks.append("| Rank | Sign | Syllable (hypothesis) |")
        chunks.append("|---:|---|---|")
        for pair in frequency["pairs"]:
            chunks.append(f"| {pair['rank']} | `{pair['sign']}` | `{pair['syllable']}` |")
        chunks.append("")
    return "\n".join(chunks)


def write_round2_outputs(result: dict[str, Any], docs_dir: Any) -> None:
    """Write the note and the Heaps figure."""
    from pathlib import Path

    from decipherment.report import _svg_chart

    docs = Path(docs_dir)
    figures = docs / "figures"
    figures.mkdir(parents=True, exist_ok=True)
    (docs / "round2_trackA_variant_merge.md").write_text(
        render_round2_tracka(result),
        encoding="utf-8",
    )
    _svg_chart(
        figures / "round2_trackA_heaps.svg",
        result["plots"]["heaps"],
        "n",
        "types",
        "Inventory growth after cited allograph merges",
        "tokens",
        "types",
        log_x=True,
        log_y=True,
    )
