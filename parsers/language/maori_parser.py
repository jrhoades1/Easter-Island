"""Parser for Maori dictionary data."""

from models.language import LanguageEntry

from .base import BaseLanguageParser


class MaoriDictionaryParser(BaseLanguageParser):
    """
    Parser for Maori language dictionaries.

    Primary source: maoridictionary.co.nz
    """

    source_name = "Maori Dictionary"
    source_url_pattern = "maoridictionary.co.nz"

    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the URL."""
        return "maoridictionary.co.nz" in url

    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """
        Parse Maori dictionary page.

        The maoridictionary.co.nz site uses a specific format with
        word entries containing headwords, definitions, and examples.
        """
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url)

        # Find word entries - adjust selectors based on actual site structure
        word_divs = soup.find_all("div", class_="word-entry")

        for word_div in word_divs:
            try:
                # Extract headword
                headword_elem = word_div.find("span", class_="headword")
                if not headword_elem:
                    headword_elem = word_div.find("h2")
                if not headword_elem:
                    continue

                word = self.clean_text(headword_elem.get_text())
                if not word:
                    continue

                # Extract definitions
                translations = []
                def_elems = word_div.find_all("span", class_="definition")
                if not def_elems:
                    def_elems = word_div.find_all("p", class_="def")

                for def_elem in def_elems:
                    text = self.clean_text(def_elem.get_text())
                    if text:
                        translations.append(self.create_translation(text))

                # Extract part of speech if available
                pos_elem = word_div.find("span", class_="pos")
                pos = self.clean_text(pos_elem.get_text()) if pos_elem else None

                # Extract examples if available
                examples = []
                example_elems = word_div.find_all("div", class_="example")
                for ex_elem in example_elems:
                    maori_text = ex_elem.find("span", class_="maori")
                    eng_text = ex_elem.find("span", class_="english")
                    if maori_text and eng_text:
                        examples.append(
                            self.create_example(
                                self.clean_text(maori_text.get_text()),
                                self.clean_text(eng_text.get_text()),
                            )
                        )

                if translations:
                    entries.append(
                        LanguageEntry(
                            word=word,
                            translations=translations,
                            part_of_speech=pos,
                            examples=examples,
                            metadata=metadata,
                        )
                    )

            except Exception:
                continue

        return entries

    def parse_search_results(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse search results page."""
        soup = self.get_soup(html)
        entries = []
        metadata = self.create_metadata(url, confidence="low")

        # Search results typically show abbreviated entries
        result_items = soup.find_all("li", class_="search-result")

        for item in result_items:
            try:
                link = item.find("a")
                if not link:
                    continue

                word = self.clean_text(link.get_text())
                preview = item.find("span", class_="preview")
                meaning = self.clean_text(preview.get_text()) if preview else ""

                if word and meaning:
                    entries.append(
                        LanguageEntry(
                            word=word,
                            translations=[self.create_translation(meaning)],
                            metadata=metadata,
                        )
                    )

            except Exception:
                continue

        return entries
