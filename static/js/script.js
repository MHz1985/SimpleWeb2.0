const sidebar = document.querySelector(".sidebar");
const sidebarClose = document.querySelector("#sidebar-close");
const menu = document.querySelector(".menu-content");
const menuItems = document.querySelectorAll(".submenu-item");
const subMenuTitles = document.querySelectorAll(".submenu .menu-title");

sidebarClose.addEventListener("click", () => sidebar.classList.toggle("close"));

menuItems.forEach((item, index) => {
  item.addEventListener("click", () => {
    menu.classList.add("submenu-active");
    item.classList.add("show-submenu");
    menuItems.forEach((item2, index2) => {
      if (index !== index2) {
        item2.classList.remove("show-submenu");
      }
    });
  });
});

subMenuTitles.forEach((title) => {
  title.addEventListener("click", () => {
    menu.classList.remove("submenu-active");
  });
});

console.log(menuItems, subMenuTitles);

// let navToggle = document.querySelector(".nav__toggle");
// let navWrapper = document.querySelector(".nav__wrapper");

// navToggle.addEventListener("click", function () {
//   if (navWrapper.classList.contains("active")) {
//     this.setAttribute("aria-expanded", "false");
//     this.setAttribute("aria-label", "menu");
//     navWrapper.classList.remove("active");
//   } else {
//     navWrapper.classList.add("active");
//     this.setAttribute("aria-label", "close menu");
//     this.setAttribute("aria-expanded", "true");
//   }
// });

// let searchToggle = document.querySelector(".search__toggle");
// let searchForm = document.querySelector(".search__form");

// searchToggle.addEventListener("click", showSearch);

// function showSearch() {
//   searchForm.classList.toggle("active");
// }

