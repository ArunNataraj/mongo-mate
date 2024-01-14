// registration.js
document.addEventListener("DOMContentLoaded", function () {
    const registrationForm = document.getElementById("registerForm");
    const passwordField = document.getElementById("password");
    const confirmPasswordField = document.getElementById("confirmPassword");
    const passwordError = document.getElementById("passwordError");

    confirmPasswordField.addEventListener("input", function () {
        const password = passwordField.value;
        const confirmPassword = confirmPasswordField.value;

        if (confirmPassword.trim() !== "" && password !== confirmPassword) {
            passwordError.textContent = "Passwords do not match.";
        } else {
            passwordError.textContent = "";
        }
    });

    registrationForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        // Make API request to the backend for authentication
        fetch("http://localhost:8000/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: username,
                password: password,
            }),
        })
            .then(response => response.json())
            .then(data => {
                passwordError.textContent = data.message;
                setTimeout(function () {
                    window.location.href = "login.html";
                }, 3000);
            })
            .catch(error => {
                console.error(error);
            });
    });
});
