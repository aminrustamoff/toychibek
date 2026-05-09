// messages.js — search/filter messages

document.addEventListener('DOMContentLoaded', () => {
  // Simple search could be added here if needed in future
  // Currently the page just displays messages
  
  // Animate cards in
  const cards = document.querySelectorAll('.message-card');
  cards.forEach((card, i) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(8px)';
    card.style.transition = `opacity .25s ease ${i * 50}ms, transform .25s ease ${i * 50}ms`;
    requestAnimationFrame(() => {
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    });
  });
});
