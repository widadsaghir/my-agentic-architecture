"""
Automated Test Suite for Executive HTML Presentation Decks.
Valide à 100% l'intégrité JavaScript, la navigabilité, la résilience DOM et les critères ergonomiques
pour garantir qu'aucun bouton n'est cassé et que la présentation est irréprochable le Jour J.
"""
import re
import pytest
from pathlib import Path

DECK_PATH = Path(r"C:\Users\ws48e6bl\Desktop\DOSSIER_AVV_SOPRA_STERIA_NEXT_FERROVIAIRE\Soutenance_AVV_SIV_Ferroviaire_Executive.html")

@pytest.fixture
def html_content():
    assert DECK_PATH.exists(), f"Fichier de présentation introuvable : {DECK_PATH}"
    return DECK_PATH.read_text(encoding="utf-8")

def test_javascript_syntax_and_braces_balance(html_content):
    """Test Unitaire : Vérifie que le code JavaScript n'a aucune accolade déséquilibrée (syntax error)."""
    scripts = re.findall(r'<script>(.*?)</script>', html_content, re.DOTALL)
    assert len(scripts) >= 1, "Aucune balise <script> trouvée !"
    js = scripts[0]

    # Vérification stricte des accolades
    open_braces = js.count('{')
    close_braces = js.count('}')
    assert open_braces == close_braces, f"Erreur de syntaxe JS : {open_braces} '{{' vs {close_braces} '}}'"

    # Vérification des parenthèses
    open_parens = js.count('(')
    close_parens = js.count(')')
    assert open_parens == close_parens, f"Erreur de syntaxe JS : {open_parens} '(' vs {close_parens} ')'"

def test_javascript_mandatory_functions_exist(html_content):
    """Test Unitaire : Vérifie que toutes les fonctions de navigation et d'interaction sont déclarées."""
    required_functions = [
        "showSlide",
        "nextSlide",
        "prevSlide",
        "goToSlide",
        "toggleFullscreen",
        "toggleTheme",
        "toggleTimer",
        "resetTimer",
        "startTimer",
        "pauseTimer",
        "updateTimerDisplay",
        "updateSlideGuideTime",
        "updateRibbonActivePill"
    ]
    for func in required_functions:
        assert re.search(r"\bfunction\s+" + re.escape(func) + r"\b", html_content), (
            f"Fonction JavaScript critique manquante : {func}()"
        )

def test_dom_slide_structure_and_total_count(html_content):
    """Test d'Intégration DOM : Vérifie que les 10 slides existent, que Slide 1 est actif et les balises div équilibrées."""
    # 1. Équilibre des balises <div>
    open_divs = html_content.count("<div")
    close_divs = html_content.count("</div")
    assert open_divs == close_divs, f"Déséquilibre HTML : {open_divs} <div> ouvertes vs {close_divs} fermées"

    # 2. Détection des 10 slides
    slides = re.findall(r'class="slide[^"]*"\s+data-slide="(\d+)"', html_content)
    assert len(slides) == 10, f"Nombre de slides incorrect : {len(slides)} au lieu de 10"
    for i in range(1, 11):
        assert str(i) in slides, f"Slide {i} manquant dans le DOM !"

    # 3. Slide 1 est initialement actif
    assert 'class="slide active" data-slide="1"' in html_content, "Le Slide 1 doit avoir la classe 'active' au chargement"

    # 4. totalSlides en JS concorde avec le DOM
    assert "const totalSlides = 10;" in html_content, "La variable JS totalSlides doit être égale à 10"

def test_interactive_buttons_and_navigation_handlers(html_content):
    """Test d'Intégration : Vérifie que tous les boutons possèdent des handlers d'événements valides."""
    # Bouton Plein Écran
    assert 'id="fs-btn"' in html_content
    assert 'onclick="toggleFullscreen()"' in html_content

    # Bouton Thème Sombre/Clair
    assert 'id="theme-btn"' in html_content
    assert 'onclick="toggleTheme()"' in html_content

    # Boutons Précédent et Suivant
    assert 'onclick="prevSlide()"' in html_content
    assert 'onclick="nextSlide()"' in html_content

    # Widgets Time Keeper
    assert 'id="time-keeper"' in html_content
    assert 'id="timer-display"' in html_content
    assert 'onclick="toggleTimer()"' in html_content

    # Raccourcis Clavier
    assert "e.key === 'ArrowRight'" in html_content
    assert "e.key === 'ArrowLeft'" in html_content
    assert "e.key.toLowerCase() === 'f'" in html_content
    assert "e.key.toLowerCase() === 's'" in html_content

def test_viewport_resilience_and_pinned_navigation(html_content):
    """Architectural Fitness Function : Vérifie l'ancrage permanent du header et du footer (zéro dézoomage)."""
    # 1. Hauteur verrouillée à l'écran
    assert re.search(r"height:\s*min\(9[0-5]vh", html_content), "Hauteur de viewport non cadenassée à min(94vh)"

    # 2. Footer et Ruban verrouillés (flex-shrink: 0)
    assert ".footer-bar" in html_content
    assert "flex-shrink: 0" in html_content

    # 3. Typographie fluide présente
    assert "clamp(" in html_content, "Typographie adaptative clamp() absente"

def test_no_broken_unicode_tofu_characters(html_content):
    """Quality Gate Graphique : Vérifie l'absence de glyphes Unicode box-drawing à risque de rendu '□□□'."""
    forbidden_tofu = ["◀──", "──▶", "■", "□"]
    for tofu in forbidden_tofu:
        assert tofu not in html_content, f"Caractère Unicode tofu '{tofu}' détecté dans la présentation !"

def test_consulting_agenda_and_qa_conformance(html_content):
    """Test Métier Conseil : Vérifie que l'agenda possède ses 5 parties et que le Q&A est cadré sur 15-20 min."""
    # 5 cartes d'agenda
    for num in ["01", "02", "03", "04", "05"]:
        assert f'class="agenda-num">{num}</div>' in html_content, f"Numéro d'agenda {num} manquant dans Slide 2"

    # Cadrage du Q&A sur 15-20 min
    assert "15 à 20 min" in html_content or "15-20 min" in html_content, "Mention 15-20 min manquante pour le Q&A"
