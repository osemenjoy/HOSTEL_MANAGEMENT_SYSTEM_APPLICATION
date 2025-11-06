from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import MatricAuthenticationForm

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/overview/', views.overview, name='overview'),
    path('dashboard/my-room/', views.my_room, name='my_room'),
    path('dashboard/request-room/', views.request_room, name='request_room'),
    path('dashboard/maintenance/', views.maintenance, name='maintenance'),
    path('dashboard/payments/', views.payments, name='payments'),
    path('dashboard/notices/', views.notices, name='notices'),
    path('dashboard/profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=MatricAuthenticationForm, template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
