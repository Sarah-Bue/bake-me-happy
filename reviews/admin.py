from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review


class ReviewAdmin(SummernoteModelAdmin):
    """
    Admin configuration for Review model
    """
    list_display = ('product', 'author', 'title', 'rating', 'date_added')
    list_filter = ('rating', 'date_added', 'product')
    search_fields = ('title', 'review_comment', 'product__name', 'author__username')
    readonly_fields = ('date_added',)
    ordering = ('-date_added',)
    summernote_fields = ('review_comment',)


admin.site.register(Review, ReviewAdmin)