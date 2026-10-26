import pytest
from src.tools.presales_linters import AsIsRealityLinter

def test_as_is_reality_linter_detects_cloud_hallucination():
    """Vérifie que l'injection injustifiée de Cloud ou Kafka dans l'AS-IS est bloquée."""
    bad_as_is = """
    # 01. Diagnostic AS-IS : Architecture Existante
    Le SI Central Cloud de l'entreprise héberge une flotte de microservices et un cluster Kafka.
    Les gares interrogent le Cloud via une liaison télécom instable.
    """
    res = AsIsRealityLinter.lint_as_is_content(bad_as_is, tender_spec="Le SI de l'entreprise est relié aux gares.")
    assert res["valid"] is False
    assert len(res["violations"]) >= 2
    assert any("cloud" in v.lower() for v in res["violations"])
    assert res["as_is_reality_score"] < 100.0

def test_as_is_reality_linter_allows_valid_on_premise_as_is():
    """Vérifie qu'un AS-IS fondé sur du On-Premise / Datacenter d'entreprise est validé à 100%."""
    valid_as_is = """
    # 01. Diagnostic AS-IS : Architecture Existante
    Le SI Central d'Entreprise hébergé en Datacenters On-Premise historiques utilise une base SQL relationnelle.
    Les gares locales disposent d'un contrôleur propriétaire relié par une liaison télécom instable.
    """
    res = AsIsRealityLinter.lint_as_is_content(valid_as_is, tender_spec="Le SI de l'entreprise est relié aux gares.")
    assert res["valid"] is True
    assert len(res["violations"]) == 0
    assert res["as_is_reality_score"] == 100.0

def test_as_is_reality_linter_allows_explicit_tender_mentions():
    """Vérifie qu'un terme moderne est toléré dans l'AS-IS si le cahier des charges le mentionne explicitement."""
    tender_spec = "Le client dispose déjà d'un bus Apache Kafka historique dans son SI."
    as_is_text = """
    # 01. Diagnostic AS-IS
    L'existant repose sur un bus Kafka vieillissant qui sature lors des pics d'aléa.
    """
    res = AsIsRealityLinter.lint_as_is_content(as_is_text, tender_spec=tender_spec)
    assert res["valid"] is True
