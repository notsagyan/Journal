import django
from .views import *
from django.urls import path, include

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name = 'auth-register'),
    path('auth/login/', LoginView.as_view(), name = 'auth-login'),
    path('auth/logout/', LogoutView.as_view(), name = 'auth-logout'),
    path('auth/', include('django.contrib.auth.urls')),
]