"""Structural tests of the genealogy hypothesis on texts I and G.

Sign numbers only. Glosses from the literature are stored as cited
hypotheses and are not applied to any sign. Ligatures stay inside
one hyphen-separated group. Stems follow the same mechanical rule
as ``published_stems`` (colon rewritten to a dot, then Barthel
allograph marks stripped).
"""

from __future__ import annotations

import random
import re
from collections import Counter
from dataclasses import dataclass

_ALLOGRAPH_MARKS = re.compile(r"[A-Za-z?*!]+")

STEM_999 = "999"
STEM_076 = "076"
STEM_200 = "200"

# Pre-specified Monte Carlo sizes. Each null owns its own seed.
NULL_CONTENT_TRIALS = 2000
NULL_CONTENT_SEED = 0
NULL_PLACEMENT_TRIALS = 2000
NULL_PLACEMENT_SEED = 2
NULL_GV6_TRIALS = 5000
NULL_GV6_SEED = 0
NULL_GV_TRIALS = 2000
NULL_GV_SEED = 1
NULL_IA_TEMPLATE_TRIALS = 2000
NULL_IA_TEMPLATE_SEED = 3


def group_stems(token: str) -> tuple[str, ...]:
    """Stems of one hyphen-separated group. Same rule as published_stems."""
    return tuple(_barthel_stems([token.replace(":", ".")]))


def _barthel_stems(tokens: list[str]) -> list[str]:
    """Copy of the calendar-scoreboard stemmer. Does not remap types."""
    stems: list[str] = []
    for token in tokens:
        piece = token.strip().rstrip("*")
        if not piece:
            continue
        for part in piece.split("."):
            part = part.strip()
            if not part:
                continue
            if part.startswith("V") and len(part) > 1 and part[1].isdigit():
                part = part[1:]
            part = _ALLOGRAPH_MARKS.sub("", part)
            if part.isdigit():
                stems.append(part.zfill(3))
    return stems


def _is_pure(token: str, stem: str) -> bool:
    return group_stems(token) == (stem,)


def _contains(token: str, stem: str) -> bool:
    return stem in group_stems(token)


def _suffixed(token: str, stem: str) -> bool:
    """True when stem is the final component and a host sign is present."""
    stems = group_stems(token)
    return len(stems) > 1 and stems[-1] == stem


def _plain_name_group(token: str) -> bool:
    """A name slot: some sign, and not the stroke, 200, or 076."""
    stems = group_stems(token)
    blocked = {STEM_076, STEM_200, STEM_999}
    return bool(stems) and blocked.isdisjoint(stems)


@dataclass(frozen=True)
class StrictPhrase:
    """One ``200 X Y.076`` hit. Child and father are stem tuples."""

    line: str
    index: int
    groups: tuple[str, str, str]
    child: tuple[str, ...]
    father: tuple[str, ...]


@dataclass(frozen=True)
class QuadPhrase:
    """One ``200 A B C.076`` hit that is longer than the strict triple."""

    line: str
    index: int
    groups: tuple[str, str, str, str]
    third: tuple[str, ...]
    father: tuple[str, ...]


def extract_strict_phrases(
    groups: list[str] | tuple[str, ...],
    line: str = "",
) -> tuple[StrictPhrase, ...]:
    """Left-to-right non-overlapping ``200 X Y.076`` phrases.

    X is one group that does not contain 200 or 076. Y.076 is one
    group whose last stem is 076 and which has another stem. A hit
    consumes three groups so the next search starts after it.
    """
    hits: list[StrictPhrase] = []
    index = 0
    while index + 2 < len(groups):
        introducer, name, patron = groups[index : index + 3]
        if (
            _is_pure(introducer, STEM_200)
            and _plain_name_group(name)
            and _suffixed(patron, STEM_076)
        ):
            father = tuple(stem for stem in group_stems(patron) if stem != STEM_076)
            hits.append(
                StrictPhrase(
                    line=line,
                    index=index,
                    groups=(introducer, name, patron),
                    child=group_stems(name),
                    father=father,
                )
            )
            index += 3
            continue
        index += 1
    return tuple(hits)


def extract_quad_phrases(
    groups: list[str] | tuple[str, ...],
    line: str = "",
) -> tuple[QuadPhrase, ...]:
    """Left-to-right ``200 A B C.076`` phrases (four groups)."""
    hits: list[QuadPhrase] = []
    index = 0
    while index + 3 < len(groups):
        window = tuple(groups[index : index + 4])
        if (
            _is_pure(window[0], STEM_200)
            and _plain_name_group(window[1])
            and _plain_name_group(window[2])
            and _suffixed(window[3], STEM_076)
        ):
            father = tuple(stem for stem in group_stems(window[3]) if stem != STEM_076)
            quad_groups = (window[0], window[1], window[2], window[3])
            hits.append(
                QuadPhrase(
                    line=line,
                    index=index,
                    groups=quad_groups,
                    third=group_stems(window[2]),
                    father=father,
                )
            )
            index += 4
            continue
        index += 1
    return tuple(hits)


def chain_links(phrases: tuple[StrictPhrase, ...]) -> int:
    """Adjacent phrases whose father stem tuple is the next child."""
    links = 0
    for left, right in zip(phrases, phrases[1:]):
        if right.index == left.index + 3 and left.father == right.child:
            links += 1
    return links


def max_chain_run(phrases: tuple[StrictPhrase, ...]) -> int:
    """Longest run of immediate father-to-child handoffs."""
    best = 0
    run = 0
    for left, right in zip(phrases, phrases[1:]):
        if right.index == left.index + 3 and left.father == right.child:
            run += 1
            best = max(best, run)
        else:
            run = 0
    return best


def _interior_segments(
    groups: list[str] | tuple[str, ...],
) -> list[tuple[str, ...]]:
    """Groups lying strictly between two pure-999 strokes on one line."""
    chunks: list[list[str]] = [[]]
    for group in groups:
        if _is_pure(group, STEM_999):
            chunks.append([])
        else:
            chunks[-1].append(group)
    if len(chunks) <= 2:
        return []
    return [tuple(chunk) for chunk in chunks[1:-1]]


def _edge_segments(
    groups: list[str] | tuple[str, ...],
) -> list[tuple[str, ...]]:
    """The span before the first pure-999 and the span after the last."""
    chunks: list[list[str]] = [[]]
    for group in groups:
        if _is_pure(group, STEM_999):
            chunks.append([])
        else:
            chunks[-1].append(group)
    if len(chunks) == 1:
        return [tuple(chunks[0])]
    return [tuple(chunks[0]), tuple(chunks[-1])]


@dataclass(frozen=True)
class StrokeCensus:
    """How 999 is written in one text. Ids only."""

    codes: int
    pure_breaks: int
    fused_groups: tuple[str, ...]
    form_counts: tuple[tuple[str, int], ...]


def census_strokes(lines: list[tuple[str, list[str]]]) -> StrokeCensus:
    """Count 999 codes. A pure break is a group whose only stem is 999."""
    forms: Counter[str] = Counter()
    fused: list[str] = []
    pure = 0
    for _name, groups in lines:
        for group in groups:
            stems = group_stems(group)
            if STEM_999 not in stems:
                continue
            forms[group.rstrip("*")] += 1
            if stems == (STEM_999,):
                pure += 1
            else:
                fused.append(group.rstrip("*"))
    ordered = tuple(sorted(forms.items(), key=lambda item: (-item[1], item[0])))
    return StrokeCensus(
        codes=sum(forms.values()),
        pure_breaks=pure,
        fused_groups=tuple(fused),
        form_counts=ordered,
    )


@dataclass(frozen=True)
class FischerCensus:
    """Positional claims about spans between pure-999 strokes."""

    pure_breaks: int
    immediate_076_group: int
    immediate_076_suffix: int
    immediate_bare_076: int
    non_immediate: tuple[tuple[str, int, str], ...]
    interior: int
    length_histogram: tuple[tuple[int, int], ...]
    length_eq_3: int
    length_mod_3: int
    length_lt_3: int
    length_median: int
    first_contains_076: int
    first_is_suffix: int
    last_contains_076: int
    penultimate_contains_076: int
    antepenultimate_contains_076: int
    ante_eligible: int
    triad_only_first: int
    onset_groups: int
    onset_contains_076: int
    other_groups: int
    other_contains_076: int
    attachment: tuple[tuple[str, int], ...]
    edge_nonempty: int
    short_segment: tuple[tuple[str, tuple[str, ...]], ...]
    interior_final_076: tuple[tuple[str, str], ...]


def _attachment_label(token: str) -> str | None:
    stems = group_stems(token)
    if STEM_076 not in stems:
        return None
    if stems == (STEM_076,):
        return "bare"
    if stems[-1] == STEM_076:
        return "suffix"
    if stems[0] == STEM_076:
        return "initial"
    return "medial"


def fischer_census(lines: list[tuple[str, list[str]]]) -> FischerCensus:
    """Measure Staff segments. Interior spans are those between two strokes."""
    non_immediate: list[tuple[str, int, str]] = []
    immediate = 0
    immediate_suffix = 0
    immediate_bare = 0
    pure = 0
    interiors: list[tuple[str, tuple[str, ...]]] = []
    edges_nonempty = 0
    attachment: Counter[str] = Counter()
    for name, groups in lines:
        for group in groups:
            label = _attachment_label(group)
            if label is not None:
                attachment[label] += 1
        for index, group in enumerate(groups):
            if not _is_pure(group, STEM_999):
                continue
            pure += 1
            if index + 1 >= len(groups) or _is_pure(groups[index + 1], STEM_999):
                non_immediate.append((name, index, ""))
                continue
            nxt = groups[index + 1]
            if _contains(nxt, STEM_076):
                immediate += 1
                if _suffixed(nxt, STEM_076):
                    immediate_suffix += 1
                elif _is_pure(nxt, STEM_076):
                    immediate_bare += 1
            else:
                non_immediate.append((name, index, nxt))
        for segment in _interior_segments(groups):
            interiors.append((name, segment))
        if any(_is_pure(group, STEM_999) for group in groups):
            for segment in _edge_segments(groups):
                if segment:
                    edges_nonempty += 1

    nonempty = [(name, segment) for name, segment in interiors if segment]
    lengths = [len(segment) for _name, segment in nonempty]
    histogram = tuple(sorted(Counter(lengths).items()))
    short = tuple((name, segment) for name, segment in nonempty if len(segment) < 3)
    finals = tuple(
        (name, segment[-1]) for name, segment in nonempty if _contains(segment[-1], STEM_076)
    )
    onset = 0
    onset_hit = 0
    other = 0
    other_hit = 0
    for _name, segment in nonempty:
        for index, group in enumerate(segment):
            if index % 3 == 0:
                onset += 1
                onset_hit += _contains(group, STEM_076)
            else:
                other += 1
                other_hit += _contains(group, STEM_076)
    ante_eligible = sum(1 for _name, segment in nonempty if len(segment) >= 3)
    length_eq_3 = sum(1 for length in lengths if length == 3)
    triad_only = 0
    for _name, segment in nonempty:
        if len(segment) != 3:
            continue
        if (
            _contains(segment[0], STEM_076)
            and not _contains(segment[1], STEM_076)
            and not _contains(segment[2], STEM_076)
        ):
            triad_only += 1
    ordered_attachment = tuple(
        (label, attachment[label])
        for label in ("bare", "suffix", "initial", "medial")
        if attachment[label]
    )
    ordered_lengths = sorted(lengths)
    median = ordered_lengths[len(ordered_lengths) // 2] if ordered_lengths else 0
    return FischerCensus(
        pure_breaks=pure,
        immediate_076_group=immediate,
        immediate_076_suffix=immediate_suffix,
        immediate_bare_076=immediate_bare,
        non_immediate=tuple(non_immediate),
        interior=len(nonempty),
        length_histogram=histogram,
        length_eq_3=length_eq_3,
        length_mod_3=sum(1 for length in lengths if length % 3 == 0),
        length_lt_3=sum(1 for length in lengths if length < 3),
        length_median=median,
        first_contains_076=sum(1 for _n, segment in nonempty if _contains(segment[0], STEM_076)),
        first_is_suffix=sum(1 for _n, segment in nonempty if _suffixed(segment[0], STEM_076)),
        last_contains_076=len(finals),
        penultimate_contains_076=sum(
            1 for _n, segment in nonempty if len(segment) >= 2 and _contains(segment[-2], STEM_076)
        ),
        antepenultimate_contains_076=sum(
            1 for _n, segment in nonempty if len(segment) >= 3 and _contains(segment[-3], STEM_076)
        ),
        ante_eligible=ante_eligible,
        triad_only_first=triad_only,
        onset_groups=onset,
        onset_contains_076=onset_hit,
        other_groups=other,
        other_contains_076=other_hit,
        attachment=ordered_attachment,
        edge_nonempty=edges_nonempty,
        short_segment=short,
        interior_final_076=finals,
    )


def _shuffle_keep_strokes(
    lines: list[tuple[str, list[str]]],
    rng: random.Random,
) -> list[tuple[str, list[str]]]:
    """Permute non-stroke groups inside each line. Stroke positions stay."""
    shuffled: list[tuple[str, list[str]]] = []
    for name, groups in lines:
        movable = [group for group in groups if not _is_pure(group, STEM_999)]
        rng.shuffle(movable)
        cursor = iter(movable)
        rebuilt = [group if _is_pure(group, STEM_999) else next(cursor) for group in groups]
        shuffled.append((name, rebuilt))
    return shuffled


def _shuffle_groups(
    lines: list[tuple[str, list[str]]],
    rng: random.Random,
) -> list[tuple[str, list[str]]]:
    """Permute every group inside each line, strokes included."""
    shuffled: list[tuple[str, list[str]]] = []
    for name, groups in lines:
        copied = list(groups)
        rng.shuffle(copied)
        shuffled.append((name, copied))
    return shuffled


def _shuffle_pooled(
    lines: list[tuple[str, list[str]]],
    rng: random.Random,
) -> list[tuple[str, list[str]]]:
    """Pool groups across lines, then restore each line's length."""
    flat = [group for _name, groups in lines for group in groups]
    rng.shuffle(flat)
    shuffled: list[tuple[str, list[str]]] = []
    offset = 0
    for name, groups in lines:
        shuffled.append((name, flat[offset : offset + len(groups)]))
        offset += len(groups)
    return shuffled


@dataclass(frozen=True)
class NullHit:
    """How many shuffles met or passed the observed statistic."""

    trials: int
    seed: int
    observed: int
    ge: int
    le: int


def _hit(trials: int, seed: int, observed: int, ge: int, le: int) -> NullHit:
    return NullHit(trials=trials, seed=seed, observed=observed, ge=ge, le=le)


def content_null(
    lines: list[tuple[str, list[str]]],
    observed: FischerCensus,
    trials: int = NULL_CONTENT_TRIALS,
    seed: int = NULL_CONTENT_SEED,
) -> dict[str, NullHit]:
    """Stroke positions fixed. Asks whether 076 sits in the claimed slots."""
    rng = random.Random(seed)
    keys = (
        "immediate_076_group",
        "first_contains_076",
        "first_is_suffix",
        "antepenultimate_contains_076",
        "triad_only_first",
        "onset_contains_076",
        "last_contains_076",
        "penultimate_contains_076",
        "other_contains_076",
    )
    ge = {key: 0 for key in keys}
    le = {key: 0 for key in keys}
    for _trial in range(trials):
        census = fischer_census(_shuffle_keep_strokes(lines, rng))
        for key in keys:
            value = getattr(census, key)
            target = getattr(observed, key)
            ge[key] += value >= target
            le[key] += value <= target
    return {key: _hit(trials, seed, getattr(observed, key), ge[key], le[key]) for key in keys}


def placement_null(
    lines: list[tuple[str, list[str]]],
    observed: FischerCensus,
    trials: int = NULL_PLACEMENT_TRIALS,
    seed: int = NULL_PLACEMENT_SEED,
) -> dict[str, NullHit]:
    """Strokes move with the other groups. Asks whether span lengths are special."""
    rng = random.Random(seed)
    keys = ("length_eq_3", "length_mod_3", "length_lt_3", "interior")
    ge = {key: 0 for key in keys}
    le = {key: 0 for key in keys}
    for _trial in range(trials):
        census = fischer_census(_shuffle_groups(lines, rng))
        for key in keys:
            value = getattr(census, key)
            target = getattr(observed, key)
            ge[key] += value >= target
            le[key] += value <= target
    return {key: _hit(trials, seed, getattr(observed, key), ge[key], le[key]) for key in keys}


@dataclass(frozen=True)
class LinePhrases:
    line: str
    strict: int
    links: int
    quads: int


@dataclass(frozen=True)
class GenealogyCensus:
    """Strict triples, the Gv6 shift, and the same template on I and Gr."""

    by_line: tuple[LinePhrases, ...]
    gv6_phrases: tuple[StrictPhrase, ...]
    gv6_links: int
    gv6_max_run: int
    gv6_quads: tuple[QuadPhrase, ...]
    gv6_quad_handoff_father: bool
    gv6_quad_handoff_third: bool
    gv567_strict: int
    gv567_links: int
    gv567_quads: int
    child_types: int
    child_tokens: int
    father_types: int
    father_tokens: int
    ia_strict: int
    ia_links: int
    gr_strict: int
    gr_links: int
    gv_strict: int
    gv_links: int


def _line_rows(
    lines: list[tuple[str, list[str]]],
) -> tuple[LinePhrases, ...]:
    rows: list[LinePhrases] = []
    for name, groups in lines:
        phrases = extract_strict_phrases(groups, name)
        rows.append(
            LinePhrases(
                line=name,
                strict=len(phrases),
                links=chain_links(phrases),
                quads=len(extract_quad_phrases(groups, name)),
            )
        )
    return tuple(rows)


def genealogy_census(
    gv_lines: list[tuple[str, list[str]]],
    gr_lines: list[tuple[str, list[str]]],
    ia_lines: list[tuple[str, list[str]]],
) -> GenealogyCensus:
    """Count the published Gv6 pattern and the same template elsewhere."""
    by_name = {name: groups for name, groups in gv_lines}
    gv6 = extract_strict_phrases(by_name["Gv6"], "Gv6")
    quads = extract_quad_phrases(by_name["Gv6"], "Gv6")
    father_match = False
    third_match = False
    if quads and gv6 and gv6[0].index == quads[0].index + 4:
        father_match = quads[0].father == gv6[0].child
        third_match = quads[0].third == gv6[0].child
    window: list[str] = []
    for name in ("Gv5", "Gv6", "Gv7"):
        window.extend(by_name[name])
    joined = extract_strict_phrases(window, "Gv5-7")
    joined_quads = extract_quad_phrases(window, "Gv5-7")
    children = [phrase.child for phrase in gv6]
    fathers = [phrase.father for phrase in gv6]
    ia_phrases = [
        phrase for name, groups in ia_lines for phrase in extract_strict_phrases(groups, name)
    ]
    gr_phrases = [
        phrase for name, groups in gr_lines for phrase in extract_strict_phrases(groups, name)
    ]
    gv_links = sum(row.links for row in _line_rows(gv_lines))
    ia_links = sum(chain_links(extract_strict_phrases(groups, name)) for name, groups in ia_lines)
    gr_links = sum(chain_links(extract_strict_phrases(groups, name)) for name, groups in gr_lines)
    return GenealogyCensus(
        by_line=_line_rows(gv_lines + gr_lines + ia_lines),
        gv6_phrases=gv6,
        gv6_links=chain_links(gv6),
        gv6_max_run=max_chain_run(gv6),
        gv6_quads=quads,
        gv6_quad_handoff_father=father_match,
        gv6_quad_handoff_third=third_match,
        gv567_strict=len(joined),
        gv567_links=chain_links(joined),
        gv567_quads=len(joined_quads),
        child_types=len(set(children)),
        child_tokens=len(children),
        father_types=len(set(fathers)),
        father_tokens=len(fathers),
        ia_strict=len(ia_phrases),
        ia_links=ia_links,
        gr_strict=len(gr_phrases),
        gr_links=gr_links,
        gv_strict=sum(row.strict for row in _line_rows(gv_lines)),
        gv_links=gv_links,
    )


def gv6_chain_null(
    groups: list[str],
    observed_links: int,
    observed_phrases: int,
    trials: int = NULL_GV6_TRIALS,
    seed: int = NULL_GV6_SEED,
) -> dict[str, NullHit]:
    """Shuffle Gv6 groups. The shift-register is the statistic."""
    rng = random.Random(seed)
    ge_links = 0
    ge_phrases = 0
    ge_run = 0
    observed_run = max_chain_run(extract_strict_phrases(groups, "Gv6"))
    for _trial in range(trials):
        copied = list(groups)
        rng.shuffle(copied)
        phrases = extract_strict_phrases(copied, "Gv6")
        links = chain_links(phrases)
        ge_links += links >= observed_links
        ge_phrases += len(phrases) >= observed_phrases
        ge_run += max_chain_run(phrases) >= observed_run
    return {
        "links": _hit(trials, seed, observed_links, ge_links, trials - ge_links),
        "phrases": _hit(trials, seed, observed_phrases, ge_phrases, trials - ge_phrases),
        "max_run": _hit(trials, seed, observed_run, ge_run, trials - ge_run),
    }


def pooled_template_null(
    lines: list[tuple[str, list[str]]],
    observed_phrases: int,
    observed_links: int,
    trials: int,
    seed: int,
) -> dict[str, NullHit]:
    """Shuffle a text with line lengths kept. Counts strict phrases and links."""
    rng = random.Random(seed)
    ge_phrases = 0
    ge_links = 0
    for _trial in range(trials):
        shuffled = _shuffle_pooled(lines, rng)
        phrases = 0
        links = 0
        for name, groups in shuffled:
            found = extract_strict_phrases(groups, name)
            phrases += len(found)
            links += chain_links(found)
        ge_phrases += phrases >= observed_phrases
        ge_links += links >= observed_links
    return {
        "phrases": _hit(trials, seed, observed_phrases, ge_phrases, trials - ge_phrases),
        "links": _hit(trials, seed, observed_links, ge_links, trials - ge_links),
    }


@dataclass(frozen=True)
class SlotDiversity:
    """Type/token counts for the three slots of interior length-3 spans."""

    x_tokens: int
    x_types: int
    y_tokens: int
    y_types: int
    z_tokens: int
    z_types: int
    x_suffix: int


def triad_slot_diversity(lines: list[tuple[str, list[str]]]) -> SlotDiversity:
    """Open-slot check on interior spans of length 3. Ids only."""
    xs: list[tuple[str, ...]] = []
    ys: list[tuple[str, ...]] = []
    zs: list[tuple[str, ...]] = []
    suffix = 0
    for _name, groups in lines:
        for segment in _interior_segments(groups):
            if len(segment) != 3:
                continue
            host = tuple(stem for stem in group_stems(segment[0]) if stem != STEM_076)
            xs.append(host)
            ys.append(group_stems(segment[1]))
            zs.append(group_stems(segment[2]))
            suffix += _suffixed(segment[0], STEM_076)
    return SlotDiversity(
        x_tokens=len(xs),
        x_types=len(set(xs)),
        y_tokens=len(ys),
        y_types=len(set(ys)),
        z_tokens=len(zs),
        z_types=len(set(zs)),
        x_suffix=suffix,
    )


@dataclass(frozen=True)
class Gloss:
    """A published gloss. Never treated as a reading by this module."""

    sign: str
    gloss: str
    status: str
    source: str


GLOSSES: tuple[Gloss, ...] = (
    Gloss(
        sign=STEM_076,
        gloss="phallus; proposed copula, or proposed patronymic marker ure",
        status="hypothesis",
        source=(
            "Fischer 1995, Rapa Nui Journal 9(4); "
            "Fischer 1997, Rongorongo: The Easter Island Script; "
            "Davletshin 2012, Journal de la Société des Océanistes 134:95-110, "
            "citing Metoro (ure) and Kondratov 1969; "
            "Guy 1998, Anthropos 93:552-555"
        ),
    ),
    Gloss(
        sign=STEM_200,
        gloss="anthropomorphic figure; proposed name introducer ko",
        status="hypothesis",
        source=(
            "Butinov and Knorozov 1956 as reported by Davletshin 2012, "
            "Journal de la Société des Océanistes 134:95-110, and by "
            "http://kohaumotu.org/rongorongo_org/rosetta/g.html"
        ),
    ),
    Gloss(
        sign=STEM_999,
        gloss="vertical stroke (Barthel slash). Divider, or a logogram inside names",
        status="hypothesis",
        source=(
            "http://kohaumotu.org/rongorongo_org/corpus/digit.html "
            "(Barthel '/' and CEIPP 000 are written 999 here); "
            "Fischer 1995 (division marker); "
            "Davletshin 2012 (argues the staff-only stroke is not punctuation)"
        ),
    ),
)


@dataclass(frozen=True)
class BoundaryRule:
    """A segmentation hook other tracks can apply. Not a translation."""

    rule_id: str
    scope: str
    statement: str
    status: str


def boundary_rules(
    strokes: StrokeCensus,
    fischer: FischerCensus,
    genealogy: GenealogyCensus,
    content: dict[str, NullHit],
    placement: dict[str, NullHit],
    gv6_null: dict[str, NullHit],
    ia_template_null: dict[str, NullHit],
) -> tuple[BoundaryRule, ...]:
    """Candidate breaks that follow from the counts, with status attached."""
    stroke_survives = (
        strokes.pure_breaks > 0
        and content["immediate_076_group"].ge == 0
        and fischer.immediate_076_group > fischer.pure_breaks // 2
    )
    triad_tendency = placement["length_mod_3"].ge == 0 and fischer.length_mod_3 < fischer.interior
    chain_survives = genealogy.gv6_links >= 3 and gv6_null["links"].ge == 0
    staff_template_common = ia_template_null["phrases"].ge * 20 > ia_template_null["phrases"].trials
    return (
        BoundaryRule(
            rule_id="I-999-break",
            scope="text I, within a line",
            statement=(
                "Treat a group whose stem tuple is exactly (999,) as a "
                "phrase break. Keep a group that merely contains 999, "
                "such as a ligature, intact."
            ),
            status="candidate" if stroke_survives else "withheld",
        ),
        BoundaryRule(
            rule_id="I-999-076-bracket",
            scope="text I, the group after a pure 999",
            statement=(
                "The group immediately after a pure 999 usually contains "
                "076. Use that pair as a bracket. Do not assume the "
                "following span is three groups long."
            ),
            status="candidate" if stroke_survives else "withheld",
        ),
        BoundaryRule(
            rule_id="I-span-multiple-of-3",
            scope="text I, interior spans between pure 999 groups",
            statement=(
                "Span lengths fall on multiples of 3 more often than "
                "when the same strokes are placed at random. The "
                "majority-of-spans-are-triads rule does not hold."
            ),
            status="tendency" if triad_tendency else "withheld",
        ),
        BoundaryRule(
            rule_id="Gv6-200-X-Y076",
            scope="Gv6 only",
            statement=(
                "On Gv6 the repeating bracket is 200, then an open "
                "group X, then a group whose last stem is 076 and whose "
                "other stem equals the next X. 200 and 076 are the "
                "closed slots in this fragment. The transcription ties "
                "076 to the preceding sign with a dot; a cited "
                "alternative reads that 076 as the start of the next "
                "name. Either cut keeps the same handoff. Do not export "
                "the bracket past Gv6."
            ),
            status="candidate" if chain_survives else "withheld",
        ),
        BoundaryRule(
            rule_id="I-200-X-Y076",
            scope="text I",
            statement=(
                "Do not segment the Staff on 200 X Y.076. Those triples "
                "have no father-to-child chain, and a shuffle of the "
                "Staff produces as many triples often enough that the "
                "count is not a rule."
            ),
            status="withheld" if staff_template_common or genealogy.ia_links == 0 else "candidate",
        ),
    )


@dataclass(frozen=True)
class GenealogyReport:
    """Full track-3 report. Glosses stay in ``glosses`` and are hypotheses."""

    strokes: StrokeCensus
    fischer: FischerCensus
    content_null: dict[str, NullHit]
    placement_null: dict[str, NullHit]
    genealogy: GenealogyCensus
    gv6_null: dict[str, NullHit]
    gv_null: dict[str, NullHit]
    ia_template_null: dict[str, NullHit]
    triad_slots: SlotDiversity
    glosses: tuple[Gloss, ...]
    rules: tuple[BoundaryRule, ...]
    stem_counts: dict[str, dict[str, int]]


def _stem_totals(lines: list[tuple[str, list[str]]]) -> dict[str, int]:
    totals = {STEM_076: 0, STEM_200: 0, STEM_999: 0, "all": 0}
    for _name, groups in lines:
        for group in groups:
            stems = group_stems(group)
            totals["all"] += len(stems)
            for stem in (STEM_076, STEM_200, STEM_999):
                totals[stem] += stems.count(stem)
    return totals


def measure_genealogy(
    ia_lines: list[tuple[str, list[str]]],
    gv_lines: list[tuple[str, list[str]]],
    gr_lines: list[tuple[str, list[str]]],
) -> GenealogyReport:
    """Run the track-3 counts and the shuffled baselines.

    ``ia_lines``, ``gv_lines`` and ``gr_lines`` are ``(line_name, groups)``
    in the caller's line order. Groups are hyphen-separated published
    tokens, not pre-stemmed signs.
    """
    strokes = census_strokes(ia_lines)
    fischer = fischer_census(ia_lines)
    content = content_null(ia_lines, fischer)
    placement = placement_null(ia_lines, fischer)
    genealogy = genealogy_census(gv_lines, gr_lines, ia_lines)
    gv6_groups = dict(gv_lines)["Gv6"]
    gv6_null = gv6_chain_null(
        gv6_groups,
        genealogy.gv6_links,
        len(genealogy.gv6_phrases),
    )
    gv_null = pooled_template_null(
        gv_lines,
        genealogy.gv_strict,
        genealogy.gv_links,
        NULL_GV_TRIALS,
        NULL_GV_SEED,
    )
    ia_null = pooled_template_null(
        ia_lines,
        genealogy.ia_strict,
        genealogy.ia_links,
        NULL_IA_TEMPLATE_TRIALS,
        NULL_IA_TEMPLATE_SEED,
    )
    rules = boundary_rules(strokes, fischer, genealogy, content, placement, gv6_null, ia_null)
    return GenealogyReport(
        strokes=strokes,
        fischer=fischer,
        content_null=content,
        placement_null=placement,
        genealogy=genealogy,
        gv6_null=gv6_null,
        gv_null=gv_null,
        ia_template_null=ia_null,
        triad_slots=triad_slot_diversity(ia_lines),
        glosses=GLOSSES,
        rules=rules,
        stem_counts={
            "I": _stem_totals(ia_lines),
            "Gv": _stem_totals(gv_lines),
            "Gr": _stem_totals(gr_lines),
        },
    )
