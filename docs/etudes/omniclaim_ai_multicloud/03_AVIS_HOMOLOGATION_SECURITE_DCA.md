# FICHE D'AUDIT ET D'AVIS DE CONFORMITÉ CISO
**Programme :** Modernisation du Cœur Sinistres & Déploiement d'Agents IA en Production (Plateforme OmniClaim AI)  
**Entreprise :** Groupe AssurGlobal  
**Classification des Données :** **C2 MASSIF** (Données personnelles, financières, bancaires et de santé - RGPD strict)  
**Référentiels :** NIST SP 800-207 (Zero-Trust), OWASP Top 10 for LLMs, RGPD, ISO/IEC 27001  
**Date de l'Audit :** Octobre 2026  
**Auditeur :** Chief Information Security Officer & Data Protection Architect (CISO)  

---

## 1. 🛡️ Avis Global du CISO

> **AVIS : FAVORABLE AVEC RÉSERVES MAJEURES (CONDITIONNÉ À L'HOMOLOGATION DCA ET AUX REMÉDIATIONS ARCHITECTURALES)**

### Justification de l'Avis
L'analyse croisée du Dossier d'Architecture Technique (DAT) et du Rapport d'Audit Contradictoire (Red Team) met en évidence un déséquilibre critique : **une complexité technique excessive ("Over-Engineering") couplée à une surface d'exposition inter-cloud superflue**, qui font peser un risque inacceptable sur la sécurité des données C2 Massif et sur la résilience opérationnelle. 

Toutefois, les garde-fous fondamentaux présentés (chiffrement CMK, cloisonnement réseau, masquage local des PII et interdiction de réentraînement des modèles par l'IA) vont dans le sens des exigences de conformité du Groupe AssurGlobal. L'avis est donc **favorable sous réserve de la mise en œuvre stricte des exigences de remédiation** formulées ci-dessous avant le passage en Dossier de Conformité Architecture (DCA).

---

## 2. 📊 Matrice d'Analyse de Classification des Données (C2 MASSIF)

La plateforme traite 15 millions de dossiers par an, contenant des pièces justificatives hautement sensibles (photographies de sinistres, factures nominatives, relevés d'identité bancaire - IBAN, et données de santé/cor corporelle).

| Axe d'Analyse | Exigence C2 / C2 Massif | Évaluation de l'Architecture Actuelle | Risque Identifié |
| :--- | :--- | :--- | :--- |
| **Confidentialité** | Chiffrement systématique au repos et en transit. Isolation stricte vis-à-vis des tiers. | Utilisation de clés CMK (KMS / Key Vault) et de TLS 1.3. Mais transit inter-cloud AWS/Azure complexe. | Exposition accrue lors des transferts inter-cloud; risque de fuite de métadonnées non chiffrées en transit. |
| **Intégrité** | Immutabilité des journaux d'audit et des données de stockage (Data Lake). | Stockage S3 avec règles de chiffrement et blocage public. Pattern Outbox. | Absence de garantie d'immutabilité stricte (WORM - Write Once, Read Many) sur les buckets de stockage de preuves. |
| **Disponibilité** | Continuité d'activité garantie (RPO = 0, RTO < 15 min). | Architecture Multi-AZ et réplication Aurora / Kafka. | Risque de panne en cascade lié à la complexité du pont inter-cloud et au dimensionnement Kafka inadapté (SPOF réseau). |
| **Conformité RGPD** | Minimisation des données, droit à l'oubli, masquage rigoureux des PII (Données Pers. / Santé). | Présence d'un filtre d'anonymisation local par expression régulière et modèles NER avant envoi vers l'IA. | **Critique :** Un faux négatif du filtre NER local expose l'enclave IA (même privée) à des données C2 Massif, constituant une violation RGPD. |

---

## 3. 🔒 Exigences de Sécurité Obligatoires (Hardening & Compliance)

Pour lever les réserves de l'avis CISO, les impératifs techniques suivants doivent être intégrés et audités sans délai :

1. **Chiffrement de Bout en Bout & CMK Exclusif :**
   * Interdiction absolue d'utiliser des clés gérées par le fournisseur cloud par défaut (SSE-S3 standard interdit). 
   * Utilisation obligatoire et exclusive de clés maîtresses client (**CMK**) gérées dans AWS KMS et Azure Key Vault HSM, avec rotation automatique annuelle et traçabilité CloudTrail / Azure Monitor de chaque appel de déchiffrement.
2. **Cloisonnement Réseau & Zero-Trust (NIST SP 800-207) :**
   * Suppression de tout accès public direct. Tous les flux inter-services et inter-clouds doivent transiter exclusivement par des **Private Endpoints**, des liaisons privées dédiées (AWS Direct Connect / Azure ExpressRoute) et des règles de sécurité (Security Groups / Network ACLs) en mode *deny-by-default*.
   * Isolation stricte des environnements (DEV, INT, PERF, PROD) sur des comptes cloud et des réseaux virtuels (VPC/VNet) étanches.
3. **Sécurité des LLMs & OWASP Top 10 for LLMs :**
   * Implantation obligatoire d'une double barrière de contrôle : le filtre de dé-identification locale des PII (NIR, IBAN, Noms) **ET** un système de garde-fous cognitifs (*NeMo Guardrails* / *Azure AI Content Safety*) pour contrer les injections de prompts indirectes via les PDF d'artisans.
   * Clause contractuelle et technique inviolable : **Zéro réentraînement des modèles d'IA sur les données assurés d'AssurGlobal** (garantie d'isolement des données d'inférence).
4. **Gestion Sécurisée des Secrets :**
   * Interdiction formelle de stocker des secrets en clair dans les manifests Terraform, les images Docker ou le code source.
   * Utilisation exclusive de HashiCorp Vault ou des gestionnaires natifs avec rotation automatique des secrets d'authentification tous les 30 jours maximum.

---

## 4. 🚀 Recommandations Impératives pour l'Homologation DCA

Le passage devant l'Architecture Review Board (ARB) pour l'obtention de l'homologation formelle du **Dossier de Conformité Architecture (DCA)** est subordonné à la réalisation des actions correctrices suivantes :

* **Action 1 : Simplification de l'Architecture (Alignment KISS / FinOps)**
  * *Exigence :* Compte tenu de la volumétrie réelle (~1,4 à 5 requêtes/sec en pic), la complexité liée au pattern multi-cloud hybride AWS/Azure et au streaming lourd (Kafka/MSK) est jugée disproportionnée. Le Solution Architect doit présenter une **variante d'architecture Single-Cloud souveraine** (ex: tout AWS ou tout Azure) pour éliminer le SPOF du pont inter-cloud, réduire les coûts de transfert et simplifier la chaîne de traçabilité Zero-Trust.
* **Action 2 : Audit de Robustesse du Filtre PII Local**
  * *Exigence :* Avant toute mise en production, un test d'intrusion spécifique (Pentest IA / Red Teaming sur les flux de dé-identification) doit être conduit et validé par la Sécurité des Systèmes d'Information pour certifier l'étanchéité du masquage des données C2 Massif.
* **Action 3 : Immutabilité du Data Lake (WORM)**
  * *Exigence :* Les buckets S3 / Stockages de documents de preuves de sinistres doivent activer les politiques d'objet verrouillé (*S3 Object Lock* en mode *Compliance*) pour garantir l'intégrité légale et financière des pièces justificatives sur la durée légale de conservation.
* **Action 4 : Plan de Continuité & Mode Dégradé IA**
  * *Exigence :* Formalisation et test d'un runbook documenté de bascule automatique ("Circuit Breaker") en cas de panne de l'enclave LLM, garantissant que la baisse de disponibilité de l'IA ne bloque jamais le traitement des dossiers urgents mais bascule sur la file d'attente humaine sécurisée (HITL) sans perte de données.

---
*Fin de l'Avis de Sécurité CISO — Document officiel soumis au comité d'homologation (ARB).*