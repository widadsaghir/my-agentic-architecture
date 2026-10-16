Date : Jeudi 15 octobre 2026

# Storyboard & Scénario de la Démonstration Vidéo (8 Minutes)

**Format :** Vidéo préenregistrée d'écran (screen-recording sans webcam), commentée en direct à l'oral par l'architecte.  
**Résolution recommandée :** 1920x1080 (Full HD), terminal agrandi (police 16px ou 18px), thème sombre épuré (ex. One Dark Pro ou Dracula).  
**Cas d'usage présenté :** Modernisation et migration cloud du socle décisionnel *NovaAnalytics*.

---

## Tableau Synoptique du Découpage Vidéo

| Séquence | Minutage | Ce qui est affiché à l'écran | Action à l'écran | Message oral (Voiceover) |
| :---: | :---: | :--- | :--- | :--- |
| **1** | 00:00 - 01:15 | VS Code : `00_CAHIER_DES_CHARGES_INPUT.md` | Défilement sur le besoin de migration | Présentation du problème métier |
| **2** | 01:15 - 02:45 | Terminal plein écran (PowerShell) | Lancement de la commande et logs des agents | Déclenchement de la brigade |
| **3** | 02:45 - 04:30 | Terminal : Logs du Challenger & CISO | Zoom sur le débat contradictoire | Mise en avant de la Red Team |
| **4** | 04:30 - 05:45 | VS Code : Le DAT et la synthèse exécutive | Ouverture de `01_DAT.md` et `00_SYNTHESE.md` | Rigueur TOGAF et exhaustivité |
| **5** | 05:45 - 06:45 | Navigateur / draw.io et VS Code (.puml) | Affichage du schéma C4 AS-IS et TO-BE | Schémas multi-formats sans effort |
| **6** | 06:45 - 07:30 | Excel : Ouverture de `backlog_jira.csv` | Ouverture directe avec colonnes bien alignées | Continuité vers le delivery SAFe |
| **7** | 07:30 - 08:00 | Terminal : Validation HITL Git & Pytest | Prompt `[O/N]` de GitPublisher + 48 tests | Souveraineté humaine et robustesse |

---

## Scénario Détaillé et Script Oral Synchronisé

### Séquence 1 : L'Input de Cadrage (00:00 à 01:15)
- **À l'écran :** Éditeur de code ouvert sur le fichier `00_CAHIER_DES_CHARGES_INPUT.md`. On voit les contraintes : socle décisionnel historique, volumétrie de 4 To, bascule vers une cible Cloud managée, criticité C2, RPO 1h, RTO 4h.
- **Parole :**  
  « Nous voici sur le point de départ de toute étude : le cahier des charges d'entrée. Ici, nous traitons le cas NovaAnalytics. C'est un cas typique de nos environnements : un monolithe décisionnel historique qui doit migrer vers le Cloud, avec des contraintes sévères de résilience, une sensibilité de données de niveau C2, et une forte exigence de maîtrise budgétaire. À ce stade, dans notre quotidien habituel, nous en aurions pour dix à quinze jours de travail pour poser la première copie du DAT. »

---

### Séquence 2 : Le Lancement de la Brigade (01:15 à 02:45)
- **À l'écran :** Bascule sur le terminal. Saisie de la commande CLI :  
  `python src/main.py --study-dir docs/etudes/migration_ssas_cloud --language fr`  
  Appui sur Entrée. Le bandeau de la brigade s'affiche, les agents s'initialisent.
- **Parole :**  
  « Je lance l'orchestrateur en lui passant le répertoire de l'étude et la langue française. En coulisses, CrewAI instancie notre brigade de neuf profils. Vous voyez s'initialiser le Lead Architect, le Solution Architect, le Challenger, le CISO et le Crafter. Chacun a son contexte injecté, y compris nos règles de doctrine issues de notre base vectorielle locale ChromaDB. »

---

### Séquence 3 : Le Contradictoire en Action (02:45 à 04:30)
- **À l'écran :** Les logs d'exécution défilent (accélérés x3). Le Solution Architect propose un bus d'événements et des microservices. Immédiatement, l'agent **Challenger / Red Team** prend la main en rouge/orange dans le terminal.  
  Extrait visible dans le terminal :  
  `[CHALLENGER ALERT] Attention : La proposition introduit un broker Kafka surdimensionné pour un flux batch nocturne. Risque de sur-ingénierie et de SPOF d'infrastructure.`  
  Puis le **CISO** intervient :  
  `[CISO AUDIT] Données classées C2 : obligation d'appliquer un chiffrement au repos via des clés gérées par le client (CMK).`
- **Parole :**  
  « Regardez bien cette séquence. C'est le cœur de la valeur du système. Le Solution Architect a d'abord proposé une architecture événementielle avec un broker Kafka. Immédiatement, notre agent Challenger intervient : il alerte sur le risque de sur-ingénierie par rapport au besoin réel, qui est une synchronisation périodique. Dans la foulée, le CISO rappelle l'exigence de chiffrement CMK sur la base de notre doctrine interne. On n'a pas une IA béni-oui-oui : on a une véritable joute technique d'architecture avant la consolidation du document final. »

---

### Séquence 4 : L'Inspection du DAT et de la Synthèse (04:30 à 05:45)
- **À l'écran :** L'exécution se termine. Retour dans l'arborescence des fichiers générés. Ouverture de `00_RESUME_EXECUTIF_ET_DECISION.md` puis de `01_DOSSIER_ARCHITECTURE_TECHNIQUE_DAT.md`.
- **Parole :**  
  « L'exécution est terminée, elle a pris moins de trois minutes. Regardons les artéfacts générés. Nous disposons d'une synthèse exécutive prête pour le comité de décision, avec un tableau de score d'architecture. Et voici le DAT complet : les huit phases TOGAF sont respectées, les flux d'intégration sont formalisés, et les choix de composants sont justifiés avec leur matrice d'adhérence. »

---

### Séquence 5 : Les Schémas Multi-Formats (05:45 à 06:45)
- **À l'écran :** Ouverture du dossier `diagrams/`.  
  1. Affichage du fichier `architecture_to_be.drawio` ouvert dans l'extension Draw.io de VS Code (ou dans le navigateur sur draw.io).  
  2. Flash rapide sur le fichier `architecture_to_be.puml` et son rendu PlantUML.
- **Parole :**  
  « Côté visualisation, finie la corvée de redessiner les schémas dans trois outils différents. Notre adaptateur déterministe génère en un seul passage le XML natif Draw.io, le PlantUML et le Mermaid. Ce que vous voyez ici dans Draw.io n'est pas une simple image figée : ce sont de vraies formes vectorielles éditables que l'on peut déplacer, recolorer ou enrichir pour une présentation spécifique. »

---

### Séquence 6 : Le Backlog Jira sous Excel (06:45 à 07:30)
- **À l'écran :** Ouverture du fichier `backlog_jira.csv` dans Excel. Les colonnes s'ouvrent parfaitement grâce au délimiteur point-virgule : `Issue Type`, `Summary`, `Description`, `Priority`, `Acceptance Criteria`.
- **Parole :**  
  « La continuité avec le delivery est immédiate. L'agent SAFe a découpé la cible en Enabler Epics et User Stories techniques. Notre adaptateur a produit ce CSV formaté avec le séparateur point-virgule adapté à nos versions françaises d'Excel. En un clic d'import Jira, l'équipe agile dispose de ses critères d'acceptation et de sa Definition of Done technique. »

---

### Séquence 7 : Le Contrôle Humain et la Robustesse (07:30 à 08:00)
- **À l'écran :** Retour sur le terminal. L'outil `GitPublisher` affiche :  
  `[SECURITY SCAN] 0 secret détecté. Confirmez-vous le commit et le push sur Git ? [O/N]`  
  Saisie de `O`. Le commit passe. Puis exécution rapide de `pytest` : les 48 tests passent en 1.8 seconde.
- **Parole :**  
  « Enfin, le principe fondamental : l'humain reste aux commandes. L'outil vérifie qu'aucun secret n'a fuité et attend notre confirmation explicite avant d'enregistrer le résultat dans Git. Et pour garantir que la plateforme reste saine dans le temps, nos quarante-huit tests d'architecture automatisés s'exécutent en moins de deux secondes. »
