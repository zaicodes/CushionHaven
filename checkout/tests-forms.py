from django.test import TestCase
from .forms import OrderForm, AddressForm


class TestForms(TestCase):
    def test_order_form(self):
        form = OrderForm(data={
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'postcode': '12345',
            'town_or_city': 'City',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 1',
            'county': 'County',
        })

        self.assertTrue(form.is_valid())

    def test_address_form(self):
        form = AddressForm(data={
            'postcode': '12345',
            'country': 'Country',
        })

        self.assertTrue(form.is_valid())
