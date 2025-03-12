from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    A view to return the profile page,
    prepopulated user information, and order history.
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    # Make a copy of POST data to ensure 'country' is included
    post_data = request.POST.copy()
    # Ensure country is always set to Ireland
    post_data['default_country'] = 'IE'

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def delete_profile(request):
    """
    Delete the user's profile and account.
    """

    if request.method == 'POST':
        user = request.user
        # Logout the user before deletion
        from django.contrib.auth import logout
        logout(request)
        # Delete the user which will cascade to profile
        user.delete()
        messages.success(request,
                         'Your profile has been deleted successfully.')
        return redirect('home')

    # If GET request, show confirmation template
    template = 'profiles/delete_confirmation.html'
    return render(request, template)


@login_required
def order_history(request, order_number):
    """
    A view to return the order history page of a specific order,
    displaying the order details.
    """

    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
            f'This is a past confirmation for order number {order_number}. '
            'A confirmation email was sent to you by email.'
        ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def orders(request):
    """
    A view to return the orders page,
    displaying all orders associated with the user.
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/orders.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)
