# CONTACT app idea from https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid

from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)  # Save the form data to a variable
            contact.save()
            return render(request, 'contact/contact_success.html', {'contact': contact})  # Pass the contact data to the template
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)