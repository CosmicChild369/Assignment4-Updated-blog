document.addEventListener('DOMContentLoaded', function() {
    // Initialize Particles.js
    particlesJS.load('particles-js', '/static/js/particles.json', function() {
        console.log('Particles.js loaded');
    });

    // GSAP Animations
    gsap.from('.navbar', { duration: 1, y: '-100%', opacity: 0, ease: 'bounce' });
    gsap.from('.container', { duration: 1, opacity: 0, stagger: 0.5 });

    // Add a fun background animation with GSAP
    gsap.to('body', { backgroundPosition: '200% center', duration: 20, ease: 'linear', repeat: -1 });
});
