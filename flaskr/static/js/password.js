const passwordBtn   = document.querySelector("#toggle__password");
const passwordInput = document.querySelector("#password")

passwordBtn.addEventListener("click",()=>{

    passwordInput.type = passwordInput.type === "password" ? "text" : "password";
    passwordBtn.classList.toggle("fa-eye");
    passwordBtn.classList.toggle("fa-eye-slash")
    
});