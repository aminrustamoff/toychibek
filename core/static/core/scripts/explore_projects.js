const purchaseButtons = document.querySelectorAll('.purchase-btn');

purchaseButtons.forEach(button => {
    if (button.tagName.toLowerCase() !== 'button') {
        return;
    }

    button.addEventListener('click', () => {
        const projectName = button.dataset.project;
        alert(`You selected: ${projectName}`);
    });
});