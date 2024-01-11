from django.urls import path
from . import views
from .views import ShippingView, PrivacyView, TermsView, RefundView


urlpatterns = [
    path("", views.all_products, name="products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("submit_review/<int:product_id>/",
         views.submit_review, name="submit_review"),
    path("shipping/", ShippingView.as_view(), name="shipping"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
    path("terms/", TermsView.as_view(), name="terms"),
    path("refund/", RefundView.as_view(), name="refund"),
]
