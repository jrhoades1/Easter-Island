"""I's cycle-231 leftover extra remaining-after-001 next-stem lock.

Cycle 234 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Leftover extra remaining-after-001 = leftover extra I 090 076
sites with a next token whose next token is none of 070, 071,
013, or 001. Nested-check leftover extra N_leftover==56,
N_with_next==55, N_no_next==1 at Ia4[166], leftover extra
exactly 8 share 070, leftover extra remaining N_remaining==47
G=071 K=6, leftover extra remaining-after-071 N_remaining2==41
G=013 K=5, leftover extra remaining-after-013 N_remaining3==36
G=001 K=3 (do not retune cycles 225–231). Nested-check cycle
232 090 076 001 I-only 3/0 and cycle 233 three forward 4-grams
1/0 each (do not retune). Nested-check N_remaining4==33
(36−3). Ia2[174] has next token 000 and is remaining-after-001;
it is not no-next. Off-I T sites are not this cycle. I-only of
090 076 G is leftover-of-leftover for a later cycle if K≥2.
Previous 4-grams of 090 076 001 are not this cycle. 076 071
and 076 070 do not count as this 2-gram. Inside-family sites
do not count as leftover extra.

Among remaining-after-001, G = the next stem with the highest
remaining-after-001 count. If a tie, pick the larger Barthel
id. K = that count. Measured: N_remaining4=33,
N_distinct_remaining4=26, G=700 by larger-id tie-break among
seven stems at count 2 (530/280/087/011/005/000 also ×2),
K=2 at Ia2[159], Ia13[143]. Cycle 231 reported next-after-G
as 700×2; measure it, do not assume it. Claim that can lose:
i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G.
True iff leftover extra 56/55/8 stay, leftover extra remaining
47/6/071 stay, leftover extra remaining-after-071 41/5/013
stay, leftover extra remaining-after-013 36/3/001 stay,
N_remaining4==33, G is uniquely most frequent under the
tie-break, and exactly K remaining-after-001 sites share G.
The claim is false: N_remaining4==33 holds and the remaining-
after-001 filter agrees with nested 36−3, but G is not
uniquely most frequent (7-way tie at K=2). Same claim-shape
as cycle 231 (leftover extra remaining-after-013 exactly 3
share 001), cycle 228 (leftover extra remaining-after-071
exactly 5 share 013), cycle 227 (leftover extra remaining
exactly 6 share 071), and cycle 226 (leftover extra exactly 8
share forward 070). This can lose if N_remaining4 ≠ 33 or the
leftover extra remaining-after-001 filter disagrees with
nested counts. Nested cycle 233 3/0 hapax, cycle 232 3/0,
cycle 230 5/0 hapax, cycle 229 5/0, cycle 223 69/3, cycle
195 6/0, and cycle 171 43/0 stay. Do not assume the result;
measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_001_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_001_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE233_CLAIM,
    STANDING_N_I_ONLY as CYCLE233_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE233_N_NOT_I_ONLY,
    TestMamariI090076001Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_013_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE230_CLAIM,
    STANDING_N_I_ONLY as CYCLE230_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE230_N_NOT_I_ONLY,
    TestMamariI090076013Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
    leftover_local_4grams,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_OFF_I,
    STANDING_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_001_i_only_scoreboard import (
    GRAM3 as CYCLE232_GRAM3,
    STANDING_I_3GRAM_090_076_001_I_ONLY as CYCLE232_CLAIM,
    STANDING_I_SITES as CYCLE232_I_SITES,
    STANDING_N_I as CYCLE232_N_I,
    STANDING_N_OFF_I as CYCLE232_N_OFF_I,
    TestMamariI3gram090076001IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_013_i_only_scoreboard import (
    GRAM3 as CYCLE229_GRAM3,
    STANDING_I_3GRAM_090_076_013_I_ONLY as CYCLE229_CLAIM,
    STANDING_I_SITES as CYCLE229_I_SITES,
    STANDING_N_I as CYCLE229_N_I,
    STANDING_N_OFF_I as CYCLE229_N_OFF_I,
    TestMamariI3gram090076013IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
    STANDING_I_3GRAM_090_076_071_I_ONLY as CYCLE195_CLAIM,
    STANDING_I_SITES as CYCLE195_I_SITES,
    STANDING_N_I as CYCLE195_N_I,
    STANDING_N_OFF_I as CYCLE195_N_OFF_I,
    TestMamariI3gram090076071IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_070_scoreboard import (
    STANDING_G as CYCLE226_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070 as CYCLE226_CLAIM,
    STANDING_K as CYCLE226_K,
    STANDING_MATCHING_SITES as CYCLE226_MATCHING_SITES,
    STANDING_N_LEFTOVER as CYCLE226_N_LEFTOVER,
    STANDING_N_NO_NEXT as CYCLE226_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE226_N_WITH_NEXT,
    leftover_extra_with_forward_070,
    TestMamariILeftoverExtra090076Forward070Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE225_G,
    STANDING_G_SITES as CYCLE225_G_SITES,
    STANDING_IA2_174,
    STANDING_IA2_174_NEXT_STEM,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_K as CYCLE225_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE225_N_LEFTOVER,
    STANDING_N_NO_NEXT as CYCLE225_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE225_N_WITH_NEXT,
    STANDING_NO_NEXT_SITES,
    group_sites_by_next_stem,
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
    leftover_sites_with_next,
    leftover_sites_without_next,
    site_next_stem,
    TestMamariILeftoverExtra090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_013_next_stem_scoreboard import (
    STANDING_G as CYCLE231_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_013_EXACTLY_K_SHARE_G as CYCLE231_CLAIM,
    STANDING_K as CYCLE231_K,
    STANDING_MATCHING_SITES as CYCLE231_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING3 as CYCLE231_N_DISTINCT,
    STANDING_N_REMAINING3 as CYCLE231_N_REMAINING3,
    STANDING_N_SHARE_013 as CYCLE231_N_SHARE_013,
    STANDING_N_WITHOUT_G as CYCLE231_N_WITHOUT_G,
    STANDING_REMAINING3_SITES as CYCLE231_REMAINING3_SITES,
    leftover_extra_remaining_after_013,
    leftover_extra_remaining_after_013_nested_counts_hold,
    leftover_extra_remaining_after_013_next_stems,
    leftover_extra_remaining_after_013_with_g,
    leftover_extra_remaining_after_013_without_g,
    TestMamariILeftoverExtra090076RemainingAfter013NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_071_next_stem_scoreboard import (
    STANDING_G as CYCLE228_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G as CYCLE228_CLAIM,
    STANDING_K as CYCLE228_K,
    STANDING_MATCHING_SITES as CYCLE228_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING2 as CYCLE228_N_DISTINCT,
    STANDING_N_REMAINING2 as CYCLE228_N_REMAINING2,
    STANDING_N_SHARE_071 as CYCLE228_N_SHARE_071,
    STANDING_N_WITHOUT_G as CYCLE228_N_WITHOUT_G,
    STANDING_REMAINING2_SITES as CYCLE228_REMAINING2_SITES,
    leftover_extra_remaining_after_071,
    leftover_extra_remaining_after_071_with_g,
    leftover_extra_remaining_after_071_without_g,
    TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    STANDING_G as CYCLE227_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 as CYCLE227_CLAIM,
    STANDING_K as CYCLE227_K,
    STANDING_MATCHING_SITES as CYCLE227_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE227_N_DISTINCT,
    STANDING_N_REMAINING as CYCLE227_N_REMAINING,
    STANDING_N_SHARE_070 as CYCLE227_N_SHARE_070,
    STANDING_N_WITHOUT_G as CYCLE227_N_WITHOUT_G,
    STANDING_REMAINING_SITES as CYCLE227_REMAINING_SITES,
    barthel_id,
    leftover_extra_nested_counts_hold,
    leftover_extra_remaining,
    leftover_extra_remaining_next_stems,
    leftover_extra_remaining_with_g,
    leftover_extra_remaining_without_g,
    TestMamariILeftoverExtra090076RemainingNextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    TestMamariILeftoverN4RemainingNext2gramScoreboard,
    i_leftover_n4_remaining_exactly_5_contain_090_076,
    leftover_n4_family_counts_hold,
    leftover_n4_rows,
    leftover_remaining_n4,
    leftover_remaining_with_g,
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
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_K = 2
LOCKED_FORWARD_STEM_070 = "070"
LOCKED_FORWARD_STEM_071 = "071"
LOCKED_FORWARD_STEM_013 = "013"
LOCKED_FORWARD_STEM_001 = "001"
LOCKED_FORWARD_STEMS = (
    LOCKED_FORWARD_STEM_070,
    LOCKED_FORWARD_STEM_071,
    LOCKED_FORWARD_STEM_013,
    LOCKED_FORWARD_STEM_001,
)
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "700")
GRAM3_NESTED_001 = ("090", "076", "001")
GRAM3_NESTED_013 = ("090", "076", "013")
GRAM3_NESTED_071 = ("090", "076", "071")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_WITH_NEXT = 55
STANDING_N_NO_NEXT = 1
STANDING_N_SHARE_070 = 8
STANDING_N_REMAINING = 47
STANDING_N_SHARE_071 = 6
STANDING_N_REMAINING2 = 41
STANDING_N_SHARE_013 = 5
STANDING_N_REMAINING3 = 36
STANDING_N_SHARE_001 = 3
STANDING_N_REMAINING4 = 33
STANDING_N_DISTINCT_REMAINING4 = 26
STANDING_N_HAPAX_REMAINING4 = 19
STANDING_G = "700"
STANDING_K = 2
STANDING_N_WITHOUT_G = 31
STANDING_N_NEXT_AFTER_G = 2
STANDING_N_NEXT_AFTER_G_STEM = "530"
STANDING_N_TIED_AT_K = 7
STANDING_TIED_STEMS = ("700", "530", "280", "087", "011", "005", "000")
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_REMAINING4_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
    (SIDE_IA, "Ia2", 159),
    (SIDE_IA, "Ia2", 165),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia3", 71),
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia7", 2),
    (SIDE_IA, "Ia7", 113),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 42),
    (SIDE_IA, "Ia12", 47),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 109),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia13", 143),
    (SIDE_IA, "Ia14", 9),
    (SIDE_IA, "Ia14", 177),
)
STANDING_REMAINING4_NEXT_STEMS = (
    "012",
    "175",
    "755",
    "470",
    "430",
    "600",
    "011",
    "384",
    "535",
    "050",
    "700",
    "147",
    "000",
    "005",
    "087",
    "090",
    "386",
    "087",
    "505",
    "280",
    "280",
    "607",
    "057",
    "072",
    "000",
    "530",
    "011",
    "300",
    "005",
    "255",
    "700",
    "530",
    "670",
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia2", 159),
    (SIDE_IA, "Ia13", 143),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "700", "011"),
    ("090", "076", "700", "076"),
)
STANDING_REMAINING4_FREQUENCY = (
    (
        "700",
        2,
        ((SIDE_IA, "Ia2", 159), (SIDE_IA, "Ia13", 143)),
        (("090", "076", "700"), ("090", "076", "700")),
    ),
    (
        "530",
        2,
        ((SIDE_IA, "Ia12", 42), (SIDE_IA, "Ia14", 9)),
        (("090", "076", "530"), ("090", "076", "530")),
    ),
    (
        "280",
        2,
        ((SIDE_IA, "Ia7", 2), (SIDE_IA, "Ia7", 113)),
        (("090", "076", "280"), ("090", "076", "280")),
    ),
    (
        "087",
        2,
        ((SIDE_IA, "Ia3", 87), (SIDE_IA, "Ia4", 162)),
        (("090", "076", "087"), ("090", "076", "087")),
    ),
    (
        "011",
        2,
        ((SIDE_IA, "Ia2", 37), (SIDE_IA, "Ia12", 47)),
        (("090", "076", "011"), ("090", "076", "011")),
    ),
    (
        "005",
        2,
        ((SIDE_IA, "Ia3", 71), (SIDE_IA, "Ia13", 109)),
        (("090", "076", "005"), ("090", "076", "005")),
    ),
    (
        "000",
        2,
        ((SIDE_IA, "Ia2", 174), (SIDE_IA, "Ia10", 141)),
        (("090", "076", "000"), ("090", "076", "000")),
    ),
    ("755", 1, ((SIDE_IA, "Ia1", 27),), (("090", "076", "755"),)),
    ("670", 1, ((SIDE_IA, "Ia14", 177),), (("090", "076", "670"),)),
    ("607", 1, ((SIDE_IA, "Ia7", 137),), (("090", "076", "607"),)),
    ("600", 1, ((SIDE_IA, "Ia2", 14),), (("090", "076", "600"),)),
    ("535", 1, ((SIDE_IA, "Ia2", 128),), (("090", "076", "535"),)),
    ("505", 1, ((SIDE_IA, "Ia5", 127),), (("090", "076", "505"),)),
    ("470", 1, ((SIDE_IA, "Ia1", 59),), (("090", "076", "470"),)),
    ("430", 1, ((SIDE_IA, "Ia1", 96),), (("090", "076", "430"),)),
    ("386", 1, ((SIDE_IA, "Ia4", 121),), (("090", "076", "386"),)),
    ("384", 1, ((SIDE_IA, "Ia2", 114),), (("090", "076", "384"),)),
    ("300", 1, ((SIDE_IA, "Ia12", 150),), (("090", "076", "300"),)),
    ("255", 1, ((SIDE_IA, "Ia13", 135),), (("090", "076", "255"),)),
    ("175", 1, ((SIDE_IA, "Ia1", 15),), (("090", "076", "175"),)),
    ("147", 1, ((SIDE_IA, "Ia2", 165),), (("090", "076", "147"),)),
    ("090", 1, ((SIDE_IA, "Ia4", 84),), (("090", "076", "090"),)),
    ("072", 1, ((SIDE_IA, "Ia10", 137),), (("090", "076", "072"),)),
    ("057", 1, ((SIDE_IA, "Ia9", 129),), (("090", "076", "057"),)),
    ("050", 1, ((SIDE_IA, "Ia2", 154),), (("090", "076", "050"),)),
    ("012", 1, ((SIDE_IA, "Ia1", 2),), (("090", "076", "012"),)),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G"
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G = False
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_001_next_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE222 = False
STANDING_SAME_AS_CYCLE226 = False
STANDING_SAME_AS_CYCLE227 = False
STANDING_SAME_AS_CYCLE228 = False
STANDING_SAME_AS_CYCLE229 = False
STANDING_SAME_AS_CYCLE230 = False
STANDING_SAME_AS_CYCLE231 = False
STANDING_SAME_AS_CYCLE232 = False
STANDING_SAME_AS_CYCLE233 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE227 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE228 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE231 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_4GRAMS_OF_090_076_001_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN = True


def leftover_extra_remaining_after_001(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra with-next sites whose next token is not 070, 071, 013, or 001."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_001_next_stems(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[str, ...]:
    """Next stems of leftover extra remaining-after-001 sites."""
    locked_set = set(locked)
    return tuple(
        nxt
        for nxt in next_stems
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_001_with_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-001 sites whose next token is G."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem
    )


def leftover_extra_remaining_after_001_without_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-001 sites whose next token is not G."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set and nxt != stem
    )


def remaining_after_001_next_stem_counts(next_stems: tuple[str, ...]) -> Counter:
    """Counts of next stems among leftover extra remaining-after-001."""
    return Counter(next_stems)


def rank_remaining_after_001_next_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining-after-001 next stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_after_001_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining-after-001 has no G."""
    ranked = rank_remaining_after_001_next_stems(
        remaining_after_001_next_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_after_001_next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    forward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining-after-001 next-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_extra_remaining_after_001(sites, next_stems, locked)
    rem_stems = leftover_extra_remaining_after_001_next_stems(sites, next_stems, locked)
    locked_set = set(locked)
    rem_grams = tuple(
        gram
        for nxt, gram in zip(next_stems, forward_3grams, strict=True)
        if nxt is not None and nxt not in locked_set
    )
    first_seen = group_sites_by_next_stem(rem_sites, rem_stems)
    grams_by_stem: dict[str, list[tuple[str, ...]]] = {
        stem: [] for stem, _ in first_seen
    }
    for nxt, gram in zip(rem_stems, rem_grams, strict=True):
        if gram is not None:
            grams_by_stem[nxt].append(gram)
    rows = tuple(
        (stem, len(stem_sites), stem_sites, tuple(grams_by_stem[stem]))
        for stem, stem_sites in first_seen
    )
    return tuple(sorted(rows, key=lambda row: (-row[1], -barthel_id(row[0]))))


def remaining_after_001_next_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING4_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining-after-001 next-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "next_stem": stem,
                "count": count,
                "leftover_extra_remaining_after_001_sites": [
                    list(site) for site in sites
                ],
                "forward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def matching_leftover_extra_remaining_after_001_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-001 next-4-gram rows."""
    rows = []
    for (side, line, index), next_gram in zip(
        leftover_sites,
        next_4grams,
        strict=True,
    ):
        rows.append(
            {
                "tablet": "I",
                "side": side,
                "line": line,
                "index": index,
                "next_4gram": list(next_gram),
                "forward_3gram": list(next_gram[:3]),
            }
        )
    return rows


def leftover_extra_remaining_after_001_nested_counts_hold(
    n_leftover: int,
    n_with_next: int,
    n_no_next: int,
    n_share_070: int,
    n_remaining: int,
    n_share_071: int,
    n_remaining2: int,
    n_share_013: int,
    n_remaining3: int,
    n_share_001: int,
    n_remaining4: int,
    expected_leftover: int = STANDING_N_LEFTOVER,
    expected_with_next: int = STANDING_N_WITH_NEXT,
    expected_no_next: int = STANDING_N_NO_NEXT,
    expected_share_070: int = STANDING_N_SHARE_070,
    expected_remaining: int = STANDING_N_REMAINING,
    expected_share_071: int = STANDING_N_SHARE_071,
    expected_remaining2: int = STANDING_N_REMAINING2,
    expected_share_013: int = STANDING_N_SHARE_013,
    expected_remaining3: int = STANDING_N_REMAINING3,
    expected_share_001: int = STANDING_N_SHARE_001,
    expected_remaining4: int = STANDING_N_REMAINING4,
) -> bool:
    """Nested leftover extra 56/55/1, 8/070, 47/6/071, 41/5/013, 36/3/001, remaining4=33."""
    return (
        leftover_extra_remaining_after_013_nested_counts_hold(
            n_leftover,
            n_with_next,
            n_no_next,
            n_share_070,
            n_remaining,
            n_share_071,
            n_remaining2,
            n_share_013,
            n_remaining3,
            expected_leftover,
            expected_with_next,
            expected_no_next,
            expected_share_070,
            expected_remaining,
            expected_share_071,
            expected_remaining2,
            expected_share_013,
            expected_remaining3,
        )
        and n_share_001 == expected_share_001
        and n_remaining4 == expected_remaining4
        and n_remaining4 == n_remaining3 - n_share_001
        and n_remaining3 == n_remaining2 - n_share_013
        and n_remaining2 == n_remaining - n_share_071
        and n_remaining == n_with_next - n_share_070
    )


def i_leftover_extra_090_076_remaining_after_001_exactly_k_share_g(
    leftover_sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    expected_g: str = STANDING_G,
    expected_k: int = HYPOTHESIS_K,
    expected_remaining4: int = STANDING_N_REMAINING4,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> bool:
    """True iff remaining4=33, G is unique max, and exactly K share G."""
    with_next = leftover_sites_with_next(leftover_sites, next_stems)
    no_next = leftover_sites_without_next(leftover_sites, next_stems)
    share_070 = leftover_extra_with_forward_070(leftover_sites, next_stems)
    remaining = leftover_extra_remaining(leftover_sites, next_stems)
    share_071 = leftover_extra_remaining_with_g(
        leftover_sites,
        next_stems,
        LOCKED_FORWARD_STEM_071,
    )
    remaining2 = leftover_extra_remaining_after_071(leftover_sites, next_stems)
    share_013 = leftover_extra_remaining_after_071_with_g(
        leftover_sites,
        next_stems,
        LOCKED_FORWARD_STEM_013,
    )
    remaining3 = leftover_extra_remaining_after_013(leftover_sites, next_stems)
    share_001 = leftover_extra_remaining_after_013_with_g(
        leftover_sites,
        next_stems,
        LOCKED_FORWARD_STEM_001,
    )
    remaining4 = leftover_extra_remaining_after_001(leftover_sites, next_stems, locked)
    rem4_stems = leftover_extra_remaining_after_001_next_stems(
        leftover_sites,
        next_stems,
        locked,
    )
    if not leftover_extra_remaining_after_001_nested_counts_hold(
        len(leftover_sites),
        len(with_next),
        len(no_next),
        len(share_070),
        len(remaining),
        len(share_071),
        len(remaining2),
        len(share_013),
        len(remaining3),
        len(share_001),
        len(remaining4),
    ):
        return False
    if len(remaining4) != expected_remaining4:
        return False
    if remaining4 != leftover_extra_remaining_after_013_without_g(
        leftover_sites,
        next_stems,
        LOCKED_FORWARD_STEM_001,
    ):
        return False
    gram, count, unique = select_remaining_after_001_g(rem4_stems)
    if not unique or gram != expected_g or count != expected_k:
        return False
    return (
        len(
            leftover_extra_remaining_after_001_with_g(
                leftover_sites,
                next_stems,
                gram,
            )
        )
        == expected_k
    )


class TestILeftoverExtra090076RemainingAfter001NextStemHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-001 next stems. No CV, no LLM."""

    def test_remaining_after_001_requires_with_next_not_070_071_013_001(self):
        """Remaining-after-001 excludes no-next and the locked 070/071/013/001 clusters."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "700"))
        self.assertEqual(GRAM3_NESTED_001, ("090", "076", "001"))
        self.assertEqual(GRAM3_NESTED_013, ("090", "076", "013"))
        self.assertEqual(GRAM3_NESTED_071, ("090", "076", "071"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("070", "071", "013", "001"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_700 = ["999", "090", "076", "700", "011"]
        self.assertEqual(site_next_stem(has_700, 1, GRAM2), "700")
        self.assertEqual(site_forward_3gram(has_700, 1, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_700, 1, GRAM2),
            ("090", "076", "700", "011"),
        )
        has_001 = ["999", "090", "076", "001", "048"]
        self.assertEqual(site_next_stem(has_001, 1, GRAM2), "001")
        self.assertNotEqual(site_next_stem(has_001, 1, GRAM2), "700")
        has_013 = ["999", "090", "076", "013", "073"]
        self.assertEqual(site_next_stem(has_013, 1, GRAM2), "013")
        self.assertNotEqual(site_next_stem(has_013, 1, GRAM2), "700")
        has_071 = ["999", "090", "076", "071", "633"]
        self.assertEqual(site_next_stem(has_071, 1, GRAM2), "071")
        self.assertNotEqual(site_next_stem(has_071, 1, GRAM2), "700")
        has_070 = ["999", "090", "076", "070", "499"]
        self.assertEqual(site_next_stem(has_070, 1, GRAM2), "070")
        self.assertNotEqual(site_next_stem(has_070, 1, GRAM2), "700")
        end_of_line = ["087", "078", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        one_token_then_eol = ["009", "009", "090", "076", "000"]
        self.assertEqual(site_next_stem(one_token_then_eol, 2, GRAM2), "000")
        self.assertIsNone(site_next_4gram(one_token_then_eol, 2, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
            (SIDE_IA, "Ia1", 5),
            (SIDE_IA, "Ia1", 6),
        )
        planted_stems = ("700", "070", "071", "013", "001", None, "530")
        self.assertEqual(
            leftover_extra_remaining_after_001(planted_sites, planted_stems),
            (planted_sites[0], planted_sites[6]),
        )
        self.assertEqual(
            leftover_extra_remaining_after_001_next_stems(planted_sites, planted_stems),
            ("700", "530"),
        )
        self.assertNotIn(
            planted_sites[1],
            leftover_extra_remaining_after_001(planted_sites, planted_stems),
        )
        self.assertNotIn(
            planted_sites[2],
            leftover_extra_remaining_after_001(planted_sites, planted_stems),
        )
        self.assertNotIn(
            planted_sites[3],
            leftover_extra_remaining_after_001(planted_sites, planted_stems),
        )
        self.assertNotIn(
            planted_sites[4],
            leftover_extra_remaining_after_001(planted_sites, planted_stems),
        )
        self.assertNotIn(
            planted_sites[5],
            leftover_extra_remaining_after_001(planted_sites, planted_stems),
        )
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_k_can_fail(self):
        """Boolean is True only when remaining4=33, unique G=700, K=2."""
        provider = MockProvider()
        leftover = STANDING_LEFTOVER_SITES
        stems = leftover_extra_next_stems(load_i_sides(), leftover, GRAM2)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_001_exactly_k_share_g(
                leftover,
                stems,
            )
        )
        rem4 = leftover_extra_remaining_after_001(leftover, stems)
        rem4_stems = leftover_extra_remaining_after_001_next_stems(leftover, stems)
        self.assertEqual(len(rem4), STANDING_N_REMAINING4)
        self.assertEqual(len(rem4), 33)
        self.assertEqual(rem4, STANDING_REMAINING4_SITES)
        self.assertEqual(rem4_stems, STANDING_REMAINING4_NEXT_STEMS)
        g, k, unique = select_remaining_after_001_g(rem4_stems)
        self.assertEqual(g, "700")
        self.assertEqual(k, 2)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = (None,) * len(leftover)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_001_exactly_k_share_g(
                leftover,
                empty_stems,
            )
        )
        planted = leftover + ((SIDE_IA, "Ia1", 0),)
        planted_stems = stems + ("700",)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_001_exactly_k_share_g(
                planted,
                planted_stems,
            )
        )
        make_001 = tuple("001" if nxt == "700" else nxt for nxt in stems)
        self.assertEqual(len(leftover_extra_remaining_after_001(leftover, make_001)), 31)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_001_exactly_k_share_g(
                leftover,
                make_001,
            )
        )
        unique_700 = list(stems)
        demotions = {
            (SIDE_IA, "Ia12", 42): "801",
            (SIDE_IA, "Ia7", 2): "802",
            (SIDE_IA, "Ia3", 87): "803",
            (SIDE_IA, "Ia2", 37): "804",
            (SIDE_IA, "Ia3", 71): "805",
            (SIDE_IA, "Ia2", 174): "806",
        }
        for i, site in enumerate(leftover):
            if site in demotions:
                unique_700[i] = demotions[site]
        unique_stems = tuple(unique_700)
        uniq_g, uniq_k, uniq_unique = select_remaining_after_001_g(
            leftover_extra_remaining_after_001_next_stems(leftover, unique_stems)
        )
        self.assertEqual(uniq_g, "700")
        self.assertEqual(uniq_k, 2)
        self.assertTrue(uniq_unique)
        self.assertEqual(len(leftover_extra_remaining_after_001(leftover, unique_stems)), 33)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_001_exactly_k_share_g(
                leftover,
                unique_stems,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G",
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G
        )
        self.assertEqual(HYPOTHESIS_K, STANDING_K)
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING4)
        self.assertEqual(2 + 31, 33)
        self.assertEqual(
            STANDING_N_REMAINING3 - STANDING_N_SHARE_001,
            STANDING_N_REMAINING4,
        )
        self.assertEqual(36 - 3, 33)
        self.assertEqual(CYCLE231_N_WITHOUT_G, STANDING_N_REMAINING4)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_001_ARE_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining-after-001 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"700": 2, "530": 2, "000": 2})
        ranked = rank_remaining_after_001_next_stems(counts)
        self.assertEqual(ranked[0], ("700", 2))
        self.assertEqual(ranked[1], ("530", 2))
        self.assertEqual(ranked[2], ("000", 2))
        self.assertEqual(
            select_remaining_after_001_g(
                ("700", "530", "700", "530")
            )[0],
            "700",
        )
        self.assertFalse(
            select_remaining_after_001_g(
                ("700", "530", "700", "530")
            )[2]
        )
        self.assertEqual(select_remaining_after_001_g(("005", "700", "005", "700"))[0], "700")
        self.assertFalse(select_remaining_after_001_g(("005", "700", "005", "700"))[2])
        self.assertEqual(select_remaining_after_001_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE227)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE228)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE231)
        self.assertFalse(STANDING_SAME_AS_CYCLE222)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE227)
        self.assertFalse(STANDING_SAME_AS_CYCLE228)
        self.assertFalse(STANDING_SAME_AS_CYCLE231)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-001 next-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.next_stems = leftover_extra_next_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.forwards = leftover_extra_forward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.with_next = leftover_sites_with_next(self.leftover_sites, self.next_stems)
        self.no_next = leftover_sites_without_next(self.leftover_sites, self.next_stems)
        self.share_070 = leftover_extra_with_forward_070(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining = leftover_extra_remaining(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_071 = leftover_extra_remaining_with_g(
            self.leftover_sites,
            self.next_stems,
            LOCKED_FORWARD_STEM_071,
        )
        self.remaining2 = leftover_extra_remaining_after_071(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_013 = leftover_extra_remaining_after_071_with_g(
            self.leftover_sites,
            self.next_stems,
            LOCKED_FORWARD_STEM_013,
        )
        self.remaining3 = leftover_extra_remaining_after_013(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_001 = leftover_extra_remaining_after_013_with_g(
            self.leftover_sites,
            self.next_stems,
            LOCKED_FORWARD_STEM_001,
        )
        self.remaining4 = leftover_extra_remaining_after_001(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining4_stems = leftover_extra_remaining_after_001_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.matching = leftover_extra_remaining_after_001_with_g(
            self.leftover_sites,
            self.next_stems,
        )
        self.without = leftover_extra_remaining_after_001_without_g(
            self.leftover_sites,
            self.next_stems,
        )
        self.frequency = remaining_after_001_next_stem_frequency_table(
            self.leftover_sites,
            self.next_stems,
            self.forwards,
        )
        self.matching_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = CYCLE224_N_INSIDE
        self.n_leftover = len(self.leftover_sites)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.n_share_070 = len(self.share_070)
        self.n_remaining = len(self.remaining)
        self.n_share_071 = len(self.share_071)
        self.n_remaining2 = len(self.remaining2)
        self.n_share_013 = len(self.share_013)
        self.n_remaining3 = len(self.remaining3)
        self.n_share_001 = len(self.share_001)
        self.n_remaining4 = len(self.remaining4)
        self.n_distinct_remaining4 = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_after_001_g(self.remaining4_stems)
        self.n_without = len(self.without)
        self.claim_holds = i_leftover_extra_090_076_remaining_after_001_exactly_k_share_g(
            self.leftover_sites,
            self.next_stems,
        )

    def test_tokens_and_nested_leftover_extra_56_55_8_47_6_071_41_5_013_36_3_001_not_retuned(
        self,
    ):
        """2-gram and leftover extra 56/55/1 / 8/070 / 47/6/071 / 41/5/013 / 36/3/001 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "700"))
        self.assertEqual(GRAM3_NESTED_001, ("090", "076", "001"))
        self.assertEqual(GRAM3_NESTED_001, CYCLE232_GRAM3)
        self.assertEqual(GRAM3_NESTED_013, ("090", "076", "013"))
        self.assertEqual(GRAM3_NESTED_013, CYCLE229_GRAM3)
        self.assertEqual(GRAM3_NESTED_071, ("090", "076", "071"))
        self.assertEqual(GRAM3_NESTED_071, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM3_FORWARD, CYCLE207_GRAM3)
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_i, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE225_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE226_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_233 = self.survey["i_090_076_001_forward_4grams_i_only"]
        self.assertEqual(prior_233["cycle"], 233)
        self.assertEqual(prior_233["N_I"], 3)
        self.assertEqual(prior_233["N_i_only"], 3)
        self.assertEqual(prior_233["N_not_i_only"], 0)
        self.assertTrue(prior_233["i_090_076_001_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE233_CLAIM)
        self.assertEqual(CYCLE233_N_I_ONLY, 3)
        self.assertEqual(CYCLE233_N_NOT_I_ONLY, 0)
        prior_232 = self.survey["i_3gram_090_076_001_i_only"]
        self.assertEqual(prior_232["cycle"], 232)
        self.assertEqual(prior_232["N_I"], 3)
        self.assertEqual(prior_232["N_off_I"], 0)
        self.assertTrue(prior_232["i_3gram_090_076_001_i_only"])
        self.assertTrue(CYCLE232_CLAIM)
        self.assertEqual(CYCLE232_N_I, 3)
        self.assertEqual(CYCLE232_N_OFF_I, 0)
        prior_231 = self.survey["i_leftover_extra_090_076_remaining_after_013_next_stem"]
        self.assertEqual(prior_231["cycle"], 231)
        self.assertEqual(prior_231["N_leftover"], 56)
        self.assertEqual(prior_231["N_with_next"], 55)
        self.assertEqual(prior_231["N_no_next"], 1)
        self.assertEqual(prior_231["N_share_070"], 8)
        self.assertEqual(prior_231["N_remaining"], 47)
        self.assertEqual(prior_231["N_share_071"], 6)
        self.assertEqual(prior_231["N_remaining2"], 41)
        self.assertEqual(prior_231["N_share_013"], 5)
        self.assertEqual(prior_231["N_remaining3"], 36)
        self.assertEqual(prior_231["G"], "001")
        self.assertEqual(prior_231["K"], 3)
        self.assertEqual(prior_231["N_without_G"], 33)
        self.assertEqual(prior_231["next_after_G"], "700")
        self.assertEqual(prior_231["N_next_after_G"], 2)
        self.assertTrue(prior_231["i_leftover_extra_090_076_remaining_after_013_exactly_K_share_G"])
        self.assertTrue(CYCLE231_CLAIM)
        self.assertEqual(CYCLE231_G, "001")
        self.assertEqual(CYCLE231_K, 3)
        self.assertEqual(CYCLE231_N_REMAINING3, 36)
        self.assertEqual(CYCLE231_N_WITHOUT_G, 33)
        prior_230 = self.survey["i_090_076_013_forward_4grams_i_only"]
        self.assertEqual(prior_230["cycle"], 230)
        self.assertEqual(prior_230["N_I"], 5)
        self.assertEqual(prior_230["N_i_only"], 5)
        self.assertEqual(prior_230["N_not_i_only"], 0)
        self.assertTrue(prior_230["i_090_076_013_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE230_CLAIM)
        self.assertEqual(CYCLE230_N_I_ONLY, 5)
        self.assertEqual(CYCLE230_N_NOT_I_ONLY, 0)
        prior_229 = self.survey["i_3gram_090_076_013_i_only"]
        self.assertEqual(prior_229["cycle"], 229)
        self.assertEqual(prior_229["N_I"], 5)
        self.assertEqual(prior_229["N_off_I"], 0)
        self.assertTrue(prior_229["i_3gram_090_076_013_i_only"])
        self.assertTrue(CYCLE229_CLAIM)
        self.assertEqual(CYCLE229_N_I, 5)
        self.assertEqual(CYCLE229_N_OFF_I, 0)
        prior_228 = self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]
        self.assertEqual(prior_228["cycle"], 228)
        self.assertEqual(prior_228["N_remaining2"], 41)
        self.assertEqual(prior_228["G"], "013")
        self.assertEqual(prior_228["K"], 5)
        self.assertTrue(CYCLE228_CLAIM)
        self.assertEqual(CYCLE228_G, "013")
        self.assertEqual(CYCLE228_K, 5)
        prior_227 = self.survey["i_leftover_extra_090_076_remaining_next_stem"]
        self.assertEqual(prior_227["cycle"], 227)
        self.assertEqual(prior_227["N_remaining"], 47)
        self.assertEqual(prior_227["G"], "071")
        self.assertEqual(prior_227["K"], 6)
        self.assertTrue(CYCLE227_CLAIM)
        self.assertEqual(CYCLE227_G, "071")
        self.assertEqual(CYCLE227_K, 6)
        prior_226 = self.survey["i_leftover_extra_090_076_forward_070"]
        self.assertEqual(prior_226["cycle"], 226)
        self.assertEqual(prior_226["G"], "070")
        self.assertEqual(prior_226["K"], 8)
        self.assertTrue(CYCLE226_CLAIM)
        self.assertEqual(CYCLE226_G, "070")
        self.assertEqual(CYCLE226_K, 8)
        prior_225 = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(prior_225["cycle"], 225)
        self.assertEqual(prior_225["N_distinct_next_stems"], 30)
        self.assertEqual(prior_225["G"], "070")
        self.assertEqual(prior_225["K"], 8)
        self.assertFalse(prior_225["i_leftover_extra_090_076_share_one_forward_stem"])
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertFalse(CYCLE224_ALL_INSIDE)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_195 = self.survey["i_3gram_090_076_071_i_only"]
        self.assertEqual(prior_195["cycle"], 195)
        self.assertEqual(prior_195["N_I"], 6)
        self.assertEqual(prior_195["N_off_I"], 0)
        self.assertTrue(prior_195["i_3gram_090_076_071_i_only"])
        self.assertTrue(CYCLE195_CLAIM)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_001_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_33_remaining4_g_700_k_2_and_hypothesis_loses(self):
        """N_remaining4=33, N_distinct=26, G=700 K=2 tied. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 55)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 1)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ((SIDE_IA, "Ia4", 166),))
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_leftover)
        self.assertEqual(55 + 1, 56)
        self.assertEqual(self.n_share_070, STANDING_N_SHARE_070)
        self.assertEqual(STANDING_N_SHARE_070, 8)
        self.assertEqual(self.share_070, CYCLE226_MATCHING_SITES)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING, 47)
        self.assertEqual(self.n_remaining, self.n_with_next - self.n_share_070)
        self.assertEqual(55 - 8, 47)
        self.assertEqual(self.remaining, CYCLE227_REMAINING_SITES)
        self.assertEqual(self.n_share_071, STANDING_N_SHARE_071)
        self.assertEqual(STANDING_N_SHARE_071, 6)
        self.assertEqual(self.share_071, CYCLE227_MATCHING_SITES)
        self.assertEqual(self.share_071, CYCLE195_I_SITES)
        if self.share_071 != CYCLE195_I_SITES:
            self.fail("leftover extra remaining 6 share 071 drifted from cycle-195 I set")
        self.assertEqual(self.n_remaining2, STANDING_N_REMAINING2)
        self.assertEqual(STANDING_N_REMAINING2, 41)
        self.assertEqual(self.n_remaining2, self.n_remaining - self.n_share_071)
        self.assertEqual(47 - 6, 41)
        self.assertEqual(self.remaining2, CYCLE228_REMAINING2_SITES)
        self.assertEqual(self.n_share_013, STANDING_N_SHARE_013)
        self.assertEqual(STANDING_N_SHARE_013, 5)
        self.assertEqual(self.share_013, CYCLE228_MATCHING_SITES)
        self.assertEqual(self.share_013, CYCLE229_I_SITES)
        if self.share_013 != CYCLE229_I_SITES:
            self.fail("leftover extra remaining-after-071 5 share 013 drifted from cycle-229 I set")
        self.assertEqual(self.n_remaining3, STANDING_N_REMAINING3)
        self.assertEqual(STANDING_N_REMAINING3, 36)
        self.assertEqual(self.n_remaining3, self.n_remaining2 - self.n_share_013)
        self.assertEqual(41 - 5, 36)
        self.assertEqual(self.remaining3, CYCLE231_REMAINING3_SITES)
        self.assertEqual(self.n_share_001, STANDING_N_SHARE_001)
        self.assertEqual(STANDING_N_SHARE_001, 3)
        self.assertEqual(STANDING_N_SHARE_001, CYCLE231_K)
        self.assertEqual(self.share_001, CYCLE231_MATCHING_SITES)
        self.assertEqual(self.share_001, CYCLE232_I_SITES)
        if self.share_001 != CYCLE232_I_SITES:
            self.fail("leftover extra remaining-after-013 3 share 001 drifted from cycle-232 I set")
        if (
            self.n_leftover != 56
            or self.n_with_next != 55
            or self.n_no_next != 1
            or self.n_share_070 != 8
            or self.n_remaining != 47
            or self.n_share_071 != 6
            or self.n_remaining2 != 41
            or self.n_share_013 != 5
            or self.n_remaining3 != 36
            or self.n_share_001 != 3
        ):
            self.fail(
                "nested leftover extra 56/55/1 / 8 share 070 / remaining 47/6/071 / "
                "remaining-after-071 41/5/013 / remaining-after-013 36/3/001 drifted"
            )
        self.assertTrue(
            leftover_extra_remaining_after_001_nested_counts_hold(
                self.n_leftover,
                self.n_with_next,
                self.n_no_next,
                self.n_share_070,
                self.n_remaining,
                self.n_share_071,
                self.n_remaining2,
                self.n_share_013,
                self.n_remaining3,
                self.n_share_001,
                self.n_remaining4,
            )
        )
        self.assertEqual(self.n_remaining4, STANDING_N_REMAINING4)
        self.assertEqual(STANDING_N_REMAINING4, 33)
        self.assertEqual(self.n_remaining4, self.n_remaining3 - self.n_share_001)
        self.assertEqual(36 - 3, 33)
        self.assertEqual(self.n_remaining4, CYCLE231_N_WITHOUT_G)
        if self.n_remaining4 != 33:
            self.fail("measured N_remaining4 drifted from 33")
        if self.n_remaining4 != self.n_remaining3 - self.n_share_001:
            self.fail("leftover extra remaining-after-001 filter disagrees with nested 36−3")
        self.assertEqual(self.remaining4, STANDING_REMAINING4_SITES)
        self.assertEqual(self.remaining4_stems, STANDING_REMAINING4_NEXT_STEMS)
        self.assertEqual(len(self.remaining4), len(self.remaining4_stems))
        self.assertEqual(
            self.remaining4,
            leftover_extra_remaining_after_013_without_g(
                self.leftover_sites,
                self.next_stems,
                LOCKED_FORWARD_STEM_001,
            ),
        )
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.remaining4)
        self.assertIn(STANDING_IA2_174, self.remaining4)
        self.assertEqual(STANDING_IA2_174_NEXT_STEM, "000")
        for site in self.share_070:
            self.assertNotIn(site, self.remaining4)
        for site in self.share_071:
            self.assertNotIn(site, self.remaining4)
        for site in self.share_013:
            self.assertNotIn(site, self.remaining4)
        for site in self.share_001:
            self.assertNotIn(site, self.remaining4)
        self.assertEqual(self.n_distinct_remaining4, STANDING_N_DISTINCT_REMAINING4)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING4, 26)
        self.assertEqual(self.n_distinct_remaining4, CYCLE231_N_DISTINCT - 1)
        self.assertEqual(self.frequency, STANDING_REMAINING4_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "700")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, HYPOTHESIS_K)
        self.assertEqual(STANDING_K, 2)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "700")
        self.assertEqual(self.frequency[0][1], 2)
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 2)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 7)
        self.assertEqual(self.frequency[1][0], STANDING_N_NEXT_AFTER_G_STEM)
        self.assertEqual(self.frequency[1][1], STANDING_N_NEXT_AFTER_G)
        self.assertEqual(STANDING_N_NEXT_AFTER_G, 2)
        self.assertEqual(STANDING_N_NEXT_AFTER_G_STEM, "530")
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 31)
        self.assertEqual(self.k + self.n_without, self.n_remaining4)
        self.assertEqual(2 + 31, 33)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX_REMAINING4)
        self.assertEqual(STANDING_N_HAPAX_REMAINING4, 19)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_001_exactly_k_share_g(
                self.leftover_sites,
                self.next_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G,
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE222)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE227)
        self.assertFalse(STANDING_SAME_AS_CYCLE228)
        self.assertFalse(STANDING_SAME_AS_CYCLE229)
        self.assertFalse(STANDING_SAME_AS_CYCLE230)
        self.assertFalse(STANDING_SAME_AS_CYCLE231)
        self.assertFalse(STANDING_SAME_AS_CYCLE232)
        self.assertFalse(STANDING_SAME_AS_CYCLE233)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE227)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE228)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE231)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_001_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertTrue(CYCLE226_CLAIM)
        self.assertTrue(CYCLE227_CLAIM)
        self.assertTrue(CYCLE228_CLAIM)
        self.assertTrue(CYCLE229_CLAIM)
        self.assertTrue(CYCLE230_CLAIM)
        self.assertTrue(CYCLE231_CLAIM)
        self.assertTrue(CYCLE232_CLAIM)
        self.assertTrue(CYCLE233_CLAIM)
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_remaining_after_001_sites_share_700(self):
        """Two leftover extra remaining-after-001 sites are 090 076 700 (tie-break G)."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia2", 159), ("090", "076", "700", "011")),
            ((SIDE_IA, "Ia13", 143), ("090", "076", "700", "076")),
        )
        for (site, nxt), (want_site, want_nxt) in zip(
            zip(self.matching, self.matching_next_4grams, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3_FORWARD)
            self.assertEqual(stems[index + STANDING_N2], "700")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "700")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_REMAINING4_SITES)
            self.assertIn(site, CYCLE231_REMAINING3_SITES)
            self.assertIn(site, CYCLE228_REMAINING2_SITES)
            self.assertIn(site, CYCLE227_REMAINING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE226_MATCHING_SITES)
            self.assertNotIn(site, CYCLE227_MATCHING_SITES)
            self.assertNotIn(site, CYCLE228_MATCHING_SITES)
            self.assertNotIn(site, CYCLE229_I_SITES)
            self.assertNotIn(site, CYCLE231_MATCHING_SITES)
            self.assertNotIn(site, CYCLE232_I_SITES)
            self.assertNotIn(site, CYCLE207_I_SITES)
            self.assertNotIn(site, CYCLE195_I_SITES)
        self.assertNotIn(STANDING_IA2_174, self.matching)
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.matching)
        self.assertIn(STANDING_IA2_174, self.remaining4)
        self.assertEqual(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_IA2_174)],
            "000",
        )
        self.assertIsNone(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_NO_NEXT_SITES[0])]
        )
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "700")
            self.assertNotEqual(nxt, "001")
            self.assertNotEqual(nxt, "013")
            self.assertNotEqual(nxt, "071")
            self.assertNotEqual(nxt, "070")
            self.assertIn(site, STANDING_REMAINING4_SITES)
        for site in self.share_070:
            self.assertNotIn(site, self.remaining4)
            self.assertNotIn(site, self.matching)
        for site in self.share_071:
            self.assertNotIn(site, self.remaining4)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE195_I_SITES)
        for site in self.share_013:
            self.assertNotIn(site, self.remaining4)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE229_I_SITES)
        for site in self.share_001:
            self.assertNotIn(site, self.remaining4)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE232_I_SITES)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining4)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining4)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_001_ARE_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_233_232_230_229_223_195_and_171_still_compute(self):
        """Cycle 233 3/0 hapax, 232 3/0, 230 5/0 hapax, 229 5/0, 223 69/3, 195 6/0, 171 43/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_233 = TestMamariI090076001Forward4gramsIOnlyScoreboard()
        prior_233.setUp()
        prior_233.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_233.test_survey_matches_computed_lock()
        self.assertEqual(prior_233.n_i_only, 3)
        self.assertEqual(prior_233.n_not_i_only, 0)
        self.assertTrue(prior_233.claim_holds)
        self.assertTrue(CYCLE233_CLAIM)
        self.assertEqual(CYCLE233_N_I_ONLY, 3)
        self.assertEqual(CYCLE233_N_NOT_I_ONLY, 0)
        if prior_233.n_i_only != 3 or prior_233.n_not_i_only != 0:
            self.fail("nested cycle 233 090 076 001 forward 4-grams 3/0 hapax drifted")
        prior_232 = TestMamariI3gram090076001IOnlyScoreboard()
        prior_232.setUp()
        prior_232.test_i_hits_are_three_on_ia_and_equal_leftover_extra_001()
        prior_232.test_3gram_is_zero_off_i_and_i_only()
        prior_232.test_survey_matches_computed_lock()
        self.assertEqual(prior_232.i_hits, CYCLE232_N_I)
        self.assertEqual(prior_232.i_hits, 3)
        self.assertEqual(prior_232.off_i_hits, CYCLE232_N_OFF_I)
        self.assertEqual(prior_232.off_i_hits, 0)
        self.assertEqual(prior_232.i_sites, CYCLE232_I_SITES)
        self.assertEqual(self.share_001, CYCLE232_I_SITES)
        self.assertTrue(prior_232.claim_holds)
        self.assertTrue(CYCLE232_CLAIM)
        if prior_232.i_hits != 3 or prior_232.off_i_hits != 0:
            self.fail("nested cycle 232 090 076 001 I-only 3/0 drifted")
        prior_231 = TestMamariILeftoverExtra090076RemainingAfter013NextStemScoreboard()
        prior_231.setUp()
        prior_231.test_counts_36_remaining3_g_001_k_3_and_hypothesis_holds()
        prior_231.test_survey_matches_computed_lock()
        self.assertEqual(prior_231.n_leftover, 56)
        self.assertEqual(prior_231.n_with_next, 55)
        self.assertEqual(prior_231.n_no_next, 1)
        self.assertEqual(prior_231.n_remaining3, 36)
        self.assertEqual(prior_231.k, 3)
        self.assertEqual(CYCLE231_G, "001")
        self.assertEqual(prior_231.matching, CYCLE231_MATCHING_SITES)
        self.assertTrue(prior_231.claim_holds)
        self.assertTrue(CYCLE231_CLAIM)
        if (
            prior_231.n_leftover != 56
            or prior_231.n_with_next != 55
            or prior_231.n_no_next != 1
            or prior_231.n_remaining3 != 36
            or prior_231.k != 3
        ):
            self.fail("nested cycle 231 leftover extra remaining-after-013 36 G=001 K=3 drifted")
        prior_230 = TestMamariI090076013Forward4gramsIOnlyScoreboard()
        prior_230.setUp()
        prior_230.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_230.test_survey_matches_computed_lock()
        self.assertEqual(prior_230.n_i_only, 5)
        self.assertEqual(prior_230.n_not_i_only, 0)
        self.assertTrue(prior_230.claim_holds)
        self.assertTrue(CYCLE230_CLAIM)
        if prior_230.n_i_only != 5 or prior_230.n_not_i_only != 0:
            self.fail("nested cycle 230 090 076 013 forward 4-grams 5/0 hapax drifted")
        prior_229 = TestMamariI3gram090076013IOnlyScoreboard()
        prior_229.setUp()
        prior_229.test_i_hits_are_five_on_ia_and_equal_leftover_extra_013()
        prior_229.test_3gram_is_zero_off_i_and_i_only()
        prior_229.test_survey_matches_computed_lock()
        self.assertEqual(prior_229.i_hits, CYCLE229_N_I)
        self.assertEqual(prior_229.i_hits, 5)
        self.assertEqual(prior_229.off_i_hits, CYCLE229_N_OFF_I)
        self.assertEqual(prior_229.off_i_hits, 0)
        self.assertEqual(prior_229.i_sites, CYCLE229_I_SITES)
        self.assertEqual(self.share_013, CYCLE229_I_SITES)
        self.assertTrue(prior_229.claim_holds)
        self.assertTrue(CYCLE229_CLAIM)
        if prior_229.i_hits != 5 or prior_229.off_i_hits != 0:
            self.fail("nested cycle 229 090 076 013 I-only 5/0 drifted")
        prior_228 = TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard()
        prior_228.setUp()
        prior_228.test_counts_41_remaining2_g_013_k_5_and_hypothesis_holds()
        prior_228.test_survey_matches_computed_lock()
        self.assertEqual(prior_228.n_leftover, 56)
        self.assertEqual(prior_228.n_remaining2, 41)
        self.assertEqual(prior_228.k, 5)
        self.assertEqual(CYCLE228_G, "013")
        self.assertTrue(prior_228.claim_holds)
        self.assertTrue(CYCLE228_CLAIM)
        prior_227 = TestMamariILeftoverExtra090076RemainingNextStemScoreboard()
        prior_227.setUp()
        prior_227.test_counts_47_remaining_g_071_k_6_and_hypothesis_holds()
        prior_227.test_survey_matches_computed_lock()
        self.assertEqual(prior_227.n_leftover, 56)
        self.assertEqual(prior_227.n_remaining, 47)
        self.assertEqual(prior_227.k, 6)
        self.assertEqual(CYCLE227_G, "071")
        self.assertTrue(prior_227.claim_holds)
        self.assertTrue(CYCLE227_CLAIM)
        prior_226 = TestMamariILeftoverExtra090076Forward070Scoreboard()
        prior_226.setUp()
        prior_226.test_counts_8_of_56_and_hypothesis_k_8_holds()
        prior_226.test_survey_matches_computed_lock()
        self.assertEqual(prior_226.n_leftover, 56)
        self.assertEqual(prior_226.k, 8)
        self.assertEqual(CYCLE226_G, "070")
        self.assertTrue(prior_226.claim_holds)
        self.assertTrue(CYCLE226_CLAIM)
        prior_225 = TestMamariILeftoverExtra090076ForwardStemScoreboard()
        prior_225.setUp()
        prior_225.test_counts_30_distinct_next_stems_and_claim_loses()
        prior_225.test_survey_matches_computed_lock()
        self.assertEqual(prior_225.n_leftover, 56)
        self.assertEqual(prior_225.n_distinct, 30)
        self.assertEqual(prior_225.g, "070")
        self.assertEqual(prior_225.k, 8)
        self.assertFalse(prior_225.claim_holds)
        self.assertFalse(CYCLE225_SHARE_ONE)
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, STANDING_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, STANDING_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, STANDING_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_195 = TestMamariI3gram090076071IOnlyScoreboard()
        prior_195.setUp()
        prior_195.test_i_hits_are_six_on_ia()
        prior_195.test_3gram_is_zero_off_i_and_i_only()
        prior_195.test_survey_matches_computed_lock()
        self.assertEqual(prior_195.i_hits, CYCLE195_N_I)
        self.assertEqual(prior_195.i_hits, 6)
        self.assertEqual(prior_195.off_i_hits, CYCLE195_N_OFF_I)
        self.assertEqual(prior_195.off_i_hits, 0)
        self.assertEqual(prior_195.i_sites, CYCLE195_I_SITES)
        self.assertEqual(self.share_071, CYCLE195_I_SITES)
        self.assertTrue(prior_195.claim_holds)
        self.assertTrue(CYCLE195_CLAIM)
        if prior_195.i_hits != 6 or prior_195.off_i_hits != 0:
            self.fail("nested cycle 195 090 076 071 I-only 6/0 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-234 leftover extra remaining-after-001 lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]
        self.assertEqual(lock["cycle"], 234)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(tuple(lock["locked_forward_stems"]), ("070", "071", "013", "001"))
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 55)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(lock["N_share_070"], STANDING_N_SHARE_070)
        self.assertEqual(lock["N_share_070"], 8)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_070_sites"]),
            CYCLE226_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 47)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_sites"]),
            CYCLE227_REMAINING_SITES,
        )
        self.assertEqual(lock["N_share_071"], STANDING_N_SHARE_071)
        self.assertEqual(lock["N_share_071"], 6)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_071_sites"]),
            CYCLE227_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_071_sites"]),
            CYCLE195_I_SITES,
        )
        self.assertEqual(lock["N_remaining2"], STANDING_N_REMAINING2)
        self.assertEqual(lock["N_remaining2"], 41)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_071_sites"]),
            CYCLE228_REMAINING2_SITES,
        )
        self.assertEqual(lock["N_share_013"], STANDING_N_SHARE_013)
        self.assertEqual(lock["N_share_013"], 5)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_013_sites"]),
            CYCLE228_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_013_sites"]),
            CYCLE229_I_SITES,
        )
        self.assertEqual(lock["N_remaining3"], STANDING_N_REMAINING3)
        self.assertEqual(lock["N_remaining3"], 36)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_013_sites"]),
            CYCLE231_REMAINING3_SITES,
        )
        self.assertEqual(lock["N_share_001"], STANDING_N_SHARE_001)
        self.assertEqual(lock["N_share_001"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_001_sites"]),
            CYCLE231_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_001_sites"]),
            CYCLE232_I_SITES,
        )
        self.assertEqual(lock["ia2_174_next_stem"], STANDING_IA2_174_NEXT_STEM)
        self.assertEqual(lock["ia2_174_next_stem"], "000")
        self.assertEqual(lock["N_remaining4"], STANDING_N_REMAINING4)
        self.assertEqual(lock["N_remaining4"], 33)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_001_sites"]),
            STANDING_REMAINING4_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_001_next_stems"]),
            STANDING_REMAINING4_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_remaining4"], STANDING_N_DISTINCT_REMAINING4)
        self.assertEqual(lock["N_distinct_remaining4"], 26)
        self.assertEqual(lock["N_hapax_remaining4"], STANDING_N_HAPAX_REMAINING4)
        self.assertEqual(lock["N_hapax_remaining4"], 19)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "700")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 7)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 31)
        self.assertEqual(lock["N_next_after_G"], STANDING_N_NEXT_AFTER_G)
        self.assertEqual(lock["N_next_after_G"], 2)
        self.assertEqual(lock["next_after_G"], STANDING_N_NEXT_AFTER_G_STEM)
        self.assertEqual(lock["next_after_G"], "530")
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_001_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_001_local_4grams"],
            matching_leftover_extra_remaining_after_001_local_4gram_rows(),
        )
        self.assertEqual(
            lock["remaining_after_001_next_stem_frequency"],
            remaining_after_001_next_stem_frequency_rows(),
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G"])
        self.assertEqual(
            lock["i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G"],
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle222"])
        self.assertFalse(lock["same_as_cycle226"])
        self.assertFalse(lock["same_as_cycle227"])
        self.assertFalse(lock["same_as_cycle228"])
        self.assertFalse(lock["same_as_cycle229"])
        self.assertFalse(lock["same_as_cycle230"])
        self.assertFalse(lock["same_as_cycle231"])
        self.assertFalse(lock["same_as_cycle232"])
        self.assertFalse(lock["same_as_cycle233"])
        self.assertTrue(lock["same_claim_shape_as_cycle222"])
        self.assertTrue(lock["same_claim_shape_as_cycle226"])
        self.assertTrue(lock["same_claim_shape_as_cycle227"])
        self.assertTrue(lock["same_claim_shape_as_cycle228"])
        self.assertTrue(lock["same_claim_shape_as_cycle231"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_090_076_G_is_not_this_cycle"])
        self.assertTrue(lock["previous_4grams_of_090_076_001_are_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle224_no_next_4gram_is_not_no_next_token"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_090_076_001_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_001_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_013_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_013_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_013_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_071_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["cycle"], 233)
        self.assertTrue(
            self.survey["i_090_076_001_forward_4grams_i_only"][
                "i_090_076_001_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["N_i_only"], 3)
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["cycle"], 232)
        self.assertTrue(self.survey["i_3gram_090_076_001_i_only"]["i_3gram_090_076_001_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_013_next_stem"]["cycle"],
            231,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_013_next_stem"][
                "i_leftover_extra_090_076_remaining_after_013_exactly_K_share_G"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_013_next_stem"]["N_remaining3"],
            36,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_013_next_stem"]["G"],
            "001",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_013_next_stem"]["K"],
            3,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_013_next_stem"]["N_without_G"],
            33,
        )
        self.assertEqual(self.survey["i_090_076_013_forward_4grams_i_only"]["cycle"], 230)
        self.assertTrue(
            self.survey["i_090_076_013_forward_4grams_i_only"][
                "i_090_076_013_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_013_forward_4grams_i_only"]["N_i_only"], 5)
        self.assertEqual(self.survey["i_090_076_013_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_013_i_only"]["cycle"], 229)
        self.assertTrue(self.survey["i_3gram_090_076_013_i_only"]["i_3gram_090_076_013_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_013_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_3gram_090_076_013_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["cycle"],
            228,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"][
                "i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["N_remaining2"],
            41,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["G"],
            "013",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["K"],
            5,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["cycle"], 227)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_next_stem"][
                "i_leftover_extra_090_076_remaining_exactly_6_share_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["N_remaining"], 47)
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["G"], "071")
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["K"], 6)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["cycle"], 226)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_forward_070"][
                "i_leftover_extra_090_076_exactly_8_share_forward_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["K"], 8)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["cycle"], 225)
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_forward_stem"][
                "i_leftover_extra_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_leftover_n4_remaining_next_2gram"]["cycle"], 222)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_next_2gram"][
                "i_leftover_n4_remaining_exactly_5_contain_090_076"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["cycle"], 195)
        self.assertTrue(self.survey["i_3gram_090_076_071_i_only"]["i_3gram_090_076_071_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertTrue(self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"])
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"], 5)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter001NextStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 234 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
