# DOCTRINE D'ENTREPRISE : CONTRÔLE DE NON-DÉRIVE ET APTITUDE ARCHITECTURALE

**Référence :** DOC-ARCH-CONFORMANCE-005  
**Référentiel :** Building Evolutionary Architectures (Neal Ford) & TOGAF Phase G (Gouvernance d'Implémentation)  
**Objectif :** Garantir que le code livré reste rigoureusement conforme à l'architecture cible (TO-BE) et éradiquer la dérive documentaire  

---

## 1. Le Principe Fondamental : Zéro Écart Invisible
Dans toute démarche d'architecture d'entreprise, il est formellement interdit de concevoir une architecture cible où des composants sont décrits dans le texte mais omis dans la livraison ou dans le backlog des développeurs.

Chaque brigade d'architecture multi-agents doit impérativement appliquer **trois mécanismes de contrôle** :

---

## 2. Les 3 Garde-Fous de Non-Dérive

### 1. La Matrice de Traçabilité des Exigences (RTM - Requirements Traceability Matrix)
* Dans chaque livrable de delivery agile (SAFe / Jira), le **SAFe Agile Enabler** doit produire une matrice croisée :
  $$\text{Composant TO-BE} \iff \text{Enabler Feature} \iff \text{User Story Jira} \iff \text{Critère d'Acceptation}$$
* Aucun composant du DAT ne doit rester sans ticket de réalisation associé.
* Les briques différées doivent être explicitement étiquetées en statut : `⚪ Prévu au Jalon X` (aucune omission silencieuse).

### 2. Les Fonctions d'Aptitude Architecturale (Architectural Fitness Functions)
* Dans le guide de conception logicielle, le **Software Crafter** doit obligatoirement spécifier des tests de conformité automatisés (ex: *NetArchTest*, *ArchUnit*, assertions de métadonnées) exécutés dans la CI/CD pour vérifier que :
  - Le découpage en paquetages respecte les frontières d'Architecture Hexagonale.
  - Aucun couplage interdit n'est introduit dans le cœur de domaine.
  - La parité des calculs entre l'ancien système et le nouveau est validée à $0.000\%$ de variance.

### 3. La Vérification Contradictoire de Non-Omission (Challenger Red Team)
* L'agent **Challenger / Red Team** a pour mission de comparer la note de cadrage d'entrée, les schémas d'architecture et le backlog de sortie :
  - Traquer les composants « fantômes » (présents dans les schémas mais absents du backlog, ou promis dans la vision mais non chiffrés dans le FinOps).
  - Alerter immédiatement sur toute divergence entre la théorie documentaire et les capacités opérationnelles réelles.
