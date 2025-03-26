from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for processing customer orders.
    """

    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode',
            'country', 'delivery_method', 'county'
        )
        # Exclude payment_method to prevent it from being rendered twice
        exclude = ('payment_method',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes to form fields.
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Eir Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Set autofocus on the full_name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Set country to Ireland and make it non-editable
        self.fields['country'].initial = 'IE'
        self.fields['country'].disabled = True
        if 'class' in self.fields['country'].widget.attrs:
            self.fields['country'].widget.attrs['class'] += (
                ' hidden-country-field')
        else:
            self.fields['country'].widget.attrs['class'] = (
                'hidden-country-field')

        # Manually add payment_method field with radio buttons
        self.fields['payment_method'] = forms.ChoiceField(
            choices=(
                ('card', 'Credit/Debit Card'), ('cash', 'Cash on Pickup')),
            widget=forms.RadioSelect(), 
            required=True,
            initial='card'
        )

        # Add placeholders and styling to all form fields
        for field in self.fields:
            # Skip placeholder for fields that are handled separately
            if field not in [
                'country', 'delivery_method', 'payment_method', 'county'
                    ]:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add stripe-style-input class to all fields except radio buttons
            if field not in ['delivery_method', 'payment_method']:
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

        # Add a default placeholder option for the county field
        if 'county' in self.fields:
            self.fields['county'].choices = [
                ('', 'Select County')] + list(self.fields['county'].choices)

        # Add radio button styling for delivery method if it exists
        if 'delivery_method' in self.fields:
            self.fields['delivery_method'].widget = forms.RadioSelect(
                choices=Order.DELIVERY_CHOICES
            )
            self.fields['delivery_method'].label = "Delivery Method"
