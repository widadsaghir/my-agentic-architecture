import csv
import re
from pathlib import Path
from typing import List, Dict, Any

class JiraBacklogExporter:
    """
    Exportateur de backlog agile vers format CSV standard Jira (Brique 4.4).
    Garantit l'encodage UTF-8-sig et le séparateur point-virgule (;) pour Excel Français.
    """
    def parse_stories_from_markdown(self, markdown_text: str) -> List[Dict[str, Any]]:
        """
        Extrait les User Stories et Enabler Stories depuis le livrable Markdown.
        Supporte les variantes d'en-têtes Markdown :
        - '### User Story ID'
        - '#### ID : Titre'
        - '### ID : Titre'
        """
        stories = []
        pattern = re.compile(r"(?:^|\n)#{3,4}\s+(?:User Story\s+)?([A-Z]+-\d+)(?:\s*:\s*([^\n]+))?")
        matches = list(pattern.finditer(markdown_text))

        # Fallback si format générique '### User Story ID'
        if not matches:
            pattern = re.compile(r"(?:^|\n)###\s+User Story\s+[`\*]*([A-Z0-9_-]+)[`\*]*")
            matches = list(pattern.finditer(markdown_text))

        # Détection d'une Definition of Done (DoD) globale au niveau du document
        global_dod_match = re.search(r"##\s+\d*\.?\s*Definition of Done.*?\n(.+?)(?=\n##|\Z)", markdown_text, re.DOTALL | re.IGNORECASE)
        global_dod = "Conforme à la DoD globale du projet (5 piliers)" if global_dod_match else ""

        for idx, match in enumerate(matches):
            story_id = match.group(1).strip()
            inline_title = match.group(2).strip() if len(match.groups()) > 1 and match.group(2) else ""

            # Délimitation du bloc de la story jusqu'à la prochaine story ou fin
            start_pos = match.end()
            end_pos = matches[idx + 1].start() if idx + 1 < len(matches) else len(markdown_text)
            block = markdown_text[start_pos:end_pos]

            # Extraction des champs
            title_match = re.search(r"\*\s*\*\*Titre\s*:\*\*\s*(.+)", block)
            format_match = re.search(r"\*\s*\*\*Description.*?\*\*\s*[:\n]\s*(.+?)(?=\n\*\s*\*\*|\Z)", block, re.DOTALL)
            points_match = re.search(r"\*\s*\*\*Estimation\s*:\*\*\s*(\d+)", block)
            crit_match = re.search(r"\*\s*\*\*Critères d'Acceptation.*?\*\*\s*[:\n]\s*(.+?)(?=\n\*\s*\*\*|\Z)", block, re.DOTALL)
            dod_match = re.search(r"\*\s*\*\*Definition of Done.*?\*\*\s*[:\n]\s*(.+?)(?=\n#|\Z)", block, re.DOTALL)

            title = inline_title or (title_match.group(1).strip() if title_match else f"User Story {story_id}")
            desc = format_match.group(1).strip() if format_match else block.strip()
            points = points_match.group(1).strip() if points_match else "5"
            acceptance = crit_match.group(1).strip().replace("\n", " ") if crit_match else ""
            dod = (dod_match.group(1).strip().replace("\n", " ") if dod_match else "") or global_dod

            stories.append({
                "issue_type": "Story",
                "id": story_id,
                "summary": f"[{story_id}] {title}",
                "description": desc,
                "story_points": points,
                "acceptance_criteria": acceptance,
                "definition_of_done": dod
            })

        return stories

    def lint_story_invest(self, story: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyse la qualité agile de la User Story selon les principes INVEST :
        - Vérifie la présence de critères d'acceptation et de Definition of Done.
        - Contrôle que la taille de la Story ne dépasse pas 8 Story Points (règle Small).
        """
        points_str = str(story.get("story_points", "5"))
        nums = re.findall(r"\d+", points_str)
        points = int(nums[0]) if nums else 5

        has_crit = bool(story.get("acceptance_criteria", "").strip())
        has_dod = bool(story.get("definition_of_done", "").strip())
        is_oversized = points > 8

        if is_oversized:
            invest_status = f"WARNING_TAILLE ({points} pts > 8 - Nécessite Découpage)"
        elif not has_crit or not has_dod:
            invest_status = "WARNING_INCOMPLETE (Critères ou DoD manquants)"
        else:
            invest_status = "CONFORME_INVEST"

        dod_status = "DOD_VALIDE" if has_dod else "DOD_MANQUANTE"

        return {
            "story_id": story.get("id", ""),
            "points": points,
            "is_oversized": is_oversized,
            "has_criteria": has_crit,
            "has_dod": has_dod,
            "invest_status": invest_status,
            "dod_status": dod_status
        }

    def export_to_csv(self, markdown_text: str, output_csv_path: Path) -> int:
        """
        Parse le markdown et génère le fichier CSV compatible Jira et Excel Français (délimiteur ;).
        """
        stories = self.parse_stories_from_markdown(markdown_text)
        output_csv_path = Path(output_csv_path)
        output_csv_path.parent.mkdir(parents=True, exist_ok=True)

        fieldnames = [
            "Issue Type",
            "Summary",
            "Description",
            "Story Points",
            "Acceptance Criteria",
            "Definition of Done",
            "INVEST Status",
            "DoD Status"
        ]

        # Encodage utf-8-sig pour que Microsoft Excel sous Windows lise directement les accents
        with open(output_csv_path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(fieldnames)

            for s in stories:
                lint = self.lint_story_invest(s)
                writer.writerow([
                    s["issue_type"],
                    s["summary"],
                    s["description"],
                    s["story_points"],
                    s["acceptance_criteria"],
                    s["definition_of_done"],
                    lint["invest_status"],
                    lint["dod_status"]
                ])

        return len(stories)
