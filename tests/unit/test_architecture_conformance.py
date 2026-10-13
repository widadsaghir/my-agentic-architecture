import inspect
import pytest
from pathlib import Path
import src.agents as agents_module
import src.tasks as tasks_module
import src.tools as tools_module

# Racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent.parent

def test_all_operational_agents_exist_and_exported():
    """
    Architectural Fitness Function (Test d'Aptitude Architecturale).
    Vérifie que 100% des agents déclarés opérationnels dans la documentation
    sont effectivement implémentés en Python et exportés dans __all__.
    """
    operational_agents = [
        "create_manager_agent",
        "create_solution_architect_agent",
        "create_challenger_agent",
        "create_ciso_agent",
        "create_crafter_agent",
        "create_safe_enabler_agent",
        "create_finops_agent",
        "create_meta_agent",
        "create_career_branding_agent"
    ]

    for agent_func_name in operational_agents:
        assert hasattr(agents_module, agent_func_name), (
            f"Dérive détectée : L'agent '{agent_func_name}' est déclaré opérationnel "
            f"mais n'est pas implémenté ou exporté dans src/agents/ !"
        )
        assert agent_func_name in agents_module.__all__, (
            f"L'agent '{agent_func_name}' n'est pas listé dans src/agents/__all__"
        )
        func = getattr(agents_module, agent_func_name)
        assert callable(func), f"'{agent_func_name}' doit être une fonction appelable"

def test_all_operational_tasks_exist_and_exported():
    """
    Architectural Fitness Function.
    Vérifie que chaque agent opérationnel possède sa fonction de tâche associée dans src/tasks/.
    """
    operational_tasks = [
        "create_preliminary_design_task",
        "create_challenge_task",
        "create_security_audit_task",
        "create_software_crafting_task",
        "create_safe_delivery_task",
        "create_finops_task",
        "create_meta_maintenance_task",
        "create_career_branding_task",
        "create_convergence_reconciliation_task"
    ]

    for task_func_name in operational_tasks:
        assert hasattr(tasks_module, task_func_name), (
            f"Dérive détectée : La tâche '{task_func_name}' n'est pas implémentée dans src/tasks/ !"
        )
        assert task_func_name in tasks_module.__all__, (
            f"La tâche '{task_func_name}' n'est pas listée dans src/tasks/__all__"
        )

def test_deterministic_tools_exist_and_exported():
    """
    Vérifie que les adaptateurs déterministes (RAG, GitPublisher, JiraExporter, DiagramExporter) sont exportés.
    """
    expected_tools = [
        "ArchitectureRAGManager",
        "KnowledgeSearchTool",
        "GitPublisher",
        "JiraBacklogExporter",
        "DiagramExporter",
        "LogAnalyzer",
        "CareerExporter"
    ]
    for tool_name in expected_tools:
        assert hasattr(tools_module, tool_name), f"Composant déterministe '{tool_name}' manquant dans src/tools/"
        assert tool_name in tools_module.__all__

def test_documentation_drift_conformance():
    """
    Vérifie la cohérence documentaire : le fichier CONTEXTE_PROJET.md doit lister
    les 8 agents et expliciter le statut des agents futurs (Meta-Agent, Carrière)
    afin qu'aucun composant ne soit oublié ou prétendu disponible à tort.
    """
    contexte_file = BASE_DIR / "docs" / "CONTEXTE_PROJET.md"
    assert contexte_file.exists(), "Le fichier docs/CONTEXTE_PROJET.md est introuvable !"
    content = contexte_file.read_text(encoding="utf-8").lower()

    # Vérification des agents en cours ou terminés
    assert "solution & infrastructure architect" in content
    assert "challenger / red team" in content
    assert "ciso & data protection" in content
    assert "software crafter" in content
    assert "safe system architect" in content
    assert "migration & finops" in content

    # Vérification des agents futurs explicites (pas oubliés !)
    assert "meta-agent" in content
    assert "agent carrière & personal branding" in content
