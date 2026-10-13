# 🚀 Backlog d'Implémentation SAFe & Jira : Plateforme OmniClaim AI (Classification C2 Massif)

**Programme :** Modernisation du Cœur Sinistres & Déploiement d'Agents IA en Production  
**Cadre Méthodologique :** SAFe 6, Software Craftsmanship (Hexagonale / DDD / TDD), Zero-Trust (NIST SP 800-207)  
**Langue :** Français [FR]

---

## 1. 📋 Fiche Enabler Epic

* **ID Epic :** `ENABLER-EPIC-01`
* **Titre :** Modernisation de la Plateforme OmniClaim AI & Socle Hybride Zero-Trust (C2 Massif)
* **Objectif (Business Outcome) :** 
  * Réduire drastiquement le *Time-to-Indemnize* (de 7-10 jours à < 15 min pour les cas simples, < 48h pour les cas complexes).
  * Absorber des pics climatiques multipliés par 10 en 24h (5 000 dossiers/heure) sans dégradation.
  * Industrialiser la détection de fraude documentaire (> 80 M€/an d'économies) tout en garantissant une étanchéité absolue des données sensibles (Classification C2 Massif) et la conformité RGPD.
* **Hypothèse de Valeur :** 
  * *Si* nous mettons en place une architecture hexagonale couplée à un pipeline d'inférence IA sécurisé (enclave isolée, masquage PII local) et un socle d'infrastructure as code (IaC) résilient (Multi-AZ, Outbox pattern), *alors* nous pourrons automatiser 80% des flux de sinistres en toute sécurité, éliminer les goulets d'étranglement du monolithe legacy et diviser par 4 les coûts opérationnels de traitement.
* **Métriques de Succès (KPIs) :**
  * Traitement de 95% des dossiers éligibles en moins de 15 minutes.
  * Disponibilité globale de la plateforme de l'ordre de $99.99\%$ (SLA).
  * Latence P99 de l'API synchrone $< 1.5$ seconde (hors inférence lourde).
  * Zéro fuite de données PII/C2 Massif (0 incident de conformité RGPD ou d'injection de prompt réussie).
  * Couverture de tests unitaires du domaine $> 90\%$ avec 0 dépendance d'infrastructure.

---

## 2. 🗺️ Liste des Enabler Features Priorisées (WSJF Aligné)

Les Enabler Features sont découpées verticalement par incréments de valeur et priorisées selon la matrice de valeur architecturale et de mitigation des risques C2.

1. **`ENABLER-FEAT-01` : Socle d'Infrastructure Zero-Trust & Chiffrement C2 (Terraform/KMS/S3)**
   * *Description :* Déploiement du VPC sécurisé multi-AZ, des clés de chiffrement maîtresses client (CMK) KMS/Key Vault, des buckets S3 immuables (Object Lock) et des ponts réseau étanches.
2. **`ENABLER-FEAT-02` : Cœur de Domaine Clean Architecture & Modèle DDD `ClaimsManagement`**
   * *Description :* Implémentation du cœur de domaine pur (Agrégat Root `Claim`, Value Objects immuables, règles métier d'approbation et d'évaluation des risques) sans aucune dépendance framework.
3. **`ENABLER-FEAT-03` : Pipeline d'Anonymisation PII Local & Enclave LLM Sécurisée**
   * *Description :* Intégration du filtre déterministe de masquage des PII (NIR, IBAN, adresses) et connexion étanche via Private Endpoints à l'enclave Azure OpenAI avec garde-fous NeMo Guardrails.
4. **`ENABLER-FEAT-04` : Adaptateurs d'Infrastructure, Outbox Pattern & Résilience Kafka/Aurora**
   * *Description :* Implémentation des adaptateurs de persistance PostgreSQL (Aurora) avec le pattern Transactionnel Outbox, et des connecteurs Kafka (MSK) résilients avec Circuit Breakers (Resilience4j).

---

## 3. 🎫 Backlog Détaillé des User Stories Jira Techniques

### ⚡ Epic/Feature : `ENABLER-FEAT-01` (Socle d'Infrastructure Zero-Trust)

#### Story 1.1 : Provisionnement du VPC Isolé et des Subnets Privés Multi-AZ
* **ID Jira :** `OMNI-101`
* **Type :** Technical Enabler Story
* **Estimations :** 5 Story Points
* **Description :**
  * **En tant que** SRE / Cloud Engineer,
  * **Je souhaite** provisionner l'infrastructure réseau de base via Terraform (VPC `var.vpc_cidr_block`, subnets privés isolés sur 3 Zones de Disponibilité et tables de routage strictes),
  * **Afin de** garantir l'étanchéité périmétrique Zero-Trust (NIST SP 800-207) et empêcher tout accès public direct aux composants de calcul de la plateforme OmniClaim AI.
* **Critères d'Acceptation Opérationnels :**
  1. Le code Terraform/OpenTofu est validé par l'outil de linting `tflint` sans aucune erreur ni avertissement de sécurité.
  2. Le VPC est créé avec `enable_dns_hostnames = true` et `enable_dns_support = true`.
  3. Aucun routeur internet (IGW) n'est attaché aux subnets d'application et de données (isolation totale).
  4. Le déploiement s'exécute avec succès sur les environnements DEV, INT et PERF via pipelines CI/CD automatisés.

#### Story 1.2 : Configuration du Chiffrement CMK et du Data Lake S3 Immuable (WORM)
* **ID Jira :** `OMNI-102`
* **Type :** Technical Enabler Story
* **Estimations :** 8 Story Points
* **Description :**
  * **En tant que** Data Security Engineer,
  * **Je souhaite** configurer une clé maîtresse client dédiée (CMK) dans AWS KMS avec rotation annuelle et un bucket S3 de stockage des documents de sinistres doté du verrouillage d'objet (*S3 Object Lock* en mode *Compliance*),
  * **Afin de** respecter strictement les exigences de classification de données **C2 MASSIF** et de garantir l'immutabilité légale et financière des pièces justificatives.
* **Critères d'Acceptation Opérationnels :**
  1. La clé KMS dispose d'une politique d'accès restrictive et d'une fenêtre de suppression de 30 jours minimum, avec rotation automatique activée (`enable_key_rotation = true`).
  2. Le bucket S3 applique par défaut le chiffrement `aws:kms` avec la CMK dédiée (interdiction stricte du chiffrement par défaut S3-Managed).
  3. Le blocage public S3 (`block_public_acls`, `block_public_policy`, `ignore_public_acls`, `restrict_public_buckets`) est configuré à `true` sans exception.
  4. Le mode *S3 Object Lock (Compliance Mode)* est activé sur le bucket de stockage pour empêcher toute altération ou suppression des pièces justificatives pendant la durée légale de conservation.

---

### ⚡ Epic/Feature : `ENABLER-FEAT-02` (Cœur de Domaine Clean Architecture & DDD)

#### Story 2.1 : Implémentation de l'Agrégat Racine `Claim` et des Value Objects Immuables
* **ID Jira :** `OMNI-201`
* **Type :** Technical Enabler Story
* **Estimations :** 5 Story Points
* **Description :**
  * **En tant que** Software Craftsperson / Développeur Backend,
  * **Je souhaite** implémenter l'Agrégat Racine `Claim`, l'entité `SupportingDocument` et les Objets de Valeur immuables (`ClaimId`, `ClaimAmount`, `FraudScore`) en respectant les principes du Domain-Driven Design (DDD),
  * **Afin de** garantir l'encapsulation stricte des invariants métier du cycle de vie des sinistres dans un cœur de domaine totalement découplé des frameworks et de l'infrastructure.
* **Critères d'Acceptation Opérationnels :**
  1. Le code source du domaine réside dans le package `com.assurglobal.omniclaim.domain` et ne contient **aucune dépendance** envers Spring Framework, Hibernate, AWS SDK ou des bibliothèques d'infrastructure.
  2. Tous les Objets de Valeur (`Value Objects`) sont immuables (`final` fields, absence de setters, utilisation de `record` ou classes immuables avec constructeurs validant les contraintes métier).
  3. La méthode d'évaluation des risques (`evaluateAndProcess`) applique l'invariant : si le montant dépasse le seuil (ex: 2000 €) ou si le score de fraude dépasse la limite (0.15), le statut bascule obligatoirement en `PENDING_MANUAL_REVIEW`, sinon en `AUTO_APPROVED`.
  4. Une suite de tests unitaires purs JUnit 5 / AssertJ couvre 100% des règles de gestion de l'agrégat sans aucun contexte Spring chargé.

---

### ⚡ Epic/Feature : `ENABLER-FEAT-03` (Pipeline d'Anonymisation PII & Enclave LLM)

#### Story 3.1 : Développement du Filtre Déterministe de Masquage Local des PII
* **ID Jira :** `OMNI-301`
* **Type :** Technical Enabler Story
* **Estimations :** 8 Story Points
* **Description :**
  * **En tant que** Security & Privacy Engineer,
  * **Je souhaite** implémenter un composant logiciel local d'anonymisation (masquage par expressions régulières et modèles NER) s'exécutant dans les pods EKS,
  * **Afin de** garantir qu'aucune donnée personnelle sensible (C2 Massif : NIR, IBAN, noms complets, adresses postales en clair) ne quitte le réseau sécurisé d'AssurGlobal vers l'enclave d'inférence LLM.
* **Critères d'Acceptation Opérationnels :**
  1. Le filtre analyse les payloads textuels et les métadonnées des documents avant toute sortie vers l'adaptateur LLM.
  2. Les numéros de Sécurité Sociale (NIR), les IBAN bancaires et les noms propres identifiés sont remplacés par des jetons de masquage sécurisés (ex: `[REDACTED_IBAN]`).
  3. Une batterie de tests unitaires de non-régression valide l'efficacité du masquage sur un jeu de données de test représentatif de 1000 dossiers contenant des PII variées.
  4. En cas d'échec ou d'ambiguïté du filtre, une exception de sécurité est levée et le dossier est automatiquement mis en quarantaine pour revue humaine.

#### Story 3.2 : Implémentation de l'Adaptateur Azure OpenAI avec Private Endpoint & Circuit Breaker
* **ID Jira :** `OMNI-302`
* **Type :** Technical Enabler Story
* **Estimations :** 5 Story Points
* **Description :**
  * **En tant que** Lead Backend Architect,
  * **Je souhaite** implémenter l'adaptateur de sortie `AzureOpenAiAdapter` implémentant le port `AiAnalyzerPort` via WebClient, couplé au pattern Circuit Breaker (Resilience4j) et à un canal réseau sécurisé par Private Endpoint,
  * **Afin de** permettre l'analyse cognitive des sinistres tout en garantissant une tolérance aux pannes robuste et une étanchéité absolue contre les appels sortants publics non maîtrisés.
* **Critères d'Acceptation Opérationnels :**
  1. L'appel vers l'enclave Azure OpenAI s'effectue exclusivement via une URL interne de type Private Endpoint (interdiction d'utiliser des points de terminaison publics).
  2. Le pattern Resilience4j `CircuitBreaker` est configuré : si le taux d'erreur 5xx dépasse 2% sur une fenêtre glissante de 10 secondes, le circuit s'ouvre, basculant immédiatement les flux vers le mode dégradé (file d'attente HITL humaine).
  3. L'adaptateur respecte strictement le contrat de l'interface de port de sortie sans fuite de classes spécifiques Azure vers le cœur de domaine.
  4. Les tests d'intégration avec WireMock simulant les réponses et les pannes de l'API Azure OpenAI passent avec succès.

---

### ⚡ Epic/Feature : `ENABLER-FEAT-04` (Adaptateurs, Outbox Pattern & Résilience)

#### Story 4.1 : Implémentation du Pattern Transactional Outbox pour PostgreSQL et Kafka
* **ID Jira :** `OMNI-401`
* **Type :** Technical Enabler Story
* **Estimations :** 8 Story Points
* **Description :**
  * **En tant que** Software Craftsperson,
  * **Je souhaite** implémenter le pattern *Transactional Outbox* pour la persistance des sinistres dans Aurora PostgreSQL et la publication des événements métiers dans les topics Kafka (MSK),
  * **Afin de** garantir l'atomicité transactionnelle parfaite (zéro perte de message ou décalage d'état en cas de crash applicatif ou de coupure réseau).
* **Critères d'Acceptation Opérationnels :**
  1. L'écriture de la modification de l'agrégat `Claim` et l'insertion de l'événement dans la table `outbox` s'exécutent dans la même transaction JDBC.
  2. Un composant de relecture asconfigurable (Debezium ou Publisher Poller) dépile la table `outbox` pour publier les événements vers le broker Kafka `claims.ingest.v1` avec garantie *At-Least-Once*.
  3. L'utilisation d'une clé d'idempotence (`X-Request-ID` / UUID v4) est obligatoire pour chaque événement publié afin d'éviter tout double traitement en aval.
  4. Les tests d'intégration basés sur **Testcontainers** (PostgreSQL + Kafka) valident le scénario de commit transactionnel et de publication asynchrone nominale et en cas de panne de Kafka.

---

## 4. 🛡️ Definition of Done (DoD) Standardisée

La *Definition of Done* (DoD) ci-dessous s'applique de manière stricte à **toutes** les User Stories techniques et Enabler Features du train SAFe pour la plateforme OmniClaim AI. Aucune story ne peut être déclarée `Done` en fin de Sprint si l'ensemble de ces critères n'est pas rempli et audité.

1. **Qualité du Code & Craftsmanship :**
   * Le code respecte les principes SOLID, KISS, YAGNI et les règles de Clean Code (nommage explicite, classes et méthodes courtes, immutabilité par défaut).
   * Le code source a fait l'objet d'une **Revue de Code croisée** obligatoire (minimum 2 approbations de pairs dont un Lead Craftsperson ou Architecte).
2. **Couverture de Tests & TDD :**
   * Le cœur de domaine dispose d'une couverture de tests unitaires purs $\ge 90\%$ (mesurée via JaCoCo) **sans aucune dépendance d'infrastructure ni contexte framework**.
   * Les tests d'intégration (utilisant Testcontainers pour PostgreSQL et Kafka) valident le bon fonctionnement des adaptateurs.
   * Zéro régression sur la suite de tests automatisés de la pipeline CI/CD.
3. **Sécurité & Conformité C2 Massif :**
   * Analyse statique du code (SAST) exécutée sans aucune vulnérabilité critique ou majeure détectée (via SonarQube / Trivy).
   * Vérification de l'absence totale de secrets, mots de passe ou clés en dur dans le code source ou les manifests de déploiement (Secret Scanning actif).
   * Validation de la conformité au chiffrement CMK et au masquage des PII pour tout composant manipulant des données de sinistres.
4. **Déploiement & Observabilité :**
   * Les manifests d'infrastructure (Terraform) ou de déploiement (Kubernetes / Helm) sont validés et versionnés dans le dépôt Git de référence.
   * Les métriques RED (Rate, Errors, Duration) et les traces distribuées OpenTelemetry (`traceparent`) sont implémentées et remontent correctement dans les dashboards d'observabilité.