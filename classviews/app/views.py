from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, FormView
from app.forms import *
# Create your views here.

def func_view(request):
    return HttpResponse('This is Function Based View which returns some text')

class class_view(View):
    def get(self, request):
        return HttpResponse('This is Class Based View which returns some text')
    

def func_template(request):
    return render(request, 'func_template.html')

class class_template(View):
    def get(self, request):
        return render(request, 'class_template.html')
    

class Template_view(TemplateView):
    template_name = 'class_template.html'


def functionbasedview(request):
    ESFO = SchoolForm()
    d = {'ESFO':ESFO}
    if request.method == 'POST':
        FO = SchoolForm(request.POST)
        if FO.is_valid():
            FO.save()
            return HttpResponse('School Created Successfully')
        return HttpResponse('Invalid Data')
    return render(request, 'functionbasedview.html', d)

class classbasedview(View):
    def get(self,request):
        ESFO = SchoolForm()
        d = {'ESFO':ESFO}
        return render(request, 'classbasedview.html', d)
    
    def post(self,request):
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('School Created Successfully using Class based views')
        return HttpResponse('Invalid Data')

class formviewtemplate(FormView):
    template_name = 'formviewtemplate.html'
    form_class = SchoolForm
    
    
    def form_valid(self, form):
        form.save()
        return HttpResponse('InsertSchoolBYFV is done')