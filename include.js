window.addEventListener("DOMContentLoaded", () => {
    const loadHTML = async (selector, file) => {
      try {
        const response = await fetch(file);
        const html = await response.text();
        document.querySelector(selector).innerHTML = html;
      } catch (error) {
        console.error(`Failed to load ${file}:`, error);
      }
    };
  
    loadHTML("#header", "header.html");
    loadHTML("#footer", "footer.html");
  });
  function includeHTML() {
    return new Promise(resolve => {
      const elements = document.querySelectorAll("[w3-include-html]");
      let total = elements.length;
      let loaded = 0;
  
      elements.forEach(el => {
        const file = el.getAttribute("w3-include-html");
        if (file) {
          fetch(file)
            .then(response => response.text())
            .then(data => {
              el.innerHTML = data;
              el.removeAttribute("w3-include-html");
              loaded++;
              if (loaded === total) resolve();
            })
            .catch(() => {
              el.innerHTML = "Page not found.";
              loaded++;
              if (loaded === total) resolve();
            });
        }
      });
    });
  }
  