import unittest
from django.test import TestCase
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from .models import Category, Product, Reviews

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(
            name='abstract',
            slug='abstract',
            friendly_name='Abstract'
        )
        self.assertEqual(category.name, 'abstract')
        self.assertEqual(category.slug, 'abstract')
        self.assertEqual(category.friendly_name, 'Abstract')

class ProductModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name='abstract',
            slug='abstract',
            friendly_name='Abstract'
        )
        self.product = Product.objects.create(
            sku=get_random_string(length=15),
            name='Test Product',
            slug='test-product',
            description='Test description',
            price=19.99,
            category=category
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.slug, 'test-product')
        self.assertEqual(self.product.description, 'Test description')
        self.assertEqual(self.product.price, 19.99)
        self.assertEqual(self.product.category.name, 'abstract')

    def test_average_review(self):
        user = User.objects.create(username='testuser')
        review = Reviews.objects.create(
            product=self.product,
            user=user,
            subject='Test Review',
            review='This is a test review.',
            rating=4.5
        )
        self.assertEqual(self.product.averageReview(), 4.5)

    def test_count_review(self):
        user = User.objects.create(username='testuser')
        review1 = Reviews.objects.create(
            product=self.product,
            user=user,
            subject='Test Review 1',
            review='This is a test review.',
            rating=4.5
        )
        review2 = Reviews.objects.create(
            product=self.product,
            user=user,
            subject='Test Review 2',
            review='This is another test review.',
            rating=3.0
        )
        self.assertEqual(self.product.countReview(), 2)

class ReviewsModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name='Test Category',
            slug='test-category',
            friendly_name='Test Friendly Name'
        )
        product = Product.objects.create(
            sku=get_random_string(length=15),
            name='Test Product',
            slug='test-product',
            description='Test description',
            price=19.99,
            category=category
        )
        user = User.objects.create(username='testuser')
        self.review = Reviews.objects.create(
            product=product,
            user=user,
            subject='Test Review',
            review='This is a test review.',
            rating=4.5
        )

    def test_review_creation(self):
        self.assertEqual(self.review.subject, 'Test Review')
        self.assertEqual(self.review.review, 'This is a test review.')
        self.assertEqual(self.review.rating, 4.5)