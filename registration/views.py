import os

from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + user + '!')
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def homepage(request):
    context = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        budget = request.POST['budget']
        message = request.POST['message']
        send_mail(
            name, # subject
            message + ' phone: ' +phone + ' budget: ' + budget, # messege
            email, # from email
            [os.getenv('EMAIL')], # to email
        )
        return render(request, 'accounts/homepage.html', {'name':name, 'email':email, 'message':message, 'phone':phone, 'budget':budget})
    else:
        return render(request, 'accounts/homepage.html', context)
