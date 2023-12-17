from django import forms
from .models import Review
from django.forms import Textarea


class ReviewForm(forms.ModelForm):
    """
    form to render product reviews
    """
    class Meta:
        model = Review
        fields = ['id', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={"rows": 4})
        }