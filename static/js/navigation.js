/**
 * Navigation Active State Handler
 * Script to automatically highlight the current page in navigation links across the website.
 */
document.addEventListener("DOMContentLoaded", function() {
    // Get current URL path
    const path = window.location.pathname;
    
    // Find all navbar links in both main and profile navigation
    const allNavLinks = document.querySelectorAll('.navbar-nav .nav-link, .profile-nav .nav-link');
    
    // Loop through links and set active class
    allNavLinks.forEach(link => {
        // Get href attribute
        const href = link.getAttribute('href');
        
        // Reset active state
        link.classList.remove('active');
        link.removeAttribute('aria-current');
        
        // Set active state for current page
        if (path === href) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        }
    });
});