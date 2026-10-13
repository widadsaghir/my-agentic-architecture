import pytest
from pathlib import Path
from unittest.mock import MagicMock
from crewai import Crew, Process, LLM
from src.agents import (
    create_manager_agent,
    create_solution_architect_agent,
    create_challenger_agent,
    create_ciso_agent,
    create_crafter_agent,
    create_safe_enabler_agent,
    create_finops_agent
)
from src.tasks import (
    create_preliminary_design_task,
    create_challenge_task,
    create_security_audit_task,
    create_software_crafting_task,
    create_safe_delivery_task,
    create_finops_task
)
from src.tools.jira_exporter import JiraBacklogExporter

def test_full_crew_e2e_execution_with_mock_llm(tmp_path):
    """
    Test End-to-End Niveau 2 du Software Crafter :
    Exécute le pipeline complet des 6 agents et 6 tâches avec un Mock LLM déterministe (0 Token / < 2s).
    Vérifie l'enchaînement de bout en bout et l'exportation du pack multi-fichiers dans study_dir.
    """
    mock_llm = LLM(model="gemini/gemini-3.8-flash", api_key="fake-test-key")
    mock_llm.call = MagicMock(side_effect=[
        "# 01 DAT Mock\nSolution d'architecture préliminaire.",
        "# 02 Audit Mock\nRapport contradictoire Red Team.",
        "# 03 DCA Mock\nAvis formel de sécurité C2 MASSIF.",
        "# 04 Craft Mock\nArchitecture Hexagonale et Domain Design.",
        "### User Story `TEST-01`\n* **Titre :** Story Test\n* **Format :** En tant que dev\n* **Estimation :** 5\n* **Critères d'Acceptation :** Given test, Then ok\n* **Definition of Done :** Done",
        "# 05 FinOps Mock\nAnalyse TCO comparatif 4 options."
    ])

    # 1. Instanciation des agents
    manager = create_manager_agent(mock_llm)
    solution = create_solution_architect_agent(mock_llm)
    challenger = create_challenger_agent(mock_llm)
    ciso = create_ciso_agent(mock_llm)
    crafter = create_crafter_agent(mock_llm)
    safe = create_safe_enabler_agent(mock_llm)
    finops = create_finops_agent(mock_llm)

    # 2. Tâches chaînées
    t1 = create_preliminary_design_task(solution, "Notes de test", "French")
    t2 = create_challenge_task(challenger, [t1], "French")
    t3 = create_security_audit_task(ciso, [t1, t2], "French")
    t4 = create_software_crafting_task(crafter, [t1, t2, t3], "French")
    t5 = create_safe_delivery_task(safe, [t1, t4, t3], "French")
    t6 = create_finops_task(finops, [t1, t2, t5], "French")

    # 3. Assemblage de la Crew
    crew = Crew(
        agents=[solution, challenger, ciso, crafter, safe, finops],
        tasks=[t1, t2, t3, t4, t5, t6],
        process=Process.sequential,
        manager_agent=manager,
        verbose=False
    )

    # 4. Exécution E2E sans token
    result = crew.kickoff()
    assert result is not None
    assert len(crew.tasks) == 6

    # 5. Validation de la génération du pack documentaire multi-fichiers
    study_dir = tmp_path / "etude_mock_e2e"
    study_dir.mkdir(parents=True, exist_ok=True)

    deliverables_mapping = [
        ("01_DOSSIER_ARCHITECTURE_TECHNIQUE_DAT.md", t1),
        ("02_RAPPORT_AUDIT_CONTRADICTOIRE.md", t2),
        ("03_AVIS_HOMOLOGATION_SECURITE_DCA.md", t3),
        ("04_CONCEPTION_HEXAGONALE_ET_DDD.md", t4),
        ("05_STRATEGIE_MIGRATION_ET_FINOPS_TCO.md", t6),
        ("06_BACKLOG_LIVRAISON_SAFE_JIRA.md", t5)
    ]

    for filename, task_obj in deliverables_mapping:
        content = str(task_obj.output.raw) if hasattr(task_obj, "output") and task_obj.output else ""
        out_file = study_dir / filename
        out_file.write_text(content, encoding="utf-8")
        assert out_file.exists()
        assert len(out_file.read_text(encoding="utf-8")) > 0

    # 6. Validation de l'export Jira CSV
    jira_csv = study_dir / "backlog_jira.csv"
    count = JiraBacklogExporter().export_to_csv(str(t5.output.raw), jira_csv)
    assert count == 1
    assert jira_csv.exists()
