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
    "Nacim Touenti est formateur, coach et boosteur de startups, fondateur de Twty Consulting. "
    "Intervenant à l'université et formateur en entreprise, il s'appuie sur 10 ans de management "
    "de projets internationaux."
)

BIO_LONG = (
    "Nacim Touenti est formateur, coach et boosteur de startups, fondateur de Twty Consulting. "
    "Intervenant à l'université et formateur en entreprise depuis 10 ans, il a travaillé avec plus de "
    "15 établissements, dont l'IUT Paris Descartes, l'ISG, la Sorbonne et PSB, et formé plus de 1000 "
    "personnes. Il s'appuie sur 10 ans de management de projets internationaux, en Europe et en Afrique, "
    "auprès de banques, de fintechs, de retailers, d'entreprises du digital et d'associations, avec des "
    "portefeuilles de projets et d'opportunités de plus de 100 millions d'euros par an. Ses sujets : "
    "gestion de projet, produit, création d'entreprise, scale-up, finance, BI et soft skills. Il "
    "intervient depuis Paris, Zurich et Tanger, en français et en anglais."
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
    ("Comment se passe la première séance de coaching ?",
     "Elle est offerte. On fait le point, et vous repartez avec une première action concrète. Même si on s'arrête là."),
    ("Quel est le délai pour démarrer ?",
     "Un premier appel de 30 minutes, souvent dans la semaine. Ensuite, je vous envoie une proposition."),
]

HOME = {
    "key": "home",
    "slug": SLUGS["home"],
    "title": "Nacim Touenti — Formateur, coach, boosteur de startups | Twty Consulting",
    "description": "Formateur, coach et boosteur de startups. Apprendre, grandir et performer avec le sourire. 10 ans de projets internationaux, 10 ans de formation en entreprise et à l'université.",
    "schema": [faq_schema(HOME_FAQ, "fr")],
    "body": f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Formateur, coach, boosteur de startups.</h1>
      <p class="lead">Apprendre, grandir et performer, avec le sourire. 10 ans de projets internationaux. 10 ans de formation sur les sujets qui comptent pour vous et votre business.</p>
      <div class="actions">
        <a class="btn" href="{CONTACT}">Parlons-en</a>
        <a class="btn btn--ghost" href="/{SLUGS['training']}">Voir les formations</a>
      </div>
    </div>
    {hero_portrait("Portrait de Nacim Touenti (photo à venir)", ["Formateur", "Coach", "Boosteur de startups"], "Paris, Zurich, Tanger")}
  </div>
</section>

{ticker(['Gestion de projet', 'Produit', "Création d'entreprise", 'Scale-up', 'Finance', 'BI et dashboards', 'Lead generation', 'Soft skills', 'Coaching', 'Leadership'], 'Thèmes')}
<section class="proof" aria-label="En bref">
  <div class="wrap proof-grid">
    <div class="proof-item">
      <h4>10 ans de projets internationaux</h4>
      <p>Europe et Afrique, en équipes multiculturelles.</p>
    </div>
    <div class="proof-item">
      <h4>Intervenant à l'université</h4>
      <p>Et formateur en entreprise depuis 10 ans.</p>
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
      <h2>Pourquoi ça marche</h2>
      <p>Tout est sur mesure. Chaque formation, chaque coaching part de vos besoins et de vos cas réels. Pas de contenu standard, pas d'approche générique copiée-collée ou produite par une IA.</p>
    </div>
    <div class="reasons reasons--four">
      <div class="reason">
        <h3>Du concret dès le lundi</h3>
        <p>Des outils testés sur de vrais projets, pas de la théorie.</p>
      </div>
      <div class="reason">
        <h3>Des équipes qui s'impliquent</h3>
        <p>Mises en situation, jeux, débats. Personne ne décroche.</p>
      </div>
      <div class="reason">
        <h3>Le sourire en plus</h3>
        <p>On apprend mieux quand on prend du plaisir. C'est ma méthode.</p>
      </div>
      <div class="reason">
        <h3>Des résultats visibles</h3>
        <p>Vous voyez la différence dans vos équipes, pas seulement sur une feuille de présence.</p>
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
      <article class="case case--featured">
        <div>
          <span class="tag">Startups</span>
          <h3>Humen Recrut</h3>
          <p>Refonte de la structure commerciale, mise en place des process, formation de l'équipe commerciale et des SDR, automatisation de la génération de leads.</p>
          <a class="more" href="/{SLUGS['startups']}">Voir l'accompagnement startups</a>
        </div>
        <div class="stats">
          <div class="stat"><b>+50 %</b><span>de leads</span></div>
          <div class="stat"><b>+3</b><span>rendez-vous clients par semaine, en moyenne sur 3 mois</span></div>
        </div>
      </article>
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
CATALOG = [
    ("Piloter vos projets", [
        {"id": "gestion-de-projet", "name": "Gestion de projet agile et hybride",
         "hook": "Livrer à l'heure. Sans épuiser l'équipe.",
         "topics": ["Choisir la bonne méthode, agile ou hybride", "Des process projet clairs et partagés", "Un reporting que les décideurs lisent", "Remettre un projet sur les rails"],
         "for": "Chefs de projet, managers, équipes tech"},
        {"id": "produit", "name": "Produit : de l'idée à la roadmap",
         "hook": "Construire le bon produit, dans le bon ordre.",
         "topics": ["Roadmap et priorisation", "Process projet et produit", "Automatisation des tâches répétitives", "Tester avant d'investir"],
         "for": "Product owners, fondateurs, équipes produit"},
    ]),
    ("Entreprendre et grandir", [
        {"id": "creation-entreprise", "name": "Créer son entreprise",
         "hook": "De l'idée au premier client. Sans se perdre en route.",
         "topics": ["Cible et proposition de valeur", "Étude de marché et logique Test & Learn", "Une feuille de route réaliste", "Pitch et premiers rendez-vous"],
         "for": "Porteurs de projet, étudiants entrepreneurs, incubés"},
        {"id": "scale-up", "name": "Scale-up : structurer la croissance",
         "hook": "Vendre plus. Et gagner plus en vendant.",
         "topics": ["Process commerciaux et politique commerciale", "Lead generation", "P&L et optimisation de la rentabilité", "Automatiser pour passer à l'échelle"],
         "for": "Dirigeants de startups et de PME en croissance"},
    ]),
    ("Finance et données", [
        {"id": "finance", "name": "La finance pour les non-financiers",
         "hook": "Comprendre les chiffres pour mieux décider. En découverte ou en mise à niveau.",
         "topics": ["Lire un bilan et un compte de résultat", "Trésorerie, marges, rentabilité", "Construire et suivre un budget", "Parler le même langage que la finance"],
         "for": "Managers, entrepreneurs, étudiants"},
        {"id": "bi-dashboards", "name": "BI et tableaux de bord",
         "hook": "Des outils qui montrent l'essentiel, en un coup d'œil.",
         "topics": ["Choisir les bons indicateurs", "Concevoir des tableaux de bord utiles", "Créer des outils sur mesure pour l'entreprise", "Automatiser la collecte des données"],
         "for": "Dirigeants, managers, équipes de pilotage"},
    ]),
    ("Posture et expertise métier", [
        {"id": "soft-skills", "name": "Soft skills et posture en entreprise",
         "hook": "Parler avec aplomb. Négocier sans braquer. Trouver sa place.",
         "topics": ["Prise de parole et persuasion", "Négociation et gestion des tensions", "Posture professionnelle et leadership"],
         "for": "Managers, équipes, étudiants et jeunes diplômés"},
        {"id": "paiement-electronique", "name": "Les fondamentaux du paiement électronique",
         "hook": "Pour les équipes de la fintech : ce qui se passe vraiment quand on paie par carte.",
         "topics": ["Le parcours d'une transaction carte", "EMV, sans contact, SoftPOS", "PCI DSS et certifications"],
         "for": "Équipes produit, projet et support de la fintech"},
    ]),
]
COURSES = [c for _, group in CATALOG for c in group]


def course_html(c):
    topics = "".join(f"<li>{t}</li>" for t in c["topics"])
    return f"""<article class="course-card" id="{c['id']}">
  <h3>{c['name']}</h3>
  <p class="hook">{c['hook']}</p>
  <ul>{topics}</ul>
  <p class="for"><b>Pour :</b> {c['for']}</p>
  <a class="more" href="{mailto('Programme : ' + c['name'])}">Demander le programme</a>
</article>"""


def catalog_html():
    out = []
    for title, group in CATALOG:
        cards = "".join(course_html(c) for c in group)
        out.append(f'<div class="catalog-group"><h3 class="catalog-title">{title}</h3><div class="course-grid">{cards}</div></div>')
    return "\n".join(out)


TRAINING = {
    "key": "training",
    "slug": SLUGS["training"],
    "title": "Formations gestion de projet, produit, création d'entreprise, finance, BI | Nacim Touenti",
    "description": "Formations sur mesure en gestion de projet, produit, création d'entreprise, scale-up, finance, BI et soft skills. En heures ou en jours, en entreprise et en école, par Nacim Touenti.",
    "schema": [course_schema(c["name"], c["hook"], "fr", f"{BASE}/{SLUGS['training']}#{c['id']}") for c in COURSES],
    "body": page_hero(
        '<a href="/">Accueil</a> / Formations',
        "Des formations qui vous font du bien.",
        "Gestion de projet, produit, création d'entreprise, scale-up, finance, BI. Sur mesure, concrètes, applicables dès le lundi.",
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
      <p>Tout s'adapte : la durée, le niveau, les exemples de votre secteur.</p>
    </div>
    {catalog_html()}
    <p class="catalog-note">En modules de quelques heures ou sur plusieurs jours. En présentiel ou à distance. En entreprise, en école ou en centre de formation. Tarif sur devis.</p>
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
    "title": "Coaching : prise de parole, leadership, confiance en soi, gestion du stress | Nacim Touenti",
    "description": "Coaching sur mesure pour dirigeants, managers, jeunes diplômés et équipes : prise de parole, leadership, confiance en soi, créativité, gestion du stress, création ou restructuration d'entreprise. Première heure offerte.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Coaching',
        "Un cap à passer ? On y va ensemble.",
        "Dirigeants, managers, jeunes diplômés. Je vous aide à prendre du recul, décider plus vite et gagner en impact. Toujours sur mesure. Première séance offerte.",
        "coaching.webp",
        "Deux professionnels marchant ensemble en ville",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Réserver ma séance offerte</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Ce qu'on travaille ensemble</h2>
    </div>
    <ul class="chips chips--big">
      <li>Prise de parole</li><li>Leadership</li><li>Confiance en soi</li><li>Créativité</li><li>Gestion du stress</li><li>Création ou restructuration d'entreprise</li>
    </ul>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <h2>Pour qui ?</h2>
    </div>
    <div class="course-grid">
      <article class="course-card"><h3>Dirigeants et fondateurs</h3><p class="hook">Seul face aux décisions ? Un regard de terrain pour trancher.</p><ul><li>Leadership</li><li>Gestion du stress</li><li>Création ou restructuration d'entreprise</li></ul></article>
      <article class="course-card"><h3>Managers et chefs de projet</h3><p class="hook">Nouveau poste, équipe plus grande, projet sous pression.</p><ul><li>Prise de parole</li><li>Leadership</li><li>Confiance en soi</li></ul></article>
      <article class="course-card"><h3>Étudiants et jeunes diplômés</h3><p class="hook">Premier job ou première boîte ? Partez avec un plan.</p><ul><li>Confiance en soi</li><li>Prise de parole</li><li>Projet professionnel</li></ul></article>
      <article class="course-card"><h3>Équipes</h3><p class="hook">Aligner, remotiver, avancer ensemble.</p><ul><li>Créativité</li><li>Cohésion</li><li>Ateliers stratégiques</li></ul></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Formats</h2>
    </div>
    <div class="reasons">
      <div class="reason"><h3>1 h découverte</h3><p>Offerte. On fait le point, sans engagement.</p></div>
      <div class="reason"><h3>Sur mesure</h3><p>Un accompagnement construit autour de vos objectifs.</p></div>
      <div class="reason"><h3>Packs de 5 ou 10 séances</h3><p>Au rythme qui vous convient.</p></div>
      <div class="reason"><h3>Atelier d'équipe</h3><p>Pour avancer ensemble, dans votre entreprise.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <h2>Comment ça marche</h2>
    </div>
    <ol class="steps">
      <li><h3>Séance offerte</h3><p>1 h pour faire le point. Sans engagement.</p></li>
      <li><h3>Objectifs</h3><p>Deux ou trois objectifs concrets. Pas plus.</p></li>
      <li><h3>Séances</h3><p>En pack de 5 ou 10, au rythme qui vous convient.</p></li>
      <li><h3>Bilan</h3><p>On mesure le chemin parcouru. Vous continuez seul.</p></li>
    </ol>
  </div>
</section>

{cta_band("Prêt à passer un cap ?", "La première heure est offerte. Vous n'avez rien à perdre.", "Réserver ma séance offerte", CONTACT, "WhatsApp", SITE["whatsapp_url"])}
""",
}

# ---------------------------------------------------------------- Startups
STARTUPS = {
    "key": "startups",
    "slug": SLUGS["startups"],
    "title": "Boosteur de startups : lancement, développement commercial, process, rentabilité | Nacim Touenti",
    "description": "Accompagnement de startups et de PME : lancement, process commerciaux, lead generation, process projet et produit, P&L. Programme Launch sur 3 mois, à la carte, mentorat. Exemple : +50 % de leads chez Humen Recrut.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Startups',
        "Boosteur de startups.",
        "Cadrer, tester, vendre, structurer. Je vous aide à passer chaque étape, avec des méthodes de terrain. Toujours sur mesure.",
        "startups.webp",
        "Équipe de startup travaillant sur une feuille de route",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Réserver un appel découverte</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Là où j'interviens</h2>
    </div>
    <div class="course-grid">
      <article class="course-card"><h3>Lancer</h3><p class="hook">De l'idée aux premiers clients.</p><ul><li>Cible et proposition de valeur</li><li>Étude de marché, tests rapides</li><li>Pitch et premiers rendez-vous</li></ul></article>
      <article class="course-card"><h3>Vendre</h3><p class="hook">Plus de leads, plus de rendez-vous, plus de clients.</p><ul><li>Process commerciaux</li><li>Lead generation et automatisation</li><li>Politique commerciale, formation des équipes</li></ul></article>
      <article class="course-card"><h3>Structurer</h3><p class="hook">Des process qui tiennent quand l'équipe grandit.</p><ul><li>Process projet et produit</li><li>Roadmap et priorités</li><li>Automatisation des tâches répétitives</li></ul></article>
      <article class="course-card"><h3>Rentabiliser</h3><p class="hook">Grandir, oui. En gagnant de l'argent.</p><ul><li>Lecture et pilotage du P&amp;L</li><li>Optimisation de la rentabilité</li><li>Tableaux de bord de pilotage</li></ul></article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head">
      <h2>Des résultats concrets</h2>
    </div>
    <article class="case-study">
      <div>
        <span class="tag">Développement commercial</span>
        <h3>Humen Recrut</h3>
        <p>Refonte de la structure commerciale, mise en place des process, formation de l'équipe commerciale et des SDR, automatisation de la génération de leads.</p>
      </div>
      <div class="stats">
        <div class="stat"><b>+50 %</b><span>de leads</span></div>
        <div class="stat"><b>+3</b><span>rendez-vous clients par semaine, en moyenne sur 3 mois</span></div>
      </div>
    </article>
    <article class="case-study case-study--small">
      <div>
        <span class="tag">Formation</span>
        <h3>AWA</h3>
        <p>Formation des équipes à la stratégie et à la politique commerciale.</p>
      </div>
    </article>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Formats</h2>
    </div>
    <div class="reasons">
      <div class="reason"><h3>Programme Launch</h3><p>3 mois, 1 à 2 séances par semaine. Des semaines dédiées si besoin.</p></div>
      <div class="reason"><h3>À la carte</h3><p>Un sujet précis, y compris un projet à redresser.</p></div>
      <div class="reason"><h3>Mentorat</h3><p>Un point régulier pour garder le cap.</p></div>
      <div class="reason"><h3>Ateliers</h3><p>Pour incubateurs et écoles, sur le modèle d'Entrepreneur Week.</p></div>
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
    "title": "Intervenant et ingénieur pédagogique pour écoles, universités et centres de formation | Nacim Touenti",
    "description": "Conception et animation de modules sur mesure, en présentiel et en ligne. Plus de 15 établissements, plus de 1000 personnes formées, plus de 20 modules créés : IUT Paris Descartes, ISG, XP School, Sorbonne, IUT Sénart, PSB.",
    "body": page_hero(
        '<a href="/">Accueil</a> / Centres de formation',
        "Vos modules, conçus et animés de A à Z.",
        "Écoles, universités, centres de formation. Intervenant à l'université et formateur en entreprise depuis 10 ans, je conçois et j'anime des modules concrets, sur mesure, en présentiel et en ligne.",
        "centres.webp",
        "Formateur animant un atelier participatif",
        f'<div class="actions"><a class="btn" href="{mailto("Proposition d intervention")}">Proposer une intervention</a></div>',
    ) + f"""
<section class="proof" aria-label="En chiffres">
  <div class="wrap proof-grid">
    <div class="proof-item"><b class="num">15+</b><h4>établissements</h4><p>Écoles, universités, centres de formation.</p></div>
    <div class="proof-item"><b class="num">1000+</b><h4>personnes formées</h4><p>Étudiants, salariés, entrepreneurs.</p></div>
    <div class="proof-item"><b class="num">20+</b><h4>modules créés</h4><p>Conçus sur mesure, de A à Z.</p></div>
  </div>
  <div class="wrap trust">
    <p>Ils m'ont fait confiance</p>
    <ul class="chips"><li>IUT Paris Descartes</li><li>ISG</li><li>XP School</li><li>Sorbonne</li><li>IUT Sénart</li><li>PSB</li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Ce que je vous apporte</h2>
    </div>
    <div class="reasons">
      <div class="reason"><h3>Interventions</h3><p>Modules courts, masterclasses, conférences.</p></div>
      <div class="reason"><h3>Ingénierie pédagogique</h3><p>Des parcours pensés pour la salle et pour le en ligne.</p></div>
      <div class="reason"><h3>Modules clés en main</h3><p>Syllabus, supports, cas pratiques compris.</p></div>
      <div class="reason"><h3>Examens et jurys</h3><p>Évaluations sur mesure, suivi de projets étudiants.</p></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div>
      <h2>Sujets</h2>
      <ul class="chips chips--big">
        <li>Gestion de projet</li><li>Produit</li><li>Création d'entreprise</li><li>Scale-up</li><li>Finance</li><li>BI et dashboards</li><li>Étude de marché</li><li>Soft skills</li><li>Leadership</li>
      </ul>
      <p style="margin-top:24px"><a class="more" href="/{SLUGS['training']}">Voir le catalogue complet</a></p>
    </div>
    <div>
      <article class="course-card">
        <span class="tag">Exemple</span>
        <h3>Un examen d'étude de marché</h3>
        <p class="hook">Bâti autour d'une startup fictive.</p>
        <ul><li>Calé sur les concepts du cours</li><li>Pièges de causalité, logique Test &amp; Learn</li><li>Des étudiants qui raisonnent, pas qui récitent</li></ul>
      </article>
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
      <li><h3>Production</h3><p>Supports, cas, évaluations. En présentiel ou en ligne.</p></li>
      <li><h3>Animation</h3><p>Je donne les cours. On fait le bilan ensemble.</p></li>
    </ol>
  </div>
</section>

{cta_band("Un module à monter ?", "Envoyez-moi le thème, le public et les dates. Je reviens vers vous vite.", "Proposer une intervention", mailto("Proposition d intervention"), "Voir le catalogue", "/" + SLUGS["training"])}
""",
}

# ---------------------------------------------------------------- À propos
LADR = (f'<a href="{SITE["ladr_url"]}" rel="noopener">Les Architectes de la Réussite</a>' if SITE["ladr_url"] else "Les Architectes de la Réussite")

ABOUT = {
    "key": "about",
    "slug": SLUGS["about"],
    "page_type": "ProfilePage",
    "title": "Nacim Touenti — Formateur, coach, boosteur de startups et fondateur de Twty Consulting",
    "description": "Qui est Nacim Touenti ? Formateur, coach et boosteur de startups. 15+ établissements, 1000+ personnes formées, 10 ans de projets internationaux, portefeuilles de plus de 100 M€ par an.",
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
          <dt>Formation</dt><dd>Gestion de projet, produit, création d'entreprise, scale-up, finance, BI, soft skills</dd>
          <dt>Coaching</dt><dd>Dirigeants, managers, jeunes diplômés, équipes</dd>
          <dt>Secteurs</dt><dd>Banques, fintechs, retailers, digital, associations</dd>
          <dt>Langues</dt><dd>Français, anglais</dd>
          <dt>Présence</dt><dd>Paris – La Défense, Zurich, Tanger</dd>
          <dt>Profil</dt><dd><a href="{SITE['linkedin_url']}" rel="me noopener">LinkedIn</a></dd>
          <dt>Engagement</dt><dd>Fondateur de l'association {LADR}</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="proof" aria-label="En chiffres">
  <div class="wrap proof-grid">
    <div class="proof-item"><b class="num">10 ans</b><h4>de projets internationaux</h4><p>Europe et Afrique.</p></div>
    <div class="proof-item"><b class="num">100 M€+</b><h4>par an</h4><p>Portefeuilles de projets et d'opportunités.</p></div>
    <div class="proof-item"><b class="num">15+</b><h4>établissements</h4><p>Écoles, universités, centres de formation.</p></div>
    <div class="proof-item"><b class="num">1000+</b><h4>personnes formées</h4><p>Étudiants, salariés, entrepreneurs.</p></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Trois casquettes, un même socle</h2>
      <p>Le terrain. Ce que je transmets, je l'ai fait.</p>
    </div>
    <div class="reasons">
      <div class="reason"><h3>Formateur et intervenant</h3><p>À l'université comme en entreprise, en salle ou en ligne.</p></div>
      <div class="reason"><h3>Coach</h3><p>Prise de parole, leadership, confiance en soi. Pour avancer, avec le sourire.</p></div>
      <div class="reason"><h3>Boosteur de startups</h3><p>Lancer, vendre, structurer, rentabiliser. Des résultats mesurables.</p></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap measure">
    <h2>Twty Consulting</h2>
    <p>Mon cabinet de formation, de coaching et d'accompagnement. Il intervient en France, en Suisse, au Maroc et plus largement en Europe et en Afrique, en français et en anglais.</p>
  </div>
</section>

{cta_band("On travaille ensemble ?", "30 minutes pour faire connaissance et parler de votre projet. Offert.", "Prendre contact", CONTACT, "Suivre sur LinkedIn", SITE["linkedin_url"])}
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
    <p class="lead">Quelques lignes suffisent. Je vous réponds sous 48 h.</p>
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
            <option>Réserver ma séance offerte</option>
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
- [Formations]({BASE}/formations.html) : gestion de projet agile et hybride, produit et roadmap, création d'entreprise, scale-up (process commerciaux, lead generation, P&L), finance pour non-financiers, BI et tableaux de bord, soft skills et posture, fondamentaux du paiement électronique. En modules d'heures ou de jours.
- [Coaching]({BASE}/coaching.html) : prise de parole, leadership, confiance en soi, créativité, gestion du stress, création ou restructuration d'entreprise. Pour dirigeants, managers, jeunes diplômés et équipes. 1 h découverte offerte, puis accompagnement sur mesure en packs de 5 ou 10 séances.
- [Accompagnement de startups]({BASE}/accompagnement-startup.html) : lancement, développement commercial (process, lead generation, politique commerciale), process projet et produit, rentabilité (P&L). Programme Launch sur 3 mois (1 à 2 séances par semaine), à la carte, mentorat, ateliers. Références : Humen Recrut (+50 % de leads, +3 rendez-vous clients par semaine en moyenne sur 3 mois), AWA (formation stratégie et politique commerciale).
- [Centres de formation et écoles]({BASE}/centres-de-formation.html) : interventions, ingénierie pédagogique en présentiel et en ligne, modules clés en main, examens et jurys. Plus de 15 établissements (dont IUT Paris Descartes, ISG, XP School, Sorbonne, IUT Sénart, PSB), plus de 1000 personnes formées, plus de 20 modules créés.

## Personne
- [À propos de Nacim Touenti]({BASE}/nacim-touenti.html)
- LinkedIn : {SITE['linkedin_url']}
- Contact : {SITE['email']}
- Présence : Paris – La Défense, Zurich, Tanger. Langues : français, anglais.

## English
- [English version]({BASE}/en/)
"""
