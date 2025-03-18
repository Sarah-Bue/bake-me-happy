document.addEventListener('DOMContentLoaded', function() {
    const starContainer = document.querySelector('.star-rating-container');
    const starOptions = document.querySelectorAll('.star-option input[type="radio"]');

    // Add change event listeners to radio buttons
    starOptions.forEach(radio => {
        radio.addEventListener('change', function() {
            const value = this.value;
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