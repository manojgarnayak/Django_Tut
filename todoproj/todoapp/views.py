from django.shortcuts import render
from todoapp.models import *
# Create your views here.

def todo(request):
    todos = TaskDetails.objects.all()
    d = {'todos': todos}
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description') 
        if title and description:
            taskObj = TaskDetails(title = title, description = description)
            taskObj.save()
    elif request.method == 'GET':
        sno = request.GET.get('sno')
        TaskDetails.objects.filter(sno=sno).delete()
        todos = TaskDetails.objects.all()
        d = {'todos': todos}
    return render(request, 'form.html', d)

sno = 0

def update(request):
    if request.method == 'GET':
        global sno
        sno = request.GET.get('sno')
        return render(request, 'update.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        TaskDetails.objects.filter(sno=sno).update(title=title, description=description)
        todos = TaskDetails.objects.all()
        d = {'todos':todos}
        return render(request, 'form.html', d)
    return render(request, 'update.html')