from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

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