from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """Contact Us form for visitors and customers"""

    CONTACT_CHOICES = [
        ("", "Reason for Contact"),
        ("Product Enquiry", "Product Enquiry"),
        ("Order Enquiry", "Order Enquiry"),
        ("Customer Service", "Customer Service"),
        ("Diverse Design", "Diverse Design Event"),
        ("Complaint", "Complaint"),
        ("Feedback", "Feedback"),
        ("Other", "Other"),
    ]
    contact_purpose = models.CharField(max_length=24, choices=CONTACT_CHOICES)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    name = models.CharField(max_length=44)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_submitted"]

        verbose_name = "Messages from User"

    def __str__(self):
        return self.email
