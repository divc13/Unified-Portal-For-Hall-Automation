from django.urls import path
from . import views

urlpatterns = [
    
    # common
    path('', views.Login, name='Login'),
    path('Login', views.Login, name='Login'),
    path('Set_Password', views.Set_Password, name='Set_Password'),
    path('Reset_Password', views.Reset_Password, name='Reset_Password'),
    path('SignUp', views.SignUp, name="SignUp"),
    path("OTP", views.OTP, name="OTP"),
    path("Logout", views.Logout, name="Logout")
]