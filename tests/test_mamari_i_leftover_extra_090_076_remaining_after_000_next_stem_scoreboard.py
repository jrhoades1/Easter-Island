"""I's cycle-255 leftover extra remaining-after-000 next-stem lock.

Cycle 256 text-search lock. Uses already-vendored A–V and the
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

Cycle 234 lost unique most frequent remaining-after-001 next
stem: N_remaining4=33, 7-way tie at count 2. Cycles 235–255
peeled that 7-way tie. Last peeled: cycle 253 leftover extra
remaining-after-005 exactly 2 share 000 HOLDS; cycle 254
3-gram 090 076 000 I-only 2/0 extra I=0; cycle 255 continuing
forward 4-grams all I-only hapax 1/0 (Ia10[141] 090 076 000
076) plus Ia2[174] line-final. The 000 cluster is closed at
n=4 forward. This cycle is the unique-max claim on leftover
extra remaining-after-000 (same claim-shape as cycle 234).
Do not peel a specific remaining stem this cycle. Do not lock
I-only of any remaining-after-000 3-gram. Do not lock previous
4-grams of 090 076 000. Off-I T sites are not this cycle.

Leftover extra remaining-after-000 = leftover extra I 090 076
sites with a next token whose next token is none of 070, 071,
013, 001, 700, 530, 280, 087, 011, 005, or 000. Nested-check
leftover extra remaining-after-001 33/2/700, remaining-after-700
31/2/530, remaining-after-530 29/2/280, remaining-after-280
27/2/087, remaining-after-087 25/2/011, remaining-after-011
23/2/005, remaining-after-005 21/2/000 (do not retune cycles
234–253). Nested-check cycle 254 2/0 extra I=0 and cycle 255
continuing 4-gram 1/0 plus Ia2[174] line-final (do not retune).
Nested-check N_remaining11==19 (21−2). Sites without a next
token are not remaining-after-000. Ia2[174] is remaining-after-005
000 (line-final), not remaining-after-000. Measure, do not assume.

Among remaining-after-000, G = the next stem with the highest
remaining-after-000 count. If a tie, pick the larger Barthel
id. K = that count. Measured: N_remaining11=19,
N_distinct_remaining11=19, all hapax count 1, G=755 by
larger-id tie-break among 19 stems at count 1, K=1 at
Ia1[27]. Claim that can lose:
i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem.
True iff some G has K ≥ 2 and no other stem has count K.
The claim is false: N_remaining11==19 holds and the remaining-
after-000 filter agrees with nested 21−2, but every next stem
is hapax (all distinct K=1). Same lose path cycle 234 named
(tie at K, or all distinct K=1). Same claim-shape as cycle 234
(remaining-after-001 unique-max lost on a 7-way tie at 2).
If it loses, still lock the frequency table, G, K, and
N_remaining11. Nested cycle 255 1/0 + line-final, cycle 254
2/0 extra I=0, cycle 253 K=2 / G=000 N_remaining10=21, cycle
234 7-way tie at 2, cycle 223 69/3, and cycle 171 43/0 stay.
Do not assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_000_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE255_CLAIM,
    STANDING_N_I_ONLY as CYCLE255_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE255_N_NOT_I_ONLY,
    STANDING_IA2_174_LINE_FINAL as CYCLE255_IA2_174_LINE_FINAL,
    TestMamariI090076000Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
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
from tests.test_mamari_i_3gram_090_076_000_i_only_scoreboard import (
    GRAM3 as CYCLE254_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE254_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_000_I_ONLY as CYCLE254_CLAIM,
    STANDING_I_SITES as CYCLE254_I_SITES,
    STANDING_N_EXTRA as CYCLE254_N_EXTRA,
    STANDING_N_I as CYCLE254_N_I,
    STANDING_N_OFF_I as CYCLE254_N_OFF_I,
    TestMamariI3gram090076000IOnlyScoreboard,
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
    leftover_extra_with_forward_070,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_IA2_174,
    STANDING_IA2_174_NEXT_STEM,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_NO_NEXT_SITES,
    group_sites_by_next_stem,
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
    leftover_sites_with_next,
    leftover_sites_without_next,
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_fwd700_scoreboard import (
    STANDING_G as CYCLE235_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_2_SHARE_700 as CYCLE235_CLAIM,
    STANDING_K as CYCLE235_K,
    STANDING_MATCHING_SITES as CYCLE235_MATCHING_SITES,
    leftover_extra_remaining_after_001_with_700,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    STANDING_G as CYCLE234_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G as CYCLE234_CLAIM,
    STANDING_K as CYCLE234_K,
    STANDING_N_DISTINCT_REMAINING4 as CYCLE234_N_DISTINCT,
    STANDING_N_REMAINING4 as CYCLE234_N_REMAINING4,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
    STANDING_REMAINING4_SITES as CYCLE234_REMAINING4_SITES,
    STANDING_TIED_STEMS as CYCLE234_TIED_STEMS,
    leftover_extra_remaining_after_001,
    leftover_extra_remaining_after_001_next_stems,
    leftover_extra_remaining_after_001_with_g,
    remaining_after_001_next_stem_frequency_table,
    select_remaining_after_001_g,
    TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_005_fwd000_scoreboard import (
    LOCKED_FORWARD_STEMS_AFTER_005,
    STANDING_G as CYCLE253_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000 as CYCLE253_CLAIM,
    STANDING_K as CYCLE253_K,
    STANDING_MATCHING_SITES as CYCLE253_MATCHING_SITES,
    STANDING_N_REMAINING10 as CYCLE253_N_REMAINING10,
    STANDING_N_WITHOUT as CYCLE253_N_WITHOUT,
    STANDING_REMAINING10_SITES as CYCLE253_REMAINING10_SITES,
    leftover_extra_remaining_after_005,
    leftover_extra_remaining_after_005_nested_counts_hold,
    leftover_extra_remaining_after_005_next_stems,
    leftover_extra_remaining_after_005_with_000,
    leftover_extra_remaining_after_005_without_000,
    TestMamariILeftoverExtra090076RemainingAfter005Fwd000Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_011_fwd005_scoreboard import (
    STANDING_G as CYCLE250_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_011_EXACTLY_2_SHARE_005 as CYCLE250_CLAIM,
    STANDING_K as CYCLE250_K,
    STANDING_MATCHING_SITES as CYCLE250_MATCHING_SITES,
    leftover_extra_remaining_after_011,
    leftover_extra_remaining_after_011_with_005,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_013_next_stem_scoreboard import (
    STANDING_G as CYCLE231_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_013_EXACTLY_K_SHARE_G as CYCLE231_CLAIM,
    STANDING_K as CYCLE231_K,
    STANDING_MATCHING_SITES as CYCLE231_MATCHING_SITES,
    leftover_extra_remaining_after_013,
    leftover_extra_remaining_after_013_with_g,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_071_next_stem_scoreboard import (
    STANDING_G as CYCLE228_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G as CYCLE228_CLAIM,
    STANDING_K as CYCLE228_K,
    STANDING_MATCHING_SITES as CYCLE228_MATCHING_SITES,
    leftover_extra_remaining_after_071,
    leftover_extra_remaining_after_071_with_g,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_087_fwd011_scoreboard import (
    STANDING_G as CYCLE247_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_011 as CYCLE247_CLAIM,
    STANDING_K as CYCLE247_K,
    STANDING_MATCHING_SITES as CYCLE247_MATCHING_SITES,
    leftover_extra_remaining_after_087,
    leftover_extra_remaining_after_087_with_011,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_280_fwd087_scoreboard import (
    STANDING_G as CYCLE244_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_280_EXACTLY_2_SHARE_087 as CYCLE244_CLAIM,
    STANDING_K as CYCLE244_K,
    STANDING_MATCHING_SITES as CYCLE244_MATCHING_SITES,
    leftover_extra_remaining_after_280,
    leftover_extra_remaining_after_280_with_087,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_530_fwd280_scoreboard import (
    STANDING_G as CYCLE241_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_530_EXACTLY_2_SHARE_280 as CYCLE241_CLAIM,
    STANDING_K as CYCLE241_K,
    STANDING_MATCHING_SITES as CYCLE241_MATCHING_SITES,
    leftover_extra_remaining_after_530,
    leftover_extra_remaining_after_530_with_280,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_700_fwd530_scoreboard import (
    STANDING_G as CYCLE238_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_700_EXACTLY_2_SHARE_530 as CYCLE238_CLAIM,
    STANDING_K as CYCLE238_K,
    STANDING_MATCHING_SITES as CYCLE238_MATCHING_SITES,
    leftover_extra_remaining_after_700,
    leftover_extra_remaining_after_700_with_530,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    STANDING_G as CYCLE227_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 as CYCLE227_CLAIM,
    STANDING_K as CYCLE227_K,
    STANDING_MATCHING_SITES as CYCLE227_MATCHING_SITES,
    barthel_id,
    leftover_extra_remaining,
    leftover_extra_remaining_with_g,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
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

LOCKED_FORWARD_STEM_070 = "070"
LOCKED_FORWARD_STEM_071 = "071"
LOCKED_FORWARD_STEM_013 = "013"
LOCKED_FORWARD_STEM_001 = "001"
LOCKED_FORWARD_STEM_700 = "700"
LOCKED_FORWARD_STEM_530 = "530"
LOCKED_FORWARD_STEM_280 = "280"
LOCKED_FORWARD_STEM_087 = "087"
LOCKED_FORWARD_STEM_011 = "011"
LOCKED_FORWARD_STEM_005 = "005"
LOCKED_FORWARD_STEM_000 = "000"
LOCKED_FORWARD_STEMS_AFTER_000 = (
    "070",
    "071",
    "013",
    "001",
    "700",
    "530",
    "280",
    "087",
    "011",
    "005",
    "000",
)
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "755")
GRAM3_NESTED_000 = ("090", "076", "000")
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
STANDING_N_SHARE_700 = 2
STANDING_N_REMAINING5 = 31
STANDING_N_SHARE_530 = 2
STANDING_N_REMAINING6 = 29
STANDING_N_SHARE_280 = 2
STANDING_N_REMAINING7 = 27
STANDING_N_SHARE_087 = 2
STANDING_N_REMAINING8 = 25
STANDING_N_SHARE_011 = 2
STANDING_N_REMAINING9 = 23
STANDING_N_SHARE_005 = 2
STANDING_N_REMAINING10 = 21
STANDING_N_SHARE_000 = 2
STANDING_N_REMAINING11 = 19
STANDING_N_DISTINCT_REMAINING11 = 19
STANDING_N_HAPAX_REMAINING11 = 19
STANDING_G = "755"
STANDING_K = 1
STANDING_N_WITHOUT_G = 18
STANDING_N_TIED_AT_K = 19
STANDING_TIED_STEMS = (
    "755",
    "670",
    "607",
    "600",
    "535",
    "505",
    "470",
    "430",
    "386",
    "384",
    "300",
    "255",
    "175",
    "147",
    "090",
    "072",
    "057",
    "050",
    "012",
)
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_REMAINING10_SITES = CYCLE253_REMAINING10_SITES
STANDING_REMAINING11_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
    (SIDE_IA, "Ia2", 165),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia14", 177),
)
STANDING_REMAINING11_NEXT_STEMS = (
    "012",
    "175",
    "755",
    "470",
    "430",
    "600",
    "384",
    "535",
    "050",
    "147",
    "090",
    "386",
    "505",
    "607",
    "057",
    "072",
    "300",
    "255",
    "670",
)
STANDING_MATCHING_SITES = ((SIDE_IA, "Ia1", 27),)
STANDING_MATCHING_NEXT_4GRAMS = (("090", "076", "755", "509"),)
STANDING_REMAINING11_FREQUENCY = (
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
STANDING_CLAIM = "i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem"
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM = False
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_000_next_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE226 = False
STANDING_SAME_AS_CYCLE234 = False
STANDING_SAME_AS_CYCLE253 = False
STANDING_SAME_AS_CYCLE254 = False
STANDING_SAME_AS_CYCLE255 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_REMAINING_AFTER_000_3GRAM_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_IA2_174_IS_REMAINING_AFTER_005_000_NOT_REMAINING_AFTER_000 = True
STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN = True


def leftover_extra_remaining_after_000(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_000,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra with-next sites whose next token is none of 070/071/013/001/700/530/280/087/011/005/000."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_000_next_stems(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_000,
) -> tuple[str, ...]:
    """Next stems of leftover extra remaining-after-000 sites."""
    locked_set = set(locked)
    return tuple(
        nxt
        for nxt in next_stems
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_000_with_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-000 sites whose next token is G."""
    remaining11 = set(leftover_extra_remaining_after_000(sites, next_stems))
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem and site in remaining11
    )


def leftover_extra_remaining_after_000_without_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_000,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-000 sites whose next token is not G."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set and nxt != stem
    )


def remaining_after_000_next_stem_counts(next_stems: tuple[str, ...]) -> Counter:
    """Counts of next stems among leftover extra remaining-after-000."""
    return Counter(next_stems)


def rank_remaining_after_000_next_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining-after-000 next stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_after_000_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining-after-000 has no G."""
    ranked = rank_remaining_after_000_next_stems(
        remaining_after_000_next_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_after_000_next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    forward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_000,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining-after-000 next-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_extra_remaining_after_000(sites, next_stems, locked)
    rem_stems = leftover_extra_remaining_after_000_next_stems(sites, next_stems, locked)
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


def remaining_after_000_next_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING11_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining-after-000 next-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "next_stem": stem,
                "count": count,
                "leftover_extra_remaining_after_000_sites": [
                    list(site) for site in sites
                ],
                "forward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def leftover_extra_remaining_after_000_nested_counts_hold(
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
    n_share_700: int,
    n_remaining5: int,
    n_share_530: int,
    n_remaining6: int,
    n_share_280: int,
    n_remaining7: int,
    n_share_087: int,
    n_remaining8: int,
    n_share_011: int,
    n_remaining9: int,
    n_share_005: int,
    n_remaining10: int,
    n_share_000: int,
    n_remaining11: int,
    expected_share_000: int = STANDING_N_SHARE_000,
    expected_remaining11: int = STANDING_N_REMAINING11,
) -> bool:
    """Nested leftover extra chain through remaining-after-000 N_remaining11==19."""
    return leftover_extra_remaining_after_005_nested_counts_hold(
        n_leftover,
        n_with_next,
        n_no_next,
        n_share_070,
        n_remaining,
        n_share_071,
        n_remaining2,
        n_share_013,
        n_remaining3,
        n_share_001,
        n_remaining4,
        n_share_700,
        n_remaining5,
        n_share_530,
        n_remaining6,
        n_share_280,
        n_remaining7,
        n_share_087,
        n_remaining8,
        n_share_011,
        n_remaining9,
        n_share_005,
        n_remaining10,
    ) and n_share_000 == expected_share_000 and n_remaining11 == expected_remaining11 and (
        n_remaining11 == n_remaining10 - n_share_000
    )


def i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
    leftover_sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_000,
) -> bool:
    """True iff remaining-after-000 has a unique most frequent next stem with K ≥ 2."""
    remaining11_stems = leftover_extra_remaining_after_000_next_stems(
        leftover_sites,
        next_stems,
        locked,
    )
    remaining11 = leftover_extra_remaining_after_000(
        leftover_sites,
        next_stems,
        locked,
    )
    if len(remaining11) != STANDING_N_REMAINING11:
        return False
    if remaining11 != leftover_extra_remaining_after_005_without_000(
        leftover_sites,
        next_stems,
    ):
        return False
    gram, count, unique = select_remaining_after_000_g(remaining11_stems)
    return bool(unique and gram is not None and count >= 2)


def matching_leftover_extra_remaining_after_000_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-000 next-4-gram rows."""
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


class TestILeftoverExtra090076RemainingAfter000NextStemHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-000 next stems. No CV, no LLM."""

    def test_remaining_after_000_requires_with_next_not_locked_stems(self):
        """Remaining-after-000 excludes no-next and the locked 070…000 clusters."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "755"))
        self.assertEqual(GRAM3_NESTED_000, ("090", "076", "000"))
        self.assertEqual(GRAM3_NESTED_000, CYCLE254_GRAM3)
        self.assertEqual(
            LOCKED_FORWARD_STEMS_AFTER_005,
            ("070", "071", "013", "001", "700", "530", "280", "087", "011", "005"),
        )
        self.assertEqual(
            LOCKED_FORWARD_STEMS_AFTER_000,
            ("070", "071", "013", "001", "700", "530", "280", "087", "011", "005", "000"),
        )
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_755 = ["999", "090", "076", "755", "509"]
        self.assertEqual(site_next_stem(has_755, 1, GRAM2), "755")
        self.assertEqual(site_forward_3gram(has_755, 1, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_755, 1, GRAM2),
            ("090", "076", "755", "509"),
        )
        has_000 = ["009", "090", "076", "000"]
        self.assertEqual(site_next_stem(has_000, 1, GRAM2), "000")
        self.assertNotEqual(site_next_stem(has_000, 1, GRAM2), "755")
        self.assertIsNone(site_next_4gram(has_000, 1, GRAM2))
        end_of_line = ["087", "078", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
            (SIDE_IA, "Ia1", 5),
            (SIDE_IA, "Ia1", 6),
            (SIDE_IA, "Ia1", 7),
            (SIDE_IA, "Ia1", 8),
            (SIDE_IA, "Ia1", 9),
            (SIDE_IA, "Ia1", 10),
            (SIDE_IA, "Ia1", 11),
            (SIDE_IA, "Ia1", 12),
        )
        planted_stems = (
            "755",
            "000",
            "005",
            "011",
            "087",
            "280",
            "530",
            "700",
            "070",
            "071",
            "013",
            "001",
            None,
        )
        rem11 = leftover_extra_remaining_after_000(planted_sites, planted_stems)
        self.assertEqual(rem11, (planted_sites[0],))
        self.assertEqual(
            leftover_extra_remaining_after_000_next_stems(planted_sites, planted_stems),
            ("755",),
        )
        self.assertEqual(
            leftover_extra_remaining_after_000_with_g(planted_sites, planted_stems),
            (planted_sites[0],),
        )
        rem10 = leftover_extra_remaining_after_005(planted_sites, planted_stems)
        self.assertEqual(rem10, (planted_sites[0], planted_sites[1]))
        self.assertNotIn(planted_sites[1], rem11)
        self.assertNotIn(planted_sites[12], rem11)
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_IA2_174_IS_REMAINING_AFTER_005_000_NOT_REMAINING_AFTER_000)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_can_fail(self):
        """Boolean is True only when remaining11=19 and some G has unique K≥2."""
        provider = MockProvider()
        leftover = STANDING_LEFTOVER_SITES
        stems = leftover_extra_next_stems(load_i_sides(), leftover, GRAM2)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
                leftover,
                stems,
            )
        )
        rem11 = leftover_extra_remaining_after_000(leftover, stems)
        rem11_stems = leftover_extra_remaining_after_000_next_stems(leftover, stems)
        self.assertEqual(len(rem11), STANDING_N_REMAINING11)
        self.assertEqual(len(rem11), 19)
        self.assertEqual(rem11, STANDING_REMAINING11_SITES)
        self.assertEqual(rem11_stems, STANDING_REMAINING11_NEXT_STEMS)
        g, k, unique = select_remaining_after_000_g(rem11_stems)
        self.assertEqual(g, "755")
        self.assertEqual(k, 1)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = (None,) * len(leftover)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
                leftover,
                empty_stems,
            )
        )
        unique_755 = list(stems)
        demote_site = (SIDE_IA, "Ia1", 2)
        promote_site = (SIDE_IA, "Ia1", 15)
        for i, site in enumerate(leftover):
            if site == demote_site:
                unique_755[i] = "012"
            if site == promote_site:
                unique_755[i] = "755"
        unique_stems = tuple(unique_755)
        uniq_g, uniq_k, uniq_unique = select_remaining_after_000_g(
            leftover_extra_remaining_after_000_next_stems(leftover, unique_stems)
        )
        self.assertEqual(uniq_g, "755")
        self.assertEqual(uniq_k, 2)
        self.assertTrue(uniq_unique)
        self.assertEqual(
            len(leftover_extra_remaining_after_000(leftover, unique_stems)),
            19,
        )
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
                leftover,
                unique_stems,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem",
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING11)
        self.assertEqual(1 + 18, 19)
        self.assertEqual(
            STANDING_N_REMAINING10 - STANDING_N_SHARE_000,
            STANDING_N_REMAINING11,
        )
        self.assertEqual(21 - 2, 19)
        self.assertEqual(CYCLE253_N_WITHOUT, STANDING_N_REMAINING11)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_000_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining-after-000 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"755": 1, "670": 1, "012": 1})
        ranked = rank_remaining_after_000_next_stems(counts)
        self.assertEqual(ranked[0], ("755", 1))
        self.assertEqual(ranked[1], ("670", 1))
        self.assertEqual(ranked[2], ("012", 1))
        self.assertEqual(select_remaining_after_000_g(("755", "670"))[0], "755")
        self.assertFalse(select_remaining_after_000_g(("755", "670"))[2])
        self.assertEqual(select_remaining_after_000_g(("755", "755", "012"))[0], "755")
        self.assertTrue(select_remaining_after_000_g(("755", "755", "012"))[2])
        self.assertEqual(select_remaining_after_000_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-000 next-stem lock. Mock only."""

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
        self.share_700 = leftover_extra_remaining_after_001_with_700(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining5 = leftover_extra_remaining_after_700(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_530 = leftover_extra_remaining_after_700_with_530(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining6 = leftover_extra_remaining_after_530(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_280 = leftover_extra_remaining_after_530_with_280(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining7 = leftover_extra_remaining_after_280(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_087 = leftover_extra_remaining_after_280_with_087(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining8 = leftover_extra_remaining_after_087(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_011 = leftover_extra_remaining_after_087_with_011(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining9 = leftover_extra_remaining_after_011(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_005 = leftover_extra_remaining_after_011_with_005(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining10 = leftover_extra_remaining_after_005(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining10_stems = leftover_extra_remaining_after_005_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_000 = leftover_extra_remaining_after_005_with_000(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining11 = leftover_extra_remaining_after_000(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining11_stems = leftover_extra_remaining_after_000_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.matching = leftover_extra_remaining_after_000_with_g(
            self.leftover_sites,
            self.next_stems,
        )
        self.without = leftover_extra_remaining_after_000_without_g(
            self.leftover_sites,
            self.next_stems,
        )
        self.frequency = remaining_after_000_next_stem_frequency_table(
            self.leftover_sites,
            self.next_stems,
            self.forwards,
        )
        self.remaining4_frequency = remaining_after_001_next_stem_frequency_table(
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
        self.n_share_700 = len(self.share_700)
        self.n_remaining5 = len(self.remaining5)
        self.n_share_530 = len(self.share_530)
        self.n_remaining6 = len(self.remaining6)
        self.n_share_280 = len(self.share_280)
        self.n_remaining7 = len(self.remaining7)
        self.n_share_087 = len(self.share_087)
        self.n_remaining8 = len(self.remaining8)
        self.n_share_011 = len(self.share_011)
        self.n_remaining9 = len(self.remaining9)
        self.n_share_005 = len(self.share_005)
        self.n_remaining10 = len(self.remaining10)
        self.n_share_000 = len(self.share_000)
        self.n_remaining11 = len(self.remaining11)
        self.n_distinct_remaining11 = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_after_000_g(
            self.remaining11_stems
        )
        self.n_without = len(self.without)
        self.claim_holds = i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
            self.leftover_sites,
            self.next_stems,
        )

    def test_tokens_and_nested_leftover_extra_through_000_not_retuned(self):
        """2-gram and leftover extra 56/55/1 through remaining-after-005 21/2/000 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "755"))
        self.assertEqual(GRAM3_NESTED_000, ("090", "076", "000"))
        self.assertEqual(GRAM3_NESTED_000, CYCLE254_GRAM3)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        prior_255 = self.survey["i_090_076_000_forward_4grams_i_only"]
        self.assertEqual(prior_255["cycle"], 255)
        self.assertEqual(prior_255["N_i_only"], 1)
        self.assertEqual(prior_255["N_not_i_only"], 0)
        self.assertTrue(prior_255["ia2_174_line_final"])
        self.assertTrue(prior_255["i_090_076_000_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE255_CLAIM)
        self.assertEqual(CYCLE255_N_I_ONLY, 1)
        self.assertEqual(CYCLE255_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE255_IA2_174_LINE_FINAL)
        prior_254 = self.survey["i_3gram_090_076_000_i_only"]
        self.assertEqual(prior_254["cycle"], 254)
        self.assertEqual(prior_254["N_I"], 2)
        self.assertEqual(prior_254["N_off_I"], 0)
        self.assertEqual(prior_254["N_extra"], 0)
        self.assertTrue(prior_254["i_3gram_090_076_000_i_only"])
        self.assertTrue(CYCLE254_CLAIM)
        self.assertEqual(CYCLE254_N_I, 2)
        self.assertEqual(CYCLE254_N_OFF_I, 0)
        self.assertEqual(CYCLE254_N_EXTRA, 0)
        prior_253 = self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]
        self.assertEqual(prior_253["cycle"], 253)
        self.assertEqual(prior_253["G"], "000")
        self.assertEqual(prior_253["K"], 2)
        self.assertEqual(prior_253["N_remaining10"], 21)
        self.assertEqual(prior_253["N_without"], 19)
        self.assertTrue(prior_253["i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"])
        self.assertTrue(CYCLE253_CLAIM)
        self.assertEqual(CYCLE253_G, "000")
        self.assertEqual(CYCLE253_K, 2)
        self.assertEqual(CYCLE253_N_REMAINING10, 21)
        self.assertEqual(CYCLE253_N_WITHOUT, 19)
        prior_234 = self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]
        self.assertEqual(prior_234["cycle"], 234)
        self.assertEqual(prior_234["N_remaining4"], 33)
        self.assertEqual(prior_234["N_tied_at_K"], 7)
        self.assertFalse(prior_234["G_uniquely_most_frequent"])
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_000_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_19_remaining11_all_hapax_g_755_k_1_and_hypothesis_loses(self):
        """N_remaining11=19, N_distinct=19, G=755 K=1 tied. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(self.n_share_070, STANDING_N_SHARE_070)
        self.assertEqual(self.share_070, CYCLE226_MATCHING_SITES)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(self.n_share_071, STANDING_N_SHARE_071)
        self.assertEqual(self.n_remaining2, STANDING_N_REMAINING2)
        self.assertEqual(self.n_share_013, STANDING_N_SHARE_013)
        self.assertEqual(self.n_remaining3, STANDING_N_REMAINING3)
        self.assertEqual(self.n_share_001, STANDING_N_SHARE_001)
        self.assertEqual(self.n_remaining4, STANDING_N_REMAINING4)
        self.assertEqual(self.remaining4, CYCLE234_REMAINING4_SITES)
        self.assertEqual(self.n_share_700, STANDING_N_SHARE_700)
        self.assertEqual(self.share_700, CYCLE235_MATCHING_SITES)
        self.assertEqual(self.n_remaining5, STANDING_N_REMAINING5)
        self.assertEqual(self.n_share_530, STANDING_N_SHARE_530)
        self.assertEqual(self.share_530, CYCLE238_MATCHING_SITES)
        self.assertEqual(self.n_remaining6, STANDING_N_REMAINING6)
        self.assertEqual(self.n_share_280, STANDING_N_SHARE_280)
        self.assertEqual(self.share_280, CYCLE241_MATCHING_SITES)
        self.assertEqual(self.n_remaining7, STANDING_N_REMAINING7)
        self.assertEqual(self.n_share_087, STANDING_N_SHARE_087)
        self.assertEqual(self.share_087, CYCLE244_MATCHING_SITES)
        self.assertEqual(self.n_remaining8, STANDING_N_REMAINING8)
        self.assertEqual(self.n_share_011, STANDING_N_SHARE_011)
        self.assertEqual(self.share_011, CYCLE247_MATCHING_SITES)
        self.assertEqual(self.n_remaining9, STANDING_N_REMAINING9)
        self.assertEqual(self.n_share_005, STANDING_N_SHARE_005)
        self.assertEqual(self.share_005, CYCLE250_MATCHING_SITES)
        self.assertEqual(self.n_remaining10, STANDING_N_REMAINING10)
        self.assertEqual(STANDING_N_REMAINING10, 21)
        self.assertEqual(self.n_remaining10, CYCLE253_N_REMAINING10)
        self.assertEqual(self.remaining10, STANDING_REMAINING10_SITES)
        self.assertEqual(self.n_share_000, STANDING_N_SHARE_000)
        self.assertEqual(self.share_000, CYCLE253_MATCHING_SITES)
        self.assertEqual(self.share_000, CYCLE254_I_SITES)
        if self.share_000 != CYCLE253_MATCHING_SITES:
            self.fail("leftover extra remaining-after-005 2 share 000 drifted from cycle-253 pair")
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
            or self.n_remaining4 != 33
            or self.n_share_700 != 2
            or self.n_remaining5 != 31
            or self.n_share_530 != 2
            or self.n_remaining6 != 29
            or self.n_share_280 != 2
            or self.n_remaining7 != 27
            or self.n_share_087 != 2
            or self.n_remaining8 != 25
            or self.n_share_011 != 2
            or self.n_remaining9 != 23
            or self.n_share_005 != 2
            or self.n_remaining10 != 21
            or self.n_share_000 != 2
        ):
            self.fail(
                "nested leftover extra 56/55/1 through remaining-after-005 21/2/000 drifted"
            )
        self.assertTrue(
            leftover_extra_remaining_after_000_nested_counts_hold(
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
                self.n_share_700,
                self.n_remaining5,
                self.n_share_530,
                self.n_remaining6,
                self.n_share_280,
                self.n_remaining7,
                self.n_share_087,
                self.n_remaining8,
                self.n_share_011,
                self.n_remaining9,
                self.n_share_005,
                self.n_remaining10,
                self.n_share_000,
                self.n_remaining11,
            )
        )
        self.assertEqual(self.n_remaining11, STANDING_N_REMAINING11)
        self.assertEqual(STANDING_N_REMAINING11, 19)
        self.assertEqual(self.n_remaining11, CYCLE253_N_WITHOUT)
        self.assertEqual(self.n_remaining11, self.n_remaining10 - self.n_share_000)
        self.assertEqual(21 - 2, 19)
        if self.n_remaining11 != 19:
            self.fail("measured N_remaining11 drifted from 19")
        if self.n_remaining11 != self.n_remaining10 - self.n_share_000:
            self.fail("leftover extra remaining-after-000 filter disagrees with nested 21−2")
        self.assertEqual(self.remaining11, STANDING_REMAINING11_SITES)
        self.assertEqual(self.remaining11_stems, STANDING_REMAINING11_NEXT_STEMS)
        self.assertEqual(len(self.remaining11), len(self.remaining11_stems))
        self.assertEqual(
            self.remaining11,
            leftover_extra_remaining_after_005_without_000(
                self.leftover_sites,
                self.next_stems,
            ),
        )
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.remaining11)
        self.assertNotIn(STANDING_IA2_174, self.remaining11)
        self.assertIn(STANDING_IA2_174, self.remaining10)
        self.assertIn(STANDING_IA2_174, self.share_000)
        self.assertEqual(STANDING_IA2_174_NEXT_STEM, "000")
        self.assertTrue(STANDING_IA2_174_IS_REMAINING_AFTER_005_000_NOT_REMAINING_AFTER_000)
        for site in self.share_000:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_070:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_071:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_013:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_001:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_700:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_530:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_280:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_087:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_011:
            self.assertNotIn(site, self.remaining11)
        for site in self.share_005:
            self.assertNotIn(site, self.remaining11)
        self.assertEqual(self.n_distinct_remaining11, STANDING_N_DISTINCT_REMAINING11)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING11, 19)
        self.assertEqual(self.frequency, STANDING_REMAINING11_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "755")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 1)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "755")
        self.assertEqual(self.frequency[0][1], 1)
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 19)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX_REMAINING11)
        self.assertEqual(STANDING_N_HAPAX_REMAINING11, 19)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 18)
        self.assertEqual(self.k + self.n_without, self.n_remaining11)
        self.assertEqual(1 + 18, 19)
        rem4_g, rem4_k, rem4_unique = select_remaining_after_001_g(self.remaining4_stems)
        self.assertEqual(rem4_g, "700")
        self.assertEqual(rem4_k, 2)
        self.assertFalse(rem4_unique)
        rem4_tied = tuple(
            stem for stem, count, _sites, _grams in self.remaining4_frequency if count == 2
        )
        self.assertEqual(rem4_tied, CYCLE234_TIED_STEMS)
        self.assertEqual(len(rem4_tied), 7)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
                self.leftover_sites,
                self.next_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM,
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE253)
        self.assertFalse(STANDING_SAME_AS_CYCLE254)
        self.assertFalse(STANDING_SAME_AS_CYCLE255)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_000_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertTrue(CYCLE226_CLAIM)
        self.assertTrue(CYCLE227_CLAIM)
        self.assertTrue(CYCLE228_CLAIM)
        self.assertTrue(CYCLE231_CLAIM)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertTrue(CYCLE235_CLAIM)
        self.assertTrue(CYCLE238_CLAIM)
        self.assertTrue(CYCLE241_CLAIM)
        self.assertTrue(CYCLE244_CLAIM)
        self.assertTrue(CYCLE247_CLAIM)
        self.assertTrue(CYCLE250_CLAIM)
        self.assertTrue(CYCLE253_CLAIM)
        self.assertTrue(CYCLE254_CLAIM)
        self.assertTrue(CYCLE255_CLAIM)
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_remaining_after_000_tiebreak_g_is_755(self):
        """Tie-break G=755 is one leftover extra remaining-after-000 hapax at Ia1[27]."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        site = STANDING_MATCHING_SITES[0]
        want_nxt = STANDING_MATCHING_NEXT_4GRAMS[0]
        stems = line_stems_for_site(self.i_sides, site)
        side, line, index = site
        self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
        self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3_FORWARD)
        self.assertEqual(stems[index + STANDING_N2], "755")
        self.assertEqual(site_next_stem(stems, index, GRAM2), "755")
        self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
        self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
        self.assertEqual(side, SIDE_IA)
        self.assertEqual(line, "Ia1")
        self.assertIn(site, STANDING_LEFTOVER_SITES)
        self.assertIn(site, STANDING_REMAINING11_SITES)
        self.assertIn(site, STANDING_REMAINING10_SITES)
        self.assertIn(site, CYCLE234_REMAINING4_SITES)
        self.assertNotIn(site, CYCLE224_INSIDE_SITES)
        self.assertNotIn(site, CYCLE226_MATCHING_SITES)
        self.assertNotIn(site, CYCLE253_MATCHING_SITES)
        self.assertNotIn(site, CYCLE254_I_SITES)
        self.assertNotIn(STANDING_IA2_174, self.matching)
        self.assertNotIn(STANDING_IA2_174, self.remaining11)
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.matching)
        self.assertEqual(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_IA2_174)],
            "000",
        )
        self.assertIsNone(
            self.next_4grams[STANDING_LEFTOVER_SITES.index(STANDING_IA2_174)]
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
            self.assertNotEqual(nxt, "755")
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS_AFTER_000)
            self.assertIn(site, STANDING_REMAINING11_SITES)
        for site in self.share_000:
            self.assertNotIn(site, self.remaining11)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE253_MATCHING_SITES)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining11)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining11)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_000_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_255_254_253_234_223_and_171_still_compute(self):
        """Cycle 255 1/0 + line-final, 254 2/0 extra I=0, 253 K=2/G=000 N_remaining10=21, 234 7-way tie, 223 69/3, 171 43/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_255 = TestMamariI090076000Forward4gramsIOnlyScoreboard()
        prior_255.setUp()
        prior_255.test_each_4gram_is_one_on_i_zero_off_i_ia2_174_line_final_and_claim_holds()
        prior_255.test_survey_matches_computed_lock()
        self.assertEqual(prior_255.n_i_only, 1)
        self.assertEqual(prior_255.n_not_i_only, 0)
        self.assertTrue(prior_255.claim_holds)
        self.assertTrue(CYCLE255_CLAIM)
        self.assertTrue(CYCLE255_IA2_174_LINE_FINAL)
        if prior_255.n_i_only != 1 or prior_255.n_not_i_only != 0:
            self.fail("nested cycle 255 090 076 000 forward 4-grams 1/0 + line-final drifted")
        prior_254 = TestMamariI3gram090076000IOnlyScoreboard()
        prior_254.setUp()
        prior_254.test_i_hits_are_two_on_ia_and_equal_leftover_extra_000()
        prior_254.test_3gram_is_zero_off_i_and_i_only()
        prior_254.test_survey_matches_computed_lock()
        self.assertEqual(prior_254.i_hits, CYCLE254_N_I)
        self.assertEqual(prior_254.i_hits, 2)
        self.assertEqual(prior_254.off_i_hits, CYCLE254_N_OFF_I)
        self.assertEqual(prior_254.off_i_hits, 0)
        self.assertEqual(len(prior_254.extra), CYCLE254_N_EXTRA)
        self.assertEqual(len(prior_254.extra), 0)
        self.assertEqual(prior_254.extra, CYCLE254_EXTRA_I_SITES)
        self.assertEqual(prior_254.i_sites, CYCLE254_I_SITES)
        self.assertTrue(prior_254.claim_holds)
        self.assertTrue(CYCLE254_CLAIM)
        if prior_254.i_hits != 2 or prior_254.off_i_hits != 0 or prior_254.extra:
            self.fail("nested cycle 254 090 076 000 I-only 2/0 extra I=0 drifted")
        prior_253 = TestMamariILeftoverExtra090076RemainingAfter005Fwd000Scoreboard()
        prior_253.setUp()
        prior_253.test_counts_2_of_21_and_hypothesis_k_2_holds()
        prior_253.test_survey_matches_computed_lock()
        self.assertEqual(prior_253.n_leftover, 56)
        self.assertEqual(prior_253.n_remaining10, 21)
        self.assertEqual(prior_253.k, 2)
        self.assertEqual(CYCLE253_G, "000")
        self.assertEqual(prior_253.matching, CYCLE253_MATCHING_SITES)
        self.assertEqual(self.share_000, prior_253.matching)
        self.assertTrue(prior_253.claim_holds)
        self.assertTrue(CYCLE253_CLAIM)
        if (
            prior_253.n_leftover != 56
            or prior_253.n_remaining10 != 21
            or prior_253.k != 2
        ):
            self.fail(
                "nested cycle 253 leftover extra remaining-after-005 exactly 2 share 000 drifted"
            )
        prior_234 = TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard()
        prior_234.setUp()
        prior_234.test_counts_33_remaining4_g_700_k_2_and_hypothesis_loses()
        prior_234.test_survey_matches_computed_lock()
        self.assertEqual(prior_234.n_leftover, 56)
        self.assertEqual(prior_234.n_remaining4, 33)
        self.assertEqual(prior_234.n_distinct_remaining4, 26)
        self.assertEqual(prior_234.k, 2)
        self.assertFalse(prior_234.unique)
        self.assertFalse(prior_234.claim_holds)
        self.assertFalse(CYCLE234_CLAIM)
        if (
            prior_234.n_leftover != 56
            or prior_234.n_remaining4 != 33
            or prior_234.n_distinct_remaining4 != 26
            or prior_234.k != 2
            or prior_234.unique
        ):
            self.fail(
                "nested cycle 234 leftover extra remaining-after-001 33 / "
                "26 distinct / 7-way tie G=700 K=2 drifted"
            )
        tied = tuple(
            stem for stem, count, _sites, _grams in prior_234.frequency if count == 2
        )
        self.assertEqual(tied, CYCLE234_TIED_STEMS)
        self.assertEqual(len(tied), 7)
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, STANDING_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, STANDING_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
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
        """CORPUS_SURVEY.json records the cycle-256 leftover extra remaining-after-000 lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]
        self.assertEqual(lock["cycle"], 256)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(tuple(lock["forward_3gram"]), ("090", "076", "755"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(
            tuple(lock["locked_forward_stems_after_000"]),
            LOCKED_FORWARD_STEMS_AFTER_000,
        )
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(lock["N_share_070"], 8)
        self.assertEqual(lock["N_remaining"], 47)
        self.assertEqual(lock["N_share_071"], 6)
        self.assertEqual(lock["N_remaining2"], 41)
        self.assertEqual(lock["N_share_013"], 5)
        self.assertEqual(lock["N_remaining3"], 36)
        self.assertEqual(lock["N_share_001"], 3)
        self.assertEqual(lock["N_remaining4"], 33)
        self.assertEqual(lock["N_share_700"], 2)
        self.assertEqual(lock["N_remaining5"], 31)
        self.assertEqual(lock["N_share_530"], 2)
        self.assertEqual(lock["N_remaining6"], 29)
        self.assertEqual(lock["N_share_280"], 2)
        self.assertEqual(lock["N_remaining7"], 27)
        self.assertEqual(lock["N_share_087"], 2)
        self.assertEqual(lock["N_remaining8"], 25)
        self.assertEqual(lock["N_share_011"], 2)
        self.assertEqual(lock["N_remaining9"], 23)
        self.assertEqual(lock["N_share_005"], 2)
        self.assertEqual(lock["N_remaining10"], 21)
        self.assertEqual(lock["N_share_000"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_000_sites"]),
            CYCLE253_MATCHING_SITES,
        )
        self.assertEqual(lock["ia2_174_next_stem"], "000")
        self.assertTrue(lock["ia2_174_is_remaining_after_005_000_not_remaining_after_000"])
        self.assertEqual(lock["N_remaining11"], STANDING_N_REMAINING11)
        self.assertEqual(lock["N_remaining11"], 19)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_000_sites"]),
            STANDING_REMAINING11_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_000_next_stems"]),
            STANDING_REMAINING11_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_remaining11"], STANDING_N_DISTINCT_REMAINING11)
        self.assertEqual(lock["N_distinct_remaining11"], 19)
        self.assertEqual(lock["N_hapax_remaining11"], STANDING_N_HAPAX_REMAINING11)
        self.assertEqual(lock["N_hapax_remaining11"], 19)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "755")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 1)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 19)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 18)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_000_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_000_local_4grams"],
            matching_leftover_extra_remaining_after_000_local_4gram_rows(),
        )
        self.assertEqual(
            lock["remaining_after_000_next_stem_frequency"],
            remaining_after_000_next_stem_frequency_rows(),
        )
        self.assertEqual(lock["cycle255_N_i_only"], 1)
        self.assertEqual(lock["cycle255_N_not_i_only"], 0)
        self.assertTrue(lock["cycle255_ia2_174_line_final"])
        self.assertEqual(lock["cycle254_N_I"], 2)
        self.assertEqual(lock["cycle254_N_off_I"], 0)
        self.assertEqual(lock["cycle254_N_extra"], 0)
        self.assertEqual(lock["cycle253_G"], "000")
        self.assertEqual(lock["cycle253_K"], 2)
        self.assertEqual(lock["cycle253_N_remaining10"], 21)
        self.assertEqual(lock["cycle234_N_remaining4"], 33)
        self.assertEqual(lock["cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["cycle234_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle223_N_I"], 69)
        self.assertEqual(lock["cycle223_N_off_I"], 3)
        self.assertEqual(lock["cycle171_N_I"], 43)
        self.assertEqual(lock["cycle171_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle226"])
        self.assertFalse(lock["same_as_cycle234"])
        self.assertFalse(lock["same_as_cycle253"])
        self.assertFalse(lock["same_as_cycle254"])
        self.assertFalse(lock["same_as_cycle255"])
        self.assertTrue(lock["same_claim_shape_as_cycle234"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_remaining_after_000_3gram_is_not_this_cycle"])
        self.assertTrue(lock["previous_4grams_of_090_076_000_are_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["ia2_174_is_remaining_after_005_000_not_remaining_after_000"])
        self.assertTrue(lock["cycle224_no_next_4gram_is_not_no_next_token"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_090_076_000_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_005_fwd000_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_090_076_000_forward_4grams_i_only"]["cycle"], 255)
        self.assertTrue(
            self.survey["i_090_076_000_forward_4grams_i_only"][
                "i_090_076_000_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_000_forward_4grams_i_only"]["N_i_only"], 1)
        self.assertTrue(self.survey["i_090_076_000_forward_4grams_i_only"]["ia2_174_line_final"])
        self.assertEqual(self.survey["i_3gram_090_076_000_i_only"]["cycle"], 254)
        self.assertTrue(self.survey["i_3gram_090_076_000_i_only"]["i_3gram_090_076_000_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_000_i_only"]["N_extra"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["cycle"],
            253,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"][
                "i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"
            ]
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter000NextStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 256 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
