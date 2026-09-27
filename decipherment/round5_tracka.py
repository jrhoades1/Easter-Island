"""Round 5 Track A: held-out confirmation of the Round 4 pictograph results.

The split, the tests, the nulls, the seeds, and the Holm family are fixed in
``docs/decipherment/round5a_preregistration.md``. That file was committed
before these scores were computed. R1 and ``class_of`` are imported from
Round 4 and are not retuned. ``MockProvider`` is accepted and never called.
A pass is not a translation: ``reading`` stays None.
"""

from __future__ import annotations

import json
import random
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from agents.base.providers import MockProvider
from decipherment.old_rapanui import cv_syllables_mapped, load_churchill_headwords
from decipherment.round2_trackb import load_lines
from decipherment.round4_tracka import (
    TESTABLE_CLASSES,
    _classify_pairs,
    _language,
    _pair_counts,
    _r1_words,
    class_of,
    windows_in,
)
from decipherment.track_c_parallels import JSON_PATH as SUBSTITUTION_JSON
from decipherment.track_c_parallels import load_side_texts, smith_waterman

REPO_ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = REPO_ROOT / "docs" / "decipherment" / "round5a_preregistration.md"
OUT_JSON = REPO_ROOT / "data" / "decipherment" / "round5a_heldout_pictograph.json"
OUT_MD = REPO_ROOT / "docs" / "decipherment" / "round5a_heldout_pictograph.md"
ROUND4_JSON = REPO_ROOT / "data" / "decipherment" / "round4a_pictograph_rebus.json"
STEMMA_JSON = REPO_ROOT / "data" / "decipherment" / "round4d_dating_stemma.json"

TRIALS = 500
ALPHA = 0.05
REBUS_SHUFFLE_SEED = 50
NOUN_MAP_SEED = 51
TWO_APART_SEED = 52
BIRD_LABEL_SEED = 53
BIRD_SIGN_SEED = 54
MIN_POOL = 8
SIGN_ORDER = ("006", "040", "143", "152", "200", "600", "680", "700")
# Corrected from the passage graph before any held-out score. See the plan.
EXPECTED_DISCOVERY = ("A", "B", "C", "E", "G", "H", "K", "P", "Q", "R")
EXPECTED_HELDOUT = ("D", "F", "I", "J", "L", "M", "N", "O", "S", "T", "U", "V", "W")
STEMMA_EDGES = (("G", "K"), ("H", "P"), ("H", "Q"), ("P", "Q"))

# Closed class frozen in the pre-registration. Not imported from a live list,
# so a later edit to the particle set cannot change this null.
CLOSED_CLASS = frozenset(
    {
        "a", "e", "i", "o", "u", "te", "ki", "ka", "ko", "ku", "ma", "mo", "me",
        "no", "na", "ni", "ra", "re", "ri", "ro", "ru", "he", "hai", "atu",
        "mai", "ana", "ai",
        "au", "maua", "matou", "taua", "tatou", "koe", "korua", "ia", "raua",
        "hoki", "ina",
    }
)

ROUND4_FAMILY_IDS = (
    "r4_neighbor_sum",
    "r4_neighbor_moon",
    "r4_neighbor_hand",
    "r4_neighbor_bird",
    "r4_neighbor_sea",
    "r4_neighbor_human",
    "r4_neighbor_human_gaping",
    "r4_two_apart_sum",
    "r4_calendar_neighbor_sum",
    "r4_calendar_two_apart_sum",
    "r4_cross_hundred",
    "r4_r1_hits",
    "r4_r1_diverse",
    "r4_r1_calendar",
    "r4_r1_gv6",
    "r4_r1_parallels",
    "r4_r2_hits",
    "r4_r2_diverse",
    "r4_r2_calendar",
    "r4_r2_gv6",
    "r4_r2_parallels",
)


def block_shuffle(row: Iterable[str], rng: random.Random) -> list[str]:
    """Shuffle a line by maximal runs. A repeated sign stays glued together."""
    blocks: list[tuple[str, int]] = []
    for stem in row:
        if blocks and blocks[-1][0] == stem:
            sign, count = blocks[-1]
            blocks[-1] = (sign, count + 1)
        else:
            blocks.append((stem, 1))
    rng.shuffle(blocks)
    shuffled: list[str] = []
    for sign, count in blocks:
        shuffled.extend([sign] * count)
    return shuffled


def frequency_bin(count: int) -> int:
    """Running-text bins from the pre-registration. Not retuned."""
    if count <= 0:
        return 0
    if count <= 20:
        return 1
    if count <= 100:
        return 2
    if count <= 300:
        return 3
    return 4


def _add_one(null_ge: int, trials: int = TRIALS) -> float:
    return (null_ge + 1) / (trials + 1)


def _effect(observed: int, draws: list[int]) -> dict[str, Any]:
    count = len(draws)
    mean = (sum(draws) / count) if count else 0.0
    variance = (sum((value - mean) ** 2 for value in draws) / count) if count else 0.0
    sd = variance ** 0.5
    effect = ((observed - mean) / sd) if sd > 0 else None
    null_ge = sum(1 for value in draws if value >= observed)
    return {
        "observed": observed,
        "trials": count,
        "null_ge": null_ge,
        "null_fraction": (null_ge / count) if count else 0.0,
        "p_add_one": _add_one(null_ge, count) if count else 1.0,
        "null_mean": mean,
        "null_sd": sd,
        "effect_size": effect,
        "null_min": min(draws) if draws else None,
        "null_max": max(draws) if draws else None,
    }


def _find(parent: dict[str, str], tablet: str) -> str:
    root = tablet
    while parent[root] != root:
        root = parent[root]
    while parent[tablet] != root:
        parent[tablet], tablet = root, parent[tablet]
    return root


def split_tablets(
    passages: list[dict[str, Any]],
    tablets: Iterable[str],
) -> dict[str, Any]:
    """Discovery is the parallel component with the most significant passages."""
    names = sorted(set(tablets))
    parent = {name: name for name in names}
    for passage in passages:
        left = passage["left"]["tablet"]
        right = passage["right"]["tablet"]
        if left not in parent or right not in parent or left == right:
            continue
        left_root = _find(parent, left)
        right_root = _find(parent, right)
        if left_root != right_root:
            parent[right_root] = left_root
    groups: dict[str, list[str]] = {}
    for name in names:
        groups.setdefault(_find(parent, name), []).append(name)
    components = [tuple(sorted(members)) for members in groups.values()]

    def passage_count(members: tuple[str, ...]) -> int:
        member_set = set(members)
        total = 0
        for passage in passages:
            left = passage["left"]["tablet"]
            right = passage["right"]["tablet"]
            if left != right and left in member_set and right in member_set:
                total += 1
        return total

    ranked = sorted(components, key=lambda members: (-passage_count(members), members))
    discovery = ranked[0]
    discovery_set = set(discovery)
    heldout = tuple(name for name in names if name not in discovery_set)
    shared = []
    for passage in passages:
        left = passage["left"]["tablet"]
        right = passage["right"]["tablet"]
        if left == right:
            continue
        left_in = left in discovery_set
        right_in = right in discovery_set
        if left_in != right_in:
            shared.append(passage["id"])
    split_edges = []
    for left, right in STEMMA_EDGES:
        if (left in discovery_set) != (right in discovery_set):
            split_edges.append(f"{left}–{right}")
    return {
        "discovery": discovery,
        "heldout": heldout,
        "components": [
            {"tablets": list(members), "significant_passages": passage_count(members)}
            for members in ranked
            if passage_count(members) > 0 or len(members) > 1
        ],
        "shared_passage_ids": shared,
        "split_stemma_edges": split_edges,
    }


def _significant_passages() -> list[dict[str, Any]]:
    payload = json.loads(SUBSTITUTION_JSON.read_text(encoding="utf-8"))
    return [item for item in payload["stem"]["passages"] if item.get("significant")]


def _check_split(split: dict[str, Any]) -> None:
    if tuple(split["discovery"]) != EXPECTED_DISCOVERY or tuple(split["heldout"]) != EXPECTED_HELDOUT:
        raise RuntimeError(
            "Split "
            f"discovery {split['discovery']} held-out {split['heldout']} "
            f"is not the pre-registered discovery {EXPECTED_DISCOVERY} "
            f"held-out {EXPECTED_HELDOUT}. No p-value was computed."
        )
    if split["shared_passage_ids"] or split["split_stemma_edges"]:
        raise RuntimeError(
            "The split shares a parallel or cuts a stemma edge. No p-value was computed. "
            f"Passages {split['shared_passage_ids']}. Edges {split['split_stemma_edges']}."
        )


def _later_copy_drops(
    passages: list[dict[str, Any]],
    heldout: set[str],
) -> set[tuple[str, int]]:
    """Drop the alphabetically later copy inside a held-out parallel."""
    dropped: set[tuple[str, int]] = set()
    for passage in passages:
        left = passage["left"]
        right = passage["right"]
        if left["tablet"] not in heldout or right["tablet"] not in heldout:
            continue
        if left["tablet"] == right["tablet"]:
            continue
        locus = left if left["tablet"] > right["tablet"] else right
        # Round 4 reads start through end inclusive.
        for index in range(int(locus["start"]), int(locus["end"]) + 1):
            dropped.add((locus["side"], index))
    return dropped


def _heldout_rows(
    heldout: set[str],
    dropped: set[tuple[str, int]],
) -> tuple[list[list[str]], int]:
    rows: list[list[str]] = []
    removed = 0
    for text in load_side_texts("stem"):
        if text.tablet not in heldout:
            continue
        for _name, start, end in text.spans:
            row: list[str] = []
            for index in range(start, end):
                if (text.side, index) in dropped:
                    removed += 1
                    if row:
                        rows.append(row)
                        row = []
                    continue
                row.append(text.signs[index])
            if row:
                rows.append(row)
    return rows, removed


def _window_is_hit(
    gram: tuple[str, ...],
    syllables: dict[str, tuple[str, ...]],
    shapes: set[tuple[str, ...]],
    formulae: dict[int, Counter[tuple[tuple[str, ...], ...]]],
) -> bool:
    parts = tuple(syllables[sign] for sign in gram)
    flat = tuple(piece for part in parts for piece in part)
    bucket = formulae.get(len(gram))
    phrase_count = bucket.get(parts, 0) if bucket else 0
    return flat in shapes or phrase_count >= 1


def mixed_word_hits(
    windows: list[tuple[str, ...]],
    words: dict[str, str],
    syllables: dict[str, tuple[str, ...]],
    shapes: set[tuple[str, ...]],
    formulae: dict[int, Counter[tuple[tuple[str, ...], ...]]],
) -> dict[str, Any]:
    """Hits among windows that are neither pure repeats nor doubled words."""
    hits = 0
    eligible = 0
    pure_repeats = 0
    doubled_words = 0
    examples: Counter[str] = Counter()
    for gram in windows:
        if len(set(gram)) < 2:
            pure_repeats += 1
            continue
        labels = [words[sign] for sign in gram]
        if len(labels) != len(set(labels)):
            doubled_words += 1
            continue
        eligible += 1
        if not _window_is_hit(gram, syllables, shapes, formulae):
            continue
        hits += 1
        examples[" ".join(labels)] += 1
    return {
        "mapped_windows": len(windows),
        "pure_sign_repeats": pure_repeats,
        "doubled_word_windows": doubled_words,
        "eligible_windows": eligible,
        "hits": hits,
        "hit_rate": (hits / eligible) if eligible else 0.0,
        "examples": [
            {"phrase": phrase, "windows": count}
            for phrase, count in examples.most_common(12)
        ],
    }


def _syllables_for(words: dict[str, str]) -> dict[str, tuple[str, ...]]:
    parsed = {sign: cv_syllables_mapped(word) for sign, word in words.items()}
    missing = [sign for sign, syllables in parsed.items() if not syllables]
    if missing:
        raise ValueError(f"rebus word is not mapped (C)V for {missing}")
    return {sign: syllables for sign, syllables in parsed.items() if syllables}


def _content_catalog(
    word_counts: dict[str, int],
) -> list[dict[str, Any]]:
    """One Churchill headword per mapped pronunciation, closed class removed.

    The vocabulary file has no part of speech. This is the pre-registered
    proxy for a noun list, not a gloss-checked noun list.
    """
    chosen: dict[tuple[str, ...], str] = {}
    for item in load_churchill_headwords():
        if item.word in CLOSED_CLASS:
            continue
        parsed = cv_syllables_mapped(item.word)
        if not parsed:
            continue
        previous = chosen.get(parsed)
        if previous is None or item.word < previous:
            chosen[parsed] = item.word
    catalog = []
    for syllables, word in sorted(chosen.items(), key=lambda pair: pair[1]):
        key = "".join(syllables)
        count = int(word_counts.get(key, 0))
        catalog.append(
            {
                "word": word,
                "syllables": list(syllables),
                "length": len(syllables),
                "running_text_count": count,
                "bin": frequency_bin(count),
            }
        )
    return catalog


def _pools_for(
    words: dict[str, str],
    word_counts: dict[str, int],
    catalog: list[dict[str, Any]],
) -> dict[str, Any]:
    pools: dict[str, list[str]] = {}
    report = []
    for sign in SIGN_ORDER:
        target = words[sign]
        syllables = cv_syllables_mapped(target)
        if not syllables:
            raise ValueError(f"R1 word {target!r} is not mapped (C)V")
        target_bin = frequency_bin(int(word_counts.get("".join(syllables), 0)))
        target_length = len(syllables)
        bins = [target_bin]
        radius = 0
        while True:
            allowed = set(bins)
            pool = [
                row["word"]
                for row in catalog
                if row["length"] == target_length and row["bin"] in allowed
            ]
            if len(pool) >= MIN_POOL or radius >= 4:
                break
            radius += 1
            if target_bin - radius >= 0:
                bins.append(target_bin - radius)
            if target_bin + radius <= 4:
                bins.append(target_bin + radius)
        if not pool:
            raise RuntimeError(f"Noun pool for {sign} is empty. No map was drawn.")
        pools[sign] = pool
        report.append(
            {
                "sign": sign,
                "word": target,
                "length": target_length,
                "target_bin": target_bin,
                "bins_used": sorted(set(bins)),
                "pool_size": len(pool),
                "expanded": bins != [target_bin],
            }
        )
    return {"by_sign": report, "pools": pools}


def _draw_map(
    rng: random.Random,
    pools: dict[str, list[str]],
) -> tuple[dict[str, str], bool]:
    used: set[str] = set()
    assignment: dict[str, str] = {}
    replaced = False
    for sign in SIGN_ORDER:
        available = [word for word in pools[sign] if word not in used]
        if not available:
            available = list(pools[sign])
            replaced = True
        assignment[sign] = rng.choice(available)
        used.add(assignment[sign])
    return assignment, replaced


def _slice(signs: tuple[str, ...], start: int, end: int) -> list[str]:
    """``start`` through ``end`` inclusive, matching Round 4 Track A."""
    return list(signs[start : end + 1])


def _heldout_slices(
    passages: list[dict[str, Any]],
    texts: dict[str, Any],
    heldout: set[str],
) -> list[tuple[list[str], list[str]]]:
    slices = []
    for passage in passages:
        left = passage["left"]
        right = passage["right"]
        if left["tablet"] not in heldout or right["tablet"] not in heldout:
            continue
        seq_a = _slice(texts[left["side"]].signs, int(left["start"]), int(left["end"]))
        seq_b = _slice(texts[right["side"]].signs, int(right["start"]), int(right["end"]))
        if seq_a and seq_b:
            slices.append((seq_a, seq_b))
    return slices


def _mismatch_pairs(seq_a: list[str], seq_b: list[str]) -> list[tuple[str, str]]:
    _score, _a0, _a1, _b0, _b1, columns = smith_waterman(seq_a, seq_b)
    pairs = []
    for sign_a, sign_b in columns:
        if sign_a is None or sign_b is None or sign_a == sign_b:
            continue
        pairs.append((sign_a, sign_b))
    return pairs


def _cross_breakdown(pairs: list[tuple[str, str]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for left, right in pairs:
        left_class = class_of(left)
        right_class = class_of(right)
        if left_class is None or left_class != right_class:
            continue
        if not left.isdigit() or not right.isdigit():
            continue
        if int(left) // 100 == int(right) // 100:
            continue
        counts[left_class] += 1
    return dict(counts)


def holm_adjust(rows: list[dict[str, Any]], alpha: float = ALPHA) -> list[dict[str, Any]]:
    """Holm 1979. Ties break on the id so the adjustment does not move."""
    ordered = sorted(rows, key=lambda row: (row["p_add_one"], row["id"]))
    family_size = len(ordered)
    running = 0.0
    adjusted: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(ordered):
        step = min(1.0, (family_size - index) * row["p_add_one"])
        running = max(running, step)
        updated = dict(row)
        updated["family_size"] = family_size
        updated["holm_rank"] = index + 1
        updated["holm_p"] = min(1.0, running)
        updated["survives_holm"] = updated["holm_p"] <= alpha
        adjusted[row["id"]] = updated
    return [adjusted[row["id"]] for row in rows]


def _round4_family(payload: dict[str, Any]) -> list[dict[str, Any]]:
    semantic = payload["semantic_cooccurrence"]
    outside = payload["semantic_cooccurrence_calendar_removed"]
    r1 = payload["rebus_r1"]
    r2 = payload["rebus_r2"]
    rows: list[dict[str, Any]] = [
        {"id": "r4_neighbor_sum", "p_add_one": semantic["p_add_one"], "round": 4},
    ]
    by_class = {item["class"]: item["p_add_one"] for item in semantic["by_class"]}
    for name in TESTABLE_CLASSES:
        rows.append({"id": f"r4_neighbor_{name}", "p_add_one": by_class[name], "round": 4})
    rows.extend(
        [
            {"id": "r4_two_apart_sum", "p_add_one": semantic["step2"]["p_add_one"], "round": 4},
            {"id": "r4_calendar_neighbor_sum", "p_add_one": outside["p_add_one"], "round": 4},
            {
                "id": "r4_calendar_two_apart_sum",
                "p_add_one": outside["step2"]["p_add_one"],
                "round": 4,
            },
            {
                "id": "r4_cross_hundred",
                "p_add_one": payload["parallel_slots"]["cross_hundred"]["p_add_one"],
                "round": 4,
            },
            {"id": "r4_r1_hits", "p_add_one": r1["p_add_one"], "round": 4},
            {"id": "r4_r1_diverse", "p_add_one": r1["diverse_p_add_one"], "round": 4},
        ]
    )
    for item in r1["contexts"]:
        rows.append({"id": f"r4_r1_{item['context']}", "p_add_one": item["p_add_one"], "round": 4})
    rows.extend(
        [
            {"id": "r4_r2_hits", "p_add_one": r2["p_add_one"], "round": 4},
            {"id": "r4_r2_diverse", "p_add_one": r2["diverse_p_add_one"], "round": 4},
        ]
    )
    for item in r2["contexts"]:
        rows.append({"id": f"r4_r2_{item['context']}", "p_add_one": item["p_add_one"], "round": 4})
    ids = tuple(row["id"] for row in rows)
    if ids != ROUND4_FAMILY_IDS:
        raise RuntimeError(f"Round 4 family ids drifted: {ids}")
    return rows


def _verdict(family: list[dict[str, Any]], bird_available: bool) -> dict[str, Any]:
    by_id = {row["id"]: row for row in family}

    def survives(test_id: str) -> bool:
        return bool(by_id[test_id]["survives_holm"])

    rebus = survives("r5_rebus_sign_shuffle") and survives("r5_rebus_noun_map")
    two_apart = survives("r5_two_apart_sign_shuffle")
    if not bird_available:
        bird = "not_tested"
    elif survives("r5_bird_label_shuffle") and survives("r5_bird_sign_shuffle"):
        bird = "survives"
    else:
        bird = "dies"
    package = "survives" if rebus and two_apart and bird != "dies" else "dies"
    return {
        "rebus": "survives" if rebus else "dies",
        "two_apart": "survives" if two_apart else "dies",
        "bird": bird,
        "package": package,
    }


def _rate_summary(draws: list[int], eligible: list[int]) -> dict[str, float]:
    rates = [(hits / windows) if windows else 0.0 for hits, windows in zip(draws, eligible)]
    mean_rate = (sum(rates) / len(rates)) if rates else 0.0
    mean_eligible = (sum(eligible) / len(eligible)) if eligible else 0.0
    return {"null_mean_rate": mean_rate, "null_mean_eligible": mean_eligible}


def run_round5_tracka(provider: MockProvider | None = None) -> dict[str, Any]:
    """Run the pre-registered held-out tests. The provider is not called."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Round 5 Track A accepts MockProvider only")

    passages = _significant_passages()
    tablets = [line.tablet for line in load_lines()]
    split = split_tablets(passages, tablets)
    _check_split(split)
    heldout = set(split["heldout"])
    discovery = set(split["discovery"])
    dropped = _later_copy_drops(passages, heldout)
    rows, removed_stems = _heldout_rows(heldout, dropped)
    words = _r1_words()
    if set(words) != set(SIGN_ORDER):
        raise RuntimeError(f"R1 signs {sorted(words)} are not the frozen eight")

    shapes, formulae, word_counts = _language()
    base_syllables = _syllables_for(words)
    observed_windows = []
    for row in rows:
        observed_windows.extend(windows_in(row, set(words)))
    rebus_observed = mixed_word_hits(observed_windows, words, base_syllables, shapes, formulae)
    two_apart_counts = _pair_counts(rows, 2)
    two_apart_observed = sum(two_apart_counts.values())

    texts = {text.side: text for text in load_side_texts("stem")}
    slices = _heldout_slices(passages, texts, heldout)
    observed_pairs: list[tuple[str, str]] = []
    for seq_a, seq_b in slices:
        observed_pairs.extend(_mismatch_pairs(seq_a, seq_b))
    bird_observed = _classify_pairs(observed_pairs, class_of)
    bird_available = bird_observed["cross_hundred_classified"] > 0

    sign_hits: list[int] = []
    sign_eligible: list[int] = []
    sign_rng = random.Random(REBUS_SHUFFLE_SEED)
    for _trial in range(TRIALS):
        shuffled_rows = [block_shuffle(row, sign_rng) for row in rows]
        windows: list[tuple[str, ...]] = []
        for row in shuffled_rows:
            windows.extend(windows_in(row, set(words)))
        scored = mixed_word_hits(windows, words, base_syllables, shapes, formulae)
        sign_hits.append(scored["hits"])
        sign_eligible.append(scored["eligible_windows"])
    rebus_sign = _effect(rebus_observed["hits"], sign_hits)
    rebus_sign.update(_rate_summary(sign_hits, sign_eligible))
    rebus_sign["seed"] = REBUS_SHUFFLE_SEED
    rebus_sign["null"] = "sign shuffle within line, adjacent repeats kept as blocks"

    catalog = _content_catalog(word_counts)
    pool_report = _pools_for(words, word_counts, catalog)
    noun_hits: list[int] = []
    noun_eligible: list[int] = []
    replacements = 0
    noun_rng = random.Random(NOUN_MAP_SEED)
    for _trial in range(TRIALS):
        assignment, replaced = _draw_map(noun_rng, pool_report["pools"])
        replacements += int(replaced)
        trial_syllables = _syllables_for(assignment)
        scored = mixed_word_hits(observed_windows, assignment, trial_syllables, shapes, formulae)
        noun_hits.append(scored["hits"])
        noun_eligible.append(scored["eligible_windows"])
    rebus_noun = _effect(rebus_observed["hits"], noun_hits)
    rebus_noun.update(_rate_summary(noun_hits, noun_eligible))
    rebus_noun["seed"] = NOUN_MAP_SEED
    rebus_noun["replacement_draws"] = replacements
    rebus_noun["null"] = (
        "random same-size maps from the Churchill content-word proxy, "
        "matched on syllable length and running-text bin"
    )

    two_draws: list[int] = []
    two_rng = random.Random(TWO_APART_SEED)
    for _trial in range(TRIALS):
        shuffled_rows = [block_shuffle(row, two_rng) for row in rows]
        two_draws.append(sum(_pair_counts(shuffled_rows, 2).values()))
    two_apart = _effect(two_apart_observed, two_draws)
    two_apart["seed"] = TWO_APART_SEED
    two_apart["by_class"] = [
        {"class": name, "pairs": two_apart_counts[name]} for name in TESTABLE_CLASSES
    ]
    two_apart["null"] = "sign shuffle within line, adjacent repeats kept as blocks"

    bird_label = None
    bird_sign = None
    if bird_available:
        typed = sorted(stem for stem in {sign for pair in observed_pairs for sign in pair} if class_of(stem))
        labels = [class_of(stem) for stem in typed]
        label_draws: list[int] = []
        label_rng = random.Random(BIRD_LABEL_SEED)
        observed_cross = bird_observed["cross_hundred_same_class"]
        for _trial in range(TRIALS):
            shuffled = list(labels)
            label_rng.shuffle(shuffled)
            lookup = dict(zip(typed, shuffled))
            scored = _classify_pairs(observed_pairs, lookup.get)
            label_draws.append(scored["cross_hundred_same_class"])
        bird_label = _effect(observed_cross, label_draws)
        bird_label["seed"] = BIRD_LABEL_SEED
        bird_label["null"] = "permute class labels on classified mismatch stems"
        bird_label["rate"] = (
            observed_cross / bird_observed["cross_hundred_classified"]
            if bird_observed["cross_hundred_classified"]
            else 0.0
        )

        sign_draws: list[int] = []
        sign_rng = random.Random(BIRD_SIGN_SEED)
        for _trial in range(TRIALS):
            pairs: list[tuple[str, str]] = []
            for seq_a, seq_b in slices:
                pairs.extend(
                    _mismatch_pairs(block_shuffle(seq_a, sign_rng), block_shuffle(seq_b, sign_rng))
                )
            sign_draws.append(_classify_pairs(pairs, class_of)["cross_hundred_same_class"])
        bird_sign = _effect(observed_cross, sign_draws)
        bird_sign["seed"] = BIRD_SIGN_SEED
        bird_sign["null"] = "block-shuffle each passage slice, then align again"

    family = _round4_family(json.loads(ROUND4_JSON.read_text(encoding="utf-8")))
    family.append(
        {
            "id": "r5_rebus_sign_shuffle",
            "p_add_one": rebus_sign["p_add_one"],
            "round": 5,
            "observed": rebus_observed["hits"],
        }
    )
    family.append(
        {
            "id": "r5_rebus_noun_map",
            "p_add_one": rebus_noun["p_add_one"],
            "round": 5,
            "observed": rebus_observed["hits"],
        }
    )
    family.append(
        {
            "id": "r5_two_apart_sign_shuffle",
            "p_add_one": two_apart["p_add_one"],
            "round": 5,
            "observed": two_apart_observed,
        }
    )
    if bird_label is not None and bird_sign is not None:
        family.append(
            {
                "id": "r5_bird_label_shuffle",
                "p_add_one": bird_label["p_add_one"],
                "round": 5,
                "observed": bird_observed["cross_hundred_same_class"],
            }
        )
        family.append(
            {
                "id": "r5_bird_sign_shuffle",
                "p_add_one": bird_sign["p_add_one"],
                "round": 5,
                "observed": bird_observed["cross_hundred_same_class"],
            }
        )
    family = holm_adjust(family)
    verdict = _verdict(family, bird_available)
    stemma = json.loads(STEMMA_JSON.read_text(encoding="utf-8"))
    result = {
        "round": 5,
        "track": "A",
        "provider": "mock",
        "provider_calls": 0,
        "reading": None,
        "plan": "docs/decipherment/round5a_preregistration.md",
        "noun_pool_label": (
            "HYPOTHESIS: Churchill 1912 headwords that parse as (C)V, minus the "
            "closed particle and pronoun list in the pre-registration. The vocabulary "
            "file does not mark nouns. One headword is kept per mapped pronunciation, "
            "the first in alphabetical order."
        ),
        "split": {
            "rule": (
                "Discovery is the significant-passage component with the most passages. "
                "Held-out is every other tablet. The alphabetically later copy of a "
                "held-out parallel is removed before the rebus and two-apart counts."
            ),
            "discovery": list(split["discovery"]),
            "heldout": list(split["heldout"]),
            "components_with_passages": split["components"],
            "stemma_newick": stemma["stemma"]["newick"],
            "stemma_edges": [f"{left}–{right}" for left, right in STEMMA_EDGES],
            "later_copy_stems_removed": removed_stems,
            "heldout_lines": len(rows),
            "heldout_stems": sum(len(row) for row in rows),
            "discovery_tablets_not_scored": sorted(discovery),
        },
        "r1": words,
        "rebus": {
            "observed": rebus_observed,
            "sign_shuffle": {key: value for key, value in rebus_sign.items()},
            "noun_map": {key: value for key, value in rebus_noun.items()},
            "pools": pool_report["by_sign"],
            "catalog_size": len(catalog),
            "closed_class_size": len(CLOSED_CLASS),
        },
        "two_apart": two_apart,
        "bird": {
            "available": bird_available,
            "passages": len(slices),
            "classified_mismatch_pairs": bird_observed["classified_mismatch_pairs"],
            "same_class": bird_observed["same_class"],
            "cross_hundred_classified": bird_observed["cross_hundred_classified"],
            "cross_hundred_same_class": bird_observed["cross_hundred_same_class"],
            "by_class": _cross_breakdown(observed_pairs),
            "label_shuffle": bird_label,
            "sign_shuffle": bird_sign,
        },
        "family": [
            {
                "id": row["id"],
                "round": row["round"],
                "p_add_one": row["p_add_one"],
                "holm_rank": row["holm_rank"],
                "holm_p": row["holm_p"],
                "survives_holm": row["survives_holm"],
            }
            for row in sorted(family, key=lambda item: item["holm_rank"])
        ],
        "family_size": len(family),
        "holm_floor_note": (
            "500 draws cannot produce an add-one p smaller than 1/501. "
            "Holm's first cutoff is 0.05 divided by the family size. "
            "A family of 26 or more cannot pass any test at that floor."
        ),
        "verdict": verdict,
        "package": verdict["package"],
    }
    return result


def _fmt(value: float | None, digits: int = 3) -> str:
    if value is None:
        return "—"
    return f"{value:.{digits}f}"


def _yn(flag: bool) -> str:
    return "yes" if flag else "no"


def render_round5_tracka(result: dict[str, Any]) -> str:
    """Plain-English report. Every number is taken from the result."""
    verdict = result["verdict"]
    rebus = result["rebus"]["observed"]
    sign = result["rebus"]["sign_shuffle"]
    noun = result["rebus"]["noun_map"]
    two = result["two_apart"]
    bird = result["bird"]
    package = "survives" if result["package"] == "survives" else "dies"
    if bird["available"]:
        label = bird["label_shuffle"]
        sliced = bird["sign_shuffle"]
        bird_sentence = (
            f"Cross-hundred substitutions on the held-out parallels are "
            f"{bird['cross_hundred_same_class']} of {bird['cross_hundred_classified']} "
            f"(label-shuffle mean {_fmt(label['null_mean'])}, effect {_fmt(label['effect_size'])}, "
            f"add-one p {_fmt(label['p_add_one'], 4)}, Holm p {_fmt(_holm(result, 'r5_bird_label_shuffle'), 4)}; "
            f"slice-shuffle mean {_fmt(sliced['null_mean'])}, effect {_fmt(sliced['effect_size'])}, "
            f"add-one p {_fmt(sliced['p_add_one'], 4)}, Holm p {_fmt(_holm(result, 'r5_bird_sign_shuffle'), 4)})."
        )
    elif bird["passages"] == 0:
        bird_sentence = (
            "Bird-class substitutions were not tested: no significant passage has both tablets "
            "in the held-out set."
        )
    else:
        bird_sentence = (
            "Bird-class substitutions were not tested: the held-out parallels have no "
            "cross-hundred pair in which both signs are classified."
        )
    class_bits = ", ".join(
        f"{name} {count}" for name, count in sorted(bird["by_class"].items())
    ) or "none"
    pool_rows = []
    for row in result["rebus"]["pools"]:
        bins = ", ".join(str(number) for number in row["bins_used"])
        pool_rows.append(
            f"| `{row['sign']}` | {row['word']} | {row['length']} | {row['target_bin']} | {bins} | "
            f"{row['pool_size']} | {_yn(row['expanded'])} |"
        )
    two_rows = []
    for row in two["by_class"]:
        two_rows.append(f"| {row['class']} | {row['pairs']} |")
    family_rows = []
    for row in result["family"]:
        family_rows.append(
            f"| `{row['id']}` | {row['round']} | {_fmt(row['p_add_one'], 4)} | {row['holm_rank']} | "
            f"{_fmt(row['holm_p'], 4)} | {_yn(row['survives_holm'])} |"
        )
    examples = rebus["examples"]
    if examples:
        example_text = ", ".join(f"{item['phrase']} ×{item['windows']}" for item in examples)
    else:
        example_text = "none"
    return f"""# Round 5, Track A — held-out check of the pictograph results

The pictograph package **{package}**. On the held-out tablets ({", ".join(result['split']['heldout'])}), mixed-word rebus hits are {rebus['hits']} on {rebus['eligible_windows']} eligible windows (sign-shuffle mean {_fmt(sign['null_mean'])}, effect {_fmt(sign['effect_size'])}, {sign['null_ge']} of {sign['trials']}, add-one p {_fmt(sign['p_add_one'], 4)}, Holm p {_fmt(_holm(result, 'r5_rebus_sign_shuffle'), 4)}; noun-map mean {_fmt(noun['null_mean'])}, effect {_fmt(noun['effect_size'])}, {noun['null_ge']} of {noun['trials']}, add-one p {_fmt(noun['p_add_one'], 4)}, Holm p {_fmt(_holm(result, 'r5_rebus_noun_map'), 4)}). Same-class signs two apart are {two['observed']} (shuffle mean {_fmt(two['null_mean'])}, effect {_fmt(two['effect_size'])}, {two['null_ge']} of {two['trials']}, add-one p {_fmt(two['p_add_one'], 4)}, Holm p {_fmt(_holm(result, 'r5_two_apart_sign_shuffle'), 4)}). {bird_sentence} The Holm family has {result['family_size']} tests. Nothing here is a translation of a tablet.

Provider: `mock`. Provider calls: {result['provider_calls']}. Reading: none.

Rebus {verdict['rebus']}. Two-apart {verdict['two_apart']}. Bird substitutions: {verdict['bird'].replace('_', ' ')}.

## What was locked

The plan is `{result['plan']}`. It was committed before these counts. R1 stays marama, rakau, omotohi, tangata, manu, makohe, ika, and rima, with `064` copying `006`. The six classes stay the Round 4 classes. No word was added. {result['noun_pool_label']}

Round 4 had already counted these held-out lines inside the corpus-wide shuffles. This is a second look at texts that share no significant passage with the discovery tablets. Holm is applied to the Round 4 pictograph tests and these Round 5 tests together so the second look does not get its own 5% gate. The two Round 4 two-apart rows can still clear Holm, because those counts were taken on the whole corpus. The package rule asks whether the held-out tests clear it. They are the ones that decide survives or dies.

## The split

Discovery, not scored: {", ".join(result['split']['discovery'])}. Held-out: {", ".join(result['split']['heldout'])}. Held-out lines after the copy removal: {result['split']['heldout_lines']}. Held-out stems: {result['split']['heldout_stems']}. Stems removed because they are the later copy of a held-out parallel: {result['split']['later_copy_stems_removed']}. The copying tree used as a check is `{result['split']['stemma_newick']}`.

## Mixed-word rebus

Mapped windows: {rebus['mapped_windows']}. Pure sign repeats left out: {rebus['pure_sign_repeats']}. Doubled-word windows left out: {rebus['doubled_word_windows']}. Eligible windows: {rebus['eligible_windows']}. Hits: {rebus['hits']}. Hit rate: {_fmt(rebus['hit_rate'])}.

The sign shuffle keeps adjacent repeats as blocks and moves those blocks inside the line. Mean hits {_fmt(sign['null_mean'])} (sd {_fmt(sign['null_sd'])}). Effect {_fmt(sign['effect_size'])}. Draws at or above the observed count: {sign['null_ge']} of {sign['trials']}. Mean eligible windows under that shuffle: {_fmt(sign['null_mean_eligible'])}. Mean hit rate: {_fmt(sign['null_mean_rate'])}.

The noun-map null keeps the signs and replaces the eight words with content words of the same syllable length and the same running-text bin, widening the bin only when a slot has fewer than {MIN_POOL} words. Catalog size: {result['rebus']['catalog_size']}. Trials that had to reuse a word because a remaining pool was empty: {noun['replacement_draws']}. Mean hits {_fmt(noun['null_mean'])} (sd {_fmt(noun['null_sd'])}). Effect {_fmt(noun['effect_size'])}. Draws at or above the observed count: {noun['null_ge']} of {noun['trials']}. Mean hit rate: {_fmt(noun['null_mean_rate'])}.

| Sign | R1 word | Syllables | Target bin | Bins used | Pool | Expanded |
| --- | --- | ---: | ---: | --- | ---: | --- |
{chr(10).join(pool_rows)}

Hit windows, R1, after the exclusions: {example_text}.

## Two apart

Observed pairs: {two['observed']}. Shuffle mean {_fmt(two['null_mean'])} (sd {_fmt(two['null_sd'])}). Effect {_fmt(two['effect_size'])}. Draws at or above the observed count: {two['null_ge']} of {two['trials']}. The class rows are a breakdown of that one count. They are not extra Holm tests.

| Class | Pairs |
| --- | ---: |
{chr(10).join(two_rows)}

## Cross-hundred substitutions

Held-out passages aligned: {bird['passages']}. Classified mismatches: {bird['classified_mismatch_pairs']}. Same class, including pairs inside one hundred: {bird['same_class']}. Cross-hundred classified pairs: {bird['cross_hundred_classified']}. Cross-hundred same class: {bird['cross_hundred_same_class']}. By class: {class_bits}.

{bird_sentence}

## Holm

Alpha 0.05. Adjusted p is the running maximum of ``(tests left) × p``, in the order fixed by the plan. A row survives when that adjusted p is at or under 0.05. {result['holm_floor_note']}

| Test | Round | Add-one p | Rank | Holm p | Survives |
| --- | ---: | ---: | ---: | ---: | --- |
{chr(10).join(family_rows)}

## What this does not claim

No tablet is translated. R1 is still a list of cited pictures plus hypotheses, not a decipherment. A neighbor pattern inside Barthel's own series is not an independent identification of a bird or a fish. The noun pool is not a parsed dictionary of nouns. Surviving Holm would still not be a reading, and this run's reading field is empty.
"""


def _holm(result: dict[str, Any], test_id: str) -> float:
    for row in result["family"]:
        if row["id"] == test_id:
            return float(row["holm_p"])
    raise KeyError(test_id)


def write_round5_outputs(result: dict[str, Any]) -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_round5_tracka(result), encoding="utf-8")
