from django.urls import path
from . import views

urlpatterns = [
    path('Mess', views.Mess, name='Mess'),
    path('Canteen', views.Canteen, name='Canteen'),
] 