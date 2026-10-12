# FICHE D'AUDIT ET D'AVIS DE CONFORMITÉ SÉCURITÉ / DCA
## Homologation d'Architecture & Conformité C2 MASSIF — Projet NovaAnalytics

**Référence :** SEC-AUDIT-2026-NOVAA-001  
**Émetteur :** Chief Information Security Officer (CISO) & Data Protection Architect  
**Destinataires :** Lead Enterprise Architect, Solution Architect, Challenger Architect, DPO  
**Classification des Données :** C2 MASSIF (Données financières & bancaires hautement sensibles)  
**Statut Global :** **FAVORABLE AVEC RÉSERVES STRICTES (Bloquantes pour le passage en DCA)**  

---

## 1. Tableau de Bord d'Évaluation de Sécurité

| Domaine Audité | Statut | Commentaire SSI / Risque Détecté |
| :--- | :---: | :--- |
| **Cloisonnement Réseau & Zero-Trust (NIST SP 800-207)** | CONFORME SOUS CONDITION | Private Endpoints obligatoires sans exception. Interdiction absolue d'adresse IP publique. |
| **Classification C2 & RGPD (DCP & Contentieux)** | RÉSERVES CRITIQUES | Données de débiteurs et contentieux (RecoveryCube) sans pseudonymisation ni purge automatisée. |
| **Cryptographie (CMK / HSM)** | RÉSERVES MAJEURES | Clés CMK obligatoires sur HSM certifié FIPS 140-2 Niveau 3. Procédure Kill-Switch $< 15\text{ min}$. |
| **Traçabilité & Détection SIEM** | CONFORME SOUS CONDITION | Streaming intégral des logs d'accès vers Microsoft Sentinel avec rétention immuable WORM 365j. |

---

## 2. Les 4 Exigences Impératives pour l'Homologation DCA

Pour que le Dossier de Conformité Architecture (DCA) soit approuvé avant toute mise en production :

### Exigence 1 : Isolation Réseau Étendue & Zéro Point de Terminaison Public
* Tout le trafic entre l'On-Premise, les modèles décisionnels et Power BI doit transiter exclusivement via **Azure Private Link** et des liaisons **ExpressRoute** dédiées avec chiffrement physique MACsec.
* Les passerelles d'accès Internet public doivent être désactivées au niveau du tenant Fabric et Power BI (`publicNetworkAccess = Disabled`).

### Exigence 2 : Chiffrement CMK et Procédure de Révocation d'Urgence (*Kill-Switch*)
* Toutes les données au repos (Lakehouse OneLake, bases tabulaires en mémoire VertiPaq) doivent être chiffrées par des clés gérées par l'entreprise (**Customer-Managed Keys - CMK**).
* Hébergement validé : **Azure Key Vault Premium** avec module matériel HSM certifié FIPS 140-2 Niveau 3 (ou Managed HSM si exigé par la politique groupe).
* Mise en œuvre d'un script d'urgence de **révocation de clé (Kill-Switch)** capable de rendre les données illisibles en moins de **15 minutes** en cas de compromission avérée du tenant.

### Exigence 3 : Protection des Données Personnelles (RGPD & RecoveryCube)
* Le *RecoveryCube* traitant des données de recouvrement, créances et contentieux clients (Données à Caractère Personnel hautement sensibles) :
  - Mise en place d'une **pseudonymisation irréversible (hachage SHA-256 avec sel dynamique)** sur les identifiants clients et comptes bancaires exposés dans les modèles de reporting.
  - Sécurité au niveau des lignes (**Row-Level Security - RLS**) et des colonnes (**Column-Level Security - CLS**) dynamique, limitant l'accès des agents de recouvrement uniquement à leur portefeuille attribué.
  - Politique de rétention et purge automatisée conforme au droit à l'effacement.

### Exigence 4 : Traçabilité et Auditabilité Immuable (SOX / SIEM)
* Envoi de 100% des logs d'audit (accès aux modèles, requêtes DAX, modifications de schémas, déploiements XMLA) vers le SIEM d'entreprise (**Azure Sentinel / Log Analytics**).
* Stockage immuable (technologie **WORM - Write Once, Read Many**) avec une période de rétention verrouillée de **365 jours minimum**.

---

## 3. Décision du CISO pour le Comité d'Architecture (ARB)
L'homologation d'architecture est conditionnée à l'intégration formelle des 4 exigences ci-dessus dans la Definition of Done (DoD) de l'équipe de réalisation et à la validation des tests de pénétration (*pentest*) de la zone d'atterrissage.
