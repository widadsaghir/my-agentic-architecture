# DOCTRINE SOFTWARE CRAFTSMANSHIP : ARCHITECTURE HEXAGONALE & TDD

**Référence :** DOC-CRAFT-HEX-002  
**Principes Directeurs :** Clean Code, Domain-Driven Design (DDD), Ports & Adapters, TDD 100%  
**Objectif :** Isoler le cœur de métier de toute dépendance technologique et garantir la testabilité pure  

---

## 1. Découplage Hexagonal (Ports & Adaptateurs)
1. **Règle de Dépendance Stricte :**  
   Les dépendances pointent toujours vers l'intérieur. Le cœur de domaine (**Domain**) ne doit importer **AUCUN** framework externe, aucun SDK Cloud (Azure, AWS, GCP), aucun ORM, et aucune bibliothèque d'infrastructure.
2. **Ports d'Entrée (Inbound / Driving Ports) :**  
   Interfaces définissant les cas d'usage métiers exécutables par des déclencheurs externes (APIs, contrôleurs CLI, consommateurs d'événements).
3. **Ports de Sortie (Outbound / Driven Ports) :**  
   Interfaces définissant les besoins du domaine pour interagir avec l'extérieur (stockage, publication d'événements, chiffrement, notification).
4. **Adaptateurs Périphériques :**  
   Composants techniques d'infrastructure implémentant les ports de sortie ou appelant les ports d'entrée.

---

## 2. Règles Domain-Driven Design (DDD) & Intégrité Financière
* **Agrégats & Invariants :** Tout changement d'état passe par une méthode de l'agrégat racine qui garantit l'intégrité (ex : équilibre Débit = Crédit dans le Grand Livre).
* **Interdiction des Types Flottants :**  
  Interdiction absolue d'utiliser des types à virgule flottante (`Float`, `Double`) pour représenter des montants monétaires. Utiliser exclusivement des types décimaux exacts (`BigDecimal` ou équivalent entier en centimes).
* **Value Objects Immuables :**  
  Représenter les concepts métiers sans identité propre (ex : `Money`, `Currency`, `TaxCode`) par des objets immuables.

---

## 3. Pyramide des Tests & Règle du TDD Déterministe
* **Tests Unitaires Purs (0 Token / < 1 ms) :**  
  90% des tests doivent s'exécuter en mémoire vive pure sans accès réseau, sans base de données et sans inférence LLM.
* **Architecture Testing (NetArchTest / ArchUnit) :**  
  Mettre en place des tests d'architecture automatisés dans la CI pour faire échouer le build si du code de domaine importe du code d'infrastructure.
