import ast
from pathlib import Path
import pytest

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SRC_DIR = BASE_DIR / "src"

def get_imported_modules(file_path: Path) -> set:
    """Analyse l'AST (Abstract Syntax Tree) d'un fichier Python pour extraire les modules importés."""
    tree = ast.parse(file_path.read_text(encoding="utf-8"), filename=str(file_path))
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
    return imports

def test_deterministic_tools_do_not_import_llm_or_orchestrators():
    """
    Règle d'Architecture Hexagonale & Craftsmanship (Séparation Cognitif vs Déterministe) :
    Les outils déterministes (GitPublisher, JiraExporter, DiagramExporter) ne doivent JAMAIS
    dépendre d'un LLM, de CrewAI ou d'orchestrateurs d'IA. Ils doivent rester 100% déterministes (0 Token).
    """
    pure_tools = [
        SRC_DIR / "tools" / "git_publisher.py",
        SRC_DIR / "tools" / "jira_exporter.py",
        SRC_DIR / "tools" / "diagram_exporter.py",
        SRC_DIR / "tools" / "log_analyzer.py",
        SRC_DIR / "tools" / "career_exporter.py"
    ]

    forbidden_modules = [
        "crewai",
        "langchain",
        "langchain_google_genai",
        "google.genai",
        "google.generativeai",
        "src.main",
        "src.agents",
        "src.tasks"
    ]

    for tool_file in pure_tools:
        assert tool_file.exists(), f"Fichier introuvable : {tool_file}"
        imports = get_imported_modules(tool_file)
        for forbidden in forbidden_modules:
            for imp in imports:
                assert not imp.startswith(forbidden), (
                    f"VIOLATION HEXAGONALE : L'outil déterministe '{tool_file.name}' "
                    f"importe '{imp}' ce qui viole l'isolation stricte du domaine !"
                )

def test_inversion_of_control_tools_do_not_depend_on_application():
    """
    Règle Ports & Adaptateurs :
    La couche 'tools' (adaptateurs) ne doit jamais dépendre de la couche applicative 'src.main'.
    """
    tools_dir = SRC_DIR / "tools"
    for tool_file in tools_dir.glob("*.py"):
        imports = get_imported_modules(tool_file)
        for imp in imports:
            assert not imp.startswith("src.main"), (
                f"VIOLATION DE DÉPENDANCE : '{tool_file.name}' dépend de 'src.main' !"
            )

def test_config_layer_is_independent_of_agents_and_tasks():
    """
    Règle de Couplage :
    La couche de configuration (src/config/) ne doit pas dépendre des agents ou des tâches.
    """
    config_file = SRC_DIR / "config" / "settings.py"
    assert config_file.exists()
    imports = get_imported_modules(config_file)
    for imp in imports:
        assert not imp.startswith("src.agents"), "La configuration ne doit pas importer src.agents"
        assert not imp.startswith("src.tasks"), "La configuration ne doit pas importer src.tasks"
        assert not imp.startswith("src.tools"), "La configuration ne doit pas importer src.tools"

def test_no_hardcoded_secrets_in_source_code():
    """
    Règle SSI & Clean Architecture :
    Aucune clé secrète en dur ne doit être présente dans les fichiers sous src/.
    """
    import re
    secret_regex = re.compile(r"AIzaSy[0-9A-Za-z-_]{33}|-----BEGIN [A-Z ]*PRIVATE KEY-----")

    for py_file in SRC_DIR.glob("**/*.py"):
        content = py_file.read_text(encoding="utf-8")
        assert not secret_regex.search(content), (
            f"FAILLE DE SÉCURITÉ : Clé secrète détectée en dur dans '{py_file.name}' !"
        )
