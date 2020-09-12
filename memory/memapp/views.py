from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'memapp/home.html')


def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        print('not valid')
        return render(request, 'memapp/registration.html', context)
    else:
        form = RegistrationForm()
        context['form'] = form
        return render(request, 'memapp/registration.html', context)
