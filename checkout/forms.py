from django import forms
from .models import Order, Address


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'country', 'postcode',
                  'town_or_city', 'street_address1',
                  'street_address2', 'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
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
        required_fields = ['full_name', 'email', 'phone_number', 'street_address1', 'postcode', 'town_or_city', "county"]
        for field_name, field in self.fields.items():
            placeholder = placeholders.get(field_name, '')
            field.widget.attrs['class'] = 'stripe-style-input'
            field.label = False
            if field_name in required_fields:
                field.required = True
                placeholder += ' *'
            field.widget.attrs['placeholder'] = placeholder


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['county', 'postcode', 'country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'street_address': 'Street Address',
            'city': 'City',
            'postcode': 'Postal Code',
            'country': 'Country',
            'county': 'County',
        }
        required_fields = ['street_address', 'city', 'postcode']
        for field_name, field in self.fields.items():
            placeholder = placeholders.get(field_name, '')
            field.widget.attrs['placeholder'] = placeholder
            field.widget.attrs['class'] = 'form-control'
            if field_name in required_fields:
                field.required = True
            else:
                field.required = False
