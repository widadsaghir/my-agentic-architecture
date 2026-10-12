# DOSSIER D'ARCHITECTURE TECHNIQUE PRÉLIMINAIRE (DAT)
## Modernisation du Socle Décisionnel SSAS vers le Cloud — Projet NovaAnalytics

**Date d'émission :** 12 octobre 2026  
**Auteur :** Solution & Infrastructure Architect  
**Classification des Données :** C2 MASSIF  
**Statut :** Livrable d'Architecture Technique Préliminaire — Pour passage en ARB  

---

## 1. Synthèse du besoin & Vision d'architecture (Phase A TOGAF)

### 1.1 Contexte Métier & Limites de l'Existant (AS-IS)
Le socle décisionnel **NovaAnalytics** constitue l'épine dorsale du pilotage financier de l'organisation. L'infrastructure actuelle héberge trois cubes analytiques distincts sur des machines virtuelles dédiées sur site (*On-Premise*) :
*   **BillingCube :** Analyse de la facturation et des flux transactionnels d'émission.
*   **RecoveryCube :** Gestion du recouvrement, contentieux, et calcul du risque de défaut.
*   **LedgerCube :** Clôtures comptables, grand livre et consolidation financière.

Cette architecture AS-IS présente des limites structurelles majeures :
*   **Goulot d'étranglement matériel & passage à l'échelle vertical :** Incapacité à absorber l'accroissement des volumes sans surdimensionner coûteusement les VM On-Premise (saturation RAM/CPU lors des retraitements nocturnes).
*   **Dette technique et obsolescence logicielle :** Les instances SSAS traditionnelles limitent l'agilité fonctionnelle, freinent l'intégration native avec les outils modernes de Data Science et complexifient la maintenance.
*   **Latence de mise à disposition :** La dépendance vis-à-vis de traitements batch monolithiques entraîne des fenêtres de chargement critiques incompatibles avec le besoin de reporting quasi temps-réel formulé par les directions financières via Power BI.

### 1.2 Vision de l'Architecture Cible
La vision d'architecture s'inscrit dans les principes de l'**Architecture Phase A (TOGAF)** :
*   **Découplage strict entre le stockage de données, le moteur de calcul analytique et le modèle sémantique de consommation.**
*   **Transition vers un modèle orienté services managés / Cloud-Native**, réduisant le coût opérationnel d'infrastructure (*No-Ops / Low-Ops* sur la couche OS/SGBD) tout en maximisant la scalabilité élastique.
*   **Homogénéisation du delivery décisionnel :** Convergence vers une plateforme sémantique unifiée exposée sans couture vers Power BI, supportant le mode *In-Memory* et/ou *Direct Lake* sans duplication inutile de données.
*   **Conformité Zero-Trust native :** Aucune surface d'exposition publique, intégration réseau hybride sécurisée et gestion des accès ultra-fine.

---

## 2. Exigences clés & Besoins Non-Fonctionnels (NFR)

Au regard de la classification **C2 MASSIF**, les exigences non-fonctionnelles sont critiques et non négociables :

| Domaine NFR | Exigence Spécifique | Cible Métrique / Standard |
| :--- | :--- | :--- |
| **Sécurité C2** | Cloisonnement réseau & chiffrement | 0 IP publique (Private Endpoints exclusifs), TLS 1.3 forcé, CMK sur HSM FIPS 140-2 Niv 3 |
| **Scalabilité** | Volumétrie financière & concurrence | > 500M lignes, 300 utilisateurs PBI simultanés ($P95 < 3\text{ s}$), batch $< 2\text{ h}$ |
| **Résilience** | Continuité d'activité financière | RTO $< 4\text{ heures}$, RPO $< 1\text{ heure}$, déploiement Zone-Redundant multi-AZ |
| **Exploitation** | DevSecOps & Architecture as Code | Format déclaratif TMDL, GitOps, 0 secret statique (OIDC), logs SIEM WORM 365j |

---

## 3. Évaluation des Scénarios d'Architecture

### 3.1 Option 1 : Réhébergement IaaS (Lift & Shift)
*   **Description :** Transposition des 3 VM SSAS On-Premise vers des machines virtuelles Azure (série Esv5 optimisée mémoire) interconnectées par ExpressRoute.
*   **Avantages :** Risque fonctionnel initial faible (code SSAS inchangé).
*   **Inconvénients :** Dette technique conservée, licences SQL Server Enterprise coûteuses, fardeau d'exploitation élevé (patching, backups, clusters manuels).

### 3.2 Option 2 : Replatforming PaaS Managé (Azure Analysis Services - AAS)
*   **Description :** Migration des modèles vers des instances managées Azure Analysis Services.
*   **Avantages :** Suppression de l'administration système et des VM.
*   **Inconvénients :** Fin de cycle de vie annoncée par Microsoft (produit gelé), pas de mode Direct Lake, coût élevé des tiers S8/S9.

### 3.3 Option 3 : Modernisation Cloud-Native / Lakehouse Sémantique Unifié (Recommandé)
*   **Description :** Modernisation via l'écosystème unifié **Microsoft Fabric** (Capacité F-SKU dédiée) ou **Modèles Sémantiques Power BI Premium**, adossés à OneLake (tables Delta Parquet avec chiffrement CMK).
*   **Avantages :** Performances In-Memory / Direct Lake sans recopie de données, pérennité jusqu'en 2035+, gouvernance native unifiée Purview, intégration native Git/TMDL.
*   **Points d'attention :** Nécessite une conversion des modèles vers le format tabulaire et un dimensionnement rigoureux de la capacité.

---

## 4. Architecture Réseau Hybride Zero-Trust (Schémas Associés)

L'interconnexion sécurisée repose sur :
1. **Liaison Hybride Sécurisée :** Connexion dédiée **Azure ExpressRoute** privée avec chiffrement physique MACsec activé sur le port réseau.
2. **Passerelle d'Ingestion :** Cluster d'**On-Premises Data Gateways (OPDG)** ou Integration Runtimes managés en multi-AZ dans le VNet Spoke.
3. **Isolation Complète :** Utilisation exclusive d'**Azure Private Endpoints (Private Link)** pour OneLake, Power BI Service et Azure Key Vault.
4. **Schémas sources disponibles :**
   - Schéma existant : `diagrams/architecture_as_is.drawio` (`.puml`, `.mmd`)
   - Schéma cible : `diagrams/architecture_to_be.drawio` (`.puml`, `.mmd`)

---

## 5. Chaîne CI/CD & Modélisation Déclarative TMDL
* **Format déclaratif TMDL (Tabular Model Definition Language)** : Versionné sous Git, remplaçant les vieux fichiers `.bim` monolithiques.
* **Pipeline DevSecOps** : Tabular Editor CLI avec *Best Practice Analyzer* (BPA), scan anti-secrets Gitleaks, et déploiement continu XMLA via identité fédérée OIDC.
