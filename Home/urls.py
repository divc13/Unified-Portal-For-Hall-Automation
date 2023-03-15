from django.urls import path
from . import views

urlpatterns = [

    path ('', views.Make_Homepage, name = 'Home')  ,
]