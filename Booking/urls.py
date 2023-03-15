from django.urls import path
from Booking import views

urlpatterns = [
    
    # students
    path('guestroom', views.guestroom, name='guestroom'),
    path('sports_equipments', views.sports_equipments, name='sports_equipments'),
    path('courts', views.courts_book, name='courts_book'),
    
    # hall manager
    path('booking_manager', views.booking_manager, name='booking_manager'),
    
    # sports secy
    path('secy_request_validation', views.secy_request_validation, name='secy_request_validation'),
    path('secy_return_validation', views.secy_return_validation, name='secy_return_validation'),
    path('secy_add_equipment', views.secy_add_equipment, name='secy_add_equipment')
    # path('return_request_initiate', views.return_request_initiate, name='return_request_initiate')
]