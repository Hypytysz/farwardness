from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages

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
    return render(request, 'accounts/homepage.html', context)