import pytest
from src.agents.architect_agents import create_challenger_agent

def test_create_challenger_agent_attributes():
    """Vérifie que l'agent Challenger / Red Team incarne la contradiction technique et la traque des SPOF."""
    challenger = create_challenger_agent(llm="gemini/gemini-1.5-flash")

    # 1. Rôle
    assert "Challenger" in challenger.role or "Red Team" in challenger.role

    # 2. Piliers clés dans le Goal (SPOF, sur-ingénierie / Golden Hammer, KISS/YAGNI)
    goal_lower = challenger.goal.lower()
    assert "spof" in goal_lower
    assert "sur-ingénierie" in goal_lower or "over-engineering" in goal_lower or "golden hammer" in goal_lower
    assert "kiss" in goal_lower or "yagni" in goal_lower or "simplification" in goal_lower

    # 3. Posture critique dans la Backstory (Reflection, contradiction constructive, SRE)
    backstory_lower = challenger.backstory.lower()
    assert "critique" in backstory_lower or "contradiction" in backstory_lower or "sre" in backstory_lower or "reflection" in backstory_lower

    # 4. Non-délégation : l'évaluateur contradictoire analyse lui-même
    assert challenger.allow_delegation is False
