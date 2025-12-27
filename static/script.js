document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".toggle").forEach(function (toggle) {
        toggle.addEventListener("click", function () {
            this.parentElement.classList.toggle("open");
        });
    });
});
