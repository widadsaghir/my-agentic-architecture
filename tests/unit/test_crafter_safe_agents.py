import pytest
from src.agents.architect_agents import create_crafter_agent, create_safe_enabler_agent

def test_crafter_agent_attributes():
    """Vérifie que l'agent Crafter porte les micro-patterns, le TDD et l'Hexagonale."""
    crafter = create_crafter_agent(llm="gemini/gemini-1.5-flash")

    assert "Crafter" in crafter.role or "Domain" in crafter.role
    goal_lower = crafter.goal.lower()
    assert "hexagonale" in goal_lower or "ports & adapters" in goal_lower
    assert "tdd" in goal_lower or "testabilité" in goal_lower

    backstory_lower = crafter.backstory.lower()
    assert "solid" in backstory_lower or "kiss" in backstory_lower
    assert crafter.allow_delegation is False

def test_safe_enabler_agent_attributes():
    """Vérifie que l'agent SAFe traduit l'architecture en Enablers et Stories Jira."""
    safe_agent = create_safe_enabler_agent(llm="gemini/gemini-1.5-flash")

    assert "SAFe" in safe_agent.role
    goal_lower = safe_agent.goal.lower()
    assert "enabler" in goal_lower
    assert "jira" in goal_lower or "user stories" in goal_lower

    backstory_lower = safe_agent.backstory.lower()
    assert "art" in backstory_lower or "train" in backstory_lower or "delivery" in backstory_lower
    assert safe_agent.allow_delegation is False
