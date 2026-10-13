import re
import subprocess
from pathlib import Path
from typing import List, Optional

class GitPublisher:
    """
    Adaptateur déterministe de publication Git sécurisée (Brique 4.3).
    Garantit le scan anti-secrets, le formatage des Conventional Commits
    et la porte d'arrêt obligatoire Human-in-the-Loop (HITL) avant tout push.
    """
    SECRET_PATTERNS = [
        (r"AIzaSy[0-9A-Za-z-_]{33}", "Clé API Google/Gemini détectée"),
        (r"AKIA[0-9A-Z]{16}", "Clé d'accès AWS Access Key détectée"),
        (r"ghp_[0-9a-zA-Z]{36}", "Token d'accès personnel GitHub détecté"),
        (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "Bloc de Clé Privée RSA/SSH/ECC détecté"),
        (r"(?i)(password|secret|api_key)\s*=\s*['\"][^'\"]{8,}['\"]", "Secret statique ou mot de passe en clair détecté")
    ]

    def scan_content_for_secrets(self, content: str) -> List[str]:
        """
        Analyse une chaîne de caractères pour y traquer la présence de secrets ou tokens.
        Retourne la liste des avertissements de sécurité.
        """
        warnings = []
        for pattern, warning_msg in self.SECRET_PATTERNS:
            if re.search(pattern, content):
                warnings.append(warning_msg)
        return warnings

    def format_conventional_commit(
        self,
        commit_type: str,
        scope: str,
        description: str,
        breaking: bool = False
    ) -> str:
        """
        Formate le message sous la norme Conventional Commits.
        Exemple : feat(architecture)!: refonte de l'interface REST
        """
        breaking_indicator = "!" if breaking else ""
        scope_part = f"({scope})" if scope else ""
        return f"{commit_type}{scope_part}{breaking_indicator}: {description}"

    def evaluate_hitl_decision(self, user_input: str) -> bool:
        """
        Évalue la décision souveraine de l'architecte humain dans la boucle Human-in-the-Loop.
        Accepte 'o', 'oui', 'y', 'yes' (insensible à la casse).
        """
        if not user_input:
            return False
        cleaned = user_input.strip().lower()
        return cleaned in ["o", "oui", "y", "yes"]

    def request_hitl_approval(self, action_description: str) -> bool:
        """
        Affiche la demande d'arbitrage dans la console et bloque l'exécution en attente de l'accord humain.
        """
        print("\n" + "=" * 70)
        print("  🛑 PORTE DE CONTRÔLE HUMAN-IN-THE-LOOP (HITL) — ARBITRAGE REQUIS")
        print("=" * 70)
        print(f"Action sollicitée : {action_description}")
        try:
            choice = input("Confirmez-vous cette action ? [O/N] : ")
            return self.evaluate_hitl_decision(choice)
        except (EOFError, KeyboardInterrupt):
            print("\n❌ Action annulée par l'utilisateur.")
            return False

    def push_to_remote(self, branch: str = "main", remote: str = "origin", repo_dir: Optional[Path] = None) -> bool:
        """
        Exécute la commande git push de manière déterministe.
        """
        cwd = str(repo_dir) if repo_dir else None
        try:
            cmd = ["git", "push", remote, branch]
            result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)
            print(f"✅ Publication réussie sur {remote}/{branch}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Échec de la publication Git : {e.stderr}")
            return False
