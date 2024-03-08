from django import forms

gender = [['MALE', 'Male'], ['FEMALE', 'Female']]
courses = [['PYTHON','Python'], ['DJANGO','Django'], ['SQL','Sql'], ['WEB DEV', 'Web Dev']]

class StudentForm(forms.Form):
    Student_Name = forms.CharField(max_length=20, required=False)
    Student_Age = forms.IntegerField(required=False)
    Password = forms.CharField(widget=forms.PasswordInput)
    Gender = forms.ChoiceField(widget=forms.RadioSelect, choices = gender)
    Courses = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = courses)
    Student_Address = forms.CharField(widget=forms.Textarea(attrs={'col': 25, 'rows': 5}))
    
