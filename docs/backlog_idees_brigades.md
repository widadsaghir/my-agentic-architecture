# 💡 Backlog & Incubateur des Brigades Multi-Agents Métier

**Projet parent :** Multi-Agent Architecture Platform (AAP)  
**Emplacement :** `my-agentic-architecture/docs/backlog_idees_brigades.md`  
**Gouvernance :** Règle du flux tendu (WIP = 1 — Une seule brigade en développement actif à la fois)  
**Date d'initialisation :** 12 octobre 2026  

---

## 🎯 Objectif du Document

Ce backlog centralise, qualifie et hiérarchise les idées de brigades multi-agents autonomes. Il permet de décharger l'esprit des nouvelles idées dès leur apparition, tout en évitant l'éparpillement grâce à une grille d'évaluation objective (complexité, dépendances externes, risques et effet de levier).

Toute idée est ensuite industrialisée selon la méthode formalisée dans le prompt réutilisable :
`assistant_archi/prompts_reutilisables/Prompt_Reusable_Conception_Brigade_MultiAgents_Metier.md`.

---

## 📊 Matrice d'Arbitrage & Priorisation

| Rang | Idée de Brigade | Complexité Technique | Dépendances Externes | Risque Opérationnel | Effet de Levier | Statut |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **#1** | **Second Brain & Gestion de Notes (Perso / Pro)** | Faible à Modérée | Fichiers locaux (Markdown, TXT, OneNote) | Nul | Immédiat (Méta-outil) | **🟢 Prioritaire (WIP = 1)** |
| **#2** | **Patrimoine Immobilier & Investissement Locatif** | Modérée à Élevée | APIs DVF, scraping annonces, fiscalité | Faible | Élevé (Patrimoine) | **🟡 En maturation** |
| **#3** | **E-commerce Sourcing Chine ➔ Amazon FBA** | Très Élevée | APIs Amazon SP-API, 1688, fret, douanes | Élevé (Trésorerie & comptes) | Potentiel financier | **⚪ En réserve** |

---

## 📝 Fiches d'Identité Détaillées des Idées

### 1. Brigade Second Brain & Gestion de Notes Métier (Perso / Pro)

- **Vision :** Transformer un flux de notes brutes hétérogènes (réunions, idées, articles, comptes-rendus, bribes de réflexions) en une base de connaissances vivante, structurée et connectée.
- **Problématique résolue :** Perte d'informations, notes oubliées, difficulté à distinguer les contextes personnel et professionnel, manque de synthèses actionnables.
- **Composition cible de la brigade :**
  - *Ingestor & Triage Agent :* Analyse la note brute, détecte la langue, le ton et affecte le contexte (Pro / Perso / Projet).
  - *Synthesizer & Summarizer :* Extrait l'essence, les décisions clés et les points d'action (Action Items).
  - *Taxonomist & Linker :* Génère les tags pertinents, crée des métadonnées frontmatter YAML et lie la note aux notes parentes ou projets existants.
  - *Challenger / Critic :* Détecte les ambiguïtés, les contradictions avec des notes antérieures ou les actions sans date/propriétaire.
  - *Action Translator :* Transforme les décisions en tâches prêtes à être exécutées (format Todo, Kanban ou calendrier).
- **Outils Déterministes purs (sans IA) :**
  - Lecteur/parseur de fichiers texte, markdown ou exports d'applications.
  - Classeur de fichiers dans l'arborescence cible (`Perso/`, `Pro/`, `Archives/`, `Projets/`).
  - Générateur d'index Markdown automatisé.
- **Livrables attendus :**
  - Arborescence de notes unifiée et enrichie de métadonnées YAML.
  - Fiches de synthèse périodiques (digest hebdomadaire).
- **Prochaine action :** Cadrer les formats de notes d'entrée et modéliser le workflow.

---

### 2. Brigade Gestion de Patrimoine Immobilier & Investissement Locatif

- **Vision :** Assister l'investisseur immobilier de bout en bout : détection d'opportunités, analyse financière rigoureuse (cash-flow, rentabilité nette, fiscalité LMNP/SCI/IR) et recommandations stratégiques d'arbitrage.
- **Problématique résolue :** Charge mentale du tri d'annonces, biais émotionnels, complexité des calculs fiscaux et estimation du risque locatif.
- **Composition cible de la brigade :**
  - *Market Watcher / Scraper :* Surveille les flux d'annonces sur des critères définis (surface, localisation, prix au m²).
  - *Data Verifier (DVF & Notaires) :* Compare le prix affiché avec l'historique réel des ventes du secteur (données ouvertes DVF).
  - *Financial & Tax Modeler :* Calcule la rentabilité brute, nette, le cash-flow mensuel et simule les régimes fiscaux (Micro-BIC, LMNP réel, SCI à l'IS/IR).
  - *Risk & Urbanism Auditor :* Évalue les risques (DPE, copropriété, travaux prévisibles, tension locative, encadrement des loyers).
  - *Investment Advisor (Orchestrateur) :* Rédige la note de synthèse d'investissement finale avec un score de recommandation go / no-go argumenté.
- **Outils Déterministes purs :**
  - Moteur de calcul financier déterministe en Python (calculs de mensualités d'emprunt, amortissements, impôts).
  - Exportateur PDF / Markdown du dossier d'investissement.
- **Livrables attendus :**
  - Dossier d'analyse d'investissement prêt pour la banque.
  - Tableau de bord de suivi du parc locatif existant (quittances, charges, fiscalité annuelle).

---

### 3. Brigade E-commerce 100% en Ligne (Sourcing Chine ➔ Vente Amazon FBA)

- **Vision :** Orchestrer une chaîne d'e-commerce automatisée : étude de marché de niches rentables sur Amazon, sourcing de fournisseurs fiables en Chine (Alibaba / 1688), optimisation de fiches produits et suivi de rentabilité.
- **Problématique résolue :** Risque financier sur des produits non rentables, temps de négociation fournisseur, complexité des contraintes logistiques et de conformité douanière/Amazon.
- **Composition cible de la brigade :**
  - *Trend & Keyword Hunter :* Analyse la demande, les volumes de recherche et la concurrence (BSR, reviews, marges estimées).
  - *Supplier Sourcing Agent :* Identifie les fabricants qualifiés, compare les prix unitaires, les MOQ (quantités minimales) et les certifications usines.
  - *Compliance & Logistics Auditor :* Vérifie les normes douanières, le marquage CE, les coûts de transport (fret maritime/aérien) et les frais Amazon FBA.
  - *Listing Copywriter & SEO Specialist :* Rédige le titre, les bullet points, la description A+ optimisés pour l'algorithme A9 d'Amazon.
  - *Margin & Pricing Controller :* Simule le seuil de rentabilité unitaire intégrant les retours, la publicité (PPC) et le stockage.
- **Outils Déterministes purs :**
  - Calculateur de marge unitaire intégrant la grille tarifaire FBA et les droits de douane.
  - Outil de vérification des certificats et formats de fichiers.
- **Livrables attendus :**
  - Fiches de validation de produit (Product Scorecard).
  - Modèles de fiches produits prêtes au déploiement.

---

## 🧭 Règle de Fonctionnement du Backlog

1. **Capture immédiate :** Dès qu'une nouvelle idée émerge, elle est consignée ici avec ses 5 paramètres (problème, brigade, dépendances, risques, valeur).
2. **Priorité stricte au WIP = 1 :** Aucune nouvelle brigade n'est codée tant que la brigade active n'a pas atteint son statut *Brique P0/P1 validée en TDD*.
3. **Mise à jour périodique :** Après chaque milestone, on réévalue l'opportunité de passer l'idée suivante en phase de cadrage.
