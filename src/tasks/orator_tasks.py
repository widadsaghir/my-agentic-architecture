"""
Tâches du Conseil d'Administration Virtuel d'Éloquence & Restitution TEDx.
Orchestre l'analyse de contexte, la table ronde des 5 grands orateurs, la fusion par le Metteur en Scène,
la notation impitoyable par le Juge d'Éloquence et le pack final prompter avec Q&A.
"""

from typing import List, Optional
from crewai import Agent, Task


def create_orator_context_analysis_task(
    agent: Agent,
    user_input: str,
    audience: str = "Dirigeants C-Level & Jury d'Architecture",
    format_type: str = "Keynote Exécutive & Pitch TEDx de 15 minutes",
    language: str = "French"
) -> Task:
    """
    Analyse le sujet, l'audience cible, les enjeux psychologiques et le format de la prise de parole.
    """
    description = (
        f"En tant qu'Analyste de Contexte & Stratège en Rhétorique :\n"
        f"Analyser en profondeur le sujet d'architecture ou la thématique soumise ci-dessous :\n"
        f"\"\"\"\n{user_input}\n\"\"\"\n\n"
        f"Paramètres de la prise de parole :\n"
        f"- 🎯 Audience cible : {audience}\n"
        f"- ⏱️ Format et contrainte : {format_type}\n\n"
        f"Tes livrables d'analyse :\n"
        f"1. L'enjeu central : Pourquoi cette intervention est cruciale et quel est le risque de l'échec ?\n"
        f"2. La psychologie de l'auditoire : Leurs doutes, leurs craintes, leurs biais et ce qui les fera basculer.\n"
        f"3. L'idée motrice unique (The Big Idea) : Le message unique qui doit rester gravé dans leur esprit.\n"
        f"4. Le fil conducteur narratif : L'opposition entre le statu quo et la vision nouvelle.\n\n"
        f"Rédiger cette note de cadrage en langue [{language}]."
    )
    expected_output = (
        f"Une note de cadrage oratoire en [{language}] définissant l'enjeu stratégique, "
        f"la psychologie de l'auditoire, l'idée motrice et l'arc narratif."
    )
    return Task(description=description, expected_output=expected_output, agent=agent)


def create_roundtable_propositions_task(
    agent: Agent,
    context_tasks: List[Task],
    language: str = "French"
) -> Task:
    """
    Table Ronde des 5 Orateurs Légendaires : Chaque orateur injecte son ADN signature.
    """
    description = (
        f"En tant que Secrétaire de la Table Ronde des Grands Orateurs :\n"
        f"Recueillir et confronter les propositions d'accroches, de formules et d'angles d'attaque "
        f"des 5 orateurs légendaires sur la base du cadrage établi :\n\n"
        f"1. 👑 L'apport d'Hassan II : La métaphore philosophique noble, la hauteur de vue souveraine et la formule de solennité.\n"
        f"2. 💡 L'apport de Steve Jobs : L'accroche choc, la dramatisation du calvaire actuel, la règle de trois et le 'One More Thing'.\n"
        f"3. 🕊️ L'apport de Martin Luther King Jr. : La formule anaphorique rythmée, l'appel aux valeurs universelles et la promesse d'avenir.\n"
        f"4. ⚔️ L'apport de Winston Churchill : Les verbes d'action au présent, la formule martiale qui réveille et la lucidité courageuse.\n"
        f"5. 🤝 L'apport de Barack Obama : L'anecdote personnelle qui touche, le pont empathique et les silences respiratoires rassembleurs.\n\n"
        f"Structurer cette table ronde divergente en langue [{language}]."
    )
    expected_output = (
        f"Le compte-rendu de la table ronde en [{language}], contenant les contributions spécifiques, "
        f"angles et formules signatures de chacun des 5 maîtres orateurs."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_stage_director_synthesis_task(
    agent: Agent,
    context_tasks: List[Task],
    language: str = "French"
) -> Task:
    """
    Le Metteur en Scène fusionne les propositions en un draft unifié annoté pour la scène.
    """
    description = (
        f"En tant qu'Executive Stage Director & Metteur en Scène :\n"
        f"Fusionner les propositions des 5 orateurs pour composer le discours intégral parfait.\n\n"
        f"Consignes impératives de composition scénique :\n"
        f"1. Rédiger le texte mot à mot, fluide et prêt à être prononcé.\n"
        f"2. Intégrer les annotations scéniques entre crochets pour guider le locuteur :\n"
        f"   - `[PAUSE 2s]` (silence stratégique pour ancrer une idée forte),\n"
        f"   - `[BREATHE]` (reprise de souffle calme),\n"
        f"   - `[SOURIRE]` (connexion humaine),\n"
        f"   - `[REGARD CAMÉRA]` ou `[REGARD AUDIENCE]` (balayage visuel),\n"
        f"   - `[↘ INTONATION DESCENDANTE]` (point ferme pour asseoir l'autorité vocale).\n"
        f"3. Rythmer le déroulé selon les 4 actes TEDx : L'Accroche magnétique, Le Calvaire du problème, "
        f"La Révélation de l'architecture, et L'Appel vibrant à l'action.\n\n"
        f"Rédiger ce script scénarisé intégral en langue [{language}]."
    )
    expected_output = (
        f"Le script intégral du discours en [{language}], entièrement annoté des repères scéniques "
        f"([PAUSE 2s], [BREATHE], [SOURIRE], [↘ INTONATION DESCENDANTE]) et structuré en 4 actes."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_eloquence_judge_evaluation_task(
    agent: Agent,
    context_tasks: List[Task],
    min_score: float = 85.0,
    language: str = "French"
) -> Task:
    """
    Tâche du Juge d'Éloquence : Évalue le discours sur 5 critères stricts, calcule la note sur 100
    et émet le verdict (VALIDÉ / À REPRENDRE).
    """
    description = (
        f"En tant que Juge Suprême d'Éloquence & Gardien de l'Impact Rhétorique :\n"
        f"Auditer avec une exigence absolue le discours scénarisé produit dans la tâche précédente.\n\n"
        f"TU DOIS IMPÉRATIVEMENT RESPECTER LE FORMAT STRUCTURE SUIVANT POUR PERMETTRE LE PARSING DÉTERMINISTE :\n\n"
        f"# Rapport d'Audit & Verdict d'Éloquence\n\n"
        f"### 📊 Synthèse Chiffrée & Grille Rhétorique :\n"
        f"- Score Global : <NOTE_ENTIERE_SUR_100>/100\n"
        f"- Clarté & Simplicité (Jobs) : <NOTE>/100\n"
        f"- Émotion & Pathos (MLK) : <NOTE>/100\n"
        f"- Rythme & Scénographie (Obama) : <NOTE>/100\n"
        f"- Vocabulaire & Élévation (Hassan II) : <NOTE>/100\n"
        f"- Force de Conviction & Concision (Churchill) : <NOTE>/100\n\n"
        f"### ⚖️ Verdict du Juge :\n"
        f"Statut : [VALIDÉ (Score >= {min_score}) OU À REPRENDRE (Score < {min_score})]\n\n"
        f"### ⚠️ Gaps & Faiblesses critiques à corriger :\n"
        f"(Lister précisément 3 à 5 exigences d'amélioration formelles si le score est inférieur à {min_score})\n"
        f"- Point 1 : ...\n"
        f"- Point 2 : ...\n\n"
        f"Rédiger ce verdict en langue [{language}]."
    )
    expected_output = (
        f"La grille d'évaluation d'éloquence en [{language}] contenant obligatoirement la ligne '- Score Global : XX/100', "
        f"les notes par critères, le statut formel et la liste numérotée des points à perfectionner."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)


def create_final_speech_pack_task(
    agent: Agent,
    context_tasks: List[Task],
    language: str = "French"
) -> Task:
    """
    Produit le Pack Complet du Discours d'Éloquence : Script intégral, Annotations prompter,
    Matrice d'arguments clés et Anticipation Q&A.
    """
    description = (
        f"En tant que Metteur en Scène et Coach Exécutif :\n"
        f"Compiler et formaliser le Pack Complet de Prise de Parole d'Élite.\n\n"
        f"Le livrable final doit comprendre les 4 volets indissociables suivants :\n\n"
        f"1. 📜 LE SCRIPT TEXTUEL INTÉGRAL ANNOTÉ (LE PROMPTER) :\n"
        f"   - Texte mot à mot prêt à être lu au prompter, minuté et annoté des repères scéniques ([PAUSE 2s], [BREATHE], [SOURIRE], [↘ INTONATION DESCENDANTE]).\n\n"
        f"2. 🎭 LES DIRECTIVES SCÉNIQUES & NOTES DU COACH :\n"
        f"   - Conseils de posture physique, d'ancrage au sol, de contact visuel et de gestion du stress (protocole sophrologique 4-4-6).\n\n"
        f"3. 🧠 LA MATRICE DES ARGUMENTS CLÉS :\n"
        f"   - Tableau synthétisant les 3 à 5 arguments maîtres, leur impact psychologique et la preuve tangible associée.\n\n"
        f"4. 🛡️ L'ANTICIPATION Q&A (QUESTIONS PIÈGES & RÉPARTIES CONSEILLÉES) :\n"
        f"   - Tableau listant les 5 questions les plus dures et déstabilisantes de l'audience, avec la répartie élégante et percutante préconisée.\n\n"
        f"Rédiger ce pack complet d'éloquence en langue [{language}]."
    )
    expected_output = (
        f"Le Pack Complet d'Éloquence en Markdown rédigé en [{language}], comprenant : "
        f"1. Le Script textuel intégral annoté, 2. Les Directives scéniques et de coaching, "
        f"3. La Matrice des arguments clés, et 4. L'Anticipation Q&A avec les 5 réparties conseillées."
    )
    return Task(description=description, expected_output=expected_output, agent=agent, context=context_tasks)
