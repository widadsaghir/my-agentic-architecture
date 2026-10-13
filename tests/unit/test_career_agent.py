import pytest
from pathlib import Path
from src.agents.architect_agents import create_career_branding_agent
from src.tools.career_exporter import CareerExporter

def test_create_career_branding_agent_attributes():
    """Vérifie que l'Agent Carrière & Personal Branding est configuré pour le CV, LinkedIn et les certifications."""
    career_agent = create_career_branding_agent(llm="gemini/gemini-3.8-flash")

    # 1. Rôle
    assert "Carrière" in career_agent.role or "Branding" in career_agent.role or "Career" in career_agent.role

    # 2. Piliers clés dans le Goal (CV, LinkedIn, Certifications)
    goal_lower = career_agent.goal.lower()
    assert "cv" in goal_lower
    assert "linkedin" in goal_lower
    assert "certification" in goal_lower

    # 3. Posture d'expert en personal branding dans la Backstory
    backstory_lower = career_agent.backstory.lower()
    assert "personal branding" in backstory_lower or "valorisation" in backstory_lower or "carrière" in backstory_lower

    # 4. Non-délégation
    assert career_agent.allow_delegation is False

def test_career_exporter_formats_cv_and_linkedin():
    """Vérifie que CareerExporter formate proprement les blocs CV et le brouillon de post LinkedIn."""
    exporter = CareerExporter()

    title = "Modernisation SSAS vers Microsoft Fabric"
    patterns = [
        "Architecture Hexagonale & DDD",
        "Zero-Trust C2 MASSIF & Private Endpoints",
        "Optimisation FinOps : TCO réduit de 40%"
    ]

    # 1. Génération de points CV
    cv_points = exporter.generate_cv_bullet_points(title, patterns)
    assert len(cv_points) == 3
    assert any("Architecture Hexagonale" in p for p in cv_points)

    # 2. Génération de post LinkedIn (REX)
    post = exporter.generate_linkedin_post(
        author_name="Lead Architect",
        study_title=title,
        key_results=patterns,
        certifications_alignment=["TOGAF 10", "SAFe 6 for Architects"]
    )
    assert "LinkedIn" in post or "#Architecture" in post or "REX" in post
    assert "Microsoft Fabric" in post
    assert "TOGAF 10" in post
