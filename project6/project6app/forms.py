from django import forms
from project6app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'