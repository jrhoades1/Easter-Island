"""Lock Track 2 syllabary-test numbers. No invented readings."""

from __future__ import annotations

from pathlib import Path

import pytest

from agents.base.providers import MockProvider
from decipherment.inventories import (
    POZDNIAKOV_52_LABELS,
    encode_lines,
    encode_token,
    pozdniakov_barthel_stems,
)
from decipherment.rapanui import is_full_reduplication, syllabify_word
from decipherment.report import render_report
from decipherment.track2 import run_track2
from tests.test_mamari_calendar_scoreboard import barthel_stems, load_mamari_fixture
from tests.test_mamari_second_passage_scoreboard import published_stems
from tests.test_mamari_small_london_kr_scoreboard import (
    KR_LINE_NAMES,
    STANDING_STEM_COUNTS,
    STANDING_STEM_TOTAL,
    extract_kr_published_tokens,
    load_vendored_kr_html,
)

DOCS = Path(__file__).resolve().parents[1] / "docs" / "decipherment"
REPORT = DOCS / "track2_syllabary_test.md"


@pytest.fixture(scope="module")
def track2_run():
    provider = MockProvider()
    return provider, run_track2(provider)


def test_syllabifier_cv_and_reduplication():
    assert syllabify_word("tangata", "strict") == ["ta", "nga", "ta"]
    assert syllabify_word("rongorongo", "strict") == ["ro", "ngo", "ro", "ngo"]
    assert syllabify_word("ika", "strict") == ["i", "ka"]
    assert syllabify_word("te", "strict") == ["te"]
    ruku = syllabify_word("ruku-ruku", "strict")
    assert ruku == ["ru", "ku", "ru", "ku"]
    assert is_full_reduplication(ruku)


def test_pozdniakov_membership_is_not_a_merge_table():
    assert len(POZDNIAKOV_52_LABELS) == 52
    assert "27a" in POZDNIAKOV_52_LABELS
    assert "901" in POZDNIAKOV_52_LABELS
    stems = pozdniakov_barthel_stems()
    assert len(stems) == 51
    assert "027" in stems
    assert "901" not in stems


def test_calendar_stems_match_scoreboard_stemmer():
    data = load_mamari_fixture()
    total = 0
    for tokens in data["lines"].values():
        expected = barthel_stems(tokens)
        got = [
            sign for token in tokens for sign in encode_token(token, "stem", drop_illegible=False)
        ]
        assert got == expected
        total += len(got)
    assert total == 101


def test_kr_illegible_drop_matches_scoreboard_when_kept():
    published = extract_kr_published_tokens(load_vendored_kr_html())
    kept = []
    dropped = []
    for name in KR_LINE_NAMES:
        tokens = published[name]
        expected = published_stems(tokens)
        got = [
            sign for token in tokens for sign in encode_token(token, "stem", drop_illegible=False)
        ]
        assert got == expected
        kept.append(len(got))
        dropped.append(
            len(
                [
                    sign
                    for token in tokens
                    for sign in encode_token(token, "stem", drop_illegible=True)
                ]
            )
        )
    assert tuple(kept) == STANDING_STEM_COUNTS
    assert sum(kept) == STANDING_STEM_TOTAL == 131
    assert tuple(dropped) == (18, 29, 29, 24, 21)
    assert sum(dropped) == 121


def test_mock_provider_only():
    provider = MockProvider()
    result = run_track2(provider)
    assert provider.get_call_history() == []
    assert result["provider_calls"] == 0
    assert result["provider"] == "mock"
    with pytest.raises(TypeError, match="MockProvider only"):
        run_track2(object())  # type: ignore[arg-type]


def test_locked_corpus_and_verdict(track2_run):
    _provider, result = track2_run
    assert result["provider_calls"] == 0
    assert result["side_count"] == 37
    assert [side["side"] for side in result["sides"]] == [
        "Aa",
        "Ab",
        "Br",
        "Bv",
        "Ca",
        "Cb",
        "Da",
        "Db",
        "Er",
        "Ev",
        "Fa",
        "Fb",
        "Gr",
        "Gv",
        "Hr",
        "Hv",
        "Ia",
        "Ja",
        "Kr",
        "Kv",
        "La",
        "Ma",
        "Na",
        "Nb",
        "Oa",
        "Pr",
        "Pv",
        "Qr",
        "Qv",
        "Ra",
        "Rb",
        "Sa",
        "Sb",
        "Ta",
        "Ua",
        "Va",
        "Wa",
    ]
    kr = next(side for side in result["sides"] if side["side"] == "Kr")
    assert kr["stem_tokens"] == 121
    assert kr["raw_tokens"] == 92
    assert result["illegible_stems_dropped"] == 353
    assert result["stem"]["tokens"] == 14488
    assert result["stem"]["inventory"] == 630
    assert result["stem"]["hapax"] == 170
    assert result["surface"]["inventory"] == 1582
    assert result["ligature_atomic"]["inventory"] == 2210
    assert result["stem"]["heaps_at"] == {
        "100": 54,
        "250": 113,
        "500": 161,
        "1000": 232,
        "2000": 301,
        "4000": 416,
        "8000": 537,
    }
    assert result["syllables"]["heaps_at"]["100"] == 26
    assert result["syllables"]["heaps_at"]["250"] == 39
    assert result["syllables"]["heaps_at"]["500"] == 43
    assert result["syllables"]["heaps_at"]["1000"] == 44
    assert result["syllables"]["heaps_at"]["2000"] == 49
    assert result["syllables"]["inventory"] == 49
    assert result["syllables"]["tokens"] == 3400
    assert result["words"]["tokens"] == 1591
    assert result["words"]["inventory"] == 633
    assert result["primary_rapanui"] == {
        "name": "thomson_strict",
        "orthography": "strict",
        "words": 1591,
        "syllables": 3400,
        "words_rejected": 54,
        "sections": 4,
    }
    assert result["thomson_strict_syllables"] == 3400
    assert result["thomson_mapped_syllables"] == 3579
    assert result["thomson_mapped_inventory"] == 49
    assert result["wikipedia_strict_syllables"] == 454
    assert result["wikipedia_strict_inventory"] == 45
    assert result["pozdniakov_label_count"] == 52
    assert result["pozdniakov_barthel_stem_count"] == 51
    assert result["pozdniakov_52"]["inventory"] == 52
    assert result["pozdniakov_52"]["coverage_of_stem_tokens"] == pytest.approx(0.5320955273329652)
    assert result["frequency_core_52"]["inventory"] == 53
    assert result["frequency_core_52"]["coverage_of_stem_tokens"] == pytest.approx(
        0.6490889011595803
    )
    assert result["hand_allograph_6_64"]["tokens_064"] == 130
    assert result["hand_allograph_6_64"]["tokens_006"] == 337
    assert result["hand_allograph_6_64"]["inventory_after_merge"] == 629
    assert result["duplicate_stem_lines"] == 0
    assert result["deduped_verdict"] == "mixed"
    verdict = result["verdict"]
    assert verdict["label"] == "mixed"
    assert verdict["structure_index"] == pytest.approx(0.0980487972445141)
    assert verdict["relative_h2_laplace"] > 0.90
    assert verdict["n_matched_syllables"] == 3400
    assert verdict["inventory_stem_at_syllable_n"] == 394
    assert verdict["inventory_syllables_at_n"] == 49
    assert verdict["ratio_stem_to_syllables"] == pytest.approx(8.040816326530612)
    assert verdict["n_matched_words"] == 1591
    assert verdict["inventory_stem_at_word_n"] == 273
    assert verdict["inventory_words_at_n"] == 633
    assert verdict["ratio_stem_to_words"] == pytest.approx(0.4312796208530806)
    assert result["stem"]["heaps_beta"] == pytest.approx(0.42161851372627307)
    assert result["syllables"]["heaps_beta"] == pytest.approx(0.14158560519433736)
    assert result["words"]["heaps_beta"] == pytest.approx(0.8132074367201261)
    assert result["stem"]["h2_conditional_mle"] == pytest.approx(4.887533261229475)
    assert result["shuffle"]["h2_conditional_mle"] == pytest.approx(5.418844441138196)
    assert result["rigid"]["h2_conditional_mle"] == 0.0
    assert result["stem"]["repetition"]["xx_rate"] == pytest.approx(0.03236929139399057)
    assert result["syllables"]["repetition"]["xx_rate"] == pytest.approx(0.029740871613663133)
    assert result["stem"]["zipf_r2"] == pytest.approx(0.9346136348838254)
    assert result["syllables"]["zipf_r2"] == pytest.approx(0.6952351411054782)
    assert result["syllable_structure_index"] == pytest.approx(0.14430821476417877)
    assert result["word_structure_index"] == pytest.approx(0.343002765519282)
    assert result["stem"]["position"]["frequent_in_all_three_rate"] == pytest.approx(
        0.3160621761658031
    )
    assert result["syllable_word_edges"]["frequent_in_all_three_rate"] == pytest.approx(
        0.9302325581395349
    )
    reduplication = result["word_reduplication"]
    assert reduplication["parsed_words"] == 1536
    assert reduplication["full_reduplications"] == 37
    assert reduplication["rate"] == pytest.approx(0.024088541666666668)
    assert result["top_stems"][:8] == [
        {"sign": "001", "count": 769},
        {"sign": "076", "count": 682},
        {"sign": "002", "count": 442},
        {"sign": "003", "count": 432},
        {"sign": "004", "count": 422},
        {"sign": "600", "count": 342},
        {"sign": "006", "count": 337},
        {"sign": "022", "count": 316},
    ]
    assert result["top_syllables"][:8] == [
        {"syllable": "a", "count": 384},
        {"syllable": "i", "count": 293},
        {"syllable": "te", "count": 193},
        {"syllable": "ta", "count": 182},
        {"syllable": "ra", "count": 171},
        {"syllable": "ki", "count": 165},
        {"syllable": "e", "count": 156},
        {"syllable": "ka", "count": 150},
    ]


def test_alignment_is_a_hypothesis_not_a_reading(track2_run):
    _provider, result = track2_run
    alignment = result["alignment"]
    assert alignment["adopted"] is False
    assert alignment["reading"] is None
    assert alignment["hypothesis_only"] is True
    assert "gloss" not in alignment
    assert alignment["cosine"] == pytest.approx(0.4040075981907491)
    assert alignment["cosine_null_ge_fraction"] == 0.0
    assert alignment["repetition_spearman"] == pytest.approx(0.26163589993478037)
    assert alignment["repetition_null_ge_fraction"] == pytest.approx(0.12)
    assert alignment["k"] == 30
    assert alignment["permutations"] == 200
    for pair in alignment["pairs"]:
        assert set(pair) == {"sign", "syllable", "rank"}


def test_report_matches_result_and_states_the_verdict(track2_run):
    _provider, result = track2_run
    text = render_report(result)
    assert REPORT.read_text(encoding="utf-8") == text
    assert "not a decipherment" in text
    assert "**Verdict: mixed.**" in text
    assert "larger than a Rapanui syllabary" in text
    assert "It is not proposed." in text
    assert "`reading` is None" in text
    for name in ("heaps.svg", "zipf.svg", "entropy.svg"):
        figure = DOCS / "figures" / name
        assert figure.is_file()
        assert figure.read_text(encoding="utf-8").startswith("<svg")
    assert encode_lines([["001", "999"]], "pozdniakov_52") == [["001", "RES"]]
