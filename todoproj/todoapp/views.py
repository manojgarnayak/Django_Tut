from django.shortcuts import render
from todoapp.models import *
from datetime import time
# Create your views here.

def todo(request):
    todos = TaskDetails.objects.all()
    d = {'todos': todos}
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description') 
        if title and description:
            taskObj = TaskDetails(title = title, description = description, date = time.today())
            taskObj.save()
    return render(request, 'form.html', d)