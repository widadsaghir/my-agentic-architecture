"""
Module d'Orchestration & Contrôle de Boucles Multi-Agents (Agentic Loop Controller).
Composant 100% déterministe (0 token LLM) pour gérer les boucles de rétroaction,
l'évaluation par critères stricts, le scoring sur 100 et le coupe-circuit (max itérations).
"""

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class QualityEvaluation:
    """Modèle de données représentant le verdict d'une passe d'évaluation qualité."""
    score: float
    passed: bool
    criteria_scores: Dict[str, float] = field(default_factory=dict)
    critiques: List[str] = field(default_factory=list)
    iteration: int = 1
    raw_verdict: str = ""
    summary: str = ""


class AgenticLoopController:
    """
    Contrôleur déterministe des boucles de rétroaction multi-agents (Self-Correction Loops).
    
    Gère le parsing des critères, le suivi de l'évolution du score au fil des itérations,
    l'injection ciblée des retours critiques dans les prompts et le seuil de bascule.
    """

    def __init__(self, min_score: float = 85.0, max_iterations: int = 4):
        """
        Initialise le contrôleur.
        
        Args:
            min_score: Score minimal sur 100 requis pour valider le livrable (défaut 85.0).
            max_iterations: Nombre maximal de cycles avant validation forcée (défaut 4).
        """
        if min_score < 0 or min_score > 100:
            raise ValueError(f"Le score minimal doit être compris entre 0 et 100 (reçu: {min_score})")
        if max_iterations < 1:
            raise ValueError(f"Le nombre maximal d'itérations doit être >= 1 (reçu: {max_iterations})")

        self.min_score = float(min_score)
        self.max_iterations = int(max_iterations)
        self.history: List[QualityEvaluation] = []

    def parse_evaluation(self, raw_text: str, iteration: int = 1) -> QualityEvaluation:
        """
        Parse l'évaluation produite par le Juge Qualité (Architecture ou Éloquence).
        Extrait le score global, les scores par critères et les critiques prioritaires.
        """
        if not raw_text or not raw_text.strip():
            eval_empty = QualityEvaluation(
                score=0.0,
                passed=False,
                iteration=iteration,
                summary="Évaluation vide reçue."
            )
            self.history.append(eval_empty)
            return eval_empty

        # 1. Extraction du score global (ex: "Score : 88/100", "SCORE: 88", "Score Global: 92")
        global_score = self._extract_score(raw_text)

        # 2. Extraction des sous-critères (ex: "SOLID: 90/100", "Résilience: 85")
        criteria_scores = self._extract_criteria_scores(raw_text)

        # 3. Extraction des critiques / points d'amélioration
        critiques = self._extract_critiques(raw_text)

        # 4. Décision binaire
        passed = global_score >= self.min_score

        summary = (
            f"Itération {iteration}: Score de {global_score:.1f}/100 "
            f"({'VALIDÉ' if passed else 'NON CONFORME - Seuil requis: ' + str(self.min_score)})"
        )

        evaluation = QualityEvaluation(
            score=global_score,
            passed=passed,
            criteria_scores=criteria_scores,
            critiques=critiques,
            iteration=iteration,
            raw_verdict=raw_text,
            summary=summary
        )
        self.history.append(evaluation)
        return evaluation

    def should_continue(self, evaluation: QualityEvaluation) -> bool:
        """
        Détermine si une nouvelle itération de correction doit être déclenchée.
        Retourne True si le score requis n'est pas atteint et qu'il reste des itérations.
        """
        if evaluation.passed:
            return False
        return evaluation.iteration < self.max_iterations

    def build_feedback_prompt(self, evaluation: QualityEvaluation, target_domain: str = "Architecture") -> str:
        """
        Formate les critiques sous forme d'instructions ciblées et impératives
        à réinjecter directement dans le prompt de révision du producteur.
        """
        feedback_lines = [
            f"### 🔄 RÉTROACTION CORRECTIVE — ITÉRATION {evaluation.iteration} (Score actuel : {evaluation.score:.1f}/100 - Seuil : {self.min_score}/100)",
            f"Le livrable précédent ne satisfait pas encore les exigences d'excellence du Comité ({target_domain}).",
            "",
            "#### 📊 Notes par critères d'évaluation :"
        ]

        if evaluation.criteria_scores:
            for criterion, score in evaluation.criteria_scores.items():
                feedback_lines.append(f"- **{criterion}** : {score:.1f}/100")
        else:
            feedback_lines.append("- Score global consolidé sous le seuil requis.")

        feedback_lines.extend([
            "",
            "#### ⚠️ Gaps & Faiblesses critiques à corriger obligatoirement :"
        ])

        if evaluation.critiques:
            for critique in evaluation.critiques:
                feedback_lines.append(f"- {critique}")
        else:
            feedback_lines.append(
                "- Renforcer la rigueur technique, éliminer les ambiguïtés et approfondir les justifications."
            )

        feedback_lines.extend([
            "",
            "#### 🎯 Consignes de révision pour cette passe :",
            "1. Conserver les points forts déjà validés sans régresser.",
            "2. Résoudre chacun des points critiques listés ci-dessus avec un niveau de précision chirurgical.",
            "3. Produire une version intégralement consolidée prête pour la nouvelle réévaluation."
        ])

        return "\n".join(feedback_lines)

    def generate_loop_summary_markdown(self) -> str:
        """
        Génère un tableau Markdown récapitulant la progression du score et des critères
        au fil des itérations.
        """
        if not self.history:
            return "Aucune itération enregistrée."

        lines = [
            "### 📈 Progression de la Qualité & Cycles de Bouclage (Self-Correction Loop)",
            "",
            "| Itération | Score Global | Seuil Requis | Statut | Critères Clés Détectés |",
            "| :---: | :---: | :---: | :---: | :--- |"
        ]

        for ev in self.history:
            status_badge = "🟢 Validé" if ev.passed else ("🟠 Révision" if ev.iteration < self.max_iterations else "🔴 Clôture forcée")
            criteria_str = ", ".join(f"{k}: {v:.0f}" for k, v in list(ev.criteria_scores.items())[:4]) or "N/A"
            lines.append(
                f"| {ev.iteration} | **{ev.score:.1f}/100** | {self.min_score:.0f}/100 | {status_badge} | {criteria_str} |"
            )

        latest = self.history[-1]
        lines.append("")
        if latest.passed:
            lines.append(f"🏆 **Verdict Final** : Qualité validée avec succès à l'itération {latest.iteration} ({latest.score:.1f}/100).")
        else:
            lines.append(f"⚠️ **Verdict Final** : Seuil maximal d'itérations atteint ({latest.iteration}/{self.max_iterations}). Livrable finalisé avec réserves.")

        return "\n".join(lines)

    # -------------------------------------------------------------------------
    # Méthodes privées d'extraction robuste (Regex déterministe)
    # -------------------------------------------------------------------------
    def _extract_score(self, text: str) -> float:
        """Extrait le score global sous diverses syntaxes."""
        # Motifs prioritaires : "Score Global : 88/100", "SCORE: 85", "Score : 90"
        patterns = [
            r"(?:score\s*global|score\s*total|global\s*score|score\s*d['’]impact|score\s*technique|score\s*final)\s*[:=]\s*(\d+(?:[\.,]\d+)?)\s*(?:/\s*100)?",
            r"(?:\[|\b)score\s*[:=]\s*(\d+(?:[\.,]\d+)?)\s*(?:/\s*100)?",
            r"(?:note|score)\s*:\s*(\d+(?:[\.,]\d+)?)\s*/\s*100",
            r"(\d+(?:[\.,]\d+)?)\s*/\s*100"
        ]

        for pat in patterns:
            match = re.search(pat, text, re.IGNORECASE)
            if match:
                try:
                    val = float(match.group(1).replace(",", "."))
                    if 0 <= val <= 100:
                        return val
                except ValueError:
                    continue

        return 0.0

    def _extract_criteria_scores(self, text: str) -> Dict[str, float]:
        """Extrait les notes par critères identifiés dans le texte."""
        criteria: Dict[str, float] = {}

        # Chercher des lignes de type "- SOLID : 85/100" ou "1. Résilience : 90"
        pattern = r"[-*•\d\.]+\s*([A-Za-zÀ-ÿ0-9_\-\s/&'\(\)]+?)\s*[:=]\s*(\d+(?:[\.,]\d+)?)\s*(?:/\s*100)?"
        for line in text.splitlines():
            line_clean = line.strip()
            # Ignorer la ligne de score global pour ne pas la dupliquer
            if re.search(r"score\s*(?:global|total|final)", line_clean, re.IGNORECASE):
                continue
            match = re.match(pattern, line_clean)
            if match:
                crit_name = match.group(1).strip(" *:_#-")
                # Filtrer les faux positifs trop longs ou non pertinents
                if 2 <= len(crit_name) <= 35:
                    try:
                        crit_score = float(match.group(2).replace(",", "."))
                        if 0 <= crit_score <= 100:
                            criteria[crit_name] = crit_score
                    except ValueError:
                        continue

        return criteria

    def _extract_critiques(self, text: str) -> List[str]:
        """Extrait les points critiques ou faiblesses identifiées."""
        critiques: List[str] = []
        in_critiques_section = False

        section_triggers = [
            "critique", "faiblesse", "amélioration", "points à corriger", "point à corriger",
            "gaps", "lacune", "objection", "à revoir", "recommandation", "remarque", "réserve"
        ]

        for line in text.splitlines():
            line_str = line.strip()
            lower = line_str.lower()

            if any(t in lower for t in section_triggers) and any(c in line_str for c in ["#", ":", "**"]):
                in_critiques_section = True
                continue

            if in_critiques_section:
                # Si on rencontre un nouveau grand titre Markdown, on sort de la section
                if line_str.startswith("# ") or line_str.startswith("## ") or line_str.startswith("### "):
                    # Ne pas sortir si c'est encore un sous-titre de critiques
                    if not any(t in lower for t in section_triggers):
                        in_critiques_section = False
                        continue

                if line_str.startswith(("-", "*", "•", "1.", "2.", "3.", "4.", "5.")):
                    # Ignorer si la ligne est une attribution de note (ex: "- SOLID : 90/100")
                    if re.search(r":\s*\d+(?:\s*/\s*100)?\s*$", line_str):
                        continue
                    cleaned = re.sub(r"^[-*•\d\.]+\s*", "", line_str).strip()
                    if len(cleaned) > 10:
                        critiques.append(cleaned)

        # Si aucune section spécifique n'a été détectée, extraire les lignes de puces négatives
        if not critiques:
            for line in text.splitlines():
                line_str = line.strip()
                if re.search(r":\s*\d+(?:\s*/\s*100)?\s*$", line_str):
                    continue
                if line_str.startswith(("-", "*", "•")) and any(w in line_str.lower() for w in ["spof", "couplage", "violation", "manque", "absent", "attention", "faible", "flou"]):
                    cleaned = re.sub(r"^[-*•]+\s*", "", line_str).strip()
                    if len(cleaned) > 10:
                        critiques.append(cleaned)

        return critiques[:10]  # Limite aux 10 points majeurs pour éviter la surcharge
