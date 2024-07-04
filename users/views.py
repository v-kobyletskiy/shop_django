from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home:home'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Authorization',
        'form': form,
    }
    return render(request, 'login.html', context)


def register(request):
    context = {
        'title': 'Home - Register'
    }
    return render(request, 'register.html', context)


def profile(request):
    context = {
        'title': 'Home - Profile'
    }
    return render(request, 'profile.html', context)


def logout(request):
    ...

