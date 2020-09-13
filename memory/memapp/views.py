from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'memapp/home.html')


@login_required
def register_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #####
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=password)
            #####
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, 'memapp/registration.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            context['error'] = 'no such user'
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'memapp/login.html', context)


@login_required
def account_view(request):
    return render(request, 'memapp/account.html')


@login_required
def create_task_view(request):

