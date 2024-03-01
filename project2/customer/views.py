from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is customer home page')

def contact(request):
    return HttpResponse('This is customer contact page')