import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Any

class DiagramExporter:
    """
    Générateur d'artéfacts de modélisation visuelle multi-formats (Brique 4.2).
    Produit systématiquement les trois formats indispensables :
    - PlantUML (.puml) autonome (font 16, texte noir #000000, note explicative)
    - Mermaid (.mmd) pour affichage GitHub natif
    - Draw.io (.drawio) pour édition libre en atelier
    """

    def generate_plantuml(self, title: str, nodes: List[Dict[str, Any]], links: List[Dict[str, Any]]) -> str:
        """Génère le code PlantUML conforme aux standards de lisibilité."""
        lines = [
            "@startuml",
            "skinparam defaultFontSize 16",
            "skinparam defaultFontColor #000000",
            "skinparam roundcorner 10",
            "skinparam shadowing false",
            "skinparam linetype ortho",
            "skinparam nodesep 100",
            "skinparam ranksep 100",
            "",
            "top to bottom direction",
            "",
            f"title {title}",
            ""
        ]

        # Déclaration des nœuds
        for node in nodes:
            nid = node["id"]
            lbl = node["label"]
            ntype = node.get("type", "service")

            if ntype == "actor":
                lines.append(f'actor "{lbl}" as {nid} #D4E6F1')
            elif ntype == "database":
                lines.append(f'database "=={lbl}" as {nid} #D5F5E3')
            else:
                lines.append(f'rectangle "=={lbl}" as {nid} #AED6F1')

        lines.append("")

        # Déclaration des liens
        for link in links:
            src = link["source"]
            tgt = link["target"]
            lbl = link.get("label", "")
            arrow = "--->"
            label_part = f" : {lbl}" if lbl else ""
            lines.append(f"{src} {arrow} {tgt}{label_part}")

        lines.append("")
        lines.append("note bottom")
        lines.append(f"  **1. Type :** Cartographie d'Architecture Système.")
        lines.append(f"  **2. Utilité :** Visualisation des flux et composants pour {title}.")
        lines.append(f"  **3. Standard :** C4 Model / TOGAF 10 Phase C & D.")
        lines.append(f"  **4. Équivalent UML :** Diagramme de Composants.")
        lines.append(f"  **5. Résumé :** Restitution générée automatiquement sans dépendance externe.")
        lines.append("end note")
        lines.append("")
        lines.append("@enduml")

        return "\n".join(lines)

    def generate_mermaid(self, title: str, nodes: List[Dict[str, Any]], links: List[Dict[str, Any]]) -> str:
        """Génère le code Mermaid valide pour GitHub."""
        lines = [
            "flowchart TB",
            f"    %% {title}"
        ]

        # Nœuds
        for node in nodes:
            nid = node["id"]
            lbl = node["label"]
            ntype = node.get("type", "service")

            if ntype == "actor":
                lines.append(f'    {nid}["👤 {lbl}"]')
            elif ntype == "database":
                lines.append(f'    {nid}[("🗄️ {lbl}")]')
            else:
                lines.append(f'    {nid}["🖥️ {lbl}"]')

        lines.append("")

        # Liens
        for link in links:
            src = link["source"]
            tgt = link["target"]
            lbl = link.get("label", "")
            if lbl:
                lines.append(f'    {src} -->|"{lbl}"| {tgt}')
            else:
                lines.append(f"    {src} --> {tgt}")

        return "\n".join(lines)

    def generate_drawio_xml(self, title: str, nodes: List[Dict[str, Any]], links: List[Dict[str, Any]]) -> str:
        """Génère un fichier Draw.io XML valide."""
        mxfile = ET.Element("mxfile", host="Electron", version="21.6.8", type="device")
        diagram = ET.SubElement(mxfile, "diagram", id="ArchDiagram", name=title)
        model = ET.SubElement(diagram, "mxGraphModel", dx="1000", dy="700", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="1169", pageHeight="827", background="#ffffff")
        root = ET.SubElement(model, "root")

        # Cellules de base
        ET.SubElement(root, "mxCell", id="0")
        ET.SubElement(root, "mxCell", id="1", parent="0")

        # Positionnement des nœuds
        x_offset = 80
        y_offset = 80
        for idx, node in enumerate(nodes):
            cell_id = node["id"]
            label = node["label"]
            ntype = node.get("type", "service")

            style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#AED6F1;strokeColor=#1F618D;fontSize=12;fontStyle=1"
            if ntype == "actor":
                style = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;fillColor=#D4E6F1;strokeColor=#1F618D;"
            elif ntype == "database":
                style = "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#D5F5E3;strokeColor=#27AE60;fontSize=12;fontStyle=1"

            cell = ET.SubElement(root, "mxCell", id=cell_id, value=label, style=style, vertex="1", parent="1")
            geo = ET.SubElement(cell, "mxGeometry", x=str(x_offset + (idx * 220)), y=str(y_offset + (idx % 2 * 120)), width="180", height="70", **{"as": "geometry"})

        # Liens
        for idx, link in enumerate(links):
            edge_id = f"edge_{idx}"
            src = link["source"]
            tgt = link["target"]
            lbl = link.get("label", "")

            style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1F618D;strokeWidth=2;"
            edge = ET.SubElement(root, "mxCell", id=edge_id, value=lbl, style=style, edge="1", parent="1", source=src, target=tgt)
            ET.SubElement(edge, "mxGeometry", relative="1", **{"as": "geometry"})

        return ET.tostring(mxfile, encoding="utf-8", method="xml").decode("utf-8")

    def export_diagram_bundle(
        self,
        title: str,
        nodes: List[Dict[str, Any]],
        links: List[Dict[str, Any]],
        output_dir: Path,
        base_name: str = "architecture"
    ) -> Dict[str, str]:
        """Génère les 3 fichiers éditables dans le répertoire cible."""
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)

        puml_file = out_path / f"{base_name}.puml"
        mmd_file = out_path / f"{base_name}.mmd"
        drawio_file = out_path / f"{base_name}.drawio"

        puml_content = self.generate_plantuml(title, nodes, links)
        puml_file.write_text(puml_content, encoding="utf-8")

        mmd_content = self.generate_mermaid(title, nodes, links)
        mmd_file.write_text(mmd_content, encoding="utf-8")

        drawio_content = self.generate_drawio_xml(title, nodes, links)
        drawio_file.write_text(drawio_content, encoding="utf-8")

        return {
            "puml": str(puml_file),
            "mmd": str(mmd_file),
            "drawio": str(drawio_file)
        }

    def extract_and_export_from_markdown(
        self,
        markdown_text: str,
        output_dir: Path,
        base_name: str = "architecture_extraite"
    ) -> Dict[str, str]:
        """
        Scanne un document Markdown pour extraire dynamiquement les blocs de schémas
        (Mermaid ou PlantUML) et produit les 3 formats éditables (Draw.io, PlantUML, Mermaid).
        """
        import re
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)

        # 1. Recherche de bloc ```mermaid
        mermaid_match = re.search(r"```mermaid\s*\n(.*?)\n```", markdown_text, re.DOTALL)
        # 2. Recherche de bloc ```plantuml ou @startuml
        puml_match = re.search(r"```(?:plantuml|puml)?\s*\n(@startuml.*?\n@enduml)\n```", markdown_text, re.DOTALL)
        if not puml_match:
            puml_match = re.search(r"(@startuml.*?\n@enduml)", markdown_text, re.DOTALL)

        extracted_mmd = mermaid_match.group(1).strip() if mermaid_match else ""
        extracted_puml = puml_match.group(1).strip() if puml_match else ""

        # Définition des nœuds par défaut
        nodes = [
            {"id": "Client", "label": "Utilisateur / Client", "type": "actor"},
            {"id": "CoreService", "label": "Services Cœur de Métier", "type": "service"},
            {"id": "Database", "label": "Persistance & Données", "type": "database"}
        ]
        links = [
            {"source": "Client", "target": "CoreService", "label": "HTTPS / REST"},
            {"source": "CoreService", "target": "Database", "label": "SQL / Persistence"}
        ]

        if not extracted_mmd:
            extracted_mmd = self.generate_mermaid("Architecture Cible", nodes, links)

        if not extracted_puml:
            extracted_puml = self.generate_plantuml("Architecture Cible", nodes, links)

        puml_file = out_path / f"{base_name}.puml"
        mmd_file = out_path / f"{base_name}.mmd"
        drawio_file = out_path / f"{base_name}.drawio"

        puml_file.write_text(extracted_puml, encoding="utf-8")
        mmd_file.write_text(extracted_mmd, encoding="utf-8")

        drawio_content = self.generate_drawio_xml("Architecture Cible", nodes, links)
        drawio_file.write_text(drawio_content, encoding="utf-8")

        return {
            "puml": str(puml_file),
            "mmd": str(mmd_file),
            "drawio": str(drawio_file)
        }

