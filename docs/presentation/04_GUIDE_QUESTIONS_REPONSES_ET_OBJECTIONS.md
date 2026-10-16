Date : Jeudi 15 octobre 2026

# Guide de Préparation aux Questions & Objections (7 Minutes Q/R)

Ce guide récapitule les questions les plus exigeantes susceptibles d'être posées par vos pairs d'architecture, accompagnées d'arguments éprouvés et percutants.

---

## 1. « Est-ce que ce type d'outil ne risque pas à terme de dévaloriser ou remplacer le rôle d'architecte ? »

### Réponse recommandée :
« C'est exactement l'inverse : cet outil redonne ses lettres de noblesse au métier d'architecte. 

Aujourd'hui, qu'est-ce qui nous dévalorise ? C'est de passer 70% de notre temps à faire de la mise en page Word, à recopier des chapitres de contexte, à redessiner les mêmes schémas sous trois logiciels et à écrire manuellement des tickets Jira. 

L'IA ne prend aucune décision souveraine. Elle n'a pas la sensibilité politique, elle ne connaît pas les subtilités relationnelles avec les équipes projets et elle ne porte aucune responsabilité juridique ou opérationnelle. La brigade joue le rôle d'un cabinet de consultants juniors et de rédacteurs ultra-rapides. Nous restons les associés seniors : nous cadrons, nous contestons les propositions de la machine, nous tranchons et nous engageons notre signature. »

---

## 2. « Comment pouvez-vous garantir qu'il n'y a pas d'hallucinations dans un dossier d'architecture de 35 pages ? »

### Réponse recommandée :
« Nous traitons ce risque à trois niveaux complémentaires :
- **Le RAG Doctrinal Local** : les agents ne puisent pas dans le vide d'Internet. Ils sont contraints par nos référentiels d'entreprise indexés dans ChromaDB (Zero-Trust, Hexagonale, WAF).
- **Le rôle Challenger / Red Team** : chaque affirmation d'un agent est passée au crible par un autre agent spécialisé dont le mandat est précisément de traquer les incohérences et la sur-ingénierie.
- **Les Outils Purs Déterministes (0 Token)** : tout ce qui touche aux formats stricts (schémas Draw.io, PlantUML, CSV Jira) n'est pas confié au hasard d'un LLM, mais à des convertisseurs en code Python pur.
- **La boucle de contrôle humain (Human-in-the-Loop)** : aucun document n'est publié sans lecture critique et validation explicite de l'architecte. »

---

## 3. « Peut-on injecter la doctrine propre à notre entreprise ou à notre groupe ? »

### Réponse recommandée :
« Absolument, et c'est tout l'intérêt de la plateforme. 

Le dossier `knowledge/doctrine/` est conçu pour accueillir nos propres standards : notre Politique de Sécurité des SI (PSSI), nos règles de zonage réseau, notre catalogue de services cloud référencés ou nos conventions d'API. 

Lors de l'indexation, le système découpe ces guides en fragments vectoriels. Dès qu'un agent doit concevoir une brique, il interroge cette base locale. Si notre doctrine interdit les adresses IP publiques sur une base de données ou impose un chiffrement CMK, le CISO et le Solution Architect l'appliquent immédiatement. »

---

## 4. « Quel est le coût financier d'une telle exécution ? »

### Réponse recommandée :
« Le coût est dérisoire par rapport au gain de temps. 

Grâce à notre découpage, nous utilisons des modèles ultra-rapides et très économiques (comme `gemini-1.5-flash`) pour les tâches intermédiaires des agents de conception, et nous réservons le modèle avancé (`gemini-1.5-pro`) uniquement pour la synthèse exécutive du Lead Architect. 

L'exécution complète d'une étude d'architecture de dix artéfacts consomme environ 150 000 tokens, ce qui représente moins de 0,15 € par étude complète. En face, le temps d'ingénierie humaine économisé se chiffre en dizaines d'heures. »

---

## 5. « Pourquoi avoir choisi CrewAI plutôt que LangChain ou une solution propriétaire ? »

### Réponse recommandée :
« Parce que CrewAI est nativement pensé pour modéliser une organisation d'équipe avec des rôles, des objectifs (`goals`), des mandats (`backstories`) et des mécanismes de délégation et de revue contradictoire. 

De plus, notre application respecte une architecture hexagonale stricte : le moteur d'agents est confiné dans une couche d'infrastructure remplaçable. Si demain nous voulons basculer sur un autre orchestrateur ou sur des modèles hébergés sur nos propres serveurs souverains, le cœur métier et la doctrine restent 100% intacts. »
