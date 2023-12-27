from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)

        # Check if user is authenticated
        if user and user.is_authenticated:
            # If the user is logged in - email field not required/widget is hidden
            self.fields['email'].required = False
            self.fields['email'].widget = forms.HiddenInput()
        else:
            # If the user is not logged in - email field required
            self.fields['email'].required = True
