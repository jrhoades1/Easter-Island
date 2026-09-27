"""Inventory growth, Zipf, entropy, repetition, position, and a null alignment.

Conditional entropy follows Rao et al. (Science, 2009): randomness of the next
sign given the previous one. ``h1`` here is the unigram entropy. ``h2`` is the
bigram conditional entropy H(next | previous), which is the quantity Rao et al.
plot. Block entropy of bigrams is ``h1_of_pairs``. Names are spelled out in the
report so the two conventions are not mixed.
"""

from __future__ import annotations

import math
import random
from collections import Counter, defaultdict

ALIGNMENT_K = 30
ALIGNMENT_PERMUTATIONS = 200
ALIGNMENT_SEED = 1
SHUFFLE_SEED = 0
RANDOM_SEED = 0
HEAPS_MIN_N = 50


def flatten(lines: list[list[str]]) -> list[str]:
    return [token for line in lines for token in line]


def inventory_size(lines: list[list[str]]) -> int:
    return len({token for line in lines for token in line})


def token_count(lines: list[list[str]]) -> int:
    return sum(len(line) for line in lines)


def heaps_curve(lines: list[list[str]]) -> list[int]:
    """``curve[n]`` is the number of distinct types in the first n tokens.

    ``curve[0]`` is 0. Line order is the order of ``lines``.
    """
    seen: set[str] = set()
    curve = [0]
    for token in flatten(lines):
        seen.add(token)
        curve.append(len(seen))
    return curve


def inventory_at(curve: list[int], n: int) -> int:
    if n <= 0 or len(curve) <= 1:
        return 0
    return curve[min(n, len(curve) - 1)]


def heaps_beta(curve: list[int]) -> float | None:
    """OLS slope of log(types) on log(tokens) for n >= 50."""
    xs: list[float] = []
    ys: list[float] = []
    last = len(curve) - 1
    for n in range(HEAPS_MIN_N, last + 1):
        types = curve[n]
        if types <= 0:
            continue
        xs.append(math.log(n))
        ys.append(math.log(types))
    if len(xs) < 2:
        return None
    _intercept, slope, _r2 = ols(xs, ys)
    return slope


def zipf_fit(lines: list[list[str]], *, min_frequency: int = 1) -> dict[str, float | int | None]:
    """OLS of log(frequency) on log(rank). Ties keep alphabetical order."""
    counts = Counter(token for line in lines for token in line)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    frequencies = [count for _sign, count in ranked if count >= min_frequency]
    if len(frequencies) < 2:
        return {"slope": None, "r2": None, "ranks": len(frequencies)}
    xs = [math.log(rank) for rank in range(1, len(frequencies) + 1)]
    ys = [math.log(count) for count in frequencies]
    _intercept, slope, r2 = ols(xs, ys)
    return {"slope": slope, "r2": r2, "ranks": len(frequencies)}


def ols(xs: list[float], ys: list[float]) -> tuple[float, float, float]:
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    var_x = sum((x - mean_x) ** 2 for x in xs)
    if var_x == 0:
        return mean_y, 0.0, 0.0
    covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    slope = covariance / var_x
    intercept = mean_y - slope * mean_x
    residual = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
    total = sum((y - mean_y) ** 2 for y in ys)
    r2 = 1.0 - residual / total if total else 0.0
    return intercept, slope, r2


def _pair_counts(lines: list[list[str]]) -> dict[str, Counter[str]]:
    successors: dict[str, Counter[str]] = defaultdict(Counter)
    for line in lines:
        for previous, nxt in zip(line, line[1:]):
            successors[previous][nxt] += 1
    return successors


def unigram_entropy(lines: list[list[str]]) -> float:
    """h1: Shannon entropy of single tokens, bits."""
    counts = Counter(token for line in lines for token in line)
    total = sum(counts.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for token in sorted(counts):
        probability = counts[token] / total
        entropy -= probability * math.log2(probability)
    return entropy


def conditional_entropy_mle(lines: list[list[str]]) -> float:
    """h2: MLE of H(next | previous) inside lines, bits."""
    successors = _pair_counts(lines)
    total = sum(sum(counter.values()) for counter in successors.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for previous in sorted(successors):
        counter = successors[previous]
        count_prev = sum(counter.values())
        weight = count_prev / total
        inner = 0.0
        for nxt in sorted(counter):
            probability = counter[nxt] / count_prev
            inner -= probability * math.log2(probability)
        entropy += weight * inner
    return entropy


def conditional_entropy_laplace(lines: list[list[str]]) -> float:
    """h2 with add-one smoothing over the observed inventory."""
    successors = _pair_counts(lines)
    types = sorted({token for line in lines for token in line})
    vocabulary = len(types)
    if vocabulary <= 1:
        return 0.0
    type_set = set(types)
    total = sum(sum(counter.values()) for counter in successors.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for previous in sorted(successors):
        counter = successors[previous]
        count_prev = sum(counter.values())
        if count_prev == 0:
            continue
        weight = count_prev / total
        denominator = count_prev + vocabulary
        inner = 0.0
        seen = 0
        for nxt in sorted(counter):
            if nxt not in type_set:
                continue
            probability = (counter[nxt] + 1) / denominator
            inner -= probability * math.log2(probability)
            seen += 1
        unseen = vocabulary - seen
        if unseen:
            probability = 1 / denominator
            inner -= unseen * probability * math.log2(probability)
        entropy += weight * inner
    return entropy


def bigram_block_entropy(lines: list[list[str]]) -> float:
    """Entropy of observed adjacent pairs, bits. Not the conditional entropy."""
    counts: Counter[tuple[str, str]] = Counter()
    for line in lines:
        for pair in zip(line, line[1:]):
            counts[pair] += 1
    total = sum(counts.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for pair in sorted(counts):
        probability = counts[pair] / total
        entropy -= probability * math.log2(probability)
    return entropy


def rao_curve(lines: list[list[str]], step: int = 20) -> list[dict[str, float | int]]:
    """Laplace h2 on the k most frequent types, then 2k, and so on.

    Tokens outside the top k are collapsed to one residual class, which is
    how a growing token-set size is compared in the Rao et al. curves.
    """
    ranked = sorted(
        Counter(token for line in lines for token in line).items(),
        key=lambda item: (-item[1], item[0]),
    )
    if not ranked:
        return []
    points: list[dict[str, float | int]] = []
    k = step
    while True:
        keep = {sign for sign, _count in ranked[:k]}
        recoded = [[token if token in keep else "OTHER" for token in line] for line in lines]
        vocabulary = inventory_size(recoded)
        h2 = conditional_entropy_laplace(recoded)
        points.append({"k": k, "vocabulary": vocabulary, "h2_laplace": h2})
        if k >= len(ranked):
            break
        k = min(len(ranked), k + step)
    return points


def repetition_rates(lines: list[list[str]]) -> dict[str, float | int]:
    """Adjacent XX rate and ABAB rate, pairs not crossing line breaks."""
    adjacent = 0
    identical = 0
    windows = 0
    abab = 0
    for line in lines:
        for previous, nxt in zip(line, line[1:]):
            adjacent += 1
            if previous == nxt:
                identical += 1
        for index in range(len(line) - 3):
            windows += 1
            first, second = line[index], line[index + 1]
            if first == line[index + 2] and second == line[index + 3] and first != second:
                abab += 1
    return {
        "adjacent_pairs": adjacent,
        "identical_pairs": identical,
        "xx_rate": (identical / adjacent) if adjacent else 0.0,
        "abab_windows": windows,
        "abab_hits": abab,
        "abab_rate": (abab / windows) if windows else 0.0,
    }


def edge_profile(
    initial: Counter[str],
    medial: Counter[str],
    final: Counter[str],
    totals: Counter[str],
    *,
    min_frequency: int,
) -> dict[str, float | int]:
    frequent = [token for token, count in totals.items() if count >= min_frequency]
    in_all_three = sum(1 for token in frequent if initial[token] and medial[token] and final[token])
    mass = sum(totals.values())
    return {
        "min_frequency": min_frequency,
        "frequent_types": len(frequent),
        "frequent_in_all_three": in_all_three,
        "frequent_in_all_three_rate": (in_all_three / len(frequent)) if frequent else 0.0,
        "initial_token_share": (sum(initial.values()) / mass) if mass else 0.0,
        "medial_token_share": (sum(medial.values()) / mass) if mass else 0.0,
        "final_token_share": (sum(final.values()) / mass) if mass else 0.0,
    }


def position_profile(lines: list[list[str]], *, min_frequency: int = 10) -> dict[str, float | int]:
    """Line-initial, medial, and final shares.

    A line of length 1 is initial only. Length 2 is initial and final.
    Medial tokens are the interior of lines of length 3 or more.
    """
    initial: Counter[str] = Counter()
    medial: Counter[str] = Counter()
    final: Counter[str] = Counter()
    for line in lines:
        if not line:
            continue
        initial[line[0]] += 1
        if len(line) >= 2:
            final[line[-1]] += 1
        if len(line) >= 3:
            medial.update(line[1:-1])
    totals = Counter(token for line in lines for token in line)
    return edge_profile(initial, medial, final, totals, min_frequency=min_frequency)


def word_edge_profile(
    syllable_groups: list[list[str]],
    *,
    min_frequency: int = 10,
) -> dict[str, float | int]:
    """Initial, medial, and final inside each word's syllable parse.

    ``syllable_groups`` is one group per word. This is not an inscribed line.
    """
    initial: Counter[str] = Counter()
    medial: Counter[str] = Counter()
    final: Counter[str] = Counter()
    totals: Counter[str] = Counter()
    for syllables in syllable_groups:
        if not syllables:
            continue
        totals.update(syllables)
        initial[syllables[0]] += 1
        if len(syllables) >= 2:
            final[syllables[-1]] += 1
        if len(syllables) >= 3:
            medial.update(syllables[1:-1])
    return edge_profile(initial, medial, final, totals, min_frequency=min_frequency)


def shuffle_lines(lines: list[list[str]], seed: int = SHUFFLE_SEED) -> list[list[str]]:
    """Same tokens and line lengths, order destroyed."""
    generator = random.Random(seed)
    pooled = flatten(lines)
    generator.shuffle(pooled)
    shuffled: list[list[str]] = []
    offset = 0
    for line in lines:
        shuffled.append(pooled[offset : offset + len(line)])
        offset += len(line)
    return shuffled


def rigid_lines(lines: list[list[str]]) -> list[list[str]]:
    """One fixed cycle of the inventory, cut into the original line lengths."""
    inventory = sorted({token for line in lines for token in line})
    if not inventory:
        return []
    output: list[list[str]] = []
    index = 0
    for line in lines:
        row = []
        for _token in line:
            row.append(inventory[index % len(inventory)])
            index += 1
        output.append(row)
    return output


def random_lines(lines: list[list[str]], seed: int = RANDOM_SEED) -> list[list[str]]:
    """Independent uniform draws from the same inventory, same line lengths."""
    inventory = sorted({token for line in lines for token in line})
    generator = random.Random(seed)
    return [[generator.choice(inventory) for _token in line] for line in lines]


def summarize(lines: list[list[str]]) -> dict[str, object]:
    """Full descriptive block for one sequence sample."""
    curve = heaps_curve(lines)
    vocabulary = inventory_size(lines)
    h1 = unigram_entropy(lines)
    h2 = conditional_entropy_mle(lines)
    h2_laplace = conditional_entropy_laplace(lines)
    log_v = math.log2(vocabulary) if vocabulary > 1 else 0.0
    zipf_all = zipf_fit(lines, min_frequency=1)
    zipf_repeat = zipf_fit(lines, min_frequency=2)
    return {
        "tokens": token_count(lines),
        "lines": len(lines),
        "inventory": vocabulary,
        "hapax": sum(1 for count in Counter(flatten(lines)).values() if count == 1),
        "heaps_beta": heaps_beta(curve),
        "h1_unigram": h1,
        "h2_conditional_mle": h2,
        "h2_conditional_laplace": h2_laplace,
        "h2_block": bigram_block_entropy(lines),
        "h2_over_log2_v": (h2_laplace / log_v) if log_v else 0.0,
        "zipf_slope": zipf_all["slope"],
        "zipf_r2": zipf_all["r2"],
        "zipf_slope_freq_ge2": zipf_repeat["slope"],
        "zipf_r2_freq_ge2": zipf_repeat["r2"],
        "repetition": repetition_rates(lines),
        "position": position_profile(lines),
        "curve": curve,
    }


def structure_index(text_h2: float, shuffled_h2: float) -> float:
    """1 means the text is rigid relative to its own unigram shuffle; 0 means not."""
    if shuffled_h2 <= 0:
        return 0.0
    return max(0.0, 1.0 - text_h2 / shuffled_h2)


def _ranked(lines: list[list[str]], k: int) -> list[str]:
    counts = Counter(token for line in lines for token in line)
    return [
        sign for sign, _count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]
    ]


def _self_rates(lines: list[list[str]], items: list[str]) -> list[float]:
    wanted = set(items)
    hits = {item: 0 for item in items}
    totals = {item: 0 for item in items}
    for line in lines:
        for previous, nxt in zip(line, line[1:]):
            if previous in wanted:
                totals[previous] += 1
                if nxt == previous:
                    hits[previous] += 1
    return [(hits[item] / totals[item]) if totals[item] else 0.0 for item in items]


def _transition(lines: list[list[str]], items: list[str]) -> list[list[float]]:
    index = {item: position for position, item in enumerate(items)}
    size = len(items)
    counts = [[0 for _column in range(size)] for _row in range(size)]
    for line in lines:
        for previous, nxt in zip(line, line[1:]):
            if previous in index and nxt in index:
                counts[index[previous]][index[nxt]] += 1
    matrix: list[list[float]] = []
    for row in counts:
        total = sum(row)
        if total == 0:
            matrix.append([0.0 for _cell in row])
        else:
            matrix.append([cell / total for cell in row])
    return matrix


def _permute_matrix(matrix: list[list[float]], permutation: list[int]) -> list[list[float]]:
    size = len(matrix)
    return [
        [matrix[permutation[row]][permutation[column]] for column in range(size)]
        for row in range(size)
    ]


def _cosine(left: list[list[float]], right: list[list[float]]) -> float:
    dot = 0.0
    left_norm = 0.0
    right_norm = 0.0
    for row_left, row_right in zip(left, right):
        for a, b in zip(row_left, row_right):
            dot += a * b
            left_norm += a * a
            right_norm += b * b
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / math.sqrt(left_norm * right_norm)


def _average_ranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda index: (values[index], index))
    ranks = [0.0 for _value in values]
    start = 0
    while start < len(order):
        end = start
        while end + 1 < len(order) and values[order[end + 1]] == values[order[start]]:
            end += 1
        # Ranks are 1-based. Ties share the average rank.
        average = (start + 1 + end + 1) / 2
        for position in range(start, end + 1):
            ranks[order[position]] = average
        start = end + 1
    return ranks


def _pearson(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    var_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    var_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    if var_x == 0 or var_y == 0:
        return 0.0
    covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    return covariance / (var_x * var_y)


def _spearman(xs: list[float], ys: list[float]) -> float:
    return _pearson(_average_ranks(xs), _average_ranks(ys))


def frequency_alignment(
    sign_lines: list[list[str]],
    syllable_lines: list[list[str]],
    *,
    k: int = ALIGNMENT_K,
    permutations: int = ALIGNMENT_PERMUTATIONS,
    seed: int = ALIGNMENT_SEED,
) -> dict[str, object]:
    """Rank-align top signs to top syllables and test that map against shuffles.

    The mapping is a hypothesis. Marginal frequencies match by construction, so
    the statistics are sequential: cosine of the within-set transition
    matrices, and Spearman correlation of self-repetition rates. The null is
    a random bijection between the same two lists.
    """
    sign_items = _ranked(sign_lines, k)
    syllable_items = _ranked(syllable_lines, k)
    width = min(len(sign_items), len(syllable_items))
    sign_items = sign_items[:width]
    syllable_items = syllable_items[:width]
    if width < 5:
        return {
            "k": width,
            "permutations": 0,
            "cosine": None,
            "cosine_null_ge_fraction": None,
            "repetition_spearman": None,
            "repetition_null_ge_fraction": None,
            "pairs": [],
        }
    sign_matrix = _transition(sign_lines, sign_items)
    syllable_matrix = _transition(syllable_lines, syllable_items)
    sign_rates = _self_rates(sign_lines, sign_items)
    syllable_rates = _self_rates(syllable_lines, syllable_items)
    observed_cosine = _cosine(sign_matrix, syllable_matrix)
    observed_spearman = _spearman(sign_rates, syllable_rates)
    generator = random.Random(seed)
    cosine_ge = 0
    spearman_ge = 0
    for _draw in range(permutations):
        permutation = list(range(width))
        generator.shuffle(permutation)
        shuffled_matrix = _permute_matrix(syllable_matrix, permutation)
        shuffled_rates = [syllable_rates[index] for index in permutation]
        if _cosine(sign_matrix, shuffled_matrix) >= observed_cosine:
            cosine_ge += 1
        if _spearman(sign_rates, shuffled_rates) >= observed_spearman:
            spearman_ge += 1
    pairs = [
        {"sign": sign, "syllable": syllable, "rank": rank + 1}
        for rank, (sign, syllable) in enumerate(zip(sign_items, syllable_items))
    ]
    return {
        "k": width,
        "permutations": permutations,
        "cosine": observed_cosine,
        "cosine_null_ge_fraction": cosine_ge / permutations,
        "repetition_spearman": observed_spearman,
        "repetition_null_ge_fraction": spearman_ge / permutations,
        "pairs": pairs,
        "hypothesis_only": True,
        "reading": None,
    }
