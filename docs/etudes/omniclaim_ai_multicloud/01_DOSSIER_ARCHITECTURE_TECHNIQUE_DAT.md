# Note de Cadrage d'Architecture Technique Préliminaire : Plateforme OmniClaim AI

**Programme :** Modernisation du Cœur Sinistres & Déploiement d'Agents IA en Production  
**Entreprise :** Groupe AssurGlobal  
**Classification des Données :** **C2 MASSIF**  
**Cadre Référentiel :** TOGAF 10 ADM, SAFe 6, Software Craftsmanship, Zero-Trust (NIST SP 800-207) & FinOps  
**Date :** Octobre 2026  

---

## 1. Synthèse du besoin & Vision d'architecture (Phase A TOGAF)

### Synthèse du besoin métier
AssurGlobal fait face à une impasse opérationnelle caractérisée par un délai de traitement des sinistres inacceptable (7 à 10 jours ouvrés), une vulnérabilité critique face aux pics climatiques (multiplication par 10 des volumes en 24h provoquant l'effondrement du monolithe Java EE / WebLogic 12c), ainsi qu'une lourde dette technique et des pertes financières liées à la fraude documentaire (80 M€/an). 

### Vision d'architecture (TO-BE)
La cible architecturale repose sur une **topologie Multi-Cloud hybride hautement résiliente** :
- **AWS (Zone Ingestion & Stream) :** Ingestion événementielle via Amazon MSK (Kafka), microservices métier sur Amazon EKS, Data Lake immuable (S3) et chiffrement par clés maîtres client (AWS KMS CMK).
- **Azure (Zone Cognitive & IA Souveraine) :** Enclave cognitive privée (Azure OpenAI / Llama-3 dédiés), moteur de recherche vectorielle (Azure AI Search), et barrières de modération (Azure AI Content Safety / NeMo).
- **Interconnexion Sécurisée :** Liaison inter-cloud dédiée (AWS Direct Connect / Azure ExpressRoute) à très faible latence (< 3 ms), avec chiffrement IPsec permanent sans transit par l'Internet public.

---

## 2. Exigences clés & Besoins Non-Fonctionnels (Scalabilité, Résilience, Sécurité)

1. **Scalabilité & Élasticité :** Absorption des pics de charge climatiques par l'architecture événementielle asynchrone (Back-pressure gérée par Kafka) et l'autoscale des pods sur EKS (KEDA / Cluster Autoscaler), éliminant les goulets d'étranglement du cluster Oracle RAC.
2. **Résilience & Isolation des pannes :** Implémentation de patterns de résilience distribués (Circuit Breaker, Bulkhead, Retry avec backoff exponentiel) et isolation stricte du domaine métier par rapport aux services externes et aux LLMs.
3. **Sécurité Zero-Trust (NIST SP 800-207 & C2 MASSIF) :** 
   - Anonymisation locale et déterministe des PII avant toute transmission externe.
   - Protection anti-prompt injection via des *Guardrails* dédiés en amont des inférences.
   - Enclave d'inférence étanche via Private Endpoints (zéro exposition sur API publique, interdiction formelle de réentraînement sur les données clients).
4. **Gouvernance Human-in-the-Loop (HITL) :** Automatisation totale pour les sinistres $< 2\,000\text{ €}$ et score de fraude $< 0.15$ ; routage systématique vers un gestionnaire humain au-delà de ces seuils.
5. **FinOps & Maîtrise des Coûts :** Minimisation du trafic de données (Data Egress) inter-cloud en ne faisant transiter que des métadonnées JSON légères (les flux lourds restant dans S3), combinée à un arbitrage économique entre modèles managés et open-source (Llama-3 sur GPU réservés).

---

## 3. Propositions de scénarios d'infrastructure

### Scénario 1 : Monolithe Étendu On-Premise avec IA externe (API publique)
* **Description :** Modernisation superficielle du monolithe WebLogic et appels directs depuis le datacenter vers des APIs LLM publiques.
* **Avantages :** Investissement initial minimal, conservation des compétences existantes.
* **Inconvénients majeurs :** Violation critique de la conformité C2 MASSIF (fuite de PII vers l'extérieur), incapacité totale à absorber les pics climatiques (SPOF sur Oracle RAC et NAS SMB/NFS), latence et coûts réseau non maîtrisés. **(Rejeté)**

### Scénario 2 : Mono-Cloud 100% AWS avec services managés IA
* **Description :** Migration intégrale des charges et de l'IA sur un seul fournisseur Cloud (AWS et Amazon Bedrock).
* **Avantages :** Simplification de la topologie réseau, pas de trafic inter-cloud.
* **Inconvénients :** Risque de verrouillage fournisseur (*vendor lock-in*) sur les modèles cognitifs souverains, et moindre flexibilité pour l'optimisation des coûts d'inférence lourde à grande échelle. **(Écarté au profit du Scénario 3)**

### Scénario 3 : Multi-Cloud Hybride (AWS Ingestion & Stockage + Azure Enclave Cognitive) — *Cible retenue*
* **Description :** Séparation des préoccupations industrielles : AWS pour le flux transactionnel massif, la volumétrie et l'ingestion ; Azure pour l'enclave cognitive souveraine et la recherche vectorielle. Liaison sécurisée ExpressRoute / Direct Connect.
* **Avantages :** Exploitation des meilleures briques technologiques de chaque cloud, souveraineté renforcée, isolation parfaite des données sensibles, maîtrise granulaire des coûts FinOps.

---

## 4. Recommandation argumentée du Solution Architect

En tant qu'Architecte Solution, **le Scénario 3 est formellement recommandé** pour les raisons fondatrices suivantes :

1. **Adéquation avec la classification C2 MASSIF :** L'utilisation d'une enclave Azure dédiée couplée à un filtrage PII local garantit un niveau de sécurité conforme aux exigences bancaires et de santé les plus strictes.
2. **Découplage strict (Architecture Hexagonale) :** L'encapsulation de la logique d'intelligence artificielle derrière le port secondaire `ClaimAnalyzerPort` protège le domaine métier contre toute modification des SDK ou des fournisseurs cloud, garantissant la testabilité et la maintenabilité du code (Software Craftsmanship).
3. **Typage fort et intégrité financière :** Utilisation systématique du Value Object `Amount(cents: int, currency: str)` pour éliminer tout risque d'arrondi ou d'erreur de calcul sur les indemnisations.
4. **Robustesse face aux crises climatiques :** Le couplage d'Amazon MSK et de l'architecture asynchrone découple l'ingestion des dossiers de leur traitement par les agents IA, absorbant sans rupture les multiplicateurs de charge de crise.

---

## 5. Risques préliminaires identifiés & Points d'attention pour les comités d'architecture

* **Risque 1 (Sécurité / IA) :** Tentatives d'injection de prompt ou d'extraction de données via des factures/devis falsifiés par des tiers.
  * *Atténuation :* Mise en place rigoureuse des barrières de modération (NeMo / Azure AI Content Safety) et validation stricte des schémas JSON en sortie d'extraction.
* **Risque 2 (FinOps / Réseau) :** Explosion des coûts de transfert de données (*Data Egress*) entre AWS et Azure.
  * *Atténuation :* Politique stricte de transfert de métadonnées légères uniquement ; maintien des binaires et documents lourds dans le Data Lake AWS S3 d'origine.
* **Risque 3 (Gouvernance / Métier) :** Effet de bord ou dérive décisionnelle d'un agent IA sur des indemnisations complexes.
  * *Atténuation :* Application intransigeante de la règle HITL (seuil strict de 2 000 € et score de risque de fraude $\ge 0.15$).