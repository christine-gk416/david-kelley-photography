from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

def about(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        redirect_to = request.REQUEST.get('next', '')
        if form.is_valid():
            subject = "Website Enquiry" 
            body = {
            'name': form.cleaned_data['name'],
            'subject': form.cleaned_data['subject'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com',['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(redirect_to)
    form = ContactForm()
    return render(request, "about/about.html", {'form': form})
