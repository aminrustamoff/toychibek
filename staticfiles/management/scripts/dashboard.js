// dashboard.js — counter animation for stat values

document.addEventListener('DOMContentLoaded', () => {

  const animateCounter = (el, target, duration = 800) => {
    const start = performance.now();
    const isFloat = String(target).includes('.');

    const step = (timestamp) => {
      const elapsed = timestamp - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = eased * target;

      if (isFloat) {
        el.textContent = '$' + Math.round(current).toLocaleString();
      } else {
        el.textContent = Math.round(current).toLocaleString();
      }

      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  document.querySelectorAll('.stat-value').forEach(el => {
    const raw = el.textContent.replace(/[^0-9.]/g, '');
    const num = parseFloat(raw);
    if (!isNaN(num) && num > 0) {
      const isDollar = el.textContent.includes('$');
      el.textContent = isDollar ? '$0' : '0';
      setTimeout(() => animateCounter(el, num, 900), 200);
    }
  });
});
