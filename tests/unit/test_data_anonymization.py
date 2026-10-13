import re
from pathlib import Path
import pytest

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = BASE_DIR / "docs"

# Regex pour détecter les adresses IPv4 privées réelles (RFC 1918)
# 10.x.x.x, 172.16-31.x.x, 192.168.x.x
RFC1918_REGEX = re.compile(
    r"\b(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2[0-9]|3[0-1])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})\b"
)

def test_no_private_ip_addresses_leaked_in_docs():
    """
    Règle de Sécurité & Anonymisation Permanente :
    Aucune adresse IP réelle ou d'infrastructure privée (RFC 1918) ne doit figurer
    dans la documentation d'architecture, les schémas ou les livrables d'études.
    """
    scanned_extensions = ["*.md", "*.puml", "*.mmd", "*.drawio", "*.csv"]
    all_files = []
    for ext in scanned_extensions:
        all_files.extend(DOCS_DIR.glob(f"**/{ext}"))

    assert len(all_files) > 0, "Aucun document trouvé pour le scan d'anonymisation !"

    violations = []
    for f in all_files:
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue

        matches = RFC1918_REGEX.findall(content)
        if matches:
            violations.append(f"{f.relative_to(BASE_DIR)} : IP(s) détectée(s) : {matches}")

    assert len(violations) == 0, (
        f"VIOLATION D'ANONYMISATION : Des adresses IP réelles ont été trouvées dans les documents :\n"
        + "\n".join(violations)
    )

def test_no_raw_api_tokens_in_docs_and_examples():
    """
    Vérifie qu'aucun jeton d'API réel n'a été inséré par mégarde dans les dossiers d'exemples ou de doc.
    """
    token_pattern = re.compile(r"AIzaSy[0-9A-Za-z-_]{33}|ghp_[0-9a-zA-Z]{36}")

    for md_file in DOCS_DIR.glob("**/*.md"):
        content = md_file.read_text(encoding="utf-8")
        matches = token_pattern.findall(content)
        assert len(matches) == 0, (
            f"FUITE DE SECRET : Jeton API détecté dans {md_file.name} !"
        )
