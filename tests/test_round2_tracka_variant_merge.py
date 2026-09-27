"""Lock Round 2 Track A allograph merges. No invented readings."""

from __future__ import annotations

from pathlib import Path

import pytest

from agents.base.providers import MockProvider
from decipherment.allographs import MERGE_RULES, encode_scheme_token, rules_for
from decipherment.round2_tracka import (
    EARLY_INVENTORY_MIN,
    HEAPS_BETA_MAX,
    SYLLABARY_TYPE_MAX,
    SYLLABARY_TYPE_MIN,
    positional_alignment,
    render_round2_tracka,
    run_round2_tracka,
)

DOCS = Path(__file__).resolve().parents[1] / "docs" / "decipherment"
REPORT = DOCS / "round2_trackA_variant_merge.md"
FIGURE = DOCS / "figures" / "round2_trackA_heaps.svg"


@pytest.fixture(scope="module")
def tracka_run():
    provider = MockProvider()
    return provider, run_round2_tracka(provider)


def test_ligature_split_examples():
    assert encode_scheme_token("606.076", "pozdniakov_2007") == ["606", "076"]
    assert encode_scheme_token("999.440.076", "barthel_families") == ["999", "440", "076"]
    assert encode_scheme_token("999.440.076", "horley_2005") == ["999", "660", "076"]
    assert encode_scheme_token("606.076", "horley_2005", decompose_ligatures=False) == ["606.076"]
    assert encode_scheme_token("049.076", "horley_2005", decompose_ligatures=False) == ["048.076"]


def test_barthel_affixes_and_uncertain_catalog_examples():
    assert encode_scheme_token("200f", "barthel_suffix_only") == ["200"]
    assert encode_scheme_token("040a", "barthel_suffix_only") == ["040a"]
    assert encode_scheme_token("040a", "pozdniakov_2007") == ["040"]
    assert encode_scheme_token("200i", "barthel_families") == ["200i"]
    assert encode_scheme_token("545", "barthel_suffix_only") == ["545"]
    assert encode_scheme_token("545", "barthel_families") == ["039"]
    assert encode_scheme_token("160b", "barthel_families") == ["160a"]
    assert encode_scheme_token("380", "barthel_families") == ["370"]
    assert encode_scheme_token("200", "barthel_families") == ["200"]
    assert encode_scheme_token("600", "barthel_families") == ["600"]
    assert encode_scheme_token("042", "barthel_families") == ["042"]


def test_pozdniakov_published_merges_leave_the_rest_in_place():
    assert encode_scheme_token("064", "pozdniakov_2007") == ["006"]
    assert encode_scheme_token("004.064", "pozdniakov_2007") == ["004", "006"]
    assert encode_scheme_token("004", "pozdniakov_2007") == ["004"]
    assert encode_scheme_token("304", "pozdniakov_2007") == ["306"]
    assert encode_scheme_token("380", "pozdniakov_2007") == ["380"]
    assert encode_scheme_token("400", "pozdniakov_2007") == ["400"]
    assert encode_scheme_token("304", "pozdniakov_1996_gaping_mouth") == ["606"]
    assert encode_scheme_token("380", "pozdniakov_1996_gaping_mouth") == ["680"]
    assert encode_scheme_token("027a", "pozdniakov_2007") == ["027a"]
    assert encode_scheme_token("027b", "pozdniakov_2007") == ["027b"]
    assert encode_scheme_token("027x", "pozdniakov_2007") == ["027b"]
    assert encode_scheme_token("027", "pozdniakov_2007") == ["027"]
    assert encode_scheme_token("099", "pozdniakov_2007") == ["099"]
    assert encode_scheme_token("095.014", "pozdniakov_2007") == ["095", "014"]
    assert encode_scheme_token("999", "pozdniakov_2007") == ["999"]
    assert "RES" not in encode_scheme_token("530", "pozdniakov_2007")


def test_horley_rules_do_not_renumber_hands_as_030():
    assert encode_scheme_token("280", "horley_2005") == ["070", "002"]
    assert encode_scheme_token("280", "horley_2005", decompose_ligatures=False) == ["280"]
    assert encode_scheme_token("386", "horley_2005") == ["073", "006"]
    assert encode_scheme_token("049", "horley_2005") == ["048"]
    assert encode_scheme_token("060", "horley_2005") == ["060"]
    assert encode_scheme_token("030", "horley_2005") == ["030"]
    assert encode_scheme_token("208", "horley_2005") == ["200"]
    assert encode_scheme_token("530", "horley_2005") == ["005"]


def test_every_rule_is_cited_and_uncertain_ones_are_flagged():
    seen = set()
    for rule in MERGE_RULES:
        assert rule.rule_id not in seen
        seen.add(rule.rule_id)
        assert rule.citation
        assert any(character.isdigit() for character in rule.citation)
        assert rule.statement
        assert rule.schemes
    uncertain = {rule.rule_id for rule in MERGE_RULES if rule.uncertain}
    assert "guy_catalog_corrections" in uncertain
    assert "hand_digit_4_to_6" in uncertain
    assert "gaping_mouth_to_bird" in uncertain
    assert "horley_one_to_one" in uncertain
    assert "horley_expansions" in uncertain
    assert "hand_6_and_64" not in uncertain
    assert "barthel_modification_affixes" not in uncertain
    assert rules_for("pozdniakov_2007")
    assert "gaping_mouth_to_bird" not in {rule.rule_id for rule in rules_for("pozdniakov_2007")}


def test_mock_provider_only(tracka_run):
    provider, result = tracka_run
    assert provider.get_call_history() == []
    assert result["provider_calls"] == 0
    assert result["provider"] == "mock"
    assert result["reading"] is None
    with pytest.raises(TypeError, match="MockProvider only"):
        run_round2_tracka(object())  # type: ignore[arg-type]


def test_gate_constants_are_the_preregistered_band():
    assert SYLLABARY_TYPE_MIN == 45
    assert SYLLABARY_TYPE_MAX == 70
    assert HEAPS_BETA_MAX == 0.25
    assert EARLY_INVENTORY_MIN == 0.80


def test_positional_alignment_is_a_hypothesis():
    signs = [["aa", "bb", "aa", "cc"], ["bb", "cc", "aa"]]
    syllables = [["a", "ta"], ["i"], ["a", "ki", "a"]]
    first = positional_alignment(signs, syllables, permutations=20, seed=1)
    second = positional_alignment(signs, syllables, permutations=20, seed=1)
    assert first == second
    assert first["hypothesis_only"] is True
    assert first["reading"] is None
    assert "gloss" not in first


def test_locked_inventories_and_gate(tracka_run):
    _provider, result = tracka_run
    assert result["provider_calls"] == 0
    assert result["side_count"] == 37
    assert result["alignment_triggered"] == []
    assert result["alignments"] == {}
    assert result["reading"] is None
    assert result["syllables"]["inventory"] == 49
    assert result["syllables"]["tokens"] == 3400
    assert result["words"]["inventory"] == 633
    assert result["words"]["tokens"] == 1591
    assert result["syllable_structure_index"] == pytest.approx(0.14430821476417877)
    assert result["word_structure_index"] == pytest.approx(0.343002765519282)
    edges = result["syllable_word_edges"]
    assert edges["frequent_types"] == 43
    assert edges["frequent_in_all_three"] == 40

    expected = {
        "stem": (14488, 630, 0.42161851372627307, 0.0980487972445141, "mixed"),
        "ligature_atomic": (10698, 2210, 0.7221734176862022, 0.09527211754227882, "logographic"),
        "barthel_suffix_only": (14488, 1104, 0.4976262074212989, 0.10175828772344242, "mixed"),
        "barthel_families": (14488, 1091, 0.49543663429135504, 0.10145616524309864, "mixed"),
        "barthel_families_whole": (10711, 2732, 0.7394395657571047, 0.08705648161714996, "logographic"),
        "pozdniakov_2007": (14488, 613, 0.417892552805696, 0.09761486210802373, "mixed"),
        "pozdniakov_2007_whole": (10711, 2173, 0.7203877806325352, 0.0960929635816713, "logographic"),
        "pozdniakov_1996_gaping_mouth": (14488, 504, 0.3775444125609017, 0.09474329838137407, "mixed"),
        "horley_2005": (14660, 573, 0.42224895252209543, 0.09553851788374379, "mixed"),
        "horley_2005_whole": (10711, 2099, 0.7221085811966682, 0.09182050169038869, "logographic"),
    }
    assert set(result["schemes"]) == set(expected)
    for scheme_id, (tokens, inventory, beta, structure, label) in expected.items():
        record = result["schemes"][scheme_id]
        assert record["tokens"] == tokens
        assert record["inventory"] == inventory
        assert record["heaps_beta"] == pytest.approx(beta)
        assert record["structure_index"] == pytest.approx(structure)
        assert record["track2_label"] == label
        assert record["uses_residual"] is False
        if record["gate"] is not None:
            assert record["gate"]["passes"] is False
            assert record["gate"]["count_in_band"] is False
            assert record["gate"]["beta_flattens"] is False
    assert result["schemes"]["stem"]["h2_conditional_mle"] == pytest.approx(4.887533261229475)
    assert result["schemes"]["pozdniakov_2007"]["coverage_of_published_barthel_stems"] == pytest.approx(
        0.5404472667034788
    )
    assert result["schemes"]["horley_2005"]["h2_conditional_mle"] == pytest.approx(4.895582371541816)
    assert result["schemes"]["pozdniakov_1996_gaping_mouth"]["heaps_at"]["2000"] == 268
    assert result["schemes"]["barthel_families"]["heaps_at"]["2000"] == 457


def test_report_matches_result_and_assigns_no_reading(tracka_run):
    _provider, result = tracka_run
    text = render_round2_tracka(result)
    assert REPORT.read_text(encoding="utf-8") == text
    assert "**Verdict: still not a syllabary.**" in text
    assert "not a decipherment" in text
    assert "`reading` is None" in text
    assert "The alignment is not run." in text
    assert "99.7%" in text
    assert FIGURE.is_file()
    assert FIGURE.read_text(encoding="utf-8").startswith("<svg")
