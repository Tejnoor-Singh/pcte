let menubtn = document.querySelector(".mobilemenu");
let siderbarcontainer = document.querySelector(".sidebar-container");
menubtn.addEventListener("click", () => {
  siderbarcontainer.classList.toggle("active-sidebar");
});
function updateTimeAndDate() {
  const now = new Date();
  const timeElement = document.querySelector(".function-time .time");
  const dateElement = document.querySelector(".function-time .date");

  const hours = String(now.getHours());
  const minutes = String(now.getMinutes());
  const seconds = String(now.getSeconds());
  const timeString = ` ${hours}:${minutes}:${seconds}`;

  const day = String(now.getDate());
  const month = String(now.getMonth() + 1);
  const year = now.getFullYear();
  const dateString = ` ${day}-${month}-${year}`;

  timeElement.textContent = timeString;
  dateElement.textContent = dateString;
}

setInterval(updateTimeAndDate, 1000);

updateTimeAndDate();
let crosslabourform = document.querySelector(".crosslabourform");
crosslabourform.addEventListener("click", () => {
  document.querySelector(".add-labour-form-container").style.display = "none";
});
let addnewlabour = document.querySelector(".add-new-labour");
addnewlabour.addEventListener("click", () => {
  document.querySelector(".add-labour-form-container").style.display = "block";
});
let home = document.querySelector(".home-page");
let labour = document.querySelector(".labour-page");
let project = document.querySelector(".projects-page");
let setting = document.querySelector(".settings-page");
let homepage = document.querySelector(".home-container");
let labourpage = document.querySelector(".labour-container");
let trackpage = document.querySelector(".project-track-container");
let track = document.querySelector(".track");
home.addEventListener("click", () => {
  labourpage.style.display = "none";
  homepage.style.display = "block";
  trackpage.style.display = "none";
});
labour.addEventListener("click", () => {
  homepage.style.display = "none";
  labourpage.style.display = "block";
  trackpage.style.display = "none";
});
track.addEventListener("click", () => {
  homepage.style.display = "none";
  labourpage.style.display = "none";
  trackpage.style.display = "block";
});

let todo_ul = document.querySelector(".ul-for-todo");
let addtodo = document.querySelector(".addbtn");
addtodo.addEventListener("click", function () {
  let input = document.querySelector(".todoiteminput").value;
  if (input === "") {
    alert("enter some data in todo");
  } else {
    let element = document.createElement("li");
    element.classList.add("todo-item");
    element.innerHTML =
      "<span>" + input + "</span>" + " " + "<span class='del'>Delete</span>";
    todo_ul.append(element);
    let delButtons = element.querySelectorAll(".del");
    delButtons.forEach(function (del) {
      del.addEventListener("click", function () {
        console.log(del.parentElement);
        del.parentElement.remove();
      });
    });
  }
});
let updatecross = document.querySelector(".crossupdateform");
updatecross.addEventListener("click", function () {
  document.querySelector(".update-project-container").style.display = "none";
});
let updateprojectbtn = document.querySelector(".update-project");
updateprojectbtn.addEventListener("click", function () {
  document.querySelector(".update-project-container").style.display = "block";
});
//let link = document.querySelectorAll(".link-in-dashboard");
//let link_count = link.length;
//for (let i = 0; i <= link_count; i++) {
//  link[i].addEventListener("click", () => {
//    siderbarcontainer.classList.remove("active-sidebar");
//  });
//}
