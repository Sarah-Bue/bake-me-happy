import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField
from decimal import Decimal

from products.models import Product
from profiles.models import UserProfile

# The Order and OrderLineItem models have been adapted
# from Code Institute's Boutique Ado project.


class Order(models.Model):
    """
    Model representing customer orders.
    Stores order information, customer details,
    delivery information, and order totals.
    """

    # User Profile
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='orders'
    )

    # Order Details
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)

    # Customer Information
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    # Delivery Information
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    COUNTY_CHOICES = [
        ('', 'Please select a County'),
        ('Carlow', 'Carlow'),
        ('Cavan', 'Cavan'),
        ('Clare', 'Clare'),
        ('Cork', 'Cork'),
        ('Donegal', 'Donegal'),
        ('Dublin', 'Dublin'),
        ('Galway', 'Galway'),
        ('Kerry', 'Kerry'),
        ('Kildare', 'Kildare'),
        ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Louth', 'Louth'),
        ('Mayo', 'Mayo'),
        ('Meath', 'Meath'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Waterford', 'Waterford'),
        ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'),
        ('Wicklow', 'Wicklow'),
    ]
    county = models.CharField(
        max_length=80, null=True, blank=True, choices=COUNTY_CHOICES
    )

    # Delivery Methods
    DELIVERY_CHOICES = [
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup'),
    ]

    delivery_method = models.CharField(
        max_length=10,
        choices=DELIVERY_CHOICES,
        default='delivery',
        null=False,
        blank=False,
    )

    # Payment Methods
    PAYMENT_METHODS = (
        ('card', 'Credit/Debit Card'),
        ('cash', 'Cash on Pickup'),
    )

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        default='card'
    )

    # Order Totals
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    # Stripe Payment
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number.
        Returns a 10-character string: 'BMH' prefix + 7 random characters
        """
        random_string = uuid.uuid4().hex[:7].upper()
        return f'BMH-{random_string}'
        #  return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added.

        Calculates the order total from line items and applies
        delivery costs based on the FREE_DELIVERY_THRESHOLD.
        """

        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        # Only apply delivery cost if delivery method is 'delivery'
        if self.delivery_method == 'delivery':
            if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
                self.delivery_cost = Decimal(settings.STANDARD_DELIVERY)
            else:
                self.delivery_cost = 0
        else:
            # No delivery cost for pickup
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Model representing individual line items within an order.
    Stores product, quantity & calculated total for each
    item in a customer's order.
    """

    # Relationships
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )

    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    # Line Item Details
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
