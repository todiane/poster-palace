# CONTACT app idea from 
# https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid

from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        if form.is_valid():
            contact = form.save(commit=False)

            # If the user is authenticated, set the contact's email to the user's email
            if request.user.is_authenticated:
                contact.email = request.user.email

            contact.save()
            return render(request, 'contact/contact_success.html', {'contact': contact})
    else:
        form = ContactForm(user=request.user)
    
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
