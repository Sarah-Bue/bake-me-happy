
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for processing customer orders.
    """
    
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                 'street_address1', 'street_address2',
                 'town_or_city', 'postcode', 'county',
                 'country',)


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes to form fields
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Set autofocus on the full_name field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Add placeholders and styling to all form fields
        for field in self.fields:
            # Country field handled separately, does not need placeholder
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add stripe-style-input class to all fields
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
