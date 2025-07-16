document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("header");
    const logo = document.querySelector(".logo");
    const hamburger = document.querySelector(".hamburger");
    const nav = document.getElementById("navbar");
  
    // Sticky shrink header
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
    if (hamburger && nav) {
      hamburger.addEventListener("click", () => {
        nav.classList.toggle("active");
      });
    }
  });  