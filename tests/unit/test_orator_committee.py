"""
Tests unitaires pour le Conseil des Grands Orateurs & Éloquence TEDx (0 token).
"""

import pytest
from unittest.mock import MagicMock
from src.agents.orator_agents import (
    create_hassan_ii_agent,
    create_steve_jobs_agent,
    create_martin_luther_king_agent,
    create_winston_churchill_agent,
    create_barack_obama_agent,
    create_stage_director_agent,
    create_eloquence_judge_agent
)
from src.tasks.orator_tasks import (
    create_orator_context_analysis_task,
    create_roundtable_propositions_task,
    create_stage_director_synthesis_task,
    create_eloquence_judge_evaluation_task,
    create_final_speech_pack_task
)


def test_orator_agents_attributes():
    mock_llm = "gemini/gemini-1.5-flash"

    hassan = create_hassan_ii_agent(mock_llm)
    assert "Hassan II" in hassan.role
    assert "dialectique" in hassan.backstory.lower() or "verbe raffiné" in hassan.backstory.lower()
    assert not hassan.allow_delegation

    jobs = create_steve_jobs_agent(mock_llm)
    assert "Steve Jobs" in jobs.role
    assert "One More Thing" in jobs.backstory
    assert "règle de trois" in jobs.backstory

    mlk = create_martin_luther_king_agent(mock_llm)
    assert "Martin Luther King" in mlk.role
    assert "I Have a Dream" in mlk.backstory or "anaphorique" in mlk.backstory

    churchill = create_winston_churchill_agent(mock_llm)
    assert "Winston Churchill" in churchill.role
    assert "Blood, toil, tears and sweat" in churchill.backstory

    obama = create_barack_obama_agent(mock_llm)
    assert "Barack Obama" in obama.role
    assert "silences" in obama.backstory or "empathique" in obama.backstory

    director = create_stage_director_agent(mock_llm)
    assert "Stage Director" in director.role

    judge = create_eloquence_judge_agent(mock_llm)
    assert "Eloquence Judge" in judge.role


def test_orator_tasks_creation():
    mock_llm = "gemini/gemini-1.5-flash"
    director = create_stage_director_agent(mock_llm)
    judge = create_eloquence_judge_agent(mock_llm)

    context_task = create_orator_context_analysis_task(
        director,
        "Lancement d'une plateforme d'architecture IA",
        audience="Comité Exécutif",
        format_type="Keynote 15 min",
        language="French"
    )
    assert "Audience cible" in context_task.description

    roundtable_task = create_roundtable_propositions_task(director, [context_task], "French")
    assert "Table Ronde des Grands Orateurs" in roundtable_task.description
    assert roundtable_task.context == [context_task]

    synthesis_task = create_stage_director_synthesis_task(director, [roundtable_task], "French")
    assert "[PAUSE 2s]" in synthesis_task.description
    assert "[BREATHE]" in synthesis_task.description

    judge_task = create_eloquence_judge_evaluation_task(judge, [synthesis_task], min_score=85.0, language="French")
    assert "Score Global :" in judge_task.description

    pack_task = create_final_speech_pack_task(director, [judge_task], "French")
    assert "Pack Complet" in pack_task.description
