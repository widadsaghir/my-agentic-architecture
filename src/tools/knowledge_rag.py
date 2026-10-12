import os
from pathlib import Path
from typing import Optional, List, Dict, Any
import chromadb
from crewai.tools import BaseTool
from pydantic import Field

# Répertoires par défaut basés sur la structure du projet
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_PERSIST_DIR = BASE_DIR / "chroma_db"
DEFAULT_KNOWLEDGE_DIR = BASE_DIR / "knowledge"

class ArchitectureRAGManager:
    """
    Gestionnaire de la base vectorielle locale ChromaDB.
    Indexe les blueprints, règles de sécurité C2, normes Cloud WAF et Software Craftsmanship.
    """
    def __init__(
        self,
        persist_dir: Optional[Path] = None,
        knowledge_dir: Optional[Path] = None,
        collection_name: str = "architecture_doctrine"
    ):
        self.persist_dir = Path(persist_dir) if persist_dir else DEFAULT_PERSIST_DIR
        self.knowledge_dir = Path(knowledge_dir) if knowledge_dir else DEFAULT_KNOWLEDGE_DIR
        self.collection_name = collection_name

        self.persist_dir.mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(path=str(self.persist_dir))
        self.collection = self.client.get_or_create_collection(name=self.collection_name)

    def ingest_knowledge(self) -> int:
        """
        Lit l'ensemble des fichiers Markdown du répertoire knowledge/ et les indexe dans ChromaDB.
        Retourne le nombre total de fragments (chunks) indexés.
        """
        if not self.knowledge_dir.exists():
            return 0

        documents: List[str] = []
        metadatas: List[Dict[str, Any]] = []
        ids: List[str] = []

        chunk_counter = 0

        for file_path in self.knowledge_dir.glob("**/*.md"):
            try:
                content = file_path.read_text(encoding="utf-8")
            except Exception:
                continue

            # Découpage logique par sections Markdown (## ) ou par blocs
            sections = content.split("\n## ")
            for idx, section in enumerate(sections):
                chunk_text = section if idx == 0 else f"## {section}"
                chunk_text = chunk_text.strip()
                if len(chunk_text) < 30:
                    continue

                chunk_id = f"{file_path.stem}_chunk_{idx}"
                documents.append(chunk_text)
                metadatas.append({
                    "source": str(file_path.name),
                    "path": str(file_path.relative_to(self.knowledge_dir)),
                    "chunk_index": idx
                })
                ids.append(chunk_id)
                chunk_counter += 1

        if documents:
            # Upsert pour éviter les doublons lors des ré-indexations
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )

        return chunk_counter

    def search(self, query: str, n_results: int = 3) -> List[Dict[str, Any]]:
        """
        Effectue une recherche sémantique par similarité vectorielle.
        """
        count = self.collection.count()
        if count == 0:
            return []

        limit = min(n_results, count)
        results = self.collection.query(
            query_texts=[query],
            n_results=limit
        )

        formatted_results: List[Dict[str, Any]] = []
        if results and "documents" in results and results["documents"]:
            docs = results["documents"][0]
            metas = results["metadatas"][0] if "metadatas" in results and results["metadatas"] else [{}] * len(docs)
            distances = results["distances"][0] if "distances" in results and results["distances"] else [0.0] * len(docs)

            for doc, meta, dist in zip(docs, metas, distances):
                formatted_results.append({
                    "content": doc,
                    "metadata": meta,
                    "distance": dist
                })

        return formatted_results


class KnowledgeSearchTool(BaseTool):
    """
    Outil CrewAI permettant aux agents d'interroger la doctrine d'architecture et de sécurité.
    """
    name: str = "Interroger la Doctrine d'Architecture & Sécurité"
    description: str = (
        "Recherche sémantiquement dans la base vectorielle locale ChromaDB les règles de sécurité Zero-Trust C2, "
        "les principes d'Architecture Hexagonale, les patterns de résilience Cloud WAF et les normes SAFe."
    )
    rag_manager: ArchitectureRAGManager = Field(default_factory=ArchitectureRAGManager)

    def _run(self, query: str) -> str:
        """Exécute la recherche vectorielle et formate les extraits pertinents."""
        results = self.rag_manager.search(query, n_results=3)
        if not results:
            return "Aucune règle ou patron d'architecture correspondant n'a été trouvé dans la base de connaissances."

        output_parts = ["### Extraits de la Doctrine d'Architecture Retrouvés :\n"]
        for idx, res in enumerate(results, 1):
            source = res["metadata"].get("source", "Inconnu")
            content = res["content"]
            output_parts.append(f"**[Source {idx} : {source}]**\n{content}\n")

        return "\n---\n".join(output_parts)
