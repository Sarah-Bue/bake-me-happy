from django.conf import settings
from decimal import Decimal

from products.models import Product


# The context has been adapted from Code Institute's "Boutique Ado" project


def basket_contents(request):
    """
    Context processor for basket contents.
    Makes basket contents available across all templates.
    """

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    # Get delivery method from session, default to 'delivery'
    delivery_method = request.session.get('delivery_method', 'delivery')

    for item_id, quantity in basket.items():
        # Get product
        try:
            product = Product.objects.get(id=item_id)
            total += quantity * product.price
            product_count += quantity
            basket_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        except Product.DoesNotExist:
            # Handle case where product doesn't exist
            pass

    # Calculate free delivery delta regardless of delivery method
    if total < settings.FREE_DELIVERY_THRESHOLD:
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        free_delivery_delta = 0

    # Only apply delivery cost if delivery method is 'delivery'
    if delivery_method == 'delivery':
        if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery = Decimal(settings.STANDARD_DELIVERY)
        else:
            delivery = 0
    else:
        # No delivery cost for pickup
        delivery = 0

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
