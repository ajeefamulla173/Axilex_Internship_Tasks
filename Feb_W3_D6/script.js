// Alert
function showAlert() {
    alert("Welcome to the Futuristic JavaScript Experience!");
}

// Change Text
function changeText() {
    const heading = document.getElementById("mainText");
    heading.innerHTML = "Heading Updated Successfully!";
    heading.style.color = "#00f5ff";
}

// Calculator
function calculate() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const resultDiv = document.getElementById("result");

    if (isNaN(num1) || isNaN(num2)) {
        resultDiv.innerHTML = "Please enter valid numbers.";
        resultDiv.style.color = "red";
        return;
    }

    const sum = num1 + num2;
    resultDiv.innerHTML = "Result: " + sum;
    resultDiv.style.color = "#00f5ff";
}

// Form Validation
function validateForm() {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const messageDiv = document.getElementById("message");

    if (name === "" || email === "" || password === "") {
        messageDiv.innerHTML = "All fields are required.";
        messageDiv.style.color = "red";
        return;
    }

    if (password.length < 6) {
        messageDiv.innerHTML = "Password must be at least 6 characters.";
        messageDiv.style.color = "red";
        return;
    }

    messageDiv.innerHTML = "Form submitted successfully!";
    messageDiv.style.color = "#00f5ff";
}