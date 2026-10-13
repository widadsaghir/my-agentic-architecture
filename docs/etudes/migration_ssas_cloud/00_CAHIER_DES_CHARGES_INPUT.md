# 📋 Note de Cadrage d'Architecture Témoin

**Projet :** NovaAnalytics (Migration Décisionnelle SSAS ➔ Cloud)  
**Date :** 12 octobre 2026  
**Statut :** Cas d'usage de référence anonymisé  
**Classification des Données :** C2 MASSIF  

---

## 1. Contexte & État Existant (AS-IS)
L'application décisionnelle **NovaAnalytics** est hébergée sur une infrastructure On-Premise dédiée.  
Le socle décisionnel repose sur la technologie Microsoft SQL Server Analysis Services (SSAS) répartie sur 3 serveurs physiques/VM de production distincts, hébergeant chacun un cube OLAP dédié à un domaine financier :
- **Cube 01 : Facturation (BillingCube)** — Traitement analytique des factures et volumétries d'émissions.
- **Cube 02 : Recouvrement (RecoveryCube)** — Suivi des impayés, relances et contentieux.
- **Cube 03 : Comptabilité Générale (LedgerCube)** — Écritures comptables, grand livre et clôtures.

### Problématiques actuelles :
1. **Saturation mémoire et CPU :** Traitement batch nocturne lent (durée > 6 heures).
2. **Maintenance opérationnelle lourde :** 3 instances indépendantes à patcher et superviser manuellement.
3. **Limitation d'élasticité :** Incapacité à absorber les clôtures mensuelles sans dégradation des temps de réponse pour les utilisateurs finaux.

---

## 2. Ambition & Objectifs de la Cible (TO-BE)
1. **Modernisation Cloud :** Migration vers une solution managée PaaS/SaaS (ex: Microsoft Fabric / Azure Analysis Services / Databricks) permettant de mutualiser les modèles de données.
2. **Performance :** Réduction du temps de rafraîchissement nocturne sous la barre des 2 heures.
3. **Sécurité & Conformité :**
   - Respect impératif de la doctrine **Zero-Trust** et **C2 MASSIF**.
   - Chiffrement au repos via clés gérées par le client (**CMK** via Azure Key Vault HSM).
   - Aucun flux transitant par l'Internet public : utilisation obligatoire de **Private Endpoints**.
4. **Agilité & Livrables :**
   - Fourniture d'un découpage en User Stories Jira techniques et Definition of Done (DoD).
   - Élaboration d'une feuille de route phasée garantissant un basculement sans rupture de service pour les directions métiers.
