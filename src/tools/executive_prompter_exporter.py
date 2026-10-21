"""
Executive Prompter & Speech Exporter (Outil Déterministe 0-Token).
Exporte les scripts d'éloquence au format prompter annoté, analyse le débit vocal,
les pauses scéniques et génère le téléprompteur interactif Single-Slide HTML.
"""

from pathlib import Path
import re
from typing import Dict, List, Optional


class ExecutivePrompterExporter:
    """Outil déterministe de formatage et d'export du Pack d'Éloquence & Prompter TEDx."""

    def __init__(self, words_per_minute: int = 130):
        """
        Initialise l'exportateur.
        
        Args:
            words_per_minute: Vitesse d'élocution moyenne pour conférencier TEDx (défaut: 130 mots/min).
        """
        self.words_per_minute = words_per_minute

    def analyze_speech_metrics(self, script_text: str) -> Dict[str, object]:
        """
        Analyse les métriques vocales et scéniques du discours.
        """
        clean_text = re.sub(r"\[.*?\]", "", script_text)
        words = re.findall(r"\b\w+\b", clean_text)
        total_words = len(words)

        duration_minutes = total_words / self.words_per_minute if total_words > 0 else 0.0

        # Comptage des repères scéniques
        pauses = len(re.findall(r"\[PAUSE.*?\]", script_text, re.IGNORECASE))
        breathes = len(re.findall(r"\[BREATHE\]", script_text, re.IGNORECASE))
        smiles = len(re.findall(r"\[SOURIRE\]", script_text, re.IGNORECASE))
        gazes = len(re.findall(r"\[REGARD.*?\]", script_text, re.IGNORECASE))
        intonations = len(re.findall(r"\[.*?INTONATION.*?\]", script_text, re.IGNORECASE))

        # Estimation de la durée des pauses (ex: 2 secondes par pause)
        extra_pause_seconds = (pauses * 2) + (breathes * 1.5)
        total_seconds = int((duration_minutes * 60) + extra_pause_seconds)
        final_minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60

        return {
            "total_words": total_words,
            "estimated_duration": f"{final_minutes} min {remaining_seconds:02d} s",
            "duration_seconds": total_seconds,
            "pauses_count": pauses,
            "breathes_count": breathes,
            "smiles_count": smiles,
            "gazes_count": gazes,
            "intonations_count": intonations,
            "scenographic_density": f"{((pauses + breathes + smiles + gazes + intonations) / max(total_words, 1)) * 100:.1f}%"
        }

    def export_prompter_markdown(
        self,
        title: str,
        script_text: str,
        metrics: Optional[Dict[str, object]] = None,
        output_file: Optional[Path] = None
    ) -> Path:
        """Exporte le prompter enrichi des métriques sous forme de document Markdown."""
        if output_file is None:
            output_file = Path("02_SCRIPT_PROMPTER_TEDX.md")

        output_file.parent.mkdir(parents=True, exist_ok=True)
        if metrics is None:
            metrics = self.analyze_speech_metrics(script_text)

        md_content = [
            f"# 🎙️ {title} — Script Prompter TEDx & Repères Scéniques",
            "",
            "### ⏱️ Métriques & Débit Vocal Estimé",
            f"- **Volume de mots** : {metrics['total_words']} mots",
            f"- **Durée estimée** : {metrics['estimated_duration']} (rythme posé à {self.words_per_minute} mots/min)",
            f"- **Pauses stratégiques** : {metrics['pauses_count']} `[PAUSE]` | **Respirations** : {metrics['breathes_count']} `[BREATHE]`",
            f"- **Points d'ancrage visuel** : {metrics['gazes_count']} `[REGARD]` | **Sourires** : {metrics['smiles_count']} `[SOURIRE]`",
            f"- **Inflections d'autorité** : {metrics['intonations_count']} `[↘ INTONATION DESCENDANTE]`",
            "",
            "---",
            "",
            "## 📜 Partition Oratoire Mot à Mot",
            "",
            script_text.strip(),
            ""
        ]

        output_file.write_text("\n".join(md_content), encoding="utf-8")
        return output_file

    def export_interactive_html(
        self,
        title: str,
        script_text: str,
        metrics: Optional[Dict[str, object]] = None,
        output_file: Optional[Path] = None
    ) -> Path:
        """
        Génère une interface de téléprompteur interactif HTML Single-Slide Haute Couture.
        """
        if output_file is None:
            output_file = Path("02_PROMPTER_INTERACTIF_TEDX.html")

        output_file.parent.mkdir(parents=True, exist_ok=True)
        if metrics is None:
            metrics = self.analyze_speech_metrics(script_text)

        # Découpage du texte en paragraphes / cartes de prompteur
        paragraphs = [p.strip() for p in script_text.split("\n\n") if p.strip()]
        if not paragraphs:
            paragraphs = [script_text]

        # Remplacement stylisé des tags scéniques
        def stylize_tags(text: str) -> str:
            replacements = [
                (r"\[PAUSE\s*(\d*s?)\]", r'<span class="badge badge-pause">⏸️ PAUSE \1</span>'),
                (r"\[BREATHE\]", r'<span class="badge badge-breathe">💨 BREATHE</span>'),
                (r"\[SOURIRE\]", r'<span class="badge badge-smile">😊 SOURIRE</span>'),
                (r"\[REGARD\s*(.*?)\]", r'<span class="badge badge-gaze">👁️ REGARD \1</span>'),
                (r"\[↘\s*INTONATION\s*DESCENDANTE\]", r'<span class="badge badge-tone">↘ INTONATION FERME</span>'),
            ]
            for pat, rep in replacements:
                text = re.sub(pat, rep, text, flags=re.IGNORECASE)
            return text

        cards_html = []
        for idx, p in enumerate(paragraphs, 1):
            stylized_p = stylize_tags(p)
            cards_html.append(f"""
            <div class="prompter-card {'active' if idx == 1 else ''}" data-slide="{idx}">
                <div class="card-meta">
                    <span class="card-num">Séquence {idx} / {len(paragraphs)}</span>
                    <span class="card-pace">Rythme : 130 mpm</span>
                </div>
                <div class="card-text">{stylized_p}</div>
            </div>
            """)

        html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Prompter Exécutif TEDx</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #090d16;
            --bg-card: #131b2e;
            --border-card: #202c45;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #3b82f6;
            --accent-glow: rgba(59, 130, 246, 0.25);
            --pause-color: #f59e0b;
            --breathe-color: #06b6d4;
            --smile-color: #10b981;
            --gaze-color: #8b5cf6;
            --tone-color: #f43f5e;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background-color: var(--bg-primary);
            color: var(--text-main);
            font-family: 'Plus Jakarta Sans', sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}
        header {{
            padding: 1.25rem 2.5rem;
            border-bottom: 1px solid var(--border-card);
            background: rgba(19, 27, 46, 0.7);
            backdrop-filter: blur(12px);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .header-title h1 {{
            font-size: 1.25rem;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: -0.02em;
        }}
        .kpi-bar {{
            display: flex;
            gap: 1rem;
        }}
        .kpi-chip {{
            background: #0f172a;
            border: 1px solid var(--border-card);
            border-radius: 9999px;
            padding: 0.35rem 1rem;
            font-size: 0.85rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-muted);
        }}
        .kpi-chip strong {{ color: var(--accent); }}
        main {{
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2.5rem;
            position: relative;
        }}
        .prompter-card {{
            display: none;
            width: 100%;
            max-width: 1100px;
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 20px;
            padding: 3rem 4rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6), 0 0 30px var(--accent-glow);
            animation: fadeIn 0.25s ease-in-out;
        }}
        .prompter-card.active {{
            display: block;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(8px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .card-meta {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 2rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            color: var(--text-muted);
            border-bottom: 1px solid var(--border-card);
            padding-bottom: 1rem;
        }}
        .card-text {{
            font-size: 1.85rem;
            line-height: 1.6;
            font-weight: 500;
            color: #ffffff;
            letter-spacing: -0.01em;
        }}
        .badge {{
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.95rem;
            font-weight: 700;
            padding: 0.2rem 0.65rem;
            border-radius: 6px;
            margin: 0 0.35rem;
            vertical-align: middle;
        }}
        .badge-pause {{ background: rgba(245, 158, 11, 0.2); color: var(--pause-color); border: 1px solid var(--pause-color); }}
        .badge-breathe {{ background: rgba(6, 182, 212, 0.2); color: var(--breathe-color); border: 1px solid var(--breathe-color); }}
        .badge-smile {{ background: rgba(16, 185, 129, 0.2); color: var(--smile-color); border: 1px solid var(--smile-color); }}
        .badge-gaze {{ background: rgba(139, 92, 246, 0.2); color: var(--gaze-color); border: 1px solid var(--gaze-color); }}
        .badge-tone {{ background: rgba(244, 63, 94, 0.2); color: var(--tone-color); border: 1px solid var(--tone-color); }}
        footer {{
            padding: 1.25rem 2.5rem;
            border-top: 1px solid var(--border-card);
            background: rgba(19, 27, 46, 0.7);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .nav-controls {{
            display: flex;
            gap: 1rem;
        }}
        button {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            color: #ffffff;
            padding: 0.6rem 1.4rem;
            border-radius: 8px;
            font-family: inherit;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }}
        button:hover {{
            background: var(--accent);
            border-color: var(--accent);
        }}
        .shortcuts {{
            font-size: 0.85rem;
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-title">
            <h1>🎙️ {title}</h1>
        </div>
        <div class="kpi-bar">
            <div class="kpi-chip">Mots : <strong>{metrics['total_words']}</strong></div>
            <div class="kpi-chip">Durée : <strong>{metrics['estimated_duration']}</strong></div>
            <div class="kpi-chip">Pauses : <strong>{metrics['pauses_count']}</strong></div>
            <div class="kpi-chip">Respirations : <strong>{metrics['breathes_count']}</strong></div>
        </div>
    </header>
    <main>
        {"".join(cards_html)}
    </main>
    <footer>
        <div class="shortcuts">
            Raccourcis : [←] Précédent | [→] / [Espace] Suivant | [F] Plein Écran
        </div>
        <div class="nav-controls">
            <button onclick="prevSlide()">← Précédent</button>
            <button onclick="nextSlide()">Suivant →</button>
        </div>
    </footer>
    <script>
        let currentSlide = 1;
        const totalSlides = {len(paragraphs)};
        function showSlide(n) {{
            if (n < 1) n = 1;
            if (n > totalSlides) n = totalSlides;
            currentSlide = n;
            document.querySelectorAll('.prompter-card').forEach(card => card.classList.remove('active'));
            const activeCard = document.querySelector(`.prompter-card[data-slide="${{currentSlide}}"]`);
            if (activeCard) activeCard.classList.add('active');
        }}
        function nextSlide() {{ showSlide(currentSlide + 1); }}
        function prevSlide() {{ showSlide(currentSlide - 1); }}
        window.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight' || e.key === ' ') {{ e.preventDefault(); nextSlide(); }}
            else if (e.key === 'ArrowLeft') {{ e.preventDefault(); prevSlide(); }}
            else if (e.key.toLowerCase() === 'f') {{
                if (!document.fullscreenElement) document.documentElement.requestFullscreen();
                else document.exitFullscreen();
            }}
        }});
    </script>
</body>
</html>
"""
        output_file.write_text(html_template, encoding="utf-8")
        return output_file
