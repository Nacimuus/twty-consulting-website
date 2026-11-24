"""Blocs HTML réutilisés par content_fr.py et content_en.py."""
from site_config import SITE

CONTACTLESS = (
    '<svg class="contactless" viewBox="0 0 30 30" aria-hidden="true">'
    '<path d="M9 8c3 4 3 10 0 14"/><path d="M14 5c4.5 5.5 4.5 14.5 0 20"/>'
    '<path d="M19 2c6 7 6 19 0 26"/></svg>'
)


def pay_card(role_label, role, presence_label, presence):
    return f"""<div class="card-stage" aria-hidden="true">
  <svg class="waves" viewBox="0 0 120 120"><path d="M40 40c12 12 12 28 0 40"/><path d="M58 28c18 18 18 46 0 64"/><path d="M76 16c24 24 24 64 0 88"/></svg>
  <div class="pay-card">
    <div class="pay-card__top">
      <div class="pay-card__brand">Twty<small>CONSULTING</small></div>
      {CONTACTLESS}
    </div>
    <div class="pay-card__mid"><span class="chip"></span></div>
    <div>
      <div class="pay-card__name">NACIM TOUENTI</div>
      <div class="pay-card__foot">
        <div class="pay-card__meta"><b>{role_label}</b>{role}</div>
        <div class="pay-card__meta" style="text-align:right"><b>{presence_label}</b>{presence}</div>
      </div>
    </div>
  </div>
</div>"""


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
