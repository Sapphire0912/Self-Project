let menu = document.querySelector(".menu");
let side_nav = document.querySelector(".side-nav");
let close_btn = document.querySelector(".close-btn");

menu.addEventListener("click", function () {
  side_nav.style.display = "block";
});

close_btn.addEventListener("click", function () {
  side_nav.style.display = "none";
});

window.addEventListener("resize", function () {
  let title = document.querySelector(".web-title");
  let text_info = document.querySelector(".text-info");
  if (window.innerWidth <= 600) {
    title.children[1].innerHTML = "Portfolio Website";
  } else {
    title.children[1].innerHTML = "/ Portfolio Website";
  }

  if (window.innerWidth <= 800) {
    text_info.children[1].innerHTML = "國立高雄科技大學 | 電子工程系 畢業";
  } else {
    text_info.children[1].innerHTML = "國立高雄科技大學 <br />電子工程系 畢業";
  }
});
