from django.shortcuts import render
from management_app.models import *
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    todos = Details.objects.all()
    d = {'todos': todos}
    if request.method == 'POST':
        patient_details = request.POST.get('name')
        phone = request.POST.get('phone')
        email_id = request.POST.get('email')
        disease_desc = request.POST.get('desc') 
        if patient_details and phone and email_id and disease_desc:
            taskObj = Details(patient_details = patient_details, phone = phone, email_id = email_id, disease_desc = disease_desc)
            taskObj.save()
    elif request.method == 'GET':
        sno = request.GET.get('sno')
        Details.objects.filter(sno=sno).delete()
        todos = Details.objects.all()
        d = {'todos': todos}
    return render(request, 'form.html', d)

sno = 0

def update(request):
    if request.method == 'GET':
        global sno
        sno = request.GET.get('sno')
        return render(request, 'update.html')
    elif request.method == 'POST':
        patient_details = request.POST.get('name')
        phone = request.POST.get('phone')
        email_id = request.POST.get('email')
        disease_desc = request.POST.get('desc')
        Details.objects.filter(sno=sno).update(patient_details = patient_details, phone = phone, email_id = email_id, disease_desc = disease_desc)
        todos = Details.objects.all()
        d = {'todos':todos}
        return render(request, 'form.html', d)
    return render(request, 'update.html')