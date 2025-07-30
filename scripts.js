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

  if (hamburger && navbar && closeMenu) {
    hamburger.addEventListener("click", () => {
      navbar.classList.add("active");
      closeMenu.classList.add("active");
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
      const items = section.querySelectorAll('.impact-item');
      items.forEach(item => item.classList.add('show'));
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
  document.querySelectorAll('.has-dropdown').forEach(item => {
    const link = item.querySelector('a');

    if (link) {
      link.addEventListener('click', (e) => {
        e.preventDefault();

        // Only toggle on click for mobile screens
        if (window.innerWidth <= 768) {
          item.classList.toggle('open');
        }
      });
    }

    item.addEventListener('mouseenter', () => {
      item.classList.add('open');
    });

    item.addEventListener('mouseleave', () => {
      item.classList.remove('open');
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
document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector('.carousel-track');
  const slides = document.querySelectorAll('.carousel-slide');
  const leftBtn = document.querySelector('.carousel-btn.left');
  const rightBtn = document.querySelector('.carousel-btn.right');

  let index = 0;
  const slideWidth = slides[0].offsetWidth + 40;

  function moveCarousel(direction) {
    if (direction === 'left') {
      index = (index <= 0) ? slides.length / 2 - 1 : index - 1;
    } else {
      index = (index >= slides.length / 2 - 1) ? 0 : index + 1;
    }
    track.style.transform = `translateX(-${index * slideWidth}px)`;
  }

  rightBtn.addEventListener("click", () => moveCarousel('right'));
  leftBtn.addEventListener("click", () => moveCarousel('left'));

  // Auto-scroll
  setInterval(() => moveCarousel('right'), 4000);

  // Swipe support
  let startX = 0;
  let isSwiping = false;

  track.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
    isSwiping = true;
  });

  track.addEventListener('touchmove', e => {
    if (!isSwiping) return;
    const diffX = e.touches[0].clientX - startX;
    if (Math.abs(diffX) > 50) {
      moveCarousel(diffX > 0 ? 'left' : 'right');
      isSwiping = false;
    }
  });

  track.addEventListener('touchend', () => {
    isSwiping = false;
  });
});
function initCarousel(trackSelector, slideSelector) {
  const track = document.querySelector(trackSelector);
  const slides = track.querySelectorAll(slideSelector);
  const wrapper = track.closest(".carousel-wrapper");
  const leftBtn = wrapper.querySelector(".carousel-btn.left");
  const rightBtn = wrapper.querySelector(".carousel-btn.right");

  let index = 0;
  const slideWidth = slides[0].offsetWidth + 40;

  function moveCarousel(direction) {
    if (direction === 'left') {
      index = (index <= 0) ? slides.length - 1 : index - 1;
    } else {
      index = (index >= slides.length - 1) ? 0 : index + 1;
    }
    track.style.transform = `translateX(-${index * slideWidth}px)`;
  }

  leftBtn.addEventListener("click", () => moveCarousel('left'));
  rightBtn.addEventListener("click", () => moveCarousel('right'));

  // Swipe support
  let startX = 0;
  let isSwiping = false;

  track.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
    isSwiping = true;
  });

  track.addEventListener('touchmove', e => {
    if (!isSwiping) return;
    const diffX = e.touches[0].clientX - startX;
    if (Math.abs(diffX) > 50) {
      moveCarousel(diffX > 0 ? 'left' : 'right');
      isSwiping = false;
    }
  });

  track.addEventListener('touchend', () => {
    isSwiping = false;
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initCarousel('.carousel-track', '.carousel-slide'); // logos
  initCarousel('.achievements-track', '.achievement-slide'); // achievements
});
