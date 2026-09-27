"""Track 4: native readings against vendored Barthel codes.

Ure Vaeiko's chants are Thomson 1891. Metoro's words are Jaussen's
notebooks as transcribed by Kohaumotu. Barthel numbers are the
fixtures already vendored in tests/fixtures. Nothing here assigns a
glyph a meaning. Fischer's "076 = copula" equation is a labeled
hypothesis and is only used as a spacing prediction.

Search comparison, not a translation. No network. No live model.
"""

from __future__ import annotations

import json
import random
import re
from collections import Counter, defaultdict
from html import unescape
from pathlib import Path

READINGS_DIR = Path(__file__).resolve().parents[1] / "data" / "readings"
THOMSON_PAGES = READINGS_DIR / "thomson_1891" / "pages"
METORO_LINES = READINGS_DIR / "metoro_jaussen" / "lines"
FIXTURES = Path(__file__).resolve().parents[1] / "tests" / "fixtures"

# Thomson prints the copula as "Ki ai Kiroto" or "Kia ai Kiroto".
_FRAME = re.compile(r"\b(?:kia\s+ai\s+kiroto|ki\s+ai\s+kiroto)\b", re.IGNORECASE)
# "Kapu te", "Kapu to", and the one printed "Mapu te".
_PRODUCT = re.compile(r"\b(?:kapu|mapu)\s+(?:te|to)\b", re.IGNORECASE)
_WORD = re.compile(r"[A-Za-z']+")
_LINE_HEADER = re.compile(r'<h3><a name="Line_(\d+)">')
_ALLOGRAPH = re.compile(r"[A-Za-z?*!]+")
_SUP_BREAK = re.compile(r"<SUP>\s*__\s*</SUP>", re.IGNORECASE)
_ITALIC = re.compile(r"<I\b[^>]*>.*?</I>", re.IGNORECASE | re.DOTALL)
_ANCHOR = re.compile(r"<A\b[^>]*>.*?</A>", re.IGNORECASE | re.DOTALL)
_PAGE_REF = re.compile(r"\[p\.\d+\]", re.IGNORECASE)
_GROUP_INDEX = re.compile(r"=\d+=")
_ROMAN = re.compile(r"\([IVXLC]+\)\.?")
_LINE_LABEL = re.compile(r"^[A-Z][a-z]\d+\.?\s*")

# Content-word overlap ignores these grammatical pieces. They are not glosses.
_FUNCTION = frozenset(
    "te ki i e o a ka kua ko ia mai no mo ra to tuu koe au era ta ma".split()
)

SHUFFLE_SEED = 0
SHUFFLE_TRIALS = 1000
MIN_REPEATS = 3

# Vendored Barthel pages for the tablets named in the sources.
TABLET_FILES = {
    "Ra": FIXTURES / "atua_ra_html" / "Ra_barthel.json",
    "Rb": FIXTURES / "atua_rb_html" / "Rb_barthel.json",
    "Ia": FIXTURES / "santiago_ia_html" / "Ia.html",
    "Sa": FIXTURES / "washington_sa_html" / "Sa.html",
    "Sb": FIXTURES / "washington_sb_html" / "Sb.html",
    "Da": FIXTURES / "echancree_da_html" / "Da.html",
    "Db": FIXTURES / "echancree_db_html" / "Db.html",
    "Er": FIXTURES / "keiti_er_html" / "Er.html",
    "Ev": FIXTURES / "keiti_ev_html" / "Ev.html",
    "Ca": FIXTURES / "mamari_ca_html" / "Ca.html",
    "Cb": FIXTURES / "mamari_cb_html" / "Cb.html",
    "Aa": FIXTURES / "tahua_aa_html" / "Aa.html",
    "Ab": FIXTURES / "tahua_ab_html" / "Ab.html",
    "Br": FIXTURES / "aruku_br_html" / "Br.html",
    "Bv": FIXTURES / "aruku_bv_html" / "Bv.html",
}

METORO_LINE_COUNTS = {
    "Br": 10,
    "Bv": 12,
    "Ab": 8,
    "Aa": 8,
    "Cb": 14,
    "Ca": 14,
    "Er": 9,
    "Ev": 8,
}

# Later catalog says which Thomson plates to compare. See SOURCE.md.
# The staff is Fischer's hypothesis, not a Thomson plate.
CHANT_TABLETS = {
    "apai": ("Er", "Ev"),
    "atua_matariri": ("Ra", "Rb"),
    "eaha": ("Sa", "Sb"),
    "ka_ihi_uiga": ("Da", "Db"),
    "ate_a_renga": ("Ca", "Cb"),
}


def thomson_page_text(page: int) -> str:
    """Plain text of one vendored Thomson page transcription."""
    html = (THOMSON_PAGES / f"{page}.html").read_text(encoding="latin-1")
    html = unescape(html)
    html = re.sub(r"(?i)<br\s*/?>", "\n", html)
    html = re.sub(r"<[^>]+>", "", html)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in html.splitlines()]
    return "\n".join(line for line in lines if line)


def atua_matariri_verses() -> list[str]:
    """The 48 printed Atua Matariri verses on Thomson 1891 pp. 520–521.

    English on those pages is not returned. A verse is one printed line
    of the Rapanui chant, including the seven lines that drop the formula.
    """
    verses: list[str] = []
    marker = re.compile(
        r"Ki ai|Kia ai|Kapu|Mapu te|Atimoterae|E\. Toto|Epuoko|Numia|Kamau|Turuki|Kaunuku"
    )
    for page in (520, 521):
        for line in thomson_page_text(page).splitlines():
            if marker.search(line):
                verses.append(line)
    return verses


def _word_count(text: str) -> int:
    return len(_WORD.findall(text))


def parse_atua_formula(verses: list[str]) -> dict:
    """Count the copulation frame and the name slots around it.

    A full verse matches Thomson's printed frame and a product marker.
    X, Y, Z are the printed name-strings, not translations. Adjacent
    gaps count words in Y + Z + the next verse's X, and only when the
    next printed verse is also a full formula verse. The product
    marker's own words are not part of that gap: the hypothesis under
    test is that the marker is either unwritten or is the delimiter,
    so it must not be smuggled into the gap it is supposed to explain.
    """
    parsed: list[dict | None] = []
    for verse in verses:
        frame = _FRAME.search(verse)
        if frame is None:
            parsed.append(None)
            continue
        product = _PRODUCT.search(verse, frame.end())
        if product is None:
            parsed.append(None)
            continue
        parsed.append(
            {
                "x": verse[: frame.start()].strip(" ;:,."),
                "y": verse[frame.end() : product.start()].strip(" ;:,."),
                "z": verse[product.end() :].strip(" ;:,."),
            }
        )
    full_indexes = [index for index, item in enumerate(parsed) if item is not None]
    adjacent_gaps: list[int] = []
    for left, right in zip(full_indexes, full_indexes[1:]):
        if right != left + 1:
            continue
        left_item = parsed[left]
        right_item = parsed[right]
        assert left_item is not None and right_item is not None
        adjacent_gaps.append(
            _word_count(left_item["y"])
            + _word_count(left_item["z"])
            + _word_count(right_item["x"])
        )
    names: dict[str, list[str]] = {"x": [], "y": [], "z": []}
    for item in parsed:
        if item is None:
            continue
        for slot in names:
            names[slot].append(re.sub(r"\s+", " ", item[slot].lower()).strip())
    repeated = {
        slot: sorted(name for name, count in Counter(values).items() if count > 1)
        for slot, values in names.items()
    }
    return {
        "verse_count": len(verses),
        "full_formula_count": len(full_indexes),
        "frame_count": sum(1 for verse in verses if _FRAME.search(verse)),
        "product_count": sum(1 for verse in verses if _PRODUCT.search(verse)),
        "adjacent_gap_count": len(adjacent_gaps),
        "adjacent_gap_histogram": dict(sorted(Counter(adjacent_gaps).items())),
        "adjacent_gap_mode3": sum(1 for gap in adjacent_gaps if gap == 3),
        "repeated_names": repeated,
        "repeated_x_count": len(repeated["x"]),
        "repeated_y_count": len(repeated["y"]),
        "repeated_z_count": len(repeated["z"]),
    }


def _stems_from_token(token: str) -> list[str]:
    """Same mechanical stem split as the calendar scoreboard.

    Ligatures stay ordered. Letter suffixes and a leading V are stripped.
    No code is invented and none is remapped onto another number.
    """
    stems: list[str] = []
    piece = token.strip().rstrip("*")
    if not piece:
        return stems
    for part in piece.replace(":", ".").split("."):
        part = part.strip()
        if part.startswith("V") and len(part) > 1 and part[1].isdigit():
            part = part[1:]
        part = _ALLOGRAPH.sub("", part)
        if part.isdigit():
            stems.append(part.zfill(3))
    return stems


def normalized_token(token: str) -> str:
    """Published sign code with allograph letters removed, ligature kept."""
    stems = _stems_from_token(token)
    return ".".join(stems)


def load_barthel_lines(side: str) -> dict[str, list[str]]:
    """Published tokens for one side, keyed by line name.

    JSON fixtures already store one token per item. HTML fixtures are
    copied from digit-bearing <td> text, split on hyphens, same rule as
    the Santiago Ia scoreboard.
    """
    path = TABLET_FILES[side]
    if path.suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        return {name: [str(token) for token in tokens] for name, tokens in payload["lines"].items()}
    html = path.read_text(encoding="utf-8")
    chunks = _LINE_HEADER.split(html)
    lines: dict[str, list[str]] = {}
    for index in range(1, len(chunks), 2):
        name = f"{side}{int(chunks[index])}"
        tokens: list[str] = []
        for cell in re.findall(r"<td>([^<]*)</td>", chunks[index + 1]):
            text = unescape(cell).strip()
            if not text or not any(character.isdigit() for character in text):
                continue
            tokens.extend(part.strip() for part in text.split("-") if part.strip())
        lines[name] = tokens
    return lines


def line_stems(tokens: list[str]) -> list[str]:
    stems: list[str] = []
    for token in tokens:
        stems.extend(_stems_from_token(token))
    return stems


def side_stem_total(side: str) -> int:
    return sum(len(line_stems(tokens)) for tokens in load_barthel_lines(side).values())


def stem_count_on_sides(sides: tuple[str, ...], stem: str) -> int:
    total = 0
    for side in sides:
        for tokens in load_barthel_lines(side).values():
            total += line_stems(tokens).count(stem)
    return total


def interior_gaps(lines: list[list[str]], delimiter: str) -> list[int]:
    """Stems strictly between successive delimiter hits on the same line.

    The partial run before the first hit and after the last hit is not
    a gap. A line with fewer than two hits contributes no gap.
    """
    gaps: list[int] = []
    for line in lines:
        run = 0
        seen = False
        for stem in line:
            if stem == delimiter:
                if seen:
                    gaps.append(run)
                seen = True
                run = 0
            elif seen:
                run += 1
    return gaps


def staff_lines() -> list[list[str]]:
    published = load_barthel_lines("Ia")
    return [line_stems(published[f"Ia{index}"]) for index in range(1, 15)]


def tablet_r_lines() -> list[list[str]]:
    ra = load_barthel_lines("Ra")
    rb = load_barthel_lines("Rb")
    lines = [line_stems(ra[f"Ra{index}"]) for index in range(1, 9)]
    lines.extend(line_stems(rb[f"Rb{index}"]) for index in range(1, 10))
    return lines


def _gap_histogram(gaps: list[int]) -> dict[int, int]:
    return dict(sorted(Counter(gaps).items()))


def _binned_share(gaps: list[int]) -> tuple[int, ...]:
    """Counts in bins 0, 1, 2, 3, 4, and 5-or-more. Integers only."""
    bins = [0, 0, 0, 0, 0, 0]
    for gap in gaps:
        bins[5 if gap >= 5 else gap] += 1
    return tuple(bins)


def _l1_counts(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    """L1 distance of two histograms after scaling each to 10000.

    Integer arithmetic so a shuffle comparison does not depend on
    binary float rounding.
    """
    left_n = sum(left) or 1
    right_n = sum(right) or 1
    return sum(abs((a * 10000) // left_n - (b * 10000) // right_n) for a, b in zip(left, right))


def staff_delimiter_test(chant_gaps: list[int], trials: int = SHUFFLE_TRIALS, seed: int = SHUFFLE_SEED) -> dict:
    """Is staff 076 spacing tighter than a within-line shuffle?

    The shuffle keeps each line's multiset of stems, so the number of
    076s on each line stays put. Only their positions change. The chant
    gaps are the adjacent name-slot widths from Atua Matariri. Closeness
    to that histogram is reported, and it is not an independent fact
    from the peak at 3: the chant widths were defined as three name slots.
    """
    lines = staff_lines()
    observed = interior_gaps(lines, "076")
    observed_bins = _binned_share(observed)
    chant_bins = _binned_share(chant_gaps)
    observed_l1 = _l1_counts(chant_bins, observed_bins)
    observed_len3 = sum(1 for gap in observed if gap == 3)
    generator = random.Random(seed)
    null_len3_ge = 0
    null_l1_le = 0
    for _ in range(trials):
        shuffled = []
        for line in lines:
            row = line[:]
            generator.shuffle(row)
            shuffled.append(row)
        gaps = interior_gaps(shuffled, "076")
        if sum(1 for gap in gaps if gap == 3) >= observed_len3:
            null_len3_ge += 1
        if _l1_counts(chant_bins, _binned_share(gaps)) <= observed_l1:
            null_l1_le += 1
    return {
        "stem_total": sum(len(line) for line in lines),
        "delimiter_count": sum(line.count("076") for line in lines),
        "interior_gap_count": len(observed),
        "interior_gap_histogram": _gap_histogram(observed),
        "interior_gap_len3": observed_len3,
        "chant_gap_bins": chant_bins,
        "staff_gap_bins": observed_bins,
        "l1_scaled": observed_l1,
        "trials": trials,
        "seed": seed,
        "null_len3_ge_observed": null_len3_ge,
        "null_l1_le_observed": null_l1_le,
    }


def adjacent_chant_gaps(verses: list[str]) -> list[int]:
    """Name-slot widths between successive full formula verses."""
    parsed = parse_atua_formula(verses)
    # Recompute the list; the histogram in parse_atua_formula is the lock.
    gaps: list[int] = []
    full: list[dict | None] = []
    for verse in verses:
        frame = _FRAME.search(verse)
        product = _PRODUCT.search(verse, frame.end()) if frame else None
        if frame is None or product is None:
            full.append(None)
            continue
        full.append(
            {
                "x": _word_count(verse[: frame.start()]),
                "y": _word_count(verse[frame.end() : product.start()]),
                "z": _word_count(verse[product.end() :]),
            }
        )
    indexes = [index for index, item in enumerate(full) if item is not None]
    for left, right in zip(indexes, indexes[1:]):
        if right != left + 1:
            continue
        left_item = full[left]
        right_item = full[right]
        assert left_item is not None and right_item is not None
        gaps.append(left_item["y"] + left_item["z"] + right_item["x"])
    if _gap_histogram(gaps) != parsed["adjacent_gap_histogram"]:
        raise RuntimeError("chant gap histogram drifted from the formula parser")
    return gaps


def metoro_groups(html: str) -> list[str]:
    """Jaussen's hyphen-groups, in the order printed on the Kohaumotu page.

    Italics (his comments and the English beside them) are dropped.
    '=01=' locators and '[p.94]' page marks are dropped. They are not signs.
    An empty group between two hyphens is kept: a blank is still a slot.
    The text before the first hyphen is the first group after the line
    label is removed.
    """
    match = re.search(r"</H3>\s*</div>\s*<HR>(.*)<HR>\s*<div", html, re.IGNORECASE | re.DOTALL)
    body = match.group(1) if match else html
    previous = None
    while previous != body:
        previous = body
        body = _ITALIC.sub(" ", body)
    body = _ANCHOR.sub(" ", body)
    body = _PAGE_REF.sub(" ", body)
    body = _GROUP_INDEX.sub(" ", body)
    parts = _SUP_BREAK.split(body)
    groups: list[str] = []
    for part in parts:
        text = re.sub(r"<[^>]+>", " ", part)
        text = unescape(text).replace("\xa0", " ")
        text = _ROMAN.sub(" ", text)
        text = re.sub(r"\s+", " ", text).strip()
        text = _LINE_LABEL.sub("", text).strip(" \t-—.,;:[]")
        text = re.sub(r"\s+", " ", text).strip()
        groups.append(text)
    while groups and not groups[0]:
        groups.pop(0)
    while groups and not groups[-1]:
        groups.pop()
    return groups


def normalize_phrase(phrase: str) -> str:
    text = phrase.lower()
    text = text.translate(str.maketrans("áàâäéèêëíìîïóòôöúùûü", "aaaaeeeeiiiioooouuuu"))
    text = text.replace("ʻ", "").replace("'", "")
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def content_words(phrase: str) -> tuple[str, ...]:
    return tuple(word for word in normalize_phrase(phrase).split() if word not in _FUNCTION and len(word) > 1)


def load_metoro_line(side: str, index: int) -> list[str]:
    path = METORO_LINES / f"{side.lower()}{index:02d}.html"
    return metoro_groups(path.read_text(encoding="latin-1"))


def metoro_pairs() -> dict:
    """Pair groups to Barthel tokens only where the counts already match.

    Unequal lines are counted and not aligned. Forcing an alignment
    would invent a correspondence the notebooks do not record.
    """
    matched_lines: list[str] = []
    mismatched: list[tuple[str, int, int]] = []
    pairs: list[tuple[str, str, str, str]] = []
    for side, count in METORO_LINE_COUNTS.items():
        published = load_barthel_lines(side)
        for index in range(1, count + 1):
            name = f"{side}{index}"
            groups = load_metoro_line(side, index)
            tokens = published.get(name, [])
            if tokens and len(groups) == len(tokens):
                matched_lines.append(name)
                for token, group in zip(tokens, groups):
                    code = normalized_token(token)
                    if not code:
                        continue
                    pairs.append((name, code, code.split(".")[0], normalize_phrase(group)))
            else:
                mismatched.append((name, len(groups), len(tokens)))
    return {
        "matched_lines": tuple(matched_lines),
        "mismatched_line_count": len(mismatched),
        "metoro_line_count": sum(METORO_LINE_COUNTS.values()),
        "pairs": pairs,
    }


def _modal_hits(groups: list[list[str]]) -> tuple[int, int]:
    hits = 0
    total = 0
    for phrases in groups:
        hits += Counter(phrases).most_common(1)[0][1]
        total += len(phrases)
    return hits, total


def _majority_types(groups: list[list[str]]) -> int:
    """Types whose single most common phrase covers at least half the hits."""
    return len(_majority_detail(groups))


def _majority_detail(groups: list[list[str]]) -> list[tuple[int, int, str]]:
    """(n, modal count, modal phrase) for types at or above a half share."""
    rows: list[tuple[int, int, str]] = []
    for phrases in groups:
        phrase, top = Counter(phrases).most_common(1)[0]
        if top * 2 >= len(phrases):
            rows.append((len(phrases), top, phrase))
    return rows


def _majority_rows(by_key: dict[str, list[str]]) -> tuple[tuple[str, int, int, str], ...]:
    """Repeated codes whose modal phrase covers at least half the hits.

    The phrase is Metoro's wording, not a meaning assigned to the code.
    """
    rows: list[tuple[str, int, int, str]] = []
    for key, phrases in by_key.items():
        if len(phrases) < MIN_REPEATS:
            continue
        phrase, top = Counter(phrases).most_common(1)[0]
        if top * 2 >= len(phrases):
            rows.append((key, len(phrases), top, phrase))
    return tuple(sorted(rows))


def _jaccard(groups: list[list[tuple[str, ...]]]) -> int:
    """Sum of pairwise content-word overlap, scaled by 1000.

    Empty glosses share nothing. A consistent lexicon would be near
    1000. The scale is integer so the shuffle lock does not drift.
    """
    numerator = 0
    denominator = 0
    for phrases in groups:
        sets = [set(phrase) for phrase in phrases]
        for left in range(len(sets)):
            for right in range(left + 1, len(sets)):
                union = sets[left] | sets[right]
                overlap = (len(sets[left] & sets[right]) / len(union)) if union else 0.0
                numerator += int(round(overlap * 1000))
                denominator += 1
    if denominator == 0:
        return 0
    return numerator // denominator


def metoro_consistency(trials: int = SHUFFLE_TRIALS, seed: int = SHUFFLE_SEED) -> dict:
    """Do repeated Barthel codes get the same Metoro phrase?

    The null permutes phrases across the paired positions and keeps
    the codes in place. Seed and trial count are fixed.
    """
    packed = metoro_pairs()
    pairs = packed["pairs"]
    by_code: dict[str, list[str]] = defaultdict(list)
    by_stem: dict[str, list[str]] = defaultdict(list)
    by_content: dict[str, list[tuple[str, ...]]] = defaultdict(list)
    for _line, code, stem, phrase in pairs:
        by_code[code].append(phrase)
        by_stem[stem].append(phrase)
        by_content[stem].append(content_words(phrase))
    code_groups = [phrases for phrases in by_code.values() if len(phrases) >= MIN_REPEATS]
    stem_groups = [phrases for phrases in by_stem.values() if len(phrases) >= MIN_REPEATS]
    content_groups = [phrases for phrases in by_content.values() if len(phrases) >= MIN_REPEATS]
    code_hits, code_total = _modal_hits(code_groups)
    stem_hits, stem_total = _modal_hits(stem_groups)
    observed_jaccard = _jaccard(content_groups)
    codes = [code for _line, code, _stem, _phrase in pairs]
    stems = [stem for _line, _code, stem, _phrase in pairs]
    phrases = [phrase for _line, _code, _stem, phrase in pairs]
    lines = [line for line, _code, _stem, _phrase in pairs]
    contents = [content_words(phrase) for phrase in phrases]
    code_keys = [code for code, group in by_code.items() if len(group) >= MIN_REPEATS]
    stem_keys = [stem for stem, group in by_stem.items() if len(group) >= MIN_REPEATS]
    # Ab1 is the line Jaussen says was still copied in full, and its group
    # count matches the vendored tokens. Its null shuffles that line only.
    ab1_by_stem: dict[str, list[str]] = defaultdict(list)
    for line, _code, stem, phrase in pairs:
        if line == "Ab1":
            ab1_by_stem[stem].append(phrase)
    ab1_groups = [group for group in ab1_by_stem.values() if len(group) >= MIN_REPEATS]
    ab1_hits, ab1_total = _modal_hits(ab1_groups) if ab1_groups else (0, 0)
    ab1_indexes = [index for index, line in enumerate(lines) if line == "Ab1"]
    ab1_keys = [stem for stem, group in ab1_by_stem.items() if len(group) >= MIN_REPEATS]
    generator = random.Random(seed)
    ab1_generator = random.Random(seed)
    null_code_ge = 0
    null_stem_ge = 0
    null_jaccard_ge = 0
    null_ab1_ge = 0
    for _ in range(trials):
        order = list(range(len(phrases)))
        generator.shuffle(order)
        shuffled_phrases = [phrases[index] for index in order]
        shuffled_contents = [contents[index] for index in order]
        code_map: dict[str, list[str]] = defaultdict(list)
        stem_map: dict[str, list[str]] = defaultdict(list)
        content_map: dict[str, list[tuple[str, ...]]] = defaultdict(list)
        for code, stem, phrase, content in zip(codes, stems, shuffled_phrases, shuffled_contents):
            code_map[code].append(phrase)
            stem_map[stem].append(phrase)
            content_map[stem].append(content)
        shuffled_code_hits, _ = _modal_hits([code_map[key] for key in code_keys])
        shuffled_stem_hits, _ = _modal_hits([stem_map[key] for key in stem_keys])
        if shuffled_code_hits >= code_hits:
            null_code_ge += 1
        if shuffled_stem_hits >= stem_hits:
            null_stem_ge += 1
        if _jaccard([content_map[key] for key in stem_keys]) >= observed_jaccard:
            null_jaccard_ge += 1
        ab1_order = ab1_indexes[:]
        ab1_generator.shuffle(ab1_order)
        ab1_map: dict[str, list[str]] = defaultdict(list)
        for position, source in zip(ab1_indexes, ab1_order):
            ab1_map[stems[position]].append(phrases[source])
        shuffled_ab1_hits, _ = _modal_hits([ab1_map[key] for key in ab1_keys])
        if shuffled_ab1_hits >= ab1_hits:
            null_ab1_ge += 1
    return {
        "matched_lines": packed["matched_lines"],
        "matched_line_count": len(packed["matched_lines"]),
        "mismatched_line_count": packed["mismatched_line_count"],
        "metoro_line_count": packed["metoro_line_count"],
        "paired_positions": len(pairs),
        "code_types_n_ge3": len(code_groups),
        "code_modal_hits": code_hits,
        "code_modal_total": code_total,
        "code_majority_types": _majority_types(code_groups),
        "stem_types_n_ge3": len(stem_groups),
        "stem_modal_hits": stem_hits,
        "stem_modal_total": stem_total,
        "stem_majority_types": _majority_types(stem_groups),
        "stem_majority_rows": _majority_rows(by_stem),
        "content_jaccard_milli": observed_jaccard,
        "ab1_positions": len(ab1_indexes),
        "ab1_stem_types_n_ge3": len(ab1_groups),
        "ab1_modal_hits": ab1_hits,
        "ab1_modal_total": ab1_total,
        "ab1_majority_types": _majority_types(ab1_groups),
        "null_ab1_modal_ge": null_ab1_ge,
        "trials": trials,
        "seed": seed,
        "null_code_modal_ge": null_code_ge,
        "null_stem_modal_ge": null_stem_ge,
        "null_jaccard_ge": null_jaccard_ge,
    }


def chant_frame_counts() -> dict[str, int]:
    """How often each printed chant repeats its own frame words."""
    pages = {
        "apai": (517, 518),
        "eaha": (523, 524),
        "ka_ihi": (525,),
        "ate": (526,),
    }
    texts = {name: "\n".join(thomson_page_text(page) for page in page_numbers) for name, page_numbers in pages.items()}
    atua = "\n".join(atua_matariri_verses())
    texts["atua_matariri"] = atua

    def hits(name: str, pattern: str) -> int:
        return len(re.findall(pattern, texts[name], flags=re.IGNORECASE))

    return {
        "atua_frame": hits("atua_matariri", r"\b(?:kia\s+ai\s+kiroto|ki\s+ai\s+kiroto)\b"),
        "apai_frame": hits("apai", r"\b(?:kia\s+ai\s+kiroto|ki\s+ai\s+kiroto)\b"),
        "apai_apai": hits("apai", r"\bapai\b"),
        "eaha_frame": hits("eaha", r"eaha to ran ariiki kete"),
        "ka_ihi_frame": hits("ka_ihi", r"ka ihi uiga"),
        "ka_ihi_auwe": hits("ka_ihi", r"auwe(?:\s+te)?\s+poki"),
        "ate_frame": hits("ate", r"\b(?:kia\s+ai\s+kiroto|ki\s+ai\s+kiroto)\b"),
        "ate_hoa": hits("ate", r"\bhoa\b"),
    }


def track4_report() -> dict:
    """All locked counts for this track. Deterministic given the fixtures."""
    verses = atua_matariri_verses()
    formula = parse_atua_formula(verses)
    gaps = adjacent_chant_gaps(verses)
    staff = staff_delimiter_test(gaps)
    r_lines = tablet_r_lines()
    metoro = metoro_consistency()
    frames = chant_frame_counts()
    assigned = {}
    for chant, sides in CHANT_TABLETS.items():
        assigned[chant] = {
            "sides": sides,
            "stems": sum(side_stem_total(side) for side in sides),
            "stem_076": stem_count_on_sides(sides, "076"),
        }
    return {
        "formula": formula,
        "staff": staff,
        "tablet_r_stems": sum(len(line) for line in r_lines),
        "tablet_r_076": sum(line.count("076") for line in r_lines),
        "tablet_r_lines": len(r_lines),
        "metoro": metoro,
        "frames": frames,
        "assigned": assigned,
    }
