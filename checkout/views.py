from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from decimal import Decimal

from .forms import OrderForm
from .models import Order, OrderLineItem
from basket.contexts import basket_contents
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import json
import stripe


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
        username = (request.user.username
                    if request.user.is_authenticated else 'AnonymousUser')
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': username,
        })
        return HttpResponse(status=200)

    # Error Handling
    except Exception as e:
        messages.error(request,
                       "Sorry, your payment cannot be processed right now. "
                       "Please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handle the checkout process for customer orders.
    Validates basket contents and displays order form.
    """

    # Initialize Stripe Keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Initialize delivery_method with a default value
    delivery_method = 'delivery'

    # Handle POST request
    if request.method == 'POST':
        basket = request.session.get('basket', {})

        # Get delivery method from POST data
        delivery_method = request.POST.get('delivery_method', 'delivery')

        # Store delivery method in session for basket_contents to use
        request.session['delivery_method'] = delivery_method

        # Set default country before collecting form data
        form_data = request.POST.copy()
        form_data['country'] = 'IE'

        # Collect form data
        form_data = {
            'full_name': form_data['full_name'],
            'email': form_data['email'],
            'phone_number': form_data['phone_number'],
            'country': form_data['country'],
            'postcode': form_data['postcode'],
            'town_or_city': form_data['town_or_city'],
            'street_address1': form_data['street_address1'],
            'street_address2': form_data['street_address2'],
            'county': form_data['county'],
            'delivery_method': delivery_method,
        }

        # Create and validate order form
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Double-check country is Ireland (security measure)
            if form_data['country'] != 'IE':
                messages.error(request,
                               "Sorry, we currently only ship to Ireland.")
                return redirect(reverse('checkout'))

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
            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )

        # Form validation error handling
        else:
            messages.error(request,
                           "There was an error with your form. "
                           "Please double check your information.")

    # Handle GET request
    else:
        basket = request.session.get('basket', {})

        # Reset delivery method to 'delivery' on checkout page load
        request.session['delivery_method'] = 'delivery'

        # Redirect if basket is empty
        if not basket:
            messages.error(request, "Your basket is empty.")
            return redirect(reverse('products'))

        # Set or get delivery method from session
        delivery_method = request.session.get('delivery_method', 'delivery')
        request.session['delivery_method'] = delivery_method

        # Initialize form with delivery method
        initial_data = {'delivery_method': delivery_method}

        # If user is authenticated, add profile data to initial_data
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                initial_data.update({
                    'full_name': profile.default_full_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'postcode': profile.default_postcode,
                    'county': profile.default_county,
                    'country': 'IE',  # Default Ireland
                })
            except UserProfile.DoesNotExist:
                pass

        order_form = OrderForm(initial=initial_data)

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

        # Check if stripe_public_key is available
        if not stripe_public_key:
            messages.warning(request, "Stripe public key is missing.")

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

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_postcode': order.postcode,
                'default_county': order.county,
                'default_country': order.country,

            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Success Message
    messages.success(request,
                     'We have received your order. '
                     f'A confirmation email will be sent to {order.email}.')

    # Semd email confirmation
    cust_email = order.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order}
    )
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order,
         'email': cust_email,
         'contact_email': settings.DEFAULT_FROM_EMAIL}
    )
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )

    # Clear basket from session
    if 'basket' in request.session:
        del request.session['basket']

    # Clear delivery_method from session
    if 'delivery_method' in request.session:
        del request.session['delivery_method']

    # Redirect to success page
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    # Render the checkout success template
    return render(request, template, context)


@require_POST
def update_delivery_method(request):
    """
    Update delivery method and recalculate costs.
    """

    delivery_method = request.POST.get('delivery_method')

    # Store delivery method in session
    request.session['delivery_method'] = delivery_method

    # Get current basket from session
    basket = request.session.get('basket', {})

    # Calculate order total from basket
    total = Decimal('0.00')
    for item_id, quantity in basket.items():
        try:
            product = get_object_or_404(Product, pk=item_id)
            total += quantity * product.price
        except Product.DoesNotExist:
            pass

    # Calculate delivery cost based on method
    if delivery_method == 'delivery':
        if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery_cost = Decimal(settings.STANDARD_DELIVERY)
        else:
            delivery_cost = Decimal('0.00')
    else:  # pickup
        delivery_cost = Decimal('0.00')

    grand_total = total + delivery_cost

    return JsonResponse({
        'delivery_cost': f'{delivery_cost:.2f}',
        'grand_total': f'{grand_total:.2f}',
    })
