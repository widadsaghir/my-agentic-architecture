# Multi-Agent Architecture Platform (AAP)

[![CI Quality Pipeline](https://github.com/widadsaghir/my-agentic-architecture/actions/workflows/ci.yml/badge.svg)](https://github.com/widadsaghir/my-agentic-architecture/actions/workflows/ci.yml)
![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![Tests](https://img.shields.io/badge/tests-65%20passed-brightgreen.svg)
![Architecture](https://img.shields.io/badge/architecture-hexagonal%20%7C%20TOGAF%2010-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Multi-Agent Architecture Platform (AAP)** is a 100% open-source, autonomous multi-agent engineering platform designed to act as an expert **Lead Solution & Enterprise Architect** and an executive **Speech & Presentation Restitution Board**.

Orchestrated with **CrewAI** and powered by **Google Gemini API**, it mobilizes 3 specialized colleges adhering to the highest industry standards: **TOGAF 10 ADM**, **SAFe 6 for Architects**, **Software Craftsmanship (Hexagonal / DDD / TDD)**, **Zero-Trust Security (NIST SP 800-207)**, **GreenOps & FinOps Cloud Economics**, and **TEDx Executive Prompter Storytelling**.

---

## 📁 Project Architecture & Annotated Tree

```text
my-agentic-architecture/
├── .github/workflows/          # ⚙️ Pipeline CI/CD GitHub Actions (65 tests auto)
│   └── ci.yml                  #    Déclenchement automatique à chaque push / PR
├── src/                        # 💎 Cœur applicatif (Architecture Hexagonale)
│   ├── agents/                 # 👥 Les Brigades d'Agents Spécialisés
│   │   ├── architect_agents.py         # Brigade TOGAF / SAFe (Manager, Solution, Challenger, CISO...)
│   │   ├── virtual_committee_agents.py # Les 5 Maîtres (Fowler, Uncle Bob, Vogels, Cockburn, Newman) + GreenOps/FinOps + Juge Qualité
│   │   ├── orator_agents.py            # Les 5 Orateurs Légendaires (Hassan II, Jobs, MLK, Churchill, Obama) + Metteur en Scène + Juge
│   │   └── __init__.py                 # Exposition unifiée des fabriques d'agents
│   ├── orchestration/          # 🔄 Moteur Déterministe de Bouclage (Self-Correction Loops)
│   │   ├── loop_controller.py  # Contrôle des cycles de révision, scoring sur 100, feedback prompts & coupe-circuit
│   │   └── __init__.py
│   ├── tasks/                  # 📋 Définitions des Tâches Spécialisées
│   │   ├── architecture_tasks.py       # Tâches DAT TOGAF (Conception, Challenge, DCA, Craft, FinOps...)
│   │   ├── virtual_committee_tasks.py  # Tâches d'audit des 5 Maîtres, scoring Quality Gate et synthèse
│   │   ├── orator_tasks.py             # Tâches de table ronde oratoire, fusion scénique, jugement et pack prompter
│   │   └── __init__.py                 # Exposition unifiée des tâches
│   ├── tools/                  # 🛠️ Adaptateurs déterministes (0 Token / Outils purs)
│   │   ├── knowledge_rag.py            # Moteur RAG ChromaDB & outil KnowledgeSearchTool
│   │   ├── diagram_exporter.py         # Générateur de schémas (Draw.io, PlantUML, Mermaid)
│   │   ├── presentation_exporter.py    # Générateur de slides 16:9 Haute Couture Bento Grid
│   │   ├── executive_prompter_exporter.py # Téléprompteur interactif HTML Single-Slide & Prompter Markdown
│   │   ├── jira_exporter.py            # Exportateur de backlog Jira en CSV (Excel FR avec ;)
│   │   ├── git_publisher.py            # Publication Git sécurisée & arbitrage HITL [O/N]
│   │   ├── log_analyzer.py             # Observabilité Meta-Agent et santé système
│   │   ├── career_exporter.py          # Mise à jour CV et génération de posts LinkedIn REX
│   │   └── __init__.py                 # Exposition des adaptateurs d'infrastructure
│   ├── config/                 # ⚙️ Configuration & Gestion des Environnements
│   │   ├── settings.py         # Chargement fail-fast du .env et mapping Gemini
│   │   └── __init__.py
│   └── main.py                 # 🚀 Orchestrateur CLI (modes togaf, committee, speech, full)
├── knowledge/doctrine/         # 📚 Base de connaissances doctrinale indexée en RAG
│   ├── 01_principes_securite_zero_trust_c2.md      # Doctrine SSI & Homologation DCA
│   ├── 02_principes_craftsmanship_hexagonale.md     # Architecture Hexagonale & DDD
│   ├── 03_patrons_cloud_waf_et_resilience.md       # Cloud Well-Architected Framework
│   ├── 04_gouvernance_safe_enablers_dod.md         # Découpage Jira & Definition of Done
│   └── 05_conformite_et_non_derive_architecture.md # Contrôle anti-dérive & RTM
├── docs/                       # 📖 Dossiers d'architecture & gouvernance
│   ├── etudes/                 # 📁 Packs d'études complets produits (DAT, DCA, FinOps, Jira...)
│   ├── presentation/           # 🎙️ Kit de restitution exécutif (Slides Haute Couture & Prompter)
│   └── CONTEXTE_PROJET.md      # 📋 Journal de bord et spécifications vivantes du projet
├── tests/unit/                 # 🛡️ Pyramide des 65 tests unitaires et d'architecture (0 token)
│   ├── test_loop_controller.py           # Tests du contrôleur de boucle d'auto-correction
│   ├── test_virtual_committee.py         # Tests des agents et tâches du Comité des 5 Maîtres
│   ├── test_orator_committee.py          # Tests des agents et tâches du Conseil des Orateurs
│   ├── test_executive_prompter_exporter.py # Tests de l'exportateur prompter TEDx
│   ├── test_e2e_virtual_committee_loop.py # Simulation E2E du rebouclage d'auto-correction
│   ├── test_hexagonal_architecture.py    # Tests d'Architecture par AST (isolation des couches)
│   ├── test_architecture_conformance.py  # Architectural Fitness Functions (anti-dérive)
│   └── ...
├── setup.ps1                   # ⚡ Script d'installation automatisée en 1 clic (PowerShell)
└── requirements.txt            # 📦 Dépendances Python (CrewAI, ChromaDB, Pytest)
```

---

## 🏛️ Les Trois Collèges d'Experts Disponibles

### 1. La Brigade Opérationnelle TOGAF & SAFe (Mode `--mode togaf`)
9 agents spécialisés pour produire le Dossier d'Architecture Technique (DAT) complet, le DCA de sécurité, la conception hexagonale, l'audit contradictoire, le TCO FinOps et le backlog Jira.

### 2. Le Comité d'Architecture Virtuel des 5 Maîtres & Green/FinOps (Mode `--mode committee`)
Un collège de référence mondiale challengeant l'architecture en boucle itérative jusqu'à l'excellence :
- **Martin Fowler** : Patterns d'entreprise (*P of EAA*), évolutivité et trajectoire de refactoring.
- **Robert C. Martin (Uncle Bob)** : Clean Architecture, principes SOLID et étanchéité absolue du domaine métier.
- **Werner Vogels** : Cloud Resilience, *Design for Failure* (« Everything fails all the time ») et anti-SPOF.
- **Alistair Cockburn** : Architecture Hexagonale (Ports & Adaptateurs) et testabilité sans mocks.
- **Sam Newman** : Décomposition des monolithes, microservices DDD et Loi de Conway.
- **GreenOps & FinOps Architect** : Sobriété numérique (gCO2eq), modélisation TCO et Right-Sizing.
- **Juge Qualité Technique** : Grille de scoring sur 100 et verdict binaire (`VALIDÉ` / `À REPRENDRE`).

### 3. Le Conseil d'Éloquence & Restitution TEDx (Mode `--mode speech`)
Un conseil d'administration virtuel d'orateurs légendaires pour composer le pitch parfait :
- **Hassan II** : Éloquence classique, hauteur de vue philosophique et noblesse métaphorique.
- **Steve Jobs** : Storytelling épuré, simplicité radicale, règle de trois et *One More Thing*.
- **Martin Luther King Jr.** : Émotion profonde (Pathos), rythme anaphorique et vision d'avenir.
- **Winston Churchill** : Formules martiales d'impact, verbes d'action et courage face à l'adversité.
- **Barack Obama** : Connexion empathique, fluidité et modulation des silences respiratoires.
- **Metteur en Scène & Juge d'Éloquence** : Fusion unifiée annotée (`[PAUSE 2s]`, `[BREATHE]`, `[SOURIRE]`, `[REGARD]`, `[↘ INTONATION FERME]`) et contrôle qualité sur 100.

---

## 🔄 Le Moteur de Bouclage Déterministe (`AgenticLoopController`)

Pour éviter les livrables tièdes ou incomplets, la plateforme applique le patron **Self-Correction Loop** :

```text
  [1. Production Initiale] ➔ [2. Table Ronde & Audit Croisé] ➔ [3. Juge Qualité (Score /100)]
                                                                           │
                                              ┌────────────────────────────┴──────────────────────────┐
                                              ▼                                                       ▼
                                    Score >= Seuil (ex: 85)                                 Score < Seuil (max 4 itérations)
                                  [Validation du Rapport Final]                         [Réinjection des Gaps dans le Prompt]
```

---

## 🚀 Prise en Main & Commandes CLI

### 1. Mode DAT TOGAF (Standard)
```powershell
python src/main.py --mode togaf --language "French" --input "docs/exemples/cadrage_migration_ssas_cloud.md" --study-dir "docs/etudes/mon_etude"
```

### 2. Mode Comité d'Architecture Virtuel (Les 5 Maîtres avec Boucle Qualité)
```powershell
python src/main.py --mode committee --min-score 85.0 --max-loops 4 --input "Cadrage de refonte du système de facturation" --study-dir "docs/etudes/comite_facturation"
```

### 3. Mode Conseil d'Éloquence (Pitch TEDx & Prompter Interactif)
```powershell
python src/main.py --mode speech --audience "Comité de Direction & Investisseurs" --input "docs/etudes/mon_etude/01_DOSSIER_ARCHITECTURE_TECHNIQUE_DAT.md" --study-dir "docs/etudes/speech_dir"
```

### 4. Mode Intégral Bout en Bout
```powershell
python src/main.py --mode full --min-score 88.0 --input "Cadrage plateforme événementielle" --study-dir "docs/etudes/full_pack"
```

---

## 🧪 Built-in Quality & Pytest (65 Tests Déterministes à 0 Token)

La suite de tests automatisée s'exécute en local sans consommer le moindre jeton LLM :

```powershell
pytest -v
```

```text
============================== 65 passed in ~50s ==============================
```

---

## 📂 Structure Détaillée du Projet

L'arborescence du projet applique une **Architecture Hexagonale stricte** séparant le domaine métier pur, les adaptateurs déterministes et l'orchestration cognitive :

```text
my-agentic-architecture/
├── .github/workflows/ci.yml       # Pipeline CI/CD GitHub Actions (65 tests)
├── .gitlab-ci.yml                 # Pipeline CI/CD GitLab (python:3.13-slim)
├── .gitignore                     # Exclusion des artefacts temporaires et caches
├── .geminiignore                  # Protection des clés et secrets
├── .aiexclude                     # Règle d'étanchéité des données
├── pytest.ini                     # Configuration de test ciblant tests/ (0 warning)
├── conftest.py                    # Injection automatique de la racine au sys.path
├── requirements.txt               # Dépendances déclarées (CrewAI, Pydantic, PyYAML...)
├── README.md                      # Documentation vitrine du projet
│
├── src/                           # Code source de la plateforme (Architecture Hexagonale)
│   ├── main.py                    # Point d'entrée de la CLI multi-modes (togaf, committee, speech, full)
│   ├── config/                    # Configuration et Circuit Breaker résilient (Google Gemini)
│   ├── domain/                    # Modèles purs et contrats d'interfaces (0 dépendance IA)
│   ├── tools/                     # 9 Adaptateurs déterministes à 0 token (RAG, Exporters, GitPublisher)
│   ├── agents/                    # 23 Personas d'élite (5 Maîtres, 5 Orateurs, FinOps, CISO...)
│   ├── tasks/                     # 24 Tâches séquentielles distillées
│   └── core/                      # Contrôleurs de boucle d'auto-correction (AgenticLoopController)
│
├── tests/                         # Suite de 65 tests TDD déterministes (0 Token)
│   └── unit/                      # Tests unitaires, fitness functions et simulations E2E
│
├── knowledge/                     # Base de connaissances RAG déterministe locale (sections Markdown)
│
└── docs/                          # Living Documentation & Restitutions d'Architecture
    ├── CONTEXTE_PROJET.md         # Journal de bord et état d'avancement des briques
    ├── architecture-cible-togaf.md # Spécification d'architecture cible
    ├── dossier-architecture-visuelle.md # Cartographie des flux et schémas C4
    ├── presentation/              # Slides interactives 16:9 et supports de démo vidéo
    ├── etudes/                    # Cas d'études réels (Billing, Migration Cloud, AWS Assessment)
    └── templates/                 # Modèles de livrables et méta-prompts d'ingénierie
```
