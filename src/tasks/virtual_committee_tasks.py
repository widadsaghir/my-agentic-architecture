"""
Tâches du Comité d'Architecture Virtuel d'Élite & Évaluateur Qualité.
Orchestre l'audit croisé des 5 grands architectes, l'évaluation GreenOps/FinOps,
le scoring par Quality Gate et la synthèse finale de consensus.
"""

from typing import List, Optional
from crewai import Agent, Task


def create_initial_architecture_draft_task(agent: Agent, user_input: str, language: str) -> Task:
    """
    Crée la tâche de proposition d'architecture initiale (Premier jet soumis au Comité).
    """
    description = (
        f"En tant qu'architecte producteur, concevoir et structurer une proposition d'architecture complète "
        f"répondant à l'expression de besoin suivante :\n"
        f"\"\"\"\n{user_input}\n\"\"\"\n\n"
        f"Le dossier doit couvrir :\n"
        f"1. La vision globale et les objectifs fonctionnels et non-fonctionnels.\n"
        f"2. Le découpage applicatif (composants, modules ou microservices).\n"
        f"3. La gestion des données (stockage, synchronisation, cohérence).\n"
        f"4. Les choix d'intégration (synchrone vs asynchrone, API, brokers).\n"
        f"5. L'infrastructure et la stratégie de résilience Cloud.\n\n"
        f"IMPORTANT : Rédiger cette proposition technique en [{language}]."
    )
    expected_output = (
        f"Un dossier de proposition d'architecture initialement structuré en [{language}], "
        f"détaillant le découpage système, les choix de flux, la persistance et l'infrastructure."
    )
    return Task(description=description, expected_output=expected_output, agent=agent)


def create_fowler_review_task(agent: Agent, context_tasks: List[Task], language: str) -> Task:
    """Audit par Martin Fowler : Patterns d'entreprise, Évolutivité, Compromis et Refactoring."""
    description = (
        f"En tant que Martin Fowler (ThoughtWorks, P of EAA, Refactoring, Software Architecture: The Hard Parts) :\n"
        f"Examiner en profondeur la proposition d'architecture soumise dans les tâches précédentes.\n\n"
        f"Tes axes d'investigation obligatoires :\n"
        f"1. 🔄 Évolutivité du système : L'architecture peut-elle évoluer au cours des 5 prochaines années sans refonte totale ?\n"
        f"2. ⚖️ Compromis d'architecture distribuée (Trade-offs) : Identifier les fausses bonnes idées, la sur-ingénierie prématurée et les coûts cachés.\n"
        f"3. 🧩 Patterns d'entreprise recommandés : Quels patterns (Outbox, Strangler Fig, Event Sourcing, Circuit Breaker) sont nécessaires ou mal appliqués ?\n"
        f"4. 🛠️ Trajectoire de refactoring : Comment découpler les composants rigides pas à pas ?\n\n"
        f"Rédiger ton avis tranché, sans langue de bois, en langue [{language}]."
    )
    expected_output = (
        f"L'avis d'audit officiel de Martin Fowler en [{language}] analysant l'évolutivité, "
        f"les compromis distribués, les patterns d'entreprise et les axes de refactoring."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_uncle_bob_review_task(agent: Agent, context_tasks: List[Task], language: str) -> Task:
    """Audit par Robert C. Martin (Uncle Bob) : SOLID, Clean Architecture et étanchéité métier."""
    description = (
        f"En tant que Robert C. Martin / Uncle Bob (Clean Architecture, Clean Code) :\n"
        f"Auditer sans concession l'architecture sous le prisme de la Clean Architecture et du Craftsmanship.\n\n"
        f"Tes axes d'investigation obligatoires :\n"
        f"1. 🧱 Respect des principes SOLID : Détecter les violations (Single Responsibility, Dependency Inversion, etc.).\n"
        f"2. 🛡️ Indépendance du domaine métier : Le cœur de métier est-il contaminé par des dépendances aux frameworks, ORM ou protocoles d'entrée ?\n"
        f"3. 🎯 L'architecture 'crie'-t-elle le métier (Screaming Architecture) plutôt que les outils techniques ?\n"
        f"4. 🧪 Testabilité unitaire : Les entités et cas d'usage peuvent-ils être testés en microsecondes sans conteneur externe ?\n\n"
        f"Rédiger tes exigences d'artisan logiciel en langue [{language}]."
    )
    expected_output = (
        f"Le rapport d'audit d'Uncle Bob en [{language}] évaluant la conformité SOLID, "
        f"l'isolation absolue du domaine et la pureté de la Clean Architecture."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_vogels_review_task(agent: Agent, context_tasks: List[Task], language: str) -> Task:
    """Audit par Werner Vogels : Résilience, Design for Failure, Cloud Native et Anti-SPOF."""
    description = (
        f"En tant que Werner Vogels (CTO Amazon, AWS Well-Architected Framework) :\n"
        f"Challenger le système avec la doctrine 'Everything fails all the time'.\n\n"
        f"Tes axes d'investigation obligatoires :\n"
        f"1. 💥 Traque absolue des SPOF (Single Points of Failure) : Base de données unique, broker non répliqué, service bloquant.\n"
        f"2. ⚡ Découplage asynchrone & Élasticité : Remplacer tout appel synchrone HTTP bloquant par des événements ou des queues tampon.\n"
        f"3. 🛡️ Résilience opérationnelle : Présence de Circuit Breakers, Bulkheads, retries avec exponential backoff et jitter, et idempotence.\n"
        f"4. 🌐 Disponibilité Multi-AZ / Multi-Région : RTO et RPO garantis en cas de crash d'un centre de données.\n\n"
        f"Rédiger ton verdict d'infrastructure en langue [{language}]."
    )
    expected_output = (
        f"L'avis d'audit de Werner Vogels en [{language}] sur la tolérance aux pannes, "
        f"l'éradication des SPOF et la résilience Cloud asynchrone."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_cockburn_review_task(agent: Agent, context_tasks: List[Task], language: str) -> Task:
    """Audit par Alistair Cockburn : Architecture Hexagonale, Ports & Adaptateurs."""
    description = (
        f"En tant qu'Alistair Cockburn (Créateur de l'Architecture Hexagonale - Ports & Adapters) :\n"
        f"Vérifier la stricte conformité hexagonale du système.\n\n"
        f"Tes axes d'investigation obligatoires :\n"
        f"1. ⬡ Définition des Ports Primaires (Driving / Inbound) : Les contrats d'entrée (API, Batch, CLI) sont-ils des interfaces découplées ?\n"
        f"2. ⬡ Définition des Ports Secondaires (Driven / Outbound) : Les dépendances de persistance, de messagerie et de services tiers sont-elles isolées par des interfaces SPI ?\n"
        f"3. 🔌 Adaptateurs interchangeables : Peut-on remplacer une base de données ou un broker sans toucher à une seule ligne du domaine ?\n"
        f"4. 💎 Testabilité en isolation : Preuve que les tests unitaires s'exécutent avec des adaptateurs bouchons en mémoire.\n\n"
        f"Rédiger tes conclusions hexagonales en langue [{language}]."
    )
    expected_output = (
        f"L'audit d'Alistair Cockburn en [{language}] analysant la frontière hexagonale, "
        f"la typologie des ports et l'interchangeabilité des adaptateurs."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_newman_review_task(agent: Agent, context_tasks: List[Task], language: str) -> Task:
    """Audit par Sam Newman : Décomposition des monolithes, Bounded Contexts et Loi de Conway."""
    description = (
        f"En tant que Sam Newman (Building Microservices, Monolith to Microservices) :\n"
        f"Évaluer la granularité des services et les frontières organisationnelles.\n\n"
        f"Tes axes d'investigation obligatoires :\n"
        f"1. 🔪 Granularité et frontières des Bounded Contexts (DDD) : Services trop gros (monolithes cachés) ou trop fins (micro-nanoservices ingérables) ?\n"
        f"2. 🗄️ Gestion des données distribuées : Éradiquer tout partage de base de données entre services (Base-per-Service stricte).\n"
        f"3. 👥 Alignement avec la Loi de Conway : L'architecture colle-t-elle à la topologie des équipes de delivery ?\n"
        f"4. 🌉 Patterns de décomposition progressive : Strangler Fig, Outbox transactionnel, Event Choreography vs Orchestration.\n\n"
        f"Rédiger ton analyse de décomposition en langue [{language}]."
    )
    expected_output = (
        f"L'audit de Sam Newman en [{language}] validant les frontières de microservices, "
        f"la séparation des bases et la trajectoire d'évolution sans monolithe distribué."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_greenops_finops_review_task(agent: Agent, context_tasks: List[Task], language: str) -> Task:
    """Audit GreenOps & FinOps : Empreinte carbone, frugalité numérique et modélisation TCO."""
    description = (
        f"En tant qu'Architecte GreenOps & FinOps :\n"
        f"Évaluer rigoureusement le coût environnemental et financier de l'architecture.\n\n"
        f"Tes axes d'investigation obligatoires :\n"
        f"1. 🌱 Éco-conception & GreenOps : Estimation de l'intensité carbone, optimisation des cycles vCPU/RAM, extinction des environnements de dev/test hors heures ouvrées.\n"
        f"2. 💰 Modélisation FinOps & TCO : Comparatif des coûts Capex vs Opex, calcul des économies via réservations (Compute Savings Plans) et dimensionnement au juste besoin (Right-Sizing).\n"
        f"3. ⚡ Architectures frugales : Gains apportés par les processeurs ARM (Graviton), les architectures Serverless à la demande et la compression des transferts de données.\n"
        f"4. 📊 Matrice d'efficience : Coût estimé par million de transactions et ratio d'émissions gCO2eq.\n\n"
        f"Rédiger ton bilan écologique et financier en langue [{language}]."
    )
    expected_output = (
        f"Le rapport d'évaluation GreenOps & FinOps en [{language}], chiffrant les gisements d'optimisation "
        f"carbone et les leviers d'économies de coûts (TCO, Right-Sizing, Sobriété)."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_quality_gate_evaluation_task(
    agent: Agent,
    context_tasks: List[Task],
    min_score: float = 85.0,
    language: str = "French"
) -> Task:
    """
    Tâche du Juge Qualité : Consolide les 6 audits, calcule la note sur 100 et émet le verdict binaire.
    """
    description = (
        f"En tant que Magistrat Suprême et Juge Qualité du Comité d'Architecture :\n"
        f"Auditer l'ensemble des revues techniques des 5 Maîtres (Fowler, Uncle Bob, Vogels, Cockburn, Newman) "
        f"et du spécialiste GreenOps/FinOps figurant dans le contexte.\n\n"
        f"TU DOIS IMPÉRATIVEMENT RESPECTER LE FORMAT STRUCTURE SUIVANT POUR PERMETTRE LE PARSING DÉTERMINISTE :\n\n"
        f"# Rapport d'Audit & Verdict Qualité du Comité d'Architecture\n\n"
        f"### 📊 Synthèse Chiffrée & Grille d'Évaluation :\n"
        f"- Score Global : <NOTE_ENTIERE_SUR_100>/100\n"
        f"- SOLID & Clean Architecture : <NOTE>/100\n"
        f"- Résilience & Anti-SPOF : <NOTE>/100\n"
        f"- Hexagonale & Ports : <NOTE>/100\n"
        f"- Microservices & Bounded Contexts : <NOTE>/100\n"
        f"- GreenOps & FinOps : <NOTE>/100\n"
        f"- Compromis & Évolutivité : <NOTE>/100\n\n"
        f"### ⚖️ Verdict du Comité :\n"
        f"Statut : [VALIDÉ (Score >= {min_score}) OU À REPRENDRE (Score < {min_score})]\n\n"
        f"### ⚠️ Gaps & Faiblesses critiques à corriger :\n"
        f"(Lister précisément 3 à 7 points concrets, obligatoires si le score est inférieur à {min_score})\n"
        f"- Point 1 : ...\n"
        f"- Point 2 : ...\n\n"
        f"Rédiger ce verdict en langue [{language}]."
    )
    expected_output = (
        f"La grille d'évaluation qualité en [{language}] contenant obligatoirement la ligne '- Score Global : XX/100', "
        f"les notes par critères, le statut formel et la liste numérotée des gaps critiques."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_committee_synthesis_task(agent: Agent, context_tasks: List[Task], language: str) -> Task:
    """
    Compiles the final official Virtual Committee Report.
    """
    description = (
        f"En tant que Secrétaire Général et Modérateur du Comité d'Architecture :\n"
        f"Rédiger le Grand Rapport Consolidé du Comité d'Architecture Virtuel d'Élite.\n\n"
        f"Le livrable final doit être un document de prestige en Markdown comprenant les 4 chapitres majeurs :\n\n"
        f"1. 🏛️ L'ÉVALUATION CRITIQUE DÉTAILLÉE DU COMITÉ :\n"
        f"   - L'avis officiel et sans concession de Martin Fowler (Compromis & Évolutivité).\n"
        f"   - L'avis de Robert C. Martin / Uncle Bob (SOLID, Clean Architecture, Purity).\n"
        f"   - L'avis de Werner Vogels (Design for Failure, SPOF, Résilience Cloud).\n"
        f"   - L'avis d'Alistair Cockburn (Hexagonal Ports & Adapters, Testabilité).\n"
        f"   - L'avis de Sam Newman (Microservices, Découpage de monolithes, Conway).\n"
        f"   - L'audit GreenOps & FinOps (Sobriété carbone, TCO, Économies).\n\n"
        f"2. 🗺️ L'ARCHITECTURE CIBLE RECOMMANDÉE PAR CONSENSUS :\n"
        f"   - Description détaillée de l'architecture validée par les 5 Maîtres.\n"
        f"   - Schéma d'architecture Mermaid intégrant tous les correctifs exigés.\n\n"
        f"3. ⚖️ L'ANALYSE DES COMPROMIS (TRADE-OFFS) :\n"
        f"   - Justification de chaque choix technique majeur et de ce qui a été délibérément rejeté (KISS, YAGNI).\n\n"
        f"4. 🚀 LE PLAN DE MIGRATION & DE TRAJECTOIRE :\n"
        f"   - Étapes concrètes de bascule progressive (Strangler Fig pattern, outbox, tests de recette).\n\n"
        f"Rédiger l'intégralité de ce rapport de référence en langue [{language}]."
    )
    expected_output = (
        f"Le Rapport Officiel du Comité d'Architecture Virtuel en Markdown rédigé en [{language}], "
        f"structuré en 4 parties : Évaluations des Maîtres, Architecture Cible Recommandée avec schéma Mermaid, "
        f"Analyse des Compromis et Plan de Migration détaillé."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)
