import pytest
from src.agents import (
    create_manager_agent,
    create_solution_architect_agent,
    create_challenger_agent,
    create_ciso_agent,
    create_crafter_agent,
    create_safe_enabler_agent
)
from src.tasks import (
    create_preliminary_design_task,
    create_challenge_task,
    create_security_audit_task,
    create_software_crafting_task,
    create_safe_delivery_task
)
from crewai import Crew, Process

def test_full_pipeline_assembly():
    """
    Vérifie l'assemblage complet de la chaîne sans appel réel LLM.
    Valide l'ordonnancement séquentiel des 5 agents spécialisés et de leurs 5 tâches.
    """
    dummy_llm = "gemini/gemini-1.5-flash"

    # 1. Instanciation des 6 agents (1 Manager + 5 Spécialistes)
    manager = create_manager_agent(dummy_llm)
    solution = create_solution_architect_agent(dummy_llm)
    challenger = create_challenger_agent(dummy_llm)
    ciso = create_ciso_agent(dummy_llm)
    crafter = create_crafter_agent(dummy_llm)
    safe = create_safe_enabler_agent(dummy_llm)

    # 2. Création des 5 tâches avec passage de contexte
    t1 = create_preliminary_design_task(solution, "Notes test", "French")
    t2 = create_challenge_task(challenger, [t1], "French")
    t3 = create_security_audit_task(ciso, [t1, t2], "French")
    t4 = create_software_crafting_task(crafter, [t1, t2, t3], "French")
    t5 = create_safe_delivery_task(safe, [t1, t4, t3], "French")

    # 3. Assemblage de la Crew
    crew = Crew(
        agents=[solution, challenger, ciso, crafter, safe],
        tasks=[t1, t2, t3, t4, t5],
        process=Process.sequential,
        manager_agent=manager,
        verbose=False
    )

    assert len(crew.agents) == 5
    assert len(crew.tasks) == 5
    assert crew.process == Process.sequential
    assert crew.manager_agent == manager
