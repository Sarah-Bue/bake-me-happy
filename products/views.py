
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, F
from django.db.models.functions import Lower
from .models import Product, Category, Occasion

def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """
    
    # Get all products initially
    products = Product.objects.all()
    
    # Initialize variables
    query = None
    categories = None
    occasions = None
    sort = None
    direction = None

    if request.GET:
        # Handle sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            
            # Handle different sort cases
            if sortkey == 'name':
                # Case-insensitive name sorting
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                # Sort by category
                sortkey = 'category__name'
            elif sortkey == 'occasion':
                # Sort by occasion
                sortkey = 'occasion__name'
            elif sortkey == 'rating':
                # Sort by rating
                sortkey = '-rating' if direction == 'desc' else 'rating'
                products = products.order_by(F('rating').desc(nulls_last=True))
            
            # Apply sort direction
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            
            # Apply sorting
            # Note: Exclude  rating sorting as handled above
            if sortkey != 'rating':
                products = products.order_by(sortkey)

        # Filter by category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Filter by occasion
        if 'occasion' in request.GET:
            occasions = request.GET['occasion'].split(',')
            products = products.filter(occasion__name__in=occasions)
            occasions = Occasion.objects.filter(name__in=occasions)

        # Search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # Search across name, German name, and description
            queries = (
                Q(name__icontains=query) |
                Q(german_name__icontains=query) |
                Q(description__icontains=query)
            )
            products = products.filter(queries)

    # Create current sorting string for context
    current_sorting = f'{sort}_{direction}' if sort and direction else ''

    # Prepare template context
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_occasions': occasions,
        'current_sorting': current_sorting,
    }

    # Render products page
    return render(
        request,
        'products/products.html',
        context
    )


def product_detail(request, product_id):
    """
    Display individual product details.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    # Render product detail page
    return render(
        request,
        'products/product_detail.html',
        context
    )