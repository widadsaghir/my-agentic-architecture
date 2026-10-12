# 📋 Contexte et Journal de Bord du Projet : Multi-Agent Architecture Platform (AAP)

**Type de projet :** Projet personnel R&D — Ingénierie d'architecture augmentée  
**Gouvernance :** Projet autonome (aucun ticket Jira d'entreprise requis)  
**Méta-Cadre Référentiel :** TOGAF 10 ADM (Phases A à G), SAFe 6 for Architects, Software Craftsmanship (Hexagonale, TDD 100%, Clean Code), Cloud WAF, Zero-Trust (NIST SP 800-207)  
**Stack technique :** Python 3.13, CrewAI, Google Gemini API (`gemini-1.5-flash`, `gemini-1.5-pro`), ChromaDB Local, Pytest  
**Branche Git courante :** `feat/brique-2-pipeline-craft-safe`  

---

## 🎯 Vision & Composition Exhaustive du Système

Le système est désormais modélisé de façon rigoureusement identique entre la cible TOGAF (`docs/architecture-cible-togaf.md`), la living documentation visuelle (`docs/dossier-architecture-visuelle.md`), la feuille de route (`docs/roadmap-implementation.md`) et les diagrammes C4 / Séquence.

### 👥 La Brigade Complète des 8 Agents Spécialisés

1. **Lead Architecture Manager (Orchestrateur TOGAF 10 & SAFe 6)** :
   - Pilote le workflow, répartit les rôles et rédige la synthèse finale du DAT (`gemini-1.5-pro`).
2. **Solution & Infrastructure Architect (Worker Macro)** :
   - Macro-patterns : Cloud WAF, EDA/Kafka, Outbox, Strangler Fig, Circuit Breakers (`gemini-1.5-flash`).
3. **Challenger / Red Team (Évaluateur Contradictoire)** :
   - Pattern *Reflection & Critique*, détection des SPOF et traque de la sur-ingénierie (KISS, YAGNI, Golden Hammer).
4. **CISO & Data Protection Architect (Évaluateur Sécurité & C2)** :
   - Conformité Zero-Trust (NIST SP 800-207), classification C1/C2/C2 massif/RGPD, chiffrement CMK, avis formel DCA.
5. **Software Crafter & Domain Architect (Worker Micro)** :
   - Micro-patterns : Architecture Hexagonale (Ports & Adapters), modélisation DDD et stratégie de testabilité unitaire 100% TDD.
6. **SAFe System Architect & Agile Delivery Enabler (Worker Delivery)** :
   - Découpage vertical du DAT en Enabler Epics, Features, User Stories Jira techniques et Definition of Done (DoD).
7. **Agent Migration & FinOps / TCO (Spécialiste Économique)** :
   - Calculs TCO comparatifs (Cloud vs On-Premise), optimisation des coûts et calendrier de bascule progressive.
8. **Meta-Agent (Agent Zero - Méta-Gouvernance & Self-Healing)** :
   - Observabilité des logs, détection des dérives d'agents/hallucinations, affinage dynamique des prompts et correctifs code.
9. **Agent Carrière & Personal Branding (Valorisation Professionnelle)** :
   - Mise à jour continue du CV, génération de brouillons de posts LinkedIn (REX) et veille certifications (TOGAF, SAFe, Cloud).

### 🛠️ L'Adaptateur Déterministe : `GitPublisher` (Tooling non-IA)
- Traité comme un **outil Python déterministe** et non comme un agent LLM (anti-pattern de sur-ingénierie évité).
- Responsabilités : Scan anti-secrets (.env, clés), formatage de commits conventionnels et push Git uniquement après accord formel **Human-in-the-Loop (HITL)**.

---

## 📊 État d'Avancement par Brique

| Brique | Libellé | Statut | Détails |
| :---: | :--- | :---: | :--- |
| **1** | Socle Technique & Connecteur Gemini | 🟢 Terminé | Modularisation (`src/config`, `src/agents`, `src/tasks`, `src/main.py`), support `--language`. |
| **2** | Brigade d'Agents Spécialisés d'Architecture | 🟡 En cours | Séquence complète (Solution ➔ Challenger ➔ CISO ➔ Crafter ➔ SAFe) câblée et testée. Reste FinOps. |
| **3** | Base Vectorielle & RAG (ChromaDB) | ⚪ En attente | Indexation locale des blueprints, règles de sécurité et templates d'entreprise. |
| **4** | Génération de Livrables & Outil GitPublisher | ⚪ En attente | DAT.md, schémas C4 autonomes (.puml, .mmd, .drawio), adaptateur GitPublisher et exports Jira. |
| **5** | Meta-Agent (Self-Healing) & Branding | ⚪ En attente | Agent Zero (monitoring des logs & patch prompts) et Agent Carrière (CV & LinkedIn). |

---

## 🧪 Bilan d'Exécution des Tests Unitaires (Pytest)

*Dernière exécution : 13/13 tests validés avec succès (100% de réussite)*

- `tests/unit/test_config.py` : 🟢 (Chargement variables, détection clé manquante/placeholder).
- `tests/unit/test_ciso_agent.py` : 🟢 (Rôle, Zero-Trust, C2 massif, non-délégation).
- `tests/unit/test_crafter_safe_agents.py` : 🟢 (Hexagonale, TDD, Clean Code, Jira, DoD, ART).
- `tests/unit/test_challenger_agent.py` : 🟢 (Contradiction, anti-SPOF, KISS/YAGNI, Golden Hammer).
- `tests/unit/test_tasks.py` : 🟢 (5 tâches testées : Conception, Challenge, Audit CISO, Craft Hexagonal, Delivery SAFe).
- `tests/unit/test_pipeline_integration.py` : 🟢 (Assemblage séquentiel complet des 5 agents et 5 tâches dans CrewAI).

---

## 📍 Prochaines Actions Prioritaires
1. **Développement de l'agent 2.5 : Migration & FinOps / TCO** (`create_finops_agent` + tests unitaires).
2. **Essai d'exécution réelle de bout en bout de la CLI** sur un sujet d'architecture témoin.
3. **Passage à la Brique 3 : Base vectorielle RAG locale (ChromaDB)**.
