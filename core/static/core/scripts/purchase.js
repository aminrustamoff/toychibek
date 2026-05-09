const form = document.querySelector('.contact-form');
const submitBtn = document.querySelector('.contact-btn');

form.addEventListener('submit', () => {

    submitBtn.innerText = 'Yuborilmoqda...';

    submitBtn.disabled = true;

});