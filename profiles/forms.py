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

        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Eir Code',
            'default_county': 'County',
        }

        # Set autofocus on the default_full_name field
        self.fields['default_full_name'].widget.attrs['autofocus'] = True

        # Set default_country to Ireland and make it non-editable
        self.fields['default_country'].initial = 'IE'
        self.fields['default_country'].disabled = True
        if 'class' in self.fields['default_country'].widget.attrs:
            self.fields['default_country'].widget.attrs['class'] += (
                ' hidden-country-field'
            )
        else:
            self.fields['default_country'].widget.attrs['class'] = (
                'hidden-country-field'
            )

        # Add placeholders and styling to all form fields
        for field in self.fields:
            # Skip placeholder for select fields
            if field not in ['default_country', 'default_county']:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add profile-form-input class to all fields
            if field not in ['default_country', 'default_county']:
                self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False

        # Add a default placeholder option for the default_county field
        if 'default_county' in self.fields:
            self.fields['default_county'].choices = [
                ('', 'Select County')
            ] + list(self.fields['default_county'].choices)
