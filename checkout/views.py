from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order,OrderLineItem
from products.models import Product
from basket.contexts import basket_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data for Stripe.
    """
    try:
        # Get payment intent ID from client secret
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Set Stripe API key
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify payment intent to include basket and save_info data
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
        })
        return HttpResponse(status=200)
    
    # Error Handling
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    """
    Handle the checkout process for customer orders.
    Validates basket contents and displays order form.
    """
    # Initialize Stripe Keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    # Handle POST request
    if request.method == 'POST':
        # Get basket from session
        basket = request.session.get('basket', {})

        # Collect form data
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # Create and validate order form
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Save order
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()

            for item_id, quantity in basket.items():
                try:
                    # Get product
                    product = Product.objects.get(id=item_id)
                    # Create order line item
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    # Save order line item
                    order_line_item.save()

                # Handle product not found
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found. "
                        "Please contact us for assistance.")
                    )
                    # Delete order and redirect to basket
                    order.delete()
                    return redirect(reverse('view_basket'))

            # Save user info to session    
            request.session['save_info'] = 'save-info' in request.POST

            # Redirect to checkout success
            return redirect(reverse('checkout_success', args=[order.order_number]))
        
        # Form validation error handling
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    # Handle GET request
    else:
        basket = request.session.get('basket', {})

        # Redirect if basket is empty
        if not basket:
            messages.error(request, "Your basket is empty.")
            return redirect(reverse('products'))
        
        # Calculate basket total for Stripe
        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)

        # Set up Stripe intent
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

        # Prepare template & context
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        # Render the checkout template
        return render(request, template, context)
    

def checkout_success(request, order_number):
    """
    Handle successful checkout and display order details.
    """

    # Get user info
    save_info = request.session.get('save_info')
    # Get order
    order = get_object_or_404(Order, order_number=order_number)
    # Message
    messages.success(request, f'We have received your order. \
                     A confirmation email will be sent to {order.email}.'
                    )
    # Clear basket
    if 'basket' in request.session:
        del request.session['basket']
    # Redirect to success page
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    # Render the checkout success template
    return render(request, template, context)