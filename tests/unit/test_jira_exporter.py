import pytest
from pathlib import Path
from src.tools.jira_exporter import JiraBacklogExporter

def test_jira_exporter_parses_and_exports_csv_with_semicolon(tmp_path):
    """
    Vérifie que l'exportateur Jira génère un fichier CSV :
    - Délimité par un point-virgule (;) pour Excel Français.
    - Encodé en UTF-8-sig pour la gestion propre des accents.
    - Contenant les champs Jira indispensables (Issue Type, Summary, Story Points, DoD).
    """
    exporter = JiraBacklogExporter()

    sample_markdown = """
### User Story `NOVA-INFRA-101`
* **Titre :** Déploiement Terraform de la Landing Zone Zero-Trust
* **Format :** En tant que Cloud Engineer, je souhaite déployer le VNet Spoke.
* **Estimation :** 5 Story Points
* **Critères d'Acceptation :** Given Terraform, When applied, Then 0 IP publique.
* **Definition of Done :** Tests unitaires validés, revue par les pairs.

### User Story `NOVA-SEC-202`
* **Titre :** Chiffrement CMK sur Azure Key Vault Premium
* **Format :** En tant que SecOps, je souhaite configurer une clé RSA 4096.
* **Estimation :** 8 Story Points
* **Critères d'Acceptation :** Given clé CMK, When révoquée, Then kill-switch < 15 min.
* **Definition of Done :** Scan Gitleaks propre, audit SIEM WORM 365j.
    """

    output_csv = tmp_path / "backlog_jira.csv"
    count = exporter.export_to_csv(sample_markdown, output_csv)

    assert count == 2
    assert output_csv.exists()

    content = output_csv.read_text(encoding="utf-8-sig")

    # 1. Vérification du délimiteur point-virgule (Règle Excel Français)
    assert ";" in content
    lines = content.strip().split("\n")
    header = lines[0]
    assert header.startswith("Issue Type;Summary;Description;Story Points")

    # 2. Vérification des données extraites
    assert "Déploiement Terraform de la Landing Zone Zero-Trust" in content
    assert "Chiffrement CMK sur Azure Key Vault Premium" in content
    assert ";5;" in content or ";5 Story Points;" in content or "5" in lines[1]

def test_jira_exporter_invest_linter_checks_oversized_stories():
    """Vérifie que le linter INVEST détecte les stories trop volumineuses (> 8 points) ou incomplètes."""
    exporter = JiraBacklogExporter()

    small_story = {
        "id": "OMNI-01",
        "story_points": "5",
        "acceptance_criteria": "Given A, When B, Then C",
        "definition_of_done": "Tests unitaires 100%"
    }
    lint_small = exporter.lint_story_invest(small_story)
    assert lint_small["invest_status"] == "CONFORME_INVEST"
    assert lint_small["is_oversized"] is False

    huge_story = {
        "id": "OMNI-02",
        "story_points": "13",
        "acceptance_criteria": "Critères ok",
        "definition_of_done": "DoD ok"
    }
    lint_huge = exporter.lint_story_invest(huge_story)
    assert "WARNING_TAILLE" in lint_huge["invest_status"]
    assert lint_huge["is_oversized"] is True

