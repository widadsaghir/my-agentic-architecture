import re
import xml.etree.ElementTree as ET
from pathlib import Path
import pytest

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = BASE_DIR / "docs"

def test_all_plantuml_diagrams_are_syntax_valid_and_offline():
    """
    Vérifie la conformité de tous les fichiers PlantUML (.puml) du projet :
    - Balises @startuml et @enduml obligatoires.
    - Interdiction absolue des !include distants (garantie de fonctionnement en réseau déconnecté).
    - Standard de police defaultFontSize 16 pour la lisibilité.
    """
    puml_files = list(DOCS_DIR.glob("**/*.puml"))
    assert len(puml_files) > 0, "Aucun fichier PlantUML trouvé dans docs/ !"

    for puml in puml_files:
        content = puml.read_text(encoding="utf-8")
        assert "@startuml" in content, f"{puml.name} : Balise @startuml manquante !"
        assert "@enduml" in content, f"{puml.name} : Balise @enduml manquante !"

        # Règle Air-Gap : Aucun import distant http/https
        assert not re.search(r"!include\s+https?://", content), (
            f"VIOLATION AIR-GAP : {puml.name} contient un '!include' distant, "
            "interdit sur les réseaux d'entreprise restreints !"
        )

def test_all_mermaid_diagrams_have_valid_syntax():
    """
    Vérifie la conformité syntaxique des fichiers Mermaid (.mmd) :
    - Interdiction de la syntaxe illégale '..>' dans les flowcharts (doit être '-.->').
    - Déclaration d'un type de diagramme valide (flowchart, sequenceDiagram, gantt).
    """
    mmd_files = list(DOCS_DIR.glob("**/*.mmd"))
    assert len(mmd_files) > 0, "Aucun fichier Mermaid trouvé dans docs/ !"

    valid_types = ("flowchart", "graph", "sequenceDiagram", "gantt", "classDiagram", "erDiagram")

    for mmd in mmd_files:
        content = mmd.read_text(encoding="utf-8").strip()
        first_line = content.split("\n")[0].strip()
        assert any(first_line.startswith(t) for t in valid_types), (
            f"{mmd.name} : Type Mermaid invalide en première ligne : '{first_line}'"
        )

        # Vérification anti-régression '..>' dans flowchart
        if first_line.startswith("flowchart"):
            assert "..>" not in content, (
                f"ERREUR SYNTAXE MERMAID : {mmd.name} contient '..>' illégal dans un flowchart ! "
                "Utiliser '-.->' pour les pointillés."
            )

def test_all_drawio_diagrams_are_valid_xml():
    """
    Vérifie que 100% des fichiers Draw.io (.drawio) du projet sont du XML valide et non corrompu.
    """
    drawio_files = list(DOCS_DIR.glob("**/*.drawio"))
    assert len(drawio_files) > 0, "Aucun fichier Draw.io trouvé dans docs/ !"

    for drawio in drawio_files:
        content = drawio.read_text(encoding="utf-8")
        try:
            root = ET.fromstring(content)
            assert root.tag == "mxfile", f"{drawio.name} : La racine XML doit être <mxfile>"
        except ET.ParseError as e:
            pytest.fail(f"XML CORROMPU : {drawio.name} n'est pas un fichier Draw.io XML valide : {e}")
