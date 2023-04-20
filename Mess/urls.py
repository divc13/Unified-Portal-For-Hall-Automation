from django.urls import path
from . import views

urlpatterns = [
    
    # student
    path('Student_Regular_Menu', views.Student_Regular_Menu, name='Student_Regular_Menu'),
    path('Student_Book_Extras', views.Student_Book_Extras, name='Student_Book_Extras'),
    path('Student_Booked_Extras', views.Student_Booked_Extras, name='Student_Booked_Extras'),
    path('Student_Apply_For_Rebate', views.Student_Apply_For_Rebate, name='Student_Apply_For_Rebate'),
    path('Student_Order_History', views.Student_Order_History, name='Student_Order_History'),
    path('Student_Applied_Rebate',views.Student_Applied_Rebate,name = 'Student_Applied_Rebate'),
    
    # manager
    path('Manager_Extra_Items', views.Manager_Extra_Items, name='Manager_Extra_Items'),
    path('Manager_Modify_Menu', views.Manager_Modify_Menu, name='Manager_Modify_Menu'),
    path('Manager_View_Feedback', views.Manager_View_Feedback, name='Manager_View_Feedback'),
    path('Manager_Rebate_Requests', views.Manager_Rebate_Requests, name='Manager_Rebate_Requests'),
    path('Manager_Students_Bills', views.Manager_Students_Bills, name='Manager_Students_Bills'),
    path('Manager_View_Orders', views.Manager_View_Orders, name='Manager_View_Orders'),
    path('Manager_Modify_BDMR', views.Manager_Modify_BDMR, name='Manager_Modify_BDMR'),
    path('Manager_Past_Rebate',views.Manager_Past_Rebate,name='Manager_Past_Rebate'),
]