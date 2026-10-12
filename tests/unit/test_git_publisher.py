import pytest
from pathlib import Path
from src.tools.git_publisher import GitPublisher

def test_git_publisher_secret_scanner_detects_keys():
    """Vérifie que le scan anti-secrets détecte les clés privées, tokens et API keys."""
    publisher = GitPublisher()

    # Contenu sain
    clean_text = "# Dossier d'Architecture\nArchitecture Cloud avec Private Endpoints."
    assert publisher.scan_content_for_secrets(clean_text) == []

    # Contenu contenant une fausse clé API Google
    leak_google = "GEMINI_API_KEY=AIzaSyD-FakeSecretKeyForTesting123456789"
    warnings_google = publisher.scan_content_for_secrets(leak_google)
    assert len(warnings_google) > 0
    assert any("Google/Gemini" in w or "API Key" in w for w in warnings_google)

    # Contenu contenant un bloc de clé privée RSA
    leak_rsa = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA0fake..."
    warnings_rsa = publisher.scan_content_for_secrets(leak_rsa)
    assert len(warnings_rsa) > 0
    assert any("Clé Privée" in w or "RSA" in w for w in warnings_rsa)

def test_format_conventional_commit():
    """Vérifie le formatage des messages sous la norme Conventional Commits."""
    publisher = GitPublisher()

    msg = publisher.format_conventional_commit(
        commit_type="docs",
        scope="architecture",
        description="ajout du dossier DAT pour NovaAnalytics"
    )
    assert msg == "docs(architecture): ajout du dossier DAT pour NovaAnalytics"

    msg_breaking = publisher.format_conventional_commit(
        commit_type="feat",
        scope="api",
        description="refonte de l'interface REST",
        breaking=True
    )
    assert msg_breaking == "feat(api)!: refonte de l'interface REST"

def test_hitl_approval_mechanism():
    """Vérifie que l'arbitrage Human-in-the-Loop accepte [O/N] et bloque le push en cas de refus."""
    publisher = GitPublisher()

    # Simulation d'approbation positive
    assert publisher.evaluate_hitl_decision(user_input="o") is True
    assert publisher.evaluate_hitl_decision(user_input="OUI") is True
    assert publisher.evaluate_hitl_decision(user_input="yes") is True

    # Simulation de refus souverain
    assert publisher.evaluate_hitl_decision(user_input="n") is False
    assert publisher.evaluate_hitl_decision(user_input="non") is False
    assert publisher.evaluate_hitl_decision(user_input="") is False
