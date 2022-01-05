from django.urls import path, include

from core.views import (
    register, 
    profile, 
    home_view
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('home/', home_view, name='home' ),    
]

