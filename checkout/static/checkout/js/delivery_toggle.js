document.addEventListener('DOMContentLoaded', function() {
    const deliveryMethodSelect = document.getElementById('delivery-method');
    const deliveryFields = document.getElementById('delivery-fields');

    // Function to update delivery method in session
    function updateDeliveryMethod(method) {
        fetch('/checkout/update-delivery-method/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: JSON.stringify({
                'delivery_method': method
            })
        })
        .then(response => response.json())
        .then(data => {
            // Update delivery cost and grand total displays
            document.querySelector('[data-delivery]').textContent = `€${data.delivery}`;
            document.querySelector('[data-grand-total]').textContent = `€${data.grand_total}`;
        });
    }

    deliveryMethodSelect.addEventListener('change', function() {
        if (this.value === 'pickup') {
            deliveryFields.style.display = 'none';
        } else {
            deliveryFields.style.display = 'block';
        }
        updateDeliveryMethod(this.value);
    });
});
