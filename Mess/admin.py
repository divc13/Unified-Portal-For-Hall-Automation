from django.contrib import admin
from Mess.models import Regular_menu
from Mess.models import Extras
from Mess.models import Orders
from Mess.models import Rebate
from Mess.models import Bill
from Mess.models import Datewise_BDMR
from Mess.models import Rating_Regular

# Register your models here.
admin.site.register(Datewise_BDMR)
admin.site.register(Regular_menu)
admin.site.register(Extras)
admin.site.register(Orders)
admin.site.register(Rebate)
admin.site.register(Bill)
admin.site.register(Rating_Regular)