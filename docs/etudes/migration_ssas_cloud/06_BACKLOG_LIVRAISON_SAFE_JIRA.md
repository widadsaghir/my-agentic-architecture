# BACKLOG D'IMPLÉMENTATION SAFE & TICKETS JIRA OPÉRATIONNELS
## Découpage Vertical, Enabler Epics, Features, User Stories & Definition of Done — Projet NovaAnalytics

**Référence :** AGILE-SAFE-2026-NOVAA-001  
**Auteur :** SAFe System Architect & Agile Delivery Enabler  
**Destinataires :** Product Managers, Product Owners, Scrum Masters, Équipes de Build du Train (ART)  
**Méthode de Priorisation :** Weighted Shortest Job First (WSJF)  
**Classification des Données :** C2 MASSIF  

---

## 1. Cadre du Programme & Découpage en Incréments (PI)

```
                           [ TRAIN DE LIVRAISON AGILE (ART) — 3 INCRÉMENTS ]

       PROGRAM INCREMENT 01 (PI-01)          PROGRAM INCREMENT 02 (PI-02)          PROGRAM INCREMENT 03 (PI-03)
  +------------------------------------+ +------------------------------------+ +------------------------------------+
  | Socle Infra, Sécurité & CI/CD      | | Migration des Modèles Métier       | | Clôtures, Industrialisation & DCA  |
  | • VNet Spoke, Private Links        | | • BillingCube (Direct Lake Pilote) | | • LedgerCube (Intégrité SOX)       |
  | • Azure Key Vault Premium CMK      | | • RecoveryCube (RLS & Hachage)     | | • Double Run Comptable (0 écart)   |
  | • Usine Logicielle TMDL GitOps     | | • Recette Performance P95 < 3s     | | • Homologation DCA & Extinction    |
  +------------------------------------+ +------------------------------------+ +------------------------------------+
```

---

## 2. Enabler Epic Chapeau

### `ENB-EPIC-01 : Modernisation Sécurisée du Socle Décisionnel NovaAnalytics vers le Cloud`
* **Hypothèse de Valeur Métier :**  
  *En migrant les trois cubes SSAS On-Premise vers des modèles sémantiques managés sous capacité Fabric dédiée avec intégration Git/TMDL et sécurité Zero-Trust C2 MASSIF, nous éliminerons 100% de la dette technique matérielle, réduirons la fenêtre batch nocturne sous les 20 minutes, et offrirons aux 300 contrôleurs de gestion un temps de réponse interactif garanti inférieur à 3 secondes, tout en économisant 60 000 €/an en MCO.*
* **Métriques de Succès (Leading Indicators) :**
  - Temps de réponse $P95 < 3\text{ secondes}$ sur 300 utilisateurs Power BI simultanés.
  - Fenêtre batch de rafraîchissement nocturne réduite de 6h à $< 20\text{ minutes}$.
  - Zéro point de terminaison public exposé (100% Private Endpoints).
  - 100% de parité financière (variance = 0.000%) lors du double-run comptable.

---

## 3. Matrice de Priorisation WSJF des Enabler Features

| ID Feature | Titre de la Feature | Valeur Métier (CoD) | Taille du Job | Score WSJF | PI Cible |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **ENB-FEAT-01** | Landing Zone VNet, Private Endpoints & Zero-Trust | 50 | 5 | **10.00** | PI-01 |
| **ENB-FEAT-02** | Azure Key Vault Premium CMK & Procédure Kill-Switch | 45 | 5 | **9.00** | PI-01 |
| **ENB-FEAT-03** | Usine Logicielle CI/CD TMDL & Tabular Editor BPA | 40 | 5 | **8.00** | PI-01 |
| **ENB-FEAT-04** | Migration Pilote BillingCube (Facturation) | 35 | 8 | **4.38** | PI-02 |
| **ENB-FEAT-05** | Migration RecoveryCube avec RLS & Pseudonymisation DCP | 30 | 8 | **3.75** | PI-02 |
| **ENB-FEAT-06** | Migration Sanctuarisée LedgerCube (Comptabilité SOX) | 48 | 13 | **3.69** | PI-03 |
| **ENB-FEAT-07** | Double-Run Financier, Audit DCA & Décommissionnement | 40 | 8 | **5.00** | PI-03 |

---

## 4. Backlog Détaillé des User Stories Jira Techniques (Échantillon Clé)

### User Story `NOVA-INFRA-101`
* **Titre :** Déploiement Infrastructure as Code (Terraform) de la Landing Zone et Private Links
* **Format :**  
  *En tant que* Cloud Platform Engineer,  
  *Je souhaite* déployer via Terraform le VNet Spoke, les subnets dédiés et les Private Endpoints vers OneLake, Power BI et Key Vault,  
  *Afin de* sanctuariser l'enclave d'atterrissage sans aucune adresse IP publique.
* **Estimation :** 5 Story Points
* **Critères d'Acceptation (Given / When / Then) :**
  - **Given** les templates Terraform exécutés dans le pipeline CI/CD,  
    **When** le provisioning est terminé,  
    **Then** `publicNetworkAccess` doit être évalué à `Disabled` sur toutes les ressources.
  - **Given** une machine de test externe sur Internet,  
    **When** elle tente de résoudre les FQDNs du tenant,  
    **Then** aucune IP publique ne doit être retournée et le trafic doit être bloqué.

### User Story `NOVA-SEC-201`
* **Titre :** Chiffrement CMK sur Azure Key Vault Premium et Test du Kill-Switch $< 15\text{ min}$
* **Format :**  
  *En tant que* Security Engineer,  
  *Je souhaite* configurer une clé RSA 4096-bit protégée par HSM au sein d'Azure Key Vault Premium et automatiser la révocation d'accès,  
  *Afin de* respecter les exigences C2 MASSIF et d'être capable de neutraliser les données en cas d'incident critique.
* **Estimation :** 5 Story Points
* **Critères d'Acceptation :**
  - **Given** une clé maîtresse CMK active rattachée à la capacité Fabric,  
    **When** le script d'urgence de révocation est déclenché,  
    **Then** 100% des requêtes sur les modèles sémantiques doivent être bloquées en moins de 15 minutes.

### User Story `NOVA-MOD-301`
* **Titre :** Conversion du BillingCube en Modèle Déclaratif TMDL et Partitionnement Incrémental
* **Format :**  
  *En tant que* Lead BI Developer,  
  *Je souhaite* sérialiser la structure du BillingCube au format TMDL dans le dépôt Git avec une politique de rafraîchissement incrémental,  
  *Afin de* réduire le temps de traitement batch nocturne sous les 20 minutes.
* **Estimation :** 8 Story Points
* **Critères d'Acceptation :**
  - **Given** le modèle TMDL déployé via le pipeline XMLA,  
    **When** le batch nocturne s'exécute,  
    **Then** seules les données modifiées à J-1 doivent être rechargées en mémoire, avec une durée totale d'exécution $< 20\text{ minutes}$.

---

## 5. Definition of Done (DoD) Standardisée sur 5 Piliers

Pour que toute User Story soit déclarée "Done", elle doit impérativement respecter :
1. **Pilier Craft & Hexagone :** Cœur de domaine découplé à 100% de tout SDK externe ; modèles TMDL déclaratifs versionnés dans Git.
2. **Pilier Testabilité TDD :** Suite de tests unitaires purs s'exécutant en $< 3\text{ secondes}$ sans token ; zéro warning critique sur Tabular Editor Best Practice Analyzer (BPA).
3. **Pilier Sécurité C2 MASSIF :** 0 IP publique ; clés CMK HSM validées ; scans de code statique (Gitleaks, SonarQube) sans vulnérabilité haute/critique.
4. **Pilier Parité Financière :** Écart de calcul financier strictement égal à $0.000\%$ par rapport aux anciens cubes SSAS.
5. **Pilier Exploitation & Observabilité :** Logs d'accès streamés vers Microsoft Sentinel avec rétention immuable WORM 365 jours.
