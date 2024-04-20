from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Comment


class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.00)

    def test_add_comment(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Simulate a POST request to add a comment
        response = self.client.post(reverse('add_comment', kwargs={
                                    'product_id': self.product.id}), {'comment': 'This is a test comment'})

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Check if the comment is added to the database
        self.assertTrue(Comment.objects.filter(
            user=self.user, product=self.product, text='This is a test comment').exists())

    def test_add_comment_empty(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Simulate a POST request to add an empty comment
        response = self.client.post(reverse('add_comment', kwargs={
                                    'product_id': self.product.id}), {'comment': ''})

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Check if the comment is not added to the database
        self.assertFalse(Comment.objects.filter(
            user=self.user, product=self.product).exists())
