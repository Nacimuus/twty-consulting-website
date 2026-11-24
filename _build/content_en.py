"""English content of twty.fr (mirror of the French version)."""
from parts import pay_card, page_hero, cta_band, mailto, faq_schema, faq_html, course_schema
from site_config import SITE

BASE = SITE["base_url"]

SLUGS = {
    "home": "index.html",
    "payment": "payment-expertise.html",
    "training": "training.html",
    "centres": "training-centres.html",
    "startups": "startup-coaching.html",
    "about": "nacim-touenti.html",
    "contact": "contact.html",
    "legal": "legal.html",
}


def u(key):
    return "/en/" + ("" if SLUGS[key] == "index.html" else SLUGS[key])


UI = {
    "og_locale": "en_GB",
    "og_alt": "Nacim Touenti, Twty Consulting: payments expertise, training and startup coaching",
    "skip": "Skip to content",
    "menu": "Menu",
    "nav_label": "Main navigation",
    "nav": [
        ("payment", "Payments expertise"),
        ("training", "Training"),
        ("centres", "Training centres"),
        ("startups", "Startups"),
        ("about", "About"),
    ],
    "lang_switch": "FR",
    "lang_title": "Version française",
    "cta_contact": "Get in touch",
    "footer_blurb": "Twty Consulting, Nacim Touenti's practice: electronic payments expertise, training and startup coaching.",
    "footer_nav": "Site",
    "footer_contact": "Contact",
    "footer_presence": "Locations",
    "tangier": "Tangier",
    "legal": "Legal notice",
}

BIO_SHORT = (
    "Nacim Touenti is a payments and project management expert, lecturer and trainer, and the founder "
    "of Twty Consulting. He helps companies, training centres and startups deliver payment projects "
    "and grow their teams' skills."
)

BIO_LONG = (
    "Nacim Touenti is an electronic payments and project management expert, university lecturer and trainer, "
    "and the founder of Twty Consulting. He leads project management across EMEA at a global payment "
    "solutions provider, where he drives the launch of payment terminals and software, their EMV "
    "certifications (L1, L2, L3), PCI DSS compliance and relationships with international card schemes. "
    "With more than ten years of experience in fintech, consulting and international rollouts across "
    "Europe and Africa, he also lectures at university and designs training programmes. Through Twty "
    "Consulting, based in Paris, Zurich and Tangier, he supports companies, training centres and startups "
    "with payments expertise, training and project, product and sales coaching."
)

ORG_DESCRIPTION = (
    "Consulting and training practice founded by Nacim Touenti: electronic payments expertise "
    "(EMV, PCI DSS, SoftPOS), training for companies and training centres, and startup coaching."
)

CONTACT = u("contact")

HOME_FAQ = [
    ("Do you work on site or remotely?",
     "Both. I work on site in Paris, Switzerland and Morocco, and remotely everywhere else."),
    ("Which languages do you work in?",
     "French and English, for both training and consulting."),
    ("Can you tailor a course to our context?",
     "Yes. Every in-house course is built around your projects, products and constraints, with case studies from your industry."),
    ("How soon can we start?",
     "A first 30-minute call can usually happen within the week. It scopes your need so I can send you a proposal."),
]

HOME = {
    "key": "home",
    "slug": SLUGS["home"],
    "title": "Nacim Touenti — Payments expert, trainer and consultant | Twty Consulting",
    "description": "Nacim Touenti, electronic payments expert (EMV, PCI DSS, SoftPOS), lecturer and trainer. Consulting, training and startup coaching with Twty Consulting.",
    "schema": [faq_schema(HOME_FAQ, "en")],
    "body": f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Deliver your payment projects. Grow your teams.</h1>
      <p class="lead">I'm Nacim Touenti, a payments and project management expert, lecturer and trainer. I help companies, training centres and startups, from EMV certification to building their teams' skills.</p>
      <div class="actions">
        <a class="btn" href="{CONTACT}">Get in touch</a>
        <a class="btn btn--ghost" href="{u('training')}">See training courses</a>
      </div>
    </div>
    {pay_card("Expertise", "Payments, training, startups", "Locations", "Paris  Zurich  Tangier")}
  </div>
</section>

<section class="proof" aria-label="At a glance">
  <div class="wrap proof-grid">
    <div class="proof-item"><h4>10+ years of experience</h4><p>Fintech, consulting and international rollouts across Europe and Africa.</p></div>
    <div class="proof-item"><h4>EMV, PCI DSS, SoftPOS, TMS</h4><p>L1 to L3 certifications and Visa, Mastercard, Amex, UPI schemes.</p></div>
    <div class="proof-item"><h4>Lecturer and trainer</h4><p>University teaching, programme design and tailored training.</p></div>
  </div>
</section>

<section class="section" id="offers">
  <div class="wrap">
    <div class="section-head">
      <h2>Three ways to work together</h2>
      <p>One standard throughout: concrete results, handed over to your teams so they last.</p>
    </div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Payments</h3><p class="who">Banks, acquirers, PSPs, fintechs, terminal vendors</p></div>
        <p class="problem">Your terminal, app or payment gateway has to launch on time, secure and certified.</p>
        <div><ul><li>Payment project assessment</li><li>EMV and scheme certification support</li><li>Interim project leadership</li></ul><a class="more" href="{u('payment')}">Explore payments expertise</a></div>
      </article>
      <article class="offer-row">
        <div><h3>Training</h3><p class="who">Companies, training centres, schools and universities</p></div>
        <p class="problem">Your teams or learners need a trainer who practises every day what he teaches.</p>
        <div><ul><li>In-house training courses</li><li>Module and programme design</li><li>Masterclasses and guest lectures</li></ul><a class="more" href="{u('training')}">See the catalogue</a></div>
      </article>
      <article class="offer-row">
        <div><h3>Startup coaching</h3><p class="who">Founders, entrepreneurs, project leads</p></div>
        <p class="problem">You have an idea or a first product: you need structure, a roadmap and sales.</p>
        <div><ul><li>3-month Launch programme</li><li>Founder and project lead coaching</li><li>Project turnaround</li></ul><a class="more" href="{u('startups')}">See startup coaching</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head"><h2>Why work with me</h2></div>
    <div class="reasons">
      <div class="reason"><h3>Hands-on</h3><p>I run payment projects across EMEA every day: terminals, software, certifications. My advice comes from projects that shipped.</p></div>
      <div class="reason"><h3>Teaching</h3><p>I lecture at university and design courses, case studies and exams. I make technical topics clear and actionable.</p></div>
      <div class="reason"><h3>Europe and Africa</h3><p>I have delivered projects on both continents, including a mobile wallet rollout. I know the constraints of mature and emerging markets.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Selected work</h2><p>A few representative projects. Details and references on request.</p></div>
    <div class="cases">
      <article class="case"><span class="tag">Payments</span><h3>Payment terminal software launch</h3><p>International deployments with local compliance and full L3 certification support.</p></article>
      <article class="case"><span class="tag">Payments</span><h3>PCI, EMV and scheme certifications</h3><p>Expertise in payment security, PCI DSS and international scheme certifications.</p></article>
      <article class="case"><span class="tag">Payments</span><h3>Mobile wallet in Africa</h3><p>Launch of mobile-first financial tools for underbanked communities.</p></article>
      <article class="case"><span class="tag">Training</span><h3>University programme design</h3><p>Programmes built around real business challenges.</p></article>
      <article class="case"><span class="tag">Startups</span><h3>Entrepreneur Week</h3><p>Workshops run with universities and companies to spark innovation and entrepreneurship.</p></article>
      <article class="case"><span class="tag">Training</span><h3>The Softies method</h3><p>A soft-skills development method rolled out in several countries.</p></article>
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

PAYMENT = {
    "key": "payment",
    "slug": SLUGS["payment"],
    "title": "Payments consultant: EMV, PCI DSS, SoftPOS expert | Nacim Touenti",
    "description": "Payment project assessments, EMV L1 to L3 and scheme certifications (Visa, Mastercard, Amex, UPI), PCI DSS, SoftPOS and TMS. Consulting and project leadership by Nacim Touenti.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Payments expertise',
        "Payments expertise",
        "I help you launch payment terminals, apps and services that pass certification first time and meet security requirements.",
        "expertise-paiement.webp",
        "Project team around a payment terminal and an EMV transaction flow screen",
        f'<div class="actions"><a class="btn" href="{mailto("Payment project assessment request")}">Request an assessment</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>Who it's for</h2>
      <p class="measure">You have a payment project under way or an ambitious goal, and you want smooth integration and global compliance.</p>
      <ul class="chips"><li>Banks</li><li>Acquirers</li><li>PSPs and gateways</li><li>Fintechs</li><li>Terminal vendors</li><li>Software vendors</li></ul>
    </div>
    <div>
      <h2>Areas of expertise</h2>
      <ul class="ticks">
        <li>EMV implementation and certification (L1, L2, L3)</li>
        <li>Visa, Mastercard, Amex, UPI and local scheme certifications</li>
        <li>SoftPOS, contactless and QR-based payments</li>
        <li>Terminal management system (TMS) setup</li>
        <li>Payment APIs, software and gateway integration</li>
        <li>Security audits, key management, PCI DSS compliance</li>
        <li>SaaS and custom architectures</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="section-head"><h2>Three engagement formats</h2></div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Payment project assessment</h3><p class="who">2 to 5 days</p></div>
        <p class="problem">An expert review of your project before a certification delay gets expensive.</p>
        <div><ul><li>Gap report: certification, security, schedule</li><li>Prioritised roadmap</li><li>Debrief with your leadership</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Project leadership</h3><p class="who">A few weeks to a few months</p></div>
        <p class="problem">A senior project lead who takes charge of the launch, suppliers and certification labs.</p>
        <div><ul><li>Governance and executive reporting</li><li>Coordination of teams and partners</li><li>Certification follow-up through to approval</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>Team training</h3><p class="who">1 to 2 days, in-house</p></div>
        <p class="problem">Product, project and support teams who finally understand the payment chain end to end.</p>
        <div><ul><li>Payments fundamentals</li><li>Preparing for EMV and scheme certification</li></ul><a class="more" href="{u('training')}">See training courses</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>How an assessment works</h2></div>
    <ol class="steps">
      <li><h3>Scoping</h3><p>A 30-minute call to understand the project, deadlines and stakes.</p></li>
      <li><h3>Review</h3><p>Documentation review and interviews with your teams and partners.</p></li>
      <li><h3>Gaps</h3><p>Risks identified across certification, security, schedule and organisation.</p></li>
      <li><h3>Debrief</h3><p>Report and prioritised roadmap, presented to your decision-makers.</p></li>
    </ol>
  </div>
</section>

{cta_band("A payment project to secure?", "Tell me about your project and deadlines: I'll come back with an assessment proposal.", "Request an assessment", mailto("Payment project assessment request"), "Get in touch", CONTACT)}
""",
}

COURSES = [
    {
        "id": "payments-fundamentals",
        "name": "Payments fundamentals: EMV, PCI DSS, SoftPOS",
        "desc": "Understand the card payment chain end to end, from the EMV chip to acquiring, and PCI DSS security requirements.",
        "for": "Product, project, sales and support teams in payments and fintech companies",
        "goals": [
            "Explain the journey of a card transaction from terminal to issuer",
            "Understand EMV, contactless, SoftPOS and tokenisation",
            "Place PCI DSS requirements and their impact on a project",
            "Work effectively with experts, labs and schemes",
        ],
        "duration": "2 days (14 h)",
        "format": "In-house, on site or remote",
    },
    {
        "id": "emv-certification",
        "name": "Preparing for EMV and scheme certification",
        "desc": "Plan and pass EMV L1, L2, L3 certifications and Visa, Mastercard, Amex and UPI certifications.",
        "for": "Project leads, engineers and quality managers at vendors, PSPs and software publishers",
        "goals": [
            "Know the steps and stakeholders of each certification level",
            "Build a realistic schedule and anticipate blockers",
            "Prepare documentation and test campaigns",
        ],
        "duration": "1 day (7 h)",
        "format": "In-house, on site or remote",
    },
    {
        "id": "project-management",
        "name": "Hybrid project management for tech teams",
        "desc": "Combine agility with compliance milestones to deliver technical projects on time.",
        "for": "Project managers, product owners, tech team leads",
        "goals": [
            "Choose and adapt an agile or hybrid method to your context",
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
    "title": "Payments, EMV, PCI DSS and project management training | Nacim Touenti",
    "description": "Training in payments (EMV, PCI DSS, SoftPOS), certification, project management, market research and soft skills. In-house, on site or remote, by Nacim Touenti.",
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

CENTRES = {
    "key": "centres",
    "slug": SLUGS["centres"],
    "title": "Expert trainer for training centres and schools | Nacim Touenti",
    "description": "Guest lecturer and programme designer for training centres, schools and universities: payments and fintech, project management, market research, entrepreneurship, soft skills.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Training centres',
        "For training centres, schools and universities",
        "You need an expert who can design a complete module and deliver it to a high standard. I bring the combined perspective of a payments practitioner and a lecturer.",
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
      <ul class="chips"><li>Electronic payments</li><li>Fintech</li><li>Project management</li><li>Agile methods</li><li>Market research</li><li>Lean and Test &amp; Learn</li><li>Entrepreneurship</li><li>Leadership</li><li>Soft skills</li></ul>
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

STARTUPS = {
    "key": "startups",
    "slug": SLUGS["startups"],
    "title": "Startup coaching: project, product, sales | Nacim Touenti",
    "description": "A 3-month Launch programme, founder and project lead coaching, project turnaround. Startup and entrepreneur coaching by Nacim Touenti.",
    "body": page_hero(
        '<a href="/en/">Home</a> / Startups',
        "Coaching for startups and entrepreneurs",
        "Going from idea to execution takes structure, clear priorities and someone who has shipped before. I help you structure your project, product and sales.",
        "startups.webp",
        "Startup team working on a roadmap",
        f'<div class="actions"><a class="btn" href="{CONTACT}">Book a discovery call</a></div>',
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Three formats</h2></div>
    <div class="offer-rows">
      <article class="offer-row">
        <div><h3>Launch programme</h3><p class="who">3 months, one session a week</p></div>
        <p class="problem">For early-stage startups that need to frame everything at once.</p>
        <div><ul><li>Project scoping and roadmap</li><li>Product: priorities, tests, first releases</li><li>Go-to-market: target, offer, pitch, sales plan</li></ul></div>
      </article>
      <article class="offer-row">
        <div><h3>One-to-one coaching</h3><p class="who">Session pack, first session free</p></div>
        <p class="problem">For a founder or project lead who wants to make better decisions, faster.</p>
        <div><ul><li>Clarify vision and next step</li><li>Communication and influence</li><li>Leadership in growth and in crisis</li></ul></div>
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
      <ul class="ticks"><li>Strategic leadership, not just task execution</li><li>Agile or hybrid methods tailored to your team</li><li>Measurable outcomes, not just deliverables</li><li>Reporting that actually helps decisions</li></ul>
    </div>
    <div>
      <h2>What I avoid</h2>
      <ul class="ticks cross"><li>Generic frameworks applied without adaptation</li><li>Documentation nobody uses</li><li>Unclear roles and scattered communication</li><li>One-size-fits-all reporting</li></ul>
    </div>
  </div>
</section>

{cta_band("Your project deserves solid foundations", "A 30-minute discovery call to review where you are and find the right format.", "Book a discovery call", CONTACT, "Message on WhatsApp", SITE["whatsapp_url"])}
""",
}

ABOUT = {
    "key": "about",
    "slug": SLUGS["about"],
    "page_type": "ProfilePage",
    "title": "Nacim Touenti — Payments expert, lecturer and founder of Twty Consulting",
    "description": "Who is Nacim Touenti? Payments and project management expert, university lecturer, trainer and founder of Twty Consulting (Paris, Zurich, Tangier).",
    "body": f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/en/">Home</a> / About</p>
    <div class="about-grid">
      <div class="portrait" role="img" aria-label="Portrait of Nacim Touenti (photo coming soon)">NT</div>
      <div>
        <h1>Nacim Touenti</h1>
        <p class="lead">Electronic payments and project management expert, lecturer and trainer, founder of Twty Consulting.</p>
        <p class="measure">{BIO_LONG}</p>
        <dl class="facts">
          <dt>Specialities</dt><dd>Payments, EMV, PCI DSS, SoftPOS, TMS, project management</dd>
          <dt>Teaching</dt><dd>University and professional training</dd>
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
    <div class="section-head"><h2>Three roles, one thread</h2><p>Making projects succeed and helping the people behind them grow.</p></div>
    <div class="reasons">
      <div class="reason"><h3>Payments practitioner</h3><p>Terminal and software launches, EMV and scheme certifications, PCI DSS compliance, rollouts in Europe and Africa.</p></div>
      <div class="reason"><h3>Lecturer and trainer</h3><p>University teaching, programme, exam and case-study design, corporate training.</p></div>
      <div class="reason"><h3>Entrepreneur</h3><p>Founder of Twty Consulting, mentor to entrepreneurs, creator of the Softies method and organiser of Entrepreneur Week.</p></div>
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
    "description": "Contact Nacim Touenti about a payment project, training or startup coaching. Email, WhatsApp, LinkedIn. Paris, Zurich, Tangier.",
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
            <option>Payment project</option>
            <option>Training for my team</option>
            <option>Teaching at a training centre or school</option>
            <option>Startup coaching</option>
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

PAGES = [HOME, PAYMENT, TRAINING, CENTRES, STARTUPS, ABOUT, CONTACT_PAGE, LEGAL]
