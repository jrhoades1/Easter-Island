# Round 4, Track E — Do the published sound values spell Rapanui?

This is a test of other people's proposals. It is not a decipherment.
No new reading was made up. Where a scholar did not publish a list of
sign-to-sound pairs, that list was left empty.

Provider: MockProvider. Provider calls: 0.
Adopted readings: none. `reading` is None.

## What was tested

Each published value was laid onto the Barthel stems of tablets A–V.
A span of two, three, or four signs counts only when every sign in it
has a value. The span scores when those sounds are exactly one attested
Rapanui word, or exactly a short phrase that already occurs in the old
Rapanui sample (Thomson's chants, Metoro's recitations, and Routledge's
timo line, plus the public-domain word lists for single words).

Two comparisons were fixed before the scores were read:

1. Shuffle the published values among the same signs.
2. Replace them with random attested sounds of the same size, 500 times,
   seed 41. The word and phrase lists are sorted first, so that seed
   always draws the same sequence.

A proposal would have to beat both, at 5 percent, and still beat them
after a Holm correction across every scored proposal, including the
tangata retest. Calendar lines Ca6–Ca9, the Gv6 genealogy, and the
Great Tradition tablets H, P, and Q are counted inside that corpus and
also printed on their own. Those extra counts are not extra chances to pass.

Attested word-shapes of two or more syllables: 2723.
Attested short phrases: 27950.
Syllable types available to the random draw: 50.

## Sets with no sound list

These were looked up and not filled in.

- **Davletshin 2022.** The abstract says twenty provisional values, eleven of them checked by cross-reading (seven logograms, four syllables). The sign-by-sign table was not in an open copy retrieved here, and it was not reconstructed.
- **Pozdniakov and Pozdniakov 2007.** No sign-sound pairs to apply. A map was not invented for them.
- **Horley.** No sign-sound pairs to apply. A map was not invented.
- **Guy 1990.** Guy says some adjunct glyphs on the Mamari crescents may be syllabic rebuses for night names. The open text retrieved from Persée does not include the itemized list, so those values were not reconstructed.
- **Barthel 1958.** The retrievable Barthel claim used in this repository is that Ca6–Ca9 is a lunar calendar, including a full-moon figure. That is a content claim, not a sign-sound table, and it was not turned into syllables.

## Scored proposals

### Davletshin 2012: davletshin_2012_names

Three sound values he states. He does not settle sign 200.

| Sign | Cited value | Kind | Status |
| --- | --- | --- | --- |
| `076` | ko (ko) | syllable | proposed |
| `021` | 'a ('a) | syllable | tentative |
| `530` | ariki (a-ri-ki) | word | tentative |

Citation: Davletshin 2012, Journal de la Société des Océanistes (https://journals.openedition.org/jso/6658).

Corpus: 2 spans (0 word, 2 formula) out of 54 valued spans. Shuffle p = 0.667 (4 of 6, permute_values). Random p = 0.914 (457 of 500). Holm-adjusted worse p = 1.000. Adopted: False.

Inside that total, the calendar slice has 0 hits, Gv6 has 0, and the Great Tradition (H, P, Q) has 0.

Examples of hits:
- Ia3: `530 076` → a-ri-ki-ko (formula)
- Gv8: `530 076` → a-ri-ki-ko (formula)

Not scored: He considers a syllabic (te), so that 076-200 would be ko te, and says he will not draw a conclusion about TB200.

### Davletshin 2012: davletshin_2012_numerals

The crescent of the Mamari passage is the word tahi 'one'.

| Sign | Cited value | Kind | Status |
| --- | --- | --- | --- |
| `040` | tahi (ta-hi) | word | proposed |

Citation: Davletshin 2012, Journal of the Polynesian Society 121(3): 243–274, Numerals and phonetic complements in the Kohau rongorongo script.

Corpus: 0 spans (0 word, 0 formula) out of 41 valued spans. Shuffle p = 1.000 (31 of 31, reassign_to_frequent_signs). Random p = 1.000 (500 of 500). Holm-adjusted worse p = 1.000. Adopted: False.

Inside that total, the calendar slice has 0 hits, Gv6 has 0, and the Great Tradition (H, P, Q) has 0.
Those signs do occur. Under this map their sounds are not an attested word or an attested short phrase, including on the calendar lines.

Not scored: The Standing Man phonetic complement is hi or i. He does not choose, so neither syllable is scored.
Not scored: A possible ru complement is one of three explanations he does not decide.

### Fischer 1995: fischer_1995

Word and phrase values from the Santiago Staff example 606.76 700 8.

| Sign | Cited value | Kind | Status |
| --- | --- | --- | --- |
| `600` | manu (ma-nu) | word | tentative |
| `606` | manu mau (ma-nu-ma-u) | phrase | tentative |
| `700` | ika (i-ka) | word | tentative |
| `008` | ra'a (ra-'a) | word | tentative |
| `076` | ki ai ki roto ki (ki-a-i-ki-ro-to-ki) | phrase | tentative |

Citation: Fischer 1995, Journal of the Polynesian Society 104: 303–321; the same sign values are restated in Fischer's further cosmogonic-text note.

Corpus: 26 spans (0 word, 26 formula) out of 181 valued spans. Shuffle p = 0.250 (30 of 120, permute_values). Random p = 0.078 (39 of 500). Holm-adjusted worse p = 0.750. Adopted: False.

Inside that total, the calendar slice has 0 hits, Gv6 has 0, and the Great Tradition (H, P, Q) has 14.

Examples of hits:
- Br9: `700 600` → i-ka-ma-nu (formula)
- Bv6: `600 600` → ma-nu-ma-nu (formula)
- Bv12: `700 600` → i-ka-ma-nu (formula)
- Ra5: `700 600` → i-ka-ma-nu (formula)
- Da5: `700 600` → i-ka-ma-nu (formula)
- Ev6: `700 600` → i-ka-ma-nu (formula)
- Hr4: `600 600` → ma-nu-ma-nu (formula)
- Hr8: `600 600` → ma-nu-ma-nu (formula)
- Hv1: `600 600` → ma-nu-ma-nu (formula)
- Hv12: `700 600` → i-ka-ma-nu (formula)
- Pr3: `600 600` → ma-nu-ma-nu (formula)
- Pr4: `600 600` → ma-nu-ma-nu (formula)

## Retest: sign 200 as tangata

This is a hypothesis, carried forward because Round 3 found a phrase
score sitting on the 5 percent line and did not adopt it. Davletshin
does not read sign 200 as tangata. The confirmatory count uses only
tablets HIJKLMNOPQRSTUV. Tablet G, including the Gv6
genealogy that suggested a 'man' sign, is not in that count.
Tablets A–G were already in the earlier pooled look, so this slice
is a check, not a fresh discovery.

Hold-out: 16 spans (0 word, 16 formula) out of 20 valued spans.
Shuffle p = 0.065 (2 of 31).
Random p = 0.014 (7 of 500).
Holm-adjusted worse p = 0.258. Adopted: False.

The A–G count is printed so it can be seen, and it is not the p-value: 9 spans.

Hold-out examples:

- Ra1: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Ra1: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Oa5: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Va1: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Hr5: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Hr5: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Hr7: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Hr11: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Pr4: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Pr4: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Pr6: `200 200` → ta-nga-ta-ta-nga-ta (formula)
- Pv1: `200 200` → ta-nga-ta-ta-nga-ta (formula)

## What this does not say

Beating a shuffle would have meant these particular sounds, on these
particular signs, spell real words more often than the same sounds
swapped around. None of the scored sets is adopted. A miss does not
prove the author wrong about a passage they were explaining. It means
the values, applied as sounds across the corpus, do not spell the
attested words and short phrases above the comparisons that were
fixed in advance.

The run uses MockProvider only. Provider calls: 0.
