from crewai import Task, Agent

def create_preliminary_design_task(agent: Agent, user_input: str, language: str) -> Task:
    """
    Crée la tâche d'analyse préliminaire d'architecture.
    La langue demandée est strictement injectée pour garantir la restitution dans la langue cible.
    """
    description = (
        f"Analyser l'expression de besoin ou les notes de cadrage suivantes :\n"
        f"\"\"\"\n{user_input}\n\"\"\"\n\n"
        f"Proposer une note de cadrage d'architecture technique préliminaire structurée.\n"
        f"IMPORTANT : Vous devez impérativement rédiger l'intégralité de votre réponse en langue [{language}]."
    )

    expected_output = (
        f"Un document Markdown complet rédigé impérativement en [{language}], structuré comme suit :\n"
        f"1. Synthèse du besoin & Vision d'architecture (Phase A TOGAF)\n"
        f"2. Exigences clés & Besoins Non-Fonctionnels (Scalabilité, Résilience, Sécurité)\n"
        f"3. Propositions de scénarios d'infrastructure (Cloud, Hybride ou On-Premise)\n"
        f"4. Recommandation argumentée du Solution Architect avec justification des choix techniques\n"
        f"5. Risques préliminaires identifiés & points d'attention pour les comités d'architecture."
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




