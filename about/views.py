from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def about(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact from {form.cleaned_data["name"]} at {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            recipient = form.cleaned_data['email']
            send_mail(email_subject, email_message, recipient,['settings.ADMIN_EMAIL'])
            form.save()
            messages.success(request, "Thanks for your message! We'll be in touch soon.")
            return redirect('about')
        else:
            messages.error(request, 'Message send failed. Please ensure the form is valid.')
            return render(request, 'about/about.html')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, "about/about.html", context)
