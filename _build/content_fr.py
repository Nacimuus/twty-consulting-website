"""Contenu français de twty.fr (langue principale).

Positionnement : formation, coaching et accompagnement. L'expérience de management de projets
internationaux (fintech, paiement électronique) sert de preuve de légitimité, pas d'offre principale.
"""
from parts import hero_portrait, ticker, page_hero, cta_band, mailto, faq_schema, faq_html, course_schema
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
    "footer_blurb": "Formation, coaching, accompagnement de startups. Par Nacim Touenti.",
    "footer_nav": "Le site",
    "footer_contact": "Contact",
    "footer_presence": "Présence",
    "tangier": "Tanger",
    "legal": "Mentions légales",
}

# Bio de référence : à recopier à l'identique sur LinkedIn, Malt, pages universités…
BIO_SHORT = (
    "Nacim Touenti est formateur en entreprise, coach, intervenant à l'université et boosteur de startups, fondateur de Twty Consulting. "
    "Il accompagne entreprises, centres de formation, startups et entrepreneurs, en s'appuyant sur plus "
    "de dix ans de management de projets internationaux."
)

BIO_LONG = (
    "Nacim Touenti est formateur, coach et intervenant à l'université. Il a fondé Twty Consulting pour "
    "former les équipes, coacher les managers et accompagner les startups. Son atout : il pratique ce "
    "qu'il transmet. Depuis plus de dix ans, il pilote des projets internationaux dans la fintech et le "
    "paiement électronique, en Europe et en Afrique. Il dirige aujourd'hui la gestion de projets EMEA "
    "pour un acteur mondial du secteur. Il a créé la méthode Softies pour développer les soft skills et "
    "organise des ateliers Entrepreneur Week avec universités et entreprises. Il intervient depuis Paris, "
    "Zurich et Tanger, en français et en anglais."
)

ORG_DESCRIPTION = (
    "Cabinet de formation, de coaching et d'accompagnement fondé par Nacim Touenti : formations pour "
    "entreprises et centres de formation, coaching individuel, accompagnement de startups et d'entrepreneurs."
)

CONTACT = "/" + SLUGS["contact"]

# ---------------------------------------------------------------- Accueil
HOME_FAQ = [
    ("Intervenez-vous en présentiel ou à distance ?",
     "Les deux. Sur place à Paris, en Suisse et au Maroc. À distance partout ailleurs."),
    ("Dans quelles langues travaillez-vous ?",
     "Français et anglais."),
    ("Vos formations peuvent-elles être financées ?",
     "Oui, dans la plupart des cas. Sur votre budget formation, ou via un organisme partenaire certifié Qualiopi pour un financement OPCO. On trouve le bon montage ensemble."),
    ("Comment se passe la première séance de coaching ?",
     "Elle est offerte. On fait le point, et vous repartez avec une première action concrète. Même si on s'arrête là."),
    ("Quel est le délai pour démarrer ?",
     "Un premier appel de 30 minutes, souvent dans la semaine. Ensuite, je vous envoie une proposition."),
]

HOME = {
    "key": "home",
    "slug": SLUGS["home"],
    "title": "Nacim Touenti — Formateur, coach, boosteur de startups | Twty Consulting",
    "description": "Formateur, coach et boosteur de startups. Apprendre, grandir et performer avec le sourire. 10 ans de projets internationaux, 6 ans de formation en entreprise et à l'université.",
    "schema": [faq_schema(HOME_FAQ, "fr")],
    "body": f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Formateur, coach, boosteur de startups.</h1>
      <p class="lead">Apprendre, grandir et performer, avec le sourire. 10 ans de projets internationaux. 6 ans de formation sur les sujets qui comptent pour vous et votre business.</p>
      <div class="actions">
        <a class="btn" href="{CONTACT}">Parlons-en</a>
        <a class="btn btn--ghost" href="/{SLUGS['training']}">Voir les formations</a>
      </div>
    </div>
    {hero_portrait("Portrait de Nacim Touenti (photo à venir)", ["Formateur", "Coach", "Boosteur de startups"], "Paris, Zurich, Tanger")}
  </div>
</section>

{ticker(['Leadership', 'Gestion de projet', 'Soft skills', 'Prise de parole', 'Étude de marché', 'Entrepreneuriat', 'Coaching', 'Méthodes agiles', 'Négociation', 'Pitch'], 'Thèmes')}
<section class="proof" aria-label="En bref">
  <div class="wrap proof-grid">
    <div class="proof-item">
      <h4>10 ans de projets internationaux</h4>
      <p>Europe et Afrique, en équipes multiculturelles.</p>
    </div>
    <div class="proof-item">
      <h4>Intervenant à l'université</h4>
      <p>Et formateur en entreprise depuis 6 ans.</p>
    </div>
    <div class="proof-item">
      <h4>Ingénieur pédagogique</h4>
      <p>Je crée des formations et des méthodes sur mesure.</p>
    </div>
  </div>
</section>

<section class="section" id="offres">
  <div class="wrap">
    <div class="section-head">
      <h2>Par où on commence ?</h2>
      <p>Former une équipe, passer un cap, lancer un projet. Choisissez.</p>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div>
          <h3>Formation</h3>
          <p class="who">Entreprises, centres de formation, écoles et universités</p>
        </div>
        <p class="problem">Les sujets qui vous feront du bien. Des formations qu'on applique dès le lundi.</p>
        <div>
          <ul>
            <li>Gestion de projet</li>
            <li>Produit</li>
            <li>Création d'entreprise</li>
            <li>Scale-up</li>
          </ul>
          <a class="more" href="/{SLUGS['training']}">Voir le catalogue</a>
        </div>
      </article>
      <article class="offer-row">
        <div>
          <h3>Coaching</h3>
          <p class="who">Dirigeants, managers, chefs de projet, jeunes diplômés</p>
        </div>
        <p class="problem">Un cap à passer ? Une décision à prendre ? On s'y met ensemble.</p>
        <div>
          <ul>
            <li>Première séance offerte</li>
            <li>Leadership, prise de parole</li>
            <li>Ateliers d'équipe</li>
          </ul>
          <a class="more" href="/{SLUGS['coaching']}">Découvrir le coaching</a>
        </div>
      </article>
      <article class="offer-row">
        <div>
          <h3>Accompagnement de startups</h3>
          <p class="who">Fondateurs, entrepreneurs, porteurs de projet</p>
        </div>
        <p class="problem">Une idée, c'est bien. Des clients, c'est mieux.</p>
        <div>
          <ul>
            <li>Programme Launch, 3 mois</li>
            <li>Développement et accompagnement commercial</li>
            <li>Process de gestion de projet et produit</li>
            <li>Mentorat d'entrepreneurs</li>
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
      <h2>Pourquoi moi ?</h2>
    </div>
    <div class="reasons">
      <div class="reason">
        <h3>Je pratique ce que j'enseigne</h3>
        <p>Je pilote des projets dans toute la zone EMEA. Mes conseils sortent du terrain. Ils ont été testés.</p>
      </div>
      <div class="reason">
        <h3>Je sais tenir une salle</h3>
        <p>J'interviens à l'université et en entreprise. Chez moi, on participe. On débat, on joue, on s'implique.</p>
      </div>
      <div class="reason">
        <h3>Je parle à tout le monde</h3>
        <p>Étudiants, managers, dirigeants. Europe et Afrique. J'adapte le ton, jamais l'exigence.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Quelques réalisations</h2>
      <p>Les détails ? Je vous les raconte de vive voix.</p>
    </div>
    <div class="cases">
      <article class="case"><span class="tag">Formation</span><h3>Conception de programmes universitaires</h3><p>Des cursus bâtis sur de vrais cas d'entreprise.</p></article>
      <article class="case"><span class="tag">Coaching</span><h3>Méthode Softies</h3><p>Ma méthode soft skills, lancée dans plusieurs pays.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Entrepreneur Week</h3><p>Des ateliers avec universités et entreprises. Objectif : faire naître des projets.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Mentorat de futurs entrepreneurs</h3><p>De l'idée à l'exécution, aux côtés des porteurs de projet.</p></article>
      <article class="case"><span class="tag">Management</span><h3>Lancements internationaux</h3><p>Des déploiements dans plusieurs pays. Des équipes de toutes les cultures.</p></article>
      <article class="case"><span class="tag">Management</span><h3>Portefeuille mobile en Afrique</h3><p>Des services financiers sur mobile pour les non-bancarisés.</p></article>
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

{cta_band("Un projet ? Une équipe à faire grandir ?", "30 minutes pour en parler. Offert, sans engagement.", "Réserver un échange", CONTACT, "WhatsApp", SITE["whatsapp_url"])}
""",
}

# ---------------------------------------------------------------- Formations
COURSES = [
    {
        "id": "soft-skills-softies",
        "name": "Soft skills et leadership : la méthode Softies",
        "desc": "Parler avec aplomb. Négocier sans braquer. Mener une équipe avec son propre style.",
        "for": "Managers, équipes projet, étudiants et jeunes diplômés",
        "goals": [
            "Prendre la parole et convaincre",
            "Négocier et désamorcer les tensions",
            "Trouver son style de leader",
        ],
        "duration": "1 jour ou parcours modulable",
        "format": "Présentiel de préférence, jeux de rôle et serious games",
    },
    {
        "id": "gestion-de-projet",
        "name": "Gestion de projet : méthodes agiles et hybrides",
        "desc": "Livrer à l'heure. Sans épuiser l'équipe.",
        "for": "Chefs de projet, product owners, managers, étudiants",
        "goals": [
            "Choisir la bonne méthode, agile ou hybride",
            "Tenir le périmètre, embarquer les parties prenantes",
            "Faire un reporting que les décideurs lisent",
            "Remettre un projet sur les rails",
        ],
        "duration": "2 jours (14 h)",
        "format": "Intra ou inter-entreprise, présentiel ou distanciel",
    },
    {
        "id": "etude-de-marche",
        "name": "Étude de marché et logique Test & Learn",
        "desc": "Arrêter de deviner. Tester, mesurer, décider.",
        "for": "Entrepreneurs, étudiants, équipes marketing et innovation",
        "goals": [
            "Poser les bonnes questions avant de collecter",
            "Éviter les pièges de causalité",
            "Tester vite et pas cher, en mode Lean",
        ],
        "duration": "1 jour (7 h), déclinable en module universitaire",
        "format": "Écoles, universités, incubateurs, entreprises",
    },
    {
        "id": "entrepreneuriat",
        "name": "Entreprendre : de l'idée aux premiers clients",
        "desc": "De l'idée au premier client. Sans se perdre en route.",
        "for": "Porteurs de projet, étudiants entrepreneurs, incubés",
        "goals": [
            "Clarifier sa cible et sa promesse",
            "Bâtir une feuille de route réaliste",
            "Pitcher et décrocher ses premiers rendez-vous",
        ],
        "duration": "1 à 2 jours, ou format atelier",
        "format": "Incubateurs, écoles, programmes d'entrepreneuriat",
    },
    {
        "id": "paiement-electronique",
        "name": "Formation technique : les fondamentaux du paiement électronique",
        "desc": "Pour les équipes de la fintech. Ce qui se passe vraiment quand on paie par carte.",
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
        "Ici, personne ne s'endort. On joue, on débat, on se trompe, on progresse. Vous repartez avec des outils, pas avec des slides.",
        "formation.webp",
        "Session de formation interactive en petit groupe",
        f'<div class="actions"><a class="btn" href="#catalogue">Voir le catalogue</a><a class="btn btn--ghost" href="{CONTACT}">Demander une formation sur mesure</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>Ma méthode</h2>
      <p class="measure">Zéro cours magistral. Vos équipes négocient, présentent, décident. Elles se trompent parfois, exprès. C'est comme ça qu'on retient.</p>
    </div>
    <ul class="ticks">
      <li>Mises en situation et études de cas réels</li>
      <li>Serious games qui font réfléchir</li>
      <li>Un débrief après chaque exercice</li>
      <li>Miro, quiz, sondages en direct</li>
    </ul>
  </div>
</section>

<section class="section section--mist" id="catalogue">
  <div class="wrap">
    <div class="section-head">
      <h2>Catalogue</h2>
      <p>Tout s'adapte. La durée, le niveau, les exemples de votre secteur.</p>
    </div>
    {"".join(course_html(c) for c in COURSES)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>De la commande à la salle</h2>
    </div>
    <ol class="steps">
      <li><h3>Conception</h3><p>On part de vos objectifs. Je construis des modules concrets.</p></li>
      <li><h3>Test</h3><p>Un essai avec de vrais participants. On ajuste.</p></li>
      <li><h3>Validation</h3><p>Vous relisez. On affine.</p></li>
      <li><h3>Animation</h3><p>Sur place ou à distance. Avec évaluation des acquis.</p></li>
    </ol>
  </div>
</section>

{cta_band("Une équipe à former ?", "Dites-moi qui, quoi, quand. Je vous envoie un programme.", "Demander une formation", CONTACT, "Vous êtes un centre de formation", "/" + SLUGS["centres"])}
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
        "Vous avez les compétences. Il vous manque parfois du recul, un sparring-partner, un cap clair. C'est mon rôle. La première séance est offerte.",
        "coaching.webp",
        "Deux professionnels marchant ensemble en ville",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Réserver ma séance offerte</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Pour qui ?</h2>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Dirigeants et fondateurs</h3><p class="who">Coaching individuel</p></div>
        <p class="problem">Seul face aux décisions ? Parlez-en à quelqu'un qui connaît le terrain.</p>
        <div><ul><li>Vision et feuille de route</li><li>Décisions difficiles et priorités</li><li>Leadership en croissance comme en crise</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Managers et chefs de projet</h3><p class="who">Coaching individuel</p></div>
        <p class="problem">Nouveau poste. Équipe plus grande. Projet sous pression. On prépare la suite.</p>
        <div><ul><li>Communication et influence</li><li>Gestion des parties prenantes</li><li>Intelligence émotionnelle et posture</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Étudiants et jeunes diplômés</h3><p class="who">Coaching de carrière</p></div>
        <p class="problem">Premier job ou première boîte ? Partez avec un plan.</p>
        <div><ul><li>Projet professionnel et état d'esprit</li><li>Recherche d'emploi et entretiens</li><li>Création d'entreprise</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Équipes</h3><p class="who">Ateliers en entreprise, sur site ou à distance</p></div>
        <p class="problem">Une équipe à aligner ou à remotiver ? Un atelier change la dynamique.</p>
        <div><ul><li>Séances stratégiques Speak-Up</li><li>Construction d'une culture de performance</li><li>Ateliers soft skills (méthode Softies)</li></ul></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <h2>Comment ça marche</h2>
    </div>
    <ol class="steps">
      <li><h3>Séance offerte</h3><p>On fait le point. Sans engagement.</p></li>
      <li><h3>Objectifs</h3><p>Deux ou trois objectifs concrets. Pas plus.</p></li>
      <li><h3>Séances</h3><p>On échange, on s'entraîne. Vous testez entre deux séances.</p></li>
      <li><h3>Bilan</h3><p>On mesure le chemin parcouru. Vous continuez seul.</p></li>
    </ol>
  </div>
</section>

{cta_band("Prêt à passer un cap ?", "La première séance est offerte. Vous n'avez rien à perdre.", "Réserver ma séance offerte", CONTACT, "WhatsApp", SITE["whatsapp_url"])}
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
        "Une idée, de l'énergie, mais pas de mode d'emploi ? Je vous aide à cadrer, tester et vendre. Vite.",
        "startups.webp",
        "Équipe de startup travaillant sur une feuille de route",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Réserver un appel découverte</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Comment je vous aide</h2>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Programme Launch</h3><p class="who">3 mois, une séance par semaine</p></div>
        <p class="problem">Trois mois pour passer de l'idée au lancement.</p>
        <div><ul><li>Un projet cadré, une feuille de route claire</li><li>Un produit testé sur de vrais clients</li><li>Une offre, un pitch, un plan commercial</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Mentorat d'entrepreneurs</h3><p class="who">Rendez-vous réguliers, sur la durée</p></div>
        <p class="problem">Quelqu'un à vos côtés quand il faut trancher.</p>
        <div><ul><li>Un point tous les 15 jours ou tous les mois</li><li>Relecture de votre pitch</li><li>Mises en relation utiles</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Ateliers pour incubateurs et écoles</h3><p class="who">Demi-journée à une semaine</p></div>
        <p class="problem">Faites avancer toute une promo d'un coup. Comme à l'Entrepreneur Week.</p>
        <div><ul><li>Ateliers idée, marché, pitch</li><li>Jurys et retours individuels</li><li>Un programme construit avec vous</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Redressement de projet</h3><p class="who">Mission courte</p></div>
        <p class="problem">Ça dérape ? On reprend la main. Vite.</p>
        <div><ul><li>Diagnostic express et plan de reprise</li><li>Périmètre et équipe recadrés</li><li>Les bons outils (Jira, Notion, ClickUp…)</li></ul></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div>
      <h2>Mes règles</h2>
      <ul class="ticks">
        <li>Parler aux clients avant de coder</li>
        <li>Tester petit avant d'investir gros</li>
        <li>Des priorités claires chaque semaine</li>
        <li>Des résultats, pas des slides</li>
      </ul>
    </div>
    <div>
      <h2>Ce que je fuis</h2>
      <ul class="ticks cross">
        <li>Les business plans que personne ne lit</li>
        <li>Les méthodes copiées-collées</li>
        <li>Les rôles flous</li>
        <li>Les réunions sans décision</li>
      </ul>
    </div>
  </div>
</section>

{cta_band("Passez de l'idée à l'action.", "30 minutes pour faire le point sur votre projet. Offert.", "Réserver un appel découverte", CONTACT, "WhatsApp", SITE["whatsapp_url"])}
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
        "Un intervenant qui tient une salle et connaît le terrain ? Je conçois et j'anime vos modules, de A à Z.",
        "centres.webp",
        "Formateur animant un atelier participatif",
        f'<div class="actions"><a class="btn" href="{mailto("Proposition d intervention")}">Proposer une intervention</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>Ce que je vous apporte</h2>
      <ul class="ticks">
        <li>Modules courts, masterclasses, conférences</li>
        <li>Programmes clés en main, supports compris</li>
        <li>Examens et cas pratiques sur mesure</li>
        <li>Jurys et suivi de projets étudiants</li>
      </ul>
    </div>
    <div>
      <h2>Sujets enseignés</h2>
      <ul class="chips">
        <li>Gestion de projet</li><li>Méthodes agiles</li><li>Leadership</li><li>Soft skills</li><li>Communication</li>
        <li>Étude de marché</li><li>Lean et Test &amp; Learn</li><li>Entrepreneuriat</li><li>Fintech et paiement</li>
      </ul>
      <p class="measure" style="margin-top:24px">Exemple : un examen d'étude de marché bâti autour d'une startup fictive. Concret, et calé sur le cours.</p>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <h2>Comment on travaille</h2>
    </div>
    <ol class="steps">
      <li><h3>Besoin</h3><p>Public, objectifs, volume horaire. Vous me briefez.</p></li>
      <li><h3>Proposition</h3><p>Programme détaillé et devis.</p></li>
      <li><h3>Production</h3><p>Supports, cas, évaluations. Dans vos formats.</p></li>
      <li><h3>Animation</h3><p>Je donne les cours. On fait le bilan ensemble.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap measure">
    <h2>Côté administratif, c'est simple</h2>
    <p>J'interviens en sous-traitance. Vous gardez la relation avec les financeurs. Je vous fournis tout pour votre démarche qualité : programme, objectifs, évaluations, CV.</p>
  </div>
</section>

{cta_band("Un module à monter ?", "Envoyez-moi le thème, le public et les dates. Je reviens vers vous vite.", "Proposer une intervention", mailto("Proposition d intervention"), "Voir le catalogue", "/" + SLUGS["training"])}
""",
}

# ---------------------------------------------------------------- À propos
ABOUT = {
    "key": "about",
    "slug": SLUGS["about"],
    "page_type": "ProfilePage",
    "title": "Nacim Touenti — Formateur, coach, boosteur de startups et fondateur de Twty Consulting",
    "description": "Qui est Nacim Touenti ? Formateur, coach, intervenant à l'université et boosteur de startups, fondateur de Twty Consulting, avec plus de 10 ans de management de projets internationaux.",
    "body": f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/">Accueil</a> / À propos</p>
    <div class="about-grid">
      <div class="portrait" role="img" aria-label="Portrait de Nacim Touenti (photo à venir)">NT</div>
      <div>
        <h1>Nacim Touenti</h1>
        <p class="lead">Formateur, coach, boosteur de startups. Et toujours manager de projets internationaux.</p>
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
      <h2>Trois casquettes, une obsession</h2>
      <p>Que les gens progressent. Pour de vrai.</p>
    </div>
    <div class="reasons">
      <div class="reason"><h3>Formateur et intervenant</h3><p>À l'université comme en entreprise. Je conçois et j'anime.</p></div>
      <div class="reason"><h3>Coach et mentor</h3><p>J'ai créé la méthode Softies. Je coache managers et dirigeants. Je mentore des entrepreneurs.</p></div>
      <div class="reason"><h3>Manager de terrain</h3><p>Je pilote des projets dans toute la zone EMEA. Plusieurs pays, plusieurs cultures, des délais serrés.</p></div>
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
    <h1>Parlons-en</h1>
    <p class="lead">Quelques lignes suffisent. Je vous réponds vite, avec un créneau de 30 minutes.</p>
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
