# RAPPORT D'AUDIT CONTRADICTOIRE (RED TEAM REVIEW)
## Contre-Analyse d'Architecture & Traque des SPOF — Projet NovaAnalytics

**Référence :** RED-TEAM-2026-NOVAA-001  
**Auteur :** Challenger Architect & Red Team Evaluator  
**Destinataires :** Lead Enterprise Architect, Architecture Review Board (ARB), DSI  
**Classification des Données :** C2 MASSIF  
**Verdict Global :** **RISQUE CRITIQUE | COMPLEXITÉ ÉLEVÉE (SUR-INGÉNIÉ)**  

---

## 1. Synthèse de l'Évaluation Contradictoire
La proposition d'architecture préliminaire souffre du syndrome aigu du **« Golden Hammer »** (Marteau Doré) articulé autour de l'écosystème **Microsoft Fabric / Direct Lake**, combiné à une sur-spécification d'infrastructure :
* **Pari risqué sur Direct Lake :** Risque critique de **Silent Fallback vers DirectQuery** dès que les quotas mémoire ou des règles DAX complexes sont sollicités. Ce phénomène dégrade les temps de réponse de 300 ms à plus de 45 secondes, inacceptable lors des clôtures comptables du Grand Livre (*LedgerCube*).
* **Fausse promesse Low-Ops :** L'empilement de machines virtuelles de passerelles (OPDG), de résolveurs DNS privés et de clusters matériels HSM dédiés recrée une charge d'exploitation lourde déguisée sous du SaaS.
* **Overhead organisationnel :** Planifier un train SAFe sur 4 PI pour trois cubes décisionnels relève d'une bureaucratie disproportionnée.

---

## 2. Matrice d'Identification des SPOF & Risques de Panne en Cascade

| Composant | Nature du Risque (SPOF / Défaillance) | Mécanisme de Cascade | Impact Métier |
| :--- | :--- | :--- | :--- |
| **Capacité Fabric F-SKU Unique** | **SPOF Logique & FinOps.** Mutualisation des 3 cubes sur une seule capacité sans étanchéité. | Une requête DAX lourde sur le *BillingCube* sature les Capacity Units (CU). Le throttling Fabric bloque le *LedgerCube* en pleine clôture financière. | **CRITIQUE** (Blocage des arrêtés comptables, rupture SLA). |
| **Silent Fallback Direct Lake** | **Défaillance de Résilience Silencieuse.** Dépassement des limites mémoire VertiPaq. | Bascule silencieuse vers DirectQuery. Effondrement du temps de réponse ($> 60\text{ s}$) et saturation des connexions Power BI. | **ÉLEVÉ** (Timeouts pour les 300 utilisateurs simultanés). |
| **Cluster OPDG sur VM IaaS** | **Goulot d'étranglement Stateful.** 3 VM IaaS dans Azure pour aspirer les données On-Premise. | Si le lien ExpressRoute subit une gigue ou saturation, les buffers disques saturent et les batchs échouent. | **ÉLEVÉ** (Dépassement de la fenêtre batch de 2 heures). |
| **Azure Key Vault Managed HSM** | **SPOF d'initialisation & Surcoût.** Dépendance stricte de Fabric pour le déchiffrement CMK. | Coût fixe récurrent de 2 300 $/mois. En cas de latence sur le HSM, indisponibilité totale du patrimoine analytique. | **CRITIQUE** (Déni de service complet sur la BI). |

---

## 3. Registre des Éliminations (Principes KISS / YAGNI)

1. **Remplacer le mode Direct Lake par le Mode VertiPaq Import avec Partitionnement Incrémental :**
   * Élimine tout risque de bascule DirectQuery.
   * Déterminisme absolu des performances ($< 3\text{ s}$ garanti en RAM).
   * Grâce au rafraîchissement incrémental XMLA, seules les données modifiées (J-1) sont transférées chaque nuit (temps d'ingestion $< 20\text{ minutes}$).
2. **Remplacer Azure Key Vault Managed HSM par Azure Key Vault Premium :**
   * Utilisation de clés RSA protégées par HSM au sein d'un Key Vault Premium standard.
   * Même conformité FIPS 140-2 Niveau 3 (C2 MASSIF).
   * **Économie : 95% de réduction des coûts de chiffrement** (économie de plus de 27 000 $/an).
3. **Supprimer les VM IaaS de passerelle (OPDG) dans Azure :**
   * Utiliser des Managed Private Integration Runtimes serverless via ExpressRoute.
   * Vraie architecture zéro-serveur (Zero-VM à patcher ou maintenir).
4. **Sanctuariser une capacité dédiée pour le LedgerCube :**
   * Séparer la capacité Finance (*LedgerCube*) de la capacité Opérationnelle (*BillingCube / RecoveryCube*) pour isoler les clôtures comptables.

---

## 4. Arbitrages Recommandés pour l'ARB
* **[ REJETÉ ]** Le mode *Direct Lake* comme cible unique par défaut (trop instable sur calculs financiers complexes).
* **[ REJETÉ ]** Le déploiement d'un cluster Managed HSM dédié (surcoût injustifié de 2 300 $/mois face à AKV Premium).
* **[ REJETÉ ]** Les VM IaaS pour les passerelles de données dans Azure (dette d'exploitation inutile).
* **[ VALIDÉ ]** L'isolation réseau stricte par Private Endpoints et ExpressRoute MACsec.
* **[ VALIDÉ ]** Le format déclaratif TMDL et l'outillage CI/CD (Tabular Editor CLI).
