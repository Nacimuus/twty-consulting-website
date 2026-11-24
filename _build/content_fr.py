"""Contenu français de twty.fr (langue principale).

Positionnement : formation, coaching et accompagnement. L'expérience de management de projets
internationaux (fintech, paiement électronique) sert de preuve de légitimité, pas d'offre principale.
"""
from parts import hero_portrait, page_hero, cta_band, mailto, faq_schema, faq_html, course_schema
from site_config import SITE

BASE = SITE["base_url"]

SLUGS = {
    "home": "index.html",
    "training": "formations.html",
    "coaching": "coaching.html",
    "startups": "accompagnement-startup.html",
    "centres": "centres-de-formation.html",
    "about": "nacim-touenti.html",
    "contact": "contact.html",
    "legal": "mentions-legales.html",
}

UI = {
    "og_locale": "fr_FR",
    "og_alt": "Nacim Touenti, Twty Consulting : formation, coaching et accompagnement de startups",
    "skip": "Aller au contenu",
    "menu": "Menu",
    "nav_label": "Navigation principale",
    "nav": [
        ("training", "Formations"),
        ("coaching", "Coaching"),
        ("startups", "Startups"),
        ("centres", "Centres de formation"),
        ("about", "À propos"),
    ],
    "lang_switch": "EN",
    "lang_title": "English version",
    "cta_contact": "Prendre contact",
    "footer_blurb": "Twty Consulting, le cabinet de Nacim Touenti : formation, coaching et accompagnement de startups et d'entrepreneurs.",
    "footer_nav": "Le site",
    "footer_contact": "Contact",
    "footer_presence": "Présence",
    "tangier": "Tanger",
    "legal": "Mentions légales",
}

# Bio de référence : à recopier à l'identique sur LinkedIn, Malt, pages universités…
BIO_SHORT = (
    "Nacim Touenti est formateur, coach et enseignant à l'université, fondateur de Twty Consulting. "
    "Il accompagne entreprises, centres de formation, startups et entrepreneurs, en s'appuyant sur plus "
    "de dix ans de management de projets internationaux."
)

BIO_LONG = (
    "Nacim Touenti est formateur, coach et enseignant à l'université, et fondateur de Twty Consulting. "
    "Il conçoit et anime des formations en gestion de projet, leadership, soft skills, étude de marché "
    "et entrepreneuriat, coache dirigeants, managers et jeunes diplômés, et accompagne startups et "
    "entrepreneurs de l'idée au lancement. Sa pédagogie s'appuie sur plus de dix ans de management de "
    "projets internationaux dans la fintech et le paiement électronique, en Europe et en Afrique : il "
    "dirige aujourd'hui la gestion de projets à l'échelle EMEA pour un acteur mondial du secteur. Il est "
    "aussi le créateur de la méthode Softies de développement des soft skills et l'organisateur "
    "d'ateliers Entrepreneur Week avec des universités et des entreprises. Twty Consulting intervient "
    "depuis Paris, Zurich et Tanger, en français et en anglais."
)

ORG_DESCRIPTION = (
    "Cabinet de formation, de coaching et d'accompagnement fondé par Nacim Touenti : formations pour "
    "entreprises et centres de formation, coaching individuel, accompagnement de startups et d'entrepreneurs."
)

CONTACT = "/" + SLUGS["contact"]

# ---------------------------------------------------------------- Accueil
HOME_FAQ = [
    ("Intervenez-vous en présentiel ou à distance ?",
     "Les deux. J'interviens en présentiel à Paris, en Suisse et au Maroc, et à distance partout ailleurs."),
    ("Dans quelles langues travaillez-vous ?",
     "En français et en anglais, pour les formations comme pour le coaching."),
    ("Vos formations peuvent-elles être financées ?",
     "Selon les cas : en intra-entreprise sur le budget formation de votre société, ou via un organisme de formation partenaire certifié Qualiopi pour un financement OPCO. Écrivez-moi pour trouver le bon montage."),
    ("Comment se passe la première séance de coaching ?",
     "Elle est offerte. Nous faisons le point sur votre situation et vos objectifs, et vous repartez avec une première piste concrète, que vous poursuiviez ou non."),
    ("Quel est le délai pour démarrer ?",
     "Un premier échange de 30 minutes peut se tenir dans la semaine. Il permet de cadrer le besoin et de vous envoyer une proposition."),
]

HOME = {
    "key": "home",
    "slug": SLUGS["home"],
    "title": "Nacim Touenti — Formateur, coach et enseignant | Twty Consulting",
    "description": "Nacim Touenti, formateur, coach et enseignant à l'université. Formations, coaching et accompagnement de startups, avec plus de 10 ans de management de projets internationaux.",
    "schema": [faq_schema(HOME_FAQ, "fr")],
    "body": f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Former, coacher, accompagner. Faire grandir les personnes et leurs projets.</h1>
      <p class="lead">Je suis Nacim Touenti, formateur, coach et enseignant à l'université. J'accompagne entreprises, centres de formation, startups et entrepreneurs avec l'expérience d'un manager qui pilote des projets internationaux au quotidien.</p>
      <div class="actions">
        <a class="btn" href="{CONTACT}">Prendre contact</a>
        <a class="btn btn--ghost" href="/{SLUGS['training']}">Voir les formations</a>
      </div>
    </div>
    {hero_portrait("Portrait de Nacim Touenti (photo à venir)", ["Formateur", "Coach", "Enseignant à l'université"], "Paris, Zurich, Tanger")}
  </div>
</section>

<section class="proof" aria-label="En bref">
  <div class="wrap proof-grid">
    <div class="proof-item">
      <h4>Plus de 10 ans de management</h4>
      <p>Projets internationaux en Europe et en Afrique, dans la fintech et le paiement électronique.</p>
    </div>
    <div class="proof-item">
      <h4>Enseignant à l'université</h4>
      <p>Cours, programmes, cas pratiques et examens conçus et animés.</p>
    </div>
    <div class="proof-item">
      <h4>Créateur de la méthode Softies</h4>
      <p>Développement des soft skills, déployé dans plusieurs pays.</p>
    </div>
  </div>
</section>

<section class="section" id="offres">
  <div class="wrap">
    <div class="section-head">
      <h2>Trois façons de travailler ensemble</h2>
      <p>Une même exigence : des progrès visibles, qui durent après mon intervention.</p>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div>
          <h3>Formation</h3>
          <p class="who">Entreprises, centres de formation, écoles et universités</p>
        </div>
        <p class="problem">Vos équipes ou vos apprenants ont besoin d'un formateur qui pratique au quotidien ce qu'il enseigne.</p>
        <div>
          <ul>
            <li>Gestion de projet, leadership, soft skills</li>
            <li>Étude de marché et entrepreneuriat</li>
            <li>Conception de modules et de programmes</li>
          </ul>
          <a class="more" href="/{SLUGS['training']}">Voir le catalogue</a>
        </div>
      </article>
      <article class="offer-row">
        <div>
          <h3>Coaching</h3>
          <p class="who">Dirigeants, managers, chefs de projet, jeunes diplômés</p>
        </div>
        <p class="problem">Vous voulez prendre de meilleures décisions, gagner en impact ou réussir une étape clé de votre parcours.</p>
        <div>
          <ul>
            <li>Coaching individuel, première séance offerte</li>
            <li>Prise de parole, influence, leadership</li>
            <li>Ateliers d'équipe et séances stratégiques</li>
          </ul>
          <a class="more" href="/{SLUGS['coaching']}">Découvrir le coaching</a>
        </div>
      </article>
      <article class="offer-row">
        <div>
          <h3>Accompagnement de startups</h3>
          <p class="who">Fondateurs, entrepreneurs, porteurs de projet</p>
        </div>
        <p class="problem">Vous avez une idée ou un premier produit : il vous faut un cadre, une feuille de route et des ventes.</p>
        <div>
          <ul>
            <li>Programme Launch sur 3 mois</li>
            <li>Mentorat d'entrepreneurs</li>
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
        <h3>Un manager de terrain</h3>
        <p>Je dirige au quotidien des projets internationaux à l'échelle EMEA. Ce que j'enseigne et ce que je conseille, je le pratique.</p>
      </div>
      <div class="reason">
        <h3>Un pédagogue</h3>
        <p>J'enseigne à l'université et je conçois cours, cas pratiques et examens. On apprend en faisant, pas en écoutant.</p>
      </div>
      <div class="reason">
        <h3>Deux continents</h3>
        <p>J'ai travaillé avec des équipes en Europe et en Afrique. Je sais adapter une méthode à chaque culture et à chaque contexte.</p>
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
      <article class="case"><span class="tag">Formation</span><h3>Conception de programmes universitaires</h3><p>Programmes construits autour de problématiques réelles d'entreprise.</p></article>
      <article class="case"><span class="tag">Coaching</span><h3>Méthode Softies</h3><p>Méthode de développement des soft skills déployée dans plusieurs pays.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Entrepreneur Week</h3><p>Ateliers organisés avec des universités et des entreprises pour stimuler l'innovation et l'entrepreneuriat.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Mentorat de futurs entrepreneurs</h3><p>Accompagnement de porteurs de projet, de la vision à l'exécution.</p></article>
      <article class="case"><span class="tag">Management</span><h3>Lancements internationaux</h3><p>Pilotage de déploiements logiciels dans plusieurs pays, avec des équipes multiculturelles.</p></article>
      <article class="case"><span class="tag">Management</span><h3>Portefeuille mobile en Afrique</h3><p>Lancement d'outils financiers mobiles pour des populations peu bancarisées.</p></article>
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

# ---------------------------------------------------------------- Formations
COURSES = [
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
    {
        "id": "gestion-de-projet",
        "name": "Gestion de projet : méthodes agiles et hybrides",
        "desc": "Piloter un projet de bout en bout, avec la bonne méthode pour son équipe et son contexte.",
        "for": "Chefs de projet, product owners, managers, étudiants",
        "goals": [
            "Choisir et adapter une méthode agile ou hybride",
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
        "id": "entrepreneuriat",
        "name": "Entreprendre : de l'idée aux premiers clients",
        "desc": "Structurer un projet entrepreneurial, tester son marché et construire un premier plan commercial.",
        "for": "Porteurs de projet, étudiants entrepreneurs, incubés",
        "goals": [
            "Clarifier sa proposition de valeur et sa cible",
            "Construire une feuille de route réaliste",
            "Préparer son pitch et ses premiers rendez-vous clients",
        ],
        "duration": "1 à 2 jours, ou format atelier",
        "format": "Incubateurs, écoles, programmes d'entrepreneuriat",
    },
    {
        "id": "paiement-electronique",
        "name": "Formation technique : les fondamentaux du paiement électronique",
        "desc": "Pour les entreprises du secteur : comprendre la chaîne de paiement par carte, EMV, PCI DSS et SoftPOS.",
        "for": "Équipes produit, projet, commerciales et support de la fintech",
        "goals": [
            "Expliquer le parcours d'une transaction carte",
            "Comprendre EMV, le sans contact et le SoftPOS",
            "Situer les exigences PCI DSS et les certifications",
        ],
        "duration": "1 à 2 jours",
        "format": "Intra-entreprise, présentiel ou distanciel",
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
    "title": "Formations soft skills, leadership, gestion de projet, entrepreneuriat | Nacim Touenti",
    "description": "Formations en soft skills et leadership (méthode Softies), gestion de projet, étude de marché et entrepreneuriat. Intra-entreprise, écoles et centres de formation, par Nacim Touenti.",
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

# ---------------------------------------------------------------- Coaching
COACHING = {
    "key": "coaching",
    "slug": SLUGS["coaching"],
    "title": "Coaching de dirigeants, managers et jeunes diplômés | Nacim Touenti",
    "description": "Coaching individuel et d'équipe : leadership, prise de parole, décision, transitions de carrière. Première séance offerte. Par Nacim Touenti, Paris, Zurich et à distance.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Coaching',
        "Coaching",
        "Un regard extérieur exigeant et bienveillant pour clarifier où vous allez, décider plus vite et gagner en impact. La première séance est offerte.",
        "coaching.webp",
        "Deux professionnels marchant ensemble en ville",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Réserver la séance offerte</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Pour qui</h2>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Dirigeants et fondateurs</h3><p class="who">Coaching individuel</p></div>
        <p class="problem">Vous portez les décisions seul et vous voulez un partenaire de réflexion qui connaît la réalité du terrain.</p>
        <div><ul><li>Vision et feuille de route</li><li>Décisions difficiles et priorités</li><li>Leadership en croissance comme en crise</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Managers et chefs de projet</h3><p class="who">Coaching individuel</p></div>
        <p class="problem">Vous prenez un nouveau poste, une équipe plus grande ou un projet sous pression.</p>
        <div><ul><li>Communication et influence</li><li>Gestion des parties prenantes</li><li>Intelligence émotionnelle et posture</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Étudiants et jeunes diplômés</h3><p class="who">Coaching de carrière</p></div>
        <p class="problem">Vous préparez votre entrée dans la vie professionnelle ou un premier projet d'entreprise.</p>
        <div><ul><li>Projet professionnel et état d'esprit</li><li>Recherche d'emploi et entretiens</li><li>Création d'entreprise</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Équipes</h3><p class="who">Ateliers en entreprise, sur site ou à distance</p></div>
        <p class="problem">Vous voulez aligner une équipe de direction ou remobiliser une équipe projet.</p>
        <div><ul><li>Séances stratégiques Speak-Up</li><li>Construction d'une culture de performance</li><li>Ateliers soft skills (méthode Softies)</li></ul></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <h2>Comment se déroule un coaching</h2>
    </div>
    <ol class="steps">
      <li><h3>Séance offerte</h3><p>Nous faisons le point sur votre situation et ce que vous voulez changer.</p></li>
      <li><h3>Objectifs</h3><p>Deux ou trois objectifs concrets et un rythme de séances adapté.</p></li>
      <li><h3>Séances</h3><p>Échanges, mises en situation et actions à tester entre deux séances.</p></li>
      <li><h3>Bilan</h3><p>Ce qui a changé, ce qui reste à travailler et comment continuer seul.</p></li>
    </ol>
  </div>
</section>

{cta_band("Prêt à passer un cap ?", "Réservez votre séance offerte pour clarifier votre situation et vos prochaines étapes.", "Réserver la séance offerte", CONTACT, "Écrire sur WhatsApp", SITE["whatsapp_url"])}
""",
}

# ---------------------------------------------------------------- Startups
STARTUPS = {
    "key": "startups",
    "slug": SLUGS["startups"],
    "title": "Accompagnement de startups et d'entrepreneurs : projet, produit, ventes | Nacim Touenti",
    "description": "Programme Launch sur 3 mois, mentorat d'entrepreneurs, ateliers pour incubateurs et redressement de projet. Accompagnement de startups par Nacim Touenti.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Startups',
        "Accompagnement de startups et d'entrepreneurs",
        "Passer de l'idée à l'exécution demande un cadre, des priorités claires et quelqu'un qui a déjà mené des lancements. Je vous aide à structurer votre projet, votre produit et vos ventes.",
        "startups.webp",
        "Équipe de startup travaillant sur une feuille de route",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Réserver un appel découverte</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Quatre formats</h2>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Programme Launch</h3><p class="who">3 mois, une séance par semaine</p></div>
        <p class="problem">Pour les startups en phase de lancement qui doivent tout cadrer en même temps.</p>
        <div><ul><li>Cadrage du projet et feuille de route</li><li>Produit : priorités, tests, premières versions</li><li>Go-to-market : cible, offre, pitch, plan commercial</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Mentorat d'entrepreneurs</h3><p class="who">Rendez-vous réguliers, sur la durée</p></div>
        <p class="problem">Pour garder le cap, prendre du recul et ne pas rester seul face aux décisions.</p>
        <div><ul><li>Points mensuels ou bimensuels</li><li>Relecture du pitch et des documents clés</li><li>Mise en relation selon les besoins</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Ateliers pour incubateurs et écoles</h3><p class="who">Demi-journée à une semaine</p></div>
        <p class="problem">Pour faire avancer plusieurs projets à la fois, sur le modèle d'Entrepreneur Week.</p>
        <div><ul><li>Ateliers idée, marché, pitch</li><li>Jurys et retours individualisés</li><li>Programmes co-construits avec votre structure</li></ul></div>
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
        <li>Des tests rapides sur le marché avant les gros investissements</li>
      </ul>
    </div>
    <div>
      <h2>Ce que j'évite</h2>
      <ul class="ticks cross">
        <li>Les méthodes génériques plaquées sans adaptation</li>
        <li>Les business plans que personne ne relit</li>
        <li>Les rôles flous et la communication dispersée</li>
        <li>Construire un produit avant d'avoir parlé aux clients</li>
      </ul>
    </div>
  </div>
</section>

{cta_band("Votre projet mérite un cadre solide", "Un appel découverte de 30 minutes pour faire le point sur votre situation et voir le format qui vous convient.", "Réserver un appel découverte", CONTACT, "Écrire sur WhatsApp", SITE["whatsapp_url"])}
""",
}

# ---------------------------------------------------------------- Centres de formation
CENTRES = {
    "key": "centres",
    "slug": SLUGS["centres"],
    "title": "Formateur et intervenant pour centres de formation, écoles et universités | Nacim Touenti",
    "description": "Intervenant et concepteur de programmes pour centres de formation, écoles et universités : gestion de projet, leadership, soft skills, étude de marché, entrepreneuriat.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Centres de formation',
        "Pour les centres de formation, écoles et universités",
        "Vous cherchez un intervenant capable de concevoir un module complet et de l'animer avec exigence. J'apporte la double casquette d'enseignant et de manager en activité.",
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
        <li>Gestion de projet</li><li>Méthodes agiles</li><li>Leadership</li><li>Soft skills</li><li>Communication</li>
        <li>Étude de marché</li><li>Lean et Test &amp; Learn</li><li>Entrepreneuriat</li><li>Fintech et paiement</li>
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

# ---------------------------------------------------------------- À propos
ABOUT = {
    "key": "about",
    "slug": SLUGS["about"],
    "page_type": "ProfilePage",
    "title": "Nacim Touenti — Formateur, coach, enseignant et fondateur de Twty Consulting",
    "description": "Qui est Nacim Touenti ? Formateur, coach et enseignant à l'université, fondateur de Twty Consulting, avec plus de 10 ans de management de projets internationaux.",
    "body": f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/">Accueil</a> / À propos</p>
    <div class="about-grid">
      <div class="portrait" role="img" aria-label="Portrait de Nacim Touenti (photo à venir)">NT</div>
      <div>
        <h1>Nacim Touenti</h1>
        <p class="lead">Formateur, coach et enseignant à l'université, fondateur de Twty Consulting.</p>
        <p class="measure">{BIO_LONG}</p>
        <dl class="facts">
          <dt>Formation</dt><dd>Gestion de projet, leadership, soft skills, étude de marché, entrepreneuriat</dd>
          <dt>Coaching</dt><dd>Dirigeants, managers, chefs de projet, jeunes diplômés</dd>
          <dt>Expérience</dt><dd>Plus de 10 ans de management de projets internationaux (fintech, paiement)</dd>
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
      <p>Faire grandir les personnes et faire réussir leurs projets.</p>
    </div>
    <div class="reasons">
      <div class="reason"><h3>Formateur et enseignant</h3><p>Cours à l'université, conception de programmes, d'examens et de cas pratiques, formations en entreprise.</p></div>
      <div class="reason"><h3>Coach et mentor</h3><p>Créateur de la méthode Softies, coach de dirigeants et de managers, mentor de futurs entrepreneurs.</p></div>
      <div class="reason"><h3>Manager de terrain</h3><p>Direction de projets internationaux à l'échelle EMEA, lancements dans plusieurs pays, équipes multiculturelles en Europe et en Afrique.</p></div>
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
    "description": "Contactez Nacim Touenti pour une formation, un coaching ou un accompagnement de startup. Email, WhatsApp, LinkedIn. Paris, Zurich, Tanger.",
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
            <option>Formation pour mon équipe</option>
            <option>Coaching individuel</option>
            <option>Accompagnement de startup</option>
            <option>Intervention en centre de formation ou école</option>
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
    "body": """
<section class="section center-404">
  <div class="wrap measure">
    <h1>Cette page n'existe pas</h1>
    <p class="lead">Elle a peut-être été déplacée lors de la refonte du site. / This page may have moved.</p>
    <div class="actions"><a class="btn" href="/">Retour à l'accueil</a><a class="btn btn--ghost" href="/en/">English site</a></div>
  </div>
</section>
""",
}

PAGES = [HOME, TRAINING, COACHING, STARTUPS, CENTRES, ABOUT, CONTACT_PAGE, LEGAL, NOT_FOUND]

LLMS_TXT = f"""
# Twty Consulting — Nacim Touenti

> {BIO_SHORT}

{BIO_LONG}

## Offres
- [Formations]({BASE}/formations.html) : soft skills et leadership (méthode Softies), gestion de projet agile et hybride, étude de marché et Test & Learn, entrepreneuriat, fondamentaux du paiement électronique.
- [Coaching]({BASE}/coaching.html) : coaching individuel de dirigeants, managers, chefs de projet et jeunes diplômés ; ateliers d'équipe. Première séance offerte.
- [Accompagnement de startups]({BASE}/accompagnement-startup.html) : programme Launch sur 3 mois, mentorat d'entrepreneurs, ateliers pour incubateurs et écoles, redressement de projet.
- [Centres de formation et écoles]({BASE}/centres-de-formation.html) : interventions, conception de modules et de programmes, examens et cas pratiques.

## Personne
- [À propos de Nacim Touenti]({BASE}/nacim-touenti.html)
- LinkedIn : {SITE['linkedin_url']}
- Contact : {SITE['email']}
- Présence : Paris – La Défense, Zurich, Tanger. Langues : français, anglais.

## English
- [English version]({BASE}/en/)
"""
