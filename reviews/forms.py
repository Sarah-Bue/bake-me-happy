from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for creating and editing reviews.
    """

    # Create radio buttons for ratings 1-5
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect(attrs={'class': 'star-rating'}),
        required=False
    )

    class Meta:
        model = Review
        fields = ['title', 'rating', 'review_comment']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'review_comment': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].required = False
        self.fields['review_comment'].required = False
