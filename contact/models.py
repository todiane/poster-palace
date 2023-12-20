from django.db import models


class Contact(models.Model):
    """ contact form for visitors and customers"""

    CONTACT_CHOICES = [
        ('', 'Reason for Contact'),
        ('PRODUCT', 'Product Enquiry'),
        ('ORDER', 'Order Enquiry'),
        ('CS', 'Customer Service'),
        ('SUGGESTIONS', 'Suggestions'),
        ('OTHER', 'Other'),

    ]
    contact_purpose = models.CharField(max_length=24, choices=CONTACT_CHOICES)
    email = models.EmailField()
    name = models.CharField(max_length=44)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_submitted']

    def __str__(self):
        return self.email
