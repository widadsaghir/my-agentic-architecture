#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Démonstration Interactive pour Enregistrement Vidéo
Ce script simule à l'écran l'exécution dynamique de la Brigade d'Architecture (AAP)
avec une mise en scène esthétique, des pauses minutées et des couleurs ANSI.

Comment l'utiliser pour fabriquer votre vidéo en 5 minutes :
1. Ouvrez votre terminal (PowerShell ou Windows Terminal) en plein écran (1920x1080).
2. Lancez l'enregistreur d'écran Windows (raccourci : Touche Windows + Alt + R ou Touche Windows + Maj + R).
3. Exécutez : python docs/presentation/enregistrer_demo_interactive.py
4. Laissez défiler le script à l'écran tout en récitant le script oral synchronisé !
"""

import sys
import time

# Codes couleurs ANSI pour rendu professionnel dans le terminal
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"

BG_BLUE = "\033[44m\033[97m"
BG_RED = "\033[41m\033[97m"
BG_GREEN = "\033[42m\033[97m"

def slow_print(text, delay=0.02, end="\n"):
    """Effet de frappe au clavier réaliste."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def header(text):
    print(f"\n{BOLD}{CYAN}{'='*80}{RESET}")
    print(f"{BOLD}{WHITE}  {text}{RESET}")
    print(f"{BOLD}{CYAN}{'='*80}{RESET}\n")

def agent_badge(name, color, role):
    return f"{BOLD}{color}[{name.upper()}]{RESET} {DIM}({role}){RESET}"

def pause(seconds=2.0):
    time.sleep(seconds)

def main():
    print("\n" * 2)
    header("MULTI-AGENT ARCHITECTURE PLATFORM (AAP) — DÉMONSTRATION OFFICIELLE")
    
    print(f"{DIM}Initialisation de l'environnement d'architecture...{RESET}")
    pause(1.2)
    print(f"{GREEN}✓ Framework d'architecture : TOGAF 10 ADM (Phases A à H){RESET}")
    print(f"{GREEN}✓ Cadre de livraison agile  : SAFe 6 for Architects (Enablers & DoD){RESET}")
    print(f"{GREEN}✓ Norme de sécurité        : Zero-Trust NIST SP 800-207 & Classification C2{RESET}")
    print(f"{GREEN}✓ Base vectorielle locale   : ChromaDB RAG (Doctrine d'entreprise indexée){RESET}")
    pause(1.5)

    # 1. Commande tapée
    print(f"\n{BOLD}{WHITE}PS C:\\Architecture\\my-agentic-architecture> {RESET}", end="")
    slow_print("python src/main.py --study-dir docs/etudes/migration_ssas_cloud --language fr", delay=0.035)
    pause(1.0)

    # 2. Bannière de démarrage
    print(f"\n{BOLD}{BG_BLUE}  BRIGADE MULTI-AGENTS ACTIVE — 9 PROFILS SPÉCIALISÉS  {RESET}")
    print(f"{CYAN}Étude ciblée :{RESET} Migration Cloud & Modernisation Socle Décisionnel NovaAnalytics")
    print(f"{CYAN}Doctrine RAG :{RESET} 5 référentiels chargés (Zero-Trust, Hexagonale, WAF, SAFe, Anti-dérive)")
    pause(2.0)

    # 3. Phase A : Lead Architect
    header("PHASE A : CADRAGE & VISION STRATÉGIQUE (TOGAF 10)")
    print(f"{agent_badge('Lead Architecture Manager', CYAN, 'Orchestrateur TOGAF')}")
    print("  ↳ Analyse du cahier des charges : Monolithe décisionnel 4 To, RPO < 1h, RTO < 4h.")
    print("  ↳ Objectifs fixés : Réduction du TCO de 30%, haute disponibilité multi-AZ, gouvernance C2.")
    print(f"  {DIM}[Validation du mandat de cadrage - Répartition des tâches]{RESET}")
    pause(2.5)

    # 4. Phase B/C/D : Macro-Architecture
    header("PHASES B, C & D : ARCHITECTURE MÉTIER, DONNÉES & INFRASTRUCTURE")
    print(f"{agent_badge('Solution Architect', BLUE, 'Worker Macro & Cloud WAF')}")
    print("  ↳ Proposition initiale :")
    print("    • Migration vers cluster Kubernetes managé et microservices de requêtage.")
    print("    • Ingestion temps réel via cluster Apache Kafka distribué (3 nœuds).")
    print("    • Base relationnelle PostgreSQL managée avec réplication synchrone.")
    pause(2.5)

    # 5. Le Débat Contradictoire (Clé de la démo)
    header("AUDIT CONTRADICTOIRE & ANALYSE CRITIQUE (RED TEAM)")
    print(f"{BOLD}{BG_RED}  CHALLENGER / RED TEAM EN ACTION  {RESET}")
    print(f"{agent_badge('Challenger Red Team', RED, 'Anti-SPOF & KISS Inspector')}")
    print(f"  {BOLD}{RED}⚠ ALERTE SUR-INGÉNIERIE DÉTECTÉE :{RESET}")
    print("    1. Le besoin métier documenté indique des flux batchs périodiques (sync à J+1).")
    print("    2. Déployer un cluster Kafka 24/7 introduit un coût inutile de 850 €/mois et un SPOF opérationnel.")
    print("    3. Recommandation contradictoire : Privilégier un pipeline de données serverless (KISS / YAGNI).")
    pause(3.0)

    print(f"\n{agent_badge('CISO & Data Protection', MAGENTA, 'Gouvernance SSI & C2')}")
    print(f"  {BOLD}{MAGENTA}🔒 EXIGENCE SSI COMPLÉMENTAIRE :{RESET}")
    print("    • Classification des flux : C2 (Données sensibles d'exploitation).")
    print("    • Injonction de doctrine : Chiffrement obligatoire au repos avec clés CMK.")
    print("    • Cloisonnement réseau : Exclusion formelle de toute IP publique (Private Link strict).")
    pause(2.5)

    print(f"\n{agent_badge('Lead Architecture Manager', CYAN, 'Arbitrage Définitif')}")
    print(f"  {BOLD}{GREEN}✓ ARBITRAGE RETENU :{RESET} Remplacement de Kafka par un pipeline managé événementiel,")
    print("  isolation réseau 100% privée, chiffrement CMK validé.")
    pause(2.0)

    # 6. Micro-architecture et Craftsmanship
    header("CONCEPTION LOGICIELLE & EXCELLENCE TECHNIQUE")
    print(f"{agent_badge('Software Crafter', GREEN, 'Hexagonale & Domain-Driven Design')}")
    print("  ↳ Découpage du domaine : 2 Bounded Contexts étanches (Ingestion, Restitution).")
    print("  ↳ Isolation du Core Domain : Ports & Adapters stricts, 0 dépendance cloud dans le modèle.")
    print("  ↳ Testabilité garantie : 100% de la logique métier testable unitairement sans conteneur.")
    pause(2.5)

    # 7. Delivery SAFe & FinOps
    header("LIVRAISON AGILE & MODÉLISATION ÉCONOMIQUE (FINOPS)")
    print(f"{agent_badge('FinOps & TCO Specialist', YELLOW, 'Calculs Économiques')}")
    print("  ↳ Coût On-Premise actuel : 142 000 € / an (matériel, licences, maintenance).")
    print("  ↳ Coût Cloud Cible calculé : 94 500 € / an (incluant instances réservées et stockage froid).")
    print(f"  ↳ {BOLD}{GREEN}Économie nette démontrée : 33.4% par an.{RESET}")
    pause(2.0)

    print(f"\n{agent_badge('SAFe System Architect', WHITE, 'Agile Delivery Enabler')}")
    print("  ↳ Découpage du DAT : 1 Enabler Epic, 3 Features, 12 User Stories techniques.")
    print("  ↳ Definition of Done (DoD) formalisée avec critères d'acceptation Gherkin.")
    pause(2.5)

    # 8. Production des Artéfacts Déterministes
    header("GÉNÉRATION DÉTERMINISTE DES ARTÉFACTS (0 TOKEN)")
    artifacts = [
        ("00_RESUME_EXECUTIF_ET_DECISION.md", "Synthèse pour le Comité de Direction"),
        ("01_DOSSIER_ARCHITECTURE_TECHNIQUE_DAT.md", "DAT complet de 35 pages (TOGAF B-C-D)"),
        ("02_RAPPORT_AUDIT_CONTRADICTOIRE.md", "Rapport d'audit de la Red Team"),
        ("03_AVIS_HOMOLOGATION_SECURITE_DCA.md", "Dossier de conformité Zero-Trust SSI"),
        ("04_CONCEPTION_HEXAGONALE_ET_DDD.md", "Modèle de domaine et interfaces de ports"),
        ("05_STRATEGIE_MIGRATION_ET_FINOPS_TCO.md", "Modèle financier et plan de bascule"),
        ("06_BACKLOG_LIVRAISON_SAFE_JIRA.md", "Spécification détaillée des User Stories"),
        ("backlog_jira.csv", "Export Excel FR prêt à l'import Jira (délimiteur ;)"),
        ("diagrams/architecture_to_be.drawio", "Schéma vectoriel éditable Draw.io natif"),
        ("diagrams/architecture_to_be.puml", "Schéma PlantUML C4 Container"),
        ("diagrams/architecture_to_be.mmd", "Schéma Mermaid Living Documentation")
    ]
    for filename, desc in artifacts:
        print(f"  {GREEN}✔ Fichier généré :{RESET} {BOLD}{filename:<42}{RESET} {DIM}→ {desc}{RESET}")
        time.sleep(0.18)
    pause(2.0)

    # 9. Sas de Sécurité GitPublisher HITL
    header("GOUVERNANCE DE SOUVERAINETÉ (HUMAN-IN-THE-LOOP)")
    print(f"{agent_badge('GitPublisher Tool', CYAN, 'Adaptateur d Infrastructure')}")
    print(f"  {DIM}[Scan de sécurité anti-fuite de secrets en cours...]{RESET}")
    pause(1.0)
    print(f"  {GREEN}✓ Scan terminé : 0 secret, 0 clé d'API, 0 IP privée détectée.{RESET}")
    print(f"\n{BOLD}{YELLOW}[HITL CONFIRMATION] Souhaitez-vous valider et pousser ces livrables sur Git ? [O/N] : {RESET}", end="")
    slow_print("O", delay=0.1)
    pause(1.0)
    print(f"{BOLD}{GREEN}✓ Validation humaine enregistrée. Commit créé : 'feat(archi): pack etude ssas cloud togaf'.{RESET}")
    pause(2.0)

    # 10. Conclusion & Tests
    header("CONTRÔLE DE NON-DÉRIVE PAR TESTS AUTOMATISÉS (PYTEST)")
    print(f"{BOLD}{WHITE}PS C:\\Architecture\\my-agentic-architecture> {RESET}", end="")
    slow_print("pytest tests/unit/ -q", delay=0.03)
    pause(0.8)
    print(f"{GREEN}................................................{RESET}")
    print(f"{BOLD}{GREEN}48 passed in 1.84s (100% Architectural Fitness Functions Validated){RESET}\n")

    print(f"{BOLD}{CYAN}{'='*80}{RESET}")
    print(f"{BOLD}{WHITE}  DÉMONSTRATION COMPLÈTE TERMINÉE AVEC SUCCÈS — PRÊT POUR LA SESSION Q/R{RESET}")
    print(f"{BOLD}{CYAN}{'='*80}{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nArrêt de la démonstration.")
