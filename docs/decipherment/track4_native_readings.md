# Track 4 — Native readings against the tablets

Question: do Ure Vaeiko's 1886 chants, or Metoro's 1870s sign-by-sign words, line up with the Barthel coding of a tablet any more tightly than a shuffle?

Short answer: the repeated sentences are real, and the Santiago Staff really does repeat glyph 076 on a tight spacing. Those two facts do not add up to a reading. The chant Thomson printed was not a sign-by-sign reading of the tablet he printed it with, and Metoro's words do not stick to the same Barthel sign.

No glyph is given a meaning here. A gloss is either quoted from a named source or marked as a hypothesis. The test uses no live model (`MockProvider` only).

## Sources

Ure Vaeiko chanted for William J. Thomson in December 1886. Thomson printed the chants in *Te Pito te Henua, or Easter Island* (Report of the U.S. National Museum for the year ending June 30, 1889; Washington, 1891). The working copy is the Kohaumotu transcription of those pages, checked against the Internet Archive scan `tepitotehenuaor00thomgoog`. Files and the plate table are in `data/readings/thomson_1891/`.

Metoro Tauʻa Ure chanted for Bishop Jaussen in the 1870s. Jaussen wrote a word-group against each sign, with a hyphen between groups. The line text is Kohaumotu's transcription of those notebooks (`data/readings/metoro_jaussen/`). Barthel 1958 and Fischer 1997 are not copied. Sign numbers are the Barthel pages already vendored under `tests/fixtures/`.

Thomson's own headings, and only those, tie a chant to plates:

| Chant | Thomson 1891 | Plates |
| --- | --- | --- |
| Apai | pp. 517–518 | XXXVI–XXXVII |
| Atua Matariri | pp. 520–521 | XXXVIII–XXXIX |
| Eaha to ran ariiki kete | pp. 523–524 | XL–XLI |
| Ka ihi uiga | p. 525 | XLII–XLIII |
| Ate-a-renga-hokau iti poheraa | p. 526 | XLIV–XLV |

A later catalog (Kohaumotu, and the vendored R index) identifies plates XXXVIII–XXXIX with Barthel tablet **R**, Smithsonian A129773-0, the tablet called Atua-Mata-Riri because of this chant. The same catalog, not Thomson, points Apai at **E**, Eaha at **S**, Ka ihi uiga at **D**, and Ate-a-renga at **C**. Those four identifications are secondary. The staff (**I**) is not in Thomson's plate list.

Salmon's English, printed by Thomson, translates the chant. It is not a glyph gloss, and this track does not use it as one.

## What Thomson already reported

On p. 516 Thomson writes that Ure Vaeiko's turns of the photograph did not follow the number of signs on the lines, and that when another tablet's photograph was slipped in, the same story went on. Ure Vaeiko's explanation, as Thomson gives it, was that the signs' values had been forgotten, but a named tablet still called up its story. That is recognition of an object, not a reading of its signs.

## Atua Matariri is a real repeated sentence

Of the 48 printed verses, 41 contain both the copula as Thomson spelled it (`Ki ai Kiroto` or `Kia ai Kiroto`) and a product marker (`Kapu te`, `Kapu to`, or the one `Mapu te`). Seven verses do not. The frame is the sentence "X ki ai ki roto Y, ka pu te Z": X couples with Y and Z comes forth. That paraphrase is Thomson's own English heading for the chant ("the marriage of certain gods and goddesses"), not a claim about any sign.

The names mostly do not repeat. Three X-names do: `tikitehatu`, `atua metua`, `kuhikia`. One Y-name does (`hiuaoioi`). One Z-name does (`ngaatu`). So the repetition is the frame, not a chorus of the same names.

Between two full verses that sit next to each other there are 38 gaps. Counting the words in Y, in Z, and in the next verse's X (and not counting the words `kapu te` themselves) gives this histogram:

| Words in the three name slots | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- |
| Adjacent verse pairs | 18 | 15 | 3 | 1 | 1 |

The mode is 3 because most names are printed as one word. That is how the sentence is built. It is not a measurement of the tablet.

The other four chants do not use this frame. Apai contains `apai` 5 times and the copula 0 times. Eaha repeats `Eaha to ran ariiki kete` 10 times. Ka ihi uiga repeats `Ka ihi uiga` 4 times and `auwe … poki` 5 times. Ate-a-renga repeats `hoa` 5 times and the copula 0 times. Those are repeated lines in the chants. They are not a sign alignment.

## Tablet R, the plates the chant was printed with

Vendored Ra plus Rb: 17 lines (Rb9 is empty), 490 stems, **0** stems of 076.

Forty-eight verses are not one verse per line of a 17-line tablet. Glyph 076, the sign Fischer later treated as the copula, is absent. There is no 076-triad structure on the object Thomson headed this chant with. The same is true of the other tablets the later catalog attaches to the other chants: E has 076 five times in 886 stems, S three times in 787, D zero times in 266, C zero times in 1004. None of those is a 076 text.

This agrees with Thomson p. 516. The chant is a traditional list. It was not read off the signs of tablet R.

## The staff pattern is real, and it is not this chant

Barthel text I, the Santiago Staff, is a different object. Vendored Ia has 2469 stems and **564** stems of 076. That 564 is the count already locked by the Ia 076 inventory. Between successive 076s on the same line there are 550 gaps (564 minus one per line). Their lengths:

| Gap | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Count | 14 | 57 | 59 | 197 | 137 | 43 | 15 | 13 | 9 | 3 | 2 | 1 |

A shuffle that keeps each line's signs and only moves them puts far fewer gaps at length 3. In 1000 such shuffles (seed 0), **none** reached 197 gaps of length 3. The staff's 076s are spaced. That is a fact about the staff. The older cell count (578 cells, median length 3, 203 cells of length 3) includes the partial run at each end of a line; the 550 gaps here are only the runs between two 076s. Both descriptions are the same spacing.

Fischer 1995 proposed that this spacing is the Atua Matariri sentence, with glyph 76 standing for `ki ai ki roto`. That gloss is a **hypothesis**. It is not a result of this test. Guy rejected the reading. Two checks from the counts:

- The chant's three name-slots are usually 3 or 4 words wide (18 and 15 of 38 pairs). The staff's gaps are also piled on 3 and 4 (197 and 137 of 550). A scaled L1 distance between those two histograms is 5222, and 0 of 1000 shuffles of the staff were that close or closer. This is the resemblance Fischer used. It is not a second, independent discovery: the chant width was defined as three name slots, and the staff was already known to peak near 3. Matching a peak at 3 to a peak at 3 does not tell you which sign is which name.
- If `ka pu te` were also written as signs, the gap between copulas would be wider than 3. Only 86 of 550 staff gaps are 5 or longer. A model that writes the product marker as extra signs fits worse than a model that writes only the copula. Both models are still hypotheses. Neither names a sign.

Thomson did not print Atua Matariri under the staff. Tablet R, which he did print it under, has no 076 at all. So the staff pattern and the chant formula are two repetitive structures that look alike at the scale of "a delimiter, then about three items." They have not been shown to be the same text.

## Metoro does not use one word for one Barthel sign

Jaussen's hyphen is one sign on the Kohaumotu pages. The vendored Barthel token (one hyphen-separated code, ligatures kept together) is the sign this comparison uses. A line is paired only when those two counts are already equal. Inventing an alignment for the other lines would manufacture a correspondence.

83 lines have a Metoro page. **5** match the vendored token count: Ab1 (82), Cb8, Ca2, Ev1, Ev8. **78** do not. That mismatch is expected on Mamari and Keiti: on Cb1 Jaussen says the chant was no longer being copied in full and that he wrote only the essential word, and that he did the same for Keiti. Ab1 is the line where he says the chant was still being written out completely, and it is also a count match, so it is the clean case.

On the 220 paired positions, codes that occur at least three times:

| Test | Observed | What the shuffle does |
| --- | --- | --- |
| Same published code, same phrase | 26 of 116 hits, 24 codes | 136 of 1000 shuffles tie or beat 26 |
| Same stem (ligature's first number), same phrase | 27 of 144 hits, 25 stems | 282 of 1000 tie or beat 27 |
| Ab1 alone, same stem, same phrase | 15 of 61 hits, 14 stems | 239 of 1000 within-Ab1 shuffles tie or beat 15 |
| Mean content-word overlap inside a stem | 24 on a scale of 1000 | 37 of 1000 shuffles tie or beat 24 |

The phrase tests are inside the shuffle. Metoro does not repeat a phrase on a repeated sign more than chance.

One stem meets a half share: **741**, on Ab1, 4 times, and 2 of those 4 are the phrase `mo te ariki`. The other two are different words. Two out of four is not a gloss, and this track does not assign 741 a meaning.

The content-word overlap is the only figure a shuffle rarely beats (37/1000). The overlap itself is 24/1000: a few words such as `rutua` show up twice under stem 005 inside otherwise different phrases (`rutua te pahu`, `rutua te maeva`). That is a trace of repeated vocabulary, not a sign list. A consistent code would reuse the same phrase and would score in the hundreds on that scale, not at 24.

## Confidence

| Claim | Confidence | Why |
| --- | --- | --- |
| Atua Matariri repeats one copulation sentence 41 times in 48 verses | High | It is a count of the 1891 print |
| That sentence was not read sign-by-sign off tablet R | High | Thomson p. 516; 48 verses vs 17 lines; 076 occurs 0 times |
| Staff glyph 076 is spaced more evenly than a line shuffle | High | 197 gaps of length 3; 0/1000 shuffles |
| That spacing *is* Atua Matariri, and 076 *means* the copula | Low | Hypothesis (Fischer 1995). The shape matches because both are "delimiter + about three items." No name is tied to a sign. The chant's own tablet lacks 076 |
| Metoro's words are a consistent Barthel lexicon | High that they are not | Phrase match is inside the shuffle on the only lines that can be paired. The leftover word-overlap is 24/1000 |

Nothing in this track is a translation.
