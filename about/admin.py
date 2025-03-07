from django.contrib import admin
from .models import About, Baker, PrivacyPolicy, AllergenInfo, FAQ
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


class AllergenInfoAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing Allergen Information content.
    """

    list_display = ('title', 'updated_on')
    summernote_fields = ('content',)


class FAQAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing FAQ content.
    """

    list_display = ('question', 'order', 'updated_on')
    list_editable = ('order',)
    summernote_fields = ('answer',)


# Register models with the admin interface
admin.site.register(About, AboutAdmin)
admin.site.register(Baker, BakerAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
admin.site.register(AllergenInfo, AllergenInfoAdmin)
admin.site.register(FAQ, FAQAdmin)
