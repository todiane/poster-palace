from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from .models import About
from products.models import Product


def index(request):
    """View to return index page"""

    recent_products = Product.objects.all()[:3]

    return render(request, "home/index.html", {"products": recent_products})


def about_pp(request):
    """View to return About Us page"""

    about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "home/about.html",
        {"about": about},
    )
