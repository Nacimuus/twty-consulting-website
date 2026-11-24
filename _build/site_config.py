"""Coordonnées et réglages communs du site twty.fr."""

SITE = {
    "base_url": "https://www.twty.fr",
    "email": "contact@twty.fr",
    "whatsapp_url": "https://wa.me/33698563366",
    "linkedin_url": "https://www.linkedin.com/in/nacimuus/",
    "phone_ch": "+41 76 291 20 16",
    "phone_ma": "+212 7 74 17 41 15",
    # Lien de prise de rendez-vous (Calendly, Cal.com…). Laisser vide tant qu'il n'existe pas :
    # les boutons renvoient alors vers la page contact.
    "booking_url": "",
    "job_title_fr": "Expert en monétique et paiement électronique, formateur et enseignant",
    "knows_about": [
        "Monétique", "Paiement électronique", "EMV", "Certification EMV L1 L2 L3",
        "PCI DSS", "SoftPOS", "Paiement sans contact", "Terminal Management System (TMS)",
        "Certifications Visa, Mastercard, Amex, UPI", "Gestion de projet", "Formation professionnelle",
        "Ingénierie pédagogique", "Étude de marché", "Accompagnement de startups", "Soft skills",
    ],
    # Ajouter ici chaque profil public (page enseignant, Malt, conférences…) : c'est ce qui
    # permet à Google et aux IA de relier ces sources à la même personne.
    "same_as": [
        "https://www.linkedin.com/in/nacimuus/",
    ],
    # Anciennes URL -> nouvelles URL
    "redirects": {
        "services.html": "/",
        "payment-systems.html": "/expertise-paiement.html",
        "project-management.html": "/accompagnement-startup.html",
        "leadership.html": "/accompagnement-startup.html",
        "training.html": "/formations.html",
        "legal.html": "/mentions-legales.html",
    },
}
