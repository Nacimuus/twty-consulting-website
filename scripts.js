document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector("header");
    const logo = document.querySelector(".logo");
  
    window.addEventListener("scroll", () => {
      if (window.scrollY > 50) {
        header.classList.add("shrink");
        if (logo) logo.classList.add("shrink");
      } else {
        header.classList.remove("shrink");
        if (logo) logo.classList.remove("shrink");
      }
    });
    const burger = document.querySelector(".burger");
    const nav = document.querySelector("nav ul");
  
    if (burger && nav) {
      burger.addEventListener("click", () => {
        nav.classList.toggle("open");
      });
    }
  });
  const hamburger = document.getElementById('hamburger');
const navbar = document.getElementById('navbar');
const logo = document.querySelector(".logo");
const header = document.querySelector("header");

hamburger.addEventListener('click', () => {
  navbar.classList.toggle('active');
});

window.addEventListener("scroll", () => {
  if (window.scrollY > 50) {
    header.classList.add("shrink");
    logo.classList.add("shrink");
  } else {
    header.classList.remove("shrink");
    logo.classList.remove("shrink");
  }
});
