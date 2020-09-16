from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, CreateTaskForm, CreateContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .services import (
    get_current_user_task_by_id_serves,
    create_task_form_serves,
    register_form_serves,
    login_form_serves,
    create_contact_form_serves,
    get_current_contact
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


@login_required
def create_contact_view(request):
    context = {}
    form = create_contact_form_serves(request, CreateContactForm)
    context['form'] = form
    return render(request, 'memapp/create_contact.html', context)


@login_required
def contact_view(request, contact_id):
    context = {}
    contact = get_current_contact(request, contact_id)
    context['contact'] = contact
    return render(request, 'memapp/contact.html', context)