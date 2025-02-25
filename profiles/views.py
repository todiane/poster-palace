from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BuyerProfile
from .forms import BuyerProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """Display a user's profile"""
    profile = get_object_or_404(BuyerProfile, user=request.user)

    if request.method == "POST":
        form = BuyerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, "Failed to update profile, please check your form for errors."
            )
    else:
        form = BuyerProfileForm(instance=profile)

    orders = profile.orders.all()
    template = "profiles/profile.html"
    context = {
        "form": form,
        "default_full_name": profile.default_full_name,
        "orders": orders,
        "on_profile_page": True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}."
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
