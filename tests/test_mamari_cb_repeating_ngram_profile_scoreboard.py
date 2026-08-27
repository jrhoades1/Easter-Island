"""Cb repeating n-gram profile: n≥4, freq≥2, already-vendored Cb.html.

Cycle 33 text-search lock. Uses the cycle-32 Kohaumotu Cb.html fixture
only. Does not scrape a new tablet. Does not re-mine Ca calendar or
remainder. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV.

Per-line extract_ngrams, same analyzer as the remainder profile.
For each distinct n-gram: tokens, n, freq, line spans. Guy's 8-stem
delimiter and the Ca remainder 9-gram are still absent. Longest n
with freq ≥2 is 5 (three n-grams, all freq 2). No repeating 8-gram. Cycle 34 locks those three n=5 grams on
the existing Ca calendar and remainder fixtures only.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import DELIMITER_MOTIF
from tests.test_mamari_cb_side_b_scoreboard import (
    CB_HTML_PATH,
    CB_LINE_NAMES,
    STANDING_STEM_COUNTS,
    STANDING_STEM_TOTAL,
    cb_line_stems,
    extract_cb_published_tokens,
    load_vendored_cb_html,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import MOTIF_9GRAM
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    PROFILE_MIN_FREQ,
    PROFILE_MIN_N,
    profile_tuple,
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_second_passage_scoreboard import (
    find_ngram_hits,
    load_corpus_survey,
)

STANDING_REPEATING_NGRAM_COUNT = 12
STANDING_COUNTS_BY_N = {4: 9, 5: 3}
STANDING_LONGEST_N = 5
STANDING_LONGEST_FREQ = 2
STANDING_LONGEST_COUNT = 3
STANDING_EIGHTGRAM_COUNT = 0
STANDING_TOP_8GRAM = None
STANDING_LONGEST_IS_GUY_DELIMITER = False
STANDING_LONGEST_IS_CA_9GRAM = False
STANDING_TOP_8GRAM_IS_GUY_DELIMITER = False
STANDING_TOP_8GRAM_IS_CA_9GRAM = False

# (tokens, n, freq, spans) — three n=5 rows, all freq 2.
STANDING_LONGEST_NGRAMS = (
    (("660", "005", "064", "660", "005"), 5, 2, (
            ("Cb4", 18, 23),
            ("Cb4", 21, 26),
        )),
    (("381", "004", "066", "760", "004"), 5, 2, (
            ("Cb6", 9, 14),
            ("Cb6", 17, 22),
        )),
    (("099", "004", "002", "004", "002"), 5, 2, (
            ("Cb8", 15, 20),
            ("Cb11", 2, 7),
        )),
)

# Full n≥4 freq≥2 table. Small enough to lock every row.
STANDING_REPEATING_NGRAMS = (
    (("001", "003", "001", "003"), 4, 2, (
            ("Cb1", 6, 10),
            ("Cb1", 8, 12),
        )),
    (("605", "700", "605", "700"), 4, 2, (
            ("Cb4", 9, 13),
            ("Cb4", 11, 15),
        )),
    (("660", "005", "064", "660"), 4, 2, (
            ("Cb4", 18, 22),
            ("Cb4", 21, 25),
        )),
    (("005", "064", "660", "005"), 4, 2, (
            ("Cb4", 19, 23),
            ("Cb4", 22, 26),
        )),
    (("381", "004", "066", "760"), 4, 2, (
            ("Cb6", 9, 13),
            ("Cb6", 17, 21),
        )),
    (("004", "066", "760", "004"), 4, 2, (
            ("Cb6", 10, 14),
            ("Cb6", 18, 22),
        )),
    (("099", "004", "002", "004"), 4, 2, (
            ("Cb8", 15, 19),
            ("Cb11", 2, 6),
        )),
    (("004", "002", "004", "002"), 4, 2, (
            ("Cb8", 16, 20),
            ("Cb11", 3, 7),
        )),
    (("002", "060", "002", "060"), 4, 2, (
            ("Cb9", 15, 19),
            ("Cb9", 17, 21),
        )),
) + STANDING_LONGEST_NGRAMS


def score_cb_repeating_ngrams(lines, analyzer):
    """n≥4 freq≥2 profile on the vendored Cb fixture. Search only."""
    return score_remainder_repeating_ngrams(
        lines, analyzer, line_names=CB_LINE_NAMES
    )


class TestCbRepeatingNgramProfileHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_reuses_remainder_scorer_with_cb_line_names(self):
        """Spans carry Cb line names; no 8-gram when n<8."""
        gram = ("A", "B", "C", "D")
        lines = [list(gram) + ["X"], ["Y"] + list(gram)]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        profile = score_cb_repeating_ngrams(lines, analyzer)
        self.assertEqual(profile.longest_n, 4)
        self.assertEqual(len(profile.rows), 1)
        self.assertEqual(profile.rows[0].spans, (("Cb1", 0, 4), ("Cb2", 1, 5)))
        self.assertIsNone(profile.top_8gram)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariCbRepeatingNgramProfileScoreboard(unittest.TestCase):
    """Cited Cb.html n≥4 freq≥2 lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.published = extract_cb_published_tokens(load_vendored_cb_html())
        self.lines = cb_line_stems(self.published)
        self.profile = score_cb_repeating_ngrams(self.lines, self.analyzer)

    def test_fixture_is_vendored_cb_not_a_new_tablet(self):
        """Cycle-32 Cb.html only. No new scrape. Ca passages are not re-mined."""
        self.assertTrue(CB_HTML_PATH.is_file())
        self.assertEqual(tuple(CB_LINE_NAMES), tuple(f"Cb{n}" for n in range(1, 15)))
        self.assertEqual(
            [len(line) for line in self.lines],
            list(STANDING_STEM_COUNTS),
        )
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_STEM_TOTAL)
        self.assertEqual(self.survey["tablet_c_side_b"]["cycle"], 32)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_profile_table_is_standing_truth(self):
        """Lock every Cb n≥4 freq≥2 n-gram: tokens, n, freq, spans."""
        p = self.profile
        locked = tuple(profile_tuple(row) for row in p.rows)
        self.assertEqual(len(locked), STANDING_REPEATING_NGRAM_COUNT)
        self.assertEqual(locked, STANDING_REPEATING_NGRAMS)
        counts: dict[int, int] = {}
        for row in p.rows:
            self.assertGreaterEqual(row.n, PROFILE_MIN_N)
            self.assertGreaterEqual(row.freq, PROFILE_MIN_FREQ)
            self.assertEqual(row.n, len(row.tokens))
            self.assertEqual(row.freq, len(row.spans))
            counts[row.n] = counts.get(row.n, 0) + 1
        self.assertEqual(counts, STANDING_COUNTS_BY_N)
        self.assertNotIn(DELIMITER_MOTIF, [row.tokens for row in p.rows])
        self.assertNotIn(MOTIF_9GRAM, [row.tokens for row in p.rows])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_n_is_5(self):
        """Longest repeating n is 5; three n-grams, each freq 2."""
        p = self.profile
        self.assertEqual(p.longest_n, STANDING_LONGEST_N)
        self.assertEqual(len(p.longest), STANDING_LONGEST_COUNT)
        locked = tuple(profile_tuple(row) for row in p.longest)
        self.assertEqual(locked, STANDING_LONGEST_NGRAMS)
        self.assertTrue(all(row.freq == STANDING_LONGEST_FREQ for row in p.longest))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_top_8gram_is_none(self):
        """No repeating 8-gram on Cb."""
        p = self.profile
        self.assertEqual(p.eightgrams, ())
        self.assertIsNone(p.top_8gram)
        self.assertEqual(p.top_8gram, STANDING_TOP_8GRAM)
        self.assertEqual(len(p.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_and_top_8_are_not_guy_or_ca_9gram(self):
        """Longest n=5 and absent top-8 are not Guy's delimiter or the Ca 9-gram."""
        p = self.profile
        longest_tokens = [row.tokens for row in p.longest]
        self.assertNotIn(DELIMITER_MOTIF, longest_tokens)
        self.assertNotIn(MOTIF_9GRAM, longest_tokens)
        self.assertEqual(
            any(tokens == DELIMITER_MOTIF for tokens in longest_tokens),
            STANDING_LONGEST_IS_GUY_DELIMITER,
        )
        self.assertEqual(
            any(tokens == MOTIF_9GRAM for tokens in longest_tokens),
            STANDING_LONGEST_IS_CA_9GRAM,
        )
        self.assertIsNone(p.top_8gram)
        self.assertEqual(
            p.top_8gram == DELIMITER_MOTIF,
            STANDING_TOP_8GRAM_IS_GUY_DELIMITER,
        )
        self.assertEqual(
            p.top_8gram == MOTIF_9GRAM,
            STANDING_TOP_8GRAM_IS_CA_9GRAM,
        )
        self.assertNotEqual(STANDING_LONGEST_N, len(DELIMITER_MOTIF))
        self.assertNotEqual(STANDING_LONGEST_N, len(MOTIF_9GRAM))
        self.assertEqual(find_ngram_hits(self.lines, DELIMITER_MOTIF), [])
        self.assertEqual(find_ngram_hits(self.lines, MOTIF_9GRAM), [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-33 Cb n-gram lock."""
        profile = self.survey["cb_repeating_ngram_profile"]
        self.assertEqual(profile["cycle"], 33)
        self.assertEqual(profile["passage"], "tablet_c_side_b")
        self.assertEqual(profile["min_n"], PROFILE_MIN_N)
        self.assertEqual(profile["min_freq"], PROFILE_MIN_FREQ)
        self.assertEqual(profile["distinct_count"], STANDING_REPEATING_NGRAM_COUNT)
        self.assertEqual(
            {int(k): v for k, v in profile["counts_by_n"].items()},
            STANDING_COUNTS_BY_N,
        )
        self.assertEqual(profile["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(profile["longest_count"], STANDING_LONGEST_COUNT)
        self.assertEqual(profile["longest_freq"], STANDING_LONGEST_FREQ)
        locked_longest = tuple(
            (
                tuple(tokens),
                n,
                freq,
                tuple(tuple(span) for span in spans),
            )
            for tokens, n, freq, spans in profile["longest"]
        )
        self.assertEqual(locked_longest, STANDING_LONGEST_NGRAMS)
        self.assertEqual(profile["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertIsNone(profile["top_8gram"])
        self.assertEqual(profile["top_8gram"], STANDING_TOP_8GRAM)
        self.assertFalse(profile["longest_is_guy_delimiter"])
        self.assertFalse(profile["longest_is_ca_9gram"])
        self.assertFalse(profile["top_8gram_is_guy_delimiter"])
        self.assertFalse(profile["top_8gram_is_ca_9gram"])
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCbRepeatingNgramImageSnapshot(unittest.TestCase):
    """Cycle 33 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
