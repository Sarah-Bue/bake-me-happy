document.addEventListener('DOMContentLoaded', function() {
    // Get Django template values
    const updateUrl = document.getElementById('id_update_url').textContent.slice(1, -1);
    const csrfToken = document.getElementById('csrf-data').getAttribute('data-csrf');

    // Get all delivery address fields
    const deliveryFields = document.querySelectorAll('#id_street_address1, #id_street_address2, #id_town_or_city, #id_county, #id_postcode, #id_country');
    
    // Get elements for payment method toggle
    const paymentMethodRadios = document.querySelectorAll('input[name="payment_method"]');
    const cardPaymentSection = document.getElementById('card-payment-section');
    const cashPaymentInfo = document.getElementById('cash-payment-info');
    const cardPaymentInfo = document.getElementById('card-payment-info');
    const submitButton = document.getElementById('submit-button');
    
    // Function to toggle visibility of delivery fields
    function toggleDeliveryFields() {
        const isDelivery = document.querySelector('input[name="delivery_method"]:checked').value === 'delivery';
        const shippingNotification = document.getElementById('shipping-notification');
        
        // Toggle each field
        deliveryFields.forEach(field => {
            const formGroup = field.closest('.form-group');
            if (formGroup) {
                formGroup.style.display = isDelivery ? 'block' : 'none';
                // Only make fields required if delivery is selected
                if (field.id !== 'id_street_address2' && field.id !== 'id_postcode') {
                    field.required = isDelivery;
                }
            }
        });
        
        // Toggle shipping notification
        if (shippingNotification) {
            shippingNotification.style.display = isDelivery ? 'block' : 'none';
        }
        
        // Update legend text
        const deliveryLegend = document.querySelector('legend[aria-label="Delivery details section"]');
        if (deliveryLegend) {
            deliveryLegend.textContent = isDelivery ? 'Delivery Details' : 'Billing Details';
        }
        
        // Update payment methods based on delivery method
        togglePaymentMethods();
    }
    
    // Function to toggle payment method options based on delivery method
    function togglePaymentMethods() {
        const isPickup = document.querySelector('input[name="delivery_method"]:checked').value === 'pickup';
        const paymentMethodGroup = document.getElementById('payment-method-group');
        
        // Show/hide payment method options
        paymentMethodGroup.style.display = isPickup ? 'block' : 'none';
        
        // If delivery is selected, force card payment
        if (!isPickup) {
            // Find the card payment radio and select it
            const cardRadio = Array.from(paymentMethodRadios).find(radio => radio.value === 'card');
            if (cardRadio) {
                cardRadio.checked = true;
            }
            // Show card payment section, hide cash info
            cardPaymentSection.classList.remove('d-none');
            cashPaymentInfo.classList.add('d-none');
            // Show card payment info
            cardPaymentInfo.classList.remove('d-none');
        } else {
            // Check which payment method is selected for pickup
            updatePaymentSections();
        }
        
        // Update order total after changing delivery method
        updateOrderTotal();
    }
    
    // Function to update payment sections based on selected payment method
    function updatePaymentSections() {
        const selectedPaymentMethod = document.querySelector('input[name="payment_method"]:checked').value;
        
        if (selectedPaymentMethod === 'cash') {
            // Hide card payment section, show cash info
            cardPaymentSection.classList.add('d-none');
            cashPaymentInfo.classList.remove('d-none');
            // Hide card payment info text
            cardPaymentInfo.classList.add('d-none');
            // Update button text
            submitButton.innerHTML = '<i class="fas fa-check me-2"></i>Complete Order';
        } else {
            // Show card payment section, hide cash info
            cardPaymentSection.classList.remove('d-none');
            cashPaymentInfo.classList.add('d-none');
            // Show card payment info text
            cardPaymentInfo.classList.remove('d-none');
            // Reset button text
            submitButton.innerHTML = '<i class="fas fa-lock me-2"></i>Complete Order';
        }
    }
    
    function updateOrderTotal() {
        const deliveryMethod = document.querySelector('input[name="delivery_method"]:checked').value;
        
        // Send AJAX request to update delivery method
        fetch(updateUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: `delivery_method=${deliveryMethod}`
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Update delivery cost
            const deliveryCells = document.querySelectorAll('td.text-end');
            let deliveryCostElement = null;
            
            // Find the cell that contains "Delivery:"
            for (let i = 0; i < deliveryCells.length; i++) {
                if (deliveryCells[i].previousElementSibling &&
                    deliveryCells[i].previousElementSibling.textContent.includes('Delivery:')) {
                    deliveryCostElement = deliveryCells[i];
                    break;
                }
            }
            
            if (deliveryCostElement) {
                deliveryCostElement.textContent = `€${data.delivery_cost}`;
            }
            
            // Update grand total
            const grandTotalCells = document.querySelectorAll('td.text-end strong');
            let grandTotalElement = null;
            
            // Find the cell that contains the grand total
            for (let i = 0; i < grandTotalCells.length; i++) {
                if (grandTotalCells[i].parentElement.previousElementSibling &&
                    grandTotalCells[i].parentElement.previousElementSibling.textContent.includes('Grand Total:')) {
                    grandTotalElement = grandTotalCells[i];
                    break;
                }
            }
            
            if (grandTotalElement) {
                grandTotalElement.textContent = `€${data.grand_total}`;
            }
            
            // Update payment warning text
            const paymentWarning = document.querySelector('.text-danger strong');
            if (paymentWarning) {
                paymentWarning.textContent = `€${data.grand_total}`;
            }
        })
        .catch(error => {
            console.error('Error updating delivery method:', error);
        });
    }
    
    // Add event listeners to delivery method radios
    const deliveryRadios = document.querySelectorAll('input[name="delivery_method"]');
    deliveryRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            toggleDeliveryFields();
        });
    });
    
    // Add event listeners to payment method radios
    paymentMethodRadios.forEach(radio => {
        radio.addEventListener('change', updatePaymentSections);
    });
    
    // Run on page load
    toggleDeliveryFields();
    updateOrderTotal();
});
