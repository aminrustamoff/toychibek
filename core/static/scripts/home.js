document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".hero-slide");
    let currentIndex = 0;

    if (slides.length > 0) {
        setInterval(() => {
            slides[currentIndex].classList.remove("active");

            currentIndex++;
            if (currentIndex >= slides.length) {
                currentIndex = 0;
            }

            slides[currentIndex].classList.add("active");
        }, 5000);
    }
});