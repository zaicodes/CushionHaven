from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile
from checkout.models import Order


class ProfileViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password')

    def setUp(self):
        # Set up modified objects used by test methods
        self.client = Client()
        self.client.force_login(self.user)
        # Create UserProfile object for the user if it doesn't exist
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)

    def test_profile_view_get(self):
        # Test GET request to the profile view
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_view_post_valid_form(self):
        # Test POST request to the profile view with valid form data
        response = self.client.post(
            reverse('profile'), {'default_phone_number': '123456789'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(UserProfile.objects.get(
            user=self.user).default_phone_number, '123456789')
        self.assertContains(response, 'Profile updated successfully')


class OrderHistoryViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password')

    def setUp(self):
        # Set up modified objects used by test methods
        self.client = Client()
        self.client.force_login(self.user)
        # Create Order object for the user if it doesn't exist
        self.order, _ = Order.objects.get_or_create(order_number='123456')

    def test_order_history_view(self):
        # Test the order history view
        response = self.client.get(
            reverse('order_history', args=[self.order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, f' {self.order.order_number}')
