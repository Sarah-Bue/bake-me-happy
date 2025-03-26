from django import forms
from crispy_forms.helper import FormHelper
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for contact submissions.
    """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            # 'subject': forms.Select(),
            'subject': forms.Select(attrs={
                'class': 'form-control select form-select',
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Custom styling for the form fields.
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your Name',
            'email': 'Your Email Address',
            'subject': 'Please select a Subject *',
            'message': 'Your Message',
        }

        # Initialize crispy forms helper
        self.helper = FormHelper(self)

        # Set autofocus on the name field
        self.fields['name'].widget.attrs['autofocus'] = True

        # Add placeholders and styling to all form fields
        for field in self.fields:
            if field == 'subject':
                # Add a default option to act as a placeholder
                self.fields[field].choices = [
                    ('', placeholders[field])
                ] + list(self.fields[field].choices)

                self.fields[field].widget.attrs['class'] += (
                    ' profile-form-input'
                )
            else:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False

            # Add profile-form-input class to subject dropdown
            if field == 'subject':
                self.fields[field].widget.attrs['class'] += (
                    'profile-form-input'
                )

        # Set a unique ID for the email field
        self.fields['email'].widget.attrs['id'] = 'contact_email'
