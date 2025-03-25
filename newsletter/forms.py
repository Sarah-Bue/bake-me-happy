from django import forms
from crispy_forms.helper import FormHelper
from .models import Subscriber


class NewsletterForm(forms.ModelForm):
    """
    Form for newsletter subscription.
    """

    class Meta:
        model = Subscriber
        fields = ['email']

    def __init__(self, *args, **kwargs):
        """
        Initialize form with custom styling and attributes.
        """
        super().__init__(*args, **kwargs)

        # Initialize crispy forms helper
        self.helper = FormHelper(self)

        # Configure email field
        self.fields['email'].label = False
        self.fields['email'].widget.attrs.update({
            'id': 'id_newsletter_email',
            'class': 'form-control',
            'placeholder': 'Email address',
            'aria-label': 'Newsletter signup email input'
        })
