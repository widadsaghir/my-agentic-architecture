# DOCTRINE DELIVERY AGILE : SAFe 6 FOR ARCHITECTS & DEFINITION OF DONE

**Référence :** DOC-SAFE-DELIV-004  
**Référentiel :** Scaled Agile Framework (SAFe 6) for Architects  
**Objectif :** Transformer les choix d'architecture technique en éléments de backlog d'ingénierie exécutables  

---

## 1. Typologie des Enablers SAFe
Les architectures ne se livrent pas sous forme de documents figés, mais sous forme d'**Enablers** embarqués dans le backlog des trains (Agile Release Trains - ART) :
1. **Enabler Epics :** Initiatives d'architecture stratégiques transverses (ex : migration Cloud d'un socle décisionnel).
2. **Enabler Features :** Incréments d'infrastructure ou de sécurité délivrant une capacité technique autonome au sein d'un Program Increment (PI). Priorisées par la méthode **WSJF** (*Weighted Shortest Job First*).
3. **Enabler Stories :** User Stories techniques confiées aux développeurs lors des sprints de 2 semaines, formalisées au format *« En tant que... Je souhaite... Afin de... »* avec critères d'acceptation opérationnels.

---

## 2. La Definition of Done (DoD) Standardisée sur 5 Piliers
Toute User Story technique d'architecture doit satisfaire les 5 piliers de la DoD avant clôture :
1. **Pilier 1 (Craft & Hexagone) :** Cœur de domaine découplé des frameworks tiers ; modèles déclaratifs versionnés dans Git.
2. **Pilier 2 (Testabilité TDD) :** Suite de tests unitaires purs $< 3\text{ s}$ à 0 token ; 0 warning critique au linter.
3. **Pilier 3 (Sécurité C2) :** Validation 0 IP publique ; clés CMK HSM effectives ; scan de secrets statiques propre (Gitleaks).
4. **Pilier 4 (Parité & Précision) :** Variance de calcul financier égale à 0.000% par rapport à l'existant.
5. **Pilier 5 (Observabilité & SIEM) :** Logs d'audit streamés en continu vers le SIEM avec rétention WORM de 365 jours.
