from django import forms
from .models import BuyerProfile


class BuyerProfileForm(forms.ModelForm):
    """Create profile form for buyers"""

    class Meta:
        model = BuyerProfile
        fields = [
            "default_street_address1",
            "default_street_address2",
            "default_town_or_city",
            "default_county",
            "default_postcode",
            "default_country",
            "default_phone_number",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_town_or_city": "Town or City",
            "default_county": "County, State or Locality",
            "default_postcode": "Postal Code",
            "default_country": "Country",
            "default_phone_number": "Phone Number",
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"
            self.fields[field].label = False
