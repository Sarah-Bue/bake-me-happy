from django.shortcuts import render, redirect


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

    # Redirect to the basket page
    return redirect('view_basket')