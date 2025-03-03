from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for Contact model.
    """

    list_display = ('name', 'email', 'subject', 'date_sent')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('date_sent',)
    readonly_fields = ('date_sent',)

# Register the Contact model with the admin site
admin.site.register(Contact, ContactAdmin)