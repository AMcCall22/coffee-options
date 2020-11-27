from django import forms
from .models import UserProfile

"""
Code adapted from from CI's Boutique Ado project,
Profile App section
"""


class UserProfileForm(forms.ModelForm):
    """
    A form for the user profile to save/update delivery address
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_country': 'Country',
            'default_phone_number': 'Phone Number',
            }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:

            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'border-black'
