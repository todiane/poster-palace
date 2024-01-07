from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.db.models import Avg, Count


class Category(models.Model):
    """Model to create product categories"""

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["name"]

        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Model to add products"""

    sku = models.CharField(
        max_length=15, default=get_random_string, null=True, blank=True
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)
    sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(default=9.95, max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def averageReview(self):
        reviews = Reviews.objects.filter(product=self, status=True).aggregate(
            average=Avg("rating")
        )
        avg = 0
        if reviews["average"] is not None:
            avg = float(reviews["average"])
        return avg

    def countReview(self):
        reviews = Reviews.objects.filter(product=self, status=True).aggregate(
            count=Count("id")
        )
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count


class Reviews(models.Model):
    """Model for buyer reviews"""

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "review"
        verbose_name_plural = "reviews"

    def __str__(self):
        return self.subject
