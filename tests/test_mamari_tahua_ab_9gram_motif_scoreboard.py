"""Tahua Ab 9-gram motif lock: hits, flanks, 8-prefix, 600-slot, cross-absent.

Cycle 39 text-search lock. Uses the already-vendored Kohaumotu Ab.html
fixture (cycle 38) plus the existing Aa, Ca calendar, Ca remainder,
and Cb fixtures. No invented Barthel. No other tablet. No
G00n→Barthel map. No type merge. No detector retune. No CV.

The cycle-38 longest Ab n-gram is locked as a motif: exact 9 tokens,
freq, spans, one published token on each side of every hit (or
line-edge), whether the cycle-38 top 8-gram is its prefix, and
whether 600 sits at the same slot in both hits. The 9-gram is
absent from Aa, the Ca calendar, Ca remainder, and Cb fixtures.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
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
from tests.test_mamari_remainder_9gram_motif_scoreboard import (
    LINE_EDGE,
    MOTIF_9GRAM,
    hit_tuple,
    score_motif_hits,
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
from tests.test_mamari_tahua_ab_scoreboard import (
    AB_LINE_NAMES,
    STANDING_LONGEST_FREQ,
    STANDING_LONGEST_N,
    STANDING_LONGEST_NGRAM,
    STANDING_LONGEST_SPANS,
    STANDING_STEM_TOTAL,
    STANDING_TOP_8GRAM,
    STANDING_TOP_8GRAM_FREQ,
    ab_line_stems,
    extract_ab_published_tokens,
    load_vendored_ab_html,
    score_ab_repeating_ngrams,
)

MOTIF_AB_9GRAM = STANDING_LONGEST_NGRAM
PREFIX_AB_8GRAM = STANDING_TOP_8GRAM
STEM_600 = "600"
STANDING_AB_MOTIF_FREQ = 2
STANDING_AB_MOTIF_SPANS = (("Ab3", 2, 11), ("Ab5", 13, 22))
# (line, start, end, before, after) — after/before is LINE_EDGE at a line end.
STANDING_AB_MOTIF_HITS = (
    ("Ab3", 2, 11, "003", "003"),
    ("Ab5", 13, 22, "208", "093"),
)
STANDING_AB_PREFIX8_HITS = (
    ("Ab3", 2, 10, "003", "050"),
    ("Ab5", 13, 21, "208", "050"),
)
STANDING_TOP_8GRAM_IS_PREFIX = True
STANDING_600_SLOT = 3
STANDING_600_SLOTS = (3,)
STANDING_600_FIXED_SLOT = True
STANDING_AA_MOTIF_HITS = ()
STANDING_CALENDAR_MOTIF_HITS = ()
STANDING_REMAINDER_MOTIF_HITS = ()
STANDING_CB_MOTIF_HITS = ()
STANDING_CROSS_ABSENT = True


def stem_slots(tokens, stem):
    """0-based indexes of stem inside tokens. Search only."""
    return tuple(index for index, token in enumerate(tokens) if token == stem)


class TestTahuaAb9gramMotifHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_flanks_medial_and_line_edge(self):
        """Medial hits keep neighbors; start/end of line is LINE_EDGE."""
        motif = MOTIF_AB_9GRAM
        prefix = PREFIX_AB_8GRAM
        lines = [list(motif), ["X"] + list(motif) + ["Y"]]
        names = ("L0", "L1")
        provider = MockProvider()
        motif_hits = score_motif_hits(lines, motif, names)
        prefix_hits = score_motif_hits(lines, prefix, names)
        self.assertEqual(
            tuple(hit_tuple(hit) for hit in motif_hits),
            (
                ("L0", 0, 9, LINE_EDGE, LINE_EDGE),
                ("L1", 1, 10, "X", "Y"),
            ),
        )
        self.assertEqual(
            tuple(hit_tuple(hit) for hit in prefix_hits),
            (
                ("L0", 0, 8, LINE_EDGE, "050"),
                ("L1", 1, 9, "X", "050"),
            ),
        )
        self.assertEqual(prefix, motif[:8])
        self.assertEqual(provider.get_call_history(), [])

    def test_600_slot_is_index_3_on_synthetic_repeats(self):
        """600 is the fourth token of the 9-gram on every synthetic copy."""
        motif = MOTIF_AB_9GRAM
        lines = [list(motif), ["X"] + list(motif) + ["Y"]]
        provider = MockProvider()
        self.assertEqual(stem_slots(motif, STEM_600), STANDING_600_SLOTS)
        self.assertEqual(motif[STANDING_600_SLOT], STEM_600)
        for sequence in lines:
            start = 0 if sequence[0] == motif[0] else 1
            window = sequence[start : start + len(motif)]
            self.assertEqual(tuple(window), motif)
            self.assertEqual(stem_slots(window, STEM_600), STANDING_600_SLOTS)
            self.assertEqual(window[STANDING_600_SLOT], STEM_600)
        self.assertTrue(STANDING_600_FIXED_SLOT)
        self.assertEqual(provider.get_call_history(), [])

    def test_empty_passage_is_absent(self):
        """A passage without the Ab 9-gram has no motif or 8-prefix hit."""
        lines = [["040", "010", "040", "030"], ["605", "003", "004"]]
        provider = MockProvider()
        self.assertEqual(score_motif_hits(lines, MOTIF_AB_9GRAM, ("C0", "C1")), ())
        self.assertEqual(score_motif_hits(lines, PREFIX_AB_8GRAM, ("C0", "C1")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariTahuaAb9gramMotifScoreboard(unittest.TestCase):
    """Cited Ab.html 9-gram motif lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.ab = ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html()))
        self.aa = aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html()))
        self.calendar = fixture_line_stems(load_mamari_fixture())
        self.remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        self.cb_lines = cb_line_stems(
            extract_cb_published_tokens(load_vendored_cb_html())
        )
        self.ab_motif = score_motif_hits(self.ab, MOTIF_AB_9GRAM, AB_LINE_NAMES)
        self.ab_prefix = score_motif_hits(self.ab, PREFIX_AB_8GRAM, AB_LINE_NAMES)
        self.profile = score_ab_repeating_ngrams(self.ab, self.analyzer)

    def test_checks_published_ab_fixture_only_for_hits(self):
        """Ab 926 stems are scored; no other tablet is scraped."""
        self.assertEqual(sum(len(line) for line in self.ab), STANDING_STEM_TOTAL)
        self.assertEqual(tuple(AB_LINE_NAMES), tuple(f"Ab{n}" for n in range(1, 9)))
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ab_motif_tokens_freq_spans_and_flanks(self):
        """9-gram is 605 003 004 600 004 003 040 003 050; freq 2 on Ab3/Ab5."""
        hits = tuple(hit_tuple(hit) for hit in self.ab_motif)
        spans = tuple((line, start, end) for line, start, end, _b, _a in hits)
        self.assertEqual(MOTIF_AB_9GRAM, STANDING_LONGEST_NGRAM)
        self.assertEqual(len(MOTIF_AB_9GRAM), STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest[0].tokens, MOTIF_AB_9GRAM)
        self.assertEqual(self.profile.longest[0].freq, STANDING_AB_MOTIF_FREQ)
        self.assertEqual(self.profile.longest[0].freq, STANDING_LONGEST_FREQ)
        self.assertEqual(self.profile.longest[0].spans, STANDING_AB_MOTIF_SPANS)
        self.assertEqual(self.profile.longest[0].spans, STANDING_LONGEST_SPANS)
        self.assertEqual(hits, STANDING_AB_MOTIF_HITS)
        self.assertEqual(spans, STANDING_AB_MOTIF_SPANS)
        self.assertEqual(len(hits), STANDING_AB_MOTIF_FREQ)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_top_8gram_is_the_9gram_prefix(self):
        """Cycle-38 top 8-gram is the 9-gram prefix; starts match."""
        hits = tuple(hit_tuple(hit) for hit in self.ab_prefix)
        self.assertEqual(PREFIX_AB_8GRAM, STANDING_TOP_8GRAM)
        self.assertEqual(PREFIX_AB_8GRAM, MOTIF_AB_9GRAM[:8])
        self.assertEqual(
            bool(PREFIX_AB_8GRAM == MOTIF_AB_9GRAM[:8]),
            STANDING_TOP_8GRAM_IS_PREFIX,
        )
        self.assertEqual(self.profile.top_8gram.tokens, PREFIX_AB_8GRAM)
        self.assertEqual(self.profile.top_8gram.freq, STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(hits, STANDING_AB_PREFIX8_HITS)
        motif_starts = [
            (line, start) for line, start, _end, _b, _a in STANDING_AB_MOTIF_HITS
        ]
        prefix_starts = [(line, start) for line, start, _end, _b, _a in hits]
        self.assertEqual(prefix_starts, motif_starts)
        after_tokens = [after for _line, _start, _end, _before, after in hits]
        self.assertEqual(after_tokens, [MOTIF_AB_9GRAM[8], MOTIF_AB_9GRAM[8]])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_600_sits_at_fixed_slot_in_both_hits(self):
        """600 is slot 3 (0-based) of both Ab 9-gram windows."""
        self.assertEqual(MOTIF_AB_9GRAM[STANDING_600_SLOT], STEM_600)
        self.assertEqual(stem_slots(MOTIF_AB_9GRAM, STEM_600), STANDING_600_SLOTS)
        hit_slots = []
        for hit in self.ab_motif:
            sequence = self.ab[AB_LINE_NAMES.index(hit.line)]
            window = sequence[hit.start : hit.end]
            self.assertEqual(tuple(window), MOTIF_AB_9GRAM)
            slots = stem_slots(window, STEM_600)
            self.assertEqual(slots, STANDING_600_SLOTS)
            self.assertEqual(window[STANDING_600_SLOT], STEM_600)
            hit_slots.append(slots)
        self.assertEqual(hit_slots, [STANDING_600_SLOTS, STANDING_600_SLOTS])
        self.assertEqual(hit_slots[0], hit_slots[1])
        self.assertTrue(STANDING_600_FIXED_SLOT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_9gram_absent_on_aa_ca_calendar_remainder_and_cb(self):
        """9-gram does not occur on Aa, Ca calendar, Ca remainder, or Cb."""
        aa = score_motif_hits(self.aa, MOTIF_AB_9GRAM, AA_LINE_NAMES)
        cal = score_motif_hits(self.calendar, MOTIF_AB_9GRAM, CALENDAR_LINE_NAMES)
        rem = score_motif_hits(self.remainder, MOTIF_AB_9GRAM, REMAINDER_LINE_NAMES)
        cb = score_motif_hits(self.cb_lines, MOTIF_AB_9GRAM, CB_LINE_NAMES)
        self.assertEqual(tuple(hit_tuple(hit) for hit in aa), STANDING_AA_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in cal), STANDING_CALENDAR_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in rem), STANDING_REMAINDER_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in cb), STANDING_CB_MOTIF_HITS)
        absent = not aa and not cal and not rem and not cb
        self.assertEqual(absent, STANDING_CROSS_ABSENT)
        self.assertEqual(find_ngram_hits(self.aa, MOTIF_AB_9GRAM), [])
        self.assertEqual(find_ngram_hits(self.calendar, MOTIF_AB_9GRAM), [])
        self.assertEqual(find_ngram_hits(self.remainder, MOTIF_AB_9GRAM), [])
        self.assertEqual(find_ngram_hits(self.cb_lines, MOTIF_AB_9GRAM), [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_aa_and_c_scoreboards_still_compute(self):
        """Aa 10-gram / Guy / Ca 9-gram / Cb 5-grams / longest-n stay."""
        aa_profile = score_aa_repeating_ngrams(self.aa, self.analyzer)
        self.assertEqual(sum(len(line) for line in self.aa), AA_STEM_TOTAL)
        self.assertEqual(aa_profile.longest_n, AA_LONGEST_N)
        self.assertEqual(aa_profile.longest[0].tokens, AA_LONGEST_NGRAM)
        self.assertEqual(aa_profile.top_8gram.tokens, AA_TOP_8GRAM)
        aa_motif = find_ngram_hits(self.aa, MOTIF_10GRAM)
        self.assertEqual(len(aa_motif), STANDING_AA_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AA_LINE_NAMES[line_index], start, start + len(MOTIF_10GRAM))
                for line_index, start in aa_motif
            ),
            STANDING_AA_MOTIF_SPANS,
        )

        guy_cal = find_ngram_hits(self.calendar, DELIMITER_MOTIF)
        guy_rem = find_ngram_hits(self.remainder, DELIMITER_MOTIF)
        guy_cb = find_ngram_hits(self.cb_lines, DELIMITER_MOTIF)
        self.assertTrue(guy_cal)
        self.assertEqual(guy_rem, [])
        self.assertEqual(guy_cb, [])

        motif_cal = find_ngram_hits(self.calendar, MOTIF_9GRAM)
        motif_rem = find_ngram_hits(self.remainder, MOTIF_9GRAM)
        motif_cb = find_ngram_hits(self.cb_lines, MOTIF_9GRAM)
        self.assertEqual(motif_cal, [])
        self.assertEqual(len(motif_rem), 2)
        self.assertEqual(motif_cb, [])

        cross = score_cb_5gram_ca_cross(
            CB_5GRAMS,
            self.calendar,
            CALENDAR_LINE_NAMES,
            self.remainder,
            REMAINDER_LINE_NAMES,
        )
        locked = tuple((row.tokens, row.calendar_hits, row.remainder_hits) for row in cross)
        self.assertEqual(locked, STANDING_CA_CROSS_TABLE)
        for gram in CB_5GRAMS:
            self.assertTrue(find_ngram_hits(self.cb_lines, gram))

        rem_profile = score_remainder_repeating_ngrams(self.remainder, self.analyzer)
        cb_profile = score_cb_repeating_ngrams(self.cb_lines, self.analyzer)
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
        self.assertEqual(tuple(CB_LINE_NAMES), tuple(f"Cb{n}" for n in range(1, 15)))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-39 Tahua Ab 9-gram motif lock."""
        lock = self.survey["tahua_ab_9gram_motif"]
        self.assertEqual(lock["cycle"], 39)
        self.assertEqual(lock["passage"], "tablet_a_tahua_side_b")
        self.assertEqual(lock["motif_tokens"], list(MOTIF_AB_9GRAM))
        self.assertEqual(lock["motif_n"], STANDING_LONGEST_N)
        self.assertEqual(lock["motif_freq"], STANDING_AB_MOTIF_FREQ)
        self.assertEqual(
            [tuple(span) for span in lock["motif_spans"]],
            list(STANDING_AB_MOTIF_SPANS),
        )
        self.assertEqual(
            [tuple(hit) for hit in lock["ab_motif_hits"]],
            list(STANDING_AB_MOTIF_HITS),
        )
        self.assertEqual(lock["prefix8_tokens"], list(PREFIX_AB_8GRAM))
        self.assertEqual(lock["top_8gram_is_prefix"], STANDING_TOP_8GRAM_IS_PREFIX)
        self.assertEqual(
            [tuple(hit) for hit in lock["ab_prefix8_hits"]],
            list(STANDING_AB_PREFIX8_HITS),
        )
        self.assertEqual(lock["stem_600"], STEM_600)
        self.assertEqual(lock["stem_600_slot"], STANDING_600_SLOT)
        self.assertEqual(lock["stem_600_slots"], list(STANDING_600_SLOTS))
        self.assertTrue(lock["stem_600_fixed_slot"])
        self.assertEqual(lock["aa_motif_hits"], [])
        self.assertEqual(lock["calendar_motif_hits"], [])
        self.assertEqual(lock["remainder_motif_hits"], [])
        self.assertEqual(lock["cb_motif_hits"], [])
        self.assertTrue(lock["aa_absent"])
        self.assertTrue(lock["c_absent"])
        self.assertTrue(lock["cross_absent"])
        ab_lock = self.survey["tablet_a_tahua_side_b"]
        self.assertEqual(ab_lock["cycle"], 38)
        self.assertEqual(tuple(ab_lock["longest_tokens"]), MOTIF_AB_9GRAM)
        self.assertEqual(tuple(ab_lock["top_8gram"]), PREFIX_AB_8GRAM)
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["cycle"], 37)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariTahuaAb9gramMotifImageSnapshot(unittest.TestCase):
    """Cycle 39 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
