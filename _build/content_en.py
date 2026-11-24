"""English content of twty.fr (mirror of the French version).

Positioning: training, coaching and startup support. International project management experience
(fintech, electronic payments) is the proof of credibility, not the main offer.
"""
from parts import hero_portrait, page_hero, cta_band, mailto, faq_schema, faq_html, course_schema
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
    "footer_blurb": "Twty Consulting, Nacim Touenti's practice: training, coaching and support for startups and entrepreneurs.",
    "footer_nav": "Site",
    "footer_contact": "Contact",
    "footer_presence": "Locations",
    "tangier": "Tangier",
    "legal": "Legal notice",
}

BIO_SHORT = (
    "Nacim Touenti is a trainer, coach and university lecturer, and the founder of Twty Consulting. "
    "He supports companies, training centres, startups and entrepreneurs, drawing on more than ten years "
    "of international project management."
)

BIO_LONG = (
    "Nacim Touenti is a trainer, coach and university lecturer, and the founder of Twty Consulting. "
    "He designs and delivers training in project management, leadership, soft skills, market research and "
    "entrepreneurship, coaches executives, managers and graduates, and supports startups and entrepreneurs "
    "from idea to launch. His teaching draws on more than ten years of managing international projects in "
    "fintech and electronic payments across Europe and Africa: he currently leads project management across "
    "EMEA for a global player in the sector. He created the Softies soft-skills method and runs Entrepreneur "
    "Week workshops with universities and companies. Twty Consulting works from Paris, Zurich and Tangier, "
    "in French and English."
)

ORG_DESCRIPTION = (
    "Training, coaching and startup support practice founded by Nacim Touenti: training for companies and "
    "training centres, one-to-one coaching, support for startups and entrepreneurs."
)

CONTACT = u("contact")

HOME_FAQ = [
    ("Do you work on site or remotely?",
     "Both. I work on site in Paris, Switzerland and Morocco, and remotely everywhere else."),
    ("Which languages do you work in?",
     "French and English, for both training and coaching."),
    ("How does the first coaching session work?",
     "It's free. We review your situation and goals, and you leave with a first concrete step, whether or not you continue."),
    ("How soon can we start?",
     "A first 30-minute call can usually happen within the week. It scopes your need so I can send you a proposal."),
]

HOME = {
    "key": "home",
    "slug": SLUGS["home"],
    "title": "Nacim Touenti — Trainer, coach and lecturer | Twty Consulting",
    "description": "Nacim Touenti, trainer, coach and university lecturer. Training, coaching and startup support, backed by 10+ years of international project management.",
    "schema": [faq_schema(HOME_FAQ, "en")],
    "body": f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Train, coach, support. Help people and their projects grow.</h1>
      <p class="lead">I'm Nacim Touenti, a trainer, coach and university lecturer. I support companies, training centres, startups and entrepreneurs with the experience of a manager who runs international projects every day.</p>
      <div class="actions">
        <a class="btn" href="{CONTACT}">Get in touch</a>
        <a class="btn btn--ghost" href="{u('training')}">See training courses</a>
      </div>
    </div>
    {hero_portrait("Portrait of Nacim Touenti (photo coming soon)", ["Trainer", "Coach", "University lecturer"], "Paris, Zurich, Tangier")}
  </div>
</section>

<section class="proof" aria-label="At a glance">
  <div class="wrap proof-grid">
    <div class="proof-item"><h4>10+ years of management</h4><p>International projects across Europe and Africa, in fintech and electronic payments.</p></div>
    <div class="proof-item"><h4>University lecturer</h4><p>Courses, programmes, case studies and exams designed and delivered.</p></div>
    <div class="proof-item"><h4>Creator of the Softies method</h4><p>Soft-skills development, rolled out in several countries.</p></div>
  </div>
</section>

<section class="section" id="offers">
  <div class="wrap">
    <div class="section-head">
      <h2>Three ways to work together</h2>
      <p>One standard throughout: visible progress that lasts after I leave.</p>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Training</h3><p class="who">Companies, training centres, schools and universities</p></div>
        <p class="problem">Your teams or learners need a trainer who practises every day what he teaches.</p>
        <div><ul><li>Project management, leadership, soft skills</li><li>Market research and entrepreneurship</li><li>Module and programme design</li></ul><a class="more" href="{u('training')}">See the catalogue</a></div>
      </article>
      <article class="offer-row">
        <div><h3>Coaching</h3><p class="who">Executives, managers, project leads, graduates</p></div>
        <p class="problem">You want to make better decisions, have more impact or succeed at a key career step.</p>
        <div><ul><li>One-to-one coaching, first session free</li><li>Public speaking, influence, leadership</li><li>Team workshops and strategy sessions</li></ul><a class="more" href="{u('coaching')}">Explore coaching</a></div>
      </article>
      <article class="offer-row">
        <div><h3>Startup support</h3><p class="who">Founders, entrepreneurs, project owners</p></div>
        <p class="problem">You have an idea or a first product: you need structure, a roadmap and sales.</p>
        <div><ul><li>3-month Launch programme</li><li>Mentoring for entrepreneurs</li><li>Project turnaround</li></ul><a class="more" href="{u('startups')}">See startup support</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><h2>Why work with me</h2></div>
    <div class="reasons">
      <div class="reason"><h3>A hands-on manager</h3><p>I run international projects across EMEA every day. What I teach and advise, I practise.</p></div>
      <div class="reason"><h3>A teacher</h3><p>I lecture at university and design courses, case studies and exams. People learn by doing, not by listening.</p></div>
      <div class="reason"><h3>Two continents</h3><p>I have worked with teams in Europe and Africa. I know how to adapt a method to each culture and context.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Selected work</h2><p>A few representative projects. Details and references on request.</p></div>
    <div class="cases">
      <article class="case"><span class="tag">Training</span><h3>University programme design</h3><p>Programmes built around real business challenges.</p></article>
      <article class="case"><span class="tag">Coaching</span><h3>The Softies method</h3><p>A soft-skills development method rolled out in several countries.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Entrepreneur Week</h3><p>Workshops run with universities and companies to spark innovation and entrepreneurship.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Mentoring future entrepreneurs</h3><p>Supporting project owners from vision to execution.</p></article>
      <article class="case"><span class="tag">Management</span><h3>International launches</h3><p>Software rollouts across several countries with multicultural teams.</p></article>
      <article class="case"><span class="tag">Management</span><h3>Mobile wallet in Africa</h3><p>Launch of mobile-first financial tools for underbanked communities.</p></article>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div><h2>Frequently asked questions</h2><p class="lead">Another question? <a href="{CONTACT}">Write to me</a>.</p></div>
    <div class="faq">{faq_html(HOME_FAQ)}</div>
  </div>
</section>

{cta_band("Let's talk about your project", "A free 30-minute call to understand your need and see how I can help.", "Get in touch", CONTACT, "Message on WhatsApp", SITE["whatsapp_url"])}
""",
}

COURSES = [
    {
        "id": "soft-skills-softies",
        "name": "Soft skills and leadership: the Softies method",
        "desc": "Build communication, negotiation, emotional intelligence and leadership through role play.",
        "for": "Managers, project teams, students and graduates",
        "goals": [
            "Speak up and persuade with clarity",
            "Negotiate and handle tension in a team",
            "Develop a leadership style that fits your personality",
        ],
        "duration": "1 day or modular programme",
        "format": "On site preferred, role play and serious games",
    },
    {
        "id": "project-management",
        "name": "Project management: agile and hybrid methods",
        "desc": "Run a project end to end, with the right method for your team and context.",
        "for": "Project managers, product owners, managers, students",
        "goals": [
            "Choose and adapt an agile or hybrid method",
            "Control scope and align stakeholders",
            "Produce reporting that helps decision-makers",
            "Turn around a struggling project",
        ],
        "duration": "2 days (14 h)",
        "format": "In-house or open session, on site or remote",
    },
    {
        "id": "market-research",
        "name": "Market research and Test & Learn",
        "desc": "Use market research as a decision-making tool and avoid the classic interpretation traps.",
        "for": "Entrepreneurs, students, marketing and innovation teams",
        "goals": [
            "Ask the right questions before collecting data",
            "Avoid causality traps in analysis",
            "Test fast and cheaply with a Lean approach",
        ],
        "duration": "1 day (7 h), available as a university module",
        "format": "Schools, universities, incubators, companies",
    },
    {
        "id": "entrepreneurship",
        "name": "Entrepreneurship: from idea to first customers",
        "desc": "Structure a business project, test the market and build a first sales plan.",
        "for": "Project owners, student entrepreneurs, incubatees",
        "goals": [
            "Clarify your value proposition and target",
            "Build a realistic roadmap",
            "Prepare your pitch and first customer meetings",
        ],
        "duration": "1 to 2 days, or workshop format",
        "format": "Incubators, schools, entrepreneurship programmes",
    },
    {
        "id": "electronic-payments",
        "name": "Technical course: electronic payments fundamentals",
        "desc": "For companies in the sector: understand the card payment chain, EMV, PCI DSS and SoftPOS.",
        "for": "Product, project, sales and support teams in fintech",
        "goals": [
            "Explain the journey of a card transaction",
            "Understand EMV, contactless and SoftPOS",
            "Place PCI DSS requirements and certifications",
        ],
        "duration": "1 to 2 days",
        "format": "In-house, on site or remote",
    },
]


def course_html(c):
    goals = "".join(f"<li>{g}</li>" for g in c["goals"])
    return f"""<article class="course" id="{c['id']}">
  <div>
    <h3>{c['name']}</h3>
    <p>{c['desc']}</p>
    <h4>Objectives</h4>
    <ul>{goals}</ul>
    <a class="more" href="{mailto('Detailed programme: ' + c['name'])}">Request the detailed programme</a>
  </div>
  <dl>
    <dt>Audience</dt><dd>{c['for']}</dd>
    <dt>Duration</dt><dd>{c['duration']}</dd>
    <dt>Format</dt><dd>{c['format']}</dd>
    <dt>Price</dt><dd>On quotation, depending on format and group size</dd>
  </dl>
</article>"""


TRAINING = {
    "key": "training",
    "slug": SLUGS["training"],
    "title": "Soft skills, leadership, project management and entrepreneurship training | Nacim Touenti",
    "description": "Training in soft skills and leadership (Softies method), project management, market research and entrepreneurship. In-house, schools and training centres, by Nacim Touenti.",
    "schema": [course_schema(c["name"], c["desc"], "en", f"{BASE}/en/{SLUGS['training']}#{c['id']}") for c in COURSES],
    "body": page_hero(
        '<a href="/en/">Home</a> / Training',
        "Training",
        "Courses built by a practitioner who teaches: learn by doing, on real cases, and leave with tools you can use the next day.",
        "formation.webp",
        "Interactive small-group training session",
        f'<div class="actions"><a class="btn" href="#catalogue">See the catalogue</a><a class="btn btn--ghost" href="{CONTACT}">Request a tailored course</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>How I teach</h2>
      <p class="measure">No lectures, no endless slides. Participants negotiate, present, decide and sometimes fail, on purpose: that's how people grow.</p>
    </div>
    <ul class="ticks">
      <li><b>Learn by doing</b>: role play, case studies, simulations</li>
      <li><b>Serious games</b>: games that teach and engage</li>
      <li><b>Step back</b>: a debrief after every exercise to anchor learning</li>
      <li><b>Interactive tools</b>: polls, quizzes, Miro and Trello boards</li>
    </ul>
  </div>
</section>

<section class="section section--mist" id="catalogue">
  <div class="wrap">
    <div class="section-head"><h2>Catalogue</h2><p>Every course can be adapted: length, level, examples from your industry.</p></div>
    {"".join(course_html(c) for c in COURSES)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>How I build a course</h2></div>
    <ol class="steps">
      <li><h3>Design</h3><p>Immersive, realistic modules built with you around your goals.</p></li>
      <li><h3>Pilot</h3><p>A trial run with real participants to refine the exercises.</p></li>
      <li><h3>Validation</h3><p>Expert review and adjustments based on feedback.</p></li>
      <li><h3>Delivery</h3><p>On-site or remote sessions, with learning assessment.</p></li>
    </ol>
  </div>
</section>

{cta_band("Training for your team?", "Tell me who you want to train, on what and by when: I'll send you a programme proposal.", "Request training", CONTACT, "For training centres", u("centres"))}
""",
}

COACHING = {
    "key": "coaching",
    "slug": SLUGS["coaching"],
    "title": "Coaching for executives, managers and graduates | Nacim Touenti",
    "description": "One-to-one and team coaching: leadership, public speaking, decision-making, career transitions. First session free. By Nacim Touenti, Paris, Zurich and remote.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Coaching',
        "Coaching",
        "A demanding, supportive outside view to clarify where you're going, decide faster and have more impact. The first session is free.",
        "coaching.webp",
        "Two professionals walking together in the city",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Book the free session</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Who it's for</h2></div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Executives and founders</h3><p class="who">One-to-one coaching</p></div>
        <p class="problem">You carry decisions alone and want a thinking partner who knows the reality on the ground.</p>
        <div><ul><li>Vision and roadmap</li><li>Hard decisions and priorities</li><li>Leadership in growth and in crisis</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Managers and project leads</h3><p class="who">One-to-one coaching</p></div>
        <p class="problem">You're taking on a new role, a bigger team or a project under pressure.</p>
        <div><ul><li>Communication and influence</li><li>Stakeholder management</li><li>Emotional intelligence and presence</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Students and graduates</h3><p class="who">Career coaching</p></div>
        <p class="problem">You're preparing to enter working life or launch a first business.</p>
        <div><ul><li>Career plan and mindset</li><li>Job search and interviews</li><li>Starting a business</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Teams</h3><p class="who">In-company workshops, on site or remote</p></div>
        <p class="problem">You want to align a leadership team or re-energise a project team.</p>
        <div><ul><li>Speak-Up strategy sessions</li><li>Building a high-performance culture</li><li>Soft-skills workshops (Softies method)</li></ul></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><h2>How coaching works</h2></div>
    <ol class="steps">
      <li><h3>Free session</h3><p>We review your situation and what you want to change.</p></li>
      <li><h3>Goals</h3><p>Two or three concrete goals and a session rhythm that suits you.</p></li>
      <li><h3>Sessions</h3><p>Discussion, role play and actions to try between sessions.</p></li>
      <li><h3>Review</h3><p>What changed, what's left and how to keep going on your own.</p></li>
    </ol>
  </div>
</section>

{cta_band("Ready for the next step?", "Book your free session to clarify your situation and your next steps.", "Book the free session", CONTACT, "Message on WhatsApp", SITE["whatsapp_url"])}
""",
}

STARTUPS = {
    "key": "startups",
    "slug": SLUGS["startups"],
    "title": "Support for startups and entrepreneurs: project, product, sales | Nacim Touenti",
    "description": "A 3-month Launch programme, mentoring for entrepreneurs, workshops for incubators and project turnaround. Startup support by Nacim Touenti.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Startups',
        "Support for startups and entrepreneurs",
        "Going from idea to execution takes structure, clear priorities and someone who has led launches before. I help you structure your project, product and sales.",
        "startups.webp",
        "Startup team working on a roadmap",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Book a discovery call</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Four formats</h2></div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Launch programme</h3><p class="who">3 months, one session a week</p></div>
        <p class="problem">For early-stage startups that need to frame everything at once.</p>
        <div><ul><li>Project scoping and roadmap</li><li>Product: priorities, tests, first releases</li><li>Go-to-market: target, offer, pitch, sales plan</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Mentoring for entrepreneurs</h3><p class="who">Regular meetings over time</p></div>
        <p class="problem">To stay on course, step back and not face decisions alone.</p>
        <div><ul><li>Monthly or fortnightly check-ins</li><li>Review of your pitch and key documents</li><li>Introductions where useful</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Workshops for incubators and schools</h3><p class="who">Half a day to a week</p></div>
        <p class="problem">To move several projects forward at once, on the Entrepreneur Week model.</p>
        <div><ul><li>Idea, market and pitch workshops</li><li>Juries and individual feedback</li><li>Programmes co-designed with your organisation</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Project turnaround</h3><p class="who">Short engagement</p></div>
        <p class="problem">For a project that is slipping: deadlines, scope, team or client relationship.</p>
        <div><ul><li>Rapid diagnosis and recovery plan</li><li>Reset scope and stakeholders</li><li>Set up the right tools (Jira, Notion, ClickUp…)</li></ul></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap two-col">
    <div>
      <h2>What I favour</h2>
      <ul class="ticks"><li>Strategic leadership, not just task execution</li><li>Agile or hybrid methods tailored to your team</li><li>Measurable outcomes, not just deliverables</li><li>Quick market tests before big investments</li></ul>
    </div>
    <div>
      <h2>What I avoid</h2>
      <ul class="ticks cross"><li>Generic frameworks applied without adaptation</li><li>Business plans nobody reads</li><li>Unclear roles and scattered communication</li><li>Building a product before talking to customers</li></ul>
    </div>
  </div>
</section>

{cta_band("Your project deserves solid foundations", "A 30-minute discovery call to review where you are and find the right format.", "Book a discovery call", CONTACT, "Message on WhatsApp", SITE["whatsapp_url"])}
""",
}

CENTRES = {
    "key": "centres",
    "slug": SLUGS["centres"],
    "title": "Trainer and guest lecturer for training centres, schools and universities | Nacim Touenti",
    "description": "Guest lecturer and programme designer for training centres, schools and universities: project management, leadership, soft skills, market research, entrepreneurship.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Training centres',
        "For training centres, schools and universities",
        "You need someone who can design a complete module and deliver it to a high standard. I bring the combined perspective of a lecturer and a working manager.",
        "centres.webp",
        "Trainer running a participatory workshop",
        f'<div class="actions"><a class="btn" href="{mailto("Teaching proposal")}">Propose a session</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>What I bring</h2>
      <ul class="ticks">
        <li><b>Teaching</b>: short modules, masterclasses, industry talks</li>
        <li><b>Turnkey design</b>: syllabus, materials, case studies, assessments</li>
        <li><b>Exams and case studies</b> aligned with course concepts</li>
        <li><b>Juries and mentoring</b> of student or entrepreneurial projects</li>
      </ul>
    </div>
    <div>
      <h2>Subjects taught</h2>
      <ul class="chips"><li>Project management</li><li>Agile methods</li><li>Leadership</li><li>Soft skills</li><li>Communication</li><li>Market research</li><li>Lean and Test &amp; Learn</li><li>Entrepreneurship</li><li>Fintech and payments</li></ul>
      <p class="measure" style="margin-top:24px">Example: a market research exam built around a fictional startup, assessing causality traps, Test &amp; Learn logic and the role of research in decision-making.</p>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><h2>How we work together</h2></div>
    <ol class="steps">
      <li><h3>Need</h3><p>Audience, learning outcomes, hours and curriculum constraints.</p></li>
      <li><h3>Proposal</h3><p>Detailed programme, assessment methods and quotation.</p></li>
      <li><h3>Production</h3><p>Materials, case studies and assessments delivered in your formats.</p></li>
      <li><h3>Delivery and review</h3><p>Sessions, assessment and lessons learned for the next intake.</p></li>
    </ol>
  </div>
</section>

{cta_band("A module to design or deliver?", "Send me the topic, audience and schedule: I'll come back with a proposal.", "Propose a session", mailto("Teaching proposal"), "See the catalogue", u("training"))}
""",
}

ABOUT = {
    "key": "about",
    "slug": SLUGS["about"],
    "page_type": "ProfilePage",
    "title": "Nacim Touenti — Trainer, coach, lecturer and founder of Twty Consulting",
    "description": "Who is Nacim Touenti? Trainer, coach and university lecturer, founder of Twty Consulting, with 10+ years of international project management.",
    "body": f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/en/">Home</a> / About</p>
    <div class="about-grid">
      <div class="portrait" role="img" aria-label="Portrait of Nacim Touenti (photo coming soon)">NT</div>
      <div>
        <h1>Nacim Touenti</h1>
        <p class="lead">Trainer, coach and university lecturer, founder of Twty Consulting.</p>
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
    <div class="section-head"><h2>Three roles, one thread</h2><p>Helping people grow and their projects succeed.</p></div>
    <div class="reasons">
      <div class="reason"><h3>Trainer and lecturer</h3><p>University teaching, programme, exam and case-study design, corporate training.</p></div>
      <div class="reason"><h3>Coach and mentor</h3><p>Creator of the Softies method, coach to executives and managers, mentor to future entrepreneurs.</p></div>
      <div class="reason"><h3>Hands-on manager</h3><p>Leading international projects across EMEA, launches in several countries, multicultural teams in Europe and Africa.</p></div>
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
    <h1>Let's talk about your project</h1>
    <p class="lead">Describe your need in a few lines. I'll reply with a proposal for a 30-minute call.</p>
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
