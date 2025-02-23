
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, F
from django.db.models.functions import Lower
from .models import Product, Category, Occasion
from favorites.models import Favorite
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """
    
    # Get all products
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
                # sortkey = '-rating' if direction == 'desc' else 'rating'
                # products = products.order_by(F('rating').desc(nulls_last=True))

                if direction == 'desc':
                    products = products.order_by(F('rating').desc(nulls_last=True))
                else:
                    products = products.order_by(F('rating').asc(nulls_last=True))
            
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
                messages.error(request, "Pleae enter search criteria and try again.")
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

    # Get favorite product IDs for authenticated user
    favorite_products = []
    if request.user.is_authenticated:
        favorite_products = Favorite.objects.filter(user=request.user).values_list('product_id', flat=True)

    # Prepare template context
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_occasions': occasions,
        'current_sorting': current_sorting,
        'favorite_products': favorite_products,
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

    # Check if product is in user's favorites
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()

    context = {
        'product': product,
        'is_favorite': is_favorite,
    }

    return render(
        request,
        'products/product_detail.html',
        context
    )


@login_required
def add_product(request):
    """
    Add a product to the store.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    # Handle form submission
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    # Render add product page
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    # Return rendered page
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get product
    product = get_object_or_404(Product, pk=product_id)

    # Handle form submission
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        # Populate form with product data & display info message
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    # Render edit product page
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    # Return rendered page
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store.
    """

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect(reverse('products'))