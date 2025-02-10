from django.shortcuts import render
from django.conf import settings
from  .models import Product


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """
    # Get all products
    products = Product.objects.all()

    # Context to pass to the template
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL
    }

    # Render the products template with the products
    return render(request, 'products/products.html', context)