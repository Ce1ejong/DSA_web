document.addEventListener('DOMContentLoaded', () => {
    console.log('DS Navigator Website Loaded Successfully! Interactive features enabled.');

    // Simple scroll animation for cards using a basic class (to simulate animation library)
    const cards = document.querySelectorAll('.algorithm-card, .accordion-item');
    
    const fadeInObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add a CSS class to trigger a smooth fade-in effect defined in style.css
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1, // Trigger when 10% of the item is visible
        rootMargin: '0px 0px -50px 0px' // Start fade-in slightly early
    });

    cards.forEach(card => {
        // Initial setup for the fade-in effect
        card.style.opacity = 0;
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        
        fadeInObserver.observe(card);
    });
});