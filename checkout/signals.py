
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# The signal handlers have been adapted from the Code Institute "Boutique Ado" project

@receiver(post_save, sender=OrderLineItem)
def update_on_line_item_save(sender, instance, created, **kwargs):
    """
    Signal handler to update order total when a line item is created or updated.
    """

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_line_item_delete(sender, instance, **kwargs):
    """
    Signal handler to update order total when a line item is deleted.
    """
    
    instance.order.update_total()
