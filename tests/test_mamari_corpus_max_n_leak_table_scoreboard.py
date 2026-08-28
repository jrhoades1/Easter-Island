"""A–V max-n leak table.

Cycle 104 text-search lock. Uses already-vendored A–V and the
cycle-99 representative longest n-grams. Does not vendor a new
tablet. Does not scrape X. W has no Barthel (cycle 100); skip W.
Raw stems. No invented sequences. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Locks exact off-home hits of each tablet's cycle-99 representative
on every vendored tablet A–V. Claim that can lose: leak_table_holds
(the only off-home leaks are H→Q×2, K→B×3 and K→G×2, P→H×2 and
P→Q×2, Q→H×2 at those exact counts; every other representative is
exact-0 off home). Cycle 99 recorded those pairs as survey notes,
not this dedicated scoreboard. A count mismatch locks the real
table and fails the claim (no retune).

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    PROFILE_MIN_N,
    STANDING_LEAK_COUNTS as HYPOTHESIS_LEAK_COUNTS,
    STANDING_LONGEST_N,
    STANDING_LONGEST_TOKENS,
    STANDING_OWN_HITS,
    VENDORED_TABLETS,
    TestMamariCorpusLongestNInventoryScoreboard,
    leak_counts,
    load_vendored_a_through_v,
    tablet_only_flag,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    TestMamariSantiagoIaIOnlyScoreboard,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

ZERO_N_TABLETS = tuple(
    letter for letter in VENDORED_TABLETS if STANDING_LONGEST_N[letter] < PROFILE_MIN_N
)
LEAKING_HOMES = ("H", "K", "P", "Q")
ZERO_OFF_HOME = tuple(
    letter for letter in VENDORED_TABLETS if letter not in LEAKING_HOMES
)
HYPOTHESIS_LEAK_PAIRS = (
    ("H", "Q", 2),
    ("K", "B", 3),
    ("K", "G", 2),
    ("P", "H", 2),
    ("P", "Q", 2),
    ("Q", "H", 2),
)
STANDING_HITS_BY_TABLET = {
    "A": (2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "B": (0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "C": (0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "D": (0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "E": (0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "F": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "G": (0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "H": (0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0),
    "I": (0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "J": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "K": (0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "L": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "M": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "N": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    "O": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "P": (0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0),
    "Q": (0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0),
    "R": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "S": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0),
    "T": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "U": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "V": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2),
}
STANDING_LEAK_COUNTS = {
    "H": {"Q": 2},
    "K": {"B": 3, "G": 2},
    "P": {"H": 2, "Q": 2},
    "Q": {"H": 2},
}
STANDING_LEAK_PAIRS = HYPOTHESIS_LEAK_PAIRS
STANDING_LEAK_HITS = {
    letter: sum(STANDING_LEAK_COUNTS.get(letter, {}).values())
    for letter in VENDORED_TABLETS
}
STANDING_CLAIM = "leak_table_holds"
STANDING_LEAK_TABLE_HOLDS = True
STANDING_RESULT = "corpus_max_n_leak_table"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False


def representative_hits(
    gram: tuple[str, ...],
    by_tablet: dict[str, list[list[str]]],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> tuple[int, ...]:
    """Full A–V hit counts. Empty / n<4 gram is 0 everywhere."""
    if len(gram) < PROFILE_MIN_N:
        return (0,) * len(tablets)
    return tablet_hit_counts(by_tablet, gram, tablets)


def leaks_from_hits(
    letter: str,
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> dict[str, int]:
    """Off-home counts >0. Counts only; not island status."""
    return {
        other: count
        for other, count in zip(tablets, hits, strict=True)
        if other != letter and count
    }


def leak_pairs(
    leaks: dict[str, dict[str, int]],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> tuple[tuple[str, str, int], ...]:
    """Stable from→to rows in letter order."""
    pairs: list[tuple[str, str, int]] = []
    for home in tablets:
        for other in tablets:
            count = leaks.get(home, {}).get(other)
            if count:
                pairs.append((home, other, count))
    return tuple(pairs)


def hypothesized_leaks(
    tablets: tuple[str, ...] = VENDORED_TABLETS,
    hypothesized: dict[str, dict[str, int]] = HYPOTHESIS_LEAK_COUNTS,
) -> dict[str, dict[str, int]]:
    """Cycle-99 survey notes, including exact-0 homes."""
    return {letter: dict(hypothesized.get(letter, {})) for letter in tablets}


def leak_table_holds(
    measured: dict[str, dict[str, int]],
    hypothesized: dict[str, dict[str, int]] | None = None,
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> bool:
    """True iff every home's off-tablet leaks match the hypothesized table."""
    expected = hypothesized_leaks(tablets, hypothesized or HYPOTHESIS_LEAK_COUNTS)
    return {letter: dict(measured.get(letter, {})) for letter in tablets} == expected


class TestCorpusMaxNLeakTableHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent n-gram counts; a gap is not a hit."""
        provider = MockProvider()
        gram = STANDING_LONGEST_TOKENS["H"]
        self.assertEqual(gram, ("072", "450", "052", "551", "003", "600", "003"))
        adjacent = [list(gram), list(gram)]
        self.assertEqual(ngram_hit_count(adjacent, gram), 2)
        gapped = [list(gram[:3]) + ["999"] + list(gram[3:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        self.assertEqual(ngram_hit_count([[]], gram), 0)
        empty = representative_hits((), {"A": [list(gram)]}, ("A",))
        self.assertEqual(empty, (0,))
        self.assertEqual(provider.get_call_history(), [])

    def test_count_mismatch_fails_claim_and_keeps_real_table(self):
        """A leak-count clash fails leak_table_holds; both tables stay."""
        provider = MockProvider()
        hypothesized = hypothesized_leaks()
        measured = hypothesized_leaks()
        measured["H"] = {"Q": 3}
        self.assertEqual(hypothesized["H"], {"Q": 2})
        self.assertEqual(measured["H"], {"Q": 3})
        self.assertFalse(leak_table_holds(measured, hypothesized))
        extra = hypothesized_leaks()
        extra["A"] = {"B": 1}
        self.assertFalse(leak_table_holds(extra, hypothesized))
        missing = hypothesized_leaks()
        missing["K"] = {"B": 3}
        self.assertFalse(leak_table_holds(missing, hypothesized))
        self.assertTrue(leak_table_holds(hypothesized, hypothesized))
        self.assertEqual(STANDING_CLAIM, "leak_table_holds")
        self.assertTrue(STANDING_LEAK_TABLE_HOLDS)
        self.assertEqual(provider.get_call_history(), [])

    def test_leak_pairs_are_from_to_counts_in_letter_order(self):
        """Pairs are (home, other, count); n<4 homes contribute none."""
        provider = MockProvider()
        hypothesized = hypothesized_leaks()
        self.assertEqual(leak_pairs(hypothesized), HYPOTHESIS_LEAK_PAIRS)
        self.assertEqual(ZERO_N_TABLETS, ("F", "J", "L", "O", "R", "T", "U"))
        self.assertEqual(ZERO_OFF_HOME, tuple("ABCDEFGIJLMNORSTUV"))
        self.assertEqual(LEAKING_HOMES, ("H", "K", "P", "Q"))
        planted = [list(STANDING_LONGEST_TOKENS["K"])]
        hits = representative_hits(
            STANDING_LONGEST_TOKENS["K"],
            {"K": planted, "B": planted * 3, "A": []},
            ("A", "B", "K"),
        )
        self.assertEqual(hits, (0, 3, 1))
        self.assertEqual(leaks_from_hits("K", hits, ("A", "B", "K")), {"B": 3})
        self.assertEqual(provider.get_call_history(), [])


class TestMamariCorpusMaxNLeakTableScoreboard(unittest.TestCase):
    """Cited-fixture A–V max-n leak table. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.hits = {
            letter: representative_hits(
                STANDING_LONGEST_TOKENS[letter], self.by_tablet
            )
            for letter in VENDORED_TABLETS
        }
        self.leaks = {
            letter: leaks_from_hits(letter, self.hits[letter])
            for letter in VENDORED_TABLETS
        }
        self.inventory_leaks = {
            letter: (
                leak_counts(
                    STANDING_LONGEST_TOKENS[letter], self.by_tablet, letter
                )
                if STANDING_LONGEST_N[letter] >= PROFILE_MIN_N
                else {}
            )
            for letter in VENDORED_TABLETS
        }
        self.own_hits = {
            letter: self.hits[letter][VENDORED_TABLETS.index(letter)]
            for letter in VENDORED_TABLETS
        }
        self.leak_hits = {
            letter: sum(self.leaks[letter].values()) for letter in VENDORED_TABLETS
        }
        self.pairs = leak_pairs(self.leaks)
        self.claim_holds = leak_table_holds(self.leaks)

    def test_representatives_are_cycle_99_tokens(self):
        """Tokens come from the inventory. None are invented. W is skipped."""
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertEqual(set(self.by_tablet), set(VENDORED_TABLETS))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(STANDING_LONGEST_TOKENS["H"], STANDING_LONGEST_TOKENS["Q"])
        self.assertEqual(
            STANDING_LONGEST_TOKENS["H"],
            ("072", "450", "052", "551", "003", "600", "003"),
        )
        self.assertEqual(STANDING_LONGEST_N["H"], 7)
        self.assertEqual(STANDING_LONGEST_N["K"], 4)
        self.assertEqual(STANDING_LONGEST_TOKENS["K"], ("260", "001", "004", "711"))
        self.assertEqual(STANDING_LONGEST_N["P"], 6)
        self.assertEqual(
            STANDING_LONGEST_TOKENS["P"],
            ("062", "006", "001", "062", "006", "001"),
        )
        self.assertEqual(STANDING_LONGEST_N["Q"], 7)
        for letter in ZERO_N_TABLETS:
            self.assertEqual(STANDING_LONGEST_N[letter], 0)
            self.assertEqual(STANDING_LONGEST_TOKENS[letter], ())
            self.assertEqual(self.hits[letter], (0,) * len(VENDORED_TABLETS))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leak_table_holds_at_cycle_99_counts(self):
        """Only H/K/P/Q leak, at the hypothesized exact counts."""
        self.assertEqual(HYPOTHESIS_LEAK_COUNTS, STANDING_LEAK_COUNTS)
        self.assertEqual(self.leaks, hypothesized_leaks())
        self.assertEqual(self.inventory_leaks, self.leaks)
        self.assertEqual(self.pairs, STANDING_LEAK_PAIRS)
        self.assertEqual(self.pairs, HYPOTHESIS_LEAK_PAIRS)
        self.assertEqual(self.leaks["H"], {"Q": 2})
        self.assertEqual(self.leaks["K"], {"B": 3, "G": 2})
        self.assertEqual(self.leaks["P"], {"H": 2, "Q": 2})
        self.assertEqual(self.leaks["Q"], {"H": 2})
        for letter in ZERO_OFF_HOME:
            self.assertEqual(self.leaks[letter], {})
            self.assertEqual(self.leak_hits[letter], 0)
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_LEAK_TABLE_HOLDS)
        self.assertEqual(STANDING_CLAIM, "leak_table_holds")
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_tablet_hits_match_locked_table(self):
        """Every representative's A–V counts, including home and zeros."""
        for letter in VENDORED_TABLETS:
            self.assertEqual(self.hits[letter], STANDING_HITS_BY_TABLET[letter])
            self.assertEqual(self.own_hits[letter], STANDING_OWN_HITS[letter])
            self.assertEqual(self.leak_hits[letter], STANDING_LEAK_HITS[letter])
            self.assertEqual(
                self.leaks[letter], STANDING_LEAK_COUNTS.get(letter, {})
            )
            gram = STANDING_LONGEST_TOKENS[letter]
            if STANDING_LONGEST_N[letter] >= PROFILE_MIN_N:
                for other, count in zip(
                    VENDORED_TABLETS, self.hits[letter], strict=True
                ):
                    self.assertEqual(
                        count, ngram_hit_count(self.by_tablet[other], gram)
                    )
            expected_only = tablet_only_flag(
                STANDING_LONGEST_N[letter], STANDING_LEAK_HITS[letter]
            )
            self.assertEqual(
                tablet_only_flag(STANDING_LONGEST_N[letter], self.leak_hits[letter]),
                expected_only,
            )
        self.assertEqual(self.own_hits["H"], 2)
        self.assertEqual(self.hits["H"][VENDORED_TABLETS.index("Q")], 2)
        self.assertEqual(self.own_hits["K"], 2)
        self.assertEqual(self.hits["K"][VENDORED_TABLETS.index("B")], 3)
        self.assertEqual(self.hits["K"][VENDORED_TABLETS.index("G")], 2)
        self.assertEqual(self.own_hits["P"], 2)
        self.assertEqual(self.hits["P"][VENDORED_TABLETS.index("H")], 2)
        self.assertEqual(self.hits["P"][VENDORED_TABLETS.index("Q")], 2)
        self.assertEqual(self.own_hits["Q"], 2)
        self.assertEqual(self.hits["Q"][VENDORED_TABLETS.index("H")], 2)
        self.assertEqual(self.own_hits["I"], 3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_inventory_i_and_w_scoreboards_still_compute(self):
        """Cycle 99 inventory, cycle 103 I-only, and cycle 100 W stay."""
        prior_inv = TestMamariCorpusLongestNInventoryScoreboard()
        prior_inv.setUp()
        prior_inv.test_per_tablet_tokens_and_leak_counts()
        prior_inv.test_survey_matches_computed_lock()
        prior_i = TestMamariSantiagoIaIOnlyScoreboard()
        prior_i.setUp()
        prior_i.test_5gram_is_zero_off_i_and_i_only()
        prior_i.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-104 A–V leak table."""
        lock = self.survey["corpus_max_n_leak_table"]
        self.assertEqual(lock["cycle"], 104)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tablets"]), VENDORED_TABLETS)
        self.assertNotIn("W", lock["tablets"])
        self.assertEqual(lock["hypothesis_from_cycle"], 99)
        self.assertEqual(lock["min_n"], PROFILE_MIN_N)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["leak_table_holds"])
        self.assertEqual(lock["leak_table_holds"], STANDING_LEAK_TABLE_HOLDS)
        self.assertEqual(tuple(lock["leaking_homes"]), LEAKING_HOMES)
        self.assertEqual(tuple(lock["zero_off_home"]), ZERO_OFF_HOME)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leak_pairs"]),
            STANDING_LEAK_PAIRS,
        )
        self.assertEqual(tuple(lock["zero_n_tablets"]), ZERO_N_TABLETS)
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        for letter in VENDORED_TABLETS:
            row = lock["rows"][letter]
            self.assertEqual(row["longest_n"], STANDING_LONGEST_N[letter])
            self.assertEqual(
                tuple(row["longest_tokens"]), STANDING_LONGEST_TOKENS[letter]
            )
            self.assertEqual(row["own_hits"], STANDING_OWN_HITS[letter])
            self.assertEqual(row["leak_hits"], STANDING_LEAK_HITS[letter])
            self.assertEqual(row["leak_counts"], STANDING_LEAK_COUNTS.get(letter, {}))
            self.assertEqual(
                tuple(row["hits_by_tablet"]), STANDING_HITS_BY_TABLET[letter]
            )
            self.assertEqual(
                row["tablet_only"],
                tablet_only_flag(
                    STANDING_LONGEST_N[letter], STANDING_LEAK_HITS[letter]
                ),
            )
            self.assertIsNone(row["island_status"])
        self.assertEqual(lock["rows"]["H"]["leak_counts"], {"Q": 2})
        self.assertEqual(lock["rows"]["K"]["leak_counts"], {"B": 3, "G": 2})
        self.assertEqual(lock["rows"]["P"]["leak_counts"], {"H": 2, "Q": 2})
        self.assertEqual(lock["rows"]["Q"]["leak_counts"], {"H": 2})
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_d_echancree_da_d_only_unchanged"])
        self.assertTrue(lock["standing_v_honolulu_va_v_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertTrue(lock["standing_s_washington_sb2_s_only_unchanged"])
        self.assertTrue(lock["standing_n_vienna_na1_n_only_unchanged"])
        self.assertTrue(lock["standing_m_vienna_ma2_m_only_unchanged"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        inventory = self.survey["corpus_longest_n_inventory"]
        self.assertEqual(inventory["cycle"], 99)
        self.assertTrue(inventory["inventory_holds"])
        self.assertEqual(inventory["rows"]["H"]["leak_counts"], {"Q": 2})
        self.assertEqual(inventory["rows"]["K"]["leak_counts"], {"B": 3, "G": 2})
        self.assertEqual(inventory["rows"]["P"]["leak_counts"], {"H": 2, "Q": 2})
        self.assertEqual(inventory["rows"]["Q"]["leak_counts"], {"H": 2})
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_d_echancree_da_d_only"]["cycle"], 102)
        self.assertTrue(self.survey["tablet_d_echancree_da_d_only"]["d_only"])
        self.assertEqual(self.survey["tablet_v_honolulu_va_v_only"]["cycle"], 101)
        self.assertTrue(self.survey["tablet_v_honolulu_va_v_only"]["v_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCorpusMaxNLeakTableImageSnapshot(unittest.TestCase):
    """Cycle 104 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
