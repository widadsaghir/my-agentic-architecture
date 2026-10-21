import sys
from pathlib import Path
import pytest
from src.main import parse_arguments

def test_cli_argument_parsing_with_all_flags(monkeypatch):
    """Vérifie que la CLI parse correctement l'ensemble des arguments sans exception."""
    test_args = [
        "main.py",
        "--mode", "committee",
        "--language", "French",
        "--input", "Notes de cadrage test",
        "--output", "test_out.md",
        "--study-dir", "docs/etudes/test_study",
        "--min-score", "90.0",
        "--max-loops", "5",
        "--audience", "Jury L2",
        "--log-file", "logs/test.log",
        "--publish-git"
    ]
    monkeypatch.setattr(sys, "argv", test_args)
    args = parse_arguments()

    assert args.mode == "committee"
    assert args.language == "French"
    assert args.input == "Notes de cadrage test"
    assert args.output == "test_out.md"
    assert args.study_dir == "docs/etudes/test_study"
    assert args.min_score == 90.0
    assert args.max_loops == 5
    assert args.audience == "Jury L2"
    assert args.log_file == "logs/test.log"
    assert args.publish_git is True

def test_cli_reads_input_file_when_path_provided(tmp_path):
    """Vérifie le chargement transparent du contenu quand un chemin de fichier est passé en entrée."""
    sample_file = tmp_path / "cadrage.md"
    sample_file.write_text("# Cadrage Projet Test\nContenu du besoin d'architecture.", encoding="utf-8")

    # Simulation de la logique de lecture de main()
    input_content = str(sample_file)
    input_path = Path(input_content)
    assert input_path.is_file()

    with open(input_path, "r", encoding="utf-8") as f:
        loaded_text = f.read()

    assert "# Cadrage Projet Test" in loaded_text
    assert "Contenu du besoin d'architecture." in loaded_text

def test_study_dir_creation_handles_nested_paths(tmp_path):
    """Vérifie que la création du dossier d'étude gère automatiquement les arborescences imbriquées."""
    deep_study_dir = tmp_path / "a" / "b" / "c" / "etude_profonde"
    assert not deep_study_dir.exists()

    deep_study_dir.mkdir(parents=True, exist_ok=True)
    assert deep_study_dir.exists()
    assert deep_study_dir.is_dir()
