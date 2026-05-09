// management_base.js — sidebar toggle + top bar date

document.addEventListener('DOMContentLoaded', () => {

  // ---- Live Date in Top Bar ----
  const dateEl = document.getElementById('topDate');
  if (dateEl) {
    const updateDate = () => {
      const now = new Date();
      const opts = { weekday: 'short', year: 'numeric', month: 'short', day: 'numeric' };
      dateEl.textContent = now.toLocaleDateString('uz-UZ', opts) ||
        now.toLocaleDateString('en-US', opts);
    };
    updateDate();
    setInterval(updateDate, 60000);
  }

  // ---- Mobile Sidebar Toggle ----
  const sidebar  = document.getElementById('sidebar');
  const toggle   = document.getElementById('menuToggle');

  if (!sidebar || !toggle) return;

  // Create overlay
  const overlay = document.createElement('div');
  overlay.className = 'sidebar-overlay';
  document.body.appendChild(overlay);

  const openSidebar = () => {
    sidebar.classList.add('open');
    overlay.classList.add('show');
    document.body.style.overflow = 'hidden';
  };
  const closeSidebar = () => {
    sidebar.classList.remove('open');
    overlay.classList.remove('show');
    document.body.style.overflow = '';
  };

  toggle.addEventListener('click', () => {
    sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
  });
  overlay.addEventListener('click', closeSidebar);

  // Close sidebar on nav click (mobile)
  sidebar.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
      if (window.innerWidth <= 768) closeSidebar();
    });
  });
});
