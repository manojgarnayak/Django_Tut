from django.db import models

# Create your models here.
gender = [['MALE', 'Male'], ["FEMALE", 'Female']]
courses = [['Python', 'PYTHON'], ['Sql', 'SQL'], ['Django', 'DJANGO']]

class Student(models.Model):
    student_name=models.CharField(max_length=100)
    student_age=models.IntegerField()
    password=models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    student_address=models.CharField(max_length=50)
    courses=models.CharField(max_length=50)