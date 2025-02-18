document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("show-generator").addEventListener("click", function() {
      loadGenerator();
  });

  document.getElementById("show-checker").addEventListener("click", function() {
      loadChecker();
  });

  // Dark Mode Toggle
  document.getElementById("toggle-mode").addEventListener("click", function() {
      document.body.classList.toggle("dark-mode");
  });
});

function loadGenerator() {
  document.getElementById("content").innerHTML = `
      <h2>Password Generator</h2>
      <label for="password-length">Choose length (12-64):</label>
      <input type="number" id="password-length" min="12" max="64" value="16">
      <button id="generate">Generate Password</button>
      <h3>Your Password:</h3>
      <div id="password-box">
          <h4 id="password">Click "Generate" to create a password</h4>
      </div>
      <button class="back-btn" onclick="window.location.reload();">Back</button>
  `;

  document.getElementById("generate").addEventListener("click", function() {
      let lengthInput = document.getElementById("password-length").value;
      let length = parseInt(lengthInput, 10);

      if (isNaN(length) || length < 12 || length > 64) {
          alert("Please enter a valid length between 12 and 64.");
          return;
      }

      const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
      let password = "";

      for (let i = 0; i < length; i++) {
          password += charset.charAt(Math.floor(Math.random() * charset.length));
      }

      document.getElementById("password").textContent = password;
  });
}

function loadChecker() {
  document.getElementById("content").innerHTML = `
      <h2>Password Strength Checker</h2>
      <input type="password" id="password" placeholder="Enter your password">
      <p id="strength">Password Strength: </p>
      <div class="progress-container">
          <div class="progress-bar" id="progress-bar"></div>
      </div>
      <button class="back-btn" onclick="window.location.reload();">Back</button>
  `;

  let passwordInput = document.getElementById("password");
  let strengthText = document.getElementById("strength");
  let progressBar = document.getElementById("progress-bar");

  passwordInput.addEventListener("input", function() {
      let password = passwordInput.value;
      if (password.length === 0) {
          strengthText.textContent = "Enter a password to check strength.";
          progressBar.style.width = "0%";
          progressBar.className = "progress-bar";
          return;
      }
      let score = checkPasswordStrength(password);
      displayStrength(score);
  });

  function checkPasswordStrength(password) {
      let score = 0;

      // Length Scoring
      if (password.length >= 12 && password.length < 16) score += 1;
      else if (password.length >= 16 && password.length < 20) score += 2;
      else if (password.length >= 20 && password.length < 24) score += 3;
      else if (password.length >= 24) score += 4;

      // Character Variety Scoring
      if (password.match(/[A-Z]/)) score += 1;  // Uppercase letters
      if (password.match(/[a-z]/)) score += 1;  // Lowercase letters
      if (password.match(/[0-9]/)) score += 1;  // Numbers
      if (password.match(/[^a-zA-Z0-9]/)) score += 2; // Special symbols

      return score;
  }

  function displayStrength(score) {
      let progressWidths = ["0%", "20%", "40%", "60%", "80%", "100%"];
      let strengthLevels = ["Weak ❌", "Moderate ⚠️", "Strong 💪", "Very Strong 🔥"];
      let colors = ["red", "orange", "yellow", "green"];

      let level = score <= 2 ? 0 : score <= 4 ? 1 : score <= 6 ? 2 : 3;

      strengthText.textContent = "Password Strength: " + strengthLevels[level];

      // ✅ **Fix: Set progress bar to 100% for "Very Strong"**
      progressBar.style.width = level === 3 ? "100%" : progressWidths[level + 1]; 
      progressBar.style.background = colors[level];
  }
}
