from . import views
from django.urls import path

urlpatterns = [
    path('', views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('login/',views.user_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
]