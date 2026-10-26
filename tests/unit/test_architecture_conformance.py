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
        # Brigade TOGAF / SAFe / CISO
        "create_manager_agent",
        "create_solution_architect_agent",
        "create_challenger_agent",
        "create_ciso_agent",
        "create_crafter_agent",
        "create_safe_enabler_agent",
        "create_finops_agent",
        "create_meta_agent",
        "create_career_branding_agent",
        "create_presales_bid_director_agent",
        # Comité d'Architecture Virtuel des 5 Maîtres & Green/FinOps
        "create_martin_fowler_agent",
        "create_uncle_bob_agent",
        "create_werner_vogels_agent",
        "create_alistair_cockburn_agent",
        "create_sam_newman_agent",
        "create_greenops_finops_agent",
        "create_architecture_quality_gate_agent",
        # Conseil des 5 Grands Orateurs & Éloquence TEDx
        "create_hassan_ii_agent",
        "create_steve_jobs_agent",
        "create_martin_luther_king_agent",
        "create_winston_churchill_agent",
        "create_barack_obama_agent",
        "create_stage_director_agent",
        "create_eloquence_judge_agent"
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
        # Tâches Brigade TOGAF / SAFe / CISO
        "create_preliminary_design_task",
        "create_challenge_task",
        "create_security_audit_task",
        "create_software_crafting_task",
        "create_safe_delivery_task",
        "create_finops_task",
        "create_meta_maintenance_task",
        "create_career_branding_task",
        "create_convergence_reconciliation_task",
        "create_executive_restitution_task",
        "create_presales_bid_audit_task",
        # Tâches Comité d'Architecture Virtuel & Quality Gate
        "create_initial_architecture_draft_task",
        "create_fowler_review_task",
        "create_uncle_bob_review_task",
        "create_vogels_review_task",
        "create_cockburn_review_task",
        "create_newman_review_task",
        "create_greenops_finops_review_task",
        "create_quality_gate_evaluation_task",
        "create_committee_synthesis_task",
        # Tâches Conseil des Grands Orateurs & Éloquence TEDx
        "create_orator_context_analysis_task",
        "create_roundtable_propositions_task",
        "create_stage_director_synthesis_task",
        "create_eloquence_judge_evaluation_task",
        "create_final_speech_pack_task"
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
    Vérifie que les adaptateurs déterministes (RAG, GitPublisher, JiraExporter, DiagramExporter, PresentationExporter, PrompterExporter) sont exportés.
    """
    expected_tools = [
        "ArchitectureRAGManager",
        "KnowledgeSearchTool",
        "GitPublisher",
        "JiraBacklogExporter",
        "DiagramExporter",
        "LogAnalyzer",
        "CareerExporter",
        "ExecutivePresentationExporter",
        "ExecutivePrompterExporter",
        "AsIsRealityLinter",
        "BidComplianceGate",
        "ZeroTofuViewportGate"
    ]
    for tool_name in expected_tools:
        assert hasattr(tools_module, tool_name), f"Composant déterministe '{tool_name}' manquant dans src/tools/"
        assert tool_name in tools_module.__all__

def test_documentation_drift_conformance():
    """
    Vérifie la cohérence documentaire : le fichier CONTEXTE_PROJET.md doit lister
    les composants majeurs du système.
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
    assert "meta-agent" in content
    assert "agent carrière & personal branding" in content
