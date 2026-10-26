"""
Presales & Bid Architecture Linters and Quality Gates.
Ce module implémente 3 Architectural Fitness Functions majeures nées du REX d'avant-vente ferroviaire :
1. AsIsRealityLinter : Détecte et bloque toute hallucination de Cloud prématuré dans l'existant (AS-IS).
2. BidComplianceGate : Valide la conformité aux standards de conseil (Livrables DAG/ADR/DAT, Entrants/Sortants, Co-construction).
3. ZeroTofuViewportGate : Bloque les caractères Unicode défaillants (tofu boxes) et garantit l'adaptation au viewport (zéro dézoomage).
"""
import re
from typing import Dict, List, Any, Optional

class AsIsRealityLinter:
    """
    Fitness Function anti-hallucination.
    Vérifie qu'aucun composant étiqueté AS-IS ou Existant n'injecte du Cloud ou des technologies cibles
    sans justification formelle dans le cahier des charges d'entrée.
    """
    FORBIDDEN_AS_IS_PATTERNS = [
        r"\bcloud\b",
        r"\baws\b",
        r"\bazure\b",
        r"\bgcp\b",
        r"\bserverless\b",
        r"\bkubernetes\b",
        r"\bk3s\b",
        r"\bk8s\b",
        r"\bkafka\b",
        r"\bmicroservices?\b"
    ]

    @classmethod
    def lint_as_is_content(cls, content: str, tender_spec: Optional[str] = None) -> Dict[str, Any]:
        """
        Analyse une section AS-IS.
        Retourne valid=True si aucun terme cible moderne n'est halluciné dans l'existant.
        """
        violations = []
        lower_content = content.lower()
        lower_spec = (tender_spec or "").lower()

        # Isoler les blocs AS-IS si le document est complet
        as_is_blocks = []
        pattern_block = r"(?:#+\s*(?:01\.|diagnostic|architecture)?\s*(?:as-is|existant)[^\n]*)(.*?)(?=#+\s*(?:02\.|transformation|to-be|cible)|\Z)"
        matches = re.findall(pattern_block, lower_content, re.DOTALL)
        if matches:
            as_is_blocks = matches
        else:
            as_is_blocks = [lower_content]

        for block in as_is_blocks:
            for pat in cls.FORBIDDEN_AS_IS_PATTERNS:
                found = re.findall(pat, block)
                if found:
                    term = found[0]
                    # Si le terme était textuellement présent dans le cahier des charges (rare), toléré
                    if term in lower_spec:
                        continue
                    violations.append(
                        f"Hallucination détectée dans l'AS-IS : Le terme '{term}' est utilisé dans l'existant "
                        f"sans être mentionné dans le cahier des charges. L'existant des grands systèmes industriels "
                        f"doit être présumé On-Premise / Datacenter historique."
                    )

        return {
            "valid": len(violations) == 0,
            "violations": violations,
            "as_is_reality_score": 100.0 if len(violations) == 0 else max(0.0, 100.0 - (len(violations) * 25.0))
        }


class BidComplianceGate:
    """
    Quality Gate pour les dossiers d'avant-vente et réponses à appels d'offres.
    Vérifie la présence obligatoire des 4 piliers de conseil gagnants.
    """
    MANDATORY_DELIVERABLES = [
        ("DAG", r"\bdags?\b"),
        ("ADR", r"\badrs?\b"),
        ("DAT", r"\bdats?\b"),
        ("PCA", r"\bpca\b")
    ]
    MANDATORY_CONCEPTS = [
        ("matrice entrants/sortants", [r"entrants?", r"sortants?"]),
        ("co-construction", [r"co-construct", r"co-conception", r"ateliers? participatifs?", r"vis ma vie"]),
        ("conduite du changement", [r"conduite du changement", r"adoption", r"formation"]),
        ("démarche mvp / pilote", [r"mvp", r"pilote", r"preuve par l'épreuve"])
    ]

    @classmethod
    def audit_bid_response(cls, markdown_doc: str) -> Dict[str, Any]:
        """
        Audite une réponse d'avant-vente.
        """
        lower = markdown_doc.lower()
        missing_deliverables = []
        missing_concepts = []

        # Vérification des livrables
        for name, pattern in cls.MANDATORY_DELIVERABLES:
            if not re.search(pattern, lower):
                missing_deliverables.append(name)

        # Vérification des concepts clés
        for concept_name, regex_list in cls.MANDATORY_CONCEPTS:
            matched = any(re.search(r, lower) for r in regex_list)
            if not matched:
                missing_concepts.append(concept_name)

        compliant = (len(missing_deliverables) == 0 and len(missing_concepts) == 0)
        score = 100.0 - (len(missing_deliverables) * 15.0) - (len(missing_concepts) * 10.0)
        score = max(0.0, score)

        return {
            "compliant": compliant,
            "score": score,
            "missing_deliverables": missing_deliverables,
            "missing_concepts": missing_concepts,
            "feedback": (
                "Proposition d'avant-vente conforme aux standards de cabinet de conseil d'élite."
                if compliant else
                f"Proposition incomplète : livrables manquants ({', '.join(missing_deliverables)}) "
                f"ou concepts de conseil absents ({', '.join(missing_concepts)})."
            )
        }


class ZeroTofuViewportGate:
    """
    Quality Gate graphique et ergonomique.
    1. Détecte et élimine les caractères Unicode défaillants (tofu boxes '□□□' causés par des glyphes box-drawing).
    2. Vérifie que les gabarits de présentation HTML garantissent le verrouillage vertical (flex-shrink: 0, height <= 94vh).
    """
    TOFU_SUSPECT_UNICODE = [
        "◀", "▶", "─", "│", "┌", "┐", "└", "┘", "├", "┤", "┬", "┴", "┼", "■", "□"
    ]

    @classmethod
    def check_string_for_tofu(cls, text: str) -> Dict[str, Any]:
        """Vérifie qu'une chaîne de badge ou de texte Pillow ne contient aucun glyphe Unicode tofu."""
        detected = []
        for char in cls.TOFU_SUSPECT_UNICODE:
            if char in text:
                detected.append(char)

        return {
            "valid": len(detected) == 0,
            "detected_tofu_glyphs": detected,
            "error_msg": (
                f"Glyphes Unicode à risque de rendu 'tofu' détectés : {detected}. "
                "Utiliser du texte ASCII pur et dessiner les flèches vectorielles via draw.polygon()."
                if detected else "Aucun glyphe tofu détecté."
            )
        }

    @classmethod
    def check_html_viewport_resilience(cls, html_content: str) -> Dict[str, Any]:
        """
        Vérifie qu'un template de présentation HTML respecte les règles Single-Slide Haute Couture :
        - Hauteur conteneur plafonnée à min(94vh, 880px) ou max-height: 94vh.
        - Footer de navigation verrouillé (flex-shrink: 0).
        - Fil d'Ariane présent et verrouillé (flex-shrink: 0).
        """
        lower = html_content.lower()
        checks = {
            "has_viewport_height_lock": bool(re.search(r"height:\s*min\(9[0-5]vh", lower) or re.search(r"max-height:\s*9[0-5]vh", lower)),
            "has_footer_locked": "flex-shrink: 0" in lower and "footer-bar" in lower,
            "has_ribbon_locked": "flex-shrink: 0" in lower and "progress-ribbon" in lower,
            "has_no_orphan_div_closing": lower.count("<div") == lower.count("</div")
        }

        all_ok = all(checks.values())
        return {
            "valid": all_ok,
            "checks": checks,
            "feedback": "Template HTML 100% résilient (zéro dézoomage requis)." if all_ok else "Défauts d'ergonomie détectés dans le template HTML."
        }
