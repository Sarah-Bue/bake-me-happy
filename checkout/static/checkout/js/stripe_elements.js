/*
    Core logic/payment flow has been adapted from:
    https://stripe.com/docs/payments/accept-a-payment

    CSS has been adapted from: 
    https://stripe.com/docs/stripe-js
*/

// Get Stripe public key & client_secret from the template - removes quotes from beginning and end
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Initialize Stripe.js with public key
var stripe = Stripe(stripePublicKey);
// Create an instance of Elements
var elements = stripe.elements();

// Style configuration for the card element
var style = {
    base: {
        // Default styling for the card element
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        // Styling for the placeholder text
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        // Styling for when the card details are invalid
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create a card Element and mount it to the card-element div
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Add loading overlay toggle function
function toggleLoadingOverlay() {
    const overlay = document.getElementById('loading-overlay');
    overlay.classList.toggle('d-none');
}

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // Prevent default form submission
    ev.preventDefault();
    // Disable card element and submit button to prevent multiple submissions
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // Display loading overlay  
    toggleLoadingOverlay();
    // Confirm payment
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        // Error handling
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // Re-enable card element and submit button
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            // Hide loading overlay
            toggleLoadingOverlay();
        // Payment success    
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
                // Hide loading overlay
                toggleLoadingOverlay();
            }
        }
    });
});