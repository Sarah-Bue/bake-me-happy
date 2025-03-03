from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order

def index(request):
    """
    A view to return the index page.
    """

    return render(request, 'home/index.html')


@login_required
def store_management(request):
    """
    A view to return the store management dashboard.
    Only accessible by admins.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect('home')
  
    # Count various objects in the system
    product_count = Product.objects.count()
    subscriber_count = Subscriber.objects.count()
    review_count = Review.objects.count()
    orders_count = Order.objects.count()

    context = {
        'product_count': product_count,
        'subscriber_count': subscriber_count,
        'review_count': review_count,
        'orders_count': orders_count,
    }

    return render(request, 'home/store_management.html', context)


@login_required
def manage_orders(request):
    """
    A view to manage customer orders
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can access this page.')
        return redirect('home')


    orders = Order.objects.all().order_by('-date')

    context = {
        'orders': orders,
    }

    return render(request, 'home/manage_orders.html', context)

