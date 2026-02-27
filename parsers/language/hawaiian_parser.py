"""Parser for Hawaiian dictionary data."""

from models.language import LanguageEntry

from .base import BaseLanguageParser


class HawaiianDictionaryParser(BaseLanguageParser):
    """
    Parser for Hawaiian language dictionaries.

    Primary source: wehewehe.org (Ulukau Hawaiian Dictionary)
    """

    source_name = "Hawaiian Dictionary"
    source_url_pattern = "wehewehe.org"

    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the URL."""
        return "wehewehe.org" in url or "ulukau.org" in url

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """
        Parse Hawaiian dictionary page.

        The wehewehe.org site displays entries from multiple Hawaiian
        dictionaries including Pukui-Elbert and Māmaka Kaiao.
        """
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url)

        # Find dictionary entries
        entry_divs = soup.find_all("div", class_="entry")
        if not entry_divs:
            entry_divs = soup.find_all("div", class_="dicentry")

        for entry_div in entry_divs:
            try:
                # Extract headword
                headword_elem = entry_div.find("span", class_="hw")
                if not headword_elem:
                    headword_elem = entry_div.find("b")
                if not headword_elem:
                    continue

                word = self.clean_text(headword_elem.get_text())
                if not word:
                    continue

                # Remove stress marks for matching purposes
                word_normalized = word.replace("ʻ", "'").replace("ā", "a").replace("ē", "e")
                word_normalized = word_normalized.replace("ī", "i").replace("ō", "o").replace("ū", "u")

                # Extract definitions
                translations = []
                def_elem = entry_div.find("span", class_="def")
                if not def_elem:
                    def_elem = entry_div.find("span", class_="definition")

                if def_elem:
                    text = self.clean_text(def_elem.get_text())
                    if text:
                        # Split multiple definitions
                        for defn in text.split(";"):
                            defn = defn.strip()
                            if defn:
                                translations.append(self.create_translation(defn))

                # Extract part of speech
                pos_elem = entry_div.find("span", class_="pos")
                pos = None
                if pos_elem:
                    pos_text = self.clean_text(pos_elem.get_text())
                    pos = self._normalize_pos(pos_text)

                # Extract source dictionary
                source_elem = entry_div.find("span", class_="source")
                source_dict = None
                if source_elem:
                    source_dict = self.clean_text(source_elem.get_text())

                # Extract examples
                examples = []
                ex_elems = entry_div.find_all("span", class_="ex")
                for ex_elem in ex_elems:
                    hawaiian = ex_elem.find("span", class_="haw")
                    english = ex_elem.find("span", class_="eng")
                    if hawaiian and english:
                        examples.append(
                            self.create_example(
                                self.clean_text(hawaiian.get_text()),
                                self.clean_text(english.get_text()),
                                source_dict,
                            )
                        )

                if translations:
                    entry = LanguageEntry(
                        word=word,
                        translations=translations,
                        part_of_speech=pos,
                        examples=examples,
                        metadata=metadata,
                    )
                    entries.append(entry)

            except Exception:
                continue

        return entries

    def _normalize_pos(self, pos_text: str) -> str:
        """Normalize part of speech abbreviations."""
        pos_map = {
            "n.": "noun",
            "v.": "verb",
            "vi.": "verb.intransitive",
            "vt.": "verb.transitive",
            "adj.": "adjective",
            "adv.": "adverb",
            "num.": "numeral",
            "prep.": "preposition",
            "conj.": "conjunction",
            "interj.": "interjection",
            "pron.": "pronoun",
        }

        pos_lower = pos_text.lower().strip()
        return pos_map.get(pos_lower, pos_text)

    def parse_word_lookup(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse a single word lookup result."""
        soup = self.get_soup(html)
        entries = []

        # The lookup page may show results from multiple dictionaries
        dict_sections = soup.find_all("div", class_="dictionary-section")

        for section in dict_sections:
            section_entries = self.parse(str(section), url)
            entries.extend(section_entries)

        return entries
