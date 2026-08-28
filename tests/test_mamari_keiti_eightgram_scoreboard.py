"""Keiti (E) eightgram lock.

Cycle 83 text-search lock. Uses already-vendored Er/Ev from cycle 80
plus the cycle-81 n=9 site lock and cycle-82 Ev leftover lock. Does
not vendor a new tablet. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No new
agents. Not a meaning dictionary.

Locks E's 4 repeating 8-grams (sequences, sites) and whether each
is an 8-window of the n=9 (prefix/suffix of the two Er2 hits) vs
an independent 8-gram on Er. Claim that can lose:
has_independent_8gram.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_keiti_ev_longest_scoreboard import (
    N9_PREFIX8,
    N9_SUFFIX8,
    TestMamariKeitiEvLongestScoreboard,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    GRAM_N9,
    STANDING_ER_SITES as N9_ER_SITES,
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
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

STANDING_EIGHTGRAMS = (
    ("040", "300", "028", "004", "430", "022", "380", "203"),
    ("300", "040", "300", "028", "004", "430", "022", "380"),
    ("040", "300", "040", "300", "028", "004", "430", "022"),
    ("092", "050", "006", "670", "092", "050", "006", "670"),
)
STANDING_FREQS = (3, 2, 2, 2)
STANDING_FROM_N9 = (True, True, False, False)
STANDING_SITES = (
    (
        (SIDE_ER, "Er2", 12),
        (SIDE_ER, "Er2", 29),
        (SIDE_ER, "Er3", 11),
    ),
    (
        (SIDE_ER, "Er2", 11),
        (SIDE_ER, "Er2", 28),
    ),
    (
        (SIDE_ER, "Er2", 27),
        (SIDE_ER, "Er4", 1),
    ),
    (
        (SIDE_ER, "Er7", 7),
        (SIDE_ER, "Er7", 11),
    ),
)
STANDING_N9_WINDOWS = (N9_PREFIX8, N9_SUFFIX8)
STANDING_ALL_FROM_N9 = False
STANDING_HAS_INDEPENDENT_8GRAM = True
STANDING_FROM_N9_COUNT = 2
STANDING_INDEPENDENT_COUNT = 2
STANDING_NEW_TABLET = False
STANDING_RESULT = "e_keiti_eightgrams"
STANDING_CLAIM = "has_independent_8gram"


def n9_eight_windows(n9: tuple[str, ...] = GRAM_N9) -> tuple[tuple[str, ...], ...]:
    """Prefix and suffix 8-windows of the n=9. Search only."""
    return (n9[:8], n9[1:])


def is_from_n9(gram: tuple[str, ...], n9: tuple[str, ...] = GRAM_N9) -> bool:
    """True iff gram is a contiguous 8-window of the n=9."""
    return gram in n9_eight_windows(n9)


def all_from_n9(
    grams: tuple[tuple[str, ...], ...],
    n9: tuple[str, ...] = GRAM_N9,
) -> bool:
    """True iff every gram is a prefix or suffix of the n=9."""
    return bool(grams) and all(is_from_n9(gram, n9) for gram in grams)


def has_independent_8gram(
    grams: tuple[tuple[str, ...], ...],
    n9: tuple[str, ...] = GRAM_N9,
) -> bool:
    """True iff at least one gram is not an 8-window of the n=9."""
    return any(not is_from_n9(gram, n9) for gram in grams)


def eightgram_sites(
    gram: tuple[str, ...],
    by_side: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Er then Ev. Search only."""
    hits = named_side_hits(by_side[SIDE_ER], E_LINE_NAMES[SIDE_ER], SIDE_ER, gram)
    hits += named_side_hits(by_side[SIDE_EV], E_LINE_NAMES[SIDE_EV], SIDE_EV, gram)
    return tuple(site_tuple(hit) for hit in hits)


class TestKeitiEightgramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_n9_windows_are_prefix_and_suffix(self):
        """Only the two 8-windows of n=9 count as from_n9."""
        provider = MockProvider()
        n9 = GRAM_N9
        prefix, suffix = n9_eight_windows(n9)
        self.assertEqual(prefix, n9[:8])
        self.assertEqual(suffix, n9[1:])
        self.assertTrue(is_from_n9(prefix, n9))
        self.assertTrue(is_from_n9(suffix, n9))
        independent = ("092", "050", "006", "670", "092", "050", "006", "670")
        self.assertFalse(is_from_n9(independent, n9))
        self.assertFalse(is_from_n9(n9[:7] + ("999",), n9))
        self.assertEqual(provider.get_call_history(), [])

    def test_all_from_n9_vs_independent(self):
        """Both booleans can fail: all windows vs one outsider."""
        provider = MockProvider()
        n9 = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
        windows = n9_eight_windows(n9)
        outsider = ("X",) * 8
        self.assertTrue(all_from_n9(windows, n9))
        self.assertFalse(has_independent_8gram(windows, n9))
        mixed = windows + (outsider,)
        self.assertFalse(all_from_n9(mixed, n9))
        self.assertTrue(has_independent_8gram(mixed, n9))
        self.assertFalse(all_from_n9((), n9))
        self.assertFalse(has_independent_8gram((), n9))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariKeitiEightgramScoreboard(unittest.TestCase):
    """Cited-fixture E eightgram vs n=9 window lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_side = load_e_sides()
        self.e_profile = score_e_longest_repeating(self.by_side, self.analyzer)
        self.eightgrams = tuple(row.tokens for row in self.e_profile.eightgrams)
        self.freqs = tuple(row.freq for row in self.e_profile.eightgrams)
        self.from_n9 = tuple(is_from_n9(gram) for gram in self.eightgrams)
        self.sites = tuple(
            eightgram_sites(gram, self.by_side) for gram in self.eightgrams
        )

    def test_eightgrams_sequences_and_sites(self):
        """Four Er 8-grams; two are n=9 windows; two are independent."""
        self.assertEqual(len(self.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(self.eightgrams, STANDING_EIGHTGRAMS)
        self.assertEqual(self.freqs, STANDING_FREQS)
        self.assertEqual(self.from_n9, STANDING_FROM_N9)
        self.assertEqual(self.sites, STANDING_SITES)
        self.assertEqual(n9_eight_windows(GRAM_N9), STANDING_N9_WINDOWS)
        self.assertEqual(STANDING_N9_WINDOWS, (N9_PREFIX8, N9_SUFFIX8))
        self.assertIn(N9_PREFIX8, self.eightgrams)
        self.assertIn(N9_SUFFIX8, self.eightgrams)
        self.assertEqual(GRAM_N9, STANDING_LONGEST_NGRAM)
        self.assertEqual(N9_ER_SITES, ((SIDE_ER, "Er2", 11), (SIDE_ER, "Er2", 28)))
        for gram, sites, from_n9 in zip(
            self.eightgrams, self.sites, self.from_n9, strict=True
        ):
            self.assertEqual(is_from_n9(gram), from_n9)
            self.assertEqual(eightgram_sites(gram, self.by_side), sites)
            self.assertEqual(ngram_hit_count(self.by_side[SIDE_ER], gram), len(sites))
            self.assertEqual(ngram_hit_count(self.by_side[SIDE_EV], gram), 0)
            for side, line, index in sites:
                names = E_LINE_NAMES[side]
                stems = self.by_side[side][names.index(line)][index : index + 8]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_ER)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_has_independent_8gram_and_not_all_from_n9(self):
        """all_from_n9 is false; has_independent_8gram is true. Either can fail."""
        self.assertEqual(all_from_n9(self.eightgrams), STANDING_ALL_FROM_N9)
        self.assertEqual(
            has_independent_8gram(self.eightgrams),
            STANDING_HAS_INDEPENDENT_8GRAM,
        )
        self.assertFalse(STANDING_ALL_FROM_N9)
        self.assertTrue(STANDING_HAS_INDEPENDENT_8GRAM)
        self.assertEqual(sum(self.from_n9), STANDING_FROM_N9_COUNT)
        self.assertEqual(
            len(self.eightgrams) - sum(self.from_n9),
            STANDING_INDEPENDENT_COUNT,
        )
        self.assertEqual(STANDING_CLAIM, "has_independent_8gram")
        self.assertTrue(STANDING_HAS_INDEPENDENT_8GRAM)
        self.assertNotEqual(STANDING_ALL_FROM_N9, STANDING_HAS_INDEPENDENT_8GRAM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_e_scoreboards_still_compute(self):
        """Cycle 80 vendor, 81 n=9, and 82 Ev leftover locks stay."""
        vendor = TestMamariKeitiVendorScoreboard()
        vendor.setUp()
        vendor.test_longest_repeating_ngram_is_9_and_eightgrams_exist()
        vendor.test_survey_matches_computed_lock()
        n9 = TestMamariKeitiN9Scoreboard()
        n9.setUp()
        n9.test_n9_is_er_only_at_er2()
        n9.test_survey_matches_computed_lock()
        ev = TestMamariKeitiEvLongestScoreboard()
        ev.setUp()
        ev.test_ev_longest_is_n6_and_has_no_n_ge_8()
        ev.test_e_eightgrams_sit_on_er_not_ev()
        ev.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-83 E eightgram lock."""
        lock = self.survey["tablet_e_keiti_eightgrams"]
        self.assertEqual(lock["cycle"], 83)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_e"], "E")
        self.assertEqual(lock["name_e"], "Keiti")
        self.assertEqual(lock["n"], 8)
        self.assertEqual(lock["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(tuple(tuple(row) for row in lock["tokens"]), STANDING_EIGHTGRAMS)
        self.assertEqual(tuple(lock["freqs"]), STANDING_FREQS)
        self.assertEqual(tuple(lock["from_n9"]), STANDING_FROM_N9)
        self.assertEqual(
            tuple(tuple(tuple(site) for site in row) for row in lock["sites"]),
            STANDING_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["n9_windows"]), STANDING_N9_WINDOWS)
        self.assertEqual(tuple(lock["n9_prefix8"]), N9_PREFIX8)
        self.assertEqual(tuple(lock["n9_suffix8"]), N9_SUFFIX8)
        self.assertEqual(lock["all_from_n9"], STANDING_ALL_FROM_N9)
        self.assertEqual(lock["has_independent_8gram"], STANDING_HAS_INDEPENDENT_8GRAM)
        self.assertEqual(lock["from_n9_count"], STANDING_FROM_N9_COUNT)
        self.assertEqual(lock["independent_count"], STANDING_INDEPENDENT_COUNT)
        self.assertFalse(lock["all_from_n9"])
        self.assertTrue(lock["has_independent_8gram"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_n9_sites_unchanged"])
        self.assertTrue(lock["standing_e_keiti_ev_longest_unchanged"])
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
        self.assertEqual(self.survey["tablet_e_keiti_ev_longest"]["cycle"], 82)
        self.assertEqual(self.survey["tablet_e_keiti_vendor"]["eightgram_count"], 4)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariKeitiEightgramImageSnapshot(unittest.TestCase):
    """Cycle 83 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
