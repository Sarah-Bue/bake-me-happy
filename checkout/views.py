from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe


def checkout(request):
    """
    Handle the checkout process for customer orders.
    Validates basket contents and displays order form.
    """
    # Initialize Stripe
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    # Get basket from session
    basket = request.session.get('basket', {})

    # Redirect if basket is empty
    if not basket:
        messages.error(request, "Your basket is empty.")
        return redirect(reverse('products'))
    
    # Calculate total cost of basket
    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    # Create a Stripe payment intent
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Initialize the order form
    order_form = OrderForm()

    # Check if stripe_public_key is available
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    # Prepare template context
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # Render the checkout template
    return render(request, template, context)