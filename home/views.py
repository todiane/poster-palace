from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from .models import About


def index(request):
    """ View to return index page """

    return render(request, 'home/index.html')


def about_pp(request):
    """View to return About poster palace (pp) page"""

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "home/about.html",
        {"about": about},
    )
