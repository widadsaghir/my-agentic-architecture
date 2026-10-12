import sys
import argparse
from pathlib import Path

# Assurer que le répertoire racine est bien dans le PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config import get_config
from src.agents import (
    create_manager_agent,
    create_solution_architect_agent,
    create_challenger_agent,
    create_ciso_agent,
    create_crafter_agent,
    create_safe_enabler_agent
)
from src.tasks import (
    create_preliminary_design_task,
    create_challenge_task,
    create_security_audit_task,
    create_software_crafting_task,
    create_safe_delivery_task
)
from crewai import Crew, Process

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Multi-Agent Architecture Platform (AAP) — Système Multi-Agents TOGAF ADM"
    )
    parser.add_argument(
        "--language",
        type=str,
        default="English",
        help="Langue cible pour les livrables d'architecture (ex : French, English, Spanish)"
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Notes de cadrage brutes, expression de besoin ou fichier d'entrée"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Chemin optionnel pour enregistrer le livrable Markdown produit"
    )
    return parser.parse_args()

def main():
    args = parse_arguments()

    print("==================================================================")
    print("  🚀 Multi-Agent Architecture Platform (AAP) — Initialisation")
    print("==================================================================")
    print(f"• Langue cible configurée : [{args.language}]")
    print(f"• Requête d'entrée       : {args.input[:100]}..." if len(args.input) > 100 else f"• Requête d'entrée       : {args.input}")

    # 1. Chargement de la configuration et des clés Gemini
    try:
        config = get_config()
    except Exception as e:
        print(f"\n❌ Erreur de configuration : {e}")
        sys.exit(1)

    print(f"• Modèle Worker (Spécialistes) : {config.worker_model}")
    print(f"• Modèle Manager (Orchestrateur): {config.manager_model}")

    # 2. Instanciation des modèles LLM Gemini
    try:
        worker_llm = config.get_worker_llm()
        manager_llm = config.get_manager_llm()
    except Exception as e:
        print(f"\n❌ Erreur lors de l'initialisation des modèles Gemini : {e}")
        sys.exit(1)

    # 3. Création de la brigade complète d'agents
    manager = create_manager_agent(manager_llm)
    solution_architect = create_solution_architect_agent(worker_llm)
    challenger = create_challenger_agent(worker_llm)
    ciso = create_ciso_agent(worker_llm)
    crafter = create_crafter_agent(worker_llm)
    safe_enabler = create_safe_enabler_agent(worker_llm)

    # 4. Création des tâches enchaînées (Conception -> Challenge -> CISO -> Craft -> SAFe)
    design_task = create_preliminary_design_task(
        agent=solution_architect,
        user_input=args.input,
        language=args.language
    )

    challenge_task = create_challenge_task(
        agent=challenger,
        context_tasks=[design_task],
        language=args.language
    )

    security_task = create_security_audit_task(
        agent=ciso,
        context_tasks=[design_task, challenge_task],
        language=args.language
    )

    crafting_task = create_software_crafting_task(
        agent=crafter,
        context_tasks=[design_task, challenge_task, security_task],
        language=args.language
    )

    delivery_task = create_safe_delivery_task(
        agent=safe_enabler,
        context_tasks=[design_task, crafting_task, security_task],
        language=args.language
    )

    # 5. Assemblage de la Crew
    crew = Crew(
        agents=[solution_architect, challenger, ciso, crafter, safe_enabler],
        tasks=[design_task, challenge_task, security_task, crafting_task, delivery_task],
        process=Process.sequential,
        manager_agent=manager,
        verbose=True
    )

    print("\n▶️ Lancement de l'orchestration multi-agents d'architecture...")
    print("   [1/5] Solution Architect (Macro-Patterns & Vision)")
    print("   [2/5] Challenger / Red Team (Traque SPOF & Anti-Sur-Ingénierie)")
    print("   [3/5] CISO & Data Protection (Zero-Trust, C2 & Homologation DCA)")
    print("   [4/5] Software Crafter (Architecture Hexagonale, DDD & TDD)")
    print("   [5/5] SAFe Agile Enabler (Backlog Jira, Enablers & DoD)")
    try:
        result = crew.kickoff()
    except Exception as e:
        print(f"\n❌ Erreur lors de l'exécution de la Crew : {e}")
        sys.exit(1)

    print("\n==================================================================")
    print("  ✅ DOSSIER D'ARCHITECTURE & AVIS CISO GÉNÉRÉS")
    print("==================================================================")
    print(result)

    # Sauvegarde optionnelle
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(result))
        print(f"\n💾 Livrable enregistré avec succès dans : {output_path}")

if __name__ == "__main__":
    main()
