from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "contact_purpose",
        "get_user_name",
        "email",
        "name",
        "phone",
        "message",
        "date_submitted",
    ]
    list_filter = ["name", "date_submitted"]

    def get_user_name(self, obj):
        return obj.user.username if obj.user else ""  # Display username if user exists

    get_user_name.short_description = "User Name"  
