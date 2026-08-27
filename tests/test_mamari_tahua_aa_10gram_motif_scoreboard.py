"""Tahua Aa 10-gram motif lock: hits, flanks, 8-prefix, C-absent.

Cycle 37 text-search lock. Uses the already-vendored Kohaumotu Aa.html
fixture (cycle 36) plus the existing Ca calendar, Ca remainder, and Cb
fixtures. No invented Barthel. No Ab.html scrape. No other tablet.
No G00n→Barthel map. No type merge. No detector retune. No CV.

The cycle-36 longest Aa n-gram is locked as a motif: exact 10 tokens,
freq, spans, one published token on each side of every hit (or
line-edge), and whether the cycle-36 top 8-gram is its prefix. The
10-gram is absent from the Ca calendar, Ca remainder, and Cb fixtures.
Cycle 39 locks the already-vendored Ab 9-gram as a motif.
Cycle 40 locks a 600 inventory on the existing fixtures.

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
from tests.test_mamari_tahua_aa_scoreboard import (
    AA_LINE_NAMES,
    STANDING_LONGEST_N,
    STANDING_LONGEST_NGRAM,
    STANDING_STEM_TOTAL,
    STANDING_TOP_8GRAM,
    STANDING_TOP_8GRAM_FREQ,
    aa_line_stems,
    extract_aa_published_tokens,
    load_vendored_aa_html,
    score_aa_repeating_ngrams,
)

MOTIF_10GRAM = STANDING_LONGEST_NGRAM
PREFIX_8GRAM = STANDING_TOP_8GRAM
STANDING_AA_MOTIF_FREQ = 2
STANDING_AA_MOTIF_SPANS = (("Aa7", 55, 65), ("Aa7", 88, 98))
# (line, start, end, before, after) — after/before is LINE_EDGE at a line end.
STANDING_AA_MOTIF_HITS = (
    ("Aa7", 55, 65, "002", "009"),
    ("Aa7", 88, 98, "020", "256"),
)
STANDING_AA_PREFIX8_HITS = (
    ("Aa7", 55, 63, "002", "009"),
    ("Aa7", 88, 96, "020", "009"),
)
STANDING_TOP_8GRAM_IS_PREFIX = True
STANDING_CALENDAR_MOTIF_HITS = ()
STANDING_REMAINDER_MOTIF_HITS = ()
STANDING_CB_MOTIF_HITS = ()
STANDING_C_ABSENT = True


class TestTahuaAa10gramMotifHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_flanks_medial_and_line_edge(self):
        """Medial hits keep neighbors; start/end of line is LINE_EDGE."""
        motif = MOTIF_10GRAM
        prefix = PREFIX_8GRAM
        lines = [list(motif), ["X"] + list(motif) + ["Y"]]
        names = ("L0", "L1")
        provider = MockProvider()
        motif_hits = score_motif_hits(lines, motif, names)
        prefix_hits = score_motif_hits(lines, prefix, names)
        self.assertEqual(
            tuple(hit_tuple(hit) for hit in motif_hits),
            (
                ("L0", 0, 10, LINE_EDGE, LINE_EDGE),
                ("L1", 1, 11, "X", "Y"),
            ),
        )
        self.assertEqual(
            tuple(hit_tuple(hit) for hit in prefix_hits),
            (
                ("L0", 0, 8, LINE_EDGE, "009"),
                ("L1", 1, 9, "X", "009"),
            ),
        )
        self.assertEqual(prefix, motif[:8])
        self.assertEqual(provider.get_call_history(), [])

    def test_empty_passage_is_absent(self):
        """A passage without the 10-gram has no motif or 8-prefix hit."""
        lines = [["040", "010", "040", "030"], ["080", "004", "280"]]
        provider = MockProvider()
        self.assertEqual(score_motif_hits(lines, MOTIF_10GRAM, ("C0", "C1")), ())
        self.assertEqual(score_motif_hits(lines, PREFIX_8GRAM, ("C0", "C1")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariTahuaAa10gramMotifScoreboard(unittest.TestCase):
    """Cited Aa.html 10-gram motif lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.aa = aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html()))
        self.calendar = fixture_line_stems(load_mamari_fixture())
        self.remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        self.cb_lines = cb_line_stems(
            extract_cb_published_tokens(load_vendored_cb_html())
        )
        self.aa_motif = score_motif_hits(self.aa, MOTIF_10GRAM, AA_LINE_NAMES)
        self.aa_prefix = score_motif_hits(self.aa, PREFIX_8GRAM, AA_LINE_NAMES)
        self.profile = score_aa_repeating_ngrams(self.aa, self.analyzer)

    def test_checks_published_aa_fixture_only_for_hits(self):
        """Aa 906 stems are scored; Ab.html is not scraped."""
        self.assertEqual(sum(len(line) for line in self.aa), STANDING_STEM_TOTAL)
        self.assertEqual(tuple(AA_LINE_NAMES), tuple(f"Aa{n}" for n in range(1, 9)))
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_aa_motif_tokens_freq_spans_and_flanks(self):
        """10-gram is 080 004 280 182 048 022 025 025 009 005; freq 2 on Aa7."""
        hits = tuple(hit_tuple(hit) for hit in self.aa_motif)
        spans = tuple((line, start, end) for line, start, end, _b, _a in hits)
        self.assertEqual(MOTIF_10GRAM, STANDING_LONGEST_NGRAM)
        self.assertEqual(len(MOTIF_10GRAM), STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest[0].tokens, MOTIF_10GRAM)
        self.assertEqual(self.profile.longest[0].freq, STANDING_AA_MOTIF_FREQ)
        self.assertEqual(self.profile.longest[0].spans, STANDING_AA_MOTIF_SPANS)
        self.assertEqual(hits, STANDING_AA_MOTIF_HITS)
        self.assertEqual(spans, STANDING_AA_MOTIF_SPANS)
        self.assertEqual(len(hits), STANDING_AA_MOTIF_FREQ)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_top_8gram_is_the_10gram_prefix(self):
        """Cycle-36 top 8-gram is the 10-gram prefix; starts match."""
        hits = tuple(hit_tuple(hit) for hit in self.aa_prefix)
        self.assertEqual(PREFIX_8GRAM, STANDING_TOP_8GRAM)
        self.assertEqual(PREFIX_8GRAM, MOTIF_10GRAM[:8])
        self.assertEqual(bool(PREFIX_8GRAM == MOTIF_10GRAM[:8]), STANDING_TOP_8GRAM_IS_PREFIX)
        self.assertEqual(self.profile.top_8gram.tokens, PREFIX_8GRAM)
        self.assertEqual(self.profile.top_8gram.freq, STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(hits, STANDING_AA_PREFIX8_HITS)
        motif_starts = [
            (line, start) for line, start, _end, _b, _a in STANDING_AA_MOTIF_HITS
        ]
        prefix_starts = [(line, start) for line, start, _end, _b, _a in hits]
        self.assertEqual(prefix_starts, motif_starts)
        after_tokens = [after for _line, _start, _end, _before, after in hits]
        self.assertEqual(after_tokens, [MOTIF_10GRAM[8], MOTIF_10GRAM[8]])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_10gram_absent_on_ca_calendar_remainder_and_cb(self):
        """10-gram does not occur on Ca calendar, Ca remainder, or Cb."""
        cal = score_motif_hits(self.calendar, MOTIF_10GRAM, CALENDAR_LINE_NAMES)
        rem = score_motif_hits(self.remainder, MOTIF_10GRAM, REMAINDER_LINE_NAMES)
        cb = score_motif_hits(self.cb_lines, MOTIF_10GRAM, CB_LINE_NAMES)
        self.assertEqual(tuple(hit_tuple(hit) for hit in cal), STANDING_CALENDAR_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in rem), STANDING_REMAINDER_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in cb), STANDING_CB_MOTIF_HITS)
        absent = not cal and not rem and not cb
        self.assertEqual(absent, STANDING_C_ABSENT)
        self.assertEqual(find_ngram_hits(self.calendar, MOTIF_10GRAM), [])
        self.assertEqual(find_ngram_hits(self.remainder, MOTIF_10GRAM), [])
        self.assertEqual(find_ngram_hits(self.cb_lines, MOTIF_10GRAM), [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_c_scoreboards_still_compute(self):
        """Guy / Ca 9-gram / three Cb 5-grams / longest-n locks on C only."""
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
        """CORPUS_SURVEY.json records the cycle-37 Tahua Aa 10-gram motif lock."""
        lock = self.survey["tahua_aa_10gram_motif"]
        self.assertEqual(lock["cycle"], 37)
        self.assertEqual(lock["passage"], "tablet_a_tahua_side_a")
        self.assertEqual(lock["motif_tokens"], list(MOTIF_10GRAM))
        self.assertEqual(lock["motif_n"], STANDING_LONGEST_N)
        self.assertEqual(lock["motif_freq"], STANDING_AA_MOTIF_FREQ)
        self.assertEqual(
            [tuple(span) for span in lock["motif_spans"]],
            list(STANDING_AA_MOTIF_SPANS),
        )
        self.assertEqual(
            [tuple(hit) for hit in lock["aa_motif_hits"]],
            list(STANDING_AA_MOTIF_HITS),
        )
        self.assertEqual(lock["prefix8_tokens"], list(PREFIX_8GRAM))
        self.assertEqual(lock["top_8gram_is_prefix"], STANDING_TOP_8GRAM_IS_PREFIX)
        self.assertEqual(
            [tuple(hit) for hit in lock["aa_prefix8_hits"]],
            list(STANDING_AA_PREFIX8_HITS),
        )
        self.assertEqual(lock["calendar_motif_hits"], [])
        self.assertEqual(lock["remainder_motif_hits"], [])
        self.assertEqual(lock["cb_motif_hits"], [])
        self.assertTrue(lock["c_absent"])
        aa_lock = self.survey["tablet_a_tahua_side_a"]
        self.assertEqual(aa_lock["cycle"], 36)
        self.assertEqual(tuple(aa_lock["longest_tokens"]), MOTIF_10GRAM)
        self.assertEqual(tuple(aa_lock["top_8gram"]), PREFIX_8GRAM)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariTahuaAa10gramMotifImageSnapshot(unittest.TestCase):
    """Cycle 37 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
