function loadDashboard() {
    const content = document.getElementById("content");
    content.innerHTML = `
        <h1>CRM Home Dashboard is running successfully 🚀</h1>
    `;
}

function loadPage(title) {
    const content = document.getElementById("content");
    content.innerHTML = `<h2>${title}</h2><p>Module under construction</p>`;
}

function loadUnitBooking() {
    const template = document.getElementById("unitBookingTemplate");
    const content = document.getElementById("content");

    // Clear content
    content.innerHTML = "";

    // Clone template and append
    const clone = template.content.cloneNode(true);
    content.appendChild(clone);
}
