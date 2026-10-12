# GUIDE DE CONCEPTION LOGICIELLE : SOFTWARE CRAFTSMANSHIP
## Découplage Hexagonal, Domain-Driven Design (DDD) & Testabilité TDD — Projet NovaAnalytics

**Référence :** CRAFT-GUIDE-2026-NOVAA-001  
**Auteur :** Software Crafter & Domain Architect  
**Destinataires :** Tech Leads, Développeurs BI, Ingénieurs Data & DevOps  
**Philosophie :** Architecture Hexagonale, Clean Code, TDD Déterministe à 0 Token, KISS, YAGNI  

---

## 1. L'Architecture Hexagonale Appliquée à la BI & au Décisionnel

Le grand écueil des projets décisionnels réside dans le couplage direct entre les formules de calcul métier (DAX) et les tuyaux d'infrastructure (connecteurs SQL, Azure, Fabric).  
Nous imposons le découplage strict en **Ports & Adaptateurs** :

```
                                  [ ARCHITECTURE HEXAGONALE DECISIONNELLE ]

                      +-------------------------------------------------------------+
                      |                      CŒUR DE DOMAINE MÉTIER                 |
                      |                         (NovaAnalytics)                     |
                      |                                                             |
                      |  • Règles de calcul comptable pures (Soldes, Ratios, Débit)  |
  [ PORT D'ENTRÉE ]   |  • Agrégat : LedgerBook (Grand Livre avec intégrité)        |   [ PORT DE SORTIE ]
  (Inbound / Driver)  |  • Agrégat : BillingPeriod (Factures & Émissions)          |   (Outbound / Driven)
  ----------------->  |  • Agrégat : RecoveryCase (Créances, Risque & Dunning)       |  ------------------->
  Contrôleurs REST /  |  • Value Objects : Money (Précision décimale, pas de Float) |  Adaptateur OneLake /
  Requêtes Power BI   |  • Value Objects : Currency, AccountNumber, TaxCode         |  Delta Parquet /
                      |                                                             |  Azure Key Vault
                      +-------------------------------------------------------------+
```

### 1.1 Définition des Ports & Adaptateurs

1. **Le Cœur de Domaine (Domain Core) :**  
   - Totalement agnostique de Microsoft, du Cloud et du framework de restitution.
   - Encapsule les règles d'intégrité financière : une facture ne peut pas avoir un montant négatif sans avoir d'avoir associé ; un débit doit strictement égaler un crédit dans le Grand Livre (*Ledger*).
   - Utilisation stricte de types de haute précision (`BigDecimal` ou équivalent) : **interdiction absolue des types flottants (`Float` / `Double`)** sur les montants monétaires.

2. **Les Ports d'Entrée (Inbound Drivers) :**  
   - Interfaces exposées pour exécuter les calculs métier et consulter les modèles.
   - Exemples : `QueryFinancialModelPort`, `ExecuteConsolidationPort`.

3. **Les Ports de Sortie (Outbound Driven) :**  
   - Interfaces définissant les besoins d'extraction de données et de chiffrement.
   - Exemples : `ExtractionSourcePort`, `DataEncryptionPort`, `AuditLogPort`.
   - Les adaptateurs concrets (`DeltaLakeAdapter`, `AzureKeyVaultAdapter`) implémentent ces ports en périphérie.

---

## 2. Modélisation Domain-Driven Design (DDD)

### 2.1 Bounded Contexts Identifiés
1. **Billing Context :** Cycle de vie des factures, taxes, abonnements et échéanciers.
2. **Recovery Context :** Recouvrement, gestion des relances, contentieux et calcul du risque de défaut (avec isolation stricte des données personnelles RGPD).
3. **Statutory Ledger Context :** Comptabilité légale, plan de comptes, écritures de journal et balances de clôture.

### 2.2 Agrégats & Value Objects
* **Agrégat Racine `LedgerEntry` :**  
  Encapsule la règle de balance équilibrée ($\sum \text{Débits} = \sum \text{Crédits}$). Aucune écriture déséquilibrée ne peut être instanciée dans le système.
* **Value Object immuable `Money` :**  
  Composé d'une valeur numérique décimale exacte et d'un code devise ISO (`Currency`). Toute opération monétaire crée une nouvelle instance immuable.

---

## 3. Matrice de Testabilité TDD (0 Dépendance & 0 Token)

En Software Craftsmanship, la confiance repose sur des tests déterministes, ultra-rapides et déconnectés de toute ressource externe :

```
                  /\
                 /  \      10 Tests E2E / Performance (< 1 min)
                /----\     Validation des temps de réponse Power BI < 3s
               /      \
              /--------\   50 Tests d'Intégration & Sécurité (< 10 sec)
             /          \  Adaptateurs Delta Parquet, RLS DAX, Kill-Switch CMK
            /------------\
           /              \  300+ Tests Unitaires Purs TDD (< 1 sec - 0 Token)
          /----------------\ Invariants DDD, calculs financiers, règles de validation
```

### Directives d'Implémentation des Tests :
1. **Tests Unitaires de Domaine (TDD) :**  
   Exécutés en mémoire vive pure sans réseau, sans base de données et sans appel d'API LLM (0 token). La suite complète doit s'exécuter en moins de **3 secondes**.
2. **Tests d'Architecture (NetArchTest / ArchUnit) :**  
   Vérification automatisée interdisant tout import de bibliothèques d'infrastructure au sein du paquet `Domain`.
3. **Tests de Parité Financière :**  
   Comparaison automatisée entre les agrégats calculés sur les anciens cubes SSAS et les nouveaux modèles tabulaires : **tolérance de variance = 0.000%**.

---

## 4. Règle d'Or de Versioning TMDL (Architecture as Code)
* Interdiction formelle des modifications de modèles directement dans le portail web Power BI.
* Tout le modèle sémantique est codifié au format **TMDL (Tabular Model Definition Language)**, stocké dans Git et déployé par le pipeline CI/CD après passage obligatoire du linter *Tabular Editor Best Practice Analyzer*.
