import pytest
from src.orchestration.loop_controller import AgenticLoopController, QualityEvaluation


def test_loop_controller_initialization_and_validation():
    controller = AgenticLoopController(min_score=85.0, max_iterations=4)
    assert controller.min_score == 85.0
    assert controller.max_iterations == 4
    assert len(controller.history) == 0

    with pytest.raises(ValueError):
        AgenticLoopController(min_score=-5)

    with pytest.raises(ValueError):
        AgenticLoopController(min_score=105)

    with pytest.raises(ValueError):
        AgenticLoopController(max_iterations=0)


def test_parse_evaluation_passing_score():
    controller = AgenticLoopController(min_score=85.0, max_iterations=4)
    raw_eval = """
    # Rapport d'Audit du Comité d'Architecture
    
    ### Synthèse Chiffrée
    - Score Global : 88/100
    - SOLID : 92/100
    - Résilience & Anti-SPOF : 85/100
    - Hexagonale & DDD : 90/100
    - GreenOps & FinOps : 85/100
    
    ### Points d'amélioration mineurs
    - Documenter le format des événements Kafka du Outbox pattern.
    - Ajouter les métriques Prometheus de latence p99 dans les SLOs.
    """

    evaluation = controller.parse_evaluation(raw_eval, iteration=1)

    assert evaluation.score == 88.0
    assert evaluation.passed is True
    assert evaluation.iteration == 1
    assert "SOLID" in evaluation.criteria_scores
    assert evaluation.criteria_scores["SOLID"] == 92.0
    assert evaluation.criteria_scores["Hexagonale & DDD"] == 90.0
    assert len(evaluation.critiques) >= 2
    assert controller.should_continue(evaluation) is False


def test_parse_evaluation_failing_score_triggers_loop():
    controller = AgenticLoopController(min_score=85.0, max_iterations=4)
    raw_eval = """
    # Évaluation Qualité - Itération 1
    
    Score Technique : 68/100
    
    Critères :
    - SOLID : 60/100
    - SPOF_Resilience : 55/100
    - Microservices : 80/100
    
    ## Axes d'amélioration critiques :
    - La base PostgreSQL unique représente un SPOF critique sous forte charge.
    - Violation du Single Responsibility Principle dans le module OrderProcessor.
    - Absence d'évaluation FinOps des instances managées.
    """

    evaluation = controller.parse_evaluation(raw_eval, iteration=1)

    assert evaluation.score == 68.0
    assert evaluation.passed is False
    assert controller.should_continue(evaluation) is True
    assert len(evaluation.critiques) >= 2

    # Génération du prompt de rétroaction
    feedback_prompt = controller.build_feedback_prompt(evaluation, target_domain="Architecture Logicielle")
    assert "RÉTROACTION CORRECTIVE" in feedback_prompt
    assert "68.0/100" in feedback_prompt
    assert "85.0/100" in feedback_prompt
    assert "SPOF" in feedback_prompt


def test_loop_controller_max_iterations_circuit_breaker():
    controller = AgenticLoopController(min_score=85.0, max_iterations=3)

    # Itération 1 : 60/100 -> continue
    ev1 = controller.parse_evaluation("Score : 60/100\n- Faiblesses :\n- Manque de résilience", iteration=1)
    assert controller.should_continue(ev1) is True

    # Itération 2 : 75/100 -> continue
    ev2 = controller.parse_evaluation("Score : 75/100\n- Faiblesses :\n- Couplage persistant", iteration=2)
    assert controller.should_continue(ev2) is True

    # Itération 3 : 80/100 (inférieur à 85 mais max itérations = 3 atteint) -> STOP
    ev3 = controller.parse_evaluation("Score : 80/100\n- Faiblesses :\n- FinOps incomplet", iteration=3)
    assert controller.should_continue(ev3) is False

    summary_md = controller.generate_loop_summary_markdown()
    assert "Progression de la Qualité" in summary_md
    assert "Itération 1" in summary_md or "| 1 |" in summary_md
    assert "| 3 |" in summary_md
    assert "Clôture forcée" in summary_md


def test_parse_empty_evaluation_safe_handling():
    controller = AgenticLoopController(min_score=80.0, max_iterations=2)
    ev = controller.parse_evaluation("", iteration=1)
    assert ev.score == 0.0
    assert ev.passed is False
    assert controller.should_continue(ev) is True
