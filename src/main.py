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
    create_finops_task,
    create_convergence_reconciliation_task
)
from src.tools import (
    ArchitectureRAGManager,
    KnowledgeSearchTool,
    GitPublisher,
    JiraBacklogExporter,
    DiagramExporter,
    LogAnalyzer,
    CareerExporter
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

    # 5. Configuration des logs d'exécution (Base d'audit pour le Meta-Agent)
    logs_dir = ROOT_DIR / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = args.log_file if args.log_file else str(logs_dir / f"execution_{timestamp}.log")

    # 6. Assemblage de la Crew
    crew = Crew(
        agents=[solution_architect, challenger, ciso, crafter, safe_enabler, finops, manager],
        tasks=[design_task, challenge_task, security_task, crafting_task, delivery_task, finops_task, convergence_task],
        process=Process.sequential,
        manager_agent=manager,
        output_log_file=log_file_path,
        verbose=True
    )

    print("\n▶️ Lancement de l'orchestration multi-agents d'architecture...")
    print("   [1/7] Solution Architect (Macro-Patterns & Vision)")
    print("   [2/7] Challenger / Red Team (Traque SPOF & Anti-Sur-Ingénierie)")
    print("   [3/7] CISO & Data Protection (Zero-Trust, C2 & Homologation DCA)")
    print("   [4/7] Software Crafter (Architecture Hexagonale, DDD & TDD)")
    print("   [5/7] SAFe Agile Enabler (Backlog Jira, Enablers & DoD)")
    print("   [6/7] Migration & FinOps / TCO (Comparatif des 4 Pistes, Coûts Min/Max)")
    print("   [7/7] Lead Architecture Manager (Consensus Gate & Synthèse de Convergence)")
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

        # Export automatique du backlog Jira au format CSV (Excel Français ;)
        delivery_output = str(delivery_task.output.raw) if hasattr(delivery_task, "output") and delivery_task.output else ""
        if delivery_output:
            jira_csv_file = study_path / "backlog_jira.csv"
            count = JiraBacklogExporter().export_to_csv(delivery_output, jira_csv_file)
            print(f"📊 Export Jira CSV ({count} User Stories, délimiteur ;) généré : {jira_csv_file}")

        # Observabilité Meta-Agent (Brique 5.1)
        actual_log_path = Path(log_file_path) if Path(log_file_path).exists() else Path(str(log_file_path) + ".txt")
        if actual_log_path.exists():
            health_report = LogAnalyzer().generate_health_report(actual_log_path)
            health_file = study_path / "08_RAPPORT_OBSERVABILITE_ET_SANTE_SYSTEME.md"
            health_file.write_text(health_report, encoding="utf-8")
            print(f"🩺 Rapport d'observabilité Meta-Agent généré : {health_file}")

        # Valorisation Carrière & LinkedIn REX (Brique 5.2)
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

        # Génération conjointe des schémas d'architecture (Draw.io, PlantUML, Mermaid)
        diagrams_dir = study_path / "diagrams"
        diagrams_dir.mkdir(parents=True, exist_ok=True)
        nodes = [
            {"id": "Client", "label": "Assuré / Courtier", "type": "actor"},
            {"id": "AWS_Ingestion", "label": "AWS MSK & EKS Services", "type": "service"},
            {"id": "Azure_Cognitive", "label": "Azure OpenAI C2 Enclave", "type": "service"},
            {"id": "Core_Database", "label": "PostgreSQL Aurora Multi-Cloud", "type": "database"},
            {"id": "HITL_Backoffice", "label": "Portail Gestionnaire HITL > 2000€", "type": "service"}
        ]
        links = [
            {"source": "Client", "target": "AWS_Ingestion", "label": "Déclaration sinistre (HTTPS)"},
            {"source": "AWS_Ingestion", "target": "Azure_Cognitive", "label": "Direct Connect / ExpressRoute"},
            {"source": "Azure_Cognitive", "target": "HITL_Backoffice", "label": "Suspension si > 2000 € ou fraude >= 0.15"},
            {"source": "AWS_Ingestion", "target": "Core_Database", "label": "Persistance & Règlements"}
        ]
        DiagramExporter().export_diagram_bundle(
            title=f"Architecture Cible — {study_title}",
            nodes=nodes,
            links=links,
            output_dir=diagrams_dir,
            base_name="architecture_cible_omniclaim"
        )
        print(f"🖼️ Schémas d'architecture (Draw.io, PlantUML, Mermaid) générés dans : {diagrams_dir}")

        print(f"📦 Pack d'architecture complet (Livrables, Schémas, Observabilité & Carrière) généré dans : {study_path}")

    print(f"📜 Journal complet des échanges et raisonnements sauvegardé dans : {log_file_path}")

    # 7. Publication Git sécurisée avec porte bloquante Human-in-the-Loop (Brique 4.3)
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
