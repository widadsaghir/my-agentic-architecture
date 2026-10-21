"""
Test End-to-End simulé (0 token) validant le cycle de bouclage multi-agents
(Self-Correction Loop) avec l'AgenticLoopController, le Comité d'Architecture et le Conseil d'Éloquence.
"""

import pytest
from src.orchestration import AgenticLoopController, QualityEvaluation


def test_agentic_loop_self_correction_workflow_simulation():
    """
    Simule un cycle complet de bouclage d'auto-correction :
    Itération 1 : Score insuffisant (72/100) -> Génération de rétroaction ciblée.
    Itération 2 : Prise en compte des critiques -> Score d'excellence (91/100) -> Validation.
    """
    controller = AgenticLoopController(min_score=85.0, max_iterations=4)

    # 1. Sortie simulée du Juge Qualité lors du Cycle 1
    eval_cycle_1 = """
    # Rapport d'Audit & Verdict Qualité du Comité d'Architecture
    
    ### 📊 Synthèse Chiffrée & Grille d'Évaluation :
    - Score Global : 72/100
    - SOLID & Clean Architecture : 65/100
    - Résilience & Anti-SPOF : 70/100
    - Hexagonale & Ports : 80/100
    - Microservices & Bounded Contexts : 75/100
    - GreenOps & FinOps : 68/100
    - Compromis & Évolutivité : 74/100
    
    ### ⚖️ Verdict du Comité :
    Statut : À REPRENDRE (Score < 85.0)
    
    ### ⚠️ Gaps & Faiblesses critiques à corriger :
    - Présence d'un broker unique sans réplication multi-AZ créant un SPOF critique.
    - Violation de Dependency Inversion : persistance SQL appelée directement par le cas d'usage métier.
    - Absence de stratégie GreenOps d'extinction nocturne des clusters non productifs.
    """

    res1 = controller.parse_evaluation(eval_cycle_1, iteration=1)
    assert res1.score == 72.0
    assert res1.passed is False
    assert controller.should_continue(res1) is True

    # Génération du prompt de feedback
    feedback_prompt = controller.build_feedback_prompt(res1, target_domain="Comité des 5 Maîtres")
    assert "72.0/100" in feedback_prompt
    assert "broker unique" in feedback_prompt
    assert "Dependency Inversion" in feedback_prompt

    # 2. Sortie simulée du Juge Qualité lors du Cycle 2 (après prise en compte des critiques)
    eval_cycle_2 = """
    # Rapport d'Audit & Verdict Qualité du Comité d'Architecture
    
    ### 📊 Synthèse Chiffrée & Grille d'Évaluation :
    - Score Global : 91/100
    - SOLID & Clean Architecture : 92/100
    - Résilience & Anti-SPOF : 95/100
    - Hexagonale & Ports : 90/100
    - Microservices & Bounded Contexts : 88/100
    - GreenOps & FinOps : 90/100
    - Compromis & Évolutivité : 90/100
    
    ### ⚖️ Verdict du Comité :
    Statut : VALIDÉ (Score >= 85.0)
    
    ### ⚠️ Gaps & Faiblesses critiques à corriger :
    - Aucune faiblesse bloquante restante. Architecture d'excellence validée.
    """

    res2 = controller.parse_evaluation(eval_cycle_2, iteration=2)
    assert res2.score == 91.0
    assert res2.passed is True
    assert controller.should_continue(res2) is False

    # Génération du résumé Markdown du bouclage
    summary = controller.generate_loop_summary_markdown()
    assert "| 1 | **72.0/100** |" in summary
    assert "| 2 | **91.0/100** |" in summary
    assert "Qualité validée avec succès à l'itération 2" in summary


def test_orator_eloquence_loop_simulation():
    """
    Simule la boucle d'évaluation d'éloquence pour le Conseil des 5 Orateurs :
    Itération 1 : Score 78/100 -> Jobs demande d'épurer, Hassan II d'élever la langue.
    Itération 2 : Score 89/100 -> Validé.
    """
    controller = AgenticLoopController(min_score=85.0, max_iterations=4)

    eval_orator_1 = """
    # Rapport d'Audit & Verdict d'Éloquence
    
    ### 📊 Synthèse Chiffrée & Grille Rhétorique :
    - Score Global : 78/100
    - Clarté & Simplicité (Jobs) : 70/100
    - Émotion & Pathos (MLK) : 85/100
    - Rythme & Scénographie (Obama) : 80/100
    - Vocabulaire & Élévation (Hassan II) : 75/100
    - Force de Conviction & Concision (Churchill) : 80/100
    
    ### ⚖️ Verdict du Juge :
    Statut : À REPRENDRE
    
    ### ⚠️ Gaps & Faiblesses critiques à corriger :
    - Trop de jargon technique dans l'introduction (Steve Jobs demande de supprimer les acronymes).
    - Manque de métaphores nobles pour décrire la transformation (Hassan II exige d'élever le verbe).
    """

    res1 = controller.parse_evaluation(eval_orator_1, iteration=1)
    assert res1.score == 78.0
    assert res1.passed is False
    assert controller.should_continue(res1) is True

    eval_orator_2 = """
    # Rapport d'Audit & Verdict d'Éloquence
    
    ### 📊 Synthèse Chiffrée & Grille Rhétorique :
    - Score Global : 89/100
    - Clarté & Simplicité (Jobs) : 90/100
    - Émotion & Pathos (MLK) : 88/100
    - Rythme & Scénographie (Obama) : 90/100
    - Vocabulaire & Élévation (Hassan II) : 90/100
    - Force de Conviction & Concision (Churchill) : 88/100
    
    ### ⚖️ Verdict du Juge :
    Statut : VALIDÉ
    
    ### ⚠️ Gaps & Faiblesses critiques à corriger :
    - Texte prêt pour la scène.
    """

    res2 = controller.parse_evaluation(eval_orator_2, iteration=2)
    assert res2.score == 89.0
    assert res2.passed is True
    assert controller.should_continue(res2) is False
