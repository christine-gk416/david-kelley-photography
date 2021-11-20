from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactForm


def about(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            """Add form submission to database and
            send form content to site owner email address """
            email_subject = f'New contact from {form.cleaned_data["name"]} \
            at {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            send_mail(email_subject, email_message,
                      sender, ['david.kelley.photos@gmail.com'])
            form.save()

            # Show a message if the form goes through
            messages.success(request,
                             "Thanks for your message! \
                             We'll be in touch soon.")
            return redirect('about')
        else:
            # Throw an error message if the form doesn't go through
            messages.error(request,
                           'Message send failed. \
                            Please ensure the form is valid.')
            return render(request, 'about/about.html')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, "about/about.html", context)
