from django.shortcuts import render


def subscription(request):
    """ View to return subscriptions page """

    return render(request, "marketing/subscriptions.html")


def poster_event(request):
    """ View to return the Diverse Design events page """

    return render(request, "marketing/poster_event.html")


def event_terms(request):
    """ View to return the terms & conditions page for event """

    return render(request, "marketing/event_terms.html")
