import pytest
from pathlib import Path
from src.agents.architect_agents import create_meta_agent
from src.tools.log_analyzer import LogAnalyzer

def test_create_meta_agent_attributes():
    """Vérifie que le Meta-Agent (Agent Zero) est configuré pour la supervision et le self-healing."""
    meta = create_meta_agent(llm="gemini/gemini-3.8-flash")

    # 1. Rôle
    assert "Meta-Agent" in meta.role or "Agent Zero" in meta.role or "Self-Healing" in meta.role

    # 2. Piliers clés dans le Goal (logs, anomalies/dérives, prompts, correctifs)
    goal_lower = meta.goal.lower()
    assert "log" in goal_lower
    assert "anomalie" in goal_lower or "dérive" in goal_lower or "santé" in goal_lower
    assert "prompt" in goal_lower or "correctif" in goal_lower or "patch" in goal_lower

    # 3. Posture de superviseur hors-bande dans la Backstory
    backstory_lower = meta.backstory.lower()
    assert "observabilité" in backstory_lower or "supervision" in backstory_lower or "self-healing" in backstory_lower

    # 4. Non-délégation
    assert meta.allow_delegation is False

def test_log_analyzer_inspects_log_file(tmp_path):
    """Vérifie que l'outil LogAnalyzer analyse un fichier de log et extrait les statistiques d'exécution."""
    sample_log = tmp_path / "execution_test.log.txt"
    sample_log.write_text(
        "2026-10-12 14:00:00 [INFO] Agent Solution & Infrastructure Architect starting task...\n"
        "2026-10-12 14:00:10 [WARNING] High latency detected on LLM call (12.5s)\n"
        "2026-10-12 14:00:20 [INFO] Agent Challenger starting task...\n"
        "2026-10-12 14:00:30 [ERROR] 404 Model deprecated, falling back to gemini-3.8-flash\n"
        "2026-10-12 14:00:40 [INFO] Crew execution completed successfully.\n",
        encoding="utf-8"
    )

    analyzer = LogAnalyzer()
    stats = analyzer.analyze_log_file(sample_log)

    assert stats["total_lines"] == 5
    assert stats["warning_count"] == 1
    assert stats["error_count"] == 1
    assert stats["status"] == "Attention Requise (Erreurs détectées)"
    assert len(stats["detected_errors"]) == 1
    assert "404 Model deprecated" in stats["detected_errors"][0]
