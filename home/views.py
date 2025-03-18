from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from about.models import Baker, FAQ
from checkout.models import Order
from contact.models import Contact
from newsletter.models import Subscriber
from products.models import Product
from reviews.models import Review


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
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    # Count various objects in the system
    product_count = Product.objects.count()
    subscriber_count = Subscriber.objects.count()
    review_count = Review.objects.count()
    orders_count = Order.objects.count()
    contact_count = Contact.objects.count()
    baker_count = Baker.objects.count()

    context = {
        'product_count': product_count,
        'subscriber_count': subscriber_count,
        'review_count': review_count,
        'orders_count': orders_count,
        'contact_count': contact_count,
        'baker_count': baker_count,
    }

    return render(request, 'home/store_management.html', context)


@login_required
def manage_orders(request):
    """
    A view to manage customer orders
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    orders = Order.objects.all().order_by('-date')

    context = {
        'orders': orders,
    }

    return render(request, 'home/manage_orders.html', context)


@login_required
def manage_subscribers(request):
    """
    A view to manage newsletter subscribers.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    # Get all subscribers ordered by subscription date (newest first)
    from newsletter.models import Subscriber
    subscribers = Subscriber.objects.all().order_by('-date_subscribed')

    context = {
        'subscribers': subscribers,
    }

    return render(request, 'home/manage_subscribers.html', context)


@login_required
def manage_reviews(request):
    """
    A view to manage product reviews.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    # Get all reviews ordered by date (newest first)
    reviews = Review.objects.all().order_by('-date_added')

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/manage_reviews.html', context)


@login_required
def manage_contacts(request):
    """
    A view to manage contact messages.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    # Get all contacts ordered by date (newest first)
    contacts = Contact.objects.all().order_by('-date_sent')

    context = {
        'contacts': contacts,
    }

    return render(request, 'home/manage_contacts.html', context)


@login_required
def manage_bakers(request):
    """
    A view to manage bakery team members.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    # Get all bakers ordered by their display order
    bakers = Baker.objects.all().order_by('order', 'name')

    context = {
        'bakers': bakers,
    }

    return render(request, 'home/manage_bakers.html', context)


@login_required
def manage_faq(request):
    """
    A view to manage frequently asked questions.
    """
    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    # Get all FAQ ordered by their display order
    faq = FAQ.objects.all().order_by('order')

    context = {
        'faq': faq,
    }

    return render(request, 'home/manage_faq.html', context)


@login_required
def manage_products(request):
    """
    A view to manage all products.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    # Get all products ordered by name
    products = Product.objects.all().order_by('name')

    context = {
        'products': products,
    }

    return render(request, 'home/manage_products.html', context)


@login_required
def view_contact(request, contact_id):
    """
    A view to display full contact details.
    """
    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners can access this page.')
        return redirect('home')

    # Get contact object
    contact = get_object_or_404(Contact, pk=contact_id)

    context = {
        'contact': contact,
    }

    return render(request, 'home/view_contact.html', context)
