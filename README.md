# Multi-Agent Architecture Platform (AAP)

[![CI Quality Pipeline](https://github.com/widadsaghir/my-agentic-architecture/actions/workflows/ci.yml/badge.svg)](https://github.com/widadsaghir/my-agentic-architecture/actions/workflows/ci.yml)
![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![Tests](https://img.shields.io/badge/tests-45%20passed-brightgreen.svg)
![Architecture](https://img.shields.io/badge/architecture-hexagonal%20%7C%20TOGAF%2010-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This project is a 100% open-source, autonomous multi-agent system designed to act as an expert **Lead Solution & Enterprise Architect**, following the TOGAF ADM framework.

## Project Structure
- `docs/craftsmanship-safe-testing-strategy.md`: Software Craftsmanship & SAFe 6 engineering strategy (Hexagonal Architecture, AI Testing Pyramid, DoD).
- `docs/dossier-architecture-visuelle.md`: Complete visual & functional architecture dossier (living documentation with C4 and Sequence diagrams).
- `docs/architecture-cible-togaf.md`: Target architecture dossier based on TOGAF ADM.
- `docs/roadmap-implementation.md`: Step-by-step implementation roadmap (Bricks 1 to 5).
- `docs/guide-installation-environnement.md`: Detailed environment & setup guide (Windows PowerShell).
- `docs/diagrams/`: Raw source files (PlantUML `.puml`, Mermaid `.mmd`, Draw.io `.drawio`).
- `src/main.py`: Main orchestration script using CrewAI and Gemini API.
- `setup.ps1`: Automated 1-click PowerShell installation script.
- `requirements.txt`: Project Python dependencies.

## Getting Started (Windows Setup)

### Option A: 1-Click Automated Setup (PowerShell)
```powershell
# In PowerShell:
.\setup.ps1
```
Then fill your Gemini API key in `.env`:
```ini
GEMINI_API_KEY=your_gemini_api_key_here
```

### Option B: Manual Setup
Refer to the detailed guide: `docs/guide-installation-environnement.md`.

### Run the System
```powershell
.\.venv\Scripts\Activate.ps1
python src/main.py --language "French" --input "Cadrage préliminaire de migration Cloud"
```
