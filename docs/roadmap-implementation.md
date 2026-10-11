# Feuille de Route d'Implémentation : Multi-Agent Architecture Platform (AAP)

**Projet :** Multi-Agent Architecture Platform (AAP)  
**Référentiel méthodologique :** TOGAF ADM (Phases A à G) & SAFe Enabler  
**Technologies cibles :** Python 3.11+, CrewAI, Google Gemini API, ChromaDB, PlantUML  
**Statut global :** En cours — Démarrage de la Brique 1  

---

## 🎯 Objectif du Projet
Construire une plateforme open-source autonome d'ingénierie d'architecture basée sur une brigade d'agents spécialisés coordonnés par un orchestrateur, capable de générer des dossiers d'architecture (DAT), des schémas C4 PlantUML et des dossiers d'arbitrage dans n'importe quelle langue cible (`--language`).

---

## 📊 Matrice d'Avancement Global

| Brique | Intitulé | Priorité | Statut | Dépendances |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Socle Technique, Modularité & Connecteur Gemini** | P0 (Critique) | 🟢 **Terminé** | Clé API Gemini |
| **2** | **Brigade d'Agents Spécialisés (CISO, Challenger, TCO)** | P1 (Haute) | 🟡 **À faire** | Brique 1 |
| **3** | **Module RAG & Base de Connaissances (ChromaDB)** | P1 (Haute) | ⚪ En attente | Brique 1 |
| **4** | **Générateurs de Livrables (DAT.md, PlantUML, Decks)** | P2 (Moyenne) | ⚪ En attente | Briques 2 & 3 |
| **5** | **Meta-Agent, Branding & Gouvernance HITL** | P2 (Moyenne) | ⚪ En attente | Brique 4 |

---

## 🧱 Détail des Briques d'Implémentation

### Brique 1 : Socle Technique, Modularité & Connecteur Gemini
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
    *   `requirements.txt` enrichi avec `langchain-google-genai`.

---

### Brique 2 : Brigade d'Agents Spécialisés
*Objectif : Déployer les personas d'architecture selon les phases TOGAF B, C et D.*

*   [x] **2.1 Agent CISO / Sécurité :**
    *   Analyse des classifications de données (C1, C2, C2 massif).
    *   Vérification des exigences de chiffrement au repos/en transit, gestion des secrets, conformité Zero-Trust (NIST SP 800-207).
    *   Tâche d'audit de sécurité et avis d'homologation DCA formel.
*   [x] **2.2 Agent Software Crafter & Domain-Driven Design (DDD) :**
    *   Maître des micro-patterns logiciels (Architecture Hexagonale Ports & Adapters, découplage métier).
    *   Garantie de la testabilité unitaire (TDD), des principes SOLID et de la simplicité (KISS/YAGNI).
*   [x] **2.3 Agent SAFe System Architect & Agile Delivery Enabler :**
    *   Traduction automatique du DAT en éléments de backlog Jira (Enabler Epics, Enabler Features, User Stories techniques).
    *   Critères d'acceptation opérationnels et Definition of Done (DoD) pour les trains SAFe (ART).
*   [ ] **2.4 Agent Challenger / Red Team (Pattern Reflection & Critique) :**
    *   Identification proactive des SPOF (Single Points of Failure).
    *   Challenger les choix du Solution Architect (scalabilité, résilience, sur-ingénierie).
*   [ ] **2.5 Agent Migration, FinOps & TCO :**
    *   Estimation des coûts comparatifs (On-premise vs Cloud IaaS/PaaS/SaaS).
    *   Scénarios de transition et jalons de bascule.

---

### Brique 3 : Module RAG & Base de Connaissances (ChromaDB)
*Objectif : Permettre aux agents d'interroger la doctrine d'architecture et des blueprints d'entreprise.*

*   [ ] **3.1 Création du répertoire de connaissances (`knowledge/`) :**
    *   Dossier de documentation de référence (templates de DAT, matrices de flux, patterns hexagonaux/microservices).
*   [ ] **3.2 Mise en place du moteur vectoriel :**
    *   Intégration de ChromaDB en mode local (léger, sans infrastructure lourde).
    *   Pipeline d'ingestion et d'indexation vectorielle via les embeddings Gemini.
*   [ ] **3.3 Tool RAG pour CrewAI :**
    *   Création d'un outil `KnowledgeSearchTool` utilisable nativement par le Solution Architect et le CISO.

---

### Brique 4 : Générateurs de Livrables & Visualisation
*Objectif : Automatiser la restitution sous des formats standardisés exploitables directement.*

*   [ ] **4.1 Générateur de Dossier d'Architecture Technique (`DAT.md`) :**
    *   Structure normalisée (Vision, Besoins Non Fonctionnels, Architecture Applicative, Données, Déploiement).
*   [ ] **4.2 Générateur de Schémas C4 PlantUML (`.puml`) :**
    *   Production de schémas autonomes sans `!include` externe (rendu garanti en réseau restreint).
    *   Diagrammes de Contexte Système (C1) et de Conteneurs (C2).
*   [ ] **4.3 Générateur de Présentation Design Authority (Marp / Markdown PPT) :**
    *   Support visuel synthétique prêt pour les comités d'architecture.

---

### Brique 5 : Meta-Agent, Personal Branding & Gouvernance HITL
*Objectif : Assurer la maintenance autonome du système, la boucle de validation humaine et la valorisation professionnelle.*

*   [ ] **5.1 Porte de validation Human-in-the-Loop (HITL) :**
    *   Suspension de l'exécution avant tout commit Git ou validation formelle du DAT pour arbitrage par le Lead Architecte.
*   [ ] **5.2 Meta-Agent (Agent Zero - Self-Healing) :**
    *   Analyse des logs d'exécution, détection des échecs d'agents et proposition d'ajustements des prompts.
*   [ ] **5.3 Agent Carrière & Branding :**
    *   Mise à jour du CV et des compétences à partir des projets d'architecture traités.
    *   Veille sur les certifications cibles et génération de brouillons de posts de partage technique.

---

## 🛠️ Règles de Contribution & Bonnes Pratiques
1. **Architecture as Code :** Tout livrable doit être versionné sous forme de fichier texte lisible (Markdown, PlantUML, YAML, Python).
2. **Agnosticisme linguistique :** Toujours valider le bon fonctionnement avec les options `--language "French"` et `--language "English"`.
3. **Sécurité :** Ne jamais commiter de clés d'API ni d'adresses IP réelles dans le dépôt Git.
