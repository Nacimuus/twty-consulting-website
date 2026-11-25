// Carte de visite NFC — changement de langue et partage
(function () {
  var root = document.documentElement;

  document.querySelectorAll("[data-set-lang]").forEach(function (b) {
    b.addEventListener("click", function () {
      var l = b.getAttribute("data-set-lang");
      root.setAttribute("data-lang", l);
      root.lang = l;
      try { localStorage.setItem("twty-lang", l); } catch (e) {}
    });
  });

  var share = document.querySelector("[data-share]");
  var status = document.querySelector(".nfc-copied");
  var url = "https://www.twty.fr/Nacim.html";
  function say(fr, en) { if (status) status.textContent = root.getAttribute("data-lang") === "en" ? en : fr; }

  if (share) {
    share.addEventListener("click", function () {
      var en = root.getAttribute("data-lang") === "en";
      var data = {
        title: "Nacim Touenti — Twty Consulting",
        text: en ? "Nacim Touenti: trainer, coach and university lecturer." : "Nacim Touenti : formateur, coach et enseignant à l'université.",
        url: url
      };
      if (navigator.share) {
        navigator.share(data).catch(function () {});
      } else if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(function () {
          say("Lien copié : " + url, "Link copied: " + url);
        }, function () { say(url, url); });
      } else {
        say(url, url);
      }
    });
  }
})();
