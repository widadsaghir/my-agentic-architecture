# Framework AAP (V3) : Méthode & Meta-Prompt de Génération de Brigades Multi-Agents

**Projet :** Multi-Agent Architecture Platform (AAP)  
**Date :** 13 octobre 2026  
**Auteur :** Lead Enterprise & Solution Architect (Software Crafter)  
**Framework Référentiel :** TOGAF 10 ADM, SAFe 6 for Architects, Software Craftsmanship (Hexagonale / DDD / TDD 100%), Zero-Trust (NIST SP 800-207) & FinOps  
**Fichier :** `docs/templates/meta_prompt_generateur_brigade.md`  

---

## 🎯 Contexte & Objectif

Ce template formalise le méta-moule du **Framework AAP (Multi-Agent Architecture Platform)**. Il permet d'initialiser, d'architecturer, de tester et de livrer de A à Z une **nouvelle brigade multi-agents d'élite sur n'importe quel domaine d'entreprise** (ex : Cybersécurité / SOC, Audit Réglementaire RGPD / DORA, Plateforme MLOps, Gouvernance FinOps Cloud, Modernisation de Cœurs Applicatifs, etc.).

La méthode garantit contractuellement :
1. **L'application stricte des Agentic Design Patterns** : Orchestrator-Workers, Reflection & Critique (Challenger), Consensus Gate (Convergence ARB), Human-in-the-Loop souverain, Self-Healing (Meta-Agent / Agent Zero) et Personal Branding.
2. **La rigueur du Software Craftsmanship** : Architecture Hexagonale (Ports & Adaptateurs), séparation stricte Cognitif vs Déterministe (0 token), et TDD déterministe à 100%.
3. **La Pyramide Complète des 48 Tests Automatisés (Built-in Quality)** :
   * Tests d'Architecture par **AST** (preuve formelle d'isolation des outils sans framework d'IA).
   * **Architectural Fitness Functions** (contrôle anti-dérive entre spécification TO-BE et code réel).
   * **Anti-Régression Visuelle** (syntaxe Mermaid `-.->`, PlantUML Air-Gap sans remote include, Draw.io XML valide).
   * **Privacy Guard** (zéro fuite d'adresses IP privées RFC 1918 et zéro secret en clair).
   * **Linter Qualité Agile INVEST** (contrôle des tailles de stories $\le 8$ points et validation de la DoD).
   * **Exécution E2E Mockée** (chaîne complète des agents exécutée en $< 2\text{ s}$ à 0 token).
4. **La Triple Restitution Visuelle Obligatoire** : Tout schéma d'architecture est généré conjointement sous **Draw.io (`.drawio`)**, **PlantUML (`.puml`)** et **Mermaid (`.mmd`)**.
5. **Le Pack Documentaire d'Élite (11 Artéfacts)** incluant le cahier des charges d'entrée, l'arbitrage de convergence et l'export Jira CSV compatible Excel Français (point-virgule et UTF-8-sig).
6. **L'Amélioration Continue Systématique :** À chaque étude, analyse critique post-exécution proposant 3 à 5 pistes concrètes d'optimisation.
7. **L'Intégration Continue (CI/CD GitHub Actions)** exécutant l'intégralité des 48 tests à chaque commit.

---

## 📁 Structure Modulaire Standard d'un Projet Multi-Agents (Arborescence Annotée)

```text
mon-projet-agentic/
├── .github/workflows/          # ⚙️ Pipeline CI/CD GitHub Actions (48 tests auto à chaque push/PR)
│   └── ci.yml                  #    Exécution de la suite pytest sous Python 3.13 en environnement Ubuntu
├── src/                        # 💎 Cœur applicatif (Architecture Hexagonale)
│   ├── agents/                 # 👥 La Brigade des agents spécialisés (Manager, Workers, Évaluateurs)
│   │   ├── architect_agents.py #    Fabrique des agents avec personas et règles de non-délégation
│   │   └── __init__.py         #    Exposition des fabriques d'agents (__all__)
│   ├── tasks/                  # 📋 Les tâches séquentielles paramétrées
│   │   ├── architecture_tasks.py#   Définition des tâches avec injection stricte de langue (--language)
│   │   └── __init__.py         #    Exposition des tâches (__all__)
│   ├── tools/                  # 🛠️ Adaptateurs déterministes (Outils purs à 0 token)
│   │   ├── knowledge_rag.py    #    Moteur RAG ChromaDB local & outil KnowledgeSearchTool
│   │   ├── diagram_exporter.py #    Générateur & extracteur dynamique de schémas (Draw.io, PlantUML, Mermaid)
│   │   ├── jira_exporter.py    #    Exportateur de backlog Jira CSV (linter INVEST, délimiteur ; et UTF-8-sig)
│   │   ├── git_publisher.py    #    Publication Git sécurisée avec porte bloquante HITL [O/N]
│   │   ├── log_analyzer.py     #    Observabilité, analyse des traces et surveillance SRE
│   │   ├── career_exporter.py  #    Mise à jour dynamique de CV et génération de posts LinkedIn REX
│   │   └── __init__.py         #    Exposition des adaptateurs (__all__)
│   ├── config/                 # ⚙️ Configuration & Gestion fail-fast des variables
│   │   ├── settings.py         #    Circuit Breaker résilient, chargement du .env et mapping Gemini
│   │   └── __init__.py
│   └── main.py                 # 🚀 Orchestrateur CLI (support --language, --input fichier/texte, --study-dir, HITL)
├── knowledge/doctrine/         # 📚 Base de connaissances doctrinale indexée en base vectorielle (RAG)
│   ├── 01_doctrine_securite.md #    Règles SSI, Zero-Trust et homologation DCA
│   ├── 02_doctrine_craft.md    #    Architecture Hexagonale, DDD et TDD
│   └── ...                     #    Doctrines métier spécifiques
├── docs/                       # 📖 Dossiers d'architecture & gouvernance
│   ├── etudes/                 # 📁 Packs d'études complets produits (11 artéfacts par étude)
│   │   └── nom_etude/          #    Dossier dédié contenant l'input et l'output complet
│   │       ├── 00_CAHIER_DES_CHARGES_INPUT.md                 # 📥 Expression de besoin source archivée
│   │       ├── 00_DECISION_ARBITRAGE_ET_SYNTHESE_CONVERGENCE.md# ⚖️ Arbitrage ARB réconcilié
│   │       ├── 01_DOSSIER_ARCHITECTURE_TECHNIQUE_DAT.md       # 🏗️ Solution Architect
│   │       ├── 02_RAPPORT_AUDIT_CONTRADICTOIRE.md             # 🎯 Challenger Red Team
│   │       ├── 03_AVIS_HOMOLOGATION_SECURITE_DCA.md           # 🛡️ CISO & Zero-Trust
│   │       ├── 04_CONCEPTION_HEXAGONALE_ET_DDD.md             # 💎 Software Crafter
│   │       ├── 05_STRATEGIE_MIGRATION_ET_FINOPS_TCO.md        # 💰 FinOps & TCO
│   │       ├── 06_BACKLOG_LIVRAISON_SAFE_JIRA.md              # 🚆 SAFe Enabler
│   │       ├── 08_RAPPORT_OBSERVABILITE_ET_SANTE_SYSTEME.md   # 🩺 Meta-Agent SRE
│   │       ├── 09_VALORISATION_CARRIERE_ET_POST_LINKEDIN_REX.md# 🚀 Career Branding
│   │       ├── backlog_jira.csv                               # 📊 Backlog CSV (Excel FR ;)
│   │       └── diagrams/                                      # 🖼️ Schémas .drawio, .puml, .mmd
│   ├── cv_architecte.md        # 👤 CV dynamique de l'architecte enrichi post-mission
│   ├── architecture-cible.md   # 🏛️ Dossier d'Architecture Cible (TOGAF ADM)
│   ├── craftsmanship-safe-testing-strategy.md # 🧪 Référentiel des 48 tests et 5 patterns d'ingénierie
│   └── roadmap-implementation.md              # 🗺️ Feuille de route (Briques 1 à 5 terminées)
├── tests/unit/                 # 🛡️ Pyramide complète des 48 tests unitaires et d'architecture
│   ├── test_hexagonal_architecture.py    # Tests d'Architecture par AST (isolation stricte 0 token)
│   ├── test_architecture_conformance.py # Architectural Fitness Functions (contrôle anti-dérive)
│   ├── test_diagram_syntax.py           # Anti-régression syntaxique schémas (Mermaid, PlantUML, Draw.io)
│   ├── test_data_anonymization.py       # Privacy Guard (0 IP privée RFC 1918, 0 secret en clair)
│   ├── test_jira_exporter.py            # Linter INVEST et conformité DoD
│   ├── test_diagram_exporter.py         # Extraction dynamique et bundle multi-formats
│   ├── test_cli_resilience.py           # Résilience CLI et arborescences imbriquées
│   ├── test_e2e_mocked_crew.py          # Exécution E2E complète mockée (0 token en < 2s)
│   └── ...                              # Tests des agents, tâches, config et adaptateurs
├── logs/                       # 📝 Traces d'exécution horodatées (ignorées par Git)
├── setup.ps1                   # ⚡ Script d'installation automatisée en 1 clic
└── requirements.txt            # 📦 Dépendances Python (CrewAI, ChromaDB, Pytest)
```

---

## 📝 Le Prompt de Génération (Prêt à l'Emploi)

> **Mode d'emploi :** Copiez-collez le bloc ci-dessous dans votre invite IA en remplaçant les variables entre crochets `[DOMAINE_METIER]`, `[OBJECTIF_GLOBAL]` et `[LIVRABLES_ATTENDUS]`.

```markdown
Vous agissez en tant que Lead Solution Architect et Software Crafter d'élite, spécialiste des architectures logicielles hexagonales et des systèmes multi-agents autonomes (Agentic Design Patterns).

Votre mission est de concevoir, d'architecturer et d'industrialiser une plateforme multi-agents complète dédiée au domaine :
👉 DOMAINE MÉTIER : [DOMAINE_METIER] (ex: Audit de conformité RGPD/DORA, Plateforme MLOps, Cadrage FinOps Cloud, Modernisation de Cœur Sinistres Multi-Cloud & Agents IA en Prod)
👉 OBJECTIF GLOBAL : [OBJECTIF_GLOBAL] (ex: Analyser des spécifications pour générer un audit complet, une matrice de risques, une architecture hexagonale découplée, un backlog Jira et enrichir le profil de carrière)
👉 LIVRABLES ATTENDUS : [LIVRABLES_ATTENDUS] (ex: Pack de 11 documents d'architecture incluant le cahier des charges source et l'arbitrage ARB, schémas C4 sous 3 formats, export Jira CSV avec linter INVEST, mise à jour CV et post LinkedIn REX)

Vous devez appliquer rigoureusement les 10 piliers d'ingénierie suivants :

### 1. La Flotte d'Agents Spécialisés (Matrice des Rôles)
Définir une brigade d'au moins 7 rôles complémentaires :
- 1 Orchestrateur / Lead Architecture Manager : Pilote le cycle de vie, répartit les rôles, arbitre les contradictions dans une tâche de convergence finale (Phase E TOGAF) et rédige la synthèse exécutive.
- 1 à 2 Workers Constructifs Macro : Experts métier produisant le fond technique avec un modèle haute vélocité (ex: Gemini Flash Lite).
- 1 Évaluateur Contradictoire (Challenger / Red Team) : Pattern "Reflection & Critique", traque les hypothèses fragiles, les SPOF, les surcoûts d'infrastructure et la sur-ingénierie (KISS/YAGNI/Golden Hammer).
- 1 Gardien de la Sécurité / Conformité (CISO) : Audite les classifications de données, le chiffrement CMK, les barrières anti-prompt injection (Guardrails) et le Zero-Trust (NIST SP 800-207).
- 1 Software Crafter & Domain Architect : Modélise l'Architecture Hexagonale (Ports & Adapters), élimine la Primitive Obsession et garantit la testabilité unitaire (TDD 100%).
- 1 Traducteur Delivery Agile (SAFe Enabler) : Convertit la cible en Enabler Epics, Features, User Stories techniques Jira et Definition of Done (DoD) sur 5 piliers.
- 1 Expert Économique / FinOps : Chiffre le TCO comparatif des trajectoires, le ROI sur 3 ans et le calendrier de bascule financièrement optimisé.
- 1 Meta-Agent (Agent Zero - Hors-bande) : Analyse les logs d'erreurs dans `logs/`, surveille la santé des prompts et propose des patchs de code.
- 1 Agent Carrière & Personal Branding : Met à jour dynamiquement le profil de compétences du CV et génère des brouillons percutants de posts LinkedIn (REX).

### 2. Séparation Cognitif vs Déterministe (Règle d'Or 0 Token)
- Interdiction stricte de créer des agents LLM pour des actions binaires ou d'infrastructure (ex: Git, commandes système, manipulations de fichiers, exports).
- Créer des adaptateurs déterministes en Python pur sous `src/tools/` :
  * `GitPublisher` : Scan anti-secrets regex (AWS, Gemini, GitHub, clés privées RSA), formatage Conventional Commits et push Git uniquement après accord formel HITL.
  * `JiraBacklogExporter` : Parsing Markdown des User Stories avec linter de qualité INVEST (< 8 pts) et export CSV délimité par point-virgule (;) et encodage UTF-8-sig pour Excel Français.
  * `DiagramExporter` : Générateur et extracteur dynamique des trois formats de schémas indispensables sans `!include` distant.
  * `LogAnalyzer` : Parseur de traces horodatées extrayant les taux d'erreurs, latences et alertes SRE.
  * `CareerExporter` : Formateur de points d'impact pour CV et posts LinkedIn REX.

### 3. Résilience d'Inférence & Circuit Breaker Multi-Modèles
- Configurer un mécanisme de Circuit Breaker transparent dans la configuration (`src/config/settings.py`) :
  * Sélectionner en priorité un modèle haute vélocité et haute disponibilité (ex: `gemini-3.5-flash-lite`).
  * En cas d'erreur de saturation 503 (*High demand*) ou 429 (*Rate limit*), intercepter l'erreur et basculer automatiquement sur un modèle de secours disponible sans interrompre l'exécution.

### 4. Distillation de Contexte & Anti-"Lost in the Middle"
- Éviter l'accumulation aveugle de contexte brut (> 400 000 caractères) entre tâches séquentielles.
- Chaque tâche transmet un condensé structuré (décisions structurantes et contraintes) et n'injecte en contexte que les tâches amont directement pertinentes.

### 5. Consensus Gate & Convergence ARB (Phase E TOGAF)
- Implémenter systématiquement une tâche finale de réconciliation pilotée par le Lead Architecture Manager (`create_convergence_reconciliation_task`).
- Arbitrer souverainement toutes les divergences entre Solution Architect, Challenger et FinOps (ex: Multi-Cloud vs Mono-Cloud).
- Produire le livrable de décision `00_DECISION_ARBITRAGE_ET_SYNTHESE_CONVERGENCE.md` garantissant un dossier cible sans contradiction interne.

### 6. Archivage Systématique du Cahier des Charges dans l'Étude
- Dès l'initialisation du paramètre `--study-dir`, le système doit automatiquement copier l'expression de besoin / input de cadrage dans le dossier d'étude sous le nom :
  📁 `docs/etudes/<nom_etude>/00_CAHIER_DES_CHARGES_INPUT.md`
- Ce fichier est commité dans Git aux côtés des livrables pour garantir une traçabilité d'audit absolue entre le besoin initial et les résultats produits.

### 7. Amélioration Continue & Pistes d'Optimisation Post-Étude
- À l'issue de chaque exécution de la brigade, vous devez impérativement adopter une posture critique de Software Crafter & Principal Architect :
  * Analyser le déroulement des échanges et des débats entre agents.
  * Proposer proactivement à l'utilisateur entre 3 et 5 pistes concrètes d'amélioration (architecturales, outillage, prompts, résilience).

### 8. Gouvernance Human-in-the-Loop (HITL) Souveraine
- **Validation Souveraine des Publications :** Le système ne doit jamais persister ou pousser de données sans une porte d'arrêt bloquante `[O/N]` dans le terminal pour validation par l'architecte humain.
- **Boucle d'Arbitrage des Propositions d'Évolution (ADR / RFC) :**
  * Aucun agent n'est autorisé à modifier unilatéralement le dossier d'architecture cible (**TO-BE**).
  * Toute proposition d'évolution émise par un agent est soumise à confirmation explicite `[O/N]` de l'architecte humain dans la console.

### 9. Pyramide de Tests Craftsmanship & Fitness Functions (48 Tests Déterministes)
Mettre en place une suite de tests automatisée découpée en 4 couches exécutées en $< 40\text{ s}$ à **0 token** :
- **Couche Architecture Hexagonale (AST) :** Analyser l'arbre syntaxique du code Python pour prouver mathématiquement que les outils déterministes n'importent aucun framework d'IA ou composant d'orchestration.
- **Couche Architectural Fitness Functions (Anti-Dérive) :** Vérifier par introspection que 100% des agents et tâches documentés existent dans le code et sont exportés dans `__all__`.
- **Couche Anti-Régression Visuelle :**
  * Interdire la syntaxe illégale `..>` dans les fichiers Mermaid (`flowchart`) et imposer `-.->`.
  * Interdire les `!include` distants dans PlantUML (garantie Air-Gap réseau déconnecté) et imposer police 16 / texte noir `#000000`.
  * Valider que 100% des fichiers Draw.io sont des XML `<mxfile>` valides par parseur Python standard.
- **Couche Privacy Guard :** Scanner l'intégralité des dossiers pour certifier l'absence absolue d'adresses IP privées d'entreprise (**RFC 1918 : 10.x, 172.16-31.x, 192.168.x**) et de clés d'API.
- **Couche Linter Agile INVEST :** Vérifier que les User Stories exportées ne dépassent pas 8 points et intègrent les critères d'acceptation et la DoD.
- **Couche E2E Mockée :** Exécuter un `crew.kickoff()` complet avec Mock LLM déterministe pour tester la transmission de contexte de bout en bout en $< 2\text{ s}$.

### 10. Le Pack Documentaire Complet par Étude (11 Artéfacts)
Chaque étude d'architecture doit générer un dossier structuré dans `docs/etudes/<nom_etude>/` comprenant :
1. `00_CAHIER_DES_CHARGES_INPUT.md` : Expression de besoin et contraintes initiales archivées.
2. `00_DECISION_ARBITRAGE_ET_SYNTHESE_CONVERGENCE.md` (Manager) : Décision arbitrée de l'ARB réconciliant le DAT final.
3. `01_DOSSIER_ARCHITECTURE_TECHNIQUE_DAT.md` (Solution Architect) : Justification des choix structurants, dimensionnement et résilience.
4. `02_RAPPORT_AUDIT_CONTRADICTOIRE.md` (Challenger Red Team) : Analyse critique des risques, SPOF et traque de la sur-ingénierie.
5. `03_AVIS_HOMOLOGATION_SECURITE_DCA.md` (CISO) : Classification des données, étanchéité Zero-Trust, chiffrement CMK et avis formel DCA.
6. `04_CONCEPTION_HEXAGONALE_ET_DDD.md` (Software Crafter) : Découplage Ports & Adapters, agrégats DDD, matrice de testabilité TDD 100%.
7. `05_STRATEGIE_MIGRATION_ET_FINOPS_TCO.md` (FinOps) : Comparatif exhaustif des trajectoires, TCO Min/Max sur 3 ans, matrice Pour/Contre et ROI.
8. `06_BACKLOG_LIVRAISON_SAFE_JIRA.md` (SAFe Enabler) : Découpage vertical en Enabler Epics, Features, User Stories Jira et DoD sur 5 piliers.
9. `08_RAPPORT_OBSERVABILITE_ET_SANTE_SYSTEME.md` (Meta-Agent SRE) : Bilan de santé des traces et surveillance des dérives.
10. `09_VALORISATION_CARRIERE_ET_POST_LINKEDIN_REX.md` (Agent Carrière) : Points d'impact CV et brouillon de post LinkedIn REX prêt à l'emploi.
11. `backlog_jira.csv` : Export CSV délimité par point-virgule (;) et encodé en UTF-8-sig avec colonnes INVEST et DoD pour Excel Français.
```

---

## ⏱️ Tableau Comparatif des Gains de Temps Réactualisé

| Phase d'Ingénierie & d'Industrialisation | Temps Estimé (Humain seul) | Temps d'Exécution (Agent IA) | Temps Économisé (Time Saved) | Gain Relatif |
| :--- | :---: | :---: | :---: | :---: |
| **1. Cadrage conceptuel & Matrice des Rôles (9 Agents)** | 4h 00 min | 5 min | **+ 3h 55 min** | **97.9%** |
| **2. Architecture Logicielle Hexagonale & Socle Modulaire** | 4h 30 min | 6 min | **+ 4h 24 min** | **97.8%** |
| **3. Module RAG Local & Base Doctrinale (ChromaDB)** | 3h 30 min | 5 min | **+ 3h 25 min** | **97.6%** |
| **4. Adaptateurs Déterministes & Générateurs Multi-Formats** | 4h 30 min | 6 min | **+ 4h 24 min** | **97.8%** |
| **5. Méta-Gouvernance, Self-Healing & Branding (Brique 5)** | 3h 00 min | 4 min | **+ 2h 56 min** | **97.8%** |
| **6. Les 5 Pistes Industrielles Avancées (Circuit Breaker, ARB, Linter)** | 4h 00 min | 5 min | **+ 3h 55 min** | **97.9%** |
| **7. Pyramide Complète des 48 Tests Craftsmanship (0 token)** | 6h 30 min | 7 min | **+ 6h 23 min** | **98.2%** |
| **8. Pipeline d'Intégration Continue (CI/CD GitHub Actions)** | 2h 00 min | 3 min | **+ 1h 57 min** | **97.5%** |
| **9. Production du Pack d'Architecture d'Élite (11 Livrables)** | 6h 00 min | 6 min | **+ 5h 54 min** | **98.3%** |
| **TOTAL GÉNÉRAL** | **38h 00 min** | **~ 47 min** | **+ 37h 13 min** | **~ 97.9%** |
