"""Loader for ``.rrt`` Rongorongo transliteration files.

The ``.rrt`` format is a deliberately simple, line-oriented plain-text format
for transliterated corpus data. It exists so that scholarly transliterations
(in the Barthel numbering system or similar) can be dropped into ``data/corpus/``
and analyzed directly, without going through the image-based CV pipeline.

Format
------
* ``# ...``            — comment, ignored.
* ``@tablet <id>``     — start a new tablet with the given short code.
* ``@name <text>``     — common name of the current tablet (e.g. "Mamari").
* ``@side <text>``     — side label of the current tablet (e.g. "recto").
* ``@synthetic``       — mark the current tablet as synthetic (non-attested)
                         demo/test data so analysis output can flag it.
* ``<line_id>: <tokens>`` — one transliterated line. Tokens are whitespace
                         separated; a ligature is written with ``-`` between
                         component glyph codes (e.g. ``6-700``).

Blank lines are ignored. A ``<line_id>:`` line before any ``@tablet`` directive
attaches to an implicit tablet whose id is the source file stem.
"""

from pathlib import Path

from models.corpus import CorpusLine, RongorongoCorpus, Tablet


class CorpusFormatError(ValueError):
    """Raised when a ``.rrt`` file cannot be parsed."""


def parse_rrt(text: str, default_tablet_id: str = "untitled") -> list[Tablet]:
    """Parse the contents of a ``.rrt`` file into a list of tablets.

    Args:
        text: Raw file contents.
        default_tablet_id: Tablet id to use for lines that appear before any
            ``@tablet`` directive.

    Returns:
        List of parsed :class:`Tablet` objects.

    Raises:
        CorpusFormatError: If a non-comment, non-blank line is malformed.
    """
    tablets: list[Tablet] = []
    current: Tablet | None = None

    def ensure_tablet() -> Tablet:
        nonlocal current
        if current is None:
            current = Tablet(tablet_id=default_tablet_id)
            tablets.append(current)
        return current

    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("@"):
            directive, _, value = line[1:].partition(" ")
            directive = directive.lower()
            value = value.strip()
            if directive == "tablet":
                if not value:
                    raise CorpusFormatError(
                        f"line {lineno}: @tablet requires an id"
                    )
                current = Tablet(tablet_id=value)
                tablets.append(current)
            elif directive == "name":
                ensure_tablet().name = value
            elif directive == "side":
                ensure_tablet().side = value
            elif directive == "synthetic":
                ensure_tablet().is_synthetic = True
            else:
                raise CorpusFormatError(
                    f"line {lineno}: unknown directive '@{directive}'"
                )
            continue

        if ":" not in line:
            raise CorpusFormatError(
                f"line {lineno}: expected '<line_id>: <tokens>' or a "
                f"'@'/'#' directive, got: {raw!r}"
            )

        line_id, _, body = line.partition(":")
        line_id = line_id.strip()
        if not line_id:
            raise CorpusFormatError(f"line {lineno}: empty line id")
        tokens = body.split()
        ensure_tablet().lines.append(CorpusLine(line_id=line_id, tokens=tokens))

    return tablets


def load_rrt_file(path: str | Path) -> list[Tablet]:
    """Load a single ``.rrt`` file into a list of tablets."""
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CorpusFormatError(f"cannot read {path}: {exc}") from exc
    return parse_rrt(text, default_tablet_id=path.stem)


def load_corpus(paths: list[str | Path]) -> RongorongoCorpus:
    """Load and merge one or more ``.rrt`` files into a single corpus.

    Args:
        paths: ``.rrt`` file paths, or directories (scanned for ``*.rrt``).

    Returns:
        A :class:`RongorongoCorpus` containing every parsed tablet.
    """
    files: list[Path] = []
    for entry in paths:
        entry = Path(entry)
        if entry.is_dir():
            files.extend(sorted(entry.glob("*.rrt")))
        else:
            files.append(entry)

    corpus = RongorongoCorpus()
    for file in files:
        corpus.tablets.extend(load_rrt_file(file))
    return corpus
