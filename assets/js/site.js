// Twty Consulting — interactions du site
// Fond « réseau » animé, halo qui suit la souris, étincelles sur les boutons,
// apparitions au défilement, en-tête flottant, menu mobile, formulaire de contact.
(function () {
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var body = document.body;

  /* ---------- Fond animé : constellation de points reliés (or et bleu) ---------- */
  var canvas = document.createElement("canvas");
  canvas.id = "bg-network";
  canvas.setAttribute("aria-hidden", "true");
  body.prepend(canvas);
  var ctx = canvas.getContext("2d");
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0, points = [], mouse = { x: -9999, y: -9999 };
  var LINK = 150;

  function resize() {
    W = window.innerWidth; H = window.innerHeight;
    canvas.width = W * dpr; canvas.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var count = Math.min(90, Math.round((W * H) / 17000));
    points = [];
    for (var i = 0; i < count; i++) {
      points.push({
        x: Math.random() * W, y: Math.random() * H,
        vx: (Math.random() - 0.5) * 0.25, vy: (Math.random() - 0.5) * 0.25,
        r: Math.random() * 1.6 + 0.6,
        gold: Math.random() < 0.35
      });
    }
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    for (var i = 0; i < points.length; i++) {
      var p = points[i];
      if (!reduceMotion) {
        p.x += p.vx; p.y += p.vy;
        if (p.x < -20) p.x = W + 20; if (p.x > W + 20) p.x = -20;
        if (p.y < -20) p.y = H + 20; if (p.y > H + 20) p.y = -20;
      }
      for (var j = i + 1; j < points.length; j++) {
        var q = points[j], dx = p.x - q.x, dy = p.y - q.y, d = Math.sqrt(dx * dx + dy * dy);
        if (d < LINK) {
          ctx.strokeStyle = "rgba(120, 200, 212," + (0.13 * (1 - d / LINK)) + ")";
          ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke();
        }
      }
      var mdx = p.x - mouse.x, mdy = p.y - mouse.y, md = Math.sqrt(mdx * mdx + mdy * mdy);
      if (md < 200) {
        ctx.strokeStyle = "rgba(216, 180, 90," + (0.35 * (1 - md / 200)) + ")";
        ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke();
      }
      ctx.fillStyle = p.gold ? "rgba(243, 220, 148, .85)" : "rgba(160, 225, 233, .6)";
      ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
    }
  }

  var running = true;
  function loop() {
    if (running) draw();
    if (!reduceMotion) requestAnimationFrame(loop);
  }
  resize();
  loop();
  window.addEventListener("resize", function () { resize(); if (reduceMotion) draw(); });
  document.addEventListener("visibilitychange", function () { running = !document.hidden; });

  /* ---------- Halo lumineux qui suit la souris ---------- */
  var raf = null;
  window.addEventListener("pointermove", function (e) {
    mouse.x = e.clientX; mouse.y = e.clientY;
    if (raf) return;
    raf = requestAnimationFrame(function () {
      body.style.setProperty("--mx", (mouse.x / W * 100).toFixed(1) + "%");
      body.style.setProperty("--my", (mouse.y / H * 100).toFixed(1) + "%");
      raf = null;
    });
  }, { passive: true });
  document.addEventListener("pointerleave", function () { mouse.x = mouse.y = -9999; });

  // Halo local sur les panneaux d'offre
  document.querySelectorAll(".offer-row").forEach(function (el) {
    el.addEventListener("pointermove", function (e) {
      var r = el.getBoundingClientRect();
      el.style.setProperty("--px", (e.clientX - r.left) + "px");
      el.style.setProperty("--py", (e.clientY - r.top) + "px");
    });
  });

  /* ---------- Étincelles dorées au clic sur les boutons ---------- */
  function sparkle(x, y) {
    if (reduceMotion || !document.body.animate) return;
    var ring = document.createElement("span");
    ring.className = "spark-ring"; ring.style.left = x + "px"; ring.style.top = y + "px";
    document.body.appendChild(ring);
    ring.animate([{ transform: "scale(.4)", opacity: 1 }, { transform: "scale(6)", opacity: 0 }], { duration: 600, easing: "ease-out" }).onfinish = function () { ring.remove(); };
    var n = 22;
    for (var i = 0; i < n; i++) {
      var s = document.createElement("span");
      s.className = i % 3 === 0 ? "spark spark--dot" : "spark";
      s.style.left = x + "px"; s.style.top = y + "px";
      document.body.appendChild(s);
      var angle = (Math.PI * 2 * i) / n + Math.random() * 0.5;
      var dist = 60 + Math.random() * 70;
      var scale = 0.7 + Math.random() * 0.8;
      var anim = s.animate([
        { transform: "translate(0,0) scale(0) rotate(0deg)", opacity: 1 },
        { transform: "translate(" + Math.cos(angle) * dist * 0.6 + "px," + Math.sin(angle) * dist * 0.6 + "px) scale(" + scale + ") rotate(90deg)", opacity: 1, offset: 0.5 },
        { transform: "translate(" + Math.cos(angle) * dist + "px," + (Math.sin(angle) * dist + 18) + "px) scale(0) rotate(180deg)", opacity: 0 }
      ], { duration: 800 + Math.random() * 400, easing: "cubic-bezier(.2,.7,.3,1)" });
      anim.onfinish = (function (el) { return function () { el.remove(); }; })(s);
    }
  }
  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".btn");
    if (!btn) return;
    var x = e.clientX, y = e.clientY;
    if (!x && !y) { // clic clavier : centre du bouton
      var r = btn.getBoundingClientRect(); x = r.left + r.width / 2; y = r.top + r.height / 2;
    }
    sparkle(x, y);
    // Laisser le temps de voir les étincelles avant de quitter la page
    var href = btn.getAttribute("href");
    if (href && !reduceMotion && btn.tagName === "A" && !btn.target && !btn.hasAttribute("download") && !e.metaKey && !e.ctrlKey && href.charAt(0) !== "#" && href.indexOf("mailto:") !== 0) {
      e.preventDefault();
      setTimeout(function () { window.location.href = href; }, 320);
    }
  });

  /* ---------- En-tête : plus compact après défilement ---------- */
  var header = document.querySelector(".site-header");
  function onScroll() { if (header) header.classList.toggle("is-scrolled", window.scrollY > 24); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Apparitions au défilement ---------- */
  if (!reduceMotion && "IntersectionObserver" in window) {
    var targets = document.querySelectorAll(".section-head, .offer-row, .reason, .case, .course, .steps li, .proof-item, .faq details, .ticks li, .chips, .cta-band h2, .two-col > div");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    targets.forEach(function (el) {
      var sib = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.style.setProperty("--d", Math.min(sib, 5) * 0.07 + "s");
      el.classList.add("reveal");
      io.observe(el);
    });
  }

  /* ---------- Menu mobile ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("menu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---------- Formulaire : prépare un email dans la messagerie du visiteur ---------- */
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var lines = [];
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.name === "message") return;
        var label = el.closest("label");
        var name = label ? label.childNodes[0].textContent.trim() : el.name;
        if (el.value) lines.push(name + " : " + el.value);
      });
      var body = form.elements.message.value + "\n\n---\n" + lines.join("\n");
      var need = form.elements.besoin || form.elements.need;
      var subject = form.dataset.subject + (need ? " — " + need.value : "");
      setTimeout(function () {
        window.location.href = "mailto:" + form.dataset.email +
          "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
      }, reduceMotion ? 0 : 300);
    });
  }
})();
