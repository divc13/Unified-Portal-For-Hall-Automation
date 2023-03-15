from django.urls import path
from . import views

urlpatterns = [
    
    # student
    path('Student_Place_Order', views.Student_Place_Order, name='Student_Place_Order'),
    path('Student_Cart', views.Student_Cart, name='Student_Cart'),
    path('Student_Pending_Order', views.Student_Pending_Order, name='Student_Pending_Order'),
    path('Student_Orders_History', views.Student_Orders_History, name='Student_Orders_History'),
    
    # owner
    path('Owner_New_Order', views.Owner_New_Order, name='Owner_New_Order'),
    path('Owner_Pending_Order', views.Owner_Pending_Order, name='Owner_Pending_Order'),
    path('Owner_Modify_Menu', views.Owner_Modify_Menu, name='Owner_Modify_Menu'),
    path('Owner_Students_Bill', views.Owner_Students_Bill, name='Owner_Students_Bill'),
]