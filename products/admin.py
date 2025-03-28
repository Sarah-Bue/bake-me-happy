from django.contrib import admin
from .models import Product, Category, Occasion, Allergen
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(SummernoteModelAdmin):
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
        'serving_size',
        'rating',
        'image',
    )

    def get_allergens(self, obj):
        """
        Custom method to display allergens in the admin panel.
        """
        return ", ".join([allergen.name for allergen in obj.allergens.all()])

    get_allergens.short_description = 'Allergens'

    # Summernote configuration for the 'description' field
    summernote_fields = ('description',)

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
admin.site.register(Allergen)
