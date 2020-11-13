from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'street_address1', 'street_address2', 'town_or_city', 'postcode', 'country', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'full_name': 'Full Name',
                'street_address1': 'Street Address 1',
                'street_address2': 'Street Address 2',
                'postcode': 'Postal Code',
                'town_or_city': 'Town or City',
                'country': 'Country',
                'email': 'Email Address',
                'phone_number': 'Phone Number',               
                }

            self.fields['full_name'].widget.attrs['autofocus'] = True
            for field in self.fields:

                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
