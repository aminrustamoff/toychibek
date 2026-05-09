// login.js — password visibility toggle + form loading state

document.addEventListener('DOMContentLoaded', () => {

  // Password toggle
  const toggleBtn = document.getElementById('togglePw');
  const pwInput   = document.getElementById('password');
  const eyeOpen   = document.getElementById('eyeOpen');
  const eyeClosed = document.getElementById('eyeClosed');

  if (toggleBtn && pwInput) {
    toggleBtn.addEventListener('click', () => {
      const isPassword = pwInput.type === 'password';
      pwInput.type = isPassword ? 'text' : 'password';
      eyeOpen.style.display   = isPassword ? 'none'  : 'block';
      eyeClosed.style.display = isPassword ? 'block' : 'none';
    });
  }

  // Form loading state
  const form    = document.querySelector('.login-form');
  const loginBtn = document.querySelector('.login-btn');

  if (form && loginBtn) {
    form.addEventListener('submit', () => {
      loginBtn.style.opacity = '.7';
      loginBtn.style.pointerEvents = 'none';
      loginBtn.querySelector('span').textContent = 'Kirish...';
    });
  }

  // Focus first empty input
  const username = document.getElementById('username');
  const password = document.getElementById('password');
  if (username && !username.value) {
    username.focus();
  } else if (password) {
    password.focus();
  }
});
