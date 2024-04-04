from django.shortcuts import render
from app.models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class InsertSchool(CreateView):
    model = School
    fields = '__all__'
    success_url = reverse_lazy('InsertSchool')

class InsertStudent(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('InsertStudent')


def obj(request, sname):
    obj = School.objects.get(school_name = sname)
    d = {'obj':obj}
    return render(request, 'obj.html', d)