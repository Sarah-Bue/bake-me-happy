from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for creating and editing reviews.
    """

    class Meta:
        model = Review
        fields = ['title', 'rating', 'review_comment']
        widgets = {
            'review_comment': SummernoteWidget(),
            'rating': forms.NumberInput(attrs={
                'min': '1',
                'max': '5',
                'class': 'form-control',
                'aria-label': 'Rating from 1 to 5 stars'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].required = False
        self.fields['review_comment'].required = False
