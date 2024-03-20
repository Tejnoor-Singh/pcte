let crosso = document.querySelector(".crossadd-projectform");
crosso.addEventListener("click", () => {
  document.querySelector(".add-new-project-container").style.display = "none";
});
let add = document.querySelector(".add-project");
add.addEventListener("click", () => {
  document.querySelector(".add-new-project-container").style.display = "flex";
});

let labourcon = document.querySelector(".labour-content-container");
let track = document.querySelector(".trackpage");
track.addEventListener("click", () => {
  document.querySelector(".home-container").style.display = "none";
  labourcon.style.display = "block";
});
let home = document.querySelector(".home-container");
let homepage = document.querySelector(".home-page");
homepage.addEventListener("click", () => {
  document.querySelector(".home-container").style.display = "block";
  labourcon.style.display = "none";
});

let menubtn = document.querySelector(".mobilemenu");
let siderbarcontainer = document.querySelector(".sidebar-container");
menubtn.addEventListener("click", () => {
  siderbarcontainer.classList.toggle("active-sidebar");
});