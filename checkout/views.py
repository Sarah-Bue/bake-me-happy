from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    Handle the checkout process for customer orders.
    Validates basket contents and displays order form.
    """
    # Get basket from session
    basket = request.session.get('basket', {})

    # Redirect if basket is empty
    if not basket:
        messages.error(request, "Your basket is empty.")
        return redirect(reverse('products'))

    # Initialize the order form
    order_form = OrderForm()

    # Prepare template context
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)