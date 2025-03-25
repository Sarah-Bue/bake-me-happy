/* JSHint directive */
/* jshint esversion: 6, browser: true, jquery: true */

/**
 * Quantity Dropdown Handler
 * This function manages the behavior of product quantity dropdowns, specifically:
 * 1. Shows warning messages when quantity of 5 is selected
 * 2. Maintains selected quantity after form submission
 */
function handleQtyMessage(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    if (currentValue === 5) {
        $(`#qty_message_${itemId}`).show();
    } else {
        $(`#qty_message_${itemId}`).hide();
    }
}

// Initialize quantity dropdowns on page load
$(document).ready(function() {
    // Check for all quantity inputs on page load
    var allQtyInputs = $('.form-select');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        
        // Get the current quantity from data attribute (will be set by the server)
        var currentQty = $(allQtyInputs[i]).data('current_qty');
        if (currentQty) {
            // Set the dropdown to the correct value
            $(`#id_qty_${itemId}`).val(currentQty);
        }
        
        handleQtyMessage(itemId);
    }

    // Show/hide error message when dropdown selection changes
    $('.form-select').change(function() {
        var selectedValue = $(this).val();
        var itemId = $(this).data('item_id');
        var errorMessage = $(`#qty_message_${itemId}`);
        
        if (selectedValue === '5') {
            errorMessage.show();
        } else {
            errorMessage.hide();
        }
    });
});