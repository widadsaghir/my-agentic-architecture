import pytest
from src.agents.architect_agents import create_ciso_agent

def test_create_ciso_agent_attributes():
    """Vérifie que l'agent CISO est initialisé avec ses règles d'architecture et de sécurité."""
    # On passe un identifiant de modèle ou un LLM valide
    ciso = create_ciso_agent(llm="gemini/gemini-1.5-flash")

    # 1. Vérification du rôle
    assert "Security" in ciso.role or "CISO" in ciso.role

    # 2. Vérification des piliers de doctrine dans le Goal (Zero-Trust, C2, NIST)
    goal_lower = ciso.goal.lower()
    assert "zero-trust" in goal_lower or "zero trust" in goal_lower
    assert "c2" in goal_lower
    assert "nist" in goal_lower or "800-207" in goal_lower

    # 3. Vérification de la posture dans la Backstory (DCA, secrets, chiffrement)
    backstory_lower = ciso.backstory.lower()
    assert "dca" in backstory_lower or "conformité" in backstory_lower
    assert "secrets" in backstory_lower or "chiffrement" in backstory_lower

    # 4. Règles de délégation : un auditeur sécurité valide son propre périmètre
    assert ciso.allow_delegation is False
