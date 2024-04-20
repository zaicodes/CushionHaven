from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Product, Comment


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Test Category',
                                friendly_name='Test Friendly Name')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_friendly_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('friendly_name').verbose_name
        self.assertEqual(field_label, 'friendly name')

    def test_get_friendly_name(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_friendly_name(), 'Test Friendly Name')


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = Category.objects.create(name='Test Category')
        Product.objects.create(
            name='Test Product', description='Test Description', price=10.00, category=category)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # Add more tests for other fields as needed...


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(
            name='Test Product', description='Test Description', price=10.00, category=category)
        Comment.objects.create(user=user, product=product, text='Test Comment')

    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'text')
