/* JSHint directive */
/* jshint esversion: 6, browser: true, jquery: true */

/**
 * The star rating has been adapted from CSS-Tricks' "Star Rating Widget" tutorial https://css-tricks.com/star-ratings/
 *
 * This script is responsible for handling the star rating functionality, providing a visual representation of the user's rating.
*/
document.addEventListener('DOMContentLoaded', function() {
    const starContainer = document.querySelector('.star-rating-container');
    const starOptions = document.querySelectorAll('.star-option input[type="radio"]');

    // Add change event listeners to radio buttons
    starOptions.forEach(radio => {
        radio.addEventListener('change', function() {
            const options = Array.from(starContainer.querySelectorAll('.star-option'));
            const index = options.findIndex(opt => opt.contains(this));

            options.forEach((opt, i) => {
                const label = opt.querySelector('.star-label');
                label.style.color = i <= index ? '#ffc107' : '#ddd';
            });
        });
    });

    // Initial state - show any pre-selected rating
    const checked = starContainer.querySelector('input[type="radio"]:checked');
    if (checked) {
        checked.dispatchEvent(new Event('change'));
    }
});