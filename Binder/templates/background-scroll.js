document.addEventListener('DOMContentLoaded', function() {
    const bgElement = document.querySelector('.background');
    window.addEventListener('scroll', function() {
        const scrollPosition = window.scrollY;
        bgElement.style.backgroundPositionY = `${scrollPosition * 0.5}px`;
    });
});
