# Feuille de Route d'Implémentation : Multi-Agent Architecture Platform (AAP)

**Projet :** Multi-Agent Architecture Platform (AAP)  
**Référentiel méthodologique :** TOGAF 10 ADM (Phases A à G), SAFe 6 for Architects & Software Craftsmanship  
**Technologies cibles :** Python 3.13, CrewAI, Google Gemini API (`1.5 Flash` / `1.5 Pro`), ChromaDB, PlantUML, Git  
**Statut global :** Brique 1 terminée, Brique 2 en cours  

---

## 🎯 Objectif du Projet
Construire une plateforme open-source autonome d'ingénierie d'architecture basée sur une brigade de 8 agents spécialisés coordonnés par un orchestrateur, capable de générer des dossiers d'architecture (DAT), des schémas C4 PlantUML, des backlogs Jira avec DoD et d'assurer sa propre maintenance via un Meta-Agent.

---

## 📊 Matrice d'Avancement Global

| Brique | Intitulé | Priorité | Statut | Dépendances |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Socle Technique, Modularité & Connecteur Gemini** | P0 (Critique) | 🟢 **Terminé** | Clé API Gemini |
| **2** | **Brigade d'Agents Spécialisés d'Architecture** | P1 (Haute) | 🟡 **En cours** | Brique 1 |
| **3** | **Module RAG & Base de Connaissances (ChromaDB)** | P1 (Haute) | ⚪ En attente | Brique 1 |
| **4** | **Générateurs de Livrables & Outil GitPublisher (HITL)** | P2 (Moyenne) | ⚪ En attente | Briques 2 & 3 |
| **5** | **Méta-Gouvernance (Meta-Agent) & Personal Branding** | P2 (Moyenne) | ⚪ En attente | Brique 4 |

---

## 🧱 Détail des Briques d'Implémentation

### Brique 1 : Socle Technique, Modularité & Connecteur Gemini 🟢
*Objectif : Transformer le script unique en une architecture logicielle propre et brancher le moteur Gemini.*

*   [x] **1.1 Restructuration modulaire du code :**
    *   `src/config/` : Configuration et chargement sécurisé du `.env`.
    *   `src/agents/` : Fabrique des agents avec personas TOGAF.
    *   `src/tasks/` : Tâches d'architecture paramétrées.
    *   `src/main.py` : Point d'entrée avec gestion des arguments (`--language`, `--input`, `--output`).
*   [x] **1.2 Intégration robuste de Gemini :**
    *   Configuration du modèle `gemini-1.5-flash` pour les agents ouvriers.
    *   Configuration du modèle `gemini-1.5-pro` pour le Manager Orchestrateur.
    *   Synchronisation automatique de la clé API pour LangChain et Google GenAI.
*   [x] **1.3 Prise en compte du paramètre multi-langues :**
    *   Injection stricte de `--language` dans les descriptions et sorties attendues des tâches.
*   [x] **1.4 Actualisation des dépendances :**
    *   `requirements.txt` enrichi avec `langchain-google-genai` et `pytest`.

---

### Brique 2 : Brigade d'Agents Spécialisés d'Architecture 🟡
*Objectif : Déployer les personas d'architecture selon les phases TOGAF B, C et D.*

*   [x] **2.1 Agent CISO / Sécurité :**
    *   Analyse des classifications de données (C1, C2, C2 massif, RGPD).
    *   Vérification des exigences de chiffrement au repos/en transit, gestion des secrets, conformité Zero-Trust (NIST SP 800-207).
    *   Tâche d'audit de sécurité et avis d'homologation DCA formel.
*   [x] **2.2 Agent Software Crafter & Domain-Driven Design (DDD) :**
    *   Maître des micro-patterns logiciels (Architecture Hexagonale Ports & Adapters, découplage métier).
    *   Garantie de la testabilité unitaire (TDD 100%), des principes SOLID et de la simplicité (KISS/YAGNI).
    *   Tâche `create_software_crafting_task` implémentée et testée.
*   [x] **2.3 Agent SAFe System Architect & Agile Delivery Enabler :**
    *   Traduction automatique du DAT en éléments de backlog Jira (Enabler Epics, Enabler Features, User Stories techniques).
    *   Critères d'acceptation opérationnels et Definition of Done (DoD) pour les trains SAFe (ART).
    *   Tâche `create_safe_delivery_task` implémentée et testée.
*   [x] **2.4 Agent Challenger / Red Team (Pattern Reflection & Critique) :**
    *   Identification proactive des SPOF (Single Points of Failure).
    *   Challenger les choix du Solution Architect (scalabilité, résilience, sur-ingénierie, Golden Hammer).
    *   Tâche d'audit contradictoire `create_challenge_task` et tests unitaires au vert.
*   [ ] **2.5 Agent Migration, FinOps & TCO :**
    *   Estimation des coûts comparatifs (On-premise vs Cloud IaaS/PaaS/SaaS).
    *   Scénarios de transition et jalons de bascule progressive.
*   [x] **2.6 Câblage complet des tâches & pipeline dans `src/main.py` :**
    *   Séquence d'élite opérationnelle : Solution ➔ Challenger ➔ CISO ➔ Crafter ➔ SAFe Enabler.
    *   Test d'intégration complet `test_full_pipeline_assembly` validé.

---

### Brique 3 : Module RAG & Base de Connaissances (ChromaDB) ⚪
*Objectif : Permettre aux agents d'interroger la doctrine d'architecture et des blueprints d'entreprise.*

*   [ ] **3.1 Création du répertoire de connaissances (`knowledge/`) :**
    *   Dossier de documentation de référence (templates de DAT, matrices de flux, patterns hexagonaux/microservices).
*   [ ] **3.2 Mise en place du moteur vectoriel :**
    *   Intégration de ChromaDB en mode local (léger, sans infrastructure lourde).
    *   Pipeline d'ingestion et d'indexation vectorielle via les embeddings Gemini.
*   [ ] **3.3 Tool RAG pour CrewAI :**
    *   Création d'un outil `KnowledgeSearchTool` utilisable nativement par le Solution Architect et le CISO.

---

### Brique 4 : Générateurs de Livrables & Outil GitPublisher ⚪
*Objectif : Automatiser la restitution sous des formats standardisés exploitables et la publication Git sécurisée.*

*   [ ] **4.1 Générateur de Dossier d'Architecture Technique (`DAT.md`) :**
    *   Structure normalisée (Vision, Besoins Non Fonctionnels, Architecture Applicative, Données, Déploiement).
*   [ ] **4.2 Générateur de Schémas C4 PlantUML (`.puml`), Mermaid (`.mmd`) et Draw.io (`.drawio`) :**
    *   Production de schémas autonomes sans `!include` externe (rendu garanti en réseau restreint).
*   [ ] **4.3 Adaptateur déterministe `GitPublisher` (Non-IA) :**
    *   Scan anti-secrets (détection de tokens, `.env`, clés privées).
    *   Génération de message conventionnel (`Conventional Commits`).
    *   Porte bloquante Human-in-the-Loop (`[O/N]`) avant tout `git push`.
*   [ ] **4.4 Générateur d'export de backlog Jira :**
    *   Export CSV/JSON des User Stories et DoD prêt pour import dans Jira.

---

### Brique 5 : Méta-Gouvernance, Personal Branding & Auto-Maintenance ⚪
*Objectif : Assurer la maintenance autonome du système et la valorisation professionnelle continue.*

*   [ ] **5.1 Meta-Agent (Agent Zero - Self-Healing) :**
    *   Observabilité des logs d'exécution de la Crew, latence et consommation de tokens.
    *   Détection des dérives de prompt et génération de patchs sur `src/agents/` ou `src/tasks/`.
*   [ ] **5.2 Agent Carrière & Personal Branding :**
    *   Mise à jour dynamique du CV à partir des technologies et patterns traités dans les DATs.
    *   Génération de brouillons de posts LinkedIn (retours d'expérience / REX vulgarisés).
    *   Cartographie continue vers les certifications visées (TOGAF 10, SAFe for Architects, Cloud WAF, L2 interne).

---

## 🛠️ Règles de Contribution & Bonnes Pratiques
1. **Architecture as Code :** Tout livrable doit être versionné sous forme de fichier texte lisible (Markdown, PlantUML, YAML, Python).
2. **Agnosticisme linguistique :** Toujours valider le bon fonctionnement avec les options `--language "French"` et `--language "English"`.
3. **Sécurité :** Ne jamais commiter de clés d'API ni d'adresses IP réelles dans le dépôt Git.
