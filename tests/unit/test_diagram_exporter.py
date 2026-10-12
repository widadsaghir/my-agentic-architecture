import pytest
from pathlib import Path
from src.tools.diagram_exporter import DiagramExporter

def test_diagram_exporter_generates_three_formats(tmp_path):
    """
    Vérifie que le DiagramExporter génère systématiquement les 3 formats :
    - PlantUML (.puml) avec skinparam defaultFontSize 16 et defaultFontColor #000000
    - Mermaid (.mmd) avec syntaxe valide
    - Draw.io (.drawio) avec structure XML valide
    """
    exporter = DiagramExporter()

    title = "Architecture Cible Test"
    nodes = [
        {"id": "usr", "label": "Utilisateur", "type": "actor"},
        {"id": "api", "label": "API Gateway", "type": "service"},
        {"id": "db", "label": "Base de Données", "type": "database"}
    ]
    links = [
        {"source": "usr", "target": "api", "label": "HTTPS"},
        {"source": "api", "target": "db", "label": "SQL"}
    ]

    out_dir = tmp_path / "diagrams"
    files = exporter.export_diagram_bundle(
        title=title,
        nodes=nodes,
        links=links,
        output_dir=out_dir,
        base_name="architecture_test"
    )

    assert "puml" in files
    assert "mmd" in files
    assert "drawio" in files

    # 1. Vérification PlantUML
    puml_content = Path(files["puml"]).read_text(encoding="utf-8")
    assert "skinparam defaultFontSize 16" in puml_content
    assert "skinparam defaultFontColor #000000" in puml_content
    assert "@startuml" in puml_content
    assert "@enduml" in puml_content

    # 2. Vérification Mermaid
    mmd_content = Path(files["mmd"]).read_text(encoding="utf-8")
    assert "flowchart" in mmd_content
    assert "usr" in mmd_content
    assert "api" in mmd_content

    # 3. Vérification Draw.io XML
    drawio_content = Path(files["drawio"]).read_text(encoding="utf-8")
    assert "<mxfile" in drawio_content
    assert "<diagram" in drawio_content
    assert "</mxfile>" in drawio_content
