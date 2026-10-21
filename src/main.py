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
    # Brigade TOGAF / SAFe / CISO
    create_manager_agent,
    create_solution_architect_agent,
    create_challenger_agent,
    create_ciso_agent,
    create_crafter_agent,
    create_safe_enabler_agent,
    create_finops_agent,
    # Comité d'Architecture Virtuel des 5 Maîtres & Green/FinOps
    create_martin_fowler_agent,
    create_uncle_bob_agent,
    create_werner_vogels_agent,
    create_alistair_cockburn_agent,
    create_sam_newman_agent,
    create_greenops_finops_agent,
    create_architecture_quality_gate_agent,
    # Conseil des 5 Grands Orateurs & Éloquence TEDx
    create_hassan_ii_agent,
    create_steve_jobs_agent,
    create_martin_luther_king_agent,
    create_winston_churchill_agent,
    create_barack_obama_agent,
    create_stage_director_agent,
    create_eloquence_judge_agent
)
from src.tasks import (
    # Tâches Brigade TOGAF / SAFe / CISO
    create_preliminary_design_task,
    create_challenge_task,
    create_security_audit_task,
    create_software_crafting_task,
    create_safe_delivery_task,
    create_finops_task,
    create_convergence_reconciliation_task,
    # Tâches Comité d'Architecture Virtuel & Quality Gate
    create_initial_architecture_draft_task,
    create_fowler_review_task,
    create_uncle_bob_review_task,
    create_vogels_review_task,
    create_cockburn_review_task,
    create_newman_review_task,
    create_greenops_finops_review_task,
    create_quality_gate_evaluation_task,
    create_committee_synthesis_task,
    # Tâches Conseil des Grands Orateurs & Éloquence TEDx
    create_orator_context_analysis_task,
    create_roundtable_propositions_task,
    create_stage_director_synthesis_task,
    create_eloquence_judge_evaluation_task,
    create_final_speech_pack_task
)
from src.tools import (
    ArchitectureRAGManager,
    KnowledgeSearchTool,
    GitPublisher,
    JiraBacklogExporter,
    DiagramExporter,
    LogAnalyzer,
    CareerExporter,
    ExecutivePresentationExporter,
    ExecutivePrompterExporter
)
from src.orchestration import AgenticLoopController
from crewai import Crew, Process


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Multi-Agent Architecture Platform (AAP) — Plateforme Multi-Agents d'Architecture & d'Éloquence"
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["togaf", "committee", "speech", "full"],
        default="togaf",
        help="Mode d'exécution : 'togaf' (dossier DAT complet), 'committee' (Comité des 5 Maîtres & boucle qualité), "
             "'speech' (Conseil des 5 Orateurs & TEDx), 'full' (chaîne intégrale)."
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
        help="Dossier d'étude optionnel pour enregistrer l'intégralité du pack documentaire d'architecture"
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=85.0,
        help="Score minimal sur 100 exigé par le Quality Gate avant validation (défaut : 85.0)"
    )
    parser.add_argument(
        "--max-loops",
        type=int,
        default=4,
        help="Nombre maximal d'itérations de rebouclage correctif (coupe-circuit, défaut : 4)"
    )
    parser.add_argument(
        "--audience",
        type=str,
        default="Comité de Direction & Jury d'Architecture",
        help="Audience cible pour le mode speech (défaut : 'Comité de Direction & Jury d'Architecture')"
    )
    parser.add_argument(
        "--publish-git",
        action="store_true",
        help="Déclencher la publication Git sécurisée avec porte bloquante Human-in-the-Loop [O/N]"
    )
    parser.add_argument(
        "--log-file",
        type=str,
        default=None,
        help="Chemin optionnel pour sauvegarder l'intégralité des traces et échanges des agents (par défaut dans logs/)"
    )
    return parser.parse_args()


def run_virtual_committee_pipeline(input_content: str, worker_llm, manager_llm, language: str,
                                   min_score: float, max_loops: int, log_file_path: str, study_dir: Path = None):
    """Exécute le Comité d'Architecture Virtuel des 5 Maîtres avec boucle d'auto-correction."""
    print("\n🏛️ ==================================================================")
    print("  COMMENCEMENT DU COMITÉ D'ARCHITECTURE VIRTUEL DES 5 MAÎTRES")
    print("==================================================================")
    print(f"• Participants : Fowler, Uncle Bob, Vogels, Cockburn, Newman, GreenOps/FinOps")
    print(f"• Arbitrage    : Juge Qualité (Seuil cible : {min_score}/100, Max itérations : {max_loops})")

    controller = AgenticLoopController(min_score=min_score, max_iterations=max_loops)

    # Agents du Comité
    fowler = create_martin_fowler_agent(worker_llm)
    uncle_bob = create_uncle_bob_agent(worker_llm)
    vogels = create_werner_vogels_agent(worker_llm)
    cockburn = create_alistair_cockburn_agent(worker_llm)
    newman = create_sam_newman_agent(worker_llm)
    greenops = create_greenops_finops_agent(worker_llm)
    judge = create_architecture_quality_gate_agent(manager_llm)

    current_prompt = input_content
    iteration = 1
    final_result = None

    while True:
        print(f"\n🔄 --- Cycle d'Audit {iteration}/{max_loops} en cours ---")

        draft_task = create_initial_architecture_draft_task(fowler, current_prompt, language)
        fowler_task = create_fowler_review_task(fowler, [draft_task], language)
        uncle_bob_task = create_uncle_bob_review_task(uncle_bob, [draft_task], language)
        vogels_task = create_vogels_review_task(vogels, [draft_task], language)
        cockburn_task = create_cockburn_review_task(cockburn, [draft_task], language)
        newman_task = create_newman_review_task(newman, [draft_task], language)
        greenops_task = create_greenops_finops_review_task(greenops, [draft_task], language)

        reviews_context = [draft_task, fowler_task, uncle_bob_task, vogels_task, cockburn_task, newman_task, greenops_task]
        eval_task = create_quality_gate_evaluation_task(judge, reviews_context, min_score=min_score, language=language)

        crew = Crew(
            agents=[fowler, uncle_bob, vogels, cockburn, newman, greenops, judge],
            tasks=[draft_task, fowler_task, uncle_bob_task, vogels_task, cockburn_task, newman_task, greenops_task, eval_task],
            process=Process.sequential,
            verbose=True
        )

        res = crew.kickoff()
        eval_output = str(eval_task.output.raw) if hasattr(eval_task, "output") and eval_task.output else str(res)
        evaluation = controller.parse_evaluation(eval_output, iteration=iteration)

        print(f"📊 {evaluation.summary}")

        if not controller.should_continue(evaluation):
            print(f"✅ Seuil atteint ou limite d'itérations atteinte. Compilation du rapport final...")
            # Tâche de synthèse finale
            synthesis_task = create_committee_synthesis_task(fowler, reviews_context + [eval_task], language)
            synthesis_crew = Crew(agents=[fowler], tasks=[synthesis_task], process=Process.sequential, verbose=True)
            final_result = synthesis_crew.kickoff()
            break

        # Construction du prompt réinjecté avec les critiques ciblées
        feedback = controller.build_feedback_prompt(evaluation, target_domain="Comité des 5 Maîtres")
        current_prompt = f"{input_content}\n\n{feedback}"
        iteration += 1

    summary_table = controller.generate_loop_summary_markdown()
    full_report = f"{summary_table}\n\n---\n\n{final_result}"

    if study_dir:
        report_file = study_dir / "00_RAPPORT_COMITE_ARCHITECTURE_VIRTUEL.md"
        report_file.write_text(full_report, encoding="utf-8")
        print(f"💾 Rapport officiel du Comité d'Architecture enregistré : {report_file}")

    return full_report


def run_orator_speech_pipeline(input_content: str, worker_llm, manager_llm, language: str,
                              min_score: float, max_loops: int, audience: str, log_file_path: str, study_dir: Path = None):
    """Exécute le Conseil des 5 Grands Orateurs avec bouclage jusqu'à l'excellence rhétorique."""
    print("\n🎙️ ==================================================================")
    print("  CONSEIL D'ADMINISTRATION DES GRANDS ORATEURS & TEDX PROMPTER")
    print("==================================================================")
    print(f"• Orateurs  : Hassan II, Steve Jobs, MLK Jr., Winston Churchill, Barack Obama")
    print(f"• Direction : Metteur en Scène & Juge d'Éloquence (Seuil : {min_score}/100)")

    controller = AgenticLoopController(min_score=min_score, max_iterations=max_loops)

    hassan = create_hassan_ii_agent(worker_llm)
    jobs = create_steve_jobs_agent(worker_llm)
    mlk = create_martin_luther_king_agent(worker_llm)
    churchill = create_winston_churchill_agent(worker_llm)
    obama = create_barack_obama_agent(worker_llm)
    director = create_stage_director_agent(manager_llm)
    judge = create_eloquence_judge_agent(manager_llm)

    current_prompt = input_content
    iteration = 1
    final_pack = None

    while True:
        print(f"\n🔄 --- Cycle Rhétorique {iteration}/{max_loops} en cours ---")

        context_task = create_orator_context_analysis_task(director, current_prompt, audience=audience, language=language)
        roundtable_task = create_roundtable_propositions_task(director, [context_task], language=language)
        synthesis_task = create_stage_director_synthesis_task(director, [context_task, roundtable_task], language=language)
        eval_task = create_eloquence_judge_evaluation_task(judge, [synthesis_task], min_score=min_score, language=language)

        crew = Crew(
            agents=[director, hassan, jobs, mlk, churchill, obama, judge],
            tasks=[context_task, roundtable_task, synthesis_task, eval_task],
            process=Process.sequential,
            verbose=True
        )

        res = crew.kickoff()
        eval_output = str(eval_task.output.raw) if hasattr(eval_task, "output") and eval_task.output else str(res)
        evaluation = controller.parse_evaluation(eval_output, iteration=iteration)

        print(f"📊 {evaluation.summary}")

        if not controller.should_continue(evaluation):
            print(f"✅ Niveau d'éloquence validé. Génération du Pack de Prise de Parole...")
            pack_task = create_final_speech_pack_task(director, [synthesis_task, eval_task], language=language)
            pack_crew = Crew(agents=[director], tasks=[pack_task], process=Process.sequential, verbose=True)
            final_pack = pack_crew.kickoff()
            break

        feedback = controller.build_feedback_prompt(evaluation, target_domain="Conseil d'Éloquence")
        current_prompt = f"{input_content}\n\n{feedback}"
        iteration += 1

    summary_table = controller.generate_loop_summary_markdown()
    full_speech_report = f"{summary_table}\n\n---\n\n{final_pack}"

    if study_dir:
        prompter_exporter = ExecutivePrompterExporter()
        pack_text = str(final_pack)

        md_prompter_file = study_dir / "02_SCRIPT_PROMPTER_TEDX.md"
        html_prompter_file = study_dir / "02_PROMPTER_INTERACTIF_TEDX.html"

        prompter_exporter.export_prompter_markdown(
            title="Soutenance & Restitution Exécutive",
            script_text=pack_text,
            output_file=md_prompter_file
        )
        prompter_exporter.export_interactive_html(
            title="Soutenance & Restitution Exécutive",
            script_text=pack_text,
            output_file=html_prompter_file
        )
        print(f"📜 Script Prompter Markdown généré : {md_prompter_file}")
        print(f"📽️ Téléprompteur interactif Single-Slide généré : {html_prompter_file}")

    return full_speech_report


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
    print(f"• Mode sélectionné         : [{args.mode.upper()}]")
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

    study_path = Path(args.study_dir) if args.study_dir else None
    if study_path:
        study_path.mkdir(parents=True, exist_ok=True)
        cahier_file = study_path / "00_CAHIER_DES_CHARGES_INPUT.md"
        cahier_file.write_text(input_content, encoding="utf-8")

    logs_dir = ROOT_DIR / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = args.log_file if args.log_file else str(logs_dir / f"execution_{timestamp}.log")

    # Aiguillage selon le mode choisi
    if args.mode == "committee":
        result = run_virtual_committee_pipeline(
            input_content=input_content,
            worker_llm=worker_llm,
            manager_llm=manager_llm,
            language=args.language,
            min_score=args.min_score,
            max_loops=args.max_loops,
            log_file_path=log_file_path,
            study_dir=study_path
        )
    elif args.mode == "speech":
        result = run_orator_speech_pipeline(
            input_content=input_content,
            worker_llm=worker_llm,
            manager_llm=manager_llm,
            language=args.language,
            min_score=args.min_score,
            max_loops=args.max_loops,
            audience=args.audience,
            log_file_path=log_file_path,
            study_dir=study_path
        )
    elif args.mode == "full":
        print("\n🌐 Exécution de la chaîne intégrale (Comité des 5 Maîtres -> Conseil des 5 Orateurs)...")
        committee_result = run_virtual_committee_pipeline(
            input_content=input_content,
            worker_llm=worker_llm,
            manager_llm=manager_llm,
            language=args.language,
            min_score=args.min_score,
            max_loops=args.max_loops,
            log_file_path=log_file_path,
            study_dir=study_path
        )
        speech_result = run_orator_speech_pipeline(
            input_content=committee_result,
            worker_llm=worker_llm,
            manager_llm=manager_llm,
            language=args.language,
            min_score=args.min_score,
            max_loops=args.max_loops,
            audience=args.audience,
            log_file_path=log_file_path,
            study_dir=study_path
        )
        result = f"# PACK INTÉGRAL ARCHITECTURE & ÉLOQUENCE\n\n{committee_result}\n\n---\n\n{speech_result}"
    else:
        # Mode par défaut : 'togaf'
        # 2.bis Initialisation de la base vectorielle RAG locale (Brique 3)
        try:
            rag_manager = ArchitectureRAGManager()
            chunks_indexed = rag_manager.ingest_knowledge()
            knowledge_tool = KnowledgeSearchTool(rag_manager=rag_manager)
            print(f"📚 Base de connaissances RAG initialisée ({chunks_indexed} fragments doctrinaux indexés dans ChromaDB)")
            agent_tools = [knowledge_tool]
        except Exception as e:
            print(f"⚠️ Avertissement RAG : exécution sans RAG ({e})")
            agent_tools = []

        # 3. Création de la brigade complète d'agents
        manager = create_manager_agent(manager_llm)
        solution_architect = create_solution_architect_agent(worker_llm, tools=agent_tools)
        challenger = create_challenger_agent(worker_llm)
        ciso = create_ciso_agent(worker_llm, tools=agent_tools)
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

        convergence_task = create_convergence_reconciliation_task(
            agent=manager,
            context_tasks=[design_task, challenge_task, finops_task],
            language=args.language
        )

        # 6. Assemblage de la Crew
        crew = Crew(
            agents=[solution_architect, challenger, ciso, crafter, safe_enabler, finops, manager],
            tasks=[design_task, challenge_task, security_task, crafting_task, delivery_task, finops_task, convergence_task],
            process=Process.sequential,
            manager_agent=manager,
            output_log_file=log_file_path,
            verbose=True
        )

        print("\n▶️ Lancement de l'orchestration multi-agents d'architecture TOGAF...")
        try:
            result = crew.kickoff()
        except Exception as e:
            print(f"\n❌ Erreur lors de l'exécution de la Crew : {e}")
            sys.exit(1)

        # Sauvegarde automatique du pack documentaire complet (1 fichier par agent)
        if study_path:
            deliverables_mapping = [
                ("00_DECISION_ARBITRAGE_ET_SYNTHESE_CONVERGENCE.md", convergence_task),
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

            # Export automatique du backlog Jira au format CSV
            delivery_output = str(delivery_task.output.raw) if hasattr(delivery_task, "output") and delivery_task.output else ""
            if delivery_output:
                jira_csv_file = study_path / "backlog_jira.csv"
                count = JiraBacklogExporter().export_to_csv(delivery_output, jira_csv_file)
                print(f"📊 Export Jira CSV ({count} User Stories, délimiteur ;) généré : {jira_csv_file}")

            # Observabilité Meta-Agent
            actual_log_path = Path(log_file_path) if Path(log_file_path).exists() else Path(str(log_file_path) + ".txt")
            if actual_log_path.exists():
                health_report = LogAnalyzer().generate_health_report(actual_log_path)
                health_file = study_path / "08_RAPPORT_OBSERVABILITE_ET_SANTE_SYSTEME.md"
                health_file.write_text(health_report, encoding="utf-8")
                print(f"🩺 Rapport d'observabilité Meta-Agent généré : {health_file}")

            # Valorisation Carrière & LinkedIn REX
            career_exporter = CareerExporter()
            study_title = input_path.stem.replace("_", " ").title() if input_path.is_file() else "Modernisation Architecture Multi-Cloud & IA"
            key_patterns = [
                "Topologie Multi-Cloud Hybride (AWS EKS/MSK + Azure OpenAI privé C2 MASSIF)",
                "Agents IA Autonomes en Production avec garde-fous (Prompt Injection, PII masqué, HITL > 2 000 €)",
                "Architecture Hexagonale découplée (Ports & Adapters) & FinOps TCO optimisé"
            ]
            linkedin_rex = career_exporter.generate_linkedin_post(
                author_name="Widad SAGHIR (Lead Architect)",
                study_title=study_title,
                key_results=key_patterns,
                certifications_alignment=["TOGAF 10 Certified", "SAFe 6 for Architects", "Cloud Solutions Architect"]
            )
            cv_bullets = career_exporter.generate_cv_bullet_points(study_title, key_patterns)
            career_report = f"# 🚀 VALORISATION DE CARRIÈRE & PERSONAL BRANDING\n\n## 📝 Entrées pour Mise à Jour du CV\n" + "\n".join(cv_bullets) + f"\n\n---\n\n## 📱 Brouillon de Post LinkedIn (REX Prêt à Publier)\n\n```markdown\n{linkedin_rex}\n```\n"
            career_file = study_path / "09_VALORISATION_CARRIERE_ET_POST_LINKEDIN_REX.md"
            career_file.write_text(career_report, encoding="utf-8")
            print(f"📈 Dossier de valorisation de carrière généré : {career_file}")

            # Schémas d'architecture (Draw.io, PlantUML, Mermaid)
            diagrams_dir = study_path / "diagrams"
            diagrams_dir.mkdir(parents=True, exist_ok=True)
            design_output = str(design_task.output.raw) if hasattr(design_task, "output") and design_task.output else ""
            DiagramExporter().extract_and_export_from_markdown(
                markdown_text=design_output,
                output_dir=diagrams_dir,
                base_name="architecture_cible_omniclaim"
            )
            print(f"🖼️ Schémas d'architecture extraits dans : {diagrams_dir}")

            # Restitution Exécutive ARB & Slide Deck 16:9 Bento Grid
            presentation_exporter = ExecutivePresentationExporter()
            presentation_slides_file = study_path / "10_SYNTHESE_EXECUTIVE_RESTITUTION_SLIDES.html"
            diagrams_map = {}
            for mmd_file in diagrams_dir.glob("*.mmd"):
                if "as_is" in mmd_file.stem.lower():
                    diagrams_map["AS-IS"] = mmd_file.read_text(encoding="utf-8")
                elif "l2_container" in mmd_file.stem.lower() or "cible" in mmd_file.stem.lower():
                    diagrams_map["TO-BE"] = mmd_file.read_text(encoding="utf-8")

            convergence_output = str(convergence_task.output.raw) if hasattr(convergence_task, "output") and convergence_task.output else ""
            restitution_source = convergence_output or design_output or input_content
            presentation_exporter.export_presentation(
                study_title=study_title,
                study_content=restitution_source,
                diagrams=diagrams_map,
                output_file=presentation_slides_file
            )
            print(f"📽️ Slide Deck Exécutif 16:9 Bento Grid généré : {presentation_slides_file}")

    print("\n==================================================================")
    print("  ✅ LIVRABLES GÉNÉRÉS AVEC SUCCÈS")
    print("==================================================================")
    print(result)

    # Sauvegarde du livrable unique optionnel
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(result))
        print(f"\n💾 Livrable de synthèse enregistré avec succès dans : {output_path}")

    # Publication Git sécurisée avec porte bloquante Human-in-the-Loop
    if args.publish_git:
        publisher = GitPublisher()
        content_to_scan = str(result)
        leak_warnings = publisher.scan_content_for_secrets(content_to_scan)

        if leak_warnings:
            print("\n🚨 SCAN ANTI-SECRETS : Publication bloquée ! Secrets potentiels détectés :")
            for w in leak_warnings:
                print(f"   • {w}")
        else:
            approved = publisher.request_hitl_approval(
                "Publication du pack d'architecture vers le dépôt distant Git sur la branche active"
            )
            if approved:
                publisher.push_to_remote(repo_dir=ROOT_DIR)
            else:
                print("ℹ️ Publication Git annulée par l'architecte en chef.")


if __name__ == "__main__":
    main()
