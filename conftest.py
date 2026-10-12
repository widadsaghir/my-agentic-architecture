import sys
from pathlib import Path

# Ajoute automatiquement la racine du projet au PYTHONPATH pour tous les tests pytest
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
