import pytest
from src.tools.presales_linters import BidComplianceGate

def test_bid_compliance_gate_validates_complete_bid():
    """Vérifie qu'une proposition contenant les 4 piliers et tous les livrables est validée à 100%."""
    complete_bid = """
    # Proposition d'Architecture & Stratégie d'Offre
    ## 1. Démarche et Livrables Contractuels
    Nous formalisons le Dossier d'Architecture Générale (DAG) selon TOGAF, consignant les ADRs majeurs.
    Les spécifications d'interfaces sont détaillées dans le DAT et le plan de résilience dans le PCA de gare.
    
    ## 2. Matrice Contractuelle
    - Entrants Client : Schémas télécoms et fiches horaires.
    - Sortants Cabinet : DAG, contrats AsyncAPI et cahier de recette.
    
    ## 3. Co-Construction & Conduite du Changement
    Nos architectes s'immergent dans un protocole « Vis ma vie » avec les équipes terrain.
    Les ateliers de co-conception permettent une conduite du changement et une adoption réussie.
    
    ## 4. Trajectoire Sécurisée
    Un pilote MVP sur 3 sites valide la résilience en conditions réelles avant tout déploiement.
    """
    res = BidComplianceGate.audit_bid_response(complete_bid)
    assert res["compliant"] is True
    assert res["score"] == 100.0
    assert len(res["missing_deliverables"]) == 0
    assert len(res["missing_concepts"]) == 0

def test_bid_compliance_gate_flags_missing_elements():
    """Vérifie que l'omission du DAG, des entrants/sortants ou de la co-construction est sanctionnée."""
    incomplete_bid = """
    # Proposition Technique
    Nous allons installer un broker Kafka et des passerelles K3s pour moderniser le système.
    La livraison se fera en mode agile classique.
    """
    res = BidComplianceGate.audit_bid_response(incomplete_bid)
    assert res["compliant"] is False
    assert res["score"] < 50.0
    assert "DAG" in res["missing_deliverables"]
    assert "matrice entrants/sortants" in res["missing_concepts"]
    assert "co-construction" in res["missing_concepts"]
