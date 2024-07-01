from django.shortcuts import render


def login(request):
    context = {
        'title': 'Home - Authorization'
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

