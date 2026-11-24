// Twty Consulting — interactions du site (menu mobile, formulaire de contact)
(function () {
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

  // Le site est statique : le formulaire prépare un email dans la messagerie du visiteur.
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
      window.location.href = "mailto:" + form.dataset.email +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);
    });
  }
})();
