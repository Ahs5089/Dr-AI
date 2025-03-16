document.addEventListener("DOMContentLoaded", () => {
    // --------------------- Page 1 ------------------ //
    const menuToggle = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector(".nav-menu");

    if (menuToggle && navMenu) {
        menuToggle.addEventListener("click", () => {
            navMenu.classList.toggle("active");
        });
    }

    // --------------------- Page 2 ------------------ //
    let currentSlide = 0;
    const slides = document.querySelectorAll(".slide");
    if (slides.length > 0) {
        function showSlide(index) {
            slides.forEach((slide, i) => {
                slide.style.display = i === index ? "block" : "none";
            });
        }

        showSlide(currentSlide);

        const nextBtn = document.querySelector(".next");
        const prevBtn = document.querySelector(".prev");

        if (nextBtn) {
            nextBtn.addEventListener("click", () => {
                currentSlide = (currentSlide + 1) % slides.length;
                showSlide(currentSlide);
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener("click", () => {
                currentSlide = (currentSlide - 1 + slides.length) % slides.length;
                showSlide(currentSlide);
            });
        }
    }

    // --------------------- Page 11 ------------------ //
    const newsletterForm = document.querySelector(".newsletter");
    if (newsletterForm) {
        const emailInput = newsletterForm.querySelector("input[type='email']");
        if (emailInput) {
            newsletterForm.querySelector("button").addEventListener("click", (e) => {
                e.preventDefault();
                const emailValue = emailInput.value.trim();

                if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailValue)) {
                    alert("Please enter a valid email address.");
                } else {
                    alert("Thank you for subscribing!");
                }
            });
        }
    }

    // --------------------- For All Pages ------------------ //
    
    const backToTop = document.createElement("button");
    backToTop.textContent = "↑";
    backToTop.className = "back-to-top";
    document.body.appendChild(backToTop);

    backToTop.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    window.addEventListener("scroll", () => {
        backToTop.style.display = window.scrollY > 300 ? "block" : "none";
    });

    
    const links = document.querySelectorAll("a[href^='#']");
    links.forEach((link) => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute("href"));
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});

