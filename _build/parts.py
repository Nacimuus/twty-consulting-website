"""Blocs HTML réutilisés par content_fr.py et content_en.py."""
from site_config import SITE

def hero_portrait(alt, roles, caption):
    """Portrait de Nacim au centre d'un système orbital, avec ses trois métiers.

    Pour passer à la photo : déposer assets/img/nacim-touenti.webp et remplacer
    <div class="portrait portrait--hero" ...>NT</div> par
    <img class="portrait portrait--hero" src="/assets/img/nacim-touenti.webp" alt="...">.
    """
    items = "".join(f"<li>{r}</li>" for r in roles)
    return f"""<div class="hero-visual">
  <div class="orbit orbit--3" aria-hidden="true"></div>
  <div class="orbit orbit--1" aria-hidden="true"><span class="sat"></span></div>
  <div class="orbit orbit--2" aria-hidden="true"><span class="sat"></span></div>
  <div class="portrait portrait--hero" role="img" aria-label="{alt}">NT</div>
  <ul class="role-tags">{items}</ul>
  <p class="role-place">{caption}</p>
</div>"""


def ticker(words, label):
    items = "".join(f"<span>{w}</span>" for w in words)
    return f"""<div class="ticker" role="region" aria-label="{label}">
  <div class="ticker__track"><div style="display:flex">{items}</div><div style="display:flex" aria-hidden="true">{items}</div></div>
</div>
"""


def page_hero(crumbs, h1, lead, img=None, alt="", actions=""):
    figure = ""
    if img:
        figure = f'<figure><img src="/assets/img/{img}" alt="{alt}" width="1400" height="1050" fetchpriority="high"></figure>'
    grid_open = '<div class="page-hero-grid">' if img else "<div>"
    return f"""<section class="page-hero">
  <div class="wrap">
    {grid_open}
      <div>
        <p class="crumbs">{crumbs}</p>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        {actions}
      </div>
      {figure}
    </div>
  </div>
</section>
"""


def cta_band(h2, p, primary_label, primary_href, secondary_label=None, secondary_href=None):
    second = ""
    if secondary_label:
        second = f'<a class="btn btn--light" href="{secondary_href}">{secondary_label}</a>'
    return f"""<section class="cta-band">
  <div class="wrap">
    <h2>{h2}</h2>
    <p>{p}</p>
    <div class="actions">
      <a class="btn btn--gold" href="{primary_href}">{primary_label}</a>
      {second}
    </div>
  </div>
</section>
"""


def mailto(subject):
    from urllib.parse import quote
    return f"mailto:{SITE['email']}?subject={quote(subject)}"


def faq_schema(qa, lang):
    return {
        "@type": "FAQPage",
        "inLanguage": lang,
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def faq_html(qa):
    return "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qa)


def course_schema(name, desc, lang, url):
    return {
        "@type": "Course",
        "name": name,
        "description": desc,
        "inLanguage": lang,
        "url": url,
        "provider": {"@id": SITE["base_url"] + "/#organisation"},
        "instructor": {"@id": SITE["base_url"] + "/#nacim-touenti"},
        "hasCourseInstance": {"@type": "CourseInstance", "courseMode": ["Onsite", "Online"]},
    }
