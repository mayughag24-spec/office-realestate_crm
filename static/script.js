document.addEventListener("DOMContentLoaded", function () {

    initTree();
    initContentLoader();

});

/* ================= TREE MENU ================= */
function initTree() {
    document.querySelectorAll(".toggle").forEach(toggle => {
        toggle.addEventListener("click", function () {
            this.parentElement.classList.toggle("open");
        });
    });
}

/* ================= CONTENT LOADER ================= */
function initContentLoader() {
    document.querySelectorAll(".load-content").forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            const url = this.dataset.url;

            fetch(url)
                .then(res => res.text())
                .then(html => {
                    const content = document.querySelector(".content");
                    content.innerHTML = html;

                    // IMPORTANT: re-init JS after load
                    reInitPageScripts();
                })
                .catch(err => console.error("Load error:", err));
        });
    });
}

/* ================= PAGE-SPECIFIC RE-INIT ================= */
function reInitPageScripts() {

    // Applicant tabs safety (if page contains them)
    if (document.querySelector(".tab-buttons")) {
        window.showApplicant = function (num, e) {
            document.querySelectorAll(".applicant-tab")
                .forEach(t => t.classList.remove("active"));

            document.querySelectorAll(".tab-buttons button")
                .forEach(b => b.classList.remove("active"));

            document.getElementById("applicant" + num)?.classList.add("active");
            e.target.classList.add("active");
        };
    }

    // Any future init functions go here
}
