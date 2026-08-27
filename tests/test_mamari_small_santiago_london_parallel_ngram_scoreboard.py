"""Small Santiago / London parallel: longest shared stem n-gram.

Cycle 61 text-search lock. Uses already-vendored Gr.html, Gv.html,
Kr.html, Kv.html and the existing parsers. Does not scrape a new
tablet. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. Not another 076 rate
table.

Published claim: G (Small Santiago) and K (London) are parallel
texts (Barthel / Pozdniakov / Horley). Cycle 55–60 showed 076
density on Gv only and zero 076 on K, so 076 is not the parallel.
This cycle locks the longest exact shared stem n-gram.

G is Gr+Gv line lists from the existing parsers; K is Kr+Kv.
N-grams stay per-line (same as extract_ngrams / find_ngram_hits).
Also lock the four per-side pairs. The claim holds on this
stemming iff the combined longest shared n ≥ 4.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
from dataclasses import dataclass
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_second_passage_scoreboard import (
    find_ngram_hits,
    load_corpus_survey,
)
from tests.test_mamari_small_london_kr_scoreboard import (
    extract_kr_published_tokens,
    kr_line_stems,
    load_vendored_kr_html,
)
from tests.test_mamari_small_london_kv_scoreboard import (
    TestMamariSmallLondonKvScoreboard,
    extract_kv_published_tokens,
    kv_line_stems,
    load_vendored_kv_html,
)
from tests.test_mamari_small_santiago_gr_scoreboard import (
    extract_gr_published_tokens,
    gr_line_stems,
    load_vendored_gr_html,
)
from tests.test_mamari_small_santiago_gv_scoreboard import (
    extract_gv_published_tokens,
    gv_line_stems,
    load_vendored_gv_html,
)

CLAIM_MIN_N = 4
SIDE_GR = "Gr"
SIDE_GV = "Gv"
SIDE_KR = "Kr"
SIDE_KV = "Kv"
G_SIDES = (SIDE_GR, SIDE_GV)
K_SIDES = (SIDE_KR, SIDE_KV)
SIDE_PAIRS = (
    (SIDE_GR, SIDE_KR),
    (SIDE_GR, SIDE_KV),
    (SIDE_GV, SIDE_KR),
    (SIDE_GV, SIDE_KV),
)

STANDING_COMBINED_N = 17
STANDING_COMBINED_TOKENS = (
    "380",
    "001",
    "003",
    "005",
    "006",
    "010",
    "380",
    "001",
    "003",
    "315",
    "380",
    "001",
    "003",
    "090",
    "001",
    "380",
    "001",
)
STANDING_COMBINED_FREQ_G = 1
STANDING_COMBINED_FREQ_K = 1
STANDING_COMBINED_SHARED_N_GE_4 = True
STANDING_CLAIM_HOLDS = True
STANDING_STEM_076_IN_LONGEST = False

STANDING_GR_KR_N = 17
STANDING_GR_KR_TOKENS = STANDING_COMBINED_TOKENS
STANDING_GR_KR_FREQ = (1, 1)
STANDING_GR_KV_N = 15
STANDING_GR_KV_TOKENS = (
    "079",
    "450",
    "019",
    "069",
    "380",
    "001",
    "003",
    "162",
    "522",
    "050",
    "002",
    "450",
    "380",
    "001",
    "003",
)
STANDING_GR_KV_FREQ = (1, 1)
STANDING_GV_KR_N = 2
STANDING_GV_KR_TOKENS = ("006", "700")
STANDING_GV_KR_FREQ = (2, 1)
STANDING_GV_KV_N = 2
STANDING_GV_KV_TOKENS = ("001", "001")
STANDING_GV_KV_FREQ = (1, 1)

# (g_side, k_side, n, tokens, freq_g, freq_k, shared_n_ge_4)
STANDING_PER_SIDE = (
    (SIDE_GR, SIDE_KR, STANDING_GR_KR_N, STANDING_GR_KR_TOKENS, *STANDING_GR_KR_FREQ, True),
    (SIDE_GR, SIDE_KV, STANDING_GR_KV_N, STANDING_GR_KV_TOKENS, *STANDING_GR_KV_FREQ, True),
    (SIDE_GV, SIDE_KR, STANDING_GV_KR_N, STANDING_GV_KR_TOKENS, *STANDING_GV_KR_FREQ, False),
    (SIDE_GV, SIDE_KV, STANDING_GV_KV_N, STANDING_GV_KV_TOKENS, *STANDING_GV_KV_FREQ, False),
)
STANDING_NEW_TABLET = False
STANDING_RESULT = "gk_parallel_shared_ngram"


@dataclass(frozen=True)
class SharedNgram:
    """Longest exact shared stem n-gram. Ids only; no meanings."""

    n: int
    tokens: tuple[str, ...]
    freq_left: int
    freq_right: int
    shared_n_ge_4: bool

    @property
    def claim_holds(self) -> bool:
        """True iff the parallel survives this Barthel stemming."""
        return self.n >= CLAIM_MIN_N


def load_g_k_sides() -> dict[str, list[list[str]]]:
    """Gr / Gv / Kr / Kv stems from the existing parsers. No new scrape."""
    return {
        SIDE_GR: gr_line_stems(extract_gr_published_tokens(load_vendored_gr_html())),
        SIDE_GV: gv_line_stems(extract_gv_published_tokens(load_vendored_gv_html())),
        SIDE_KR: kr_line_stems(extract_kr_published_tokens(load_vendored_kr_html())),
        SIDE_KV: kv_line_stems(extract_kv_published_tokens(load_vendored_kv_html())),
    }


def concat_sides(
    by_side: dict[str, list[list[str]]],
    names: tuple[str, ...],
) -> list[list[str]]:
    """Join already-parsed line lists. Does not flatten across lines."""
    lines: list[list[str]] = []
    for name in names:
        lines.extend(by_side[name])
    return lines


def ngram_frequencies(lines: list[list[str]], n: int) -> Counter[tuple[str, ...]]:
    """Per-line n-gram counts. Same windows as find_ngram_hits."""
    counts: Counter[tuple[str, ...]] = Counter()
    for sequence in lines:
        if len(sequence) < n:
            continue
        for start in range(len(sequence) - n + 1):
            counts[tuple(sequence[start : start + n])] += 1
    return counts


def longest_shared_ngram(
    left: list[list[str]],
    right: list[list[str]],
) -> SharedNgram:
    """Longest exact shared stem n-gram. Ties: higher freqs, then lex."""
    max_n = min(
        max((len(sequence) for sequence in left), default=0),
        max((len(sequence) for sequence in right), default=0),
    )
    for n in range(max_n, 0, -1):
        left_counts = ngram_frequencies(left, n)
        right_counts = ngram_frequencies(right, n)
        common = set(left_counts) & set(right_counts)
        if not common:
            continue
        tokens = min(
            common,
            key=lambda gram: (-left_counts[gram], -right_counts[gram], gram),
        )
        return SharedNgram(
            n=n,
            tokens=tokens,
            freq_left=left_counts[tokens],
            freq_right=right_counts[tokens],
            shared_n_ge_4=n >= CLAIM_MIN_N,
        )
    return SharedNgram(
        n=0,
        tokens=(),
        freq_left=0,
        freq_right=0,
        shared_n_ge_4=False,
    )


def score_g_k_parallel(
    by_side: dict[str, list[list[str]]],
) -> tuple[SharedNgram, tuple[tuple, ...]]:
    """Combined G vs K lock plus the four per-side rows."""
    combined = longest_shared_ngram(
        concat_sides(by_side, G_SIDES),
        concat_sides(by_side, K_SIDES),
    )
    per_side = tuple(
        (
            g_side,
            k_side,
            row.n,
            row.tokens,
            row.freq_left,
            row.freq_right,
            row.shared_n_ge_4,
        )
        for g_side, k_side in SIDE_PAIRS
        for row in (longest_shared_ngram(by_side[g_side], by_side[k_side]),)
    )
    return combined, per_side


class TestSmallSantiagoLondonParallelHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_longest_shared_and_claim_threshold(self):
        """n≥4 holds; n<4 loses; missing share is n=0; ties prefer freq then lex."""
        provider = MockProvider()
        left = [["001", "002", "003", "004", "005"], ["006", "007"]]
        right = [["009", "001", "002", "003", "004", "005"], ["006", "007"]]
        hit = longest_shared_ngram(left, right)
        self.assertEqual(hit.n, 5)
        self.assertEqual(hit.tokens, ("001", "002", "003", "004", "005"))
        self.assertEqual((hit.freq_left, hit.freq_right), (1, 1))
        self.assertTrue(hit.shared_n_ge_4)
        self.assertTrue(hit.claim_holds)
        self.assertEqual(len(find_ngram_hits(left, hit.tokens)), 1)

        short = longest_shared_ngram([["010", "011", "012"]], [["010", "011", "099"]])
        self.assertEqual(short.n, 2)
        self.assertEqual(short.tokens, ("010", "011"))
        self.assertFalse(short.shared_n_ge_4)
        self.assertFalse(short.claim_holds)
        self.assertLess(short.n, CLAIM_MIN_N)

        empty = longest_shared_ngram([["010"]], [["011"]])
        self.assertEqual(empty, SharedNgram(0, (), 0, 0, False))
        self.assertFalse(empty.claim_holds)

        tied = longest_shared_ngram(
            [["020", "021"], ["020", "021"], ["022", "023"]],
            [["020", "021"], ["022", "023"]],
        )
        self.assertEqual(tied.n, 2)
        self.assertEqual(tied.tokens, ("020", "021"))
        self.assertEqual((tied.freq_left, tied.freq_right), (2, 1))
        self.assertEqual(provider.get_call_history(), [])

    def test_concat_sides_keeps_line_lists(self):
        """G/K concat is Gr+Gv / Kr+Kv lines, not a flattened stream."""
        provider = MockProvider()
        by_side = {
            SIDE_GR: [["380", "001"]],
            SIDE_GV: [["076", "200"]],
            SIDE_KR: [["380", "001"]],
            SIDE_KV: [["004"]],
        }
        self.assertEqual(concat_sides(by_side, G_SIDES), [["380", "001"], ["076", "200"]])
        self.assertEqual(concat_sides(by_side, K_SIDES), [["380", "001"], ["004"]])
        combined, per_side = score_g_k_parallel(by_side)
        self.assertEqual(combined.n, 2)
        self.assertEqual(combined.tokens, ("380", "001"))
        self.assertFalse(combined.shared_n_ge_4)
        self.assertFalse(combined.claim_holds)
        self.assertEqual(per_side[0][:3], (SIDE_GR, SIDE_KR, 2))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonParallelNgramScoreboard(unittest.TestCase):
    """Cited Gr+Gv vs Kr+Kv longest shared n-gram lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_g_k_sides()
        self.combined, self.per_side = score_g_k_parallel(self.by_side)

    def test_combined_longest_shared_ngram_and_claim(self):
        """G vs K longest n=17, freq 1/1; shared n≥4 exists; claim holds."""
        self.assertEqual(self.combined.n, STANDING_COMBINED_N)
        self.assertEqual(self.combined.tokens, STANDING_COMBINED_TOKENS)
        self.assertEqual(self.combined.freq_left, STANDING_COMBINED_FREQ_G)
        self.assertEqual(self.combined.freq_right, STANDING_COMBINED_FREQ_K)
        self.assertEqual(self.combined.shared_n_ge_4, STANDING_COMBINED_SHARED_N_GE_4)
        self.assertEqual(self.combined.claim_holds, STANDING_CLAIM_HOLDS)
        self.assertGreaterEqual(self.combined.n, CLAIM_MIN_N)
        self.assertTrue(STANDING_CLAIM_HOLDS)
        self.assertTrue(STANDING_COMBINED_SHARED_N_GE_4)
        self.assertEqual(len(self.combined.tokens), STANDING_COMBINED_N)
        self.assertEqual(
            "076" in self.combined.tokens,
            STANDING_STEM_076_IN_LONGEST,
        )
        self.assertFalse(STANDING_STEM_076_IN_LONGEST)
        g_lines = concat_sides(self.by_side, G_SIDES)
        k_lines = concat_sides(self.by_side, K_SIDES)
        self.assertEqual(len(find_ngram_hits(g_lines, self.combined.tokens)), 1)
        self.assertEqual(len(find_ngram_hits(k_lines, self.combined.tokens)), 1)
        self.assertEqual(sum(len(line) for line in g_lines), 714)
        self.assertEqual(sum(len(line) for line in k_lines), 226)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_per_side_longest_shared_ngrams(self):
        """Gr↔Kr n=17; Gr↔Kv n=15; Gv↔K n=2 (no shared n≥4)."""
        self.assertEqual(self.per_side, STANDING_PER_SIDE)
        self.assertEqual(len(self.per_side), len(SIDE_PAIRS))
        for row, locked in zip(self.per_side, STANDING_PER_SIDE):
            g_side, k_side, n, tokens, freq_g, freq_k, ge4 = locked
            scored = longest_shared_ngram(self.by_side[g_side], self.by_side[k_side])
            self.assertEqual(row, locked)
            self.assertEqual(scored.n, n)
            self.assertEqual(scored.tokens, tokens)
            self.assertEqual((scored.freq_left, scored.freq_right), (freq_g, freq_k))
            self.assertEqual(scored.shared_n_ge_4, ge4)
            self.assertEqual(scored.shared_n_ge_4, n >= CLAIM_MIN_N)
            self.assertEqual(len(find_ngram_hits(self.by_side[g_side], tokens)), freq_g)
            self.assertEqual(len(find_ngram_hits(self.by_side[k_side], tokens)), freq_k)
        self.assertEqual(self.per_side[0][3], STANDING_COMBINED_TOKENS)
        self.assertFalse(self.per_side[2][6])
        self.assertFalse(self.per_side[3][6])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_kv_scoreboard_still_computes(self):
        """Cycle 60 Kv vendor and prior G/K scoreboards stay."""
        prior = TestMamariSmallLondonKvScoreboard()
        prior.setUp()
        prior.test_stem_count_motifs_076_rate_and_locked_ngrams()
        prior.test_existing_kr_scoreboard_still_computes()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-61 G/K parallel n-gram lock."""
        lock = self.survey["tablet_g_k_parallel_shared_ngram"]
        self.assertEqual(lock["cycle"], 61)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["claim"], "g_k_parallel_texts")
        self.assertEqual(lock["g_sides"], list(G_SIDES))
        self.assertEqual(lock["k_sides"], list(K_SIDES))
        self.assertEqual(lock["min_n"], CLAIM_MIN_N)
        self.assertEqual(lock["combined_n"], STANDING_COMBINED_N)
        self.assertEqual(tuple(lock["combined_tokens"]), STANDING_COMBINED_TOKENS)
        self.assertEqual(lock["combined_freq_g"], STANDING_COMBINED_FREQ_G)
        self.assertEqual(lock["combined_freq_k"], STANDING_COMBINED_FREQ_K)
        self.assertEqual(lock["combined_shared_n_ge_4"], STANDING_COMBINED_SHARED_N_GE_4)
        self.assertEqual(lock["claim_holds"], STANDING_CLAIM_HOLDS)
        self.assertFalse(lock["stem_076_in_longest"])
        self.assertFalse(lock["new_tablet"])
        locked_sides = tuple(
            (
                g_side,
                k_side,
                n,
                tuple(tokens),
                freq_g,
                freq_k,
                ge4,
            )
            for g_side, k_side, n, tokens, freq_g, freq_k, ge4 in lock["per_side"]
        )
        self.assertEqual(locked_sides, STANDING_PER_SIDE)
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
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_k_small_london_verso_kv"]["cycle"], 60)
        self.assertEqual(self.survey["tablet_k_small_london_recto"]["cycle"], 59)
        self.assertEqual(self.survey["tablet_g_small_santiago_verso_gv"]["cycle"], 56)
        self.assertEqual(self.survey["tablet_g_small_santiago_recto_gr"]["cycle"], 55)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonParallelImageSnapshot(unittest.TestCase):
    """Cycle 61 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
