# FICHE D'AUDIT ET AVIS DE CONFORMITÉ CISO
**Projet :** Plateforme OmniClaim AI (AssurGlobal)  
**Cadre de référence :** NIST SP 800-207 (Zero-Trust), RGPD, OWASP Top 10 for LLMs, Architecture Hexagonale, SAFe 6.  
**Classification des données :** **C2 MASSIF** (Données à caractère personnel sensibles, données financières, documents justificatifs d'assurance).  

---

### 1. Avis global du CISO

> **AVIS : FAVORABLE AVEC RÉSERVES MAJEURES (SOUS CONDITION DE RECONCEPTION DE LA TOPOLOGIE)**

L'alignement sur les exigences de traçabilité, de cloisonnement et de gouvernance (Human-in-the-Loop) est globalement salué. Cependant, **l'architecture cible proposée (Scénario 3 - Multi-Cloud Hybride AWS/Azure) est invalidée en l'état** par la gouvernance de la sécurité des données. La complexité du réseau inter-cloud, la multiplication des frontières de confiance et les risques de fuite de métadonnées ou de latence incompatible avec la criticité métier imposent un recentrage de la stratégie d'infrastructure.

---

### 2. Matrice d'analyse de classification des données (Niveau C2 massif, impacts Cloud)

| Axe d'Analyse | Exigence C2 Massif & RGPD | Évaluation de la Proposition Initiale | Risque Sécurité / Conformité |
| :--- | :--- | :--- | :--- |
| **Périmètre des PII** | Isolation stricte, traçabilité des accès, minimization des transferts. | Anonymisation locale et déterministe avant transmission externe. | **Moyen** : Dépend de la robustesse de l'algorithme d'anonymisation embarqué sur l'Ingestion AWS. |
| **Hébergement des Modèles & Inférence** | Souveraineté des traitements, interdiction absolue de réentraînement sur les données clients. | Enclave Azure dédiée (Azure OpenAI / Llama-3). | **Élevé** : Le transit inter-cloud (AWS -> Azure) de charges complexes augmente la surface d'attaque et les risques d'exposition de métadonnées sensibles en transit. |
| **Résidence des Données** | Stockage exclusif au sein de l'Union Européenne, conformité stricte aux exigences RGPD (Art. 32 & 44+). | Data Lake S3 (AWS) + Stockage Azure. | **Conforme** sous réserve de validation des régions de déploiement (ex: `eu-west-1` / `france-central`). |

---

### 3. Exigences de sécurité obligatoires

Pour tout passage en Dossier de Conformité Architecture (DCA), les exigences techniques suivantes sont **non négociables** :

1. **Chiffrement de bout en bout et gestion des secrets (KMS / Vault) :**
   * Utilisation exclusive de clés maîtres client dédiées (**CMK - Customer Managed Keys**) gérées dans des HSM certifiés (AWS KMS / Azure Key Vault). 
   * **Interdiction formelle** de stocker des clés d'API, des secrets de connexion ou des tokens d'accès en clair dans les fichiers de configuration, les variables d'environnement non chiffrées ou le code source (Software Craftsmanship / GitGuardian compliance).
   * Chiffrement des flux en transit par TLS 1.3 obligatoire, adossé à un pinning de certificats et à l'interdiction des suites cryptographiques obsolètes.
2. **Posture Zero-Trust (NIST SP 800-207) & Cloisonnement Réseau :**
   * **Private Endpoints obligatoires** pour l'accès aux services cognitifs et aux bases de données vectorielles (Azure AI Search / S3). Aucune exposition sur l'Internet public.
   * Mise en place d'un contrôle d'accès fondé sur l'identité et le contexte (Micro-segmentation, mTLS systématique entre les microservices sur Amazon EKS via un Service Mesh type Istio/Linkerd).
3. **Protection contre l'OWASP Top 10 for LLMs :**
   * Implémentation systématique de barrières de modération en amont et en aval de l'inférence (LLM Guardrails / NeMo Guardrails) pour contrer les injections de prompts indirectes (factures/devis malveillants).
   * Validation rigoureuse des schémas de sortie des modèles (JSON Schema validation) pour empêcher toute exécution de code arbitraire ou d'hallucination structurelle critique.

---

### 4. Recommandations impératives pour l'homologation DCA

L'homologation du Dossier de Conformité Architecture (DCA) par le CISO est suspendue à la levée des réserves suivantes :

1. **Simplification topologique (Arbitrage Mono-Cloud) :**
   * Il est demandé d'étudier en priorité un **alignement sur un modèle Mono-Cloud unifié (AWS natif avec Amazon Bedrock)** ou, à défaut, de justifier par une analyse de risque formelle la nécessité absolue du Scénario 3 (Multi-Cloud). La suppression de la liaison inter-cloud (Direct Connect / ExpressRoute) réduit drastiquement la surface d'attaque et les risques de rupture de service.
2. **Durcissement du Plan de Continuité et du Mode Dégradé (Fail-Safe) :**
   * Formalisation d'un scénario de repli synchrone (Fallback) : en cas d'indisponibilité de l'enclave IA ou de dépassement des seuils de latence, les dossiers doivent basculer de manière transparente et sécurisée vers une file de traitement humain (HITL) sans perte d'intégrité des données.
3. **Audit de conformité du code et des dépendances :**
   * Intégration de gates de sécurité obligatoires dans la pipeline CI/CD (SAST, SCA, scan de conteneurs et analyse dynamique des prompts) avant toute mise en production des agents IA.