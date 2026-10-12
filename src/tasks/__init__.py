"""
Module de définition des tâches d'architecture pour CrewAI.
"""
from .architecture_tasks import (
    create_preliminary_design_task,
    create_security_audit_task,
    create_challenge_task,
    create_software_crafting_task,
    create_safe_delivery_task
)

__all__ = [
    "create_preliminary_design_task",
    "create_security_audit_task",
    "create_challenge_task",
    "create_software_crafting_task",
    "create_safe_delivery_task"
]
