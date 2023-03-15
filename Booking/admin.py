from django.contrib import admin
from Booking.models import Guestroom,Courts,sports_equipments_registered,sports_equipments_request,sports_equipmnents_store

# Register your models here.
admin.site.register(Guestroom)
admin.site.register(Courts)
admin.site.register(sports_equipments_registered)
admin.site.register(sports_equipments_request)
admin.site.register(sports_equipmnents_store)

