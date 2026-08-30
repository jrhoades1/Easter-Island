"""I's cycle-279 3-gram site previous 4-grams off-I hapax lock.

Cycle 280 text-search lock. Uses already-vendored A–V and the
cycle-279 I sites of 3-gram 045 090 076 (N_I=2, N_off_I=0,
extra I=0). Both I sites are the leftover extra remaining-
after-071 previous-045 pair (045-starts one token earlier;
090-starts Ia1[15]/Ia2[37]). Extra I of this 3-gram is empty
leftover-of-leftover; there is no extra I to include (unlike
cycle 246 / 263 / 269). Does not retune that 3-gram, leftover
extra remaining-after-071 previous-045 (cycle 278 K_045=2 /
N_remaining_after_090_and_076_and_071_and_045=29), leftover
extra remaining-after-076 previous-071 (cycle 275 holds),
leftover extra remaining-after-090 previous-076 (cycle 273
holds), leftover extra remaining-after-600 previous-090
(cycle 271 holds), leftover extra remaining-after-600 unique
previous stem (cycle 270 lost), leftover extra remaining-
after-999 previous-600 (cycle 267 holds), leftover extra
previous-999 (cycle 261 holds), leftover extra
share-one-previous-stem (cycle 260 lost), leftover extra
sites, leftover n=4 remaining 090 076 020 010, the leftover
n=4 set, or the already-closed leftover remaining family.
Does not peel leftover extra remaining-after-045 / remaining
009 this cycle. Does not retune leftover n=4. Does not
retune the forward peel of leftover extra I 090 076 (cycles
225–259). Does not overwrite cycle 167's 3-gram I-only 16/0
lock. Does not overwrite cycle 279's 3-gram I-only 2/0 lock.
Does not overwrite cycle 277's previous-4 I-only hapax 2/0
lock. Does not overwrite cycle 276's 3-gram I-only 2/0 lock.
Does not retune cycle 272's 3-gram 090 090 076 I-only lose
3/1 on T extra I=1 or peel its T / extra-I. Does not retune
cycle 274's 3-gram 076 090 076 I-only lose 3/1 on T extra
I=1 or peel its T / extra-I. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same claim-shape as cycle 213 (previous 4-grams of I-only
720 076 070 were all I-only hapax 1/0 x3), cycle 269
(previous 4-grams of I-only 600 090 076 were all I-only
hapax 6/0), and cycle 277 (previous 4-grams of I-only
071 090 076 were all I-only hapax 2/0). Token before G:
each previous 4-gram is contiguous W 045 090 076. Cycle 219
lost: 090 076 070 000 leaks 1/1 on T. Cycle 207 lost:
090 076 070 is not I-only (8/1 on T). Cycle 223 lost:
090 076 is not I-only (69/3 on T). Cycle 263 lost: previous
4-grams of I 999 090 076 were I-only but not all hapax
(14/0, N_not_hapax=2). Cycle 278 listed previous 4-grams
093 045 090 076 / 061 045 090 076; measure, do not assume.
090 076 without 045, 999 090 076, 600 090 076, 090 090 076,
076 090 076, 071 090 076, 720 076 070, 090 076 070,
076 071 090, and leftover n=4 remaining 090 076 020 010 do
not count as these 4-grams. Do not retune leftover n=4,
076-cells, or any detector. Do not lock leftover extra
remaining-after-045. Do not assume hapax; count each from
fixtures.

Locks exact consecutive hits of each I 045 090 076 previous
4-gram on tablet I and on every other vendored tablet A–H
and J–V. Two distinct 4-grams from the 2 I sites (both have
a previous token; N_line_initial=0). Both leftover extra
previous-045 (extra I=0). Both have N_I=1 and N_off_I=0.
Claim that can lose:
i_045_090_076_previous_4grams_all_i_only_hapax. True only if
every I 045 090 076 site that has a previous token has
previous 4-gram N_I==1 and N_off_I==0. Line-initial 3-grams
with no W do not make the claim lose; still lock them.
Measured: N_i_only=2 / N_not_i_only=0 / N_not_hapax=0.
The claim is true (all hapax, no off-I leak). Nested-check
each I 3-gram site that has a previous token ⊆ I sites of
its previous 4-gram. Nested cycle 279 2/0 extra I=0, cycle
278 K_045=2 N_remaining_after_090_and_076_and_071_and_045=29
previous 4-grams 093 045 090 076 / 061 045 090 076, cycle
277 prev4 hapax 2/0, cycle 276 2/0 extra I=0, cycle 275
K_071=2 N=31, cycle 274 3/1 extra I=1, cycle 273 K_076=2
N=33, cycle 272 3/1 extra I=1, cycle 271 K_090=2 N=35,
cycle 270 unique-max false 5-way K=2 G=090, cycle 269 6/0
N_not_hapax=0, cycle 268 6/0 extra I=2, cycle 263 14/0
N_not_hapax=2, cycle 223 69/3, and cycle 207 8/1 on T stay.

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
from tests.test_mamari_i_3gram_045_090_076_i_only_scoreboard import (
    GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE279_EXTRA_I_SITES,
    STANDING_I_3GRAM_045_090_076_I_ONLY as CYCLE279_CLAIM,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE279_PREVIOUS_4GRAMS,
    STANDING_I_SITE_ROWS as CYCLE279_SITE_ROWS,
    STANDING_I_SITES as CYCLE279_I_SITES,
    STANDING_LEFTOVER_3GRAM_SITES as CYCLE279_LEFTOVER_3GRAM_SITES,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE279_LEFTOVER_MATCHING_SITES,
    STANDING_N_EXTRA as CYCLE279_N_EXTRA,
    STANDING_N_I as CYCLE279_N_I,
    STANDING_N_OFF_I as CYCLE279_N_OFF_I,
    extra_i_sites,
    leftover_extra_090_076_site_for_3gram,
    leftover_extra_remaining_after_071_previous_045_subset,
    leftover_3gram_sites,
    site_previous_4gram_for_3gram,
    TestMamariI3gram045090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_071_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE276_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE276_EXTRA_I_SITES,
    STANDING_I_3GRAM_071_090_076_I_ONLY as CYCLE276_CLAIM,
    STANDING_I_SITES as CYCLE276_I_SITES,
    STANDING_N_EXTRA as CYCLE276_N_EXTRA,
    STANDING_N_I as CYCLE276_N_I,
    STANDING_N_OFF_I as CYCLE276_N_OFF_I,
    TestMamariI3gram071090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_076_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE274_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE274_EXTRA_I_SITES,
    STANDING_I_3GRAM_076_090_076_I_ONLY as CYCLE274_CLAIM,
    STANDING_N_EXTRA as CYCLE274_N_EXTRA,
    STANDING_N_I as CYCLE274_N_I,
    STANDING_N_OFF_I as CYCLE274_N_OFF_I,
    TestMamariI3gram076090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE272_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE272_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_090_076_I_ONLY as CYCLE272_CLAIM,
    STANDING_N_EXTRA as CYCLE272_N_EXTRA,
    STANDING_N_I as CYCLE272_N_I,
    STANDING_N_OFF_I as CYCLE272_N_OFF_I,
    TestMamariI3gram090090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_600_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE268_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE268_EXTRA_I_SITES,
    STANDING_I_3GRAM_600_090_076_I_ONLY as CYCLE268_CLAIM,
    STANDING_N_EXTRA as CYCLE268_N_EXTRA,
    STANDING_N_I as CYCLE268_N_I,
    STANDING_N_OFF_I as CYCLE268_N_OFF_I,
    TestMamariI3gram600090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_720_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE212_GRAM3,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_I_SITES as CYCLE167_I_SITES,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_071_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_071_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE277_CLAIM,
    STANDING_N_I_ONLY as CYCLE277_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE277_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE277_N_NOT_I_ONLY,
    TestMamariI071090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_I_ONLY,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
)
from tests.test_mamari_i_600_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_600_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE269_CLAIM,
    STANDING_N_I_ONLY as CYCLE269_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE269_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE269_N_NOT_I_ONLY,
    TestMamariI600090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_720_076_070_previous_4grams_i_only_scoreboard import (
    STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY as CYCLE213_I_ONLY,
    STANDING_SEQUENCES as CYCLE213_SEQUENCES,
)
from tests.test_mamari_i_999_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE263_CLAIM,
    STANDING_N_I_ONLY as CYCLE263_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE263_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE263_N_NOT_I_ONLY,
    TestMamariI999090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_071_prev045_scoreboard import (
    STANDING_G as CYCLE278_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_REMAINING_AFTER_071_EXACTLY_2_SHARE_PREVIOUS_045 as CYCLE278_CLAIM,
    STANDING_K_045 as CYCLE278_K_045,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE278_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE278_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_090_AND_076_AND_071 as CYCLE278_N_REMAINING_AFTER_090_AND_076_AND_071,
    STANDING_N_REMAINING_AFTER_090_AND_076_AND_071_AND_045 as CYCLE278_N_REMAINING_AFTER_090_AND_076_AND_071_AND_045,
    TestMamariILeftoverExtra090076RemainingAfter071Prev045Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_prev071_scoreboard import (
    STANDING_G as CYCLE275_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_EXACTLY_2_SHARE_PREVIOUS_071 as CYCLE275_CLAIM,
    STANDING_K_071 as CYCLE275_K_071,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE275_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE275_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_090_AND_076_AND_071 as CYCLE275_N_REMAINING_AFTER_090_AND_076_AND_071,
    TestMamariILeftoverExtra090076RemainingAfter600Prev071Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_prev076_scoreboard import (
    STANDING_G as CYCLE273_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_EXACTLY_2_SHARE_PREVIOUS_076 as CYCLE273_CLAIM,
    STANDING_K_076 as CYCLE273_K_076,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE273_MATCHING_PREVIOUS_4GRAMS,
    STANDING_N_REMAINING_AFTER_090_AND_076 as CYCLE273_N_REMAINING_AFTER_090_AND_076,
    TestMamariILeftoverExtra090076RemainingAfter600Prev076Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_090_scoreboard import (
    STANDING_G as CYCLE271_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE271_CLAIM,
    STANDING_K_090 as CYCLE271_K_090,
    STANDING_N_REMAINING_AFTER_090 as CYCLE271_N_REMAINING_AFTER_090,
    TestMamariILeftoverExtra090076RemainingAfter600Previous090Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    STANDING_G as CYCLE270_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED_AT_K,
    STANDING_TIED_STEMS as CYCLE270_TIED_STEMS,
    TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING_LEFTOVERS,
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
NEAR_MISS_999_090_076 = CYCLE167_GRAM3
NEAR_MISS_600_090_076 = CYCLE268_GRAM3
NEAR_MISS_090_090_076 = CYCLE272_GRAM3
NEAR_MISS_076_090_076 = CYCLE274_GRAM3
NEAR_MISS_071_090_076 = CYCLE276_GRAM3
NEAR_MISS_076_071_090 = ("076", "071", "090")
NEAR_MISS_LEFTOVER_N4_020_010 = ("090", "076", "020", "010")
STANDING_CYCLE279_SITES = CYCLE279_I_SITES
STANDING_PER_SITE_PREVIOUS_4GRAMS = CYCLE279_PREVIOUS_4GRAMS


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
STANDING_N_SEQUENCES = 2
STANDING_N_I_SITES = 2
STANDING_N_WITH_PREVIOUS = 2
STANDING_N_LINE_INITIAL = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_PREVIOUS_STEMS = tuple(gram[0] for gram in STANDING_SEQUENCES)
STANDING_N_I_EACH = (1, 1)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_SEQUENCES
STANDING_HAPAX_EACH = (True, True)
STANDING_I_ONLY_EACH = (True, True)
STANDING_I_SITES = (
    ((SIDE_IA, "Ia1", 13),),
    ((SIDE_IA, "Ia2", 35),),
)
STANDING_CYCLE279_SITES_BY_GRAM = (
    ((SIDE_IA, "Ia1", 14),),
    ((SIDE_IA, "Ia2", 36),),
)
STANDING_ROLES = (
    "leftover_extra",
    "leftover_extra",
)
STANDING_NOT_HAPAX_SEQUENCES = ()
STANDING_NOT_HAPAX_I_SITES = ()
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_OFF_I_SITES = ((),) * STANDING_N_SEQUENCES
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (STANDING_HITS_BY_TABLET_ONE_ON_I,) * STANDING_N_SEQUENCES
STANDING_N_I_ONLY = 2
STANDING_N_NOT_I_ONLY = 0
STANDING_N_HAPAX = 2
STANDING_N_NOT_HAPAX = 0
STANDING_N_I_ONLY_SITES = 2
STANDING_N_NOT_I_ONLY_SITES = 0
STANDING_N_NOT_HAPAX_SITES = 0
STANDING_LEAKING_4GRAMS = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_EXTRA_I_SITES = CYCLE279_EXTRA_I_SITES
STANDING_N_EXTRA = 0
STANDING_LEFTOVER_MATCHING_SITES = CYCLE279_LEFTOVER_MATCHING_SITES
STANDING_LEFTOVER_3GRAM_SITES = CYCLE279_LEFTOVER_3GRAM_SITES
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_CLAIM = "i_045_090_076_previous_4grams_all_i_only_hapax"
STANDING_I_045_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX = True
STANDING_I_045_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY = True
STANDING_RESULT = "i_045_090_076_previous_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE213_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE219_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE263_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE269_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE277_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE278 = False
STANDING_SAME_AS_CYCLE279 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE213 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE269 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE277 = True
STANDING_090_076_WITHOUT_045_DOES_NOT_COUNT = True
STANDING_999_090_076_DOES_NOT_COUNT = True
STANDING_600_090_076_DOES_NOT_COUNT = True
STANDING_090_090_076_DOES_NOT_COUNT = True
STANDING_076_090_076_DOES_NOT_COUNT = True
STANDING_071_090_076_DOES_NOT_COUNT = True
STANDING_720_076_070_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_076_071_090_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_020_010_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_045_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_REMAINING_AFTER_045 = True
STANDING_DO_NOT_PEEL_009 = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_CYCLE167_NOT_OVERWRITTEN = True
STANDING_CYCLE276_NOT_OVERWRITTEN = True
STANDING_CYCLE277_NOT_OVERWRITTEN = True
STANDING_CYCLE278_NOT_RETUNED = True
STANDING_CYCLE279_NOT_OVERWRITTEN = True
STANDING_CYCLE272_NOT_RETUNED = True
STANDING_CYCLE274_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True


def previous_4gram_start_site(
    cycle279_site: tuple[str, str, int],
) -> tuple[str, str, int] | None:
    """Previous 4-gram starts one token before 045 090 076; None at line start."""
    side, line, index = cycle279_site
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


def i_045_090_076_previous_4grams_all_i_only_hapax(
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
    cycle279_site: tuple[str, str, int],
    gram_i_sites: tuple[tuple[str, str, int], ...],
) -> bool:
    """True iff the 3-gram site's previous-4 start is among that 4-gram's I sites."""
    start = previous_4gram_start_site(cycle279_site)
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
        "cycle279_site": list(row["cycle279_site"]),
        "leftover_extra_090_076_site": list(row["leftover_extra_090_076_site"]),
        "previous_stem": row["previous_stem"],
        "role": row["role"],
        "in_cycle278_leftover_extra_2": row["in_cycle278_leftover_extra_2"],
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
        "cycle279_site": (prior["side"], prior["line"], prior["index"]),
        "leftover_extra_090_076_site": prior["leftover_extra_090_076_site"],
        "previous_stem": prior["previous_4gram"][0],
        "role": (
            "extra_i"
            if not prior["in_cycle278_leftover_extra_2"]
            else "leftover_extra"
        ),
        "in_cycle278_leftover_extra_2": prior["in_cycle278_leftover_extra_2"],
        "inside_leftover_n4_remaining": prior["inside_leftover_n4_remaining"],
        "N_I": _n_i_for_gram(prior["previous_4gram"]),
        "N_off_I": 0,
        "hapax": _n_i_for_gram(prior["previous_4gram"]) == 1,
        "i_only": True,
        "line_initial": False,
    }
    for prior in CYCLE279_SITE_ROWS
)


class TestI045090076Previous4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-279 previous 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 999 / 090 076 / leftover n=4 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("093", "045", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[1], ("061", "045", "090", "076"))
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
        overlap = [["093", "045", "090", "076", "093", "045", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:2]) + ["000"] + list(STANDING_SEQUENCES[0][2:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_720_076_070)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_600_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_071_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_071_090)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_LEFTOVER_N4_020_010)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["045", "090", "076"]], STANDING_SEQUENCES[0]), 0)
        planted = ["093", "045", "090", "076"]
        self.assertEqual(site_previous_4gram_for_3gram(planted, 1, GRAM3), STANDING_SEQUENCES[0])
        self.assertIsNone(site_previous_4gram_for_3gram(["045", "090", "076"], 0, GRAM3))
        self.assertTrue(STANDING_090_076_WITHOUT_045_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_600_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_071_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_720_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_090_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_020_010_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_hapax_requires_n_i_1_and_zero_off_i_per_site(self):
        """Boolean is True only when every with-previous site is hapax I-only."""
        provider = MockProvider()
        n_i = dict(zip(STANDING_SEQUENCES, STANDING_N_I_EACH, strict=True))
        n_off = dict(zip(STANDING_SEQUENCES, STANDING_N_OFF_I_EACH, strict=True))
        self.assertTrue(
            i_045_090_076_previous_4grams_all_i_only_hapax(
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                n_i,
                n_off,
            )
        )
        leak_off = dict(n_off)
        leak_off[STANDING_SEQUENCES[0]] = 1
        self.assertFalse(
            i_045_090_076_previous_4grams_all_i_only_hapax(
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                n_i,
                leak_off,
            )
        )
        shared = dict(n_i)
        shared[STANDING_SEQUENCES[0]] = 2
        self.assertFalse(
            i_045_090_076_previous_4grams_all_i_only_hapax(
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                shared,
                n_off,
            )
        )
        line_initial = (None,) + STANDING_PER_SITE_PREVIOUS_4GRAMS[1:]
        self.assertTrue(
            i_045_090_076_previous_4grams_all_i_only_hapax(
                line_initial,
                n_i,
                n_off,
            )
        )
        shared_line_initial = dict(n_i)
        shared_line_initial[STANDING_SEQUENCES[1]] = 2
        self.assertFalse(
            i_045_090_076_previous_4grams_all_i_only_hapax(
                line_initial,
                shared_line_initial,
                n_off,
            )
        )
        self.assertTrue(sequence_is_i_only(2, 0))
        self.assertFalse(sequence_is_i_only_hapax(2, 0))
        self.assertTrue(sequence_is_i_only_hapax(1, 0))
        self.assertFalse(sequence_is_i_only_hapax(1, 1))
        self.assertEqual(STANDING_CLAIM, "i_045_090_076_previous_4grams_all_i_only_hapax")
        self.assertTrue(STANDING_I_045_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX)
        self.assertTrue(STANDING_I_045_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY_HAPAX)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(STANDING_N_NOT_HAPAX, 0)
        self.assertEqual(STANDING_N_NOT_I_ONLY, 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_279_previous_not_retuned(self):
        """4-grams stay the cycle-279 I-site previous runs; extra I is empty."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("045", "090", "076"))
        self.assertEqual(STANDING_PER_SITE_PREVIOUS_4GRAMS, CYCLE279_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_CYCLE279_SITES, CYCLE279_I_SITES)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(STANDING_EXTRA_I_SITES, ())
        self.assertEqual(STANDING_SEQUENCES, CYCLE278_MATCHING_PREVIOUS_4GRAMS)
        leftover_set = set(CYCLE278_MATCHING_PREVIOUS_4GRAMS)
        self.assertTrue(leftover_set.issubset(set(STANDING_PER_SITE_PREVIOUS_4GRAMS)))
        self.assertEqual(len(CYCLE278_MATCHING_PREVIOUS_4GRAMS), 2)
        self.assertNotEqual(STANDING_SEQUENCES[0], STANDING_SEQUENCES[1])
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_720_076_070))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_090_076_070))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_999_090_076))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_600_090_076))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_090_090_076))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_076_090_076))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_071_090_076))
            self.assertFalse(is_contiguous_substring(gram, CYCLE219_LEAK_4GRAM))
        for site, gram in zip(
            STANDING_CYCLE279_SITES,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            strict=True,
        ):
            start = previous_4gram_start_site(site)
            self.assertIsNotNone(start)
            self.assertEqual(start[2], site[2] - 1)
            self.assertEqual(
                leftover_extra_090_076_site_for_4gram(start),
                leftover_extra_090_076_site_for_3gram(site),
            )
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE213_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE219_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE263_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE269_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE277_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE278)
        self.assertFalse(STANDING_SAME_AS_CYCLE279)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE213)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE269)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE277)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_045_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_045)
        self.assertTrue(STANDING_DO_NOT_PEEL_009)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE279_NOT_OVERWRITTEN)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI045090076Previous4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture cycle-279 previous-4 I-only hapax lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle279_sites = STANDING_CYCLE279_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.per_site_previous = tuple(
            site_previous_4gram_for_3gram(
                line_stems_for_site(self.i_sides, site),
                site[2],
                GRAM3,
            )
            for site in self.cycle279_sites
        )
        self.line_initial = tuple(
            site
            for site, gram in zip(self.cycle279_sites, self.per_site_previous, strict=True)
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
        self.claim_holds = i_045_090_076_previous_4grams_all_i_only_hapax(
            self.per_site_previous,
            self.n_i_by_gram,
            self.n_off_i_by_gram,
        )

    def test_tokens_and_sites_are_cycle_279_lock_not_retuned(self):
        """4-grams and I sites stay the cycle-279 previous lock; cycle 167 stays 16/0."""
        self.assertEqual(GRAM3, ("045", "090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle279_sites, STANDING_CYCLE279_SITES)
        self.assertEqual(len(self.cycle279_sites), 2)
        self.assertEqual(self.per_site_previous, STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(len(self.line_initial), STANDING_N_LINE_INITIAL)
        prior_279 = self.survey["i_3gram_045_090_076_i_only"]
        self.assertEqual(prior_279["cycle"], 279)
        self.assertEqual(tuple(prior_279["tokens3"]), GRAM3)
        self.assertEqual(prior_279["N_I"], CYCLE279_N_I)
        self.assertEqual(prior_279["N_I"], 2)
        self.assertEqual(prior_279["N_off_I"], CYCLE279_N_OFF_I)
        self.assertEqual(prior_279["N_off_I"], 0)
        self.assertEqual(prior_279["N_extra"], CYCLE279_N_EXTRA)
        self.assertEqual(prior_279["N_extra"], 0)
        self.assertTrue(prior_279["i_3gram_045_090_076_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_279["i_sites"]),
            STANDING_CYCLE279_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            prior_279["i_previous_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_279["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertTrue(leftover_extra_remaining_after_071_previous_045_subset())
        self.assertEqual(extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(leftover_3gram_sites(), STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_3GRAM_SITES), 2)
        leftover_045_starts = tuple(
            (side, line, index - 1) for side, line, index in CYCLE278_MATCHING_SITES
        )
        self.assertTrue(set(leftover_045_starts).issubset(set(STANDING_CYCLE279_SITES)))
        prior_278 = self.survey[
            "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_remaining_after_071_previous_045"
        ]
        self.assertEqual(prior_278["cycle"], 278)
        self.assertEqual(prior_278["K_045"], 2)
        self.assertEqual(prior_278["N_remaining_after_090_and_076_and_071_and_045"], 29)
        self.assertTrue(
            prior_278[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_remaining_after_071_exactly_2_share_previous_045"
            ]
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE278_MATCHING_PREVIOUS_4GRAMS],
            prior_278["matching_previous_4grams"],
        )
        prior_277 = self.survey["i_071_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_277["cycle"], 277)
        self.assertTrue(prior_277["i_071_090_076_previous_4grams_all_i_only_hapax"])
        self.assertEqual(prior_277["N_i_only"], 2)
        self.assertEqual(prior_277["N_not_i_only"], 0)
        self.assertEqual(prior_277["N_not_hapax"], 0)
        prior_276 = self.survey["i_3gram_071_090_076_i_only"]
        self.assertEqual(prior_276["cycle"], 276)
        self.assertTrue(prior_276["i_3gram_071_090_076_i_only"])
        self.assertEqual(prior_276["N_I"], 2)
        self.assertEqual(prior_276["N_off_I"], 0)
        self.assertEqual(prior_276["N_extra"], 0)
        prior_275 = self.survey[
            "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_previous_071"
        ]
        self.assertEqual(prior_275["cycle"], 275)
        self.assertEqual(prior_275["K_071"], 2)
        self.assertEqual(prior_275["N_remaining_after_090_and_076_and_071"], 31)
        prior_274 = self.survey["i_3gram_076_090_076_i_only"]
        self.assertEqual(prior_274["cycle"], 274)
        self.assertFalse(prior_274["i_3gram_076_090_076_i_only"])
        self.assertEqual(prior_274["N_I"], 3)
        self.assertEqual(prior_274["N_off_I"], 1)
        self.assertEqual(prior_274["N_extra"], 1)
        prior_273 = self.survey[
            "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"
        ]
        self.assertEqual(prior_273["cycle"], 273)
        self.assertEqual(prior_273["K_076"], 2)
        self.assertEqual(prior_273["N_remaining_after_090_and_076"], 33)
        prior_272 = self.survey["i_3gram_090_090_076_i_only"]
        self.assertEqual(prior_272["cycle"], 272)
        self.assertFalse(prior_272["i_3gram_090_090_076_i_only"])
        self.assertEqual(prior_272["N_I"], 3)
        self.assertEqual(prior_272["N_off_I"], 1)
        self.assertEqual(prior_272["N_extra"], 1)
        prior_271 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]
        self.assertEqual(prior_271["cycle"], 271)
        self.assertEqual(prior_271["K_090"], 2)
        self.assertEqual(prior_271["N_remaining_after_090"], 35)
        prior_270 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]
        self.assertEqual(prior_270["cycle"], 270)
        self.assertEqual(prior_270["G"], "090")
        self.assertEqual(prior_270["K"], 2)
        self.assertFalse(prior_270["G_uniquely_most_frequent"])
        self.assertEqual(prior_270["N_tied_at_K"], 5)
        prior_269 = self.survey["i_600_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_269["cycle"], 269)
        self.assertTrue(prior_269["i_600_090_076_previous_4grams_all_i_only_hapax"])
        self.assertEqual(prior_269["N_i_only"], 6)
        self.assertEqual(prior_269["N_not_i_only"], 0)
        self.assertEqual(prior_269["N_not_hapax"], 0)
        prior_268 = self.survey["i_3gram_600_090_076_i_only"]
        self.assertEqual(prior_268["cycle"], 268)
        self.assertTrue(prior_268["i_3gram_600_090_076_i_only"])
        self.assertEqual(prior_268["N_I"], 6)
        self.assertEqual(prior_268["N_off_I"], 0)
        self.assertEqual(prior_268["N_extra"], 2)
        prior_263 = self.survey["i_999_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_263["cycle"], 263)
        self.assertFalse(prior_263["i_999_090_076_previous_4grams_all_i_only_hapax"])
        self.assertEqual(prior_263["N_i_only"], 14)
        self.assertEqual(prior_263["N_not_i_only"], 0)
        self.assertEqual(prior_263["N_not_hapax"], 2)
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
        self.assertNotEqual(STANDING_CLAIM, "i_3gram_999_090_076_i_only")
        self.assertNotEqual(STANDING_CLAIM, "i_3gram_045_090_076_i_only")
        self.assertNotEqual(STANDING_CLAIM, "i_071_090_076_previous_4grams_all_i_only_hapax")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(CYCLE278_K_045, 2)
        self.assertEqual(CYCLE278_N_REMAINING_AFTER_090_AND_076_AND_071_AND_045, 29)
        self.assertIn(NEAR_MISS_LEFTOVER_N4_020_010, CYCLE222_MATCHING_LEFTOVERS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_all_4grams_are_i_only_hapax_and_claim_holds(self):
        """N_i_only=2 / N_not_i_only=0 / N_not_hapax=0. No off-I leak. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_hapax, STANDING_N_HAPAX)
        self.assertEqual(self.n_not_hapax, STANDING_N_NOT_HAPAX)
        self.assertEqual(self.n_i_only, 2)
        self.assertEqual(self.n_not_i_only, 0)
        self.assertEqual(self.n_not_hapax, 0)
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
            STANDING_CYCLE279_SITES,
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
        self.assertEqual(STANDING_EXTRA_I_SITES, ())
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off in zip(self.hits_by_tablet, self.off_i, strict=True):
            self.assertEqual(hits, STANDING_HITS_BY_TABLET_ONE_ON_I)
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
        for tablet, *counts in zip(VENDORED_TABLETS, *self.hits_by_tablet, strict=True):
            for count, gram in zip(counts, self.grams, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, 1 if tablet == "I" else 0)
        self.assertTrue(self.claim_holds)
        self.assertEqual(
            self.claim_holds,
            STANDING_I_045_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX,
        )
        self.assertTrue(STANDING_I_045_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY_HAPAX)
        self.assertEqual(STANDING_CLAIM, "i_045_090_076_previous_4grams_all_i_only_hapax")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE213)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE269)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE277)
        self.assertTrue(CYCLE213_I_ONLY)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertNotIn(CYCLE219_LEAK_4GRAM, STANDING_SEQUENCES)
        for gram in CYCLE213_SEQUENCES:
            self.assertNotIn(gram, STANDING_SEQUENCES)
        self.assertTrue(CYCLE277_CLAIM)
        self.assertEqual(CYCLE277_N_I_ONLY, 2)
        self.assertEqual(CYCLE277_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE277_N_NOT_HAPAX, 0)
        self.assertTrue(CYCLE269_CLAIM)
        self.assertEqual(CYCLE269_N_I_ONLY, 6)
        self.assertEqual(CYCLE269_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE269_N_NOT_HAPAX, 0)
        self.assertFalse(CYCLE263_CLAIM)
        self.assertEqual(CYCLE263_N_I_ONLY, 14)
        self.assertEqual(CYCLE263_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE263_N_NOT_HAPAX, 2)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_045_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_045)
        self.assertTrue(STANDING_DO_NOT_PEEL_009)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE279_NOT_OVERWRITTEN)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        not_hapax_sites = 0
        for row in STANDING_SITE_ROWS:
            self.assertEqual(row["tablet"], "I")
            self.assertFalse(row["line_initial"])
            self.assertTrue(row["i_only"])
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["N_I"], 1)
            self.assertTrue(row["hapax"])
            self.assertEqual(row["role"], "leftover_extra")
            self.assertTrue(row["in_cycle278_leftover_extra_2"])
            self.assertFalse(row["inside_leftover_n4_remaining"])
            if not row["hapax"]:
                not_hapax_sites += 1
        self.assertEqual(not_hapax_sites, STANDING_N_NOT_HAPAX_SITES)
        self.assertEqual(STANDING_N_NOT_HAPAX_SITES, 0)
        self.assertEqual(STANDING_N_I_ONLY_SITES, 2)
        self.assertEqual(STANDING_N_NOT_I_ONLY_SITES, 0)
        extra_rows = [row for row in STANDING_SITE_ROWS if row["role"] == "extra_i"]
        self.assertEqual(len(extra_rows), 0)
        leftover_rows = [row for row in STANDING_SITE_ROWS if row["role"] == "leftover_extra"]
        self.assertEqual(len(leftover_rows), 2)
        self.assertEqual(leftover_rows[0]["cycle279_site"], (SIDE_IA, "Ia1", 14))
        self.assertEqual(leftover_rows[0]["tokens4"], ("093", "045", "090", "076"))
        self.assertEqual(leftover_rows[1]["cycle279_site"], (SIDE_IA, "Ia2", 36))
        self.assertEqual(leftover_rows[1]["tokens4"], ("061", "045", "090", "076"))
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, STANDING_N_I_EACH, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        if self.n_not_hapax != 0:
            self.fail("measured N_not_hapax drifted from 0")
        if not self.claim_holds:
            self.fail("hapax claim unexpectedly lost")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_279_278_277_276_275_274_273_272_271_270_269_268_263_223_207_167_still_compute(self):
        """Cycle 279 2/0 extra I=0, 278 K=2/29, 277 prev4 hapax 2/0, 276 2/0, 275 K=2/31, 274 3/1, 273 K_076=2/33, 272 3/1, 271 K_090=2/35, 270 5-way lose, 269 6/0, 268 6/0 extra I=2, 263 14/0 N_not_hapax=2 stay."""
        prior_279 = TestMamariI3gram045090076IOnlyScoreboard()
        prior_279.setUp()
        prior_279.test_i_hits_are_two_on_ia_and_leftover_extra_045_is_subset()
        prior_279.test_3gram_is_zero_off_i_and_i_only()
        prior_279.test_survey_matches_computed_lock()
        self.assertEqual(prior_279.i_hits, 2)
        self.assertEqual(prior_279.off_i_hits, 0)
        self.assertEqual(prior_279.i_sites, CYCLE279_I_SITES)
        self.assertEqual(len(prior_279.extra), 0)
        self.assertEqual(CYCLE279_N_I, 2)
        self.assertEqual(CYCLE279_N_OFF_I, 0)
        self.assertEqual(CYCLE279_N_EXTRA, 0)
        self.assertTrue(CYCLE279_CLAIM)
        if prior_279.i_hits != 2 or prior_279.off_i_hits != 0 or len(prior_279.extra) != 0:
            self.fail("nested cycle 279 045 090 076 I-only 2/0 extra I=0 drifted")
        prior_278 = TestMamariILeftoverExtra090076RemainingAfter071Prev045Scoreboard()
        prior_278.setUp()
        prior_278.test_counts_2_of_31_and_hypothesis_k_2_holds()
        prior_278.test_survey_matches_computed_lock()
        self.assertEqual(prior_278.k_045, 2)
        self.assertEqual(CYCLE278_G, "045")
        self.assertEqual(prior_278.n_remaining_after_090_and_076_and_071_and_045, 29)
        self.assertEqual(
            prior_278.matching_previous_4grams,
            (("093", "045", "090", "076"), ("061", "045", "090", "076")),
        )
        self.assertTrue(prior_278.claim_holds)
        self.assertTrue(CYCLE278_CLAIM)
        if (
            prior_278.k_045 != 2
            or CYCLE278_G != "045"
            or prior_278.n_remaining_after_090_and_076_and_071_and_045 != 29
        ):
            self.fail(
                "nested cycle 278 leftover extra remaining-after-071 previous-045 "
                "K_045=2 N_remaining_after_090_and_076_and_071_and_045=29 drifted"
            )
        prior_277 = TestMamariI071090076Previous4gramsIOnlyScoreboard()
        prior_277.setUp()
        prior_277.test_all_4grams_are_i_only_hapax_and_claim_holds()
        prior_277.test_survey_matches_computed_lock()
        self.assertEqual(prior_277.n_i_only, 2)
        self.assertEqual(prior_277.n_not_i_only, 0)
        self.assertEqual(prior_277.n_not_hapax, 0)
        self.assertTrue(prior_277.claim_holds)
        self.assertTrue(CYCLE277_CLAIM)
        if (
            prior_277.n_i_only != 2
            or prior_277.n_not_i_only != 0
            or prior_277.n_not_hapax != 0
            or not prior_277.claim_holds
        ):
            self.fail("nested cycle 277 prev4 hapax 2/0 N_not_hapax=0 drifted")
        prior_276 = TestMamariI3gram071090076IOnlyScoreboard()
        prior_276.setUp()
        prior_276.test_i_hits_are_two_on_ia_and_leftover_extra_071_is_subset()
        prior_276.test_3gram_is_zero_off_i_and_i_only()
        prior_276.test_survey_matches_computed_lock()
        self.assertEqual(prior_276.i_hits, 2)
        self.assertEqual(prior_276.off_i_hits, 0)
        self.assertEqual(prior_276.i_sites, CYCLE276_I_SITES)
        self.assertEqual(len(prior_276.extra), 0)
        self.assertEqual(CYCLE276_N_I, 2)
        self.assertEqual(CYCLE276_N_OFF_I, 0)
        self.assertEqual(CYCLE276_N_EXTRA, 0)
        self.assertTrue(CYCLE276_CLAIM)
        if prior_276.i_hits != 2 or prior_276.off_i_hits != 0 or len(prior_276.extra) != 0:
            self.fail("nested cycle 276 071 090 076 I-only 2/0 extra I=0 drifted")
        prior_275 = TestMamariILeftoverExtra090076RemainingAfter600Prev071Scoreboard()
        prior_275.setUp()
        prior_275.test_counts_2_of_33_and_hypothesis_k_2_holds()
        prior_275.test_survey_matches_computed_lock()
        self.assertEqual(prior_275.k_071, 2)
        self.assertEqual(CYCLE275_G, "071")
        self.assertEqual(prior_275.n_remaining_after_090_and_076_and_071, 31)
        self.assertEqual(
            prior_275.matching_previous_4grams,
            (("076", "071", "090", "076"), ("092", "071", "090", "076")),
        )
        self.assertTrue(prior_275.claim_holds)
        self.assertTrue(CYCLE275_CLAIM)
        if (
            prior_275.k_071 != 2
            or CYCLE275_G != "071"
            or prior_275.n_remaining_after_090_and_076_and_071 != 31
        ):
            self.fail(
                "nested cycle 275 leftover extra remaining-after-076 previous-071 "
                "K_071=2 N_remaining_after_090_and_076_and_071=31 drifted"
            )
        prior_274 = TestMamariI3gram076090076IOnlyScoreboard()
        prior_274.setUp()
        prior_274.test_3gram_is_one_off_i_and_not_i_only()
        prior_274.test_survey_matches_computed_lock()
        self.assertEqual(prior_274.i_hits, CYCLE274_N_I)
        self.assertEqual(prior_274.off_i_hits, CYCLE274_N_OFF_I)
        self.assertEqual(CYCLE274_N_EXTRA, 1)
        self.assertFalse(prior_274.claim_holds)
        self.assertFalse(CYCLE274_CLAIM)
        if prior_274.i_hits != 3 or prior_274.off_i_hits != 1 or CYCLE274_N_EXTRA != 1:
            self.fail("nested cycle 274 076 090 076 I-only 3/1 extra I=1 drifted")
        prior_273 = TestMamariILeftoverExtra090076RemainingAfter600Prev076Scoreboard()
        prior_273.setUp()
        prior_273.test_counts_2_of_35_and_hypothesis_k_2_holds()
        prior_273.test_survey_matches_computed_lock()
        self.assertEqual(prior_273.k_076, 2)
        self.assertEqual(CYCLE273_G, "076")
        self.assertEqual(prior_273.n_remaining_after_090_and_076, 33)
        self.assertTrue(CYCLE273_CLAIM)
        if (
            prior_273.k_076 != 2
            or CYCLE273_G != "076"
            or prior_273.n_remaining_after_090_and_076 != 33
        ):
            self.fail(
                "nested cycle 273 leftover extra remaining-after-090 previous-076 "
                "K_076=2 N_remaining_after_090_and_076=33 drifted"
            )
        prior_272 = TestMamariI3gram090090076IOnlyScoreboard()
        prior_272.setUp()
        prior_272.test_3gram_is_one_off_i_and_not_i_only()
        prior_272.test_survey_matches_computed_lock()
        self.assertEqual(prior_272.i_hits, CYCLE272_N_I)
        self.assertEqual(prior_272.off_i_hits, CYCLE272_N_OFF_I)
        self.assertEqual(CYCLE272_N_EXTRA, 1)
        self.assertFalse(prior_272.claim_holds)
        self.assertFalse(CYCLE272_CLAIM)
        if prior_272.i_hits != 3 or prior_272.off_i_hits != 1 or CYCLE272_N_EXTRA != 1:
            self.fail("nested cycle 272 090 090 076 I-only 3/1 extra I=1 drifted")
        prior_271 = TestMamariILeftoverExtra090076RemainingAfter600Previous090Scoreboard()
        prior_271.setUp()
        prior_271.test_counts_2_of_37_and_hypothesis_k_2_holds()
        prior_271.test_survey_matches_computed_lock()
        self.assertEqual(prior_271.k_090, 2)
        self.assertEqual(CYCLE271_G, "090")
        self.assertEqual(prior_271.n_remaining_after_090, 35)
        self.assertTrue(CYCLE271_CLAIM)
        if (
            prior_271.k_090 != 2
            or CYCLE271_G != "090"
            or prior_271.n_remaining_after_090 != 35
        ):
            self.fail(
                "nested cycle 271 leftover extra remaining-after-600 previous-090 "
                "K_090=2 N_remaining_after_090=35 drifted"
            )
        prior_270 = TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard()
        prior_270.setUp()
        prior_270.test_counts_37_remaining_g_090_k_2_five_way_tie_and_hypothesis_loses()
        prior_270.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_TIED_AT_K, 5)
        self.assertEqual(CYCLE270_TIED_STEMS, ("090", "076", "071", "045", "009"))
        self.assertFalse(prior_270.unique)
        self.assertFalse(prior_270.claim_holds)
        self.assertFalse(CYCLE270_CLAIM)
        if (
            CYCLE270_G != "090"
            or CYCLE270_K != 2
            or prior_270.unique
            or CYCLE270_N_TIED_AT_K != 5
        ):
            self.fail("nested cycle 270 unique-max false 5-way K=2 G=090 drifted")
        prior_269 = TestMamariI600090076Previous4gramsIOnlyScoreboard()
        prior_269.setUp()
        prior_269.test_all_4grams_are_i_only_hapax_and_claim_holds()
        prior_269.test_survey_matches_computed_lock()
        self.assertEqual(prior_269.n_i_only, 6)
        self.assertEqual(prior_269.n_not_i_only, 0)
        self.assertEqual(prior_269.n_not_hapax, 0)
        self.assertTrue(prior_269.claim_holds)
        self.assertTrue(CYCLE269_CLAIM)
        if (
            prior_269.n_i_only != 6
            or prior_269.n_not_i_only != 0
            or prior_269.n_not_hapax != 0
            or not prior_269.claim_holds
        ):
            self.fail("nested cycle 269 600 090 076 previous 4-grams 6/0 N_not_hapax=0 drifted")
        prior_268 = TestMamariI3gram600090076IOnlyScoreboard()
        prior_268.setUp()
        prior_268.test_3gram_is_zero_off_i_and_i_only()
        prior_268.test_survey_matches_computed_lock()
        self.assertEqual(prior_268.i_hits, CYCLE268_N_I)
        self.assertEqual(prior_268.off_i_hits, CYCLE268_N_OFF_I)
        self.assertEqual(CYCLE268_N_EXTRA, 2)
        self.assertTrue(prior_268.claim_holds)
        self.assertTrue(CYCLE268_CLAIM)
        if prior_268.i_hits != 6 or prior_268.off_i_hits != 0 or CYCLE268_N_EXTRA != 2:
            self.fail("nested cycle 268 600 090 076 I-only 6/0 extra I=2 drifted")
        prior_263 = TestMamariI999090076Previous4gramsIOnlyScoreboard()
        prior_263.setUp()
        prior_263.test_shared_4grams_are_i_only_not_hapax_and_claim_loses()
        prior_263.test_survey_matches_computed_lock()
        self.assertEqual(prior_263.n_i_only, 14)
        self.assertEqual(prior_263.n_not_i_only, 0)
        self.assertEqual(prior_263.n_not_hapax, 2)
        self.assertFalse(prior_263.claim_holds)
        self.assertFalse(CYCLE263_CLAIM)
        if (
            prior_263.n_i_only != 14
            or prior_263.n_not_i_only != 0
            or prior_263.n_not_hapax != 2
            or prior_263.claim_holds
        ):
            self.fail("nested cycle 263 999 090 076 previous 4-grams 14/0 N_not_hapax=2 drifted")
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
        unused_274_extra = CYCLE274_EXTRA_I_SITES
        unused_272_extra = CYCLE272_EXTRA_I_SITES
        unused_268_extra = CYCLE268_EXTRA_I_SITES
        unused_273_4grams = CYCLE273_MATCHING_PREVIOUS_4GRAMS
        unused_275_sites = CYCLE275_MATCHING_SITES
        unused_278_n = CYCLE278_N_REMAINING_AFTER_090_AND_076_AND_071
        unused_223_n = (CYCLE223_N_I, CYCLE223_N_OFF_I)
        unused_207_n = (CYCLE207_N_I, CYCLE207_N_OFF_I)
        unused_167_n = (CYCLE167_N_I, CYCLE167_N_OFF_I)
        unused_273_n = CYCLE273_N_REMAINING_AFTER_090_AND_076
        unused_276_extra = CYCLE276_EXTRA_I_SITES
        self.assertEqual(len(unused_274_extra), 1)
        self.assertEqual(len(unused_272_extra), 1)
        self.assertEqual(len(unused_268_extra), 2)
        self.assertEqual(len(unused_273_4grams), 2)
        self.assertEqual(len(unused_275_sites), 2)
        self.assertEqual(unused_278_n, 31)
        self.assertEqual(unused_223_n, (69, 3))
        self.assertEqual(unused_207_n, (8, 1))
        self.assertEqual(unused_167_n, (16, 0))
        self.assertEqual(unused_273_n, 33)
        self.assertEqual(len(unused_276_extra), 0)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_045_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE276_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE277_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE278_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE279_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE272_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE274_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-280 previous-4 I-only hapax lock."""
        lock = self.survey["i_045_090_076_previous_4grams_i_only"]
        self.assertEqual(lock["cycle"], 280)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only_hapax"])
        self.assertEqual(lock["hypothesis_all_i_only_hapax"], HYPOTHESIS_ALL_I_ONLY_HAPAX)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_I_3gram"], CYCLE279_N_I)
        self.assertEqual(lock["N_I_3gram"], 2)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE279_N_OFF_I)
        self.assertEqual(lock["N_off_I_3gram"], 0)
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle279_sites"]),
            STANDING_CYCLE279_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_extra_remaining_after_071_previous_045_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertTrue(lock["leftover_extra_remaining_after_071_previous_045_subset_of_i_sites"])
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 2)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(lock["N_distinct_4grams"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_distinct_4grams"], 2)
        self.assertEqual(
            tuple(lock["per_site_previous_stems"]),
            tuple(gram[0] for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS),
        )
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), 2)
        for row, gram, sites, cycle_sites, prev, role, n_on, n_off, hapax, off_sites in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_I_SITES,
            STANDING_CYCLE279_SITES_BY_GRAM,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_HAPAX_EACH,
            STANDING_OFF_I_SITES,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["cycle279_sites"]), cycle_sites)
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
            self.assertEqual(tuple(row["hits_by_tablet"]), STANDING_HITS_BY_TABLET_ONE_ON_I)
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
        self.assertEqual(lock["not_hapax_4grams"], [])
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_not_hapax"], STANDING_N_NOT_HAPAX)
        self.assertEqual(lock["N_i_only"], 2)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["N_not_hapax"], 0)
        self.assertEqual(lock["N_i_only_sites"], STANDING_N_I_ONLY_SITES)
        self.assertEqual(lock["N_not_i_only_sites"], STANDING_N_NOT_I_ONLY_SITES)
        self.assertEqual(lock["N_not_hapax_sites"], STANDING_N_NOT_HAPAX_SITES)
        self.assertEqual(lock["N_i_only_sites"], 2)
        self.assertEqual(lock["N_not_hapax_sites"], 0)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_045_090_076_previous_4grams_all_i_only_hapax"])
        self.assertTrue(lock["i_045_090_076_previous_4grams_all_i_only"])
        self.assertEqual(
            lock["i_045_090_076_previous_4grams_all_i_only_hapax"],
            STANDING_I_045_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX,
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
        self.assertFalse(lock["same_as_cycle263_previous_4grams"])
        self.assertFalse(lock["same_as_cycle269_previous_4grams"])
        self.assertFalse(lock["same_as_cycle277_previous_4grams"])
        self.assertFalse(lock["same_as_cycle278"])
        self.assertFalse(lock["same_as_cycle279"])
        self.assertTrue(lock["same_claim_shape_as_cycle213"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["same_claim_shape_as_cycle263"])
        self.assertTrue(lock["same_claim_shape_as_cycle269"])
        self.assertTrue(lock["same_claim_shape_as_cycle277"])
        self.assertTrue(lock["090_076_without_045_does_not_count"])
        self.assertTrue(lock["999_090_076_does_not_count"])
        self.assertTrue(lock["600_090_076_does_not_count"])
        self.assertTrue(lock["090_090_076_does_not_count"])
        self.assertTrue(lock["076_090_076_does_not_count"])
        self.assertTrue(lock["071_090_076_does_not_count"])
        self.assertTrue(lock["720_076_070_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["076_071_090_does_not_count"])
        self.assertTrue(lock["leftover_n4_020_010_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_045_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_remaining_after_045"])
        self.assertTrue(lock["do_not_peel_009"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["cycle167_not_overwritten"])
        self.assertTrue(lock["cycle276_not_overwritten"])
        self.assertTrue(lock["cycle277_not_overwritten"])
        self.assertTrue(lock["cycle278_not_retuned"])
        self.assertTrue(lock["cycle279_not_overwritten"])
        self.assertTrue(lock["cycle272_not_retuned"])
        self.assertTrue(lock["cycle274_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_045_kept"])
        self.assertEqual(lock["nested_cycle279_N_I"], 2)
        self.assertEqual(lock["nested_cycle279_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle279_N_extra"], 0)
        self.assertEqual(lock["nested_cycle278_K_045"], 2)
        self.assertEqual(lock["nested_cycle278_N_remaining_after_090_and_076_and_071"], 31)
        self.assertEqual(lock["nested_cycle278_N_remaining_after_090_and_076_and_071_and_045"], 29)
        self.assertEqual(
            [list(gram) for gram in CYCLE278_MATCHING_PREVIOUS_4GRAMS],
            lock["nested_cycle278_matching_previous_4grams"],
        )
        self.assertEqual(lock["nested_cycle277_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle277_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle277_N_not_hapax"], 0)
        self.assertTrue(lock["nested_cycle277_all_i_only_hapax"])
        self.assertEqual(lock["nested_cycle276_N_I"], 2)
        self.assertEqual(lock["nested_cycle276_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle276_N_extra"], 0)
        self.assertTrue(lock["nested_cycle276_i_only"])
        self.assertEqual(lock["nested_cycle275_K_071"], 2)
        self.assertEqual(lock["nested_cycle275_N_remaining_after_090_and_076_and_071"], 31)
        self.assertEqual(
            [list(gram) for gram in CYCLE275_MATCHING_PREVIOUS_4GRAMS],
            lock["nested_cycle275_matching_previous_4grams"],
        )
        self.assertEqual(lock["nested_cycle274_N_I"], 3)
        self.assertEqual(lock["nested_cycle274_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle274_N_extra"], 1)
        self.assertFalse(lock["nested_cycle274_i_only"])
        self.assertEqual(lock["nested_cycle273_K_076"], 2)
        self.assertEqual(lock["nested_cycle273_N_remaining_after_090_and_076"], 33)
        self.assertEqual(lock["nested_cycle272_N_I"], 3)
        self.assertEqual(lock["nested_cycle272_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle272_N_extra"], 1)
        self.assertFalse(lock["nested_cycle272_i_only"])
        self.assertEqual(lock["nested_cycle271_K_090"], 2)
        self.assertEqual(lock["nested_cycle271_N_remaining_after_090"], 35)
        self.assertFalse(lock["nested_cycle270_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle270_G"], "090")
        self.assertEqual(lock["nested_cycle270_K"], 2)
        self.assertEqual(lock["nested_cycle270_N_tied_at_K"], 5)
        self.assertEqual(tuple(lock["nested_cycle270_tied_stems_at_K"]), CYCLE270_TIED_STEMS)
        self.assertEqual(lock["nested_cycle269_N_i_only"], 6)
        self.assertEqual(lock["nested_cycle269_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle269_N_not_hapax"], 0)
        self.assertTrue(lock["nested_cycle269_all_i_only_hapax"])
        self.assertEqual(lock["nested_cycle268_N_I"], 6)
        self.assertEqual(lock["nested_cycle268_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle268_N_extra"], 2)
        self.assertEqual(lock["nested_cycle263_N_i_only"], 14)
        self.assertEqual(lock["nested_cycle263_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle263_N_not_hapax"], 2)
        self.assertFalse(lock["nested_cycle263_all_i_only_hapax"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["standing_i_3gram_045_090_076_i_only_unchanged"])
        self.assertTrue(
            lock[
                "standing_i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_remaining_after_071_previous_045_unchanged"
            ]
        )
        self.assertTrue(lock["standing_i_071_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_071_090_076_i_only_unchanged"])
        self.assertTrue(
            lock[
                "standing_i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_previous_071_unchanged"
            ]
        )
        self.assertTrue(lock["standing_i_3gram_076_090_076_i_only_unchanged"])
        self.assertTrue(
            lock[
                "standing_i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076_unchanged"
            ]
        )
        self.assertTrue(lock["standing_i_3gram_090_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_090_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_600_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_600_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_999_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_720_076_070_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_045_090_076_i_only"]["cycle"], 279)
        self.assertTrue(self.survey["i_3gram_045_090_076_i_only"]["i_3gram_045_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_045_090_076_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_045_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_045_090_076_i_only"]["N_extra"], 0)
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_remaining_after_071_previous_045"
            ]["cycle"],
            278,
        )
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_remaining_after_071_previous_045"
            ]["K_045"],
            2,
        )
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_remaining_after_071_previous_045"
            ]["N_remaining_after_090_and_076_and_071_and_045"],
            29,
        )
        self.assertEqual(self.survey["i_071_090_076_previous_4grams_i_only"]["cycle"], 277)
        self.assertTrue(
            self.survey["i_071_090_076_previous_4grams_i_only"][
                "i_071_090_076_previous_4grams_all_i_only_hapax"
            ]
        )
        self.assertEqual(self.survey["i_071_090_076_previous_4grams_i_only"]["N_i_only"], 2)
        self.assertEqual(self.survey["i_071_090_076_previous_4grams_i_only"]["N_not_hapax"], 0)
        self.assertEqual(self.survey["i_3gram_071_090_076_i_only"]["cycle"], 276)
        self.assertTrue(self.survey["i_3gram_071_090_076_i_only"]["i_3gram_071_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_071_090_076_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_071_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_071_090_076_i_only"]["N_extra"], 0)
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_previous_071"
            ]["cycle"],
            275,
        )
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_previous_071"
            ]["K_071"],
            2,
        )
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_previous_071"
            ]["N_remaining_after_090_and_076_and_071"],
            31,
        )
        self.assertEqual(self.survey["i_3gram_076_090_076_i_only"]["cycle"], 274)
        self.assertEqual(self.survey["i_3gram_076_090_076_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_076_090_076_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_076_090_076_i_only"]["N_extra"], 1)
        self.assertFalse(self.survey["i_3gram_076_090_076_i_only"]["i_3gram_076_090_076_i_only"])
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"
            ]["cycle"],
            273,
        )
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"
            ]["K_076"],
            2,
        )
        self.assertEqual(
            self.survey[
                "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_previous_076"
            ]["N_remaining_after_090_and_076"],
            33,
        )
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["cycle"], 272)
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_090_090_076_i_only"]["N_extra"], 1)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]["cycle"],
            271,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]["K_090"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"][
                "N_remaining_after_090"
            ],
            35,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["cycle"],
            270,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["G"],
            "090",
        )
        self.assertEqual(self.survey["i_600_090_076_previous_4grams_i_only"]["cycle"], 269)
        self.assertTrue(
            self.survey["i_600_090_076_previous_4grams_i_only"][
                "i_600_090_076_previous_4grams_all_i_only_hapax"
            ]
        )
        self.assertEqual(self.survey["i_600_090_076_previous_4grams_i_only"]["N_i_only"], 6)
        self.assertEqual(self.survey["i_600_090_076_previous_4grams_i_only"]["N_not_hapax"], 0)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["cycle"], 268)
        self.assertTrue(self.survey["i_3gram_600_090_076_i_only"]["i_3gram_600_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_extra"], 2)
        self.assertEqual(self.survey["i_999_090_076_previous_4grams_i_only"]["cycle"], 263)
        self.assertFalse(
            self.survey["i_999_090_076_previous_4grams_i_only"][
                "i_999_090_076_previous_4grams_all_i_only_hapax"
            ]
        )
        self.assertEqual(self.survey["i_999_090_076_previous_4grams_i_only"]["N_i_only"], 14)
        self.assertEqual(self.survey["i_999_090_076_previous_4grams_i_only"]["N_not_hapax"], 2)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
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


class TestMamariI045090076Previous4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 280 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
