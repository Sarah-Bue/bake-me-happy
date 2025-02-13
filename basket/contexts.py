
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

# The context processor function has been adapted from Code Institute's "Boutique Ado" project.

def basket_contents(request):
    """
    Context processor for the shopping basket.
    Makes basket data available to all templates across the site.
    Calculates totals, delivery costs, and free delivery threshold.
    """
    # Initialize lists and counters
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    # Iterate through items in basket session
    for item_id, quantity in basket.items():
        # Get product information
        product = get_object_or_404(Product, pk=item_id)
        # Calculate subtotal for current item
        subtotal = quantity * product.price
        # Add to running total
        total += subtotal
        # Increment product count
        product_count += quantity
        # Add item details to basket items list
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })

    # Calculate delivery costs
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Calculate grand total including delivery
    grand_total = delivery + total

    # Create context dictionary
    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
