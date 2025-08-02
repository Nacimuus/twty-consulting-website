// Include HTML for header/footer
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

// Setup mobile menu
function setupMobileMenu() {
  const hamburger = document.querySelector(".hamburger");
  const closeMenu = document.querySelector(".close-menu");
  const mobileNav = document.querySelector(".mobile-nav");
  const dropdownToggles = document.querySelectorAll(".has-dropdown > a");

    // Hide close icon initially
    closeMenu.style.display = "none";

  if (!hamburger || !closeMenu || !mobileNav) return;

  hamburger.addEventListener("click", () => {
    mobileNav.classList.add("active");
    hamburger.style.display = "none";
    closeMenu.style.display = "block";
    
  });

  closeMenu.addEventListener("click", () => {
    mobileNav.classList.remove("active");
    closeMenu.style.display = "none";
    hamburger.style.display = "block";
  });

  dropdownToggles.forEach(link => {
    link.addEventListener("click", (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        const parent = link.parentElement;
        parent.classList.toggle("open");
      }
    });
  });
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

// Observe section for counters
function observeImpactSection() {
  const section = document.getElementById("impact");
  if (!section) return;
  const observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      section.querySelectorAll('.impact-item').forEach(item => item.classList.add('show'));
      animateCounters();
      observer.unobserve(section);
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

// Cookie banner
function setupCookieBanner() {
  const banner = document.getElementById("cookie-banner");
  const acceptBtn = document.getElementById("accept-cookies");
  const refuseBtn = document.getElementById("refuse-cookies");

  if (!banner) return;
  if (!localStorage.getItem("cookiesAccepted") && !localStorage.getItem("cookiesRefused")) {
    banner.style.display = "block";
  }
  acceptBtn?.addEventListener("click", () => {
    localStorage.setItem("cookiesAccepted", "true");
    banner.style.display = "none";
  });
  refuseBtn?.addEventListener("click", () => {
    localStorage.setItem("cookiesRefused", "true");
    banner.style.display = "none";
  });
}

// Carousel logic
function initCarousel(trackSelector, slideSelector) {
  const track = document.querySelector(trackSelector);
  if (!track) return;
   const achievementTrack = document.querySelector('.achievements-track');
  const achievementSlides = document.querySelectorAll('.achievement-slide');
  const achievementLeftBtn = document.querySelector('.achievements-carousel .carousel-btn.left');
  const achievementRightBtn = document.querySelector('.achievements-carousel .carousel-btn.right');

  let achievementIndex = 0;
  const achievementSlideWidth = achievementSlides[0].offsetWidth + 40;

  function moveAchievementCarousel(direction) {
    if (direction === 'left') {
      achievementIndex = (achievementIndex <= 0) ? achievementSlides.length - 1 : achievementIndex - 1;
    } else {
      achievementIndex = (achievementIndex >= achievementSlides.length - 1) ? 0 : achievementIndex + 1;
    }
    achievementTrack.style.transform = `translateX(-${achievementIndex * achievementSlideWidth}px)`;
  }

  achievementRightBtn.addEventListener("click", () => moveAchievementCarousel('right'));
  achievementLeftBtn.addEventListener("click", () => moveAchievementCarousel('left'));

  setInterval(() => moveAchievementCarousel('right'), 6000);

  let achievementStartX = 0;
  let achievementSwiping = false;

  achievementTrack.addEventListener('touchstart', e => {
    achievementStartX = e.touches[0].clientX;
    achievementSwiping = true;
  });

  achievementTrack.addEventListener('touchmove', e => {
    if (!achievementSwiping) return;
    const diffX = e.touches[0].clientX - achievementStartX;
    if (Math.abs(diffX) > 50) {
      moveAchievementCarousel(diffX > 0 ? 'left' : 'right');
      achievementSwiping = false;
    }
  });

  achievementTrack.addEventListener('touchend', () => {
    achievementSwiping = false;
  });

  // === THEY TRUST US CAROUSEL ===
  const trustTrack = document.querySelector('.trust-track');
  const trustSlides = document.querySelectorAll('.trust-slide');
  const trustLeftBtn = document.querySelector('.trust-carousel .carousel-btn.left');
  const trustRightBtn = document.querySelector('.trust-carousel .carousel-btn.right');

  let trustIndex = 0;
  const trustSlideWidth = trustSlides[0].offsetWidth + 40;

  function moveTrustCarousel(direction) {
    if (direction === 'left') {
      trustIndex = (trustIndex <= 0) ? trustSlides.length - 1 : trustIndex - 1;
    } else {
      trustIndex = (trustIndex >= trustSlides.length - 1) ? 0 : trustIndex + 1;
    }
    trustTrack.style.transform = `translateX(-${trustIndex * trustSlideWidth}px)`;
  }

  trustRightBtn.addEventListener("click", () => moveTrustCarousel('right'));
  trustLeftBtn.addEventListener("click", () => moveTrustCarousel('left'));

  setInterval(() => moveTrustCarousel('right'), 5000);

  let trustStartX = 0;
  let trustSwiping = false;

  trustTrack.addEventListener('touchstart', e => {
    trustStartX = e.touches[0].clientX;
    trustSwiping = true;
  });

  trustTrack.addEventListener('touchmove', e => {
    if (!trustSwiping) return;
    const diffX = e.touches[0].clientX - trustStartX;
    if (Math.abs(diffX) > 50) {
      moveTrustCarousel(diffX > 0 ? 'left' : 'right');
      trustSwiping = false;
    }
  });

  trustTrack.addEventListener('touchend', () => {
    trustSwiping = false;
  });
};

// 🔄 MAIN INIT FLOW
document.addEventListener("DOMContentLoaded", () => {
  includeHTML().then(() => {
    setupMobileMenu();
    setupShrinkHeader();
    observeImpactSection();
    initScrollAnimations();
    setupCookieBanner();
    initCarousel('.carousel-track', '.carousel-slide'); // logos
    initCarousel('.achievements-track', '.achievement-slide'); // achievements
  });
});
