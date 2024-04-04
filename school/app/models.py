from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=50, primary_key=True)
    principal = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return self.school_name
    
class Student(models.Model):
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_age = models.IntegerField()

    def __str__(self):
        return self.student_name