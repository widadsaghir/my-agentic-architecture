import pytest
from src.agents.architect_agents import create_presales_bid_director_agent
from src.tasks.architecture_tasks import create_presales_bid_audit_task

def test_presales_bid_director_agent_attributes():
    """Vérifie que le 24ème agent porte la posture avant-vente, les livrables formels et le dérisquage MVP."""
    agent = create_presales_bid_director_agent(llm="gemini/gemini-1.5-flash")

    assert "Presales" in agent.role or "Avant-Vente" in agent.role
    goal_lower = agent.goal.lower()
    assert "livrables formels" in goal_lower or "dag" in goal_lower
    assert "entrants" in goal_lower and "sortants" in goal_lower
    assert "co-construction" in goal_lower or "mvp" in goal_lower

    backstory_lower = agent.backstory.lower()
    assert "conseil" in backstory_lower
    assert "as-is" in backstory_lower or "foisonnement" in backstory_lower
    assert agent.allow_delegation is False

def test_presales_bid_audit_task_creation():
    """Vérifie que la tâche d'avant-vente impose le pack des livrables et la matrice entrants/sortants."""
    agent = create_presales_bid_director_agent(llm="gemini/gemini-1.5-flash")
    task = create_presales_bid_audit_task(agent=agent, language="Français")

    desc_lower = task.description.lower()
    assert "entrants" in desc_lower and "sortants" in desc_lower
    assert "livrables formels" in desc_lower or "dag" in desc_lower
    assert "co-construction" in desc_lower or "vis ma vie" in desc_lower
    assert "mvp" in desc_lower or "pilote" in desc_lower

    output_lower = task.expected_output.lower()
    assert "matrice contractuelle" in output_lower or "entrants" in output_lower
    assert "45 min" in output_lower or "20 min pitch" in output_lower
