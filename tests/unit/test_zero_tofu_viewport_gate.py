import pytest
from src.tools.presales_linters import ZeroTofuViewportGate

def test_zero_tofu_gate_detects_broken_unicode():
    """Vérifie que les glyphes Unicode box-drawing à risque de rendu tofu sont interceptés."""
    bad_arrow_label = "◀── Remontée Alerte Terrain ──▶"
    res = ZeroTofuViewportGate.check_string_for_tofu(bad_arrow_label)
    assert res["valid"] is False
    assert "◀" in res["detected_tofu_glyphs"]
    assert "─" in res["detected_tofu_glyphs"]
    assert "▶" in res["detected_tofu_glyphs"]

def test_zero_tofu_gate_allows_clean_ascii():
    """Vérifie qu'un libellé propre en pur ASCII est validé."""
    clean_label = "Flux Retour : Remontee d'Alerte Terrain [mTLS 1.3]"
    res = ZeroTofuViewportGate.check_string_for_tofu(clean_label)
    assert res["valid"] is True
    assert len(res["detected_tofu_glyphs"]) == 0

def test_viewport_resilience_gate_checks_html():
    """Vérifie que la Quality Gate valide un gabarit avec height locked et barres verrouillées."""
    valid_html = """
    <style>
      #slide-viewport {
        height: min(94vh, 880px);
        overflow: hidden;
      }
      .progress-ribbon {
        flex-shrink: 0;
      }
      .footer-bar {
        flex-shrink: 0;
      }
    </style>
    <div id="slide-viewport">
      <div class="progress-ribbon"></div>
      <div class="slide"></div>
      <div class="footer-bar"></div>
    </div>
    """
    res = ZeroTofuViewportGate.check_html_viewport_resilience(valid_html)
    assert res["valid"] is True
    assert res["checks"]["has_viewport_height_lock"] is True
    assert res["checks"]["has_footer_locked"] is True
    assert res["checks"]["has_ribbon_locked"] is True
    assert res["checks"]["has_no_orphan_div_closing"] is True
