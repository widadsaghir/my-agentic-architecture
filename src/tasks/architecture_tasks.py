from crewai import Task, Agent

def create_preliminary_design_task(agent: Agent, user_input: str, language: str) -> Task:
    """
    Crée la tâche de conception de Dossier d'Architecture Technique (DAT) de niveau Grand Compte / Big Tech.
    Exige une modélisation C4 complète (AS-IS et TO-BE Niveaux 1 à 4) avec schémas Mermaid intégrés,
    un dimensionnement capacitaire quantifié, une matrice réseau/secrets, les patterns Big Tech,
    l'environnementalisme (DEV/INT/PERF/PROD), le code Terraform et le volet SRE / MCO.
    """
    description = (
        f"En tant que Lead Solution Architect d'élite inspiré par les standards d'ingénierie des Grands Comptes (Netflix, Spotify, Amazon) :\n"
        f"Analyser l'expression de besoin ou les notes de cadrage suivantes :\n"
        f"\"\"\"\n{user_input}\n\"\"\"\n\n"
        f"Concevoir et rédiger le Dossier d'Architecture Technique (DAT) de référence complet, rigoureux et prêt pour la validation par l'Architecture Review Board (ARB).\n\n"
        f"VOTRE DAT DOIT COUVRIR DE FAÇON EXHAUSTIVE LES 8 CHAPITRES INDUSTRIELS SUIVANTS :\n\n"
        f"1. 🏛️ SYNTHÈSE DU BESOIN & VISION D'ARCHITECTURE (TOGAF Phase A & B) :\n"
        f"   - Objectifs business, drivers stratégiques et cartographie des parties prenantes.\n"
        f"   - Modélisation de l'architecture existante AS-IS avec schéma Mermaid intégré illustrant les SPOF et goulots d'étranglement.\n\n"
        f"2. 🗺️ CARTOGRAPHIE C4 MULTI-NIVEAUX (TO-BE) AVEC SCHÉMAS MERMAID EMBARQUÉS :\n"
        f"   - Niveau 1 (System Context) : Frontières du système, utilisateurs et partenaires externes.\n"
        f"   - Niveau 2 (Container Diagram) : Découpage applicatif, brokers d'événements, bases de données, enclaves IA.\n"
        f"   - Niveau 3 (Component Diagram) : Architecture Hexagonale interne d'un microservice clé (Domaine, Ports SPI/API, Adaptateurs).\n"
        f"   - Niveau 4 (Deployment & Network Topology) : Topologie physique Cloud Multi-AZ, VPC, subnets privés, PrivateLink, passerelles de transit.\n"
        f"   - Diagramme de séquence de bout en bout (Déclaration -> Dé-identification PII -> Inférence IA -> HITL -> Règlement).\n"
        f"   *IMPORTANT : Chaque schéma doit être rédigé sous forme de bloc de code ```mermaid valide dans le corps du DAT.*\n\n"
        f"3. 📊 DIMENSIONNEMENT CAPACITAIRE & VOLUMÉTRIE QUANTIFIÉE :\n"
        f"   - Calcul précis de la charge nominale et des pics exceptionnels (x10 en 24h).\n"
        f"   - Dimensionnement vCPU/RAM des clusters de calcul (ex: EKS/AKS) et politique d'autoscaling (HPA/KEDA).\n"
        f"   - Dimensionnement des clusters de streaming (partitionnement Kafka, rétention, débit Mo/s, IOPS SSD).\n"
        f"   - Dimensionnement des bases de données (instances primaires Multi-AZ, read replicas, pool de connexions).\n\n"
        f"4. 🔒 SÉCURITÉ ZERO-TRUST, CHIFFREMENT & GESTION DES SECRETS (C2 MASSIF) :\n"
        f"   - Authentification et autorisation (mTLS inter-services, jetons OIDC/OAuth 2.0 avec scopes fins).\n"
        f"   - Gestion des clés de chiffrement client (KMS CMK / Cloud HSM) au repos et en transit (TLS 1.3).\n"
        f"   - Gestion et rotation automatique des secrets d'infrastructure tous les 30 jours (Secrets Manager / Vault).\n"
        f"   - Garde-fous IA : Dé-identification PII locale, barrières anti-prompt injection et politique d'enclave souveraine.\n\n"
        f"5. ⚡ PATTERNS D'ARCHITECTURE & RÉSILIENCE BIG TECH :\n"
        f"   - Résilience : Déploiement Multi-AZ (3 zones), Circuit Breakers, Bulkheads, Dead Letter Queues (DLQ).\n"
        f"   - Cohérence des données : Transactional Outbox Pattern, clés d'idempotence et Saga Pattern pour les paiements.\n"
        f"   - Objectifs de reprise : RTO < 15 minutes et RPO = 0 (zéro perte de données en cas de panne de datacenter).\n\n"
        f"6. 🌍 TOPOLOGIE DES ENVIRONNEMENTS & STRATÉGIE DE DÉPLOIEMENT :\n"
        f"   - Ségrégation étanche des 4 environnements : DEV, INT (Recette métier), PERF (Tirs de charge de masse), PROD.\n"
        f"   - Isolation par comptes / abonnements Cloud distincts.\n"
        f"   - Stratégie de déploiement continu sans interruption (Blue-Green / Canary Deployments).\n\n"
        f"7. 💻 SQUELETTE D'INFRASTRUCTURE AS CODE (TERRAFORM / OPENTOFU) :\n"
        f"   - Fournir un exemple concret de code Terraform HCL modulaire déployant l'infrastructure sécurisée (VPC, Subnets privés, Cluster conteneurs, Enclave sécurisée, Private Endpoints).\n\n"
        f"8. 🩺 MCO, OBSERVABILITÉ & INGÉNIERIE SRE (RUN) :\n"
        f"   - Définition des SLI/SLO/SLA (ex: Disponibilité 99.99%, latence P99 < 1.5s, Error Budget).\n"
        f"   - Observabilité Full-Stack (OpenTelemetry, traçage distribué, métriques RED/USE, logs centralisés).\n"
        f"   - Matrice des astreintes et Runbook opérationnel d'incident.\n\n"
        f"IMPORTANT : Rédiger l'intégralité de ce Dossier d'Architecture Technique en langue [{language}]."
    )

    expected_output = (
        f"Un Dossier d'Architecture Technique (DAT) de niveau Grand Compte en Markdown rédigé impérativement en [{language}], structuré comme suit :\n"
        f"1. 🏛️ Synthèse du besoin & Vision d'architecture (Phase A TOGAF) avec Schéma AS-IS (Mermaid)\n"
        f"2. 🗺️ Cartographie C4 TO-BE Complète avec 5 Schémas Mermaid embarqués (Contexte L1, Conteneurs L2, Composants Hexagonaux L3, Déploiement Réseau Multi-AZ L4, Séquence de Flux)\n"
        f"3. 📊 Dimensionnement capacitaire, volumétrie et calculs de charge (vCPU, RAM, IOPS, Partitions Kafka)\n"
        f"4. 🔒 Sécurité Zero-Trust, Chiffrement KMS CMK, Gestion des Secrets et Garde-fous IA C2 MASSIF\n"
        f"5. ⚡ Patterns de Résilience Big Tech (Circuit Breakers, Outbox, Idempotence, RTO/RPO)\n"
        f"6. 🌍 Topologie des 4 Environnements (DEV, INT, PERF, PROD) et Déploiement Canary\n"
        f"7. 💻 Code d'Infrastructure as Code (Terraform / OpenTofu HCL modulaire)\n"
        f"8. 🩺 Observabilité SRE, Matrice SLI/SLO, Runbook d'incident et MCO."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent
    )

def create_security_audit_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche d'audit de sécurité et de conformité par le CISO (Brique 2).
    Prend en entrée le résultat de la tâche de conception pour évaluer les risques.
    """
    description = (
        f"Auditer rigoureusement la proposition d'architecture technique formulée par le Solution Architect.\n"
        f"Vérifier point par point :\n"
        f"- Le respect des principes Zero-Trust (NIST SP 800-207) et le cloisonnement réseau.\n"
        f"- Le niveau de classification des données (C1, C2, C2 massif, RGPD) et les exigences de chiffrement (au repos/en transit).\n"
        f"- La gestion sécurisée des secrets (KMS/Vault) et l'absence de clés en clair.\n"
        f"- Les critères d'homologation pour le passage en Dossier de Conformité Architecture (DCA).\n\n"
        f"IMPORTANT : Rédiger l'intégralité de votre avis de sécurité en langue [{language}]."
    )

    expected_output = (
        f"Une fiche d'audit et d'avis de conformité CISO en Markdown rédigée en [{language}], comprenant :\n"
        f"1. Avis global du CISO (Favorable / Favorable avec réserves / Défavorable)\n"
        f"2. Matrice d'analyse de classification des données (Niveau C2/C2 massif, impacts Cloud)\n"
        f"3. Exigences de sécurité obligatoires (Chiffrement CMK, Zero-Trust, Private Endpoints)\n"
        f"4. Recommandations impératives pour l'homologation DCA."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )

def create_challenge_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche de revue contradictoire et de challenge par le Challenger / Red Team (Brique 2.4).
    Prend en entrée la proposition du Solution Architect pour traquer les failles et la sur-ingénierie.
    """
    description = (
        f"Analyser et challenger de manière impitoyable et constructive la proposition d'architecture formulée par le Solution Architect.\n"
        f"Votre mission contradictoire consiste à :\n"
        f"- Identifier chaque point unique de défaillance (SPOF) potentiel et tester les hypothèses de résilience.\n"
        f"- Détecter les symptômes de sur-ingénierie et le syndrome du marteau doré (Golden Hammer) : y a-t-il des composants inutiles ?\n"
        f"- Proposer des simplifications radicales et pragmatiques en appliquant les principes KISS (Keep It Simple, Stupid) et YAGNI (You Aren't Gonna Need It).\n"
        f"- Formuler une liste de contre-propositions et d'arbitrages recommandés.\n\n"
        f"IMPORTANT : Rédiger l'intégralité de votre rapport de challenge en langue [{language}]."
    )

    expected_output = (
        f"Un rapport d'audit contradictoire (Red Team Review) en Markdown rédigé impérativement en [{language}], comprenant :\n"
        f"1. Synthèse du niveau de risque et de complexité (Faible / Modéré / Critique)\n"
        f"2. Matrice d'identification des SPOF et des risques de panne en cascade\n"
        f"3. Traque de la sur-ingénierie : composants superflus ou surdimensionnés à éliminer\n"
        f"4. Recommandations de simplification pragmatique (KISS/YAGNI) et alternatives sobres\n"
        f"5. Avis consultatif pour l'arbitrage du Lead Architect."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )

def create_software_crafting_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche de modélisation logicielle pure par le Software Crafter (Brique 2.2).
    Prend en entrée la macro-architecture pour concevoir les micro-patterns :
    Architecture Hexagonale (Ports & Adapters), DDD et stratégie de testabilité unitaire 100% TDD.
    """
    description = (
        f"Traduire la macro-architecture technique en micro-patterns logiciels purs et propres selon les principes du Software Craftsmanship.\n"
        f"Votre modélisation doit impérativement définir :\n"
        f"1. Le découplage en Architecture Hexagonale (Ports & Adapters) : identifier le Cœur de Domaine métier, les Ports d'Entrée (Drivers/Inbound), les Ports de Sortie (Driven/Outbound) et leurs Adaptateurs respectifs.\n"
        f"2. La modélisation Domain-Driven Design (DDD) : définir le Bounded Context, les Agrégats racines, les Entités et les Value Objects immuables.\n"
        f"3. La stratégie de testabilité unitaire (TDD 100%) : garantir que le domaine métier est testable avec 0 dépendance d'infrastructure et 0 token (tests unitaires purs, mocks/stubs des ports).\n"
        f"4. L'application des principes SOLID, Clean Code et KISS/YAGNI au niveau du code source.\n\n"
        f"IMPORTANT : Rédiger l'intégralité de votre guide de conception logicielle en langue [{language}]."
    )

    expected_output = (
        f"Un guide de conception logicielle Software Craftsmanship en Markdown rédigé en [{language}], comprenant :\n"
        f"1. Spécification de l'Architecture Hexagonale (Schéma textuel Domaine ⟷ Ports ⟷ Adaptateurs)\n"
        f"2. Modélisation DDD (Bounded Context, Agrégats, Entités, Value Objects)\n"
        f"3. Matrice de testabilité TDD (Pyramide des tests, typologie des tests unitaires déterministes)\n"
        f"4. Directives Clean Code & SOLID pour les développeurs des équipes de build."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )

def create_safe_delivery_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche de découpage delivery agile par le SAFe Agile Enabler (Brique 2.3).
    Prend en entrée les travaux d'architecture pour générer le backlog Jira opérationnel :
    Enabler Epics, Enabler Features, User Stories techniques et Definition of Done (DoD).
    """
    description = (
        f"Traduire l'ensemble du dossier d'architecture technique (macro-patterns, sécurité C2, architecture hexagonale) "
        f"en éléments de backlog agile directement exploitables par les équipes de build d'un train SAFe (ART).\n"
        f"Votre découpage opérationnel doit produire :\n"
        f"1. L'Enabler Epic chapeau structurant la trajectoire d'implémentation.\n"
        f"2. Les Enabler Features découpées verticalement par incrément de valeur.\n"
        f"3. Les User Stories techniques prêtes pour le backlog Jira (format : En tant que... Je souhaite... Afin de...).\n"
        f"4. Les critères d'acceptation opérationnels et la Definition of Done (DoD) pour chaque story (tests unitaires, couverture, revue de code, sécurité).\n\n"
        f"IMPORTANT : Rédiger l'intégralité du backlog et des User Stories en langue [{language}]."
    )

    expected_output = (
        f"Un backlog d'implémentation SAFe & Jira en Markdown rédigé en [{language}], comprenant :\n"
        f"1. Fiche Enabler Epic (Objectif, hypothèse de valeur, métriques de succès)\n"
        f"2. Liste des Enabler Features priorisées\n"
        f"3. Backlog détaillé des User Stories Jira techniques avec critères d'acceptation\n"
        f"4. Definition of Done (DoD) standardisée pour les équipes de développement."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )

def create_finops_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche d'évaluation stratégique de migration et d'analyse FinOps / TCO (Brique 2.5).
    Compare les différentes options Cloud, modélise le budget à 3 ans et produit la matrice des Pour/Contre.
    """
    description = (
        f"Réaliser une étude comparative exhaustive et rigoureuse des trajectoires de migration Cloud possibles "
        f"pour l'architecture évaluée (IaaS Lift & Shift, PaaS managé, SaaS / Cloud-Native, Lakehouse unifié).\n"
        f"Votre mission FinOps & Économique consiste à :\n"
        f"1. Modéliser et chiffrer les postes de dépenses : Coûts d'infrastructure Run récurrents, Coûts de Build / Migration, "
        f"et Coûts de Licences (avec Software Assurance, capacités réservées F-SKU ou équivalent).\n"
        f"2. Calculer le Coût Global de Possession (TCO) estimé sur 3 ans sous forme de fourchettes réalistes (Min / Max).\n"
        f"3. Établir une matrice comparative détaillée des « Pour » (+) et des « Contre » (-) pour chaque trajectoire.\n"
        f"4. Formuler une recommandation d'arbitrage argumentée et un calendrier de bascule financièrement optimisé.\n\n"
        f"IMPORTANT : Rédiger l'intégralité de l'étude stratégique de migration et du rapport FinOps en langue [{language}]."
    )

    expected_output = (
        f"Une étude stratégique de migration et comparatif FinOps / TCO en Markdown rédigée en [{language}], comprenant :\n"
        f"1. Tableau comparatif des options de migration avec coûts estimés Run, Build et Licences\n"
        f"2. Fourchette de TCO à 3 ans (Min / Max) et calcul du ROI (Retour sur Investissement)\n"
        f"3. Matrice des « Pour / Contre » détaillée par trajectoire\n"
        f"4. Recommandation d'arbitrage argumentée et calendrier de transition phasé."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )

def create_meta_maintenance_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche de méta-gouvernance et d'auto-maintenance du système (Brique 5.1).
    Analyse les logs d'exécution, audite la santé des agents et propose des patchs de prompts/code.
    """
    description = (
        f"Analyser l'exécution de la brigade d'architecture et auditer les traces d'échanges.\n"
        f"Votre mission de Méta-Gouvernance consiste à :\n"
        f"1. Évaluer la fluidité du passage de relais entre agents et identifier les éventuels goulots d'étranglement ou latences.\n"
        f"2. Détecter les dérives de prompts, les répétitions ou les signes d'hallucinations.\n"
        f"3. Formuler des recommandations de correctifs de prompts ou d'optimisation de code pour l'auto-guérison (Self-Healing) du système.\n\n"
        f"IMPORTANT : Rédiger votre rapport d'audit système en langue [{language}]."
    )

    expected_output = (
        f"Un rapport d'observabilité et d'auto-maintenance du système en Markdown rédigé en [{language}], comprenant :\n"
        f"1. Bilan d'exécution et taux de complétude des tâches de la brigade\n"
        f"2. Analyse de la santé des prompts et détection des dérives\n"
        f"3. Propositions de correctifs de prompts et de code pour le Self-Healing\n"
        f"4. Recommandations de dimensionnement pour les prochaines exécutions."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )

def create_career_branding_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche de valorisation de carrière et de personal branding (Brique 5.2).
    Met à jour les compétences du CV et génère un post LinkedIn percutant (REX).
    """
    description = (
        f"Extraire la substantifique moelle d'ingénierie et d'architecture démontrée dans cette étude pour valoriser le profil du Lead Architect.\n"
        f"Votre mission de Personal Branding consiste à :\n"
        f"1. Extraire les compétences, méthodologies et patterns appliqués (ex: Cloud WAF, Hexagonale, Zero-Trust, C2, FinOps, SAFe) sous forme de points d'impact pour un CV.\n"
        f"2. Rédiger un brouillon de post LinkedIn complet, engageant et professionnel (Retour d'Expérience - REX) prêt à la publication.\n"
        f"3. Cartographier les acquis de cette étude vers les référentiels de certification professionnelle (TOGAF 10, SAFe for Architects, Azure Solutions Architect).\n\n"
        f"IMPORTANT : Rédiger l'ensemble des livrables de carrière en langue [{language}]."
    )

    expected_output = (
        f"Un dossier de valorisation de carrière et personal branding en Markdown rédigé en [{language}], comprenant :\n"
        f"1. Fiche de mise à jour du CV (Bullet points d'impact et mots-clés de compétences certifiables)\n"
        f"2. Brouillon de post LinkedIn prêt à l'emploi (Format REX professionnel avec accroche, enseignements clés et hashtags)\n"
        f"3. Matrice de correspondance vers les certifications professionnelles cibles."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )

def create_convergence_reconciliation_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche de convergence et réconciliation d'architecture (Phase E TOGAF / Consensus Gate).
    Le Lead Manager arbitre les divergences entre Solution Architect, Challenger et FinOps,
    et produit le document de décision consolidé et sans contradiction.
    """
    description = (
        f"En tant que Lead Architecture Manager et autorité d'arbitrage de l'Architecture Review Board (ARB) :\n"
        f"1. Analyser l'ensemble des livrables produits par la brigade : le DAT préliminaire, l'audit critique du Challenger (Red Team), "
        f"l'avis d'homologation du CISO, la conception hexagonale du Crafter et l'étude TCO du FinOps.\n"
        f"2. Identifier formellement toutes les contradictions ou divergences d'arbitrage (ex: Multi-Cloud vs Mono-Cloud, technologies divergentes).\n"
        f"3. Rendre une décision d'arbitrage souveraine, argumentée et définitive pour le comité de direction.\n"
        f"4. Mettre à jour et consolider les choix structurants pour garantir la parfaite cohérence du dossier cible sans contradiction interne.\n\n"
        f"IMPORTANT : Rédiger votre synthèse de convergence en langue [{language}]."
    )

    expected_output = (
        f"Un document de décision d'arbitrage et de convergence d'architecture en Markdown rédigé en [{language}], comprenant :\n"
        f"1. Synthèse exécutive de la décision finale (Décision formelle de l'ARB)\n"
        f"2. Tableau des divergences identifiées et arbitrages rendus (Option initiale vs Critique Red Team vs Décision finale)\n"
        f"3. Architecture cible consolidée et réconciliée (Sans aucune contradiction interne)\n"
        f"4. Trajectoire de transition et plan d'action immédiat."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )

def create_executive_restitution_task(agent: Agent, context_tasks: list, language: str) -> Task:
    """
    Crée la tâche de restitution exécutive d'architecture devant l'Architecture Review Board (ARB) et le C-Level.
    Produit la synthèse stratégique comparant AS-IS et TO-BE, extrait les KPIs majeurs et prépare
    le storyboard pour l'exportation du Slide Deck HTML 16:9 au standard Haute Couture Bento Grid.
    """
    description = (
        f"En tant que Lead Solution Architect et responsable de la restitution devant l'Architecture Review Board (ARB) et le C-Level :\n"
        f"1. Analyser l'ensemble des livrables de l'étude (DAT, décision d'arbitrage ARB, audit CISO, brique Craft et analyse FinOps).\n"
        f"2. Formaliser un storyboard exécutif de restitution d'architecture à fort impact visuel :\n"
        f"   - Une accroche exécutive stratégique (Executive Statement).\n"
        f"   - Les 6 indicateurs de performance clés (KPIs chiffrés : ROI, SLA, latence, TCO, etc.).\n"
        f"   - La comparaison directe AS-IS vs TO-BE intégrant les schémas d'architecture Mermaid de l'étude.\n"
        f"   - Les 4 arbitrages et décisions structurantes validés lors de la convergence.\n"
        f"   - Un plan d'action d'exécution et de trajectoire (Sprints / PI Planning SAFe).\n"
        f"3. Rédiger le script de discours oral minuté pour le présentateur (avec version en Français et en Anglais).\n"
        f"Ce storyboard servira de socle pour générer le Slide Deck HTML 16:9 interactif au standard Haute Couture Bento Grid.\n\n"
        f"IMPORTANT : Rédiger votre storyboard de restitution exécutive en langue [{language}]."
    )

    expected_output = (
        f"Un dossier de restitution exécutive d'architecture en Markdown rédigé en [{language}], comprenant :\n"
        f"1. Executive Statement & Vision stratégique de transformation\n"
        f"2. Les 6 KPIs d'architecture et de valeur business (Format clé: valeur)\n"
        f"3. Synthèse comparative AS-IS vs TO-BE avec schémas Mermaid intégrés\n"
        f"4. Matrice des 4 décisions d'arbitrage majeures (ADRs) et compromis associés\n"
        f"5. Plan de trajectoire de delivery et ROI FinOps\n"
        f"6. Script de discours oral minuté pour la soutenance ARB."
    )

    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent,
        context=context_tasks
    )





