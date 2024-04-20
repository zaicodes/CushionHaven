from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product


class BagViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name="Test Product", price=10)

    def test_add_to_bag(self):
        # Test adding a product to the bag
        url = reverse('add_to_bag', kwargs={'item_id': self.product.pk})
        response = self.client.post(
            url, {'quantity': 1, 'redirect_url': reverse('view_bag')})
        # Expecting a redirect status code
        self.assertEqual(response.status_code, 302)

    def test_remove_from_bag(self):
        # Add the item to the bag first
        self.client.post(reverse('add_to_bag', kwargs={'item_id': self.product.pk}), {
                         'quantity': 1, 'redirect_url': reverse('view_bag')})

        # Test removing the item from the bag
        url = reverse('remove_from_bag', kwargs={'item_id': self.product.pk})
        response = self.client.post(url)
        # Expecting a success response
        self.assertEqual(response.status_code, 200)
