"""
Tests unitaires pour l'exportateur déterministe ExecutivePrompterExporter (0 token).
"""

import pytest
from pathlib import Path
from src.tools.executive_prompter_exporter import ExecutivePrompterExporter


def test_analyze_speech_metrics():
    exporter = ExecutivePrompterExporter(words_per_minute=130)

    sample_script = """
    Mesdames et Messieurs, [REGARD AUDIENCE] nous sommes à un tournant décisif. [PAUSE 2s]
    [BREATHE]
    Chaque architecture que nous validons aujourd'hui engage la résilience de notre entreprise pour la décennie à venir.
    [SOURIRE]
    Ce n'est pas une simple évolution technique, c'est une refondation totale. [↘ INTONATION DESCENDANTE]
    """

    metrics = exporter.analyze_speech_metrics(sample_script)

    assert metrics["total_words"] > 25
    assert metrics["pauses_count"] == 1
    assert metrics["breathes_count"] == 1
    assert metrics["smiles_count"] == 1
    assert metrics["gazes_count"] == 1
    assert metrics["intonations_count"] == 1
    assert "min" in metrics["estimated_duration"]


def test_export_prompter_markdown_and_html(tmp_path: Path):
    exporter = ExecutivePrompterExporter(words_per_minute=130)

    sample_script = "L'architecture est un acte de responsabilité. [PAUSE 2s]\n\nNous choisissons la clarté."
    md_file = tmp_path / "prompter.md"
    html_file = tmp_path / "prompter.html"

    exported_md = exporter.export_prompter_markdown(
        title="Keynote Architecture",
        script_text=sample_script,
        output_file=md_file
    )
    assert exported_md.exists()
    content_md = exported_md.read_text(encoding="utf-8")
    assert "Script Prompter TEDx" in content_md
    assert "Volume de mots" in content_md

    exported_html = exporter.export_interactive_html(
        title="Keynote Architecture",
        script_text=sample_script,
        output_file=html_file
    )
    assert exported_html.exists()
    content_html = exported_html.read_text(encoding="utf-8")
    assert "<!DOCTYPE html>" in content_html
    assert "prompter-card" in content_html
    assert "badge-pause" in content_html


def test_validate_pocket_guide_structure():
    exporter = ExecutivePrompterExporter()

    incomplete_html = '<div class="action-bar"></div><div class="kpi-grid"></div>'
    res_incomplete = exporter.validate_pocket_guide_structure(incomplete_html)
    assert not res_incomplete["is_valid"]
    assert "star_guide" in res_incomplete["missing_elements"]
    assert "acting_masterclass" in res_incomplete["missing_elements"]

    complete_html = """
    <div class="action-bar">PDF, STAR, Coaching, Pitch, QA, Mental</div>
    <div class="kpi-grid">KPI Chips</div>
    <div id="star-guide">STAR Masterclass</div>
    <div id="acting-masterclass">Acting & Orator Masterclass</div>
    <div id="sophro">Sophrology & Mindset</div>
    <div id="speech">Pitch Mot a Mot</div>
    <div id="qa">Top 10 QA Questions</div>
    """
    res_complete = exporter.validate_pocket_guide_structure(complete_html)
    assert res_complete["is_valid"]
    assert res_complete["pillars_count"] == 7
    assert len(res_complete["missing_elements"]) == 0

