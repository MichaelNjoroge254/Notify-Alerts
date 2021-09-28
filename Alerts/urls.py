from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView


urlpatterns = [
  path('', views.profile, name='uprofile'),
  path('index/', views.index, name='home'),  
  path('search/', views.search, name='search'),
  path('ajax/search/', views.searchajax, name='searchajax'),
  path('accounts/login/',LoginView.as_view(template_name='django_registration/login.html')),
  path('accounts/register/',RegistrationView.as_view(template_name='django_registration/registration_form.html')),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  