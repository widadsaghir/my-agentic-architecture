# ÉTUDE STRATÉGIQUE DE MIGRATION & RAPPORT FINOPS / TCO : PLATEFORME OMNICLAIM AI
**Groupe AssurGlobal — Programme Modernisation du Cœur Sinistres & IA**  
**Classification des Données :** **C2 MASSIF**  
**Auteur :** Spécialiste Migration, FinOps & TCO (Certifié FinOps / Cloud Economist)  
**Date :** Octobre 2026  

---

## SYNTHÈSE EXÉCUTIVE FINANCIÈRE & STRATÉGIQUE

L’analyse économique et architecturale menée sur le programme *OmniClaim AI* démontre qu'un choix de trajectoire inadapté peut compromettre la rentabilité du projet. Face aux contraintes de criticité **C2 MASSIF**, à la nécessité d'absorber des multiplicateurs de charge climatique x10, et au rejet justifié de la Red Team concernant la sur-ingénierie du Scénario 3 (Multi-Cloud Hybride AWS/Azure), cette étude évalue et compare **quatre trajectoires de migration réalistes** basées sur une cible **Mono-Cloud AWS unifiée et souveraine**.

L'objectif de ce rapport est de fournir aux décideurs (Direction Générale, DSI, Comité d'Arbitrage Financier) les éléments chiffrés rigoureux permettant de sélectionner la trajectoire optimale maximisant le ROI à 3 ans, tout en maîtrisant les risques d'infrastructure (Run), d'investissement initial (Build) et de licences logicielles.

---

## 1. TABLEAU COMPARATIF DES OPTIONS DE MIGRATION (RUN, BUILD, LICENCES)

Quatre trajectoires technico-économiques ont été modélisées pour porter la nouvelle plateforme *OmniClaim AI* en remplacement du monolithe WebLogic 12c / Oracle RAC :

1. **Trajectoire A : IaaS Lift & Shift (AWS EC2 / RDS Oracle)** — Migration brute du monolithe existant avec virtualisation sur le cloud, sans refactoring.
2. **Trajectoire B : PaaS Managé (AWS ECS / Aurora PostgreSQL)** — Modernisation modérée par conteneurisation des services et utilisation de bases de données managées relationnelles.
3. **Trajectoire C : SaaS / Cloud-Native & Microservices Serverless** — Architecture hautement élastique (EKS, SQS, Bedrock, Serverless) conforme à la cible Clean Architecture et aux exigences C2 MASSIF.
4. **Trajectoire D : Lakehouse Unifié & IA Native (Data Platform + Ingestion massive)** — Approche centrée sur l'analytique et le traitement massif des flux de données non structurées (factures, rapports d'expertise).

### Tableau comparatif consolidé (Horizon 3 Ans)

| Postes de Dépenses & Indicateurs | Trajectoire A : IaaS Lift & Shift | Trajectoire B : PaaS Managé | Trajectoire C : SaaS / Cloud-Native (Cible Recommandée) | Trajectoire D : Lakehouse Unifié |
| :--- | :--- | :--- | :--- | :--- |
| **Architecture Cible** | VM EC2 monolithiques + RDS Oracle | ECS Fargate + Aurora PostgreSQL | EKS + Serverless (SQS/Lambda) + Bedrock | Data Lakehouse + Spark managé + EKS |
| **Coût Build / Migration (Initial)** | **180 k€ – 250 k€** (Faible refactoring, migration brute) | **450 k€ – 600 k€** (Conteneurisation et adaptation base) | **850 k€ – 1 100 k€** (Refactoring profond, TDD, Clean Arch) | **1 200 k€ – 1 600 k€** (Refonte data platform & pipelines ETL) |
| **Coût Run Annuel (Infrastructure & Compute)** | **420 k€ / an** (Provisionnement fixe surdimensionné pic) | **280 k€ / an** (AutoScale modéré, instances réservées) | **190 k€ / an** (Optimisation Serverless & Compute Elastic) | **340 k€ / an** (Calcul lourd analytique & stockage massif) |
| **Coût Run sur 3 Ans (Infrastructure)** | **1 260 k€ – 1 400 k€** | **840 k€ – 950 k€** | **570 k€ – 650 k€** | **1 020 k€ – 1 150 k€** |
| **Coût Licences & Support (3 Ans)** | **900 k€ – 1 200 k€** (Licences Oracle RAC / WebLogic on-core) | **150 k€ – 250 k€** (Bases de données managées, paquets) | **50 k€ – 100 k€** (Open-source, composants managés AWS) | **200 k€ – 350 k€** (Licences Data Platform / Moteurs) |
| **TCO Global estimé (3 Ans)** | **2 340 k€ – 2 850 k€** | **1 440 k€ – 1 800 k€** | **1 470 k€ – 1 850 k€** | **2 420 k€ – 3 100 k€** |
| **Indice de Risque FinOps & Technique** | **Élevé** (Dette technique, surcoût licences) | **Modéré** (Verrouillage PaaS modéré) | **Maîtrisé** (Élastique, gouvernance stricte FinOps) | **Élevé** (Complexité de traitement, coûts cachés S3/Egress) |

---

## 2. FOURCHETTE DE TCO À 3 ANS & CALCUL DU ROI

### Modélisation du Coût Global de Possession (TCO) Min / Max

Le TCO global intègre la formule : $\text{TCO}_{3\text{ans}} = \text{Coût Build} + (\text{Coût Run Annuel} \times 3) + \text{Coût Licences (3 ans)}$.

* **Trajectoire A (IaaS Lift & Shift) :**
  * Min : $180\text{ k€} + (420\text{ k€} \times 3) + 900\text{ k€} = \mathbf{2\,340\text{ k€}}$
  * Max : $250\text{ k€} + (480\text{ k€} \times 3) + 1\,200\text{ k€} = \mathbf{2\,890\text{ k€}}$
* **Trajectoire B (PaaS Managé) :**
  * Min : $450\text{ k€} + (280\text{ k€} \times 3) + 150\text{ k€} = \mathbf{1\,440\text{ k€}}$
  * Max : $600\text{ k€} + (320\text{ k€} \times 3) + 250\text{ k€} = \mathbf{1\,810\text{ k€}}$
* **Trajectoire C (Cloud-Native / Clean Architecture — Cible Recommandée) :**
  * Min : $850\text{ k€} + (190\text{ k€} \times 3) + 50\text{ k€} = \mathbf{1\,470\text{ k€}}$
  * Max : $1\,100\text{ k€} + (220\text{ k€} \times 3) + 100\text{ k€} = \mathbf{1\,860\text{ k€}}$
* **Trajectoire D (Lakehouse Unifié) :**
  * Min : $1\,200\text{ k€} + (340\text{ k€} \times 3) + 200\text{ k€} = \mathbf{2\,420\text{ k€}}$
  * Max : $1\,600\text{ k€} + (400\text{ k€} \times 3) + 350\text{ k€} = \mathbf{3\,150\text{ k€}}$

### Analyse du Retour sur Investissement (ROI)

Bien que la Trajectoire C présente un coût de Build initial élevé ($850\text{ k€} - 1\,100\text{ k€}$) lié à l'exigence de Clean Architecture et au développement des adaptateurs IA/Bedrock, son coût de Run récurrent est le plus bas du marché ($190\text{ k€}/an$) grâce à l'élasticité asynchrone (KEDA/SQS) et à l'élimination totale des licences logicielles propriétaires.

* **Économie récurrente (Run + Licences) par rapport au statu quo / Trajectoire A :** $\approx 550\text{ k€}$ à $700\text{ k€}$ par an.
* **Calcul du ROI (Horizon 3 ans) :**
  $$\text{ROI} = \frac{\text{Gains cumulés sur 3 ans} - \text{Investissement Initial (Build)}}{\text{Investissement Initial (Build)}} \times 100$$
  * En prenant un investissement initial médian de $975\text{ k€}$ et des gains annuels de $600\text{ k€}$ (soit $1\,800\text{ k€}$ sur 3 ans) :
    $$\text{ROI} = \frac{1\,800\text{ k€} - 975\text{ k€}}{975\text{ k€}} \times 100 \approx \mathbf{+84.6\%}$$
* **Délai de récupération du capital (Payback Period) :** $\approx 18\text{ mois}$ après la bascule en production.

---

## 3. MATRICE COMPARATIVE DÉTAILLÉE DES « POUR » ET DES « CONTRE »

| Trajectoire | Pour (+) | Contre (-) |
| :--- | :--- | :--- |
| **Trajectoire A :<br>IaaS Lift & Shift** | • Investissement initial minimal<br>• Migration rapide sans refactoring du code existant<br>• Conservation totale des habitudes d'exploitation | • Maintien de la dette technique et du monolithe fragile<br>• Coûts de licences Oracle/WebLogic exorbitants<br>• Incapacité avérée à absorber les pics climatiques (SPOF Oracle RAC) |
| **Trajectoire B :<br>PaaS Managé** | • Réduction sensible de la charge d'administration des bases de données<br>• Conteneurisation facilitant le déploiement<br>• TCO global modéré à moyen terme | • Verrouillage fournisseur (*vendor lock-in*) sur les services PaaS propriétaires<br>• Flexibilité limitée pour l'optimisation fine des coûts d'inférence IA<br>• Refactoring partiel insuffisant pour une architecture Zero-Trust stricte |
| **Trajectoire C :<br>Cloud-Native (Cible)** | • Adéquation parfaite avec la Clean Architecture et le TDD<br>• Élasticité totale et absorption des pics (x10) sans sur-provisionnement<br>• Conformité C2 MASSIF rigoureuse (Bedrock, KMS CMK, isolation)<br>• Coûts de Run et de licences minimaux | • Coût de Build initial élevé nécessitant des compétences expertes en Software Craftsmanship<br>• Complexité initiale de mise en œuvre de la gouvernance asynchrone |
| **Trajectoire D :<br>Lakehouse Unifié** | • Puissance analytique maximale pour le croisement des données historiques et de la fraude<br>• Unification des mondes Data et Transactionnel | • Sur-ingénierie massive pour un cœur de traitement de sinistres opérationnel<br>• Coûts de stockage et de calcul analytique très élevés (Run onéreux)<br>• Risque de latence inadapté au traitement temps réel des dossiers $< 2\,000\text{ €}$ |

---

## 4. RECOMMANDATION D'ARBITRAGE ARGUMENTÉE & CALENDRIER PHASÉ

### Recommandation d'Arbitrage

En tant que spécialiste FinOps & TCO, **l'arbitrage formel se porte sur la Trajectoire C (Cloud-Native & Clean Architecture sur AWS Mono-Cloud)**. 

1. **Justification Économique :** C'est la seule option qui rompt définitivement avec la spirale inflationniste des licences logicielles propriétaires (Oracle/WebLogic). L'investissement initial en Build est largement compensé par la division par deux des coûts de Run dès la deuxième année.
2. **Alignment Stratégique & Réponse à la Red Team :** En abandonnant le Scénario 3 (Multi-Cloud Hybride AWS/Azure) au profit d'un **Mono-Cloud AWS unifié**, AssurGlobal supprime les coûts cachés de transfert de données (*Data Egress*), élimine la latence inter-cloud et réduit drastiquement la complexité opérationnelle pour les équipes d'exploitation.
3. **Maîtrise du Risque Financier :** L'application stricte des règles FinOps (instances Spot pour les traitements non critiques, Savings Plans sur les clusters EKS, chiffrement KMS optimisé) garantit que le budget ne dérivera pas lors des pics climatiques.

---

### Calendrier de Bascule Financièrement Optimisé (Phasage SAFe 6)

Le plan de déploiement est cadencé pour lisser les dépenses d'investissement (Build) et sécuriser un retour sur investissement rapide par incréments de valeur (PI - Program Increment).

```
[M0 - M3] Phase 1 : Cœur de Domaine & Socle AWS
   │
   ├──► [M4 - M6] Phase 2 : Adaptateurs Sécurisés & Bedrock (MVP)
   │      │
   │      └──► [M7 - M9] Phase 3 : Ingestion Asynchrone & Règle HITL (Pilote)
   │             │
   │             └──► [M10 - M12] Phase 4 : Industrialisation & Bascule Totale (Run Optimisé)
```

#### Phase 1 : Socle Fondationnel & Cœur de Domaine (Mois 1 à 3)
* **Actions FinOps & Build :** Initialisation de l'infrastructure as Code (Terraform) sur AWS. Développement du cœur de domaine DDD (JIRA-101, JIRA-102) en TDD strict.
* **Budget Consommé :** $\approx 250\text{ k€}$ (Build).
* **Jalon de Contrôle 1 (ARB 1) :** Validation de la couverture de tests unitaires à 100% sur le cœur pur sans dépendance d'infrastructure.

#### Phase 2 : Connexion des Adaptateurs & Enclave IA Bedrock (Mois 4 à 6)
* **Actions FinOps & Build :** Implémentation des adaptateurs S3 chiffrés KMS (JIRA-202) et intégration de l'adaptateur Amazon Bedrock avec Guardrails et anonymisation PII (JIRA-301, JIRA-302).
* **Budget Consommé :** $\approx 300\text{ k€}$ (Build) + $30\text{ k€}$ (Run test).
* **Jalon de Contrôle 2 (ARB 2) :** Audit de sécurité Zero-Trust (C2 MASSIF) et validation de la non-fuite de PII par l'équipe Red Team.

#### Phase 3 : Ingestion Asynchrone, SQS & Gouvernance HITL — Pilote (Mois 7 à 9)
* **Actions FinOps & Build :** Déploiement des adaptateurs entrants REST / SQS (JIRA-401) et mise en production d'un premier pilote ciblé sur un volume restreint de sinistres (règle HITL $< 2\,000\text{ €}$).
* **Budget Consommé :** $\approx 200\text{ k€}$ (Build) + $50\text{ k€}$ (Run pilote).
* **Jalon de Contrôle 3 (ARB 3) :** Mesure du taux d'automatisation (Straight-Through Processing $\ge 60\%$) et validation de la réactivité sous charge simulée.

#### Phase 4 : Industrialisation, Migration Totale & Optimisation FinOps (Mois 10 à 12)
* **Actions FinOps & Build :** Bascule définitive du trafic de production du monolithe WebLogic vers la nouvelle plateforme Cloud-Native. Mise en place des politiques de Capacity Management, Savings Plans AWS et des alertes de budget FinOps en temps réel.
* **Budget Consommé :** $\approx 150\text{ k€}$ (Build finalisation) + $60\text{ k€}$ (Run production).
* **Jalon de Clôture :** Décommissionnement complet du monolithe WebLogic et de la base Oracle RAC, actant la fin des paiements de licences et l'atteinte du régime de croisière FinOps ($190\text{ k€}/an$).