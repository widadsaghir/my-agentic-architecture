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
