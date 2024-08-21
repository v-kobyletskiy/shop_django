from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from carts.models import Cart
from orders.models import Order, OrderItem
from .forms import UserLoginForm, UserRegisterForm, ProfileForm


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    # success_url = reverse_lazy('home:home')

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('home:home')

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()

        if user:
            auth.login(self.request, user)
            if session_key:
                # delete old authorized user carts
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                # add new authorized user carts from anonymous session
                Cart.objects.filter(session_key=session_key).update(user=user)

                messages.success(self.request, f'{user.username}, you are now logged in')

                return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Authorization'
        return context


class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:profile')

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance

        if user:
            form.save()
            auth.login(self.request, user)

        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(self.request, f'{user.username}, you are registered and logged in')
        return HttpResponseRedirect(self.success_url)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Register'
        return context


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error occurs')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Profile'
        context['orders'] = (Order.objects.filter(user=self.request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id"))
        return context


class UserCartView(TemplateView):
    template_name = 'users-cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Cart'
        return context

# def users_cart(request):
#     return render(request, 'users-cart.html')


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully')
#             return HttpResponseRedirect(reverse('user:profile'))
#     else:
#         form = ProfileForm(instance=request.user)
#
#     orders = (Order.objects.filter(user=request.user)
#               .prefetch_related(
#         Prefetch(
#             "orderitem_set",
#             queryset=OrderItem.objects.select_related("product"),
#         )
#     ).order_by("-id"))
#     context = {
#         'title': 'Home - Profile',
#         'form': form,
#         'orders': orders,
#     }
#     return render(request, 'profile.html', context)


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, you are now logged out')
    auth.logout(request)
    return redirect(reverse('home:home'))


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#
#             session_key = request.session.session_key
#
#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f'{username}, you are now logged in')
#
#                 if session_key:
#                     # delete old authorized user carts
#                     forgot_carts = Cart.objects.filter(user=user)
#                     if forgot_carts.exists():
#                         forgot_carts.delete()
#                     # add new authorized user carts from anonymous session
#                     Cart.objects.filter(session_key=session_key).update(user=user)
#
#                 redirect_page = request.POST.get('next', None)
#                 if redirect_page and redirect_page != reverse('user:logout'):
#                     return HttpResponseRedirect(request.POST.get('next'))
#
#                 return HttpResponseRedirect(reverse('home:home'))
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'title': 'Home - Authorization',
#         'form': form,
#     }
#     return render(request, 'login.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#
#             session_key = request.session.session_key
#
#             user = form.instance
#             auth.login(request, user)
#
#             if session_key:
#                 Cart.objects.filter(session_key=session_key).update(user=user)
#
#             messages.success(request, f'{user.username}, you are registered and logged in')
#             return HttpResponseRedirect(reverse('home:home'))
#     else:
#         form = UserRegisterForm()
#
#     context = {
#         'title': 'Home - Register',
#         'form': form,
#     }
#     return render(request, 'register.html', context)