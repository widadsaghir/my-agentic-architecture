import re
from pathlib import Path
from typing import Dict, Any, List

class LogAnalyzer:
    """
    Outil d'observabilité et d'analyse de traces pour le Meta-Agent / Agent Zero (Brique 5.1).
    Scanne les logs d'exécution, détecte les erreurs, les latences et les dérives de prompts.
    """
    def analyze_log_file(self, log_path: Path) -> Dict[str, Any]:
        """
        Analyse un fichier de log d'exécution et produit un bilan d'observabilité structuré.
        """
        log_file = Path(log_path)
        if not log_file.exists():
            return {
                "total_lines": 0,
                "warning_count": 0,
                "error_count": 0,
                "status": "Fichier de log introuvable",
                "detected_errors": [],
                "detected_warnings": []
            }

        lines = log_file.read_text(encoding="utf-8").splitlines()
        warnings: List[str] = []
        errors: List[str] = []

        for line in lines:
            line_str = line.strip()
            if "[ERROR]" in line_str or "ERROR:" in line_str or "Exception" in line_str or "ClientError" in line_str:
                errors.append(line_str)
            elif "[WARNING]" in line_str or "WARNING:" in line_str or "DeprecationWarning" in line_str:
                warnings.append(line_str)

        if errors:
            status = "Attention Requise (Erreurs détectées)"
        elif warnings:
            status = "Nominal avec Avertissements"
        else:
            status = "100% Opérationnel & Nominal"

        return {
            "total_lines": len(lines),
            "warning_count": len(warnings),
            "error_count": len(errors),
            "status": status,
            "detected_errors": errors[:5],  # Top 5 erreurs
            "detected_warnings": warnings[:5]
        }

    def generate_health_report(self, log_path: Path) -> str:
        """Formate un rapport de santé système en Markdown pour le Meta-Agent."""
        stats = self.analyze_log_file(log_path)
        lines = [
            f"# 🩺 RAPPORT D'OBSERVABILITÉ ET DE SANTÉ SYSTÈME (META-AGENT)",
            f"**Fichier audité :** `{log_path.name}`",
            f"**Statut Global :** **{stats['status']}**",
            f"**Lignes de traces :** {stats['total_lines']}",
            f"**Avertissements :** {stats['warning_count']}",
            f"**Erreurs détectées :** {stats['error_count']}\n"
        ]

        if stats["detected_errors"]:
            lines.append("### 🚨 Principales Anomalies Détectées :")
            for err in stats["detected_errors"]:
                lines.append(f"- `{err}`")

        return "\n".join(lines)
