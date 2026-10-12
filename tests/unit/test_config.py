import os
import pytest
from src.config.settings import AppConfig

def test_app_config_loads_environment(monkeypatch):
    """Vérifie que la configuration lit correctement les variables d'environnement."""
    monkeypatch.setenv("GEMINI_API_KEY", "test_mock_key_12345")
    monkeypatch.setenv("GEMINI_WORKER_MODEL", "gemini-1.5-flash")
    monkeypatch.setenv("GEMINI_MANAGER_MODEL", "gemini-1.5-pro")

    config = AppConfig()

    assert config.api_key == "test_mock_key_12345"
    assert config.worker_model == "gemini-1.5-flash"
    assert config.manager_model == "gemini-1.5-pro"
    assert os.environ.get("GOOGLE_API_KEY") == "test_mock_key_12345"

def test_app_config_raises_error_when_key_missing(monkeypatch):
    """Vérifie qu'une exception explicite est levée si la clé API est absente."""
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setenv("GEMINI_API_KEY", "")

    with pytest.raises(ValueError, match="GEMINI_API_KEY est manquante"):
        AppConfig()

def test_app_config_raises_error_when_placeholder_key(monkeypatch):
    """Vérifie qu'une exception est levée si la clé est restée sur la valeur par défaut."""
    monkeypatch.setenv("GEMINI_API_KEY", "votre_cle_api_ici")

    with pytest.raises(ValueError, match="GEMINI_API_KEY est manquante ou non renseignée"):
        AppConfig()
