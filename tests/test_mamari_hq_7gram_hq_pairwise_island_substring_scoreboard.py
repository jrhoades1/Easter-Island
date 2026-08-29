"""H/Q's cycle-99/104/108 representative 7-gram vs locked H∩Q n≥8 islands.

Cycle 109 text-search lock. Uses already-vendored A–V, the
cycle-99/104/108 H and Q representative, and the cycle-70
fifteen maximal Q–H pairwise islands. Does not vendor a new
tablet. Does not scrape X. W has no Barthel (cycle 100); skip W.
Does not redo H–Q pairwise n≥8 or H∩P∩Q triple inventories.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Locks whether 072 450 052 551 003 600 003 is an exact contiguous
substring of a locked H–Q pairwise n≥8 island (the H∩Q set, not
the cycle-71 H∩P∩Q triple). Independently measures the longest
contiguous H∩Q n-gram that contains that 7-gram and occurs on
both H and Q, plus P's hit count of that maximal. Claim that
can lose: hq_7gram_is_hq_pairwise_island_substring.

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
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_hq_max_n_hpq_island_substring_scoreboard import (
    GRAM7,
    STANDING_H_HITS,
    STANDING_H_SITES,
    STANDING_HITS_BY_TABLET,
    STANDING_HQ_MAX_N_IS_HPQ_ISLAND_SUBSTRING,
    STANDING_P_HITS,
    STANDING_P_SITES,
    STANDING_Q_HITS,
    STANDING_Q_SITES,
    TestMamariHqMaxNHpqIslandSubstringScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
    substring_offsets,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
    P_SIDES,
    SIDE_HR,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    concat_sides,
    ngram_frequencies,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    LINE_NAMES,
    STANDING_QH_MAXIMAL_COUNT,
    STANDING_QH_MAXIMALS,
    TestMamariSmallStPetersburgSharedN8Scoreboard,
    named_qhp_hits,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides as load_h_p_q_sides,
)
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    Q_SIDES,
    SIDE_QR,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

LOCKED_PAIRWISE_ISLANDS = tuple(
    tokens for tokens, _n, _fq, _fh, _qs, _hs in STANDING_QH_MAXIMALS
)
STANDING_ISLAND_31_TOKENS = STANDING_QH_MAXIMALS[0][0]
STANDING_ISLAND_31_N = STANDING_QH_MAXIMALS[0][1]
STANDING_ISLAND_31_Q_SITE = STANDING_QH_MAXIMALS[0][4]
STANDING_ISLAND_31_H_SITE = STANDING_QH_MAXIMALS[0][5]
STANDING_ISLAND_31_OFFSETS = (24,)
STANDING_ISLAND_11_TOKENS = STANDING_QH_MAXIMALS[8][0]
STANDING_ISLAND_11_N = STANDING_QH_MAXIMALS[8][1]
STANDING_ISLAND_11_Q_SITE = STANDING_QH_MAXIMALS[8][4]
STANDING_ISLAND_11_H_SITE = STANDING_QH_MAXIMALS[8][5]
STANDING_ISLAND_11_OFFSETS = (1,)
STANDING_MATCHING_ISLANDS = (
    (
        STANDING_ISLAND_31_TOKENS,
        STANDING_ISLAND_31_N,
        STANDING_ISLAND_31_H_SITE,
        STANDING_ISLAND_31_Q_SITE,
        STANDING_ISLAND_31_OFFSETS,
    ),
    (
        STANDING_ISLAND_11_TOKENS,
        STANDING_ISLAND_11_N,
        STANDING_ISLAND_11_H_SITE,
        STANDING_ISLAND_11_Q_SITE,
        STANDING_ISLAND_11_OFFSETS,
    ),
)
STANDING_MATCHING_ISLAND_COUNT = 2
STANDING_HQ_7GRAM_IS_HQ_PAIRWISE_ISLAND_SUBSTRING = True
STANDING_MAXIMAL_TOKENS = STANDING_ISLAND_31_TOKENS
STANDING_MAXIMAL_N = STANDING_ISLAND_31_N
STANDING_MAXIMAL_H_SITES = (STANDING_ISLAND_31_H_SITE,)
STANDING_MAXIMAL_Q_SITES = (STANDING_ISLAND_31_Q_SITE,)
STANDING_MAXIMAL_P_SITES = ()
STANDING_MAXIMAL_H_HITS = 1
STANDING_MAXIMAL_Q_HITS = 1
STANDING_MAXIMAL_P_HITS = 0
STANDING_MAXIMAL_HITS_BY_TABLET = (
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
)
STANDING_CLAIM = "hq_7gram_is_hq_pairwise_island_substring"
STANDING_RESULT = "hq_7gram_hq_pairwise_island_substring"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False


def matching_pairwise_islands(
    gram: tuple[str, ...] = GRAM7,
    maximals: tuple = STANDING_QH_MAXIMALS,
) -> tuple[tuple, ...]:
    """Locked H–Q pairwise islands whose tokens contain gram as a run."""
    rows = []
    for tokens, n, _freq_q, _freq_h, q_site, h_site in maximals:
        offsets = substring_offsets(gram, tokens)
        if offsets:
            rows.append((tokens, n, h_site, q_site, offsets))
    return tuple(rows)


def hq_7gram_is_hq_pairwise_island_substring(
    gram: tuple[str, ...] = GRAM7,
    maximals: tuple = STANDING_QH_MAXIMALS,
) -> bool:
    """True iff the H/Q 7-gram sits inside at least one locked H∩Q island."""
    return bool(matching_pairwise_islands(gram, maximals))


def line_at(
    by_side: dict[str, list[list[str]]],
    site: tuple[str, str, int],
) -> list[str]:
    """Named line stems for a locked (side, line, index) site."""
    side, line, _index = site
    return by_side[side][LINE_NAMES[side].index(line)]


def extend_aligned_sites(
    h_seq: list[str],
    h_index: int,
    q_seq: list[str],
    q_index: int,
    n: int,
) -> tuple[str, ...]:
    """Grow a shared window left/right from one aligned H/Q 7-gram pair."""
    left = 0
    while h_index - left - 1 >= 0 and q_index - left - 1 >= 0:
        if h_seq[h_index - left - 1] != q_seq[q_index - left - 1]:
            break
        left += 1
    right = 0
    while h_index + n + right < len(h_seq) and q_index + n + right < len(q_seq):
        if h_seq[h_index + n + right] != q_seq[q_index + n + right]:
            break
        right += 1
    return tuple(h_seq[h_index - left : h_index + n + right])


def longest_hq_extension(
    gram: tuple[str, ...] = GRAM7,
    by_side: dict[str, list[list[str]]] | None = None,
    h_sites: tuple[tuple[str, str, int], ...] | None = None,
    q_sites: tuple[tuple[str, str, int], ...] | None = None,
) -> tuple[tuple[str, ...], int]:
    """Longest exact H∩Q n-gram that contains gram. Search only."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    if h_sites is None:
        h_sites = named_qhp_hits(by_side, H_SIDES, gram)
    if q_sites is None:
        q_sites = named_qhp_hits(by_side, Q_SIDES, gram)
    best: tuple[str, ...] = ()
    for h_site in h_sites:
        h_seq = line_at(by_side, h_site)
        for q_site in q_sites:
            q_seq = line_at(by_side, q_site)
            tokens = extend_aligned_sites(
                h_seq, h_site[2], q_seq, q_site[2], len(gram)
            )
            if len(tokens) > len(best) or (len(tokens) == len(best) and tokens < best):
                best = tokens
    return (best, len(best))


def longest_shared_containing(
    gram: tuple[str, ...] = GRAM7,
    by_side: dict[str, list[list[str]]] | None = None,
) -> tuple[tuple[str, ...], int]:
    """Same maximal via shared n-gram frequencies, not site pairing."""
    if by_side is None:
        by_side = load_h_p_q_sides()
    h_lines = concat_sides(by_side, H_SIDES)
    q_lines = concat_sides(by_side, Q_SIDES)
    max_n = min(
        max((len(sequence) for sequence in h_lines), default=0),
        max((len(sequence) for sequence in q_lines), default=0),
    )
    for n in range(max_n, len(gram) - 1, -1):
        shared = set(ngram_frequencies(h_lines, n)) & set(ngram_frequencies(q_lines, n))
        hits = [tokens for tokens in shared if is_contiguous_substring(gram, tokens)]
        if hits:
            tokens = min(hits)
            return (tokens, n)
    return ((), 0)


class TestHq7gramHqPairwiseIslandSubstringHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_substring_requires_contiguous_tokens(self):
        """A gap is not a substring; a planted pairwise run that contains it is."""
        provider = MockProvider()
        self.assertEqual(GRAM7, ("072", "450", "052", "551", "003", "600", "003"))
        planted = ("381",) + GRAM7 + ("385", "003", "670")
        self.assertTrue(is_contiguous_substring(GRAM7, planted))
        self.assertEqual(substring_offsets(GRAM7, planted), (1,))
        gapped = GRAM7[:3] + ("999",) + GRAM7[3:]
        self.assertFalse(is_contiguous_substring(GRAM7, gapped))
        self.assertEqual(substring_offsets(GRAM7, GRAM7[:6]), ())
        self.assertTrue(is_contiguous_substring(GRAM7, GRAM7))
        self.assertEqual(provider.get_call_history(), [])

    def test_matching_pairwise_islands_are_exact_locked_rows(self):
        """Locked pairwise islands hit; a miss-only inventory does not."""
        provider = MockProvider()
        planted_hit = (
            ("381",) + GRAM7 + ("385", "003", "670"),
            11,
            1,
            1,
            (SIDE_QR, "Qr3", 51),
            (SIDE_HR, "Hr3", 71),
        )
        planted_miss = STANDING_QH_MAXIMALS[1]
        planted = (planted_hit, planted_miss)
        self.assertEqual(
            matching_pairwise_islands(GRAM7, planted),
            (
                (
                    planted_hit[0],
                    11,
                    (SIDE_HR, "Hr3", 71),
                    (SIDE_QR, "Qr3", 51),
                    (1,),
                ),
            ),
        )
        self.assertTrue(hq_7gram_is_hq_pairwise_island_substring(GRAM7, planted))
        self.assertFalse(hq_7gram_is_hq_pairwise_island_substring(GRAM7, (planted_miss,)))
        self.assertEqual(
            matching_pairwise_islands(GRAM7, STANDING_QH_MAXIMALS),
            STANDING_MATCHING_ISLANDS,
        )
        self.assertTrue(hq_7gram_is_hq_pairwise_island_substring(GRAM7, STANDING_QH_MAXIMALS))
        self.assertEqual(STANDING_CLAIM, "hq_7gram_is_hq_pairwise_island_substring")
        self.assertTrue(STANDING_HQ_7GRAM_IS_HQ_PAIRWISE_ISLAND_SUBSTRING)
        self.assertEqual(provider.get_call_history(), [])

    def test_extension_grows_only_while_h_and_q_match(self):
        """Synthetic H/Q lines grow to a shared prefix+suffix; a mismatch stops."""
        provider = MockProvider()
        by_side = load_h_p_q_sides()
        planted_h = ("111", "222") + GRAM7 + ("333",)
        planted_q = ("111", "222") + GRAM7 + ("333",)
        by_side[SIDE_HR] = [list(planted_h)]
        by_side[SIDE_QR] = [list(planted_q)]
        h_sites = ((SIDE_HR, LINE_NAMES[SIDE_HR][0], 2),)
        q_sites = ((SIDE_QR, LINE_NAMES[SIDE_QR][0], 2),)
        tokens, n = longest_hq_extension(GRAM7, by_side, h_sites, q_sites)
        self.assertEqual(tokens, planted_h)
        self.assertEqual(n, 10)
        by_side[SIDE_QR] = [["000", "222", *GRAM7, "999"]]
        tokens, n = longest_hq_extension(GRAM7, by_side, h_sites, q_sites)
        self.assertEqual(tokens, ("222",) + GRAM7)
        self.assertEqual(n, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHq7gramHqPairwiseIslandSubstringScoreboard(unittest.TestCase):
    """Cited-fixture H/Q 7-gram vs H–Q pairwise islands. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.hpq_sides = load_h_p_q_sides()
        self.h_sites = named_qhp_hits(self.hpq_sides, H_SIDES, GRAM7)
        self.q_sites = named_qhp_hits(self.hpq_sides, Q_SIDES, GRAM7)
        self.p_sites = named_qhp_hits(self.hpq_sides, P_SIDES, GRAM7)
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM7, VENDORED_TABLETS)
        self.matches = matching_pairwise_islands(GRAM7)
        self.claim_holds = hq_7gram_is_hq_pairwise_island_substring(GRAM7)
        self.maximal_tokens, self.maximal_n = longest_hq_extension(
            GRAM7, self.hpq_sides, tuple(self.h_sites), tuple(self.q_sites)
        )
        self.freq_tokens, self.freq_n = longest_shared_containing(GRAM7, self.hpq_sides)
        self.maximal_h_sites = named_qhp_hits(
            self.hpq_sides, H_SIDES, self.maximal_tokens
        )
        self.maximal_q_sites = named_qhp_hits(
            self.hpq_sides, Q_SIDES, self.maximal_tokens
        )
        self.maximal_p_sites = named_qhp_hits(
            self.hpq_sides, P_SIDES, self.maximal_tokens
        )
        self.maximal_hits_by_tablet = tablet_hit_counts(
            self.by_tablet, self.maximal_tokens, VENDORED_TABLETS
        )

    def test_tokens_are_cycle_99_h_and_q_representative(self):
        """7-gram is the cycle-99/104/108 H and Q representative. None invented."""
        self.assertEqual(GRAM7, INVENTORY_LONGEST_TOKENS["H"])
        self.assertEqual(GRAM7, INVENTORY_LONGEST_TOKENS["Q"])
        self.assertEqual(GRAM7, ("072", "450", "052", "551", "003", "600", "003"))
        self.assertEqual(INVENTORY_LONGEST_N["H"], 7)
        self.assertEqual(INVENTORY_LONGEST_N["Q"], 7)
        self.assertEqual(len(GRAM7), 7)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["H"]["longest_tokens"]),
            GRAM7,
        )
        self.assertEqual(
            tuple(self.survey["hq_max_n_hpq_island_substring"]["tokens7"]),
            GRAM7,
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_cycle_108_sites_and_triple_miss_stay(self):
        """H=2, Q=2, P=0 at the cycle-108 addresses. Triple islands still miss."""
        self.assertEqual(tuple(self.h_sites), STANDING_H_SITES)
        self.assertEqual(tuple(self.q_sites), STANDING_Q_SITES)
        self.assertEqual(tuple(self.p_sites), STANDING_P_SITES)
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("H")], STANDING_H_HITS)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("Q")], STANDING_Q_HITS)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("P")], STANDING_P_HITS)
        self.assertFalse(STANDING_HQ_MAX_N_IS_HPQ_ISLAND_SUBSTRING)
        self.assertFalse(self.survey["hq_max_n_hpq_island_substring"]["hq_max_n_is_hpq_island_substring"])
        self.assertEqual(self.survey["hq_max_n_hpq_island_substring"]["cycle"], 108)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_7gram_is_substring_of_two_locked_hq_pairwise_islands(self):
        """Boolean is true; cycle-70 n=31 and n=11 islands contain it."""
        self.assertEqual(len(LOCKED_PAIRWISE_ISLANDS), STANDING_QH_MAXIMAL_COUNT)
        self.assertEqual(STANDING_QH_MAXIMAL_COUNT, 15)
        self.assertEqual(STANDING_QH_MAXIMALS[0][1], 31)
        self.assertEqual(self.matches, STANDING_MATCHING_ISLANDS)
        self.assertEqual(len(self.matches), STANDING_MATCHING_ISLAND_COUNT)
        self.assertEqual(STANDING_MATCHING_ISLAND_COUNT, 2)
        tokens_31, n_31, h_31, q_31, off_31 = self.matches[0]
        tokens_11, n_11, h_11, q_11, off_11 = self.matches[1]
        self.assertEqual(tokens_31, STANDING_ISLAND_31_TOKENS)
        self.assertEqual(n_31, STANDING_ISLAND_31_N)
        self.assertEqual(h_31, STANDING_ISLAND_31_H_SITE)
        self.assertEqual(q_31, STANDING_ISLAND_31_Q_SITE)
        self.assertEqual(off_31, STANDING_ISLAND_31_OFFSETS)
        self.assertEqual(tokens_11, STANDING_ISLAND_11_TOKENS)
        self.assertEqual(n_11, STANDING_ISLAND_11_N)
        self.assertEqual(h_11, STANDING_ISLAND_11_H_SITE)
        self.assertEqual(q_11, STANDING_ISLAND_11_Q_SITE)
        self.assertEqual(off_11, STANDING_ISLAND_11_OFFSETS)
        self.assertTrue(is_contiguous_substring(GRAM7, STANDING_ISLAND_31_TOKENS))
        self.assertTrue(is_contiguous_substring(GRAM7, STANDING_ISLAND_11_TOKENS))
        for island in LOCKED_PAIRWISE_ISLANDS:
            if island in (STANDING_ISLAND_31_TOKENS, STANDING_ISLAND_11_TOKENS):
                self.assertTrue(is_contiguous_substring(GRAM7, island))
            else:
                self.assertFalse(is_contiguous_substring(GRAM7, island))
        self.assertEqual(
            (SIDE_HR, "Hr3", STANDING_ISLAND_31_H_SITE[2] + STANDING_ISLAND_31_OFFSETS[0]),
            STANDING_H_SITES[0],
        )
        self.assertEqual(
            (SIDE_QR, "Qr3", STANDING_ISLAND_31_Q_SITE[2] + STANDING_ISLAND_31_OFFSETS[0]),
            STANDING_Q_SITES[0],
        )
        self.assertEqual(
            (SIDE_HR, "Hr3", STANDING_ISLAND_11_H_SITE[2] + STANDING_ISLAND_11_OFFSETS[0]),
            STANDING_H_SITES[1],
        )
        self.assertEqual(
            (SIDE_QR, "Qr3", STANDING_ISLAND_11_Q_SITE[2] + STANDING_ISLAND_11_OFFSETS[0]),
            STANDING_Q_SITES[1],
        )
        for side, line, index in STANDING_H_SITES + STANDING_Q_SITES:
            stems = self.hpq_sides[side][LINE_NAMES[side].index(line)][index : index + 7]
            self.assertEqual(tuple(stems), GRAM7)
        self.assertEqual(self.claim_holds, STANDING_HQ_7GRAM_IS_HQ_PAIRWISE_ISLAND_SUBSTRING)
        self.assertTrue(STANDING_HQ_7GRAM_IS_HQ_PAIRWISE_ISLAND_SUBSTRING)
        self.assertEqual(STANDING_CLAIM, "hq_7gram_is_hq_pairwise_island_substring")
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertLess(len(GRAM7), 8)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_maximal_hq_extension_is_n31_and_p_is_zero(self):
        """Independent H/Q stem measure: longest shared container is n=31, P=0."""
        self.assertEqual(self.maximal_n, STANDING_MAXIMAL_N)
        self.assertEqual(self.maximal_tokens, STANDING_MAXIMAL_TOKENS)
        self.assertEqual(self.maximal_n, 31)
        self.assertEqual(len(self.maximal_tokens), 31)
        self.assertTrue(is_contiguous_substring(GRAM7, self.maximal_tokens))
        self.assertEqual(substring_offsets(GRAM7, self.maximal_tokens), (24,))
        self.assertEqual(self.freq_n, STANDING_MAXIMAL_N)
        self.assertEqual(self.freq_tokens, STANDING_MAXIMAL_TOKENS)
        self.assertEqual(self.maximal_tokens, STANDING_ISLAND_31_TOKENS)
        self.assertEqual(tuple(self.maximal_h_sites), STANDING_MAXIMAL_H_SITES)
        self.assertEqual(tuple(self.maximal_q_sites), STANDING_MAXIMAL_Q_SITES)
        self.assertEqual(tuple(self.maximal_p_sites), STANDING_MAXIMAL_P_SITES)
        self.assertEqual(len(self.maximal_h_sites), STANDING_MAXIMAL_H_HITS)
        self.assertEqual(len(self.maximal_q_sites), STANDING_MAXIMAL_Q_HITS)
        self.assertEqual(len(self.maximal_p_sites), STANDING_MAXIMAL_P_HITS)
        self.assertEqual(STANDING_MAXIMAL_P_HITS, 0)
        self.assertEqual(
            ngram_hit_count(concat_sides(self.hpq_sides, P_SIDES), self.maximal_tokens),
            0,
        )
        self.assertEqual(self.maximal_hits_by_tablet, STANDING_MAXIMAL_HITS_BY_TABLET)
        self.assertEqual(
            self.maximal_hits_by_tablet[VENDORED_TABLETS.index("P")],
            STANDING_MAXIMAL_P_HITS,
        )
        for side, line, index in STANDING_MAXIMAL_H_SITES + STANDING_MAXIMAL_Q_SITES:
            stems = self.hpq_sides[side][LINE_NAMES[side].index(line)][
                index : index + STANDING_MAXIMAL_N
            ]
            self.assertEqual(tuple(stems), STANDING_MAXIMAL_TOKENS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_pairwise_triple_and_w_scoreboards_still_compute(self):
        """Cycle 70 H–Q pairwise, cycle 108 triple-miss, and W stay."""
        prior_qh = TestMamariSmallStPetersburgSharedN8Scoreboard()
        prior_qh.setUp()
        prior_qh.test_q_vs_h_inventory_tokens_n_freq_and_hits()
        prior_qh.test_survey_matches_computed_lock()
        prior_triple = TestMamariHqMaxNHpqIslandSubstringScoreboard()
        prior_triple.setUp()
        prior_triple.test_7gram_is_not_substring_of_any_locked_hpq_island()
        prior_triple.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-109 H/Q pairwise-island lock."""
        lock = self.survey["hq_7gram_hq_pairwise_island_substring"]
        self.assertEqual(lock["cycle"], 109)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens7"]), GRAM7)
        self.assertEqual(lock["n7"], 7)
        self.assertEqual(lock["from_cycle"], 108)
        self.assertEqual(lock["h_hits"], STANDING_H_HITS)
        self.assertEqual(lock["q_hits"], STANDING_Q_HITS)
        self.assertEqual(lock["p_hits"], STANDING_P_HITS)
        self.assertEqual(tuple(tuple(row) for row in lock["h_sites"]), STANDING_H_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["q_sites"]), STANDING_Q_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["p_sites"]), STANDING_P_SITES)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["hq_7gram_is_hq_pairwise_island_substring"])
        self.assertEqual(
            lock["hq_7gram_is_hq_pairwise_island_substring"],
            STANDING_HQ_7GRAM_IS_HQ_PAIRWISE_ISLAND_SUBSTRING,
        )
        self.assertEqual(lock["matching_island_count"], STANDING_MATCHING_ISLAND_COUNT)
        self.assertEqual(lock["island_count"], STANDING_QH_MAXIMAL_COUNT)
        self.assertEqual(len(lock["matching_islands"]), 2)
        match_31 = lock["matching_islands"][0]
        self.assertEqual(tuple(match_31["tokens"]), STANDING_ISLAND_31_TOKENS)
        self.assertEqual(match_31["n"], STANDING_ISLAND_31_N)
        self.assertEqual(tuple(match_31["h_site"]), STANDING_ISLAND_31_H_SITE)
        self.assertEqual(tuple(match_31["q_site"]), STANDING_ISLAND_31_Q_SITE)
        self.assertEqual(tuple(match_31["offsets"]), STANDING_ISLAND_31_OFFSETS)
        match_11 = lock["matching_islands"][1]
        self.assertEqual(tuple(match_11["tokens"]), STANDING_ISLAND_11_TOKENS)
        self.assertEqual(match_11["n"], STANDING_ISLAND_11_N)
        self.assertEqual(tuple(match_11["h_site"]), STANDING_ISLAND_11_H_SITE)
        self.assertEqual(tuple(match_11["q_site"]), STANDING_ISLAND_11_Q_SITE)
        self.assertEqual(tuple(match_11["offsets"]), STANDING_ISLAND_11_OFFSETS)
        self.assertEqual(lock["hq_7gram_maximal_n"], STANDING_MAXIMAL_N)
        self.assertEqual(tuple(lock["hq_7gram_maximal_tokens"]), STANDING_MAXIMAL_TOKENS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["maximal_h_sites"]),
            STANDING_MAXIMAL_H_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["maximal_q_sites"]),
            STANDING_MAXIMAL_Q_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["maximal_p_sites"]),
            STANDING_MAXIMAL_P_SITES,
        )
        self.assertEqual(lock["maximal_h_hits"], STANDING_MAXIMAL_H_HITS)
        self.assertEqual(lock["maximal_q_hits"], STANDING_MAXIMAL_Q_HITS)
        self.assertEqual(lock["maximal_p_hits"], STANDING_MAXIMAL_P_HITS)
        self.assertEqual(lock["maximal_p_hits"], 0)
        self.assertEqual(tuple(lock["maximal_hits_by_tablet"]), STANDING_MAXIMAL_HITS_BY_TABLET)
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_q_shared_n8_unchanged"])
        self.assertTrue(lock["standing_hq_max_n_hpq_island_substring_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_p_max_n_hpq_island_substring_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_q_shared_n8_inventory"]["cycle"], 70)
        self.assertEqual(
            self.survey["tablet_q_shared_n8_inventory"]["q_vs_h"]["maximal_count"], 15
        )
        self.assertEqual(
            self.survey["tablet_q_shared_n8_inventory"]["q_vs_h"]["maximals"][0][1], 31
        )
        self.assertEqual(self.survey["hq_max_n_hpq_island_substring"]["cycle"], 108)
        self.assertFalse(
            self.survey["hq_max_n_hpq_island_substring"]["hq_max_n_is_hpq_island_substring"]
        )
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertEqual(
            self.survey["tablet_h_p_q_triple_n8_inventory"]["maximal_count"], 5
        )
        self.assertEqual(self.survey["p_max_n_hpq_island_substring"]["cycle"], 107)
        self.assertTrue(
            self.survey["p_max_n_hpq_island_substring"]["p_max_n_is_hpq_island_substring"]
        )
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHq7gramHqPairwiseIslandSubstringImageSnapshot(unittest.TestCase):
    """Cycle 109 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
