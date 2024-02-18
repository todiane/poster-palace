from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from profiles.models import BuyerProfile
from products.models import Category, Product, Reviews
from contact.models import Contact


# Testing checkout cart and profile models
class TestOrderModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='SallySmith',
            email='ssmith@gmail.com',
            password='S1mile48',
            id='1',
        )
        self.user.save()

        self.customer_profile = BuyerProfile.objects.get(user=self.user)

        self.my_order = Order.objects.create(
                order_number='260124GDB051177MY8DE1C0DC',
                user_profile=self.profiles,
                full_name='Sally Smith',
                email='ssmith@gmail.com',
                phone_number='60134541',
                country='United Kingdom',
                postcode='TF75ME',
                town_or_city='Peckham',
                street_address1='67 Pudding Lane',
                street_address2='Off Cake Street',
                county='London',
                date='2024-01-13T12:00:00',
                order_total='55.90',
                grand_total='55.90',
                original_bag='bag',
                stripe_pid='pid'
                )

    def teardown(self):
        self.my_order.delete()
        self.customer_profile.delete()
        self.user.delete()

    def test_order_creation(self):
        self.assertTrue(Order.objects.filter(order_number='260124GDB051177MY8DE1C0DC'))
        self.assertEqual(str(self.my_order), '260124GDB051177MY8DE1C0DC')

    def test_generate_order_number(self):
        self.assertTrue(self.my_order._generate_order_number())


class TestOrderLineItemModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test user, product, and order
        """
        self.user = User.objects.create(
            username='SallySmith',
            email='ssmith@gmail.com',
            password='S1mile48',
            id='1',
        )
        self.user.save()

        self.buyer_profile = BuyerProfile.objects.get(user=self.user)

        self.my_category = Category.objects.create(
            name='bright',
            slug='bright',
            friendly_name='Bright'
        )

        self.my_category.save()
        self.product = Product.objects.create(
            category=self.my_category,
            name='Bright Nature',
            description='Kaleidoscopic celebration of the natural world',
            price=27.95,

        )

        self.my_order = Order.objects.create(
                order_number='260124GDB051177MY8DE1C0DC',
                user_profile=self.profiles,
                full_name='Sally Smith',
                email='ssmith@gmail.com',
                phone_number='60134541',
                country='United Kingdom',
                postcode='TF75ME',
                town_or_city='Peckham',
                street_address1='67 Pudding Lane',
                street_address2='Off Cake Street',
                county='London',
                date='2024-01-13T12:00:00',
                order_total='55.90',
                grand_total='55.90',
                original_bag='bag',
                stripe_pid='pid'
                )
        self.new_oderlineitem = OrderLineItem.objects.create(
            order=self.my_order,
            product=self.product,
            quantity=2,
            lineitem_total=55.90
        )
        self.new_oderlineitem.save()

    def test_orderlineitem_creation(self):
        self.assertEqual(OrderLineItem.objects.count(), 1)
        self.assertEqual(str(self.new_orderlineitem))


# testing reviews model
class TestReviewModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test review
        """
        self.user = User.objects.create(
            username='SallySmith',
            email='ssmith@gmail.com',
            password='S1mile48',
            id='1',
        )
        self.user.save()
        self.my_category = Category.objects.create(
            name='bright',
            slug='bright',
            friendly_name='Bright'
        )
        self.my_category.save()
        self.product = Product.objects.create(
            category=self.my_category,
            name='Bright Nature',
            description='Kaleidoscopic celebration of the natural world',
            price=27.95,
        )

        self.my_review = Review.objects.create(
            author=self.user,
            product=self.product,
            content='My first review'

        )

    def tearDown(self):
        self.my_review.delete()
        self.my_category.delete()
        self.product.delete()
        self.user.delete()

    def test_string_method_return(self):
        self.assertEqual(str(self.my_review),
                         'Review by SallySmith for Bright Nature: My first review'

                         )

# testing contact us model
class TestContactModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='SallySmith',
            email='ssmith@gmail.com',
            password='S1mile48',
            id='1',
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_string_method_return(self):
        self.contact = Contact.objects.create(
            contact_choices='Other',
            name=self.user.username,
            email='ssmith@gmail.com',
            phone='123456',
            message='other test message'

        )
        self.assertEqual(str(self.contact),
                         'Contact SSmith and other test message created')


# Test for wish list model

class TestWishlistModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='SallySmith',
            email='ssmith@gmail.com',
            password='S1mile48',
            id='1',
        )
        self.user.save()
        self.my_category = Category.objects.create(
            name='bright',
            slug='bright',
            friendly_name='Bright'
        )
        self.my_category.save()
        self.product = Product.objects.create(
            category=self.my_category,
            name='Bright Nature',
            description='Kaleidoscopic celebration of the natural world',
            price=27.95,
        )

    def tearDown(self):
        self.user.delete()

    def test_string_method_return(self):
        self.my_wishlist = Wishlist.objects.create(
            user=self.user,
            product=self.product

        )
        self.assertEqual(str(self.my_wishlist), 'Test Bright Nature in Bright')