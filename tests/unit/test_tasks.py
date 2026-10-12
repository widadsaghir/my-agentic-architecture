import pytest
from crewai import Agent
from src.tasks.architecture_tasks import (
    create_preliminary_design_task,
    create_security_audit_task,
    create_challenge_task,
    create_software_crafting_task,
    create_safe_delivery_task,
    create_finops_task
)

@pytest.fixture
def agent():
    return Agent(
        role="Test Architect",
        goal="Tester la configuration et les attributs des tâches",
        backstory="Agent de test dédié aux validations unitaires",
        llm="gemini/gemini-1.5-flash",
        allow_delegation=False
    )

def test_preliminary_design_task_language_injection(agent):
    """Vérifie que la tâche de conception préliminaire injecte strictement la langue demandée."""
    task_fr = create_preliminary_design_task(agent, "Notes projet Far&Co", "French")

    assert "[French]" in task_fr.description
    assert "[French]" in task_fr.expected_output
    assert "Notes projet Far&Co" in task_fr.description

    task_en = create_preliminary_design_task(agent, "Project notes", "English")
    assert "[English]" in task_en.description
    assert "[English]" in task_en.expected_output

def test_security_audit_task_language_and_doctrine(agent):
    """Vérifie que la tâche CISO intègre les exigences de sécurité et la langue."""
    task = create_security_audit_task(agent, context_tasks=[], language="French")

    assert "[French]" in task.description
    assert "[French]" in task.expected_output
    assert "Zero-Trust" in task.description or "zero-trust" in task.description.lower()
    assert "C2" in task.description
    assert "DCA" in task.description

def test_challenge_task_language_and_doctrine(agent):
    """Vérifie que la tâche Challenger intègre la recherche de SPOF, l'anti-sur-ingénierie et la langue."""
    task = create_challenge_task(agent, context_tasks=[], language="French")

    assert "[French]" in task.description
    assert "[French]" in task.expected_output
    desc_lower = task.description.lower()
    assert "spof" in desc_lower
    assert "sur-ingénierie" in desc_lower or "golden hammer" in desc_lower or "kiss" in desc_lower
    assert task.context == []

def test_software_crafting_task_language_and_doctrine(agent):
    """Vérifie que la tâche Software Crafter intègre l'Architecture Hexagonale, le DDD et le TDD."""
    task = create_software_crafting_task(agent, context_tasks=[], language="French")

    assert "[French]" in task.description
    assert "[French]" in task.expected_output
    desc_lower = task.description.lower()
    assert "hexagonale" in desc_lower or "ports" in desc_lower or "adapters" in desc_lower
    assert "ddd" in desc_lower or "domaine" in desc_lower or "agrégat" in desc_lower
    assert "tdd" in desc_lower or "tests unitaires" in desc_lower or "solid" in desc_lower
    assert task.context == []

def test_safe_delivery_task_language_and_doctrine(agent):
    """Vérifie que la tâche SAFe Enabler intègre le découpage en backlog Jira et la Definition of Done."""
    task = create_safe_delivery_task(agent, context_tasks=[], language="French")

    assert "[French]" in task.description
    assert "[French]" in task.expected_output
    desc_lower = task.description.lower()
    assert "jira" in desc_lower or "user stories" in desc_lower or "enabler" in desc_lower
    assert "dod" in desc_lower or "definition of done" in desc_lower
    assert task.context == []

def test_finops_task_language_and_doctrine(agent):
    """Vérifie que la tâche FinOps intègre l'analyse des coûts, le TCO comparatif et la langue."""
    task = create_finops_task(agent, context_tasks=[], language="French")

    assert "[French]" in task.description
    assert "[French]" in task.expected_output
    desc_lower = task.description.lower()
    assert "tco" in desc_lower
    assert "coût" in desc_lower or "budget" in desc_lower or "comparatif" in desc_lower
    assert task.context == []



