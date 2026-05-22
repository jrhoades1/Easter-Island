# Rongorongo Corpus Data

This directory holds **transliterated** Rongorongo corpus data — tablets
already encoded by scholars as sequences of glyph codes. It is the input to
`corpus_stats.py` and the statistical-analysis pipeline.

> The only file shipped here is `sample_synthetic.rrt`, which contains
> **invented, non-attested data** for pipeline testing. It is marked
> `@synthetic` so every analysis run flags it. Do not draw research
> conclusions from it.

## Why transliterations, not images

The image-based computer-vision pipeline (`glyph_cataloger.py`) re-derives a
glyph catalog from scratch, which is error-prone and duplicates work that
Rongorongo scholars have already done carefully by hand. The statistical layer
instead consumes existing scholarly transliterations directly, so the analysis
rests on the field's accepted glyph readings rather than on CV guesses.

## Obtaining a real corpus

Rongorongo has ~26 surviving inscribed objects. Several scholarly resources
publish transliterations in standardized glyph-numbering systems:

- **Barthel numbering system** — Barthel, T.S. (1958), *Grundlagen zur
  Entzifferung der Osterinselschrift*. The ~600-sign catalog and the
  three-letter line references (e.g. `Ca7` = tablet C, side a, line 7) used by
  most later work.
- **CEIPP** (Centre d'Études sur l'Île de Pâques et la Polynésie) — maintains
  a reference corpus and photographic documentation.
- **Pozdniakov, K. (1996)**, "Les bases du déchiffrement de l'écriture de
  l'île de Pâques", *Journal de la Société des Océanistes* — statistical
  analysis and a machine-readable encoding of the corpus.
- **Horley, P.** — published tablet-by-tablet transliterations and corrections
  in the *Rapa Nui Journal*.

Check the licence/terms of any source before committing its data to this
repository. Transliterations are scholarly work product.

## File format (`.rrt`)

Plain UTF-8 text, line-oriented. See `processors/corpus_loader.py` for the
authoritative parser.

```
# comment line, ignored
@tablet C            # start a tablet, short code "C"
@name Mamari         # common name (optional)
@side recto          # side label (optional)
@synthetic           # mark tablet as non-attested test data (optional)
Ca1: 1 2 6 700 8     # a line: "<line_id>: <space-separated glyph tokens>"
Ca2: 6-700 8 1 2     # "6-700" is a ligature (fused glyphs 6 and 700)
```

- Glyph **tokens** are whitespace-separated and kept as opaque strings, so any
  numbering system works (Barthel integers, variant suffixes like `6a`, etc.).
- A **ligature** is written with `-` between component codes. Statistics
  decompose ligatures into their component glyphs for frequency counts, and
  also report how many tokens were ligatures.
- `line_id` is free-form; the Barthel `<tablet><side><line>` convention
  (e.g. `Ca7`) is recommended so output is easy to cross-check.
