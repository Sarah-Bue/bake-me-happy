from django.contrib import admin
from .models import Product, Category, Occasion


class ProductAdmin(admin.ModelAdmin):
    """
    Admin model for managing products.
    """
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

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin model for managing categories.
    """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


class OccasionAdmin(admin.ModelAdmin):
    """
    Admin model for managing occasions.
    """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


# Registered models

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
