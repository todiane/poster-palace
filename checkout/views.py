from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):

    bag = request.session.get('bag', {})
    if not bag:
            messages.error(request, (
                "You don't have any items in your bag."))
            return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51M9aRBHzrsg64asgW5x1JDTKE4yzz4zophMuurdnE2UoyPGprnIJYykPDXAWeTXck67YOk77vFylYFVkJde8TiLX00tlCkrSn9',
  
    }

    return render(request, template, context)