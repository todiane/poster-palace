from django.shortcuts import render


def subscription(request):
    """ View to return subscriptions page """
 
    return render(request, "marketing/subscriptions.html")

