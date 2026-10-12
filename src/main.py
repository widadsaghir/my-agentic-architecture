import sys
import argparse
from datetime import datetime
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
    create_safe_enabler_agent,
    create_finops_agent
)
from src.tasks import (
    create_preliminary_design_task,
    create_challenge_task,
    create_security_audit_task,
    create_software_crafting_task,
    create_safe_delivery_task,
    create_finops_task
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
    parser.add_argument(
        "--study-dir",
        type=str,
        default=None,
        help="Dossier d'étude optionnel pour enregistrer l'intégralité du pack documentaire d'architecture (un fichier par agent)"
    )
    parser.add_argument(
        "--log-file",
        type=str,
        default=None,
        help="Chemin optionnel pour sauvegarder l'intégralité des traces et échanges des agents (par défaut dans logs/)"
    )
    return parser.parse_args()

def main():
    args = parse_arguments()

    # 0. Détection et lecture automatique si --input est un fichier
    input_content = args.input
    input_path = Path(args.input)
    if input_path.is_file():
        try:
            with open(input_path, "r", encoding="utf-8") as f:
                input_content = f.read()
            print(f"📄 Fichier de cadrage détecté et chargé : {input_path}")
        except Exception as e:
            print(f"⚠️ Erreur lors de la lecture du fichier {input_path}, utilisation du texte brut : {e}")

    print("==================================================================")
    print("  🚀 Multi-Agent Architecture Platform (AAP) — Initialisation")
    print("==================================================================")
    print(f"• Langue cible configurée : [{args.language}]")
    print(f"• Requête d'entrée       : {input_content[:100]}..." if len(input_content) > 100 else f"• Requête d'entrée       : {input_content}")

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
    finops = create_finops_agent(worker_llm)

    # 4. Création des tâches enchaînées (Conception -> Challenge -> CISO -> Craft -> SAFe -> FinOps)
    design_task = create_preliminary_design_task(
        agent=solution_architect,
        user_input=input_content,
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

    finops_task = create_finops_task(
        agent=finops,
        context_tasks=[design_task, challenge_task, delivery_task],
        language=args.language
    )

    # 5. Configuration des logs d'exécution (Base d'audit pour le Meta-Agent)
    logs_dir = ROOT_DIR / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = args.log_file if args.log_file else str(logs_dir / f"execution_{timestamp}.log")

    # 6. Assemblage de la Crew
    crew = Crew(
        agents=[solution_architect, challenger, ciso, crafter, safe_enabler, finops],
        tasks=[design_task, challenge_task, security_task, crafting_task, delivery_task, finops_task],
        process=Process.sequential,
        manager_agent=manager,
        output_log_file=log_file_path,
        verbose=True
    )

    print("\n▶️ Lancement de l'orchestration multi-agents d'architecture...")
    print("   [1/6] Solution Architect (Macro-Patterns & Vision)")
    print("   [2/6] Challenger / Red Team (Traque SPOF & Anti-Sur-Ingénierie)")
    print("   [3/6] CISO & Data Protection (Zero-Trust, C2 & Homologation DCA)")
    print("   [4/6] Software Crafter (Architecture Hexagonale, DDD & TDD)")
    print("   [5/6] SAFe Agile Enabler (Backlog Jira, Enablers & DoD)")
    print("   [6/6] Migration & FinOps / TCO (Comparatif des 4 Pistes, Coûts Min/Max)")
    print(f"   [Trace] Enregistrement en direct des échanges dans : {log_file_path}")
    try:
        result = crew.kickoff()
    except Exception as e:
        print(f"\n❌ Erreur lors de l'exécution de la Crew : {e}")
        sys.exit(1)

    print("\n==================================================================")
    print("  ✅ DOSSIER D'ARCHITECTURE & ÉVALUATIONS GÉNÉRÉS")
    print("==================================================================")
    print(result)

    # Sauvegarde du livrable unique optionnel
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(result))
        print(f"\n💾 Livrable de synthèse enregistré avec succès dans : {output_path}")

    # Sauvegarde automatique du pack documentaire complet (1 fichier par agent)
    if args.study_dir:
        study_path = Path(args.study_dir)
        study_path.mkdir(parents=True, exist_ok=True)

        deliverables_mapping = [
            ("01_DOSSIER_ARCHITECTURE_TECHNIQUE_DAT.md", design_task),
            ("02_RAPPORT_AUDIT_CONTRADICTOIRE.md", challenge_task),
            ("03_AVIS_HOMOLOGATION_SECURITE_DCA.md", security_task),
            ("04_CONCEPTION_HEXAGONALE_ET_DDD.md", crafting_task),
            ("05_STRATEGIE_MIGRATION_ET_FINOPS_TCO.md", finops_task),
            ("06_BACKLOG_LIVRAISON_SAFE_JIRA.md", delivery_task)
        ]

        for filename, task_obj in deliverables_mapping:
            target_file = study_path / filename
            output_content = str(task_obj.output.raw) if hasattr(task_obj, "output") and task_obj.output else ""
            if output_content:
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(output_content)

        print(f"📦 Pack d'architecture complet (6 dossiers d'experts) généré dans : {study_path}")

    print(f"📜 Journal complet des échanges et raisonnements sauvegardé dans : {log_file_path}")

if __name__ == "__main__":
    main()
