import os
from pathlib import Path
from dotenv import load_dotenv

# Chemin vers la racine du projet pour charger le .env avec certitude
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
else:
    load_dotenv()

class AppConfig:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key or self.api_key == "votre_cle_api_ici":
            raise ValueError(
                "Erreur de configuration : GEMINI_API_KEY est manquante ou non renseignée dans le fichier .env.\n"
                "Veuillez définir votre clé dans le fichier .env à la racine du projet."
            )

        # Synchronisation avec la variable standard attendue par LangChain / Google
        os.environ["GOOGLE_API_KEY"] = self.api_key

        self.worker_model = os.getenv("GEMINI_WORKER_MODEL", "gemini-1.5-flash")
        self.manager_model = os.getenv("GEMINI_MANAGER_MODEL", "gemini-1.5-pro")

    def get_worker_llm(self):
        """Retourne l'instance LLM pour les agents ouvriers / spécialistes."""
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=self.worker_model,
            google_api_key=self.api_key,
            temperature=0.3
        )

    def get_manager_llm(self):
        """Retourne l'instance LLM pour le Manager Orchestrateur (raisonnement avancé)."""
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=self.manager_model,
            google_api_key=self.api_key,
            temperature=0.2
        )

def get_config() -> AppConfig:
    return AppConfig()
