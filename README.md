# Multi-Agent Architecture Platform (AAP)

This project is a 100% open-source, autonomous multi-agent system designed to act as an expert **Lead Solution & Enterprise Architect**, following the TOGAF ADM framework.

## Project Structure
- `docs/architecture-cible-togaf.md`: Target architecture dossier based on TOGAF ADM.
- `docs/roadmap-implementation.md`: Step-by-step implementation roadmap (Bricks 1 to 5).
- `docs/guide-installation-environnement.md`: Detailed environment & setup guide (Windows PowerShell).
- `docs/diagrams/`: Architectural diagrams (C4 Model & Sequence diagrams in PlantUML & Mermaid).
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
