"""
Module de définition des tâches d'architecture pour CrewAI.
"""
from .architecture_tasks import (
    create_preliminary_design_task,
    create_security_audit_task,
    create_challenge_task,
    create_software_crafting_task,
    create_safe_delivery_task,
    create_finops_task,
    create_meta_maintenance_task,
    create_career_branding_task,
    create_convergence_reconciliation_task,
    create_executive_restitution_task,
    create_presales_bid_audit_task
)

from .virtual_committee_tasks import (
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

from .orator_tasks import (
    create_orator_context_analysis_task,
    create_roundtable_propositions_task,
    create_stage_director_synthesis_task,
    create_eloquence_judge_evaluation_task,
    create_final_speech_pack_task
)

__all__ = [
    # Tâches Brigade TOGAF / SAFe / CISO / AVV
    "create_preliminary_design_task",
    "create_security_audit_task",
    "create_challenge_task",
    "create_software_crafting_task",
    "create_safe_delivery_task",
    "create_finops_task",
    "create_meta_maintenance_task",
    "create_career_branding_task",
    "create_convergence_reconciliation_task",
    "create_executive_restitution_task",
    "create_presales_bid_audit_task",
    # Tâches Comité d'Architecture Virtuel & Quality Gate
    "create_initial_architecture_draft_task",
    "create_fowler_review_task",
    "create_uncle_bob_review_task",
    "create_vogels_review_task",
    "create_cockburn_review_task",
    "create_newman_review_task",
    "create_greenops_finops_review_task",
    "create_quality_gate_evaluation_task",
    "create_committee_synthesis_task",
    # Tâches Conseil des Grands Orateurs & Éloquence TEDx
    "create_orator_context_analysis_task",
    "create_roundtable_propositions_task",
    "create_stage_director_synthesis_task",
    "create_eloquence_judge_evaluation_task",
    "create_final_speech_pack_task"
]
