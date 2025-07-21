// 1. Include HTML (for header/footer)
function includeHTML(callback) {
    const elements = document.querySelectorAll("[w3-include-html]");
    let total = elements.length;
    let loaded = 0;
  
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
            if (loaded === total && typeof callback === "function") {
              callback(); // Only run after all includes
            }
          })
          .catch(err => {
            el.innerHTML = "Page not found.";
            console.error(err);
          });
      }
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
  