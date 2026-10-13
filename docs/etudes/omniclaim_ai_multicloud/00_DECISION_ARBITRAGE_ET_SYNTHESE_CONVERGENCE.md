# DÉCISION D'ARBITRAGE & SYNTHÈSE DE CONVERGENCE (ARB) — OMNICLAIM AI

**Instance de Gouvernance :** Architecture Review Board (ARB)  
**Rôle :** 👑 Lead Enterprise Architecture Manager (TOGAF 10 ADM & SAFe 6)  
**Statut de la Décision :** **DÉCISION FERME & EXÉCUTOIRE (CONSENSUS GATE)**  
**Classification des Données :** **C2 MASSIF**  
**Date :** Octobre 2026  

---

## 1. Synthèse Exécutive de l'Arbitrage Final

Après instruction contradictoire menée par l'ensemble de la brigade d'architecture (Solution Architect, Challenger Red Team, CISO, Software Crafter, SAFe Enabler et FinOps), le Lead Architecture Manager rend l'arbitrage formel suivant :

> **DÉCISION D'ARBITRAGE N° 2026-ARB-042 :**  
> **Rejet de la topologie Multi-Cloud fragmentée en Phase 1 au profit d'un socle Cloud-Native unifié sous AWS avec Amazon Bedrock en enclave souveraine C2 MASSIF, complété d'une isolation stricte par Architecture Hexagonale garantissant la réversibilité sans réécriture.**

Cet arbitrage résout la divergence majeure soulevée par le **Challenger Red Team** et confirmée par l'analyse financière **FinOps** : le coût d'egress inter-cloud (AWS vers Azure) et la dispersion des compétences DevOps auraient grevé le ROI de 140 k€/an sans gain métier mesurable.

---

## 2. Matrice des Divergences & Arbitrages Rendus

| Sujet d'Architecture | Proposition Initiale (Solution Architect) | Objections Critiques (Challenger & FinOps) | Décision Arbitrée (Consensus Gate) |
| :--- | :--- | :--- | :--- |
| **Topologie Cloud** | Multi-Cloud Hybride (AWS Ingestion + Azure OpenAI) | Risque de surcoût egress réseau (140 k€/an), latence Direct Connect et complexité IAM croisée. | **Mono-Cloud AWS unifié en Phase 1** (Amazon Bedrock privé) avec enclave de secours Azure en Phase 2. |
| **Souveraineté des Modèles IA** | Appel direct à des API managées de tokens | Risque de prompt injection indirecte et fuite PII sur des endpoints mutualisés. | **Bedrock Guardrails + Dé-identification locale PII** avant toute inférence. Zéro apprentissage sur les données clients. |
| **Gouvernance Décisionnelle** | Automatisation maximale par agents IA | Risque d'hallucination et d'indemnisation frauduleuse sans recours. | **Règle bloquante Human-in-the-Loop (HITL)** : automatisation stricte sous 2 000 € et score < 0.15. Au-delà, suspension et arbitrage humain. |
| **Couplage Applicatif** | Intégration via SDK Cloud natifs | Risque de *Vendor Lock-in* rendant toute réversibilité impossible. | **Architecture Hexagonale pure (Ports & Adapters)** : le cœur métier ignore AWS et Bedrock via le port SPI `ClaimAnalyzerPort`. |

---

## 3. Architecture Cible Consolidée & Réconciliée

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             ARCHITECTURE CIBLE RÉCONCILIÉE ASSURGLOBAL                           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ZONE INGESTION & ÉVÉNEMENTS (AWS)                                                                │
│ • Amazon API Gateway (mTLS, WAF C2) ➔ Amazon MSK (Kafka Asynchrone)                              │
│ • Absorption des pics climatiques (multiplicateur x10 en 24h sans contention)                    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ZONE CŒUR MÉTIER & TRAITEMENT (AWS EKS & ARCHITECTURE HEXAGONALE)                                │
│ • Microservices conteneurisés sous EKS avec typage fort DDD (`ClaimAmount`, `FraudScore`)        │
│ • Ports & Adapters : Cœur de domaine 100% découplé de l'infrastructure                           │
│ • Persistance : Amazon Aurora PostgreSQL Multi-AZ (Chiffrement KMS CMK)                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ ENCLAVE COGNITIVE & GARDE-FOUS IA (AMAZON BEDROCK PRIVÉ)                                         │
│ • Modèles multimodaux hébergés en réseau privé (VPC PrivateLink, 0 transit internet)              │
│ • Détection de fraude, OCR multimodal de constats et barrières anti-prompt injection             │
│ • Règle HITL : Routage automatique vers corbeille gestionnaire si montant > 2000 € ou fraude >= 0.15│
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Bilan Économique & Trajectoire de Réalisation

* **Coût d'Investissement Build :** $350\text{ k€}$ (sur 3 Quarters SAFe, 6 Sprints).
* **Coût Récurrent Run :** $190\text{ k€/an}$ (contre $700\text{ k€/an}$ actuellement sous Oracle/WebLogic On-Premise).
* **Économie Nette à 3 ans :** **$+84.6\%$ de ROI** avec seuil de rentabilité (*Payback*) atteint au **18ème mois**.
* **Prochaine Étape :** Démarrage du PI Planning (Program Increment) sur l'Enabler Epic `OMNI-EPIC-001` par le train SAFe.
