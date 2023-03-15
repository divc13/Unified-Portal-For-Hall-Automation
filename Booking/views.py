from django.shortcuts import render, HttpResponse
from datetime import datetime
from Booking.models import Guestroom,sports_equipments_request,Courts,sports_equipments_registered,sports_equipmnents_store

# Create your views here.
 
def guestroom(request): #student
    if request.user.is_authenticated:
        if request.user.designation == "Student" :
            context = {}
            #let's keep the booking logs updated
            today = datetime.today().date()
            rooms = Guestroom.objects.all()
            for room in rooms:
                out_date = room.checkout_date
                if(today>out_date):
                    room.delete()

            #This codes will tackle when the request of booking is made
            if request.method == "POST":
                room = request.POST.get('room')
                checkin_date = request.POST.get('checkin_date')
                checkout_date = request.POST.get('checkout_date')
                price = request.POST.get('price')

                rooms = Guestroom.objects.filter(room=room)
                if(len(rooms)>0):
                    flag=1
                    for room_item in rooms:
                        in_date = room_item.checkin_date
                        out_date = room_item.checkout_date

                        request_in_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
                        request_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()
                        

                        if (request_in_date>=in_date and request_in_date<=out_date) or (request_out_date>=in_date and request_out_date<=out_date):
                            flag=0
                            break

                    if flag==1:
                        guestroom_request = Guestroom(checkin_date = checkin_date, checkout_date = checkout_date, price=price,
                                            date=datetime.today(),name=request.user.name,username=request.user.username,room=room)
                        
                        guestroom_request.save()
                        return render(request,'guestroom.html',context)
                    else:
                        rooms=Guestroom.objects.filter(room=room)
                        for room in rooms:
                            room_r=room
                            break
                        return HttpResponse(f'Those dates clash with another reservation as this room booked between {room_r.checkin_date} and {room_r.checkout_date}.\nPlease go back and try another date or another room.\n UPHA team highly regrets your inconvenience')
                    
                else:
                    guestroom_request = Guestroom(checkin_date = checkin_date, checkout_date = checkout_date, price=price,
                                            date=datetime.today(),name=request.user.name,username=request.user.username,room=room)
                        
                    guestroom_request.save()
                
            return render(request,'guestroom.html',context)
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")    
    
        
def sports_equipments(request): #student\
    if request.user.designation == "Student" :
        context = {
            'cricket_item':sports_equipments_registered.objects.get(equipments='CB'),
            'table_tennis_item':sports_equipments_registered.objects.get(equipments='TT'),
            'badminton_item':sports_equipments_registered.objects.get(equipments='BM'),
            'hockey_item':sports_equipments_registered.objects.get(equipments='HK'),
            'basketball_item':sports_equipments_registered.objects.get(equipments='BB'),
            'football_item':sports_equipments_registered.objects.get(equipments='FB'),
            
            'request_querry':sports_equipments_request.objects.filter(username=request.user.username,secy_validation='NO'),
            'validated_request_querry':sports_equipments_request.objects.filter(username=request.user.username,secy_validation='YES')
        }

        if request.method =="POST":
            
            action = request.POST.get("submit")
            if (action == "Return Item"): #
                return_equipment = request.POST.get('return_equipment')
                # return_item_check = sports_equipments_request.objects.filter(equipment_selected = return_equipment,username=request.user.username)
                # if (return_item_check): 
                #     pass
                # else:
                item_of_return = sports_equipments_request.objects.get(equipment_selected = return_equipment,username=request.user.username)
                # number_of_items = len(items_of_return)
                item_of_return.student_return_request='YES'
                item_of_return.save()
            
            else:
                equipment_selected_get = request.POST.get("equipment_selected")
                check_requested_item = sports_equipments_request.objects.filter(username=request.user.username,equipment_selected=equipment_selected_get)
                if (check_requested_item):
                    pass
                else:    
                    equipment_request = sports_equipments_request(equipment_selected=equipment_selected_get,date=datetime.today(),
                                                                name=request.user.name,username=request.user.username,argument = equipment_selected_get+'_'+str(request.user.name))
                    equipment_request.save()


        return render(request,'sports_equipments.html',context)
    else:
        return render(request,"Error.html")

def courts_book(request): #student
    if request.user.designation == "Student" :
        context ={
            'var_date' : str(datetime.today()),
            'var_time' : str(datetime.now().time())
        }
        today = datetime.today().date()
        court_items = Courts.objects.all().filter(day_of_booking = today)
        time = datetime.now().time()
        for court in court_items:
            out_time = court.time_of_checkout
            if(time>out_time):
                court.delete()

        if request.method =='POST':
            sports = request.POST.get('sport')
            checkin_time = request.POST.get('checkin_time')
            checkout_time = request.POST.get('checkout_time')
            date = request.POST.get('date')

            #This codes will tackle when the request of booking is mad
            court_items = Courts.objects.filter(sports=sports)
            if(len(court_items)>0):
                flag=1
                for court_item in court_items:
                    in_time = court_item.time_of_checkin
                    out_time = court_item.time_of_checkout
                    day = court_item.day_of_booking

                    request_in_time = datetime.strptime(checkin_time, "%Y-%m-%d").time()
                    request_out_time = datetime.strptime(checkout_time, "%Y-%m-%d").time()
                    request_date = datetime.strptime(date, "%Y-%m-%d").date()
                    
                    if(request_date == day):
                        if (request_in_time>=in_time and request_in_time<=out_time) or (request_out_time>=in_time and request_out_time<=out_time):
                            flag=0
                            break

                if flag==1:
                    courts_request = Courts(sports=sports, time_of_checkin = checkin_time, time_of_checkout = checkout_time, day_of_booking = date,
                                    date=datetime.today(), name=request.user.name,username=request.user.username)
                    courts_request.save()
                    return render(request,'courts.html',context)
                else:
                    courts=Courts.objects.filter(sports=sports)
                    for court in courts:
                        court_r=court
                        break
                    return HttpResponse(f'Those date-time clash with another booking of good as this room booked between {court_r.time_of_checkin} and {court_r.time_of_checkout}.\nPlease go back and try another date or another room.\n UPHA team highly regrets your inconvenience')
                
            else:
                courts_request = Courts(sports=sports, time_of_checkin = checkin_time, time_of_checkout = checkout_time, day_of_booking = date,
                                    date=datetime.today(), name=request.user.name,username=request.user.username)
                courts_request.save()

            
        return render(request,'courts.html',context)
    else:
        return render(request,"Error.html")

def booking_manager(request): #hall manager
    if request.user.designation == "Hall Manager":
        context = {
            'query_results' : Guestroom.objects.all()
        }
        
        return render(request,'booking_manager.html',context)
    else:
        return render(request,"Error.html")
#sports secy functions
def secy_request_validation(request):
    if request.user.is_authenticated:
        if request.user.designation == "Sports Secy":
            context ={
                'querry':sports_equipments_request.objects.all().filter(secy_validation='NO')
            }
            if request.method=="POST":
                requester_username=request.POST.get('requester_username')
                item_requested=request.POST.get('item_requested')
                secy_action=request.POST.get('action')
                if (secy_action == "validated"):
                    item=sports_equipments_request.objects.get(equipment_selected = item_requested,username=requester_username) 
                    item.secy_validation='YES'
                    item.save()   

                    reg_item = sports_equipments_registered.objects.get(equipments= item_requested)
                    reg_item.quantity = reg_item.quantity-1
                    reg_item.save()
                else:
                    item=sports_equipments_request.objects.get(equipment_selected = item_requested,username=requester_username)
                    item.delete()
                
            return render(request,'secy_validate_request.html',context)
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")

def secy_return_validation(request):
    if request.user.is_authenticated:
        if request.user.designation == "Sports Secy":
            context ={
                'querry':sports_equipments_request.objects.all().filter(student_return_request='YES')
            }

            if request.method == 'POST':
                returner_roll = request.POST.get('returner_roll')
                item_returning = request.POST.get('item_returning')

                item = sports_equipments_request.objects.get(equipment_selected=item_returning,username=returner_roll)
                item.delete()
                reg_item = sports_equipments_registered.objects.get(equipments=item_returning)
                reg_item.quantity = reg_item.quantity + 1
                reg_item.save()
            return render(request,'secy_validate_return.html',context)
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")

def secy_add_equipment(request):
    if request.user.is_authenticated:
        if request.user.designation == "Sports Secy":
            if request.method=='POST':
                sport_selected =request.POST.get('sport')
                equipment_quantity = request.POST.get('equipment_quantity')

                sport_store = sports_equipmnents_store.objects.get(equipments_store=sport_selected)
                sport_store.quantity_store = sport_store.quantity_store+ int(equipment_quantity)
                sport_store.save()

                sport_reg = sports_equipments_registered.objects.get(equipments=sport_selected)
                sport_reg.quantity = sport_reg.quantity+ int(equipment_quantity)
                sport_reg.save()

            return render(request,'secy_add_equipments.html')
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")


# def return_request_initiate(request):
#     if request.user.is_authenticated:
#         if request.user.designation == "Student":
#             if request.method=='POST':
#                 return_equipment = request.POST.get('return_equipment')
#                 return_item_check = sports_equipments_request.objects.filter(equipment_selected = return_equipment,username=request.user.username)
#                 if (return_item_check): 
#                     pass
#                 else:
#                     item_of_return = sports_equipments_request.objects.get(equipment_selected = return_equipment,username=request.user.username)
#                     # number_of_items = len(items_of_return)
#                     item_of_return.student_return_request='YES'
#                     item_of_return.save()
#             return render(request,'sports_equipments.html')   
#         else: 
#             return render(request,"Error.html")
#     else:
#         return render(request,"Error.html")