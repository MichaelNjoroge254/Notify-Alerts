from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView


urlpatterns = [
  path('', views.profile, name='uprofile'),
  path('index/', views.index, name='home'),  
  # path('accounts/register/',
  #        RegistrationView.as_view(success_url='accounts/login'),
  #       name='django_registration_register'),
  path('accounts/login/',LoginView.as_view(template_name='django_registration/login.html')),
  path('accounts/register/',RegistrationView.as_view(template_name='django_registration/registration_form.html')),
  path('accounts', include('registration.backends.simple.urls')),
  path('accounts', include('django.contrib.auth.urls')),
  path('search/', views.search, name='search'),
  path('ajax/search/', views.searchajax, name='searchajax'),
 
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  