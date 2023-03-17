from django.shortcuts import render, HttpResponse
from datetime import datetime
from Booking.models import Guestroom,sports_equipments_request,Courts,sports_equipments_registered,sports_equipmnents_store
from django.contrib import messages

# Create your views here.
 
def guestroom(request): #student
    if request.user.is_authenticated:
        if request.user.designation == "Student" :
            context = {
                'messages' : messages.get_messages(request)
            }
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

                request_in_date = datetime.strptime(checkin_date, "%Y-%m-%d").date()
                request_out_date = datetime.strptime(checkout_date, "%Y-%m-%d").date()

                if (request_in_date<request_out_date and request_in_date>=today):
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
                            messages.success(request, f'Your request for this room has been sent to the Hall manager, UPHA team will communicate their confirmation to you.')
                            return render(request,'guestroom.html',context)
                        else:
                            rooms=Guestroom.objects.filter(room=room)
                            for room in rooms:
                                room_r=room
                                break
                            messages.error(request, f'The room you have requested is already booked from {room_r.checkin_date} to {room_r.checkout_date}. UPHA team highly regrets the inconvenience caused.')
                            return render(request,'guestroom.html',context)
                    else:
                        guestroom_request = Guestroom(checkin_date = checkin_date, checkout_date = checkout_date, price=price,
                                                date=datetime.today(),name=request.user.name,username=request.user.username,room=room)
                            
                        guestroom_request.save()
                        messages.success(request, f'Your request for this room has been sent to the Hall manager, Please reach out to him for further details.')

                else:
                    if(request_in_date>today):
                        messages.error(request, f'Checkin date can not be after checkout date, please enter dates correctly again.')
                    else:
                        messages.error(request, f'Checkin date can not be before today, please enter dates correctly again.')
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
            'validated_request_querry':sports_equipments_request.objects.filter(username=request.user.username,secy_validation='YES'),
            'messages' : messages.get_messages(request)
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
                messages.success(request, f'Your request for returning this item has been sent to the secretary.')
            
            else:
                equipment_selected_get = request.POST.get("equipment_selected")
                check_requested_item = sports_equipments_request.objects.filter(username=request.user.username,equipment_selected=equipment_selected_get)
                if (check_requested_item):
                    messages.error(request, f'You have already requested for this item.')
                    pass
                else:    
                    equipment_request = sports_equipments_request(equipment_selected=equipment_selected_get,date=datetime.today(),
                                                                name=request.user.name,username=request.user.username,argument = equipment_selected_get+'_'+str(request.user.name))
                    equipment_request.save()
                    messages.success(request, f'Your request for this item has been sent to the secretary.')


        return render(request,'sports_equipments.html',context)
    else:
        return render(request,"Error.html")

def courts_book(request): #student
    if request.user.designation == "Student" :
        context ={
            'var_date' : str(datetime.today()),
            'var_time' : str(datetime.now().time()),
            'messages' : messages.get_messages(request)
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

            request_in_time = datetime.strptime(checkin_time, "%H:%M").time()
            request_out_time = datetime.strptime(checkout_time, "%H:%M").time()
            request_date = datetime.strptime(date, "%Y-%m-%d").date()


            if(request_in_time<=request_out_time and request_date>=datetime.today().date()):
                #This codes will tackle when the request of booking is mad
                court_items = Courts.objects.filter(sports=sports)
                if(len(court_items)>0):
                    flag=1
                    for court_item in court_items:
                        in_time = court_item.time_of_checkin
                        out_time = court_item.time_of_checkout
                        day = court_item.day_of_booking

                        request_in_time = datetime.strptime(checkin_time, "%H:%M").time()
                        request_out_time = datetime.strptime(checkout_time, "%H:%M").time()
                        request_date = datetime.strptime(date, "%Y-%m-%d").date()
                        
                        if(request_date == day):
                            if (request_in_time>=in_time and request_in_time<=out_time) or (request_out_time>=in_time and request_out_time<=out_time):
                                flag=0
                                break

                    if flag==1:
                        courts_request = Courts(sports=sports, time_of_checkin = checkin_time, time_of_checkout = checkout_time, day_of_booking = date,
                                        date=datetime.today(), name=request.user.name,username=request.user.username)
                        courts_request.save()
                        messages.success(request, 'Your have succesfully booked the court, enjoy your playtime :)')
                        return render(request,'courts.html',context)
                    else:
                        courts=Courts.objects.filter(sports=sports)
                        for court in courts:
                            court_r=court
                            break
                        messages.error(request, 'The court is already booked for the given time, please try again with different time :(')
                        return render(request,'courts.html',context)                
                else:
                    courts_request = Courts(sports=sports, time_of_checkin = checkin_time, time_of_checkout = checkout_time, day_of_booking = date,
                                        date=datetime.today(), name=request.user.name,username=request.user.username)
                    courts_request.save()
                    messages.success(request, 'Your have succesfully booked the court, enjoy your playtime :)')
            else:
                if(request_date>=datetime.now().date()):
                    messages.error(request, 'The checkin time is greater than or same as checkout time, please try again with different time :(')
                else:
                    messages.error(request, 'The date is in past, please try again with different date :(')
                return render(request,'courts.html',context)
            
        return render(request,'courts.html',context)
    else:
        return render(request,"Error.html")

#sports secy functions
def secy_request_validation(request):
    if request.user.is_authenticated:
        if request.user.designation == "Sports Secy":
            context ={
                'querry':sports_equipments_request.objects.all().filter(secy_validation='NO'),
                'messages' : messages.get_messages(request)
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
                    messages.success(request, 'The request has been validated')
                else:
                    item=sports_equipments_request.objects.get(equipment_selected = item_requested,username=requester_username)
                    messages.success(request, 'The request has been rejected')
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
                'querry':sports_equipments_request.objects.all().filter(student_return_request='YES'),
                'messages' : messages.get_messages(request)
            }

            if request.method == 'POST':
                returner_roll = request.POST.get('returner_roll')
                item_returning = request.POST.get('item_returning')

                item = sports_equipments_request.objects.get(equipment_selected=item_returning,username=returner_roll)
                item.delete()
                reg_item = sports_equipments_registered.objects.get(equipments=item_returning)
                reg_item.quantity = reg_item.quantity + 1
                reg_item.save()
                messages.success(request, 'The return has been validated')
            return render(request,'secy_validate_return.html',context)
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")

def secy_add_equipment(request):
    if request.user.is_authenticated:
        if request.user.designation == "Sports Secy":
            context ={
                'message':messages.get_messages(request)
            }
            if request.method=='POST':
                sport_selected =request.POST.get('sport')
                equipment_quantity = request.POST.get('equipment_quantity')

                if (equipment_quantity >0):
                    sport_store = sports_equipmnents_store.objects.get(equipments_store=sport_selected)
                    sport_store.quantity_store = sport_store.quantity_store+ int(equipment_quantity)
                    sport_store.save()

                    sport_reg = sports_equipments_registered.objects.get(equipments=sport_selected)
                    sport_reg.quantity = sport_reg.quantity+ int(equipment_quantity)
                    sport_reg.save()
                    messages.success(request, 'The equipment has been added successfully')
                else:
                    messages.error(request, 'The quantity of equipment should be greater than 0')
            return render(request,'secy_add_equipments.html',context)
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")

def booking_manager(request): #hall manager
    if request.user.is_authenticated:
        if request.user.designation == "Hall Manager":
            context = {
                'query_results' : Guestroom.objects.all()
            }
            if request.method =="POST":
                username = request.POST.get('username')
                room = request.POST.get('room')
                action = request.POST.get('action')

                get_booking = Guestroom.objects.get(username=username,room=room)
                if action == "approve":
                    messages.success(request, 'The booking has been validated')
                else:
                    messages.success(request, 'The booking has been rejected')
                    get_booking.delete()

            return render(request,'booking_manager.html',context)
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")