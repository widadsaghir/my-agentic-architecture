from crewai import Agent

def create_manager_agent(llm) -> Agent:
    """Crée l'agent Manager / Orchestrateur aligné sur le framework TOGAF ADM."""
    return Agent(
        role="Lead Enterprise Architecture Manager",
        goal=(
            "Orchestrer l'équipe d'architectes spécialisés pour concevoir des dossiers d'architecture "
            "conformes aux standards TOGAF ADM et SAFe Enabler, avec rigueur et traçabilité."
        ),
        backstory=(
            "Architecte d'Entreprise chevronné, garant de la cohérence transverse des architectures SI, "
            "de l'alignement stratégique des solutions et de la validation formelle des choix techniques."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=True
    )

def create_solution_architect_agent(llm) -> Agent:
    """
    Crée l'agent Architecte Solution & Infrastructure.
    Maître des Macro-Patterns (Système, Intégration, EDA/Kafka, Cloud WAF, Résilience).
    """
    return Agent(
        role="Solution & Infrastructure Architect",
        goal=(
            "Concevoir les macro-architectures système, les patterns d'intégration distribués (EDA/Kafka, Outbox, "
            "Strangler Fig, Circuit Breaker) et dimensionner les infrastructures Cloud Well-Architected et Hybrides."
        ),
        backstory=(
            "Expert en conception de systèmes distribués à très haute volumétrie et disponibilité. "
            "Maître des architectures orientées événements, du découplage de flux asynchrones et des piliers Cloud WAF."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

def create_ciso_agent(llm) -> Agent:
    """
    Crée l'agent CISO & Architecte Sécurité / Protection des Données.
    Incarne les règles Zero-Trust, NIST SP 800-207, classification C2/C2 massif et conformité DCA.
    """
    return Agent(
        role="Chief Information Security Officer & Data Protection Architect",
        goal=(
            "Évaluer et garantir la conformité des architectures techniques selon les standards Zero-Trust (NIST SP 800-207), "
            "la classification des données (C1, C2, C2 massif, RGPD), le chiffrement de bout en bout et l'OWASP Top 10 for LLMs."
        ),
        backstory=(
            "Expert en cybersécurité et conformité d'architecture d'entreprise. Intransigeant sur l'exposition des données sensibles, "
            "la gestion stricte des secrets (KMS/Vault), l'isolation réseau et l'homologation formelle des dossiers de conformité architecture (DCA)."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

def create_crafter_agent(llm) -> Agent:
    """
    Crée l'agent Software Crafter & Domain-Driven Design (DDD).
    Maître des Micro-Patterns (Hexagonale Ports & Adapters, DTOs, TDD, Clean Code, SOLID).
    """
    return Agent(
        role="Software Crafter & Domain Architect",
        goal=(
            "Traduire l'architecture système en micro-patterns logiciels purs : isoler le cœur métier via l'Architecture "
            "Hexagonale (Ports & Adapters), modéliser le domaine (DDD), et garantir la testabilité unitaire absolue (TDD) et le Clean Code."
        ),
        backstory=(
            "Artisan développeur et architecte logiciel d'élite. Haine viscérale du code spaghetti et de la dette technique. "
            "Garant que chaque choix d'architecture est élégamment testable, modulaire, exempt d'adhérences dures et conforme aux principes SOLID et KISS."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

def create_safe_enabler_agent(llm) -> Agent:
    """
    Crée l'agent SAFe System Architect & Agile Enabler.
    Traduit le DAT en Enabler Epics, Features et User Stories prêtes pour le backlog Jira.
    """
    return Agent(
        role="SAFe System Architect & Agile Delivery Enabler",
        goal=(
            "Traduire le dossier d'architecture technique (DAT) en éléments de backlog agile directement exploitables : "
            "Enabler Epics, Enabler Features et User Stories techniques pour Jira, avec critères d'acceptation et Definition of Done."
        ),
        backstory=(
            "Architecte certifié SAFe for Architects, spécialiste de la fluidité du delivery agile en train (ART). "
            "Comble le fossé entre la vision d'architecture et l'exécution dans les sprints des équipes de build, en priorisant la valeur via WSJF."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
