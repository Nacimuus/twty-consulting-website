"""Contenu français de twty.fr (langue principale)."""
from parts import pay_card, page_hero, cta_band, mailto, faq_schema, faq_html, course_schema
from site_config import SITE

BASE = SITE["base_url"]

SLUGS = {
    "home": "index.html",
    "payment": "expertise-paiement.html",
    "training": "formations.html",
    "centres": "centres-de-formation.html",
    "startups": "accompagnement-startup.html",
    "about": "nacim-touenti.html",
    "contact": "contact.html",
    "legal": "mentions-legales.html",
}

UI = {
    "og_locale": "fr_FR",
    "og_alt": "Nacim Touenti, Twty Consulting : expertise paiement, formation et accompagnement de startups",
    "skip": "Aller au contenu",
    "menu": "Menu",
    "nav_label": "Navigation principale",
    "nav": [
        ("payment", "Expertise paiement"),
        ("training", "Formations"),
        ("centres", "Centres de formation"),
        ("startups", "Startups"),
        ("about", "À propos"),
    ],
    "lang_switch": "EN",
    "lang_title": "English version",
    "cta_contact": "Prendre contact",
    "footer_blurb": "Twty Consulting, le cabinet de Nacim Touenti : expertise en paiement électronique, formation et accompagnement de startups.",
    "footer_nav": "Le site",
    "footer_contact": "Contact",
    "footer_presence": "Présence",
    "tangier": "Tanger",
    "legal": "Mentions légales",
}

# Bio de référence : à recopier à l'identique sur LinkedIn, Malt, pages universités…
BIO_SHORT = (
    "Nacim Touenti est expert en monétique et en gestion de projet, enseignant et formateur, "
    "fondateur de Twty Consulting. Il accompagne entreprises, centres de formation et startups "
    "sur leurs projets de paiement et la montée en compétences de leurs équipes."
)

BIO_LONG = (
    "Nacim Touenti est expert en paiement électronique et en gestion de projet, enseignant et formateur, "
    "et fondateur de Twty Consulting. Il dirige la gestion de projets à l'échelle EMEA chez un acteur mondial "
    "des solutions de paiement, où il pilote le lancement de terminaux et de logiciels de paiement, "
    "leurs certifications EMV (L1, L2, L3), la conformité PCI DSS et les relations avec les schémas "
    "internationaux. Avec plus de dix ans d'expérience dans la fintech, le conseil et le déploiement "
    "international, en Europe comme en Afrique, il enseigne également à l'université et conçoit des "
    "programmes de formation. Avec Twty Consulting, présent à Paris, Zurich et Tanger, il accompagne "
    "entreprises, centres de formation et startups : expertise paiement, formation et accompagnement "
    "de projets, de produits et de stratégie commerciale."
)

ORG_DESCRIPTION = (
    "Cabinet de conseil et de formation fondé par Nacim Touenti : expertise en monétique et paiement "
    "électronique (EMV, PCI DSS, SoftPOS), formations pour entreprises et centres de formation, "
    "accompagnement de startups."
)

CONTACT = "/" + SLUGS["contact"]

# ---------------------------------------------------------------- Accueil
HOME_FAQ = [
    ("Intervenez-vous en présentiel ou à distance ?",
     "Les deux. J'interviens en présentiel à Paris, en Suisse et au Maroc, et à distance partout ailleurs."),
    ("Dans quelles langues travaillez-vous ?",
     "En français et en anglais, pour les formations comme pour les missions de conseil."),
    ("Vos formations peuvent-elles être financées ?",
     "Selon les cas : en intra-entreprise sur le budget formation de votre société, ou via un organisme de formation partenaire certifié Qualiopi pour un financement OPCO. Écrivez-moi pour trouver le bon montage."),
    ("Pouvez-vous adapter une formation à notre contexte ?",
     "Oui. Chaque formation intra est construite à partir de vos projets, de vos produits et de vos contraintes, avec des cas pratiques tirés de votre secteur."),
    ("Quel est le délai pour démarrer ?",
     "Un premier échange de 30 minutes peut se tenir dans la semaine. Il permet de cadrer le besoin et de vous envoyer une proposition."),
]

HOME = {
    "key": "home",
    "slug": SLUGS["home"],
    "title": "Nacim Touenti — Expert monétique, formateur et consultant | Twty Consulting",
    "description": "Nacim Touenti, expert en paiement électronique (EMV, PCI DSS, SoftPOS), enseignant et formateur. Conseil, formations et accompagnement de startups avec Twty Consulting.",
    "schema": [faq_schema(HOME_FAQ, "fr")],
    "body": f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Réussir vos projets de paiement. Faire grandir vos équipes.</h1>
      <p class="lead">Je suis Nacim Touenti, expert en monétique et en gestion de projet, enseignant et formateur. J'accompagne entreprises, centres de formation et startups, de la certification EMV à la montée en compétences de leurs équipes.</p>
      <div class="actions">
        <a class="btn" href="{CONTACT}">Prendre contact</a>
        <a class="btn btn--ghost" href="/{SLUGS['training']}">Voir les formations</a>
      </div>
    </div>
    {pay_card("Expertise", "Paiement, formation, startups", "Présence", "Paris  Zurich  Tanger")}
  </div>
</section>

<section class="proof" aria-label="En bref">
  <div class="wrap proof-grid">
    <div class="proof-item">
      <h4>Plus de 10 ans d'expérience</h4>
      <p>Fintech, conseil et déploiements internationaux en Europe et en Afrique.</p>
    </div>
    <div class="proof-item">
      <h4>EMV, PCI DSS, SoftPOS, TMS</h4>
      <p>Certifications L1 à L3 et schémas Visa, Mastercard, Amex, UPI.</p>
    </div>
    <div class="proof-item">
      <h4>Enseignant et formateur</h4>
      <p>Cours à l'université, programmes et formations sur mesure.</p>
    </div>
  </div>
</section>

<section class="section" id="offres">
  <div class="wrap">
    <div class="section-head">
      <h2>Trois façons de travailler ensemble</h2>
      <p>Une même exigence : des résultats concrets, transmis à vos équipes pour qu'ils durent.</p>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div>
          <h3>Paiement et monétique</h3>
          <p class="who">Banques, acquéreurs, PSP, fintechs, fabricants de terminaux</p>
        </div>
        <p class="problem">Votre terminal, votre application ou votre passerelle de paiement doit sortir à l'heure, sécurisé et certifié.</p>
        <div>
          <ul>
            <li>Diagnostic de projet paiement</li>
            <li>Accompagnement aux certifications EMV et schémas</li>
            <li>Pilotage de projet de transition</li>
          </ul>
          <a class="more" href="/{SLUGS['payment']}">Découvrir l'expertise paiement</a>
        </div>
      </article>
      <article class="offer-row">
        <div>
          <h3>Formation</h3>
          <p class="who">Entreprises, centres de formation, écoles et universités</p>
        </div>
        <p class="problem">Vos équipes ou vos apprenants ont besoin d'un intervenant qui pratique au quotidien ce qu'il enseigne.</p>
        <div>
          <ul>
            <li>Formations intra-entreprise</li>
            <li>Conception de modules et de programmes</li>
            <li>Masterclasses et interventions</li>
          </ul>
          <a class="more" href="/{SLUGS['training']}">Voir le catalogue</a>
        </div>
      </article>
      <article class="offer-row">
        <div>
          <h3>Accompagnement de startups</h3>
          <p class="who">Fondateurs, entrepreneurs, chefs de projet</p>
        </div>
        <p class="problem">Vous avez une idée ou un premier produit : il vous faut un cadre, une feuille de route et des ventes.</p>
        <div>
          <ul>
            <li>Programme Launch sur 3 mois</li>
            <li>Coaching de dirigeant et de chef de projet</li>
            <li>Redressement de projet en difficulté</li>
          </ul>
          <a class="more" href="/{SLUGS['startups']}">Voir l'accompagnement</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <h2>Pourquoi travailler avec moi</h2>
    </div>
    <div class="reasons">
      <div class="reason">
        <h3>Le terrain</h3>
        <p>Je pilote au quotidien des projets de paiement à l'échelle EMEA : terminaux, logiciels, certifications. Mes recommandations viennent de projets livrés.</p>
      </div>
      <div class="reason">
        <h3>La pédagogie</h3>
        <p>J'enseigne à l'université et je conçois des cours, des cas pratiques et des examens. Je rends un sujet technique clair et actionnable.</p>
      </div>
      <div class="reason">
        <h3>L'Europe et l'Afrique</h3>
        <p>J'ai mené des projets sur les deux continents, dont le déploiement d'un portefeuille mobile. Je connais les contraintes des marchés matures comme émergents.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Réalisations</h2>
      <p>Quelques projets représentatifs. Détails et références sur demande.</p>
    </div>
    <div class="cases">
      <article class="case"><span class="tag">Paiement</span><h3>Lancement de logiciel pour terminaux de paiement</h3><p>Déploiements internationaux avec mise en conformité locale et accompagnement complet à la certification L3.</p></article>
      <article class="case"><span class="tag">Paiement</span><h3>Certifications PCI, EMV et schémas</h3><p>Expertise en sécurité des paiements, PCI DSS et certifications auprès des schémas internationaux.</p></article>
      <article class="case"><span class="tag">Paiement</span><h3>Portefeuille mobile en Afrique</h3><p>Lancement d'outils financiers mobiles pour des populations peu bancarisées.</p></article>
      <article class="case"><span class="tag">Formation</span><h3>Conception de programmes universitaires</h3><p>Programmes construits autour de problématiques réelles d'entreprise.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Entrepreneur Week</h3><p>Ateliers organisés avec des universités et des entreprises pour stimuler l'innovation et l'entrepreneuriat.</p></article>
      <article class="case"><span class="tag">Formation</span><h3>Méthode Softies</h3><p>Méthode de développement des soft skills déployée dans plusieurs pays.</p></article>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div>
      <h2>Questions fréquentes</h2>
      <p class="lead">Une autre question ? <a href="{CONTACT}">Écrivez-moi</a>.</p>
    </div>
    <div class="faq">
      {faq_html(HOME_FAQ)}
    </div>
  </div>
</section>

{cta_band("Parlons de votre projet", "Un premier échange de 30 minutes, sans engagement, pour comprendre votre besoin et voir comment je peux vous aider.", "Prendre contact", CONTACT, "Écrire sur WhatsApp", SITE["whatsapp_url"])}
""",
}

# ---------------------------------------------------------------- Expertise paiement
PAYMENT = {
    "key": "payment",
    "slug": SLUGS["payment"],
    "title": "Consultant monétique et expert EMV, PCI DSS, SoftPOS | Nacim Touenti",
    "description": "Diagnostic de projet paiement, certifications EMV L1 à L3 et schémas (Visa, Mastercard, Amex, UPI), PCI DSS, SoftPOS et TMS. Conseil et pilotage par Nacim Touenti.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Expertise paiement',
        "Expertise paiement et monétique",
        "Je vous aide à lancer des terminaux, des applications et des services de paiement qui passent les certifications du premier coup et respectent les exigences de sécurité.",
        "expertise-paiement.webp",
        "Équipe projet autour d'un terminal de paiement et d'un tableau de flux de transactions EMV",
        f'<div class="actions"><a class="btn" href="{mailto("Demande de diagnostic projet paiement")}">Demander un diagnostic</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>Pour qui</h2>
      <p class="measure">Vous avez un projet de paiement en cours ou un objectif ambitieux, et vous voulez une intégration sans accroc et une conformité internationale.</p>
      <ul class="chips">
        <li>Banques</li><li>Acquéreurs</li><li>PSP et passerelles</li><li>Fintechs</li><li>Fabricants de terminaux</li><li>Éditeurs de logiciels</li>
      </ul>
    </div>
    <div>
      <h2>Domaines d'intervention</h2>
      <ul class="ticks">
        <li>Implémentation et certification EMV (L1, L2, L3)</li>
        <li>Certifications Visa, Mastercard, Amex, UPI et schémas locaux</li>
        <li>SoftPOS, sans contact et paiement par QR code</li>
        <li>Mise en place de systèmes de gestion de parc (TMS)</li>
        <li>APIs de paiement, logiciels et intégration de passerelles</li>
        <li>Audits de sécurité, gestion des clés, conformité PCI DSS</li>
        <li>Architectures SaaS et solutions sur mesure</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <h2>Trois formats de mission</h2>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Diagnostic projet paiement</h3><p class="who">2 à 5 jours</p></div>
        <p class="problem">Un regard expert sur votre projet avant qu'un retard de certification ne coûte cher.</p>
        <div><ul><li>Rapport d'écarts : certification, sécurité, planning</li><li>Feuille de route priorisée</li><li>Restitution à votre direction</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Pilotage de projet</h3><p class="who">Mission de quelques semaines à quelques mois</p></div>
        <p class="problem">Un chef de projet senior qui prend en main le lancement, les fournisseurs et les laboratoires de certification.</p>
        <div><ul><li>Gouvernance et reporting pour la direction</li><li>Coordination des équipes et des partenaires</li><li>Suivi des certifications jusqu'à l'obtention</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Formation des équipes</h3><p class="who">1 à 2 jours, intra-entreprise</p></div>
        <p class="problem">Des équipes produit, projet et support qui comprennent enfin la chaîne de paiement de bout en bout.</p>
        <div><ul><li>Fondamentaux de la monétique</li><li>Préparer une certification EMV et schémas</li></ul><a class="more" href="/{SLUGS['training']}">Voir les formations</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Comment se déroule un diagnostic</h2>
    </div>
    <ol class="steps">
      <li><h3>Cadrage</h3><p>Un échange de 30 minutes pour comprendre le projet, les échéances et les enjeux.</p></li>
      <li><h3>Analyse</h3><p>Revue de la documentation et entretiens avec vos équipes et vos partenaires.</p></li>
      <li><h3>Écarts</h3><p>Identification des risques : certification, sécurité, planning, organisation.</p></li>
      <li><h3>Restitution</h3><p>Rapport et feuille de route priorisée, présentés à vos décideurs.</p></li>
    </ol>
  </div>
</section>

{cta_band("Un projet de paiement à sécuriser ?", "Décrivez-moi votre projet et vos échéances : je vous réponds avec une proposition de diagnostic.", "Demander un diagnostic", mailto("Demande de diagnostic projet paiement"), "Prendre contact", CONTACT)}
""",
}

# ---------------------------------------------------------------- Formations
COURSES = [
    {
        "id": "fondamentaux-monetique",
        "name": "Fondamentaux de la monétique : EMV, PCI DSS, SoftPOS",
        "desc": "Comprendre la chaîne de paiement par carte de bout en bout, de la puce EMV à l'acquisition, et les exigences de sécurité PCI DSS.",
        "for": "Équipes produit, projet, commerciales et support d'entreprises du paiement ou de la fintech",
        "goals": [
            "Expliquer le parcours d'une transaction carte, du terminal à l'émetteur",
            "Comprendre EMV, le sans contact, le SoftPOS et la tokenisation",
            "Situer les exigences PCI DSS et leurs impacts sur un projet",
            "Dialoguer efficacement avec experts, laboratoires et schémas",
        ],
        "duration": "2 jours (14 h)",
        "format": "Intra-entreprise, présentiel ou distanciel",
    },
    {
        "id": "certification-emv",
        "name": "Préparer une certification EMV et schémas",
        "desc": "Planifier et réussir les certifications EMV L1, L2, L3 et les certifications Visa, Mastercard, Amex et UPI.",
        "for": "Chefs de projet, ingénieurs et responsables qualité de fabricants, PSP et éditeurs",
        "goals": [
            "Connaître les étapes et les acteurs de chaque niveau de certification",
            "Construire un planning réaliste et anticiper les points de blocage",
            "Préparer la documentation et les campagnes de tests",
        ],
        "duration": "1 jour (7 h)",
        "format": "Intra-entreprise, présentiel ou distanciel",
    },
    {
        "id": "gestion-de-projet",
        "name": "Gestion de projet hybride pour équipes tech",
        "desc": "Combiner agilité et jalons de conformité pour livrer des projets techniques à l'heure.",
        "for": "Chefs de projet, product owners, managers d'équipes techniques",
        "goals": [
            "Choisir et adapter une méthode agile ou hybride à son contexte",
            "Maîtriser le périmètre et aligner les parties prenantes",
            "Produire un reporting utile aux décideurs",
            "Redresser un projet en difficulté",
        ],
        "duration": "2 jours (14 h)",
        "format": "Intra ou inter-entreprise, présentiel ou distanciel",
    },
    {
        "id": "etude-de-marche",
        "name": "Étude de marché et logique Test & Learn",
        "desc": "Utiliser l'étude de marché comme outil d'aide à la décision et éviter les pièges classiques d'interprétation.",
        "for": "Entrepreneurs, étudiants, équipes marketing et innovation",
        "goals": [
            "Formuler les bonnes questions avant de collecter des données",
            "Éviter les pièges de causalité dans l'analyse",
            "Tester vite et à moindre coût avec une démarche Lean",
        ],
        "duration": "1 jour (7 h), déclinable en module universitaire",
        "format": "Écoles, universités, incubateurs, entreprises",
    },
    {
        "id": "soft-skills-softies",
        "name": "Soft skills et leadership : la méthode Softies",
        "desc": "Développer communication, négociation, intelligence émotionnelle et leadership par la mise en situation.",
        "for": "Managers, équipes projet, étudiants et jeunes diplômés",
        "goals": [
            "Prendre la parole et convaincre avec clarté",
            "Négocier et gérer les tensions en équipe",
            "Développer un leadership adapté à sa personnalité",
        ],
        "duration": "1 jour ou parcours modulable",
        "format": "Présentiel de préférence, jeux de rôle et serious games",
    },
]


def course_html(c):
    goals = "".join(f"<li>{g}</li>" for g in c["goals"])
    return f"""<article class="course" id="{c['id']}">
  <div>
    <h3>{c['name']}</h3>
    <p>{c['desc']}</p>
    <h4>Objectifs</h4>
    <ul>{goals}</ul>
    <a class="more" href="{mailto('Programme détaillé : ' + c['name'])}">Demander le programme détaillé</a>
  </div>
  <dl>
    <dt>Public</dt><dd>{c['for']}</dd>
    <dt>Durée</dt><dd>{c['duration']}</dd>
    <dt>Format</dt><dd>{c['format']}</dd>
    <dt>Tarif</dt><dd>Sur devis, selon le format et le nombre de participants</dd>
  </dl>
</article>"""


TRAINING = {
    "key": "training",
    "slug": SLUGS["training"],
    "title": "Formations monétique, EMV, PCI DSS et gestion de projet | Nacim Touenti",
    "description": "Formations en monétique (EMV, PCI DSS, SoftPOS), certification, gestion de projet, étude de marché et soft skills. Intra-entreprise, présentiel ou distanciel, par Nacim Touenti.",
    "schema": [course_schema(c["name"], c["desc"], "fr", f"{BASE}/{SLUGS['training']}#{c['id']}") for c in COURSES],
    "body": page_hero(
        '<a href="/">Accueil</a> / Formations',
        "Formations",
        "Des formations construites par un praticien qui enseigne : on apprend en faisant, sur des cas réels, et on repart avec des outils utilisables dès le lendemain.",
        "formation.webp",
        "Session de formation interactive en petit groupe",
        f'<div class="actions"><a class="btn" href="#catalogue">Voir le catalogue</a><a class="btn btn--ghost" href="{CONTACT}">Demander une formation sur mesure</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>Ma façon de former</h2>
      <p class="measure">Pas de cours magistral ni de diaporama sans fin. Les participants négocient, présentent, décident et parfois se trompent, volontairement : c'est ainsi qu'on progresse.</p>
    </div>
    <ul class="ticks">
      <li><b>Apprendre en faisant</b> : mises en situation, études de cas, simulations</li>
      <li><b>Serious games</b> : des jeux qui enseignent et qui engagent</li>
      <li><b>Prendre du recul</b> : un débrief après chaque exercice pour ancrer les acquis</li>
      <li><b>Outils interactifs</b> : sondages, quiz, tableaux Miro et Trello</li>
    </ul>
  </div>
</section>

<section class="section section--mist" id="catalogue">
  <div class="wrap">
    <div class="section-head">
      <h2>Catalogue</h2>
      <p>Chaque formation est adaptable : durée, niveau, exemples tirés de votre secteur.</p>
    </div>
    {"".join(course_html(c) for c in COURSES)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Comment je construis une formation</h2>
    </div>
    <ol class="steps">
      <li><h3>Conception</h3><p>Des modules immersifs et réalistes, construits avec vous autour de vos objectifs.</p></li>
      <li><h3>Test pilote</h3><p>Un essai avec de vrais participants pour affiner les exercices.</p></li>
      <li><h3>Validation</h3><p>Relecture par des experts et ajustements selon les retours.</p></li>
      <li><h3>Animation</h3><p>Sessions en présentiel ou à distance, avec évaluation des acquis.</p></li>
    </ol>
  </div>
</section>

{cta_band("Une formation pour votre équipe ?", "Dites-moi qui vous voulez former, sur quoi et dans quel délai : je vous envoie une proposition de programme.", "Demander une formation", CONTACT, "Vous êtes un centre de formation", "/" + SLUGS["centres"])}
""",
}

# ---------------------------------------------------------------- Centres de formation
CENTRES = {
    "key": "centres",
    "slug": SLUGS["centres"],
    "title": "Formateur expert pour centres de formation et écoles | Nacim Touenti",
    "description": "Intervenant et concepteur de programmes pour centres de formation, écoles et universités : paiement et fintech, gestion de projet, étude de marché, entrepreneuriat, soft skills.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Centres de formation',
        "Pour les centres de formation, écoles et universités",
        "Vous cherchez un intervenant expert, capable de concevoir un module complet et de l'animer avec exigence. J'apporte la double casquette de praticien du paiement et d'enseignant.",
        "centres.webp",
        "Formateur animant un atelier participatif",
        f'<div class="actions"><a class="btn" href="{mailto("Proposition d intervention")}">Proposer une intervention</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>Ce que je vous apporte</h2>
      <ul class="ticks">
        <li><b>Interventions</b> : modules courts, masterclasses, conférences métiers</li>
        <li><b>Conception clés en main</b> : syllabus, supports, cas pratiques, évaluations</li>
        <li><b>Examens et cas pratiques</b> alignés sur les concepts du cours</li>
        <li><b>Jurys et accompagnement</b> de projets étudiants ou entrepreneuriaux</li>
      </ul>
    </div>
    <div>
      <h2>Sujets enseignés</h2>
      <ul class="chips">
        <li>Monétique et paiement électronique</li><li>Fintech</li><li>Gestion de projet</li><li>Méthodes agiles</li>
        <li>Étude de marché</li><li>Lean et Test &amp; Learn</li><li>Entrepreneuriat</li><li>Leadership</li><li>Soft skills</li>
      </ul>
      <p class="measure" style="margin-top:24px">Exemple : un examen d'étude de marché construit autour d'une startup fictive, qui évalue les pièges de causalité, la logique Test &amp; Learn et le rôle de l'étude de marché dans la décision.</p>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <h2>Notre collaboration, étape par étape</h2>
    </div>
    <ol class="steps">
      <li><h3>Besoin</h3><p>Public, objectifs pédagogiques, volume horaire et contraintes du référentiel.</p></li>
      <li><h3>Proposition</h3><p>Programme détaillé, modalités d'évaluation et devis.</p></li>
      <li><h3>Production</h3><p>Supports, cas pratiques et évaluations livrés dans vos formats.</p></li>
      <li><h3>Animation et bilan</h3><p>Sessions, évaluation des acquis et retour d'expérience pour la session suivante.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap measure">
    <h2>Financement et cadre administratif</h2>
    <p>J'interviens en sous-traitance de votre organisme, qui conserve la relation avec les financeurs. Je vous fournis tous les éléments nécessaires à votre démarche qualité : programme, objectifs, modalités d'évaluation, CV de l'intervenant.</p>
  </div>
</section>

{cta_band("Un module à concevoir ou à animer ?", "Envoyez-moi le thème, le public et le calendrier : je reviens vers vous avec une proposition.", "Proposer une intervention", mailto("Proposition d intervention"), "Voir le catalogue", "/" + SLUGS["training"])}
""",
}

# ---------------------------------------------------------------- Startups
STARTUPS = {
    "key": "startups",
    "slug": SLUGS["startups"],
    "title": "Accompagnement de startups : projet, produit, ventes | Nacim Touenti",
    "description": "Programme Launch sur 3 mois, coaching de dirigeant et de chef de projet, redressement de projet. Accompagnement de startups et d'entrepreneurs par Nacim Touenti.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Startups',
        "Accompagnement de startups et d'entrepreneurs",
        "Passer de l'idée à l'exécution demande un cadre, des priorités claires et quelqu'un qui a déjà livré. Je vous aide à structurer votre projet, votre produit et vos ventes.",
        "startups.webp",
        "Équipe de startup travaillant sur une feuille de route",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Réserver un appel découverte</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Trois formats</h2>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Programme Launch</h3><p class="who">3 mois, une séance par semaine</p></div>
        <p class="problem">Pour les startups en phase de lancement qui doivent tout cadrer en même temps.</p>
        <div><ul><li>Cadrage du projet et feuille de route</li><li>Produit : priorités, tests, premières versions</li><li>Go-to-market : cible, offre, pitch, plan commercial</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Coaching individuel</h3><p class="who">Pack de séances, première séance offerte</p></div>
        <p class="problem">Pour un fondateur ou un chef de projet qui veut prendre de meilleures décisions, plus vite.</p>
        <div><ul><li>Clarifier sa vision et sa prochaine étape</li><li>Communication et influence</li><li>Leadership en croissance comme en crise</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Redressement de projet</h3><p class="who">Mission courte</p></div>
        <p class="problem">Pour un projet qui dérape : délais, périmètre, équipe ou relation client.</p>
        <div><ul><li>Diagnostic rapide et plan de reprise</li><li>Recadrage du périmètre et des parties prenantes</li><li>Mise en place d'outils adaptés (Jira, Notion, ClickUp…)</li></ul></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div>
      <h2>Ce que je privilégie</h2>
      <ul class="ticks">
        <li>Un pilotage stratégique, pas seulement l'exécution de tâches</li>
        <li>Des méthodes agiles ou hybrides adaptées à votre équipe</li>
        <li>Des résultats mesurables, pas seulement des livrables</li>
        <li>Un reporting qui aide vraiment à décider</li>
      </ul>
    </div>
    <div>
      <h2>Ce que j'évite</h2>
      <ul class="ticks cross">
        <li>Les méthodes génériques plaquées sans adaptation</li>
        <li>La documentation qui ne sert à personne</li>
        <li>Les rôles flous et la communication dispersée</li>
        <li>Le reporting identique pour tous les publics</li>
      </ul>
    </div>
  </div>
</section>

{cta_band("Votre projet mérite un cadre solide", "Un appel découverte de 30 minutes pour faire le point sur votre situation et voir le format qui vous convient.", "Réserver un appel découverte", CONTACT, "Écrire sur WhatsApp", SITE["whatsapp_url"])}
""",
}

# ---------------------------------------------------------------- À propos
ABOUT = {
    "key": "about",
    "slug": SLUGS["about"],
    "page_type": "ProfilePage",
    "title": "Nacim Touenti — Expert paiement, enseignant et fondateur de Twty Consulting",
    "description": "Qui est Nacim Touenti ? Expert en monétique et gestion de projet, enseignant à l'université, formateur et fondateur de Twty Consulting (Paris, Zurich, Tanger).",
    "body": f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/">Accueil</a> / À propos</p>
    <div class="about-grid">
      <div class="portrait" role="img" aria-label="Portrait de Nacim Touenti (photo à venir)">NT</div>
      <div>
        <h1>Nacim Touenti</h1>
        <p class="lead">Expert en paiement électronique et en gestion de projet, enseignant et formateur, fondateur de Twty Consulting.</p>
        <p class="measure">{BIO_LONG}</p>
        <dl class="facts">
          <dt>Spécialités</dt><dd>Monétique, EMV, PCI DSS, SoftPOS, TMS, gestion de projet</dd>
          <dt>Enseignement</dt><dd>Université et formation professionnelle</dd>
          <dt>Langues</dt><dd>Français, anglais</dd>
          <dt>Présence</dt><dd>Paris – La Défense, Zurich, Tanger</dd>
          <dt>Profil</dt><dd><a href="{SITE['linkedin_url']}" rel="me noopener">LinkedIn</a></dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Trois métiers, une même ligne</h2>
      <p>Faire réussir les projets et faire grandir les personnes qui les portent.</p>
    </div>
    <div class="reasons">
      <div class="reason"><h3>Praticien du paiement</h3><p>Lancement de terminaux et de logiciels, certifications EMV et schémas, conformité PCI DSS, déploiements en Europe et en Afrique.</p></div>
      <div class="reason"><h3>Enseignant et formateur</h3><p>Cours à l'université, conception de programmes, d'examens et de cas pratiques, formations en entreprise.</p></div>
      <div class="reason"><h3>Entrepreneur</h3><p>Fondateur de Twty Consulting, mentor d'entrepreneurs, créateur de la méthode Softies et organisateur d'Entrepreneur Week.</p></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap measure">
    <h2>Twty Consulting</h2>
    <p>{ORG_DESCRIPTION} Le cabinet intervient en France, en Suisse, au Maroc et plus largement en Europe et en Afrique, en français et en anglais.</p>
    <div class="actions"><a class="btn" href="{CONTACT}">Prendre contact</a><a class="btn btn--ghost" href="{SITE['linkedin_url']}" rel="me noopener">Suivre sur LinkedIn</a></div>
  </div>
</section>
""",
}

# ---------------------------------------------------------------- Contact
CONTACT_PAGE = {
    "key": "contact",
    "slug": SLUGS["contact"],
    "page_type": "ContactPage",
    "title": "Contact — Nacim Touenti | Twty Consulting",
    "description": "Contactez Nacim Touenti pour un projet de paiement, une formation ou un accompagnement de startup. Email, WhatsApp, LinkedIn. Paris, Zurich, Tanger.",
    "body": f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/">Accueil</a> / Contact</p>
    <h1>Parlons de votre projet</h1>
    <p class="lead">Décrivez votre besoin en quelques lignes. Je vous réponds avec une proposition d'échange de 30 minutes.</p>
  </div>
</section>
<section class="section">
  <div class="wrap contact-grid">
    <form class="form" id="contact-form" data-email="{SITE['email']}" data-subject="Demande via twty.fr">
      <div class="row">
        <label>Nom<input name="nom" autocomplete="name" required></label>
        <label>Email<input name="email" type="email" autocomplete="email" required></label>
      </div>
      <div class="row">
        <label>Organisation<input name="organisation" autocomplete="organization"></label>
        <label>Votre besoin
          <select name="besoin">
            <option>Projet de paiement</option>
            <option>Formation pour mon équipe</option>
            <option>Intervention en centre de formation ou école</option>
            <option>Accompagnement de startup</option>
            <option>Autre</option>
          </select>
        </label>
      </div>
      <label>Message<textarea name="message" rows="6" required></textarea></label>
      <div><button class="btn" type="submit">Préparer l'email</button></div>
      <p class="hint">Le bouton ouvre votre messagerie avec votre message prêt à envoyer à {SITE['email']}.</p>
    </form>
    <aside>
      <ul class="channels">
        <li><b>Email</b><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
        <li><b>WhatsApp</b><a href="{SITE['whatsapp_url']}" rel="noopener">Écrire sur WhatsApp</a></li>
        <li><b>LinkedIn</b><a href="{SITE['linkedin_url']}" rel="me noopener">Nacim Touenti</a></li>
      </ul>
      <div class="offices">
        <p><b>Paris – La Défense</b><br>Courbevoie, France</p>
        <p><b>Zurich</b><br>Wallisellen, Suisse<br><a href="tel:{SITE['phone_ch'].replace(' ', '')}">{SITE['phone_ch']}</a></p>
        <p><b>Tanger</b><br>Maroc<br><a href="tel:{SITE['phone_ma'].replace(' ', '')}">{SITE['phone_ma']}</a></p>
      </div>
    </aside>
  </div>
</section>
""",
}

# ---------------------------------------------------------------- Mentions légales
LEGAL = {
    "key": "legal",
    "slug": SLUGS["legal"],
    "title": "Mentions légales | Twty Consulting",
    "description": "Mentions légales et politique de confidentialité du site twty.fr.",
    "body": f"""
<section class="section">
  <div class="wrap legal">
    <h1>Mentions légales</h1>
    <h2>Éditeur du site</h2>
    <p>Twty Consulting — [forme juridique et numéro SIREN à compléter]<br>
    Responsable de la publication : Nacim Touenti<br>
    Adresse : [adresse du siège à compléter]<br>
    Email : <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
    <h2>Hébergement</h2>
    <p>GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
    <h2>Propriété intellectuelle</h2>
    <p>Les textes, visuels, logos et contenus de ce site sont la propriété de Twty Consulting, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
    <h2>Données personnelles</h2>
    <p>Le site ne stocke aucune donnée saisie : le formulaire de contact prépare un email dans votre propre messagerie. Les emails reçus servent uniquement à répondre à votre demande et ne sont jamais cédés. Conformément au RGPD, vous pouvez demander l'accès, la rectification ou la suppression de vos données en écrivant à <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
    <h2>Cookies</h2>
    <p>Ce site n'utilise ni cookie publicitaire ni outil de mesure d'audience. Les polices de caractères sont chargées depuis Google Fonts, ce qui transmet votre adresse IP à Google lors de l'affichage des pages.</p>
  </div>
</section>
""",
}

NOT_FOUND = {
    "key": "404",
    "slug": "404.html",
    "noindex": True,
    "title": "Page introuvable | Twty Consulting",
    "description": "Cette page n'existe pas ou a été déplacée.",
    "body": f"""
<section class="section center-404">
  <div class="wrap measure">
    <h1>Cette page n'existe pas</h1>
    <p class="lead">Elle a peut-être été déplacée lors de la refonte du site. / This page may have moved.</p>
    <div class="actions"><a class="btn" href="/">Retour à l'accueil</a><a class="btn btn--ghost" href="/en/">English site</a></div>
  </div>
</section>
""",
}

PAGES = [HOME, PAYMENT, TRAINING, CENTRES, STARTUPS, ABOUT, CONTACT_PAGE, LEGAL, NOT_FOUND]

LLMS_TXT = f"""
# Twty Consulting — Nacim Touenti

> {BIO_SHORT}

{BIO_LONG}

## Offres
- [Expertise paiement et monétique]({BASE}/expertise-paiement.html) : diagnostic de projet paiement, certifications EMV L1/L2/L3 et schémas (Visa, Mastercard, Amex, UPI), PCI DSS, SoftPOS, TMS, pilotage de projet.
- [Formations]({BASE}/formations.html) : fondamentaux de la monétique, préparation aux certifications, gestion de projet hybride, étude de marché et Test & Learn, soft skills (méthode Softies).
- [Centres de formation et écoles]({BASE}/centres-de-formation.html) : interventions, conception de modules et de programmes, examens et cas pratiques.
- [Accompagnement de startups]({BASE}/accompagnement-startup.html) : programme Launch sur 3 mois, coaching, redressement de projet.

## Personne
- [À propos de Nacim Touenti]({BASE}/nacim-touenti.html)
- LinkedIn : {SITE['linkedin_url']}
- Contact : {SITE['email']}
- Présence : Paris – La Défense, Zurich, Tanger. Langues : français, anglais.

## English
- [English version]({BASE}/en/)
"""
