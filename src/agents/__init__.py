"""
Module de fabrique des agents d'architecture et comités d'experts.
"""
from .architect_agents import (
    create_manager_agent,
    create_solution_architect_agent,
    create_ciso_agent,
    create_crafter_agent,
    create_safe_enabler_agent,
    create_challenger_agent,
    create_finops_agent,
    create_meta_agent,
    create_career_branding_agent,
    create_presales_bid_director_agent
)

from .virtual_committee_agents import (
    create_martin_fowler_agent,
    create_uncle_bob_agent,
    create_werner_vogels_agent,
    create_alistair_cockburn_agent,
    create_sam_newman_agent,
    create_greenops_finops_agent,
    create_architecture_quality_gate_agent
)

from .orator_agents import (
    create_hassan_ii_agent,
    create_steve_jobs_agent,
    create_martin_luther_king_agent,
    create_winston_churchill_agent,
    create_barack_obama_agent,
    create_stage_director_agent,
    create_eloquence_judge_agent
)

__all__ = [
    # Brigade TOGAF / SAFe / CISO / AVV
    "create_manager_agent",
    "create_solution_architect_agent",
    "create_ciso_agent",
    "create_crafter_agent",
    "create_safe_enabler_agent",
    "create_challenger_agent",
    "create_finops_agent",
    "create_meta_agent",
    "create_career_branding_agent",
    "create_presales_bid_director_agent",
    # Comité d'Architecture Virtuel des 5 Maîtres & Green/FinOps
    "create_martin_fowler_agent",
    "create_uncle_bob_agent",
    "create_werner_vogels_agent",
    "create_alistair_cockburn_agent",
    "create_sam_newman_agent",
    "create_greenops_finops_agent",
    "create_architecture_quality_gate_agent",
    # Conseil des 5 Grands Orateurs & Éloquence TEDx
    "create_hassan_ii_agent",
    "create_steve_jobs_agent",
    "create_martin_luther_king_agent",
    "create_winston_churchill_agent",
    "create_barack_obama_agent",
    "create_stage_director_agent",
    "create_eloquence_judge_agent"
]
