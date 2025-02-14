from django import template

# Register the template tag
register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal for a product.
    """
    return price * quantity