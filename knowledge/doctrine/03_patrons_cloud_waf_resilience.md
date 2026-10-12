# DOCTRINE CLOUD ARCHITECTURE : WELL-ARCHITECTED & PATRONS DE RÉSILIENCE

**Référence :** DOC-CLOUD-WAF-003  
**Frameworks :** Azure / AWS Well-Architected Framework, Reactive Architecture  
**Piliers :** Fiabilité, Efficacité des Performances, Optimisation des Coûts (FinOps)  

---

## 1. Patrons de Résilience pour Architectures Distribuées
1. **Circuit Breaker (Coupe-Circuit) :**  
   Interdire les appels en boucle vers un service tiers ou une base de données en défaillance. Bascule en état ouvert après $N$ échecs consécutifs, avec politique de dégradation douce (*Graceful Degradation*).
2. **Transactional Outbox Pattern :**  
   Pour découpler une base de données locale et un broker de messages (Kafka, Event Hubs). Les événements sont persistés dans la même transaction SQL que la mise à jour métier avant d'être publiés de façon asynchrone garantie (*At-Least-Once*).
3. **Strangler Fig (Étranglement Progressif) :**  
   Décommissionnement maîtrisé d'un système monolithique hérité (*Legacy*) par dérivation progressive des flux d'appels via une passerelle d'API vers les nouveaux services modernes.

---

## 2. Principes Décisionnels & BI Moderne (SSAS ➔ Fabric / Lakehouse)
* **Direct Lake vs VertiPaq Import :**
  - Le mode *Direct Lake* est réservé aux tables de faits volumineuses sans expressions DAX exotiques.
  - Pour les clôtures comptables strictes ou les calculs financiers complexes, privilégier le **mode Import VertiPaq avec rafraîchissement incrémental partitionné** pour garantir un déterminisme total de temps de réponse $< 3\text{ secondes}$ sans risque de bascule silencieuse vers DirectQuery.
* **Architecture as Code Sémantique (TMDL) :**  
  Tous les modèles décisionnels doivent être sérialisés sous forme de fichiers texte modulaires **TMDL (Tabular Model Definition Language)**, stockés dans Git et validés par le *Best Practice Analyzer* (BPA).
