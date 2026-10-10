# Cartographie d'Architecture du Projet : Multi-Agent Architecture Platform (AAP)

Ce répertoire regroupe les diagrammes d'architecture du projet, déclinés en **PlantUML (`.puml`)** pour les rendus formels et en **Mermaid (`.mmd`)** pour la visualisation native dans GitHub et vos documents Markdown.

---

## 1. C4 Model — Niveau 1 : Contexte Système

Ce diagramme positionne la plateforme dans son environnement direct, avec ses utilisateurs et ses dépendances externes.

### Visualisation Mermaid :
```mermaid
flowchart TD
    User["👤 Lead Architect (Human-in-the-Loop)"]
    AAP["🖥️ Multi-Agent Architecture Platform (AAP)<br/><i>Plateforme multi-agents CrewAI & Gemini</i>"]
    Knowledge["📚 Doctrine & Sources de Connaissance<br/><i>Blueprints, DAT templates, TOGAF</i>"]
    GeminiAPI["☁️ Google Gemini API<br/><i>Gemini 1.5 Pro & 1.5 Flash</i>"]
    GitRepo["📦 Dépôt Git & Livrables<br/><i>DAT.md, Schémas .puml, Decks</i>"]

    User -->|"1. Paramètres (--language, --input) & validation HITL"| AAP
    AAP -->|"2. Interrogation RAG"| Knowledge
    AAP -->|"3. Requêtes d'inférence LLM"| GeminiAPI
    AAP -->|"4. Sauvegarde des livrables"| GitRepo
    AAP -->|"5. Restitution du rapport validé"| User

    style User fill:#D4E6F1,stroke:#2980B9,stroke-width:2px
    style AAP fill:#AED6F1,stroke:#1F618D,stroke-width:3px
    style Knowledge fill:#D5F5E3,stroke:#27AE60,stroke-width:2px
    style GeminiAPI fill:#FCF3CF,stroke:#F39C12,stroke-width:2px
    style GitRepo fill:#EDBB99,stroke:#D35400,stroke-width:2px
```

* **Fichier PlantUML source :** [`c4_level1_system_context.puml`](./c4_level1_system_context.puml)
* **Fichier Mermaid source :** [`c4_level1_system_context.mmd`](./c4_level1_system_context.mmd)
* **Fichier Draw.io natif :** [`c4_level1_system_context.drawio`](./c4_level1_system_context.drawio)

---

## 2. C4 Model — Niveau 2 : Conteneurs Applicatifs

Ce diagramme détaille les briques logicielles internes de la plateforme Python (CLI, Configuration, Orchestrateur, Agents, RAG et Exportateurs).

### Visualisation Mermaid :
```mermaid
flowchart TB
    User["👤 Lead Architect (Human-in-the-Loop)"]
    GeminiService["☁️ Google Gemini Cloud Service<br/><i>gemini-1.5-flash & gemini-1.5-pro</i>"]
    LocalFS["💾 Système de Fichiers & Git<br/><i>DAT.md, Schémas .puml, .env</i>"]

    subgraph AAP ["🖥️ Multi-Agent Architecture Platform (AAP)"]
        direction TB
        CLI["💻 Interface CLI (main.py)<br/><i>argparse (--language, --input)</i>"]
        ConfigMgr["⚙️ Config & LLM Manager (settings.py)<br/><i>dotenv, LangChain Google GenAI</i>"]
        CrewEngine["🧠 Moteur CrewAI<br/><i>Processus d'orchestration</i>"]
        
        subgraph Fleet ["👥 Brigade d'Agents Spécialisés"]
            ManagerAgent["👑 Manager (TOGAF Lead)"]
            SolutionAgent["🏗️ Solution Architect"]
            CisoAgent["🛡️ CISO (Sécurité/C2)"]
            ChallengerAgent["🎯 Challenger (Red Team)"]
        end

        TaskFactory["📋 Fabrique de Tâches<br/><i>Injection langue & contraintes</i>"]
        VectorDB["🗄️ Base RAG (ChromaDB)<br/><i>Indexation blueprints & normes</i>"]
        Exporter["📤 Exportateur de Livrables<br/><i>Générateur DAT & PlantUML</i>"]
    end

    User -->|"Lance la commande CLI"| CLI
    CLI -->|"Charge la config"| ConfigMgr
    ConfigMgr -->|"Connecte les LLMs"| GeminiService
    CLI -->|"Déclenche l'orchestration"| CrewEngine
    CrewEngine -->|"Coordonne"| Fleet
    Fleet -->|"Reçoit les instructions"| TaskFactory
    Fleet -->|"Interroge les patterns"| VectorDB
    Fleet -->|"Inférences LLM"| GeminiService
    CrewEngine -->|"Consolide les livrables"| Exporter
    Exporter -->|"Écrit les fichiers"| LocalFS
    CLI -->|"Restitue la synthèse"| User

    style User fill:#D4E6F1,stroke:#2980B9,stroke-width:2px
    style GeminiService fill:#FCF3CF,stroke:#F39C12,stroke-width:2px
    style LocalFS fill:#EDBB99,stroke:#D35400,stroke-width:2px
    style AAP fill:#F2F4F4,stroke:#7F8C8D,stroke-width:2px
    style Fleet fill:#E8F8F5,stroke:#1ABC9C,stroke-width:2px
```

* **Fichier PlantUML source :** [`c4_level2_container.puml`](./c4_level2_container.puml)
* **Fichier Mermaid source :** [`c4_level2_container.mmd`](./c4_level2_container.mmd)
* **Fichier Draw.io natif :** [`c4_level2_container.drawio`](./c4_level2_container.drawio)

---

## 3. Diagramme de Séquence : Workflow d'Exécution & Reflection Loop

Ce diagramme illustre le flux séquentiel des échanges, de la commande utilisateur jusqu'à la boucle contradictoire avec le Challenger et l'export des fichiers.

### Visualisation Mermaid :
```mermaid
sequenceDiagram
    autonumber
    actor User as 👤 Lead Architect (HITL)
    participant CLI as 💻 CLI (src/main.py)
    participant Config as ⚙️ Config & LLMs
    participant Manager as 👑 Manager (TOGAF)
    participant Solution as 🏗️ Solution Architect
    participant RAG as 🗄️ Base RAG (ChromaDB)
    participant Challenger as 🎯 Challenger (Red Team)
    participant Gemini as ☁️ Google Gemini API
    participant FS as 💾 Système de Fichiers

    %% Étape 1
    rect rgb(235, 245, 251)
    note right of User: Étape 1 : Initialisation
    User->>CLI: python src/main.py --language "French" --input "..."
    CLI->>Config: get_config() & instancie LLMs
    Config-->>CLI: worker_llm (Flash) & manager_llm (Pro)
    CLI->>CLI: Prépare les agents & la tâche (injection langue)
    end

    %% Étape 2
    rect rgb(234, 250, 241)
    note right of CLI: Étape 2 : Orchestration & Conception
    CLI->>Manager: crew.kickoff()
    Manager->>Solution: Délègue l'analyse d'architecture
    Solution->>RAG: Requête de patterns similaires
    RAG-->>Solution: Blueprints & templates
    Solution->>Gemini: Inférence (Prompt + RAG) [Gemini Flash]
    Gemini-->>Solution: Ébauche d'architecture
    end

    %% Étape 3
    rect rgb(253, 237, 236)
    note right of Solution: Étape 3 : Boucle Critique (Red Team)
    Solution->>Challenger: Soumission pour audit contradictoire
    Challenger->>Gemini: Analyse des failles & SPOF [Gemini Flash]
    Gemini-->>Challenger: Critique & risques
    Challenger-->>Solution: Recommandations de correction
    Solution->>Solution: Ajustement de l'architecture
    Solution-->>Manager: Architecture consolidée
    end

    %% Étape 4
    rect rgb(254, 249, 231)
    note right of Manager: Étape 4 : Synthèse & Validation HITL
    Manager->>Gemini: Synthèse DAT finale en langue cible [Gemini Pro]
    Gemini-->>Manager: Dossier d'architecture finalisé
    Manager-->>CLI: Résultat de la Crew
    CLI->>User: 🛑 Présentation pour validation Human-in-the-Loop
    User->>CLI: Approbation formelle
    CLI->>FS: Sauvegarde DAT.md et schémas .puml
    FS-->>CLI: Fichiers écrits
    CLI-->>User: Affichage du livrable et confirmation
    end
```

* **Fichier PlantUML source :** [`sequence_architecture_workflow.puml`](./sequence_architecture_workflow.puml)
* **Fichier Mermaid source :** [`sequence_architecture_workflow.mmd`](./sequence_architecture_workflow.mmd)
