const errorsMsg     = document.querySelector("#info_error");
const form          = document.querySelector("#form");
const passwordInput = document.querySelector("#password");
const specialCharacters = ["@", "#", "$", "%", "^", "&", "*", "|"];
form.addEventListener('submit', (e) =>{

    let hasSpecialCharacter = false;

    let errors = [];
    console.log(passwordInput);
    if (passwordInput.value.length < 8){
        errors.push("Password must be at least 8 characters long!")
    }

    for (const char of passwordInput.value){
        if (specialCharacters.includes(char)){
            hasSpecialCharacter = true;
        }
    }


    if(!hasSpecialCharacter){
        errors.push("Your password must have one of the following characters: " + specialCharacters.join(","));
    }
    if(errors.length > 0){
        e.preventDefault();
        errorsMsg.innerText = errors.join(', ');
    }
})