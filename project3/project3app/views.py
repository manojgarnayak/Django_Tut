from django.shortcuts import render

# Create your views here.
def home(request):
    d = {
        'name' : 'manoj',
        'age' : 23
    }
    return render(request, 'home.html', d)

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        return render(request, 'login.html')
    return render(request, 'register.html')

def contactus(request):
    return render(request, 'contactus.html')