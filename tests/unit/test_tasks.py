import pytest
from crewai import Agent
from src.tasks.architecture_tasks import (
    create_preliminary_design_task,
    create_security_audit_task,
    create_challenge_task
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

