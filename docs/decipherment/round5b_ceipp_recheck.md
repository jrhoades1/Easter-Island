# Round 5, Track B — CEIPP drawings rechecked against the key passages

The headline counts do not move. The drawings were fetched. No Barthel number in the repository was replaced, because a new number would have been an invention. Crescent counts, delimiter gaps, the Gv6 handoffs, the Staff rate of 076 after a 999 bar, the Great Tradition alignment, and the bird-substitution counts stay where the vendored Barthel text already had them.

Provider: `MockProvider`. Provider calls: 0.

## Credit and licence

Drawings and transliteration: C.E.I.P.P. (Cercle d'Études sur l'Île de Pâques et la Polynésie), from Thomas Barthel's materials, published on rongorongo.org and mirrored at kohaumotu.org.

The CEIPP copyright page says: "There are no restrictions on copying and distributing the contents of this site as long as the sources are acknowledged and the distribution is non-profit." Source: [kohaumotu.org/rongorongo_org/copy.html](http://kohaumotu.org/rongorongo_org/copy.html), the mirror of the CEIPP page. That licence is not the licence of this repository. The raster strips and the vector pages were fetched for this check and were not committed. What is stored is the URLs, the SHA-256 hashes, and this note. See also `docs/round4e_image_sources.md`.

## What was fetched

Two forms of the same mirror were used.

The CEIPP raster strips are the line drawings named in the corpus pages. The ones opened for this check are about 74 pixels tall (Mamari strips 522 pixels wide, the others 622). At that size a crescent, a bar, and a full figure can be told apart. A catalog number such as 044 versus 078 cannot. Those strips were not used to assign a new number. Round 3 had already found the Commons photograph of Mamari illegible at catalog precision. That finding stands.

The Kohaumotu vector pages on the same mirror (`C_svg_codes_b.html` and the matching pages for G, H, P, Q, and I) trace each glyph as its own outline and print a Barthel label beside it. The outlines were used for width, height, and whether two outlines share a slot. The printed label was compared with the vendored HTML. Where the label and the HTML disagree, the outline was not given a third number.

## Calendar, Ca6–Ca9

All 28 signs coded `040` in the calendar slice are tall crescents on the vector outlines. There is one `143`, wider than those crescents, and one `152`, a closed figure rather than a crescent. The 13 / 13 split around `152`, and the gaps 2, 6, 3, 2, 5, 3, 5, are unchanged. Six full delimiters still open with `390`.

Four places were looked at harder. None became a code change.

- After `152`, the outlines of `600` and `390` share one horizontal slot and are both short. The crescent `041` is the next slot. Guy 1990 reads the stack as one sign, `*690`, and says catalog 690 is a different sign. The drawing agrees that it is one slot. It does not write Guy's number. Round 3 already recorded his proposal. It is not applied again here.
- `044.040` is a figure beside a crescent. Guy 1990 prefers `078.040`. The outline fits either figure. It was left as `044.040`.
- The two signs coded `041h` are short crescents, about a quarter to a third the height of an ordinary `041`. Horley 2011 accounts for the two small superscript crescents and does not change the number. They stay `041`.
- A narrow unnumbered path sits inside the first `378`. It is not a sign between `041` and `378`. It was not inserted.

## Gv6

All 38 stems on the line match the vendored text. Each of the six `076` outlines overlaps the sign before it and is separated by a gap from the sign after it. The drawing attaches `076` to the preceding sign. Davletshin 2012 notes that one can still read `076` as opening the next name. That is a parse of the same attachment, not a different code. The four `200 X Y.076` phrases and the three handoffs are unchanged.

## Santiago Staff

Every one of the 97 outlines coded `999` is a narrow stroke, between 2.4 and 7.6 units wide. None is a full figure. Of the 96 pure bars, 91 are still followed by a group that contains `076` (85 of those as a suffix, 3 as a bare `076`). The rate 91/96 does not change.

On a few lines the vector edition orders the pieces inside a ligature differently from the vendored colon (`021:290.076` on Ia5, `021:090.076` on Ia8 and Ia13). `076` is still in the group. A few other labels differ by a digit. Those outlines were not reassigned. Horley, Pozdniakov, and Guy do not give a replacement list for these bars in the sources already used.

The vector file numbers the Staff lines in the opposite order from Barthel's Ia1–Ia11. The comparison used Barthel's numbers.

## Great Tradition, H recto 2 / P / Q recto 2

The long parallel is still Great Santiago recto from Hr2 offset 36 through the start of Hr4, against Small St Petersburg recto from the start of Qr2 through Qr3 offset 65. Span 125, 107 matches, 16 mismatches. Nothing in that alignment was edited.

The two bird substitutions inside that stretch are still H `600` opposite Q `400`, and H `607` opposite Q `407`. Both pairs are full-height figures. The vector labels match the vendored codes, including the uncertain mark on Q's `400`. Across the whole stored parallel set the bird cross-hundred count stays 18. Guy 2006 classes series 400–409 with series 600–699 as birds. That classification was not changed.

One hand column on Hr3 offset 37 is `064` in the vendored text and on the parallel copy Q. The vector label on H is `006?`. Pozdniakov 1996 and Guy 2006 already treat 006 and 064 as alternating hands. Replacing this 064 would invent a mismatch with Q. It was left as `064`.

Two other stacked pairs (`006` with `042` on Hr3, and the same pair on Qr3) share a slot. The editions list the pieces in opposite orders. The stems are the same. Unnumbered fragments on Pr2 sit inside `202` and `306` and are not new signs.

A label `048` where the vendored text has `042`, at Hr4 offset 71, is past the end of the counted stretch. It was not adopted.

The rebus signs from Round 4 map R1 that sit in this stretch (`200`, `600`, `700`, `006`, `064`) are full figures or hands in those columns, not bars. No word was attached.

## What changed

| Count | Before this recheck | After |
| --- | ---: | ---: |
| Calendar `040` | 28 | 28 |
| `040` before / after `152` | 13 / 13 | 13 / 13 |
| Gaps between delimiters | 2, 6, 3, 2, 5, 3, 5 | 2, 6, 3, 2, 5, 3, 5 |
| Full delimiters opening `390` | 6 | 6 |
| Gv6 phrases / handoffs | 4 / 3 | 4 / 3 |
| Staff groups with `076` after a pure `999` | 91 of 96 | 91 of 96 |
| H/Q span, matches, mismatches | 125, 107, 16 | 125, 107, 16 |
| Bird substitutions in that stretch | 2 | 2 |
| Bird substitutions in the stored parallels | 18 | 18 |

The machine-readable record is `data/decipherment/round5b_ceipp_recheck.json`.
