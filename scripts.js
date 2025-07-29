// Include HTML (header/footer)
function includeHTML() {
  return new Promise((resolve, reject) => {
    const elements = document.querySelectorAll("[w3-include-html]");
    let total = elements.length;
    let loaded = 0;

    if (total === 0) resolve(); // nothing to load

    elements.forEach(el => {
      const file = el.getAttribute("w3-include-html");
      if (file) {
        fetch(file)
          .then(response => {
            if (!response.ok) throw new Error("Failed to load " + file);
            return response.text();
          })
          .then(data => {
            el.innerHTML = data;
            el.removeAttribute("w3-include-html");
            loaded++;
            if (loaded === total) resolve();
          })
          .catch(err => {
            el.innerHTML = "Page not found.";
            console.error(err);
            reject(err);
          });
      }
    });
  });
}

// Mobile menu toggle
function setupMobileMenu() {
  const hamburger = document.querySelector(".hamburger");
  const closeMenu = document.querySelector(".close-menu");
  const navbar = document.getElementById("navbar");

  if (hamburger && navbar) {
    hamburger.addEventListener("click", () => {
      navbar.classList.toggle("active");
      closeMenu?.classList.toggle("active", navbar.classList.contains("active"));
    });
  }

  if (closeMenu && navbar) {
    closeMenu.addEventListener("click", () => {
      navbar.classList.remove("active");
      closeMenu.classList.remove("active");
    });
  }
}

// Header shrink on scroll
function setupShrinkHeader() {
  const header = document.querySelector("header");
  const logo = document.querySelector(".logo");

  if (!header) return;

  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      header.classList.add("shrink");
      logo?.classList.add("shrink");
    } else {
      header.classList.remove("shrink");
      logo?.classList.remove("shrink");
    }
  });
}

// Animate counters
function animateCounters() {
  const counters = document.querySelectorAll('.counter');
  counters.forEach(counter => {
    counter.innerText = '0';
    const update = () => {
      const target = +counter.getAttribute('data-target');
      const current = +counter.innerText;
      const increment = Math.ceil(target / 200);
      if (current < target) {
        counter.innerText = `${current + increment}`;
        setTimeout(update, 20);
      } else {
        counter.innerText = target;
      }
    };
    update();
  });
}

function observeImpactSection() {
  const section = document.getElementById("impact");
  if (!section) return;

  const observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      animateCounters();
      observer.unobserve(section);
    }
  }, { threshold: 0.3 });

  observer.observe(section);
}

// Scroll animation observer
function initScrollAnimations() {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in-up').forEach(el => observer.observe(el));
}

// Expand value cards
function initValueCards() {
  document.querySelectorAll('.value-card').forEach(card => {
    card.addEventListener('click', function () {
      document.querySelectorAll('.value-card').forEach(c => {
        if (c !== this) c.classList.remove('active');
      });
      this.classList.toggle('active');
    });
    card.addEventListener('keypress', function (e) {
      if (e.key === 'Enter' || e.key === ' ') this.click();
    });
  });
}

// Expand philosophy cards
function initPhilosophyCards() {
  document.querySelectorAll('.philosophy-card').forEach(card => {
    card.addEventListener('click', () => {
      card.classList.toggle('open');
    });
  });
}

// Expand value boxes
function initValueBoxes() {
  document.querySelectorAll('.value-box').forEach(box => {
    box.addEventListener('click', () => {
      box.classList.toggle('open');
    });
  });
}

// Global init
document.addEventListener("DOMContentLoaded", () => {
  includeHTML().then(() => {
    setupMobileMenu();
    setupShrinkHeader();
    initScrollAnimations();
    initPhilosophyCards();
    initValueBoxes();
    initValueCards();
    observeImpactSection(); // ← only runs once when visible
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("accept-cookies");

  if (!localStorage.getItem("cookiesAccepted")) {
    banner.style.display = "block";
  }

  acceptBtn?.addEventListener("click", () => {
    localStorage.setItem("cookiesAccepted", "true");
    banner.style.display = "none";
  });
});
