# Cahier des Charges & Cadrage d'Architecture : Plateforme OmniClaim AI

**Programme :** Modernisation du Cœur Sinistres & Déploiement d'Agents IA en Production  
**Entreprise :** Groupe AssurGlobal (Assurance IARD & Santé — 15 millions de dossiers par an)  
**Classification des Données :** **C2 MASSIF** (Données personnelles, bancaires, d'immatriculation et éléments de santé)  
**Cadre Référentiel :** TOGAF 10 ADM, SAFe 6 for Architects, Software Craftsmanship (Hexagonale / DDD / TDD), Zero-Trust (NIST SP 800-207) & FinOps  
**Date :** Octobre 2026  

---

## 1. Contexte Métier & Enjeux Stratégiques

AssurGlobal gère plus de 15 millions de déclarations de sinistres par an (automobiles, habitations, catastrophes naturelles).

### Les Défis Majeurs du Métier :
1. **Délai de traitement inacceptable :** Le temps moyen de traitement d'un dossier sinistre (de la déclaration au virement d'indemnisation) est actuellement de **7 à 10 jours ouvrés**, provoquant une insatisfaction client croissante.
2. **Vulnérabilité aux pics climatiques :** Lors d'événements météorologiques majeurs (grêle, inondations, tempêtes), le volume quotidien est multiplié par 10 en 24 heures, provoquant l'effondrement des serveurs et une paralysie opérationnelle.
3. **Coûts de gestion et fraudes non détectées :** 75% du temps des gestionnaires est consommé par des tâches manuelles à faible valeur ajoutée (retranscription de factures de carrosserie, vérification de devis d'artisans), tandis que la fraude documentaire opportuniste coûte plus de 80 M€/an.

---

## 2. Architecture Actuelle (AS-IS) : Le Mur Technique

Le système actuel repose sur une infrastructure traditionnelle vieillissante :
- **Socle Applicatif :** Monolithe Java EE (WebLogic 12c) hébergé sur des machines virtuelles VMware On-Premise dans le datacenter historique.
- **Base de Données :** Cluster Oracle Database 19c RAC sous Linux, saturé lors des batchs nocturnes de calculs d'indemnisation (temps de traitement batch : 8 heures par nuit).
- **Stockage de Documents :** Serveur NAS partagé (SMB/NFS) non indexé contenant 40 To de photos et PDF non structurés.
- **Points de Douleur (SPOF & Dette) :**
  * Verrouillages transactionnels massifs sur les tables d'indemnisation lors des batchs.
  * Absence d'élasticité à la demande.
  * Zéro capacité native d'analyse d'images ou d'intelligence artificielle.

---

## 3. Vision Cible (TO-BE) : Multi-Cloud Hybride & Agents IA en Production

La cible stratégique repose sur une **topologie Multi-Cloud hybride** tirant le meilleur parti des leaders du Cloud, avec découplage strict :

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                          TOPOLOGIE MULTI-CLOUD HYBRIDE                                           │
├─────────────────────────────────────────┬────────────────────────────────────────────────────────────────────────┤
│ CLOUD AWS (Zone Ingestion & Stream)     │ CLOUD AZURE (Zone Cognitive & IA Souveraine)                           │
├─────────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ • Ingestion événementielle Kafka (MSK)  │ • Enclave cognitive privée (Azure OpenAI / Modèles Llama-3 dédiés)     │
│ • Microservices métier sous EKS         │ • Moteur d'embeddings et recherche vectorielle (Azure AI Search)       │
│ • Stockage Data Lake immuable S3        │ • Garde-fous IA & modération (Azure AI Content Safety / NeMo)          │
│ • Chiffrement CMK via AWS KMS           │ • Chiffrement CMK via Azure Key Vault HSM                              │
├─────────────────────────────────────────┴────────────────────────────────────────────────────────────────────────┤
│ 🔗 Interconnexion Sécurisée : Liaison dédiée directe Cloud-to-Cloud (Inter-Cloud Direct Connect / ExpressRoute)   │
│    à très faible latence (< 3 ms) et trafic chiffré IPsec sans transit sur l'Internet public.                   │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. La Brigade d'Agents IA Autonomes en PRODUCTION

Le cœur de la transformation réside dans le déploiement d'une brigade de 3 agents IA spécialisés orchestrés en production :

### Agent 1 : « Vision & Extracteur de Pièces » (Multimodal Document AI)
- **Rôle :** Analyse instantanée des photos de dégâts (carrosserie, toiture) et extraction des devis/factures PDF d'artisans.
- **Capacités :** OCR multimodal haute précision, détection de photomontages ou réutilisation frauduleuse d'images trouvées sur le web.
- **SLA :** Extraction et structuration en JSON normalisé en moins de 1,2 seconde par document.

### Agent 2 : « Détection de Fraude & Conformité Métier » (Risk & Fraud Agent)
- **Rôle :** Corrélation du sinistre avec la base historique et détection des incohérences.
- **Capacités :** Calcul d'un score de risque de fraude ($0.00$ à $1.00$) basé sur des graphes de connaissances (liens suspects entre artisans récurrents, assurés et montants surfacturés).

### Agent 3 : « Évaluateur de Préjudice & Indemnisation » (Claim Settlement Agent)
- **Rôle :** Application des barèmes contractuels du contrat d'assurance et calcul du montant net à indemniser.
- **Capacités :** Génération de la lettre d'accord pour l'assuré et émission de l'ordre de virement bancaire automatique.

---

## 5. Exigences Non Fonctionnelles & Garde-Fous de Sécurité

### A. Sécurité & Conformité Zero-Trust (NIST SP 800-207 & C2 MASSIF)
1. **Anonymisation PII à la volée :** Avant toute soumission de texte ou d'image aux modèles d'IA, les identités, numéros de sécurité sociale et coordonnées bancaires doivent être masqués par un filtre de dé-identification local déterministe.
2. **Protection Anti-Prompt Injection :** Implémentation d'une couche barrière (*Guardrails*) interceptant les tentatives de jailbreak ou d'injonction malveillante dissimulée dans les devis uploadés par les tiers.
3. **Enclave d'Inférence Étanche :** Aucun appel API externe public. Toutes les inférences LLM s'exécutent au sein d'un Virtual Network isolé via Private Endpoints. Les données client ne sont **jamais utilisées pour réentraîner les modèles**.

### B. Gouvernance Human-in-the-Loop (HITL) Obligatoire
* **Règle des 2 000 € :** L'agent IA est habilité à décaisser de manière 100% autonome **uniquement pour les sinistres simples inférieurs à 2 000 €** avec un score de fraude inférieur à $0.15$.
* **Seuil d'arbitrage humain :** Tout dossier dépassant **2 000 €**, ou présentant une ambiguïté contractuelle, ou un score de fraude $\ge 0.15$ est immédiatement suspendu et routé vers la corbeille d'un gestionnaire humain avec la synthèse pré-remplie par l'IA.

### C. Software Craftsmanship & Architecture Hexagonale
* **Découplage absolu des LLMs (Ports & Adapters) :** Le moteur d'IA doit être encapsulé derrière une interface de port secondaire (`ClaimAnalyzerPort`). Le cœur de domaine métier (`Claim`, `IndemnificationPolicy`, `Amount`) ne doit dépendre d'aucun SDK cloud ou IA.
* **Typage fort financier :** Interdiction des types primitifs flottants pour les montants monétaires (utilisation stricte du Value Object `Amount(cents: int, currency: str)`).

### D. FinOps & Maîtrise des Coûts
* **Piège du trafic réseau (Data Egress) :** La bande passante entre AWS et Azure doit être minimisée en ne transférant que des métadonnées JSON légères, les images brutes restant stockées dans le Data Lake AWS S3.
* **Arbitrage LLM :** Comparaison des coûts entre modèles managés à la consommation de tokens (Pay-per-token) et déploiement de modèles open-source (Llama-3 70B) sur instances GPU réservées sous Azure.

---

## 6. Livrables Attendus pour le Comité d'Architecture (ARB)

La brigade d'architectes IA doit produire l'ensemble du pack d'architecture technique pour validation formelle :
1. Fiche de synthèse exécutive décisionnelle (One-Pager ARB).
2. Synthèse managériale TOGAF 10 & SAFe 6.
3. Dossier d'Architecture Technique (DAT) complet.
4. Rapport contradictoire Red Team (Challenger) traquant les risques de l'IA en prod et du multi-cloud.
5. Avis formel d'homologation de sécurité DCA (CISO).
6. Spécification d'Architecture Hexagonale et modélisation DDD (Crafter).
7. Étude financière FinOps et modélisation comparative du TCO sur 3 ans.
8. Backlog Jira d'exécution complet avec Definition of Done (DoD).
9. Feuille de route d'implémentation et planning Gantt phasé.
10. Schémas d'architecture complets AS-IS et TO-BE aux 3 formats (**Draw.io `.drawio`**, **PlantUML `.puml`**, **Mermaid `.mmd`**).
