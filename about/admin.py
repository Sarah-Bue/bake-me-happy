
from django.contrib import admin
from .models import About, Baker, PrivacyPolicy
from django_summernote.admin import SummernoteModelAdmin


class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface managing Acout content.
    """

    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)


class BakerAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing baker profiles.
    """

    list_display = ('name', 'title', 'order')
    list_editable = ('order',)
    summernote_fields = ('bio',)


class PrivacyPolicyAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing Privacy Policy conent.
    """
    
    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)


# Register the About model with the custom AboutAdmin class
admin.site.register(About, AboutAdmin)
admin.site.register(Baker, BakerAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
