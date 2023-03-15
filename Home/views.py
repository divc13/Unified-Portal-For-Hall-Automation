from django.shortcuts import render

# Create your views here.

def Make_Homepage (request):
    if request.user.is_authenticated:
        return render (request, 'Home.html')
    else:
        return render(request, "Error.html")