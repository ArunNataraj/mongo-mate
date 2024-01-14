document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const errorMessage = document.getElementById("error-message");
  
    loginForm.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const username = document.getElementById("email").value;
      const password = document.getElementById("password").value;
  
      // Make API request to the backend for authentication
      fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: username ,
          password: password,
        }),
      })
        .then(response => response.json())
        .then(data => {
          // Check if the authentication was successful
          if ("access_token" in data) {
            // Redirect to the dashboard or perform other actions
            localStorage.setItem("accessToken", data.access_token);
            window.location.href = "dashboard.html";
          } else {
            errorMessage.textContent = "Invalid credentials";
          }
        })
        .catch(error => {
          console.error("Error during authentication:", error);
          errorMessage.textContent = "Error during authentication";
        });
    });
  });
  