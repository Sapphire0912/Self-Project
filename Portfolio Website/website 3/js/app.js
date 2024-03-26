let menu = document.querySelector(".menu");
let side_nav = document.querySelector(".side-nav");
let close_btn = document.querySelector(".close-btn");

menu.addEventListener("click", function () {
  side_nav.style.display = "block";
});

close_btn.addEventListener("click", function () {
  side_nav.style.display = "none";
});
