"""Unit tests for Executive Presentation Exporter (0-token deterministic tool).

Validates that executive restitution presentations are generated in 16:9
Bento Grid format with AS-IS vs TO-BE comparisons and single-slide navigation.
"""

from pathlib import Path
import pytest
from src.tools.presentation_exporter import ExecutivePresentationExporter


@pytest.fixture
def sample_study_content() -> str:
    return """# Executive Architecture Synthesis: OmniClaim AI

## Executive Statement
Decomposed monolithic legacy claims core into an autonomous event-driven multi-cloud architecture.

## Key Performance Indicators
- ROI: +84.6%
- Latency: < 350ms
- SLA: 99.99%
- TCO Savings: 35%
- Batch Acceleration: 3.5x
- HITL Escalation: < 5%

## AS-IS Architecture (Legacy Monolith)
- Monolithic Java 8 application running on WebLogic with Oracle RAC database.
- Severe batch locking contention and single point of failure (SPOF).
- Manual claims processing taking 12 to 14 business days.

## TO-BE Architecture (Event-Driven Multi-Cloud)
- Autonomous multi-agent pipeline orchestrated on Amazon EKS with Kafka MSK streaming.
- Enterprise Sovereign AI Enclave on Amazon Bedrock with local PII de-identification.
- Instant claims settlement (< 350ms) with Human-in-the-Loop gate for claims > 2,000 EUR.

## Key Trade-Offs & Decisions
1. Event Streaming: Chose Amazon MSK over REST for outbox replayability and sub-second latency.
2. AI Sovereignty: Chose Amazon Bedrock over public API to guarantee zero training on customer PII.
3. Database Strategy: Chose Aurora PostgreSQL Multi-AZ with PgBouncer over Oracle Exadata.
"""


def test_executive_presentation_exporter_generates_valid_html(tmp_path: Path, sample_study_content: str):
    """Test that presentation exporter compiles markdown + diagrams into interactive 16:9 HTML."""
    out_file = tmp_path / "10_SYNTHESE_EXECUTIVE_RESTITUTION_SLIDES.html"
    exporter = ExecutivePresentationExporter()

    diagrams = {
        "AS-IS": "graph LR\n  Client --> Monolith[Legacy WebLogic]\n  Monolith --> Oracle[(Oracle RAC)]",
        "TO-BE": "graph LR\n  Client --> API[Amazon API Gateway]\n  API --> EKS[Amazon EKS Squads]\n  EKS --> MSK[Amazon MSK]\n  EKS --> Bedrock[Amazon Bedrock]",
    }

    result_path = exporter.export_presentation(
        study_title="OmniClaim AI — Executive Restitution",
        study_content=sample_study_content,
        diagrams=diagrams,
        output_file=out_file,
    )

    assert result_path.exists()
    html_text = result_path.read_text(encoding="utf-8")

    # Assert Haute Couture Standards
    assert "Capgemini" in html_text or "IAF" in html_text or "Executive" in html_text
    assert "bento-grid" in html_text
    assert "16in 9in landscape" in html_text or "16:9" in html_text or "1480px" in html_text
    assert "showSlide" in html_text
    assert "toggleFullScreen" in html_text

    # Assert AS-IS and TO-BE presence
    assert "AS-IS" in html_text
    assert "TO-BE" in html_text
    assert "Legacy WebLogic" in html_text
    assert "Amazon Bedrock" in html_text


def test_executive_presentation_exporter_parses_kpis(sample_study_content: str):
    """Test KPI extraction from executive study markdown."""
    exporter = ExecutivePresentationExporter()
    kpis = exporter.extract_kpis(sample_study_content)

    assert len(kpis) >= 4
    labels = [k["label"].lower() for k in kpis]
    assert any("roi" in l for l in labels)
    assert any("latency" in l or "sla" in l or "tco" in l for l in labels)


def test_executive_presentation_exporter_handles_empty_diagrams(tmp_path: Path, sample_study_content: str):
    """Test graceful generation when no diagrams dictionary is provided."""
    out_file = tmp_path / "empty_diagrams_presentation.html"
    exporter = ExecutivePresentationExporter()

    result_path = exporter.export_presentation(
        study_title="Fallback Test Study",
        study_content=sample_study_content,
        diagrams=None,
        output_file=out_file,
    )

    assert result_path.exists()
    content = result_path.read_text(encoding="utf-8")
    assert "Fallback Test Study" in content
