# ÉTUDE STRATÉGIQUE DE MIGRATION CLOUD & ANALYSE FINOPS / TCO
## Comparatif Exhaustif des Pistes de Migration, Analyse des Coûts & Recommandation Arbitrée — Projet NovaAnalytics

**Référence :** FINOPS-STRAT-2026-NOVAA-001  
**Auteur :** Lead Cloud Migration Specialist & FinOps Architect  
**Destinataires :** Direction Générale, DSI, Direction Financière, Architecture Review Board (ARB)  
**Classification des Données :** C2 MASSIF  

---

## 1. Synthèse Exécutive du Cadrage FinOps

La migration du patrimoine décisionnel NovaAnalytics (actuellement hébergé sur 3 serveurs physiques SSAS On-Premise) vers le Cloud ne constitue pas une simple opération technique : il s'agit d'un **arbitrage économique et opérationnel structurant**.

L'étude financière et technique a évalué **4 trajectoires de migration distinctes**, depuis le réhébergement conservateur (*Lift & Shift*) jusqu'à la refonte en Lakehouse unifié.

```
                           [ ÉVENTAIL DES 4 PISTES DE MIGRATION CLOUD ]

    (1) IaaS Lift & Shift        (2) PaaS Managé            (3) SaaS Fabric / PBI         (4) Lakehouse Databricks
  +-------------------------+ +-------------------------+ +-------------------------+ +-------------------------+
  | VM Azure Esv5 Dédiées   | | Azure Analysis Services | | Modèles Sémantiques     | | Delta Lake / Unity Cat. |
  | SSAS On-Prem Transposé  | | Tier S-SKU (Standard)   | | Capacité F-SKU / PBI    | | Moteur Photon / SQL     |
  +-------------------------+ +-------------------------+ +-------------------------+ +-------------------------+
  | Coût Build : FAIBLE     | | Coût Build : MOYEN      | | Coût Build : MOYEN      | | Coût Build : TRÈS ÉLEVÉ |
  | Coût Run   : TRÈS ÉLEVÉ | | Coût Run   : ÉLEVÉ      | | Coût Run   : OPTIMISÉ   | | Coût Run   : ÉLEVÉ      |
  | Dette Tech : MAINTENUE  | | Pérennité  : OBSOLÈTE   | | Pérennité  : STRATÉGIQUE| | Pérennité  : AGNOSTIQUE |
  +-------------------------+ +-------------------------+ +-------------------------+ +-------------------------+
```

---

## 2. Analyse Comparative Détaillée des 4 Pistes de Migration

### 📊 Tableau Synthétique Multicritères & Coûts Estimés (TCO à 3 Ans)

| Critère d'Évaluation | Piste 1 : IaaS (Lift & Shift) | Piste 2 : PaaS (Azure Analysis Services) | Piste 3 : Modernisation Fabric / PBI | Piste 4 : Lakehouse Databricks / Snowflake |
| :--- | :--- | :--- | :--- | :--- |
| **Description Technique** | 3 VM Azure E16sv5 (128 Go RAM) avec SQL Server EE sous Windows Server. | 3 instances Azure Analysis Services (tier S4 ou S8v2) managées. | Capacité réservée Microsoft Fabric (F64/F128) avec Semantic Models TMDL. | Databricks SQL Serverless + Unity Catalog + Power BI Direct Lake / DirectQuery. |
| **Effort de Migration (Build)** | **Faible :** 40 à 60 J/H (Transposition VM, ExpressRoute). | **Moyen :** 80 à 110 J/H (Migration vers modèle tabulaire PaaS). | **Moyen :** 120 à 160 J/H (Conversion TMDL, intégration CI/CD). | **Très Élevé :** 250 à 350 J/H (Refonte complète pipelines & sémantique). |
| **Coût de Build Initial** | **35 000 € à 50 000 €** | **65 000 € à 90 000 €** | **95 000 € à 130 000 €** | **200 000 € à 280 000 €** |
| **Coût Run Annuel (Infra + Licences)** | **110 000 € à 145 000 € / an**<br>*(Licences SQL EE + VM 24/7 + Storage)* | **90 000 € à 120 000 € / an**<br>*(Instances S4/S8v2 sans élasticité fine)* | **65 000 € à 85 000 € / an**<br>*(Capacité F64 réservée 1 an + OneLake)* | **115 000 € à 160 000 € / an**<br>*(DBUs Databricks + VM compute + ADLS Gen2)* |
| **Coût d'Exploitation (MCO / No-Ops)** | **Élevé :** 30 000 € / an (Patching OS, backup, clusters HA manuels). | **Moyen :** 15 000 € / an (Administration brique PaaS isolée). | **Très Faible :** $< 5 000\text{ € / an}$ (Service managé sans VM ni OS). | **Moyen-Élevé :** 25 000 € / an (Expertise plateforme Lakehouse/Spark). |
| **TCO Global à 3 Ans (Min / Max)** | **395 000 € — 515 000 €** | **350 000 € — 465 000 €** | **🟢 305 000 € — 390 000 € (Le plus économique)** | **565 000 € — 785 000 €** |
| **Pérennité & Support Éditeur** | 🔴 Déclinante (Fin d'innovation SSAS). | 🔴 Obsolescence programmée par Microsoft. | 🟢 Maximale (Cœur stratégique Microsoft 2035+). | 🟢 Maximale (Standard ouvert Delta Lake). |
| **Conformité C2 MASSIF & Chiffrement** | Complexe (Hardening VM / BitLocker). | Partielle (VNet Injection limitée). | 🟢 Excellente (Private Link + CMK Key Vault). | 🟢 Excellente (Chiffrement CMK natif). |
| **Performance Requêtes Utilisateurs** | Moyenne (Contrainte mémoire des VM). | Bonne (Moteur In-Memory VertiPaq). | 🟢 Maximale ($< 3\text{ s}$ en VertiPaq / Direct Lake). | Variable selon clusters chauds/froids. |

---

### 🔍 Fiches d'Évaluation par Trajectoire

#### Piste 1 : Réhébergement IaaS (Lift & Shift sur Machines Virtuelles Cloud)
* **Les « Pour » (+)** :  
  + Délais de bascule très courts (migration brute d'images disques ou sauvegarde/restauration SSAS).
  + Zéro perturbation pour les développeurs de requêtes existantes.
* **Les « Contre » (-)** :  
  - **Fausse économie Cloud :** Aucune élasticité ; les VM doivent rester allumées en permanence.
  - Double peine financière : paiement de l'infrastructure Cloud PLUS des licences SQL Server Enterprise avec Software Assurance.
  - Conservation intégrale de la dette technique (patching Windows, vulnérabilités OS, gestion des pannes matérielles virtuelles).
* **Verdict FinOps :** **NON RECOMMANDÉ** (TCO le plus défavorable sur la durée sans aucun gain de valeur métier).

#### Piste 2 : Replatforming PaaS (Azure Analysis Services - AAS)
* **Les « Pour » (+)** :  
  + Suppression des tâches d'administration du système d'exploitation Windows.
  + Compatibilité directe avec les modèles tabulaires existants.
* **Les « Contre » (-)** :  
  - **Impasse technologique :** Microsoft n'investit plus sur AAS et oriente tous ses clients vers Fabric / Power BI Premium.
  - Grille tarifaire rigide : le passage d'une instance S4 à S8 double instantanément la facture sans granularité fine.
* **Verdict FinOps :** **À PROSCRIRE** (Investir du budget en 2026 sur un produit en fin de vie commerciale est une faute de gestion).

#### Piste 3 : Modernisation Cloud-Native (Microsoft Fabric / Modèles Sémantiques PBI) — RECOMMANDÉ
* **Les « Pour » (+)** :  
  + **TCO le plus bas à 3 ans :** Mutualisation des trois cubes au sein d'une enveloppe de capacité réservée (ex : F64 ou P1) avec lissage de charge.
  + Mode *No-Ops* réel : Zéro serveur à patcher, sauvegardes et haute disponibilité gérées nativement.
  + Intégration fluide avec Power BI sans couche intermédiaire inutile.
  + Mode déclaratif TMDL permettant un déploiement continu à coût d'intégration nul.
* **Les « Contre » (-)** :  
  - Nécessite l'arbitrage prudent recommandé par le Challenger : **utiliser le moteur VertiPaq en mode Import partitionné** pour sécuriser les temps de réponse comptables, et réserver Direct Lake aux données de facturation volumineuses.
* **Verdict FinOps :** **MEILLEUR CHOIX STRATÉGIQUE & ÉCONOMIQUE (ROI amorti dès le 14e mois)**.

#### Piste 4 : Architecture Lakehouse Unifiée (Databricks / Snowflake)
* **Les « Pour » (+)** :  
  + Zéro dépendance vis-à-vis des composants propriétaires Microsoft (indépendance multi-cloud).
  + Puissance de calcul illimitée pour de la Data Science avancée.
* **Les « Contre » (-)** :  
  - **Sur-ingénierie et surcoût massif pour le besoin exprimé :** Coûts de Build exorbitants (> 200 k€) et complexité d'ingénierie disproportionnée pour un parc de 3 cubes décisionnels financiers.
* **Verdict FinOps :** **REJETÉ POUR SUR-DIMENSIONNEMENT (Principe YAGNI)**.

---

## 3. Plan d'Action & Trajectoire de Bascule Recommandée

Pour minimiser les risques financiers et techniques, nous recommandons une bascule progressive en **4 étapes jalonnées** :

```
[ Mois 1 : Socle Sécurisé ] ──► [ Mois 2 : Pilote Facturation ] ──► [ Mois 3-4 : Bascule Compta ] ──► [ Mois 5 : Extinction ]
  • Landing Zone Private Link    • Migration BillingCube             • Migration LedgerCube (Sanctuarisé) • Décommissionnement
  • Azure Key Vault Premium CMK  • Validation batch < 20 min         • Migration RecoveryCube (RLS/DCP)   • Arrêt définitif des VM
  • Validation DCA de Sécurité   • Recette P95 < 3s Power BI         • Double Run financier (0 écart)     • Gain FinOps effectif
```

1. **Jalon 1 (Mois 1 — 25 k€) :** Déploiement du socle sécurisé Terraform (VNet Spoke, Private Endpoints, Azure Key Vault Premium avec clés CMK) et levée des réserves CISO (homologation DCA).
2. **Jalon 2 (Mois 2 — 35 k€) :** Migration pilote du **BillingCube** vers un modèle sémantique optimisé (validation du gain de temps d'ingestion nocturne $< 20\text{ minutes}$).
3. **Jalon 3 (Mois 3-4 — 55 k€) :** Migration du **LedgerCube** (avec capacité sanctuarisée pour les clôtures) et du **RecoveryCube** (avec pseudonymisation SHA-256 des débiteurs). Période de *Double-Run* comptable de 30 jours (tolérance de variance = 0.000%).
4. **Jalon 4 (Mois 5) :** Décommissionnement physique définitif des 3 serveurs On-Premise. **Économie annuelle récurrente constatée : ~ 60 000 € / an**.
