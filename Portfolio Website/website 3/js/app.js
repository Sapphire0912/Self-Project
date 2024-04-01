/* 控制所有 header 裡面導覽列選單事件 */
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
  }, 300);
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

/* 控制 Resume 選單的事件 */
/* 
   判斷使用者的視窗正在哪個頁面, 要更新 nav 的點選狀態 
   : 更新 currentClicked 數值
*/
let sectionNav = document.querySelectorAll(".each-nav");
let contentSection = document.querySelector(".content-section");
let currentClicked = "opt1";

function removeBeforeStatus() {
  /* 消除先前 button 的狀態 */
  sectionNav.forEach((eachNav) => {
    if (eachNav.classList[1] == currentClicked) {
      eachNav.children[0].classList.remove("active");
    }
  });
}

window.addEventListener("scroll", () => {
  let eachIdElement = contentSection.querySelectorAll("[id]");
  let windowHeight = window.innerHeight;
  let currentContentId;

  eachIdElement.forEach((content) => {
    let position = content.getBoundingClientRect();
    let centerY = windowHeight / 2;
    if (centerY >= position.top && centerY <= position.bottom) {
      currentContentId = content.id;
    }
  });
  currentContentId = "#" + currentContentId;
  sectionNav.forEach((eachNav) => {
    let href = eachNav.children[1].getAttribute("href");
    if (href == currentContentId && eachNav.classList[1] != currentClicked) {
      removeBeforeStatus();
      currentClicked = eachNav.classList[1];
      eachNav.children[0].classList.add("active");
    }
  });
});

sectionNav.forEach((eachNav) => {
  eachNav.addEventListener("click", (event) => {
    if (event.target.tagName == "A") {
      let parent = event.target.parentNode.classList[1];
      if (currentClicked != parent) {
        removeBeforeStatus();
        currentClicked = parent;
        event.target.parentNode.children[0].classList.add("active");
      }
    }
  });
});

/* 控制 back-top 的按鈕事件 */
let backTop = document.getElementById("back-top");
if (backTop != null) {
  window.addEventListener("scroll", () => {
    if (currentClicked == "opt1") {
      backTop.style.display = "none";
    } else {
      backTop.style.display = "block";
    }
  });

  backTop.addEventListener("click", (event) => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });
}
