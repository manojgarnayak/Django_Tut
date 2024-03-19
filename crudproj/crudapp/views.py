from django.shortcuts import render
from crudapp.models import *
# Create your views here.

def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description') 
        taskObj = TaskDetails(title = title, description = description)
        taskObj.save()
    return render(request, 'form.html')