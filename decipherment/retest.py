"""Re-run every headline test on a transcription file and compare with the baseline.

    python -m decipherment.retest --transcription data/decipherment/transcriptions/barthel_ceipp.csv

The tests and their shuffle nulls are the existing repository functions
(rounds 1–6). This module only feeds them lines from a transcription file
instead of the vendored HTML pages. No decision rule is changed. A test
whose lines are missing is reported as not computable. ``MockProvider`` is
accepted and never called; no network and no paid API is used.
"""

from __future__ import annotations

import argparse
import copy
import json
import random
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

from agents.base.providers import MockProvider
from decipherment.inventories import encode_lines
from decipherment.round2_trackb import SLOT_SEED as SLOT076_SEED
from decipherment.round2_trackb import SLOT_TRIALS as SLOT076_TRIALS
from decipherment.round2_trackb import Anchors, LineText, _outside_076_groups, _slot_null
from decipherment.round3_trackb import (
    between_delimiter_040,
    count_378_delimiters,
    flatten,
    guy_040_counts,
    runs_around_152,
    shuffle_kokore_hits,
    stem_lines,
    SHUFFLE_DRAWS as KOKORE_DRAWS,
    SHUFFLE_SEED as KOKORE_SEED,
)
from decipherment.round4_tracka import (
    SLOT_SEED as BIRD_SEED,
    SLOT_TRIALS as BIRD_TRIALS,
    _classify_pairs,
    _slot_null as _bird_slot_null,
    _slot_pairs,
    class_of,
)
from decipherment.round5b_ceipp import _bird_pair
from decipherment.track3_genealogy import (
    NULL_CONTENT_SEED,
    NULL_CONTENT_TRIALS,
    NULL_GV6_SEED,
    NULL_GV6_TRIALS,
    NULL_GV_SEED,
    NULL_GV_TRIALS,
    chain_links,
    content_null,
    extract_strict_phrases,
    fischer_census,
    group_stems,
    gv6_chain_null,
    pooled_template_null,
)
from decipherment.track_c_parallels import (
    NULL_SEED as PARALLEL_NULL_SEED,
    NULL_TRIALS as PARALLEL_NULL_TRIALS,
    SideText,
    _column_counts,
    _passage_dict,
    _substitution_report,
    find_passages,
    null_max_scores,
    smith_waterman,
)
from decipherment.transcription import BASELINE_CSV, Corpus, barthel_corpus, read_csv
from parsers.native_readings import SHUFFLE_SEED as GAP_SEED
from parsers.native_readings import SHUFFLE_TRIALS as GAP_TRIALS
from parsers.native_readings import interior_gaps, line_stems

REPO_ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = REPO_ROOT / "data" / "decipherment" / "retest_baseline.json"
PASSAGE_PATH = REPO_ROOT / "data" / "decipherment" / "substitution_classes.json"
DEFAULT_OUT = REPO_ROOT / "data" / "decipherment" / "retest"

# The repository's adoption line for a shuffle null (ADOPT_FRACTION in rounds 2 and 4).
NULL_GATE = 0.05
OPENERS = frozenset({"390"})
CALENDAR_LINES = ("Ca6", "Ca7", "Ca8", "Ca9")
# Calendar window in Barthel group positions: Ca6 from group 18 (stem 24,
# the 390.041-315y-041 delimiter), all of Ca7 and Ca8, Ca9 groups 0–1.
# These are the bounds of tests/fixtures/mamari_ca6_ca9_barthel.json.
CALENDAR_CA6_FIRST_GROUP = 18
CALENDAR_CA9_GROUPS = 2
STAFF_LINES = tuple(f"Ia{n}" for n in range(1, 15))
HEADLINE_PASSAGE_ID = "P001"
GREAT_TRADITION = ("H", "P", "Q")

STATUS_SAME = "holds (same)"
STATUS_HOLDS = "holds (changed)"
STATUS_BREAKS = "breaks"
STATUS_NA = "not computable"
STATUS_CHANGED = "changed (count only, no null)"
STATUS_PARTIAL_HOLDS = "holds (partial corpus)"
STATUS_PARTIAL_WEAK = "inconclusive (partial corpus)"


# ---------------------------------------------------------------- adapters


def side_texts(corpus: Corpus, mode: str = "stem") -> tuple[SideText, ...]:
    """``track_c_parallels.load_side_texts`` on a corpus instead of the vendored pages."""
    texts: list[SideText] = []
    for raw in corpus.located_sides():
        signs: list[str] = []
        spans: list[tuple[str, int, int]] = []
        for number, tokens in raw.lines:
            encoded = encode_lines([list(tokens)], mode)
            row = encoded[0] if encoded else []
            start = len(signs)
            signs.extend(row)
            if row:
                spans.append((f"{raw.side}{number}", start, len(signs)))
        if signs:
            texts.append(SideText(raw.side[0], raw.side, raw.path, tuple(signs), tuple(spans)))
    texts.sort(key=lambda item: item.side)
    return tuple(texts)


def line_texts(corpus: Corpus) -> tuple[LineText, ...]:
    return tuple(
        LineText(side=side, number=number, groups=groups, stems=tuple(group_stems(t) for t in groups))
        for side, number, groups in corpus.lines
    )


def anchors_for(lines: tuple[LineText, ...]) -> Anchors:
    """``round2_trackb.build_anchors`` without requiring Gv6 or the Staff to exist."""
    chain: set[int] = set()
    for line in lines:
        if line.side == "Gv" and line.number == 6:
            for phrase in extract_strict_phrases(line.groups, line.line_id):
                chain.update(range(phrase.index, phrase.index + 3))
    bracket: set[tuple[int, int]] = set()
    for line in lines:
        if line.side != "Ia":
            continue
        for index, token in enumerate(line.groups):
            if group_stems(token) == ("999",) and index + 1 < len(line.groups):
                if "076" in group_stems(line.groups[index + 1]):
                    bracket.add((line.number, index + 1))
    return Anchors(frozenset(chain), frozenset(bracket), frozenset())


def _missing(corpus: Corpus, names: tuple[str, ...]) -> list[str]:
    have = corpus.line_map()
    return [name for name in names if name not in have]


def _null(trials: int, seed: int, ge: int, *, observed: Any = None) -> dict[str, Any]:
    return {
        "trials": trials,
        "seed": seed,
        "observed": observed,
        "ge": ge,
        "fraction": ge / trials if trials else None,
        "p_add_one": (ge + 1) / (trials + 1) if trials else None,
    }


def _na(reason: str) -> dict[str, Any]:
    return {"computable": False, "reason": reason, "values": {}, "nulls": {}}


def _ok(values: dict[str, Any], nulls: dict[str, Any] | None = None, notes: list[str] | None = None) -> dict[str, Any]:
    return {"computable": True, "reason": None, "values": values, "nulls": nulls or {}, "notes": notes or []}


# ---------------------------------------------------------------- tests


def _calendar_lines(corpus: Corpus) -> dict[str, tuple[str, ...]] | None:
    have = corpus.line_map()
    if any(name not in have for name in CALENDAR_LINES):
        return None
    return {
        "Ca6": have["Ca6"][CALENDAR_CA6_FIRST_GROUP:],
        "Ca7": have["Ca7"],
        "Ca8": have["Ca8"],
        "Ca9": have["Ca9"][:CALENDAR_CA9_GROUPS],
    }


def test_calendar(corpus: Corpus, nulls: bool) -> dict[str, Any]:
    tokens = _calendar_lines(corpus)
    if tokens is None:
        return _na("missing lines: " + ", ".join(_missing(corpus, CALENDAR_LINES)))
    lines = stem_lines(tokens)
    flat = flatten(lines)
    if flat.count("152") != 1:
        return _na(f"the calendar window has {flat.count('152')} copies of 152; the split needs exactly one")
    before, after = guy_040_counts(lines, OPENERS)
    runs_before, runs_after = runs_around_152(lines)
    at = flat.index("152")
    values = {
        "calendar_stems": len(flat),
        "calendar_040": flat.count("040"),
        "calendar_040_before_152": before,
        "calendar_040_after_152": after,
        "calendar_152": flat.count("152"),
        "calendar_143": flat.count("143"),
        "143_immediately_before_152": at > 0 and flat[at - 1] == "143",
        "kokore_runs_6_before_5_after": 6 in runs_before and 5 in runs_after,
    }
    out_nulls = {}
    if nulls:
        out_nulls["kokore_shuffle"] = _null(
            KOKORE_DRAWS, KOKORE_SEED, shuffle_kokore_hits(flat), observed=values["kokore_runs_6_before_5_after"]
        )
    return _ok(values, out_nulls)


def test_delimiters(corpus: Corpus, nulls: bool) -> dict[str, Any]:
    tokens = _calendar_lines(corpus)
    if tokens is None:
        return _na("missing lines: " + ", ".join(_missing(corpus, CALENDAR_LINES)))
    lines = stem_lines(tokens)
    return _ok(
        {
            "calendar_040_gaps": list(between_delimiter_040(lines, OPENERS)),
            "calendar_full_delimiters": count_378_delimiters(lines, OPENERS),
        }
    )


def test_gv6(corpus: Corpus, nulls: bool) -> dict[str, Any]:
    have = corpus.line_map()
    if "Gv6" not in have:
        return _na("missing line: Gv6")
    groups = list(have["Gv6"])
    phrases = extract_strict_phrases(groups, "Gv6")
    links = chain_links(phrases)
    values = {
        "gv6_groups": len(groups),
        "gv6_phrases": len(phrases),
        "gv6_handoffs": links,
        "gv6_child_names": [".".join(phrase.child) for phrase in phrases],
    }
    out_nulls = {}
    if nulls:
        line_null = gv6_chain_null(groups, links, len(phrases))
        out_nulls["gv6_group_shuffle"] = _null(NULL_GV6_TRIALS, NULL_GV6_SEED, line_null["links"].ge, observed=links)
        gv_lines = [(f"Gv{number}", list(tokens)) for number, tokens in corpus.side_lines("Gv")]
        strict = 0
        verso_links = 0
        for name, tokens in gv_lines:
            found = extract_strict_phrases(tokens, name)
            strict += len(found)
            verso_links += chain_links(found)
        verso = pooled_template_null(gv_lines, strict, verso_links, NULL_GV_TRIALS, NULL_GV_SEED)
        out_nulls["gv_verso_shuffle"] = _null(NULL_GV_TRIALS, NULL_GV_SEED, verso["links"].ge, observed=verso_links)
    return _ok(values, out_nulls)


def _staff(corpus: Corpus) -> list[tuple[str, list[str]]] | None:
    have = corpus.line_map()
    if any(name not in have for name in STAFF_LINES):
        return None
    return [(name, list(have[name])) for name in STAFF_LINES]


def test_staff(corpus: Corpus, nulls: bool) -> dict[str, Any]:
    lines = _staff(corpus)
    if lines is None:
        return _na("missing lines: " + ", ".join(_missing(corpus, STAFF_LINES)))
    census = fischer_census(lines)
    values = {
        "staff_076_after_999": census.immediate_076_group,
        "staff_pure_999": census.pure_breaks,
        "staff_076_after_999_rate": round(census.immediate_076_group / census.pure_breaks, 6)
        if census.pure_breaks
        else None,
    }
    out_nulls = {}
    if nulls:
        hit = content_null(lines, census)["immediate_076_group"]
        out_nulls["staff_keep_bars_shuffle"] = _null(
            NULL_CONTENT_TRIALS, NULL_CONTENT_SEED, hit.ge, observed=census.immediate_076_group
        )
    return _ok(values, out_nulls)


def test_staff_gaps(corpus: Corpus, nulls: bool) -> dict[str, Any]:
    lines = _staff(corpus)
    if lines is None:
        return _na("missing lines: " + ", ".join(_missing(corpus, STAFF_LINES)))
    stems = [line_stems(groups) for _name, groups in lines]
    gaps = interior_gaps(stems, "076")
    observed3 = sum(1 for gap in gaps if gap == 3)
    values = {
        "staff_076": sum(line.count("076") for line in stems),
        "staff_076_gaps": len(gaps),
        "staff_076_gap_len3": observed3,
        "staff_076_gap_len4": sum(1 for gap in gaps if gap == 4),
    }
    out_nulls = {}
    if nulls:
        # Same draws as parsers.native_readings.staff_delimiter_test.
        rng = random.Random(GAP_SEED)
        ge = 0
        for _ in range(GAP_TRIALS):
            shuffled = []
            for line in stems:
                row = line[:]
                rng.shuffle(row)
                shuffled.append(row)
            ge += sum(1 for gap in interior_gaps(shuffled, "076") if gap == 3) >= observed3
        out_nulls["staff_line_shuffle_len3"] = _null(GAP_TRIALS, GAP_SEED, ge, observed=observed3)
    return _ok(values, out_nulls)


def test_group_final_076(corpus: Corpus, nulls: bool) -> dict[str, Any]:
    lines = line_texts(corpus)
    anchors = anchors_for(lines)
    values: dict[str, Any] = {}
    out_nulls: dict[str, Any] = {}
    notes = []
    for label, tablet in (("staff", "I"), ("other", None)):
        groups = _outside_076_groups(lines, anchors, tablet=tablet)
        eligible, finals, null = _slot_null(groups)
        if not eligible:
            notes.append(f"no eligible 076 groups for the {label} cut")
            continue
        values[f"{label}_eligible_groups"] = eligible
        values[f"{label}_final_076"] = finals
        if nulls:
            out_nulls[f"{label}_random_slot"] = _null(SLOT076_TRIALS, SLOT076_SEED, _ge(null), observed=finals)
    if not values:
        return _na("no group holding one 076 and another sign: " + "; ".join(notes))
    return _ok(values, out_nulls, notes)


def _ge(null: Any) -> int:
    for name in ("ge", "null_ge", "hits"):
        if hasattr(null, name):
            return int(getattr(null, name))
    raise AttributeError(f"no ge field on {null!r}")


@lru_cache(maxsize=1)
def _stored_passages() -> tuple[dict[str, Any], ...]:
    payload = json.loads(PASSAGE_PATH.read_text(encoding="utf-8"))
    return tuple(payload["stem"]["passages"])


@lru_cache(maxsize=1)
def _baseline_sides() -> dict[str, SideText]:
    return {side.side: side for side in side_texts(barthel_corpus())}


def _remap_passage(passage: dict[str, Any], sides: dict[str, SideText]) -> tuple[list[list[str | None]] | None, str]:
    """Fixed baseline alignment, signs re-read from the new corpus by (line, offset).

    Returns (columns, mode). ``mode`` is ``fixed`` when every line used has
    the baseline length, ``realigned`` when Smith–Waterman was re-run on the
    same loci, or a reason string with ``None`` columns when a line is missing.
    """
    base = _baseline_sides()
    metas = (passage["left"], passage["right"])
    used_lines: set[str] = set()
    for meta in metas:
        old = base[meta["side"]]
        for index in range(meta["start"], meta["end"]):
            used_lines.add(old.locate(index)[0])
    new_spans: dict[str, tuple[str, int, int]] = {}
    for meta in metas:
        if meta["side"] not in sides:
            return None, f"missing side {meta['side']}"
        for name, start, end in sides[meta["side"]].spans:
            new_spans[name] = (meta["side"], start, end)
    missing = sorted(name for name in used_lines if name not in new_spans)
    if missing:
        return None, "missing lines " + ", ".join(missing)
    same_length = True
    for meta in metas:
        old = base[meta["side"]]
        for name, start, end in old.spans:
            if name in used_lines:
                _side, new_start, new_end = new_spans[name]
                if new_end - new_start != end - start:
                    same_length = False
    if same_length:
        columns = copy.deepcopy(passage["columns"])
        for slot, meta in enumerate(metas):
            old = base[meta["side"]]
            new = sides[meta["side"]]
            index = meta["start"]
            for column in columns:
                if column[slot] is None:
                    continue
                line, offset = old.locate(index)
                column[slot] = new.signs[new.absolute(line, offset)]
                index += 1
        return columns, "fixed"
    segments = []
    for meta in metas:
        old = base[meta["side"]]
        new = sides[meta["side"]]
        first_line, first_offset = old.locate(meta["start"])
        last_line, last_offset = old.locate(meta["end"] - 1)
        start = new.absolute(first_line, min(first_offset, new_spans[first_line][2] - new_spans[first_line][1] - 1))
        end = new.absolute(last_line, min(last_offset, new_spans[last_line][2] - new_spans[last_line][1] - 1))
        segments.append(new.signs[start : end + 1])
    *_rest, columns = smith_waterman(segments[0], segments[1])
    return [list(column) for column in columns], "realigned"


def test_hq(corpus: Corpus, nulls: bool) -> dict[str, Any]:
    sides = {side.side: side for side in side_texts(corpus)}
    headline = next(p for p in _stored_passages() if p["id"] == HEADLINE_PASSAGE_ID)
    columns, mode = _remap_passage(headline, sides)
    if columns is None:
        return _na(f"H/Q headline span {headline['left']['locus']} / {headline['right']['locus']}: {mode}")
    matches, mismatches, _gaps, left_used, right_used = _column_counts([tuple(c) for c in columns])
    notes = [] if mode == "fixed" else ["line lengths changed; the two loci were re-aligned with Smith–Waterman"]
    return _ok(
        {
            "parallel_span": max(left_used, right_used),
            "parallel_matches": matches,
            "parallel_mismatches": mismatches,
            "parallel_bird_substitutions": sum(1 for left, right in columns if _bird_pair(left, right)),
            "alignment": mode,
        },
        notes=notes,
    )


def _great_tradition_missing(corpus: Corpus) -> list[str]:
    return [tablet for tablet in GREAT_TRADITION if tablet not in corpus.tablets]


def _parallel_run(corpus: Corpus, nulls: bool) -> dict[str, Any]:
    sides = side_texts(corpus)
    by_side = {side.side: side for side in sides}
    frequencies: Counter[str] = Counter(sign for side in sides for sign in side.signs)
    raw = find_passages(sides)
    scores = null_max_scores(sides, PARALLEL_NULL_TRIALS, PARALLEL_NULL_SEED) if nulls else []
    threshold = max(scores) if scores else 0
    ranked = sorted(raw, key=lambda item: (-item.score, item.left_side, item.right_side, item.left_start))
    passages = [
        _passage_dict(passage, by_side, passage.score > threshold, f"P{index:03d}")
        for index, passage in enumerate(ranked, start=1)
    ]
    return {"sides": by_side, "passages": passages, "frequencies": frequencies, "null_scores": scores}


def test_parallels(corpus: Corpus, nulls: bool, cache: dict[str, Any]) -> dict[str, Any]:
    missing = _great_tradition_missing(corpus)
    if missing:
        return _na("the Great Tradition needs tablets H, P and Q; missing " + ", ".join(missing))
    run = cache.setdefault("parallels", _parallel_run(corpus, nulls))
    significant = [p for p in run["passages"] if p["significant"]]
    subs = _substitution_report(significant, run["frequencies"])
    systematic = [pair for pair in subs["pairs"] if pair["kind"] == "systematic"]
    pair_400_600 = next((pair["count"] for pair in subs["pairs"] if {pair["a"], pair["b"]} == {"400", "600"}), 0)
    values = {
        "candidate_passages": len(run["passages"]),
        "significant_passages": len(significant),
        "systematic_substitution_pairs": len(systematic),
        "systematic_pairs": sorted(f"{pair['a']}-{pair['b']}x{pair['count']}" for pair in systematic),
        "pair_400_600": pair_400_600,
    }
    out_nulls = {}
    if nulls:
        out_nulls["within_side_shuffle_max_score"] = {
            "trials": PARALLEL_NULL_TRIALS,
            "seed": PARALLEL_NULL_SEED,
            "observed": len(significant),
            "max_score": max(run["null_scores"]) if run["null_scores"] else 0,
            "ge": 0 if significant else None,
            "fraction": 0.0 if significant else 1.0,
        }
    return _ok(values, out_nulls)


def test_birds(corpus: Corpus, nulls: bool, cache: dict[str, Any]) -> dict[str, Any]:
    missing = _great_tradition_missing(corpus)
    if missing:
        return _na("the bird swaps are counted in the Great Tradition parallels; missing " + ", ".join(missing))
    run = cache.setdefault("parallels", _parallel_run(corpus, nulls))
    significant = [p for p in run["passages"] if p["significant"]]
    pairs, _meta = _slot_pairs(significant, run["sides"])
    observed = _classify_pairs(pairs, class_of)
    values = {
        "cross_hundred_classified": observed["cross_hundred_classified"],
        "cross_hundred_same_class": observed["cross_hundred_same_class"],
        "cross_hundred_bird": sum(
            1 for left, right in pairs
            if class_of(left) == "bird" and class_of(right) == "bird" and int(left) // 100 != int(right) // 100
        ),
    }
    # Round 6A count: bird pairs on the stored alignment of the 99 passages.
    fixed = 0
    skipped = 0
    for passage in _stored_passages():
        columns, _mode = _remap_passage(passage, run["sides"])
        if columns is None:
            skipped += 1
            continue
        fixed += sum(1 for left, right in columns if _bird_pair(left, right))
    values["corpus_bird_substitutions_fixed_alignment"] = fixed
    notes = [f"{skipped} stored passages skipped (lines missing)"] if skipped else []
    out_nulls = {}
    if nulls:
        slot = _bird_slot_null(pairs, observed)["cross_hundred"]
        out_nulls["class_label_shuffle"] = _null(BIRD_TRIALS, BIRD_SEED, slot["null_ge"], observed=slot["observed"])
    return _ok(values, out_nulls, notes)


# ---------------------------------------------------------------- registry

TESTS: tuple[dict[str, Any], ...] = (
    {"id": "calendar_040", "label": "Mamari calendar: 040 count, 13/13 split around 152, kokore runs", "fn": test_calendar,
     "headline": ("calendar_040", "calendar_040_before_152", "calendar_040_after_152", "calendar_143", "kokore_runs_6_before_5_after")},
    {"id": "calendar_delimiters", "label": "Mamari calendar: 040 gaps between delimiters", "fn": test_delimiters,
     "headline": ("calendar_040_gaps", "calendar_full_delimiters")},
    {"id": "gv6_handoff", "label": "Gv6: 200 X Y.076 phrases and handoffs", "fn": test_gv6,
     "headline": ("gv6_phrases", "gv6_handoffs")},
    {"id": "staff_bar_076", "label": "Staff: 076 in the group after a bare 999", "fn": test_staff,
     "headline": ("staff_076_after_999", "staff_pure_999")},
    {"id": "staff_076_gaps", "label": "Staff: gaps between 076 peak at 3 and 4", "fn": test_staff_gaps,
     "headline": ("staff_076_gaps", "staff_076_gap_len3", "staff_076_gap_len4")},
    {"id": "group_final_076", "label": "076 ends its group (Staff and other tablets)", "fn": test_group_final_076,
     "headline": ("staff_eligible_groups", "staff_final_076", "other_eligible_groups", "other_final_076"), "corpus_wide": True},
    {"id": "parallels", "label": "Parallel passages above the shuffle null; gated substitution pairs", "fn": test_parallels,
     "headline": ("significant_passages", "systematic_substitution_pairs", "pair_400_600"), "cache": True, "corpus_wide": True},
    {"id": "hq_headline", "label": "H/Q headline span: matches and mismatches", "fn": test_hq,
     "headline": ("parallel_span", "parallel_matches", "parallel_mismatches")},
    {"id": "bird_swaps", "label": "Bird signs (400s/600s) swap as a class", "fn": test_birds,
     "headline": ("cross_hundred_same_class", "cross_hundred_classified"), "cache": True, "corpus_wide": True},
)


def run_tests(corpus: Corpus, *, nulls: bool = True, provider: MockProvider | None = None) -> dict[str, Any]:
    provider = provider or MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("the retest harness accepts MockProvider only")
    cache: dict[str, Any] = {}
    results: dict[str, Any] = {}
    for test in TESTS:
        if test.get("cache"):
            results[test["id"]] = test["fn"](corpus, nulls, cache)
        else:
            results[test["id"]] = test["fn"](corpus, nulls)
    return {
        "source": corpus.source,
        "tablets": list(corpus.tablets),
        "sides": list(corpus.sides),
        "signs": sum(len(group_stems(g)) for _s, _n, groups in corpus.lines for g in groups),
        "provider": "MockProvider",
        "provider_calls": len(provider.get_call_history()),
        "nulls_run": nulls,
        "tests": results,
    }


def _null_passes(null: dict[str, Any]) -> bool:
    fraction = null.get("fraction")
    return fraction is not None and fraction <= NULL_GATE


def compare(result: dict[str, Any], baseline: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for test in TESTS:
        now = result["tests"][test["id"]]
        base = baseline["tests"][test["id"]]
        row = {"id": test["id"], "label": test["label"], "changes": {}, "nulls": {}, "reason": now.get("reason")}
        if not now["computable"]:
            row["status"] = STATUS_NA
            rows.append(row)
            continue
        for key in test["headline"]:
            if key in now["values"] and now["values"].get(key) != base["values"].get(key):
                row["changes"][key] = {"baseline": base["values"].get(key), "now": now["values"][key]}
        missing_keys = [key for key in test["headline"] if key not in now["values"]]
        for name, null in now["nulls"].items():
            row["nulls"][name] = {
                "baseline": f"{base['nulls'][name]['ge']}/{base['nulls'][name]['trials']}" if name in base["nulls"] else None,
                "now": f"{null['ge']}/{null['trials']}" if null.get("ge") is not None else "n/a",
                "passes": _null_passes(null),
            }
        null_changed = any(cell["baseline"] != cell["now"] for cell in row["nulls"].values())
        nulls_pass = all(cell["passes"] for cell in row["nulls"].values())
        has_null = bool(row["nulls"])
        pattern_lost = test["id"] == "calendar_040" and not now["values"].get("kokore_runs_6_before_5_after")
        partial = bool(test.get("corpus_wide")) and set(result["tablets"]) < set(baseline["tablets"])
        notes = list(now.get("notes") or [])
        if not row["changes"] and not null_changed and not missing_keys:
            row["status"] = STATUS_SAME
        elif partial:
            # Counts on a subset of tablets are not comparable with the full corpus.
            row["status"] = STATUS_PARTIAL_HOLDS if has_null and nulls_pass else STATUS_PARTIAL_WEAK
            notes.append(f"computed on tablets {''.join(result['tablets'])} only")
        elif not has_null:
            row["status"] = STATUS_CHANGED
        elif nulls_pass and not pattern_lost:
            row["status"] = STATUS_HOLDS
        else:
            row["status"] = STATUS_BREAKS
        if missing_keys:
            notes.append("not computed: " + ", ".join(missing_keys))
        row["notes"] = notes
        rows.append(row)
    return rows


def _fmt(value: Any) -> str:
    if isinstance(value, list):
        return "[" + ",".join(str(v) for v in value) + "]"
    return str(value)


def render_markdown(result: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    out = [
        f"# Retest: {result['source']}",
        "",
        f"Tablets: {''.join(result['tablets'])}. Signs: {result['signs']}. Nulls run: {'yes' if result['nulls_run'] else 'no'}. "
        f"Provider: MockProvider ({result['provider_calls']} calls).",
        "",
        "| Test | Status | Changed counts (baseline → now) | Nulls (≥ observed / draws, baseline → now) | Notes |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        changes = "; ".join(f"{k}: {_fmt(v['baseline'])} → {_fmt(v['now'])}" for k, v in row["changes"].items()) or "—"
        nulls = "; ".join(f"{k}: {v['baseline']} → {v['now']}" for k, v in row["nulls"].items()) or "—"
        notes = row["reason"] if row["status"] == STATUS_NA else "; ".join(row.get("notes") or []) or ""
        out.append(f"| {row['label']} | {row['status']} | {changes} | {nulls} | {notes} |")
    out.append("")
    return "\n".join(out)


def load_baseline() -> dict[str, Any]:
    return json.loads(BASELINE_PATH.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Re-run the rongorongo headline tests on a transcription file.")
    parser.add_argument("--transcription", type=Path, default=BASELINE_CSV)
    parser.add_argument("--out-dir", type=Path, default=None, help="default data/decipherment/retest/<file stem>")
    parser.add_argument("--no-nulls", action="store_true", help="skip the shuffle nulls (counts only)")
    parser.add_argument("--write-baseline", action="store_true", help="store this run as the baseline (Barthel file only)")
    args = parser.parse_args(argv)
    if args.write_baseline and args.transcription.resolve() != BASELINE_CSV.resolve():
        parser.error("--write-baseline is only for the converted Barthel/CEIPP file")
    corpus = read_csv(args.transcription)
    result = run_tests(corpus, nulls=not args.no_nulls)
    if args.write_baseline:
        BASELINE_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    baseline = load_baseline()
    rows = compare(result, baseline)
    out_dir = args.out_dir or DEFAULT_OUT / args.transcription.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "results.json").write_text(
        json.dumps({"result": result, "comparison": rows}, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    markdown = render_markdown(result, rows)
    (out_dir / "comparison.md").write_text(markdown, encoding="utf-8")
    print(markdown)
    print(f"wrote {out_dir / 'results.json'} and {out_dir / 'comparison.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
