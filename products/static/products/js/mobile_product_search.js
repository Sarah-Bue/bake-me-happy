document.addEventListener('DOMContentLoaded', function() {
    const searchToggle = document.getElementById('mobile-search-toggle');
    const searchContainer = document.getElementById('mobile-search-container');
    
    if (searchToggle && searchContainer) {
        searchToggle.addEventListener('click', function(e) {
            e.preventDefault();
            if (searchContainer.style.display === 'none') {
                searchContainer.style.display = 'block';
                document.getElementById('mobile-product-search').focus();
            } else {
                searchContainer.style.display = 'none';
            }
        });
    }
});
