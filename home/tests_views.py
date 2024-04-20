from django.test import TestCase, Client
from django.urls import reverse


class HomeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()


    def test_index_view(self):
        # Test access to the index page
        response = self.client.get(reverse('home'))  # Updated to use 'home' instead of 'index'
        self.assertEqual(response.status_code, 200)  # Expecting a success status code
        self.assertTemplateUsed(response, 'home/index.html')
