from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('test', views.test_view, name='test'),
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('account', views.account_view, name='account'),
    path('create_task', views.create_task_view, name='create_task'),
    path('task/<int:task_id>', views.task_view, name='task'),
    path('create_contact', views.create_contact_view, name='create_contact'),
    path('contact/<int:contact_id>', views.contact_view, name='contact')
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
