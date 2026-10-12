# BACKLOG D'IMPLÉMENTATION TECHNIQUE SAFe & JIRA
**Projet :** NovaAnalytics — Modernisation du socle décisionnel (SSAS ➔ Cloud)  
**Classification :** C2 MASSIF  
**Rôle :** SAFe System Architect & Agile Delivery Enabler  
**Langue :** Français  

---

## 1. Fiche Enabler Epic

```
===================================================================================================
                                      SAFe ENABLER EPIC
===================================================================================================
```

* **Identifiant :** `EPIC-ENABLER-01`
* **Titre :** Modernisation Cloud-Native Sécurisée et Hybride du Socle Décisionnel NovaAnalytics (C2 MASSIF)
* **Type :** Architecture & Infrastructure Enabler
* **Périmètre ART :** Train Décisionnel & Plateforme Hybride (ART Nova)
* **Propriétaire :** System Architect / Solution Architect
* **Statut de Gouvernance :** Approuvé en ARB / Prêt pour PI Planning

### Hypothèse de Valeur (Business Outcome Hypothesis)
En migrant les trois cubes multidimensionnels/tabulaires on-premise (*LedgerCube*, *RecoveryCube*, *BillingCube*) vers une architecture hexagonale modulaire et une infrastructure cloud unifiée (*Microsoft Fabric / OneLake / Semantic Models*) entièrement cloisonnée en réseau privé (Zero-Trust, chiffrée en CMK FIPS 140-2 Niveau 3) :
1. Nous éliminerons les goulots d'étranglement de scalabilité mémoire et CPU lors des arrêtés nocturnes et clôtures comptables, abaissant la fenêtre d'ingestion globale de 6h à moins de 2h.
2. Nous réduirons à moins de 3 secondes le temps de restitution interactif pour 300 utilisateurs financiers simultanés.
3. Nous garantirons la stricte conformité réglementaire bancaire/financière et RGPD (C2 MASSIF) par l'étanchéité des endpoints réseau, la pseudonymisation à la source des créances et l'automatisation GitOps en format déclaratif TMDL.

### Métriques de Succès & Indicateurs Avancés (Leading Indicators)
* **Performance de Restitution :** $P95 < 3\text{ s}$ sur l'exécution des requêtes DAX complexes en concurrence nominale (300 requêtes concurrentes).
* **Fenêtre de Traitement Batch :** Durée totale de rafraîchissement partitionné $< 120\text{ minutes}$ (contre 360 min initialement).
* **Zero-Trust Network Exposure :** $0$ adresse IP publique exposée, $100\%$ des flux d'ingestion et de consommation routés exclusivement via Azure Private Link / Private Endpoints.
* **Résilience Cryptographique (Kill Switch) :** Révocation et isolation totale des accès aux modèles de données en $< 15\text{ minutes}$ via désactivation de la KEK dans Azure Key Vault.
* **Qualité du Delivery Logiciel :** Couverture de tests unitaires sur le domaine pur $> 95\%$, exécution de la suite de tests de domaine $< 3\text{ secondes}$, $0$ avertissement *Tabular Editor Best Practice Analyzer (BPA)* et $0$ faille critique/haute aux scans SAST/IaC.

### Portée (Scope)
* **In-Scope :**
  * Atterrissage Landing Zone Azure durcie (VNet, Spoke, Private Endpoints, Azure Key Vault Premium HSM, ExpressRoute privé avec MACsec).
  * Implémentation du pattern d'Architecture Hexagonale (DDD) pour l'ingestion, le calcul des règles de gestion financière, et la pseudonymisation C2 MASSIF.
  * Usine logicielle CI/CD déclarative TMDL via OIDC / Managed Identities (GitOps, Tabular Editor CLI, non-régression DAX).
  * Migration des trois cubes : *LedgerCube* (priorité intégrité comptable/SOX), *RecoveryCube* (priorité sécurisation DCP/RGPD), *BillingCube* (priorité volumétrie/partitionnement).
  * Branchement SIEM / Log Analytics avec audit immuable (WORM 365 jours).
* **Out-of-Scope :**
  * Refonte UX des rapports Power BI front-end métiers (périmètre des équipes BI Features/Produit).
  * Remplacement des bases de données sources OLTP On-Premise.
  * Déploiement multi-région hors UE (interdiction formelle de sortir de la région `Azure France Central`).

---

## 2. Matrice des Enabler Features Priorisées (WSJF)

Le calcul du **WSJF (Weighted Shortest Job First)** repose sur la formule SAFe standard :
$$\text{WSJF} = \frac{\text{Cost of Delay (CoD)}}{\text{Job Size}} = \frac{\text{User-Business Value (UBV)} + \text{Time Criticality (TC)} + \text{Risk Reduction / Opp. Enablement (RR/OE)}}{\text{Job Size}}$$

Échelle de notation de type suite de Fibonacci modifiée (1, 2, 3, 5, 8, 13, 20).

| Feature ID | Titre de l'Enabler Feature | UBV | TC | RR/OE | CoD | Job Size | Score WSJF | Cible PI |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FEAT-01** | **Socle Landing Zone Zero-Trust, Private Link & Chiffrement CMK C2** | 8 | 13 | 20 | **41** | 5 | **8.20** | **PI 1** |
| **FEAT-02** | **Usine Logicielle DevSecOps & Pipeline CI/CD Déclaratif TMDL / GitOps** | 8 | 8 | 13 | **29** | 5 | **5.80** | **PI 1** |
| **FEAT-03** | **Architecture Hexagonale & Moteur de Domaine Déterministe (DDD Pure Engine)** | 13 | 5 | 13 | **31** | 8 | **3.88** | **PI 1 - PI 2** |
| **FEAT-04** | **Migration & Sécurisation Critique du LedgerCube (Intégrité SOX)** | 20 | 13 | 8 | **41** | 8 | **5.13** | **PI 2** |
| **FEAT-05** | **Ingestion Pseudonymisée & Modélisation Sécurisée du RecoveryCube (RGPD)** | 13 | 8 | 13 | **34** | 8 | **4.25** | **PI 2 - PI 3** |
| **FEAT-06** | **Pipeline Haute Volumétrie & Partitionnement du BillingCube** | 8 | 5 | 5 | **18** | 5 | **3.60** | **PI 3** |

### Dépendances Techniques Majeures
* `FEAT-01` et `FEAT-02` sont les prérequis structurels (*hard dependencies*) pour toute exécution en environnement Azure et déploiement de modèles.
* `FEAT-03` fournit les interfaces et les Value Objects métiers indispensables au respect des invariants de `FEAT-04` et `FEAT-05`.
* `FEAT-04` conditionne la validation d'homologation de conformité financière (clôture comptable légale).

---

## 3. Backlog Détaillé des User Stories Jira Techniques

---

### FEATURE FEAT-01 : Socle Landing Zone Zero-Trust, Private Link & Chiffrement CMK C2

#### Story Jira `US-TECH-01.1` : Provisioning Terraform du Hub/Spoke, Private Endpoints et Extinction Réseau Public
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-01`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant qu'** Ingénieur Cloud Platform / DevSecOps,  
  > **Je souhaite** déployer l'enclave réseau Spoke Azure, les Private Endpoints pour OneLake, Fabric et Key Vault, en désactivant tout point d'accès public,  
  > **Afin de** respecter le principe Zero-Trust (NIST SP 800-207) et éliminer l'exposition internet des données financières C2 MASSIF.

* **Critères d'Acceptation Opérationnels :**
  1. Le code Terraform provisionne le VNet Spoke dans la région `France Central` sans passerelle internet publique (`0.0.0.0/0` routé vers une appliance pare-feu interne ou drop par défaut).
  2. Les Private Endpoints (`pep-onelake`, `pep-powerbi-xmla`, `pep-keyvault`) sont créés avec leurs cartes réseaux (NIC) associées dans le sous-réseau `snet-private-endpoints`.
  3. L'argument `public_network_access_enabled = false` est validé sur l'ensemble des ressources compatibles du template.
  4. Les zones DNS privées (`privatelink.analysis.windows.net`, `privatelink.vaultcore.azure.net`, `privatelink.pbidedicated.windows.net`) sont intégrées et résolubles depuis le cluster de build et le VNet hybride.
  5. Un scan statique Checkov/Tfsec passe en pipeline avec $0$ violation de sévérité Haute ou Critique.

---

#### Story Jira `US-TECH-01.2` : Configuration d'Azure Key Vault Premium HSM, CMK et Procédure de Kill Switch
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-01`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant que** Responsable Sécurité des Systèmes d'Information (RSSI / Architecte Sécurité),  
  > **Je souhaite** instancier un coffre Azure Key Vault Premium FIPS 140-2 Niveau 3 avec purge protection, générer une clé de chiffrement KEK RSA 4096 bits et implémenter un script de révocation d'urgence,  
  > **Afin de** satisfaire les contraintes cryptographiques C2 MASSIF et permettre l'isolation des données en moins de 15 minutes en cas d'intrusion.

* **Critères d'Acceptation Opérationnels :**
  1. Le Key Vault est provisionné en SKU `Premium` avec activation obligatoire des drapeaux `enable_soft_delete = true` et `purge_protection_enabled = true`.
  2. Une clé KEK RSA 4096 bits (`cmk-fabric-nova-prod`) est générée, protégée par le module HSM matériel (FIPS 140-2 Niveau 3).
  3. La rotation automatique des clés est planifiée avec une politique d'expiration de 180 jours.
  4. L'accès au plan de données Key Vault est strictement confié au Service Principal du tenant Fabric via RBAC Azure (`Key Vault Crypto Service Encryption User`), sans clés secrètes statiques.
  5. **Vérification du Kill Switch :** Un runbook automatisé (Azure CLI/PowerShell) révoque les permissions ou désactive la clé KEK. Le test démontre que les accès XMLA et de requêtage aux cubes renvoient un code d'erreur de chiffrement dans un délai chronométré $\le 15\text{ minutes}$.

---

#### Story Jira `US-TECH-01.3` : Raccordement Hybride Sécurisé ExpressRoute MACsec & Cluster Passerelle Managée
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-01`
* **Points d'estimation (Story Points) :** 3
* **Format Jira :**
  > **En tant qu'** Ingénieur Réseau Hybride,  
  > **Je souhaite** configurer le peering privé ExpressRoute avec chiffrement MACsec activé et raccorder le cluster de runtime managé (Managed Private VNet),  
  > **Afin de** sécuriser les transferts de données transactionnelles depuis les bases on-premise sans transiter par des VM passerelles non étanches.

* **Critères d'Acceptation Opérationnels :**
  1. Le chiffrement de liaison de données IEEE 802.1AE (MACsec) est vérifié actif sur les interfaces de peering ExpressRoute physiques reliant le Datacenter à l'infrastructure Azure.
  2. Aucun composant IaaS d'ingestion n'expose de port de gestion (RDP/SSH) sur des réseaux externes.
  3. Les routes UDR (User Defined Routes) et les règles de NSG appliquent une politique de rejet par défaut (*Deny-All*) autorisant uniquement le protocole TDS (port 1433/TCP) vers les serveurs de bases de données internes du système financier.
  4. Le test de charge réseau confirme le transit sans perte de paquets pour un débit minimal garanti de $2\text{ Gbps}$ pendant les fenêtres de réplication batch.

---

### FEATURE FEAT-02 : Usine Logicielle DevSecOps & Pipeline CI/CD Déclaratif TMDL / GitOps

#### Story Jira `US-TECH-02.1` : Chaîne de Contrôle Qualité Statique CI (TMDL Linter, BPA & Scan Secret Gitleaks)
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-02`
* **Points d'estimation (Story Points) :** 3
* **Format Jira :**
  > **En tant que** Lead Développeur BI / Artisan DevSecOps,  
  > **Je souhaite** automatiser les contrôles statiques Tabular Editor BPA et le scan de secrets au déclenchement de chaque Pull Request sur le dépôt de modèles TMDL,  
  > **Afin de** bloquer les non-conformités de modélisation, les failles d'optimisation DAX et les fuites d'identifiants avant tout merge.

* **Critères d'Acceptation Opérationnels :**
  1. Le pipeline CI s'exécute sur Azure DevOps / GitLab CI à l'ouverture de toute PR ciblant la branche `main`.
  2. Un scan Gitleaks s'exécute en pré-validation : la présence du moindre mot de passe, clé SAS, token ou chaîne de connexion brute échoue immédiatement le build (code de sortie $\ne 0$).
  3. L'utilitaire Tabular Editor CLI exécute le *Best Practice Analyzer (BPA)* sur l'ensemble de l'arborescence TMDL du projet.
  4. Toute règle de sévérité 1 ou 2 (règles de performance DAX, colonnes invisibles non masquées, typage erroné, absence de hiérarchie temporelle) bloque le pipeline avec affichage détaillé des lignes TMDL en faute.
  5. La durée d'exécution totale de cette étape de validation CI n'excède pas 90 secondes.

---

#### Story Jira `US-TECH-02.2` : Pipeline CD de Déploiement Déclaratif via XMLA & Fédération d'Identité OIDC
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-02`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant que** Release Train Engineer (RTE) / Architecte Solution,  
  > **Je souhaite** déployer automatiquement les artefacts de modèles tabulaires TMDL validés vers les espaces de travail Fabric dédiés via l'endpoint XMLA en utilisant l'authentification Workload Identity (OIDC),  
  > **Afin de** supprimer le stockage de tokens statiques dans la CI/CD et garantir un déploiement continu zéro-downtime des métadonnées.

* **Critères d'Acceptation Opérationnels :**
  1. Aucune variable secrète (`client_secret`) n'est configurée dans les paramètres de la CI/CD ; l'authentification auprès de Microsoft Entra ID s'effectue exclusivement via Workload Identity Federation (jeton éphémère OIDC).
  2. Le déploiement TMDL compile le modèle de métadonnées et met à jour l'espace de travail cible via les API XMLA (`Microsoft.AnalysisServices.Tabular`).
  3. Le déploiement s'opère sans interruption de requêtage pour les utilisateurs en cours de consultation (*Zero Downtime Metadata Refresh*).
  4. Le statut de la validation et l'empreinte Git (SHA-1 du commit déployé) sont tagués dans les métadonnées de description du modèle sémantique.
  5. Les accès au pipeline de déploiement en production nécessitent l'approbation formelle de deux relecteurs désignés (revue par les pairs obligatoire).

---

### FEATURE FEAT-03 : Socle Cœur Hexagonal & Moteur de Domaine Déterministe (DDD Pure Engine)

#### Story Jira `US-TECH-03.1` : Modélisation DDD Pure du Cœur Métier `FinancialLedger` & Value Objects Immuables
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-03`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant qu'** Artisan Développeur Cœur de Domaine,  
  > **Je souhaite** implémenter l'Agrégat `LedgerBook`, ses entités internes et les Value Objects immuables (`Money`, `Currency`, `LedgerAccountCode`) dans une bibliothèque .NET exempte de tout framework technique,  
  > **Afin de** garantir formellement l'intégrité de la partie double comptable et l'immutabilité des clôtures de façon 100% déterministe.

* **Critères d'Acceptation Opérationnels :**
  1. Le projet `NovaAnalytics.Domain` ne possède aucune dépendance binaire vers `Microsoft.Data.*`, `Azure.*`, `EntityFramework`, ou tout package réseau/HTTP.
  2. Le Value Object `Money` utilise un type numérique décimal à virgule fixe (128-bit) avec arrondi bancaire (*MidpointRounding.AwayFromZero*) et interdit les calculs inter-devises non explicites.
  3. L'Agrégat `LedgerBook` empêche l'ajout de toute écriture (`AccountingEntry`) dès lors que son état est basculé à `IsClosed = true`, en levant une exception `DomainInvariantViolationException`.
  4. La méthode `ConsolidateAndClose()` valide l'invariant absolu : $\sum \text{Débits} - \sum \text{Crédits} = 0$. Tout écart lève une `UnbalancedLedgerException`.
  5. Des tests d'architecture automatisés (*NetArchTest*) sont intégrés pour échouer la compilation si un composant d'infrastructure est référencé dans le domaine.

---

#### Story Jira `US-TECH-03.2` : Spécification des Ports d'Entrée/Sortie et Double de Test en Mémoire (Spies/Stubs)
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-03`
* **Points d'estimation (Story Points) :** 3
* **Format Jira :**
  > **En tant qu'** Artisan Développeur Applicatif,  
  > **Je souhaite** définir les interfaces formelles des Ports Hexagonaux (`ILedgerPersistencePort`, `IAuditEventPublisherPort`, `ICryptoKeyProviderPort`) et leurs doublures de test mémoire pures,  
  > **Afin de** rendre la couche applicative totalement découplée de l'infrastructure et testable sans dépendance externe.

* **Critères d'Acceptation Opérationnels :**
  1. Les interfaces de ports de sortie se situent exclusivement dans `NovaAnalytics.Application.Ports.Outbound` et ne renvoient que des types du Domaine ou des types primitifs de base.
  2. Le cas d'usage `ConsolidateLedgerPeriodUseCase` orchestre la récupération de l'agrégat, l'appel de consolidation métier, la persistance et l'émission d'événement d'audit sans faire appel à un conteneur externe.
  3. Les doubles de tests mémoires (`InMemoryLedgerRepositorySpy`, `InMemoryAuditPublisherSpy`) permettent d'exécuter la suite complète de tests applicatifs en moins de $50\text{ millisecondes}$.
  4. Tout échec technique au niveau d'un port (ex: coupure de persistance) est intercepté et transformé en type fonctionnel structuré `Result<T>` sans faire fuiter de stack trace technique vers le domaine.

---

### FEATURE FEAT-04 : Migration & Sécurisation Critique du LedgerCube (Intégrité SOX)

#### Story Jira `US-TECH-04.1` : Adaptateur de Persistance SQL vers Modèle TMDL Partitionné pour le Grand Livre
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-04`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant que** Développeur Infrastructure & Data Engine,  
  > **Je souhaite** développer l'adaptateur de sortie `VertiPaqXmlaSyncAdapter` extrayant les données validées du Grand Livre vers les partitions tabulaires TMDL correspondantes,  
  > **Afin de** remplacer le traitement monolithique SSAS par un chargement incrémental par période comptable sans régression d'intégrité.

* **Critères d'Acceptation Opérationnels :**
  1. L'adaptateur implémente l'interface `ISemanticPartitionPublisherPort`.
  2. Les partitions du modèle TMDL *LedgerCube* sont découpées par exercice et par mois comptable (`PeriodCode`).
  3. Le rafraîchissement d'une période clôturée (`Closed`) ne retraite jamais l'historique figé mais met à jour uniquement la partition courante en mode rafraîchissement incrémental XMLA.
  4. Les types de données comptables dans TMDL utilisent explicitement le type `Currency` ou `Decimal` à 4 décimales (exclusion formelle des approximations `Double`).
  5. La synchronisation d'un volume de test de $50\text{ millions}$ d'écritures s'exécute en moins de $20\text{ minutes}$ via les canaux de transmission managés.

---

#### Story Jira `US-TECH-04.2` : Tests de Non-Régression Mathématique et Financière du Grand Livre (SSAS vs Fabric)
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-04`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant qu'** Expert BI / Auditeur Financier,  
  > **Je souhaite** exécuter un framework de tests automatisés comparant au centime près les résultats des calculs de balance et consolidations entre le SSAS existant et le nouveau modèle Fabric,  
  > **Afin de** certifier la stricte conformité réglementaire SOX et le décret d'intégrité avant l'arrêt de l'ancien cube.

* **Critères d'Acceptation Opérationnels :**
  1. Un script de validation automatique exécute 50 requêtes de synthèses (balances générales, balances âgées, grands livres auxiliaires) simultanément sur SSAS et sur le modèle Fabric.
  2. Le différentiel toléré sur l'ensemble des agrégats monétaires consolidés est de $0{,}00\text{ €}$ (zéro centime d'écart sur les comptes de classe 1 à 7).
  3. Les mesures DAX calculant le résultat consolidé reportent fidèlement la gestion des devises multiples selon le taux de change de clôture de la période concernée.
  4. Un rapport de certification horodaté et inaltérable est généré et stocké dans l'espace documentaire de gouvernance pour l'audit externe.

---

### FEATURE FEAT-05 : Ingestion Pseudonymisée & Modélisation Sécurisée du RecoveryCube (RGPD)

#### Story Jira `US-TECH-05.1` : Adaptateur Cryptographique de Pseudonymisation Débiteurs SHA-256 avec Sel HSM
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-05`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant qu'** Ingénieur Cryptographie / Développeur Backend,  
  > **Je souhaite** développer l'adaptateur `Sha256SaltedAnonymizerAdapter` injectant un sel tournant extrait de manière sécurisée depuis le Key Vault pour dériver les identifiants clients,  
  > **Afin de** détruire irréversiblement les données identifiantes en clair dès la frontière d'ingestion analytique et respecter la politique RGPD C2 MASSIF.

* **Critères d'Acceptation Opérationnels :**
  1. L'adaptateur implémente l'interface `IDebtorAnonymizationPort`.
  2. Aucun identifiant client en clair (`ClearDebtorId`, SIREN, Numéro de compte bancaire) ne franchit la frontière du modèle sémantique sans être transformé en hash hexadécimal immuable (`AnonymizedDebtorHash`).
  3. Le sel cryptographique utilisé fait un minimum de 256 bits et est récupéré en mémoire vive via le port `ICryptoKeyProviderPort` sans jamais être persisté sur disque ou loggé.
  4. L'algorithme de hachage applique l'instruction SHA-256 avec salt dynamique sans collision détectée sur un jeu de validation de 10 millions de clés distinctes.
  5. Des tests unitaires spécifiques vérifient qu'une chaîne vide, nulle ou malformée lève immédiatement une exception d'invalidation sans générer de hash par défaut.

---

#### Story Jira `US-TECH-05.2` : Matrice RLS/CLS Dynamique et Filtrage Sécurisé du Risque de Défaut
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-05`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant qu'** Architecte Sécurité Applicative,  
  > **Je souhaite** définir dans le fichier TMDL les règles de sécurité Row-Level Security (RLS) et Column-Level Security (CLS) restreignant l'accès aux données de litiges contentieux et d'évaluation du risque,  
  > **Afin d'** interdire la consultation de portefeuilles de créances non autorisés aux utilisateurs non habilités.

* **Critères d'Acceptation Opérationnels :**
  1. Les rôles de sécurité (`RiskAnalyst`, `RecoveryManager`, `ExternalAuditor`) sont déclarés dans le format TMDL avec prédicats DAX de filtrage basés sur `USERPRINCIPALNAME()`.
  2. Les utilisateurs affectés au rôle `RiskAnalyst` ne visualisent que les créances rattachées à leur périmètre géographique ou entité juridique de rattachement.
  3. Les colonnes sensibles (ex: coordonnées de contact, motifs de contestation juridique) sont masquées via CLS aux utilisateurs qui ne possèdent pas l'habilitation de niveau superviseur.
  4. Des tests de requêtage automatisés simulent des sessions avec divers contextes d'identité Entra ID : aucune élévation de privilèges ni fuite d'enregistrements transverses n'est observée.
  5. Aucune règle RLS ne provoque de bascule en mode *DirectQuery* dégradé lors du requêtage des tables volumineuses.

---

### FEATURE FEAT-06 : Ingestion Haute Volumétrie OneLake & Migration BillingCube

#### Story Jira `US-TECH-06.1` : Ingestion Parallèle Delta Lake vers OneLake avec Chiffrement CMK
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-06`
* **Points d'estimation (Story Points) :** 5
* **Format Jira :**
  > **En tant que** Data Engineer / Ingénieur de Plateforme,  
  > **Je souhaite** déployer les flux d'extraction haute volumétrie de la facturation vers OneLake au format Delta Parquet optimisé et chiffré par CMK,  
  > **Afin d'** absorber le volume de 500 millions de lignes dans la fenêtre de traitement de 2 heures.

* **Critères d'Acceptation Opérationnels :**
  1. Les données sources de facturation sont converties en fichiers au format Delta Parquet partitionnés par année et par mois d'émission (`BillingYearMonth`).
  2. L'écriture dans OneLake applique automatiquement l'instruction de compaction et d'alignement (*V-Order* / *Z-Order* sur les clés de requêtage fréquentes) pour optimiser les performances de lecture du moteur tabulaire.
  3. L'ingestion complète d'une charge quotidienne incrémentale ($15\text{ millions}$ de lignes transactionnelles) s'exécute en moins de $30\text{ minutes}$.
  4. Les conteneurs de stockage sous-jacents confirment l'activation effective du chiffrement transparent avec la clé CMK (`cmk-fabric-nova-prod`).
  5. En cas d'anomalie d'ingestion au milieu du traitement, la transactionnalité Delta Lake (ACID) garantit l'annulation complète sans persistance de données orphelines ou corrompues.

---

#### Story Jira `US-TECH-06.2` : Benchmark de Concurrence Interactive Power BI (< 3s sur 300 utilisateurs)
* **Épopée parente :** `EPIC-ENABLER-01` / `FEAT-06`
* **Points d'estimation (Story Points) :** 3
* **Format Jira :**
  > **En tant qu'** Ingénieur Performance & Scalabilité,  
  > **Je souhaite** exécuter un banc de test de charge simulant 300 utilisateurs concurrents interrogeant simultanément le modèle sémantique de facturation,  
  > **Afin de** valider l'absence de saturation mémoire et garantir des temps de réponse inférieurs à 3 secondes au 95e percentile.

* **Critères d'Acceptation Opérationnels :**
  1. L'outil de tir de performance (JMeter ou équivalent via scripts d'exécution DAX XMLA) génère un profil de trafic progressif jusqu'à 300 sessions simultanées exécutant des requêtes interactives Power BI.
  2. Le temps de rendu des requêtes DAX complexes reste strictement inférieur à $3{,}0\text{ secondes}$ pour $95\%$ des requêtes exécutées ($P95 < 3\text{ s}$).
  3. La consommation mémoire et CPU de la capacité Fabric dédiée ne déclenche aucun mécanisme de restriction ou de dégradation automatique de service (*Capacity Throttling*).
  4. Aucun basculement vers DirectQuery n'est constaté durant l'ensemble du scénario de test.
  5. Un rapport de performance détaillé est publié et archivé dans les artefacts de release de l'Incrément de Programme (PI).

---

## 4. Definition of Done (DoD) Standardisée

Cette Definition of Done constitue l'accord qualité non négociable liant les équipes de build, le System Architect, le RSSI et le Product Management. **Aucune User Story ne peut être fermée ou basculée dans la colonne "Done" sans validation intégrale des 5 piliers suivants.**

```
===================================================================================================
                             DEFINITION OF DONE (DoD) - ÉQUIPES BUILD ART
===================================================================================================
```

```
       [ PILIER 1 ]             [ PILIER 2 ]             [ PILIER 3 ]
  Code & Software Crafts    Tests & Déterminisme     Sécurité C2 & Zero-Trust
  • Clean Code / SOLID      • 0 I/O Réseau Domaine   • 0 IP Publique (PeP)
  • NetArchTest conforme    • Tests unitaires < 3s   • Clés CMK FIPS 140-2
  • 0 Warning Compilation   • Couverture > 95%       • 0 Secret en clair (OIDC)
            \                    |                    /
             +-------------------+-------------------+
                                 |
        +------------------------+------------------------+
        |                                                 |
  [ PILIER 4 ]                                      [ PILIER 5 ]
  Performance & Scalabilité                         CI/CD & Observabilité
  • P95 Requêtes < 3s                               • Tabular Editor BPA (0 Warn)
  • Ingestion batch < 2h                            • Logs SIEM WORM 365j
  • Modèle TMDL sans Fallback                       • Revue par 2 pairs validée
```

---

### Pilier 1 : Qualité du Code Source & Software Craftsmanship
* [ ] **Respect Strict de l'Architecture Hexagonale :** Le projet `Domain` ne contient aucun import technique (absence totale de packages de bases de données, SDK cloud ou frameworks HTTP). Les dépendances pointent exclusivement vers l'intérieur.
* [ ] **Validation d'Architecture Automatisée :** Les tests d'architecture de type *NetArchTest* sont passés avec succès lors de la compilation locale et CI.
* [ ] **Principes SOLID & Clean Code :**
  * Absence formelle d'obsession primitive : les concepts métiers sont portés par des Value Objects immuables (`Money`, `RiskScore`, `Currency`, `AccountingPeriod`).
  * Les entités et agrégats intègrent leurs invariants métiers et appliquent le pattern *Fail-Fast* (rejet immédiat de toute valeur invalide à l'instanciation).
  * Zéro référence `null` : utilisation obligatoire des types optionnels (`Option<T>`) ou de structures de résultats explicites (`Result<T>`).
* [ ] **Rigueur de Compilation :** La compilation s'exécute avec l'option `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>` sans aucun avertissement (*Zero Warning*).

---

### Pilier 2 : Tests & Déterminisme Mathématique
* [ ] **Indépendance Totale des Tests Unitaires :** L'intégralité de la suite de tests unitaires du Domaine (`NovaAnalytics.Domain.UnitTests`) s'exécute de façon strictement déterministe (sans connexion réseau, sans conteneur Docker, sans base de données, sans secret d'infrastructure).
* [ ] **Performance d'Exécution :** La suite complète des tests de domaine s'exécute en moins de **3 secondes** sur un poste de développement standard et dans l'agent CI.
* [ ] **Couverture de Code :**
  * La couverture de branches (*Branch Coverage*) mesurée sur les agrégats du Domaine, les Value Objects et les règles de calcul financières est strictement supérieure à **95%**.
  * La couverture globale sur la couche Application (Use Cases) est supérieure à **85%**.
* [ ] **Tests d'Intégration Isolés :** Les adaptateurs techniques (SQL, XMLA, Key Vault) disposent de tests d'intégration dédiés s'exécutant sur des environnements éphémères ou via des doublures d'interfaces explicites.

---

### Pilier 3 : Sécurité C2 MASSIF & Conformité Zero-Trust
* [ ] **Cloisonnement Réseau Absolu :** Aucune adresse IP publique n'est ouverte. L'ensemble des composants communique exclusivement via des Private Endpoints rattachés au VNet d'entreprise.
* [ ] **Chiffrement de Bout en Bout :**
  * Les données au repos sont chiffrées par clé gérée par le client (CMK) adossée à Azure Key Vault Premium / Managed HSM certifié FIPS 140-2 Niveau 3.
  * Les flux en transit imposent l'usage strict du protocole TLS 1.3 avec suites cryptographiques robustes (suites dépréciées désactivées).
  * Les liaisons inter-sites hybrides exploitent un chiffrement physique MACsec IEEE 802.1AE.
* [ ] **Éradication des Secrets en Clair :**
  * Le scan de sécurité SAST (Gitleaks / TruffleHog) atteste de l'absence totale de secrets, mots de passe, tokens ou clés de stockage dans le code source ou la configuration Git.
  * L'authentification inter-services et CI/CD exploite exclusivement la fédération d'identités (OIDC / Managed Identities).
* [ ] **Pseudonymisation & RGPD :** Tout identifiant à caractère personnel ou bancaire entrant dans le périmètre analytique (notamment le *RecoveryCube*) est irréversiblement transformé à la source via hachage salé SHA-256 conformément aux directives de la DSSI.
* [ ] **Règles RLS/CLS Vérifiées :** Les matrices d'habilitations de filtrage au niveau de la ligne et de la colonne sont couvertes par des scénarios de tests unitaires simulant des contextes d'utilisateurs distincts.

---

### Pilier 4 : Performance & Scalabilité Opérationnelle
* [ ] **Temps de Réponse Interactif :** Le profilage des requêtes DAX sur un volume de test représentatif valide un temps moyen de réponse inférieur à **3 secondes** sur le 95e percentile ($P95 < 3\text{ s}$) sous charge de 300 utilisateurs simultanés.
* [ ] **Fenêtre d'Exécution Batch :** Le rafraîchissement incrémental partitionné du cube garantit une ingestion complète en moins de **2 heures**.
* [ ] **Préservation du Moteur In-Memory / Direct Lake :** Aucune requête ou mesure métier complexe ne provoque de basculement silencieux et inattendu vers le mode dégradé *DirectQuery*.
* [ ] **Dimensionnement FinOps :** Les ressources allouées respectent l'enveloppe de capacité attribuée, sans déclencher de mécanismes de throttling sur les charges courantes.

---

### Pilier 5 : Déploiement Continu, Observabilité & Revue par les Pairs
* [ ] **Audit Qualité Modélisation TMDL :** L'analyseur statique de bonnes pratiques (*Tabular Editor Best Practice Analyzer*) ne remonte aucune violation d'intégrité ou d'optimisation sur les définitions TMDL.
* [ ] **Revue de Code Systématique (Peer Review) :** La Pull Request a été formellement approuvée par au moins **deux réviseurs** techniques (dont le Tech Lead ou l'Architecte Système pour tout changement impactant le Domaine ou l'Infrastructure).
* [ ] **Traçabilité & Observabilité SSI :**
  * L'ensemble des événements de déploiement, de modification de schéma, et d'exécution de clôture est tracé et déversé dans le SIEM d'entreprise (Azure Sentinel / Log Analytics).
  * La rétention d'audit immuable (stockage WORM) est configurée et active pour un minimum de 365 jours.
* [ ] **Documentation Vivante :** Le modèle de données, les schémas relationnels et les métadonnées sont documentés directement dans les artefacts déclaratifs TMDL et synchronisés dans le catalogue de gouvernance de données Purview.