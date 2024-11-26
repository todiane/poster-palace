from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
     # make rating required and limit the range from 1 to 5
    rating = forms.FloatField(required=True, min_value=1, max_value=5)
    class Meta:
        model = Reviews
        fields = ['subject', 'review', 'rating']