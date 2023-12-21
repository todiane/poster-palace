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



""" Error handling """


def handler404(request, exception):
    """Rendering the 404 page."""
    return render(request, '404.html', status=404)


def handler500(request):
    """Rendering the 500 page."""
    return render(request, '500.html', status=500)


def handler403(request, exception):
    """Rendering the 403 page."""
    if isinstance(exception, PermissionDenied):
        return render(request, '403.html', status=403)
    else:
        # Handle unexpected errors with a generic 500 error page
        return render(request, '500.html', status=500)