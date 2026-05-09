const purchaseBtn = document.querySelector('.purchase-btn');
const contactBtn = document.querySelector('.contact-btn');

if (purchaseBtn && purchaseBtn.tagName.toLowerCase() === 'button') {
    purchaseBtn.addEventListener('click', () => {
        alert('Purchase request sent!');
    });
}

if (contactBtn) {
    contactBtn.addEventListener('click', () => {
        window.location.href = '/contacts/';
    });
}