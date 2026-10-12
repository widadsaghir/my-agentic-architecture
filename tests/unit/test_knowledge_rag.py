import pytest
from pathlib import Path
from src.tools.knowledge_rag import ArchitectureRAGManager, KnowledgeSearchTool

@pytest.fixture
def temp_rag_setup(tmp_path):
    """Fixture créant un dossier de connaissances temporaire et une base ChromaDB isolée."""
    knowledge_dir = tmp_path / "knowledge"
    knowledge_dir.mkdir(parents=True, exist_ok=True)
    persist_dir = tmp_path / "chroma_db"
    persist_dir.mkdir(parents=True, exist_ok=True)

    # Document 1 : Sécurité
    sec_doc = knowledge_dir / "sec_c2.md"
    sec_doc.write_text(
        "# DOCTRINE SÉCURITÉ C2\n\nPour le niveau C2 MASSIF, il faut utiliser des Private Endpoints et une clé CMK sur HSM FIPS 140-2.",
        encoding="utf-8"
    )

    # Document 2 : Craftsmanship
    craft_doc = knowledge_dir / "craft_hex.md"
    craft_doc.write_text(
        "# DOCTRINE ARCHITECTURE HEXAGONALE\n\nLe Cœur de Domaine ne doit dépendre d'aucun framework. Ports et Adaptateurs obligatoires.",
        encoding="utf-8"
    )

    manager = ArchitectureRAGManager(persist_dir=persist_dir, knowledge_dir=knowledge_dir)
    return manager

def test_rag_manager_ingestion_and_search(temp_rag_setup):
    """Vérifie que le RAG indexe correctement les documents et retrouve le contenu pertinent."""
    manager = temp_rag_setup

    # 1. Ingestion
    count = manager.ingest_knowledge()
    assert count >= 2

    # 2. Recherche sémantique Sécurité C2
    results_sec = manager.search("exigences C2 MASSIF Private Endpoints", n_results=1)
    assert len(results_sec) > 0
    assert "C2 MASSIF" in results_sec[0]["content"] or "Private Endpoints" in results_sec[0]["content"]

    # 3. Recherche sémantique Hexagonale
    results_craft = manager.search("Architecture Hexagonale Domaine Ports", n_results=1)
    assert len(results_craft) > 0
    assert "Hexagonale" in results_craft[0]["content"] or "Ports" in results_craft[0]["content"]

def test_knowledge_search_tool_execution(temp_rag_setup):
    """Vérifie que l'outil CrewAI KnowledgeSearchTool formate correctement la réponse pour les agents."""
    manager = temp_rag_setup
    manager.ingest_knowledge()

    tool = KnowledgeSearchTool(rag_manager=manager)

    response = tool._run("Quelles sont les règles pour le niveau C2 MASSIF ?")
    assert isinstance(response, str)
    assert "C2 MASSIF" in response or "Private Endpoints" in response
