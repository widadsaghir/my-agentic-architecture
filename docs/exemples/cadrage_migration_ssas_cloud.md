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

---

## 2. Flux et Intégrations
- **En amont (Extraction) :** Les 3 instances SSAS se synchronisent et extraient périodiquement d'importants volumes de données depuis des bases de données de production transactionnelles d'entreprise (flux batch nocturnes et synchronisations planifiées).
- **En aval (Consommation) :** Les cubes exposent leurs modèles sémantiques pour la consultation et le reporting via le service **Power BI** (tableaux de bord décisionnels pour les équipes de gestion et directions métiers).

---

## 3. Exigences de Sécurité & Conformité (Non-Négociables)
- **Classification : Niveau C2 MASSIF** (données financières et clients sensibles à fort volume).
- **Zero-Trust (NIST SP 800-207) :** Cloisonnement réseau strict, authentification forte et pas d'exposition sur l'Internet public (Private Endpoints uniquement).
- **Chiffrement de bout en bout :** Chiffrement au repos avec clés gérées par le client (**Customer Managed Keys - CMK / HSM**) et chiffrement en transit (TLS 1.3).
- **Gouvernance des données :** Respect du RGPD, traçabilité des accès et contrôle d'accès fin aux données (Row-Level Security - RLS).

---

## 4. Objectifs de l'Étude d'Architecture Cible (TO-BE)
1. **Évaluer et comparer l'ensemble des scénarios de migration Cloud possibles :**
   - *Option 1 : Réhébergement IaaS (Lift & Shift)* — Migration des VM existantes avec maintien des instances SSAS On-Premise transposées sur Cloud IaaS.
   - *Option 2 : Replatforming PaaS managé* — Migration vers Azure Analysis Services (AAS) ou service managé équivalent.
   - *Option 3 : Modernisation Cloud-Native / Lakehouse* — Migration vers Microsoft Fabric (Semantic Models Power BI Premium) ou plateforme Lakehouse unifiée (Snowflake / Databricks).
2. **Architecture Réseau & Intégration Hybride :**
   - Définir la passerelle d'intégration sécurisée entre le Cloud et les sources de données transactionnelles restant On-Premise (Data Gateway privée, ExpressRoute / VPN dédié).
3. **Automatisation & Chaîne CI/CD :**
   - Modéliser la chaîne de déploiement continu des modèles tabulaires / sémantiques (*Architecture as Code*, Tabular Editor, scripts TMDL/BIM, pipelines GitLab/Azure DevOps).
4. **Découpage Agile (SAFe) :**
   - Découper la trajectoire de bascule progressive en Enabler Epics, Enabler Features et User Stories Jira avec Definition of Done (DoD).
