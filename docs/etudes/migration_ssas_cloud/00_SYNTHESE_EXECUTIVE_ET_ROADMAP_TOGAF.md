# SYNTHÈSE EXÉCUTIVE D'ARCHITECTURE & FEUILLE DE ROUTE TOGAF
## Étude de Cadrage Stratégique : Migration du Patrimoine SSAS vers le Cloud — Projet NovaAnalytics

**Référence Dossier :** TOGAF-STUDY-2026-NOVAA-001  
**Auteur :** Lead Enterprise Architecture Manager (Orchestrateur TOGAF 10 ADM & SAFe 6)  
**Destinataires :** Direction Générale, DSI, Directeurs Financiers, Architecture Review Board (ARB)  
**Date :** 12 octobre 2026  
**Classification des Données :** C2 MASSIF  
**Statut :** Dossier Consolidé de Restitution d'Architecture — Pour Décision d'Investissement  

---

## 1. Vue d'Ensemble & Alignement Stratégique (Phase A TOGAF)

Le présent dossier consolide les travaux d'instruction collégiale menés par la brigade d'architectes spécialisés (Solution Architect, Challenger Red Team, CISO, Software Crafter, FinOps et SAFe Delivery).

L'étude arbitre la trajectoire de modernisation des **trois cubes décisionnels critiques** de l'organisation (*Facturation, Recouvrement, Comptabilité Générale*), actuellement hébergés sur des instances SSAS physiques On-Premise vieillissantes et saturées.

```
                           [ L'ALIGNEMENT MÉTHODOLOGIQUE TOGAF 10 ADM ]

  Phase A : Vision           Phase B : Métier           Phase C & D : SI & Infra     Phase E & F : Solutions & Roadmap
+------------------------+ +------------------------+ +--------------------------+ +-----------------------------------+
| Découplage analytique  | | Cadrage des 3 domaines | | Hub/Spoke VNet Zero-Trust| | Arbitrage Option 3 (Fabric/TMDL)  |
| No-Ops sur l'OS        | | Facturation, Recouvre- | | Private Endpoints exclus.| | TCO à 3 ans : 305 k€ (ROI 14 mois)|
| C2 MASSIF non-négociable| | ment, Grand Livre SOX  | | Clés CMK sur HSM FIPS    | | Trajectoire en 4 jalons (5 mois)  |
+------------------------+ +------------------------+ +--------------------------+ +-----------------------------------+
```

---

## 2. Matrice d'Arbitrage & Synthèse des Avis d'Experts

L'originalité et la robustesse de cette démarche d'architecture reposent sur la prise en compte intégrale de la contradiction contradictoire :

| Rôle Spécialiste | Position / Avis Émis | Impact Structurant sur la Décision Finale |
| :--- | :---: | :--- |
| **Solution Architect** | *Recommandation Option 3* | Modernisation Cloud-Native Microsoft Fabric / Semantic Models avec OneLake. |
| **Challenger (Red Team)** | *Avis Défavorable sur Direct Lake* | Rejet du mode Direct Lake pour la comptabilité (risque de fallback DirectQuery). **Imposition du mode VertiPaq Import partitionné** pour sécuriser les temps de réponse ($< 3\text{ s}$). Élimination du Managed HSM (27 k$/an sauvés). |
| **CISO & Sécurité** | *Favorable sous Réserves Strictes* | Imposition d'une enclave réseau 100% privée (Private Link), chiffrement CMK, kill-switch en $< 15\text{ min}$ et **pseudonymisation SHA-256 des débiteurs (RGPD)**. |
| **Software Crafter** | *Directives Craft Validées* | Découpage en Architecture Hexagonale pure (Ports & Adapters), modélisation DDD (Agrégats *LedgerEntry*, *Money* sans float), et versioning Git au format TMDL. |
| **Migration & FinOps** | *Validation Économique Option 3* | **TCO le plus bas du marché (305 k€ à 3 ans)** contre 515 k€ pour le IaaS Lift & Shift. Économie pérenne récurrente : ~60 000 €/an. |
| **SAFe Agile Enabler** | *Trajectoire Prête pour le Train* | Découpage en 7 Enabler Features prioritaires (WSJF), backlog Jira prêt et Definition of Done (DoD) sur 5 piliers. |

---

## 3. Cartographie des Livrables de l'Étude (Le Pack Documentaire)

Le comité de direction et les équipes de réalisation disposent de l'ensemble des documents d'ingénierie détaillés au sein de ce dossier :

* 📁 **`01_DOSSIER_ARCHITECTURE_TECHNIQUE_DAT.md`** : Spécifications complètes du Solution Architect, dimensionnement et patrons de résilience.
* 📁 **`02_RAPPORT_AUDIT_CONTRADICTOIRE.md`** : Contre-enquête de la Red Team, traque des SPOF et matrice de simplification KISS/YAGNI.
* 📁 **`03_AVIS_HOMOLOGATION_SECURITE_DCA.md`** : Rapport officiel de sécurité du CISO, exigences Zero-Trust C2 MASSIF et critères d'homologation.
* 📁 **`04_CONCEPTION_HEXAGONALE_ET_DDD.md`** : Guide de conception logicielle du Software Crafter, modélisation des agrégats et stratégie de tests unitaires 100% TDD.
* 📁 **`05_STRATEGIE_MIGRATION_ET_FINOPS_TCO.md`** : Comparatif financier exhaustif des 4 pistes (IaaS, PaaS, SaaS, Lakehouse) et analyse de rentabilité (ROI).
* 📁 **`06_BACKLOG_LIVRAISON_SAFE_JIRA.md`** : Backlog d'implémentation opérationnel, User Stories chiffrées avec critères d'acceptation et DoD.
* 📁 **`diagrams/`** : Schémas d'architecture éditables de l'état existant (**AS-IS**) et cible (**TO-BE**) sous les 3 formats : **Draw.io (`.drawio`)**, **PlantUML (`.puml`)** et **Mermaid (`.mmd`)**.

---

## 4. Feuille de Route de Transition TOGAF (Phases E & F)

La trajectoire de transformation industrielle s'étale sur **5 mois** en 4 jalons opérationnels :

```
JALON 1 (Mois 1) : FONDATIONS & HOMOLOGATION DCA
└── Déploiement Terraform du VNet Spoke et des Private Endpoints (0 IP Publique).
└── Activation du chiffrement CMK sur Azure Key Vault Premium (FIPS 140-2 Niveau 3).
└── Validation formelle de l'homologation de sécurité DCA par le CISO.

JALON 2 (Mois 2) : PILOTE FACTURATION (BILLINGCUBE)
└── Modélisation déclarative TMDL du BillingCube.
└── Ingestion nocturne incrémentale via ExpressRoute MACsec (Batch validé < 20 min).
└── Recette utilisateurs Power BI (300 requêtes concurrentes < 3s).

JALON 3 (Mois 3-4) : BASCULE COMPTABILITÉ & RECOUVREMENT
└── Déploiement sanctuarisé du LedgerCube (capacité dédiée aux clôtures financières).
└── Déploiement du RecoveryCube avec pseudonymisation dynamique SHA-256 (RGPD).
└── Campagne de Double-Run financier de 30 jours (Écart strict = 0.000%).

JALON 4 (Mois 5) : DÉCOMMISSIONNEMENT & EXTINCTION ON-PREMISE
└── Extinction physique des 3 serveurs SSAS On-Premise.
└── Bascule intégrale en mode No-Ops / Cloud souverain managé.
└── Enregistrement de l'économie FinOps récurrente (60 000 €/an).
```

---

## 5. Décision Finale Recommandée à l'Attention du Comité d'Architecture (ARB)
L'Architecture Review Board est invité à :
1. **Valider formellement la trajectoire Option 3** (Capacité Fabric / Modèles Sémantiques TMDL avec moteur VertiPaq Import partitionné).
2. **Autoriser le budget de Build de 115 000 €** (Jalons 1 à 3), amorti dès le 14e mois par l'extinction des licences et de l'infrastructure On-Premise.
3. **Mandater le train SAFe (ART)** pour démarrer les User Stories du Jalon 1 dès le prochain Program Increment.
