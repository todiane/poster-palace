from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class WishList(models.Model):
    """User can start a wishlist"""

    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wishlist_user"
    )
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="wishlist_product"
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str("Wishlist")
