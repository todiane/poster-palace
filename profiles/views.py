from django.shortcuts import render, get_object_or_404

from .models import BuyerProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(BuyerProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)