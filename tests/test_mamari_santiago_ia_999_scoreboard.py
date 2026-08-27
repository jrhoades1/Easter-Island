"""Santiago Ia 999 lock: count, documented cue, split-at-999 profile.

Cycle 47 text-search lock. Uses the already-vendored Kohaumotu Ia.html
fixture (cycle 46). No invented Barthel. No Ib scrape. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.

Cycle 46 treated 999 as a stem: longest n with freq≥2 is
999 071 076 010 079 (freq 3). This cycle locks what 999 is on
this fixture, then recomputes that profile with 999 as a break.

Ia.html / ATTRIBUTION do not name 999 as a gap, damage, line-end,
or a Barthel type. That absence is the cue lock (None). Both
interpretations stay: 999 as a stem (cycle 46) and 999 as a break
(split sequences at 999, drop those stems).

Search lock, not a merge and not a translation. MockProvider only.
"""

import re
import unittest
from collections import Counter

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_600_sandwich_scoreboard import SANDWICH
from tests.test_mamari_aruku_br_scoreboard import (
    BR_LINE_NAMES,
    STANDING_LONGEST_N as BR_LONGEST_N,
    STANDING_LONGEST_NGRAM as BR_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as BR_STEM_TOTAL,
    br_line_stems,
    extract_br_published_tokens,
    load_vendored_br_html,
    score_br_repeating_ngrams,
)
from tests.test_mamari_aruku_bv_scoreboard import (
    BV_LINE_NAMES,
    STANDING_LONGEST_N as BV_LONGEST_N,
    STANDING_LONGEST_NGRAM as BV_8GRAM,
    STANDING_STEM_TOTAL as BV_STEM_TOTAL,
    bv_line_stems,
    extract_bv_published_tokens,
    load_vendored_bv_html,
    score_bv_repeating_ngrams,
)
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_cb_5gram_ca_cross_scoreboard import (
    CB_5GRAMS,
    STANDING_CA_CROSS_TABLE,
    score_cb_5gram_ca_cross,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CB_EIGHTGRAM_COUNT,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CB_LONGEST_N,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_NGRAMS,
    score_cb_repeating_ngrams,
)
from tests.test_mamari_cb_side_b_scoreboard import (
    CB_LINE_NAMES,
    cb_line_stems,
    extract_cb_published_tokens,
    load_vendored_cb_html,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import MOTIF_9GRAM
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    RemainderNgramProfile,
    RemainderNgramRow,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CA_REMAINDER_EIGHTGRAM_COUNT,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CA_REMAINDER_LONGEST_N,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    REMAINDER_LINE_NAMES,
    extract_ca_published_tokens,
    find_ngram_hits,
    load_corpus_survey,
    load_vendored_ca_html,
    remainder_line_stems,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    IA_HTML_DIR,
    IA_HTML_PATH,
    IA_LINE_NAMES,
    I_INDEX_HTML_PATH,
    STANDING_EIGHTGRAM_COUNT as IA_EIGHTGRAM_COUNT,
    STANDING_LONGEST_FREQ as IA_AS_STEM_LONGEST_FREQ,
    STANDING_LONGEST_N as IA_AS_STEM_LONGEST_N,
    STANDING_LONGEST_NGRAM as IA_AS_STEM_LONGEST_NGRAM,
    STANDING_LONGEST_SPANS as IA_AS_STEM_LONGEST_SPANS,
    STANDING_STEM_TOTAL as IA_STEM_TOTAL,
    extract_ia_published_tokens,
    ia_line_stems,
    load_vendored_ia_html,
    score_ia_repeating_ngrams,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import (
    MOTIF_10GRAM,
    STANDING_AA_MOTIF_FREQ,
    STANDING_AA_MOTIF_SPANS,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    AA_LINE_NAMES,
    STANDING_LONGEST_N as AA_LONGEST_N,
    STANDING_LONGEST_NGRAM as AA_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as AA_STEM_TOTAL,
    STANDING_TOP_8GRAM as AA_TOP_8GRAM,
    aa_line_stems,
    extract_aa_published_tokens,
    load_vendored_aa_html,
    score_aa_repeating_ngrams,
)
from tests.test_mamari_tahua_ab_9gram_motif_scoreboard import (
    MOTIF_AB_9GRAM,
    STANDING_AB_MOTIF_FREQ,
    STANDING_AB_MOTIF_SPANS,
)
from tests.test_mamari_tahua_ab_scoreboard import (
    AB_LINE_NAMES,
    STANDING_LONGEST_N as AB_LONGEST_N,
    STANDING_LONGEST_NGRAM as AB_LONGEST_NGRAM,
    STANDING_STEM_TOTAL as AB_STEM_TOTAL,
    ab_line_stems,
    extract_ab_published_tokens,
    load_vendored_ab_html,
    score_ab_repeating_ngrams,
)

STEM_999 = "999"
ROLE_CUES = ("gap", "damage", "lacuna", "illegible", "line-end")
STANDING_999_DOCUMENTED_CUE = None
STANDING_IA_HTML_999_LEFTOVERS = ()
STANDING_999_STEM_COUNT = 97
STANDING_999_PREFIX_COUNT = 3
STANDING_999_ISOLATED_COUNT = 94
STANDING_999_ONLY_AS_PREFIX = False
STANDING_999_LINE_EDGE_COUNT = 0
STANDING_999_ADJACENT_PAIRS = 0
STANDING_999_IA11_COUNT = 0
STANDING_999_PREFIX_HITS = (("Ia4", 6), ("Ia4", 25), ("Ia5", 108))
STANDING_999_PUBLISHED_FORMS = (
    ("999", 87),
    ("999h", 6),
    ("999t", 3),
    ("999.440.076", 1),
)
STANDING_SPLIT_STEM_TOTAL = 2372
STANDING_SPLIT_LONGEST_N = 5
STANDING_SPLIT_LONGEST_COUNT = 4
STANDING_SPLIT_LONGEST_FREQ = 2
STANDING_SPLIT_EIGHTGRAM_COUNT = 0
STANDING_SPLIT_TOP_8GRAM = None
# (tokens, n, freq, spans) after splitting each Ia line at 999.
STANDING_SPLIT_LONGEST_NGRAMS = (
    (("430", "076", "006", "000", "076"), 5, 2, (
            ("Ia1", 129, 134),
            ("Ia14", 162, 167),
        )),
    (("076", "010", "079", "006", "700"), 5, 2, (
            ("Ia6", 19, 24),
            ("Ia13", 72, 77),
        )),
    (("076", "011", "090", "090", "076"), 5, 2, (
            ("Ia12", 39, 44),
            ("Ia14", 102, 107),
        )),
    (("400", "070", "076", "020", "010"), 5, 2, (
            ("Ia13", 85, 90),
            ("Ia14", 126, 131),
        )),
)


def ia_html_999_leftovers(html: str) -> tuple[str, ...]:
    """999 leftovers after dropping xmlns 1999 and digit <td> cells."""
    text = html.replace('xmlns="http://www.w3.org/1999/xhtml"', "")
    text = re.sub(r"<td>[^<]*\d[^<]*</td>", "", text)
    return tuple(re.findall(r"999", text))


def documented_999_cue(attribution: str, ia_html: str) -> str | None:
    """Role named on the same line as 999 in Ia.html / ATTRIBUTION.

    Returns None when those files do not name a role. Does not invent
    a meaning. xmlns 1999 is stripped first so the year is not a cue.
    """
    leftovers = ia_html_999_leftovers(ia_html)
    found: list[str] = []
    for line in attribution.splitlines():
        if "999" not in line:
            continue
        lower = line.lower()
        found.extend(role for role in ROLE_CUES if role in lower)
    leftover_text = " ".join(leftovers).lower()
    found.extend(role for role in ROLE_CUES if role in leftover_text)
    roles = tuple(sorted(set(found)))
    if not roles:
        return None
    return roles[0] if len(roles) == 1 else ",".join(roles)


def ia_999_published_forms(published: dict[str, list[str]]) -> tuple[tuple[str, int], ...]:
    """Published token forms that contain 999, count desc then token."""
    counts: Counter[str] = Counter()
    for name in IA_LINE_NAMES:
        for token in published[name]:
            if "999" in token:
                counts[token] += 1
    return tuple(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def ia_999_hits(lines: list[list[str]]) -> tuple[tuple[str, int], ...]:
    """(line, index) for every stem 999. Search only."""
    hits: list[tuple[str, int]] = []
    for name, line in zip(IA_LINE_NAMES, lines):
        for index, stem in enumerate(line):
            if stem == STEM_999:
                hits.append((name, index))
    return tuple(hits)


def ia_999_prefix_hits(
    lines: list[list[str]],
    gram: tuple[str, ...] = IA_AS_STEM_LONGEST_NGRAM,
) -> tuple[tuple[str, int], ...]:
    """999 hits that start the cycle-46 5-gram."""
    prefix = {hit for hit in find_ngram_hits(lines, gram)}
    names = IA_LINE_NAMES
    return tuple(
        (name, index)
        for name, index in ia_999_hits(lines)
        if (names.index(name), index) in prefix
    )


def split_stems_at_999(
    line: list[str],
    stem: str = STEM_999,
) -> list[tuple[int, list[str]]]:
    """Runs of stems that are not 999, with the original start index."""
    runs: list[tuple[int, list[str]]] = []
    start: int | None = None
    for index, token in enumerate(line):
        if token == stem:
            if start is not None:
                runs.append((start, line[start:index]))
                start = None
        elif start is None:
            start = index
    if start is not None:
        runs.append((start, line[start:]))
    return runs


def ia_segments_split_at_999(
    lines: list[list[str]],
) -> tuple[list[list[str]], tuple[tuple[str, int], ...]]:
    """Ia1–Ia14 split at 999. Segments keep the original start index."""
    segments: list[list[str]] = []
    meta: list[tuple[str, int]] = []
    for name, line in zip(IA_LINE_NAMES, lines):
        for offset, run in split_stems_at_999(line):
            segments.append(run)
            meta.append((name, offset))
    return segments, tuple(meta)


def _remap_split_row(
    row: RemainderNgramRow,
    lookup: dict[str, tuple[str, int]],
) -> RemainderNgramRow:
    """Rewrite synthetic segment names back to Ia line spans."""
    spans = tuple(
        (lookup[name][0], lookup[name][1] + start, lookup[name][1] + end)
        for name, start, end in row.spans
    )
    return RemainderNgramRow(tokens=row.tokens, n=row.n, freq=row.freq, spans=spans)


def score_ia_split_999_ngrams(lines, analyzer):
    """n≥4 freq≥2 profile on Ia after splitting each line at 999."""
    segments, meta = ia_segments_split_at_999(lines)
    names = tuple(f"{name}@{offset}" for name, offset in meta)
    lookup = {f"{name}@{offset}": (name, offset) for name, offset in meta}
    profile = score_remainder_repeating_ngrams(
        segments, analyzer, line_names=names
    )
    rows = tuple(_remap_split_row(row, lookup) for row in profile.rows)
    longest_n = max((row.n for row in rows), default=0)
    eightgrams = tuple(row for row in rows if row.n == 8)
    return RemainderNgramProfile(
        rows=rows,
        longest_n=longest_n,
        longest=tuple(row for row in rows if row.n == longest_n),
        eightgrams=eightgrams,
        top_8gram=eightgrams[0] if eightgrams else None,
    )


class TestSantiagoIa999Helpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM."""

    def test_documented_cue_none_unless_role_shares_a_999_line(self):
        """A role word next to 999 is a cue; Ia.html leftovers stay empty."""
        html = (
            '<html xmlns="http://www.w3.org/1999/xhtml">'
            "<td>430.076-999-071</td>"
            "</html>"
        )
        self.assertEqual(ia_html_999_leftovers(html), ())
        self.assertIsNone(documented_999_cue("longest: 999 071 076 010 079", html))
        self.assertEqual(
            documented_999_cue("999 marks a gap in the staff", html),
            "gap",
        )
        leftover_html = html + "<p>999</p>"
        self.assertEqual(ia_html_999_leftovers(leftover_html), ("999",))
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_split_at_999_breaks_sequences_and_drops_the_stem(self):
        """999 is not a stem after the split; n-grams cannot cross it."""
        line = ["430", "076", "999", "071", "076", "010", "079"]
        self.assertEqual(
            split_stems_at_999(line),
            [(0, ["430", "076"]), (3, ["071", "076", "010", "079"])],
        )
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        padded = [[] for _ in IA_LINE_NAMES]
        padded[0] = line
        padded[-1] = ["430", "076", "006", "000", "076"]
        profile = score_ia_split_999_ngrams(padded, analyzer)
        self.assertEqual(profile.longest_n, 0)
        crossed = ("076", "999", "071")
        self.assertEqual(find_ngram_hits([line], crossed), [(0, 1)])
        segments, _meta = ia_segments_split_at_999(padded)
        self.assertEqual(find_ngram_hits(segments, crossed), [])
        self.assertNotIn(STEM_999, [stem for segment in segments for stem in segment])
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIa999Scoreboard(unittest.TestCase):
    """Cited Ia.html 999 count / cue / split profile. MockProvider only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.html = load_vendored_ia_html()
        self.attribution = (IA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.published = extract_ia_published_tokens(self.html)
        self.lines = ia_line_stems(self.published)
        self.as_stem = score_ia_repeating_ngrams(self.lines, self.analyzer)
        self.split = score_ia_split_999_ngrams(self.lines, self.analyzer)
        self.hits = ia_999_hits(self.lines)
        self.prefix = ia_999_prefix_hits(self.lines)

    def test_999_count_is_not_only_the_5gram_prefix(self):
        """97 stems; 3 start 999 071 076 010 079; 94 are isolated codes."""
        self.assertEqual(len(self.hits), STANDING_999_STEM_COUNT)
        self.assertEqual(len(self.prefix), STANDING_999_PREFIX_COUNT)
        self.assertEqual(self.prefix, STANDING_999_PREFIX_HITS)
        isolated = tuple(hit for hit in self.hits if hit not in set(self.prefix))
        self.assertEqual(len(isolated), STANDING_999_ISOLATED_COUNT)
        self.assertEqual(bool(len(isolated) == 0), STANDING_999_ONLY_AS_PREFIX)
        self.assertFalse(STANDING_999_ONLY_AS_PREFIX)
        edge = sum(
            1
            for name, index in self.hits
            if index == 0 or index + 1 == len(self.lines[IA_LINE_NAMES.index(name)])
        )
        adjacent = sum(
            1
            for line in self.lines
            for index in range(len(line) - 1)
            if line[index] == STEM_999 and line[index + 1] == STEM_999
        )
        self.assertEqual(edge, STANDING_999_LINE_EDGE_COUNT)
        self.assertEqual(adjacent, STANDING_999_ADJACENT_PAIRS)
        self.assertEqual(self.lines[10].count(STEM_999), STANDING_999_IA11_COUNT)
        self.assertEqual(IA_LINE_NAMES[10], "Ia11")
        self.assertEqual(ia_999_published_forms(self.published), STANDING_999_PUBLISHED_FORMS)
        self.assertEqual(sum(count for _form, count in STANDING_999_PUBLISHED_FORMS), 97)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_documented_cue_is_none_on_ia_html_and_attribution(self):
        """Ia.html / ATTRIBUTION do not name 999 as gap, damage, or line-end."""
        self.assertEqual(ia_html_999_leftovers(self.html), STANDING_IA_HTML_999_LEFTOVERS)
        self.assertEqual(
            documented_999_cue(self.attribution, self.html),
            STANDING_999_DOCUMENTED_CUE,
        )
        self.assertIsNone(STANDING_999_DOCUMENTED_CUE)
        self.assertFalse((IA_HTML_DIR / "Ib.html").exists())
        self.assertTrue(IA_HTML_PATH.is_file())
        self.assertTrue(I_INDEX_HTML_PATH.is_file())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_as_stem_and_split_at_999_profiles(self):
        """Stem reading keeps the cycle-46 5-gram; break reading has no 8-gram."""
        self.assertEqual(sum(len(line) for line in self.lines), IA_STEM_TOTAL)
        self.assertEqual(self.as_stem.longest_n, IA_AS_STEM_LONGEST_N)
        self.assertEqual(self.as_stem.longest[0].tokens, IA_AS_STEM_LONGEST_NGRAM)
        self.assertEqual(self.as_stem.longest[0].freq, IA_AS_STEM_LONGEST_FREQ)
        self.assertEqual(self.as_stem.longest[0].spans, IA_AS_STEM_LONGEST_SPANS)
        self.assertEqual(len(self.as_stem.eightgrams), IA_EIGHTGRAM_COUNT)

        segments, _meta = ia_segments_split_at_999(self.lines)
        self.assertEqual(sum(len(segment) for segment in segments), STANDING_SPLIT_STEM_TOTAL)
        self.assertEqual(STANDING_SPLIT_STEM_TOTAL, IA_STEM_TOTAL - STANDING_999_STEM_COUNT)
        self.assertNotIn(STEM_999, [stem for segment in segments for stem in segment])
        self.assertEqual(self.split.longest_n, STANDING_SPLIT_LONGEST_N)
        self.assertEqual(len(self.split.longest), STANDING_SPLIT_LONGEST_COUNT)
        self.assertEqual(
            tuple((row.tokens, row.n, row.freq, row.spans) for row in self.split.longest),
            STANDING_SPLIT_LONGEST_NGRAMS,
        )
        self.assertTrue(all(row.freq == STANDING_SPLIT_LONGEST_FREQ for row in self.split.longest))
        self.assertNotIn(STEM_999, [stem for row in self.split.longest for stem in row.tokens])
        self.assertIsNone(self.split.top_8gram)
        self.assertEqual(STANDING_SPLIT_TOP_8GRAM, None)
        self.assertEqual(len(self.split.eightgrams), STANDING_SPLIT_EIGHTGRAM_COUNT)
        self.assertEqual(STANDING_SPLIT_EIGHTGRAM_COUNT, 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_a_b_c_and_ia_scoreboards_still_compute(self):
        """Aa / Ab / Br / Bv / Guy / Ca 9-gram / sandwich / Ia as-stem stay."""
        aa = aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html()))
        ab = ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html()))
        br = br_line_stems(extract_br_published_tokens(load_vendored_br_html()))
        bv = bv_line_stems(extract_bv_published_tokens(load_vendored_bv_html()))
        calendar = fixture_line_stems(load_mamari_fixture())
        remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        cb_lines = cb_line_stems(extract_cb_published_tokens(load_vendored_cb_html()))

        aa_profile = score_aa_repeating_ngrams(aa, self.analyzer)
        self.assertEqual(sum(len(line) for line in aa), AA_STEM_TOTAL)
        self.assertEqual(aa_profile.longest_n, AA_LONGEST_N)
        self.assertEqual(aa_profile.longest[0].tokens, AA_LONGEST_NGRAM)
        self.assertEqual(aa_profile.top_8gram.tokens, AA_TOP_8GRAM)
        aa_motif = find_ngram_hits(aa, MOTIF_10GRAM)
        self.assertEqual(len(aa_motif), STANDING_AA_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AA_LINE_NAMES[line_index], start, start + len(MOTIF_10GRAM))
                for line_index, start in aa_motif
            ),
            STANDING_AA_MOTIF_SPANS,
        )

        ab_profile = score_ab_repeating_ngrams(ab, self.analyzer)
        self.assertEqual(sum(len(line) for line in ab), AB_STEM_TOTAL)
        self.assertEqual(ab_profile.longest_n, AB_LONGEST_N)
        self.assertEqual(ab_profile.longest[0].tokens, AB_LONGEST_NGRAM)
        ab_motif = find_ngram_hits(ab, MOTIF_AB_9GRAM)
        self.assertEqual(len(ab_motif), STANDING_AB_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AB_LINE_NAMES[line_index], start, start + len(MOTIF_AB_9GRAM))
                for line_index, start in ab_motif
            ),
            STANDING_AB_MOTIF_SPANS,
        )

        br_profile = score_br_repeating_ngrams(br, self.analyzer)
        self.assertEqual(sum(len(line) for line in br), BR_STEM_TOTAL)
        self.assertEqual(br_profile.longest_n, BR_LONGEST_N)
        self.assertEqual(br_profile.longest[0].tokens, BR_LONGEST_NGRAM)
        self.assertIsNone(br_profile.top_8gram)

        bv_profile = score_bv_repeating_ngrams(bv, self.analyzer)
        self.assertEqual(sum(len(line) for line in bv), BV_STEM_TOTAL)
        self.assertEqual(bv_profile.longest_n, BV_LONGEST_N)
        self.assertEqual(bv_profile.longest[0].tokens, BV_8GRAM)
        self.assertEqual(len(find_ngram_hits(bv, BV_8GRAM)), 2)

        guy_cal = find_ngram_hits(calendar, DELIMITER_MOTIF)
        guy_rem = find_ngram_hits(remainder, DELIMITER_MOTIF)
        guy_cb = find_ngram_hits(cb_lines, DELIMITER_MOTIF)
        self.assertTrue(guy_cal)
        self.assertEqual(guy_rem, [])
        self.assertEqual(guy_cb, [])

        motif_cal = find_ngram_hits(calendar, MOTIF_9GRAM)
        motif_rem = find_ngram_hits(remainder, MOTIF_9GRAM)
        motif_cb = find_ngram_hits(cb_lines, MOTIF_9GRAM)
        self.assertEqual(motif_cal, [])
        self.assertEqual(len(motif_rem), 2)
        self.assertEqual(motif_cb, [])

        self.assertEqual(find_ngram_hits(calendar, SANDWICH), [])
        self.assertEqual(find_ngram_hits(remainder, SANDWICH), [])
        self.assertEqual(find_ngram_hits(cb_lines, SANDWICH), [])
        self.assertEqual(find_ngram_hits(aa, SANDWICH), [])
        self.assertEqual(len(find_ngram_hits(ab, SANDWICH)), 3)
        self.assertEqual(find_ngram_hits(br, SANDWICH), [])
        self.assertEqual(find_ngram_hits(bv, SANDWICH), [])

        cross = score_cb_5gram_ca_cross(
            CB_5GRAMS,
            calendar,
            CALENDAR_LINE_NAMES,
            remainder,
            REMAINDER_LINE_NAMES,
        )
        locked = tuple((row.tokens, row.calendar_hits, row.remainder_hits) for row in cross)
        self.assertEqual(locked, STANDING_CA_CROSS_TABLE)
        for gram in CB_5GRAMS:
            self.assertTrue(find_ngram_hits(cb_lines, gram))

        rem_profile = score_remainder_repeating_ngrams(remainder, self.analyzer)
        cb_profile = score_cb_repeating_ngrams(cb_lines, self.analyzer)
        self.assertEqual(rem_profile.longest_n, CA_REMAINDER_LONGEST_N)
        self.assertEqual(len(rem_profile.eightgrams), CA_REMAINDER_EIGHTGRAM_COUNT)
        self.assertGreaterEqual(CA_REMAINDER_EIGHTGRAM_COUNT, 1)
        self.assertEqual(cb_profile.longest_n, CB_LONGEST_N)
        self.assertEqual(len(cb_profile.eightgrams), CB_EIGHTGRAM_COUNT)
        self.assertEqual(CB_EIGHTGRAM_COUNT, 0)
        self.assertEqual(
            tuple(row.tokens for row in cb_profile.longest),
            tuple(tokens for tokens, _n, _freq, _spans in STANDING_LONGEST_NGRAMS),
        )
        self.assertEqual(self.as_stem.longest[0].tokens, IA_AS_STEM_LONGEST_NGRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-47 Ia 999 break lock."""
        lock = self.survey["santiago_ia_999_break"]
        self.assertEqual(lock["cycle"], 47)
        self.assertEqual(lock["passage"], "tablet_i_santiago_staff")
        self.assertEqual(lock["stem"], STEM_999)
        self.assertIsNone(lock["documented_cue"])
        self.assertEqual(lock["ia_html_999_leftovers"], [])
        self.assertEqual(lock["stem_count"], STANDING_999_STEM_COUNT)
        self.assertEqual(lock["prefix_of_cycle46_5gram"], STANDING_999_PREFIX_COUNT)
        self.assertEqual(
            [tuple(hit) for hit in lock["prefix_hits"]],
            list(STANDING_999_PREFIX_HITS),
        )
        self.assertEqual(lock["isolated_count"], STANDING_999_ISOLATED_COUNT)
        self.assertFalse(lock["only_as_prefix"])
        self.assertEqual(lock["line_edge_count"], STANDING_999_LINE_EDGE_COUNT)
        self.assertEqual(lock["adjacent_pairs"], STANDING_999_ADJACENT_PAIRS)
        self.assertEqual(lock["ia11_count"], STANDING_999_IA11_COUNT)
        self.assertEqual(
            [tuple(row) for row in lock["published_forms"]],
            list(STANDING_999_PUBLISHED_FORMS),
        )
        self.assertEqual(lock["as_stem_longest_n"], IA_AS_STEM_LONGEST_N)
        self.assertEqual(tuple(lock["as_stem_longest_tokens"]), IA_AS_STEM_LONGEST_NGRAM)
        self.assertEqual(lock["as_stem_longest_freq"], IA_AS_STEM_LONGEST_FREQ)
        self.assertEqual(lock["split_stem_total"], STANDING_SPLIT_STEM_TOTAL)
        self.assertEqual(lock["split_longest_n"], STANDING_SPLIT_LONGEST_N)
        self.assertEqual(lock["split_longest_count"], STANDING_SPLIT_LONGEST_COUNT)
        self.assertEqual(lock["split_longest_freq"], STANDING_SPLIT_LONGEST_FREQ)
        locked_split = tuple(
            (
                tuple(tokens),
                n,
                freq,
                tuple(tuple(span) for span in spans),
            )
            for tokens, n, freq, spans in lock["split_longest_ngrams"]
        )
        self.assertEqual(locked_split, STANDING_SPLIT_LONGEST_NGRAMS)
        self.assertEqual(lock["split_eightgram_count"], STANDING_SPLIT_EIGHTGRAM_COUNT)
        self.assertIsNone(lock["split_top_8gram"])
        self.assertFalse(lock["ib_html"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["aruku_bv_8gram_motif"]["cycle"], 45)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIa999ImageSnapshot(unittest.TestCase):
    """Cycle 47 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
