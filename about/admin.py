
from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for About model with Summernote editor.
    """

    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)

# Register the About model with the custom AboutAdmin class
admin.site.register(About, AboutAdmin)
