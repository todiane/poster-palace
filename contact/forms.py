from django import forms
from django.forms import ModelForm
from .models import Contact, User


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["contact_purpose", "name", "email", "phone", "message"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(ContactForm, self).__init__(*args, **kwargs)

        # Check if user is authenticated
        if user and user.is_authenticated:
            # If user is logged in - email field is hidden
            self.fields["email"].required = False
            self.fields["email"].widget = forms.HiddenInput()
            if "user" in self.fields:
                self.fields["user"].required = False
                self.fields["user"].widget = forms.HiddenInput()

            # Set the user instance for saving later
            self.instance.user = user
        else:
            # If the user is not logged in - email field required
            self.fields["email"].required = True
