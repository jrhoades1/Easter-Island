# Round 4, Track A — pictographic meanings and rebus readings

Signs of one pictured class do not sit next to each other more than a shuffle (303 pairs, 389 of 500, fraction 0.778). The same classes two signs apart do (394 pairs, 0 of 500, fraction 0.000). In the parallel passages, cross-series substitutions that share a class are 18 of 34 (bird 18; 23 of 500, fraction 0.046). The rebus word list scores 44 hits against a shuffle mean of 19.300 (4 of 500, fraction 0.008). The calendar context has 16 hits and does not clear its own null (fraction 0.468). Gv6 has 0 mapped windows. The parallel context has 28 hits (fraction 0.016). Under the rule fixed beforehand the map is recorded as R1. Nothing here is a translation of a tablet.

Provider: `mock`. Provider calls: 0.

The pictures below are cited. A word is a published proposal or it is marked HYPOTHESIS. The tests were fixed before these scores were read.

## What held, and what failed

### Held

- The secondary count, different signs of one class two places apart, beats the same shuffle (394 pairs; 0 of 500; fraction 0.000; add-one p 0.002). Classes under 5% on their own: bird, human. It was not the gate.
- Cross-hundred parallel substitutions share a class more often than the label shuffle.
- R1 rebus hits beat the shuffled word assignment (44 hits; rate 0.518; 4 of 500; fraction 0.008).
- R1 hits that mix two different words also beat the shuffle.
- The sensitivity map R2 beats its own shuffle. It is not adopted.
- The adoption rule records R1 because the summed hits and the mixed-word hits both clear 5%. The calendar context and Gv6 do not. The record is not a translation.

### Failed

- Same-class neighbors did not beat the line shuffle (303 pairs; 389 of 500; fraction 0.778; add-one p 0.778).
- After the Mamari calendar stems are removed, the neighbor count does not beat the shuffle.

## What was fixed first

Six classes can co-occur as two different signs: moon (`040`, `041`, `143`, `152`), hand (`006`, `061`, `062`, `063`, `064`), bird (Barthel 400–409 and 600–699), sea (700–759 and 770–799), human (200–299), and gaping-mouth human (300–399). `042` is not a moon sign. Guy's claim that 42 is 40 rotated is one stacked pair, and the Round 2 allograph note already refuses to apply it everywhere. `760` is the suggested lizard, not a fish. Series 410–599 are left unclassified because Guy 2006 says the digit code breaks down there.

The neighbor statistic counts adjacent stems on one line that fall in the same class and are not the same sign. The null shuffles the stems inside each line, 500 draws, seed 40. A class is claimed only if its fraction is at or under 0.0083 (0.05 divided by 6). The sum is claimed at 0.05. A second distance, two signs apart, is counted on the same draws and is not a gate. The calendar control deletes the Mamari calendar stems and repeats the shuffle with seed 40.

Parallel slots use the 99 significant stem passages already stored from Round 2. Each pair of slices is aligned again with the same Smith-Waterman scorer. The semantic gate is the cross-hundred subset: both signs are classified, their hundreds digits differ, and they share a class. The label null permutes class labels on the classified stems that occur in those mismatch columns, 500 draws, seed 41. Sharing a class inside one hundred is reported and is not the gate, because that is where allographs live.

The rebus assigns each chosen sign one whole word. `064` copies whatever word `006` receives. A window is 2, 3, or 4 mapped signs in a row. An unmapped sign breaks the row. A hit is a window whose syllables are one attested word, or whose words occur in that order in the primary running text. A strict formula is the Round 3 rule, count at least 4. The primary hit does not require that. Contexts are the joined Mamari calendar, the Gv6 line, and the left slice of each significant parallel. The null shuffles the words among the signs, 500 draws. R1 seed 42. R2 seed 43. A context is claimed only under the Bonferroni cut 0.0167. Adoption needs both the total and the diverse hits (two different words in the window) at or under 0.05. R2 cannot be adopted.

## Pictographs

| Sign | Icon confidence | Class | Tokens | Word | Word label | Rebus |
| --- | --- | --- | ---: | --- | --- | --- |
| `040` | high | moon | 152 | marama | HYPOTHESIS | R1 |
| `041` | high | moon | 54 | — | — | — |
| `143` | medium | moon | 1 | rakau | HYPOTHESIS | R1 |
| `152` | medium-high | moon | 1 | omotohi | HYPOTHESIS | R1 |
| `200` | high | human | 311 | tangata | published_hypothesis | R1 |
| `300` | high | human_gaping | 112 | — | — | — |
| `400` | medium-high | bird | 81 | — | — | — |
| `600` | high | bird | 342 | manu | HYPOTHESIS | R1 |
| `680` | medium-high | bird | 24 | makohe | HYPOTHESIS | R1 |
| `700` | high | sea | 288 | ika | HYPOTHESIS | R1 |
| `721` | medium | sea | 7 | — | — | — |
| `760` | medium | lizard | 39 | moko | HYPOTHESIS | R2 |
| `006` | high | hand | 337 | rima | HYPOTHESIS | R1 |
| `064` | high | hand | 130 | rima | HYPOTHESIS | alias |
| `061` | high | hand | 90 | — | — | — |
| `062` | high | hand | 100 | — | — | — |
| `063` | high | hand | 100 | — | — | — |
| `067` | medium | plant | 84 | niu | contested | R2 |
| `076` | low | contested | 682 | ure | published_hypothesis | R2 |
| `008` | low | — | 149 | — | — | — |

Class token totals, every stem the class function labels, not only the rows above: moon 208, hand 757, bird 1053, sea 839, human 1256, gaping-mouth human 953, plant 84, lizard 39. Corpus stems: 14841.

### Sources, one row at a time

- `040`: Guy 1990, JSO 91: 135–149: glyph 40A is the repeated night sign. Guy 2006, Rapa Nui Journal 20(1): glyph 40 is a crescent, and glyph 42 is that crescent rotated in one stacked pair (not applied to every 042). The word marama is the ordinary noun 'moon' (Metoro, vendored ca06–ca09; Churchill 1912 headword). Guy does not read the sign as that word. HYPOTHESIS: object-noun for the picture.
- `041`: Guy 2006, Rapa Nui Journal 20(1): the signs under 41 are the mirror image of those under 40. Guy 1990: delimiter crescents are not nights. No separate word is assigned.
- `143`: Guy 1990: a deep filled crescent immediately before glyph 152. Horley 2011, JSO 132: 17–38, agrees 152 is full moon. The Track 1 alignment of the Thomson / Englert / Métraux lists puts rakau on the night before omotohi. HYPOTHESIS: that night-name, not a phonetic proof.
- `152`: Guy 1990 and Horley 2011: sign 152 is full moon. Guy 2006: an anthropomorphic figure seated above a heap of stones inside an ovoid, the cook in the moon. The word omotohi is the recorded full-moon night name (Thomson 1891; Englert's list as already printed in Track 1). HYPOTHESIS: the night name at that slot.
- `200`: Barthel 1958: 40–41, via Guy 2006: series 200–299 are headed figures with ears or eyes. Wikipedia 'Rongorongo' groups glyph 200 with that head shape. Butinov and Knorozov 1957, JPS 66: 5–17, and Davletshin 2012, JSO 134: 95–110, treat 200 as a man or a title. The word tangata is that proposal. Guy 2006 also argues the head behaves as a taxogram, which is a different claim.
- `300`: Barthel 1958: 40–41, via Guy 2006 and the kohaumotu summary already cited in decipherment/allographs.py: series 300–399 have a round head and a gaping mouth. No agreed Rapanui word.
- `400`: Guy 2006: glyph 400 has the head of series 300 and the body of a bird; glyphs 400–409 are clear depictions of a bird. No separate word is assigned. Reading it as tangata manu would be an uncited extra.
- `600`: Barthel 1958: 40–41, via Guy 2006: series 600–699 are ornithomorphic. Wikipedia 'Rongorongo': the hundreds digit 6 is figures with beaks. The word manu is the ordinary noun 'bird' (Churchill 1912 headword). HYPOTHESIS: object-noun. Not a claim that every 600-series sign is this one species.
- `680`: Wikipedia 'Rongorongo', citing McLaughlin 2004, Rapa Nui Journal 18: 87–94, and Lee 1992: glyph 680 is a double-headed frigatebird, also on a moai topknot. Horley 2005 maps long-beak heads 661–684 to 660, so 680 may be an allograph of a long-beaked bird rather than its own logogram. The word makohe is the Churchill 1912 headword for the frigatebird. HYPOTHESIS: object-noun.
- `700`: Guy 2006: 700 has been suggested as a fish. Wikipedia 'Rongorongo': hundreds digit 7 is fish, arthropods, and the like, and human skulls carry the single fish glyph 700, which may stand for ika 'war casualty; fish'. The homophone is the ethnographic name kohau ika in that article. HYPOTHESIS: the word ika (Churchill 1912; Wikipedia lang=rap). The casualty sense is the same word.
- `721`: Guy 2006: 721 has been suggested as a shark. No Rapanui word is assigned. The English gloss is not turned into a headword that is absent from the vendored lexicon.
- `760`: Guy 2006: 760 has been suggested as a lizard. Not in the widely agreed set, because he marks it as a suggestion. The word moko is the Churchill 1912 headword. HYPOTHESIS: object-noun. Sensitivity map R2 only.
- `006`: Guy 2006: isolated glyph 6 is the same shape as hand 6 (lifted, three fingers and a thumb). Pozdniakov 1996, JSO 103: 296: hands 6 and 64 substitute in repeated phrases. The word rima is the Churchill 1912 headword and the Track 1 numeral rima. HYPOTHESIS: object-noun 'hand', which is homophonous with the numeral five. Neither Guy nor Pozdniakov prints that reading.
- `064`: Pozdniakov 1996: 296 and Guy 2006: hand 4 alternates with hand 6. The rebus copies the word assigned to 006. 064 is not its own permutation item.
- `061`: Guy 2006, Figure 10d: glyphs 61–64 are the same shapes as hands 1–4. No separate word. Isolated digits 1–5 and 7 are different signs, and they are not put in this class.
- `062`: Guy 2006, Figure 10d: glyph 62 is hand shape 2, a lifted fist. No separate Rapanui word is assigned.
- `063`: Guy 2006, Figure 10d. No separate word. Not read as an adze.
- `067`: Wikipedia 'Rongorongo', note 6, citing Barthel 1958: 66: glyph 67 is thought to represent the extinct Easter Island palm. The same note says the Jaussen list identified it as the niu coconut palm, a species introduced after contact. Contested. Sensitivity map R2 only. niu is not a Churchill headword in the vendored list.
- `076`: Fischer 1995 and 1997: 076 is a phallic suffix. Davletshin 2012: patronymic ure. Guy 1998, Anthropos 93: 552–555, rejects Fischer's cosmogonic reading. The picture is not widely agreed. Sensitivity map R2 only. The word ure is in Thomson and in Churchill 1912.
- `008`: Guy 2006 uses glyph 8 as a nickname 'flower'. Fischer's Staff example, already locked in Track 3 as 606.076 700 008, glosses one 008 as the sun. The two claims disagree. No class and no word.

### Left out

- **canoe.** No Barthel number for a canoe is stated by Barthel 1958 as cited here, Guy 1990, Guy 2006, Horley 2011, Davletshin 2012, or the Wikipedia glyph notes used above. The Churchill headword vaka is not attached to a sign.
- **sea turtle.** Wikipedia mentions a sea-turtle glyph in a caption and does not give a Barthel number in the prose. Glyph 280 is described there with glyph 200 as a headed figure, and Horley 2005 decomposes 280 as 070.002. It is not entered as a turtle. The Churchill headword honu is not attached to a sign.
- **Guy 2006 calendar phonograms atua, hua, hiro/ro.** Guy 2006 proposes a feather-cloak sign for atua, a fruit or scrotum sign for hua, and glyph 3 or 30 for ro or hiro. The prose does not lock those pictures to a Barthel number that this track can separate from the plate. They are not encoded.

Identical neighbors of the two single-sign classes, not a gate: `067` sits next to itself 4 times, `760` 0 times.

## Semantic co-occurrence

Summed different-sign neighbors: **303**. Line shuffle: 389 of 500 reach that count (fraction 0.778, add-one p 0.778). Holds at 5%: no.

| Class | Pairs | Null | Fraction | Bonferroni |
| --- | ---: | --- | ---: | --- |
| moon | 6 | 487 of 500 | 0.974 | no |
| hand | 41 | 10 of 500 | 0.020 | no |
| bird | 80 | 34 of 500 | 0.068 | no |
| sea | 35 | 470 of 500 | 0.940 | no |
| human | 91 | 440 of 500 | 0.880 | no |
| human_gaping | 50 | 482 of 500 | 0.964 | no |

Two signs apart, same draws, not the neighbor gate: 394 pairs, null 0 of 500 (fraction 0.000, add-one p 0.002). Would have cleared 5% if it had been the gate: yes.

| Class | Two apart | Null | Fraction |
| --- | ---: | --- | ---: |
| moon | 13 | 129 of 500 | 0.258 |
| hand | 34 | 83 of 500 | 0.166 |
| bird | 107 | 0 of 500 | 0.000 |
| sea | 48 | 115 of 500 | 0.230 |
| human | 131 | 0 of 500 | 0.000 |
| human_gaping | 61 | 257 of 500 | 0.514 |

After the calendar is removed, the two-apart count is 379 (null 0 of 500, fraction 0.000). A pattern that fits these two distances is Guy 2006's harmonic sequence: a repeated slot of one kind of sign, with something else between the repetitions. Neighbors are then often different classes, and the matching class sits two places away. That reading of the distances is an interpretation of a result that was already in the plan. It is not a new test.

Calendar stems removed (101 stems taken out of the Mamari passage). Sum: **301**. Null 312 of 500 (fraction 0.624, add-one p 0.625). Holds: no.

| Class | Pairs | Null | Fraction | Bonferroni |
| --- | ---: | --- | ---: | --- |
| moon | 4 | 24 of 500 | 0.048 | no |
| hand | 41 | 14 of 500 | 0.028 | no |
| bird | 80 | 33 of 500 | 0.066 | no |
| sea | 35 | 471 of 500 | 0.942 | no |
| human | 91 | 449 of 500 | 0.898 | no |
| human_gaping | 50 | 460 of 500 | 0.920 | no |

These classes are Barthel's appearance bins, plus the few signs Guy and the calendar papers single out. A positive neighbor count means those bins sit together in the text. It does not discover the pictures. The pictures were the input.

## Parallel slots

Passages: 99. Published mismatch cells: 254. Realigned mismatch cells: 249. Realigned columns: 2125.

Classified mismatch pairs: 118. Same class: 101 (rate 0.856). Label shuffle: 0 of 500 (fraction 0.000, add-one p 0.002). This rate includes pairs inside one hundred. It is not the semantic gate.

Cross-hundred classified pairs: 34. Same class: 18 (rate 0.529). Label shuffle: 23 of 500 (fraction 0.046, add-one p 0.048). Holds at 5%: yes.

Those 18 pairs break down by class as: bird 18. Pair counts, order ignored: 400–600 ×9, 400–605 ×2, 407–607 ×1, 400–633 ×1, 405–605 ×1, 400–680 ×1, 409–609 ×1, 401–600 ×1, 405–600 ×1. Series 400–409 was classed with series 600–699 because Guy 2006 says the first ten signs of series 400 are birds. Pozdniakov 1996 had already treated gaping-mouth and bird heads as variants, and the 2007 inventory still lists 400 apart from 600. This gate says those two hundreds fill the same parallel slots more than a relabeling. It does not say that fish, hands, or people do.

## Rebus

R1 words, and whether the vendored lists contain them. Running-text count is the mapped spelling, so `tagata` and `tangata` share a count.

| Sign | Word | Syllables | In a word list | Running-text tokens |
| --- | --- | --- | ---: | ---: |
| `040` | marama | ma-ra-ma | yes | 100 |
| `143` | rakau | ra-ka-u | yes | 18 |
| `152` | omotohi | o-mo-to-hi | yes | 0 |
| `200` | tangata | ta-nga-ta | yes | 432 |
| `600` | manu | ma-nu | yes | 271 |
| `680` | makohe | ma-ko-he | yes | 0 |
| `700` | ika | i-ka | yes | 98 |
| `006` | rima | ri-ma | yes | 125 |

R1 windows: 85. Hits: 44. Hit rate: 0.518. Null mean hits: 19.300. Null: 4 of 500 (fraction 0.008, add-one p 0.010). Holds: yes. Diverse hits: 15. Diverse null: 15 of 500 (fraction 0.030, add-one p 0.032). Diverse holds: yes. Adopted: yes.

| Context | Windows | Hits | Rate | Diverse | Phrase | Word | Strict formula | Null | Fraction | Bonferroni |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| calendar | 44 | 16 | 0.364 | 0 | 16 | 0 | 0 | 234 of 500 | 0.468 | no |
| gv6 | 0 | 0 | 0.000 | 0 | 0 | 0 | 0 | 500 of 500 | 1.000 | no |
| parallels | 41 | 28 | 0.683 | 15 | 28 | 1 | 5 | 8 of 500 | 0.016 | yes |

Hit windows, R1:

- calendar: marama marama ×16 (running text 1)
- gv6: none
- parallels: tangata tangata ×9 (running text 1), ika manu ×8 (running text 2), manu manu ×4 (running text 4), tangata manu ×2 (running text 1), ika tangata ×2 (running text 1), tangata rima ×1 (running text 10), rima tangata ×1 (running text 3), tangata ika ×1 (running text 1)

Gv6 phrases under R1. An unmapped sign stays a number. These lines are the genealogy pattern from Track 3. They are not extra hits unless the mapped signs also form a window of length 2 or more.

- strict: 200 000! 280.076 → tangata 000 280 076
- strict: 200 280 730.076 → tangata 280 730 076
- strict: 200 730 517a.076 → tangata 730 517 076
- strict: 200 517a 222.076 → tangata 517 222 076
- quad: 200 769 381 002.076 → tangata 769 381 002 076

R2 adds `076` ure, `067` niu, and `760` moko. Windows: 99. Hits: 46. Rate: 0.465. Null mean: 21.892. Null: 6 of 500 (fraction 0.012, add-one p 0.014). Holds: yes. Diverse: 16 (18 of 500, fraction 0.036). Adopted: no.

| Context | Windows | Hits | Rate | Diverse | Null | Fraction |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| calendar | 44 | 16 | 0.364 | 0 | 280 of 500 | 0.560 |
| gv6 | 4 | 0 | 0.000 | 0 | 500 of 500 | 1.000 |
| parallels | 51 | 30 | 0.588 | 16 | 5 of 500 | 0.010 |

Fischer's Staff triad `606.076 700 008` is the example already locked in Track 3. R1 reads `700` as ika and does not assign `606` or `008`. `076` is only on R2. The triad is not scored as its own crib beyond whatever window the rules already catch.

## What this does not claim

No tablet is translated. A neighbor count inside Barthel's own series is not an independent identification of birds or fish. A rebus hit on a repeated crescent is the word assigned to that one sign, said twice. Guy's taxogram argument for sign 200 is still open, and it pulls against reading every 200 as tangata. Metoro's recitations are language material. Track 4 already found they do not label the signs, and this track does not pair them again.

The run uses `MockProvider` only. Provider calls: 0.
