from django.shortcuts import render


""" Error handling """


def handler403(request, exception):
    """Render 403 page - Permission denied"""
    return render(request, 'errors/403.html', status=403)


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "errors/500.html", status=500)
