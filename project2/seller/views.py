from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is seller home page')

def contact(request):
    return HttpResponse('This is seller contact page')