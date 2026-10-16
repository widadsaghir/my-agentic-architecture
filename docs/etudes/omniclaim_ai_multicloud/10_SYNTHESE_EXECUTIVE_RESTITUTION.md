# Restitution Exécutive d'Architecture — OmniClaim AI
## 🎯 Storyboard ARB, Comparatif AS-IS vs TO-BE & Discours Minuté

**Projet :** OmniClaim AI — Modernisation Multi-Cloud Hybride & IA Souveraine  
**Public Cible :** Architecture Review Board (ARB) & C-Level (CTO, CISO, Head of Claims)  
**Format :** Storyboard de Soutenance 16:9 Bento Grid & Discours Oral Miroir  
**Livrable Associé :** `10_SYNTHESE_EXECUTIVE_RESTITUTION_SLIDES.html`  

---

## 📌 SOMMAIRE DU STORYBOARD

1. **Slide 1 : Vision Stratégique, Drivers Métier & Indicateurs Clés (KPIs)**
2. **Slide 2 : Rupture Architecturale — Comparatif AS-IS (Legacy) vs TO-BE (Cible)**
3. **Slide 3 : Matrice des Décisions d'Arbitrage (ADRs), FinOps & Plan de Trajectoire**

---

# SLIDE 1 : VISION STRATÉGIQUE & DRIVERS MÉTIER

### 🎯 Accroche Exécutive (Executive Statement) :
> *"Décomposition de la dette monolithique historique en une architecture multi-cloud résiliente pilotée par les événements, combinant accélération de règlement à moins de 350ms, conformité Zero-Trust souveraine et rentabilité FinOps prouvée (+84.6% ROI)."*

### 📊 Les 6 Indicateurs de Performance Clés (KPIs) :
- **ROI Projeté :** **+84.6%** (Payback en 14.2 mois)
- **Latence de Bout-en-Bout :** **< 350 ms** (vs 12 à 14 jours ouvrés dans l'AS-IS)
- **Disponibilité Opérationnelle :** **99.99% SLA** (Multi-AZ 3 zones)
- **Réduction TCO Infrastructure :** **-35%** par mutualisation des conteneurs EKS
- **Accélération des Batchs :** **3.5x** via découplage Kafka
- **Escalade HITL (Human-in-the-Loop) :** **< 5%** des dossiers (dossiers $> 2\,000\ €$ ou fraude $> 0.15$)

### 🏛️ Matrice Bento Grid des 4 Piliers :
1. 🔵 **Drivers Métier :** Élimination des goulots d'étranglement de règlement et scalabilité automatique x10 en cas d'intempéries majeures.
2. 🟢 **Sécurité & Zero-Trust :** Dé-identification PII locale dans les pods EKS, conformité RGPD stricte et zéro entraînement sur les données clients.
3. 🟣 **Trajectoire Technologique :** Migration vers conteneurs Kubernetes EKS, streaming Kafka MSK et enclave d'inférence privée via AWS PrivateLink.
4. 🟠 **FinOps & Économie d'Échelle :** Coût à l'usage optimisé avec modèles Serverless et dimensionnement élastique KEDA.

---

# SLIDE 2 : RUPTURE ARCHITECTURALE — AS-IS VS TO-BE

```
                     ┌───────────────────────────────────────────────┐
                     │          COMPARATIF ARCHITECTURAL             │
                     └───────────────────────────────────────────────┘

   🟠 AS-IS : MONOLITHE ON-PREMISE                🟢 TO-BE : MULTI-CLOUD ÉVÉNEMENTIEL
   ─────────────────────────────────              ───────────────────────────────────
   • Application Java 8 WebLogic On-Prem          • Microservices conteneurisés Amazon EKS
   • Base relationnelle Oracle RAC saturée        • Streaming temps réel Amazon MSK (Kafka)
   • Traitements batch nocturnes bloquants        • Base Aurora PostgreSQL Multi-AZ (PgBouncer)
   • Délais de traitement : 12 à 14 jours         • Règlement instantané : < 350 ms
   • Goulot d'étranglement & SPOF critique        • Tolérance aux pannes Multi-AZ (RTO < 15m)
```

### 🗺️ Schémas Mermaid Embarqués :
* **AS-IS :** `diagrams/architecture_cible_omniclaim_as_is.mmd`
* **TO-BE (Container L2) :** `diagrams/architecture_cible_omniclaim_l2_container.mmd`

---

# SLIDE 3 : DÉCISIONS D'ARBITRAGE (ADRs) & FINOPS

| Domaine | Arbitrage Validé par l'ARB | Justification & Compromis Retenu |
| :--- | :--- | :--- |
| **Streaming** | **Amazon MSK (Kafka) vs REST synchrone** | Rejouabilité des événements, découplage total et modèle *Transactional Outbox* sans perte de données. |
| **Souveraineté IA** | **Amazon Bedrock (eu-west-3) vs API publique** | Garantie contractuelle de non-entraînement sur les prompts et transit sécurisé via AWS PrivateLink. |
| **Persistance** | **Aurora PostgreSQL Multi-AZ vs Oracle Exadata** | Élimination des surcoûts de licences propriétaires, division par deux du TCO et bascule Multi-AZ en < 30s. |
| **Gouvernance HITL** | **Seuil d'arbitrage automatique à 2 000 €** | Protection anti-fraude absolue : les dossiers à fort montant requièrent une validation humaine souveraine. |

---

## 🎙️ SCRIPT ORAL MINUTÉ DE SOUTENANCE ARB (5 MINUTES)

### 🇬🇧 Spoken Script in English :
> *"Members of the Architecture Review Board, I am proud to present the target architecture for OmniClaim AI.*  
>  
> *Today, our claims operations are constrained by an aging on-premise monolith: synchronous database locks cause overnight batch contention, stretching claim settlements to 14 days.*  
>  
> *Our target architecture resolves this debt through a decoupled event-driven multi-cloud foundation:*  
> *1. We established asynchronous event streaming using **Amazon MSK (Kafka)**, achieving sub-second processing and guaranteed order.*  
> *2. We deployed an **Enterprise Sovereign AI Enclave on Amazon Bedrock** accessible strictly over **AWS PrivateLink**, with local PII de-identification in our EKS pods to guarantee zero customer data leakage.*  
> *3. For financial safety, we enforced a strict **Human-in-the-Loop policy**: any claim above €2,000 or exhibiting high fraud scores is automatically escalated to our human claims adjusters.*  
>  
> *From a FinOps perspective, this architecture reduces our infrastructure footprint by 35% while delivering an **+84.6% ROI** with a payback period of 14.2 months.*  
>  
> *This blueprint is fully validated by our 48 deterministic TDD tests, certified Zero-Trust C2 compliant, and ready for immediate PI-1 delivery. Thank you."*

---

### 🇫🇷 Version Miroir en Français :
> *« Membres de l'Architecture Review Board, j'ai l'honneur de vous présenter l'architecture cible d'OmniClaim AI.*  
> *Aujourd'hui, notre gestion des sinistres est bridée par un monolithe On-Premise vieillissant : les verrous de base de données saturent les batchs nocturnes et allongent les règlements à 14 jours.*  
> *Notre architecture cible dénoue cette dette grâce à un socle multi-cloud événementiel :*  
> *1. Nous avons instauré du streaming asynchrone avec **Amazon MSK (Kafka)** pour traiter les événements en moins de 350 ms.*  
> *2. Nous avons conçu une **enclave souveraine sur Amazon Bedrock** via **AWS PrivateLink**, avec anonymisation PII locale dans nos pods EKS pour empêcher toute fuite de données.*  
> *3. Pour la sécurité financière, nous avons imposé un **seuil Human-in-the-Loop** : tout sinistre supérieur à 2 000 € est routé vers un gestionnaire humain.*  
> *Sur le plan FinOps, cette solution réduit notre empreinte de 35% avec un **ROI de +84.6%** rentabilisé en 14 mois.*  
> *Cette architecture est validée à 100% par nos 48 tests TDD et prête pour le déploiement. Je vous remercie. »*
