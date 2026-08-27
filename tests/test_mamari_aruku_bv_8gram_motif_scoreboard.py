"""Aruku Bv 8-gram motif lock: hits, flanks, cross-absent.

Cycle 45 text-search lock. Uses the already-vendored Kohaumotu Bv.html
fixture (cycle 44) plus the existing Br, Aa, Ab, Ca calendar, Ca
remainder, and Cb fixtures. No invented Barthel. No other tablet.
No G00n→Barthel map. No type merge. No detector retune. No CV.

The cycle-44 longest Bv n-gram is locked as a motif: exact 8 tokens,
freq, spans, one published token on each side of every hit (or
line-edge). The 8-gram is absent from Br, Aa, Ab, the Ca calendar,
Ca remainder, and Cb fixtures.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
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
    STANDING_LONGEST_FREQ,
    STANDING_LONGEST_N,
    STANDING_LONGEST_NGRAM,
    STANDING_LONGEST_SPANS,
    STANDING_STEM_TOTAL,
    STANDING_TOP_8GRAM,
    STANDING_TOP_8GRAM_FREQ,
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

MOTIF_BV_8GRAM = STANDING_LONGEST_NGRAM
STANDING_BV_MOTIF_FREQ = 2
STANDING_BV_MOTIF_SPANS = (("Bv5", 18, 26), ("Bv6", 39, 47))
# (line, start, end, before, after) — after/before is LINE_EDGE at a line end.
STANDING_BV_MOTIF_HITS = (
    ("Bv5", 18, 26, "663", "236"),
    ("Bv6", 39, 47, "673", "092"),
)
STANDING_BR_MOTIF_HITS = ()
STANDING_AA_MOTIF_HITS = ()
STANDING_AB_MOTIF_HITS = ()
STANDING_CALENDAR_MOTIF_HITS = ()
STANDING_REMAINDER_MOTIF_HITS = ()
STANDING_CB_MOTIF_HITS = ()
STANDING_CROSS_ABSENT = True


class TestArukuBv8gramMotifHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_flanks_medial_and_line_edge(self):
        """Medial hits keep neighbors; start/end of line is LINE_EDGE."""
        motif = MOTIF_BV_8GRAM
        lines = [list(motif), ["X"] + list(motif) + ["Y"]]
        names = ("L0", "L1")
        provider = MockProvider()
        motif_hits = score_motif_hits(lines, motif, names)
        self.assertEqual(
            tuple(hit_tuple(hit) for hit in motif_hits),
            (
                ("L0", 0, 8, LINE_EDGE, LINE_EDGE),
                ("L1", 1, 9, "X", "Y"),
            ),
        )
        self.assertEqual(len(motif), 8)
        self.assertEqual(provider.get_call_history(), [])

    def test_empty_passage_is_absent(self):
        """A passage without the Bv 8-gram has no motif hit."""
        lines = [["040", "010", "040", "030"], ["002", "065", "042", "300"]]
        provider = MockProvider()
        self.assertEqual(score_motif_hits(lines, MOTIF_BV_8GRAM, ("C0", "C1")), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariArukuBv8gramMotifScoreboard(unittest.TestCase):
    """Cited Bv.html 8-gram motif lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.bv = bv_line_stems(extract_bv_published_tokens(load_vendored_bv_html()))
        self.br = br_line_stems(extract_br_published_tokens(load_vendored_br_html()))
        self.aa = aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html()))
        self.ab = ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html()))
        self.calendar = fixture_line_stems(load_mamari_fixture())
        self.remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        self.cb_lines = cb_line_stems(
            extract_cb_published_tokens(load_vendored_cb_html())
        )
        self.bv_motif = score_motif_hits(self.bv, MOTIF_BV_8GRAM, BV_LINE_NAMES)
        self.profile = score_bv_repeating_ngrams(self.bv, self.analyzer)

    def test_checks_published_bv_fixture_only_for_hits(self):
        """Bv 738 stems are scored; no other tablet is scraped."""
        self.assertEqual(sum(len(line) for line in self.bv), STANDING_STEM_TOTAL)
        self.assertEqual(tuple(BV_LINE_NAMES), tuple(f"Bv{n}" for n in range(1, 13)))
        self.assertEqual(self.profile.longest_n, STANDING_LONGEST_N)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_bv_motif_tokens_freq_spans_and_flanks(self):
        """8-gram is 002 065 042 300 385 003 065 200; freq 2 on Bv5/Bv6."""
        hits = tuple(hit_tuple(hit) for hit in self.bv_motif)
        spans = tuple((line, start, end) for line, start, end, _b, _a in hits)
        self.assertEqual(MOTIF_BV_8GRAM, STANDING_LONGEST_NGRAM)
        self.assertEqual(MOTIF_BV_8GRAM, STANDING_TOP_8GRAM)
        self.assertEqual(len(MOTIF_BV_8GRAM), STANDING_LONGEST_N)
        self.assertEqual(self.profile.longest[0].tokens, MOTIF_BV_8GRAM)
        self.assertEqual(self.profile.longest[0].freq, STANDING_BV_MOTIF_FREQ)
        self.assertEqual(self.profile.longest[0].freq, STANDING_LONGEST_FREQ)
        self.assertEqual(self.profile.longest[0].spans, STANDING_BV_MOTIF_SPANS)
        self.assertEqual(self.profile.longest[0].spans, STANDING_LONGEST_SPANS)
        self.assertEqual(self.profile.top_8gram.tokens, MOTIF_BV_8GRAM)
        self.assertEqual(self.profile.top_8gram.freq, STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(hits, STANDING_BV_MOTIF_HITS)
        self.assertEqual(spans, STANDING_BV_MOTIF_SPANS)
        self.assertEqual(len(hits), STANDING_BV_MOTIF_FREQ)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_8gram_absent_on_br_aa_ab_ca_calendar_remainder_and_cb(self):
        """8-gram does not occur on Br, Aa, Ab, Ca calendar, remainder, or Cb."""
        br = score_motif_hits(self.br, MOTIF_BV_8GRAM, BR_LINE_NAMES)
        aa = score_motif_hits(self.aa, MOTIF_BV_8GRAM, AA_LINE_NAMES)
        ab = score_motif_hits(self.ab, MOTIF_BV_8GRAM, AB_LINE_NAMES)
        cal = score_motif_hits(self.calendar, MOTIF_BV_8GRAM, CALENDAR_LINE_NAMES)
        rem = score_motif_hits(self.remainder, MOTIF_BV_8GRAM, REMAINDER_LINE_NAMES)
        cb = score_motif_hits(self.cb_lines, MOTIF_BV_8GRAM, CB_LINE_NAMES)
        self.assertEqual(tuple(hit_tuple(hit) for hit in br), STANDING_BR_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in aa), STANDING_AA_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in ab), STANDING_AB_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in cal), STANDING_CALENDAR_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in rem), STANDING_REMAINDER_MOTIF_HITS)
        self.assertEqual(tuple(hit_tuple(hit) for hit in cb), STANDING_CB_MOTIF_HITS)
        absent = not br and not aa and not ab and not cal and not rem and not cb
        self.assertEqual(absent, STANDING_CROSS_ABSENT)
        self.assertEqual(find_ngram_hits(self.br, MOTIF_BV_8GRAM), [])
        self.assertEqual(find_ngram_hits(self.aa, MOTIF_BV_8GRAM), [])
        self.assertEqual(find_ngram_hits(self.ab, MOTIF_BV_8GRAM), [])
        self.assertEqual(find_ngram_hits(self.calendar, MOTIF_BV_8GRAM), [])
        self.assertEqual(find_ngram_hits(self.remainder, MOTIF_BV_8GRAM), [])
        self.assertEqual(find_ngram_hits(self.cb_lines, MOTIF_BV_8GRAM), [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_a_br_and_c_scoreboards_still_compute(self):
        """Aa / Ab / Br / Guy / Ca 9-gram / Cb 5-grams / longest-n stay."""
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

        ab_profile = score_ab_repeating_ngrams(self.ab, self.analyzer)
        self.assertEqual(sum(len(line) for line in self.ab), AB_STEM_TOTAL)
        self.assertEqual(ab_profile.longest_n, AB_LONGEST_N)
        self.assertEqual(ab_profile.longest[0].tokens, AB_LONGEST_NGRAM)
        ab_motif = find_ngram_hits(self.ab, MOTIF_AB_9GRAM)
        self.assertEqual(len(ab_motif), STANDING_AB_MOTIF_FREQ)
        self.assertEqual(
            tuple(
                (AB_LINE_NAMES[line_index], start, start + len(MOTIF_AB_9GRAM))
                for line_index, start in ab_motif
            ),
            STANDING_AB_MOTIF_SPANS,
        )

        br_profile = score_br_repeating_ngrams(self.br, self.analyzer)
        self.assertEqual(sum(len(line) for line in self.br), BR_STEM_TOTAL)
        self.assertEqual(br_profile.longest_n, BR_LONGEST_N)
        self.assertEqual(br_profile.longest[0].tokens, BR_LONGEST_NGRAM)
        self.assertIsNone(br_profile.top_8gram)

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
        self.assertEqual(tuple(AA_LINE_NAMES), tuple(f"Aa{n}" for n in range(1, 9)))
        self.assertEqual(tuple(AB_LINE_NAMES), tuple(f"Ab{n}" for n in range(1, 9)))
        self.assertEqual(tuple(BR_LINE_NAMES), tuple(f"Br{n}" for n in range(1, 11)))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-45 Aruku Bv 8-gram motif lock."""
        lock = self.survey["aruku_bv_8gram_motif"]
        self.assertEqual(lock["cycle"], 45)
        self.assertEqual(lock["passage"], "tablet_b_aruku_kurenga_verso")
        self.assertEqual(lock["motif_tokens"], list(MOTIF_BV_8GRAM))
        self.assertEqual(lock["motif_n"], STANDING_LONGEST_N)
        self.assertEqual(lock["motif_freq"], STANDING_BV_MOTIF_FREQ)
        self.assertEqual(
            [tuple(span) for span in lock["motif_spans"]],
            list(STANDING_BV_MOTIF_SPANS),
        )
        self.assertEqual(
            [tuple(hit) for hit in lock["bv_motif_hits"]],
            list(STANDING_BV_MOTIF_HITS),
        )
        self.assertEqual(lock["br_motif_hits"], [])
        self.assertEqual(lock["aa_motif_hits"], [])
        self.assertEqual(lock["ab_motif_hits"], [])
        self.assertEqual(lock["calendar_motif_hits"], [])
        self.assertEqual(lock["remainder_motif_hits"], [])
        self.assertEqual(lock["cb_motif_hits"], [])
        self.assertTrue(lock["br_absent"])
        self.assertTrue(lock["aa_absent"])
        self.assertTrue(lock["ab_absent"])
        self.assertTrue(lock["c_absent"])
        self.assertTrue(lock["cross_absent"])
        bv_lock = self.survey["tablet_b_aruku_kurenga_verso"]
        self.assertEqual(bv_lock["cycle"], 44)
        self.assertEqual(tuple(bv_lock["longest_tokens"]), MOTIF_BV_8GRAM)
        self.assertEqual(tuple(bv_lock["top_8gram"]), MOTIF_BV_8GRAM)
        self.assertEqual(self.survey["tablet_b_aruku_kurenga_recto"]["cycle"], 43)
        self.assertEqual(self.survey["tahua_ab_9gram_motif"]["cycle"], 39)
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["cycle"], 37)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariArukuBv8gramMotifImageSnapshot(unittest.TestCase):
    """Cycle 45 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
