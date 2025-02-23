from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Favorite


@login_required
def view_favorites(request):
    """
    A view to return the favorites list page.
    """
    # Retrieve the user's favorites
    favorites = Favorite.objects.filter(user=request.user)

    # Pass the favorites to the template
    context = {
        'favorites': favorites,
    }

    # Render the favorites template
    return render(request, 'favorites/favorites.html', context)


@login_required
def toggle_favorites(request, product_id):
    """
    Toggle a product in favorites.
    """

    # Get the product
    product = get_object_or_404(Product, pk=product_id)
    favorite = Favorite.objects.filter(user=request.user, product=product)

    # If the product is already in favorites, remove it
    if favorite.exists():
        favorite.delete()
        messages.success(request, f'{product.name} has been removed from your Favorites.')
    
    # If the product is not in favorites, add it
    else:
        Favorite.objects.create(user=request.user, product=product)
        messages.success(request, f'{product.name} has been added to your Favorites.')

    return redirect(request.META.get('HTTP_REFERER', 'favorites'))