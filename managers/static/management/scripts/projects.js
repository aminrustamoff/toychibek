// projects.js — delete modal + image preview for form

// ---- Delete Modal (project list page) ----
function confirmDelete(btn) {
  const id   = btn.dataset.id;
  const name = btn.dataset.name;
  const modal = document.getElementById('deleteModal');
  const nameSpan = document.getElementById('projectNameSpan');
  const form = document.getElementById('deleteForm');

  if (!modal) return;
  nameSpan.textContent = name;
  form.action = `/management/projects/${id}/delete/`;
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

  // Close modal on backdrop click
  const modal = document.getElementById('deleteModal');
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });
    // ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });
  }

  // ---- Image Preview (form page) ----
  const fileInput   = document.querySelector('.form-file-input, input[type="file"]');
  const previewImg  = document.getElementById('previewImg');
  const placeholder = document.getElementById('uploadPlaceholder');

  if (fileInput && previewImg) {
    fileInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;

      if (!file.type.startsWith('image/')) {
        alert("Iltimos, rasm faylini tanlang.");
        fileInput.value = '';
        return;
      }

      const reader = new FileReader();
      reader.onload = (ev) => {
        previewImg.src = ev.target.result;
        previewImg.style.display = 'block';
        if (placeholder) placeholder.style.display = 'none';
      };
      reader.readAsDataURL(file);
    });
  }
});
