from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    """
    A class to customize the admin interface for the Subscriber model.
    """
    
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)

admin.site.register(Subscriber, SubscriberAdmin)