# Multi-Agent Architecture Platform (AAP)

[![CI Quality Pipeline](https://github.com/widadsaghir/my-agentic-architecture/actions/workflows/ci.yml/badge.svg)](https://github.com/widadsaghir/my-agentic-architecture/actions/workflows/ci.yml)
![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![Tests](https://img.shields.io/badge/tests-48%20passed-brightgreen.svg)
![Architecture](https://img.shields.io/badge/architecture-hexagonal%20%7C%20TOGAF%2010-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Multi-Agent Architecture Platform (AAP)** is a 100% open-source, autonomous multi-agent engineering platform designed to act as an expert **Lead Solution & Enterprise Architect**. 

Orchestrated with **CrewAI** and powered by **Google Gemini API**, it mobilizes a specialized brigade of 9 agents adhering to the highest industry standards: **TOGAF 10 ADM**, **SAFe 6 for Architects**, **Software Craftsmanship (Hexagonal / DDD / TDD)**, **Zero-Trust Security (NIST SP 800-207)**, and **FinOps Cloud Economics**.

---

## 📁 Project Architecture & Annotated Tree

```text
my-agentic-architecture/
├── .github/workflows/          # ⚙️ Pipeline CI/CD GitHub Actions (45 tests auto)
│   └── ci.yml                  #    Déclenchement automatique à chaque push / PR
├── src/                        # 💎 Cœur applicatif (Architecture Hexagonale)
│   ├── agents/                 # 👥 La Brigade des 9 agents d'architecture (TOGAF/SAFe)
│   │   ├── architect_agents.py #    Fabrique des agents (Manager, Solution, Challenger, CISO...)
│   │   └── __init__.py         #    Exposition des fabriques d'agents
│   ├── tasks/                  # 📋 Les 8 tâches séquentielles paramétrées
│   │   ├── architecture_tasks.py#   Définition des tâches avec injection stricte de langue
│   │   └── __init__.py         #    Exposition des tâches d'architecture
│   ├── tools/                  # 🛠️ Adaptateurs déterministes (0 Token / Outils purs)
│   │   ├── knowledge_rag.py    #    Moteur RAG ChromaDB & outil KnowledgeSearchTool
│   │   ├── diagram_exporter.py #    Générateur de schémas (Draw.io, PlantUML, Mermaid)
│   │   ├── jira_exporter.py    #    Exportateur de backlog Jira en CSV (Excel FR)
│   │   ├── git_publisher.py    #    Publication Git sécurisée & arbitrage HITL [O/N]
│   │   ├── log_analyzer.py     #    Observabilité et analyse des traces d'exécution
│   │   ├── career_exporter.py  #    Mise à jour CV et génération de posts LinkedIn REX
│   │   └── __init__.py         #    Exposition des adaptateurs d'infrastructure
│   ├── config/                 # ⚙️ Configuration & Gestion des Environnements
│   │   ├── settings.py         #    Chargement fail-fast du .env et mapping Gemini
│   │   └── __init__.py
│   └── main.py                 # 🚀 Orchestrateur CLI (support --language, --study-dir, HITL)
├── knowledge/doctrine/         # 📚 Base de connaissances doctrinale indexée en RAG
│   ├── 01_principes_securite_zero_trust_c2.md      # Doctrine SSI & Homologation DCA
│   ├── 02_principes_craftsmanship_hexagonale.md     # Architecture Hexagonale & DDD
│   ├── 03_patrons_cloud_waf_et_resilience.md       # Cloud Well-Architected Framework
│   ├── 04_gouvernance_safe_enablers_dod.md         # Découpage Jira & Definition of Done
│   └── 05_conformite_et_non_derive_architecture.md # Contrôle anti-dérive & RTM
├── docs/                       # 📖 Dossiers d'architecture & gouvernance
│   ├── etudes/                 # 📁 Packs d'études complets produits (10 artéfacts par étude)
│   │   └── migration_ssas_cloud/#   Étude témoin NovaAnalytics (DAT, DCA, FinOps, Jira...)
│   ├── diagrams/               # 🖼️ Schémas sources multi-formats (.drawio, .puml, .mmd)
│   ├── architecture-cible-togaf.md           # 🏛️ Dossier d'Architecture Cible TOGAF 10
│   ├── craftsmanship-safe-testing-strategy.md # 🧪 Référentiel des 45 tests & 5 patterns
│   ├── dossier-architecture-visuelle.md       # 🎨 Dossier visuel C4 et living doc
│   └── roadmap-implementation.md              # 🗺️ Feuille de route (Briques 1 à 5 terminées)
├── tests/unit/                 # 🛡️ Pyramide des 45 tests unitaires et d'architecture (0 token)
│   ├── test_hexagonal_architecture.py    # Tests d'Architecture par AST (isolation des couches)
│   ├── test_architecture_conformance.py # Architectural Fitness Functions (anti-dérive)
│   ├── test_diagram_syntax.py           # Anti-régression syntaxe schémas (Mermaid, PlantUML)
│   ├── test_data_anonymization.py       # Privacy Guard (0 IP privée RFC 1918, 0 secret)
│   ├── test_cli_resilience.py           # Résilience CLI et arborescences imbriquées
│   ├── test_e2e_mocked_crew.py          # Exécution E2E complète Mockée (0 token en < 2s)
│   └── ...                              # Tests des agents, tâches, config et adaptateurs
├── setup.ps1                   # ⚡ Script d'installation automatisée en 1 clic (PowerShell)
└── requirements.txt            # 📦 Dépendances Python (CrewAI, ChromaDB, Pytest)
```

---

## 👥 La Brigade Complète des 9 Agents Spécialisés

| Rôle Agent | Type | Framework | Mission Principale |
| :--- | :--- | :--- | :--- |
| **👑 Lead Architecture Manager** | Orchestrateur | TOGAF 10 & SAFe 6 | Pilote le cycle de vie, répartit les tâches et rédige la synthèse exécutive. |
| **🏗️ Solution & Infra Architect** | Constructif (Macro) | Cloud WAF & EDA | Conçoit les macro-patterns (Kafka, Outbox, Private Endpoints) avec le RAG. |
| **🎯 Challenger / Red Team** | Évaluateur | Heuristiques SRE | Traque la sur-ingénierie (*Golden Hammer*), les SPOF et impose KISS/YAGNI. |
| **🛡️ CISO & Data Protection** | Garde Sécurité | Zero-Trust & RGPD | Audit de classification C2 MASSIF, chiffrement CMK et avis d'homologation DCA. |
| **💎 Software Crafter & DDD** | Constructif (Micro) | Hexagonale & Clean Code | Isole le domaine métier (Ports & Adapters) et garantit la testabilité unitaire. |
| **🚆 SAFe Agile Delivery Enabler** | Delivery Agile | SAFe 6 ART | Découpe l'architecture en Enabler Epics, Features et User Stories Jira avec DoD. |
| **💰 Migration & FinOps / TCO** | Économiste Cloud | FinOps Foundation | Chiffre le TCO comparatif (Cloud vs On-Premise) et le calendrier de bascule. |
| **🔧 Meta-Agent (Agent Zero)** | Méta-Supervision | Self-Healing / SRE | Supervise les logs d'exécution, détecte les dérives et propose des patchs. |
| **📈 Agent Carrière & Branding** | Valorisation | Career Management | Met à jour le CV de l'architecte et rédige des brouillons de posts LinkedIn (REX). |

---

## 🚀 Prise en Main Rapide (Installation & Exécution)

### Option A : Installation Automatisée en 1 Clic (PowerShell)
```powershell
.\setup.ps1
```
Renseignez votre clé API Gemini dans le fichier `.env` généré :
```ini
GEMINI_API_KEY=votre_cle_gemini_ici
```

### Option B : Exécution d'une Étude d'Architecture
```powershell
# 1. Activer l'environnement virtuel
.\.venv\Scripts\Activate.ps1

# 2. Lancer la brigade en français avec export du pack documentaire complet
python src/main.py --language "French" --input "docs/exemples/cadrage_migration_ssas_cloud.md" --study-dir "docs/etudes/ma_nouvelle_etude" --publish-git
```

---

## 🧪 Built-in Quality & Pytest (48 Tests Déterministes à 0 Token)

La suite de tests automatisée s'exécute en **moins de 36 secondes** sans consommer le moindre jeton LLM :

```powershell
pytest -v
```

```text
======================= 48 passed, 153 warnings in 35.77s =======================
```

Pour consulter le détail des 5 patterns d'ingénierie logicielle (Architectural Fitness Functions, Defect-Driven Testing, Mock E2E, Privacy Guard, Contract Validation), référez-vous au document :  
👉 **`docs/craftsmanship-safe-testing-strategy.md`**.

---

## 🛠️ Instancier votre Propre Brigade (Framework AAP Meta-Prompt)

Vous souhaitez créer une flotte d'agents spécialisés sur un autre domaine d'entreprise (Cybersécurité / SOC, Audit RGPD / DORA, Plateforme MLOps, Cadrage FinOps Cloud) ?  

Le méta-moule industriel complet du **Framework AAP (V3)** est disponible dans :  
👉 **`docs/templates/meta_prompt_generateur_brigade.md`**

Il contient le cahier des charges, la structure modulaire, les 10 piliers d'ingénierie logicielle, les contrats de tests et le prompt prêt à l'emploi avec comparatif des gains de temps (~97.9% d'économie).
