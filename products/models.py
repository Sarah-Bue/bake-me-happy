from django.db import models


class Category(models.Model):
    """
    Model representing product categories.
    Stores categories for products with both a technical name and an optional
    customer-friendly display name.
    """

    # Meta class to set plural name in admin interface
    class Meta:
        verbose_name_plural = 'Categories'

    # Fields
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    # String method to return name
    def __str__(self):
        return self.name

    # String method to return friendly name
    def get_friendly_name(self):
        return self.friendly_name


class Occasion(models.Model):
    """
    Model representing product occasions.
    
    Stores occasions with both a technical name
    and an optional customer-friendly display name.
    """

    # Fields
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    # String method to return name
    def __str__(self):
        return self.name
    
    # String method to return friendly name
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model representing products.
    
    Stores comprehensive product information including names in both English and German,
    pricing, categorization, and optional details like SKU and images.
    """
        
    # Mandatory fields
    name = models.CharField(max_length=100)
    german_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Optional fields
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    occasion = models.ForeignKey('Occasion', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # String method to return name
    def __str__(self):
        return self.name