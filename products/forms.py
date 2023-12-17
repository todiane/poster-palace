from django import forms
from .models import Review
from django.forms import Textarea


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        