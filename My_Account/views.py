from django.shortcuts import render
from django.shortcuts import render
from Canteen.models import Bill as Canteen_Bill
from Mess.models import Bill as Mess_Bill

def Mess(request):
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            bill = Mess_Bill.objects.filter(User_Name = request.user.username).order_by('Bill_Month')
            return render(request, "Mess.html", context={'bills': bill})
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")
  
def Canteen(request):
    if request.user.is_authenticated:
        if request.user.designation == "Student":
            bill = 0
            if Canteen_Bill.objects.filter(User_Name = request.user.username):
                bill = Canteen_Bill.objects.filter(User_Name = request.user.username)[0].Amount
            return render(request, "Canteen.html", context= {'bill': bill})
        else:
            return render(request, "Error.html")
    else:
        return render(request, "Error.html")
