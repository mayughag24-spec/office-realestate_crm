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
