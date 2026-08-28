"""Keiti (E) Ev longest n-gram lock.

Cycle 82 text-search lock. Uses already-vendored Er/Ev from cycle 80
plus the cycle-81 n=9 site lock. Does not vendor a new tablet.
Ev as a side (Ev-only leftover after Er's n=9). Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Locks Ev's longest repeating n-gram (n, sequence, sites), whether
n≥8 exists on Ev, and how many of E's 4 eightgrams sit on Ev vs
Er. The n=9's 8-prefix/suffix are Er. Claim that can lose:
ev_has_n_ge_8.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_keiti_n9_scoreboard import (
    GRAM_N9,
    TestMamariKeitiN9Scoreboard,
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_keiti_vendor_scoreboard import (
    E_LINE_NAMES,
    SIDE_ER,
    SIDE_EV,
    STANDING_EIGHTGRAM_COUNT,
    STANDING_LONGEST_NGRAM,
    TestMamariKeitiVendorScoreboard,
    load_e_sides,
    score_e_longest_repeating,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

GRAM_EV = ("002", "034", "002", "001", "002", "034")
N9_PREFIX8 = STANDING_LONGEST_NGRAM[:8]
N9_SUFFIX8 = STANDING_LONGEST_NGRAM[1:]
STANDING_EV_LONGEST_N = 6
STANDING_EV_HAS_N_GE_8 = False
STANDING_EV_LONGEST_NGRAM = GRAM_EV
STANDING_EV_HITS = 2
STANDING_ER_HITS = 0
STANDING_EV_SITES = (
    (SIDE_EV, "Ev1", 1),
    (SIDE_EV, "Ev6", 29),
)
STANDING_ER_SITES = ()
STANDING_E_EIGHTGRAMS_ON_ER = 4
STANDING_E_EIGHTGRAMS_ON_EV = 0
STANDING_NEW_TABLET = False
STANDING_RESULT = "e_keiti_ev_longest"
STANDING_CLAIM = "ev_has_n_ge_8"


def score_ev_longest_repeating(by_side: dict[str, list[list[str]]], analyzer: NgramAnalyzer):
    """n≥4 freq≥2 profile on Ev only. Search only."""
    return score_remainder_repeating_ngrams(
        by_side[SIDE_EV],
        analyzer,
        line_names=E_LINE_NAMES[SIDE_EV],
    )


def has_n_ge_8(profile) -> bool:
    """True iff any repeating row is n≥8."""
    return any(row.n >= 8 for row in profile.rows)


def eightgram_side_counts(
    grams: tuple[tuple[str, ...], ...],
    by_side: dict[str, list[list[str]]],
) -> tuple[int, int]:
    """How many grams sit on Er vs Ev. A gram may sit on both."""
    on_er = sum(1 for gram in grams if ngram_hit_count(by_side[SIDE_ER], gram) > 0)
    on_ev = sum(1 for gram in grams if ngram_hit_count(by_side[SIDE_EV], gram) > 0)
    return on_er, on_ev


class TestKeitiEvLongestHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_ev_scorer_uses_ev_line_names(self):
        """Spans carry Ev names; n<8 is not n≥8."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        gram = ("A", "B", "C", "D", "E", "F")
        by_side = {
            SIDE_ER: [list(gram)],
            SIDE_EV: [list(gram) + ["X"], ["Y"] + list(gram)],
        }
        profile = score_ev_longest_repeating(by_side, analyzer)
        self.assertEqual(profile.longest_n, 6)
        self.assertEqual(len(profile.longest), 1)
        self.assertEqual(profile.longest[0].spans, (("Ev1", 0, 6), ("Ev2", 1, 7)))
        self.assertFalse(has_n_ge_8(profile))
        self.assertIsNone(profile.top_8gram)
        planted8 = tuple(f"S{i}" for i in range(8))
        by_side[SIDE_EV] = [list(planted8), list(planted8)]
        self.assertTrue(has_n_ge_8(score_ev_longest_repeating(by_side, analyzer)))
        self.assertEqual(provider.get_call_history(), [])

    def test_eightgram_side_counts_split_er_and_ev(self):
        """A gram on Er only, Ev only, or both is counted per side."""
        provider = MockProvider()
        er_only = tuple(f"R{i}" for i in range(8))
        ev_only = tuple(f"V{i}" for i in range(8))
        both = tuple(f"B{i}" for i in range(8))
        by_side = {
            SIDE_ER: [list(er_only), list(both)],
            SIDE_EV: [list(ev_only), list(both)],
        }
        self.assertEqual(eightgram_side_counts((er_only, ev_only, both), by_side), (2, 2))
        self.assertEqual(eightgram_side_counts((er_only,), by_side), (1, 0))
        self.assertEqual(eightgram_side_counts((ev_only,), by_side), (0, 1))
        self.assertEqual(eightgram_side_counts((), by_side), (0, 0))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariKeitiEvLongestScoreboard(unittest.TestCase):
    """Cited-fixture Ev longest n-gram lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_side = load_e_sides()
        self.ev_profile = score_ev_longest_repeating(self.by_side, self.analyzer)
        self.e_profile = score_e_longest_repeating(self.by_side, self.analyzer)
        self.ev_sites = named_side_hits(
            self.by_side[SIDE_EV],
            E_LINE_NAMES[SIDE_EV],
            SIDE_EV,
            GRAM_EV,
        )
        self.er_sites = named_side_hits(
            self.by_side[SIDE_ER],
            E_LINE_NAMES[SIDE_ER],
            SIDE_ER,
            GRAM_EV,
        )
        self.e_eightgrams = tuple(row.tokens for row in self.e_profile.eightgrams)
        self.e_eightgrams_on_er, self.e_eightgrams_on_ev = eightgram_side_counts(
            self.e_eightgrams,
            self.by_side,
        )

    def test_ev_longest_is_n6_and_has_no_n_ge_8(self):
        """Ev leftover longest is n=6 at Ev1[1] / Ev6[29]; ev_has_n_ge_8 is false."""
        self.assertEqual(self.ev_profile.longest_n, STANDING_EV_LONGEST_N)
        self.assertEqual(self.ev_profile.longest_n, 6)
        self.assertEqual(len(self.ev_profile.longest), 1)
        self.assertEqual(self.ev_profile.longest[0].tokens, STANDING_EV_LONGEST_NGRAM)
        self.assertEqual(GRAM_EV, ("002", "034", "002", "001", "002", "034"))
        self.assertEqual(len(GRAM_EV), STANDING_EV_LONGEST_N)
        self.assertEqual(len(self.ev_sites), STANDING_EV_HITS)
        self.assertEqual(len(self.er_sites), STANDING_ER_HITS)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.ev_sites), STANDING_EV_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.er_sites), STANDING_ER_SITES)
        self.assertEqual(self.ev_profile.longest[0].freq, STANDING_EV_HITS)
        self.assertEqual(ngram_hit_count(self.by_side[SIDE_EV], GRAM_EV), STANDING_EV_HITS)
        self.assertEqual(ngram_hit_count(self.by_side[SIDE_ER], GRAM_EV), STANDING_ER_HITS)
        for side, line, index in STANDING_EV_SITES:
            names = E_LINE_NAMES[side]
            stems = self.by_side[side][names.index(line)][index : index + len(GRAM_EV)]
            self.assertEqual(tuple(stems), GRAM_EV)
        self.assertEqual(has_n_ge_8(self.ev_profile), STANDING_EV_HAS_N_GE_8)
        self.assertFalse(STANDING_EV_HAS_N_GE_8)
        self.assertEqual(self.ev_profile.eightgrams, ())
        self.assertIsNone(self.ev_profile.top_8gram)
        self.assertEqual(STANDING_CLAIM, "ev_has_n_ge_8")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_e_eightgrams_sit_on_er_not_ev(self):
        """E's 4 eightgrams, including the n=9 8-prefix/suffix, are Er-only."""
        self.assertEqual(len(self.e_eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.e_eightgrams_on_er, STANDING_E_EIGHTGRAMS_ON_ER)
        self.assertEqual(self.e_eightgrams_on_ev, STANDING_E_EIGHTGRAMS_ON_EV)
        self.assertEqual(STANDING_E_EIGHTGRAMS_ON_ER, 4)
        self.assertEqual(STANDING_E_EIGHTGRAMS_ON_EV, 0)
        self.assertEqual(N9_PREFIX8, STANDING_LONGEST_NGRAM[:8])
        self.assertEqual(N9_SUFFIX8, STANDING_LONGEST_NGRAM[1:])
        self.assertIn(N9_PREFIX8, self.e_eightgrams)
        self.assertIn(N9_SUFFIX8, self.e_eightgrams)
        self.assertGreater(ngram_hit_count(self.by_side[SIDE_ER], N9_PREFIX8), 0)
        self.assertGreater(ngram_hit_count(self.by_side[SIDE_ER], N9_SUFFIX8), 0)
        self.assertEqual(ngram_hit_count(self.by_side[SIDE_EV], N9_PREFIX8), 0)
        self.assertEqual(ngram_hit_count(self.by_side[SIDE_EV], N9_SUFFIX8), 0)
        self.assertEqual(GRAM_N9, STANDING_LONGEST_NGRAM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_e_scoreboards_still_compute(self):
        """Cycle 80 vendor lock and cycle 81 n=9 site lock stay."""
        vendor = TestMamariKeitiVendorScoreboard()
        vendor.setUp()
        vendor.test_longest_repeating_ngram_is_9_and_eightgrams_exist()
        vendor.test_survey_matches_computed_lock()
        n9 = TestMamariKeitiN9Scoreboard()
        n9.setUp()
        n9.test_n9_is_er_only_at_er2()
        n9.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-82 Ev longest n-gram lock."""
        lock = self.survey["tablet_e_keiti_ev_longest"]
        self.assertEqual(lock["cycle"], 82)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_e"], "E")
        self.assertEqual(lock["name_e"], "Keiti")
        self.assertEqual(lock["side"], SIDE_EV)
        self.assertEqual(lock["ev_longest_n"], STANDING_EV_LONGEST_N)
        self.assertEqual(lock["ev_has_n_ge_8"], STANDING_EV_HAS_N_GE_8)
        self.assertEqual(tuple(lock["tokens"]), STANDING_EV_LONGEST_NGRAM)
        self.assertEqual(lock["ev_hits"], STANDING_EV_HITS)
        self.assertEqual(lock["er_hits"], STANDING_ER_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["ev_sites"]),
            STANDING_EV_SITES,
        )
        self.assertEqual(tuple(lock["er_sites"]), STANDING_ER_SITES)
        self.assertEqual(lock["e_eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(lock["e_eightgrams_on_er"], STANDING_E_EIGHTGRAMS_ON_ER)
        self.assertEqual(lock["e_eightgrams_on_ev"], STANDING_E_EIGHTGRAMS_ON_EV)
        self.assertEqual(tuple(lock["n9_prefix8"]), N9_PREFIX8)
        self.assertEqual(tuple(lock["n9_suffix8"]), N9_SUFFIX8)
        self.assertFalse(lock["ev_has_n_ge_8"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_n9_sites_unchanged"])
        self.assertTrue(lock["standing_d_echancree_vendor_unchanged"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_gr_locks_unchanged"])
        self.assertTrue(lock["standing_gv_locks_unchanged"])
        self.assertTrue(lock["standing_kr_locks_unchanged"])
        self.assertTrue(lock["standing_kv_locks_unchanged"])
        self.assertTrue(lock["standing_hp_vendor_unchanged"])
        self.assertTrue(lock["standing_q_vendor_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["cycle"], 80)
        self.assertEqual(self.survey["tablet_e_keiti_n9_sites"]["cycle"], 81)
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["eightgram_count"], 4)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariKeitiEvLongestImageSnapshot(unittest.TestCase):
    """Cycle 82 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
