from django.shortcuts import render, redirect
from .forms import SubFrom
from .models import Sub
from . models import Newsletter
from django.contrib import messages
from .forms import NewsletterForm
from django.http import HttpResponse
from .management.commands.send_newsletter_file import send_newsletter
from .forms import NewsletterSendForm





def subscribe(request):
    if request.method == 'POST':
        
        form = SubFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your subscription')
            return redirect('SubSuccess')
        else:
            messages.error(request, 'There was a problem with your subscription')
    else:
        form = SubFrom()
    return render(request, 'subscribe.html', {'form': form})

def Create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('NewsletterSuccess')  # Redirect to the home page or success page after saving
    else:
        form = NewsletterForm()
    
    return render(request, 'create_newsletter.html', {'form': form})

def SubSuccess(request):
    return render(request, 'SubSuccess.html')

def NewsletterSuccess(request):
    return render(request, 'NewsletterSuccess.html')

def SendNewsletterView(request):
    if request.method == 'POST':
        form = NewsletterSendForm(request.POST)
        if form.is_valid():
            newsletter = form.cleaned_data['newsletter']
            send_newsletter(newsletter.id)  # Call the function correctly
            messages.success(request, f'Newsletter {newsletter.id} has been sent successfully!')
            return redirect('send_newsletter')
    else:
        form = NewsletterSendForm()

    return render(request, 'send_newsletter.html', {'form': form})




    
    