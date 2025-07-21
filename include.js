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
  