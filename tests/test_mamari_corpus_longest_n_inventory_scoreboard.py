"""A–V corpus longest repeating n-gram inventory.

Cycle 99 text-search lock. A–V Barthel sweep is closed. Uses already-
vendored sides only (r/v or a/b as they exist). Does not vendor a new
tablet. Does not scrape W. Does not change parsers. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune. No
CV. No new agents. Not a meaning dictionary.

Per tablet: longest repeating n-gram (n≥4 freq≥2, else 0). Combined
sides. For each tablet with longest n≥4, whether that exact max
n-gram is tablet-only vs leaks (counts only; no new island status
for n<8). Ev's already-locked local n=6 is checked as a side, not a
23rd tablet.

Claim that can lose: inventory_holds — locked per-tablet longest n
equals the measured value, and every already-locked local length
matches. A length mismatch records both numbers and fails the claim
(no retune).

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_honolulu2_vendor_scoreboard import (
    SIDE_UA,
    load_u_sides,
)
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    SIDE_VA,
    TestMamariHonolulu3VendorScoreboard,
    load_v_sides,
)
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as V_N4_GRAM,
)
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    load_t_sides,
)
from tests.test_mamari_keiti_ev_longest_scoreboard import (
    STANDING_EV_LONGEST_N,
    STANDING_EV_LONGEST_NGRAM,
    TestMamariKeitiEvLongestScoreboard,
    score_ev_longest_repeating,
)
from tests.test_mamari_keiti_vendor_scoreboard import load_e_sides
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_tahua_aa_scoreboard import (
    _TABLET_ROW,
    load_vendored_tablets_html,
)
from tests.test_mamari_washington_sb2_s_only_scoreboard import (
    load_vendored_by_tablet as load_vendored_a_through_s,
)

VENDORED_TABLETS = tuple("ABCDEFGHIJKLMNOPQRSTUV")
W_PAGES = ("Wa.html", "Wb.html", "Wr.html", "Wv.html", "W.html")
FIXTURES_DIR = Path(__file__).parent / "fixtures"
PROFILE_MIN_N = 4

STANDING_SIDES = {
    "A": ("Aa", "Ab"),
    "B": ("Br", "Bv"),
    "C": ("Ca", "Cb"),
    "D": ("Da", "Db"),
    "E": ("Er", "Ev"),
    "F": ("Fa", "Fb"),
    "G": ("Gr", "Gv"),
    "H": ("Hr", "Hv"),
    "I": ("Ia",),
    "J": ("Ja",),
    "K": ("Kr", "Kv"),
    "L": ("La",),
    "M": ("Ma",),
    "N": ("Na", "Nb"),
    "O": ("Oa",),
    "P": ("Pr", "Pv"),
    "Q": ("Qr", "Qv"),
    "R": ("Ra", "Rb"),
    "S": ("Sa", "Sb"),
    "T": ("Ta",),
    "U": ("Ua",),
    "V": ("Va",),
}

STANDING_LONGEST_N = {
    "A": 10,
    "B": 8,
    "C": 13,
    "D": 4,
    "E": 9,
    "F": 0,
    "G": 9,
    "H": 7,
    "I": 5,
    "J": 0,
    "K": 4,
    "L": 0,
    "M": 4,
    "N": 6,
    "O": 0,
    "P": 6,
    "Q": 7,
    "R": 0,
    "S": 7,
    "T": 0,
    "U": 0,
    "V": 4,
}

STANDING_LONGEST_TOKENS = {
    "A": ("080", "004", "280", "182", "048", "022", "025", "025", "009", "005"),
    "B": ("002", "065", "042", "300", "385", "003", "065", "200"),
    "C": (
        "040",
        "040",
        "040",
        "040",
        "040",
        "390",
        "041",
        "378",
        "041",
        "670",
        "008",
        "078",
        "711",
    ),
    "D": ("002", "200", "052", "600"),
    "E": ("300", "040", "300", "028", "004", "430", "022", "380", "203"),
    "F": (),
    "G": ("007", "006", "124", "006", "124", "098", "007", "059", "002"),
    "H": ("072", "450", "052", "551", "003", "600", "003"),
    "I": ("999", "071", "076", "010", "079"),
    "J": (),
    "K": ("260", "001", "004", "711"),
    "L": (),
    "M": ("006", "022", "006", "022"),
    "N": ("004", "064", "034", "006", "004", "064"),
    "O": (),
    "P": ("062", "006", "001", "062", "006", "001"),
    "Q": ("072", "450", "052", "551", "003", "600", "003"),
    "R": (),
    "S": ("004", "660", "081", "004", "660", "081", "004"),
    "T": (),
    "U": (),
    "V": V_N4_GRAM,
}

STANDING_LONGEST_FREQ = {
    letter: (0 if n == 0 else (3 if letter == "I" else 2))
    for letter, n in STANDING_LONGEST_N.items()
}
STANDING_LONGEST_COUNT = {
    "A": 1,
    "B": 1,
    "C": 1,
    "D": 2,
    "E": 1,
    "F": 0,
    "G": 1,
    "H": 1,
    "I": 5,
    "J": 0,
    "K": 5,
    "L": 0,
    "M": 1,
    "N": 1,
    "O": 0,
    "P": 2,
    "Q": 2,
    "R": 0,
    "S": 1,
    "T": 0,
    "U": 0,
    "V": 1,
}
STANDING_OWN_HITS = dict(STANDING_LONGEST_FREQ)
STANDING_LEAK_COUNTS = {
    "H": {"Q": 2},
    "K": {"B": 3, "G": 2},
    "P": {"H": 2, "Q": 2},
    "Q": {"H": 2},
}
STANDING_LEAK_HITS = {
    letter: sum(STANDING_LEAK_COUNTS.get(letter, {}).values())
    for letter in VENDORED_TABLETS
}

PRIOR_LONGEST_N = {
    "M": 4,
    "N": 6,
    "S": 7,
    "E": 9,
    "D": 4,
    "V": 4,
    "F": 0,
    "J": 0,
    "L": 0,
    "O": 0,
    "R": 0,
    "T": 0,
    "U": 0,
}
PRIOR_EV_LONGEST_N = STANDING_EV_LONGEST_N
PRIOR_V_TOKENS = V_N4_GRAM
STANDING_EV_N = STANDING_EV_LONGEST_N
STANDING_EV_TOKENS = STANDING_EV_LONGEST_NGRAM
STANDING_PRIOR_DISAGREEMENTS = ()
STANDING_CLAIM = "inventory_holds"
STANDING_RESULT = "corpus_longest_n_inventory"
STANDING_NEW_TABLET = False
STANDING_W_HTML = False
STANDING_SWEEP_CLOSED = True
STANDING_NEXT_CATALOG = "W"
STANDING_CATALOG_W = ("W", "W/index.html", "Honolulu 4 [#445]")


def load_vendored_a_through_v() -> dict[str, list[list[str]]]:
    """Already-vendored A–V. No W scrape."""
    by_tablet = load_vendored_a_through_s()
    t = load_t_sides()
    u = load_u_sides()
    v = load_v_sides()
    return {
        **by_tablet,
        "T": t[SIDE_TA],
        "U": u[SIDE_UA],
        "V": v[SIDE_VA],
    }


def score_tablet_longest(lines: list[list[str]], analyzer: NgramAnalyzer, letter: str):
    """n≥4 freq≥2 profile on one tablet's combined sides. Search only."""
    names = tuple(f"{letter}{index + 1}" for index in range(len(lines)))
    return score_remainder_repeating_ngrams(lines, analyzer, line_names=names)


def leak_counts(
    gram: tuple[str, ...],
    by_tablet: dict[str, list[list[str]]],
    letter: str,
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> dict[str, int]:
    """Other-tablet hit counts >0. Counts only; not island status."""
    counts: dict[str, int] = {}
    for other in tablets:
        if other == letter:
            continue
        hits = ngram_hit_count(by_tablet[other], gram)
        if hits:
            counts[other] = hits
    return counts


def tablet_only_flag(n: int, leak_hits: int) -> bool | None:
    """True/False when n≥4; None when there is no max n-gram."""
    if n < PROFILE_MIN_N:
        return None
    return leak_hits == 0


def island_status(n: int) -> None:
    """Cycle 99 does not invent island status, including for n<8."""
    _ = n
    return None


def prior_length_disagreements(
    measured_n: dict[str, int],
    priors: dict[str, int] = PRIOR_LONGEST_N,
) -> tuple[tuple[str, int, int], ...]:
    """(tablet, prior, measured) where lengths disagree. Do not retune."""
    return tuple(
        (letter, priors[letter], measured_n[letter])
        for letter in priors
        if measured_n[letter] != priors[letter]
    )


def inventory_holds(
    locked_n: dict[str, int],
    measured_n: dict[str, int],
    disagreements: tuple[tuple[str, int, int], ...],
) -> bool:
    """True iff locked n equals measured n and no prior length clash."""
    return locked_n == measured_n and not disagreements


def vendored_w_html_names(fixtures: Path = FIXTURES_DIR) -> tuple[str, ...]:
    """W Barthel filenames under fixtures, if any."""
    return tuple(name for name in W_PAGES if any(fixtures.glob(f"**/{name}")))


def catalog_w_row(tablets_html: str) -> tuple[str, str, str] | None:
    """W row from already-vendored tablets.html. Does not fetch W."""
    for letter, href, linked_name, _plain in _TABLET_ROW.findall(tablets_html):
        if letter == "W" and href:
            return (letter, href, linked_name)
    return None


class TestCorpusLongestNInventoryHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_prior_mismatch_records_both_numbers_and_fails_claim(self):
        """A length clash fails inventory_holds and keeps both numbers."""
        provider = MockProvider()
        measured = dict(STANDING_LONGEST_N)
        measured["M"] = 5
        clashes = prior_length_disagreements(measured)
        self.assertEqual(clashes, (("M", 4, 5),))
        self.assertFalse(inventory_holds(STANDING_LONGEST_N, measured, clashes))
        self.assertTrue(
            inventory_holds(STANDING_LONGEST_N, dict(STANDING_LONGEST_N), ())
        )
        self.assertEqual(STANDING_CLAIM, "inventory_holds")
        self.assertEqual(provider.get_call_history(), [])

    def test_leak_flag_is_counts_not_island_for_n_lt_8(self):
        """n=7 leak is tablet_only False; island_status stays unset."""
        provider = MockProvider()
        self.assertTrue(tablet_only_flag(7, 0))
        self.assertFalse(tablet_only_flag(7, 2))
        self.assertIsNone(tablet_only_flag(0, 0))
        self.assertIsNone(island_status(7))
        self.assertIsNone(island_status(13))
        gram = ("A", "B", "C", "D")
        planted = {"X": [list(gram)], "Y": []}
        self.assertEqual(leak_counts(gram, planted, "X", ("X", "Y")), {})
        planted["Y"] = [list(gram)]
        self.assertEqual(leak_counts(gram, planted, "X", ("X", "Y")), {"Y": 1})
        self.assertEqual(provider.get_call_history(), [])


class TestMamariCorpusLongestNInventoryScoreboard(unittest.TestCase):
    """Cited-fixture A–V longest-n inventory. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.profiles = {
            letter: score_tablet_longest(self.by_tablet[letter], self.analyzer, letter)
            for letter in VENDORED_TABLETS
        }
        self.measured_n = {
            letter: self.profiles[letter].longest_n for letter in VENDORED_TABLETS
        }
        self.measured_tokens = {
            letter: (
                self.profiles[letter].longest[0].tokens
                if self.profiles[letter].longest
                else ()
            )
            for letter in VENDORED_TABLETS
        }
        self.own_hits = {
            letter: (
                ngram_hit_count(self.by_tablet[letter], self.measured_tokens[letter])
                if self.measured_n[letter] >= PROFILE_MIN_N
                else 0
            )
            for letter in VENDORED_TABLETS
        }
        self.leaks = {
            letter: (
                leak_counts(self.measured_tokens[letter], self.by_tablet, letter)
                if self.measured_n[letter] >= PROFILE_MIN_N
                else {}
            )
            for letter in VENDORED_TABLETS
        }
        self.leak_hits = {
            letter: sum(self.leaks[letter].values()) for letter in VENDORED_TABLETS
        }
        self.e_sides = load_e_sides()
        self.ev_profile = score_ev_longest_repeating(self.e_sides, self.analyzer)
        ev_clash = ()
        if self.ev_profile.longest_n != PRIOR_EV_LONGEST_N:
            ev_clash = (("Ev", PRIOR_EV_LONGEST_N, self.ev_profile.longest_n),)
        self.disagreements = prior_length_disagreements(self.measured_n) + ev_clash
        self.claim_holds = inventory_holds(
            STANDING_LONGEST_N, self.measured_n, self.disagreements
        ) and self.measured_tokens["V"] == PRIOR_V_TOKENS

    def test_sweep_is_a_through_v_without_w(self):
        """Vendored letters are A–V; W is named in the catalog but not vendored."""
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(set(self.by_tablet), set(VENDORED_TABLETS))
        self.assertEqual(vendored_w_html_names(), ())
        self.assertFalse(STANDING_W_HTML)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertTrue(STANDING_SWEEP_CLOSED)
        self.assertEqual(STANDING_NEXT_CATALOG, "W")
        self.assertEqual(
            catalog_w_row(load_vendored_tablets_html()), STANDING_CATALOG_W
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_inventory_holds_and_priors_match(self):
        """Locked n equals measured n; known locals match; claim holds."""
        self.assertEqual(self.measured_n, STANDING_LONGEST_N)
        self.assertEqual(self.disagreements, STANDING_PRIOR_DISAGREEMENTS)
        self.assertEqual(self.disagreements, ())
        for letter, prior in PRIOR_LONGEST_N.items():
            self.assertEqual(self.measured_n[letter], prior)
            self.assertEqual(STANDING_LONGEST_N[letter], prior)
        self.assertEqual(self.ev_profile.longest_n, PRIOR_EV_LONGEST_N)
        self.assertEqual(self.ev_profile.longest[0].tokens, STANDING_EV_TOKENS)
        self.assertEqual(self.measured_tokens["V"], PRIOR_V_TOKENS)
        self.assertEqual(PRIOR_V_TOKENS, ("048", "010", "048", "010"))
        self.assertTrue(self.claim_holds)
        self.assertEqual(STANDING_CLAIM, "inventory_holds")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_tablet_tokens_and_leak_counts(self):
        """Primary max n-gram tokens; tablet-only vs leak counts; no island."""
        for letter in VENDORED_TABLETS:
            profile = self.profiles[letter]
            self.assertEqual(profile.longest_n, STANDING_LONGEST_N[letter])
            self.assertEqual(len(profile.longest), STANDING_LONGEST_COUNT[letter])
            self.assertEqual(self.measured_tokens[letter], STANDING_LONGEST_TOKENS[letter])
            if profile.longest:
                self.assertEqual(profile.longest[0].freq, STANDING_LONGEST_FREQ[letter])
            self.assertEqual(self.own_hits[letter], STANDING_OWN_HITS[letter])
            self.assertEqual(self.leaks[letter], STANDING_LEAK_COUNTS.get(letter, {}))
            self.assertEqual(self.leak_hits[letter], STANDING_LEAK_HITS[letter])
            expected_only = tablet_only_flag(
                STANDING_LONGEST_N[letter], STANDING_LEAK_HITS[letter]
            )
            self.assertEqual(
                tablet_only_flag(self.measured_n[letter], self.leak_hits[letter]),
                expected_only,
            )
            self.assertIsNone(island_status(self.measured_n[letter]))
        self.assertEqual(self.leaks["H"], {"Q": 2})
        self.assertEqual(self.leaks["K"], {"B": 3, "G": 2})
        self.assertEqual(self.leaks["P"], {"H": 2, "Q": 2})
        self.assertEqual(self.leaks["Q"], {"H": 2})
        self.assertTrue(tablet_only_flag(self.measured_n["A"], self.leak_hits["A"]))
        self.assertFalse(tablet_only_flag(self.measured_n["H"], self.leak_hits["H"]))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_v_and_ev_scoreboards_still_compute(self):
        """Cycle 98 V vendor lock and cycle 82 Ev longest stay."""
        prior_v = TestMamariHonolulu3VendorScoreboard()
        prior_v.setUp()
        prior_v.test_longest_repeating_ngram_is_4()
        prior_v.test_survey_matches_computed_lock()
        prior_ev = TestMamariKeitiEvLongestScoreboard()
        prior_ev.setUp()
        prior_ev.test_ev_longest_is_n6_and_has_no_n_ge_8()
        prior_ev.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-99 A–V inventory."""
        lock = self.survey["corpus_longest_n_inventory"]
        self.assertEqual(lock["cycle"], 99)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tablets"]), VENDORED_TABLETS)
        self.assertNotIn("W", lock["tablets"])
        self.assertTrue(lock["sweep_closed"])
        self.assertEqual(lock["next_catalog"], STANDING_NEXT_CATALOG)
        self.assertEqual(tuple(lock["catalog_w"]), STANDING_CATALOG_W)
        self.assertFalse(lock["w_html"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["inventory_holds"])
        self.assertEqual(lock["prior_disagreements"], [])
        self.assertEqual(lock["ev_longest_n"], STANDING_EV_N)
        self.assertEqual(tuple(lock["ev_longest_tokens"]), STANDING_EV_TOKENS)
        for letter in VENDORED_TABLETS:
            row = lock["rows"][letter]
            self.assertEqual(tuple(row["sides"]), STANDING_SIDES[letter])
            self.assertEqual(row["longest_n"], STANDING_LONGEST_N[letter])
            self.assertEqual(tuple(row["longest_tokens"]), STANDING_LONGEST_TOKENS[letter])
            self.assertEqual(row["longest_freq"], STANDING_LONGEST_FREQ[letter])
            self.assertEqual(row["longest_count"], STANDING_LONGEST_COUNT[letter])
            self.assertEqual(row["own_hits"], STANDING_OWN_HITS[letter])
            self.assertEqual(row["leak_hits"], STANDING_LEAK_HITS[letter])
            self.assertEqual(row["leak_counts"], STANDING_LEAK_COUNTS.get(letter, {}))
            self.assertEqual(
                row["tablet_only"],
                tablet_only_flag(STANDING_LONGEST_N[letter], STANDING_LEAK_HITS[letter]),
            )
            self.assertIsNone(row["island_status"])
        self.assertEqual(lock["prior_longest_n"]["M"], 4)
        self.assertEqual(lock["prior_longest_n"]["N"], 6)
        self.assertEqual(lock["prior_longest_n"]["S"], 7)
        self.assertEqual(lock["prior_longest_n"]["E"], 9)
        self.assertEqual(lock["prior_longest_n"]["Ev"], 6)
        self.assertEqual(lock["prior_longest_n"]["D"], 4)
        self.assertEqual(lock["prior_longest_n"]["V"], 4)
        self.assertEqual(tuple(lock["v_tokens"]), PRIOR_V_TOKENS)
        self.assertTrue(lock["standing_v_honolulu_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_ev_longest_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_v_honolulu_vendor"]["cycle"], 98)
        self.assertEqual(self.survey["tablet_e_keiti_ev_longest"]["cycle"], 82)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCorpusLongestNInventoryImageSnapshot(unittest.TestCase):
    """Cycle 99 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
