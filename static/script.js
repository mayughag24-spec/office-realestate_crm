document.addEventListener("DOMContentLoaded", function () {
    // TREE TOGGLE
    document.querySelectorAll(".toggle").forEach(function (toggle) {
        toggle.addEventListener("click", function () {
            this.parentElement.classList.toggle("open");
        });
    });

    // CONTENT LOADER
    document.querySelectorAll(".load-content").forEach(function (link) {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const url = this.getAttribute("data-url");
            fetch(url)
                .then(response => response.text())
                .then(html => {
                    document.querySelector(".content").innerHTML = html;
                })
                .catch(error => {
                    console.error("Error loading content:", error);
                });
        });
    });
});
