# Round 4, Track C: rock art and carved objects

No sign gains a word. The supported claims are shape matches that a published paper already ties to a Barthel number. Where the tablets were tested, the question was only whether those signs pile up in particular texts more than a random placement of the same number of hits. A yes would still not be a translation.

Provider: `mock`. Provider calls: 0. `reading` is null. Adopted lexical readings: none.

## What was compared

The outside material is the rock art catalogued by Georgia Lee and the carved objects discussed by Horley and Lee, the Orliacs, Fischer's corpus as updated by Horley, Davletshin and Wieczorek, Routledge, and Métraux. The sign corpus is the vendored Barthel text: 14488 stems on 22 tablets.

Horley and Lee 2008 print Barthel numbers for the comparisons below. A suffixed number is tested as that allograph, not as the whole stem. Komari, Makemake faces, the full birdman body, turtles, canoes, tahonga, the back of Hoa Hakananai'a, the Peabody birdman stones, and the New York birdman figure are in the dataset with a null sign number, because this round did not verify a number for them. McLaughlin 2004's glyph 51 and glyph 638 were not adopted: on the published page the two columns run together, so the pairing is not clean enough to use.

The wooden rei miro J and L are already rongorongo texts. Their signs are listed and then left without an implication. The crescent *shape* of a rei miro is a different claim, and that claim is sign 007.

## How the test works

For a sign with k hits, k positions are drawn at random among the stems. The statistic is the chi-square of tablet counts against tablet length. The p-value is (hits + 1) / (trials + 1), one sided, greater than the observed statistic.

Trials: 2000. Seed: 4. A sign enters the corrected test only at 20 hits or more. Signs in that set: 074, 660, 680, 007, 240. The corrected threshold is 0.0100. Control signs, the eight most common stems outside the set: 001, 076, 002, 003, 004, 600, 006, 022. Their median p-value is 0.0005.

A sign is called more concentrated than chance only if it has at least 20 hits, its p-value clears 0.05 divided by the number of such signs, and that p-value is also smaller than the median p-value of the eight most common signs that are not in the petroglyph set. That status is about where the sign sits. It is not a meaning.

## Signs with a published number

| Sign | Motif in the source | Vendored stems | Published count | Most used tablet | p | Status |
|---|---|---:|---|---|---:|---|
| 700b | fish with a bulb at the base of the tail | 1 | — | P (1) | null | not_tested |
| 721 | fish with a bulb at the base of the tail | 7 | — | P (2) | null | not_tested |
| 733 | fish with a bulb at the base of the tail | 4 | — | B (1) | null | not_tested |
| 074 | hook-shaped or gourd-shaped figure with a komari cut on it | 135 | 94 | A (31) | 0.1649 | ordinary |
| 660 | long-beaked bird | 32 | 29 | A (11) | 0.0100 | nominal_only |
| 680 | two-headed long-beaked bird | 24 | 23 | R (9) | 0.0040 | nominal_only |
| 007 | rei miro | 171 | — | A (35) | 0.0055 | nominal_only |
| 240 | sitting man | 24 | — | A (6) | 0.0330 | nominal_only |
| 513 | eye mask | 2 | — | I (2) | null | not_tested |
| 550 | bird with a star around its head | 2 | — | C (1) | null | not_tested |

Published counts are Barthel's, quoted by Horley and Lee. They are not replaced by the vendored recount. A difference means the Kohaumotu encoding and Barthel's 1958 total are not the same sample. It is not a new reading.

Neighbor signs are in the JSON. They were not turned into a p-value.

Stem 700, which is wider than the cited allograph 700b, occurs 288 times. 700b itself occurs once. The wider stem is not used as evidence for the tail-bulb petroglyph.

The eight common control signs, included so a small p-value can be compared with an ordinary sign:

| Control sign | Stems | p |
|---|---:|---:|
| 001 | 769 | 0.0005 |
| 076 | 682 | 0.0005 |
| 002 | 442 | 0.0005 |
| 003 | 432 | 0.0005 |
| 004 | 422 | 0.0005 |
| 600 | 342 | 0.0010 |
| 006 | 337 | 0.0005 |
| 022 | 316 | 0.0005 |

7 of the 8 common signs sit on the floor of this permutation test (p = 0.0005). A petroglyph sign is counted as more bunched than chance only when it clears the corrected threshold and is also past that median. None does.

## Do the themed signs cluster together?

| Theme | Hits | p | Status |
|---|---:|---:|---|
| long-beaked birds at the birdman court | 56 | 0.0100 | nominal_only |
| the tail-bulb forms named by Horley and Lee | 12 | null | not_tested |
| the four signs Horley and Lee name on locus 17 | 199 | 0.0020 | nominal_only |

Pre-set pairs, asked before the counts were read. The p-value is for sharing a line, not for sitting side by side. Adjacent hits are the raw count in either order.

| Pair | Why it was paired | Lines in common | p | Adjacent hits |
|---|---|---:|---:|---:|
| 660 680 | two long-beaked bird forms | 1 | 0.6347 | 0 |
| 700b 721 | tail-bulb marine signs | 0 | 1.0000 | 0 |
| 700b 733 | tail-bulb marine signs | 0 | 1.0000 | 0 |
| 721 733 | tail-bulb marine signs | 0 | 1.0000 | 0 |

## A check on one printed claim

Horley and Lee say open-beak forms of sign 660 occur on Br2, Br7, Pr2, and Ua3. In the vendored pages:

- Br2: stem 660 is not on the line. Other 600-series stems there: 600, 630, 670. They are not treated as open-beak 660.
- Br7: stem 660 is not on the line. Other 600-series stems there: 600, 624, 638, 678. They are not treated as open-beak 660.
- Pr2: stem 660 is not on the line. Other 600-series stems there: 600, 670, 675. They are not treated as open-beak 660.
- Ua3: stem 660 is not on the line. Other 600-series stems there: 600. They are not treated as open-beak 660.

## Carved objects that do not yield a sign meaning

Rei miro 1 (tablet J) has 2 stems in the vendored text: 522 088. Implication: null.

Rei miro 2 (tablet L) has 51 stems. Implication: null. The list is in the JSON.

The New York birdman figure is not vendored, so its signs are null. Tahonga pendants, moai kavakava cranial carvings, and the 'Orongo stones are documented for what the objects were. The hand-like carving on Peabody Essex E 18646 is only called similar to 052, 52x, or 162, so those numbers stay unadopted and untested.

## What is supported, and what is speculation

These signs meet the corrected threshold on their own: 660, 680, 007. They do not beat the ordinary common signs, which are bunched at least as tightly. The small p-value is the usual shape of this corpus, not evidence that the petroglyph theme gathered them. `supported_lexical_readings` is empty.

Supported, as iconography only:

- 700b, 721, and 733 are the fish forms Horley and Lee name. In this corpus they occur 1, 7, and 4 times. That is below the pre-set count of 20, so the concentration test is null. The picture match is real as far as their paper goes. A fishing reading is speculation. Stem 700 is a wider sign and is not this match.
- 074 resembles the hook or gourd in house 44. Strength: printed number, plus Barthel's count of 94. Calling it a fertility sign because a komari was cut on the petroglyph is speculation.
- 660 resembles a long-beaked bird, and 680 a two-headed one. Strength: printed numbers and counts. A manutara or Makemake reading is speculation.
- 007 resembles a rei miro. Strength: printed number. It does not read the texts on the wooden pectorals.
- 240 resembles a sitting man, 513 an eye mask, 550 a bird with a star at its head. Strength: one sentence in Horley and Lee 2008, with no count. A Makemake reading of 513 is speculation.

Speculation, left null and untested: glyph 51 as komari, glyph 638 as the birdman, any turtle or canoe sign, any tahonga or egg sign, Fedorova's reading of a cranial carving as the name Vai Rapa, and Fischer's creation-chant decipherment. Those last two are someone else's hypotheses. This round does not adopt them.

Horley and Lee themselves say the Mata Ngarau pictures match single signs and do not form a continuous text. Fischer's definition, as McLaughlin quotes it, requires a sequence of two or more glyphs before something counts as an inscription. The rock art can suggest what a picture is of. It cannot, by itself, supply the word.

## Sources

- Barthel, Thomas S. 1958. *Grundlagen zur Entzifferung der Osterinselschrift*. Hamburg: Cram, de Gruyter. Counts as cited by Horley and Lee, not re-read page by page here.
- Fischer, Steven Roger. 1997. *Rongorongo: The Easter Island Script*. Oxford: Clarendon Press. Used for the object catalog as updated by Horley, Davletshin and Wieczorek 2018, and for the definition of an inscription as quoted by McLaughlin.
- Forment, Francina. 1993. In Fischer, ed., *Easter Island Studies*. Cited at page 212 by Wieczorek and Horley for designs shared across figurines and tahonga.
- Horley, Paul. 2005. Allographic variations and statistical analysis of the rongorongo script. *Rapa Nui Journal* 19(2): 107–116.
- Horley, Paul, and Georgia Lee. 2008. Rock art of the sacred precinct at Mata Ngarau, 'Orongo. *Rapa Nui Journal* 22(2): 110–116.
- Horley, Paul, and Georgia Lee. 2012. Easter Island's birdman stones in the collection of the Peabody Museum. *Rapa Nui Journal* 26(1): 5–20. No glyph number was verified from the article text in this round.
- Horley, Paul, Albert Davletshin, and Rafal Wieczorek. 2018. How many scripts were there on Easter Island? In Jakubowska-Vorbrich, ed., *The Sleep of Reason Produces Monsters*.
- Koll, Robert R. 1991. Petroglyphs inside Orongo's houses. *Rapa Nui Journal* 5(4): 61–62.
- Lee, Georgia. 1990. *An Uncommon Guide to Easter Island*. Counts of 375 birdmen, 195 komari, and 140 faces, as quoted by Horley and Lee 2008.
- Lee, Georgia. 1992. *The Rock Art of Easter Island*. Los Angeles: UCLA Institute of Archaeology.
- Lee, Georgia. 2004. Rapa Nui's sea creatures. *Rapa Nui Journal* 18(1).
- McLaughlin, Shawn. 2004. Rongorongo and the rock art of Easter Island. *Rapa Nui Journal* 18(2): 87–94.
- Métraux, Alfred. 1940. *Ethnology of Easter Island*. Bernice P. Bishop Museum Bulletin 160. Pages as cited by Horley and Lee.
- Orliac, Catherine, and Michel Orliac. 2008. *Trésors de l'Île de Pâques / Treasures of Easter Island*. Paris.
- Routledge, Katherine. 1919. *The Mystery of Easter Island*. London.
- Routledge, Katherine. 1920. Survey of the village and carved rocks of Orongo. *Journal of the Royal Anthropological Institute* 50: 425–451.
- Wieczorek, Rafal M., and Paul Horley. 2023. New visualization method for cranial carvings of Rapanui wooden figurines. *Archaeometry*.
