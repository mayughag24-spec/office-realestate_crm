function loadDashboard() {
  document.getElementById("content").innerHTML =
    "<h1>CRM Home Dashboard is running successfully 🚀</h1>";
}

function loadPage(name) {
  document.getElementById("content").innerHTML =
    "<h2>" + name + "</h2><p>Module under construction</p>";
}

function loadUnitBooking() {
  const content = document.getElementById("content");
  const template = document.getElementById("unitBookingTemplate");

  content.innerHTML = "";
  content.appendChild(template.content.cloneNode(true));
}
