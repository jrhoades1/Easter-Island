"""Parser for Tahitian dictionary data."""

from models.language import LanguageEntry

from .base import BaseLanguageParser


class TahitianDictionaryParser(BaseLanguageParser):
    """
    Parser for Tahitian language dictionaries.

    Primary source: farevanaa.pf (Académie Tahitienne)
    """

    source_name = "Tahitian Dictionary"
    source_url_pattern = "farevanaa.pf"

    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the URL."""
        return (
            "farevanaa.pf" in url
            or "lexique-tahitien" in url
            or "tahitiandictionary" in url
        )

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """
        Parse Tahitian dictionary page.

        The farevanaa.pf site is the official Académie Tahitienne
        dictionary with detailed linguistic information.
        """
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url)

        # Find word entries
        entry_divs = soup.find_all("div", class_="entry")
        if not entry_divs:
            entry_divs = soup.find_all("article", class_="word")
        if not entry_divs:
            entry_divs = soup.find_all("tr", class_="dict-entry")

        for entry_div in entry_divs:
            try:
                # Extract headword
                headword_elem = entry_div.find("span", class_="headword")
                if not headword_elem:
                    headword_elem = entry_div.find("td", class_="word")
                if not headword_elem:
                    headword_elem = entry_div.find("strong")
                if not headword_elem:
                    continue

                word = self.clean_text(headword_elem.get_text())
                if not word:
                    continue

                # Handle glottal stop variations
                # Tahitian uses ʻ (okina) for glottal stop
                word = word.replace("'", "ʻ")

                # Extract translations/definitions
                translations = []

                # French definition (Tahitian dictionaries often use French)
                fr_def = entry_div.find("span", class_="def-fr")
                if fr_def:
                    text = self.clean_text(fr_def.get_text())
                    if text:
                        translations.append(
                            self.create_translation(text, language="fr")
                        )

                # English definition if available
                en_def = entry_div.find("span", class_="def-en")
                if en_def:
                    text = self.clean_text(en_def.get_text())
                    if text:
                        translations.append(self.create_translation(text))

                # Generic definition field
                def_elem = entry_div.find("td", class_="definition")
                if not def_elem:
                    def_elem = entry_div.find("span", class_="meaning")
                if def_elem and not translations:
                    text = self.clean_text(def_elem.get_text())
                    if text:
                        # Detect language - French uses more accents
                        lang = "fr" if any(c in text for c in "éèêëàâùûîïôœæç") else "en"
                        translations.append(
                            self.create_translation(text, language=lang)
                        )

                # Extract part of speech
                pos_elem = entry_div.find("span", class_="pos")
                if not pos_elem:
                    pos_elem = entry_div.find("abbr", class_="grammatical")
                pos = None
                if pos_elem:
                    pos = self._normalize_pos(self.clean_text(pos_elem.get_text()))

                # Extract examples
                examples = []
                ex_divs = entry_div.find_all("div", class_="example")
                for ex_div in ex_divs:
                    tah_text = ex_div.find("span", class_="tahitian")
                    trans_text = ex_div.find("span", class_="translation")
                    if tah_text and trans_text:
                        examples.append(
                            self.create_example(
                                self.clean_text(tah_text.get_text()),
                                self.clean_text(trans_text.get_text()),
                            )
                        )

                # Extract etymology if available
                etym_elem = entry_div.find("span", class_="etymology")
                etymology = None
                if etym_elem:
                    etymology = self.clean_text(etym_elem.get_text())

                if translations:
                    entry = LanguageEntry(
                        word=word,
                        translations=translations,
                        part_of_speech=pos,
                        examples=examples,
                        etymology=etymology,
                        metadata=metadata,
                    )
                    entries.append(entry)

            except Exception:
                continue

        return entries

    def _normalize_pos(self, pos_text: str) -> str:
        """Normalize part of speech (handles French abbreviations)."""
        pos_map = {
            # French abbreviations
            "n.": "noun",
            "v.": "verb",
            "adj.": "adjective",
            "adv.": "adverb",
            "num.": "numeral",
            "prép.": "preposition",
            "conj.": "conjunction",
            "interj.": "interjection",
            "pron.": "pronoun",
            # Tahitian-specific
            "v.i.": "verb.intransitive",
            "v.t.": "verb.transitive",
            "v.a.": "verb.active",
            "n.m.": "noun.masculine",
            "n.f.": "noun.feminine",
        }

        pos_lower = pos_text.lower().strip()
        return pos_map.get(pos_lower, pos_text)

    def parse_word_list(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse a word list page (index or search results)."""
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url, confidence="low")

        # Word list items
        list_items = soup.find_all("li", class_="word-item")
        if not list_items:
            list_items = soup.find_all("a", class_="word-link")

        for item in list_items:
            try:
                if item.name == "a":
                    word = self.clean_text(item.get_text())
                else:
                    link = item.find("a")
                    word = self.clean_text(link.get_text()) if link else ""

                # Get preview definition if available
                preview = item.find("span", class_="preview")
                meaning = self.clean_text(preview.get_text()) if preview else ""

                if word:
                    translations = (
                        [self.create_translation(meaning)] if meaning else []
                    )
                    entries.append(
                        LanguageEntry(
                            word=word,
                            translations=translations,
                            metadata=metadata,
                        )
                    )

            except Exception:
                continue

        return entries
