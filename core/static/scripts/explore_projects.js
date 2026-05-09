const purchaseButtons = document.querySelectorAll('.purchase-btn');

purchaseButtons.forEach(button => {

    button.addEventListener('click', () => {

        const projectName = button.dataset.project;

        alert(`You selected: ${projectName}`);

    });

});