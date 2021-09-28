"""Notify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView
# from Alerts.views import *

urlpatterns = [
    path('', include('Alerts.urls')),
    path('admin/', admin.site.urls),    
    #  path('accounts/login/',
    #      RegistrationView.as_view(success_url='/'),
    #     name='django_registration_register'),
    path('accounts/login/',LoginView.as_view(template_name='django_registration/login.html')),
    path('accounts/register/',RegistrationView.as_view(template_name='django_registration/registration_form.html')),
    path('accounts', include('registration.backends.simple.urls')),
    path('accounts', include('django.contrib.auth.urls')),
]
