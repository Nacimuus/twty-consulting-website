#!/usr/bin/env python3
"""Générateur du site statique twty.fr.

Usage : python3 _build/build.py   (depuis la racine du dépôt)

Le contenu vit dans _build/content_fr.py et _build/content_en.py.
Le dossier _build n'est pas publié par GitHub Pages (préfixe « _ »).
Chaque page générée contient l'en-tête, le pied de page et les métadonnées
SEO directement dans le HTML (plus de chargement par JavaScript).
"""
import json
import os
import sys
from datetime import date
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import content_fr  # noqa: E402
import content_en  # noqa: E402
from site_config import SITE  # noqa: E402

LANGS = {"fr": content_fr, "en": content_en}
TODAY = date.today().isoformat()


def url_for(lang, slug):
    prefix = "/" if lang == "fr" else "/en/"
    if slug == "index.html":
        return prefix
    return prefix + slug


def abs_url(lang, slug):
    return SITE["base_url"] + url_for(lang, slug)


def graph_base():
    person = {
        "@type": "Person",
        "@id": SITE["base_url"] + "/#nacim-touenti",
        "name": "Nacim Touenti",
        "givenName": "Nacim",
        "familyName": "Touenti",
        "url": SITE["base_url"] + "/nacim-touenti.html",
        "jobTitle": SITE["job_title_fr"],
        "description": content_fr.BIO_SHORT,
        "worksFor": {"@id": SITE["base_url"] + "/#organisation"},
        "knowsAbout": SITE["knows_about"],
        "knowsLanguage": ["fr", "en"],
        "sameAs": SITE["same_as"],
        "email": "mailto:" + SITE["email"],
    }
    org = {
        "@type": "ProfessionalService",
        "@id": SITE["base_url"] + "/#organisation",
        "name": "Twty Consulting",
        "url": SITE["base_url"] + "/",
        "logo": SITE["base_url"] + "/assets/img/logo-twty.png",
        "image": SITE["base_url"] + "/assets/img/og-twty.jpg",
        "email": SITE["email"],
        "founder": {"@id": SITE["base_url"] + "/#nacim-touenti"},
        "description": content_fr.ORG_DESCRIPTION,
        "areaServed": ["France", "Suisse", "Maroc", "Europe", "Afrique"],
        "address": [
            {"@type": "PostalAddress", "addressLocality": "Courbevoie (Paris La Défense)", "addressCountry": "FR"},
            {"@type": "PostalAddress", "addressLocality": "Wallisellen (Zurich)", "addressCountry": "CH"},
            {"@type": "PostalAddress", "addressLocality": "Tanger", "addressCountry": "MA"},
        ],
        "sameAs": SITE["same_as"],
    }
    website = {
        "@type": "WebSite",
        "@id": SITE["base_url"] + "/#site",
        "url": SITE["base_url"] + "/",
        "name": "Twty Consulting",
        "inLanguage": ["fr", "en"],
        "publisher": {"@id": SITE["base_url"] + "/#organisation"},
    }
    return [person, org, website]


def render_head(lang, page, alternates):
    ui = LANGS[lang].UI
    title = escape(page["title"])
    desc = escape(page["description"])
    canonical = abs_url(lang, page["slug"])
    og_image = SITE["base_url"] + "/assets/img/og-twty.jpg"
    links = []
    for alt_lang, alt_slug in alternates.items():
        links.append(f'<link rel="alternate" hreflang="{alt_lang}" href="{abs_url(alt_lang, alt_slug)}">')
    if "fr" in alternates:
        links.append(f'<link rel="alternate" hreflang="x-default" href="{abs_url("fr", alternates["fr"])}">')
    graph = graph_base() + page.get("schema", [])
    webpage = {
        "@type": page.get("page_type", "WebPage"),
        "@id": canonical + "#page",
        "url": canonical,
        "name": page["title"],
        "description": page["description"],
        "inLanguage": lang,
        "isPartOf": {"@id": SITE["base_url"] + "/#site"},
        "dateModified": TODAY,
    }
    if page.get("page_type") == "ProfilePage":
        webpage["mainEntity"] = {"@id": SITE["base_url"] + "/#nacim-touenti"}
    graph.append(webpage)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    robots = '<meta name="robots" content="noindex">' if page.get("noindex") else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Nacim Touenti">
{robots}
<link rel="canonical" href="{canonical}">
{chr(10).join(links)}
<meta property="og:type" content="{'profile' if page.get('page_type') == 'ProfilePage' else 'website'}">
<meta property="og:site_name" content="Twty Consulting">
<meta property="og:locale" content="{ui['og_locale']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{escape(ui['og_alt'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
<meta name="theme-color" content="#0e4b5d">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/favicon/apple-icon-180x180.png">
<link rel="manifest" href="/favicon/manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css?v={TODAY}">
<script type="application/ld+json">
{ld}
</script>
</head>
"""


def render_header(lang, page, alternates):
    ui = LANGS[lang].UI
    items = []
    for key, label in ui["nav"]:
        slug = LANGS[lang].SLUGS[key]
        current = ' aria-current="page"' if key == page["key"] else ""
        items.append(f'<li><a href="{url_for(lang, slug)}"{current}>{label}</a></li>')
    other = "en" if lang == "fr" else "fr"
    other_slug = alternates.get(other, "index.html")
    contact_url = url_for(lang, LANGS[lang].SLUGS["contact"])
    return f"""<body>
<a class="skip" href="#contenu">{ui['skip']}</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{url_for(lang, 'index.html')}">
      <img src="/assets/img/logo-twty.webp" alt="Twty Consulting" width="63" height="52">
      <span>Nacim Touenti<small>Twty Consulting</small></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu">{ui['menu']}</button>
    <nav class="nav-menu" id="menu" aria-label="{ui['nav_label']}">
      <ul>
        {chr(10).join('        ' + i for i in items).strip()}
      </ul>
      <a class="lang" href="{url_for(other, other_slug)}" hreflang="{other}" lang="{other}" title="{ui['lang_title']}">{ui['lang_switch']}</a>
      <a class="btn btn--small" href="{contact_url}">{ui['cta_contact']}</a>
    </nav>
  </div>
</header>
<main id="contenu">
"""


def render_footer(lang):
    ui = LANGS[lang].UI
    S = LANGS[lang].SLUGS
    offer_links = "\n".join(
        f'<li><a href="{url_for(lang, S[k])}">{label}</a></li>' for k, label in ui["nav"]
    )
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/img/logo-twty.webp" alt="Twty Consulting" width="77" height="64" loading="lazy">
        <p>{ui['footer_blurb']}</p>
      </div>
      <div>
        <h4>{ui['footer_nav']}</h4>
        <ul>
{offer_links}
        </ul>
      </div>
      <div>
        <h4>{ui['footer_contact']}</h4>
        <ul>
          <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li><a href="{SITE['whatsapp_url']}" rel="noopener">WhatsApp</a></li>
          <li><a href="{SITE['linkedin_url']}" rel="noopener me">LinkedIn</a></li>
        </ul>
      </div>
      <div>
        <h4>{ui['footer_presence']}</h4>
        <ul>
          <li>Paris – La Défense</li>
          <li>Zurich</li>
          <li>{ui['tangier']}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="mt-0">© {date.today().year} Twty Consulting — Nacim Touenti</p>
      <p class="mt-0"><a href="{url_for(lang, S['legal'])}">{ui['legal']}</a></p>
    </div>
  </div>
</footer>
<script src="/assets/js/site.js?v={TODAY}" defer></script>
</body>
</html>
"""


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)


def build_pages():
    entries = []
    for lang, mod in LANGS.items():
        for page in mod.PAGES:
            alternates = {}
            for l2, m2 in LANGS.items():
                if page["key"] in m2.SLUGS:
                    alternates[l2] = m2.SLUGS[page["key"]]
            html = render_head(lang, page, alternates) + render_header(lang, page, alternates) + page["body"] + render_footer(lang)
            out = page["slug"] if lang == "fr" else "en/" + page["slug"]
            write(out, html)
            if not page.get("noindex"):
                entries.append((lang, page, alternates))
    return entries


def build_redirects():
    for old, new in SITE["redirects"].items():
        write(old, f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>Page déplacée — Twty Consulting</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{SITE['base_url']}{new}">
<meta http-equiv="refresh" content="0; url={new}">
</head><body><p>Cette page a déménagé : <a href="{new}">{SITE['base_url']}{new}</a></p></body></html>
""")


def build_sitemap(entries):
    rows = []
    for lang, page, alternates in entries:
        alts = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{abs_url(l, s)}"/>' for l, s in alternates.items()
        )
        prio = "1.0" if page["key"] == "home" else "0.8"
        rows.append(f"""  <url>
    <loc>{abs_url(lang, page['slug'])}</loc>
    <lastmod>{TODAY}</lastmod>
    <priority>{prio}</priority>{alts}
  </url>""")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE['base_url']}/sitemap.xml\n")


def main():
    entries = build_pages()
    build_redirects()
    build_sitemap(entries)
    write("llms.txt", content_fr.LLMS_TXT.strip() + "\n")
    print(f"{len(entries)} pages indexables générées, {len(SITE['redirects'])} redirections.")


if __name__ == "__main__":
    main()
