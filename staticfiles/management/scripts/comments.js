// comments.js — delete confirmation modal

function confirmDelete(btn) {
  const id   = btn.dataset.id;
  const name = btn.dataset.name;
  const modal = document.getElementById('deleteModal');
  const authorSpan = document.getElementById('commentAuthorSpan');
  const form = document.getElementById('deleteForm');

  if (!modal) return;
  authorSpan.textContent = name;
  form.action = `/management/comments/${id}/delete/`;
  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const modal = document.getElementById('deleteModal');
  if (modal) {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('deleteModal');
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });
  }
});
