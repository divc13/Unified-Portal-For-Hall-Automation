from django.shortcuts import render

# Create your views here.

def Make_Homepage (request):
    # rendering the home page
    if request.user.is_authenticated:
        return render (request, 'Home.html')
    else:
        return render(request, "Error.html")