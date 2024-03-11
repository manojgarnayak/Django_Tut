
from django.shortcuts import render, HttpResponse
from project7app.models import *
from project7app.forms import *

# Create your views here.
def sform(request):
    SFO = StudentForm()
    d = {'SFO':SFO}
    if request.method == 'POST':
        student_name=request.POST.get('student_name')
        student_age=request.POST.get('student_age')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        student_address=request.POST.get('student_address')
        courses=request.POST.get('course')
        SO = Student(student_name=student_name, student_age=student_age, password=password, gender=gender, student_address=student_address,courses=courses)
        SO.save()
        return HttpResponse('Student Created Successfully')
    return render(request, 'form.html',d)