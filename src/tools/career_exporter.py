from pathlib import Path
from typing import List, Optional

class CareerExporter:
    """
    Outil de valorisation professionnelle pour l'Agent Carrière & Personal Branding (Brique 5.2).
    Met à jour le profil de compétences du CV et génère des brouillons de posts LinkedIn (REX).
    """

    def generate_cv_bullet_points(self, study_title: str, patterns_applied: List[str]) -> List[str]:
        """
        Extrait et formate les compétences techniques clés sous forme d'entrées pour CV.
        """
        bullets = []
        for pattern in patterns_applied:
            bullets.append(f"• Conçu et cadré l'architecture '{study_title}' en appliquant : {pattern}.")
        return bullets

    def generate_linkedin_post(
        self,
        author_name: str,
        study_title: str,
        key_results: List[str],
        certifications_alignment: Optional[List[str]] = None
    ) -> str:
        """
        Génère un brouillon de post LinkedIn (REX - Retour d'Expérience)
        adoptant un ton professionnel, naturel et percutant.
        """
        cert_line = ""
        if certifications_alignment:
            cert_line = f"\n🎯 Alignement méthodologique : {', '.join(certifications_alignment)}\n"

        results_formatted = "\n".join([f"👉 {res}" for res in key_results])

        post = f"""🚀 [REX Architecture] — {study_title}

Partage d'expérience sur notre récent chantier de cadrage d'architecture :

Comment moderniser un socle critique sans compromettre la sécurité ni la performance ?

Voici les 3 piliers structurants que nous avons appliqués avec succès :
{results_formatted}
{cert_line}
💡 Le plus grand enseignement : en architecture, la simplicité (KISS/YAGNI) et la testabilité unitaire déterministe (0 token) restent nos meilleurs alliés face à la complexité des plateformes modernes.

Et vous, comment gérez-vous l'étanchéité de vos modèles décisionnels en environnement Cloud ? Échangeons en commentaires !

#Architecture #EnterpriseArchitecture #CloudWAF #SoftwareCraftsmanship #SAFe #FinOps #ZeroTrust
"""
        return post.strip()
