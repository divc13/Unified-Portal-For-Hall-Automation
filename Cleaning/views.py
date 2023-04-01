from django.shortcuts import render
from Cleaning.models import Cleaning_Request
from datetime import datetime
from django.contrib import messages


def Past_Request(request):
    # Displays completed cleaning requests raised by a user in the past
    if request.user.is_authenticated:
        if request.user.designation == "Student" :
            user_history = Cleaning_Request.objects.filter(User_Name=request.user.username, Done=True)
            # user_history is a QuerySet storing requests from the user
            return render(request, 'Past_Request.html', context= {'lodging': user_history})
        else:
            # If the user is not a student
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")
    
def Pending_Request(request):
    # Used to mark pending requests as complete
    if request.user.is_authenticated:
        if request.user.designation == "Student" :
            pending_list = Cleaning_Request.objects.filter(Done = False, User_Name=request.user.username)
            if request.method == 'POST':
                x = request.POST.get('identity')
                # used to identify which request is being marked as complete
                req=Cleaning_Request.objects.filter(id = int(x))[0]
                req.Done = True
                req.save()
                messages.success(request, "Your request has been removed from pending requests successfully")
            # After updating the database, the page reloads.
            return render(request, 'Pending_Request.html', context= {'lodging': pending_list, "messages": messages.get_messages(request)})

        else:
            return render(request,"Error.html")
    else: 
        return render(request,"Error.html")


def Lodge_Request(request):
    # Creates a Request object when a cleaning request is lodged
    if request.user.is_authenticated:
        if request.user.designation == "Student" :
            if request.method == 'POST' :
                place = request.POST.get("place")
                username =request.user.username
                room = request.POST.get('room')    
                comments=request.POST.get('comment')

                req_object = Cleaning_Request( 
                    User_Name=username,
                    Place=place,
                    Room=room,
                    comments=comments,
                    Cleaning_DateTime=datetime.now() )
                req_object.save()
                messages.success(request, "Your request has been sent!")
                return render(request, "Lodge_Request.html", context={"messages": messages.get_messages(request)})
            return render(request, "Lodge_Request.html")
        else:
            return render(request,"Error.html")
    else: return render(request,"Error.html")


def Cleaning_hall(request):
    if request.user.is_authenticated:
        if request.user.designation == "Hall Manager":
            request_list = Cleaning_Request.objects.filter( Done=False )
            return render(request, 'Cleaning_hall.html', context= {'lodging': request_list})
            # All requests made are displayed to the manager
        else:
            return render(request,"Error.html")
    else:
        return render(request,"Error.html")
