let logintab = document.querySelector(".login-tab");
let signuptab = document.querySelector(".signup-tab");
logincontent = document.querySelector(".form-login-container");
let signcontent = document.querySelector(".form-signup-container");
signuptab.addEventListener("click", () => {
  signcontent.style.display = "block";
  logincontent.style.display = "none";
  logintab.classList.remove("active-tab");
  signuptab.classList.add("active-tab");
});
logintab.addEventListener("click", () => {
  logincontent.style.display = "block";
  signcontent.style.display = "none";
  signuptab.classList.remove("active-tab");
  logintab.classList.add("active-tab");
});
document.querySelector(".upload-label").addEventListener("click",()=>{
document.getElementById("image").click()})