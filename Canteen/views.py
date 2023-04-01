from django.shortcuts import render
from Canteen.models import Order
from Canteen.models import Bill
from Canteen.models import Menu
from django.contrib import messages
from datetime import datetime
from Login.models import User_class
from django.conf import settings
from django.core.mail import send_mail
import pytz

def Student_Place_Order(request):
    # helps student add item to their cart
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            menu = Menu.objects.all().exclude(Item_Name = "").exclude(Item_Name = "None")       # in case canteen manager is in the process of adding an item, dont show it to student
            if request.method == "POST":                        # add to cart
                quantity = int(request.POST.get("quantity"))
                idt = request.POST.get("submit")
                Add_item = Menu.objects.filter(id=idt)[0]
                if Order.objects.filter(Item_Name=Add_item.Item_Name, Cart_Status=True):        # if the item is already there in the cart
                    Item = Order.objects.filter(Item_Name=Add_item.Item_Name,Cart_Status = True)[0]
                    Item.Quantity += quantity
                    Item.Amount += Item.Price * quantity
                    Item.save()

                else:
                    order = Order(
                        User_Name=request.user.username,
                        Name=request.user.name,
                        Quantity=quantity,
                        Item_Name=Add_item.Item_Name,
                        Price=Add_item.Price,
                        Cart_Status=1,
                        Amount=quantity * Add_item.Price,
                        Order_Date_Time=datetime.now(),
                    )
                    order.save()
                messages.success(
                    request, "Your order has been successfully added to cart"
                )
            data = {"menu": menu, "messages": messages.get_messages(request)}
            return render(request, "Student_Place_Order.html", data)
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Student_Cart(request):
    # shows the cart to student
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            if request.method == "POST":
                if "order_validation1" in request.POST:             # remove item from cart
                    order = request.POST.get("order_validation1")
                    if Order.objects.filter(id=int(order)):
                        req = Order.objects.filter(id=int(order))[0]
                        req.delete()
                    messages.success(
                        request, "Your Cart Item has been successfully removed"
                    )
                if "order_validation2" in request.POST:             # in case student books the cart
                    orders = Order.objects.filter(Cart_Status=True)
                    if not orders:                                  # and it was empty
                        messages.error(
                        request, "Your Cart was Empty"
                        )
                    else:                                           # else send it to canteen manager
                        for obj in orders:
                            obj.Cart_Status = False
                            obj.Processing_Status = True
                            obj.save()
                        messages.success(
                            request, "Order request has been made to Canteen Manager"
                        )

            cart = Order.objects.filter(Cart_Status = True, User_Name = request.user.username)
            bill = 0
            for obj in cart:
                bill = bill + obj.Amount
            return render(
                request,
                "Student_Cart.html",
                context={
                    "carting": cart,
                    "bill": bill,
                    "messages": messages.get_messages(request),
                },
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Student_Pending_Order(request):
    # after the order is sent to canteen manager, student can look at his oder status here
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            order = Order.objects.filter(History_Status=False, Cart_Status=False, User_Name=request.user.username)
            return render(
                request, "Student_Pending_Order.html", context={"ordering": order}
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Student_Orders_History(request):
    # after the transaction was done with, student can see his previous orders in order history
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            order = Order.objects.filter(History_Status=True, Cart_Status=False, User_Name=request.user.username)
            return render(
                request, "Student_Orders_History.html", context={"ordering": order}
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Owner_New_Order(request):
    # the incoming orders are accepted/rejectede here
    if request.user.is_authenticated:
        if request.user.designation == "Canteen Manager":
            order1 = Order.objects.filter(Processing_Status=True)

            if request.method == "POST":

                if "accepted" in request.POST:                                      # if order was accepted
                    id = request.POST.get("accepted")
                    order = Order.objects.filter(id=int(id))[0]
                    order.Accepted_Status = 1
                    order.Processing_Status = 0
                    order.save()
                    bill=Bill.objects.filter(User_Name=order.User_Name)
                    if bill:                                                        # if a due already exists
                        bill[0].Amount = bill[0].Amount + order.Amount              # modify student dues
                        bill[0].save()
                    else:                                                           # else create an entry
                        bill=Bill(
                            User_Name=order.User_Name,
                            Name=order.Name,
                            Amount=order.Amount,
                        )
                        bill.save()
                    messages.success(request, "You accepted the order")
                elif "rejected" in request.POST:                                    # if the order was rejected, sends mail
                    id = request.POST.get("rejected")
                    order = Order.objects.filter(id=int(id))[0]
                    order.Accepted_Status = 0
                    order.History_Status = 1
                    order.Processing_Status = 0
                    order.save()
                    
                    username = order.User_Name
                    name = User_class.objects.filter(username=username)[0].name
                    dt = order.Order_Date_Time.astimezone(pytz.timezone('Asia/Kolkata'))
                    dt = dt.strftime("%Y-%m-%d %H:%M:%S")
                    subject = "Order Rejected"
                    message = f"Dear {name}, Your order, made on {dt}, with items {order.Item_Name} has been rejected. We deeply regret this. Contact the canteen manager."
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [
                        f"{username}@iitk.ac.in",
                    ]
                    send_mail(subject, message, email_from, recipient_list)
                    
                    
                    messages.error(request, "You rejected the order")

                return render(
                    request,
                    "Owner_New_Order.html",
                    context={
                        "pending_orders": order1,
                        "messages": messages.get_messages(request),
                    },
                )
            return render(
                request, "Owner_New_Order.html", context={"pending_orders": order1}
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Owner_Pending_Order(request):
    # helps owner change the status of order which were accepted
    if request.user.is_authenticated:
        if request.user.designation == "Canteen Manager":
            order = Order.objects.filter(Processing_Status=False, History_Status=False, Accepted_Status=True)
            if request.method == "POST":
                if "served" in request.POST:                                            # if the order was server
                    id = request.POST.get("served")
                    pending_orders = Order.objects.filter(id=int(id))[0]
                    pending_orders.Served_Status = 1                                    # update status
                    if pending_orders.Payment_Status == 1:
                        pending_orders.History_Status = 1
                    pending_orders.save()
                    messages.success(request, "updated served status")
                if "paid" in request.POST:                                              # if student paid
                    id = request.POST.get("paid")
                    pending_orders = Order.objects.filter(id=int(id))[0]
                    pending_orders.Payment_Status = 1                                   # update status
                    if pending_orders.Served_Status == 1:
                        pending_orders.History_Status = 1
                    pending_orders.save()
                    bill=Bill.objects.filter(User_Name = pending_orders.User_Name)[0]
                    bill.Amount = bill.Amount - pending_orders.Amount                   # update bill
                    bill.save()
                    messages.success(request, "Payment status updated.")

                if "remove" in request.POST:                                            # if the transaction was completed
                    id = request.POST.get("remove")
                    pending_orders = Order.objects.filter(id=int(id))[0]
                    if pending_orders.Served_Status == False:
                        messages.error(request, "Order is not served, so cannot be removed.")
                    else:
                        pending_orders.History_Status = 1
                        pending_orders.save()
                        messages.success(request, "Transaction Completed")

            return render(
                request,
                "Owner_Pending_Order.html",
                context={
                    "pending_order": order,
                    "messages": messages.get_messages(request),
                },
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Owner_Modify_Menu(request):
    # helps owner modify the canteen menu
    if request.user.is_authenticated:
        if request.user.designation == "Canteen Manager":
            extras = Menu.objects.all()
            if request.method == "POST":
                if "add_hidden_item" in request.POST:                               # if owner wants to add an item
                    if "editable_mode" in request.POST:                             # and he was editing the menu
                        for obj in Menu.objects.all():                              # first update all items
                            item = request.POST.get("item" + str(obj.id))
                            if item is not None:
                                price = request.POST.get("price" + str(obj.id))
                                extra_items = Menu.objects.filter(id=obj.id)[0]
                                extra_items.Item_Name = item
                                extra_items.Price = price
                                extra_items.save()
                            else:
                                obj.delete()
                    extra_items1 = Menu()
                    extra_items1.save()
                    idt = extra_items1.id
                    return render(
                        request,
                        "Owner_Modify_Menu.html",
                        context={"extra_item": extras, "status_check": 1},
                    )

                if "submit" in request.POST:                                        # if owner saves the changes
                    for obj in Menu.objects.all():
                        item = request.POST.get("item" + str(obj.id))
                        if item is not None:
                            price = request.POST.get("price" + str(obj.id))
                            extra_items = Menu.objects.filter(id=obj.id)[0]
                            extra_items.Item_Name = item
                            extra_items.Price = price
                            extra_items.save()
                        else:
                            obj.delete()
                    return render(
                        request,
                        "Owner_Modify_Menu.html",
                        context={"extra_item": extras, "status_check": 0},
                    )

                elif "edit" in request.POST:                                        # if owner clicks on edit
                    return render(
                        request,
                        "Owner_Modify_Menu.html",
                        context={"extra_item": extras, "status_check": 1},
                    )

                elif "delete" in request.POST:                                      # if owner delets an item from the menu
                    idt = request.POST.get("delete")
                    if "editable_mode" in request.POST:                             # and the owner was in edit mode
                        for obj in Menu.objects.all():
                            item = request.POST.get("item" + str(obj.id))
                            if item is not None:
                                price = request.POST.get("price" + str(obj.id))
                                extra_items = Menu.objects.filter(id=obj.id)[0]
                                extra_items.Item_Name = item
                                extra_items.Price = price
                                extra_items.save()
                            else:
                                obj.delete()
                    if Menu.objects.filter(id=idt):
                        extra_items_del = Menu.objects.filter(id=idt)[0]
                        extra_items_del.delete()
                    return render(
                        request,
                        "Owner_Modify_Menu.html",
                        context={"extra_item": extras, "status_check": 0},
                    )

            else:
                return render(
                    request, "Owner_Modify_Menu.html", context={"extra_item": extras}
                )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")


def Owner_Students_Bill(request):
    # in case owner clears dues of a student
    if request.user.is_authenticated:
        if request.user.designation == "Canteen Manager":
            if request.method == "POST":
                clear_dues_amount = request.POST.get("order_validation1")
                username = request.POST.get("submit")
                req = Bill.objects.filter(User_Name=username)[0]
                dues = req.Amount
                unpaid_amount = int(dues) - int(clear_dues_amount)
                req.Amount = unpaid_amount
                req.save()                                              # update the bill
                messages.success(request, "Dues Successfully Updated")
                bill = Bill.objects.exclude(Amount=0)
                return render(
                    request,
                    "Owner_Students_Bill.html",
                    context={
                        "billing": bill,
                        "messages": messages.get_messages(request),
                    },
                )
            bill = Bill.objects.exclude(Amount=0)
            return render(
                request, "Owner_Students_Bill.html", context={"billing": bill}
            )
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")
