"""English content of twty.fr (mirror of the French version).

Positioning: training, coaching and startup support. International project management experience
(fintech, electronic payments) is the proof of credibility, not the main offer.
"""
from parts import hero_portrait, ticker, page_hero, cta_band, mailto, faq_schema, faq_html, course_schema
from site_config import SITE

BASE = SITE["base_url"]

SLUGS = {
    "home": "index.html",
    "training": "training.html",
    "coaching": "coaching.html",
    "startups": "startup-coaching.html",
    "centres": "training-centres.html",
    "about": "nacim-touenti.html",
    "contact": "contact.html",
    "legal": "legal.html",
}


def u(key):
    return "/en/" + ("" if SLUGS[key] == "index.html" else SLUGS[key])


UI = {
    "og_locale": "en_GB",
    "og_alt": "Nacim Touenti, Twty Consulting: training, coaching and startup support",
    "skip": "Skip to content",
    "menu": "Menu",
    "nav_label": "Main navigation",
    "nav": [
        ("training", "Training"),
        ("coaching", "Coaching"),
        ("startups", "Startups"),
        ("centres", "Training centres"),
        ("about", "About"),
    ],
    "lang_switch": "FR",
    "lang_title": "Version française",
    "cta_contact": "Get in touch",
    "footer_blurb": "Training, coaching, startup support. By Nacim Touenti.",
    "footer_nav": "Site",
    "footer_contact": "Contact",
    "footer_presence": "Locations",
    "tangier": "Tangier",
    "legal": "Legal notice",
}

BIO_SHORT = (
    "Nacim Touenti is a corporate trainer, coach, university guest lecturer and startup booster, and the founder of Twty Consulting. "
    "He supports companies, training centres, startups and entrepreneurs, drawing on more than ten years "
    "of international project management."
)

BIO_LONG = (
    "Nacim Touenti is a trainer, coach and university guest lecturer. He founded Twty Consulting to train teams, "
    "coach managers and support startups. His edge: he practises what he passes on. For more than ten years "
    "he has run international projects in fintech and electronic payments, across Europe and Africa. "
    "Today he leads project management across EMEA for a global player in the sector. He created the "
    "Softies method for soft skills and runs Entrepreneur Week workshops with universities and companies. "
    "He works from Paris, Zurich and Tangier, in French and English."
)

ORG_DESCRIPTION = (
    "Training, coaching and startup support practice founded by Nacim Touenti: training for companies and "
    "training centres, one-to-one coaching, support for startups and entrepreneurs."
)

CONTACT = u("contact")

HOME_FAQ = [
    ("Do you work on site or remotely?",
     "Both. On site in Paris, Switzerland and Morocco. Remote everywhere else."),
    ("Which languages do you work in?",
     "French and English."),
    ("How does the first coaching session work?",
     "It's free. We take stock, and you leave with a first concrete action. Even if we stop there."),
    ("How soon can we start?",
     "A first 30-minute call, often within the week. Then I send you a proposal."),
]

HOME = {
    "key": "home",
    "slug": SLUGS["home"],
    "title": "Nacim Touenti — Trainer, coach, startup booster | Twty Consulting",
    "description": "Trainer, coach and startup booster. Learn, grow and perform, with a smile. 10 years of international projects, 6 years of training in companies and universities.",
    "schema": [faq_schema(HOME_FAQ, "en")],
    "body": f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Trainer, coach, startup booster.</h1>
      <p class="lead">Learn, grow and perform, with a smile. 10 years of international projects. 6 years of training on the topics that matter to you and your business.</p>
      <div class="actions">
        <a class="btn" href="{CONTACT}">Let's talk</a>
        <a class="btn btn--ghost" href="{u('training')}">See training courses</a>
      </div>
    </div>
    {hero_portrait("Portrait of Nacim Touenti (photo coming soon)", ["Trainer", "Coach", "Startup booster"], "Paris, Zurich, Tangier")}
  </div>
</section>

{ticker(['Project management', 'Product', 'Starting a business', 'Scale-up', 'Finance', 'BI and dashboards', 'Lead generation', 'Soft skills', 'Coaching', 'Leadership'], 'Topics')}
<section class="proof" aria-label="At a glance">
  <div class="wrap proof-grid">
    <div class="proof-item"><h4>10 years of international projects</h4><p>Europe and Africa, with multicultural teams.</p></div>
    <div class="proof-item"><h4>University guest lecturer</h4><p>And corporate trainer for 6 years.</p></div>
    <div class="proof-item"><h4>Instructional designer</h4><p>I create tailored courses and methods.</p></div>
  </div>
</section>

<section class="section" id="offers">
  <div class="wrap">
    <div class="section-head">
      <h2>Where do we start?</h2>
      <p>Train a team, take a step up, launch a project. Your call.</p>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Training</h3><p class="who">Companies, training centres, schools and universities</p></div>
        <p class="problem">Topics that do you good. Training you use on Monday.</p>
        <div><ul><li>Project management</li><li>Product</li><li>Starting a business</li><li>Scale-up</li></ul><a class="more" href="{u('training')}">See the catalogue</a></div>
      </article>
      <article class="offer-row">
        <div><h3>Coaching</h3><p class="who">Executives, managers, project leads, graduates</p></div>
        <p class="problem">A step to take? A decision to make? Let's work on it together.</p>
        <div><ul><li>First session free</li><li>Leadership, public speaking</li><li>Team workshops</li></ul><a class="more" href="{u('coaching')}">Explore coaching</a></div>
      </article>
      <article class="offer-row">
        <div><h3>Startup support</h3><p class="who">Founders, entrepreneurs, project owners</p></div>
        <p class="problem">An idea is good. Customers are better.</p>
        <div><ul><li>Launch programme, 3 months</li><li>Business development and sales support</li><li>Project and product processes</li><li>Mentoring for entrepreneurs</li></ul><a class="more" href="{u('startups')}">See startup support</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><h2>Why it works</h2><p>Everything is tailor-made. Every course and every coaching starts from your needs and your real cases. No standard content, no generic copy-paste or AI-generated approach.</p></div>
    <div class="reasons reasons--four">
      <div class="reason"><h3>Hands-on from Monday</h3><p>Tools tested on real projects, not theory.</p></div>
      <div class="reason"><h3>Teams that get involved</h3><p>Role play, games, debate. Nobody switches off.</p></div>
      <div class="reason"><h3>With a smile</h3><p>People learn better when they enjoy it. That's my method.</p></div>
      <div class="reason"><h3>Visible results</h3><p>You see the difference in your teams, not just on an attendance sheet.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Selected work</h2><p>Want the details? I'll tell you in person.</p></div>
    <div class="cases">
      <article class="case"><span class="tag">Training</span><h3>University programme design</h3><p>Courses built on real business cases.</p></article>
      <article class="case"><span class="tag">Coaching</span><h3>The Softies method</h3><p>My soft-skills method, launched in several countries.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Entrepreneur Week</h3><p>Workshops with universities and companies. The goal: new projects.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Mentoring future entrepreneurs</h3><p>From idea to execution, alongside project owners.</p></article>
      <article class="case"><span class="tag">Management</span><h3>International launches</h3><p>Rollouts in several countries. Teams from every culture.</p></article>
      <article class="case"><span class="tag">Management</span><h3>Mobile wallet in Africa</h3><p>Mobile financial services for the unbanked.</p></article>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div><h2>Frequently asked questions</h2><p class="lead">Another question? <a href="{CONTACT}">Write to me</a>.</p></div>
    <div class="faq">{faq_html(HOME_FAQ)}</div>
  </div>
</section>

{cta_band("A project? A team to grow?", "30 minutes to talk it through. Free, no strings.", "Book a call", CONTACT, "WhatsApp", SITE["whatsapp_url"])}
""",
}

CATALOG = [
    ("Run your projects", [
        {"id": "project-management", "name": "Agile and hybrid project management",
         "hook": "Deliver on time. Without burning out the team.",
         "topics": ["Pick the right method, agile or hybrid", "Clear, shared project processes", "Reporting leaders actually read", "Get a project back on track"],
         "for": "Project managers, managers, tech teams"},
        {"id": "product", "name": "Product: from idea to roadmap",
         "hook": "Build the right product, in the right order.",
         "topics": ["Roadmap and prioritisation", "Project and product processes", "Automating repetitive work", "Test before you invest"],
         "for": "Product owners, founders, product teams"},
    ]),
    ("Start and grow", [
        {"id": "starting-a-business", "name": "Starting a business",
         "hook": "From idea to first customer. Without getting lost on the way.",
         "topics": ["Target and value proposition", "Market research and Test & Learn", "A realistic roadmap", "Pitch and first meetings"],
         "for": "Project owners, student entrepreneurs, incubatees"},
        {"id": "scale-up", "name": "Scale-up: structuring growth",
         "hook": "Sell more. And earn more from every sale.",
         "topics": ["Sales processes and sales policy", "Lead generation", "P&L and profitability optimisation", "Automate to scale"],
         "for": "Leaders of growing startups and SMEs"},
    ]),
    ("Finance and data", [
        {"id": "finance", "name": "Finance for non-financial people",
         "hook": "Understand the numbers to decide better. Beginner or refresher level.",
         "topics": ["Read a balance sheet and P&L", "Cash, margins, profitability", "Build and track a budget", "Speak the same language as finance"],
         "for": "Managers, entrepreneurs, students"},
        {"id": "bi-dashboards", "name": "BI and dashboards",
         "hook": "Tools that show what matters, at a glance.",
         "topics": ["Pick the right indicators", "Design useful dashboards", "Build tailored tools for the business", "Automate data collection"],
         "for": "Leaders, managers, operations teams"},
    ]),
    ("Presence and industry expertise", [
        {"id": "soft-skills", "name": "Soft skills and professional presence",
         "hook": "Speak with confidence. Negotiate without friction. Find your place.",
         "topics": ["Public speaking and persuasion", "Negotiation and handling tension", "Professional presence and leadership"],
         "for": "Managers, teams, students and graduates"},
        {"id": "electronic-payments", "name": "Electronic payments fundamentals",
         "hook": "For fintech teams: what really happens when you pay by card.",
         "topics": ["The journey of a card transaction", "EMV, contactless, SoftPOS", "PCI DSS and certifications"],
         "for": "Product, project and support teams in fintech"},
    ]),
]
COURSES = [c for _, group in CATALOG for c in group]


def course_html(c):
    topics = "".join(f"<li>{t}</li>" for t in c["topics"])
    return f"""<article class="course-card" id="{c['id']}">
  <h3>{c['name']}</h3>
  <p class="hook">{c['hook']}</p>
  <ul>{topics}</ul>
  <p class="for"><b>For:</b> {c['for']}</p>
  <a class="more" href="{mailto('Programme: ' + c['name'])}">Request the programme</a>
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
    "title": "Project management, product, business creation, finance and BI training | Nacim Touenti",
    "description": "Tailored training in project management, product, starting a business, scale-up, finance, BI and soft skills. Hours or days, in companies and schools, by Nacim Touenti.",
    "schema": [course_schema(c["name"], c["hook"], "en", f"{BASE}/en/{SLUGS['training']}#{c['id']}") for c in COURSES],
    "body": page_hero(
        '<a href="/en/">Home</a> / Training',
        "Training that does you good.",
        "Project management, product, starting a business, scale-up, finance, BI. Tailored, hands-on, usable on Monday.",
        "formation.webp",
        "Interactive small-group training session",
        f'<div class="actions"><a class="btn" href="#catalogue">See the catalogue</a><a class="btn btn--ghost" href="{CONTACT}">Request a tailored course</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>My method</h2>
      <p class="measure">No lectures. Your teams negotiate, present and decide. Sometimes they fail, on purpose. That's how it sticks.</p>
    </div>
    <ul class="ticks">
      <li>Role play and real case studies</li>
      <li>Serious games that make people think</li>
      <li>A debrief after every exercise</li>
      <li>Miro, quizzes, live polls</li>
    </ul>
  </div>
</section>

<section class="section section--mist" id="catalogue">
  <div class="wrap">
    <div class="section-head"><h2>Catalogue</h2><p>Everything adapts: length, level, examples from your industry.</p></div>
    {catalog_html()}
    <p class="catalog-note">Modules of a few hours or several days. On site or remote. In companies, schools or training centres. Price on quotation.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>From brief to classroom</h2></div>
    <ol class="steps">
      <li><h3>Design</h3><p>We start from your goals. I build hands-on modules.</p></li>
      <li><h3>Pilot</h3><p>A trial with real participants. We adjust.</p></li>
      <li><h3>Validation</h3><p>You review. We refine.</p></li>
      <li><h3>Delivery</h3><p>On site or remote. With learning assessment.</p></li>
    </ol>
  </div>
</section>

{cta_band("A team to train?", "Tell me who, what and when. I'll send you a programme.", "Request training", CONTACT, "For training centres", u("centres"))}
""",
}

COACHING = {
    "key": "coaching",
    "slug": SLUGS["coaching"],
    "title": "Coaching: public speaking, leadership, self-confidence, stress management | Nacim Touenti",
    "description": "Tailored coaching for executives, managers, graduates and teams: public speaking, leadership, self-confidence, creativity, stress management, starting or restructuring a business. First hour free.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Coaching',
        "A step to take? Let's do it together.",
        "Executives, managers, graduates. I help you step back, decide faster and have more impact. Always tailored. First session free.",
        "coaching.webp",
        "Two professionals walking together in the city",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Book my free session</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>What we work on</h2></div>
    <ul class="chips chips--big">
      <li>Public speaking</li><li>Leadership</li><li>Self-confidence</li><li>Creativity</li><li>Stress management</li><li>Starting or restructuring a business</li>
    </ul>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head"><h2>Who is it for?</h2></div>
    <div class="course-grid">
      <article class="course-card"><h3>Executives and founders</h3><p class="hook">Alone with the decisions? A field-tested view to help you decide.</p><ul><li>Leadership</li><li>Stress management</li><li>Starting or restructuring a business</li></ul></article>
      <article class="course-card"><h3>Managers and project leads</h3><p class="hook">New role, bigger team, project under pressure.</p><ul><li>Public speaking</li><li>Leadership</li><li>Self-confidence</li></ul></article>
      <article class="course-card"><h3>Students and graduates</h3><p class="hook">First job or first company? Go in with a plan.</p><ul><li>Self-confidence</li><li>Public speaking</li><li>Career plan</li></ul></article>
      <article class="course-card"><h3>Teams</h3><p class="hook">Align, re-energise, move forward together.</p><ul><li>Creativity</li><li>Team cohesion</li><li>Strategy workshops</li></ul></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Formats</h2></div>
    <div class="reasons">
      <div class="reason"><h3>1-hour discovery</h3><p>Free. We take stock, no commitment.</p></div>
      <div class="reason"><h3>Tailored</h3><p>Support built around your goals.</p></div>
      <div class="reason"><h3>Packs of 5 or 10 sessions</h3><p>At the pace that suits you.</p></div>
      <div class="reason"><h3>Team workshop</h3><p>To move forward together, in your company.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><h2>How it works</h2></div>
    <ol class="steps">
      <li><h3>Free session</h3><p>1 hour to take stock. No commitment.</p></li>
      <li><h3>Goals</h3><p>Two or three concrete goals. No more.</p></li>
      <li><h3>Sessions</h3><p>In packs of 5 or 10, at your pace.</p></li>
      <li><h3>Review</h3><p>We measure the progress. You carry on alone.</p></li>
    </ol>
  </div>
</section>

{cta_band("Ready for the next step?", "The first hour is free. You have nothing to lose.", "Book my free session", CONTACT, "WhatsApp", SITE["whatsapp_url"])}
""",
}

STARTUPS = {
    "key": "startups",
    "slug": SLUGS["startups"],
    "title": "Startup booster: launch, sales development, processes, profitability | Nacim Touenti",
    "description": "Support for startups and SMEs: launch, sales processes, lead generation, project and product processes, P&L. 3-month Launch programme, à la carte, mentoring. Example: +50% leads at Humen Recrut.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Startups',
        "Startup booster.",
        "Frame, test, sell, structure. I help you through every stage, with field-tested methods. Always tailored.",
        "startups.webp",
        "Startup team working on a roadmap",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Book a discovery call</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Where I step in</h2></div>
    <div class="course-grid">
      <article class="course-card"><h3>Launch</h3><p class="hook">From idea to first customers.</p><ul><li>Target and value proposition</li><li>Market research, quick tests</li><li>Pitch and first meetings</li></ul></article>
      <article class="course-card"><h3>Sell</h3><p class="hook">More leads, more meetings, more customers.</p><ul><li>Sales processes</li><li>Lead generation and automation</li><li>Sales policy, team training</li></ul></article>
      <article class="course-card"><h3>Structure</h3><p class="hook">Processes that hold as the team grows.</p><ul><li>Project and product processes</li><li>Roadmap and priorities</li><li>Automating repetitive work</li></ul></article>
      <article class="course-card"><h3>Make it profitable</h3><p class="hook">Grow, yes. And make money doing it.</p><ul><li>Reading and steering the P&amp;L</li><li>Profitability optimisation</li><li>Management dashboards</li></ul></article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><h2>Real results</h2></div>
    <article class="case-study">
      <div>
        <span class="tag">Sales development</span>
        <h3>Humen Recrut</h3>
        <p>Sales structure overhaul, process set-up, training of the sales team and SDRs, automated lead generation.</p>
      </div>
      <div class="stats">
        <div class="stat"><b>+50%</b><span>more leads</span></div>
        <div class="stat"><b>+3</b><span>customer meetings a week, on average over 3 months</span></div>
      </div>
    </article>
    <article class="case-study case-study--small">
      <div>
        <span class="tag">Training</span>
        <h3>AWA</h3>
        <p>Team training on sales strategy and sales policy.</p>
      </div>
    </article>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Formats</h2></div>
    <div class="reasons">
      <div class="reason"><h3>Launch programme</h3><p>3 months, 1 to 2 sessions a week. Dedicated weeks if needed.</p></div>
      <div class="reason"><h3>À la carte</h3><p>One specific topic, including a project to turn around.</p></div>
      <div class="reason"><h3>Mentoring</h3><p>Regular check-ins to stay on course.</p></div>
      <div class="reason"><h3>Workshops</h3><p>For incubators and schools, on the Entrepreneur Week model.</p></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div>
      <h2>My rules</h2>
      <ul class="ticks"><li>Talk to customers before you build</li><li>Test small before you invest big</li><li>Clear priorities every week</li><li>Results, not slides</li></ul>
    </div>
    <div>
      <h2>What I steer clear of</h2>
      <ul class="ticks cross"><li>Business plans nobody reads</li><li>Copy-paste methods</li><li>Unclear roles</li><li>Meetings with no decision</li></ul>
    </div>
  </div>
</section>

{cta_band("Go from idea to action.", "30 minutes to review your project. Free.", "Book a discovery call", CONTACT, "WhatsApp", SITE["whatsapp_url"])}
""",
}

CENTRES = {
    "key": "centres",
    "slug": SLUGS["centres"],
    "title": "Guest lecturer and instructional designer for schools, universities and training centres | Nacim Touenti",
    "description": "Tailored modules designed and delivered, on site and online. 15+ institutions, 1,000+ people trained, 20+ modules created: IUT Paris Descartes, ISG, XP School, Sorbonne, IUT Sénart, PSB.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Training centres',
        "Your modules, designed and delivered end to end.",
        "Schools, universities, training centres. A university guest lecturer and corporate trainer for 6 years, I design and deliver hands-on, tailored modules, on site and online.",
        "centres.webp",
        "Trainer running a participatory workshop",
        f'<div class="actions"><a class="btn" href="{mailto("Teaching proposal")}">Propose a session</a></div>',
    ) + f"""
<section class="proof" aria-label="In figures">
  <div class="wrap proof-grid">
    <div class="proof-item"><b class="num">15+</b><h4>institutions</h4><p>Schools, universities, training centres.</p></div>
    <div class="proof-item"><b class="num">1,000+</b><h4>people trained</h4><p>Students, employees, entrepreneurs.</p></div>
    <div class="proof-item"><b class="num">20+</b><h4>modules created</h4><p>Tailor-made, end to end.</p></div>
  </div>
  <div class="wrap trust">
    <p>They have trusted me</p>
    <ul class="chips"><li>IUT Paris Descartes</li><li>ISG</li><li>XP School</li><li>Sorbonne</li><li>IUT Sénart</li><li>PSB</li></ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>What I bring</h2></div>
    <div class="reasons">
      <div class="reason"><h3>Teaching</h3><p>Short modules, masterclasses, talks.</p></div>
      <div class="reason"><h3>Instructional design</h3><p>Courses built for the classroom and for online.</p></div>
      <div class="reason"><h3>Turnkey modules</h3><p>Syllabus, materials and case studies included.</p></div>
      <div class="reason"><h3>Exams and juries</h3><p>Tailored assessments, student project follow-up.</p></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div>
      <h2>Subjects</h2>
      <ul class="chips chips--big"><li>Project management</li><li>Product</li><li>Starting a business</li><li>Scale-up</li><li>Finance</li><li>BI and dashboards</li><li>Market research</li><li>Soft skills</li><li>Leadership</li></ul>
      <p style="margin-top:24px"><a class="more" href="{u('training')}">See the full catalogue</a></p>
    </div>
    <div>
      <article class="course-card">
        <span class="tag">Example</span>
        <h3>A market research exam</h3>
        <p class="hook">Built around a fictional startup.</p>
        <ul><li>Aligned with the course concepts</li><li>Causality traps, Test &amp; Learn logic</li><li>Students who reason, not recite</li></ul>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><h2>How we work</h2></div>
    <ol class="steps">
      <li><h3>Brief</h3><p>Audience, outcomes, hours. You brief me.</p></li>
      <li><h3>Proposal</h3><p>Detailed programme and quotation.</p></li>
      <li><h3>Production</h3><p>Materials, cases, assessments. On site or online.</p></li>
      <li><h3>Delivery</h3><p>I teach. We review together.</p></li>
    </ol>
  </div>
</section>

{cta_band("A module to set up?", "Send me the topic, audience and dates. I'll get back to you fast.", "Propose a session", mailto("Teaching proposal"), "See the catalogue", u("training"))}
""",
}

ABOUT = {
    "key": "about",
    "slug": SLUGS["about"],
    "page_type": "ProfilePage",
    "title": "Nacim Touenti — Trainer, coach, startup booster and founder of Twty Consulting",
    "description": "Who is Nacim Touenti? Trainer, coach, university guest lecturer and startup booster, founder of Twty Consulting, with 10+ years of international project management.",
    "body": f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/en/">Home</a> / About</p>
    <div class="about-grid">
      <div class="portrait" role="img" aria-label="Portrait of Nacim Touenti (photo coming soon)">NT</div>
      <div>
        <h1>Nacim Touenti</h1>
        <p class="lead">Trainer, coach, startup booster. And still an international project manager.</p>
        <p class="measure">{BIO_LONG}</p>
        <dl class="facts">
          <dt>Training</dt><dd>Project management, leadership, soft skills, market research, entrepreneurship</dd>
          <dt>Coaching</dt><dd>Executives, managers, project leads, graduates</dd>
          <dt>Experience</dt><dd>10+ years managing international projects (fintech, payments)</dd>
          <dt>Languages</dt><dd>French, English</dd>
          <dt>Locations</dt><dd>Paris – La Défense, Zurich, Tangier</dd>
          <dt>Profile</dt><dd><a href="{SITE['linkedin_url']}" rel="me noopener">LinkedIn</a></dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Three hats, one obsession</h2><p>That people really improve.</p></div>
    <div class="reasons">
      <div class="reason"><h3>Trainer and guest lecturer</h3><p>At university and in companies. I design and I teach.</p></div>
      <div class="reason"><h3>Coach and mentor</h3><p>I created the Softies method. I coach managers and executives. I mentor entrepreneurs.</p></div>
      <div class="reason"><h3>Hands-on manager</h3><p>I run projects across EMEA. Several countries, several cultures, tight deadlines.</p></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap measure">
    <h2>Twty Consulting</h2>
    <p>{ORG_DESCRIPTION} The practice works in France, Switzerland, Morocco and more broadly across Europe and Africa, in French and English.</p>
    <div class="actions"><a class="btn" href="{CONTACT}">Get in touch</a><a class="btn btn--ghost" href="{SITE['linkedin_url']}" rel="me noopener">Follow on LinkedIn</a></div>
  </div>
</section>
""",
}

CONTACT_PAGE = {
    "key": "contact",
    "slug": SLUGS["contact"],
    "page_type": "ContactPage",
    "title": "Contact — Nacim Touenti | Twty Consulting",
    "description": "Contact Nacim Touenti about training, coaching or startup support. Email, WhatsApp, LinkedIn. Paris, Zurich, Tangier.",
    "body": f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/en/">Home</a> / Contact</p>
    <h1>Let's talk</h1>
    <p class="lead">A few lines are enough. I'll reply fast, with a 30-minute slot.</p>
  </div>
</section>
<section class="section">
  <div class="wrap contact-grid">
    <form class="form" id="contact-form" data-email="{SITE['email']}" data-subject="Enquiry via twty.fr">
      <div class="row">
        <label>Name<input name="name" autocomplete="name" required></label>
        <label>Email<input name="email" type="email" autocomplete="email" required></label>
      </div>
      <div class="row">
        <label>Organisation<input name="organisation" autocomplete="organization"></label>
        <label>Your need
          <select name="need">
            <option>Training for my team</option>
            <option>One-to-one coaching</option>
            <option>Startup support</option>
            <option>Teaching at a training centre or school</option>
            <option>Other</option>
          </select>
        </label>
      </div>
      <label>Message<textarea name="message" rows="6" required></textarea></label>
      <div><button class="btn" type="submit">Prepare the email</button></div>
      <p class="hint">The button opens your email app with your message ready to send to {SITE['email']}.</p>
    </form>
    <aside>
      <ul class="channels">
        <li><b>Email</b><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
        <li><b>WhatsApp</b><a href="{SITE['whatsapp_url']}" rel="noopener">Message on WhatsApp</a></li>
        <li><b>LinkedIn</b><a href="{SITE['linkedin_url']}" rel="me noopener">Nacim Touenti</a></li>
      </ul>
      <div class="offices">
        <p><b>Paris – La Défense</b><br>Courbevoie, France</p>
        <p><b>Zurich</b><br>Wallisellen, Switzerland<br><a href="tel:{SITE['phone_ch'].replace(' ', '')}">{SITE['phone_ch']}</a></p>
        <p><b>Tangier</b><br>Morocco<br><a href="tel:{SITE['phone_ma'].replace(' ', '')}">{SITE['phone_ma']}</a></p>
      </div>
    </aside>
  </div>
</section>
""",
}

LEGAL = {
    "key": "legal",
    "slug": SLUGS["legal"],
    "title": "Legal notice | Twty Consulting",
    "description": "Legal notice and privacy policy of twty.fr.",
    "body": f"""
<section class="section">
  <div class="wrap legal">
    <h1>Legal notice</h1>
    <h2>Publisher</h2>
    <p>Twty Consulting — [legal form and company number to be completed]<br>
    Publication director: Nacim Touenti<br>
    Address: [registered address to be completed]<br>
    Email: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
    <h2>Hosting</h2>
    <p>GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA.</p>
    <h2>Intellectual property</h2>
    <p>Texts, visuals, logos and content on this site belong to Twty Consulting unless stated otherwise. Reproduction without permission is prohibited.</p>
    <h2>Personal data</h2>
    <p>This site stores no data you type: the contact form prepares an email in your own email app. Emails received are used only to answer your request and are never shared. Under the GDPR, you can ask to access, correct or delete your data by writing to <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
    <h2>Cookies</h2>
    <p>This site uses no advertising cookies and no audience measurement. Fonts are loaded from Google Fonts, which sends your IP address to Google when pages are displayed.</p>
  </div>
</section>
""",
}

PAGES = [HOME, TRAINING, COACHING, STARTUPS, CENTRES, ABOUT, CONTACT_PAGE, LEGAL]
