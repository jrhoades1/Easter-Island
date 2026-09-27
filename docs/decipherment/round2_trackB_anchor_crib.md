# Round 2, Track B — Round 1 anchors as a crib

Round 1 left five anchors: the Mamari night crescent, the full-moon pair, the calendar separator, the Gv6 handoff `200 X Y.076`, and the Staff bar that is followed by 076. This note takes those anchors out of their passages and asks two questions.

1. If the signs were phonetic, with a sound value taken from the Rapanui word for that anchor, do the strings they form outside the passages spell attested Rapanui words more often than a shuffle of the same values?
2. If the signs were logograms, do those outside contexts stay in the same semantic neighborhood?

No reading is adopted. A phonetic reading would have to spell the crib words, and beat both nulls, at the gate used in Track 2 (no more than 5% of nulls reach the observed score, and the score itself has to be above zero). None of the pre-specified maps clears that gate. Counts are locked by `tests/test_round2_trackb_anchor_crib.py`. The provider is `MockProvider` and it is never called.

## Sources

Sign meanings are the Round 1 citations, not new glosses.

| Anchor | Round 1 claim | Where it is anchored |
| --- | --- | --- |
| `040` | Guy 1990: the repeated night sign on Mamari Ca6–Ca9. High inside that passage, not for a lone crescent | 28 of the passage’s stems |
| `143` `152` | Guy 1990 and Horley 2011: 152 is full moon, 143 the night before it | One pair, Ca7 |
| `390 041 378 041 670 008 078 711` | Guy 1990: the group that separates nights. Ca6 uses `315` in the third slot, and one short form uses `375` | The calendar only |
| `200 X Y.076` | Butinov and Knorozov, via Davletshin 2012 and Guy: a genealogy handoff on Gv6. 200 as “man” / title and 076 as *ure* are hypotheses | Four phrases, three handoffs |
| `999` then 076 | Staff bars followed by a 076-group, 91/96 | Text I |

The words the crib is allowed to spell are listed in `data/rapanui/crib_headwords.txt`.

| Source | What was used | What was not used |
| --- | --- | --- |
| Thomson 1891, *Te Pito te Henua*, pp. 517–526 and the lexicon examples on pp. 546–547 | Public-domain chants (love song excluded) and the cited examples (`raa-po-tahi`, `poki`, `tangata`, `ure`, `tamahine`, `tamaroa`, `Ki ai Kiroto`). The open lexicon | The English glosses |
| Wikipedia `lang=rap` spans already vendored (CC BY-SA 4.0) | Modern-orthography words, including `pō`, `ko`, `poki`, `tau` | Running-text bigrams in Track 2 stay separate |
| Track 1 night table | The aligned Englert / Thomson / Métraux names already printed there. Thomson 1891 p. 546, Métraux 1940 p. 50, Englert 1948 pp. 311–312 | Englert’s dictionary. He died in 1969; Chilean copyright runs 70 years, and `data/rapanui/SOURCES.md` already excludes the book. The night names are the short list already in this repository |
| Metoro, vendored under `data/readings/metoro_jaussen/` | Single word-tokens: `marama`, `mahina`, `tama`, `tamaiti`, `poki`, `ure` | Any sign alignment. Track 4 found that Metoro’s words do not label Barthel signs |
| Churchill 1912, *Easter Island* (Carnegie Institution of Washington, Publication 174) | Nothing. The book is public domain. It is not vendored, and no headword was copied from it | The vocabulary |
| Fuentes 1960, *Diccionario y gramática de la lengua de la Isla de Pascua* | Nothing. This repository does not treat it as a public-domain source | The dictionary |

Bare *hina* does not occur in the vendored texts. *tahina* is a different word. *mahina* does occur, once, in Metoro’s Br3 line (`e puhi mahina te ahi`), and it is in the headword list. *tagata* in Metoro is the same word as Thomson’s *tangata* once *g* is read as *ng*; the strict form stored here is *tangata*.

A word enters the match list only when every consonant is an onset. The Track 2 syllabifier drops a stranded consonant, and that would turn Thomson’s *tantan* into ta-ta. Those forms are left out. The open list has 656 word-shapes. The crib targets, headwords of two or more syllables, are 48. The syllable inventory of the open list is 54.

## Where “outside the anchor” is

Stems are the same mechanical Barthel numbers as Track 1 and Track 3 (ligatures split, allograph letters stripped). The corpus is the vendored Kohaumotu pages for tablets A–V: 14,841 stems. W has no Barthel page.

A stem is inside an anchor, and is left out of the crib, when:

- it is `040`, `143`, or `152` inside the calendar (Ca6 from stem 24, all of Ca7 and Ca8, the first two stems of Ca9)
- it is `200` or `076` inside the four Gv6 handoff phrases (`200`, name, `Y.076`, group indexes 5–16)
- it is `076` in the group immediately after a pure `999` on the Staff (91 groups, 92 stems: Ia7 group 116 is `076.076t`, so one group contributes two stems)

The Gv6 quad that does not hand off, `200 769 381 002.076`, stays outside that cut. It is one of the outside `200`s and one of the outside `076`s.

## Occurrences outside the anchors

| Sign | In the corpus | Inside an anchor | Outside |
| --- | ---: | ---: | ---: |
| `040` | 152 | 28, all in the calendar | 124 |
| `143` | 1 | 1 | 0 |
| `152` | 1 | 1 | 0 |
| `200` | 311 | 4, the Gv6 openers | 307 |
| `076` | 682 | 4 on Gv6 and 92 in the Staff bracket | 586 |

`143` and `152` do not occur outside that one Ca7 pair. Anything that needs those two signs cannot be checked on another tablet.

Outside counts by tablet, A through V:

| Sign | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `040` | 17 | 9 | 17 | 1 | 19 | 2 | 5 | 10 | 4 | 0 | 1 | 0 | 0 | 1 | 3 | 8 | 9 | 12 | 5 | 0 | 1 | 0 |
| `200` | 14 | 31 | 11 | 10 | 14 | 2 | 13 | 54 | 22 | 0 | 2 | 0 | 2 | 5 | 3 | 55 | 33 | 16 | 14 | 3 | 0 | 3 |
| `076` | 3 | 8 | 0 | 0 | 5 | 0 | 41 | 8 | 472 | 0 | 0 | 0 | 0 | 1 | 0 | 6 | 7 | 0 | 3 | 32 | 0 | 0 |

C’s 17 crescents are the ones Track 1 already placed outside Ca6–Ca9. I’s 472 signs `076` are Staff signs that are not the group right after a bar. The other tablets together have 114.

Place on the line, outside the anchors. A one-sign line counts as the start.

| Sign | Start | Middle | End |
| --- | ---: | ---: | ---: |
| `040` | 3 | 121 | 0 |
| `200` | 8 | 297 | 2 |
| `076` | 0 | 579 | 7 |

### Repeated frames

Interior neighbors of outside `040`, frames that occur at least four times:

| Frame | Times | Where |
| --- | ---: | --- |
| `760 040 006` | 6 | Ca10:11, Ca10:22, Ca10:30, Ca11:6, Ca11:18, Ca12:1 |
| `003 040 003` | 6 | Cb10:31, Ab2:27, Ab3:8, Ab3:35, Ab5:19, Ab5:46 |
| `300 040 300` | 4 | Er1:32, Er2:12, Er2:29, Er4:3 |

The six `760 040 006` frames are on Mamari, on the lines after the calendar. They are not the delimiter. `006` and `760` are not in the sky set below.

Runs of `040` that sit entirely outside the calendar: 104 of length 1, 7 of length 2, 2 of length 3. The length-3 runs are Ra2:0 and Cb13:15. The length-2 runs are Bv2:5, Rb2:8, Er1:49, Er2:48, Er6:40, Hv10:29, Cb4:28. Track 1 already found that runs of five or more are calendar-only. That remains true.

Outside `200` is often the first stem of a group (154 groups) or a bare group (103). It is the last stem in 22 groups. The interior frame `200 200 200` occurs 6 times. The five `200 X Y.076` triples outside Gv6 are the five Track 3 already listed on the Staff, and they do not hand off:

| Line | Group index | Groups |
| --- | ---: | --- |
| Ia3 | 45 | `200` `690.090` `129.076` |
| Ia8 | 94 | `200f` `023` `440.076` |
| Ia11 | 117 | `200` `726` `571.076` |
| Ia12 | 68 | `200?` `380.061x` `002V:076` |
| Ia14 | 92 | `200` `700` `071.076` |

Most outside `076` stems are the last stem of a ligature. On the Staff, outside the bar-bracket, the sign immediately before `076` in the same group is `090` 50 times, `430` 25 times, `700` 18 times, then `071`, `604`, `002`, `001`, and `606` (14, 11, 10, 10, 10). That predecessor is the other half of the ligature, not a separate word.

### Separator sub-clusters

Every contiguous piece of length at least 2 was taken from the three published separators (`378`, `315`, and the short `375` form) and searched on A–V. A hit is outside when the whole piece is not inside the calendar.

| Piece | Inside the calendar | Outside |
| --- | ---: | ---: |
| `390 041 378 041 670 008 078 711` | 6 | 0 |
| `390 041 315 041 670 008 078 711` | 1 | 0 |
| `390 041 375 041` | 1 | 0 |
| Any piece of length 3 or more | the delimiter slices | 0 |
| `670 008` | (inside the seven full delimiters) | 1, Qv9:5, between `000` stems |
| `375 041` | the short Ca6 delimiter | 1, Hv10:26 |

Hv10:26 is `375 041 041 040 040`. The two crescents at Hv10:29 are one of the length-2 runs above. It is not the eight-sign separator.

A whole-line shuffle (500 draws, seed 2) rebuilds some length-3-or-longer piece outside the calendar in 9 draws. The observed count is 0, which is also the result in the other 491 draws. The two outside bigrams do not clear the gate: `670 008` is reached 313 times out of 500, and `375 041` 47 times out of 500.

## Phonetic crib

The rule is acrophony, applied mechanically. The value of a sign is the first (C)V syllable of one cited word. Four maps were fixed before the scores were read. `143` is *rakau* (ra) and `152` is *omotohi* (o) in all four, from the Track 1 alignment and from Guy’s placement of the pair.

| Map | `040` | `200` | `076` |
| --- | --- | --- | --- |
| H1 | *po* (po), night | *tangata* (ta) | *ure* (u) |
| H2 | *marama* (ma), moon | *ko* (ko) | *poki* (po) |
| H3 | *po* (po) | *ko* (ko) | *ure* (u) |
| H4 | *po* (po) | *ko* (ko) | *tama* (ta) |

*po* is the Wikipedia span `pō` and Thomson’s `raa-po-*` compounds. *marama* and *tama* are Metoro word-tokens. *ko* is a Wikipedia span. *poki*, *ure*, and *tangata* are in Thomson. Davletshin’s *ure* for 076, and his “man” for 200, stay hypotheses; H1 is what those hypotheses become if they are read as acrophony.

Thomson prints the copula as three tokens, `Ki ai Kiroto`. That is a phrase, not a first syllable, so it is not one of the four values. It is in the phrase test below as the word sequence *ki* + *ai* + *kiroto*, which none of these maps writes.

The test string is a contiguous run of 2, 3, or 4 stems, on one line, in which every stem is one of the five anchor signs, and none of those stems is inside an anchor. There are 81 such strings: `200 200` 25 times, `076 076` 13, `040 040` 11, `200 076` 8, `076 200` 7, `200 200 200` 6, and six rarer shapes. A hit is a string whose syllables are exactly one open-list word, or exactly one crib target. Overlapping strings are each counted. The same strings are used for every map.

Two nulls:

- **Permutation.** The five syllables of that map are reassigned to the five signs in every order (120). This asks whether this pairing is special among these candidate sounds.
- **Random syllables.** Five distinct syllables are drawn from the 54 attested syllable types, 500 times, seed 0. The same draws are scored against every map. This asks whether these sounds spell words more often than other sounds.

A whole-word rebus is scored separately. Each sign stands for its whole cited word, and a string of signs hits when that word sequence occurs in Thomson or in the Wikipedia spans. The null is the 120 permutations of the five words.

### Scores

| Map | Open-list hits | Permutation | Random syllables | Crib-target hits | Phrase hits |
| --- | --- | --- | ---: | ---: | ---: |
| H1 | 17 | 66 of 120 | 105 of 500 | 0 | 0 |
| H2 | 0 | 120 of 120 | 500 of 500 | 0 | 0 |
| H3 | 2 | 88 of 120 | 294 of 500 | 0 | 0 |
| H4 | 3 | 92 of 120 | 270 of 500 | 0 | 0 |

H1’s 17 hits are *tau* (ta-u) eight times, from `200 076`; *uta* (u-ta) seven times, from `076 200`; and *pou* (po-u) twice, from `040 076`. H3’s two hits are *pou*. H4’s three hits are *tapo* (ta-po), from `076 040`. Those four words are in the chants or the Wikipedia spans. None of them is a night name, *marama*, *poki*, *tama*, *ure*, or *tangata*.

Crib-target hits are 0 for every map, and for all 120 permutations of each map. The random draw is not empty in the same way: 15 of the 500 draws spell at least one crib target, and the highest of those draws spells 8. The motivated maps spell none. A score of zero cannot clear the gate, because every null reaches zero.

The same four maps, applied to strings that lie entirely inside the anchors, also spell 0 crib targets. The calendar’s crescents are repetitions of one sign. Under these values that is one syllable said again, not the list of night names. There is no outside string of the shape sign-A, sign-B, sign-A, which is the shape *marama* (ma-ra-ma) would need.

The phrase nulls are 120 of 120 at a score of zero. *tangata ure*, *ko poki*, *ko tama*, and the other recombinations of these glosses do not occur as word sequences in the vendored text.

## Logogram test

The alternative is that the anchor keeps its meaning and does not spell. The outside neighborhood is then the evidence.

**Sky and time signs**, fixed from the citations before the count: `041` (Guy’s delimiter crescent), `143`, `152`, and `008`. `008` is inside the delimiter; Fischer 1995 also glosses one `008` as the sun. Both citations are hypotheses. `040` itself is not counted as “another” sky sign.

Outside the calendar, `040` has 245 neighbor slots (a line edge has one). 7 of those neighbors are in the sky set: `041` four times, `008` three times, `143` and `152` never. A shuffle that moves stems inside each line, and that keeps the calendar block from mixing with the rest of Ca6 and Ca9 (500 draws, seed 1), reaches 7 or more in 66 draws. The sky-neighbor claim does not clear the gate.

**Repetition of `040`.** The 124 outside crescents form 11 adjacent pairs. The same shuffle reaches 11 in 0 draws. The clumping is real. The longest outside run is still 3, against 6 and 5 inside the calendar. Clumping is not a night name.

**Other signs that occur in the calendar.** The calendar passage uses 21 stem types. Outside `040` has 49 neighbor tokens that belong to that set and are not `040` itself. The same shuffle reaches 49 in 0 draws. This is a collocation with signs that happen to occur in the passage. The set includes `003` and `600`, which Track 1 did not read as sky signs. The sky subset of the same set failed its own test. The collocation is not adopted as a logogram.

**Separator.** Length 3 and up does not occur outside the calendar. The two stray bigrams do not clear the gate. The separator does not travel.

**Genealogy.** Outside Gv6 there are 5 strict `200 X Y.076` phrases and 0 handoffs. Shuffling the groups inside each of those lines (500 draws, seed 3) produces at least 5 phrases in 127 draws, and produces a handoff in 0 draws. Five phrases are an ordinary outcome. A handoff is not produced by the shuffle and is not present in the text. The handoff remains the Gv6 fact from Track 3.

**`076` as a final sign.** Groups outside the anchors that contain exactly one `076` and at least one other stem: on the Staff, 393 of 408 end in `076`; on the other tablets, 97 of 105 end in `076`. Putting that one `076` in a random slot of its own group (500 draws, seed 5) reaches those counts in 0 draws, on each cut. The suffix habit is corpus-wide, not only the group after a Staff bar. It does not choose among *ure*, *poki*, and *tama*. Those three values were the phonetic maps, and they spelled none of the crib words.

Group shapes for outside occurrences, one count per group: `076` is a suffix in 493 groups, bare in 67, initial in 15, medial in 8. `200` is initial in 154, bare in 103, final in 22, medial in 9.

## What survives, and what does not

| Claim | Result | Adopted as a reading? |
| --- | --- | --- |
| H1–H4 spell night names, *marama*, *mahina*, *poki*, *tama*, *ure*, or *tangata* outside the anchors | 0 hits. 15 of 500 random syllable draws do spell a crib word | No |
| The same maps spell attested words above the null | H1’s 17 hits (*tau*, *uta*, *pou*) sit inside both nulls. H2 is 0. H3 and H4 are *pou* and *tapo*, also inside the nulls | No |
| The signs stand for the whole cited words in sequence | 0 phrase hits, 120 of 120 permutations | No |
| `143` or `152` carries the full moon outside Ca7 | No tokens to test | No |
| The separator is reused outside Mamari | No piece of length 3 or more. Two bigrams, neither above the gate | No |
| Outside `040` sits next to the other cited sky signs | 7 of 245 slots, 66 of 500 shuffles | No |
| Outside `040` still clumps | 11 pairs, 0 of 500 shuffles. Longest run 3 | No. The clumping stands. It is not a gloss |
| Outside `040` prefers signs that also occur in the calendar passage | 49 neighbors, 0 of 500 | No. The set is not a semantic field |
| `200 X Y.076` with a father-to-child handoff is a rule outside Gv6 | 5 phrases, 0 handoffs, 127 of 500 shuffles reach 5 phrases | No |
| `076` ends its group outside the Staff bar | 393/408 on I, 97/105 elsewhere, both 0 of 500 | No gloss. The suffix habit stands |

Confidence is high that these four acrophonic maps, and the whole-word maps built from the same glosses, are not a decipherment of the outside text: the crib score is zero while a random syllable draw sometimes spells a crib word, and the open-list hits are ordinary words the null also reaches. Confidence is high that `143` and `152` have no second attestation in A–V, so their full-moon reading cannot be checked elsewhere. Confidence is high that the eight-sign separator does not recur. Confidence is high that `076` is a suffix beyond the Staff bar, and low that the suffix is *ure*, *poki*, or *tama*. Confidence is low for any reading of a lone `040`. The outside crescents clump more than a shuffle, in short runs, and their neighbors are not the cited sky signs.

Nothing in this track is a translation.
