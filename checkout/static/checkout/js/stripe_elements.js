/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Only initialize Stripe when card payment is selected
function initializeStripe() {
    const paymentMethod = document.querySelector('input[name="payment_method"]:checked')?.value;
    const paymentMethodGroupVisible = document.getElementById('payment-method-group').offsetParent !== null;
    
    if (paymentMethod === 'card' || !paymentMethodGroupVisible) {
        // Get Stripe public key and client secret
        const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
        const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);
        
        // Initialize Stripe
        const stripe = Stripe(stripePublicKey);
        const elements = stripe.elements();
        
        // Create card element with styling
        const style = {
            base: {
                color: '#000',
                fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
                fontSmoothing: 'antialiased',
                fontSize: '16px',
                '::placeholder': {
                    color: '#aab7c4'
                }
            },
            invalid: {
                color: '#dc3545',
                iconColor: '#dc3545'
            }
        };
        
        const card = elements.create('card', {style: style});
        card.mount('#card-element');
        
        // Handle realtime validation errors on the card element
        card.addEventListener('change', function (event) {
            const errorDiv = document.getElementById('card-errors');
            if (event.error) {
                const html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${event.error.message}</span>
                `;
                errorDiv.innerHTML = html;
            } else {
                errorDiv.textContent = '';
            }
        });
        
        // Handle form submit
        const form = document.getElementById('payment-form');
        form.addEventListener('submit', function(ev) {
            ev.preventDefault();
            
            // Check if payment method is cash
            const paymentMethod = document.querySelector('input[name="payment_method"]:checked')?.value;
            
            if (paymentMethod === 'cash') {
                // For cash payments, just submit the form without Stripe processing
                form.submit();
                return;
            }
            
            // For card payments, process with Stripe
            card.update({ 'disabled': true });
            document.getElementById('submit-button').disabled = true;
            
            // Show loading overlay
            document.getElementById('loading-overlay').classList.remove('d-none');
            
            // Get billing details
            const saveInfo = Boolean(document.getElementById('id-save-info')?.checked);
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            
            // Create an object to pass to the view
            const postData = {
                'csrfmiddlewaretoken': csrfToken,
                'client_secret': clientSecret,
                'save_info': saveInfo,
            };
            
            // Post to the cache_checkout_data view
            const url = '/checkout/cache_checkout_data/';
            
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams(postData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Confirm card payment
                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: form.full_name.value,
                            phone: form.phone_number.value,
                            email: form.email.value,
                            address:{
                                line1: form.street_address1.value,
                                line2: form.street_address2.value,
                                city: form.town_or_city.value,
                                country: form.country.value,
                                state: form.county.value,
                            }
                        }
                    },
                    shipping: {
                        name: form.full_name.value,
                        phone: form.phone_number.value,
                        address: {
                            line1: form.street_address1.value,
                            line2: form.street_address2.value,
                            city: form.town_or_city.value,
                            country: form.country.value,
                            postal_code: form.postcode.value,
                            state: form.county.value,
                        }
                    },
                }).then(function(result) {
                    if (result.error) {
                        // Show error to customer
                        const errorDiv = document.getElementById('card-errors');
                        const html = `
                            <span class="icon" role="alert">
                                <i class="fas fa-times"></i>
                            </span>
                            <span>${result.error.message}</span>
                        `;
                        errorDiv.innerHTML = html;
                        
                        // Hide loading overlay
                        document.getElementById('loading-overlay').classList.add('d-none');
                        
                        // Re-enable card element and submit button
                        card.update({ 'disabled': false });
                        document.getElementById('submit-button').disabled = false;
                    } else {
                        // Payment succeeded, submit the form
                        if (result.paymentIntent.status === 'succeeded') {
                            form.submit();
                        }
                    }
                });
            })
            .catch(error => {
                // Hide loading overlay and re-enable form
                document.getElementById('loading-overlay').classList.add('d-none');
                card.update({ 'disabled': false });
                document.getElementById('submit-button').disabled = false;
                console.error('Error:', error);
            });
        });
    }
}

// Call this on page load and when payment method changes
document.addEventListener('DOMContentLoaded', function() {
    initializeStripe();
    const paymentMethodRadios = document.querySelectorAll('input[name="payment_method"]');
    paymentMethodRadios.forEach(radio => {
        radio.addEventListener('change', initializeStripe);
    });
    const deliveryRadios = document.querySelectorAll('input[name="delivery_method"]');
    deliveryRadios.forEach(radio => {
        radio.addEventListener('change', initializeStripe);
    });
});