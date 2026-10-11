# Stratégie d'Ingénierie Logicielle : Software Craftsmanship & SAFe 6

**Projet :** Multi-Agent Architecture Platform (AAP)  
**Rôle :** Lead Enterprise & Solution Architect (Software Crafter)  
**Piliers :** Architecture Hexagonale, Clean Code, Test-Driven Development (TDD), Built-in Quality (SAFe 6)  
**Statut :** Référence méthodologique et technique obligatoire  
**Version :** 1.0 — Octobre 2026  

---

## 1. Vision & Philosophie : Faire du Projet une Pièce d'Artisanat

Pour qu'un système d'agents autonomes soit viable et maintenable en entreprise, il ne doit pas être un assemblage de scripts jetables. Ce projet applique à la lettre le **Manifeste pour le Software Craftsmanship** et la rigueur de **SAFe 6** :

1. **Pas seulement du code qui fonctionne, mais du code bien conçu (*Well-Crafted Software*) :**  
   Lisible, modulaire, exempt de duplication, appliquant les principes SOLID, KISS (*Keep It Simple, Stupid*) et YAGNI (*You Aren't Gonna Need It*).
2. **Pas seulement réagir au changement, mais ajouter constamment de la valeur (*Steadily Adding Value*) :**  
   Chaque brique est conçue comme un **Enabler SAFe** consolidant notre piste d'atterrissage architecturale (*Architectural Runway*).
3. **Built-in Quality (SAFe 6) :**  
   La qualité n'est pas vérifiée à la fin par hasard. Elle est injectée dès la conception grâce au *Shift-Left Testing* (tests automatisés dès les premières lignes de code).

---

## 2. Architecture Logicielle : L'Architecture Hexagonale (Ports & Adapters)

Pour éviter que notre logique métier d'architecture ne soit prisonnière d'une bibliothèque tierce (CrewAI, LangChain ou Google GenAI), le code est organisé selon les principes de l'**Architecture Hexagonale d'Alistair Cockburn**.

```
                          ┌─────────────────────────────────────┐
                          │   ENTRÉES (Inbound Adapters)        │
                          │   • CLI Runner (src/main.py)        │
                          │   • Futur Webhook Jira / GitLab     │
                          └──────────────────┬──────────────────┘
                                             │
                       ┌─────────────────────▼─────────────────────┐
                       │           COEUR DE DOMAINE (Pur)          │
                       │   • Définition des Rôles & Personas       │
                       │   • Règles TOGAF, WAF, Zero-Trust, C2     │
                       │   • Stratégie de cadrage linguistique     │
                       │   • Aucune dépendance externe dure !      │
                       └─────────────────────┬─────────────────────┘
                                             │
      ┌──────────────────────────────────────┼──────────────────────────────────────┐
      │ (Port LLM)                           │ (Port RAG)                           │ (Port Exporter)
┌─────▼────────────────┐              ┌──────▼───────────────┐              ┌───────▼──────────────┐
│ ADAPTER LLM          │              │ ADAPTER VECTOR STORE │              │ ADAPTER LIVRABLES    │
│ • Google Gemini      │              │ • ChromaDB local     │              │ • FileSystem Writer  │
│ • Mock LLM (Tests)   │              │ • In-Memory (Tests)  │              │ • PlantUML / Draw.io │
│ • Futur Ollama/Local │              │                      │              │ • Marp Decks         │
└──────────────────────┘              └──────────────────────┘              └──────────────────────┘
```

### Les 3 Règles d'Or de notre Hexagone :
1. **La Règle de Dépendance :** Le domaine métier (règles d'architecture, personas, logique de cadrage) ne dépend de rien. Ce sont les détails techniques (Gemini, CrewAI, ChromaDB, système de fichiers) qui dépendent du domaine via des interfaces (*Inversion de Dépendance - DIP*).
2. **Agnosticisme du Fournisseur d'IA :** Le cœur manipule une interface `LLMProviderPort`. Si nous voulons basculer demain sur un modèle Open-Source on-premise (Mistral/Llama pour données C2), nous écrivons un nouvel adaptateur sans toucher à un seul agent.
3. **Testabilité Déconnectée :** Grâce aux Ports, nous pouvons tester l'intégralité du système sans connexion internet ni clé d'API, en branchant un `MockLLMAdapter`.

---

## 3. La Pyramide de Tests du Crafter pour les Systèmes Multi-Agents

Tester un système d'agents est réputé complexe en raison du non-déterminisme des LLM. Pour garantir une fiabilité absolue à coût zéro en tokens, nous appliquons une **pyramide de tests en 3 niveaux** :

```
                        / \
                       /   \
                      / E2E \       <-- Niveau 3 : Smoke Test réel (API Gemini réelle)
                     / Évals \          (Validation de conformité TOGAF & langue)
                    /─────────\
                   /           \
                  / Intégration \   <-- Niveau 2 : Tests avec Mock LLM & Fichiers
                 /   Adapters    \      (Vérifie que les chaînes CrewAI tournent sans erreur)
                /─────────────────\
               /                   \
              /  Tests Unitaires    \ <-- Niveau 1 : Déterministes, ultra-rapides (< 1 sec)
             /   Domain & Config     \   (Vérifie .env, injection de langue, personas)
            /─────────────────────────\
```

### Niveau 1 : Tests Unitaires Purs (Déterministes, 0 token, < 1 seconde)
* **Objectif :** Tester la logique pure sans réseau, sans GPU et sans LLM.
* **Périmètre :**
  * `test_config.py` : validation des variables d'environnement, comportement en cas de clé manquante ou de proxy absent.
  * `test_tasks.py` : vérification que le paramètre `--language` injecte rigoureusement la langue demandée dans les prompts.
  * `test_agents_domain.py` : vérification que les personas embarquent les bons mots-clés de conformité (Zero-Trust, classification C2, absence d'inventions).

### Niveau 2 : Tests d'Intégration & Adaptateurs (Avec Mock LLM)
* **Objectif :** Vérifier que la plomberie CrewAI et le passage de relais entre agents fonctionnent parfaitement.
* **Périmètre :**
  * Simulation des réponses d'agents via un `FakeLLM` déterministe pré-enregistré.
  * Vérification de l'écriture des fichiers (`DAT.md`, `.puml`, `.drawio`) : non-vacuité, encodage UTF-8, syntaxe valide.
  * Ce niveau tourne en intégration continue (CI) à chaque commit en moins de 5 secondes.

### Niveau 3 : Tests d'Évaluation & Smoke Tests E2E (Avec vraie API)
* **Objectif :** Valider la qualité de restitution de la brigade complète en conditions réelles.
* **Périmètre :**
  * Exécution d'un cas test calibré (ex : *« Migration Cloud Far&Co »*).
  * **Assertions architecturales automatisées :**
    * Le document contient-il les 5 sections TOGAF attendues ?
    * Le texte est-il bien dans la langue demandée ?
    * **Règle absolue d'anonymisation :** Aucune adresse IP réelle (`\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b`) ne doit être présente dans les sorties.

---

## 4. Definition of Done (DoD) & Standards de Qualité SAFe 6

Dans notre cadre de travail, une fonctionnalité (Enabler technique ou brique d'agent) n'est déclarée **Terminée (Done)** que si les critères suivants sont tous validés :

| Critère | Exigence de Qualité | Vérification |
| :--- | :--- | :--- |
| **1. Modularité Clean Code** | Code découpé en responsabilités uniques (SRP), typé et sans redondance. | Revue de code / Crafter |
| **2. Couverture de Tests** | Tests unitaires (Niveau 1) écrits et passants à 100% au vert. | `pytest` |
| **3. Non-Régression** | Les fonctionnalités précédentes continuent de s'exécuter sans erreur. | `pytest` global |
| **4. Living Documentation** | Mise à jour de la feuille de route et des schémas d'architecture. | Markdown & Diagrams |
| **5. Commit Atomique** | Commit unitaire suivant la norme *Conventional Commits*. | `git log` |

---

## 5. La Discipline des Commits (Le Rythme du Crafter)

Fini les commits massifs regroupant trois jours de travail. Nous suivons le rythme cadencé du Software Craftsmanship :

```
[ Écriture du Test Unitaire ] ➔ Échec (Rouge)
               │
               ▼
[ Écriture du Code Minimal ]  ➔ Succès (Vert)
               │
               ▼
[ Refactoring & Nettoyage ]   ➔ Toujours Vert
               │
               ▼
[ Micro-Commit Atomique ]     ➔ git commit -m "feat(ciso): add CISO agent with C2 rules"
```

### Conventions de nommage des commits :
* `feat(scope): ...` : Nouvelle fonctionnalité ou nouvel agent opérationnel.
* `test(scope): ...` : Ajout ou enrichissement d'une suite de tests.
* `refactor(scope): ...` : Amélioration du design sans changer le comportement extérieur.
* `docs(scope): ...` : Évolution de la documentation ou des schémas d'architecture.
* `chore(scope): ...` : Mise à jour des dépendances, outillage ou scripts de build.
