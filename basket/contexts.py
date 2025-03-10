from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product

from decimal import Decimal

# The context has been adapted from Code Institute's "Boutique Ado" project


def basket_contents(request):
    """
    Context processor for the shopping basket.
    Calculates item totals, delivery costs, and provides basket information
    across all templates.
    """

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    # Calculate totals for each item in the basket
    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Calculate delivery costs and free delivery delta
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

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
