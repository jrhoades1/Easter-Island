"""I's leftover n=4 remaining remaining-after-011 next-stem lock.

Cycle 298 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–287), leftover n=4 remaining
share-one-forward-stem (cycle 288 lost), leftover n=4
remaining exactly 4 share next 020 (cycle 289), leftover n=4
remaining remaining-after-020 unique next stem (cycle 292),
leftover n=4 remaining remaining-after-020 exactly 3 share
next 087 (cycle 293), leftover n=4 remaining remaining-
after-087 unique next stem (cycle 294 lost), leftover n=4
remaining remaining-after-087 exactly 2 share next 057
(cycle 295), leftover n=4 remaining remaining-after-057
unique next stem (cycle 296), leftover n=4 remaining
remaining-after-057 exactly 2 share next 011 (cycle 297),
3-gram 090 076 011 I-only (cycle 248), or leftover extra
remaining-after-011 exactly 2 share next 005 (cycle 250).
Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Leftover n=4 remaining remaining-after-011 next stems are
not yet locked as unique-max. Cycle 296 unique-max G/K and
cycle 297 exact-K 011 peel are inventory for the 011 peel,
not remaining-after-011 unique-max. Cycle 296/297 frequency
of remaining-after-057 minus 011 (hapax 607/021) is nested
inventory, not this claim; measure remaining-after-011 from
the 2 sites. Cycle 248 leftover extra 090 076 011 I-only
4/0 extra I=2 equals leftover n=4 remaining remaining-after-
057 011 sites; do not retune 247/248. Cycle 250 leftover
extra remaining-after-011 exactly 2 share next 005 is a
different leftover-extra population; do not retune 249/250.
Do not peel a specific remaining-after-011 stem this cycle.
Do not lock I-only of remaining-after-011 3-grams this
cycle. Off-I T sites are not this cycle. 076 071 and
076 070 do not count as this 2-gram. Leftover extra sites
do not count as leftover n=4 remaining.

Leftover n=4 remaining remaining-after-011 = leftover n=4
remaining I 090 076 sites whose next token is none of 020,
087, 057, or 011. For each such site, take the next token
if any (lock line-final / no-next count separately). Nested-
check leftover n=4 remaining N_inside==13, K_020==4,
N_remaining_after_020==9, K_087==3, N_remaining_after_087==6,
K_057==2, N_remaining_after_057==4, K_011==2,
N_remaining_after_011==2 (do not retune
224/288/289/292/293/294/295/296/297). Nested-check cycle 248
extra I equals leftover n=4 remaining remaining-after-057
011 sites (do not retune 248/297). Record (do not fail the
unique-max claim on) site-level overlap of remaining-after-
011 with leftover extra remaining-after-000 extra I (cycle
258 extra I=3; cycle 259 extra-I including 057/607). Count
next-stem frequencies among remaining-after-011 sites that
have a next token. G = the next stem with the highest
remaining-after-011 with-next count. If a tie, pick the
larger Barthel id. K = that count.

Claim that can lose:
i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem.
True iff remaining-after-011 leftover n=4 remaining I
090 076 has N_remaining_after_011==2 and a unique most
frequent next stem G with K ≥ 2 (no tie at max K; not a
hapax pile). This can lose the same way cycle 256 lost
(19 hapax, G=755 K=1) and cycle 294 lost (2-way tie at
K=2), or hold the same way cycle 292 held (G=087 K=3) and
cycle 296 held (G=011 K=2). Unique-max G/K is inventory
for a later peel if the claim holds or loses with K≥2.
Measured: N_remaining_after_011=2, N_with_next=2,
N_no_next=0, N_distinct=2, all hapax (607 at Ia8[106] /
021 at Ia13[17]), G=607 (largest-id tie-break), unique-max
false. The claim is false. Nested cycle 297 K_011=2
N_remaining=2 extra I overlap, cycle 296 unique-max G=011
K=2, cycle 294 unique-max false 2-way tie G=057 K=2, cycle
292 unique-max G=087 K=3, cycle 258 extra I=3 / cycle 259
extra-I 057/607, cycle 250 leftover extra remaining-after-
011 exactly 2 share 005, cycle 248 4/0 extra I=2, cycle
224 13/56, and cycle 223 69/3 stay. Do not assume the
result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
    leftover_local_4grams,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_OFF_I,
    STANDING_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    GRAM3 as CYCLE248_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE248_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_011_I_ONLY as CYCLE248_CLAIM,
    STANDING_I_SITES as CYCLE248_I_SITES,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE248_LEFTOVER_MATCHING_SITES,
    STANDING_N_EXTRA as CYCLE248_N_EXTRA,
    STANDING_N_I as CYCLE248_N_I,
    STANDING_N_OFF_I as CYCLE248_N_OFF_I,
    TestMamariI3gram090076011IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    group_sites_by_next_stem,
    leftover_sites_with_next,
    leftover_sites_without_next,
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE258_N_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_BY_X as CYCLE259_EXTRA_I_BY_X,
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_DISTINCT_REMAINING11 as CYCLE256_N_DISTINCT,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G as CYCLE234_CLAIM,
    STANDING_K as CYCLE234_K,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_011_fwd005_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_011_EXACTLY_2_SHARE_005 as CYCLE250_CLAIM,
    STANDING_K as CYCLE250_K,
    STANDING_MATCHING_SITES as CYCLE250_MATCHING_SITES,
    TestMamariILeftoverExtra090076RemainingAfter011Fwd005Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    STANDING_G as CYCLE270_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE270_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED_AT_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    barthel_id,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_020_scoreboard import (
    GRAM3_FORWARD as GRAM3_NESTED_020,
    STANDING_G as CYCLE289_G,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020 as CYCLE289_CLAIM,
    STANDING_K as CYCLE289_K,
    STANDING_MATCHING_SITES as CYCLE289_MATCHING_SITES,
    STANDING_N_INSIDE as CYCLE289_N_INSIDE,
    STANDING_N_REMAINING_AFTER_020 as CYCLE289_N_REMAINING_AFTER_020,
    STANDING_REMAINING_AFTER_020_SITES as CYCLE289_REMAINING_AFTER_020_SITES,
    TestMamariILeftoverN4Remaining090076Forward020Scoreboard,
    leftover_n4_remaining_with_forward_020,
    leftover_n4_remaining_without_forward_020,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE288_N_INSIDE,
    STANDING_N_NO_NEXT as CYCLE288_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE288_N_WITH_NEXT,
    STANDING_NEXT_STEM_FREQUENCY as CYCLE288_FREQUENCY,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
    leftover_n4_remaining_forward_3grams,
    leftover_n4_remaining_next_4grams,
    leftover_n4_remaining_next_stems,
    leftover_n4_remaining_sites_with_next,
    leftover_n4_remaining_sites_without_next,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_forward_087_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087 as CYCLE293_CLAIM,
    STANDING_K_087 as CYCLE293_K_087,
    STANDING_MATCHING_EQUALS_CYCLE245_EXTRA_I as CYCLE293_EQUALS_245,
    STANDING_MATCHING_SITES as CYCLE293_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_020 as CYCLE293_N_REMAINING_AFTER_020,
    STANDING_N_REMAINING_AFTER_087 as CYCLE293_N_REMAINING_AFTER_087,
    STANDING_REMAINING_AFTER_087_SITES as CYCLE293_REMAINING_AFTER_087_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter020Forward087Scoreboard,
    leftover_n4_remaining_remaining_after_020_with_forward_087,
    leftover_n4_remaining_remaining_after_020_without_forward_087,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_scoreboard import (
    STANDING_G as CYCLE292_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE292_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_UNIQUE_NEXT_STEM as CYCLE292_CLAIM,
    STANDING_K as CYCLE292_K,
    STANDING_MATCHING_SITES as CYCLE292_MATCHING_SITES,
    STANDING_N_DISTINCT as CYCLE292_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_020 as CYCLE292_N_REMAINING,
    STANDING_REMAINING_FREQUENCY as CYCLE292_REMAINING_FREQUENCY,
    STANDING_REMAINING_SITES as CYCLE292_REMAINING_SITES,
    leftover_n4_remaining_remaining_after_020,
    leftover_n4_remaining_remaining_after_020_nested_counts_hold,
    leftover_n4_remaining_remaining_after_020_next_stems,
    leftover_n4_remaining_remaining_after_020_with_next,
    leftover_n4_remaining_remaining_after_020_without_next,
    TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011 as CYCLE297_CLAIM,
    STANDING_K_011 as CYCLE297_K_011,
    STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I as CYCLE297_EQUALS_248,
    STANDING_MATCHING_SITES as CYCLE297_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_011 as CYCLE297_N_REMAINING_AFTER_011,
    STANDING_N_REMAINING_AFTER_057 as CYCLE297_N_REMAINING_AFTER_057,
    STANDING_REMAINING_AFTER_011_SITES as CYCLE297_REMAINING_AFTER_011_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter057Forward011Scoreboard,
    leftover_n4_remaining_remaining_after_057_with_forward_011,
    leftover_n4_remaining_remaining_after_057_without_forward_011,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_057_next_stem_scoreboard import (
    STANDING_G as CYCLE296_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE296_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_UNIQUE_NEXT_STEM as CYCLE296_CLAIM,
    STANDING_K as CYCLE296_K,
    STANDING_MATCHING_EQUALS_CYCLE248_EXTRA_I as CYCLE296_EQUALS_248,
    STANDING_MATCHING_SITES as CYCLE296_MATCHING_SITES,
    STANDING_N_DISTINCT as CYCLE296_N_DISTINCT,
    STANDING_N_HAPAX as CYCLE296_N_HAPAX,
    STANDING_N_REMAINING_AFTER_057 as CYCLE296_N_REMAINING,
    STANDING_REMAINING_FREQUENCY as CYCLE296_REMAINING_FREQUENCY,
    STANDING_REMAINING_SITES as CYCLE296_REMAINING_SITES,
    leftover_n4_remaining_remaining_after_057,
    leftover_n4_remaining_remaining_after_057_nested_counts_hold,
    leftover_n4_remaining_remaining_after_057_next_stems,
    leftover_n4_remaining_remaining_after_057_with_next,
    leftover_n4_remaining_remaining_after_057_without_next,
    matching_equals_cycle248_extra_i,
    TestMamariILeftoverN4Remaining090076RemainingAfter057NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_087_forward_057_scoreboard import (
    CYCLE258_EXTRA_I_057,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_EXACTLY_2_SHARE_FORWARD_057 as CYCLE295_CLAIM,
    STANDING_K_057 as CYCLE295_K_057,
    STANDING_MATCHING_EQUALS_CYCLE258_EXTRA_I as CYCLE295_EQUALS_258,
    STANDING_MATCHING_SITES as CYCLE295_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_057 as CYCLE295_N_REMAINING_AFTER_057,
    STANDING_N_REMAINING_AFTER_087 as CYCLE295_N_REMAINING_AFTER_087,
    STANDING_REMAINING_AFTER_057_SITES as CYCLE295_REMAINING_AFTER_057_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter087Forward057Scoreboard,
    leftover_n4_remaining_remaining_after_087_with_forward_057,
    leftover_n4_remaining_remaining_after_087_without_forward_057,
    matching_equals_cycle258_extra_i_057,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_087_next_stem_scoreboard import (
    STANDING_G as CYCLE294_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE294_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_UNIQUE_NEXT_STEM as CYCLE294_CLAIM,
    STANDING_K as CYCLE294_K,
    STANDING_MATCHING_SITES as CYCLE294_MATCHING_SITES,
    STANDING_N_DISTINCT as CYCLE294_N_DISTINCT,
    STANDING_N_HAPAX as CYCLE294_N_HAPAX,
    STANDING_N_REMAINING_AFTER_087 as CYCLE294_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE294_N_TIED,
    STANDING_REMAINING_FREQUENCY as CYCLE294_REMAINING_FREQUENCY,
    STANDING_REMAINING_SITES as CYCLE294_REMAINING_SITES,
    STANDING_TIED_STEMS as CYCLE294_TIED_STEMS,
    leftover_n4_remaining_remaining_after_087,
    leftover_n4_remaining_remaining_after_087_nested_counts_hold,
    leftover_n4_remaining_remaining_after_087_next_stems,
    leftover_n4_remaining_remaining_after_087_with_next,
    leftover_n4_remaining_remaining_after_087_without_next,
    TestMamariILeftoverN4Remaining090076RemainingAfter087NextStemScoreboard,
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

LOCKED_FORWARD_STEMS = ("020", "087", "057", "011")
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "607")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_NEXT_INSIDE = 13
STANDING_N_NO_NEXT_INSIDE = 0
STANDING_K_020 = 4
STANDING_N_REMAINING_AFTER_020 = 9
STANDING_K_087 = 3
STANDING_N_REMAINING_AFTER_087 = 6
STANDING_K_057 = 2
STANDING_N_REMAINING_AFTER_057 = 4
STANDING_K_011 = 2
STANDING_N_REMAINING_AFTER_011 = 2
STANDING_N_WITH_NEXT = 2
STANDING_N_NO_NEXT = 0
STANDING_NO_NEXT_SITES = ()
STANDING_N_DISTINCT = 2
STANDING_N_HAPAX = 2
STANDING_G = "607"
STANDING_K = 1
STANDING_N_WITHOUT_G = 1
STANDING_N_TIED_AT_K = 2
STANDING_TIED_STEMS = ("607", "021")
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_REMAINING_SITES = CYCLE297_REMAINING_AFTER_011_SITES
STANDING_REMAINING_NEXT_STEMS = (
    "607",
    "021",
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia8", 106),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "607", "755"),
)
STANDING_WITHOUT_G_SITES = (
    (SIDE_IA, "Ia13", 17),
)
STANDING_WITHOUT_G_NEXT_4GRAMS = (
    ("090", "076", "021", "020"),
)
STANDING_REMAINING_FREQUENCY = (
    ("607", 1, STANDING_MATCHING_SITES, (("090", "076", "607"),)),
    ("021", 1, STANDING_WITHOUT_G_SITES, (("090", "076", "021"),)),
)
STANDING_CYCLE296_REMAINING_AFTER_011_INVENTORY = (
    ("607", 1),
    ("021", 1),
)
STANDING_OVERLAP_CYCLE258_EXTRA_I = (
    (SIDE_IA, "Ia8", 106),
)
STANDING_OVERLAP_CYCLE259_EXTRA_I = (
    (SIDE_IA, "Ia8", 106),
)
STANDING_OVERLAP_CYCLE258_EXTRA_I_607 = True
STANDING_OVERLAP_CYCLE259_EXTRA_I_607 = True
STANDING_OVERLAP_CYCLE258_EXTRA_I_057 = False
STANDING_IA13_OVERLAPS_CYCLE258_OR_259 = False
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem"
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_UNIQUE_NEXT_STEM = False
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_011_next_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE234 = False
STANDING_SAME_AS_CYCLE248 = False
STANDING_SAME_AS_CYCLE250 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_AS_CYCLE258 = False
STANDING_SAME_AS_CYCLE259 = False
STANDING_SAME_AS_CYCLE270 = False
STANDING_SAME_AS_CYCLE288 = False
STANDING_SAME_AS_CYCLE289 = False
STANDING_SAME_AS_CYCLE292 = False
STANDING_SAME_AS_CYCLE293 = False
STANDING_SAME_AS_CYCLE294 = False
STANDING_SAME_AS_CYCLE295 = False
STANDING_SAME_AS_CYCLE296 = False
STANDING_SAME_AS_CYCLE297 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE294 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE296 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_REMAINING_AFTER_011_3GRAM_IS_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_090_076_011_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_011_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_DO_NOT_PEEL_607 = True
STANDING_CYCLE296_FREQUENCY_MINUS_011_IS_NESTED_INVENTORY = True
STANDING_CYCLE297_EXACT_K_011_IS_NESTED_INVENTORY = True
STANDING_CYCLE248_EXTRA_I_EQUALS_REMAINING_AFTER_057_011 = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_CYCLE167_268_297_NOT_OVERWRITTEN = True
STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL = True


def leftover_n4_remaining_remaining_after_011(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose next token is none of 020, 087, 057, 011."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt not in locked_set
    )


def leftover_n4_remaining_remaining_after_011_next_stems(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[str, ...]:
    """Next stems of remaining-after-011 sites that have a next token."""
    locked_set = set(locked)
    return tuple(
        nxt
        for nxt in next_stems
        if nxt is not None and nxt not in locked_set
    )


def leftover_n4_remaining_remaining_after_011_with_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-011 leftover n=4 remaining sites that have a next token."""
    remaining = leftover_n4_remaining_remaining_after_011(sites, next_stems, locked)
    rem_next = tuple(
        nxt
        for site, nxt in zip(sites, next_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_with_next(remaining, rem_next)


def leftover_n4_remaining_remaining_after_011_without_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-011 leftover n=4 remaining sites with no next token."""
    remaining = leftover_n4_remaining_remaining_after_011(sites, next_stems, locked)
    rem_next = tuple(
        nxt
        for site, nxt in zip(sites, next_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_without_next(remaining, rem_next)


def leftover_n4_remaining_remaining_after_011_with_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-011 sites whose next token is G."""
    remaining = set(leftover_n4_remaining_remaining_after_011(sites, next_stems, locked))
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem and site in remaining
    )


def leftover_n4_remaining_remaining_after_011_without_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-011 sites whose next token is not G."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set and nxt != stem
    )


def remaining_after_011_next_stem_counts(next_stems: tuple[str, ...]) -> Counter:
    """Counts of next stems among leftover n=4 remaining remaining-after-011 with-next."""
    return Counter(next_stems)


def rank_remaining_after_011_next_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining-after-011 next stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_after_011_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining-after-011 has no G."""
    ranked = rank_remaining_after_011_next_stems(
        remaining_after_011_next_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_after_011_next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    forward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining-after-011 next-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_n4_remaining_remaining_after_011_with_next(
        sites, next_stems, locked
    )
    rem_stems = leftover_n4_remaining_remaining_after_011_next_stems(
        sites, next_stems, locked
    )
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


def remaining_after_011_next_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining-after-011 next-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "next_stem": stem,
                "count": count,
                "leftover_n4_remaining_remaining_after_011_sites": [
                    list(site) for site in sites
                ],
                "forward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def leftover_n4_remaining_remaining_after_011_nested_counts_hold(
    n_inside: int,
    k_020: int,
    n_remaining_after_020: int,
    k_087: int,
    n_remaining_after_087: int,
    k_057: int,
    n_remaining_after_057: int,
    k_011: int,
    n_remaining: int,
    expected_inside: int = STANDING_N_INSIDE,
    expected_k_020: int = STANDING_K_020,
    expected_remaining_after_020: int = STANDING_N_REMAINING_AFTER_020,
    expected_k_087: int = STANDING_K_087,
    expected_remaining_after_087: int = STANDING_N_REMAINING_AFTER_087,
    expected_k_057: int = STANDING_K_057,
    expected_remaining_after_057: int = STANDING_N_REMAINING_AFTER_057,
    expected_k_011: int = STANDING_K_011,
    expected_remaining: int = STANDING_N_REMAINING_AFTER_011,
) -> bool:
    """Nested leftover n=4 remaining 13/4/9/3/6/2/4/2/2."""
    return (
        n_inside == expected_inside
        and k_020 == expected_k_020
        and n_remaining_after_020 == expected_remaining_after_020
        and k_087 == expected_k_087
        and n_remaining_after_087 == expected_remaining_after_087
        and k_057 == expected_k_057
        and n_remaining_after_057 == expected_remaining_after_057
        and k_011 == expected_k_011
        and n_remaining == expected_remaining
        and n_remaining_after_020 == n_inside - k_020
        and n_remaining_after_087 == n_remaining_after_020 - k_087
        and n_remaining_after_057 == n_remaining_after_087 - k_057
        and n_remaining == n_remaining_after_057 - k_011
    )


def i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem(
    inside_sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> bool:
    """True iff remaining-after-011 has N=2 and a unique most frequent next stem with K ≥ 2."""
    remaining = leftover_n4_remaining_remaining_after_011(
        inside_sites,
        next_stems,
        locked,
    )
    remaining_stems = leftover_n4_remaining_remaining_after_011_next_stems(
        inside_sites,
        next_stems,
        locked,
    )
    if len(remaining) != STANDING_N_REMAINING_AFTER_011:
        return False
    if remaining != leftover_n4_remaining_remaining_after_057_without_forward_011(
        inside_sites,
        next_stems,
    ):
        return False
    gram, count, unique = select_remaining_after_011_g(remaining_stems)
    return bool(unique and gram is not None and count >= 2)


def matching_leftover_n4_remaining_remaining_after_011_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover n=4 remaining remaining-after-011 next-4-gram rows."""
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


def remaining_after_011_overlap_sites(
    remaining: tuple[tuple[str, str, int], ...],
    extra_i: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """Site-level overlap of remaining-after-011 with a leftover-extra extra-I set."""
    extra_set = set(extra_i)
    return tuple(site for site in remaining if site in extra_set)


class TestILeftoverN4Remaining090076RemainingAfter011NextStemHelpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining remaining-after-011 next stems. No CV, no LLM."""

    def test_remaining_after_011_requires_next_none_of_020_087_057_011(self):
        """Remaining-after-011 excludes next 020, 087, 057, and 011; line-final is remaining, no-next."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "607"))
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("020", "087", "057", "011"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_607 = ["090", "076", "607", "755"]
        self.assertEqual(site_next_stem(has_607, 0, GRAM2), "607")
        self.assertEqual(site_forward_3gram(has_607, 0, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_607, 0, GRAM2),
            ("090", "076", "607", "755"),
        )
        has_021 = ["090", "076", "021", "020"]
        self.assertEqual(site_next_stem(has_021, 0, GRAM2), "021")
        self.assertNotEqual(site_next_stem(has_021, 0, GRAM2), "607")
        has_011 = ["090", "076", "011", "027"]
        self.assertEqual(site_next_stem(has_011, 0, GRAM2), "011")
        self.assertNotEqual(site_next_stem(has_011, 0, GRAM2), "607")
        has_057 = ["090", "076", "057", "600"]
        self.assertEqual(site_next_stem(has_057, 0, GRAM2), "057")
        self.assertNotEqual(site_next_stem(has_057, 0, GRAM2), "607")
        has_087 = ["090", "076", "087", "291"]
        self.assertEqual(site_next_stem(has_087, 0, GRAM2), "087")
        self.assertNotEqual(site_next_stem(has_087, 0, GRAM2), "607")
        has_020 = ["090", "076", "020", "010"]
        self.assertEqual(site_next_stem(has_020, 0, GRAM2), "020")
        self.assertNotEqual(site_next_stem(has_020, 0, GRAM2), "607")
        end_of_line = ["999", "021", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
            (SIDE_IA, "Ia1", 5),
            (SIDE_IA, "Ia1", 6),
        )
        planted_stems = ("607", "020", None, "021", "087", "057", "011")
        rem = leftover_n4_remaining_remaining_after_011(planted_sites, planted_stems)
        self.assertEqual(rem, (planted_sites[0], planted_sites[2], planted_sites[3]))
        self.assertEqual(
            leftover_n4_remaining_remaining_after_011_next_stems(
                planted_sites, planted_stems
            ),
            ("607", "021"),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_011_with_next(
                planted_sites, planted_stems
            ),
            (planted_sites[0], planted_sites[3]),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_011_without_next(
                planted_sites, planted_stems
            ),
            (planted_sites[2],),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_011_with_g(
                planted_sites, planted_stems
            ),
            (planted_sites[0],),
        )
        self.assertNotIn(planted_sites[1], rem)
        self.assertNotIn(planted_sites[4], rem)
        self.assertNotIn(planted_sites[5], rem)
        self.assertNotIn(planted_sites[6], rem)
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE296_FREQUENCY_MINUS_011_IS_NESTED_INVENTORY)
        self.assertTrue(STANDING_CYCLE297_EXACT_K_011_IS_NESTED_INVENTORY)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_can_fail(self):
        """Boolean is True only when remaining=2 and some G has unique K≥2."""
        provider = MockProvider()
        inside = STANDING_INSIDE_SITES
        stems = leftover_n4_remaining_next_stems(load_i_sides(), inside, GRAM2)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem(
                inside,
                stems,
            )
        )
        rem = leftover_n4_remaining_remaining_after_011(inside, stems)
        rem_stems = leftover_n4_remaining_remaining_after_011_next_stems(inside, stems)
        self.assertEqual(len(rem), STANDING_N_REMAINING_AFTER_011)
        self.assertEqual(len(rem), 2)
        self.assertEqual(rem, STANDING_REMAINING_SITES)
        self.assertEqual(rem_stems, STANDING_REMAINING_NEXT_STEMS)
        g, k, unique = select_remaining_after_011_g(rem_stems)
        self.assertEqual(g, "607")
        self.assertEqual(k, 1)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = ("020",) * len(inside)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem(
                inside,
                empty_stems,
            )
        )
        hold_stems = list(stems)
        # Remaining-after-011 already has hapax 607/021. Promote 021 to 607
        # so unique-max 607×2 (cycle-296 hold shape) while N stays 2.
        promote = {(SIDE_IA, "Ia13", 17): "607"}
        for i, site in enumerate(inside):
            if site in promote:
                hold_stems[i] = promote[site]
        held = tuple(hold_stems)
        held_g, held_k, held_unique = select_remaining_after_011_g(
            leftover_n4_remaining_remaining_after_011_next_stems(inside, held)
        )
        self.assertEqual(held_g, "607")
        self.assertEqual(held_k, 2)
        self.assertTrue(held_unique)
        self.assertEqual(
            len(leftover_n4_remaining_remaining_after_011(inside, held)),
            2,
        )
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem(
                inside,
                held,
            )
        )
        drifted_stems = list(stems)
        # Promote a remaining-after-057 011 site to 607 so N_remaining_after_011
        # becomes 3; unique-max 607×2 still fails the N==2 gate.
        drifted_stems_map = {(SIDE_IA, "Ia2", 107): "607"}
        for i, site in enumerate(inside):
            if site in drifted_stems_map:
                drifted_stems[i] = drifted_stems_map[site]
        drifted = tuple(drifted_stems)
        drifted_g, drifted_k, drifted_unique = select_remaining_after_011_g(
            leftover_n4_remaining_remaining_after_011_next_stems(inside, drifted)
        )
        self.assertEqual(drifted_g, "607")
        self.assertEqual(drifted_k, 2)
        self.assertTrue(drifted_unique)
        self.assertEqual(
            len(leftover_n4_remaining_remaining_after_011(inside, drifted)),
            3,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem(
                inside,
                drifted,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem",
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_UNIQUE_NEXT_STEM
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING_AFTER_011)
        self.assertEqual(1 + 1, 2)
        self.assertEqual(
            STANDING_K_011 + STANDING_N_REMAINING_AFTER_011,
            STANDING_N_REMAINING_AFTER_057,
        )
        self.assertEqual(2 + 2, 4)
        self.assertEqual(
            STANDING_K_057 + STANDING_N_REMAINING_AFTER_057,
            STANDING_N_REMAINING_AFTER_087,
        )
        self.assertEqual(2 + 4, 6)
        self.assertEqual(
            STANDING_K_087 + STANDING_N_REMAINING_AFTER_087,
            STANDING_N_REMAINING_AFTER_020,
        )
        self.assertEqual(3 + 6, 9)
        self.assertEqual(STANDING_K_020 + STANDING_N_REMAINING_AFTER_020, STANDING_N_INSIDE)
        self.assertEqual(4 + 9, 13)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_PEEL_607)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_011_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_011_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining-after-011 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"607": 1, "021": 1})
        ranked = rank_remaining_after_011_next_stems(counts)
        self.assertEqual(ranked[0], ("607", 1))
        self.assertEqual(ranked[1], ("021", 1))
        self.assertEqual(select_remaining_after_011_g(("607", "021"))[0], "607")
        self.assertFalse(select_remaining_after_011_g(("607", "021"))[2])
        self.assertEqual(select_remaining_after_011_g(("607", "607", "021"))[0], "607")
        self.assertTrue(select_remaining_after_011_g(("607", "607", "021"))[2])
        self.assertEqual(select_remaining_after_011_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE294)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE296)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE294)
        self.assertFalse(STANDING_SAME_AS_CYCLE296)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertFalse(CYCLE270_UNIQUE)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertFalse(CYCLE294_UNIQUE)
        self.assertTrue(CYCLE296_UNIQUE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter011NextStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-011 next-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.inside_sites = STANDING_INSIDE_SITES
        self.next_stems = leftover_n4_remaining_next_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.forwards = leftover_n4_remaining_forward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.with_next_inside = leftover_n4_remaining_sites_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next_inside = leftover_n4_remaining_sites_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.share_020 = leftover_n4_remaining_with_forward_020(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_after_020 = leftover_n4_remaining_remaining_after_020(
            self.inside_sites,
            self.next_stems,
        )
        self.share_087 = leftover_n4_remaining_remaining_after_020_with_forward_087(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_after_087 = leftover_n4_remaining_remaining_after_087(
            self.inside_sites,
            self.next_stems,
        )
        self.share_057 = leftover_n4_remaining_remaining_after_087_with_forward_057(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_after_057 = leftover_n4_remaining_remaining_after_057(
            self.inside_sites,
            self.next_stems,
        )
        self.share_011 = leftover_n4_remaining_remaining_after_057_with_forward_011(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining = leftover_n4_remaining_remaining_after_011(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_011_next_stems(
            self.inside_sites,
            self.next_stems,
        )
        self.with_next = leftover_n4_remaining_remaining_after_011_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next = leftover_n4_remaining_remaining_after_011_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.matching = leftover_n4_remaining_remaining_after_011_with_g(
            self.inside_sites,
            self.next_stems,
        )
        self.without = leftover_n4_remaining_remaining_after_011_without_g(
            self.inside_sites,
            self.next_stems,
        )
        self.frequency = remaining_after_011_next_stem_frequency_table(
            self.inside_sites,
            self.next_stems,
            self.forwards,
        )
        self.matching_next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_next_inside = len(self.with_next_inside)
        self.n_no_next_inside = len(self.no_next_inside)
        self.k_020 = len(self.share_020)
        self.n_remaining_after_020 = len(self.remaining_after_020)
        self.k_087 = len(self.share_087)
        self.n_remaining_after_087 = len(self.remaining_after_087)
        self.k_057 = len(self.share_057)
        self.n_remaining_after_057 = len(self.remaining_after_057)
        self.k_011 = len(self.share_011)
        self.n_remaining = len(self.remaining)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.n_distinct = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_after_011_g(self.remaining_stems)
        self.n_without = len(self.without)
        self.overlap_258 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_258_607 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_BY_X["607"],
        )
        self.overlap_259_607 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_BY_X["607"],
        )
        self.overlap_258_057 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_BY_X["057"],
        )
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem(
                self.inside_sites,
                self.next_stems,
            )
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_4_9_3_6_2_4_2_2_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/4/9/3/6/2/4/2/2 stay prior locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "607"))
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(CYCLE248_GRAM3, ("090", "076", "011"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("020", "087", "057", "011"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(len(STANDING_INSIDE_SITES), STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE224_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE288_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE289_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_297 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_forward_011"]
        self.assertEqual(prior_297["cycle"], 297)
        self.assertEqual(prior_297["K_011"], 2)
        self.assertEqual(prior_297["N_remaining_after_011"], 2)
        self.assertEqual(prior_297["N_remaining_after_057"], 4)
        self.assertTrue(
            prior_297["i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011"]
        )
        self.assertTrue(CYCLE297_CLAIM)
        self.assertEqual(CYCLE297_K_011, 2)
        self.assertEqual(CYCLE297_N_REMAINING_AFTER_011, 2)
        self.assertEqual(CYCLE297_N_REMAINING_AFTER_057, 4)
        prior_296 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"]
        self.assertEqual(prior_296["cycle"], 296)
        self.assertEqual(prior_296["G"], "011")
        self.assertEqual(prior_296["K"], 2)
        self.assertEqual(prior_296["N_remaining_after_057"], 4)
        self.assertEqual(prior_296["N_distinct"], 3)
        self.assertTrue(prior_296["G_uniquely_most_frequent"])
        self.assertTrue(CYCLE296_CLAIM)
        self.assertEqual(CYCLE296_G, "011")
        self.assertEqual(CYCLE296_K, 2)
        self.assertEqual(CYCLE296_N_REMAINING, 4)
        self.assertEqual(CYCLE296_N_DISTINCT, 3)
        self.assertTrue(CYCLE296_UNIQUE)
        prior_295 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_forward_057"]
        self.assertEqual(prior_295["cycle"], 295)
        self.assertEqual(prior_295["K_057"], 2)
        self.assertEqual(prior_295["N_remaining_after_057"], 4)
        self.assertTrue(
            prior_295["i_leftover_n4_remaining_090_076_remaining_after_087_exactly_2_share_forward_057"]
        )
        self.assertTrue(CYCLE295_CLAIM)
        prior_294 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]
        self.assertEqual(prior_294["cycle"], 294)
        self.assertEqual(prior_294["G"], "057")
        self.assertEqual(prior_294["K"], 2)
        self.assertFalse(prior_294["G_uniquely_most_frequent"])
        self.assertFalse(CYCLE294_CLAIM)
        self.assertFalse(CYCLE294_UNIQUE)
        prior_293 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]
        self.assertEqual(prior_293["cycle"], 293)
        self.assertEqual(prior_293["K_087"], 3)
        self.assertTrue(CYCLE293_CLAIM)
        prior_292 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]
        self.assertEqual(prior_292["cycle"], 292)
        self.assertEqual(prior_292["G"], "087")
        self.assertEqual(prior_292["K"], 3)
        self.assertTrue(prior_292["G_uniquely_most_frequent"])
        self.assertTrue(CYCLE292_CLAIM)
        prior_289 = self.survey["i_leftover_n4_remaining_090_076_forward_020"]
        self.assertEqual(prior_289["cycle"], 289)
        self.assertEqual(prior_289["K"], 4)
        self.assertTrue(CYCLE289_CLAIM)
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertFalse(CYCLE288_SHARE_ONE)
        prior_250 = self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]
        self.assertEqual(prior_250["cycle"], 250)
        self.assertEqual(prior_250["K"], 2)
        self.assertTrue(prior_250["i_leftover_extra_090_076_remaining_after_011_exactly_2_share_005"])
        self.assertTrue(CYCLE250_CLAIM)
        self.assertEqual(CYCLE250_K, 2)
        prior_248 = self.survey["i_3gram_090_076_011_i_only"]
        self.assertEqual(prior_248["cycle"], 248)
        self.assertEqual(prior_248["N_I"], 4)
        self.assertEqual(prior_248["N_off_I"], 0)
        self.assertEqual(prior_248["N_extra"], 2)
        self.assertTrue(CYCLE248_CLAIM)
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(CYCLE224_ALL_INSIDE)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        unused_224_n = CYCLE224_N_I
        self.assertEqual(unused_224_n, 69)
        unused_288_n = CYCLE288_N_WITH_NEXT
        self.assertEqual(unused_288_n, 13)
        unused_288_no = CYCLE288_N_NO_NEXT
        self.assertEqual(unused_288_no, 0)
        unused_288_freq = CYCLE288_FREQUENCY
        self.assertEqual(unused_288_freq[0][0], "020")
        unused_292_freq = CYCLE292_REMAINING_FREQUENCY
        self.assertEqual(unused_292_freq[0][0], "087")
        unused_296_freq = CYCLE296_REMAINING_FREQUENCY
        self.assertEqual(unused_296_freq[0][0], "011")
        unused_296_hapax = CYCLE296_N_HAPAX
        self.assertEqual(unused_296_hapax, 2)
        unused_294_tied = CYCLE294_TIED_STEMS
        self.assertEqual(unused_294_tied, ("057", "011"))
        unused_294_hapax = CYCLE294_N_HAPAX
        self.assertEqual(unused_294_hapax, 2)
        unused_294_tied_n = CYCLE294_N_TIED
        self.assertEqual(unused_294_tied_n, 2)
        unused_258_n = CYCLE258_N_I_ONLY
        self.assertEqual(unused_258_n, 19)
        unused_258_extra = CYCLE258_N_EXTRA
        self.assertEqual(unused_258_extra, 3)
        unused_259 = CYCLE259_EXTRA_I_BY_X["607"]
        self.assertEqual(unused_259, ((SIDE_IA, "Ia8", 106),))
        unused_020_with = leftover_n4_remaining_remaining_after_020_with_next
        unused_020_without = leftover_n4_remaining_remaining_after_020_without_next
        unused_020_stems = leftover_n4_remaining_remaining_after_020_next_stems
        unused_087_with = leftover_n4_remaining_remaining_after_087_with_next
        unused_087_without = leftover_n4_remaining_remaining_after_087_without_next
        unused_087_stems = leftover_n4_remaining_remaining_after_087_next_stems
        unused_057_with = leftover_n4_remaining_remaining_after_057_with_next
        unused_057_without = leftover_n4_remaining_remaining_after_057_without_next
        unused_without_020 = leftover_n4_remaining_without_forward_020
        unused_without_087 = leftover_n4_remaining_remaining_after_020_without_forward_087
        unused_289_rem = CYCLE289_REMAINING_AFTER_020_SITES
        unused_292_sites = CYCLE292_REMAINING_SITES
        unused_293_rem = CYCLE293_REMAINING_AFTER_087_SITES
        unused_293_n020 = CYCLE293_N_REMAINING_AFTER_020
        unused_292_match = CYCLE292_MATCHING_SITES
        unused_294_sites = CYCLE294_REMAINING_SITES
        unused_296_eq = CYCLE296_EQUALS_248
        unused_297_eq = CYCLE297_EQUALS_248
        unused_293_eq = CYCLE293_EQUALS_245
        unused_295_eq = CYCLE295_EQUALS_258
        unused_258_fn = matching_equals_cycle258_extra_i_057
        unused_248_fn = matching_equals_cycle248_extra_i
        self.assertTrue(callable(unused_020_with))
        self.assertTrue(callable(unused_020_without))
        self.assertTrue(callable(unused_020_stems))
        self.assertTrue(callable(unused_087_with))
        self.assertTrue(callable(unused_087_without))
        self.assertTrue(callable(unused_087_stems))
        self.assertTrue(callable(unused_057_with))
        self.assertTrue(callable(unused_057_without))
        self.assertTrue(callable(unused_without_020))
        self.assertTrue(callable(unused_without_087))
        self.assertEqual(len(unused_289_rem), 9)
        self.assertEqual(len(unused_292_sites), 9)
        self.assertEqual(len(unused_293_rem), 6)
        self.assertEqual(unused_293_n020, 9)
        self.assertEqual(len(unused_292_match), 3)
        self.assertEqual(len(unused_294_sites), 6)
        self.assertTrue(unused_296_eq)
        self.assertTrue(unused_297_eq)
        self.assertTrue(unused_293_eq)
        self.assertTrue(unused_295_eq)
        self.assertTrue(callable(unused_258_fn))
        self.assertTrue(callable(unused_248_fn))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_011_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_PEEL_607)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_268_297_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_remaining_g_607_k_1_hapax_and_hypothesis_loses(self):
        """N_remaining=2, N_with_next=2, N_distinct=2, G=607 K=1 hapax. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next_inside, STANDING_N_WITH_NEXT_INSIDE)
        self.assertEqual(STANDING_N_WITH_NEXT_INSIDE, CYCLE288_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT_INSIDE, 13)
        self.assertEqual(self.n_no_next_inside, STANDING_N_NO_NEXT_INSIDE)
        self.assertEqual(STANDING_N_NO_NEXT_INSIDE, CYCLE288_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT_INSIDE, 0)
        self.assertEqual(self.k_020, STANDING_K_020)
        self.assertEqual(STANDING_K_020, CYCLE289_K)
        self.assertEqual(STANDING_K_020, 4)
        self.assertEqual(self.share_020, CYCLE289_MATCHING_SITES)
        self.assertEqual(self.n_remaining_after_020, STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(self.k_087, STANDING_K_087)
        self.assertEqual(STANDING_K_087, CYCLE293_K_087)
        self.assertEqual(STANDING_K_087, 3)
        self.assertEqual(self.share_087, CYCLE293_MATCHING_SITES)
        self.assertEqual(self.share_087, CYCLE292_MATCHING_SITES)
        self.assertEqual(self.k_057, STANDING_K_057)
        self.assertEqual(STANDING_K_057, CYCLE295_K_057)
        self.assertEqual(STANDING_K_057, 2)
        self.assertEqual(self.share_057, CYCLE295_MATCHING_SITES)
        self.assertEqual(self.share_057, CYCLE294_MATCHING_SITES)
        self.assertEqual(self.share_057, CYCLE258_EXTRA_I_057)
        self.assertTrue(matching_equals_cycle258_extra_i_057(self.share_057))
        self.assertEqual(self.k_011, STANDING_K_011)
        self.assertEqual(STANDING_K_011, CYCLE297_K_011)
        self.assertEqual(STANDING_K_011, 2)
        self.assertEqual(self.share_011, CYCLE297_MATCHING_SITES)
        self.assertEqual(self.share_011, CYCLE296_MATCHING_SITES)
        self.assertEqual(self.share_011, CYCLE248_EXTRA_I_SITES)
        self.assertTrue(matching_equals_cycle248_extra_i(self.share_011))
        self.assertTrue(STANDING_CYCLE248_EXTRA_I_EQUALS_REMAINING_AFTER_057_011)
        self.assertTrue(
            leftover_n4_remaining_remaining_after_020_nested_counts_hold(
                self.n_inside,
                self.n_with_next_inside,
                self.k_020,
                self.n_remaining_after_020,
            )
        )
        self.assertTrue(
            leftover_n4_remaining_remaining_after_087_nested_counts_hold(
                self.n_inside,
                self.k_020,
                self.n_remaining_after_020,
                self.k_087,
                self.n_remaining_after_087,
            )
        )
        self.assertTrue(
            leftover_n4_remaining_remaining_after_057_nested_counts_hold(
                self.n_inside,
                self.k_020,
                self.n_remaining_after_020,
                self.k_087,
                self.n_remaining_after_087,
                self.k_057,
                self.n_remaining_after_057,
            )
        )
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_nested_counts_hold(
                self.n_inside,
                self.k_020,
                self.n_remaining_after_020,
                self.k_087,
                self.n_remaining_after_087,
                self.k_057,
                self.n_remaining_after_057,
                self.k_011,
                self.n_remaining,
            )
        )
        self.assertEqual(self.n_remaining_after_087, STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(self.n_remaining_after_057, STANDING_N_REMAINING_AFTER_057)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, 4)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, CYCLE296_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, CYCLE295_N_REMAINING_AFTER_057)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_011)
        self.assertEqual(STANDING_N_REMAINING_AFTER_011, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_011, CYCLE297_N_REMAINING_AFTER_011)
        self.assertEqual(self.n_remaining, self.n_remaining_after_057 - self.k_011)
        self.assertEqual(4 - 2, 2)
        self.assertEqual(
            self.n_remaining,
            self.n_inside - self.k_020 - self.k_087 - self.k_057 - self.k_011,
        )
        self.assertEqual(13 - 4 - 3 - 2 - 2, 2)
        if self.n_remaining != 2:
            self.fail("measured N_remaining_after_011 drifted from 2")
        if self.n_remaining != self.n_remaining_after_057 - self.k_011:
            self.fail(
                "leftover n=4 remaining remaining-after-011 filter disagrees with nested 4−2"
            )
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_NEXT_STEMS)
        self.assertEqual(len(self.remaining), len(self.remaining_stems))
        self.assertEqual(
            self.remaining,
            leftover_n4_remaining_remaining_after_057_without_forward_011(
                self.inside_sites,
                self.next_stems,
            ),
        )
        self.assertEqual(
            self.remaining_after_057,
            leftover_n4_remaining_remaining_after_087_without_forward_057(
                self.inside_sites,
                self.next_stems,
            ),
        )
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 2)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 0)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ())
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_remaining)
        self.assertEqual(2 + 0, 2)
        for site in self.share_020:
            self.assertNotIn(site, self.remaining)
        for site in self.share_087:
            self.assertNotIn(site, self.remaining)
        for site in self.share_057:
            self.assertNotIn(site, self.remaining)
        for site in self.share_011:
            self.assertNotIn(site, self.remaining)
            self.assertIn(site, self.remaining_after_057)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT)
        self.assertEqual(STANDING_N_DISTINCT, 2)
        self.assertEqual(self.frequency, STANDING_REMAINING_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "607")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 1)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "607")
        self.assertEqual(self.frequency[0][1], 1)
        self.assertEqual(self.frequency[1][0], "021")
        self.assertEqual(self.frequency[1][1], 1)
        self.assertEqual(self.frequency[0][1], self.frequency[1][1])
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 2)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX)
        self.assertEqual(STANDING_N_HAPAX, 2)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 1)
        self.assertEqual(self.without, STANDING_WITHOUT_G_SITES)
        self.assertEqual(self.k + self.n_without, self.n_remaining)
        self.assertEqual(1 + 1, 2)
        cycle296_remaining_after_011_inventory = tuple(
            (stem, count)
            for stem, count, _sites, _grams in CYCLE296_REMAINING_FREQUENCY
            if stem != "011"
        )
        self.assertEqual(
            cycle296_remaining_after_011_inventory,
            STANDING_CYCLE296_REMAINING_AFTER_011_INVENTORY,
        )
        self.assertEqual(
            set(cycle296_remaining_after_011_inventory),
            {(stem, count) for stem, count, _sites, _grams in self.frequency},
        )
        self.assertTrue(STANDING_CYCLE296_FREQUENCY_MINUS_011_IS_NESTED_INVENTORY)
        self.assertTrue(STANDING_CYCLE297_EXACT_K_011_IS_NESTED_INVENTORY)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem(
                self.inside_sites,
                self.next_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_UNIQUE_NEXT_STEM,
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_UNIQUE_NEXT_STEM
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE248)
        self.assertFalse(STANDING_SAME_AS_CYCLE250)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE258)
        self.assertFalse(STANDING_SAME_AS_CYCLE259)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertFalse(STANDING_SAME_AS_CYCLE288)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE294)
        self.assertFalse(STANDING_SAME_AS_CYCLE295)
        self.assertFalse(STANDING_SAME_AS_CYCLE296)
        self.assertFalse(STANDING_SAME_AS_CYCLE297)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE294)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE296)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_011_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_PEEL_607)
        self.assertTrue(STANDING_CYCLE296_FREQUENCY_MINUS_011_IS_NESTED_INVENTORY)
        self.assertTrue(STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertTrue(CYCLE289_CLAIM)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertTrue(CYCLE293_CLAIM)
        self.assertFalse(CYCLE294_CLAIM)
        self.assertTrue(CYCLE295_CLAIM)
        self.assertTrue(CYCLE296_CLAIM)
        self.assertTrue(CYCLE297_CLAIM)
        self.assertTrue(CYCLE248_CLAIM)
        self.assertTrue(CYCLE250_CLAIM)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertTrue(CYCLE259_CLAIM)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertFalse(CYCLE256_CLAIM)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE256_N_DISTINCT, 19)
        self.assertEqual(CYCLE256_G, "755")
        self.assertEqual(CYCLE256_K, 1)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_TIED_AT_K, 5)
        self.assertFalse(CYCLE270_UNIQUE)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_K, 2)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertEqual(CYCLE292_G, "087")
        self.assertEqual(CYCLE292_K, 3)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertEqual(CYCLE294_G, "057")
        self.assertEqual(CYCLE294_K, 2)
        self.assertFalse(CYCLE294_UNIQUE)
        self.assertEqual(CYCLE296_G, "011")
        self.assertEqual(CYCLE296_K, 2)
        self.assertTrue(CYCLE296_UNIQUE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_n4_remaining_remaining_after_011_site_is_607(self):
        """One leftover n=4 remaining remaining-after-011 site is 090 076 607 (hapax inventory)."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia8", 106), ("090", "076", "607", "755")),
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
            self.assertEqual(stems[index + STANDING_N2], "607")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "607")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE289_MATCHING_SITES)
            self.assertNotIn(site, CYCLE292_MATCHING_SITES)
            self.assertNotIn(site, CYCLE294_MATCHING_SITES)
            self.assertNotIn(site, CYCLE295_MATCHING_SITES)
            self.assertNotIn(site, CYCLE296_MATCHING_SITES)
            self.assertNotIn(site, CYCLE297_MATCHING_SITES)
            self.assertNotIn(site, CYCLE248_EXTRA_I_SITES)
            self.assertNotIn(site, CYCLE250_MATCHING_SITES)
            self.assertIn(site, CYCLE259_EXTRA_I_SITES)
            self.assertIn(site, CYCLE259_EXTRA_I_BY_X["607"])
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "607")
            self.assertNotEqual(nxt, "011")
            self.assertNotEqual(nxt, "057")
            self.assertNotEqual(nxt, "087")
            self.assertNotEqual(nxt, "020")
            self.assertIn(site, STANDING_REMAINING_SITES)
            self.assertEqual(site, (SIDE_IA, "Ia13", 17))
            self.assertEqual(site_next_4gram(stems, index, GRAM2), ("090", "076", "021", "020"))
        for site in self.share_020:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in self.share_087:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in self.share_057:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in self.share_011:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE248_EXTRA_I_SITES)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
        for site in CYCLE248_LEFTOVER_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        for site in CYCLE250_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_011_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_PEEL_607)
        leftover_extra_011 = tuple(
            site for site in CYCLE248_I_SITES if site not in CYCLE248_EXTRA_I_SITES
        )
        for site in leftover_extra_011:
            self.assertNotIn(site, self.remaining)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_overlap_cycle258_259_extra_i_recorded_does_not_lose(self):
        """Remaining-after-011 overlaps cycle 258/259 extra I at Ia8[106] only; record, do not fail."""
        self.assertEqual(self.overlap_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258_607, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259_607, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258_057, ())
        self.assertTrue(STANDING_OVERLAP_CYCLE258_EXTRA_I_607)
        self.assertTrue(STANDING_OVERLAP_CYCLE259_EXTRA_I_607)
        self.assertFalse(STANDING_OVERLAP_CYCLE258_EXTRA_I_057)
        self.assertFalse(STANDING_IA13_OVERLAPS_CYCLE258_OR_259)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_BY_X["607"])
        self.assertNotIn((SIDE_IA, "Ia13", 17), CYCLE259_EXTRA_I_SITES)
        self.assertNotIn((SIDE_IA, "Ia13", 17), CYCLE259_EXTRA_I_BY_X["607"])
        self.assertNotIn((SIDE_IA, "Ia13", 17), CYCLE259_EXTRA_I_BY_X["057"])
        self.assertNotIn((SIDE_IA, "Ia8", 114), self.remaining)
        self.assertNotIn((SIDE_IA, "Ia9", 28), self.remaining)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertFalse(self.claim_holds)
        self.assertFalse(self.unique)
        self.assertEqual(self.k, 1)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        self.assertEqual(len(CYCLE259_EXTRA_I_SITES), 3)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertTrue(CYCLE259_CLAIM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_297_296_294_256_250_248_224_223_still_compute(self):
        """Cycle 297 K_011=2 N=2, 296 unique-max G=011 K=2, 294 unique-max false, 256 hapax lose, 250 leftover extra 005, 248 4/0 extra I=2, 224 13/56, 223 69/3 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_297 = TestMamariILeftoverN4Remaining090076RemainingAfter057Forward011Scoreboard()
        prior_297.setUp()
        prior_297.test_counts_2_of_4_and_hypothesis_k_2_holds()
        prior_297.test_survey_matches_computed_lock()
        self.assertEqual(prior_297.k_011, 2)
        self.assertEqual(prior_297.n_remaining_after_011, 2)
        self.assertEqual(prior_297.matching, CYCLE297_MATCHING_SITES)
        self.assertEqual(self.share_011, prior_297.matching)
        self.assertEqual(self.remaining, prior_297.without)
        self.assertTrue(prior_297.equals_cycle248)
        self.assertTrue(prior_297.claim_holds)
        self.assertTrue(CYCLE297_CLAIM)
        if (
            prior_297.k_011 != 2
            or prior_297.n_remaining_after_011 != 2
            or not prior_297.equals_cycle248
        ):
            self.fail(
                "nested cycle 297 leftover n=4 remaining remaining-after-057 exactly 2 share 011 / N_remaining=2 drifted"
            )
        prior_296 = TestMamariILeftoverN4Remaining090076RemainingAfter057NextStemScoreboard()
        prior_296.setUp()
        prior_296.test_counts_4_remaining_g_011_k_2_and_hypothesis_holds()
        prior_296.test_survey_matches_computed_lock()
        self.assertEqual(prior_296.n_remaining, 4)
        self.assertEqual(prior_296.n_distinct, 3)
        self.assertEqual(prior_296.g, "011")
        self.assertEqual(prior_296.k, 2)
        self.assertTrue(prior_296.unique)
        self.assertTrue(prior_296.claim_holds)
        self.assertTrue(CYCLE296_CLAIM)
        if (
            prior_296.n_remaining != 4
            or prior_296.g != "011"
            or prior_296.k != 2
            or not prior_296.unique
        ):
            self.fail(
                "nested cycle 296 leftover n=4 remaining remaining-after-057 unique-max G=011 K=2 drifted"
            )
        prior_294 = TestMamariILeftoverN4Remaining090076RemainingAfter087NextStemScoreboard()
        prior_294.setUp()
        prior_294.test_counts_6_remaining_g_057_k_2_tie_and_hypothesis_loses()
        prior_294.test_survey_matches_computed_lock()
        self.assertEqual(prior_294.n_remaining, 6)
        self.assertEqual(prior_294.n_distinct, 4)
        self.assertEqual(prior_294.g, "057")
        self.assertEqual(prior_294.k, 2)
        self.assertFalse(prior_294.unique)
        self.assertFalse(prior_294.claim_holds)
        self.assertFalse(CYCLE294_CLAIM)
        if (
            prior_294.n_remaining != 6
            or prior_294.g != "057"
            or prior_294.k != 2
            or prior_294.unique
        ):
            self.fail(
                "nested cycle 294 leftover n=4 remaining remaining-after-087 unique-max false G=057 K=2 drifted"
            )
        prior_256 = TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard()
        prior_256.setUp()
        prior_256.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE256_G, "755")
        self.assertEqual(CYCLE256_K, 1)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertFalse(CYCLE256_CLAIM)
        if CYCLE256_G != "755" or CYCLE256_K != 1 or CYCLE256_UNIQUE:
            self.fail("nested cycle 256 leftover extra remaining-after-000 hapax lose G=755 K=1 drifted")
        prior_250 = TestMamariILeftoverExtra090076RemainingAfter011Fwd005Scoreboard()
        prior_250.setUp()
        prior_250.test_counts_2_of_23_and_hypothesis_k_2_holds()
        prior_250.test_survey_matches_computed_lock()
        self.assertEqual(prior_250.k, 2)
        self.assertEqual(prior_250.matching, CYCLE250_MATCHING_SITES)
        self.assertTrue(prior_250.claim_holds)
        self.assertTrue(CYCLE250_CLAIM)
        for site in CYCLE250_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
        if prior_250.k != 2 or not prior_250.claim_holds:
            self.fail("nested cycle 250 leftover extra remaining-after-011 exactly 2 share 005 drifted")
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        self.assertTrue(CYCLE258_CLAIM)
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(len(CYCLE259_EXTRA_I_SITES), 3)
        self.assertTrue(CYCLE259_CLAIM)
        prior_248 = TestMamariI3gram090076011IOnlyScoreboard()
        prior_248.setUp()
        prior_248.test_3gram_is_zero_off_i_and_i_only()
        prior_248.test_survey_matches_computed_lock()
        self.assertEqual(prior_248.i_hits, CYCLE248_N_I)
        self.assertEqual(prior_248.i_hits, 4)
        self.assertEqual(prior_248.off_i_hits, CYCLE248_N_OFF_I)
        self.assertEqual(prior_248.off_i_hits, 0)
        self.assertEqual(len(prior_248.extra), CYCLE248_N_EXTRA)
        self.assertEqual(len(prior_248.extra), 2)
        self.assertEqual(prior_248.extra, CYCLE248_EXTRA_I_SITES)
        self.assertEqual(self.share_011, prior_248.extra)
        self.assertTrue(prior_248.claim_holds)
        self.assertTrue(CYCLE248_CLAIM)
        if prior_248.i_hits != 4 or prior_248.off_i_hits != 0 or len(prior_248.extra) != 2:
            self.fail("nested cycle 248 090 076 011 I-only 4/0 extra I=2 drifted")
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        if prior_224.n_inside != 13 or prior_224.n_leftover != 56:
            self.fail("nested cycle 224 13/56 drifted")
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
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-298 leftover n=4 remaining remaining-after-011 lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_next_stem"]
        self.assertEqual(lock["cycle"], 298)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(tuple(lock["forward_3gram"]), ("090", "076", "607"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(tuple(lock["locked_forward_stems"]), ("020", "087", "057", "011"))
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_with_next_inside"], STANDING_N_WITH_NEXT_INSIDE)
        self.assertEqual(lock["N_with_next_inside"], 13)
        self.assertEqual(lock["N_no_next_inside"], STANDING_N_NO_NEXT_INSIDE)
        self.assertEqual(lock["N_no_next_inside"], 0)
        self.assertEqual(lock["K_020"], STANDING_K_020)
        self.assertEqual(lock["K_020"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_020_sites"]),
            CYCLE289_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_020"], STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(lock["N_remaining_after_020"], 9)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_020_sites"]),
            CYCLE292_REMAINING_SITES,
        )
        self.assertEqual(lock["K_087"], STANDING_K_087)
        self.assertEqual(lock["K_087"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_087_sites"]),
            CYCLE293_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_087"], STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(lock["N_remaining_after_087"], 6)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_087_sites"]),
            CYCLE294_REMAINING_SITES,
        )
        self.assertEqual(lock["K_057"], STANDING_K_057)
        self.assertEqual(lock["K_057"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_057_sites"]),
            CYCLE295_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_057"], STANDING_N_REMAINING_AFTER_057)
        self.assertEqual(lock["N_remaining_after_057"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_057_sites"]),
            CYCLE296_REMAINING_SITES,
        )
        self.assertEqual(lock["K_011"], STANDING_K_011)
        self.assertEqual(lock["K_011"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_011_sites"]),
            CYCLE297_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_011"], STANDING_N_REMAINING_AFTER_011)
        self.assertEqual(lock["N_remaining_after_011"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_011_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_011_next_stems"]),
            STANDING_REMAINING_NEXT_STEMS,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 2)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 2)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 2)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "607")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 1)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 2)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_remaining_after_011_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_remaining_after_011_local_4grams"],
            matching_leftover_n4_remaining_remaining_after_011_local_4gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["without_G_sites"]),
            STANDING_WITHOUT_G_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_WITHOUT_G_NEXT_4GRAMS],
            lock["without_G_next_4grams"],
        )
        self.assertEqual(
            lock["remaining_after_011_next_stem_frequency"],
            remaining_after_011_next_stem_frequency_rows(),
        )
        self.assertEqual(
            [list(pair) for pair in STANDING_CYCLE296_REMAINING_AFTER_011_INVENTORY],
            lock["cycle296_remaining_after_011_inventory"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["overlap_cycle258_extra_i_sites"]),
            STANDING_OVERLAP_CYCLE258_EXTRA_I,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["overlap_cycle259_extra_i_sites"]),
            STANDING_OVERLAP_CYCLE259_EXTRA_I,
        )
        self.assertTrue(lock["overlap_cycle258_extra_i_607"])
        self.assertTrue(lock["overlap_cycle259_extra_i_607"])
        self.assertFalse(lock["overlap_cycle258_extra_i_057"])
        self.assertFalse(lock["ia13_overlaps_cycle258_or_259"])
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertEqual(lock["cycle297_K_011"], 2)
        self.assertEqual(lock["cycle297_N_remaining_after_011"], 2)
        self.assertTrue(lock["cycle297_extra_i_overlap"])
        self.assertEqual(lock["cycle296_G"], "011")
        self.assertEqual(lock["cycle296_K"], 2)
        self.assertEqual(lock["cycle296_N_remaining_after_057"], 4)
        self.assertEqual(lock["cycle296_N_distinct"], 3)
        self.assertTrue(lock["cycle296_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle295_K_057"], 2)
        self.assertEqual(lock["cycle295_N_remaining_after_057"], 4)
        self.assertTrue(lock["cycle295_extra_i_overlap"])
        self.assertEqual(lock["cycle294_G"], "057")
        self.assertEqual(lock["cycle294_K"], 2)
        self.assertEqual(lock["cycle294_N_remaining_after_087"], 6)
        self.assertEqual(lock["cycle294_N_distinct"], 4)
        self.assertFalse(lock["cycle294_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle294_N_tied_at_K"], 2)
        self.assertEqual(tuple(lock["cycle294_tied_stems"]), CYCLE294_TIED_STEMS)
        self.assertEqual(lock["cycle293_K_087"], 3)
        self.assertEqual(lock["cycle293_N_remaining_after_087"], 6)
        self.assertTrue(lock["cycle293_extra_i_overlap"])
        self.assertEqual(lock["cycle292_G"], "087")
        self.assertEqual(lock["cycle292_K"], 3)
        self.assertEqual(lock["cycle292_N_remaining_after_020"], 9)
        self.assertEqual(lock["cycle292_N_distinct"], 5)
        self.assertTrue(lock["cycle292_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle289_G"], "020")
        self.assertEqual(lock["cycle289_K"], 4)
        self.assertEqual(lock["cycle289_N_remaining_after_020"], 9)
        self.assertEqual(lock["cycle288_N_inside"], 13)
        self.assertEqual(lock["cycle288_N_with_next"], 13)
        self.assertEqual(lock["cycle288_N_distinct"], 6)
        self.assertEqual(lock["cycle288_G"], "020")
        self.assertEqual(lock["cycle288_K"], 4)
        self.assertTrue(lock["cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["cycle250_K"], 2)
        self.assertTrue(lock["cycle250_exactly_2_share_005"])
        self.assertEqual(lock["cycle248_N_I"], 4)
        self.assertEqual(lock["cycle248_N_off_I"], 0)
        self.assertEqual(lock["cycle248_N_extra"], 2)
        self.assertTrue(lock["cycle248_extra_i_equals_remaining_after_057_011"])
        self.assertEqual(lock["cycle258_N_extra"], 3)
        self.assertEqual(lock["cycle258_extra_I_of_607"], 1)
        self.assertEqual(lock["cycle258_extra_I_of_057"], 2)
        self.assertEqual(lock["cycle259_N_extra_i"], 3)
        self.assertEqual(lock["cycle224_N_inside"], 13)
        self.assertEqual(lock["cycle224_N_leftover"], 56)
        self.assertEqual(lock["cycle223_N_I"], 69)
        self.assertEqual(lock["cycle223_N_off_I"], 3)
        self.assertEqual(lock["cycle256_N_remaining11"], 19)
        self.assertEqual(lock["cycle256_G"], "755")
        self.assertEqual(lock["cycle256_K"], 1)
        self.assertFalse(lock["cycle256_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle270_G"], "090")
        self.assertEqual(lock["cycle270_K"], 2)
        self.assertEqual(lock["cycle270_N_tied_at_K"], 5)
        self.assertFalse(lock["cycle270_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["cycle234_G_uniquely_most_frequent"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle234"])
        self.assertFalse(lock["same_as_cycle248"])
        self.assertFalse(lock["same_as_cycle250"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertFalse(lock["same_as_cycle258"])
        self.assertFalse(lock["same_as_cycle259"])
        self.assertFalse(lock["same_as_cycle270"])
        self.assertFalse(lock["same_as_cycle288"])
        self.assertFalse(lock["same_as_cycle289"])
        self.assertFalse(lock["same_as_cycle292"])
        self.assertFalse(lock["same_as_cycle293"])
        self.assertFalse(lock["same_as_cycle294"])
        self.assertFalse(lock["same_as_cycle295"])
        self.assertFalse(lock["same_as_cycle296"])
        self.assertFalse(lock["same_as_cycle297"])
        self.assertTrue(lock["same_claim_shape_as_cycle234"])
        self.assertTrue(lock["same_claim_shape_as_cycle256"])
        self.assertTrue(lock["same_claim_shape_as_cycle270"])
        self.assertTrue(lock["same_claim_shape_as_cycle292"])
        self.assertTrue(lock["same_claim_shape_as_cycle294"])
        self.assertTrue(lock["same_claim_shape_as_cycle296"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_remaining_after_011_3gram_is_not_this_cycle"])
        self.assertTrue(lock["i_only_of_090_076_011_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_remaining_after_011_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["do_not_peel_607"])
        self.assertTrue(lock["cycle296_frequency_minus_011_is_nested_inventory"])
        self.assertTrue(lock["cycle297_exact_k_011_is_nested_inventory"])
        self.assertTrue(lock["cycle248_extra_i_equals_remaining_after_057_011"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["cycle167_268_297_not_overwritten"])
        self.assertTrue(lock["g_k_is_inventory_for_later_peel"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_057_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_087_forward_057_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_087_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_forward_087_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_020_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_011_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_011_fwd005_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_forward_011"]["cycle"],
            297,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_forward_011"][
                "i_leftover_n4_remaining_090_076_remaining_after_057_exactly_2_share_forward_011"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_forward_011"]["K_011"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_forward_011"][
                "N_remaining_after_011"
            ],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"]["cycle"],
            296,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"][
                "i_leftover_n4_remaining_090_076_remaining_after_057_unique_next_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_057_next_stem"]["G"],
            "011",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]["cycle"],
            294,
        )
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"][
                "i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]["cycle"], 250)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"][
                "i_leftover_extra_090_076_remaining_after_011_exactly_2_share_005"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["cycle"], 248)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_I"], 4)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_extra"], 2)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"], 13)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
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


class TestMamariILeftoverN4Remaining090076RemainingAfter011NextStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 298 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
