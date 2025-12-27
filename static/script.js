document.querySelectorAll('.tree > li > span').forEach(item => {
  item.addEventListener('click', function () {
    this.parentElement.classList.toggle('open');
  });
});

function loadPage(page) {
  document.getElementById("content").innerHTML =
    "<h2>" + page + " page loaded</h2>";
}
