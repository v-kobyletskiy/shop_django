from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderItem
from .forms import UserLoginForm, UserRegisterForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, you are now logged in')

                if session_key:
                    # delete old authorized user carts
                    forgot_carts = Cart.objects.filter(user=user)
                    if forgot_carts.exists():
                        forgot_carts.delete()
                    # add new authorized user carts from anonymous session
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('home:home'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Authorization',
        'form': form,
    }
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f'{user.username}, you are registered and logged in')
            return HttpResponseRedirect(reverse('home:home'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Home - Register',
        'form': form,
    }
    return render(request, 'register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = (Order.objects.filter(user=request.user)
              .prefetch_related(
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product"),
        )
    ).order_by("-id"))
    context = {
        'title': 'Home - Profile',
        'form': form,
        'orders': orders,
    }
    return render(request, 'profile.html', context)


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, you are now logged out')
    auth.logout(request)
    return redirect(reverse('home:home'))


def users_cart(request):
    return render(request, 'users-cart.html')
