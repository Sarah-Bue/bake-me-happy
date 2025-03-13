from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to manage user profile information.
    """

    class Meta:
        model = UserProfile
        # Exclude user field, show all other fields
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels, and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # Make country read-only        
        self.fields['default_country'].widget.attrs['readonly'] = True
        self.fields['default_country'].widget.attrs['disabled'] = True

        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Eir Code',
            'default_county': 'Please select a County',
            'default_country': 'Ireland'
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Add placeholders and classes to form fields
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False