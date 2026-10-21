# Support de Présentation : L'Architecte Augmenté

**Public cible :** Communauté des Architectes Solution, Entreprise et Domaine  
**Format :** Présentation dynamique (15 min) + Démo vidéo (8 min) + Échanges & Q/R (7 min) = 30 min  
**Objectif :** Démontrer la valeur d'une brigade multi-agents spécialisée dans la conception, le contradictoire et la documentation d'architecture.

---

## Slide 1 : Page de Titre & Accroche

### Éléments Visuels
- Fond sombre sobre et épuré.
- Typographie moderne et contrastée.
- Schéma conceptuel en filigrane : une boussole d'architecture entourée d'un réseau de nœuds interconnectés.

### Contenu Textuel
```text
L'ARCHITECTE AUGMENTÉ
Concevoir, challenger et outiller à l'échelle

Retour d'expérience sur la plateforme Multi-Agent Architecture Platform (AAP)
```

### Note de bas de page
*Session Communauté d'Architecture — 30 minutes*

---

## Slide 2 : Le Paradoxe Quotidien de l'Architecte

### Éléments Visuels
- Deux colonnes comparatives contrastées (attentes vs réalité).
- Graphique circulaire (Camembert) montrant la répartition réelle du temps.

### Contenu Textuel
| Où va notre valeur ajoutée ? | Ce qui consomme 70% de nos journées |
| :--- | :--- |
| Arbitrages stratégiques et vision cible | Rédaction manuelle de DAT volumineux (30 à 60 pages) |
| Dialogue de cadrage avec les métiers et le Product Management | Déclinaison fastidieuse en User Stories et Enablers Jira |
| Accompagnement au sol des équipes de delivery | Remplissage de matrices de conformité et fiches SSI |
| Veille technologique et innovation | Retranscription manuelle de schémas (Visio, Draw.io, PlantUML) |

### Chiffre Clé au centre
> **70%** du temps d'un architecte est aujourd'hui absorbé par la formalisation documentaire plutôt que par l'arbitrage de conception.

---

## Slide 3 : Le Mirage du Simple Chatbot IA

### Éléments Visuels
- Schéma d'opposition visuelle entre un "Chatbot isolé" et un "Comité d'Architecture".
- Icônes d'alerte : risque d'illusion et de complaisance.

### Contenu Textuel
```text
Pourquoi un prompt unique dans ChatGPT ou Gemini ne suffit pas :

[ Chatbot Isolé ] 
  ├── Approbation systématique  ──> Valide la première idée, même sur-ingéniée
  ├── Absence de doctrine locale ──> Ignore le Zero-Trust, l'Hexagonale ou le WAF
  ├── Manque de contradictoire   ──> Ne traque ni les SPOF, ni les coûts cachés
  └── Absence d'outillage        ──> Incapable de générer du Draw.io ou du CSV Jira
```

### Constat Majeur
Un modèle de langage généraliste est un **exécutant poli**, alors qu'un architecte a besoin d'un **sparring-partner contradictoire**.

---

## Slide 4 : Le Concept de la Brigade Multi-Agents (AAP)

### Éléments Visuels
- Disposition radiale : le Lead Architect au centre, entouré des 8 rôles spécialisés.
- Code couleur distinct par fonction (Bleu : Conception, Rouge : Sécurité & Audit, Vert : Craft & Delivery, Orange : Économie).

### Contenu Textuel
```text
                       [ Lead Architecture Manager ]
                                     │
       ┌─────────────────────────────┼─────────────────────────────┐
       │                             │                             │
[ Macro & Infra ]            [ Red Team Contradictoire ]   [ SSI & Zero-Trust ]
Solution Architect           Challenger / Anti-SPOF        CISO & Data Protection
(Cloud WAF, EDA, Outbox)     (KISS, YAGNI, résilience)     (NIST 800-207, C1/C2)
       │                             │                             │
       ├─────────────────────────────┼─────────────────────────────┤
       │                             │                             │
[ Micro & Code ]             [ Delivery & Découpage ]      [ Modèle Économique ]
Software Crafter             SAFe System Architect         FinOps & Migration TCO
(Hexagonale, DDD, TDD)       (Enablers, US, DoD, CSV)      (Calcul TCO, bascule)
       │                             │                             │
       └─────────────────────────────┴─────────────────────────────┘
                                     │
                       [ Adaptateurs Purs Déterministes ]
                       (Schémas multi-formats, CSV Excel, Git HITL)
```

---

## Slide 5 : L'Ingénierie Sous le Capot : Craftsmanship & Zéro Dérive

### Éléments Visuels
- Schéma en couches de l'Architecture Hexagonale du projet.
- Badge vert : 48 tests unitaires exécutés en moins de 2 secondes.

### Contenu Textuel
- **Isolation Hexagonale stricte** : Le domaine métier d'architecture est 100% indépendant des frameworks de LLM.
- **RAG Local Doctrinal (ChromaDB)** : Injection automatique de nos règles de sécurité, de craft et de cloud sans dépendance cloud externe.
- **Outils Déterministes (0 Token)** :
  - *DiagramExporter* : Génération synchronisée en PlantUML, Mermaid et Draw.io natif XML.
  - *JiraBacklogExporter* : Génération CSV avec délimiteur point-virgule compatible direct Excel français.
  - *GitPublisher* : Détection automatique des secrets (.env, tokens) et sas de validation humaine obligatoire (Human-in-the-Loop).
- **Architectural Fitness Functions** : 48 tests par analyse d'arbre syntaxique (AST) qui vérifient qu'aucun agent ne dérive de son rôle.

---

## Slide 6 : Le Workflow Opérationnel : Du Cadrage aux Livrables

### Éléments Visuels
- Schéma pipeline en 5 étapes séquentielles : Cadrage Markdown -> Conception Macro -> CHOC CONTRADICTOIRE (Red Team & CISO) -> Craft & Delivery -> Sortie Déterministe & HITL.

### Points Clés
- Injection de la doctrine locale depuis ChromaDB.
- Étape charnière : Le Challenger traque la sur-ingénierie et le CISO audite les données sensibles (C2 & CMK).
- SAS de sécurité GitPublisher avec confirmation humaine obligatoire `[O/N]`.

---

## Slide 7 : Le Portfolio des Projets Développés sous Git

### Éléments Visuels
- Grille 2x2 présentant les 4 projets du portfolio d'ingénierie logicielle sous Git.

### Contenu Textuel
| Projet Git | Nature & Cadre | Rôle & Innovation Majeure |
| :--- | :--- | :--- |
| **NovaAnalytics (AAP)** | `my-agentic-architecture` | Étude pilote de migration décisionnelle Cloud : 10 livrables produits, Red Team refusant Kafka pour du serverless, TCO -33.4%, 12 US Jira. |
| **CareerFleet AI** | `career-fleet-ai` | Système multi-agents dédié au personal branding et à la valorisation de carrière d'architecte (Coach, Profiler, Portfolio Builder). |
| **Agentic Notes Assistant** | `agentic-notes-assistant` | Assistant de captation de réunions et d'extraction automatique des Architecture Decision Records (ADR). |
| **AI Prompts & Doctrine Library** | `ai-prompts-library` | Référentiel de doctrine as code (Clean Code, Hexagonale, Zero-Trust) alimentant la base vectorielle locale ChromaDB. |

---

## Slide 8 : Transition vers la Démonstration Vidéo

### Éléments Visuels
- Capture d'écran du terminal en action montrant les logs colorés et la collaboration entre agents.
- Minuteur affiché : 8 minutes de démonstration.

### Message Clé
```text
« Place à la démonstration : 
  Regardons comment la brigade réagit face à un cahier des charges de migration complexe. »
```
- Cas d'usage : Modernisation d'un socle décisionnel monolithique vers une architecture Cloud managée.
- Ce que vous allez voir :
  1. Le cadrage et le lancement de la commande.
  2. Le débat contradictoire entre le Solution Architect et le Challenger.
  3. L'arbitrage du CISO sur le chiffrement des données.
  4. L'inspection des livrables finaux et le contrôle humain (Human-in-the-Loop).

---

## Slide 9 : Synthèse & Débat Ouvert : L'Architecte de Demain

### Éléments Visuels
- Formule visuelle marquante : `Architecte Humain (Discernement) + Brigade IA (Formalisation) = Impact Décuplé`.


### Contenu Textuel
- **Ce que la brigade apporte :**
  - Fin du syndrome de la page blanche : un premier jet complet et argumenté en 5 minutes.
  - Audit contradictoire systématique : aucune décision n'est acceptée sans avoir été attaquée par le Red Team.
  - Continuité de chaîne : de la vision stratégique TOGAF jusqu'au ticket Jira SAFe.
- **Ce que l'architecte conserve jalousement :**
  - La souveraineté de décision : l'IA propose, l'humain arbitre.
  - La sensibilité politique, humaine et contractuelle que nulle machine ne peut appréhender.
  - La responsabilité pleine et entière des choix engagés vis-à-vis du SI.

---

## Slide 9 : Questions & Débat Ouvert

### Éléments Visuels
- Liste de 3 questions d'ouverture pour lancer la discussion avec les pairs.

### Contenu Textuel
```text
Échangeons entre pairs :

1. Dans vos projets actuels, quel est le livrable qui vous prend le plus de temps ?
2. Comment envisagez-vous l'intégration d'un rôle "Challenger / Red Team" dans vos comités ?
3. Quelles sont les briques de doctrine d'entreprise que nous devrions injecter en priorité ?
```
