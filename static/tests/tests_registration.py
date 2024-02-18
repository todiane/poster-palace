from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        # Test user registration functionality
        response = self.client.post(reverse('register'), {
            'username': 'manager',
            'email': 'test@example.com',
            'password1': 'test!Password123',
            'password2': 'test!Password123'
        })
        self.assertEqual(response.status_code, 302)  # Check for successful redirection
        self.assertTrue(User.objects.filter(username='manager').exists())  # Check if user is created

        # Check if the user is created with the correct password
        user = User.objects.get(username='manager')
        self.assertTrue(user.check_password('test!Password123'))