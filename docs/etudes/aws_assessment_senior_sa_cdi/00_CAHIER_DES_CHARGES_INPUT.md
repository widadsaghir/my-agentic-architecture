# 🎯 Cahier des Charges & Cadrage d'Entraînement : Assessment Technique AWS (Senior / Principal Solutions Architect L6-L7)

**Programme :** Préparation Intensive & Entraînement Assessment Technique — Recrutement AWS CDI  
**Cible Professionnelle :** **Senior Solutions Architect (L6)** / **Principal Solutions Architect (L7)** chez Amazon Web Services (AWS)  
**Objectif Rémunération :** **Top de marché (Maximum Package)** — Fourchette cible Total Comp : **180 k€ - 240 k€+** (Base fixe + Variable / Sign-on bonus Années 1-2 + RSUs Amazon vestées sur 4 ans)  
**Cadre Méthodologique :** AWS Well-Architected Framework (6 Piliers), Amazon Leadership Principles (STAR), TOGAF 10 ADM, SAFe 6 for Architects, Software Craftsmanship (Hexagonale, DDD, TDD, Resilient Event-Driven Architecture)  
**Comité Virtuel d'Évaluation :** Werner Vogels (CTO AWS), Martin Fowler, Uncle Bob, Sam Newman, Alistair Cockburn + Bar Raiser AWS Virtuel  
**Date d'Initialisation :** Octobre 2026  

---

## 1. Ambition & Positionnement Stratégique

### 1.1. L'Objectif Ultime
Décrocher une offre ferme d'embauche en CDI chez AWS au plus haut niveau de classification et de rémunération possible en tant qu'Architecte de Solutions d'Élite, grâce à une démonstration irréfutable d'excellence technique, de leadership d'influence et de maîtrise des architectures distribuées à très grande échelle.

### 1.2. Ce qui sépare un "Hire" standard d'un "Strong Hire" au Salaire Maximal (Bar Raiser Standard)
Chez AWS, le package salarial dépend directement du **Leveling (L6 vs L7)** et de l'évaluation globale par le panel d'interviewers et le **Bar Raiser** :
1. **Profondeur Technique ("Dive Deep") sans langue de bois :** Maîtrise des couches réseau bas niveau (VPC, Transit Gateway, Route 53, Direct Connect), des mécanismes de stockage distribué (DynamoDB partition keys, S3 Strong Consistency), de l'asynchronisme (SQS FIFO, SNS, EventBridge, Kinesis) et de la résilience (Cell-based architecture, Shuffle Sharding, Chaos Engineering).
2. **Arbitrages d'Architecture et Frugalité ("Frugality" & "Invent and Simplify") :** Savoir expliquer *pourquoi* une solution a été choisie plutôt qu'une autre en quantifiant le coût (FinOps), la latence p99 et la charge opérationnelle (Undifferentiated Heavy Lifting).
3. **Obsession Client & Impact Business ("Customer Obsession" & "Deliver Results") :** Ne jamais concevoir la technique pour la technique, mais lier chaque choix d'infrastructure à un ROI mesurable, à la disponibilité du service et à la satisfaction client.
4. **Capacité à convaincre au Whiteboard ("Have Backbone; Disagree and Commit" & "Earn Trust") :** Défendre ses choix avec calme, rigueur et autorité face aux questions pièges des Principal Architects d'AWS.

---

## 2. Le Défi Technique de l'Assessment (Le Scénario Whiteboard)

Pour l'entraînement, nous retenons un scénario de complexité critique représentatif des entretiens AWS L6/L7 :

### Scénario : « Global Mission-Critical Real-Time Fintech & Billing Platform »
- **Échelle :** 50 millions de transactions quotidiennes, pic à 25 000 transactions/seconde, couverture multi-régions (Europe & Amérique du Nord).
- **Contraintes SLA / SLO :**
  - Latence p99 $< 50\text{ ms}$ en lecture, $< 150\text{ ms}$ en écriture.
  - Disponibilité $\ge 99.999\%$ (Five Nines), avec $RPO = 0$ (aucune perte de transaction financière autorisée) et $RTO < 30\text{ secondes}$.
- **Sécurité & Conformité :**
  - Données financières et bancaires hautement sensibles (PCI-DSS Level 1, ISO 27001, RGPD / Souveraineté européenne).
  - Chiffrement bout en bout (In-Transit mTLS 1.3, At-Rest KMS CMK avec rotation automatique et HSM CloudHSM).
  - Cloisonnement Zero-Trust strict (Multi-Accounts AWS Organizations, SCPs, IAM Identity Center, VPC PrivateLink, zéro exposition directe sur Internet).
- **Legacy & Transition :**
  - Coexistence avec un cœur monolithique historique On-Premise via AWS Direct Connect résilient.
  - Découplage progressif via Strangler Fig Pattern et Event Sourcing (Kafka / Amazon MSK ou Kinesis + DynamoDB).

---

## 3. Les 6 Piliers du Well-Architected Framework à Maîtriser

| Pilier AWS | Exigences Clés pour l'Assessment L6/L7 |
| :--- | :--- |
| **1. Operational Excellence** | Infrastructure as Code (Terraform / AWS CDK), Observabilité distribuée (OpenTelemetry, CloudWatch Container Insights, X-Ray), Runbooks automatisés, GameDays et injection d'erreurs (AWS Fault Injection Simulator). |
| **2. Security (Zero-Trust)** | Multi-Account Landing Zone (Control Tower), Service Control Policies (SCPs), IAM Permissions Boundaries, Envelope Encryption via KMS, AWS WAF, GuardDuty, Macie, Secrets Manager avec rotation automatique. |
| **3. Reliability & Resilience** | Architecture Multi-AZ & Multi-Régions (Active-Active ou Warm Standby), Route 53 ARC (Application Recovery Controller), Cell-Based Architecture, Découplage asynchrone SQS / Dead Letter Queues (DLQ), Backoff exponentiel et Jitter. |
| **4. Performance Efficiency** | Caching multi-niveaux (CloudFront, ElastiCache Redis, DAX), architectures serverless vs containers (Lambda vs ECS/EKS Fargate), Right-Sizing dynamique, Auto-Scaling réactif et prédictif. |
| **5. Cost Optimization (FinOps)** | Arbitrage On-Demand vs Savings Plans / Reserved Instances vs Spot, politiques de cycle de vie S3 (Intelligent-Tiering, Glacier Flexible/Instant), élimination des transferts de données inter-AZ inutiles, tagging strict des coûts. |
| **6. Sustainability** | Optimisation de l'empreinte carbone (AWS Customer Carbon Footprint Tool), adoption des processeurs ARM AWS Graviton (3/4) pour un meilleur ratio performance/watt. |

---

## 4. Alignement Leadership Principles (Amazon LPs) & Histoires STAR

L'assessment technique AWS évalue en continu l'ancrage des Leadership Principles à travers les réalisations concrètes :

1. **Customer Obsession :** Exemple concret où une décision d'architecture a directement protégé les utilisateurs finaux contre une panne majeure ou un surcoût.
2. **Dive Deep :** Capacité à descendre au niveau des octets, des paquets réseau, des plans d'exécution SQL/NoSQL ou des verrous distribués pour diagnostiquer un incident complexe.
3. **Invent and Simplify :** Transformation d'un processus lourd et coûteux en une brique élégante, hautement réutilisable et automatisée.
4. **Are Right, A Lot :** Anticipation d'un écueil technologique majeur (ex: piège du multi-cloud naïf ou saturation d'un cluster) et réorientation précoce de l'équipe vers la solution pérenne.
5. **Think Big :** Conception d'une vision d'architecture capable de scaler x10 ou x100 sans réécriture logicielle majeure.
6. **Have Backbone; Disagree and Commit :** Capacité à challenger fermement un choix d'architecture sous-optimal face à un client ou un manager, arguments chiffrés à l'appui, tout en sachant exécuter la décision finale.

---

## 5. Découpage du Plan d'Entraînement en US & Enablers

- **US 1 (Cadrage & Design Whiteboard) :** Modélisation de l'architecture cible du cas pratique (schémas C4, flux, topologie VPC multi-comptes, choix de services).
- **US 2 (Audit Contradictoire & Questions Pièges du Jury AWS) :** Session de questions/réponses intenses par la brigade d'agents (Werner Vogels et Red Team simulant les Principal Architects AWS).
- **US 3 (Focus Deep-Dive Sécurité & Résilience) :** Réponses détaillées sur les scénarios de sinistre (Partition Split, panne AZ, fuite de données, failover inter-régions).
- **US 4 (Préparation STAR des Leadership Principles) :** Formulation des 6 à 8 récits clés STAR basés sur l'expérience réelle et les projets d'envergure menés (Félix, OmniClaim, etc.).
- **US 5 (Pitch & Stratégie de Négociation du Package Maximal) :** Préparation du discours oral de soutenance et des leviers de négociation salariale (Total Comp L6/L7).
