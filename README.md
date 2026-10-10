# Multi-Agent Architecture Platform (AAP)

This project is a 100% open-source, autonomous multi-agent system designed to act as an expert **Lead Solution & Enterprise Architect**, following the TOGAF ADM framework.

## Project Structure
- `docs/architecture-cible-togaf.md`: Target architecture dossier based on TOGAF ADM.
- `src/main.py`: Main orchestration script using CrewAI and Gemini API.
- `requirements.txt`: Project Python dependencies.

## Getting Started (Laptop Setup)
1. Clone your repository:
   ```bash
   git clone <your-github-repo-url>
   cd my-agentic-architecture
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Gemini API key:
   ```bash
   export GEMINI_API_KEY="your_api_key"
   ```
4. Run the system:
   ```bash
   python src/main.py --language "English" --input "Your raw notes or project request"
   ```
