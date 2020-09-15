import datetime
from django.contrib.auth import authenticate, login, logout


def get_current_user_task_by_id_serves(request, task_id):
    """returns object from task related with current user"""
    return request.user.tasks.get(id=task_id)


def base_form_serves(request, form_class):
    if request.POST:
        form_to_return = form_class(request.POST)
    else:
        form_to_return = form_class()
    return request, form_to_return


def create_task_form_serves(request, form_class):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            theme = form.cleaned_data.get('theme')
            text = form.cleaned_data.get('text')
            request.user.tasks.create(theme=theme, text=text, last_update=datetime.datetime.now())
    else:
        form = form_class()
    return form


def register_form_serves(request, form_class):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = form_class()
    return form


def login_form_serves(request, form_class, context):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return form
            else:
                context['error'] = 'no such user'
    else:
        form = form_class()
    return form
