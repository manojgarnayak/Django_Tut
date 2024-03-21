from django.shortcuts import render, HttpResponse
from imageapp.forms import DetailsForm
# Create your views here.

def register(request):
    EDFO = DetailsForm()
    d = {'EDFO':EDFO}
    if request.method == 'POST' and request.FILES:
        DFDO = DetailsForm(request.POST, request.FILES)
        DFDO.save()
        return HttpResponse('User Registered Successfully')
    return render(request, 'register.html', d)