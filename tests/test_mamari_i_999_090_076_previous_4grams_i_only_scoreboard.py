"""I's cycle-262 3-gram site previous 4-grams off-I hapax lock.

Cycle 263 text-search lock. Uses already-vendored A–V and the
cycle-262 I sites of 3-gram 999 090 076 (N_I=16, N_off_I=0,
extra I=1 at Ia9[27] inside leftover n=4 remaining
999 090 076 057). Extra I of this 3-gram is leftover-of-leftover;
include it in the 4-gram lock (same as cycle 246 including extra
I of 090 076 087). Does not retune that 3-gram, leftover extra
previous-999 (cycle 261 K_999=15 / N_remaining_after_999=41),
leftover extra share-one-previous-stem (cycle 260 lost),
leftover extra sites, leftover n=4 remaining 999 090 076 057,
the leftover n=4 set, or the already-closed leftover remaining
family. Does not peel leftover extra remaining-after-999 this
cycle. Does not retune the forward peel of leftover extra I
090 076 (cycles 225–259). Does not overwrite cycle 167's
3-gram I-only 16/0 lock. Does not vendor a new tablet. Does
not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same claim-shape as cycle 213 (previous 4-grams of I-only
720 076 070 were all I-only hapax 1/0 x3). Token before G:
each previous 4-gram is contiguous W 999 090 076. Cycle 219
lost: 090 076 070 000 leaks 1/1 on T. Cycle 207 lost:
090 076 070 is not I-only (8/1 on T). Cycle 223 lost:
090 076 is not I-only (69/3 on T). Cycle 220 5-gram
999 090 076 070 000 is a different n=5 (1/0). 090 076 without
999, 720 076 070, and 999 090 076 071 do not count as these
4-grams. Do not retune leftover n=4, 076-cells, or any
detector. Do not lock leftover extra remaining-after-999.
Do not assume hapax; count each from fixtures.

Locks exact consecutive hits of each I 999 090 076 previous
4-gram on tablet I and on every other vendored tablet A–H
and J–V. Fourteen distinct 4-grams from the 16 I sites (all
16 have a previous token; N_line_initial=0). Shared:
000 999 090 076 is N_I=2 at Ia3[35]/Ia5[0];
090 999 090 076 is N_I=2 at Ia12[45]/Ia14[138]. Extra I
previous 4-gram 244 999 090 076 is N_I=1 at Ia9[26]. All
fourteen have N_off_I=0. Claim that can lose:
i_999_090_076_previous_4grams_all_i_only_hapax. True only if
every I 999 090 076 site that has a previous token has
previous 4-gram N_I==1 and N_off_I==0. Line-initial 3-grams
with no W do not make the claim lose; still lock them.
Measured: N_i_only=14 / N_not_i_only=0 / N_not_hapax=2.
The claim is false (shared 4-grams, not an off-I leak).
Nested-check each I 3-gram site that has a previous token ⊆
I sites of its previous 4-gram. Nested cycle 262 16/0 extra
I=1, cycle 261 K_999=15 N_remaining=41, cycle 260 34 distinct
G=999 K=15, cycle 220 5-gram 1/0, cycle 223 69/3, cycle 207
8/1 on T, and cycle 167 16/0 stay.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_720_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE212_GRAM3,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_I_SITES as CYCLE167_I_SITES,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_leftover_extra_previous_i_only_scoreboard import (
    GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE262_EXTRA_I_SITES,
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE262_CLAIM,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE262_PREVIOUS_4GRAMS,
    STANDING_I_SITE_ROWS as CYCLE262_SITE_ROWS,
    STANDING_I_SITES as CYCLE262_I_SITES,
    STANDING_LEFTOVER_3GRAM_SITES as CYCLE262_LEFTOVER_3GRAM_SITES,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE262_LEFTOVER_MATCHING_SITES,
    STANDING_N_EXTRA as CYCLE262_N_EXTRA,
    STANDING_N_I as CYCLE262_N_I,
    STANDING_N_LEFTOVER as CYCLE262_N_LEFTOVER,
    STANDING_N_OFF_I as CYCLE262_N_OFF_I,
    extra_i_sites,
    leftover_extra_090_076_site_for_3gram,
    leftover_extra_previous_999_subset,
    leftover_3gram_sites,
    site_previous_4gram_for_3gram,
    TestMamariI3gram999090076LeftoverExtraPreviousIOnlyScoreboard,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    GRAM5 as CYCLE220_GRAM5,
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_CLAIM,
    STANDING_I_SITES as CYCLE220_I_SITES,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
    TestMamariI5gram999090076070000IOnlyScoreboard,
)
from tests.test_mamari_i_720_076_070_previous_4grams_i_only_scoreboard import (
    STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY as CYCLE213_I_ONLY,
    STANDING_SEQUENCES as CYCLE213_SEQUENCES,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_I_ONLY,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_G as CYCLE261_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 as CYCLE261_CLAIM,
    STANDING_K_999 as CYCLE261_K_999,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE261_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
    STANDING_N_LEFTOVER_EXTRA as CYCLE261_N_LEFTOVER_EXTRA,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    NEAR_MISS_999_090_076_071,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    line_stems_for_site,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    OFF_I_TABLETS,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_ALL_I_ONLY_HAPAX = True
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N5 = 5
NEAR_MISS_720_076_070 = CYCLE212_GRAM3
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076 = GRAM2
NEAR_MISS_5GRAM = CYCLE220_GRAM5
NEAR_MISS_LEFTOVER_N4_057 = ("999", "090", "076", "057")
STANDING_CYCLE262_SITES = CYCLE262_I_SITES
STANDING_PER_SITE_PREVIOUS_4GRAMS = CYCLE262_PREVIOUS_4GRAMS


def distinct_previous_4grams(
    grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """First-seen distinct previous 4-grams. None (line-initial) is skipped."""
    seen: list[tuple[str, ...]] = []
    for gram in grams:
        if gram is not None and gram not in seen:
            seen.append(gram)
    return tuple(seen)


STANDING_SEQUENCES = distinct_previous_4grams(STANDING_PER_SITE_PREVIOUS_4GRAMS)
STANDING_N_SEQUENCES = 14
STANDING_N_I_SITES = 16
STANDING_N_WITH_PREVIOUS = 16
STANDING_N_LINE_INITIAL = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_PREVIOUS_STEMS = tuple(gram[0] for gram in STANDING_SEQUENCES)
STANDING_N_I_EACH = (1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_SEQUENCES
STANDING_HAPAX_EACH = (
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
)
STANDING_I_ONLY_EACH = (True,) * STANDING_N_SEQUENCES
STANDING_I_SITES = (
    ((SIDE_IA, "Ia1", 0),),
    ((SIDE_IA, "Ia2", 8),),
    ((SIDE_IA, "Ia3", 35), (SIDE_IA, "Ia5", 0)),
    ((SIDE_IA, "Ia3", 69),),
    ((SIDE_IA, "Ia4", 110),),
    ((SIDE_IA, "Ia4", 152),),
    ((SIDE_IA, "Ia5", 21),),
    ((SIDE_IA, "Ia6", 90),),
    ((SIDE_IA, "Ia7", 66),),
    ((SIDE_IA, "Ia7", 127),),
    ((SIDE_IA, "Ia9", 26),),
    ((SIDE_IA, "Ia9", 127),),
    ((SIDE_IA, "Ia12", 45), (SIDE_IA, "Ia14", 138)),
    ((SIDE_IA, "Ia13", 107),),
)
STANDING_CYCLE262_SITES_BY_GRAM = (
    ((SIDE_IA, "Ia1", 1),),
    ((SIDE_IA, "Ia2", 9),),
    ((SIDE_IA, "Ia3", 36), (SIDE_IA, "Ia5", 1)),
    ((SIDE_IA, "Ia3", 70),),
    ((SIDE_IA, "Ia4", 111),),
    ((SIDE_IA, "Ia4", 153),),
    ((SIDE_IA, "Ia5", 22),),
    ((SIDE_IA, "Ia6", 91),),
    ((SIDE_IA, "Ia7", 67),),
    ((SIDE_IA, "Ia7", 128),),
    ((SIDE_IA, "Ia9", 27),),
    ((SIDE_IA, "Ia9", 128),),
    ((SIDE_IA, "Ia12", 46), (SIDE_IA, "Ia14", 139)),
    ((SIDE_IA, "Ia13", 108),),
)
STANDING_ROLES = (
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
    "extra_i",
    "leftover_extra",
    "leftover_extra",
    "leftover_extra",
)
STANDING_NOT_HAPAX_SEQUENCES = (
    ("000", "999", "090", "076"),
    ("090", "999", "090", "076"),
)
STANDING_NOT_HAPAX_I_SITES = (
    ((SIDE_IA, "Ia3", 35), (SIDE_IA, "Ia5", 0)),
    ((SIDE_IA, "Ia12", 45), (SIDE_IA, "Ia14", 138)),
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_OFF_I_SITES = ((),) * STANDING_N_SEQUENCES
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_TWO_ON_I = tuple(
    2 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_HITS_BY_TABLET_TWO_ON_I if n_i == 2 else STANDING_HITS_BY_TABLET_ONE_ON_I
    for n_i in STANDING_N_I_EACH
)
STANDING_N_I_ONLY = 14
STANDING_N_NOT_I_ONLY = 0
STANDING_N_HAPAX = 12
STANDING_N_NOT_HAPAX = 2
STANDING_N_I_ONLY_SITES = 16
STANDING_N_NOT_I_ONLY_SITES = 0
STANDING_N_NOT_HAPAX_SITES = 4
STANDING_LEAKING_4GRAMS = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_EXTRA_I_SITES = CYCLE262_EXTRA_I_SITES
STANDING_N_EXTRA = 1
STANDING_LEFTOVER_MATCHING_SITES = CYCLE262_LEFTOVER_MATCHING_SITES
STANDING_LEFTOVER_3GRAM_SITES = CYCLE262_LEFTOVER_3GRAM_SITES
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_CLAIM = "i_999_090_076_previous_4grams_all_i_only_hapax"
STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX = False
STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY = True
STANDING_RESULT = "i_999_090_076_previous_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE213_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE219_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE220_5GRAM = False
STANDING_SAME_AS_CYCLE246_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE262 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE213 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE246_EXTRA_I = True
STANDING_090_076_WITHOUT_999_DOES_NOT_COUNT = True
STANDING_720_076_070_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_999_090_076_071_DOES_NOT_COUNT = True
STANDING_5GRAM_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_057_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_CYCLE167_NOT_OVERWRITTEN = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True


def previous_4gram_start_site(
    cycle262_site: tuple[str, str, int],
) -> tuple[str, str, int] | None:
    """Previous 4-gram starts one token before 999 090 076; None at line start."""
    side, line, index = cycle262_site
    if index < 1:
        return None
    return (side, line, index - 1)


def leftover_extra_090_076_site_for_4gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """090 076 starts two tokens after the previous-4 start."""
    side, line, index = site
    return (side, line, index + 2)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def sequence_is_i_only_hapax(n_i: int, n_off_i: int) -> bool:
    """True iff N_I==1 and N_off_I=0."""
    return n_i == 1 and n_off_i == 0


def i_999_090_076_previous_4grams_all_i_only_hapax(
    per_site_previous: tuple[tuple[str, ...] | None, ...],
    n_i_by_gram: dict[tuple[str, ...], int],
    n_off_i_by_gram: dict[tuple[str, ...], int],
) -> bool:
    """True iff every with-previous site has previous 4-gram hapax I-only.

    Line-initial sites (previous is None) do not make the claim lose.
    Shared 4-grams (N_I>1) lose. Off-I leaks (N_off_I>0) lose.
    """
    for gram in per_site_previous:
        if gram is None:
            continue
        if not sequence_is_i_only_hapax(n_i_by_gram[gram], n_off_i_by_gram[gram]):
            return False
    return True


def i_sites_subset_of_previous_4gram(
    cycle262_site: tuple[str, str, int],
    gram_i_sites: tuple[tuple[str, str, int], ...],
) -> bool:
    """True iff the 3-gram site's previous-4 start is among that 4-gram's I sites."""
    start = previous_4gram_start_site(cycle262_site)
    if start is None:
        return True
    return start in gram_i_sites


def site_row_as_survey(row: dict) -> dict:
    """JSON-ready per-I-site row (lists, not tuples)."""
    return {
        "tablet": row["tablet"],
        "side": row["side"],
        "line": row["line"],
        "index": row["index"],
        "tokens4": list(row["tokens4"]),
        "cycle262_site": list(row["cycle262_site"]),
        "leftover_extra_090_076_site": list(row["leftover_extra_090_076_site"]),
        "previous_stem": row["previous_stem"],
        "role": row["role"],
        "in_cycle261_leftover_extra_15": row["in_cycle261_leftover_extra_15"],
        "inside_leftover_n4_remaining": row["inside_leftover_n4_remaining"],
        "N_I": row["N_I"],
        "N_off_I": row["N_off_I"],
        "hapax": row["hapax"],
        "i_only": row["i_only"],
        "line_initial": row["line_initial"],
    }


def _n_i_for_gram(gram: tuple[str, ...]) -> int:
    """Locked N_I for one distinct previous 4-gram."""
    return STANDING_N_I_EACH[STANDING_SEQUENCES.index(gram)]


STANDING_SITE_ROWS = tuple(
    {
        "tablet": "I",
        "side": prior["side"],
        "line": prior["line"],
        "index": prior["index"] - 1,
        "tokens4": prior["previous_4gram"],
        "cycle262_site": (prior["side"], prior["line"], prior["index"]),
        "leftover_extra_090_076_site": prior["leftover_extra_090_076_site"],
        "previous_stem": prior["previous_4gram"][0],
        "role": (
            "extra_i"
            if not prior["in_cycle261_leftover_extra_15"]
            else "leftover_extra"
        ),
        "in_cycle261_leftover_extra_15": prior["in_cycle261_leftover_extra_15"],
        "inside_leftover_n4_remaining": prior["inside_leftover_n4_remaining"],
        "N_I": _n_i_for_gram(prior["previous_4gram"]),
        "N_off_I": 0,
        "hapax": _n_i_for_gram(prior["previous_4gram"]) == 1,
        "i_only": True,
        "line_initial": False,
    }
    for prior in CYCLE262_SITE_ROWS
)


class TestI999090076Previous4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-262 previous 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 720 / 090 076 070 / 5-gram are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("602", "999", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[2], ("000", "999", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[10], ("244", "999", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[12], ("090", "999", "090", "076"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_SEQUENCES)
        self.assertEqual(
            distinct_previous_4grams(STANDING_PER_SITE_PREVIOUS_4GRAMS),
            STANDING_SEQUENCES,
        )
        self.assertEqual(len(STANDING_PER_SITE_PREVIOUS_4GRAMS), STANDING_N_I_SITES)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[1:], GRAM3)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["000", "999", "090", "076", "000", "999", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_NOT_HAPAX_SEQUENCES[0]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:2]) + ["000"] + list(STANDING_SEQUENCES[0][2:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_720_076_070)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_5GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_LEFTOVER_N4_057)], STANDING_SEQUENCES[10]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["999", "090", "076"]], STANDING_SEQUENCES[0]), 0)
        planted = ["602", "999", "090", "076"]
        self.assertEqual(site_previous_4gram_for_3gram(planted, 1, GRAM3), STANDING_SEQUENCES[0])
        self.assertIsNone(site_previous_4gram_for_3gram(["999", "090", "076"], 0, GRAM3))
        self.assertTrue(STANDING_090_076_WITHOUT_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_720_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_5GRAM_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_057_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_hapax_requires_n_i_1_and_zero_off_i_per_site(self):
        """Boolean is True only when every with-previous site is hapax I-only."""
        provider = MockProvider()
        n_i = dict(zip(STANDING_SEQUENCES, STANDING_N_I_EACH, strict=True))
        n_off = dict(zip(STANDING_SEQUENCES, STANDING_N_OFF_I_EACH, strict=True))
        self.assertFalse(
            i_999_090_076_previous_4grams_all_i_only_hapax(
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                n_i,
                n_off,
            )
        )
        hapax_n_i = {gram: 1 for gram in STANDING_SEQUENCES}
        self.assertTrue(
            i_999_090_076_previous_4grams_all_i_only_hapax(
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                hapax_n_i,
                n_off,
            )
        )
        leak_off = dict(n_off)
        leak_off[STANDING_SEQUENCES[0]] = 1
        self.assertFalse(
            i_999_090_076_previous_4grams_all_i_only_hapax(
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                hapax_n_i,
                leak_off,
            )
        )
        shared = dict(hapax_n_i)
        shared[STANDING_NOT_HAPAX_SEQUENCES[0]] = 2
        self.assertFalse(
            i_999_090_076_previous_4grams_all_i_only_hapax(
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                shared,
                n_off,
            )
        )
        line_initial = (None,) + STANDING_PER_SITE_PREVIOUS_4GRAMS[1:]
        self.assertFalse(
            i_999_090_076_previous_4grams_all_i_only_hapax(
                line_initial,
                n_i,
                n_off,
            )
        )
        self.assertTrue(
            i_999_090_076_previous_4grams_all_i_only_hapax(
                line_initial,
                hapax_n_i,
                n_off,
            )
        )
        self.assertTrue(sequence_is_i_only(2, 0))
        self.assertFalse(sequence_is_i_only_hapax(2, 0))
        self.assertTrue(sequence_is_i_only_hapax(1, 0))
        self.assertFalse(sequence_is_i_only_hapax(1, 1))
        self.assertEqual(STANDING_CLAIM, "i_999_090_076_previous_4grams_all_i_only_hapax")
        self.assertFalse(STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX)
        self.assertTrue(STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY_HAPAX)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(STANDING_N_NOT_HAPAX, 2)
        self.assertEqual(STANDING_N_NOT_I_ONLY, 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_262_previous_not_retuned(self):
        """4-grams stay the cycle-262 I-site previous runs; extra I is included."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(STANDING_PER_SITE_PREVIOUS_4GRAMS, CYCLE262_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_CYCLE262_SITES, CYCLE262_I_SITES)
        self.assertEqual(STANDING_CYCLE262_SITES, CYCLE167_I_SITES)
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertEqual(STANDING_EXTRA_I_SITES, ((SIDE_IA, "Ia9", 27),))
        self.assertIn(("244", "999", "090", "076"), STANDING_SEQUENCES)
        self.assertIn(("244", "999", "090", "076"), STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertNotIn(("244", "999", "090", "076"), CYCLE261_MATCHING_PREVIOUS_4GRAMS)
        leftover_set = set(CYCLE261_MATCHING_PREVIOUS_4GRAMS)
        self.assertTrue(leftover_set.issubset(set(STANDING_PER_SITE_PREVIOUS_4GRAMS)))
        self.assertEqual(len(CYCLE261_MATCHING_PREVIOUS_4GRAMS), 15)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_720_076_070))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_090_076_070))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_999_090_076_071))
            self.assertFalse(is_contiguous_substring(gram, CYCLE219_LEAK_4GRAM))
        for site, gram in zip(
            STANDING_CYCLE262_SITES,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            strict=True,
        ):
            start = previous_4gram_start_site(site)
            self.assertIsNotNone(start)
            self.assertEqual(start[2], site[2] - 1)
            self.assertEqual(leftover_extra_090_076_site_for_4gram(start), leftover_extra_090_076_site_for_3gram(site))
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE213_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE219_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE220_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE262)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE213)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE246_EXTRA_I)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI999090076Previous4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture cycle-262 previous-4 I-only hapax lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle262_sites = STANDING_CYCLE262_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.per_site_previous = tuple(
            site_previous_4gram_for_3gram(
                line_stems_for_site(self.i_sides, site),
                site[2],
                GRAM3,
            )
            for site in self.cycle262_sites
        )
        self.line_initial = tuple(
            site
            for site, gram in zip(self.cycle262_sites, self.per_site_previous, strict=True)
            if gram is None
        )
        self.grams = STANDING_SEQUENCES
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams)
        self.n_i = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) + STANDING_IB_HITS
            for gram in self.grams
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.grams
        )
        self.off_i = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in self.grams
        )
        self.n_off_i = tuple(sum(row) for row in self.off_i)
        self.n_i_by_gram = dict(zip(self.grams, self.n_i, strict=True))
        self.n_off_i_by_gram = dict(zip(self.grams, self.n_off_i, strict=True))
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if not sequence_is_i_only(on, off)
        )
        self.n_hapax = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only_hapax(on, off)
        )
        self.n_not_hapax = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if not sequence_is_i_only_hapax(on, off)
        )
        self.leaking = tuple(
            gram
            for gram, off in zip(self.grams, self.n_off_i, strict=True)
            if off
        )
        self.claim_holds = i_999_090_076_previous_4grams_all_i_only_hapax(
            self.per_site_previous,
            self.n_i_by_gram,
            self.n_off_i_by_gram,
        )

    def test_tokens_and_sites_are_cycle_262_lock_not_retuned(self):
        """4-grams and I sites stay the cycle-262 previous lock; cycle 167 stays 16/0."""
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle262_sites, STANDING_CYCLE262_SITES)
        self.assertEqual(self.cycle262_sites, CYCLE167_I_SITES)
        self.assertEqual(len(self.cycle262_sites), 16)
        self.assertEqual(self.per_site_previous, STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(len(self.line_initial), STANDING_N_LINE_INITIAL)
        prior_262 = self.survey["i_3gram_999_090_076_leftover_extra_previous_i_only"]
        self.assertEqual(prior_262["cycle"], 262)
        self.assertEqual(tuple(prior_262["tokens3"]), GRAM3)
        self.assertEqual(prior_262["N_I"], CYCLE262_N_I)
        self.assertEqual(prior_262["N_I"], 16)
        self.assertEqual(prior_262["N_off_I"], CYCLE262_N_OFF_I)
        self.assertEqual(prior_262["N_off_I"], 0)
        self.assertEqual(prior_262["N_extra"], CYCLE262_N_EXTRA)
        self.assertEqual(prior_262["N_extra"], 1)
        self.assertTrue(prior_262["i_3gram_999_090_076_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_262["i_sites"]),
            STANDING_CYCLE262_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            prior_262["i_previous_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_262["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertTrue(leftover_extra_previous_999_subset())
        self.assertEqual(extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(leftover_3gram_sites(), STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_3GRAM_SITES), 15)
        leftover_999_starts = tuple(
            (side, line, index - 1) for side, line, index in CYCLE261_MATCHING_SITES
        )
        self.assertTrue(set(leftover_999_starts).issubset(set(STANDING_CYCLE262_SITES)))
        prior_261 = self.survey["i_leftover_extra_090_076_previous_999"]
        self.assertEqual(prior_261["cycle"], 261)
        self.assertEqual(prior_261["K_999"], 15)
        self.assertEqual(prior_261["N_remaining_after_999"], 41)
        self.assertTrue(prior_261["i_leftover_extra_090_076_exactly_15_share_previous_999"])
        prior_260 = self.survey["i_leftover_extra_090_076_previous_stem"]
        self.assertEqual(prior_260["cycle"], 260)
        self.assertEqual(prior_260["N_distinct_previous_stems"], 34)
        self.assertEqual(prior_260["G"], "999")
        self.assertEqual(prior_260["K"], 15)
        self.assertFalse(prior_260["i_leftover_extra_090_076_share_one_previous_stem"])
        prior_220 = self.survey["i_5gram_999_090_076_070_000_i_only"]
        self.assertEqual(prior_220["cycle"], 220)
        self.assertTrue(prior_220["i_5gram_999_090_076_070_000_i_only"])
        self.assertEqual(prior_220["N_I"], 1)
        self.assertEqual(prior_220["N_off_I"], 0)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in prior_167["i_sites"]),
            CYCLE167_I_SITES,
        )
        self.assertNotEqual(STANDING_CLAIM, prior_167["claim"] if "claim" in prior_167 else "i_3gram_999_090_076_i_only")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(CYCLE261_K_999, 15)
        self.assertEqual(CYCLE261_N_REMAINING_AFTER_999, 41)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_shared_4grams_are_i_only_not_hapax_and_claim_loses(self):
        """N_i_only=14 / N_not_i_only=0 / N_not_hapax=2. No off-I leak. Claim loses."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_hapax, STANDING_N_HAPAX)
        self.assertEqual(self.n_not_hapax, STANDING_N_NOT_HAPAX)
        self.assertEqual(self.n_i_only, 14)
        self.assertEqual(self.n_not_i_only, 0)
        self.assertEqual(self.n_not_hapax, 2)
        self.assertEqual(self.leaking, STANDING_LEAKING_4GRAMS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ())
        not_hapax = tuple(
            gram
            for gram, hapax in zip(STANDING_SEQUENCES, STANDING_HAPAX_EACH, strict=True)
            if not hapax
        )
        self.assertEqual(not_hapax, STANDING_NOT_HAPAX_SEQUENCES)
        for site, gram in zip(
            STANDING_CYCLE262_SITES,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            strict=True,
        ):
            start = previous_4gram_start_site(site)
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(site_previous_4gram_for_3gram(stems, site[2], GRAM3), gram)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N3]), GRAM3)
            gram_sites = STANDING_I_SITES[STANDING_SEQUENCES.index(gram)]
            self.assertTrue(i_sites_subset_of_previous_4gram(site, gram_sites))
            self.assertIn(start, gram_sites)
        extra_start = previous_4gram_start_site(STANDING_EXTRA_I_SITES[0])
        self.assertEqual(extra_start, (SIDE_IA, "Ia9", 26))
        self.assertEqual(
            STANDING_PER_SITE_PREVIOUS_4GRAMS[STANDING_CYCLE262_SITES.index(STANDING_EXTRA_I_SITES[0])],
            ("244", "999", "090", "076"),
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off, n_on in zip(self.hits_by_tablet, self.off_i, self.n_i, strict=True):
            expected = (
                STANDING_HITS_BY_TABLET_TWO_ON_I
                if n_on == 2
                else STANDING_HITS_BY_TABLET_ONE_ON_I
            )
            self.assertEqual(hits, expected)
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
        for tablet, *counts in zip(VENDORED_TABLETS, *self.hits_by_tablet, strict=True):
            for count, gram, n_on in zip(counts, self.grams, self.n_i, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, n_on if tablet == "I" else 0)
        self.assertFalse(self.claim_holds)
        self.assertEqual(
            self.claim_holds,
            STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX,
        )
        self.assertTrue(STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY_HAPAX)
        self.assertEqual(STANDING_CLAIM, "i_999_090_076_previous_4grams_all_i_only_hapax")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE213)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE246_EXTRA_I)
        self.assertTrue(CYCLE213_I_ONLY)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertNotIn(CYCLE219_LEAK_4GRAM, STANDING_SEQUENCES)
        for gram in CYCLE213_SEQUENCES:
            self.assertNotIn(gram, STANDING_SEQUENCES)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        not_hapax_sites = 0
        for row in STANDING_SITE_ROWS:
            self.assertEqual(row["tablet"], "I")
            self.assertFalse(row["line_initial"])
            self.assertTrue(row["i_only"])
            self.assertEqual(row["N_off_I"], 0)
            if not row["hapax"]:
                not_hapax_sites += 1
                self.assertEqual(row["N_I"], 2)
                self.assertIn(row["tokens4"], STANDING_NOT_HAPAX_SEQUENCES)
        self.assertEqual(not_hapax_sites, STANDING_N_NOT_HAPAX_SITES)
        self.assertEqual(STANDING_N_NOT_HAPAX_SITES, 4)
        self.assertEqual(STANDING_N_I_ONLY_SITES, 16)
        self.assertEqual(STANDING_N_NOT_I_ONLY_SITES, 0)
        extra_rows = [row for row in STANDING_SITE_ROWS if row["role"] == "extra_i"]
        self.assertEqual(len(extra_rows), 1)
        self.assertEqual(extra_rows[0]["cycle262_site"], (SIDE_IA, "Ia9", 27))
        self.assertEqual(extra_rows[0]["tokens4"], ("244", "999", "090", "076"))
        self.assertTrue(extra_rows[0]["hapax"])
        self.assertTrue(extra_rows[0]["inside_leftover_n4_remaining"])
        self.assertFalse(extra_rows[0]["in_cycle261_leftover_extra_15"])
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, STANDING_N_I_EACH, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        if self.n_not_hapax != 2:
            self.fail("measured N_not_hapax drifted from 2")
        if self.claim_holds:
            self.fail("hapax claim unexpectedly held")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_262_261_260_223_220_207_167_scoreboards_still_compute(self):
        """Cycle 262 16/0 extra I=1, 261 K=15/41, 260 34/999/15, 220 1/0, 223 69/3, 207 8/1, 167 16/0 stay."""
        prior_262 = TestMamariI3gram999090076LeftoverExtraPreviousIOnlyScoreboard()
        prior_262.setUp()
        prior_262.test_i_hits_are_sixteen_on_ia_and_leftover_extra_999_is_subset()
        prior_262.test_3gram_is_zero_off_i_and_i_only()
        prior_262.test_survey_matches_computed_lock()
        self.assertEqual(prior_262.i_hits, 16)
        self.assertEqual(prior_262.off_i_hits, 0)
        self.assertEqual(prior_262.i_sites, CYCLE262_I_SITES)
        self.assertEqual(len(prior_262.extra), 1)
        self.assertEqual(CYCLE262_N_I, 16)
        self.assertEqual(CYCLE262_N_OFF_I, 0)
        self.assertEqual(CYCLE262_N_EXTRA, 1)
        self.assertTrue(CYCLE262_CLAIM)
        if prior_262.i_hits != 16 or prior_262.off_i_hits != 0 or len(prior_262.extra) != 1:
            self.fail("nested cycle 262 999 090 076 leftover extra previous I-only 16/0 extra I=1 drifted")
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(CYCLE261_G, "999")
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertEqual(prior_261.n_leftover_extra, 56)
        self.assertTrue(CYCLE261_CLAIM)
        if (
            prior_261.k_999 != 15
            or CYCLE261_G != "999"
            or prior_261.n_remaining_after_999 != 41
        ):
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 N_remaining=41 drifted")
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertFalse(CYCLE260_SHARE_ONE)
        if prior_260.n_distinct != 34 or CYCLE260_G != "999" or CYCLE260_K != 15:
            self.fail("nested cycle 260 34 distinct G=999 K=15 drifted")
        prior_220 = TestMamariI5gram999090076070000IOnlyScoreboard()
        prior_220.setUp()
        prior_220.test_5gram_is_zero_off_i_and_i_only()
        prior_220.test_survey_matches_computed_lock()
        self.assertEqual(prior_220.i_hits, 1)
        self.assertEqual(prior_220.off_i_hits, 0)
        self.assertEqual(prior_220.i_sites, CYCLE220_I_SITES)
        self.assertTrue(CYCLE220_CLAIM)
        if prior_220.i_hits != 1 or prior_220.off_i_hits != 0:
            self.fail("nested cycle 220 999 090 076 070 000 I-only 1/0 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertEqual(prior_207.off_i_sites, CYCLE207_OFF_I_SITES)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, 16)
        self.assertEqual(prior_167.off_i_hits, 0)
        self.assertEqual(prior_167.i_sites, CYCLE167_I_SITES)
        self.assertTrue(CYCLE167_CLAIM)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-263 previous-4 I-only hapax lock."""
        lock = self.survey["i_999_090_076_previous_4grams_i_only"]
        self.assertEqual(lock["cycle"], 263)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only_hapax"])
        self.assertEqual(lock["hypothesis_all_i_only_hapax"], HYPOTHESIS_ALL_I_ONLY_HAPAX)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_I_3gram"], CYCLE262_N_I)
        self.assertEqual(lock["N_I_3gram"], 16)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE262_N_OFF_I)
        self.assertEqual(lock["N_off_I_3gram"], 0)
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle262_sites"]),
            STANDING_CYCLE262_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_extra_previous_999_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertTrue(lock["leftover_extra_previous_999_subset_of_i_sites"])
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 16)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(lock["N_distinct_4grams"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_distinct_4grams"], 14)
        self.assertEqual(tuple(lock["per_site_previous_stems"]), tuple(
            gram[0] for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS
        ))
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), 14)
        for row, gram, sites, cycle_sites, prev, role, n_on, n_off, hapax, off_sites in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_I_SITES,
            STANDING_CYCLE262_SITES_BY_GRAM,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_HAPAX_EACH,
            STANDING_OFF_I_SITES,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["cycle262_sites"]), cycle_sites)
            self.assertEqual(row["previous_stem"], prev)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["ia_hits"], n_on)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(row["ib_sites"], [])
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual([list(site_row) for site_row in off_sites], row["off_i_sites"])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            expected_hits = (
                STANDING_HITS_BY_TABLET_TWO_ON_I
                if n_on == 2
                else STANDING_HITS_BY_TABLET_ONE_ON_I
            )
            self.assertEqual(tuple(row["hits_by_tablet"]), expected_hits)
            self.assertTrue(row["i_only"])
            self.assertEqual(row["hapax"], hapax)
        self.assertEqual(
            [site_row_as_survey(row) for row in STANDING_SITE_ROWS],
            lock["site_rows"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            lock["per_site_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["distinct_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_NOT_HAPAX_SEQUENCES],
            lock["not_hapax_4grams"],
        )
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_not_hapax"], STANDING_N_NOT_HAPAX)
        self.assertEqual(lock["N_i_only"], 14)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["N_not_hapax"], 2)
        self.assertEqual(lock["N_i_only_sites"], STANDING_N_I_ONLY_SITES)
        self.assertEqual(lock["N_not_i_only_sites"], STANDING_N_NOT_I_ONLY_SITES)
        self.assertEqual(lock["N_not_hapax_sites"], STANDING_N_NOT_HAPAX_SITES)
        self.assertEqual(lock["N_i_only_sites"], 16)
        self.assertEqual(lock["N_not_hapax_sites"], 4)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_999_090_076_previous_4grams_all_i_only_hapax"])
        self.assertTrue(lock["i_999_090_076_previous_4grams_all_i_only"])
        self.assertEqual(
            lock["i_999_090_076_previous_4grams_all_i_only_hapax"],
            STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle213_previous_4grams"])
        self.assertFalse(lock["same_as_cycle219_forward_4grams"])
        self.assertFalse(lock["same_as_cycle220_5gram"])
        self.assertFalse(lock["same_as_cycle246_forward_4grams"])
        self.assertFalse(lock["same_as_cycle262"])
        self.assertTrue(lock["same_claim_shape_as_cycle213"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["same_claim_shape_as_cycle246_extra_i"])
        self.assertTrue(lock["090_076_without_999_does_not_count"])
        self.assertTrue(lock["720_076_070_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["999_090_076_071_does_not_count"])
        self.assertTrue(lock["5gram_does_not_count"])
        self.assertTrue(lock["leftover_n4_057_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_999_is_not_this_cycle"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["cycle167_not_overwritten"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertEqual(lock["nested_cycle262_N_I"], 16)
        self.assertEqual(lock["nested_cycle262_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle262_N_extra"], 1)
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle260_N_distinct_previous_stems"], 34)
        self.assertEqual(lock["nested_cycle260_G"], "999")
        self.assertEqual(lock["nested_cycle260_K"], 15)
        self.assertFalse(lock["nested_cycle260_share_one_previous_stem"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle220_N_I"], 1)
        self.assertEqual(lock["nested_cycle220_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["standing_i_3gram_999_090_076_leftover_extra_previous_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_5gram_999_090_076_070_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_720_076_070_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_999_090_076_leftover_extra_previous_i_only"]["cycle"], 262)
        self.assertTrue(
            self.survey["i_3gram_999_090_076_leftover_extra_previous_i_only"][
                "i_3gram_999_090_076_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["cycle"], 261)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["K_999"], 15)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_999"]["N_remaining_after_999"],
            41,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["cycle"], 260)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_stem"]["N_distinct_previous_stems"],
            34,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_5gram_999_090_076_070_000_i_only"]["cycle"], 220)
        self.assertTrue(
            self.survey["i_5gram_999_090_076_070_000_i_only"][
                "i_5gram_999_090_076_070_000_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["cycle"], 213)
        self.assertTrue(
            self.survey["i_720_076_070_previous_4grams_i_only"][
                "i_720_076_070_previous_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI999090076Previous4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 263 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
