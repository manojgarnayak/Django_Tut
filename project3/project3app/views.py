from django.shortcuts import render
from project3app.models import *
# Create your views here.
def landing(request):
    return render(request, 'landingpage.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        detailsobj = Details(username=username, password=password, email=email)
        detailsobj.save()
        return render(request, 'login.html')
    return render(request, 'register.html')

def contactus(request):
    return render(request, 'contactus.html')