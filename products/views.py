from django.shortcuts import render, get_object_or_404
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
    return render(
        request,
        'products/products.html',
        context
    )


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    # Get product with given id or return 404 error
    product = get_object_or_404(Product, pk=product_id)

    # Context to pass to the template
    context = {
        'product': product,
        'MEDIA_URL': settings.MEDIA_URL
    }

    # Render the product_detail template with the product
    return render(
        request,
        'products/product_detail.html',
        context
    )