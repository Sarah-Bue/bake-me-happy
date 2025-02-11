from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from  .models import Product, Category


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

        # Get all products
    products = Product.objects.all()
    query = None
    categories = None

    # Search Handling
    if request.GET:

        # Category Handling
        if 'category' in request.GET:
            # Get the category from the request
            categories = request.GET['category'].split(',')
            # Filter products by category
            products = products.filter(category__name__in=categories)
            # Get category names for display
            categories = Category.objects.filter(name__in=categories)



        # Keyword Search Handling
        if 'q' in request.GET:
            # Get the query from the request
            query = request.GET['q']
            # If query is empty, return error message
            if not query:
                messages.error(request, "Please enter a search criteria.")
                # Redirect to products page
                return redirect(reverse('products'))

            # If query is not empty, search for products with matching:
            # - English name OR
            # - German name OR
            # - Description
            queries = (
                Q(name__icontains=query) |
                Q(german_name__icontains=query) |
                Q(description__icontains=query)
            )
            products = products.filter(queries)

    # Context to pass to the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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