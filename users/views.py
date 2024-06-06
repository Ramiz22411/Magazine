from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from cart.models import Cart

from .forms import UserForm, RegisterForm, ProfileForm
from orders.models import Order, OrderItem


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, You have successfully login')

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('users:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('myapp:index'))
    else:
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, You have successfully register your profile')

            if session_key:
                Cart.oblects.filter(session_key=session_key).update(user=user)

            if request.POST.get('next', None):
                return HttpResponseRedirect(request.POST.get('next'))
            return HttpResponseRedirect(reverse('myapp:index'))
    else:
        form = RegisterForm()

    template = 'users/registration.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required()
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully update your profile')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = RegisterForm(instance=request.user)

    orders = Order.objects.filter(user=request.user).prefetch_related(
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product"),
        )
    ).order_by("-id")

    template = 'users/profile.html'
    context = {
        "form": form,
        'orders': orders
    }
    return render(request, template, context)


@login_required()
def logout_user(request):
    messages.success(request, f'{request.user.username} You have successfully logged out')
    auth.logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))


def users_cart(request):
    return render(request, 'cart/cart.html')
