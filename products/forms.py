from django import forms
from .models import Reviews
from django.core.exceptions import ValidationError

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['rating'].required = True
        self.fields['rating'].error_messages = {'required': 'Please select a rating'}

    class Meta:
        model = Reviews
        fields = ["subject", "review", "rating"]

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get('subject')
        review = cleaned_data.get('review')
        rating = cleaned_data.get('rating')

        if not subject:
            raise ValidationError("Subject is a required field")

        if not review:
            raise ValidationError("Review is a required field")

        if not rating:
            raise ValidationError("Rating is a required field")