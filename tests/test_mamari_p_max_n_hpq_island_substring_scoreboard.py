"""P's cycle-99/104 representative 6-gram vs locked H∩P∩Q n≥8 islands.

Cycle 107 text-search lock. Uses already-vendored A–V and the
cycle-99/104 P representative plus the cycle-71 five maximal
H∩P∩Q islands. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Does not redo H∩P∩Q n≥8
inventories. Raw stems. No invented Barthel. No G00n→Barthel map.
No type merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Locks exact hit sites of 062 006 001 062 006 001 on P, H, and Q
(same contiguous Barthel parser as the leak table) and whether
that 6-gram is an exact contiguous substring of a locked H∩P∩Q
n≥8 island. Claim that can lose: p_max_n_is_hpq_island_substring.
A leak-count clash locks the real counts and fails the cycle-104
restatement (no retune).

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_N as INVENTORY_LONGEST_N,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_TOKENS as INVENTORY_LONGEST_TOKENS,
)
from tests.test_mamari_corpus_max_n_leak_table_scoreboard import (
    HYPOTHESIS_LEAK_PAIRS,
    TestMamariCorpusMaxNLeakTableScoreboard,
    leak_table_holds,
    leaks_from_hits,
    representative_hits,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_hpq_island_off_hpq_scoreboard import (
    LOCKED_ISLANDS,
    TestMamariHpqIslandOffHpqScoreboard,
)
from tests.test_mamari_hpq_triple_n8_scoreboard import (
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    TestMamariHpqTripleN8Scoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
    substring_offsets,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
    HR_LINE_NAMES,
    HV_LINE_NAMES,
    P_SIDES,
    PR_LINE_NAMES,
    PV_LINE_NAMES,
    SIDE_HR,
    SIDE_HV,
    SIDE_PR,
    SIDE_PV,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    named_qhp_hits,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides as load_h_p_q_sides,
)
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    Q_SIDES,
    QR_LINE_NAMES,
    QV_LINE_NAMES,
    SIDE_QR,
    SIDE_QV,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

GRAM6 = INVENTORY_LONGEST_TOKENS["P"]
STANDING_P_HITS = 2
STANDING_H_HITS = 2
STANDING_Q_HITS = 2
STANDING_HR_HITS = 2
STANDING_HV_HITS = 0
STANDING_PR_HITS = 2
STANDING_PV_HITS = 0
STANDING_QR_HITS = 2
STANDING_QV_HITS = 0
STANDING_P_SITES = (
    (SIDE_PR, "Pr3", 14),
    (SIDE_PR, "Pr3", 17),
)
STANDING_H_SITES = (
    (SIDE_HR, "Hr3", 27),
    (SIDE_HR, "Hr3", 30),
)
STANDING_Q_SITES = (
    (SIDE_QR, "Qr3", 7),
    (SIDE_QR, "Qr3", 10),
)
STANDING_HV_SITES = ()
STANDING_PV_SITES = ()
STANDING_QV_SITES = ()
STANDING_HITS_BY_TABLET = (
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    2,
    0,
    0,
    0,
    0,
    0,
)
STANDING_LEAK_COUNTS = {"H": 2, "Q": 2}
STANDING_LEAK_TABLE_HOLDS = True
STANDING_ISLAND_N = 11
STANDING_ISLAND_TOKENS = (
    "062",
    "006",
    "001",
    "062",
    "006",
    "001",
    "062",
    "006",
    "001",
    "020",
    "064",
)
STANDING_ISLAND_H_SITE = (SIDE_HR, "Hr3", 27)
STANDING_ISLAND_P_SITE = (SIDE_PR, "Pr3", 14)
STANDING_ISLAND_Q_SITE = (SIDE_QR, "Qr3", 7)
STANDING_ISLAND_OFFSETS = (0, 3)
STANDING_MATCHING_ISLANDS = (
    (
        STANDING_ISLAND_TOKENS,
        STANDING_ISLAND_N,
        STANDING_ISLAND_H_SITE,
        STANDING_ISLAND_P_SITE,
        STANDING_ISLAND_Q_SITE,
        STANDING_ISLAND_OFFSETS,
    ),
)
STANDING_MATCHING_ISLAND_COUNT = 1
STANDING_P_MAX_N_IS_HPQ_ISLAND_SUBSTRING = True
STANDING_CLAIM = "p_max_n_is_hpq_island_substring"
STANDING_RESULT = "p_max_n_hpq_island_substring"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False

LINE_NAMES = {
    SIDE_HR: HR_LINE_NAMES,
    SIDE_HV: HV_LINE_NAMES,
    SIDE_PR: PR_LINE_NAMES,
    SIDE_PV: PV_LINE_NAMES,
    SIDE_QR: QR_LINE_NAMES,
    SIDE_QV: QV_LINE_NAMES,
}


def matching_islands(
    gram: tuple[str, ...] = GRAM6,
    maximals: tuple = STANDING_MAXIMALS,
) -> tuple[tuple, ...]:
    """Locked islands whose tokens contain gram as a contiguous run."""
    rows = []
    for tokens, n, _freq_h, _freq_p, _freq_q, h_site, p_site, q_site in maximals:
        offsets = substring_offsets(gram, tokens)
        if offsets:
            rows.append((tokens, n, h_site, p_site, q_site, offsets))
    return tuple(rows)


def p_max_n_is_hpq_island_substring(
    gram: tuple[str, ...] = GRAM6,
    maximals: tuple = STANDING_MAXIMALS,
) -> bool:
    """True iff the P representative sits inside at least one locked island."""
    return bool(matching_islands(gram, maximals))


class TestPMaxNHpqIslandSubstringHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_substring_requires_contiguous_tokens(self):
        """A gap is not a substring; the planted island is."""
        provider = MockProvider()
        self.assertEqual(GRAM6, ("062", "006", "001", "062", "006", "001"))
        self.assertTrue(is_contiguous_substring(GRAM6, STANDING_ISLAND_TOKENS))
        self.assertEqual(substring_offsets(GRAM6, STANDING_ISLAND_TOKENS), (0, 3))
        gapped = STANDING_ISLAND_TOKENS[:3] + ("999",) + STANDING_ISLAND_TOKENS[3:]
        self.assertFalse(is_contiguous_substring(GRAM6, gapped[:7]))
        self.assertEqual(
            substring_offsets(GRAM6, ("062", "006", "999", "001", "062", "006", "001")),
            (),
        )
        self.assertEqual(substring_offsets((), STANDING_ISLAND_TOKENS), ())
        self.assertEqual(substring_offsets(GRAM6, GRAM6[:5]), ())
        self.assertTrue(is_contiguous_substring(GRAM6, GRAM6))
        self.assertEqual(provider.get_call_history(), [])

    def test_matching_islands_are_exact_locked_rows(self):
        """Only islands that contain the 6-gram count; a miss stays empty."""
        provider = MockProvider()
        planted = (
            (
                STANDING_ISLAND_TOKENS,
                11,
                1,
                1,
                1,
                STANDING_ISLAND_H_SITE,
                STANDING_ISLAND_P_SITE,
                STANDING_ISLAND_Q_SITE,
            ),
            (
                ("002", "144", "002", "662", "680", "005", "010", "005"),
                8,
                1,
                1,
                1,
                ("Hr", "Hx", 0),
                ("Pr", "Px", 0),
                ("Qr", "Qx", 0),
            ),
        )
        self.assertEqual(matching_islands(GRAM6, planted), STANDING_MATCHING_ISLANDS)
        self.assertTrue(p_max_n_is_hpq_island_substring(GRAM6, planted))
        self.assertFalse(
            p_max_n_is_hpq_island_substring(
                ("999", "999", "999", "999", "999", "999"), planted
            )
        )
        self.assertEqual(STANDING_CLAIM, "p_max_n_is_hpq_island_substring")
        self.assertTrue(STANDING_P_MAX_N_IS_HPQ_ISLAND_SUBSTRING)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariPMaxNHpqIslandSubstringScoreboard(unittest.TestCase):
    """Cited-fixture P 6-gram vs H∩P∩Q islands. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.hpq_sides = load_h_p_q_sides()
        self.p_sites = named_qhp_hits(self.hpq_sides, P_SIDES, GRAM6)
        self.h_sites = named_qhp_hits(self.hpq_sides, H_SIDES, GRAM6)
        self.q_sites = named_qhp_hits(self.hpq_sides, Q_SIDES, GRAM6)
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM6, VENDORED_TABLETS)
        self.leaks = leaks_from_hits("P", self.hits_by_tablet)
        self.matches = matching_islands(GRAM6)
        self.claim_holds = p_max_n_is_hpq_island_substring(GRAM6)

    def test_tokens_are_cycle_99_p_representative(self):
        """6-gram is the cycle-99/104 P representative. None invented."""
        self.assertEqual(GRAM6, INVENTORY_LONGEST_TOKENS["P"])
        self.assertEqual(GRAM6, ("062", "006", "001", "062", "006", "001"))
        self.assertEqual(INVENTORY_LONGEST_N["P"], 6)
        self.assertEqual(len(GRAM6), 6)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["P"]["longest_tokens"]),
            GRAM6,
        )
        self.assertEqual(
            tuple(self.survey["corpus_max_n_leak_table"]["rows"]["P"]["longest_tokens"]),
            GRAM6,
        )
        self.assertEqual(
            self.survey["corpus_longest_n_inventory"]["rows"]["P"]["longest_n"], 6
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leak_counts_hold_at_cycle_104_sites(self):
        """H=2, Q=2, P=2; else 0 on A–V. Leak-table restatement holds."""
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("H")], STANDING_H_HITS)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("P")], STANDING_P_HITS)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("Q")], STANDING_Q_HITS)
        self.assertEqual(self.leaks, STANDING_LEAK_COUNTS)
        for letter, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], GRAM6))
            if letter not in ("H", "P", "Q"):
                self.assertEqual(count, 0)
        representative = representative_hits(GRAM6, self.by_tablet)
        self.assertEqual(representative, STANDING_HITS_BY_TABLET)
        self.assertEqual(leaks_from_hits("P", representative), {"H": 2, "Q": 2})
        self.assertTrue(
            leak_table_holds(
                {
                    "H": {"Q": 2},
                    "K": {"B": 3, "G": 2},
                    "P": self.leaks,
                    "Q": {"H": 2},
                }
            )
        )
        self.assertTrue(STANDING_LEAK_TABLE_HOLDS)
        self.assertIn(("P", "H", 2), HYPOTHESIS_LEAK_PAIRS)
        self.assertIn(("P", "Q", 2), HYPOTHESIS_LEAK_PAIRS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_h_p_and_q_sites_are_locked_addresses(self):
        """P→H and P→Q leaks have site lists, not just counts."""
        self.assertEqual(tuple(self.p_sites), STANDING_P_SITES)
        self.assertEqual(tuple(self.h_sites), STANDING_H_SITES)
        self.assertEqual(tuple(self.q_sites), STANDING_Q_SITES)
        self.assertEqual(len(self.p_sites), STANDING_P_HITS)
        self.assertEqual(len(self.h_sites), STANDING_H_HITS)
        self.assertEqual(len(self.q_sites), STANDING_Q_HITS)
        self.assertEqual(STANDING_HV_SITES, ())
        self.assertEqual(STANDING_PV_SITES, ())
        self.assertEqual(STANDING_QV_SITES, ())
        self.assertEqual(ngram_hit_count(self.hpq_sides[SIDE_HR], GRAM6), STANDING_HR_HITS)
        self.assertEqual(ngram_hit_count(self.hpq_sides[SIDE_HV], GRAM6), STANDING_HV_HITS)
        self.assertEqual(ngram_hit_count(self.hpq_sides[SIDE_PR], GRAM6), STANDING_PR_HITS)
        self.assertEqual(ngram_hit_count(self.hpq_sides[SIDE_PV], GRAM6), STANDING_PV_HITS)
        self.assertEqual(ngram_hit_count(self.hpq_sides[SIDE_QR], GRAM6), STANDING_QR_HITS)
        self.assertEqual(ngram_hit_count(self.hpq_sides[SIDE_QV], GRAM6), STANDING_QV_HITS)
        for side, line, index in STANDING_H_SITES + STANDING_P_SITES + STANDING_Q_SITES:
            names = LINE_NAMES[side]
            stems = self.hpq_sides[side][names.index(line)][index : index + 6]
            self.assertEqual(tuple(stems), GRAM6)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_6gram_is_substring_of_locked_n11_island_only(self):
        """Boolean is true; only the Hr3[27]/Pr3[14]/Qr3[7] n=11 island contains it."""
        self.assertEqual(len(LOCKED_ISLANDS), STANDING_MAXIMAL_COUNT)
        self.assertEqual(STANDING_MAXIMAL_COUNT, 5)
        self.assertEqual(self.matches, STANDING_MATCHING_ISLANDS)
        self.assertEqual(len(self.matches), STANDING_MATCHING_ISLAND_COUNT)
        self.assertEqual(STANDING_MATCHING_ISLAND_COUNT, 1)
        tokens, n, h_site, p_site, q_site, offsets = self.matches[0]
        self.assertEqual(tokens, STANDING_ISLAND_TOKENS)
        self.assertEqual(tokens, STANDING_MAXIMALS[1][0])
        self.assertEqual(n, STANDING_ISLAND_N)
        self.assertEqual(h_site, STANDING_ISLAND_H_SITE)
        self.assertEqual(p_site, STANDING_ISLAND_P_SITE)
        self.assertEqual(q_site, STANDING_ISLAND_Q_SITE)
        self.assertEqual(offsets, STANDING_ISLAND_OFFSETS)
        self.assertTrue(is_contiguous_substring(GRAM6, STANDING_ISLAND_TOKENS))
        for island in LOCKED_ISLANDS:
            if island == STANDING_ISLAND_TOKENS:
                self.assertTrue(is_contiguous_substring(GRAM6, island))
            else:
                self.assertFalse(is_contiguous_substring(GRAM6, island))
        h_start = STANDING_ISLAND_H_SITE[2]
        p_start = STANDING_ISLAND_P_SITE[2]
        q_start = STANDING_ISLAND_Q_SITE[2]
        self.assertEqual(
            tuple((SIDE_HR, "Hr3", h_start + offset) for offset in offsets),
            STANDING_H_SITES,
        )
        self.assertEqual(
            tuple((SIDE_PR, "Pr3", p_start + offset) for offset in offsets),
            STANDING_P_SITES,
        )
        self.assertEqual(
            tuple((SIDE_QR, "Qr3", q_start + offset) for offset in offsets),
            STANDING_Q_SITES,
        )
        self.assertEqual(self.claim_holds, STANDING_P_MAX_N_IS_HPQ_ISLAND_SUBSTRING)
        self.assertTrue(STANDING_P_MAX_N_IS_HPQ_ISLAND_SUBSTRING)
        self.assertEqual(STANDING_CLAIM, "p_max_n_is_hpq_island_substring")
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertLess(len(GRAM6), 8)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_leak_inventory_and_hpq_scoreboards_still_compute(self):
        """Cycle 104 leak table, cycle 71 H∩P∩Q, cycle 72 off-H/P/Q, and W stay."""
        prior_leak = TestMamariCorpusMaxNLeakTableScoreboard()
        prior_leak.setUp()
        prior_leak.test_leak_table_holds_at_cycle_99_counts()
        prior_leak.test_survey_matches_computed_lock()
        prior_n8 = TestMamariHpqTripleN8Scoreboard()
        prior_n8.setUp()
        prior_n8.test_inventory_tokens_n_freq_and_hits()
        prior_n8.test_survey_matches_computed_lock()
        prior_off = TestMamariHpqIslandOffHpqScoreboard()
        prior_off.setUp()
        prior_off.test_five_by_twelve_hit_table()
        prior_off.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-107 P 6-gram island lock."""
        lock = self.survey["p_max_n_hpq_island_substring"]
        self.assertEqual(lock["cycle"], 107)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens6"]), GRAM6)
        self.assertEqual(lock["n6"], 6)
        self.assertEqual(lock["from_cycle"], 99)
        self.assertEqual(lock["p_hits"], STANDING_P_HITS)
        self.assertEqual(lock["h_hits"], STANDING_H_HITS)
        self.assertEqual(lock["q_hits"], STANDING_Q_HITS)
        self.assertEqual(tuple(tuple(row) for row in lock["p_sites"]), STANDING_P_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["h_sites"]), STANDING_H_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["q_sites"]), STANDING_Q_SITES)
        self.assertEqual(lock["hr_hits"], STANDING_HR_HITS)
        self.assertEqual(lock["hv_hits"], STANDING_HV_HITS)
        self.assertEqual(lock["pr_hits"], STANDING_PR_HITS)
        self.assertEqual(lock["pv_hits"], STANDING_PV_HITS)
        self.assertEqual(lock["qr_hits"], STANDING_QR_HITS)
        self.assertEqual(lock["qv_hits"], STANDING_QV_HITS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["leak_counts"], STANDING_LEAK_COUNTS)
        self.assertTrue(lock["leak_table_holds"])
        self.assertEqual(lock["leak_table_holds"], STANDING_LEAK_TABLE_HOLDS)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["p_max_n_is_hpq_island_substring"])
        self.assertEqual(
            lock["p_max_n_is_hpq_island_substring"],
            STANDING_P_MAX_N_IS_HPQ_ISLAND_SUBSTRING,
        )
        self.assertEqual(lock["matching_island_count"], STANDING_MATCHING_ISLAND_COUNT)
        self.assertEqual(lock["island_count"], STANDING_MAXIMAL_COUNT)
        match = lock["matching_islands"][0]
        self.assertEqual(tuple(match["tokens"]), STANDING_ISLAND_TOKENS)
        self.assertEqual(match["n"], STANDING_ISLAND_N)
        self.assertEqual(tuple(match["h_site"]), STANDING_ISLAND_H_SITE)
        self.assertEqual(tuple(match["p_site"]), STANDING_ISLAND_P_SITE)
        self.assertEqual(tuple(match["q_site"]), STANDING_ISLAND_Q_SITE)
        self.assertEqual(tuple(match["offsets"]), STANDING_ISLAND_OFFSETS)
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(
            self.survey["corpus_max_n_leak_table"]["rows"]["P"]["leak_counts"],
            {"H": 2, "Q": 2},
        )
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertEqual(
            self.survey["tablet_h_p_q_triple_n8_inventory"]["maximal_count"], 5
        )
        self.assertEqual(self.survey["tablet_h_p_q_island_off_hpq_hits"]["cycle"], 72)
        self.assertFalse(self.survey["tablet_h_p_q_island_off_hpq_hits"]["any_off_hpq"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariPMaxNHpqIslandSubstringImageSnapshot(unittest.TestCase):
    """Cycle 107 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
