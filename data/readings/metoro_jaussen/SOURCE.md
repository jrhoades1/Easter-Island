# Metoro's readings for Jaussen

## What was recorded

In the 1870s Bishop Florentin Étienne Jaussen ("Tepano") had Metoro Tauʻa Ure chant tablets and wrote a word or phrase against each sign, separated by hyphens. Jaussen died in 1891. The notebook wording is public domain.

Jaussen's 1893 book (*L'île de Pâques: historique, écriture, et répertoire des signes…*, Paris) is a sign list, not the line-by-line chant. The line-by-line text used here is Kohaumotu's transcription of the notebooks:

- Index: http://kohaumotu.org/rongorongo_org/metoro/index.html
- Layout: http://kohaumotu.org/rongorongo_org/metoro/layout.html
- One HTML file per line in `lines/` (retrieved 2026-09-27)

Kohaumotu's layout note, which this parser follows: italics are Jaussen's comments; `[p.94]` is his page number; each group ending in a hyphen is one sign. The hyphen is printed as `<SUP>__</SUP>`. Every fifth group is numbered `=01=`, `=05=`, and so on. Those numbers are locators, not signs.

Site notice (http://kohaumotu.org/rongorongo_org/copy.html): copy is allowed if the source is acknowledged and the use is non-profit. These HTML files are not covered by this repository's MIT license.

Barthel's *Grundlagen zur Entzifferung der Osterinselschrift* (1958) and Fischer's *Rongorongo: The Easter Island Script* (1997) also print Metoro. Those books are not reproduced here. Pairing uses the Barthel codes already vendored from Kohaumotu HTML under `tests/fixtures/`.

## Tablets

Kohaumotu's index gives four tablets, which are the ones Jaussen had Metoro read:

| Tablet | Barthel lines with a Metoro page | Vendored Barthel |
| --- | --- | --- |
| B Aruku Kurenga | Br1–Br10, Bv1–Bv12 | `aruku_br_html`, `aruku_bv_html` |
| A Tahua | Ab1–Ab8, Aa1–Aa8 (side b is printed before side a) | `tahua_ab_html`, `tahua_aa_html` |
| C Mamari | Cb1–Cb14, then Ca14 back to Ca1 | `mamari_cb_html`, `mamari_ca_html` |
| E Keiti | Er1–Er9, Ev1–Ev8 | `keiti_er_html`, `keiti_ev_html` |

On Tahua, the Ab1 page says the chant was still being written out in full. On Mamari Cb1, Jaussen writes that the chant is no longer complete and that, with a finger on the sign, he tried to write only the essential word, and that he did the same for the last tablet (Keiti). A line whose word-groups do not equal the vendored Barthel tokens is left unpaired. This track does not invent a sign alignment to force them together.

Guy's argument that Metoro read the verso of Keiti back to front is a secondary claim (Kohaumotu `metoro/guy.html`). The primary test pairs a line only in the order the groups are printed. A reverse pairing is reported separately and is still a hypothesis about order, not a meaning.
