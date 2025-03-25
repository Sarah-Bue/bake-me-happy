from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for Profile model.
    """
    list_display = ('user', 'default_phone_number', 'default_country')
    search_fields = ('user__username', 'default_phone_number')


# Register the Profile model with the admin site
admin.site.register(UserProfile, UserProfileAdmin)
