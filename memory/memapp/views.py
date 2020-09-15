from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, CreateTaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .services import (
    get_current_user_task_by_id_serves,
    create_task_form_serves,
    register_form_serves,
    login_form_serves
)


def home_view(request):
    return render(request, 'memapp/home.html')


def register_view(request):
    context = {}
    form = register_form_serves(request, RegistrationForm)
    context['form'] = form
    return render(request, 'memapp/registration.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}
    form = login_form_serves(request, LoginForm, context)
    context['form'] = form
    return render(request, 'memapp/login.html', context)


@login_required
def account_view(request):
    return render(request, 'memapp/account.html')


@login_required
def create_task_view(request):
    context = {}
    form = create_task_form_serves(request, CreateTaskForm)
    context['form'] = form
    return render(request, 'memapp/create_task.html', context)


@login_required
def task_view(request, task_id):
    context = {}
    task = get_current_user_task_by_id_serves(request, task_id)
    context['task'] = task
    return render(request, 'memapp/task.html', context)


def test_view(request):
    return redirect('home')