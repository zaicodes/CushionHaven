from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password')

    def test_user_profile_creation(self):
        # Test that a user profile is created when a user is created
        user = User.objects.get(username='testuser')
        user_profile = UserProfile.objects.get(user=user)
        self.assertIsNotNone(user_profile)
        self.assertEqual(user_profile.default_phone_number, None)
        self.assertEqual(user_profile.default_street_address1, None)
        # Add more assertions for other fields as needed...

    def test_user_profile_update(self):
        # Test that a user profile is updated when a user is updated
        user = User.objects.get(username='testuser')
        user_profile = UserProfile.objects.get(user=user)
        user_profile.default_phone_number = '123456789'
        user_profile.save()
        updated_user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(
            updated_user_profile.default_phone_number, '123456789')
        # Add more assertions for other fields as needed...


class UserProfileSignalTest(TestCase):
    def test_signal_receiver(self):
        # Test that the signal creates a user profile when a user is created
        user = User.objects.create_user(
            username='testsignaluser', email='testsignal@example.com', password='password')
        user_profile = UserProfile.objects.filter(user=user).first()
        self.assertIsNotNone(user_profile)

        # Test that the signal updates the user profile when a user is updated
        user.first_name = 'Updated First Name'
        user.save()
        updated_user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(updated_user_profile.user.first_name,
                         'Updated First Name')
        # Add more assertions for other fields as needed...
