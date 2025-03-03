
from django.contrib import admin
from .models import About, Baker
from django_summernote.admin import SummernoteModelAdmin


class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for About model with Summernote editor.
    """

    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)


class BakerAdmin(SummernoteModelAdmin):
    """
    Admin model for managing bakers
    """

    list_display = ('name', 'title', 'order')
    list_editable = ('order',)
    summernote_fields = ('bio',)

# Register the About model with the custom AboutAdmin class
admin.site.register(About, AboutAdmin)
admin.site.register(Baker, BakerAdmin)
