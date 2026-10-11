import pytest
from src.tasks.architecture_tasks import create_preliminary_design_task, create_security_audit_task

class DummyAgent:
    pass

def test_preliminary_design_task_language_injection():
    """Vérifie que la tâche de conception préliminaire injecte strictement la langue demandée."""
    agent = DummyAgent()
    task_fr = create_preliminary_design_task(agent, "Notes projet Far&Co", "French")

    assert "[French]" in task_fr.description
    assert "[French]" in task_fr.expected_output
    assert "Notes projet Far&Co" in task_fr.description

    task_en = create_preliminary_design_task(agent, "Project notes", "English")
    assert "[English]" in task_en.description
    assert "[English]" in task_en.expected_output

def test_security_audit_task_language_and_doctrine():
    """Vérifie que la tâche CISO intègre les exigences de sécurité et la langue."""
    agent = DummyAgent()
    task = create_security_audit_task(agent, context_tasks=[], language="French")

    assert "[French]" in task.description
    assert "[French]" in task.expected_output
    assert "Zero-Trust" in task.description or "zero-trust" in task.description.lower()
    assert "C2" in task.description
    assert "DCA" in task.description
