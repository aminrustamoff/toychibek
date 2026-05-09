// base.js — global utilities, auto-dismiss alerts
document.addEventListener('DOMContentLoaded', () => {
  // Auto-dismiss alerts after 4 seconds
  document.querySelectorAll('.alert').forEach(alert => {
    setTimeout(() => {
      alert.style.transition = 'opacity .4s, transform .4s';
      alert.style.opacity = '0';
      alert.style.transform = 'translateX(10px)';
      setTimeout(() => alert.remove(), 400);
    }, 4000);
  });
});
