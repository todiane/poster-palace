from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
    ShippingView, 
    PrivacyView, 
    TermsView, 
    RefundView, 
)

class TestProductViews(SimpleTestCase):
    def test_shipping_view(self):
        url = reverse('shipping')  
        self.assertEqual(resolve(url).func.view_class, ShippingView)

    def test_privacy_view(self):
        url = reverse('privacy')  
        self.assertEqual(resolve(url).func.view_class, PrivacyView)

    def test_terms_view(self):
        url = reverse('terms')  
        self.assertEqual(resolve(url).func.view_class, TermsView)

    def test_refund_view(self):
        url = reverse('refund')  
        self.assertEqual(resolve(url).func.view_class, RefundView)
