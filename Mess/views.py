import calendar
from django.db.models import Q
from datetime import datetime
from django.conf import settings
from dateutil.rrule import rrule, DAILY
from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import render
from django.core.mail import send_mail
from Mess.models import Regular_menu
from Mess.models import Extras
from Mess.models import Orders
from Mess.models import Datewise_BDMR
from Mess.models import Bill
from Mess.models import Rebate
from Mess.models import Rating_Regular
from Login.models import User_class


def Student_Regular_Menu(request):
    # Displaying the regular menu to the students.
    if request.user.is_authenticated:
        if request.user.designation == "Student":

            regular_menu = Regular_menu.objects.all().exclude(Items = "").exclude(Items = "None").order_by("Day_Number","Meal_Number")
            if request.method == "POST":        # gets rating from the form

                id_list = []
                average_rating = 0

                for item in regular_menu:

                    if ("rating" + str(item.id)) in request.POST:

                        value = request.POST.get("rating" + str(item.id))

                        rating_objects = Rating_Regular.objects.filter(
                            Day=item.Day,
                            Meal=item.Meal,
                            User_Name=request.user.username,
                        )

                        if rating_objects:      #updating previous rating

                            rating_obj = rating_objects[0]
                            rating_obj.Rating_Value = value
                            rating_obj.save()

                        else:                   # making a new rating object if not present

                            rating_obj = Rating_Regular(
                                Meal=item.Meal,
                                Day=item.Day,
                                User_Name=request.user.username,
                            )
                            rating_obj.Rating_Value = value
                            rating_obj.save()

                        objects = Rating_Regular.objects.filter(        # updating the average rating
                            Meal=item.Meal, Day=item.Day
                        )
                        Review_Count = 0
                        Review_Total = 0
                        for obj1 in objects:
                            Review_Count += 1
                            Review_Total += obj1.Rating_Value

                        if Review_Count:
                            average_rating = Review_Total / Review_Count

                        item.Rating = average_rating
                        item.save()

                    rating_objects = Rating_Regular.objects.filter(
                        Day=item.Day, Meal=item.Meal, User_Name=request.user.username
                    )

                    if rating_objects:

                        for obj in rating_objects:
                            id_list.append(obj.id)

                return render(
                    request,
                    "Student_Regular_Menu.html",
                    context={"menu": regular_menu, "id_list": id_list},
                )

            return render(
                request, "Student_Regular_Menu.html", context={"menu": regular_menu}
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Student_Book_Extras(request):

    if request.user.is_authenticated:
        if request.user.designation == "Student":
            # Processes requests to purchase extras by students
            extras = Extras.objects.all().exclude(Item_Name = "").exclude(Item_Name = "None").order_by(
                "-Start_Time"
            )  # QuerySet containing all extras

            if request.method == "POST":

                quantity = int(request.POST.get("quantity"))  # number requested
                idt = request.POST.get("identity")
                order = Extras.objects.filter(id=idt)[0]  # key of the item ordered
                if (
                    int(order.Available_Orders) >= quantity
                    and datetime.now().timestamp() > order.Start_Time.timestamp()
                    and datetime.now().timestamp() < order.End_Time.timestamp()
                ):
                    # order is placed if the re - quantityquired number is available and the booking window is open
                    order.Available_Orders = order.Available_Orders

                    pending_order = Orders(
                        Meal=order.Meal,
                        Order_Date_Time=datetime.now(),
                        Meal_Date=order.Meal_Date,
                        User_Name=request.user.username,
                        Item_Name=order.Item_Name,
                        Quantity=quantity,
                        Price=order.Price,
                        Amount=quantity * order.Price,
                    )

                    order.save()
                    pending_order.save()

                    bill_objects = Bill.objects.filter(
                        User_Name=pending_order.User_Name,
                        Bill_Month=pending_order.Order_Date_Time.month,
                    )

                    if not bill_objects:
                        # if it is the first order of the month from the user a new instance of Bill is initialised
                        bill = Bill(
                            User_Name=pending_order.User_Name,
                            Bill_Month=pending_order.Order_Date_Time.month,
                        )
                        bill.Extras_Amount = pending_order.Amount
                        bill.Month_Name = calendar.month_name[bill.Bill_Month]
                        bill.messbillcalc()
                        bill.save()

                    else:
                        # else the corresponding Bill object is updated
                        bill = bill_objects[0]
                        bill.Extras_Amount += pending_order.Amount
                        bill.Month_Name = calendar.month_name[bill.Bill_Month]
                        bill.messbillcalc()
                        bill.save()

                    messages.success(request, "Order Booked")

                else:
                    messages.error(request, "Order cannot be booked now")

            return render(
                request,
                "Student_Book_Extras.html",
                context={
                    "extra_items": extras,
                    "messages": messages.get_messages(request),
                },
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Student_Booked_Extras(request):
    # marks booked extras as delivered
    if request.user.is_authenticated:
        if request.user.designation == "Student":

            orders = Orders.objects.filter(
                History_Status=False, User_Name=request.user.username
            ).order_by("-Order_Date_Time")

            if request.method == "POST":                            # order is sent to history after validating
                idt = request.POST.get("order_validation")
                pending_order = Orders.objects.filter(id=idt)[0]
                pending_order.History_Status = True
                pending_order.save()
                messages.success(request, "Order Validated")

            for obj in orders:
                if obj.Meal_Date.timetuple() < datetime.now().date().timetuple():
                    obj.delete()
                    # order object is deleted if not validated at the meal date

            return render(
                request,
                "Student_Booked_Extras.html",
                context={
                    "pending_orders": orders,
                    "messages": messages.get_messages(request),
                },
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Student_Apply_For_Rebate(request):
    # Processes rebate requests raised by students
    # initialises Rebate object
    if request.user.is_authenticated:
        if request.user.designation == "Student":

            if request.method == "POST":

                from_date = datetime.strptime(str(request.POST.get("from")), "%Y-%m-%d")
                to_date = datetime.strptime(str(request.POST.get("to")), "%Y-%m-%d")
                
                if from_date <= to_date:

                    if Rebate.objects.filter(Date_From=from_date,Date_To=to_date,User_Name=request.user.username,status = 1) or Rebate.objects.filter(Date_From=from_date,Date_To=to_date,User_Name=request.user.username,status = 0):
                        messages.error(request,
                        "You have already applied for rebate for same duration.",)
                        
                        
                    else:
                        rebate_request = Rebate(
                            Date_From=from_date,
                            Date_To=to_date,
                            User_Name=request.user.username,
                        )
                        rebate_request.Rebate_Days = rebate_request.date_diff()
                        rebate_request.save()
                        messages.success(
                            request,
                            "Your rebate request has been sent to the mess manager. You will soon receive a confirmation email.",
                        )
                
                else :
                    messages.error(
                        request,
                        "From-Date must be less than equal to To-Date",
                    )

            return render(
                request,
                "Student_Apply_For_Rebate.html",
                context={
                    "currentdate": datetime.today,
                    "messages": messages.get_messages(request),
                },
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")
    
def Student_Applied_Rebate(request):
    # Used to accept/reject pending rebate requests
    if request.user.is_authenticated:
        if request.user.designation == "Student":

            requests = Rebate.objects.all().order_by("-Date_From", "status")
            return render(
                request, "Student_Applied_Rebate.html", context={"req": requests,"messages": messages.get_messages(request)}
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Student_Order_History(request):
    # displays previous orders made by a student on request
    if request.user.is_authenticated:

        if request.user.designation == "Student":
            past_orders = Orders.objects.filter(
                History_Status=True, User_Name=request.user.username
            ).order_by("Order_Date_Time")
            return render(
                request,
                "Student_Order_History.html",
                context={"order_history": past_orders},
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Manager_Modify_Menu(request):
    # stores changes to the regular menu made by the mess manager
    if request.user.is_authenticated:
        if request.user.designation == "Mess Manager":

            regularmenu = Regular_menu.objects.order_by("Day_Number","Meal_Number")

            if request.method == "POST":
                
                
                if (
                    ("submit" in request.POST)
                    or (
                        "add_hidden_item" in request.POST
                        and "editable_mode" in request.POST
                    )
                    or ("delete" in request.POST and "editable_mode" in request.POST)
                ):
                    # Commits changes to the database
                    
                    Day_Choices = {
                            "Sunday": 0,
                            "Monday": 1,
                            "Tuesday": 2,
                            "Wednesday": 3,
                            "Thursday": 4,
                            "Friday": 5,
                            "Saturday": 6,
                    }
                    
                    Meal_Choices = {
                            "Breakfast": 0,
                            "Lunch": 1,
                            "Dinner": 2,
                    }

                    for obj in Regular_menu.objects.all():  
                        
                        item = request.POST.get("item" + str(obj.id))
                        if item is not None:
                            day = request.POST.get("day" + str(obj.id))
                            meal = request.POST.get("meal" + str(obj.id))
                            if Regular_menu.objects.filter(id=obj.id):
                                menu = Regular_menu.objects.filter(id=obj.id)[0]
                                menu.Day = day
                                menu.Day_Number = Day_Choices[day]
                                menu.Meal_Number = Meal_Choices[meal]
                                menu.Items = item
                                menu.Meal = meal
                                menu.save()
                        else:
                            obj.delete()
                            

                if "add_hidden_item" in request.POST:           # makes a field which mess manager will have to fill

                    for item1 in Regular_menu.objects.all():
                        for item2 in Regular_menu.objects.all():
                            if item1.id != item2.id:
                                if (item1.Day == item2.Day) and (item1.Meal == item2.Meal) and (item1.Items == item2.Items):
                                    if item1:
                                        item1.delete()
                                        break
                                    
                    obj = Regular_menu(Day = "Sunday")
                    obj.save()
                    return render(
                        request,
                        "Manager_Modify_Menu.html",
                        context={"regularmenu": regularmenu, "status_check": 1},
                    )

                elif "submit" in request.POST:                  # the changes were stored hence render message
                    
                    for item1 in Regular_menu.objects.all():
                        for item2 in Regular_menu.objects.all():
                            if item1.id != item2.id:
                                if (item1.Day == item2.Day) and (item1.Meal == item2.Meal) and (item1.Items == item2.Items):
                                    if item1:
                                        item1.delete()
                                        break

                    messages.success(request, "Changes made successfully.")
                    return render(
                        request,
                        "Manager_Modify_Menu.html",
                        context={
                            "regularmenu": regularmenu,
                            "status_check": 0,
                            "messages": messages.get_messages(request),
                        },
                    )

                elif "edit" in request.POST:                    # status_check makes the menu editable

                    return render(
                        request,
                        "Manager_Modify_Menu.html",
                        context={"regularmenu": regularmenu, "status_check": 1},
                    )

                elif "delete" in request.POST:                  # deletes the item with id as idt
                    idt = request.POST.get(
                        "delete"
                    )
                    if Regular_menu.objects.filter(id=idt):
                        menu_del = Regular_menu.objects.filter(id=idt)[0]
                        menu_del.delete()
                        
                    for item1 in Regular_menu.objects.all():
                        for item2 in Regular_menu.objects.all():
                            if item1.id != item2.id:
                                if (item1.Day == item2.Day) and (item1.Meal == item2.Meal) and (item1.Items == item2.Items):
                                    if item1:
                                        item1.delete()
                                        break

                    messages.success(request, "Deleted Successfully")
                    return render(
                        request,
                        "Manager_Modify_Menu.html",
                        context={
                            "regularmenu": regularmenu,
                            "status_check": 0,
                            "messages": messages.get_messages(request),
                        },
                    )

            else:
                return render(
                    request, "Manager_Modify_Menu.html", context={"regularmenu": regularmenu}
                )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Manager_Extra_Items(request):
    # Adds extras to the weekly menu
    if request.user.is_authenticated:
        if request.user.designation == "Mess Manager":

            extras = Extras.objects.all().order_by("-Start_Time")

            if request.method == "POST":
                
                flag = 0

                if (
                    ("submit" in request.POST)
                    or (
                        "add_hidden_item" in request.POST
                        and "editable_mode" in request.POST
                    )
                    or ("delete" in request.POST and "editable_mode" in request.POST)
                ):
                    # Commits changes to the database

                    for obj in Extras.objects.all():  # for obj in extras?
                        
                        meal_date = request.POST.get("meal_date" + str(obj.id))
                        if meal_date is not None:

                            meal_date = datetime.strptime(str(meal_date), "%Y-%m-%d")
                            meal = request.POST.get("meal" + str(obj.id))
                            item = request.POST.get("item" + str(obj.id))
                            capacity = request.POST.get("capacity" + str(obj.id))
                            price = request.POST.get("price" + str(obj.id))

                            start_time = request.POST.get("start_time" + str(obj.id))
                            start_time = datetime.strptime(
                                str(start_time), "%Y-%m-%dT%H:%M"
                            )
                            end_time = request.POST.get("end_time" + str(obj.id))
                            end_time = datetime.strptime(str(end_time), "%Y-%m-%dT%H:%M")
                            
                            if meal_date.date()<end_time.date():            # checks the time
                                if flag == 0:
                                    messages.error(request, "Meal date must be greater than end time.")
                                flag = 1
                                continue
                            
                            if start_time > end_time:                       # checks the time
                                if flag == 0:
                                    messages.error(request, "Start time must be less than end time.")
                                flag = 1
                                continue
                            
                            else:
                                extra_items = Extras.objects.filter(id=obj.id)[0]
                                extra_items.Meal = meal
                                extra_items.Meal_Date = meal_date
                                extra_items.Item_Name = item
                                extra_items.Capacity = capacity
                                extra_items.Price = price
                                extra_items.Start_Time = start_time
                                extra_items.End_Time = end_time
                                extra_items.Available_Orders = capacity

                                extra_items.save()
                                
                        else:
                            obj.delete()

                if "add_hidden_item" in request.POST:               # makes an entry which will be filled by mes manager
                    
                    for item1 in Extras.objects.all():
                        for item2 in Extras.objects.all():
                            if item1.id != item2.id:
                                if (item1.Meal_Date == item2.Meal_Date) and (item1.Meal == item2.Meal) and (item1.Item_Name == item2.Item_Name):
                                    if item1:
                                        item1.delete()
                                        break

                    obj = Extras(Meal_Date =  datetime.today(),Start_Time = datetime.now(),End_Time = datetime.now())
                    obj.save()
                    return render(
                        request,
                        "Manager_Extra_Items.html",
                        context={"extra_item": extras, "status_check": 1},
                    )

                elif "submit" in request.POST:
                    for item1 in Extras.objects.all():
                        for item2 in Extras.objects.all():
                            if item1.id != item2.id:
                                if (item1.Meal_Date == item2.Meal_Date) and (item1.Meal == item2.Meal) and (item1.Item_Name == item2.Item_Name):
                                    if item1:
                                        item1.delete()
                                        break
                    if flag:
                        return render(
                            request,
                            "Manager_Extra_Items.html",
                            context={
                                "extra_item": extras,
                                "status_check": 1,
                                "messages": messages.get_messages(request),
                            },
                        )
                    else :
                        messages.success(request, "Changes made successfully.")
                        return render(
                            request,
                            "Manager_Extra_Items.html",
                            context={
                                "extra_item": extras,
                                "status_check": 0,
                                "messages": messages.get_messages(request),
                            },
                        )

                elif "edit" in request.POST:                        # status checks make the menu editable

                    return render(
                        request,
                        "Manager_Extra_Items.html",
                        context={"extra_item": extras, "status_check": 1},
                    )

                elif "delete" in request.POST:
                    # to delete extras from the weekly menu
                    idt = request.POST.get(
                        "delete"
                    )  # idt is the key of the object to be deleted
                    if Extras.objects.filter(id=idt):
                        extra_items_del = Extras.objects.filter(id=idt)[0]
                        extra_items_del.delete()
                    
                    for item1 in Extras.objects.all():
                        for item2 in Extras.objects.all():
                            if item1.id != item2.id:
                                if (item1.Meal_Date == item2.Meal_Date) and (item1.Meal == item2.Meal) and (item1.Item_Name == item2.Item_Name):
                                    if item1:
                                        item1.delete()
                                        break

                    messages.success(request, "Deleted Successfully")
                    return render(
                        request,
                        "Manager_Extra_Items.html",
                        context={
                            "extra_item": extras,
                            "status_check": 0,
                            "messages": messages.get_messages(request),
                        },
                    )

            else:
                return render(
                    request, "Manager_Extra_Items.html", context={"extra_item": extras}
                )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Manager_Rebate_Requests(request):
    # Used to accept/reject pending rebate requests
    if request.user.is_authenticated:
        if request.user.designation == "Mess Manager":

            requests = Rebate.objects.filter(
                status=0
            )  # "rebate" is a QuerySet storing all pending rebate requests

            if request.method == "POST":
                if "accept" in request.POST:
                    # for requests that are accepted
                    idt = request.POST.get("accept")
                    rebate = Rebate.objects.filter(id=idt)[0]

                    # An email is sent to the student
                    username = rebate.User_Name
                    name = User_class.objects.filter(username=username)[0].name
                    fromdt = rebate.Date_From
                    todt = rebate.Date_To
                    rebate_days = rebate.Rebate_Days
                    subject = "Rebate Request Accepted"
                    message = f"Dear {name}, Your rebate request for a period of {rebate_days} days has been accepted."
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [
                        f"{username}@iitk.ac.in",
                    ]
                    send_mail(subject, message, email_from, recipient_list)

                    # Database is updated
                    rebate.status = 1
                    rebate.save()
                    
                    messages.success(request,"Rebate Request Accepted.")

                    for dt in rrule(DAILY, dtstart=fromdt, until=todt):

                        bill_objects = Bill.objects.filter(
                            User_Name=username, Bill_Month=dt.month,Year = dt.year,
                        )

                        if not bill_objects:
                            # If there is no Bill object corresponding to the student, an instance is initialised
                            bill = Bill(
                                User_Name=username,
                                Bill_Month=dt.month,
                                Year = dt.year,
                            )
                            bill.rebate_days += 1
                            bill.Month_Name = calendar.month_name[bill.Bill_Month]
                            bill.messbillcalc()
                            bill.save()

                        else:
                            # If a Bill object is present, then it is updated
                            bill = bill_objects[0]
                            bill.rebate_days += 1
                            bill.Month_Name = calendar.month_name[bill.Bill_Month]
                            bill.messbillcalc()
                            bill.save()

                elif "reject" in request.POST:
                    messages.success(request,"Rebate Request Rejected.")
                    # For requests that are rejected
                    idt = request.POST.get("reject")
                    rebate = Rebate.objects.filter(id=idt)[0]

                    username = rebate.User_Name
                    name = User_class.objects.filter(username=username)[0].name
                    fromdt = rebate.Date_From
                    todt = rebate.Date_To
                    rebate_days = rebate.Rebate_Days
                    subject = "Rebate Request Rejected"
                    message = f"Dear {name}, Your rebate request for a period of {rebate_days} days has been rejected."
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [
                        f"{username}@iitk.ac.in",
                    ]
                    send_mail(
                        subject, message, email_from, recipient_list
                    )  # Sends emails to the user

                    rebate.status = 2
                    rebate.save()  # Updates database

            return render(
                request, "Manager_Rebate_Requests.html", context={"req": requests,"messages": messages.get_messages(request)}
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Manager_Past_Rebate(request):
    # Used to accept/reject pending rebate requests
    if request.user.is_authenticated:
        if request.user.designation == "Mess Manager":

            requests = Rebate.objects.filter(
                Q(status = 1)| Q(status = 1)
            ) # "rebate" is a QuerySet storing all pending rebate requests

            return render(
                request, "Manager_Past_Rebate.html", context={"req": requests,"messages": messages.get_messages(request)}
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")
    
    

def Manager_Students_Bills(request):
    # Used to clear dues from the database when a student pays the mess dues
    if request.user.is_authenticated:
        if request.user.designation == "Mess Manager":
            bill = Bill.objects.all().order_by("Year","Bill_Month","User_Name")
            if request.method == "POST":
                key = request.POST.get("clear_dues")
                if Bill.objects.filter(id=key):
                    billObject = Bill.objects.filter(id=key)[0]
                    billObject.delete()
                # The Bill object corresponding to the mess dues of a student for a particular month
                # is deleted when payment is confirmed by the mess manager
                messages.success(request, "Dues cleared successfully")

            return render(
                request,
                "Manager_Students_Pending_Bills.html",
                context={"bills": bill, "messages": messages.get_messages(request)},
            )
        else:
            return (request, "Error.html")
    else:
        return (request, "Error.html")


def Manager_View_Orders(request):
    if request.user.designation == "Mess Manager":
        to_deliver = Orders.objects.filter(History_Status=False)
        # to_deliver QuerySet storing orders that have been placed but have not been served
        return render(
            request, "Manager_View_Orders.html", context={"orders": to_deliver}
        )
    else:
        return render(request, "Error.html")


def Manager_View_Feedback(request):
    # Generetes a webpage containing feedback for the mess manager
    if request.user.is_authenticated:
        if request.user.designation == "Mess Manager":

            regular_menu = Regular_menu.objects.all()
            return render(
                request,
                "Manager_View_Feedback.html",
                context={"regular_menu": regular_menu},
            )

        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Manager_Modify_BDMR(request):
    if request.user.is_authenticated:
        if request.user.designation == "Mess Manager":

            if request.method == "POST":
                    
                if "bdmr_submit" in request.POST:
                    bdmr = request.POST.get("BDMR")
                    date = request.POST.get("bdmr_submit")
                    date = datetime.strptime(str(date), "%Y-%m-%d")
                    for obj in User_class.objects.filter(designation="Student"):
                        # The Bill object corresponding to each student is modified when the BDMR of a day is uploaded/updated
                        bill_objects = Bill.objects.filter(
                            User_Name=obj.username, Bill_Month=date.month,Year = date.year,
                        )
                        
                        if not bill_objects:
                            # If the Bill object corresponding to the user for the current month has not been initialised
                            # it is done when the BDMR is being saved
                            bill = Bill(
                                User_Name=obj.username,
                                Bill_Month=date.month,
                                Year = date.year,
                            )
                            bdmr_obj = Datewise_BDMR.objects.filter(Date=date)
                            if not bdmr_obj:
                                # if the BDMR is being uploaded instead of updated
                                bill.Basic_Amount += float(bdmr)
                            else:
                                bill.Basic_Amount += float(bdmr) - bdmr_obj[0].BDMR

                            bill.Total_Days = 1
                            bill.Month_Name = calendar.month_name[bill.Bill_Month]
                            bill.messbillcalc()
                            bill.save()

                        else:
                            # If a Bill object has been generated for the user

                            bill = bill_objects[0]
                            bdmr_obj = Datewise_BDMR.objects.filter(Date=date)
                            if not bdmr_obj:
                                bill.Basic_Amount += float(bdmr)
                            else:
                                bill.Basic_Amount += float(bdmr) - bdmr_obj[0].BDMR

                            bill.Total_Days += 1
                            bill.Month_Name = calendar.month_name[bill.Bill_Month]
                            bill.messbillcalc()
                            bill.save()

                    # A "Datewise_BDMR" object is generated/updated
                    date_and_bdmr = Datewise_BDMR(
                        Date=date,
                        BDMR=bdmr,
                    )
                    date_and_bdmr.save()

                    messages.success(request, "BDMR modified")
                    
                    return render(
                        request,
                        "Manager_Modify_BDMR.html",
                        context={"messages": messages.get_messages(request)},
                    )

                if "BDMR_Date" in request.POST:
                    date = request.POST.get("BDMR_Date")
                    date = datetime.strptime(str(date), "%Y-%m-%d")
                    if Datewise_BDMR.objects.filter(Date = date):
                        amt = Datewise_BDMR.objects.filter(Date = date)[0].BDMR
                    else:
                        amt = 0
                    return render(
                        request,
                        "Manager_Modify_BDMR.html",
                        context={"messages": messages.get_messages(request),"date":date,"amount":amt},
                    )
            return render(
                request,
                "Manager_Modify_BDMR.html",
                context={"messages": messages.get_messages(request)},
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")
