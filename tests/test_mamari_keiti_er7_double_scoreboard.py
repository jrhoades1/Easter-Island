"""Keiti (E) Er7 doubled 4-gram off-E lock.

Cycle 84 text-search lock. Uses already-vendored Er/Ev from cycle 80
plus the cycle-83 independent Er7 eightgram and already-vendored
A / B / C / D / G / K / H / P / Q / I. Does not vendor a new
tablet. Raw stems. No invented Barthel. No G00n→Barthel map. No
type merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Locks the doubled 4-gram 092 050 006 670 and its 8-gram double
on Er7 (hit count and sites) and exact hits off E on
A/B/C/D/G/K/H/P/Q/I/Ev. Claim that can lose: e_only.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_keiti_eightgram_scoreboard import (
    STANDING_EIGHTGRAMS,
    STANDING_SITES,
    TestMamariKeitiEightgramScoreboard,
)
from tests.test_mamari_keiti_ev_longest_scoreboard import (
    TestMamariKeitiEvLongestScoreboard,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    OFF_E_TABLETS as OFF_E_LETTER_TABLETS,
    TestMamariKeitiN9Scoreboard,
    load_off_e_by_tablet,
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_keiti_vendor_scoreboard import (
    E_LINE_NAMES,
    SIDE_ER,
    SIDE_EV,
    TestMamariKeitiVendorScoreboard,
    load_e_sides,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

GRAM4 = ("092", "050", "006", "670")
GRAM8 = GRAM4 + GRAM4
OFF_E_TABLETS = OFF_E_LETTER_TABLETS + ("Ev",)
ER7_LINE = "Er7"
STANDING_ER7_HITS = 2
STANDING_ER7_SITES = (
    (SIDE_ER, ER7_LINE, 7),
    (SIDE_ER, ER7_LINE, 11),
)
STANDING_OFF_E_HITS = 0
STANDING_OFF_E_BY_TABLET = (0,) * len(OFF_E_TABLETS)
STANDING_E_ONLY = True
STANDING_NEW_TABLET = False
STANDING_RESULT = "e_keiti_er7_double"
STANDING_CLAIM = "e_only"


def doubled_4gram(gram4: tuple[str, ...] = GRAM4) -> tuple[str, ...]:
    """8-gram formed by repeating the 4-gram. Search only."""
    return gram4 + gram4


def er7_line(by_side: dict[str, list[list[str]]]) -> list[str]:
    """Er7 stems from already-vendored Er. No new scrape."""
    return by_side[SIDE_ER][E_LINE_NAMES[SIDE_ER].index(ER7_LINE)]


def er7_hit_count(
    by_side: dict[str, list[list[str]]],
    gram: tuple[str, ...] = GRAM8,
) -> int:
    """Exact consecutive hits of gram on Er7 only."""
    return ngram_hit_count([er7_line(by_side)], gram)


def load_off_er7_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A/B/C/D/G/K/H/P/Q/I plus Ev. No new scrape."""
    by_tablet = dict(load_off_e_by_tablet())
    by_tablet["Ev"] = load_e_sides()[SIDE_EV]
    return by_tablet


def off_e_hit_counts(
    by_tablet: dict[str, list[list[str]]],
    gram: tuple[str, ...] = GRAM4,
) -> tuple[int, ...]:
    """Hit counts on locked off-E surfaces. Search only."""
    return tuple(ngram_hit_count(by_tablet[tablet], gram) for tablet in OFF_E_TABLETS)


def is_e_only(er7_hits: int, off_e_hits: int) -> bool:
    """True iff the gram hits Er7 and is exact-0 off E."""
    return er7_hits > 0 and off_e_hits == 0


class TestKeitiEr7DoubleHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram / 8-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(doubled_4gram(GRAM4), GRAM8)
        self.assertEqual(GRAM8, STANDING_EIGHTGRAMS[3])
        adjacent4 = [list(GRAM4) + list(GRAM4)]
        self.assertEqual(ngram_hit_count(adjacent4, GRAM4), 2)
        self.assertEqual(ngram_hit_count(adjacent4, GRAM8), 1)
        gapped = [list(GRAM4[:2]) + ["999"] + list(GRAM4[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4), 0)
        self.assertEqual(ngram_hit_count(gapped, GRAM8), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_e_only_requires_er7_and_zero_off_e(self):
        """Boolean is True only when Er7 is nonzero and off-E is 0."""
        provider = MockProvider()
        self.assertTrue(is_e_only(2, 0))
        self.assertFalse(is_e_only(2, 1))
        self.assertFalse(is_e_only(0, 0))
        self.assertFalse(is_e_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "e_only")
        self.assertEqual(provider.get_call_history(), [])


class TestMamariKeitiEr7DoubleScoreboard(unittest.TestCase):
    """Cited-fixture Er7 doubled 4-gram off-E lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_e_sides()
        self.er7_sites = named_side_hits(
            [er7_line(self.by_side)],
            (ER7_LINE,),
            SIDE_ER,
            GRAM8,
        )
        self.er7_hits = len(self.er7_sites)
        self.off_e = load_off_er7_by_tablet()
        self.off_e_counts = off_e_hit_counts(self.off_e, GRAM4)
        self.off_e_hits = sum(self.off_e_counts)
        self.off_e_8_counts = off_e_hit_counts(self.off_e, GRAM8)

    def test_er7_hits_are_two_eightgrams(self):
        """8-gram double is cycle-83 independent gram; Er7[7] and Er7[11]."""
        self.assertEqual(GRAM4, ("092", "050", "006", "670"))
        self.assertEqual(GRAM8, doubled_4gram(GRAM4))
        self.assertEqual(GRAM8, STANDING_EIGHTGRAMS[3])
        self.assertEqual(self.er7_hits, STANDING_ER7_HITS)
        self.assertEqual(STANDING_ER7_HITS, 2)
        self.assertEqual(self.er7_hits, er7_hit_count(self.by_side, GRAM8))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.er7_sites), STANDING_ER7_SITES)
        self.assertEqual(STANDING_ER7_SITES, STANDING_SITES[3])
        self.assertEqual(ngram_hit_count(self.by_side[SIDE_ER], GRAM8), STANDING_ER7_HITS)
        self.assertEqual(ngram_hit_count(self.by_side[SIDE_EV], GRAM8), 0)
        for side, line, index in STANDING_ER7_SITES:
            names = E_LINE_NAMES[side]
            stems4 = self.by_side[side][names.index(line)][index : index + 4]
            stems8 = self.by_side[side][names.index(line)][index : index + 8]
            self.assertEqual(tuple(stems4), GRAM4)
            self.assertEqual(tuple(stems8), GRAM8)
            self.assertEqual(side, SIDE_ER)
            self.assertEqual(line, ER7_LINE)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_double_is_zero_off_e_and_e_only(self):
        """4-gram and 8-gram are 0 on A, B, C, D, G, K, H, P, Q, I, Ev."""
        self.assertEqual(tuple(self.off_e), OFF_E_TABLETS)
        self.assertEqual(OFF_E_TABLETS, ("A", "B", "C", "D", "G", "K", "H", "P", "Q", "I", "Ev"))
        self.assertEqual(self.off_e_counts, STANDING_OFF_E_BY_TABLET)
        self.assertEqual(self.off_e_8_counts, STANDING_OFF_E_BY_TABLET)
        self.assertEqual(self.off_e_hits, STANDING_OFF_E_HITS)
        self.assertEqual(STANDING_OFF_E_HITS, 0)
        self.assertEqual(sum(self.off_e_8_counts), 0)
        for tablet, count4, count8 in zip(
            OFF_E_TABLETS, self.off_e_counts, self.off_e_8_counts, strict=True
        ):
            self.assertEqual(count4, ngram_hit_count(self.off_e[tablet], GRAM4))
            self.assertEqual(count8, ngram_hit_count(self.off_e[tablet], GRAM8))
            self.assertEqual(count4, 0)
            self.assertEqual(count8, 0)
        self.assertNotIn(SIDE_ER, self.off_e)
        self.assertEqual(is_e_only(self.er7_hits, self.off_e_hits), STANDING_E_ONLY)
        self.assertTrue(STANDING_E_ONLY)
        self.assertEqual(STANDING_CLAIM, "e_only")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_e_scoreboards_still_compute(self):
        """Cycle 80–83 E locks stay."""
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
        ev.test_survey_matches_computed_lock()
        eight = TestMamariKeitiEightgramScoreboard()
        eight.setUp()
        eight.test_eightgrams_sequences_and_sites()
        eight.test_has_independent_8gram_and_not_all_from_n9()
        eight.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-84 Er7 doubled 4-gram lock."""
        lock = self.survey["tablet_e_keiti_er7_double"]
        self.assertEqual(lock["cycle"], 84)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_e"], "E")
        self.assertEqual(lock["name_e"], "Keiti")
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(tuple(lock["tokens8"]), GRAM8)
        self.assertEqual(lock["n4"], 4)
        self.assertEqual(lock["n8"], 8)
        self.assertEqual(lock["er7_hits"], STANDING_ER7_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["er7_sites"]),
            STANDING_ER7_SITES,
        )
        self.assertEqual(lock["off_e_hits"], STANDING_OFF_E_HITS)
        self.assertEqual(tuple(lock["off_e_tablets"]), OFF_E_TABLETS)
        self.assertEqual(tuple(lock["off_e_by_tablet"]), STANDING_OFF_E_BY_TABLET)
        self.assertEqual(lock["e_only"], STANDING_E_ONLY)
        self.assertTrue(lock["e_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_n9_sites_unchanged"])
        self.assertTrue(lock["standing_e_keiti_ev_longest_unchanged"])
        self.assertTrue(lock["standing_e_keiti_eightgrams_unchanged"])
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
        self.assertEqual(self.survey["tablet_e_keiti_eightgrams"]["cycle"], 83)
        self.assertEqual(
            tuple(self.survey["tablet_e_keiti_eightgrams"]["tokens"][3]),
            GRAM8,
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariKeitiEr7DoubleImageSnapshot(unittest.TestCase):
    """Cycle 84 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
