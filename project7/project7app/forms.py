from django import forms

gender = [['MALE', 'Male'], ["FEMALE", 'Female']]
courses = [['Python', 'PYTHON'], ['Sql', 'SQL'], ['Django', 'DJANGO']]
class StudentForm(forms.Form):
    student_name = forms.CharField(max_length=50, required=False)
    student_age = forms.IntegerField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=gender, widget=forms.RadioSelect)
    student_address = forms.CharField(widget=forms.Textarea(attrs={'cols':25,'rows':5}))
    courses = forms.MultipleChoiceField(choices=courses, widget=forms.CheckboxSelectMultiple)
    