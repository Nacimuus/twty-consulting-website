// Include HTML for header and footer
function includeHTML() {
  return new Promise((resolve, reject) => {
    const elements = document.querySelectorAll("[w3-include-html]");
    let total = elements.length;
    let loaded = 0;

    if (total === 0) return resolve();

    elements.forEach(el => {
      const file = el.getAttribute("w3-include-html");
      if (file) {
        fetch(file)
          .then(res => {
            if (!res.ok) throw new Error("Failed to load " + file);
            return res.text();
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

// Shrink header on scroll
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

// Observe impact section for counter animation
function observeImpactSection() {
  const section = document.getElementById("impact");
  if (!section) return;

  const observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      animateCounters();
      observer.unobserve(section); // Only once
    }
  }, { threshold: 0.3 });

  observer.observe(section);
}

// Scroll animations
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

// Cookie consent
function setupCookieBanner() {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("accept-cookies");

  if (!banner) return;

  if (!localStorage.getItem("cookiesAccepted")) {
    banner.style.display = "block";
  }

  acceptBtn?.addEventListener("click", () => {
    localStorage.setItem("cookiesAccepted", "true");
    banner.style.display = "none";
  });
}

// Dropdown for desktop nav
function setupDropdowns() {
  document.querySelectorAll('.has-dropdown > a').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const parent = link.parentElement;
      parent.classList.toggle('open');
    });
  });
}

// Init
document.addEventListener("DOMContentLoaded", () => {
  includeHTML().then(() => {
    setupMobileMenu();
    setupShrinkHeader();
    observeImpactSection();
    initScrollAnimations();
    setupCookieBanner();
    setupDropdowns();
  });
});
