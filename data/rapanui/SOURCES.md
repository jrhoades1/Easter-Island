# Rapanui comparison corpus

Sequence statistics in Track 2 use running text. Isolated word lists are stored
here so the orthography is documented, and they are not concatenated into the
running-text bigrams.

## Thomson 1891 (public domain)

- File: `thomson_1891_chants.txt`
- Work: William J. Thomson, "Te Pito te Henua, or Easter Island," *Report of the
  U.S. National Museum for the year ending June 30, 1889* (Washington, 1891),
  pp. 517–526.
- Status: published 1891 as a United States government report. Public domain.
- Digital image used only to copy the Rapanui lines: Internet Archive
  identifier `cu31924105726222`, file `cu31924105726222_djvu.txt`.
- What was copied: the Rapanui lines of Apai, Atua Matariri, Eaha to ran ariiki
  kete, and Ka ihi uiga, plus the short "love song." English translations,
  plate captions, and page headers were not copied. End-of-line hyphenation in
  the print was rejoined when the next line continues in lowercase
  (`kapi-` / `piri` → `kapipiri`). Mid-line hyphens such as `moko-moko` were
  left in place.
- Known limits: the print is a poor record of the recitation (Salmon's
  transcription, then a typeset report). Spellings are inconsistent and some
  letters are not Rapanui phonemes. The love song contains Tahitian loans
  (`forani`, `moni`, `fahiti`); Track 2 leaves it in the file and leaves it
  out of the primary sequence (`include_love_song=False`).
- Not copied: the two-column English–Rapanui vocabulary (pp. 546–552). The
  Internet Archive OCR interleaves the columns, so a mechanical parse would
  mix English glosses into the Rapanui sample.

### Lexicon examples from the same report

- File: `thomson_1891_lexicon_examples.txt`
- Source: Thomson 1891, pp. 546–547, the prose discussion of reduplication and
  a few kinship and month-day examples. Each line is one cited word or short
  phrase, not a sentence of running text.
- Track 2 does not insert these into the chant sequences.

## English Wikipedia (CC BY-SA 4.0)

- File: `wikipedia_rap_spans.txt`
- Source already vendored at `tests/fixtures/wikipedia_rapa_nui.html`
  (article "Rapa Nui language," revision id 1333689608 in that snapshot).
- License: Creative Commons Attribution-ShareAlike 4.0. The snapshot's
  canonical link is `https://en.wikipedia.org/wiki/Rapa_Nui_language`.
- What was copied: text nodes inside elements with `lang="rap"`. Template
  spans that contain `+`, `/`, parentheses, or digits were dropped (paradigms
  such as `tau/tou/tū` and `he + maꞌeha`). Spanish punctuation around a span
  was stripped.
- Use: modern-orthography syllable check. These spans are mostly dictionary
  examples and short phrases, so Track 2 does not pool them with Thomson when
  it estimates conditional entropy of running text.
- Phonology reference used as a ceiling, not as a word list: the same article's
  Phonology section says Rapa Nui has ten consonants and five vowels. Track 2
  treats a fully crossed (C)V inventory as 10×5 + 5 = 55 syllables. That
  ceiling is an assumption (every consonant with every vowel, plus bare
  vowels), not a count Wikipedia prints.

## Crib headwords (Round 2 Track B only)

- File: `crib_headwords.txt`
- What it is: the closed list of moon-night and kinship words the anchor crib
  is allowed to spell. It is not running text, and Track 2 does not read it.
- Night names: the short aligned list already printed in
  `docs/decipherment/track1_mamari_calendar.md` (Thomson 1891 p. 546,
  Métraux 1940 p. 50, Englert 1948 pp. 311–312). That list is proper names
  already in this repository. Englert's dictionary is still not copied.
- Other rows cite a vendored Thomson line, a Wikipedia `lang=rap` span, or
  one Metoro word-token already under `data/readings/metoro_jaussen/`.
  Metoro's words are vocabulary only. Track 4 found they do not label
  Barthel signs.
- William Churchill, *Easter Island: The Rapanui Speech and the Peopling of
  Southeast Polynesia* (Carnegie Institution of Washington, Publication 174,
  1912) is a public-domain book. It is not vendored here, and no headword
  was copied from it.
- Jordi Fuentes, *Diccionario y gramática de la lengua de la Isla de Pascua*
  (Santiago, 1960) is not used. This repository does not treat it as a
  public-domain source.

## Not used

- Sebastian Englert's dictionary and grammar. Englert died in 1969; Chilean
  copyright runs for 70 years after death, so those books were not copied.
  The night-name spellings in `crib_headwords.txt` are the short list already
  aligned in the Track 1 note, not entries transcribed from the dictionary.
- A Rapa Nui Bible. No public-domain edition was identified. Modern Bible
  translations are copyrighted and were not copied.
- Omniglot and Glosbe pages already under `tests/fixtures/`. Those sites were
  not treated as a source for running text.

## Syllable encoding

See `decipherment/rapanui.py`. Two switchable orthographies:

- `strict`: keep a word only if every letter is a Rapanui vowel
  (`a e i o u`, including macrons collapsed to one vowel), consonant
  (`h k m n p r t v`), `ng` / `ŋ`, or a glottal mark (`' ʻ ʼ ꞌ ʔ`).
- `mapped`: Thomson-oriented letter substitution applied before that filter:
  `b→p`, `d→t`, `f→h`, `l→r`, `w→v`, `c→k`, `j→h`, `q→k`, `y→i`, `g→ŋ`
  (after `ng` is read as one consonant), and `s` and `x` deleted. This is an
  analysis choice for 19th-century spelling, not a claim about Thomson's
  phonetics.

Primary running text is Thomson with the love song excluded. The orthography
is `strict` when that sample still has at least 1,500 syllables, and `mapped`
otherwise.
