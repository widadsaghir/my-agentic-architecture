import pytest
from src.agents.architect_agents import create_finops_agent

def test_create_finops_agent_attributes():
    """Vérifie que l'agent FinOps est initialisé avec les piliers d'évaluation économique et TCO."""
    finops = create_finops_agent(llm="gemini/gemini-3.8-flash")

    # 1. Rôle
    assert "FinOps" in finops.role or "TCO" in finops.role

    # 2. Piliers clés dans le Goal (TCO, coûts comparatifs, rentabilité, ROI)
    goal_lower = finops.goal.lower()
    assert "tco" in goal_lower
    assert "coût" in goal_lower or "budget" in goal_lower
    assert "comparatif" in goal_lower or "trajectoire" in goal_lower

    # 3. Posture d'expert économique dans la Backstory
    backstory_lower = finops.backstory.lower()
    assert "finops" in backstory_lower
    assert "cloud" in backstory_lower or "rentabilité" in backstory_lower

    # 4. Non-délégation
    assert finops.allow_delegation is False
