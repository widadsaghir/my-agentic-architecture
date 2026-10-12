# 📑 FICHE DE SYNTHÈSE EXÉCUTIVE & DÉCISIONNELLE (ONE-PAGER)
## Modernisation du Socle Décisionnel SSAS vers le Cloud — Projet NovaAnalytics

**Date :** 12 octobre 2026  
**Auteur :** Lead Enterprise & Solution Architect (Software Crafter)  
**Destinataires :** Direction Générale, DSI, Directeurs Financiers, Architecture Review Board (ARB)  
**Classification des Données :** **C2 MASSIF**  
**Décision Sollicitée :** Approbation formelle de la trajectoire cible et engagement du budget initial (Jalon 1 & 2 : 60 k€)  

---

### 1. Le Constat & La Problématique Métier
* **L'Existant (AS-IS) :** Trois cubes décisionnels Microsoft SQL Server Analysis Services (SSAS) hébergés sur 3 serveurs physiques/VM On-Premise dédiés :
  - *BillingCube* (Facturation), *RecoveryCube* (Recouvrement & créances), *LedgerCube* (Comptabilité & clôtures SOX).
* **Les Risques & Blocages :**
  - **Saturation matérielle :** Les batchs d'ingestion nocturnes dépassent 6 heures et frôlent l'ouverture des marchés.
  - **Dette technique & obsolescence :** SSAS On-Premise n'évolue plus chez l'éditeur ; limitations pour les 300 utilisateurs Power BI interactifs.
  - **Sécurité C2 MASSIF :** Exigence stricte d'étanchéité, zéro exposition Internet et conformité RGPD sur les données de débiteurs.

---

### 2. L'Arbitrage d'Architecture Cible (TO-BE)
Après audit contradictoire (Red Team) et revue CISO, **l'Option 3 (Modernisation Cloud-Native Microsoft Fabric / Modèles Sémantiques TMDL)** est retenue avec un ajustement prudent :
* **Moteur In-Memory VertiPaq en Mode Import Partitionné :** Rejet du mode Direct Lake pour la comptabilité afin d'éviter tout effondrement de performance (*silent fallback* en DirectQuery). Le temps de réponse reste **garanti $< 3\text{ secondes}$** en RAM.
* **Fenêtre batch nocturne réduite sous les 20 minutes** grâce au rafraîchissement incrémental XMLA (seules les données de la veille sont transférées).
* **Isolation Réseau Zero-Trust :** Enclave réseau VNet 100% privée (Azure Private Link), aucun endpoint public, ExpressRoute dédié avec chiffrement MACsec.
* **Sécurité C2 MASSIF :** Clés gérées par le client (**Customer-Managed Keys - CMK**) sur HSM certifié FIPS 140-2 Niveau 3 (Azure Key Vault Premium) avec procédure Kill-Switch en $< 15\text{ minutes}$. Pseudonymisation SHA-256 avec sel dynamique sur les données clients et créances (RGPD).

---

### 3. Les Chiffres Clés FinOps & Rentabilité (ROI)

```
+-----------------------------------------------------------------------------------------+
|                                    BILAN FINANCIER À 3 ANS                              |
+-----------------------------------------------------------------------------------------+
| • Budget de Réalisation (Build)       : 115 000 € (Jalons 1 à 3 étalés sur 5 mois)      |
| • Coût de Fonctionnement Run Annuel   : 70 000 € / an (Capacité réservée + OneLake)     |
| • TCO Global sur 3 ans (Cible Fabric) : 325 000 € (Contre 515 000 € pour le IaaS Lift)  |
| • Économie Nette Récurrente           : ~ 60 000 € / an (Extinction serveurs & licences)|
| • Retour sur Investissement (ROI)     : AMORTI DÈS LE 14e MOIS D'EXPLOITATION           |
+-----------------------------------------------------------------------------------------+
```

---

### 4. Calendrier de Déploiement & Prochains Jalons

| Jalon | Échéance | Objectif Opérationnel Majeur | Livrable Clé |
| :---: | :---: | :--- | :--- |
| **Jalon 1** | **Mois 1** | Fondations Landing Zone Zero-Trust & Chiffrement CMK | Homologation DCA validée par le CISO |
| **Jalon 2** | **Mois 2** | Migration Pilote Facturation (*BillingCube*) en TMDL | Batch validé $< 20\text{ min}$ & P95 $< 3\text{ s}$ |
| **Jalon 3** | **Mois 3-4** | Bascule *LedgerCube* & *RecoveryCube* avec RLS/RGPD | Double-run comptable 30j (0.000% écart) |
| **Jalon 4** | **Mois 5** | Décommissionnement & Extinction des 3 VM On-Premise | Économie effective de 60 k€/an actée |

---

### 5. Décision Soumise au Comité d'Architecture (ARB)
* ✅ **Validation formelle** de la trajectoire Modernisation Modèles Sémantiques TMDL (Option 3 ajustée).
* ✅ **Approbation de l'enveloppe initiale de 60 000 €** pour l'exécution des Jalons 1 et 2.
* ✅ **Mandat délivré à l'équipe de réalisation** pour intégrer les Enabler User Stories dans le prochain sprint.
