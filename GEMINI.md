# 🏛️ GEMINI Context: my-agentic-architecture

## 📋 Purpose & Identity
Ce dépôt est un projet personnel open-source d'ingénierie d'architecture augmentée par intelligence artificielle multi-agents (CrewAI, Hexagonale pure, 100% TDD déterministe à 0 token).

---

## 🎯 Mandats & Standards d'Architecture d'Élite

1. **Architecture Hexagonale Pure & Découplage 0-Token :**
   - Les outils déterministes sous `src/tools/` ne doivent JAMAIS importer d'orchestres ou de dépendances LLM.
   - Testabilité déterministe à 100% sans mocks instables.

2. **Standard Universel Livrable « Pocket Guide Mobile Haute Couture (7 Piliers) » :**
   - Pour TOUTE restitution orale, soutenance (Board, L2, avant-vente) ou keynote, la brigade d'orateurs et les outils déterministes (`ExecutivePrompterExporter`) doivent obligatoirement être capables de générer et valider un **Pocket Guide Mobile** (`.html` responsive et export PDF A4 portrait) respectant la structure en 7 piliers :
     1. **Barre d'action sticky :** `🖨️ PDF`, `🌟 Guide STAR`, `🎭 Coaching Acteur`, `🎙️ Pitch`, `❓ Q&A`, `🧘 Mental`.
     2. **En-tête & KPI Grid :** Métriques d'envergure et volumétries clés.
     3. **Masterclass STAR :** Décodage complet S-T-A-R, tableau d'évaluation et cartographie des slides.
     4. **Masterclass Acteur Pro, Mémorisation & Vente :**
        - Plan d'action d'échauffement en 4 étapes (Ancrage 4-4-6, Stylo, Italienne réflexe, Incarnation scénique).
        - Mindset de vente consultative (Risk Mitigation, Imputabilité, ROI) & tableau comparative *Candidat* vs *Souverain*.
        - Secrets de comédiens (L'Italienne, Palais de mémoire 8 salles, Trigger Words 3 par slide).
        - Tableau Stanislavski du Sous-Texte secret par slide.
        - Voix FBI Chris Voss *Late-Night FM DJ* (intonation descendante ↘, 3 gestes).
        - Riposte Q&A en 3 temps (*Acknowledge ➔ Reframe ➔ Deliver* + silence final).
     5. **Mental & Sophrologie :** Cohérence cardiaque 4-4-6, posture Hassan II, routine 30 min/jour, mantra de souveraineté.
     6. **Pitch Mot-à-Mot STAR chronométré :** Badges `[S]`, `[T]`, `[A]`, `[R]`, didascalies scéniques et traduction FR.
     7. **Top 10 Questions Pièges :** En anglais avec réponses modèles et décodage stratégique.
   - Validation automatisée via `ExecutivePrompterExporter.validate_pocket_guide_structure()`.

3. **Vérification Systématique TDD :**
   - Toujours exécuter `pytest tests/unit` et s'assurer que 100% des tests sont verts avant tout commit.
