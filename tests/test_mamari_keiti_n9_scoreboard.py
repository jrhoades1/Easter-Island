"""Keiti (E) n=9 site lock.

Cycle 81 text-search lock. Uses already-vendored Er/Ev from cycle 80
plus already-vendored A / B / C / D / G / K / H / P / Q / I. Does
not vendor a new tablet. The 9-gram is the cycle-80 longest
repeating n-gram. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents. Not
a meaning dictionary.

Locks the exact 9-stem sequence, Er/Ev hit counts and line/index
sites, whether the repeat is side-local (Er-only or Ev-only), and
off-E hits on A/B/C/D/G/K/H/P/Q/I. Claim that can lose: the n=9
is side-local.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_600_inventory_scoreboard import (
    PASSAGE_AA,
    PASSAGE_AB,
    PASSAGE_CALENDAR,
    PASSAGE_CB,
    PASSAGE_REMAINDER,
)
from tests.test_mamari_echancree_vendor_scoreboard import (
    SIDE_DA,
    SIDE_DB,
    load_d_sides,
)
from tests.test_mamari_keiti_vendor_scoreboard import (
    E_LINE_NAMES,
    SIDE_ER,
    SIDE_EV,
    STANDING_LONGEST_N,
    STANDING_LONGEST_NGRAM,
    TestMamariKeitiVendorScoreboard,
    load_e_sides,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    SIDE_HR,
    SIDE_HV,
    SIDE_PR,
    SIDE_PV,
)
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    PASSAGE_BR,
    PASSAGE_BV,
    PASSAGE_IA,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import (
    find_ngram_hits,
    load_corpus_survey,
)
from tests.test_mamari_small_santiago_gv_430_076_200_ngram_scoreboard import (
    PASSAGE_GR,
    PASSAGE_GV,
)
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import (
    PASSAGE_KR,
    PASSAGE_KV,
    existing_gk_17gram_lines,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides,
)
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    SIDE_QR,
    SIDE_QV,
)

GRAM_N9 = STANDING_LONGEST_NGRAM
OFF_E_TABLETS = ("A", "B", "C", "D", "G", "K", "H", "P", "Q", "I")
STANDING_ER_HITS = 2
STANDING_EV_HITS = 0
STANDING_ER_SITES = (
    (SIDE_ER, "Er2", 11),
    (SIDE_ER, "Er2", 28),
)
STANDING_EV_SITES = ()
STANDING_SIDE_LOCAL = True
STANDING_SIDE_LOCAL_SIDE = SIDE_ER
STANDING_OFF_E_HITS = 0
STANDING_OFF_E_BY_TABLET = (0,) * len(OFF_E_TABLETS)
STANDING_NEW_TABLET = False
STANDING_RESULT = "e_keiti_n9_sites"
STANDING_CLAIM = "side_local"


@dataclass(frozen=True)
class SiteHit:
    """One exact n=9 hit. Ids only; no meanings."""

    side: str
    line: str
    index: int


def site_tuple(hit: SiteHit) -> tuple[str, str, int]:
    """Stable lock row: side, line, index."""
    return (hit.side, hit.line, hit.index)


def named_side_hits(
    lines: list[list[str]],
    line_names: tuple[str, ...],
    side: str,
    gram: tuple[str, ...],
) -> tuple[SiteHit, ...]:
    """(side, line, index) for every exact hit. Search only."""
    return tuple(
        SiteHit(side, line_names[line_index], start)
        for line_index, start in find_ngram_hits(lines, gram)
    )


def is_side_local(er_hits: int, ev_hits: int) -> bool:
    """True iff the gram hits exactly one of Er or Ev."""
    return (er_hits > 0) != (ev_hits > 0)


def side_local_side(er_hits: int, ev_hits: int) -> str | None:
    """The only E side with hits, or None if not side-local."""
    if not is_side_local(er_hits, ev_hits):
        return None
    return SIDE_ER if er_hits > 0 else SIDE_EV


def load_off_e_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A/B/C/D/G/K/H/P/Q/I. No new scrape."""
    abcigk = existing_gk_17gram_lines()
    d = load_d_sides()
    hpq = load_q_h_p_sides()
    return {
        "A": abcigk[PASSAGE_AA] + abcigk[PASSAGE_AB],
        "B": abcigk[PASSAGE_BR] + abcigk[PASSAGE_BV],
        "C": abcigk[PASSAGE_CALENDAR] + abcigk[PASSAGE_REMAINDER] + abcigk[PASSAGE_CB],
        "D": d[SIDE_DA] + d[SIDE_DB],
        "G": abcigk[PASSAGE_GR] + abcigk[PASSAGE_GV],
        "K": abcigk[PASSAGE_KR] + abcigk[PASSAGE_KV],
        "H": hpq[SIDE_HR] + hpq[SIDE_HV],
        "P": hpq[SIDE_PR] + hpq[SIDE_PV],
        "Q": hpq[SIDE_QR] + hpq[SIDE_QV],
        "I": abcigk[PASSAGE_IA],
    }


def off_e_hit_counts(
    by_tablet: dict[str, list[list[str]]],
    gram: tuple[str, ...] = GRAM_N9,
) -> tuple[int, ...]:
    """Hit counts on locked off-E tablets. Search only."""
    return tuple(ngram_hit_count(by_tablet[tablet], gram) for tablet in OFF_E_TABLETS)


class TestKeitiN9Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent n=9 counts; a gap is not a hit."""
        provider = MockProvider()
        gram = GRAM_N9
        adjacent = [list(gram) + list(gram[:3])]
        self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        gapped = [list(gram[:5]) + ["999"] + list(gram[5:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        empty = [[]]
        self.assertEqual(ngram_hit_count(empty, gram), 0)
        hits = named_side_hits([list(gram), ["X"] + list(gram)], ("L1", "L2"), "Er", gram)
        self.assertEqual(tuple(site_tuple(hit) for hit in hits), (("Er", "L1", 0), ("Er", "L2", 1)))
        self.assertEqual(len(gram), STANDING_LONGEST_N)
        self.assertEqual(provider.get_call_history(), [])

    def test_side_local_is_exactly_one_side(self):
        """Boolean is True only when Er XOR Ev is nonzero."""
        provider = MockProvider()
        self.assertTrue(is_side_local(2, 0))
        self.assertTrue(is_side_local(0, 1))
        self.assertFalse(is_side_local(1, 1))
        self.assertFalse(is_side_local(0, 0))
        self.assertEqual(side_local_side(2, 0), SIDE_ER)
        self.assertEqual(side_local_side(0, 3), SIDE_EV)
        self.assertIsNone(side_local_side(1, 1))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariKeitiN9Scoreboard(unittest.TestCase):
    """Cited-fixture E n=9 sites and off-E leak lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_e_sides()
        self.er_sites = named_side_hits(
            self.by_side[SIDE_ER],
            E_LINE_NAMES[SIDE_ER],
            SIDE_ER,
            GRAM_N9,
        )
        self.ev_sites = named_side_hits(
            self.by_side[SIDE_EV],
            E_LINE_NAMES[SIDE_EV],
            SIDE_EV,
            GRAM_N9,
        )
        self.er_hits = len(self.er_sites)
        self.ev_hits = len(self.ev_sites)
        self.off_e = load_off_e_by_tablet()
        self.off_e_counts = off_e_hit_counts(self.off_e)
        self.off_e_hits = sum(self.off_e_counts)

    def test_n9_is_er_only_at_er2(self):
        """Sequence is cycle-80 n=9; Er2[11] and Er2[28]; Ev 0; side_local."""
        self.assertEqual(GRAM_N9, STANDING_LONGEST_NGRAM)
        self.assertEqual(len(GRAM_N9), STANDING_LONGEST_N)
        self.assertEqual(GRAM_N9, ("300", "040", "300", "028", "004", "430", "022", "380", "203"))
        self.assertEqual(self.er_hits, STANDING_ER_HITS)
        self.assertEqual(self.ev_hits, STANDING_EV_HITS)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.er_sites), STANDING_ER_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.ev_sites), STANDING_EV_SITES)
        self.assertEqual(self.er_hits, ngram_hit_count(self.by_side[SIDE_ER], GRAM_N9))
        self.assertEqual(self.ev_hits, ngram_hit_count(self.by_side[SIDE_EV], GRAM_N9))
        for side, line, index in STANDING_ER_SITES:
            names = E_LINE_NAMES[side]
            stems = self.by_side[side][names.index(line)][index : index + len(GRAM_N9)]
            self.assertEqual(tuple(stems), GRAM_N9)
        self.assertEqual(is_side_local(self.er_hits, self.ev_hits), STANDING_SIDE_LOCAL)
        self.assertEqual(side_local_side(self.er_hits, self.ev_hits), STANDING_SIDE_LOCAL_SIDE)
        self.assertTrue(STANDING_SIDE_LOCAL)
        self.assertEqual(STANDING_CLAIM, "side_local")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n9_is_zero_off_e(self):
        """Exact n=9 is 0 on already-vendored A, B, C, D, G, K, H, P, Q, I."""
        self.assertEqual(tuple(self.off_e), OFF_E_TABLETS)
        self.assertEqual(self.off_e_counts, STANDING_OFF_E_BY_TABLET)
        self.assertEqual(self.off_e_hits, STANDING_OFF_E_HITS)
        self.assertEqual(STANDING_OFF_E_HITS, 0)
        for tablet, count in zip(OFF_E_TABLETS, self.off_e_counts):
            self.assertEqual(count, ngram_hit_count(self.off_e[tablet], GRAM_N9))
            self.assertEqual(count, 0)
        self.assertNotIn(SIDE_ER, self.off_e)
        self.assertNotIn(SIDE_EV, self.off_e)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_e_vendor_scoreboard_still_computes(self):
        """Cycle 80 E vendor lock stays."""
        prior = TestMamariKeitiVendorScoreboard()
        prior.setUp()
        prior.test_stem_counts_and_tradition_islands_absent()
        prior.test_longest_repeating_ngram_is_9_and_eightgrams_exist()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-81 E n=9 site lock."""
        lock = self.survey["tablet_e_keiti_n9_sites"]
        self.assertEqual(lock["cycle"], 81)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_e"], "E")
        self.assertEqual(lock["name_e"], "Keiti")
        self.assertEqual(tuple(lock["tokens"]), GRAM_N9)
        self.assertEqual(lock["n"], STANDING_LONGEST_N)
        self.assertEqual(lock["er_hits"], STANDING_ER_HITS)
        self.assertEqual(lock["ev_hits"], STANDING_EV_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["er_sites"]),
            STANDING_ER_SITES,
        )
        self.assertEqual(tuple(lock["ev_sites"]), STANDING_EV_SITES)
        self.assertEqual(lock["side_local"], STANDING_SIDE_LOCAL)
        self.assertEqual(lock["side_local_side"], STANDING_SIDE_LOCAL_SIDE)
        self.assertEqual(lock["off_e_hits"], STANDING_OFF_E_HITS)
        self.assertEqual(tuple(lock["off_e_tablets"]), OFF_E_TABLETS)
        self.assertEqual(tuple(lock["off_e_by_tablet"]), STANDING_OFF_E_BY_TABLET)
        self.assertTrue(lock["side_local"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
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
        self.assertEqual(tuple(self.survey["tablet_e_keiti_vendor"]["longest_tokens"]), GRAM_N9)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariKeitiN9ImageSnapshot(unittest.TestCase):
    """Cycle 81 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
