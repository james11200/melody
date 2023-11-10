
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "melody") {
        // alert("登入成功");
        window.open('http://localhost:3000/users/user-list',"_self");
        // location.reload('http://localhost:3000/users/user-list');
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})