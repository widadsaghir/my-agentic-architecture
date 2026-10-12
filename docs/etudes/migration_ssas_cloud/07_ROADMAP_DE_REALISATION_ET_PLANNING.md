# FEUILLE DE ROUTE DE RÉALISATION, PLANNING GANTT & JALONS (ROADMAP)
## Trajectoire Industrielle de Migration Cloud — Projet NovaAnalytics

**Référence :** ROADMAP-REAL-2026-NOVAA-001  
**Auteur :** Lead Enterprise Architect & SAFe Release Train Engineer (RTE)  
**Destinataires :** Directeurs de Projet, PMO, Product Owners, Tech Leads, Équipes de Build  
**Durée Globale :** 5 Mois (20 Semaines / 10 Sprints de 2 semaines)  
**Budget Alloué :** 115 000 € (Build)  

---

## 1. Diagramme de Gantt Prévisionnel (Mermaid)

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title Planning de Réalisation — Migration Décisionnelle Cloud (NovaAnalytics)
    excludes    weekends

    section JALON 1 : Socle & DCA (Mois 1)
    Déploiement Landing Zone Terraform & VNet Spoke   :done,    j1_1, 2026-11-02, 10d
    Configuration Azure Key Vault Premium & CMK HSM    :done,    j1_2, after j1_1, 5d
    Mise en place ExpressRoute MACsec & Private Links  :active,  j1_3, after j1_1, 10d
    Validation Homologation Sécurité DCA (CISO)        :crit,    j1_4, after j1_2, 5d
    JALON GO / NO-GO 1 : Socle Sécurisé Homologué      :milestone, m1, 2026-11-27, 0d

    section JALON 2 : Pilote Facturation (Mois 2)
    Modélisation Déclarative TMDL du BillingCube       :         j2_1, after m1, 10d
    Mise en place Usine CI/CD Tabular Editor BPA       :         j2_2, after m1, 8d
    Test Batch Ingestion Incrémentale OneLake (<20m)   :         j2_3, after j2_1, 7d
    Recette Utilisateurs Power BI (P95 < 3s)           :crit,    j2_4, after j2_3, 5d
    JALON GO / NO-GO 2 : Pilote Facturation en Prod    :milestone, m2, 2026-12-31, 0d

    section JALON 3 : Bascule Compta & Recouvrement (Mois 3-4)
    Modélisation TMDL RecoveryCube & RLS SHA-256 (DCP) :         j3_1, after m2, 12d
    Sanctuarisation Capacité Dédiée LedgerCube (Compta):         j3_2, after m2, 10d
    Campagne de Double-Run Financier (30 jours)        :crit,    j3_3, 2027-01-25, 25d
    Contrôle Zéro Écart (Variance = 0.000%)            :crit,    j3_4, after j3_3, 5d
    JALON GO / NO-GO 3 : Bascule Définitive Finance    :milestone, m3, 2027-03-05, 0d

    section JALON 4 : Décommissionnement (Mois 5)
    Arrêt des Traitements Batchs On-Premise            :         j4_1, after m3, 5d
    Sauvegarde d'Archivage Froid WORM Légale (10 ans)  :         j4_2, after j4_1, 5d
    Extinction Physique des 3 VM SSAS                  :crit,    j4_3, after j4_2, 5d
    JALON FINAL : Décommissionnement & Économies Actées:milestone, m4, 2027-03-26, 0d
```

---

## 2. Découpage Détaillé par Phase & Sprints

### 🔵 PHASE 1 : Fondations Sécurisées, Réseau & Homologation DCA (Sprint 1 & 2 — Mois 1)
* **Sprint 1 (S1-S2) :**
  - Provisioning de la Landing Zone Azure via Terraform (VNet Spoke, Subnets dédiés, NSG durcis).
  - Interconnexion ExpressRoute avec chiffrement matériel MACsec et peering privé.
  - Déploiement d'Azure Key Vault Premium avec clé maîtresse RSA 4096-bit protégée par HSM (FIPS 140-2 Niveau 3).
* **Sprint 2 (S3-S4) :**
  - Déploiement des Private Endpoints pour OneLake, Fabric et Key Vault (`publicNetworkAccess = Disabled`).
  - Implémentation et test du script d'urgence de révocation de clé (**Kill-Switch en $< 15\text{ minutes}$**).
  - Revue formelle CISO et signature de l'**Homologation d'Architecture DCA**.
* **Livrable & Porte d'Arrêt :** ✅ **Jalon Go/No-Go 1 (Socle Homologué)**.

---

### 🟢 PHASE 2 : Industrialisation CI/CD & Pilote Facturation (Sprint 3 & 4 — Mois 2)
* **Sprint 3 (S5-S6) :**
  - Mise en place du pipeline GitLab/Azure DevOps avec intégration OIDC (zéro secret statique dans Git).
  - Automatisation du linter *Tabular Editor Best Practice Analyzer* (BPA) et scan Gitleaks.
  - Reverse-engineering et conversion de la structure du *BillingCube* au format déclaratif **TMDL**.
* **Sprint 4 (S7-S8) :**
  - Configuration du rafraîchissement incrémental XMLA (seules les données de la veille sont rechargées).
  - Validation de la fenêtre d'ingestion nocturne : **durée constatée $< 20\text{ minutes}$** (vs 6h auparavant).
  - Banc de test de performance avec 300 utilisateurs Power BI concurrents ($P95 < 3\text{ secondes}$).
* **Livrable & Porte d'Arrêt :** ✅ **Jalon Go/No-Go 2 (Mise en service opérationnelle du BillingCube)**.

---

### 🟡 PHASE 3 : Bascule Comptabilité, Recouvrement & Double-Run (Sprint 5 à 8 — Mois 3 & 4)
* **Sprint 5 & 6 (S9-S12) :**
  - Modélisation TMDL du *RecoveryCube* avec implémentation de la pseudonymisation SHA-256 salée des débiteurs et sécurité fine Row-Level Security (RLS) conforme RGPD.
  - Modélisation du *LedgerCube* (Grand Livre) et sanctuarisation d'une capacité dédiée pour isoler les clôtures financières de tout risque de contention.
* **Sprint 7 & 8 (S13-S16) :**
  - **Campagne de Double-Run financier de 30 jours consécutifs** : exécution simultanée des clôtures sur SSAS On-Premise et sur les nouveaux modèles Cloud.
  - Audit automatisé des balances et états financiers : **contrôle strict d'une variance égale à 0.000%**.
* **Livrable & Porte d'Arrêt :** ✅ **Jalon Go/No-Go 3 (Validation formelle des Commissaires aux Comptes et Directeurs Financiers)**.

---

### 🔴 PHASE 4 : Décommissionnement Définitif & Clôture FinOps (Sprint 9 & 10 — Mois 5)
* **Sprint 9 (S17-S18) :**
  - Bascule définitive de 100% des rapports Power BI utilisateurs vers les nouveaux modèles sémantiques.
  - Coupure des flux batchs ETL alimentant les serveurs On-Premise.
  - Export d'archivage froid conforme aux obligations légales de conservation des écritures (WORM 10 ans).
* **Sprint 10 (S19-S20) :**
  - Extinction électrique et décommissionnement physique des 3 serveurs physiques/VM On-Premise.
  - Résiliation des licences SQL Server Enterprise et des contrats de maintenance associés.
  - Constat officiel de l'économie FinOps récurrente de **60 000 € / an**.
* **Livrable Final :** 🏆 **Projet NovaAnalytics clôturé avec succès**.

---

## 3. Matrice RACI du Projet

| Tâche / Livrable Majeur | Lead Architect | Tech Lead BI | DevSecOps Lead | RSSI / CISO | Product Owner Finance |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Cadrage Architecture & Choix Cible** | **A / R** | C | C | C | I |
| **Homologation de Sécurité DCA** | C | I | C | **A / R** | I |
| **Déploiement Landing Zone Terraform** | C | I | **A / R** | C | I |
| **Modélisation TMDL & DAX** | C | **A / R** | C | I | C |
| **Pipeline CI/CD & Tabular Editor BPA** | I | C | **A / R** | C | I |
| **Double-Run & Recette Financière (0%)** | C | C | I | I | **A / R** |
| **Extinction & Décommissionnement** | **A** | R | R | I | C |

*Légende : **A** = Accountable (Décideur/Responsable final), **R** = Responsible (Réalisateur), **C** = Consulted (Consulté), **I** = Informed (Informé).*

---

## 4. Consommation Budgétaire Prévisionnelle par Jalon

```
+-----------------------------------------------------------------------------------------+
| JALON                  | EFFORT ESTIMÉ | BUDGET ALLOUÉ | CUMUL BUDGET  | LIVRABLE VALIDÉ|
+------------------------+---------------+---------------+---------------+----------------+
| Jalon 1 (Fondations)   | 35 J/H        | 25 000 €      | 25 000 €      | Visa DCA CISO  |
| Jalon 2 (Pilote Fact.) | 45 J/H        | 35 000 €      | 60 000 €      | Batch < 20 min |
| Jalon 3 (Compta/Double)| 70 J/H        | 55 000 €      | 115 000 €     | Variance 0.000%|
| Jalon 4 (Extinction)   | 10 J/H        | Inclus MCO    | 115 000 €     | -60 k€/an gain |
+------------------------+---------------+---------------+---------------+----------------+
| TOTAL PROJET BUILD     | 160 J/H       | 115 000 €     | 115 000 €     | ROI à 14 mois  |
+-----------------------------------------------------------------------------------------+
```
