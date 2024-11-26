from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.contrib.messages import get_messages
import json

# models to import
from checkout.models import Order, OrderLineItem
from profiles.models import BuyerProfile
from products.models import Category, Product, Reviews
from contact.models import Contact
from wishlist.models import WishList

# views models to import
from product.views import submit_review
from bag.views import remove_from_bag

# forms to import
from contact.forms import ContactForm


# Testing Views for Bag app
class TestBagView(TestCase):

    def test_return_template(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

class TestAddToCartView(TestCase):

    def test_add_to_bag(self):
        response = self.client.post('/add_to_bag/', data={
            'id': '18',
            'name': 'Purple Rain',
            'qty': '2',
            'image': 'dark_moon.jpg',
            'price': '29.95',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        cart_data = response_data['data']
        self.assertTrue(cart_data)
        cart_item = cart_data['1']
        self.assertEqual(cart_item['name'], 'Purple Rain')
        self.assertEqual(cart_item['qty'], 2)
        self.assertEqual(cart_item['price'], 29.95)
        self.assertEqual(cart_item['image'], 'purple_rain.png')


# Testing Views for Reviews
class TestReviewViews(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test review
        """
        self.user = User.objects.create(
            username='KamiSmith',
            email='ksmith@hotmail.com',
            password='L0gM3In24',
            id='2',
        )
        self.user.save()
        self.my_category = Category.objects.create(
            name='abstract',
            slug='abstract',
            friendly_name='Abstract'
        )
        self.my_category.save()
        self.product = Product.objects.create(
            category=self.my_category,
            name='Purple Rain',
            description='Purple rain poster',
            price=29.95,
            id='18'
        )

    def tearDown(self):
        self.product.delete()
        self.my_category.delete()
        self.user.delete()

    def test_review_creation(self):
        self.client.force_login(self.user)
        response = self.client.post('/products/submit_review/', data={
            'id': '4',
            'user': self.user.username,
            'product_id': self.product.id,
            'content': 'My Testing Review',
            'current_time': '2024-02-18T10:00:00'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Review.objects.filter(author=self.user).exists())

    def test_update_review(self):
        self.client.force_login(self.user)
        self.my_review = Review.objects.create(
            author=self.user,
            product=self.product,
            content='My New Testing Review',
            id='4'

        )
        response = self.client.post('/products/submit_review/', data={
            'product_id': self.my_review.id,
            'content': 'My Review',
            'current_time': '2024-02-18T10:00:30',
            'id': '4'

        })
        self.assertEqual(response.status_code, 200)

    def test_delete_review(self):
        self.client.force_login(self.user)
        self.my_review = Review.objects.create(
            author=self.user,
            product=self.product,
            content='My New Testing Review',
            id='4'

        )
        response = self.client.post('/review/delete_review/', data={
                'review_id': self.my_review.id

        })
        self.assertEqual(response.status_code, 302)

        self.new_user = User.objects.create(
            username='KamiSmith',
            email='ksmith@hotmail.com',
            password='L0gM3In24',
            id='2',
        )
        self.new_user.save()
        self.my_new_review = Review.objects.create(
            author=self.new_user,
            product=self.product,
            content='My New Testing Review',
            id='4'

        )


# Testing Views for Contact Us App
class ContactViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='KamiSmith',
            email='ksmith@hotmail.com',
            password='L0gM3In24',
            id='2',
        )

    def test_contact_view_authenticated(self):
        client = Client()
        client.force_login(self.user)

        # Test the contact view for an authenticated user
        response = client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

        # Check if the form uses the user's email
        form = response.context['form']
        self.assertEqual(form.fields['email'].initial, self.user.email)

    def test_contact_view_not_authenticated(self):
        client = Client()

        # Test the contact view for an unauthenticated user
        response = client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

        # Check if the form asks for email
        form = response.context['form']
        self.assertTrue('email' in form.fields)


# Testing Views for WishList
class WishListViewTestCase(TestCase):
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='KamiSmith',
            email='ksmith@hotmail.com',
            password='L0gM3In24',
            id='2',
        )
        self.product = Product.objects.create(name='Purple Rain', price=29.95)

    def test_render_wishlist_page_authenticated(self):
        request = self.factory.get(reverse('wishlist'))
        request.user = self.user
        response = wishlist_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_render_wishlist_page_unauthenticated(self):
        request = self.factory.get(reverse('wishlist'))
        response = wishlist_view(request)
        self.assertEqual(response.status_code, 302)  

    def test_add_to_wishlist(self):
        initial_count = WishList.objects.count()
        request = self.factory.post(reverse('add_wish'), {'product-id': self.product.id})
        request.user = self.user
        response = wishlist_view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(WishList.objects.count(), initial_count + 1)

    def test_delete_wish(self):
        wish_item = WishList.objects.create(user=self.user, product=self.product)
        initial_count = WishList.objects.count()
        request = self.factory.post(reverse('delete_wish'), {'item-id': wish_item.id}, content_type='application/json')
        request.user = self.user
        response = wishlist_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(WishList.objects.count(), initial_count - 1)
    