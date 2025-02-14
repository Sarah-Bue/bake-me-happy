from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """
    A view that renders the shopping basket contents page.
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ 
    A view to add a quantity of the specified product to the shopping basket.
    """

    # Get the quantity added to the basket
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url') or request.META.get('HTTP_REFERER', '/products/')
    basket = request.session.get('basket', {})

    # Add or update the item in the basket
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    # Update the session basket data
    request.session['basket'] = basket

    # Get product info for the message
    product = Product.objects.get(pk=item_id)
    messages.success(request, f'{product.name} has been added to your basket')

    # Redirect to the basket page
    return redirect(redirect_url)


def update_basket(request, item_id):
    """
    A view to update the quantity of the specified product.
    """

    # Get the quantity added to the basket
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    # Update the item in the basket
    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    # Update the session basket data
    request.session['basket'] = basket

    # Get product info for the message
    product = Product.objects.get(pk=item_id)
    messages.success(request, f'Updated {product.name} quantity to {quantity}')

    # Redirect to the basket page
    return redirect('view_basket')


def remove_from_basket(request, item_id):
    """
    A view to remove the specified product from the shopping basket.
    """
    
    try:
        # Get the basket data from the session
        basket = request.session.get('basket', {})

        # Remove the item from the basket
        basket.pop(item_id)

        # Update the session basket data
        request.session['basket'] = basket

        # Get product info for the message
        product = Product.objects.get(pk=item_id)
        messages.success(request, f'{product.name} has been removed from your basket')

        # Redirect to the basket page
        return redirect('view_basket')

    # Error Handling
    except Exception as e:
        return redirect('view_basket')