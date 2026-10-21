"""
Tests unitaires pour le Comité d'Architecture Virtuel des 5 Maîtres & Évaluateur Qualité.
Vérifie les rôles, les attributions doctrinales, les tâches et la non-délégation (0 token).
"""

import pytest
from unittest.mock import MagicMock
from src.agents.virtual_committee_agents import (
    create_martin_fowler_agent,
    create_uncle_bob_agent,
    create_werner_vogels_agent,
    create_alistair_cockburn_agent,
    create_sam_newman_agent,
    create_greenops_finops_agent,
    create_architecture_quality_gate_agent
)
from src.tasks.virtual_committee_tasks import (
    create_initial_architecture_draft_task,
    create_fowler_review_task,
    create_uncle_bob_review_task,
    create_vogels_review_task,
    create_cockburn_review_task,
    create_newman_review_task,
    create_greenops_finops_review_task,
    create_quality_gate_evaluation_task,
    create_committee_synthesis_task
)


def test_virtual_committee_agents_attributes():
    mock_llm = "gemini/gemini-1.5-flash"

    fowler = create_martin_fowler_agent(mock_llm)
    assert "Martin Fowler" in fowler.role
    assert "Patterns of Enterprise Application Architecture" in fowler.backstory
    assert not fowler.allow_delegation

    uncle_bob = create_uncle_bob_agent(mock_llm)
    assert "Uncle Bob" in uncle_bob.role
    assert "Clean Architecture" in uncle_bob.backstory
    assert "SOLID" in uncle_bob.backstory
    assert not uncle_bob.allow_delegation

    vogels = create_werner_vogels_agent(mock_llm)
    assert "Werner Vogels" in vogels.role
    assert "Everything fails all the time" in vogels.backstory
    assert not vogels.allow_delegation

    cockburn = create_alistair_cockburn_agent(mock_llm)
    assert "Alistair Cockburn" in cockburn.role
    assert "Hexagonale" in cockburn.backstory or "Ports & Adapters" in cockburn.backstory
    assert not cockburn.allow_delegation

    newman = create_sam_newman_agent(mock_llm)
    assert "Sam Newman" in newman.role
    assert "Building Microservices" in newman.backstory or "Monolith to Microservices" in newman.backstory
    assert not newman.allow_delegation

    greenops = create_greenops_finops_agent(mock_llm)
    assert "GreenOps & FinOps" in greenops.role
    assert "carbone" in greenops.backstory.lower()
    assert "finops" in greenops.backstory.lower()
    assert not greenops.allow_delegation

    judge = create_architecture_quality_gate_agent(mock_llm)
    assert "Quality Gate" in judge.role
    assert not judge.allow_delegation


def test_virtual_committee_tasks_creation():
    mock_llm = "gemini/gemini-1.5-flash"
    judge = create_architecture_quality_gate_agent(mock_llm)
    fowler = create_martin_fowler_agent(mock_llm)

    init_task = create_initial_architecture_draft_task(fowler, "Migrer le monolithe vers le Cloud", "French")
    assert "proposition d'architecture" in init_task.description.lower()

    fowler_task = create_fowler_review_task(fowler, [init_task], "French")
    assert "Martin Fowler" in fowler_task.description
    assert fowler_task.context == [init_task]

    gate_task = create_quality_gate_evaluation_task(judge, [fowler_task], min_score=85.0, language="French")
    assert "Score Global :" in gate_task.description
    assert "85.0" in gate_task.description or "85" in gate_task.description

    synthesis_task = create_committee_synthesis_task(fowler, [gate_task], "French")
    assert "Grand Rapport Consolidé" in synthesis_task.description
