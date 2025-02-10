from django.contrib import admin
from .models import Product, Category, Occasion


class ProductAdmin(admin.ModelAdmin):
    """
    Admin model for managing products.
    """

    # Fields to display in the admin interface
    list_display = (
        'name',
        'german_name',
        'category',
        'occasion',
        'sku',
        'price',
        'rating',
        'image',
    )

    # Fields to use for filtering
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin model for managing categories.
    """

    # Fields to display in the admin interface
    list_display = (
        'friendly_name',
        'name',
    )

    # Fields to use for filtering
    ordering = ('name',)


class OccasionAdmin(admin.ModelAdmin):
    """
    Admin model for managing occasions.
    """

    # Fields to display in the admin interface
    list_display = (
        'friendly_name',
        'name',
    )

    # Fields to use for filtering
    ordering = ('name',)


# Registered models

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
