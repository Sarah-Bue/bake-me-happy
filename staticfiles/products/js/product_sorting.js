/* JSHint directive */
/* jshint esversion: 6, browser: true, jquery: true */

// The sorting functionality JS has been adapted from Code Institute's "Boutique Ado" project 

/**
 * Product Sorting Functionality 
 * Handles the sorting of products based on user selection.
 */
$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);
    var selectedVal = selector.val();

    // If a sorting option is selected (not reset)
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        // Update URL search parameters with sort field and direction
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        // If reset option is selected
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});