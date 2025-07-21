document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("header");
    const logo = document.querySelector(".logo");
    const hamburger = document.querySelector(".hamburger");
    const navbar = document.getElementById("navbar");
  
    // Header shrink on scroll
    window.addEventListener("scroll", () => {
      if (window.scrollY > 50) {
        header.classList.add("shrink");
        logo?.classList.add("shrink");
      } else {
        header.classList.remove("shrink");
        logo?.classList.remove("shrink");
      }
    });
  
    // Toggle mobile nav
    if (hamburger && navbar) {
      hamburger.addEventListener("click", () => {
        navbar.classList.toggle("active");
      });
    }
  
    // Load external HTML files (header/footer)
    includeHTML();
  });
  
  function includeHTML() {
    const elements = document.querySelectorAll("[w3-include-html]");
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
            includeHTML(); // Handle nested includes if needed
          })
          .catch(err => {
            el.innerHTML = "Page not found.";
            console.error(err);
          });
      }
    });
  }
  
  document.addEventListener("DOMContentLoaded", includeHTML);
  