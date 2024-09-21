// Function to open a new page (replace 'newpage.html' with the actual URL)
function openNewPage() {
    window.location.href = 'newpage.html'; // Replace with your actual URL or path
}

// Smooth animation on page load
window.onload = () => {
    setTimeout(() => {
        document.querySelectorAll('.animate-fade-in').forEach(el => {
            el.style.opacity = 1;
        });
        document.querySelectorAll('.animate-slide-up').forEach(el => {
            el.style.transform = 'translateY(0)';
            el.style.opacity = 1;
        });
    }, 500);
};
