from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['rating'].required = True
        self.fields['rating'].error_messages = {'required': 'Please select a rating'}

    class Meta:
        model = Reviews
        fields = ["subject", "review", "rating"]

        