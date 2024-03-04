from django.shortcuts import render
from project4app.models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fname')
        password = request.POST.get('password')
        email = request.POST.get('email')
        detailsobj = LoginDetail(fullname=fullname, password=password, email=email)
        detailsobj.save()
        return render(request, 'login.html')
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')