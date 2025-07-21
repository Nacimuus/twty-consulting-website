// 1. Include HTML (for header/footer)
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
  
  // 2. Setup mobile menu toggle
  function setupMobileMenu() {
    const hamburger = document.querySelector(".hamburger");
    const navMenu = document.querySelector("nav ul");
  
    if (hamburger && navMenu) {
      hamburger.addEventListener("click", () => {
        navMenu.classList.toggle("open");
      });
    }
  }
  
  // 3. Setup shrink on scroll
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
  
  // 4. Run once DOM is loaded
  document.addEventListener("DOMContentLoaded", () => {
    includeHTML(() => {
      setupMobileMenu();
      setupShrinkHeader();
    });
  });
  // Expand/collapse for value cards
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.value-card').forEach(card => {
      card.addEventListener('click', function() {
        // Collapse others if you want only one open at a time:
        document.querySelectorAll('.value-card').forEach(c => {
          if (c !== this) c.classList.remove('active');
        });
        // Toggle this one
        this.classList.toggle('active');
      });
      // Optional: keyboard accessibility
      card.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          this.click();
        }
      });
    });
  });
  function initNavigation() {
    const header = document.querySelector("header");
    const logo = document.querySelector(".logo");
    const hamburger = document.querySelector(".hamburger");
    const navbar = document.getElementById("navbar");
  
    // Shrink header on scroll
    window.addEventListener("scroll", () => {
      if (window.scrollY > 50) {
        header?.classList.add("shrink");
        logo?.classList.add("shrink");
      } else {
        header?.classList.remove("shrink");
        logo?.classList.remove("shrink");
      }
    });
  
    // Toggle mobile menu
    if (hamburger && navbar) {
      hamburger.addEventListener("click", () => {
        navbar.classList.toggle("active");
      });
    }
  }
  document.addEventListener("DOMContentLoaded", () => {
    includeHTML().then(() => {
      initNavigation();
    });
  });
  function initPhilosophyCards() {
    const cards = document.querySelectorAll('.philosophy-card');
  
    cards.forEach(card => {
      card.addEventListener('click', () => {
        card.classList.toggle('open'); // allows multiple cards to be open at once
      });
    });
  }
  document.addEventListener("DOMContentLoaded", () => {
    includeHTML().then(() => {
      initNavigation();
      initPhilosophyCards(); // ✅ Call it here
    });
  });
  function initValueBoxes() {
    const boxes = document.querySelectorAll('.value-box');
  
    boxes.forEach(box => {
      box.addEventListener('click', () => {
        box.classList.toggle('open');
      });
    });
  }
  
  // After header/footer injected
  includeHTML().then(() => {
    initNavigation();
    initValueBoxes();
  });
  document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector(".hamburger");
    const closeMenu = document.querySelector(".close-menu");
    const navbar = document.getElementById("navbar");
  
    if (hamburger && navbar) {
      hamburger.addEventListener("click", () => {
        const isActive = navbar.classList.toggle("active");
        if (closeMenu) {
          closeMenu.classList.toggle("active", isActive);
        }
      });
    }
  
    if (closeMenu && navbar) {
      closeMenu.addEventListener("click", () => {
        navbar.classList.remove("active");
        closeMenu.classList.remove("active");
      });
    }
  });
  document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".impact-item");
  
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("show");
        }
      });
    }, { threshold: 0.3 });
  
    items.forEach(item => observer.observe(item));
  });
  