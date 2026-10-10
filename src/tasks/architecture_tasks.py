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
