let menu = document.querySelector(".menu");
let side_nav = document.querySelector(".side-nav");
let side_nav_ul = document.querySelector(".side-nav ul");
let close_btn = document.querySelector(".close-btn");

menu.addEventListener("click", function () {
  side_nav.style.display = "block";
  side_nav.style.animation = "animate-open 0.5s forwards";
  setTimeout(() => {
    side_nav_ul.style.display = "flex";
    side_nav_ul.style.flexDirection = "column";
  }, 100);
});

close_btn.addEventListener("click", function () {
  side_nav.style.animation = "animate-close 0.5s forwards";
  setTimeout(() => {
    side_nav_ul.style.display = "none";
  }, 150);
  setTimeout(() => {
    side_nav.style.display = "none";
  }, 350);
});
