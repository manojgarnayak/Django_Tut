from django.shortcuts import render
from userapp.forms import *
# Create your views here.
def register(request):
    UFO = UserForm()
    PFO = ProfileForm()
    d = {'UFO': UFO, 'PFO': PFO}
    return render(request, 'register.html', d)