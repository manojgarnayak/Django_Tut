from django.shortcuts import render
from project5app.forms import *
# Create your views here.

def form(request):
    FormObj = StudentForm()
    context = {'FormObj': FormObj}
    return render(request, 'myform.html', context)