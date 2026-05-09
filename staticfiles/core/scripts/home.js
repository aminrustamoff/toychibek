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

    // Counter animation
    const statBoxes = document.querySelectorAll(".stat-box h3");
    let hasAnimated = false;

    const animateCounter = (element, target) => {
        let current = 0;
        const duration = 2000; // 2 seconds
        const startTime = Date.now();
        const cleanTarget = parseInt(target.replace(/[^0-9]/g, ''));

        const easeOutQuad = (t) => 1 - (1 - t) * (1 - t);

        const updateCounter = () => {
            const elapsed = Date.now() - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easedProgress = easeOutQuad(progress);
            
            current = Math.floor(cleanTarget * easedProgress);
            element.textContent = current + '+';

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target;
            }
        };

        updateCounter();
    };

    const statsSection = document.querySelector(".stats");
    if (statsSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !hasAnimated) {
                    hasAnimated = true;
                    statBoxes.forEach(box => {
                        const originalText = box.textContent;
                        animateCounter(box, originalText);
                    });
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        observer.observe(statsSection);
    }
});