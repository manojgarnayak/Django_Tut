from django import forms
from imageapp.models import *

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'